# etap19 — działanie w dwóch sektorach jako funkcja obiegów (poprawka 162)
#
# Pytanie: czy „działanie = obroty fazy” obejmuje grawitację tak samo jak cechowanie,
# czy potrzebne są dwie postacie. Nośnik wspólny do sprawdzenia: OBIEGI (pętle, holonomie).
#
# Zdania do upadku (zapisane przed rachunkiem):
#  Z1 (grawitacja, Regge 2D): kąt holonomii transportu równoległego wokół wierzchołka,
#      liczony NIEZALEŻNIE (przenoszenie wektora przez wspólne krawędzie ścian),
#      = deficyt 2π − Σ kątów przy wierzchołku, dla każdego wierzchołka, do 1e-9.
#  Z2: Σ_v deficyt = 2π·χ = 4π (sfera) do 1e-9  — suma obiegów po zamkniętym brzegu 2D = liczba.
#  Z3 (cechowanie U(1)): działanie Wilsona S_W = Σ_f (1 − cos θ_f) nie zmienia się przy
#      losowej fazie w wierzchołkach (faza w punkcie ≡ Ø) do 1e-9;
#      kontrola: „działanie” z faz na krawędziach S_L = Σ_e (1 − cos a_e) ZMIENIA się.
#  Z4: Σ_f θ_f (θ_f w (−π, π]) = 2π·n, n całkowite — suma obiegów po zamkniętym brzegu 2D = liczba.
#  K  (kontrola płaska): wierzchołek wewnętrzny płaskiej siatki: deficyt = 0 i holonomia = 0.
#
# Parametry na górze; tylko numpy; czas < 1 s.
import numpy as np

SEED = 1
PODZIAL = 3          # podział dwudziestościanu (liczba trójkątów = 20·4^PODZIAL)
SZUM = 0.25          # losowe zaburzenie promienia wierzchołków (kształt, nie topologia)
TOL = 1e-9

rng = np.random.default_rng(SEED)

def dwudziestoscian():
    t = (1 + 5 ** 0.5) / 2
    V = np.array([[-1, t, 0], [1, t, 0], [-1, -t, 0], [1, -t, 0], [0, -1, t], [0, 1, t],
                  [0, -1, -t], [0, 1, -t], [t, 0, -1], [t, 0, 1], [-t, 0, -1], [-t, 0, 1]], float)
    F = [[0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11], [1, 5, 9], [5, 11, 4],
         [11, 10, 2], [10, 7, 6], [7, 1, 8], [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8],
         [3, 8, 9], [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1]]
    return list(V / np.linalg.norm(V, axis=1)[:, None]), F

def podziel(V, F):
    V = list(V); cache = {}
    def srodek(a, b):
        k = (min(a, b), max(a, b))
        if k not in cache:
            m = (V[a] + V[b]) / 2; V.append(m / np.linalg.norm(m)); cache[k] = len(V) - 1
        return cache[k]
    G = []
    for a, b, c in F:
        ab, bc, ca = srodek(a, b), srodek(b, c), srodek(c, a)
        G += [[a, ab, ca], [b, bc, ab], [c, ca, bc], [ab, bc, ca]]
    return V, G

def kat(P, a, b, c):  # kąt przy wierzchołku a w trójkącie abc
    u, v = P[b] - P[a], P[c] - P[a]
    return np.arccos(np.clip(u @ v / np.linalg.norm(u) / np.linalg.norm(v), -1, 1))

def deficyty(P, F):
    d = np.full(len(P), 2 * np.pi)
    for a, b, c in F:
        d[a] -= kat(P, a, b, c); d[b] -= kat(P, b, c, a); d[c] -= kat(P, c, a, b)
    return d

def holonomia(P, F, v):
    """Przenosi wektor styczny przez kolejne ściany wokół v (przez wspólne krawędzie: obrót wokół
    krawędzi, który przeprowadza normalną ściany f na normalną ściany g) i zwraca kąt obrotu po pełnym
    obiegu. Nie używa sumy kątów przy v. Obieg zgodny z orientacją ścian: (v, p, q) -> (v, q, r)."""
    rot = {}
    for f in F:
        if v in f:
            i = f.index(v); a, p, q = f[i:] + f[:i]
            rot[p] = (p, q)                      # ściana (v, p, q) wchodzi krawędzią (v,p), wychodzi (v,q)
    def normalna(p, q):
        n = np.cross(P[p] - P[v], P[q] - P[v]); return n / np.linalg.norm(n)
    start = next(iter(rot)); p, q = rot[start]
    e0 = P[p] - P[v]; x0 = e0 / np.linalg.norm(e0); x = x0.copy(); n0 = normalna(p, q)
    for _ in range(len(rot)):
        p, q = rot[p]; nf = normalna(p, q)
        r = rot[q][1]; ng = normalna(q, r)
        e = P[q] - P[v]; e /= np.linalg.norm(e)
        al, be = x @ e, x @ np.cross(nf, e)       # współrzędne względem krawędzi w ścianie f
        x = al * e + be * np.cross(ng, e)         # te same współrzędne w ścianie g
        p = q
        if p == start: break
    return np.arctan2(x @ np.cross(n0, x0), x @ x0)

