"""
Test ulamkow 6/7, 7/15, 3/5 z ekstrapolacja do granicy (A100).

USTALONE PRZED RACHUNKIEM:
  Model zbieznosci: r(N) = r_inf + c / ln N, dopasowanie na N = 2000 ... 32000.
  (Wszystkie liczniki rosna jak ln N, wiec poprawki do stosunkow ~ 1/ln N.)
  UWAGA O DZWIGNI: 1/ln N obejmuje tylko 0,132-0,096; ekstrapolacja do 0 wzmacnia bledy ~2,7x.
  Dlatego werdykt ma trzy stany: PRZESZLO / UPADLO tylko gdy niepewnosc r_inf <= 0,003,
  inaczej NIEROZSTRZYGALNE (test nie ma rozdzielczosci, zadne zdanie nie jest rozstrzygniete).
  ZDANIA DO UPADKU:
    Z1. r_inf(ranga/F)  = 6/7  = 0,85714 +- 0,003
    Z2. r_inf(F/beta1)  = 7/15 = 0,46667 +- 0,003
    Z3. r_inf(D/beta1)  = 3/5  = 0,60000 +- 0,003
    Z4. r_inf dla trzech geometrii zgadza sie w +- 0,003 (uniwersalnosc granicy)
  8 ziaren na punkt. Geometrie: diament, kwadrat (t,x), szerokie pudlo 2 x 0,5.

GPU: C, C^2, C^3, linki, sciany, elementy srodkowe (wsadowo). CPU: skladowe, eliminacja GF(2).
Checkpoint po kazdym (geometria, N, ziarno) do etap0z_ulamki.json.
"""
import numpy as np, json, os, time
try:
    import cupy as cp; XP = cp; GPU = True
except ImportError:
    XP = np; GPU = False
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

GEOMS = ["diament", "kwadrat", "szerokie"]
Ns    = [2000, 4000, 8000, 16000, 24000, 32000]
SEEDS = range(1, 9)
CKPT  = "etap0z_ulamki.json"
BATCH = 4096
CEL   = {"ranga/F": 6/7, "F/beta1": 7/15, "D/beta1": 3/5}

def free():
    if GPU: cp.get_default_memory_pool().free_all_blocks()
def to_np(a): return cp.asnumpy(a) if GPU else a

def causal(N, seed, geom):
    rs = XP.random.RandomState(seed)
    a, b = rs.rand(N).astype(XP.float32), rs.rand(N).astype(XP.float32)
    if geom == "diament":
        t, x = (a + b) / np.float32(np.sqrt(2)), (a - b) / np.float32(np.sqrt(2))
    elif geom == "kwadrat":
        t, x = a, b
    else:
        t, x = np.float32(0.5) * a, np.float32(2.0) * b
    return (t[None, :] - t[:, None]) > XP.abs(x[None, :] - x[:, None])

def stats(N, seed, geom):
    C  = causal(N, seed, geom); free()
    Cf = C.astype(XP.float32)
    IV = Cf @ Cf
    L  = C & (IV < 0.5)
    C3 = IV @ Cf
    FM = (IV == 2) & C & (C3 == 0)
    del C3, Cf; free()
    FP, FQ = XP.where(FM); del FM, IV; free()
    LP, LQ = XP.where(L)
    keys = LP.astype(XP.int64) * N + LQ.astype(XP.int64)
    E = int(len(keys))
    Lc = to_np(L); del L; free()
    nc, _ = connected_components(csr_matrix(Lc | Lc.T), directed=False); del Lc
    b1 = E - N + int(nc)
    rows = []
    for s in range(0, len(FP), BATCH):
        p = FP[s:s+BATCH]; q = FQ[s:s+BATCH]
        mid = C[p, :] & C[:, q].T
        _, z = XP.where(mid); z = z.reshape(-1, 2); a, b = z[:, 0], z[:, 1]
        k = XP.stack([p.astype(XP.int64)*N + a, p.astype(XP.int64)*N + b,
                      a.astype(XP.int64)*N + q,   b.astype(XP.int64)*N + q], axis=1)
        rows.append(to_np(XP.searchsorted(keys, k))); del mid, z, a, b, k
    del C, keys, FP, FQ; free()
    rows = np.concatenate(rows) if rows else np.zeros((0, 4), np.int64)
    piv = {}; r = 0
    for row in rows:
        row = set(int(v) for v in row)
        while row:
            m = min(row)
            if m in piv: row ^= piv[m]
            else: piv[m] = row; r += 1; break
    F = len(rows)
    return {"ranga/F": r / F, "F/beta1": F / b1, "D/beta1": (b1 - r) / b1}

res = json.load(open(CKPT)) if os.path.exists(CKPT) else {}
for g in GEOMS:
    for N in Ns:
        for s in SEEDS:
            key = f"{g}|{N}|{s}"
            if key in res: continue
            t0 = time.time()
            try:
                res[key] = stats(N, s, g)
            except Exception as e:
                print(f"  !! {key} pominiete: {type(e).__name__}"); free(); continue
            json.dump(res, open(CKPT, "w"))
            print(f"  {key}: " + "  ".join(f"{k}={v:.4f}" for k, v in res[key].items())
                  + f"   ({time.time()-t0:.0f}s)", flush=True)

print("\nEKSTRAPOLACJA r(N) = r_inf + c/ln N  (model ustalony przed rachunkiem)")
rinf = {}
for g in GEOMS:
    print(f"\n{g}:")
    for q, cel in CEL.items():
        xs, ys, es = [], [], []
        for N in Ns:
            v = [res[f"{g}|{N}|{s}"][q] for s in SEEDS if f"{g}|{N}|{s}" in res]
            if len(v) < 2: continue
            xs.append(1/np.log(N)); ys.append(np.mean(v)); es.append(np.std(v, ddof=1)/np.sqrt(len(v)))
        if len(xs) < 3:
            print(f"  {q}: za malo punktow"); continue
        xs, ys, es = map(np.array, (xs, ys, es))
        (c, r0), cov = np.polyfit(xs, ys, 1, w=1/es, cov="unscaled")
        dr = np.sqrt(cov[1, 1]); rinf[(g, q)] = (r0, dr)
        if dr > 0.003: wer = "NIEROZSTRZYGALNE (niepewnosc > 0,003)"
        else: wer = "PRZESZLO" if abs(r0 - cel) <= 0.003 else "UPADLO"
        print(f"  {q:8s}: punkty " + ", ".join(f"{y:.4f}±{e:.4f}" for y, e in zip(ys, es))
              + f" | r_inf = {r0:.4f} ± {dr:.4f}  cel {cel:.4f}  -> {wer}")

print("\nZ4: uniwersalnosc granicy (rozrzut r_inf miedzy geometriami, prog 0,003)")
for q in CEL:
    v = [rinf[(g, q)][0] for g in GEOMS if (g, q) in rinf]
    if len(v) > 1:
        dmax = max(rinf[(g, q)][1] for g in GEOMS if (g, q) in rinf)
        wer = "NIEROZSTRZYGALNE" if dmax > 0.003 else ("PRZESZLO" if max(v)-min(v) <= 0.003 else "UPADLO")
        print(f"  {q:8s}: " + ", ".join(f"{x:.4f}" for x in v)
              + f"  rozrzut {max(v)-min(v):.4f} (max niepewnosc {dmax:.4f}) -> {wer}")
