# Rekordy z INSPIRE (tytuł, abstrakt, autorzy, czasopismo) dla prac spoza arXiv — po zapytaniu INSPIRE.
# Zapis do JSON po każdej pozycji. Użycie:
# python3 -I narzedzia/inspire.py WYJSCIE.json 'Klucz::t "tytuł" and a Nazwisko' ...

import sys, json, subprocess, os, urllib.parse, time
out = sys.argv[1]
store = json.load(open(out)) if os.path.exists(out) else {}
qs = sys.argv[2:]
for q in qs:
    key, query = q.split('::', 1)
    if key in store: continue
    url = 'https://inspirehep.net/api/literature?size=1&sort=mostcited&fields=titles,abstracts,authors.full_name,publication_info,arxiv_eprints&q=' + urllib.parse.quote(query)
    r = subprocess.run(['curl', '-s', '--max-time', '40', url], capture_output=True, text=True)
    try:
        h = json.loads(r.stdout)['hits']['hits']
    except Exception:
        print(key, 'BLAD', r.stdout[:120]); continue
    if not h:
        print(key, 'BRAK'); continue
    m = h[0]['metadata']
    pi = (m.get('publication_info') or [{}])[0]
    store[key] = {'t': m.get('titles', [{}])[0].get('title', ''), 'au': [a.get('full_name', '') for a in m.get('authors', [])[:6]],
                  'y': str(pi.get('year', '')), 'ab': (m.get('abstracts') or [{}])[0].get('value', ''),
                  'jr': f"{pi.get('journal_title','')} {pi.get('journal_volume','')} ({pi.get('year','')}) {pi.get('page_start','')}",
                  'ax': [e.get('value') for e in m.get('arxiv_eprints', [])], 'src': 'inspire'}
    json.dump(store, open(out, 'w'), ensure_ascii=False)
    v = store[key]
    print(f"{key} | {v['y']} | {v['au'][0] if v['au'] else ''} | {v['t'][:80]} | {v['jr']} | ab={len(v['ab'])}")
    time.sleep(1)
