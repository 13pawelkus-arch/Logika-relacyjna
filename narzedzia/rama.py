# rama.py — wypisuje ramę z PLIKU (nie ze streszczenia w CLAUDE.md), w czterech częściach mieszczących się
# w jednym wyniku narzędzia. Czytać w całości na starcie sesji i po każdej kompresji kontekstu.
#
#   python3 narzedzia/rama.py 1   Jak czytać, Cel, Przed liczeniem, pułapki, Dopuszczalne stany, Gdzie zaczynać,
#                                 A0, A1, Sito, Reguła językowa, Sztuki czy miara, Reguły
#   python3 narzedzia/rama.py 2   R1a — definicja czasu (łańcuch Ø)
#   python3 narzedzia/rama.py 3   R1b + R1c — 3D z definicji czasu; most do światła
#   python3 narzedzia/rama.py 4   wypowiedzi użytkownika o czasie, 3D i świetle (rozmowa źródłowa, [n])
#
# Na starcie i po kompresji CAŁY plik główny i WSZYSTKIE wypowiedzi użytkownika (26.09, użytkownik: „Wystarczyło
# czytać plik główny i rozmowy na początku + na bieżąco. To nie jest tanie, ale jak widać konieczne.”), kawałkami
# po ~24 tys. znaków (Read ucina długie linie):
#   python3 narzedzia/rama.py plik          liczba kawałków pliku głównego i wypowiedzi
#   python3 narzedzia/rama.py plik K        kawałek K pliku głównego (K = 1…N), po kolei
#   python3 narzedzia/rama.py rozmowy K     kawałek K wypowiedzi użytkownika ze wszystkich zapisów (rozmowa źródłowa
#                                           pierwsza; bez powtórzeń i bez streszczeń kompresji wklejonych jako wiadomość)
#
# Sekcje wybierane po nagłówkach, nie po numerach linii (plik rośnie). Znacznik przeczytania: /tmp/logika-rama/.
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wypowiedzi import PLIKI as ZAPISY, wiadomosci

KAT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLIK = os.path.join(KAT, 'logika-relacyjna-v3.5.md')
ROZMOWA = os.path.join(KAT, 'rozmowa', 'logika-relacyjna-rozmowa.md')
ZNACZNIKI = '/tmp/logika-rama'

CZESCI = {
    '1': ['## Jak czytać', '## Cel', '## Przed liczeniem', '## Sześć pułapek', '## Dopuszczalne stany',
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


def kawalki_rozmow():
    widziane, czesci = set(), []
    for f in ZAPISY:
        for n, nagl, tresc in wiadomosci(f):
            if not tresc or tresc in widziane or tresc.startswith('This session is being continued'):
                continue
            widziane.add(tresc)
            czesci.append(f'=== {os.path.basename(f)} {nagl}\n{tresc}')
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
    if cz in ('plik', 'rozmowy'):
        if len(sys.argv) < 3:
            sys.exit(f'plik główny: {len(kawalki_pliku())} kawałków (rama.py plik K); '
                     f'wypowiedzi: {len(kawalki_rozmow())} kawałków (rama.py rozmowy K)')
        kaw = kawalki_pliku() if cz == 'plik' else kawalki_rozmow()
        k = int(sys.argv[2])
        a, b, s = kaw[k - 1]
        print(f'=== {cz} {k}/{len(kaw)} (linie {a}–{b})\n{s}')
        os.makedirs(ZNACZNIKI, exist_ok=True)
        open(os.path.join(ZNACZNIKI, f'{cz}{k}'), 'w').close()
        sys.exit()
    if cz in CZESCI:
        tekst = sekcje(CZESCI[cz])
    elif cz == '4':
        tekst = ('# Wypowiedzi użytkownika [H] o czasie, 3D i świetle (rozmowa źródłowa). To jest rama; '
                 'plik ją zapisuje, CLAUDE.md tylko streszcza.\n\n' + wypowiedzi(NR_4))
    else:
        sys.exit('użycie: python3 narzedzia/rama.py 1|2|3|4 | plik [K] | rozmowy K')
    print(tekst)
    if len(tekst) > 28000:
        print(f'\n!!! część {cz} ma {len(tekst)} znaków — wynik narzędzia może być ucięty; podzielić część w rama.py.')
    os.makedirs(ZNACZNIKI, exist_ok=True)
    open(os.path.join(ZNACZNIKI, f'czesc{cz}'), 'w').close()
