# etap29 — węzeł (M, O) zestawiony z masą (§F1) i działaniem (R1f): co O czyta z wnętrza, gdy jest masa.
#
# Kontekst: 172–173 — węzeł = para (M, O), M moduł względem O; 175 — z masą (sumy po drogach) elementy
# wnętrza o różnej głębokości waży O różnie; 177 — obieg = diament; §F1/166 — „masa” ma dwa odczyty
# (A = na własne tyknięcie, B = współczynnik przy rozdzielczości); R1f-3 — cztery odczyty tej samej fazy.
# Propagator z masą: Johnston, arXiv:0806.3083, hop-stop: G = Φ + b·Φ·G ⇒ G = Φ(I − bΦ)⁻¹,
# Φ = a·(macierz skoków), b = −m²V₀ = waga zatrzymania w elemencie (168 pkt 1a).
#
# TWIERDZENIE (na kartce; rachunek niżej jest kontrolą, nie dowodem):
#   M moduł względem O, x ∈ M, y ∉ M, M ≺ y. Każda droga x = v₀ ≺ … ≺ v_n = y ma ostatni element
#   v_j ∈ M; v_{j+1} ∉ M i v_j ≺ v_{j+1}, więc z modułowości M ≺ v_{j+1}, a droga nie wraca do M
#   (element między dwoma elementami M musiałby leżeć w M). Waga drogi rozpada się na część wewnątrz M
#   (do v_j, z zatrzymaniem w v_j — chyba że v_j = x, wtedy to początek drogi) i część poza M, która
#   nie zależy od tego, przez który element M droga wyszła. Stąd
#       G[x, y] = g(x) · h(y),  g(x) = Σ_w (I + b·G_M)[x, w],  h(y) bez zależności od x.
#   Czynnik g należy do M (ten sam dla każdego czytającego), h — do czytającego.
#
# ZDANIA PRZED PRZEBIEGIEM (mogą upaść):
#   Z1  blok G[M, O⁺] ma rząd DOKŁADNIE 1, także z masą; to samo G[O⁻, M]. Upadek = różni czytający
#       czytają różne kombinacje wnętrza, czyli to, co O czyta z M, nie jest jedną liczbą.
#   Z2  rozkład dokładny: G[x, y] = g(x)·h(y), błąd względny < 1e-10.
#   Z3  g(x) = Σ_w (I + b·G_M)[x, w]; g stała dokładnie wtedy, gdy b = 0 albo wszystkie elementy M
#       mają tę samą ważoną głębokość (wnętrze bez relacji = bliźniaki, 173: węzłem nie są).
#       PIERWSZA WERSJA UPADŁA (100/102): zapisałem g = Σ_w (I + G_M)[x, w], bez wagi zatrzymania b
#       w ostatnim elemencie wnętrza. Błąd asystenta, zapisany w rejestrze.
#   Z4  kontrola negatywna (czy zdanie coś wyróżnia — pułapka 3): dla losowych podzbiorów niebędących
#       modułami rząd > 1 w większości prób.
#   Z5  skoki po linkach (światło): rozkład zachodzi tak samo, a suma w g biegnie po elementach M
#       mających link na zewnątrz (elementy maksymalne w M).
# CPU, sekundy.
import numpy as np


def domkniecie(C):
    C = C.copy().astype(bool)
    for k in range(len(C)):
        C |= np.outer(C[:, k], C[k, :])
    return C


def linki(C):
    Ci = C.astype(int)
    return ((Ci == 1) & ((Ci @ Ci) == 0)).astype(float)


def los2d(n, g):
    p, q = g.permutation(n), g.permutation(n)
    return (p[:, None] < p[None, :]) & (q[:, None] < q[None, :])


