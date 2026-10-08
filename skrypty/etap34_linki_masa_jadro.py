# etap34 — kontrola poprawki 242: skoki po linkach i zatrzymania (wagi Johnstona bez gestosci).
# Rozstrzygniecie: masa/linki-separatory-jadro.md. Twierdzenia sa na kartce; tu tylko kontrola liczb,
# dokladnie (sympy: wymierne i symbol eta = a*b), bez losowania porzadkow i bez wartosci eta.
#
# Zdania, ktore moga upasc:
#  (1) podane krawedzie sa dokladnie linkami porzadku, a profile wszystkich osmiu elementow sa rozne;
#  (2) f = p - q + x - y lezy w ker(L - L^T), a nie w ker(C - C^T);
#  (3) slaby separator ("nad x i nad zadnym innym maksymalnym elementem nosnika") istnieje dla linkow i dla C,
#      a mimo to jadro ma wektory nie-blizniacze w obu konstrukcjach (ten sam porzadek);
#  (4) B^T Delta_eta B = Phi - Phi^T dla B = I - eta*Phi, Phi = L oraz Phi = C (tozsamosc w eta, nie probki);
#  (5) f_eta = (I - eta L) f lezy w ker Delta_eta, a dla eta != 0 nie lezy w ker Delta_0;
#  (6) dla h w ker Delta_0: Phi h = Phi^T h (wspolczynnik dopisany przez mase);
#  (7) element dolozony nad S naklada na zaleznosci S jeden warunek linkowy: suma f po jego linkowych poprzednikach;
#  (8) stalosc rzedu nie przenosi sie na podzbiory: to, czy zapis A niesie B, zalezy od a*b.
# Wymaga: sympy.

import sympy as sp

N = ['p', 'q', 'u', 'v', 'x', 'y', 'z', 'w']
ix = {s: i for i, s in enumerate(N)}
n = len(N)
E = [('p', 'u'), ('u', 'x'), ('x', 'z'), ('q', 'v'), ('v', 'y'), ('y', 'w'), ('q', 'z'), ('p', 'w')]


def domkniecie(krawedzie, n):
    C = sp.zeros(n)
    for a, b in krawedzie:
        C[a, b] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if C[i, k] and C[k, j]:
                    C[i, j] = 1
    return C


def linki(C):
    m = C.shape[0]
    L = sp.zeros(m)
    for i in range(m):
        for j in range(m):
            if C[i, j] and not any(C[i, k] and C[k, j] for k in range(m)):
                L[i, j] = 1
    return L


def w_przestrzeni(baza, v):
    if not baza:
        return v == sp.zeros(*v.shape)
    return sp.Matrix.hstack(*baza, v).rank() == len(baza)


C = domkniecie([(ix[a], ix[b]) for a, b in E], n)
L = linki(C)
dane = sp.zeros(n)
for a, b in E:
    dane[ix[a], ix[b]] = 1
wyn = {}
wyn['(1) linki == podane krawedzie'] = (L == dane)
wyn['(1) profile linkowe rozne'] = len({(tuple(L[:, i]), tuple(L[i, :])) for i in range(n)}) == n
wyn['(1) profile porzadku rozne'] = len({(tuple(C[:, i]), tuple(C[i, :])) for i in range(n)}) == n

D_L, D_C = L - L.T, C - C.T
f = sp.Matrix([1, -1, 0, 0, 1, -1, 0, 0])
wyn['(2) Delta_0 f = 0 (linki)'] = (D_L * f == sp.zeros(n, 1))
wyn['(2) (C - C^T) f != 0'] = (D_C * f != sp.zeros(n, 1))
H_L, H_C = D_L.nullspace(), D_C.nullspace()
wyn['(2) dim ker linki = 2, dim ker C = 2'] = (len(H_L) == 2 and len(H_C) == 2)
wyn['(2) jadra rozne'] = not all(w_przestrzeni(H_C, h) for h in H_L)
print('ker(L - L^T):', [list(h) for h in H_L])
print('ker(C - C^T):', [list(h) for h in H_C])


def slabe_separatory(P, g):
    nos = [i for i in range(n) if g[i] != 0]
    maks = [i for i in nos if not any(C[i, t] for t in nos)]
    out = {}
    for s in maks:
        out[N[s]] = [N[j] for j in range(n) if P[s, j] and not any(P[t, j] for t in maks if t != s)]
    return out


