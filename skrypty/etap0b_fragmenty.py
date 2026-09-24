import sys
args=sys.argv[1:]; sys.argv=['x',args[0],args[1]]
src=open('stage0v.py').read().split('print(f"seed=')[0]; exec(src)
t=(u+v)/np.sqrt(2); m=int(np.argmin(np.abs(t[ch]-np.sqrt(2)/2)))
g=5.0; lam=g*eps
V=np.zeros((N+K,N+K)); kk=np.arange(m+1); V[ch[kk],N+kk]=lam; V[N+kk,ch[kk]]=lam
X=np.linalg.inv(np.eye(N+K)-G0@V)@B
Sd=X[[N+m,N+m-1]]; cm,cm1=ch[m],ch[m-1]
Rel=C+C.T
def Sred(R,rel=1e-10):
    if len(R)==0: return 0.0
    Jr=R@J@R.T; W=R@Gin@R.T+0.5j*Jr
    mu,Vv=np.linalg.eigh(1j*Jr); mx=np.abs(mu).max()
    if mx==0: return 0.0
    k=np.abs(mu)>rel*mx; Vv=Vv[:,k]
    sig=np.linalg.eigvals((Vv.conj().T@W@Vv)/mu[k][:,None]).real
    sig=sig[(np.abs(sig)>1e-10)&(np.abs(sig-1)>1e-10)]
    return float(np.sum(sig*np.log(np.abs(sig))))
sS=Sred(Sd)
def I(idx): 
    idx=np.array(sorted(idx),int); R=X[idx]
    return sS+Sred(R)-Sred(np.vstack([Sd,R]))
spc=(C[:,cm]==0)&(C[cm,:]==0)&(C[:,cm1]==0)&(C[cm1,:]==0)
rr=np.random.default_rng(int(args[0])+7)
print(f"N={N} m={m}/{M} S(S)={sS:.4f}")
print("  w   smax nfr |U| | max[S,F] max[Fi,Fj](b) | I(S:U)/S AL | krzywa I(S:F)/S(S) przy 10/25/50/75/100% fragm. | II/S (b)      II/S (a)      (a)-(b) | monot.")
for smax in [2,4]:
  for w in [0.02,0.04,0.08,0.15,0.3]:
    E=np.where((np.abs(t-t[cm])<w)&spc&(~np.isin(np.arange(N),ch)))[0]; Es=set(E)
    Cp=C+np.eye(N); CE=Cp[np.ix_(E,E)]
    tot=Cp[E,:]@Cp[:,E]; inE=CE@CE
    P,Qm=np.where((C[np.ix_(E,E)]>0)&(tot<=smax)&(tot==inE))
    cand=[np.where((Cp[E[a],:]>0)&(Cp[:,E[b]]>0))[0] for a,b in zip(P,Qm)]
    o_=rr.permutation(len(cand)); cand=[cand[i] for i in o_]; frs=[]; used=np.zeros(N,bool)
    for iv in cand:
        iv=np.array(iv)
        if used[iv].any(): continue
        if frs and Rel[np.ix_(iv,np.where(used)[0])].any(): continue
        frs.append(iv); used[iv]=True
    nf=len(frs)
    if nf<4: print(f" {w:4.2f} {smax}   {nf:3d}  za malo fragmentow"); continue
    U=np.concatenate(frs); sizes=[len(f) for f in frs]
    cS=np.abs(Sd@J@X[U].T).max()
    cF=max(np.abs(X[a]@J@X[b].T).max() for i,a in enumerate(frs) for b in frs[i+1:])
    IU=I(U); AL=IU<=2*min(sS,Sred(X[U]))+1e-9
    curve=[]; mono=0
    for fr in [0.1,0.25,0.5,0.75,1.0]:
        vals=[]
        for d in range(8):
            o=rr.permutation(nf); k=max(1,int(round(fr*nf)))
            A=np.concatenate([frs[i] for i in o[:k]]); vals.append(I(A))
            if k<nf:
                A2=np.concatenate([frs[i] for i in o[:k+1]])
                if I(A2)<vals[-1]-1e-9: mono+=1
        curve.append(np.mean(vals)/sS)
    def II(parts):
        out=[]
        for d in range(8):
            o=rr.permutation(len(parts)); h=len(parts)//2
            G1=np.concatenate([parts[i] for i in o[:h]]); G2=np.concatenate([parts[i] for i in o[h:]])
            out.append((I(np.concatenate([G1,G2]))-I(G1)-I(G2))/sS)
        return np.mean(out),np.std(out)
    IIb=II(frs)
    perm=rr.permutation(U); pa=[]; s0=0
    for s in sizes: pa.append(perm[s0:s0+s]); s0+=s
    IIa=II(pa)
    print(f" {w:4.2f} {smax}   {nf:3d} {len(U):3d} | {cS:.0e}   {cF:.0e}      | {IU/sS:5.3f}   {'ok' if AL else 'NIE'} | "
          + " ".join(f"{c:5.3f}" for c in curve)
          + f" | {IIb[0]:+.3f}±{IIb[1]:.3f} {IIa[0]:+.3f}±{IIa[1]:.3f} {IIa[0]-IIb[0]:+.3f} | {mono}")
