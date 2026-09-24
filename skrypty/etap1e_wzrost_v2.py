"""Regula v2: czworoscian i narodziny. Siec = rozmaitosc 3D z czworoscianow (kazda sciana <= 2 czworosciany).
Odczyt: losowa trajektoria czyta 3 pozostale wierzcholki losowego swojego czworoscianu (+ wlasny koniec = pamiec).
Narodziny z p_b na krok: nowa trajektoria na losowej scianie brzegowej."""
import numpy as np, sys
from collections import deque
from math import gamma
from scipy.optimize import brentq
def f_MM(d): return gamma(d+1)*gamma(d/2)/(4*gamma(3*d/2))
def d_MM(r):
    try: return brentq(lambda d: f_MM(d)-r, 1.01, 20)
    except ValueError: return np.nan
def grow(N,seed,mode,pb=0.05):
    rng=np.random.default_rng(seed)
    tets=[(0,1,2,3)]; face_count={}; tets_of={i:[0] for i in range(4)}
    def fkey(a,b,c): return tuple(sorted((a,b,c)))
    for f in [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]: face_count[fkey(*f)]=1
    W=4; C=np.zeros((N,N),bool); tip=[0,1,2,3]; n=4; step=0; boundary_order=list(face_count.keys())
    while n<N:
        if (step%20==0 if mode=="bez_dynamiki" else rng.random()<pb):
            bf=[f for f,c in face_count.items() if c==1]
            if mode=="bez_dynamiki": f=[g for g in boundary_order if face_count[g]==1][0]
            else: f=bf[int(rng.integers(len(bf)))]
            a,b,c=f; new=W; W+=1
            t=len(tets); tets.append((a,b,c,new)); face_count[f]=2
            for x in (a,b,c): tets_of[x].append(t)
            tets_of[new]=[t]
            for g in [(a,b,new),(a,c,new),(b,c,new)]:
                k=fkey(*g); face_count[k]=face_count.get(k,0)+1; boundary_order.append(k)
            chosen=[tip[a],tip[b],tip[c]]
            past=C[:n,chosen].any(axis=1); past[chosen]=True; C[:n,n]=past; tip.append(n); n+=1
        else:
            i=(step%W) if mode=="bez_dynamiki" else int(rng.integers(W))
            tl=tets_of[i]; t=tl[0] if mode=="bez_dynamiki" else tl[int(rng.integers(len(tl)))]
            others=[x for x in tets[t] if x!=i]
            chosen=[tip[x] for x in others]+([] if mode=="bez_pamieci" else [tip[i]])
            past=C[:n,chosen].any(axis=1); past[chosen]=True; C[:n,n]=past; tip[i]=n; n+=1
        step+=1
    adj=[set() for _ in range(W)]
    for tt in tets:
        for x in tt:
            for y in tt:
                if x!=y: adj[x].add(y)
    return C,adj,W
def balls(adj,W,rng,samples=20):
    out=[]
    for s in rng.choice(W,min(samples,W),replace=False):
        D=np.full(W,-1); D[s]=0; dq=deque([s])
        while dq:
            a=dq.popleft()
            for b in adj[a]:
                if D[b]<0: D[b]=D[a]+1; dq.append(b)
        out.append([np.sum((D>=0)&(D<=k)) for k in range(1,9)])
    return np.mean(out,axis=0), int(max(0,max(D)))
def dim_intervals(C,rng,k=40,minsize=150):
    Cf=C.astype(np.float32); IV=Cf@Cf; P,Q=np.where((IV>=minsize)&C)
    if len(P)==0: return np.nan
    sel=rng.choice(len(P),min(k,len(P)),replace=False); ds=[]
    for s in sel:
        p,q=P[s],Q[s]; I=np.where(C[p]&C[:,q])[0]; m=len(I)
        ds.append(d_MM(C[np.ix_(I,I)].sum()/m**2))
    return np.nanmedian(ds)
N=int(sys.argv[1])
for mode in ["pelna","bez_pamieci","bez_dynamiki"]:
    C,adj,W=grow(N,1,mode); rng=np.random.default_rng(1)
    b,diam=balls(adj,W,rng); dm=dim_intervals(C,rng)
    ratios=b[1:]/b[:-1]
    print(f"\n== {mode}: trajektorii {W}, estymator MM z porzadku {dm:.2f}")
    print("   kulki k=1..8:", " ".join(f"{x:.0f}" for x in b))
    print("   iloraz kolejnych kulek:", " ".join(f"{x:.2f}" for x in ratios), "  (staly>1 = wykladniczo; ->1 = potegowo)")
    kk=np.arange(1,9); m=b<0.5*W
    if m.sum()>=3: print(f"   nachylenie log-log (kulki < W/2): {np.polyfit(np.log(kk[m]),np.log(b[m]),1)[0]:.2f}")
