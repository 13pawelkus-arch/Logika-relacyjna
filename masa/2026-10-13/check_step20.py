"""Threshold representation audit; conditional current/measure, no frame-only claim."""
from pathlib import Path
import json
import sys
sys.path.insert(0, str(Path(__file__).parent / 'deps'))
import mpmath as mp
import sympy as sp

checks = {}
exact_count = 0


def exact(label, expression):
    global exact_count
    value = sp.simplify(expression)
    assert value == 0, (label, value)
    exact_count += 1


def exact_matrix(label, expression):
    for entry in expression:
        exact(label, entry)


t, r, c, beta = sp.symbols('t r c beta', real=True)
rho = sp.sqrt(1-4*t)*(1+2*t)
tail = rho/3
exact('tail derivative', sp.diff(tail, t)+4*t/sp.sqrt(1-4*t))
exact('tail at zero', tail.subs(t, 0)-sp.Rational(1, 3))
exact('tail at threshold', tail.subs(t, sp.Rational(1, 4)))


def beta_integral(n, exponent):
    return sp.simplify(sp.gamma(n+1)*sp.gamma(exponent+1)
                       /sp.gamma(n+exponent+2)/4**(n+1))


moments = []
for k in range(10):
    value = 4*beta_integral(k+1, sp.Rational(-1, 2))
    target = 2*sp.factorial(k+1)**2/sp.factorial(2*k+3)
    exact('moment', value-target)
    if k:
        from_tail = sp.Rational(k, 3)*(beta_integral(k-1, sp.Rational(1, 2))
                                      +2*beta_integral(k, sp.Rational(1, 2)))
        exact('tail moment', value-from_tail)
    moments.append(str(value))

angular = (1+c)**2+(1-c)**2+2*(1-beta**2)*(1-c**2)
angular_ratio = sp.integrate(angular, (c, -1, 1))/sp.Rational(16, 3)
exact('angular average ratio', angular_ratio-(3-beta**2)/2)

sigma = [sp.Matrix([[0, 1], [1, 0]]),
         sp.Matrix([[0, -sp.I], [sp.I, 0]]),
         sp.diag(1, -1)]
eye = sp.eye(2)
a, b = sp.symbols('a b', positive=True)
E = (a*a+b*b)/2
p = (a*a-b*b)/2
m = a*b
A, B = sp.diag(a, b), sp.diag(b, a)
exact_matrix('mass closure', A*B-m*eye)
exact('shell determinant', E*E-p*p-m*m)
exact_matrix('normalization', A*A+B*B-2*E*eye)
pair_current = [A*s*B+B*s*A for s in sigma]
for i in range(3):
    expected = 2*(E if i < 2 else m)*sigma[i]
    exact_matrix('current without gamma notation', pair_current[i]-expected)
    weight = sp.trace(pair_current[i]*pair_current[i].conjugate().T)
    exact('spin sum', weight-8*(E*E if i < 2 else m*m))
exact_matrix('time component zero', A*B-B*A)

# The two Weyl blocks solve the canonical free mass relation.
U = B.col_join(A)
V = A.col_join(-B)
Pplus, Pminus = A*A, B*B
Kp = (-m*eye).row_join(Pminus).col_join(Pplus.row_join(-m*eye))
Kanti = (m*eye).row_join(Pplus).col_join(Pminus.row_join(m*eye))
exact_matrix('particle mass relation', Kp*U)
exact_matrix('antiparticle mass relation', Kanti*V)

# Exact arbitrary-direction check: tensor, not just its angular integral.
rotations = [eye, sp.Rational(3, 5)*eye+sp.I*sp.Rational(4, 5)*sigma[1],
             (eye+sp.I*(sigma[0]+sigma[1]+sigma[2]))/2]
tensor_entries = 0
for av, bv in [(1, 1), (2, 1), (3, 2), (5, 1)]:
    ev, pv, mv = E.subs({a: av, b: bv}), p.subs({a: av, b: bv}), av*bv
    for rotation in rotations:
        exact_matrix('rotation unitary', rotation*rotation.conjugate().T-eye)
        Ar = rotation*A.subs({a: av, b: bv})*rotation.conjugate().T
        Br = rotation*B.subs({a: av, b: bv})*rotation.conjugate().T
        direction = rotation*sigma[2]*rotation.conjugate().T
        n = [sp.trace(direction*s)/2 for s in sigma]
        js = [Ar*s*Br+Br*s*Ar for s in sigma]
        for i in range(3):
            for j in range(3):
                actual = sp.trace(js[i]*js[j].conjugate().T)
                expected = 8*(ev*ev*int(i == j)-pv*pv*n[i]*n[j])
                exact('rotated pair tensor', actual-expected)
                tensor_entries += 1

# General on-shell transverse current has two form factors.
f1, f2 = sp.symbols('f1 f2', real=True)
for i in range(3):
    Ji = f1*pair_current[i]+f2*(E/m)*(A*sigma[i]*A+B*sigma[i]*B)
    expected = 2*E*(f1+f2)*sigma[i] if i < 2 else 2*m*(f1+E*E/(m*m)*f2)*sigma[i]
    exact_matrix('Dirac and Pauli weights', Ji-expected)

