"""
Regula R4: narodziny trajektorii; partnerzy nowej trajektorii wybierani sposrod sasiedztwa rodzica
(promien 2) wedlug NAKLADANIA PRZESZLOSCI W OKNIE. Zapis steruje siecia.

PAMIEC: brak macierzy N x N. Kazda trajektoria trzyma bitset swojej przeszlosci w oknie
(bufor pierscieniowy o dlugosci Wmax*Rmax bitow). Okno efektywne = R rund = R * W(t) ostatnich elementow.
BLOKI: w kazdym kroku aktualizowany jest zbior niezalezny w sieci partnerow (krok Luby'ego).
Trajektorie nie bedace partnerami nie czytaja nawzajem swoich koncow -> ich kroki sa przestrzennie
rozdzielone -> kolejnosc liczenia nic nie znaczy (to nie jest przyblizenie).

ZDANIA DO UPADKU (przed rachunkiem):
  Z1. Siec R4 ma srednia odleglosc rosnaca SZYBCIEJ niz R3 (R3: 6,3 / 8,7 / 11,0 / 14,3 dla W = 1e3 ... 6,4e4).
  Z2. Jesli rosnie potegowo: wykladnik >= 1/4 (1/3 = siec 3D).
  Z3. Wynik nie zalezy od okna R (2, 4, 8) w granicach czynnika 2 wykladnika.
WOLNE WYBORY: start (4 trajektorie wzajemnie partnerami); b; promien sasiedztwa 2; rodzic wymienia
partnera o najmniejszym nakladaniu na dziecko; okno R; nakladanie liczone jak Boguna-Krioukov
(wspolne / (min(tylko A, tylko B) + wspolne)) wzgledem okna, nie wspolnego przodka.
"""
import numpy as np, json, os, time
try:
    import cupy as cp; XP = cp; GPU = True
except ImportError:
    XP = np; GPU = False
from collections import deque

WMAX   = 128_000          # na 40 GB: R=4 -> ~8 GB bitsetow, R=8 -> ~16 GB
B_FRAC = 0.5              # udzial narodzin wsrod zdarzen (b)
RS     = [2, 4, 8]
SNAP   = [1_000, 4_000, 16_000, 64_000, 128_000]
SEEDS  = [1, 2]
CKPT   = "etap1i_r4_wyniki.json"

POP = XP.array([bin(i).count("1") for i in range(256)], dtype=XP.uint8)
def popcount_rows(A):                       # A: (k, words) uint64 -> (k,)
    return POP[A.view(XP.uint8)].reshape(A.shape[0], -1).sum(axis=1, dtype=XP.int64)

