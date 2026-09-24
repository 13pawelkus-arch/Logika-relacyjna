"""H2 kompleksu scian (1+1): z czego sklada sie jadro brzegu nad GF(2). Diagnostyka do wyprowadzenia ranga/F (§F2, C4a.22).
Czesc 1 (N=3000, ziarno 1): baza jadra, redukcja wag, typy 4-cykli, rangi typow I (2-2-2) i II (1-2-2-1), wszystkie 4-cykle.
Wymaga etap0z_gf2.py w tym samym katalogu."""
import numpy as np, sys, collections, itertools
sys.argv=['x','0']; exec(open('etap0z_gf2.py').read().split('print("   N')[0])
def build2(N,seed):
    rng=np.random.default_rng(seed); u,v=rng.random(N),rng.random(N)
    C=((u[:,None]<u[None,:])&(v[:,None]<v[None,:])); Cf=C.astype(np.float32)
    IV=Cf@Cf; L=C&(IV<0.5); C3=IV@Cf
    P,Q=np.where(L); eid={(int(a),int(b)):k for k,(a,b) in enumerate(zip(P,Q))}
    FP,FQ=np.where((IV==2)&C&(C3==0)); faces=[]; fv=[]
    for p,q in zip(FP,FQ):
        a,b=np.where(C[p]&C[:,q])[0]
        faces.append(frozenset({eid[(p,a)],eid[(p,b)],eid[(a,q)],eid[(b,q)]})); fv.append((p,a,b,q))
    return u,v,C,faces,fv
N=int(sys.argv[1]) if False else 3000
u,v,C,faces,fv=build2(N,1)
# jadro: eliminacja ze sledzeniem kombinacji
piv={}; ker=[]
for i,f in enumerate(faces):
    row=set(f); comb={i}
    while row:
        p=min(row)
        if p in piv: row^=piv[p][0]; comb^=piv[p][1]
        else: piv[p]=(row,comb); break
    if not row: ker.append(comb)
print("F",len(faces),"dim ker",len(ker),"rank/F",1-len(ker)/len(faces))
# redukcja wag: powtarzane XOR jesli zmniejsza
ker=[set(k) for k in ker]
for it in range(6):
    ker.sort(key=len); ch=0
    for i in range(len(ker)):
        for j in range(i):
            x=ker[i]^ker[j]
            if len(x)<len(ker[i]): ker[i]=x; ch+=1
    if not ch: break
sz=collections.Counter(len(k) for k in ker); print("rozmiary cykli (liczba scian):",sorted(sz.items())[:15])
# opis najmniejszych
def opis(k):
    el=sorted(set(e for i in k for e in fv[i]))
    sub=C[np.ix_(el,el)]
    return len(el), int(sub.sum())
cnt=collections.Counter(opis(k) for k in ker if len(k)<=8)
print("(elementow, relacji) dla cykli <=8 scian:",cnt.most_common(10))
k=min(ker,key=len); el=sorted(set(e for i in k for e in fv[i]))
print("przyklad: sciany",[tuple(int(z) for z in fv[i]) for i in k])
for e in el: print(e, round(float(u[e]),4), round(float(v[e]),4), "przyszlosc w zbiorze:",[int(z) for z in el if C[e,z]])
# grupy wedlug pary srodkowej
from collections import defaultdict
G=defaultdict(list)
for (p,a,b,q) in fv: G[(min(a,b),max(a,b))].append((p,q))
s=0
for ab,E in G.items():
    P={e[0] for e in E}; Q={e[1] for e in E}
    # skladowe grafu dwudzielnego
    par={}
    def f(x):
        while par.setdefault(x,x)!=x: x=par[x]
        return x
    for p,q in E: par[f(('p',p))]=f(('q',q))
    comp=len({f(('p',p)) for p in P})
    s+=len(E)-len(P)-len(Q)+comp
print("suma beta1(G_ab) =",s," vs dim ker =",len(ker), " grup:",len(G))
typ=collections.Counter()
ex={}
for k in ker:
    if len(k)!=4: continue
    mids=frozenset(frozenset(fv[i][1:3]) for i in k); bots=frozenset(fv[i][0] for i in k); tops=frozenset(fv[i][3] for i in k)
    key=(len(mids),len(bots),len(tops)); typ[key]+=1; ex.setdefault(key,k)
print("typy 4-cykli (ile par srodkowych, dolow, gor):",typ)
for key,k in ex.items():
    print(key,[tuple(int(z) for z in fv[i]) for i in k])
# ile typu II i czy typy sa niezalezne
fidx={fv[i]:i for i in range(len(fv))}
fidx2={}
for i,(p,a,b,q) in enumerate(fv): fidx2[(p,frozenset((a,b)),q)]=i
Cf=C.astype(np.float32); IV=Cf@Cf
XP,XQ=np.where(C&(IV==4)); II=[]
for x,y in zip(XP,XQ):
    m=np.where(C[x]&C[:,y])[0]; S=C[np.ix_(m,m)]
    if S.sum()==4 and (S.sum(0)==2).sum()==2 and (S.sum(1)==2).sum()==2:
        lo=[m[i] for i in range(4) if S[i].sum()==2]; hi=[m[i] for i in range(4) if S[:,i].sum()==2]
        cyc={fidx2[(x,frozenset(lo),h)] for h in hi}|{fidx2[(l,frozenset(hi),y)] for l in lo}
        II.append(cyc)
I4=[]
for ab,E in G.items():
    P=sorted({e[0] for e in E}); Q=sorted({e[1] for e in E}); Es=set(E)
    for p1,p2 in itertools.combinations(P,2):
        for q1,q2 in itertools.combinations(Q,2):
            if {(p1,q1),(p1,q2),(p2,q1),(p2,q2)}<=Es:
                I4.append({fidx2[(p,frozenset(ab),q)] for p in (p1,p2) for q in (q1,q2)})
def rank(vs):
    piv={}; r=0
    for v in vs:
        row=set(v)
        while row:
            p=min(row)
            if p in piv: row^=piv[p]
            else: piv[p]=row; r+=1; break
    return r
import itertools
print("#II",len(II),"#I(4-cykle)",len(I4),"rank I",rank(I4),"rank II",rank(II),"rank I+II",rank(I4+II),"dim ker",len(ker))
# wszystkie 4-cykle: pary scian o wspolnym linku, suma -> klucz; dwie rozlaczne pary o tej samej sumie
l2f=defaultdict(list)
for i,f in enumerate(faces):
    for l in f: l2f[l].append(i)
pairs=set()
for l,fs in l2f.items():
    for i,j in itertools.combinations(fs,2): pairs.add((min(i,j),max(i,j)))
bykey=defaultdict(list)
for i,j in pairs: bykey[frozenset(faces[i]^faces[j])].append((i,j))
C4=set()
for k,ps in bykey.items():
    for (a,b),(c,d) in itertools.combinations(ps,2):
        if len({a,b,c,d})==4: C4.add(frozenset((a,b,c,d)))
C4=[set(c) for c in C4]
print("wszystkich 4-cykli:",len(C4),"ich ranga:",rank(C4),"dim ker:",len(ker))
