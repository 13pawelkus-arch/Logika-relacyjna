"""
REGULA R-KAT NA PELNYM SPRINKLINGU 3+1 — krotkie lancuchy (Colab A100 40 GB). Na bazie etap11 v2.
Po co: etap16 (20 krokow, gestosc z etap8) okazal sie zdominowany przez okno kandydatow w ukladzie pudla
(n_A ~ 0,3, n_B ~ 1,5 el./tykn. -> pchniecie bladzi ~0,4-0,7 na krok, okno odcina 50-80% krokow A od kroku ~7;
etap16b). Dlugie lancuchy w gestym rezimie wymagalyby ~10^9-10^10 punktow. Dlatego: waliduje sie REDUKCJE
LOKALNA dla R-KAT (dotad sprawdzona na pelnym sprinklingu tylko dla r, regula nadwyzki - etap11) na
krotkich lancuchach (3 kroki pamieci), z oknem 4 x rms pchniecia, jak w etap11.
Regula R-KAT: s = ln(tk/tref) w [delta-eps, delta+eps], delta = -(eps coth(4 eps) - 1/4); wybor: najmniejsze r.

ZDANIA DO UPADKU (przed przebiegiem):
  G1. srednia s = 0: |srednia| < 3 bledy statystyczne i < 0,1 sqrt(var_s)       (brak dryfu tempa)
  G2. var(s) / var_s = 1,00 +- 0,03                                              (tk ma rozklad miary pasma)
  G3. rms(r) / wzor (lam3 pasma logarytmicznego, lokalny tref) = 1,00 +- 0,05
  G4. |korelacja(s, r)| < 0,02                                                   (niezaleznosc tempa i ramy)
v2 (po tescie CPU v1: sr(s) -0,006/-0,008, z = -1,8/-2,4 przy 100 trajektoriach): okno c liczone z zapasem
  na bladzenie tref (3 sigma przez 3 kroki); v1 liczylo c od tau0 i moglo obcinac gorny skraj pasma.
Jesli G1-G4 przejda: wyniki §F1 dla R-KAT wynikaja z redukcji lokalnej (tam niezaleznosc od v jest dokladna
z niezmienniczosci), bez potrzeby dlugich przebiegow w pudle.
"""
import numpy as np, json, os, sys, time
from math import gamma, pi
try:
    import cupy as cp; XP = cp; GPU = True
except ImportError:
    XP = np; GPU = False

# ---------------- PARAMETRY ----------------
NS     = [10, 30, 100, 300, 1000]               # 2 dekady (3000 pominiete: okno x1,3 -> koszt x3)
EPSS   = [0.05, 0.10, 0.20]
NMAX   = 3000                                   # przy tau = 1; rho = 24*NMAX/pi ~ 22 900
K      = 1000                                   # trajektorii na (n, eps); 3000 przyrostow -> blad sr(s) ~0,001
L      = 5                                      # kroki: 0 (cel zewn.) + 3 kroki pamieci -> 3 przyrosty r
VMAX   = 0.6
T_, S_ = 8.0, 10.0                              # pudlo w jednostkach tau(NMAX) = 1  -> ~183 mln punktow (2,9 GB)
SEED   = 1
PAMIEC = 1.2e8                                  # elementow kandydatow na porcje (~8 GB na A100 40 GB; przy 80 GB mozna 2.5e8)
LIMIT_SIATKI = 10e9                             # bajtow na siatke kubelkow (A100 40 GB); przy 80 GB mozna 25e9
CKPT   = "etap17_rkat.json"
WERSJA = "rkat-v2"
if len(sys.argv) > 1 and sys.argv[1] == "test":                 # szybki test logiki na CPU
    NS, NMAX, K, EPSS, CKPT = [30, 100, 300], 300, 100, [0.10], "test11.json"
# -------------------------------------------

