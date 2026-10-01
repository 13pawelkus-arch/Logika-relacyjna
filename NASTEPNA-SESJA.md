# Pierwsza wiadomość do następnej sesji

**Do wklejenia przez użytkownika jako pierwsza wiadomość.** Plik jest nadpisywany na końcu każdej sesji —
nie dopisywać do niego, nie streszczać w nim ramy. Niesie **bieżący krok**, nie framework.

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

**I to, co 204 dodało:** tło nie niesie niczego, więc ρ, V₀ i ℓ wypadają z wyniku **z powodu, nie z reguły**.
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
