"""
TEST NA POZIOMIE SWIATLA (A100). Rozwiazanie dychotomii: niezmienniczosc Lorentza po stronie
relacji nieczytanych (nieograniczona walencja), skonczona walencja dopiero po stronie ODCZYTU.

TLO: sprinkling 3+1 (wszystkie relacje, Lorentz z konstrukcji) - nic nie usuwamy.
TRAJEKTORIE: rozlaczne lancuchy (kazdy krok: najblizszy w czasie wlasnym, jeszcze nieuzyty element w przyszlosci).
ODCZYT: w kazdym swoim elemencie trajektoria czyta TRZY inne o najswiezszym zapisie
        (najmniejsze opoznienie w krokach zrodla) + PAMIEC (ta czytana w poprzednim kroku).

ZDANIA DO UPADKU (przed rachunkiem):
  Z1. Siec odczytow ma wymiar 3 +- 0,3 (kulki; i wykladnik odleglosci ~ K^(1/3)).
  Z2. Odleglosc w sieci rosnie LINIOWO z prawdziwa odlegloscia przestrzenna.
  Z3. KONTROLA bez pamieci: wymiar nizszy niz z pamiecia (jak R5 vs R6).
  Z4. KONTROLA losowa: czytanie trzech losowych trajektorii zamiast najswiezszych -> maly swiat,
      brak korelacji z odlegloscia przestrzenna.
WOLNE WYBORY: liczba czytanych (3) + pamiec; wybor "najswiezszy zapis"; budowa lancuchow;
  rozmiar diamentu; N i K; dlugosc lancucha L.
"""
import numpy as np, json, os, time
try:
    import cupy as cp; XP = cp; GPU = True
except ImportError:
    XP = np; GPU = False
from collections import deque

N      = 400_000       # elementow w sprinklingu 3+1
K      = 3_000         # trajektorii
L      = 16            # dlugosc lancucha (elementow na trajektorie)
BLOCK  = 512           # zdarzen odczytu liczonych naraz
SEEDS  = [1, 2]
CKPT   = "etap2a_swiatlo.json"

def sprinkle(N, rng):
    P = []
    while len(P) < N:
        X = rng.uniform(-1, 1, (2*N, 4)); ok = np.abs(X[:, 0]) + np.linalg.norm(X[:, 1:], axis=1) <= 1
        P.extend(X[ok])
    X = np.array(P[:N], dtype=np.float32); return X[:, 0].copy(), X[:, 1:].copy()

def trajektorie(t, x, K, L, rng, kand=12):
    # okno czasu wlasnego z gestosci: liczba kandydatow w przedziale ~ rho*(pi/24)*tau^4
    N = len(t); rho = N / (2*np.pi/3)
    taumax = float((kand*24/(np.pi*rho))**0.25)
    used = np.zeros(N, bool); chains = []
    order = np.argsort(t); cand = order[:int(0.4*N)]; rng.shuffle(cand)
    tg = XP.asarray(t); xg = XP.asarray(x)
    for s in cand:
        if len(chains) >= K: break
        if used[s]: continue
        ch = [int(s)]; used[s] = True
        for _ in range(L-1):
            a = ch[-1]
            dt = tg - tg[a]; d2 = ((xg - xg[a])**2).sum(axis=1)
            tau2 = dt**2 - d2
            ok = (dt > 0) & (tau2 > 0) & (tau2 <= taumax**2) & XP.asarray(~used)
            if not bool(ok.any()): break
            nxt = int(XP.argmax(XP.where(ok, tau2, -1.0)))   # najwiekszy czas wlasny w oknie = najblizej geodezyjnej
            ch.append(nxt); used[nxt] = True
        if len(ch) == L: chains.append(ch)
    print(f"  okno czasu wlasnego tau_max = {taumax:.3f}", flush=True)
    return chains

