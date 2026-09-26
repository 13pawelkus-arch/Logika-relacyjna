# etap26 — entropia względna stanu koherentnego wobec stanu SJ na poddiamencie (literaturowe 1+1)
#
# PO CO. A11d (poprawka 169): dosłowne ≡ = entropia względna 0 (Witten §3.3); entropia względna Arakiego jest
# porównaniem dwóch stanów, skończona sama z siebie. Na zbiorach przyczynowych policzono dotąd tylko przypadek
# szczególny — informację wzajemną I(A:B) = S(ρ_AB‖ρ_A⊗ρ_B) (Duffy–Jones–Yazdi 2022). Przypadek ogólny: dwa różne
# stany na tym samym obszarze. Najprostszy: stan koherentny (przesunięcie pola o δ) wobec SJ (propozycja
# użytkownika, 26.09). Wtedy S(ρ_δ‖ρ) = ½ δᵀ h δ DOKŁADNIE (forma kwadratowa jest całą entropią względną,
# wszystkie rzędy); h — forma kwadratowa hamiltonianu modularnego stanu SJ na obszarze, z tego samego zagadnienia
# własnego W v = λ iΔ v co entropia SJ (λ = ½ + ν).
#
# WZÓR (czynnik). Na obrazie iΔ_U: Γ = R_U, X = Γ^{1/2}(iΔ_U)^{-1}Γ^{1/2} (hermitowska, wartości ±ν),
#   S = ½ Σ_s |ν_s| ε(|ν_s|) |⟨y_s, Γ^{-1/2} δ⟩|²,  ε(ν) = ln((ν+½)/(ν−½));  S_EE = Σ_{ν>0}[(ν+½)ln(ν+½) − (ν−½)ln(ν−½)].
#   Sprawdzone niezależnie z macierzy gęstości w bazie Focka (1 mod do 8 cyfr; 2 mody do 1·10⁻⁶).
# WZÓR (pełna algebra obszaru, v2). Jądro iΔ_U = obserwable centralne φ(z), [φ(z), ·] = 0 w U. Gdy W_U z ≠ 0,
#   fluktuują — odrzucenie jądra ogranicza algebrę (Arias–Huerta–Martinez, arXiv:2609.12047, §2: „selecting a
#   nondegenerate subspace amounts to restricting the observable algebra”). Stan = rozkład po centrum × stany
#   warunkowe; reguła łańcuchowa:
#   S_full = ½ δ_K† Γ_KK⁻¹ δ_K + ½ δ̃† h(Γ_c) δ̃,  Γ_c = Γ_II − Γ_IK Γ_KK⁻¹ Γ_KI,  δ̃ = δ_I − Γ_IK Γ_KK⁻¹ δ_K.
#   Sprawdzone (K0): centrum zregularyzowane małym komutatorem η → granica wzoru niezdegenerowanego, różnica ∝ η.
#   W kontinuum jądro iΔ_U na diamencie = □C_c^∞(U), W z = 0 (równanie pola, własność time-slice) — centrum nie ma.
#   Na porządku centrum fluktuuje: udział centrum = miara braku własności time-slice na porządku (por. C4a.2–3).
# SJ: W = ½(|iΔ| + iΔ), R = Re W = ½|iΔ| (z eigh(iΔ) w pełnej precyzji; D = ½(Cᵀ − C), konwencje etap0p).
#
# USTAWIENIE. Sprinkling do diamentu [0,1]² (u, v), ρ = 2N (miara dt dx); U = centralny poddiament V/V_U = 4 (R = 0,25),
# U_mały: V/V_U = 16 (R = 0,125), U_mały ⊂ U. Przesunięcie: fala d = A·P(u)·H(v), P(u) = (u−u₀)/σ·e^{−(u−u₀)²/2σ²}
# (nieparzysta — bez składowej stałej, podczerwień 1+1), H(v) = dystrybuanta źródła w v (v₀ = 0,12, σ_v = 0,03; H = 1 na U),
# u₀ = 0,5, A = 1, σ ∈ {0,06; 0,08; 0,12} (σ = 0,08 — główna, wybrana w v1). Wersja gładka: d(x_i) (rozwiązanie
# kontinuum); wersja dyskretna: d = Δf/ρ, f = 4A·P′(u)·h(v) — rozwiązanie z własnym propagatorem porządku (K_R = ½C),
# źródło poza U. Odniesienie [L]: Casini–Huerta–Myers, JHEP 1105:036 (2011): H = 2π∫(R²−x²)/(2R)·T₀₀ dx (próżnia
# Minkowskiego, CFT); dla stanu koherentnego S = 2π∫(R²−x²)/(2R)·A²P′(½+x)² dx (kanoniczny T₀₀ — Casini–Grillo–Pontello,
# PRD 99, 125020 (2019), klin; w 1+1 bezmasowym kanoniczny = konforemny). SJ w U ≠ Minkowski (U nie leży głęboko:
# Afshordi–Buck–Dowker–Rideout–Sorkin–Yazdi, JHEP 10 (2012) 088) — porównanie rzędu 1, nie ścisłe.
#
# HISTORIA (jawnie). v1: tylko czynnik (jądro odrzucone), zdania v1: Z1 wykładnik S_F na ostatnim podwojeniu
# < 0,10 / > 0,50; Z2 S_F/S_CHM ∈ [0,75; 1,25]; Z3 |dysk/gład − 1| < 0,15; K4 waga przesunięcia w jądrze < 1%.
# Sprawdzenie kodu v1 (N = 500, 1000; 1 ziarno; σ = 0,08): S_F(U) = 4,24 / 4,73 wobec S_CHM = 11,49 (0,37 / 0,41),
# S_F(U_mały) = 2,03 / 2,70 wobec 4,46; K4 = 0,32 / 0,021 — waga w jądrze nie jest mała → metoda zmieniona na pełną
# algebrę (v2). Zdania v2 zapisane po tym sprawdzeniu i przed jakimkolwiek przebiegiem v2.
# Sprawdzenie kodu v2 (N = 500, 1000, 2000; 1 ziarno) — dwa błędy metody, poprawione w v3:
#   (a) N = 1000, gładkie: S_full = 27,7 przy S_F = 4,73 — kierunek zerowy R_U = para BLIŹNIAKÓW z A3a (elementy 200, 610;
#       wektor (e_i − e_j)/√2; R_U-wartość 3,8·10⁻¹⁷ przy pełnej precyzji). Bliźniaki mają identyczne kolumny Δ ⇒
#       Δ(e_i − e_j) = 0 i W(e_i − e_j) = 0 ⇒ φ_i = φ_j w stanie SJ [T]. Przesunięcie próbkowane z kontinuum nadaje
#       bliźniakom różne wartości — nie jest stanem porządku (formalnie S = ∞); 27,7 = artefakt precyzji (√(DᵀD) rozmywa
#       zero do ~10⁻⁸). Rozwiązanie dyskretne Δf ma tę składową 6·10⁻¹⁶. Poprawka: eigh(iΔ) w pełnej precyzji; przesunięcie
#       gładkie rzutowane na obraz iΔ (ker iΔ = dokładne zera, |λ| < 1e-10·max; 8 przy N = 1000, 10 przy N = 2000);
#       w jądrze iΔ_U kierunki z W z = 0 (iloraz, Arias i in.) oddzielone od fluktuujących (centrum).
#   (b) N = 2000, dyskretne: S = 15,8 (4,0 przy N = 1000) — szum Poissona próbkowanego źródła: rms(Δf/ρ − A·P) = 0,55
#       przy rms sygnału 0,39 (oszacowanie wariancji ≈ 156/N dla σ_v = 0,03). Z4 v2 WYCOFANE przed przebiegiem (mierzyłoby
#       szum); wersja dyskretna tylko informacyjnie, szersze źródło (v₀ = 0,10, σ_v = 0,05), rms szumu raportowane.
# Zdania v3 = zdania v2 bez Z4, dla przesunięcia gładkiego rzutowanego (jedyne dopuszczalne); zapisane przed przebiegiem v3.
# Sprawdzenie kodu v3 (po zapisaniu zdań v3): N = 500, 1000, 2000, 4096, po 1 ziarnie — liczby tylko jako kontrola kodu;
# werdykty wyłącznie na przebiegu GPU (więcej ziaren, ≥ 1,2 dekady).
#
# ZDANIA v3 (przed przebiegiem; werdykty na przebiegu GPU, N = 1024 … 16384–24576 wg pamięci — ≥ 1,2 dekady):
# Z1 [główne — „sztuki czy miara”]: S_full (gładkie rzutowane, bez obcięcia, U, σ = 0,08) jest liczbą, nie gęstością:
#     wykładnik d ln S / d ln N między N_max a największym N ≤ N_max/2 < 0,10 → PRZESZŁO; > 0,50 → UPADŁO; pomiędzy →
#     NIEROZSTRZYGNIĘTE. Ta sama klasyfikacja raportowana dla pozostałych σ, U_mały i wersji dyskretnej (bez werdyktu).
#     Kontrola stanu: wykładnik S_EE ≥ 0,9 (prawo objętościowe nieobciętego SJ, A10).
# Z2 [własność time-slice na porządku]: udział centrum u = 1 − S_F/S_full dla przesunięcia gładkiego rzutowanego
#     (U, σ = 0,08) maleje z N: wykładnik u(N) na całym zakresie < −0,2 → PRZESZŁO (centrum znika, porządek odtwarza
#     równość algebr asymptotycznie); |wykładnik| < 0,1 → UPADŁO (centrum niesie stały udział); pomiędzy →
#     NIEROZSTRZYGNIĘTE.
# Z3 [kontinuum, rzędu 1]: S_full(U, σ = 0,08, gładkie, największe N) / S_CHM ∈ [0,75; 1,25]. Upadek nie rozstrzyga
#     między „porządek nie odtwarza kontinuum przy tym N” a „SJ ≠ Minkowski w U” (wyżej).
# (Z4 v2 wycofane — wyżej, (b).)
# K0 wzór z centrum = granica η → 0 wzoru niezdegenerowanego (< 1e-4 przy η = 1e-5); K1 S(2δ) = 4S(δ) (kod);
# K2 S_full(U_mały) ≤ S_full(U) w każdej realizacji (twierdzenie: A(U_mały) ⊂ A(U)); dla S_F tylko raport (brak twierdzenia);
# K3 brak modów niefizycznych (ν < ½) — czynnik i stany warunkowe; K4 składowa przesunięcia rzutowanego w kierunkach
# zerowych R_U < 1e-10 (względnie) — przesunięcie jest stanem porządku.
# Informacyjnie (bez zdania): rozwiązanie dyskretne z próbkowanego źródła (+ rms szumu); podwójne obcięcie SY (c = 1, 2),
# przesunięcie rzutowane na zachowane mody; liczba dokładnych zer iΔ (bliźniaki i inne) i kierunków zerowych W w U.
#
# URUCHOMIENIE. Lokalnie (CPU, sprawdzenie kodu): python3 etap26_entropia_wzgledna.py --szybko
# Colab (GPU): wkleić całość, uruchomić; checkpoint po każdym (N, ziarno) w CKPT; przy braku pamięci N pomijane.
import json, math, os, sys, time
import numpy as np
try:
    import cupy as cp
    XP, GPU = cp, True
