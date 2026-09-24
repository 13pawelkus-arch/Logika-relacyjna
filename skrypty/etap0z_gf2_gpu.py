"""
Prawdziwa ranga niewypelnionej czesci nad GF(2) przy duzym N (A100).
D_prawdziwe = beta1 - rank(brzegi scian) = D_gorne + dim H2.

GPU: C, C^2, C^3, linki, sciany, elementy srodkowe scian (wsadowo), indeksy linkow.
CPU: skladowe (graf rzadki) i eliminacja nad GF(2) (wiersze po 4 linki, pivot = najmniejszy indeks).
Checkpoint po kazdym N do etap0z_gf2_wyniki.json.

Na CPU (N<=6000) wyszlo: ranga scian = 0,86*F, D_prawdziwe/beta1 -> 0,60, D/N ~ 0,56*ln N.
ZDANIA DO UPADKU przy 16000-32000:
  (a) ranga scian / F zostaje 0,86 (+-0,01)
  (b) D_prawdziwe/beta1 zostaje 0,60 (+-0,01)
  (c) przyrost D_prawdziwe/el na podwojenie N zostaje ~0,39 (logarytm, 0,56*ln N)
"""
import numpy as np, json, os, time
try:
    import cupy as cp; XP = cp; GPU = True
except ImportError:
    XP = np; GPU = False
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

Ns    = [16000, 24000, 32000]
SEEDS = [1, 2]
CKPT  = "etap0z_gf2_wyniki.json"
BATCH = 4096

def free():
    if GPU: cp.get_default_memory_pool().free_all_blocks()
def to_np(a): return cp.asnumpy(a) if GPU else a

def build(N, seed):
    rs = XP.random.RandomState(seed)
    u, v = rs.rand(N), rs.rand(N)
    C  = (u[:, None] < u[None, :]) & (v[:, None] < v[None, :])
    Cf = C.astype(XP.float32)
    IV = Cf @ Cf
    L  = C & (IV < 0.5)
    C3 = IV @ Cf
    FM = (IV == 2) & C & (C3 == 0)                 # sciany
    del C3, Cf; free()
    FP, FQ = XP.where(FM); del FM, IV; free()
    # indeksy linkow: klucz i*N+j, posortowany
    LP, LQ = XP.where(L)
    keys = LP.astype(XP.int64) * N + LQ.astype(XP.int64)   # juz posortowane (row-major)
    E = int(len(keys))
    Lc = to_np(L); del L; free()
    ncomp, _ = connected_components(csr_matrix(Lc | Lc.T), directed=False); del Lc
    beta1 = E - N + int(ncomp)
    # elementy srodkowe scian, wsadowo: C[p,:] & C[:,q]
    edges = []
    for s in range(0, len(FP), BATCH):
        p = FP[s:s+BATCH]; q = FQ[s:s+BATCH]
        mid = C[p, :] & C[:, q].T                  # (batch, N), w kazdym wierszu dokladnie 2
        r, z = XP.where(mid)
        z = z.reshape(-1, 2); a, b = z[:, 0], z[:, 1]
        k = XP.stack([p.astype(XP.int64)*N + a, p.astype(XP.int64)*N + b,
                      a.astype(XP.int64)*N + q,   b.astype(XP.int64)*N + q], axis=1)
        idx = XP.searchsorted(keys, k)
        edges.append(to_np(idx))
        del mid, r, z, a, b, k, idx
    del C, keys, FP, FQ; free()
    edges = np.concatenate(edges) if edges else np.zeros((0, 4), np.int64)
    return beta1, E, edges

def rank_gf2(rows):
    piv = {}; r = 0
    for row in rows:
        row = set(int(x) for x in row)
        while row:
            p = min(row)
            if p in piv: row ^= piv[p]
            else: piv[p] = row; r += 1; break
    return r

res = json.load(open(CKPT)) if os.path.exists(CKPT) else {}
for N in Ns:
    for s in SEEDS:
        key = f"{N}|{s}"
        if key in res: print(f"  N={N} s={s} z checkpointu"); continue
        t0 = time.time()
        try:
            b1, E, edges = build(N, s)
        except Exception as e:
            print(f"  !! N={N} s={s} pominiete: {type(e).__name__}"); free(); continue
        t1 = time.time(); rk = rank_gf2(edges); t2 = time.time()
        F = len(edges)
        res[key] = dict(N=N, beta1=b1, E=E, F=F, rank=rk, t_gpu=t1-t0, t_gf2=t2-t1)
        json.dump(res, open(CKPT, "w"))
        print(f"  N={N} s={s}: F={F} rank={rk} dimH2={F-rk} | GPU {t1-t0:.0f}s, GF(2) {t2-t1:.0f}s", flush=True)

print("\n   N   | beta1/el | F/el | rank/F | dimH2/el | D_gorne/el | D_prawdz/el | D/beta1")
rows = []
for N in sorted({v["N"] for v in res.values()}):
    vs = [v for v in res.values() if v["N"] == N]
    b1 = np.mean([v["beta1"] for v in vs]); F = np.mean([v["F"] for v in vs]); rk = np.mean([v["rank"] for v in vs])
    print(f"{N:6d} | {b1/N:8.3f} | {F/N:4.2f} | {rk/F:6.3f} | {(F-rk)/N:8.3f} | {(b1-F)/N:10.3f} | {(b1-rk)/N:11.3f} | {(b1-rk)/b1:.3f}")
    rows.append([N, (b1-rk)/N])
rows = np.array(rows)
if len(rows) > 1:
    d = [(rows[k+1,1]-rows[k,1])/np.log2(rows[k+1,0]/rows[k,0]) for k in range(len(rows)-1)]
    print("przyrost D_prawdz/el na podwojenie N:", ", ".join(f"{x:+.3f}" for x in d), " (oczekiwane ~0,39)")
