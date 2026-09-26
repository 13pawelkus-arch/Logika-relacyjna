# rama.py — wypisuje ramę z PLIKU (nie ze streszczenia w CLAUDE.md), w czterech częściach mieszczących się
# w jednym wyniku narzędzia. Definicja czasu i wyprowadzenie wymiarów (2, 3) — do powrotu w każdej chwili.
#
#   python3 narzedzia/rama.py 1   Jak czytać, Cel, Przed liczeniem, pułapki, Dopuszczalne stany, Gdzie zaczynać,
#                                 A0, A1, Sito, Reguła językowa, Sztuki czy miara, Reguły
#   python3 narzedzia/rama.py 2   R1a — definicja czasu (łańcuch Ø)
#   python3 narzedzia/rama.py 3   R1b + R1c — 3D z definicji czasu; most do światła
#   python3 narzedzia/rama.py 4   wypowiedzi użytkownika o czasie, 3D i świetle (rozmowa źródłowa, [n])
#
# Całość — raz na początku nowej sesji (użytkownik, 26.09): plik główny, a po nim wszystkie rozmowy chronologicznie,
# z odpowiedziami asystenta (cały tok rozumowania), bez wywołań narzędzi, bez bloków kodu i bez streszczeń kompresji;
# kawałkami po ~24 tys. znaków (Read ucina długie linie):
#   python3 narzedzia/rama.py calosc        liczba kawałków
#   python3 narzedzia/rama.py calosc K      kawałek K (K = 1…N), po kolei
#   python3 narzedzia/rama.py plik [K]      sam plik główny (np. sprawdzenie całości na końcu sesji)
#
# Sekcje wybierane po nagłówkach, nie po numerach linii (plik rośnie).
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wypowiedzi import wszystkie

KAT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLIK = os.path.join(KAT, 'logika-relacyjna-v3.5.md')
ROZMOWA = os.path.join(KAT, 'rozmowa', 'logika-relacyjna-rozmowa.md')
# rozmowy chronologicznie: źródłowa (16–24.09), sesje CC 24.09, 24/25.09 („rozmowa 2”), 25.09, 26.09, dalsze wg daty
ROZMOWY = [os.path.join(KAT, 'rozmowa', f) for f in (
    'logika-relacyjna-rozmowa.md', 'claude-code-sesja-2026-09-24.md', 'claude-code-sesja-2026-09-24-2.md')]

CZESCI = {
    '1': ['## Jak czytać', '## Cel', '## Przed liczeniem', '## Osiem pułapek', '## Dopuszczalne stany',
          '## Gdzie zaczynać', '## A0.', '## A1.', '## Sito', '## Reguła językowa', '## Sztuki czy miara', '## Reguły'],
    '2': ['## R1a.'],
    '3': ['## R1b.', '## R1c.'],
}
# wypowiedzi użytkownika — numery z CLAUDE.md (czas, pamięć, pseudokierunek, 3D, płaskość, światło, c)
NR_4 = [54, 70, 72, 76, 80, 98, 134, 136, 148, 150, 152, 154, 156, 164, 266, 334, 336, 392, 394, 398, 400, 402,
        422, 424, 426, 482, 488, 491, 493, 511, 543]


def sekcje(prefiksy):
    t = open(PLIK, encoding='utf-8').read()
    kawalki = re.split(r'\n(?=## )', t)
    wynik = []
    for p in prefiksy:
        traf = [k for k in kawalki if k.startswith(p)]
        if not traf:
            wynik.append(f'!!! BRAK SEKCJI „{p}” — nagłówek zmieniony? Poprawić narzedzia/rama.py.')
        wynik += traf
    return '\n\n'.join(wynik)


ROZMIAR = 24000


def kawalki(tekst):
    wynik, cur, n, start = [], [], 0, 1
    linie = tekst.split('\n')
    for i, l in enumerate(linie, 1):
        if n + len(l) > ROZMIAR and cur:
            wynik.append((start, i - 1, '\n'.join(cur))); cur, n, start = [], 0, i
        cur.append(l); n += len(l) + 1
    wynik.append((start, len(linie), '\n'.join(cur)))
    return wynik


def kawalki_pliku():
    return kawalki(open(PLIK, encoding='utf-8').read())


def rozmowy():
    import glob
    reszta = sorted(f for f in glob.glob(os.path.join(KAT, 'rozmowa', '*.md')) if f not in ROZMOWY)
    return ROZMOWY + reszta


def kawalki_calosci():
    czesci = ['# PLIK GŁÓWNY\n\n' + open(PLIK, encoding='utf-8').read()]
    for f in rozmowy():
        czesci.append(f'# ROZMOWA: {os.path.basename(f)}')
        for n, kto, nagl, tresc in wszystkie(f):
            if tresc.startswith('This session is being continued'):
                continue                                        # streszczenie kompresji, nie wypowiedź
            tresc = re.sub(r'(?ms)^(`{3,}).*?^\1[ \t]*$', lambda m: f'[blok kodu: {m.group(0).count(chr(10)) - 1} linii]', tresc)
            czesci.append(f'{nagl}\n{tresc}')
    return kawalki('\n\n'.join(czesci))


def wypowiedzi(numery):
    t = open(ROZMOWA, encoding='utf-8').read()
    wynik = []
    for k in re.split(r'\n(?=## \[\d+\] )', t):
        m = re.match(r'## \[(\d+)\] Użytkownik', k)
        if m and int(m.group(1)) in numery:
            wynik.append(re.sub(r'<details>.*?</details>', '', k, flags=re.S).strip())
    return '\n\n'.join(wynik)


if __name__ == '__main__':
    cz = sys.argv[1] if len(sys.argv) > 1 else ''
    if cz in ('plik', 'calosc'):
        kaw = kawalki_pliku() if cz == 'plik' else kawalki_calosci()
        if len(sys.argv) < 3:
            print(f'{cz}: {len(kaw)} kawałków (rama.py {cz} K)')
            sys.exit(0)
        k = int(sys.argv[2])
        a, b, s = kaw[k - 1]
        print(f'=== {cz} {k}/{len(kaw)}\n{s}')
        sys.exit()
    if cz in CZESCI:
        tekst = sekcje(CZESCI[cz])
    elif cz == '4':
        tekst = ('# Wypowiedzi użytkownika [H] o czasie, 3D i świetle (rozmowa źródłowa).\n\n' + wypowiedzi(NR_4))
    else:
        sys.exit('użycie: python3 narzedzia/rama.py 1|2|3|4 | calosc [K] | plik [K]')
    print(tekst)
    if len(tekst) > 28000:
        print(f'\n!!! część {cz} ma {len(tekst)} znaków — wynik narzędzia może być ucięty; podzielić część w rama.py.')
