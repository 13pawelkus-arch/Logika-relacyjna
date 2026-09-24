"""Test lorentzowskosci: porzadek z odczytow na sieci R6 (3D) i R5 (2D).
Kazdy krok: losowa trajektoria czyta konce wszystkich sasiadow w sieci + wlasny koniec (linki).
Estymator Myrheima-Meyera liczony w przedzialach I(p,q), p i q na tej samej trajektorii, k krokow wlasnych."""
import numpy as np, sys
from math import gamma
from scipy.optimize import brentq
exec(open('r6d.py').read().split('mode=sys.argv[1]')[0])
def f_MM(d): return gamma(d+1)*gamma(d/2)/(4*gamma(3*d/2))
def d_MM(r):
    try: return brentq(lambda d: f_MM(d)-r,1.01,20)
    except ValueError: return np.nan
def history(adj,T,seed):
    rng=np.random.default_rng(seed); W=len(adj); nb=[np.array(sorted(a)) for a in adj]
    tip=np.arange(W); parents=[[] for _ in range(W)]; chain=[[i] for i in range(W)]; n=W
    for _ in range(T*W):
        i=int(rng.integers(W)); par=[int(tip[i])]+[int(tip[j]) for j in nb[i]]
        parents.append(par); tip[i]=n; chain[i].append(n); n+=1
    children=[[] for _ in range(n)]
    for e,ps in enumerate(parents):
        for p in ps: children[p].append(e)
    return parents,children,chain
def interval_mm(parents,children,p,q):
    past=set(); st=[q]
    while st:
        x=st.pop()
        for y in parents[x]:
            if y>p and y not in past: past.add(y); st.append(y)
    fut=set(); st=[p]
    while st:
        x=st.pop()
        for y in children[x]:
            if y<q and y not in fut: fut.add(y); st.append(y)
    I=sorted(past & fut); n=len(I)
    if n<60: return np.nan,n
    pos={e:k for k,e in enumerate(I)}; P=[0]*n; R=0
    for k,e in enumerate(I):
        b=0
        for y in parents[e]:
            j=pos.get(y)
            if j is not None: b|=P[j]|(1<<j)
        P[k]=b; R+=bin(b).count("1")
    return d_MM(R/n**2),n
W,T,K=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
for nazwa,pam in [("R5 (siec 2D, kontrola)",False),("R6 (siec 3D, pamiec)",True)]:
    adj=grow(W,1,pamiec=pam); parents,children,chain=history(adj,T,1)
    rng=np.random.default_rng(2); ds=[];ns=[]
    for _ in range(40):
        i=int(rng.integers(W)); c=chain[i]
        if len(c)<K+3: continue
        a=int(rng.integers(1,len(c)-K)); d,n=interval_mm(parents,children,c[a],c[a+K])
        if not np.isnan(d): ds.append(d); ns.append(n)
    print(f" {nazwa:24s}: estymator MM w przedzialach (k={K}) = {np.median(ds):.2f}  (srednia {np.mean(ds):.2f} ± {np.std(ds)/np.sqrt(len(ds)):.2f}, n przedzialow {len(ds)}, sr. rozmiar {np.mean(ns):.0f})",flush=True)
