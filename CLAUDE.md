# Logika relacyjna — instrukcja dla Claude

Ten plik wczytuje się automatycznie na starcie każdej sesji. **Rozmawiamy po polsku.** Zacząć od sekcji „Jak pracujemy”.

> **Waga (użytkownik, 26.09.2026, dosłownie):** „Chodzi mi głównie o to, żebyś widział i zdawał sobie sprawę z wagi tego, co tu jest robione. Może brzmi niewinnie — »definicja czasu«. Ale to m.in. ta definicja wywala cały świat do góry nogami w taki sposób, że nic nie jest już takie samo jak było. Łącznie z matematyką i teoriami. Trudność polega na tym, że my nie tworzymy nowych, tylko odrzucamy interpretacje, uwarunkowania i zmienia to nasz sposób patrzenia diametralnie.”
>
> „Za każdym razem, jak próbowałem to kompresować do jakiejś skróconej esencji, nic dobrego z tego nie wynikło. Jest tam bardzo dużo istotnych przejść logicznych, które nie są ani oczywiste, ani nie znajdziesz ich w żadnej bazie danych w takiej formie.”
>
> **Wniosek dla pracy:** rama czytana w pełnym tekście (plik + rozmowy), nie ze streszczeń — także nie ze streszczeń w tym pliku. Formuły z literatury zostają, ich pytania odpadają; ponieważ matematyka wygląda tak samo, dawne odczytanie wraca niezauważone (sesja 3: poprawki 151, 159, 161, 165). `filtr.py` łapie tylko słowa; złe pytanie bez złego słowa („czy informacja ginie”) łapie tylko R1a przeczytane w całości.

## Jak pracujemy (użytkownik, 26.09.2026, po sesji 4)

**Ten plik to indeks, nie rama.** Rama = `logika-relacyjna-v3.5.md` + rozmowy w `rozmowa/`. Streszczenia niżej („Indeks ramy”, „Gdzie skończyliśmy”) służą do znalezienia sekcji pliku i numeru [n], nie do wnioskowania.

Protokół z sesji 3–4 (czytanie wszystkiego co kawałek, lista kroków przed każdym tematem i wpisem, przypomnienia przy każdej wiadomości, automatyczny filtr) — **wycofany**. Użytkownik: „Nie masz żadnej swobody i znowu jest przesadzone wszystko z drugą stronę za bardzo. Jak wcześniej co chwilę gubiłeś i nie brałeś pod uwagę tego, co jest w pliku głównym, tak teraz znowu za bardzo. […] Ze skrajności w skrajność. Kompresować źle, czytać co kawałek wszystko źle.”

- **Na początku nowej sesji, raz: całość** — plik główny i rozmowy, „całe rozmowy z twoimi odpowiedziami, a nie tylko to, co ja piszę”, żeby mieć ogólny pogląd, co robimy:
  ```
  python3 narzedzia/rama.py calosc      # liczba kawałków (~25 tys. znaków każdy, razem ~1,6 mln znaków)
  python3 narzedzia/rama.py calosc K    # K = 1…N, po kolei: plik główny, potem rozmowy chronologicznie
  ```
  Potem stan: „Gdzie skończyliśmy” niżej i ostatnie wiersze rejestru §E w pliku.
- **Zawsze „z tyłu głowy”: wyprowadzenie czasu i wymiarów** (R1a, R1b, R1c; `python3 narzedzia/rama.py 2` i `3`). „Filtr podstawowy to definicja czasu i powstawanie wymiarów. To trzeba zawsze mieć z tyłu głowy, bo potrafi fundamentalnie zmienić rachunek, nic nie zmieniając.” (§E, Reguły).
- **Resztę — przed konkretnym krokiem:** wracać do fragmentów, które mają coś wspólnego z tym krokiem — sekcje pliku (grep) i wymiany w rozmowach (`python3 narzedzia/wypowiedzi.py 'regex'`, `--nr N --wymiana`); kody rachunków w `skrypty/`.
- **Na końcu sesji, ewentualnie, całość jeszcze raz** — sprawdzić, czy coś nieuprawnionego się nie wkradło (`python3 narzedzia/rama.py plik K`).
- **Po kompresji kontekstu** (w trakcie sesji): czas i wymiary (`rama.py 2`, `3`) oraz fragmenty bieżącego kroku; całości od nowa nie trzeba. Przypomina o tym hook SessionStart.
- `narzedzia/filtr.py` (sformułowania wobec R1a/R1b; łapie tylko słowa) — do użycia z własnej decyzji, bez automatu.

