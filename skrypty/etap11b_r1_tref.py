"""
Kontrola PO FAKCIE do etap11: r1 (korelacja kolejnych |skokow pchniecia|) wyszla +0,02 / +0,07 / +0,21
dla eps = 0,05 / 0,1 / 0,2, niezaleznie od n. Nie bylo zdania przed przebiegiem.
Hipoteza [A] (po fakcie): r1 pochodzi z dziedziczenia tref — pasmo liczone wzgledem poprzedniego
kroku, wiec dwa kolejne skoki losuja przy podobnym tref (a gestosc kandydatow ~ tref^4).
Test: ta sama redukcja lokalna co etap10c, ale z lancuchem tref jak w etap11
(krok 0 w pasmie wokol tau0, potem 3 kroki pamieci). Jesli r1 z MC = r1 z GPU -> w pelni wyjasnione
przez regule, bez korelacji ze wspolnych punktow sprinklingu. Druga kolumna: r1 po normowaniu lokalnym
(powinno ~0, jesli wyjasnienie jest pelne).
"""
import numpy as np
from math import gamma, pi
rng = np.random.default_rng(11)
def lancuch(eps, n, K=20000, L=5):
    rho = 24*n/pi
    def losuj(tref):
        lam3 = rho*tref**4*((1+eps)**4-(1-eps)**4)/4
        s = ((4*pi/3)*lam3)**(-1/3); W = 6*s
        VW = 4*pi*(np.sinh(2*W)/4 - W/2); k = max(1, rng.poisson(lam3*VW))
        r = np.empty(0)
        while len(r) < k:
            c = rng.uniform(0, W, 3*k); a = rng.uniform(0, np.sinh(W)**2, 3*k); r = np.concatenate([r, c[a < np.sinh(c)**2]])
        r = r[:k]; tk = tref*rng.uniform((1-eps)**4, (1+eps)**4, k)**0.25
        tpc = np.sqrt(tref**2 + tk**2 + 2*tref*tk*np.cosh(r)); j = np.argmin(tpc - tref - tk)
        return r[j], tk[j], s*np.sqrt(gamma(5/3))
    R = np.zeros((K, L-2)); Z = np.zeros((K, L-2))
    for k in range(K):
        tref = 1.0*rng.uniform((1-eps)**4, (1+eps)**4)**0.25      # krok 0: tk w pasmie wokol tau0
        for i in range(L-2):
            r, tk, pred = losuj(tref); R[k, i] = r; Z[k, i] = r/pred; tref = tk
    c = lambda A: np.corrcoef(A[:, :-1].ravel(), A[:, 1:].ravel())[0, 1]
    return c(R), c(Z)
gpu = {0.05: 0.024, 0.10: 0.070, 0.20: 0.211}                        # srednie po n z etap11
print(" eps  | r1 MC (surowe) | r1 GPU (sr. po n) | r1 MC znormowane lokalnie")
for eps in (0.05, 0.10, 0.20):
    a, b = lancuch(eps, 100)
    print(f" {eps:.2f} | {a:+.3f}         | {gpu[eps]:+.3f}            | {b:+.3f}")
