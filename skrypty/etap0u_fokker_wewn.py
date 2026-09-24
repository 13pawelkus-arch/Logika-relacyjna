"""Suma Fokkera z odlegloscia miedzy liniami liczona Z PORZADKU (nakladanie przyczynowe).
R = S*d/tau ; S = (alpha*t_P)^2/Delta * #{pary s^2<=Delta}, s^2 z najdluzszego lancucha.
d: dla probki elementow linii 2 liczymy max po elementach linii 1 przestrzennych wzgledem nich."""
import numpy as np, sys
al=1/np.sqrt(2)
def setup(N,seed):
    rng=np.random.default_rng(seed); u,v=rng.random(N),rng.random(N)
    C=((u[:,None]<u[None,:])&(v[:,None]<v[None,:]))
    def ch(mask):
        L=np.zeros(N,int); pv=-np.ones(N,int)
        for x in np.argsort(u+v):
            if not mask[x]: continue
            ps=np.where(C[:,x]&mask)[0]
            if len(ps): j=ps[np.argmax(L[ps])]; L[x]=L[j]+1; pv[x]=j
        x=int(np.argmax(np.where(mask,L,-1))); o=[]
        while x>=0: o.append(x); x=pv[x]
        return np.array(o[::-1])
    m=np.ones(N,bool); c1=ch(m); m[c1]=False; c2=ch(m)
    return u,v,C,c1,c2
def nlong(C,x,y,u,v):
    I=np.where(C[x]&C[:,y])[0]
    if len(I)==0: return 1
    o=I[np.argsort((u+v)[I])]; L=np.ones(len(o),int)
    for i in range(len(o)):
        ps=np.where(C[o[:i],o[i]])[0]
        if len(ps): L[i]=L[ps].max()+1
    return int(L.max())+1
def d_overlap(C,N,p,q,rng,ncand=120,tmin=0.35,tmax=0.75):
    common=np.where(C[:,p]&C[:,q])[0]
    if len(common)==0: return np.nan
    if len(common)>ncand: common=rng.choice(common,ncand,replace=False)
    out=[]
    for c in common:
        Ia=C[c]&C[:,p]; Ib=C[c]&C[:,q]
        NAC,NBC=int(Ia.sum()),int(Ib.sum()); NC=int((Ia&Ib).sum())
        if min(NAC,NBC)<5 or NC<5: continue
        NA,NB=NAC-NC,NBC-NC
        O=NC/(min(NA,NB)+NC)
        if not (0<O<1): continue
        if abs(NAC-NBC)>=0.5*np.sqrt(NAC+NBC)*np.sqrt(1-O): continue
        tau=np.sqrt(2*0.5*(NAC+NBC)/N)
        if not (tmin<tau<tmax): continue
        out.append(tau*(1-O)/np.sqrt(O))
    return np.median(out) if out else np.nan
def run(N,seed,Ds):
    rng=np.random.default_rng(seed+100)
    u,v,C,c1,c2=setup(N,seed)
    tP=N**-0.5; t=(u+v)/np.sqrt(2); x=(u-v)/np.sqrt(2)
    # d ze wspolrzednych (odniesienie)
    xi=np.interp(t[c1],t[c2],x[c2],left=np.nan,right=np.nan)
    d_xy=np.nanmean(np.abs(x[c1]-xi))
    # d z porzadku: probka elementow linii 2, max po przestrzennych elementach linii 1
    ds=[]; ds_true=[]
    for b in c2[np.linspace(len(c2)//4,3*len(c2)//4,8).astype(int)]:
        cand=c1[(~C[c1,b])&(~C[b,c1])]
        if len(cand)>12: cand=cand[np.linspace(0,len(cand)-1,12).astype(int)]
        vals=[d_overlap(C,N,a,b,rng) for a in cand]
        vals=[z for z in vals if not np.isnan(z)]
        if vals: ds.append(max(vals))
        tv=[np.sqrt(abs((x[a]-x[b])**2-(t[a]-t[b])**2)) for a in cand]
        if tv: ds_true.append(max(tv))
    d_ord=np.mean(ds) if ds else np.nan
    d_true=np.mean(ds_true) if ds_true else np.nan
    # suma Fokkera
    pairs=[]
    for a_ in c1:
        for b_ in c2[C[a_,c2]]:
            if 2*(u[b_]-u[a_])*(v[b_]-v[a_])<=max(Ds)*3: pairs.append((a_,b_))
        for b_ in c2[C[c2,a_]]:
            if 2*(u[a_]-u[b_])*(v[a_]-v[b_])<=max(Ds)*3: pairs.append((b_,a_))
    s2=np.array([(al*tP*nlong(C,p,q,u,v))**2 for p,q in pairs]) if pairs else np.array([])
    tau_tot=al*tP*len(c1)
    S=[(al*tP)**2/D*np.sum(s2<=D) for D in Ds]
    return d_xy,d_true,d_ord,tau_tot,S
Ds=[0.005,0.01,0.02]
print("  N  ziarno | d niezmien. (wspolrz.) | d z porzadku | blad | R=S*d/tau dla Delta=0.005/0.01/0.02")
for N in [int(z) for z in sys.argv[1].split(',')]:
    for s in [1,2]:
        dxy,dtr,dor,tau,S=run(N,s,Ds)
        R=[z*dor/tau for z in S]
        print(f"{N:5d} {s:2d}    | {dtr:.4f} (rownoczasowa {dxy:.4f}) | {dor:.4f} | {(dor-dtr)/dtr*100:+5.1f}% | "
              +"  ".join(f"{r:.3f}" for r in R),flush=True)
