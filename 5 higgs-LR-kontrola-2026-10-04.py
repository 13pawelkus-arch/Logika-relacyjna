#!/usr/bin/env python3
"""Kontrole przekładu L<->R z Higgsem; wyłącznie dane syntetyczne.

Zakres: pełna kinematyka 3+1 dla drzewowego wkładu skalarnego oraz
jednopętlowy diagram lepton+h. Nie jest to pełna poprawka NLO SM.
Przed każdym blokiem zapisano oczekiwanie i zdanie o upadku.
Uruchomienie: python3 higgs-LR-kontrola-2026-10-04.py
Wymagania: numpy, scipy. Bez danych eksperymentalnych.
"""
import json
import math
import numpy as np
from scipy.integrate import quad

checks = []
def check(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    checks.append(name)

def close(a, b, atol=2e-12):
    return np.allclose(a, b, rtol=2e-11, atol=atol)

# Prerejestracja danych: omega=1 oznacza normalizację względem wspólnego
# odczytu, nie jednostkę SI. m_a/omega=1/10, m_f/omega=2/5,
# m_g/omega=3/10, v/omega=2, m_h/omega=1/2.
# Kierunki mają trzy składowe; nie redukujemy przestrzeni do 1+1.
ratios = (0.0, 0.1, 0.3, 0.4)
directions = [np.array([2., 3., 6.])/7,
              np.array([6., 2., 3.])/7,
              np.array([1., 2., 2.])/3]

# Spodziewam się: gamma realizują sygnaturę +--- i prawidłowe projektory.
# Zdanie o upadku: błąd antykomutatora lub P_L P_R unieważnia test śladów.
I2, O2 = np.eye(2), np.zeros((2, 2))
sigmas = [np.array([[0,1],[1,0]],complex),
          np.array([[0,-1j],[1j,0]],complex),
          np.array([[1,0],[0,-1]],complex)]
g0 = np.block([[I2,O2],[O2,-I2]]).astype(complex)
gammas = [g0] + [np.block([[O2,s],[-s,O2]]) for s in sigmas]
I4 = np.eye(4, dtype=complex)
g5 = 1j * gammas[0] @ gammas[1] @ gammas[2] @ gammas[3]
PL, PR = (I4-g5)/2, (I4+g5)/2
metric = np.array([1.,-1.,-1.,-1.])
check('Clifford +---', all(close(gammas[u]@gammas[v]+gammas[v]@gammas[u],
      (2*metric[u]*I4 if u==v else 0*I4)) for u in range(4) for v in range(4)))
check('Projektory chiralne',close(PL@PR,0*I4) and close(PL@PL,PL) and close(PR@PR,PR))

def slash(p):
    return sum(metric[i]*p[i]*gammas[i] for i in range(4))

def bar(A):
    return g0@A.conj().T@g0

def pair(m, omega=1., direction=directions[0]):
    p=math.sqrt(omega*omega/4-m*m)*direction
    return np.r_[omega/2,p], np.r_[omega/2,-p]

def spin_gram(m, omega=1., direction=directions[0]):
    k1,k2=pair(m,omega,direction)
    R1,R2=slash(k1)+m*I4,slash(k2)-m*I4
    P=[PL,PR]
    return np.array([[np.trace(R1@P[i]@R2@bar(P[j])) for j in range(2)] for i in range(2)])

# Spodziewam się: W_LL=W_RR=omega²-2m², W_LR=-2m²;
# suma koherentna daje 2(omega²-4m²), we wszystkich kierunkach.
# Zdanie o upadku: niezgodny element Grama albo zależność od kierunku.
for rho in ratios:
    predicted=np.array([[1-2*rho*rho,-2*rho*rho],[-2*rho*rho,1-2*rho*rho]])
    check('Gram L/R rho='+str(rho),all(close(spin_gram(rho,direction=n),predicted) for n in directions))
    check('Koherentna suma rho='+str(rho),close(spin_gram(rho).sum(),2*(1-4*rho*rho)))
check('Kontrola pominięcia interferencji',not close(np.trace(spin_gram(.4)),spin_gram(.4).sum()))

# Spodziewam się: niezależna całka po kątach i ślady dają pełny
# drzewowy przekrój skalarny ya² yf² omega² beta_a beta_f³ |D|²/(64 pi).
# Zdanie o upadku: rozbieżność normalizacji spinu, strumienia lub fazy.
def xs_from_traces(mf, omega=1.):
    ma,v,mh=.1,2.,.5
    ga,gf=ma/v,mf/v
    Dh=1/(omega*omega-mh*mh)  # poza biegunem; bez sztucznej szerokości
    pa,pb=pair(ma,omega,np.array([0.,0.,1.]))
    init=np.trace((slash(pb)-ma*I4)@(slash(pa)+ma*I4)).real/4
    ba=math.sqrt(1-4*ma*ma/(omega*omega))
    bf=math.sqrt(1-4*mf*mf/(omega*omega))
    def dcos(u):
        n=np.array([math.sqrt(max(0.,1-u*u)),0.,u])
        final=spin_gram(mf,omega,n).sum().real
        amp2=(ga*gf*Dh)**2*init*final
        return 2*math.pi*amp2/(64*math.pi**2*omega**2)*bf/ba
    return quad(dcos,-1,1,epsabs=1e-14)[0]

def xs_formula(mf,omega=1.):
    ma,v,mh=.1,2.,.5
    ya,yf=math.sqrt(2)*ma/v,math.sqrt(2)*mf/v
    ba=math.sqrt(1-4*ma*ma/omega**2)
    bf=math.sqrt(1-4*mf*mf/omega**2)
    return ya*ya*yf*yf*omega**2*ba*bf**3/(64*math.pi*(omega**2-mh**2)**2)

for mf in (.3,.4):
    check('Pełna normalizacja sigma mf='+str(mf),close(xs_from_traces(mf),xs_formula(mf),atol=1e-16))
raw_ratio=xs_from_traces(.4)/xs_from_traces(.3)
check('Nieusuwalna waga progowa',close(raw_ratio,3/4) and not close(math.sqrt(raw_ratio),4/3))

# Spodziewam się: interferencja skalara z wektorem jest nieparzysta
# w cos(theta); z prądem osiowym znika. Niesymetryczny odczyt ją zachowa.
# Zdanie o upadku: część parzysta przy odczycie symetrycznym albo
# identyczne zero przy zadeklarowanej niesymetrycznej akceptancji.
def scalar_vector_trace(u,ma=.1,mf=.3):
    p1,p2=pair(ma,direction=np.array([0.,0.,1.]))
    k1,k2=pair(mf,direction=np.array([math.sqrt(max(0.,1-u*u)),0.,u]))
    a=np.array([np.trace((slash(p2)-ma*I4)@(slash(p1)+ma*I4)@gammas[i]) for i in range(4)])
    b=np.array([np.trace((slash(k1)+mf*I4)@(slash(k2)-mf*I4)@gammas[i]) for i in range(4)])
    return (np.sum(metric*a*b)/4).real

check('Nieparzysta interferencja h-V',close(scalar_vector_trace(.3),-scalar_vector_trace(-.3)))
interference_symmetric=quad(scalar_vector_trace,-1,1)[0]
interference_asymmetric=quad(lambda u:(1+.5*u)/2*scalar_vector_trace(u),-1,1)[0]
check('Interferencja: zależność od odczytu',abs(interference_symmetric)<1e-13 and abs(interference_asymmetric)>1e-4)
k1,k2=pair(.3)
axial=[np.trace((slash(k1)+.3*I4)@(slash(k2)-.3*I4)@gammas[i]@g5) for i in range(4)]
check('Brak interferencji scalar-axial',close(axial,np.zeros(4)))

# Spodziewam się: uśrednienie po dwóch energiach nie zachowa prostego
# skrócenia wspólnego propagatora przy różnych wagach progowych.
# Zdanie o upadku: iloraz niezależny od udziału dwóch energii.
mix_a=(xs_formula(.4,1)+xs_formula(.4,2))/(xs_formula(.3,1)+xs_formula(.3,2))
mix_b=(xs_formula(.4,1)+3*xs_formula(.4,2))/(xs_formula(.3,1)+3*xs_formula(.3,2))
check('Splot energii zachowuje wagę propagacji',not close(mix_a,mix_b))

# Spodziewam się: po odjęciu dwóch rozdzielczości zostają dwie całki
# logarytmiczne F (waga x) i G (waga 1), bez skali regulatora.
# Zdanie o upadku: zależność wyniku od wspólnego przeskalowania mas
# i obu pędów albo pominięcie różnicy F/G.
def kernels(r,eta,mh=.5):
    def logratio(x):
        base=x*mh*mh+(1-x)*eta*eta
        return math.log((base+x*(1-x)*r*r)/(base+x*(1-x)))
    f,fe=quad(lambda x:x*logratio(x),0,1,epsabs=2e-12,epsrel=2e-12)
    g,ge=quad(logratio,0,1,epsabs=2e-12,epsrel=2e-12)
    return f,g,max(fe,ge)

f1,g1,err1=kernels(2,.3)
f2,g2v,err2=kernels(2,.4)
check('Wagi pętli zależne od kanału',f1>f2>0 and g1>g2v>0)
check('Dwa różne człony propagatora',not close(f1,g1))

def kernel_dimensional(Q,Q0,m,mh,reg):
    def d(x,q): return x*mh*mh+(1-x)*m*m+x*(1-x)*q*q
    return quad(lambda x:x*(math.log(d(x,Q)/reg**2)-math.log(d(x,Q0)/reg**2)),0,1,epsabs=2e-12)[0]
values=[kernel_dimensional(2*scale,scale,.3*scale,.5*scale,reg*scale)
        for scale in (1.,7.,.2) for reg in (.4,3.,11.)]
check('Brak regulatora i jednostki w różnicy',all(close(x,f1) for x in values))

# Spodziewam się: znak monotoniczności pochodzi z obu mianowników,
# a nie z dopasowania krzywej. Kontrola różnicowa sprawdza pochodną.
# Zdanie o upadku: zły znak lub brak zgodności dwóch obliczeń pochodnej.
r,eta,mh=2.,.3,.5
def analytic_derivative(x):
    b=x*mh*mh+(1-x)*eta*eta+x*(1-x)
    a=b+x*(1-x)*(r*r-1)
    return x*(1-x)*(1/a-1/b)
der=quad(analytic_derivative,0,1,epsabs=2e-12)[0]
step=1e-5
numerical=(kernels(r,math.sqrt(eta*eta+step),mh)[0]-kernels(r,math.sqrt(eta*eta-step),mh)[0])/(2*step)
check('Ścisły znak zależności od masy',der<0 and close(der,numerical,atol=2e-8))

# Spodziewam się: gdy OBA porównywane pędy są duże względem mas,
# F -> ln r, G -> 2 ln r. Sam Q duży przy Q0 przy progu nie wystarcza.
# Zdanie o upadku: odchylenie nie maleje po wspólnym zmniejszeniu eta_i,eta_h.
uv=[]
for scale in (1.,.1,.01,.001):
    f,g,err=kernels(2,.3*scale,.5*scale)
    uv.append((scale,f,g,abs(f-math.log(2)),abs(g-2*math.log(2))))
check('Granica wspólnego logarytmu',all(uv[i+1][3]<uv[i][3] and uv[i+1][4]<uv[i][4] for i in range(3)))
check('Wartość graniczna',uv[-1][3]<1e-5 and uv[-1][4]<2e-5)

result={
    'liczba_kontroli':len(checks),
    'status':'wszystkie zadeklarowane kontrole przeszły',
    'dane':'syntetyczne, bez mas lub sprzężeń z pomiaru',
    'born':{'mass_ratio':4/3,'event_ratio':raw_ratio,'naive_amplitude_ratio':math.sqrt(raw_ratio),
            'sigma_f':xs_from_traces(.4),'sigma_g':xs_from_traces(.3)},
    'interference':{'symmetric':interference_symmetric,'asymmetric':interference_asymmetric},
    'energy_mixture_ratios':[mix_a,mix_b],
    'loop':{'r':2,'eta_h':.5,'eta_f':.3,'F_f':f1,'G_f':g1,'eta_g':.4,'F_g':f2,'G_g':g2v,
            'integration_error_max':max(err1,err2),'dF_d_eta2':der},
    'uv_columns':['mass_scale','F','G','F_error','G_error'],
    'uv':uv,
}
if __name__=='__main__':
    print(json.dumps(result,ensure_ascii=False,indent=2))
