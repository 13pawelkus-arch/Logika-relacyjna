"""Checks of proposed test-128 candidates; no source-framework writeback."""
from pathlib import Path
import json
import sympy as s

count=0
def zero(label,x):
    global count
    if isinstance(x,s.MatrixBase):
        for v in x: zero(label,v)
        return
    value=s.trigsimp(s.simplify(x))
    assert value==0,(label,value)
    count+=1

I=s.eye(2); O=s.zeros(2)
sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
Sigma=[I]+sig; Bars=[I]+[-v for v in sig]
Q,a,theta=s.symbols('Q a theta',real=True)
neutral=s.symbols('h')
t=s.exp(s.I*Q*a)*neutral
zero('one oriented link first derivative',s.diff(t,a)-s.I*Q*t)
zero('one oriented link second derivative',s.diff(t,a,2)+Q*Q*t)

# A scalar phase on the entire unitary has Xi=0.
u_global=s.exp(s.I*Q*a)*I
Xglobal=-s.I*u_global.conjugate().T*s.diff(u_global,a)
zero('whole-unitary scalar phase current',Xglobal-Q*I)
zero('whole-unitary scalar phase Xi',s.diff(Xglobal,a))

# End labels, NOT chirality labels. Additive commuting LR mass does not change
# this result. This is a full Hermitian link evolution, not the bare t block.
K=s.Matrix([[0,s.exp(s.I*Q*a)],[s.exp(-s.I*Q*a),0]])
u=s.cos(theta)*I-s.I*s.sin(theta)*K
u0=u.subs(a,0); up=s.diff(u,a).subs(a,0); upp=s.diff(u,a,2).subs(a,0)
X=-s.I*u0.conjugate().T*up
Xi=-s.I*(up.conjugate().T*up+u0.conjugate().T*upp)
Xtarget=Q*(s.cos(theta)*s.sin(theta)*sig[1]-s.sin(theta)**2*sig[2])
Xitarget=Q*Q*s.sin(theta)*s.cos(theta)*sig[0]
zero('endpoint link unitary',u0.conjugate().T*u0-I)
zero('full link current',X-Xtarget)
zero('full link Xi',Xi-Xitarget)
zero('second derivative identity',u0.conjugate().T*upp+X*X-s.I*Xi)
v=s.symbols('v',real=True)
N=(I+v*sig[0])/2
zero('nonzero instantaneous expectation',s.trace(N*Xi)-v*Q*Q*s.sin(theta)*s.cos(theta))

# Canonical LR Schur reduction: test the full determinant Hessian, all source
# directions, rather than assigning the induced contact a scalar polarization.
mode_exchange=sig[0]
seagull_samples=[]; schur_entries=0
def four(p):
    return sum((p[i]*Sigma[i] for i in range(4)),s.zeros(2))
def barfour(p):
    return sum((p[i]*Bars[i] for i in range(4)),s.zeros(2))
for mass,pa,pb in [(1,(3,0,0,1),(5,0,1,2)),
                   (2,(4,1,0,1),(6,0,2,1)),
                   (3,(5,1,1,0),(7,1,0,2))]:
    L=s.diag(four(pa),four(pb)); R=s.diag(barfour(pa),barfour(pb))
    e=s.eye(4); z=s.zeros(4)
    full=(-mass*e).row_join(L).col_join(R.row_join(-mass*e))
    G=full.inv(); S=(L*R-mass*mass*e)/mass; GS=S.inv()
    VL=[s.kronecker_product(mode_exchange,j) for j in Sigma]
    VR=[s.kronecker_product(mode_exchange,j) for j in Bars]
    VV=[z.row_join(VL[i]).col_join(VR[i].row_join(z)) for i in range(4)]
    Si=[(VL[i]*R+L*VR[i])/mass for i in range(4)]
    for mu in range(4):
        for nu in range(4):
            Sij=(VL[mu]*VR[nu]+VL[nu]*VR[mu])/mass
            eta=int(mu==nu)*(1 if mu==0 else -1)
            zero('induced contact tensor',Sij-s.Rational(2,mass)*eta*e)
            full_h=-s.trace(G*VV[mu]*G*VV[nu])
            contact=s.trace(GS*Sij)
            bubble=-s.trace(GS*Si[mu]*GS*Si[nu])
            zero('complete Schur Hessian',full_h-contact-bubble)
            schur_entries+=1
            if mu==nu==0:seagull_samples.append(str(contact))

# Transversality does not set the scalar coefficient or its slope.
q=s.Matrix(s.symbols('q0 q1 q2 q3',real=True)); metric=s.diag(1,-1,-1,-1)
q2=(q.T*metric*q)[0]
C0,C1=s.symbols('C0 C1',real=True)
transverse=(q2*metric-q*q.T)*(C0+C1*q2)
zero('constant and linear transverse structures',(q.T*metric)*transverse)

# A local contact in link-phase variables can acquire argument dependence
# when those phases are projected onto a source profile.
omega=s.symbols('omega',real=True)
profile_square=2*(1-s.cos(omega))/omega**2
profile_series=s.series(profile_square,omega,0,6).removeO()
zero('profile contact expansion',profile_series-(1-omega**2/12+omega**4/360))

# Closed transported channels are real below their pole, but change the read.
zeta,g,M=s.symbols('zeta g M',real=True,nonzero=True)
sigma=g*g/(zeta-M)
zero('closed channel slope',s.diff(sigma,zeta).subs(zeta,0)+g*g/M**2)

# Two carried arms already give order-Q^2 interference; number of paths is
# not, by itself, a count of additional internal EM propagators.
a1,a2=s.symbols('a1 a2',real=True)
prob=(1+s.cos(Q*(a1-a2)))/2
zero('two-chain interference order',s.diff(prob,a1,2).subs({a1:0,a2:0})+Q*Q/2)
lam=s.symbols('lambda',real=True)
holonomy=s.exp(s.I*Q*(a1-a2))
zero('holonomy current starts at one source insertion',s.diff(lam*(holonomy-1),a1).subs({a1:0,a2:0})-s.I*Q*lam)

out={'status':'PASS','exact_scalar_checks':count,
     'full_vs_reduced_hessians':schur_entries,
     'seagull_00_trace_samples':seagull_samples,
     'Xi_for_full_phase_hopping_unitary':'Q^2 sin(theta) cos(theta) tau_x',
     'Xi_for_global_phase_unitary':'0',
     'link_profile_square_series':str(profile_series),
     'closed_channel_slope_at_zero':'-g^2/M^2',
     'scope':'bare link jets, full contact identity, canonical LR reduction; no proof of a frame-selected scalar EM polynomial or perturbative-order identification'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
