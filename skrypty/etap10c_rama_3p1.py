"""
MOST PRZEZ RAME w 3+1 — CPU, bez pudla.
Uzasadnienie redukcji: regula patrzy tylko na pasmo [tref(1-eps), tref(1+eps)] wokol konca trajektorii;
pasma kolejnych krokow sa rozlaczne (punkty pasma nowego kroku leza ~2tau od poprzedniego elementu),
a sprinkling Poissona jest niezalezny na rozlacznych obszarach i niezmienniczy wzgledem pchniec.
Wiec kazdy krok = niezalezne losowanie kandydatow w lokalnym ukladzie poprzedniego kroku.
W 1+1 ta redukcja zgodzila sie z pelnym przebiegiem (etap10 po lokalnym normowaniu: 1,00-1,03).

Miara kandydatow: rho * tau^3 dtau * sinh^2(r) dr dOmega  (r = wzgledne pchniecie).
Najblizszy w H^3: P(r>R) = exp(-(4pi/3) lam3 R^3), lam3 = rho*tref^4*((1+eps)^4-(1-eps)^4)/4
  -> rms(r) = sqrt(Gamma(5/3)) * ((4pi/3) lam3)^(-1/3),   n = rho*pi*tref^4/24.
ZDANIA DO UPADKU (zapisane przed rachunkiem, §F2):
  Q1. wykladnik rms(r) wobec n = -0,33 +- 0,03
  Q2. rms(r) / wzor = 1,00 +- 0,05
  MOST: liczba ram ~ 1/r^3 ~ n  -> wspolczynnik przy ln n = 1 (jak w 1+1).
"""
import numpy as np
from math import gamma, pi
rng = np.random.default_rng(5)
def krok(eps, n, M=20000):
    rho = 24*n/pi                                   # tref = 1
    lam3 = rho*((1+eps)**4-(1-eps)**4)/4
    pred = np.sqrt(gamma(5/3))*((4*pi/3)*lam3)**(-1/3)
    W = 8*pred
    VW = 4*pi*(np.sinh(2*W)/4 - W/2)               # objetosc kuli o promieniu W w H^3
    out = np.empty(M)
    for m in range(M):
        k = rng.poisson(lam3*VW)
        while k == 0: k = rng.poisson(lam3*VW)
        # r z gestoscia ~ sinh^2 r na [0,W] (odrzucanie)
        r = np.empty(0)
        while len(r) < k:
            c = rng.uniform(0, W, 3*k); a = rng.uniform(0, np.sinh(W)**2, 3*k)
            r = np.concatenate([r, c[a < np.sinh(c)**2]])
        r = r[:k]
        tk = rng.uniform((1-eps)**4, (1+eps)**4, k)**0.25       # gestosc ~ tau^3
        tpc = np.sqrt(1 + tk**2 + 2*tk*np.cosh(r))
        out[m] = r[np.argmin(tpc - 1 - tk)]
    return np.sqrt((out**2).mean()), pred
NS = [3, 10, 30, 100, 300, 1000, 3000]
print(" eps     n  | rms(r)    | wzor      | Q2 stosunek")
for eps in (0.05, 0.10, 0.20):
    xs, ys = [], []
    for n in NS:
        s, p = krok(eps, n)
        print(f" {eps:.2f} {n:5d} | {s:.5f}  | {p:.5f}  | {s/p:.3f}")
        xs.append(np.log(n)); ys.append(np.log(s))
    print(f"   Q1 eps={eps}: wykladnik = {np.polyfit(xs, ys, 1)[0]:+.4f}  (przewidywane -0,333)\n")
