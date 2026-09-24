import sys
from scipy.sparse.csgraph import connected_components
args=sys.argv[1:]; sys.argv=['x',args[0],args[1]]
src=open('stage0v.py').read().split('print(f"seed=')[0].replace('om=2*np.pi*3/np.sqrt(2)','om=0.5'); exec(src)
t=(u+v)/np.sqrt(2); m=int(np.argmin(np.abs(t[ch]-np.sqrt(2)/2)))
g=5.0; lam=g*eps
V=np.zeros((N+K,N+K)); kk=np.arange(m+1); V[ch[kk],N+kk]=lam; V[N+kk,ch[kk]]=lam
X=np.linalg.inv(np.eye(N+K)-G0@V)@B
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
rr=np.random.default_rng(int(args[0])+7)
print(f"N={N} m={m} omega=0.5")
for w in [float(x) for x in args[2].split(',')]:
    E=np.where((np.abs(t-t[cm])<w)&spc&(~np.isin(np.arange(N),ch)))[0]
    nc,lab=connected_components(Rel[np.ix_(E,E)],directed=False)
    frs=[E[lab==c] for c in range(nc) if np.sum(lab==c)>=2]
    nf=len(frs); U=np.concatenate(frs); sz=sorted(len(f) for f in frs)
    cF=max(np.abs(X[a]@J@X[b].T).max() for i,a in enumerate(frs) for b in frs[i+1:])
    cS=np.abs(Sd@J@X[U].T).max()
    print(f"-- w={w}: |E|={len(E)}  fragmentow={nf}  pokrycie={len(U)/len(E):.2f}  rozmiary: med {np.median(sz):.0f}, max {sz[-1]}  | max[Fi,Fj]={cF:.0e} max[S,F]={cS:.0e}")
    allc={}
    print("     s  | S(S)   | I(S:U)/S AL | I/S przy 5% 10% 25% 50% 100%   | R_0.5  R_0.25 | II/S")
    perms=[rr.permutation(nf) for _ in range(6)]
    for s in [1,2,4,8,16,32]:
        G=np.eye(n)*0.5; G[r,r]=s**2/(2*om); G[r+1,r+1]=om/(2*s**2)
        sS=Sred(Sd,G)
        def I(idx):
            R=X[np.sort(idx)]; return sS+Sred(R,G)-Sred(np.vstack([Sd,R]),G)
        cur=np.zeros(nf)
        for o in perms:
            acc=[]
            for k in range(1,nf+1):
                acc.append(frs[o[k-1]]); cur[k-1]+=I(np.concatenate(acc))/len(perms)
        IU=cur[-1]; AL=IU<=2*min(sS,Sred(X[U],G))+1e-9; fr=np.arange(1,nf+1)/nf
        def R(th):
            ok=np.where(cur>=th*sS)[0]; return 1/fr[ok[0]] if len(ok) else 0
        ii=[]
        for o in perms:
            h=nf//2; G1=np.concatenate([frs[i] for i in o[:h]]); G2=np.concatenate([frs[i] for i in o[h:]])
            ii.append((I(np.concatenate([G1,G2]))-I(G1)-I(G2))/sS)
        allc[s]=(cur/sS).tolist()
        pk=[cur[max(0,int(np.ceil(q*nf))-1)]/sS for q in [0.05,0.1,0.25,0.5,1.0]]
        print(f"  {s:4d}  | {sS:.3f}  | {IU/sS:.3f}  {'ok' if AL else 'NIE'} | "+" ".join(f"{x:.3f}" for x in pk)+f" | {R(0.5):5.1f}  {R(0.75):5.1f} | {np.mean(ii):+.3f}")

    import json; json.dump({"N":N,"seed":int(args[0]),"w":w,"nf":nf,"curves":allc},open(f"real_{N}_{args[0]}_{w}.json","w"))
