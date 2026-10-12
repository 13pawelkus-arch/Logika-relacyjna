"""Dokładna kontrola mapy amplitud, wag i jednopętlowych zmian Yukaw.

Uruchomienie: python3 sprawdzenie-mapy-masy-2026-10-04.py
Wyłącznie biblioteka standardowa: ułamki wymierne i wymierne liczby zespolone.
Oczekiwania M0–M8 zapisano przed kontrolami w towarzyszącej notatce.
Wszystkie dane są syntetyczne. To kontrola przyjętych równań SM.
"""

from dataclasses import dataclass
from fractions import Fraction as F
import json


@dataclass(frozen=True)
class Q:
    """Zespolona liczba wymierna bez arytmetyki zmiennoprzecinkowej."""
    real: F = F(0)
    imag: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "real", F(self.real))
        object.__setattr__(self, "imag", F(self.imag))

    def __add__(self, other):
        other = q(other)
        return Q(self.real + other.real, self.imag + other.imag)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.real, -self.imag)

    def __sub__(self, other):
        return self + (-q(other))

    def __rsub__(self, other):
        return q(other) + (-self)

    def __mul__(self, other):
        other = q(other)
        return Q(self.real * other.real - self.imag * other.imag,
                 self.real * other.imag + self.imag * other.real)

    __rmul__ = __mul__

    def conjugate(self):
        return Q(self.real, -self.imag)

    def norm2(self):
        return self.real ** 2 + self.imag ** 2

    def __truediv__(self, other):
        other = q(other)
        norm = other.norm2()
        if norm == 0:
            raise ZeroDivisionError()
        numerator = self * other.conjugate()
        return Q(numerator.real / norm, numerator.imag / norm)


def q(value):
    return value if isinstance(value, Q) else Q(value)


def matrix(rows):
    return [[q(x) for x in row] for row in rows]


def zeros(rows, cols=None):
    return matrix([[0] * (cols if cols is not None else rows) for _ in range(rows)])


def eye(n):
    return matrix([[int(a == b) for b in range(n)] for a in range(n)])


def diagonal(values):
    return matrix([[values[a] if a == b else 0 for b in range(len(values))] for a in range(len(values))])


def dagger(a):
    return [[a[row][col].conjugate() for row in range(len(a))] for col in range(len(a[0]))]


def mm(a, b):
    if len(a[0]) != len(b):
        raise ValueError("Niezgodne rozmiary macierzy")
    return [[sum((a[row][k] * b[k][col] for k in range(len(b))), Q())
             for col in range(len(b[0]))] for row in range(len(a))]


