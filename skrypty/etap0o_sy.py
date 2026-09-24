import numpy as np
def prep(N,seed,ratio=4.0):
    rng=np.random.default_rng(seed); u,v=rng.random(N),rng.random(N)
    C=((u[:,None]<u[None,:])&(v[:,None]<v[None,:])).astype(float)
    D=0.5*(C.T-C); al,V=np.linalg.eigh(1j*D)
    h=0.5*(1-1/np.sqrt(ratio)); U=np.where((u>h)&(u<1-h)&(v>h)&(v<1-h))[0]
    return al,V,U
def S_of(al,V,U,N,c):
    kg=c*np.sqrt(N)/(4*np.pi); keep=np.abs(al)>kg; pos=keep&(al>0)
    VU=V[U]
    Du=(VU[:,keep]*al[keep])@VU[:,keep].conj().T
    Wu=(VU[:,pos]*al[pos])@VU[:,pos].conj().T
    NU=len(U); mu,Q=np.linalg.eigh(1j*Du); ku=c*np.sqrt(NU)/(4*np.pi)
    sel=np.abs(mu)>ku
    if sel.sum()<2: return 0.0,0
    P=Q[:,sel]; B=P.conj().T@Wu@P
    lam=np.linalg.eigvals(B/mu[sel][:,None]).real
    lam=lam[(np.abs(lam)>1e-10)&(np.abs(lam-1)>1e-10)]
    return float(np.sum(lam*np.log(np.abs(lam)))), int(sel.sum())
cs=[0.1,0.25,0.5,1.0,2.0,4.0]
Ns=[1024,2048,3072]
tab={c:[] for c in cs}
for N in Ns:
    accs={c:[] for c in cs}
    for s in [1,2]:
        al,V,U=prep(N,s)
        for c in cs:
            S,m=S_of(al,V,U,N,c); accs[c].append((S,m))
    for c in cs: tab[c].append((N,np.mean([a[0] for a in accs[c]]),np.mean([a[1] for a in accs[c]])))
print("   c   | S(N=1024)  S(2048)  S(3072) | modow w U | nachylenie wzgledem ln N")
for c in cs:
    v=tab[c]; sl=np.polyfit(np.log([x[0] for x in v]),[x[1] for x in v],1)[0]
    print(f" {c:5.2f} | "+"  ".join(f"{x[1]:8.3f}" for x in v)+f" | {v[-1][2]:6.0f}    | {sl:+.3f}")
print("\nporownanie: 1/6 = 0.167, 1/3 = 0.333")
