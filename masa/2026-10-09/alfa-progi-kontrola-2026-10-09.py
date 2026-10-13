"""Kontrola §F0: ułamki dokładne i dwie niezależne całki.
Wejścia syntetyczne; brak dopasowania do zmierzonych mas.
Wymaga NumPy oraz SciPy. Uruchomienie: python alfa-progi-kontrola-2026-10-09.py
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, comb, log1p, pi, sqrt
import json
import numpy as np
from scipy.integrate import quad

OUT = Path(__file__).with_suffix(".json")
result = {"scope": "Jednopętlowy wkład fermionowy, podana F_gamma. Wejścia syntetyczne, bez danych masowych; kontrole nie zastępują dowodów w raporcie.", "exact": {}, "numerical": {}}
coefficients = {}
for k in range(1, 9):
    integral = sum(Q((-1)**j * comb(k+1, j), k+2+j) for j in range(k+2))
    integrated = Q(2, k) * integral
    closed = Q(2 * factorial(k+1)**2, k * factorial(2*k+3))
    assert integrated == closed
    coefficients[str(k)] = str(closed)
result["exact"]["a_k"] = coefficients

def moments(rs, cs, maximum):
    return [sum(c*r**k for r,c in zip(rs,cs)) for k in range(maximum+1)]

cases_exact = [
    ([Q(1),Q(2),Q(3)], [Q(1)]*3),
    ([Q(1)]*3, [Q(1),Q(4,9),Q(1,9)]),
    ([Q(1),Q(1,4),Q(1,9)], [Q(1)]*3),
    ([Q(17,7),Q(19,7),Q(6,7)], [Q(2),Q(4,3),Q(1,3)])
]
variance_controls=[]
for rs,cs in cases_exact:
    p=moments(rs,cs,2)
    lhs=p[0]*p[2]-p[1]**2
    rhs=sum(cs[i]*cs[j]*(rs[i]-rs[j])**2 for i in range(len(rs)) for j in range(i+1,len(rs)))
    assert lhs == rhs and lhs >= 0
    assert (lhs == 0) == (len(set(rs)) == 1)
    variance_controls.append({"r":list(map(str,rs)),"weights":list(map(str,cs)),"variance":str(lhs)})
result["exact"]["variance_controls"] = variance_controls

first=[Q(1),Q(2),Q(3)]
second=[Q(17,7),Q(19,7),Q(6,7)]
first_p=moments(first,[Q(1)]*3,3)
second_p=moments(second,[Q(1)]*3,3)
assert first_p[1:3] == second_p[1:3] and first_p[3] != second_p[3]
result["exact"]["two_moments_do_not_determine_three_masses"]={"r_first":list(map(str,first)),"r_second":list(map(str,second)),"moments_first":list(map(str,first_p[1:])),"moments_second":list(map(str,second_p[1:]))}

synthetic=[Q(1),Q(1,4),Q(1,9)]
p=moments(synthetic,[Q(1)]*3,7)
e1=p[1]
e2=(p[1]**2-p[2])/2
e3=(p[1]**3-3*p[1]*p[2]+2*p[3])/6
assert e1 == sum(synthetic)
assert e2 == sum(synthetic[i]*synthetic[j] for i in range(3) for j in range(i+1,3))
assert e3 == synthetic[0]*synthetic[1]*synthetic[2]
assert all(r**3-e1*r**2+e2*r-e3 == 0 for r in synthetic)
for k in range(5):
    assert p[k+3] == e1*p[k+2]-e2*p[k+1]+e3*p[k]
predicted_p4=(p[1]**4-6*p[1]**2*p[2]+3*p[2]**2+8*p[1]*p[3])/6
assert predicted_p4 == p[4]
D=3*p[2]/p[1]**2-1
scaled=moments([Q(7,3)**2*r for r in synthetic],[Q(1)]*3,2)
assert 3*scaled[2]/scaled[1]**2-1 == D
result["exact"]["synthetic_polynomial"]={"r":list(map(str,synthetic)),"p1_p2_p3":list(map(str,p[1:4])),"e1_e2_e3":list(map(str,[e1,e2,e3])),"p4":str(p[4]),"p4_from_first_three":str(predicted_p4),"D":str(D),"reference_rescaling_invariant":True,"recurrence_checked_through_p7":True}
recovered=np.roots([1,-float(e1),float(e2),-float(e3)])
assert np.max(np.abs(recovered.imag)) < 1e-12
ratios=sorted(1/np.sqrt(recovered.real))
root_error=max(abs(a-b) for a,b in zip(ratios,[1,2,3]))
assert root_error < 1e-11
result["numerical"]["reconstruction"]={"recovered_m_over_q_star":ratios,"max_absolute_error":root_error}

rho_mu=Q(1,9)
beta_mu=sqrt(float(1-4*rho_mu))
weight_mu=beta_mu*float(1+2*rho_mu)
synthetic_R=3.0
physical_channel_ratio=synthetic_R/weight_mu
restored_R=physical_channel_ratio*weight_mu
assert abs(restored_R-synthetic_R) < 1e-13 and abs(physical_channel_ratio-synthetic_R) > 0.1
result["numerical"]["muon_reference_weight"]={"m_mu_squared_over_omega_squared":str(rho_mu),"weight_mu":weight_mu,"synthetic_spectral_R":synthetic_R,"physical_hadron_to_muon_channel_ratio":physical_channel_ratio,"restored_spectral_R":restored_R,"uncorrected_ratio_is_different":True}

fake_p0,fake_p1,fake_p2=3,3,1
assert fake_p0*fake_p2-fake_p1**2 < 0
result["exact"]["incompatible_curve_moments"]={"p0":fake_p0,"p1":fake_p1,"p2":fake_p2,"variance":fake_p0*fake_p2-fake_p1**2}

def F_gamma(value):
    integral,error=quad(lambda x:2*x*(1-x)*log1p(x*(1-x)*value),0,1,epsabs=2e-13,epsrel=2e-13)
    return integral,error
def dispersion_free(a,chi):
    integral,error=quad(lambda b:4*a*b*b*(3-b*b)/((4*a+chi*(1-b*b))*(4*a+1-b*b)),0,1,epsabs=2e-13,epsrel=2e-13)
    return -(chi-1)*integral/(3*pi),abs(chi-1)*error/(3*pi)
errors=[]
spectral_cases=[]
for a in [0.01,0.25,1.,9.]:
    for chi in [0.25,1.,2.,9.]:
        f1,e_f1=F_gamma(chi/a)
        f2,e_f2=F_gamma(1/a)
        direct=-(f1-f2)/pi
        dispersive,e_disp=dispersion_free(a,chi)
        error=abs(direct-dispersive)
        errors.append(error)
        spectral_cases.append({"m2_over_q2_squared":a,"q1_squared_over_q2_squared":chi,"direct":direct,"dispersion":dispersive,"absolute_error":error,"estimated_quadrature_error":(e_f1+e_f2)/pi+e_disp})
assert max(errors) < 1e-11
result["numerical"]["full_threshold_vs_dispersion"]={"cases":spectral_cases,"max_absolute_error":max(errors),"float_arithmetic":"IEEE double; exact identities checked separately on fractions"}
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"saved":OUT.name,"exact_controls":list(result["exact"]),"spectral_cases":len(spectral_cases),"max_spectral_error":max(errors),"max_reconstruction_error":root_error},ensure_ascii=False))
