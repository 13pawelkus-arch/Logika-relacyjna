import numpy as np
du,dv=0.8,0.02; u0,v0=0.1,0.1
def tau(a,b): return np.sqrt(np.maximum(2*(b[0]-a[0])*(b[1]-a[1]),0))   # ds^2=2 du dv
def rperp(e,a,p):
    ta,tb,tab=tau(e,a),tau(e,p),tau(p,a)
    val=(ta+tb+tab)*(ta+tb-tab)*(ta-tb+tab)*(ta-tb-tab)
    return np.sqrt(max(val,0))/(2*ta)
print("  N     | dlugosc | r_poprz: srednia    max      | r/tau")
res=[]
for N in [600,2400,9600,38400,153600]:
    Rm=[];Rx=[];Ls=[]
    for seed in range(1,6):
        rng=np.random.default_rng(seed); u,v=rng.random(N),rng.random(N)
        idx=np.where((u>u0)&(u<u0+du)&(v>v0)&(v<v0+dv))[0]
        U,V=u[idx],v[idx]; o=np.argsort(U); U,V=U[o],V[o]
        L=np.ones(len(U),int); pv=-np.ones(len(U),int)
        for i in range(len(U)):
            js=np.where((U[:i]<U[i])&(V[:i]<V[i]))[0]
            if len(js): j=js[np.argmax(L[js])]; L[i]=L[j]+1; pv[i]=j
        i=int(np.argmax(L)); ch=[]
        while i>=0: ch.append(i); i=pv[i]
        ch=ch[::-1]; e=(U[ch[0]],V[ch[0]]); a=(U[ch[-1]],V[ch[-1]])
        rs=[rperp(e,a,(U[k],V[k])) for k in ch[1:-1]]
        if rs: Rm.append(np.mean(rs)); Rx.append(np.max(rs)); Ls.append(len(ch))
    t=tau((u0,v0),(u0+du,v0+dv))
    print(f"{N:7d} | {np.mean(Ls):6.1f}  | {np.mean(Rm):.3e}  {np.mean(Rx):.3e} | {np.mean(Rm)/t:.3f}")
    res.append([N,np.mean(Rm),np.mean(Rx)])
res=np.array(res)
for i,nm in [(1,"srednie r_poprz"),(2,"max r_poprz")]:
    p=np.polyfit(np.log(res[:,0]),np.log(res[:,i]),1)[0]
    print(f"wykladnik w N: {nm:16s} {p:+.3f}   (przewidywanie Boguna-Krioukov: -0.167)")
