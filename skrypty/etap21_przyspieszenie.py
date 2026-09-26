# etap21 — przyspieszenie jako nadwyżka z odwrotnej nierówności trójkąta (poprawka 164)
#
# Kandydat (R1f-4; §F1 etap8 „piąta pułapka”): trzy elementy trajektorii p ≺ q ≺ c, odległe o tyknięcie δ;
#   nadwyżka E = τ(p,c) − τ(p,q) − τ(q,c) ≥ 0 (zero dokładnie dla prostej).
#   Ruch o stałym przyspieszeniu własnym a: E = (2/a)[sinh(aδ) − 2 sinh(aδ/2)] = a²δ³/4 + O(a⁴δ⁵)
#   → przyspieszenie na tyknięcie:  a·δ = 2·√(E/δ)  (stosunek dwóch liczebności — bez gęstości, bez pojemnika).
#
# Zdania do upadku (zapisane przed rachunkiem):
#  A1 (kontinuum, 1+1): estymator 2√(E/δ³) → a przy δ → 0; błąd względny maleje jak δ² (stosunek ≈ 4 przy
#      połowieniu δ); prosta (a = 0): E = 0 dokładnie; pchnięcie całej trójki nie zmienia E (do 1e-12).
#  A2 (kontinuum, 3+1): dla ruchu po okręgu (a = γ²v²/R) i dla losowej gładkiej trajektorii estymator zbiega do
#      |a^μ| (normy Minkowskiego przyspieszenia) jak δ².
#  A3 (porządek, 1+1, sprinkling): τ zastąpione długością najdłuższego łańcucha L (miara odczytu, R1a);
#      nadwyżka w linkach E_L ≥ 0 zawsze (nadaddytywność łańcuchów — bez wyjątku);
#      (a·δ)_est = 2·√([E_L(a) − E_L(0)] / L(p,q)) — stosunek liczebności, bez ρ — zbiega do a·δ
#      przy rosnącej gęstości (skan ≥ 1 dekada); kontrola a = 0 odejmuje obciążenie skończonej liczebności.
#      Upada, jeśli stosunek zmierzony/oczekiwany nie zbliża się do 1 z gęstością albo zależy od a.
import numpy as np, bisect, time

SEED = 11
rng = np.random.default_rng(SEED)

# ---------- A1: kontinuum 1+1, ruch hiperboliczny ----------
def hiperbola(a, tau):
    if a == 0: return np.array([tau, 0.0])
    return np.array([np.sinh(a * tau) / a, (np.cosh(a * tau) - 1) / a])
def interwal(x, y):
    d = y - x; return np.sqrt(d[0] ** 2 - d[1:] @ d[1:])
def nadwyzka(p, q, c): return interwal(p, c) - interwal(p, q) - interwal(q, c)
def pchnij2(x, v):
    g = 1 / np.sqrt(1 - v * v); return np.array([g * (x[0] + v * x[1]), g * (x[1] + v * x[0])])

print("A1 (kontinuum 1+1): a_est = 2√(E/δ³)")
ok1 = True
for a in (0.1, 0.5, 1.0, 2.0):
    bledy = []
    for d in (0.4, 0.2, 0.1, 0.05):
        p, q, c = hiperbola(a, -d), hiperbola(a, 0), hiperbola(a, d)
        E = nadwyzka(p, q, c); aest = 2 * np.sqrt(E / d ** 3); bledy.append(abs(aest - a) / a)
        v = rng.uniform(-0.9, 0.9); Eb = nadwyzka(pchnij2(p, v), pchnij2(q, v), pchnij2(c, v))
        ok1 &= abs(Eb - E) < 1e-12 * max(1, E)
    st = [bledy[i] / bledy[i + 1] for i in range(3)]
    print(f"   a = {a}: błędy względne {', '.join(f'{b:.1e}' for b in bledy)}; stosunki przy połowieniu δ: {', '.join(f'{s:.2f}' for s in st)}")
    ok1 &= all(3.5 < s < 4.5 for s in st)
