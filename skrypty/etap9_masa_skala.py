"""
MASA I SKALA - most do logarytmow (§F2). Colab / A100.

Po co: jedna gestosc daje punkt, nie funkcje. Logarytmy z C4a pochodzily ze STOSUNKU SKAL.
Tu stosunkiem skal jest: liczba elementow na tykniecie  n = rho * (pi/24) * tau0^4.
UWAGA: zwiekszanie N przy stalym KAND (poprzednie skrypty) jest tautologia - Poisson jest
niezmienniczy wzgledem skali, kazdy krok widzi to samo. Dlatego skanujemy TYKNIECIE przy stalej
gestosci (rownowazne skanowaniu gestosci przy stalym tyknieciu; liczy sie tylko rho*tau0^4).

Regula: jak etap8 v6 (pasmo wzgledem poprzedniego kroku; prostota = nadwyzka z odwrotnej
nierownosci trojkata). Populacje: A tau0, B 1,5*tau0.

ZDANIA DO UPADKU:
  S1. szerokosc wzgledna tempa (odchylenie/srednia) wobec n:
        ~ n^(-1/2)  -> szum Poissona, MOSTU TEDY NIE MA
        ~ 1/ln n    -> masa ma wbudowany logarytm skali, JEST MOST
        stala       -> szerokosc wbudowana w regule
      (rozstrzygniecie ln vs stala wymaga >= 2 dekad w n - skan daje 3)
  S2. przesuniecie stosunku |A/B - 1,5| maleje z n (artefakt dyskretnosci)
  S3. dryf |koniec/poczatek - 1| maleje z n
"""
import numpy as np, json, os, time
try:
    import cupy as cp; XP = cp; GPU = True
except ImportError:
    XP = np; GPU = False

T_, S_  = 16.0, 6.0
N       = 19_000_000
K       = 500                              # trajektorii na populacje (pamiec rosnie z n)
L       = 16
TAU0S   = [0.056, 0.10, 0.18, 0.32]        # tykniecie A; B = 1,5*tau0  -> n od ~0,007 do ~7,5
SEEDS   = [1, 2]
WERSJA  = "v1-skala"
CKPT    = "etap9_skala.json"

def log(s): print(s, flush=True)
def tonp(a): return cp.asnumpy(a) if GPU else np.asarray(a)

def siatka(t, x, c):
    nt = int(np.ceil(T_/c))+2; ns = int(np.ceil(S_/c))+2
    rho = len(t)/(T_*S_**3); bucket = int(max(16, 1.6*rho*c**4 + 6*np.sqrt(rho*c**4)))
    ci = XP.stack([XP.floor(t/c), XP.floor(x[:,0]/c), XP.floor(x[:,1]/c), XP.floor(x[:,2]/c)], 1).astype(XP.int32)
    cell = ((ci[:,0]*ns + ci[:,1])*ns + ci[:,2])*ns + ci[:,3]; ncell = nt*ns*ns*ns
    order = XP.argsort(cell); cs = cell[order]
    starts = XP.searchsorted(cs, XP.arange(ncell), side="left")
    poz = XP.arange(len(t)) - starts[cs]; keep = poz < bucket
    buck = XP.full((ncell, bucket), -1, dtype=XP.int32)
    buck[cs[keep], poz[keep]] = order[keep].astype(XP.int32)
    obciete = float(1 - float(keep.sum())/len(t))
    return buck, nt, ns, bucket, obciete

OFF = XP.asarray(np.array([[d0,d1,d2,d3] for d0 in (0,1) for d1 in (-1,0,1) for d2 in (-1,0,1) for d3 in (-1,0,1)], dtype=np.int32))
def kand(buck, t, x, tips, c, nt, ns):
    c0 = XP.stack([XP.floor(t[tips]/c), XP.floor(x[tips,0]/c), XP.floor(x[tips,1]/c), XP.floor(x[tips,2]/c)], 1).astype(XP.int32)
    cc = XP.clip(c0[:,None,:] + OFF[None,:,:], 0, XP.asarray([nt-1, ns-1, ns-1, ns-1], dtype=XP.int32))
    cid = ((cc[:,:,0]*ns + cc[:,:,1])*ns + cc[:,:,2])*ns + cc[:,:,3]
    return buck[cid].reshape(len(tips), -1)