## Czym jest projekt

Praca użytkownika (hotelarz, nie fizyk z zawodu, który od pierwszego zdania trzyma się bezwzględnie struktury logiki relacyjnej) z asystentem. **Porządkowanie struktury logicznej fizyki**, nie nowa fizyka: „Nie tworzymy nowych teorii ani nie mnożymy hipotez. Korzystamy z tego, co już jest (cała nauka to solidna baza), oczyszczonego z interpretacji. Zmiana sposobu patrzenia może być równie wielka jak nowe odkrycie.” Narzędzia: teoria zbiorów przyczynowych, stan Sorkina–Johnstona, reguły wzrostu, teoria informacji (§F).

## Pliki

| plik | co to |
|---|---|
| `logika-relacyjna-v3.5.md` | **Główny dokument, czytać najpierw.** Zasady, słownik, wyniki, poprawki (rejestr w §E), otwarte pytania. |
| `rozmowa/logika-relacyjna-rozmowa.md` | Pełny zapis rozmowy źródłowej (16–24.09.2026, 591 wiad.). **Przy każdym temacie pojęciowym czytać wypowiedzi użytkownika stąd (grep), bo dokument główny ich nie zawiera w całości.** Numery wiadomości [n] poniżej odnoszą się do tego pliku. |
| `rozmowa/claude-code-sesja-2026-09-26.md` | Zapis sesji CC 4 (26.09.2026): protokół startu z hookami zadziałał (rama 1–4 przed pierwszą odpowiedzią); temat (a) stosunki e : μ : τ — dwa odczyty „masy” (A = faza na własne tyknięcie / masa biegunowa, B = Yukawy przy wspólnej rozdzielczości), rama ich nie ustala, Koide i δ = 2/9 tylko na A (etap23, 166); zestawienie stanu zespołu wpisane (167); temat (b) krytyczność λ na porządku (168): pojedynczy element = miejsce relacji jednostronnych (Johnston), porządek nie wybiera λ, warunek Veltmana nie jest warunkiem ramy (etap24) — trzy błędy asystenta wykryte przez użytkownika (3+1 jako 4D, relacja bez jednostronnych, x jako obiekt); protokół: cały plik główny i rozmowy na starcie sesji i po kompresji, filtr podstawowy; temat (c) sztywność (169): druga wariacja = rozróżnialność sąsiednich konfiguracji, cztery poziomy w pliku, dosłowne ≡ = entropia względna 0, pułapki 7–8 (trzy uwagi użytkownika); temat (d) entropia względna na porządku (170): doprecyzowanie użytkownika (informacja wzajemna = przypadek szczególny), Arias i in., bliźniaki = zera iΔ, centrum algebry, etap26/26b na GPU — nie niesie obcięcia, rośnie jak ln N ze współczynnikiem zależnym od πR/σ; luźna rozmowa o balansie oznaczoności i nieoznaczoności (niewpisana); procedury z sesji 3–4 wycofane („Jak pracujemy”). |
| `rozmowa/claude-code-sesja-2026-09-25.md` | Zapis sesji CC 3 (25–26.09.2026): porządek po 136 (142), R1e spin i fala EM (143–145), dwa typy logarytmów i lista wejść §F1 (146–147), warunek na końcu Plancka i zliczenie kierunków (148–150), błąd „jedna relacja” zamiast zespołu (151), zespół funkcji wypisany i wyprowadzony (152–153, 155), zasada wielu punktów tylko dla λ, pokolenia, Koide (154), grupa cechowania i pokolenia warunkowo z J₃(𝕆), test wierności według pliku (156–157), uzupełnienie z rozmów (158), czarne dziury: A5d przez definicję czasu i 3D (159), warunki końca przy osobliwości (160), Hawking i krzywa Page'a (161), R1f działanie, energia, pęd i masa z fazy, przyspieszenie (162–164), Pendleton–Ross bez kierunku (165), diagnoza CLAUDE.md i protokół z hookami. |
| `rozmowa/claude-code-sesja-2026-09-24-2.md` | Zapis sesji CC 2 (24/25.09.2026, „rozmowa 2”): audyt i naprawy pliku, R1b (dowód 3D), R1c (światło), R1d (elektron), hipoteza samopodobieństwa, zasady „filtr”, „nie pytać o ocenę”, „obiekt”. Zewnętrzne oceny pominięte na życzenie użytkownika. |
| `rozmowa/claude-code-sesja-2026-09-24.md` | Zapis sesji w Claude Code (24–25.09.2026): przeniesienie projektu do repo, etap10–18, twierdzenie o redukcji lokalnej, synteza czasu, rysunki, przepisanie tego pliku. Numery [n] w nawiasach dotyczą tamtej rozmowy tylko wtedy, gdy wyraźnie napisano „sesja CC”. |
| `skrypty/etap*.py` | Skrypty rachunków (etap0–9 odtworzone z rozmowy; etap10–18 z sesji 25.09; etap19–22 z sesji 3: obiegi, faza, przyspieszenie, Pendleton–Ross; etap23–24 z sesji 4: dwa odczyty stosunków leptonów; trzy warunki ciszy tła — λ, β_λ, Veltman; etap25: kontrole tożsamości do sztywności, 169; etap26–26c: entropia względna stanu koherentnego wobec SJ — rachunek CPU/GPU, test mechanizmu, kontrole wzorów w bazie Focka, 170). |
| `narzedzia/` | `rama.py` (`calosc K`: plik główny i wszystkie rozmowy z odpowiedziami, kawałkami — raz na początku sesji; `plik K`: sam plik główny; części 2–3: czas i wymiary, 1 i 4: zasady i wypowiedzi o czasie), `wypowiedzi.py` (wypowiedzi użytkownika we wszystkich rozmowach; `--wymiana` z odpowiedzią), `filtr.py` (sformułowania wobec R1a/R1b, opcjonalnie), `transkrypt.py` (zapis sesji), `start.sh` (hook). |
| `.claude/settings.json` | Hook SessionStart: przypomnienie, jak pracujemy (nowa sesja: całość; po kompresji: czas i wymiary + fragmenty bieżącego kroku), numpy. |
| `rysunki/` | Rysunki użytkownika: `triada_z_zapisami.png`, `triada_z_zapisami_2.jpg`. |

