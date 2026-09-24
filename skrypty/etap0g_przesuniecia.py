"""(a) Zespol przesuniec: klasyczna zmienna d (wariancja Vd) przesuwa detektor w q.
I(d:F) = S(Gamma_F + Vd m m^T) - S(Gamma_F), m = odpowiedz obserwabli na d."""
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
def S(R,G):
    Jr=R@J@R.T; W=R@G@R.T+0.5j*Jr
    mu,Vv=np.linalg.eigh(1j*Jr); mx=np.abs(mu).max()
    if mx==0: return 0.0
    k=np.abs(mu)>1e-10*mx; Vv=Vv[:,k]
    sig=np.linalg.eigvals((Vv.conj().T@W@Vv)/mu[k][:,None]).real
    sig=sig[(np.abs(sig)>1e-10)&(np.abs(sig-1)>1e-10)]
    return float(np.sum(sig*np.log(np.abs(sig))))
def Id(R,Vd):                      # informacja o klasycznym przesunieciu
    mm=R[:,r]                      # odpowiedz na d (kolumna q0)
    return S(R,Gin+Vd*np.outer(np.eye(n)[r],np.eye(n)[r]))-S(R,Gin)
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
nf=len(frs); U=np.concatenate(frs); perms=[rr.permutation(nf) for _ in range(6)]
print(f"N={N} seed={seed} nf={nf} |U|={len(U)}  (kontrola g=0 i Vd=0 ponizej)")
# kontrola g=0
V0=np.zeros_like(V); X0=np.linalg.solve(np.eye(N+K)-G0@V0,B)
print(f"  g=0:  I(d:U)={Id(X0[U],4.0):.2e}   |  Vd=0: I(d:U)={Id(X[U],0.0):.2e}  I(d:S)={Id(Sd,0.0):.2e}")
out={"N":N,"seed":int(seed),"nf":nf,"sizes":[len(f) for f in frs],"curves":{}}
print("   Vd  | I(d:S)  I(d:U)  | krzywa I(d:F)/I(d:U) przy 10/25/50/75/100% fragmentow")
for Vd in [0.25,1.0,4.0,16.0,64.0,256.0]:
    IS=Id(Sd,Vd); cur=np.zeros(nf)
    for o in perms:
        acc=[]
        for k in range(nf):
            acc.append(frs[o[k]]); cur[k]+=Id(X[np.sort(np.concatenate(acc))],Vd)/len(perms)
    IU=cur[-1]; out["curves"][Vd]=(cur/IU).tolist()
    pk=[cur[max(0,int(np.ceil(q*nf))-1)]/IU for q in [0.1,0.25,0.5,0.75,1.0]]
    print(f" {Vd:6.2f} | {IS:6.3f}  {IU:6.3f}  | "+" ".join(f"{x:.3f}" for x in pk))
json.dump(out,open(f"disp_{mode}_{N}_{seed}.json","w"))