def log(s): print(s, flush=True)
def tonp(a): return cp.asnumpy(a) if GPU else np.asarray(a)
RHO = 24*NMAX/pi
SQG = np.sqrt(gamma(5/3))
def delta(eps): return -(eps/np.tanh(4*eps) - 0.25)
def var_s(eps):
    xx = np.linspace(-eps, eps, 20001); w = np.exp(4*xx); m = (xx*w).sum()/w.sum(); return float(((xx-m)**2*w).sum()/w.sum())
def wzor(tref, eps):
    de = delta(eps); lam3 = RHO*tref**4*(np.exp(4*(de+eps)) - np.exp(4*(de-eps)))/4
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
    rw = 4*wzor(tau0, eps)                           # okno wzglednego pchniecia: 4 x przewidywane rms (ogon ~ e^-75)
    etamax = np.arctanh(VMAX) + 3*wzor(tau0, eps)    # predkosc startu + dryf przez 3 kroki
    # v2: zapas na bladzenie tref przez 3 kroki (3 sigma) - v1 (zapas (1+eps)^1.3) obcinal gorny skraj pasma
    c = np.exp(delta(eps) + eps + 3*np.sqrt(3*var_s(eps)))*tau0*np.cosh(etamax + rw)
    # BEZPIECZNIK (v2): pamiec siatki i miejsce w pudle sprawdzane PRZED alokacja
    lam = RHO*c**4; bucket_est = lam + 6*np.sqrt(lam) + 10
    ncell_est = (int(np.ceil(T_/c))+2)*(int(np.ceil(S_/c))+2)**3
    if ncell_est*bucket_est*4 > LIMIT_SIATKI or 2*c > S_ - 2.5:
        log(f"  eps={eps} n={n}: POMINIETE — okno c={c:.2f}, siatka {ncell_est*bucket_est*4/1e9:.1f} GB "
            f"(limit {LIMIT_SIATKI/1e9:.0f} GB) lub pudlo za male")
        return None
    buck, nt, ns, bucket, obc = siatka(t, x, c)
    P = max(1, int(PAMIEC/(54*bucket)))
    # starty: nisko w czasie, w srodku przestrzeni
    low = XP.where((t < 0.15*T_) & (XP.abs(x - S_/2).max(1) < 0.5))[0]
    tips = low[XP.asarray(rng.choice(int(len(low)), K, replace=False))].astype(XP.int32)
    vcel = rng.uniform(0, VMAX, K).astype(np.float32)
    kier = rng.normal(size=(K,3)).astype(np.float32); kier /= np.linalg.norm(kier, axis=1)[:,None]
    vcel_g, kier_g = XP.asarray(vcel), XP.asarray(kier)
    ch = [tips.copy()]; zyje = XP.ones(K, dtype=bool); tref = XP.full(K, tau0, dtype=XP.float32)
    R, TR, SS = [], [], []                                   # wzgledne pchniecia i tref przy wyborze
    for krok in range(L-1):
        nxt = tips.copy(); ok_all = XP.zeros(K, dtype=bool); rk = XP.zeros(K, dtype=XP.float32); sk_all = XP.zeros(K, dtype=XP.float32); tk_all = XP.zeros(K, dtype=XP.float32)
        for s0 in range(0, K, P):
            sl = slice(s0, min(s0+P, K)); tp = tips[sl]
            C = kand(buck, t, x, tp, c, nt, ns); okc = C >= 0; ci = XP.where(okc, C, 0)
            dt = t[ci] - t[tp][:,None]; dx = x[ci] - x[tp][:,None,:]
            tk = XP.sqrt(XP.maximum(dt**2 - (dx**2).sum(-1), 0))
            tr = tref[sl][:,None]
            sk = XP.log(XP.maximum(tk, 1e-12)/tr); de = delta(eps)
            dobre = okc & (dt > 0) & (sk > de-eps) & (sk < de+eps) & (dt < c)
            if krok == 0:
                cel = x[tp][:,None,:] + (vcel_g[sl][:,None]*dt)[:,:,None]*kier_g[sl][:,None,:]
                score = -((x[ci] - cel)**2).sum(-1); r = XP.zeros_like(tk)
            else:
                p = ch[-2][sl]
                u0p, u1p = czterop(t[tp]-t[p], x[tp]-x[p])                       # 4-predkosc poprzedniego kroku
                u0c, u1c = czterop(dt, dx)
                r = XP.arccosh(XP.maximum(u0p[:,None]*u0c - (u1p[:,None,:]*u1c).sum(-1), 1.0))
                dobre &= r < rw
                score = -r                                                        # R-KAT: najmniejsze wzgledne pchniecie
            best = XP.argmax(XP.where(dobre, score, -1e30), axis=1); ar = XP.arange(len(tp))
            nxt[sl] = ci[ar, best]; ok_all[sl] = dobre.any(1); rk[sl] = r[ar, best]; tk_all[sl] = tk[ar, best]; sk_all[sl] = sk[ar, best]
            del C, okc, ci, dt, dx, tk, dobre, score, r, sk
        # brzeg pudla: trajektoria musi miec cale okno w srodku
        tn, xn = t[nxt], x[nxt]
        wbrzeg = (tn < T_ - c) & (xn.min(1) > c) & (xn.max(1) < S_ - c)
        zyje &= ok_all & (wbrzeg if krok < L-2 else True)       # ostatni koniec juz nie szuka -> nie potrzebuje okna
        if krok > 0: R.append(rk); TR.append(tref.copy()); SS.append(sk_all)
        tref = XP.where(ok_all, tk_all, tref); tips = XP.where(ok_all, nxt, tips).astype(XP.int32); ch.append(tips.copy())
        if GPU: cp.get_default_memory_pool().free_all_blocks()
    del buck
    if GPU: cp.get_default_memory_pool().free_all_blocks()
    z = tonp(zyje); R = tonp(XP.stack(R, 1))[z]; TR = tonp(XP.stack(TR, 1))[z]; SS = tonp(XP.stack(SS, 1))[z]
    return R, TR, SS, vcel[z], dict(c=c, bucket=bucket, obciete=obc, P=P, zywych=int(z.sum()))

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
        out = przebieg(t, x, n, eps, rng)
        if out is None: continue
        R, TR, SS, vc, info = out
        if len(R) < 20: log(f"eps={eps} n={n}: za malo zywych ({len(R)})"); continue
        Z = R / wzor(TR, eps); sf = SS.ravel()
        wyn = dict(sr_s=float(sf.mean()), blad_s=float(sf.std()/np.sqrt(len(sf))), G2=float(sf.var()/var_s(eps)),
                   G3=float(np.sqrt((Z**2).mean())), G4=float(np.corrcoef(sf, R.ravel())[0,1]),
                   q3_wolne=float(np.sqrt((Z[vc < 0.3]**2).mean())), q3_szybkie=float(np.sqrt((Z[vc >= 0.3]**2).mean())), **info)
        res[key] = wyn; json.dump(res, open(CKPT, "w"), indent=1)
        log(f"eps={eps} n={n:5d}: G1 sr(s) {wyn['sr_s']:+.5f} +- {wyn['blad_s']:.5f} (z={wyn['sr_s']/wyn['blad_s']:+.1f}; "
            f"/sqrt(var_s) {wyn['sr_s']/np.sqrt(var_s(eps)):+.3f}) | G2 {wyn['G2']:.3f} | G3 {wyn['G3']:.3f} "
            f"(wolne/szybkie {wyn['q3_wolne']:.3f}/{wyn['q3_szybkie']:.3f}) | G4 {wyn['G4']:+.3f} | zywych {info['zywych']} | {time.time()-t0:.0f}s")
log('KONIEC — wklej wszystkie linie eps=... n=...')