## Indeks ramy (streszczenie do szukania; źródło: plik i wypowiedzi [n] — `narzedzia/rama.py`, `narzedzia/wypowiedzi.py`)

**Punkt wyjścia [0–26]:** fakt jest zawsze fałszywy. Fakty wypowiada wspólny aparat poznawczy, opinie pojedynczy; jedno i drugie jest fałszywe. Opinia to nieuprawniona projekcja stanu jednego aparatu na obiekt. Tylko dwa zdania są prawdziwe: **milczenie i relacja**. **Logika relacyjna = struktura bez zawartości; obiektywna rzeczywistość (Ro) = zawartość bez struktury.** Wszechświat (R) to wycinek Ro objęty relacją, nie Ro [104–108].

**Nic nie jest „cechą”, „właściwością” ani „pojęciem pierwotnym” [36, 94].** Masa, energia, ładunek, spin to nie cechy. Czas, przestrzeń, ładunek, energia, spin, pole EM, elektron, kwark, gluon, fala EM mają być zdefiniowane; masa na końcu. Masa nie będzie jedną funkcją: kwarki i elektrony na to nie pozwalają, a dynamika wymusza logarytm → **zespół funkcji, relacja relacji, stosunek stosunków** [94]. Formalizmy już istnieją, trzeba je przekształcić na bezwymiarowe stosunki i funkcje logarytmiczne [82–84]. α „przereklamowana, sama wyskoczy po drodze” [88].