def podstaw(C, x, D):
    """wstawia porządek D w miejsce elementu x porządku C; zwraca porządek i indeksy modułu"""
    n, k = len(C), len(D)
    reszta = [i for i in range(n) if i != x]
    P = np.zeros((n - 1 + k, n - 1 + k), bool)
    P[:n - 1, :n - 1] = C[np.ix_(reszta, reszta)]
    P[:n - 1, n - 1:] = C[reszta, x][:, None]
    P[n - 1:, :n - 1] = C[x, reszta][None, :]
    P[n - 1:, n - 1:] = D
    return P, list(range(n - 1, n - 1 + k))


def propagator(S, b, a=0.5):
    """G = Φ(I − bΦ)⁻¹, Φ = a·S; G[x, y] = suma po drogach od x do y"""
    F = a * S.astype(float)
    return F @ np.linalg.inv(np.eye(len(S)) - b * F)


def rzad(B):
    """(druga wartość osobliwa / pierwsza); 0 = rząd dokładnie 1"""
    if min(B.shape) < 2 or not np.any(B):
        return 0.0, int(np.linalg.matrix_rank(B, tol=1e-12))
    s = np.linalg.svd(B, compute_uv=False)
    return s[1] / s[0], int(np.linalg.matrix_rank(B, tol=1e-10 * s[0]))


def blad_rozkladu(B):
    """największy błąd względny najlepszego przybliżenia g⊗h"""
    U, s, Vt = np.linalg.svd(B)
    return np.abs(B - s[0] * np.outer(U[:, 0], Vt[0])).max() / np.abs(B).max()


def waga_wnetrza(S_M, b, a=0.5, wyjscia=None):
    """g(x) = Σ_w (I + b·G_M)[x, w]; przy skokach po linkach suma biegnie po wyjściach modułu"""
    G_M = propagator(S_M, b, a)
    W = np.eye(len(S_M)) + b * G_M
    return W.sum(axis=1) if wyjscia is None else W[:, wyjscia].sum(axis=1)


def para(n, k, ziarno, wagi='relacje'):
    """losowy porządek z wstawionym modułem M; zwraca porządek, M, czytających nad i pod M"""
    g = np.random.default_rng(ziarno)
    P, M = podstaw(domkniecie(los2d(n, g)), int(g.integers(n)), domkniecie(los2d(k, g)))
    P = domkniecie(P)
    poza = [i for i in range(len(P)) if i not in M]
    Op = [i for i in poza if all(P[m, i] for m in M)]
    Om = [i for i in poza if all(P[i, m] for m in M)]
    if not Op or not Om:
        return None
    S = P.astype(float) if wagi == 'relacje' else linki(P)
    return dict(P=P, M=M, Op=Op, Om=Om, S=S, S_M=S[np.ix_(M, M)])


PARAMS = [(14, 4), (18, 5), (22, 6), (26, 3)]
B_LIST = [0.0, -0.3, -0.9]

print('=== Z1, Z2, Z3: co O czyta z wnętrza węzła ===')
print(f"{'n':>4} {'k':>3} {'b':>6} {'s2/s1 M→O⁺':>12} {'s2/s1 O⁻→M':>12} {'błąd g⊗h':>10} "
      f"{'g stała':>8} {'g − wzór':>10}")
zle = {'Z1': 0, 'Z2': 0, 'Z3': 0}
stale_z_masa, prob = 0, 0
for ziarno in range(12):
    for (n, k) in PARAMS:
        for b in B_LIST:
            w = para(n, k, ziarno * 100 + n + k)
            if w is None:
                continue
            prob += 1
            G = propagator(w['S'], b)
            B, B2 = G[np.ix_(w['M'], w['Op'])], G[np.ix_(w['Om'], w['M'])]
            r1, _ = rzad(B)
            r2, _ = rzad(B2)
            e = blad_rozkladu(B)
            kol, gg = B[:, 0], waga_wnetrza(w['S_M'], b)
            stala = np.ptp(kol) / np.abs(kol).max() < 1e-12
            odch = np.abs(kol / kol[0] - gg / gg[0]).max()
            plaskie = np.ptp(gg) / np.abs(gg).max() < 1e-12      # wszystkie głębokości równe
            zle['Z1'] += (r1 > 1e-10) or (r2 > 1e-10)
            zle['Z2'] += e > 1e-10
            zle['Z3'] += (odch > 1e-10) or (stala != (b == 0.0 or plaskie))
            stale_z_masa += (b != 0.0) and stala
            if ziarno < 2:
                print(f'{n:>4} {k:>3} {b:>6.1f} {r1:>12.2e} {r2:>12.2e} {e:>10.2e} '
                      f'{str(stala):>8} {odch:>10.2e}')