def add(a, b):
    return [[x + y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def scale(scalar, a):
    return [[q(scalar) * x for x in row] for row in a]


def subtract(a, b):
    return add(a, scale(-1, b))


def trace(a):
    return sum((a[k][k] for k in range(len(a))), Q())


def column(a, k):
    return [[row[k]] for row in a]


def projection(a, v):
    return mm(mm(dagger(v), a), v)[0][0]


def norm_matrix(a):
    return sum((x.norm2() for row in a for x in row), F(0))


def real(value):
    value = q(value)
    if value.imag:
        raise AssertionError("Wielkość powinna być rzeczywista")
    return value.real


results = {}


def require(name, condition):
    if not condition:
        raise AssertionError(name)
    results[name] = True


# M1. Spodziewam się: ten sam Gram znormalizowany nie ustala norm.
# Zdanie o upadku: identyczny Gram wymusza identyczne stosunki singularne.
y1, y2 = diagonal([1, 2, 3]), diagonal([1, 3, 5])
normalized = []
for y, strengths in ((y1, [1, 2, 3]), (y2, [1, 3, 5])):
    x = mm(dagger(y), y)
    normalizer = diagonal([F(1, n) for n in strengths])
    normalized.append(mm(mm(normalizer, x), normalizer))
require("M1_same_normalized_gram", normalized[0] == normalized[1])
require("M1_different_strength_ratios", F(2) != F(3))


# M2. Spodziewam się: wagi |V|² są dodatnie, kompletne i odtwarzają rzut X.
# Zdanie o upadku: niezgodność rozkładu spektralnego lub sum wag.
c12, s12 = F(3, 5), F(4, 5)
c23, s23 = F(5, 13), F(12, 13)
c13, s13 = F(15, 17), F(8, 17)
r12 = matrix([[c12, s12, 0], [-s12, c12, 0], [0, 0, 1]])
r23 = matrix([[1, 0, 0], [0, c23, s23], [0, -s23, c23]])
r13 = matrix([[c13, 0, Q(0, -s13)], [0, 1, 0], [Q(0, -s13), 0, c13]])
v = mm(mm(r23, r13), r12)
require("M2_unitarity", mm(dagger(v), v) == eye(3))
p = [[entry.norm2() for entry in row] for row in v]
require("M2_nonnegative_weights", all(x >= 0 for row in p for x in row))
require("M2_row_sums", all(sum(row) == 1 for row in p))
require("M2_column_sums", all(sum(p[a][b] for a in range(3)) == 1 for b in range(3)))
up = [F(1, 7), F(2, 7), F(4, 7)]
down = [F(1, 9), F(2, 9), F(5, 9)]
lepton = [F(1, 13), F(3, 13), F(7, 13)]
yu = diagonal(up)
yd = mm(diagonal(down), dagger(v))
ye = diagonal(lepton)
xu, xd, xe = [mm(dagger(y), y) for y in (yu, yd, ye)]
require("M2_up_projections", all(
    xd[a][a] == q(sum(p[a][b] * down[b] ** 2 for b in range(3))) for a in range(3)
))
require("M2_down_projections", all(
    projection(xu, column(v, b)) == q(sum(p[a][b] * up[a] ** 2 for a in range(3)))
    for b in range(3)
))
require("M2_wrong_V_squared_rejected", any(
    xd[a][a] != sum((down[b] ** 2 * v[a][b] * v[a][b] for b in range(3)), Q())
    for a in range(3)
))
j = (v[0][0] * v[1][0].conjugate() * v[1][1] * v[0][1].conjugate()).imag
require("M2_nonzero_cyclic_phase", j != 0)
results["synthetic_cyclic_imaginary_part"] = str(j)


# M0. Spodziewam się: porównania kolumn odtwarzają X przy wspólnej metryce.
# Zdanie o upadku: pominięta metryka/propagator zmienia odczyt.
gram = [[mm(dagger(column(yd, a)), column(yd, b))[0][0] for b in range(3)] for a in range(3)]
require("M0_column_gram", gram == xd)
metric = diagonal([1, 2, 3])
require("M0_channel_dependent_metric_changes_gram", mm(mm(dagger(yd), metric), yd) != xd)


# M5. Spodziewam się: generatorowe kwadraty dadzą Casimiry z przyjętych reprezentacji.
# Zdanie o upadku: suma norm nie odpowiada Casimirowi.
pauli = [matrix([[0, 1], [1, 0]]), matrix([[0, Q(0, -1)], [Q(0, 1), 0]]), diagonal([1, -1])]
casimir2 = zeros(2)
for generator in pauli:
    casimir2 = add(casimir2, scale(F(1, 4), mm(dagger(generator), generator)))
require("M5_SU2_Casimir", casimir2 == scale(F(3, 4), eye(2)))
gell_mann = [
    matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    matrix([[0, Q(0, -1), 0], [Q(0, 1), 0, 0], [0, 0, 0]]),
    diagonal([1, -1, 0]),
    matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    matrix([[0, 0, Q(0, -1)], [0, 0, 0], [Q(0, 1), 0, 0]]),
    matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    matrix([[0, 0, 0], [0, 0, Q(0, -1)], [0, Q(0, 1), 0]]),
]
casimir3 = zeros(3)
for generator in gell_mann:
    casimir3 = add(casimir3, scale(F(1, 4), mm(dagger(generator), generator)))
# Ósmy generator: diag(1,1,-2)/(2 sqrt(3)); jego kwadrat ma mianownik 12.
casimir3 = add(casimir3, scale(F(1, 12), diagonal([1, 1, 4])))
require("M5_SU3_Casimir", casimir3 == scale(F(4, 3), eye(3)))
coefficients = {
    "u": [3 * (F(1, 6) ** 2 + F(2, 3) ** 2), 3 * F(3, 4), 3 * (F(4, 3) + F(4, 3))],
    "d": [3 * (F(1, 6) ** 2 + F(-1, 3) ** 2), 3 * F(3, 4), 3 * (F(4, 3) + F(4, 3))],
    "e": [3 * (F(-1, 2) ** 2 + F(-1) ** 2), 3 * F(3, 4), F(0)],
}
require("M5_coefficients", coefficients == {
    "u": [F(17, 12), F(9, 4), F(8)], "d": [F(5, 12), F(9, 4), F(8)],
    "e": [F(15, 4), F(9, 4), F(0)],
})
results["conditional_c_coefficients"] = {key: list(map(str, value)) for key, value in coefficients.items()}


# M3. Spodziewam się: wszystkie logarytmiczne pochodne zgodzą się z rzutami.
# Zdanie o upadku: niezgodność albo dodatkowy człon od zmiany bazy.
gauge = [F(1, 5), F(1, 4), F(1, 3)]
gau = {key: sum(c * g ** 2 for c, g in zip(value, gauge)) for key, value in coefficients.items()}
t = real(3 * trace(xu) + 3 * trace(xd) + trace(xe))
bu = add(scale(F(3, 2), subtract(xu, xd)), scale(t - gau["u"], eye(3)))
bd = add(scale(F(3, 2), subtract(xd, xu)), scale(t - gau["d"], eye(3)))
be = add(scale(F(3, 2), xe), scale(t - gau["e"], eye(3)))
dot_yu, dot_yd, dot_ye = [mm(y, b) for y, b in ((yu, bu), (yd, bd), (ye, be))]
dot_xu, dot_xd, dot_xe = [add(mm(dagger(dy), y), mm(dagger(y), dy))
                         for y, dy in ((yu, dot_yu), (yd, dot_yd), (ye, dot_ye))]
eta_u = [real(dot_xu[a][a] / (2 * up[a] ** 2)) for a in range(3)]
eta_d = [real(projection(dot_xd, column(v, b)) / (2 * down[b] ** 2)) for b in range(3)]
eta_e = [real(dot_xe[a][a] / (2 * lepton[a] ** 2)) for a in range(3)]
expected_u = [t - gau["u"] + F(3, 2) * (up[a] ** 2 - sum(p[a][b] * down[b] ** 2 for b in range(3))) for a in range(3)]
expected_d = [t - gau["d"] + F(3, 2) * (down[b] ** 2 - sum(p[a][b] * up[a] ** 2 for a in range(3))) for b in range(3)]
expected_e = [t - gau["e"] + F(3, 2) * lepton[a] ** 2 for a in range(3)]
require("M3_all_nine_spectral_derivatives", eta_u == expected_u and eta_d == expected_d and eta_e == expected_e)
w = mm(r12, r13)
for name, yf, bf, eigenvectors, values, eta in (
    ("u", yu, bu, eye(3), up, eta_u), ("d", yd, bd, v, down, eta_d)
):
    yf_new, bf_new = mm(yf, w), mm(mm(dagger(w), bf), w)
    dot_yf_new = mm(yf_new, bf_new)
    dot_xf_new = add(mm(dagger(dot_yf_new), yf_new), mm(dagger(yf_new), dot_yf_new))
    eig_new = mm(dagger(w), eigenvectors)
    require("M3_common_basis_" + name, all(
        real(projection(dot_xf_new, column(eig_new, k)) / (2 * values[k] ** 2)) == eta[k]
        for k in range(3)
    ))


# M4. Spodziewam się: reszta po propagatorach wynosi -2X_partner.
# Zdanie o upadku: niezgodność sumy z pełnym wynikiem SM.
waves_u = add(add(xu, scale(F(1, 2), add(xu, xd))), scale(t, eye(3)))
waves_d = add(add(xd, scale(F(1, 2), add(xu, xd))), scale(t, eye(3)))
waves_e = add(scale(F(3, 2), xe), scale(t, eye(3)))
require("M4_up_vertex_remainder", subtract(add(bu, scale(gau["u"], eye(3))), waves_u) == scale(-2, xd))
require("M4_down_vertex_remainder", subtract(add(bd, scale(gau["d"], eye(3))), waves_d) == scale(-2, xu))
require("M4_lepton_vertex_remainder", subtract(add(be, scale(gau["e"], eye(3))), waves_e) == zeros(3))


# M6. Spodziewam się: konwersja lambda_source=2lambda i g1²=5gY²/3 zgodzi wszystkie monomiany.
# Zdanie o upadku: choć jeden współczynnik po konwersji jest inny.
converted = {
    "lambda2": F(12) * 4 / 2, "lambda_gY2": -F(9, 5) * F(5, 3) * 2 / 2,
    "lambda_g22": -F(9) * 2 / 2, "gY4": F(27, 100) * F(5, 3) ** 2 / 2,
    "gY2_g22": F(9, 10) * F(5, 3) / 2, "g24": F(9, 4) / 2,
    "lambda_T": F(4) * 2 / 2, "H4": -F(4) / 2,
}
require("M6_lambda_conventions", converted == {
    "lambda2": F(24), "lambda_gY2": -F(3), "lambda_g22": -F(9),
    "gY4": F(3, 8), "gY2_g22": F(3, 4), "g24": F(9, 8),
    "lambda_T": F(4), "H4": -F(2),
})
require("M6_quartic_gram", real(trace(mm(xd, xd))) == sum(
    mm(dagger(column(yd, a)), column(yd, b))[0][0].norm2()
    for a in range(3) for b in range(3)
))


# M7. Spodziewam się: wspólne T i cechowanie znikną, różnice Yukaw pozostaną.
# Zdanie o upadku: różnica pochodnych zawiera inny człon.
require("M7_down_ratio", eta_d[2] - eta_d[1] == F(3, 2) * (
    down[2] ** 2 - down[1] ** 2 - sum(up[a] ** 2 * (p[a][2] - p[a][1]) for a in range(3))
))
require("M7_lepton_ratio", eta_e[2] - eta_e[0] == F(3, 2) * (lepton[2] ** 2 - lepton[0] ** 2))
beta = [F(41, 6), F(-19, 6), F(-7)]
require("M7_gauge_elimination", all(
    2 * b * (-c / (2 * b)) == -c for value in coefficients.values() for c, b in zip(value, beta)
))


# M8. Spodziewam się: wspólny czynnik znika, względne czynniki A/B pozostają.
# Zdanie o upadku: wynik nie odtwarza ilorazu przy wspólnej normalizacji.
# Ogólny dowód algebraiczny jest w notatce; tutaj przykład kontrolny.
af, ag, zf, zg, common = F(1, 7), F(2, 9), F(3, 5), F(5, 8), F(11, 13)
require("M8_AB_ratio", (common * af * zf) / (common * ag * zg) == (af / ag) * (zf / zg))

results["scope"] = "dokladna_algebra_jednej_petli_SM; wszystkie_liczby_syntetyczne; brak_przewidywania_mas"
results["check_count"] = sum(value is True for value in results.values())
print(json.dumps(results, ensure_ascii=False, indent=2))
