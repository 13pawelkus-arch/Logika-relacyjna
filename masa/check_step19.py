"""General Gaussian boundary weights, causal contact response and target measure."""
import json
from itertools import product
from fractions import Fraction
from math import factorial,log
import numpy as np
from scipy.linalg import expm,expm_frechet
from scipy.integrate import quad

dag=lambda a:a.conj().T
tr=np.trace
err=lambda a,b:float(np.max(np.abs(a-b)))

def annihilators(d):
    c=np.array([[0,1],[0,0]],complex); z=np.diag([1,-1]); eye=np.eye(2)
    result=[]
    for k in range(d):
        a=np.array([[1]],complex)
        for j in range(d):a=np.kron(a,z if j<k else c if j==k else eye)
        result.append(a)
    return result

def lift(h,aa):
    return sum((h[p,q]*dag(aa[p])@aa[q] for p,q in product(range(len(aa)),repeat=2)),
               np.zeros_like(aa[0]))

def exponential_jet(h,hp,hpp):
    A,B,C=-1j*h,-1j*hp,-1j*hpp
    u,du=expm_frechet(A,B)
    z=np.zeros_like(A); d=len(A)
    blocks=np.block([[A,B,C/2],[z,A,B],[z,z,A]])
    ddu=2*expm(blocks)[:d,2*d:3*d]
    return u,du,ddu

def full_product(steps,r=None,s=None):
    u=np.eye(len(steps[0][0]),dtype=complex)
    for k,(t,dt,ddt) in enumerate(steps):
        chosen=ddt if k==r==s else dt if k==r or k==s else t
        u=chosen@u
    return u

def source_hessians(U,first,second,rho,F):
    p=tr(F@U@rho@dag(U))
    zp=np.array([tr(F@v@rho@dag(U)) for v in first])
    C=np.empty((len(first),len(first)),complex); H=C.copy()
    for r,s in product(range(len(first)),repeat=2):
        C[r,s]=tr(F@first[s]@rho@dag(first[r]))/p-zp[r].conjugate()*zp[s]/(p*p)
        H[r,s]=tr(F@second[r][s]@rho@dag(U))/p-zp[r]*zp[s]/(p*p)
    return C,H

d=3; aa=annihilators(d); eye=np.eye(d)
rng=np.random.default_rng(1900)
def hermitian():
    m=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
    return (m+dag(m))/10
R,S=expm(-hermitian()),expm(-hermitian())
rv,re=np.linalg.eigh(R); Rh=(re*np.sqrt(rv))@dag(re); Rhi=(re/np.sqrt(rv))@dag(re)
rho=expm(lift((re*np.log(rv))@dag(re),aa)); rho/=tr(rho)
sv,se=np.linalg.eigh(S)
rawF=expm(lift((se*np.log(sv))@dag(se),aa))
F=.8*rawF/np.linalg.eigvalsh(rawF).max()
N=R@np.linalg.inv(eye+R)
lam,V=np.linalg.eigh(N)
contact_jets=[]; fock_jets=[]
local_x=[]; local_xi=[]
for p,q in [(0,1),(1,2),(0,2),(1,2),(0,1)]:
    h=hermitian(); hp=np.zeros_like(h); hpp=np.zeros_like(h)
    hp[p,q]=1j*h[p,q]; hp[q,p]=hp[p,q].conjugate()
    hpp[p,q]=-h[p,q]; hpp[q,p]=hpp[p,q].conjugate()
    jet=exponential_jet(h,hp,hpp)
    contact_jets.append(jet)
    fock_jets.append(exponential_jet(lift(h,aa),lift(hp,aa),lift(hpp,aa)))
    u,du,ddu=jet
    local_x.append(-1j*dag(u)@du)
    local_xi.append(-1j*(dag(du)@du+dag(u)@ddu))

checks=dict(conditioned_channel_sum=0.,conditioned_matrix_formula=0.,
            same_branch_hessian=0.,inclusive_covariance=0.,
            causal_branch_derivatives=0.,causal_fock_commutator=0.,
            causal_occupation_sum=0.,causal_future_zero=0.,
            transported_contact_current=0.,mean_current=0.,
            target_log_measure=0.,target_moments=0.,target_log_constant=0.)
