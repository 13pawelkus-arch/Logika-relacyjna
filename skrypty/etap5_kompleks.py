import numpy as np
from collections import deque, defaultdict
def kompleks(W,seed,fifo=True):
    rng=np.random.default_rng(seed); tets=[(0,1,2,3)]; nv=4
    et=defaultdict(set)
    def dodaj(t,i):
        for a in range(4):
            for b in range(a+1,4): et[(min(t[a],t[b]),max(t[a],t[b]))].add(i)
    dodaj(tets[0],0); Q=deque(sorted(et.keys())); zywe={0}
    while nv<W:
        if fifo:
            if not Q: break
            e=Q.popleft()
        else:
            ks=list(et.keys()); e=ks[int(rng.integers(len(ks)))]
        ts=[i for i in et.get(e,()) if i in zywe]
        if not ts: continue
        u,v=e; w=nv; nv+=1
        for i in ts:
            t=tets[i]; poz=[x for x in t if x not in (u,v)]; zywe.discard(i)
            for zam in (u,v):
                nowy=tuple(sorted([zam,w]+poz)); j=len(tets); tets.append(nowy); zywe.add(j); dodaj(nowy,j)
            for a in poz+[u,v]: Q.append((min(a,w),max(a,w)))
        et.pop(e,None)
    adj=[set() for _ in range(nv)]
    for i in zywe:
        t=tets[i]
        for a in range(4):
            for b in range(a+1,4): adj[t[a]].add(t[b]); adj[t[b]].add(t[a])
    return adj
