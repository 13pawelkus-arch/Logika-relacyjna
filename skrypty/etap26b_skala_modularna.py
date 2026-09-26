# etap26b — co steruje wzrostem S(N) w etap26: test mechanizmu (literaturowe 1+1, stan SJ, stany koherentne)
#
# SKĄD. etap26 (GPU, N = 1024…20480): entropia względna S(ρ_δ‖ρ_SJ) fali A·P(u) na poddiamencie prawie nie zależy od
# obcięcia (7,68 / 7,43 / 7,47 przy entropii splątania 1652 / 2,51 / 1,63), centrum algebry znika (N^−0,80), ale Z1
# nierozstrzygnięte (+0,123): dla ostrych impulsów przyrost na podwojenie N stały (S ∝ ln N), dla gładkich maleje.
# PO FAKCIE (etap26, jawnie): tempo wzrostu porządkuje się według πR/σ (ostrość impulsu względem obszaru, bez zmiany
# przy dylatacji): 13,1 → 0,67; 9,8 → 0,60; 6,5 → 0,45 i 0,40 (para o tym samym πR/σ); 4,9 → 0,28; 3,3 → 0,13.
# Rozpoznanie (CPU, N ≤ 4096, hipotezy zapisane przed): wzrost niosą mody prawie czyste (2% najcięższych: 71–87% S
# i cały przyrost); filtr przesunięcia do modów ciągłych go nie usuwa (H_UV odrzucona); mody przy brzegu U ≈ 0
# (H_brzeg odrzucona). Odczyt [O][?]: w kontinuum impuls ma energię modularną ~2πβk ≈ πR/σ; stan SJ obcięty do U na
# porządku ma pułap widma modularnego ε_max = 6,0 → 8,1 (N = 1024 → 20480; ~0,5 na podwojenie); poniżej pułapu S się
# ustala, powyżej rośnie razem z nim (R5: skończony porządek = algebra typu I, widmo modularne ograniczone od góry).
# Ten skrypt sprawdza ten odczyt na NOWYCH impulsach; zdania zapisane przed przebiegiem.
#
# METODA (jak etap26 v3). SJ: W = ½(|iΔ| + iΔ), eigh(iΔ) w pełnej precyzji; przesunięcie gładkie rzutowane na obraz iΔ
# (bliźniaki z A3a = dokładne zera iΔ, φ_i = φ_j w stanie SJ); pełna algebra obszaru: centrum (jądro iΔ_U z W z ≠ 0)
# klasycznie + stany warunkowe; kierunki z W z = 0 w ilorazie. S = ½ δᵀhδ dokładnie. Rozkład S_F (czynnik) na mody
# Williamsona s: wkład ½ w_s |⟨y_s, Γ^{-1/2}δ⟩|², w_s = ν_s ε_s, ε_s = ln((ν_s+½)/(ν_s−½)) — energia modularna modu.
# Obszary: U (V/V_U = 4, R = 0,25), U_mały (V/V_U = 16, R = 0,125); fala d = A·P(u)·H(v), P(u) = (u−u₀)/σ·e^{−(u−u₀)²/2σ²}.
#
# NOWE IMPULSY (w etap26 ich nie było): U: σ = 0,04; 0,16; 0,24 (πR/σ = 19,6; 4,9; 3,3); U_mały: σ = 0,03; 0,04; 0,24
# (13,1; 9,8; 1,6). Stare: U 0,06; 0,08; 0,12; U_mały 0,06; 0,08; 0,12 — podane dla porządku, werdykty T1–T2 na nowych.
#
# ZDANIA (przed przebiegiem):
# T1 [dylatacja]: pary o tym samym πR/σ i tym samym N_U — (U, σ, N) oraz (U_mały, σ/2, 4N) — mają równe przyrosty S na
#     podwojenie N na trzech odcinkach (U: 1024→2048→4096→5120; U_mały: 4096→8192→16384→20480). Pary nowe:
#     (U 0,16 | U_mały 0,08), (U 0,24 | U_mały 0,12), (U_mały 0,03 | U 0,06), (U_mały 0,04 | U 0,08).
#     z = różnica przyrostów / błąd; błąd średniej z wariancji ziaren łączonej po N dla danego (obszar, σ).
#     PRZESZŁO: |z| ≤ 2 na wszystkich 12 odcinkach; UPADŁO: |z| > 3 na którymś odcinku w ≥ 2 z 4 par; inaczej NIEROZSTRZYGNIĘTE.
# T2 [mechanizm]: przyrost późny L = [S(20480) − S(8192)] / log₂2,5 (na podwojenie):
#     (a) L < 0,15 dla πR/σ ≤ 3,3 (nowe: U 0,24; U_mały 0,24);
#     (b) L > 0,5 dla πR/σ ≥ 9,8 (nowe: U 0,04; U_mały 0,03; U_mały 0,04);
#     (c) korelacja rang Spearmana (πR/σ, L) po wszystkich 12 przypadkach ≥ 0,9.
#     PRZESZŁO: (a), (b) i (c); UPADŁO: naruszenie (a) lub (b) o > 2 błędy albo ρ < 0,7; inaczej NIEROZSTRZYGNIĘTE.
# T3 [mody prawie czyste]: dla πR/σ ≥ 6,5 przy N = 20480 2% modów o największej wadze niesie ≥ 70% S_F i ≥ 80% przyrostu S_F
#     na odcinku 8192→20480. PRZESZŁO: wszystkie progi; UPADŁO: którykolwiek udział < 50%; inaczej NIEROZSTRZYGNIĘTE.
# KONTROLE: K0 wzór z centrum = granica η → 0 (< 1e-4); K2 S_full(U_mały) ≤ S_full(U) dla wspólnych σ w każdej realizacji
# (twierdzenie: A(U_mały) ⊂ A(U)); K3 brak modów niefizycznych; K4 składowe zerowe przesunięć < 1e-10 (względnie);
# K5 odtworzenie etap26: średnie S_full(U, σ = 0,08) po tych samych ziarnach = wartości z etap26_wyniki.log (± 0,002).
# RAPORT bez zdania: pułap ε_max(obszar, N); średnia energia modularna ważona wkładem; rozkład wkładów w ε; S/S_CHM.
#
# URUCHOMIENIE. Lokalnie (CPU, sprawdzenie kodu): python3 etap26b_skala_modularna.py --szybko
# Colab (A100 40 GB): wkleić całość, uruchomić; checkpoint po każdym (N, ziarno) w CKPT; przy braku pamięci N pomijane.
import json, math, os, sys, time
import numpy as np
try:
    import cupy as cp
    XP, GPU = cp, True