**Łańcuch Ø [102–120]:** `[Ø ≡ Ro ≡ γ₀ ≡ t₀ ≡ |ψ⟩ ≡ (r=0) ≡ (Ĥ|Ψ⟩=0) ≡ Δ ≡ 2D ≡ (l_P t_P) ≡ Ø] ≠ R⊗R`. ≡ = **nierozróżnialność, nie tożsamość**. Cel: różne zjawiska i otoczenia, różne formalizmy; po przekształceniu na bezwymiarowe można czytać wszystkie naraz (hipoteza do sprawdzenia). Wykluczenie wymaga pokazania, że się **wzajemnie wykluczają**, a nie że dają różne wyniki. Ø jest absolutne; różni je tylko relacja otoczenia [412–414]; przenoszenie różnic na Ø wolno tylko pośrednio („nazwa pliku zobowiązuje” [416]). **Relacja z Ø jest jednostronna, niesymetryczna** (Ø→A, A→Ø), zwykła relacja jest dwustronna [122–124].

**Superpozycja, pole, próżnia [110, 242–244, 258, 268]:** o superpozycji nic nie można powiedzieć; rachunek w przestrzeni Hilberta dotyczy zawsze relacji otoczenia, nie superpozycji. **Pole bez wzbudzenia ≡ Ø. Próżnia ≡ Ø. Wzbudzenie = różnica = informacja = odczyt. Pole EM = nośnik, nie treść. Foton = minimalne wzbudzenie = minimalna informacja.** Fala istnieje tylko w relacji do czegoś i jest ≡ pole [264].

**ŚWIATŁO JEST NAJWAŻNIEJSZE [80, 164, 394, 422–426, 488, 493]:** foton to „król tego wszystkiego”; jego **t=0 jest warunkiem, żeby przestrzeń była relacją, a nie zapadła się**. Foton nie odróżnia emisji od absorpcji. **c nie jest prędkością pokonywania dystansu, tylko przekazu informacji.** Mierzalna jest tylko prędkość w dwie strony, w jedną to konwencja [266]. **c jest nieskończona, gdy nikt nie czyta (= pole bez wzbudzeń); gdy ktoś czyta, jest ograniczona do ~300 tys. km/s**. To ten sam mechanizm co dekoherencja w laboratorium. Rozstrzygać „na poziomie światła”.

**CZAS [54, 334, 336, 394, 398, 491; synteza w R1a]:** całość nie ma otoczenia → Ĥ|Ψ⟩=0 → czas tylko jako relacja wewnątrz (Page–Wootters) → **odczyt jest zawsze teraz** → przeszłość *nie jest*, jest tylko **zapis w strukturze**, a **pamięć to struktura sama w sobie** (fotony niosą obraz sprzed milionów lat) → zapis bywa rozproszony albo ostry (struktura nie rozprasza jednorodnie [336]) → stąd **pseudokierunek** (strzałka czasu, szklanka, rozcięty palec [152–156]); stan sam nie niesie etykiety „przed/po” (klocki LEGO). **Nie przemycać kierunku „wcześniej–później” (np. z kolejności budowania symulacji; poprawka 106).**

