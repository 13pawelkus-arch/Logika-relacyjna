# etap28 — zapis czytającego na porządku: węzeł jako moduł (poprawka 172, A11d).
#
# Moduł M: podzbiór, do którego każdy element spoza odnosi się tak samo (≺ wszystkich, ≻ wszystkich albo ∥ wszystkich).
# Δ = K_R − K_Rᵀ; blok Δ[otoczenie, M] mówi, co z modułu widać z zewnątrz.
# Zdania zapisane przed przebiegiem:
#   Z1  ½C (1+1 bez masy): wiersz elementu spoza jest stały na M → rząd bloku 1 (widać tylko Σ_M φ);
#   Z2  L (3+1 bez masy): link z zewnątrz tylko do wszystkich maksymalnych albo wszystkich minimalnych elementów M
#       → rząd ≤ 2, elementy wnętrza (ani min., ani maks.) bez żadnego sprzężenia na zewnątrz;
#   Z3  z masą (rezolwenta, waga na krok): droga rozkłada się na wewnętrzną i zewnętrzną → nadal rząd ≤ 2,
#       wnętrze wchodzi przez własne drogi; elementy o tych samych drogach mają te same kolumny;
#   Z4  Gallai: wstawienie łańcucha k w element porządku pierwszego mnoży liczbę orientacji przechodnich przez k!,
#       antyłańcucha — przez 1;
#   Z5  rozsiew (2D: losowa permutacja; 4D: diament): moduły tylko 2-elementowe, w liczbie niezależnej od n albo
#       z brzegu pudła; moduł z łańcuchem ≥ 3 przy n ≥ 200 nie występuje.
# CPU, minuty (rozsiew n = 400 w 4D najdłużej). Moduły większe niż n/2 pomijane (reszta całości = brzeg pudła).
import itertools
import numpy as np

rng = np.random.default_rng(5)


def domkniecie(C):
    C = C.copy().astype(bool)
    for k in range(len(C)):
        C |= np.outer(C[:, k], C[k, :])
    return C


def linki(C):
    C = C.astype(int)
    return ((C == 1) & ((C @ C) == 0)).astype(float)


def podstaw(C, x, D):
    """wstawia porządek D w miejsce elementu x porządku C; zwraca nowy porządek i indeksy modułu"""
    n, k = len(C), len(D)
    reszta = [i for i in range(n) if i != x]
    P = np.zeros((n - 1 + k, n - 1 + k), bool)
    P[:n - 1, :n - 1] = C[np.ix_(reszta, reszta)]
    P[:n - 1, n - 1:] = C[reszta, x][:, None]
    P[n - 1:, :n - 1] = C[x, reszta][None, :]
    P[n - 1:, n - 1:] = D
    return P, list(range(n - 1, n - 1 + k))


def los2d(n):
    p, q = rng.permutation(n), rng.permutation(n)
    return (p[:, None] < p[None, :]) & (q[:, None] < q[None, :])


def diament4(n):
    X = []
    while len(X) < n:
        t, x, y, z = rng.uniform(-1, 1, 4)
        if np.sqrt(x * x + y * y + z * z) < 1 - abs(t):
            X.append((t, x, y, z))
    X = np.array(X)
    dt = X[None, :, 0] - X[:, None, 0]
    dr = np.linalg.norm(X[None, :, 1:] - X[:, None, 1:], axis=2)
    return (dt > 0) & (dt >= dr)


# Z1–Z3
C0 = los2d(40)
x = int(np.argmax(C0.sum(0) * C0.sum(1)))                      # element z przeszłością i przyszłością
D = np.zeros((6, 6), bool)                                      # wnętrze: 0<1<2<3, 4 między 0 a 3, 5 między 1 a 3
for a, b in ((0, 1), (1, 2), (2, 3), (0, 4), (4, 3), (1, 5), (5, 3)):
    D[a, b] = True