except ImportError:
    XP, GPU = np, False

# ===================== PARAMETRY =====================
N_LISTA = [1024, 2048, 4096, 8192, 16384, 20480, 24576]   # 24576: tylko A100 80 GB (bezpiecznik)
ZIARNA = {1024: 4, 2048: 4, 4096: 3, 8192: 3, 16384: 3, 20480: 2, 24576: 2}
SIGMY = [0.06, 0.08, 0.12]
SIGMA_GL = 0.08
U0, V0, SIGV, AMP = 0.5, 0.12, 0.03, 1.0      # fala gładka (H(v) = 1 na obu obszarach)
V0_ZR, SIGV_ZR = 0.10, 0.05                   # źródło rozwiązania dyskretnego (informacyjnie)
REGIONY = {'U': 4.0, 'Um': 16.0}
C_OBC = [1.0, 2.0]
TOL_JADRO = 1e-10                             # zera iΔ i iΔ_U: |λ| < TOL·max|λ|
TOL_ZERO_W = 1e-10                            # kierunek jądra iΔ_U z W z = 0: wartość Γ_KK < TOL·max(Γ)
ZAPAS = 0.85
BAJTY_NA_N2 = 64.0                            # szczyt eigh(iΔ): iΔ + kopia + przestrzeń zheevd (~4 macierze zespolone)
CKPT = 'etap26_wyniki.json'
if '--szybko' in sys.argv:
    N_LISTA, ZIARNA, CKPT = [500, 1000, 2000], {500: 1, 1000: 1, 2000: 1}, 'etap26_szybko.json'
