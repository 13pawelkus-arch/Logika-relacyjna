"""Wazona suma Fokkera miedzy dwiema liniami swiata, czas wlasny Z PORZADKU (najdluzszy lancuch).
S = (alpha*t_P)^2/Delta * #{pary (x,y) miedzy liniami z s^2_int <= Delta},  alpha=1/sqrt(2), t_P=N^{-1/2}."""
import numpy as np, sys
al=1/np.sqrt(2)
def chains(N,rng):
    u,v=rng.random(N),rng.random(N)
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
def nlong(C,x,y,u,v):                     # najdluzszy lancuch od x do y (na elementach przedzialu)
    I=np.where(C[x]&C[:,y])[0]
    if len(I)==0: return 1                 # link: dlugosc 1 krok
    o=I[np.argsort((u+v)[I])]
    L=np.ones(len(o),int)
    for i in range(len(o)):
        ps=np.where(C[o[:i],o[i]])[0]
        if len(ps): L[i]=L[ps].max()+1
    return int(L.max())+1
def run(N,seed,Deltas,frac=1.0):
    rng=np.random.default_rng(seed); u,v=chains(N,rng)[:2]
    u,v,C,c1,c2=chains(N,np.random.default_rng(seed))
    k1=int(len(c1)*frac); k2=int(len(c2)*frac)
    a=c1[:k1]; b=c2[:k2]; tP=N**-0.5
    pairs=[]
    for x in a:
        for y in b[C[x,b]]:
            V=(u[y]-u[x])*(v[y]-v[x])           # objetosc przedzialu = s^2/2
            if 2*V<=max(Deltas)*3:              # wstepny filtr, potem dokladny czas wlasny z porzadku
                pairs.append((x,y))
        for y in b[C[b,x]]:
            V=(u[x]-u[y])*(v[x]-v[y])
            if 2*V<=max(Deltas)*3: pairs.append((y,x))
    s2=[]
    for x,y in pairs:
        n=nlong(C,x,y,u,v); s2.append((al*tP*n)**2)
    s2=np.array(s2)
    return len(c1),k1,[( (al*tP)**2/D*np.sum(s2<=D) ) for D in Deltas],[int(np.sum(s2<=D)) for D in Deltas]
Deltas=[0.005,0.01,0.02,0.04]
print("Zdanie 1 i 2: S w funkcji N i Delta (3 realizacje)")
print("   N  |  L  | "+"  ".join(f"D={D:<6}" for D in Deltas)+" |  liczby par")
for N in [600,1200,2400,4800]:
    Ss=[];cs=[];Ls=[]
    for s in [1,2,3]:
        L,k,S,c=run(N,s,Deltas); Ss.append(S); cs.append(c); Ls.append(L)
    Ss=np.array(Ss).mean(axis=0); cs=np.array(cs).mean(axis=0)
    print(f"{N:5d} | {np.mean(Ls):3.0f} | "+"  ".join(f"{x:7.2f}" for x in Ss)+" | "+" ".join(f"{c:5.0f}" for c in cs))
print("\nZdanie 3: S w funkcji dlugosci odcinka (N=2400, frakcja linii)")
for f in [0.25,0.5,0.75,1.0]:
    Ss=[]
    for s in [1,2,3]:
        L,k,S,c=run(2400,s,Deltas,frac=f); Ss.append(S)
    print(f"  frakcja {f:4.2f}: "+"  ".join(f"{x:7.2f}" for x in np.array(Ss).mean(axis=0)))
