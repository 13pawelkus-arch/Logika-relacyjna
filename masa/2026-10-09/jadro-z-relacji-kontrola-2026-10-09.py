"""Dokladna kontrola kroku 259: jadro i wagi z jednej pelnej relacji.

Python 3, tylko biblioteka standardowa. Parametry sa syntetyczne.
Dowody dla wszystkich argumentow sa w raporcie; kontrola nie wybiera teorii.
Wyjscie JSON powstaje obok tego skryptu.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
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
        return C(self.re + x.re, self.im + x.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, x):
        return self + -self.cast(x)

    def __rsub__(self, x):
        return self.cast(x) + -self

    def __mul__(self, x):
        x = self.cast(x)
        return C(self.re*x.re - self.im*x.im, self.re*x.im + self.im*x.re)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self.cast(x)
        norm = x.re*x.re + x.im*x.im
        if not norm:
            raise ZeroDivisionError('Gaussian rational division by zero')
        return self*C(x.re/norm, -x.im/norm)

    def conj(self):
        return C(self.re, -self.im)


def matrix(rows):
    return [[C.cast(x) for x in row] for row in rows]


def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def add(A, B):
    assert len(A) == len(B) and len(A[0]) == len(B[0])
    return [[a+b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def scale(x, A):
    return [[C.cast(x)*a for a in row] for row in A]


def mul(A, B):
    assert len(A[0]) == len(B)
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), C())
             for j in range(len(B[0]))] for i in range(len(A))]


def dagger(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def inverse(A):
    n = len(A)
    rows = [row[:] + unit for row, unit in zip(A, eye(n))]
    for i in range(n):
        pivot = next((j for j in range(i, n) if rows[j][i] != C()), None)
        if pivot is None:
            raise ValueError('Singular matrix')
        rows[i], rows[pivot] = rows[pivot], rows[i]
        value = rows[i][i]
        rows[i] = [v/value for v in rows[i]]
        for j in range(n):
            if j != i:
                value = rows[j][i]
                rows[j] = [v-value*w for v, w in zip(rows[j], rows[i])]
    return [row[n:] for row in rows]


def rank(A):
    rows = [r[:] for r in A]
    i = 0
    for k in range(len(A[0])):
        pivot = next((j for j in range(i, len(A)) if rows[j][k] != C()), None)
        if pivot is None:
            continue
        rows[i], rows[pivot] = rows[pivot], rows[i]
        value = rows[i][k]
        rows[i] = [v/value for v in rows[i]]
        for j in range(i+1, len(A)):
            value = rows[j][k]
            rows[j] = [v-value*w for v, w in zip(rows[j], rows[i])]
        i += 1
        if i == len(rows):
            break
    return i


def determinant(A):
    rows = [r[:] for r in A]
    value = C(1)
    for i in range(len(A)):
        pivot = next((j for j in range(i, len(A)) if rows[j][i] != C()), None)
        if pivot is None:
            return C()
        if pivot != i:
            rows[i], rows[pivot] = rows[pivot], rows[i]
            value = -value
        entry = rows[i][i]
        value *= entry
        for j in range(i+1, len(A)):
            ratio = rows[j][i]/entry
            rows[j] = [v-ratio*w for v, w in zip(rows[j], rows[i])]
    return value


def block(A, B, C0, D):
    return [ra+rb for ra, rb in zip(A, B)] + [rc+rd for rc, rd in zip(C0, D)]


def blocks(U):
    return ([r[:2] for r in U[:2]], [r[2:] for r in U[:2]],
            [r[:2] for r in U[2:]], [r[2:] for r in U[2:]])


def kron(A, B):
    return [[a*b for a in ra for b in rb] for ra in A for rb in B]


def power(A, n):
    out = eye(len(A))
    for _ in range(n):
        out = mul(out, A)
    return out


def cpow(z, n):
    out = C(1)
    for _ in range(n):
        out *= z
    return out


def trace(A):
    return sum((A[i][i] for i in range(len(A))), C())


def norm2(z):
    return z.re*z.re + z.im*z.im


def horizontal(parts):
    return [sum((part[i] for part in parts), []) for i in range(len(parts[0]))]


def gram_blocks(blocks0):
    return [sum((b[i] for b in blockrow), [])
            for blockrow in blocks0 for i in range(len(blockrow[0]))]


I2, I4 = eye(2), eye(4)
Z2 = scale(0, I2)
SIGMA = [matrix([[0, 1], [1, 0]]),
         matrix([[0, C(0, -1)], [C(0, 1), 0]]),
         matrix([[1, 0], [0, -1]])]
PS = matrix([[0, 0, 0, 0], [0, F(1, 2), F(-1, 2), 0],
             [0, F(-1, 2), F(1, 2), 0], [0, 0, 0, 0]])
PT = add(I4, scale(-1, PS))
POINTS = [C(), C(F(1, 3)), C(F(1, 4), F(1, 3)), C(F(-1, 2)), C(0, F(1, 2))]


def transfer(U, z):
    A, B, C0, D = blocks(U)
    X = mul(inverse(add(I2, scale(-z, D))), C0)
    return add(A, scale(z, mul(B, X))), X


def defect(Tw, Tz):
    return add(I2, scale(-1, mul(dagger(Tw), Tz)))


def check_unitary_response(U, expected_rank):
    assert mul(dagger(U), U) == I4 and mul(U, dagger(U)) == I4
    data = [transfer(U, z) for z in POINTS]
    pick = []
    for i, w in enumerate(POINTS):
        row = []
        for j, z in enumerate(POINTS):
            Tw, Xw = data[i]
            Tz, Xz = data[j]
            delta = 1 - w.conj()*z
            assert defect(Tw, Tz) == scale(delta, mul(dagger(Xw), Xz))
            row.append(scale(C(1)/delta, defect(Tw, Tz)))
        pick.append(row)
    E = horizontal([X for _, X in data])
    P = gram_blocks(pick)
    assert P == mul(dagger(E), E) and rank(P) == expected_rank
    A, B, C0, D = blocks(U)
    assert rank(horizontal([mul(power(D, n), C0) for n in range(4)])) == expected_rank
    # Independent impulse propagation in the full four-dimensional process.
    x = C0
    for n in range(6):
        out = mul(U, Z2+x)
        assert out[:2] == mul(mul(B, power(D, n)), C0)
        x = out[2:]
    # Telescoping conservation for nonstationary preparations.
    inputs = [matrix([[1], [C(0, F(1, 3))]]),
              matrix([[F(-1, 2)], [C(F(2, 7), F(1, 5))]]),
              matrix([[C(0, F(3, 4))], [F(4, 9)]]),
              matrix([[0], [0]])]
    x = matrix([[0], [0]])
    norm_in, norm_out = C(), C()
    for v in inputs:
        out = mul(U, v+x)
        y, x = out[:2], out[2:]
        norm_in += trace(mul(dagger(v), v))
        norm_out += trace(mul(dagger(y), y))
        assert norm_in == norm_out + trace(mul(dagger(x), x))
    # A nontrivial hidden basis rotation preserves the full complex response.
    W = matrix([[F(3, 5), F(4, 5)], [F(-4, 5), F(3, 5)]])
    V = block(I2, Z2, Z2, W)
    U2 = mul(mul(V, U), dagger(V))
    assert mul(dagger(U2), U2) == I4
    for z, (Tz, Xz) in zip(POINTS, data):
        T2, X2 = transfer(U2, z)
        assert T2 == Tz and X2 == mul(W, Xz)
    return {'gram_pairs': 25, 'pick_size': 10, 'reachable_rank': expected_rank,
            'impulse_coefficients': 6, 'norm_telescoping_steps': 4,
            'hidden_basis_response_checks': 5}


def check_schur(H, expected_rank):
    assert dagger(H) == H
    A, B, Bt, Ch = blocks(H)
    assert Bt == dagger(B)
    zetas = [C(2), C(-1), C(F(1, 3), F(1, 2)), C(0, 1), C(F(3, 2), F(1, 4))]
    upper_count = 0
    for z in zetas:
        Rq = inverse(add(scale(z, I2), scale(-1, Ch)))
        S = mul(mul(B, Rq), dagger(B))
        D = add(add(scale(z, I2), scale(-1, A)), scale(-1, S))
        full = inverse(add(scale(z, I4), scale(-1, H)))
        assert inverse(D) == [r[:2] for r in full[:2]]
        if z.im > 0:
            ImS = scale(C(0, F(-1, 2)), add(S, scale(-1, dagger(S))))
            realdiff = add(scale(z.re, I2), scale(-1, Ch))
            positive = add(mul(realdiff, realdiff), scale(z.im*z.im, I2))
            expected = scale(-z.im, mul(mul(B, inverse(positive)), dagger(B)))
            assert ImS == expected
            # These controls use diagonal Ch, so the sign is also checked exactly.
            assert Ch[0][1] == Ch[1][0] == C()
            for j in range(2):
                assert positive[j][j].im == 0 and positive[j][j].re > 0
            upper_count += 1
    moments = [mul(mul(B, power(Ch, n)), dagger(B)) for n in range(7)]
    hankel = gram_blocks([[moments[i+j] for j in range(4)] for i in range(4)])
    E = horizontal([mul(power(Ch, n), dagger(B)) for n in range(4)])
    assert hankel == mul(dagger(E), E) and rank(hankel) == expected_rank
    return {'projected_inverse_checks': 5, 'upper_half_plane_checks': upper_count,
            'hankel_size': 8, 'hankel_rank': expected_rank}


def run():
    results = {'status': 'PASS', 'arithmetic': 'exact Gaussian rationals; no tolerance',
               'scope': 'synthetic operator identities, not selection of QED from the frame'}
    assert mul(PS, PS) == PS and trace(PS) == C(1)
    # Solve the commutation constraints on the entire operator space, not samples.
    Js = [scale(F(1, 2), add(kron(s, I2), kron(I2, s))) for s in SIGMA]
    basis = [matrix([[int(i == a and j == b) for j in range(4)] for i in range(4)])
             for a in range(4) for b in range(4)]
    constraints = []
    for J in Js:
        images = [add(mul(E, J), scale(-1, mul(J, E))) for E in basis]
        constraints.extend([[img[i][j] for img in images]
                            for i in range(4) for j in range(4)])
    assert rank(constraints) == 14
    pscol = [[entry] for row in PS for entry in row]
    ptcol = [[entry] for row in PT for entry in row]
    assert rank(horizontal([pscol, ptcol])) == 2
    assert mul(constraints, pscol) == [[C()] for _ in constraints]
    assert mul(constraints, ptcol) == [[C()] for _ in constraints]
    # Requiring H to annihilate the singlet fixes the singlet block to zero.
    images = [mul(E, PS) for E in basis]
    sharp = constraints+[[img[i][j] for img in images] for i in range(4) for j in range(4)]
    assert rank(sharp) == 15 and mul(sharp, ptcol) == [[C()] for _ in sharp]
    results['isotropic_operator_classification'] = {'operator_coefficients': 16,
        'commutation_equations': 48, 'constraint_rank': 14,
        'solution_basis': ['P_s', 'P_t'], 'sharp_singlet_constraint_rank': 15,
        'sharp_solution_basis': ['P_t'],
        'scope': 'common-rotation invariant operators on exactly two carriers'}
    for s in SIGMA:
        part1, part2 = scale(F(1, 2), kron(s, I2)), scale(F(1, 2), kron(I2, s))
        J = add(part1, part2)
        assert mul(J, PS) == scale(0, I4)
        assert trace(mul(PS, power(part1, 2))) == C(F(1, 4))
        assert trace(mul(PS, power(part2, 2))) == C(F(1, 4))
        assert trace(mul(PS, mul(part1, part2))) == C(F(-1, 4))
    results['sharp_singlet_constraints'] = 3
    q_values = [C(0, 1), C(F(3, 5), F(4, 5))]
    results['singlet_relations'] = []
    for q in q_values:
        assert norm2(q) == 1
        U = add(PS, scale(q, PT))
        assert mul(U, PS) == PS
        for s in SIGMA:
            J = scale(F(1, 2), add(kron(s, I2), kron(I2, s)))
            assert mul(U, J) == mul(J, U)
        record = check_unitary_response(U, 1)
        a = (q+1)/2
        for z in POINTS:
            T, _ = transfer(U, z)
            assert T == matrix([[q, 0], [0, (a-q*z)/(1-a*z)]])
        for z in [C(1), C(-1), C(0, 1)]:
            T, _ = transfer(U, z)
            assert mul(dagger(T), T) == I2
        T, _ = transfer(U, C(1))
        assert T == matrix([[q, 0], [0, 1]])
        rho_plus = matrix([[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]])
        out = mul(mul(T, rho_plus), dagger(T))
        p = trace(mul(rho_plus, out))
        assert p == C((1+q.re)/2)
        record['q'] = {'re': str(q.re), 'im': str(q.im)}
        record['boundary_probability_plus'] = str(p.re)
        record['boundary_unitarity_checks'] = 3
        results['singlet_relations'].append(record)
    # A fully reachable two-channel realization also satisfies the entire Gram test.
    Ag = matrix([[F(3, 5), 0], [0, F(5, 13)]])
    Bg = matrix([[F(-4, 5), 0], [0, F(-12, 13)]])
    Cg = scale(-1, Bg)
    results['full_reachability_control'] = check_unitary_response(block(Ag, Bg, Cg, Ag), 2)
    # Deliberately invalid reweighting; assertions verify the exact failure.
    U = add(PS, scale(C(0, 1), PT))
    A, B, C0, D = blocks(U)
    bad_values = {}
    for z in [C(1), C(F(4, 5))]:
        excursion = mul(mul(B, inverse(add(I2, scale(-z, D)))), C0)
        bad = add(A, scale(2*z, excursion))
        bad_values[z.re] = bad[1][1]
    assert bad_values[F(1)] == C(F(3, 2), F(-1, 2))
    assert norm2(bad_values[F(1)]) == F(5, 2)
    assert bad_values[F(4, 5)] == C(F(29, 26), F(-11, 26))
    assert 1-norm2(bad_values[F(4, 5)]) == F(-143, 338)
    results['reweighting_rejected'] = {'boundary_probability': '5/2',
                                      'disk_norm_deficit': '-143/338'}
    # Every individual reading is contractive, but the three-point Gram is impossible.
    zs = [C(), C(F(1, 2)), C(0, F(1, 2))]
    ts = [z.conj() for z in zs]
    pick = [[(1-ts[i].conj()*ts[j])/(1-zs[i].conj()*zs[j])
             for j in range(3)] for i in range(3)]
    assert all(norm2(t) <= 1 for t in ts)
    assert determinant(pick) == C(F(-4, 17))
    results['joint_readings_rejected'] = {'individual_norms_ok': True,
                                          'three_point_determinant': '-4/17'}
    # Hermitian bridge, both singlet-compatible and full-rank coupling.
    assert mul(PT, PS) == scale(0, I4)
    results['singlet_generator_schur'] = check_schur(PT, 1)
    for z in [C(2), C(-1), C(F(1, 3), F(1, 2)), C(0, 1)]:
        full = inverse(add(scale(z, I4), scale(-1, PT)))
        assert full[1][1] == (z-C(F(1, 2)))/(z*(z-C(1)))
        assert full[1][1] == (C(1)/z+C(1)/(z-C(1)))/2
    half_inverse = inverse(add(scale(F(1, 2), I4), scale(-1, PT)))
    assert half_inverse[1][1] == C()  # Full resolvent regular at the elimination pole.
    results['two_pole_decomposition'] = {'checks': 4, 'residues': ['1/2', '1/2'],
                                         'full_resolvent_at_half': '0'}
    Ah = matrix([[1, C(0, F(1, 3))], [C(0, F(-1, 3)), F(-2, 5)]])
    Bh = matrix([[F(1, 3), C(0, F(1, 5))], [F(2, 7), F(3, 4)]])
    Ch = matrix([[F(-1, 2), 0], [0, F(2, 3)]])
    Hg = block(Ah, Bh, dagger(Bh), Ch)
    results['full_rank_generator_schur'] = check_schur(Hg, 2)
    residues = []
    for j, lam in enumerate([F(-1, 2), F(2, 3)]):
        projector = matrix([[int(i == j and k == j) for k in range(2)] for i in range(2)])
        W = mul(mul(Bh, projector), dagger(Bh))
        col = [[row[j]] for row in Bh]
        assert W == mul(col, dagger(col)) and rank(W) == 1
        assert trace(W).im == 0 and trace(W).re > 0
        residues.append((lam, W))
    for z in [C(2), C(0, 1), C(F(1, 3), F(1, 2))]:
        S = mul(mul(Bh, inverse(add(scale(z, I2), scale(-1, Ch)))), dagger(Bh))
        spectral = Z2
        for lam, W in residues:
            spectral = add(spectral, scale(C(1)/(z-C(lam)), W))
        assert S == spectral
    results['spectral_residue_gram_checks'] = 2
    results['spectral_sum_checks'] = 3
    return results


if __name__ == '__main__':
    output = run()
    output_path = Path(__file__).with_suffix('.json')
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(output, ensure_ascii=False, indent=2))
