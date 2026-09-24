"""
Czy suma po petlach jest zbiezna po unormowaniu miara? (d=2, GPU)

RACHUNEK WYMIAROWY (przed liczeniem): dzialanie ~ integral F^2 dV ma wymiar F^2 L^2;
petla niesie faze F*Sigma, Sigma ma wymiar L^2, wiec (F*Sigma)^2 ma F^2 L^4.
Waga musi miec wymiar L^-2, czyli byc proporcjonalna do gestosci rho. Bez swobody.

ZDANIE DO UPADKU:  rho * suma(Sigma^2) po minimalnych petlach NIE zalezy od N.
  wykladnik 0    -> "superekstensywnosc" byla artefaktem zliczania
  wykladnik > 0  -> brak jest prawdziwy, wagi nie wystarcza

Stan na CPU (0,9 dekady, N=600..4800): liczba petli ~ N^1,221, suma wazona ~ N^0,226,
nachylenia lokalne maleja (0,34 -> 0,14). Potrzeba 2 dekad, zeby rozstrzygnac.

Minimalna petla: para p<q, ktorej przedzial zawiera DOKLADNIE 2 elementy, wzajemnie
nieporownywalne. Sigma = pole czworokata (p,x,q,y) we wspolrzednych stozkowych.
"""
import numpy as np
try:
    import cupy as cp; XP = cp; GPU = True
except ImportError:
    XP = np; GPU = False

Ns    = [1200, 2400, 4800, 9600, 19200, 38400]   # 38400: macierz bool 1,5 GB, C@C w float16/32
SEEDS = [1, 2, 3]

def run(N, seed):
    rng = XP.random.default_rng(seed)
    u, v = rng.random(N), rng.random(N)
    C = (u[:, None] < u[None, :]) & (v[:, None] < v[None, :])
    Cf = C.astype(XP.float32)
    IV = Cf @ Cf                      # liczba elementow w przedziale
    del Cf
    if GPU: cp.get_default_memory_pool().free_all_blocks()
    mask = (IV > 1.5) & (IV < 2.5) & C
    del IV
    P, Q = XP.where(mask)
    P = cp.asnumpy(P) if GPU else P; Q = cp.asnumpy(Q) if GPU else Q
    Cc = cp.asnumpy(C) if GPU else C
    uu = cp.asnumpy(u) if GPU else u; vv = cp.asnumpy(v) if GPU else v
    del C
    if GPU: cp.get_default_memory_pool().free_all_blocks()
    S2 = 0.0; n = 0
    for p, q in zip(P, Q):
        I = np.where(Cc[p] & Cc[:, q])[0]
        if len(I) != 2: continue
        a, b = I
        if Cc[a, b] or Cc[b, a]: continue           # musza byc nieporownywalne
        pts = [(uu[p], vv[p]), (uu[a], vv[a]), (uu[q], vv[q]), (uu[b], vv[b])]
        A = 0.5 * abs(sum(pts[i][0]*pts[(i+1) % 4][1] - pts[(i+1) % 4][0]*pts[i][1] for i in range(4)))
        S2 += A*A; n += 1
    return n, S2

print(f"backend: {'CuPy/GPU' if GPU else 'NumPy/CPU'}")
print("  N    | liczba petli | rho*sum(Sigma^2)")
res = []
for N in Ns:
    try:
        out = [run(N, s) for s in SEEDS]
    except Exception as e:
        print(f"  !! N={N} pominiete: {type(e).__name__}"); continue
    n = np.mean([o[0] for o in out]); S = np.mean([o[1] for o in out])
    print(f"{N:6d} | {n:11.0f}  | {N*S:10.4f}", flush=True)
    res.append([N, n, N*S])
res = np.array(res)
lg = lambda y: np.polyfit(np.log(res[:, 0]), np.log(y), 1)[0]
print(f"\nwykladnik liczby petli : {lg(res[:,1]):+.3f}   (1 = ekstensywna)")
print(f"wykladnik sumy wazonej : {lg(res[:,2]):+.3f}   (0 = zbiezna)")
print("nachylenia lokalne sumy wazonej (kolejne pary punktow):")
for i in range(len(res)-1):
    e = np.log(res[i+1,2]/res[i,2]) / np.log(res[i+1,0]/res[i,0])
    print(f"  N={res[i,0]:.0f} -> {res[i+1,0]:.0f}: {e:+.3f}")
