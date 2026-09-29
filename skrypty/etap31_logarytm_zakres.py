# etap31 — skąd logarytm w entropii względnej (170): zakres czy gęstość?
#
# Propozycja użytkownika (29.09): „liczba miejsc, przez które przechodzi odczyt, rośnie multiplikatywnie
# z rozdzielczością, nie addytywnie. Jeśli to da się postawić z samej struktury odczytu, logarytm wypadnie
# sam i nie trzeba go wkładać.”
#
# Przekład na to, co jest policzone (170): S = a + b·log₂N na nieobciętym porządku, b tylko od πR/σ.
# Hamiltonian modularny diamentu generuje pchnięcie konforemne (Casini–Huerta–Myers 2011; Bisognano–Wichmann),
# więc energia modularna ε JEST rapidity — „miejscem”, o którym mówi propozycja. Wtedy:
#     S = (gęstość wkładu na jednostkę ε) × (zakres ε),
# a logarytm pochodzi z zakresu: ε_max rośnie jak ln N, bo liczba rozróżnialnych ram rośnie jak N
# (§F2: ∫du/u = ln N, koszt wskazania ramy — współczynniki 1, ½, 0,834 policzone tą samą drogą).
# Nic nie trzeba wkładać: logarytm jest zakresem pchnięć, tak jak wszędzie indziej w 1+1.
#
# ZDANIA PRZED PRZEBIEGIEM (mogą upaść):
#   K   kontrola odtworzenia: b (przyrost S na podwojenie N) zgodne z 170 w ±25% —
#       0,19 / 0,45 / 0,60 dla πR/σ = 3,3 / 6,5 / 9,8 (σ = 0,24 / 0,12 / 0,08 przy R = 0,25).
#   L1  wkład do S rozłożony po ε jest PŁASKI: skumulowane S(<ε) liniowe w ε na [1, ε_max],
#       czyli dS/dε ≈ const (R² dopasowania liniowego > 0,95). Upadek = wkład skupiony w wąskim ε.
#   L2  zakres rośnie logarytmicznie: ε_max rośnie 0,4–0,7 na podwojenie N (170: pułap 0,5–0,6).
#   L3  ZWIĄZEK: b ≈ (dS/dε)·(przyrost ε_max na podwojenie), zgodność w ±30%. To wiąże dwie wielkości
#       mierzone osobno — jeśli nie zachodzi, logarytm nie jest zakresem pchnięć.
#   L4  zależność od kształtu wzbudzenia siedzi w GĘSTOŚCI, nie w zakresie: dS/dε rośnie z πR/σ,
#       a ε_max od πR/σ nie zależy (rozrzut < 10%).
#
# WYNIK v1 (N = 512…4096, πR/σ = 3,3 / 6,5 / 9,8): K PRZESZŁO (b = 0,160 / 0,417 / 0,528 wobec 0,19 / 0,45 / 0,60
# z 170 — uproszczona wersja czynnikowa odtwarza pomiar GPU); L2 PRZESZŁO (Δε_max = 0,434 na podwojenie,
# to samo dla każdego kształtu); L1 MIESZANE (R² rośnie z N dla fali gładkiej: 0,90 → 0,97; maleje dla ostrej:
# 0,66 → 0,31); L3 PRZESZŁO tylko dla 3,3, UPADŁO dla 6,5 i 9,8 (b = 0,417 / 0,528 wobec iloczynu 0,145 / 0,153);
# L4 UPADŁO w części „gęstość”: średnia dS/dε jest ta sama dla wszystkich kształtów (0,346 / 0,335 / 0,352),
# a b różni się trzykrotnie. Zakres zachowuje się tak, jak przewiduje propozycja; średnia gęstość nie.
# Diagnoza (przed v2): przyrost zakresu dokłada mody wyłącznie na GÓRNYM końcu widma, a wkład ostrej fali
# jest tam skupiony (170, T3: 2% najcięższych modów niesie ≥ 70% S) — więc b ustala gęstość lokalna przy ε_max,
# nie średnia po całym widmie.
#
# ZDANIE v2 (zapisane przed przebiegiem v2):
#   L3′ b ≈ (gęstość wkładu w pasie ε ∈ [ε_max − 1, ε_max]) × Δε_max, ±30%, dla wszystkich trzech kształtów.
#       Upadek = logarytmu nie tłumaczy sam zakres pchnięć.
#
# WYNIK v2: L3′ UPADŁO w drugą stronę — iloczyn 0,743 / 1,629 / 1,744 wobec b = 0,160 / 0,417 / 0,528
# (przeszacowanie 3,3–4,6×). Gęstość w górnym pasie jest 5–11× większa od średniej, ale przyrost S jest
# znacznie mniejszy: przy rosnącym N cały rozkład wkładów po ε maleje (średnia gęstość 0,42 → 0,30),
# zamiast dokładać nowy pas przy ustalonej reszcie. Rozkład „gęstość × zakres” nie opisuje S.
#
# ZDANIE v3 (zapisane przed przebiegiem v3) — test wprost, bez rozkładania na czynniki:
#   L5  S zależy od N i od obszaru WYŁĄCZNIE przez ε_max: punkty (ε_max, S) dla dwóch obszarów
#       (R_U = 0,25 i 0,125, ta sama fala względem obszaru) leżą na jednej krzywej — odchylenie < 15%.
#       Przejście = logarytm jest zakresem pchnięć, mimo że nie rozkłada się na gęstość × zakres.
#       Upadek = zakres nie wystarcza; S zależy od N także poza nim.
#
# OGRANICZENIA (zapisane przed przebiegiem): wersja czynnikowa (jądro iΔ_U odrzucone) — udział centrum
# maleje jak N^−0,8 i przy tych N wynosi ułamek procenta (170), ale to jest przybliżenie; N = 512…4096,
# czyli 0,9 dekady — poniżej progu z §E, więc to test MECHANIZMU, nie nowa wartość b (b zmierzone w 170
# na 1,3 dekady). Literaturowe 1+1 = narzędzie bez triady (pułapka 5).
import numpy as np

