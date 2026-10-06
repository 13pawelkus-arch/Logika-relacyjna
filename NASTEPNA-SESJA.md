# Następny krok: zliczyć Ø-miejsca na relację — pierwsza połowa kroku 2

Druga połowa kroku 2 (przeniesienie `𝒢` z 212) **została zamknięta na stałe poprawką 223** — nie wracać.
Otwarte są jeszcze krok 4 (rura ilościowo) i `[?]` z 221, ale **nie mieszać ich z tym**.

---

## Co jest na stole

208 ustaliło **rodzaj** każdej wolnej danej zespołu: wszystkie są **stosunkami liczności**, a cztery z nich
(trzy przesunięcia `1/α_i` + unormowanie Yukaw) to stosunki **do miejsc, w których relacja spotyka Ø**.
I tam stoi przeformułowanie kroku 2, dosłownie:

> „To przeformułowuje krok 2 (183) z polowania na warunki w **zliczenie Ø-miejsc na relację**: wolna dana
> jest odległością w liczności do Ø-miejsca, a 183 [T] mówi już, że tylko λ przechodzi przez zero
> **wewnątrz** zakresu — więc pozostałe Ø-miejsca leżą na krańcach i tyle jest warunków, ile krańców.”

183 [T] ma już połowę roboty zrobioną: w zespole jednopętlowym **tylko λ** może przejść przez zero wewnątrz
zakresu, bo `1/α_i` jest liniowe w `t` (zero tylko asymptotycznie — Landau albo transmutacja), Yukawy mają
równanie **multiplikatywne** (`y_f = 0` jest punktem stałym), a **człon bez λ ma tylko `β_λ`**.

**Pytanie, które zostaje:** ile Ø-miejsc ma każda relacja i **czy każde daje warunek**. Nie „ile warunków
dają granice Ø” — to było stare, złe postawienie.

---

## Czytać w całości, zanim cokolwiek

- **`## R1a`** (18,7 tys. znaków) — cała, razem z tabelą GRANICE Ø i blokiem 207. Tam jest definicja tego,
  czym Ø-miejsce jest, i poprawka użytkownika, że granice Ø **nie są dwoma końcami**.
- **blok 183 w `## §F1`** (2,2 tys., zaczyna się „GRANICE Ø WEWNĄTRZ ZAKRESU”) — krótki, przeczytać dosłownie
  razem z jego kontrolą „czy zdanie coś wyróżnia”.
- **blok 208 w `### A11d`** — tabela 19 odczytów z kolumną „powód”, bo to ona mówi, **do jakiego** Ø-miejsca
  odnosi się każda z czterech danych.
- **blok 223 w `## §F1`** — bo daje narzędzie (niżej) i bo zamyka drugą połowę tego kroku; żeby jej nie
  otwierać z powrotem.

`## §F1` ma 92,4 tys. znaków i **w tej sesji został przeczytany w całości** przy 223. Jeśli następna sesja
czyta go znowu w całości — dobrze; jeśli nie, to **te dwa bloki plus tabela „STAN ZESPOŁU” są minimum**,
i trzeba to zapisać jako świadome zawężenie, nie przemilczeć.

---

## Zdanie, które ma upaść

> **Każde Ø-miejsce relacji daje jeden warunek na jej wolną daną, więc warunków jest tyle, ile Ø-miejsc.**

Rozstrzygnięcia wypisane **z góry**:

- **(a) Zdanie przechodzi.** Wtedy jest liczba do porównania z bilansem 149 (17 wolnych danych wobec ~1
  warunku) i **pierwszy raz od 149 ten bilans się rusza**. Natychmiast sprawdzić, czy nie liczy się
  tego samego Ø-miejsca dwa razy (Landau i transmutacja to **jedno** miejsce widziane z dwóch stron, czy dwa).
- **(b) Część Ø-miejsc nie daje warunku, bo zależy od opisu, nie od obiektu.** Wtedy liczba warunków maleje
  i **to jest wynik**, nie porażka — patrz narzędzie niżej. Podejrzenie konkretne: położenie bieguna Landaua
  i skala transmutacji są poza jedną pętlą zależne od schematu, a 208 odrzuciło `μ²` dokładnie za „zależy od
  samej skali cięcia, nie od stosunku dwóch rozdzielczości”.
