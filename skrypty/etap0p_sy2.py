"""Poprawione: lambda = 1/2 + nu, nu = wartosci wlasne (iDelta|U)^-1 R|U.
Mody niefizyczne: lambda in (0,1)  (|nu|<1/2) - lamie nieoznaczonosc, usuwane przez obciecie lokalne.
Wariant A: tylko obciecie lokalne minimalne (bez globalnego)  -> oczekiwane prawo objetosciowe.
Wariant B: podwojne obciecie (globalne sqrt(N)/4pi + lokalne sqrt(N_U)/4pi + usuniecie niefizycznych)."""
import numpy as np
def prep(N,seed,ratio):
    rng=np.random.default_rng(seed); u,v=rng.random(N),rng.random(N)
    C=((u[:,None]<u[None,:])&(v[:,None]<v[None,:])).astype(float)
    D=0.5*(C.T-C); al,V=np.linalg.eigh(1j*D)
    h=0.5*(1-1/np.sqrt(ratio)); U=np.where((u>h)&(u<1-h)&(v>h)&(v<1-h))[0]
    return al,V,U
def entropy(al,V,U,N,cg=None,cu=None):
    VU=V[U]; NU=len(U)
    keep=np.ones(len(al),bool) if cg is None else np.abs(al)>cg*np.sqrt(N)/(4*np.pi)
    pos=keep&(al>0)
    Du=(VU[:,keep]*al[keep])@VU[:,keep].conj().T          # iDelta|U (po obcieciu globalnym)
    Wu=(VU[:,pos]*al[pos])@VU[:,pos].conj().T             # W|U
    Ru=Wu-0.5*Du                                          # R|U (czesc rzeczywista)
    mu,Q=np.linalg.eigh(Du)
    thr=(1e-10*np.abs(mu).max()) if cu is None else cu*np.sqrt(NU)/(4*np.pi)
    sel=np.abs(mu)>thr
    P=Q[:,sel]
    nu=np.linalg.eigvals((P.conj().T@Ru@P)/mu[sel][:,None]).real
    lam=0.5+nu
    unphys=np.sum((lam>1e-8)&(lam<1-1e-8))
    good=lam[(lam>=1-1e-8)|(lam<=1e-8)]
    good=good[np.abs(good)>1e-10]
    return float(np.sum(good*np.log(np.abs(good)))), NU, int(sel.sum()), int(unphys), int(len(lam))
print("WARIANT A: bez obciecia globalnego, lokalnie tylko usuniecie modow niefizycznych (V/V_U=16)")
print("   N   | N_U | modow | niefiz./wszystkie |   S     | S/N_U")
A=[]
for N in [512,1024,2048,3072]:
    r=[entropy(*prep(N,s,16.0),N) for s in [1,2]]
    S=np.mean([x[0] for x in r]); NU=np.mean([x[1] for x in r])
    print(f"{N:6d} | {NU:4.0f} | {np.mean([x[2] for x in r]):5.0f} | {np.mean([x[3] for x in r]):5.0f} / {np.mean([x[4] for x in r]):4.0f}      | {S:7.2f} | {S/NU:.3f}")
    A.append([NU,S])
A=np.array(A); print(f"  wykladnik S wzgledem N_U: {np.polyfit(np.log(A[:,0]),np.log(A[:,1]),1)[0]:+.2f}  (1 = prawo objetosciowe)")
print("\nWARIANT B: podwojne obciecie (c_g = c_u = 1)")
print("   N   | N_U | modow | niefiz./wszystkie |   S")
B=[]
for N in [512,1024,2048,3072,4096]:
    r=[entropy(*prep(N,s,16.0),N,cg=1.0,cu=1.0) for s in [1,2]]
    S=np.mean([x[0] for x in r]); NU=np.mean([x[1] for x in r])
    print(f"{N:6d} | {NU:4.0f} | {np.mean([x[2] for x in r]):5.0f} | {np.mean([x[3] for x in r]):5.0f} / {np.mean([x[4] for x in r]):4.0f}      | {S:7.3f}")
    B.append([N,S])
B=np.array(B)
print(f"  S = {np.polyfit(np.log(B[:,0]),B[:,1],1)[0]:.3f}*ln N + ...   | 1/6=0.167, 1/3=0.333")
