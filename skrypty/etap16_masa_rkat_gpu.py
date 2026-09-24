"""
MASA — DWIE POPULACJE przy regule R-KAT (etap15). Colab A100 40 GB. Na bazie etap8 v6.
Po co: wyniki §F1 (A/B = 1,507; tempo niezalezne od v) byly liczone regula "najmniejsza nadwyzka",
ktora ma dryf tempa ~eps^2 (etap13). Regula R-KAT go usuwa (etap15, D1-D3). Czy §F1 stoi?

REGULA R-KAT (pamiec JEDNOKROKOWA - A/B nie jest wymuszone):
  s = ln(tk/tref) w [delta-eps, delta+eps], delta = -(eps*coth(4 eps) - 1/4)  (d = 3+1), eps = 0,1
  prostota = najmniejsze wzgledne pchniecie r: cosh r = (tpc^2 - tref^2 - tk^2)/(2 tref tk)
Poprawka przy okazji: kubelek liczony z gestosci (etap8 mial 64 miejsca przy ~90 elementach w komorce).

ZDANIA DO UPADKU (przed przebiegiem):
  F1. tempo A/B = 1,500 +- 0,010                       (etap8: 1,508 / 1,507)
  F2. w kazdej populacji |korelacja(tempo, v)| < 0,05 i szybkie/wolne = 1,00 +- 0,02
                                                        (etap8: A 0,988 / -0,03; B 1,055 / +0,13 - upadlo)
  F3. dryf mediana(koniec/poczatek) = 1,00 +- 0,02     (etap8: 0,94-0,95)
  (filtr scian dodany przed przebiegiem: liczone tylko trajektorie >= 3h od scian przez caly czas)
  F4. rozrzut wzgledny tempa = przewidywanie z bladzenia ln tref (policzone ponizej, bez przestrzeni) +- 15%
      (etap8: ~15%, wtedy przypisane pasmu)
"""
import numpy as np, json, os, time
try:
    import cupy as cp; XP = cp; GPU = True
except ImportError:
    XP = np; GPU = False

T_, S_ = 16.0, 14.0     # szersze pudlo: trajektoria v=0,8 przechodzi ~5,6 w 19 krokach, start w srodku (+-1)     # wyzsza tuba: przy L=20 trajektoria nie moze wyjsc gora (obserwacja: nagly zgon wszystkich na kroku ~10 przy T=10)
N      = 241_000_000   # ta sama gestosc co etap8 (19 mln na 16x6^3) -> h ~ 0,36; ~3,9 GB punktow
K      = 20_000
L      = 20
KAND   = 12
EPS    = 0.10
SCIANA = 3.0           # odstep od scian w jednostkach h
DELTA  = -(EPS/np.tanh(4*EPS) - 0.25)
PORCJA = 1000          # trajektorii naraz; przy 80 GB mozna 2000
SEEDS  = [1, 2]
CKPT   = "etap16_rkat.json"
WERSJA = "rkat-v1"
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
    lam = len(t)/(T_*S_**3)*h**4; BUCKET = int(lam + 6*np.sqrt(lam) + 10)
    order = XP.argsort(cell); cs = cell[order]
    starts = XP.searchsorted(cs, XP.arange(ncell), side="left")
    poz = XP.arange(len(t)) - starts[cs]; keep = poz < BUCKET
    buck = XP.full((ncell, BUCKET), -1, dtype=XP.int32)
    buck[cs[keep], poz[keep]] = order[keep].astype(XP.int32)
    obc = 1 - float(keep.sum())/len(t)
    return buck, nt, ns, obc

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
    low = XP.where((t < 0.1*T_) & (XP.abs(x - S_/2).max(1) < 1.0))[0]      # start w srodku pudla
    sel = XP.asarray(rng.choice(int(len(low)), K, replace=False))
    tips = low[sel].astype(XP.int32)
    v = XP.asarray(rng.uniform(0.02, vmax, K).astype(np.float32))
    kier = XP.asarray(rng.normal(size=(K,3)).astype(np.float32))
    kier = kier / XP.linalg.norm(kier, axis=1)[:,None]
    ch = [tips.copy()]; tau0 = XP.zeros(K, dtype=XP.float32)
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
                tref = XP.sqrt(XP.maximum((t[tp]-t[pp])**2 - ((x[tp]-x[pp])**2).sum(-1), 1e-12))[:,None]
                sk = XP.log(XP.maximum(tau_krok, 1e-12)/tref)
                dobre = dobre & (sk > DELTA-EPS) & (sk < DELTA+EPS)
                tpc2 = (t[ci] - t[pp][:,None])**2 - ((xc - x[pp][:,None,:])**2).sum(-1)
                chr_ = (tpc2 - tref**2 - tau_krok**2)/(2*tref*XP.maximum(tau_krok, 1e-12))   # cosh r
                score = -chr_; del tpc2, chr_, sk
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

