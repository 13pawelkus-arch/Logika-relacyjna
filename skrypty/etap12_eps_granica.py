"""
SKAN eps -> 0: czy eps jest regularyzacja (jak warstwa Delta u Fokkera, C4a.14-15), czy niesie skale.
Pytanie [H] (uzytkownik): jesli stala ma skonczona granice przy eps -> 0, eps to tylko regularyzacja
i pytanie "skad eps" znika; jesli nie ma, eps niesie prawdziwa skale.

Redukcja lokalna (potwierdzona pelnym sprinklingiem: etap10 w 1+1, etap11 w 3+1), z lancuchem tref
jak w etap11 (krok 0 w pasmie wokol tau0 = 1, potem 3 kroki pamieci, pasmo wzgledem poprzedniego kroku).
n = 2000 staly (lam = 4*eps*n >= 40 nawet przy eps = 0,005). eps: 0,2 ... 0,005 (1,6 dekady).

ZDANIA DO UPADKU (przed rachunkiem):
  E1. Przy stalym n stala NIE ma granicy: std(d_eta) ~ eps^(-1,00 +- 0,02) w 1+1,
      rms(r) ~ eps^(-0,333 +- 0,01) w 3+1. (Wyprowadzenie: eps wchodzi tylko przez lam = eps*n.)
  E2. Kombinacja bez eps ma granice: surowy wspolczynnik (bez lokalnego normowania) -> 1,
      odchylka od 1 przy eps <= 0,01 mniejsza niz 1% (artefakt tref znika jak Delta u Fokkera).
  E3. r1 (korelacja kolejnych |skokow|) -> 0: przy eps <= 0,02 |r1| < 0,01.
  E4. Rozdzielczosc tykniecia sigma(tk/tref) = eps/sqrt3 (1+1, gestosc ~tau w pasmie ~ plaska),
      wiec iloczyn sigma(tk/tref) * std(d_eta) * n = 1/(4*sqrt6) = 0,1021 +- 5%, NIEZALEZNIE od eps.
      Odczyt [A][?]: trajektoria nie wyostrzy naraz tempa i ramy — iloczyn ustala samo n.
      (Uwaga: wyglada jak relacja nieoznacznosci — nazwa to pulapka; to zdanie o liczbie kandydatow.)
"""
import numpy as np
from math import gamma, pi
rng = np.random.default_rng(12)
N_EL = 2000
EPSS = [0.2, 0.1, 0.05, 0.02, 0.01, 0.005]
K    = 20000

def krok(tref, eps, d):
    """jeden krok reguly w lokalnym ukladzie; zwraca (skok pchniecia, tk, przewidywanie lokalne)"""
    if d == 2:
        rho = 2*N_EL
        lam = rho*tref**2*((1+eps)**2-(1-eps)**2)/2                   # na jednostke pchniecia
        pred = 1/(np.sqrt(2)*lam)                                     # std(d_eta) = sqrt2/(2 lam)
        W = 10*pred; k = max(1, rng.poisson(lam*2*W))
        r = rng.uniform(-W, W, k)
        tk = tref*np.sqrt(rng.uniform((1-eps)**2, (1+eps)**2, k))    # gestosc ~ tau
    else:
        rho = 24*N_EL/pi
        lam = rho*tref**4*((1+eps)**4-(1-eps)**4)/4
        pred = np.sqrt(gamma(5/3))*((4*pi/3)*lam)**(-1/3)
        W = 6*pred/np.sqrt(gamma(5/3)); VW = 4*pi*(np.sinh(2*W)/4 - W/2); k = max(1, rng.poisson(lam*VW))
        r = np.empty(0)
        while len(r) < k:
            c = rng.uniform(0, W, 3*k); a = rng.uniform(0, np.sinh(W)**2, 3*k); r = np.concatenate([r, c[a < np.sinh(c)**2]])
        r = r[:k]; tk = tref*rng.uniform((1-eps)**4, (1+eps)**4, k)**0.25   # gestosc ~ tau^3
    tpc = np.sqrt(tref**2 + tk**2 + 2*tref*tk*np.cosh(r))
    j = np.argmin(tpc - tref - tk)
    return r[j], tk[j], pred

def przebieg(eps, d):
    R = np.zeros((K, 3)); Z = np.zeros((K, 3)); Q = np.zeros((K, 3))
    for k in range(K):
        e = 2 if d == 2 else 4
        tref = rng.uniform((1-eps)**e, (1+eps)**e)**(1/e)            # krok 0
        for i in range(3):
            r, tk, pred = krok(tref, eps, d); R[k, i] = r; Z[k, i] = r/pred; Q[k, i] = tk/tref; tref = tk
    c = lambda A: np.corrcoef(A[:, :-1].ravel(), A[:, 1:].ravel())[0, 1]
    if d == 2:
        sd = R.std(); nom = 1/(4*np.sqrt(2)*eps*N_EL)
        return dict(skok=sd, surowy=sd/nom, lokalny=Z.std(), r1=c(np.abs(R)), sq=Q.std(), E4=Q.std()*sd*N_EL)
    rms = np.sqrt((R**2).mean()); nom = np.sqrt(gamma(5/3))*((4*pi/3)*(24*N_EL/pi)*((1+eps)**4-(1-eps)**4)/4)**(-1/3)
    return dict(skok=rms, surowy=rms/nom, lokalny=np.sqrt((Z**2).mean()), r1=c(R), sq=Q.std())

for d in (2, 4):
    print(f"\n=== d = {'1+1' if d == 2 else '3+1'}, n = {N_EL}, K = {K} x 3 przyrosty ===")
    print(" eps    | skok      | surowy/wzor | lokalny/wzor | r1      | sigma(tk/tref) | eps/sqrt3" + (" | E4 iloczyn" if d == 2 else ""))
    W = []
    for eps in EPSS:
        w = przebieg(eps, d); W.append(w)
        print(f" {eps:.3f}  | {w['skok']:.6f}  | {w['surowy']:.4f}      | {w['lokalny']:.4f}       | {w['r1']:+.4f} | {w['sq']:.5f}        | {eps/np.sqrt(3):.5f}"
              + (f"   | {w['E4']:.4f}" if d == 2 else ""))
    pot = np.polyfit(np.log(EPSS), np.log([w['skok'] for w in W]), 1)[0]
    print(f" E1: wykladnik skoku wobec eps = {pot:+.4f}  (przewidywane {'-1,00' if d == 2 else '-0,333'})")
