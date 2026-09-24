"""Seria N: nachylenie log R_delta w delta vs 2S(S), pojemnosc fragmentow. omega=0.5, g=5, odczyt w srodku.
uzycie: series.py seed N mode w   (mode: comp | diam2 | diam4)"""
import sys, json, time
from scipy.sparse.csgraph import connected_components
seed,N,mode,w=sys.argv[1],sys.argv[2],sys.argv[3],float(sys.argv[4]); sys.argv=['x',seed,N]
t0=time.time()
src=open('stage0v.py').read().split('print(f"seed=')[0].replace('om=2*np.pi*3/np.sqrt(2)','om=0.5'); exec(src)
t=(u+v)/np.sqrt(2); m=int(np.argmin(np.abs(t[ch]-np.sqrt(2)/2)))
g=5.0; lam=g*eps
V=np.zeros((N+K,N+K)); kk=np.arange(m+1); V[ch[kk],N+kk]=lam; V[N+kk,ch[kk]]=lam
X=np.linalg.solve(np.eye(N+K)-G0@V,B)
Sd=X[[N+m,N+m-1]]; cm,cm1=ch[m],ch[m-1]; Rel=C+C.T
def Sred(R,G,rel=1e-10):
    Jr=R@J@R.T; W=R@G@R.T+0.5j*Jr
    mu,Vv=np.linalg.eigh(1j*Jr); mx=np.abs(mu).max()
    if mx==0: return 0.0
    k=np.abs(mu)>rel*mx; Vv=Vv[:,k]
    sig=np.linalg.eigvals((Vv.conj().T@W@Vv)/mu[k][:,None]).real
    sig=sig[(np.abs(sig)>1e-10)&(np.abs(sig-1)>1e-10)]
    return float(np.sum(sig*np.log(np.abs(sig))))
spc=(C[:,cm]==0)&(C[cm,:]==0)&(C[:,cm1]==0)&(C[cm1,:]==0)
rr=np.random.default_rng(int(seed)+7)
E=np.where((np.abs(t-t[cm])<w)&spc&(~np.isin(np.arange(N),ch)))[0]
if mode=='comp':
    nc,lab=connected_components(Rel[np.ix_(E,E)],directed=False)
    frs=[E[lab==c] for c in range(nc) if np.sum(lab==c)>=2]
else:
    smax=int(mode[-1]); Cp=C+np.eye(N); CE=Cp[np.ix_(E,E)]
    tot=Cp[E,:]@Cp[:,E]; inE=CE@CE
    P,Qm=np.where((C[np.ix_(E,E)]>0)&(tot<=smax)&(tot==inE))
    cand=[np.where((Cp[E[a],:]>0)&(Cp[:,E[b]]>0))[0] for a,b in zip(P,Qm)]
    o_=rr.permutation(len(cand)); frs=[]; used=np.zeros(N,bool)
    for i in o_:
        iv=cand[i]
        if used[iv].any(): continue
        if frs and Rel[np.ix_(iv,np.where(used)[0])].any(): continue
        frs.append(iv); used[iv]=True
nf=len(frs); U=np.concatenate(frs)
cF=max(np.abs(X[a]@J@X[b].T).max() for i,a in enumerate(frs) for b in frs[i+1:]) if nf>1 else 0
cS=np.abs(Sd@J@X[U].T).max()
perms=[rr.permutation(nf) for _ in range(5)]
out={"N":N,"seed":int(seed),"mode":mode,"w":w,"E":len(E),"nf":nf,"sizes":[len(f) for f in frs],
     "comm_FF":float(cF),"comm_SF":float(cS),"s":{}}
for s in [1,4,16]:
    G=np.eye(n)*0.5; G[r,r]=s**2/(2*om); G[r+1,r+1]=om/(2*s**2)
    sS=Sred(Sd,G)
    SF=[Sred(X[f],G) for f in frs]; SU=Sred(X[U],G)
    def I(idx):
        R=X[np.sort(idx)]; return sS+Sred(R,G)-Sred(np.vstack([Sd,R]),G)
    cur=np.zeros(nf)
    for o in perms:
        acc=[]
        for k in range(nf):
            acc.append(frs[o[k]]); cur[k]+=I(np.concatenate(acc))/len(perms)
    AL=bool(cur[-1]<=2*min(sS,SU)+1e-9)
    out["s"][s]={"SS":sS,"cur":(cur/sS).tolist(),"SF":SF,"SU":SU,"AL":AL}
out["time"]=time.time()-t0
json.dump(out,open(f"ser_{mode}_{N}_{seed}.json","w"))
print(f"{mode} N={N} seed={seed}: |E|={len(E)} nf={nf} max_rozm={max(out['sizes'])} [F,F]={cF:.0e} [S,F]={cS:.0e} "
      + " ".join(f"s={s}:S={out['s'][s]['SS']:.2f},C={sum(out['s'][s]['SF'])/out['s'][s]['SS']:.2f},AL={out['s'][s]['AL']}" for s in out['s'])
      + f"  t={out['time']:.0f}s")
