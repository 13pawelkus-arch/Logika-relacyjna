# Sesja wzorcowa — jak wygląda praca

**Czytać na początku sesji, po `STOP.md`. Jeszcze raz — część „Sprawdzenie własnego wyniku” — zanim cokolwiek wejdzie do pliku głównego albo rejestru.**

To nie jest rama (rama to `logika-relacyjna-v3.5.md`) i nie jest lista zakazów. To dziewięć przypadków z tego projektu, przeprowadzonych tak, jak ma wyglądać robota: zdanie, ruch, wynik, sekcja, z której to wynika. Werdyktów nie trzeba pamiętać, bo następny przypadek będzie inny; trzeba widzieć **ruch** i **skąd on się bierze**. Większość z nich najpierw rozwiązałem źle — numery poprawek prowadzą do rejestru i do drogi w zapisach sesji.

## Skąd się biorą ruchy

- **Prawdziwe są dwa zdania: milczenie i relacja [10].** Stąd jeden kształt dowodu, który wraca wszędzie (R1b-A): cokolwiek miałoby nieść tło — (i) żaden odczyt się nie różni, więc nic nie niesie; (ii) jakiś się różni, więc niesie to układ relacji. Trzeciej możliwości nie ma.
- **Definicja czasu i 3D (R1a) i jej zapis (R1b-F, R1c-F): `X = x⁰·𝟙 + x·σ`.** Trzy składowe `x` to trzy odczyty komplementarne; każdy jest relacją dwóch pozostałych (domknięcie, `d − 2 = 1`). `x⁰` stoi przy 𝟙, które nie rozróżnia żadnych dwóch stanów, i wchodzi do `det X = (x⁰)² − |x|²` z przeciwnym znakiem. To czwarte odniesienie innego rodzaju, a jego odczyt jest czasem. Stąd stożek (światło: `det = 0`, t = 0) i to, że czas nie jest osią.
- **Łańcuch Ø (R1a):** foton, superpozycja, osobliwość, 2D, Planck, pole bez wzbudzenia, tło. Nic z niego nie ma położenia, wartości ani cechy; mówi się o nim tylko od strony znanego otoczenia.

## Przypadki

### 1. „Gęstość energii promieniowania ∝ T⁴, bo czasoprzestrzeń ma cztery wymiary”
- **Ruch:** nie litera, tylko rachunek — z czego jest ta czwórka? Gęstość modów po trzech składowych pędu daje T³: to osie przestrzenne, czyli trzy odczyty komplementarne (wtórny opis 3D, R1b-F D0). Czwarta potęga to energia modu, a energia jest składową przy 𝟙 w `P = E·𝟙 + p·σ` (R1c pkt 3, R1f-2), nie czwartą osią.
- **Wynik:** liczba zostaje, odczyt „cztery wymiary” odpada; 4 = 3 + 1 jako punkty odniesienia (słownik, pułapka 5).
- **Kontrola:** gdyby `x⁰` liczyć jak czwartą σ (obrót Wicka), warunek światła `det P = 0` nie ma rozwiązań poza zerem — nie byłoby czego liczyć.

### 2. „Interwał to długość w czterech wymiarach”
- **Ruch:** co się dzieje ze znakiem? „Długość” to suma kwadratów, czyli 𝟙 potraktowane jak czwarta σ.
- **Wynik:** wcale. Interwał zerowy to światło (`det ρ = 0`, stany czyste, R1c-F), a nie ten sam punkt; bez przeciwnego znaku znika stożek, a z nim porządek (R1c pkt 2, 4, 7).
- **Uwaga:** to zdanie nie ma żadnej podejrzanej litery — błąd siedzi w treści. Przypadek 3 jest odwrotny.

### 3. „Logarytm tylko przy d = 3” (155) — litera wygląda źle, treść jest dobra (245–247)
- **Przebieg:** wycofałem to jako „liczenie osi”, bo 3D nie ma nic wspólnego z liczbą 3 (245). Cofnąłem to w 246, ale w samym cofnięciu jeszcze dwa razy poprawiłem według litery (`M^{4−D}`, „oś czasu”), co cofnęło 247.
- **Ruch, który złapałby to od razu:** najpierw przeczytać w całości sekcję definiującą obiekt, potem oceniać zapis. R1b-F D0: „Przestrzeń := Bᵈ”, więc przestrzenne `d` w rachunku z czasem poza osiami to `d` z R1b. Następnie zapytać, na czym stoi liczba. Nielsen liczy hamiltonowsko: płaszczyzna obiegu i jeden swobodny kierunek, który jest relacją dwóch kierunków obiegu, czyli `d − 2 = 1` (R1b Wniosek 1). Czas wchodzi jako energia.
- **Wynik:** stoi. Odpada tylko „3 = D − 1” w γ_m. Tam trójka to kierunki prostopadłe do pędu w czterech składowych, razem z `x⁰`; po samych osiach przestrzennych ślad tego rzutnika to 2.
- **Rodzaj błędu:** kryterium zawieszone na formie zapisu (222) — sortowanie po tym, jak coś jest napisane, a nie po tym, od czego zależy. Do tego przejście ze skrajności w skrajność.