def pomiar(t, x, E, h):
    # filtr scian (nowy wobec etap8): cala trajektoria >= 3h od scian przestrzennych, inaczej komorki
    # przy scianie sa obciete i szybkie trajektorie sa odbijane -> falszywa zaleznosc od v
    xe = x[E]; sc = ((xe > SCIANA*h) & (xe < S_ - SCIANA*h)).all(axis=(1,2))
    E = E[sc]
    tau2 = (t[E[:,1:]] - t[E[:,:-1]])**2 - ((x[E[:,1:]] - x[E[:,:-1]])**2).sum(-1)
    tau = XP.sqrt(XP.maximum(tau2, 0))
    ok = (tau > 0).all(axis=1)
    tau = tau[ok]; Eo = E[ok]
    cz = 1.0/tau.mean(axis=1)
    v = XP.linalg.norm(x[Eo[:,-1]] - x[Eo[:,0]], axis=1)/(t[Eo[:,-1]] - t[Eo[:,0]])
    half = tau.shape[1]//2
    c1 = 1.0/tau[:,:half].mean(axis=1); c2 = 1.0/tau[:,half:].mean(axis=1)
    pocz = 1.0/tau[:,:3].mean(axis=1); kon = 1.0/tau[:,-3:].mean(axis=1)
    return list(map(tonp, (cz, v, c1, c2, pocz, kon))) + [int(sc.sum())]

def przewid_F4(ts, M=200000, seed=7):
    """rozrzut wzgledny 1/<tau> przy bladzeniu ln tref: krok 0 ~ pasmo +-0,05h wokol ts (gestosc ~tau^3),
    potem L-2 krokow s z gestoscia ~e^(4s) na [DELTA-EPS, DELTA+EPS]. Bez przestrzeni."""
    g = np.random.default_rng(seed)
    t1 = g.uniform((ts-0.05)**4, (ts+0.05)**4, M)**0.25
    s = np.log(g.uniform(np.exp(4*(DELTA-EPS)), np.exp(4*(DELTA+EPS)), (M, L-2)))/4
    tau = t1[:,None]*np.exp(np.concatenate([np.zeros((M,1)), np.cumsum(s, 1)], 1))
    cz = 1/tau.mean(1); return cz.std()/cz.mean()
F4_PRZ = {"A": przewid_F4(TAU_A), "B": przewid_F4(TAU_B)}
log(f"F4 przewidywane rozrzuty: A {F4_PRZ['A']:.4f}, B {F4_PRZ['B']:.4f}  (delta = {DELTA:+.5f})")
res = json.load(open(CKPT)) if os.path.exists(CKPT) else {}
for seed in SEEDS:
    rs = XP.random.RandomState(seed)
    t = rs.uniform(0, T_, N).astype(XP.float32); x = rs.uniform(0, S_, (N,3)).astype(XP.float32)
    rho = N/(T_*S_**3); h = float((24*KAND/(np.pi*rho))**0.25)
    log(f"ziarno {seed}: tau={h:.3f}, gestosc {rho:.0f}")
    buck, nt, ns, obc = siatka(t, x, h); log(f"  siatka gotowa, obciete {obc:.3%}")
    wyn = {}
    for nazwa, ts in [("populacja A", TAU_A), ("populacja B", TAU_B)]:
        key = f"{WERSJA}|{seed}|{nazwa}"
        if key in res: log(f"  {nazwa}: z checkpointu"); wyn[nazwa] = res[key]; continue
        t0 = time.time(); E = buduj(t, x, buck, h, nt, ns, K, L, seed + (0 if ts == TAU_A else 1000), tau_start=ts)
        cz, v, c1, c2, pocz, kon, nsc = pomiar(t, x, E, h)
        if len(cz) == 0:
            log(f"  {nazwa}: BRAK WAZNYCH TRAJEKTORII (n=0)"); continue
        q1, q3 = np.quantile(v, [0.25, 0.75])
        r = dict(n=int(len(cz)), po_filtrze_scian=nsc, srednia=float(cz.mean()), rozrzut=float(cz.std()),
                 korelacja=float(np.corrcoef(cz, v)[0,1]), stosunek=float(cz[v>=q3].mean()/cz[v<=q1].mean()),
                 stabilnosc=float(np.corrcoef(c1, c2)[0,1]), dryf=float(np.median(kon/pocz)),
                 v_max=float(v.max()), tempa=[float(z) for z in np.quantile(cz, [0.05, 0.95])],
                 rozrzut_wzgl=float(cz.std()/cz.mean()))
        res[key] = r; wyn[nazwa] = r; json.dump(res, open(CKPT, "w"))
        log(f"  {nazwa} (tau_start={ts}h): n={r['n']} | tempo {r['srednia']:.3f} ± {r['rozrzut']:.3f} | "
            f"korelacja z v {r['korelacja']:+.3f} | szybkie/wolne {r['stosunek']:.3f} | "
            f"stabilnosc {r['stabilnosc']:+.3f} | dryf (koniec/poczatek) {r['dryf']:.3f} | v_max {r['v_max']:.2f}  ({time.time()-t0:.0f}s)")
    if len(wyn) == 2:
        A, B = wyn["populacja A"], wyn["populacja B"]
        log(f"  >> F1 tempo A/B = {A['srednia']/B['srednia']:.4f}  (1,500 +- 0,010)")
        for nm, P in (("A", A), ("B", B)):
            log(f"  >> {nm}: F2 kor {P['korelacja']:+.3f} (|.|<0,05), szybkie/wolne {P['stosunek']:.3f} (1,00+-0,02) | "
                f"F3 dryf {P['dryf']:.3f} (1,00+-0,02) | F4 rozrzut {P['rozrzut_wzgl']:.4f} / przewid. {F4_PRZ[nm]:.4f} "
                f"= {P['rozrzut_wzgl']/F4_PRZ[nm]:.3f} (1+-0,15)")
