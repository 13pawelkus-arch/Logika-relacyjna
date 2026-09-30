# Pierwsza wiadomość do następnej sesji

**Do wklejenia przez użytkownika jako pierwsza wiadomość.** Plik jest nadpisywany na końcu każdej sesji —
nie dopisywać do niego, nie streszczać w nim ramy. Niesie **bieżący krok**, nie framework.

Powód (30.09): start sesji daje ~82 tys. znaków zakazów, mapy i wyprowadzenia czasu/3D, a bieżąca robota
(A11d) nie jest w tym wcale. Ta wiadomość wypełnia tę dziurę. Nie zastępuje plików.

---

**Krok 1 jest zamknięty (poprawki 198–202). Bierzemy krok 3: waga zatrzymania na skok a·b dla konkretnych par (M, O).**

Najpierw `git pull`.

**Przeczytaj `### A11d` w całości** — teraz 99,5 tys. znaków (~25 tys. tokenów), bo doszły bloki 198–202.
Nie grepem. Bloki 180, 181, 186 i 202 muszą być przeczytane **razem**: 186 kwalifikuje ℓ jako pojemnik,
181 mimo to nazwało nim wynik, 194 to poprawiło, a 202 pokazało, że nazwy „odcisk” i „zapis” też były zlane.
To jest sekcja, w której powtarza się ten sam błąd nazewniczy, i czytana w całości sama go pokazuje.

**Co dokładnie zostało otwarte — cytat z 181 po korekcie 194, nie odsyłacz:**

> „**Obiektem ramy jest tu wyłącznie a·b — waga zatrzymania na skok, czysta liczba przy strukturze.**
> Przepisanie a·b = −(m·ℓ)²/… to **słownik rozsiewu**, bo ℓ = ρ^{−1/d} jest wielkością pojemnika […].
> Wolno go użyć jako narzędzia przekładu na literaturę (185), **nie wolno nim nazywać wyniku**.”

A w „Najbliższych krokach”: „Po odjęciu ℓ pytanie jest strukturalne: **co a·b wynosi dla danej pary (M, O),
bez jednostek i bez ρ**.”

**Czego NIE trzeba szukać od nowa — to już stoi po sesji CC 8.** Odczyt pary (M, O) przez jeden nośnik to
**dokładnie trzy parametry rzeczywiste**, D = ½|Δr| (odległość Blocha od Ø), i czwartego kanału nie ma (199).
Rozkładają się na **przezroczystość** (c = 1), **odcisk** (|c| = 1, c ≠ 1 — faza, wnętrze nic nie zapisało),
**zapis** (|c| < 1 — wnętrze zapisało, V = |c|) i **wymianę** (oś z — wnętrze daje albo bierze tyknięcie);
202 pokazało, że to są własności **pary (sprzężenie, stan wnętrza)**, nie samego sprzężenia — jedna bramka
(CNOT) daje wszystkie trzy, zależnie wyłącznie od ⟨X⟩_τ.

**Pierwsza rzecz do rozstrzygnięcia, zanim cokolwiek policzysz — dwa formalizmy, nie jeden.** a·b żyje
w obrazie **wag** (hop-stop Johnstona: b = −m²V₀ jako waga zatrzymania w elemencie), a 198–202 są w obrazie
**stanów** (kubit na linku, kanał, wektor Blocha). 180 zapisało to wprost: „**b jest wagą, nie fazą —
zgodność postaci, nie tożsamość**”. Więc pytanie „co a·b wynosi dla pary” może w ogóle nie być pytaniem
o to samo, co 198–202. To jest do rozstrzygnięcia **pierwsze**, na kartce, i rozstrzygnięcie jest wynikiem
niezależnie od tego, jak wypadnie.

**Zdanie do upadku — trzy rozstrzygnięcia, każde jest wynikiem:**

- a·b wychodzi **jako liczba wyznaczona przez parę** (M, O), bez jednostek i bez ρ → **wynik o parze**;
- a·b zależy od czegoś, co **nie jest własnością pary** → wg [290] dosłownie: *„Liczba jest dopuszczalna
  tylko wtedy, gdy nie rośnie z gęstością. Jeśli rośnie, jest gęstością, a nie liczbą, i wymaga miary.”*
  → **miara, nie sztuki**; odpada jako liczba;
- a·b okazuje się **parametrem wkładanym, a nie odczytywanym** — w hop-stop b jest **wejściem** propagatora,
  nie czymś, co struktura wyznacza → pytanie po oczyszczeniu **znika**, a wg `STOP.md` „pytanie, które po
  oczyszczeniu znika, jest wynikiem, nie porażką”.

**Co niepewne, i nie zostało sprawdzone.** Trzecie rozstrzygnięcie jest moim podejrzeniem, nie ustaleniem:
b = −m²V₀ wygląda na wielkość wstawianą do propagatora z zewnątrz, a nie wyprowadzaną ze struktury.
Jeśli tak, to cały krok 3 jest pytaniem źle postawionym — ale **tego nie sprawdziłem**, i nie wolno tego
przyjąć bez rachunku, bo dokładnie tak brzmiałoby wygodne wyjście.

**Dwie rzeczy, których czytanie sekcji nie łapie (obie sprawdzone w tej sesji, obie zadziałały):**

1. Pytanie ze `STOP.md`: **co rama po tym wpisie pozwala albo czego zabrania, czego nie pozwalała przedtem?**
   Brak odpowiedzi = nie ma wpisu.
2. Ścieżka, nie sam wniosek: `python3 narzedzia/wypowiedzi.py 'waga zatrzymania|hop-stop|przelicznik' --wymiana --po 3`.
   W tej sesji ścieżka rozstrzygnęła spór, którego plik główny nie rozstrzygał — czy „przechodzi na zewnątrz”
   z 174 znaczy przeniesienie, czy zależność (202/201: zależność, bo słowo „Definicja.” obejmuje dwa
   pierwsze zdania, a trzecie zaczyna się od „Czyli”).

**Trzecia rzecz, którą warto mieć z tyłu głowy — metodyka, nie treść (błąd z 201).** Jeżeli warunek, który
sprawdzasz, jest **równością** (kanałów, wag, odczytów), to wycina **zbiór miary zero** i **losowanie go nie
znajdzie nigdy**. Warunek rozstrzyga się na równaniach, nie na próbkach. W tej sesji podałem 40 000 losowań
jako poszlakę pustości i była to wartość zerowa — użytkownik: „to nie jest przeszukanie, to próbkowanie
dopełnienia. Instrument nie widzi tego, czego szukasz.”

**Jeśli wolisz inny krok:** otwarte zostają jeszcze 2 (granice Ø wewnątrz zakresu, 183 — wymaga przeczytania
`## R1a` 15 tys. i `## §F1` 71 tys., i grozi mu potwierdzanie) oraz 4 (rura na porządku ilościowo, 171 —
też w A11d). Krok 3 jest wybrany dlatego, że stoi w **tej samej sekcji**, którą sesja CC 8 przerobiła,
i 199 zapisało wprost, że stoi **za** krokiem 1 — a krok 1 jest już zamknięty.

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
