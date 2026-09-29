# etap28 — węzeł jako para (M, O); moduły w rozsiewie (poprawki 172–173, A11d).
#
# Moduł M względem otoczenia O: każdy element O stoi w tej samej relacji (≺, ≻ albo ∥) do wszystkich elementów M.
# Δ = K_R − K_Rᵀ; blok Δ[O, M] mówi, co O czyta z M.
#
# Część 1 — TESTY POPRAWNOŚCI DEFINICJI (tautologie, nie wyniki; użytkownik 29.09):
#   Z1  ½C (sam porządek): wiersz elementu O jest stały na M → rząd bloku 1 (O czyta tylko Σ_M φ, z dwóch stron);
#   Z2  L (wagi na linkach): link z zewnątrz tylko do wszystkich maksymalnych albo wszystkich minimalnych elementów M,
#       elementy wnętrza bez linku na zewnątrz → rząd ≤ 2 (link zależy od elementów spoza pary);
#   Z3  (NIE tautologia, poprawka 175) z masą (rezolwenta, waga na krok): z każdej strony jedna suma ważona drogami
#       od elementu do brzegu M → rząd ≤ 2, ale kolumny wnętrza niezerowe i równe tylko dla tej samej głębokości;
#   Z4  Gallai: łańcuch k wstawiony w element porządku pierwszego mnoży liczbę orientacji przechodnich przez k!,
#       antyłańcuch — przez 1 (wnętrza nie da się ustawić z zewnątrz).
# Część 2 — ROZSIEW = OTOCZENIE O = WSZYSTKO; moduły tylko przypadkowe. Zdania zapisane przed przebiegiem:
#   Z5  (użytkownik) 2D: częstość bliźniaków mniej więcej stała względem n = 100–400;
#   Z6  (użytkownik) moduły z łańcuchem 3 rzędy wielkości rzadsze, ale niezerowe przy dość wielu próbach;
#   Z7  (asystent, kartka) 2D = losowa permutacja; moduł-łańcuch k = k kolejnych pozycji o kolejnych rosnących
#       wartościach → łańcuch 3 ≈ 1/n na próbę (spada z n), ogólnie n^(2−k); 4D przy tych n — brzeg diamentu.
# CPU, kilka minut. Elementy bez żadnej relacji (4D) pominięte: otoczenie bez możliwości, nie struktura.
import itertools
import time
import numpy as np


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


def los2d(n, g):
    p, q = g.permutation(n), g.permutation(n)
    return (p[:, None] < p[None, :]) & (q[:, None] < q[None, :])


def diament4(n, g):
    X = []
    while len(X) < n:
        t, x, y, z = g.uniform(-1, 1, 4)
        if np.sqrt(x * x + y * y + z * z) < 1 - abs(t):
            X.append((t, x, y, z))
    X = np.array(X)
    dt = X[None, :, 0] - X[:, None, 0]
    dr = np.linalg.norm(X[None, :, 1:] - X[:, None, 1:], axis=2)
    return (dt > 0) & (dt >= dr)


# ---------- część 1: testy poprawności definicji ----------
rng = np.random.default_rng(5)
C0 = los2d(40, rng)
x = int(np.argmax(C0.sum(0) * C0.sum(1)))                      # element z przeszłością i przyszłością
D = np.zeros((6, 6), bool)                                      # wnętrze: 0<1<2<3, 4 między 0 a 3, 5 między 1 a 3
for a, b in ((0, 1), (1, 2), (2, 3), (0, 4), (4, 3), (1, 5), (5, 3)):
    D[a, b] = True
P, M = podstaw(C0, x, domkniecie(D))
zew = [i for i in range(len(P)) if i not in M]
C, L, I = P.astype(float), linki(P), np.eye(len(P))
wagi = {'½C (sam porządek)': 0.5 * C,
        'L (wagi na linkach)': L,
        'L(1−0,3L)⁻¹ (z masą)': L @ np.linalg.inv(I - 0.3 * L),
        '½C(1−0,2C)⁻¹ (z masą)': 0.5 * C @ np.linalg.inv(I - 0.2 * C)}
for nazwa, K in wagi.items():
    B = (K - K.T)[np.ix_(zew, M)]
    klasy = {}
    for j, m in enumerate(M):
        klasy.setdefault(tuple(np.round(B[:, j], 9)), []).append(m - M[0])
    print(f'{nazwa:24s} rząd bloku {np.linalg.matrix_rank(B, tol=1e-9)} | '
          f'elementy M o tej samej kolumnie: {sorted(klasy.values())} | '
          f'|kolumna| (0 min, 3 maks, 1 2 4 5 wnętrze): {np.round(np.abs(B).sum(0), 2)}')
