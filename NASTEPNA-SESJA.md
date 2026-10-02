# Pierwsza wiadomość do następnej sesji

**Do wklejenia przez użytkownika jako pierwsza wiadomość.** Plik jest nadpisywany na końcu każdej sesji —
nie dopisywać do niego, nie streszczać w nim ramy. Niesie **bieżący krok**, nie framework.

---

## NAJPIERW: zadaj to pytanie, zanim cokolwiek przeczytasz i zanim cokolwiek policzysz

Nie zaczynaj od czytania sekcji. Pierwsza wiadomość do użytkownika ma być **dokładnie tym pytaniem**
(nie streszczeniem, nie parafrazą). Ono rozstrzyga kolejność całego kroku 3 i nie da się go zdjąć z pliku:

> „Pytanie do ciebie, bo rozstrzyga kolejność, a nie umiem go zdjąć z pliku: waga kroku ma być jedna,
> i wtedy jedna z dwóch postaci (−ν² rzeczywiste / e^{iν} okresowe) jest narzędziem cudzej konstrukcji —
> czy to są dwa różne sprzężenia, oba dopuszczone przez 179 pkt 7, i wtedy pytanie „ile wynosi a·b"
> ma dwie różne odpowiedzi, bo dotyczy dwóch różnych par?"

**Dlaczego to musi iść pierwsze:** obie postaci stoją w pliku obok siebie i obie są używane. `−ν²` to waga
zatrzymania z 181 (kwadrat wagi zwrotu szachownicy, B1). `e^{iν}` to faza na własne tyknięcie (R1f-3), i w tej
postaci wchodzi do czynnika kanału w 198 (`c = ∏(1 − p_k(1 − e^{−iφ_k}))`). **179 pkt 7** (DiVincenzo: relacja
wielu nośników rozkłada się na relacje par) dopuszcza sprzężenia parami i 199 już się na nie powołało,
wprowadzając wymianę obok odcisku — czyli precedens na **dwa różne sprzężenia w jednej strukturze już jest**.

