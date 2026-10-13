#!/usr/bin/env python3
"""Punkt 4: idealny zapis, zachowanie energii i skończone odniesienie fazowe.

Wymaga Python >=3.10 i sympy. Wszystkie kontrole są dokładne.
To test jawnego sektora z addytywną energią, nie dowód całej ramy.
"""
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parent
checks = []
q, zp, zm = s.symbols('q zp zm', nonzero=True)
unit_symbols = [q, zp, zm]
I = s.I
K = s.kronecker_product
eye2 = s.eye(2)
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -I], [I, 0]])
Z = s.diag(1, -1)
P0, P1 = s.diag(1, 0), s.diag(0, 1)


def sim(x):
    return x.applyfunc(s.simplify) if isinstance(x, s.MatrixBase) else s.simplify(x)


def adj(x):
    return x.conjugate().T.subs({s.conjugate(t): 1/t for t in unit_symbols})


def eq(name, actual, expected):
    delta = sim(actual - expected)
    ok = delta == (s.zeros(*delta.shape) if isinstance(delta, s.MatrixBase) else 0)
    checks.append({'name': name, 'method': 'exact', 'pass': bool(ok)})
    if not ok:
        raise AssertionError(f'{name}: {delta}')


def ket(n, d):
    x = s.zeros(d, 1)
    x[n] = 1
    return x


V = K(P0, eye2) + K(P1, X)  # CNOT S -> wskaźnik R, baza logiczna
pt = s.Matrix([[3, s.sqrt(3)], [s.sqrt(3), 1]]) / 4
F = s.Matrix([[s.Rational(1, 2), s.sqrt(3)/2],
              [-s.sqrt(3)/2, s.Rational(1, 2)]])  # kolumny: energia 0,1
eq('energy_basis_orthonormal', F.H * F, eye2)
eq('energy_eigenprojector', F.H * pt * F, P1)
ZE = sim(F.H * Z * F)
Zdiag = s.diag(ZE[0, 0], ZE[1, 1])
Zoff = ZE - Zdiag
Zparallel = sim(F * Zdiag * F.H)
eq('parallel_readout_component', Zparallel, s.sqrt(3)*X/4 + Z/4)
VE = sim(K(F.H, eye2) * V * K(F, eye2))

# 1. Żaden hamiltonian samego wskaźnika nie naprawia idealnego CNOT.
epsilon, ax, ay, az = s.symbols('epsilon ax ay az', real=True)
HR = ax*X + ay*Y + az*Z  # składnik I zawsze komutuje
Hadd = K(epsilon*pt, eye2) + K(eye2, HR)
comm = sim(V*Hadd-Hadd*V)
equations = [part for z in comm for part in [s.re(z), s.im(z)] if part != 0]
sol = s.linsolve(equations, (epsilon, ax, ay, az))
if sol != s.FiniteSet((0, ax, 0, 0)):
    raise AssertionError(f'unexpected additive-energy solutions: {sol}')
checks.append({'name':'all_pointer_hamiltonians_solved', 'method':'exact', 'pass':True,
               'solution':str(sol)})
eq('noncommuting_measured_observable', pt*Z-Z*pt, -I*s.sqrt(3)*Y/2)
eq('offdiagonal_energy_witness', pt[0, 1], s.sqrt(3)/4)


def lifted_model(L):
    """S ma energię 0,1; A ma 0,...,L+1; R ma energię zero.

    Kolejność czynników S,A,R. Każdy wewnętrzny sektor k=s+a
    otrzymuje blok VE. Sektory brzegowe otrzymują I_R i X_R.
    Jest to skończony operator unitarny bez cyklicznego zawijania energii.
    """
    N = L + 2
    W = s.zeros(4*N)
    idx = lambda ss, aa, rr: (ss*N+aa)*2+rr
    for total in range(1, N):
        indices = [idx(0, total, 0), idx(0, total, 1),
                   idx(1, total-1, 0), idx(1, total-1, 1)]
        for row in range(4):
            for col in range(4):
                W[indices[row], indices[col]] = VE[row, col]
    for rr in [0, 1]:
        W[idx(0,0,rr),idx(0,0,rr)]=1
        W[idx(1,N-1,1-rr),idx(1,N-1,rr)]=1
    energies = [ss+aa for ss in [0, 1] for aa in range(N) for rr in [0, 1]]
    H = s.diag(*energies)
    eq(f'finite_unitary_L{L}', W.H*W, s.eye(4*N))
    eq(f'exact_energy_conservation_L{L}', W*H-H*W, s.zeros(4*N))
    # Jawne rozłożenie na pary modułów: S-A, S-R, S-A.
    # Każda z trzech operacji osobno zachowuje tę samą energię.
    rotate=s.zeros(2*N)
    for total in range(1,N):
        positions=[total,N+total-1]
        for row in range(2):
            for col in range(2):
                rotate[positions[row],positions[col]]=F[row,col]
    rotate[0,0]=rotate[2*N-1,2*N-1]=1
    Rfull=K(rotate,eye2)
    middle=K(P0,s.eye(N),eye2)+K(P1,s.eye(N),X)
    eq(f'reference_rotation_unitary_L{L}',Rfull.H*Rfull,s.eye(4*N))
    eq(f'reference_rotation_conserves_energy_L{L}',Rfull*H-H*Rfull,s.zeros(4*N))
    eq(f'pointer_copy_conserves_energy_L{L}',middle*H-H*middle,s.zeros(4*N))
    eq(f'pair_module_decomposition_L{L}',Rfull.H*middle*Rfull,W)
    kernels = []
    for outcome in [0, 1]:
        rows = [idx(ss, aa, outcome) for ss in [0, 1] for aa in range(N)]
        cols = [idx(ss, aa, 0) for ss in [0, 1] for aa in range(N)]
        kernels.append(W.extract(rows, cols))
    eq(f'full_instrument_completeness_L{L}',
       sum((v.H*v for v in kernels), s.zeros(2*N)), s.eye(2*N))
    Hsa = s.diag(*[ss+aa for ss in [0, 1] for aa in range(N)])
    for rr, kr in enumerate(kernels):
        eq(f'outcome_energy_conservation_L{L}_r{rr}', kr*Hsa-Hsa*kr, s.zeros(2*N))
    return N, kernels


