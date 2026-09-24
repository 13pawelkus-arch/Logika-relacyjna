"""
MASA — kandydat 2 przy WEWNETRZNEJ regule kontynuacji (Colab: edytuj stale na gorze).

Poprzednie porazki: czestosc samoodczytu zalezala od predkosci, bo moja regula budowy trajektorii
odwolywala sie do ukladu pudla (okno w czasie wspolrzednosciowym, kierunek z zewnatrz).
TU: trajektoria kontynuuje sie PAMIECIA — nastepny element maksymalizuje czas wlasny liczony
od elementu PRZEDOSTATNIEGO (najmniejsze zakrzywienie linii). Regula czysto porzadkowa,
nie zna zadnego ukladu; predkosc pochodzi z dwoch pierwszych elementow i jest niesiona dalej.

MIERZONE: czestosc tyknięc = (liczba krokow)/(suma czasow wlasnych krokow) = 1/<tau_krok>.
ZDANIA DO UPADKU:
  M0a. inicjalizacja: to samo tyknięcie poczatkowe dla wszystkich (inaczej korelacja jest artefaktem)
  M0. regula wewnetrzna NIE hamuje: rozklad predkosci na koncu podobny do poczatkowego
      (poprzednia wersja, sam max czasu wlasnego do przodu, sciagala wszystko do 0,01-0,13)
  M1. czestosc NIE zalezy od predkosci wzgledem tla: |korelacja| < 0,05 i stosunek szybkie/wolne 1,00 +- 0,05
  M2. czestosc jest stabilna wzdluz trajektorii: korelacja polowa-polowa > 0,5
  M3. KONTROLA (regula zewnetrzna, okno w czasie wspolrzednosciowym): korelacja z predkoscia
      istotnie DODATNIA (odtworzenie +0,333 z CPU) - pokazuje, ze roznica bierze sie z reguly
Odniesienie z CPU: regula zewnetrzna dawala korelacje +0,333 i stosunek 1,39.
"""
import numpy as np, json, os, time
try:
    import cupy as cp; XP = cp; GPU = True
except ImportError:
    XP = np; GPU = False

T_, S_ = 16.0, 6.0     # wyzsza tuba: przy L=20 trajektoria nie moze wyjsc gora (obserwacja: nagly zgon wszystkich na kroku ~10 przy T=10)
N      = 19_000_000    # gestosc dobrana tak, by okno tau zostalo ~0,36 mimo wyzszej tuby
K      = 20_000
L      = 20
KAND   = 12
BUCKET = 64
SEEDS  = [1, 2]
CKPT   = "etap7_masa.json"
WERSJA = "v4"          # znacznik wersji reguly: po zmianie regul stare wyniki nie blokuja przebiegu
                       # (v1: pasmo wzgledem poprzedniego kroku - dryf zabijal trajektorie;
                       #  v2: tuba T=10 - trajektorie wychodzily gora; v3: pasmo wzgledem tau0, T=16;
                       #  v4: MINIMUM tau(p,c) zamiast maksimum - odwrotna nierownosc trojkata)

def log(s): print(s, flush=True)
def tonp(a): return cp.asnumpy(a) if GPU else np.asarray(a)

def siatka(t, x, h):
    nt = int(np.ceil(T_/h))+2; ns = int(np.ceil(S_/h))+2
    ci = XP.stack([XP.floor(t/h), XP.floor(x[:,0]/h), XP.floor(x[:,1]/h), XP.floor(x[:,2]/h)], 1).astype(XP.int32)
    cell = ((ci[:,0]*ns + ci[:,1])*ns + ci[:,2])*ns + ci[:,3]
    ncell = nt*ns*ns*ns
    order = XP.argsort(cell); cs = cell[order]
    starts = XP.searchsorted(cs, XP.arange(ncell), side="left")
    poz = XP.arange(len(t)) - starts[cs]; keep = poz < BUCKET
    buck = XP.full((ncell, BUCKET), -1, dtype=XP.int32)
    buck[cs[keep], poz[keep]] = order[keep].astype(XP.int32)
    return buck, nt, ns

