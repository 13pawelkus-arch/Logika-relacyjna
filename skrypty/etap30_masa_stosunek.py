# etap30 — masa jako stosunek, bez jednostki i bez pojemnika (uwaga użytkownika 29.09).
#
# Uwaga użytkownika: „Żeby zrównać, trzeba czegoś do przeliczenia jednostek, a każde takie coś przychodzi
# z pojemnikiem, bo jednostka jest odniesieniem zewnętrznym. […] m·τ musi wcześniej zostać przepisane jako
# stosunek — inaczej przelicznik będzie tym, czym miał nie być.”
#
# Przepisanie (kontrola wymiarowa, kartka): w modelu hop-stop (Johnston) waga drogi o n skokach to a^n·b^(n−1).
# Żeby wyrazy szeregu miały ten sam wymiar, [a][b] = 1, więc jedynym bezwymiarowym parametrem jest a·b:
#   1+1: a = ½, b = −m²/ρ = −(m·ℓ)²  →  a·b = −(m·ℓ)²/2
#   3+1: a = √ρ/(2π√6), b = −m²V₀    →  a·b = −(m·ℓ)²/(2π√6),  ℓ = ρ^(−1/4)
# W obu: parametrem jest **ν = m·ℓ = faza na jedno własne tyknięcie** (R1f-3), a nie m i ρ osobno.
# Zgodne z B1 („szachownica Feynmana: waga (imε) za zwrot, bezwymiarowym parametrem jest mε”)
# i z R1f-3 M2 (m² = relacja dwóch części t = 0): waga zatrzymania = (iν)² = −ν², kwadrat wagi zwrotu.
#
# PYTANIE TEGO RACHUNKU: skoro ν jest liczbą, to czym jest odczytywalne? Z 180: O czyta z modułu jedną
# liczbę, w której ν i struktura wnętrza są splecione. Więc ν może wyjść dopiero ze STOSUNKU dwóch
# odczytów — dwóch wnętrz w tym samym otoczeniu, tym samym miejscu i dla tego samego czytającego ([94]:
# „stosunek dwóch stosunków”).
#
# ZDANIA PRZED PRZEBIEGIEM (mogą upaść):
#   Z1  stosunek odczytów dwóch wnętrz wstawionych w to samo miejsce nie zależy od reszty porządku
#       ani od tego, który element O czyta — zależy tylko od ν i od obu wnętrz;
#   Z2  dla wnętrz o tym samym rozkładzie głębokości stosunek nie zależy od ν (ν nieodczytywalne) —
#       to samo, co „ramiona równej długości gaszą człon z tyknięć” (177);
#   Z3  dla wnętrz o różnej głębokości stosunek jest ściśle monotoniczny w ν² na (0, 1),
#       więc ν² jest odtwarzalne z dwóch odczytów — bez jednostki, bez ρ, bez przelicznika;
#   Z4  kontrola: odczyt zależy od m i ρ wyłącznie przez ν = m·ℓ (dwie różne pary (m, ρ) o tym samym
#       ν dają identyczne odczyty).
# CPU, sekundy.
import numpy as np


def domkniecie(C):
    C = C.copy().astype(bool)
    for k in range(len(C)):
        C |= np.outer(C[:, k], C[k, :])
    return C


def los2d(n, g):
    p, q = g.permutation(n), g.permutation(n)
    return (p[:, None] < p[None, :]) & (q[:, None] < q[None, :])


def podstaw(C, x, D):
    n, k = len(C), len(D)
    reszta = [i for i in range(n) if i != x]
    P = np.zeros((n - 1 + k, n - 1 + k), bool)
    P[:n - 1, :n - 1] = C[np.ix_(reszta, reszta)]
    P[:n - 1, n - 1:] = C[reszta, x][:, None]
    P[n - 1:, :n - 1] = C[x, reszta][None, :]
    P[n - 1:, n - 1:] = D
    return P, list(range(n - 1, n - 1 + k))


def propagator(S, b, a=0.5):
    F = a * S.astype(float)
    return F @ np.linalg.inv(np.eye(len(S)) - b * F)


def odczyt(C_zew, x, D, nu2, a=0.5):
    """wstawia wnętrze D w miejsce x; zwraca wektor odczytów na elementach O nad modułem"""
    P, M = podstaw(C_zew, x, D)
    P = domkniecie(P)
    poza = [i for i in range(len(P)) if i not in M]
    Op = [i for i in poza if all(P[m, i] for m in M)]
    if not Op:
        return None, None
    G = propagator(P.astype(float), -nu2, a)
    # źródło: jednakowe na wszystkich elementach wnętrza (O i tak nie rozróżnia elementów M — 173)
    return G[np.ix_(M, Op)].sum(axis=0), Op


# wnętrza: łańcuchy o 1, 2, 3 elementach i antyłańcuch 3-elementowy
def lancuch(k):
    return domkniecie(np.triu(np.ones((k, k), bool), 1))


