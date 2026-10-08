#!/bin/bash
# stop.sh — hook PreToolUse: ściana przed odruchem „jest pytanie → jest rachunek”.
# Przy każdej próbie zapisu w skrypty/ (nowy rachunek) i przy zapisie do pliku głównego
# wypisuje z STOP.md to, co ma zatrzymać: trzy pytania i listę zamkniętych gałęzi.
# Powód: opis ramy działa na wiedzę, a błąd jest odruchem — trzeba go zatrzymać tam, gdzie odpala.
wejscie=$(cat)
sciezka=$(printf '%s' "$wejscie" | python3 -c '
import json, sys
try:
    d = json.load(sys.stdin).get("tool_input", {})
    print(d.get("file_path") or d.get("notebook_path") or "")
except Exception:
    print("")
' 2>/dev/null)

case "$sciezka" in
  */skrypty/*)
    echo "STOP (skrypty/ — nowy rachunek). Zanim napiszesz:"
    sed -n '/^## Trzy pytania/,/^---$/p' "$CLAUDE_PROJECT_DIR/STOP.md" | sed '$d'
    sed -n '/^## Zamknięte/,/^## Czego nigdy/p' "$CLAUDE_PROJECT_DIR/STOP.md" | sed '$d'
    echo "Pełny STOP.md: 5 tys. znaków, przeczytaj, jeśli nie czytałeś w tej sesji."
    ;;
  */logika-relacyjna-v3.5.md|*/poprawki.md)
    echo "STOP (wpis do ramy). Sprawdź przed wpisaniem:"
    sed -n '/^## Czego nigdy/,$p' "$CLAUDE_PROJECT_DIR/STOP.md"
    echo
    sed -n '/^## Sprawdzenie własnego wyniku/,/^\*Nowy przypadek/p' "$CLAUDE_PROJECT_DIR/SESJA-WZORCOWA.md" | sed '$d'
    ;;
esac
exit 0
