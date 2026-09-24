"""Czy najdluzszy lancuch utrzymuje rame? Odchylenie poprzeczne od cieciwy okna o m krokach.
1/2 = dyfuzja polozenia, 3/2 = dyfuzja predkosci (swerves), 2/3 = geodezyjna KPZ."""
import numpy as np, sys
def rperp(e,a,p):
    tau=lambda X,Y: np.sqrt(max(2*(Y[0]-X[0])*(Y[1]-X[1]),0))
    ta,tb,tab=tau(e,a),tau(e,p),tau(p,a)
    if ta<=0: return np.nan
    val=(ta+tb+tab)*(ta+tb-tab)*(ta-tb+tab)*(ta-tb-tab)
    return np.sqrt(max(val,0))/(2*ta)
def chain(N,seed):
    rng=np.random.default_rng(seed); u,v=rng.random(N),rng.random(N)
    C=((u[:,None]<u[None,:])&(v[:,None]<v[None,:]))
    L=np.zeros(N,int); pv=-np.ones(N,int)
    for x in np.argsort(u+v):
        ps=np.where(C[:,x])[0]
        if len(ps): j=ps[np.argmax(L[ps])]; L[x]=L[j]+1; pv[x]=j
    x=int(np.argmax(L)); o=[]
    while x>=0: o.append(x); x=pv[x]
    o=o[::-1]
    return np.array([(u[i],v[i]) for i in o])
print("   N  | dlugosc | m: srednie |r_poprz|")
res={}
for N in [int(z) for z in sys.argv[1].split(',')]:
    ms=[4,6,8,12,16,24,32,48,64]
    acc={m:[] for m in ms}
    Ls=[]
    for s in [1,2,3]:
        P=chain(N,s); L=len(P)-1; Ls.append(L)
        for m in ms:
            if m>L//2: continue
            for k in range(0,L-m):
                r=rperp(P[k],P[k+m],P[k+m//2])
                if not np.isnan(r): acc[m].append(r)
    row=[]
    for m in ms:
        if acc[m]: row.append((m,np.mean(acc[m]))); res.setdefault(m,[]).append((N,np.mean(acc[m])))
    print(f"{N:5d} | {np.mean(Ls):6.0f}  | "+"  ".join(f"m={m}: {r:.4f}" for m,r in row),flush=True)
    x=np.array([m for m,_ in row]); y=np.array([r for _,r in row])
    print(f"        wykladnik wzgledem m: {np.polyfit(np.log(x),np.log(y),1)[0]:+.3f}   (1/2 dyfuzja, 2/3 KPZ, 3/2 swerves)")
