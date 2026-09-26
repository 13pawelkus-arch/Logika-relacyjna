# etap26c — niezależne kontrole wzorów z etap26 (entropia względna stanu koherentnego; poprawka 170)
#
# PO CO. etap26 i etap26b liczą S(ρ_δ‖ρ) wzorem, nie z macierzy gęstości. Tu wzory sprawdzone inną drogą,
# na małych układach, gdzie da się policzyć wprost (wcześniej: kontrole w scratchpadzie sesji 26.09, tu zebrane,
# żeby liczby z pliku głównego były do wglądu).
#
# WZÓR (czynnik, stan gaussowski o kowariancji Γ i komutatorze Ω, przesunięcie δ):
#   X = Γ^{1/2}(iΩ)^{-1}Γ^{1/2} (wartości ±ν), S = ½ Σ_s |ν_s| ε(|ν_s|) |⟨y_s, Γ^{-1/2}δ⟩|², ε(ν) = ln((ν+½)/(ν−½)).
#   Dla przesunięcia forma kwadratowa jest CAŁĄ entropią względną (log ρ kwadratowy, człon liniowy ma średnią 0).
# WZÓR (algebra z centrum — Ω z jądrem K, w którym W ≠ 0): reguła łańcuchowa po rozkładzie na centrum:
#   S_full = ½ δ_K† Γ_KK⁻¹ δ_K + ½ δ̃† h(Γ_c) δ̃, Γ_c = Γ_II − Γ_IK Γ_KK⁻¹ Γ_KI, δ̃ = δ_I − Γ_IK Γ_KK⁻¹ δ_K.
#
# ZDANIA (przed rachunkiem):
#   F1 jeden mod ściśnięty termiczny: wzór = Tr ρ_δ(ln ρ_δ − ln ρ) w bazie Focka (n ≤ 79) do 1e-7;
#   F2 dwa mody splątane: różnica wzór − Fock maleje ze wzrostem obcięcia bazy Focka (błąd obcięcia, nie wzoru);
#   C1 algebra z centrum: centrum zregularyzowane małym komutatorem η (pary zmiennych klasycznych) → wzór
#      niezdegenerowany; różnica do S_full maleje liniowo z η (η = 1e-2 … 1e-5);
#   C2 (raport) samo warunkowanie na centrum zmienia wynik także przy δ_K = 0 (S_full ≠ S_czynnik).
#
# WYNIK (26.09, CPU, 91 s): F1 PRZESZŁO — max różnica 2,1e-9 w 4 przypadkach; F2 PRZESZŁO — różnica 3,2e-4 / 7,7e-6 /
#   1,2e-7 / 2,2e-9 przy n ≤ 21 / 29 / 37 / 45 (błąd obcięcia bazy Focka); C1 PRZESZŁO — różnica przy η = 1e-5 ≤ 1,1e-5,
#   ~10× mniejsza na dekadę η; C2 S_full / S_czynnik przy δ_K = 0: 7,31 / 3,72, 2,36 / 1,89, 5,29 / 4,82, 4,89 / 2,87.
#
# URUCHOMIENIE: python3 etap26c_kontrola_wzorow.py   (CPU, ~1,5 min; część F2 dominuje)
import time
import numpy as np


def expa(M):
    """exp(M) dla M antyhermitowskiego (przez eigh)."""
    H = -1j * M
    H = (H + H.conj().T) / 2
    l, V = np.linalg.eigh(H)
    return (V * np.exp(1j * l)) @ V.conj().T


def logh(R):
    R = (R + R.conj().T) / 2
    l, V = np.linalg.eigh(R)
    return (V * np.log(np.clip(l, 1e-300, None))) @ V.conj().T


def eps(a):
    return np.log((a + 0.5) / (a - 0.5))


def wzor(G, Om, d):
    """½ δᵀ h δ dla Ω niezdegenerowanego."""
    g, O = np.linalg.eigh(G)
    Gh = (O * np.sqrt(g)) @ O.T
    Gmh = (O / np.sqrt(g)) @ O.T
    X = Gh @ np.linalg.inv(1j * Om) @ Gh
    X = (X + X.conj().T) / 2
    nu, Y = np.linalg.eigh(X)
    a = np.abs(nu)
    return 0.5 * np.sum(a * eps(a) * np.abs(Y.conj().T @ (Gmh @ d)) ** 2)


