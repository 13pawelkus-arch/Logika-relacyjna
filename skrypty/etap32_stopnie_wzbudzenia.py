# -*- coding: utf-8 -*-
"""
etap32 — STOPNIE WZBUDZENIA DLA ZNANEGO O (krok 1, poprawka 174) na strukturze
minimalnej (179).  Kontrola do kartki; twierdzenia są na kartce, tu tylko to,
czego kartka nie rozstrzyga: wartość, kontrola negatywna i różnica dwóch miar.

Układ (179): nośnik = kubit na linku, element = relacja dwóch nośników.
Para (M, O): nośnik przelotowy A wchodzi do M linkiem brzegowym, spotyka się
we wnętrzu z nośnikami wewnętrznymi (bez linku do O), wychodzi do O.
Sprzężenie: faza na własne tyknięcie (R1f-3), U = CPHASE.
Ø = nośnik wewnętrzny w stanie podstawowym; zawartość = wzbudzony.

  stopień  D(M,O) = max po przygotowaniach O z  ½‖ρ_O(zawartość) − ρ_O(Ø)‖₁
  (kształt D Englerta z 173, tylko między zawartościami, nie drogami — 174)

Żadnego N, żadnej gęstości, żadnego pojemnika; wszystko dokładne na kilku
kubitach.

CZEGO TU NIE MA, BO JEST TAUTOLOGIĄ (a nie wynikiem):
  „stan O zależy od wnętrza tylko przez kanał Λ” — to jest definicja Λ, skoro
  nośniki wewnętrzne nie mają linku do O.  To samo co „w samym porządku zero
  sprzężenia wnętrza z O jest tautologią” (173).  Nie testuję tautologii.

ZDANIA ZAPISANE PRZED PRZEBIEGIEM (co może upaść i co wtedy wiemy)
------------------------------------------------------------------
Z1  WARTOŚĆ.  D = |sin(Δφ/2)|, Δφ = suma faz na tyknięciach, do 1e-6;
    D wraca do zera i nie przekracza 1 — głębokość wchodzi WYŁĄCZNIE okresowo.
    UPADEK: D rośnie z głębokością, więc „więcej wnętrza = więcej wzbudzenia”.

Z2  KRES NALEŻY DO PARY.  Dowolny kanał wstawiony między M a O (element spoza
    pary) daje D' ≤ D, w 200 losowych próbach.  UPADEK: stopień nie jest
    wielkością pary nawet jako kres górny.

Z3  KONTROLA NEGATYWNA (pułapka 3).  Dwa wnętrza RÓŻNE strukturalnie — jeden
    nośnik wewnętrzny wobec dwóch, inne obsadzenia, inne fazy — dobrane tak,
    żeby dać ten sam kanał Λ: stan O identyczny (≤1e-12), mimo |M| = 1 wobec 2.
    Po złamaniu modułu (element O czyta nośnik wewnętrzny) te same dwa wnętrza
    dają stany O różne (>1e-3).  UPADEK (brak różnicy w drugiej części):
    zdanie nie wyróżnia modułu i nic nie mówi.

Z5  STOPNIE, NIE SAM KRES (poprawka użytkownika do pierwszej wersji wpisu).
    D = ½|c − 1| dokładnie, do 1e-15, dla p ∈ [0,1] i dla iloczynów dwóch
    nośników; dla jednego nośnika D = p·|sin(φ/2)| — liniowo w obsadzeniu.
    |sin(Δφ/2)| to przypadek p = 1, czyli kres.  Sprawdzana jest przy okazji
    postać zaproponowana przez użytkownika, √(1 − |⟨ψ_c|ψ_1⟩|²) ze stanami
    czystymi: ma zawyżać wszędzie poza |c| = 1, bo przy |c| < 1 stan O jest
    mieszany.  UPADEK: D nie jest ½|c − 1|, czyli stopniowanie ma inny kształt.

Z6  ZERO IZOLOWANE, NIE TOŻSAMOŚCIOWE.  W punkcie c = 1 przy p = 1 (φ = 2πk)
    zmiana fazy o ε przywraca D liniowo (D/ε → p/2), więc to NIE jest
    milczenie 174 (tam kanał nie zależy od zawartości i D znika tożsamościowo),
    tylko ≡ Ø dla tego O.  UPADEK: D nie wraca — wtedy to byłoby milczenie.

Z4  DWIE MIARY DAJĄ DWIE RÓŻNE ODPOWIEDZI.  Dla n nośników przechodzących z M
    do O: D nasyca się do 1 i nigdy jej nie przekracza, a entropia względna
    S(ρ_c‖ρ_Ø) rośnie liniowo w n, bez kresu.  UPADEK: obie rosną albo obie
    stoją — wtedy wybór miary nie ma znaczenia i [290] nie rozstrzyga.
"""

