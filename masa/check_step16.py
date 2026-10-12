"""Checks of bilinear composition and the full boundary-weighted determinant."""
import json
from itertools import product
import numpy as np
from scipy.linalg import expm, expm_frechet

dag = lambda x: x.conj().T
err = lambda x,y: float(np.max(np.abs(x-y)))
tr = np.trace

def annihilators(d):
    c=np.array([[0,1],[0,0]],complex)
    z=np.diag([1,-1]); eye=np.eye(2)
    result=[]
    for k in range(d):
        a=np.array([[1]],complex)
        for j in range(d): a=np.kron(a,z if j<k else c if j==k else eye)
        result.append(a)
    return result

def lift(h, aa):
    out=np.zeros_like(aa[0])
    for i,j in product(range(len(aa)), repeat=2): out+=h[i,j]*dag(aa[i])@aa[j]
    return out

def exterior(m):
    d=len(m)
    occ=[[k for k in range(d) if mask & (1<<(d-1-k))] for mask in range(2**d)]
    out=np.zeros((2**d,2**d),complex)
    for i,ii in enumerate(occ):
        for j,jj in enumerate(occ):
            if len(ii)==len(jj):
                out[i,j]=1 if not ii else np.linalg.det(m[np.ix_(ii,jj)])
    return out

checks={}
a2=annihilators(2); even=[0,3]; odd=[2,1]
u2=np.eye(2,dtype=complex); t2=np.eye(4,dtype=complex)
pair_errors=[]
for theta,phase,dl,dr,c in [(.37,0,0,0,0),(.21,.43,.15,-.26,.17),(-.12,-.31,.27,.08,-.09)]:
    h=np.array([[dl,theta*np.exp(1j*phase)],[theta*np.exp(-1j*phase),dr]])
    u=expm(-1j*h); t=expm(-1j*(c*np.eye(4)+lift(h,a2)))
    A=t[np.ix_(even,even)]; B=t[np.ix_(odd,odd)]
    pair_errors.append(abs(np.linalg.det(A)-np.linalg.det(B)))
    pair_errors.append(abs(np.linalg.det(A)-np.exp(-1j*(2*c+tr(h)))))
    u2=u@u2; t2=t@t2
pair_errors.append(abs(np.linalg.det(t2[np.ix_(even,even)])-np.linalg.det(t2[np.ix_(odd,odd)])))
checks['pair_and_composed_determinants_max_error']=float(max(pair_errors))
assert max(pair_errors)<2e-13

# Three overlapping mode contacts: noncommuting L/R mixing, transport and phases.
d=3; aa=annihilators(d); eye=np.eye(d,dtype=complex)
base=[np.array([[.12,.31,0],[.31,-.23,0],[0,0,.07]],complex),
      np.array([[.19,0,0],[0,.08,.27-.11j],[0,.27+.11j,-.16]],complex),
      np.array([[-.08,0,.22+.09j],[0,.17,0],[.22-.09j,0,.13]],complex)]
links=[(0,1),(1,2),(0,2)]
def contact(k,a):
    h=base[k].copy(); i,j=links[k]
    h[i,j]*=np.exp(1j*a); h[j,i]=h[i,j].conjugate()
    hp=np.zeros((d,d),complex)
    hp[i,j]=1j*h[i,j]; hp[j,i]=hp[i,j].conjugate()
    u,du=expm_frechet(-1j*h,-1j*hp)
    return h,u,du

def process(tags):
    u=eye.copy(); U=np.eye(2**d,dtype=complex)
    for k,a in enumerate(tags):
        h,t,_=contact(k,a)
        u=t@u; U=expm(-1j*lift(h,aa))@U
    return u,U

ha,hb=base[:2]
lhs=lift(ha,aa)@lift(hb,aa)-lift(hb,aa)@lift(ha,aa)
checks['bilinear_commutator_error']=err(lhs,lift(ha@hb-hb@ha,aa))
assert checks['bilinear_commutator_error']<2e-13
rg=np.array([[.31,.12j,.08],[-.12j,-.23,.11],[.08,.11,.19]],complex)
sf=np.array([[-.16,.07,.09j],[.07,.28,-.13],[-.09j,-.13,.11]],complex)
R=expm(-rg); S=expm(-sf)
rho=expm(-lift(rg,aa)); rho/=tr(rho)
rawF=expm(-lift(sf,aa)); f=.8/np.linalg.eigvalsh(rawF).max(); F=f*rawF
assert err(rho,exterior(R)/np.linalg.det(eye+R))<2e-13
assert err(F,f*exterior(S))<2e-13
det_errors=[]; composition_errors=[]
samples=[([0,0,0],[0,0,0]),([.21,-.13,.07],[-.12,.04,.23]),
         ([-.31,.18,.09],[.05,-.27,.11]),([.17,.06,-.24],[.17,.06,-.24])]
