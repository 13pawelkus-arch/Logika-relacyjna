"""
Liczba czworoscianow wokol krawedzi w kompleksie z etap5 (triada = sciana, pamiec = czwarty wierzcholek).
[L] Regge 1961: krzywizna w kompleksie czworoscianow siedzi na krawedziach; dla czworoscianow foremnych
plasko wokol krawedzi przy 2pi/arccos(1/3) = 5,104 czworoscianach -> 5 = krzywizna dodatnia, 6+ = ujemna.
ZDANIE PRZED RACHUNKIEM: srednia liczba czworoscianow wokol krawedzi WEWNETRZNEJ > 5,104
(zgodnie z ujemna krzywizna Olliviera -0,16 z etap5). Rozklad (ile 4, 5, 6, ...) raportowany.
Zastrzezenie: kompleks kombinatoryczny = czworosciany rowne (sztywne) = "zero absolutne" w jezyku ramy;
dynamika (falujace boki) nie jest tu obecna, wiec to jest migawka, nie srednia po odczytach.
"""
import numpy as np, math, collections, sys
sys.path.insert(0, '.')
from collections import deque, defaultdict
def kompleks_tety(W, seed=1):
    src = open('etap5_kompleks.py').read()
    src = src.replace("    adj=[set() for _ in range(nv)]", "    return [tets[i] for i in zywe]\n    adj=[set() for _ in range(nv)]")
    ns = {}; exec(src, ns); return ns['kompleks'](W, seed)
flat = 2*math.pi/math.acos(1/3)
for W in (4000, 16000, 48000):
    T = kompleks_tety(W)
    fc = collections.Counter(); ec = collections.Counter()
    for t in T:
        for f in [tuple(sorted(t[:i]+t[i+1:])) for i in range(4)]: fc[f] += 1
        for a in range(4):
            for b in range(a+1, 4): ec[(min(t[a],t[b]), max(t[a],t[b]))] += 1
    brzeg = set()
    for f, k in fc.items():
        if k == 1:
            for a in range(3):
                for b in range(a+1, 3): brzeg.add((f[a], f[b]))
    wew = [k for e, k in ec.items() if e not in brzeg]
    h = collections.Counter(wew)
    print(f"W={W}: czworoscianow {len(T)}, krawedzi wewn. {len(wew)}, srednio {np.mean(wew):.3f} (plasko {flat:.3f}) | "
          f"rozklad: " + ", ".join(f"{k}:{h[k]/len(wew):.1%}" for k in sorted(h)[:8]))
