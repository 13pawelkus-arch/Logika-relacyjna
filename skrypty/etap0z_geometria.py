"""Test 6/7, 7/15, 3/5 przy zmianie geometrii. Te same definicje co gf2.py."""
import numpy as np, sys, time
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
def sprinkle(N,seed,geom):
    rng=np.random.default_rng(seed)
    if geom=="diament":
        u,v=rng.random(N),rng.random(N); t=(u+v)/np.sqrt(2); x=(u-v)/np.sqrt(2)
    elif geom=="kwadrat":
        t,x=rng.random(N),rng.random(N)
    elif geom=="szerokie":
        t,x=0.5*rng.random(N),2*rng.random(N)
    dt=t[None,:]-t[:,None]; dx=np.abs(x[None,:]-x[:,None])
    return dt>dx
def stats(C):
    N=len(C); Cf=C.astype(np.float32); IV=Cf@Cf; L=C&(IV<0.5); C3=IV@Cf
    P,Q=np.where(L); eid={(int(a),int(b)):k for k,(a,b) in enumerate(zip(P,Q))}
    E=len(P); nc,_=connected_components(csr_matrix(L|L.T),directed=False); b1=E-N+nc
    FP,FQ=np.where((IV==2)&C&(C3==0)); rows=[]
    for p,q in zip(FP,FQ):
        a,b=np.where(C[p]&C[:,q])[0]
        rows.append({eid[(p,a)],eid[(p,b)],eid[(a,q)],eid[(b,q)]})
    piv={}; r=0
    for row in rows:
        row=set(row)
        while row:
            m=min(row)
            if m in piv: row^=piv[m]
            else: piv[m]=row; r+=1; break
    return b1,len(rows),r,nc
N=int(sys.argv[1]); geoms=sys.argv[2].split(','); nse=int(sys.argv[3])
print(f"N={N}")
print(" geometria | ranga/F  (6/7=0,857) | F/beta1 (7/15=0,467) | D/beta1 (3/5=0,600) | skladowe")
for g in geoms:
    a=[];b=[];c=[];ncs=[]
    for s in range(1,nse+1):
        b1,F,r,nc=stats(sprinkle(N,s,g)); a.append(r/F); b.append(F/b1); c.append((b1-r)/b1); ncs.append(nc)
    f=lambda z: f"{np.mean(z):.4f}±{np.std(z,ddof=1)/np.sqrt(len(z)):.4f}"
    print(f" {g:9s} | {f(a):20s} | {f(b):20s} | {f(c):19s} | {np.mean(ncs):.0f}",flush=True)
