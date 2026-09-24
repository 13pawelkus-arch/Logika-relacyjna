"""Zakotwiczenie na zrodlach: skalowanie liczby par miedzy dwiema liniami swiata.
(1) pary w relacji, (2) pary polaczone linkiem, (3) korony w calym sprinklingu (probkowanie)."""
import numpy as np, sys
def run(N,seed):
    rng=np.random.default_rng(seed); u,v=rng.random(N),rng.random(N)
    C=((u[:,None]<u[None,:])&(v[:,None]<v[None,:]))
    Cf=C.astype(np.float32); C2=(Cf@Cf)>0.5                    # istnieje element posredni
    L=np.zeros(N,int); prev=-np.ones(N,int)
    for x in np.argsort(u+v):
        ps=np.where(C[:,x])[0]
        if len(ps): j=ps[np.argmax(L[ps])]; L[x]=L[j]+1; prev[x]=j
    def chain(mask):
        Lm=np.zeros(N,int); pv=-np.ones(N,int)
        for x in np.argsort(u+v):
            if not mask[x]: continue
            ps=np.where(C[:,x]&mask)[0]
            if len(ps): j=ps[np.argmax(Lm[ps])]; Lm[x]=Lm[j]+1; pv[x]=j
        x=int(np.argmax(np.where(mask,Lm,-1))); out=[]
        while x>=0: out.append(x); x=pv[x]
        return np.array(out[::-1])
    m=np.ones(N,bool); ch1=chain(m); m[ch1]=False; ch2=chain(m)
    rel=int(C[np.ix_(ch1,ch2)].sum()+C[np.ix_(ch2,ch1)].sum())
    lk=int((C[np.ix_(ch1,ch2)]&~C2[np.ix_(ch1,ch2)]).sum()+(C[np.ix_(ch2,ch1)]&~C2[np.ix_(ch2,ch1)]).sum())
    # korony w calym sprinklingu: probkowanie par nieporownywalnych
    Rel=C|C.T; np.fill_diagonal(Rel,True)
    a=rng.integers(0,N,4000); b=rng.integers(0,N,4000); ok=~Rel[a,b]
    a,b=a[ok],b[ok]; tot=0
    for x,y in zip(a,b):
        f=np.where(C[x]&C[y])[0]
        if len(f)<2: continue
        tot+=len(f)*(len(f)-1)/2-C[np.ix_(f,f)].sum()
    npairs=(N*(N-1)/2)*( (~Rel).sum()/2 )/(N*(N-1)/2)          # liczba par nieporownywalnych
    crowns=tot/len(a)*((~Rel).sum()/2)/2                        # /2: (b1,b2) nieuporzadkowane juz uwzglednione
    return len(ch1),len(ch2),rel,lk,crowns
print(" N    | L1  L2 | pary w relacji | linki | korony (calosc)")
res=[]
for N in [300,600,1200,2400]:
    r=np.array([run(N,s) for s in [1,2,3]]).mean(axis=0); res.append((N,)+tuple(r))
    print(f"{N:5d} | {r[0]:3.0f} {r[1]:3.0f} | {r[2]:10.1f}     | {r[3]:5.1f} | {r[4]:.3e}")
res=np.array(res)
for i,name in [(3,"L1 (dlugosc lancucha)"),(5,"pary w relacji"),(6,"linki miedzy liniami"),(7,"korony w calosci")]:
    p=np.polyfit(np.log(res[:,0]),np.log(res[:,i-2]),1)[0]
    print(f"wykladnik w N: {name:24s} {p:+.2f}")
