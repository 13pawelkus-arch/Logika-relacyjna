"""Kontrole pochodzenia wagi EM, 09.10.2026.

Wejścia QED są jawne w raporcie. Kontrole nie dowodzą wyprowadzenia działania
z ramy. Algebra macierzowa jest dokładna nad liczbami wymiernymi zespolonymi.
Całki zachowują pełne mianowniki i część urojoną powyżej progu.
Uruchomienie: Python z numpy/scipy; wynik JSON na stdout.
"""
from dataclasses import dataclass
from fractions import Fraction as F
import cmath
import json
import math
from scipy.integrate import quad


@dataclass(frozen=True)
class C:
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, 're', F(self.re))
        object.__setattr__(self, 'im', F(self.im))

    @staticmethod
    def cast(x):
        return x if isinstance(x, C) else C(x)

    def __add__(self, x):
        x = self.cast(x)
        return C(self.re+x.re, self.im+x.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, x):
        return self + -self.cast(x)

    def __rsub__(self, x):
        return self.cast(x) + -self

    def __mul__(self, x):
        x = self.cast(x)
        return C(self.re*x.re-self.im*x.im, self.re*x.im+self.im*x.re)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self.cast(x)
        norm = x.re*x.re+x.im*x.im
        assert norm
        return self*C(x.re/norm, -x.im/norm)

    def conj(self):
        return C(self.re, -self.im)


def matrix(rows):
    return [[C.cast(x) for x in row] for row in rows]


def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def add(A, B):
    return [[a+b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def scale(x, A):
    return [[C.cast(x)*a for a in row] for row in A]


def mul(A, B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), C())
             for j in range(len(B[0]))] for i in range(len(A))]