# Equal EM charges commute with the zigzag mass generator.
qL, qR, theta = sp.symbols('qL qR theta', real=True)
hm = sp.Matrix([[0, theta], [theta, 0]])
Q = sp.diag(qL, qR)
exact_matrix('equal charge mass commutator', (Q*hm-hm*Q).subs(qR, qL))

# Scalar charge current, normalized to the same massless fermion channel.
scalar = 4*beta**2*(1-c*c)
fermion_reference = 8*(1+c*c)
scalar_ratio = beta*sp.integrate(scalar, (c, -1, 1))/sp.integrate(fermion_reference, (c, -1, 1))
exact('negative spin control', scalar_ratio-beta**3/4)

# The standard invariant product shell measure gives p^(d-2)/E.
# Its equal-total-energy ratio to m=0 is beta^(d-2), not its absolute scale.
d = sp.symbols('d', integer=True, positive=True)
phase_measure = p**(d-1)/(4*E*E)/(2*p/E)
exact('shell radial Jacobian', phase_measure-p**(d-2)/(8*E))

# Diagnostic family on the physical timelike interval only.
# It is NOT asserted to be a full model of the frame or a physical new coupling.
lam = sp.symbols('lambda', real=True)
F2 = 16*lam*t*t*(1-4*t)
GM = 1+F2
GE = 1+4*lam*t*(1-4*t)
poly = sp.expand(GM**2+2*t*GE**2)
rho_lam = sp.sqrt(1-4*t)*poly
exact('same UV endpoint', rho_lam.subs(t, 0)-1)
exact('same threshold currents GM', GM.subs(t, sp.Rational(1, 4))-1)
exact('same threshold currents GE', GE.subs(t, sp.Rational(1, 4))-1)
mu1_lam = sp.simplify(sum(coeff*beta_integral(power[0], sp.Rational(1, 2))/3
                          for power, coeff in sp.Poly(poly, t).terms()))
assert sp.simplify(mu1_lam-sp.Rational(1, 15)) != 0
diagnostic = {
    'F2_on_physical_interval': str(F2),
    'mu0': '1/3',
    'mu1': str(mu1_lam),
    'mu1_at_lambda_1_over_100': str(mu1_lam.subs(lam, sp.Rational(1, 100))),
    'scope': 'nonuniqueness of the specified current/kinematics/endpoints only; not a countermodel of the complete frame'
}

# Positivity of the diagnostic logarithmic measure is an exact inequality,
# certified by positive Bernstein coefficients on x=4t in [0,1].
x = sp.symbols('x', real=True)
poly_x = sp.expand(poly.subs({t: x/4, lam: sp.Rational(1, 100)}))
derivative_numerator = sp.expand(2*poly_x-4*(1-x)*sp.diff(poly_x, x))
positive_polynomial = sp.Poly(sp.cancel(derivative_numerator/x), x)
degree = positive_polynomial.degree()
bernstein = [sp.simplify(sum(positive_polynomial.nth(k)*sp.binomial(j,k)/sp.binomial(degree,k)
                            for k in range(j+1))) for j in range(degree+1)]
assert all(v > 0 for v in bernstein)
diagnostic['positive_measure_at_lambda_1_over_100'] = True
diagnostic['Bernstein_certificate'] = [str(v) for v in bernstein]

mp.mp.dps = 80
max_error = mp.mpf('0')
integrals = []
for value in ['0.01', '0.1', '1', '4', '10', '100', '1000']:
    rv = mp.mpf(value)
    feynman = 2*mp.quad(lambda x: x*(1-x)*mp.log1p(rv*x*(1-x)), [0, mp.mpf('.5'), 1])
    measure = mp.quad(lambda v: (1-v*v)/2*mp.log1p(rv*(1-v*v)/4), [0, 1])
    threshold = rv/3*mp.quad(lambda v: v*v*(3-v*v)/(4+rv*(1-v*v)), [0, 1])
    dispersion = rv/3*mp.quad(lambda sv: mp.sqrt(1-4/sv)*(1+2/sv)/(sv*(sv+rv)), [4, 8, 32, 128, mp.inf])
    error = max(abs(feynman-x) for x in [measure, threshold, dispersion])
    assert error < mp.mpf('1e-70'), (value, error)
    max_error = max(max_error, error)
    integrals.append({'r': value, 'F_gamma': mp.nstr(feynman, 35), 'max_error': mp.nstr(error, 8)})

output = {
    'status': 'PASS', 'exact_scalar_identities': exact_count,
    'rotated_spin_tensor_entries': tensor_entries, 'moments_mu_0_through_9': moments,
    'high_precision_digits': mp.mp.dps, 'max_integral_error': mp.nstr(max_error, 10),
    'four_representations': integrals, 'scalar_negative_control': 'beta^3/4',
    'current_diagnostic': diagnostic,
    'scope': 'algebra and conditional invariant phase-space/current reconstruction; causality assumptions and frame sufficiency require separate arguments'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(output, ensure_ascii=False, indent=2))