def reference(L, z=1):
    return s.Matrix([0] + [z**n / s.sqrt(L) for n in range(1,L+1)] + [0])


def finite_instrument(L, z=1):
    N, kernels = models[L]
    chi = reference(L, z)
    inject = K(eye2, chi)
    operators = []
    for kr in kernels:
        A = kr*inject  # A: S -> S,A
        ops = [A.extract([aa, N+aa], [0,1]) for aa in range(N)]
        operators.append(ops)
    return operators


def effective_E0(gamma, z=1):
    return (eye2+Zdiag+gamma*s.Matrix([[0, ZE[0,1]/z],[ZE[1,0]*z, 0]]))/2


models = {L: lifted_model(L) for L in [1,2,3,4,8]}
single_results = []
for L in models:
    gamma = s.Rational(L-1,L)
    ins = finite_instrument(L)
    effect = sim(sum((op.H*op for op in ins[0]), s.zeros(2)))
    expected = effective_E0(gamma)
    eq(f'effect_from_full_unitary_L{L}', effect, expected)
    post0 = sim(sum((op*(eye2/2)*op.H for op in ins[0]), s.zeros(2)))
    eq(f'preparation_outcome_weight_L{L}', s.trace(post0), s.Rational(1,2))
    eq(f'actual_conditional_preparation_L{L}', 2*post0, expected)
    code_effect = sim(F*effect*F.H)
    correct = sim(code_effect[0,0])
    eq(f'correct_binary_record_L{L}', correct, 1-s.Rational(3,8*L))
    bloch_length = sim(2*s.trace(expected**2)-1)
    eq(f'conditional_complementarity_L{L}', bloch_length, (1+3*gamma**2)/4)
    ref = reference(L)
    energy = s.diag(*range(L+2))
    variance = sim((ref.H*energy**2*ref)[0]-(ref.H*energy*ref)[0]**2)
    eq(f'energy_variance_of_named_reference_L{L}', variance, s.Rational(L*L-1,12))
    single_results.append({'L':L,'gamma':str(gamma),'correct_binary_record':str(correct),
                           'energy_variance_in_gap_units':str(variance),
                           'conditional_state_purity':str(sim(s.trace(expected**2)))})

# 2. Uogólnienie odczytu dla dowolnych widoczności i względnych faz.
gp, gm = s.symbols('gamma_p gamma_m', real=True)
U = s.diag(1,q)
p_general = sim(s.trace(effective_E0(gm,zm)*U*effective_E0(gp,zp)*adj(U)))
expected_p = s.Rational(5,8) + s.Rational(3,16)*gp*gm*(q*zp/zm+zm/(q*zp))
eq('general_relational_readout_all_phases', p_general, expected_p)
zcommon = s.Symbol('zcommon', nonzero=True)
eq('common_phase_cancels', p_general.subs({zp:zp*zcommon,zm:zm*zcommon}), p_general)
advance=s.Symbol('advance',nonzero=True)
eq('common_free_advance_of_system_and_readout_reference_cancels',
   p_general.subs({q:advance,zp:1,zm:advance}),s.Rational(5,8)+s.Rational(3,8)*gp*gm)
relative=s.Symbol('relative',nonzero=True)
eq('only_additional_relative_phase_survives_common_free_advance',
   p_general.subs({q:advance*relative,zp:1,zm:advance}),
   s.Rational(5,8)+s.Rational(3,16)*gp*gm*(relative+1/relative))
eq('ideal_reference_limit', p_general.subs({gp:1,gm:1,zp:1,zm:1}),
   (5+3*(q+1/q)/2)/8)
eq('no_reference_coherence_no_phase_signal', p_general.subs(gp,0), s.Rational(5,8))

