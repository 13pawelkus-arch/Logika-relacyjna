# etap25 — kontrole do tematu (c): sztywność (A11d; poprawka 169)
#
# To są sprawdzenia tożsamości i przykładów ze źródeł, nie rachunek z wynikiem, który mógłby wyjść inaczej.
# Zdania (każde może upaść tylko przez błąd algebry albo odczytu źródła):
# Z1 [T]: nośnik, S = −m·τ (R1f-3). Różnica faz drogi zgiętej p→q→c i prostej p→c = m·E,
#     E = τ(p,c) − τ(p,q) − τ(q,c) (nadwyżka z R1f-5) — dokładnie, w 3+1; E bez zmiany przy pchnięciu.
# Z2 [T]: odchylenie środka o x (w układzie cięciwy, T = ½τ(p,c)): E → x²/T; zgodnie z R1f-5 (E = a²δ³/4
#     dla ruchu o stałym przyspieszeniu, trzy punkty co δ czasu własnego).
# Z3 [T]: najprostsza kontynuacja (min E) nie zależy od m — m jest wspólnym czynnikiem różnicy faz.
# Z4 [T]: nierelatywistycznie m·E → (m/2)∫v²dt (dwa odcinki o prędkościach ±x/T na czasie 2T).
# Z5 [T]: foton przy częstości ustalonej przez czytającego: różnica długości drogi 2(√((L/2)² + x²) − L/2) → x²/(L/2)
#     (strefa Fresnela); dla fali de Broglie'a nośnika masywnego L/p = τ/m (p = γmv, L = vt, τ = t/γ).
# Z6 [T] (przykład ze źródła: Watanabe, arXiv:1208.6338, „Example”): K = (ab + c)² + a²b⁴ — hesjan w zerze
#     diag(0, 0, 2) (zdegenerowany); wzdłuż osi a i b K = 0 (dosłowne ≡); wzdłuż (t, t, −t²) K = t⁶ > 0
#     (rozróżnialne, dopiero w szóstym rzędzie) — kierunek zerowy formy drugiego rzędu ≠ ≡.
# Z7 [T] (A11b): koszt relacji C(x<y) = −ln Pr[x przed y] w losowym rozszerzeniu liniowym. Antyłańcuch {x, y, z}:
#     Pr = ½; po dołożeniu y ≺ z: ⅓ (koszt rośnie); po dołożeniu x ≺ z: ⅔ (maleje) — „kolejne tańsze” nie jest ogólne.
import itertools
import numpy as np

rng = np.random.default_rng(1)


def tau(a, b):
    d = b - a
    s = d[0] ** 2 - np.sum(d[1:] ** 2)
    return np.sqrt(s) if (s > 0 and d[0] > 0) else np.nan


def boost(v, X):
    g = 1 / np.sqrt(1 - v @ v)
    n = v / np.sqrt(v @ v)
    L = np.eye(4)
    L[0, 0] = g
    L[0, 1:] = L[1:, 0] = g * v
    L[1:, 1:] += (g - 1) * np.outer(n, n)
    return X @ L.T


# Z1
maxd = maxb = 0.0
n = 0
while n < 2000:
    p = np.zeros(4)
    q = np.r_[rng.uniform(1, 2), rng.uniform(-.5, .5, 3)]
    c = q + np.r_[rng.uniform(1, 2), rng.uniform(-.5, .5, 3)]
    t1, t2, t3 = tau(p, q), tau(q, c), tau(p, c)
    if np.isnan([t1, t2, t3]).any():
        continue
    m = rng.uniform(.1, 5)
    E = t3 - t1 - t2
    dphi = (-m * (t1 + t2)) - (-m * t3)
    maxd = max(maxd, abs(dphi - m * E))
    P, Q, C = boost(rng.uniform(-.5, .5, 3), np.array([p, q, c]))
    maxb = max(maxb, abs((tau(P, C) - tau(P, Q) - tau(Q, C)) - E))
    n += 1
print(f'Z1: 2000 trójek w 3+1: max |Δφ − m·E| = {maxd:.1e}; max |E(po pchnięciu) − E| = {maxb:.1e}')

