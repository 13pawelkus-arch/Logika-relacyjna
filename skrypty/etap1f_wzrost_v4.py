"""Regula v4: krawedz = Ø z przodu. Narodziny na scianach brzegowych, nowa trajektoria SWIEZA (pusta przeszlosc).
Odczyt: 3 partnerzy + pamiec. Relaksacja wnetrza: z p. q partner -> partner partnera.
Pomiar: kulki w sieci partnerow dla najstarszych i najmlodszych trajektorii."""
import numpy as np, sys
from collections import deque
def grow(N,seed,q,pb=0.12):
    rng=np.random.default_rng(seed)
    face_count={}; fkey=lambda a,b,c: tuple(sorted((a,b,c)))
    for f in [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]: face_count[fkey(*f)]=1
    part={i:[j for j in range(4) if j!=i] for i in range(4)}
    C=np.zeros((N,N),bool); tip=[0,1,2,3]; born=[0,0,0,0]; W=4; n=4; step=0
    while n<N:
        if rng.random()<pb:
            bf=[f for f,c in face_count.items() if c==1]; f=bf[int(rng.integers(len(bf)))]
            a,b,c=f; new=W; W+=1; face_count[f]=2
            for g in [(a,b,new),(a,c,new),(b,c,new)]:
                k=fkey(*g); face_count[k]=face_count.get(k,0)+1
            part[new]=[a,b,c]
            tip.append(n); born.append(step); n+=1                       # swiezy: pusta przeszlosc
        else:
            i=int(rng.integers(W))
            if q>0 and rng.random()<q:
                k=int(rng.integers(3)); via=part[i][int(rng.integers(3))]
                opts=[j for j in part[via] if j!=i and j not in part[i]]
                if opts: part[i][k]=int(rng.choice(opts))
            chosen=[tip[j] for j in part[i]]+[tip[i]]
            past=C[:n,chosen].any(axis=1); past[chosen]=True; C[:n,n]=past; tip[i]=n; n+=1
        step+=1
    adj=[set() for _ in range(W)]
    for i in range(W):
        for j in part[i]: adj[i].add(j); adj[j].add(i)
    return adj,np.array(born),W
def ball(adj,s,K=8):
    W=len(adj); D=np.full(W,-1); D[s]=0; dq=deque([s])
    while dq:
        a=dq.popleft()
        for b in adj[a]:
            if D[b]<0: D[b]=D[a]+1; dq.append(b)
    return [np.sum((D>=0)&(D<=k)) for k in range(1,K+1)]
N=int(sys.argv[1])
print(f"N={N}")
for q in [0.0,0.3]:
    for s in [1,2]:
        adj,born,W=grow(N,s,q); order=np.argsort(born)
        old=order[:max(10,W//5)]; young=order[-max(10,W//5):]
        bo=np.mean([ball(adj,x) for x in old],axis=0); by=np.mean([ball(adj,x) for x in young],axis=0)
        ro=bo[1:5]/bo[:4]; ry=by[1:5]/by[:4]
        print(f" q={q} ziarno {s}: W={W}")
        print(f"    stare : kulki {' '.join(f'{x:.0f}' for x in bo[:6])} | ilorazy {' '.join(f'{x:.2f}' for x in ro)}")
        print(f"    mlode : kulki {' '.join(f'{x:.0f}' for x in by[:6])} | ilorazy {' '.join(f'{x:.2f}' for x in ry)}",flush=True)
