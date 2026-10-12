"""Full two-path L/R module: gauge identities, Fock trace and branch Hessians."""
import json
from itertools import product
import numpy as np
from scipy.linalg import expm

dag=lambda x:x.conj().T
err=lambda x,y:float(np.max(np.abs(x-y)))
tr=np.trace
sx=np.array([[0,1],[1,0]],complex)
beam=np.kron(np.array([[1,1],[1,-1]],complex)/np.sqrt(2),np.eye(2))
v=np.array([1,0,0,0],complex)
effect=np.diag([1.,1.,0.,0.])
D0=np.array([[1,0],[-1,0],[0,1],[0,-1]],float)
loop=np.array([1,1,-1,-1],float)
common=np.ones(4)
profile=loop/4

def block_diag(a,b):
    z=np.zeros_like(a)
    return np.block([[a,z],[z,b]])

def module(tags,theta1,theta2,charge):
    m1=expm(-1j*theta1*sx); m2=expm(-1j*theta2*sx)
    incoming=block_diag(np.exp(1j*charge*tags[0])*np.eye(2),
                        np.exp(1j*charge*tags[2])*np.eye(2))
    outgoing=block_diag(np.exp(1j*charge*tags[1])*np.eye(2),
                        np.exp(1j*charge*tags[3])*np.eye(2))
    mass=block_diag(m1,m2)
    return beam@outgoing@mass@incoming@beam

def jets(tags,theta1,theta2,charge):
    x=np.exp(1j*charge*(tags[0]+tags[1]))*expm(-1j*theta1*sx)
    y=np.exp(1j*charge*(tags[2]+tags[3]))*expm(-1j*theta2*sx)
    z=np.zeros((2,2),complex)
    part=[beam@block_diag(x,z)@beam,beam@block_diag(z,y)@beam]
    group=[0,0,1,1]
    u=part[0]+part[1]
    first=[1j*charge*part[g] for g in group]
    second=[[(-charge*charge*part[group[r]] if group[r]==group[s]
             else np.zeros((4,4),complex)) for s in range(4)] for r in range(4)]
    return u,first,second

def exterior(m):
    d=len(m)
    occ=[[k for k in range(d) if mask & (1<<(d-1-k))] for mask in range(2**d)]
    out=np.zeros((2**d,2**d),complex)
    for i,ii in enumerate(occ):
        for j,jj in enumerate(occ):
            if len(ii)==len(jj):
                out[i,j]=1 if not ii else np.linalg.det(m[np.ix_(ii,jj)])
    return out

checks=dict(unitarity=0.,contact_product=0.,gauge_invariance=0.,
            pure_trace=0.,gaussian_determinant=0.,rank_one_limit_identity=0.,
            mixed_hessian=0.,same_branch_hessian=0.,probability_hessian=0.,
            gauge_nullspace=0.,common_phase_nullspace=0.,
            positive_gram=0.,gauge_quotient=0.,repeated_mass=0.)
F=exterior(effect)
rho_pure=np.zeros((16,16),complex); rho_pure[8,8]=1
cases=[(.2,.2),(.2,.7),(.4,1.2),(.1,2.1)]
charges=[-1.,.5,1.3]
source_pairs=[(np.zeros(4),np.zeros(4)),
              (np.array([.13,-.2,.3,.07]),np.array([-.14,.1,.05,-.2])),
              (np.array([-.07,.11,-.16,.23]),np.array([.12,-.2,.21,.09]))]