if '--cpu4096' in sys.argv:
    N_LISTA, ZIARNA, CKPT = [512, 1024, 2048, 4096], {512: 2, 1024: 2, 2048: 2, 4096: 2}, 'etap26_cpu.json'
# =====================================================


def zwolnij():
    if GPU:
        cp.get_default_memory_pool().free_all_blocks()


def wolna():
    if not GPU:
        return float('inf')
    zwolnij()
    return float(cp.cuda.runtime.memGetInfo()[0])


def eps(a):
    return XP.log((a + 0.5) / (a - 0.5))


def P_(u, s):
    x = u - U0
    return x / s * np.exp(-x * x / (2 * s * s))


def dP_(u, s):
    x = u - U0
    return (1 - x * x / (s * s)) / s * np.exp(-x * x / (2 * s * s))


def Hv(v, v0=V0, sv=SIGV):
    return 0.5 * (1 + np.vectorize(math.erf)((v - v0) / (math.sqrt(2) * sv)))


def hv(v, v0=V0_ZR, sv=SIGV_ZR):
    return np.exp(-(v - v0) ** 2 / (2 * sv ** 2)) / (math.sqrt(2 * math.pi) * sv)


def chm(R, s):
    x = np.linspace(-R, R, 40001)
    y = (R * R - x * x) / (2 * R) * (AMP * dP_(0.5 + x, s)) ** 2
    return float(2 * math.pi * np.sum((y[1:] + y[:-1]) / 2 * np.diff(x)))


