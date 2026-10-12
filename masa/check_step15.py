"""Algebra checks for section 15; these are not alternative physical models."""
import json
from itertools import product
import numpy as np
from scipy.linalg import expm

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1, -1]).astype(complex)
I4 = np.eye(4, dtype=complex)
dag = lambda a: a.conj().T
tr = np.trace
err = lambda a, b: float(np.max(np.abs(a - b)))
checks = {}

# Noncommuting preparation and effect, three independently tagged contacts.
H = [np.kron(X, I2) + .3*np.kron(Z, Y),
     .7*np.kron(Y, Z) + .2*np.kron(I2, X),
     .6*np.kron(Z, X) - .4*np.kron(Y, I2)]
L = [.17*np.kron(Y, X), -.12*np.kron(X, Z), .09*np.kron(I2, Y)]
T0 = [expm(.23j*np.kron(Y, X)), expm(-.31j*np.kron(X, Z)),
      expm(.19j*(np.kron(Z, I2) + np.kron(X, Y)))]
rho = expm(-.6*np.kron(X, I2) - .25*np.kron(Z, Z))
rho /= tr(rho)
F = expm(-.4*np.kron(Y, I2) + .2*np.kron(X, Z))
F /= 1.1*np.linalg.eigvalsh(F).max()

def unitary(a):
    u = I4.copy()
    for t, h, ell, x in zip(T0, H, L, a):
        u = t @ expm(1j*(x*h + x*x*ell/2)) @ u
    return u

zero = np.zeros(3)
U = unitary(zero)
E = dag(U) @ F @ U
p = tr(E @ rho).real
assert p > 0 and err(E@rho, rho@E) > .001
prefix = I4.copy()
J, Jprime = [], []
for t, h, ell in zip(T0, H, L):
    J.append(dag(prefix) @ h @ prefix)
    Jprime.append(dag(prefix) @ ell @ prefix)
    prefix = t @ prefix

z = np.array([tr(E@j@rho)/p for j in J])
C = np.array([[tr(E@js@rho@jr)/p - z[r].conjugate()*z[s]
               for s, js in enumerate(J)] for r, jr in enumerate(J)])
lef = dag(np.linalg.cholesky(E))
rig = np.linalg.cholesky(rho)
A0 = lef @ rig
centered = [lef@j@rig - v*A0 for j, v in zip(J, z)]
gram = np.array([[tr(dag(a)@b)/p for b in centered] for a in centered])
checks['conditional_gram_error'] = err(C, gram)
checks['conditional_gram_min_eigenvalue'] = float(np.linalg.eigvalsh(C).min())
assert checks['conditional_gram_error'] < 2e-13
assert checks['conditional_gram_min_eigenvalue'] > -2e-13

def logZ(ap, am):
    return np.log(tr(F@unitary(ap)@rho@dag(unitary(am))))

h = 1e-4
mixed_errors = []
for r, s in product(range(3), repeat=2):
    er, es = zero.copy(), zero.copy()
    er[r], es[s] = h, h
    fd = (logZ(es, er)-logZ(es, -er)-logZ(-es, er)+logZ(-es, -er))/(4*h*h)
    mixed_errors.append(abs(fd-C[r, s]))
checks['nine_mixed_derivatives_max_error'] = float(max(mixed_errors))
assert max(mixed_errors) < 2e-6

# The same-contact term is fixed by the same unitary family.
same_errors = []
for r, (jr, jp) in enumerate(zip(J, Jprime)):
    comm = lambda a,b: a@b-b@a
    first = tr(E@(1j*comm(jr, rho)))
    second = tr(E@(-comm(jr, comm(jr, rho))+1j*comm(jp, rho)))
    expected = second/p - (first/p)**2
    er = zero.copy(); er[r] = h
    fd = (logZ(er, er)-2*logZ(zero, zero)+logZ(-er, -er))/(h*h)
    same_errors.append(abs(fd-expected))
checks['three_physical_second_derivatives_max_error'] = float(max(same_errors))
assert max(same_errors) < 2e-6
assert abs(tr(E@I4@rho@I4)/p - tr(E@rho)/p*tr(E@rho)/p) < 2e-13

