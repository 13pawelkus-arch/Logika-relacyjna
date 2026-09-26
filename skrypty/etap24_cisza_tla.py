# etap24 — trzy warunki „ciszy tła” na końcu Plancka: czy mogą zachodzić razem (temat (b) po 167)
#
# Warunki (normalizacja V = λ|H|⁴, m_H² = 2λv², jak w §F1 i u Hamady–Kawaia–Ody):
#   (i)   λ(koniec) = 0                                        — 154, „Ø z Ø nie jest relacją”
#   (ii)  β_λ(koniec) = 0; przy λ = 0:  6y_t⁴ = ⅜[2g₂⁴ + (g₂² + g_Y²)²]   ⇔ 6m_W⁴ + 3m_Z⁴ − 12m_t⁴ = 0 (155 D)
#   (iii) goła masa Higgsa przy obcięciu = 0 (Veltman; HKO, PRD 87, 053009, wz. 14):
#         C = 6λ + ¾g_Y² + 9⁄4·g₂² − 6y_t² = 0;  przy λ = 0:  ⇔ 6m_W² + 3m_Z² − 12m_t² = 0
# Zdania zapisane przed rachunkiem:
# Z1 [T]: przy λ = 0 warunki (ii) i (iii) wykluczają się dla wszystkich dodatnich m_W², m_Z²:
#     z (iii) m_t² = (2m_W² + m_Z²)/4, wtedy 6m_W⁴ + 3m_Z⁴ − 12m_t⁴ = 3[(m_W² − m_Z²/2)² + m_Z⁴/2] > 0.
#     Sprawdzenie numeryczne na siatce i losowo; kontrola: przy λ ≠ 0 (bez warunku (i)) oba warunki
#     DAJĄ SIĘ spełnić razem (inaczej wykluczenie nie wynikałoby z λ = 0, tylko z samej treści MS).
# Z2 (ilustracja na danych źródłowych, dwie pętle; Antusch–Hinze–Saad, arXiv:2510.01312v2, tab. 2):
#     na skalach 10¹²…10¹⁶ GeV y_t wymagane przez (ii) > y_t wymagane przez (iii), oba < y_t zmierzone.
import numpy as np

print('Z1 [T] — (ii) i (iii) przy λ = 0:')
x, y = np.meshgrid(np.linspace(1e-3, 10, 801), np.linspace(1e-3, 10, 801))   # m_W², m_Z² (dowolne jednostki)
z = (2 * x + y) / 4                                                            # m_t² z (iii)
s4 = 6 * x ** 2 + 3 * y ** 2 - 12 * z ** 2
wz = 3 * ((x - y / 2) ** 2 + y ** 2 / 2)
rng = np.random.default_rng(1)
xr, yr = rng.uniform(0, 1e4, 10 ** 6), rng.uniform(0, 1e4, 10 ** 6)
s4r = 6 * xr ** 2 + 3 * yr ** 2 - 12 * ((2 * xr + yr) / 4) ** 2
ok1 = (s4 > 0).all() and np.allclose(s4, wz) and (s4r > 0).all()
print(f'  siatka 801×801: min STr M⁴ = {s4.min():.3e} > 0; tożsamość 3[(x − y/2)² + y²/2] do {np.abs(s4-wz).max():.1e}; '
      f'10⁶ losowych: min {s4r.min():.3e} > 0')
# kontrola: bez λ = 0 — szukamy (λ, y_t) spełniających oba warunki przy danych g₂, g_Y
g2, gY = 0.52296, 0.575240 * np.sqrt(3 / 5)          # 10¹⁶ GeV, AHS tab. 2 (g1 w normalizacji GUT)
def warunki(lam, yt):
    beta = 24 * lam ** 2 + 12 * lam * yt ** 2 - 6 * yt ** 4 - 3 * lam * (3 * g2 ** 2 + gY ** 2) + 3 / 8 * (2 * g2 ** 4 + (g2 ** 2 + gY ** 2) ** 2)
    C = 6 * lam + 0.75 * gY ** 2 + 2.25 * g2 ** 2 - 6 * yt ** 2
    return beta, C
# z C = 0: y_t² = λ + (¾g_Y² + 9⁄4 g₂²)/6; wstawiamy do β i szukamy zera w λ
lam = np.linspace(-0.5, 0.5, 200001)
yt2 = lam + (0.75 * gY ** 2 + 2.25 * g2 ** 2) / 6
m = yt2 > 0
b = warunki(lam[m], np.sqrt(yt2[m]))[0]
zm = np.where(np.sign(b[:-1]) != np.sign(b[1:]))[0]
rozw = [(lam[m][i], np.sqrt(yt2[m][i])) for i in zm]
kontrola1 = len(rozw) > 0 and all(abs(l) > 1e-3 for l, _ in rozw)
print('  kontrola (λ swobodne): rozwiązania (λ, y_t) = ' + ', '.join(f'({l:+.4f}, {t:.4f})' for l, t in rozw)
      + (' -> istnieją, λ ≠ 0: wykluczenie pochodzi z λ = 0' if kontrola1 else ' -> KONTROLA MARTWA'))
print(f'-> Z1 {"PRZESZŁO" if ok1 and kontrola1 else "UPADŁO"}\n')

print('Z2 — y_t wymagane przez (ii) i (iii) przy λ = 0 wobec zmierzonego (AHS tab. 2, MS-bar, dane PDG 2024):')
skale = {'1e12 GeV': (0.534498, 0.55157, 0.5138), '1e16 GeV': (0.575240, 0.52296, 0.4454)}
ok2 = True
for s, (g1, g2_, yt) in skale.items():
    gY_ = g1 * np.sqrt(3 / 5)
    yt_ii = (3 / 8 * (2 * g2_ ** 4 + (g2_ ** 2 + gY_ ** 2) ** 2) / 6) ** 0.25
    yt_iii = np.sqrt((0.75 * gY_ ** 2 + 2.25 * g2_ ** 2) / 6)
    ok2 &= yt_ii > yt_iii and yt_ii < yt and yt_iii < yt
    print(f'  {s}: y_t(ii: β_λ = 0) = {yt_ii:.4f}   y_t(iii: C = 0) = {yt_iii:.4f}   różnica {100*(yt_ii/yt_iii-1):.1f}%   zmierzone {yt:.4f}')
print(f'-> Z2 {"PRZESZŁO" if ok2 else "UPADŁO"}')