except ImportError:
    XP, GPU = np, False

# ===================== PARAMETRY =====================
N_LISTA = [1024, 2048, 4096, 5120, 8192, 16384, 20480]
ZIARNA = {1024: 6, 2048: 6, 4096: 6, 5120: 6, 8192: 6, 16384: 4, 20480: 4}
SIGMY = {'U': [0.04, 0.06, 0.08, 0.12, 0.16, 0.24], 'Um': [0.03, 0.04, 0.06, 0.08, 0.12, 0.24]}
NOWE = [('U', 0.04), ('U', 0.16), ('U', 0.24), ('Um', 0.03), ('Um', 0.04), ('Um', 0.24)]
PARY = [(('U', 0.16), ('Um', 0.08)), (('U', 0.24), ('Um', 0.12)), (('U', 0.06), ('Um', 0.03)), (('U', 0.08), ('Um', 0.04))]
PARA_STARA = (('U', 0.12), ('Um', 0.06))
N_PARY = [1024, 2048, 4096, 5120]                     # U przy N, U_mały przy 4N
U0, V0, SIGV, AMP = 0.5, 0.12, 0.03, 1.0
REGIONY = {'U': 4.0, 'Um': 16.0}
TOL_JADRO = 1e-10
TOL_ZERO_W = 1e-10
UDZIAL_CIEZKICH = 0.02
KOSZ, NKOSZ = 0.25, 48                                # koszyki energii modularnej ε: [0, 12)
ZAPAS = 0.85
BAJTY_NA_N2 = 64.0
CKPT = 'etap26b_wyniki.json'
ETAP26_U008 = {1024: (4, 4.949), 2048: (4, 5.687), 4096: (3, 6.259), 8192: (3, 6.854), 16384: (3, 7.497), 20480: (2, 7.675)}
if '--szybko' in sys.argv:
    N_LISTA, ZIARNA, CKPT = [512, 1024, 2048], {512: 2, 1024: 2, 2048: 2}, 'etap26b_szybko.json'