P, M = podstaw(C0, x, domkniecie(D))
zew = [i for i in range(len(P)) if i not in M]
C, L, I = P.astype(float), linki(P), np.eye(len(P))
wagi = {'½C (1+1 bez masy)': 0.5 * C,
        'L (3+1 bez masy)': L,
        'L(1−0,3L)⁻¹ (z masą)': L @ np.linalg.inv(I - 0.3 * L),
        '½C(1−0,2C)⁻¹ (z masą)': 0.5 * C @ np.linalg.inv(I - 0.2 * C)}
for nazwa, K in wagi.items():
    B = (K - K.T)[np.ix_(zew, M)]
    klasy = {}
    for j, m in enumerate(M):
        klasy.setdefault(tuple(np.round(B[:, j], 9)), []).append(m - M[0])
    print(f'{nazwa:24s} rząd bloku {np.linalg.matrix_rank(B, tol=1e-9)} | '
          f'elementy M o tej samej kolumnie: {sorted(klasy.values())}')
wn = [M[i] for i in (1, 2, 4, 5)]                               # ani minimalne, ani maksymalne w M
print('   sprzężenie wnętrza przy L:', np.abs((L - L.T)[np.ix_(zew, wn)]).sum())


# Z4
def orientacje(G):
    kr = [(i, j) for i in range(len(G)) for j in range(i + 1, len(G)) if G[i, j]]
    ile = 0
    for bity in itertools.product((0, 1), repeat=len(kr)):
        O = np.zeros_like(G, bool)
        for (i, j), b in zip(kr, bity):
            O[(i, j) if b else (j, i)] = True
        ile += bool((domkniecie(O) == O).all())
    return ile


N4 = np.zeros((4, 4), bool)
N4[0, 1] = N4[2, 1] = N4[2, 3] = True                            # porządek „N”: graf P4, bez modułów
print('Z4 orientacje: „N”', orientacje(N4 | N4.T),
      '| łańcuch 3 w miejscu elementu', orientacje((lambda P: P | P.T)(podstaw(N4, 2, domkniecie(np.triu(np.ones((3, 3), bool), 1)))[0])),
      '| antyłańcuch 2', orientacje((lambda P: P | P.T)(podstaw(N4, 2, np.zeros((2, 2), bool))[0])))


# Z5
def modul(kod, x, y, n):
    S = np.zeros(n, bool)
    S[[x, y]] = True
    while True:
        k = kod[:, S]
        rozr = (k.min(1) != k.max(1)) & ~S
        if not rozr.any():
            return S
        S |= rozr
        if S.sum() > n // 2:
            return None


for nazwa, gen in (('2D', los2d), ('4D', diament4)):
    for n in (100, 200, 400):
        prob, rozm, lan, bl, lk, st_bl, st_all = 3, [], 0, 0, 0, [], []
        for _ in range(prob):
            C = gen(n)
            kod = C.astype(np.int8) * 2 + C.T.astype(np.int8)
            st = C.sum(0) + C.sum(1)
            st_all += list(st)
            znal = set()
            for a, b in itertools.combinations(range(n), 2):
                S = modul(kod, a, b, n)
                if S is not None:
                    znal.add(frozenset(np.nonzero(S)[0]))
            for S in znal:
                idx = sorted(S)
                rozm.append(len(S))
                Cs = C[np.ix_(idx, idx)].astype(int)
                lan += bool((Cs @ Cs > 0).any())
                if len(S) == 2:
                    if Cs.any():
                        lk += 1
                    else:
                        bl += 1
                        st_bl += [st[i] for i in idx]
        print(f'Z5 {nazwa} n={n}: moduły ≤ n/2 na próbę {len(rozm) / prob:.1f}, rozmiary {sorted(set(rozm))}, '
              f'z łańcuchem ≥ 3: {lan} | bliźniaki {bl / prob:.1f}, linki uszczelnione {lk / prob:.1f} na próbę | '
              f'relacji na element bliźniaka {np.mean(st_bl) if st_bl else 0:.1f} (mediana w próbie {np.median(st_all):.0f})',
              flush=True)
