# Pierwsza wiadomość do następnej sesji

**Do wklejenia przez użytkownika jako pierwsza wiadomość.** Plik jest nadpisywany na końcu każdej sesji —
nie dopisywać do niego, nie streszczać w nim ramy. Niesie **bieżący krok**, nie framework.

---

**Bierzemy krok 2 w postaci, jaką dała mu 208: ile Ø-miejsc ma każda relacja zespołu i czy każde daje warunek.** Nie „ile warunków dają granice Ø” — to było polowanie na liczby. Kroki 1 i 3 zamknięte (198–202, 206); [?] z [399] pkt 4 zamknięte (207) — **nie wracać do żadnego z nich.**

Najpierw `git pull`.

---

## Jedna rzecz o sposobie pracy, i jest najważniejsza z dwóch ostatnich sesji

**Przejścia logiczne stoją w transkryptach rozmów, w ODPOWIEDZIACH ASYSTENTA — nie w pliku głównym i nie w wypowiedziach użytkownika.** Plik niesie wnioski. `wypowiedzi.py` oddaje zdania użytkownika, czyli też wnioski. To, **jak** coś się urodziło — co po drodze upadło, które zdanie było czyje — jest wyłącznie w `rozmowa/*.md`, i czyta się to zwykłym grepem po obu stronach.

Użytkownik, dosłownie: *„Użyj tych plików, wyszukaj w nich po słowach i przeczytaj nie tylko to co użytkownik pisze, ale i odpowiedzi asystenta. Tam są wszystkie przejścia logiczne — nie wypisane w skrócie. Tylko to jest podgląd na żywo jak to się wszystko rodziło."*

I druga, powiedziana wprost: **„Trudność każdej sesji to doprowadzić żebyś w końcu widział całość, a nie fragmenty. Bez tego jest dupa blada."** Praktycznie to znaczy: krok, który tylko doszlifowuje policzone twierdzenie albo szuka kolejnej liczby w sektorze, o którym rama wydała werdykt, jest fragmentem — nawet jeśli stoi na liście kroków.

---

## Co trzeba przeczytać, w tej kolejności

1. **`## R1a`** w całości (17 tys. znaków) — tabela granic Ø i blok **207** (trzy warunki = jedna nieidentyczność).
2. **Blok 208 w `### A11d`** — tabela rodzajów 19 odczytów. Bez niej krok 2 wróci do polowania na liczby.
3. **`## §F1`** w całości (71 tys., ~18 tys. tokenów) — „STAN ZESPOŁU" (167), poziomy 1–4 (152–153), 154–155, 165, 183.
4. **Transkrypt źródłowy, wymiany [394]–[401]:** `sed -n '14350,14616p' rozmowa/logika-relacyjna-rozmowa.md`. Tam rodzi się definicja czasu i „3+1 liczy punkty odniesienia, nie osie".

---

## Zdanie do upadku

**Każda relacja zespołu ma dokładnie te Ø-miejsca, które leżą na krańcach jej zakresu, i każde z nich daje jeden warunek; wyjątkiem jest λ, która ma Ø-miejsce wewnątrz zakresu, i to dlatego jest jedyną ustaloną.**

Co już stoi i czego nie trzeba dowodzić od nowa: **183 [T]** — w zespole jednopętlowym tylko λ może przejść przez zero wewnątrz zakresu (cechowanie liniowe w t; Yukawy multiplikatywne, więc y = 0 jest punktem stałym; tylko β_λ ma człon bez λ). **208** — wolna dana każdego sprzężenia jest stosunkiem liczności do jego własnego Ø-miejsca (Landau przy b > 0, transmutacja `n_Λ = n·e^{2π/(b₀α_s)}` dla α₃), a unormowanie Yukaw jest stosunkiem do drugiego końca (`v/m_P`).

Rozstrzygnięcia z góry:
- **Przechodzi** → liczba warunków jest policzona, a nie zgadnięta, i bilans z 149 („15–19 wolnych wobec 1 warunku") dostaje wreszcie drugą stronę.
- **Przechodzi, ale warunków jest mniej niż Ø-miejsc** → trzeba powiedzieć, które Ø-miejsce warunku nie daje **i dlaczego**. Węższy wynik, też wynik.
- **Upada** → Ø-miejsca nie są tym, co ustala wolne dane, i wtedy 208 trzeba przeczytać jeszcze raz, bo to w nim postawiono tę zależność.

---

## Pierwsza rzecz na kartce, bo jest jedyną otwartą z 208

**θ_QCD.** 208 nie rozstrzygnęło jego rodzaju i to jest jedyny [?], jaki stamtąd zostaje:
- jako **faza relacji faz z samą sobą** byłaby samorelacją — a wtedy „Ø z Ø nie jest relacją" (154) dałoby **θ_QCD = 0 w całym zakresie**, nie tylko na końcu, bo θ jednopętlowo **nie biegnie** (inaczej niż λ);
- ale fizyczna jest wyłącznie kombinacja **`θ̄ = θ + arg det M`**, co wiąże θ z Yukawami — czyli czyni ją relacją **dwóch sektorów**, nie samorelacją, i wtedy warunku nie ma.

Rozstrzyga to, **która z tych dwóch postaci jest obiektem ramy**. To jest kartka, nie rachunek. Waga: gdyby wyszła pierwsza, byłaby to **liczba, która mogła wyjść inaczej** (A0) — druga po λ. Natura daje |θ̄| < 10⁻¹⁰. [L] Hamada–Kawai–Kawana dostają θ ≈ 0 z zasady wielu punktów (150) — **wziąć formalizm i wynik, nie pytanie**.

---

## Czego NIE robić

**Nie szukać wartości.** 208 zabrania warunku ramy na odczyt, który nie jest samorelacją — dotyczy to e : μ : τ (166), CKM i przesunięć sprzężeń. Pytanie jest o **rodzaj i liczbę Ø-miejsc**, nie o liczby.

**Nie traktować μ² jako odczytu** (208): „dostrojenie wobec Λ²" nie jest pytaniem ramy; legalną postacią tego pytania jest `v/m_P`.

**Nie uzasadniać niczego pojemnością** (207): „skończona struktura", „brak miejsca", „zdolność zapisu jako rozmiar" — każdy taki argument jest pojemnikiem.

**Nie liczyć na rozsiewie** i nie wracać do gałęzi ze `STOP.md`.

**Nie robić tabel odpowiedniości między R1a a czymkolwiek.** Tabela liczy, a punkt odniesienia innego rodzaju nie jest pozycją na liście (CC 10 straciła na tym dwie wymiany).

---

## Co niepewne

**Czy „Ø-miejsce" jest jednym pojęciem.** W 208 nazwałem tak trzy różne rzeczy: biegun Landaua (relacja rozbiega), transmutację (sprzężenie schodzi do zera), i koniec Plancka (wszystko nieodróżnialne). 183 mówi, że granice Ø są wszędzie i że wiersze tabeli to **przykłady parametru p**, nie lista miejsc — więc może to jedno pojęcie, a może trzy. **Rozstrzygnąć to przed liczeniem warunków**, inaczej liczenie będzie o trzech różnych rzeczach pod jedną nazwą.

**Czego nie sprawdziłem w CC 10:** czy przy dwóch pętlach klasyfikacja z 208 się trzyma (183 mówi [O], rachunkiem niesprawdzone, że struktura w tym punkcie się nie zmienia); i czy „8 stosunków Yukaw" to właściwa liczba niezależnych relacji, czy trzeba ją liczyć inaczej, gdy część z nich nie biegnie.

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
