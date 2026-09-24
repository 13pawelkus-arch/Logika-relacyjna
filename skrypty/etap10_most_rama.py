"""
MOST MASA <-> LOGARYTMY PRZEZ RAME (§F1/§F2), d = 1+1, CPU.

Po co: §F2 pokazal, ze ln N = koszt wskazania RAMY (pchniecia) z rozdzielczoscia dyskretnosci.
Trajektoria masywna niesie wlasna rame (pchniecie eta kolejnych krokow). Pytanie: z jaka
rozdzielczoscia trajektoria sama wyznacza swoja rame, i czy ta rozdzielczosc zalezy od
liczby elementow na tykniecie n = rho*tau^2/2 (w 1+1 objetosc przedzialu o czasie wlasnym tau).

Regula: jak etap8/9 (pasmo +-eps wzgledem poprzedniego kroku; kontynuacja = najmniejsza nadwyzka
z odwrotnej nierownosci trojkata tau(p,c) - tau(p,tip) - tau(tip,c)).

WYPROWADZENIE PRZED RACHUNKIEM [A]:
  W pasmie [tau(1-eps), tau(1+eps)] miara elementow w (tau, eta) to rho*tau*dtau*deta, wiec
  kandydaci w pchnieciu tworza proces Poissona o gestosci  lam = 2*eps*rho*tau^2 = 4*eps*n.
  Nadwyzka rosnie monotonicznie z |d_eta|, wiec regula bierze kandydata najblizszego w pchnieciu.
  Odleglosc najblizszego z dwoch stron ~ Exp(2*lam)  ->  std(d_eta) = sqrt(2)/(2*lam) = 1/(4*sqrt(2)*eps*n).

ZDANIA DO UPADKU:
  P1. std(d_eta) * 4*sqrt(2)*eps*n = 1,00 +- 0,10  dla kazdego n i eps (gdzie lam*zakres >> 1)
  P2. wykladnik std(d_eta) wobec n = -1,00 +- 0,05 (Poisson/dyfuzja dalaby -0,5)
  P3. przyrosty d_eta nieskorelowane (autokorelacja z krokiem 1: |r| < 0,05) -> pchniecie bladzi losowo
  KONTROLA: wybor losowy w pasmie (bez pamieci kierunku) -> std(d_eta) nie zalezy od n.
MOST (odczyt, nie zdanie do upadku): liczba ram rozroznialnych przez trajektorie w zakresie R
  = R/delta_eta ~ n, wiec koszt wskazania ramy = ln n + const, wspolczynnik 1.
  Masa wchodzi pod logarytm: n = rho*tau^2/2 = stosunek skali tykniecia do skali dyskretnosci.
"""
import numpy as np, json, time, sys

TAU   = 1.0
NS    = [5, 15, 50, 150, 500]          # elementow na tykniecie: 2 dekady
EPSS  = [0.05, 0.10, 0.20]
K     = 200
L     = 16
ETAMX = 2.2                            # okno pchniec wzgledem ukladu pudla
SEEDS = [1, 2]
T_, X_ = 60.0, 60.0
OUT   = "etap10_most_rama.json"

def sprinkle(rho, seed):
    rng = np.random.default_rng(seed)
    n = rng.poisson(rho * T_ * 2 * X_)
    t = rng.uniform(0, T_, n); x = rng.uniform(-X_, X_, n)
    u = (t + x) / np.sqrt(2); v = (t - x) / np.sqrt(2)
    return u, v

class Siatka:
    def __init__(s, u, v, h):
        s.h = h; row = np.floor(u / h).astype(np.int64)
        o = np.lexsort((v, row)); s.u, s.v, s.row = u[o], v[o], row[o]
        s.key = s.row * 1e6 + s.v                                   # v << 1e6
    def okno(s, u0, v0, U):
        r0, r1 = int(np.floor(u0 / s.h)), int(np.floor((u0 + U) / s.h))
        idx = []
        for r in range(r0, r1 + 1):
            a = np.searchsorted(s.key, r * 1e6 + v0, "right"); b = np.searchsorted(s.key, r * 1e6 + v0 + U, "right")
            if b > a: idx.append(np.arange(a, b))
        if not idx: return np.zeros(0, np.int64)
        i = np.concatenate(idx); du = s.u[i] - u0
        return i[(du > 0) & (du <= U)]