# =====================================================
WSZYSTKIE_S = sorted(set(SIGMY['U']) | set(SIGMY['Um']))


def zwolnij():
    if GPU:
        cp.get_default_memory_pool().free_all_blocks()


def wolna():
    if not GPU:
        return float('inf')
    zwolnij()
    return float(cp.cuda.runtime.memGetInfo()[0])


def P_(u, s):
    x = u - U0
    return x / s * np.exp(-x * x / (2 * s * s))


def dP_(u, s):
    x = u - U0
    return (1 - x * x / (s * s)) / s * np.exp(-x * x / (2 * s * s))


def Hv(v):
    return 0.5 * (1 + np.vectorize(math.erf)((v - V0) / (math.sqrt(2) * SIGV)))


def chm(R, s):
    x = np.linspace(-R, R, 40001)
    y = (R * R - x * x) / (2 * R) * (AMP * dP_(0.5 + x, s)) ** 2
    return float(2 * math.pi * np.sum((y[1:] + y[:-1]) / 2 * np.diff(x)))


def forma(G, m):
    """(Γ = G, iΩ = diag m) w bazie własnej iΩ → h, min|ν|, liczba niefizycznych, S_EE, (Y, Γ^{-1/2}, w, ε)."""
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
    ep = XP.log((ae + 0.5) / (ae - 0.5))
    w = ae * ep
    h = Gmh @ (Y * w) @ Y.conj().T @ Gmh
    ap = a[(nu > 0) & (a > 0.5 + 1e-12)]
    see = float(XP.sum((ap + .5) * XP.log(ap + .5) - (ap - .5) * XP.log(ap - .5)))
    return h, float(a.min()), niefiz, see, (Y, Gmh, w, ep)


def modularne(DU, RU):
    """δ ↦ wynik (S_full, S_F, rozkład S_F na mody); jądro iΔ_U = zera (W z = 0: iloraz) ⊕ centrum (W z ≠ 0)."""
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
        Qz = None if Qz.shape[1] == 0 else Qz
        Qc = None if Qc.shape[1] == 0 else Qc
    k = 0 if Qc is None else int(Qc.shape[1])
    hF, nuF, nfF, see, (Y, Gmh, w, ep) = forma(GII, m)
    kk = max(1, int(round(UDZIAL_CIEZKICH * int(w.shape[0]))))
    prog = XP.sort(w)[-kk]
    ciezkie = w >= prog
    ik = XP.clip(XP.floor(ep / KOSZ).astype(XP.int64), 0, NKOSZ - 1)
    diag = dict(NU=int(DU.shape[0]), jadro=int(Qk.shape[1]), zera=0 if Qz is None else int(Qz.shape[1]), k=k,
                nuF=nuF, niefizF=nfF, SEE=see, nuC=nuF, niefizC=nfF,
                eps_max=float(XP.log((nuF + 0.5) / (nuF - 0.5))) if nuF > 0.5 + 1e-12 else float('inf'),
                mody_kosze=[int(x) for x in XP.bincount(ik, minlength=NKOSZ)[:NKOSZ]])
    A = hC = GCC = None
    if k:
        GIC = P.conj().T @ RU @ Qc
        GCC = Qc.conj().T @ RU @ Qc
        GCC = (GCC + GCC.conj().T) / 2
        A = XP.linalg.solve(GCC, GIC.conj().T).conj().T
        hC, nuC, nfC, _, _ = forma(GII - A @ GIC.conj().T, m)
        diag.update(nuC=nuC, niefizC=nfC)

    def S(d):
        d = d.astype(XP.complex128)
        nd = float(XP.linalg.norm(d))
        z0 = 0.0 if Qz is None else float(XP.linalg.norm(Qz.conj().T @ d)) / nd
        dI = P.conj().T @ d
        c = Y.conj().T @ (Gmh @ dI)
        wkl = 0.5 * w * XP.abs(c) ** 2
        SF = float(wkl.sum())
        wyn = dict(SF=SF, z0=z0, ciezkie=float(wkl[ciezkie].sum()),
                   eps_sr=float((ep * wkl).sum() / wkl.sum()),
                   kosze=[float(x) for x in XP.bincount(ik, weights=wkl, minlength=NKOSZ)[:NKOSZ]])
        if not k:
            wyn['Sfull'] = SF
            return wyn
        dK = Qc.conj().T @ d
        Scl = 0.5 * float(XP.real(dK.conj() @ XP.linalg.solve(GCC, dK)))
        dt = dI - A @ dK
        wyn['Sfull'] = Scl + 0.5 * float(XP.real(dt.conj() @ (hC @ dt)))
        return wyn
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
        idx = [0, 1, 2, 3, 4, 6]
        Gam = Gf[np.ix_(idx, idx)]
        Om0 = np.zeros((6, 6))
        Om0[:4, :4] = J(2)
        d = rng.normal(size=6)
        f, _ = modularne(XP.asarray(Om0), XP.asarray(Gam))
        Sf = f(XP.asarray(d))['Sfull']
        Om = Om0.copy()
        Om[4, 5], Om[5, 4] = 1e-5, -1e-5
        mu, Q = np.linalg.eigh(1j * Om)
        h, _, _, _, _ = forma(XP.asarray(Q.conj().T @ Gam @ Q), XP.asarray(mu))
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
    iD = 1j * D
    del D
    zwolnij()
    lam, V = XP.linalg.eigh(iD)
    del iD
    zwolnij()
    a = XP.abs(lam)
    V0v = V[:, a < TOL_JADRO * float(a.max())]
    wyn = {'czas_eigh': time.time() - t0, 'zera_globalnie': int(V0v.shape[1])}
    przes = {}
    for s in WSZYSTKIE_S:                                 # przesunięcie gładkie rzutowane na obraz iΔ (stan porządku)
        d = XP.asarray(AMP * P_(u, s) * Hv(v))
        przes[s] = XP.real(d - V0v @ (V0v.conj().T @ d.astype(XP.complex128)))
    for r, i in ids.items():
        VU = V[i]
        RU = XP.real(0.5 * (VU * a) @ VU.conj().T)
        S, dg = modularne(DU[r], RU)
        for s in SIGMY[r]:
            dg[f'{s}'] = S(przes[s][i])
        wyn[r] = dg
    del V, lam, a
    zwolnij()
    wyn['czas'] = time.time() - t0
    log(f'  N={N} ziarno={ziarno}: {wyn["czas"]:.0f} s (eigh {wyn["czas_eigh"]:.0f} s); zera iΔ {wyn["zera_globalnie"]}; '
        f'N_U={wyn["U"]["NU"]} (ε_max {wyn["U"]["eps_max"]:.2f}), U_mały {wyn["Um"]["NU"]} (ε_max {wyn["Um"]["eps_max"]:.2f})')
    return wyn