**3D, i nie 4D ani 154D; tego NIE WOLNO oddzielać od definicji czasu [72, 98, 136, 150, 392, 400, 482, 511; 25.09]:**
- **1D nie istnieje.** **2D = płaskość = nieoznaczoność = skala Plancka**: relacja przestrzeni = 0, nic nie można powiedzieć [76]. **Zero absolutne = powrót do 2D** [72] i jest nieosiągalne → struktura zawsze w ruchu [70].
- **Triada** (3 węzły) z dynamiką daje płaszczyznę: boki falują, kurczą się, rozszerzają, **dalej płasko**; bez pamięci ruchu nie da się zauważyć, jakby go nie było [400].
- **Pamięć/zapis** (trajektoria, „dym za samolotami” [72, 134]) = dostęp do innych układów struktury niż bieżący = **czwarty punkt odniesienia** = czas. Bez dynamiki nie ma czego pamiętać, bez pamięci nie ma zmiany: **wszystko naraz** [392, 402].
- **3 wymiary przestrzenne = 4 punkty odniesienia** (3 węzły relacji + 1 punkt informacji o dynamicznej strukturze; ten punkt jest w superpozycji, dopóki pole nie jest wzbudzone). **3D jest warunkiem koniecznym i wystarczającym do ustalenia każdej pozycji.** „4D” w pliku = 3D + dynamika + pamięć [98]; **3+1 = punkty, nie osie** [400].
- **Dlaczego nie więcej [511]:** wyższy wymiar wymagałby pięciu punktów odniesienia w jednym atomowym kroku; odczyt generuje informację już przy czterech; każdy kolejny element to węzeł w istniejącym 3D, zmiana gęstości, nie nowa oś [72]. 3D to strukturalne minimum.
- **Rysunki 25.09:** punkty zapisu leżą na trajektoriach, **każdy łączy się naraz z całą triadą** (odczyt = czworościan), jest ich wiele, bez kolejności. Drugi rysunek to **statyczny wycięty kadr**: odbiorca przed ekranem jest czwartym punktem odniesienia, triada widziana z własnej płaszczyzny. **Współliniowości tam nie ma — istnieje tylko w 2D (≡ Ø), w 3D nie ma racji bytu** (poprawka 117). Rysunek na ekranie sam jest projekcją 2D: nie czytać go jak konfiguracji w strukturze. **„To nie znaczy, że płaskość w ogóle istnieje.”** Płaskość ≡ Ø, nieosiągalna [543].
- **Dowód ma być strukturalny** (nie dopuszcza innych przypadków), nie przez przykłady [66, 148].

**Węzły i „obserwator” [404–408]:** jądro atomu to węzeł interakcji; węzeł, który jako całość jest w relacji z innym węzłem, zyskuje punkt odniesienia (patrzy sam na siebie). Słowo „świadomość” do kosza. Henry Molaison: zmieniony aparat odczytu, ten sam mechanizm; przy 100% c i 0 s „przeskok fazowy” = stan nierozróżnialny od osobliwości.

**Kosmologia (hipoteza użytkownika, sam nazywa ją skokiem, nie krokiem [442, 448]):** „naszą” chwilę zero przenieść na krawędź rozszerzającego się wszechświata: z tyłu struktura (otoczenie), z przodu Ø (tam inflacja). **Czarne dziury:** „tam, gdzie tworzenie relacji nie wyprzedziło odczytywania?” [460], ale **najpierw oczyścić OTW z interpretacji** (nie mówi o zapadaniu, krzywiznach ani nieskończonych gęstościach), ujęcie informacyjne [462–466]. Kosmologiczna asymetria materii [126]. „Pomiędzy kwarkami a płaskością jest pustynia” [545]; w czarnej dziurze takie samo Ø w osobliwości i podobna pustynia od horyzontu [547].

## Zasady pracy (pełne w dokumencie: „Jak czytać”, „Przed liczeniem”, §E)