R_U = 0.25          # połowa boku poddiamentu w (u, v): V/V_U = 4
U0 = 0.5            # środek fali
AMPL = 1.0
PROG = 1e-10        # próg jądra (względem największej wartości własnej)


def rozsiew(N, rng):
    """N punktów w diamencie [0,1]² we współrzędnych stożkowych (u, v)"""
    return rng.random((N, 2))


def macierz_D(X):
    """D = K_R − K_Rᵀ, K_R = ½C; C[i,j] = 1 gdy i ≺ j (u_i < u_j i v_i < v_j)"""
    C = (X[:, 0][:, None] < X[:, 0][None, :]) & (X[:, 1][:, None] < X[:, 1][None, :])
    K = 0.5 * C.astype(float)
    return K - K.T


def stan_SJ(D):
    """iΔ = iD; W = ½(|iΔ| + iΔ); R = Re W = ½|iΔ| — z pełnej diagonalizacji"""
    w, V = np.linalg.eigh(1j * D)
    absiD = (V * np.abs(w)) @ V.conj().T
    return absiD, w, V


def fala(X, sigma):
    """nieparzysty profil w u (bez składowej stałej — podczerwień 1+1)"""
    z = (X[:, 0] - U0) / sigma
    return AMPL * z * np.exp(-0.5 * z * z)