for ap,am in samples:
    up,Up=process(ap); um,Um=process(am)
    direct=tr(F@Up@rho@dag(Um))
    compact=f*np.linalg.det(eye+S@up@R@dag(um))/np.linalg.det(eye+R)
    det_errors.append(abs(direct-compact))
    composition_errors.append(err(Up,exterior(up)))
checks['four_full_trace_determinants_max_error']=float(max(det_errors))
checks['three_contact_compositions_max_error']=float(max(composition_errors))
assert max(det_errors)<2e-13 and max(composition_errors)<2e-13

def boundary_kernel(up,um):
    zero=np.zeros_like(eye)
    return np.block([[eye,zero,zero,S],[-dag(um),eye,zero,zero],
                     [zero,-R,eye,zero],[zero,zero,-up,eye]])

block_errors=[]
for ap,am in samples:
    up,_=process(ap); um,_=process(am)
    block_errors.append(abs(np.linalg.det(boundary_kernel(up,um))-
                           np.linalg.det(eye+S@up@R@dag(um))))
checks['four_block_kernel_determinants_max_error']=float(max(block_errors))
assert max(block_errors)<2e-12

# All nine mixed two-contact responses: full Fock covariance vs determinant jets.
u,U=process([0,0,0]); E=dag(U)@F@U; p=tr(E@rho)
steps=[contact(k,0) for k in range(3)]
derivatives=[]
for r in range(3):
    v=eye.copy()
    for k,(_,t,dt) in enumerate(steps): v=(dt if k==r else t)@v
    derivatives.append(v)
J=[lift(-1j*dag(u)@v,aa) for v in derivatives]
D=eye+S@u@R@dag(u); Di=np.linalg.inv(D)
Ki=np.linalg.inv(boundary_kernel(u,u))
response_errors=[]; block_response_errors=[]
for r,s in product(range(3),repeat=2):
    full=tr(E@J[s]@rho@J[r])/p-tr(E@rho@J[r])*tr(E@J[s]@rho)/(p*p)
    dp=S@derivatives[s]@R@dag(u)
    dm=S@u@R@dag(derivatives[r])
    dmp=S@derivatives[s]@R@dag(derivatives[r])
    compact=tr(Di@dmp-Di@dm@Di@dp)
    response_errors.append(abs(full-compact))
    kp=np.zeros((4*d,4*d),complex); km=kp.copy()
    kp[3*d:4*d,2*d:3*d]=-derivatives[s]
    km[d:2*d,0:d]=-dag(derivatives[r])
    # Here the two source branches enter different blocks, so K_{-,+}=0.
    effective_action_mixed=tr(Ki@km@Ki@kp)
    block_response_errors.append(abs(effective_action_mixed+full))
checks['nine_mixed_responses_max_error']=float(max(response_errors))
checks['nine_block_kernel_responses_max_error']=float(max(block_response_errors))
assert max(response_errors)<2e-13 and max(block_response_errors)<2e-13

# Different endpoint bases must change preparation and effect together.
gi=np.diag(np.exp(1j*np.array([.12,-.31,.07])))
go=np.diag(np.exp(1j*np.array([-.19,.09,.28])))
up,_=process(samples[1][0]); um,_=process(samples[1][1])
Rp=gi@R@dag(gi); Sp=go@S@dag(go)
upp=go@up@dag(gi); ump=go@um@dag(gi)
orig=f*np.linalg.det(eye+S@up@R@dag(um))/np.linalg.det(eye+R)
changed=f*np.linalg.det(eye+Sp@upp@Rp@dag(ump))/np.linalg.det(eye+Rp)
checks['endpoint_covariance_error']=float(abs(orig-changed))
assert abs(orig-changed)<2e-13
checks['status']='PASS'
checks['scope']='bilinear sector and Gaussian boundary weights; not a selection of the Dirac kernel or F_gamma'
print(json.dumps(checks,ensure_ascii=False,indent=2))
