"""
DWA ZADANIA - wersja z praca na GPU (Colab: edytuj CO ponizej, nie uzywaj argv).

CO ZMIENIONE wzgledem etap3:
  - budowa trajektorii RownolegLE na GPU (siatka kubelkowa + gather), zamiast petli po krokach w Pythonie;
    WOLNY WYBOR: brak wylacznosci elementow (trajektorie moga rzadko trafic w ten sam element) -
    to wlasnie wylacznosc wymuszala sekwencyjnosc;
  - wybor trojki najswiezszych liczony na GPU (na CPU wracaja tylko 3 liczby na trajektorie);
  - BLOK konfigurowalny; pamiec bloku ~ BLOK * K * L * 4 B * ~4 tablice;
  - status po kazdym kroku budowy i po kazdym bloku migawki.

ZDANIA DO UPADKU (A): wymiar 3 +- 0,1; stosunek odleglosc/krok staly dla k>=2 (10%);
  pamiec zmienia wymiar o < 0,1; kontrola losowa: profil plaski.
  Odniesienie (N=5 mln, K=4000): 3,03 +- 0,04 (pamiec), 3,10 +- 0,04 (bez).
ZDANIE (B): zgodnosc dwoch pomiarow wymiaru (<0,3) tylko dla trzech polaczen z pamiecia.
"""
import json, os, time
import numpy as np
from collections import deque
try:
    import cupy as cp; XP = cp; GPU = True
except ImportError:
    XP = np; GPU = False

CO      = "AB"          # "A", "B" albo "AB"
T_, S_  = 10.0, 6.0
NA      = 24_000_000    # przy problemach z pamiescia: 12_000_000
KA      = 20_000        # trajektorii
LA      = 33            # krokow na trajektorie
KAND    = 12            # srednia liczba kandydatow w oknie (wyznacza tau)
BUCKET  = 64            # miejsc na komorke siatki
BLOK    = 128           # trajektorii liczonych naraz w migawce
SEEDS_A = [1, 2, 3]
CKPT_A  = "etap3b_A.json"

def log(s): print(s, flush=True)
def tonp(a): return cp.asnumpy(a) if GPU else np.asarray(a)

