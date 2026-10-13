"""Kontrole kroku 262: pełne dopasowanie masowe O(alpha^2) wektorowego QED.

Współczynniki całek dwupętlowych: literatura wskazana w raporcie.
Dokładne przeliczenie logarytmów: fractions. Pełne funkcje dwóch mas:
niezależna całka spektralna scipy i analityczne dilogarytmy Decimal.
Wszystkie przykłady są syntetyczne; nie wykonujemy dopasowania mas.
Uruchomienie: python3 AB-drugi-rzad-kontrola-2026-10-09.py
Wymaga scipy; reszta to biblioteka standardowa.
"""
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
import math
import warnings
from scipy.integrate import quad, IntegrationWarning, solve_ivp


def atan_series(x):
    total, power, k = x, x, 1
    while True:
        power *= -x*x
        term = power / (2*k+1)
        old = total
        total += term
        if total == old:
            return total
        k += 1


with localcontext() as ctx:
    ctx.prec = 90
    PI = 16*atan_series(D(1)/5)-4*atan_series(D(1)/239)
    Z2 = PI*PI/6
    Z3 = D(0)
    for n in range(1, 180):
        Z3 += D((-1)**(n-1))/D(n**3*math.comb(2*n,n))
    Z3 *= D(5)/2


def li2(x):
    """Real Li_2(x), x <= 1, by exact identities and convergent series."""
    x = D(x)
    if x == 1:
        return +Z2
    if x == 0:
        return D(0)
    if x < -1:
        return -li2(1/x)-Z2-(-x).ln()**2/2
    if x < 0:
        return -li2(x/(x-1))-(1-x).ln()**2/2
    if x > D('0.5'):
        return Z2-x.ln()*(1-x).ln()-li2(1-x)
    total, power, n = D(0), x, 1
    while True:
        old = total
        total += power/(n*n)
        if total == old:
            return total
        n += 1
        power *= x


@lru_cache(maxsize=None)
def V(z, precision=70):
    """Full one-fermion-loop coefficient, external B mass as argument.

    Hoang hep-ph/0008102 eq. (222), divided by 3, plus the massless
    coefficient from Melnikov--van Ritbergen hep-ph/9912391.
    The Li_2(z)+ln(z)ln(1-z) combination is rewritten as
    zeta(2)-Li_2(1-z), real for every positive z; no cut is discarded.
    """
    with localcontext() as ctx:
        ctx.prec = precision
        z = D(str(z))
        if z <= 0:
            raise ValueError('z musi być dodatnie')
        l = z.ln()
        ap = li2(-z)-l*l/2+l*(1+z).ln()+Z2
        am = -li2(1-z)-l*l/2-Z2
        fp = (D(3)/2*l*l+PI*PI/4-D(3)/2*z*z*(l+D(3)/2)
              +D(3)/2*(1+z)*(1+z**3)*ap
              +D(3)/2*(1-z)*(1-z**3)*am)
        return -D(71)/96-Z2/2+fp/3


def H_analytic(r, z):
    with localcontext() as ctx:
        ctx.prec = 70
        r, z = D(str(r)), D(str(z))
        l = r.ln()
        return 12*(V(str(z/r))-V(str(z)))+13*l-6*l*l+12*l*z.ln()


def integrate(f, a=0., b=1., **kw):
    options = dict(epsabs=2e-10, epsrel=2e-10, limit=260)
    options.update(kw)
    value, error = quad(f, a, b, **options)
    assert math.isfinite(value) and math.isfinite(error)
    return value


def H_spectral(r, z):
    """Independent full dispersion integral of 261, with s mapped to velocity."""
    if r == 1:
        return 0.
    def outer(v):
        a = 1-v*v
        def inner(x):
            b = a*(1-x)**2
            denominator = 4*z*z*x+r*r*b
            return (4-2*x)*math.log1p((1-r*r)*b/denominator)
        return v*v*(3-v*v)/a*integrate(inner, epsabs=2e-10)
    return integrate(outer, epsabs=2e-9, epsrel=2e-10)


