# etap27 — rura czasopodobna na porządku: jądro komutatora zbudowanego z samego porządku (poprawka 171, A11d).
#
# Δ = K_R − K_Rᵀ, K_R = C/2 (równe wagi na relacjach; stała nie zmienia jądra). Σ f_x φ(x) = 0  ⇔  Δ f = 0.
# [T] na kartce: f ∈ ker Δ  ⇔  dla każdego z: Σ_{y≻z} f_y = Σ_{y≺z} f_y.
# [T] separatory: jeśli dla każdego x maksymalnego w nośniku f istnieje z ≻ x, które z nośnika ma pod sobą tylko
#     x (z bliźniakami) i przeszłość x, a nad sobą nic — f jest sumą różnic bliźniaków.
# Zdania zapisane przed przebiegiem:
#   Z1  łańcuch nieparzysty ma jądro (skew-rank parzysty): łańcuch 3 → φ_b = φ_a + φ_c;
#   Z2  po dopisaniu separatorów (dla każdej klasy bliźniaków element nad dokładnie J⁻[x] ∪ [x]) jądro na P
#       = różnice bliźniaków P, w każdej próbie;
#   Z3  bez separatorów (sam skończony P) jądro bywa większe niż bliźniaki (kontrprzykłady z brzegu).
# CPU, sekundy. Losowe porządki wymiaru 2 = przecięcie dwóch porządków liniowych (bez współrzędnych).
import numpy as np

rng = np.random.default_rng(7)


def wymiar_jadra(C, kolumny, tol=1e-9):
    D = (C - C.T)[:, kolumny]
    s = np.linalg.svd(D, compute_uv=False)
    return len(kolumny) - int((s > tol * max(1.0, s.max())).sum())


def losowy(n):
    p, q = rng.permutation(n), rng.permutation(n)
    return np.array([[1.0 if (p[i] < p[j] and q[i] < q[j]) else 0.0 for j in range(n)] for i in range(n)])


def klasy_blizniakow(C):
    kl = {}
    for x in range(len(C)):
        kl.setdefault((tuple(C[:, x]), tuple(C[x])), []).append(x)
    return list(kl.values())


def z_separatorami(C):
    n, kl = len(C), klasy_blizniakow(C)
    P = np.zeros((n + len(kl), n + len(kl)))
    P[:n, :n] = C
    for k, klasa in enumerate(kl):
        for y in set(np.nonzero(C[:, klasa[0]])[0]) | set(klasa):
            P[y, n + k] = 1.0
    return P, kl


# Z1
L3 = np.triu(np.ones((3, 3)), 1)
u, s, vt = np.linalg.svd(L3 - L3.T)
v = vt[-1] / vt[-1][0]
print('Z1 łańcuch 3: wymiar jądra', wymiar_jadra(L3, [0, 1, 2]), '| wektor', np.round(v, 3),
      '| po separatorach', wymiar_jadra(z_separatorami(L3)[0], [0, 1, 2]))
# Z2, Z3
prob = z2 = z3 = 0
for n in range(3, 26):
    for _ in range(120):
        C = losowy(n)
        P, kl = z_separatorami(C)
        bl = sum(len(k) - 1 for k in kl)
        prob += 1
        z2 += wymiar_jadra(P, list(range(n))) == bl
        z3 += wymiar_jadra(C, list(range(n))) > bl
print(f'Z2 z separatorami: jądro = różnice bliźniaków w {z2}/{prob}')
print(f'Z3 bez separatorów: jądro większe niż bliźniaki w {z3}/{prob}')
