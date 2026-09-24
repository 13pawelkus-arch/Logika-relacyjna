"""
PASMO BEZ DRYFU TEMPA + ponowny test podzialu budzetu (po etap13).

Problem (etap13): pasmo [tref(1-eps), tref(1+eps)] + wybor najmniejszej nadwyzki -> dryf ln tref ~ eps^2
(miara kandydatow rho tau^(d-1) dtau woli dluzsze kroki, nadwyzka woli krotsze; netto dodatni).
Ograniczenie: pamiec musi zostac JEDNOKROKOWA (pasmo wzgledem tau0 wymuszaloby A/B = 1,5, §F1 v3).

REGULA R-KAT [A] (wybor konstrukcji, wyprowadzony, nie dopasowany):
  (1) prostota = najmniejsze WZGLEDNE PCHNIECIE r miedzy krokami (cosh r = (tpc^2 - tref^2 - tk^2)/(2 tref tk),
      same czasy wlasne = objetosci przedzialow). Nie zalezy od dlugosci kroku -> wybor nie faworyzuje tk.
  (2) pasmo logarytmiczne s = ln(tk/tref) w [delta-eps, delta+eps]; kandydaci maja gestosc ~ e^(d s), wiec
      E[s] = delta + eps*coth(d*eps) - 1/d  ->  delta = -(eps*coth(d*eps) - 1/d)  daje E[s] = 0 DOKLADNIE.
  Poniewaz r i tk sa niezalezne w mierze Poissona, wybrany tk ma rozklad samej miary pasma.

ZDANIA DO UPADKU:
  D1. dryf ln tref: |dryf na krok| * L_t < 0,05   (etap13: 0,20-0,31 w 1+1, 1,7-2,3 w 3+1)
  D2. nachylenie var(ln tref) = var_s (wariancja uc. wykladniczego rozkladu na [delta-eps, delta+eps]) +-5%
  D3. rms skoku pchniecia przy wyborze najmniejszego r = wzor z lam pasma logarytmicznego +-3%
  Podzial budzetu (kandydat "trwalosc", hipoteza [A]): L_t = 1/var_s, L_f = 1/rms^2, eps* z L_t = L_f.
  B5'. L_t/L_f (nachylenia z okna L <= L_t(eps*)/4) = 1 +-0,2 przy eps*, 16 +-25% przy eps*/2, 1/16 +-25% przy 2eps*
Redukcja lokalna (etap10/11), n = 200, K = 400.
"""
import numpy as np
from math import gamma, pi
from scipy.optimize import brentq
rng = np.random.default_rng(15)
N_EL, K = 200, 4000

def delta(eps, d): return -(eps/np.tanh(d*eps) - 1/d)
def var_s(eps, d):
    x = np.linspace(-eps, eps, 20001); w = np.exp(d*x); m = (x*w).sum()/w.sum(); return ((x-m)**2*w).sum()/w.sum()
def lam(eps, d, tref=1.0):
    de = delta(eps, d)
    if d == 2: return 2*N_EL*tref**2*(np.exp(2*(de+eps)) - np.exp(2*(de-eps)))/2      # na jednostke pchniecia
    return (24*N_EL/pi)*tref**4*(np.exp(4*(de+eps)) - np.exp(4*(de-eps)))/4          # na jednostke objetosci H^3
def rms_wz(eps, d, tref=1.0):
    l = lam(eps, d, tref)
    return 1/(np.sqrt(2)*l) if d == 2 else np.sqrt(gamma(5/3))*((4*pi/3)*l)**(-1/3)
def losuj_s(eps, d, size):
    de = delta(eps, d); a, b = np.exp(d*(de-eps)), np.exp(d*(de+eps))
    return np.log(rng.uniform(a, b, size))/d                                          # gestosc ~ e^(d s)