def wklady(X, D, absiD, wD, VD, sigma, r_u=None):
    """zwraca (wkład_s, ε_s) dla modów obszaru U oraz S = Σ wkład"""
    r_u = R_U if r_u is None else r_u
    wU = np.where((np.abs(X[:, 0] - 0.5) <= r_u) & (np.abs(X[:, 1] - 0.5) <= r_u))[0]
    if len(wU) < 20:
        return None
    iD_U = (1j * D)[np.ix_(wU, wU)]
    G_U = 0.5 * absiD[np.ix_(wU, wU)]                    # Γ = R|_U

    # rzut przesunięcia na obraz iΔ (pełnego), potem obcięcie do U
    obraz = np.abs(wD) > PROG * np.abs(wD).max()
    d = fala(X, sigma).astype(complex)
    d = VD[:, obraz] @ (VD[:, obraz].conj().T @ d)
    dU = d[wU]

    # obraz iΔ_U (odrzucenie centrum — wersja czynnikowa)
    lu, Vu = np.linalg.eigh(iD_U)
    ob = np.abs(lu) > PROG * np.abs(lu).max()
    P = Vu[:, ob]
    iD_r = (P.conj().T @ iD_U @ P)
    G_r = (P.conj().T @ G_U @ P)

    # Γ^{1/2} i Γ^{-1/2} na obrazie
    g, Vg = np.linalg.eigh(G_r)
    dodat = g > PROG * g.max()
    Q, gd = Vg[:, dodat], g[dodat]
    G_half = (Q * np.sqrt(gd)) @ Q.conj().T
    G_mhalf = (Q / np.sqrt(gd)) @ Q.conj().T

    X_mod = G_half @ np.linalg.inv(iD_r) @ G_half
    X_mod = 0.5 * (X_mod + X_mod.conj().T)
    nu, Y = np.linalg.eigh(X_mod)

    proj = Y.conj().T @ (G_mhalf @ (P.conj().T @ dU))
    an = np.abs(nu)
    ok = an > 0.5 + 1e-9
    eps = np.zeros_like(an)
    eps[ok] = np.log((an[ok] + 0.5) / (an[ok] - 0.5))
    wk = 0.5 * an * eps * np.abs(proj) ** 2
    return wk[ok], eps[ok], float(wk.sum())


def gestosc_gorna(wk, eps, pas=1.0):
    """wkład na jednostkę ε w górnym pasie widma — tam, gdzie przyrost zakresu dokłada nowe mody"""
    em = eps.max()
    sel = eps >= em - pas
    return float(wk[sel].sum() / pas)


def nachylenie(x, y):
    A = np.vstack([x, np.ones_like(x)]).T
    wsp, *_ = np.linalg.lstsq(A, y, rcond=None)
    pred = A @ wsp
    ss = 1 - ((y - pred) ** 2).sum() / max(((y - y.mean()) ** 2).sum(), 1e-30)
    return wsp[0], wsp[1], ss


SIGMY = [(0.24, 3.3, 0.19), (0.12, 6.5, 0.45), (0.08, 9.8, 0.60)]
NY = [512, 1024, 2048, 4096]
ZIARNA_MALE, ZIARNA_DUZE = [1, 2], [1]   # przy N = 4096 jedno ziarno (koszt)

print('=== S(N) i zakres widma modularnego ===')
print(f"{'πR/σ':>6} {'N':>6} {'S':>9} {'ε_max':>8} {'dS/dε':>9} {'R² (L1)':>8} {'modów':>7}")
wyn = {}
for sigma, ratio, b_lit in SIGMY:
    for N in NY:
        S_l, e_l, g_l, r2_l, gg_l = [], [], [], [], []
        for z in (ZIARNA_DUZE if N >= 4096 else ZIARNA_MALE):
            rng = np.random.default_rng(1000 * z + N)
            X = rozsiew(N, rng)
            D = macierz_D(X)
            absiD, wD, VD = stan_SJ(D)
            r = wklady(X, D, absiD, wD, VD, sigma)
            if r is None:
                continue
            wk, eps, S = r
            kol = np.argsort(eps)
            e_s, w_s = eps[kol], wk[kol]
            skum = np.cumsum(w_s)
            sel = e_s >= 1.0
            if sel.sum() > 10:
                nach, _, r2 = nachylenie(e_s[sel], skum[sel])
            else:
                nach, r2 = np.nan, np.nan
            S_l.append(S); e_l.append(e_s.max()); g_l.append(nach); r2_l.append(r2)
            gg_l.append(gestosc_gorna(w_s, e_s))
        if not S_l:
            continue
        wyn.setdefault(ratio, []).append((N, np.mean(S_l), np.mean(e_l), np.mean(g_l), np.mean(gg_l)))
        print(f'{ratio:>6.1f} {N:>6} {np.mean(S_l):>9.3f} {np.mean(e_l):>8.3f} '
              f'{np.mean(g_l):>9.4f} {np.mean(r2_l):>8.3f} {len(wk):>7}')

