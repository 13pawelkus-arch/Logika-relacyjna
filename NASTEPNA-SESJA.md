# Następny krok: twierdzenie o separatorach dla wag Johnstona — skoki po linkach i zatrzymania (krok 4, 171)

**Jedyny otwarty krok z listy** (krok 9 odpadł w 240). Z dwóch rzeczy, które zostały w 171 — „inne wagi K_R” i „wersja
ilościowa” — ta wiadomość niesie **pierwszą**: ilościowa wymaga progu („skończona dokładność”), którego jeszcze nie umiemy
postawić bez pojemnika, a wagi da się postawić bez gęstości (niżej).

## Skąd ten krok — tylko tyle, ile potrzeba

171 (A11d), dla równych wag (`K = ½C`, sam porządek), komutator `Δ = K − Kᵀ`:

> **Jądro wprost z porządku [T]:** f ∈ ker Δ ⇔ dla każdego elementu z: Σ_{y≻z} f_y = Σ_{y≺z} f_y — każdy element widzi
> nad sobą tyle wagi, co pod sobą.
>
> **Twierdzenie o separatorach [T]:** jeśli dla każdego x maksymalnego w nośniku f istnieje z ≻ x, które spośród nośnika
> ma pod sobą tylko x (z bliźniakami) i przeszłość x, a nad sobą nic, to f jest sumą różnic bliźniaków. […] **Dokładne
> relacje między odczytami istnieją tylko między elementami ≡ albo tam, gdzie brak separatora.**
>
> **Granice, otwarte:** dowód dla równych wag (K ∝ C, sam porządek); inne konstrukcje (sumy po linkach w 3+1, Johnston;
> exp(L), Hinrichsen–Kastrati) dają warunek tego samego kształtu z wagami K_R, ale dowód potrzebuje innego separatora.

I 241 (w tym samym bloku), dla równych wag: *element z dołożony nad S nakłada na zależności S dokładnie jeden warunek:
`Σ f` po `S ∩ przeszłość(z)` = 0* — więc rozróżnialność wraca o tyle, ile przybywa różnych widzianych zbiorów, nie
relacji; struktura bez zatrzymania nie musi dawać separatorów.

**Dlaczego wagi Johnstona da się postawić bez gęstości (sprawdzone w tej sesji, na wzorach z pliku):** 168 pkt 1a i 169 —
*„trajektoria o n skokach ma amplitudę aⁿbⁿ⁻¹; a — skok do następnego elementu, b — zatrzymanie w elemencie pośrednim”*,
w ℝ^{1,3} skoki po linkach, `Φ = a·L` (L — macierz linków), *„K = I + Φ(I − bΦ)⁻¹”*. Stąd:
- **bez masy** `K − I = a·L`: stałe `a` (to ono niesie `√ρ`) nie zmienia jądra — zostaje macierz linków;
- **z masą** `K − I = a·L(I − ab·L)⁻¹ = a·Σ_k (ab)^{k−1}·L^k`: L jest nilpotentna, więc to skończona suma; waga relacji
  x ≺ y = **liczba dróg po linkach z x do y, ważona `(ab)^{liczba zatrzymań}`**. Jądro zależy tylko od porządku i od
  liczby `a·b` — a ta jest odczytem, nie wejściem (206: *„`a·b` nie jest wejściem, jest odczytem”*; 181: jedyny
  bezwymiarowy parametr hop-stop).

Więc pytanie jest o **dowolny porządek** z dwiema konstrukcjami wag ze zliczeń — twierdzenie o strukturze spełniającej
warunek, nie rachunek na pojemniku.

---

## Czytać w całości, zanim cokolwiek

- **blok 171 w `### A11d`** („RURA CZASOPODOBNA NA PORZĄDKU”, z punktem 241 na końcu; ok. 5 tys. znaków);
- **w `## §F1`, blok 154 pkt 1a, podpunkt „Formalizm [L] (ze źródła)”** (Johnston; ok. 0,7 tys.) i **w 169 punkt „na
  porządku”** (`K = I + Φ(I − bΦ)⁻¹`);
