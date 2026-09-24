"""Czy wiecej partnerow daje wiecej wymiarow? R6 z m wspolnymi sasiadami zamiast jednego."""
import numpy as np
from collections import deque
exec("def mean_dist"+open('r6.py').read().split('def mean_dist')[1].split('for pam in')[0])
def grow(W,seed,m=1,pamiec=True):
    rng=np.random.default_rng(seed)
    adj=[{1,2,3},{0,2,3},{0,1,3},{0,1,2}]; mem={}; owner={}
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
            sel=list(rng.choice(common,min(m,len(common)),replace=False))
            conn+= [int(c) for c in sel]
            c0=int(sel[0]); F=frozenset((u,v,c0)); mm=mem.pop(F,None)
            if mm is not None: owner.pop(mm,None)
            if pamiec and mm is not None and mm not in conn: conn.append(mm)
            setmem(frozenset((u,w,c0)),v); setmem(frozenset((w,v,c0)),u)
        for x in conn: adj[w].add(x); adj[x].add(w); add(w,x)
    return adj
print(" polaczen (u,v + m sasiadow [+ pamiec]) | wymiar z odleglosci | kulki (W=64000) | stopien sr.")
for m,pam in [(1,False),(1,True),(2,False),(2,True),(3,True)]:
    rows=[]
    for W in [4000,16000,64000]:
        rows.append((W,np.mean([mean_dist(grow(W,s,m,pam),10,s) for s in [1,2]])))
    r=np.array(rows); p=np.polyfit(np.log(r[:,0]),np.log(r[:,1]),1)[0]
    a=grow(64000,1,m,pam); bd=ball_dim(a,6,1); st=np.mean([len(z) for z in a])
    opis=f"2 + {m}" + (" + pamiec" if pam else "")
    print(f" {opis:38s} | {1/p:6.2f}              | {bd[0]:.2f} ± {bd[1]:.2f}     | {st:.2f}",flush=True)
