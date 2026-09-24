"""Skaner niewypelnialnych cykli w grafie linkow (d=2).
V = elementy, E = linki, F = sciany (przedzialy 2-elementowe), beta1 = E-V+skladowe.
D = beta1 - F  (gorne oszacowanie liczby cykli niegenerowanych przez sciany).
Korony z linkow sa niewypelnialne automatycznie (element w pasie zlamalby definicje linku)."""
import numpy as np, sys
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
def scan(N,seed):
    rng=np.random.default_rng(seed); u,v=rng.random(N),rng.random(N)
    C=((u[:,None]<u[None,:])&(v[:,None]<v[None,:]))
    Cf=C.astype(np.float32); IV=Cf@Cf
    L=C&(IV<0.5)                                   # linki
    E=int(L.sum())
    G=csr_matrix((L|L.T).astype(np.int8))
    ncomp,_=connected_components(G,directed=False)
    beta1=E-N+ncomp
    P2,Q2=np.where((IV>1.5)&(IV<2.5)&C)            # kandydaci na sciany
    F=0
    for p,q in zip(P2,Q2):
        I=np.where(C[p]&C[:,q])[0]
        if len(I)==2 and not (C[I[0],I[1]] or C[I[1],I[0]]): F+=1   # oba nieporownywalne = kwadrat
    # korony: pary a1||a2 z co najmniej dwoma wspolnymi nastepnikami-linkami, te zas nieporownywalne
    Lf=L.astype(np.float32); M=Lf@Lf.T             # wspolni nastepnicy linkowi
    kor=0
    P,Q=np.where(np.triu(M>1.5,1))
    for a1,a2 in zip(P,Q):
        if C[a1,a2] or C[a2,a1]: continue
        s=np.where(L[a1]&L[a2])[0]
        if len(s)<2: continue
        kor+=int(((~C[np.ix_(s,s)])&(~C[np.ix_(s,s)].T)).sum()//2)
    return N,E,F,beta1,kor,ncomp
print("   N  | linkow/el | scian/el | beta1/el | D=(beta1-F)/el | korony/el | skladowe")
res=[]
for N in [int(z) for z in sys.argv[1].split(',')]:
    r=np.array([scan(N,s)[1:] for s in [1,2]],dtype=float).mean(axis=0)
    E,F,b1,kor,nc=r
    print(f"{N:5d} | {E/N:9.3f} | {F/N:8.3f} | {b1/N:8.3f} | {(b1-F)/N:14.3f} | {kor/N:9.3f} | {nc:.0f}",flush=True)
    res.append([N,E/N,F/N,(b1-F)/N,kor/N])
res=np.array(res)
for i,nm in [(1,"linkow/el"),(2,"scian/el"),(3,"D/el"),(4,"korony/el")]:
    print(f"wykladnik {nm:10s} w N: {np.polyfit(np.log(res[:,0]),np.log(res[:,i]),1)[0]:+.3f}")
