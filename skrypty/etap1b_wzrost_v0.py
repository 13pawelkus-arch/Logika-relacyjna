"""Regula wzrostu v0: siec W trajektorii. Nowy element x nad koncem wlasnej trajektorii (pamiec)
i nad koncami trzech innych, wzajemnie nieporownywalnych (triada). Wybor trajektorii losowy (dynamika).
Kontrole: bez pamieci; bez dynamiki (po kolei, stali sasiedzi)."""
import numpy as np, sys
from math import gamma
from scipy.optimize import brentq
def f_MM(d): return gamma(d+1)*gamma(d/2)/(4*gamma(3*d/2))
def d_MM(r):
    try: return brentq(lambda d: f_MM(d)-r, 1.01, 20)
    except ValueError: return np.nan
def grow(N,W,seed,mode):
    rng=np.random.default_rng(seed)
    C=np.zeros((N,N),bool)            # C[a,b] = a < b
    tip=list(range(W)); n=W            # W elementow startowych, antylancuch
    step=0
    while n<N:
        if mode=="bez_dynamiki":
            i=step%W; others=[(i+1)%W,(i+2)%W,(i+3)%W]
        else:
            i=int(rng.integers(W))
            cand=[j for j in range(W) if j!=i]; rng.shuffle(cand)
            others=[];
            for j in cand:
                tj=tip[j]
                if all(not C[tj,tip[k]] and not C[tip[k],tj] for k in others): others.append(j)
                if len(others)==3: break
            if len(others)<3: step+=1; continue
        chosen=[tip[j] for j in others]
        if mode!="bez_pamieci": chosen.append(tip[i])
        past=C[:n,chosen].any(axis=1); past[chosen]=True
        C[:n,n]=past
        tip[i]=n; n+=1; step+=1
    return C
def dim_intervals(C,rng,k=40,minsize=150):
    N=len(C); Cf=C.astype(np.float32); IV=Cf@Cf
    P,Q=np.where((IV>=minsize)&C)
    if len(P)==0: return np.nan,0
    sel=rng.choice(len(P),min(k,len(P)),replace=False); ds=[]
    for s in sel:
        p,q=P[s],Q[s]; I=np.where(C[p]&C[:,q])[0]; n=len(I)
        R=C[np.ix_(I,I)].sum(); ds.append(d_MM(R/n**2))
    return np.nanmedian(ds),len(P)
def twins_inner(C):
    past=C.sum(0); fut=C.sum(1); keys={}
    for i in range(len(C)):
        if past[i]>0 and fut[i]>0: keys.setdefault((C[:,i].tobytes(),C[i,:].tobytes()),[]).append(i)
    return sum(len(v)*(len(v)-1)//2 for v in keys.values())
N=int(sys.argv[1])
print(f"N={N}")
print(" regula          |  W | wymiar (mediana w przedzialach) | przedzialow >=150 | blizniaki we wnetrzu")
for W in [16,64]:
    for mode in ["pelna","bez_pamieci","bez_dynamiki"]:
        ds=[];np_=[];tw=[]
        for s in [1,2]:
            C=grow(N,W,s,mode); d,npairs=dim_intervals(C,np.random.default_rng(s)); ds.append(d); np_.append(npairs); tw.append(twins_inner(C))
        print(f" {mode:15s} | {W:2d} | {np.nanmean(ds):6.3f}                          | {np.mean(np_):9.0f}         | {np.mean(tw):.1f}",flush=True)