OFF = None
def kandydaci(buck, t, x, tips, h, nt, ns, zasieg=2):
    global OFF
    if OFF is None or OFF.shape[1] != 4:
        OFF = XP.asarray(np.array([[d0,d1,d2,d3] for d0 in range(zasieg+1)
                                   for d1 in range(-zasieg,zasieg+1)
                                   for d2 in range(-zasieg,zasieg+1)
                                   for d3 in range(-zasieg,zasieg+1)], dtype=np.int32))
    c0 = XP.stack([XP.floor(t[tips]/h), XP.floor(x[tips,0]/h),
                   XP.floor(x[tips,1]/h), XP.floor(x[tips,2]/h)], 1).astype(XP.int32)
    cc = XP.clip(c0[:,None,:] + OFF[None,:,:], 0,
                 XP.asarray([nt-1, ns-1, ns-1, ns-1], dtype=XP.int32))
    cid = ((cc[:,:,0]*ns + cc[:,:,1])*ns + cc[:,:,2])*ns + cc[:,:,3]
    return buck[cid].reshape(len(tips), -1)

def buduj(t, x, buck, h, nt, ns, K, L, seed, wewnetrzna=True, vmax=0.8):
    rng = np.random.default_rng(seed)
    low = XP.where(t < 0.1*T_)[0]
    sel = XP.asarray(rng.choice(int(len(low)), K, replace=False))
    tips = low[sel].astype(XP.int32)
    v = XP.asarray(rng.uniform(0.02, vmax, K).astype(np.float32))
    kier = XP.asarray(rng.normal(size=(K,3)).astype(np.float32))
    kier = kier / XP.linalg.norm(kier, axis=1)[:,None]
    ch = [tips.copy()]; tau0 = None
    for krok in range(L-1):
        cand = kandydaci(buck, t, x, tips, h, nt, ns)
        ok = cand >= 0; ci = XP.where(ok, cand, 0).astype(XP.int32)
        dt = t[ci] - t[tips][:,None]; d2 = ((x[ci] - x[tips][:,None,:])**2).sum(-1)
        dobre = ok & (dt > 0) & (dt**2 > d2) & (dt < 3.0*h)   # przy tau0~0,5h okno 3h dopuszcza predkosci do ~0,98
        if krok == 0:
            # inicjalizacja: ten sam czas wlasny kroku dla WSZYSTKICH (to samo "tyknięcie poczatkowe"),
            # rozne kierunki i predkosci. Bez tego tempo tyknięc dziedziczy sie z warunku poczatkowego
            # i korelacja z predkoscia jest artefaktem inicjalizacji.
            tau_krok = XP.sqrt(XP.maximum(dt**2 - d2, 0))
            pasmo = (tau_krok > 0.45*h) & (tau_krok < 0.55*h)
            celx = x[tips][:,None,:] + (v[:,None]*dt)[:,:,None]*kier[:,None,:]
            score = XP.where(pasmo, -((x[ci] - celx)**2).sum(-1), -1e30)
        elif not wewnetrzna:
            celx = x[tips][:,None,:] + (v[:,None]*dt)[:,:,None]*kier[:,None,:]
            score = -((x[ci] - celx)**2).sum(-1)                  # kontrola: kierunek trzymany w ukladzie pudla
        else:
            # wewnetrzna, NIEHAMUJACA: rowne tyknięcia (ten sam czas wlasny kroku co poprzednio),
            # a wsrod nich najprostsza kontynuacja (max czas wlasny od przedostatniego).
            # Sam max czasu wlasnego do przodu preferuje male przesuniecie -> hamuje trajektorie.
            # pasmo wzgledem TYKNIECIA POCZATKOWEGO (nie poprzedniego): wzgledem poprzedniego
            # tyknięcie dryfuje w gore o kilkanascie % na krok i po ~15 krokach wypada z okna
            # (obserwacja: "zyje 15/20000" przy kroku 17).
            # ODWROTNA NIEROWNOSC TROJKATA: tau(p,c) >= tau(p,q)+tau(q,c), rownosc tylko gdy q lezy
            # na prostej p->c. Linia prosta daje NAJMNIEJSZY tau(p,c) przy ustalonych krokach,
            # wiec kontynuacja najprostsza = MINIMUM tau(p,c), nie maksimum.
            # (Maksimum wybieralo kontynuacje najbardziej zakrzywiona -> hamowanie, predkosci <=0,15.)
            p = ch[-2]
            tau_krok = XP.sqrt(XP.maximum(dt**2 - d2, 0))
            pasmo = (tau_krok > 0.8*tau0[:,None]) & (tau_krok < 1.2*tau0[:,None])
            dobre = dobre & pasmo
            score = -((t[ci] - t[p][:,None])**2 - ((x[ci] - x[p][:,None,:])**2).sum(-1))  # minus: minimum tau(p,c)
        best = XP.argmax(XP.where(dobre, score, -1e30), axis=1)
        nxt = ci[XP.arange(len(tips)), best]
        if krok == 0:
            tau0 = XP.sqrt(XP.maximum((t[nxt]-t[tips])**2 - ((x[nxt]-x[tips])**2).sum(-1), 1e-12))
        zyje = dobre.any(axis=1)
        tips = XP.where(zyje, nxt, tips).astype(XP.int32)
        ch.append(tips.copy())
        n_zyje = int(zyje.sum())
        if krok % 5 == 0 or n_zyje < 0.9*K: log(f"    krok {krok+2}/{L}: zyje {n_zyje}/{K}")
        if n_zyje == 0: log("    WSZYSTKIE martwe - trajektorie wyszly z tuby albo pasmo za waskie"); break
    return XP.stack(ch, 1)

