import sys,json
from scipy.sparse.csgraph import connected_components
seed,N,w,mode=sys.argv[1],sys.argv[2],float(sys.argv[3]),sys.argv[4]; sys.argv=['x',seed,N]
src=open('stage0v.py').read().split('print(f"seed=')[0].replace('om=2*np.pi*3/np.sqrt(2)','om=0.5'); exec(src)
t=(u+v)/np.sqrt(2); m_=int(np.argmin(np.abs(t[ch]-np.sqrt(2)/2)))
g=5.0; lam=g*eps
V=np.zeros((N+K,N+K)); kk=np.arange(m_+1); V[ch[kk],N+kk]=lam; V[N+kk,ch[kk]]=lam
X=np.linalg.solve(np.eye(N+K)-G0@V,B)
Sd=X[[N+m_,N+m_-1]]; cm,cm1=ch[m_],ch[m_-1]; Rel=C+C.T
Gin=np.eye(n)*0.5; Gin[r,r]=1/(2*om); Gin[r+1,r+1]=om/2
eq=np.zeros(n); eq[r]=1
def S(R,G):
    Jr=R@J@R.T; W=R@G@R.T+0.5j*Jr
    mu,Vv=np.linalg.eigh(1j*Jr); mx=np.abs(mu).max()
    if mx==0: return 0.0
    k=np.abs(mu)>1e-10*mx; Vv=Vv[:,k]
    sig=np.linalg.eigvals((Vv.conj().T@W@Vv)/mu[k][:,None]).real
    sig=sig[(np.abs(sig)>1e-10)&(np.abs(sig-1)>1e-10)]
    return float(np.sum(sig*np.log(np.abs(sig))))
def Id(R,Vd): return S(R,Gin+Vd*np.outer(eq,eq))-S(R,Gin)
spc=(C[:,cm]==0)&(C[cm,:]==0)&(C[:,cm1]==0)&(C[cm1,:]==0)
E=np.where((np.abs(t-t[cm])<w)&spc&(~np.isin(np.arange(N),ch)))[0]
rr=np.random.default_rng(int(seed)+7)
if mode=="comp":
    nc,lab=connected_components(Rel[np.ix_(E,E)],directed=False)
    frs=[E[lab==c] for c in range(nc) if np.sum(lab==c)>=2]
else:
    smax=int(mode[-1]); Cp=C+np.eye(N); CE=Cp[np.ix_(E,E)]; tot=Cp[E,:]@Cp[:,E]; inE=CE@CE
    P,Qm=np.where((C[np.ix_(E,E)]>0)&(tot<=smax)&(tot==inE))
    cand=[np.where((Cp[E[a],:]>0)&(Cp[:,E[b]]>0))[0] for a,b in zip(P,Qm)]
    frs=[]; used=np.zeros(N,bool)
    for i in rr.permutation(len(cand)):
        iv=cand[i]
        if used[iv].any(): continue
        if frs and Rel[np.ix_(iv,np.where(used)[0])].any(): continue
        frs.append(iv); used[iv]=True
out={"N":N,"seed":int(seed),"w":w,"mode":mode,"nf":len(frs),"res":{}}
for Vd in [4.0,64.0]:
    IS=Id(Sd,Vd); rows=sorted((len(f),Id(X[f],Vd)/IS) for f in frs)
    out["res"][Vd]={"IS":IS,"frag":rows}
    sizes=np.array([a for a,_ in rows]); vals=np.array([b for _,b in rows])
    if Vd==64.0:
        print("   fragment: rozm | I/I(d:S) | ile elem. odcinka oddzialywania w przeszlosci fragmentu (max po elementach)")
        dat=[]
        for f in frs:
            npast=max(int(C[ch[:m_+1],x].sum()) for x in f)
            dat.append((Id(X[f],Vd)/IS,len(f),npast))
        for v,sz,npst in sorted(dat,reverse=True):
            print(f"      {sz:3d} el. | {v:.3f}    | {npst:3d} / {m_+1}")
        import numpy as _np
        a=_np.array([d[0] for d in dat]); b=_np.array([d[2] for d in dat])
        print(f"   korelacja I z liczba elementow oddzialywania w przeszlosci: r = {_np.corrcoef(a,b)[0,1]:+.2f}")
    line=[]
    for d in [0.5,0.25,0.1]:
        ok=vals>=1-d
        line.append(f"{int(sizes[ok].min())}" if ok.any() else "brak")
    print(f"{mode:5s} N={N} seed={seed} w={w} Vd={Vd:5.1f} nf={len(frs)} rozm.{sizes.min()}-{sizes.max()} | "
          f"najmniejszy wystarczajacy (d=0.5/0.25/0.1): {'/'.join(line)} el.  | I(d:F)/I(d:S): min {vals.min():.2f} max {vals.max():.2f}")
json.dump(out,open(f"scale_{mode}_{N}_{seed}_{w}.json","w"))