# ---------------------------------------------------------------- pomiary
def ball_dim(adj, k, seed, frac=0.3):
    W = len(adj); rng = np.random.default_rng(seed); ds = []
    for s in rng.choice(W, min(k, W), replace=False):
        D = np.full(W, -1); D[s] = 0; dq = deque([int(s)])
        while dq:
            a = dq.popleft()
            for c in adj[a]:
                if D[c] < 0: D[c] = D[a] + 1; dq.append(c)
        v = D[D >= 0]
        if v.max() < 3: continue
        rs = np.arange(1, int(v.max()) + 1); cnt = np.array([(v <= r).sum() for r in rs])
        m = (cnt < frac * W) & (cnt > 20)
        if m.sum() >= 4: ds.append(np.polyfit(np.log(rs[m]), np.log(cnt[m]), 1)[0])
    return (float(np.mean(ds)) if ds else float("nan"),
            float(np.std(ds) / np.sqrt(max(len(ds), 1))) if ds else float("nan"))

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
def zadanie_A():
    res = json.load(open(CKPT_A)) if os.path.exists(CKPT_A) else {}
    for seed in SEEDS_A:
        t00 = time.time()
        rng = XP.random.RandomState(seed)
        t = rng.uniform(0, T_, NA).astype(XP.float32)
        x = rng.uniform(0, S_, (NA, 3)).astype(XP.float32)
        rho = NA / (T_ * S_**3); h = float((24 * KAND / (np.pi * rho))**0.25)
        nt = int(np.ceil(T_ / h)) + 2; ns = int(np.ceil(S_ / h)) + 2
        log(f"A ziarno {seed}: tau={h:.3f}, siatka {nt}x{ns}^3, sprinkling {time.time()-t00:.0f}s")
        # --- siatka kubelkowa: dla kazdej komorki do BUCKET elementow
        ci = XP.stack([XP.floor(t / h), XP.floor(x[:, 0] / h),
                       XP.floor(x[:, 1] / h), XP.floor(x[:, 2] / h)], axis=1).astype(XP.int32)
        cell = ((ci[:, 0] * ns + ci[:, 1]) * ns + ci[:, 2]) * ns + ci[:, 3]
        ncell = nt * ns * ns * ns
        order = XP.argsort(cell); cs = cell[order]
        # pozycja w kubelku
        starts = XP.searchsorted(cs, XP.arange(ncell), side="left")
        poz = XP.arange(NA) - starts[cs]
        keep = poz < BUCKET
        buck = XP.full((ncell, BUCKET), -1, dtype=XP.int32)
        buck[cs[keep], poz[keep]] = order[keep].astype(XP.int32)
        del order, cs, poz, keep, cell
        if GPU: cp.get_default_memory_pool().free_all_blocks()
        log(f"  siatka gotowa ({time.time()-t00:.0f}s), kubelki {ncell}")
        # --- starty: elementy z dolu tuby
        low = XP.where(t < 0.08 * T_)[0]
        sel = low[XP.asarray(np.random.default_rng(seed).choice(int(len(low)), KA, replace=False))]
        tips = sel.astype(XP.int32); chains = [tips.copy()]
        off = XP.asarray(np.array([[d0, d1, d2, d3] for d0 in (0, 1) for d1 in (-1, 0, 1)
                                   for d2 in (-1, 0, 1) for d3 in (-1, 0, 1)], dtype=np.int32))
        for krok in range(LA - 1):
            c0 = XP.stack([XP.floor(t[tips] / h), XP.floor(x[tips, 0] / h),
                           XP.floor(x[tips, 1] / h), XP.floor(x[tips, 2] / h)], axis=1).astype(XP.int32)
            cc = c0[:, None, :] + off[None, :, :]                       # (K,54,4)
            cc = XP.clip(cc, 0, XP.asarray([nt-1, ns-1, ns-1, ns-1], dtype=XP.int32))
            cid = ((cc[:, :, 0] * ns + cc[:, :, 1]) * ns + cc[:, :, 2]) * ns + cc[:, :, 3]
            cand = buck[cid].reshape(len(tips), -1)                      # (K, 54*BUCKET)
            ok = cand >= 0
            ci2 = XP.where(ok, cand, 0).astype(XP.int32)
            dt = t[ci2] - t[tips][:, None]
            d2 = ((x[ci2] - x[tips][:, None, :])**2).sum(-1)
            tau2 = dt**2 - d2
            good = ok & (dt > 0) & (tau2 > 0) & (tau2 <= h * h)
            best = XP.argmax(XP.where(good, tau2, -1.0), axis=1)
            nxt = ci2[XP.arange(len(tips)), best]
            zyje = good.any(axis=1)
            tips = XP.where(zyje, nxt, tips).astype(XP.int32)
            chains.append(tips.copy())
            log(f"  krok {krok+2}/{LA}: zyje {int(zyje.sum())}/{KA} ({time.time()-t00:.0f}s)")
            if int(zyje.sum()) < 0.5 * KA:
                log("  ZA DUZO trajektorii utknelo - zmniejsz LA albo zwieksz NA"); break
        E = XP.stack(chains, axis=1)                                     # (K, L)
        L = E.shape[1]; Kc = E.shape[0]
        tE = t[E]; xE = x[E]; ar = XP.arange(L)[None, None, :]
        cen = tonp(xE.mean(axis=1))
        log(f"  trajektorie: {Kc} x {L}, budowa {time.time()-t00:.0f}s")

        def migawka(pamiec=True, losowo=False, s=0):
            rng2 = np.random.default_rng(s); adj = [set() for _ in range(Kc)]
            krok = L - 1
            for s0 in range(0, Kc, BLOK):
                ks = XP.arange(s0, min(s0 + BLOK, Kc))
                for off_, glowny in ([(0, True)] + ([(-1, False)] if (pamiec and krok > 0) else [])):
                    te = tE[ks, krok + off_][:, None, None]
                    xe = xE[ks, krok + off_][:, None, None, :]
                    dt = tE[None, :, :] - te
                    past = (dt < 0) & (dt**2 > ((xE[None, :, :, :] - xe)**2).sum(-1))
                    lp = XP.where(past.any(2), XP.where(past, ar, -1).max(2), -1)
                    sw = XP.where(lp >= 0, (L - 1) - lp, 10**6)
                    sw[XP.arange(len(ks)), ks] = 10**6
                    if glowny and losowo:
                        r = XP.where(sw < 10**6, XP.asarray(np.random.default_rng(s0+s).random(sw.shape)), 2.0)
                        pick = tonp(XP.argsort(r, axis=1)[:, :3]); val = tonp(XP.sort(r, axis=1)[:, :3]) < 2.0
                    else:
                        n = 3 if glowny else 1
                        pick = tonp(XP.argsort(sw, axis=1)[:, :n]); val = tonp(XP.sort(sw, axis=1)[:, :n]) < 10**6
                    for r_ in range(pick.shape[0]):
                        k = s0 + r_
                        for j, okj in zip(pick[r_], val[r_]):
                            if okj and int(j) != k: adj[k].add(int(j)); adj[int(j)].add(k)
                if (s0 // BLOK) % 20 == 0: log(f"    migawka {s0}/{Kc} ({time.time()-t00:.0f}s)")
            return adj

        for nazwa, kw in [("pamiec", {}), ("bez pamieci", dict(pamiec=False)), ("losowo", dict(losowo=True))]:
            key = f"{seed}|{nazwa}"
            if key in res: log(f"  {nazwa}: z checkpointu"); continue
            t1 = time.time(); adj = migawka(s=seed, **kw)
            d, e = ball_dim(adj, 40, seed); md = mean_dist(adj, 40, seed)
            D = np.full((Kc, Kc), -1, dtype=np.int16)
            for s_ in np.random.default_rng(seed).choice(Kc, 60, replace=False):
                D[s_, s_] = 0; dq = deque([int(s_)])
                while dq:
                    a = dq.popleft()
                    for c in adj[a]:
                        if D[s_, c] < 0: D[s_, c] = D[s_, a] + 1; dq.append(c)
            real = np.linalg.norm(cen[:, None, :] - cen[None, :, :], axis=2)
            prof = [(k, float(real[D == k].mean())) for k in range(1, 14) if (D == k).sum() > 50]
            res[key] = dict(wymiar=d, blad=e, odleglosc=md, profil=prof,
                            stopien=float(np.mean([len(a) for a in adj])))
            json.dump(res, open(CKPT_A, "w"))
            log(f"  {nazwa:12s}: wymiar {d:.2f} ± {e:.2f} | stopien {res[key]['stopien']:.1f} | "
                f"odl/k (k>=2): " + " ".join(f"{r/k:.2f}" for k, r in prof[1:]) + f"  ({time.time()-t1:.0f}s)")
        del t, x, tE, xE, E, buck
        if GPU: cp.get_default_memory_pool().free_all_blocks()

# ================================================================ ZADANIE B
def powielanie(W, seed, k_dziedz, pamiec):
    rng = np.random.default_rng(seed)
    adj = [{1, 2, 3}, {0, 2, 3}, {0, 1, 3}, {0, 1, 2}]; zrodlo = [0, 0, 0, 0]
    while len(adj) < W:
        p = int(rng.integers(len(adj))); nowy = len(adj); adj.append(set())
        sas = list(adj[p])
        wyb = [int(z) for z in rng.choice(sas, min(k_dziedz, len(sas)), replace=False)] if sas else []
        conn = [p] + wyb
        if pamiec and zrodlo[p] not in conn: conn.append(zrodlo[p])
        for q in conn: adj[nowy].add(q); adj[q].add(nowy)
        zrodlo.append(p)
    return adj

def zadanie_B(W=200_000):
    log(f"\nB: powielanie wezla, W={W}. Zgodnosc = |z odleglosci - z kulek| < 0,3")
    log(" konfiguracja                     | z odleglosci | z kulek      | roznica | stopien")
    zg = []
    for k in [1, 2, 3, 4]:
        for pam in [False, True]:
            rows = []
            for Wi in [W // 16, W // 4, W]:
                rows.append((Wi, np.mean([mean_dist(powielanie(Wi, s, k, pam), 12, s) for s in [1, 2]])))
            r = np.array(rows); p = np.polyfit(np.log(r[:, 0]), np.log(r[:, 1]), 1)[0]
            a = powielanie(W, 1, k, pam); bd = ball_dim(a, 12, 1)
            dd = 1 / p if p > 0 else float("nan"); roz = abs(dd - bd[0])
            opis = f"rodzic + {k}" + (" + pamiec" if pam else "")
            log(f" {opis:32s} | {dd:8.2f}     | {bd[0]:.2f} ± {bd[1]:.2f}  | {roz:6.2f} | "
                f"{np.mean([len(z) for z in a]):.2f}" + ("   <-- ZGODNE" if roz < 0.3 else ""))
            if roz < 0.3: zg.append((opis, bd[0]))
    log(" ZGODNE: " + (", ".join(f"{o} (d≈{d:.2f})" for o, d in zg) if zg else "brak"))

if "B" in CO: zadanie_B()
if "A" in CO: zadanie_A()
