# filtr.py — sprawdza sformułowania wobec definicji czasu (R1a) i 3D (R1b): słowa, które w tym projekcie
# już przemycały kierunek, cechy albo gotową czasoprzestrzeń (rejestr §E: 65, 105, 106, 110, 151, 159, 165).
# To są OSTRZEŻENIA, nie błędy: cytat, negacja („bez „powstawania”") i porządek pracy w pliku są w porządku.
# Każde trafienie w zdaniu MERYTORYCZNYM przeformułować (odczyt zawsze teraz; zapis ostry/rozproszony;
# stosunek dwóch punktów odniesienia zamiast przebiegu).
#
#   python3 narzedzia/filtr.py PLIK            cały plik
#   echo 'tekst' | python3 narzedzia/filtr.py  szkic przed wpisem
#   python3 narzedzia/filtr.py --diff          dodane linie (niezatwierdzone) w pliku głównym i CLAUDE.md
#   python3 narzedzia/filtr.py --hook          tryb hooka PostToolUse (diff + ostatni commit, bez powtórzeń)
import hashlib, json, os, re, subprocess, sys

KAT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLIKI = ['logika-relacyjna-v3.5.md', 'CLAUDE.md']
STAN = '/tmp/logika-rama'

WZORCE = [
    (r'\bpotem\b|\bnastępnie\b', 'kierunek „wcześniej–później” (R1a; poprawki 106, 159, 165)'),
    (r'\b(wcześniej|później)\b', 'kierunek? (w porządku, jeśli o kolejności pracy w pliku)'),
    (r'powsta(je|ją|wa\w*|nie\w*|ł\w*)\b', '„powstawanie” = kierunek (poprawka 159)'),
    (r'początkow\w*|na początku', '„początkowe” — w jednym punkcie odniesienia (poprawka 165)'),
    (r'przepływ\w*|\bpłynie\b|\bupływ\w*', '„przepływ” czasu/informacji (poprawka 159)'),
    (r'ostatni\w* odczyt\w*|\bna końcu\b(?! Plancka)', '„ostatni” / „na końcu” = kierunek (poprawki 138, 159)'),
    (r'zapad\w*|kolaps\w*', 'narracja OTW (A5d: OTW nie mówi o zapadaniu)'),
    (r'zdąż\w*|przyciąg\w*|w podczerwieni|w nadfiolecie|ewolu\w*|dąży\w*', 'przebieg zamiast stosunku stosunków (poprawka 165)'),
    (r'\bw czasie\b|zmienia się w czasie|\bz czasem\b(?! własnym)', 'czas jako zewnętrzny parametr (R1a)'),
    (r'docier\w*|dotrze\w*|\bleci\b|podróż\w*|pokonuj\w*', 'c = przekaz informacji, nie pokonywanie drogi'),
    (r'foton (robi|emituje|wysyła|leci|przenosi)', '„foton robi” (zasada z poprawki 165)'),
    (r'\bcech(a|ą|y|ę|ami|om)?\b|właściwoś\w*|pojęci\w* pierwotn\w*|fundamentaln\w*', '„nic nie jest cechą” [36, 94]'),
    (r'horyzont\w* zdarzeń', 'teleologia (poprawka 159: zostaje brzeg lokalny [460])'),
    (r'jedn\w* relacj\w* między końcami', 'błąd 151: cel = zespół funkcji [94]'),
    (r'problem\w* czasu|Kucha', 'życzenie użytkownika: nie wpisywać [272–276]'),
]


def bez_cytatow(l):
    # cytat i nazwanie błędu („powstaje”, "potem") nie są sformułowaniem — maskowane tą samą długością
    return re.sub(r'„[^”]*”|"[^"]*"', lambda m: ' ' * len(m.group(0)), l)


def sprawdz(linie, zrodlo=''):
    traf = []
    for nr, l0 in linie:
        l = bez_cytatow(l0)
        for wz, pow_ in WZORCE:
            for m in re.finditer(wz, l, re.I):
                a = max(0, m.start() - 60)
                traf.append(f'{zrodlo}{nr}: …{l0[a:m.end() + 60].strip()}…  ⟶ [{m.group(0)}] {pow_}')
    return traf


def dodane(diff):
    wynik, nr, plik = [], 0, ''
    for l in diff.splitlines():
        if l.startswith('+++ '): plik = l[6:] + ':'
        elif l.startswith('@@'):
            nr = int(re.search(r'\+(\d+)', l).group(1))
        elif l.startswith('+'):
            wynik.append((f'{plik}{nr}', l[1:])); nr += 1
        elif not l.startswith('-'): nr += 1
    return wynik


def git(*a):
    return subprocess.run(['git', '-C', KAT, *a], capture_output=True, text=True).stdout


def hook():
    try: json.load(sys.stdin)
    except Exception: pass
    os.makedirs(STAN, exist_ok=True)
    linie = dodane(git('diff', '-U0', '--', *PLIKI))
    head = git('rev-parse', 'HEAD').strip()
    p_head = os.path.join(STAN, 'head')
    stary = open(p_head).read().strip() if os.path.exists(p_head) else head
    if head and stary != head:                    # commit w tym samym wywołaniu co wpis: sprawdzić, co wszedł
        linie += dodane(git('diff', '-U0', stary, head, '--', *PLIKI))
    open(p_head, 'w').write(head)
    traf = sprawdz([(n, l) for n, l in linie], '')
    # każde ostrzeżenie tylko raz na sesję (klucz: treść bez numeru linii)
    p_w = os.path.join(STAN, 'filtr_zgloszone')
    byly = set(open(p_w, encoding='utf-8').read().splitlines()) if os.path.exists(p_w) else set()
    klucz = lambda x: hashlib.sha1(x.split(': ', 1)[-1].encode()).hexdigest()
    traf = [x for x in traf if klucz(x) not in byly]
    if not traf: return 0
    with open(p_w, 'a', encoding='utf-8') as f: f.write(''.join(klucz(x) + '\n' for x in traf))
    print('FILTR (R1a/R1b) — ostrzeżenia w dopisanych liniach. Cytat, negacja i porządek pracy — w porządku; '
          'w zdaniu merytorycznym przeformułować przed commitem (albo poprawić wpis):', file=sys.stderr)
    print('\n'.join(traf[:40]), file=sys.stderr)
    if len(traf) > 40: print(f'… i {len(traf) - 40} więcej: python3 narzedzia/filtr.py --diff', file=sys.stderr)
    return 2


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['--hook']: sys.exit(hook())
    if a[:1] == ['--diff']: t = sprawdz(dodane(git('diff', '-U0', '--', *PLIKI)))
    elif a: t = sprawdz(enumerate(open(a[0], encoding='utf-8').read().splitlines(), 1), a[0] + ':')
    else: t = sprawdz(enumerate(sys.stdin.read().splitlines(), 1))
    print('\n'.join(t) if t else 'filtr: brak ostrzeżeń')
    print(f'--- {len(t)} ostrzeżeń (cytat, negacja, porządek pracy — w porządku)')