- **(c) Pytanie źle postawione, bo „Ø-miejsce” zlewa dwie rzeczy.** Zero sprzężenia (relacja znika, `α → 0`)
  i rozbieżność sprzężenia (Landau, `1/α → 0`) to **nie to samo**, a 183 wymienia oba w jednym zdaniu.
  Wtedy krok brzmi: najpierw rozdzielić, potem zliczać. Precedens: 221 rozdzieliło trzy obiekty pod literą
  `z`, 206 zespoliło dwie trójki i tabela to policzyła.

---

## Narzędzie zrobione w tej sesji (223) — i ostrzeżenie, że tnie w obie strony

223 dało **test dwustronny**: wielkość, która jest **stała przy zmianie obiektu** i **zmienna przy zmianie
opisu**, nie może ograniczać obiektu tam, gdzie jest stała. Nie wymaga rozpoznania bazy ani pojemnika —
wystarczy policzyć obie pochodne. Tym padło przeniesienie `𝒢` na `α_i` i `y_f`.

**Ostrzeżenie: ten test prawdopodobnie tnie także w ten krok**, i trzeba to sprawdzić **przed** zliczaniem,
nie po. Pytanie do każdego Ø-miejsca po kolei: czy jego położenie zmienia się, gdy zmienia się **opis**
(schemat, rząd pętli, definicja sprzężenia), przy nietkniętym obiekcie? Jeśli tak — to Ø-miejsce nie jest
warunkiem i wypada, tak samo jak `μ²` w 208. Jeśli nie zmienia się przy żadnej zmianie opisu — zostaje.

**Czego NIE robić (z 222):** nie wnioskować z postaci zapisu. „`1/α` jest liniowe, więc zero jest tylko
asymptotyczne” jest zdaniem o jednopętlowym **równaniu**, nie o relacji; 183 samo to oznacza („przy dwóch
pętlach struktura się nie zmienia — [O], rachunkiem niesprawdzone”).

---

## Jak NIE robić — z zapisanych błędów, nie z ostrożności

> **„Albo niosła, albo nie niosła. Dowód ma być strukturalny a nie bajdurzeniem o przykładach”**
> (użytkownik, CC 9)

Zliczenie to nie lista przykładów Ø-miejsc. Albo jest reguła mówiąca, ile ich ma relacja danego rodzaju,
albo nie ma zliczenia.

> **„Nie szukać wartości”** — 208 zabrania warunku na odczyt, który nie jest samorelacją.

Więc nawet jeśli Ø-miejsc wyjdzie dużo, **nie wolno z nich robić wartości** dla czegoś, co nie jest
samorelacją. Liczba warunków i liczba ustalonych danych to dwie różne rzeczy.

I trzeci, najświeższy, z 222: **sprawdzić, czy kwantyfikator reguły równa się kwantyfikatorowi dowodu.**
Jeśli wyjdzie reguła „każda relacja ma `k` Ø-miejsc”, to zanim trafi do bloku ogólnego — sprawdzić, na ilu
rodzajach relacji została pokazana.

---

## Co niepewne

**Czy „Ø-miejsce” jest w ogóle policzalne bez wybranego zakresu.** 183 mówi „wewnątrz zakresu” i „na
krańcach”, a zakres to para rozdzielczości. Jeśli liczba Ø-miejsc zależy od wybranego zakresu, to jest
wielkością, nie relacją — po 208 wypadałaby tym samym kryterium, którym wypadło `μ²`. **Nie wiem, i to jest
pierwsza rzecz do sprawdzenia, nie do założenia.**

**Czy λ liczy się raz, czy dwa.** 183 [T] daje λ zero **wewnątrz** zakresu, a 154 daje jej warunek **na
końcu Plancka** (`λ = 0` i `β_λ = 0`), i 183 mówi, że ten drugi jest „przypadkiem szczególnym warunku
dotyczącego całego zakresu”. Czy to jedno Ø-miejsce czy dwa — od tego zależy, czy jedyne wykorzystane
trafienie zespołu było jednym warunkiem czy dwoma.

**Czego nie sprawdziłem w literaturze:** czy ktoś policzył **niezależność od schematu** położenia zera albo
bieguna sprzężenia — po kształcie, nie po nazwie („Landau pole scheme dependence” coś da, ale lepsze:
„location … independent of the renormalization scheme”, „invariant … all orders … coupling vanishes”).

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
