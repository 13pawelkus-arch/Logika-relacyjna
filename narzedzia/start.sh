#!/bin/bash
# start.sh — hook SessionStart. Na starcie, po /clear i po kompresji kontekstu kasuje znaczniki przeczytania
# ramy (rama znika z kontekstu razem z rozmową); przy wznowieniu zostawia. Doinstalowuje numpy, jeśli brak.
wejscie=$(cat)
zrodlo=$(printf '%s' "$wejscie" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("source",""))' 2>/dev/null)
mkdir -p /tmp/logika-rama
[ "$zrodlo" != "resume" ] && rm -f /tmp/logika-rama/czesc* /tmp/logika-rama/plik* /tmp/logika-rama/rozmowy* /tmp/logika-rama/filtr_zgloszone
git -C "$CLAUDE_PROJECT_DIR" rev-parse HEAD > /tmp/logika-rama/head 2>/dev/null
python3 -c 'import numpy' 2>/dev/null || pip install -q numpy >/dev/null 2>&1
cat <<'TXT'
LOGIKA RELACYJNA — PROTOKÓŁ STARTU (hook SessionStart; szczegóły i powód: CLAUDE.md, sekcja PROTOKÓŁ).
Pierwsze działanie sesji, przed jakąkolwiek odpowiedzią merytoryczną — CAŁY plik główny, po kolei, w całości:
  python3 narzedzia/rama.py plik          (liczba kawałków)
  python3 narzedzia/rama.py plik K        (K = 1…N)
Rozmowy — przy każdej wątpliwości, całe wymiany (wypowiedź + odpowiedź): python3 narzedzia/wypowiedzi.py 'REGEX',
  python3 narzedzia/wypowiedzi.py --nr N --wymiana. Kody rachunków: skrypty/.
Użytkownik (26.09): „Proponuję czytać sam plik, a rozmowy w razie wątpliwości niech służą… Plik główny jest ich
bieżącym zapisem od samego początku. Poszerzony o obliczenia.” „Filtr podstawowy to definicja czasu i powstawanie
wymiarów” — R1a–R1c; §E, Reguły.
Potem stan: sekcja „Gdzie skończyliśmy” w CLAUDE.md i ostatnie wiersze rejestru §E w pliku.
CLAUDE.md to indeks i protokół, NIE rama. Streszczenie nie zastępuje pliku ani wypowiedzi użytkownika.
TXT