# Z2
T = 1.0
for x in (1e-1, 1e-2, 1e-3):
    E = 2 * T - 2 * np.sqrt(T * T - x * x)
    print(f'Z2: x = {x:g}: E/(x²/T) = {E / (x * x / T):.8f}')
for a in (0.3, 0.1, 0.03):
    d = 0.5
    pts = [np.array([np.sinh(a * s) / a, (np.cosh(a * s) - 1) / a, 0, 0]) for s in (-d, 0, d)]
    E = tau(pts[0], pts[2]) - tau(pts[0], pts[1]) - tau(pts[1], pts[2])
    Th = tau(pts[0], pts[2]) / 2
    x = abs(pts[1][1] - pts[0][1])
    print(f'Z2: a = {a}: E/(a²δ³/4) = {E / (a * a * d ** 3 / 4):.6f}; E/(x²/T) = {E / (x * x / Th):.6f}')

# Z3: środek q przesuwany w poprzek; argmin różnicy faz dla różnych m
xs = np.linspace(-0.3, 0.3, 601)
Es = np.array([2 * T - 2 * np.sqrt(T * T - x * x) for x in xs])
am = {m: xs[np.argmin(m * Es)] for m in (0.1, 1.0, 10.0)}
print(f'Z3: najprostsza kontynuacja (x przy min m·E) dla m = 0,1 / 1 / 10: {am[0.1]:+.3f} / {am[1.0]:+.3f} / {am[10.0]:+.3f}')

# Z4
m = 2.0
for x in (1e-1, 1e-2):
    mE = m * (2 * T - 2 * np.sqrt(T * T - x * x))
    nr = 0.5 * m * (x / T) ** 2 * (2 * T)
    print(f'Z4: x = {x:g}: m·E / ((m/2)∫v²dt) = {mE / nr:.6f}')

# Z5
L = 1.0
for x in (1e-1, 1e-2):
    dl = 2 * (np.sqrt((L / 2) ** 2 + x * x) - L / 2)
    print(f'Z5: Fresnel, x = {x:g}: ΔL/(x²/(L/2)) = {dl / (x * x / (L / 2)):.6f}')
vs = rng.uniform(0.01, 0.99, 1000)
tt, mm = 1.0, 1.7
g = 1 / np.sqrt(1 - vs ** 2)
err = np.abs((vs * tt) / (g * mm * vs) - (tt / g) / mm).max()
print(f'Z5: de Broglie: max |L/p − τ/m| = {err:.1e} (1000 prędkości)')


# Z6
def K(a, b, c):
    return (a * b + c) ** 2 + a ** 2 * b ** 4


h = 1e-4
H = np.zeros((3, 3))
e = np.eye(3) * h
for i in range(3):
    for j in range(3):
        H[i, j] = (K(*(e[i] + e[j])) - K(*(e[i] - e[j])) - K(*(-e[i] + e[j])) + K(*(-e[i] - e[j]))) / (4 * h * h)
print('Z6: hesjan K w zerze (numerycznie):', np.round(H, 6).tolist())
for t in (0.1, 0.01):
    print(f'Z6: t = {t:g}: K(t,0,0) = {K(t, 0, 0):.1e}, K(0,t,0) = {K(0, t, 0):.1e}, '
          f'K(t,t,−t²)/t⁶ = {K(t, t, -t * t) / t ** 6:.6f}, K(t,t,0)/t⁴ = {K(t, t, 0) / t ** 4:.6f}')


# Z7
def pr_x_przed_y(rel):
    ok = [s for s in itertools.permutations('xyz') if all(s.index(u) < s.index(w) for u, w in rel)]
    return sum(s.index('x') < s.index('y') for s in ok) / len(ok)


for rel, opis in (([], 'antyłańcuch'), ([('y', 'z')], 'po dołożeniu y ≺ z'), ([('x', 'z')], 'po dołożeniu x ≺ z')):
    pr = pr_x_przed_y(rel)
    print(f'Z7: {opis}: Pr[x ≺ y] = {pr:.4f}, koszt −ln Pr = {-np.log(pr):.4f}')
