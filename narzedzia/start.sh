#!/bin/bash
# start.sh — hook SessionStart.
#
# POWÓD (29.09.2026, użytkownik): „Jak wezmę ten plik i wkleję go po prostu do osobnego czatu, to działa
# zupełnie inaczej, niż jak go czytasz z repo.” Mechanizm: tekst wklejony przez użytkownika ma status
# „to, czego trzymam się w pracy”, a tekst zwrócony przez narzędzie — status „dane do przejrzenia”.
# Wyjście tego hooka wchodzi do kontekstu jako komunikat systemowy, czyli z tym pierwszym statusem.
# Dlatego hook nie mówi, co przeczytać — podaje treść: STOP.md oraz z pliku głównego słownik skrótów,
# R1a, R1b, R1c, A2 (tablica przekładu) i osiem pułapek nazewniczych. To jest filtr, nie materiał:
# ~43 tys. znaków = 10% pliku; czytanie całości przez rama.py to ~120 tys. tokenów i niższy status.
# Treść jest wyciągana z plików w locie, żeby istniała w jednym egzemplarzu i nie mogła się rozjechać.
wejscie=$(cat)
zrodlo=$(printf '%s' "$wejscie" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("source",""))' 2>/dev/null)
python3 -c 'import numpy' 2>/dev/null || pip install -q numpy >/dev/null 2>&1
cd "$CLAUDE_PROJECT_DIR" || exit 0

cat STOP.md
echo
echo "=============================================================================="
echo "PONIŻEJ, z logika-relacyjna-v3.5.md, w pełnym brzmieniu — to jest filtr, nie materiał:"
echo "  1. słownik skrótów — jednoznaczny odczyt tego, co w literaturze znaczy co innego;"
echo "  2. R1a — definicja czasu, łańcuch nierozróżnialności Ø, granice Ø;"
echo "  3. R1b — wyprowadzenie 3D, razem z czasem i nigdy osobno, oraz dlaczego nie inaczej;"
echo "  4. R1c — most do światła i porządku przyczynowego;"
echo "  5. A2 — tablica przekładu: przekształcenia na postać bezwymiarową, bez metrów i sekund;"
echo "  6. osiem pułapek nazewniczych — miejsca, w których błąd wchodzi przez nazwę."
echo "Reszta pliku (443 tys. znaków) to materiał: fragmentami, przy konkretnym kroku."
echo "=============================================================================="
echo
python3 - <<'PY'
t = open('logika-relacyjna-v3.5.md', encoding='utf-8').read()
def sek(a, b):
    i = t.index(a)
    return t[i:t.index(b, i)]
print(sek('## Jak czytać ten plik', '## R1a.'))
print(sek('## R1a. Łańcuch Ø', '## R1b.'))
print(sek('## R1b. Trzy wymiary', '## R1c.'))
print(sek('## R1c. Most R1b', '## R1d.'))
print(sek('## A2. Tablica przekładu', '## A3. Ø'))
print(sek('## Osiem pułapek nazewniczych', '## Dopuszczalne stany'))
PY

echo "=============================================================================="
if [ "$zrodlo" = "compact" ]; then
  echo "Po kompresji kontekstu: powyższe wystarcza. Fragmenty pliku i rozmów — tylko do bieżącego kroku."
elif [ "$zrodlo" = "resume" ]; then
  echo "Sesja wznowiona. STOP.md obowiązuje przed każdym rachunkiem i każdym wpisem."
else
  echo "Nowa sesja. Reszta pliku głównego (443 tys. znaków) — NIE w całości: fragmentami, przy konkretnym"
  echo "kroku, tak samo jak rozmowy (grep, narzedzia/wypowiedzi.py). Stan: „Gdzie skończyliśmy” w CLAUDE.md,"
  echo "ostatnie wiersze rejestru w poprawki.md."
fi