def poly_add(*polys):
    n = max(map(len,polys))
    return [sum((p[k] if k<len(p) else F(0) for p in polys), F(0))
            for k in range(n)]


def poly_scale(c,p):
    return [c*v for v in p]


def poly_mul(p,q):
    out = [F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):
            out[i+j] += x*y
    return out


def poly_der(p):
    return [k*p[k] for k in range(1,len(p))]


def exact_checks():
    # C is left symbolic in the report; it only enters the constant below.
    # Set that constant to zero here: all nonconstant identities hold for any C.
    f = [F(1),F(3,4)]
    g = [F(0),F(21,32),F(9,32)]
    d = poly_add(poly_mul(f,f),poly_scale(F(-3,2),f),poly_scale(-1,g))
    h = poly_add(d,poly_scale(F(-1,2),poly_mul(f,f)))
    assert d == [F(-1,2),F(-9,32),F(9,32)]
    assert h == [F(-1),F(-33,32),F(0)]
    # gamma from differentiating log(M/m), including the running of m in L.
    gamma_ff = F(9,4)+2*h[1]
    assert gamma_ff == F(3,16)
    vp_logs = [F(0),F(-13,24),F(-1,8)]
    gamma_vp = poly_add(poly_scale(F(2,3),f),poly_scale(2,poly_der(vp_logs)))
    assert gamma_vp == [F(-5,12),F(0)]
    # Ratio coefficient in B variables, inverse mapping, and A variables.
    c1,c2 = F(-3,2),F(33,16)
    inv1,inv2 = -c1,c1*c1-c2
    assert inv2 == F(3,16)
    assert c1+inv1 == 0 and c2+inv2+c1*inv1 == 0
    assert c2-c1*c1 == F(-3,16)
    # If one inverts 1/z_m but freezes L_M=L_m, the d coefficient misses -3f/2.
    wrong_d = poly_add(poly_mul(f,f),poly_scale(-1,g))
    assert poly_add(wrong_d,poly_scale(-1,d)) == poly_scale(F(3,2),f)+[F(0)]
    wrong_h = poly_add(wrong_d,poly_scale(F(-1,2),poly_mul(f,f)))
    assert -2*wrong_h[1] == F(-3,16)  # wrong if presented in B variables!
    assert -2*wrong_h[1] != c2
    # Coupling conversion: a_B=a_0+a_0^2 S_L/3.
    assert F(-3,2)/3+F(1,2) == 0
    # Explicit mu derivative of VP ratio versus derivative of one-loop alpha_B.
    assert F(-3,2)*F(2,3)+2*F(1,2) == 0
    return {'status':'PASS','D_FF_log_coefficients':[str(x) for x in d[1:]],
            'log_M_over_m_FF_coefficients':[str(x) for x in h[1:]],
            'gamma_FF':str(gamma_ff),'gamma_VP_per_Q2_c':str(gamma_vp[0]),
            'ratio_B_second_order':str(c2),'ratio_A_second_order':'-3/16',
            'inverse_second_order':str(inv2),
            'omitted_argument_iteration_detected':True,
            'coupling_conversion_and_mu_cancellation':'exact'}


def coefficient_constants():
    with localcontext() as ctx:
        ctx.prec=70
        C=D(7)/128-D(15)/8*Z2-D(3)/4*Z3+3*Z2*D(2).ln()
        return C, -D(1)/2-C, -D(1)-C


def log_match_coefficients(mi,mu,Q,spectrum):
    """log(M_i/m_i) = a*b1+a^2*b2, a=alpha_MSbar/pi.
    Spectrum entries: (mass, N_c Q_f^2), same full theory for every external i.
    """
    L=2*math.log(mu/mi)
    C= float(coefficient_constants()[0])
    b1=Q*Q*(1+3*L/4)
    b2=Q**4*(-1-C-33*L/32)
    b2+=Q*Q*sum(c*(float(V(str(mf/mi)))-13*L/24-L*L/8)
                for mf,c in spectrum)
    return b1,b2