def run(seed, R, Wmax):
    rng = XP.random.RandomState(seed); hrng = np.random.default_rng(seed)
    L = R * Wmax; words = (L + 63) // 64
    bits = XP.zeros((Wmax, words), dtype=XP.uint64)       # przeszlosc w oknie, per trajektoria
    part = XP.full((Wmax, 3), -1, dtype=XP.int64)
    tipslot = XP.zeros(Wmax, dtype=XP.int64)
    part[:4] = XP.array([[1,2,3],[0,2,3],[0,1,3],[0,1,2]])
    tipslot[:4] = XP.arange(4)
    W = 4; n = 4
    snaps = {}
    def slot_bit(s):
        return (s // 64), XP.left_shift(XP.uint64(1), (s % 64).astype(XP.uint64))
    # zaznacz poczatkowe elementy jako obecne w oknie samych siebie
    w0, m0 = slot_bit(tipslot[:4]); 
    for k in range(4): bits[k, int(w0[k])] |= m0[k]
    while W < Wmax:
        # --- zbior niezalezny (krok Luby'ego) wsrod W trajektorii
        prio = rng.random_sample(W)
        P = part[:W]
        m_out = XP.max(XP.where(P >= 0, prio[XP.clip(P, 0, W-1)], -1.0), axis=1)
        m_in = XP.full(W, -1.0)
        src = XP.repeat(XP.arange(W), 3); dst = P.reshape(-1); ok = dst >= 0
        if GPU: cp.maximum.at(m_in, dst[ok], prio[src[ok]])
        else:   np.maximum.at(m_in, dst[ok], prio[src[ok]])
        I = XP.where(prio > XP.maximum(m_out, m_in))[0]
        nb = int(len(I))
        if nb == 0: continue
        # --- nowe elementy: sloty w buforze, czyszczenie starych bitow w tych slotach
        slots = (n + XP.arange(nb)) % L
        ws, ms = slot_bit(slots)
        bits[:W, :] &= ~XP.zeros((1, words), dtype=XP.uint64)  # no-op (utrzymanie typu)
        for wk in XP.unique(ws).tolist():
            mask = XP.bitwise_or.reduce(ms[ws == wk]) if GPU else np.bitwise_or.reduce(ms[ws == wk])
            bits[:W, wk] &= ~mask
        # --- przeszlosc nowych elementow = OR (wlasny koniec + 3 partnerow) + ich sloty
        idx = XP.concatenate([I[:, None], part[I]], axis=1)          # (nb, 4)
        newbits = XP.bitwise_or.reduce(bits[idx], axis=1) if GPU else np.bitwise_or.reduce(bits[idx], axis=1)
        tw, tm = slot_bit(tipslot[idx])
        for c in range(4):
            newbits[XP.arange(nb), tw[:, c]] |= tm[:, c]
        newbits[XP.arange(nb), ws] |= ms                              # element sam w swoim oknie
        # --- okno efektywne R*W(t): maska wiekowa
        age_lo = max(0, n + nb - R * W)
        valid = XP.zeros(words, dtype=XP.uint64)
        live = (XP.arange(age_lo, n + nb)) % L
        vw, vm = slot_bit(live)
        if GPU: cp.bitwise_or.at(valid, vw, vm)
        else:   np.bitwise_or.at(valid, vw, vm)
        # --- narodziny czy odczyt
        born = XP.asarray(hrng.random(nb) < B_FRAC)
        rd = XP.where(~born)[0]
        bits[I[rd]] = newbits[rd]; tipslot[I[rd]] = slots[rd]
        bI = XP.where(born)[0]
        room = Wmax - W; bI = bI[:room]
        if len(bI):
            par = I[bI]; nbits = newbits[bI] & valid
            c1 = part[par]                                           # (k,3)
            c2 = part[XP.clip(c1, 0, W-1)].reshape(len(bI), 9)       # (k,9)
            cand = XP.concatenate([par[:, None], c1, c2], axis=1)    # (k,13)
            # nakladanie: wspolne / (min(tylko A, tylko B) + wspolne)
            k = len(bI); CB = bits[XP.clip(cand, 0, W-1)] & valid     # (k,13,words)
            inter = popcount_rows((CB & nbits[:, None, :]).reshape(k*13, words)).reshape(k, 13)
            a_all = popcount_rows(nbits)[:, None]
            b_all = popcount_rows(CB.reshape(k*13, words)).reshape(k, 13)
            O = inter / (XP.minimum(a_all - inter, b_all - inter) + inter + 1e-9)
            O = O + 1e-9 * rng.random_sample(O.shape)
            O = XP.where(cand < 0, -1.0, O)
            # unikalni najlepsi trzej (bez duplikatow)
            order = XP.argsort(-O, axis=1)
            newid = W + XP.arange(k)
            chosen = XP.full((k, 3), -1, dtype=XP.int64)
            oc = to = None
            cand_np = cp.asnumpy(cand) if GPU else cand
            ord_np = cp.asnumpy(order) if GPU else order
            ch_np = np.full((k, 3), -1, dtype=np.int64)
            for r in range(k):
                seen = []
                for j in ord_np[r]:
                    v = int(cand_np[r, j])
                    if v >= 0 and v not in seen: seen.append(v)
                    if len(seen) == 3: break
                ch_np[r, :len(seen)] = seen
            chosen = XP.asarray(ch_np)
            part[newid] = chosen; bits[newid] = newbits[bI]; tipslot[newid] = slots[bI]
            # rodzic wymienia partnera o najmniejszym nakladaniu na dziecko
            Op = O[:, 1:4]                                           # nakladanie partnerow rodzica
            worst = XP.argmin(Op, axis=1)
            part[par, worst] = newid
            W += k
        n += nb
        for S in SNAP:
            if S <= W and S not in snaps:
                snaps[S] = (cp.asnumpy(part[:S]) if GPU else part[:S].copy())
    return snaps

def mean_dist(P, k=20, seed=0):
    W = len(P); adj = [set() for _ in range(W)]
    for i in range(W):
        for j in P[i]:
            if 0 <= j < W: adj[i].add(int(j)); adj[int(j)].add(i)
    rng = np.random.default_rng(seed); out = []
    for s in rng.choice(W, min(k, W), replace=False):
        D = np.full(W, -1); D[s] = 0; dq = deque([s])
        while dq:
            a = dq.popleft()
            for c in adj[a]:
                if D[c] < 0: D[c] = D[a] + 1; dq.append(c)
        out.append(D[D >= 0].mean())
    return float(np.mean(out))

res = json.load(open(CKPT)) if os.path.exists(CKPT) else {}
for R in RS:
    for s in SEEDS:
        key = f"R{R}|{s}"
        if key in res: continue
        t0 = time.time()
        try:
            snaps = run(s, R, WMAX)
        except Exception as e:
            print(f"  !! {key}: {type(e).__name__}: {e}"); continue
        res[key] = {str(S): mean_dist(P) for S, P in snaps.items()}
        json.dump(res, open(CKPT, "w"))
        print(f"  {key}: " + "  ".join(f"W={S}: {v:.2f}" for S, v in res[key].items()) + f"   ({time.time()-t0:.0f}s)", flush=True)

print("\nR3 (odniesienie): W=1e3: 6.32  4e3: 8.67  1.6e4: 11.02  6.4e4: 14.32")
for R in RS:
    rows = [(int(S), np.mean([res[f'R{R}|{s}'][S] for s in SEEDS if f'R{R}|{s}' in res and S in res[f'R{R}|{s}']]))
            for S in map(str, SNAP) if any(S in res.get(f'R{R}|{s}', {}) for s in SEEDS)]
    if len(rows) < 3: continue
    r = np.array(rows); p = np.polyfit(np.log(r[:,0]), np.log(r[:,1]), 1)[0]
    inc = [(r[k+1,1]-r[k,1]) / np.log2(r[k+1,0]/r[k,0]) for k in range(len(r)-1)]
    print(f"R={R}: " + "  ".join(f"W={int(a)}: {b:.2f}" for a, b in r) + f"   | wykladnik {p:.3f} | przyrosty/podwojenie " + ", ".join(f"{x:+.2f}" for x in inc))
