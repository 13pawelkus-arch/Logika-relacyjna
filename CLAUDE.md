# Logika relacyjna — instrukcja dla Claude

Ten plik wczytuje się automatycznie na starcie każdej sesji. **Rozmawiamy po polsku.** Zacząć od sekcji PROTOKÓŁ.

> **Waga (użytkownik, 26.09.2026, dosłownie):** „Chodzi mi głównie o to, żebyś widział i zdawał sobie sprawę z wagi tego, co tu jest robione. Może brzmi niewinnie — »definicja czasu«. Ale to m.in. ta definicja wywala cały świat do góry nogami w taki sposób, że nic nie jest już takie samo jak było. Łącznie z matematyką i teoriami. Trudność polega na tym, że my nie tworzymy nowych, tylko odrzucamy interpretacje, uwarunkowania i zmienia to nasz sposób patrzenia diametralnie.”
>
> „Za każdym razem, jak próbowałem to kompresować do jakiejś skróconej esencji, nic dobrego z tego nie wynikło. Jest tam bardzo dużo istotnych przejść logicznych, które nie są ani oczywiste, ani nie znajdziesz ich w żadnej bazie danych w takiej formie.”
>
> **Wniosek dla pracy:** rama czytana w pełnym tekście (plik + rozmowy), nie ze streszczeń — także nie ze streszczeń w tym pliku. Formuły z literatury zostają, ich pytania odpadają; ponieważ matematyka wygląda tak samo, dawne odczytanie wraca niezauważone (sesja 3: poprawki 151, 159, 161, 165). `filtr.py` łapie tylko słowa; złe pytanie bez złego słowa („czy informacja ginie”) łapie tylko R1a przeczytane w całości.

## PROTOKÓŁ — czytać przed wszystkim innym

**Ten plik to indeks i protokół, nie rama.** Rama = `logika-relacyjna-v3.5.md` + wypowiedzi użytkownika w `rozmowa/`. Streszczenia niżej („Indeks ramy”, „Gdzie skończyliśmy”) służą do znalezienia sekcji pliku i numeru [n], **nie do wnioskowania ani do testu wierności**.

**1. Start sesji i po każdej kompresji kontekstu: cały plik główny i wszystkie wypowiedzi użytkownika.** Użytkownik (26.09, po poprawce 168): „Wystarczyło czytać plik główny i rozmowy na początku + na bieżąco. To nie jest tanie, ale jak widać konieczne.” Hook SessionStart to przypomina; hook UserPromptSubmit przypomina przy każdej wiadomości i wypisuje brakujące kawałki. Po kolei, w całości:
```
python3 narzedzia/rama.py plik          # liczba kawałków (~24 tys. znaków; Read ucina długie linie)
python3 narzedzia/rama.py plik K        # K = 1…N: cały plik główny
python3 narzedzia/rama.py rozmowy K     # K = 1…M: wypowiedzi użytkownika ze wszystkich rozmów, bez powtórzeń
```
Na bieżąco: krok 2 przy każdym temacie. Części `rama.py 1–4` (Jak czytać … Reguły; R1a; R1b + R1c; wypowiedzi o czasie, 3D, świetle) służą do powrotu w trakcie sesji; w całości zawierają się w powyższym.

**Filtr podstawowy (użytkownik, 26.09):** „Filtr podstawowy to definicja czasu i powstawanie wymiarów. To trzeba zawsze mieć z tyłu głowy, bo potrafi fundamentalnie zmienić rachunek, nic nie zmieniając.” W pliku: §E, Reguły (poprawka 168). Nowych wzorców do `filtr.py` nie dopisywać: „Filtry sobie daruj, bo w końcu przepiszesz cały plik główny w formie filtrów.”

Stan: „Gdzie skończyliśmy” niżej i ostatnie wiersze rejestru §E w pliku.

**2. Przed każdym tematem, rachunkiem i wpisem.** Dotyczy każdego kroku, także po „Ok”, „Wpisuj”, „Zaczynaj”: to zgoda na treść, nie zwolnienie z kroków.
1. **Wypowiedzi użytkownika na ten temat.**
   - Polecenie: `python3 narzedzia/wypowiedzi.py 'regex'` (przeszukuje wszystkie rozmowy; opcje `--pelne`, `--nr 94,104`).
   - W odpowiedzi podać numery [n], na których się opieram.
   - Te same słowa nie znaczą tego samego pojęcia: „relacja relacji” u użytkownika jest szersza niż u asystenta (158).
2. **Co już jest w pliku.** Grep tematu w `logika-relacyjna-v3.5.md`: przekształcenia, wcześniejsze wyniki, wiersze rejestru §E (czy ten temat miał już błąd). Nie wypisywać od nowa tego, co już jest.
3. **Test wierności robić wobec pliku, nie wobec CLAUDE.md.** Sekcje: Dopuszczalne stany, Sito, A0, A1, Cel, Dalej otwarte oraz R1a i R1b.
4. **Sformułowania przepuścić przez R1a i R1b.**
   - Odczyt jest zawsze teraz. Zamiast przebiegu: stosunek dwóch punktów odniesienia. Nic nie jest cechą.
   - Hook PostToolUse sam uruchamia `narzedzia/filtr.py` na diffie pliku głównego i CLAUDE.md. Ostrzeżenie w zdaniu merytorycznym oznacza: przeformułować.
   - Szkic można sprawdzić przed wpisem: `echo '…' | python3 narzedzia/filtr.py`.
