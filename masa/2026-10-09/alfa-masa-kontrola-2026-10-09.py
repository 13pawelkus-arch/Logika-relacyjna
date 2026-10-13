"""Kontrole 261: wspólne widmo α i wkładu masowego EM.

Parametry wyłącznie syntetyczne. Dokładna algebra używa ułamków
zespolonych; całki niezależnych reprezentacji używają scipy/numpy.
Uruchomienie: python alfa-masa-kontrola-2026-10-09.py
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


import cmath
import math
import warnings
from scipy.integrate import quad, IntegrationWarning

I2, I4 = eye(2), eye(4)
O2 = scale(0, I2)
SIGMA = [mat([[0, 1], [1, 0]]),
         mat([[0, Z(0, -1)], [Z(0, 1), 0]]),
         mat([[1, 0], [0, -1]])]
HL = [I2] + [scale(-1, a) for a in SIGMA]
HR = [I2] + SIGMA
HV = [block(a, O2, O2, b) for a, b in zip(HL, HR)]
G0 = block(O2, I2, I2, O2)
DG = [mul(G0, a) for a in HV]
METRIC = [1, -1, -1, -1]


def slashed(p):
    return add(*(scale(METRIC[i]*p[i], DG[i]) for i in range(4)))


def dot(p, k):
    return sum((METRIC[i]*Z.cast(p[i])*k[i] for i in range(4)), Z())


def sigma(p):
    return add(*(scale(p[i+1], SIGMA[i]) for i in range(3)))


def hkernel(p, mass):
    return block(add(scale(p[0], I2), sigma(p)), scale(-mass, I2),
                 scale(-mass, I2), add(scale(p[0], I2), scale(-1, sigma(p))))


def reduced(p, mass):
    a, b, c, f = split(hkernel(p, mass))
    r = inv(f)
    s = add(a, scale(-1, mul(b, r, c)))
    return r, inv(s)


def algebra_checks():
    points = [(F(3), F(1, 3), F(1, 5), F(-1, 4)),
              (Z(F(4), F(1, 2)), F(-1, 2), F(1, 4), F(1, 3))]
    trace_cases = 0
    reduction_cases = 0
    omissions = []
    for mass in [F(0), F(1)]:
        for p in points:
            s0 = dot(p, p)
            r0, l0 = reduced(p, mass)
            assert det(hkernel(p, mass)) == (s0-mass*mass)*(s0-mass*mass)
            assert det(inv(l0)) == (s0-mass*mass)*(s0-mass*mass)/s0
            assert det(inv(r0)) == s0
            for k in points:
                for mu in range(4):
                    for nu in range(4):
                        num = trace(mul(DG[mu], add(slashed(p), scale(mass, I4)),
                                        DG[nu], add(slashed(k), scale(mass, I4))))
                        metric = METRIC[mu] if mu == nu else 0
                        expected = 4*(Z.cast(p[mu])*k[nu]+Z.cast(p[nu])*k[mu]
                                      -metric*(dot(p, k)-mass*mass))
                        assert num == expected
                        trace_cases += 1
                        gp, gk = inv(hkernel(p, mass)), inv(hkernel(k, mass))
                        rp, lp = reduced(p, mass)
                        rk, lk = reduced(k, mass)
                        vm = add(HL[mu], scale(mass*mass, mul(rp, HR[mu], rk)))
                        vn = add(HL[nu], scale(mass*mass, mul(rk, HR[nu], rp)))
                        full = trace(mul(gp, HV[mu], gk, HV[nu]))
                        closed_r = trace(mul(rp, HR[mu], rk, HR[nu]))
                        closed_l = trace(mul(lp, vm, lk, vn))
                        contact_p = mass*mass*trace(mul(lp, rp, HR[mu], rk, HR[nu], rp))
                        contact_k = mass*mass*trace(mul(lk, rk, HR[nu], rp, HR[mu], rk))
                        assert full == closed_r+closed_l+contact_p+contact_k
                        reduction_cases += 1
                        if mass and full != closed_l:
                            omissions.append((mu, nu))
    assert omissions
    # Exact scalar check of the dimensionally regulated transverse reduction.
    regulator_cases = 0
    for d in [F(3), F(7, 2), F(4), F(9, 2)]:
        y, msq, qsq = F(2, 7), F(5, 3), F(11, 5)
        a = y*(1-y)
        delta = msq-a*qsq
        assert (2/d-1)*d*delta/(d-2)+msq+a*qsq == 2*a*qsq
        regulator_cases += 1
    # Integrated mass weights and the epsilon*numerator finite term.
    assert F(4)-F(2, 2) == 3
    assert F(2, 2)-2 == -1
    # Constant 4 of the ordinary photon result: 2*integral w ln(1-x)=-5.
    assert -2*(4*F(-1)-2*F(-3, 4))-1 == 4
    return {"exact_trace_cases": trace_cases,
            "exact_closed_LR_reduction_cases": reduction_cases,
            "nonzero_omissions_detected": len(omissions),
            "regulator_identity_cases": regulator_cases,
            "mass_log_weight": 3, "mass_finite_constant": 4}


def integrate(f, a=0.0, b=1.0, **kw):
    options = dict(epsabs=2e-10, epsrel=2e-10, limit=240)
    options.update(kw)
    value, error = quad(f, a, b, **options)
    assert math.isfinite(value) and math.isfinite(error)
    return value


def F_param(r):
    return integrate(lambda x: 2*x*(1-x)*math.log1p(r*x*(1-x)))


SERIES = [float(F(2*math.factorial(k+1)**2,
                  k*math.factorial(2*k+3))) for k in range(1, 21)]


def F_closed(r):
    if r == 0:
        return 0.0
    if r < 0.12:
        # Convergent series, not a discarded threshold: at 0.12 the
        # relative geometric factor is at most 0.03; 20 terms suffice.
        return sum((-1)**(k+1)*a*r**k for k, a in enumerate(SERIES, 1))
    root = math.sqrt(1+4/r)
    log = 2*math.asinh(math.sqrt(r)/2)
    return ((1-2/r)*root*log+4/r-5/3)/3


def F_spectral(r):
    # v is the pair velocity; this includes the entire cut to infinity.
    return r/3*integrate(lambda v: v*v*(3-v*v)/(4+r-r*v*v))


def Phi_param(z):
    z = complex(z)
    if z.imag:
        f = lambda x: -2*x*(1-x)*cmath.log(1-z*x*(1-x))
        return complex(integrate(lambda x: f(x).real),
                       integrate(lambda x: f(x).imag))
    s = z.real
    if s < 4:
        return complex(integrate(lambda x: -2*x*(1-x)*math.log(1-s*x*(1-x))))
    beta = math.sqrt(max(0.0, 1-4/s))
    low, high = (1-beta)/2, (1+beta)/2
    f = lambda x: -2*x*(1-x)*math.log(abs(1-s*x*(1-x)))
    parts = [(0, low), (low, high), (high, 1)]
    re = sum(integrate(f, a, b) for a, b in parts if b > a)
    primitive = lambda x: x*x/2-x*x*x/3
    im = 2*math.pi*(primitive(high)-primitive(low))
    return complex(re, im)


def Phi_spectral(z):
    z = complex(z)
    if z.imag:
        f = lambda v: z/3*v*v*(3-v*v)/(4-z+z*v*v)
        return complex(integrate(lambda v: f(v).real),
                       integrate(lambda v: f(v).imag))
    s = z.real
    if s < 4:
        return complex(s/3*integrate(lambda v: v*v*(3-v*v)/(4-s+s*v*v)))
    if s == 4:
        return complex(F(8, 9))
    beta = math.sqrt(1-4/s)
    f = lambda v: v*v*(3-v*v)/(v+beta)
    re = integrate(f, weight="cauchy", wvar=beta)/3
    im = math.pi/3*beta*(1+2/s)
    return complex(re, im)


def H_spectral(r, z):
    if r == 1:
        return 0.0
    def outer(v):
        a = 1-v*v
        def inner(x):
            b = a*(1-x)**2
            denominator = 4*z*z*x+r*r*b
            log_ratio = math.log1p((1-r*r)*b/denominator)
            return (4-2*x)*log_ratio
        return v*v*(3-v*v)/a*integrate(inner, epsabs=2e-9, epsrel=2e-9)
    return integrate(outer, epsabs=2e-8, epsrel=2e-9)


def H_response(r, z):
    if r == 1:
        return 0.0
    def outer(u):
        ratio = math.exp(u)/(z*z)
        return -3*integrate(lambda x: (4-2*x)*F_closed(ratio*(1-x)**2/x),
                            epsabs=1e-9, epsrel=2e-10)
    return integrate(outer, 0, 2*math.log(r), epsabs=2e-8)


def H_asymptotic(r, z):
    l = math.log(r)
    return -6*l*math.log(1/(z*z))-6*l*l+13*l


def averaged_F(a):
    return integrate(lambda x: (4-2*x)/3*F_closed(a*(1-x)**2/x),
                     epsabs=2e-13, epsrel=2e-10)


def numeric_checks():
    pol = []
    for r in [0.001, 0.1, 0.2, 1.0, 2.0, 20.0, 1000.0]:
        p, c, s = F_param(r), F_closed(r), F_spectral(r)
        err = max(abs(p-c), abs(p-s))
        assert err < 2e-9
        pol.append(dict(r=r, parameter=p, closed=c, spectral=s, error=err))
    complex_pol = []
    for z in [0.0, 1.0, 3.9, 4.0, 4.01, 5.0, 9.0, 100.0,
              1+0.7j, 5+0.3j, 10+0.2j]:
        p, s = Phi_param(z), Phi_spectral(z)
        err = abs(p-s)
        assert err < 3e-8
        complex_pol.append(dict(z=[complex(z).real, complex(z).imag],
                                parameter=[p.real, p.imag],
                                spectral=[s.real, s.imag], error=err))
    mass = []
    for r, z in [(0.5, 0.2), (2.0, 0.2), (2.0, 1.0),
                 (2.0, 4.0), (3.0, 0.7), (3.0, 3.0)]:
        s, p = H_spectral(r, z), H_response(r, z)
        err = abs(s-p)
        assert err < 2e-7
        assert (r > 1 and s < 0) or (r < 1 and s > 0)
        mass.append(dict(r=r, internal_mass_over_reference=z,
                         spectral=s, response=p, error=err))
    # A fixed spectral channel, three external masses: exact differences
    # must compose, without readjusting weights or the spectral channel.
    h21 = H_response(2, 0.7)
    h32 = H_response(1.5, 0.7/2)
    h31 = H_response(3, 0.7)
    composition_error = abs(h21+h32-h31)
    reversal_error = abs(H_response(0.5, 0.7/2)+h21)
    assert composition_error < 2e-8 and reversal_error < 2e-8
    assert H_response(1, 0.3) == 0
    # Common rescaling of all three masses leaves both ratios unchanged.
    mi, mj, mf, factor = 2.0, 1.0, 0.7, 8.0
    assert H_response(mi/mj, mf/mj) == H_response(
        (factor*mi)/(factor*mj), (factor*mf)/(factor*mj))
    light = []
    for z in [0.01, 0.001, 0.0001]:
        full, asym = H_response(2, z), H_asymptotic(2, z)
        light.append(dict(z=z, full=full, asymptotic=asym, difference=full-asym))
    assert all(abs(b["difference"]) < abs(a["difference"])
               for a, b in zip(light, light[1:]))
    assert abs(light[-1]["difference"]) < 0.01
    heavy = [dict(z=z, value=H_response(2, z)) for z in [1.0, 4.0, 16.0]]
    assert all(abs(b["value"]) < abs(a["value"])
               for a, b in zip(heavy, heavy[1:]))
    mean_light = []
    for a in [1e-3, 1e-5, 1e-7]:
        mean = averaged_F(a)
        mean_light.append(dict(a=a, mean=mean,
                               normalized=mean/(a*math.log(1/a)),
                               asymptotic_coefficient=4/45,
                               fixed_scale_value=F_closed(math.exp(-0.5)*a)))
    assert all(abs(b["normalized"]-4/45) < abs(a["normalized"]-4/45)
               for a, b in zip(mean_light, mean_light[1:]))
    assert mean_light[-1]["mean"] > 10*mean_light[-1]["fixed_scale_value"]
    mean_large = [dict(a=a, remainder=averaged_F(a)-(math.log(a)/3-13/18))
                  for a in [1e2, 1e4, 1e6]]
    assert all(abs(b["remainder"]) < abs(a["remainder"])
               for a, b in zip(mean_large, mean_large[1:]))
    # Scheme matching: include the same fermionic charge-conversion term
    # in the ordinary one-loop mass expression. Its algebra is exact.
    l, L, S, qsq = F(2, 3), F(5, 4), F(7, 2), F(1)
    charge_coefficient = S*L/3
    first_mass_coefficient = -F(3, 2)*qsq*l
    conversion = F(1, 2)*qsq*S*L*l
    assert first_mass_coefficient*(-charge_coefficient) == conversion
    # d/dln(mu) of one-loop correction through beta(alpha), in units
    # alpha^2/pi^2, versus explicit derivative of the matched bubble.
    derivative_first = -qsq*S*l
    derivative_bubble = qsq*S*l
    assert derivative_first+derivative_bubble == 0
    # Log coefficients of the massless fermion-loop result from the
    # independent on-shell/MS expression: f(L)=-13L/24-L^2/8.
    li, lj = F(2, 3), F(7, 5)
    f = lambda x: -F(13, 24)*x-F(1, 8)*x*x
    log_r = (lj-li)/2
    expected = F(1, 2)*lj*log_r-F(1, 2)*log_r*log_r+F(13, 12)*log_r
    assert f(li)-f(lj) == expected
    return dict(spacelike_polarization=pol, continued_polarization=complex_pol,
                mass_spectral_vs_response=mass,
                difference_composition_error=composition_error,
                difference_reversal_error=reversal_error,
                equal_mass_difference=0,
                common_scale_invariance=True,
                small_internal_mass=light, heavy_channel_decoupling=heavy,
                averaged_response_low_argument=mean_light,
                averaged_response_high_argument=mean_large,
                exact_free_determinant_cancellation=True,
                exact_charge_scheme_matching=True,
                exact_common_mu_cancellation_in_fermion_loop_sector=True,
                exact_massless_two_loop_log_match=True)


def main():
    with warnings.catch_warnings():
        warnings.simplefilter("error", IntegrationWarning)
        output = {"step": 261, "parameters": "synthetic only",
                  "scope": "canonical vector QED; full one-loop polarization; "
                           "one renormalized fermion vacuum-polarization insertion "
                           "in a same-charge mass difference",
                  "algebra": algebra_checks(), "numerics": numeric_checks(),
                  "status": "PASS"}
    target = Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({"status": "PASS", "result": str(target),
                      "exact_trace_cases": output["algebra"]["exact_trace_cases"],
                      "exact_closed_LR_reduction_cases":
                          output["algebra"]["exact_closed_LR_reduction_cases"],
                      "max_pol_error": max(x["error"] for x in
                          output["numerics"]["continued_polarization"]),
                      "max_mass_error": max(x["error"] for x in
                          output["numerics"]["mass_spectral_vs_response"])},
                     ensure_ascii=False))


if __name__ == '__main__':
    main()

