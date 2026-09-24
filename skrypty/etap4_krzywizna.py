"""Krzywizna Olliviera-Ricciego: kappa(x,y) = 1 - W1(mx,my)/d(x,y), miary jednostajne na sasiadach."""
import numpy as np
from collections import deque
from scipy.optimize import linprog
from r6grow import grow
def bfs_dist(adj,s,maxd=4):
    D={s:0}; dq=deque([s])
    while dq:
        a=dq.popleft()
        if D[a]>=maxd: continue
        for c in adj[a]:
            if c not in D: D[c]=D[a]+1; dq.append(c)
    return D
def ollivier(adj,edges):
    out=[]
    for x,y in edges:
        A=sorted(adj[x]); B=sorted(adj[y])
        if not A or not B: continue
        Dx={a:bfs_dist(adj,a) for a in A}
        C=np.array([[Dx[a].get(b,8) for b in B] for a in A],float)
        na,nb=len(A),len(B)
        Aeq=np.zeros((na+nb,na*nb)); beq=np.concatenate([np.ones(na)/na,np.ones(nb)/nb])
        for i in range(na): Aeq[i,i*nb:(i+1)*nb]=1
        for j in range(nb): Aeq[na+j,j::nb]=1
        r=linprog(C.ravel(),A_eq=Aeq,b_eq=beq,bounds=(0,None),method="highs")
        if r.success: out.append(1-r.fun)
    return np.array(out)
def siatka3d(n):
    idx=lambda a,b,c:(a*n+b)*n+c; adj=[set() for _ in range(n**3)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for da,db,dc in [(1,0,0),(0,1,0),(0,0,1)]:
                    a2,b2,c2=(a+da)%n,(b+db)%n,(c+dc)%n
                    adj[idx(a,b,c)].add(idx(a2,b2,c2)); adj[idx(a2,b2,c2)].add(idx(a,b,c))
    return adj
def drzewo(n):
    adj=[set() for _ in range(n)]
    for i in range(1,n):
        p=(i-1)//2; adj[i].add(p); adj[p].add(i)
    return adj
rng=np.random.default_rng(1)
for nazwa,adj in [("R6 (triada + pamiec, 3D)",grow(16000,1,True)),
                  ("R5 (triada, 2D)",grow(16000,1,False)),
                  ("siatka 3D (kontrola plaska)",siatka3d(16)),
                  ("drzewo (kontrola ujemna)",drzewo(16000))]:
    xs=rng.choice(len(adj),250,replace=False)
    E=[(int(x),int(sorted(adj[x])[0])) for x in xs if adj[x]]
    k=ollivier(adj,E[:150])
    print(f" {nazwa:34s}: krzywizna {k.mean():+.3f} ± {k.std()/np.sqrt(max(len(k),1)):.3f}  (n={len(k)})",flush=True)
