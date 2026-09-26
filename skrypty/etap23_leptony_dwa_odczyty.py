# etap23 — stosunki e : μ : τ: dwa odczyty pod jedną nazwą (temat (a) po 165)
#
# Odczyt A = masa w sensie R1f-3: faza na WŁASNE tyknięcie nośnika = masa biegunowa (każdy lepton czyta siebie).
# Odczyt B = stosunek Yukaw (współczynników działania, R1f-1) przy WSPÓLNEJ rozdzielczości μ, schemat MS-bar
#            („masy biegnące” z §F1, poziom 2; 153: „e : μ : τ praktycznie stoją”).
# Dane [L]: A — PDG 2024/2025 (tabela zbiorcza leptonów); B — Antusch, Hinze, Saad, arXiv:2510.01312v2,
#           wzór (2.4) (M_Z) i tabela 2 (MS-bar, dane PDG 2024, SMDR + dwupętlowe RGE).
#
# Zdania zapisane przed rachunkiem:
# Z1 (153): stosunki y_μ/y_e, y_τ/y_e, y_τ/y_μ na 9 skalach M_Z … 10¹⁶ GeV zmieniają się względnie o < 10⁻³
#     (max/min − 1). Kontrola (żeby test nie był martwy): pojedyncze y_f zmieniają się w tym zakresie o > 1%.
# Z2: odczyty A i B są różne: dla każdej pary B/A − 1 > 0,5%, znak dodatni i kolejność τ/e > μ/e > τ/μ;
#     wielkość zgodna do 20% z jedną pętlą QED: B/A − 1 ≈ (3α/2π)·ln(m_i/m_j) (α = α(0); różnica = relacja
#     nośnika z polem EM między własnym tyknięciem a wspólną rozdzielczością).
# Z3 (Koide wyłącznie jako kontrola rozróżniająca odczyty, nie cel): Q = Σm/(Σ√m)²;
#     |Q_A − 2/3| < 2σ_A oraz |Q_B(M_Z) − 2/3| > 10σ_B (σ propagowane bez korelacji z błędów 1σ źródła —
#     zawyżone, więc ostrożne dla „> 10σ”). Q_B na pozostałych skalach tylko raportowane.
import numpy as np

# --- odczyt A: masy biegunowe [MeV], PDG 2024/2025 ---
mA = np.array([0.51099895000, 105.6583755, 1776.93])
sA = np.array([0.00000000015, 0.0000023, 0.09])

# --- odczyt B: Yukawy MS-bar (y_e/1e-6, y_μ/1e-4, y_τ/1e-2), dane PDG 2024 ---
skale = ['M_Z', '1 TeV', '3 TeV', '10 TeV', '100 TeV', '1e7 GeV', '1e9 GeV', '1e12 GeV', '1e16 GeV']
yB = np.array([
    [2.77713, 5.85042, 0.99378], [2.8227, 5.9465, 1.0101], [2.8402, 5.9833, 1.0163],
    [2.8492, 6.0022, 1.0196], [2.8637, 6.0327, 1.0248], [2.8681, 6.0421, 1.0264],
    [2.8508, 6.0056, 1.0201], [2.7978, 5.8939, 1.0012], [2.6935, 5.6745, 0.9639]]) * np.array([1e-6, 1e-4, 1e-2])
sB = np.array([
    [0.00036, 0.00075, 0.00014], [0.0006, 0.0013, 0.0002], [0.0014, 0.0030, 0.0005],
    [0.0015, 0.0032, 0.0005], [0.0024, 0.0050, 0.0008], [0.0039, 0.0083, 0.0014],
    [0.0054, 0.0113, 0.0019], [0.0072, 0.0152, 0.0026], [0.0091, 0.0192, 0.0033]]) * np.array([1e-6, 1e-4, 1e-2])
alfa0 = 1 / 137.035999178

pary = [(1, 0, 'μ/e'), (2, 0, 'τ/e'), (2, 1, 'τ/μ')]
def Q(m): return m.sum() / np.sqrt(m).sum() ** 2
def sigQ(m, s):  # propagacja bez korelacji, numerycznie
    g = np.array([(Q(m + np.eye(3)[k] * s[k] * 1e-3) - Q(m)) / 1e-3 for k in range(3)])
    return float(np.sqrt((g ** 2).sum()))

print('Z1 — stosunki Yukaw przy wspólnej rozdzielczości (odczyt B) na 9 skalach:')
ok1 = True
for i, j, n in pary:
    r = yB[:, i] / yB[:, j]
    zm = r.max() / r.min() - 1
    ok1 &= zm < 1e-3
    print(f'  y{n}: ' + ' '.join(f'{x:.4f}' for x in r) + f'   zmiana względna {zm:.1e}')
