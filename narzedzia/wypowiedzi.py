# wypowiedzi.py — wypowiedzi UŻYTKOWNIKA we wszystkich zapisach rozmów (rama to jego zdania, nie streszczenia).
#
#   python3 narzedzia/wypowiedzi.py 'zesp[oó]ł funkcji|relacja relacji'     akapity z trafieniem, z numerem [n]
#   python3 narzedzia/wypowiedzi.py 'czarn\w* dziur' --pelne                 całe wiadomości z trafieniem
#   python3 narzedzia/wypowiedzi.py --nr 94,104                              całe wiadomości [94], [104] (rozmowa źródłowa)
#   python3 narzedzia/wypowiedzi.py --nr 82 --plik 09-24-2                   numer z zapisu sesji CC (fragment nazwy pliku)
#
# Wyszukiwanie bez rozróżniania wielkości liter. Numery [n] w rozmowie źródłowej są numerami z CLAUDE.md;
# w zapisach sesji CC numeracja jest własna (podawać plik). W odpowiedzi wymienić [n], na których się opieram.
import glob, os, re, sys

KAT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'rozmowa')
PLIKI = sorted(glob.glob(os.path.join(KAT, '*.md')), key=lambda f: ('logika-relacyjna-rozmowa' not in f, f))


def wiadomosci(plik):
    # <details> (wyniki i wywołania narzędzi w zapisach sesji CC) usuwane PRZED podziałem: wydruki narzędzi
    # zawierają linie „## [n] Użytkownik …” (np. rama.py 4), które inaczej udawałyby wypowiedzi użytkownika
    t = re.sub(r'<details>.*?</details>', '', open(plik, encoding='utf-8').read(), flags=re.S)
    for k in re.split(r'\n(?=## \[\d+\] )', t):
        m = re.match(r'## \[(\d+)\] Użytkownik[^\n]*', k)
        if m:
            tresc = re.sub(r'<details>.*?</details>', '', k[m.end():], flags=re.S).strip()
            yield int(m.group(1)), m.group(0), tresc


def main(a):
    pelne = '--pelne' in a
    a = [x for x in a if x != '--pelne']
    plik_f = None
    if '--plik' in a:
        i = a.index('--plik'); plik_f = a[i + 1]; del a[i:i + 2]
    if '--nr' in a:
        nr = {int(x) for x in a[a.index('--nr') + 1].split(',')}
        pliki = [f for f in PLIKI if (plik_f in f if plik_f else 'logika-relacyjna-rozmowa' in f)]
        for f in pliki:
            for n, nagl, tresc in wiadomosci(f):
                if n in nr: print(f'=== {os.path.basename(f)} {nagl}\n{tresc}\n')
        return
    if not a:
        sys.exit('użycie: python3 narzedzia/wypowiedzi.py REGEX [--pelne] [--plik FRAGMENT] | --nr 94,104 [--plik FRAGMENT]')
    wz = re.compile(a[0], re.I)
    ile = 0
    for f in PLIKI:
        if plik_f and plik_f not in f: continue
        for n, nagl, tresc in wiadomosci(f):
            if not wz.search(tresc): continue
            ile += 1
            print(f'=== {os.path.basename(f)} {nagl}')
            if pelne: print(tresc)
            else:
                for ak in re.split(r'\n\s*\n', tresc):
                    if wz.search(ak): print(ak.strip()[:1500])
            print()
    print(f'--- {ile} wiadomości użytkownika z trafieniem')


if __name__ == '__main__':
    main(sys.argv[1:])