# ------------------------------- raport -------------------------------
def dane(res, r, s, pole='Sfull'):
    """{N: lista wartości po ziarnach}"""
    out = {}
    for N in N_LISTA:
        x = [res[f'{N}|{z}'][r][f'{s}'][pole] for z in range(1, ZIARNA[N] + 1) if f'{N}|{z}' in res]
        if x:
            out[N] = x
    return out


def srednie(res, r, s, pole='Sfull'):
    """{N: (średnia, błąd)} — błąd z wariancji ziaren łączonej po N (zapisane w zdaniach)."""
    dd = dane(res, r, s, pole)
    war = [np.var(x, ddof=1) for x in dd.values() if len(x) > 1]
    s2 = float(np.mean(war)) if war else 0.0
    return {N: (float(np.mean(x)), math.sqrt(s2 / len(x))) for N, x in dd.items()}


def przyrosty(sr, Ns):
    """przyrosty na podwojenie na kolejnych odcinkach Ns: [(wartość, błąd)]"""
    out = []
    for n1, n2 in zip(Ns[:-1], Ns[1:]):
        if n1 in sr and n2 in sr:
            d = math.log2(n2 / n1)
            out.append(((sr[n2][0] - sr[n1][0]) / d, math.hypot(sr[n1][1], sr[n2][1]) / d))
        else:
            out.append(None)
    return out


def rangi(x):
    o = np.argsort(x)
    r = np.empty(len(x))
    r[o] = np.arange(len(x))
    return r