zm_poj = yB.max(axis=0) / yB.min(axis=0) - 1
kontrola1 = (zm_poj > 0.01).all()
print(f'  kontrola: pojedyncze y_e, y_μ, y_τ zmieniają się o ' + ', '.join(f'{100*z:.1f}%' for z in zm_poj)
      + (' -> test nie jest martwy' if kontrola1 else ' -> KONTROLA MARTWA'))
print(f'-> Z1 {"PRZESZŁO" if ok1 and kontrola1 else "UPADŁO"}\n')

print('Z2 — odczyt A (własne tyknięcie) wobec B (wspólna rozdzielczość, M_Z):')
ok2 = True; roz = {}
for i, j, n in pary:
    A = mA[i] / mA[j]; B = yB[0, i] / yB[0, j]
    d = B / A - 1; est = 3 * alfa0 / (2 * np.pi) * np.log(mA[i] / mA[j])
    roz[n] = d
    ok2 &= (d > 0.005) and (0.8 < d / est < 1.2)
    print(f'  {n}: A = {A:.6f}   B = {B:.6f}   B/A − 1 = {100*d:.3f}%   jedna pętla QED {100*est:.3f}%   stosunek {d/est:.3f}')
ok2 &= roz['τ/e'] > roz['μ/e'] > roz['τ/μ']
print(f'-> Z2 {"PRZESZŁO" if ok2 else "UPADŁO"}\n')

print('Z3 — Koide jako kontrola rozróżniająca odczyty (nie cel):')
QA, sQA = Q(mA), sigQ(mA, sA)
th = lambda q: np.degrees(np.arccos(1 / np.sqrt(3 * q)))
print(f'  A (biegunowe):  Q = {QA:.7f}   Q − 2/3 = {QA-2/3:+.2e}   = {(QA-2/3)/sQA:+.2f} σ   θ = {th(QA):.4f}°')
# m_τ z Q = 2/3 przy danych m_e, m_μ (pierwiastek dodatni)
a, b = np.sqrt(mA[0]), np.sqrt(mA[1])
# m_e + m_μ + x² = 2/3 (a + b + x)²  ->  x²/3 − (4/3)(a+b)x + (a²+b²) − (2/3)(a+b)² = 0
wsp = [1 / 3, -4 / 3 * (a + b), a * a + b * b - 2 / 3 * (a + b) ** 2]
x = max(np.roots(wsp).real)
print(f'  m_τ z Q = 2/3 i biegunowych m_e, m_μ: {x*x:.3f} MeV; PDG 2024: {mA[2]} ± {sA[2]} -> {(mA[2]-x*x)/sA[2]:+.2f} σ')
ok3 = abs(QA - 2 / 3) < 2 * sQA
for k, s in enumerate(skale):
    QB, sQB = Q(yB[k]), sigQ(yB[k], sB[k])
    if k == 0: ok3 &= abs(QB - 2 / 3) > 10 * sQB
    print(f'  B ({s:>8}): Q = {QB:.6f}   Q − 2/3 = {QB-2/3:+.2e}   = {(QB-2/3)/sQB:+7.1f} σ (bez korelacji)   θ = {th(QB):.3f}°')
print(f'-> Z3 {"PRZESZŁO" if ok3 else "UPADŁO"}')

# --- dopisane PO rachunku, tylko raport (bez zdania, nic nie rozstrzyga) — pułapka numerologiczna ---
# Parametryzacja: √m_n/μ − 1 = A·cos(δ + 2πn/3), μ = średnia √m; A = √2 ⇔ Q = 2/3.
# δ_L „nieodróżnialne od 2/9” (Żenczykowski, PRD 86, 117303 (2012)); 2/9 w pliku ma INNE źródło:
# R* = 2(8 + b₃)/9 z Pendletona–Rossa (165). Wspólnego wejścia brak — zapisane jako pułapka, nie wynik.
print('\nRaport (dopisany po rachunku): kąt δ trzech pierwiastków')
for nazwa, m in (('A (biegunowe)', mA), ('B (Yukawy, M_Z)', yB[0])):
    c = np.sqrt(m) / np.sqrt(m).mean() - 1
    Aamp = np.sqrt(2 * np.sum(c ** 2) / 3)
    d = np.arccos(c.max() / Aamp)
    print(f'  {nazwa:16}: amplituda/√2 − 1 = {Aamp/np.sqrt(2)-1:+.2e}   δ = {d:.7f}   δ − 2/9 = {d-2/9:+.2e}')
