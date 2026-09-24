import numpy as np
from collections import deque
exec(open('r5.py').read().split('def grow_r5')[0])
exec("def stats"+open('r5.py').read().split('def stats')[1].split('print(')[0])
def grow(W,seed,mode,k=8):
    rng=np.random.default_rng(seed)
    adj=[{1,2,3},{0,2,3},{0,1,3},{0,1,2}]
    edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]; eidx={e:i for i,e in enumerate(edges)}
    def add(a,b):
        e=(a,b) if a<b else (b,a); eidx[e]=len(edges); edges.append(e)
    def rem(a,b):
        e=(a,b) if a<b else (b,a); i=eidx.pop(e); last=edges.pop()
        if i<len(edges): edges[i]=last; eidx[last]=i
    while len(adj)<W:
        if mode=="wyrownanie":
            cand=[edges[int(x)] for x in rng.integers(len(edges),size=k)]
            u,v=min(cand,key=lambda e: len(adj[e[0]])+len(adj[e[1]]))
        else:
            u,v=edges[int(rng.integers(len(edges)))]
        common=list(adj[u]&adj[v]); w=len(adj); adj.append(set())
        adj[u].discard(v); adj[v].discard(u); rem(u,v)
        if mode=="triada":
            conn=[u,v]+([common[int(rng.integers(len(common)))]] if common else [])
        else:
            conn=[u,v]+common
        for x in conn: adj[w].add(x); adj[x].add(w); add(w,x)
    return adj
for mode in ["wyrownanie","triada"]:
    print(f"\n== {mode}")
    print("     W  | srednia odleglosc | przyrost/podwojenie | stopien sr. | max")
    rows=[];prev=None
    for W in [1000,4000,16000,64000]:
        r=np.array([stats(grow(W,s,mode),16,s) for s in [1,2]]).mean(axis=0)
        inc="" if prev is None else f"{(r[0]-prev)/2:+.2f}"
        print(f" {W:6d} | {r[0]:8.2f}          | {inc:7s}             | {r[1]:6.2f}      | {r[2]:4.0f}",flush=True)
        prev=r[0]; rows.append((W,r[0]))
    r=np.array(rows); p=np.polyfit(np.log(r[:,0]),np.log(r[:,1]),1)[0]
    print(f"   wykladnik: {p:.3f}   (cel 1/3)")
