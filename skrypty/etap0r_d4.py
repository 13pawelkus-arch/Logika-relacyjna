"""d=4: K_R = L/(2*pi*sqrt(6)), L = macierz linkow. Pary o tym samym N_U, rozne N."""
import numpy as np, json, os, sys
K4=1/(2*np.pi*np.sqrt(6))
def sprinkle4(N,rng,T=1.0):
    # gestosc w t ~ (T-|t|)^3, promien ~ r^2 w [0, T-|t|]
    x=rng.random(N); s=np.where(rng.random(N)<0.5,-1,1)
    tt=T*(1-(1-x)**0.25)*0  # placeholder
    # odwrotna dystrybuanta dla |t|: F(a)=1-(1-a/T)^4
    a=T*(1-(1-rng.random(N))**0.25); t=s*a
    R=T-np.abs(t); u=rng.random(N)**(1/3)*R
    v=rng.normal(size=(N,3)); v/=np.linalg.norm(v,axis=1)[:,None]
    return t, v*u[:,None]
def causal(t,X):
    dt=t[None,:]-t[:,None]
    d2=((X[None,:,:]-X[:,None,:])**2).sum(-1)
    return (dt>0)&(dt**2>d2)
def links(C):
    Cf=C.astype(np.float32)
    return C&~((Cf@Cf)>0.5)
def entropy(al,V,U,N,c,k=K4):
    VU=V[U]; NU=len(U)
    thr=c*np.sqrt(N)/(4*np.pi)*(k/0.5)
    keep=np.abs(al)>thr; pos=keep&(al>0)
    Du=(VU[:,keep]*al[keep])@VU[:,keep].conj().T
    Wu=(VU[:,pos]*al[pos])@VU[:,pos].conj().T
    Ru=Wu-0.5*Du
    mu,Q=np.linalg.eigh(Du); thr2=c*np.sqrt(NU)/(4*np.pi)*(k/0.5)
    sel=np.abs(mu)>thr2
    if sel.sum()<2: return 0.0,NU,0
    P=Q[:,sel]; M=(P.conj().T@Ru@P)/mu[sel][:,None]
    lam=0.5+np.linalg.eigvals(M).real
    good=lam[(lam>=1-1e-8)|(lam<=1e-8)]; good=good[np.abs(good)>1e-10]
    return float(np.sum(good*np.log(np.abs(good)))),NU,int(sel.sum())
CK='d4.json'; res=json.load(open(CK)) if os.path.exists(CK) else {}
N=int(sys.argv[1]); r=float(sys.argv[2]); nse=int(sys.argv[3])
for s in range(1,nse+1):
    key=f"{N}|{r}|{s}"
    if key in res: continue
    rng=np.random.default_rng(s)
    t,X=sprinkle4(N,rng)
    C=causal(t,X); L=links(C); del C
    D=K4*(L.T.astype(float)-L.astype(float)); del L
    al,V=np.linalg.eigh(1j*D); del D
    T2=1.0/r**0.25
    U=np.where((np.abs(t)+np.linalg.norm(X,axis=1))<T2)[0]
    res[key]={str(c):entropy(al,V,U,N,c)[0] for c in [0.5,1.0,2.0]}
    res[key]["NU"]=len(U); res[key]["modes"]=entropy(al,V,U,N,1.0)[2]
    json.dump(res,open(CK,'w'))
    print(f"N={N} r={r} s={s} N_U={len(U)} modow(c=1)={res[key]['modes']} "
          + " ".join(f"S(c={c})={res[key][str(c)]:.3f}" for c in [0.5,1.0,2.0]),flush=True)