def J(n):
    Jm = np.zeros((2 * n, 2 * n))
    for i in range(n):
        Jm[2 * i, 2 * i + 1], Jm[2 * i + 1, 2 * i] = 1, -1
    return Jm


def F1():
    n = 80
    a = np.diag(np.sqrt(np.arange(1, n)), 1).astype(complex)
    ad = a.conj().T
    x, p = (a + ad) / np.sqrt(2), (a - ad) / (1j * np.sqrt(2))
    Om = J(1)
    wynik = []
    for nbar, r, dx, dp in ((0.3, 0.0, 0.4, 0.0), (0.3, 0.5, 0.4, -0.2), (1.2, -0.4, 0.1, 0.3), (0.05, 0.8, -0.3, 0.25)):
        rho = np.diag((nbar / (1 + nbar)) ** np.arange(n) / (1 + nbar)).astype(complex)
        Sq = expa(0.5 * r * (a @ a - ad @ ad))
        rho = Sq @ rho @ Sq.conj().T
        Q = [x, p]
        G = np.array([[np.trace(rho @ (Qi @ Qj + Qj @ Qi) / 2).real for Qj in Q] for Qi in Q])
        al = (dx + 1j * dp) / np.sqrt(2)
        D = expa(al * ad - np.conj(al) * a)
        rd = D @ rho @ D.conj().T
        S_f = np.trace(rd @ (logh(rd) - logh(rho))).real
        S_w = wzor(G, Om, np.array([dx, dp]))
        wynik.append(abs(S_f - S_w))
        print(f'  F1 n̄={nbar}, r={r:+.1f}, δ=({dx},{dp}): Fock {S_f:.8f} | wzór {S_w:.8f} | różnica {abs(S_f - S_w):.1e}')
    print(f'F1: max różnica {max(wynik):.1e} → {"PRZESZŁO" if max(wynik) < 1e-7 else "UPADŁO"}')


def F2():
    Om = J(2)
    d = np.array([0.3, -0.1, 0.2, 0.25])
    roznice = []
    for n in (22, 30, 38, 46):
        t0 = time.time()
        a1 = np.diag(np.sqrt(np.arange(1, n)), 1).astype(complex)
        I = np.eye(n)
        A, B = np.kron(a1, I), np.kron(I, a1)
        Ad, Bd = A.conj().T, B.conj().T
        Q = [(A + Ad) / np.sqrt(2), (A - Ad) / (1j * np.sqrt(2)), (B + Bd) / np.sqrt(2), (B - Bd) / (1j * np.sqrt(2))]
        nb1, nb2 = 0.2, 0.5
        th = np.kron(np.diag((nb1 / (1 + nb1)) ** np.arange(n) / (1 + nb1)),
                     np.diag((nb2 / (1 + nb2)) ** np.arange(n) / (1 + nb2))).astype(complex)
        S2 = expa(0.4 * (A @ B - Ad @ Bd))          # ściśnięcie dwumodowe (splątanie)
        BS = expa(0.7 * (Ad @ B - A @ Bd))          # dzielnik wiązki
        rho = BS @ S2 @ th @ S2.conj().T @ BS.conj().T
        G = np.array([[np.trace(rho @ (Qi @ Qj + Qj @ Qi) / 2).real for Qj in Q] for Qi in Q])
        al1, al2 = (d[0] + 1j * d[1]) / np.sqrt(2), (d[2] + 1j * d[3]) / np.sqrt(2)
        D = expa(al1 * Ad - np.conj(al1) * A + al2 * Bd - np.conj(al2) * B)
        rd = D @ rho @ D.conj().T
        S_f = np.trace(rd @ (logh(rd) - logh(rho))).real
        S_w = wzor(G, Om, d)
        roznice.append(abs(S_f - S_w))
        print(f'  F2 n ≤ {n - 1}: Fock {S_f:.8f} | wzór {S_w:.8f} | różnica {abs(S_f - S_w):.1e} ({time.time() - t0:.0f} s)', flush=True)
    malejaco = all(roznice[i + 1] < roznice[i] for i in range(len(roznice) - 1))
    print(f'F2: różnica maleje z obcięciem: {"tak" if malejaco else "nie"}; przy największym n {roznice[-1]:.1e} '
          f'→ {"PRZESZŁO" if malejaco and roznice[-1] < 1e-6 else "UPADŁO"}')


