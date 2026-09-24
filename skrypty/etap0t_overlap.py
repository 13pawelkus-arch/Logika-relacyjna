"""Odleglosc przestrzenna z porzadku (Boguna-Krioukov 2401.17376), d=2.
O = N[C]/(min(N[A],N[B])+N[C]);  d = tau_c (1-O)/sqrt(O);  tau_c = 0.5*alpha1*rho^-1/2*(n(c,a)+n(c,b))."""
import numpy as np, sys
al1=1/np.sqrt(2)
def run(N,l,seed,ta=0.8):
    rng=np.random.default_rng(seed)
    t=np.concatenate([rng.random(N),[ta,ta]]); x=np.concatenate([rng.random(N)-0.5,[-l/2,+l/2]])
    A,B=N,N+1                                  # indeksy zdarzen a i b
    def prec(i,J):                             # i < J (wektorowo)
        return (t[J]-t[i])>np.abs(x[J]-x[i])
    idx=np.arange(len(t))
    pa=idx[(t<ta)&((ta-t)>np.abs(x-x[A]))]     # przeszlosc a
    pb=idx[(t<ta)&((ta-t)>np.abs(x-x[B]))]
    common=np.intersect1d(pa,pb)
    # dlugosc najdluzszego lancucha do celu: DP po przeszlosci celu
    def chains(target,past):
        o=past[np.argsort(-t[past])]; h={}
        for k,xk in enumerate(o):
            later=o[:k]
            m=0
            if len(later):
                rel=(t[later]-t[xk])>np.abs(x[later]-x[xk])
                if rel.any(): m=max(h[y] for y in later[rel])
            h[xk]=1+m
        return h
    ha=chains(A,pa); hb=chains(B,pb)
    est=[]
    cand=common if len(common)<=2500 else rng.choice(common,2500,replace=False)
    for c in cand:
        Ia=pa[((t[pa]-t[c])>np.abs(x[pa]-x[c]))]            # I(c,a)
        Ib=pb[((t[pb]-t[c])>np.abs(x[pb]-x[c]))]
        NAC,NBC=len(Ia),len(Ib)
        NC=len(np.intersect1d(Ia,Ib,assume_unique=True))
        if NC<5 or NAC<5 or NBC<5: continue
        NA,NB=NAC-NC,NBC-NC
        O=NC/(min(NA,NB)+NC)
        if O<=0 or O>=1: continue
        if abs(NAC-NBC) >= 0.5*np.sqrt(NAC+NBC)*np.sqrt(1-O): continue   # filtr wewnetrzny
        tau_ch=0.5*al1*N**-0.5*(ha[c]+hb[c])
        tau_v=np.sqrt(2*0.5*(NAC+NBC)/N)          # V=tau^2/2 w d=2 -> tau z liczby elementow
        if not (0.25<tau_v<0.45): continue        # okno: tau_c >> l, stozek wewnatrz pudla
        est.append((tau_ch*(1-O)/np.sqrt(O), tau_v*(1-O)/np.sqrt(O)))
    return np.array(est) if est else np.zeros((0,2))
for N in [int(a) for a in sys.argv[1].split(',')]:
    for l in [0.1,0.2]:
        ch=[];vo=[]
        for s in [1,2,3]:
            e=run(N,l,s)
            if len(e): ch.append(np.median(e[:,0])); vo.append(np.median(e[:,1]))
        ch,vo=np.array(ch),np.array(vo)
        print(f"N={N:6d} l={l:.2f} | tau z lancucha: {ch.mean():.4f} ({abs(ch.mean()-l)/l*100:4.1f}%) | tau z objetosci: {vo.mean():.4f} ({abs(vo.mean()-l)/l*100:4.1f}%)",flush=True)
