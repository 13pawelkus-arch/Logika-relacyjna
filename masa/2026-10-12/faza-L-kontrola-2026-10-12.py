#!/usr/bin/env python3
"""Faza a L: dokładny test pełnych instrumentów i wspólnych korelacji.

Python >=3.10, sympy. Nie importuje ani nie wykonuje poprzedniej kontroli.
L to długość obsadzonego odcinka drabiny; k to odstęp energii badanego S.
"""
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parent
checks = []
q, z = s.symbols('q z', complex=True, zero=False)
unit_symbols = [q, z]
K = s.kronecker_product
I2 = s.eye(2)
X = s.Matrix([[0, 1], [1, 0]])
Z = s.diag(1, -1)
P0, P1 = s.diag(1, 0), s.diag(0, 1)
F = s.Matrix([[s.Rational(1,2), s.sqrt(3)/2],
              [-s.sqrt(3)/2, s.Rational(1,2)]])
V = K(P0, I2) + K(P1, X)
VE = s.simplify(K(F.H, I2) * V * K(F, I2))
ZE = s.simplify(F.H * Z * F)
Zd = s.diag(ZE[0,0], ZE[1,1])


def sim(x):
    return x.applyfunc(s.simplify) if isinstance(x, s.MatrixBase) else s.simplify(x)


def adj(x):
    return x.conjugate().T.subs({s.conjugate(a):1/a for a in unit_symbols})


def eq(name, actual, expected):
    delta = sim(actual - expected)
    zero = s.zeros(*delta.shape) if isinstance(delta, s.MatrixBase) else 0
    ok = delta == zero
    checks.append({'name':name, 'method':'exact', 'pass':bool(ok)})
    if not ok:
        raise AssertionError(f'{name}: {delta}')


def phase_effect(c):
    return (I2 + Zd + s.Matrix([[0,ZE[0,1]*s.conjugate(c)],
                                [ZE[1,0]*c,0]]))/2


def ladder(L, k):
    """Unitarna dylatacja na S,A,R w sektorach energii k*s+n."""
    N = L + 2*k
    W = s.zeros(4*N)
    ix = lambda ss, nn, rr: (ss*N+nn)*2+rr
    for total in range(k, N):
        pos = [ix(0,total,0), ix(0,total,1),
               ix(1,total-k,0), ix(1,total-k,1)]
        for i in range(4):
            for j in range(4):
                W[pos[i],pos[j]] = VE[i,j]
    for n in range(k):
        for r in [0,1]:
            W[ix(0,n,r),ix(0,n,r)] = 1
    for n in range(N-k,N):
        for r in [0,1]:
            W[ix(1,n,1-r),ix(1,n,r)] = 1
    H = s.diag(*[k*ss+n for ss in [0,1] for n in range(N) for r in [0,1]])
    tag = f'L{L}_k{k}'
    eq(f'unitarity_{tag}', W.H*W, s.eye(4*N))
    eq(f'energy_conservation_{tag}', W*H-H*W, s.zeros(4*N))
    pos0 = [ix(ss,n,0) for ss in [0,1] for n in range(N)]
    pos1 = [ix(ss,n,1) for ss in [0,1] for n in range(N)]
    M0, M1 = W.extract(pos0,pos0), W.extract(pos1,pos0)
    eq(f'complete_instrument_{tag}', M0.H*M0+M1.H*M1, s.eye(2*N))
    eq(f'outcome_projector_{tag}', M0.H*M0, M0)
    return {'L':L, 'k':k, 'N':N, 'M0':M0, 'support':list(range(k,k+L))}


def shift(N, k):
    out = s.zeros(N)
    for n in range(k,N):
        out[n-k,n] = 1
    return out


def ref(model, profile=None, phase=1):
    L, N = model['L'], model['N']
    profile = profile if profile is not None else [1/s.sqrt(L)]*L
    out = s.zeros(N,1)
    for a,n in zip(profile,model['support']):
        out[n] = a*phase**n
    return out


def effect_from_model(model, state):
    N, M0 = model['N'], model['M0']
    amplitude = M0*K(I2,state)
    effects, post = s.zeros(2), s.zeros(2)
    for n in range(N):
        op = amplitude.extract([n,N+n],[0,1])
        effects += adj(op)*op
        post += op*(I2/2)*adj(op)
    return sim(effects), sim(post)


models = {key:ladder(*key) for key in
          [(1,1),(2,1),(3,1),(4,1),(8,1),(1,2),(2,2),(3,2),(4,2),
           (2,3),(3,3),(4,3)]}