5. **Formalizm z literatury: pełny i ze źródła, nie z pamięci.** Wszystkie człony, dane i parametry. Do tego pytanie: co zakłada pytanie wzięte z literatury.

**Dlaczego tak (diagnoza sesji 3, 25–26.09.2026).**
- CLAUDE.md miał 26 KB streszczeń i dawał złudzenie znajomości ramy.
- Instrukcja „czytać wypowiedzi użytkownika (grep)” nie miała wyzwalacza.
- „Wpisuj” było wykonywane od razu, bez sprawdzeń.

Interwencje użytkownika:

| wypowiedź użytkownika | co się stało | pominięty krok |
|---|---|---|
| „Najpierw wróć do plików poprzednich rozmów i porównaj…” | Wpis o zespole zrobiony bez ani jednego grepa rozmów. Zdanie [104] wzięte ze streszczenia jako „jedna relacja między końcami”, co przeczy [94] (poprawka 151). | 2.1 |
| „A przekształcenia są chyba wszystkie już w pliku” | Przed wypisaniem nie sprawdzono A2 i R1d. | 2.2 |
| „Zweryfikuj te uwagi” | Równania wypisane z pamięci, niepełne: brak członu śladowego T, −3/2·y_t², θ_QCD (153). | 2.5 |
| „Rama to plik logika relacyjna. Przejrzyj go…” | Test wierności zrobiony wobec CLAUDE.md. Dopuszczalne stany, Sito, A0, A1 nieprzeczytane. „Dlaczego 𝕆” rozstrzygane od strony Ø (157). | 1, 2.3 |
| „Przejrzyj jeszcze rozmowy zanim zaczniesz” | Pominięte [104] R ⊗ R (158). | 2.1 |
| „Zapoznaj się dokładnie z definicją czasu, oraz wyprowadzenia wymiaru 3D…” | R1a przeczytane pierwszy raz dopiero po 25 wymianach. Analiza czarnych dziur z „ostatnim odczytem”, „powstają”, „przepływem” (159). | 1, 2.4 |
| „3+1 to nie znaczy 4D… samo x jest relacją / zbiorem relacji… Przeczytaj plik główny cały” (sesja 4) | Analiza (b) po kompresji, z ramą 1–4, bez całego pliku: 3+1 wzięte za cztery wymiary; „relacja wymaga dwóch różnych elementów” bez relacji jednostronnych (154 miało to dobrze); x jako obiekt (x ≺ x). Żadne z trzech zdań nie dało ostrzeżenia filtra (168). | 1 (cały plik), 2.3, 2.4 |

Hooki są w `.claude/settings.json`, znaczniki w `/tmp/logika-rama/`. Jeśli komunikat „PROTOKÓŁ STARTU” nie pojawił się na starcie sesji, hook nie zadziałał. Protokół obowiązuje wtedy tak samo.

## Czym jest projekt

Praca użytkownika (hotelarz, nie fizyk z zawodu, który od pierwszego zdania trzyma się bezwzględnie struktury logiki relacyjnej) z asystentem. **Porządkowanie struktury logicznej fizyki**, nie nowa fizyka: „Nie tworzymy nowych teorii ani nie mnożymy hipotez. Korzystamy z tego, co już jest (cała nauka to solidna baza), oczyszczonego z interpretacji. Zmiana sposobu patrzenia może być równie wielka jak nowe odkrycie.” Narzędzia: teoria zbiorów przyczynowych, stan Sorkina–Johnstona, reguły wzrostu, teoria informacji (§F).

## Pliki

