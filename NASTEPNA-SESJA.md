> **Najpierw `SESJA-WZORCOWA.md`** (po `STOP.md`): jak wygląda praca — dziesięć przypadków z ruchem i powodem; jej część „Sprawdzenie własnego wyniku” jeszcze raz przed każdym wpisem.

> **Przed każdym zdaniem o `D`, `d`, osiach albo czasie jako wymiarze — w każdym kroku, a przy pętlach, całkach po obrocie Wicka i `D` na pewno — przeczytać w całości R1b-F (z D0 i Lematem 1) i R1c-F, potem §E pod regułą 185.** Powód (245–247, 8.10): wszystko, co potrzebne, stało w pliku, a i tak dwa razy poprawiałem zapis według litery (`d = 3`, `D`, „oś czasu”). Rozstrzyga rachunek: czy odczyt stoi na `x⁰` (składowa przy 𝟙 w `X = x⁰·𝟙 + x·σ`) policzonym jak czwarta oś.

# Następny krok (zalecany; wybiera użytkownik): czy trzy warunki klasy, z których wychodzi `F_γ` (271), to to samo wejście, na którym już stoją 152, 208, 225 i 263 (krok 15 w `CLAUDE.md`)

**Stan na 13.10 (wieczór).** Ściana `F_γ` z 269 została przestawiona (271). Ogon miary celu jest wagą progową pary: `ν_γ([t,1/4]) = ρ̂(t)/3`, `F_γ(r) = (1/3)∫₀^{1/4} ρ̂(t)·r dt/(1+rt)`, `ρ̂ = β(3−β²)/2`. Kształt `ρ̂` wychodzi z macierzy 2×2 (`P± = E𝟙 ± p n·σ`, `A = √P₊`, `B = √P₋`, `AB = m𝟙`, prąd `Aσ_iB + Bσ_iA = (2Eσ₁, 2Eσ₂, 2mσ₃)`), `β` — z miary orbity `det P = m²`, normowanie się kasuje, skalar daje `β³/4`. Neutralnych amplitud kontaktów, stanu rodziny ani całego działania do samego progu nie potrzeba. Test 128 (drugi asystent, `masa/2026-10-13/test-128-prad-kontakt-miara-2026-10-13.md` §§7–9) pokazał, że 179, 268 i 257 nie wybierają trzech rzeczy — to nazwane warunki klasy:
- **W1** — EM działa w tym rzędzie wyłącznie przez generator ładunku `Q` na transporcie, bez elementarnego odczytu holonomii przez spin (`F₁ = 1`, `F₂ = 0`);
- **W2** — sektor EM jest swobodny i kwadratowy: w tym rzędzie spotkanie link–link nie przenosi holonomii (abelowość U(1) tego nie daje — człon Pauliego i nieliniowe sprzężenia fotonów są z nią zgodne);
- **W3** — pełna odpowiedź jest ograniczona, `(D(s) − D(0))/s → 0`: jedno odejmowanie (odniesienie) wystarcza, człon `c·r` znika. Przy stałym `F₂ = κ` jest `ρ̂ ∝ s` (sprawdzone), więc W1 i W3 są sprzężone.

Do tego most `ζ ↔ s` (argument krokowy rezolwenty do niezmiennika pary) i klasa stacjonarna.

## Skąd ten krok

W języku literatury W1–W3 to renormalizowalność. Asystent CC zauważył (13.10, [?], niewpisane), że to samo wejście stoi już niejawnie w czterech miejscach ramy:
- **152** — współczynniki `b = 41/6, −19/6, −7` to jednopętlowy bieg renormalizowalnego SM; ze stałym członem Pauliego bieg przy dużej rozdzielczości nie jest logarytmiczny;
- **208** — bilans 17 to parametry renormalizowalnego SM; `κ_f` dla każdego naładowanego nośnika albo `c·r` byłyby nowymi wolnymi danymi;
- **225** — „bieg nie zależy od mas, łamią go tylko progi” to własność teorii renormalizowalnych w schemacie niezależnym od mas;
- **263** — „klasa” (pełny spinor wektorowy, dodatnia reprezentacja spektralna bez odejmowań) jest tam jawnie nazwana jako wejście.

