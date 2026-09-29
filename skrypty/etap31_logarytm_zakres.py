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


def wklady(X, D, absiD, wD, VD, sigma):
    """zwraca (wkład_s, ε_s) dla modów obszaru U oraz S = Σ wkład"""
    wU = np.where((np.abs(X[:, 0] - 0.5) <= R_U) & (np.abs(X[:, 1] - 0.5) <= R_U))[0]
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
        S_l, e_l, g_l, r2_l = [], [], [], []
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
        if not S_l:
            continue
        wyn.setdefault(ratio, []).append((N, np.mean(S_l), np.mean(e_l), np.mean(g_l)))
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
    print(f'{ratio:>6.1f} {b:>13.3f} {b_lit:>8.2f} {str(K):>7} {de:>8.3f} {str(L2):>4} '
          f'{gest * de:>10.3f} {str(L3):>8}')

print('\n=== L4: kształt wzbudzenia siedzi w gęstości, nie w zakresie ===')
for sigma, ratio, _ in SIGMY:
    d = np.array(wyn[ratio], float)
    print(f'  πR/σ = {ratio:>4}: dS/dε = {d[:, 3].mean():.4f}, ε_max(N=4096) = {d[-1, 2]:.3f}')
em = np.array([np.array(wyn[r], float)[-1, 2] for _, r, _ in SIGMY])
print(f'  rozrzut ε_max po kształtach: {np.ptp(em) / em.mean() * 100:.1f}% (L4: < 10%)')