matrix_entries=0
for count in range(1,6):
    steps=contact_jets[:count]; fs=fock_jets[:count]
    u,U=full_product(steps),full_product(fs)
    du=[full_product(steps,r=k) for k in range(count)]
    dU=[full_product(fs,r=k) for k in range(count)]
    ddu=[[full_product(steps,r=r,s=s) for s in range(count)] for r in range(count)]
    ddU=[[full_product(fs,r=r,s=s) for s in range(count)] for r in range(count)]
    X=[-1j*dag(u)@v for v in du]
    B=dag(u)@S@u
    L=np.linalg.solve(eye+B@R,B)
    occupation=Rh@L@Rh
    eta,T=np.linalg.eigh(occupation)
    Y=[Rhi@x@Rh for x in X]
    Yr=[dag(T)@y@T for y in Y]
    Nop=R@L
    C,H=source_hessians(U,dU,ddU,rho,F)
    CI,HI=source_hessians(U,dU,ddU,rho,np.eye(len(U)))
    prefix=np.eye(d,dtype=complex); Xi=[]
    for k in range(count):
        carried=dag(prefix)@local_x[k]@prefix
        checks['transported_contact_current']=max(checks['transported_contact_current'],err(X[k],carried))
        Xi.append(dag(prefix)@local_xi[k]@prefix)
        prefix=steps[k][0]@prefix
    for r,s in product(range(count),repeat=2):
        channel=np.sum(eta[:,None]*(1-eta[None,:])*Yr[r].conjugate()*Yr[s])
        compact=tr(dag(Y[r])@occupation@Y[s]@(eye-occupation))
        hh=tr(Nop@dag(u)@ddu[r][s])+tr(Nop@X[s]@Nop@X[r])
        checks['conditioned_channel_sum']=max(checks['conditioned_channel_sum'],abs(channel-C[r,s]))
        checks['conditioned_matrix_formula']=max(checks['conditioned_matrix_formula'],abs(compact-C[r,s]))
        checks['same_branch_hessian']=max(checks['same_branch_hessian'],abs(hh-H[r,s]))
        covariance=tr(N@X[r]@(eye-N)@X[s])
        checks['inclusive_covariance']=max(checks['inclusive_covariance'],abs(covariance-CI[r,s]))
        response=(HI[r,s]+CI[s,r]-CI[r,s]-HI[r,s].conjugate())/(2j)
        if r>s:
            target=1j*tr(N@(X[r]@X[s]-X[s]@X[r]))
            xr,xs=dag(V)@X[r]@V,dag(V)@X[s]@V
            transition=1j*np.sum((lam[:,None]-lam[None,:])*xr*xs.T)
            jf,jg=lift(X[r],aa),lift(X[s],aa)
            full=1j*tr(rho@(jf@jg-jg@jf))
        elif r==s:
            target=tr(N@Xi[r]); transition=target; full=tr(rho@lift(Xi[r],aa))
        else:
            target=transition=full=0.
            checks['causal_future_zero']=max(checks['causal_future_zero'],abs(response))
        checks['causal_branch_derivatives']=max(checks['causal_branch_derivatives'],abs(response-target))
        checks['causal_fock_commutator']=max(checks['causal_fock_commutator'],abs(full-target))
        checks['causal_occupation_sum']=max(checks['causal_occupation_sum'],abs(transition-target))
        matrix_entries+=1
    E=dag(U)@F@U; p=tr(E@rho)
    for k in range(count):
        mean=tr(E@lift(X[k],aa)@rho)/p
        checks['mean_current']=max(checks['mean_current'],abs(mean-tr(Nop@X[k])))

# A different calculation: the complete positive logarithmic measure of the
# target F_gamma, derived by t=x(1-x), not inferred from the test matrices.
moment=lambda k:2*Fraction(factorial(k+1)**2,factorial(2*k+3))
moments=[moment(k) for k in range(6)]
assert moments==[Fraction(1,3),Fraction(1,15),Fraction(1,70),Fraction(1,315),Fraction(1,1386),Fraction(1,6006)]
for k,m in enumerate(moments):
    value=quad(lambda t:2*t*t**k,0,.25,weight='alg',wvar=(0,-.5),epsabs=1.e-13)[0]
    checks['target_moments']=max(checks['target_moments'],abs(value-float(m)))
for r in [.03,.4,2.,11.,250.]:
    original=2*quad(lambda x:x*(1-x)*np.log1p(r*x*(1-x)),0,1,epsabs=1.e-13)[0]
    measure=quad(lambda t:2*t*np.log1p(r*t),0,.25,weight='alg',wvar=(0,-.5),epsabs=1.e-13)[0]
    checks['target_log_measure']=max(checks['target_log_measure'],abs(measure-original))
constant=quad(lambda t:0 if t==0 else 2*t*log(t),0,.25,weight='alg',wvar=(0,-.5),epsabs=1.e-13)[0]
checks['target_log_constant']=abs(constant+5/9)
for key,value in checks.items():assert value<3.e-11,(key,value)
print(json.dumps(dict(status='PASS',contact_prefixes=5,response_entries=matrix_entries,
    moments=list(map(str,moments)),max_errors=checks,
    scope='complete Gaussian channel formula and causal response; target measure audited separately, not derived from the frame'),indent=2))
