"""Rozklad odleglosci d(A,x) od najdluzszego lancucha A do elementow polaczonych z nim linkiem.
d liczona z nakladania przyczynowego (C4a.17). Jednostka: t_P = N^-1/2."""
import numpy as np, sys
def prep(N,seed):
    rng=np.random.default_rng(seed); u,v=rng.random(N),rng.random(N)
    C=((u[:,None]<u[None,:])&(v[:,None]<v[None,:]))
    L=np.zeros(N,int); pv=-np.ones(N,int)
    for x in np.argsort(u+v):
        ps=np.where(C[:,x])[0]
        if len(ps): j=ps[np.argmax(L[ps])]; L[x]=L[j]+1; pv[x]=j
    x=int(np.argmax(L)); o=[]
    while x>=0: o.append(x); x=pv[x]
    A=np.array(o[::-1])
    Cf=C.astype(np.float32); LK=C&~((Cf@Cf)>0.5)
    return u,v,C,LK,A,rng
def d_ov(C,N,p,q,rng,nc=60):
    com=np.where(C[:,p]&C[:,q])[0]
    if len(com)==0: return np.nan
    if len(com)>nc: com=rng.choice(com,nc,replace=False)
    out=[]
    for c in com:
        Ia=C[c]&C[:,p]; Ib=C[c]&C[:,q]
        NAC,NBC=int(Ia.sum()),int(Ib.sum()); NC=int((Ia&Ib).sum())
        if min(NAC,NBC)<5 or NC<5: continue
        NA,NB=NAC-NC,NBC-NC; O=NC/(min(NA,NB)+NC)
        if not (0<O<1): continue
        if abs(NAC-NBC)>=0.5*np.sqrt(NAC+NBC)*np.sqrt(1-O): continue
        tau=np.sqrt(2*0.5*(NAC+NBC)/N)
        if tau<0.15: continue
        out.append(tau*(1-O)/np.sqrt(O))
    return np.median(out) if out else np.nan
print("   N  | badanych x | d/t_P: mediana  p75   p90   max")
for N in [int(z) for z in sys.argv[1].split(',')]:
    vals=[]
    for s in [1,2]:
        u,v,C,LK,A,rng=prep(N,s); tP=N**-0.5
        linked=np.where(LK[A].any(axis=0)|LK[:,A].any(axis=1))[0]
        linked=linked[~np.isin(linked,A)]
        if len(linked)>40: linked=rng.choice(linked,40,replace=False)
        for x in linked:
            cand=A[(~C[A,x])&(~C[x,A])]
            if len(cand)==0: continue
            if len(cand)>6: cand=cand[np.linspace(0,len(cand)-1,6).astype(int)]
            ds=[d_ov(C,N,a,x,rng) for a in cand]
            ds=[z for z in ds if not np.isnan(z)]
            if ds: vals.append(max(ds)/tP)
    v=np.array(vals)
    print(f"{N:5d} | {len(v):9d}  | {np.median(v):7.2f} {np.percentile(v,75):6.2f} {np.percentile(v,90):6.2f} {v.max():6.2f}",flush=True)
