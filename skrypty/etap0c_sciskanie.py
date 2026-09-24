import sys
args=sys.argv[1:]; sys.argv=['x',args[0],args[1]]
src=open('stage0v.py').read().split('print(f"seed=')[0]; exec(src)
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
w=0.08; smax=2
E=np.where((np.abs(t-t[cm])<w)&spc&(~np.isin(np.arange(N),ch)))[0]
Cp=C+np.eye(N); CE=Cp[np.ix_(E,E)]; tot=Cp[E,:]@Cp[:,E]; inE=CE@CE
P,Qm=np.where((C[np.ix_(E,E)]>0)&(tot<=smax)&(tot==inE))
cand=[np.where((Cp[E[a],:]>0)&(Cp[:,E[b]]>0))[0] for a,b in zip(P,Qm)]
o_=rr.permutation(len(cand)); cand=[cand[i] for i in o_]; frs=[]; used=np.zeros(N,bool)
for iv in cand:
    if used[iv].any(): continue
    if frs and Rel[np.ix_(iv,np.where(used)[0])].any(): continue
    frs.append(iv); used[iv]=True
nf=len(frs); U=np.concatenate(frs)
perms=[rr.permutation(nf) for _ in range(8)]
print(f"N={N} fragmentow={nf} |U|={len(U)}")
print("   s    | S(S)   | I(S:U)/S | krzywa I/S przy k/nf = 0.1 0.25 0.5 0.75 1   | R_0.1 R_0.5 | R'_0.1 R'_0.5 | II/S(b)")
curves={}
for s in [1/8,1/4,1/2,1,2,4,8,16]:
    G=np.eye(n)*0.5; G[r,r]=s**2/(2*om); G[r+1,r+1]=om/(2*s**2)
    sS=Sred(Sd,G)
    def I(idx):
        R=X[np.sort(idx)]; return sS+Sred(R,G)-Sred(np.vstack([Sd,R]),G)
    cur=np.zeros(nf)
    for o in perms:
        for k in range(1,nf+1):
            cur[k-1]+=I(np.concatenate([frs[i] for i in o[:k]]))/len(perms)
    IU=cur[-1]; fr=np.arange(1,nf+1)/nf
    def R(thr):
        ok=np.where(cur>=thr)[0]
        return (1/fr[ok[0]]) if len(ok) else 0.0
    ii=[]
    for o in perms:
        h=nf//2; G1=np.concatenate([frs[i] for i in o[:h]]); G2=np.concatenate([frs[i] for i in o[h:]])
        ii.append((I(np.concatenate([G1,G2]))-I(G1)-I(G2))/sS)
    pick=[cur[max(0,int(round(q*nf))-1)]/sS for q in [0.1,0.25,0.5,0.75,1.0]]
    curves[s]=cur/sS
    print(f" {s:6.3f} | {sS:.4f} | {IU/sS:6.3f}   | "+" ".join(f"{x:5.3f}" for x in pick)
          +f" | {R(0.9*sS):5.2f} {R(0.5*sS):5.2f} | {R(0.9*IU):5.2f}  {R(0.5*IU):5.2f}  | {np.mean(ii):+.3f}")
np.save(f"curves_{N}.npy",{k:v for k,v in curves.items()},allow_pickle=True)