def lancuchy(eps, d, L):
    tref = np.ones(K); lt = np.zeros((K, L)); cum = np.zeros((K, L)); step = np.zeros((K, L))
    eta = np.zeros(K); u = np.tile([1., 0, 0, 0], (K, 1))
    for s in range(L):
        l = lam(eps, d, tref); pr = rms_wz(eps, d, tref)
        if d == 2:
            W = np.minimum(10*pr, 50.0); k = np.maximum(1, rng.poisson(l*2*W)); M = int(k.max())
            r = rng.uniform(-1, 1, (K, M))*W[:, None]; key = np.abs(r)
        else:
            W = np.minimum(6*pr/np.sqrt(gamma(5/3)), 3.0); VW = 4*pi*(np.sinh(2*W)/4 - W/2); k = np.maximum(1, rng.poisson(l*VW)); M = int(k.max())
            r = np.empty((K, M)); fill = np.zeros((K, M), bool)
            while not fill.all():                                                      # odrzucanie: gestosc ~ sinh^2 r
                c = rng.random((K, M))*W[:, None]; a = rng.random((K, M))*np.sinh(W)[:, None]**2
                ok = (a < np.sinh(c)**2) & ~fill; r[ok] = c[ok]; fill |= ok
            key = r
        msk = np.arange(M)[None, :] < k[:, None]
        j = np.argmin(np.where(msk, key, np.inf), 1); a_ = np.arange(K); rr = r[a_, j]
        tref = tref*np.exp(losuj_s(eps, d, K))                                          # tk niezalezny od r (R-KAT)
        lt[:, s] = np.log(tref); step[:, s] = rr/pr
        if d == 2: eta = eta + rr; cum[:, s] = eta**2
        else:
            nh = rng.normal(size=(K, 3)); nh /= np.linalg.norm(nh, axis=1)[:, None]
            loc0, loc = np.cosh(rr), np.sinh(rr)[:, None]*nh
            g = u[:, 0]; bv = u[:, 1:]; ud = (bv*loc).sum(1)
            u = np.concatenate([(g*loc0 + ud)[:, None], loc + bv*(loc0[:, None] + ud[:, None]/(1+g)[:, None])], 1)
            cum[:, s] = np.arccosh(np.maximum(u[:, 0], 1.0))**2
    return lt, cum, step

# v2 (po awarii pamieci i przegladzie wlasnych kryteriow, PRZED ponownym przebiegiem):
#  - D1 mierzony osobno: K_D = 4000 lancuchow x 40 krokow, dryf porownany z szumem (z = dryf/blad) i z etap13
#  - D3 ze WSZYSTKICH krokow (kazdy znormowany wzorem przy wlasnym tref), nie z pierwszego
#  - B5' WYCOFANE PO czesciowym przebiegu v1 (1+1: L_t/L_f = 21 / 2,2 / 2,6; 3+1: 6,1 / 1,6; potem awaria pamieci),
#    wiec upadlo, a wycofanie jest diagnoza PO FAKCIE: ostrosc ramy zalezy od biezacego tref (n_ef = n tref^d), a porownanie
#    L_t z L_f wymaga umownej jednostki (e-krotnosc tykniecia vs jednostka pchniecia) -> stala eps* umowna.
#    Zostaje skalowanie (niezalezne od umowy): L_t ~ eps^-2 (D1, D2) i L_f ~ (eps n)^(2/(d-1)) (etap10-12)
#    => eps* tau ~ rho^(-1/d) przy KAZDEJ umowie.
print(" d   | eps   | D1 dryf/krok | blad    | z     | dryf/eps^2 (etap13: 1+1 ~0,08, 3+1 ~0,57) | D2 nach/var_s | D3 rms/wzor (wszystkie kroki)")
for d in (2, 4):
    for e in (0.05, 0.1, 0.2):
        K = 4000; lt, cum, st = lancuchy(e, d, 40)
        inc = np.diff(np.concatenate([np.zeros((K, 1)), lt], 1), axis=1)
        dr = inc.mean(); err = inc.mean(1).std()/np.sqrt(K)
        v = lt.var(0); x = np.arange(1, 41); sl = (x*v).sum()/(x*x).sum()
        d3 = st.std() if d == 2 else np.sqrt((st**2).mean())
        print(f" {d}   | {e:.2f}  | {dr:+.6f}    | {err:.6f} | {dr/err:+.2f} | {dr/e**2:+.4f}                                   | {sl/var_s(e, d):.3f}         | {d3:.4f}")
