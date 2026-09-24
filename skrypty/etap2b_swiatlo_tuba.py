"""
TEST NA POZIOMIE SWIATLA - wersja "tuba" z indeksem komorkowym (A100; trajektorie licza sie i na CPU).

TLO: sprinkling w pudle: czas [0,T] x trzy kierunki [0,S]^3 (3 kierunki + porzadek = 4 punkty odniesienia).
     Wszystkie relacje obecne (nieograniczona walencja, brak wyrozniowego ukladu) - nic nie usuwamy.
TRAJEKTORIE: lancuchy; nastepny element = ten o NAJWIEKSZYM czasie wlasnym w oknie tau_max
     (najblizej geodezyjnej). tau_max wyliczane z gestosci: liczba kandydatow w przedziale = rho*(pi/24)*tau^4.
     Indeks komorkowy o boku tau_max -> koszt kroku staly zamiast O(N).
ODCZYT: w kazdym elemencie trajektoria czyta TRZY inne o najswiezszym zapisie (najmniejsze opoznienie
     w krokach zrodla) + PAMIEC (czytana w poprzednim kroku).

ZDANIA DO UPADKU:
  Z1. Siec odczytow ma wymiar 3 +- 0,3 (kulki).
  Z2. Odleglosc w sieci rosnie liniowo z prawdziwa odlegloscia przestrzenna.
  Z3. Kontrola bez pamieci: wymiar nizszy.
  Z4. Kontrola losowa (trzy losowe zamiast najswiezszych): maly swiat, brak korelacji z odlegloscia.
WOLNE WYBORY: T, S, N, K, L; liczba czytanych (3)+pamiec; regula budowy lancucha; okno tau_max (k=12 kandydatow).
"""
import numpy as np, json, os, time
from collections import deque
try:
    import cupy as cp; XP = cp; GPU = True
except ImportError:
    XP = np; GPU = False

T, S   = 8.0, 5.0
N      = 5_000_000      # CPU wystarcza (~5 min/ziarno); A100 dopiero przy K >= 20 tys.
K, L   = 4_000, 12
KAND   = 12
BLOCK  = 256
SEEDS  = [1, 2, 3]
CKPT   = "etap2b_swiatlo.json"

def sprinkle(N, rng):
    t = rng.uniform(0, T, N).astype(np.float32)
    x = rng.uniform(0, S, (N, 3)).astype(np.float32)
    return t, x

def siatka(t, x, h):
    c = np.stack([np.floor(t/h)] + [np.floor(x[:, i]/h) for i in range(3)], axis=1).astype(np.int64)
    nt, ns = int(np.ceil(T/h))+1, int(np.ceil(S/h))+1
    key = ((c[:, 0]*ns + c[:, 1])*ns + c[:, 2])*ns + c[:, 3]
    o = np.argsort(key); key = key[o]
    start = {}
    uk, ui = np.unique(key, return_index=True)
    for k, i in zip(uk.tolist(), ui.tolist()): start[k] = i
    ends = dict(zip(uk.tolist(), (list(ui[1:]) + [len(key)])))
    return o, start, ends, ns

