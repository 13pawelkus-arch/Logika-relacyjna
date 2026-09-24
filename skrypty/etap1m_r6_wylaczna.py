"""R6 z pamiecia wylaczna: kazdy punkt jest pamiecia co najwyzej jednej sciany naraz; przejmuje najswiezsza.
Wybor miejsca identyczny z R5 (losowa krawedz, losowy wspolny sasiad)."""
import numpy as np
from collections import deque
exec("def mean_dist"+open('r6.py').read().split('def mean_dist')[1].split('for pam in')[0])
def grow(W,seed,pamiec=True):
    rng=np.random.default_rng(seed)
    adj=[{1,2,3},{0,2,3},{0,1,3},{0,1,2}]
    mem={}; owner={}
    def setmem(F,x):
        old=owner.get(x)
        if old is not None and old!=F: mem.pop(old,None)
        if F in mem: owner.pop(mem[F],None)
        mem[F]=x; owner[x]=F
    for F,x in [((0,1,2),3),((0,1,3),2),((0,2,3),1),((1,2,3),0)]: setmem(frozenset(F),x)
    edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]; eidx={e:k for k,e in enumerate(edges)}
    def add(a,b):
        e=(a,b) if a<b else (b,a); eidx[e]=len(edges); edges.append(e)
    def rem(a,b):
        e=(a,b) if a<b else (b,a); k=eidx.pop(e); last=edges.pop()
        if k<len(edges): edges[k]=last; eidx[last]=k
    while len(adj)<W:
        u,v=edges[int(rng.integers(len(edges)))]
        common=list(adj[u]&adj[v]); w=len(adj); adj.append(set())
        adj[u].discard(v); adj[v].discard(u); rem(u,v)
        conn=[u,v]
        if common:
            c=common[int(rng.integers(len(common)))]; conn.append(c)
            F=frozenset((u,v,c)); m=mem.pop(F,None)
            if m is not None: owner.pop(m,None)
            if pamiec and m is not None and m not in (u,v,c): conn.append(m)
            setmem(frozenset((u,w,c)),v); setmem(frozenset((w,v,c)),u)
        for x in conn: adj[w].add(x); adj[x].add(w); add(w,x)
    return adj
for pam in [False,True]:
    print(f"\n== {'Z PAMIECIA (wylaczna, najswiezsza)' if pam else 'BEZ PAMIECI (kontrola = R5)'}")
    rows=[];mx=[]
    for W in [1000,4000,16000,64000]:
        adjs=[grow(W,s,pam) for s in [1,2]]
        md=np.mean([mean_dist(a,12,s) for s,a in zip([1,2],adjs)])
        deg=np.concatenate([[len(x) for x in a] for a in adjs]); mx.append(deg.max())
        rows.append((W,md)); print(f"  W={W:6d}: srednia odleglosc {md:7.2f} | stopien sr. {deg.mean():.2f}, max {deg.max()}",flush=True)
    r=np.array(rows); p=np.polyfit(np.log(r[:,0]),np.log(r[:,1]),1)[0]
    pm=np.polyfit(np.log(r[:,0]),np.log(mx),1)[0]
    bd=[ball_dim(grow(64000,s,pam),6,s) for s in [1,2]]
    print(f"  wykladnik odleglosci {p:.3f} -> wymiar {1/p:.2f} | kulki (W=64000): {np.mean([b[0] for b in bd]):.2f} ± {np.mean([b[1] for b in bd]):.2f} | stopien max ~ W^{pm:.2f}")