- **blok 206 w `### A11d`** (ok. 6 tys.) — dlaczego `a·b` jest odczytem;
- **blok 172–173** (moduł względem O) — 241 łączy brak separatora z modułem; dla linków trzeba sprawdzić, czy to samo.

---

## Zdanie, które ma upaść

> **Dla skoków po linkach (`K − I = a·L`) twierdzenie o separatorach zachodzi w tej samej postaci: dokładne relacje
> między odczytami istnieją tylko między elementami ≡ albo tam, gdzie brak separatora — z separatorem zdefiniowanym
> przez linki (element, który ma link do x i do żadnego innego maksymalnego elementu nośnika). Przy `a·b ≠ 0` jądro jest
> zawarte w jądrze bezmasowym.**

Warunek jądra dla linków, do wypisania przed czymkolwiek: f ∈ ker(L − Lᵀ) ⇔ dla każdego z: Σ_{y: z⋖y} f_y =
Σ_{y: y⋖z} f_y (⋖ — link).

Rozstrzygnięcia wypisane **z góry**:

- **(a) Przechodzi.** Wtedy 171 obejmuje światło (skoki po linkach) i masę; trzeba powiedzieć, co zmienia `a·b` — czy
  jądro z masą jest mniejsze (masa przywraca rozróżnialność), równe, czy zależy od wartości `a·b` (wtedy: czy są
  wyróżnione wartości, i czy to nie jest zbiór miary zero — 201: *„warunek rozstrzyga się na równaniach, nie na
  próbkach”*).
- **(b) Upada:** dla linków istnieje dokładna relacja między elementami nie-≡ mimo separatora linkowego. Wtedy trzeba ją
  **nazwać** — co linki niosą dokładnie, czego porządek nie niesie — i powiedzieć, czy to zdanie o świetle.
- **(c) Źle postawione:** „≡” dla linków nie jest tym samym co bliźniaki porządku (te same link-sąsiedztwa ⇐ bliźniaki,
  ale nie odwrotnie). Wtedy najpierw zdefiniować, co jest ≡ przy skokach po linkach, i dopiero potem pytać.

---

## Co niepewne — i tu jest najwięcej

**241 może się nie przenosić.** Dla linków element z dołożony nad S widzi linkami tylko **maksymalne** elementy
`S ∩ przeszłość(z)` bez pośredników, więc jego warunek to suma po tych elementach, nie po całym widzianym zbiorze. Czy
„rozróżnialność wraca o tyle, ile przybywa różnych widzianych zbiorów” ma odpowiednik — nie wiem. Nie zakładać.

**Kierunek z `a·b`.** Kusi „masa przywraca rozróżnialność, bo dokłada wagi dalszym relacjom”. To jest hipoteza, nie
wynik; szereg w `(ab)` jest skończony, ale jego wkład do jądra może się znosić.

**Hinrichsen–Kastrati (`exp(L)`, arXiv:2604.24812)** — cytowane w 171, nie sprawdzane w tej sesji. Przed użyciem
przeczytać abstrakt (`narzedzia/arxiv_abs.py`).

**Świadkowie, nie dowód.** Losowe małe porządki (jak w `etap27`, `etap33`) wolno użyć do znalezienia kontrprzykładu albo
do kontroli, nigdy jako argumentu „w N% prób”. Twierdzenie ma być na kartce.

---

## Jak NIE robić — z zapisanych błędów tej sesji

- **Położenie dla tła albo Ø** (240, 227–229): `v` jest tłem ≡ Ø (R1d pkt 1), Planck ≡ 2D ≡ Ø — żadne z nich nie ma
  miejsca na osi. Oś biegu to nie arena.
- **Wskazówka użytkownika podcina krok, a nie dokłada materiału** (240): gdy użytkownik mówi „gdzieś już o tym
  mówiliśmy”, najpierw sprawdzić, czy to nie unieważnia tego, co robię.
- **Źródło przed wynikiem** (238): rozstrzygnięcie 237 stało w `masa/8` §5, a ja je wyprowadzałem od nowa. Przed
  wpisem sprawdzić, czy to już nie stoi w pliku, w `masa/` albo w rozmowach.
- **Niesprawdzone nie idzie do pliku głównego** (240): [?] własnego rachunku nie rozsiewać po pięciu sekcjach.

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
