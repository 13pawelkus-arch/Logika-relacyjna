#!/bin/bash
# start.sh — hook SessionStart. Na starcie, po /clear i po kompresji kontekstu kasuje znaczniki przeczytania
# ramy (rama znika z kontekstu razem z rozmową); przy wznowieniu zostawia. Doinstalowuje numpy, jeśli brak.
wejscie=$(cat)
zrodlo=$(printf '%s' "$wejscie" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("source",""))' 2>/dev/null)
mkdir -p /tmp/logika-rama
[ "$zrodlo" != "resume" ] && rm -f /tmp/logika-rama/czesc* /tmp/logika-rama/filtr_zgloszone
git -C "$CLAUDE_PROJECT_DIR" rev-parse HEAD > /tmp/logika-rama/head 2>/dev/null
python3 -c 'import numpy' 2>/dev/null || pip install -q numpy >/dev/null 2>&1
cat <<'TXT'
LOGIKA RELACYJNA — PROTOKÓŁ STARTU (hook SessionStart; szczegóły i powód: CLAUDE.md, sekcja PROTOKÓŁ).
Pierwsze działanie sesji, przed jakąkolwiek odpowiedzią merytoryczną — przeczytać ramę z PLIKU i rozmów, w całości:
  python3 narzedzia/rama.py 1   (Jak czytać, Cel, Przed liczeniem, pułapki, Dopuszczalne stany, Gdzie zaczynać, A0, A1, Sito, Reguły)
  python3 narzedzia/rama.py 2   (R1a — definicja czasu)
  python3 narzedzia/rama.py 3   (R1b + R1c — 3D z definicji czasu, światło)
  python3 narzedzia/rama.py 4   (wypowiedzi użytkownika o czasie, 3D, świetle)
Potem stan: sekcja „Gdzie skończyliśmy” w CLAUDE.md i ostatnie wiersze rejestru §E w pliku.
CLAUDE.md to indeks i protokół, NIE rama. Streszczenie nie zastępuje R1a/R1b ani wypowiedzi użytkownika.
TXT
