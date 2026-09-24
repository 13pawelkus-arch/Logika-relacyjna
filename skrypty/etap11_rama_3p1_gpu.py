"""
MOST PRZEZ RAME w 3+1 — PELNY SPRINKLING (GPU, Colab A100 40 GB).
Cel: potwierdzic redukcje z etap10c (kazdy krok = niezalezne losowanie w lokalnym ukladzie
poprzedniego kroku) na prawdziwym sprinklingu, ze wspolnymi punktami i ukladem pudla.

Stosunek skal: n = rho*pi*tau^4/24 (elementow na tykniecie). Gestosc STALA, skanujemy tykniecie
tau0 = (n/NMAX)^(1/4) (Poisson jest niezmienniczy wzgledem skali; liczy sie tylko rho*tau^4).
Regula: jak etap9/10 — pasmo +-eps wzgledem POPRZEDNIEGO kroku, kontynuacja = najmniejsza
nadwyzka tau(p,c) - tref - tk. Krok 0: najblizej zadanej predkosci (v_cel do 0,6).
Mierzone: r = wzgledne pchniecie kolejnych krokow, cosh r = -(u1.u2) (4-predkosci).
Wzor (etap10c): rms(r) = sqrt(Gamma(5/3)) * ((4pi/3) lam3)^(-1/3),
                lam3 = rho*tref^4*((1+eps)^4-(1-eps)^4)/4   (tref = czas wlasny poprzedniego kroku)

ZDANIA DO UPADKU (zapisane przed przebiegiem):
  Q1. wykladnik rms(r) wobec n = -0,333 +- 0,03 (dla kazdego eps)
  Q2. rms(r / wzor_lokalny) = 1,00 +- 0,05 (dla n >= 10; przy n = 3 dyskretnosc)
  Q3. niezmienniczosc: Q2 liczone osobno dla v_cel < 0,3 i >= 0,3 rozni sie o < 5%
  Jesli Q2 upadnie, a etap10c przeszedl -> redukcja do lokalnego losowania jest bledna
  (wspolne punkty / korelacje miedzy krokami maja znaczenie) i wynik 3+1 z etap10c nie stoi.

URUCHOMIENIE: w Colab (GPU A100) -> !pip install cupy-cuda12x (zwykle juz jest), wkleic calosc.
Checkpoint: etap11_rama.json — przerwany przebieg wznawia sie od miejsca przerwania.
Test na CPU (maly): python3 etap11_rama_3p1_gpu.py test
"""
import numpy as np, json, os, sys, time
from math import gamma, pi
try:
    import cupy as cp; XP = cp; GPU = True
except ImportError:
    XP = np; GPU = False

# ---------------- PARAMETRY ----------------
NS     = [3, 10, 30, 100, 300, 1000, 3000]      # elementow na tykniecie: 3 dekady
EPSS   = [0.05, 0.10, 0.20]
NMAX   = 3000                                   # przy tau = 1; rho = 24*NMAX/pi ~ 22 900
K      = 2000                                   # trajektorii na (n, eps)
L      = 5                                      # kroki: 0 (cel zewn.) + 3 kroki pamieci -> 3 przyrosty r
VMAX   = 0.6
T_, S_ = 7.0, 8.0                               # pudlo w jednostkach tau(NMAX) = 1  -> ~82 mln punktow
SEED   = 1
PAMIEC = 1.2e8                                  # elementow kandydatow na porcje (~8 GB na A100 40 GB; przy 80 GB mozna 2.5e8)
CKPT   = "etap11_rama.json"
WERSJA = "v1"
if len(sys.argv) > 1 and sys.argv[1] == "test":                 # szybki test logiki na CPU
    NS, NMAX, K, EPSS, CKPT = [30, 100, 300], 300, 100, [0.10], "test11.json"
# -------------------------------------------

def log(s): print(s, flush=True)
def tonp(a): return cp.asnumpy(a) if GPU else np.asarray(a)
RHO = 24*NMAX/pi
SQG = np.sqrt(gamma(5/3))
def wzor(tref, eps):
    lam3 = RHO*tref**4*((1+eps)**4-(1-eps)**4)/4
    return SQG*((4*pi/3)*lam3)**(-1/3)

