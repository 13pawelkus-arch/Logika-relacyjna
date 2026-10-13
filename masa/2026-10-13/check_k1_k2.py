"""Exact diagnostics for K1 and K2, with fixed operations and their own Grams.

These are algebraic scope checks, not a construction of the physical EM family.
Requires Python 3 and sympy. Writes check_k1_k2.json alongside this script.
"""
from pathlib import Path
import json
import sympy as s

checks = []


def zero(label, value):
    items = list(value) if isinstance(value, s.MatrixBase) else [value]
    for item in items:
        reduced = s.trigsimp(s.simplify(item))
        if reduced != 0:
            reduced = s.trigsimp(s.simplify(s.expand_complex(reduced)))
        assert reduced == 0, (label, reduced)
    checks.append(label)


I = s.eye(2)
sx = s.Matrix([[0, 1], [1, 0]])
sy = s.Matrix([[0, -s.I], [s.I, 0]])
sz = s.diag(1, -1)

# A real pair event transfers a relative phase; it is not cloning.
phi, chi = s.symbols('phi chi', real=True)
swap = s.Matrix([[1, 0, 0, 0], [0, 0, 1, 0],
                 [0, 1, 0, 0], [0, 0, 0, 1]])
pair = s.exp(s.I*s.pi/4)*swap
zero('pair unitary', pair.conjugate().T*pair-s.eye(4))
zero('pair determinant is one', pair.det()-1)
phase_rotation = s.diag(1, s.exp(s.I*chi))
joint_rotation = s.kronecker_product(phase_rotation, phase_rotation)
zero('pair respects joint U1 rotation', pair*joint_rotation-joint_rotation*pair)
initial = s.Matrix([1, 0, s.exp(s.I*phi), 0])/s.sqrt(2)
target = s.exp(s.I*s.pi/4)*s.Matrix([1, s.exp(s.I*phi), 0, 0])/s.sqrt(2)
zero('relative phase transferred by the pair event', pair*initial-target)
zero('spectator extension is unitary',
     s.kronecker_product(pair, I).conjugate().T*s.kronecker_product(pair, I)-s.eye(8))

# Two carried arms: amplitude coefficient is not the same as Gram overlap.
theta, phase, Q = s.symbols('theta phase Q', real=True)
c, b = s.cos(theta), s.sin(theta)
splitter = s.Matrix([[c, -b], [b, c]])
path0 = splitter*s.diag(1, 0)*splitter.T
path1 = splitter*s.diag(0, 1)*splitter.T
unitary = s.exp(s.I*Q*phase)*path0+path1
zero('carried two-path module is unitary', unitary.conjugate().T*unitary-I)
zero('amplitude lambda is cos(theta)^2',
     unitary[0, 0]-(1+c*c*(s.exp(s.I*Q*phase)-1)))
g11, g22, g12 = c**4, b**4, c*c*b*b
zero('two-path Gram has rank one', g11*g22-g12*g12)
zero('actual Gram overlap is lambda*(1-lambda)', g12-c*c*(1-c*c))
probability = s.expand(unitary[0, 0]*s.conjugate(unitary[0, 0]))
zero('probability uses that same Gram',
     probability-(g11+g22+2*g12*s.cos(Q*phase)))
zero('interference response is already order Q^2',
     s.diff(probability, phase, 2).subs(phase, 0)+2*Q*Q*g12)

# Two parallel oriented links. Their local reverse blocks are conjugate.
a1, a2 = s.symbols('a1 a2', real=True)
hop = s.exp(s.I*Q*a1)+s.exp(s.I*Q*a2)
kernel = s.Matrix([[3, hop], [s.conjugate(hop), 3]])
base = {a1: 0, a2: 0}
G = kernel.subs(base).inv()
V = [kernel.diff(a).subs(base) for a in (a1, a2)]
W = [[kernel.diff(a, d).subs(base) for d in (a1, a2)] for a in (a1, a2)]
contact = s.Matrix(2, 2, lambda i, j: -s.trace(G*W[i][j]))
bubble = s.Matrix(2, 2, lambda i, j: s.trace(G*V[i]*G*V[j]))
full = contact+bubble
explicit = s.hessian(-s.log(kernel.det()), (a1, a2)).subs(base)
zero('local W is contact diagonal', contact+s.Rational(4, 5)*Q*Q*I)
zero('VV has a nonzero same-contact contraction',
     bubble-s.Rational(2, 5)*Q*Q*s.ones(2))