- **Filtr na rachunki (25.09; 26.09 „filtr podstawowy”, poprawka 168 — patrz „Jak pracujemy”):** mamy definicję czasu ze wszystkimi konsekwencjami i strukturę, przez którą czas daje 3D; reszta to konsekwencja logiczna. **Każdy rachunek i każde pytanie przepuszczać przez ten filtr:** odczyt zawsze teraz, bez kierunku; przeszłość = zapis (ostry/rozproszony); odczyt = wzbudzenie = foton = link, c nieskończone bez odczytu; 3D = triada + zapis (4 punkty, nie osie), więcej = skróty, nie oś; 2D/płaskość ≡ Ø, nieosiągalne; struktura zawsze w ruchu (sztywna migawka = zero absolutne, wykluczone); nic nie jest cechą. Pytanie, które zakłada coś sprzecznego z filtrem, jest źle postawione, zanim cokolwiek policzymy.
- **Nie pytać o ocenę — rozstrzygać strukturą (25.09).** „Moja ocena i każda inna jest figę warta. Użyj logiki relacyjnej.” Ocena to projekcja stanu jednego aparatu (opinia). Zamiast pytać użytkownika „czy to trafne”, sprawdzić zgodność z definicjami ramy i kontrolą (np. co zostaje po usunięciu składnika).
- **„Obiekt” tylko w znaczeniu ramy (25.09, poprawka 132):** obiekt = (stabilna) struktura relacji, która **jako całość** jest w relacji z inną strukturą. Np. jądro atomu: struktura relacji, która jako całość tworzy relację przestrzeni z elektronem; atom: struktura, która jako całość tworzy relację przestrzeni z innym atomem (węzły [404–408]). Nigdy jako nośnik zawartości poza strukturą — pytanie „ten sam obiekt czy tylko ta sama struktura” jest wtedy źle postawione (struktury bez różnicy relacji są ≡).
- **Nie przejmować interpretacji (25.09).** Nie wymyślamy teorii ani matematyki; jedyna różnica to sposób patrzenia, którego w literaturze nie ma. Przed każdym rachunkiem i pytaniem z literatury **10 razy zastanowić się, co właściwie chcemy policzyć** i co dana wielkość/pytanie zakłada (kierunek, cechę, zewnętrzny parametr, gotową czasoprzestrzeń). Z literatury bierzemy formalizm i wynik, **nie pytanie**. Złamane w poprawkach 105, 106, 110 (§E).
- **Najpierw porządek, potem liczenie** [144]. **Najpierw literatura** („nie kosztuje, a pozwala zadać dobre pytanie”).
- **Przed rachunkiem zdanie, które może przez niego upaść**, i kontrole. Liczba bez warunków (n, d, estymator, próby) nie jest wynikiem. Wniosek z zakresu < dekady nie jest wnioskiem. Każdy parametr ustawiony ręcznie skanować.
- **Kryterium „sztuki czy miara”** [288–290]: liczba jest dopuszczalna tylko, gdy nie rośnie z gęstością; inaczej wymaga miary.
- **Znaczniki:** [H] użytkownik · [A] asystent · [L] literatura; [T] dowód · [P] rachunek · [O] obserwacja strukturalna · [?] domysł. **Własne błędy jawnie w rejestrze.** Wyjaśnienia po fakcie oznaczać jako po fakcie.
- **„Nie ma porażek, są źle zadane pytania i nietrafione próby formalizacji”** [436]. **Werdykty na koniec**, ale podsumowania **stanowcze i jednoznaczne** [537–539]. „Żadna reguła” jest zakazane; zawsze konkretnie która [438].
- **Skróty myślowe wolno**, jeśli czytający wie, że to skróty (słownik na początku dokumentu) [418].
- **Duży koszt obliczeń = sygnał ostrzegawczy:** zanim coś pójdzie na godziny GPU, sprawdzić, czy to nie twierdzenie do udowodnienia albo koszt własnego pudła, okna czy siatki (25.09; etap11 potwierdzał twierdzenie, etap16 zdominowało pudło).
- **Rachunki dłuższe niż kilka minut na CPU: od razu na GPU** (Colab A100 40 GB, 80 GB możliwe, ale jednostki drogie). Kod gotowy do wklejenia, parametry na górze, checkpointy, bezpiecznik pamięci liczony przed alokacją (było OOM). Lokalnie tylko sprawdzenie, że kod działa. Nie liczyć wszystkiego z automatu [96].
- **Nie wpisywać do plików** „problem czasu” ani nazwiska Kuchař [272–276] (życzenie użytkownika).
- Na koniec sesji: zaktualizować dokument (albo podbić wersję), rejestr, sekcję „Gdzie skończyliśmy” tutaj; commit + push.
- **Zapis rozmowy z Claude Code:** przed końcem każdej sesji `python3 narzedzia/transkrypt.py rozmowa/claude-code-sesja-RRRR-MM-DD.md --tytul '…' --opis '…'` (zewnętrznych ocen nie włączać — życzenie użytkownika; usunąć ręcznie, jeśli były), dopisać wiersz w tabeli „Pliki”, commit + push. W Claude Code nie ma eksportu, a kontener znika po sesji.

