"""Regula R2: partnerzy wybierani przez odleglosc z porzadku (nakladanie przyczynowe wzgledem calej przeszlosci).
Stala liczba trajektorii W, bez narodzin. Start: korzen + W nieporownywalnych.
Kontrole: bez pamieci, bez dynamiki (po kolei), losowi partnerzy."""
import numpy as np, sys
from collections import deque
exec(open('wzrost_v1.py').read().split('def grow(')[0])          # d_MM, importy
exec("def dim_intervals"+open('wzrost_v1.py').read().split('def dim_intervals')[1].split('N,W=int')[0])
def grow_r2(N,W,seed,mode):
    rng=np.random.default_rng(seed)
    C=np.zeros((N,N),bool); C[0,1:W+1]=True                      # korzen 0 pod wszystkimi
    tip=list(range(1,W+1)); chains=[[t] for t in tip]; n=W+1; log=[]; step=0
    while n<N:
        i=step%W if mode=="bez_dynamiki" else int(rng.integers(W))
        ti=tip[i]; Pi=C[:n,ti].copy(); Pi[ti]=True
        cand=[j for j in range(W) if j!=i and not Pi[tip[j]]]
        if len(cand)<3: step+=1; continue
        if mode=="losowi":
            part=list(rng.choice(cand,3,replace=False))
        else:
            T=np.array([tip[j] for j in cand]); PT=C[:n,T].copy(); PT[T,np.arange(len(T))]=True
            inter=(PT & Pi[:,None]).sum(0); a_only=Pi.sum()-inter; b_only=PT.sum(0)-inter
            O=inter/(np.minimum(a_only,b_only)+inter+1e-9)
            O=O+1e-9*rng.random(len(O))                               # remisy losowo
            part=[cand[k] for k in np.argsort(-O)[:3]]
        chosen=[tip[j] for j in part]
        if mode!="bez_pamieci": chosen=chosen+[ti]
        past=C[:n,chosen].any(axis=1); past[chosen]=True
        C[:n,n]=past; tip[i]=n; chains[i].append(n); log.append((i,part)); n+=1; step+=1
    return C,chains,log
def reading_graph(log,W,window):
    adj=[set() for _ in range(W)]
    for i,part in log[-window:]:
        for j in part: adj[i].add(j); adj[j].add(i)
    return adj
def dists(adj,W):
    D=np.full((W,W),-1)
    for s in range(W):
        D[s,s]=0; dq=deque([s])
        while dq:
            a=dq.popleft()
            for b in adj[a]:
                if D[s,b]<0: D[s,b]=D[s,a]+1; dq.append(b)
    return D
def lagmat(C,chains,W):
    L=np.full((W,W),np.nan)
    for i in range(W):
        xi=chains[i][-1]
        for j in range(W):
            if i==j: continue
            ks=[k for k,e in enumerate(chains[j]) if C[e,xi]]
            if ks: L[i,j]=len(chains[j])-1-ks[-1]
    return L
N,W=int(sys.argv[1]),int(sys.argv[2])
for mode in ["odleglosc","bez_pamieci","bez_dynamiki","losowi"]:
    C,chains,log=grow_r2(N,W,1,mode)
    adj=reading_graph(log,W,window=len(log)//2); D=dists(adj,W)
    comp=len(set(tuple(np.where(D[s]>=0)[0]) for s in range(W)))
    reach=D[D>0]; diam=int(reach.max()) if reach.size else 0
    ks=list(range(1,min(8,diam)+1)); ball=[np.mean(np.sum((D<=k)&(D>=0),axis=1)) for k in ks]
    L=lagmat(C,chains,W); lagk=[np.nanmean(L[D==k]) for k in ks]
    kk=np.array(ks); b=np.array(ball); m=b<0.5*W
    bd=np.polyfit(np.log(kk[m]),np.log(b[m]),1)[0] if m.sum()>=2 else np.nan
    sl=np.polyfit(kk,lagk,1)[0] if len(ks)>1 else np.nan
    dm=dim_intervals(C,np.random.default_rng(1))
    deg=np.mean([len(a) for a in adj])
    print(f"\n== {mode}: skladowe {comp}, srednica {diam}, sredni stopien {deg:.1f}, estymator z porzadku {dm:.2f}")
    print("   k | kulka | opoznienie")
    for k,bb,l in zip(ks,ball,lagk): print(f"  {k:2d} | {bb:6.1f} | {l:6.2f}")
    print(f"   wymiar z kulek (kulki < W/2): {bd:.2f}   nachylenie opoznienia: {sl:.2f}",flush=True)
