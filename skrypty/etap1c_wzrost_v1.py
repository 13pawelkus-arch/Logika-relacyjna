"""Regula v1: odczyt natychmiastowy, ale tylko PARTNEROW (siec dekoherencji).
A: partnerzy trwali (losowi na starcie). B: dziedziczeni z przesunieciem (p=0.1: wymiana na partnera partnera).
Kontrola: krag (i-1, i+1, i+2)."""
import numpy as np, sys
from collections import deque
from math import gamma
from scipy.optimize import brentq
def f_MM(d): return gamma(d+1)*gamma(d/2)/(4*gamma(3*d/2))
def d_MM(r):
    try: return brentq(lambda d: f_MM(d)-r, 1.01, 20)
    except ValueError: return np.nan
def grow(N,W,seed,mode,q=0.1):
    rng=np.random.default_rng(seed)
    if mode=="krag": part=[[(i-1)%W,(i+1)%W,(i+2)%W] for i in range(W)]
    else: part=[list(rng.choice([j for j in range(W) if j!=i],3,replace=False)) for i in range(W)]
    C=np.zeros((N,N),bool); tip=list(range(W)); chains=[[i] for i in range(W)]; n=W
    while n<N:
        i=int(rng.integers(W))
        if mode=="B" and rng.random()<q:
            k=int(rng.integers(3)); via=part[i][int(rng.integers(3))]
            opts=[j for j in part[via] if j!=i and j not in part[i]]
            if opts: part[i][k]=int(rng.choice(opts))
        chosen=[tip[i]]+[tip[j] for j in part[i]]
        past=C[:n,chosen].any(axis=1); past[chosen]=True
        C[:n,n]=past; tip[i]=n; chains[i].append(n); n+=1
    return C,part,chains
def graph_dist(part,W):
    adj=[set() for _ in range(W)]
    for i in range(W):
        for j in part[i]: adj[i].add(j); adj[j].add(i)
    D=np.full((W,W),-1)
    for s in range(W):
        D[s,s]=0; dq=deque([s])
        while dq:
            a=dq.popleft()
            for b in adj[a]:
                if D[s,b]<0: D[s,b]=D[s,a]+1; dq.append(b)
    return D
def lag(C,chains,W):
    L=np.full((W,W),np.nan)
    for i in range(W):
        xi=chains[i][-1]
        for j in range(W):
            if i==j: continue
            cj=chains[j]; inpast=[k for k,e in enumerate(cj) if C[e,xi]]
            if inpast: L[i,j]=len(cj)-1-inpast[-1]
    return L
def dim_intervals(C,rng,k=40,minsize=150):
    Cf=C.astype(np.float32); IV=Cf@Cf; P,Q=np.where((IV>=minsize)&C)
    if len(P)==0: return np.nan
    sel=rng.choice(len(P),min(k,len(P)),replace=False); ds=[]
    for s in sel:
        p,q=P[s],Q[s]; I=np.where(C[p]&C[:,q])[0]; n=len(I)
        ds.append(d_MM(C[np.ix_(I,I)].sum()/n**2))
    return np.nanmedian(ds)
N,W=int(sys.argv[1]),int(sys.argv[2])
for mode in ["krag","A","B"]:
    C,part,chains=grow(N,W,1,mode); D=graph_dist(part,W); L=lag(C,chains,W)
    ks=range(1,min(9,int(D.max())+1))
    lagk=[np.nanmean(L[D==k]) for k in ks]
    ball=[np.mean((D<=k)&(D>=0),axis=None)*W for k in ks]
    sl=np.polyfit(list(ks)[:len(lagk)],lagk,1)[0] if len(lagk)>1 else np.nan
    kk=np.array(list(ks)); b=np.array(ball); m=(b<0.5*W)&(kk>=1)
    bd=np.polyfit(np.log(kk[m]),np.log(b[m]),1)[0] if m.sum()>=2 else np.nan
    dm=dim_intervals(C,np.random.default_rng(1))
    print(f"\n== {mode}: srednica sieci {D.max()}, estymator MM z porzadku: {dm:.2f}")
    print("   k | opoznienie (kroki zrodla) | trajektorii w kulce k")
    for k,l,bb in zip(ks,lagk,ball): print(f"  {k:2d} | {l:8.2f}                  | {bb:7.1f}")
    print(f"   nachylenie opoznienia (1/c): {sl:.2f} kroku na krok sieci | wymiar z kulek (log-log, kulki < W/2): {bd:.2f}")
