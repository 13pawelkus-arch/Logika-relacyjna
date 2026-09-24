import numpy as np
src=open('fokker.py').read().split('Deltas=[0.005')[0]; exec(src)
al=1/np.sqrt(2)
def run2(N,seed,Ds):
    rng=np.random.default_rng(seed); u,v,C,c1,c2=chains(N,rng)
    tP=N**-0.5; t=(u+v)/np.sqrt(2); x=(u-v)/np.sqrt(2)
    t1,x1=t[c1],x[c1]; t2,x2=t[c2],x[c2]
    xi=np.interp(t1,t2,x2,left=np.nan,right=np.nan); d=np.nanmean(np.abs(x1-xi))
    tau_tot=al*tP*len(c1)
    pairs=[]
    for a_ in c1:
        for b_ in c2[C[a_,c2]]:
            if 2*(u[b_]-u[a_])*(v[b_]-v[a_])<=max(Ds)*3: pairs.append((a_,b_))
        for b_ in c2[C[c2,a_]]:
            if 2*(u[a_]-u[b_])*(v[a_]-v[b_])<=max(Ds)*3: pairs.append((b_,a_))
    s2=np.array([(al*tP*nlong(C,p,q,u,v))**2 for p,q in pairs]) if pairs else np.array([])
    out=[]
    for D in Ds:
        S=(al*tP)**2/D*np.sum(s2<=D)
        out.append((S, S*d/tau_tot, np.sqrt(2*D*N)))
    return d,tau_tot,out
print("R = S*d/tau  (przewidywanie: stala rzedu 1);  n_max = sqrt(2*Delta*N)")
print("   N   |  Delta   | n_max |   S     |   d    |   R")
rows=[]
for N,Ds in [(1200,[0.01,0.02,0.04,0.08]),(2400,[0.005,0.01,0.02,0.04]),(4800,[0.0025,0.005,0.01,0.02])]:
    acc={D:[] for D in Ds}; ds=[]
    for s in [1,2,3,4]:
        d,tau,out=run2(N,s,Ds); ds.append(d)
        for D,(S,R,nm) in zip(Ds,out): acc[D].append((S,R,nm))
    for D in Ds:
        S=np.mean([a[0] for a in acc[D]]); R=np.mean([a[1] for a in acc[D]]); nm=acc[D][0][2]
        print(f"{N:6d} | {D:7.4f}  | {nm:5.1f} | {S:6.2f}  | {np.mean(ds):.3f}  | {R:.3f}")
        rows.append((N,D,nm,R))
rows=np.array(rows)
print("\ntest zbieznosci po n_max (pary o tym samym n_max, rozne N i Delta):")
for nm in sorted(set(np.round(rows[:,2],1))):
    sel=rows[np.abs(rows[:,2]-nm)<0.15]
    if len(sel)>1:
        print(f"  n_max={nm:5.1f}: R = "+", ".join(f"{r:.3f} (N={int(n)}, D={D:.4f})" for n,D,_,r in sel))
print(f"\nwykladnik R wzgledem n_max (wszystkie punkty): {np.polyfit(np.log(rows[:,2]),np.log(rows[:,3]),1)[0]:+.2f}")
print(f"wykladnik R wzgledem Delta  (wszystkie punkty): {np.polyfit(np.log(rows[:,1]),np.log(rows[:,3]),1)[0]:+.2f}")