# Two fermionic modes: CAR, Gaussian transport and full weighted Wick formula.
gam = [np.kron(X,I2), np.kron(Y,I2), np.kron(Z,X), np.kron(Z,Y)]
P = np.kron(Z,Z)
for a,b in product(range(4), repeat=2):
    assert err(gam[a]@gam[b]+gam[b]@gam[a], 2*(a==b)*I4) < 1e-14
B = lambda a,b: 1j*gam[a]@gam[b]
rg = expm(-.37*B(0,1)-.23*B(1,2)+.41*B(2,3))
rg /= tr(rg)
eg = expm(.29*B(0,2)-.33*B(1,3))
eg /= 1.1*np.linalg.eigvalsh(eg).max()
pg = tr(eg@rg)
Gs = expm(.21j*B(0,3)-.15j*B(1,2))
Gr = expm(-.17j*B(0,2)+.11j*B(1,3))
xx = [dag(Gs)@g@Gs for g in gam]
yy = [dag(Gr)@g@Gr for g in gam]
cross = np.array([[tr(eg@x@rg@y)/pg for y in yy] for x in xx])
vp = np.array([[0,.8,.2,0],[-.8,0,.1,-.3],[-.2,-.1,0,.6],[0,.3,-.6,0]])
vm = np.array([[0,.2,-.4,.1],[-.2,0,.7,0],[.4,-.7,0,.3],[-.1,0,-.3,0]])
Js = sum((.25j*vp[a,b]*xx[a]@xx[b] for a,b in product(range(4), repeat=2)), np.zeros((4,4),complex))
Jr = sum((.25j*vm[c,d]*yy[c]@yy[d] for c,d in product(range(4), repeat=2)), np.zeros((4,4),complex))
direct = tr(eg@Js@rg@Jr)/pg-tr(eg@Js@rg)*tr(eg@rg@Jr)/(pg*pg)
wick, residual_contracted, residuals = 0j, 0j, []
for a,b,c,d in product(range(4), repeat=4):
    four = tr(eg@xx[a]@xx[b]@rg@yy[c]@yy[d])/pg
    pp = tr(eg@xx[a]@xx[b]@rg)/pg
    mm = tr(eg@rg@yy[c]@yy[d])/pg
    pair = cross[a,c]*cross[b,d]-cross[a,d]*cross[b,c]
    remainder = four-pp*mm+pair
    residuals.append(abs(remainder))
    wick += vp[a,b]*vm[c,d]*pair/16
    residual_contracted -= vp[a,b]*vm[c,d]*remainder/16
checks['weighted_wick_256_components_max_error'] = float(max(residuals))
checks['current_contraction_error'] = float(abs(direct-wick))
assert max(residuals) < 2e-13 and abs(direct-wick) < 2e-13
assert abs(direct-wick-residual_contracted) < 2e-13

# Classification check: even/odd determinant ratio and cubic residual.
# It is a test of the algebraic criterion, not two candidate physical worlds.
even, odd = [0,3], [1,2]
ratio_errors, closure_errors = [], []
for chi in [0., .73, -1.12]:
    gate = expm(.25j*chi*P)@Gs
    A = gate[np.ix_(even,even)]
    Bodd = gate[np.ix_(odd,odd)]
    ratio = np.linalg.det(A)/np.linalg.det(Bodd)
    ratio_errors.append(abs(ratio-np.exp(1j*chi)))
    for g in gam:
        mapped = dag(gate)@g@gate
        projection = sum((tr(k@mapped)/4*k for k in gam), np.zeros((4,4),complex))
        remainder = mapped-projection
        norm = np.sqrt(tr(dag(remainder)@remainder).real/4)
        closure_errors.append(abs(norm-abs(np.sin(chi/2))))
checks['parity_determinant_ratio_max_error'] = float(max(ratio_errors))
checks['twelve_linear_closure_norms_max_error'] = float(max(closure_errors))
assert max(ratio_errors) < 2e-13 and max(closure_errors) < 2e-13

checks['status'] = 'PASS'
checks['scope'] = 'algebraic identities and conditional Gaussian reduction; not a derivation of F_gamma'
print(json.dumps(checks, ensure_ascii=False, indent=2))
