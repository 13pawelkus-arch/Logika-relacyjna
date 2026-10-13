> **Najpierw `SESJA-WZORCOWA.md`** (po `STOP.md`): jak wygląda praca — dziesięć przypadków z ruchem i powodem; jej część „Sprawdzenie własnego wyniku” jeszcze raz przed każdym wpisem. Przypadek 10 jest nowy i dotyczy dokładnie tego kroku.

> **Przed każdym zdaniem o `D`, `d`, osiach albo czasie jako wymiarze — w każdym kroku, a w kroku 12 (α z progami: pętle, całki po obrocie Wicka, `D`) na pewno — przeczytać w całości R1b-F (z D0 i Lematem 1) i R1c-F, potem §E pod regułą 185.** Powód (245–247, 8.10): wszystko, co potrzebne, stało w pliku, a i tak dwa razy poprawiałem zapis według litery (`d = 3`, `D`, „oś czasu”), bo czytałem R1b od Wniosku 1, bez D0, a zdanie użytkownika wziąłem jako regułę zamiast z niej wyprowadzić. Rozstrzyga rachunek: czy odczyt stoi na `x⁰` (składowa przy 𝟙 w `X = x⁰·𝟙 + x·σ`) policzonym jak czwarta oś.

# Następny krok (zalecany; wybiera użytkownik): skąd w relacjach 179 biorą się neutralne amplitudy kontaktów — czyli czy `F_γ` wychodzi z ramy (krok 13 w `CLAUDE.md`, luka 269)

**Stan na 13.10.** Użytkownik prowadził 9–12.10 pracę z innym asystentem; 13.10 scalona jako 251–269 (rejestr; materiał w `masa/2026-10-09/`, `masa/01-…`, `masa/02-…`, `masa/2026-10-12/`, `masa/przyporzadkowanie realizacji dynamicznej.md`). Rozmów z tego okresu nie ma — ścieżką dla zdań użytkownika jest `masa/21-punkt-wznowienia-2026-10-05.md` i raporty. Alternatywy, jeśli użytkownik wybierze inaczej: krok 12 (α z progami — dane `R`, W), kroki 10–11 (171), obserwacja 14 (do decyzji użytkownika, nie do liczenia).

## Skąd ten krok — tylko tyle, ile potrzeba

Próba z 12.10 doszła do miejsca, które sama nazwała dokładnie (`przyporzadkowanie…` §19.7):

> „R1d określa masowy zygzak, wspólny ładunek L/R i koneksję. Neutralny transport całej rodziny oraz przygotowanie jej modów nie są w tym zapisie ilościowo określone. […] Nie ma więc wyznaczonej ν_kontakty, którą dałoby się porównać z (19.12). […] To jest dokładne miejsce zatrzymania obecnego rachunku, a nie obietnica, że następne samo różniczkowanie je usunie.”

Co już stoi (nie liczyć od nowa): reguła wag wszystkich kanałów dla gaussowskich końców (`C_ℓk = Σ η_a(1−η_b)…`), przyczynowa odpowiedź z wagami `λ_a − λ_b`, krok `1/α(n−1) − 1/α(n) = −κ_n ln[n/(n−1)]`, χ = 0 z dwuliniowego zygzaka, moduł dwudrogowy `p(Φ) = ½[1 + c₁₂cos QΦ]` z `c₁₂ = cos[(n₁−n₂)ϑ]` — zliczenia przejść masowych wchodzą jako waga obiegu. Cel jest wyznaczony: `F_γ(r) = ∫₀^{1/4} ln(1+rt) dν_γ(t)`, `dν_γ = 4t/√(1−4t)dt`, momenty `μ_k = 2[(k+1)!]²/(2k+3)!` = 1/3, 1/15, 1/70, 1/315, … — zgodność `F_kontakty = F_γ` ⇔ zgodność wszystkich momentów `k ≥ 1` (§19.7).

**Korekty użytkownika z 12.10, które mają obowiązywać od pierwszej wiadomości** (cytaty z notatki punktu wznowienia — omówienie tamtego asystenta, nie słowa użytkownika): *„Asystent kilkakrotnie wracał do ustalania podstaw, zamiast je zastosować; użytkownik przerwał tę pętlę. Nie dziedziczyć tego błędu jako nowego planu.”* oraz *„Nie uruchamiamy dynamiki. Nie ma rozróżnialności bez dynamiki.”*, *„Zegar nie jest dodatkowym »czymś«. Badany proces i jego relacje pełnią rolę zegara.”*