| plik | co to |
|---|---|
| `logika-relacyjna-v3.5.md` | **Główny dokument, czytać najpierw.** Zasady, słownik, wyniki, poprawki (rejestr w §E), otwarte pytania. |
| `rozmowa/logika-relacyjna-rozmowa.md` | Pełny zapis rozmowy źródłowej (16–24.09.2026, 591 wiad.). **Przy każdym temacie pojęciowym czytać wypowiedzi użytkownika stąd (grep), bo dokument główny ich nie zawiera w całości.** Numery wiadomości [n] poniżej odnoszą się do tego pliku. |
| `rozmowa/claude-code-sesja-2026-09-26.md` | Zapis sesji CC 4 (26.09.2026): protokół startu z hookami zadziałał (rama 1–4 przed pierwszą odpowiedzią); temat (a) stosunki e : μ : τ — dwa odczyty „masy” (A = faza na własne tyknięcie / masa biegunowa, B = Yukawy przy wspólnej rozdzielczości), rama ich nie ustala, Koide i δ = 2/9 tylko na A (etap23, 166); zestawienie stanu zespołu wpisane (167); temat (b) krytyczność λ na porządku (168): pojedynczy element = miejsce relacji jednostronnych (Johnston), porządek nie wybiera λ, warunek Veltmana nie jest warunkiem ramy (etap24) — trzy błędy asystenta wykryte przez użytkownika (3+1 jako 4D, relacja bez jednostronnych, x jako obiekt); protokół: cały plik główny i rozmowy na starcie sesji i po kompresji, filtr podstawowy. |
| `rozmowa/claude-code-sesja-2026-09-25.md` | Zapis sesji CC 3 (25–26.09.2026): porządek po 136 (142), R1e spin i fala EM (143–145), dwa typy logarytmów i lista wejść §F1 (146–147), warunek na końcu Plancka i zliczenie kierunków (148–150), błąd „jedna relacja” zamiast zespołu (151), zespół funkcji wypisany i wyprowadzony (152–153, 155), zasada wielu punktów tylko dla λ, pokolenia, Koide (154), grupa cechowania i pokolenia warunkowo z J₃(𝕆), test wierności według pliku (156–157), uzupełnienie z rozmów (158), czarne dziury: A5d przez definicję czasu i 3D (159), warunki końca przy osobliwości (160), Hawking i krzywa Page'a (161), R1f działanie, energia, pęd i masa z fazy, przyspieszenie (162–164), Pendleton–Ross bez kierunku (165), diagnoza CLAUDE.md i protokół z hookami. |
| `rozmowa/claude-code-sesja-2026-09-24-2.md` | Zapis sesji CC 2 (24/25.09.2026, „rozmowa 2”): audyt i naprawy pliku, R1b (dowód 3D), R1c (światło), R1d (elektron), hipoteza samopodobieństwa, zasady „filtr”, „nie pytać o ocenę”, „obiekt”. Zewnętrzne oceny pominięte na życzenie użytkownika. |
| `rozmowa/claude-code-sesja-2026-09-24.md` | Zapis sesji w Claude Code (24–25.09.2026): przeniesienie projektu do repo, etap10–18, twierdzenie o redukcji lokalnej, synteza czasu, rysunki, przepisanie tego pliku. Numery [n] w nawiasach dotyczą tamtej rozmowy tylko wtedy, gdy wyraźnie napisano „sesja CC”. |
| `skrypty/etap*.py` | Skrypty rachunków (etap0–9 odtworzone z rozmowy; etap10–18 z sesji 25.09; etap19–22 z sesji 3: obiegi, faza, przyspieszenie, Pendleton–Ross; etap23–24 z sesji 4: dwa odczyty stosunków leptonów; trzy warunki ciszy tła — λ, β_λ, Veltman). |
| `narzedzia/` | `rama.py` (cały plik główny i wszystkie wypowiedzi użytkownika kawałkami: `plik K`, `rozmowy K`; części 1–4 do powrotu w trakcie sesji), `wypowiedzi.py` (wypowiedzi użytkownika we wszystkich rozmowach), `filtr.py` (sformułowania wobec R1a/R1b), `transkrypt.py` (zapis sesji), `start.sh` i `przypomnienie.py` (hooki). |
| `.claude/settings.json` | Hooki: SessionStart (protokół startu, numpy), UserPromptSubmit (protokół przy każdej wiadomości; brakujące kawałki pliku i rozmów), PostToolUse (filtr na diffie pliku głównego i CLAUDE.md). |
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

- **Filtr na rachunki (25.09; 26.09 „filtr podstawowy”, poprawka 168 — patrz PROTOKÓŁ):** mamy definicję czasu ze wszystkimi konsekwencjami i strukturę, przez którą czas daje 3D; reszta to konsekwencja logiczna. **Każdy rachunek i każde pytanie przepuszczać przez ten filtr:** odczyt zawsze teraz, bez kierunku; przeszłość = zapis (ostry/rozproszony); odczyt = wzbudzenie = foton = link, c nieskończone bez odczytu; 3D = triada + zapis (4 punkty, nie osie), więcej = skróty, nie oś; 2D/płaskość ≡ Ø, nieosiągalne; struktura zawsze w ruchu (sztywna migawka = zero absolutne, wykluczone); nic nie jest cechą. Pytanie, które zakłada coś sprzecznego z filtrem, jest źle postawione, zanim cokolwiek policzymy.
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

## Gdzie skończyliśmy (26.09.2026, sesja CC 4; dokument v3.5, rejestr do 168)

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
- **Wcześniejsze wyniki, bez zmian:** §F2, C4a, C5; poprawka 103 (etap7–9 obniżone); H₂; etap18 = zero absolutne.

## Najbliższe kroki

1. **Zespół.** Zestawienie stanu jest w pliku (167); (a) stosunki leptonów zrobione (166: rama ich nie ustala); (b) krytyczność λ na porządku zrobiona (168: porządek nie daje odpowiednika warunków ze 154 ani liczby). Dalej:
   - (c) sztywność (A11d). Przed nią PROTOKÓŁ 1: cały plik główny i rozmowy.
2. **Otwarte liczby i pytania:** y_e; asymetria 10⁻⁹; H₂; α jako transmutacja; „+1” za Page'em [?]; kierunek przyspieszenia [?]; przyspieszenie w porządku 3+1.
3. **Czarne dziury:** pytania P-K w C5 po filtrze.