zero('complete logdet Hessian', full-explicit)
gauge = s.Matrix([1, 1])
cycle = s.Matrix([1, -1])
zero('complete response annihilates pure gauge', full*gauge)
zero('completed contact plus off-diagonal VV',
     full-(-s.Rational(2, 5)*Q*Q*I+
           s.Rational(2, 5)*Q*Q*s.Matrix([[0, 1], [1, 0]])))
incomplete = contact + bubble - s.diag(bubble[0, 0], bubble[1, 1])
zero('omitting VV diagonal fails Ward by a definite amount',
     incomplete*gauge+s.Rational(2, 5)*Q*Q*gauge)

# Zero-argument Ward data do not fix a whole argument-dependent transverse part.
r, d0, d1 = s.symbols('r d0 d1', real=True)
transverse = (d0+d1*r)*cycle*cycle.T
zero('all transverse scalar slopes satisfy Ward', transverse*gauge)
zero('slope is invisible at zero argument',
     transverse.subs(r, 0)-d0*cycle*cycle.T)
zero('projection preserves the slope',
     (cycle.T*transverse*cycle)[0]/(cycle.T*(cycle*cycle.T)*cycle)[0]-(d0+d1*r))

# Gaussian response needs a homogeneous stationary sequence for a lag resolvent.
zeta = s.symbols('zeta')
n0, n1 = s.symbols('n0 n1', real=True)
unit_step = s.diag(1, s.exp(-s.I*s.pi/3))
N = s.diag(n0, n1)
lag_values = []
for m in range(1, 7):
    Xm = (unit_step.conjugate().T**m)*sx*(unit_step**m)
    answer = s.I*s.trace(N*(Xm*sx-sx*Xm))
    zero('retarded lag '+str(m), answer-2*(n0-n1)*s.sin(m*s.pi/3))
    lag_values.append(answer)
resolvent = s.sqrt(3)*(n0-n1)*zeta/(1-zeta+zeta*zeta)
series = s.series(resolvent, zeta, 0, 7).removeO()
for m, answer in enumerate(lag_values, 1):
    zero('resolvent coefficient '+str(m), series.coeff(zeta, m)-answer)

def transported(angle):
    step = s.diag(1, s.exp(-s.I*angle))
    return step.conjugate().T*sx*step

state = s.diag(1, 0)
X = [transported(angle) for angle in (0, s.pi/3, s.pi/2)]
near0 = s.I*s.trace(state*(X[1]*X[0]-X[0]*X[1]))
near1 = s.I*s.trace(state*(X[2]*X[1]-X[1]*X[2]))
zero('nonhomogeneous first adjacent response', near0-s.sqrt(3))
zero('nonhomogeneous second adjacent response', near1-1)

# Point-current and constant-Pauli threshold behavior, using the established map.
t = s.symbols('t', positive=True)
kappa = s.symbols('kappa', real=True)
beta = s.sqrt(1-4*t)
rho = beta*((1+kappa)**2+2*t*(1+kappa/(4*t))**2)
zero('constant Pauli high-energy weight', s.limit(t*rho, t, 0)-kappa*kappa/8)
zero('point current high-energy weight', s.limit(rho.subs(kappa, 0), t, 0)-1)
zero('one-subtraction near-edge divergence',
     s.limit(t*r*rho/(1+r*t), t, 0)-r*kappa*kappa/8)
zero('two-subtraction integrand finite at edge',
     s.limit(t*r*r*rho/(1+r*t), t, 0)-r*r*kappa*kappa/8)

output = {
    'status': 'PASS',
    'named_algebraic_checks': len(checks),
    'checks': checks,
    'two_path_example_at_theta_pi_over_4': {
        'amplitude_lambda': '1/2', 'Gram_12': '1/4'},
    'W_vertex': str(contact),
    'VV_including_diagonal': str(bubble),
    'full_response': str(full),
    'stationary_lag_resolvent': str(resolvent),
    'adjacent_nonhomogeneous_responses': [str(near0), str(near1)],
    'scope': 'pair transfer of relative state phase; fixed two-path Gram; Gaussian Hessian and Ward; stationary-step resolvent; threshold asymptotics. No proof of a frame-selected physical Pauli coupling or a scalar EM subtraction bound.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(output, ensure_ascii=False, indent=2))