import numpy as np

RNG = np.random.default_rng(20260930)
TOL = 1e-12

KET0 = np.array([1, 0], dtype=complex)
KET1 = np.array([0, 1], dtype=complex)
R0 = np.outer(KET0, KET0.conj())
R1 = np.outer(KET1, KET1.conj())


def slad_czesciowy(rho, wymiary, zostaw):
    n = len(wymiary)
    rho = rho.reshape(list(wymiary) + list(wymiary))
    usun = [k for k in range(n) if k not in zostaw]
    wym = list(wymiary)
    for k in sorted(usun, reverse=True):
        rho = np.trace(rho, axis1=k, axis2=k + len(wym))
        wym = wym[:k] + wym[k + 1:]
    d = int(np.prod(wym))
    return rho.reshape(d, d)


def odl_sladowa(a, b):
    return 0.5 * np.abs(np.linalg.eigvalsh(a - b)).sum()


def entropia_wzgledna(rho, sigma):
    """S(rho‖sigma) w bitach, dokładnie: Tr rho log2 rho - Tr rho log2 sigma."""
    wr, Vr = np.linalg.eigh(rho)
    ws, Vs = np.linalg.eigh(sigma)
    wr = np.clip(wr, 0.0, None)
    ws = np.clip(ws, 0.0, None)
    czlon1 = float(sum(a * np.log2(a) for a in wr if a > 0))
    nak = np.abs(Vs.conj().T @ Vr) ** 2          # |<b_j|a_i>|^2, indeks [j, i]
    czlon2 = 0.0
    for i, a in enumerate(wr):
        if a <= 0:
            continue
        for j, b in enumerate(ws):
            if nak[j, i] <= 1e-18:
                continue
            if b <= 0:
                return np.inf
            czlon2 += a * nak[j, i] * np.log2(b)
    return czlon1 - czlon2


# ---------------------------------------------------------------------------
# Kanał modułu: A przechodzi przez wnętrze, nośniki wewnętrzne są śladowane.
# Przy sprzężeniu CPHASE(f) z nośnikiem w stanie o obsadzeniu p kanał na A
# mnoży element pozadiagonalny przez  c = 1 − p + p·e^{−if}.  Kanał zależy od
# wnętrza WYŁĄCZNIE przez iloczyn tych czynników.
# ---------------------------------------------------------------------------

def czynnik(p, f):
    return 1.0 - p + p * np.exp(-1j * f)


def kanal_z_czynnika(c):
    """ρ_A → element pozadiagonalny × c (i sprzężenie)."""
    def Lam(rho_RA):
        d_R = rho_RA.shape[0] // 2
        out = rho_RA.reshape(d_R, 2, d_R, 2).copy()
        out[:, 0, :, 1] *= c
        out[:, 1, :, 0] *= np.conj(c)
        return out.reshape(2 * d_R, 2 * d_R)
    return Lam


def stopien_z_czynnikow(c_c, c_0, prob=6000, po=None, d_R=2):
    Lc, L0 = kanal_z_czynnika(c_c), kanal_z_czynnika(c_0)
    naj = 0.0
    for _ in range(prob):
        v = RNG.normal(size=2 * d_R) + 1j * RNG.normal(size=2 * d_R)
        v /= np.linalg.norm(v)
        rho = np.outer(v, v.conj())
        a, b = Lc(rho), L0(rho)
        if po is not None:
            a, b = po(a), po(b)
        naj = max(naj, odl_sladowa(a, b))
    return naj


