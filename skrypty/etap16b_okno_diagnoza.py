"""
Diagnoza PO FAKCIE do etap16 (F1, F3 upadly; F2 upadlo dla B; F4 przeszlo).
Hipoteza [A]: przy gestosci z etap8 tykniecie miesci n_A ~ 0,3 i n_B ~ 1,5 elementu, wiec skok pchniecia
na krok jest duzy (r ~ 0,5-0,8), a najblizszy w pchnieciu kandydat czesto lezy POZA oknem kandydatow
(dt < 3h w czasie pudla, zasieg komorek >= 2h w kazdej osi przestrzennej). Okno odcina dluzsze kroki
przy duzym pchnieciu wzgledem pudla -> skraca tykniecie, silniej dla szybkich i dla rzadszego A.
Test: redukcja lokalna BEZ okna (pelna przestrzen pchniec) -> ulamek wybranych krokow, ktore wypadlyby
poza okno etap16, osobno dla A/B i wolnych/szybkich. Jesli ulamek jest rzedu procentow -> wyjasnia.
"""
import numpy as np
from math import pi
rng = np.random.default_rng(16)
h = 0.359; rho = 5489.0; EPS = 0.10; DELTA = -(EPS/np.tanh(4*EPS) - 0.25)
def boost(u, loc0, loc):
    g = u[:, 0]; bv = u[:, 1:]; ud = (bv*loc).sum(1)
    return np.concatenate([(g*loc0 + ud)[:, None], loc + bv*(loc0[:, None] + ud[:, None]/(1+g)[:, None])], 1)
for nazwa, ts in (("A", 0.4), ("B", 0.6)):
    tau = ts*h; n = rho*pi*tau**4/24; lam3 = rho*tau**4*(np.exp(4*(DELTA+EPS)) - np.exp(4*(DELTA-EPS)))/4
    K = 20000; v = rng.uniform(0.02, 0.9, K); g = 1/np.sqrt(1-v**2)
    d = rng.normal(size=(K, 3)); d /= np.linalg.norm(d, axis=1)[:, None]
    u = np.concatenate([g[:, None], (g*v)[:, None]*d], 1)
    W = 4.0; VW = 4*pi*(np.sinh(2*W)/4 - W/2); out = np.zeros(K, bool); rs = np.zeros(K)
    for k in range(K):
        m = max(1, rng.poisson(lam3*VW))
        r = np.empty(0)
        while len(r) < m:
            c = rng.uniform(0, W, 3*m); a = rng.uniform(0, np.sinh(W)**2, 3*m); r = np.concatenate([r, c[a < np.sinh(c)**2]])
        j = np.argmin(r[:m]); rr = r[j]; rs[k] = rr
        tk = tau*np.exp(np.log(rng.uniform(np.exp(4*(DELTA-EPS)), np.exp(4*(DELTA+EPS))))/4)
        nh = rng.normal(size=3); nh /= np.linalg.norm(nh)
        un = boost(u[k:k+1], np.array([np.cosh(rr)]), (np.sinh(rr)*nh)[None, :])[0]
        dt, dx = tk*un[0], tk*un[1:]
        out[k] = (dt > 3*h) or (np.abs(dx).max() > 2*h)
    wol, szy = v < 0.3, v > 0.6
    print(f"{nazwa}: n = {n:.3f} el./tykn. | rms r = {np.sqrt((rs**2).mean()):.3f} | poza oknem: wszystkie {out.mean():.3%}, "
          f"wolne (v<0,3) {out[wol].mean():.3%}, szybkie (v>0,6) {out[szy].mean():.3%}")

# CZESC 2 (dopisana po wyniku czesci 1, ktory hipoteze odrzucil dla pierwszego kroku):
# cale lancuchy 19 krokow w redukcji lokalnej bez okna; pchniecie bladzi, wiec pozniejsze kroki sa szybsze.
print("\nCzesc 2: lancuchy 19 krokow bez okna (K = 3000)")
for nazwa, ts in (("A", 0.4), ("B", 0.6)):
    tau0 = ts*h; K = 3000; v = rng.uniform(0.02, 0.8, K); g = 1/np.sqrt(1-v**2)
    d = rng.normal(size=(K, 3)); d /= np.linalg.norm(d, axis=1)[:, None]
    u = np.concatenate([g[:, None], (g*v)[:, None]*d], 1); tref = np.full(K, tau0)
    poza = np.zeros((K, 18), bool); W = 4.0; VW = 4*pi*(np.sinh(2*W)/4 - W/2); X = np.zeros((K, 4))
    for s in range(18):
        for k in range(K):
            lam3 = rho*tref[k]**4*(np.exp(4*(DELTA+EPS)) - np.exp(4*(DELTA-EPS)))/4
            m = max(1, rng.poisson(lam3*VW)); r = np.empty(0)
            while len(r) < m:
                c = rng.uniform(0, W, 3*m); a = rng.uniform(0, np.sinh(W)**2, 3*m); r = np.concatenate([r, c[a < np.sinh(c)**2]])
            rr = r[:m].min(); tk = tref[k]*np.exp(np.log(rng.uniform(np.exp(4*(DELTA-EPS)), np.exp(4*(DELTA+EPS))))/4)
            nh = rng.normal(size=3); nh /= np.linalg.norm(nh)
            u[k] = boost(u[k:k+1], np.array([np.cosh(rr)]), (np.sinh(rr)*nh)[None, :])[0]
            dt, dx = tk*u[k, 0], tk*u[k, 1:]; X[k] += np.concatenate([[dt], dx])
            poza[k, s] = (dt > 3*h) or (np.abs(dx).max() > 2*h); tref[k] = tk
    vk = np.linalg.norm(X[:, 1:], axis=1)/X[:, 0]
    print(f"{nazwa}: poza oknem na krokach 1-6 / 7-12 / 13-18: {poza[:, :6].mean():.1%} / {poza[:, 6:12].mean():.1%} / {poza[:, 12:].mean():.1%} | "
          f"lancuchy z >=1 krokiem poza: {poza.any(1).mean():.1%} | v koncowe (koniec-poczatek): mediana {np.median(vk):.2f}, 95% {np.quantile(vk, 0.95):.3f}")
