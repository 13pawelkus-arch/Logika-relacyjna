# etap33 (poprawka 241): przybywanie relacji a separatory — rozstrzygnięcie [?] z 171.
# Dokładne ułamki, CPU, sekundy. Losowe porządki wymiaru 2 to tylko świadkowie (twierdzenie ich nie używa).
# Zdanie do upadku: istnieje skończony porządek S z wektorem jądra Δ = C − Cᵀ o sumie 0,
# który nie jest kombinacją różnic bliźniaków. Upada, jeśli dla N ≤ 8 takiego nie ma.
# Kontrola: po dołożeniu L elementów nad całym S (łańcuch — tylko jako świadek „bez końca”)
# ten wektor nadal leży w jądrze, a elementy C nie są separatorami.
import random, itertools
from fractions import Fraction as Fr

def nullspace(M):
    M=[[Fr(x) for x in r] for r in M]; m=len(M); n=len(M[0]); piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if M[i][c]!=0),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]; pv=M[r][c]; M[r]=[x/pv for x in M[r]]
        for i in range(m):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[a-f*b for a,b in zip(M[i],M[r])]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]; basis=[]
    for fc in free:
        v=[Fr(0)]*n; v[fc]=Fr(1)
        for i,pc in enumerate(piv): v[pc]=-M[i][fc]
        basis.append(v)
    return basis

def rank(V):
    if not V: return 0
    return len(V[0])-len(nullspace(V))

def order_dim2(N):
    a=list(range(N)); b=list(range(N)); random.shuffle(b)
    return [[1 if (a[x]<a[y] and b[x]<b[y]) else 0 for y in range(N)] for x in range(N)]

def kernel(C):
    N=len(C); D=[[C[x][y]-C[y][x] for y in range(N)] for x in range(N)]
    return nullspace(D)

def twins(C):
    N=len(C); T=[]
    for x,y in itertools.combinations(range(N),2):
        if all(C[z][x]==C[z][y] for z in range(N)) and all(C[x][z]==C[y][z] for z in range(N)):
            v=[0]*N; v[x]=1; v[y]=-1; T.append(v)
    return T

random.seed(1)
found=None
for N in range(3,9):
    for _ in range(400):
        C=order_dim2(N)
        K=kernel(C)
        Z=[v for v in K]  # podprzestrzeń sumy zero: jądro ∩ {Σ=0}
        if not K: continue
        # jądro ∩ {Σ=0}
        A=[ [sum(v) for v in K] ]
        coef=nullspace(A) if any(sum(v)!=0 for v in K) else [[Fr(int(i==j)) for j in range(len(K))] for i in range(len(K))]
        Z=[[sum(c[k]*K[k][i] for k in range(len(K))) for i in range(N)] for c in coef]
        T=twins(C)
        if rank(Z+T) > rank(T):
            found=(N,C,Z,T); break
    if found: break

N,C,Z,T=found
print('N =',N,'| relacje x≺y:',[(x,y) for x in range(N) for y in range(N) if C[x][y]])
print('bliźniaki:',T)
w=next(v for v in Z if rank(T+[v])>rank(T))
print('wektor jądra o sumie 0, nie z bliźniaków:',[str(x) for x in w])
# Kontrola: dołożyć L elementów, każdy nad całym S (i łańcuch między nimi)
for L in (1,5,20):
    M=N+L
    C2=[[0]*M for _ in range(M)]
    for x in range(N):
        for y in range(N): C2[x][y]=C[x][y]
    for i in range(L):
        for x in range(N): C2[x][N+i]=1
        for j in range(i+1,L): C2[N+i][N+j]=1
    D2=[[C2[x][y]-C2[y][x] for y in range(M)] for x in range(M)]
    w2=list(w)+[Fr(0)]*L
    res=max(abs(sum(D2[r][c]*w2[c] for c in range(M))) for r in range(M))
    # czy któryś element C jest separatorem: ma pod sobą z nośnika tylko jeden maksymalny element nośnika
    supp=[i for i in range(N) if w[i]!=0]
    maxs=[x for x in supp if not any(C[x][y] for y in supp)]
    sep=any(sum(C2[x][N+i] for x in maxs)==1 for i in range(L))
    print(f'L={L}: |Δw| = {res}, separator wśród dołożonych: {sep}, maksymalne w nośniku: {maxs}')

# --- Ogólna postać [T], sprawdzenie na losowych przypadkach.
# Zdanie do upadku: dla S i dołożonych elementów z_1..z_L (każdy nad częścią S, nic z S nad nim)
# jądro S∪Z ograniczone do S = {f ∈ ker Δ_S : Σ_{S∩przesz(z_i)} f = 0 dla każdego i},
# a składowe na Z są zerowe; liczy się liczba RÓŻNYCH widzianych zbiorów, nie L.
def downset(C,N,seed_elems):
    D=set()
    for s in seed_elems:
        D.add(s); D|={x for x in range(N) if C[x][s]}
    return D
bad=0; trials=0
for N in range(3,9):
    for _ in range(150):
        C=order_dim2(N); K=kernel(C)
        L=random.randint(1,6)
        seen=[downset(C,N,random.sample(range(N),random.randint(1,N))) for _ in range(L)]
        # dołożyć po 1..3 kopie każdego widzianego zbioru (różne elementy, ten sam zbiór widziany)
        Z=[D for D in seen for _ in range(random.randint(1,3))]
        M=N+len(Z); C2=[[0]*M for _ in range(M)]
        for x in range(N):
            for y in range(N): C2[x][y]=C[x][y]
        for i,D in enumerate(Z):
            for x in D: C2[x][N+i]=1
        K2=kernel(C2)
        # przewidywanie: wektory f na S z ker_S i Σ_D f=0 dla każdego widzianego D, zera na Z
        if K:
            A=[[sum(v[x] for x in D) for v in K] for D in seen]
            co=nullspace(A)
            P=[[sum(c[k]*K[k][i] for k in range(len(K))) for i in range(N)]+[0]*len(Z) for c in co]
        else: P=[]
        # porównanie: rzut K2 na S z zerami na Z — sprawdzamy równość przestrzeni ograniczonych do wektorów zerowych na Z
        K2S=[v for v in K2]
        # przestrzeń K2 ∩ {zera na Z}
        if K2:
            B=[[v[N+i] for v in K2] for i in range(len(Z))]
            co2=nullspace(B) if any(any(r) for r in B) else [[Fr(int(i==j)) for j in range(len(K2))] for i in range(len(K2))]
            Q=[[sum(c[k]*K2[k][i] for k in range(len(K2))) for i in range(M)] for c in co2]
        else: Q=[]
        trials+=1
        if rank(P+Q)!=rank(P) or rank(P+Q)!=rank(Q): bad+=1
print(f'ogólna postać: {trials} prób, niezgodnych {bad}')