# ============================ Z1 — wartość ================================
print("=" * 74)
print("Z1  wartość:  D = |sin(Δφ/2)|,  głębokość wchodzi tylko okresowo")
print("=" * 74)
f = 0.7
print("   d   Δφ = d·f      D (zmierzone)     |sin(Δφ/2)|      różnica")
bledy = []
for d in range(0, 15):
    # zawartość: nośnik wewnętrzny wzbudzony (p = 1) na d tyknięciach
    c_c, c_0 = czynnik(1.0, d * f), czynnik(1.0, 0.0)
    D = stopien_z_czynnikow(c_c, c_0, prob=4000)
    wz = abs(np.sin(d * f / 2))
    bledy.append(abs(D - wz))
    print(f"  {d:2d}   {d*f:8.3f}      {D:.9f}      {wz:.9f}      {abs(D-wz):.2e}")
okres = 2 * np.pi / f
print(f"  pełny obrót po Δφ = 2π, czyli po {okres:.3f} tyknięcia")
ok1 = max(bledy) < 1e-6
print(f"  WERDYKT Z1: {'PRZESZŁO' if ok1 else 'UPADŁO'}  (maks błąd {max(bledy):.2e})")
print("  -> D wraca do zera i nie przekracza 1; głębokość NIE podnosi stopnia.")

# ============================ Z2 — kres pary ==============================
print()
print("=" * 74)
print("Z2  kres należy do pary: nic spoza niej nie podnosi D")
print("=" * 74)
c_c, c_0 = czynnik(1.0, 3 * f), 1.0 + 0j
D_para = stopien_z_czynnikow(c_c, c_0, prob=8000)


def losowy_kanal_1kubit():
    G = RNG.normal(size=(4, 2)) + 1j * RNG.normal(size=(4, 2))
    V, _ = np.linalg.qr(G)

    def E(r):
        return slad_czesciowy(V @ r @ V.conj().T, [2, 2], [0])
    return E


naj_wzrost = -1.0
for _ in range(200):
    E = losowy_kanal_1kubit()

    def po(rho_RA, E=E):
        d_R = rho_RA.shape[0] // 2
        blk = rho_RA.reshape(d_R, 2, d_R, 2)
        out = np.zeros_like(blk)
        for i in range(d_R):
            for j in range(d_R):
                out[i, :, j, :] = E(blk[i, :, j, :])
        return out.reshape(2 * d_R, 2 * d_R)

    naj_wzrost = max(naj_wzrost, stopien_z_czynnikow(c_c, c_0, prob=400, po=po)
                     - D_para)
print(f"  D dla samej pary (3 tyknięcia): {D_para:.9f}")
print(f"  największy wzrost po dołożeniu elementu spoza pary: {naj_wzrost:+.3e}")
ok2 = naj_wzrost < 1e-9
print(f"  WERDYKT Z2: {'PRZESZŁO' if ok2 else 'UPADŁO'}")

# ================= Z3 — kontrola negatywna (czy wyróżnia moduł) ===========
print()
print("=" * 74)
print("Z3  kontrola negatywna: dwa RÓŻNE wnętrza o tym samym kanale")
print("=" * 74)
# wnętrze II: DWA nośniki wewnętrzne, różne obsadzenia i różne fazy
p1, f1, p2, f2 = 0.35, 1.1, 0.8, 0.45
c_II = czynnik(p1, f1) * czynnik(p2, f2)
# wnętrze I: JEDEN nośnik, (p, f) rozwiązane tak, żeby dać ten sam czynnik
#   c = 1 − p(1 − e^{−if});  1 − e^{−if} ma moduł 2 sin(f/2) i argument f/2
u = 1.0 - c_II
theta, r = np.angle(u), abs(u)
f_I = np.pi - 2 * theta          # arg(1 - e^{-if}) = pi/2 - f/2
p_I = r / (2 * np.cos(theta))
c_I = czynnik(p_I, f_I)
print(f"  wnętrze I : 1 nośnik,  p = {p_I:.6f},  f = {f_I:.6f}")
print(f"  wnętrze II: 2 nośniki, (p,f) = ({p1}, {f1}) i ({p2}, {f2})")
print(f"  czynnik kanału:  I = {c_I:.12f}   II = {c_II:.12f}"
      f"   |Δ| = {abs(c_I - c_II):.2e}")

v = RNG.normal(size=4) + 1j * RNG.normal(size=4)
v /= np.linalg.norm(v)
rho_in = np.outer(v, v.conj())
roz_modul = odl_sladowa(kanal_z_czynnika(c_I)(rho_in),
                        kanal_z_czynnika(c_II)(rho_in))