def forma(G, m):
    """h dla (Γ = G, iΩ = diag m) w bazie własnej iΩ; zwraca h, min|ν|, liczbę modów niefizycznych, S_EE."""
    G = (G + G.conj().T) / 2
    g, O = XP.linalg.eigh(G)
    if float(g.min()) <= 0:
        raise ValueError(f'Γ nie jest dodatnio określona: {float(g.min()):.3e}')
    Gh = (O * XP.sqrt(g)) @ O.conj().T
    Gmh = (O / XP.sqrt(g)) @ O.conj().T
    X = Gh @ (Gh / m[:, None])
    X = (X + X.conj().T) / 2
    nu, Y = XP.linalg.eigh(X)
    a = XP.abs(nu)
    niefiz = int((a < 0.5 - 1e-9).sum())
    ae = XP.maximum(a, 0.5 + 1e-12)
    h = Gmh @ (Y * (ae * eps(ae))) @ Y.conj().T @ Gmh
    ap = a[(nu > 0) & (a > 0.5 + 1e-12)]
    see = float(XP.sum((ap + .5) * XP.log(ap + .5) - (ap - .5) * XP.log(ap - .5)))
    return h, float(a.min()), niefiz, see


def modularne(DU, RU):
    """δ ↦ (S_full, S_F, S_cl, waga centrum, składowa zerowa); jądro iΔ_U = zera (W z = 0: iloraz) ⊕ centrum (W z ≠ 0)."""
    mu, Q = XP.linalg.eigh(1j * DU)
    sel = XP.abs(mu) > TOL_JADRO * float(XP.abs(mu).max())
    P, m, Qk = Q[:, sel], mu[sel], Q[:, ~sel]
    GII = P.conj().T @ RU @ P
    skala = float(XP.abs(XP.diag(GII)).max())
    Qz = Qc = None
    if Qk.shape[1]:
        GKK = Qk.conj().T @ RU @ Qk
        gk, Ok = XP.linalg.eigh((GKK + GKK.conj().T) / 2)
        zer = gk < TOL_ZERO_W * skala
        Qz, Qc = Qk @ Ok[:, zer], Qk @ Ok[:, ~zer]
        if Qz.shape[1] == 0:
            Qz = None
        if Qc.shape[1] == 0:
            Qc = None
    k = 0 if Qc is None else int(Qc.shape[1])
    hF, nuF, nfF, see = forma(GII, m)
    diag = dict(NU=int(DU.shape[0]), jadro=int(Qk.shape[1]), zera=0 if Qz is None else int(Qz.shape[1]), k=k,
                nuF=nuF, niefizF=nfF, SEE=see, nuC=nuF, niefizC=nfF, kondK=0.0)
    A = hC = GCC = None
    if k:
        GIC = P.conj().T @ RU @ Qc
        GCC = Qc.conj().T @ RU @ Qc
        GCC = (GCC + GCC.conj().T) / 2
        gc = XP.linalg.eigvalsh(GCC)
        diag['kondK'] = float(gc.min() / gc.max())
        A = XP.linalg.solve(GCC, GIC.conj().T).conj().T
        hC, nuC, nfC, _ = forma(GII - A @ GIC.conj().T, m)
        diag.update(nuC=nuC, niefizC=nfC)

    def S(d):
        d = d.astype(XP.complex128)
        nd = float(XP.linalg.norm(d))
        z0 = 0.0 if Qz is None else float(XP.linalg.norm(Qz.conj().T @ d)) / nd
        dI = P.conj().T @ d
        SF = 0.5 * float(XP.real(dI.conj() @ (hF @ dI)))
        if not k:
            return SF, SF, 0.0, 0.0, z0
        dK = Qc.conj().T @ d
        Scl = 0.5 * float(XP.real(dK.conj() @ XP.linalg.solve(GCC, dK)))
        dt = dI - A @ dK
        return Scl + 0.5 * float(XP.real(dt.conj() @ (hC @ dt))), SF, Scl, float(XP.linalg.norm(dK)) / nd, z0
    return S, diag