def siatka(t, x, c):
    nt = int(np.ceil(T_/c))+2; ns = int(np.ceil(S_/c))+2
    lam = RHO*c**4; bucket = int(max(16, lam + 6*np.sqrt(lam) + 10))
    ci = XP.stack([XP.floor(t/c), XP.floor(x[:,0]/c), XP.floor(x[:,1]/c), XP.floor(x[:,2]/c)], 1).astype(XP.int32)
    cell = ((ci[:,0]*ns + ci[:,1])*ns + ci[:,2])*ns + ci[:,3]; ncell = nt*ns**3
    order = XP.argsort(cell); cs = cell[order]
    starts = XP.searchsorted(cs, XP.arange(ncell), side="left")
    poz = XP.arange(len(t)) - starts[cs]; keep = poz < bucket
    buck = XP.full((ncell, bucket), -1, dtype=XP.int32)
    buck[cs[keep], poz[keep]] = order[keep].astype(XP.int32)
    obc = 1 - float(keep.sum())/len(t)
    del ci, cell, order, cs, starts, poz, keep
    return buck, nt, ns, bucket, obc

OFF = XP.asarray(np.array([[a,b,c_,d] for a in (0,1) for b in (-1,0,1) for c_ in (-1,0,1) for d in (-1,0,1)], dtype=np.int32))
def kand(buck, t, x, tips, c, nt, ns):
    c0 = XP.stack([XP.floor(t[tips]/c), XP.floor(x[tips,0]/c), XP.floor(x[tips,1]/c), XP.floor(x[tips,2]/c)], 1).astype(XP.int32)
    cc = XP.clip(c0[:,None,:] + OFF[None,:,:], 0, XP.asarray([nt-1, ns-1, ns-1, ns-1], dtype=XP.int32))
    cid = ((cc[:,:,0]*ns + cc[:,:,1])*ns + cc[:,:,2])*ns + cc[:,:,3]
    return buck[cid].reshape(len(tips), -1)

def czterop(dt, dx):
    tau = XP.sqrt(XP.maximum(dt**2 - (dx**2).sum(-1), 1e-20))
    return dt/tau, dx/tau[...,None]

def przebieg(t, x, n, eps, rng):
    tau0 = (n/NMAX)**0.25
    rw = 5*wzor(tau0, eps)                           # okno wzglednego pchniecia: 5 x przewidywane rms (ogon ~ e^-100)
    etamax = np.arctanh(VMAX) + 3*wzor(tau0, eps)    # predkosc startu + dryf przez 3 kroki
    c = (1+eps)**1.3*tau0*np.cosh(etamax + rw)       # okno czasu pokrywa cale okno pchniec (z zapasem na dryf tref)
    buck, nt, ns, bucket, obc = siatka(t, x, c)
    P = max(1, int(PAMIEC/(54*bucket)))
    # starty: nisko w czasie, w srodku przestrzeni
    low = XP.where((t < 0.15*T_) & (XP.abs(x - S_/2).max(1) < 1.0))[0]
    tips = low[XP.asarray(rng.choice(int(len(low)), K, replace=False))].astype(XP.int32)
    vcel = rng.uniform(0, VMAX, K).astype(np.float32)
    kier = rng.normal(size=(K,3)).astype(np.float32); kier /= np.linalg.norm(kier, axis=1)[:,None]
    vcel_g, kier_g = XP.asarray(vcel), XP.asarray(kier)
    ch = [tips.copy()]; zyje = XP.ones(K, dtype=bool); tref = XP.full(K, tau0, dtype=XP.float32)
    R, TR = [], []                                   # wzgledne pchniecia i tref przy wyborze
    for krok in range(L-1):
        nxt = tips.copy(); ok_all = XP.zeros(K, dtype=bool); rk = XP.zeros(K, dtype=XP.float32); tk_all = XP.zeros(K, dtype=XP.float32)
        for s0 in range(0, K, P):
            sl = slice(s0, min(s0+P, K)); tp = tips[sl]
            C = kand(buck, t, x, tp, c, nt, ns); okc = C >= 0; ci = XP.where(okc, C, 0)
            dt = t[ci] - t[tp][:,None]; dx = x[ci] - x[tp][:,None,:]
            tk = XP.sqrt(XP.maximum(dt**2 - (dx**2).sum(-1), 0))
            tr = tref[sl][:,None]
            dobre = okc & (dt > 0) & (tk > (1-eps)*tr) & (tk < (1+eps)*tr) & (dt < c)
            if krok == 0:
                cel = x[tp][:,None,:] + (vcel_g[sl][:,None]*dt)[:,:,None]*kier_g[sl][:,None,:]
                score = -((x[ci] - cel)**2).sum(-1); r = XP.zeros_like(tk)
            else:
                p = ch[-2][sl]
                u0p, u1p = czterop(t[tp]-t[p], x[tp]-x[p])                       # 4-predkosc poprzedniego kroku
                u0c, u1c = czterop(dt, dx)
                r = XP.arccosh(XP.maximum(u0p[:,None]*u0c - (u1p[:,None,:]*u1c).sum(-1), 1.0))
                dobre &= r < rw
                tpc = XP.sqrt(XP.maximum((t[ci]-t[p][:,None])**2 - ((x[ci]-x[p][:,None,:])**2).sum(-1), 0))
                score = -(tpc - tr - tk)
            best = XP.argmax(XP.where(dobre, score, -1e30), axis=1); ar = XP.arange(len(tp))
            nxt[sl] = ci[ar, best]; ok_all[sl] = dobre.any(1); rk[sl] = r[ar, best]; tk_all[sl] = tk[ar, best]
            del C, okc, ci, dt, dx, tk, dobre, score, r
        # brzeg pudla: trajektoria musi miec cale okno w srodku
        tn, xn = t[nxt], x[nxt]
        wbrzeg = (tn < T_ - c) & (xn.min(1) > c) & (xn.max(1) < S_ - c)
        zyje &= ok_all & wbrzeg
        if krok > 0: R.append(rk); TR.append(tref.copy())
        tref = XP.where(ok_all, tk_all, tref); tips = XP.where(ok_all, nxt, tips).astype(XP.int32); ch.append(tips.copy())
        if GPU: cp.get_default_memory_pool().free_all_blocks()
    del buck
    if GPU: cp.get_default_memory_pool().free_all_blocks()
    z = tonp(zyje); R = tonp(XP.stack(R, 1))[z]; TR = tonp(XP.stack(TR, 1))[z]
    return R, TR, vcel[z], dict(c=c, bucket=bucket, obciete=obc, P=P, zywych=int(z.sum()))

