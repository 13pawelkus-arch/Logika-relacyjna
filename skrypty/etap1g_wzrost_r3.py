"""Regula R3: narodziny trajektorii z dziedziczona lokalnoscia. Parametr b = udzial narodzin w krokach.
Start: 4 trajektorie wzajemnie partnerami. Narodziny: x nad koncem i + koncami partnerow i, zaczyna nowa i';
partnerzy i' = i + 2 partnerow i; i wymienia jednego partnera na i'. Odczyt: x nad koncem i + koncami partnerow."""
import numpy as np, sys
from collections import deque
exec("def dim_intervals"+open('wzrost_v1.py').read().split('def dim_intervals')[1].split('N,W=int')[0])
exec(open('wzrost_v1.py').read().split('def grow(')[0])
def grow_r3(N,b,seed):
    rng=np.random.default_rng(seed)
    C=np.zeros((N,N),bool); tip=[0,1,2,3]; part=[[1,2,3],[0,2,3],[0,1,3],[0,1,2]]; n=4
    while n<N:
        i=int(rng.integers(len(tip)))
        chosen=[tip[i]]+[tip[j] for j in part[i]]
        past=C[:n,chosen].any(axis=1); past[chosen]=True; C[:n,n]=past
        if rng.random()<b:
            new=len(tip); pj=list(rng.choice(part[i],2,replace=False))
            part.append([i]+[int(x) for x in pj]); tip.append(n)
            k=int(rng.integers(3)); part[i][k]=new
        else:
            tip[i]=n
        n+=1
    return C,tip,part
def diam(part):
    W=len(part); adj=[set() for _ in range(W)]
    for i in range(W):
        for j in part[i]: adj[i].add(j); adj[j].add(i)
    mx=0
    for s in range(0,W,max(1,W//40)):
        D={s:0}; dq=deque([s])
        while dq:
            a=dq.popleft()
            for c in adj[a]:
                if c not in D: D[c]=D[a]+1; dq.append(c)
        mx=max(mx,max(D.values()))
    return mx
N=int(sys.argv[1])
print(f"N={N}")
print("   b   |   W  | srednica sieci | log2(W) | pary koncow nieporownywalne | estymator z porzadku")
for b in [0.02,0.1,0.3,0.6]:
    rows=[]
    for s in [1,2]:
        C,tip,part=grow_r3(N,b,s); T=np.array(tip)
        sub=C[np.ix_(T,T)]; W=len(T); unrel=1-(sub|sub.T).sum()/(W*(W-1))
        rows.append((W,diam(part),unrel,dim_intervals(C,np.random.default_rng(s))))
    W=np.mean([r[0] for r in rows]); print(f" {b:5.2f} | {W:4.0f} | {np.mean([r[1] for r in rows]):8.1f}       | {np.log2(W):5.1f}   | {np.mean([r[2] for r in rows]):.3f}                       | {np.nanmean([r[3] for r in rows]):.2f}",flush=True)
