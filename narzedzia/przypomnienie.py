# przypomnienie.py — hook UserPromptSubmit: dokleja do każdej wiadomości użytkownika krótki protokół.
# Jeśli cały plik główny i wszystkie wypowiedzi użytkownika nie zostały przeczytane w tej sesji (albo po kompresji
# kontekstu) — mocne przypomnienie z listą brakujących kawałków (26.09: „Wystarczyło czytać plik główny i rozmowy
# na początku + na bieżąco. To nie jest tanie, ale jak widać konieczne.”).
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rama import kawalki_pliku, kawalki_rozmow

try: json.load(sys.stdin)
except Exception: pass


def zakresy(nr):
    wynik, i = [], 0
    while i < len(nr):
        j = i
        while j + 1 < len(nr) and nr[j + 1] == nr[j] + 1: j += 1
        wynik.append(f'{nr[i]}' if i == j else f'{nr[i]}–{nr[j]}'); i = j + 1
    return ', '.join(wynik)


brak = []
for nazwa, kaw in (('plik', kawalki_pliku()), ('rozmowy', kawalki_rozmow())):
    nr = [k for k in range(1, len(kaw) + 1) if not os.path.exists(f'/tmp/logika-rama/{nazwa}{k}')]
    if nr: brak.append(f'{nazwa} {zakresy(nr)}')
if brak:
    print('PLIK GŁÓWNY I ROZMOWY NIEPRZECZYTANE w tej sesji / po kompresji (brak: ' + '; '.join(brak) + '). '
          'Zanim odpowiesz merytorycznie: python3 narzedzia/rama.py plik K, potem python3 narzedzia/rama.py rozmowy K '
          '— po kolei, w całości. Użytkownik (26.09): „Wystarczyło czytać plik główny i rozmowy na początku + na '
          'bieżąco. To nie jest tanie, ale jak widać konieczne.”')
print('Protokół (CLAUDE.md): (1) wypowiedzi użytkownika na ten temat — python3 narzedzia/wypowiedzi.py \'REGEX\', '
      'w odpowiedzi podać [n]; (2) co już jest w pliku i rejestrze §E (grep); (3) filtr podstawowy: definicja czasu '
      'razem z wyprowadzeniem 3D (R1a–R1c) — sformułowania i odczyt rachunku; (4) równania z literatury — pełne, '
      'ze źródła, nie z pamięci. „Ok”/„Wpisuj”/„Zaczynaj” = zgoda na treść, nie zwolnienie z (1)–(4).')