def M_niezdeg(G, iOm):
    g, O = np.linalg.eigh((G + G.conj().T) / 2)
    Gh = (O * np.sqrt(g)) @ O.conj().T
    Gmh = (O / np.sqrt(g)) @ O.conj().T
    X = Gh @ (Gh / iOm[:, None])
    X = (X + X.conj().T) / 2
    nu, Y = np.linalg.eigh(X)
    a = np.abs(nu)
    return Gmh @ (Y * (a * eps(np.maximum(a, 0.5 + 1e-15)))) @ Y.conj().T @ Gmh


def S_z_centrum(Gam, Om, d, tol=1e-12):
    mu, Q = np.linalg.eigh(1j * Om)
    sel = np.abs(mu) > tol * np.abs(mu).max()
    P, Qk, m = Q[:, sel], Q[:, ~sel], mu[sel]
    GII, dI = P.conj().T @ Gam @ P, P.conj().T @ d
    SF = 0.5 * np.real(dI.conj() @ M_niezdeg(GII, m) @ dI)
    GIK, GKK, dK = P.conj().T @ Gam @ Qk, Qk.conj().T @ Gam @ Qk, Qk.conj().T @ d
    A = np.linalg.solve(GKK, GIK.conj().T).conj().T          # Γ_IK Γ_KK⁻¹
    Gc, dt = GII - A @ GIK.conj().T, dI - A @ dK
    Scl = 0.5 * np.real(dK.conj() @ np.linalg.solve(GKK, dK))
    return Scl + 0.5 * np.real(dt.conj() @ M_niezdeg(Gc, m) @ dt), SF


def C12():
    rng = np.random.default_rng(7)
    m, kpar = 2, 2                    # 2 mody kwantowe + 2 położenia dodatkowych modów jako centrum
    najgorsza = 0.0
    for proba in range(4):
        H = rng.normal(size=(2 * (m + kpar), 2 * (m + kpar)))
        H = H + H.T
        Jm = J(m + kpar)
        lam, U = np.linalg.eig(Jm @ H * 0.3)
        S = np.real(U @ np.diag(np.exp(lam)) @ np.linalg.inv(U))       # symplektyczne: exp(J H · 0,3)
        Gfull = 0.5 * S @ S.T + (0.02 + 0.05 * proba) * np.eye(2 * (m + kpar))
        idx = list(range(2 * m)) + [2 * m + 2 * j for j in range(kpar)]
        Gam = Gfull[np.ix_(idx, idx)]
        nwym = len(idx)
        Om0 = np.zeros((nwym, nwym))
        Om0[:2 * m, :2 * m] = J(m)
        for dK_zero in (False, True):
            d = rng.normal(size=nwym)
            if dK_zero:
                d[2 * m:] = 0.0
            Sfull, SF = S_z_centrum(Gam, Om0, d)
            wiersz = []
            for eta in (1e-2, 1e-3, 1e-4, 1e-5):
                Om = Om0.copy()
                Om[2 * m:, 2 * m:] = eta * J(1)
                mu, Q = np.linalg.eigh(1j * Om)
                x = Q.conj().T @ d
                wiersz.append(0.5 * np.real(x.conj() @ M_niezdeg(Q.conj().T @ Gam @ Q, mu) @ x))
            najgorsza = max(najgorsza, abs(wiersz[-1] - Sfull))
            print(f'  C próba {proba} (δ_K {"= 0" if dK_zero else "≠ 0"}): S_full {Sfull:.6f}, S_czynnik {SF:.6f}; '
                  f'η = 1e-2…1e-5: ' + ' '.join(f'{s:.6f}' for s in wiersz) + f' | różnica przy η = 1e-5: {abs(wiersz[-1] - Sfull):.1e}')
    print(f'C1: max różnica przy η = 1e-5: {najgorsza:.1e} → {"PRZESZŁO" if najgorsza < 1e-4 else "UPADŁO"}; '
          f'C2: raport wyżej (S_full wobec S_czynnik przy δ_K = 0)')


if __name__ == '__main__':
    t0 = time.time()
    F1()
    F2()
    C12()
    print(f'razem {time.time() - t0:.0f} s')