def pomiar(t, x, E):
    tau2 = (t[E[:,1:]] - t[E[:,:-1]])**2 - ((x[E[:,1:]] - x[E[:,:-1]])**2).sum(-1)
    tau = XP.sqrt(XP.maximum(tau2, 0))
    ok = (tau > 0).all(axis=1)
    tau = tau[ok]; Eo = E[ok]
    cz = 1.0/tau.mean(axis=1)
    v = XP.linalg.norm(x[Eo[:,-1]] - x[Eo[:,0]], axis=1)/(t[Eo[:,-1]] - t[Eo[:,0]])
    half = tau.shape[1]//2
    c1 = 1.0/tau[:,:half].mean(axis=1); c2 = 1.0/tau[:,half:].mean(axis=1)
    return map(tonp, (cz, v, c1, c2))

res = json.load(open(CKPT)) if os.path.exists(CKPT) else {}
for seed in SEEDS:
    rs = XP.random.RandomState(seed)
    t = rs.uniform(0, T_, N).astype(XP.float32); x = rs.uniform(0, S_, (N,3)).astype(XP.float32)
    rho = N/(T_*S_**3); h = float((24*KAND/(np.pi*rho))**0.25)
    log(f"ziarno {seed}: tau={h:.3f}, gestosc {rho:.0f}")
    buck, nt, ns = siatka(t, x, h); log("  siatka gotowa")
    for nazwa, wew in [("regula wewnetrzna (pamiec)", True), ("regula zewnetrzna (kontrola)", False)]:
        key = f"{WERSJA}|{seed}|{nazwa}"
        if key in res: log(f"  {nazwa}: z checkpointu"); continue
        t0 = time.time(); E = buduj(t, x, buck, h, nt, ns, K, L, seed, wewnetrzna=wew)
        cz, v, c1, c2 = pomiar(t, x, E)
        if len(cz) == 0:                                   # zabezpieczenie (uzytkownik): pusta proba
            log(f"  {nazwa}: BRAK WAZNYCH TRAJEKTORII (n=0)")
            res[key] = dict(korelacja=float("nan"), stosunek=float("nan"), stabilnosc=float("nan"), n=0)
            json.dump(res, open(CKPT, "w")); continue
        q1, q3 = np.quantile(v, [0.25, 0.75])
        kor = float(np.corrcoef(cz, v)[0,1]); stos = float(cz[v>=q3].mean()/cz[v<=q1].mean())
        stab = float(np.corrcoef(c1, c2)[0,1])
        res[key] = dict(korelacja=kor, stosunek=stos, stabilnosc=stab, n=int(len(cz)),
                        srednia=float(cz.mean()), rozrzut=float(cz.std()),
                        v_min=float(v.min()), v_max=float(v.max()))
        json.dump(res, open(CKPT, "w"))
        log(f"  {nazwa}: n={len(cz)} | korelacja z v {kor:+.3f} | szybkie/wolne {stos:.3f} | "
            f"stabilnosc {stab:+.3f} | predkosci {v.min():.2f}-{v.max():.2f}  ({time.time()-t0:.0f}s)")