def raport(res, log):
    Ns = [N for N in N_LISTA if any(f'{N}|{z}' in res for z in range(1, ZIARNA[N] + 1))]
    if not Ns:
        return
    R = {r: 0.5 / math.sqrt(q) for r, q in REGIONY.items()}
    przyp = [(r, s) for r in REGIONY for s in SIGMY[r]]
    pr = {(r, s): math.pi * R[r] / s for r, s in przyp}
    log('\n=== RAPORT etap26b (średnie po ziarnach ± błąd z wariancji łączonej) ===')
    for r, s in sorted(przyp, key=lambda k: -pr[k]):
        sr = srednie(res, r, s)
        ch = chm(R[r], s)
        nowy = ' [NOWY]' if (r, s) in NOWE else ''
        log(f'{r:2s} σ={s:<5} πR/σ={pr[(r, s)]:5.1f}{nowy}: ' + ' | '.join(f'{N}: {m:.3f}±{e:.3f}' for N, (m, e) in sr.items())
            + f'  | S_CHM {ch:.3f}, S/S_CHM przy {Ns[-1]}: {sr[Ns[-1]][0] / ch:.3f}')
    # K5
    sr = srednie(res, 'U', 0.08)
    k5 = []
    for N, (nz, stara) in ETAP26_U008.items():
        x = dane(res, 'U', 0.08).get(N, [])
        if len(x) >= nz:
            k5.append(abs(float(np.mean(x[:nz])) - stara))
    log(f'\nK5 (odtworzenie etap26, U σ=0,08, te same ziarna): max |różnica| = '
        f'{max(k5) if k5 else float("nan"):.4f} (< 0,002) na {len(k5)} punktach')
    # T1
    log('\nT1 (dylatacja): przyrosty na podwojenie, U przy N ∈ 1024→2048→4096→5120, U_mały przy 4N')
    zle3 = 0
    wszystkie_ok = True
    kompletne = True
    for A, B in PARY + [PARA_STARA]:
        pa = przyrosty(srednie(res, *A), N_PARY)
        pb = przyrosty(srednie(res, *B), [4 * n for n in N_PARY])
        zs = []
        for x, y in zip(pa, pb):
            if x is None or y is None:
                zs.append(None)
                continue
            zs.append((x[0] - y[0]) / max(math.hypot(x[1], y[1]), 1e-12))
        opis = ' ; '.join(('—' if x is None or y is None else f'{x[0]:.3f}±{x[1]:.3f} vs {y[0]:.3f}±{y[1]:.3f} (z={z:+.1f})')
                          for x, y, z in zip(pa, pb, zs))
        stara = (A, B) == PARA_STARA
        log(f'   {A[0]} {A[1]} | {B[0]} {B[1]} (πR/σ={pr[A]:.1f}){" [para z etap26, poza werdyktem]" if stara else ""}: {opis}')
        if stara:
            continue
        if any(z is None for z in zs):
            kompletne = False
            continue
        if max(abs(z) for z in zs) > 3:
            zle3 += 1
        if max(abs(z) for z in zs) > 2:
            wszystkie_ok = False
    if not kompletne:
        log('T1: dane niepełne → bez werdyktu')
    else:
        log(f'T1: {"PRZESZŁO" if wszystkie_ok else ("UPADŁO" if zle3 >= 2 else "NIEROZSTRZYGNIĘTE")} '
            f'(par z |z| > 3: {zle3} z 4)')
    # T2
    if 8192 in Ns and 20480 in Ns:
        log('\nT2 (mechanizm): L = [S(20480) − S(8192)] / log₂2,5')
        Ls = {}
        for k in sorted(przyp, key=lambda k: -pr[k]):
            sr = srednie(res, *k)
            L = (sr[20480][0] - sr[8192][0]) / math.log2(2.5)
            eL = math.hypot(sr[20480][1], sr[8192][1]) / math.log2(2.5)
            Ls[k] = (L, eL)
            log(f'   {k[0]:2s} σ={k[1]:<5} πR/σ={pr[k]:5.1f}: L = {L:.3f} ± {eL:.3f}{" [NOWY]" if k in NOWE else ""}')
        a_ok = all(Ls[k][0] < 0.15 for k in NOWE if pr[k] <= 3.3 + 1e-9)
        b_ok = all(Ls[k][0] > 0.5 for k in NOWE if pr[k] >= 9.8 - 1e-9)
        a_zle = any(Ls[k][0] - 0.15 > 2 * Ls[k][1] for k in NOWE if pr[k] <= 3.3 + 1e-9)
        b_zle = any(0.5 - Ls[k][0] > 2 * Ls[k][1] for k in NOWE if pr[k] >= 9.8 - 1e-9)
        x = np.array([pr[k] for k in Ls])
        y = np.array([Ls[k][0] for k in Ls])
        rho = float(np.corrcoef(rangi(x), rangi(y))[0, 1])
        c_ok = rho >= 0.9
        v = 'PRZESZŁO' if (a_ok and b_ok and c_ok) else ('UPADŁO' if (a_zle or b_zle or rho < 0.7) else 'NIEROZSTRZYGNIĘTE')
        log(f'T2: (a) {"tak" if a_ok else "nie"}, (b) {"tak" if b_ok else "nie"}, (c) ρ = {rho:.3f} → {v}')
    else:
        log('\nT2: brak N = 8192 lub 20480 → bez werdyktu')
    # T3
    if 8192 in Ns and 20480 in Ns:
        log('\nT3 (mody prawie czyste): udział 2% najcięższych modów w S_F przy 20480 i w przyroście 8192→20480')
        ok, zle = True, False
        for k in sorted(przyp, key=lambda k: -pr[k]):
            if pr[k] < 6.5 - 1e-9:
                continue
            SF = srednie(res, *k, pole='SF')
            Hc = srednie(res, *k, pole='ciezkie')
            u1 = Hc[20480][0] / SF[20480][0]
            u2 = (Hc[20480][0] - Hc[8192][0]) / (SF[20480][0] - SF[8192][0])
            ok &= (u1 >= 0.7) and (u2 >= 0.8)
            zle |= (u1 < 0.5) or (u2 < 0.5)
            log(f'   {k[0]:2s} σ={k[1]:<5} πR/σ={pr[k]:5.1f}: udział w S_F {u1:.3f}, w przyroście {u2:.3f}')
        log(f'T3: {"PRZESZŁO" if ok else ("UPADŁO" if zle else "NIEROZSTRZYGNIĘTE")}')
    # pułap i średnia energia modularna
    log('\nRaport: pułap widma modularnego ε_max (średnia po ziarnach) i średnia ε ważona wkładem do S_F')
    for r in REGIONY:
        em = []
        for N in Ns:
            x = [res[f'{N}|{z}'][r]['eps_max'] for z in range(1, ZIARNA[N] + 1) if f'{N}|{z}' in res]
            em.append(f'{N}: {np.mean(x):.2f}')
        log(f'   ε_max {r}: ' + ' | '.join(em))
        for s in SIGMY[r]:
            es = srednie(res, r, s, pole='eps_sr')
            log(f'      σ={s:<5} πR/σ={pr[(r, s)]:5.1f}: ⟨ε⟩ ' + ' | '.join(f'{N}: {m:.2f}' for N, (m, e) in es.items()))
    # kontrole
    przeb = [k for k in res if '|' in k]
    wsp = sorted(set(SIGMY['U']) & set(SIGMY['Um']))
    k2 = [(k, s) for k in przeb for s in wsp if res[k]['Um'][f'{s}']['Sfull'] > res[k]['U'][f'{s}']['Sfull'] * (1 + 1e-9)]
    k3 = sum(res[k][r]['niefizF'] + res[k][r]['niefizC'] for k in przeb for r in REGIONY)
    k4 = max(res[k][r][f'{s}']['z0'] for k in przeb for r in REGIONY for s in SIGMY[r])
    cen = max(1 - res[k][r][f'{s}']['SF'] / res[k][r][f'{s}']['Sfull'] for k in przeb for r in REGIONY for s in SIGMY[r])
    log(f'\nK0: {res.get("K0", float("nan")):.1e}; K2: {"tak" if not k2 else "NIE " + str(k2[:3])}; K3 niefizyczne: {k3}; '
        f'K4 max składowa zerowa: {k4:.1e}; (raport) największy udział centrum: {cen:.4f}')


def main():
    plik_log = open(CKPT.replace('.json', '.log'), 'a', encoding='utf-8')

    def log(s):
        print(s, flush=True)
        plik_log.write(s + '\n')
        plik_log.flush()
    res = json.load(open(CKPT)) if os.path.exists(CKPT) else {}
    log(f'etap26b — {"GPU" if GPU else "CPU"}; checkpoint: {len([k for k in res if "|" in k])} przebiegów')
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
            except Exception as e:
                log(f'N={N} ziarno={z}: BŁĄD {type(e).__name__}: {e}')
                zwolnij()
                break
            json.dump(res, open(CKPT, 'w'))
    raport(res, log)


if __name__ == '__main__':
    main()