def siec(t, x, chains, pamiec=True, losowo=False, seed=0):
    rng = np.random.default_rng(seed)
    Kc = len(chains); E = XP.asarray(np.array(chains).reshape(-1))      # (Kc*L,)
    tE = XP.asarray(t)[E]; xE = XP.asarray(x)[E]
    poz = XP.tile(XP.arange(L), Kc); own = XP.repeat(XP.arange(Kc), L)
    adj = [set() for _ in range(Kc)]
    prev = [None]*Kc
    idxs = np.arange(Kc*L)
    for s in range(0, len(idxs), BLOCK):
        b = idxs[s:s+BLOCK]
        te = tE[XP.asarray(b)][:, None]; xe = xE[XP.asarray(b)][:, None, :]
        dt = tE[None, :] - te; d2 = ((xE[None, :, :] - xe)**2).sum(axis=2)
        past = (dt < 0) & (dt**2 > d2)
        lag = XP.where(past, (L - 1) - poz[None, :], 10**6).reshape(len(b), Kc, L).min(axis=2)  # (B,Kc)
        lag[XP.arange(len(b)), own[XP.asarray(b)]] = 10**6                                      # nie czytamy siebie
        best = XP.argsort(lag, axis=1)[:, :3]
        lagn = cp.asnumpy(lag) if GPU else lag; bestn = cp.asnumpy(best) if GPU else best
        for r, e in enumerate(b):
            k = int(e) // L
            if losowo:
                ok = np.where(lagn[r] < 10**6)[0]
                if len(ok) == 0: continue
                czyt = list(rng.choice(ok, min(3, len(ok)), replace=False))
            else:
                czyt = [int(j) for j in bestn[r] if lagn[r, int(j)] < 10**6]
            if not czyt: continue
            if pamiec and prev[k] is not None: czyt = czyt + [prev[k]]
            for j in czyt:
                if j != k: adj[k].add(j); adj[j].add(k)
            prev[k] = czyt[0]
    return adj

def pomiar(adj, Kc, cen, seed):
    rng = np.random.default_rng(seed); ds = []; md = []
    D = np.full((Kc, Kc), -1)
    src = rng.choice(Kc, min(40, Kc), replace=False)
    for s in src:
        D[s, s] = 0; dq = deque([int(s)])
        while dq:
            a = dq.popleft()
            for c in adj[a]:
                if D[s, c] < 0: D[s, c] = D[s, a] + 1; dq.append(c)
        v = D[s][D[s] >= 0]; md.append(v.mean())
        rs = np.arange(1, int(v.max()) + 1); cnt = np.array([(v <= r).sum() for r in rs])
        m = (cnt < 0.3*Kc) & (cnt > 15)
        if m.sum() >= 3: ds.append(np.polyfit(np.log(rs[m]), np.log(cnt[m]), 1)[0])
    real = np.linalg.norm(cen[:, None, :] - cen[None, :, :], axis=2)
    prof = []
    for k in range(1, 8):
        m = D == k
        if m.sum() > 20: prof.append((k, float(real[m].mean()), float(real[m].std()/np.sqrt(m.sum()))))
    return (float(np.mean(ds)) if ds else float("nan"), float(np.mean(md)),
            float(np.mean([len(a) for a in adj])), prof)

res = json.load(open(CKPT)) if os.path.exists(CKPT) else {}
for seed in SEEDS:
    rng = np.random.default_rng(seed)
    t0 = time.time(); t, x = sprinkle(N, rng)
    ch = trajektorie(t, x, K, L, rng); Kc = len(ch)
    cen = np.array([x[c].mean(axis=0) for c in ch])
    print(f"ziarno {seed}: trajektorii {Kc}, dlugosc {L}, budowa {time.time()-t0:.0f}s", flush=True)
    for nazwa, kw in [("pamiec", dict(pamiec=True)), ("bez pamieci", dict(pamiec=False)),
                      ("losowo (kontrola)", dict(pamiec=True, losowo=True))]:
        key = f"{seed}|{nazwa}"
        if key in res: continue
        t1 = time.time(); adj = siec(t, x, ch, seed=seed, **kw)
        d, mdist, st, prof = pomiar(adj, Kc, cen, seed)
        res[key] = dict(wymiar=d, srednia_odleglosc=mdist, stopien=st, profil=prof, czas=time.time()-t1)
        json.dump(res, open(CKPT, "w"))
        print(f"  {nazwa:18s}: wymiar {d:.2f} | sr. odleglosc {mdist:.2f} | stopien {st:.1f} | "
              + " ".join(f"k={k}:{r:.3f}" for k, r, _ in prof) + f"  ({time.time()-t1:.0f}s)", flush=True)
