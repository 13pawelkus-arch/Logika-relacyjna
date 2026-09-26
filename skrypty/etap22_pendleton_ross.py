# etap22 — Pendleton–Ross / Hill bez kierunku: stosunek stosunków (poprawka 165)
#
# R = y_t²/g₃², jedna pętla, tylko QCD i top (b₃ = −7):
#   16π² d ln R/dt = 2 g₃² (9/2·R − (8 + b₃)),  16π² d ln g₃²/dt = 2 b₃ g₃²
#   ⇒ u = 1/R:  d(u − 9/2)/d ln g₃² = (u − 9/2)/b₃   ⇒   (u − 9/2) ∝ α₃^{1/b₃} = α₃^{−1/7}
# Zdanie do upadku: relacja (1/R₁ − 9/2)/(1/R₂ − 9/2) = (α₃₁/α₃₂)^{1/b₃} zachodzi dla dowolnych dwóch punktów
# odniesienia t₁, t₂ (bez wyróżniania „początku”), do dokładności całkowania — dla trzech różnych wartości R
# w jednym punkcie (w tym R ≫ 1: quasi-punkt Hilla). Kontrola: z wykładnikiem 1/b₃ ± 20% relacja nie zachodzi.
import numpy as np
b3 = -7.0
def pochodne(t, s):
    yt2, g2 = s
    d_yt2 = 2 * yt2 * (4.5 * yt2 - 8 * g2) / (16 * np.pi ** 2)
    d_g2 = 2 * b3 * g2 * g2 / (16 * np.pi ** 2)
    return np.array([d_yt2, d_g2])
def rk4(s, t0, t1, n=20000):
    h = (t1 - t0) / n; t = t0
    for _ in range(n):
        k1 = pochodne(t, s); k2 = pochodne(t + h / 2, s + h / 2 * k1); k3 = pochodne(t + h / 2, s + h / 2 * k2); k4 = pochodne(t + h, s + h * k3)
        s = s + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4); t += h
    return s
aP = None
L = np.log(1.22e19 / 173.0)            # zakres pustyni (ln stosunku skal) — tylko do liczb
g2_P = 4 * np.pi / (1 / 0.1085 + (7 / (2 * np.pi)) * L)   # α₃ w drugim punkcie (jedna pętla)
print(f"α₃: {0.1085:.4f} i {g2_P/(4*np.pi):.4f} (stosunek {0.1085/(g2_P/(4*np.pi)):.2f})")
ok = True
for R_P in (0.1, 2.0, 50.0):
    s_P = np.array([R_P * g2_P, g2_P])
    s_t = rk4(s_P, L, 0.0)
    R_t = s_t[0] / s_t[1]
    lewa = (1 / R_t - 4.5) / (1 / R_P - 4.5)
    for wyk, nazwa in ((1 / b3, "1/b₃"), (1.2 / b3, "1,2/b₃"), (0.8 / b3, "0,8/b₃")):
        prawa = ((s_t[1] / (4 * np.pi)) / (g2_P / (4 * np.pi))) ** wyk
        r = abs(lewa - prawa) / abs(prawa)
        if nazwa == "1/b₃": ok &= r < 1e-6; msg = "PRZESZŁO" if r < 1e-6 else "UPADŁO"
        else: msg = "kontrola: nie zachodzi" if r > 1e-3 else "KONTROLA MARTWA"
        print(f"  R w jednym punkcie = {R_P:>5}: R w drugim = {R_t:.4f}; wykładnik {nazwa}: różnica względna {r:.1e} -> {msg}")
    if R_P == 50.0:
        yt = np.sqrt(s_t[0]); print(f"  quasi-punkt Hilla (R ≫ 1): R = {R_t:.3f}, y_t = {yt:.3f}, m_t = y_t·174 GeV ≈ {yt*174:.0f} GeV (tylko QCD+top, jedna pętla); zmierzone 173")
print(f"-> {'PRZESZŁO' if ok else 'UPADŁO'}; wzdłuż całej pustyni odchylenie (1/R − 9/2) zmienia się o czynnik {(0.1085/(g2_P/(4*np.pi)))**(1/7):.2f}")