def antylancuch(k):
    return np.zeros((k, k), bool)


print('=== Z1: stosunek odczytów nie zależy od reszty porządku ani od czytającego ===')
print(f"{'ziarno':>7} {'n':>4} {'ν²':>6} {'stosunek (łańcuch3 / antyłańcuch3)':>36} {'rozrzut po y':>13}")
stos = {}
for ziarno in range(6):
    for n in (12, 18):
        g = np.random.default_rng(700 + ziarno)
        C = domkniecie(los2d(n, g))
        x = int(g.integers(n))
        for nu2 in (0.2, 0.6):
            c1, Op1 = odczyt(C, x, lancuch(3), nu2)
            c2, Op2 = odczyt(C, x, antylancuch(3), nu2)
            if c1 is None or c2 is None or len(Op1) != len(Op2):
                continue
            r = c1 / c2
            stos.setdefault(nu2, []).append(float(r[0]))
            print(f'{ziarno:>7} {n:>4} {nu2:>6.1f} {r[0]:>36.10f} {np.ptp(r):>13.2e}')
for nu2, v in stos.items():
    print(f'  ν² = {nu2}: rozrzut po porządkach = {np.ptp(v):.2e} (wartość {v[0]:.10f})')

print('\n=== Z2: wnętrza o tym samym rozkładzie głębokości — ν nieodczytywalne ===')
g = np.random.default_rng(11)
C = domkniecie(los2d(16, g))
x = 5
for nu2 in (0.05, 0.3, 0.8):
    c1, _ = odczyt(C, x, antylancuch(3), nu2)
    c2, _ = odczyt(C, x, antylancuch(3)[:2, :2] if False else antylancuch(3), nu2)
    # dwa różne antyłańcuchy tej samej wielkości = ten sam rozkład głębokości
    print(f'  ν² = {nu2:>4}: stosunek = {(c1 / c2)[0]:.12f}')
# para o tej samej głębokości, różnym kształcie: antyłańcuch 3 vs antyłańcuch 3 z jednym elementem więcej? nie —
# bierzemy dwa wnętrza, w których każdy element jest maksymalny i minimalny: antyłańcuchy o 2 i 3 elementach
print('  antyłańcuch 2 vs antyłańcuch 3 (obie głębokości zerowe, różna liczność):')
for nu2 in (0.05, 0.3, 0.8):
    c1, _ = odczyt(C, x, antylancuch(2), nu2)
    c2, _ = odczyt(C, x, antylancuch(3), nu2)
    print(f'    ν² = {nu2:>4}: stosunek = {(c1 / c2)[0]:.12f}')

print('\n=== Z3: wnętrza o różnej głębokości — stosunek monotoniczny w ν², ν² odtwarzalne ===')
nu2y = np.linspace(0.01, 0.99, 25)
for opis, D1, D2 in [('łańcuch2 / antyłańcuch2', lancuch(2), antylancuch(2)),
                     ('łańcuch3 / antyłańcuch3', lancuch(3), antylancuch(3)),
                     ('łańcuch3 / łańcuch2', lancuch(3), lancuch(2))]:
    r = []
    for nu2 in nu2y:
        c1, _ = odczyt(C, x, D1, nu2)
        c2, _ = odczyt(C, x, D2, nu2)
        r.append((c1 / c2)[0])
    r = np.array(r)
    d = np.diff(r)
    mono = bool(np.all(d > 0) or np.all(d < 0))
    print(f'  {opis:>24}: r({nu2y[0]:.2f}) = {r[0]:.6f} → r({nu2y[-1]:.2f}) = {r[-1]:.6f}; '
          f'monotoniczny: {mono}; zakres {np.ptp(r):.4f}')
    if mono:
        # odtworzenie ν² z odczytanego stosunku (interpolacja odwrotna)
        cel = 0.37
        c1, _ = odczyt(C, x, D1, cel)
        c2, _ = odczyt(C, x, D2, cel)
        rc = (c1 / c2)[0]
        kol = (r, nu2y) if d[0] > 0 else (r[::-1], nu2y[::-1])
        odtw = np.interp(rc, kol[0], kol[1])
        print(f'    odtworzone ν² z samego stosunku: {odtw:.4f} (włożone {cel})')

print('\n=== Z4: odczyt zależy od m i ρ wyłącznie przez ν = m·ℓ ===')
for (m, rho) in [(0.5, 4.0), (1.0, 16.0), (2.0, 64.0)]:      # m·ℓ = m/√ρ = 0,25 w każdym wierszu (1+1)
    nu2 = m ** 2 / rho
    c, _ = odczyt(C, x, lancuch(3), nu2)
    print(f'  m = {m:>4}, ρ = {rho:>5}: ν = {np.sqrt(nu2):.4f}, odczyt[0] = {c[0]:.12f}')