def K0():
    """Wzór z centrum wobec granicy η → 0 (centrum zregularyzowane małym komutatorem); losowe układy kwantowo-klasyczne."""
    rng = np.random.default_rng(7)

    def J(n):
        Jm = np.zeros((2 * n, 2 * n))
        for i in range(n):
            Jm[2 * i, 2 * i + 1], Jm[2 * i + 1, 2 * i] = 1, -1
        return Jm
    najg = 0.0
    for proba in range(3):
        H = rng.normal(size=(8, 8))
        H = H + H.T
        lam, Uv = np.linalg.eig(J(4) @ H * 0.3)
        S_ = np.real(Uv @ np.diag(np.exp(lam)) @ np.linalg.inv(Uv))
        Gf = 0.5 * S_ @ S_.T + (0.02 + 0.05 * proba) * np.eye(8)
        idx = [0, 1, 2, 3, 4, 6]                         # 2 mody kwantowe + 2 położenia (centrum)
        Gam = Gf[np.ix_(idx, idx)]
        Om0 = np.zeros((6, 6))
        Om0[:4, :4] = J(2)
        d = rng.normal(size=6)
        f, _ = modularne(XP.asarray(Om0), XP.asarray(Gam))
        Sf = f(XP.asarray(d))[0]
        Om = Om0.copy()
        Om[4, 5], Om[5, 4] = 1e-5, -1e-5
        mu, Q = np.linalg.eigh(1j * Om)
        h, _, _, _ = forma(XP.asarray(Q.conj().T @ Gam @ Q), XP.asarray(mu))
        x = XP.asarray(Q.conj().T @ d)
        Sreg = 0.5 * float(XP.real(x.conj() @ (h @ x)))
        najg = max(najg, abs(Sreg - Sf) / Sf)
    return najg