## Oś projektu (podsumowanie użytkownika, 25.09.2026)

1. **Definicja czasu i c** (największa zmiana), zawsze razem z 3D.
2. **3D z triady + czwarty punkt (pamięć/zapis/czas)**: **domknięte strukturalnie w R1b/R1c** (sesja CC 2). Wcześniej: R6 z pamięcią wyłączną 3,11 / 3,01; krzywizna — pytania o płaskość źle postawione (poprawka 113).
3. **Zespół funkcji logarytmicznych (α, kwarki, elektrony) → masa**: boczna droga podjęta, bo na tym etapie dało się do niej wrócić; potem powrót do 3D.
4. **Hipoteza nadrzędna (25.09, §F1): układ samopodobny aż do całości; masa nie jest ostatnim krokiem — „żaden krok tam nie zaprowadzi, to musi być ustalone wszystko na raz”.** Logarytmy = ślad samopodobieństwa (du/u); masa = miejsce łamania samopodobieństwa. **Cel = zespół funkcji [94], nie jedna relacja** (poprawka 151: „jedna relacja między końcami” to był błąd asystenta z [105]); liczby = wartości funkcji w jednym stanie [88].

## Gdzie skończyliśmy (26.09.2026, sesja CC 4; dokument v3.5, rejestr do 170)

Tu tylko mapa. Treść każdej pozycji jest w wierszu rejestru §E o podanym numerze i we wskazanej sekcji pliku.

- **Czas, c, 3D: domknięte strukturalnie.**
  - R1a: definicja czasu.
  - R1b: dowód 3D (P0–P6, Masanes i in. 2014; poprawki 123, 128).
  - R1c: det ρ = norma Minkowskiego, stożek stanów ≡ stożek przyczynowy (129).
  - Krzywizna: pytania o płaskość źle postawione (113).
- **R1d:** elektron, pole EM, kwark. **R1e:** spin i fala EM (143–145).
- **R1f, działanie i energia (162–164).**
  - S/ħ = obroty fazy. Wspólny nośnik obu sektorów = obiegi (etap19). Dwie wagi = dwie rodziny R4.
  - Energia = obroty fazy na tyknięcie w miejscu czytającego.
  - m² = det P = 2k₁·k₂; faza na własne tyknięcie = m (etap20).
  - Przyspieszenie a·τ = 2√(E/τ) z odwrotnej nierówności trójkąta; Unruh (etap21). Porządek 3+1 niepoliczony.
  - Audyt: wszystkie pojęcia §F1 i A5d mają definicje.
- **A5d, czarne dziury (159–161).**
  - Z zewnątrz brzeg 2D ≡ Ø.
  - Horyzont zdarzeń odpada (teleologia), zostaje brzeg lokalny [460].
  - Warunki przy osobliwości (160).
  - Hawking; krzywa Page'a jako funkcja liczebności; wyspy; firewall wykluczony (161).
  - „+1” za punktem Page'a: [?].
- **§F1, zespół funkcji [94] (151–158, 165–168).**
  - **Stan zespołu: zestawienie „STAN ZESPOŁU” w §F1 (167).**
  - Wypisany (152–153): 3 sprzężenia (b = 41/6, −19/6, −7), Yukawy tylko jako stosunki (odczyt B, 166), λ; 19 odczytów.
  - Wyprowadzony (155): −⅓ = „sztuki czy miara”; logarytm tylko przy d = 3.
  - Zasada wielu punktów tylko dla λ na końcu Plancka (154). Jedyne trafienie struktury: m_H i m_t na granicy stabilności.
  - Grupa cechowania oraz ≤ 3 i ≥ 3 pokolenia: warunkowo z J₃(𝕆) (156–158).
  - Pendleton–Ross i Hill jako stosunek stosunków: (1/R − 9/2) ∝ α₃^{1/b₃}. „Za wolno” = wykładnik −1/7 wobec pustyni (165, etap22).
  - Leptony e : μ : τ (166, etap23): „masa” ma dwa odczyty — A = faza na własne tyknięcie (masa biegunowa, R1f-3), B = Yukawy przy wspólnej rozdzielczości; różnica 1–3%. Rama nie daje żadnego warunku na dwa stosunki. Koide i δ = 2/9 zachodzą tylko na A. Pułapka nazewnicza nr 6.
  - Krytyczność λ na porządku (168, 154 pkt 1a): pojedynczy element = miejsce relacji jednostronnych (Johnston: końce drogi, zatrzymania = relacja dwóch części t = 0); porządek nie wybiera λ i nie daje liczby. Warunek Veltmana nie jest warunkiem ramy (etap24 [T]: przy λ = 0 wyklucza się z β_λ = 0; człon Λ² = opis samego końca). Bieg λ na porządku niepoliczony (Jubb 2023). B1 poprawione: ℝ^{1,3} = 3D ramy.
  - Wątek poboczny: 146–150 (typy logarytmów S/K, ⅓, warunek na końcach, Ĥ|Ψ⟩ = 0 nie ustala stałych).