def trajektorie(t, x, K, L, rng):
    N = len(t); rho = N/(T*S**3); h = float((24*KAND/(np.pi*rho))**0.25)
    o, start, ends, ns = siatka(t, x, h)
    used = np.zeros(N, bool); chains = []
    seeds = np.where(t < 0.15*T)[0]; rng.shuffle(seeds)
    def kandydaci(a):
        ci = [int(t[a]//h)] + [int(x[a, i]//h) for i in range(3)]
        out = []
        for dt_ in (0, 1):
            for dxx in (-1, 0, 1):
                for dyy in (-1, 0, 1):
                    for dzz in (-1, 0, 1):
                        kk = (((ci[0]+dt_)*ns + ci[1]+dxx)*ns + ci[2]+dyy)*ns + ci[3]+dzz
                        if kk in start: out.append(o[start[kk]:ends[kk]])
        return np.concatenate(out) if out else np.array([], dtype=np.int64)
    for s in seeds:
        if len(chains) >= K: break
        if used[s]: continue
        ch = [int(s)]; used[s] = True
        for _ in range(L-1):
            a = ch[-1]; C = kandydaci(a)
            if len(C) == 0: break
            dt = t[C]-t[a]; d2 = ((x[C]-x[a])**2).sum(axis=1); tau2 = dt**2-d2
            ok = (dt > 0) & (tau2 > 0) & (tau2 <= h*h) & (~used[C])
            if not ok.any(): break
            nxt = int(C[np.argmax(np.where(ok, tau2, -1))]); ch.append(nxt); used[nxt] = True
        if len(ch) == L: chains.append(ch)
    return chains, h

def siec(t, x, chains, krok=None, pamiec=True, losowo=False, seed=0):
    """MIGAWKA: po jednym odczycie z kazdej trajektorii, z tego samego kroku.
    Przestrzen jest relacja W DANEJ CHWILI - sklejanie odczytow z calego zycia trajektorii
    miesza rozne chwile i tworzy polaczenia miedzy miejscami, ktore nigdy nie byly blisko
    jednoczesnie (pierwsza wersja: stopien 22, wymiar 2,42 zamiast 3,01)."""
    rng = np.random.default_rng(seed); Kc = len(chains)
    E = np.array(chains); L_ = E.shape[1]
    krok = L_ - 1 if krok is None else krok
    tE = XP.asarray(t[E]); xE = XP.asarray(x[E]); ar = XP.arange(L_)[None, :]
    adj = [set() for _ in range(Kc)]
    def swiezosc(te, xe, k):
        dt = tE - te; d2 = ((xE - xe)**2).sum(axis=2); past = (dt < 0) & (dt**2 > d2)
        lp = XP.where(past.any(axis=1), XP.where(past, ar, -1).max(axis=1), -1)
        sw = XP.where(lp >= 0, (L_ - 1) - lp, 10**6); sw[k] = 10**6
        return cp.asnumpy(sw) if GPU else sw
    for k in range(Kc):
        sw = swiezosc(tE[k, krok], xE[k, krok], k)
        ok = np.where(sw < 10**6)[0]
        if len(ok) == 0: continue
        czyt = ([int(j) for j in rng.choice(ok, min(3, len(ok)), replace=False)] if losowo
                else [int(j) for j in ok[np.argsort(sw[ok])[:3]]])
        if pamiec and krok > 0:                      # pamiec: najswiezszy zapis z poprzedniego kroku
            sp = swiezosc(tE[k, krok-1], xE[k, krok-1], k)
            if sp.min() < 10**6: czyt.append(int(np.argmin(sp)))
        for j in czyt:
            if j != k: adj[k].add(j); adj[j].add(k)
    return adj

def pomiar(adj, Kc, cen, seed):
    rng = np.random.default_rng(seed); ds = []; md = []
    src = rng.choice(Kc, min(40, Kc), replace=False); D = np.full((Kc, Kc), -1)
    for s in src:
        D[s, s] = 0; dq = deque([int(s)])
        while dq:
            a = dq.popleft()
            for c in adj[a]:
                if D[s, c] < 0: D[s, c] = D[s, a]+1; dq.append(c)
        v = D[s][D[s] >= 0]; md.append(v.mean())
        rs = np.arange(1, int(v.max())+1); cnt = np.array([(v <= r).sum() for r in rs])
        m = (cnt < 0.3*Kc) & (cnt > 15)
        if m.sum() >= 3: ds.append(np.polyfit(np.log(rs[m]), np.log(cnt[m]), 1)[0])
    real = np.linalg.norm(cen[:, None, :] - cen[None, :, :], axis=2)
    prof = [(k, float(real[D == k].mean()), int((D == k).sum())) for k in range(1, 8) if (D == k).sum() > 20]
    return (float(np.mean(ds)) if ds else float("nan"), float(np.mean(md)),
            float(np.mean([len(a) for a in adj])), prof)

if __name__ == "__main__":
    res = json.load(open(CKPT)) if os.path.exists(CKPT) else {}
    for seed in SEEDS:
        rng = np.random.default_rng(seed); t0 = time.time()
        t, x = sprinkle(N, rng); ch, h = trajektorie(t, x, K, L, rng); Kc = len(ch)
        cen = np.array([x[c].mean(axis=0) for c in ch])
        print(f"ziarno {seed}: okno tau={h:.3f}, trajektorii {Kc} x {L}, budowa {time.time()-t0:.0f}s", flush=True)
        if Kc < 200: print("  za malo trajektorii - zwieksz N albo zmniejsz L"); continue
        for nazwa, kw in [("pamiec", dict(pamiec=True)), ("bez pamieci", dict(pamiec=False)),
                          ("losowo (kontrola)", dict(pamiec=True, losowo=True))]:
            key = f"{seed}|{nazwa}"
            if key in res: continue
            t1 = time.time(); adj = siec(t, x, ch, seed=seed, **kw)
            d, mdist, st, prof = pomiar(adj, Kc, cen, seed)
            res[key] = dict(wymiar=d, odleglosc=mdist, stopien=st, profil=prof)
            json.dump(res, open(CKPT, "w"))
            print(f"  {nazwa:18s}: wymiar {d:.2f} | sr. odleglosc {mdist:.2f} | stopien {st:.1f} | "
                  + " ".join(f"k={k}:{r:.2f}" for k, r, _ in prof) + f"  ({time.time()-t1:.0f}s)", flush=True)