def jeden(N, ziarno, log):
    t0 = time.time()
    rng = np.random.default_rng(ziarno)
    u, v = rng.random(N), rng.random(N)
    ug, vg = XP.asarray(u), XP.asarray(v)
    C = (ug[:, None] < ug[None, :]) & (vg[:, None] < vg[None, :])
    D = C.T.astype(XP.float64)
    D -= C
    D *= 0.5
    del C
    ids = {}
    for r, q in REGIONY.items():
        h = 0.5 * (1 - 1 / math.sqrt(q))
        ids[r] = XP.asarray(np.where((u > h) & (u < 1 - h) & (v > h) & (v < 1 - h))[0])
    DU = {r: D[i][:, i] for r, i in ids.items()}
    przes, szum = {}, {}
    for s in SIGMY:
        przes[('gl', s)] = XP.asarray(AMP * P_(u, s) * Hv(v))
        przes[('dy', s)] = D @ XP.asarray(4 * AMP * dP_(u, s) * hv(v)) / (2 * N)
        iU = ids['U']
        szum[s] = float(XP.sqrt(XP.mean((przes[('dy', s)][iU] - XP.asarray(AMP * P_(u, s))[iU]) ** 2)) /
                        XP.sqrt(XP.mean(XP.asarray(AMP * P_(u, s))[iU] ** 2)))
    iD = 1j * D
    del D
    zwolnij()
    lam, V = XP.linalg.eigh(iD)                          # pełna precyzja małych |λ| (DᵀD rozmywa zera do ~1e-8)
    del iD
    zwolnij()
    a = XP.abs(lam)
    zero = a < TOL_JADRO * float(a.max())
    V0v = V[:, zero]
    wyn = {'czas_eigh': time.time() - t0, 'zera_globalnie': int(zero.sum())}
    for s in SIGMY:                                      # przesunięcie gładkie rzutowane na obraz iΔ (stan porządku)
        d = przes[('gl', s)]
        przes[('gp', s)] = XP.real(d - V0v @ (V0v.conj().T @ d.astype(XP.complex128)))
        wyn[f'zerowa_gl{s}'] = float(XP.linalg.norm(d - przes[('gp', s)]) / XP.linalg.norm(d))
    for r, i in ids.items():
        VU = V[i]
        RU = XP.real(0.5 * (VU * a) @ VU.conj().T)
        S, dg = modularne(DU[r], RU)
        for (typ, sg), d in przes.items():
            if typ == 'gl':
                continue
            dUr = d[i]
            Sfull, SF, Scl, wK, z0 = S(dUr)
            S2 = S(2 * dUr)[0]
            dg[f'{typ}{sg}'] = dict(Sfull=Sfull, SF=SF, Scl=Scl, wK=wK, z0=z0, K1=abs(S2 - 4 * Sfull) / Sfull)
        for c in C_OBC:                                  # informacyjnie: podwójne obcięcie SY
            keep = a > c * math.sqrt(N) / (4 * math.pi)
            Vk, VUk, lk = V[:, keep], VU[:, keep], lam[keep]
            DUt = -1j * (VUk * lk) @ VUk.conj().T
            RUt = 0.5 * (VUk * XP.abs(lk)) @ VUk.conj().T
            mu, Q = XP.linalg.eigh(1j * DUt)
            zach = XP.abs(mu) > c * math.sqrt(int(len(i))) / (4 * math.pi)
            if int(zach.sum()) == 0:
                dg[f'obc{c}'] = None
                continue
            Qs, ms = Q[:, zach], mu[zach]
            h, nu, nf, see = forma(Qs.conj().T @ RUt @ Qs, ms)
            e = {}
            for (typ, sg), d in przes.items():
                if typ == 'gl':
                    continue
                xi = Qs.conj().T @ (Vk @ (Vk.conj().T @ d.astype(XP.complex128)))[i]
                e[f'{typ}{sg}'] = 0.5 * float(XP.real(xi.conj() @ (h @ xi)))
            dg[f'obc{c}'] = dict(SEE=see, nu=nu, niefiz=nf, zach=int(zach.sum()), S=e)
        wyn[r] = dg
    wyn['szum_dy'] = szum
    del V, lam, a
    zwolnij()
    wyn['czas'] = time.time() - t0
    log(f'  N={N} ziarno={ziarno}: {wyn["czas"]:.0f} s (eigh {wyn["czas_eigh"]:.0f} s); zera iΔ {wyn["zera_globalnie"]}; '
        f'N_U={wyn["U"]["NU"]}: jądro {wyn["U"]["jadro"]} (zera W {wyn["U"]["zera"]}, centrum {wyn["U"]["k"]}); '
        f'U_mały: jądro {wyn["Um"]["jadro"]} (zera W {wyn["Um"]["zera"]}, centrum {wyn["Um"]["k"]})')
    return wyn


def srednia(res, N, r, klucz, pole):
    x = [res[f'{N}|{z}'][r][klucz][pole] for z in range(1, ZIARNA[N] + 1) if f'{N}|{z}' in res]
    return (float(np.mean(x)), float(np.std(x, ddof=1) / math.sqrt(len(x))) if len(x) > 1 else 0.0, len(x)) if x else None