def buduj(t, x, buck, c, nt, ns, tau_s, seed, vmax=0.9):
    rng = np.random.default_rng(seed)
    low = XP.where(t < 0.1*T_)[0]; tips = low[XP.asarray(rng.choice(int(len(low)), K, replace=False))].astype(XP.int32)
    v = XP.asarray(rng.uniform(0.02, vmax, K).astype(np.float32))
    kier = XP.asarray(rng.normal(size=(K,3)).astype(np.float32)); kier /= XP.linalg.norm(kier, axis=1)[:,None]
    ch = [tips.copy()]; nadm = []
    PORCJA = 25                                           # trajektorii liczonych naraz: pamiec nie zalezy od K
    for krok in range(L-1):
        nxt_all = tips.copy(); zyje_all = XP.zeros(K, dtype=bool); nad = []
        for s0 in range(0, K, PORCJA):
            sl = slice(s0, min(s0+PORCJA, K)); tp = tips[sl]
            C = kand(buck, t, x, tp, c, nt, ns); ok = C >= 0; ci = XP.where(ok, C, 0).astype(XP.int32)
            dt = t[ci] - t[tp][:,None]; d2 = ((x[ci] - x[tp][:,None,:])**2).sum(-1)
            tk = XP.sqrt(XP.maximum(dt**2 - d2, 0))
            dobre = ok & (dt > 0) & (dt**2 > d2) & (dt < c)
            if krok == 0:
                pas = (tk > 0.9*tau_s) & (tk < 1.1*tau_s)
                celx = x[tp][:,None,:] + (v[sl][:,None]*dt)[:,:,None]*kier[sl][:,None,:]
                score = -((x[ci] - celx)**2).sum(-1)
            else:
                p = ch[-2][sl]
                tref = XP.sqrt(XP.maximum((t[tp]-t[p])**2 - ((x[tp]-x[p])**2).sum(-1), 1e-12))
                pas = (tk > 0.9*tref[:,None]) & (tk < 1.1*tref[:,None])
                tpc = XP.sqrt(XP.maximum((t[ci]-t[p][:,None])**2 - ((x[ci]-x[p][:,None,:])**2).sum(-1), 0))
                score = -(tpc - tref[:,None] - tk)
            dobre = dobre & pas; nad.append(dobre.sum(1))
            best = XP.argmax(XP.where(dobre, score, -1e30), axis=1)
            nxt_all[sl] = ci[XP.arange(len(tp)), best]; zyje_all[sl] = dobre.any(1)
            del C, ok, ci, dt, d2, tk, dobre, pas, score
        nadm.append(float(XP.concatenate(nad).mean()))
        tips = XP.where(zyje_all, nxt_all, tips).astype(XP.int32); ch.append(tips.copy())
        if int(zyje_all.sum()) == 0: log("      wszystkie martwe"); break
        if GPU: cp.get_default_memory_pool().free_all_blocks()
    return XP.stack(ch, 1), float(np.mean(nadm))

def pomiar(t, x, E):
    tau = XP.sqrt(XP.maximum((t[E[:,1:]]-t[E[:,:-1]])**2 - ((x[E[:,1:]]-x[E[:,:-1]])**2).sum(-1), 0))
    ok = (tau > 0).all(1); tau = tau[ok]; Eo = E[ok]
    if len(tau) == 0: return None
    cz = 1/tau.mean(1); v = XP.linalg.norm(x[Eo[:,-1]]-x[Eo[:,0]], axis=1)/(t[Eo[:,-1]]-t[Eo[:,0]])
    dryf = (1/tau[:,-3:].mean(1))/(1/tau[:,:3].mean(1))
    return [tonp(a) for a in (cz, v, dryf)]

