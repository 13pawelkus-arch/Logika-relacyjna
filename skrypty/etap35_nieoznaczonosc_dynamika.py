# etap35 — kontrola poprawki 270: nieoznaczosc, brak zera absolutnego i dynamika (R1a, R1b-F, Page–Wootters).
# Twierdzenia sa na kartce (blok 270 w R1a); tu tylko kontrola tozsamosci, bez losowania wnioskow.
#
# Zdania, ktore moga upasc:
#  (1) suma wariancji trzech odczytow komplementarnych w kuli B^3 to 3 - |r|^2 (symbolicznie), wiec >= 2;
#      calkowita oznaczonosc (r w {+-1}^3, |r|^2 = 3) lezy poza kula; dla d = 1 suma 1 - r^2 znika na koncach;
#  (2) przy G Psi = 0, G = G_C + G_S: Var(G) = 0, Var(G_S) = Var(G_C) = v = -Cov(G_C, G_S);
#  (3) zegar kowariantny E_th = e^{-i G_C th} E_0 e^{i G_C th}: stan S warunkowany wskazaniem th
#      to dokladnie e^{-i G_S th} psi_S(0) (z dokladnoscia do fazy) — dla stanu z wiezem;
#  (4) v = 0 (stan iloczynowy stanow wlasnych): stan warunkowy stały przy kazdym th;
#  (5) Mandelstam–Tamm w singlecie (G_S = sigma3/2, Delta = 1/2): |<psi(0)|psi(th)>| = cos(th/2),
#      ortogonalnosc dokladnie przy th = pi — granica osiagnieta;
#  (6) dla kubitu-czesci: sum_i Var(sigma_i/2) = (3 - |r|^2)/4 >= 1/2;
#  (7) trzy wiezy J_i Psi = 0 (C dowolne, tu trzy kubity): stan czesci-kubitu = 1/2, v_i = 1/4 dla kazdego i
#      (niezmienniczosc pod wspolnymi obrotami + Schur; na kartce, tu kontrola).
# Wymaga: sympy, numpy, scipy.
import sympy as s
import numpy as np
from scipy.linalg import expm

ok = []
def check(name, cond):
    ok.append((name, bool(cond)))
    if not cond:
        raise AssertionError(name)

# (1)
r1, r2, r3 = s.symbols('r1 r2 r3', real=True)
X = s.Matrix([[0, 1], [1, 0]]); Y = s.Matrix([[0, -s.I], [s.I, 0]]); Z = s.Matrix([[1, 0], [0, -1]])
rho = (s.eye(2) + r1*X + r2*Y + r3*Z) / 2
var_sum = s.simplify(sum((rho*P*P).trace() - ((rho*P).trace())**2 for P in (X, Y, Z)))
check('(1) suma wariancji = 3 - |r|^2', s.simplify(var_sum - (3 - r1**2 - r2**2 - r3**2)) == 0)
check('(1) calkowita oznaczonosc poza kula: |r|^2 = 3 > 1', var_sum.subs({r1: 1, r2: 1, r3: 1}) == 0)
r = s.symbols('r', real=True)
check('(1) d = 1: 1 - r^2 znika na koncach', (1 - r**2).subs(r, 1) == 0 and (1 - r**2).subs(r, -1) == 0)

# (2)–(4): losowy stan z wiezem na sektorach |-E_k>_C |E_k>_S
rng = np.random.default_rng(270)
E = np.array([0., 1., 2.]); I3 = np.eye(3)
GS = np.diag(E); GC = np.diag(-E)
G = np.kron(GC, I3) + np.kron(I3, GS)
c = rng.normal(size=3) + 1j*rng.normal(size=3); c /= np.linalg.norm(c)
Psi = sum(c[k]*np.kron(I3[:, k], I3[:, k]) for k in range(3))
def mean(A, p): return np.vdot(p, A @ p).real
def var(A, p): return mean(A @ A, p) - mean(A, p)**2
GSf, GCf = np.kron(I3, GS), np.kron(GC, I3)
v = var(GSf, Psi); cov = mean(GCf @ GSf, Psi) - mean(GCf, Psi)*mean(GSf, Psi)
check('(2) G Psi = 0', np.linalg.norm(G @ Psi) < 1e-12)
check('(2) Var(G) = 0', abs(var(G, Psi)) < 1e-12)
check('(2) Var(G_S) = Var(G_C) = -Cov > 0', abs(v - var(GCf, Psi)) < 1e-12 and abs(v + cov) < 1e-12 and v > 0)
chi0 = np.ones(3) / np.sqrt(3)
def cond(th, P):
    chi = expm(-1j*GC*th) @ chi0
    psi = np.kron(chi.conj(), I3) @ P
    return psi / np.linalg.norm(psi)
for th in (0.3, 1.1, 2.5):
    pred = expm(-1j*GS*th) @ cond(0, Psi)
    check(f'(3) ewolucja warunkowa th={th}', abs(abs(np.vdot(cond(th, Psi), pred)) - 1) < 1e-12)
    check(f'(3) odczyt zmienia sie th={th}', abs(abs(np.vdot(cond(0, Psi), cond(th, Psi))) - 1) > 1e-6)
Psi0 = np.kron(I3[:, 1], I3[:, 1])
check('(4) v = 0', abs(var(GSf, Psi0)) < 1e-14)
for th in (0.3, 1.1, 2.5):
    check(f'(4) stan warunkowy staly th={th}', abs(abs(np.vdot(cond(0, Psi0), cond(th, Psi0))) - 1) < 1e-12)

# (5)
psi = np.array([1, -1]) / np.sqrt(2); g = np.diag([0.5, -0.5])
for th in (np.pi/3, np.pi/2, np.pi):
    f = abs(np.vdot(psi, expm(-1j*g*th) @ psi))
    check(f'(5) MT nasycone th={th:.4f}', abs(f - np.cos(th/2)) < 1e-12)

# (6)
half = sum((rho*(P/2)*(P/2)).trace() - ((rho*P/2).trace())**2 for P in (X, Y, Z))
check('(6) suma Var(sigma_i/2) = (3 - |r|^2)/4', s.simplify(half - (3 - r1**2 - r2**2 - r3**2)/4) == 0)

# (7)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex)
def op(m, k, n=4):
    out = np.array([[1.]], complex)
    for j in range(n):
        out = np.kron(out, m if j == k else np.eye(2))
    return out
J = [sum(op(m/2, k) for k in range(4)) for m in (sx, sy, sz)]
J2 = sum(Ji @ Ji for Ji in J)
w, V = np.linalg.eigh(J2)
N0 = V[:, np.abs(w) < 1e-10]
check('(7) sektor J = 0 dla 3 + 1 kubitow ma wymiar 2', N0.shape[1] == 2)
for _ in range(5):
    a = rng.normal(size=2) + 1j*rng.normal(size=2); P7 = N0 @ (a/np.linalg.norm(a))
    check('(7) trzy wiezy', all(np.linalg.norm(Ji @ P7) < 1e-12 for Ji in J))
    M = P7.reshape(8, 2); rS = M.T @ M.conj()
    check('(7) stan czesci = 1/2', np.linalg.norm(rS - np.eye(2)/2) < 1e-12)
    check('(7) v_i = 1/4', all(abs(var(op(m/2, 3), P7) - 0.25) < 1e-12 for m in (sx, sy, sz)))

print({'status': 'PASS', 'kontrole': len(ok), 'v_przyklad': round(v, 12)})
