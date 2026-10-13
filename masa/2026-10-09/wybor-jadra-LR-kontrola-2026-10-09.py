"""Kontrole kroku 263; Python 3, wyłącznie biblioteka standardowa.
Dokładne zespolone ułamki. Parametry syntetyczne, bez danych mas.
Primitives algebraiczne zachowane z kontroli 260; nowe testy dotyczą
pełnych źródeł drugiego rzędu i dodatniej reprezentacji spektralnej.
Dowody i zakres znajdują się w wybor-jadra-LR-2026-10-09.md.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import json


@dataclass(frozen=True)
class Z:
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "re", F(self.re))
        object.__setattr__(self, "im", F(self.im))

    @staticmethod
    def cast(x):
        return x if isinstance(x, Z) else Z(x)

    def __add__(self, x):
        x = self.cast(x)
        return Z(self.re + x.re, self.im + x.im)

    __radd__ = __add__

    def __neg__(self):
        return Z(-self.re, -self.im)

    def __sub__(self, x):
        return self + -self.cast(x)

    def __rsub__(self, x):
        return self.cast(x) + -self

    def __mul__(self, x):
        x = self.cast(x)
        return Z(self.re*x.re - self.im*x.im, self.re*x.im + self.im*x.re)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self.cast(x)
        n = x.re*x.re + x.im*x.im
        if not n:
            raise ZeroDivisionError("Dzielenie przez zero")
        return self * Z(x.re/n, -x.im/n)

    def conj(self):
        return Z(self.re, -self.im)


def mat(rows):
    return [[Z.cast(x) for x in row] for row in rows]


def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def scale(x, a):
    return [[Z.cast(x)*v for v in row] for row in a]


def add(*args):
    n, m = len(args[0]), len(args[0][0])
    assert all(len(a) == n and len(a[0]) == m for a in args)
    return [[sum((a[i][j] for a in args), Z()) for j in range(m)] for i in range(n)]


def mul(*args):
    out = args[0]
    for b in args[1:]:
        assert len(out[0]) == len(b)
        out = [[sum((out[i][k]*b[k][j] for k in range(len(b))), Z())
                for j in range(len(b[0]))] for i in range(len(out))]
    return out


def adj(a):
    return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a[0]))]


def inv(a):
    n = len(a)
    assert len(a[0]) == n
    out = [row[:] + unit for row, unit in zip(a, eye(n))]
    for i in range(n):
        k = next((j for j in range(i, n) if out[j][i] != Z()), None)
        if k is None:
            raise ValueError("Macierz osobliwa")
        out[i], out[k] = out[k], out[i]
        d = out[i][i]
        out[i] = [v/d for v in out[i]]
        for j in range(n):
            if j != i:
                d = out[j][i]
                out[j] = [v-d*w for v, w in zip(out[j], out[i])]
    result = [row[n:] for row in out]
    assert mul(a, result) == eye(n) and mul(result, a) == eye(n)
    return result


def det(a):
    out = [row[:] for row in a]
    value = Z(1)
    for i in range(len(a)):
        k = next((j for j in range(i, len(a)) if out[j][i] != Z()), None)
        if k is None:
            return Z()
        if i != k:
            out[i], out[k] = out[k], out[i]
            value = -value
        v = out[i][i]
        value *= v
        for j in range(i+1, len(a)):
            ratio = out[j][i]/v
            out[j] = [x-ratio*y for x, y in zip(out[j], out[i])]
    return value


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Z())


def block(a, b, c, d):
    return [ra+rb for ra, rb in zip(a, b)] + [rc+rd for rc, rd in zip(c, d)]


def split(a):
    return ([r[:2] for r in a[:2]], [r[2:] for r in a[:2]],
            [r[:2] for r in a[2:]], [r[2:] for r in a[2:]])


def pp(a):
    return [r[:2] for r in a[:2]]


I2, I4 = eye(2), eye(4)
O2 = scale(0, I2)
SIG = [mat([[0, 1], [1, 0]]), mat([[0, Z(0, -1)], [Z(0, 1), 0]]),
       mat([[1, 0], [0, -1]])]
GAM = [block(O2, I2, I2, O2)] + [block(O2, s, scale(-1, s), O2) for s in SIG]
MET = [1, -1, -1, -1]


def kron(a, b):
    return [[x*y for x in ra for y in rb] for ra in a for rb in b]


def sub(a, b):
    return add(a, scale(-1, b))


def comm(a, b):
    return sub(mul(a, b), mul(b, a))


def enc(x):
    x = Z.cast(x)
    return {'re': str(x.re), 'im': str(x.im)}


def reconstructed_inverse(a, b, m):
    r = inv(sub(mul(a, b), scale(m*m, I2)))
    return block(scale(m, r), mul(r, a), mul(b, r),
                 scale(F(1, 1)/m, sub(mul(b, r, a), I2)))


def d_reconstructed(a, b, ai, bi, r, ri, m):
    return block(scale(m, ri), add(mul(ri, a), mul(r, ai)),
                 add(mul(bi, r), mul(b, ri)),
                 scale(F(1, 1)/m, add(mul(bi, r, a), mul(b, ri, a), mul(b, r, ai))))


def dd_reconstructed(a, b, ai, bi, aj, bj, r, ri, rj, rij, m):
    return block(scale(m, rij), add(mul(rij, a), mul(ri, aj), mul(rj, ai)),
                 add(mul(bi, rj), mul(bj, ri), mul(b, rij)),
                 scale(F(1, 1)/m, add(mul(bi, rj, a), mul(bi, r, aj),
                     mul(bj, ri, a), mul(b, rij, a), mul(b, ri, aj),
                     mul(bj, r, ai), mul(b, rj, ai))))


def padd(a, b):
    return [((a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0)))
            for i in range(max(len(a), len(b)))]


def pscale(x, a):
    return [F(x)*y for y in a]


def pmul(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += F(x)*F(y)
    return out


def main():
    checks = {}
    for mu in range(4):
        for nu in range(4):
            assert add(mul(GAM[mu], GAM[nu]), mul(GAM[nu], GAM[mu])) == scale(
                2*MET[mu]*int(mu == nu), I4)
    checks['clifford_exact'] = 16

    # Noncommuting Pi_mu test the actual commutator term, not just free p^2.
    pi = [add(scale(2, I2), SIG[0]), SIG[1], SIG[2], add(I2, scale(F(1, 2), SIG[0]))]
    slash = add(*(kron(g, p) for g, p in zip(GAM, pi)))
    pi_sq = add(*(scale(MET[i], mul(pi[i], pi[i])) for i in range(4)))
    spin_term = add(*(scale(Z(0, F(-1, 2)), kron(
        scale(Z(0, F(1, 2)), comm(GAM[mu], GAM[nu])), comm(pi[mu], pi[nu])))
        for mu in range(4) for nu in range(4)))
    assert mul(slash, slash) == add(kron(I4, pi_sq), spin_term)
    assert spin_term != scale(0, eye(8))
    assert mul(slash, slash) != kron(I4, pi_sq)
    checks['pauli_term_noncommuting_8_by_8'] = True

    backgrounds = [
        (add(scale(4, I2), SIG[0], scale(F(1, 2), SIG[2])),
         add(scale(3, I2), SIG[1], scale(F(-1, 3), SIG[2])), F(1, 2)),
        (add(scale(5, I2), SIG[1], scale(F(2, 3), SIG[2])),
         add(scale(2, I2), SIG[0], scale(F(1, 4), SIG[1])), F(2)),
        (add(scale(3, I2), SIG[2], scale(F(1, 5), SIG[0])),
         add(scale(4, I2), SIG[0], scale(F(-1, 2), SIG[1])), F(3, 2)),
    ]
    variations = [(I2, I2)] + [(s, scale(-1, s)) for s in SIG]
    counts = {'full_inverse': 0, 'determinant': 0, 'first_source_response': 0,
              'second_source_response': 0, 'first_logdet': 0, 'second_logdet': 0,
              'missing_seagull_detected': 0}
    witness = None
    for a, b, m in backgrounds:
        d = block(scale(-m, I2), a, b, scale(-m, I2))
        g = inv(d)
        q = sub(mul(a, b), scale(m*m, I2))
        r = inv(q)
        assert g == reconstructed_inverse(a, b, m)
        counts['full_inverse'] += 1
        assert det(d) == det(scale(-1, q))
        counts['determinant'] += 1
        # Missing local source contact changes the full RR response by I/m.
        wrong = block(scale(m, r), mul(r, a), mul(b, r), scale(1/m, mul(b, r, a)))
        assert wrong != g
        assert sub(wrong, g) == block(O2, O2, O2, scale(1/m, I2))
        for ai, bi in variations:
            di = block(O2, ai, bi, O2)
            qi = add(mul(ai, b), mul(a, bi))
            ri = scale(-1, mul(r, qi, r))
            gi = scale(-1, mul(g, di, g))
            assert gi == d_reconstructed(a, b, ai, bi, r, ri, m)
            counts['first_source_response'] += 1
            assert trace(mul(g, di)) == trace(mul(r, qi))
            counts['first_logdet'] += 1
            for aj, bj in variations:
                dj = block(O2, aj, bj, O2)
                qj = add(mul(aj, b), mul(a, bj))
                qij = add(mul(ai, bj), mul(aj, bi))
                rj = scale(-1, mul(r, qj, r))
                rij = add(mul(r, qi, r, qj, r), mul(r, qj, r, qi, r),
                          scale(-1, mul(r, qij, r)))
                gij = add(mul(g, di, g, dj, g), mul(g, dj, g, di, g))
                assert gij == dd_reconstructed(a, b, ai, bi, aj, bj, r, ri, rj, rij, m)
                counts['second_source_response'] += 1
                full_logdet = -trace(mul(g, dj, g, di))
                reduced_logdet = trace(sub(mul(r, qij), mul(r, qj, r, qi)))
                assert full_logdet == reduced_logdet
                counts['second_logdet'] += 1
                without_seagull = -trace(mul(r, qj, r, qi))
                if without_seagull != full_logdet:
                    counts['missing_seagull_detected'] += 1
                    if witness is None:
                        witness = {'full': enc(full_logdet), 'without_contact': enc(without_seagull)}
    assert witness is not None
    checks['second_order_equivalence'] = counts
    checks['missing_two_insertion_contact_witness'] = witness

    # A=1, B=s+3/16: both poles have positive squared mass but one weight is negative.
    r1, r2 = F(1, 16), F(9, 16)
    d = padd([0, 1], pscale(-1, pmul([F(3, 16), 1], [F(3, 16), 1])))
    assert d == pscale(-1, pmul([-r1, 1], [-r2, 1]))
    # Numerators of 2/(s-r1) - 2/(s-r2) and the corresponding scalar term.
    assert padd(pscale(-2, [-r2, 1]), pscale(2, [-r1, 1])) == [F(1), F(0)]
    assert padd(pscale(F(-1, 2), [-r2, 1]), pscale(F(3, 2), [-r1, 1])) == [F(3, 16), F(1)]
    checks['higher_derivative_signed_spectrum'] = {
        'A': '1', 'B': 's+3/16', 'masses': ['1/4', '3/4'], 'vector_weights': ['2', '-2']}

    # Positive two-atom diagnostic; not a new particle model for the project.
    # Fv=(s-5/2)/D, Fs=(3s/2-3)/D, D=(s-1)(s-4).
    den = pmul([-1, 1], [-4, 1])
    nv, ns = [F(-5, 2), 1], [-3, F(3, 2)]
    invden = padd(pmul([0, 1], pmul(nv, nv)), pscale(-1, pmul(ns, ns)))
    assert invden == pmul(den, [F(-9, 4), 1])
    checks['positive_nonpolynomial_inverse'] = {
        'vector_weights': ['1/2', '1/2'], 'mass_squared': ['1', '4'],
        'A': '(s-5/2)/(s-9/4)', 'B': '(3*s/2-3)/(s-9/4)',
        'limit_x_times_h': '1'}

    # Sanity check for the degree inequality; the proof for all degrees is in the report.
    surviving = []
    for n in range(9):
        for m in range(-1, 9):  # -1 denotes the zero polynomial B.
            exponent = n + 1 - max(2*n+1, 2*m)
            if exponent >= 0:
                surviving.append((n, m))
    assert surviving == [(0, -1), (0, 0)]
    checks['degree_sanity_check_not_a_proof'] = {'cases': 90, 'surviving': surviving}
    checks['scope'] = ('Exact algebra and synthetic witnesses; not selection of polynomiality, '
                       'vacuum, source map, EM transverse coupling or masses from R1a.')
    out = {'status': 'PASS', 'arithmetic': 'exact rational complex, no tolerances', 'checks': checks}
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()