## Czytać w całości, zanim cokolwiek

1. `masa/21-punkt-wznowienia-2026-10-05.md` — blok aktualny (do „Archiwum”), ~7,5 tys. znaków.
2. Plik główny: R1f-1 (~11 tys.; punkty 257–263 i 269), §F0 blok 269 (~2 tys.), A11d bloki 177 + 179 (~17 tys.), 268 (~2,5 tys.), 267 (~3,6 tys.).
3. `masa/przyporzadkowanie realizacji dynamicznej.md` §14 (~13 tys. bez kodu), §18 (~13 tys.), §19 (~15 tys.). Kod kontroli w tekście; nie uruchamiać ponownie bez nowego problemu (zrobione 13.10, PASS).

## Zdanie, które ma upaść

„W rodzinie, w której n liczy przejścia masowe zygzaka (R1d, 269), a transport EM idzie po tych samych kontaktach, z przygotowaniem i efektem jednego O, redukcja z §13.3 daje miarę `ν_kontakty` o momentach `μ₀ = 1/3`, `μ₁/μ₀ = 1/5`, `μ₂/μ₁ = 3/14`.” Rozstrzygnięcia wypisane z góry:
- **(a)** miara wyznaczona i zgodna we wszystkich momentach → `F_γ` wychodzi z kontaktów w tej rodzinie (wtedy osobno: co z tego jest wyborem rodziny);
- **(b)** wyznaczona i niezgodna → wynik negatywny **dla tego przyporządkowania**, nie dla ramy (przypadek 10);
- **(c)** niewyznaczona, bo potrzebny jest dodatkowy wybór (amplitud `h_ℓ`, stanu, profili) → nazwać ten wybór i zrobić dla niego test 128: które zdanie ramy łamie jego zanegowanie. „Najprostszy”, „lokalny”, „kanoniczny” bez definicji nie są odpowiedzią.

## Co niepewne — i tu jest najwięcej

- **Czy n z §F0 (obieg radarowy, `q ∝ 1/n`) to to samo n co liczba przejść zygzaka w module §18.** Raport wprost tego nie utożsamia (§18.5: „nie utożsamia się ich automatycznie z n ukończonego odczytu radarowego”). Jeśli to dwa różne zliczenia, zdanie wyżej trzeba najpierw postawić z właściwym n.
- **Wagi Johnstona `a·b` (206, 242) jako kandydat na neutralne amplitudy.** Kuszą, bo dają propagator z hop-stop bez gęstości (B = I − a·b·Φ). Ale odtworzenie propagatora Feynmana u Johnstona idzie przez rozsiew (pojemnik, B1, `STOP.md`) — samo podobieństwo kształtu nie jest przyporządkowaniem. Sprawdzić, co zostaje bez rozsiewu, zanim cokolwiek się policzy.
- **Stan.** §19.5: N = 0 nie wynika z „pole bez wzbudzenia ≡ Ø”; zmiana opisu modów zamienia zygzak w tworzenie pary. Przygotowanie trzeba wskazać z relacji O, nie z nazwy „próżnia”.
- **Pomiar mierzy wynik, nie trafność kroku:** jeśli wyjdzie (a), sprawdzić, czy zgodność nie została włożona przez wybór kanonicznej klasy (257) — to byłby przypadek 5 (potwierdzanie).

## Jak NIE robić

- Nie ustalać od nowa czasu, 3D, dynamiki ani osobnego zegara (przypadek 10; korekta użytkownika z 12.10).
- Nie wstawiać kanonicznego propagatora Diraca i nie ogłaszać wyniku §14.4 wyprowadzeniem — to rachunek warunkowy, już zrobiony.
- Nie porównywać `(18.11)` (krzywizna prawdopodobieństwa skończonego fragmentu) wprost z `F_γ` — to nie jest jądro EM z §13.3.
- Nie liczyć na rozsiewie (`STOP.md`), nawet jeśli wagi Johnstona tam „działają”.

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