print('\n=== K, L2, L3: przyrosty na podwojenie N ===')
print(f"{'πR/σ':>6} {'b (rachunek)':>13} {'b (170)':>8} {'K ±25%':>7} {'Δε_max':>8} {'L2':>4} "
      f"{'dS/dε·Δε':>10} {'L3 ±30%':>8}")
for sigma, ratio, b_lit in SIGMY:
    d = np.array(wyn[ratio], float)
    lg = np.log2(d[:, 0])
    b, _, _ = nachylenie(lg, d[:, 1])
    de, _, _ = nachylenie(lg, d[:, 2])
    gest = d[:, 3].mean()
    K = abs(b - b_lit) / b_lit < 0.25
    L2 = 0.4 <= de <= 0.7
    L3 = abs(gest * de - b) / max(b, 1e-9) < 0.30
    gg = d[:, 4].mean()
    L3p = abs(gg * de - b) / max(b, 1e-9) < 0.30
    print(f'{ratio:>6.1f} {b:>13.3f} {b_lit:>8.2f} {str(K):>7} {de:>8.3f} {str(L2):>4} '
          f'{gest * de:>10.3f} {str(L3):>8}  | górny pas: gęstość {gg:>6.3f}, '
          f'iloczyn {gg * de:>6.3f}, L3′ {str(L3p)}')

print('\n=== L4: kształt wzbudzenia siedzi w gęstości, nie w zakresie ===')
for sigma, ratio, _ in SIGMY:
    d = np.array(wyn[ratio], float)
    print(f'  πR/σ = {ratio:>4}: dS/dε = {d[:, 3].mean():.4f}, ε_max(N=4096) = {d[-1, 2]:.3f}')
em = np.array([np.array(wyn[r], float)[-1, 2] for _, r, _ in SIGMY])
print(f'  rozrzut ε_max po kształtach: {np.ptp(em) / em.mean() * 100:.1f}% (L4: < 10%)')


print('\n=== L5: czy S zależy od N i obszaru wyłącznie przez ε_max ===')
print(f"{'R_U':>6} {'σ':>6} {'N':>6} {'N_U':>6} {'ε_max':>8} {'S':>9}")
pkt = []
for r_u, sig in [(0.25, 0.12), (0.125, 0.06)]:            # to samo πR/σ = 6,5 względem obszaru
    for N in (1024, 2048, 4096):
        rng = np.random.default_rng(1000 + N)
        X = rozsiew(N, rng)
        D = macierz_D(X)
        absiD, wD, VD = stan_SJ(D)
        r = wklady(X, D, absiD, wD, VD, sig, r_u=r_u)
        if r is None:
            continue
        wk, eps, S = r
        nU = int(((np.abs(X[:, 0] - 0.5) <= r_u) & (np.abs(X[:, 1] - 0.5) <= r_u)).sum())
        pkt.append((r_u, eps.max(), S))
        print(f'{r_u:>6.3f} {sig:>6.2f} {N:>6} {nU:>6} {eps.max():>8.3f} {S:>9.3f}')

duze = np.array([(e, s) for r, e, s in pkt if r == 0.25], float)
male = np.array([(e, s) for r, e, s in pkt if r == 0.125], float)
if len(duze) > 1 and len(male) > 0:
    odch = []
    for e, s in male:
        if duze[:, 0].min() - 0.5 <= e <= duze[:, 0].max() + 0.5:
            s_int = np.interp(e, duze[:, 0], duze[:, 1])
            odch.append(abs(s - s_int) / max(s_int, 1e-9))
    if odch:
        print(f'  odchylenie małego obszaru od krzywej dużego: {max(odch) * 100:.1f}% (L5: < 15%)')
    else:
        print('  zakresy ε_max się nie pokrywają — L5 nierozstrzygnięte przy tych N')