def raport(res, log):
    Ns = [N for N in N_LISTA if any(f'{N}|{z}' in res for z in range(1, ZIARNA[N] + 1))]
    if not Ns:
        return
    ch = {(r, s): chm(0.5 / math.sqrt(q), s) for r, q in REGIONY.items() for s in SIGMY}
    log('\n=== RAPORT (średnie po ziarnach ± błąd średniej; F = sam czynnik) ===')
    log('CHM (Minkowski): ' + ', '.join(f'{r} σ={s}: {v:.3f}' for (r, s), v in ch.items()))
    for r in REGIONY:
        for typ in ('gp', 'dy'):
            for s in SIGMY:
                k = f'{typ}{s}'
                wiersz = []
                for N in Ns:
                    a = srednia(res, N, r, k, 'Sfull')
                    b = srednia(res, N, r, k, 'SF')
                    wiersz.append(f'{N}: {a[0]:.3f}±{a[1]:.3f} (F {b[0]:.3f})')
                log(f'{r} {typ} σ={s}: ' + ' | '.join(wiersz))
    for r in REGIONY:
        log(f'S_full/S_CHM ({r}, gp): ' + ' | '.join(
            f'σ={s}: ' + ' '.join(f'{srednia(res, N, r, f"gp{s}", "Sfull")[0] / ch[(r, s)]:.3f}' for N in Ns) for s in SIGMY))
    lN = np.log(np.array(Ns, float))

    def wyk(y):
        return np.diff(np.log(np.array(y, float))) / np.diff(lN)
    Nm = Ns[-1]
    polowa = [N for N in Ns if N <= Nm / 2]
    if polowa:
        Np = polowa[-1]
        see = [np.mean([res[f'{N}|{z}']['U']['SEE'] for z in range(1, ZIARNA[N] + 1) if f'{N}|{z}' in res]) for N in Ns]
        S1 = [srednia(res, N, 'U', f'gp{SIGMA_GL}', 'Sfull')[0] for N in Ns]
        w1 = math.log(S1[-1] / S1[Ns.index(Np)]) / math.log(Nm / Np)
        log(f'\nwykładniki lokalne S_full(U, gp, σ={SIGMA_GL}): {np.round(wyk(S1), 3)} | S_EE(U): {np.round(wyk(see), 3)}')
        v1 = 'PRZESZŁO' if w1 < 0.10 else ('UPADŁO' if w1 > 0.50 else 'NIEROZSTRZYGNIĘTE')
        log(f'Z1: wykładnik {Np}→{Nm}: {w1:+.3f} → {v1}; kontrola S_EE: {np.mean(wyk(see)):.2f} (≥ 0,9)')
        for r in REGIONY:
            for typ in ('gp', 'dy'):
                for s in SIGMY:
                    y = [srednia(res, N, r, f'{typ}{s}', 'Sfull')[0] for N in Ns]
                    log(f'   (raport) {r} {typ} σ={s}: wykładniki {np.round(wyk(y), 3)}')
        uz = [1 - srednia(res, N, 'U', f'gp{SIGMA_GL}', 'SF')[0] / srednia(res, N, 'U', f'gp{SIGMA_GL}', 'Sfull')[0] for N in Ns]
        wu = np.polyfit(lN, np.log(np.maximum(uz, 1e-300)), 1)[0]
        v2 = 'PRZESZŁO' if wu < -0.2 else ('UPADŁO' if abs(wu) < 0.1 else 'NIEROZSTRZYGNIĘTE')
        log(f'Z2: udział centrum (gp, U) {np.round(uz, 5)}; wykładnik {wu:+.3f} → {v2}')
    S3 = srednia(res, Nm, 'U', f'gp{SIGMA_GL}', 'Sfull')[0] / ch[('U', SIGMA_GL)]
    S3m = srednia(res, Nm, 'Um', f'gp{SIGMA_GL}', 'Sfull')[0] / ch[('Um', SIGMA_GL)]
    log(f'Z3: S_full/S_CHM (U, σ={SIGMA_GL}, N={Nm}) = {S3:.3f} → {"PRZESZŁO" if 0.75 <= S3 <= 1.25 else "UPADŁO"}'
        f'; (raport) U_mały: {S3m:.3f}; pozostałe σ (U): ' +
        ', '.join(f'{s}: {srednia(res, Nm, "U", f"gp{s}", "Sfull")[0] / ch[("U", s)]:.3f}' for s in SIGMY))
    przeb = [k for k in res if '|' in k]
    typy = [f'{t}{s}' for t in ('gp', 'dy') for s in SIGMY]
    k1 = max(res[k][r][t]['K1'] for k in przeb for r in REGIONY for t in typy)
    k2 = [(k, t) for k in przeb for t in typy if res[k]['Um'][t]['Sfull'] > res[k]['U'][t]['Sfull'] * (1 + 1e-9)]
    k2F = [(k, t) for k in przeb for t in typy if res[k]['Um'][t]['SF'] > res[k]['U'][t]['SF'] * (1 + 1e-9)]
    k3 = sum(res[k][r]['niefizF'] + res[k][r]['niefizC'] for k in przeb for r in REGIONY)
    k4 = max(res[k][r][t]['z0'] for k in przeb for r in REGIONY for t in typy)
    log(f'K0 (wzór z centrum): {res.get("K0", float("nan")):.1e}; K1: {k1:.0e}; K2 (S_full): '
        f'{"tak" if not k2 else "NIE " + str(k2[:3])}; K2 dla S_F (raport): {len(k2F)} naruszeń z {len(przeb) * len(typy)}; '
        f'K3 niefizyczne: {k3}; K4 max składowa zerowa (rzutowane i dyskretne): {k4:.1e}')
    for N in Ns:
        z = [res[f'{N}|{zz}'] for zz in range(1, ZIARNA[N] + 1) if f'{N}|{zz}' in res]
        log(f'   N={N}: zera iΔ {np.mean([w["zera_globalnie"] for w in z]):.1f}; składowa zerowa gładkiego (przed rzutem) '
            f'{max(w[f"zerowa_gl{SIGMA_GL}"] for w in z):.1e}; U: jądro {np.mean([w["U"]["jadro"] for w in z]):.1f} '
            f'(zera W {np.mean([w["U"]["zera"] for w in z]):.1f}, centrum {np.mean([w["U"]["k"] for w in z]):.1f}) / '
            f'N_U {np.mean([w["U"]["NU"] for w in z]):.0f}; min ν czynnik {min(w["U"]["nuF"] for w in z):.4f}, '
            f'warunkowo {min(w["U"]["nuC"] for w in z):.4f}; kond(Γ_centrum) {min(w["U"]["kondK"] for w in z):.1e}; '
            f'S_EE(U) {np.mean([w["U"]["SEE"] for w in z]):.1f}; szum dysk./sygnał (σ={SIGMA_GL}) '
            f'{np.mean([w["szum_dy"][str(SIGMA_GL)] if str(SIGMA_GL) in w["szum_dy"] else w["szum_dy"][SIGMA_GL] for w in z]):.2f}')
        for c in C_OBC:
            ob = [w['U'][f'obc{c}'] for w in z if w['U'].get(f'obc{c}')]
            if ob:
                log(f'      obcięcie c={c}: S_EE {np.mean([o["SEE"] for o in ob]):.3f}, S(gp σ={SIGMA_GL}) '
                    f'{np.mean([o["S"][f"gp{SIGMA_GL}"] for o in ob]):.3f}, niefiz {sum(o["niefiz"] for o in ob)}, '
                    f'zach. {np.mean([o["zach"] for o in ob]):.0f}')


