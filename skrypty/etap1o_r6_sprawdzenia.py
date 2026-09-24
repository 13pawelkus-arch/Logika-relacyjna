"""Sprawdzenia R6: start (czworoscian / plaski dysk bez pamieci), regula przejmowania (najswiezsza / pierwsza)."""
import numpy as np, sys
from collections import deque
exec("def mean_dist"+open('r6.py').read().split('def mean_dist')[1].split('for pam in')[0])
def start_plaski(R=6):
    # plaski triangulowany dysk: siatka trojkatna (heksagonalna) promienia R
    pts={}; 
    for a in range(-R,R+1):
        for b in range(-R,R+1):
            if abs(a)+abs(b)+abs(-a-b)<=2*R: pts[(a,b)]=len(pts)
    adj=[set() for _ in pts]
    for (a,b),i in pts.items():
        for da,db in [(1,0),(0,1),(-1,1)]:
            j=pts.get((a+da,b+db))
            if j is not None: adj[i].add(j); adj[j].add(i)
    return adj
def grow(W,seed,pamiec=True,start="czworoscian",przejmuje="najswiezsza"):
    rng=np.random.default_rng(seed)
    mem={}; owner={}
    def setmem(F,x):
        old=owner.get(x)
        if old is not None and old!=F:
            if przejmuje=="najswiezsza": mem.pop(old,None)
            else: return                                  # pierwsza zatrzymuje
        if F in mem: owner.pop(mem[F],None)
        mem[F]=x; owner[x]=F
    if start=="czworoscian":
        adj=[{1,2,3},{0,2,3},{0,1,3},{0,1,2}]
        for F,x in [((0,1,2),3),((0,1,3),2),((0,2,3),1),((1,2,3),0)]: setmem(frozenset(F),x)
    else:
        adj=start_plaski()
    edges=[]; eidx={}
    for a in range(len(adj)):
        for b in adj[a]:
            if a<b: eidx[(a,b)]=len(edges); edges.append((a,b))
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
def badaj(nazwa,Ws,seeds,**kw):
    rows=[]
    for W in Ws:
        md=np.mean([mean_dist(grow(W,s,**kw),10,s) for s in seeds]); rows.append((W,md))
    r=np.array(rows); p=np.polyfit(np.log(r[:,0]),np.log(r[:,1]),1)[0]
    bd=[ball_dim(grow(Ws[-1],s,**kw),6,s) for s in seeds]
    print(f" {nazwa:44s} | " + " ".join(f"{m:6.2f}" for _,m in rows) + f" | wymiar z odl. {1/p:.2f} | kulki {np.mean([b[0] for b in bd]):.2f} ± {np.mean([b[1] for b in bd]):.2f}",flush=True)
mode=sys.argv[1]
if mode=="start_i_przejmowanie":
    Ws=[1000,4000,16000,64000]; print(" wariant                                      | sr. odleglosc przy W=1e3,4e3,1.6e4,6.4e4")
    badaj("plaski start, bez pamieci",Ws,[1,2],pamiec=False,start="plaski")
    badaj("plaski start, z pamiecia (najswiezsza)",Ws,[1,2],pamiec=True,start="plaski")
    badaj("czworoscian, z pamiecia, PIERWSZA zatrzymuje",Ws,[1,2],pamiec=True,przejmuje="pierwsza")