def stan_O_zlamany(wnetrza, rho_RA):
    """Moduł złamany: jeden nośnik wewnętrzny ma link do O, więc nie jest
    śladowany w M — O czyta go wprost (detektor drogi, 173)."""
    d_R = rho_RA.shape[0] // 2
    # pierwszy nośnik wnętrza zostaje; reszta śladowana przez czynnik
    p, f_, c_reszty = wnetrza
    rho_W = (1 - p) * R0 + p * R1
    rho = np.kron(rho_RA, rho_W)
    n = 2 * d_R * 2
    U = np.eye(n, dtype=complex).reshape(d_R, 2, 2, d_R, 2, 2)
    for a in range(2):
        for w in range(2):
            U[:, a, w, :, a, w] = np.eye(d_R) * np.exp(1j * f_ * a * w)
    U = U.reshape(n, n)
    rho = U @ rho @ U.conj().T
    # pozostałe nośniki wnętrza (śladowane) dokładają czynnik na A
    blk = rho.reshape(d_R, 2, 2, d_R, 2, 2)
    blk[:, 0, :, :, 1, :] *= c_reszty
    blk[:, 1, :, :, 0, :] *= np.conj(c_reszty)
    return blk.reshape(n, n)


a_zl = stan_O_zlamany((p_I, f_I, 1.0 + 0j), rho_in)
b_zl = stan_O_zlamany((p1, f1, czynnik(p2, f2)), rho_in)
roz_zlam = odl_sladowa(a_zl, b_zl)
print(f"  moduł zachowany : różnica stanów O = {roz_modul:.2e}   (|M| = 1 wobec 2)")
print(f"  moduł złamany   : różnica stanów O = {roz_zlam:.2e}")
ok3 = roz_modul < 1e-12 and roz_zlam > 1e-3
print(f"  WERDYKT Z3: {'PRZESZŁO' if ok3 else 'UPADŁO'}")
print("  -> nierozróżnialność wnętrz jest własnością MODUŁU, nie sprzężenia.")

# ==================== Z4 — dwie miary, dwie odpowiedzi ====================
print()
print("=" * 74)
print("Z4  D wobec entropii względnej przy n nośnikach z M do O")
print("=" * 74)
# jeden nośnik: stan O dla zawartości i dla Ø, na przygotowaniu (|0>+|1>)/√2
psi = (KET0 + KET1) / np.sqrt(2)
rho1 = np.outer(psi, psi.conj())


def stan_1(c):
    out = rho1.copy()
    out[0, 1] *= c
    out[1, 0] *= np.conj(c)
    return out


c_c1, c_01 = czynnik(1.0, 0.9), 1.0 + 0j
rc, r0_ = stan_1(c_c1), stan_1(c_01)
# Ø jest czysty => entropia względna nieskończona; bierzemy Ø lekko zdekoherowane
rc, r0_ = stan_1(czynnik(1.0, 0.9)), stan_1(0.60 + 0j)
print("   n      D (nasyca się)        S(ρ_c‖ρ_Ø) [bity]")
Dn, Sn = [], []
for n in range(1, 8):
    A = rc.copy()
    B = r0_.copy()
    for _ in range(n - 1):
        A = np.kron(A, rc)
        B = np.kron(B, r0_)
    D = odl_sladowa(A, B)
    S = entropia_wzgledna(A, B)
    Dn.append(D)
    Sn.append(S)
    print(f"  {n:2d}      {D:.9f}           {S:.6f}")
lin = np.polyfit(range(1, 8), Sn, 1)
ok4 = (max(Dn) <= 1.0 + 1e-12) and abs(Sn[-1] - 7 * Sn[0]) < 1e-8
print(f"  S dokładnie liniowe w n: nachylenie {lin[0]:.6f} bit/nośnik,"
      f"  S(7) - 7*S(1) = {Sn[-1] - 7 * Sn[0]:.2e}")
print(f"  WERDYKT Z4: {'PRZESZŁO' if ok4 else 'UPADŁO'}")
print("  -> D jest liczbą (kres 1), entropia względna jest miarą (rośnie z n).")

