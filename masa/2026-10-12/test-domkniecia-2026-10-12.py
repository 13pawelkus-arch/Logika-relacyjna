#!/usr/bin/env python3
"""Dokładny test wybranego sektora, nie test całej ramy ontologicznej.

Wymagania: Python >=3.10, sympy, numpy.
Uruchomienie: python test-domkniecia-2026-10-12.py
Wynik: test-domkniecia-2026-10-12.json obok skryptu.

Współczynniki w q są sprawdzane symbolicznie dla dowolnego |q|=1.
Kontrole pełnej macierzy zegara są dodatkowe i numeryczne.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parent
Q = sp.Symbol("q", nonzero=True)
I = sp.I
SQ3 = sp.sqrt(3)
K = sp.kronecker_product
checks: list[dict] = []


def simp(x):
    if isinstance(x, sp.MatrixBase):
        return x.applyfunc(sp.simplify)
    return sp.simplify(x)


def adj(x):
    """Hermitowskie sprzężenie na okręgu |q|=1, bez próbkowania faz."""
    return x.conjugate().T.subs(sp.conjugate(Q), 1 / Q)


def eq(name, actual, expected):
    delta = simp(actual - expected)
    ok = delta == (sp.zeros(*delta.shape) if isinstance(delta, sp.MatrixBase) else 0)
    checks.append({"name": name, "method": "exact", "pass": bool(ok)})
    if not ok:
        raise AssertionError(f"{name}: {delta}")


def close(name, residual, tolerance=1e-11):
    ok = float(residual) < tolerance
    checks.append({"name": name, "method": "numeric", "pass": bool(ok),
                   "residual": float(residual), "tolerance": tolerance})
    if not ok:
        raise AssertionError(f"{name}: {residual}")


def vec(bits):
    v = sp.zeros(2 ** len(bits), 1)
    v[int(bits, 2), 0] = 1
    return v


def embed(op, target, n):
    return K(*[op if j == target else sp.eye(2) for j in range(n)])


def swap(a, b, n):
    out = sp.zeros(2**n)
    for col in range(2**n):
        bits = [(col >> (n - 1 - j)) & 1 for j in range(n)]
        bits[a], bits[b] = bits[b], bits[a]
        row = sum(bit << (n - 1 - j) for j, bit in enumerate(bits))
        out[row, col] = 1
    return out


def cnot(control, target, n):
    out = sp.zeros(2**n)
    for col in range(2**n):
        active = (col >> (n - 1 - control)) & 1
        row = col ^ (1 << (n - 1 - target)) if active else col
        out[row, col] = 1
    return out


def reduced_pure(v, keep, n):
    rest = [j for j in range(n) if j not in keep]
    a = sp.zeros(2 ** len(keep), 2 ** len(rest))
    for index in range(2**n):
        bits = [(index >> (n - 1 - j)) & 1 for j in range(n)]
        row = sum(bits[j] << (len(keep) - 1 - k) for k, j in enumerate(keep))
        col = sum(bits[j] << (len(rest) - 1 - k) for k, j in enumerate(rest))
        a[row, col] = v[index]
    return simp(a * adj(a))


def probability(v, required, n):
    out = 0
    for index in range(2**n):
        if all(((index >> (n - 1 - j)) & 1) == bit for j, bit in required.items()):
            z = v[index]
            out += sp.conjugate(z).subs(sp.conjugate(Q), 1 / Q) * z
    return simp(out)


X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -I], [I, 0]])
Z = sp.diag(1, -1)
P0 = sp.diag(1, 0)
P1 = sp.diag(0, 1)

# 1. Wewnętrzne relacje czterech fizycznych nośników.
s = (vec("01") - vec("10")) / sp.sqrt(2)
t0 = (vec("01") + vec("10")) / sp.sqrt(2)
tp, tm = vec("00"), vec("11")
l0 = K(s, s)
l1 = (K(tp, tm) - K(t0, t0) + K(tm, tp)) / SQ3
W = l0.row_join(l1)
eq("code_isometry", W.H * W, sp.eye(2))
for label, pauli in zip("xyz", [X, Y, Z]):
    total = sum((embed(pauli, j, 4) / 2 for j in range(4)), sp.zeros(16))
    eq(f"total_spin_{label}_annihilates_entire_code", total * W, sp.zeros(16, 2))
    for j in range(4):
        eq(f"single_spin_{j}_{label}_has_zero_code_expectation",
           W.H * embed(pauli, j, 4) * W, sp.zeros(2))

E12, E23 = swap(0, 1, 4), swap(1, 2, 4)
e12, e23 = simp(W.H * E12 * W), simp(W.H * E23 * W)
eq("pair_12_relation", e12, -Z)
eq("pair_23_relation", e23, (Z + SQ3 * X) / 2)
eq("X_from_pair_relations", (2 * e23 + e12) / SQ3, X)
eq("Y_from_noncommuting_relations", (Z * X - X * Z) / (2 * I), Y)
for a, pa in enumerate([X, Y, Z]):
    for b, pb in enumerate([X, Y, Z]):
        expected = int(a == b) * sp.eye(2)
        expected += sum((I * sp.LeviCivita(a, b, c) * pc
                         for c, pc in enumerate([X, Y, Z])), sp.zeros(2))
        eq(f"Pauli_closure_{a}_{b}", pa * pb, expected)

ps_full, pt_full = (sp.eye(16) - E23) / 2, (sp.eye(16) + E23) / 2
Ufull = ps_full + Q * pt_full
ps, pt = simp(W.H * ps_full * W), simp(W.H * pt_full * W)
U = simp(W.H * Ufull * W)
Uexpected = sp.Matrix([[1 + 3 * Q, SQ3 * (Q - 1)],
                      [SQ3 * (Q - 1), 3 + Q]]) / 4
eq("U_derived_from_physical_pair", U, Uexpected)
eq("full_pair_unitary_all_phases", adj(Ufull) * Ufull, sp.eye(16))
eq("no_leakage_from_global_singlet", Ufull * W, W * U)
eq("logical_U_unitary_all_phases", adj(U) * U, sp.eye(2))

state = U[:, 0]
cosq, sinq = (Q + 1 / Q) / 2, (Q - 1 / Q) / (2 * I)
r = [simp((adj(state) * p * state)[0]) for p in [X, Y, Z]]
expected_r = [SQ3 * (1 - cosq) / 4, SQ3 * sinq / 2, (1 + 3 * cosq) / 4]
for axis, value, expected in zip("xyz", r, expected_r):
    eq(f"Bloch_{axis}_all_phases", value, expected)
eq("conditional_Bloch_purity", sum(a**2 for a in r), 1)
eq("complementary_variance_sum", sum(1 - a**2 for a in r), 2)
eq("phase_reconstructed_from_y_z", (4 * r[2] - 1) / 3 + I * 2 * r[1] / SQ3, Q)
pz = simp((1 + r[2]) / 2)
eq("probability_formula", pz, (5 + 3 * cosq) / 8)
eq("q_i_probability", pz.subs(Q, I), sp.Rational(5, 8))
eq("q_minus_1_probability", pz.subs(Q, -1), sp.Rational(1, 4))

# 2. Pełny proces w logicznych modułach S,E,R,B,O.
# E jest wewnętrznym partnerem przygotowania. S nie ma wybranego stanu czystego.
# R i B niosą pojedyncze wyniki; O zapisuje ich różnicę (XOR).
initial = (vec("00000") + vec("11000")) / sp.sqrt(2)
eq("initial_S_is_maximally_mixed", reduced_pure(initial, [0], 5), sp.eye(2) / 2)
H = (X + Z) / sp.sqrt(2)
basis = {"z": sp.eye(2), "x": H, "y": H * sp.diag(1, -I)}
processes = {}
final_states = {}
for axis, basis_change in basis.items():
    eq(f"internal_analyzer_{axis}", basis_change.H * Z * basis_change,
       {"x": X, "y": Y, "z": Z}[axis])
    operations = [cnot(0, 2, 5), embed(U, 0, 5), embed(basis_change, 0, 5),
                  cnot(0, 3, 5), cnot(2, 4, 5), cnot(3, 4, 5)]
    states = [initial]
    for j, op in enumerate(operations):
        eq(f"apparatus_{axis}_operation_{j}_unitary", adj(op) * op, sp.eye(32))
        states.append(simp(op * states[-1]))
        eq(f"full_process_{axis}_norm_{j+1}", (adj(states[-1]) * states[-1])[0], 1)
    final = states[-1]
    final_states[axis] = final
    processes[axis] = (operations, states)
    p_r0 = probability(final, {2: 0}, 5)
    eq(f"preparation_record_weight_{axis}", p_r0, sp.Rational(1, 2))
    p = simp(probability(final, {2: 0, 4: 0}, 5) / p_r0)
    eq(f"internal_reader_probability_{axis}", p,
       (1 + r[{"x": 0, "y": 1, "z": 2}[axis]]) / 2)
    eq(f"old_record_and_partner_remain_correlated_{axis}",
       probability(final, {1: 0, 2: 1}, 5) + probability(final, {1: 1, 2: 0}, 5), 0)
    wrong = sum((probability(final, {2: a, 3: b, 4: 1 - (a ^ b)}, 5)
                 for a in [0, 1] for b in [0, 1]), sp.Integer(0))
    eq(f"reader_carries_comparison_{axis}", wrong, 0)
    # Brak warunkowania niesionym przygotowaniem: każdy analizator widzi 1/2.
    eq(f"discard_preparation_record_erases_phase_signal_{axis}",
       probability(final, {3: 0}, 5), sp.Rational(1, 2))
    # Pamięć po przygotowaniu nie znika w żadnym kolejnym zdarzeniu.
    for j, st in enumerate(states[1:], start=1):
        eq(f"record_carried_{axis}_stage_{j}",
           probability(st, {1: 0, 2: 1}, 5) + probability(st, {1: 1, 2: 0}, 5), 0)

# Instrument przygotowania działa dla każdego wejścia o niezerowym wyniku r=0.
a, b = sp.symbols("a b", real=True)
c, d = sp.symbols("c d")
rho = sp.Matrix([[a, c], [d, b]])
eq("preparation_conditional_state_independent_of_input", P0 * rho * P0, a * P0)

# 3. Nieiniektywność lokalnego zapisu; nie jest argumentem o pojemności.
plus = sp.Matrix([1, 1]) / sp.sqrt(2)
plus_i = sp.Matrix([1, I]) / sp.sqrt(2)
record_plus = cnot(0, 1, 2) * K(plus, vec("0"))
record_plus_i = cnot(0, 1, 2) * K(plus_i, vec("0"))
eq("record_of_plus", reduced_pure(record_plus, [1], 2), sp.eye(2) / 2)
eq("record_of_plus_i", reduced_pure(record_plus_i, [1], 2), sp.eye(2) / 2)
eq("joint_records_keep_distinct_phase",
   (adj(record_plus) * record_plus_i)[0], (1 + I) / 2)

# 4. Wewnętrzny zegar: wszystkie więzy propagacji dla całej rodziny q.
# B_n = <n+1| tensor I - <n| tensor V_n, G = sum B_n^dagger B_n.
# Współczynniki historii są równe w wybranej wersji; nie nazywamy ich wyprowadzonymi.
history_probabilities = {}
for axis, (ops, states) in processes.items():
    nclock = len(states)
    history = sp.Matrix.vstack(*states) / sp.sqrt(nclock)
    eq(f"history_normalization_{axis}", (adj(history) * history)[0], 1)
    for j, op in enumerate(ops):
        eq(f"history_constraint_{axis}_{j}", states[j + 1] - op * states[j], sp.zeros(32, 1))
    clock_weight = simp((adj(states[-1]) * states[-1])[0] / nclock)
    joint_r0 = probability(states[-1], {2: 0}, 5) / nclock
    joint_o0_r0 = probability(states[-1], {2: 0, 4: 0}, 5) / nclock
    eq(f"internal_clock_weight_{axis}", clock_weight, sp.Rational(1, 7))
    eq(f"joint_clock_and_preparation_weight_{axis}", joint_r0, sp.Rational(1, 14))
    result = simp(joint_o0_r0 / joint_r0)
    eq(f"clock_conditioned_readout_{axis}", result,
       (1 + r[{"x": 0, "y": 1, "z": 2}[axis]]) / 2)
    history_probabilities[axis] = str(result)

# Dodatkowe sprawdzenie niezależnie z pełnej macierzy G i projektu zdarzenia.
full_clock_results = []
for qvalue in [I, -1]:
    ops, states = processes["z"]
    opsn = [np.array(v.subs(Q, qvalue).evalf(), dtype=complex) for v in ops]
    statesn = [np.array(v.subs(Q, qvalue).evalf(), dtype=complex).reshape(-1) for v in states]
    nclock, dim = len(statesn), len(statesn[0])
    G = np.zeros((nclock * dim, nclock * dim), dtype=complex)
    for j, op in enumerate(opsn):
        left, right = slice(j * dim, (j + 1) * dim), slice((j + 1) * dim, (j + 2) * dim)
        G[left, left] += np.eye(dim)
        G[right, right] += np.eye(dim)
        G[right, left] -= op
        G[left, right] -= op.conj().T
    psi = np.concatenate(statesn) / np.sqrt(nclock)
    close(f"full_G_annihilates_history_q_{qvalue}", np.linalg.norm(G @ psi))
    close(f"full_G_Hermitian_q_{qvalue}", np.linalg.norm(G - G.conj().T))
    ev = np.linalg.eigvalsh(G)
    close(f"full_G_positive_q_{qvalue}", max(0.0, -float(ev.min())))
    cumulative = [np.eye(dim, dtype=complex)]
    for op in opsn:
        cumulative.append(op @ cumulative[-1])
    history_isometry = np.vstack(cumulative) / np.sqrt(nclock)
    physical_projector = history_isometry @ history_isometry.conj().T
    close(f"G_annihilates_all_allowed_inputs_q_{qvalue}", np.linalg.norm(G @ history_isometry))
    close(f"physical_projector_idempotent_q_{qvalue}",
          np.linalg.norm(physical_projector @ physical_projector - physical_projector))
    numerator = denominator = 0.0
    event_diagonal = np.zeros(nclock * dim)
    for idx, amp in enumerate(psi):
        clock, word = divmod(idx, dim)
        if clock == 6 and ((word >> 2) & 1) == 0:
            denominator += abs(amp)**2
            if (word & 1) == 0:
                numerator += abs(amp)**2
                event_diagonal[idx] = 1
    expected = float(sp.re(pz.subs(Q, qvalue)))
    close(f"full_matrix_readout_q_{qvalue}", abs(numerator / denominator - expected))
    # Efekt komutujący z więzem daje to samo prawdopodobieństwo na historii.
    stationary_effect = (physical_projector * event_diagonal) @ physical_projector
    close(f"stationary_event_commutes_with_constraint_q_{qvalue}",
          np.linalg.norm(G @ stationary_effect - stationary_effect @ G))
    close(f"stationary_event_same_readout_q_{qvalue}",
          abs(np.vdot(psi, stationary_effect @ psi) - numerator))
    full_clock_results.append({"q": str(qvalue), "dimension": nclock * dim,
                               "p": numerator / denominator,
                               "probability_clock_and_record": denominator,
                               "smallest_G_eigenvalue": float(ev.min())})

# 5. Dołączenie rzeczywistego zapisu kanału singlet/tryplet zmienia interferencję.
# <e_s|e_t> = mu, dla rzeczywistego 0 <= mu <= 1. To jawna rodzina aparatu.
beta = sp.Symbol("beta", real=True)
mu = sp.cos(beta)
tag_rotation = sp.Matrix([[sp.cos(beta), -sp.sin(beta)], [sp.sin(beta), sp.cos(beta)]])
tag_unitary = K(ps, sp.eye(2)) + K(pt, tag_rotation)
eq("channel_tag_unitary", simp(tag_unitary.H * tag_unitary), sp.eye(4))
tagged = simp(tag_unitary * K(state, vec("0")))
eq("tagged_global_norm", (adj(tagged) * tagged)[0], 1)
# Liczymy p projekcji S na |0>, zachowując obie amplitudy znacznika.
p_tag = simp(sum(sp.conjugate(tagged[j]).subs(sp.conjugate(Q), 1/Q) * tagged[j]
                 for j in [0, 1]))
eq("record_controls_interference_weight", p_tag, (5 + 3 * mu * cosq) / 8)
eq("coherent_record_limit", p_tag.subs(beta, 0), pz)
eq("distinguishable_channel_record_erases_local_phase", p_tag.subs(beta, sp.pi / 2), sp.Rational(5, 8))
tagged_rho = reduced_pure(tagged, [0], 2)
tagged_r = [simp(sp.trace(tagged_rho * p)) for p in [X, Y, Z]]
eq("record_overlap_controls_Bloch_length", sum(a**2 for a in tagged_r), (1 + 3 * mu**2) / 4)
eq("record_overlap_controls_complementary_uncertainty",
   sum(1 - a**2 for a in tagged_r), (11 - 3 * mu**2) / 4)

# 6. Kontrole negatywne: aparat i wagi nie są dowolnymi dodatkami.
tampered = sp.Matrix([state[0], 2 * state[1]])
badnorm = simp((adj(tampered) * tampered)[0])
eq("double_transition_weight_breaks_norm_q_i", badnorm.subs(Q, I), sp.Rational(17, 8))
broken_ops = list(processes["z"][0])
broken_ops[3] = sp.eye(32)  # Usunięcie zapisu nowego wyniku przy pozostawieniu czytającego.
broken = initial
for op in broken_ops:
    broken = simp(op * broken)
eq("missing_new_record_gives_false_constant_answer",
   probability(broken, {2: 0, 4: 0}, 5) / probability(broken, {2: 0}, 5), 1)

# 7. Spójność wag historii także nie wybiera fazy: dowolne niezerowe a_n.
# B_n^a = <n+1|/a_(n+1) tensor I - <n|/a_n tensor V_n.
weights = [sp.Rational(x) for x in [1, 2, 3, 1, 2, 1, 3]]
ops, states = processes["z"]
weighted_norm = sum(a**2 for a in weights)
weighted = sp.Matrix.vstack(*[a * st for a, st in zip(weights, states)]) / sp.sqrt(weighted_norm)
eq("weighted_clock_history_normalized", (adj(weighted) * weighted)[0], 1)
for j, op in enumerate(ops):
    eq(f"weighted_clock_constraint_{j}",
       weights[j + 1] * states[j + 1] / weights[j + 1]
       - op * (weights[j] * states[j]) / weights[j], sp.zeros(32, 1))
eq("conditional_probability_independent_of_clock_weight",
   probability(weights[-1] * states[-1], {2: 0, 4: 0}, 5)
   / probability(weights[-1] * states[-1], {2: 0}, 5), pz)

report = {
    "date": "2026-10-12", "status": "PASS",
    "scope": "Wybrany sektor relacyjnego procesu kwantowego; nie pełna rama R1a–R1c ani wybór prawa faz.",
    "exact_family": "q on unit circle, no phase sampling used for symbolic claims",
    "probability": "p(O=0|C=6,R=0) = (5+3 cos(theta))/8",
    "tagged_probability": "p = (5+3 mu cos(theta))/8; mu is overlap of actual channel records",
    "conditional_bloch": ["sqrt(3)(1-cos(theta))/4", "sqrt(3)sin(theta)/2", "(1+3cos(theta))/4"],
    "phase_reconstruction": "q=(4 r_z-1)/3 + 2i r_y/sqrt(3)",
    "history_probabilities": history_probabilities,
    "full_clock_results": full_clock_results,
    "counts": {kind: sum(c["method"] == kind for c in checks) for kind in ["exact", "numeric"]},
    "checks": checks,
}
path = ROOT / "test-domkniecia-2026-10-12.json"
path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: report[k] for k in ["status", "scope", "probability", "tagged_probability", "counts", "full_clock_results"]}, ensure_ascii=False, indent=2))