def ratio_coefficients(mi,mj,Q,spectrum,mu,scheme='B'):
    r=mi/mj
    l=math.log(r)
    vp=Q*Q/12*sum(c*float(H_analytic(r,mf/mj)) for mf,c in spectrum)
    if scheme=='B':
        vp+=Q*Q*l/2*sum(c*2*math.log(mu/mf) for mf,c in spectrum)
    return -1.5*Q*Q*l,33/16*Q**4*l+vp


def numeric_checks():
    out={}
    with localcontext() as ctx:
        ctx.prec=70
        assert abs(li2(D(-1))+Z2/2)<D('1e-65')
        assert abs(li2(D('0.5'))-(Z2/2-D(2).ln()**2/2))<D('1e-65')
        assert abs(V('1')-(Z2-D(143)/96))<D('1e-64')
        small=D('1e-8')
        v0=-D(71)/96-Z2/2
        small_slope=(V(str(small))-v0)/small
        assert abs(small_slope-PI*PI/4)<D('4e-8')
        # Heavy-loop limit at mu=m_f agrees with mass decoupling 89/288.
        z=D('1000000')
        heavy=V(str(z))-z.ln()**2/2-D(13)/12*z.ln()
        assert abs(heavy-D(89)/288)<D('1e-10')
        out['limits']={'V_0':str(v0),'V_1':str(V('1')),
                       'small_z_linear_coefficient':str(small_slope),
                       'heavy_constant':str(heavy),'expected_heavy_constant':'89/288'}
    cases=[(.5,.03),(2.,.2),(2.,1.),(3.,4.),(1.3,.2),(6.,3.),(.8,5.),(2.,8.)]
    comparisons=[]
    for r,z in cases:
        hs=H_spectral(r,z)
        ha=float(H_analytic(r,z))
        error=abs(hs-ha)
        assert error<3e-8, (r,z,hs,ha,error)
        comparisons.append({'r':r,'z':z,'spectral':hs,'analytic':ha,'abs_error':error})
    out['full_threshold_comparisons']=comparisons
    out['max_threshold_error']=max(x['abs_error'] for x in comparisons)
    identities=[]
    for r,z in [(2,.2),(2,1),(.7,3),(5,.3)]:
        # Full reversal and additivity; analytic precision removes quadrature error.
        with localcontext() as ctx:
            ctx.prec=60
            rd,zd=D(str(r)),D(str(z))
            reverse=H_analytic(str(rd),str(zd))+H_analytic(str(1/rd),str(zd/rd))
            assert abs(reverse)<D('1e-50')
            middle=D('1.7')
            add=H_analytic(str(rd),str(zd))-H_analytic(str(rd/middle),str(zd/middle))-H_analytic(str(middle),str(zd))
            assert abs(add)<D('1e-50')
            identities.append({'r':r,'z':z,'reversal':str(reverse),'additivity':str(add)})
    out['identities']=identities
    # Independent individual matching versus the compact ratio; different charges,
    # masses and multiplicities inside loops, identical external charges.
    spectrum=[(.2,1.),(1.,1.),(3.,4/3),(8.,1/3)]
    comparison=[]
    for mi,mj,Q,mu in [(2,1,1,1),(2,1,1,7),(.5,3,2/3,2),(4,2,2,8),(1,1,1,3)]:
        bi=log_match_coefficients(mi,mu,Q,spectrum)
        bj=log_match_coefficients(mj,mu,Q,spectrum)
        compact=ratio_coefficients(mi,mj,Q,spectrum,mu)
        err=max(abs(bi[k]-bj[k]-compact[k]) for k in (0,1))
        assert err<2e-12
        # Match alpha_0 and alpha_B coefficient by coefficient.
        zero=ratio_coefficients(mi,mj,Q,spectrum,mu,'0')
        sl=sum(c*2*math.log(mu/mf) for mf,c in spectrum)
        assert abs(zero[1]-(compact[1]+compact[0]*sl/3))<2e-12
        comparison.append({'mi':mi,'mj':mj,'Q':Q,'mu':mu,'difference_error':err})
    out['individual_vs_ratio']=comparison
    # Actual finite-step inversion: published m/M (A arguments) against our M/m
    # (B arguments). Remainder must scale as a^3, including changed internal masses.
    C=float(coefficient_constants()[0]); mu=2.7; ms=[.6,1.4,3.2]; qs=[1.,1.,2/3]
    inversions=[]
    for a in [.002,.001,.0005]:
        spec=[(m,q*q) for m,q in zip(ms,qs)]
        coeff=[log_match_coefficients(m,mu,q,spec) for m,q in zip(ms,qs)]
        poles=[m*(1+a*c[0]+a*a*(c[1]+c[0]*c[0]/2)) for m,c in zip(ms,coeff)]
        recovered=[]
        for pole,q in zip(poles,qs):
            L=2*math.log(mu/pole)
            zm1=-q*q*(1+3*L/4)
            zm2=q**4*(C+21*L/32+9*L*L/32)
            zm2+=q*q*sum(qf*qf*(-float(V(str(mf/pole)))+13*L/24+L*L/8)
                            for mf,qf in zip(poles,qs))
            recovered.append(pole*(1+a*zm1+a*a*zm2))
        err=max(abs(x/y-1) for x,y in zip(recovered,ms))
        inversions.append({'a':a,'max_relative_residual':err,'residual_over_a3':err/a**3})
    for x,y in zip(inversions,inversions[1:]):
        assert 7.6<x['max_relative_residual']/y['max_relative_residual']<8.4
    out['A_B_inversion']=inversions
    # Independent RG evolution of the input parameters; the output pole is constant
    # up to the omitted third order, for unequal charges as well.
    evolutions=[]
    for a in [.002,.001,.0005]:
        S=sum(q*q for q in qs)
        def rhs(t,y):
            aa=y[0]
            beta=2*S/3*aa*aa  # sufficient for an O(a^2) invariance check
            gammas=[1.5*q*q*aa+(3*q**4/16-5*q*q*S/12)*aa*aa for q in qs]
            return [beta]+[-g for g in gammas]
        t1=.6
        solution=solve_ivp(rhs,[0,t1],[a]+[math.log(m) for m in ms],rtol=1e-12,atol=1e-14)
        af=solution.y[0,-1]; mf=[math.exp(x) for x in solution.y[1:,-1]]
        spec0=list(zip(ms,[q*q for q in qs])); spec1=list(zip(mf,[q*q for q in qs]))
        values=[]
        for i,q in enumerate(qs):
            b=log_match_coefficients(ms[i],mu,q,spec0)
            c=log_match_coefficients(mf[i],mu*math.exp(t1),q,spec1)
            logpole0=math.log(ms[i])+a*b[0]+a*a*b[1]
            logpole1=math.log(mf[i])+af*c[0]+af*af*c[1]
            values.append(abs(logpole1-logpole0))
        err=max(values)
        evolutions.append({'a':a,'max_log_pole_residual':err,'residual_over_a3':err/a**3})
    for x,y in zip(evolutions,evolutions[1:]):
        assert 7.5<x['max_log_pole_residual']/y['max_log_pole_residual']<8.5
    out['RG_evolution']=evolutions
    return out


def main():
    with warnings.catch_warnings():
        warnings.simplefilter('error',IntegrationWarning)
        result={'status':'PASS','scope':'full O(alpha^2) mass matching in canonical vector QED',
                'inputs':'published two-loop coefficients and specified positive fermion spectrum',
                'exact':exact_checks(),'numerical':numeric_checks()}
    C,Dff,Clog=coefficient_constants()
    result['constants']={'C_FF_published':str(C),'D_FF_forward':str(Dff),'C_log_forward':str(Clog)}
    dest=Path(__file__).with_suffix('.json')
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'max_threshold_error':result['numerical']['max_threshold_error'],
                      'threshold_cases':len(result['numerical']['full_threshold_comparisons']),
                      'output':str(dest)},ensure_ascii=False))


if __name__=='__main__':
    main()
