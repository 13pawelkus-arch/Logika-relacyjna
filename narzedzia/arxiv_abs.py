# Abstrakty prac z arXiv ze stron arxiv.org/abs/ID (metatagi citation_*), z odstępem 3 s.
# Zapisuje do pliku JSON po KAŻDEJ pracy, więc przerwanie niczego nie kasuje (7.10.2026: przepływy
# wieloagentowe zgubiły wszystko, a API export.arxiv.org, Semantic Scholar i OpenAlex były wyczerpane).
# Użycie: python3 -I narzedzia/arxiv_abs.py WYJSCIE.json 1901.04741,hep-th/0001210,...

import sys, json, subprocess, os, re, html, time
out, ids = sys.argv[1], sys.argv[2].split(',')
store = json.load(open(out)) if os.path.exists(out) else {}
def meta(h, name):
    return [html.unescape(m) for m in re.findall(r'<meta name="%s" content="([^"]*)"' % name, h)]
for i in ids:
    if i in store: continue
    r = subprocess.run(['curl', '-s', '--max-time', '40', 'https://arxiv.org/abs/' + i], capture_output=True, text=True)
    h = r.stdout
    t = meta(h, 'citation_title')
    if not t:
        print(f"{i} | BRAK ({len(h)}B)"); time.sleep(3); continue
    ab = meta(h, 'citation_abstract')
    store[i] = {'t': ' '.join(t[0].split()), 'au': meta(h, 'citation_author'),
                'y': (meta(h, 'citation_date') or [''])[0][:4], 'ab': ' '.join((ab or [''])[0].split()),
                'jr': ' '.join(meta(h, 'citation_journal_title')[:1]), 'src': 'arxiv.org/abs'}
    json.dump(store, open(out, 'w'), ensure_ascii=False)
    v = store[i]
    print(f"{i} | {v['y']} | {v['au'][0].split(',')[0] if v['au'] else ''} | {v['t'][:85]} | ab={len(v['ab'])}")
    time.sleep(3)
