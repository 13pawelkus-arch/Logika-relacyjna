"""H2: liczniki typow I i II wobec N (1+1, 2 ziarna) + P(motyl) = 1/24 z permutacji."""
import numpy as np, sys, itertools, collections, time
from collections import defaultdict
# P(motyl) z permutacji: 4 punkty posortowane po u, porzadek i<j & pi(i)<pi(j)
def rel(pi): return {(i,j) for i in range(4) for j in range(4) if i<j and pi[i]<pi[j]}
mot={(0,2),(0,3),(1,2),(1,3)}
print("P(motyl) =", sum(rel(p)==mot for p in itertools.permutations(range(4))),"/ 24")
def licz(N,seed):
    rng=np.random.default_rng(seed); u,v=rng.random(N),rng.random(N)
    C=((u[:,None]<u[None,:])&(v[:,None]<v[None,:])); Cf=C.astype(np.float32)
    IV=Cf@Cf; L=C&(IV<0.5); C3=IV@Cf
    FP,FQ=np.where((IV==2)&C&(C3==0))
    G=defaultdict(list)
    for p,q in zip(FP,FQ):
        a,b=np.where(C[p]&C[:,q])[0]; G[(a,b)].append((p,q))
    sb=0
    for E in G.values():
        par={}
        def f(x):
            while par.setdefault(x,x)!=x: x=par[x]
            return x
        for p,q in E: par[f((0,p))]=f((1,q))
        P={e[0] for e in E}; Q={e[1] for e in E}
        sb+=len(E)-len(P)-len(Q)+len({f((0,p)) for p in P})
    # typ II: przedzialy z 4 elementami w ukladzie motyla
    XP,XQ=np.where(C&(IV==4)); n2=0
    for x,y in zip(XP,XQ):
        m=np.where(C[x]&C[:,y])[0]; S=C[np.ix_(m,m)]
        if S.sum()==4 and (S.sum(0)==2).sum()==2 and (S.sum(1)==2).sum()==2: n2+=1
    return len(FP), sb, n2
print("   N   | F/N    | sum_b1(I)/N | #II/N  | (I+II)/F | 1-(I+II)/F")
for N in [1000,2000,4000,8000]:
    r=np.array([licz(N,s) for s in (1,2)],float).mean(0)
    print(f"{N:6d} | {r[0]/N:.4f} | {r[1]/N:.4f}      | {r[2]/N:.4f} | {(r[1]+r[2])/r[0]:.4f}   | {1-(r[1]+r[2])/r[0]:.4f}",flush=True)
