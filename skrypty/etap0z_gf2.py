"""Prawdziwa ranga niewypelnionej czesci: D = beta1 - rank_GF2(brzegi scian).
Eliminacja rzadka nad GF(2): wiersz = zbior indeksow linkow (4 na sciane), pivot = najmniejszy indeks."""
import numpy as np, sys, time
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
def build(N,seed):
    rng=np.random.default_rng(seed); u,v=rng.random(N),rng.random(N)
    C=((u[:,None]<u[None,:])&(v[:,None]<v[None,:])); Cf=C.astype(np.float32)
    IV=Cf@Cf; L=C&(IV<0.5); C3=IV@Cf
    P,Q=np.where(L); eid={(int(a),int(b)):k for k,(a,b) in enumerate(zip(P,Q))}
    E=len(P); ncomp,_=connected_components(csr_matrix(L|L.T),directed=False)
    beta1=E-N+ncomp
    FP,FQ=np.where((IV==2)&C&(C3==0))
    faces=[]
    for p,q in zip(FP,FQ):
        a,b=np.where(C[p]&C[:,q])[0]
        faces.append({eid[(p,a)],eid[(p,b)],eid[(a,q)],eid[(b,q)]})
    return beta1,faces
def rank_gf2(rows):
    piv={}; r=0
    for row in rows:
        row=set(row)
        while row:
            p=min(row)
            if p in piv: row^=piv[p]
            else: piv[p]=row; r+=1; break
    return r
print("   N  |   beta1 |     F | rank(scian) | dim H2 | D_gorne/el | D_prawdziwe/el | czas")
for N in [int(z) for z in sys.argv[1].split(',')]:
    out=[]
    for s in [1,2]:
        t0=time.time(); b1,faces=build(N,s); rk=rank_gf2(faces); out.append((b1,len(faces),rk,time.time()-t0))
    b1=np.mean([o[0] for o in out]); F=np.mean([o[1] for o in out]); rk=np.mean([o[2] for o in out])
    print(f"{N:5d} | {b1:7.0f} | {F:5.0f} | {rk:11.0f} | {F-rk:6.1f} | {(b1-F)/N:10.3f} | {(b1-rk)/N:14.3f} | {np.mean([o[3] for o in out]):.0f}s",flush=True)
