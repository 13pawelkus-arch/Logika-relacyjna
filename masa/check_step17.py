"""Algebraic audit of phase placement and branch responses; no physical model fit."""
import json
from itertools import product
import numpy as np
from scipy.linalg import expm

dag = lambda x: x.conj().T
err = lambda x, y: float(np.max(np.abs(x-y)))
eye = np.eye(2, dtype=complex)
sx = np.array([[0,1],[1,0]], complex)

def chirality(a, charge):
    z = np.exp(1j*charge*a)
    return np.array([[0,z],[z.conjugate(),0]], complex)

def lift(u):
    result = np.zeros((4,4), complex)
    result[0,0] = 1
    result[1:3,1:3] = u
    result[3,3] = np.linalg.det(u)
    return result

checks = dict(exponential=0., single_determinant=0., branch_determinant=0.,
              full_fock_trace=0., mixed_hessian=0., same_branch_hessian=0.,
              covariance_curvature=0., graph_gauge_covariance=0.,
              full_endpoint_covariance=0.)
theta_values = [0., .2, .73, 1.37, np.pi/2, np.pi, 2.9]
charges = [.3, 1., -1.]
eps_values = [0., 1.e-4, .1, .43, -.8]
samples = 0
for theta, charge, epsilon in product(theta_values, charges, eps_values):
    a = .37
    c, s = np.cos(theta), np.sin(theta)
    u = c*eye-1j*s*chirality(a,charge)
    checks['exponential'] = max(checks['exponential'],
        err(u,expm(-1j*theta*chirality(a,charge))))
    checks['single_determinant'] = max(checks['single_determinant'],
        abs(np.linalg.det(eye+u)-4*np.cos(theta/2)**2))
    up = expm(-1j*theta*chirality(a+epsilon/2,charge))
    um = expm(-1j*theta*chirality(a-epsilon/2,charge))
    z = np.linalg.det(eye+up@dag(um))/4
    closed = 1-s*s*np.sin(charge*epsilon/2)**2
    checks['branch_determinant'] = max(checks['branch_determinant'],abs(z-closed))
    direct = np.trace(lift(up)@dag(lift(um)))/4
    checks['full_fock_trace'] = max(checks['full_fock_trace'],abs(z-direct))
    samples += 1

for theta, charge in product(theta_values, charges):
    a=.37; c,s=np.cos(theta),np.sin(theta)
    b=chirality(a,charge)
    bp=np.array([[0,1j*charge*b[0,1]],[-1j*charge*b[1,0],0]],complex)
    u=c*eye-1j*s*b
    du=-1j*s*bp
    ddu=1j*charge*charge*s*b
    dplus=du@dag(u); dminus=u@dag(du)
    inverse=np.linalg.inv(eye+u@dag(u))
    mixed=np.trace(inverse@du@dag(du)-inverse@dminus@inverse@dplus)
    same=np.trace(inverse@ddu@dag(u)-inverse@dplus@inverse@dplus)
    target=charge*charge*s*s/2
    checks['mixed_hessian']=max(checks['mixed_hessian'],abs(mixed-target))
    checks['same_branch_hessian']=max(checks['same_branch_hessian'],abs(same+target))
    j=-1j*dag(u)@du
    jf=np.zeros((4,4),complex); jf[1:3,1:3]=j; jf[3,3]=np.trace(j)
    covariance=np.trace(jf@jf)/4-(np.trace(jf)/4)**2
    checks['covariance_curvature']=max(checks['covariance_curvature'],abs(covariance-target))

# The uniform complex multiplier is not a unitary contact family.
theta=.73; charge=1.; a=.41
ha=np.exp(1j*charge*a)*theta*sx
ua=expm(-1j*ha)
invalid=dict(hermiticity_error=err(ha,dag(ha)),
             unitarity_error=err(dag(ua)@ua,eye),
             det_u_error=abs(np.linalg.det(ua)-1),
             diagonal_normalized_trace=float(np.real(np.linalg.det(eye+ua@dag(ua))/4)))
assert invalid['hermiticity_error']>.1
assert invalid['unitarity_error']>.1
assert invalid['det_u_error']<1.e-12
assert abs(invalid['diagonal_normalized_trace']-np.cosh(theta*np.sin(charge*a))**2)<1.e-12

# End labels refer to existing contacts. One oriented link phase multiplies
# its entire L/R block; the reverse block is its Hermitian conjugate.
rng=np.random.default_rng(179)
edges=[(0,1),(1,2),(2,0)]
weights=[rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)) for _ in edges]
angles=np.array([.2,-.4,.7]); chi=np.array([.1,.3,-.2]); charge=.8
def graph_h(aa):
    h=np.zeros((6,6),complex)
    for v in range(3): h[2*v:2*v+2,2*v:2*v+2]=(.2+.1*v)*sx
    for (v,w),t,angle in zip(edges,weights,aa):
        block=t*np.exp(1j*charge*angle)
        h[2*v:2*v+2,2*w:2*w+2]=block
        h[2*w:2*w+2,2*v:2*v+2]=dag(block)
    return h
g=np.diag(np.repeat(np.exp(1j*charge*chi),2))
shift=np.array([chi[v]-chi[w] for v,w in edges])
hp,hm=graph_h(angles),graph_h(angles+np.array([.03,-.01,.02]))
up,um=expm(-1j*hp),expm(-1j*hm)
upg,umg=expm(-1j*graph_h(angles+shift)),expm(-1j*graph_h(angles+np.array([.03,-.01,.02])+shift))
checks['graph_gauge_covariance']=max(err(upg,g@up@dag(g)),err(umg,g@um@dag(g)))
random_positive=lambda: (lambda x:dag(x)@x/20+np.eye(6))(
    rng.normal(size=(6,6))+1j*rng.normal(size=(6,6)))
r,s=random_positive(),random_positive()
z=lambda u1,u2,r1,s1:np.linalg.det(np.eye(6)+s1@u1@r1@dag(u2))/np.linalg.det(np.eye(6)+r1)
checks['full_endpoint_covariance']=abs(z(up,um,r,s)-z(upg,umg,g@r@dag(g),g@s@dag(g)))
assert abs(sum(angles+shift)-sum(angles))<1.e-12
for key,value in checks.items(): assert value<2.e-11, (key,value)
print(json.dumps(dict(status='PASS',scope='phase and branch algebra only, not F_gamma',
                     branch_samples=samples,max_errors=checks,
                     invalid_uniform_multiplier=invalid),indent=2))