Jeśli to jedno wejście, `F_γ` nie jest nową ścianą, tylko tym samym wyborem działania, który rama ma otwarty od dawna (R1d pkt 3: „otwarta dynamika — wagi obiegów — = działanie”; 257: druga wariacja nie wybiera działania).

## Czytać w całości, zanim cokolwiek

1. Plik główny: §F0 blok 271 (~4 tys.), 208 (A11d, ~5 tys.), 225 (§F1), R1f-1 punkt 263 (~1,5 tys.), 152 i STAN ZESPOŁU (§F1).
2. `masa/2026-10-13/test-128-prad-kontakt-miara-2026-10-13.md` §§7–9 (~17 tys.) — K1 i K2 z kontrolami.
3. `masa/2026-10-13/odpowiedz-progowa-pary-2026-10-13.md` §20.7–20.8 (~5 tys.) — dwie funkcje `F₁`, `F₂` i rodzina diagnostyczna.

## Zdanie, które ma upaść

„Każde z 152, 208, 225 i 263 przestaje zachodzić po zanegowaniu W1, W2 albo W3 — i dla każdego da się wskazać, którego.” Rozstrzygnięcia wypisane z góry:
- **(a)** zachodzi dla wszystkich czterech → W1–W3 to jedno wejście ramy, już używane; dopisać je jawnie przy tych czterech miejscach, a `F_γ` liczyć jak każdą inną funkcję zespołu;
- **(b)** któreś z czterech zachodzi bez W1–W3 → dla `F_γ` W1–W3 są wejściem dodatkowym; nazwać, czego brakuje temu miejscu do `F_γ`;
- **(c)** zanegowanie W1–W3 da się zrobić tylko przez dołożenie skali (wielkość z jednostką, cięcie, położenie Plancka) → wtedy W1–W3 wynikają z punktu 4 `STOP.md` (bez pikseli i jednostek), i to byłby wynik ramy, nie wejście. Tego rozstrzygnięcia **nie zakładać** — człon Pauliego ma postać `κ/(2m)`, czyli skalę samego nośnika, a nie zewnętrzną; trzeba sprawdzić, nie przyjąć.

## Co niepewne — i tu jest najwięcej

- **Czy „renormalizowalność” to w ogóle jedna rzecz w ramie.** W1 (brak spinowego odczytu holonomii), W2 (brak link–link) i W3 (wzrost) mogą mieć trzy różne źródła; zgodność z jedną nazwą z literatury nie jest dowodem.
- **Wyjaśnienie z literatury jest pułapką.** Standardowe uzasadnienie (człony nierenormalizowalne tłumione potęgami ciężkiej skali, np. Plancka) daje skali położenie — dokładnie błąd 227–229. Brać formalizm i wynik, nie to pytanie ani tę odpowiedź.
- **Pomiar `g−2`** zgadza się z rachunkiem przy `F₂ = 0` w wiodącym rzędzie do ~10⁻¹² — to obserwacja wspólnego aparatu, nie wyprowadzenie W1.
- **Most `ζ ↔ s`** zostaje otwarty niezależnie od wyniku tego kroku.

## Jak pracować

- Zanim komenda pójdzie do drugiego asystenta: wypisać oba możliwe wyniki i co każdy zmienia w ramie. Jeśli jedyna możliwa odpowiedź wynika z konstrukcji zapisu, to nie jest test (13.10: pierwsza wersja K1 — złapana pytaniem użytkownika „Przemyślane?”).
- Przeglądy i sprawdzenia — skryptem albo inline, nie przepływem wieloagentowym: 13.10 limit sesji przerwał przepływ i nie zostało nic (ta sama przyczyna co 7.10).

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