E0 = nadwyzka(hiperbola(0, -0.3), hiperbola(0, 0), hiperbola(0, 0.3))
ok1 &= abs(E0) < 1e-15
print(f"   prosta: E = {E0:.1e};  pchnięcia nie zmieniają E: {'tak' if ok1 else 'NIE'}  -> A1 {'PRZESZŁO' if ok1 else 'UPADŁO'}")

# ---------- A2: kontinuum 3+1 ----------
def trajektoria_tau(xfun, tmax, n=200001):
    t = np.linspace(-tmax, tmax, n); X = np.array([xfun(s) for s in t])
    v = np.gradient(X, t, axis=0); tau = np.concatenate([[0], np.cumsum(np.sqrt(1 - (v[1:] ** 2).sum(1)) * np.diff(t))])
    tau -= np.interp(0, t, tau); return t, X, tau
def punkt(t, X, tau, s):
    ts = np.interp(s, tau, t); return np.r_[ts, [np.interp(ts, t, X[:, k]) for k in range(3)]]
def acc_prawdziwe(xfun, t0, h=1e-4):
    ev = lambda s: np.r_[s, xfun(s)]
    x = [ev(t0 - h), ev(t0), ev(t0 + h)]
    v = (x[2] - x[0]) / (2 * h); A = (x[2] - 2 * x[1] + x[0]) / h ** 2
    g2 = 1 / (1 - v[1:] @ v[1:]);             # u = γ(1, v); a^μ = γ² A + (γ⁴ v·A) v  (dla A^0 = 0)
    vv = v[1:]; AA = A[1:]; a4 = np.r_[g2 * g2 * (vv @ AA), g2 * AA + g2 * g2 * (vv @ AA) * vv]
    return np.sqrt(-(a4[0] ** 2 - a4[1:] @ a4[1:]))
R, vk = 1.0, 0.6; w = vk / R
okrag = lambda s: np.array([R * np.cos(w * s), R * np.sin(w * s), 0.0])
kk = rng.normal(size=(3, 3)) * 0.05; ff = rng.uniform(0.5, 1.5, (3, 3)); ph = rng.uniform(0, 2 * np.pi, (3, 3))
losowa = lambda s: np.array([sum(kk[i, j] * np.sin(ff[i, j] * s + ph[i, j]) for j in range(3)) for i in range(3)])
print("A2 (kontinuum 3+1):")
ok2 = True
for nazwa, xf in (("okrąg (a = γ²v²/R)", okrag), ("losowa gładka", losowa)):
    t, X, tau = trajektoria_tau(xf, 3.0)
    atrue = acc_prawdziwe(xf, 0.0)
    if nazwa.startswith("okrąg"): atrue_an = (1 / (1 - vk ** 2)) * vk ** 2 / R; atrue_msg = f" (analitycznie {atrue_an:.6f})"
    else: atrue_msg = ""
    bledy = []
    for d in (0.4, 0.2, 0.1):
        p, q, c = punkt(t, X, tau, -d), punkt(t, X, tau, 0), punkt(t, X, tau, d)
        aest = 2 * np.sqrt(nadwyzka(p, q, c) / d ** 3); bledy.append(abs(aest - atrue) / atrue)
    st = [bledy[i] / bledy[i + 1] for i in range(2)]
    print(f"   {nazwa}: |a| = {atrue:.6f}{atrue_msg}; błędy {', '.join(f'{b:.1e}' for b in bledy)}; stosunki {', '.join(f'{s:.2f}' for s in st)}")
    ok2 &= bledy[-1] < 5e-3 and all(2.5 < s < 5.5 for s in st)
print(f"   -> A2 {'PRZESZŁO' if ok2 else 'UPADŁO'}")

# ---------- A3: porządek 1+1 (sprinkling), najdłuższe łańcuchy ----------
def lis(v):
    t = []
    for x in v:
        i = bisect.bisect_left(t, x)
        if i == len(t): t.append(x)
        else: t[i] = x
    return len(t)
def L(pu, pv, qu, qv, U, V):   # liczba linków najdłuższego łańcucha od p do q (wnętrze + 1)
    m = (U > pu) & (U < qu) & (V > pv) & (V < qv)
    idx = np.argsort(U[m]); return lis(V[m][idx]) + 1