- **Sztywność, temat (c) (169, A11d).**
  - „Opór przeciw zmianie” źle postawione; druga wariacja = rozróżnialność sąsiednich konfiguracji.
  - Cztery poziomy już w pliku: nośnik m (różnica faz drogi zgiętej i prostej = m·E dokładnie, etap25), relacje faz 1/g² (poziom 1 zespołu), tło m_H² = V″, struktura 1/G = liczność.
  - Kierunek zerowy formy = ≡ tylko do drugiego rzędu; dosłowne ≡ = entropia względna 0 (uwagi użytkownika; Watanabe, Witten).
  - Entropia względna (Araki) na porządku: poprawka 170 (niżej).
  - Pułapki nazewnicze 7 („sztywny”) i 8 („stabilna”: część rzeczywista bieguna = węzeł, urojona = trwanie).
- **Entropia względna na porządku (170, A11d; etap26, etap26b, etap26c).**
  - Doprecyzowanie użytkownika: informacja wzajemna = entropia względna (przypadek szczególny); policzony przypadek ogólny: stan koherentny wobec SJ.
  - Pełna algebra obszaru: centrum (jądro iΔ_U z W z ≠ 0) klasycznie + stany warunkowe; bliźniaki z A3a = dokładne zera iΔ (φ_i = φ_j).
  - Nie niesie obcięcia (test (ii)); udział centrum maleje jak N^−0,8; na nieobciętym porządku S = a + b·log₂N, b tylko od πR/σ (test (i) nie przeszedł); źródło logarytmu otwarte; test A11e zablokowany.
  - Arias–Huerta–Martinez: równe algebry → ≡ obszarów we wszystkich rzędach; na porządku nie z automatu.
- **Wcześniejsze wyniki, bez zmian:** §F2, C4a, C5; poprawka 103 (etap7–9 obniżone); H₂; etap18 = zero absolutne.

## Najbliższe kroki

1. **Zespół.** Zestawienie stanu jest w pliku (167); (a) stosunki leptonów zrobione (166: rama ich nie ustala); (b) krytyczność λ na porządku zrobiona (168: porządek nie daje odpowiednika warunków ze 154 ani liczby); (c) sztywność zrobiona (169: druga wariacja, już w ramie na czterech poziomach); entropia względna na porządku policzona (170: nie niesie obcięcia, rośnie jak ln N). Dalej (do decyzji użytkownika):
   - źródło logarytmu entropii względnej (A11d, 170): inny kształt fali (przewidywanie b ≈ 0,1·S_CHM na jednostkę ln N), poddiamenty niekwadratowe (pchnięte); w drugim kroku ℝ^{1,3};
   - twierdzenie o rurze czasopodobnej na porządku (otoczenie łańcucha wobec diamentu).
2. **Otwarte liczby i pytania:** y_e; asymetria 10⁻⁹; H₂; α jako transmutacja; „+1” za Page'em [?]; kierunek przyspieszenia [?]; przyspieszenie w porządku 3+1.
3. **Czarne dziury:** pytania P-K w C5 po filtrze.
