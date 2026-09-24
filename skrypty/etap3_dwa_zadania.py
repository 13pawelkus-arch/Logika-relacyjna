"""
DWA ZADANIA (A100). Uruchom: python etap3_dwa_zadania.py A   albo   ... B   albo   ... AB

ZADANIE A - test na poziomie swiatla w duzej skali (GPU).
  Tlo: sprinkling w tubie (czas x trzy kierunki). Trajektorie: lancuchy (najwiekszy czas wlasny
  w oknie tau z gestosci; indeks komorkowy). Odczyt: trzy trajektorie o najswiezszym zapisie + pamiec.
  Siec brana jako MIGAWKA (jeden krok na trajektorie).
  ZDANIA DO UPADKU:
    A1. wymiar migawki = 3 +- 0,1 (blad z 3 ziaren)
    A2. stosunek (prawdziwa odleglosc)/(krok w sieci) stalny dla k >= 2 w granicach 10%
    A3. pamiec nie zmienia wymiaru o wiecej niz 0,1 (tlo juz ma trzy kierunki)
    A4. kontrola losowa: profil plaski, brak proporcjonalnosci
  Odniesienie (N=5 mln, K=4000, 3 ziarna): 3,03 +- 0,04 (pamiec), 3,10 +- 0,04 (bez), kontrola plaska.

ZADANIE B - NIEZALEZNA RODZINA REGUL (CPU/GPU, tanie).
  Inny mechanizm wzrostu: POWIELANIE wezla (nie podzial relacji). Nowy wezel = kopia losowego wezla,
  dziedziczy k jego relacji + relacje z rodzicem (+ opcjonalnie pamiec: wezel, z ktorego rodzic powstal).
  ZDANIE DO UPADKU:
    B1. zgodnosc dwoch niezaleznych pomiarow wymiaru (|z odleglosci - z kulek| < 0,3) wystepuje
        TYLKO dla trzech polaczen z pamiecia - tak jak w rodzinie "podzial relacji" (R5/R6/R7).
  Jesli tak -> przestaje to byc wlasnoscia jednej reguly.
"""
import sys, json, os, time
import numpy as np
from collections import deque
try:
    import cupy as cp; XP = cp; GPU = True
except ImportError:
    XP = np; GPU = False

# ---------------------------------------------------------------- wspolne pomiary
def ball_dim(adj, k, seed, frac=0.3):
    W = len(adj); rng = np.random.default_rng(seed); ds = []
    for s in rng.choice(W, min(k, W), replace=False):
        D = np.full(W, -1); D[s] = 0; dq = deque([int(s)])
        while dq:
            a = dq.popleft()
            for c in adj[a]:
                if D[c] < 0: D[c] = D[a] + 1; dq.append(c)
        v = D[D >= 0]
        rs = np.arange(1, int(v.max()) + 1); cnt = np.array([(v <= r).sum() for r in rs])
        m = (cnt < frac * W) & (cnt > 20)
        if m.sum() >= 4: ds.append(np.polyfit(np.log(rs[m]), np.log(cnt[m]), 1)[0])
    return (float(np.mean(ds)) if ds else float("nan"),
            float(np.std(ds) / np.sqrt(max(len(ds), 1))))

def mean_dist(adj, k, seed):
    W = len(adj); rng = np.random.default_rng(seed); out = []
    for s in rng.choice(W, min(k, W), replace=False):
        D = np.full(W, -1); D[s] = 0; dq = deque([int(s)])
        while dq:
            a = dq.popleft()
            for c in adj[a]:
                if D[c] < 0: D[c] = D[a] + 1; dq.append(c)
        out.append(D[D >= 0].mean())
    return float(np.mean(out))

# ================================================================ ZADANIE A
T_, S_ = 10.0, 6.0
NA, KA, LA, KAND = 24_000_000, 20_000, 33, 12
SEEDS_A = [1, 2, 3]
CKPT_A = "etap3_A.json"

def sprinkle(N, rng):
    return (rng.uniform(0, T_, N).astype(np.float32),
            rng.uniform(0, S_, (N, 3)).astype(np.float32))

