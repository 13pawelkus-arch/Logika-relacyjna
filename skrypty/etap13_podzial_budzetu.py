"""
CO USTALA PODZIAL BUDZETU n MIEDZY MASE A RAME (§F2, po etap12).

Z etap12: ostrosc tempa sigma_t = eps/sqrt3 (na krok), ostrosc ramy: 1+1 d_eta = 1/(4 sqrt2 eps n),
3+1 rms = sqrt(G(5/3)) ((4pi/3) lam3)^(-1/3), lam3 ~ 2 eps rho tau^4.

B1 [A], rachunek (nie test): suma bitow tempa i ramy NIE zalezy od eps:
     1+1: ln(1/sigma_t) + ln(R/d_eta) = ln(4 sqrt6 R n);  3+1 analogicznie (ramy ~ 1/rms^3 ~ eps n).
     -> zadna zasada "maksimum informacji" nie wybiera eps. Podzial jest zdegenerowany informacyjnie.
KANDYDAT [A][?] (hipoteza, nie wynik): wybor przez TRWALOSC. Tempo bladzi: var(ln tref) rosnie o eps^2/3
     na krok -> tozsamosc masy trwa L_t = 3/eps^2 krokow. Rama bladzi: L_f = 1/rms^2 krokow.
     L_t maleje z eps, L_f rosnie -> maksimum min(L_t, L_f) przy L_t = L_f:
       1+1: eps* = (3/32)^(1/4) n^(-1/2) = 0,553 n^(-1/2)  ->  eps* tau = 0,782 rho^(-1/2)
       3+1: eps*^(8/3) = 3 G(5/3) (8 pi rho tau^4/3)^(-2/3) -> eps* tau = 0,854 rho^(-1/4)
     Odczyt: przy zrownowazonym podziale bezwzgledna ostrosc tykniecia = skala dyskretnosci, niezaleznie
     od masy i wymiaru. (Tylko jesli kryterium trwalosci zostanie przyjete.)

ZDANIA DO UPADKU (dotycza zalozen kandydata, nie samego kryterium):
  B2. brak dryfu ln tref: |dryf na krok| * L_t < 0,2
  B3. var(ln tref) liniowe w krokach, nachylenie = eps^2/3 +-10%   (L_t = 3/eps^2)
  B4. kumulowane pchniecie ramy: <r_L^2> = L * rms^2 +-10%          (L_f = 1/rms^2)
  B5. L_t/L_f = 1 +-0,2 przy eps*, 16 +-25% przy eps*/2, 1/16 +-25% przy 2 eps*
Redukcja lokalna (potwierdzona w etap10/11), n = 200, K = 400 lancuchow, L = 1500 krokow.
"""
import numpy as np
from math import gamma, pi
rng = np.random.default_rng(13)
N_EL, K, L = 200, 400, 1500

def lancuchy(eps, d):
    tref = np.ones(K); lt = np.zeros((K, L)); cum = np.zeros((K, L))
    if d == 2: eta = np.zeros(K)
    else:
        u = np.tile([1., 0, 0, 0], (K, 1)); u0 = u.copy()
    for s in range(L):
        if d == 2:
            rho = 2*N_EL; lam = rho*tref**2*((1+eps)**2-(1-eps)**2)/2; pred = 1/(np.sqrt(2)*lam)
            W = 10*pred; M = int(np.max(lam*2*W)*1.5 + 30)
            k = rng.poisson(lam*2*W); msk = np.arange(M)[None, :] < k[:, None]
            r = rng.uniform(-1, 1, (K, M))*W[:, None]
            tk = tref[:, None]*np.sqrt(rng.uniform((1-eps)**2, (1+eps)**2, (K, M)))
        else:
            rho = 24*N_EL/pi; lam = rho*tref**4*((1+eps)**4-(1-eps)**4)/4
            pred = np.sqrt(gamma(5/3))*((4*pi/3)*lam)**(-1/3); W = 6*pred/np.sqrt(gamma(5/3))
            VW = 4*pi*(np.sinh(2*W)/4 - W/2); M = int(np.max(lam*VW)*1.5 + 30)
            k = rng.poisson(lam*VW); msk = np.arange(M)[None, :] < k[:, None]
            r = W[:, None]*rng.random((K, M))**(1/3)                      # male r: sinh^2 r ~ r^2 (W << 1)
            tk = tref[:, None]*rng.uniform((1-eps)**4, (1+eps)**4, (K, M))**0.25
        tpc = np.sqrt(tref[:, None]**2 + tk**2 + 2*tref[:, None]*tk*np.cosh(r))
        j = np.argmin(np.where(msk, tpc - tref[:, None] - tk, np.inf), 1); a = np.arange(K)
        rr, tref = r[a, j], tk[a, j]
        lt[:, s] = np.log(tref)
        if d == 2:
            eta = eta + rr; cum[:, s] = eta**2
        else:
            nh = rng.normal(size=(K, 3)); nh /= np.linalg.norm(nh, axis=1)[:, None]
            loc = np.concatenate([np.cosh(rr)[:, None], np.sinh(rr)[:, None]*nh], 1)   # w ukladzie spoczynkowym u
            # boost z ukladu spoczynkowego do u: Lambda(u) loc
            ud = (bv*loc[:, 1:]).sum(1)
            t_new = g*loc[:, 0] + ud
            x_new = loc[:, 1:] + bv*(loc[:, 0][:, None] + ud[:, None]/(1+g)[:, None])
            u = np.concatenate([t_new[:, None], x_new], 1)
            cum[:, s] = np.arccosh(np.maximum(u[:, 0], 1.0))**2          # u0 = (1,0,0,0)
    return lt, cum

def nachylenie(y):  # var lub srednia kwadratu vs krok, fit liniowy przez 0 na calym zakresie
    x = np.arange(1, L+1); return (x*y).sum()/(x*x).sum()

for d in (2, 4):
    if d == 2:
        es = (3/32)**0.25/np.sqrt(N_EL); rf = lambda e: 1/(4*np.sqrt(2)*e*N_EL)
    else:
        lam = lambda e: (24*N_EL/pi)*((1+e)**4-(1-e)**4)/4
        rf = lambda e: np.sqrt(gamma(5/3))*((4*pi/3)*lam(e))**(-1/3)
        from scipy.optimize import brentq
        es = brentq(lambda e: e**2/3 - rf(e)**2, 1e-4, 0.5)
    print(f"\n=== d = {'1+1' if d == 2 else '3+1'}, n = {N_EL}, eps* = {es:.4f} ===")
    print(" eps     | B2 dryf*L_t | B3 nachyl/(eps^2/3) | B4 nachyl/rms^2 | L_t    | L_f    | B5 L_t/L_f | przewid.")
    for f, pr in ((0.5, 16), (1.0, 1), (2.0, 1/16)):
        e = es*f; lt, cum = lancuchy(e, d)
        v = lt.var(0); drift = np.polyfit(np.arange(1, L+1), lt.mean(0), 1)[0]
        s3 = nachylenie(v); s4 = nachylenie(cum.mean(0))
        Lt, Lf = 1/s3, 1/s4
        print(f" {e:.5f} | {abs(drift)*3/e**2:+.3f}      | {s3/(e**2/3):.3f}               | {s4/rf(e)**2:.3f}           | {Lt:6.0f} | {Lf:6.0f} | {Lt/Lf:.3f}      | {pr:.3f}")
