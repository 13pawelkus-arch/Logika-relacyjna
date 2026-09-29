#!/bin/bash
# start.sh — hook SessionStart. Pierwsza rzecz w każdej sesji: STOP.md (5 tys. znaków, 1% pliku głównego).
# Powód: opis ramy działa na wiedzę, a błąd jest odruchem; sam plik główny jest za duży, żeby czytać go
# przed każdym krokiem, a zapisy sesji są jeszcze większe. Doinstalowuje numpy.
wejscie=$(cat)
zrodlo=$(printf '%s' "$wejscie" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("source",""))' 2>/dev/null)
python3 -c 'import numpy' 2>/dev/null || pip install -q numpy >/dev/null 2>&1

echo "LOGIKA RELACYJNA — NAJPIERW: cat STOP.md (krótkie; pięć punktów, czym to się różni od standardowego"
echo "podejścia, lista zamkniętych gałęzi, trzy pytania przed rachunkiem). Bez tego reszta nie ma sensu."
echo

if [ "$zrodlo" = "compact" ]; then
cat <<'TXT'
Po kompresji kontekstu: STOP.md, potem definicja czasu i wyprowadzenie wymiarów razem
(python3 narzedzia/rama.py 2 i 3 — R1a, R1b, R1c) oraz fragmenty pliku i rozmów związane z bieżącym krokiem.
Całości nie trzeba czytać od nowa. Zasady: CLAUDE.md, „Jak pracujemy”.
TXT
elif [ "$zrodlo" != "resume" ]; then
cat <<'TXT'
Nowa sesja: STOP.md, potem raz plik główny w całości (python3 narzedzia/rama.py plik — liczba kawałków;
python3 narzedzia/rama.py plik K — po kolei). Rozmowy i poprawki.md jako konkretne odniesienie przed danym
krokiem (narzedzia/wypowiedzi.py); zapisy sesji są WIĘKSZE od pliku głównego, więc nie czytać ich w całości.
Potem stan: „Gdzie skończyliśmy” w CLAUDE.md.
TXT
else
cat <<'TXT'
Wznowiona sesja: STOP.md przed pierwszym rachunkiem i przed pierwszym wpisem do pliku.
TXT
fi