def trajektorie(t, x, K, L, rng):
    N = len(t); rho = N / (T_ * S_**3); h = float((24 * KAND / (np.pi * rho))**0.25)
    ns = int(np.ceil(S_ / h)) + 2; nt = int(np.ceil(T_ / h)) + 2
    ci = (np.floor(t / h).astype(np.int64), *(np.floor(x[:, i] / h).astype(np.int64) for i in range(3)))
    key = ((ci[0] * ns + ci[1]) * ns + ci[2]) * ns + ci[3]
    o = np.argsort(key); ks = key[o]
    uk, ui = np.unique(ks, return_index=True)
    start = dict(zip(uk.tolist(), ui.tolist()))
    ends = dict(zip(uk.tolist(), (list(ui[1:]) + [len(ks)])))
    used = np.zeros(N, bool); chains = []
    seeds = np.where(t < 0.1 * T_)[0]; rng.shuffle(seeds)
    def kand(a):
        c = (int(t[a] // h), int(x[a, 0] // h), int(x[a, 1] // h), int(x[a, 2] // h))
        out = []
        for d0 in (0, 1):
            for d1 in (-1, 0, 1):
                for d2 in (-1, 0, 1):
                    for d3 in (-1, 0, 1):
                        kk = (((c[0] + d0) * ns + c[1] + d1) * ns + c[2] + d2) * ns + c[3] + d3
                        if kk in start: out.append(o[start[kk]:ends[kk]])
        return np.concatenate(out) if out else np.empty(0, np.int64)
    for s in seeds:
        if len(chains) >= K: break
        if used[s]: continue
        ch = [int(s)]; used[s] = True
        for _ in range(L - 1):
            a = ch[-1]; C = kand(a)
            if len(C) == 0: break
            dt = t[C] - t[a]; d2 = ((x[C] - x[a])**2).sum(1); tau2 = dt**2 - d2
            ok = (dt > 0) & (tau2 > 0) & (tau2 <= h * h) & (~used[C])
            if not ok.any(): break
            nxt = int(C[np.argmax(np.where(ok, tau2, -1))]); ch.append(nxt); used[nxt] = True
        if len(ch) == L: chains.append(ch)
    return chains, h

def migawka(t, x, chains, krok=None, pamiec=True, losowo=False, seed=0, blok=64):
    rng = np.random.default_rng(seed); Kc = len(chains)
    E = np.array(chains); L = E.shape[1]; krok = L - 1 if krok is None else krok
    tE = XP.asarray(t[E]); xE = XP.asarray(x[E]); ar = XP.arange(L)[None, None, :]
    adj = [set() for _ in range(Kc)]
    for s0 in range(0, Kc, blok):
        ks = np.arange(s0, min(s0 + blok, Kc))
        for off, dodaj in ([(0, True)] + ([(-1, False)] if (pamiec and krok > 0) else [])):
            te = tE[XP.asarray(ks), krok + off][:, None, None]
            xe = xE[XP.asarray(ks), krok + off][:, None, None, :]
            dt = tE[None, :, :] - te; d2 = ((xE[None, :, :, :] - xe)**2).sum(-1)
            past = (dt < 0) & (dt**2 > d2)
            lp = XP.where(past.any(2), XP.where(past, ar, -1).max(2), -1)
            sw = XP.where(lp >= 0, (L - 1) - lp, 10**6)
            sw[XP.arange(len(ks)), XP.asarray(ks)] = 10**6
            swn = cp.asnumpy(sw) if GPU else sw
            for r, k in enumerate(ks):
                ok = np.where(swn[r] < 10**6)[0]
                if len(ok) == 0: continue
                if dodaj:
                    czyt = ([int(j) for j in rng.choice(ok, min(3, len(ok)), replace=False)] if losowo
                            else [int(j) for j in ok[np.argsort(swn[r][ok])[:3]]])
                else:
                    czyt = [int(ok[np.argmin(swn[r][ok])])]     # pamiec: jeden z poprzedniego kroku
                for j in czyt:
                    if j != int(k): adj[int(k)].add(j); adj[j].add(int(k))
    return adj

def zadanie_A():
    res = json.load(open(CKPT_A)) if os.path.exists(CKPT_A) else {}
    for seed in SEEDS_A:
        rng = np.random.default_rng(seed); t0 = time.time()
        t, x = sprinkle(NA, rng); ch, h = trajektorie(t, x, KA, LA, rng); Kc = len(ch)
        cen = np.array([x[c].mean(0) for c in ch])
        print(f"A ziarno {seed}: tau={h:.3f}, trajektorii {Kc} x {LA}, budowa {time.time()-t0:.0f}s", flush=True)
        if Kc < 2000: print("  za malo trajektorii"); continue
        for nazwa, kw in [("pamiec", {}), ("bez pamieci", dict(pamiec=False)), ("losowo", dict(losowo=True))]:
            key = f"{seed}|{nazwa}"
            if key in res: continue
            t1 = time.time(); adj = migawka(t, x, ch, seed=seed, **kw)
            d, e = ball_dim(adj, 40, seed); md = mean_dist(adj, 40, seed)
            D = np.full((Kc, Kc), -1); rng2 = np.random.default_rng(seed)
            for s in rng2.choice(Kc, 60, replace=False):
                D[s, s] = 0; dq = deque([int(s)])
                while dq:
                    a = dq.popleft()
                    for c in adj[a]:
                        if D[s, c] < 0: D[s, c] = D[s, a] + 1; dq.append(c)
            real = np.linalg.norm(cen[:, None, :] - cen[None, :, :], axis=2)
            prof = [(k, float(real[D == k].mean())) for k in range(1, 12) if (D == k).sum() > 50]
            res[key] = dict(wymiar=d, blad=e, odleglosc=md,
                            stopien=float(np.mean([len(a) for a in adj])), profil=prof)
            json.dump(res, open(CKPT_A, "w"))
            ratio = " ".join(f"{r/k:.2f}" for k, r in prof[1:])
            print(f"  {nazwa:12s}: wymiar {d:.2f} ± {e:.2f} | stopien {res[key]['stopien']:.1f} | "
                  f"odl/k (k>=2): {ratio}  ({time.time()-t1:.0f}s)", flush=True)

# ================================================================ ZADANIE B
def powielanie(W, seed, k_dziedz, pamiec):
    """Nowy wezel = kopia losowego rodzica: dziedziczy k jego relacji + relacje z rodzicem
       (+ pamiec: wezel, z ktorego rodzic sam powstal)."""
    rng = np.random.default_rng(seed)
    adj = [{1, 2, 3}, {0, 2, 3}, {0, 1, 3}, {0, 1, 2}]
    zrodlo = [0, 0, 0, 0]                                  # z czego powstal dany wezel (pamiec)
    while len(adj) < W:
        p = int(rng.integers(len(adj))); nowy = len(adj); adj.append(set())
        sas = list(adj[p])
        wyb = [int(z) for z in rng.choice(sas, min(k_dziedz, len(sas)), replace=False)] if sas else []
        conn = [p] + wyb
        if pamiec and zrodlo[p] not in conn and zrodlo[p] != nowy: conn.append(zrodlo[p])
        for q in conn: adj[nowy].add(q); adj[q].add(nowy)
        zrodlo.append(p)
    return adj

def zadanie_B(W=200_000):
    print(f"\nB: powielanie wezla, W={W}. Zgodnosc = |wymiar z odleglosci - z kulek| < 0,3")
    print(" polaczen (rodzic + k [+ pamiec]) | z odleglosci | z kulek       | roznica | stopien")
    out = []
    for k in [1, 2, 3, 4]:
        for pam in [False, True]:
            rows = []
            for Wi in [W // 16, W // 4, W]:
                rows.append((Wi, np.mean([mean_dist(powielanie(Wi, s, k, pam), 12, s) for s in [1, 2]])))
            r = np.array(rows); p = np.polyfit(np.log(r[:, 0]), np.log(r[:, 1]), 1)[0]
            a = powielanie(W, 1, k, pam); bd = ball_dim(a, 12, 1)
            dd = 1 / p if p > 0 else float("nan"); roz = abs(dd - bd[0])
            opis = f"1 + {k}" + (" + pamiec" if pam else "")
            print(f" {opis:32s} | {dd:8.2f}     | {bd[0]:.2f} ± {bd[1]:.2f}   | {roz:6.2f} "
                  f"| {np.mean([len(z) for z in a]):.2f}"
                  + ("   <-- ZGODNE" if roz < 0.3 else ""), flush=True)
            out.append((opis, dd, bd[0], roz))
    zg = [o for o in out if o[3] < 0.3]
    print("\n ZGODNE konfiguracje: " + (", ".join(f"{o[0]} (d≈{o[2]:.2f})" for o in zg) if zg else "brak"))

if __name__ == "__main__":
    co = sys.argv[1] if len(sys.argv) > 1 else "AB"
    if "B" in co: zadanie_B()
    if "A" in co: zadanie_A()
