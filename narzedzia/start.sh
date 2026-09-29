#!/bin/bash
# start.sh — hook SessionStart.
#
# POWÓD (29.09.2026, poprawka 192 — poprawia 188).
# Obserwacja użytkownika: „Jak wezmę ten plik i wkleję go po prostu do osobnego czatu, to działa zupełnie
# inaczej, niż jak go czytasz z repo.” To są dane z zewnątrz. Moje wyjaśnienie („wyjście hooka ma ten sam
# status co wiadomość użytkownika”) było niesprawdzalną dorobioną historią — WYCOFANE.
# Sprawdzalny powód, który zostaje, nie wymaga żadnej tezy o statusie: treść obecna ZANIM postawię pytanie
# może to pytanie ukształtować; treść pobrana PO jest już przefiltrowana przez pytanie — idę po to, co pasuje.
# MIARA (29.09): poprzednia wersja wypisywała 49 599 znaków, a do kontekstu weszło 2 KB podglądu i ścieżka
# do pliku. Czyli 44 KB ramy nie dochodziło wcale. Dlatego hook wypisuje teraz tylko STOP.md (~5,7 tys.
# znaków) — to, co faktycznie dochodzi. Reszta ramy: fragmentami, przy konkretnym kroku.
# Jeśli STOP.md urośnie na tyle, że wyjście zacznie być obcinane, hook przestanie działać — to jest jedyny
# sprawdzalny powód, żeby go trzymać krótko.
wejscie=$(cat)
zrodlo=$(printf '%s' "$wejscie" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("source",""))' 2>/dev/null)
python3 -c 'import numpy' 2>/dev/null || pip install -q numpy >/dev/null 2>&1
cd "$CLAUDE_PROJECT_DIR" || exit 0

cat STOP.md
echo
echo "=============================================================================="
echo "Rama (443 tys. znaków): fragmentami, przy konkretnym kroku — nie w całości i nie na zapas."
echo "  filtr podstawowy, gdy krok tego wymaga:  python3 narzedzia/rama.py 2   (czas)   3  (3D)"
echo "  sekcja po nazwie:                        grep -n '^## R1c' logika-relacyjna-v3.5.md"
echo "  wypowiedzi użytkownika na temat:         python3 narzedzia/wypowiedzi.py 'regex' --wymiana"
echo "=============================================================================="
echo

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