### 4. „Entropia względna rośnie jak a + b·log₂N — to źródło logarytmu” (170, 182–186)
- **Ruch:** czy wynik zależy od N, gęstości, ℓ, pudła albo siatki? Jeśli tak, opisuje pojemnik, w który wsypano punkty, a nie relacje (R1b-A: tło nie niesie niczego, więc to, co tu „niesie”, jest własnością konstrukcji).
- **Wynik:** gałąź zamknięta na stałe (186, `STOP.md`). Kosztowny rachunek (GPU) był sygnałem ostrzegawczym, nie postępem.

### 5. „Parametr afiniczny wyznacza czas własny i porządek” (191) — poprawne i puste
- **Ruch:** test ze `STOP.md` — co rama po tym wpisie pozwala albo czego zabrania, czego przedtem nie? Tu: nic. To R1c pkt 2, 4 i 7 w notacji OTW.
- **Wynik:** przekład, nie wynik (R1c pkt 9 ma rangę „przekład”). Ten sam los spotkał wpis 210, usunięty z ramy.
- **Odruch, z którego to wychodzi:** gdy pada zdanie, szukam formalnego obiektu, który je potwierdza. Algebra się zgadza, filtr jest czysty — i nic nie przybyło.

### 6. „Milczenie pociąga przezroczystość” (200 → 201 → 211)
- **Przebieg:** 200 postawiło domysł warunkowy. 201 dowiodło, że przy milczeniu `U = V ⊗ W`, a ja zapisałem następnik domysłu jako dowiedziony. Kanał dalej działa jako `VρV†`; świadek stał w pliku dwa razy, jako kontrola dodatnia.
- **Ruch:** po każdym dowodzie zapytać, czy przesłanka domysłu jest jeszcze spełniona przez cokolwiek. Ogólniej: czy moje zdanie nie jest mocniejsze od źródła, które powołuje (211, 222, 244).

### 7. „Położenie skali Plancka na osi biegu”, „położenie v wobec Ø-miejsc” (227–229, 240)
- **Ruch:** czy pytanie nadaje położenie albo wartość czemuś z łańcucha Ø? Planck ≡ 2D ≡ Ø (R1a, GRANICE Ø pkt 2), a `v` jest tłem, „wszędzie ta sama”, więc ≡ Ø (R1d, „Trzy punkty otwarte”, pkt 1).
- **Wynik:** pytanie źle postawione, krok wycofany. `m/m_P` to przepisanie jednostki, nie relacja (B1).
- **Rodzaj błędu (228):** coś, co już stało, dostaje nazwę, położenie albo dowód, których nie miało.

### 8. „[94] pkt 4: masa = miejsce łamania samopodobieństwa” (225)
- **Ruch:** zanim użyję etykiety albo przypiszę zdanie użytkownikowi — ścieżka w źródle, nie streszczenie: `python3 narzedzia/wypowiedzi.py --nr 94 --wymiana`.
- **Wynik:** [94] nie ma punktów; hipoteza to [104]; zdanie o `n_Λ` jest asystenta z [105]; etykietę stworzył późniejszy werdykt. Most do zdania użytkownika usunięty, a hipoteza [104] stoi, tylko bez podparcia asystenta.

### 9. „Warunek Veltmana: człon kwadratowy w cięciu musi znikać” (168)
- **Ruch:** czyje to pytanie? Literatura pyta o „naturalność”. W ramie ten człon zależy od opisu samego cięcia, a nie od stosunku dwóch odczytów (208), a o skali Plancka nic nie można powiedzieć [543].
- **Wynik:** to nie jest warunek ramy (168, [T]: przy λ = 0 wyklucza się z β_λ = 0). Z literatury bierze się formalizm i wynik, nigdy pytanie.
- **Przy każdej cudzej pracy:** co autor mówi, że robi, i czego wynik faktycznie używa. Przy świetle: wolno brać relację odczytów (różnicę czasów przybycia, stosunek linii widma), nie historię światła przed odczytem (ds² = 0).

## Sprawdzenie własnego wyniku

Przyłożyć do tego, co policzone albo ustalone, ruchy z przypadków. Na każde pytanie trzeba umieć odpowiedzieć, wskazując sekcję pliku głównego:

1. **Na czym stoi liczba** — czy na `x⁰` policzonym jak czwarta oś? (1–3)
2. **Czy zależy od N, gęstości, ℓ, pudła, siatki?** (4)
3. **Co rama po wpisie pozwala albo czego zabrania, czego przedtem nie?** (5)
4. **Czy zdanie jest mocniejsze od źródła; czy przesłanka domysłu przeżyła dowód?** (6)
5. **Czy coś z łańcucha Ø dostało położenie, wartość albo cechę?** (7)
6. **Kto co powiedział** — sprawdzone ścieżką w źródle, a nie z etykiety ani streszczenia? (8)
7. **Czyje jest pytanie** — z ramy czy z literatury? (9)
8. **Czy nie poprawiam w drugą stronę** — odrzucam za literę, słowo albo podobieństwo do dawnego błędu, zamiast za to, na czym rzecz stoi? (3)

Jeśli na któreś nie umiem odpowiedzieć sekcją, wpisu nie ma. Zostaje sekcja do przeczytania w całości.

*Nowy przypadek dopisać tylko wtedy, gdy pokazuje ruch, którego tu nie ma. Przypadki 1–2 były testem w 248, więc do testów się już nie nadają.*