def trajektorie(S, eps, seed, losowo=False):
    rng = np.random.default_rng(seed + 777)
    U = TAU * 1.6 * np.exp(ETAMX) / np.sqrt(2)                      # zapas na dryf tref
    # start: elementy przy t~1, x w srodku
    t0 = (S.u + S.v) / np.sqrt(2); x0 = (S.u - S.v) / np.sqrt(2)
    kand0 = np.where((t0 < 1.0) & (np.abs(x0) < X_ / 3))[0]
    starts = rng.choice(kand0, K, replace=False)
    eta_cel = np.arctanh(rng.uniform(-0.9, 0.9, K))
    wyn = []
    for k in range(K):
        tip = starts[k]; prev = None; tref = TAU; etas = []; ok = True
        for krok in range(L - 1):
            i = S.okno(S.u[tip], S.v[tip], U)
            du = S.u[i] - S.u[tip]; dv = S.v[i] - S.v[tip]
            m = dv > 0; i, du, dv = i[m], du[m], dv[m]
            tk = np.sqrt(2 * du * dv); eta = 0.5 * np.log(du / dv)
            m = (tk > (1 - eps) * tref) & (tk < (1 + eps) * tref) & (np.abs(eta) < ETAMX)
            i, du, dv, tk, eta = i[m], du[m], dv[m], tk[m], eta[m]
            if len(i) == 0: ok = False; break
            if losowo and krok > 0:
                j = rng.integers(len(i))
            elif krok == 0:
                j = np.argmin(np.abs(eta - eta_cel[k]))
            else:
                pu, pv = S.u[prev], S.v[prev]
                tpc = np.sqrt(2 * (S.u[i] - pu) * (S.v[i] - pv))
                j = np.argmin(tpc - tref - tk)
            # granica pudla: nie ufamy krokom blisko brzegu
            tt = (S.u[i[j]] + S.v[i[j]]) / np.sqrt(2); xx = (S.u[i[j]] - S.v[i[j]]) / np.sqrt(2)
            if tt > T_ - U * np.sqrt(2) or abs(xx) > X_ - U * np.sqrt(2): ok = False; break
            etas.append(eta[j]); prev, tip = tip, i[j]
            tref = tk[j]                                             # pasmo wzgledem poprzedniego kroku
        if ok and len(etas) == L - 1: wyn.append(etas)
    return np.array(wyn)

def statystyki(E):
    d = np.diff(E[:, 1:], axis=1)                                    # pomijamy krok startowy (cel zewnetrzny)
    a, b = d[:, :-1].ravel(), d[:, 1:].ravel()
    return float(d.std()), float(np.corrcoef(a, b)[0, 1]), int(len(E))

if __name__ == "__main__":
    tryb = sys.argv[1] if len(sys.argv) > 1 else "pelny"
    res = {}
    for n in NS:
        rho = 2 * n / TAU**2
        for seed in SEEDS:
            t0 = time.time(); u, v = sprinkle(rho, seed); S = Siatka(u, v, 0.5)
            for eps in EPSS:
                for los in (False, True):
                    E = trajektorie(S, eps, seed, losowo=los)
                    sd, r1, kk = statystyki(E)
                    res[f"{n}|{eps}|{int(los)}|{seed}"] = dict(sd=sd, r1=r1, K=kk)
            print(f"n={n} ziarno {seed}: {len(u)} elementow, {time.time()-t0:.0f}s", flush=True)
    json.dump(res, open(OUT, "w"), indent=1)

    print("\n n   eps  | std(d_eta)  | P1: std*4sqrt2*eps*n | P3: r1  | kontrola losowa std | trajektorii")
    for eps in EPSS:
        xs, ys = [], []
        for n in NS:
            q = [res[f"{n}|{eps}|0|{s}"] for s in SEEDS]; c = [res[f"{n}|{eps}|1|{s}"] for s in SEEDS]
            sd = np.mean([a["sd"] for a in q]); r1 = np.mean([a["r1"] for a in q]); sc = np.mean([a["sd"] for a in c])
            print(f"{n:4d} {eps:.2f} | {sd:.5f}     | {sd*4*np.sqrt(2)*eps*n:.3f}               | {r1:+.3f}  | {sc:.3f}               | {sum(a['K'] for a in q)}")
            xs.append(np.log(n)); ys.append(np.log(sd))
        print(f"   P2 eps={eps}: wykladnik std wobec n = {np.polyfit(xs, ys, 1)[0]:+.3f}  (przewidywane -1,00)\n")