print(f'\npróby: {prob}; naruszenia — Z1: {zle["Z1"]}, Z2: {zle["Z2"]}, Z3: {zle["Z3"]}')
print(f'g stała mimo masy: {stale_z_masa} — wszystkie z wnętrzem bez relacji (bliźniaki, 173)')

print('\n=== Z4: kontrola negatywna — losowe podzbiory, nie moduły ===')
prob_n, wieksze = 0, 0
wg_Op = {}
for ziarno in range(800):
    g = np.random.default_rng(10000 + ziarno)
    P = domkniecie(los2d(20, g))
    K = sorted(g.choice(20, 5, replace=False).tolist())
    poza = [i for i in range(20) if i not in K]
    Op = [i for i in poza if all(P[m, i] for m in K)]
    if len(Op) < 2:
        continue
    if all(all(P[m, i] == P[K[0], i] and P[i, m] == P[i, K[0]] for m in K) for i in poza):
        continue                                                  # to jednak moduł
    prob_n += 1
    r, _ = rzad(propagator(P.astype(float), -0.6)[np.ix_(K, Op)])
    wieksze += r > 1e-10
    if r <= 1e-10:
        wg_Op[len(Op)] = wg_Op.get(len(Op), 0) + 1
print(f'  nie-moduły: {prob_n}; z rzędem > 1: {wieksze}; rząd 1 przypadkiem: {prob_n - wieksze}')
print(f'  przypadkowy rząd 1 wg liczby czytających: {dict(sorted(wg_Op.items()))}')

print('\n=== Z5: skoki po linkach (światło) ===')
for ziarno in range(6):
    w = para(20, 5, ziarno, wagi='linki')
    if w is None:
        continue
    G = propagator(w['S'], -0.6)
    B = G[np.ix_(w['M'], w['Op'])]
    if not np.any(B):
        continue
    r, rk = rzad(B)
    wyj = [i for i in range(len(w['M'])) if w['S_M'][i].sum() == 0]     # elementy bez linku w M w górę
    gg = waga_wnetrza(w['S_M'], -0.6, wyjscia=wyj)
    kol = B[:, 0]
    odch = np.abs(kol / kol[0] - gg / gg[0]).max() if kol[0] != 0 and gg[0] != 0 else np.nan
    print(f'  ziarno {ziarno}: s2/s1 = {r:.2e}, rząd = {rk}, błąd g⊗h = {blad_rozkladu(B):.2e}, '
          f'g − wzór(wyjścia) = {odch:.2e}')

print('\n=== rozdział stron pary: g (wnętrze M) i h (czytający) ===')
w = para(20, 5, 7)
G = propagator(w['S'], -0.6)
B = G[np.ix_(w['M'], w['Op'])]
U, s, Vt = np.linalg.svd(B)
g, h = U[:, 0] * s[0], Vt[0]
print('  g z bloku (unormowane): ', np.round(g / g[0], 6))
print('  g ze wzoru:             ', np.round(waga_wnetrza(w['S_M'], -0.6) / waga_wnetrza(w['S_M'], -0.6)[0], 6))
print('  h czytających:          ', np.round(h / h[0], 6))
print('  -> jeden czynnik wewnętrzny dla każdego czytającego; czytający różnią się tylko własnym h')
