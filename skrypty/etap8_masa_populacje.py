"""
MASA — DWIE POPULACJE (rozroznialne masy). Na bazie etap7 v4.

MASA — kandydat 2 przy WEWNETRZNEJ regule kontynuacji (Colab: edytuj stale na gorze).

Poprzednie porazki: czestosc samoodczytu zalezala od predkosci, bo moja regula budowy trajektorii
odwolywala sie do ukladu pudla (okno w czasie wspolrzednosciowym, kierunek z zewnatrz).
TU: trajektoria kontynuuje sie PAMIECIA — nastepny element maksymalizuje czas wlasny liczony
od elementu PRZEDOSTATNIEGO (najmniejsze zakrzywienie linii). Regula czysto porzadkowa,
nie zna zadnego ukladu; predkosc pochodzi z dwoch pierwszych elementow i jest niesiona dalej.

MIERZONE: czestosc tyknięc = (liczba krokow)/(suma czasow wlasnych krokow) = 1/<tau_krok>.
ZDANIA DO UPADKU (etap8, dwie populacje):
  P1. tyknięcie poczatkowe: populacja A 0,4h, populacja B 0,6h -> tempo A/B = 1,5 +- 0,1
  P2. w KAZDEJ populacji tempo nie zalezy od predkosci (stosunek szybkie/wolne 1,00 +- 0,05)
  (v6: prostota mierzona NADWYZKA z odwrotnej nierownosci trojkata, nie minimum tau(p,c))
  P3. PASMO_WZGL = "poprzedni": tempo niesione krok po kroku wylacznie pamiecia utrzymuje sie
      (tempo na koncu w granicach 10% tempa poczatkowego) - przy regule minimum nie ma dryfu
  P4. populacje pozostaja rozroznialne: nakladanie rozkladow tempa < 10%
  (uwaga: przy PASMO_WZGL = "poczatkowe" stosunek 1,5 bylby wymuszony konstrukcja - slabszy test)

ZDANIA etap7:
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
CKPT   = "etap8_populacje.json"
WERSJA = "v6-nadwyzka"
PASMO_WZGL = "poprzedni"   # "poprzedni" (uczciwy test) albo "poczatkowe"
TAU_A, TAU_B = 0.4, 0.6    # tyknięcia poczatkowe dwoch populacji (w jednostkach h)          # znacznik wersji reguly: po zmianie regul stare wyniki nie blokuja przebiegu
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

def buduj(t, x, buck, h, nt, ns, K, L, seed, wewnetrzna=True, vmax=0.8, tau_start=0.5):
    rng = np.random.default_rng(seed)
    low = XP.where(t < 0.1*T_)[0]
    sel = XP.asarray(rng.choice(int(len(low)), K, replace=False))
    tips = low[sel].astype(XP.int32)
    v = XP.asarray(rng.uniform(0.02, vmax, K).astype(np.float32))
    kier = XP.asarray(rng.normal(size=(K,3)).astype(np.float32))
    kier = kier / XP.linalg.norm(kier, axis=1)[:,None]
    ch = [tips.copy()]; tau0 = XP.zeros(K, dtype=XP.float32)
    PORCJA = 1500          # trajektorii liczonych naraz (szczyt pamieci ~ PORCJA * 24 tys. kandydatow)
    for krok in range(L-1):
        nxt_all = tips.copy(); zyje_all = XP.zeros(K, dtype=bool)
        for s0 in range(0, K, PORCJA):
            sl = slice(s0, min(s0 + PORCJA, K))
            tp = tips[sl]
            cand = kandydaci(buck, t, x, tp, h, nt, ns)
            ok = cand >= 0; ci = XP.where(ok, cand, 0).astype(XP.int32); del cand
            xc = x[ci]
            dt = t[ci] - t[tp][:,None]; d2 = ((xc - x[tp][:,None,:])**2).sum(-1)
            dobre = ok & (dt > 0) & (dt**2 > d2) & (dt < 3.0*h); del ok
            tau_krok = XP.sqrt(XP.maximum(dt**2 - d2, 0))
            if krok == 0:
                pasmo = (tau_krok > (tau_start-0.05)*h) & (tau_krok < (tau_start+0.05)*h)
                celx = x[tp][:,None,:] + (v[sl][:,None]*dt)[:,:,None]*kier[sl][:,None,:]
                score = XP.where(pasmo, -((xc - celx)**2).sum(-1), -1e30); del celx
            elif not wewnetrzna:
                celx = x[tp][:,None,:] + (v[sl][:,None]*dt)[:,:,None]*kier[sl][:,None,:]
                score = -((xc - celx)**2).sum(-1); del celx
            else:
                pp = ch[-2][sl]
                if PASMO_WZGL == "poprzedni":
                    tau_ref = XP.sqrt(XP.maximum((t[tp]-t[pp])**2 - ((x[tp]-x[pp])**2).sum(-1), 1e-12))
                    pasmo = (tau_krok > 0.9*tau_ref[:,None]) & (tau_krok < 1.1*tau_ref[:,None])
                else:
                    pasmo = (tau_krok > 0.8*tau0[sl][:,None]) & (tau_krok < 1.2*tau0[sl][:,None])
                dobre = dobre & pasmo
                tpc = XP.sqrt(XP.maximum((t[ci] - t[pp][:,None])**2 - ((xc - x[pp][:,None,:])**2).sum(-1), 0))
                tpq = XP.sqrt(XP.maximum((t[tp]-t[pp])**2 - ((x[tp]-x[pp])**2).sum(-1), 0))[:,None]
                score = -(tpc - tpq - tau_krok); del tpc
            del xc, d2
            best = XP.argmax(XP.where(dobre, score, -1e30), axis=1)
            n_ = ci[XP.arange(ci.shape[0]), best]; z_ = dobre.any(axis=1)
            nxt_all[sl] = XP.where(z_, n_, tp); zyje_all[sl] = z_
            if krok == 0:
                tau0[sl] = XP.sqrt(XP.maximum((t[n_]-t[tp])**2 - ((x[n_]-x[tp])**2).sum(-1), 1e-12))
            del ci, dt, dobre, score, tau_krok
            if GPU: cp.get_default_memory_pool().free_all_blocks()
        tips = nxt_all.astype(XP.int32); zyje = zyje_all
        ch.append(tips.copy())
        n_zyje = int(zyje.sum())
        if krok % 5 == 0 or n_zyje < 0.9*K: log(f"    krok {krok+2}/{L}: zyje {n_zyje}/{K}")
        if n_zyje == 0: log("    WSZYSTKIE martwe"); break
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
    pocz = 1.0/tau[:,:3].mean(axis=1); kon = 1.0/tau[:,-3:].mean(axis=1)
    return map(tonp, (cz, v, c1, c2, pocz, kon))

res = json.load(open(CKPT)) if os.path.exists(CKPT) else {}
for seed in SEEDS:
    rs = XP.random.RandomState(seed)
    t = rs.uniform(0, T_, N).astype(XP.float32); x = rs.uniform(0, S_, (N,3)).astype(XP.float32)
    rho = N/(T_*S_**3); h = float((24*KAND/(np.pi*rho))**0.25)
    log(f"ziarno {seed}: tau={h:.3f}, gestosc {rho:.0f}")
    buck, nt, ns = siatka(t, x, h); log("  siatka gotowa")
    wyn = {}
    for nazwa, ts in [("populacja A", TAU_A), ("populacja B", TAU_B)]:
        key = f"{WERSJA}|{PASMO_WZGL}|{seed}|{nazwa}"
        if key in res: log(f"  {nazwa}: z checkpointu"); wyn[nazwa] = res[key]; continue
        t0 = time.time(); E = buduj(t, x, buck, h, nt, ns, K, L, seed + (0 if ts == TAU_A else 1000), tau_start=ts)
        cz, v, c1, c2, pocz, kon = pomiar(t, x, E)
        if len(cz) == 0:
            log(f"  {nazwa}: BRAK WAZNYCH TRAJEKTORII (n=0)"); continue
        q1, q3 = np.quantile(v, [0.25, 0.75])
        r = dict(n=int(len(cz)), srednia=float(cz.mean()), rozrzut=float(cz.std()),
                 korelacja=float(np.corrcoef(cz, v)[0,1]), stosunek=float(cz[v>=q3].mean()/cz[v<=q1].mean()),
                 stabilnosc=float(np.corrcoef(c1, c2)[0,1]), dryf=float(np.median(kon/pocz)),
                 v_max=float(v.max()), tempa=[float(z) for z in np.quantile(cz, [0.05, 0.95])])
        res[key] = r; wyn[nazwa] = r; json.dump(res, open(CKPT, "w"))
        log(f"  {nazwa} (tau_start={ts}h): n={r['n']} | tempo {r['srednia']:.3f} ± {r['rozrzut']:.3f} | "
            f"korelacja z v {r['korelacja']:+.3f} | szybkie/wolne {r['stosunek']:.3f} | "
            f"stabilnosc {r['stabilnosc']:+.3f} | dryf (koniec/poczatek) {r['dryf']:.3f} | v_max {r['v_max']:.2f}  ({time.time()-t0:.0f}s)")
    if len(wyn) == 2:
        A, B = wyn["populacja A"], wyn["populacja B"]
        log(f"  >> P1 tempo A/B = {A['srednia']/B['srednia']:.3f}  (oczekiwane {TAU_B/TAU_A:.2f})")
        log(f"  >> P4 przedzialy 5-95%: A {A['tempa'][0]:.2f}-{A['tempa'][1]:.2f} | B {B['tempa'][0]:.2f}-{B['tempa'][1]:.2f}"
            f"  -> {'rozlaczne' if A['tempa'][0] > B['tempa'][1] else 'NAKLADAJA SIE'}")