# Sprawdzenie faz instrumentu bez zakładania wzoru E0.
ins = finite_instrument(3,zp)
Ephase = sim(sum((adj(op)*op for op in ins[0]), s.zeros(2)))
postphase = sim(sum((op*(eye2/2)*adj(op) for op in ins[0]), s.zeros(2)))
eq('phase_dependent_instrument_effect', Ephase, effective_E0(s.Rational(2,3),zp))
eq('phase_dependent_actual_preparation', 2*postphase, Ephase)


def on_second_reference(op, Np, Nm):
    """Operator na S,A_m, osadzony w kolejności S,A_p,A_m."""
    out = s.zeros(2*Np*Nm)
    for ss in [0,1]:
        for tt in [0,1]:
            for ap in range(Np):
                for am in range(Nm):
                    for bm in range(Nm):
                        out[(ss*Np+ap)*Nm+am,(tt*Np+ap)*Nm+bm]=op[ss*Nm+am,tt*Nm+bm]
    return out


def norm(v):
    return sim((adj(v)*v)[0])


# 3. Dwa rzeczywiste zapisy, ze wszystkimi amplitudami odniesień zachowanymi.
pair_results=[]
for Lp,Lm in [(1,1),(2,3),(4,4)]:
    Np,kp=models[Lp]
    Nm,km=models[Lm]
    Prep=K(kp[0],s.eye(Nm))
    Read=on_second_reference(km[0],Np,Nm)
    Um=K(U,s.eye(Np*Nm))
    A=Read*Um*Prep
    dim=2*Np*Nm
    energies=[ss+ap+am for ss in [0,1] for ap in range(Np) for am in range(Nm)]
    H=s.diag(*energies)
    eq(f'joint_process_conserves_energy_L{Lp}_{Lm}', A*H-H*A, s.zeros(dim))
    v=[K(ket(ss,2),reference(Lp),reference(Lm)) for ss in [0,1]]
    preparation_weight=sim(sum(norm(Prep*w) for w in v)/2)
    joint=sim(sum(norm(A*w) for w in v)/2)
    eq(f'joint_preparation_weight_L{Lp}_{Lm}',preparation_weight,s.Rational(1,2))
    gamma_p,gamma_m=s.Rational(Lp-1,Lp),s.Rational(Lm-1,Lm)
    p=sim(joint/preparation_weight)
    eq(f'full_joint_response_L{Lp}_{Lm}',p,
       expected_p.subs({gp:gamma_p,gm:gamma_m,zp:1,zm:1}))
    # Dokładna dekoherencja wyłącznie MIĘDZY CAŁKOWITYMI sektorami energii.
    # Zachowuje wewnętrzne relacje fazowe; nie dekoheruje odniesień osobno.
    twirled_joint=s.Integer(0)
    twirled_preparation=s.zeros(2)
    for w in v:
        for en in sorted(set(energies)):
            component=s.Matrix([w[j] if energies[j]==en else 0 for j in range(dim)])
            if any(component):
                twirled_joint+=norm(A*component)/2
                prep_component=Prep*component
                coefficient_matrix=s.Matrix(2,Np*Nm,list(prep_component))
                twirled_preparation+=coefficient_matrix*adj(coefficient_matrix)/2
    eq(f'absolute_phase_removed_same_response_L{Lp}_{Lm}',twirled_joint,joint)
    eq(f'local_preparation_without_absolute_phase_L{Lp}_{Lm}',
       twirled_preparation/preparation_weight,effective_E0(0))
    # Te same rozkłady energii, ale usunięta również względna koherencja:
    independently_dephased=s.Integer(0)
    for ss in [0,1]:
        for ap in range(1,Lp+1):
            for am in range(1,Lm+1):
                column=(ss*Np+ap)*Nm+am
                independently_dephased+=norm(A[:,column])/(2*Lp*Lm)
    eq(f'energy_variance_alone_not_enough_L{Lp}_{Lm}',
       independently_dephased/preparation_weight,s.Rational(5,8))
    pair_results.append({'L_preparation':Lp,'L_readout':Lm,'p_q_i':str(p.subs(q,I)),
                         'p_q_minus1':str(p.subs(q,-1)),'p_formula':str(p)})

# Ogólny algebraiczny powód: operator zachowuje sektory energii, więc
# operator efektu również; puryfikacja sumy sektorów daje ostry więz.
# Zapisujemy tylko nierównoważne wartości testowe, nie wywodzimy rodziny z prób.
data={'date':'2026-10-12','status':'PASS','checks_count':len(checks),
      'scope':'Sektor z addytywną zachowaną energią i jawnie określonymi odniesieniami fazowymi.',
      'ideal_pointer_constraint_solution':str(sol),
      'general_response':str(p_general),
      'single_reference_results':single_results,
      'full_process_results':pair_results,
      'checks':checks}
(ROOT/'punkt4-energia-zapis-kontrola-2026-10-12.json').write_text(
    json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:data[key] for key in ['status','checks_count','ideal_pointer_constraint_solution',
      'general_response','single_reference_results','full_process_results']},ensure_ascii=False,indent=2))
