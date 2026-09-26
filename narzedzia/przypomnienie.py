# przypomnienie.py — hook UserPromptSubmit: dokleja do każdej wiadomości użytkownika krótki protokół.
# Jeśli rama nie została przeczytana w tej sesji (albo po kompresji kontekstu) — mocne przypomnienie.
import json, os, sys

try: json.load(sys.stdin)
except Exception: pass
brak = [c for c in '1234' if not os.path.exists(f'/tmp/logika-rama/czesc{c}')]
if brak:
    print('RAMA NIEPRZECZYTANA w tej sesji / po kompresji (brak części ' + ', '.join(brak) + '). Zanim odpowiesz '
          'merytorycznie: python3 narzedzia/rama.py ' + ' ; python3 narzedzia/rama.py '.join(brak) +
          ' — przeczytać w całości. CLAUDE.md to indeks, nie rama (sesja 3: R1a przeczytane dopiero po 25 wymianach).')
print('Protokół (CLAUDE.md): (1) wypowiedzi użytkownika na ten temat — python3 narzedzia/wypowiedzi.py \'REGEX\', '
      'w odpowiedzi podać [n]; (2) co już jest w pliku i rejestrze §E (grep); (3) sformułowania przez R1a/R1b; '
      '(4) równania z literatury — pełne, ze źródła, nie z pamięci. „Ok”/„Wpisuj”/„Zaczynaj” = zgoda na treść, '
      'nie zwolnienie z (1)–(4).')
