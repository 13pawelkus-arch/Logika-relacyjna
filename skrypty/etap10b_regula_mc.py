"""
Kontrola PO FAKCIE do etap10 (P1 upadlo dla eps=0,2, na granicy dla 0,1).
Hipoteza [A], wypowiedziana po zobaczeniu wyniku: odchylka pochodzi z samej reguly, nie ze struktury.
Nadwyzka = tref*tk*(cosh d_eta - 1)/(tref+tk) + ... zalezy tez od tk, wiec regula nie bierze
dokladnie najblizszego w pchnieciu, tylko wymienia pchniecie na krotszy krok.
Test: proces Poissona kandydatow w pasmie o mierze rho*tau*dtau*deta, wybor DOKLADNA nadwyzka,
bez zadnej przestrzeni. Jesli std*4sqrt2*eps*n z tego rachunku = wartosci z etap10 (1,05 / 1,11 / 1,4-1,6),
to odchylka jest wlasnoscia reguly (wyboru, ktory ustawilem sam), a nie struktury.
"""
import numpy as np
rng = np.random.default_rng(3)
def jeden(eps, n, M=20000, W=4.0):
    lam = 4*eps*n                                     # na jednostke pchniecia
    out = []
    for _ in range(M):
        k = rng.poisson(lam*2*W)
        if k == 0: continue
        eta = rng.uniform(-W, W, k)
        # tau o gestosci ~ tau na [1-eps, 1+eps]
        a, b = (1-eps)**2, (1+eps)**2
        tk = np.sqrt(rng.uniform(a, b, k))
        tref = 1.0
        tpc = np.sqrt(tref**2 + tk**2 + 2*tref*tk*np.cosh(eta))
        j = np.argmin(tpc - tref - tk)
        out.append(eta[j])
    return np.std(out)
print(" eps    n  | std*4sqrt2*eps*n (sama regula) | najblizszy w pchnieciu (idealnie 1)")
for eps in (0.05, 0.10, 0.20):
    for n in (15, 150):
        s = jeden(eps, n)
        print(f" {eps:.2f} {n:4d} | {s*4*np.sqrt(2)*eps*n:.3f}")
