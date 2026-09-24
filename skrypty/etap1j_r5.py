"""R5: narodziny = podzial losowej relacji (u,v): nowy w polaczony z u, v i wszystkimi wspolnymi sasiadami u,v.
Start: czworoscian (K4). Pomiar: srednia odleglosc vs W, stopien maksymalny."""
import numpy as np, sys
from collections import deque
def grow_r5(W,seed):
    rng=np.random.default_rng(seed)
    adj=[{1,2,3},{0,2,3},{0,1,3},{0,1,2}]
    edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]; eidx={e:k for k,e in enumerate(edges)}
    def add(a,b):
        e=(a,b) if a<b else (b,a); eidx[e]=len(edges); edges.append(e)
    def rem(a,b):
        e=(a,b) if a<b else (b,a); k=eidx.pop(e); last=edges.pop()
        if k<len(edges): edges[k]=last; eidx[last]=k
    while len(adj)<W:
        u,v=edges[int(rng.integers(len(edges)))]
        common=adj[u]&adj[v]; w=len(adj); adj.append(set())
        adj[u].discard(v); adj[v].discard(u); rem(u,v)
        for x in [u,v]+list(common):
            adj[w].add(x); adj[x].add(w); add(w,x)
    return adj
def stats(adj,k,seed):
    W=len(adj); rng=np.random.default_rng(seed); md=[]
    for s in rng.choice(W,k,replace=False):
        D=np.full(W,-1); D[s]=0; dq=deque([s])
        while dq:
            a=dq.popleft()
            for c in adj[a]:
                if D[c]<0: D[c]=D[a]+1; dq.append(c)
        md.append(D.mean())
    deg=np.array([len(a) for a in adj])
    return np.mean(md),deg.mean(),deg.max(),np.percentile(deg,99)
print("     W  | srednia odleglosc | przyrost/podwojenie | stopien sr. | max | 99%")
rows=[];prev=None
for W in [1000,4000,16000,64000,256000]:
    r=np.array([stats(grow_r5(W,s),16,s) for s in [1,2]]).mean(axis=0)
    inc="" if prev is None else f"{(r[0]-prev)/2:+.2f}"
    print(f" {W:6d} | {r[0]:8.2f}          | {inc:7s}             | {r[1]:6.2f}      | {r[2]:4.0f} | {r[3]:.0f}",flush=True)
    prev=r[0]; rows.append((W,r[0]))
r=np.array(rows); p=np.polyfit(np.log(r[:,0]),np.log(r[:,1]),1)
q=np.polyfit(np.log(r[:,0]),r[:,1],1)
rp=np.std(np.log(r[:,1])-np.polyval(p,np.log(r[:,0]))); rq=np.std(r[:,1]-np.polyval(q,np.log(r[:,0])))/r[:,1].mean()
print(f"\nsrednia odleglosc ~ W^{p[0]:.3f} (rozrzut {rp:.3f})   |   ~ {q[0]:.2f}*ln W (rozrzut {rq:.3f})   | cel: 1/3 = 0.333")
