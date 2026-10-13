"""Dokladne kontrole przyporzadkowania jader i wag, 09.10.2026.

Python 3, tylko biblioteka standardowa. Liczby sa syntetyczne.
Kontrole sprawdzaja wskazane tozsamosci, nie wybor dzialania z calej ramy.
Zadnej rodziny diagnostycznej nie przypisujemy statusu nowej fizycznej teorii.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial
import json

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


def dot(p, k):
    return sum((F(metric[i])*F(p[i])*F(k[i]) for i in range(4)), F(0))


def norm2(z):
    return z.re*z.re+z.im*z.im


def determinant(A):
    rows = [row[:] for row in A]
    det = C(1)
    for i in range(len(A)):
        pivot = next((j for j in range(i, len(A)) if rows[j][i] != C()), None)
        if pivot is None:
            return C()
        if pivot != i:
            rows[i], rows[pivot] = rows[pivot], rows[i]
            det = -det
        value = rows[i][i]
        det *= value
        for j in range(i+1, len(A)):
            ratio = rows[j][i]/value
            rows[j] = [v-ratio*w for v, w in zip(rows[j], rows[i])]
    return det


records = {}

# Transport po dwoch drogach, cztery rozne konwencje faz koncow.
edges = {(3, 1): C(F(3, 5), F(4, 5)),
         (1, 0): C(F(5, 13), F(12, 13)),
         (3, 2): C(F(7, 25), F(24, 25)),
         (2, 0): C(F(3, 5), F(-4, 5))}
gauges = [C(F(3, 5), F(-4, 5)), C(0, 1),
          C(F(5, 13), F(-12, 13)), C(F(7, 25), F(24, 25))]
assert all(norm2(v) == 1 for v in [*edges.values(), *gauges])
changed = {(x, y): gauges[x]*u*gauges[y].conj() for (x, y), u in edges.items()}
paths = [edges[3, 1]*edges[1, 0], edges[3, 2]*edges[2, 0]]
paths_g = [changed[3, 1]*changed[1, 0], changed[3, 2]*changed[2, 0]]
assert all(ug == gauges[3]*u*gauges[0].conj() for u, ug in zip(paths, paths_g))
assert paths[0]*paths[1].conj() == paths_g[0]*paths_g[1].conj()
psi0, psi3 = C(F(5, 13), F(12, 13)), C(F(3, 5), F(4, 5))
amp = psi3.conj()*(paths[0]+2*paths[1])*psi0
amp_g = (gauges[3]*psi3).conj()*(paths_g[0]+2*paths_g[1])*(gauges[0]*psi0)
assert amp == amp_g
# Znormalizowane przygotowanie (1,2)/sqrt(5) oraz efekt (1,1)/sqrt(2).
prob = norm2(paths[0]+2*paths[1])/10
assert 0 <= prob <= 1 and prob == norm2(paths_g[0]+2*paths_g[1])/10
records['link_gauge_covariance'] = {'exact': True, 'unequal_weights': ['1', '2'],
                                    'probability': str(prob)}

# Ogolne chiralne jadro i odwrotnosc uzyskana niezaleznie eliminacja Gaussa.
dirac_cases = [([3, 1, 0, 1], F(2, 3), F(5, 4), F(1, 3), F(4, 7)),
               ([1, 2, 1, 0], F(7, 5), F(3, 2), F(2, 5), F(3, 7)),
               ([2, 1, 1, 0], F(9, 8), F(4, 5), F(5, 6), F(7, 9))]
for p, aL, aR, bL, bR in dirac_cases:
    pbar, pmatrix = [row[2:] for row in slash(p)[:2]], [row[:2] for row in slash(p)[2:]]
    s = dot(p, p)
    assert mul(pbar, pmatrix) == scale(s, I2)
    D = block(scale(-bL, I2), scale(aR, pbar), scale(aL, pmatrix), scale(-bR, I2))
    N = block(scale(bR, I2), scale(aR, pbar), scale(aL, pmatrix), scale(bL, I2))
    denominator = s*aL*aR-bL*bR
    assert denominator
    expected = scale(1/denominator, N)
    assert inverse(D) == expected
    assert mul(D, expected) == I4 and mul(expected, D) == I4
    assert determinant(D) == C(denominator**2)
records['chiral_kernel_inverse'] = {'exact': True, 'cases': len(dirac_cases)}

# Poprzeczne jadro EM i odwrotnosc po ustaleniu cechowania.
photon_cases = [([3, 1, 1, 0], F(3, 5), F(7, 4)),
                ([1, 2, 0, 1], F(7, 3), F(5, 6)),
                ([2, 0, 1, 0], F(-2, 3), F(9, 5))]
g = matrix([[metric[i]*int(i == j) for j in range(4)] for i in range(4)])
for p, xi, h in photon_cases:
    s = dot(p, p)
    lower = [metric[i]*F(p[i]) for i in range(4)]
    K = matrix([[h*(lower[i]*lower[j]-s*metric[i]*int(i == j))
                 for j in range(4)] for i in range(4)])
    assert all(sum((F(p[i])*K[i][j] for i in range(4)), C()) == C() for j in range(4))
    gf = matrix([[-h/xi*lower[i]*lower[j] for j in range(4)] for i in range(4)])
    Kfixed = add(K, gf)
    Gupper = matrix([[-F(1)/(h*s)*(metric[i]*int(i == j)-(1-xi)*F(p[i])*F(p[j])/s)
                     for j in range(4)] for i in range(4)])
    assert mul(Kfixed, Gupper) == I4
    assert inverse(Kfixed) == Gupper
records['photon_transversality_and_inverse'] = {'exact': True, 'cases': len(photon_cases)}

# Pelne funkcje w tozsamosci Wardowskiej; takze rowne niezmienniki i q=0.
# Wspolczynniki sa kontrolnymi ulamkami, nie fizycznymi funkcjami QED.
coeffs = [(F(1), F(2, 7), F(1, 13), F(3, 5), F(-1, 11), F(1, 17)),
          (F(1), F(0), F(0), F(2, 3), F(0), F(0))]
momentum_pairs = [([3, 1, 0, 1], [2, 0, 1, 0]),
                  ([2, 1, 0, 0], [2, 0, 1, 0]),
                  ([1, 2, 1, 0], [3, 1, 2, 0]),
                  ([2, 1, 0, 0], [2, 1, 0, 0])]
charges = [F(1), F(-1, 3)]
ward_count, diagonal_count, transverse_count = 0, 0, 0
for a0, a1, a2, b0, b1, b2 in coeffs:
    def Aval(s): return a0+a1*s+a2*s*s
    def Bval(s): return b0+b1*s+b2*s*s
    for k, p in momentum_pairs:
        sk, sp = dot(k, k), dot(p, p)
        # Divided differences polynomials: regular even when sk == sp.
        dA, dB = a1+a2*(sk+sp), b1+b2*(sk+sp)
        scalar_sum = scale(F(1, 2), add(slash(k), slash(p)))
        second = add(scale(dA, scalar_sum), scale(-dB, I4))
        for Q in charges:
            V = [scale(Q, add(scale((Aval(sk)+Aval(sp))/2, gamma[mu]),
                             scale(k[mu]+p[mu], second))) for mu in range(4)]
            q = [F(k[i])-F(p[i]) for i in range(4)]
            contraction = scale(0, I4)
            for mu in range(4): contraction = add(contraction, scale(metric[mu]*q[mu], V[mu]))
            Dk = add(scale(Aval(sk), slash(k)), scale(-Bval(sk), I4))
            Dp = add(scale(Aval(sp), slash(p)), scale(-Bval(sp), I4))
            assert contraction == scale(Q, add(Dk, scale(-1, Dp)))
            ward_count += 1
            if k == p:
                jet = add(scale(a1+2*a2*sp, slash(p)), scale(-(b1+2*b2*sp), I4))
                for mu in range(4):
                    derivative = scale(Q, add(scale(Aval(sp), gamma[mu]), scale(2*p[mu], jet)))
                    assert V[mu] == derivative
                diagonal_count += 1
            # Antysymetria niezalezna od funkcji A,B i Q.
            T = []
            for mu in range(4):
                component = scale(0, I4)
                for nu in range(4):
                    comm = add(mul(gamma[mu], gamma[nu]), scale(-1, mul(gamma[nu], gamma[mu])))
                    component = add(component, scale(C(0, F(1, 2))*metric[nu]*q[nu], comm))
                T.append(component)
            summed = scale(0, I4)
            for mu in range(4): summed = add(summed, scale(metric[mu]*q[mu], T[mu]))
            assert summed == scale(0, I4)
            if any(q): assert any(t != scale(0, I4) for t in T)
            # Niezerowa zmiana V nie narusza tej samej tozsamosci.
            new_contraction = scale(0, I4)
            for mu in range(4):
                new_contraction = add(new_contraction, scale(metric[mu]*q[mu], add(V[mu], scale(F(2, 5), T[mu]))))
            assert new_contraction == contraction
            transverse_count += 1
records['ward_full_functions'] = {'exact': True, 'cases': ward_count,
                                  'diagonal_limits': diagonal_count,
                                  'transverse_checks': transverse_count}

# Normalizacja pol: dwa zestawy wspolczynnikow, to samo eta oraz e.
normalizations = [(F(25), F(9), F(3, 2), F(3, 5), F(3)),
                  (F(49), F(25), F(147, 50), F(1), F(5))]
normalized = []
for zpsi, za, mass, e0, sqrtza in normalizations:
    assert sqrtza*sqrtza == za
    eta, e = mass/zpsi, e0/sqrtza
    canonical_vertex = zpsi*e0/zpsi/sqrtza
    assert canonical_vertex == e
    normalized.append((eta, e, e*e))
assert normalized[0] == normalized[1]
records['field_normalization'] = {'exact': True, 'eta': str(normalized[0][0]),
                                   'e': str(normalized[0][1]), 'four_pi_alpha': str(normalized[0][2])}

# Rodzina wag tego samego obiegu. Dokladny szereg do rzedu szostego.
s_series = {2: F(1, 2), 4: F(-1, 24), 6: F(1, 720)}
square = {}
for i, a in s_series.items():
    for j, b in s_series.items(): square[i+j] = square.get(i+j, F(0))+a*b
weights = []
for lam in [F(0), F(1, 2), F(1)]:
    series = {i: s_series.get(i, F(0))+lam*square.get(i, F(0)) for i in [2, 4, 6]}
    hessian = factorial(2)*series[2]
    fourth = factorial(4)*series[4]
    assert hessian == 1 and fourth == -1+6*lam
    weights.append({'lambda': str(lam), 'hessian': str(hessian),
                    'fourth_derivative': str(fourth), 'value_at_pi_over_two': str(1+lam)})
assert len({x['value_at_pi_over_two'] for x in weights}) == 3
records['same_hessian_different_loop_weights'] = {'exact': True, 'beta': '1', 'cases': weights}

# Ten sam komutator modu; rozne przygotowania maja inne korelatory.
# N=1 mozna zrealizowac przez stan quasi-free z geometrycznymi wagami obsadzen.
phase = C(F(3, 5), F(-4, 5))
commutators, correlators = [], []
for N in [F(0), F(1)]:
    greater = (N+1)*phase+N*phase.conj()
    lesser = (N+1)*phase.conj()+N*phase
    commutators.append(greater-lesser)
    correlators.append(greater)
assert commutators[0] == commutators[1] and correlators[0] != correlators[1]
records['same_mode_commutator_different_correlators'] = {'exact': True,
                                                        'greater': [{'re': str(v.re), 'im': str(v.im)} for v in correlators]}

print(json.dumps({'scope': 'Kontrole algebry i zakresu przeslanek; nie wybor dzialania z calej ramy; dane syntetyczne',
                  'status': 'PASS', 'exact': records}, ensure_ascii=False, indent=2))

