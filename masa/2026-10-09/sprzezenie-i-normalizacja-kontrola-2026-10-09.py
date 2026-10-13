"""Dokładne kontrole kroku 260, tylko biblioteka standardowa Python 3.

Parametry syntetyczne. Nie wybierają mas ani działania z ramy.
Macierze zawierają dokładne zespolone liczby wymierne, bez tolerancji.
Kontrole porównują pełną odwrotność i wstawki z niezależnym rachunkiem
zredukowanego jądra. Dowód dla wszystkich argumentów znajduje się w raporcie.
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
SIGMA = [mat([[0, 1], [1, 0]]), mat([[0, Z(0, -1)], [Z(0, 1), 0]]),
         mat([[1, 0], [0, -1]])]
GL = [I2] + [scale(-1, a) for a in SIGMA]
GR = [I2] + SIGMA
GAMMA = [block(a, O2, O2, b) for a, b in zip(GL, GR)]


def sigma(p):
    return add(*(scale(x, a) for x, a in zip(p, SIGMA)))


def kernel(point, m):
    w, p = point
    s = sigma(p)
    l, f = add(scale(w, I2), s), add(scale(w, I2), scale(-1, s))
    b = scale(-m, I2)
    return block(l, b, b, f)


def schur(k):
    a, b, c, f = split(k)
    r = inv(f)
    s = add(a, scale(-1, mul(b, r, c)))
    left = [ra+rb for ra, rb in zip(I2, scale(-1, mul(b, r)))]
    right = I2 + scale(-1, mul(r, c))
    return s, r, left, right


def vertex(left_point, right_point, m, mu):
    rk = inv(split(kernel(left_point, m))[3])
    rp = inv(split(kernel(right_point, m))[3])
    return add(GL[mu], scale(m*m, mul(rk, GR[mu], rp)))


def contract(q, tensors):
    return add(scale(q[0], tensors[0]),
               *(scale(-q[i+1], tensors[i+1]) for i in range(3)))


def wdiff(k, p):
    return [k[0]-p[0]] + [a-b for a, b in zip(k[1], p[1])]


# Pełne odczyty 3D: każda składowa p i sigma_y pozostają w rachunku.
POINTS = [
    (Z(3), (F(1, 3), F(2, 5), F(-1, 4))),
    (Z(4), (F(-2, 3), F(1, 5), F(3, 7))),
    (Z(F(5, 2)), (F(2, 7), F(-3, 8), F(1, 2))),
    (Z(3, F(1, 2)), (F(3, 5), F(-1, 7), F(2, 9))),
]
MASSES = [F(0), F(1, 3), F(1), F(2)]


def run():
    counts = {}
    nprop = nward = nresponse = nsecond = 0
    for m in MASSES:
        data = []
        for p in POINTS:
            k = kernel(p, m)
            g = inv(k)
            s, r, left, right = schur(k)
            ge = inv(s)
            assert ge == pp(g)
            w, mom = p
            d = w*w-sum((Z(x)*x for x in mom), Z())-m*m
            assert ge == scale(Z(1)/d, split(k)[3])
            nprop += 1
            data.append((k, g, s, r, left, right, ge))
        for ki, kpoint in enumerate(POINTS):
            kk, gk, sk, rk, lk, ek, gek = data[ki]
            for pi, ppoint in enumerate(POINTS):
                kp, gp, sp, rp, lp, ep, gep = data[pi]
                v = [vertex(kpoint, ppoint, m, mu) for mu in range(4)]
                for mu in range(4):
                    assert v[mu] == mul(lk, GAMMA[mu], ep)
                    assert mul(gek, v[mu], gep) == pp(mul(gk, GAMMA[mu], gp))
                    nresponse += 1
                assert contract(wdiff(kpoint, ppoint), v) == add(sk, scale(-1, sp))
                assert contract(wdiff(kpoint, ppoint), GAMMA) == add(kk, scale(-1, kp))
                nward += 1

        # Dwie wstawki: wszystkie 16 par typów przy różnych k,l,p.
        for ki, kpoint in enumerate(POINTS):
            pi, li = (ki+1) % len(POINTS), (ki+2) % len(POINTS)
            ppoint, lpoint = POINTS[pi], POINTS[li]
            kk, gk, sk, rk, lk, ek, gek = data[ki]
            kp, gp, sp, rp, lp, ep, gep = data[pi]
            kl, gl, sl, rl, ll, el, gel = data[li]
            for mu in range(4):
                for nu in range(4):
                    # Jedna kolejność fotonów. Druga wynika z zamiany mu,nu
                    # i argumentu pośredniego, nie z obcięcia propagatora.
                    contact = scale(m*m, mul(rk, GR[mu], rl, GR[nu], rp))
                    vkl = vertex(kpoint, lpoint, m, mu)
                    vlp = vertex(lpoint, ppoint, m, nu)
                    reduced = add(mul(gek, vkl, gel, vlp, gep),
                                  mul(gek, contact, gep))
                    full = pp(mul(gk, GAMMA[mu], gl, GAMMA[nu], gp))
                    assert reduced == full
                    nsecond += 1
    counts.update(propagators=nprop, ward_pairs=nward,
                  one_insertion_components=nresponse, ordered_two_insertion_components=nsecond)

    # Cały wyznacznik: odpowiedź zamkniętego rachunku fermionowego.
    # To kontrole macierzowych integrandów, bez sumy po modach lub pętli.
    nloop = 0
    for m in MASSES:
        for p in POINTS:
            k = kernel(p, m)
            g = inv(k)
            s, r, left, right = schur(k)
            ge = inv(s)
            assert det(k) == det(split(k)[3])*det(s)
            for mu in range(4):
                vmu = vertex(p, p, m, mu)
                for nu in range(4):
                    vnu = vertex(p, p, m, nu)
                    contact = scale(m*m, add(mul(r, GR[mu], r, GR[nu], r),
                                             mul(r, GR[nu], r, GR[mu], r)))
                    full = trace(mul(g, GAMMA[mu], g, GAMMA[nu]))
                    closed_r = trace(mul(r, GR[mu], r, GR[nu]))
                    reduced = trace(mul(ge, vmu, ge, vnu)) + trace(mul(ge, contact))
                    assert full == closed_r + reduced
                    nloop += 1
    counts["determinant_factorizations"] = 16
    counts["closed_two_insertion_integrands"] = nloop

    point = (Z(3), (0, 0, 0))
    k = kernel(point, F(1))
    g = inv(k)
    s, r, left, right = schur(k)
    ge = inv(s)
    v = vertex(point, point, F(1), 0)
    contact = scale(2, mul(r, r, r))
    assert trace(mul(g, g)) == Z(F(5, 8))
    assert trace(mul(r, r)) == Z(F(2, 9))
    assert trace(mul(ge, contact)) == Z(F(1, 18))
    assert trace(mul(ge, v, ge, v)) == Z(F(25, 72))
    counts["closed_response_example"] = {
        "full": "5/8", "eliminated_determinant": "2/9",
        "reduced_vertices": "25/72", "induced_contact": "1/18",
        "without_eliminated_determinant": "29/72"
    }

    # Dowolne końce w obu kanałach: zachować źródła i bezpośredni człon Q.
    src = mat([[1], [Z(F(2, 3), F(1, 4))], [F(-2, 5)], [Z(0, F(3, 7))]])
    eff = mat([[Z(F(1, 7), F(1, 5))], [F(3, 4)], [Z(2, F(-1, 2))], [F(2, 9)]])
    for m in MASSES:
        for p in POINTS:
            k = kernel(p, m)
            s, r, left, right = schur(k)
            a, b, c, f = split(k)
            jp, jq = src[:2], src[2:]
            fp, fq = adj(eff[:2]), adj(eff[2:])
            je = add(jp, scale(-1, mul(b, r, jq)))
            fe = add(fp, scale(-1, mul(fq, r, c)))
            assert mul(adj(eff), inv(k), src) == add(mul(fe, inv(s), je), mul(fq, r, jq))
    counts["full_endpoint_amplitudes"] = 16

    # Dowolne bloki wierzchołka: przypadek z off-diagonalnymi wstawkami.
    arbitrary = mat([[1, Z(0, 1), F(1, 2), F(-2, 3)],
                     [2, F(-1, 4), Z(1, 1), F(3, 7)],
                     [F(2, 5), F(-1, 2), 3, Z(0, -1)],
                     [Z(F(1, 3), F(1, 2)), 1, F(-3, 2), 2]])
    va, vb, vc, vf = split(arbitrary)
    for kpoint in POINTS:
        for ppoint in POINTS:
            kk, kp = kernel(kpoint, F(2)), kernel(ppoint, F(2))
            sk, rk, lk, ek = schur(kk)
            sp, rp, lp, ep = schur(kp)
            ak, bk, ck, fk = split(kk)
            ap, bp, cp, fp = split(kp)
            ve = add(va, scale(-1, mul(vb, rp, cp)),
                     scale(-1, mul(bk, rk, vc)), mul(bk, rk, vf, rp, cp))
            assert ve == mul(lk, arbitrary, ep)
            assert mul(inv(sk), ve, inv(sp)) == pp(mul(inv(kk), arbitrary, inv(kp)))
    counts["arbitrary_block_vertices"] = 16

    # Test skończonej kowariancji: macierz reprezentuje zmianę faz końców,
    # nie przestrzenną kratę. Oba projektory komutują z transformacją.
    k = kernel(POINTS[3], F(1))
    gphase = mat([[Z(F(3, 5), F(4, 5)), 0], [0, Z(F(5, 13), F(12, 13))]])
    gfull = block(gphase, O2, O2, gphase)
    kg = mul(gfull, k, adj(gfull))
    s, r, left, right = schur(k)
    sg = schur(kg)[0]
    assert sg == mul(gphase, s, adj(gphase))
    assert inv(sg) == mul(gphase, inv(s), adj(gphase))
    counts["finite_endpoint_covariance"] = 2

    # Dokładna normalizacja pełnych modów masowych, na różnych p 3D.
    # Wybrano wymierne wektory spełniające w^2=p^2+m^2.
    shell = [(F(1), (F(0), F(0), F(0)), F(1)),
             (F(3), (F(2), F(2), F(0)), F(1)),
             (F(5), (F(2), F(2), F(4)), F(1)),
             (F(13), (F(3), F(4), F(0)), F(12))]
    spinors = [mat([[1], [0]]), mat([[F(3, 5)], [Z(0, F(4, 5))]])]
    charge = F(-1)
    for w, mom, m in shell:
        point = (Z(w), mom)
        k = kernel(point, m)
        s, r, left, right = schur(k)
        n = add(I2, scale(m*m, mul(r, r)))
        v0 = vertex(point, point, m, 0)
        assert n == mul(adj(right), right) and v0 == n
        for u in spinors:
            psi = mul(right, u)
            assert mul(k, psi) == scale(0, psi)
            norm = mul(adj(psi), psi)[0][0]
            assert norm == mul(adj(u), n, u)[0][0]
            assert mul(adj(u), scale(charge, v0), u)[0][0]/norm == Z(charge)
    counts["on_shell_norm_and_charge"] = 8

    # Odwrócona kolejność: stary wierzchołek po pełnej redukcji nie wystarcza.
    p, k = (Z(3), (0, 0, 0)), (Z(4), (0, 0, 0))
    correct = vertex(k, p, F(1), 0)
    sp, sk = schur(kernel(p, F(1)))[0], schur(kernel(k, F(1)))[0]
    assert correct == scale(F(13, 12), I2)
    assert add(sk, scale(-1, sp), scale(-1, I2)) == scale(F(1, 12), I2)
    counts["bare_vertex_ward_violation"] = "1/12 * I2"
    counts["rest_correct_charge"] = "Q"
    counts["rest_bare_charge_with_full_norm"] = "Q/2"
    rest = (Z(1), (0, 0, 0))
    s, r, left, right = schur(kernel(rest, F(1)))
    u = mat([[1], [0]])
    norm = mul(adj(mul(right, u)), mul(right, u))[0][0]
    assert norm == Z(2)
    assert mul(adj(u), scale(charge, vertex(rest, rest, F(1), 0)), u)[0][0]/norm == Z(charge)
    assert mul(adj(u), scale(charge, I2), u)[0][0]/norm == Z(charge/2)

    # Na s=0 eliminacja R jest osobliwa, ale pełna odwrotność jest regularna.
    point = (Z(1), (F(0), F(0), F(1)))
    k = kernel(point, F(2))
    projected = pp(inv(k))
    assert projected == scale(F(-1, 4), split(k)[3])
    try:
        schur(k)
    except ValueError:
        pass
    else:
        raise AssertionError("Oczekiwano osobliwego bloku R")
    counts["singular_elimination_regular_full_response"] = 1

    # Przy eta=0 pełny kontakt i poprawka wierzchołka znikają.
    for kpoint in POINTS:
        for ppoint in POINTS:
            for mu in range(4):
                assert vertex(kpoint, ppoint, F(0), mu) == GL[mu]
    counts["zero_mass_vertex_limits"] = 64

    result = {"status": "PASS", "arithmetic": "exact Gaussian rationals",
              "synthetic": True, "checks": counts,
              "scope": "Fixed canonical L/R kernel and EM insertion; no loop integral, no mass inference, no derivation of the full relation from the frame."}
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
