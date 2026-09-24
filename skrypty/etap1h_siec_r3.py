"""Sama siec partnerow z R3 (nie zalezy od porzadku ani od b): narodziny z dziedziczona lokalnoscia."""
import numpy as np
from collections import deque
def grow_graph(W,seed):
    rng=np.random.default_rng(seed)
    part=[[1,2,3],[0,2,3],[0,1,3],[0,1,2]]
    while len(part)<W:
        i=int(rng.integers(len(part))); new=len(part)
        pj=rng.choice(part[i],2,replace=False)
        part.append([i,int(pj[0]),int(pj[1])])
        part[i][int(rng.integers(3))]=new
    adj=[set() for _ in range(W)]
    for i in range(W):
        for j in part[i]: adj[i].add(j); adj[j].add(i)
    return adj
def ecc_sample(adj,k,rng):
    W=len(adj); out=[]
    for s in rng.choice(W,k,replace=False):
        D=np.full(W,-1); D[s]=0; dq=deque([s])
        while dq:
            a=dq.popleft()
            for c in adj[a]:
                if D[c]<0: D[c]=D[a]+1; dq.append(c)
        out.append((D.max(),D.mean()))
    return np.array(out)
print("     W   | srednica (max z probki) | srednia odleglosc | przyrost sredniej na podwojenie")
prev=None; rows=[]
for W in [1000,4000,16000,64000,256000]:
    r=[]
    for s in [1,2]:
        e=ecc_sample(grow_graph(W,s),20,np.random.default_rng(s)); r.append(e)
    r=np.vstack(r); dmax=r[:,0].max(); dmean=r[:,1].mean()
    inc="" if prev is None else f"{(dmean-prev)/2:+.2f}"
    print(f" {W:7d} | {dmax:6.0f}                  | {dmean:7.2f}           | {inc}",flush=True)
    prev=dmean; rows.append((W,dmean))
r=np.array(rows)
p=np.polyfit(np.log(r[:,0]),np.log(r[:,1]),1); q=np.polyfit(np.log(r[:,0]),r[:,1],1)
rp=np.std(np.log(r[:,1])-np.polyval(p,np.log(r[:,0]))); rq=np.std(r[:,1]-np.polyval(q,np.log(r[:,0])))/r[:,1].mean()
print(f"\nsrednia odleglosc ~ W^{p[0]:.3f} (rozrzut {rp:.3f})   |   ~ {q[0]:.2f}*ln W (rozrzut {rq:.3f})")