def dagger(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def inverse(A):
    n = len(A)
    rows = [row[:] + unit for row, unit in zip(A, eye(n))]
    for i in range(n):
        pivot = next(j for j in range(i, n) if rows[j][i] != C())
        rows[i], rows[pivot] = rows[pivot], rows[i]
        value = rows[i][i]
        rows[i] = [v/value for v in rows[i]]
        for j in range(n):
            if j != i:
                value = rows[j][i]
                rows[j] = [v-value*w for v, w in zip(rows[j], rows[i])]
    return [row[n:] for row in rows]


def block(A, B, C0, D):
    return [ra+rb for ra, rb in zip(A, B)] + [rc+rd for rc, rd in zip(C0, D)]


I2 = eye(2)
Z2 = scale(0, I2)
I4 = eye(4)
sigma = [matrix([[0, 1], [1, 0]]),
         matrix([[0, C(0, -1)], [C(0, 1), 0]]),
         matrix([[1, 0], [0, -1]])]


def gamma_from(triad):
    return [block(Z2, I2, I2, Z2)] + [block(Z2, s, scale(-1, s), Z2) for s in triad]


gamma = gamma_from(sigma)
metric = [1, -1, -1, -1]


def slash(p, gam=gamma):
    out = scale(0, I4)
    for j in range(4):
        out = add(out, scale(metric[j]*F(p[j]), gam[j]))
    return out


def contraction(A, gam=gamma):
    out = scale(0, I4)
    for g, sign in zip(gam, metric):
        out = add(out, scale(sign, mul(mul(g, A), g)))
    return out


def integrate_polynomial(coeffs):
    return sum((F(c)/F(i+1) for i, c in enumerate(coeffs)), F(0))


def qcomplex(fun, a, b, points=None):
    kwargs = dict(epsabs=2e-12, epsrel=2e-12, limit=250)
    if points:
        kwargs['points'] = points
    return complex(quad(lambda x: fun(x).real, a, b, **kwargs)[0],
                   quad(lambda x: fun(x).imag, a, b, **kwargs)[0])


out = {'scope': 'QED jednej petli, jawne wejscia dzialania; dane syntetyczne; '
                'kontrole nie wyprowadzaja dzialania z R1a-R1c', 'exact': {}, 'numerical': {}}

# Spodziewam się: tożsamości licznika działają na całej bazie operatorów,
# także po zmianie triady. Kontrola nie jest losowym dowodem.
pauli_basis = [I2] + sigma
for A in pauli_basis:
    lhs = scale(0, I2)
    for s in sigma:
        lhs = add(lhs, mul(mul(s, A), s))
    trace = A[0][0]+A[1][1]
    assert lhs == add(scale(2*trace, I2), scale(-1, A))
for i in range(4):
    for j in range(4):
        assert add(mul(gamma[i], gamma[j]), mul(gamma[j], gamma[i])) == \
            scale(2*metric[i] if i == j else 0, I4)
assert contraction(I4) == scale(4, I4)
for A in gamma:
    assert contraction(A) == scale(-2, A)
U = matrix([[F(3, 5), F(4, 5)], [-F(4, 5), F(3, 5)]])
assert mul(U, dagger(U)) == I2
rotated = gamma_from([mul(mul(U, s), dagger(U)) for s in sigma])
assert contraction(I4, rotated) == scale(4, I4)
for A in rotated:
    assert contraction(A, rotated) == scale(-2, A)
out['exact']['pauli_basis_and_clifford'] = True
out['exact']['triad_covariance'] = True

# Pełna tożsamość Wardowska na dwóch niezdegenerowanych wejściach.
ward_cases = [([3, F(1, 2), 0, F(2, 3)], [F(1, 3), F(1, 5), F(1, 4), 0], F(2, 5)),
              ([F(5, 2), 0, F(3, 4), F(1, 6)], [F(2, 3), 0, F(1, 7), F(1, 5)], F(1, 2))]
for p, k, eta in ward_cases:
    X = add(slash(p), scale(-eta, I4))
    Y = add(X, scale(-1, slash(k)))
    S = inverse(Y)
    left = mul(mul(slash(k), S), slash(k))
    right = add(add(mul(mul(X, S), X), scale(-1, X)), scale(-1, slash(k)))
    assert left == right
out['exact']['ward_identity'] = True

# Po połączeniu kanonicznych propagatorów wewnętrzny pęd ma wagę x.
kinetic = integrate_polynomial([0, -2])
mass = integrate_polynomial([4])
assert kinetic == -1 and mass == 4 and mass+kinetic == 3
# a_xi=-1+(1-xi); b_xi=4-(1-xi). Polinomy [stała, współczynnik xi].
a_xi = [F(-1)+1, F(-1)]
b_xi = [F(4)-1, F(1)]
assert [a+b for a, b in zip(a_xi, b_xi)] == [F(3), F(0)]
out['exact']['feynman_weights'] = {'kinetic': str(kinetic), 'mass': str(mass),
                                   'normalized_mass': str(mass+kinetic)}
out['exact']['gauge_polynomials'] = {'a_xi': list(map(str, a_xi)),
                                    'b_xi': list(map(str, b_xi)), 'sum': ['3', '0']}

# MS-bar: całka logarytmiczna daje 5, człon epsilon razy biegun daje -1.
# int ln(1-x)=-1; int x ln(1-x)=-3/4.
log_weight = F(4)*F(-1)-F(2)*F(-3, 4)
evanescent = integrate_polynomial([-2, 2])
finite = -2*log_weight+evanescent
assert log_weight == F(-5, 2) and evanescent == -1 and finite == 4
out['exact']['finite_matching'] = {'log_integral': str(log_weight),
                                  'log_contribution': str(-2*log_weight),
                                  'epsilon_times_pole': str(evanescent), 'total': str(finite)}

# Wagi UV z części kulombowskiej, Gaunta i odejmowanego rzutu podłużnego.
# Wszystkie całki z sqrt(y) zapisane przez t=sqrt(y).
parts = {
    'Coulomb': (F(0), integrate_polynomial([2, 0, -2]), integrate_polynomial([2])),
    'Gaunt': (-integrate_polynomial([3, -3]), integrate_polynomial([1, -1]),
              integrate_polynomial([3])),
    'spatial_projection': (integrate_polynomial([1, -1]),
                           -integrate_polynomial([1, 1])+integrate_polynomial([0, 0, 2]),
                           integrate_polynomial([-1]))}
total = tuple(sum((v[j] for v in parts.values()), F(0)) for j in range(3))
assert total == (F(-1), F(1), F(4))
for s in [F(0), F(1, 4), F(1), F(4), F(9)]:
    assert total[0]*(1+s)+total[1]*s+total[2] == 3
out['exact']['coulomb_pole_parts'] = {
    k: {'gamma0_frequency': str(v[0]), 'gamma_spatial': str(v[1]),
        'mass': str(v[2]), 'rest_mass_combination': str(v[0]+v[2])}
    for k, v in parts.items()}
out['exact']['coulomb_total'] = list(map(str, total))
out['exact']['wrong_omissions'] = {'mass_without_kinetic': '4',
                                  'without_spatial_projection_at_rest': '7/2',
                                  'without_epsilon_finite_term': '5'}

# Niezależna całka radialna po wykonaniu całki po częstości.
master_cases = []
for d1, d2 in [(1., 4.), (.25, 9.), (2., .5), (1., 1.), (.09, .7), (3., 5.)]:
    def radial(k):
        return k*k*((k*k+d1)**(-1.5)-(k*k+d2)**(-1.5))/(8*math.pi**2)
    direct = quad(radial, 0, math.inf, epsabs=5e-13, epsrel=5e-13, limit=250)[0]
    expected = math.log(d2/d1)/(16*math.pi**2)
    error = abs(direct-expected)
    assert error < 2e-12
    master_cases.append({'d1': d1, 'd2': d2, 'direct': direct, 'expected': expected, 'error': error})
out['numerical']['frequency_radial_master'] = master_cases

# Pełne jednopętlowe jądro, ze znakiem i0 oraz członem epsilon razy biegun.
L = math.log(4.)


def direct_integrals(z):
    def log_response(x):
        v = 1-z*x
        log_v = complex(math.log(abs(v)), -math.pi if v < 0 else 0.)
        return complex(L-math.log(1-x), 0.)-log_v
    cuts = [1/z] if z > 1 else None
    return qcomplex(log_response, 0, 1, cuts), qcomplex(lambda x: x*log_response(x), 0, 1, cuts)


def closed_integrals(z):
    if z == 0:
        return complex(L+1), complex(L/2+F(3, 4))
    if z == 1:
        return complex(L+2), complex(L/2+F(3, 2))
    v = 1-z
    log_v = complex(math.log(abs(v)), -math.pi if v < 0 else 0.)
    return (L+2+(1-z)/z*log_v,
            L/2+1+1/(2*z)+(1-z*z)/(2*z*z)*log_v)


kernel_cases = []
for z in [-3., 0., .4, .9, 1., 1.7, 4.]:
    i0, i1 = direct_integrals(z)
    j0, j1 = closed_integrals(z)
    a, b = -2*i1+1, 4*i0-2
    error = max(abs(i0-j0), abs(i1-j1))
    assert error < 2e-10
    if z == 1:
        assert abs(a+b-(4+3*L)) < 2e-10
    if z > 1:
        assert abs(a.imag+math.pi*(1-1/z**2)) < 2e-10
        assert abs(b.imag-4*math.pi*(1-1/z)) < 2e-10
    kernel_cases.append({'p2_over_eta2': z, 'a': {'re': a.real, 'im': a.imag},
                         'b': {'re': b.real, 'im': b.imag}, 'error': error})
out['numerical']['full_feynman_kernel'] = kernel_cases

# Z całego masowo odjętego jądra Coulomba na powłoce, również w innych ramach:
# (1+s) I0 - 3s I1 = 4s/3. Dowód całkowaniem przez części jest w raporcie.
coulomb_cases = []
for s in [0., .01, .25, 1., 9., 100.]:
    i0 = quad(lambda t: 2*math.log(1+s*(1-t*t)), 0, 1, epsabs=2e-12, epsrel=2e-12)[0]
    i1 = quad(lambda t: 2*t*t*math.log(1+s*(1-t*t)), 0, 1, epsabs=2e-12, epsrel=2e-12)[0]
    residual = 4*s/3-(1+s)*i0+3*s*i1
    assert abs(residual) < 3e-10
    coulomb_cases.append({'spatial_p2_over_eta2': s, 'I0': i0, 'I1': i1, 'mass_residual': residual})
out['numerical']['full_coulomb_on_shell_projection'] = coulomb_cases
out['max_errors'] = {
    'radial_master': max(r['error'] for r in master_cases),
    'full_feynman_integrals': max(r['error'] for r in kernel_cases),
    'coulomb_finite_mass_projection': max(abs(r['mass_residual']) for r in coulomb_cases)}
print(json.dumps(out, ensure_ascii=False, indent=2))
