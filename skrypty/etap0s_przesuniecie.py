import numpy as np, json, os, sys
exec(open('sy2.py').read().split('print("WARIANT A')[0])
def prep2(N,seed):
    rng=np.random.default_rng(seed); u,v=rng.random(N),rng.random(N)
    C=((u[:,None]<u[None,:])&(v[:,None]<v[None,:])).astype(float)
    D=0.5*(C.T-C); al,V=np.linalg.eigh(1j*D)
    return al,V,u,v
def Umask(u,v,a,u0,v0):
    return np.where((u>u0)&(u<u0+a)&(v>v0)&(v<v0+a))[0]
N=int(sys.argv[1]); nse=int(sys.argv[2]); a=0.25   # r=16
CK='shift.json'; res=json.load(open(CK)) if os.path.exists(CK) else {}
przes=[("srodek",0.0,0.0),("przestrz 0,1",+0.1,-0.1),("przestrz 0,2",+0.2,-0.2),
       ("przestrz 0,3",+0.3,-0.3),("czas +0,1",+0.1,+0.1),("czas +0,2",+0.2,+0.2)]
for s in range(1,nse+1):
    al,V,u,v=prep2(N,s)
    for nazwa,du,dv in przes:
        k=f"{N}|{nazwa}|{s}"
        if k in res: continue
        U=Umask(u,v,a,0.375+du,0.375+dv)
        res[k]={"NU":len(U)}
        for c in [1.0,2.0]:
            res[k][str(c)]=entropy(al,V,U,N,cg=c,cu=c)[0]
        json.dump(res,open(CK,'w'))
    print(f"N={N} s={s} gotowe",flush=True)
print(f"\n{'przesuniecie':14s} | N_U | S(c=1)          | S(c=2)")
for nazwa,du,dv in przes:
    A=np.array([res[f"{N}|{nazwa}|{s}"]["1.0"] for s in range(1,nse+1)])
    B=np.array([res[f"{N}|{nazwa}|{s}"]["2.0"] for s in range(1,nse+1)])
    NU=np.mean([res[f"{N}|{nazwa}|{s}"]["NU"] for s in range(1,nse+1)])
    print(f"{nazwa:14s} | {NU:4.0f} | {A.mean():5.3f}±{A.std(ddof=1)/np.sqrt(len(A)):.3f}  | {B.mean():5.3f}±{B.std(ddof=1)/np.sqrt(len(B)):.3f}")