res = json.load(open(CKPT)) if os.path.exists(CKPT) else {}
for seed in SEEDS:
    rs = XP.random.RandomState(seed)
    t = rs.uniform(0, T_, N).astype(XP.float32); x = rs.uniform(0, S_, (N,3)).astype(XP.float32)
    rho = N/(T_*S_**3); log(f"ziarno {seed}: gestosc {rho:.0f}")
    for tau0 in TAU0S:
        key = f"{WERSJA}|{seed}|{tau0}"
        if key in res: log(f"  tau0={tau0}: z checkpointu"); continue
        c = 2.4*1.5*tau0                             # komorka = okno czasu dla B (v<=0,9 -> gamma<=2,3)
        buck, nt, ns, bucket, obc = siatka(t, x, c)
        n = rho*(np.pi/24)*tau0**4
        wyn = {}
        for nazwa, ts in [("A", tau0), ("B", 1.5*tau0)]:
            t0 = time.time(); E, nadm = buduj(t, x, buck, c, nt, ns, ts, seed + (0 if nazwa == "A" else 1000))
            r = pomiar(t, x, E)
            if r is None: log(f"  tau0={tau0} {nazwa}: brak waznych"); continue
            cz, v, dr = r
            wyn[nazwa] = dict(sr=float(cz.mean()), szer=float(cz.std()/cz.mean()), n=int(len(cz)),
                              dryf=float(np.median(dr)), kor=float(np.corrcoef(cz, v)[0,1]), nadm=nadm)
            log(f"  tau0={tau0} {nazwa}: n_el/tykn={n*(1.5**4 if nazwa=='B' else 1):.3f} | kand/krok {nadm:.0f} | "
                f"tempo {cz.mean():.3f} | szer {wyn[nazwa]['szer']:.3f} | dryf {wyn[nazwa]['dryf']:.3f} | "
                f"kor(v) {wyn[nazwa]['kor']:+.3f} | waznych {len(cz)} | obciete {obc:.2%}  ({time.time()-t0:.0f}s)")
        if len(wyn) == 2:
            wyn["AB"] = wyn["A"]["sr"]/wyn["B"]["sr"]; wyn["n"] = n
            log(f"  >> tau0={tau0}: A/B = {wyn['AB']:.4f} (oczek. 1,5) | przesuniecie {abs(wyn['AB']-1.5):.4f}")
        res[key] = wyn; json.dump(res, open(CKPT, "w"))
        del buck
        if GPU: cp.get_default_memory_pool().free_all_blocks()

log("\nPODSUMOWANIE (srednia po ziarnach): n | szer A | szer B | |A/B-1,5| | dryf A | dryf B")
rows = []
for tau0 in TAU0S:
    w = [res.get(f"{WERSJA}|{s}|{tau0}", {}) for s in SEEDS]; w = [q for q in w if "AB" in q]
    if not w: continue
    f = lambda k, p: np.mean([q[p][k] for q in w])
    n = w[0]["n"]; sA, sB = f("szer","A"), f("szer","B"); ab = np.mean([abs(q["AB"]-1.5) for q in w])
    log(f"  n={n:8.3f} | {sA:.4f} | {sB:.4f} | {ab:.4f} | {f('dryf','A'):.3f} | {f('dryf','B'):.3f}")
    rows.append((n, sA, sB))
if len(rows) >= 3:
    r = np.array(rows); ln = np.log(r[:,0])
    for i, nm in [(1, "A"), (2, "B")]:
        pot = np.polyfit(ln, np.log(r[:,i]), 1)[0]
        log(f"  S1 {nm}: szerokosc ~ n^{pot:+.3f}   (Poisson: -0,5; stala: 0; 1/ln n: bardzo slaby spadek)")