single = []
for (L,k), model in models.items():
    state = ref(model,phase=z)
    T = shift(model['N'],k)
    c = sim((adj(state)*T*state)[0])
    gamma = s.Rational(max(L-k,0),L)
    eq(f'uniform_overlap_L{L}_k{k}', c, gamma*z**k)
    effect, post = effect_from_model(model,state)
    expected = phase_effect(c).subs(s.conjugate(z),1/z)
    eq(f'full_instrument_phase_effect_L{L}_k{k}',effect,expected)
    eq(f'full_conditional_preparation_L{L}_k{k}',2*post,expected)
    eq(f'preparation_probability_L{L}_k{k}',s.trace(post),s.Rational(1,2))
    single.append({'L':L,'k':k,'overlap':str(c),'phase_signal':L>k})


def on_second(op, Np, No):
    out = s.zeros(2*Np*No)
    for ss in [0,1]:
        for tt in [0,1]:
            for p in range(Np):
                for o in range(No):
                    for oo in range(No):
                        out[(ss*Np+p)*No+o,(tt*Np+p)*No+oo] = op[ss*No+o,tt*No+oo]
    return out


def pair_operator(Lp, Lo, k):
    """Pełny efekt po dwóch zapisach; nie przyjmuje stanu iloczynowego A_p,A_o."""
    mp, mo = models[Lp,k], models[Lo,k]
    Np, No = mp['N'], mo['N']
    D = Np*No
    Prep = K(mp['M0'],s.eye(No))
    Read = on_second(mo['M0'],Np,No)
    U = K(s.diag(1,q),s.eye(D))
    A = Read*U*Prep
    full_effect = adj(A)*A
    # Wstępny stan S = I/2. Warunek R=0 ma prawdopodobieństwo 1/2,
    # dlatego oba czynniki 1/2 skracają się we wspólnym odczycie.
    traced = full_effect[:D,:D]+full_effect[D:,D:]
    prep_effect = Prep.H*Prep
    prep_traced = (prep_effect[:D,:D]+prep_effect[D:,D:])/2
    positions = [p*No+o for p in mp['support'] for o in mo['support']]
    eq(f'joint_prep_probability_L{Lp}_{Lo}_k{k}',
       prep_traced.extract(positions,positions),s.eye(Lp*Lo)/2)
    Tp, To = shift(Np,k), shift(No,k)
    transfer = K(Tp,To.H)
    expected = s.Rational(5,8)*s.eye(D)+s.Rational(3,16)*(q*transfer+transfer.H/q)
    eq(f'operator_identity_for_all_joint_states_L{Lp}_{Lo}_k{k}',
       traced.extract(positions,positions),expected.extract(positions,positions))
    HA = s.diag(*[p+o for p in range(Np) for o in range(No)])
    eq(f'transfer_has_zero_total_energy_mode_L{Lp}_{Lo}_k{k}',
       transfer*HA-HA*transfer,s.zeros(D))
    reduced_transfer = transfer.extract(positions,positions)
    return {'mp':mp, 'mo':mo, 'effect':sim(traced.extract(positions,positions)),
            'transfer':reduced_transfer}


pairs = {key:pair_operator(*key) for key in
         [(1,3,1),(2,2,1),(2,3,1),(3,3,1),(2,3,2),(3,3,2),(3,4,3)]}


def restricted_profile(profile, phase=1, k=1):
    return s.Matrix([a*phase**(j+k) for j,a in enumerate(profile)])


def check_joint_case(name, pair, rho, expected_c):
    eq(f'normalized_{name}',s.trace(rho),1)
    c = sim(s.trace(pair['transfer']*rho))
    eq(f'relational_correlator_{name}',c,expected_c)
    p = sim(s.trace(pair['effect']*rho))
    expected = s.Rational(5,8)+s.Rational(3,16)*(q*c+s.conjugate(c)/q)
    expected = expected.subs(s.conjugate(z),1/z)
    eq(f'full_readout_{name}',p,expected)
    return {'case':name,'correlator':str(c),'p_formula':str(p),
            'p_theta0_phase0':str(sim(p.subs({q:1,z:1}))),
            'p_thetapi_phase0':str(sim(p.subs({q:-1,z:1})))}


examples = []
for Lp,Lo,k in pairs:
    pair = pairs[Lp,Lo,k]
    v = K(restricted_profile([1/s.sqrt(Lp)]*Lp,k=k),
          restricted_profile([1/s.sqrt(Lo)]*Lo,k=k))
    c = s.Rational(max(Lp-k,0),Lp)*s.Rational(max(Lo-k,0),Lo)
    examples.append(check_joint_case(f'uniform_L{Lp}_{Lo}_k{k}',pair,v*v.H,c))