def zawin(a): return (a + np.pi) % (2 * np.pi) - np.pi

# --- siatka zamknięta (sfera, χ = 2) ---
V, F = dwudziestoscian()
for _ in range(PODZIAL): V, F = podziel(V, F)
V0 = np.array(V)
F = [list(f) for f in F]
# zgodna orientacja ścian ustalona na NIEZABURZONEJ sferze (normalna na zewnątrz), potem zaburzenie kształtu
for f in F:
    a, b, c = f
    if np.dot(np.cross(V0[b] - V0[a], V0[c] - V0[a]), V0[a] + V0[b] + V0[c]) < 0: f[1], f[2] = f[2], f[1]
P = V0 * (1 + SZUM * rng.uniform(-1, 1, (len(V0), 1)))
nV, nF = len(P), len(F); nE = 3 * nF // 2
print(f"siatka: V={nV} E={nE} F={nF}  χ={nV - nE + nF}")

d = deficyty(P, F)
h = np.array([holonomia(P, F, v) for v in range(nV)])
r1p, r1m = np.max(np.abs(zawin(h - d))), np.max(np.abs(zawin(h + d)))
r1 = min(r1p, r1m)   # jeden znak dla wszystkich wierzchołków (konwencja kierunku obiegu), nie wybór per wierzchołek
print(f"Z1 holonomia ∓ deficyt: max |h−d| = {r1p:.2e}, max |h+d| = {r1m:.2e}  -> {'PRZESZŁO' if r1 < TOL else 'UPADŁO'} (znak {'+' if r1p<r1m else '−'}, wspólny)")
r2 = abs(d.sum() - 4 * np.pi)
print(f"Z2 Σ deficyt = {d.sum():.12f}  vs 4π = {4*np.pi:.12f}  różnica {r2:.1e} -> {'PRZESZŁO' if r2 < TOL else 'UPADŁO'}")
print(f"   (deficyty: min {d.min():+.4f}, max {d.max():+.4f} — lokalnie dowolne, suma = liczba)")

# --- cechowanie U(1) na tej samej siatce ---
kraw = {}
for a, b, c in F:
    for x, y in ((a, b), (b, c), (c, a)):
        k = (min(x, y), max(x, y))
        if k not in kraw: kraw[k] = rng.uniform(-np.pi, np.pi)
def faza(A, x, y): return A[(x, y)] if x < y else -A[(y, x)]
def obiegi(A): return np.array([zawin(faza(A, a, b) + faza(A, b, c) + faza(A, c, a)) for a, b, c in F])
def S_W(A): return np.sum(1 - np.cos(obiegi(A)))
def S_L(A): return np.sum(1 - np.cos(np.array(list(A.values()))))
chi = rng.uniform(-np.pi, np.pi, nV)
A2 = {k: v + chi[k[1]] - chi[k[0]] for k, v in kraw.items()}
r3 = abs(S_W(A2) - S_W(kraw)); r3k = abs(S_L(A2) - S_L(kraw))
print(f"Z3 S_W przed/po fazie w punktach: {S_W(kraw):.9f} / {S_W(A2):.9f}  różnica {r3:.1e} -> {'PRZESZŁO' if r3 < TOL else 'UPADŁO'}")
print(f"   kontrola S_L (fazy krawędzi): {S_L(kraw):.4f} / {S_L(A2):.4f}  różnica {r3k:.3f} -> {'kontrola działa' if r3k > 1e-3 else 'KONTROLA MARTWA'}")
th = obiegi(kraw); n = th.sum() / (2 * np.pi)
r4 = abs(n - round(n))
print(f"Z4 Σ obiegów/2π = {n:.12f}  (n = {round(n)})  odchylenie {r4:.1e} -> {'PRZESZŁO' if r4 < TOL else 'UPADŁO'}")

# --- kontrola płaska: wierzchołek wewnętrzny płaskiego wachlarza ---
k = 7; ang = (np.arange(k) + rng.uniform(-0.3, 0.3, k)) * 2 * np.pi / k   # przerwy < π: wachlarz naprawdę płaski (poprzednio losowe kąty dawały przerwę > π i nachodzące trójkąty)
Pp = np.vstack([[0, 0, 0], np.c_[np.cos(ang) * rng.uniform(0.5, 1.5, k), np.sin(ang) * rng.uniform(0.5, 1.5, k), np.zeros(k)]])
Fp = [[0, 1 + i, 1 + (i + 1) % k] for i in range(k)]
dp = deficyty(Pp, Fp)[0]; hp = holonomia(Pp, Fp, 0)
print(f"K  płaski wierzchołek: deficyt {dp:+.1e}, holonomia {hp:+.1e} -> {'PRZESZŁO' if abs(dp) < TOL and abs(hp) < TOL else 'UPADŁO'}")
