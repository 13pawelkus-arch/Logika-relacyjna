# transkrypt.py — zapis rozmowy z Claude Code (jsonl) → rozmowa/claude-code-sesja-RRRR-MM-DD.md.
# W Claude Code nie ma eksportu, a kontener znika po sesji: uruchomić przed końcem każdej sesji, potem commit + push.
# Zewnętrznych ocen NIE włączać (życzenie użytkownika) — jeśli były w rozmowie, usunąć je z pliku wynikowego ręcznie.
#
#   python3 narzedzia/transkrypt.py rozmowa/claude-code-sesja-2026-09-27.md \
#       --tytul 'Rozmowa w Claude Code — sesja 4 (27.09.2026) — zapis' --opis 'Kontynuacja sesji 3 (…). Poprawki 166–…'
#   [--jsonl ŚCIEŻKA]   domyślnie: najnowszy plik w ~/.claude/projects/*Logika-relacyjna*/
import argparse, glob, json, os, re

ap = argparse.ArgumentParser()
ap.add_argument('out'); ap.add_argument('--tytul', default='Rozmowa w Claude Code — zapis'); ap.add_argument('--opis', default='')
ap.add_argument('--jsonl')
a = ap.parse_args()
src = a.jsonl or max(glob.glob(os.path.expanduser('~/.claude/projects/*Logika-relacyjna*/*.jsonl')), key=os.path.getmtime)


def clean(s):
    s = re.sub(r'<system-reminder>.*?</system-reminder>', '', s, flags=re.S)
    return re.sub(r'<user-prompt-submit-hook>.*?</user-prompt-submit-hook>', '', s, flags=re.S).strip()
def ts(d): return d.get('timestamp', '')[:16].replace('T', ' ')
def cut(s, n=1500): return s if len(s) <= n else s[:n] + '\n…[ucięto]'
def neutral(s):  # ani wydruk narzędzia, ani treść wiadomości nie może udawać nagłówka wiadomości ani otworzyć/zamknąć bloku <details>
    s = s.replace('<details>', '&lt;details&gt;').replace('</details>', '&lt;/details&gt;')
    return re.sub(r'(?m)^## \[', ' ## [', s)


L = [f'# {a.tytul}', '', (a.opis + ' ' if a.opis else '') + 'Wiadomości użytkownika i odpowiedzi asystenta w całości; '
     'wywołania narzędzi skrócone; przypomnienia systemowe, wyniki hooków i wewnętrzne rozumowanie pominięte.', '', '---', '']
n = 0
for line in open(src, encoding='utf-8'):
    try: d = json.loads(line)
    except Exception: continue
    if d.get('isSidechain') or d.get('isMeta'): continue
    t = d.get('type'); m = d.get('message') or {}; c = m.get('content')
    if t == 'user':
        for b in ([c] if isinstance(c, str) else (c if isinstance(c, list) else [])):
            if isinstance(b, str) or b.get('type') == 'text':
                s = clean(b if isinstance(b, str) else b['text'])
                if s and not s.startswith('<') and s != 'Tool loaded.':
                    n += 1; L += [f'## [{n}] Użytkownik — {ts(d)}', '', neutral(s), '']
            elif b.get('type') == 'tool_result':
                r = b.get('content')
                if isinstance(r, list): r = '\n'.join(x.get('text', '') for x in r if isinstance(x, dict))
                L += ['<details><summary>wynik</summary>', '', '````', neutral(cut(clean(str(r or '')))), '````', '</details>', '']
    elif t == 'assistant' and isinstance(c, list):
        for b in c:
            if b.get('type') == 'text' and b['text'].strip():
                n += 1; L += [f'## [{n}] Asystent — {ts(d)}', '', neutral(b['text'].strip()), '']
            elif b.get('type') == 'tool_use':
                i = b.get('input', {})
                desc = i.get('description') or i.get('query') or i.get('url') or i.get('file_path') or ''
                body = i.get('command') or i.get('prompt') or ''
                L += ['<details><summary>narzędzie</summary>', '', '````', neutral(f"{b['name']}: {desc}"), neutral(cut(body, 800)), '````', '</details>', '']
open(a.out, 'w', encoding='utf-8').write('\n'.join(L))
print(f'{a.out}: {n} wiadomości (źródło {src})')