def proba(a, rho, d=1.0):
    P = [hiperbola(a, s) for s in (-d, 0.0, d)]
    uv = [(x[0] + x[1], x[0] - x[1]) for x in P]
    (pu, pv), (qu, qv), (cu, cv) = uv
    area = (cu - pu) * (cv - pv) / 2
    n = rng.poisson(rho * area)
    U = rng.uniform(pu, cu, n); V = rng.uniform(pv, cv, n)
    # POPRAWKA (błąd konstrukcji w pierwszym przebiegu): q jest elementem porządku — musi należeć do zbioru,
    # inaczej łańcuch przez q nie jest dostępny i nadaddytywność L(p,c) ≥ L(p,q) + L(q,c) może zawieść.
    U = np.r_[U, qu]; V = np.r_[V, qv]
    Lpc, Lpq, Lqc = L(pu, pv, cu, cv, U, V), L(pu, pv, qu, qv, U, V), L(qu, qv, cu, cv, U, V)
    return Lpc - Lpq - Lqc, Lpq
print("A3 (porządek 1+1, sprinkling; τ → najdłuższy łańcuch):")
t0 = time.time(); ujemnych = 0
wyniki = {}
for rho, ns in ((1000, 600), (4000, 400), (16000, 250), (64000, 120)):
    for a in (0.0, 0.5, 1.0, 1.5):
        E = []; Lq = []
        for _ in range(ns):
            e, lq = proba(a, rho); E.append(e); Lq.append(lq); ujemnych += (e < 0)
        wyniki[(rho, a)] = (np.mean(E), np.std(E) / np.sqrt(ns), np.mean(Lq))
    print(f"   ρ = {rho}: gotowe ({time.time() - t0:.0f} s)")
print(f"   nadwyżka E_L < 0 w {ujemnych} próbach (musi być 0: nadaddytywność łańcuchów)")
ok3 = ujemnych == 0
for a in (0.5, 1.0, 1.5):
    wiersz = []
    for rho in (1000, 4000, 16000, 64000):
        Ea, sa, Lq = wyniki[(rho, a)]; E0_, s0, _ = wyniki[(rho, 0.0)]
        roz = Ea - E0_
        ad = 2 * np.sqrt(max(roz, 0) / Lq)
        err = (ad / 2) * 0.5 * np.hypot(sa, s0) / max(roz, 1e-9) * 2
        wiersz.append((rho, ad, err))
    # POPRAWKA (błąd porównania w pierwszym przebiegu): oczekiwane = estymator kontinuum przy TYM SAMYM δ = 1,
    # nie granica δ → 0 (A1: przy skończonym aδ estymator ma własną poprawkę).
    # POPRAWKA 2 (błąd porównania w drugim przebiegu): w porządku tyknięcie między kolejnymi elementami
    # trajektorii = L(p,q) = odczyt po CIĘCIWIE (łuku w porządku nie ma); odniesienie liczone tak samo:
    Pm, P0, Pp = hiperbola(a, -1.0), hiperbola(a, 0), hiperbola(a, 1.0)
    ocz = 2 * np.sqrt(nadwyzka(Pm, P0, Pp) / interwal(Pm, P0))
    print(f"   a = {a} (odniesienie kontinuum, tyknięcie = cięciwa: {ocz:.4f}): " + "; ".join(f"ρ={r}: {x:.3f} ± {e:.3f} (stosunek {x / ocz:.3f})" for r, x, e in wiersz))
    st = [x / ocz for _, x, _ in wiersz]
    sig_last = wiersz[-1][2] / ocz
    ok3 &= abs(st[-1] - 1) < max(0.02, 3 * sig_last)   # warunek zaostrzony: przy najwyższej gęstości w 2% albo 3σ
print(f"   -> A3 {'PRZESZŁO' if ok3 else 'UPADŁO'}  (przy najwyższej gęstości stosunek w 2% / 3σ od 1, dla każdego a; czas {time.time() - t0:.0f} s)")
