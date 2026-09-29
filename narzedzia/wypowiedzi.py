# wypowiedzi.py — wypowiedzi UŻYTKOWNIKA we wszystkich zapisach rozmów (rama to jego zdania, nie streszczenia).
#
#   python3 narzedzia/wypowiedzi.py 'zesp[oó]ł funkcji|relacja relacji'     akapity z trafieniem, z numerem [n]
#   python3 narzedzia/wypowiedzi.py 'czarn\w* dziur' --pelne                 całe wiadomości z trafieniem
#   python3 narzedzia/wypowiedzi.py --nr 94,104                              całe wiadomości [94], [104] (rozmowa źródłowa)
#   python3 narzedzia/wypowiedzi.py --nr 82 --plik 09-24-2                   numer z zapisu sesji CC (fragment nazwy pliku)
#   python3 narzedzia/wypowiedzi.py --nr 94 --wymiana                        wypowiedź razem z odpowiedzią asystenta
#   python3 narzedzia/wypowiedzi.py 'regex' --wymiana [--po 3]                ŚCIEŻKA: trafienie + tyle odpowiedzi po nim
#   python3 narzedzia/wypowiedzi.py 'regex' --oba                            szuka też w wypowiedziach asystenta
#
# PO CO --wymiana W TRYBIE SZUKANIA (poprawka 193): samo zdanie użytkownika to WNIOSEK, a wniosek zwykle stoi
# już w pliku głównym — więc wyszukanie bez tej flagi oddaje to, co się już miało, i nic nie wnosi. Droga do
# wniosku (zarzut asystenta, korekta, co odpadło) jest w wiadomościach NASTĘPUJĄCYCH po trafieniu.
#       (w rozmowach jest cały tok rozumowania, nie tylko wypowiedzi użytkownika — użytkownik, 26.09)
#
# Wyszukiwanie bez rozróżniania wielkości liter. Numery [n] w rozmowie źródłowej są numerami z CLAUDE.md;
# w zapisach sesji CC numeracja jest własna (podawać plik). W odpowiedzi wymienić [n], na których się opieram.
import glob, os, re, sys

# tylko bloki strukturalne z transkrypt.py (od początku linii): wzmianka o <details> w treści wiadomości
# nie może otworzyć bloku i zjeść tekstu aż do następnego zamknięcia
BLOK = re.compile(r'(?ms)^<details><summary>.*?^</details>[ \t]*$')

KAT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'rozmowa')
PLIKI = sorted(glob.glob(os.path.join(KAT, '*.md')), key=lambda f: ('logika-relacyjna-rozmowa' not in f, f))


def wiadomosci(plik):
    # bloki <details> (wyniki i wywołania narzędzi w zapisach sesji CC) usuwane PRZED podziałem: wydruki narzędzi
    # zawierają linie „## [n] Użytkownik …” (np. rama.py 4), które inaczej udawałyby wypowiedzi użytkownika
    t = BLOK.sub('', open(plik, encoding='utf-8').read())
    for k in re.split(r'\n(?=## \[\d+\] )', t):
        m = re.match(r'## \[(\d+)\] Użytkownik[^\n]*', k)
        if m:
            tresc = BLOK.sub('', k[m.end():]).strip()
            yield int(m.group(1)), m.group(0), tresc


def wszystkie(plik):
    t = BLOK.sub('', open(plik, encoding='utf-8').read())
    for k in re.split(r'\n(?=## \[\d+\] )', t):
        m = re.match(r'## \[(\d+)\] (Użytkownik|Asystent)[^\n]*', k)
        if m: yield int(m.group(1)), m.group(2), m.group(0), k[m.end():].strip()


def main(a):
    pelne = '--pelne' in a
    wymiana = '--wymiana' in a
    oba = '--oba' in a
    a = [x for x in a if x not in ('--pelne', '--wymiana', '--oba')]
    po = 1
    if '--po' in a:
        i = a.index('--po'); po = int(a[i + 1]); del a[i:i + 2]
    plik_f = None
    if '--plik' in a:
        i = a.index('--plik'); plik_f = a[i + 1]; del a[i:i + 2]
    if '--nr' in a:
        nr = {int(x) for x in a[a.index('--nr') + 1].split(',')}
        pliki = [f for f in PLIKI if (plik_f in f if plik_f else 'logika-relacyjna-rozmowa' in f)]
        for f in pliki:
            if not wymiana:
                for n, nagl, tresc in wiadomosci(f):
                    if n in nr: print(f'=== {os.path.basename(f)} {nagl}\n{tresc}\n')
                continue
            druk = False
            for n, rola, nagl, tresc in wszystkie(f):
                if rola == 'Użytkownik': druk = n in nr
                if druk: print(f'=== {os.path.basename(f)} {nagl}\n{tresc}\n')
        return
    if not a:
        sys.exit('użycie: python3 narzedzia/wypowiedzi.py REGEX [--wymiana [--po N]] [--oba] [--pelne] '
                 '[--plik FRAGMENT] | --nr 94,104 [--wymiana] [--plik FRAGMENT]')
    wz = re.compile(a[0], re.I)
    ile = 0
    for f in PLIKI:
        if plik_f and plik_f not in f: continue
        msgs = list(wszystkie(f))
        for i, (n, rola, nagl, tresc) in enumerate(msgs):
            if rola != 'Użytkownik' and not oba: continue
            if not wz.search(tresc): continue
            ile += 1
            print(f'=== {os.path.basename(f)} {nagl}')
            if pelne or wymiana: print(tresc)
            else:
                for ak in re.split(r'\n\s*\n', tresc):
                    if wz.search(ak): print(ak.strip()[:1500])
            print()
            if wymiana:
                # ŚCIEŻKA: samo zdanie użytkownika to WNIOSEK — ten zwykle stoi już w pliku głównym.
                # Droga do niego (zarzut asystenta, korekta, co odpadło) jest w tym, co następuje po nim.
                for n2, rola2, nagl2, tresc2 in msgs[i + 1:i + 1 + po]:
                    print(f'--> {os.path.basename(f)} {nagl2}\n{tresc2}\n')
    print(f'--- {ile} trafień' + ('' if oba else ' w wypowiedziach użytkownika'))


if __name__ == '__main__':
    main(sys.argv[1:])
