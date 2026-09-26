# rama.py — wypisuje ramę z PLIKU (nie ze streszczenia w CLAUDE.md), w czterech częściach mieszczących się
# w jednym wyniku narzędzia. Czytać w całości na starcie sesji i po każdej kompresji kontekstu.
#
#   python3 narzedzia/rama.py 1   Jak czytać, Cel, Przed liczeniem, pułapki, Dopuszczalne stany, Gdzie zaczynać,
#                                 A0, A1, Sito, Reguła językowa, Sztuki czy miara, Reguły
#   python3 narzedzia/rama.py 2   R1a — definicja czasu (łańcuch Ø)
#   python3 narzedzia/rama.py 3   R1b + R1c — 3D z definicji czasu; most do światła
#   python3 narzedzia/rama.py 4   wypowiedzi użytkownika o czasie, 3D i świetle (rozmowa źródłowa, [n])
#
# Sekcje wybierane po nagłówkach, nie po numerach linii (plik rośnie). Znacznik przeczytania: /tmp/logika-rama/.
import os, re, sys

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
    if cz in CZESCI:
        tekst = sekcje(CZESCI[cz])
    elif cz == '4':
        tekst = ('# Wypowiedzi użytkownika [H] o czasie, 3D i świetle (rozmowa źródłowa). To jest rama; '
                 'plik ją zapisuje, CLAUDE.md tylko streszcza.\n\n' + wypowiedzi(NR_4))
    else:
        sys.exit('użycie: python3 narzedzia/rama.py 1|2|3|4')
    print(tekst)
    if len(tekst) > 28000:
        print(f'\n!!! część {cz} ma {len(tekst)} znaków — wynik narzędzia może być ucięty; podzielić część w rama.py.')
    os.makedirs(ZNACZNIKI, exist_ok=True)
    open(os.path.join(ZNACZNIKI, f'czesc{cz}'), 'w').close()