res = json.load(open(CKPT)) if os.path.exists(CKPT) else {}
rs = XP.random.RandomState(SEED)
Npkt = int(RHO*T_*S_**3)
log(f"GPU={GPU} | rho={RHO:.0f} | punktow {Npkt/1e6:.1f} mln")
t = rs.uniform(0, T_, Npkt).astype(XP.float32); x = rs.uniform(0, S_, (Npkt,3)).astype(XP.float32)
rng = np.random.default_rng(SEED + 99)
for eps in EPSS:
    for n in NS:
        key = f"{WERSJA}|{eps}|{n}"
        if key in res: log(f"eps={eps} n={n}: z checkpointu"); continue
        t0 = time.time()
        R, TR, vc, info = przebieg(t, x, n, eps, rng)
        if len(R) < 20: log(f"eps={eps} n={n}: za malo zywych ({len(R)})"); continue
        Z = R / wzor(TR, eps)                                              # znormowane lokalnym tref
        a, b = R[:,:-1].ravel(), R[:,1:].ravel()
        wyn = dict(rms=float(np.sqrt((R**2).mean())), q2=float(np.sqrt((Z**2).mean())),
                   q3_wolne=float(np.sqrt((Z[vc < 0.3]**2).mean())), q3_szybkie=float(np.sqrt((Z[vc >= 0.3]**2).mean())),
                   r1=float(np.corrcoef(a, b)[0,1]), wzor_nom=float(wzor((n/NMAX)**0.25, eps)), **info)
        res[key] = wyn; json.dump(res, open(CKPT, "w"), indent=1)
        log(f"eps={eps} n={n:5d}: rms {wyn['rms']:.5f} (wzor {wyn['wzor_nom']:.5f}) | Q2 {wyn['q2']:.3f} | "
            f"Q3 {wyn['q3_wolne']:.3f}/{wyn['q3_szybkie']:.3f} | r1 {wyn['r1']:+.3f} | zywych {info['zywych']} | "
            f"obciete {info['obciete']:.2%} | {time.time()-t0:.0f}s")

log("\nPODSUMOWANIE")
for eps in EPSS:
    w = [(n, res[f"{WERSJA}|{eps}|{n}"]) for n in NS if f"{WERSJA}|{eps}|{n}" in res]
    if len(w) >= 3:
        pot = np.polyfit(np.log([q[0] for q in w]), np.log([q[1]["rms"] for q in w]), 1)[0]
        q2 = ", ".join("%.3f" % q[1]["q2"] for q in w if q[0] >= 10)
        log(f"  eps={eps}: Q1 wykladnik = {pot:+.4f} (przewidywane -0,333 +- 0,03) | Q2 (n>=10) = {q2}")
