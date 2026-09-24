"""Kandydat na kontrprzyklad: entropia splatania podobszaru w d=2 (stan SJ).
(a) bez obciecia: wykladnik w N?   (b) z obcieciem Sorkina-Yazdiego: log?"""
import numpy as np, scipy.linalg as sl
def setup(N,seed):
    rng=np.random.default_rng(seed); u,v=rng.random(N),rng.random(N)
    C=((u[:,None]<u[None,:])&(v[:,None]<v[None,:])).astype(float)
    D0=0.5*(C.T-C)                      # iDelta/i ; [phi,phi]=i D0
    return u,v,D0
def SJ(D0,cut=0.0):
    lam,V=np.linalg.eigh(1j*D0)
    k=np.abs(lam)>max(cut,1e-10)
    W=(V[:,k&(lam>0)]*lam[k&(lam>0)])@V[:,k&(lam>0)].conj().T
    Dt=(V[:,k]*lam[k])@V[:,k].conj().T
    return W,Dt
def Sreg(idx,W,Dt,relloc=1e-10):
    A=Dt[np.ix_(idx,idx)]; B=W[np.ix_(idx,idx)]
    mu,Q=np.linalg.eigh(A); mx=np.abs(mu).max()
    k=np.abs(mu)>relloc*mx; Q=Q[:,k]
    sig=np.linalg.eigvals((Q.conj().T@B@Q)/mu[k][:,None]).real
    sig=sig[(np.abs(sig)>1e-10)&(np.abs(sig-1)>1e-10)]
    return float(np.sum(sig*np.log(np.abs(sig))))
print("(a) bez obciecia: poddiament o ustalonej objetosci (1/16 diamentu)")
print("   N   | elementow w obszarze | S        | S/element")
res=[]
for N in [300,600,1200,2400]:
    Ss=[];ns=[]
    for s in [1,2]:
        u,v,D0=setup(N,s); W,Dt=SJ(D0)
        idx=np.where((u>0.375)&(u<0.625)&(v>0.375)&(v<0.625))[0]
        Ss.append(Sreg(idx,W,Dt)); ns.append(len(idx))
    print(f"{N:6d} | {np.mean(ns):8.0f}             | {np.mean(Ss):8.2f} | {np.mean(Ss)/np.mean(ns):.3f}")
    res.append([N,np.mean(Ss),np.mean(ns)])
res=np.array(res)
print(f"  wykladnik S wzgledem N: {np.polyfit(np.log(res[:,0]),np.log(res[:,1]),1)[0]:+.2f}  (1.0 = prawo objetosciowe -> to gestosc)")
print(f"  S * t_P^2 (czyli S/N):  "+"  ".join(f"{S/N:.4f}" for N,S,_ in res))
print("\n(b) z obcieciem Sorkina-Yazdiego (prog c*sqrt(N)/(4pi) na widmie iDelta, globalnie i lokalnie)")
print("   N   | S(c=1)   S(c=2)  | wzgledem log N")
res2=[]
for N in [300,600,1200,2400]:
    row=[]
    for c in [1.0,2.0]:
        Ss=[]
        for s in [1,2]:
            u,v,D0=setup(N,s); cut=c*np.sqrt(N)/(4*np.pi); W,Dt=SJ(D0,cut)
            idx=np.where((u>0.375)&(u<0.625)&(v>0.375)&(v<0.625))[0]
            Ss.append(Sreg(idx,W,Dt,relloc=cut/max(np.abs(np.linalg.eigvalsh(1j*Dt[np.ix_(idx,idx)])).max(),1e-12)))
        row.append(np.mean(Ss))
    print(f"{N:6d} | {row[0]:7.3f}  {row[1]:7.3f} |")
    res2.append([N]+row)
res2=np.array(res2)
for i,c in [(1,1.0),(2,2.0)]:
    p=np.polyfit(np.log(res2[:,0]),res2[:,i],1)
    q=np.polyfit(np.log(res2[:,0]),np.log(np.maximum(res2[:,i],1e-6)),1)[0]
    print(f"  c={c}: dopasowanie S = {p[0]:.3f}*ln N + {p[1]:.3f}   |  wykladnik potegowy: {q:+.2f}")
