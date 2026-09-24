"""Czy warstwa wokol stozka o USTALONEJ objetosci daje sume ~ L (ekstensywna w czasie wlasnym)?
Dla par (x na linii 1, y na linii 2) w relacji liczymy objetosc przedzialu |I(x,y)|/N.
Prog k elementow (skala dyskretnosci) vs prog eps objetosci (skala ustalona)."""
import numpy as np
def run(N,seed):
    rng=np.random.default_rng(seed); u,v=rng.random(N),rng.random(N)
    C=((u[:,None]<u[None,:])&(v[:,None]<v[None,:]))
    def chain(mask):
        Lm=np.zeros(N,int); pv=-np.ones(N,int)
        for x in np.argsort(u+v):
            if not mask[x]: continue
            ps=np.where(C[:,x]&mask)[0]
            if len(ps): j=ps[np.argmax(Lm[ps])]; Lm[x]=Lm[j]+1; pv[x]=j
        x=int(np.argmax(np.where(mask,Lm,-1))); o=[]
        while x>=0: o.append(x); x=pv[x]
        return np.array(o[::-1])
    m=np.ones(N,bool); c1=chain(m); m[c1]=False; c2=chain(m)
    Cf=C.astype(np.float32); IV=(Cf@Cf)                     # liczba elementow w przedziale
    out={}
    for k in [0,1,3]:
        out[f"k<={k}"]=int(((C[np.ix_(c1,c2)])&(IV[np.ix_(c1,c2)]<=k)).sum()+((C[np.ix_(c2,c1)])&(IV[np.ix_(c2,c1)]<=k)).sum())
    for e in [0.002,0.005]:
        thr=e*N
        out[f"eps={e}"]=int(((C[np.ix_(c1,c2)])&(IV[np.ix_(c1,c2)]<=thr)).sum()+((C[np.ix_(c2,c1)])&(IV[np.ix_(c2,c1)]<=thr)).sum())
    return len(c1),out
Ns=[300,600,1200,2400]; keys=None; tab=[]
for N in Ns:
    rs=[run(N,s) for s in [1,2,3]]; keys=list(rs[0][1].keys())
    L=np.mean([r[0] for r in rs]); vals=[np.mean([r[1][k] for r in rs]) for k in keys]
    tab.append([N,L]+vals); print(f"N={N:5d} L={L:5.1f} | "+"  ".join(f"{k}: {v:7.1f}" for k,v in zip(keys,vals)))
tab=np.array(tab)
print("\nwykladniki w N (L ma +0.5):")
for i,k in enumerate(keys):
    print(f"  {k:10s}: {np.polyfit(np.log(tab[:,0]),np.log(np.maximum(tab[:,2+i],0.5)),1)[0]:+.2f}")
