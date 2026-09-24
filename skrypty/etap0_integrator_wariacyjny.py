"""Etap 0, wersja wariacyjna. Jedno liniowe dzialanie: pole (G_R=C^T/2) + oscylator swobodny na lancuchu
(dokladne rozwiazanie w tau_k=k*eps) + symetryczne sprzezenie V (lambda miedzy q_k i phi(c_k)).
Heisenberg: X = (1 - G0 V)^{-1} X_in.  Stan poczatkowy: omega_SJ (x) omega_osc (iloczyn)."""
import numpy as np, scipy.linalg as sl, sys
seed=int(sys.argv[1]); N=int(sys.argv[2]); rng=np.random.default_rng(seed)
u,v=rng.random(N),rng.random(N)
C=((u[:,None]<u[None,:])&(v[:,None]<v[None,:])).astype(float)
GRf=0.5*C.T; D0=GRf-GRf.T
T,Q=sl.schur(D0,output='real'); cols=[]; tol=1e-9*np.abs(D0).max(); i=0
while i<N:
    if i+1<N and abs(T[i+1,i])>tol:
        m=T[i,i+1]; a,b=Q[:,i],Q[:,i+1]
        if m<0: a,b,m=b,a,-m
        cols+=[a*np.sqrt(m),b*np.sqrt(m)]; i+=2
    else: i+=1
A=np.array(cols).T; r=A.shape[1]; n=r+2
J=np.zeros((n,n)); J[np.arange(0,n,2),np.arange(1,n,2)]=1; J=J-J.T
order=np.argsort(u+v); L=np.zeros(N,int); prev=-np.ones(N,int)
for x in order:
    ps=np.where(C[:,x]>0)[0]
    if len(ps): j=ps[np.argmax(L[ps])]; L[x]=L[j]+1; prev[x]=j
x=np.argmax(L); ch=[]
while x>=0: ch.append(x); x=prev[x]
ch=np.array(ch[::-1]); M=len(ch)-1; K=M+1
eps=np.sqrt(2)/M; om=2*np.pi*3/np.sqrt(2); tau=eps*np.arange(K)
# X_in = B z ;  z=(xi_1..xi_r, q0, p0)
B=np.zeros((N+K,n)); B[:N,:r]=A
B[N:,r]=np.cos(om*tau); B[N:,r+1]=np.sin(om*tau)/om
Dosc=-np.sin(om*(tau[:,None]-tau[None,:]))/om                 # [q(k),q(l)] = i Dosc(k,l)
G0=np.zeros((N+K,N+K)); G0[:N,:N]=GRf
G0[N:,N:]=np.tril(Dosc,-1)                                      # retardowany: k>l
Gin=np.eye(n)*0.5; Gin[r,r]=1/(2*om); Gin[r+1,r+1]=om/2
# relacja przyczynowa na wszystkich zmiennych (detektor k siedzi w elemencie ch[k])
site=np.concatenate([np.arange(N),ch])
Rel=C[np.ix_(site,site)]+C[np.ix_(site,site)].T
Same=site[:,None]==site[None,:]
Spacelike=(Rel==0)&(~Same)
def S(R):
    Jr=R@J@R.T; W=R@Gin@R.T+0.5j*Jr
    mu,V=np.linalg.eigh(1j*Jr); k=np.abs(mu)>1e-9*max(1,np.abs(mu).max())
    V=V[:,k]; sig=np.linalg.eigvals((V.conj().T@W@V)/mu[k][:,None]).real
    sig=sig[(np.abs(sig)>1e-10)&(np.abs(sig-1)>1e-10)]
    return float(np.sum(sig*np.log(np.abs(sig))))
chk0=np.abs(B@J@B.T-(G0-G0.T)).max()                           # in-stan zgodny z G0
print(f"seed={seed} N={N} r={r} M={M} eps={eps:.4f} | kontrola wejscia |BJB^T-(G0-G0^T)|={chk0:.1e}")
print("  g    | |XJX^T-(Gf-Gf^T)|  mikroprzycz. max  (w tym pole-det) | rzad  | S(calosc) S(S)     S(S^c)")
for g in [0.0,5.0,-5.0,20.0]:
    lam=g*eps
    V=np.zeros((N+K,N+K)); V[ch,N+np.arange(K)]=lam; V[N+np.arange(K),ch]=lam
    Minv=np.linalg.inv(np.eye(N+K)-G0@V)
    X=Minv@B; Gf=Minv@G0
    Sig=X@J@X.T
    peierls=np.abs(Sig-(Gf-Gf.T)).max()
    mc=np.abs(Sig[Spacelike]).max()
    FD=Spacelike.copy(); FD[:N,:N]=False; FD[N:,N:]=False
    mcfd=np.abs(Sig[FD]).max()
    Sd=X[[N+M,N+M-1]]
    Ac=sl.null_space(Sd@J).T
    print(f"{g:6.1f} | {peierls:.1e}           {mc:.1e}          ({mcfd:.1e})     | {np.linalg.matrix_rank(X)}/{n} | {S(X):.1e}  {S(Sd):.5f}  {S(Ac):.5f}")