# To samo L=3 i rozkład energii, inny profil faz: suma sąsiednich
# koherencji znosi się w wybranym jednolitym instrumencie, lecz drugi mod zostaje.
uniform = [1/s.sqrt(3)]*3
cancel = [1/s.sqrt(3),1/s.sqrt(3),-1/s.sqrt(3)]
optimal = [s.Rational(1,2),1/s.sqrt(2),s.Rational(1,2)]
for k in [1,2]:
    pair = pairs[3,3,k]
    v = K(restricted_profile(cancel,z,k),restricted_profile(cancel,1,k))
    expected = 0 if k==1 else z**2/9
    examples.append(check_joint_case(f'phase_cancellation_L3_k{k}',pair,v*adj(v),expected))
pair = pairs[3,3,1]
v = K(restricted_profile(optimal,z),restricted_profile(optimal))
examples.append(check_joint_case('optimized_same_L3',pair,v*adj(v),z/2))
rho_diag = s.eye(9)/9
examples.append(check_joint_case('dephased_same_L3',pair,rho_diag,0))
energy = s.diag(1,2,3)
for name, profile in [('uniform',uniform),('phase_cancellation',cancel)]:
    v = s.Matrix(profile)
    variance = sim((v.H*energy**2*v)[0]-(v.H*energy*v)[0]**2)
    eq(f'same_energy_variance_{name}',variance,s.Rational(2,3))
eq('same_energy_distribution_after_phase_cancellation',
   s.diag(*[(a*s.conjugate(a)) for a in cancel]),s.eye(3)/3)

# Faza istnieje w relacji obu odniesień o ostrej sumie energii;
# oba lokalne stany są diagonalne i mają zerowy lokalny korelator.
pair = pairs[2,2,1]
v = s.Matrix([0,1,z,0])/s.sqrt(2)  # |1,2>+z|2,1>
rho = v*adj(v)
rp = s.zeros(2)
ro = s.zeros(2)
for a in range(2):
    for b in range(2):
        rp[a,b] = sum(rho[a*2+j,b*2+j] for j in range(2))
        ro[a,b] = sum(rho[j*2+a,j*2+b] for j in range(2))
eq('correlated_reference_local_p_diagonal',rp,I2/2)
eq('correlated_reference_local_o_diagonal',ro,I2/2)
Hjoint = s.diag(2,3,3,4)
eq('correlated_reference_sharp_total_energy',Hjoint*v,3*v)
examples.append(check_joint_case('correlated_refs_local_phase_absent',pair,rho,z/2))
dephased = s.diag(*[rho[j,j] for j in range(4)])
examples.append(check_joint_case('same_correlated_populations_dephased',pair,dephased,0))

# Usunięcie fazy wobec wspólnego zewnętrznego odniesienia pozostawia wynik.
for name, input_rho in [('correlated',rho),
                        ('product_uniform',K(s.ones(2,1),s.ones(2,1))*K(s.ones(2,1),s.ones(2,1)).H/4)]:
    energies = [2,3,3,4]
    twirled = s.Matrix(4,4,lambda a,b:input_rho[a,b] if energies[a]==energies[b] else 0)
    eq(f'global_phase_removed_same_response_{name}',
       s.trace(pair['effect']*twirled),s.trace(pair['effect']*input_rho))

# W tym jednorodnym sektorze brak dopasowanej różnicy energii zabrania
# wymiany między etykietami S, niezależnie od liczby poziomów drabiny.
resonance = []
for delta in [s.Rational(1,2),s.sqrt(2),s.Integer(1),s.Integer(2)]:
    N = 6
    matching = [(n,m) for n in range(N) for m in range(N)
                if sim(n-(delta+m))==0]
    expected = 0 if delta in [s.Rational(1,2),s.sqrt(2)] else N-int(delta)
    eq(f'matched_energy_pairs_gap_{delta}',len(matching),expected)
    resonance.append({'system_gap_in_ladder_steps':str(delta),
                      'matched_pairs':len(matching)})

result = {'status':'PASS','exact_checks':len(checks),'scope':'named additive-energy quantum readout',
          'uniform_references':single,'full_process_examples':examples,
          'energy_matching':resonance,'checks':checks}
out = ROOT/'faza-L-kontrola-2026-10-12.json'
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'output':str(out)},ensure_ascii=False))
