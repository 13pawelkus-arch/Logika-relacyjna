"""
Etap 0q. Duzy przebieg: dryf nachylenia + niezaleznosc od rozmiaru poddiamentu.

ZDANIA DO UPADKU (przed rachunkiem):
  Z1. Nachylenie S wobec ln N nie zalezy od V/V_U (4, 9, 16, 36) w granicach slupkow.
  Z2. Stala rosnie o (1/3)*ln(sqrt(r1/r2)) przy zmianie stosunku objetosci:
      0,231 na kazde poczworzenie r  (bo S = (1/3) ln(l_U/eps), l_U ~ V_U^(1/2)).
  Z3. Nachylenie w przesuwanych oknach po ln N NIE maleje monotonicznie poza slupki.
      Jesli maleje -> prawo logarytmiczne nie jest asymptotyczne (dryf z C4a.16d).
  Z4. Wariant A (bez obciecia globalnego) daje wykladnik 1 dla kazdego V/V_U.

Koszt: eigh liczone RAZ na (N, ziarno); ratio i c to tanie operacje na podmacierzach.
Jesli pamiec nie wystarczy na najwieksze N, usun je z listy Ns - reszta zostaje wazna.
"""
import numpy as np
try:
    import cupy as cp; XP = cp; GPU = True
except ImportError:
    XP = np; GPU = False

# A100 40 GB: 24576 wchodzi (macierz zespolona 9,7 GB, eigh potrzebuje ~3x).
# A100 80 GB: mozna dolozyc 32768. Przy OOM skrypt pomija dane N i leci dalej.
Ns     = [2048, 4096, 8192, 12288, 16384, 20480, 24576]
SEEDS_BY_N = {2048: 8, 4096: 8, 8192: 8, 12288: 6, 16384: 6, 20480: 4, 24576: 3}
NSEED  = min(SEEDS_BY_N.values())      # tyle ziaren wchodzi do wspolnych dopasowan
CKPT   = "etap0q_wyniki.json"
CS     = [1.0, 1.5, 2.0, 3.0]
RATIOS = [4.0, 9.0, 16.0, 36.0]
WIN    = 4          # ile punktow w oknie przy badaniu dryfu

viol = []
def free():
    if GPU: cp.get_default_memory_pool().free_all_blocks()

def prep(N, seed):
    rng = XP.random.default_rng(seed)
    u, v = rng.random(N), rng.random(N)
    C = ((u[:, None] < u[None, :]) & (v[:, None] < v[None, :])).astype(float)
    D = 0.5 * (C.T - C); del C; free()
    al, V = XP.linalg.eigh(1j * D); del D; free()
    return al, V, u, v

def mask(u, v, ratio):
    h = 0.5 * (1 - 1 / np.sqrt(ratio))
    return XP.where((u > h) & (u < 1 - h) & (v > h) & (v < 1 - h))[0]

def entropy(al, V, U, N, c=None, tag=""):
    VU = V[U]; NU = int(len(U))
    keep = XP.ones(len(al), bool) if c is None else XP.abs(al) > c * np.sqrt(N) / (4 * np.pi)
    pos = keep & (al > 0)
    Du = (VU[:, keep] * al[keep]) @ VU[:, keep].conj().T
    Wu = (VU[:, pos]  * al[pos])  @ VU[:, pos].conj().T
    Ru = Wu - 0.5 * Du; del Wu
    mu, Q = XP.linalg.eigh(Du)
    thr = 1e-10 * float(XP.abs(mu).max()) if c is None else c * np.sqrt(NU) / (4 * np.pi)
    sel = XP.abs(mu) > thr; P = Q[:, sel]
    M = (P.conj().T @ Ru @ P) / mu[sel][:, None]
    M = cp.asnumpy(M) if GPU else np.asarray(M)
    ev = np.linalg.eigvals(M)
    sc = np.abs(ev).max() + 1e-300
    if float(np.abs(ev.imag).max()) / sc > 1e-8: viol.append(f"{tag}: czesc urojona")
    lam = 0.5 + ev.real; ls = np.sort(lam)
    if float(np.abs(ls + ls[::-1] - 1.0).max()) > 1e-6 * max(1.0, np.abs(lam).max()):
        viol.append(f"{tag}: brak parowania lambda")
    good = lam[(lam >= 1 - 1e-8) | (lam <= 1e-8)]; good = good[np.abs(good) > 1e-10]
    del Du, Ru, Q, P; free()
    return float(np.sum(good * np.log(np.abs(good)))), NU, int(sel.sum())