wn = [M[i] for i in (1, 2, 4, 5)]                               # ani minimalne, ani maksymalne w M
print('   sprzężenie wnętrza przy L:', np.abs((L - L.T)[np.ix_(zew, wn)]).sum())


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
sym = lambda Q: Q | Q.T
print('Z4 orientacje: „N”', orientacje(sym(N4)),
      '| łańcuch 3 w miejscu elementu', orientacje(sym(podstaw(N4, 2, domkniecie(np.triu(np.ones((3, 3), bool), 1)))[0])),
      '| antyłańcuch 2', orientacje(sym(podstaw(N4, 2, np.zeros((2, 2), bool))[0])))


# ---------- część 2: rozsiew, moduły przypadkowe ----------
def modul2(kod, n):
    """wszystkie 2-elementowe moduły: pary, których żaden inny element nie rozróżnia"""
    wyn, por = [], (kod != 0)
    for a in range(n - 1):
        mism = (kod[:, a][:, None] != kod[:, a + 1:]).sum(0)
        mism -= 2 * por[a, a + 1:]                              # z = a i z = b dają niezgodność, gdy a, b w relacji
        wyn += [(a, a + 1 + j) for j in np.nonzero(mism == 0)[0]]
    return wyn


def modul3(kod, n, a, b):
    """trzecie elementy w dopełniające moduł {a, b} do modułu {a, b, w} (każdy moduł 3-el. zawiera moduł 2-el.)"""
    out = []
    for w in range(n):
        if w in (a, b):
            continue
        z = np.ones(n, bool)
        z[[a, b, w]] = False
        if (kod[z, a] == kod[z, w]).all():
            out.append(w)
    return out


def policz(C):
    kod = C.astype(np.int8) * 2 + C.T.astype(np.int8)
    n, lk, bl, trojki = len(C), 0, 0, set()
    for a, b in modul2(kod, n):
        if C[a, b] or C[b, a]:
            lk += 1
        else:
            bl += 1
        trojki |= {frozenset((a, b, w)) for w in modul3(kod, n, a, b)}
    l3 = 0
    for T in trojki:
        Cs = C[np.ix_(sorted(T), sorted(T))].astype(int)
        l3 += int((Cs @ Cs > 0).any())
    return lk, bl, len(trojki), l3


rng2 = np.random.default_rng(29)
print('Z5–Z7, 2D, dokładnie z porządku:')
for n, prob in ((100, 1500), (200, 400), (400, 100)):
    t0, s, zgodny = time.time(), np.zeros(4), 0
    for _ in range(prob):
        p, q = rng2.permutation(n), rng2.permutation(n)
        C = (p[:, None] < p[None, :]) & (q[:, None] < q[None, :])
        wynik = policz(C)
        s += wynik
        d = np.diff(q[np.argsort(p)])                            # skrót: wartości w kolejności pozycji
        zgodny += int(((d[:-1] == 1) & (d[1:] == 1)).sum()) == wynik[3]
    s /= prob
    print(f'  n={n:3d} prób {prob:4d}: link uszczelniony {s[0]:.3f}, bliźniak bez relacji {s[1]:.3f} na próbę | '
          f'moduły 3-el. {s[2]:.4f}, łańcuch 3 {s[3]:.4f} (1/n = {1 / n:.4f}) | skrót zgodny w {zgodny}/{prob} | '
          f'{time.time() - t0:.0f} s', flush=True)
print('Z6–Z7, 2D, łańcuch 3 skrótem przez permutację:')
for n in (100, 200, 400):
    prob, ile = 200000, 0
    for _ in range(prob // 1000):
        d = np.diff(np.argsort(rng2.random((1000, n)), axis=1), axis=1)
        ile += int(((d[:, :-1] == 1) & (d[:, 1:] == 1)).sum())
    print(f'  n={n:3d}: łańcuch 3 na próbę {ile / prob:.5f} (1/n = {1 / n:.5f}; {ile} w {prob} próbach)', flush=True)

rng4 = np.random.default_rng(31)
print('Z5–Z7, 4D (elementy bez relacji pominięte):')
for n, prob in ((100, 60), (200, 30), (400, 12)):
    s, niz, st_mod, st_all = np.zeros(4), 0, [], []
    for _ in range(prob):
        C = diament4(n, rng4)
        st = C.sum(0) + C.sum(1)
        zyw = np.nonzero(st > 0)[0]
        niz += n - len(zyw)
        C, st = C[np.ix_(zyw, zyw)], st[zyw]
        st_all += list(st)
        kod = C.astype(np.int8) * 2 + C.T.astype(np.int8)
        st_mod += [st[i] for pr in modul2(kod, len(C)) for i in pr]
        s += policz(C)
    s /= prob
    print(f'  n={n:3d} prób {prob:3d}: izolowanych {niz / prob:.1f} | link uszczelniony {s[0]:.2f}, bliźniak bez relacji '
          f'{s[1]:.2f} na próbę | relacji na element w module {np.mean(st_mod) if st_mod else 0:.1f} '
          f'(mediana {np.median(st_all):.0f}) | moduły 3-el. {s[2]:.3f}, łańcuch 3 {s[3]:.3f}', flush=True)
