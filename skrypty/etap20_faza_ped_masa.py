# etap20 — czy energia, pęd i masa pochodzą z tej samej fazy (sprawdzenie zdania z R1f, poprawka 163)
#
# Zapis: faza nośnika φ = S/ħ; E = obroty fazy na tyknięcie czytającego, p = obroty fazy na odległość,
# m = obroty fazy na WŁASNE tyknięcie. Jednostki c = ħ = 1.
#
# Zdania do upadku (zapisane przed rachunkiem):
#  M1: m² = det(E·1 + p·σ) (tożsamość R1c zastosowana do gradientu fazy) — do 1e-12.
#  M2: każdy gradient czasopodobny = suma dwóch zerowych k1 + k2 (dwie części t = 0, zygzak R1d),
#      i m² = 2·(k1·k2) (iloczyn Minkowskiego = relacja dwóch części); kontrola: k1 ∥ k2 → m = 0.
#  M3: faza zebrana wzdłuż linii świata na jedno własne tyknięcie = m, NIEZALEŻNIE od prędkości
#      względem czytającego (do 1e-12); kontrola: faza na tyknięcie czytającego (E) i na odległość (p)
#      zależą od prędkości.
#  M4: przesunięcie zera fazy E → E + c (dopuszczalne, gdy faza w punkcie ≡ Ø i nic poza tym) psuje M3:
#      faza na własne tyknięcie zaczyna zależeć od prędkości → „masa z fazy” wymaga niezmienniczości
#      Lorentza (R1c), która ustala zero. Zdanie upada, jeśli przesunięcie NIE psuje M3.
import numpy as np

SEED = 7
N = 2000
rng = np.random.default_rng(SEED)
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
def mink(a, b): return a[0] * b[0] - a[1:] @ b[1:]

# losowe gradienty czasopodobne: masa m, prędkość względem czytającego v (|v| < 1)
m = rng.uniform(0.1, 5, N)
kier = rng.normal(size=(N, 3)); kier /= np.linalg.norm(kier, axis=1)[:, None]
v = rng.uniform(0, 0.99, N)[:, None] * kier
g = 1 / np.sqrt(1 - (v ** 2).sum(1))
E = g * m; p = (g * m)[:, None] * v

# M1
det = np.array([np.linalg.det(E[i] * np.eye(2) + sum(p[i, j] * sig[j] for j in range(3))).real for i in range(N)])
r1 = np.max(np.abs(det - m ** 2) / m ** 2)
print(f"M1 m² = det(E + p·σ): max względna różnica {r1:.1e} -> {'PRZESZŁO' if r1 < 1e-12 else 'UPADŁO'}")

# M2: rozkład na dwie części zerowe: w układzie spoczynkowym k1,2 = (m/2)(1, ±n), potem pchnięcie o v
def pchniecie(x, v):
    b2 = v @ v
    if b2 == 0: return x
    gg = 1 / np.sqrt(1 - b2); bx = v @ x[1:]
    t = gg * (x[0] + bx); s = x[1:] + ((gg - 1) * bx / b2 + gg * x[0]) * v
    return np.r_[t, s]
r2, r2n, r2c = 0, 0, 0
for i in range(N):
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    k1 = pchniecie(np.r_[m[i] / 2, m[i] / 2 * n], v[i]); k2 = pchniecie(np.r_[m[i] / 2, -m[i] / 2 * n], v[i])
    r2 = max(r2, np.max(np.abs(k1 + k2 - np.r_[E[i], p[i]])) / E[i])
    r2n = max(r2n, abs(mink(k1, k1)) / E[i] ** 2, abs(mink(k2, k2)) / E[i] ** 2)
    r2 = max(r2, abs(2 * mink(k1, k2) - m[i] ** 2) / m[i] ** 2)
    kk = np.r_[1.0, n] * rng.uniform(0.1, 3); ll = np.r_[1.0, n] * rng.uniform(0.1, 3)   # równoległe zerowe
    r2c = max(r2c, abs(mink(kk + ll, kk + ll)))
print(f"M2 p = k1 + k2 (zerowe), m² = 2 k1·k2: max różnica {r2:.1e}, |k²| {r2n:.1e} -> {'PRZESZŁO' if max(r2, r2n) < 1e-12 else 'UPADŁO'}")
print(f"   kontrola: dwie równoległe części zerowe -> m² = {r2c:.1e} (masa 0) -> {'kontrola działa' if r2c < 1e-12 else 'KONTROLA MARTWA'}")

# M3: faza zebrana między dwoma zdarzeniami linii świata (czas czytającego T): Δφ = E·T − p·x, x = v·T
T = 10.0
dphi = E * T - (p * v).sum(1) * T
tau = T / g
na_wlasne = dphi / tau; na_czyt = dphi / T; na_odl = (p ** 2).sum(1) ** 0.5
r3 = np.max(np.abs(na_wlasne - m) / m)
vv = np.linalg.norm(v, axis=1)
k_czyt = np.corrcoef(na_czyt / m, vv)[0, 1]      # wzdłuż linii świata nośnika, na tyknięcie czytającego = m·√(1−v²)
k_E = np.corrcoef(E / m, vv)[0, 1]               # w miejscu czytającego (∂φ/∂t przy stałym x) = E = γm
k_odl = np.corrcoef(na_odl / m, vv)[0, 1]        # na odległość = |p| = γmv
r3b = np.max(np.abs(na_czyt - m / g) / m)
print(f"M3 faza na własne tyknięcie = m: max względna różnica {r3:.1e} -> {'PRZESZŁO' if r3 < 1e-12 else 'UPADŁO'}")
print(f"   kontrola (wszystkie inne tempa zależą od |v|; warunek |korelacja| > 0,3):")
print(f"     wzdłuż linii świata na tyknięcie czytającego = m·√(1−v²) (różnica {r3b:.1e}); korelacja z |v| {k_czyt:+.3f}")
print(f"     w miejscu czytającego E = γm: korelacja {k_E:+.3f};  na odległość |p| = γmv: korelacja {k_odl:+.3f}")
print(f"     -> {'kontrola działa' if min(abs(k_czyt), abs(k_E), abs(k_odl)) > 0.3 else 'KONTROLA MARTWA'}")

# M4: przesunięcie zera fazy o stałą c
c = 0.7
dphi_c = (E + c) * T - (p * v).sum(1) * T
na_wlasne_c = dphi_c / tau
k4 = np.corrcoef(na_wlasne_c - m, np.linalg.norm(v, axis=1))[0, 1]
roz = np.max(np.abs(na_wlasne_c - m))
print(f"M4 po przesunięciu zera (c = {c}): faza na własne tyknięcie − m zależy od |v|: korelacja {k4:+.3f}, max odchylenie {roz:.2f}"
      f" -> {'PRZESZŁO (zero ustala Lorentz)' if roz > 1e-3 and k4 > 0.3 else 'UPADŁO'}")