g = sp.Matrix([-1, 1, 1, -1, -1, 1, 0, 0])           # wektor z ker(C - C^T) o tym samym nosniku maksymalnym
wyn['(3) g w ker(C - C^T)'] = (D_C * g == sp.zeros(n, 1))
sl_L, sl_C = slabe_separatory(L, f), slabe_separatory(C, g)
print('slabe separatory, linki:', sl_L, ' C:', sl_C)
wyn['(3) slabe separatory istnieja (linki i C)'] = all(sl_L.values()) and all(sl_C.values())

eta = sp.symbols('eta')
I = sp.eye(n)
for nazwa, Phi, D0 in (('L', L, D_L), ('C', C, D_C)):
    B = I - eta * Phi
    R = Phi * B.inv()
    De = R - R.T
    wyn[f'(4) B^T Delta_eta B = Delta_0, Phi = {nazwa}'] = (sp.simplify(B.T * De * B - D0) == sp.zeros(n))
    wyn[f'(4) det B = 1, Phi = {nazwa}'] = (sp.simplify(B.det()) == 1)
    H = D0.nullspace()
    wyn[f'(6) Phi h = Phi^T h na ker, Phi = {nazwa}'] = all(Phi * h == Phi.T * h for h in H)

B = I - eta * L
De = (L * B.inv()) - (L * B.inv()).T
fe = B * f
print('f_eta =', list(fe))
wyn['(5) Delta_eta f_eta = 0'] = (sp.simplify(De * fe) == sp.zeros(n, 1))
wyn['(5) Delta_0 f_eta = eta * (niezerowy wektor)'] = (sp.expand(D_L * fe / eta) != sp.zeros(n, 1))
wyn['(5) L ker nie zawiera sie w ker'] = not all(w_przestrzeni(H_L, L * h) for h in H_L)

# (7) element r nad S; rozne zbiory przeszlosci; warunek nakladany na zaleznosci S (wektory o nosniku w S)
def warunki_po_dolozeniu(przeszlosc_r):
    m = n + 1
    kr = [(ix[a], ix[b]) for a, b in E] + [(ix[s], n) for s in przeszlosc_r]
    C2 = domkniecie(kr, m)
    L2 = linki(C2)
    D2 = L2 - L2.T
    # zaleznosci S po dolozeniu: wektory ker(D2) z zerem na r
    K2 = sp.Matrix.vstack(D2, sp.Matrix([[0] * n + [1]])).nullspace()
    K2 = [k[:n, 0] for k in K2]
    front = [N[j] for j in range(n) if L2[j, n]]
    # przewidywanie: H_L ograniczone warunkiem sum f po froncie = 0
    a = sp.Matrix([[1 if N[j] in front else 0 for j in range(n)]])
    Hm = sp.Matrix.hstack(*H_L)
    pred = [Hm * c for c in (a * Hm).nullspace()]
    zgodne = len(pred) == len(K2) and all(w_przestrzeni(K2, v) for v in pred)
    return front, len(K2), zgodne


for przeszl in (['z', 'w'], ['z'], ['x'], ['x', 'y'], ['u', 'v'], ['p'], ['q', 'y']):
    front, dimk, ok = warunki_po_dolozeniu(przeszl)
    print(f'(7) r nad {przeszl}: linki do {front}, dim zaleznosci S = {dimk}, zgodnie z jednym warunkiem: {ok}')
    wyn[f'(7) jeden warunek, r nad {przeszl}'] = ok

# (8) zapis A niesie B (kryterium 171: rank Delta[:, A u B] = rank Delta[:, A]) zalezy od a*b
def niesie(D, A, Bz):
    ca = [ix[s] for s in A]
    cb = [ix[s] for s in A + Bz]
    return D[:, ca].rank(simplify=True) == D[:, cb].rank(simplify=True)


wyn['(8) bez masy {p,q,x} niesie y; przy a*b != 0 nie, a {p,q,x,u,v} tak'] = (
    niesie(D_L, ['p', 'q', 'x'], ['y']) and not niesie(De, ['p', 'q', 'x'], ['y'])
    and niesie(De, ['p', 'q', 'x', 'u', 'v'], ['y']))

print()
for k, v in wyn.items():
    print(('OK  ' if v else 'UPADLO  ') + k)
print('\nwszystko:', all(wyn.values()))
