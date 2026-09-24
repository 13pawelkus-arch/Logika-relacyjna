"""Masa jako czestosc samoodczytu: ile razy element trajektorii i czyta trajektorie j,
ktora WCZESNIEJ czytala i (najkrotsza zamknieta petla odczytu). Struktura jak w zadaniu A."""
import numpy as np, sys
exec(open('t3.py').read().split('if __name__')[0])
def historia(t,x,chains,losowo=False,seed=1):
    rng=np.random.default_rng(seed); Kc=len(chains); E=np.array(chains); L=E.shape[1]
    tE=t[E]; xE=x[E]; ar=np.arange(L)[None,:]
    czytal={}                       # (i,j) -> lista krokow, w ktorych i czytal j
    odczyty=[[] for _ in range(Kc)] # na trajektorie: lista (krok, [j,...])
    for k in range(Kc):
        for s in range(L):
            dt=tE-tE[k,s]; d2=((xE-xE[k,s])**2).sum(2); past=(dt<0)&(dt**2>d2)
            lp=np.where(past.any(1),np.where(past,ar,-1).max(1),-1)
            sw=np.where(lp>=0,(L-1)-lp,10**6); sw[k]=10**6
            ok=np.where(sw<10**6)[0]
            if len(ok)==0: continue
            czyt=list(rng.choice(ok,min(3,len(ok)),replace=False)) if losowo else list(ok[np.argsort(sw[ok])[:3]])
            odczyty[k].append((s,[int(j) for j in czyt]))
            for j in czyt: czytal.setdefault((k,int(j)),[]).append(s)
    return odczyty,czytal
def powroty(odczyty,czytal,Kc,zakres=None):
    out=np.zeros(Kc); licz=np.zeros(Kc)
    for k in range(Kc):
        for s,js in odczyty[k]:
            if zakres and not (zakres[0]<=s<zakres[1]): continue
            licz[k]+=len(js)
            for j in js:
                wcz=czytal.get((j,k),[])
                if any(u<s for u in wcz): out[k]+=1
    return np.divide(out,np.maximum(licz,1))
N,K,L=1_500_000,1200,12
rng=np.random.default_rng(1); t,x=sprinkle(N,rng); ch,h=trajektorie(t,x,K,L,rng)
Kc=len(ch); print(f"trajektorii {Kc} x {L}, okno {h:.3f}")
for nazwa,los in [("odczyt najswiezszych",False),("odczyt losowy (kontrola)",True)]:
    od,cz=historia(t,x,ch,losowo=los)
    p=powroty(od,cz,Kc); p1=powroty(od,cz,Kc,(0,L//2)); p2=powroty(od,cz,Kc,(L//2,L))
    m=(p1>0)|(p2>0)
    r=np.corrcoef(p1[m],p2[m])[0,1]
    print(f" {nazwa:26s}: srednia czestosc powrotow {p.mean():.3f} ± {p.std()/np.sqrt(Kc):.3f}"
          f" | rozrzut miedzy trajektoriami {p.std():.3f}"
          f" | korelacja polowa-polowa {r:+.3f} (n={m.sum()})",flush=True)
