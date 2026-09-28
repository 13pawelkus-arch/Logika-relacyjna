#!/bin/bash
# start.sh — hook SessionStart: krótkie przypomnienie, jak pracujemy (CLAUDE.md, „Jak pracujemy”). Doinstalowuje numpy.
wejscie=$(cat)
zrodlo=$(printf '%s' "$wejscie" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("source",""))' 2>/dev/null)
python3 -c 'import numpy' 2>/dev/null || pip install -q numpy >/dev/null 2>&1
if [ "$zrodlo" = "compact" ]; then
cat <<'TXT'
LOGIKA RELACYJNA — po kompresji kontekstu: wrócić do definicji czasu i wyprowadzenia wymiarów
(python3 narzedzia/rama.py 2 i 3 — R1a, R1b, R1c) oraz do fragmentów pliku i rozmów związanych z bieżącym krokiem.
Całości nie trzeba czytać od nowa. Zasady: CLAUDE.md, „Jak pracujemy”.
TXT
elif [ "$zrodlo" != "resume" ]; then
cat <<'TXT'
LOGIKA RELACYJNA — nowa sesja: raz, na początku, plik główny w całości (python3 narzedzia/rama.py plik — liczba
kawałków; python3 narzedzia/rama.py plik K — po kolei). Rozmowy i poprawki.md tylko jako konkretne odniesienie
przed danym krokiem, w pełnym tekście (narzedzia/wypowiedzi.py). Potem stan: „Gdzie skończyliśmy” w CLAUDE.md.
Zasady: CLAUDE.md, „Jak pracujemy”.
TXT
fi
