# Następny krok: czy dwa warunki z 154 dotykają `v/m_P` — jedynej danej, która łamie samopodobieństwo

Krok 2 zamknięty w całości (223, 224), krok o [104] zamknięty (225), wątek Naviera–Stokesa zamknięty
(226; użytkownik: *„wątek OpenAI, chyba można odpuścić"*). Otwarte są jeszcze krok 4 (rura ilościowo)
i `[?]` z 221, ale **nie mieszać ich z tym**.

## Najpierw: literatura pod samopodobieństwo

Użytkownik na koniec CC 12: *„jeśli chodzi o samopodobieństwo to chyba nie robiliśmy przeglądu literatury
konkretnie pod samopodobieństwo. A jest tego trochę"*. **Jeśli istnieje `literatura/samopodobienstwo.md`,
przeczytać go przed tym krokiem** — przynajmniej część o (S) i o następnym kroku (prace, które wiążą
hierarchię z warunkiem na końcu albo z punktem stałym). **Jeśli go nie ma — zrobić przegląd najpierw**
(pierwsze podejście 7.10 przerwał limit sesji: wszystkie agenty, zero wyników). Mapa jest materiałem
wejściowym, nie wpisem: każdy kandydat do ramy przechodzi test ze `STOP.md` dopiero tutaj.

---

## Co jest na stole

225 ustaliło dwie rzeczy, które razem dają to pytanie:

1. **Samopodobieństwo zespołu łamie dokładnie jedna dana niosąca skalę — `v`, w postaci legalnej `v/m_P`.**
   Trzy niezależne podpory: autonomia układu w schemacie niezależnym od mas (beta-funkcje nie zależą od mas,
   łamie tylko próg w `m_i = y_i·v/√2`), 218 (wspólny logarytm tylko przy `η = m/Q₀ → 0`), 180 pkt 5 (skala
   wnętrza przechodzi do O przez liczbę własnych tyknięć). A **nie** biegun `n_Λ` — to było zdanie asystenta
   z [105], puste przez bijekcję i sprzeczne z definicją w 152.
2. **Jedyne warunki, jakie rama ma, to dwa z 154:** `λ = 0` i `β_λ = 0` **na końcu Plancka** (224 pokazało,
   że innych Ø-miejsc z warunkami nie ma). 154 odczytało je jako **ustalające `m_H` i `m_t`**.

I to, co 225 zauważyło, a **świadomie nie wpisało** (222), dosłownie z bloku:

> „Dwa warunki 154 dotyczą wartości **na** końcu Plancka, a przejście do `m_H`, `m_t` idzie przez bieg na
> zakresie `ln(m_P/v)` — więc są relacją między `{m_H/v, m_t/v, v/m_P, sprzężenia}`. 154 odczytało je jako
> ustalające `m_H` i `m_t` przy danym `v/m_P`; to jest **wybór, które dane są wejściem**."

Czyli: dwa warunki na trzy wielkości. 154 trzymało `v/m_P` jako wejście. Równie dobrze można trzymać `m_t`
i dostać `v/m_P`. **Jeżeli tak, to pierwszy raz od początku `v/m_P` przestaje być tylko wolnym odczytem.**

---

## Czytać w całości, zanim cokolwiek

- **blok 154 w `## §F1`** (zaczyna się „ZASADA WIELU PUNKTÓW, POKOLENIA, LEPTONY") — cały pkt 1 z tabelą
  i pkt 1a (168: krytyczność λ na porządku, warunek Veltmana, `μ²`) — bo tam stoi, **jak** te dwa warunki
  zostały wyprowadzone i co dokładnie zostało z nich wzięte.
- **blok 225** (w `§F1`, zaraz za tabelą logarytmów) — bo z niego bierze się pytanie.
- **blok 224** (koniec bloku 183) — bo jego warunek (A) „położenie Ø-miejsca ustalone niezależnie od wolnej
  danej" **może się tu okazać za słabo sformułowany** (patrz „Co niepewne").
- **blok 208 w `### A11d`** — wiersz o unormowaniu Yukaw (`v/m_P`) i wiersz o `μ²`.

---

## Zdanie, które ma upaść

> **Dwa warunki z 154 są relacją między `m_H/v`, `m_t/v` i `v/m_P`, więc ograniczają także `v/m_P` —
> a odczyt „ustalają `m_H` i `m_t`" jest tylko jednym z wyborów wejścia.**

Rozstrzygnięcia wypisane **z góry**:

- **(a) Zdanie przechodzi.** Wtedy treść 154 trzeba zapisać jako **relację**, nie jako „ustalone `m_H`, `m_t`"
  — a wybór, co jest wejściem, jest opisem (223: stałe przy zmianie obiektu, zmienne przy zmianie opisu).
  I od razu ostrzeżenie: dla zmierzonych mas `λ` znika **dużo niżej niż `m_P`** (Buttazzo i in., cytowane
  w 154 — „przy `m_H = 125` stabilność do Plancka wymaga `m_t ≈ 171`"). Więc w odczycie „ustala `v/m_P`"
  zmierzone masy dałyby **inne** `v/m_P` niż rzeczywiste — i to jest albo trafienie, albo chybienie jedynego
  warunku ramy, zależnie od tego, jak się go czyta. **To trzeba policzyć uczciwie, nie wybrać odczytu po
  wyniku.**
- **(b) Zdanie upada: warunki nie dotykają `v/m_P` z nazwalnego powodu.** Wtedy powód jest wynikiem — i trzeba
  sprawdzić, czy nie jest to ten sam ruch co w 224 (bijekcja), tylko o poziom niżej.
- **(c) Pytanie źle postawione, bo „koniec Plancka" zlewa dwie rzeczy.** **Nazwany** jest niezależnie (2D ≡ Ø),
  ale jego **położenie w `t` względem `v`** to właśnie `ln(m_P/v)`, czyli sama wolna dana. Wtedy krok brzmi:
  najpierw rozdzielić „nazwany jako Ø" od „położony w `t`", potem pytać. Precedens: 224 rozdzieliło dwa końce
  pod nazwą „Ø-miejsce", 221 trzy obiekty pod literą `z`.

---

## Co niepewne — i tu jest najwięcej

**224 może wymagać poprawki.** W 224 warunek (A) brzmiał: Ø-miejsce daje warunek, gdy jego położenie jest
ustalone niezależnie od wolnej danej — i koniec Plancka zaliczyłem jako taki, **bo jest nazwany niezależnie**.
Ale nazwanie to nie położenie: w zmiennej `t` koniec Plancka leży w odległości `ln(m_P/v)` od odniesienia,
a to jest `v/m_P`. **Jeśli (c) jest trafione, to 224 (A) zlało „nazwany" z „położony"** — i trzeba to
poprawić tam, nie tylko tu. Nie wiem, i **to jest pierwsza rzecz do sprawdzenia**, zanim cokolwiek się
policzy. Jeśli 224 trzeba poprawić, to jest poprawka do własnego wpisu z tej samej sesji — zapisać ją jako
taką, nie przemilczeć.

**Dwa znaczenia „samopodobieństwa" w samym pytaniu (226, dopisane po tym, jak ten plik już stał).** Zdanie kroku
mówi o `v/m_P` jako „jedynej danej łamiącej samopodobieństwo" — to jest **(L)**: prawo bez wyróżnionej skali,
relacje biegną (152, 225). A drugi warunek 154, `β_λ = 0`, to **(S)**: stan na końcu, relacje nie biegną
(148: „punkt stały = dokładne samopodobieństwo"). **(L) nie daje (S)** — zespół biegnie przy (L) dokładnym.
Więc **nie wolno** rozumować „przy `m_P` `v` jest pomijalne, więc koniec jest samopodobny, więc `β_λ = 0` nie
mówi nic o `v`" — to zlewa (L) z (S) i z góry daje rozstrzygnięcie (b). Pułapka nr 12 w liście kontrolnej.
**I rzecz w pliku, której nie było na liście do czytania:** tabela 149 („ZLICZENIE KIERUNKÓW", `§F1`, zaraz za
blokiem 148) ma wiersz *„Higgs μ² | relewantne (= hierarchia v/m_P) | 1"* — w punkcie stałym przy Plancku
`v/m_P` jest kierunkiem relewantnym, czyli wolnym. To literatura (asymptotic safety), nie rama, a 208 wyrzuciło
`μ²` jako nie-odczyt; ale to jest dokładnie postać „(S) na końcu nie ustala danej, która łamie (L)". Przeczytać
148–149 w całości razem z 154, zanim się cokolwiek orzeknie — nie traktować tego wiersza jako odpowiedzi.

**Czy to w ogóle jest krok na kartkę.** Pytanie „czy warunki dotykają `v/m_P`" jest strukturalne (ile równań,
ile niewiadomych, co jest wejściem) — kartka. Ale ostrzeżenie z (a) dotyka **wartości** (gdzie znika `λ` dla
zmierzonych mas), a 208 i użytkownik (*„przestać się interesować liczbami"*) każą wartości nie szukać.
Rozdzielić: **struktura relacji — tak; liczba `v/m_P` z niej — nie w tym kroku.**

**Czego nie sprawdziłem w literaturze:** czy ktoś zapisał krytyczność Higgsa jako **warunek na hierarchię**,
a nie na masy — po kształcie: „Planck scale … determined by … criticality", „hierarchy … fixed by …
vanishing of the quartic", „ratio of the electroweak to the Planck scale … from the stability boundary".

---

## Jak NIE robić — z zapisanych błędów, nie z ostrożności

> **„Trzeba wyrzucać. […] Tego się dowiesz jak podasz strukturalny dowód. Cwaniaczku. Wcześniej tego nie
> powiesz"** (użytkownik, CC 9)

Nie zaczynać od „oczywiście dotykają, dwa równania na trzy niewiadome". Kolejność jest częścią wyniku.

**Z tej sesji, trzy razy z rzędu:** sprawdzić **kto co powiedział**, zanim się orzeknie o treści (225: etykieta
„[94] pkt 4" nie istniała, zdanie było asystenta, a punkt osi był dopisany pod nagłówkiem użytkownika);
sprawdzić, czy **kwantyfikator reguły równa się kwantyfikatorowi dowodu** (222); i sprawdzić **obie nogi
testu**, zanim się go użyje (224: zapowiedziałem, że test z 223 tnie, a nie ciął).

---

## Na koniec tej sesji: nadpisz ten plik

Napisz tu pierwszą wiadomość do **następnej** sesji, o kroku, który będzie następny. Zasady, które sprawiają,
że to działa — sprawdzone, nie wymyślone:

- **jeden krok, jedna wiadomość** — nie lista wszystkiego otwartego;
- **treść w środku, nie odsyłacz** — cytat z rozmowy wklejony, nie numer [n] do pobrania;
- **sekcja do przeczytania w całości**, nazwana i z rozmiarem;
- **zdanie, które może upaść**, z rozstrzygnięciami wypisanymi z góry;
- **to, co niepewne** — nie tylko wnioski. Wpis, który niesie same konkluzje, przeniesie też błąd,
  a pisze go sesja najmniej zdolna zobaczyć własny;
- **nie streszczać ramy.** Rama jest w `logika-relacyjna-v3.5.md` i w rozmowach. Ta wiadomość niesie krok.