# ================== Z5 — stopnie: D = ½|c − 1| na całym dysku ==============
print()
print("=" * 74)
print("Z5  stopnie, nie sam kres:  D = ½|c − 1|,  jeden nośnik: D = p·|sin(φ/2)|")
print("=" * 74)
print("    p      φ       D (zmierzone)   ½|c−1|       p·|sin(φ/2)|  wzór ze stanów czystych")
bl5 = []
for pp, ff in [(1.0, 0.7), (1.0, np.pi), (0.5, 0.7), (0.25, 2.0),
               (0.8, 4.0), (0.1, 1.0), (0.0, 1.3)]:
    c = czynnik(pp, ff)
    D = stopien_z_czynnikow(c, 1.0 + 0j, prob=20000)
    wz, gr = 0.5 * abs(c - 1), pp * abs(np.sin(ff / 2))
    ov = abs((1 + np.conj(c)) / (np.sqrt(2) * np.sqrt(1 + abs(c) ** 2)))
    czyste = np.sqrt(max(0.0, 1 - ov ** 2))
    bl5 += [abs(D - wz), abs(D - gr)]
    print(f"  {pp:5.2f}  {ff:6.3f}    {D:.9f}    {wz:.9f}  {gr:.9f}   {czyste:.9f}")
print("  iloczyny dwóch nośników:")
for a, b, cc, dd in [(0.35, 1.1, 0.8, 0.45), (1.0, 2.0, 1.0, 1.5), (0.6, 0.9, 0.3, 2.2)]:
    c = czynnik(a, b) * czynnik(cc, dd)
    D = stopien_z_czynnikow(c, 1.0 + 0j, prob=20000)
    bl5.append(abs(D - 0.5 * abs(c - 1)))
    print(f"    D = {D:.9f}   ½|c−1| = {0.5*abs(c-1):.9f}   różnica {abs(D-0.5*abs(c-1)):.2e}")
ok5 = max(bl5) < 1e-8
print(f"  WERDYKT Z5: {'PRZESZŁO' if ok5 else 'UPADŁO'}  (maks błąd {max(bl5):.2e})")
print("  -> stopniowanie siedzi w obsadzeniu p; wzór ze stanów czystych zawyża,")
print("     bo przy |c| < 1 stan O jest mieszany (przy c = 0 to ½·1, nie |0>).")

# ============== Z6 — zero izolowane, nie tożsamościowe =====================
print()
print("=" * 74)
print("Z6  zero przy Δφ = 2πk jest IZOLOWANE — to ≡ Ø dla tego O, nie milczenie")
print("=" * 74)
pp = 1.0
print("      ε        D(2π + ε)      D/ε        (oczekiwane p/2 = 0,5)")
il = []
for eps in [1e-1, 1e-2, 1e-3, 1e-4]:
    c = czynnik(pp, 2 * np.pi + eps)
    D = 0.5 * abs(c - 1)                      # wzór potwierdzony w Z5
    il.append(D / eps)
    print(f"   {eps:7.0e}    {D:.12f}   {D/eps:.9f}")
# milczenie 174 dla porównania: kanał nie zależy od zawartości
c_milcz_p0, c_milcz_p1 = czynnik(0.0, 1.3), czynnik(0.0, 1.3 + 0.1)
print(f"  milczenie 174 (kanał niezależny od zawartości): D = "
      f"{0.5*abs(c_milcz_p0-1):.1e} i po zaburzeniu fazy {0.5*abs(c_milcz_p1-1):.1e}")
ok6 = abs(il[-1] - pp / 2) < 1e-3 and 0.5 * abs(c_milcz_p1 - 1) < 1e-15
print(f"  WERDYKT Z6: {'PRZESZŁO' if ok6 else 'UPADŁO'}  (D/ε → {il[-1]:.6f})")
print("  -> D wraca liniowo, więc zero jest izolowane: wzbudzony moduł jest")
print("     NIEROZRÓŻNIALNY od Ø dla tego O, a nie milczący (pułapka 9).")

print()
print("=" * 74)
print("PODSUMOWANIE")
for nazwa, ok in [("Z1", ok1), ("Z2", ok2), ("Z3", ok3), ("Z4", ok4),
                  ("Z5", ok5), ("Z6", ok6)]:
    print(f"  {nazwa}: {'PRZESZŁO' if ok else 'UPADŁO'}")
print("=" * 74)