Dopóki to nie jest rozstrzygnięte, „ile wynosi a·b" może być jednym pytaniem albo dwoma, a trzecia część ruchu
(„a propagator i tak wychodzi") dotyczyłaby wtedy dwóch różnych propagatorów. **Nie zgaduj i nie rozstrzygaj
tego sam** — użytkownik powiedział wprost, że tego nie da się zdjąć z pliku.

---

**Bierzemy krok 3: waga zatrzymania a·b — ale pełny ruch, nie połowa. Sesja CC 9 przeformułowała to pytanie (204) i to jest jedyny powód, dla którego warto je ruszać.**

Najpierw `git pull`.

**Przeczytaj w całości dwie rzeczy, w tej kolejności:**
1. **`R1b-A`** — nowy blok za R1b, **4 tys. znaków**. Twierdzenie o tle. Krótkie, i bez niego krok 3 nie ma sensu.
2. **`### A11d`** — **97 tys. znaków** (~25 tys. tokenów). Nie grepem. Bloki 180, 181, 186 stoją obok siebie i wykluczają się czytane osobno.

---

## Czego NIE robić — bo sesja CC 9 zrobiła to i użytkownik to obalił

**Nie pytaj „ile wynosi a·b”.** To jest pytanie Johnstona. U niego `b = −m²V₀` jest **wejściem z konstrukcji**:
zadajesz pole o danej masie wsypane w rozmaitość, m wkładasz, a V₀ to objętość areny. Nikt tam nie jest tym
zdziwiony i nikt tego nie pytał — bo nie ma tam pary (M, O). **Nie ma miliona nieudanych prób. Nie ma ani jednej.**

**I nie zatrzymuj się na „b jest wkładane, więc pytanie znika”.** To jest połowa ruchu i brzmi dokładnie jak
„eter jest założeniem, więc pytanie znika”. Nie znika. Ruch ma **trzy części**:

> **wkładane → nie robi roboty → a propagator i tak wychodzi.**

Dopiero trzecia coś rozstrzyga. Pierwsze dwie same w sobie są obserwacją o cudzym zapisie.

**I najważniejsze, znalezione 2.10: ten ruch jest już w pliku wykonany, na obiekcie o poziom wyżej.**
Słownik: **G = przelicznik zliczanie↔geometria, w zliczaniu G ≡ 1**. A5: równanie Einsteina **i tak wychodzi**,
jako bilans liczby relacji przez lokalny brzeg odczytywalności (Jacobson, w pliku „PRZESZŁO jako bilans”).
Tabela pojęć, jedna linijka: **„energia grawitacyjna tylko przez brzeg”**.
`b = −m²V₀` z V₀ = objętością jest **tym samym kształtem**: przelicznikiem zliczanie↔geometria o poziom niżej.
**Przeczytaj te trzy miejsca, zanim cokolwiek policzysz** — to jest gotowy wzorzec, nie analogia.

---

## Zdanie do upadku, i co znaczy każde wyjście

**Zdanie:** *to, co w hop-stop wkłada się jako a·b, jest wyznaczone przez samą parę (M, O) — a wkładanie go
jest zapisem tego, czego się o tej parze nie wie.*

- **Wychodzi, że jest wyznaczone** → trzecia część ruchu wykonana, wkładany parametr okazał się bezrobotny.
- **Wychodzi, że para go nie wyznacza, ale ogranicza, jakie a·b są dopuszczalne** → węższy wynik, też wynik. Nie mieszać z pierwszym.
- **Wychodzi, że para nie mówi o nim nic** → wtedy **uczciwie: trzecia część nie wyszła**, i to nie jest to samo co „pytanie znika”.
  Pustka jest odpowiedzią tylko wtedy, gdy się ją pokaże, a nie gdy się na niej poprzestanie przed sprawdzeniem.

---

## Czego nie trzeba szukać od nowa

Odczyt pary (M, O) przez jeden nośnik to **dokładnie trzy parametry rzeczywiste**, D = ½|Δr|, czwartego kanału
nie ma (199). Rozkładają się na **przezroczystość** (c = 1), **odcisk** (|c| = 1, c ≠ 1), **zapis** (|c| < 1, V = |c|)
i **wymianę** (oś z). 202: to są własności **pary (sprzężenie, stan wnętrza)**, nie samego sprzężenia — jedna bramka
(CNOT) daje wszystkie trzy, zależnie wyłącznie od ⟨X⟩_τ. 203 [T]: na dysku równikowym **|r| = |c|**, więc
**4 det ρ = 1 − |c|²** — widzialność, promień Blocha i położenie wobec stożka to **jedna liczba**.

**I to, co dodały 204 i 205:** tło nie niesie niczego, więc ρ, V₀ i ℓ wypadają z wyniku **z powodu, nie z reguły**.
205: **baza nośnika to pojemnik przestrzeni stanów** — baza wyznaczona przez sprzężenie opisuje sprzężenie,
ale nie wolno jej przenosić na zdanie o parze ani o M. Oraz: **|M| jest zliczeniem wnętrza, a czytane jest
zliczenie brzegu** (twierdzenie *Brzeg pary* w A11d); „od |M| nie zależy” z 198 wycofane.
Nie trzeba tego za każdym razem udowadniać na nowo — twierdzenie jest wyczerpujące. Trzeba tylko nie zostawić
ich w odpowiedzi.

---

## Co niepewne, i czego nie sprawdziłem

**Dwa formalizmy, nie jeden.** a·b żyje w obrazie **wag** (hop-stop: b = −m²V₀, waga zatrzymania w elemencie),
a 198–203 są w obrazie **stanów** (kubit na linku, kanał, wektor Blocha). 180 zapisało wprost: „**b jest wagą,
nie fazą — zgodność postaci, nie tożsamość**”. Czy „co a·b wynosi dla pary” jest w ogóle pytaniem o to samo,
co 198–203 — **nierozstrzygnięte**, i to jest pierwsza rzecz na kartce.

**Precedens, który może to zamknąć bez rachunku — ale nie zakładaj tego.** Poprawka 168, dosłownie:
*„porządek nie daje mu odpowiednika ani liczby”* — werdykt dla λ, o którą pytano tak samo. **Przeczytaj blok 168
i rozstrzygnij, czy a·b jest tym samym rodzajem obiektu.** Różnica, która może być istotna albo pozorna:
λ żyje w teorii pola w kontinuum, a a·b jest wagą **na samym porządku**. Rozstrzyga blok, nie analogia.

**Uwaga metodyczna z 201, która kosztowała jedną poprawkę.** Jeśli warunek, który sprawdzasz, jest **równością**,
to wycina **zbiór miary zero** i **losowanie nie znajdzie go nigdy**. Warunek rozstrzyga się na równaniach,
nie na próbkach. Użytkownik wtedy: „to nie jest przeszukanie, to próbkowanie dopełnienia. Instrument nie widzi tego,
czego szukasz.”

---

## Jedna rzecz o sposobie pracy, bo kosztowała całą sesję CC 9

Użytkownik, dosłownie: **„my głównie usuwamy i sprawdzamy. definicja czasu usuwa a nie dodaje”** oraz
**„Oprócz czasu i 3d nie ma tam nic co by ci dało inny rezultat”**.

**I druga, z 2.10, kosztowała trzy wymiany:** na pytanie „jak grawitacja traktuje masę” poszedłem do
podręcznika OTW. Użytkownik musiał powiedzieć wprost: *„Przeczytaj co na temat grawitacji mówi plik główny”* —
i tam stało wszystko, z twierdzeniem, w sekcji, w której właśnie pracowałem. **Odruch jest rozpoznany:
sięgam na zewnątrz dokładnie wtedy, gdy chcę potwierdzić kształt odpowiedzi.** Reguła na to już stoi
(*z literatury bierzemy formalizm i wynik, nie pytanie*) — ja wziąłem interpretację, czyli o stopień gorzej.

To **nie jest kryterium do przykładania do gotowej roboty.** CC 9 trzy razy z rzędu zamieniła zdanie o rzeczy
na procedurę dla siebie — zrobiła z tego test, punktowała nim otwarte kroki („ten dotyka czasu i 3D, tamten nie”),
i za każdym razem dostała po głowie. Nie ma menu, w którym jedne pozycje mają składnik, a inne nie.
**Kryterium jest sam mechanizm:** wziąć coś, co wszyscy wkładają, pokazać że nie robi roboty, wyrzucić,
i zobaczyć, że to co zostało i tak wydaje to, co miało bez tego nie powstać.

I jeszcze: **„inny rezultat” nie jest miarą.** GPS działa niezależnie od tego, czym jest czas — równania OTW
wystarczają i są zastosowane. Nie korzystamy z niczego, czego nie ma w QM, OTW i teorii informacji.

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
