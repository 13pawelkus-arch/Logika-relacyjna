"""Kalibracja: czy estymator z porzadku = wymiar sieci partnerow + 1?
Sieci wstawione swiadomie: krag (1D), siatka 11x11 (2D), szescian 5x5x5 (3D), periodyczne.
W kazdym kroku trojka partnerow losowana sposrod sasiadow siatki (dynamika)."""
import numpy as np, sys
exec(open('wzrost_v1.py').read().split('N,W=int(sys.argv[1])')[0])
def neighbors(shape):
    idx=np.arange(np.prod(shape)).reshape(shape); nb=[]
    for flat in range(idx.size):
        c=np.array(np.unravel_index(flat,shape)); lst=[]
        for ax in range(len(shape)):
            for s in (-1,1):
                cc=c.copy(); cc[ax]=(cc[ax]+s)%shape[ax]; lst.append(int(idx[tuple(cc)]))
        if len(shape)==1:
            for s2 in (-2,2): lst.append(int((flat+s2)%shape[0]))
        nb.append(sorted(set(lst)))
    return nb
def grow_lattice(N,shape,seed):
    rng=np.random.default_rng(seed); nb=neighbors(shape); W=len(nb)
    C=np.zeros((N,N),bool); tip=list(range(W)); n=W
    while n<N:
        i=int(rng.integers(W)); part=rng.choice(nb[i],3,replace=False)
        chosen=[tip[i]]+[tip[j] for j in part]
        past=C[:n,chosen].any(axis=1); past[chosen]=True
        C[:n,n]=past; tip[i]=n; n+=1
    return C
N=int(sys.argv[1])
print(f"N={N}")
print(" siec              | wymiar sieci | estymator z porzadku (2 ziarna) | oczekiwane (wymiar+1)")
for name,shape in [("krag 128",(128,)),("siatka 11x11",(11,11)),("szescian 5x5x5",(5,5,5))]:
    ds=[dim_intervals(grow_lattice(N,shape,s),np.random.default_rng(s)) for s in [1,2]]
    print(f" {name:17s} | {len(shape)}            | {np.mean(ds):.2f}  ({ds[0]:.2f}, {ds[1]:.2f})              | {len(shape)+1}",flush=True)