def main():
    plik_log = open(CKPT.replace('.json', '.log'), 'a', encoding='utf-8')

    def log(s):
        print(s, flush=True)
        plik_log.write(s + '\n')
        plik_log.flush()
    res = json.load(open(CKPT)) if os.path.exists(CKPT) else {}
    log(f'etap26 v3 — {"GPU" if GPU else "CPU"}; checkpoint: {len([k for k in res if "|" in k])} przebiegów')
    if 'K0' not in res:
        res['K0'] = K0()
        log(f'K0: wzór z centrum vs granica η→0: {res["K0"]:.1e} (< 1e-4)')
    for N in N_LISTA:
        potrzeba = BAJTY_NA_N2 * N * N
        if potrzeba > ZAPAS * wolna():
            log(f'N={N}: POMINIĘTE — szczyt {potrzeba / 1e9:.1f} GB > {ZAPAS:.0%} wolnej ({wolna() / 1e9:.1f} GB)')
            continue
        for z in range(1, ZIARNA[N] + 1):
            k = f'{N}|{z}'
            if k in res:
                continue
            try:
                res[k] = jeden(N, z, log)
            except Exception as e:                                # np. brak pamięci przy nietypowym stanie puli
                log(f'N={N} ziarno={z}: BŁĄD {type(e).__name__}: {e}')
                zwolnij()
                break
            json.dump(res, open(CKPT, 'w'))
    raport(res, log)


if __name__ == '__main__':
    main()