samples=0
for (theta1,theta2),charge,(ap,am) in product(cases,charges,source_pairs):
    up=module(ap,theta1,theta2,charge); um=module(am,theta1,theta2,charge)
    checks['unitarity']=max(checks['unitarity'],err(dag(up)@up,np.eye(4)))
    compact,_,_=jets(ap,theta1,theta2,charge)
    checks['contact_product']=max(checks['contact_product'],err(up,compact))
    shiftedp=module(ap+D0@np.array([.3,-.17]),theta1,theta2,charge)
    shiftedm=module(am+D0@np.array([-.2,.31]),theta1,theta2,charge)
    checks['gauge_invariance']=max(checks['gauge_invariance'],err(up,shiftedp),err(um,shiftedm))
    z=dag(v)@dag(um)@effect@up@v
    pp=[ap[0]+ap[1],ap[2]+ap[3]]
    pm=[am[0]+am[1],am[2]+am[3]]
    coherence=np.cos(theta1-theta2)
    closed=(np.exp(1j*charge*(pp[0]-pm[0]))+
            np.exp(1j*charge*(pp[1]-pm[1]))+
            coherence*np.exp(1j*charge*(pp[0]-pm[1]))+
            coherence*np.exp(1j*charge*(pp[1]-pm[0])))/4
    direct=tr(F@exterior(up)@rho_pure@dag(exterior(um)))
    checks['pure_trace']=max(checks['pure_trace'],abs(z-closed),abs(z-direct))
    for t in [.3,2.,17.]:
        R=t*np.outer(v,dag(v))
        rho=exterior(R)/np.linalg.det(np.eye(4)+R)
        exact=np.linalg.det(np.eye(4)+effect@up@R@dag(um))/np.linalg.det(np.eye(4)+R)
        full=tr(F@exterior(up)@rho@dag(exterior(um)))
        checks['gaussian_determinant']=max(checks['gaussian_determinant'],abs(exact-full))
        checks['rank_one_limit_identity']=max(checks['rank_one_limit_identity'],
                                            abs(exact-(1+t*z)/(1+t)))
    samples+=1

# All sixteen entries from the same process, including contact second derivatives.
for (theta1,theta2),charge in product(cases,charges):
    u,first,second=jets(np.zeros(4),theta1,theta2,charge)
    p=dag(v)@dag(u)@effect@u@v
    zp=np.array([dag(v)@dag(u)@effect@du@v for du in first])
    C=np.empty((4,4),complex); H=np.empty((4,4),complex)
    for r,s in product(range(4),repeat=2):
        C[r,s]=(dag(v)@dag(first[r])@effect@first[s]@v)/p-zp[r].conjugate()*zp[s]/(p*p)
        H[r,s]=(dag(v)@dag(u)@effect@second[r][s]@v)/p-zp[r]*zp[s]/(p*p)
    c=np.cos(theta1-theta2)
    predictedC=charge*charge*(1-c)/(4*(1+c))*np.outer(loop,loop)
    predictedH=-charge*charge/4*np.outer(loop,loop)
    Kp=-2*np.real(H+C)
    predictedKp=charge*charge*c/(1+c)*np.outer(loop,loop)
    checks['mixed_hessian']=max(checks['mixed_hessian'],err(C,predictedC))
    checks['same_branch_hessian']=max(checks['same_branch_hessian'],err(H,predictedH))
    checks['probability_hessian']=max(checks['probability_hessian'],err(Kp,predictedKp))
    checks['gauge_nullspace']=max(checks['gauge_nullspace'],err(C@D0,np.zeros((4,2))),
                                   err(H@D0,np.zeros((4,2))),err(Kp@D0,np.zeros((4,2))))
    checks['common_phase_nullspace']=max(checks['common_phase_nullspace'],
        err(C@common,np.zeros(4)),err(H@common,np.zeros(4)))
    checks['positive_gram']=max(checks['positive_gram'],max(0.,-np.linalg.eigvalsh(C).min()))
    L=np.array([[1,0],[1,0],[0,1],[0,1]],float)/np.sqrt(2)
    checks['gauge_quotient']=max(checks['gauge_quotient'],err(C,L@(L.T@C@L)@L.T))
    # Independent scalar derivatives of p(Phi)=(1+c*cos(Q Phi))/2.
    p0=(1+c)/2
    scalar_curvature=charge*charge*c/(1+c)
    checks['probability_hessian']=max(checks['probability_hessian'],
        abs(profile@Kp@profile-scalar_curvature),abs(p-p0))

for n1,n2 in [(1,3),(2,7),(5,5)]:
    theta=.19
    repeated1=np.linalg.matrix_power(expm(-1j*theta*sx),n1)
    repeated2=np.linalg.matrix_power(expm(-1j*theta*sx),n2)
    overlap=(dag(repeated2)@repeated1)[0,0]
    checks['repeated_mass']=max(checks['repeated_mass'],abs(overlap-np.cos((n1-n2)*theta)))

for key,value in checks.items(): assert value<2.e-11,(key,value)
print(json.dumps(dict(status='PASS',branch_samples=samples,gaussian_traces=3*samples,
     response_matrices=12,max_errors=checks,
     scope='full specified two-path module and gauge quotient, not F_gamma or physical electron dynamics'),indent=2))
