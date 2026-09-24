"""
Skaner niewypelnialnych cykli (d=2) - wersja w pelni wektorowa, A100.

Dwie tozsamosci z definicji linku usuwaja wszystkie petle w Pythonie:
  1. Sciana = przedzial p<q z DOKLADNIE 2 elementami, wzajemnie nieporownywalnymi.
     Te dwa sa porownywalne <=> istnieje sciezka dlugosci 3 z p do q.
     Wiec: sciana <=> C[p,q] i (C^2)[p,q]==2 i (C^3)[p,q]==0.
  2. Dwa rozne nastepniki linkowe tego samego elementu SA nieporownywalne
     (gdyby b1<b2, to a->b2 nie byloby linkiem). Symetrycznie dla poprzednikow.
     Wiec liczba koron = sum_{a1<a2} C(M,2),  M = L @ L^T.
  (Obie sprawdzone na CPU co do sztuki; stara petla koron liczyla tez przekatna.)

Pamiec przy N: kazda macierz float32 to 4*N^2 bajtow (N=24000 -> 2,3 GB).
Szczyt ~5 takich macierzy naraz -> N=32000 ok. 12 GB... uwaga na 40 GB przy 40000.
Generator CuPy != NumPy: to sa niezalezne realizacje, nie reprodukcja.
"""
import numpy as np, cupy as cp
from scipy.sparse.csgraph import connected_components as cc_cpu
from scipy.sparse import csr_matrix as csr_cpu

Ns    = [1000, 2000, 4000, 8000, 16000, 24000, 32000]
SEEDS = [1, 2, 3]

def free(): cp.get_default_memory_pool().free_all_blocks()

def scan_gpu(N, seed):
    rs = cp.random.RandomState(seed)
    u, v = rs.rand(N), rs.rand(N)
    C  = (u[:, None] < u[None, :]) & (v[:, None] < v[None, :])
    Cf = C.astype(cp.float32)
    IV = Cf @ Cf                                   # liczba elementow w przedziale
    L  = C & (IV < 0.5)                            # linki
    E  = int(L.sum())
    C3 = IV @ Cf                                   # sciezki dlugosci 3 (test porownywalnosci)
    F  = int(((IV == 2) & C & (C3 == 0)).sum())    # sciany
    del C3, Cf; free()
    Lf = L.astype(cp.float32)
    M  = Lf @ Lf.T                                 # wspolni nastepnicy linkowi
    kor = float(cp.triu(M * (M - 1) / 2, 1).sum(dtype=cp.float64))
    del M, Lf, IV, C; free()
    # skladowe: graf linkow jest rzadki -> na CPU tanio
    Lc = cp.asnumpy(L); del L; free()
    G = csr_cpu(Lc | Lc.T); ncomp, _ = cc_cpu(G, directed=False)
    beta1 = E - N + ncomp
    return E, F, beta1, kor, ncomp

print("   N   | linkow/el | scian/el | beta1/el | D=(beta1-F)/el | korony/el | skladowe")
res = []
for N in Ns:
    try:
        r = np.array([scan_gpu(N, s) for s in SEEDS], dtype=float).mean(axis=0)
    except Exception as e:
        print(f"  !! N={N} pominiete: {type(e).__name__}"); free(); continue
    E, F, b1, kor, nc = r
    print(f"{N:6d} | {E/N:9.3f} | {F/N:8.3f} | {b1/N:8.3f} | {(b1-F)/N:14.3f} | {kor/N:9.3f} | {nc:.0f}", flush=True)
    res.append([N, E/N, F/N, (b1-F)/N, kor/N])

res = np.array(res)
print("\nprzyrosty na podwojenie N (stale = logarytm):")
for i, nm in [(1,"linkow/el"),(2,"scian/el"),(3,"D/el"),(4,"korony/el")]:
    d = [(res[k+1,i]-res[k,i])/np.log2(res[k+1,0]/res[k,0]) for k in range(len(res)-1)]
    a = np.polyfit(np.log(res[:,0]), res[:,i], 1)[0]
    print(f"  {nm:10s}: " + ", ".join(f"{x:+.3f}" for x in d) + f"   | dopasowanie: {a:.3f}*ln N + ...")