res = {}
import json, os
if os.path.exists(CKPT):
    res = {tuple(json.loads(k)): v for k, v in json.load(open(CKPT)).items()}
    print(f"wczytano checkpoint: {len(res)} serii")

done_N = []
for N in Ns:
    if ("A", RATIOS[0], N) in res:
        done_N.append(N); print(f"  ... N={N} z checkpointu"); continue
    try:
      for s in range(1, SEEDS_BY_N.get(N, 4) + 1):
        al, V, u, v = prep(N, s)
        for r in RATIOS:
            U = mask(u, v, r)
            res.setdefault(("A", r, N), []).append(entropy(al, V, U, N, None, f"A r={r} N={N}")[0])
            for c in CS:
                res.setdefault((c, r, N), []).append(entropy(al, V, U, N, c, f"c={c} r={r} N={N}")[0])
            del U
        del al, V, u, v; free()
    except Exception as e:
        print(f"  !! N={N} pominiete: {type(e).__name__}: {e}", flush=True)
        for k in [k for k in res if k[2] == N]: del res[k]
        free(); continue
    done_N.append(N)
    json.dump({json.dumps(list(k)): v for k, v in res.items()}, open(CKPT, "w"))
    print(f"  ... N={N} gotowe ({SEEDS_BY_N.get(N,4)} ziaren, zapisane)", flush=True)

Ns = done_N          # dalsze dopasowania tylko po tym, co sie policzylo

def slope(key_c, r, sub):
    x = np.log(np.array(sub, float)); out = []
    for i in range(NSEED):
        y = np.array([res[(key_c, r, N)][i] for N in sub])
        out.append(np.polyfit(x, y, 1)[0])
    return float(np.mean(out)), float(np.std(out) / np.sqrt(len(out)))

print("\nZ4 / kontrola A: wykladnik S wobec N (ma byc ~1)")
for r in RATIOS:
    x = np.log(np.array(Ns, float)); o = []
    for i in range(NSEED):
        y = np.log([res[("A", r, N)][i] for N in Ns]); o.append(np.polyfit(x, y, 1)[0])
    print(f"  V/V_U={r:5.1f}: {np.mean(o):+.3f} +- {np.std(o)/np.sqrt(len(o)):.3f}")

print("\nZ1: nachylenie wobec ln N, pelny zakres")
print(f"{'c':>5} | " + " | ".join(f"r={r:<5.0f}" for r in RATIOS))
for c in CS:
    print(f"{c:5.1f} | " + " | ".join(f"{slope(c,r,Ns)[0]:.3f}+-{slope(c,r,Ns)[1]:.3f}" for r in RATIOS)
          + "   (1/6 = 0.167)")

print("\nZ2: stala przy najwiekszym N — roznice miedzy sasiednimi r (ma byc 0,231)")
for c in CS:
    v = [np.mean(res[(c, r, Ns[-1])]) for r in RATIOS]
    d = [v[i] - v[i+1] for i in range(len(v)-1)]
    print(f"  c={c:4.1f}: S = " + ", ".join(f"{x:.3f}" for x in v)
          + "   roznice: " + ", ".join(f"{x:+.3f}" for x in d))

print(f"\nZ3: dryf — nachylenie w przesuwanych oknach po {WIN} punktow (r=16)")
for c in CS:
    row = []
    for i in range(len(Ns) - WIN + 1):
        sub = Ns[i:i+WIN]; m, e = slope(c, 16.0, sub)
        row.append(f"[{sub[0]}-{sub[-1]}] {m:.3f}+-{e:.3f}")
    print(f"  c={c:4.1f}: " + "  ".join(row))

print(f"\nziarna uzyte we wspolnych dopasowaniach: {NSEED} (pojedyncze punkty maja wiecej: {SEEDS_BY_N})")
print("KONTROLE:", "wszystkie przeszly" if not viol else f"NARUSZONE: {viol[:10]}")
