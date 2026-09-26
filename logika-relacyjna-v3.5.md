# Logika relacyjna — v3.5

> **v3.5 (sesja CC 2, 24/25.09.2026)** = v3.4 + **R1b** (dowód strukturalny 3D z definicji czasu, z zapisem formalnym R1b-F i testem wierności), **R1c** (most do światła i porządku: stożek stanów ≡ stożek przyczynowy), **R1d** (elektron, pole EM, kwark; energia i odległość jako relacje), **hipoteza nadrzędna samopodobieństwa** (§F1), słownik: „obiekt”; poprawki 110–136. Oznaczenia „v3.4” w treści zostają jako historia.

> **v3.4 (25.09):** nowe sekcje **R1b — dowód strukturalny 3D z definicji czasu** i **R1c — most do światła i porządku**, **R1d — elektron, pole EM, kwark** (poprawki 114–133).
>
> **v3.4** = v3.3 + §C4a punkty 1–16 (etap 0, fragmenty, ściskanie, Fokker, entropia) + dopisek o Ĥ|Ψ⟩=0 w R1a + rejestr 25–48.
>
> **v3.3 (wrzesień 2026)** = v3.2 + dopiski z rozmowy 5. Nowe miejsca: R1a, pułapka nr 5, C4, uzupełnienia w „Dalej otwarte”, B1, §D, rejestr (21–24). Reszta bez zmian.

Jeden plik: zasady pracy + słownik. Zapis wielkości fizycznych bez jednostek — wszystko jest liczbą albo stosunkiem liczb.

---

## Jak czytać ten plik

**Cztery pola przy każdym rachunku.** Wartość · kontrola, która przeszła · co by go obaliło · czyja teza. Wartość bez warunków (n, d, estymator, liczba prób) nie jest wynikiem — v2 straciło tak jedną liczbę i wyprodukowało fałszywą zgodność.

**Poprawki stoją przy rachunku, którego dotyczą.** W v2 były zebrane w §E, na końcu, z dala od liczb, które unieważniały. Rejestr zbiorczy jest teraz tylko spisem — treść poprawki jest w miejscu, gdzie działa.

**Znaczniki pochodzenia:** **[H]** teza użytkownika · **[A]** teza asystenta · **[L]** literatura
**Znaczniki ugruntowania:** **[T]** dowód · **[P]** rachunek · **[O]** obserwacja strukturalna · **[?]** domysł

Pochodzenie nie jest uprzejmością. Ma znaczenie diagnostyczne — patrz rejestr w §E.

**ZASADA METODY (użytkownik, v3.4).** **Nie tworzymy nowych teorii ani nie mnożymy hipotez. Korzystamy z tego, co już jest — z całej nauki, która jest solidną bazą — oczyszczonej z interpretacji.** Zmiana sposobu patrzenia może być równie wielka jak nowe odkrycie, jeśli baza jest solidna.
- **Przykład z historii [L]:** transformacje Lorentza istniały przed 1905 r. (Lorentz, Poincaré); Einstein nie dodał matematyki, tylko zmienił sposób patrzenia (bez eteru, jednoczesność zależna od obserwatora). Podobnie Lagrange/Hamilton, całki po trajektoriach Feynmana: te same przewidywania, nowe drogi.
- **Dyscyplina czyszczenia (asystent):** **zostaje to, co mierzalne lub strukturalne; odpada narracja.** Przykład: „przestrzeń wygina się jak płachta” — narracja; krzywizna jako tensor Riemanna — mierzalna (siły pływowe: różnica przyspieszeń dwóch swobodnie spadających ciał obok siebie). Czyszczenie usuwa opowieść, zostawia dane i strukturę.
- **W praktyce v3.4:** prawie każde narzędzie było gotowe (Boguñá–Krioukov, Sorkin–Yazdi, Page–Wootters, Zurek, Jacobson, Bombelli–Henson–Sorkin); nasze było zestawienie i pytania z niego wynikające.

**Skróty myślowe są dozwolone** (użytkownik: „jeszcze nie raz użyję podobnego skrótu”), dopóki czytający wie, że to skróty. Poniższy słownik podaje ich **jednoznaczny odczyt relacyjny**. Tam, gdzie skrót ukrywał prawdziwą zależność, poprawka stoi przy wyniku.

| skrót | odczyt relacyjny | gdzie |
|---|---|---|
| „foton ma t = 0” | interwał między emisją a absorpcją jest zerowy; brak elementów pośrednich | A2, R1a |
| „czas własny τ = L” | długość najdłuższego łańcucha między dwoma elementami = **miara jednego odczytu** wzdłuż trajektorii, **nie czas** | A2, R1a |
| „czas”, „przeszłość” | odczyt informacji ze struktury, zawsze teraz; przeszłość = zapis odczytywany teraz | R1a |
| „prędkość c” | **tempo przekazu informacji** (nie pokonywania dystansu); przelicznik łańcuch ↔ odległość; w jedną stronę konwencja (Reichenbach) | C4a.13, C5 |
| „odległość między zdarzeniami” | nakładanie przyczynowe względem wspólnej przeszłości | C4a.17 |
| „masa cząstki” | [?] częstość samoodczytu trajektorii mierzona względem innego węzła | R1a, B1 |
| „entropia obszaru” | liczba o relacji obszaru z resztą **po wybranym cięciu**; zależy od gęstości globalnej, nie tylko od obszaru | C4a.16e |
| „wymiar”, „3+1”, „d = 4” | liczba **punktów odniesienia** (triada + odczyt), nie osi; mierzona jako skalowanie liczebności przedziałów | R1a, §E |
| „węzeł”, „cząstka” | moduł: podzbiór widziany jednakowo z zewnątrz | R1a |
| „próżnia”, „pole” | Ø od strony danego otoczenia | R1a, §E |
| „Ø ma cechę …” | **zawsze** skrót za „od strony otoczenia X Ø wygląda w naszym opisie jako …” | §E (reguła językowa) |



> **UWAGA OGÓLNA DO v3.2.** Ten plik **nie zawiera wszystkiego, co ustalono**, i nigdy nie zawierał. Rozmowa 3 ma szereg rzeczy ostrzej i pełniej — w szczególności retrospekcję (§R2). Po kontekst w konkretnym temacie należy wracać do rozmowy źródłowej, a nie zakładać, że skrót tutaj jest kompletny. To jest własność pliku, nie usterka: skrót robiony pod jeden wątek gubi to, co było ważne dla innego.

---



## R1. Łańcuch Ø

$$\text{osobliwość}\equiv\text{chwila zero}\equiv\text{foton}\equiv\text{superpozycja}\equiv(t{=}0)\equiv\text{nieoznaczoność}\equiv 2D/\text{Planck}\equiv\varnothing$$

To nie jest lista zjawisk.(Ø jest absolutne, różni je wyłącznie relacja otoczenia) jest to **lista otoczeń indeksowana jednym Ø**. Zjawiska są różne; Ø jest jedno.

Zamysł: zredukować każde z tych miejsc do struktury interakcji, pozbyć się jednostek, przekształcić do bezwymiarowych stosunków — a potem szukać, czy stosunki się powtarzają. Miejsca opisane lepiej mają służyć za kalibrację dla opisanych gorzej. Najgorzej opisana jest chwila zero.

## R1a. Łańcuch Ø — zapis z v3.3 [H]

$$[\varnothing \equiv R_o \equiv \gamma_0 \equiv t_0 \equiv |\psi\rangle \equiv (r{=}0) \equiv (\hat H|\Psi\rangle{=}0) \equiv \Delta \equiv 2D \equiv (l_P\,t_P) \equiv \varnothing] \;\neq\; R\otimes R$$

| symbol | znaczenie |
|---|---|
| ≡ | **nieodróżnialność**, nie tożsamość. Zjawiska są różne; nic ich nie odróżnia od strony Ø |
| $R_o$ | obiektywna rzeczywistość — zawartość bez struktury |
| $\gamma_0$ | foton |
| $t_0$ | chwila zero |
| $\lvert\psi\rangle$ | superpozycja |
| $(r{=}0)$ | osobliwość |
| $\hat H\lvert\Psi\rangle{=}0$ | stan bez ewolucji (Wheeler–DeWitt) — patrz niżej |
| Δ | nieoznaczoność |
| $R$ (pierwsze) | relacja |
| $R$ (drugie) | **wycinek $R_o$ objęty relacją = wszechświat.** Wszechświat ≠ obiektywna rzeczywistość |
| $R\otimes R$ | świat relacji złożonych z relacji |
| obiekt | **(stabilna) struktura relacji, która jako całość jest w relacji z inną strukturą** (użytkownik, 25.09; poprawka 132). Np. jądro atomu = struktura relacji, która jako całość tworzy relację przestrzeni z elektronem; atom jako całość = struktura relacji, która jako całość tworzy relację przestrzeni z innym atomem. Por. węzły [404–408]. **Nie**: nośnik zawartości poza strukturą |

**Cel zapisu:** różne zjawiska mają różne otoczenia i różne formalizmy, które nigdy nie traktują ich jako nieodróżnialnych. Po przekształceniu na bezwymiarowe można czytać wszystkie opisy jednocześnie. **To hipoteza do sprawdzenia**, nie wynik. Porównywalność obala się tylko przez pokazanie, że stosunki się **wzajemnie wykluczają** (np. jeden wymaga addytywności, drugi jej zabrania), a nie przez to, że dają różne wartości — różne wartości wynikają z różnych otoczeń.

**Ĥ|Ψ⟩ = 0 — konsekwencja, nie zagadka [L][H].** Więz hamiltonianowy wynika wprost z niezmienniczości względem reparametryzacji czasu: nie ma zewnętrznego parametru, względem którego całość mogłaby ewoluować. To ten sam brak co przy zachowaniu energii (bez czasopodobnego wektora Killinga nie ma globalnie zachowanej energii): **całość nie ma otoczenia**. Czas wraca jako **korelacja wewnątrz całości**: stan podukładu warunkowany wskazaniem innego podukładu (zegara) zmienia się zgodnie ze zwykłą ewolucją (Page–Wootters 1983; rozwinięcia: Giovannetti–Lloyd–Maccone; układ dwóch fotonów: Moreva i in.). Globalnie nic nie płynie, lokalnie wszystko. **Wzbudzenia i relacje są lokalne.**
**Uwaga [A]:** zero w Ĥ|Ψ⟩=0 („nie ma parametru”) to inne zero niż τ=0 fotonu („interwał znika”); w łańcuchu łączy je nieodróżnialność, nie tożsamość.

**SYNTEZA: CZAS BEZ DOKŁADANIA CZEGOKOLWIEK [H] (użytkownik, 25.09.2026).**
1. Całość nie ma otoczenia → brak zewnętrznego parametru → Ĥ|Ψ⟩ = 0 (standardowa konsekwencja niezmienniczości względem reparametryzacji).
2. Całość nie ewoluuje → czas może być tylko relacją wewnątrz, między podukładami (Page–Wootters).
3. Relacja wewnątrz = czytanie jednego przez drugie; czytanie odbywa się w jednym stanie → **zawsze teraz**.
4. Przeszłość zostaje tylko jako **zapis** w strukturze; zapis jest ostry albo rozproszony → stąd **kierunek**.
5. Zapis = dostęp do innych układów struktury niż bieżący → punkt odniesienia, którego triada nie ma → **3+1 jako punkty, nie osie**.
- **Numeracja 1–5 to kolejność czytania, nie wyprowadzania [H] (poprawka 137).** Definicja czasu powstała razem z warunkami koniecznymi i wystarczającymi dla 3D i osobno by się nie udała; to samo dotyczy P0–P6 w R1b (wszystko naraz [392, 402]).
„Nigdzie po drodze nie trzeba niczego dodawać. Trzeba tylko nie dokładać interpretacji.”
- **Kierunek siedzi w relacji stan–zapis, nie w stanie.** Rozłączone klocki mogą być przed złożeniem i po rozebraniu; rozstrzyga dopiero zapis czytany teraz (pamięć, zdjęcie, ślady). **Ile przeszłości istnieje dla czytającego, zależy od jego zdolności zapisu:** dla mózgu 200 rozsypanych klocków ma mniej przeszłości niż dla aparatu fotograficznego.
- **Nieuchwytność „teraz” [O]:** każda próba uchwycenia odczytu robi z niego zapis; **odczyt nie może być treścią własnego odczytu**. „Teraz” jest aktem, nie zawartością, więc wszystko, co da się złapać, jest już zapisem.
- **[L] Augustyn, *Wyznania* XI, 20:** nie ma trzech czasów, są trzy teraźniejszości: *praesens de praeteritis* = pamięć (*memoria*), *praesens de praesentibus* = oglądanie (*contuitus*), *praesens de futuris* = oczekiwanie (*expectatio*). Niemal dosłownie „przeszłość = zapis czytany teraz”. **[L] Rovelli, „Is time's arrow perspectival?” (2015):** strzałka zależy od tego, które zmienne czytający potrafi odczytać; najbliższy odpowiednik we współczesnej fizyce.
- **Uwagi asystenta [A] (nie są otwartymi pytaniami; poprawki 110, 111):**
  - ~~**„Bez hipotezy przeszłości”:** w literaturze asymetrię zapisów (ślady przeszłości, nie przyszłości) wyprowadza się zwykle z niskiej entropii początku (Albert, Loewer). Rama pokazuje, że kierunek jest w relacji stan–zapis, ale musi jeszcze wyprowadzić **zgodność kierunku między wszystkimi czytającymi** (mózg, aparat, ślady wskazują tę samą stronę). Kandydat: zapisy są wspólne, bo czytający są częścią tej samej struktury. Niesprawdzone.~~ **PYTANIE ŹLE POSTAWIONE — WYCOFANE (użytkownik [H], poprawka 110).** (1) Zakłada kierunek jako cechę struktury, co do której czytający mogą się zgadzać; w ramie kierunek to pseudokierunek [152–154], stan nie niesie etykiety „przed/po”. (2) Każe wyprowadzić definicję: „przeszłość” to nazwa na to, co czytający ma zapisane [394], więc „zapisy wskazują przeszłość” jest tautologią; hipoteza przeszłości jest potrzebna tylko tam, gdzie kierunek jest dany z góry, a zapisy mają się z nim zgadzać. (3) „Wszyscy czytający się zgadzają” to zdanie wspólnego aparatu, czyli fakt [8]; rama mówi odwrotnie: ilość przeszłości zależy od zdolności zapisu (mózg vs aparat, 200 klocków), a nierównomierność bierze się z rozpraszania w strukturze [336] i z tego, że cofnięcie wymagałoby synchronicznego działania całości [154]. **Błąd asystenta:** pytanie przejęte z literatury (Albert, Loewer) razem z jej założeniem.
  - **Status [A]:** wyjaśnienia porażek v0 (wszyscy czytają wszystkich → zapadnięcie), v3/v5 (odczyt szybszy niż produkcja informacji → bezruch) i R2 (zamknięty zbiór trajektorii się wymieszał) przyszły **po** porażkach, więc mają oznaczenie **po fakcie**. To oznaczenie, nie pytanie. Wcześniej zapisana tu „zasada na przyszłość” dublowała istniejącą regułę (zdanie do upadku przed rachunkiem) — usunięta (poprawka 111).
**Zmiana = dynamika × pamięć; hierarchia węzłów [H] (użytkownik, v3.4).** Pierwotna dynamika **produkuje** informację; pamięć ją **przechowuje**. Bez pamięci produkcja przepada — **nie ma zmiany**. Bez dynamiki wszystko stoi i nie ma czego pamiętać — **też nie ma zmiany**. Iloczyn, nie suma: żaden składnik nie wystarcza sam. Wheeler–DeWitt traktują wszechświat jako **jeden węzeł relacji — jako całość statyczny**; zawiera mniejsze węzły, te mniejsze itd., **aż do 2D Plancka**.
- **Czas jest ograniczony z dwóch stron, a OBA BRZEGI SĄ W ŁAŃCUCHU Ø [A]:** od góry — całość bez otoczenia, statyczna ($\hat H|\Psi\rangle=0$); od dołu — skala Plancka, 2D, brak informacji ($l_P t_P$, 2D). Czas istnieje wyłącznie między nimi: w węzłach, które mają otoczenie **i** mają informację. **Łańcuch Ø to brzeg hierarchii, z obu stron.**

**Węzeł, który jako całość jest w relacji z innym węzłem [H] (użytkownik, v3.4).** Mechanizm ogólny, na każdej skali — **słowo „świadomość” usunięte** (przypisuje cechę obiektowi, czyli mechanizm opinii z początku pliku). Przykład: **jądro atomu** jest węzłem interakcji; razem z elektronem tworzy strukturę, która **jako całość** jest w relacji z innym atomem — wnętrze z zewnątrz niewidoczne, relacja idzie przez kilka parametrów całości. Ten sam mechanizm w mózgu (węzły relacjonujące się jako całości); przykład H.M. (Henry Molaison): po operacji brak nowych zapisów deklaratywnych, ale uczenie ruchowe zachowane — **zapis powstawał w strukturze, lecz nie był odczytywalny przez aparat pamięci jawnej** („zawarte” kontra „odczytywalne”).
- **Łańcuch Ø lokalnie:** między brzegami hierarchii (Planck — Wheeler–DeWitt) ten sam stan występuje lokalnie wszędzie, gdzie nic nie jest odróżnione: niewzbudzona próżnia, superpozycja, osobliwość.
- **Zapis w porządku [A]: MODUŁ.** Podzbiór M jest modułem, gdy każdy element spoza M jest w **tej samej** relacji ze wszystkimi elementami M — z zewnątrz M wygląda jak jeden punkt. Moduły tworzą **drzewo dekompozycji modularnej**: korzeń = cała struktura (statyczna całość), liście = pojedyncze elementy (dolny brzeg). **To jest hierarchia węzłów zapisana bez importu.**
  - **bliźniaki z A3a = najmniejsze moduły** (dwa elementy o identycznych relacjach ze wszystkim) — pomysł Rideouta „materia jako wzorce relacji” to pomysł na moduły;
  - **dlaczego w sprinklingu nie ma cząstek, z drugiej strony:** z prawa $n^{k-(k-1)d}$ w 3+1 modułów praktycznie nie ma i jest ich coraz mniej z gęstością — tło nie ma węzłów (zgodne z C4a.21).
  - **Zastrzeżenie:** moduł ścisły jest bardzo wymagający; realny atom jest węzłem tylko w przybliżeniu (z bliska wnętrze widać). Do testów potrzebna wersja przybliżona: **jaki ułamek elementów z zewnątrz widzi podzbiór jednakowo**.

**To samo pięć razy w C4a:** brak globalnego cięcia (C1/C2), brak globalnego zachowania energii, brak pochłaniacza (WF), brak powierzchni Cauchy'ego (plaster), brak podziału otoczenia w próżni — jedna przyczyna: całość nie ma otoczenia, więc nie ma dla niej ani czasu, ani cięcia, ani zachowania.

**Czas [H] — co z tego wynika.** Przeszłości nie ma. Jest **zapis w samej strukturze relacji** (pamięć), a odczyt jest zawsze teraźniejszy: obserwabla w elemencie odczytu to kombinacja danych wejściowych, „przeszłość” wchodzi wyłącznie jako relacje zawarte w tym jednym stanie. **To jest czas.**
**Rozróżnienie, bez którego „informacja nie ginie” zbiera za dużo [A]:** informacja nie ginie **w strukturze**, ale przestaje być **odczytywalna z danego miejsca**. Ta różnica robi całą robotę przy strzałce czasu (szklanka się nie składa, choć nic nie zostało wymazane — A4d).
**DEFINICJA CZASU [H] (użytkownik, v3.4).** **Czas to odczyt informacji ze struktury relacji; odczyt jest zawsze TERAZ.** Przeszłość nie „jest” — jest tylko informacja o konkretnym układzie struktury, **ostra** (łatwa do odczytania) albo **rozproszona** (trudna). „Przeszłość” i „przyszłość” to etykiety **wzorców** względem tego, co da się odczytać: stan „klocki rozłączone” może być i przeszłością, i przyszłością; kierunek daje to, co jest zapisane i czytelne teraz. „Ile temu” (8 minut dla Słońca, 6 z bliżej) to wynik porównania z zegarem aparatu czytającego — wszystkie odczyty są teraz.
- **Konsekwencje dla pliku [A]:** (1) najdłuższy łańcuch (A2, „czas własny”) **nie jest czasem**, tylko **miarą jednego odczytu** — tego, który wykonuje trajektoria; (2) **kierunek czasu nie jest własnością relacji ≺**, tylko asymetrią czytelności (rozproszone trudniej odczytać niż ostre); (3) aparaty różnią się zdolnością utrwalenia (mózg: 2 klocki tak, 200 nie; aparat fotograficzny: 200 przez dziesiątki lat).
- **Światło:** foton ma t=0 — od jego strony emisja i absorpcja są jednym. „8 minut” powstaje dopiero w aparacie z zegarem i wymaga synchronizacji (konwencja Reichenbacha, C4a.13). **Światło nie ma prędkości c; jest prędkość c w relacji do.**

**3+1 — UŻYWANE ŚWIADOMIE [H] (użytkownik, v3.4).** Triada **bez pamięci jest płaska**, nawet z dynamiką: czytając tylko bieżący stan, nie ma się dostępu do innych układów, jakie struktura może mieć, więc **ruchu nie da się zauważyć — jakby go nie było** (pomimo braku zera absolutnego). Nie powstaje dodatkowy punkt odniesienia; nie ma 3D. **Pamięć = dostęp do innych możliwych układów struktury**; dopiero ona daje czwarty punkt odniesienia.
- **Liczenie [A]: 3+1 liczy PUNKTY ODNIESIENIA, nie osie.** 3 punkty triady + 1 punkt odczytu = 4 punkty w położeniu ogólnym (czworościan) → rozpinają 3D. **„+1” nie jest czwartą osią, tylko punktem, bez którego trzeciej osi by nie było: „3” nie istnieje bez „+1”.** Brak podwójnego liczenia pamięci. Zgodne z tym, że estymator Myrheima–Meyera daje w 3+1 liczbę **4** (cztery punkty odniesienia).
- **Pułapka nr 5 — rozstrzygnięta:** **2D w łańcuchu Ø = płaszczyzna bez pamięci** (triada bez dostępu do innych układów, brak informacji). **Literaturowe d=2 = linia + czas** (jeden kierunek z pamięcią). To są **różne** rzeczy — zbieżność „d_s → 2 w skali Plancka = granica oznaczoności” (R3) opierała się na dwóch różnych dwójkach.

**Warunki muszą zachodzić razem [H] (użytkownik).** Triada daje płaszczyznę; dynamika (brak zera absolutnego) daje informację o ruchu; z niej trajektoria, czyli informacja zapisana w samej strukturze; a odczyt tej informacji ze struktury to **czas** — i on automatycznie tworzy **czwarty punkt odniesienia**. **Wszystko to musi grać razem, jednocześnie, żeby było coś, a nie nic.** Żaden z tych składników nie jest wcześniejszy od pozostałych.
**Zgodność z rachunkami [A]:** w C4a.12, C4a.19 i C4a.21 wyszło, że cięcie musi przyjść od trajektorii — lokalne otoczenie Boguñy–Krioukova wymaga wybrania geodezyjnej, suma Fokkera zamyka się tylko przy liniach świata. To jest ten czwarty punkt odniesienia widziany od strony liczenia.

**Zapis jest nierównomierny [H] (użytkownik).** W bazie wybranej przez oddziaływanie utrwala się **ostro i redundantnie**; poza nią rozprasza się tak, że odzyskanie jest o rzędy wielkości trudniejsze. Zmierzone w C4a:
- gdy jest co zapisać (zespół przesunięć, C4a.9): **pojedynczy link — dwa elementy — zna ponad połowę zapisu**, a wszystkie fragmenty razem 93–98%;
- gdy nie ma (ściśnięcie przy s=1, C4a.4): wszystkie fragmenty razem 25–55%, brak płaskiego odcinka;
- **decyduje położenie, nie rozmiar** (C4a.10): korelacja I(d:F) z liczbą elementów odcinka oddziaływania w przeszłości fragmentu **r = +0,84**; link 2-elementowy z 36/46 w przeszłości wie 0,90, fragment 7-elementowy z 2/46 wie 0,18.
- Mechanizm z literatury [L]: oddziaływanie z otoczeniem wybiera stany wskaźnikowe i tylko je rozgłasza w wielu kopiach (Zurek); reszta dekoheruje natychmiast i jest praktycznie nieodzyskiwalna.

**GRANICE Ø — RELACJA JEDNOSTRONNA [H] (użytkownik, zapis asystenta, v3.4).** Niech p ≥ 0 będzie parametrem, dla którego **p = 0 oznacza Ø** (czas własny na krok, okno odczytu, temperatura, 1 − v/c, skala względem Plancka).
1. **Niezmienniczość od środka:** dla każdego p > 0 mechanizmy są te same od środka; zmienia się wyłącznie **relacja do innych węzłów** (obiekt przy 99,999% c we własnym układzie nie widzi zmiany; Henry Molaison z oknem 0,0001 s nadal czyta siebie).
2. **Nieosiągalność:** żadna ciągła droga wewnątrz struktury nie kończy się w p = 0 (dla temperatury i skali Plancka — do przemyślenia, użytkownik). Zbliżanie się niczego nie zmienia od środka; **granica jest skokiem innego rodzaju**, nie końcem drogi. W granicy ginie **zdolność struktury do czytania samej siebie** (100% c: brak własnego zegara; okno 0: brak odczytu) — stan nieodróżnialny od osobliwości.
3. **Jednostronność:** przejście między strukturą a Ø zachodzi **wyłącznie jako zdarzenie**, zawsze w jednym kierunku — A → Ø albo Ø → A — **nigdy jako relacja dwustronna A ↔ Ø**.

| parametr | droga ciągła (p → 0) | skok A → Ø | skok Ø → A |
|---|---|---|---|
| 1 − v/c | rozpędzanie masy: nigdy c | anihilacja (masa → fotony) | kreacja par (fotony → masa) |
| okno odczytu | dopóki > 0, mechanizm ten sam | utrata odczytu | nowy odczyt, dekoherencja |
| przedział w strukturze | zagęszczanie: zawsze element między | wpadnięcie pod horyzont | promieniowanie Hawkinga |
| **stosunek tempa odczytu** (dylatacja grawitacyjna) | zbliżanie się do horyzontu **widziane z zewnątrz**: stosunek → 0, nigdy nie osiąga | przekroczenie horyzontu (od środka: pojedyncze zdarzenie w skończonym czasie własnym) | [?] (Hawking — patrz wiersz wyżej) |
| temperatura | chłodzenie: nigdy 0 | [?] do przemyślenia | [?] do przemyślenia |
| skala | poniżej Plancka nic nie odróżnia | [?] do przemyślenia | [?] do przemyślenia |
| węzeł → całość | otoczenia nie da się odseparować; całość statyczna **tylko jako całość** | — | **rozszerzanie: wszechświat cały czas tworzy nowe relacje przestrzenne** (od środka Ø → A zachodzi nieustannie) |

- **Wniosek (poprawiony, v3.4):** Ø jest **jedno** — nieodróżnialność oznacza, że absolutność jest wszędzie taka sama i **nie można jej dzielić na takie i owakie**. Różnice w tabeli dotyczą wyłącznie **tego, co wiemy o zdarzeniach od naszej strony** (otoczenia), nie Ø. Puste pola to luki w wiedzy, nie własność granicy.
- **POPRAWKA (asystent, v3.4):** pierwsza wersja dzieliła Ø na „punkty kontaktu” i „brzegi hierarchii” — **naruszenie pułapki nr 1** (Ø jest jedno; wszystko, co różni człony, należy do otoczenia). Wpisała też „brak skoku” dla całości, co przeczy rozszerzaniu (użytkownik).
- **DYLATACJA GRAWITACYJNA W JĘZYKU ODCZYTU [H] (użytkownik + asystent, v3.4).** Klasycznie, bez interpretacji: zegar głębiej w polu wskazuje mniej względem dalekiego; sygnały stamtąd przesunięte ku czerwieni; przy horyzoncie przesunięcie rośnie bez granic — daleki obserwator nigdy nie widzi przekroczenia, spadające ciało przekracza w skończonym czasie własnym. GPS: zegary satelitów zyskują ~45 μs/dobę (słabsze pole), tracą ~7 μs (ruch), netto ~38 μs.
  - **Dylatacja = stosunek tempa odczytu dwóch czytających**, nie „czas płynie wolniej”: na jeden krok dalekiego czytającego przypada coraz mniej odczytywalnych zapisów z obszaru bliżej horyzontu. W porządku: stosunek długości dwóch łańcuchów między kolejnymi wymianami sygnałów (ta sama wielkość co „opóźnienie” w regule v1).
  - **Przesunięcie ku czerwieni = rozproszenie zapisu:** te same zapisy docierają rozciągnięte na więcej kroków czytającego — mniej ostre. Rozróżnienie ostre/rozproszone wyznaczone **położeniem**, nie aparatem.
  - **Od środka nic się nie zmienia** (punkt 1 wyżej); **horyzont = granica, przy której stosunek → 0** — z zewnątrz zbliżanie się nie kończy się nigdy (punkt 2), od środka przekroczenie jest pojedynczym zdarzeniem w jednym kierunku (punkt 3).
  - **Wniosek:** dylatacja grawitacyjna to **ten sam wiersz co v → c**, widziany z innej strony — zgodnie z zasadą równoważności (pole i przyspieszenie lokalnie nieodróżnialne).
  - **Test do reguły wzrostu z narodzinami:** w obszarze ze stłumionymi narodzinami **stosunek tempa odczytu** (trajektoria stamtąd / trajektoria z zewnątrz) powinien **spadać**, a nie tylko opóźnienie rosnąć — dylatacja wyrastająca z reguły.
- **Związek z masą (hipoteza z v3.4):** masa = częstość samoodczytu trajektorii. Przy v → c mierzona z zewnątrz spada do 0 (dylatacja), od środka bez zmian; dopiero w granicy znika — foton bez masy i zegara. Henry przy oknie 0 i foton = ten sam stan: brak samoodczytu.

**Relacja z Ø nie jest zwykłą relacją [H].** Zwykła relacja jest dwustronna. Z Ø możliwa jest tylko jednostronna: $\varnothing\to A$ albo $A\to\varnothing$, każda osobno. Niesymetryczność kluczowa w kosmologii (asymetria barionowa — na razie tylko dopasowanie kształtu, bez rzędu wielkości η).

**O Ø nie da się nic powiedzieć** — liczyć wyłącznie w relacji do znanego otoczenia (laboratorium nie dopuszcza słonia; chwila zero z częściowym otoczeniem — dopuściła).

**Konwencja wymiaru w tym pliku [H]:** zapis „4D” oznacza **3D + dynamika + pamięć**. Literatura (Myrheim–Meyer, sprinkling d=…) liczy 1 czas + (d−1) przestrzeni. Patrz pułapka nr 5.

**Konsekwencja, której plik do v3.1 nie wyciągał:** program jest **porównawczy z definicji**, więc wymaga co najmniej dwóch otoczeń. Wszystkie liczby w §A pochodzą ze sprinklingu do diamentu w płaskim Minkowskim. 

## R1b. Trzy wymiary z definicji czasu — dowód strukturalny [H][L][T] (v3.4, 25.09; po audycie, poprawka 123)

### R1b-F. Zapis formalny [T][L] (poprawka 127; słowa niżej = glosa, [418])

**Oznaczenia.** Układ A: Ω_A ⊂ ℝ^{K_A} — zbiór stanów (wypukły, domknięty, dim < ∞); odczyt = efekt E: Ω_A → [0,1] afiniczny, wynik p = E(ω); G_A — domknięta grupa przekształceń odwracalnych Ω_A → Ω_A; ∂ₑΩ_A — stany czyste (ekstremalne). Układ złożony: p(x,y) = (E_x ⊗ E_y)·ω_AB — bez kolejności odczytów.

**Definicje.**
- **D0** (wymiar): d := dim Ω_A, gdy Ω_A ≅ Bᵈ = {r ∈ ℝᵈ : |r| ≤ 1}. Przestrzeń := Bᵈ (zbiór wszystkich odczytów); innej nie ma.
- **D1** (pojemność): N_A := max{n : ∃ ω₁…ωₙ, E₁…Eₙ, Σ Eᵢ = 1, Eᵢ(ωⱼ) = δᵢⱼ}.
- **D2** (zapis, przeszłość): 𝒫_X := {Y ≠ X : I(M_X : Y) > 0} — Y *inny* układ, nie „wcześniejszy” (brak ≺ w definicji).
- **D3** (relacja): T ∈ G_AB jest relacją ⇔ T ∉ G_A ⊗ G_B.

**Przesłanki** (glosa ramy w tabeli niżej).
- **P0:** Ĥ|Ψ⟩ = 0 ⇒ e^{−iĤs}|Ψ⟩ = |Ψ⟩ ∀s ∈ ℝ; brak aktora zewnętrznego ⇒ G_A = ⟨{e^{sX}}_{s∈ℝ}⟩ ⇒ **G_A spójna**.
- **P1:** N_A = 2.
- **P2:** ∀ ω, φ ∈ ∂ₑΩ_A ∃ G ∈ G_A : Gω = φ.
- **P3:** ∂Ω_A nie zawiera odcinków (ścisła wypukłość).
- **P5:** span{ω_A ⊗ ω_B} = ℝ^{K_A} ⊗ ℝ^{K_B}, tj. K_AB = K_A·K_B.
- **P6:** G_AB ⊄ G_A ⊗ G_B.

**Lemat 1** (P0, P2, P3; W² := ∫_{G_A} HᵀH dH): Ω_A ≅ Bᵈ, ∂ₑΩ_A = Sᵈ⁻¹, K_A = d + 1, G_A ⊆ SO(d) przechodnia na Sᵈ⁻¹; μ := ∫ Gω dG = 0 jest jedynym punktem stałym G_A.

**Twierdzenie** (Masanes, Müller, Pérez-García, Augusiak 2014, Tw. 1–2; d = 1: P0):
P0 ∧ P1 ∧ P2 ∧ P3 ∧ P5 ∧ P6 ⇒ **d = 3**, G_A = SO(3), G_AB = Ad SU(4) (z dokładnością do równoważnej reprezentacji częściowo transponowanej).
- d = 1: G_A = O(1) = {±1}, niespójna ⊥ P0.
- d = 2 ∨ d ≥ 4: G_AB ⊆ G_A ⊗ G_B ⊥ P6.
- **Rola przesłanek [H] (poprawka 137):** P0, P2, P3 dają kulę dowolnego wymiaru (P0 wyklucza d = 1); **d = 3 wybierają P1, P5 i P6**; pamięć (D2, Wniosek 2) decyduje o **dostępie** do kuli. P5 dźwiga wykluczenie mechaniki kwantowej rzeczywistej (d = 2) i kwaternionowej (d = 5): obie **mają** relację (splątanie), odpadają wyłącznie na tomografii lokalnej. Eksperymenty Renou i in., Nature 600, 625 (2021); Chen i in., PRL 128, 040403 (2022); Li i in., PRL 128, 040402 (2022) wykluczające teorię rzeczywistą są **potwierdzeniem, nie podporą** dowodu. Numeracja P0–P6 = kolejność czytania.

**Wniosek 1** (4 punkty): stan bez szumu r ∈ B³ wyznaczony przez trzy odczyty komplementarne: rᵢ = 2E_{eᵢ}(ω) − 1, i = 1, 2, 3; E_{eᵢ}(ω_{eⱼ}) = ½ dla i ≠ j. Dwa odczyty: rząd 2 < 3 (stan nieustalony); czwarty: liniowo zależny (K_A = 4 = 1 + 3). {e₁, e₂, e₃} = triada, ω = czwarty punkt.

**Wniosek 2** (pamięć, kontrola bez niej): czytający bez zapisu ma jeden odczyt E_y na bieżącym stanie; dostępne Ω_A/∼, gdzie ω ∼ φ ⇔ E_y(ω) = E_y(φ): Ω_A/∼ ≅ B¹, G(B¹) = O(1) niespójna ⇒ brak ciągłego przekształcenia („ruchu nie da się zauważyć” [400]). Z zapisem M odczytów wzdłuż e₁, e₂, e₃ (I(M : ωᵢ) > 0, D2): dostępne Ω_A = B³.

**Wniosek 3** (Ø): ∂B³ = S², dim 2 (sfera sama ≡ Ø; całość bez relacji, t = 0); μ = 0 — brak informacji o kierunku; ∀ ω ∈ int B³ ∃ czysty Ψ_AB : Tr_B Ψ_AB = ω (puryfikacja; Chiribella–D’Ariano–Perinotti 2011) — wnętrze B³ tylko z relacji.

**Test wierności przekładu (poprawka 128) [O].** Kryterium jak w łańcuchu Ø: wykluczenie, nie ocena. Przekład P jest wierny ⇔ ¬P wyklucza się ze zdaniem ramy. Wtedy rama ⇒ P i zastrzeżenie „o ile przekład jest wierny” znika.

| przesłanka | ¬P | wyklucza się z |
|---|---|---|
| P0: G_A spójna | ∃ przekształcenie nieosiągalne w sposób ciągły = skok bez niczego pomiędzy, niegenerowany relacją wewnątrz | „nie ma zewnętrznych aktorów” [354]; „całość nie ma otoczenia, dla całości t=0” [270] |
| P1: N_A = 2 | N_A = 1: brak dwóch rozróżnialnych stanów = brak różnicy; N_A ≥ 3: zawiera różnicę dwustanową, więc nie jest najmniejsza | N_A = 1: „wzbudzenie = różnica = informacja”, brak różnicy ≡ Ø [258, 242]; N_A ≥ 3: „foton = minimalna różnica” [258] |
| P2a: G_A przechodnia na ∂ₑΩ_A | ∃ ω, φ czyste, nieprzekształcalne: stan czysty różni się od innego sam z siebie, bez relacji | „nic nie jest cechą” [36, 94] |
| P2b: p(x,y) niezależne od kolejności odczytów | wynik zależy od „przed/po” = stan niesie etykietę kolejności | klocki: stan nie niesie etykiety przed/po [394] |
| P3: ∂Ω_A bez odcinków | na sumie wszystkich odczytów wyróżnione są punkty brzegu (ekstremalne vs nieekstremalne) | „dla całej sfery t=0”, sfera ≡ Ø: na całości nic nie wyróżnione (sesja 25.09, poprawka 120) |
| P5: tomografia lokalna | ∃ różnica stanów pary nieodczytywalna przez odczyty części i korelacje = **różnica pary niesiona przez nic poza nią samą** (użytkownik, poprawka 137) | **„cecha”** [36, 94]; także „wzbudzenia i relacje są lokalne” [270] |
| P6: G_AB ⊄ G_A ⊗ G_B | nośniki nigdy nie wchodzą w relację | „dwa zdania prawdziwe: milczenie i relacja” [10]; foton t=0 = warunek, żeby przestrzeń była relacją [80] |
| tło: liniowe mieszanie | prawdopodobieństwo zależy od tego, czy etykietę przygotowania pominięto przed czy po odczycie (tak liniowość wyprowadzają Masanes i in., §III) | [394] (brak przed/po) |
| tło: dim Ω_A < ∞ | ustalenie stanu wymaga nieskończenie wielu niezależnych odczytów = stanu nie da się ustalić odczytem | „o superpozycji nic nie można powiedzieć” [110]: nieodczytywalne ≡ Ø, nie nośnik informacji |

**Wynik:** każda przesłanka i oba założenia tła są **wymuszone** przez zdanie ramy (¬P ⊥ rama). Łańcuch: **rama ⇒ P0 ∧ … ∧ P6 ⇒ d = 3.** D0 jest definicją, nie przekładem: nie może być niewierna, najwyżej niespójna, a spójności nic nie przeczy. Status wynikania rama ⇒ P: [O] asystenta, sprawdzalny wierszem tabeli, bez oceny.

### Glosa (słowa, źródła w rozmowie)

**Teza:** trzy wymiary przestrzenne (= 4 punkty odniesienia) są jedynym przypadkiem, w którym najmniejsze nośniki informacji mogą w ogóle wejść ze sobą w relację. Dowód nie przegląda przypadków, tylko nie dopuszcza innych [148]. Nie używa przestrzeni tła, zewnętrznego czasu ani kierunku.

**Skąd:** rama użytkownika (R1a, synteza czasu) + formalizm uogólnionych teorii probabilistycznych, wzięty bez interpretacji: Müller–Masanes, New J. Phys. 15, 053040 (2013), arXiv:1206.0630; **Masanes, Müller, Pérez-García, Augusiak, J. Math. Phys. 55, 122203 (2014), arXiv:1111.4060** (twierdzenie o d = 3; bez przestrzeni fizycznej). Przekład założenie po założeniu i historia dochodzenia: C5, poprawki 114–121. Numery [n] = rozmowa źródłowa; „sesja 25.09” = rozmowa w Claude Code z 25.09.

**Definicja D0 (użytkownik, sesja 25.09):** „Kula stanów to zbiór wszystkich możliwych kierunków / odczytów / pozycji — wtedy to faktycznie jest 3D.” **Wymiar przestrzeni := wymiar kuli wszystkich możliwych odczytów.** Bez D0 twierdzenie mówi o kubitach, nie o przestrzeni. [L] Müller–Masanes (2013, §V i Przykład 39) pokazują, że struktura euklidesowa przestrzeni może być odziedziczona z prawdopodobieństw odczytów, a nie odwrotnie.

**Przesłanki twierdzenia (lewa kolumna: zdanie ramy; [H] = słowa użytkownika, [A] = mój przekład):**

| # | rama | formalizm [L] |
|---|---|---|
| P0 | [H] Całość nie ma otoczenia, „dla całości t=0; wzbudzenia i relacje są lokalne” [270]; czytanie „zawsze teraz” [334, 394]; „niezmienniczość względem reparametryzacji: Ĥ\|Ψ⟩=0” (sesja CC 72) | ciągła jednoparametrowa grupa e^(−iĤt), względem której całość stoi; części zmieniają się tylko względem czytającego (Page–Wootters). Parametr t = dowolna etykieta, nie czas (poprawka 118) |
| P1 | [H] „Foton — minimalne wzbudzenie. Minimalna różnica. Minimalna informacja.” [258] | **układ binarny**: dokładnie dwa stany doskonale rozróżnialne ([A]: minimalna różnica = 1 bit) |
| P2 | [H] stan nie niesie etykiety przed/po (klocki) [394]; [A] żaden ostry odczyt nie jest wyróżniony — wyróżniony byłby „cechą” [36, 94] | **ciągła odwracalność**: każde dwa stany czyste łączy ciągłe przekształcenie odwracalne; wyniki odczytów części **nie zależą od kolejności w czasie** (w samej definicji układu złożonego) |
| P3 | [H] „Suma wszystkich kierunków 3 takich węzłów — objętość sfery” [150]; „lokalny odczyt może mieć dowolny kształt; suma wszystkich odczytów wokół jednego punktu odniesienia daje sferę”; „sama powierzchnia sfery jest 2D ≡ Ø; dla całej sfery t=0” (sesja 25.09; poprawki 120–121) | **okrągłość**: zbiór stanów (= suma odczytów) ściśle wypukły; z ciągłą odwracalnością i średnią Haara W² = ∫HᵀH dH → elipsoida → **kula** |
| P5 | [H] „Wzbudzenia i relacje są lokalne” [270] — nie ma odczytu całości z zewnątrz | **tomografia lokalna**: stan pary wyznaczony przez odczyty części i ich korelacje |
| P6 | [H] „Istnieją tylko dwa zdania prawdziwe: milczenie i relacja” [10] | **oddziaływanie**: istnieje przekształcenie pary nierozkładalne na lokalne (⇔ splątanie) |

**Tło:** stan = prawdopodobieństwa odczytów, mieszanie przygotowań liniowe; prawdopodobieństwo nigdy nie dotyczy „samej superpozycji”, tylko relacji otoczenia [110, 244] (poprawka 114).

**Krok 1 — zbiór odczytów jest kulą [T][L].** Z P1–P3: stany czyste (ostre odczyty) tworzą sferę, której żaden punkt nie jest wyróżniony; wszystkie inne stany są mieszaninami. W środku stan μ, jedyny niezmienniczy względem wszystkich przekształceń, bez informacji o kierunku. Wymiar kuli d = liczba **wzajemnie komplementarnych** odczytów potrzebnych do ustalenia stanu (przy stanie ostrym wzdłuż jednego kierunku odczyt wzdłuż prostopadłego daje 1/2, czyli nic).

**Krok 2 — relacja istnieje tylko przy d = 3 [T][L].** Z P2, P5, P6 (Masanes i in. 2014, Tw. 1–2):
- **d = 1** (bit klasyczny, odcinek): przekształcenia odwracalne to {1, −1}, grupa niespójna — sprzeczne z ciągłą odwracalnością. Zgodne z [H] „1D nie istnieje” (sesja CC 82). (spójność grupy: poprawka 125).
- **d = 2 i d ≥ 4:** każde przekształcenie odwracalne pary rozkłada się na lokalne — **relacji między nośnikami nie ma**. Dla 2D zgodne z [H] „relacja pomiędzy dwoma węzłami jest = 0” [76]. Dla d ≥ 4 zgodne z [H] [511] („nic nie wymaga piątego punktu”) i mocniej: nie tylko „skróty zamiast osi” (symulacja R7), lecz brak relacji w ogóle.
- **d = 3:** relacja istnieje i jest dokładnie relacją dwóch kubitów (splątanie, ewolucja unitarna).
- Powód grupowy (Müller–Masanes 2013): **dla d ≥ 3** obroty zostawiające jeden kierunek w miejscu, SO(d−1), są przemienne tylko przy d = 3; d = 1 i d = 2 wypadają z innych powodów (wyżej).

**Krok 3 — przekład na punkty odniesienia [O].** Stan w kuli 3D ustalają odczyty wzdłuż **trzech** komplementarnych kierunków (dwa nie wystarczają, czwarty nic nie dokłada) = **triada, trzy węzły relacji**. Ustalany stan = **czwarty punkt**: [H] „1 punkt odniesienia to informacja o dynamicznej strukturze, w superpozycji, dopóki pole nie jest wzbudzone” (sesja CC 82). **3 wymiary = 4 punkty, nie osie** [400]. Trzy odczyty nie leżą w jednej płaszczyźnie, bo płaszczyzna ≡ Ø (współliniowość istnieje tylko w 2D; poprawka 117).

**Krok 4 — czas, pamięć i 3D [O] (rozstrzygnięte strukturą, poprawka 124).** [H] „Samo 3 jest płaskie. Nawet jak jest dynamika — bez pamięci ruchu nie da się zauważyć… nie powstaje dodatkowy punkt odniesienia. Nie ma 3D” [400]; pamięć = dostęp do innych układów struktury niż bieżący.
- **Pamięć w formalizmie = stan nośnika jako zapis informacji o innym układzie.** Bob czyta teraz stan niosący kierunek Alicji, bez wspólnego układu współrzędnych — dostęp do układu innego niż bieżący, czyli definicja z [400] dosłownie.
- **„Wiele odczytów zebranych razem” to nie osobne wejście:** odczyt jest zawsze teraz, więc wcześniejsze odczyty istnieją tylko jako zapis — to ten sam mechanizm zastosowany do własnych odczytów czytającego. Pamięć wchodzi do dowodu raz.
- **Kontrola bez pamięci, w samym formalizmie:** czytający bez zapisu ma tylko bieżący odczyt wzdłuż jednej osi; z kuli widzi jej rzut na tę oś = odcinek = **bit klasyczny (d = 1)**, którego przekształcenia odwracalne to tylko skok {1, −1}, bez ciągłości → **ruchu nie da się zauważyć**, dokładnie jak w [400]. Dopiero zapisy odczytów wzdłuż trzech komplementarnych osi dają kulę 3D. Ta sama kontrola, którą w R5/R6 robiliśmy symulacją (bez pamięci 2, z pamięcią 3), tu wynika strukturalnie.
- Ciągłość (P0) wyklucza d = 1; brak kierunku (P2) siedzi w definicji układu złożonego. Łącznik (nie przesłanka twierdzenia): [H] „3D jest tylko lokalne jako wynik świata relacji wewnątrz” (sesja 25.09) ↔ [L] puryfikacja: stan mieszany (wnętrze kuli) jest częścią stanu czystego większego układu (Chiribella, D’Ariano, Perinotti, Phys. Rev. A 84, 012311, 2011, arXiv:1011.6451). Stąd: **definicji czasu nie wolno oddzielać od wyprowadzenia 3D** [511; CLAUDE.md].

**Wniosek (stanowczo):** przy D0 i P0–P6 **3D jest jedyną możliwością**; 2D i każde d ≥ 4 są wykluczone strukturalnie, brakiem relacji, nie przez przykłady; 1D — ciągłością (spójność grupy: poprawka 125) i niezależnie ramą. Symulacje R5–R7 (triada 2, triada + pamięć 3, więcej połączeń = brak rozmaitości) są z tym zgodne, ale nie są częścią dowodu.

~~**Otwarte (jedno, formalne) [?]:** aksjomat ciągłej odwracalności u Masanesa i in. jest równoważny **spójności całej grupy** przekształceń odwracalnych (każde przekształcenie osiągalne w sposób ciągły). Przekład P0 (poprawka 118) daje ciągłość jednej rodziny (ewolucji względem czytającego), P2 daje brak wyróżnionego odczytu. Czy rama daje spójność całej grupy — czyli wyklucza przekształcenie „skokiem”, bez niczego pomiędzy — nie jest jeszcze pokazane. Od tego zależy formalnie tylko wykluczenie d = 1.~~

**ZAMKNIĘTE strukturą (poprawka 125) [O]:** [H] „W rygorze relacyjnym nie ma zewnętrznych aktorów. Źródło nie może być obcym ciałem wetkniętym w strukturę” [354]. Każde przekształcenie odwracalne jest więc relacją wewnątrz, czyli pochodzi z dynamiki wewnętrznej; ta jest ciągłą jednoparametrową grupą (P0). Grupa złożona z ciągłych jednoparametrowych podgrup jest spójna. Przekształcenie „skokiem”, nieosiągalne w sposób ciągły, wymagałoby aktora spoza całości — a całość nie ma otoczenia. Spójność + brak wyróżnionego odczytu (P2) = ciągła odwracalność w pełnym sensie Masanesa i in. **Wykluczenie d = 1 stoi więc na twierdzeniu, nie tylko na ramie.**

**Granice (czego dowód nie mówi):**
- Dotyczy **stanów i odczytów** (kula, pary nośników); most do porządku przyczynowego i światła: **R1c** (stożek stanów = stożek przyczynowy, czyste = zerowe). Związek z C5 (R6, krzywizna) nie jest tu dowodzony.
- ~~Przesłanki to przekłady; twierdzenie obowiązuje o tyle, o ile przekład jest wierny.~~ **Zastąpione testem wierności w R1b-F (poprawka 128):** każda przesłanka jest wymuszona przez zdanie ramy (¬P wyklucza się z ramą). Zostaje jedno: przesłankami dowodu są zdania ramy — dowód pokazuje, co z nich wynika, nie uzasadnia ich z zewnątrz (zgodnie z zasadą metody).
- Formalizm zakłada skończony wymiar zbioru stanów i liniowe mieszanie przygotowań.
- Masanes i in. rozważają pary nośników; uogólnienie na wiele nośników przy d = 3 jest w ich ref. 21; dla d ≠ 3 wystarcza para.

**Zestawienie z propozycją zewnętrzną (25.09, tekst i schemat „Formalny most: odczyt → pamięć → czas relacyjny → 3D”, nie autorstwa użytkownika; poprawka 126) — przez filtr:**
- **Wzięte [A]:** formalny zapis przeszłości: **przeszłość dla aparatu X = {Y : I(M_X : Y) > 0}** — zbiór konfiguracji, o których zapis aparatu niesie informację (informacja wzajemna > 0). Operacyjny odpowiednik [394] i R1a („ile przeszłości istnieje, zależy od zdolności zapisu”: mózg vs aparat fotograficzny = różna pojemność kanału zapisu). **Warunek:** Y to *inny* układ, nie „wcześniejszy” — w oryginale „S_wcześniejsze / R_earlier” przemyca kierunek (poprawka 106). Po tej poprawce zgodne z krokiem 4: pamięć = zapis o innym układzie.
- **Już jest w R1b:** „nowy wynik” wg propozycji (założenia relacyjne ⇒ pamięć ⇒ przestrzeń stanów ⇒ 3D bez wkładania 3D; bez pamięci formalnie nie-3D) = R1b + krok 4 (poprawka 124). Proponowane cztery modele (bez dynamiki / bez pamięci / z pamięcią / więcej połączeń) = R5–R7, bez geometrii na wejściu, teraz zamknięte strukturalnie. Grupa SO(3) nie jest założeniem, tylko wynikiem (Masanes i in., Tw. 2). Pytanie, czy rama wymusza formalizm (skończony wymiar, liniowe mieszanie), jest w „Granicach”.
- **Odrzucone (sprzeczne z ramą):** ciąg odczyt → pamięć → czas → 3D (rama: wszystko naraz; pamięć i czas to jeden czwarty punkt); „stan wcześniejszy” (kierunek); „d_state = 3, ale d_physical ≠ 3” i „twierdzenie identyfikacji” (zakłada przestrzeń tła; obowiązuje D0); czas jako „struktura *uporządkowanych* korelacji” i „czas pojawia się, gdy relacje mają własności wymagane od czasu” (porządek + kryterium z interpretacji); „r₀ = 2” jako twierdzenie ramy (formalnie bez pamięci rząd 1; 1D i 2D to ta sama klasa bez relacji); rama „mini-teorii do obalenia” (zasada metody: porządkowanie, nie nowa teoria; obalić można przekład).

## R1c. Most R1b ↔ światło i porządek przyczynowy [T][L][O] (v3.4, 25.09; poprawka 129)

**Cel:** domknąć granicę R1b („dotyczy odczytów, nie porządku przyczynowego”) na poziomie światła, zgodnie z [488]: „musi się rozstrzygnąć na poziomie światła”.

### R1c-F. Zapis formalny

**Tożsamość [T]** (algebra 2×2; sprawdzona numerycznie na losowym Z ∈ SL(2,ℂ)): macierz hermitowska X = x⁰·𝟙 + x·σ ↔ wektor x^μ = (x⁰, x) ∈ ℝ^{1,3}, **det X = (x⁰)² − |x|²** (norma Minkowskiego).
- Stan nośnika z R1b: ρ = ½(𝟙 + r·σ), r ∈ B³ ⇒ x = ½(1, r), **4 det ρ = 1 − |r|²**.
- **ρ ≥ 0 ⇔ x⁰ ≥ |x|:** zbiór (nieznormowanych) stanów = **stożek przyczynowy przyszłości** w ℝ^{1,3}.
- **Stany czyste (|r| = 1, ∂B³) ⇔ det ρ = 0 ⇔ wektory zerowe** (świetlne). Wnętrze B³ ⇔ wektory czasopodobne. μ (r = 0) ⇔ oś czasu czytającego.
- **tr ρ = 1** = przekrój stożka hiperpłaszczyzną x⁰ = ½ = **kula B³**.
- ρ ↦ ZρZ†, Z ∈ SL(2,ℂ): zachowuje det i dodatniość ⇒ element **SO⁺(3,1)**; Z ∈ SU(2) = obroty (zachowują przekrój), pozostałe = pchnięcia (zmieniają przekrój; po ponownym znormowaniu działają na B³ rzutowo).
- ∂B³ = S² = zbiór kierunków zerowych przez punkt = **sfera niebieska**; SO⁺(3,1) ≅ PSL(2,ℂ) działa na niej jak przekształcenia Möbiusa (konforemnie).

**[L]** Penrose–Rindler, *Spinors and Space-Time* I (1984): sfera niebieska = kierunki zerowe = sfera Riemanna; B. Oblak, „From the Lorentz group to the celestial sphere”, arXiv:1508.00920. **Höhn, Müller, „An operational approach to spacetime symmetries: Lorentz transformations from quantum communication”, New J. Phys. 18, 063026 (2016), arXiv:1412.8462** (przeczytane: wstęp, Tw. 3.6, Tw. 4.12, §4.5): bez zakładania czasoprzestrzeni, przyczynowości, sygnatury ani wymiaru — dwóch obserwatorów bez wspólnej ramy uzgadnia opis układów kwantowych; przy „kubicie-korzeniu” grupa przekładu opisów to **SO(3)** (wyniki odczytów jako etykiety), a gdy wyniki mają wielkość — **O⁺(3,1) × skala λ > 0**. Skala λ = umowa jednostek, jedyna niezależna od grupy. Malament (J. Math. Phys. 18, 1399, 1977), Hawking–King–McCarthy (1976): porządek przyczynowy wyznacza geometrię z dokładnością do czynnika konforemnego.

### Odczyt w ramie [O]

1. **Kula odczytów z R1b = przekrój stożka świetlnego w ramie czytającego.** 3D (B³) i „+1” (normowanie tr ρ = własna rama czytającego) — **3+1 jako punkty i przekrój, nie cztery osie** [400].
2. **Ostre odczyty = światło.** ∂B³ (suma wszystkich odczytów wokół punktu, P3) = sfera niebieska = wszystkie promienie docierające do punktu. **det ρ = 0 ⇔ interwał zero ⇔ foton, t = 0** [80]. „Sama powierzchnia sfery jest 2D ≡ Ø” (poprawka 120) = zbiór kierunków zerowych, na którym nic nie ma czasu własnego.
3. **Wnętrze = relacja z czasem własnym.** Punkty wnętrza B³ są czasopodobne (det ρ > 0) i istnieją tylko z relacji (puryfikacja, R1b krok 4). **4 det ρ = 1 − |r|² = entropia liniowa** — „czas własny²” stanu = stopień jego relacji z otoczeniem. [?] Związek z masą (masa = tempo samoodczytu, §F1; dla czterowektora pędu det = m²) — **niezbadany, tylko zbieżność formy. **Dopisek 163 (R1f-3):** dla **macierzy pędu** P = E·𝟙 + p·σ związek jest [T]: m² = det P; dla ρ zostaje formą.**
4. **c.** „c ≤” ⇔ **ρ ≥ 0** (prawdopodobieństwa nieujemne): nic nie leży poza stożkiem, tak jak żaden stan nie ma |r| > tr ρ. c = 1 to granica czytelności nośnika minimalnego (ostry odczyt), nie prędkość. **„c nieskończone, gdy nikt nie czyta”:** sam stożek (bez przekroju) ma tylko promienie, nie ma prędkości; prędkość pojawia się dopiero po wyborze przekroju = ramy czytającego („C w relacji do” [394]).
5. **Rama i pchnięcia.** Zmiana czytającego = SL(2,ℂ) na nośniku = grupa Lorentza (Höhn–Müller, bez tła). To te same pchnięcia, których **koszt wskazania daje logarytmy w §F2** (ln n) — grupa przekładu między czytającymi jest grupą, po której całkujemy.
6. **Dwa pierwotne (A1).** Porządek → geometria z dokładnością do czynnika konforemnego (Malament); u Höhna–Müllera jedyny element poza grupą to skala λ. **Porządek + liczność = Lorentz + skala** [O].
7. **Kierunek.** Dodatnie macierze wyznaczają jedną połowę stożka; −ρ nie jest stanem. „Przyszłość vs przeszłość” = umowa znaku dodatniości = **jeden bit** (por. Gallai, poprawka 106): pseudokierunek, nie cecha.
8. **Dlaczego to działa tylko przy 3D.** Kula Bᵈ zawsze jest przekrojem stożka w ℝ^{1,d}, ale relacja między nośnikami istnieje tylko przy d = 3 (R1b). **Stąd ℝ^{1,3}: jedyny stożek, w którym nośniki światła mogą się wiązać.**

### Stan i granice

- **[T]:** tożsamości algebraiczne (det = norma Minkowskiego; dodatniość = stożek; SL(2,ℂ) → SO⁺(3,1); czyste = zerowe). **[L]:** Höhn–Müller — grupa Lorentza z komunikacji, bez tła.
- ~~**[O][?] do sprawdzenia:** czy stożek stanów jednego nośnika to „ten sam obiekt” co stożek przyczynowy punktu (a nie tylko ta sama struktura).~~ **ŹLE POSTAWIONE (użytkownik [H], poprawki 130, 132).** „Obiekt” w pytaniu użyty jako nośnik zawartości poza strukturą; w ramie obiekt = (stabilna) struktura relacji, która jako całość jest w relacji z inną (słownik). Rozróżnienie „ten sam obiekt / ta sama struktura” zakładało zawartość poza strukturą; logika relacyjna = struktura bez zawartości, zawartość bez struktury = Ro, niedostępna [18]. Struktury bez żadnej różnicy relacji są nierozróżnialne: **stożek stanów nośnika ≡ stożek przyczynowy punktu** (≡ jak w łańcuchu Ø), a zgodność struktur jest [T]. Nic więcej do sprawdzenia. ~~Zostaje otwarte: translacje~~ **Translacje rozstrzygnięte strukturą (poprawka 131) [O][L]:** „translacja” = przesunięcie położenia, zakłada pojemnik; po D0 położenie to relacja, więc translacja = zmiana punktu odniesienia na innego czytającego; relacja między czytającymi = porządek między ich elementami (linki = światło) = jeden z dwóch pierwotnych (A1). Stożek w każdym punkcie: R1c; relacje między punktami: porządek; sklejenie: **Malament (1977)** — porządek między wszystkimi punktami wyznacza geometrię (z translacjami) z dokładnością do czynnika konforemnego, który uzupełnia liczność. Höhn–Müller nie mają translacji, bo badają dwa laboratoria bez porządku między nimi. **R1c nie ma punktów otwartych**; zostaje tylko [?] det ρ ↔ masa (forma).
- Punkt 3 (det ρ ↔ masa) — tylko forma, nie wynik.

## R1d. Elektron, pole elektronowe i relacja z polem EM; kwark — zapis relacyjny [L][O] (v3.4, 25.09; poprawka 133)

**Skąd:** pogawędka 25.09 (użytkownik: „brakuje pogawędki o samym elektronie, polu elektronowym i tej dziwnej relacji z polem EM”; „zyg-zak… mógłby mieć związek z przeciwnymi funkcjami energii do odległości dla kwarków i elektronów”). Lista pojęć [94] i kolejność przed masą (A3): … → pole → próżnia → energia → ładunek, spin → elektron, kwark, gluon → masa.

### R1d-F. Zapis formalny [L]

- **Nośnik i światło (z R1c):** ξ ∈ ℂ² (spinor, spin ½) = nośnik minimalny z R1b; kierunek zerowy = ξξ† (wektor, spin 1). Obrót o 2π: ξ ↦ −ξ, ξξ† ↦ ξξ†.
- **Faza w punkcie ≡ Ø:** ψ(x) ↦ e^{iθ(x)}ψ(x) nie zmienia żadnego odczytu. Odczytywalne tylko **porównania**: ψ̄(x)·U(x,y)·ψ(y), U(x,y) = P exp(i e ∫ₓʸ A). Pole EM = koneksja A = **relacja faz między punktami**; natężenie F = obieg fazy po małej pętli (holonomia). Ładunek e = siła sprzężenia fazy z relacją; α = e²/4π.
- **Relacja vs relacja relacji:** F = dA (abelowa: relacja nie niesie ładunku, foton neutralny) vs F = dA − i g [A, A] (nieabelowa, kolor: relacja niesie ładunek, gluony wiążą się ze sobą).
- **Zygzak (Penrose, *The Road to Reality*, §25.2):** ψ = (ψ_L, ψ_R), każde bezmasowe (t = 0, porusza się z c); masa sprzęga je: −m(ψ̄_L ψ_R + ψ̄_R ψ_L); przechodzenie L ↔ R z częstością ~ m. Wektor czasopodobny = suma dwóch zerowych (R1c).
- **Odległość i energia bez pojemnika (poprawka 134):**
  - **odległość r := ½·n_ob** — n_ob = liczba tyknięć (elementów) własnej trajektorii czytającego między wysłaniem linku a odczytem jego powrotu (obieg; definicja metra 1983, „tylko prędkość w dwie strony” [266]); w jednostkach ℓ.
  - **energia E := ν** — częstość odczytu: liczba zmian odczytu nośnika na jedno tyknięcie czytającego (przelicznik ħ, A2). We własnej ramie nośnika ν = masa = tempo samoodczytu (§F1); u innego czytającego — **w miejscu czytającego** — większa, E = γ·m (stosunek temp; *poprawka 163: to nie jest dylatacja — dylatacją jest faza wzdłuż linii świata nośnika na tyknięcie czytającego, m·√(1−v²); R1f-3*). Noether: to, co stałe przy przesunięciu wzdłuż porządku (A3).
  - **E·r = liczba odczytów na jeden obieg** — bezwymiarowe. Skala w biegnących sprzężeniach: μ ~ 1/n_ob, więc **ln(μ/μ₀) = ln(n₀/n)** = logarytm stosunku liczebności (A2: ln(N_Λ/N)).
- **Biegnące sprzężenia:** 1/α_i(n) = 1/α_i(n₀) + (b_i/2π)·ln(n₀/n); wkład pola o spinie s do b ∝ (−1)^{2s}[(2s)² − ⅓] (A2): −⅓ „orbitalny” (ekranuje), (2s)² „spinowy” (antyekranuje, działa tylko gdy relacja niesie ładunek) — Nielsen, Am. J. Phys. 49, 1171 (1981).
  - QED: 1/α(n) = 1/α(n₀) − (2/3π)·Σ N_c Q²·ln(n₀/n) (A2: nachylenie ΣN_cQ² = 8) → sprzężenie **rośnie przy krótkim obiegu**; E·r ≈ α (stałe z dokładnością do logarytmu) — **α to sama relacja „odczyty na obieg”** (A2: α = promień Bohra / zredukowana długość Comptona = stosunek dwóch obiegów).
  - QCD: b₀ = 11 − ⅔ n_f > 0 → sprzężenie **maleje przy krótkim obiegu** (swoboda asymptotyczna), rośnie przy długim (uwięzienie: E·r rośnie jak n_ob², przy napięciu struny σ w jednostkach ℓ⁻²).
- **Transmutacja:** n_Λ = n·exp(+2π / (b₀ α_s(n))) — liczba tyknięć obiegu, przy której logarytm QCD sięga jedności (Λ_QCD ~ 1/n_Λ) — tu logarytm QCD sięga jedności → większość masy protonu. Dla QED analogiczna skala poza zasięgiem → masa elektronu nie z tego mechanizmu.

### Odczyt w ramie [O]

1. **Pole elektronowe bez wzbudzenia ≡ Ø**, jak pole EM [242, 258]. Elektron = wzbudzenie = odczyt, nie „cząstka z polem wokół”.
2. **„Dziwna relacja” z polem EM:** pole EM nie jest drugim bytem obok elektronu, tylko **relacją między fazami pola elektronowego w różnych punktach** (faza w punkcie ≡ Ø). Foton = minimalne wzbudzenie tej relacji. Zgodne z „Dalej otwarte”: pole jako faza na zamkniętych drogach (Giles, Sverdlov–Bombelli, Pellegrin).
3. **Ładunek nie jest cechą:** siła, z jaką faza jest związana relacją.
4. **Elektron = relacja dwóch struktur świetlnych (L, R, każda t = 0); masa = tempo ich wzajemnego przechodzenia** = „tempo samoodczytu” (§F1). Hoyle–Narlikar w A3: „ten sam zygzak”.
5. **Przeciwne funkcje sprzężenia od obiegu (dawniej „energii od odległości”)** *(uwaga 158: „relacja relacji” niżej = węższy odczyt asystenta; u użytkownika [78] przestrzeń, [94] masa, [104] świat R ⊗ R)*: znak z (−1)^{2s} = **nośnik (spinor, zygzak) vs jego złożenie (wektor, światło)** + to, czy relacja niesie ładunek. W języku [94]: **elektron — relacja (abelowa); kwark — relacja relacji (nieabelowa, kolor wiąże się sam ze sobą)**. Tempo zygzaka (masa) nie ustala znaku, tylko liczbę tyknięć obiegu, od której nośnik wchodzi do rachunku.
6. **Zespół funkcji logarytmicznych dla masy [94] = zespół biegnących sprzężeń**, każde z współczynnikiem wyznaczonym przez spin i przez to, czy relacja wiąże się sama ze sobą (liczby z A2). Dwa typy logarytmu (relacja / relacja relacji) — stąd „jedna funkcja nie wystarczy, kwarki i elektrony na to nie pozwalają”.

### Trzy punkty otwarte — rozpisane (poprawka 135)

**1. Co ustala częstość zygzaka elektronu.** [L] L i R nie przechodzą w siebie wprost; łączy je relacja z polem Higgsa: m = y·v/√2, v — wartość w próżni, wszędzie ta sama. [O] Wszędzie to samo = nierozróżnialne ≡ Ø; tło działa na nośnik (umożliwia zygzak), nośnik tła nie odczyta → **jednostronna relacja z Ø** [122–124]. **Masa = siła jednostronnej relacji nośnika z nierozróżnialnym tłem.** Status: m_e/m_P = y_e·(v/m_P)/√2 — stosunek stosunków; „co ustala y_e” otwarte także w fizyce → **nie osobny krok na końcu, tylko jeden z wykładników ustalanych razem z resztą (§F1, poprawka 136); „masa na końcu” z [94] = kolejność definiowania, nie wyprowadzania (por. 137; poprawka 142).** Masa protonu głównie z transmutacji, nie z Higgsa: dwa mechanizmy, zgodnie z „kwarki i elektrony nie pozwolą na jedną funkcję”. **Dopisek (poprawka 166) [O]:** „siła jednostronnej relacji z tłem” (y·v) = odczyt **B** (współczynnik działania przy danej rozdzielczości); masa w sensie R1f-3 (faza na własne tyknięcie) = odczyt **A** (masa biegunowa). Bez pętli to samo; różni je relacja nośnika z polem EM między własnym tyknięciem a rozdzielczością — dla stosunków leptonów 1–3% (§F1, 154 pkt 3 i 166; pułapka nazewnicza nr 6).

**2. Asymetria [126].** ~~„asymetria między dwiema częściami zygzaka”~~ — **błąd asystenta:** L i R to składniki tego samego elektronu, nie materia/antymateria. [L] Sacharow (1967): potrzebne naraz — relacja rozróżniająca połówki zygzaka (oddziaływanie słabe czyta tylko L), faza nieusuwalna (naruszenie CP), brak równowagi. [O] Faza w punkcie ≡ Ø, więc każda faza przerzucalna w punkt jest usuwalna; **nieusuwalna istnieje tylko jako relacja faz ≥ 3 pokoleń** (Kobayashi–Maskawa 1973: przy dwóch wszystkie usuwalne) — zbieżność z triadą [?], ta sama liczba, nie wyprowadzenie. Brak równowagi = pseudokierunek z zapisu; „+1” = zapis, który przetrwał. Status: struktura przełożona; wielkość 10⁻⁹ otwarta także w fizyce (faza MS daje za mało).

**3. Przekład relacji faz na porządek przyczynowy.** Faza w punkcie ≡ Ø → fazę przypisuje się **linkom** (relacjom minimalnym = fotonom); odczytywalne tylko obiegi: **diament p≺q (dwa łańcuchy) = część elektryczna, korona (zygzak czterech linków) = część magnetyczna** (Pellegrin, „Dalej otwarte”; tam: „treść magnetyczna wymaga naprzemiennych kierunków relacji” — znów zygzak [?]). „Holonomie dołożone do par” przestają być wadą: przypisanie fazy relacjom to definicja pola EM jako relacji. Status: **przekład jest**; otwarta dynamika (wagi obiegów, zbieżność sum) = „działanie” w kolejności pojęć (A3), nie przekład.

Pkt 5–6 odczytu to zestawienie formalizmu z ramą, nie wyprowadzenie z P0–P6.

## R1e. Spin i fala EM — zapis relacyjny [T][L][O] (v3.5, 25.09; poprawki 143–144)

**Skąd:** lista pojęć [94] (spin, fala EM) po R1b–R1d; potrzebne przed §F1, bo czynnik spinowy (−1)^{2s}[(2s)² − ⅓] jest na liście wejść (poprawka 139). **Filtr:** „spin = wewnętrzny moment pędu” = cecha; pytanie „ile wynosi spin elektronu” źle postawione. Pytanie w ramie: **jaką relację tworzy nośnik z kierunkiem czytającego.**

### R1e-F. Zapis formalny

- **Spin ½ [T]:** stan nośnika minimalnego = punkt kuli B³ (R1b), wektor n; wg D0 ta kula jest przestrzenią kierunków. Odczyt wzdłuż osi czytającego m: p = (1 + n·m)/2 — **relacja dwóch kierunków**.
- **Znak [T][L]:** obrót o 2π: ξ ↦ −ξ; znak nieodczytywalny w punkcie, odczytywalny tylko jako relacja dwóch dróg (interferometria neutronowa: Rauch i in., Phys. Lett. A 54, 425 (1975); Werner i in., PRL 35, 1053 (1975)). Ten sam znak = (−1)^{2s} we współczynniku b biegnących sprzężeń (spin–statystyka).
- **s(s+1) [T]:** S² = Sx² + Sy² + Sz² wymaga trzech osi czytającego (triady) i jest ten sam dla każdej triady — niezmiennik relacji nośnik–triada (jak norma Minkowskiego).
- **Masa a spin [L] (Wigner 1939, §F1):** masywny — SO(3), wszystkie kierunki dostępne; bezmasowy — E(2), odczytywalna tylko helicność.
- **Fala EM — dwie różne kule, obie B³, obie ze stożkiem Minkowskiego [T][L]:**
  - (a) **sfera niebieska** = kierunki propagacji = stany czyste spinora (R1c);
  - (b) **kula Poincarégo** = polaryzacja: macierz koherencji J ≥ 0, det J = (S₀² − S₁² − S₂² − S₃²)/4 ≥ 0 — ta sama forma co det ρ w R1c (Han, Kim, Noz, Phys. Rev. E 56, 6065 (1997)); polaryzacja pełna = brzeg. **Kula (b) nie jest przestrzenią kierunków:** kąt polaryzacji liniowej θ ↦ 2θ na kuli.
- **Liczba polaryzacji [T]:** bezmasowe pole wektorowe w d wymiarach przestrzennych ma d − 1 polaryzacji; kubit (nośnik minimalny R1b) tylko przy d = 3; przy d = 4 — trzy stany, przestrzeń stanów wymiaru 8.

### Odczyt w ramie [O]

1. **Spin nie jest cechą:** każda odczytywalna wielkość spinowa to relacja — dwóch kierunków (nośnik, czytający), dwóch dróg (znak) albo nośnika i triady (s(s+1)). „Spin wzdłuż z” bez czytającego ≡ Ø (superpozycja, [110]).
2. **Znak 2π ma postać „faza w punkcie ≡ Ø” z R1d:** odczytywalne tylko porównanie. **Część (−1)^{2s} listy wejść §F1 jest już w ramie:** nośnik (ξ) vs jego złożenie (ξξ†, światło) — R1d pkt 5.
3. **Polaryzacja = relacja fotonu z osiami czytającego w płaszczyźnie prostopadłej do kierunku;** od czytającego nie zależy tylko helicność (E(2)).
4. **Fala EM** = regularny wzór relacji faz na linkach (R1d); bez odczytu ≡ Ø [264]; odczytywalna przez interferencję (relację dwóch dróg); częstość = częstość odczytu (E := ν, R1d).
5. **„Foton = minimalne wzbudzenie = minimalna informacja” [258] działa tylko w 3D:** polaryzacja fotonu jest kubitem wyłącznie przy d = 3. **Spójność z R1b, nie niezależny dowód** (R1b zakłada już, że nośnik minimalny to kubit).

### Stan i granice

- **Zdanie do upadku:** każda odczytywalna wielkość spinowa jest relacją (dwóch kierunków, dwóch dróg, nośnika i triady). Upada, jeśli jakąś da się odczytać z jednego nośnika bez odniesienia.
- ~~**[?] Skąd ⅓ w (2s)² − ⅓**~~ **ROZSTRZYGNIĘTE (poprawka 145) [L][T]:** ⅓ **nie jest 1/d** — to stała na każdy stan polaryzacji, z sumy po poziomach Landaua (ruch w płaszczyźnie prostopadłej do pola; Nielsen, Am. J. Phys. 49, 1171 (1981)). Wymiar wchodzi przez **liczbę stanów**: nośnik relacji (gluon) w D wymiarach czasoprzestrzeni ma D − 2 polaryzacji, z nich 2 z s_z = ±1 i D − 4 z s_z = 0 → 2·(4 − ⅓) − (D − 4)·⅓ = **(26 − D)/3**: D = 4 → 22/3 (znane 11/3 po połowie), D = 26 → 0 (znane znikanie jednopętlowej funkcji beta Yanga–Millsa w D = 26; nLab „beta function”, arXiv:hep-th/9907205). Oba zgodne tylko przy ⅓ niezależnym od D. **[O]:** tylko w 3D wszystkie polaryzacje nośnika relacji są „spinowe” (brak stanów s_z = 0) — spójne z pkt 5 (foton = kubit tylko w 3D); obserwacja, nie dowód.
- Otwarte dalej: „działanie” (wagi obiegów faz na linkach) i energia w pełni.

## R1f. Działanie i energia — zapis relacyjny [L][T][P][O] (v3.5, 26.09; poprawka 162)

**Skąd:** kolejność pojęć [H] (A11d): … pole → próżnia → **działanie → energia** → ładunek, spin → … → masa; [130] „dalej nie wiem, co to jest energia, masa”; [166]; [190] „zachowanie energii działa lokalnie, nie dla całego wszechświata”; sesja CC 2 [97] „zamienić słowa energia i odległość na konkretne relacje”. **Powód pilności (użytkownik, 26.09):** „Jeśli masa ma się ustalić naraz, to każde niedokończone pojęcie przed nią wejdzie do zespołu cicho. „+1” za punktem Page'a można zostawić jako otwarte i nic się nie zawali; niedokończona energia zawali F1.”

**Audyt — gdzie energia i działanie weszły do §F1 i A5d bez definicji:**

| gdzie | co weszło | stan po R1f |
|---|---|---|
| **152–155, cały zespół** | sprzężenia i Yukawy = **współczynniki działania** (efektywnego); β, γ = ich zależność od rozdzielczości | zespół jest zdaniem o działaniu — działanie zdefiniowane niżej |
| **155 A** (b) | „energia próżni Σ½ω” | użyta **wyłącznie różnica** ΔE(B) − E(0) = relacja próżni z otoczeniem (polem B) — dopisane w §F1 |
| **155 D** (λ, supertrace) | Σ(−1)^{2s} n·m⁴ — energia próżni zależna od φ (Coleman–Weinberg) | tylko różnica względem wartości pola — dopisane |
| **148, 150, 154** | „energie próżni”, „różnica energii próżni względem całości” | energia stanów ≡ Ø ma sens wyłącznie jako różnica względem otoczenia — dopisane |
| **150** | stałe jako „energie” sprzężone z czasami | energia jako wielkość sprzężona z zegarem czytającego (Page–Wootters) — niżej |
| **159, 161** (A5d) | przepływ energii (Jacobson; już zamieniony na bilans), T_H, warunek energii zerowej, M | energia grawitacyjna tylko przez brzeg — niżej |
| **R1d** | E := ν — jedyna dotychczasowa definicja (jeden nośnik, jeden czytający) | uzupełniona: pęd, masa, próżnia, zachowanie |

### R1f-1. Działanie

- **Poziom historii [L]:** amplituda historii = e^{iS/ħ} (Feynman); **S/ħ = liczba obrotów fazy wzdłuż relacji** (bezwymiarowa; ħ = przelicznik, A2 „ħ częściowo”). Faza w punkcie ≡ Ø, odczytywalne są tylko **porównania faz** (interferencja) — R1d. **Działanie nie jest cechą, tylko relacją faz między zapisami.** Obejmuje oba sektory z konstrukcji (także sumę po historiach zbiorów przyczynowych z działaniem BDG).
- **Poziom lokalny — wspólny nośnik: OBIEGI (holonomie) [T][P].** Rachunek `etap19_dzialanie_obiegi.py` — zdania zapisane przed rachunkiem; zamknięta siatka trójkątów (podzielony dwudziestościan, zaburzenie promienia ±25%, V = 642 i 2562, χ = 2), 5 ziaren:
  - **Z1 (grawitacja, Regge 2D):** kąt holonomii wektora przeniesionego wokół wierzchołka **niezależnie** (obrót wokół wspólnych krawędzi ścian, bez sumy kątów) = deficyt 2π − Σ kątów, dla każdego wierzchołka: **max różnica ≤ 3,6·10⁻¹⁵** (jeden wspólny znak konwencji obiegu; przeciwny znak — różnice do π). Deficyty lokalnie dowolne (−4,1…+4,2). — PRZESZŁO.
  - **Z2:** Σ deficytów = 4π = 2π·χ, różnica ≤ 6·10⁻¹³ (Gauss–Bonnet). — PRZESZŁO.
  - **Z3 (cechowanie U(1)):** działanie Wilsona S_W = Σ_f(1 − cos θ_f) (θ_f = obieg fazy wokół ściany) **bez zmiany** przy losowej fazie w wierzchołkach (faza w punkcie ≡ Ø): różnica 0; **kontrola:** „działanie” z faz krawędzi Σ(1 − cos a_e) zmienia się (o 0,6–89). — PRZESZŁO.
  - **Z4:** Σ obiegów fazy po zamkniętej powierzchni = 2π·n, n całkowite (n = −21…+10, odchylenie ≤ 4·10⁻¹⁵; liczba monopolowa). — PRZESZŁO.
  - **K (kontrola płaska):** wewnętrzny wierzchołek płaskiego wachlarza: deficyt i holonomia ≤ 8·10⁻¹⁶. — PRZESZŁO. **Błąd konstrukcji kontroli (asystent), poprawiony w trakcie:** pierwsza wersja wachlarza losowała kąty, przy przerwie > π trójkąty nachodziły (ziarno 2: deficyt = holonomia = −0,05, oba ≠ 0); także pierwsza wersja przenoszenia wektora zmieniała znak heurystycznie i przeorientowywała ściany po zaburzeniu (Z1: różnice π) — zastąpione obrotem wokół krawędzi i orientacją z niezaburzonej sfery.
- **Dwie wagi obiegu = dwie rodziny z R4 [L][O]** (nie dwie niezależne postacie):
  - **cechowanie:** waga = **faza obiegu**, **kwadratowo** (Wilson 1 − cos θ ≈ θ²/2 ↔ F²), **bez skali** — rodzina stożka (R4: Maxwell konforemny dokładnie w d = 4; sprzężenie bezwymiarowe, logarytm tylko przy d = 3 — 155). Wymaga trzeciego elementu: faza w punkcie ≡ Ø (157).
  - **grawitacja:** waga = **kąt obiegu × pole** (Regge: S = Σ_h A_h ε_h), **liniowo**, **ze skalą** (A/l_P²) — rodzina objętości (R4). W porządku: działanie BDG = **liczność małych przedziałów (diamentów) ze znakami** (A2) — tylko dwa pierwotne (porządek + liczność, A1).
  - **W porządku ten sam obiekt:** diament (przedział = dwa łańcuchy). BDG liczy diamenty z k elementami wewnątrz; faza na diamentach = część elektryczna pola (Pellegrin, R1d pkt 3). **Działanie = suma po obiegach; waga = liczność (grawitacja) albo faza (cechowanie).**
- **Suma obiegów po zamkniętym brzegu 2D = 2π · liczba całkowita — w obu sektorach** (Z2, Z4) [T][P]: na brzegu 2D ≡ Ø odczytywalna jest tylko liczba (lokalne obiegi dowolne) — zgodne z A5d pkt 1 (jedyna odczytywalna wielkość brzegu = liczba relacji przez brzeg).
- **Sztywność** (druga wariacja, A11d) — otwarte.

### R1f-2. Energia

- **E = −∂S/∂(tyknięcie czytającego) przy stałym miejscu czytającego** (Hamilton–Jacobi) = **liczba obrotów fazy na jedno tyknięcie czytającego, w miejscu czytającego = ν z R1d** *(uściślone w 163: „w miejscu czytającego” — inne odczyty tej samej fazy w R1f-3)* — R1d już była tą definicją; R1f pokazuje skąd. **Pęd** = obroty fazy na obieg (odległość, R1d); **masa** = obroty na własne tyknięcie (Compton; zygzak R1d; samoodczyt §F1); E·r = odczyty na obieg (R1d). **Energia, pęd, masa = jedna struktura (faza, S/ħ) czytana na trzy sposoby.** Zegar = podukład czytającego (Page–Wootters), nie parametr zewnętrzny.
- **Energia próżni:** próżnia ≡ Ø → **energia próżni sama w sobie nie istnieje** (rozbieżność o ~120 rzędów = interpretacja; A5c, Bianchi–Rovelli). Istnieją tylko **różnice względem otoczenia:** zależność od pola B (155 A), od wartości pola (155 D, 154), różnice między próżniami odczytywalne przez ściany i grawitację (154). **[L] Casimir:** siłę da się policzyć bez energii próżni, jako relację między płytami (Jaffe, PRD 72, 021301 (2005)) — mierzy się relację otoczenia, nie energię Ø.
- **Energia grawitacyjna [L]:** nie ma lokalnej gęstości (zasada równoważności); istnieje tylko jako **całka po brzegu** (ADM, Brown–York) = relacja przez brzeg — zgodne z A5d (M czarnej dziury odczytywalne tylko na brzegu; brak włosów, 160).
- **Zachowanie energii:** lokalne [190], względem zegara czytającego; w strukturze bez ciągłej symetrii najwyżej **średnio** [191]; dla całości brak (całość bez otoczenia; A5b, A5c).

### R1f-3. Pęd i masa z tej samej fazy — sprawdzenie (poprawka 163) [T][P][L]

**Rachunek** `etap20_faza_ped_masa.py` — zdania przed rachunkiem; 2000 losowych nośników (m = 0,1–5, |v| do 0,99), 2 ziarna; c = ħ = 1:

| zdanie | wynik |
|---|---|
| **M1:** m² = det(E·𝟙 + p·σ) (tożsamość R1c dla gradientu fazy) | ≤ 1,1·10⁻¹⁴ — PRZESZŁO |
| **M2:** każdy gradient czasopodobny = suma dwóch zerowych k₁ + k₂ (dwie części t = 0 — zygzak R1d), **m² = 2·(k₁·k₂)** | ≤ 7·10⁻¹⁵ — PRZESZŁO; kontrola: dwie części **równoległe** → m² ≤ 2·10⁻¹⁴ (masa 0) |
| **M3:** faza na **własne** tyknięcie = m, niezależnie od prędkości | ≤ 1,4·10⁻¹⁴ — PRZESZŁO |
| **M4:** przesunięcie zera fazy (E → E + 0,7) psuje M3 (zależność od |v|, korelacja +0,71, odchylenie do 4,6) | PRZESZŁO — **zero fazy ustala niezmienniczość Lorentza (R1c)** |

**Błąd asystenta w warunku kontroli M3 (poprawiony przed przyjęciem wyniku):** zakładał, że wszystkie inne tempa rosną z prędkością; jedno maleje — warunek zmieniony na |korelacja| > 0,3.

**Cztery odczyty tej samej fazy (uściślenie, które rachunek wymusza):**
- **na własne tyknięcie nośnika = m** — niezmiennik; to jest masa;
- **wzdłuż linii świata nośnika, na tyknięcie czytającego = m·√(1−v²)** — maleje (korelacja z |v| −0,93); **to jest dylatacja** (R1a: „masa z zewnątrz spada do 0 przy v → c”);
- **w miejscu czytającego = E = γ·m** — rośnie (+0,71); to R1d „u innego czytającego większa” (**nie** dylatacja — sformułowanie R1d poprawione);
- **na odległość = |p| = γ·m·v** (+0,82).

**Wnioski [T][O]:** (1) **masa = relacja dwóch części t = 0** (M2): gdy ich kierunki nierozróżnialne (równoległe) — masy nie ma; zygzak R1d jako [T]; R1c pkt 3 — dla macierzy pędu m² = det P [T]. (2) **Zero fazy ustala Lorentz** (M4): w próżni nie ma nośnika, który by je ustalił → energia próżni sama w sobie nieodczytywalna — zgodne z R1f-2. (3) [L] Nierelatywistycznie masa też jest fazą: współczynnik fazy przy pchnięciu Galileusza (reguła superselekcji Bargmanna, 1954).

### R1f-4. Audyt po kolei — pojęcia w §F1 i A5d (poprawka 163)

| pojęcie | gdzie użyte | definicja w ramie | status |
|---|---|---|---|
| ładunek | 152 (hiperładunki), R1d | R1d: siła wiązania fazy; A2: z anomalii [86] | jest |
| sprzężenie α, g | cały §F1 | R1d: siła wiązania; α = odczyty na obieg | jest |
| skala / rozdzielczość t = ln(n₀/n) | cały §F1 | R1d: obieg odczytu | jest |
| spin | 152, 155 | R1e | jest |
| kolor, Casimiry | 152, 155 | grupa: 156–157 | warunkowo |
| stan (masowy, słaby) | 154, 155 | R1b (prawdopodobieństwa odczytów); 154 (relacja z tłem / z W) | jest |
| energia, działanie, energia próżni, potencjał | 148–155 | R1f-1, R1f-2 | jest |
| pęd, masa | R1f | R1f-3 | jest (po uściśleniu sformułowań) |
| krzywizna, grawitacja | 154, A5d | poprawka 113 + R1f-1 (krzywizna = kąt obiegu) | jest |
| **przyspieszenie** | **A5d: Unruh, T_H = κ/2π, κ = lim(V·a)** | **R1f-5 (poprawka 164): a·τ = 2√(E/τ), nadwyżka odwrotnej nierówności trójkąta** | **jest (od 164)** |
| temperatura | A5d | Ø od strony czytającego z przyspieszeniem; T·τ = √(E/τ)/π (R1f-5) | jest (od 164) |
| **S_bulk (wzór na wyspy)** | **A5d (b), pkt 3** | entropia splątania pola — **zależna od cięcia** (R5, poprawka 51) | **weszło cicho** |

- **Przyspieszenie — kandydat już w pliku [O][?]:** §F1 (etap8, „piąta pułapka”): **nadwyżka z odwrotnej nierówności trójkąta** τ(p,c) − τ(p,q) − τ(q,c) ≥ 0 — zero dokładnie dla prostej, niezależna od długości kroku. Przyspieszenie := nadwyżka na jedno tyknięcie — bez pojemnika. **Niesprawdzone** — następny krok.
- **S_bulk [L]:** we wzorze na wyspy sensowna jest tylko **entropia uogólniona** (pole brzegu/4G + S_bulk): zależna od cięcia część S_bulk przechodzi w renormalizację 1/G w członie brzegowym (Susskind–Uglum, PRD 50, 2700 (1994)). **W ramie:** odczytywalna jest tylko liczba relacji przez brzeg **razem** z resztą, nie każda część osobno — zgodne z „entropia jest efektem, a nie prawem” (C4a.16e).

### R1f-5. Przyspieszenie — nadwyżka z odwrotnej nierówności trójkąta (poprawka 164) [T][P][O]

**Definicja (kandydat z R1f-4, z §F1 etap8 „piąta pułapka”):** trzy kolejne elementy trajektorii p ≺ q ≺ c; **nadwyżka E = τ(p,c) − τ(p,q) − τ(q,c) ≥ 0** (zero dokładnie dla prostej); w porządku τ = najdłuższy łańcuch (miara odczytu, R1a), a E_L = L(p,c) − L(p,q) − L(q,c) ≥ 0 **zawsze** (nadaddytywność łańcuchów). **Przyspieszenie na tyknięcie: a·τ = 2·√(E/τ)**, τ = L(p,q) — **stosunek dwóch liczebności, bez gęstości i bez pojemnika.** Kontinuum: ruch o stałym przyspieszeniu własnym daje E = (2/a)[sinh(aδ) − 2 sinh(aδ/2)] = a²δ³/4 + O(a⁴δ⁵) [T].

**Rachunek** `etap21_przyspieszenie.py` (zdania przed rachunkiem):

| zdanie | wynik |
|---|---|
| **A1** (kontinuum 1+1): 2√(E/δ³) → a jak δ² (stosunek błędów 4 przy połowieniu δ); prosta: E = 0; pchnięcie trójki nie zmienia E | stosunki 4,00 dla a = 0,1–2; E(prosta) = 0; pchnięcia bez zmiany — PRZESZŁO |
| **A2** (kontinuum 3+1): zbieżność do |a^μ| (normy Minkowskiego) jak δ² | okrąg: |a| = 0,5625 = γ²v²/R, stosunki 3,97–3,99; losowa gładka trajektoria: 3,96–3,99 — PRZESZŁO |
| **A3** (porządek 1+1, sprinkling, ρ = 1000–64000 — 1,8 dekady; 120–600 prób na punkt): E_L ≥ 0 zawsze; (aτ)_est = 2√([E_L(a) − E_L(0)]/L(p,q)) zbiega do odniesienia kontinuum | E_L < 0 w **0** próbach; stosunki przy ρ = 64000: **0,995 / 1,005 / 1,011** (a = 0,5 / 1,0 / 1,5), zbieżne z góry od 1,03 przy ρ = 1000; odchylenie maleje ~ρ^(−1/3) (0,031 → 0,019 → 0,014 → 0,011 — obciążenie skończonej liczebności najdłuższego łańcucha) — PRZESZŁO |

**Błędy konstrukcji asystenta w A3 (jawnie, poprawione ze strukturalnego powodu przed przyjęciem wyniku):** (1) element q nie należał do zbioru przy liczeniu L(p,c) — łańcuch przez q niedostępny, E_L < 0 w 44 próbach; q jest elementem porządku; (2) porównanie z granicą δ → 0 zamiast z estymatorem kontinuum przy tym samym tyknięciu; (3) odniesienie liczone po **łuku**, a w porządku tyknięcie między kolejnymi elementami to **cięciwa** L(p,q) (łuku w porządku nie ma) — poprawka cięciwy przewidziana **przed** trzecim przebiegiem (0,995 / 0,980 / 0,955 wobec zmierzonych 0,990 / 0,984 / 0,966 w drugim); **warunek A3 zaostrzony po drugim przebiegu** (z „w stronę 1” na „w 2% albo 3σ przy najwyższej gęstości”), bo pierwotny był za luźny i przepuszczał dryf od 1.

**Odczyt w ramie [O]:** (1) **przyspieszenie = odchylenie własnego zapisu od najprostszej kontynuacji**, odczytywalne **od środka** (z liczebności własnych łańcuchów), jak masa na własne tyknięcie (R1f-3) — nie „przyspieszenie w przestrzeni”, tylko stosunek nadwyżki do tyknięcia. (2) Estymator daje **wielkość** |a|; kierunek przyspieszenia byłby relacją z triadą (3D) — [?], niepoliczone. (3) **Temperatura (Unruh) [L][O]:** T = a/2π → **T·τ = √(E/τ)/π** — Ø od strony czytającego z nadwyżką E wygląda termicznie z tym stosunkiem; A5d: κ = lim(V·a) — oba czynniki zdefiniowane (V = stosunek tempa odczytu, a z nadwyżki). **Ograniczenie:** test porządkowy tylko w 1+1 (pułapka 5: d = 1 + 1 literatury, nie płaszczyzna ramy) — w 3+1 estymator sprawdzony wyłącznie w kontinuum (A2); porządek 3+1 niepoliczony.

**Status:** definicje [O] asystenta, spójne z R1d (nic nie dokładają); formalizmy [L]; rachunek [P] tylko dla Z1–Z4 (2D, jedna siatka topologiczna — sfera). Czego rachunek nie pokazuje: czy w porządku (bez siatki) waga BDG i faza obiegu na tych samych diamentach dają w granicy działanie Einsteina–Hilberta i Yanga–Millsa jednocześnie — to hipoteza BDG i program Pellegrina/Sverdlova–Bombellego, niepoliczone u nas.

## R2. Retrospekcja 

Wersja w B2 („działa na rozkładach, nie na epizodach") jest prawdziwa, ale gubi ruch, który tam wykonano.

**Retrospekcja zwraca rozkłady, nie epizody.** Chwila zero wydarzyła się raz, więc estymator dostaje jeden pomiar na jeden nieznany parametr i rozrzut przekracza odstęp między k=1 a k=3. To jest granica metody, nie estymatora — więcej świadectwa nie ma i nie będzie.

**Wyjście znalezione:** późne zdarzenia Ø są tego samego typu, więc pierwsza chwila zero jest **najstarszym egzemplarzem rodziny**, nie jedynym. Dostęp nie prowadzi wstecz — prowadzi **na drugą stronę tej samej relacji, którą już zajmujemy**: dzisiejsze zdarzenie Ø ma częściowe otoczenie, a my **jesteśmy** tym otoczeniem.

**Skutek dla porządkowania:** pytanie „co było przed" zostało zamienione na „**jaki jest stosunek otoczenia do zdarzenia Ø**". A to jest **dokładnie C2**. Retrospekcja chwili zero, warunek niezmienniczości wzrostu i C2 to **jedno pytanie w trzech miejscach pliku**, nie trzy sprawy. [A]

## R3. Stosunek otoczenia do Ø już ma nazwy [L]

W otoczeniach dobrze opisanych ta wielkość istnieje, jest nazwana i policzona. Szukanie jej od zera było stratą.

| człon | otoczenie | opisane przez | stosunek otoczenie : Ø | skąd cięcie |
|---|---|---|---|---|
| superpozycja | środowisko dekoherujące | kwantowy darwinizm (Zurek) | redundancja $R_\delta=1/f_\delta$ | **plateau** w informacji wzajemnej |
| osobliwość | promieniowanie | reguła wysp / QES, krzywa Page'a | entropia promieniowania do entropii dziury | **czas Page'a** → po filtrze: **stosunek liczebności = 1** (zapis czytającego : relacje przez brzeg), nie chwila (A5d (b), poprawka 161) |
| nieoznaczoność | pamięć kwantowa | entropowe relacje nieoznaczoności | człon warunkowy | niesprawdzone |
| 2D / Planck | skala | wymiar spektralny (CDT, AS, zbiory przyczynowe) | $d_s(\sigma)$ | bieg wymiaru |
| foton, t=0 | stożek świetlny | — | — | niesprawdzone |
| **chwila zero** | **nieznane** | **—** | **—** | **to jest niewiadoma** |

**Trzy rzeczy z tej tabeli:**

1. **Wszystkie opisane stosunki są stosunkami entropii.** Redundancja to informacja wzajemna względem entropii układu; krzywa Page'a to entropia promieniowania względem entropii dziury; nasze $f=\log e(C)/(n\log n)$ też. Jedna rodzina wielkości, nie luźne podobieństwo.
2. **Mają wewnętrzne cięcie.** Redundancja nie jest zdefiniowana przez wybrane z ręki k, tylko przez **plateau**: informacja wzajemna rośnie z rozmiarem fragmentu, wypłaszcza się na wysokości entropii układu, potem rośnie znowu. Cięcie daje kształt krzywej. To jest odpowiedź na to, na czym utknęło C1.
3. **Chwila zero jest jedynym członem bez opisanego otoczenia.** Stąd inwersja: kalibrować tam, gdzie znamy oba człony, odwracać tam, gdzie znamy tylko strukturę. Układ ma jedną niewiadomą, nie osiem.

## R4. Podział konforemny — dokąd co należy [A][L]

Wychodzi czterokrotnie z czterech niezależnych stron i jest najostrzejszym wynikiem strukturalnym v3.2.

Teoria zbiorów przyczynowych rozkłada metrykę na strukturę przyczynową i konforemny czynnik skalujący: **porządek niesie strukturę przyczynową, gęstość elementów koduje czynnik objętości**. To jest A1 nazwane inaczej. Wykład Sorkina nosi tytuł „Gravity from Order and Number".

Stąd:

- **Rodzina stożka** (Weyl, wolne pole): wielkości będące progami na strukturze przyczynowej. Elektromagnetyzm jest konforemnie niezmienniczy **dokładnie w czterech wymiarach** — ślad tensora energii-pędu znika tam i tylko tam; ogólniej cechowane p-tensory są konforemnie niezmiennicze w 2p+2 wymiarach. Znajomość dualności Hodge'a na 2-formach wyznacza metrykę konforemną — wynik unikalny dla d=4.
- **Rodzina objętości** (Ricci, materia, masa): wielkości reagujące na czynnik objętości. Masa łamie niezmienniczość konforemną, bo wprowadza skalę.

**Cztery dojścia do tego samego:**
1. rozbicie A1 na porządek i liczność;
2. konforemna niezmienniczość Maxwella wyłącznie w d=4;
3. u Minza i u Gallego Torromégo „bezmasowe = brzeg między obszarami";
4. dowód Jacobsona jest ścisły **dla pól konforemnych**, a dla nieconforemnych wymaga osobnego, niedowiedzionego założenia — granica jego pewności przebiega dokładnie tą linią.

**Kryterium sortujące, zmierzone (A9c):** czy wielkość przeżywa odkształcenie konforemne przy ustalonym n. Ostrzejsze niż „wolne od n", bo sprawdzone po obu stronach.

## R5. Czego ta rama nie może dać — ograniczenia twarde [L]

- **Dwa pierwotne ⇒ jeden wolny wykładnik.** W obszarze konforemnie płaskim porządek ma **dokładnie jeden parametr**. Zmierzyliśmy to dziesięcioma wielkościami z pięciu niezależnych dróg i za każdym razem wychodziło d albo funkcja d. Nie dlatego, że źle liczono — dlatego, że nie ma tam nic innego.
- **Algebry lokalne w KTP są czynnikami typu III.** Nie ma rozkładu na iloczyn tensorowy „wnętrze × zewnętrze", nie ma macierzy gęstości obszaru, nie ma skończonej entropii splątania bez obcięcia. Prawo powierzchniowe jest stwierdzeniem o regularyzacji. Intuicja „dwa węzły tworzą relację i ta relacja to przestrzeń" jest bliższa obrazowi modularnemu niż dwudzielnemu splątaniu — ale narzędziem jest wtedy teoria modularna, nie entropia podukładu.
- **Skończony zbiór przyczynowy daje skończone macierze, czyli typ I.** Nie odtworzy typu III z konstrukcji. Cokolwiek liczymy, jest regularyzacją, a część własności może być przy skończonym n niedostępna **z zasady**, nie z braku mocy obliczeniowej.
- **Usunięcie rozmaitości nie usuwa założenia.** Żeby mieć porządek, trzeba go czymś wygenerować; sprinkling, wzrost sekwencyjny i KR to trzy różne założenia. Założenie przenosi się z geometrii do reguły wzrostu.

---


## Cel

Porządkowanie struktury logicznej. Nie nowa fizyka, nie nowe aksjomaty, nie nowe byty. Wolno budować nowe konstrukcje z istniejących składników.

**Tylko prawda jest ciekawa.** Wynik dopasowany do znanej liczby jest nudny, bo nie dowiadujesz się z niego niczego.

## Przed liczeniem — sześć zdań 

1. **Sprawdź literaturę** Sprawdzenie kosztuje zapytanie, rachunek kosztuje sesję.  odkryto koło **cztery razy**: Glaser–Surya (lokalność), Minz (bliźniaki), Boguñá–Krioukov (odległość przez nakładanie przeszłości), Sorkin–Yazdi (prawo objętościowe). Wszystkie były do znalezienia jednym zapytaniem.
2. **Rachunek bez zdania, które mogłoby przez niego upaść, nie jest rachunkiem.** Kryterium z A0 („czy istnieje liczba, która mogłaby wyjść inaczej") stosuje się do własnych przebiegów, nie tylko do cudzych publikacji.
3. **Kontrole graniczne PRZED rachunkiem.** Jeśli nie da się takiej wypisać, rachunek jest niesprawdzalny.
4. **Kontrole łapią błędy rachunku, nie pojęciowe.** Na świeżym terenie milczą.
5. **Liczba bez warunków nie jest wynikiem.** Zawsze n, d, estymator, liczba prób.
6. **Porządkowanie idzie przed liczeniem.**

Pełne reguły — §E.

## Sześć pułapek nazewniczych — lista kontrolna

Cztery pierwsze wystąpiły w rachunkach; piąta to różnica konwencji między tym plikiem a literaturą; szósta to dwa odczyty jednej wielkości pod jedną nazwą w samym pliku (poprawka 166). Za każdym razem błąd wszedł przez etykietę, nie przez rachunek.

| | pułapka | pełny zapis |
|---|---|---|
| **1** | **Ø jest absolutne.** Nie ma „rodzajów Ø". Różni je wyłącznie relacja otoczenia — własność otoczenia, nie Ø. **Dopisek v3.4 (użytkownik):** przenoszenie różnic otoczeń na Ø jest kuszące jak opinia; **wolno pośrednio, pamiętając, że to pośrednio** — nigdy jako cecha samego Ø. Reguła językowa w §E. | A3 |
| **2** | **Ø ≠ zbiór pusty.** „Element o pustej przeszłości" jest doskonale odróżnialny, więc nie jest Ø. | A3 |
| **3** | **Horyzont nie jest końcem relacji — ale „jednostronność" go nie definiuje.** Zdanie prawdziwe o wszystkim nie wyróżnia niczego. | A5 |
| **4** | **Otoczenie: elementy czy relacje?** Trzy różne wielkości. **Zamknięta w v3.2** — patrz C2. | A8, C2 |
| **5** | **„4D” i „2D” — dwie konwencje pod jedną nazwą.** W pliku 3+1 liczy **punkty odniesienia** (triada + odczyt), nie osie; 2D w łańcuchu Ø = płaszczyzna bez pamięci. W literaturze d=2 = 1 przestrzeń + czas. **Rozstrzygnięte w v3.4: to są różne rzeczy** (R1a, „3+1 używane świadomie”). | R1a |
| **6** | **„Masa” — dwa odczyty pod jedną nazwą (poprawka 166).** **A** = faza na własne tyknięcie nośnika (R1f-3) = masa biegunowa; **B** = współczynnik działania (Yukawa · v) przy danej rozdzielczości (R1d, punkt otwarty 1; §F1 „masy biegnące”). Bez pętli to samo; poza tym różni je relacja nośnika z polem EM — dla stosunków leptonów 1–3%, a relacja Koidego zachodzi tylko na A (na B: Q − 2/3 = 1,16·10⁻³, 63σ). Wystąpiło w 154 pkt 3: „bez skali” uzasadnione na B, Koide liczony na A. | §F1 (154, 166), R1d, R1f-3 |

**Reguła z pułapki nr 3:** poprawka może przenieść błąd o piętro, zamiast go usunąć. Po każdej poprawce pytać, **czy nowe zdanie coś wyróżnia, czy jest prawdziwe o wszystkim.** Wystąpiło ponownie w v3.2 przy L (patrz A9d).

## Dopuszczalne stany

Otoczenie ma **dwa** stany: pełne i częściowe. **Całkowity brak otoczenia wypada z układu.** To ograniczenie na hipotezy, nie wynik pomiaru.

## Gdzie zaczynać

**Stan v3.5 (poprawka 142).** Oś 1–2 (czas, c, 3D) domknięta strukturalnie w R1a–R1c; R1d = przekład elektronu, pola EM i kwarka. Kolejność pracy (bez rachunków):

1. **Porządek po poprawce 136** — zrobione w 142.
2. **Spin i fala EM z R1b/R1c — zrobione w R1e (143):** spin = kierunek jako stan nośnika (kula odczytów = kula kierunków, D0); polaryzacja (kula Poincarégo — **inna kula niż kierunki**, θ ↦ 2θ; poprawka 144): S₀² − S₁² − S₂² − S₃² ≥ 0 = ta sama norma Minkowskiego co det ρ (R1c). Potrzebne przed §F1, bo czynnik (−1)^{2s}[(2s)² − ⅓] jest na liście wejść (poprawka 139).
3. **§F1: tabela wszystkich logarytmów i lista wejść — zrobione (146–147).** Następne (poprawka 151): **zespół funkcji [94]** — wypisać z A2, R1d i biegu mas cały zespół (sprzężenia i masy wszystkich fermionów) jako relacje stosunków od logarytmu liczebności, każdą funkcję przypisać do typu relacja / relacja relacji; cel: struktura zespołu, nie liczby [88]. Literatura: grupa renormalizacji jako samopodobieństwo („przepływ” po filtrze = relacja rozdzielczości odczytu). **Zrobione (152–158, 165–167):** zespół wypisany i wyprowadzony; stan — zestawienie „STAN ZESPOŁU” w §F1 (167); stosunki e : μ : τ — rama ich nie ustala (166).
4. Później: energia w pełni i „działanie”; czarne dziury po oczyszczeniu OTW; liczby otwarte (y_e, 10⁻⁹, H₂, α). *(Energia i działanie: R1f, 162–164; czarne dziury: A5d, 159–161.)*

**Techniczne, nadal otwarte (z v3.2):**

1. Czy prawo $n^{k-(k-1)d}$ z A3a jest gdzieś opublikowane — Minz 2406.14533 pod kątem wykładnika. **Dopisek v3.3 [L]:** Johnston, doktorat (arXiv:1010.5514, §4.2.1) opisuje pomysł Rideouta: materia jako klasy elementów o identycznych relacjach („pary niehegelowskie”) — to są bliźniaki z A3a, kilkanaście lat przed Minzem.
2. Wzór asymptotyczny na średnią liczbę rozszerzeń liniowych n-elementowego porządku (z rozszerzenia dowodu Kleitmana–Rothschilda na pary (P, ≺)) — narzędzie analityczne na dryf f(KR) z A9b.
3. Zmiękczony stan SJ — bez niego entropia na zbiorze przyczynowym łamie prawo powierzchniowe i liczby są poprawne, ale nie o próżni (A10).

---

# §A — UPORZĄDKOWANE

## A0. Ramy [H]

**Świadomość** to unikalna struktura interakcji, która jako zbiór jest interakcją.

**Fakt** = stan wspólnego aparatu poznawczego, ekstrapolowany na zewnątrz. Fakt nie jest obiektywny — jest ograniczoną formą komunikacji.

**Opinia** = ten sam mechanizm na stanach indywidualnych. Zaprzeczenie komunikacji.

**Matematyka** nie „jest", dlatego działa niezależnie od interakcji. Staje się komunikacją wtedy i tylko wtedy, gdy ma oparcie w strukturze logiki **oraz** jest sprawdzalnym pomostem do aparatów poznawczych. Kryterium robocze: **czy istnieje liczba, która mogłaby wyjść inaczej.**

**Niezmiennik** = struktura relacji, w której liczność jest elementem struktury, nie dodatkiem.

> **Status w v3.2:** to jest zapis stanowiska, nie aparat rachunkowy (poprawka nr 19). Kryterium robocze z tego akapitu jest jedyną rzeczą stąd, która ma zastosowanie operacyjne — i ma je także do własnych rachunków.

## A1. Dwa pierwotne

| | |
|---|---|
| **porządek** | ≺, antysymetryczna, przechodnia. Para uporządkowana = rozdzielenie czasopodobne. Para nieuporządkowana = rozdzielenie przestrzenne. |
| **liczba** | liczność. **Element struktury, nie jej uzupełnienie.** [H] — teza sporna, patrz B4 |

**[L]** Malament 1977: struktura przyczynowa daje metrykę z dokładnością do czynnika konforemnego; brakującą skalę daje liczenie objętości.

$$\text{porządek} + \text{liczba} = \text{geometria}$$

Dwa pierwotne dają **jedną** niezależną kombinację bezwymiarową: $N\sim L^d$. Stąd $d$ jest jedynym wolnym wykładnikiem struktury.

> **Rozwinięcie w v3.2 (A):** to nie jest tylko ograniczenie na kształt odpowiedzi. To jest **przewidywanie o tym, czego nie da się znaleźć w płaskiej przestrzeni**, i zostało potwierdzone dziesięcioma wielkościami — patrz R5 i A9e.
>
> **Terminologicznie:** porządek ↔ struktura konforemna, liczność ↔ czynnik objętości. Wielkość niezależna od n jest w granicy wyznaczona przez sam porządek, czyli przez geometrię konforemną. Kryterium „wolne od n" **jest** kryterium „wyznaczone przez strukturę konforemną", a nie techniczną ostrożnością.

## A2. Tablica przekładu

### Czas, przestrzeń, ruch

| wielkość | zapis relacyjny | warunki / status |
|---|---|---|
| czas własny | $\tau = L$ = długość najdłuższego łańcucha. Liczba całkowita. **Odczyt (v3.4): miara jednego odczytu wzdłuż trajektorii, nie czas — R1a.** | [L] |
| objętość | $V = N$ = liczba elementów w interwale porządku | [L] |
| przestrzenność | para nieuporządkowana | [L] |
| wymiar | wykładnik $N\sim L^d$ | [P] sprinkling do diamentu: d=2→2,02; 3→3,05; 4→4,07; 5→5,06 |
| ułamek uporządkowania | $\Gamma(d{+}1)\Gamma(d/2)/2\Gamma(3d/2)$ | [T] d=2→1/2, d=3→0,2286, d=4→1/10, d=6→1/56. Kontrola n=3000: 0,4990 / 0,2315 / 0,1055 ✔ |
| prędkość | $L_{\text{ścieżki}}/L_{\max}=\sqrt{1-v^2}$ | [P] błędy 0–5% przy N=4000 |
| geodezyjna | najdłuższy łańcuch. Zero swobody. | [L] |
| krzywizna | odchylenie $N$ od wzrostu jak $n^d$ | [L] |
| strzałka czasu | rząd części antysymetrycznej. Przełącznik, nie kontinuum. | [P] n=20 |
| $c$ | **nie jest wielkością mierzoną**: stożek jest porządkiem, więc c ≡ 1; foton = zero elementów pośrednich. Dwustronna prędkość = przelicznik (łańcuch ↔ odległość), jednostronna = konwencja. **Pełny status: C4a.13; bilans przeliczników: B1.** | [P] |

**Uwaga do „wymiaru" [L], v3.2 — dwa różne pojęcia pod jedną nazwą.**
Wymiar Myrheima–Meyera zakłada zanurzenie w rozmaitość lorentzowską i liczy 1 czas + (d−1) przestrzeni. Wymiar porządkowy (Dushnik–Miller) to najmniejsza liczba porządków liniowych, których przecięcie daje dany porządek, i nie zakłada rozmaitości. **Nie są tym samym.**

Müller (2023): $\dim_{DM}(\mathbb{R}^{1,n})=\aleph_0$ dla każdego $n\ge2$; dolne oszacowanie $\aleph_0$ dotyczy wszystkich wcześniej zdefiniowanych wymiarów porządkowych. Meyer (1993): wymiar Minkowskiego i standardowy wymiar porządku pokrywają się **w wymiarze dwa i nie w wyższych**.

Czyli: **liczba „4" nie jest własnością porządku, tylko założonego zanurzenia.** Porządek zapytany o własny wymiar odpowiada „nieskończoność". Zgodność zachodzi wyłącznie przy jednym kierunku przestrzennym — gdy kierunki są dwa lub więcej, rozdzielenie przestrzenne przestaje być przecięciem skończonej liczby porządków liniowych. To jest ścisła wersja zdania „czasu nie wolno traktować jak wymiaru".

Podział pracy: **porządek daje liczbę ($d_{MM}$, wolną od n), założenie rozmaitościowości daje jej nazwę.** Stąd bierze się test Glasera–Suryi (C1).

### Grawitacja, horyzont, kosmologia

| wielkość | zapis relacyjny | warunki / status |
|---|---|---|
| działanie | Benincasa–Dowker–Glaser: zliczanie interwałów o małej liczności ze znakami naprzemiennymi | [P][L] S/n: sprinkling 4D→0,70; 2D→2,55; KR→−325; perkolacja→−20 |
| pole horyzontu | liczba molekuł. **Nie „par jednostronnych"** — A5 | [P] stosunek 0,92–1,14 bez dryfu; $a^{(4)}=\sqrt3/10$; wykładnik 0,431 wobec 0,500 przy 28–64 molekułach |
| $G$ | przelicznik zliczanie↔geometria. W zliczaniu $G\equiv1$. | [L] Jacobson |
| $\Lambda$ | $\sim1/\sqrt N$. N=2,18×10²⁴⁴ → 6,8×10⁻¹²³ wobec 2,9×10⁻¹²² | [L] Sorkin 1987, chybienie ×4,3 |
| płaskość | $R_s/R=(R/R_H)^2$ — tożsamość algebraiczna | [T] |

**POPRAWKA do $R_s/R_H$** Dla kuli o promieniu $R$ przy gęstości krytycznej $R_s/R=(R/R_H)^2$; redukuje się do $\Omega$ tylko gdy $R=R_H$. Przy $R_H=14{,}5$ Gly i $R_p=46{,}1$ Gly: $R_p/R_H=3{,}18$ to **stosunek promieni**, a $R_s/R_p=10{,}1$ to **stosunek analogiczny do Ω**. **Do wpisywania: $R_s/R=(R/R_H)^2$ z podaniem $R$.** Wzór nosi własną kontrolę; sama liczba nie.

**Uzupełnienie do „działania" [L], v3.2.** Działanie BDG jest **odpowiednikiem działania Einsteina–Hilberta dla zbioru przyczynowego**, liczonym z liczebności małych interwałów porządku $N_0, N_1, N_2, N_3$. Hipoteza Benincasy–Dowkera: na sprinklingu daje działanie Einsteina–Hilberta plus człon brzegowy (objętość przecięcia brzegu przeszłego i przyszłego). Istnieją osobne prace o członie brzegowym (Dowker; Buck–Dowker–Jubb–Surya).

**Konsekwencja dla B4 i dla „kosztu" (A11):** funkcja kosztu konfiguracji **już istnieje** i nazywa się działaniem. Nie trzeba jej definiować.

### Ładunek, sprzężenia, α

| wielkość | zapis relacyjny | status |
|---|---|---|
| ładunek | $Q=\tfrac12\pm\tfrac{1}{2N_c}$ | [P] |
| hiperładunki | $Y_L=-N_cY_Q$, $Y_e=2N_cY_Q$, $Y_u=-(N_c{+}1)Y_Q$, $Y_d=(N_c{-}1)Y_Q$ | [P] |
| współczynniki beta | $(-1)^{2s}(4s^2-\tfrac13)$ | [P] |
| $\alpha$ | $1/\alpha=\frac{2}{3\pi d}\ln(N_\Lambda/N)$; nachylenie $\Sigma N_cQ^2=8{,}000$ | [P] |
| $\alpha$ geometrycznie | promień Bohra / **zredukowana** długość Comptona = 137,036 | [P] |

α **nie jest przelicznikiem** — jest bezwymiarowa od początku. [H]

→ Cały zespół (sprzężenia, masy, λ) z tych przekształceń: **§F1, „Zespół funkcji [94]” (poprawka 152).**

---

## A3. Ø

**Ø jest absolutne.** [H] Nieodróżnialność tak samo w chwili zero, jak w superpozycji w laboratorium.

> **POPRAWKA nr 1** Ø jest jedno, różni je wyłącznie **relacja otoczenia**. Po poprawce te same liczby ułożyły się na jednej osi — nic nie było przeliczane.

> **POPRAWKA nr 3** **Ø ≠ zbiór pusty.** Element o pustej przeszłości jest doskonale odróżnialny.

**Dopuszczalne są dwa stany otoczenia: pełne i częściowe.** [H]

### A3a. Prawo nieodróżnialności [P][T]

**Wartość.** Bliźniaki = pary o identycznej przeszłości i przyszłości.
$$E[k\text{-krotki nieodróżnialne}] \;\propto\; n^{\,k-(k-1)d}$$
Wykładniki zmierzone: d=2 → +0,026 (przew. 0); d=3 → −0,888 (−1); d=4 → −1,467, lokalnie zbieżny do −1,91 (−2).
Warunki: sprinkling do diamentu przyczynowego Minkowskiego, regresja po n w kilku dekadach, jądro oddzielone od brzegu.

**Kontrola, która przeszła.** Łańcuch: |Aut| = 1, e(C) = 1. Antyłańcuch: |Aut| = n!, e(C) = n!.

**Test predykcyjny.** Trójki w d=2 → **−0,978** wobec przewidzianego **−1**. Wypisane PRZED rachunkiem. ✔

**Co by obaliło.** Wykładnik niezależny od d. Albo zależność od gęstości sprinklingu przy ustalonym n. Albo trójki w d=2 dające cokolwiek poza −1.

**Czyja teza.** [A] rachunek; [H] pojęcie Ø.

Wymiar krytyczny $d_{\text{kryt}}(k)=k/(k-1)$: k=2→**2**, k=3→1,5, k→∞→1.

> **ZNALEZIONE W LITERATURZE (v3.2) [L].** Pojęcie ma nazwę: Minz (2024) nazywa dwa elementy **singleton-symetrycznymi**, gdy pokrywają się ich zbiory elementów połączonych linkiem — w przeszłość i w przyszłość. To są bliźniaki z A3a, co do definicji.
>
> **Twierdzenie 4.1 (Minz):** sprinkling w d-wymiarowym Minkowskim jest całkowicie lokalnie niesymetryczny **z prawdopodobieństwem 1** — w nieskończonym sprinklingu bliźniaków nie ma wcale.
>
> **To nie obala A3a.** Dowód idzie przez region $I_t$ o objętości rosnącej z t i **wymaga nieograniczonego t**. W ograniczonym diamencie t jest ograniczone i argument nie startuje. A3a mierzy w diamencie przy rosnącej gęstości — inny reżim.
>
> **Zgodność w granicy:** wykładnik $k-(k-1)d$ jest ujemny dla $d>k/(k-1)$, więc bliźniaki znikają. A3a jest **ilościową wersją twierdzenia Minza w ograniczonym obszarze**. Przypadek d=2, k=2 jest graniczny (wykładnik 0) — plik już to zauważył jako $d_{kryt}(2)=2$.
>
> **Czego u Minza nie ma: wykładnika.** Pisze jakościowo, że porządki KR mogą zawierać symetrie lokalne chętniej niż sprinklingi. **Prawo $n^{k-(k-1)d}$ w tej pracy nie występuje.** Następne miejsce do sprawdzenia: Minz, „Local symmetries in partially ordered sets", arXiv 2406.14533.

### A3b. Sonda działa na skali jednego elementu [P]

**Wartość.** Średnie rozdzielenie par bliźniaczych ~1/n. Wykładnik −1,011 wobec −1. Iloczyn $n\cdot\langle sep\rangle$:

| n | 50 | 100 | 200 | 400 | 800 |
|---|---|---|---|---|---|
| $n\langle sep\rangle$ | 2,04 | 2,00 | 1,97 | 1,99 | 1,96 |

Czyli **dokładnie d = 2** przy szesnastokrotnej zmianie n. Stała nie dopasowywana.

**Co by obaliło.** $n\langle sep\rangle$ rosnące lub malejące z n; wartość różna od d.

**Czego to NIE dowodzi.** Sprinkling do płaskiej czasoprzestrzeni jest czterowymiarowy na każdej skali z konstrukcji. Redukcja $d\to2$ **jest założeniem, nie wynikiem** (§D).

---

## A4. Pamięć i druga zasada

**Pamięć = niedomiar symetrii etykietowania.** [A]

$$\text{zapomniane}=\log e(C),\qquad \text{zapamiętane}=\log n!-\log e(C)$$

> **Dopisek v3.5 [H][O] (poprawka 138).** **log e(C) nie ma orientacji:** e(C) = e(C odwróconego) (każde rozszerzenie liniowe odwraca się w rozszerzenie porządku odwróconego) — zgodne z definicją czasu. log e(C) = liczba uporządkowań „przed/po”, których struktura nie ustala = **ilościowa postać „stan nie niesie etykiety przed/po”** (R1a). Podział A4 zapomniane / zapamiętane = **rozproszone / ostre** z R1a, na dwóch poziomach: log e(C) — część nieczytelna dla **każdego** czytającego (cała struktura); część zależna od czytającego (mózg vs aparat) = przeszłość aparatu 𝒫_X = {Y : I(M_X : Y) > 0} (R1b-F, D2). Łączy definicję czasu z A4d.


**Kontrole, które przeszły.** Łańcuch → 0,0000. Antyłańcuch → 1,0000. Estymator SIS sprawdzony wobec dokładnego zliczania przy n=16–24: SIS-60 myli się o 0,1–2,3%.

> **POPRAWKA nr 11 (asystent, v3.2) — o zakresie walidacji SIS.** SIS-60 był walidowany przy n=16–24, a używany przy n=80–1280. Obciążenie **rośnie z n i zależy od struktury**:
>
> | punkt | 60 prób | 500 | 5000 | 20000–50000 |
> |---|---|---|---|---|
> | sprinkling d=4, n=80 (S) | 208,69 | 211,03 | 212,29 | 213,51 |
> | sprinkling d=4, n=320 (f) | 0,6520 | 0,6603 | 0,6620 | 0,6713 |
> | KR, n=320 (f) | 0,6473 | 0,6500 | 0,6490 | 0,6498 |
>
> Przy n=320 sprinkling nie saturuje nawet przy 20000 prób (3%), a KR saturuje przy 0,4%. **Porównywanie f między strukturami przy stałej liczbie prób jest samo obciążone.**

### A4a. Ułamek zapomniany — wielkość ZALEŻNA OD n

| n | d=2 | d=3 | d=4 |
|---|---|---|---|
| 20 | 0,504 | 0,723 | 0,841 |
| 80 | 0,489 | 0,695 | 0,819 |
| 320 | 0,463 | 0,653 | 0,772 |
| 1280 | 0,454 | 0,635 | 0,740 |

estymator SIS-60. Odtworzone niezależną implementacją.

### A4b. Niezmiennikiem jest f(d), nie ułamek [P]

$$\text{ułamek}=\frac{S}{\log n!}=f(d)\cdot\frac{n\ln n}{\ln n!}$$

Czynnik $\ln n!/(n\ln n)$ rośnie bardzo wolno do 1: 0,670 (n=12) → 0,781 (n=80) → 0,829 (n=320) → 0,861 (n=1280) → 0,907 (n=45000). Ułamek **musi** więc maleć do f(d) od góry. To tożsamość, nie pomiar.

> **POPRAWKA nr 5** v2 porównywało f(4)=0,700 z ułamkiem 0,772 jako „zgodność dwóch niezależnych rachunków". Fałsz: są związane tożsamością, więc przy n=320 **muszą** różnić się o 17%. Zgodność wyszła **dlatego**, że zawyżone f pomnożono przez pominięty czynnik 0,83.

> **POPRAWKA nr 9** „Droga przez ułamek" i „pomiar bezpośredni" to **jedno wyrażenie**, bo $\ln n!$ się skraca: $f=\frac{S}{\ln n!}\cdot\frac{\ln n!}{n\ln n}=\frac{S}{n\ln n}$. Więc rozbieżność 9% przy n=80 to **dwa niezgodne rachunki $\log e(C)$ w jednym punkcie**, nie dryf z n. Domyka się przeliczeniem jednego punktu.

> ## POPRAWKA nr 13 — A4b i A4c′ ZAMKNIĘTE
>
> **To nie były dwa niezgodne rachunki $\log e(C)$. To były dwa różne obszary.**
>
> Pomiar bezpośredni brał `P[:n]` z jednego sprinklingu do n=400. Po sortowaniu po czasie jest to **dolna warstwa diamentu, nie interwał przyczynowy**. Odtworzone:
>
> | n | 40 | 80 | 120 | 160 | 240 | 320 | 400 |
> |---|---|---|---|---|---|---|---|
> | f, sposób `P[:n]` | 0,697 | 0,715 | 0,718 | 0,720 | 0,714 | **0,693** | **0,650** |
> | f, niezależny diament | 0,625 | 0,645 | 0,653 | 0,654 | 0,653 | 0,652 | 0,651 |
> | ułamek uporządkowania przy `P[:n]` | 0,027 | 0,028 | 0,029 | 0,029 | 0,031 | 0,046 | 0,099 |
>
> Plik miał 0,7006 / 0,6977 / 0,6950 / 0,6970 / 0,7004, potem 0,684 i 0,628 — **ten sam kształt i ten sam punkt załamania**. Mechanizm widać w ostatnim wierszu: obcięty obszar ma ułamek uporządkowania 0,028, czyli $d_{MM}=5{,}5$, i wraca do 4,02 dopiero gdy n dobija do 400.
>
> **Kontrola wewnętrzna:** krzywa f(d) w d≈5,5 interpoluje na ~0,73; zmierzono 0,715. **0,700 leży na tej samej krzywej, przy wymiarze, który ten obszar naprawdę ma.**
>
> **0,700 to f(≈5,5), nie f(4).** Nie było anomalii. Była jedna krzywa i jeden źle podpisany obszar.
>
> Do tego: pięć „stabilnych" punktów n=40–240 to **jedno losowanie czytane pięć razy** — zagnieżdżone, nie niezależne. Stabilność była pozorna z konstrukcji.
>
> Kategoria błędu jest już w §D: „Myrheim–Meyer po całym diamencie jest obciążony — formuła jest dla interwału przyczynowego, nie dowolnego zbioru." Plik miał diagnozę i nie zastosował jej do własnego pomiaru f.
>
> **Rozrzut, którego nikt nie podawał:** przy n=80, d=4 f waha się między losowaniami od 0,617 do 0,673 (8,6%), a ułamek uporządkowania wynosi 0,103 ± 0,021 (±20%). Jeden sprinkling przy n=80 nie jest dobrze określoną strukturą.

**Wartości f(d) obowiązujące (v3.2), n=320, SIS-2000, niezależne diamenty:**

| d | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| f — v3.1 (SIS-60) | 0,391 | 0,546 | 0,637 | 0,709 | 0,758 |
| **f — v3.2** | **0,394** | **0,559** | **0,656** | **0,715** | **0,765** |

Wartości v3.1 były zaniżone przez obciążenie SIS-60, tym bardziej im wyższe d.

### A4c. (1−f)·d — status obniżony [P][A]

| d | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| (1−f)d — v3.1 | 1,218 | 1,362 | 1,452 | 1,455 | 1,452 |
| **(1−f)d — v3.2** | **1,212** | **1,322** | **1,377** | **1,424** | **1,412** |

Rozrzut: sd(f) = 0,003–0,010 → ±0,02–0,04 na (1−f)d.

**Test predykcyjny (stoi).** Z d=2,3,4 wyekstrapolowano plateau, stąd przewidziane f(5)≈0,70 i f(6)≈0,75 — wypisane PRZED rachunkiem. Wyszło 0,709 i 0,758. ✔

> **POPRAWKA nr 14 (asystent, v3.2) — poprawka nr 10 ODWRÓCONA.**
>
> Poprawka nr 10 mówiła: kolano, nie zbieżność; gładka forma $a+b/d$ dopasowana do d=2,3 celuje w 1,650, czyli w inną liczbę niż plateau; przyrosty +0,144 / +0,090 / +0,003 / −0,003.
>
> Przy poprawionych f przyrosty wynoszą **+0,110 / +0,055 / +0,047 / −0,013** — bez załamania. Dopasowanie $a+b/d$ **wyłącznie z d=2,3** daje
> $$(1-f)d \;=\; 1{,}542-0{,}661/d$$
> i przewiduje d=4,5,6 z maksymalną resztą **0,020**. Wersja z v3.1 chybiała o 0,054 i rosła.
>
> **Nie ma kolana. Jest zbieżność do ~1,54.** Kolano było artefaktem obciążenia rosnącego z d.

> ## POPRAWKA nr 12 — A4c traci status niezmiennika
>
> Odkształcenie gęstości przy ustalonym n (konforemne, czyli przy niezmienionych stożkach) przesuwa sprinkling d=4 po krzywej f(ułamek uporządkowania) **nieodróżnialnie od sprinklingów o innym d**:
>
> | obiekt | ułam. up. | f |
> |---|---|---|
> | sprinkling d=3 | 0,2454 | 0,5503 |
> | odkształcony d=4, λ=−0,90 | 0,1779 | 0,6101 |
> | sprinkling d=4 | 0,1053 | 0,6493 |
> | odkształcony d=4, λ=+0,90 | 0,0570 | 0,6874 |
> | sprinkling d=5 | 0,0354 | 0,7255 |
> | **Kleitman–Rothschild** | **0,3781** | **0,6243** |
>
> Odkształcone leżą na krzywej nieodkształconych z odchyleniem **≤0,022**. KR leży od niej o **0,168** — osiem razy dalej.
>
> Czyli w rodzinie konforemnie płaskiej **f jest funkcją samego ułamka uporządkowania**. A ułamek wyznacza $d_{MM}$. Więc $(1-f)\cdot d$ **jest funkcją samego d** — przekodowaniem wymiaru Myrheima–Meyera, nie wielkością niezależną. „Plateau" to miejsce, w którym ta jedna krzywa się wypłaszcza.
>
> To tłumaczy, dlaczego (1−f)d było tak wrażliwe na obciążenie estymatora: wielkość pochodna, bez własnego oparcia.
>
> **Pytanie „czy plateau to 3/2" traci desygnat.** Nie ma czego pytać.
>
> **Co A4c zachowuje:** rolę **wskaźnika rozmaitościowości**, bo KR rzeczywiście odstaje (A9b). To jest słabsza rola niż „kandydat na niezmiennik" i niż „kandydat na test B4".
>
> **Dawne A4c′ (skąd 0,700; czy plateau to 3/2) — zamknięte** poprawkami 13 i 12: pierwszy punkt przez diagnozę obszaru, drugi przez utratę desygnatu. Sekcja usunięta w v3.4.

### A4d. Druga zasada jako twierdzenie [T][A]

$e(C')\ge e(C)$ dla C ⊂ C′ (podporządek). ~~bo nowy element zawsze można dopisać na końcu~~ — **„na końcu” przemycało kierunek (poprawka 106); dowód bez kierunku (poprawka 138):** każde rozszerzenie liniowe C′ obcięte do C jest rozszerzeniem C, i każde rozszerzenie C daje się tak otrzymać (obcięcie jest „na”), więc e(C′) ≥ e(C). Równość ⇔ położenie nowych elementów jest wymuszone (np. nowy element porównywalny ze wszystkimi); dla wzrostu łańcuchowego zawsze równość.

**Kontrole, które przeszły.** Wzrost łańcuchowy → S = 0,000000 przy n=10, 30, 60. Monotoniczność potwierdzona w d=2 i d=4.

**Co to daje.** Strzałka czasu i wzrost entropii są tu **jednym zdaniem**. Druga zasada nie jest tendencją statystyczną.

### A4e. To NIE jest entropia horyzontu

$\log e(C)$ skaluje się jak $n\ln n$. Entropia horyzontu skaluje się jak **pole**, kowymiaru 2: $A\sim L^{d-2}$, a przy $N\sim L^d$ daje $n^{(d-2)/d}$ — dla d=4 jak $n^{0{,}50}$.

> **POPRAWKA nr 8 (użytkownik, v3).** v2 i v3 miały $n^{(d-1)/d}$, czyli objętość plastra, nie pole. **Kontrola, która to wyłapuje bez liczenia:** rozmowa 2 podawała rozbieżność rosnącą jak $n^{1{,}5}$, co wychodzi z $n^2/4$ wobec $n^{0{,}5}$. Błąd był wykrywalny z samego pliku.

| entropia | skalowanie | wobec $n^{0{,}5}$ (d=4) |
|---|---|---|
| liczba porządków | $\approx n^2/4$ bitów | $n^{1{,}5}$ |
| rozszerzenia liniowe $\log e(C)$ | $n\ln n$ | $n^{0{,}5}\ln n$ |

Uczciwy status: **ścisła entropia Boltzmanna z dowiedzioną drugą zasadą, i nie jest to entropia, którą mierzy horyzont.**

> **Wzmocnienie w v3.2 [P].** Zmierzono wprost przez cięcie przestrzenne sprinklingu: nadwyżka informacji przez cięcie ma wykładnik **1,08 (d=2) i 1,17 (d=4)**, wobec powierzchniowych 0,50 i 0,75. **Prawo objętościowe, nie powierzchniowe.** Przewidziane przed rachunkiem i potwierdzone. Kontrola obciążenia: przy 500/2000/20000 prób wartość chodzi w granicach 15–30% bez systematycznego dryfu.
>
> To samo dotyczy entropii Sorkina–Johnstona (A10): wykładnik 1,057. **Dwie niezależne entropie na zbiorze przyczynowym, obie objętościowe.**

Przestrzeń i pamięć są przeciwstawne: co daje miejsce obok, odbiera porządek przed. Jedna liczba, $\log e(C)$, czytana z dwóch stron. [O]

---

## A5. Horyzont — i co właściwie liczy definicja molekuł

> **POPRAWKA nr 2 (użytkownik, rozmowa 3).** „Horyzont to koniec relacji" było błędem; definicja molekuł z 2019 coś liczy i wynik jest uniwersalny dla wszystkich horyzontów przyczynowych.

> **POPRAWKA nr 6 (audyt v2, asystent) — poprawka nr 2 przeniosła błąd o piętro.** „Miejsce relacji jednostronnych" jest prawdziwe i **nie wyróżnia niczego**: antysymetria czyni każdą parę uporządkowaną jednostronną. Własność należy do przekroju, a tam jest tautologią.

**Trzy piętra jednostronności:**

| piętro | co tam jest |
|---|---|
| **para** | puste. Antysymetria. |
| **przekrój** | definicja, nie wyróżnik. „Jednostronny" = „A domknięte w dół" = **A jest zbiorem przeszłym**. |
| **treść** | **który** zbiór przeszły, **plus** link, **plus** warunek max/min. To liczy definicja z 2019. |

**Definicja molekuł horyzontu** [L] (Barton, Counsell, Dowker, Gould, Jubb, Taylor 2019, PRD 100, 126008): $p^-$ i $p^+$ **oba w przeszłości Σ**; $p^-$ na zewnątrz horyzontu, $p^+$ wewnątrz; $p^+$ jest **jedynym** elementem przeszłości Σ w przyszłości $p^-$.

**Wartość** [P]. Stosunek zmierzonego do przewidywanego 0,92–1,14 bez dryfu, przy $a^{(4)}=\sqrt3/10=0{,}1732$. Wykładnik 0,431 wobec 0,500.
**Kontrola, która przeszła.** Stara definicja Dou–Sorkina (1999) rozbiega w d≥3 — potwierdzone własnym rachunkiem (1,52–1,57 zamiast 0,50).
**Co by obaliło.** Wykładnik inny niż 0,5 przy większej liczbie molekuł; zależność od typu horyzontu.
**Zasięg.** Uniwersalny dla wszystkich horyzontów przyczynowych.

### A5a. Ile zawęża warunek „przekrój jednostronny" [P]

$b(d)=1-\log_2 J/n$, gdzie $J$ = liczba zbiorów przeszłych.

**Kontrole wypisane przed rachunkiem:** łańcuch → $J=n+1$; antyłańcuch → $J=2^n$, b=0; ułamek uporządkowania → 0,5000 / 0,2286 / 0,1000; przekrój przeszły → dokładnie 0 relacji wstecz. **Wszystkie przeszły.**

| d | b(d), n=12→36 |
|---|---|
| 2 | 0,48 → 0,66 |
| 3 | 0,30 → 0,35 |
| 4 | 0,12 → 0,17 |

> **POPRAWKA nr 20a (asystent, v3.4).** v3.1 pisało „w d=4 horyzont jest jednym z ~$2^{0{,}85n}$ przekrojów jednostronnych". Liczba 0,85 to **środek dryfu podany bez etykiety n**: b(4) idzie 0,12→0,17 przy n=12→36, więc 1−b idzie 0,88→0,83. Poprawnie: **$2^{(1-b(4))n}$ z podaniem n**, albo zakres 0,83–0,88 dla n=12–36.

**Zastrzeżenie:** stabilne jest tylko uporządkowanie b(2) > b(3) > b(4). W d=2 i d=3 wartości dryfują (§D).

### A5b. Liczby fizyczne [P]

**Otoczenie osobliwości** (molekuły horyzontu): **1,43×10⁶²** (masa Księżyca), 1,05×10⁷⁷ (słoneczna), 4,43×10⁹⁶ (M87\*). Skaluje się jak $M^2$; przy masie Plancka zostaje ~12,6.

> **POPRAWKA nr 11a (asystent, v3.2) — Księżyc.** v3.1 podawało **2,65×10⁶²**, co nie pasuje do własnego prawa $M^2$. Przy kotwicy 1,05×10⁷⁷ (masa słoneczna, $1{,}989\times10^{30}$ kg): M87\* → 4,436×10⁹⁶ (plik 4,43×10⁹⁶ ✔), masa Plancka → 12,57 (plik ~12,6 ✔), Księżyc ($7{,}342\times10^{22}$ kg) → **1,43×10⁶²**. Liczba 2,65×10⁶² odpowiada masie 9,99×10²² kg — domysł [?]: wpisano okrągłe 10²³.
>
> **Kontrola wewnętrzna, wystarczy podzielić.** Błąd był wykrywalny z samego pliku, bez żadnego zewnętrznego źródła.

**Sfera fotonowa** $r=1{,}5r_s$. Opóźnienie: 9,3×10⁻⁵ s (słoneczna), 399 s (Sgr A\*), **7,0 dni (M87\*)**.

**Krawędź obserwowalnego:** horyzont cząstek 46,1 mld ly, powierzchnia ostatniego rozproszenia 45,2 mld ly. Chwila zero leży na **obwodzie**, nie w tyle.

**CMB:** horyzont cząstek przy rekombinacji 280,14 Mpc, rozwiera **1,158°**; każdy punkt ma relację z **0,0102%** powierzchni; **9,8×10³** obszarów bez wzajemnej relacji, zgodnych co do 10⁻⁵.

**Energia fotonów CMB:** zniknęło **99,9083%**. Brak symetrii przesunięcia w czasie ⇒ brak zachowania energii (Noether). Entropia współporuszająca zachowana do 6 miejsc.

**Masa jako gęstość zwrotów:** elektron 1 zwrot na 2,39×10²² elementów, mion 1,16×10²⁰, proton 1,30×10¹⁹. **Uwaga: to przepisanie $m/m_P$, nie wynik** (B1).

---

### A5c. Kosmologia, GPS, ruch nieustający — w ramie (v3.5; poprawka 140) [H][L][O]

- **Chwila zero na obwodzie (A5b); patrzeć do przodu, żeby zobaczyć tył [H].** Obserwowalny wszechświat = kula odczytów wokół nas. **Uściślenie [O]:** sfera CMB to nie ∂B³ w sensie R1c (sfera kierunków), tylko **granica, na której zapis przechodzi z ostrego w rozproszony** (wcześniej plazma rozprasza światło); za nią nie Ø, lecz zapis nieczytelny — dokładnie R1a.
- **Horyzont = brzeg odczytywalności**, raz oglądany z zewnątrz (osobliwość), raz ze środka (chwila zero) [H]; [L] Gibbons–Hawking (1977): horyzont kosmologiczny ma temperaturę i entropię jak horyzont czarnej dziury.
- **„Co było przed Wielkim Wybuchem” = druga strona tej samej relacji (R2).** Planck zamyka regres od dołu, całość bez otoczenia od góry; wieloświaty i cykle potrzebują pojemnika albo zewnętrznego czasu (filtr). **Ślady „poprzednich eonów” ≡ śladom obecnym:** rozstrzygnąć da się liczby, nie historię (przeszłość = zapis teraz).
- **Λ [L]:** stała to stała; rozbieżność o ~120 rzędów bierze się z interpretacji energii próżni (Bianchi–Rovelli, „Why all these prejudices against a constant?”, 2010). Sorkin przewidział Λ ~ 1/√N przed 1998.
- **Ciemna materia [?]:** zdanie relacyjne się trzyma — **Ø od strony światła, nie od strony porządku** (nie odczytywana przez światło, obecna w porządku). „Interpretacja na interpretacji” — [?]: timescape (Wiltshire; Seifert i in., MNRAS Lett. 537, L55, 2025, arXiv:2412.15143) zastępuje ciemną **energię** (nie materię) i jest sporny; świadectwa ciemnej materii (soczewkowanie, piki CMB) nie stoją wyłącznie na przybliżeniu newtonowskim. Rozbieżność z interpretacją OTW (przybliżenie newtonowskie, globalny czas kosmiczny) [H] — do sprawdzenia osobno dla energii i materii.
- **„Fotony straciły energię” = interpretacja [H].** Energia = częstość odczytu względem czytającego (R1d); przesunięcie ku czerwieni = stosunek temp odczytu źródła i czytającego. 99,9083% w A5b = 1 − 1/(1 + z), z = 1089,9. Globalnego zachowania energii nie ma (brak symetrii przesunięcia w czasie; A5b).
- **GPS [H][L]:** cztery satelity = 3+1 punkty odniesienia, czas odbiornika wychodzi jako niewiadoma (rozmowa [151]). Dylatacja zależy od **potencjału**, nie od natężenia pola (w środku Ziemi pole zerowe, zegar najwolniejszy); potencjał da się odczytać tylko jako **stosunek dwóch zegarów** (R1d: dylatacja = stosunek temp).
- **Ruch nieustający vs pobieranie pracy [H][O].** Ruch nieustający = fundament ramy (zero absolutne nieosiągalne) i nie przeczy fizyce (orbity, prądy w nadprzewodniku). **Pobieranie pracy — lokalnie nie**, ale nie z globalnej symetrii przesunięcia w czasie (której całość nie ma), tylko z drugiej zasady, która tu jest twierdzeniem (A4d). **Dla całości pytanie źle postawione:** całość nie ma otoczenia, nie ma komu oddać pracy. Hasło „perpetuum mobile się da” przeczy A4d, jeśli znaczy perpetuum mobile II rodzaju.


### A5d. Czarne dziury — OTW bez interpretacji, przez definicję czasu i 3D (v3.5; poprawka 159) [H][L][T][O]

**Skąd:** [460]–[472], [547]; warunek wstępny użytkownika [462]: „trzeba oczyścić OTW z interpretacji. Ta teoria nie mówi nic o żadnym zapadaniu, krzywiznach, ani nieskończonych gęstościach”; sesja CC 1 [82]: definicji czasu nie wolno używać bez połączenia z tym, jak czas tworzy 3D. Trzy zdania „OTW bez interpretacji” z „Dalej otwarte” przepuszczone przez filtr (R1a, R1b, R1c).

**Naruszenia w pierwszej wersji analizy (asystent) — poprawione niżej:**

| sformułowanie | co łamało |
|---|---|
| „łańcuch o skończonej liczbie odczytów, **ostatni** odczyt, łańcuch **kończy się** za brzegiem” | „ostatni”, „kończy się” zakładają „potem” — odczyt zawsze teraz [334, 394]; „za brzegiem” = mówienie o Ø wprost; osobliwość opisywać wyłącznie nie wprost, przez bezpośrednie otoczenie (poprawka 113; sesja CC 2 [25]) |
| „front światła się **zwęża**”, θ jako „tempo” wzdłuż promienia | „nie mówić, że foton cokolwiek robi” [142]; c = przekaz informacji, nie pokonywanie dystansu [493] |
| „powierzchnie uwięzione **powstają** ze zwykłych danych” | zagadnienie początkowe (dane → ewolucja) przemyca kierunek (poprawka 106) |
| „**przepływ** energii przez horyzont” | narracja; energia = częstość odczytu względem czytającego (R1d) → bilans |

**1. Horyzont od strony 3D [H][O].** 3D = triada + zapis (dostęp do innych układów niż bieżący; R1b krok 4, [400]); bez zapisu — płasko. **Od strony czytającego z zewnątrz obszar, którego zapisu nikt z zewnątrz nie odczyta, nie ma swojego „+1” — zostaje z niego brzeg: 2D = płaskość ≡ Ø.** Brzeg złożony z promieni światła (powierzchnia zerowa, t = 0); sesja CC 2 [52]: „**Sama powierzchnia sfery jest 2D ≡ Ø; dla całej sfery t = 0**.” **Entropia ∝ pole — źródło strukturalne, nie narracja:** jedyne, co odczytywalne o obszarze, to liczba relacji przez jego brzeg 2D (molekuły, A5 [P]). „Zawarte, ale nieodczytywalne” + zawartość liczona brzegiem = „agregat informacyjny” [466] z podstawą w dowodzie 3D. **Pułapka 5:** „redukcja wymiaru do 2” przy osobliwościach w literaturze (Carlip, CDT, wymiar spektralny) = d = 1 + 1, nie nasza płaszczyzna bez pamięci — nie utożsamiać.

**2. Równanie Einsteina jako równanie stanu (Jacobson, PRL 75, 1260 (1995)) — PRZESZŁO jako bilans.** S = **liczba relacji przez lokalny brzeg odczytywalności** (molekuły, A5), **nie** entropia splątania (zależy od cięcia: R5, poprawka 51; [H] „entropia jest efektem, a nie prawem”); T = **Ø od strony czytającego z przyspieszoną trajektorią** (trajektoria = zapis, „dym” [134]; reguła językowa: „od strony otoczenia X Ø wygląda jako Y”); „dla każdego lokalnego horyzontu” = dla każdego czytającego z osobna, bez globalnego czasu (zachowanie energii tylko lokalnie [190]); G = przelicznik (A2); zamiast „przepływu” — bilans częstości odczytu. **Równanie Einsteina = skutek liczności** (A1: liczność element struktury), Λ = stała całkowania (Jacobson; zgodne z poprawką 150).

**3. Osobliwość — PRZESZŁO, wyłącznie nie wprost.** Twierdzenia Penrose'a–Hawkinga: istnieją krzywe przyczynowe o skończonej mierze odczytu (najdłuższy łańcuch = miara jednego odczytu, nie czas — R1a), których nie da się przedłużyć; „nieskończona gęstość” = interpretacja [462]. **Wszystkie przesłanki leżą po stronie otoczenia:** brak zamkniętych krzywych przyczynowych = antysymetria porządku (A1); warunek energii zerowej = dodatniość (częstość odczytu ≥ 0; R1c, R1d); powierzchnia brzegowa = [460] (pkt 4). Wniosek dotyczy Ø. **W ramie: „od strony otoczenia spełniającego te warunki struktura ma brzeg ≡ Ø”** — dozwolone przeniesienie na Ø pośrednio (reguła językowa, [414]); o tym, co „za” — nic. **Bez etykiety kierunku** (poprawka 138) to samo zdanie opisuje chwilę zero: **osobliwość ≡ chwila zero** (łańcuch Ø; [547]; sesja CC 2 [113]).

**4. Brzeg lokalny zamiast horyzontu zdarzeń.** Horyzont zdarzeń ∂J⁻(𝓘⁺) — **NIE PRZESZEDŁ:** teleologiczny, wymaga „kiedykolwiek” = całości i kierunku; odczyt zawsze teraz, całość bez otoczenia. **Błąd asystenta z [463]:** „definicja czysto porządkowa” — porządkowa, ale globalna; to samo dotyczyło zdania „nie leżą w przeszłości **żadnego** czytającego” (niżej, „Dalej otwarte”). **Zostaje brzeg określony strukturalnie [L][O]:** powierzchnia, przy której światło (linki) po żadnej stronie nie dokłada relacji przestrzennych (powierzchnia uwięziona / horyzont pułapkowy: Hayward, PRD 49, 6467 (1994); Ashtekar–Krishnan, Living Rev. Rel. 7, 10 (2004)) — **[460] użytkownika = przesłanka Penrose'a**, zapisana jako stosunek liczebności; „wyprzedziło” w [460] = skrót za **stosunek** tworzenia do odczytu, nie kolejność. **Bez etykiety kierunku** brzeg „uwięziony” ≡ „anty-uwięziony” (kosmologiczny): horyzont z zewnątrz ≡ horyzont ze środka (sesja CC 2 [113]; A5c). Dylatacja (stosunek tempa odczytu → 0) — tabela granic Ø w R1a, bez zmian.

**5. [470] — czy czarne dziury są konieczne (bez „powstawania”):** w strukturze z antysymetrią i dodatniością brzeg ≡ Ø jest obecny wszędzie, gdzie stosunek tworzenia do odczytu spełnia [460] [T — twierdzenie] — zdanie o strukturze, nie o przebiegu; nie osobny postulat. [L] Christodoulou (*The Formation of Black Holes in General Relativity*, 2009, arXiv:0805.3880) — tylko jako informacja, że takie konfiguracje nie są wyjątkiem (bez języka „powstają”).

**6. [547] — pustynia od horyzontu:** od strony otoczenia horyzont = ostatnia rozróżnialna struktura (jak kwarki), osobliwość = Ø (jak Planck), między nimi nic rozróżnialnego [545, 547].

**Czarna dziura po oczyszczeniu (stanowczo):** od strony czytającego z zewnątrz — **brzeg 2D ≡ Ø** (bez własnego „+1”, bo zapis obszaru nieodczytywalny z zewnątrz), na którym światło po żadnej stronie nie dokłada relacji przestrzennych [460]; stosunek tempa odczytu dalekiego do bliskiego → 0 [472]; jedyna odczytywalna liczba = liczba relacji przez brzeg (∝ pole); równanie wiążące = bilans liczby relacji przez lokalne brzegi (Jacobson, S = molekuły). **Nie ma:** zapadania, krzywizny jako „wyginania”, nieskończonej gęstości, horyzontu „na zawsze”, niczego „za” brzegiem.

**Dalej (pytania, niepoliczone):** ~~(a) czy warunki końca z poprawki 154 mają odpowiednik przy osobliwości~~ **(a) — rozstrzygnięte niżej (poprawka 160);** ~~(b) promieniowanie Hawkinga i krzywa Page'a jako Ø → A~~ **(b) — rozstrzygnięte niżej (poprawka 161).**

**(a) WARUNKI KOŃCA PRZY OSOBLIWOŚCI (poprawka 160) [L][O].**
- **Postawienie:** warunki ze 154 dotyczą samego Ø (relacja Ø z Ø nie istnieje; sąsiedztwo końca nierozróżnialne); Ø jest jedno (pułapka 1), więc przy osobliwości ≡ Ø obowiązują **tak samo i trywialnie** — w tej postaci pytanie nic nie wnosi. **Dobrze postawione:** czy **otoczenie** osobliwości ma tę samą charakterystykę co otoczenie końca Plancka i czy warunki dają tam coś **odczytywalnego** (jak przy Plancku m_H, m_t po naszej stronie pustyni). Dwa otoczenia (A5d): czytający blisko osobliwości (od środka nic się nie zmienia) i czytający z zewnątrz (tylko brzeg 2D ≡ Ø).
- **1. Od strony czytających blisko osobliwości:**

| koniec Plancka (rama) | otoczenie osobliwości (literatura) |
|---|---|
| [76]: „przestrzeń, czyli relacja pomiędzy dwoma węzłami, jest = 0 — nie da się wyróżnić żadnej relacji” | **cisza asymptotyczna** (BKL: Biełinski–Chałatnikow–Lifszyc 1970; Andersson–van Elst–Lim–Uggla, PRL 94, 051101 (2005)): relacje między sąsiednimi punktami znikają, każdy punkt sam dla siebie |
| **λ(koniec) = 0:** tło bez relacji z samym sobą | **„materia nie ma znaczenia”** (BKL): potencjał pola skalarnego (λφ⁴, masa) nie odgrywa roli, liczy się część kinetyczna — **relacja tła z samym sobą nierozróżnialna, bez niczyjego żądania** |
| **β_λ(koniec) = 0:** sąsiedztwo nierozróżnialne, koniec samopodobny | **z polem skalarnym otoczenie „spokojne”** (Andersson–Rendall, CMP 218, 479 (2001)): jedna samopodobna postać Kasnera, bez oscylacji; **w 3D bez pola skalarnego — chaos BKL** (Mixmaster; Damour–Henneaux–Rendall–Weaver, Ann. Henri Poincaré 3, 1049 (2002)), bez prostej samopodobnej postaci |

    **Wniosek [O]:** literatura opisuje otoczenie osobliwości tak, jak rama koniec Plancka; oba warunki 154 mają odpowiedniki, których nikt nie dokładał (MS ma pole skalarne — Higgs) — potwierdzenie ≡ od strony literatury. Bez etykiety kierunku: BKL (zrobione dla osobliwości kosmologicznej) stosuje się tak samo do wnętrza czarnej dziury — zgodne z „osobliwość ≡ chwila zero” (pkt 3). **Pułapka 5:** „efektywne 1 + 1 w każdym punkcie” = liczenie literatury; w ramie brak relacji między węzłami = brak triady = ≡ Ø. **Zastrzeżenie:** rotujące czarne dziury mają inne wnętrze (horyzont Cauchy'ego, „mass inflation”); powyższe dotyczy osobliwości przestrzennopodobnych.
- **2. Z zewnątrz — NIE dają odczytu, i to jest wynik:** twierdzenie o braku włosów (Israel, Carter, Robinson) [L] — przez brzeg odczytywalne tylko **M, J, Q** (w ramie: M = relacja z tłem, J = relacja kierunków (R1e), Q = relacja faz U(1)); reszta ≡. **Brak włosów skalarnych** (Bekenstein, PRD 5, 1239 (1972)) [L]: pole skalarne nie zostawia śladu na brzegu — **relacja tła, której dotyczą oba warunki, z zewnątrz nieodczytywalna.** [O][?] (węższy odczyt asystenta, 158): ładunek abelowy odczytywalny na brzegu (Gauss), kolor nie („kolorowe” czarne dziury niestabilne — Bizoń, PRL 64, 2844 (1990); kolor uwięziony).
- **Werdykt (stanowczo):** (1) **odpowiedniki istnieją** — cisza asymptotyczna = [76], nieistotny potencjał = λ ≡ 0, spokojna postać Kasnera przy polu skalarnym = samopodobny koniec; niezależne potwierdzenie osobliwość ≡ koniec Plancka ≡ Ø. (2) **Z zewnątrz nie dają nowej liczby:** przy Plancku pustynia leży po naszej stronie i funkcje zespołu łączą koniec z odczytami tutaj (→ m_H, m_t); przy czarnej dziurze pustynia [547] leży **za brzegiem 2D ≡ Ø**, przez który przechodzą tylko M, J, Q — żadna funkcja zespołu nie łączy osobliwości z odczytem z zewnątrz. **Warunki obowiązują, ale nie ustalają odczytu.**

**(b) PROMIENIOWANIE HAWKINGA I KRZYWA PAGE'A (poprawka 161) [T][L][O][?].** Sformułowania sprawdzone wobec R1a i R1b: bez „parowania w czasie”, „potem”, „dziura emituje”; o Ø tylko od strony otoczenia.
- **0. Filtr na pytanie.** „Paradoks informacyjny: czy informacja ginie?” — **źle postawione**; R1a wprost: „informacja nie ginie **w strukturze**, ale przestaje być **odczytywalna z danego miejsca**”. Dobrze postawione: **dla którego czytającego i przy jakiej liczbie odczytów zapis obszaru staje się odczytywalny.** „Parowanie” jako przebieg w czasie → przeparametryzować przez **liczebność** (ile kwantów czytający ma zapisanych), nie chwilę. **„Firewall”** (Almheiri–Marolf–Polchinski–Sully, JHEP 02 (2013) 062) **wyklucza się z ramą:** zakłada coś dramatycznego na brzegu dla spadającego czytającego — sprzeczne z pkt 1 tabeli granic Ø (od środka mechanizmy te same) [O].
- **1. Promieniowanie Hawkinga = Ø od strony czytającego z zewnątrz [L][O].** Ten sam mechanizm co pkt 2 (Unruh): **próżnia ≡ Ø od strony czytającego stojącego poza brzegiem wygląda jak termiczna** — reguła językowa, nie „dziura coś wysyła”; w tabeli granic Ø: skok Ø → A = nowy odczyt. **T_H = κ/2π, κ = lim(V·a)**: V = stosunek tempa odczytu dalekiego do bliskiego (→ 0), a = przyspieszenie potrzebne do utrzymania się (→ ∞; *przyspieszenie: R1f-5 (poprawka 164), a·τ = 2√(E/τ)*); **w ramie: T_H mówi, jak szybko stosunek tempa odczytu znika na brzegu** [472] — iloczyn skończony, choć każdy czynnik osobno nie. Rozkład termiczny = **zapis rozproszony** (R1a): pojedynczy odczyt nie niesie struktury.
- **2. Krzywa Page'a — funkcja liczebności, nie czasu [T][L].** Page, PRL 71, 1291 (1993) [T]: dla losowego stanu czystego na R ⊗ B średnia entropia ≈ min(ln d_R, ln d_B) (z małą poprawką) — **czysta kombinatoryka liczności, bez czasu**. Krzywa Page'a (PRL 71, 3743 (1993)) = ten sam wynik z liczbą zapisanych kwantów na osi. **Punkt Page'a = równość liczebności:** zapis czytającego (R) = liczba relacji przez brzeg (∝ pole, pkt 1 wyżej) — **stosunek = 1, nie chwila**; to „cięcie” z tabeli R3 bez „czasu Page'a”. Przy S ∝ M² równość przy M ≈ M₀/√2 [L].
- **3. Wyspy / QES — formuła i wynik, nie opowieść [L][O].** S(R) = min ext_I [pole(∂I)/4 + S_bulk(R ∪ I)] (Penington, arXiv:1905.08255; Almheiri–Engelhardt–Marolf–Maxfield, arXiv:1905.08762); opowieść o replikowych tunelach euklidesowych odrzucona (jak w 150). *Dopisek 163 (R1f-4):* S_bulk zależy od cięcia; sensowna jest tylko suma pole/4 + S_bulk (entropia uogólniona; Susskind–Uglum 1994) — odczytywalna liczba relacji przez brzeg razem z resztą, nie części osobno. **W ramie:** entropia R = **najtańszy brzeg** (najmniejsza liczba relacji przez brzeg + reszta); za punktem Page'a najtańszy brzeg obejmuje obszar wewnątrz („wyspę”) — **zapis wnętrza należy do tego, co czyta posiadacz R.** R1a dosłownie: „ile przeszłości istnieje dla czytającego, zależy od jego zdolności zapisu” (mózg vs aparat, 200 klocków) — zapis wnętrza istnieje dla czytającego z dostatecznym R, dla innych nie: **„zawarte, ale nieodczytywalne” → „odczytywalne dla konkretnego czytającego”.** Zgodne z pkt 1 tabeli granic Ø: partner kwantu spadającego jest już częścią wyspy R — brak podwójnego liczenia, brak firewalla.
- **4. Połączenie z 3D [O][?].** Przed punktem Page'a: dla czytającego z zewnątrz obszar = brzeg 2D ≡ Ø, bez „+1” (zapis wnętrza niedostępny, pkt 1 wyżej). Za punktem Page'a: czytający z R ma zapis wnętrza = dostęp do innego układu niż bieżący (R1b krok 4) — **dla tego czytającego obszar zyskuje „+1”, staje się dostępny w 3D.** Przejście nie jest chwilą; rządzi nim stosunek liczebności (zapis czytającego : brzeg). [?] — odczyt asystenta, spójny z R1a/R1b, bez dowodu.
- **5. „Koniec parowania” przy masie Plancka [O].** Przy m ≈ m_P brzeg ma ~12,6 relacji (A5b), a ƛ_C ↔ r_s są swoimi lustrami (140): **czarna dziura ≡ nośnik elementarny** (zygzak ≡ pętla światła). **„Co zostaje” (resztki) — źle postawione:** tam nic nie odróżnia (≡ Ø).
- **Werdykt (stanowczo):** (1) paradoks w postaci „czy informacja ginie” — źle postawiony; R1a rozstrzyga: nie ginie w strukturze, chodzi wyłącznie o odczytywalność dla konkretnego czytającego. (2) Promieniowanie Hawkinga = Ø od strony czytającego z zewnątrz (Ø → A, reguła językowa); T_H = jak szybko stosunek tempa odczytu znika na brzegu. (3) Krzywa Page'a = funkcja liczebności (Page, [T]), bez czasu; punkt Page'a = równość zapisu czytającego i liczby relacji przez brzeg. (4) Za nim zapis wnętrza należy do posiadacza R (wyspy) — dosłownie „ile przeszłości istnieje, zależy od zdolności zapisu”. (5) Firewall wyklucza się z niezmienniczością od środka; resztki przy m_P — źle postawione.
- **Dalej [?]:** czy „+1” dla obszaru za punktem Page'a (pkt 4) da się ująć formalnie, jak krok 4 w R1b.

## A6. Wzorzec: porządek daje stosunki, liczba daje skalę [A][O]

| | stosunki | skala |
|---|---|---|
| Malament | metryka z dokł. do czynnika konforemnego | objętość |
| α | nachylenie $\Sigma N_cQ^2=8$ | punkt zaczepienia |
| ładunki | wymuszone przez $N_c$ | normalizacja U(1) |
| $(t_n)$ | określone z dokł. do wspólnego czynnika | $t_0=1$ konwencjonalnie |
| reguła Borna | $P(i)/P(j)$ nie wymaga normalizacji | $\Sigma\,\lvert i\rangle\langle i\rvert=1$ |

**Status sekcji: sporny.** Teza B4 [H] unieważnia to rozdzielenie jako artefakt opisu.

> **Wzmocnienie w v3.2.** To rozdzielenie **jest** podziałem konforemnym z §R4: „stosunki" to strona porządku (Weyl, konforemne, elektromagnetyzm), „skala" to strona liczności (Ricci, objętość, masa). A6 i R4 to jedno spostrzeżenie w dwóch miejscach.

### A6a. Skończone zliczanie istnieje wyłącznie przy dyskretności [P]

**Wartość.** Entropia splątania bloku L, swobodne fermiony (c=1): S rośnie jak $(c/3)\ln L$, zmierzone nachylenie **0,3334** wobec 1/3. Warunki: L = 8…512.
**Kontrola.** Nachylenie **musiało** dać c/3 — wypisane przed rachunkiem, przeszło.
**Znaczenie.** S rośnie **bez granicy**. Zdejmij obcięcie — rozbiega.

Algebry C\* i GPT **wpisują normalizację w aksjomat**. Gleason: dla wymiaru ≥3 każda miara na kracie projekcji ma postać $\mathrm{Tr}(\rho P)$. Lokalne algebry w QFT są **typu III₁ i nie mają śladu w ogóle** — macierz gęstości nie istnieje. Iloczyn skrzyżowany z obserwatorem przeprowadza III₁ → II.

Trzy rzeczy są jedną: **dyskretność, istnienie śladu, możliwość normalizacji.**

> **Uzupełnienie v3.2 [L].** To jest ta sama przeszkoda, którą R5 wymienia jako ograniczenie ramy, i jest ważniejsza, niż plik ją traktował. Reeh–Schlieder: próżnia jest cykliczna i separująca dla algebry **każdego** obszaru — obserwator o ograniczonym obszarze i nieograniczonych zasobach może dosięgnąć całej przestrzeni Hilberta. Tomita–Takesaki daje z takiego stanu kanoniczny **przepływ modularny**, wyprowadzony, nie wkładany. Dla klina jest to pchnięcie (Bisognano–Wichmann), dla kieszeni konforemnej znany jawnie.
>
> **Konforemne pole Killinga kieszeni, znikające w obu wierzchołkach — to jest przepływ modularny.** Konstrukcja Jacobsona (A11) jest teorią modularną zastosowaną do diamentu.

---

## A7. Dekoherencja przy częściowym otoczeniu [P]

**Wartość.** Spójność $\sim(2/3)^k$, k = liczba **niedostępnych** elementów otoczenia. Dopasowanie $\exp(-0{,}4052k)$, czyli 0,6668 na element. Warunki: 400 losowań, N=40, k = 0…40.
**Kontrola.** Analityczne $\langle|\langle e_1|e_0\rangle|\rangle$ dla losowych kubitów = 2/3. Zgodność do 0,0001.
**Skala.** Przy k=40 zostaje 6,5×10⁻⁸. **Kilkadziesiąt niedostępnych elementów wystarcza.**
**Co by obaliło.** Degradacja potęgowa zamiast wykładniczej; czynnik różny od 2/3.

**Rozróżnienie jakościowe.** Otoczenie **niedostępne ale znane co do wymiaru** → ślad, stan klasyczny, prawdopodobieństwa normalizują się. Otoczenie **nie w relacji w ogóle** → nie dostajesz złej liczby, nie dostajesz obiektu. Przeżywają **stosunki**.

> **Powiązanie v3.2 [L].** To jest otoczenie „superpozycja" z tabeli R3, a wielkością nazwaną jest tam **redundancja kwantowego darwinizmu** $R_\delta=1/f_\delta$, gdzie $f_\delta$ to rozmiar fragmentu niosącego wszystko poza δ informacji o stanach wskaźnikowych. A7 mierzy degradację; redundancja mierzy stosunek otoczenia do układu — i ma **wewnętrzne cięcie przez plateau**. To jest dokładnie ta wielkość, której C2 szukało.

---

## A8. Chwila zero [H]

**Pytanie o chwilę zero nie prowadzi wstecz.** Prowadzi na drugą stronę tej samej relacji, którą już zajmujemy wobec dzisiejszych zdarzeń Ø. Nie jesteśmy „wcześniej" — jesteśmy OBOK.

Jeśli zdarzenia Ø są tego samego typu, to nie było przejściem z niczego.

**Przedmiotem jest stosunek, nie wielkość.**

Domysł [H][?]: nasza chwila zero miała otoczenie **częściowe**, tak samo jak zdarzenia Ø „na froncie".

> **POPRAWKA nr 4 (użytkownik, rozmowa 3): otoczenie mierzone niespójnie.** Raz w elementach przestrzennych (623), raz w parach (10⁷⁷), raz w udziale pola (0,0102%). **Rozstrzygnięte w v3.2 — patrz C2.**

> **Osobna awaria spójności (użytkownik, rozmowa 3).** „Zerowe otoczenie chwili zero" zapisane jako ustalenie piętnaście minut po tym, jak własny estymator pokazał, że k=1 nie odróżnia się od k=3. **Rachunek nie chroni przed złym odczytaniem własnego rachunku.**

> **Uzupełnienie v3.2 — patrz §R2.** Rozmowa 3 ma tu ostrzejszą postać, której w v3.1 nie było: dostęp prowadzi na drugą stronę relacji, **my jesteśmy otoczeniem** dzisiejszego zdarzenia Ø, a pytanie zostało przeformułowane na „jaki jest stosunek otoczenia do Ø" — czyli na C2.

> **Do wpisania jako [H][?], pole „co by obaliło" puste** (z dokumentu ramowego, nie policzone):
> - **inflacja jako różnica otoczenia** między chwilą zero a 2D/nieoznaczonością;
> - osobliwość informacyjna z dołożeniem Hawkinga.
>
> Pierwsza jest hipotezą o otoczeniu, czyli dokładnie tym, czego dotyczy C2.

---

## A9. Niezmienniki zmierzone w v3.2 — NOWA SEKCJA

Cztery wielkości policzone w rozmowie 4. Wszystkie na sprinklingu do diamentu, czyli dalej **n=1** w sensie §R1.

### A9a. f jest niezmiennikiem tylko porządków rozmaitościowych [P][A]

**Wartość.** Przy wyrównanym obciążeniu (SIS-20000, 3 losowania):

| n | 80 | 160 | 320 |
|---|---|---|---|
| f, sprinkling d=4 | 0,642 | 0,659 | 0,654 |
| f, Kleitman–Rothschild | 0,563 | 0,610 | 0,650 |

Sprinkling jest **płaski w n**. KR **pełznie i nie ma wartości granicznej**.

Ostrzej, bez pośrednictwa $d_{MM}$: sprinkling o ułamku uporządkowania 0,377 (tyle co KR) ma f≈0,455; KR ma 0,645. **Przy identycznej liczbie par uporządkowanych KR zapomina o 43% więcej.** Para (ułamek, f) rozdziela to, czego sam ułamek nie rozdziela.

**Kontrola wypisana przed rachunkiem i NIEPRZESZŁA (ważne):** asystent przewidział, że KR ma „prawie wszystkie pary przestrzenne", więc f > 0,76. To było **złe na kartce**: KR ma ułamek uporządkowania **3/8 = 0,375**, czyli jest bardziej uporządkowany niż sprinkling d=3 i d=4. Poprawiona kontrola przed rachunkiem: jeśli KR leży na krzywej sprinklingowej, $(1-f)d$ ma wyjść 1,24–1,28. **Wyszło 0,841. Nie leży.**

**Co by obaliło.** f(KR) zbieżne do wartości granicznej przy większym n; albo KR lądujący na krzywej sprinklingowej.

**Konsekwencja dla ramy:** transport między otoczeniami wymaga nie wspólnej miary otoczenia, lecz **wspólnej niezależności od n**. KR nie odpada dlatego, że ma inną liczbę — odpada dlatego, że **nie ma liczby**.

> **POPRAWKA nr 15 (asystent, v3.2, po sprawdzeniu literatury) — perkolacja.** dotyczy zdania z **roboczej wersji v3.2**, które do pliku nie weszło: „rozdzielenie jest stopniowalne, nie binarne — perkolacja p=0,02 siedzi blisko krzywej". Zachowane jako ostrzeżenie: **to był znany fałszywy alarm, nie stopniowalność.**
>
> Glaser i Surya wzięli dokładnie te parametry perkolacji, dla których Ahmed i Rideout twierdzili rozmaitościowość (Myrheim–Meyer d≈3 albo 4), i stwierdzili, że **nie przechodzą testu liczebności interwałów** dla żadnego d. Wskaźniki makroskopowe mówią „rozmaitościowa", mikroskopowy mówi „nie".
>
> $(1-f)\cdot d$ jest wskaźnikiem **makroskopowym** i dzieli tę słabość. Potwierdzone własnym rachunkiem: perkolacja ma maksimum $N_m$ przy **m=2–3**, nie przy m=0. Płasko nierozmaitościowa, bez gradacji.

### A9b. Walidacja generatorów wobec opublikowanych sygnatur [P][L]

| struktura | $N_0$ | $N_{1..6}$ | maksimum |
|---|---|---|---|
| sprinkling d=2, d=4 | duże | malejące | **m=0** |
| Kleitman–Rothschild, n=1000 | 124 821 | **0** | m=0, ale bez interwałów |
| perkolacja p=0,005…0,03 | — | — | **m=2–3** |

Zgadza się z opisem Glasera i Suryi: KR ma dużo linków, ale prawie żadnych interwałów dwu- i trzyelementowych; perkolacja ma maksimum przy m>0 w przeciwieństwie do płaskiej czasoprzestrzeni. Zmierzone $N_m/N_0$ leżą **poniżej** granicy asymptotycznej i zbliżają się powoli — zgodnie z ich uwagą, że zbieżność jest wielomianowa i granicy nie da się sprawdzić numerycznie.

**Kontrola przeszła: generatory odtwarzają cudze wyniki.**

### A9c. Podział konforemny — zmierzony [P][A]

**Odkształcenie konforemne** = zmiana gęstości sprinklingu przy ustalonym n i niezmienionych stożkach. Parametr λ, waga $1+\lambda h$; $h$ promieniowe (parzyste względem $t\to1-t$) w teście, czasowe (nieparzyste) w kontroli.

**Kontrola.** Dla odkształcenia nieparzystego $\log e(\lambda)=\log e(-\lambda)$ **dokładnie**, bo $e(P^*)=e(P)$. Współczynnik liniowy musi być zerem. Zmierzono **−0,13 ± 2,5**. ✔

**Wynik 1 — rodzina objętości.** Dla odkształcenia parzystego współczynnik liniowy $\log e(C)$ wynosi **+44,20 ± 2,5**, czyli **18σ**. $\log e(C)$ reaguje na czynnik konforemny.

**Wynik 2 — rodzina stożka.** Próg $k^*$ (A9d) pod tym samym odkształceniem:

| d | λ | k=1 | k=2 | k=3 | k=4 |
|---|---|---|---|---|---|
| 2 | −0,9 / 0 / +0,9 | +0,291 / +0,292 / +0,143 | **−0,057 / −0,009 / +0,009** | | |
| 3 | −0,9 / 0 / +0,9 | +0,531 / +0,515 / +0,497 | +0,205 / +0,170 / +0,186 | **−0,072 / −0,114 / +0,033** | |
| 4 | −0,9 / 0 / +0,9 | +0,641 / +0,676 / +0,661 | +0,399 / +0,389 / +0,462 | +0,059 / +0,063 / +0,118 | **−0,049 / +0,003 / +0,048** |

**Próg stoi na d przy każdym λ.** Wartości $|klasa|$ przy k=1 zmieniają się między skrajnymi λ 2,68× (d=2), 1,70× (d=3), 1,60× (d=4) — **wartości płyną, próg nie**.

**To jest kryterium sortujące z §R4, zmierzone po obu stronach.** Jedna wielkość reaguje 18σ tam, gdzie druga nie drga.

**Czego to NIE pokazuje.** Odkształcenie gęstości jest z konstrukcji konforemnie płaskie. Wynik mówi, że $k^*$ **ignoruje czynnik konforemny** — nie mówi, że widzi cokolwiek poza d.

### A9d. $k^*=d$ — próg zamiast wykładnika [P][A]

**Konstrukcja.** Obserwator = łańcuch („linia świata"). Sygnatura elementu x względem łańcucha = liczba jego elementów w przeszłości x (pozycja cięcia). To jest dyskretna wersja **współrzędnych emisyjnych**: cztery przyszłe stożki świetlne przecinają się generycznie w jednym zdarzeniu, i tak działa relatywistyczny system pozycyjny. Trzy tory wyznaczają zdarzenie z dokładnością do jednoparametrowej rodziny.

**Wartość.** Wykładnik wzrostu $|klasa|\sim n^\beta$ wyłącza się dokładnie przy k=d: dwa tory w d=2, trzy w d=3, cztery w d=4 (tablica w A9c).

**Kontrole.** Antyłańcuch → zero informacji przy każdym rozmiarze fragmentu. Łańcuch (d=1) → γ = 0,980 wobec 1/d = 1. Kleitman–Rothschild → $m^*$ idzie 19→29 przy szesnastokrotnym wzroście n, czyli $\sim\log n$, a nie $n^{1/d}$ — **trzecia niezależna obserwabla dająca ten sam podział rozmaitościowe / nierozmaitościowe**.

**Dlaczego to jedyny estymator trafiający w d=4.** Cztery policzone w tej sesji:

| estymator | odczyt przy d=4 |
|---|---|
| Myrheim–Meyer | 4,10 |
| β (wyostrzanie rankingu, A9e) | −0,313 → d≈3,2 |
| γ (kolano nieodróżnialności, A9e) | 0,345 → d≈2,9 |
| **$k^*$ (tory)** | **4, dokładnie** |

Tamte trzy **dopasowują wykładnik**, ten odczytuje **przejście**. Przejście jest liczbą całkowitą i nie da się go przesunąć o kilkanaście procent.

> **POPRAWKA nr 16 (asystent, v3.2) — L nie jest parametrem wolnym, ale związanie samego skalowania nie wystarcza.**
>
> Pierwsza wersja rachunku dawała L (liczbę elementów na tor) z ręki. Przy L=60 **dwa tory wystarczały w każdym wymiarze** — ale to było czyste przegródkowanie: 61² komórek na 121 kandydatów. **Linia świata w zbiorze przyczynowym jest zrobiona z elementów tego samego zbioru, więc nie może być próbkowana gęściej niż skala dyskretności:** $L\sim n^{1/d}$.
>
> Po związaniu skalowania test zaczął mierzyć geometrię. **Ale stała przy L została na 1 i nie była sprawdzana** — i to ona niosła wynik w rachunku fali pp (§D). Poprawka przeniosła błąd o piętro: skalowanie dobre, przedczynnik wolny.
>
> **Reguła: związać skalowanie to za mało. Każdy parametr, który sam sobie ustawiłeś, trzeba przeskanować.**

**Trzy fikołki w tym rachunku, wszystkie własne:** (1) nadajniki na stałym promieniu w losowych kierunkach — w d=2 kierunki są dwa, więc się nakładały i k=1,2,3 dały identyczny wynik; poprawione na wierzchołki sympleksu; (2) tory pokrywały tylko środek obszaru, więc elementy spoza zasięgu miały jednakową zdegenerowaną sygnaturę i dominowały średnią geometryczną; poprawione przez ograniczenie do odbierających z każdego toru; (3) L jako parametr wolny, wyżej.

### A9e. β i γ — ta sama liczba czytana dwa razy [P][A]

**β** = wykładnik wyostrzania rankingu przestrzennego: dla k najbardziej nakładających się nieporównywalnych partnerów selektywność (średnie $|\Delta x|$ w N podzielone przez średnie po wszystkich nieporównywalnych) poprawia się jak $n^\beta$. **Niezależny od k**: rozrzut po k rozciągniętym dziesięciokrotnie (3→30) wynosi 0,002–0,011.

**γ** = wykładnik położenia kolana krzywej nieodróżnialności: $m^*\sim n^\gamma$, gdzie $m^*$ to rozmiar fragmentu, przy którym $|klasa|$ siada na 1.

| d | β | γ | suma | −1/d, +1/d |
|---|---|---|---|---|
| 2 | −0,506 | +0,509 | +0,003 | ∓0,500 |
| 3 | −0,374 | +0,359 | −0,015 | ∓0,333 |
| 4 | −0,313 | +0,345 | +0,032 | ∓0,250 |

$\beta+\gamma\approx0$. Dwie obserwable, dwie różne metody, osobne przebiegi — obie mierzą skalę dyskretności $n^{-1/d}$ i obie odchylają się od $1/d$ tak samo przy rosnącym d. **Artefakt jednego estymatora nie powtórzyłby się w drugim.** To wzmacnia diagnozę skończonego rozmiaru, a nie wynik.

**Co by obaliło.** β zależne od k. Albo $\beta+\gamma$ istotnie różne od zera.

**Status prawa $\beta=-1/d$:** trafia w d=2 (−0,506 wobec −0,500), chybia o 12% przy d=3 i 25% przy d=4. Diagnoza: przy n=1600 w d=4 przez diament mieści się $n^{1/4}=6{,}3$ długości dyskretności, a przy d=2 mieści się 40.

> **POPRAWKA nr 18 (asystent, v3.2) — d=2 nie nadaje się na przypadek walidujący.**
>
> Przez dwie sesje d=2 było traktowane jako wzorcowe, bo tam prawa trafiały. Tłumaczono to statystyką. To było prawdziwe, ale niepełne: **d=2 jest zdegenerowane strukturalnie w co najmniej trzech opublikowanych sensach naraz.**
>
> 1. Wymiar porządkowy równa się wymiarowi Minkowskiego **tylko** przy d=2 (Meyer 1993).
> 2. Automorfizmy przyczynowe są tam odwzorowaniami konforemnymi; dla $n\ge3$ twierdzenie Zeemana czyni je sztywnymi.
> 3. U Glasera–Suryi $S^2_m=1$ niezależnie od m — ich odcisk degeneruje się akurat w d=2.
>
> **Każde prawo postaci $a+b/d$ albo $a+bd$ przechodzące przez d=2 i chybiające przy d=4 trzeba czytać ostrożniej**: może trafiać w d=2 z powodu degeneracji, a nie z powodu prawa. Dotyczy to $\beta=-1/d$ i $\gamma=+1/d$ wprost.

### A9f. Obserwatorzy wybrani z samego porządku [P][A] — bez współrzędnych

Pierwszy rachunek w projekcie, w którym **nie ma ani jednej współrzędnej**: łańcuchy wybrane z porządku (najdłuższe ścieżki), sygnatura z porządku, klasy z porządku.

Ilorazy kolejnych k — o ile każdy następny obserwator poprawia rozdzielczość, n=4000:

| struktura | 1→2 | 2→3 | 3→4 | 4→5 | 5→6 |
|---|---|---|---|---|---|
| sprinkling d=2 | 1,76 | 1,26 | 1,08 | 1,02 | **1,01** |
| sprinkling d=3 | 6,34 | 2,41 | 1,48 | 1,27 | **1,12** |
| sprinkling d=4 | 3,82 | 2,93 | 2,05 | 1,52 | **1,35** |
| **Kleitman–Rothschild** | 2,12 | 1,94 | 1,83 | 1,77 | **1,72** |

Sprinklingi **nasycają się**. KR **nie nasyca się nigdy** — każdy następny obserwator płaci tyle samo.

**Znaczenie [O].** Struktura, która się nasyca, ma coś, co można wyczerpać — i to „coś" nazywa się potem wymiarem. Struktura, która się nie nasyca, tego nie ma. **Wymiar jest tu wynikiem nasycenia, nie założeniem.**

**Czego to NIE pokazuje.** Rozstawienie obserwatorów z porządku wyszło **gorsze** niż ręczne: przy d=4 i k=4 zostaje $|klasa|\approx23$, podczas gdy sympleks we współrzędnych daje ~3. Dwa kryteria wyboru („najdłuższy łańcuch", „zasiew z antyłańcucha") są obie gorsze od ręcznego. **Pytanie, czy trzy dobrze wybrane tory dorównują czterem ustawionym ręcznie, pozostaje otwarte** — i jest to brak metody wyboru, nie wynik.

Następny krok tam: wybór obserwatorów przez samą optymalizację (hill-climbing po zbiorze łańcuchów, minimalizując średni $\log|klasa|$), bez kryterium narzuconego z góry.

---

## A10. Entropia kieszeni — stan SJ [P][L] — NOWA SEKCJA

**Stan Sorkina–Johnstona jest próżnią wyprowadzoną z samego porządku.** Nie wkłada się go: bierze się retardowaną funkcję Greena (w d=2 dla pola bezmasowego $K_R=\tfrac12 C$, gdzie C to macierz przyczynowa), stąd $i\Delta=i(K_R-K_R^{\mathsf T})$, hermitowską, i stan jako **dodatnią część jej widma**. Jest kowariantnie i jednoznacznie określony w każdej czasoprzestrzeni globalnie hiperbolicznej.

To jest **punkt 5 z tabeli R3 — próżnia jako porządek referencyjny — policzony.**

**Kontrole, które przeszły.** $i\Delta$ hermitowska dokładnie. Widmo symetryczne względem zera (197/197 przy n=400). Warunek SJ $W-\bar W=i\Delta$ do $10^{-14}$. W dodatnio półokreślona. **Niezmienniczość względem odwrócenia czasu: różnica dokładnie zero.**

**Kontrola nieplanowana, która przeszła.** Widmo uogólnionego zagadnienia $Wv=i\lambda\Delta v$ chodzi **parami $\lambda$ i $1-\lambda$** (−15,2507 z +16,2507; −7,3948 z +8,3948; …), żadna nie wpada do (0,1). Dzięki temu $\sum\lambda\ln|\lambda|$ zwija się do standardowej entropii gaussowskiej $\sum_{\lambda>1}[\lambda\ln\lambda-(\lambda-1)\ln(\lambda-1)]$. Parowanie **przeżywa obcięcie dokładnie** (błąd $10^{-15}$), więc wzór jest poprawny także w wersji obciętej.

**Te $\lambda$ są widmem modularnym** — czyli „hierarchią korelacji" z punktu 4 listy otoczeń.

**Wartość.** Skalowanie z N dla poddiamentu: wykładnik **+1,057**. **Prawo objętościowe.**

> **To jest znany wynik, nie usterka implementacji [L].** Entropia na zbiorze przyczynowym daje prawo objętościowe zamiast powierzchniowego; do odzyskania powierzchniowego potrzebne jest obcięcie widma.
>
> **I ma opublikowaną diagnozę, znalezioną w v3.2:** stan SJ **nie jest hadamardowski na brzegu kieszeni** (praca z 2024 o własności hadamardowskiej w czterowymiarowym diamencie), a osobliwe cechy entropii splątania w teorii zbiorów przyczynowych są tam badane **jako możliwy skutek niehadamardowości**. Poprawką jest **zmiękczony stan SJ**.

**Trzy próby obcięcia, wszystkie nieudane [P]:**

| schemat | wynik |
|---|---|
| ułamek modów globalnych | wykładnik 1,057 → 0,948 → 1,078, potem entropia zapada do zera |
| ułamek modów podobszaru | 1,07 → 0,65, nigdy 0 |
| stała liczba modów | S maleje z N **i z rozmiarem obszaru** (−1,08 względem $\log a$) — niefizyczne |

**Diagnoza [P].** Przy n=262144 entropia w funkcji liczby zachowanych modów jest **liniowa w k**: 0,089 na mod przy k=8 i 0,081 przy k=48. Każdy zachowany mod wnosi tyle samo. Stąd **żadne obcięcie liczące mody nie może dać prawa powierzchniowego**: przy liczbie modów skalującej się z obszarem wychodzi objętość, a przy stałej — entropia nie rośnie z obszarem. Opublikowana recepta musi wybierać mody przez porównanie z widmem kontinuum, a nie przez ich liczbę.

**Twarde zatrzymanie, nie brak cierpliwości.** Bez analitycznego widma Pauliego–Jordana nie ma tu dalszej drogi.

---

## A11. Koszt, sztywność, masa [P][T][A] — NOWA SEKCJA

### A11a. Koszt pojedynczej relacji [T]

Z tożsamości $e(P)=e(P{+}x{<}y)+e(P{+}y{<}x)$ (każde rozszerzenie liniowe ustawia x i y w jednej z dwóch kolejności):

$$\boxed{\;\mathcal{C}(x{<}y)=-\log\Pr[\,x\text{ przed }y\text{ w losowym rozszerzeniu liniowym}\,]\;}$$

Koszt narzucenia relacji to minus logarytm z tego, jak prawdopodobna **już była**. Zero, jeśli porządek ją wymuszał; $\log2$ przy parze maksymalnie nierozstrzygniętej. Na marginesie: $\Pr[x\text{ przed }y]$ dla par nieporównywalnych jest przedmiotem hipotezy 1/3–2/3, więc ma własną literaturę.

### A11b. D jest addytywne tożsamościowo [T]

$$D(C)=\log n!-\log e(C)$$

Dla rozłącznej sumy $e(A\sqcup B)=e(A)e(B)\binom{n_A+n_B}{n_A}$, więc **$\log e(C)$ nie jest addytywne** (człon przeplotu $\approx n\log2$ dla równych połówek). Ale w D czynnik przeplotu **znosi się dokładnie**:

$$\log(n_A{+}n_B)!-\log e(A\sqcup B)=\big[\log n_A!-\log e(A)\big]+\big[\log n_B!-\log e(B)\big]$$

**Kontrola numeryczna, dokładne zliczanie, n=8+8:** błąd addytywności $10^{-15}$ w czterech układach, przy czym $\log e$ chybia o 7–9 natów w tych samych.

| struktura, n=320 | $D/(n\log n)$ |
|---|---|
| antyłańcuch | 0,0000 |
| sprinkling d=6 | 0,070 |
| sprinkling d=5 | 0,116 |
| **sprinkling d=4** | **0,177** |
| Kleitman–Rothschild | 0,179 |
| sprinkling d=3 | 0,271 |
| sprinkling d=2 | 0,436 |
| łańcuch | 0,8287 (maksimum) |

**Dlaczego D, a nie $\log e$.** D i f niosą tę samą informację (są związane afinicznie przy ustalonym n). Zmienia się **prawo składania**. Dla wielkości mającej być masą to jest całość, bo masa jest zdefiniowana przez to, jak się składa. Warunek addytywności wzięty z Gallego Torromé, Isidro, Fernández de Córdoba (Found. Phys. 53, 52, 2023), gdzie $T_{a\sqcup b}=T_aT_b$ daje masy dodające się.

**Koszt skumulowany a krańcowy — rozróżnienie, które trzeba trzymać.** Skumulowany ($D$) **rośnie**: przy n=320, d=4 wynosi $0{,}175\cdot n\log n$. Krańcowy ($\mathcal{C}$) **maleje**, bo im bardziej porządek jest określony, tym bliżej jedynki jest prawdopodobieństwo. Kolejne interakcje są **coraz tańsze**, nie coraz droższe. Teza „struktura kosztuje z każdą kolejną interakcją" jest prawdziwa dla skumulowanego i fałszywa dla krańcowego.

### A11c. Koszt sprzężenia [T][P]

$$\text{nadwyżka}(A,B)=D(A\!\leftrightarrow\!B)-D(A)-D(B)=\log e(A\sqcup B)-\log e(A\!\leftrightarrow\!B)$$

**Minus logarytm ułamka swobodnych przepleceń, które sprzężenie przeżyły.** Ta sama postać co $\mathcal{C}$, dla całego sprzężenia naraz.

**Obie granice wypisane przed rachunkiem i trafione co do szóstego miejsca** (n=8+8): zero relacji → nadwyżka 0,000000; pełne sprzężenie → $\log\binom{16}{8}=9{,}462654$.

**Koszt na relację zależy od tego, co się sprzęga:**

| co sprzęgamy | domknięte relacje | nadwyżka | na relację |
|---|---|---|---|
| antyłańcuch × antyłańcuch | 8 | 4,175 | **0,522** |
| sprinkling d=2 × sprinkling d=2 | 41 | 6,596 | 0,161 |
| łańcuch × łańcuch | 40 | 4,357 | **0,109** |

Pięciokrotna różnica. Antyłańcuch jest swobodny, więc każda relacja wycina dużo; łańcuch jest sztywny, więc relacje wiążące są wzajemnie nadmiarowe przez przechodniość. **To jest właściwy kształt dla kosztu wiązania** — wielkość zależna wyłącznie od liczby wiązań byłaby podejrzana.

**Kontrola, która NIE przeszła (ważna):** wcześniejsza obserwacja, że nadwyżka jest liniowa w liczbie domkniętych relacji ze stałą $\log\binom{n}{n_A}/(n_An_B)$, wychodziła tylko dla jednej pary (sprinkling d=2). Po zmianie struktur $R^2=0{,}64$, reszty do 2,8. **Nie jest to prawo.**

### A11d. Masa — czego nie ma [L]

**W teorii zbiorów przyczynowych masa nie jest wyprowadzona.** D'Alembertian służy do zapisania równania ruchu dla pola **bezmasowego**; masa dokłada się jako człon $m^2\varphi$.

**Działanie BDG jest funkcją kosztu konfiguracji** (A2), i jest tym, co tłumi porządki KR w sumie po historiach. KR są **entropowo dominujące** — gdyby liczyła się tylko liczba konfiguracji, całka byłaby przez nie zdominowana. **Konkurencja entropii z działaniem jest głównym otwartym problemem tej dziedziny** (Loomis i Carlip; Carlip–Carlip–Surya 2024; Mathur–Singh–Surya). Nasz wynik A9a jest z tej samej strony sporu, mierzony innymi obserwablami.

**Czego u nas nie ma, a co byłoby czymś innym niż działanie:** działanie jest **pierwszą wariacją** — kosztem bycia w stanie. Pytanie o opór przeciw zmianie to **sztywność**, czyli druga wariacja. Nie widziałem jej policzonej i my jej nie policzyliśmy.

**Zastrzeżenie do $m\sim\log(\text{złożoność})$ [L][?].** W pracy Gallego Torromégo równania (3.1) i (4.1) są **postulowane**, nie wyprowadzone; nie ma tam liczby, która mogłaby wyjść inaczej. Po kryterium z A0 to jest rama, nie rachunek. **Ale jest o jedno podstawienie od testowalności:** z $m=\lambda(N-N_{min})$ i wspólnego $N_{min}$ dla wszystkich bezmasowych wynika, że **stosunki mas muszą być wymierne o wspólnym mianowniku** — a to jest sprawdzalne na tablicy mas.

**Rozbieżność skalowania, nierozstrzygnięta.** Ich Model 2 daje masę liniową w liczbie stopni swobody; nasze D dla spójnego sprinklingu rośnie jak $n\log n$, więc $D/n$ rośnie jak $\log n$. Albo n nie jest ich N, albo jedna z dwóch postaci jest zła.

### A11e. Równowaga splątania — dlaczego nasz test nie mógł zadziałać [L][A]

**Jacobson (PRL 2016):** entropia splątania w małych kieszeniach przyczynowych jest maksymalna **przy ustalonej objętości** w lokalnie maksymalnie symetrycznej próżni; półklasyczne równanie Einsteina zachodzi dla wariacji pierwszego rzędu **wtedy i tylko wtedy**, gdy ta entropia jest stacjonarna. Wzrost entropii materii musi być skompensowany spadkiem entropii geometrii, a żądanie znoszenia się daje równanie Einsteina.

**Cztery dopasowania do tego, co robimy:** obiekt to mała kieszeń przyczynowa; więz „przy ustalonej objętości" mamy za darmo, bo objętość **jest** licznością; próżnia to punkt stacjonarny — **stąd bierze się jałowość płaskiego sprinklingu** (R5); a pierwsza wariacja znika z założenia, więc zawartość siedzi w **drugiej**, czyli w sztywności (A11d).

Piąte, mniejsze: konforemne pole Killinga kieszeni **znika w obu wierzchołkach i na brzegu kuli** — czyli dokładnie w tych punktach, które we wszystkich naszych rachunkach kasował `bulk_mask`.

> **POPRAWKA nr 17 (asystent, v3.2) — nasz test odkształceniowy nie mógł rozstrzygnąć.**
>
> Zmierzono: $\log e(C)$ niestacjonarne pod odkształceniem promieniowym (18σ); entropia SJ surowa niestacjonarna pod tym samym (7,0σ, wrażliwość 4,21% ± 0,61% na jednostkę λ wobec 6,40% ± 0,36% dla $\log e$). Kontrola nieparzysta przeszła w obu (0,2σ i −0,13).
>
> **Ale ten test mierzy jeden z dwóch członów, które mają się znosić.** Odkształcono geometrię przy polu w stanie SJ, czyli w próżni **dla tej geometrii** — a odkształcenie promieniowe nie daje przestrzeni maksymalnie symetrycznej, więc Jacobson **sam przewiduje tam niestacjonarność**. Drugiego członu nie włożono.
>
> **Dobrze wykonany rachunek nie na tym obiekcie.** Ten sam gatunek co L jako parametr wolny (A9d).
>
> **Co zostaje uczciwego:** $\log e(C)$ i entropia SJ reagują na to samo odkształcenie **podobnie** (6,4% wobec 4,2%). Na jedynym teście, na którym da się je porównać, zachowują się tak samo — więc teza, że nasza entropia kombinatoryczna jest niewłaściwym zastępnikiem, jest słabsza, niż wyglądała.
>
> **Właściwy test** musi prowadzić **wewnątrz rodziny maksymalnie symetrycznej** (płaska ↔ de Sitter, obie są równowagami). Człon liniowy jest tam chroniony symetrią, więc badać trzeba kwadratowy. Do tego potrzeba obcięcia dającego prawo powierzchniowe (A10) i kilkakrotnie większej statystyki. Nie jest to kwestia jednego przebiegu.

---

# §B — CZĘŚCIOWO

## B1. ħ / masa

Droga istnieje: szachownica Feynmana daje wagę $(im\varepsilon)$ za zwrot, więc bezwymiarowym parametrem jest $m\varepsilon$. Model hop-stop Johnstona robi to na zbiorze przyczynowym. **W 2D zrobione, w 4D nie.**

> **Dopisek v3.3 [L].** Hoyle–Narlikar (1974, streszczone u Johnstona §3.14.3): propagator bezmasowy = ½(opóźniony + przyspieszony), cząstka „przeskakuje” w przyszły albo przeszły stożek — ten sam zygzak. Propagator Feynmana = swobodny + „odpowiedź wszechświata”, pod warunkiem znajomości masy wszędzie.
>
> **Kolejność pojęć przed masą [H]:** porządek i liczność → czas, objętość, przestrzenność → relacja t=0 → **pole** (brak) → próżnia → działanie → energia → ładunek, spin → elektron, kwark, gluon → masa. Pole jest najbardziej krytyczne. Energia wg Noether = to, co niezmienione przy przesunięciu wzdłuż porządku — sprinkling nie ma ciągłych symetrii, więc najwyżej zachowanie średnie [A][?].

Rendering liczbowy (elektron: 1 zwrot na 2,39×10²² elementów) **jest przepisaniem $m/m_P$, nie wynikiem.**

Bilans przeliczników: c ✓ (jako przelicznik, nie wielkość mierzona — A2, C4a.13), G ✓, $k_B$ ✓, e ✓, **ħ częściowo**. α nie należy do tej listy (A2).

> **Uzupełnienie v3.2.** Masa nie jest wyprowadzona w tej dziedzinie w ogóle (A11d), więc „ħ częściowo" jest częścią większego braku, nie osobnym punktem.

## B2. Retrospekcja

**Działa na rozkładach, nie na epizodach.** [A] — **pełniejsza wersja w §R2, z rozmowy 3.**

**Co się udało.** Reguła wzrostu odczytana wstecz: błąd 1,7–15,7%. Kolejność powstawania: korelacja 0,87–0,96 — **warunki: n=30, graf o wagach niesymetrycznych (ratio 0,3), rozkład Hodge'a, pięć losowań** (rozmowa 2).

**Kontrola negatywna, którą trzeba trzymać razem z wynikiem:** sam wysoki udział gradientu (84%) NIE jest sygnaturą wzrostu — czysto losowa niesymetryczna macierz daje te same 83,6%.

**Chwila zero nie ma wielokrotnego świadectwa.** Estymata k, q=0,005: k=1 → 1,26±0,63; k=3 → 3,42±1,06; k=10 → 10,47±1,90. Przy q=0,02 systematycznie zawyża. **Rozrzut przekracza odstęp między k=1 a k=3.** Nie z powodu słabego estymatora — więcej świadectwa nie ma.

**Ślad k w całej strukturze** [P]: w₁ = **1,92**, w₂ = 1,26, w₀ = 0,67, L = 0,48, r = **0,01**. **Wygasa w trzech warstwach.** Obserwable globalne są zerowe — dlatego CMB nie może nieść k.

**Droga otwarta.** Późne zdarzenia Ø są tego samego typu, więc dają wielokrotne świadectwo o tym, **jak wygląda chwila zero w ogóle**. Zastrzeżenie: pierwsza może nie należeć do rodziny.

> **USUNIĘTE z v2 i nadal usunięte.** Zdanie „w d=4 struktura zapomina 77% własnej historii, stąd korelacja 0,87–0,96" — korelacja pochodzi z **innej struktury** (rozmowa 2, n=30, wagi niesymetryczne, rozkład Hodge'a). Zestawienie było **analogią zapisaną jako wynik**.

## B3. Klasa relacji jednostronnych — KLASA ODRZUCONA; sam kandydat „stacjonarność” otwarty

Trzej członkowie o różnym pochodzeniu: sfera fotonowa (geodezyjne), molekuły horyzontu (zliczanie par), sfera Hubble'a (gęstość krytyczna).

**Klasa nie może stać na jednostronności, bo dwa z trzech członów jej nie mają.** Rachunek, n=4000:

| przekrój | A→B | B→A |
|---|---|---|
| rurka czasopodobna, d=2 | 927 990 | 909 994 |
| rurka czasopodobna, d=4 | 154 912 | 165 113 |
| zbiór przeszły, d=2 | 1 971 705 | **0** |
| zbiór przeszły, d=4 | 471 873 | **0** |

Kandydat na „coś innego" (stacjonarność kierunku zerowego) jest warunkiem ciągłym. **B3 rozstrzyga się dopiero po C1 i C2.**

> **Status w v3.2.** C1 i C2 mają odpowiedzi z literatury (§C), więc B3 przestaje być zablokowane z tego powodu. Ale nikt go nie podjął ponownie i zostaje otwarte.
>
> **B3 jest próbą generalną całego programu i wyszła negatywnie.** Trzej członkowie z różnych źródeł, złożeni w klasę na podstawie podobieństwa, policzeni, odpowiedź „nie". Ośmioelementowy łańcuch z §R1 ma ten sam kształt. To nie przesądza jego losu, ale pokazuje, jak wygląda test i że wynik może być negatywny.

## B4. Liczność jako element struktury [H]

Teza zmienia A6. Jeśli liczność jest **wewnątrz** struktury, to rozdzielenie „stosunki vs skala" jest artefaktem opisu. Malament daje metrykę z dokł. do czynnika konforemnego, bo bierze **sam porządek** — czyli niepełny opis.

**Pierwszy kandydat na test:** prawo $k-(k-1)d$ (A3a) — jedyna zmierzona wielkość, w której kombinatoryka i porządek występują nierozdzielnie.

> **Drugi kandydat WYCOFANY.** v3.1 wskazywało A4c. Po poprawce nr 12 $(1-f)d$ jest funkcją samego d, więc nie wiąże liczności z wymiarem — jest przekodowaniem wymiaru. **Odpada jako test B4.**
>
> **Kandydat wchodzący w jego miejsce:** para (ułamek uporządkowania, f), która **rozdziela KR od sprinklingów** (A9a) — bo tam f przestaje być funkcją ułamka, więc liczność niesie coś, czego porządek sam nie niesie. To jest bliżej tezy B4 niż A4c kiedykolwiek było.

---

# §C — CIĘCIE I OTOCZENIE

> C1, C2 i C3 są **zamknięte**. Żywe zostają C4 (plan) i C4a (wyniki).

> **ZMIANA STATUSU W v3.2.** C1 i C2 były w v3.1 opisane jako otwarte i blokujące B3. **Obie mają odpowiedzi w literaturze, starsze od tego pliku.** Rachunki asystenta w rozmowie 4 odkryły je ponownie, numerycznie, co dało kontrolę na kod i nic ponadto.

## C1. „obok" / lokalność — ODPOWIEDŹ W LITERATURZE [L]

**Nieskończona walencja jest twierdzeniem, nie artefaktem.** W nieskończonym zbiorze przyczynowym przybliżanym Minkowskim najbliższymi sąsiadami elementu są linki, a każdy element ma ich **nieskończenie wiele** — w przeszłość i w przyszłość. Graf ma nieskończoną walencję, w przeciwieństwie do innych typów dyskretności. **I to jest cecha niosąca treść niezmienniczości Lorentza**, bo z każdym zdarzeniem wiążą się niezwarte hiperbole niezmiennicze względem pchnięć. Nie jest to usterka do naprawienia.

**Rozwiązanie nie jest cięciem, tylko odciskiem** (Glaser, Surya 2013). Bierze się dowolny interwał porządku $I[x,y]$, liczy profil liczebności interwałów $N_m$ i porównuje z analitycznym $\langle N^d_m\rangle$ w granicach $\pm\sqrt N$. Zgadza się → obszar jest lokalny. Istnienie obszarów lokalnych jest **warunkiem koniecznym rozmaitościowości**, a przy okazji daje nowy estymator wymiaru, dający wynik pusty dla zbiorów nierozmaitościowych.

**Dodatkowo w literaturze:** Boguñá, Krioukov, „Measuring spatial distances in causal sets via causal overlaps", PRD 110 (2024); Eichhorn, Surya, Versteegen, „Induced spatial geometry from causal structure" (2019); Rideout, Wallden, „Spacelike distance from discrete causal order" (2009). **C1 ma nie jedną odpowiedź, tylko co najmniej trzy, z różnych lat.**

> **POPRAWKA nr 17a (asystent, v3.2) — diagnoza w v3.1 umieszczała przeszkodę w złym miejscu.**
>
> v3.1: „okno K=60 to lokalność po etykiecie, a etykieta jest niefizyczna z założenia". **Wersja bezetykietowa ma dokładnie tę samą wadę.** Zmierzono: porządek wyznacza **ranking przestrzenny** (top-k po nakładaniu przeszłości jest selektywny i poprawia się z n we wszystkich d), ale **nie wyznacza otoczenia** — cięcie (k albo próg θ) jest zawsze z zewnątrz.
>
> **Przeszkodą nie jest etykieta, tylko brak wewnętrznego cięcia.** Usunięcie etykiet nie usuwa parametru.
>
> **A wewnętrzne cięcie istnieje w innym otoczeniu:** plateau redundancji w kwantowym darwinizmie (R3). Pożyczka idzie w obie strony — literatura zbiorów przyczynowych ma odpowiedź na lokalność, literatura informacji kwantowej ma odpowiedź na cięcie.
>
> Niesprawdzone: czy w widmie nakładania jest wewnętrzna przerwa dająca cięcie bez parametru.

## C2. Miara otoczenia — ROZSTRZYGNIĘTE [L][P]

**Gotowa odpowiedź, lepsza od naszej:**

$$S^d_m=\lim_{\rho\to\infty}\frac{\langle N^d_m\rangle}{\langle N^d_0\rangle}=\frac{\Gamma(2/d+m)}{\Gamma(2/d)\,\Gamma(m+1)}$$

W wiodącym rzędzie **nie zależy od N**. Bezwymiarowy, w zamkniętej postaci, niosący d, **bez parametru**. Dokładnie to, czego szuka §R.

Skalowanie: $\langle N^d_m\rangle\sim N^{2-2/d}$ dla d>2 i $N\log N$ dla d=2.

**Nasza własna próba, słabsza, ale warta zapisania [P]:** przy stałym otoczeniu (k=30 najbliższych po nakładaniu, czyli 31 elementów) relacje **wewnętrzne** są niezależne od n (139→134 dla d=2, 41→50 dla d=3, 20→16 dla d=4 przy n=200→1600), a relacje **przecinające** rosną liniowo z n (2582→24146 dla d=2). Po kryterium n-niezależności: **wewnętrzne są dopuszczalną miarą, przecinające nie.**

**Rozwiązanie poprawki nr 4.** Trzy liczby z A8 nie są trzema miarami jednej rzeczy. **623 elementy to objętość. 10⁷⁷ par to relacje przecinające, czyli brzeg. 0,0102% pola to już bezwymiarowy ułamek.** Zarzut był słuszny, a powód jest strukturalny, nie niechlujstwo. „Elementy czy relacje" jest źle postawione, dopóki nie rozbije się relacji na wewnętrzne i przecinające.

**Ułamek uporządkowania wewnątrz otoczenia** (n=1600): 0,31 / 0,11 / 0,039 dla d=2/3/4, wobec globalnych 0,50 / 0,229 / 0,100. Stabilny w n, słabo zależny od k (dryf 10–20% między k=10 a k=100). **Wolny od n, jeszcze nie wolny od cięcia.**

## C4. Plateau redundancji z detektorem na zbiorze przyczynowym — PLAN [H][A]

**Pytanie:** czy plateau redundancji jest wewnętrznym cięciem (C1/C2)? **Ustalone przed rachunkiem [H]:** w czystej próżni SJ nie ma układu ani bazy wskaźnikowej, więc plateau zakłada cięcie, nie daje go. Plateau istnieje tylko w oknie między rozgłoszeniem a wymieszaniem (Riedel–Zurek–Zwolak 2012); próżnia jest stacjonarna (A11e). Najsilniejsza redundancja pochodzi z rozproszonego światła (Riedel–Zurek) — otoczeniem zapisującym jest rodzina stożka: **groźba błędnego koła**.

**Luka [L]:** Pilgrim (2021, detektor na zbiorze, 2D i 4D; kliknięcia na geodezyjnej, w 4D nie znikają z gęstością), SJ (próżnia), kwantowy darwinizm (plateau) istnieją osobno; nikt ich nie złożył. Alkofer–D'Odorico–Saueressig–Versteegen (PRD 94, 104055, 2016): odcisk w tempie emisji, stłumienie przy dynamicznej redukcji wymiaru. Belenchia (doktorat SISSA 2017): nielokalność modyfikuje odpowiedź detektora. Xu (2023): dekoherencja detektora UDW w kontinuum. *(Stan wiedzy: wrzesień 2026, sprawdzone pobieżnie.)* **Brak plateau u Alkofera i in. nie jest świadectwem — nie liczyli I(S:F).**

**Ustawienie:**
- d=2 (SJ z samego porządku tylko tu; wynik NIE przenosi się na rodzinę stożka w d=4 — w d=2 brak pola magnetycznego i degeneracja, poprawka nr 18)
- detektor: **oscylator harmoniczny na łańcuchu** (model Pilgrima; stan gaussowski → entropie z kowariancji jak w A10), sprzężenie g
- fragmenty: kawałki **pogrubionego antyłańcucha w PRZYSZŁOŚCI odcinka oddziaływania** (niezależne wzajemnie; zapis ma kierunek Ø → otoczenie)
- **dwa przebiegi na tych samych realizacjach:** *tło* (oscylator w stanie podstawowym) i *zapis* (oscylator przygotowany, np. ściśnięty)
- skany: grubość antyłańcucha, obcięcie SJ, gęstość (≥ dekada; niepewności z bootstrapu po realizacjach; SJ ~ N³)
- porównywać **I/S(S)**, nie surowe I — S(S) sama może zależeć od gęstości

**Kontrole przed rachunkiem:**
- g=0 → I(S:F)=0 dla każdego F
- I(∅)=0; czystość stanu na użytym obszarze sprawdzona jawnie (S(A)=S(dopełnienie przyczynowe))
- obcięcie SJ **lokalne**, nie globalne (§D)

**Zdania do upadku:**
1. Wysokość płaskiego odcinka w przebiegu zapisu: I/S(S)=1, niezależna od obcięcia SJ.
2. Położenie/wysokość przesuwa się z grubością antyłańcucha → cięcie nie jest wewnętrzne.
3. Przebieg tła daje płaski odcinek na tej samej wysokości I/S(S) co przebieg zapisu → to nie plateau z zapisu.
4. Wysokość w przebiegu zapisu skaluje się z gęstością tak samo jak w przebiegu tła → to nie plateau z zapisu.
5. W d=2 płaski odcinek tła (jeśli jest) musi maleć z gęstością (tło Pilgrima znika w granicy). Jeśli nie maleje → złe odczytanie Pilgrima albo błąd kodu.

**Otwarte przed rachunkiem [?]:**
- czy stan ściśnięty oscylatora wystarcza do plateau (literatura: darwinizm dla oscylatorów, np. 1911.07958)
- potwierdzić w źródle, że tło Pilgrima w d=2 znika z gęstością
- informacja wzajemna nie jest addytywna po źródłach — tła nie da się po prostu odjąć; tło może też samo niszczyć plateau (mieszanie)

## C4a. Etap 0 i test fragmentów — WYNIKI [P][A]

Skrypty: `etap0_integrator_wariacyjny.py`, `etap0b_fragmenty.py`. Wszędzie d=2, $G_R=C^T/2$, detektor = oscylator na najdłuższym łańcuchu, ω=6π/√2, ε=√2/M, stan wejściowy **iloczyn** $\omega_{SJ}\otimes\omega_{osc}$ (współrzędne kanoniczne, $\Gamma_{in}=\tfrac12 I_r\oplus\mathrm{diag}(1/2\omega,\omega/2)$), bez obcięcia SJ, jedna realizacja na N.

**1. Integrator.** Pierwsza wersja (krok Eulera + siła z pamięcią) łamała komutatory o ~$10^{-3}$, malejąco jak ~$\varepsilon^{2}$ (zakres ×4 — kierunek, nie wniosek); „test znaku sprzężenia” był artefaktem niespójności. **Wersja wariacyjna:** jedno liniowe działanie, $X=(1-G_0V)^{-1}X_{in}$.

| kontrola (N=300/600/1200; g=0, ±5, 20) | wynik | mogła upaść? |
|---|---|---|
| wejście zgodne z $G_0$ | ≤2·10⁻¹⁴ | tak |
| komutator = Peierls pełnej teorii | ≤2·10⁻¹⁴ | nie (tożsamość) |
| **mikroprzyczynowość, wszystkie pary przestrzenne** | ≤2·10⁻¹⁴ | **tak — kontrola negatywna (detektor odwrócony): 3,6·10⁻²** |
| S(całość)=0; S(S)=S(Sᶜ) symplektyczne | 0; 5 cyfr | nie (tożsamości) |
| g=0 → S(S)=0 | 0 | tak |

Znak g bez znaczenia (±5 identyczne). S(S)≈0,40 przy g=5, prawie stałe w N (obserwacja).

**2. Entropia podzbioru — rozstrzygnięte.** Widmo komutatora na podzbiorze ma **przerwę 12–15 dekad**; zera są **dokładne** (mpmath 50 cyfr: 10⁻⁵²). Redukcja symplektyczna (odrzucenie jądra) jest jednoznaczna; próg wewnątrz przerwy nie zmienia wyniku. **Ujemna „informacja wzajemna” nie pochodziła z obcięcia, tylko ze złego wyboru podukładów:** I(S:F) ma sens tylko gdy [S,F]=0. Losowe F: 122/300 przypadków I<0; F przestrzenne względem odczytu: 0/300, zmiana progu 0. Konwencja do pamiętania: odrzucenie jądra pomija kierunki klasyczne, które mają fluktuacje.
**Przewidywanie asystenta „obcięcie strukturalne” UPADŁO w tej postaci.** **Pole na antyłańcuchu ma komutator ≡ 0** — brak stopni kwantowych.

**3. Plaster przestrzenny (odczyt w środku) — test reguły sumy źle postawiony.** Plaster nie jest dopełnieniem S. Zmierzone: $S(S\cup E_w)$ rośnie z liczbą elementów (~0,2–0,5 na element — **prawo objętościowe, A10**): plaster nie jest powierzchnią Cauchy'ego. Połówki plastra: $\max|[F,F^c]|=\tfrac12$ dokładnie (w d=2 każda para w relacji). Δ reguły sumy przechodzi przez zero przy w zależnym od N — **dwa efekty się znoszą**, nie wielkość strukturalna.
**Wniosek:** bez obcięcia żaden plaster nie spełnia założeń Zurka (otoczenie = iloczyn fragmentów, S∪E czyste). **Obcięcie nie jest potrzebne, żeby entropia istniała; jest potrzebne, żeby otoczenie się rozkładało.**

**4. Fragmenty komutujące — wzajemnie przestrzenne diamenty 2–4 el. w plastrze (b) vs losowy podział tych samych elementów (a).** g=5, **oscylator w stanie podstawowym = przebieg TŁA**, 8 losowań na punkt, w=0,02–0,30.
Kontrole: [S,F]≤3·10⁻¹⁶, [Fᵢ,Fⱼ]≤9·10⁻¹⁵, Araki–Lieb ok, monotoniczność 0 naruszeń.

| N | fragm. | I(S:U)/S(S) | II/S w (b) | II/S w (a) | (a)−(b) |
|---|---|---|---|---|---|
| 600 | 7–14 | 0,23–0,53 | −0,05…0,00 | +0,08…+0,26 (dwa wybuchy −142, −71) | +0,10…+0,26 |
| 1200 | 12–20 | 0,35–0,52 | −0,07…−0,02 | +0,06…+0,24 | +0,11…+0,29 |
| 2400 | 18–26 | 0,37–0,56 | −0,14…−0,11 | +0,14…+0,17 | +0,25…+0,31 |

(II = I(S:G₁G₂)−I(S:G₁)−I(S:G₂); ujemne = redundancja, dodatnie = synergia.)
- **Brak płaskiego odcinka;** I(S:F) rośnie ~liniowo z liczbą fragmentów. Zdanie „w próżni bez zdarzenia plateau się nie pojawia” — **nie upadło**, w dostępnym zakresie.
- W (b) słaba redundancja, rosnąca z N (kierunek; zakres ×4, 1 realizacja).
- **Niekomutowanie udaje synergię** — test na połówkach plastra odczytałby „brak darwinizmu” fałszywie.
- Grubość plastra i rozmiar diamentu bez widocznego wpływu (w ×15).
- **Ograniczenie twarde:** liczba wzajemnie przestrzennych diamentów rośnie ~√N; dekada fragmentów wymaga N×100.

**Literatura QBM (streszczenie użytkownika, niesprawdzone przez asystenta) [L][?]:** Blume-Kohout–Zurek 2008 — darwinizm w ruchu Browna ze stanem silnie ściśniętym; $R_\delta$ rośnie z czynnikiem ściśnięcia (podane: $R_\delta\approx s^{2\delta}$). Zurek 2022 — krzywe częściowej informacji w QBM mają kształt niezależny od rozmiaru otoczenia; skalowanie z δ inne niż logarytmiczne w modelach spinowych; stany ściśnięte w p dekoherują natychmiast, w x po obrocie π/2.
**Uwaga [A]:** powyższe wyniki to s=1 (stan podstawowy) — przy s=1 redundancji nie oczekuje się w żadnym modelu. **Zgodność z QBM NIE została przetestowana.**

**5. Przebieg ZAPISU — skan ściśnięcia s** (`etap0c_sciskanie.py`). Kowariancja startowa detektora $\mathrm{diag}(s^2/2\omega,\ \omega/2s^2)$; s>1 = szeroki w q (sprzężenie przez q). g=5, w=0,08, diamenty 2-el., 1 realizacja; N=600 (11 fragm.), N=1200 (16 fragm.).
- **Szybki oscylator (ω≈13,3, ωτ_m≈10 rad):** S(S) prawie symetryczne w s↔1/s; fragmenty niosą ≤60% S(S); R′ 2–4; brak wzrostu. **Zdanie „s>1 dekoheruje szybciej” UPADŁO** — orientacja uśrednia się obrotem (~1,6 obrotu w czasie oddziaływania).
- **Wolny oscylator (ωτ_m<π/2).** Stosunek S(S)(s)/S(S)(1/s): ω=1 → 1,46–1,60; ω=0,5 → 1,61–2,03 (N=600 i 1200 zgodne). **Asymetria orientacji — PRZESZŁO.** Druga część „stosunek rośnie z s” — **upadła** (spadek przy s=8).
- ω=0,5, N=1200: I(S:F)/S(S) przy 10/50/100% fragmentów: s=1: 0,27/0,59/0,78; s=4: 0,49/0,74/0,87; s=16: 0,64/0,82/0,91. $R_{0,5}$: 3,2 (s=1) → 4,0 → 5,3 → 8,0 (s=8, 16 — **sufit siatki**: 2 z 16 fragmentów). II/S(S): −0,44 → −0,75. Po stronie 1/s brak wzrostu ($R_{0,5}$ 1,8–2,7).
- **Odczyt:** dla s>1 krzywa wklęsła i wysycająca, silna redundancja — jakościowo jak QBM u Zurka (redundancja rośnie z delokalizacją w zmiennej sprzężenia). **Kształtu $R_\delta(s)$ nie da się porównać z $s^{2\delta}$** (4 punkty, sufit R ≤ liczba fragmentów).
- Zdanie „kształt niezależny od N”: I(S:U)/S(S) przy s=8: 0,87 (N=600) i 0,88 (N=1200) — zgodne, test słaby.
- **Zastrzeżenia:** wolny oscylator w bezmasowym polu d=2 jest silnie splątany już w stanie podstawowym (S(S)≈2 przy s=1 wobec 0,23 dla szybkiego) — możliwy efekt podczerwieni specyficzny dla d=2. Jedna realizacja na N.

**6. (B) Fragmenty = składowe spójne grafu relacji w plastrze** (`etap0d_skladowe.py`) — wybór wewnętrzny dla porządku, bez decyzji; składowe komutują z definicji. ω=0,5, g=5, N=1200. Kontrole: [Fᵢ,Fⱼ]≤5·10⁻¹⁵, [S,F]≤3·10⁻¹⁵, Araki–Lieb bez naruszeń.
- Grubość: w=0,02 → 16 fragm., pokrycie plastra 0,67; w=0,04 → 6, pokrycie 0,99; w=0,08 → 2 (zlewanie się składowych).
- **Zdanie „R₀,₅=8 było sufitem” — PRZESZŁO** (przy w=0,02 dochodzi do 16 = nowy sufit).
- 6 realizacji (w=0,02; 10–16 fragm.), f_δ z interpolacji, serie ucięte wyłączone.
  - Na „dostępnym” zakresie s wykładnik rósł z δ (0,41 / 0,47 / 0,61 dla δ=0,25/0,35/0,5; stosunek 1,52±0,16). **Na wspólnym zakresie s zależność od δ znika** (s=1–4: 0,52/0,58/0,59; s=2–8: 0,51/0,48/0,50) — pozorny wzrost był artefaktem różnych zakresów. Pojedyncza realizacja dawała stosunek 1,7 — przypadkowa zgodność z oczekiwaną liczbą.
- **Źródło sprawdzone [L]:** Blume-Kohout–Zurek, arXiv:0704.3615 / PRL 101, 240405 (2008). Definicja R_δ jak u nas. Przy założeniu, że I(S:F) zależy tylko od f i E = cała kąpiel: $f_\delta=e^{-2\delta H_S}/(1+e^{-2\delta H_S})$, $R_\delta\approx e^{2\delta H_S}\approx s^{2\delta}$ (r. 17), bo $H_S\approx\ln s$. Ściśnięcia ~10³–10⁵; R₅₀% > 10³ = ich granica rozdzielczości. W przeglądzie Zurka niezmienniczość kształtu krzywej dotyczy **ściśnięcia i czasu**, nie rozmiaru otoczenia.
- **U nas S(S) rośnie o 0,63/0,67/0,69/0,70/0,69 na podwojenie s (ln 2=0,693)** — przesłanka $H_S\approx\ln s$ spełniona (z przesunięciem ≈2 nat).
- Test $R_\delta-1\propto s^{2\delta}$ przy małym δ (zapisany przed rachunkiem: 0,20/0,30/0,50 dla δ=0,10/0,15/0,25): wyszło 1,23 (n=2) / 1,09±0,09 / 0,81±0,07 — **ale test źle postawiony:** próg (1−δ)S(S) leży przy I(S:U)=0,82–0,93·S(S), więc R zależy od tego, jak blisko progu podchodzi całość fragmentów, nie od redundancji.
- **Wniosek:** brak czystego okna. Mały δ — niepełne otoczenie; duży δ — sufit liczby fragmentów. **Cały zbiór fragmentów leży jeszcze na rosnącej części krzywej** (w czystym przypadku pełne E niesie 2H_S, „plateau” na H_S; u nas I(S:U) < S(S)). Źródło = A10: bez obcięcia żaden cienki obszar nie zawiera pełnego otoczenia.
- **Stoi:** S(S)≈const+ln s; asymetria orientacji; redundancja rośnie z delokalizacją. **Nierozstrzygnięte:** postać $R_\delta(s)$ — ani „zgodne z $s^{2\delta}$”, ani „obalone”.

**7. Seria N i pojemność** (`etap0e_seria.py`; ω=0,5, g=5, w=0,02, 6 realizacji na punkt, s∈{1,4,16}, zakres δ wspólny dla N).
- **Liniowość:** przy stałym δ log R liniowe w **log s** (R² 0,98), nie w s (0,76–0,94) — potęga, jak u Zurka. Przy stałym s log R liniowe w **δ** (R² 0,97–0,99) — wykładniczo w δ, jak u Zurka.
- **Odniesienie poprawione [A]:** dokładny wzór $R=1+e^{2\delta H_S}$ daje na użytych zakresach δ nachylenie/(2H_S)=0,87 (s=1), 0,90 (s=4), 0,90 (s=16). Wcześniejsze „s=1 trafia w 2S(S) co do 1%” było porównaniem z asymptotyką — wtedy s=1 było o ~12% za strome.
- **S(S) nie zależy od N** (wykładnik −0,001 dla każdego s).
- **Seria na składowych zafałszowana:** przy stałym w składowe rosną z N (maks. 2–6 / 5–12 / 15–27 el.), a większe fragmenty obniżają nachylenie — dwa efekty się znosiły.
- **Czysta seria (diamenty ≤2), H_eff/S ÷ wzór dokładny:**

| s | N=1200 | N=2400 |
|---|---|---|
| 1 | 1,13 | 1,37 |
| 4 | 0,88 | **1,03** |
| 16 | 0,84 | **1,00** |

  (1) rośnie razem z pojemnością (C=ΣS(F)/S: 12–14 → 23–26; I(S:U)/S: 0,73–0,88 → 0,83–0,92) — zachowanie zgodne z niepełnością. Przy s≥4 niedobór znika przy N=2400; przy s=1 nachylenie przekracza wzór coraz bardziej. Różnica s=1 vs s≥4 (~0,3) zostaje. Dwa N — kierunek.
- **Hipoteza nasycenia pojemności fragmentu — UPADŁA (w złą stronę).** N=2400, H_eff/S dla s=1/4/16: diamenty≤2: 1,19/0,93/0,90; ≤4: 1,03/0,82/0,80; składowe: 0,98/0,79/0,78. Większe fragmenty → niższe nachylenie. C≫1 wszędzie — fragmenty splątane głównie z resztą zbioru; pojemność nie jest wąskim gardłem.
- **Wynik:** H_eff zależy od podziału otoczenia o ~0,1–0,2 — tyle, ile mierzone efekty. To liczba (zbiór + detektor + **cięcie otoczenia**), nie samego zbioru. Wzór Zurka zakłada, że I zależy tylko od f (fragmenty jednorodne); u nas nie są.

**8. Ważony ułamek f** (`etap0f_wazone.py`; N=2400, w=0,02, 6 realizacji, 6 permutacji zapisanych osobno; f ważone liczbą fragmentów / liczbą elementów / S(Fᵢ); krzywe uśrednione na wspólnej siatce f).
- **Zapisane przed analizą:** jeśli źródłem zależności od podziału jest niejednorodność fragmentów, rozrzut między podziałami maleje po ważeniu. **Kontrola:** dla diamentów ≤2 ważenie elementami ≡ ważenie liczbą — **przeszło (różnica 0)**.
- Rozrzut H_eff/S (÷ wzór dokładny) między składowymi, diamentami ≤2 i ≤4, dla s=1/4/16: liczba 0,21/0,15/0,11; elementy 0,21/0,17/0,20; entropia 0,23/0,20/0,20. **Hipoteza niejednorodności — UPADŁA.**
- Realizacje 4 i 6: oba podziały złożone wyłącznie z linków, różny tylko wybór linków. Różnica H_eff/S: −0,25/−0,23/−0,22 (real. 4) i +0,01/−0,05/−0,08 (real. 6). **Sam dowolny wybór linków zmienia H_eff w jednej realizacji do 0,25** — tyle, ile cały „efekt podziału”. Średnia różnica ≤2 vs ≤4 (0,1–0,15, ~2σ) nie jest pewnym efektem rozmiaru.
- **Wniosek:** H_eff zależy od tego, **które** elementy są otoczeniem, nie od wielkości fragmentów. To jest cięcie, widoczne jako rozrzut wewnątrz realizacji.
- **Jedyny podział bez losowego wyboru — składowe spójne:** H_eff/S ÷ wzór dokładny = **1,17±0,05 (s=1), 0,89±0,04 (s=4), 0,89±0,04 (s=16)** przy N=2400, w=0,02. Grubość w pozostaje wyborem.
- Porównanie metod: liczenie przez uśrednienie na siatce f zgodne z wcześniejszym (diamenty ≤2: 1,39/1,04/1,00 wobec 1,37/1,03/1,00).

**9. Zespół przesunięć — jest co zapisywać** (`etap0g_przesuniecia.py`). Podstawa [H]: **pole bez wzbudzenia ≡ Ø**, więc ściśnięcie zapisuje „w pustce”; zapis wymaga wzbudzenia. **Uwaga techniczna [A]:** samo przesunięcie (stan koherentny) nie zmienia żadnej entropii — kowariancja bez zmian. Dlatego zapisywaną wielkością jest **klasyczny zespół przesunięć** d o wariancji V_d, a miarą $I(d{:}F)=S(\Gamma_F+V_d\,mm^T)-S(\Gamma_F)$ (Holevo), m = odpowiedź obserwabli na d.
- Kontrole: g=0 → 0; V_d=0 → 0 (dokładnie).
- N=2400, w=0,02, składowe (17 fragm.), ω=0,5, g=5:

| V_d | I(d:S) | I(d:U)/I(d:S) | R₀,₅ | R₀,₂₅ | R₀,₁ |
|---|---|---|---|---|---|
| 0,25 | 0,106 | 0,925 | >17 | 6,2 | 2,0 |
| 4 | 0,783 | 0,954 | >17 | 8,5 | 3,6 |
| 16 | 1,391 | 0,969 | >17 | 15,3 | 5,9 |
| 256 | 2,748 | 0,983 | >17 | >17 | 8,5 |

- **Płaski odcinek jest**: 25% fragmentów niesie 91–98% całości; **jeden fragment zna ponad połowę zapisu przy każdym V_d**; otoczenie wie prawie tyle co detektor.
- **Wynik nie zależy od cięcia:** I(d:U) przy V_d=4 = 0,747 (składowe), 0,743 (linki), 0,744 (inna realizacja) — wobec rozrzutu 0,25 dla H_eff w punkcie 8.
- **Zastrzeżenie [A]:** d jest klasyczne, a informację klasyczną można kopiować — redundancja i plateau są tu spodziewane także w kontinuum. To potwierdza „musi być co zapisywać”, ale nie jest samo w sobie dowodem struktury darwinowskiej.

**10. Czy plateau daje skalę (cięcie wewnętrzne)? — NIE.** Zapisane przed rachunkiem: (1) rozmiar najmniejszego wystarczającego fragmentu niezależny od podziału; (2) przy rosnącym N rośnie w elementach, ale objętość dąży do stałej; (3) zależność od w lub podziału obala kandydata.
- **Wynik: najmniejszy wystarczający fragment ma 2 elementy (pojedynczy link) przy N=600, 1200 i 2400.** To minimum możliwe; objętość dąży do zera. **Przewidywanie (2) UPADŁO — plateau nie wyznacza skali.**
- **Decyduje położenie, nie rozmiar:** I(d:F_i)/I(d:S) od 0,04 do 0,94 przy tym samym rozmiarze. Korelacja I z liczbą elementów odcinka oddziaływania w przeszłości fragmentu: **r = +0,84** (N=2400, V_d=4). Link 2-elementowy z 36/46 w przeszłości: 0,90; fragment 7-elementowy z 2/46: 0,18.
- **Odczyt [H]:** zapis leży w przyszłości źródła — kryterium czysto porządkowe („dym” z przykładu z samolotami). To sugeruje, że brakująca reguła wag dla pętli (Pellegrin) może pochodzić z **zakotwiczenia na źródłach** (por. Wheeler–Feynman, C4a „Dalej otwarte”), a nie z plateau.
- **Zastrzeżenie:** „dużo odcinka w przeszłości” i „blisko przestrzennie” są w tym ustawieniu powiązane; rozdzieliłby je plaster wzięty wyżej niż odczyt. Jedna realizacja.

**11. Czy zakotwiczenie na źródłach (Wheeler–Feynman) wystarcza?** (`etap0i_wf.py`) — **WNIOSEK UNIEWAŻNIONY przez 14 i 15 (poprawka 44).** Odpowiedź brzmi: **wystarcza**, jeśli liczyć miarę, a nie sztuki. Poniższy rachunek zostaje jako zapis tego, co zmierzono, i jako przykład błędu normalizacyjnego. Czytać razem z 14 i 15.
Zapisane przed rachunkiem (d=2, dwie linie świata = najdłuższe łańcuchy, L ∝ √N): (1) pary w relacji ∝ N; (2) pary połączone **linkiem** ∝ N^0,5 (wtedy suma ekstensywna w czasie własnym); (3) kontrola z koronami.
- Zmierzone (3 realizacje na punkt, N=300–2400): L ∝ N^0,51 ✓; pary w relacji ∝ N^1,04 ✓; **linki ∝ N^0,21 — wysycają się** (17,7 → 24,3 → 29,3 → 27,0). **Przewidywanie (2) UPADŁO.** Przy większej gęstości między odległymi punktami zawsze znajdzie się element pośredni: **link nie jest dyskretnym odpowiednikiem stożka** dla odległych zdarzeń.
- Warstwy o ustalonej **liczbie elementów** (k ≤ 0, 1, 3): wykładnik +0,21–0,22 (zanikają). Warstwy o ustalonej **objętości** (ε=0,002; 0,005): +0,93 i +1,02, czyli ∝ L², bo liczba elementów linii na jednostkę czasu własnego rośnie jak √N. Odległość między liniami 0,16–0,29 przy szerokości diamentu 1,41 — linie nie leżą na sobie.
- **Kontrola (3) była źle postawiona** (asystent): policzone korony ze wszystkich czwórek → N^3,97, banalne; Pellegrin liczy korony **z linków**.
- **Wniosek:** zakotwiczenie usuwa sumowanie po całym sprinklingu i dobrze lokalizuje zapis (r=0,84, C4a.10), ale nie daje zbieżnej reguły wag. Ani skala dyskretności, ani ustalona objętość nie odtwarza działania Fokkera (∝ L).

**14. Ważona suma Fokkera — POPRAWKA do punktu 11** (`etap0l_fokker.py`). Działanie Fokkera to miara, nie liczba: dyskretny odpowiednik $\iint d\tau_1 d\tau_2\,\delta(s^2)$ to $S=(\alpha t_P)^2/\Delta \cdot \#\{\text{pary } s^2\le\Delta\}$, czas własny **z porządku** (najdłuższy łańcuch, α=1/√2, t_P=N^(−1/2)). Dwie linie świata (najdłuższe łańcuchy), 3–4 realizacje.

| N | Δ=0,005 | 0,01 | 0,02 | 0,04 |
|---|---|---|---|---|
| 600 | 10,22 | 8,86 | 6,49 | 5,41 |
| 1200 | 11,11 | 8,19 | 7,05 | 5,91 |
| 2400 | 7,78 | 6,78 | 5,92 | 4,91 |
| 4800 | 9,67 | 8,77 | 7,39 | 6,17 |

- **Zdanie 1 (S niezależne od N) — PRZESZŁO** (N ×8, ±15%, bez trendu; gołe liczby par rosną ×8: 61→464).
- **Zdanie 3 (S ∝ długość odcinka) — PRZESZŁO** (Δ=0,01: 1,48 / 2,66 / 4,11 / 6,78 dla ¼, ½, ¾, 1).
- **Zdanie 2 (S niezależne od Δ) — NIE PRZESZŁO**: S ∝ Δ^(−0,23); przy N=4800 i Δ=0,00125…0,01 wykładnik −0,23 (14,50 / 11,00 / 9,85 / 8,89), więc to nie górna krawędź okna (d²≈0,04). Kandydat: rozmycie kwantowania przy n_max=3–10 (fluktuacja długości łańcucha ~1 przenosi pary przez próg). Nierozstrzygnięte.
- **Wniosek:** punkt 11 („suma nadekstensywna, zakotwiczenie nie wystarcza”) **był błędny** — rozbieżność brała się z liczenia par zamiast ważenia miarą. Po unormowaniu suma jest skończona i ekstensywna w czasie własnym. **Ale** pełna wewnętrzność reguły wag wymagałaby niezależności od Δ; zostaje resztkowa zależność od szerokości warstwy — słabszy ślad skali niż wcześniej, ale obecny.

**15. Skąd resztkowa zależność od Δ — ROZSTRZYGNIĘTE: to nie dyskretność** (`etap0m_wykladnik.py`).
Przewidywanie ciągłe dla dwóch prostych linii oddalonych o d: $\iint d\tau_1 d\tau_2\,\delta(s^2)=\tau/d$. Badana wielkość: **R = S·d/τ** (przewidywanie: stała rzędu 1). N=1200, 2400, 4800; Δ tak dobrane, by n_max=√(2ΔN) się pokrywały; 4 realizacje.
- **Zdanie 1 (R rzędu 1) — PRZESZŁO:** R = 0,52–1,20, a przy najcieńszych warstwach 1,19–1,20.
- **Zdanie 2/3 (zbieżność po n_max) — NIE:** punkty o tym samym n_max rozjeżdżają się (n_max=13,9: R = 0,518 / 0,750 / 0,818). Rozrzut wokół wspólnej krzywej R(n_max): **17,4%**.
- **Zbieżność po Δ/d² — TAK:** wszystkie 12 punktów na jednej krzywej, rozrzut **3,8%**; punkty o tym samym Δ/d² przy n_max różnym dwukrotnie zgadzają się w kilku procentach. Ekstrapolacja Δ/d²→0: **R = 1,25** (ciągłe: 1).
- **Wniosek:** zależność od Δ to błąd przybliżenia δ(s²) warstwą o skończonej szerokości — znika, gdy warstwa jest cienka względem geometrii. **Brak śladu skali.** Dla tej wielkości w d=2: **zakotwiczenie na źródłach + normalizacja miarą wystarczają**; suma skończona, niezależna od gęstości, ekstensywna w czasie własnym, odtwarza τ/d. **Punkt 11 upada w całości.**
- **Zastrzeżenie:** d liczone ze **współrzędnych**, nie z porządku. Pełna wewnętrzność wymaga odległości przestrzennej z nakładania przyczynowego (C4a.12) — następny krok. Także: d=2, linie = najdłuższe łańcuchy (wędrują), 4 realizacje, R(0)=1,25 wobec 1 (konwencja α, sposób liczenia d).

**16. Entropia jako kandydat na kontrprzykład dla kryterium „sztuki czy miara” [P]** (`etap0n_entropia.py`, `etap0o_sy.py`).
Kryterium (użytkownik): *liczba jest dopuszczalna tylko wtedy, gdy nie rośnie z gęstością; jeśli rośnie, jest gęstością i wymaga miary — mnożymy przez potęgę t_P wynikającą z wymiaru, przewidzianą PRZED rachunkiem, nie dopasowaną po.*
- **(a) Bez obcięcia:** poddiament 1/16 objętości, N=300…2400, 2 realizacje: S = 6,37 / 15,10 / 32,09 / 63,52; **wykładnik +1,10** (prawo objętościowe). S/N = 0,021 / 0,025 / 0,027 / 0,027 → zbiega. **To gęstość, nie liczba — kryterium działa, nie jest to kontrprzykład.**
- **(b) Z obcięciem — NIEROZSTRZYGNIĘTE.** Wersja uproszczona (próg c√N/(4π) globalnie, próg względny lokalnie) dała S = 0,179·ln N (c=1) i 0,199·ln N (c=2), co kusząco zgadza się z oczekiwanym 1/6 wobec ln N (= 1/3 wobec ln k_max). **Ale pełne podwójne obcięcie wg 1712.04227 §3.1–3.2 (próg √N/(4π) w dużym diamencie i √N_U/(4π) w poddiamencie) NIE odtworzyło prawa powierzchniowego**: S skacze wokół zera (−1,5…+0,45) dla V/V_U = 4 i 16, przy skanie stałej c = 0,1…4; nachylenia to szum.
- **Diagnoza [A]:** wartości własne uogólnionego problemu powinny leżeć w λ≥1 lub λ≤0 (para (1+n, −n) = entropia bozonowa); u nas część wpada w (0,1) → ujemne wkłady. Po moim drugim obcięciu **W|_U przestaje być dodatnie względem obciętego iΔ|_U**. Przepis mówi: obcięcie działa jednocześnie na iΔ_κ|_U **i na W_κ|_U (równoważnie R_κ|_U)** — czyli obcina się część rzeczywistą, a nie rzutuje odziedziczone W na podprzestrzeń własną iΔ. **Następne podejście zaczyna się od poprawnej wersji drugiego obcięcia.**
- **(c) POPRAWIONA IMPLEMENTACJA — WYNIK** (`etap0p_sy2.py`). Błąd był w liczeniu λ wprost z W (złe uwarunkowanie, mieszanie modów). Poprawnie: $W=R+\tfrac12 i\Delta$, więc $\lambda=\tfrac12+\nu$, gdzie ν to wartości własne $(i\Delta|_U)^{-1}R|_U$; mody niefizyczne to λ∈(0,1) (|ν|<½, łamią nieoznaczoność). Po tej zmianie modów niefizycznych nie ma wcale.
  - **Kontrola (mogła upaść):** bez obcięcia globalnego wykładnik **+1,03** — prawo objętościowe, jak w literaturze.
  - **Podwójne obcięcie (c=1, V/V_U=16), 3–8 realizacji:** S = 1,910±0,046 (N=512); 2,250±0,048 (1024); 2,198±0,024 (2048); 2,356±0,071 (3072); 2,374±0,065 (4096). Zakres 1,9–2,4 pokrywa się z rysunkiem 3 w 1712.04227 (1,8–2,5).
  - **Dopasowanie ważone (c=1, N=512…4096): S = (0,188 ± 0,065)·ln N.** Przewidywanie 1/6=0,167 → 0,3σ; 1/3=0,333 → 2,2σ. Wobec ln k_max daje to 0,376, a literatura podaje 1/3 — to samo zdanie w dwóch zmiennych.
  - **Skan stałej c przy poprawionym λ (V/V_U=16, 4 realizacje, N=1024/2048/3072):** c=0,5 → S≈5,2–6,0, nachylenie +0,656; **c=1 → 2,2–2,4, +0,088**; c=1,5 → +0,101; c=2 → +0,061; c=3 → +0,045. **Nachylenie silnie zależy od c**, a przy c=1 na węższym zakresie N wychodzi 0,088 zamiast 0,188.
  - **Status po małym przebiegu:** zgodny z 1/6, niezgodny z 1/3 na 2,2σ, ale **nie wniosek wg §E** — 0,9 dekady, jedna wartość c.
  - **(d) DUŻY PRZEBIEG — WARUNKI §E SPEŁNIONE** (użytkownik, GPU/CuPy, inny generator niż NumPy, więc **niezależny pomiar, nie reprodukcja**). N = 512…16384 (**1,5 dekady**), 6 ziaren, V/V_U=16, skan c = 0,5…3, kontrole (hermitowskość, część urojona ≤1,9·10⁻¹⁵, parowanie λ↔1−λ ≤5,3·10⁻¹⁰) przeszły.
    - **Kontrola wariantu A:** wykładnik wobec N_U = **+1,055 ± 0,032** (bez najmniejszego punktu +1,056; ogon +1,038) — prawo objętościowe.
    - **Nachylenie wobec ln N:** c=1 → 0,182±0,068; c=1,5 → 0,165±0,042; c=2 → 0,179±0,036; c=3 → 0,168±0,028. **Średnia dla c≥1: ≈0,17.** Bez N=512: 0,161 / 0,158 / 0,175 / 0,175.
    - **Falsyfikator ze skryptu** („pełne i obcięte różnią się o więcej niż słupek”) **przechodzi dla c≥1** (różnice 0,021 / 0,007 / 0,004 / 0,007) i **upada dla c=0,5** (0,135 przy słupku 0,086) — mały próg skażony przejściówką.
    - **Nachylenie nie zależy od c (c≥1): rozrzut 0,028, mniejszy od słupków. Stała zależy silnie** (S przy N=16384: 5,99 / 3,78 / 2,60 / 1,90 / 1,63 / 1,37 dla c=0,5…3). Tak zachowuje się obcięcie UV w $S=\tfrac13\ln(\ell/\varepsilon)$: zmienia ε, nie współczynnik. **To osobny argument, że mierzone jest prawo, nie artefakt progu** — i odpowiedź na poprawkę 49.
    - **Wynik: 1/6 = 0,167 trafione; 1/3 = 0,333 odpada.** Zastrzeżenia poprzedniego statusu (0,9 dekady, jedna wartość c) **zniesione**.
    - **Zostaje jedno [?]:** nachylenia na ogonie (4 ostatnie N, 0,5 dekady) są konsekwentnie niższe: 0,127 / 0,155 / 0,131 / 0,154 dla c=1…3, średnio 0,142 wobec 0,174 z pełnego zakresu. Szum czy dryf w dół — **rozstrzygnięte w (e): szum.**

  - **(e) SKAN ROZMIARU OBSZARU — LOGARYTM NIE POCHODZI OD POLA POWIERZCHNI** (`etap0q_sy_duzy.py`, użytkownik, A100; N = 2048…16384, 6–8 ziaren, c ∈ {1; 1,5; 2; 3}, **V/V_U ∈ {4; 9; 16; 36}**; 20480 i 24576 padły na pamięci GPU).
    - **Z4 (kontrola A): przeszło** — wykładnik +1,004 / +1,016 / +1,044 / +1,051 dla r=4/9/16/36.
    - **Z1 (nachylenie niezależne od r): przeszło** — wszystkie 16 kombinacji (c, r) w przedziale 0,154–0,190, średnio ≈0,172. 1/6 trafione, 1/3 odpada.
    - **Z3 (brak dryfu): przeszło** — okna [2048–12288] i [4096–16384] różnią się o 0,009 / 0,021 / 0,012 / −0,006 przy podobnych słupkach. **Otwarte pytanie z (d) zamknięte: to był szum.**
    - **Z2 (stała spada o (1/6)·ln(r₂/r₁) = 0,135 / 0,096 / 0,135): UPADŁO.** Zmierzone różnice: −0,132 / −0,025 / +0,022 (c=1) i podobnie dla pozostałych c — niemonotoniczne, z odwrotnym znakiem. Przy dziewięciokrotnej zmianie objętości obszaru S zmienia się o mniej niż 0,13.
    - **Test rozstrzygający — pary o tym samym $N_U$, różnym N** (zdanie do upadku: przy równym $N_U$ entropie są równe, bo $\ell_U/\varepsilon\propto\sqrt{N_U}$): **upadło w 12 na 12 przypadków, na 5–20σ.** Różnice (N₂/N₁ = 4): $N_U$=512: +0,492 / +0,338 / +0,335 / +0,305; $N_U$=455: +0,189 / +0,199 / +0,170 / +0,190; $N_U$=1024: +0,398 / +0,321 / +0,299 / +0,300 — wszystkie bliskie **+0,231 = (1/6)·ln 4**, czyli wartości dla zależności od **gęstości globalnej**.
    - **Mechanizm:** liczba zachowanych modów rośnie jak √N, nie jak √N_U (c=1, r=16: 13 przy N=512, 109 przy N=16384). **Mierzony logarytm to logarytm liczby zachowanych modów globalnych, nie rozmiaru obszaru**; „1/6 wobec ln N” to (1/2)·ln N pod inną nazwą.
    - **Dlaczego nie było widać:** w literaturze rysuje się S wobec $N_U$ **przy ustalonym** V/V_U — wtedy N i $N_U$ są proporcjonalne i obu odczytów nie da się odróżnić. Rozdzielają je dopiero pary o równym $N_U$ i różnym N.
    - **Odczyt [H] (użytkownik):** entropia jest **efektem, nie prawem** — liczbą o relacji obszaru z resztą, zależną od cięcia. To, co po obcięciu wychodzi jako logarytm, jest efektem procedury odcinania modów.
    - **Zastrzeżenia:** to **nasza** implementacja podwójnego obcięcia (odtwarza jednak i prawo objętościowe, i zakres wartości z 1712.04227); **d=2**; **jedna rodzina obszarów** (koncentryczne diamenty); **nie wiadomo, czy w d=4 tak samo**.
    - **Co zdjęłoby zastrzeżenia:** (i) d=4 z $K_R=\frac{1}{2\pi\sqrt6}\cdot$(macierz linków) — ta sama procedura, inny propagator; (ii) obszar przesunięty, nie koncentryczny; (iii) niezależna implementacja obcięcia.

  - **(g) OBSZAR PRZESUNIĘTY — zastrzeżenie (ii) ZDJĘTE** (`etap0s_przesuniecie.py`). d=2, r=16 (ta sama objętość), poddiament odsuwany od środka: przestrzennie (u w górę, v w dół) i czasowo (oba w tę samą stronę). N=2048 (5 ziaren) i N=4096 (2 ziarna). **Zdanie przed rachunkiem:** przy ustalonym N i objętości S nie zależy od położenia, dopóki obszar nie dotyka rogów.

| przesunięcie | S(c=1), N=2048 | S(c=2), N=2048 | S(c=1), N=4096 | S(c=2), N=4096 |
|---|---|---|---|---|
| środek | 2,202±0,035 | 1,242±0,015 | 2,319±0,057 | 1,382±0,035 |
| przestrzenne 0,1 | 2,238±0,047 | 1,240±0,024 | 2,426±0,102 | 1,349±0,013 |
| przestrzenne 0,2 | 2,191±0,068 | 1,211±0,033 | 2,194±0,016 | 1,258±0,010 |
| przestrzenne 0,3 | 2,134±0,062 | **1,087±0,028** | 2,096±0,058 | **1,228±0,001** |
| czasowe +0,1 | 2,220±0,055 | 1,239±0,024 | 2,342±0,065 | 1,385±0,034 |
| czasowe +0,2 | 2,290±0,042 | **1,319±0,034** | 2,474±0,080 | **1,493±0,002** |

    - **We wnętrzu zdanie przechodzi:** przesunięcia 0,1 i 0,2 nieodróżnialne od środka.
    - **Przy brzegu nie:** przestrzenne 0,3 (obszar przy rogu) daje −0,154 przy c=2, czasowe +0,2 (pod wierzchołkiem przyszłości) +0,077; przy N=4096 odpowiednio −0,154 i +0,111. **Efekt nie maleje z gęstością** — gdyby był artefaktem dyskretności, zmalałby dwukrotnie.
    - **Odczyt [H]:** liczba nazywana entropią obszaru zależy od tego, **jak obszar leży względem reszty**, nie tylko ile go jest. To jest „efekt, nie prawo” w postaci mierzalnej.
    - **Zostaje ostatnie zastrzeżenie:** niezależna implementacja obcięcia (iii).

  - **(f) TO SAMO W d=4 — zastrzeżenie (i) CZĘŚCIOWO ZDJĘTE** (`etap0r_d4.py`). **Uwaga o nazwie (pułapka nr 5):** literaturowe „d=4” to w konwencji tego pliku **3 kierunki + dynamika i pamięć** — sprinkling w diamencie z trzema kierunkami przestrzennymi i porządkiem, nie czwarty kierunek. Propagator: $K_R=L/(2\pi\sqrt6)$, L = macierz linków. Para o równym $N_U$ (~130 elementów): N=512, r=4 wobec N=2048, r=16; 3–4 ziarna.

| c | N=512, r=4 | N=2048, r=16 | stosunek |
|---|---|---|---|
| 0,5 | 18,7 ± 0,5 | 38,4 ± 1,4 | ×2,05 |
| 1,0 | 7,90 ± 0,32 | 16,35 ± 0,48 | ×2,07 |
| 2,0 | 1,69 ± 0,03 | 2,43 ± 0,10 | ×1,43 |

    - **Zdanie „przy równym $N_U$ entropie równe” upada także tutaj** — entropia podwaja się przy czterokrotnym wzroście gęstości i tym samym obszarze. **Efekt nie jest specyficzny dla d=2.**
    - **Ale mechanizm jest inny niż w d=2 i liczby nie nadają się na wniosek ilościowy:** liczba modów jest w obu członach pary prawie równa (38–46 wobec 40–46), a entropia i tak się podwaja; zależność od c jest bardzo silna (38 → 2,4 przy c od 0,5 do 2); S na element rośnie z gęstością, co wygląda na resztkę prawa objętościowego, nie na logarytm. **Podejrzenie:** próg $\alpha_{min}$ przeniesiony z d=2 przez przeskalowanie stałej propagatora **nie jest właściwym obcięciem dla d=4**. Przed jakimkolwiek wnioskiem ilościowym: sprawdzić w literaturze wersję progu dla d=4.
- **Granica kryterium [H]:** logarytm nie daje się unormować żadną potęgą t_P. Jeśli (b) się potwierdzi, oznacza to: **miara wystarcza tam, gdzie nie ma cięcia; logarytm jest znakiem, że cięcie już zostało zrobione.**
- **Poprawki do serii (użytkownik):** bliźniaki z A3a nie są kontrprzykładem — prawo $n^{k-(k-1)d}$ samo jest normalizacją (wykładnik: 0 dla k=2,d=2; ujemny dla d≥3 lub k≥3; niezmiennikiem jest współczynnik). Mody w podzbiorze **nie należą** do tej serii: tam problemem było niezerowe centrum algebry, a lekarstwem redukcja symplektyczna, nie normalizacja.

**12. Skala Sorkina: import czy porządek? — IMPORT; ale jest zamiennik [L].**
- Skala nielokalności ξ ≥ l (ε=(l/ξ)^d) została wprowadzona, by stłumić fluktuacje, które przy pojedynczym sprinklingu są ogromne i rosną z gęstością; w uogólnieniu Aslanbeigi–Saravani–Sorkin zasięg nielokalności zadaje **pojedynczy wolny parametr**. W pracy o granicy na masę Higgsa (2305.07595) autorzy zauważają, że rozdzielenie skali nielokalności i dyskretności może nie być spójne, i skłaniają się do utożsamienia ρ^(−1/4) ze skalą dyskretności.
- **Boguñá–Krioukov, arXiv:2506.18745 (2025):** (a) operatory nielokalne **nie zbiegają** dla pola stałego (dają −2ρφ₀ zamiast 0) ani dla pola funkcji τ² (rozbieżność przy skończonym ρ); zbieżność wymaga zwartego nośnika, co jest równoważne wyborowi układu odniesienia. (b) **Lokalne otoczenie z samego porządku:** czas własny = najdłuższy łańcuch (A2), odległość przestrzenna = nakładanie przyczynowe (Boguñá–Krioukov 2024 — **już cytowane w A2**); sąsiedzi o tym samym czasie własnym nie są równoważni **między sobą**, więc można je uporządkować po odległości przestrzennej. (c) Wychodzi operator **lokalny, lorentzowsko niezmienniczy, samouśredniający**, zbieżny na dowolnym polu, **bez skali nielokalności**.
- **Cena:** zamiast wolnego parametru — **reguła skalowania** (okna na n, m zależne od t_P; optymalne m ~ t_P^(−(6−β_d)/(d+6))), stałe α_d, β_d (α_d ściśle znane tylko dla d=1) oraz wybór geodezyjnej przez zdarzenie. Nie nowa skala, ale nadal wybór. Jedna grupa, praca świeża, numeryka w 2+1.
- **Konsekwencja dla pięciu porażek [H]:** brakującym składnikiem nie jest skala, tylko **odległość przestrzenna mierzona porządkiem**. Nasz test WF użył linków (za wąsko, wysycenie) i objętości (za szeroko, ∝ L²), a nie miał trzeciej opcji: „ustalona odległość przestrzenna z porządku”. Tym samym narzędziem należy próbować: wag pętli (Pellegrin), jądra Fokkera, wyboru otoczenia dla fragmentów (C4a.8), cięcia C1/C2 i obcięcia SJ (A10).

**13. Pole, fala, foton, c — porządkowanie pojęć [H] + test nośnika [P]** (`etap0k_foton.py`).

**Lista (użytkownik):** bez czasoprzestrzeni; 3D + dynamika (brak zera absolutnego) + trajektoria i pamięć = czas.
- **pole ≡ Ø** — nośnik, struktura, w której wzbudzenia są możliwe; brak różnicy, brak informacji;
- **fala = wzbudzenie = różnica = informacja** — **poza Ø**; samo słowo „fala” zakłada już wzbudzenie (poprawka użytkownika do błędu asystenta, który wrzucił falę do Ø);
- **foton = minimalne wzbudzenie** = relacja bez elementów pośrednich (t=0);
- **prędkość nie należy do fali** — powstaje dopiero w porównaniu z inną strukturą mającą zegar.

**c** (zestawienie: A2 wiersz „c”, B1 bilans przeliczników)**:** dwustronna prędkość jest mierzalna (jeden zegar, sygnał tam i z powrotem), **jednostronna nie** — synchronizacja dwóch zegarów wymaga znajomości tego, co miałaby zmierzyć (konwencja Reichenbacha ε ∈ (0,1); ε=½ to wybór Einsteina). W porządku: dwa zdarzenia „jednoczesne” to para nieuporządkowana, czyli brak relacji. **c ≡ 1 z definicji** — stożek to porządek; „pomiar c” = porównanie dwóch miar z porządku (najdłuższy łańcuch ↔ odległość przestrzenna). **Uwaga [L]:** Malament — porządek **plus jedna linia świata** wyznacza już standardową jednoczesność jednoznacznie; to trajektoria, nie porządek, ustala synchronizację (spór z konwencjonalistami trwa).

**Test: czy „łańcuch linków przy stożku” jest nośnikiem relacji t=0? — NIE.** Para prawie zerowa (Δu=0,8; Δv=0,02; τ≈0,179), nośnik = najdłuższy łańcuch e→a, N=600…153 600 (×256), 8–12 realizacji.
- Zdanie 1 (łańcuch istnieje, długość ∝ √(ρV)) — **przeszło** (wykładnik +0,55; 92 elementy przy N=153 600).
- Kontrola (kolejne pary są linkami) — **przeszła** (91/91, 44/44, …).
- Zdanie 2 (rozmycie poprzeczne maleje z gęstością, przewidywane ∝N^(−1/6) za Boguñą–Krioukovem) — **UPADŁO**: wykładnik −0,06 (średnia), +0,015 (maksimum); wartości 1,07 / 1,24 / 1,00 / 1,06 / 0,77 ·10⁻².
- Zdanie 3 (rozmycie maleje względem grubości stożka) — **UPADŁO**: r/τ = 0,05–0,07 przy każdym N **i** przy każdej grubości (dv = 0,005…0,08), r ≈ ¼ maksimum możliwego w przedziale.
- **Odczyt:** rozmycie jest narzucone przez kształt przedziału, nie przez dyskretność. Łańcuch nie wyostrza się do linii — wypełnia cały przedział. Para dokładnie zerowa: przedział pusty, **nośnika nie ma wcale**. Propozycja asystenta „foton = łańcuch linków przy stożku” — **fałszywa**. Zgodne z „foton ≡ Ø”: nie da się o nim powiedzieć nic poza relacją do otoczenia.
- Zastrzeżenie: 2,4 dekady gęstości; nie wyklucza zaniku rozmycia przy gęstościach o rzędy wielkości większych.

**Otwarte [?]:** „pole = struktura, w której wzbudzenia są możliwe” nie odróżnia pól. **Prowadzone w „Dalej otwarte” → „Co odróżnia pola”.**

**17. ODLEGŁOŚĆ PRZESTRZENNA Z PORZĄDKU — DZIAŁA** (`etap0t_overlap.py`). Brakujący składnik z C4a.12, zbudowany i sprawdzony.
- **Definicja [L]** (Boguñá–Krioukov, arXiv:2401.17376 / PRD 110, 024008): dla c we wspólnej przeszłości a i b, z $I(x,y)$ = przedział Alexandrowa: $A=I(a,c)\setminus I(b,c)$, $B=I(b,c)\setminus I(a,c)$, $C=I(a,c)\cap I(b,c)$, a nakładanie przyczynowe $\mathcal{O}=\frac{N[C]}{\min(N[A],N[B])+N[C]}$ (objętości → **liczby elementów**, korespondencja liczba–objętość). W d=2 odwraca się dokładnie: $d=\tau_c\frac{1-\mathcal{O}}{\sqrt{\mathcal{O}}}$. Wybór c też wewnętrzny: filtr $|N[A\cup C]-N[B\cup C]|<\tfrac12\sqrt{N[A\cup C]+N[B\cup C]}\sqrt{1-\mathcal{O}}$.
- **Zdanie do upadku:** oszacowana odległość zgadza się z prawdziwą, a błąd względny maleje z gęstością.
- **Wynik (d=2, a i b w t=0,8, okno $0{,}25<\tau_c<0{,}45$, 3 ziarna, do 2500 kandydatów c):** z $\tau_c$ liczonym **z objętości** ($V=\tau^2/2$, czyli $\tau=\sqrt{2N[I]/\rho}$): błąd 6,6% → 6,4% → **3,5%** dla l=0,1 i 5,3% → 2,9% → **2,4%** dla l=0,2 przy N = 2000/4000/8000. **PRZESZŁO.**
- **Z $\tau_c$ z długości łańcucha** ($\tfrac12\alpha_1\rho^{-1/2}(n(c,a)+n(c,b))$, α₁=1/√2) błąd stoi na 13–19% i nie maleje — bias estymatora łańcuchowego ($\rho^{(\beta_d-1)/(d+1)}$) przy krótkich łańcuchach. **Do użytku: wersja objętościowa.**
- **Gdzie to teraz wstawić:** (i) C4a.15 — d liczone ze współrzędnych, jedyne miejsce, w którym suma Fokkera nie jest jeszcze wewnętrzna; (ii) warstwa wokół stożka w C4a.11 (trzecia opcja, której nie miałem); (iii) wagi pętli (Pellegrin) i wybór otoczenia dla fragmentów (C4a.8).
- **Zastrzeżenia:** d=2; ρ i d wchodzą jako znane (tak samo jak w estymatorze łańcuchowym); stożki obcięte przez brzeg pudła — stąd okno na τ_c.

**18. SUMA FOKKERA W CAŁOŚCI Z PORZĄDKU — i dwa błędy, które się znosiły** (`etap0u_fokker_wewn.py`). Podmiana ostatniego wejścia ze współrzędnych (d) na miarę z C4a.17.
- **Uwaga do sformułowania:** sama suma S była już wewnętrzna (s² z najdłuższego łańcucha, waga z t_P). Ze współrzędnych pochodziło **odniesienie** R = S·d/τ. Ten krok czyni wewnętrznym **test**.
- **Test 1 (miara zgadza się z prawdą) — PRZESZŁO:** d z porządku wobec **niezmienniczej odległości prostopadłej** (supremum po elementach przestrzennych): +9,2% / −6,7% / +12,8% / +3,7% (N=1200 i 2400, po 2 ziarna). **Poprzednie porównanie było z odległością równoczasową** (0,16 wobec 0,20) — to była zła wielkość odniesienia, nie błąd miary.
- **POPRAWKA NORMALIZACJI:** warstwa {0 ≤ s² ≤ Δ} to **połowa** szerokości, w której rozkłada się δ(s²) — druga połowa (s²<0) to pary przestrzenne, których nie zliczamy. Poprawna waga: $(\alpha t_P)^2/(2\Delta)$, nie $/\Delta$.
- **Test 2 (R rzędu 1) — PRZESZŁO:** po obu poprawkach ekstrapolacja przy Δ/d²→0 daje **R′ = 1,00** (przewidywanie ciągłe: dokładnie 1).
- **Test 3 (zbieżność po Δ/d²) — PRZESZŁO:** wykładnik −0,219 (wcześniej −0,23), rozrzut 10,6% wobec 3,8% — zgodne z ~10% błędem samej miary d i dwoma ziarnami na punkt.
- **Dwa błędy się znosiły:** wcześniejsze R(0)=1,25 = (za małe d) × (za duża waga). Po poprawieniu obu wychodzi 1,00. Reguła z §E w działaniu.
- **Stan:** **każdy składnik pochodzi z porządku** — s² z najdłuższego łańcucha, waga z $t_P$, odległość z nakładania przyczynowego. Brak wejścia ze współrzędnych. Zakotwiczenie na źródłach + normalizacja miarą + odległość z porządku odtwarzają ciągłą wartość τ/d.
- **Zastrzeżenia:** d=2; 2 ziarna na punkt; N ≤ 2400; linie świata = najdłuższe łańcuchy (wędrują, stąd rozrzut d).

**19. Czy „superekstensywność” pętli to też błąd normalizacji? — CZĘŚCIOWO** (`etap0v_petle_gpu.py`).
- **Rachunek wymiarowy przed liczeniem:** działanie ∫F²dV ma wymiar F²L²; pętla niesie fazę F·Σ, Σ ma L², więc (F·Σ)² ma F²L⁴ → **waga musi mieć wymiar L⁻², czyli być ∝ ρ**. Bez swobody wyboru potęgi.
- **Zdanie do upadku:** ρ·Σ_p Σ_p² po minimalnych pętlach nie zależy od N.
- **Rodzina pętli:** minimalna — para p≺q, której przedział ma **dokładnie 2 elementy**, wzajemnie nieporównywalne; Σ = pole czworokąta. (Pellegrin liczy pętle z linków po wszystkich czwórkach — rodzina dużo liczniejsza.)
- **Wynik (d=2, N=600…4800, 0,9 dekady, 2–3 ziarna):** liczba pętli ~ **N^1,221**, suma ważona ~ **N^0,226**. Nachylenia lokalne maleją: 0,34 (2400→3600), 0,14 (3600→4800).
- **DUŻY PRZEBIEG (użytkownik, GPU, N=1200…38400, 1,5 dekady, 3 ziarna) — ROZSTRZYGNIĘTE: to LOGARYTM.** ρ·ΣΣ² = 2,93 / 3,51 / 4,13 / 4,71 / 5,30 / 5,84; **przyrosty na podwojenie N: 0,58 / 0,62 / 0,58 / 0,59 / 0,54 — stałe**, czyli $\rho\sum\Sigma^2 \approx 0{,}84\ln N - 3{,}0$. Malejące nachylenia log-log (0,261 → 0,140) to sygnatura logarytmu, nie potęgi zbiegającej do zera. **Liczba pętli rośnie jak N·ln N** (na element: 2,13 / 2,40 / 2,76 / 3,10 / 3,46 / 3,81).
- **Źródłem są nieograniczone pchnięcia, nie ultrafiolet.** Kontrola: **linków na element** 4,90 / 5,78 / 6,25 / 7,12 / 7,75 (N=600…9600) — przyrost ~0,7 na podwojenie, **też logarytm**; mediana wydłużenia linku (u/v, miara pchnięcia) rośnie 15 → 55, czyli ~N^0,45.
- **WNIOSEK [H]: tego logarytmu nie usunie żadna reguła jednocześnie wewnętrzna dla porządku i niezmiennicza.** Przy ustalonej objętości przedziału **porządek nie odróżnia pary wydłużonej od nierozciągniętej** — dwuelementowy przedział wygląda identycznie niezależnie od pchnięcia. To jest niezmienniczość Lorentza. Odcięcie skrajnych pchnięć wymaga wskazania geodezyjnej, czyli **układu odniesienia z zewnątrz**.
- **Dlaczego Fokker wyszedł, a pętle nie:** w C4a.14/15/18 **układ odniesienia dostarczają same linie świata** — sumujemy po parach zaczepionych na dwóch trajektoriach, więc zakres pchnięć jest ograniczony. W sumie po pętlach nie ma żadnej trajektorii. **Cięcie musi przyjść od trajektorii, czyli od źródła** — to samo, co Johnston nazywa „odfiltrowaniem reszty wszechświata”, i to samo, czego wymaga lokalne otoczenie Boguñy–Krioukova (wybór geodezyjnej). Nie jest to obejście skali Sorkina, tylko ta sama rzecz nazwana inaczej.
- **Zgodne z regułą z §E:** logarytm = miejsce, w którym potęga t_P nie wystarcza i konieczne jest cięcie.

**20. CO ODRÓŻNIA CZĄSTKĘ OD SZUMU TŁA — podłoga szumu zmierzona** (`etap0w_rama.py`). Pytanie użytkownika: w rygorze relacyjnym źródło nie może być wetknięte z zewnątrz; musi być lokalną asymetrią wewnątrz grafu. Co czyni zagęszczenie relacji trwałym węzłem, a nie szumem?
- **Stan literatury [L]:** cząstka jest tam wstrzykiwana tak samo. Modele „swerves” (Dowker–Henson–Sorkin 2004; Philpott–Dowker–Sorkin 2009) zakładają trajektorię i regułę kontynuacji zachowującą pęd; dyskretność daje losowe zbaczanie → niezmiennicza dyfuzja w przestrzeni fazowej. Modele wewnętrzne (Philpott) używają najdłuższych łańcuchów jako geodezyjnych; autorka pisze, że żaden nie próbuje być realistyczny. **Kryterium cząstki nie istnieje.**
- **Kandydat na kryterium [H] (z C4a.19):** cząstka = **lokalne, trwałe ograniczenie zakresu pchnięć**, czyli struktura dostarczająca własną ramę. Tożsamość = trwałość ramy, pęd = jej orientacja, zdolność do oddziaływania = to, że rama czyni sumy skończonymi.
- **Pomiar podłogi szumu (d=2, N=2000/4000/8000, 3 ziarna):** błądzenie poprzeczne najdłuższego łańcucha, mierzone niezmienniczo jako odległość prostopadła punktu od cięciwy okna o m krokach. **Zdania do upadku postawione przed rachunkiem: 1/2 (dyfuzja położenia), 3/2 (swerves), 2/3 (geodezyjna KPZ).**
  - Wykładnik wobec m: **0,68 / 0,63 / 0,72** (po odrzuceniu skrajnego okna sięgającego połowy łańcucha, gdzie działa przypięcie końców). **2/3 = 0,667 trafione; 1/2 i 3/2 odpadają.**
  - Niezależna kontrola: przy ustalonym m odchylenie maleje jak **N^(−0,50)**, czyli ∝ t_P. Razem: $r\approx c\,\tau^{2/3}t_P^{1/3}$, czyli **$r/\tau\approx c\,(t_P/\tau)^{1/3}$**. Wykładnik 1/3 = **β₁ z Boguñy–Krioukova** — dwa niezależne rachunki trafiają w tę samą liczbę.
- **Wniosek:** **tło samo utrzymuje ramę asymptotycznie.** Nie trzeba nic wstrzykiwać, by mieć trwały kierunek — wystarczy łańcuch, przy τ ≫ t_P (ta sama granica co dla lokalnego otoczenia BK). **Ale to daje ramę, nie cząstkę:** łańcuch przechodzi przez każdy element, więc rama jest własnością tła, nie czegoś wyróżnionego.
- **Co musiałaby mieć cząstka [H][?]:** ramę **wyróżnioną** — ograniczać pchnięcia w swoim otoczeniu **mocniej niż tło**. Mierzalne: rozkład wydłużeń linków wokół kandydata ma mieć ograniczony ogon, podczas gdy w tle mediana rośnie jak N^0,45 (C4a.19). To jest następny test.
- **Rozbieżność z literaturą [A]:** swerves wkładają dyfuzję prędkości regułą dynamiczną (3/2); wewnętrzny najdłuższy łańcuch błądzi z wykładnikiem 2/3.

**21. OGON SĄSIEDZTWA — podłoga szumu dla „wyróżnionej ramy”** (`etap0x_ogon.py`). Uwaga użytkownika: przełożenie tego na macierz C nie jest trywialne, bo szuka się **defektu topologicznego w rozkładzie linków**. **Kluczowe [H]:** wydłużenia (pchnięcia) **nie ma w C** — przy ustalonej objętości przedziału porządek nie odróżnia linku wydłużonego od nierozciągniętego; elongacja u/v z C4a.19 była podpórką ze współrzędnych. Pchnięcie jest **relacją**, więc „ograniczony ogon” da się sformułować tylko względem czegoś, co kandydat sam dostarcza.
- **Kryterium bez importu:** dla łańcucha A i elementów x połączonych z nim **linkiem** liczymy d(A,x) miarą z nakładania przyczynowego (C4a.17) — wszystko z porządku: łańcuch, linki, odległość. Jednostka: $t_P$ (w bezwzględnych i tak wszystko maleje).
- **Zdanie do upadku:** ogon rozkładu $d(A,x)/t_P$ rośnie z gęstością (oczekiwane ~N^0,2 z elongacji N^0,45).
- **Wynik (d=2, 2 ziarna, ~70 elementów x na punkt):**

| N | mediana d/t_P | p75 | p90 | max |
|---|---|---|---|---|
| 1000 | 4,26 | 10,33 | 15,14 | 19,9 |
| 2000 | 5,45 | 10,41 | 17,06 | 35,2 |
| 4000 | 5,58 | 12,68 | 21,72 | 36,3 |

  Wykładniki: mediana **N^0,20**, p90 **N^0,26**. **PRZESZŁO.** Sąsiedztwo linkowe rozciąga się na coraz więcej długości Plancka, ~N^(1/4).
- **WNIOSEK [H]: w statycznym sprinklingu cząstki być nie może.** Cząstka musiałaby mieć ogon **ograniczony w jednostkach t_P**, czyli ustalony zasięg sąsiedztwa niezależny od gęstości — to lokalne złamanie niezmienniczości pchnięć. Sprinkling Poissona jest niezmienniczy z konstrukcji, więc każda struktura dziedziczy tę niezmienniczość; taka konfiguracja może wystąpić tylko przypadkiem, z prawdopodobieństwem malejącym z gęstością. **Źródło musi pochodzić z reguły łamiącej niezmienniczość lokalnie — z dynamiki wzrostu (asymetria kosztu rozszerzeń), nie z gotowego sprinklingu.**
**22. SKANER NIEWYPEŁNIALNYCH CYKLI — podłoga szumu dla „defektu topologicznego”** (`etap0y_skaner.py`).
- **Definicje (tylko porządek):** ściana = przedział p≺q o **dokładnie dwóch wzajemnie nieporównywalnych** elementach (kwadrat p→x→q←y←p); β₁ = E − V + składowe (ranga przestrzeni cykli grafu linków); **D = β₁ − F**.
- **Dwie obserwacje strukturalne [A]:** (i) **korona z czterech linków jest niewypełnialna automatycznie** — element w pasie złamałby definicję linku, więc to nie jest osobny warunek; (ii) **trójkątów nie ma**: jeśli x→y→z są linkami, to x→z linkiem być nie może.
- **Wynik (d=2, 2 ziarna, N=500…4000):**

| N | linków/el | ścian/el | β₁/el | **D/el** | koron/el |
|---|---|---|---|---|---|
| 500 | 4,70 | 1,52 | 3,70 | **2,19** | 4,21 |
| 1000 | 5,47 | 2,01 | 4,48 | **2,47** | 5,47 |
| 2000 | 6,22 | 2,40 | 5,22 | **2,82** | 6,83 |
| 4000 | 6,85 | 2,68 | 5,85 | **3,16** | 7,67 |

  (Kolumna koron **poprawiona** — poprawka 60; pierwotne wartości 6,27 / 8,09 / 10,07 / 11,33 były zawyżone. D nie było dotknięte.)

  Przyrosty D/el na podwojenie N: 0,28 / 0,36 / 0,34 — stałe → **logarytm: D/N ≈ 0,47·ln N − 0,73**.
- **Wniosek:** **gęstość defektów też nie jest skończona** — topologia grafu linków dziedziczy ten sam logarytm pchnięć co C4a.19 (cykle powstają głównie z par silnie wydłużonych). **Defekt nie może być zdefiniowany jako sama obecność niewypełnialnego cyklu**; musi być **nadwyżką ponad 0,47·ln N na element**. To jest teraz konkretna podłoga do porównań dla każdej dynamiki.
- **Dwie tożsamości z definicji linku (sprawdzone co do sztuki na CPU) [A]:** (a) przedział dwuelementowy jest ścianą ⇔ $(C^3)[p,q]=0$ (brak ścieżki długości 3); (b) dwa różne następniki linkowe tego samego elementu są **zawsze** nieporównywalne (gdyby b₁≺b₂, a→b₂ nie byłoby linkiem), symetrycznie poprzedniki — więc **liczba koron = Σ_{a₁<a₂} C(M,2), M = L·Lᵀ**. Usuwa to wszystkie pętle; wersja GPU: `etap0y_skaner_gpu.py`. Na 300 parach na punkt: 0 naruszeń obu założeń.
- **DUŻY PRZEBIEG GPU (użytkownik, A100, N=1000…32000, 1,5 dekady, 3 ziarna, `etap0y_skaner_gpu.py`):**

| N | linków/el | ścian/el | β₁/el | **D/el** | koron/el |
|---|---|---|---|---|---|
| 1000 | 5,467 | 1,910 | 4,468 | 2,558 | 5,428 |
| 2000 | 6,276 | 2,406 | 5,277 | 2,870 | 7,039 |
| 4000 | 6,891 | 2,674 | 5,892 | 3,218 | 7,840 |
| 8000 | 7,557 | 3,014 | 6,557 | 3,542 | 8,786 |
| 16000 | 8,250 | 3,368 | 7,250 | 3,882 | 9,895 |
| 24000 | 8,683 | 3,591 | 7,683 | 4,092 | 10,736 |
| 32000 | 8,949 | 3,715 | 7,949 | 4,234 | 11,111 |

  - Dopasowania: linków/el ≈ **0,99·ln N**, ścian/el ≈ **0,51·ln N**, **D/el ≈ 0,49·ln N** (przyrosty 0,31–0,36 na podwojenie, najstabilniejsze w tabeli), koron/el ≈ 1,58·ln N (najbardziej zaszumione).
  - **Kontrola wewnętrzna:** przy jednej składowej β₁ = E − N + 1, więc β₁/el = linków/el − 1 — zgadza się w każdym wierszu.
  - **Podłoga dla defektów: D/N ≈ ½·ln N** (CPU dawało 0,47, GPU 0,485).
  - **Hipoteza [H][?], zapisana przed sprawdzeniem:** współczynniki są prostymi ułamkami — linki ~ ln N, ściany ~ ½·ln N, D ~ ½·ln N; stosunek D/β₁ schodzi 0,57 → 0,53 i **wygląda, że dąży do ½: asymptotycznie połowa cykli grafu linków jest niewypełnialna.** Do weryfikacji analitycznej.
  - Źródło: ln N = 2·ln(ℓ/t_P) — zakres pchnięć od skali Plancka do rozmiaru diamentu.
- **PRAWDZIWA RANGA NAD GF(2)** (`etap0z_gf2.py`). Kompleks: elementy, linki, ściany. Niewypełniona część = β₁ − rank(∂₂); bez komórek 3-wymiarowych rank(∂₂) = F − dim H₂, więc **D_prawdziwe = D_górne + dim H₂**. Eliminacja rzadka (pivot = najmniejszy indeks linku), 2 ziarna, N=500…6000; czas pomijalny (6 s przy 6000).

| N | β₁/el | F/el | ranga ścian / F | dim H₂/el | D_górne/el | **D_prawdziwe/el** | D_prawdz./β₁ |
|---|---|---|---|---|---|---|---|
| 500 | 3,70 | 1,52 | 0,873 | 0,19 | 2,19 | **2,38** | 0,64 |
| 1000 | 4,48 | 2,01 | 0,858 | 0,29 | 2,47 | **2,75** | 0,62 |
| 2000 | 5,22 | 2,40 | 0,865 | 0,32 | 2,82 | **3,15** | 0,60 |
| 4000 | 5,85 | 2,68 | 0,862 | 0,37 | 3,16 | **3,53** | 0,60 |
| 6000 | 6,28 | 2,90 | 0,859 | 0,41 | 3,38 | **3,79** | 0,60 |

  - **Przewidywanie „H₂ małe” — UPADŁO:** ~**14% ścian jest zależnych** (tworzą zamknięte powierzchnie); ranga ścian = **0,86·F**, stała przy każdym N. Górne oszacowanie było zaniżone o stały procent ścian.
  - **Hipoteza „połowa cykli niewypełnialna” — UPADŁA:** prawdziwy stosunek D/β₁ stabilizuje się na **0,60** (0,603 / 0,605 / 0,603 dla N=2000/4000/6000). ½ było artefaktem górnego oszacowania.
  - **GPU, N=16000…32000 (użytkownik, A100, 2 ziarna, `etap0z_gf2_gpu.py`; eliminacja GF(2) ≤ 1 s, GPU ≤ 15 s):**

| N | β₁/el | F/el | ranga/F | dim H₂/el | D_górne/el | D_prawdz/el | D/β₁ |
|---|---|---|---|---|---|---|---|
| 16000 | 7,261 | 3,37 | 0,857 | 0,482 | 3,887 | 4,369 | 0,602 |
| 24000 | 7,696 | 3,60 | 0,854 | 0,524 | 4,096 | 4,620 | 0,600 |
| 32000 | 7,942 | 3,72 | 0,857 | 0,531 | 4,223 | 4,754 | 0,599 |

    Zdania zapisane przed przebiegiem: **(a) ranga/F = 0,86±0,01 — PRZESZŁO**; **(b) D/β₁ = 0,60±0,01 — PRZESZŁO**; **(c) przyrost ~0,39 na podwojenie — PRZESZŁO w średniej** (krótkie odcinki: 0,429 i 0,323; pełny zakres 2000→32000: **0,402**; 500→32000: **0,396**). D/β₁ w zakresie 0,599–0,605 dla wszystkich pięciu N od 2000 do 32000.
    **Obserwacja POST HOC [?] (nieprzewidziana — dopasowanie do znanej liczby, reguła z §E):** ranga/F ≈ 0,857 ≈ **6/7**; jeśli F/β₁ → **7/15** (zmierzone 0,464–0,468; 7/15 = 0,467), to D/β₁ = 1 − (6/7)(7/15) = **3/5** ściśle. Nie jest to wynik; do sprawdzenia analitycznie albo jako zdanie przewidziane przed następnym przebiegiem.
  - **TEST „TRADYCYJNY” (zdania zapisane przed rachunkiem, `etap0z_geometria.py`).** Zmiana tego, co mogło obalić obserwację: **geometria obszaru** (diament, kwadrat w (t,x), szerokie pudło 2×0,5). Zdania przy N=8000: ranga/F = 6/7±0,01; F/β₁ = 7/15±0,01; D/β₁ = 3/5±0,01.

| geometria (N=8000, 2 ziarna) | ranga/F | F/β₁ | D/β₁ |
|---|---|---|---|
| diament | 0,8545±0,0050 | 0,4638±0,0046 | 0,6037±0,0016 |
| kwadrat | 0,8614±0,0014 | 0,4613±0,0007 | 0,6026±0,0001 |
| szerokie | 0,8606±0,0002 | 0,4588±0,0038 | 0,6052±0,0032 |

    - **Wszystkie trzy zdania PRZESZŁY we wszystkich trzech geometriach.** Przy N=4000 szerokie pudło było jeszcze poza pasmem (F/β₁=0,445; D/β₁=0,616) — efekt skończonego rozmiaru, najsilniejszy przy największym zakresie pchnięć.
    - **Wynik mocny: UNIWERSALNOŚĆ** — trzy stosunki nie zależą od kształtu obszaru (różnice ≤0,007 przy N=8000). Własność struktury grafu linków, nie diamentu.
    - **Dokładność ułamków — NIEROZSTRZYGNIĘTA.** Pasmo ±0,01 jest szerokie wobec odległości między kandydatami. Drobniej: D/β₁ przy N=8000 siedzi o 0,003–0,005 **powyżej** 3/5; F/β₁ wciąż rośnie z N (diament 0,459 → 0,464 → 0,468 przy 4000/8000/32000). Test ułamków wymaga przewidzenia granicy i zawężenia błędu o rząd wielkości.
  - **TEST UŁAMKÓW Z EKSTRAPOLACJĄ (użytkownik, A100, `etap0z_ulamki_gpu.py`; 3 geometrie × N=2000…32000 × 8 ziaren = 144 przebiegi).** Model ustalony przed rachunkiem: r(N) = r_∞ + c/ln N; werdykt trójstanowy (PRZESZŁO / UPADŁO tylko przy niepewności r_∞ ≤ 0,003).
    - **Formalnie: wszystkie 9 zdań i 3 zdania o uniwersalności — NIEROZSTRZYGALNE** (niepewność r_∞ = 0,0033–0,0067). **Uwaga o projekcie [A]:** 1/ln N obejmuje tylko 0,132–0,096, ekstrapolacja do 0 wzmacnia błędy ~2,7×; pierwsza wersja (N ≥ 8000, pasmo 0,015) była nieosiągalna z konstrukcji — wykryte przy walidacji na CPU, przed przebiegiem.
    - **Odczyt (A), model ustalony:** r_∞ daleko od ułamków — ranga/F ≈ 0,833–0,843 (4σ od 6/7), F/β₁ ≈ 0,503–0,516 (6σ od 7/15), D/β₁ ≈ 0,569–0,576 (5σ od 3/5). Ułamki byłyby wartościami **przechodzonymi** przy N ≈ 20–30 tys., nie granicami.
    - **Odczyt (B), bez modelu:** górne punkty w diamencie i kwadracie stają: F/β₁ 0,4675→0,4675 i 0,4676→0,4680; D/β₁ 0,6002→0,5997 i 0,5999→0,5997 (24000→32000). Szerokie pudło dochodzi z zewnątrz.
    - **ROZSTRZYGNIĘCIE BEZ MODELU: ranga/F nie stoi na 6/7.** Kwadrat: 0,8563 / 0,8556 / 0,8554 (±0,0005); diament: 0,8551 / 0,8564 (±0,0004) → płaskowyż ≈ **0,8556**, o 0,0015 poniżej 6/7 (~3σ). Z tożsamości **D/β₁ = 1 − (ranga/F)·(F/β₁)** (sprawdzenie: 1 − 0,8555×0,4677 = 0,5999): jeśli ranga/F ≠ 6/7, to **7/15 i 3/5 nie mogą być jednocześnie dokładne**. **Trójka ułamków UPADA jako całość (~3σ), niezależnie od modelu ekstrapolacji.** Pojedynczo 7/15 i 3/5 mogą być zbiegami okoliczności.
    - **Co zostaje mocne: UNIWERSALNOŚĆ** przy ustalonym N — przy 32000 rozrzut między geometriami: ranga/F 0,0016; F/β₁ 0,004; D/β₁ 0,002.
    - **Nie wykonano (decyzja):** przebieg na 80 GB (N≈45000) rozstrzygnąłby A kontra B na 2–4σ (przewidywania zapisane: np. diament F/β₁ — A: 0,4695±0,0005, B: 0,4667), ale nie zmienia wniosku o ułamkach; nieopłacalny.
  - **Podłoga dla defektów (zaktualizowana): D/N ≈ 0,57·ln N**, 1,8 dekady (500…32000). Poprzednio: 0,56·ln N (CPU, N ≤ 6000).
  - **Nowa podłoga dla defektów: D/N ≈ 0,56·ln N** (przyrosty 0,37–0,43 na podwojenie). Zgodne z rachunkiem z dwóch stałych: β₁ ≈ ln N, ranga ścian ≈ 0,86·½ ln N → D ≈ 0,57·ln N. Dwie drogi, ta sama liczba.
- **Zastrzeżenie (dla D_górne):** D = β₁ − F to **górne oszacowanie** (ściany mogą być liniowo zależne); prawdziwa ranga wymaga eliminacji nad GF(2) — osobny krok. Także: 2 ziarna, 0,9 dekady, d=2.
- **Pierwotna uwaga (v3.4, użytkownik):** korona Pellegrina jako najmniejszy kandydat; w d=2 magnetycznie pusta — patrz „Dalej otwarte”.

**Stan C4a po punkcie 8:** postać Zurka (log R liniowe w δ i w log s) — zgodna. Wartość nachylenia — zależy od cięcia otoczenia z rozrzutem ~0,2 w pojedynczej realizacji. Deterministyczne cięcie (składowe) daje ~0,9 wzoru przy s≥4 i ~1,2 przy s=1. **Otwarte:** zależność od w dla składowych; N=4800; czy różnica s=1 vs s≥4 jest strukturalna.

**Następny krok (pierwotny):** otoczenie niosące ≥ 2S(S) (pełne w sensie informacyjnym) — wymaga albo obcięcia przywracającego prawo powierzchniowe, albo fragmentów spoza plastra. To jest ta sama przeszkoda co A10 i C1.

**Plan pierwotny przebiegu zapisu (wykonany powyżej):** skan czynnika ściśnięcia s (kowariancja startowa detektora $\mathrm{diag}(s^2/2\omega,\ \omega/2s^2)$, stan czysty). Zdania do upadku:
- $R_\delta$ rośnie z s (kształt porównać z QBM);
- krzywa $I(S:F)/S(S)$ w funkcji ułamka fragmentów niezależna od N;
- przy s=1 wynik powtarza przebieg tła (kontrola).

## C5. Reguła wzrostu — PROJEKT WSTĘPNY [H][A] (v3.4)

**Dlaczego od razu 3+1:** przegląd wymiarowy w §E — w 2D nie ma miejsca na triadę, a przejście krystaliczne w 2D rzędach nie ma odpowiednika w 3+1.
**Dlaczego nie etapami:** sprinkling zakłada gotową czasoprzestrzeń, wzrost sekwencyjny (Rideout–Sorkin) — kolejność narodzin jako czas zewnętrzny. U nas żaden składnik nie jest wcześniejszy (R1a: warunki muszą zachodzić razem). **Jednostka wzrostu musi nieść wszystkie składniki naraz.**

**Kandydat na jednostkę (jeden krok = jeden nowy element x, jednocześnie):**
- **pamięć** — link do własnego poprzednika na łańcuchu (to, co aparat zapisał o sobie);
- **triada** — linki do **trzech elementów, od których informacja dochodzi do x bezpośrednio** (link = relacja bez pośredników = to, co w strukturze odpowiada **światłu**), wzajemnie nieporównywalnych i **niewspółliniowych**;
- **odczyt** — sam x, zawsze teraz; czwarty punkt odniesienia.
Reszta przeszłości x wynika z przechodniości = **informacja rozproszona**; linki = **informacja ostra**.

**Kryterium niewspółliniowości (tylko z porządku):** z odległością z nakładania przyczynowego (C4a.17): trójka zdegenerowana ⇔ d(a,c) = d(a,b) + d(b,c); prawdziwa triada ⇔ nierówność trójkąta ostra. **W 1+1 każda trójka nieporównywalna jest zdegenerowana** — stąd brak płaszczyzny w 2D z konstrukcji.

**Rozstrzygnięcie liczenia (v3.4):** trzeci kierunek nie jest osobnym składnikiem obok odczytu — odczyt (czwarty punkt) poza płaszczyznę triady wypycha **pamięć**, czyli to, że x leży we wspólnej przyszłości triady i kontynuuje własny łańcuch. 3+1 = 3 punkty + 1 punkt odczytu.

**Dwie kontrole (v3.4, z „zmiana = dynamika × pamięć”):**
- **bez pamięci** — nowy element nie ma linku do własnego poprzednika → oczekiwane: struktura płaska;
- **bez dynamiki** — wybór triady deterministyczny, bez swobody → nic się nie produkuje → oczekiwane: struktura periodyczna (kryształ), bez informacji.
Właściwa reguła ma **oba** składniki: swobodę wyboru (produkcja informacji) i link do poprzednika (przechowanie). **Jeśli wersja pełna nie odróżni się od obu kontroli, konstrukcja się nie trzyma.**

**Drugi test (v3.4): modularność.** Czy wyhodowana struktura ma **nietrywialne drzewo modułów** — węzły na kilku skalach naraz, a nie tylko pojedyncze elementy i całość. Miara: moduły przybliżone (ułamek elementów z zewnątrz widzących podzbiór jednakowo). **Podłoga:** sprinkling 3+1 — modułów praktycznie brak (A3a). Kontrole jak wyżej (bez pamięci, bez dynamiki).

**Pierwsze zdanie do upadku:** wymiar wyhodowanej struktury mierzony z porządku (Myrheim–Meyer) zgadza się z 3+1 (w konwencji pliku: 3D + dynamika i pamięć), **bez podawania wymiaru z zewnątrz**. Jeśli nie — reguła jest zła niezależnie od reszty.

**Narzędzia skalibrowane (v3.4, `etap1a_kalibracja.py`):**
- **Estymator Myrheima–Meyera** (ułamek par w relacji → wymiar): na sprinklingach N=4000 daje **2,000 / 2,975 / 3,982** dla d = 2 / 3 / 4. **Przeszło** (± 0,1).
- **Podłoga modułów (bliźniaki):** d=2 — stała (1–2 pary, zgodnie z n⁰); d=3 — zero; d=4 — **pozornie 16–25 par, ale to artefakt brzegu**: ~6 elementów przy „pasie” diamentu bez żadnej relacji ma ten sam pusty klucz. Po ich wyłączeniu: 0–1,5; we wnętrzu 0–0,5 → **w 3+1 prawdziwych bliźniaków praktycznie brak**, zgodnie z $n^{2-d}$. Wniosek metodyczny: moduły liczyć tylko we wnętrzu.

**REGUŁA v0 „sieć trajektorii” — UPADŁA** (`etap1b_wzrost_v0.py`). W trajektorii; w kroku losowa trajektoria i dostaje x nad końcem własnym (pamięć) i nad końcami trzech innych, wzajemnie nieporównywalnych (triada; **wybór asystenta: „najświeższy element innej trajektorii”**). Test niewspółliniowości pominięty. N=2000, 2 ziarna, estymator liczony wewnątrz przedziałów ≥150 elementów.

| reguła | W=16 | W=64 |
|---|---|---|
| pełna | 1,05 | 1,37 |
| bez pamięci | 1,07 | 1,51 |
| bez dynamiki | 1,15 | 1,93 |

- **Wymiar ~1 zamiast ~4**: struktura prawie łańcuchowa; ponad milion dużych przedziałów przy N=2000 — praktycznie brak odstępów przestrzennych.
- **Diagnoza [A]:** „najświeższy element innej trajektorii” = każdy odczyt dostaje **w jednym kroku całą przeszłość** trzech innych; informacja rozchodzi się natychmiast i przechodnio → **nieskończona prędkość światła wbudowana w regułę**; nie ma nic nieodczytanego, więc nie ma przestrzeni. Ten sam kłopot co w klasycznym wzroście sekwencyjnym (zlewanie w porządek prawie liniowy).
- **KOREKTA DIAGNOZY (użytkownik + asystent, v3.4):** **nieskończona prędkość światła jest fundamentem, nie błędem** (foton t=0: emisja i absorpcja są jednym; w porządku — link). Odczyt „najświeższego elementu” realizuje to poprawnie. **Przestrzeń nie zapadła się przez c, tylko przez pełną łączność — wszyscy czytali wszystkich.** Dowód z tabeli: w kontroli bez dynamiki odczyt był **tak samo natychmiastowy**, a wymiar wzrósł do 1,93, bo każda trajektoria czytała stałych sąsiadów. **Skończone c pojawia się dopiero w relacji do aparatu z zegarem:** ile kroków własnej trajektorii mija między kolejnymi odczytami źródła; dalekie źródło w sieci partnerów dochodzi przez wielu pośredników, rozproszone — „ile temu” rośnie, choć nic nie leci wolniej („8 minut” / „6 minut”). **Dla reguły: natychmiastowy odczyt zostaje jako fundament; ograniczamy tylko, KOGO można czytać.** Poprzednie sformułowanie „nieskończona prędkość światła wbudowana w regułę” jako przyczyna porażki — źle postawione.
- **Wskazówka:** najwyższy wymiar daje kontrola **bez dynamiki** (stały krąg sąsiadów, 1,93 przy W=64) — odtworzyła strukturę jednowymiarową. **Wymiar bierze się z tego, KTO może czytać KOGO, nie z samego aktu czytania.** Przy losowych partnerach każdy jest blisko każdego i przestrzeń się zapada.
- **Następny krok [A][?]:** reguła potrzebuje **lokalności**, a „bliskie” nie może być wstawione z zewnątrz. Kandydat: **pamięć partnerów** — trajektoria czyta te, które czytał jej poprzednik, i tylko powoli zmienia ten zbiór; sąsiedztwo staje się częścią zapisu. Otwarte: czy wygeneruje sąsiedztwo trójwymiarowe (a nie jednowymiarowe ani zapadnięte).

**REGUŁA v1 — odczyt natychmiastowy, ale tylko PARTNERÓW (sieć dekoherencji)** (`etap1c_wzrost_v1.py`). W=128, N=6000. Interpretacja (użytkownik): **„nieskończoność prędkości światła jest nieskończona tylko wtedy, gdy nikt nie czyta; gdy ktoś czyta — jest ograniczona”**; to ten sam mechanizm co dekoherencja superpozycji w laboratorium (korelacje splątania „natychmiastowe”, ale bez sygnału; zapis rozchodzi się przez otoczenie lokalnie). **Sieć partnerów = kto dekoheruje kogo.** W fizyce lokalność oddziaływań jest założona — tu musi urosnąć.

| wersja | średnica | opóźnienie vs odległość k | kulka k | estymator z porządku |
|---|---|---|---|---|
| krąg | 32 | **liniowo, 1,30 kroku/krok sieci** | **liniowo** (5, 9, 13…) | 1,83 |
| A trwałe losowe | 5 | rośnie, coraz wolniej | wykładniczo (7, 35, 102) | 1,40 |
| B dziedziczone | 5 | rośnie, coraz wolniej | wykładniczo (7, 37, 100) | 1,43 |

- **Skończone c wyłania się samo**, gdy odczyt jest ograniczony do partnerów — w kręgu opóźnienie idealnie liniowe z odległością. **Wyprowadzone, nie wstawione.**
- **Sieci losowe (trwałe i dziedziczone) = mały świat:** średnica 5 przy 128, brak skończonego wymiaru; dziedziczenie z przesunięciem (q=0,1) nie zdąży przebudować ekspandera.

**Kalibracja „estymator = wymiar sieci + 1” — UPADŁA** (`etap1d_kalibracja_sieci.py`). Sieci wstawione świadomie, trójka partnerów losowana w każdym kroku spośród sąsiadów: krąg 1,81; siatka 11×11 **1,66**; sześcian 5×5×5 **1,51** (oczekiwane 2, 3, 4). Dodatkowo: 11×11 przy 12 odczytach/traj. 2,32, przy 50 — 1,81 (zapętlenie informacji działa); 24×24 przy 9 — 2,11 (większa siatka nie ratuje).
- **Przyczyna [A]:** estymator Myrheima–Meyera jest wyprowadzony dla **sprinklingu w Minkowskim** (stożki kuliste). Porządek hodowany na siatce ma stożki o kształcie siatki — wzór go nie opisuje. Krąg dał ~2 prawdopodobnie tylko dlatego, że w 1D stożek jest odcinkiem.
- **ROZDZIELENIE POMIARÓW (ustalone przed dalszym liczeniem):** (1) **wymiar sieci dekoherencji** — z wzrostu kulek w sieci partnerów (działa: krąg → 1); (2) **estymator z porządku** — nie mierzy tego wymiaru, tylko sprawdza, **czy porządek jest lorentzowski** (niezmienniczy względem pchnięć). Na siatce z definicji nie jest.
- **Warunek dla dobrej reguły:** **oba naraz** — kulki ~k³ **i** estymator ~4. To jest ryzyko kryształu widziane z drugiej strony: ustalona sieć daje wymiar, ale traci niezmienniczość.

**WOLNE WYBORY — zasada (użytkownik + asystent, v3.4):** zdanie obalające musi dotyczyć **konkretnej** reguły z ustalonymi parametrami. Dopóki reguła zawiera wybory, których rama nie narzuca, porażka obciąża wybór, nie tezę. Zdanie obalające tezę „3+1 z triady i odczytu” da się postawić dopiero dla reguły, w której każdy wybór jest wyprowadzony albo przeskanowany i pokazany jako nieistotny. Użytkownik: *„dopóki są drogi i pomysły, które mają logiczny sens — róbmy swoje; gdy się skończą, zatrzymamy się i przemyślimy całość”.*
- **v1 — wolne wybory:** W=128 (stałe), sieć startowa losowa, reguła zmiany partnerów, q=0,1, niewspółliniowość pominięta.

**v2 „czworościan i narodziny”** (`etap1e_wzrost_v2.py`): start z czworościanu, narodziny na ścianach brzegowych (każda ściana ≤ 2 czworościany — „smak −1” Bianconi), odczyt = pozostałe wierzchołki losowego własnego czworościanu. **Kulki identyczne z pamięcią i bez niej** — sieć rośnie wyłącznie przez narodziny, które nie patrzą na odczyty: **geometria odłączona od czasu**; taka reguła nie może sprawdzić tezy. Sieć za mała (W=315, średnica ~5), estymator 1,84.

**v3** = v2 + narodziny tylko na ścianach o **wzajemnie nieporównywalnych** końcach: **ZAKLESZCZENIE** (4 trajektorie). Pierwszy odczyt w czworościanie wyrównuje informację; nieporównywalnej triady już nigdy nie ma. W ramie: **„wszystko stoi”** — odczyt wyrównuje szybciej, niż cokolwiek produkuje. **Narodziny muszą być skokiem Ø → A (nowa trajektoria świeża, pusta przeszłość), nie odczytem.**

**Obraz krawędzi (użytkownik, v3.4) — STATUS: [H] PRZESKOK, NIEWYPROWADZONY** (użytkownik: „nie doszedłem do tego krok po kroku logiką relacyjną; to raczej hipoteza, nie mam spójnego obrazu”). Reguły v4 i v5 zbudowane na nim **dziedziczą tę niepewność**: „naszą” chwilę zero przesuwamy na krawędź rozszerzającego się wszechświata. **Z tyłu** — istniejąca struktura, określone otoczenie. **Z przodu** — relacji przestrzeni nie ma, wszędzie Ø; w tę stronę możliwa jest inflacja. Patrząc na krawędź, patrzymy na to, co było „przed” naszą chwilą zero. ~~**Wniosek [A]:** hiperboliczność przy krawędzi jest **wymagana** (inflacja), nie jest porażką~~ — **WYCOFANE (poprawka 70).** Uczciwie tylko warunkowo: **jeśli** hipoteza frontu jest prawdziwa, hiperboliczność przy krawędzi jest z nią zgodna. **Bez niej wynik literatury (wzrost na brzegu → mały świat) obowiązuje jako negatywny.** Pytanie o płaskie wnętrze pozostaje, ale jako pytanie w obrębie hipotezy.

**v4** (`etap1f_wzrost_v4.py`): narodziny na brzegu, **świeże**; relaksacja wnętrza (q: partner → partner partnera). **Przewidywanie „stare trajektorie przy q>0 rosną wolniej” — UPADŁO, w przeciwną stronę:** przy q=0,3 kulka 2-krokowa starych obejmuje 370–420 z ~730 (bez relaksacji 98–133) — **zastępowanie partnerem partnera tworzy skróty, wnętrze się zapada**. Ponadto **stare trajektorie mają ~14 sąsiadów, młode 4 — huby** (narodziny ciągle doklejają się do ścian zawierających stare węzły; mechanizm sieci bezskalowej u Bianconi). **Niezgodność z obrazem:** brzeg geometryczny sieci zawiera stare, już odczytane wierzchołki; **krawędź w ramie to front INFORMACYJNY** — elementy jeszcze nieodczytane.

**v5** = v4 bez relaksacji + narodziny tylko na ścianach, których **wszystkie trzy końce są nieodczytane**: **ZAKLESZCZENIE** (4 trajektorie). Pojedyncze narodziny tworzą **jeden** świeży koniec, a ściana dla kolejnych potrzebuje **trzech** — z jednego świeżego elementu front się nie odtwarza; odczyt zjada go szybciej.
- **Wniosek [H][A]:** skok Ø → A musi wnosić świeżość co najmniej w tempie, w jakim odczyt ją zużywa. Zgodne z „wszystko musi zajść jednocześnie, żeby było coś”: **najmniejsze „coś” = cały czworościan** (triada + odczyt), więc skok Ø → A powinien tworzyć **od razu cały czworościan świeżych elementów**, przyłączony do frontu — nie pojedynczą trajektorię.

**REGUŁA R2 — partnerzy przez odległość z porządku (wybór użytkownika: stałe W, bez narodzin)** (`etap1e_wzrost_r2.py`). Start: korzeń + W=128 nieporównywalnych; w kroku losowa trajektoria i; kandydaci = końce innych, nieleżące w przeszłości końca i; triada = trzej najbliżsi wg nakładania przyczynowego; odczyt nad końcem własnym i triadą. **Wolne wybory zapisane przed rachunkiem:** start z korzeniem; W=128; nakładanie względem **całej** przeszłości (nie okna wspólnego przodka jak u BK); remisy losowo. **Ryzyko zapisane:** zamknięcie w izolowanych grupach.

| wersja | średnica sieci odczytów | średni stopień | estymator z porządku |
|---|---|---|---|
| odległość (cała przeszłość) | 2 | 78 | 1,10 |
| bez pamięci | 2 | 77 | 1,10 |
| bez dynamiki | 2 | 75 | 1,11 |
| losowi partnerzy | 2 | 83 | 1,20 |
| okno 1W / 2W / 4W | 2 / 2 / 2 | 78 / 78 / 77 | 1,12 / 1,13 / 1,11 |

- **R2 nie odróżnia się od losowego wyboru**; zamiast izolowanych grup — **pełne ujednolicenie**. Zdanie (2) (skończona średnica, kulki potęgowe) **UPADŁO** we wszystkich wersjach, także z oknem.
- **Diagnoza 1:** czytanie **zmniejsza** odległość — odczyt partnera wnosi całą jego przeszłość, więc zbliża do wszystkich, których on czytał; nakładanie nasyca się do ~1. Zgodne z definicją czasu: stary zapis jest rozproszony i dotyczy wszystkich po równo; bliskość niesie tylko świeży.
- **Diagnoza 2 (po oknach, rozstrzygająca):** problem jest w **starcie**. Symetryczny start = wszystkie odległości równe → pierwsze wybory losowe → mały świat w ~log W rund → od tej chwili nawet świeży zapis dociera wszędzie w kilka kroków, każde okno nasycone. **Odległość z porządku może WZMOCNIĆ lokalność, która już jest, ale nie może jej STWORZYĆ z symetrycznego startu.** Utrzymała się tylko lokalność wstawiona z góry (krąg, siatka).
- **Obciąża wolne wybory:** symetryczny start oraz **stałe W bez narodzin**.
- **Wniosek [H] (asystent, do potwierdzenia):** w zamkniętym zbiorze trajektorii przestrzeń nie ma skąd się wziąć — informacja zawsze zdąży się wymieszać. **Rozszerzanie** (nowe trajektorie rodzące się przy istniejących, dziedziczące lokalność) wygląda na **warunek**, nie dodatek — zgodnie z tezą użytkownika, że wszechświat cały czas tworzy nowe relacje przestrzenne. Mielizna: to droga Bianconi–Rahmede (hiperboliczność).

**REGUŁA R3 — narodziny trajektorii z dziedziczoną lokalnością** (`etap1g_wzrost_r3.py`, `etap1h_siec_r3.py`). Start: 4 trajektorie wzajemnie partnerami. W kroku losowa trajektoria i; z prawdop. **b narodziny**: x nad końcem i i końcami jej partnerów zaczyna nową trajektorię i′ (partnerzy i′ = i + dwóch partnerów i; i wymienia jednego partnera na i′); inaczej **odczyt**. **Wolne wybory:** start; reguła dziedziczenia; brak zmiany partnerów poza narodzinami; b.

| b | W | średnica sieci | log₂ W | pary końców nieporównywalne | estymator z porządku |
|---|---|---|---|---|---|
| 0,02 | 107 | 6,5 | 6,7 | 0,895 | 1,23 |
| 0,10 | 492 | 11,5 | 8,9 | 0,977 | 1,72 |
| 0,30 | 1520 | 14,5 | 10,6 | 0,988 | 1,92 |
| 0,60 | 2998 | 18,0 | 11,5 | 0,993 | 2,40 |

- **Zdanie 1 (małe b → ujednolicenie) — PRZESZŁO** (estymator 1,23, jak R2).
- **Zdanie 2 (nieporównywalność rośnie z b) — PRZESZŁO:** ułamek i estymator rosną monotonicznie. **Im bardziej tworzenie wyprzedza odczyt, tym mniej ujednolicenia — pierwszy liczbowy ślad tezy o rozszerzaniu.**
- **Zdanie 3 (sieć = mały świat) — pozornie nie przeszło** (średnica rosła szybciej niż log₂ W; łączenie punktów o różnym b sugerowało W^0,31). **Czysty test:** sieć partnerów w R3 **nie zależy od porządku ani od b** (odczyty nie zmieniają partnerstw) — hodowana bez macierzy relacji do W = 256 000: średnia odległość 6,32 / 8,67 / 11,02 / 14,32 / 17,67 dla W = 10³…2,56·10⁵; przyrosty na podwojenie 1,18 / 1,18 / 1,65 / 1,67; dopasowania W^0,185 i 2,05·ln W równie dobre (rozrzut 2,5% / 3,1%). Sieć 3D dałaby ~40. **„d = 3” UPADŁO; sieć prawie małym światem** — mielizna Bianconi–Rahmede potwierdzona. Podpowiedź W^0,31 była złudzeniem małego zakresu.
- **WNIOSEK KONSTRUKCYJNY [A]:** w R3 **kto czyta kogo rozstrzyga losowe dziedziczenie, odcięte od zapisu** — odczyty i b nie mają wpływu na sieć, więc zapis i odczyt **nie mogą kształtować przestrzeni**. Rama wymaga odwrotnie: przestrzeń ma wynikać z tego, co zapisane i odczytane.
- **Następny krok (R4):** przy narodzinach nowa trajektoria wybiera partnerów **spośród sąsiedztwa rodzica, według odległości z porządku** — wtedy b i historia odczytów wpływają na sieć; dopiero wtedy test wymiaru sieci ma sens.

**REGUŁA R4 — partnerzy dziecka wybierani spośród sąsiedztwa rodzica wg nakładania w oknie** (`etap1i_wzrost_r4_gpu.py`). **Infrastruktura (działa, gotowa na następne reguły):** brak macierzy N×N — każda trajektoria trzyma bitset przeszłości w oknie (bufor pierścieniowy; W×R·W bitów: W=128 tys., R=4 → ~8 GB); **okno w rundach** (R·W(t) ostatnich elementów; R2 pokazała, że bliskość niosą tylko świeże zapisy; informacja ~1 krok sieci/rundę → okno R rund widzi promień ~R; skan R=2/4/8 zaplanowany); **bloki = zbiór niezależny w sieci partnerów** (krok Luby'ego) — trajektorie niebędące partnerami nie czytają nawzajem swoich końców, ich kroki są przestrzennie rozdzielone, **kolejność liczenia nic nie znaczy (to nie przybliżenie)**.
**Walidacja na CPU (W ≤ 8000, R=4, 1 ziarno) — wszystkie warianty dają mały świat; A100 NIE użyte:**
- **nakładanie BK** (wspólne / (min(tylko A, tylko B) + wspólne)): śr. odległość 3,5–4,3, **mniej niż R3** — miara daje 1, gdy przeszłość kandydata **zawiera** naszą → wybierane trajektorie o najszerszej przeszłości = **preferencyjne dołączanie do hubów**;
- **Jaccard** (wspólne / suma): 6,85 / 9,21 / 10,67 / 11,59 / 12,30 — na starcie bardziej lokalnie niż R3, ale przyrosty **maleją** (2,36 → 0,71): wolniej niż logarytm. Hubów brak (śr. stopień 6, maks. ~28 stabilne). Mechanizm: kandydaci w **promieniu 2** + rodzic oddaje partnera → linki wydłużają się przypadkowo (skróty jak Watts–Strogatz);
- **promień 1:** 7,4 / 8,3 / 7,6 / 9,3 / 10,5 — w przybliżeniu logarytmicznie.
- **Zdanie Z1 (R4 rośnie szybciej niż R3) — UPADŁO** we wszystkich wariantach już przy małej skali.
- **Wniosek z R3–R4 [A]:** **dołączanie nowych węzłów do istniejących** (losowo, przez odległość, do hubów czy lokalnie) daje sieć bliską małemu światu — zgodnie z mielizną Bianconi–Rahmede.

**R5 — PROPOZYCJA (do sprawdzenia na CPU) [H]:** rozszerzanie to **wstawianie nowych relacji POMIĘDZY istniejące**, nie doklejanie na brzegu (użytkownik: „wszechświat cały czas tworzy nowe relacje przestrzenne”). Narodziny = **wstawienie nowej trajektorii między dwóch partnerów** (rozdzielenie ich połączenia). Z konstrukcji wydłuża odległości; **podział krawędzi zachowuje wymiar struktury startowej** — przy starcie triada + odczyt (najmniejsza struktura 3D) wymiar 3 byłby **dziedziczony, nie wstawiany**, zgodnie z tezą o czterech punktach odniesienia. Zdanie do upadku: średnia odległość ~ W^(1/3).

**REGUŁA R5 — wstawianie POMIĘDZY (podział relacji), sprawdzona na CPU** (`etap1j_r5.py`, `etap1k_r5_warianty.py`). Start: czworościan. Narodziny: losowa relacja (u,v) zostaje rozdzielona — znika u–v, pojawia się w. **Tylko sieć (bez porządku i odczytu).**
- **Pełny podział** (w łączy się z u, v i **wszystkimi** wspólnymi sąsiadami — zachowuje topologię triangulacji): średnia odległość 3,94 → 7,17 dla W = 10³ … 2,56·10⁵, **W^0,11**; **huby** — maks. stopień 118 → 1848 (~W^½): wspólni sąsiedzi zyskują połączenie przy każdym podziale; podział skrajnie nierównomierny. **Zdanie „1/3” UPADŁO.**
- **Wyrównywanie** (dzielona krawędź o najmniejszej sumie stopni): **gwiazda** — jeden węzeł połączony ze wszystkimi, odległość 2. Odrzucone.
- **TRIADA** (w łączy się z u, v i **jednym** wspólnym sąsiadem — dokładnie trzy połączenia): stopnie ograniczone (śr. 3,2; maks. 25 → 56), średnia odległość 14,6 / 28,1 / 58,7 / 123,0 dla W = 10³ … 6,4·10⁴ → **W^0,515 → wymiar ≈ 1,94**. **Niezależny pomiar — wzrost kulek:** **1,96 ± 0,13** (W = 64 tys.), **1,95 ± 0,15** (W = 256 tys.).
  - **Wynik: triada bez pamięci daje płaszczyznę** — struktura dwuwymiarowa bez żadnej geometrii podanej z zewnątrz (start trójwymiarowy, wymiar zszedł do 2).
  - **Zgodność z R1a** („triada bez pamięci jest płaska”, zapisane **przed** rachunkiem) — **zgodność, nie potwierdzenie**: test nie był pod to zdanie zaprojektowany.
- **ZDANIE DO UPADKU NA NASTĘPNY KROK (zapisane przed rachunkiem):** dołożenie **pamięci** (sprzężenie wstawiania z porządkiem i odczytem) podnosi wymiar z 2 do **3** — **oba pomiary razem**: kulki 3 ± 0,2 i odległość ~W^(1/3); **kontrola bez pamięci zostaje przy 2**. Jeśli pamięć niczego nie zmieni — teza „trzeci kierunek z pamięci” ma kłopot na liczbach.

**REGUŁA R6 — pamięć jako czwarty punkt odniesienia (konstrukcja użytkownika)** (`etap1l_r6.py`). **Opis (użytkownik):** (1) płaski trójkąt XYZ; zero absolutne nieosiągalne → boki falują, kurczą się, rozszerzają — dalej płasko; ta zmiana generuje informację = trajektorię (pamięć o tym, jak boki wyglądały przed chwilą); dopiero teraz można mówić o ruchu. (2) X, Y, Z = trzy punkty odniesienia; skumulowana informacja o przeszłości = **czwarty, wirtualny punkt odniesienia = czas**; układ = X, Y, Z + 1 punkt informacyjny.
**Przekład:** start = XYZ + T (czworościan), pamięć ściany XYZ = T; dynamika = rozdzielenie boku a–b ściany (a,b,c) i wstawienie w połączonego z a, b, c (triada, jak R5); **pamięć** = relacja w z punktem pamięci ściany m; nowe ściany: (a,w,c) z pamięcią b (odcięty wierzchołek = „jak wyglądała przed chwilą”), (w,b,c) z pamięcią a.
- **Pierwsza wersja — test nieważny:** wybór miejsca przez losową **ścianę z listy** zamiast krawędzi (jak w R5) → kontrola bez pamięci nie odtworzyła 2D (oba warianty ~wykładnik 0,16, kulki 3,7–3,9). **Błąd asystenta: test różnił się od R5 dwiema rzeczami naraz.**
- **Wersja poprawiona (wybór identyczny z R5; różnica wyłącznie relacja w–m):**

| | wykładnik odległości → wymiar | wymiar z kulek (W=64 tys.) | stopień maks. |
|---|---|---|---|
| bez pamięci (**kontrola = R5, przeszła**) | 0,541 → **1,85** | **2,05 ± 0,15** | 27 → 59 |
| z pamięcią | 0,230 → **4,35** | **3,56 ± 0,22** | 50 → 206 |

- **PAMIĘĆ PODNOSI WYMIAR** z ~2 do 3,5–4,4 — jedyna różnica to relacja z punktem pamięci. **Pierwszy liczbowy ślad konstrukcji: trójkąt z dynamiką płaski, punkt informacyjny dokłada kierunek.**
- **Zdanie „3 w obu pomiarach” — UPADŁO:** kulki 3,56 ± 0,22 (~2,5σ nad 3), odległość 4,35; pomiary niezgodne → wymiar niedookreślony. **Prawdopodobna przyczyna:** punkty pamięci jako **huby** (maks. stopień 50 → 206) — punkt będący pamięcią wielu ścian dostaje połączenie przy każdym wstawieniu → skróty podnoszą wymiar.
- **Poprawka do sprawdzenia:** pamięć = **najświeższy bezpośredni poprzedni stan danej ściany** („jak boki wyglądały przed chwilą”), żaden punkt nie jest pamięcią wielu ścian naraz.

**R6 z pamięcią WYŁĄCZNĄ, NAJŚWIEŻSZĄ — WYNIK** (`etap1m_r6_wylaczna.py`). Ustalenie przed rachunkiem: każdy punkt jest w danej chwili pamięcią **co najwyżej jednej** ściany; nowa ściana, która dostaje już zajęty punkt, **przejmuje go** (najświeższa wygrywa), stara traci pamięć; ściana, w którą wstawiono węzeł, znika i zwalnia swój punkt. Wybór miejsca identyczny z R5. **Zdania do upadku:** z pamięcią 3 w obu pomiarach (kulki 3 ± 0,2; odległość 3 ± 0,3); kontrola 2; stopień maks. nie rośnie potęgowo.

| | wymiar z odległości | wymiar z kulek (W=64 tys.) | stopień maks. |
|---|---|---|---|
| bez pamięci (kontrola) | 1,85 | 2,05 ± 0,15 | ~W^0,19 |
| **z pamięcią (wyłączna, najświeższa)** | **3,11** (wykładnik 0,321) | **3,01 ± 0,18** | ~W^0,21 |

- **WSZYSTKIE ZDANIA PRZESZŁY.** Oba pomiary zgodne (w wersji niewyłącznej nie były) → wymiar dobrze określony. Hubów brak (wzrost stopnia jak w kontroli).
- **Dlaczego mocne:** **wspólny start** — obie wersje od tego samego czworościanu; bez pamięci schodzi do 2. **Trójwymiarowość nie jest odziedziczona po starcie, tylko wytwarzana przez pamięć** (wiązanie każdego nowego odczytu z bezpośrednio poprzednim stanem jego ściany). **To jest dwuetapowa konstrukcja użytkownika w liczbach: triada + dynamika → płaszczyzna; informacja „jak boki wyglądały przed chwilą” = czwarty punkt odniesienia → 3D.**
- **Czego ten wynik JESZCZE NIE mówi:** (1) to wymiar **sieci kto-czyta-kogo**, nie porządku przyczynowego — druga połowa warunku C5 (lorentzowskość porządku) **niepoliczona**; (2) pamięć **kombinatoryczna** (punkt przypisany ścianie), nie wyprowadzona z porządku i odczytu; (3) **wolne wybory:** start z czworościanu, jednostajny wybór krawędzi, reguła przejmowania, pamięć ściany = odcięty wierzchołek; (4) **statystyka:** 2 ziarna, 1,8 dekady, kulki przy jednym W.
- **Następne sprawdzenia:** W do 256 tys. i więcej ziaren; kulki przy kilku W; inny start (czy 3 zostaje); wrażliwość na regułę przejmowania; potem sprzężenie z porządkiem i test lorentzowskości.

**SPRAWDZENIA R6 (tanie, CPU)** (`etap1o_r6_sprawdzenia.py`). Zdania przed rachunkiem: pasmo 3 ± 0,3 w obu pomiarach.
- **Większe W i NOWE ziarna (3, 4), do W = 256 tys. — PRZESZŁO:** wymiar z odległości **3,10**; wykładniki lokalne na kolejnych odcinkach **0,334 / 0,299 / 0,343** (stabilnie ~1/3 przez 2,4 dekady); kulki przy 256 tys. 2,80 ± 0,25.
- **Reguła przejmowania „pierwsza zatrzymuje” — PRZESZŁO:** 2,88 (odległość) i 2,86 ± 0,09 (kulki), zgodnie. Wynik nie zależy od tego, który stan pamięci wygrywa.
- **Płaski start (triangulowany dysk, 127 węzłów, bez punktów pamięci) — NIEWAŻNE:** kontrola bez pamięci dała 2,54 / 2,98 ± 0,47 zamiast 2 (pomiary niezgodne) — prawdopodobnie stan przejściowy (dysk o stopniu 6 → reguła triady prowadzi do ~3,2). Z pamięcią 3,58 / 2,82 ± 0,16 (niezgodne). Nie liczone.

**TEST LORENTZOWSKOŚCI PORZĄDKU — UPADŁ** (`etap1n_lorentz_r6.py`). Porządek z odczytów na ustalonej sieci (każdy krok: losowa trajektoria czyta końce wszystkich sąsiadów + własny); estymator MM w przedziałach między elementami tej samej trajektorii odległymi o k=6 kroków (W=8000, T=16 rund). **Zdania:** R6 → 4 ± 0,3; kontrola R5 → 3 ± 0,3; ostrzeżenie zapisane z góry: na siatce kalibracja MM upadła (stożki o kształcie siatki).
| | przewidywanie | estymator (mediana; średnia) |
|---|---|---|
| R5 (sieć 2D) | 3 ± 0,3 | **2,21**; 2,27 ± 0,12 (22 przedziały, śr. 258 el.) |
| R6 (sieć 3D) | 4 ± 0,3 | **2,33**; 2,44 ± 0,11 (30 przedziałów, śr. 601 el.) |
- **Przyczyna — TWIERDZENIE [L]:** Bombelli–Henson–Sorkin („Discreteness without symmetry breaking: a theorem”, Mod. Phys. Lett. A 24, 2579, 2009; gr-qc/0605006): **nie da się przypisać sprinklingowi grafu o skończonej walencji zgodnie z niezmienniczością Lorentza.** Sieć R6 ma skończoną walencję (~4,3) → porządek z odczytów na niej **z konieczności wyróżnia układ** (spoczynkowy układ sieci). **Błąd asystenta:** zdanie zapisane bez sprawdzenia literatury — upadek był przewidywalny z twierdzenia.
- **DYCHOTOMIA [A]:** **ograniczony, lokalny odczyt** (skończona walencja) dał w R6 **trójwymiarowość**, ale **nie może** dać niezmienniczości Lorentza; **niezmienniczość Lorentza wymaga nieograniczonej liczby bezpośrednich relacji na element** (w sprinklingu linków przybywa bez końca: ~ln N w 2D, ~N^½ w 3+1 — C2, C4a.22). **To, co zrobiło trzy wymiary, jest tym, co zabija niezmienniczość.**
- **FUNDAMENT (użytkownik, v3.4):** **nieskończone c = automatycznie pole EM bez wzbudzeń.** To nie jest następstwo do sprawdzenia, tylko fundament ramy — **musi się rozstrzygnąć na poziomie światła.** Pole EM w próżni i wzbudzenia dające fale EM to **„relacja przestrzeni”**. (Zgodne z łańcuchem Ø: pole bez wzbudzenia ≡ Ø; fala = wzbudzenie = informacja; foton = minimalne wzbudzenie.)
- **PUNKT STARTU NA NASTĘPNĄ SESJĘ:** struktura, w której **relacje nieczytane** (pole bez wzbudzeń, c nieskończone) mają **nieograniczoną walencję** — co daje niezmienniczość Lorentza, zgodnie z twierdzeniem BHS — a **odczyty** (wzbudzenia, c skończone) mają **skończoną walencję** i dają trójwymiarowość jak w R6. Test: czy obie własności współistnieją, gdy wyróżniony układ jest **układem czytającego**, a nie całej struktury.
- **FUNDAMENT (użytkownik, v3.4):** **nieskończone c = pole EM bez wzbudzeń** (Ø od strony światła). To nie jest tylko logiczne następstwo do sprawdzenia — to **fundament ramy**, i dychotomia **musi się rozstrzygnąć na poziomie światła**. **Pole EM w próżni i jego wzbudzenia (fale EM) = relacja przestrzeni.** Konsekwencja dla projektu reguły: strona nieczytana (nieograniczona walencja, niezmienniczość Lorentza) to pole bez wzbudzeń; odczyt (skończona walencja, układ czytającego) to wzbudzenie, czyli foton. Następny krok w C5 zaczyna się od światła, nie od sieci.
- **ROZWIĄZANIE DYCHOTOMII NA POZIOMIE ŚWIATŁA [H] (użytkownik — fragment o klockach i fotonach; odczyt asystenta, v3.4), DO SPRAWDZENIA:**
  - **Foton nie ma w sobie „ile temu”** — od jego strony emisja i absorpcja są jednym; „8 minut” i „6 minut” to dwa położenia czytającego, nie dwie cechy fotonu. Relacja nie wyróżnia układu; układ pojawia się w odczycie.
  - **Relacja nieczytana wiąże źródło z każdym możliwym czytającym** (cały stożek przyszłości) = **nieograniczona walencja**; odczyt wybiera jedno pochłonięcie, jeden aparat, jedno „teraz” = **walencja skończona**.
  - **Dwie strony dychotomii to ta sama relacja przed odczytem i po nim:** pole bez wzbudzeń (nieczytane, bez wyróżnionego układu, c nieskończone) — odczyt (jedna zrealizowana relacja, układ czytającego, c skończone „w relacji do”, z tego odległości i przestrzeń).
  - **Błąd w poprzednim teście:** sieć R6 (warstwa **zrealizowanych odczytów**) potraktowana jak **cały** porządek. Twierdzenie BHS zabrania skończonej walencji **całemu** porządkowi, nie **sieci odczytów** konkretnych trajektorii.
  - **TEST (zapisany przed rachunkiem):** tło = sprinkling 3+1 (wszystkie relacje, nieograniczona walencja, Lorentz z konstrukcji); trajektorie = łańcuchy w sprinklingu; odczyty = wybór, regułą R6 z pamięcią, niewielu linków spośród dostępnych. **Zdanie do upadku:** sieć odczytów ma wymiar **3** (jak R6) **i** porządek, w którym siedzi, pozostaje lorentzowski (estymator **4**) — nic nie usunięte, tylko przeczytane.
- **DEFINICJA c (użytkownik, v3.4): prędkość światła to nie prędkość, z jaką światło pokonuje dystans, tylko prędkość, z jaką światło przekazuje informację.** Zgodne z fizyką bez interpretacji [L]: (1) od 1983 r. **metr jest zdefiniowany przez światło** (droga w 1/299 792 458 s) — dystans jest definiowany przez przekaz informacji, nie odwrotnie; odległość radarowa = czas obiegu sygnału; (2) mierzalna jest tylko prędkość **w dwie strony** (obieg informacji), w jedną stronę — konwencja (Reichenbach); (3) szybciej niż c „poruszają się” bez sprzeczności rzeczy, które **nie przenoszą informacji** (plamka lasera na Księżycu, prędkość fazowa, oddalanie galaktyk przy rozszerzaniu). Zgodne z v1: skończone c wyszło jako tempo przekazu informacji między czytającymi (1 krok sieci / krok odczytu), nic się nie poruszało.
- **Możliwe rozwiązanie w ramie [H][?] (do sprawdzenia, nie wynik):** „c nieskończone, dopóki nikt nie czyta” — nieograniczona walencja należy do **relacji nieczytanych** (strona Ø), skończona do **odczytu**, który jest zawsze odczytem **konkretnej trajektorii**. Wyróżniony układ byłby wtedy **układem czytającego**, nie globalnym — co fizyka dopuszcza. Por. Kent (arXiv:1803.11484): po ustaleniu pary punktów czasowo rozdzielonych wyróżniony kierunek przestrzenny da się zdefiniować nawet dla typowego sprinklingu.

**STAN RAMY PO v3.4 — trzy definicje i dwie drogi do wymiaru (użytkownik):**
1. **Czas** — zgodny z mechanizmem Page'a–Woottersa (czas jako korelacja wewnątrz całości, która sama jest statyczna), z więzem Wheelera–DeWitta i z tym, jak dekoherencja wybiera zapis. Trzy niezależne miejsca w fizyce mówią to samo w innych językach.
2. **c** — jako tempo przekazu informacji: zgodne z definicją metra od 1983 r., z mierzalnością wyłącznie prędkości w dwie strony (Reichenbach) i z tym, co może, a co nie może przekraczać c.
3. **Trzy wymiary** — **struktura logiczna + jeden wynik liczbowy** (R6: triada bez pamięci 2, z pamięcią 3, wspólny start, dwa zgodne pomiary). **Pełnego dowodu brak:** test lorentzowskości upadł, a jego rozwiązanie na poziomie światła jest zapisane, ale niepoliczone.
   - **Droga A (pierwsza): test lorentzowskości — rozwiązanie na poziomie światła** (wyżej).
   - **Droga B (rezerwowa): skala Plancka — dodatkowy stopień swobody ze splatania/rzutowania struktur dwuwymiarowych.** Istniejące koncepcje [L]: **redukcja wymiaru spektralnego do ~2** w skali Plancka (triangulacje przyczynowe, asymptotyczne bezpieczeństwo, Carlip — R3); **zasada holograficzna** ('t Hooft, Susskind: obszar 3D opisany danymi na brzegu 2D, entropia ∝ pole); **przestrzeń z plątania** (Ryu–Takayanagi: entropia splątania ∝ pole; Van Raamsdonk: rozplątanie rozrywa geometrię); **sieci tensorowe** (MERA, Swingle: dodatkowy wymiar jako **skala**, kierunek zgrubiania opisu). **Wspólne [A]:** dodatkowy kierunek pojawia się tam, gdzie pojawia się **relacja między opisami**, a nie nowy byt — zgodnie z R6, gdzie trzeci wymiar wziął się z relacji z poprzednim stanem.

**TEST NA POZIOMIE ŚWIATŁA — WYNIK** (`etap2b_swiatlo_tuba.py`). Tło: sprinkling w tubie (czas × trzy kierunki; **4 punkty odniesienia**, nie „4 wymiary” — pułapka 5), wszystkie relacje obecne, nieograniczona walencja, brak wyróżnionego układu. Trajektorie: łańcuchy (następny element = największy czas własny w oknie τ z gęstości; **indeks komórkowy** zdejmuje ścianę kosztu O(N) na krok). Odczyt: trzy trajektorie o **najświeższym zapisie** (+ pamięć).
- **Poprawka konstrukcji:** pierwsza wersja sklejała odczyty z **całego życia** trajektorii (stopień 22, wymiar 2,42) — przestrzeń to relacja **w danej chwili**, więc sieć bierze się jako **migawka** (po jednym odczycie z każdej trajektorii, ten sam krok).
- **Efekt skończonego rozmiaru:** K=1200 → wymiar 2,63; **K=4000 → 3,01**.

| migawka (K=4000) | wymiar | stopień | profil: prawdziwa odległość przy k=1…7 |
|---|---|---|---|
| najświeższe odczyty | **3,01** | 5,5 | 0,57 0,80 1,07 1,42 1,81 2,23 2,68 |
| losowa (kontrola) | 4,68 | 6,0 | 2,77 3,05 3,13 3,17 3,20 3,22 3,14 — **płaski** |

- **Z1 (wymiar 3 ± 0,3) — PRZESZŁO** (3,01). **Z4 (kontrola losowa: brak korelacji) — PRZESZŁO** (profil płaski). **Z2 (liniowość profilu) — częściowo**: rośnie monotonicznie, ale przyrosty lekko rosną. **Z3 (pamięć) — niezbadane** przy K=4000; przy K=1200 pamięć nie robiła różnicy — sensowne, bo **tu trzy wymiary są już w tle**, więc pamięć nie musi ich wytwarzać (inaczej niż w R6, gdzie tła nie było).
- **PRZEBIEG DUŻY (użytkownik, A100, `etap3b_dwa_zadania_gpu.py`): N = 24 mln, K = 20 000 trajektorii × 31 kroków, 3 ziarna, τ = 0,301.** Budowa trajektorii zrównoleglona na GPU (siatka kubełkowa; **wolny wybór: brak wyłączności elementów** — to ona wymuszała sekwencyjność), wybór trójki najświeższych liczony na GPU. Czas: ~4 s budowa, ~70 s migawka na wariant.

| wariant | ziarna 1 / 2 / 3 | średnia |
|---|---|---|
| **z pamięcią** | 3,01 / 2,97 / 3,04 | **3,01 ± 0,02** |
| bez pamięci | 3,02 / 3,03 / 3,09 | 3,05 ± 0,02 |
| losowa (kontrola) | — | stosunek spada 1,58 → 0,55 |

  - **A1 (wymiar 3 ± 0,1) — PRZESZŁO:** 3,01 ± 0,02.
  - **A2 (stały stosunek odl./krok dla k≥2, ±10%) — PRZESZŁO:** 0,26–0,31 na dwunastu kolejnych k (~±9% wokół 0,285); lekkie wygięcie (spadek w środku, wzrost na końcu).
  - **A3 (pamięć zmienia wymiar o < 0,1) — PRZESZŁO:** różnica 0,04. Potwierdza: w tle mającym już trzy kierunki pamięć nie ma czego wytwarzać.
  - **A4 (kontrola losowa: brak proporcjonalności) — PRZESZŁO mocno:** stosunek spada trzykrotnie.
  - **Kontrola nieplanowana:** przebieg **bez wyłączności elementów** dał ten sam wynik co wersja z wyłącznością (3,03 ± 0,04) → **ten wolny wybór nie ma znaczenia.**
- **ROZWIĄZANIE DYCHOTOMII W JEDNEJ STRUKTURZE [A]:** tło ma **nieograniczoną walencję i niezmienniczość Lorentza z konstrukcji** (nic nie usunięto), a **warstwa odczytów** wycięta z niego regułą „najświeższy zapis” ma **skończoną walencję (5,5) i wymiar 3**. Twierdzenie Bombelli–Henson–Sorkin nie jest złamane: dotyczy **całego** porządku, nie warstwy odczytów. **Skończona walencja i wyróżniony układ należą do czytającego, nie do struktury.**
- **PRZEBIEG PEŁNY (3 ziarna, N=5 mln, K=4000, L=12):** wymiar **z pamięcią 3,10 / 3,02 / 2,98 → 3,03 ± 0,04**; **bez pamięci 3,17 / 3,09 / 3,04 → 3,10 ± 0,04**; kontrola losowa: profil płaski.
  - **Z2 — PRZESZŁO:** stosunek prawdziwej odległości do liczby kroków w sieci jest **stały**: 0,40 / 0,37 / 0,38 / 0,39 / 0,41 / 0,42 dla k = 2…7 → odległość w sieci **proporcjonalna** do przestrzennej (współczynnik ≈ 0,40). Pierwszy krok (0,51) odstaje — rzadkie próbkowanie. Kontrola losowa: ten sam stosunek spada 2,24 → 0,58, brak proporcjonalności.
  - **Z3 — UPADŁO w zapisanej postaci:** bez pamięci wymiar nie jest niższy (3,10 wobec 3,03, różnica ~1,3σ). **Interpretacja:** tu trzy kierunki są już w tle, więc pamięć nie ma czego wytwarzać; w R6 tła nie było i tam pamięć podniosła wymiar z 2 do 3. **Nie są to wyniki sprzeczne: pamięć tworzy wymiar, gdy nie ma go skąd wziąć, i nie dokłada go tam, gdzie już jest.**
- **Zastrzeżenia:** Z3 upadło (patrz wyżej); wolne wybory (T, S, N, K, L, trójka+pamięć, reguła budowy łańcucha, okno τ z 12 kandydatów); wymiar mierzony tylko z kulek.

**DLACZEGO NIE WIĘCEJ WYMIARÓW? [H] (użytkownik) + TEST (`etap1p_r7_wiecej.py`).** Argument użytkownika: wyższy wymiar wymagałby pięciu punktów odniesienia w jednym atomarnym kroku, a odczyt (czas) generuje informację już przy czterech (minimalna pojemność na zmianę i pamięć), więc **nic nie wymaga piątego**; kolejny element będzie węzłem **wewnątrz** istniejącej rozmaitości 3D, nie nową osią. **3D jako strukturalne minimum; co wystarczające, wyznacza granicę.**
**Zastrzeżenie asystenta przed testem:** „nic nie wymaga” ≠ „nie da się”. **Zdanie do upadku:** cztery partnerzy + pamięć dają 4.

| połączenia | wymiar z odległości | wymiar z kulek | stopień |
|---|---|---|---|
| 2 + 1 (triada) | 1,87 | 2,21 ± 0,16 | 3,2 |
| **2 + 1 + pamięć** | **3,24** | **2,81 ± 0,13** | 4,3 |
| 2 + 2 | 5,59 | 3,36 ± 0,16 | 6,0 |
| 2 + 2 + pamięć | 4,92 | 3,23 ± 0,16 | 6,2 |
| 2 + 3 + pamięć | 6,03 | 4,02 ± 0,20 | 7,3 |

- **Zdanie UPADŁO, ale nie tak, jak można było oczekiwać:** przy większej liczbie połączeń **dwa niezależne pomiary przestają się zgadzać** (5,59 vs 3,36; 6,03 vs 4,02) → struktura **nie ma dobrze określonego wymiaru**, zachowuje się jak sieć ze skrótami, nie jak rozmaitość. **Zgodne są tylko: triada (1,87 / 2,21) i triada + pamięć (3,24 / 2,81; w dokładniejszym przebiegu 3,11 / 3,01).**
- **Wniosek [A]:** nie chodzi o to, że piątego punktu **nie da się** dodać, tylko że po jego dodaniu **struktura przestaje być rozmaitością** — dodatkowe elementy tworzą skróty wewnątrz istniejącej struktury, a nie nową oś. **To jest dokładnie zdanie użytkownika, teraz na liczbach: rozmaitość istnieje tylko przy triadzie z pamięcią.**
- **Zastrzeżenie:** może to być własność tej rodziny reguł (więcej połączeń = więcej skrótów z natury); sprawdzenie na innej rodzinie pokazałoby, czy jest ogólne.

**ZADANIE B — NIEZALEŻNA RODZINA „POWIELANIE WĘZŁA” (użytkownik, przebieg; `etap3b_dwa_zadania_gpu.py`).** Inny mechanizm: nowy węzeł = kopia losowego rodzica, dziedziczy k jego relacji + relację z rodzicem (+ opcjonalnie pamięć: węzeł, z którego rodzic powstał). Skan k = 1…4, z pamięcią i bez. **Zdanie B1:** zgodność dwóch pomiarów (<0,3) wystąpi tylko dla trzech połączeń z pamięcią.
- **Wynik przy W = 200 000 (pełna tabela):**

| konfiguracja | z odległości | z kulek | różnica | stopień |
|---|---|---|---|---|
| rodzic + 1 | 8,37 | 5,75 ± 0,30 | 2,62 | 4,00 |
| rodzic + 1 + pamięć | 10,39 | 5,77 ± 0,30 | 4,63 | 5,47 |
| rodzic + 2 | 11,15 | 5,79 ± 0,19 | 5,36 | 6,00 |
| rodzic + 2 + pamięć | 10,28 | 6,11 ± 0,29 | 4,17 | 7,20 |
| rodzic + 3 | 10,17 | 5,99 ± 0,36 | 4,18 | 8,00 |
| rodzic + 3 + pamięć | 11,16 | 6,33 ± 0,41 | 4,83 | 9,06 |
| rodzic + 4 | 12,67 | 6,01 ± 0,37 | 6,66 | 10,00 |
| rodzic + 4 + pamięć | 12,77 | 6,47 ± 0,35 | 6,29 | 10,98 |

- **ZGODNYCH KONFIGURACJI BRAK.** Rozbieżności przy W = 200 tys. (2,6–6,7) są **większe** niż przy W = 8 tys. (1,75–3,18) → **nie jest to efekt skończonej wielkości; wymiar w tej rodzinie nie istnieje.** Wymiar z kulek trzyma się ~6 niezależnie od k (5,75–6,47), a z odległości rośnie 8,4 → 12,8: tak wygląda sieć, w której odległości prawie nie rosną z rozmiarem (mały świat). **B1 nierozstrzygnięte** (nie ma w tej rodzinie przypadku do porównania), ale osobny wynik:
- **ROZMAITOŚĆ WYMAGA ROZSZERZANIA OD ŚRODKA [A]:** doklejanie nowych węzłów do istniejących — losowe (R3), przez odległość z porządku (R4), przez powielanie (B) — zawsze daje mały świat albo strukturę bez określonego wymiaru. **Rozmaitość pojawiła się wyłącznie tam, gdzie nowe relacje powstawały POMIĘDZY istniejącymi (R5, R6).** Zgodne z tezą użytkownika: nowe relacje przestrzenne nie doklejają się na brzegu, tylko powstają wewnątrz.
- **Otwarte:** uniwersalność triady wymaga **trzeciej** rodziny reguł — takiej, która produkuje rozmaitości, ale działa inaczej niż podział relacji.
- **PRÓBA NIEZALEŻNEJ RODZINY — „powielanie węzła”** (`etap3_dwa_zadania.py`, zadanie B; użytkownik, W = 200 tys.; asystent, W = 8 tys.). Inny mechanizm: nowy węzeł = kopia losowego rodzica, dziedziczy k jego relacji + relację z rodzicem (+ pamięć = węzeł, z którego rodzic powstał). Skan k = 1…4 z pamięcią i bez. **Wynik: ŻADNA konfiguracja nie jest zgodna** (różnice dwóch pomiarów 1,75–3,18 przy W = 8 tys.; brak zgodnych także przy W = 200 tys.) — ta rodzina **w ogóle nie produkuje rozmaitości**, przy żadnej liczbie połączeń.
  - **Co to znaczy [A]:** teza „zgodność tylko przy triadzie z pamięcią” **nie została potwierdzona w drugiej rodzinie**, bo ta rodzina nie daje rozmaitości w żadnym wariancie. Osobny wynik, spójny z R3/R4: **doklejanie nowych węzłów do istniejących zawsze daje mały świat; rozmaitość wymaga wstawiania POMIĘDZY (rozszerzania od środka).**
  - **Status tezy o triadzie:** nadal **jedna rodzina reguł** (podział relacji). Potrzebna trzecia rodzina, która w ogóle potrafi dawać rozmaitości.

**PRZEGLĄD LITERATURY (v3.4, pozycje wskazane przez użytkownika) [L]:**
- **Trugenberger, grawitacja kombinatoryczna** (JHEP 2017, 45; arXiv:1610.05934; przegląd: Universe 9, 499, 2023): zespół grafów rządzony krzywizną Olliviera–Ricciego; **przejście fazowe losowe → geometryczne przez kondensację krótkich cykli**; w 2D faza geometryczna to powierzchnie o **ujemnej krzywiźnie** z dwiema skalami (Planck i promień krzywizny); **materia = kawałki losowych bitów rozmiaru Plancka o energii danej nadmiarem krzywizny** (zbieżne z naszym „cząstka = nadwyżka ponad podłogę”, C4a.21–22). Podejście równowagowe, nie reguła wzrostu.
- **Bianconi–Rahmede (NGF)**: rosnące kompleksy symplicjalne; geometria **hiperboliczna**, w d>2 bezskalowe.
- **Najbliższy kandydat do przeczytania:** da Silva, Bianconi, da Costa, Dorogovtsev, Mendes, „Complex network view of evolving manifolds”, Phys. Rev. E 97, 032316 (2018).
- **Duplikacja węzłów:** zgodnie z literaturą daje struktury bezskalowe i małe światy — nasza rodzina B to potwierdza.

**KRZYWIZNA SIECI R6 — ZDANIE UPADŁO** (`etap4_krzywizna.py`). Zdanie przed rachunkiem: R6 ma krzywiznę bliską zeru (płaska), nie ujemną.

| struktura | krzywizna Olliviera–Ricciego |
|---|---|
| **R6 (triada + pamięć)** | **−0,325 ± 0,036** |
| R5 (triada) | −0,258 ± 0,030 |
| drzewo (kontrola ujemna) | −0,360 ± 0,027 |
| siatka 3D (płaska, stopień 6) | 0,000 |
| **losowy graf geometryczny 3D, stopień 4,2 (płaski, ta sama rzadkość)** | **+0,083 ± 0,031** |

- **Kontrola rozstrzyga:** płaski graf o tej samej rzadkości daje krzywiznę **dodatnią**, więc pomiar rozróżnia. **Sieć R6 jest ujemnie zakrzywiona**, niemal jak drzewo.
- **Status wyniku R6 zmieniony:** struktura jest trójwymiarowa w sensie wzrostu kulek, ale **hiperboliczna, nie płaska** — ta sama klasa co NGF Bianconi i faza geometryczna Trugenbergera. **Dotarliśmy na mieliznę z mapy, tylko od strony wzrostu zamiast zespołu.**
- **Napięcie do wyjaśnienia:** ujemna krzywizna zwykle daje wykładniczy wzrost kulek, a mierzyliśmy r³. Najprostsze wyjaśnienie: promień krzywizny porównywalny z rozmiarem układu — hiperboliczność ujawniłaby się przy większych zasięgach.

**PRÓBA PRZYWRÓCENIA TRÓJKĄTOWI STATUSU — SERIA (v3.4, `etap4_krzywizna.py`, `etap5_kompleks.py`).** Cel: sprawdzić, czy ujemna krzywizna R6 pochodzi od triady, czy od sposobu wyboru miejsca.

| wariant | wymiar | krzywizna |
|---|---|---|
| graf, losowa relacja (R6) | 3,01 | −0,325 |
| graf, najstarsza relacja (FIFO) | 1,58 | −0,269 |
| graf, wszyscy wspólni sąsiedzi + FIFO | 3,67 | −0,113 |
| **kompleks czworościanów** (triada = ściana, pamięć = czwarty wierzchołek), FIFO | **2,89 ± 0,08** | −0,160 |
| kontrola: **płaska triangulacja 3D** (Freudenthal, stopień 12) | 3 | **0,000** |
| kontrola: płaski graf geometryczny 3D (stopień 4,2) | 3 | +0,083 |

- **Trójwymiarowość jest odporna:** wychodzi w trzech implementacjach, także w wersji na **kompleksie**, gdzie konstrukcja użytkownika (czworościan = triada + czas) jest oddana dosłownie. **Płaskości nie ma w żadnej.**
- **Kontrole są poprawne:** płaska triangulacja o stopniu 12 daje dokładnie 0,000 — miara rozróżnia przy tej samej gęstości połączeń.
- **Teza użytkownika:** (1) **nie ma czegoś takiego jak płaskość**; (2) **o skali Plancka nic nie można powiedzieć**; (3) **oba są nieodróżnialne od Ø**. Płaskość = zerowa krzywizna = brak odróżnienia = Ø; żądanie płaskości było żądaniem, by struktura była nieodróżnialna od Ø. Zgodne z tabelą granic: do Ø nie prowadzi droga ciągła. **Poprzednie „upadło” było źle postawione.**
- **Test z tego wynikający:** jeśli płaskość jest granicą, |krzywizna| maleje z gęstością. **UPADŁO w obu rodzinach:** graf — stała (−0,359 / −0,420 / −0,330 przy W = 2/8/32 tys.); **kompleks — ROŚNIE** (−0,078 / −0,141 / −0,213 przy W = 4/16/48 tys.).
- **POPRAWKA DO POSTAWIENIA PYTANIA (użytkownik): „pomiędzy kwarkami a płaskością jest pustynia”.** Krzywizna Olliviera liczona na **pojedynczej relacji** jest wielkością z najmniejszej skali; płaskość obserwowana w kosmologii dotyczy skali o kilkadziesiąt rzędów większej. Ujemna krzywizna w UV jest więc **zgodna** z niemal zerową w IR — dokładnie tak działa obraz Trugenbergera (długość Plancka i promień krzywizny odwrotnie powiązane, pomiędzy nimi gładka powierzchnia). **Pytanie „czy krzywizna maleje z gęstością” było źle postawione; właściwe: czy maleje ze SKALĄ POMIARU.**
- **Test skali — NIEWAŻNY (kontrola upadła):** krzywizna liczona na parach w odległości r (miary na sąsiadach): kompleks −0,137 / +0,046 / +0,000 / +0,063 dla r=1…4; **drzewo (kontrola ujemna) przechodzi na plus** (+0,147 przy r=2) zamiast pozostać ujemne; płaska triangulacja 0,000 przy każdym r. **Wada normalizacji:** dla dalekich par transport ≈ r, więc wynik dąży do zera niezależnie od geometrii. **Poprawna wersja wymaga miar na kulach promienia r** (transport na setkach węzłów) — do zrobienia.
- ~~**NAJOSTRZEJSZE OTWARTE MIEJSCE:** między „płaskość to Ø, więc nieosiągalna” a obserwacją (przestrzeń płaska z dokładnością <1%) zostaje luka. Nasze struktury nie zbliżają się do zera nawet asymptotycznie. Ta rodzina reguł tego nie wypełnia.~~ **LUKA ŹLE POSTAWIONA (użytkownik [H] + asystent, 25.09, poprawka 113).** „Płaska z dokładnością <1%” to zdanie wspólnego aparatu (fakt): przy tej rozdzielczości odczytu krzywizny nie da się odróżnić, a nieodróżnialność to znaczenie ≡ w łańcuchu Ø. **Krzywizna doprowadzona do zera = wpadnięcie w skalę Plancka, nieoznaczoność albo osobliwość** — „miejsca”, o których nic nie można powiedzieć (2D, $l_P t_P$ i osobliwość są w łańcuchu Ø). Szukanie reguły, która sprowadza krzywiznę do zera, było żądaniem, żeby struktura stała się Ø. **Takie miejsca opisuje się wyłącznie nie wprost, przez bezpośrednie otoczenie** (zgodnie z „przenoszenie różnic na Ø tylko pośrednio”, R1/R3). Mierzalne jest więc to, jak wygląda otoczenie miejsca nieodróżnialnego od Ø, a nie to, czy struktura do niego zbiega.
- **Ø opisywane nie wprost, przez otoczenie — ten sam mechanizm w dwóch formalizmach (25.09, poprawka 114).** **→ Zebrane jako dowód w R1b.**
  - **[H] użytkownik (potwierdzenie odczytu asystenta):** triada sama = 2D ≡ Ø; jej bezpośrednim otoczeniem są zapisy połączone linkami (światło); **3D = opis Ø nie wprost, przez otoczenie** — czworościan nie dokłada wymiaru do płaszczyzny, tylko jest jedynym sposobem, w jaki o niej da się coś powiedzieć (drugi rysunek: triada współliniowa, zapisy nad i pod). **Dowód 3D i opis miejsc Ø przez otoczenie to ten sam dowód.**
  - **[H] użytkownik: przestrzeń Hilberta robi dokładnie to samo.** O superpozycji jako takiej nic nie można powiedzieć; prawdopodobieństwa i cały rachunek odnoszą się zawsze do ewentualnej dekoherencji w określonym otoczeniu (por. [110], łańcuch Ø: |ψ⟩ ≡ Ø).
  - **[L] formalizm, bez interpretacji:** Gleason (1957) — prawdopodobieństwa są miarą na rzutach, więc istnieją dopiero po wskazaniu rozkładu (kontekstu); Kochen–Specker (1967) — w wymiarze ≥ 3 nie ma wartości niezależnych od kontekstu; Zurek (einselekcja, Rev. Mod. Phys. 75, 715, 2003) — bazę wskaźnikową wyznacza oddziaływanie z otoczeniem. Wszystkie trzy mówią formalnie: stan sam nie niesie wartości, niesie je relacja z otoczeniem.
  - **[L] Müller–Masanes, „Three-dimensionality of space and the quantum bit: an information-theoretic approach”, New J. Phys. 15, 053040 (2013), arXiv:1206.0630 (przeczytane w całości, v4) — przekład przez filtr (poprawka 115):**
    - **Założenia tła:** d wymiarów przestrzennych + jeden czas; **stała płaska przestrzeń tła** z jednoznacznym przenoszeniem wektorów; wszystko w spoczynku (bez efektów relatywistycznych); makroskopowe urządzenie obracane grupą SO(d). **Odpada** (gotowa przestrzeń). Uwaga: w §V i Przykładzie 39 autorzy sami rozważają odwrócenie — przestrzeń jako rozmaitość topologiczna bez struktury euklidesowej, a struktura euklidesowa **odziedziczona z wypukłości prawdopodobieństw**.
    - **Postulat 1 (kodowanie):** Alicja koduje każdy kierunek w stanie tak, że Bob odtwarza go w granicy wielu kopii; **nie mają wspólnego układu współrzędnych**, liczy się tylko względna orientacja nośnika i przyrządu. **Przechodzi** — kierunek jest relacją, nie cechą. Jeden odczyt daje jeden wynik; kierunek ustala się z wielu odczytów [?] (por. rysunek: wiele zapisów wokół triady, bez kolejności).
    - **Postulat 2 (minimalność):** nie da się zakodować nic więcej bez zaszumienia informacji o kierunku. **Przechodzi** — foton = minimalne wzbudzenie = minimalna informacja.
    - **Twierdzenie 1:** przestrzeń stanów nośnika to kula d-wymiarowa; stany czyste na sferze, **w środku stan maksymalnie mieszany μ — jedyny niezmienniczy względem wszystkich obrotów**, bez żadnej informacji o kierunku. [O][?] μ ≡ Ø: nierozróżnialny od każdej orientacji; stan opisywalny tylko przez to, że wszystko inne jest jego mieszaniną z kierunkiem.
    - **Postulat 3 (sumy obserwabli) ≡ tomografia lokalna:** stan pary wyznaczony przez odczyty części i ich korelacje. **Przechodzi** — całość bez otoczenia znana tylko przez odczyty wewnątrz.
    - **Postulat 4 (oddziaływanie):** istnieje ciągła jednoparametrowa grupa przekształceń odwracalnych pary, która nie jest iloczynem lokalnych. **Częściowo:** „odwracalna” przechodzi za darmo (stan bez etykiety przed/po); „nie-iloczyn” = relacja, której nie da się rozłożyć na odczyty osobno — przechodzi; **„parametr t ∈ ℝ jako czas” odpada**; zostaje ciągłość rodziny przekształceń — **otwarte, czy rama ją daje** („zawsze w ruchu” ≠ „ciągle”). **ROZSTRZYGNIĘTE (użytkownik [H], poprawka 118): odpowiedź w syntezie czasu (sesja CC, wiad. 72; R1a) — „niezmienniczość względem reparametryzacji: Ĥ|Ψ⟩=0”.** Reparametryzacja = dowolne przemianowanie parametru; Ĥ|Ψ⟩=0 to niezmienniczość całości względem **ciągłej jednoparametrowej grupy** e^(−iĤt) generowanej przez Ĥ. Ciągła grupa jest więc w pierwszym ogniwie łańcucha; całość względem niej stoi (brak otoczenia), części zmieniają się tylko względem podukładu czytającego (Page–Wootters [L]: stan warunkowy względem odczytu zegara spełnia równanie Schrödingera). **Przekład P4:** grupa ciągła = grupa reparametryzacji; t = dowolna etykieta, nie czas; odwracalność = brak etykiety przed/po; nie-iloczyn = relacja. **P4 przechodzi w całości; d = 3 stoi na tym, co już jest w ramie.**
    - **Twierdzenie 2: d = 3.** d = 1: para nośników to klasyczny czworościan stanów, skończenie wiele przekształceń, brak ciągłego oddziaływania. **d = 2 i d ≥ 4: każde odwracalne przekształcenie pary rozkłada się na lokalne — oddziaływania nie ma.** Powód wg autorów: podgrupa obrotów zostawiająca jeden kierunek w miejscu, SO(d−1), jest przemienna (dla d ≥ 3) tylko przy d = 3. **[?] w ramie:** po ustaleniu jednego kierunku zostaje płaszczyzna, w której kolejność obrotów nic nie znaczy — 2D, gdzie „kolejność” nie niesie informacji. Niesprawdzone.
    - **Twierdzenie 3:** przy d = 3 para nośników to dokładnie dwa kubity, ewolucja unitarna. Poza d = 3 „nośnika minimalnej informacji o kierunku” w ogóle nie ma (Tw. 26).
    - **[H] użytkownik (25.09): kula stanów = zbiór wszystkich możliwych kierunków / odczytów / pozycji — i wtedy faktycznie jest 3D.** Rozbieżność „wymiar kuli vs 4 punkty” rozstrzygnięta tak (poprawka 116):
      - **[O][L]** kula ma „d niezależnych, wzajemnie komplementarnych pomiarów” (s. 7); przy d = 3 stan ustala się dopiero z odczytów wzdłuż **trzech** kierunków — dwa nie wystarczają, czwarty nic nie dokłada. To „3D = warunek konieczny i wystarczający do ustalenia każdej pozycji”: **3 komplementarne odczyty = triada (3 węzły relacji), 4. punkt = sam stan**, w superpozycji do odczytu (= „punkt informacji w superpozycji, dopóki pole nie jest wzbudzone”).
      - **[O][?]** środek μ (brak informacji o kierunku) opisywalny tylko przez to, co od niego odchodzi (każdy stan = mieszanina μ z kierunkiem) — „Ø nie wprost”.
      - ~~**Napięcie [?]:** drugi rysunek (triada współliniowa, 3D z zapisów) vs kula (trzy współpłaszczyznowe kierunki pomiaru nie ustalają stanu). Zgodne tylko, jeśli warunkiem na triadę jest **niezależność (komplementarność) trzech relacji**, nie kształt węzłów w przestrzeni. Odczyt asystenta, do potwierdzenia.~~ **NAPIĘCIE ŹLE POSTAWIONE (użytkownik [H], poprawka 117):** drugi rysunek to kadr (projekcja na ekran, odbiorca = czwarty punkt), nie triada współliniowa; współliniowość jest tylko w 2D ≡ Ø. **Błąd asystenta:** potraktował płaską projekcję (sama jest 2D ≡ Ø) jak konfigurację w strukturze. Nie ma więc potrzeby osłabiać warunku na triadę do „niezależności relacji”; zgodność z kulą bez zastrzeżeń: trzy odczyty ustalające stan nie leżą w jednej płaszczyźnie, bo płaszczyzna ≡ Ø.
    - **[L] praca źródłowa kroku d = 3: Masanes, Müller, Pérez-García, Augusiak, „Entanglement and the three-dimensionality of the Bloch ball”, J. Math. Phys. 55, 122203 (2014), arXiv:1111.4060 (przeczytane: wyniki i aksjomaty) — przez filtr (poprawka 119). BEZ PRZESTRZENI FIZYCZNEJ:** stan = prawdopodobieństwa odczytów; nie ma w niej ani przestrzeni, ani obrotów urządzeń.
      - **Układ binarny:** dokładnie dwa stany doskonale rozróżnialne = najmniejsza różnica, 1 bit. **Przechodzi** (foton = minimalna informacja).
      - **Tomograficzna lokalność:** stan złożony wyznaczony przez odczyty części. **Przechodzi.**
      - **Układ złożony:** łączne prawdopodobieństwa odczytów części **nie zależą od kolejności w czasie** („independently of the temporal ordering”). **Przechodzi** — brak kierunku wprost w definicji.
      - **Ciągła odwracalność:** każde dwa stany czyste łączy ciągłe przekształcenie odwracalne (grupa spójna; „t może być interpretowane jako czas” — interpretacja, odrzucamy). **Przechodzi:** ciągłość = reparametryzacja (118), odwracalność = brak etykiety przed/po, przechodniość na stanach czystych = żaden ostry odczyt nie jest wyróżniony.
      - **Oddziaływanie** (istnieje dynamika nie-iloczynowa ⇔ splątanie). **Przechodzi** = relacja.
      - **„Okrągłość” (roundness):** zbiór stanów układu binarnego jest ściśle wypukły (brzeg bez odcinków); z ciągłą odwracalnością daje kulę. **JEDYNE ZAŁOŻENIE BEZ PRZEKŁADU.** W 2013 kulę dawały P1–P2, ale przez obroty w przestrzeni tła. Autorzy wymieniają inne źródła kuli: przyczynowość informacyjna, lokalność gałęzi, „brak zysku informacji ⇒ brak zaburzenia” (ich ref. 17–20) — do sprawdzenia. Ostrzeżenie: „brzeg bez płaskich kawałków” ↔ „płaskość ≡ Ø” to na razie **gra słów (pułapka nazewnicza)**, nie przekład.
      - **„OKRĄGŁOŚĆ” ROZSTRZYGNIĘTA (użytkownik [H], 25.09, poprawka 120):** „Sama powierzchnia sfery jest 2D ≡ Ø. 3D jest tylko lokalne jako wynik świata relacji wewnątrz. Dla całego wszechświata lub dla całej sfery t=0” (por. rozmowa [150], [270], [402]: całość bez relacji → t=0; wzbudzenia i relacje lokalne; hierarchia węzłów do 2D Plancka).
        - **Odczyt [A]:** brzeg kuli = zbiór wszystkich ostrych odczytów = sfera = 2D ≡ Ø; brzeg jako całość nie ma otoczenia → t=0 → nic na nim nie jest wyróżnione (Wheeler–DeWitt zastosowany do zbioru odczytów). Płaski odcinek na brzegu byłby wyróżnioną strukturą na całości; struktura powstaje tylko lokalnie, z relacji wewnątrz. **Okrągłość nie jest osobnym założeniem.**
        - **[L] formalny odpowiednik „3D tylko lokalnie, z relacji”: oczyszczanie (puryfikacja).** Każdy stan wnętrza kuli (mieszany) jest częścią stanu czystego większego układu, czyli lokalnym śladem relacji; samotny układ leży na sferze. Chiribella, D’Ariano, Perinotti, „Informational derivation of quantum theory”, Phys. Rev. A 84, 012311 (2011), arXiv:1011.6451 — puryfikacja jako postulat wyprowadzenia teorii kwantowej.
        - **Stan dowodu 3D [A]:** wszystkie założenia Masanesa i in. (2014) przełożone; d = 3 jest jedynym wymiarem kuli odczytów, w którym dwa minimalne nośniki informacji wchodzą w relację. ~~**[?] do domknięcia na kartce:** czy „brak wyróżnienia na całości” wyklucza wszystkie nieokrągłe zbiory stanów układu binarnego, czy tylko wielościany (te wypadają już na ciągłości).~~ **ZAMKNIĘTE (użytkownik [H], poprawka 121): „Lokalny odczyt może mieć dowolny kształt. Suma wszystkich odczytów wokół jednego punktu odniesienia daje sferę.”** Pytanie źle postawione: mieszało kształt pojedynczego odczytu ze zbiorem stanów, a zbiór stanów u Masanesa i in. to już suma wszystkich odczytów. Formalnie to samo robią oni (sekcja III): średnia po wszystkich przekształceniach W² = ∫HᵀH dH daje elipsoidę → kula. Nieokrągłe kształty nie są wykluczone — są lokalne; sfera jest sumą, w której żaden kierunek nie jest wyróżniony.
      - **Wynik:** kula wymiaru d = 2, 3, 4, …: **oddziaływanie (splątanie) istnieje tylko przy d = 3**, i wtedy to dokładnie dwa kubity (Tw. 1–2). d = 1 (bit klasyczny) wypada już na ciągłości: przekształcenia odwracalne to permutacje, grupa niespójna. **W ramie:** 1D nie istnieje, 2D — relacji brak, ≥ 4 — relacji brak, 3 — jedyny przypadek, w którym dwa minimalne nośniki informacji wchodzą w relację. **Dowód strukturalny, bez przestrzeni tła, z jednym nieprzełożonym założeniem (okrągłość).**
    - **Co zostaje po filtrze [A]:** 3D jest jedynym przypadkiem, w którym dwa minimalne nośniki informacji mogą wejść w relację nierozkładalną na odczyty osobno; przy 2D i przy więcej niż 3D relacji brak. Zgodne z „2D ≡ Ø, relacja przestrzeni = 0” i z „więcej niż 4 punkty nic nie dokłada” — u nich mocniej: nie skróty, tylko brak relacji w ogóle. **Rozbieżność do rozstrzygnięcia:** u nich 3 = wymiar kuli stanów, u nas 3D = 4 punkty odniesienia.

**PRZEGLĄD LITERATURY: KRZYWIZNA, PUSTYNIA, CZARNE DZIURY (v3.4, 25.09) [L] — po uwadze użytkownika [H]: krzywizna nie schodziła do zera, pustynia między kwarkami a Planckiem przeszkadza, zmienić otoczenie na czarne dziury.**
- **van der Hoorn, Cunningham, Lippner, Trugenberger, Krioukov, Phys. Rev. Research 3, 013211 (2021):** krzywizna Olliviera grafów geometrycznych zbiega do krzywizny Ricciego rozmaitości **tylko na otoczeniach mezoskopowych** (skala pomiaru → 0 wolniej niż skala połączeń). Na skali pojedynczej krawędzi zbieżności nie ma. **Nasze „krzywizna nie schodzi do zera” (C5, R6) było mierzone dokładnie na skali, na której zbieżności nie ma.** Nasza „poprawna wersja na kulach promienia r” to ich warunek mezoskopowy. **Pustynia w języku literatury: okno skal ℓ_dyskr ≪ δ ≪ R_krzywizny**, jedyny zakres, w którym krzywizna jest w ogóle zdefiniowana.
- **Barton, Borza, Röhrig, „Ollivier–Ricci curvature for causal sets”, arXiv:2606.04910 (VI 2026):** krzywizna Olliviera dla zbiorów przyczynowych z transportu lorentzowskiego, **mezoskopowa, zdefiniowana WZDŁUŻ ŁAŃCUCHÓW MAKSYMALNYCH** (czyli trajektorii), z miar na diamentach przyczynowych. Odtwarza stałe krzywizny Minkowskiego, de Sittera i anty-de Sittera na gęstym sprinklingu.
- **Braun, Li, „Timelike Ollivier–Ricci curvature”, arXiv:2609.18664 (IX 2026):** konstrukcja współwymiaru 1 (miary na małych przestrzennopodobnych płatach przez bliskie zdarzenia) odtwarza krzywiznę Ricciego w kierunkach czasopodobnych. **Echo równania Raychaudhuriego:** zmiana objętości przestrzennej wzdłuż geodezyjnej czasopodobnej ↔ Ricci.
- **Eichhorn i in., „Towards black-hole horizons and geodesic focusing in causal sets”, arXiv:2605.06813 (V 2026):** lokalna diagnostyka horyzontu zdarzeń z dyskretnych krzywych czasopodobnych; pierwsze kroki do horyzontu pozornego przez **ogniskowanie** („drabiny” jako ślady geodezyjnych zerowych).
- **Molekuły horyzontu:** Dou–Sorkin; Barton, Counsell, Dowker, Gould, Jubb, Taylor, Phys. Rev. D 100, 126008 (2019): oczekiwana liczba molekuł = pole horyzontu w jednostkach dyskretności × czynnik rzędu 1 zależny od wymiaru. Liczenie boltzmannowskie: Phys. Rev. D 110, 026015 (2024). Zgodne z naszym A5.
- **Odczyt [A][O] — co z tego wynika dla ramy:**
  1. W literaturze krzywizna jest wielkością **odczytywaną przez trajektorię** (łańcuch maksymalny, ogniskowanie, Raychaudhuri), a nie własnością samej triady przestrzennej. W naszym języku: krzywizna pojawia się dopiero z czwartym punktem odniesienia. **Triada sama nie niesie krzywizny na skali ogniwa; to nie porażka trójkąta, tylko złe miejsce pomiaru.** Możliwa odpowiedź na „przywrócenie trójkątowi statusu”.
  2. OTW po oczyszczeniu z interpretacji: krzywizna = ogniskowanie (Raychaudhuri) = to, jak odczyt objętości sąsiadów zmienia się wzdłuż trajektorii. To czysto informacyjne zdanie, zgodne z definicją czasu (R1a).
  3. Czarna dziura to otoczenie, w którym górny kraniec pustyni ma **liczbę**: liczbę molekuł horyzontu (∝ pole). Horyzont pozorny = miejsce, gdzie ogniskowanie przestaje pozwalać na odczyt z zewnątrz. To nasza definicja „zawarte, ale nieodczytywalne”.
- **POPRAWKA (użytkownik [H], 25.09): „nie ma żadnego kierunku; odczyt jest zawsze teraz”.** Moja propozycja porządku w R6 („p ≺ q, gdy q wyrosło z linii ścian przez p”) przemycała kierunek z kolejności budowania symulacji. **WYCOFANA.** Źródła w rozmowie: przeszłość nie *jest*, jest tylko zapis czytany teraz (wiad. 334, 394, 491, klocki LEGO: stan rozłączony może być przeszłością i przyszłością); strzałka czasu = pseudokierunek z rozproszenia zapisu (152–156); pamięć = struktura sama w sobie (54).
  - **Diament nie potrzebuje kierunku [T][L]:** I[p,q] w porządku odwróconym = I[q,p], ten sam zbiór. Graf porównywalności (które pary są w relacji, bez mówienia, który wcześniej) wyznacza porządek z dokładnością do odwróceń (Gallai 1967, orientacje przechodnie; w typowym przypadku jeden bit na spójną część). **Strzałka czasu w porządku przyczynowym to ta umowa o jednym bicie**, zgodnie z „pseudokierunkiem” użytkownika. Diament = „to, co leży pomiędzy dwoma odczytami”, bez „wcześniej–później”.
  - **Pytanie o R6 przeformułowane:** nie „co było pierwsze”, tylko **czy R6 ma relację „pomiędzy”?** Propozycja [A][?]: z leży pomiędzy x i y, gdy leży na drodze relacji odczytu (połączeń z punktem pamięci) łączącej x z y. Boki triady to relacje przestrzenne, połączenia pamięci to relacje odczytu, bez kierunku. Czeka na potwierdzenie użytkownika. Wersja zapasowa: symetryczna krzywizna Olliviera na kulach promienia r (van der Hoorn i in.), bez diamentów.
  - **RYSUNEK UŻYTKOWNIKA (`rysunki/triada_z_zapisami.png`) [H]:** triada X, Y, Z; wokół faliste linie = trajektorie (zapisy dawnych układów, „dym”); na nich punkty zapisu (czerwony, niebieski, zielony, czarny), **każdy połączony naraz ze wszystkimi trzema wierzchołkami**, kilka jednocześnie, bez kolejności. **Odczyt = jeden krok triada ↔ zapis = czworościan.** Odpowiednik diamentu w tej konstrukcji to **czworościan (triada + zapis)**, bez kierunku. Moja propozycja „pomiędzy = droga po odczytach” (łańcuch) wycofana.
  - **Dopowiedzenie użytkownika [H]:** (1) lokalna struktura jest **dynamiczna** (boki falują), bo zero absolutne jest nieosiągalne (rozmowa, wiad. 72, 482); (2) **przestrzeń = relacja**; w próżni to pole EM ≡ Ø, **wzbudzenia = odczyty**, bez odczytu = superpozycja ≡ Ø (wiad. 242, 244, 258, 268); (3) **dlatego światło jest najważniejsze** (wiad. 488: nieskończone c ≡ pole bez wzbudzeń; „musi się rozstrzygnąć na poziomie światła”).
  - **DRUGI RYSUNEK (`rysunki/triada_z_zapisami_2.jpg`) i WYMIARY [H] (użytkownik, 25.09):** **statyczny wycięty kadr** (projekcja na płaski ekran) w chwili, gdy **odbiorca przed ekranem jest czwartym punktem odniesienia** — triada widziana z własnej płaszczyzny, więc X, Z, Y wypadają na jednej kresce obrazu. **Współliniowości tam nie ma: współliniowość istnieje tylko w 2D (≡ Ø); w 3D nie ma racji bytu** (użytkownik, poprawka 117). ~~triada współliniowa (X, Z, Y na prostej)~~; zapisy nad i pod nią, każdy połączony z całą triadą. „Mogłem też tak to narysować. To nie znaczy, że płaskość w ogóle istnieje.” Kształt triady nie ma znaczenia; trójwymiarowość dają zapisy. **1D nie istnieje. 2D = płaskość = nieoznaczoność = skala Plancka, relacja przestrzeni = 0, nic nie można powiedzieć. 3D = warunek konieczny i wystarczający do ustalenia każdej pozycji. 3 wymiary przestrzenne = 4 punkty odniesienia** (3 węzły relacji + 1 punkt informacji o dynamicznej strukturze, w superpozycji, dopóki pole nie jest wzbudzone). **Definicji czasu nie wolno używać bez połączenia z tym, jak czas tworzy 3D i dlaczego nie 4D ani 154D** (rozmowa, wiad. 511).
  - **Odczyt [A][O]:** połączenia zapis ↔ wierzchołek to odczyty, czyli wzbudzenia, czyli najmniejsze różnice = **fotony**. W porządku przyczynowym foton to **link** (relacja bez niczego pomiędzy, t = 0). **Czworościan = triada + zapis połączony trzema linkami, czyli zbudowany ze światła.** Boki triady w próżni są ≡ Ø i stają się czymś dopiero przez odczyty. Geometria (krzywizna) = to, jak odczyty-światło zamykają się wokół krawędzi triad.
  - **REGGE NA KOMPLEKSIE Z etap5 (`etap18_regge_krawedzie.py`, CPU, sekundy) [L][P].** [L] Regge 1961: w kompleksie czworościanów krzywizna siedzi na krawędziach; dla równych czworościanów płasko przy 2π/arccos(1/3) = **5,104** czworościanu wokół krawędzi (5 → dodatnia, 6+ → ujemna); równe czworościany nie wypełniają przestrzeni. **Zdanie przed rachunkiem:** średnio > 5,104 wokół krawędzi wewnętrznej (zgodnie z Ollivierem −0,16).
    - **Wynik:** średnia 5,098 / 5,111 / 5,122 przy W = 4 / 16 / 48 tys. Przy W = 4 tys. zdanie upadło, przy większych przeszło o włos. **Średnia przechodzi przez wartość płaską i dryfuje dalej.** Z tożsamości Eulera dla 3-rozmaitości (E = V + T) średnia = 6/(1 + V/T), a **T/V rośnie jak ln W** (5,10 / 5,38 / 5,66 przy 8 / 32 / 128 tys.). „Średnio płasko” jest więc zdaniem o **stosunku liczebności T/V = 5,70**, przez które reguła wzrostu tylko przechodzi, bez zatrzymania.
    - **Lokalnie nie ma płaskości wcale:** rozkład jest dwumodalny, **72% krawędzi ma 4 czworościany** (deficyt +78°), **27–28% ma 8** (−204°), 5 i 6 prawie nie występuje (0–1%). Każda krawędź jest silnie zakrzywiona, a średnia bywa płaska.
    - **Zastrzeżenie [A]:** kompleks kombinatoryczny = czworościany równe i sztywne = migawka bez dynamiki, czyli **„zero absolutne” w języku ramy, które rama wyklucza**. Przy falujących bokach deficyty nie są ustalone przez same liczby; płaskość mogłaby być tylko średnią po odczytach. Tego ta migawka nie mierzy. Kolejny logarytm (T/V ∝ ln W) do zestawienia z §F2 [?].
- **Pytania, które z tego wynikają (niepoliczone) — po filtrze (25.09, poprawka 113):**
  - **P-K1:** czy w strukturze R6 (pamięć wyłączna, 3,11 / 3,01) krzywizna z diamentów (bez kierunku, patrz poprawka wyżej) wzdłuż trajektorii, liczona w oknie mezoskopowym, zbiega do zera? Poprzednie pomiary liczyły krzywiznę Olliviera grafu przestrzennego na skali ogniwa, gdzie zbieżności nie ma z twierdzenia. **[źle postawione]** zakłada płaskość (≡ Ø) jako cel zbieżności; diament wzdłuż łańcucha zamiast czworościanu (triada + zapis).
  - **P-K2:** czy pustynia jest niczym więcej niż oknem mezoskopowym, czyli czy jej długość w bitach (ln stosunku skal) jest tym samym logarytmem co w §F2 (koszt wskazania)? **[do przeformułowania]** „okno mezoskopowe” to warunek działania estymatora Olliviera, nie własność struktury; porównanie dwóch logarytmów (stosunek stosunków) zostaje.
  - **P-K3:** czy na sprinklingu Schwarzschilda ogniskowanie wzdłuż trajektorii (Raychaudhuri) daje horyzont pozorny w miejscu, gdzie liczba molekuł horyzontu = pole/4, bez podawania r_s z zewnątrz? **[źle postawione]** gotowa geometria z r_s z zewnątrz i OTW z interpretacją; w ramie czarna dziura = „tworzenie relacji nie wyprzedziło odczytywania” [460], osobliwość ≡ Ø, opisywalna tylko przez otoczenie.
  - **P-K4 [A][?] (sesja CC 24.09, wiad. 80, po rysunku i Regge):** czy struktura, w której odczyty są linkami (światło), a boki triady są ≡ Ø, dopóki nikt ich nie czyta, może mieć lokalnie tylko krzywiznę dodatnią albo ujemną (4 albo 8, nigdy „pomiędzy”), a płaskość wyłącznie jako średnią po wielu odczytach? Jeśli tak, **pustynia = skala, na której liczba odczytów wystarcza, żeby średnia się ustaliła**; jej długość wynikałaby z liczby fotonów, nie z geometrii. Odpowiedź użytkownika: drugi rysunek i „to nie znaczy, że płaskość w ogóle istnieje” (wiad. 82); pytanie nierozstrzygnięte. **[źle postawione]** płaskość jako cel (średnia po odczytach); Regge liczony na sztywnej migawce = zero absolutne.

**MAPA MIELIZN (v3.4) — trzy znane wyniki wzrostu, każdy już u nas widziany [L]:**

| droga | wynik w literaturze | u nas |
|---|---|---|
| wzrost sekwencyjny z przypadkowym łączeniem (Rideout–Sorkin) | porządek prawie liniowy, nie rozmaitość | v0: wymiar ~1 |
| ustalona siatka | wymiar jest, brak niezmienniczości Lorentza (kryształ) | kalibracja: estymator 1,5–2,3 |
| sklejanie czworościanów wzdłuż trójkątnych ścian, bez czasu (Bianconi–Rahmede, „network geometry with flavor”, Sci. Rep. 7, 41974, 2017; arXiv:1607.05710) | geometria **hiperboliczna**, mały świat (nieskończony wymiar Hausdorffa), skończony wymiar spektralny | v1: sieci losowe, średnica 5 |

- **„Triada + odczyt = czworościan” ma precedens:** NGF w d=3 skleja czworościany na trójkątach — i daje geometrię hiperboliczną, nie płaską.
- **Nikt nie ma reguły dającej jednocześnie płaską 3D i porządek lorentzowski** — otwarty problem rozmaitościowości w teorii zbiorów przyczynowych, nie lokalna trudność.
- **Co mamy nowego:** porządek przyczynowy (NGF go nie ma) + trajektorie z pamięcią (klasyczny wzrost sekwencyjny ich nie ma). Czy to zmienia wynik — nieznane. **Szansa porażki wysoka.**
- **Kompas:** zdania przed rachunkiem; kontrole bez pamięci i bez dynamiki; dwa pomiary (kulki w sieci dekoherencji; lorentzowskość porządku); podłogi z tła; przegląd wymiarowy; reguła językowa dla Ø.

**Ryzyka i otwarte:**
- **kryształ:** ograniczona walencja w przeszłość (4 zamiast ~N^(1/2) w sprinklingu 3+1) może dać sieć regularną z globalnie wyróżnioną ramą. W ramie pliku niezmienniczość Lorentza należałaby do strony Ø (pole bez wzbudzeń), a wszystko, co istnieje, jest ramą — wtedy niezmienniczość na dużych skalach musiałaby wyłaniać się **statystycznie** z przypadkowej orientacji ram. Do sprawdzenia, nie do założenia.
- **linki na dużą odległość:** w gęstym sprinklingu odległe zdarzenia prawie nigdy nie są linkiem (C4a.13). W regule wzrostu linki nie są resztką gotowej geometrii, tylko tym, z czego struktura rośnie — więc odległe źródła mogą być linkiem. Zgodność z geometrią sprawdzi estymator wymiaru.
- **który element jest „własnym poprzednikiem” i które trzy dochodzą „bezpośrednio”** — reguła wyboru musi być wewnętrzna; intuicji jeszcze brak.

## C3. Jednostronność — ZAMKNIĘTA

Odpowiedź „sposób mówienia", patrz A5.

## Sito na kształt odpowiedzi — POPRAWIONE

> **POPRAWKA nr 16a (asystent, v3.2).** v3.1: „dopuszczalne są potęgi o wykładniku $a+bd$ z a, b całkowitymi".
>
> Naturalny wykładnik w tej literaturze to $2-2/d$, czyli **$a+b/d$**. Poprawione dopasowanie A4c daje $1{,}542-0{,}661/d$ — też $a+b/d$. A3a daje $k-(k-1)d$, czyli $a+bd$.
>
> **Obie postacie występują. Sito jak zapisane wycinało połowę tego, co faktycznie wychodzi.**

Kształt odpowiedzi niekoniecznie jest prostym stosunkiem x/y — może być stosunkiem stosunków albo logarytmem stosunku (α już jest tego typu). Stosunku niesprowadzalnego nie umiem wykluczyć; jeśli istnieje, znaczy że pierwotnych jest więcej niż dwa — i to jest wynik, nie porażka (A1).

## Dalej otwarte

**Grupa cechowania z porządku.** Nadmiar w samym porządku wymiera jak $n^{2-d}$, więc w d=4 znika. Grupa musiałaby siedzieć w czymś **dołożonym** do elementów — a wtedy nie jest wyprowadzona.

> **Dopisek v3.5 (R1d pkt 3; poprawka 142):** fazy na linkach = definicja pola EM jako relacji, więc zarzut „dołożone do elementów” przestaje działać (relacja faz nie jest treścią dołożoną do elementów). **Sama grupa U(1) nadal nie jest wyprowadzona z porządku** — otwarte.

> **Dopisek v3.5 (poprawka 157) [O]:** rama **nie daje** grupy cechowania z dwóch pierwotnych (potwierdzone). Grupa wymaga elementu spoza porządku i liczności — wg „Sita” to wynik, nie porażka (pierwotnych więcej niż dwa). Plik ustala jego postać: nie byt, nieodczytywalny w punkcie (≡ Ø, „Dopuszczalne stany”), opisywany pośrednio od strony relacji cechowania (jak faza w R1d). Warunkowe wyprowadzenie G_SM i 3 pokoleń z tak ujętego elementu: §F1, poprawki 156–157.

> **Dopisek v3.4 [H]:** brakującym składnikiem we wszystkich pięciu miejscach jest **odległość przestrzenna z porządku** (nakładanie przyczynowe, Boguñá–Krioukov 2024/2025), a nie skala nielokalności — patrz C4a.12.

> **Dopisek v3.3 — pole jako faza na zamkniętych drogach [H][L].** W kontinuum fazy na wszystkich pętlach wyznaczają pole (Giles 1981). W porządku nie ma zamkniętych łańcuchów (antysymetria), więc pętla = łańcuchy w przód i wstecz.
>
> - **Sverdlov–Bombelli (arXiv:0807.2066) [L]:** lagranżjan Yanga–Millsa przez holonomie między parami + relacje + objętości; natężenie z obiegu po trójce punktów. Holonomie **dołożone do wszystkich par, także przestrzennych**. Przekład z kontinuum, nie wyprowadzenie.
> - **Pellegrin (Zenodo 10.5281/zenodo.21865788, 2026, bez recenzji) [L]:** pętla zakotwiczona na parze p≺q (dwa łańcuchy) jest **zawsze czysto elektryczna** (biwektor czasopodobny). „Korona” (dwa elementy dolne, dwa górne, pętla zygzakiem, same linki) ma biwektor przestrzennopodobny w 96–99% → treść magnetyczna; w 1+1 waga magnetyczna ≡ 0 (test, który mógł tylko upaść — przeszedł). Liczby koron $N^{2,34}$ wobec elektrycznych $N^{2,51}$, N=250–24000 (×96), dokładne zliczanie; tłumienie znika przy pętlach nie-linkowych i w obszarze wydłużonym; asymptotyka otwarta. Średni zbiór „między linkami” → 3π w d=4 (przypadek graniczny); prawo linków $2-2/d$ potwierdzone w d=3, 4, nie w d=2. **Faza nadal z kontinuum** (zgodność „do precyzji maszynowej” = Stokes dla stałego pola, kontrola kodu, nie fizyka). Żadna suma po pętlach nie jest zbieżna bez reguły wag — brak cięcia.
> - **Wniosek [A][O]:** treść magnetyczna wymaga **naprzemiennych kierunków relacji**; jednostronne zakotwiczenie daje tylko „czas”.
> - **Propozycja asystenta WYCOFANA [A]:** faza jako płaszczyzny antysymetrycznej części iΔ (pary ±λ). To są **mody pola skalarnego** (Johnston), bez polaryzacji — pułapka nazewnicza. W d=4 funkcja Greena i tak motywowana kontinuum (przegląd Nomaana 2306.04800).
> - **Bezpośrednie oddziaływanie [L]:** Johnston §3.14.3 — nielokalność zbioru przyczynowego pasuje do Wheelera–Feynmana lepiej niż opis różniczkowy. Hemion (1988): elektrodynamika Fokkera na lokalnie skończonym porządku, utknął na prędkościach (u nas A2 ma prędkość). **Przeszkoda wg Johnstona: trzeba znać cały zbiór i „odfiltrować” resztę wszechświata = cięcie.** Wheeler–Feynman jest symetryczny w czasie; asymetria z pochłaniacza (kosmologia). Na zbiorze: WF używa części symetrycznej $G_R$, SJ antysymetrycznej. Bauer–Deckert–Dürr–Hinrichs (1306.3756): istotny jest efektywny opis cząstki w otoczeniu.
> - **Analogia [H]:** jak zachowanie energii — działa lokalnie, nie dla całego wszechświata (brak globalnego wektora Killinga). Całość nie ma otoczenia → nie ma globalnej symetrii ani globalnego cięcia.
> - **Luka obejmuje całą rodzinę stożka [A]:** superekstensywność z mnożenia się linków (Pellegrin) = ta sama nielokalność co d'Alembertiany; dla skalara załatane zewnętrzną skalą nielokalności.

**Czarne dziury — PYTANIE OTWARTE (użytkownik, v3.4).** „Zbyt wyjątkowe miejsca, żeby je pomijać; na pewno trzeba będzie do tego dojść.” Warunek wstępny (użytkownik): **OTW trzeba najpierw oczyścić z interpretacji** — teoria nie mówi nic o zapadaniu, krzywiznach ani nieskończonych gęstościach; rozpatrywać w ujęciu informacyjnym. Nie rozstrzygać przedwcześnie.
- > **Po filtrze: A5d (poprawka 159).** Zdanie (1) — przeszło jako bilans (S = molekuły, nie entropia splątania); (2) — przeszło wyłącznie nie wprost, osobliwość ≡ chwila zero; (3) horyzont zdarzeń — **nie przeszedł** (teleologia: „kiedykolwiek” = całość + kierunek), zastąpiony brzegiem lokalnym [460]; zdanie „nie leżą w przeszłości **żadnego** czytającego” niżej — tak samo teleologiczne. Od strony 3D: z zewnątrz obszar bez odczytywalnego zapisu = brzeg 2D ≡ Ø.
- **OTW bez interpretacji (trzy zdania, do sprawdzenia):** (1) równanie Einsteina jako **równanie stanu** — przepływ energii przez lokalny horyzont = temperatura × przyrost entropii ∝ pole (Jacobson 1995); (2) osobliwość jako **niekompletność** krzywych przyczynowych — łańcuchy urywające się bez elementu końcowego (twierdzenia Penrose'a–Hawkinga), nie gęstość; (3) horyzont jako **brzeg przeszłości** obszaru dalekich obserwatorów — definicja czysto porządkowa. → Czarna dziura = obszar, którego zdarzenia **nie leżą w przeszłości żadnego czytającego z zewnątrz**: zawarte, ale nieodczytywalne.
- **„Osobliwość informacyjna” [L]:** jednego ustalonego pojęcia nie znaleziono; najbliższe: **Stoica** (osobliwości „łagodne” = metryka zdegenerowana, składowe skończone; opis bez nieskończoności, przedłużenie poza osobliwość, redukcja wymiaru; arXiv:1507.03131); **teoria uczenia osobliwego** (Watanabe: degeneracja metryki Fishera = różne stany nieodróżnialne pomiarem); **fuzzballe** (horyzonty i osobliwości jako skutek za małej liczby stopni swobody w opisie). Wspólne: osobliwość = **miejsce utraty rozróżnialności** — to jest ≡ z łańcucha Ø.
- **Trzy możliwe odczyty (bez rozstrzygnięcia):** (a) **agregat informacyjny** — maksymalna entropia przy danym brzegu (Bekenstein–Hawking: entropia ∝ pole horyzontu, nieprzekraczalna); (b) **stabilizacja wzrostu** — lokalne zamknięcie mieszania (ujednolicenie z R2) brzegiem odczytywalności; (c) **coś innego** — np. zdegenerowanie metryki (Stoica).
- **Test możliwy w regule wzrostu:** czy powstają zbiory elementów, które nie leżą w przeszłości końców trajektorii z zewnątrz (brzeg odczytywalności wyznaczony samym porządkiem).

**Co odróżnia pola: czy relacja wraca do siebie [H].** „Pole = struktura, w której wzbudzenia są możliwe” nie odróżnia pól. Hipoteza (rozmowa 5, niepoliczona): nie wraca do siebie → grupa abelowa U(1) (foton, rozchodzi się swobodnie); wraca → nieabelowa SU(3) (gluon, zamyka się). Kontekst: C4a.13.

> **Dopisek v3.5 (R1d; poprawka 142) [L][O]:** przełożone. Nie wraca: F = dA — relacja nie niesie ładunku, abelowa (elektron = relacja). Wraca: F = dA − ig[A,A] — relacja relacji, nieabelowa (kwark). Rozstrzygnięte przekładem; na porządku niepoliczone (wagi obiegów = „działanie”).

**Stałe wzrostu $(t_n)$.** Przestrzeń nieskończenie wymiarowa. Rideout i Sorkin stawiają jako otwarte; 25 lat później struktury generowane dynamicznie nie dają porządków przybliżalnych rozmaitościami.

**Czy stosunek otoczenia do Ø jest niezmiennikiem wzrostu.** Warunek wstępny dla przenoszenia między otoczeniami. **Po §R2 wiadomo, że to jest to samo pytanie co retrospekcja chwili zero.** Niebadane.

**Sztywność (druga wariacja) zamiast działania (pierwszej).** A11d. Nie widziałem policzonej.

**Czy prawo $n^{k-(k-1)d}$ jest w literaturze.** Nie ma go u Minza 2410.02862. **Jedno miejsce prowadzenia tego wątku: „Gdzie zaczynać” 1** (tam też dopisek v3.3: Rideout/Johnston, „pary niehegelowskie” — pojęcie bliźniaków jest starsze niż Minz, ale wykładnika nadal nikt nie podał). Do sprawdzenia: Minz, arXiv 2406.14533.

**Wzór asymptotyczny na średnią liczbę rozszerzeń liniowych** n-elementowego porządku (rozszerzenie dowodu Kleitmana–Rothschilda na pary (P, ≺)) — analityczne narzędzie na dryf f(KR) z A9a. Niesprawdzone.

**Zmiękczony stan SJ** — bez niego liczby z A10 są poprawne, ale nie o próżni.

~~**Weryfikacja twierdzenia z rozmowy 1**, że Poisson Sorkina został częściowo obalony przez CMB.~~ **ROZSTRZYGNIĘTE (v3.5; poprawka 142) [L]:** zdanie z rozmowy 1 było nieprecyzyjne. CMB nie dotyczy rozkładu Poissona (sprinklingu), tylko scenariusza **„everpresent Λ”** (Λ fluktuuje jak 1/√N). CMB ogranicza amplitudę tych fluktuacji (Barrow 2007, gr-qc/0612128; Zwane–Afshordi–Sorkin, CQG 35, 194002 (2018), arXiv:1703.06265); część wersji przechodzi (Das–Nasiri–Yazdi 2023, arXiv:2304.03819). Status: ograniczone, nie obalone; do ramy nic nie wnosi.

**Optymalizacja wyboru obserwatorów** (A9f) — czy trzy dobrze wybrane tory dorównują czterem ustawionym ręcznie.

Uwaga: szukamy w tym, co **już jest**. Trzy powody, dla których stosunek mógł nie wyjść: nikt nie zauważył; uznano za mało istotne; **albo z nieporządku nie chciało wyjść**. W v3.2 doszedł czwarty, częstszy od tamtych: **zauważono i opublikowano, a myśmy nie sprawdzili.**

---

# §D — SPRAWDZONE I NIEUDANE

**Powiększanie: wszystkie pięć reguł wzrostu dają łańcuch.** r ≈ 0,99, d ≈ 1,0–1,2. Przyczyna: **przestrzenność nie jest w tych regułach zdarzeniem, tylko resztą po zdarzeniach.**

> **Sprostowanie v3.2.** Zdanie „nowy element zawsze wybiera przodków, więc zawsze ląduje wyżej, nigdy obok" jest **za mocne**: dołożenie elementu bez przodków jest dopuszczalne. Ale efekt jest ten sam — przy n elementach prawdopodobieństwo, że nowy nie ma żadnego przodka, wynosi $(1-p)^{n-1}$, czyli maleje wykładniczo. **Dokładanie „obok" jest dozwolone i wykładniczo tłumione.** Stąd te struktury wychodzą KR-podobne.
>
> I jest to znane: klasyczny wzrost sekwencyjny Rideouta–Sorkina, którego szczególnym przypadkiem jest perkolacja przechodnia, **nie produkuje zbiorów rozmaitościowych** — potwierdzone własnym rachunkiem (A9b) i opublikowane (Glaser–Surya).

**Stary pomiar rozszerzania mierzył złą zmienną.** Szerokość co 250–500 **elementów**, a numer elementu rośnie liniowo z definicji.

**Punkty izolowane w sprinklingu to artefakt brzegu diamentu**, nie model osobliwości.

**Myrheim–Meyer po całym diamencie jest obciążony.** Kontrola dała 5,41→4,06 zamiast stałego 4. Formuła jest dla **interwału przyczynowego**, nie dowolnego zbioru. **W v3.2 okazało się, że ta sama diagnoza tłumaczy pomiar f z rozmowy 3** (poprawka nr 13) — plik miał ją i nie zastosował do własnej liczby.

**„CMB to nasze plecy" w wersji dosłownej — sprawdzone i nieznalezione.** Wersja prawdziwa: obserwacja wzajemna, nie zwrotna.
*Zastrzeżenie metodologiczne: ten rachunek odpowiadał na twierdzenie, którego nie postawiono.*

**Redukcja wymiarowa d→2 nietestowalna w sprinklingu.** Brakujący element jest konkretny: **struktura, w której d biegnie** (CDT, asymptotyczne bezpieczeństwo, grawitacja Hořavy).

**b(d) nie jest zbieżne w d=2 i d=3** (A5a). Stabilne jest tylko uporządkowanie.

**Aczel nie wykonał ani jednej operacji.** Miał uzasadniać, że w porządku nie ma nieskończonego zstępowania (ufundowanie) — ale każdy porządek częściowy lokalnie skończony jest ufundowany z definicji, więc nic nie wyróżnia. Ta część układu jest **odłączona** od rachunków. **Do skreślenia, chyba że znajdzie się teza, którą ma trzymać.**

**Macierze niesymetryczne dały czas, nie dały wymiaru.** Wymiar części symetrycznej dalej wynosi ~n−1. Czeka na mechanizm selekcji.

*Darmowy fakt formalny:* macierze skośnie symetryczne mają zawsze rząd parzysty. Część „rotacyjna" struktury zawsze rozkłada się na dwuwymiarowe płaszczyzny.

## Nieudane w v3.2

**Fala pp — próg nie reaguje na Weyla.** Napisano sypacz do fali płaskiej w postaci Rosena, $ds^2=-2\,du\,dv+a(u)^2dx^2+b(u)^2dy^2$ z $\ddot a=-A(u)a$ i $\ddot b=+A(u)b$ (warunek próżni: Ricci zero, Weyl niezerowy), $\sqrt{-g}=ab$. Warunek przyczynowy wyprowadzony, nie zgadnięty:
$$2\Delta v\ge\frac{(\Delta x)^2}{\int du/a^2}+\frac{(\Delta y)^2}{\int du/b^2},\qquad \Delta u>0$$

**Kontrole przeszły:** granica płaska zgadza się z Minkowskim liczonym niezależnie w $(t,z,x,y)$ — **0 niezgodnych par na 2 250 000**; przechodniość 0 naruszeń na 200 000 trójek; kaustyka przy $\pi/(2\sqrt{A_0})$.

**Wynik wstępny (wycofany):** przy c=1 (jeden element toru na skalę dyskretności) β przy k=4 rośnie z amplitudą 0,078 → 0,118, dwa poziomy, przejście przy $A_0\approx1{,}2$, **9,0σ**.

**Wynik po sprawdzeniu przedczynnika (obowiązujący):**

| c (gęstość torów) | β przy $A_0$=0 | β przy $A_0$=2,45 | różnica |
|---|---|---|---|
| 1,0 | +0,0931 | +0,1616 | 0,068 |
| 2,0 | +0,0318 | +0,0507 | 0,019 |
| 4,0 | **+0,0062** | **+0,0078** | **0,0016** |

**Podłoga znika przy zagęszczaniu torów, a efekt amplitudy znika razem z nią.** Przy c=2 skan amplitudy jest monotoniczny (0,0315 → 0,0564), bez dwóch poziomów i bez skoku.

**Prawda:** próg wynosi 4 w obu przypadkach. Kaustyka leży poza obszarem dla każdego badanego $A_0$, więc odwzorowanie pozostaje różnowartościowe. Amplituda zmienia **uwarunkowanie** odwzorowania (rozmycie precyzji przy skończonej rozdzielczości), nie próg. **Zdanie „próg rośnie powyżej 4" jest fałszywe.**

**Przyczyna błędu:** związano skalowanie L, nie sprawdzono stałej przy L (poprawka nr 16).

**Reguła stąd:** **wniosek z zakresu węższego niż dekada nie jest wnioskiem** — pierwsza wersja szła po L od 5 do 8. Ale i to nie wystarczyło: trzeba dekady w n **oraz** skanu po każdym parametrze ustawionym przez siebie.

**Nadwyżka informacji przez cięcie nie daje prawa powierzchniowego** (A4e): wykładniki 1,08 i 1,17.

**Trzy schematy obcięcia entropii SJ** (A10) — żaden nie przywraca prawa powierzchniowego, z policzalnego powodu.

**Test odkształceniowy Jacobsona źle zaprojektowany** (poprawka nr 17) — mierzy jeden z dwóch członów, które mają się znosić.

**Dwa intrinsic kryteria wyboru obserwatorów gorsze od ręcznego** (A9f).

## Nieudane w v3.3

**Test plateau w wersji „poddiament D + losowe fragmenty reszty” — źle postawiony.** d=2, N=400, |D|=36, SJ z $G_R=C/2$, 2 realizacje, 8 losowań.
- **Kontrola, która nie przeszła:** czystość. Bez obcięcia S(D)=13,34 wobec S(reszta)=18,96, niezależnie od tolerancji $10^{-6}$…$10^{-12}$ — nie numeryka. Symetria $I(f)+I(1-f)=2S(D)$ też nie.
- **Przyczyna:** reszta zawiera przeszłość i przyszłość D — dla pola to nie są niezależne podukłady (R5 w liczbach). Otoczenie **nie rozkłada się na niezależne fragmenty bez cięcia**: niezależne są tylko podzbiory antyłańcucha, a antyłańcuchy (nawet pogrubione) nie są dobrymi powierzchniami Cauchy'ego (1712.04227).
- **Drugi błąd (asystent):** obcięcie SJ globalne niszczy czystość z konstrukcji; przy c≥0,5 krzywa leży równo na 1,00 od f≈0,4 — **FAŁSZYWE PLATEAU**. Liczby do wyrzucenia.
- Poprawiona wersja: C4.

---

# §F — ZMIANA PUNKTU WIDZENIA: JĘZYK INFORMACJI (plan, v3.4)

**Ustalenie (użytkownik):** to **zmiana języka opisu, nie zmiana tematu**. Te same obiekty, te same otwarte pytania, inny sposób pytania. Powód: pojęcia ramy to zapis, odczyt, rozproszenie i dostępność — czyli pojęcia teorii informacji, a nie geometrii siatek.

**Przekład (nic z wyników nie znika, zmienia się etykieta):**

| dotąd (geometria) | od teraz (informacja) |
|---|---|
| wymiar sieci odczytów | ile kroków kosztuje dotarcie informacji do odległego miejsca |
| krzywizna | czy ten koszt rośnie liniowo z odległością, czy wykładniczo |
| płaskość | liniowy koszt odczytu na dużych skalach |
| hiperboliczność | struktura, w której skróty są tańsze niż droga wprost |
| horyzont | brzeg odczytywalności: zapis zawarty, ale niedostępny |
| pustynia | zakres skal, na których koszt zmienia charakter |

Przykłady przekładu: „3,01 z zadania A” = koszt odczytu rośnie jak pierwiastek trzeciego stopnia z liczby dostępnych miejsc; „ujemna krzywizna R6” = w tej strukturze istnieją skróty.

**Kandydaci na narzędzia (ocena asystenta):**
- **odzyskiwalność informacji** (kwantowa korekcja błędów jako formalizm, nie jako model grawitacji): „zawarte, ale nieodczytywalne” jako **wielkość liczbowa**; jeden język dla H.M., 200 klocków i horyzontu. **Najbliżej ramy.**
- **złożoność / kompresowalność opisu:** „ile kosztuje odtworzenie stanu z zapisu” — dosłownie przykład z klockami (mózg przegrywa, bo opis przekracza pojemność; aparat wygrywa). Zastrzeżenie: w ogólności nieobliczalna, pracuje się na przybliżeniach.
- **redundancja Zurka jako narzędzie** (nie cytat): plateau = ilu niezależnych świadków ma ten sam zapis. **Najtańsze — kod już mamy (C4a).**
- **termodynamika informacji** (Landauer, Bennett): kasowanie kosztuje, odczyt nie — jedyne miejsce, gdzie zapis i odczyt mają jednostki; może być potrzebne przy masie.
- Z czwórki użytkownika: **nawigowalność sieci** (Boguñá–Krioukov) — tania, liczona na gotowych strukturach, mierzy, czy odczyt lokalny wystarcza do dotarcia; **kod HaPPY** — naturalny dom dla „zawarte vs odczytywalne”, ale wymaga stanów kwantowych; **sieci tensorowe (MERA)** — dodatkowy wymiar = skala, struktura hiperboliczna: możliwe rozpoznanie rodziny, w której wylądował R6; **Wolfram** — nasze reguły to przepisywanie hipergrafów, wartość głównie katalogowa.

**Zastrzeżenie (asystent):** te języki mierzą **dostępność zapisu**; żaden sam z siebie nie powie, skąd bierze się przestrzeń. Pytanie „dlaczego przestrzeń jest prawie płaska” brzmi w nich „dlaczego koszt odczytu rośnie liniowo, a nie wykładniczo” — to samo pytanie, nadal otwarte.

## §F1. MASA — następny temat (plan)

> **HIPOTEZA NADRZĘDNA [H] (użytkownik, 25.09; poprawka 136):** „To będzie układ samopodobny, aż do całego wszechświata. Masa nie może być oddzielnym, ostatnim etapem, do którego można dojść krok po kroku. Żaden krok tam nie zaprowadzi. To musi być ustalone wszystko na raz.”
> - **W ramie już jest [O]:** hierarchia węzłów od 2D Plancka do całości (Wheeler–DeWitt), oba końce ≡ Ø, „mechanizm ogólny na każdej skali” [402, 404]; „wszystko naraz” [392, 402]; R1d: masa = jednostronna relacja nośnika z tłem wszędzie tym samym = relacja węzła z całością.
> - **Odpowiednik formalny [L][O]:** samopodobieństwo = brak wyróżnionej skali; jedyna miara niezmiennicza względem skali to du/u → logarytm. ~~**Każdy logarytm w dokumencie jest śladem samopodobieństwa:**~~ **Za szerokie (poprawka 146) — dotyczy tylko logarytmów typu S (tabela niżej):** ln n (§F2, ∫du/u), T/V ∝ ln W (etap18), ln(n₀/n) biegnących sprzężeń (R1d), 1/α ∝ ln(N_Λ/N) (A2). „Dynamika wymusza logarytm” [94] = struktura jest samopodobna. **Masa = miejsce, gdzie samopodobieństwo się łamie** (logarytm sięga jedności: n_Λ = n·e^{2π/(bα)}) — skala jako wykładnik stosunku sprzężeń obejmującego cały zakres, nie wynik kroku. Pustynia [545] = zakres bez łamania samopodobieństwa.
> - ~~**Konsekwencja dla planu:** … jedna relacja między końcami hierarchii (Planck ≡ Ø, całość ≡ Ø), z której wszystkie skale wychodzą jako wykładniki logarytmów liczebności („zespół funkcji logarytmicznych” [94]).~~ **BŁĄD ASYSTENTA (poprawka 151):** „jedna relacja między końcami” to dopisek asystenta z sesji CC 2 [105], nie hipoteza użytkownika [104], i **przeczy [94]** („na pewno nie dostanę jednej prostej funkcji, albo jednego stosunku. Kwarki i elektrony na to nie pozwalają”).
> - **Konsekwencja dla planu (poprawiona, 151):** masa nie jest krokiem po czasie/3D/świetle, tylko ustala się razem z nimi. **Celem jest sam zespół funkcji** [94] — funkcje biegu bezwymiarowych stosunków (β dla sprzężeń, γ dla mas) od logarytmu stosunku skal (liczebności), dwóch typów (relacja / relacja relacji), **samopodobny i ustalany naraz** [104]. **Liczby (1/137, y_e, …) to wartości funkcji w jednym stanie** [88] — odczyty, nie cel; „same wyskoczą po drodze”.
> - **Przekształcenia są już w pliku [H][L]:** użytkownik [86] → A2 (ładunki z N_c i anomalii, hiperładunki, współczynnik beta (−1)^{2s}(4s² − ⅓), 1/α jako ln(N_Λ/N) z nachyleniem ΣN_cQ² = 8); R1d (biegnące sprzężenia w liczebności obiegu, transmutacja); R1e/145 (pochodzenie ⅓, liczba polaryzacji). **Jawnie brak tylko biegu mas** [L][O]: m(μ₁)/m(μ₂) = [α_s(μ₁)/α_s(μ₂)]^{γ₀/(2b₀)}, wykładnik 12/(33 − 2n_f) (γ₀ = 8 z koloru, b₀ = 11 − ⅔n_f) — **stosunek mas = stosunek sprzężeń do potęgi stosunku współczynników** = dosłownie „stosunek dwóch stosunków do stosunku” [94]; wszystkie wejścia z listy 147. Dla elektronu (QED) wykładnik innego znaku i typu (relacja zamiast relacji relacji) — „kwarki i elektrony nie pozwolą na jedną funkcję”. Kwark odczytywalny tylko jako m_b(m_b) — „stosunek odniesiony do stosunku” [95].
> - ~~**Zdanie do upadku:** istnieje skala niewyprowadzalna z ilorazu końców hierarchii, niezapisywalna jako wykładnik logarytmu liczebności.~~ **PUSTE — błąd asystenta (poprawka 139):** każdą liczbę da się zapisać jako exp(ln x), więc zdanie nie może upaść. **Poprawione:** wykładniki muszą pochodzić **wyłącznie z policzonych współczynników** (b₀, 2π, ΣN_cQ², (−1)^{2s}[(2s)² − ⅓], liczebności porządku) — **lista dozwolonych wejść zapisana przed rachunkiem, bez żadnej stałej dopasowywanej**. Upada, gdy dla którejś skali takiego zapisu nie ma.
> - **Precedens i ostrzeżenie [L][H]:** bootstrap konforemny (wykładniki z samej spójności, bez kroków). Ostrzeżenie: numerologia Diraca i Eddingtona — przykład pułapki: **ln(R_H/l_P) = 140,3** (H₀ = 67,4) wobec 1/α ≈ 137. Literatura do §F1: **Meissner–Nicolai, Phys. Lett. B 648, 312 (2007)** — klasycznie konforemny Model Standardowy, skale z łamania radiacyjnego (logarytmy).
> - **Masa, środek, kula — jeden warunek [L][T] (Wigner 1939):** cząstka masywna ma układ spoczynkowy i grupę SO(3) wokół środka; bezmasowa ma E(2) i nie ma układu spoczynkowego. W ramie: masa ⇔ środek μ i własna oś czasu ⇔ kula 3D wokół środka (R1b) ⇔ wnętrze stożka (R1c); bez masy tylko brzeg (światło). „Kula = suma wszystkich odczytów w relacji do środka” [H].
> - **Dwa promienie wokół jednego środka [O]:** r_s/ƛ_C = 2(m/m_P)² (tożsamość, niczego sama nie wyprowadza). Spotykają się przy m = m_P/√2 (dół); dla sfery Hubble’a przy gęstości krytycznej **r_s = R_H dokładnie** (góra; A2: R_s/R = (R/R_H)²), dla obserwowalnego wszechświata co do rzędu. **Oba końce hierarchii to miejsca, gdzie te dwa promienie się pokrywają.**
> - **Sfera fotonowa = samoodczyt przez pętlę światła [H][O]:** na r = 1,5 r_s światło krąży po okręgu — patrząc poziomo widzi się tył własnej głowy: przeszłość jako zapis czytany teraz, tym razem zapis siebie. Jedno okrążenie 3π r_s/c = wartości z A5b (9,3·10⁻⁵ s Słońce, 399 s Sgr A*, 7,0 d M87*) — **na zegarze dalekiego czytającego; na własnym zegarze stojącego na sferze × √(1/3): 5,4·10⁻⁵ s, 231 s, 4,0 d.** „Ile temu” należy do relacji z czytającym (R1d: energia = częstość odczytu względem czytającego). Tempo samoodczytu pętlą ~ 1/m, częstość Comptona (zygzak, R1d) ~ m; przecinają się przy m ≈ 0,23 m_P (zegar daleki) / 0,30 m_P (własny) — skala Plancka. **Obraz [H]: poniżej m_P nośnik czyta siebie przez zygzak, powyżej przez pętlę światła; na granicy oba sposoby się spotykają** (formalnie ta sama tożsamość dwóch promieni).
> - **Lustro tylko w 3D [L][T]:** ƛ_C ↔ r_s przy m → m_P²/m (Carr, arXiv:1402.1427; wyższe wymiary: arXiv:1611.01913). W d wymiarach przestrzennych r_s ∝ m^{1/(d−2)}, ƛ_C ∝ 1/m — **dokładne lustro tylko przy d = 3**. Zygzak i pętla światła są swoimi odbiciami wyłącznie w 3D — ten sam wymiar co z R1b, niezależną drogą. Końce: przy m_P oba samoodczyty ≡ (l_P t_P ≡ Ø); na sferze Hubble’a pętla obejmuje całość bez otoczenia (t = 0). [?] lustro m ↔ m_P²/m jako najprostszy formalny przypadek samopodobieństwa.
> - **TABELA LOGARYTMÓW (poprawka 146) [A][O].** Dwa typy (oba = „koszt wskazania” z §F2, ale tylko S należy do §F1):
  - **typ S (skala, ∫du/u)** — wskazanie jednej skali spośród rozłożonych samopodobnie = ślad samopodobieństwa;
  - **typ K (kombinatoryka, ln liczby możliwości)** — wskazanie jednej spośród równoprawnych (ln n!); **samopodobieństwa tu nie ma**.

| logarytm | typ | po czym biegnie | współczynnik | status |
|---|---|---|---|---|
| koszt wskazania ramy ln n (etap10–11, §F2) | S | tyknięcie / dyskretność, n ∝ ρ/m⁴ | **1, policzony [T][P], także w 3+1** | **jedyny logarytm dokumentu przechodzący do 3+1**, masa pod logarytmem |
| ln N z §F2 (linki, ściany, D) | S | zakres pchnięć, ln N = 2 ln(ℓ/t_P) | 1 i ⟨α²⟩ = 0,834 policzone; 0,57 zmierzone | tylko 1+1; w 3+1 potęga (§E) |
| biegnące sprzężenia ln(n₀/n) (R1d) | S | obieg odczytu | b/2π z listy wejść [L] | przełożone |
| 1/α ∝ ln(N_Λ/N) (A2) | S | jw. | ΣN_cQ² = 8 policzone | [P] |
| transmutacja n_Λ = n·e^{2π/(b₀α_s)} (R1d) | S | jw. | 2π, b₀ | [L]; **wymaga wartości brzegowej α_s** |
| Λ ~ N^{−1/2} („everpresent Λ”, Sorkin) | S/K | liczebność całości | **½ z Poissona, policzone** [L] | postać dokładnie taka, jakiej żąda poprawka 139; CMB ogranicza amplitudę fluktuacji (Dalej otwarte) |
| log e(C), D = log n! − log e(C) (A4, A11) | K | uporządkowania | f(d) zmierzone | nie samopodobieństwo |
| nadwyżka sprzężenia log C(n, n_A), koszt relacji −log Pr (A11) | K | przeploty | policzone | jw. |
| entropia SJ (1/6)·ln N (C4a.16) | — | liczba modów po cięciu | — | **artefakt procedury cięcia** (poprawka 51) |
| T/V ∝ ln W (etap18) | ? | — | zmierzone | **z migawki sztywnej wykluczonej filtrem** (zero absolutne); tylko z tą adnotacją |
| ln(R_H/l_P) = 140,3 | — | — | — | pułapka numerologii |

- **LISTA DOZWOLONYCH WEJŚĆ (poprawka 147; zapisana przed jakimkolwiek rachunkiem):**
  - **wolno:** d = 3 (R1b); 2π (obieg fazy); (−1)^{2s}, (2s_z)², ⅓ na stan, liczba polaryzacji d − 1 (R1e); N_c, n_f, ΣN_cQ², liczba pokoleń 3; współczynniki strukturalne policzone w dokumencie: 1 (koszt wskazania ramy), ½ (Poisson), ∫f(w)dw konfiguracji; **jedna liczebność: stosunek końców hierarchii (Planck ≡ Ø ↔ całość ≡ Ø)**;
  - **nie wolno:** wartości zmierzone (α(m_Z), y_e, v); współczynniki tylko zmierzone (f(d), 0,57), dopóki nie zostaną policzone.
  - **Zdanie do upadku (doprecyzowane):** dla każdej skali **jedna** kombinacja wejść, zapisana przed rachunkiem; przeszukiwanie kombinacji = numerologia (Eddington). Upada, gdy któraś skala wymaga wejścia spoza listy.
  - ~~**Pytanie właściwe §F1**~~ **Pytanie poboczne (poprawka 151; cel = zespół funkcji, nie wartości [88]) [A][O]:** biegnące sprzężenia potrzebują **wartości brzegowej** (1/α(n₀)). W hipotezie „wszystko naraz” może ona pochodzić tylko z **warunku na obu końcach** (oba ≡ Ø). Pytanie brzmi: **jaki warunek na końcach ustala wartości brzegowe** — pytania o y_e czy α z osobna są źle postawione.
- **Grupa renormalizacji po filtrze [L][O]:** Kadanoff (1966, bloki spinów), Wilson–Kogut (1974); „przepływ UV → IR” przemyca kierunek — w ramie **relacja między rozdzielczościami odczytu**; zgrubienie = odczyt przy mniejszej rozdzielczości = więcej nierozróżnialnych = zapis rozproszony. [?] monotoniczność c/a (Zamolodchikov 1986; Komargodski–Schwimmer 2011) ↔ A4d/138 — A4d dotyczy dokładania elementów, nie zgrubienia.
- **STAN ZESPOŁU — zestawienie po 166 (poprawka 167) [O].** Tabela z końca sesji 3 (zapis sesji 3, [91]; wtedy niewpisana), sprawdzona wobec pliku i uzupełniona o 166. Mapa, nie treść — treść w poprawkach podanych w nawiasach.

| co | stan |
|---|---|
| **funkcje** (policzone, bez dopasowania) | 3 sprzężenia: b = 41/6, −19/6, −7 (152); 9 Yukaw fermionów naładowanych **tylko jako stosunki** — odczyt B (166), wykładniki wymierne; wewnątrz typu biegnie tylko 3. pokolenie przez y_t, e : μ : τ stoją (153); λ: 24λ² + część bez λ = supertrace (155 D); CKM i θ_QCD jednopętlowo praktycznie nie biegną (153) |
| **wyprowadzenie współczynników** | z elementów ramy: (−1)^{2s} = znak 2π, (2s_z)² (R1e); −⅓ = obiegi dyskretne wobec miary („sztuki czy miara”); d = 3 (logarytm, 3 polaryzacje; [?] 3 w γ_m); c (εμ = 1); ładunki z anomalii i N_c (155). **Niewyprowadzone:** grupa cechowania i liczba pokoleń (warunkowo 156–158); człon 3/2(Y_u†Y_u − Y_d†Y_d) (cytowany, 155 C) |
| **pojęcia** | wszystkie pojęcia zespołu mają definicje w ramie (R1f-4); kolor i Casimiry warunkowo (156–157) |
| **odczyty** | 19 = 3 sprzężenia + 9 mas (w zespole: Yukawy — odczyt B, 166) + 4 CKM + 2 Higgs (λ, μ²) + θ_QCD; N równań → N wartości w jednym (dowolnym) punkcie odniesienia = spójność [88] z matematyką, nie odkrycie (153, 165) |
| **ustalone strukturą i trafione** | λ = 0 i β_λ = 0 na końcu Plancka (Ø z Ø nie jest relacją; sąsiedztwo nieodróżnialne) → m_H i m_t związane; natura na granicy stabilności, zgodność co do kilku σ (dokładna krytyczność: m_H = 129,4 ± 1,8 GeV wobec 125) — **jedyne trafienie** (154) |
| **ustalone strukturą, nietrafione** | R\* = 2/9 (Pendleton–Ross; w naturze R(m_t) ≈ 0,65) i quasi-punkt Hilla (≈ 203 GeV wobec 173) — wykładnik 1/b₃ = −1/7 mały wobec pustyni (165) |
| **nieustalone — rama nie daje warunku** | e : μ : τ — 0 warunków na 2 stosunki (166); empirycznie Q = 2/3 i δ = 2/9, tylko na odczycie A, niewyprowadzone; hierarchia pokoleń — zespół ślepy, niosą ją wyłącznie odczyty jednostronnej relacji z tłem (154 pkt 2); stałe z całości: Ĥ\|Ψ⟩ = 0 ich nie ustala (150) |
| **otwarte** | CKM; θ_QCD; y_e (skala relacji z tłem); grupa i 3 pokolenia warunkowo (156–158); krytyczność λ policzona wprost na porządku; sztywność (A11d) |
| **zastrzeżenia** | jedna pętla; progi mas zmieniają n_f; brak neutrin; G i Λ poza zespołem (152) |

- **ZESPÓŁ FUNKCJI [94] — wypisany (poprawka 152) [L][P][O].** Jedna pętla, zakres bez skal pośrednich (pustynia [545]); współczynniki sprawdzone rachunkiem na ułamkach z ładunków A2 (N_c = 3, 3 pokolenia). Zmienna: **t = ln(n₀/n)** — logarytm stosunku liczebności obiegu (R1d); znak t = konwencja (który czytający jest odniesieniem), bez kierunku.
  - **Poziom 1 — sprzężenia (relacje), 3 funkcje:** 1/α_i(t) = 1/α_i(0) − (b_i/2π)·t, wszystkie b z jednego wzoru A2: **b = −Σ (−1)^{2s}(4s² − ⅓)·T(R)** (wektor × C_A, każdy fermion Weyla, każdy skalar zespolony).

| relacja | b_i | skład | typ |
|---|---|---|---|
| U(1)_Y | **41/6** | fermiony 20/3 + Higgs 1/6 (ΣY² z hiperładunków A2) | **relacja** (b > 0, tylko ekranowanie) |
| SU(2) | **−19/6** | wektor −22/3 + fermiony 4 + Higgs 1/6 | **relacja relacji** |
| SU(3) | **−7** | wektor −11 + kwarki 4 | **relacja relacji** |

    Każda funkcja to prosta w t: przesunięcie punktu odniesienia zmienia tylko punkt odczytu — **samopodobieństwo dosłownie**. Łamie się, gdzie 1/α₃ → 0 (transmutacja, R1d).
  - **Poziom 2 — masy (stosunek stosunków), 9 funkcji fermionów naładowanych:** ~~bez samosprzężenia Yukawy (dobre dla wszystkich poza top): y_f(t)/y_f(0) = Π_i [α_i(t)/α_i(0)]^{p_i}~~ **BŁĄD ASYSTENTA (poprawka 153; uwaga użytkownika):** pominięty wspólny człon śladowy **T = Tr(3Y_u†Y_u + 3Y_d†Y_d + Y_e†Y_e) ≈ 3y_t²** (renormalizacja pola Higgsa), wchodzący do biegu **każdego** y_f. Nie jest mały: przy m_t T ≈ 2,65 wobec części cechowania leptonów 9/4·g² + 15/4·g′² ≈ 1,43 (pominięte prawie 2× większe od uwzględnionego); dla kwarków ~24% części QCD (8g₃² ≈ 10,9). Ponadto m_f = y_f·v/√2, a bieg v powyżej skali elektrosłabej zależy od cechowania → **pojedyncza „masa biegnąca” nie jest tam czystym obiektem; stosunek jest.** **Poziom 2 — poprawnie, od razu dla stosunków:** T i v skracają się w każdym stosunku, więc dla dwóch typów f, f′: **(m_f/m_f′)(t) / (m_f/m_f′)(0) = Π_i [α_i(t)/α_i(0)]^{p_i(f) − p_i(f′)} × (czynnik różnic Yukaw, poziom 3)**, p_i = −c_i/(2b_i) — stosunek mas = iloczyn stosunków sprzężeń do potęg będących różnicami stosunków policzonych współczynników = „stosunek stosunków” [94] w pełnej postaci. c_i = 3·[C_i(L) + C_i(R)] (Casimiry i hiperładunki).

| typ | c₁ | c₂ | c₃ | p₁ | p₂ | p₃ |
|---|---|---|---|---|---|---|
| u, c, t | 17/12 | 9/4 | 8 | −17/164 | 27/76 | **4/7** |
| d, s, b | 5/12 | 9/4 | 8 | −5/164 | 27/76 | **4/7** |
| e, μ, τ | 15/4 | 9/4 | **0** | −45/164 | 27/76 | **—** |

    Kontrola: p₃ = 4/7 = znane 12/(33 − 2n_f) przy n_f = 6; poniżej progów 12/23, 12/25, 4/9. **Kwark: 3 czynniki, elektron: 2 (bez relacji relacji koloru) — dwa kształty funkcji, nie jedna [94].**
  - **Poziom 3 — czego zespół nie przenosi (poprawione, 153):** stosunki mas wewnątrz typu mają identyczne wykładniki cechowania i wspólne T → te czynniki się skracają. ~~prawie nie biegną (tylko samosprzężenie Yukawy, istotne dla top)~~ **Błąd asystenta:** równanie dla Y_d zawiera 3/2(Y_d†Y_d − Y_u†Y_u); w bazie kwarków dolnych Y_u†Y_u przechodzi przez CKM → wkład top −3/2·y_t²·|V_ti|²: b (|V_tb|² ≈ 1) ≈ −1,3, s (|V_ts|² ≈ 1,6·10⁻³) i d (|V_td|² ≈ 8·10⁻⁵) pomijalne. **Poprawnie: wewnątrz typu biegnie tylko trzecie pokolenie, przez y_t, w obu typach kwarków (t: +3/2·y_t², b: −3/2·y_t²).** W równaniu leptonów nie ma Y_u (tylko 3/2·Y_e†Y_e) → **e : μ : τ biegną jedynie przez y_τ², praktycznie stoją.** Stosunki między typami biegną: m_b/m_τ — p(d) − p(e): 4/7 od koloru, +40/164 od U(1) **oraz −3/2·y_t² od top** (znany czynnik w unifikacji b–τ). CKM (4 liczby): jednopętlowo tylko przez Yukawy, prawie stoi.
  - **Poziom 4 — relacja tła z samym sobą, 1 funkcja:** 16π²·dλ/dt = 24λ² + 12λy_t² − 6y_t⁴ − 3λ(3g₂² + g′²) + ⅜[2g₂⁴ + (g₂² + g′²)²]. W ramie: nierozróżnialne tło (Higgs ≡ Ø, R1d) w relacji z sobą i z nośnikami; tu krytyczność z 148 (λ, β_λ ≈ 0 przy Plancku).
  - **Stosunek ustalony przez sam zespół [L][T][P] (przepisane bez kierunku — poprawka 165):** R = y_t²/g₃², jedna pętla, QCD + top: 16π²·d ln R/dt = 2g₃²(9/2·R − (8 + b₃)), 16π²·d ln g₃²/dt = 2b₃g₃² ⇒ dla u = 1/R: **(1/R − 9/2) ∝ α₃^{1/b₃} = α₃^{−1/7}**, czyli **(1/R₁ − 9/2)/(1/R₂ − 9/2) = (α₃₁/α₃₂)^{1/b₃}** dla **dowolnych dwóch** punktów odniesienia — stosunek stosunków z policzonym wykładnikiem 1/b₃, bez wyróżnionego „początku”. **R\* = 2/9** (u = 9/2; Pendleton–Ross 1981) = jedyny stosunek, dla którego odchylenie znika — ustalony z samych współczynników, bez żadnego odczytu; **w naturze niezrealizowany:** R(m_t) ≈ 0,65. **„Ustala, ale za wolno” (użytkownik, 153) — w ramie:** wykładnik 1/b₃ = −1/7 jest mały wobec zakresu pustyni: α₃ zmienia się w całej pustyni ~5,7× (0,108 ↔ 0,019), więc odchylenie (1/R − 9/2) tylko **~1,28×**. **Quasi-punkt Hilla** (Phys. Rev. D 24, 691 (1981)) w tej samej postaci: gdy R ≫ 1 w jednym punkcie, w drugim R = 1/[9/2·(1 − (α₃₁/α₃₂)^{1/b₃})] ≈ 0,995 → y_t ≈ 1,17, m_t ≈ 203 GeV (tylko QCD + top, jedna pętla; zmierzone 173) — drugi stosunek ustalony strukturą, też nietrafiony. **Sprawdzenie** `etap22_pendleton_ross.py`: relacja zachodzi do 4·10⁻¹⁴ dla R = 0,1 / 2 / 50 w jednym punkcie; kontrola: wykładnik 1/b₃ ± 20% — różnica ~5% (nie zachodzi). *Poprzednie sformułowanie („przyciąga w podczerwieni… od Plancka do m_t R nie zdąży dojść”) — przebieg z kierunkiem; zastąpione.*
  - **Wnioski [O]:** (1) **kształt zespołu jest w całości policzony** — wykładniki i nachylenia to liczby wymierne z listy 147 (spin, N_c, hiperładunki, 3 pokolenia); dopasowania nie ma nigdzie. (2) ~~~17–19 „wolnych danych” = dokładnie jeden odczyt na funkcję — wniosek~~ **(poprawione, 153):** N równań pierwszego rzędu wymaga dokładnie N wartości w jednym (dowolnym) punkcie odniesienia t — *nie „początkowych”: początek nie jest wyróżniony (165)*, więc „jeden odczyt na funkcję” to **spójność [88] z matematyką, nie odkrycie**. Liczba: 3 sprzężenia + 9 mas + 4 CKM + 2 Higgs (λ, μ²) + **θ_QCD** (brakowało; jednopętlowo nie biegnie) = **19**. **Treść jest tam, gdzie struktura sama ustala któryś z odczytów** (jak Pendleton–Ross, Hill). (3) **Pokolenia = trzy kopie tych samych funkcji;** zespół ich nie odróżnia — hierarchię między pokoleniami niosą wyłącznie odczyty; jedyne, co zespół mówi o pokoleniach: faza nieusuwalna wymaga ≥ 3 kopii (R1d, Kobayashi–Maskawa).
  - **Zastrzeżenia:** jedna pętla; progi mas zmieniają n_f; brak neutrin; G i Λ poza zespołem (G ustala jednostkę).
- **TEST WIERNOŚCI DLA (b) — według pliku (poprawka 157) [T][L][O].** Zdania pliku użyte: „Dopuszczalne stany” (całkowity brak otoczenia wypada z układu); R1 („O Ø nie da się nic powiedzieć — liczyć wyłącznie w relacji do znanego otoczenia”) + pułapka 1; A1/R5 (dwa pierwotne); „Dalej otwarte” (grupa „w czymś dołożonym → nie wyprowadzona”); „Sito” (stosunek niesprowadzalny ⇒ pierwotnych więcej niż dwa — wynik, nie porażka); „Cel” (nie nowe byty); A0 (liczba, która mogłaby wyjść inaczej).

| zdanie (b) | ¬P | wyklucza się z | wynik |
|---|---|---|---|
| **1. w punkcie ≡ Ø** | sektor oktonionowy odczytywalny w punkcie sam z siebie | J₃(𝕆) nie tworzy złożeń z żadnym układem kwantowym (Barnum–Graydon–Wilce, Quantum 4, 359 (2020), arXiv:1606.09331 [T]; wyjątek: składnik czysto klasyczny) → brak możliwego otoczenia → **„całkowity brak otoczenia wypada z układu”** (Dopuszczalne stany); także „cecha” [36, 94] | **PRZESZŁO** |
| **2. dlaczego 𝕆, a nie ℂ, ℍ, M₃(ℂ)** | — | **źle postawione:** pytanie, jaką algebrą jest Ø w punkcie; plik: „O Ø nie da się nic powiedzieć — liczyć wyłącznie w relacji do znanego otoczenia”. **Pierwsza wersja testu (argument z maksymalności: 𝕆 największe w kierunku Hurwitza, ale J₃(𝕆) nie zawiera J_n(ℂ), n ≥ 4) próbowała rozstrzygnąć od strony Ø — ten sam błąd co poprawka 65.** Postać opisu pośredniego ustala otoczenie = odczytane relacje cechowania (G_SM) | **ŹLE POSTAWIONE** (błąd asystenta) |
| **3. relacje między punktami odczytywalne** | brak relacji | sektor bez relacji nie ma otoczenia → wypada z układu = (a); istnienie sektora = istnienie jego relacji; rozstrzyga pomiar (kolor odczytywany) | zgodne z plikiem; decyduje obserwacja |

  - **Werdykt (stanowczo):** (1) **grupa cechowania nie wynika z dwóch pierwotnych** (plik, „Dalej otwarte”); 156 wyprowadza ją z elementu spoza porządku i liczności — **wg „Sita” to wynik, nie porażka: pierwotnych jest więcej niż dwa.** (2) **Postać trzeciego elementu jest przez plik ustalona:** nie byt („Cel”), nie odczytywalny w punkcie (wiersz 1) → tylko (b): **milczenie w punkcie, opisywane pośrednio od strony relacji cechowania** (wzór R1d dla fazy). (3) **Którą algebrą opisać to milczenie, ustala otoczenie, nie Ø:** 𝕆 ⊃ ℂ i M₃(ℂ) Connesa opisują to samo otoczenie G_SM. (4) **Różni je kryterium A0** (nie ocena): droga oktonionowa daje liczbę, która mogła wyjść inaczej — pokoleń ≤ 3, z [126] = 3 (obaliłoby ją czwarte pokolenie / N_ν ≠ 3); droga Connesa o pokoleniach milczy (3 = wejście). Wg A0 w sprawie pokoleń komunikacją jest tylko droga oktonionowa; utożsamienie „pokolenia = 3 z J₃(𝕆)” zostaje [?].
- **Uzupełnienie z rozmów (poprawka 158) [H][O]:** (1) **[104] (użytkownik): „[Ø ≡ … ≡ Ø] ≠ R ⊗ R — iloczyn tensorowy relacji przez relację. Czyli świat relacji złożonych z relacji.”** Świat = R ⊗ R (złożenia); J₃(𝕆) nie ma iloczynu tensorowego (Barnum–Graydon–Wilce) → **nie należy do R ⊗ R**, zostaje po stronie nawiasu [Ø ≡ …] = postać (b). Bezpośrednie zdanie użytkownika, mocniejsze niż „Dopuszczalne stany” — wiersz 1 testu (b) przechodzi przez [104]. (2) **Termin „relacja relacji”:** u użytkownika — przestrzeń [78] („przestrzeń to jest relacja relacji”), masa [94], świat R ⊗ R [104]; u asystenta (R1d/133, 152, 154, 156) — węższy odczyt: relacja nieabelowa (pole niosące ładunek), CKM. Niekoniecznie sprzeczne (pole niosące ładunek = relacja wchodząca w relacje), ale **to odczyt asystenta, nie znaczenie nadane przez użytkownika**; do rozstrzygnięcia. (3) **Droga oktonionowa (156–157) nie pochodzi z rozmów** (o 𝕆 i pokoleniach nic poza [94], [126]) — propozycja asystenta + literatura; zasada metody: „nie mnożymy hipotez” → utożsamienie z pokoleniami zostaje [?], jej rozwijanie = dokładanie hipotez.
- **GRUPA CECHOWANIA I LICZBA POKOLEŃ — wyprowadzenie warunkowe (poprawka 156) [T][L][O][?].**
  - **Algebra odczytów [T][L]:** odczyty bez kolejności → algebra Jordana (A∘B = ½(AB + BA) przemienny = niezależny od kolejności, R1b-F P2b, [394]; „suma kwadratów = 0 ⇒ wszystkie = 0” = dodatniość, R1c). Klasyfikacja kompletna (Jordan–von Neumann–Wigner 1934): J_n(ℝ), J_n(ℂ), J_n(ℍ), czynniki spinowe (kule), **jeden wyjątek J₃(𝕆)**. R1b wybiera z tej listy: J₂(𝕂) = kula B^{1+dim 𝕂} → B², **B³**, B⁵, B⁹ dla ℝ, ℂ, ℍ, 𝕆; d = 3 ⇔ 𝕂 = ℂ. Hurwitz: ℝ, ℂ, ℍ, 𝕆 = jedyne układy liczbowe, w których stosunki składają się z zachowaniem normy (|xy| = |x||y|) — pełna lista algebr „stosunku stosunków”; 𝕆 największa i zawiera pozostałe.
  - **Grupa [L][O]:**

| krok | treść | status |
|---|---|---|
| 1 | R1b wybiera ℂ (jednostka urojona i); w 𝕆: 𝕆 = ℂ ⊕ ℂ³ | [T] |
| 2 | przekształcenia 𝕆 zachowujące i: Aut(𝕆) = G₂ ⊃ **SU(3)** | [T] Günaydin–Gürsey, J. Math. Phys. 14, 1651 (1973) |
| 3 | oktonionowy „kubit” J₂(𝕆) = B⁹ → **Spin(9)** (stabilizator idempotentu w F₄ = Aut J₃(𝕆)) | [T] |
| 4 | **część Spin(9) zachowująca 𝕆 = ℂ ⊕ ℂ³ = G_SM = (SU(3) × SU(2) × U(1))/ℤ₆** | [L] Dubois-Violette–Todorov–Drenska; Todorov–Dubois-Violette, arXiv:1806.09450; Krasnov, arXiv:1912.11282, doi:10.1063/5.0039941 |

    **W ramie [O]:** grupa cechowania = przekształcenia wyjątkowej algebry odczytów, które **nie odróżniają niczego ponad to, co już odróżnia przestrzeń (ℂ z R1b)**; wymiar 36 → 12 (8 + 3 + 1). ℝ daje tylko {±1}, wykluczone przez P0 (niespójna) — brak cechowania z ℝ, zgodnie z naturą. Alternatywa [L]: Chamseddine–Connes („Why the Standard Model”, 2007): algebra łączna ℂ ⊕ ℍ ⊕ M₃(ℂ) z M₂(ℍ) ⊕ M₄(ℂ), bez 𝕆; 3 = 4 − 1 (lepton = czwarty kolor), liczba pokoleń = wejście.
  - **Pokolenia [T][L][?]:** **≤ 3:** J_n(𝕆) jest algebrą Jordana tylko dla n ≤ 3 (niełączność 𝕆) [T]; utożsamienie „pokolenia = 3 z J₃(𝕆)” [?] (Dubois-Violette 2016; Boyle, arXiv:2006.16265 — trójkość Spin(8)). **≥ 3:** asymetria [126] wymaga łamania CP (Sacharow), faza nieusuwalna dopiero przy ≥ 3 (Kobayashi–Maskawa) [T][L]. **= 3** warunkowo na utożsamieniu. **Spójność ze 153–154 [O]:** trzy pozadiagonalne oktoniony J₃(𝕆) = 8_v, 8_s, 8_c grupy Spin(8), permutowane przez S₃ (trójkość) [T] = „pokolenia = trzy kopie, zespół ślepy”: funkcje cechowania szanują S₃, łamią ją tylko odczyty jednostronnej relacji z tłem (Yukawy); S₃ = symetria zapachowa ze 154. Potwierdzenie, nie podpora: N_ν = 3 (szerokość Z), ≤ 8 (swoboda asymptotyczna). 3 z J₃(𝕆) (niełączność) ≠ 3 z R1b (tomografia lokalna) — różne źródła, nie utożsamiać.
  - **Jedno założenie:** odczyty wewnętrzne są oktonionowe. **Napięcie z ramą:** układy oktonionowe nie tworzą złożeń (brak iloczynu tensorowego → P5, P6 nie zachodzą; ¬P5 = „cecha”, 137). (a) rama wyklucza sektor oktonionowy → wyprowadzenie upada (zostaje Connes, 3 niewyprowadzone); (b) sektor oktonionowy = algebra **jednego punktu**, sama nieodczytywalna (≡ Ø, jak faza w punkcie, R1d), odczytywalne tylko jej relacje między punktami (pole cechowania). Rozstrzyga test wierności (157).
- **WYPROWADZENIE FUNKCJI ZESPOŁU (poprawka 155) [T][L][P][O].**
  - *(R1f, poprawka 162: „energia próżni” niżej = wyłącznie różnica ΔE(B) − E(0), relacja próżni z otoczeniem — polem B; energia Ø sama w sobie nie istnieje.)*
  - **A. Sprzężenia: b = −Σ(−1)^{2s}[(2s_z)² − ⅓]·T(R)** (Nielsen, Am. J. Phys. 49, 1171 (1981); Hughes, Phys. Lett. B 97, 246 (1980)). Naładowany nośnik w stałym polu B: poziomy Landaua (skwantowane obiegi w płaszczyźnie ⟂ B) + swobodne k_z wzdłuż B; E² = k_z² + eB(2n+1) − 2s_z·eB. Energia próżni: Σ½ω z gęstością eB/2π na poziom, znak (−1)^{2s}. Suma po dyskretnych obiegach minus całka (Euler–Maclaurin, suma po środkach, krok h = 2eB): **+h²/24·g′(0)**; przesunięcie spinowe a = 2s_z·eB: **−a²/2·g′(0)**; człon liniowy znosi się między ±s_z → razem −(e²B²/2)·g′(0)·**[(2s_z)² − ⅓]**. **Sprawdzenie [P]:** suma − całka wprost, eB = 0,02/0,01/0,005: na stan −0,33333 (s_z = 0), +0,66667 (±½), +3,66668 (±1) wobec −⅓, ⅔, 11/3 — zgodność 10⁻⁵, zbieżna z eB → 0. Dalej: g′(0) ∝ ∫dk_z/|k_z| = ln(Λ/μ); εμ = 1 zamienia przenikalność magnetyczną próżni na bieg ładunku; zliczenie stanów (pole zespolone ×2, wektor rzeczywisty tylko s_z = ±1) daje A2: −11/3·C_A (wektor), +⅔T (Weyl), +⅓T (skalar zespolony).

| składnik | w rachunku | w ramie | status |
|---|---|---|---|
| (−1)^{2s} | znak energii próżni fermionów | znak obrotu o 2π (R1e) | [T] |
| (2s_z)² | przesunięcie spinowe do kwadratu | relacja kierunku nośnika z kierunkiem pola (R1e) | [T] |
| **−⅓** | **suma po dyskretnych obiegach − całka** (h²/24, h = 2eB) | **„sztuki czy miara” [288–290]:** wkład orbitalny (ekranowanie) = różnica między liczeniem obiegów a miarą | [T] rachunek, [O] odczyt |
| ln(Λ/μ) | ∫dk_z/\|k_z\|: **dokładnie jeden** swobodny kierunek poza płaszczyzną obiegu | przy d wymiarach przestrzennych d − 2 kierunki → potęga Λ^{d−3}; **logarytm tylko przy d = 3 — „dynamika wymusza logarytm” [94] ⇔ d = 3 (R1b)** | [T] (wymiar sprzężenia M^{4−D}) |
| εμ = 1 | niezmienniczość Lorentza | c (R1c) | [T] |
| T(R), C_A, ładunki | teoria grup | N_c, anomalie (A2, [86]) | [L] |

  - **B. Masy: c = 3·[C(L) + C(R)].** Masa = zygzak L ↔ R (R1d); każda połówka niesie swoje relacje cechowania; wymiar anomalny zygzaka = suma wag obu połówek. Kwark ma trzeci czynnik (C₃ = 4/3 na połówkę, relacja relacji koloru), elektron nie. **Czynnik 3 [?]:** w cechowaniu Landaua z rzutnika poprzecznego, γ^μ P_μν γ^ν = D − 1 = 3; podział zależy od cechowania (niezmiennicza tylko suma), przy jednej pętli w regularyzacji wymiarowej „3 = D − 1” nieodróżnialne od innej postaci — odczyt, nie dowód.
  - **C. Człony Yukawy.** T = Tr(N_c·Y_u†Y_u + N_c·Y_d†Y_d + Y_e†Y_e): renormalizacja pola Higgsa = tło czytane przez wszystkie nośniki (waga N_c za kolor); wspólne → skraca się w stosunkach (153) [L]. 3/2(Y_u†Y_u − Y_d†Y_d): cytowane (Machacek–Vaughn 1984; Arason i in. 1992), niewyprowadzone; różnica znaku: u, d = dwie połówki dubletu SU(2), czytają tło z przeciwnym hiperładunkiem (u przez H̃, d przez H) [O].
  - **D. λ.** *(R1f: supertrace = różnica energii próżni względem wartości pola, nie energia Ø.)* 24λ² = 2(N + 8)λ², N = 4 rzeczywiste składowe dubletu [T]. Część niezależna od λ = supertrace: ⅜[2g₂⁴ + (g₂² + g′²)²] − 6y_t⁴ = (2/v⁴)[**6**·m_W⁴ + **3**·m_Z⁴ − **12**·m_t⁴] (sprawdzone algebraicznie [T]); wagi = liczby stanów: W± 2 × **3 polaryzacje**, Z **3** (masywny wektor: SO(3), kula 3D — Wigner, §F1), top 12 = 2 spin × 2 (cząstka/antycząstka) × N_c; bozony +, fermiony − = (−1)^{2s}. **Warunek 154 w nowym świetle:** β_λ = 0 przy λ = 0 ⇔ **Σ(−1)^{2s}·n_i·m_i⁴ = 0** na końcu Plancka — relacje tła z nośnikami zważone znakiem statystyki bilansują się; tło ≡ Ø nie niesie netto znaku statystyki [O]; y_t ≈ 0,39 z 154 = ten bilans.
  - **Wynik:** każdy współczynnik zespołu wywodzi się z elementów ramy — spin i znak 2π (R1e), dyskretność obiegów wobec miary (⅓), **d = 3** (logarytm, 3 polaryzacje, [?] 3 w γ_m), c (εμ = 1), ładunki z anomalii i N_c (A2). **Niewyprowadzone: grupa cechowania i liczba pokoleń** (wejścia listy 147; „Dalej otwarte”, 154). **Najmocniejsze zdanie:** −⅓ (ekranowanie) = różnica między liczeniem dyskretnych obiegów a miarą ciągłą — kryterium „sztuki czy miara” siedzi dosłownie we współczynniku, który rozstrzyga o swobodzie asymptotycznej.
- **ZASADA WIELU PUNKTÓW, POKOLENIA, LEPTONY (poprawka 154) [L][O][P]:**
  - *(R1f, poprawka 162: „energie próżni” w 148, 150, 154 mają sens wyłącznie jako różnice względem otoczenia; dla całości — brak.)*
  - **1. Test wierności dla zasady wielu punktów.** **Wersja ogólna (150: „dowolne dwie próżnie mają równą energię”) NIE PRZESZŁA — domysł asystenta wycofany:** ¬P (próżnie różnią się energią) jest odczytywalne wewnątrz struktury (grawitacja/krzywizna/Λ; ściana między obszarami) = różnica relacji otoczenia, którą wolno opisywać pośrednio [414]; ¬P nie wyklucza się z żadnym zdaniem ramy. **Wersja zawężona do końca Plancka PRZESZŁA, i tylko dla λ.** Kontrola „nie dowodzi za dużo”: znikanie wszystkich relacji przy Plancku byłoby fałszywe (α₁, α₂, α₃, y_t przy Plancku ≠ 0) — rama musi wybierać; wybiera λ:

| warunek | ¬P | wyklucza się z |
|---|---|---|
| **λ(koniec) = 0** | tło ≡ Ø ma niezerową relację z samym sobą na końcu, gdzie nic nie jest odróżnialne | λ = relacja **tła z tłem** (Higgs ≡ Ø, R1d) = Ø z Ø; relacja wymaga różnicy [242, 258], relacja z Ø jednostronna [122–124], Ø z Ø = nierozróżnialność, nie relacja. **g** (relacje faz między nośnikami) i **y** (jednostronna relacja nośnika z tłem) tego warunku nie dostają |
| **β_λ(koniec) = 0** | λ = 0 w samym punkcie końca, ≠ 0 tuż obok | przy Plancku punkt nieodróżnialny od sąsiedztwa [76]; (l_P t_P) ≡ Ø — warunek na koniec obowiązuje w całym nierozróżnialnym otoczeniu → znika wartość **i pochodna** |

    **Wynik [O]:** dokładnie dwa warunki Froggatta–Nielsena, w ramie bez multiwszechświata i bez punktu stałego AS (do kontroli strukturą). Przy λ = 0: β_λ = 0 ⇔ 6y_t⁴ = ⅜[2g₂⁴ + (g₂² + g′²)²] → przy Plancku **y_t ≈ 0,39** (bieg z pomiarów ≈ 0,38–0,40) [P, zgrubnie]. **Dwa odczyty ustalone strukturą: m_H, m_t.** Natura blisko, nie dokładnie: dokładna krytyczność przy m_t = 173,1 → m_H = 129,4 ± 1,8 GeV (Holthausen–Lim–Lindner, arXiv:1112.2415), zmierzone 125; przy m_H = 125 stabilność do Plancka wymaga m_t ≈ 171; zmierzone wartości na granicy stabilności (Buttazzo i in., JHEP 12 (2013) 089). **Pierwsze miejsce, gdzie odczyt ustalony strukturą zgadza się z naturą co do kilku σ** (głównie niepewność m_t), nie tylko co do rzędu.
  - **2. Pokolenia w ramie.** Filtr: „pokolenie nr 2” jako etykieta = cecha; „czym różnią się pokolenia same w sobie” — źle postawione. We wszystkich relacjach z nośnikami (cechowanie) pokolenia są ≡ (zespół: identyczne funkcje, 153); różnią się wyłącznie **jednostronną relacją z tłem ≡ Ø** (y_f, R1d) — tło działa, nośnik go nie odczyta → **hierarchii nie niesie struktura nośnika**, siedzi po stronie Ø, którą wolno opisywać tylko pośrednio [414]; stąd zespół jest na nią ślepy [O]. **CKM [O]:** stan masowy = relacja z tłem, stan słaby = relacja z W; CKM = niezgodność dwóch relacji = **relacja relacji**; faza nieusuwalna wymaga ≥ 3 kopii (R1d). **Co ustala 3 [L]:** anomalie — nie (znoszą się w każdym pokoleniu); swoboda asymptotyczna QCD — ≤ 8 pokoleń (n_f ≤ 16); szerokość Z — N_ν = 3 (pomiar); CP — ≥ 3 (Kobayashi–Maskawa). Wyprowadzenia 3 brak; symetrie zapachowe S₃/A₄ (permutacje trzech) ↔ triada — [?] zbieżność. **Werdykt:** rama przestawia pytanie z etykiety na „trzy odczyty jednostronnej relacji z Ø”; liczb nie daje.
  - **3. Leptony.** ~~Stosunki e : μ : τ nie biegną (153) = nie zależą od rozdzielczości odczytu; kwarkowe biegną przez y_t → **relacja bez skali może istnieć tylko dla leptonów** [O].~~ **CICHA ZMIANA ODCZYTU — błąd asystenta (poprawka 166):** „nie biegną” dotyczy stosunku Yukaw przy wspólnej rozdzielczości (odczyt B), a Koide niżej jest liczony z mas biegunowych (odczyt A) — dwie różne liczby; rozpisane w bloku 166 niżej. **Koide [L][P]:** Q = Σm/(Σ√m)² = ~~0,666661 z mas biegunowych (2/3 − 6·10⁻⁶); przewidywane m_τ = 1776,97 MeV wobec 1776,86 ± 0,12 (1σ)~~ **0,6666645 z mas biegunowych PDG 2024 (2/3 − 2,2·10⁻⁶, −0,43σ); przewidywane m_τ = 1776,969 MeV wobec 1776,93 ± 0,09** (166; skreślone wartości — dane PDG 2022). **W ramie [O]:** Q = 1/(3cos²θ), θ = kąt między (√m_e, √m_μ, √m_τ) a (1, 1, 1): **θ = ~~44,9997°~~ 44,9999°**. (1, 1, 1) = to, co pokoleń nie odróżnia (≡); część prostopadła = to, co różnicuje. **Q = 2/3 ⇔ część nierozróżniająca waży tyle co różnicująca.** Status: przepisanie obserwacji, bez wyprowadzenia; **ostrzeżenie numerologiczne** — wolno jako kontrolę dopiero po wyprowadzeniu z wejść z listy 147, **i tylko na odczycie A (166)**.
  - **STOSUNKI e : μ : τ — DWA ODCZYTY; CZY RAMA JE USTALA (poprawka 166) [L][P][T][O].** Temat (a) po 165; zdania przed rachunkiem; dane [L] ze źródeł.
    - **Dwa odczyty pod jedną nazwą.** **A** = masa w sensie R1f-3: faza na własne tyknięcie nośnika = **masa biegunowa** (każdy lepton czyta siebie). **B** = stosunek Yukaw — współczynników działania (R1f-1) — przy **wspólnej** rozdzielczości: „masy biegnące” z poziomu 2 i „siła jednostronnej relacji z tłem” z R1d (punkt otwarty 1). Bez pętli A = B; różni je relacja każdego nośnika z polem EM między jego własnym tyknięciem a wspólną rozdzielczością. Oba bez skali — ale to różne liczby (pułapka nazewnicza nr 6).
    - **Rachunek** `etap23_leptony_dwa_odczyty.py`. Dane: A — PDG 2024 (m_e = 0,51099895000(15), m_μ = 105,6583755(23), m_τ = 1776,93(9) MeV); B — Antusch, Hinze, Saad, arXiv:2510.01312v2, wzór (2.4) i tab. 2: Yukawy MS-bar na 9 skalach M_Z … 10¹⁶ GeV (dane PDG 2024; SMDR, dwupętlowe RGE).

| zdanie (przed rachunkiem) | wynik |
|---|---|
| **Z1** (153): stosunki B nie zależą od rozdzielczości (< 10⁻³ na całym zakresie); kontrola: pojedyncze Yukawy zmieniają się o > 1% | y_μ/y_e = 210,66, y_τ/y_e = 3578,4, y_τ/y_μ = 16,986; zmiana ≤ 1,1·10⁻⁴ na 14 dekadach (poziom zaokrągleń tabeli); każda Yukawa osobno: 6,5% — PRZESZŁO |
| **Z2**: A ≠ B (> 0,5% dla każdej pary), znak i kolejność τ/e > μ/e > τ/μ, wielkość do 20% jak w jednej pętli QED: B/A − 1 ≈ (3α/2π)·ln(m_i/m_j) | A: 206,768 / 3477,37 / 16,8177; B/A − 1 = 1,88% (μ/e), 2,91% (τ/e), 1,00% (τ/μ); wzór: 1,86 / 2,84 / 0,98% (stosunki 1,01–1,02) — PRZESZŁO |
| **Z3** (Koide wyłącznie jako kontrola rozróżniająca odczyty): \|Q_A − 2/3\| < 2σ, \|Q_B − 2/3\| > 10σ przy M_Z | Q_A = 2/3 − 2,2·10⁻⁶ (−0,43σ); Q_B = 2/3 + 1,16·10⁻³ **na każdej z 9 skal** (63σ przy M_Z; błędy bez korelacji — zawyżone); zgodne z Xing–Zhang (hep-ph/0602134: „około 0,2% przy M_Z”) — PRZESZŁO |

    **Wynik [P]:** **jedyna znana relacja między masami leptonów dotyczy odczytu A — masy w sensie ramy (R1f-3) — nie Yukaw.** [L] Koide przewidział w 1982 r. m_τ = 1776,97 MeV przy zmierzonych wtedy 1784,2 ± 3,2; w 1992 r. zmierzono 1776,99 ± 0,28 (za J. Baezem, *Azimuth*, 4.04.2021) — liczba, która mogła wyjść inaczej (A0); wzór nadal niewyprowadzony. **Dopisek po rachunku (raport, bez zdania):** kąt δ w parametryzacji √m_n/μ − 1 = √2·cos(δ + 2πn/3) (μ = średnia √m): **δ_A = 2/9 + 2,5·10⁻⁶ (0,41σ)**, δ_B = 2/9 − 1,1·10⁻³ [L] (Żenczykowski, PRD 86, 117303 (2012): δ_L „nieodróżnialne od 2/9”). **Dwa empiryczne warunki (Q = 2/3, δ = 2/9) odtwarzają oba stosunki do obecnej precyzji; żaden niewyprowadzony; oba zachodzą tylko na A.**
    - **Czy rama ustala e : μ : τ — zdanie po zdaniu [T][O]:**

| zdanie ramy | co daje dla e : μ : τ |
|---|---|
| pokolenia ≡ we wszystkich relacjach z nośnikami (153; pkt 2 wyżej) | nic — zespół ślepy na pokolenia |
| „relacja z tłem nie odróżnia kopii” | ≡ pełne (każda baza kopii równoważna, jak w cechowaniu: Y ↦ U_L·Y·U_e†, U(3)_L × U(3)_e) ⇒ **Y = 0, brak mas** [T]; ≡ z zachowaną parą L_i–e_i (wspólne U(3)) ⇒ Y ∝ 𝟙, masy równe, Q = 1/3 — ale parę L–e ustala właśnie relacja z tłem; ≡ tylko permutacyjne, lewe i prawe niezależnie (S₃L × S₃R; Harari, Haut, Weyers, PLB 78, 459 (1978)) ⇒ Y ∝ macierz jedynek, masy **(0, 0, 3k)**, Q = 1 — wymaga wyróżnionej bazy kopii = etykiet (pkt 2: etykieta = cecha). Natura przeczy wszystkim trzem → **e, μ, τ są odróżnialne wyłącznie przez samą relację z tłem** [O] (zgodne z pkt 2); wartości to nie ustala |
| masa = faza na własne tyknięcie (R1f-3) | ustala, **który** odczyt jest masą (A), nie jego wartość |
| koniec Plancka (pkt 1 wyżej) | warunek tylko dla λ (tło z tłem); y go nie dostaje |
| całość, Ĥ\|Ψ⟩ = 0 (150) | stałe nieustalone |
| lista 147 | przed rachunkiem nie zapisano żadnej kombinacji wejść; szukanie jej po fakcie = numerologia [376–378] |
| Froggatt–Nielsen (150, „Następne”) | ε i ładunki dopasowane; ε policzalne tylko ze strunami, anomalnym U(1) i mechanizmem Greena–Schwarza (Ramond, hep-ph/9808488) — nowe byty („Cel”) |

    **Werdykt (stanowczo): 0 warunków ramy na 2 stosunki — rama nie ustala e : μ : τ.** Nie „wyskoczą po drodze” [88]: zespół ich nie zawiera, a same nie zależą od rozdzielczości, więc żadna funkcja zespołu ich nie ustala. **„Sito” nie rozstrzyga:** pokazano, że stosunki są niewyprowadzone, nie — że niesprowadzalne.
    - **Co zostaje [O]:** (1) **pułapka nazewnicza nr 6** („masa” = A albo B). (2) **Kontrola zaostrzona:** relacja między leptonami wyprowadzona kiedykolwiek musi dotyczyć samoodczytów (A); ta sama relacja dla B jest wykluczona (63σ). (3) **Pytanie Sumino** (arXiv:0812.2090, 0812.2103: poprawka QED psuje relację Koidego dla mas biegunowych → nowe bozony rodzinowe U(3), które ją znoszą) **— źle postawione po filtrze:** zakłada wyróżnioną wysoką rozdzielczość, przy której relacje obowiązują, a masy biegunowe z nich wynikają (wyróżniona skala i kierunek „od wysokiej do niskiej”; §F1, „RG po filtrze”). W ramie żadna rozdzielczość nie jest wyróżniona, masa = A → zarzut odpada; **wyprowadzenia to nie daje.** (4) **„Relacja bez skali tylko dla leptonów” — z dwóch różnych powodów:** na B, bo stosunki kwarkowe biegną przez y_t (153); na A, bo tylko leptony mają odczyt na własnym tyknięciu (kwark tylko jako m_b(m_b), „stosunek odniesiony do stosunku”, 151).
    - **Pułapki numerologiczne (zapisane, żeby ich nie łączyć):** (a) **δ = 2/9 ≠ R\* = 2/9** z Pendletona–Rossa (165): kąt parametryzacji pierwiastków mas leptonów wobec stosunku y_t²/g₃² z b₃ — różne obiekty, żadnego wspólnego wejścia; (b) „2/3 = środek między Q = 1/3 (masy ≡) a Q = 1 (S₃L × S₃R)” — środek tylko w zmiennej Q; w kącie θ środek wypada przy 27°; (c) „45° = stożek światła jak w R1c” — dla trzech kopii warunek światła z R1c (część śladowa = bezśladowa ⇔ det = 0) uogólnia się na dwa sposoby: rząd 1 (Q = 1) albo równe normy obu części (Q = 2/3); wybór pasującego po fakcie = Eddington.
- > **Uwaga (poprawka 151):** 148–150 szukały warunków ustalających **wartości** — skutek błędu z [105] (jedna relacja zamiast zespołu). Liczenie w 149–150 doszło okrężną drogą do [94]. **Zostaje:** typy S/K (146), ⅓ (145), „Ĥ|Ψ⟩ = 0 nie ustala stałych” (150, zgodne z [88]: stała = wartość funkcji w jednym stanie = odczyt), forma „stała = relacja lokalnego z całością” (150). Wątek wartości brzegowych — poboczny.
- **WARUNEK NA KOŃCU PLANCKA — literatura i filtr (poprawka 148) [L][O][T]:**
  - **Trzy precedensy [L]:** (1) **punkt stały = dokładne samopodobieństwo na końcu:** Shaposhnikov–Wetterich, Phys. Lett. B 683, 196 (2010), arXiv:0912.0208 — λ przy skali Plancka w punkcie stałym w zerze → m_H ≈ 126 GeV (kilka GeV), przed odkryciem; założenie: brak skal pośrednich między Fermim a Planckiem = **pustynia [545]**. Eichhorn–Held–Wetterich, Phys. Lett. B 782, 198 (2018), arXiv:1711.02949 — to samo dla sprzężenia cechowania, α obliczalne, zależne od zawartości materii GUT i od niepewnej siły wkładu grawitacji. (2) **nierozróżnialność próżni (zasada wielu punktów):** Froggatt–Nielsen, Phys. Lett. B 368, 96 (1996), hep-ph/9511371 — dwie próżnie (elektrosłaba i planckowska) o równej energii → m_t = 173 ± 5, m_H = 135 ± 9 GeV. (3) **obserwacja:** zmierzone m_H ≈ 125, m_t ≈ 173 stawiają MS tuż przy granicy stabilności; przy skali Plancka λ i β_λ bliskie zera (Buttazzo i in., JHEP 12 (2013) 089).
  - **Wejścia:** wszystkie trzy biorą zmierzone sprzężenia cechowania (dwie także m_t) — **żadna nie mieści się na liście 147**; każda ustala jedną–dwie wielkości przy danych pozostałych. „Wszystko naraz” w literaturze nie istnieje.
  - **Po filtrze (forma warunku, bez mechanizmu) [O]:** (1) na końcu Plancka bezwymiarowe relacje nie zależą od rozdzielczości odczytu = dokładne samopodobieństwo ≡ Ø — zgodne z §F1 bez dokładania. Nie bierzemy: metryki jako fluktuującego pola (przestrzeń jako pojemnik) ani „punktu stałego osiąganego przy obniżaniu skali” (przepływ = kierunek). (2) próżnia ≡ Ø [242–258], więc dwie próżnie o równej energii = łańcuch Ø zastosowany do próżni. **Pułapka nazewnicza:** „płaski potencjał” (λ ≈ 0) ≠ płaskość 2D; przenosi się tylko ≡ (próżnia nie rozróżnia wartości pola).
  - **Dlaczego oba końce [T] (RG) / [O]:** warunek punktu stałego na jednym końcu ustala tylko sprzężenia **nierelewantne** w tym punkcie (u S–W λ — dlatego przewidziane); kierunki **relewantne i marginalne** zostają wolne, po jednej liczbie na kierunek (sprzężenie cechowania dążące do zera zostawia wolną skalę — transmutacja, R1d). **Sam koniec Plancka nie wystarcza; wolne dane musi ustalić drugi koniec (całość ≡ Ø).** „Oba końce” to wymóg liczenia danych, nie styl. Na drugim końcu literatura ma jedną relację: Λ ~ N^{−1/2} (Sorkin, ½ z Poissona).
  - **Zdanie do upadku (przed rachunkiem):** liczba kierunków relewantnych i marginalnych punktu stałego na końcu Plancka ≤ liczba warunków z końca całości. Upada, gdy wolnych danych jest więcej, niż drugi koniec może ustalić.
- **ZLICZENIE KIERUNKÓW — ZDANIE Z 148 UPADŁO w tej postaci (poprawka 149) [L][P]:** punkt stały przy Plancku wg asymptotic safety (wyniki warunkowe: zależne od przybliżenia, dla szerokiego, nie dowolnego zakresu sprzężeń grawitacji; wariant najbardziej przewidujący, Eichhorn–Held, arXiv:1707.01107, PRL 121, 151302 (2018)):

| sektor | w punkcie stałym | wolne dane |
|---|---|---|
| grawitacja | ≤ 3 kierunki relewantne (G, Λ, trzeci; przybliżenia f(R), arXiv:1805.09656) | 2–3 (G ustala jednostkę) |
| Higgs μ² | relewantne (= hierarchia v/m_P) | 1 |
| Higgs λ | nierelewantne → przewidziane (Shaposhnikov–Wetterich) | 0 |
| cechowanie U(1), SU(2), SU(3) | swoboda asymptotyczna = marginalnie relewantne; U(1) w innym wariancie przewidziane (JHEP 01 (2018) 030) | 2–3 |
| Yukawa top | punkt stały oddziałujący → przewidziane; także m_t − m_b ≈ 170 GeV | 0 |
| pozostałe Yukawy, CKM, θ_QCD | swoboda asymptotyczna → wolne | ~12 |

  - **Liczenie:** koniec Plancka zostawia **~15–19 wolnych danych**; koniec całości w literaturze daje **1 warunek** (Λ ~ N^{−1/2}). **15–19 > 1 → upadło** zestawienie „punkt stały AS przy Plancku + jedna relacja z całości”.
  - **Nie upadła hipoteza §F1** — liczenie mówi, czego od niej trzeba: koniec Plancka musi w ramie ustalać więcej niż punkt stały **albo** koniec całości musi dawać więcej niż jeden warunek. Trzeciej drogi nie ma.
    - **(a) Koniec Plancka:** punkt stały = samopodobieństwo = połowa „≡ Ø”; druga połowa = **nierozróżnialność próżni** (Froggatt–Nielsen) — każda równość energii próżni to dodatkowe równanie, niezależne od punktu stałego (precedens: m_t trafione).
    - **(b) Koniec całości:** literatura ma tylko Λ. W ramie całość bez otoczenia → Ĥ|Ψ⟩ = 0 — więz w każdym punkcie, nie jedna liczba. **Ile warunków na bezwymiarowe relacje z tego wychodzi — niesprawdzone przez nikogo.**
  - **Nowe zdanie do upadku:** suma niezależnych równań z obu końców ≥ liczba wolnych danych (~15–19). Kolejność: najpierw (b) (tego w literaturze nie ma, rama ma tu własne zdanie), potem (a).
- **(b) CAŁOŚĆ BEZ OTOCZENIA — WERDYKT, FORMA WIELOLOKALNA, ZAPACHY (poprawka 150) [L][O]:**
  - **(b) w postaci z 149 UPADŁO (≤ 1 warunek).** Henneaux–Teitelboim, Phys. Lett. B 222, 195 (1989): w grawitacji unimodularnej Λ = **stała całkowania**, jedyny globalny stopień swobody, sprzężony z czterowymiarową objętością („czas kosmiczny”); funkcja falowa spełnia równanie Wheelera–DeWitta, a Λ pozostaje dowolne. Magueijo (arXiv:2104.11529): to samo dla każdej stałej — każda sprzężona z własnym czasem relacyjnym, więz → równanie Schrödingera ze stałymi jako „energiami”. Sekwestracja (Kaloper–Padilla, PRL 112, 091304 (2014)): Λ = średnia po całej historii — 1 warunek, bezwymiarowych sprzężeń nie dotyka. **Więz nie ustala wartości stałych, czyni je wielkościami zachowanymi, sprzężonymi z globalną liczebnością (N).** Warunków na wartości: 0; zostaje rozdzielczość ~N^{−1/2} → 1 warunek dla Λ (wartość na granicy rozdzielczości, Sorkin).
  - **W ramie [O]:** stała nieustalona = superpozycja wartości ≡ Ø [110]; wartość stałej istnieje tylko w odczycie, z rozdzielczością 1/√N. Zgodne z ramą, ale wartości nie daje.
  - **Jedyna forma z jednym warunkiem na stałą [L]:** działanie wielolokalne — stała = funkcjonał całek po całej czasoprzestrzeni, dominuje jedna wartość (Coleman 1988; Kawai–Okada, Prog. Theor. Phys. 127, 689 (2012), arXiv:1110.2303; Hamada–Kawai–Kawana, arXiv:1509.05955: Λ ≈ 0, θ_QCD ≈ 0, zasada wielu punktów). Bennett–Nielsen (hep-ph/9607341): zasada wielu punktów z **nielokalności** → sprzężenia cechowania, α⁻¹ = 136,8 ± 9 (wejścia: 3 pokolenia — na liście; wybór grupy AGUT — nie). **W literaturze (a) i (b) to jedna forma.**
  - **Po filtrze:** odrzucone multiwszechświat, tunele, „superpozycja wszechświatów” (sprzeczne z [110]; Ro niedostępne) i euklidesowa całka (Hebecker–Mikhail–Soler, arXiv:1807.00824; w wersji lorentzowskiej małe Λ niezagwarantowane — Kawana, arXiv:1405.2743). **Zostaje forma: stała = relacja członu lokalnego z całością** — ta sama co R1d (masa = jednostronna relacja z nierozróżnialnym tłem) [O]; zbiór przyczynowy jest nielokalny sam z siebie (Dalej otwarte) → forma wielolokalna prawdopodobnie nie jest dodatkiem [?].
  - **Zasada wielu punktów w ramie, bez multiwszechświata [?] (domysł asystenta):** każda próżnia ≡ Ø, Ø absolutne, różni je tylko relacja otoczenia [412–414]; całość nie ma otoczenia → różnica energii dwóch próżni względem całości = różnica, której nic nie odczytuje = **cecha** (jak ¬P5, poprawka 137) → równe energie. **Do testu wierności (poprawka 128); słaby punkt:** różnice energii próżni są odczytywalne lokalnie (ściany domen, grawitacja).
  - **Liczenie po (a) + (b):** całość ≤ 1 (Λ); zasada wielu punktów — Higgs 2 (m_t, m_H; Froggatt–Nielsen), cechowanie 3 (Bennett–Nielsen, z AGUT, ±7%) → **~6 wobec ~15–19. Brakuje ~10, wszystkie z sektora zapachów** (lżejsze Yukawy, CKM) = „kwarki i elektrony nie pozwolą na jedną funkcję” [94], y_e otwarte. Precedens: mechanizm Froggatta–Nielsena (1979), y ~ ε^n — ln y = (całkowita)·ln ε; ale ε ≈ 0,2 dopasowane, ładunki wybrane ręcznie → **nie na liście 147**.
  - **[H] (użytkownik, 25.09):** „**Dlatego szukamy zespołu funkcji.**” — brakujące równania to dokładnie miejsce [94]: jedna funkcja (jeden warunek na końcach) nie wystarcza, bo sektor zapachów wymaga zespołu.
  - **Następne:** test wierności dla zasady wielu punktów w ramie; potem literatura zapachów: czy w ε^n cokolwiek da się policzyć (ε, wykładniki), czy wszystko jest dopasowane. **Zamknięte:** test wierności — 154 pkt 1 (tylko λ na końcu Plancka); literatura zapachów — 166: ε i ładunki dopasowane, ε policzalne tylko z nowymi bytami (struny, anomalne U(1), Green–Schwarz); stosunki leptonów — rama nie daje warunku.
- **Domysł [?]:** definicja masy może powstać razem z warunkiem stabilności węzła (obiekt = stabilna struktura relacji, słownik).

**Hipoteza (v3.4):** masa = **częstość, z jaką trajektoria czyta samą siebie**. Zdanie o odczycie, nie o geometrii — **nie wymaga rozstrzygnięcia sprawy przestrzeni**, więc można je testować teraz, na strukturze z zadania A (sprinkling + trajektorie + odczyty).
- **Co już pasuje:** foton nie czyta siebie (t=0) → brak masy; przy v→c częstość samoodczytu mierzona z zewnątrz spada, od środka bez zmian (dylatacja); masa i prędkość siedzą w tym samym wierszu tabeli granic Ø.
**DEFINICJA ROBOCZA I PIERWSZY WYNIK (v3.4, `etap6_masa.py`).** Skąd kandydat: w pliku jest już pytanie „czy relacja wraca do siebie” (nie wraca → U(1), foton; wraca → SU(3)). Masa jako częstość samoodczytu to **to samo pytanie zadane o trajektorię**: jak często informacja wysłana przez trajektorię do niej wraca. Foton: nic nie wraca, od jego strony nie ma „potem”.
**Definicja (wewnętrzna, mierzalna):** dla trajektorii i — liczba **powrotów na odczyt**: ile razy element i czyta trajektorię j, która **wcześniej** czytała i (najkrótsza zamknięta pętla odczytu). Struktura: sprinkling + trajektorie + odczyty jak w zadaniu A (N=1,5 mln, K=1200, L=12).
**Zdania przed rachunkiem:** (1) częstość stabilna wzdłuż trajektorii (połowa–połowa); (2) różni się między trajektoriami bardziej niż przypadkiem; (3) kontrola losowa niszczy obie własności.

| | częstość powrotów | rozrzut między trajektoriami | korelacja połowa–połowa |
|---|---|---|---|
| odczyt najświeższych | 0,287 ± 0,008 | 0,280 | **+0,750** |
| odczyt losowy (kontrola) | 0,033 ± 0,001 | 0,040 | −0,180 |

- **WSZYSTKIE TRZY ZDANIA PRZESZŁY.** **Pierwszy raz w v3.4 pojedyncza trajektoria ma własną, zachowaną cechę liczbową.**
- **Wykluczone najprostsze wyjaśnienie:** korelacja częstości z lokalną gęstością sąsiadów **−0,044**, z liczbą różnych czytanych trajektorii **−0,267**; po usunięciu wpływu obu korelacja połowa–połowa pozostaje **+0,746**. **To nie jest gęstość ani liczba partnerów.**
- **Zastrzeżenia:** jedno ziarno, K=1200, L=12; pętle tylko długości 2; brak związku z jakąkolwiek skalą fizyczną (to na razie liczba bez jednostek); nie sprawdzono, czy zachowuje się jak masa (dodawanie, dylatacja, zależność od prędkości względem tła).
**TEST PRĘDKOŚCIOWY — KANDYDAT ODPADA (v3.4).** Zdania przed rachunkiem: (a) **od środka** (na własny krok) częstość nie zależy od prędkości; (b) **z zewnątrz** (na czas współrzędnościowy) maleje jak √(1−v²); (c) kontrola losowa nie pokazuje żadnej z tych zależności.
- **Pierwszy przebieg (prędkości 0,01–0,30):** na krok 0,404 wobec 0,404 (korelacja −0,020) — (a) pozornie przeszło; na czas: stosunek 0,980 wobec przewidywania 0,986 — zgodne, ale efekt 2%, nierozstrzygnięty.
- **Odkryty błąd konstrukcji:** reguła budowy trajektorii („największy czas własny w oknie”) **nie jest niezmiennicza** — daje trajektorie prawie spoczywające w układzie pudła. Zerowy wynik (a) był pozorny.
- **Drugi przebieg (prędkości 0,02–0,79, trajektorie o zadanej prędkości):**

| | wolne | szybkie | korelacja z v |
|---|---|---|---|
| na własny krok | 0,307 | 0,176 | **−0,236** |
| na czas współrzędnościowy | 0,947 | 0,568 | stosunek 0,599 wobec 0,822 z dylatacji |

- **ZDANIE (a) UPADŁO:** częstość na własny krok zależy od prędkości. **Przyczyna:** powrót wymaga drogi tam i z powrotem, więc trajektoria szybka **ucieka własnym odbiciom** — ci, którzy ją czytali, zostają z tyłu. Mierzona wielkość zależy od ruchu **względem zespołu**, a zespół wyznacza układ spoczynku (działa jak ośrodek).
- **Wniosek:** „częstość powrotów” to **tempo oddziaływania z otoczeniem**, wielkość zależna od układu — **nie masa**. Zachowanie wzdłuż trajektorii (korelacja 0,75) zostaje jako fakt, ale opisuje relację z otoczeniem, nie cechę własną.
**KANDYDAT 2 — częstość zegara własnego (v3.4).** Poprawka do wcześniejszego zapisu: „własny element bez pośredników” to **link**, a łańcuch fotonowy składa się z samych linków — taka wielkość byłaby dla fotonu **maksymalna**, nie zerowa. Poprawnie, z fizyki bez interpretacji: masa = **częstość zegara własnego** (Compton, ω = mc²/ħ); foton nie ma masy, bo między emisją a absorpcją **nie ma zdarzenia pośredniego**. **Definicja:** liczba własnych elementów na jednostkę czasu własnego (obie wielkości niezmiennicze).
- **Wynik (400 trajektorii, prędkości 0,02–0,78):** korelacja z prędkością **+0,333**; wolne 2,74, szybkie 3,82 (stosunek **1,39**); stabilność połowa–połowa +0,473. **(a) UPADŁO.**
- **Przyczyna (błąd konstrukcji):** trajektoria o zadanej prędkości wybiera element najbliższy celowi w oknie **czasu współrzędnościowego**, więc przy dużej prędkości trafia bliżej stożka, gdzie czas własny kroku jest mały. Wielkość mierzy **sposób prowadzenia trajektorii**, nie jej własność.
- **WNIOSEK POJĘCIOWY [A]:** w obu kandydatach wielkość zależała od tego, **jak trajektoria siebie kontynuuje**. **Masa nie jest cechą odczytywaną z gotowej linii świata, lecz własnością reguły, wedle której trajektoria siebie przedłuża.** Trajektoria „leniwa” (kroki o maksymalnym czasie własnym) tyka rzadko; drobiąca kroki tyka często.

**KANDYDAT 3 — drobność samokontynuacji (v3.4).** Stosunek liczby własnych kroków do **maksymalnej możliwej** na tej samej drodze (najdłuższy łańcuch między końcami). Obie liczby czysto porządkowe → niezmienniczy z konstrukcji. Foton: między końcami linku nie ma elementów, wielkość znika.
- **Wynik (118 trajektorii, prędkości 0,05–0,81):** średnia 0,494; korelacja z prędkością **+0,197** (błąd ~0,09, czyli ~2σ); szybkie/wolne **1,16** (wobec 1,39 dla kandydata 2). **Zależność spadła o połowę, ale NIEROZSTRZYGNIĘTE.**
**KANDYDAT 3 = KANDYDAT 2 W INNEJ NORMALIZACJI [A]:** w sprinklingu najdłuższy łańcuch ∝ czas własny × ρ^(1/4), więc „kroki/najdłuższy łańcuch” to „kroki na czas własny” podzielone przez stałą. Różnica 1,39 vs 1,16 pochodzi z fluktuacji. **Zwiększanie próby tego nie naprawi — naprawić trzeba konstrukcję.**

**TRZY PUŁAPKI KONSTRUKCJI TRAJEKTORII (v3.4, `etap7_masa_gpu.py`) — najcenniejszy wynik tej rundy:**
1. **Reguła zewnętrzna** (okno w czasie współrzędnościowym + kierunek zadany w układzie pudła): tempo tyknięć zależy od prędkości (korelacja +0,32; szybkie/wolne 1,46–1,61). Wielkość mierzy regułę, nie strukturę.
2. **„Maksymalny czas własny do przodu” HAMUJE:** τ² = Δt²−Δx², więc maksymalizacja preferuje małe przesunięcie przestrzenne → wszystkie trajektorie wytracają prędkość (0,01–0,13) i opadają do układu próbkowania. **Geodezyjna maksymalizuje czas własny między ustalonymi końcami, nie krok po kroku.**
3. **Równe tyknięcia dziedziczą warunek początkowy:** przy wymuszeniu τ_kroku ≈ τ_poprzedniego stabilność rośnie do **+0,930**, ale korelacja z prędkością skacze do +0,63 — bo pierwszy krok budowany regułą zewnętrzną dawał szybkim trajektoriom krok bliski stożkowi (małe τ). **To zachowanie jest jednak MASO-PODOBNE: tempo tyknięć jest warunkiem początkowym niesionym przez trajektorię, a nie narzuconym przez otoczenie.**
- **Poprawiona konstrukcja:** jednakowe **tyknięcie początkowe** dla wszystkich (wąskie pasmo τ), różne kierunki i prędkości; dalej kontynuacja wewnętrzna (równe tyknięcia + najprostsza kontynuacja od przedostatniego).
- **Walidacja (800 trajektorii, N=0,8 mln, L=8):** reguła wewnętrzna — korelacja **+0,166**, szybkie/wolne **1,096**, stabilność +0,667; kontrola zewnętrzna — +0,241 i **1,46**. **Kierunek dobry, nierozstrzygnięte:** zakres prędkości tylko 0,01–0,25 (przy ustalonym τ szybkie trajektorie potrzebują większego okna — parametr do poszerzenia).
**PRZEBIEG DUŻY I CZWARTA PUŁAPKA — ZNAK (v3.4).** Przebieg użytkownika (N=19 mln, K=20 tys., L=20, 2 ziarna) dał: reguła wewnętrzna korelacja +0,065/+0,049, stosunek **1,010/1,008**, stabilność +0,725/+0,727, ale **prędkości tylko 0,00–0,15**; kontrola +0,298/+0,310, stosunek 1,524/1,543, prędkości do 0,81. **Niezmienniczość pokazana tam, gdzie i tak nie ma czego pokazywać** (przy v≤0,15 dylatacja to promil).
- **Czwarta pułapka — ZNAK (odwrotna nierówność trójkąta):** dla p≺q≺c zachodzi τ(p,c) ≥ τ(p,q)+τ(q,c), **równość tylko gdy q leży na prostej**. **Linia prosta daje NAJMNIEJSZY** τ(p,c) przy ustalonych krokach — więc najprostsza kontynuacja to **minimum**, nie maksimum. Maksymalizacja wybierała kontynuację **najbardziej zakrzywioną** → resztkowe hamowanie.
- **Po poprawce znaku (v4, walidacja 800 trajektorii):**

| | korelacja z v | szybkie/wolne | stabilność | zakres prędkości |
|---|---|---|---|---|
| **reguła wewnętrzna** | **+0,051** | **1,015** | +0,630 | **0,07–0,91** |
| kontrola zewnętrzna | +0,335 | 1,612 | +0,475 | 0,02–0,82 |

- **WSZYSTKIE ZDANIA PRZECHODZĄ:** M0 (nie hamuje: prędkości do 0,91, γ do 2,4), M1 (tempo nie zależy od prędkości: 1,015), M2 (stabilne: +0,630), M3 (kontrola pokazuje, że różnica bierze się z reguły: 1,612).
- **Status kandydata 2 przy niezmienniczej kontynuacji:** tempo tyknięć na czas własny jest **niesione przez trajektorię i niezależne od ruchu** — zachowanie maso-podobne. Do rozstrzygnięcia w pełnym przebiegu: statystyka i stabilność przy L=20.
**PEŁNY PRZEBIEG v4 (użytkownik, N=19 mln, K=20 tys., L=20, 2 ziarna) — WSZYSTKIE ZDANIA PRZESZŁY:**

| | korelacja z v | szybkie/wolne | stabilność | prędkości |
|---|---|---|---|---|
| **reguła wewnętrzna** | **+0,034 / +0,027** | **1,005 / 1,005** | **+0,770 / +0,771** | 0,02–0,90 |
| kontrola zewnętrzna | +0,298 / +0,310 | 1,524 / 1,543 | +0,638 / +0,645 | 0,00–0,81 |

- **M0 ✓** (prędkości do 0,90, γ do 2,3); **M1 ✓** (|korelacja| 0,03 < 0,05; stosunek 1,005 w paśmie ±0,05 — uczciwie: przy n=20 tys. korelacja 0,03 jest statystycznie odróżnialna od zera, ale efekt to 0,5% na całym zakresie, ~100× mniej niż w kontroli); **M2 ✓** (stabilność wzrosła 0,63 → **0,77** przy dłuższych trajektoriach); **M3 ✓** (kontrola 1,52–1,54).
- **WYNIK [A]:** trajektoria kontynuująca się pamięcią (najprostsza droga w sensie czasu własnego = minimum τ(p,c)) niesie **tempo tyknięć niezależne od ruchu i zachowane przez całe życie**. **Zachowanie masy spoczynkowej, wyprowadzone z samego porządku, bez układu odniesienia.**
- **Czego jeszcze NIE pokazuje:** wszystkie trajektorie startowały z **tym samym** tyknięciem → sprawdzono „ta sama masa, różne prędkości”. **Następne zdanie:** dwie populacje o różnym tyknięciu początkowym (np. 0,4h i 0,6h) mają tempo w stosunku 1,5 i **obie** pozostają niezależne od prędkości.
**DWIE POPULACJE — ROZRÓŻNIALNE MASY (v3.4, `etap8_masa_populacje.py`).** Tyknięcie początkowe A = 0,4h, B = 0,6h. **Uczciwy test:** pasmo tyknięcia liczone względem **poprzedniego kroku**, więc tempo przenoszone wyłącznie pamięcią (przy paśmie względem początkowego stosunek 1,5 byłby wymuszony). Zdania: P1 A/B = 1,5 ± 0,1; P2 w każdej populacji szybkie/wolne 1,00 ± 0,05; P3 dryf < 10%; P4 nakładanie rozkładów < 10%.
- **PIĄTA PUŁAPKA — miara prostoty:** samo minimum τ(p,c) preferuje **mniejsze kroki** (mniejszy krok też zmniejsza τ(p,c)) → dryf tempa +22% w B, stosunek 1,38. **Poprawnie: nadwyżka z odwrotnej nierówności trójkąta** τ(p,c) − τ(p,q) − τ(q,c) ≥ 0 — zero dokładnie dla prostej i **niezależna od długości kroku**. Po poprawce (walidacja): A/B = 1,503, dryf 0,973.
- **PEŁNY PRZEBIEG (użytkownik, N=19 mln, K=20 tys. na populację, L=20, 2 ziarna):**

| | tempo | szybkie/wolne | korelacja z v | stabilność | dryf |
|---|---|---|---|---|---|
| A (0,4h) | 6,78 ± 1,07 | **0,988 / 0,988** | −0,03 | 0,75 | 0,95 |
| B (0,6h) | 4,50 ± 0,67 | **1,055 / 1,052** | +0,13 | 0,74 | 0,94 |

  - **P1 — PRZESZŁO:** A/B = **1,508 / 1,507** (oczekiwane 1,50). **Niewymuszone** — tempo przeniesione przez 20 kroków wyłącznie pamięcią. **Najmocniejsze zdanie gałęzi masy.**
  - **P3 — PRZESZŁO:** dryf 5–6%.
  - **P2 — przeszło dla A, minimalnie upadło dla B:** 1,052–1,055 (poza pasmem o kilka tysięcznych); korelacja +0,13 → **w populacji o dłuższym tyknięciu słaba resztkowa zależność od prędkości**; w A jej brak.
  - **P4 — NIEROZSTRZYGNIĘTE:** skrypt sprawdzał rozłączność przedziałów 5–95% (ostrzejsze niż zdanie) — zachodzą w pasie 5,16–5,68, bo rozrzut w każdej populacji ~15%; **zapisanego progu „nakładanie < 10%” nie policzono** (błąd asystenta: kryterium w kodzie ≠ zdanie).
**MOST DO LOGARYTMÓW PRZEZ SZEROKOŚĆ — SPRAWDZONY I ZAMKNIĘTY (v3.4, `etap9_masa_skala.py`).** Uwaga użytkownika: jedna gęstość daje punkt, nie funkcję; logarytmy z C4a pochodziły ze stosunku skal; trzeba skanu ≥ dekady i sprawdzenia, czy szerokość idzie jak 1/ln n (most), 1/√n (Poisson, mostu brak) czy stoi.
- **Poprawka asystenta do projektu:** skan N przy stałym `KAND` to **tautologia** — sprinkling Poissona jest niezmienniczy względem skali, każdy krok widzi to samo. Właściwy stosunek skal: **liczba elementów na tyknięcie** n = ρ(π/24)τ₀⁴; skanowane tyknięcie przy stałej gęstości (równoważne). Rozstrzygnięcie ln vs stała wymaga ≥ 2 dekad.
- **Walidacja (K=150):** n = 0,09 / 1,5 / 13,6 (dwie dekady) → szerokość A **0,099 / 0,095 / 0,103**, B 0,101 / 0,106 — **stała**, ani Poisson, ani logarytm.
- **Test kontrolny pasma — SZEROKOŚĆ = PASMO TOLERANCJI:**

| pasmo | szerokość A | szerokość B | dryf |
|---|---|---|---|
| ±5% | 0,044 | 0,048 | 0,99 |
| ±10% | 0,095 | 0,106 | 0,98 |
| ±20% | 0,191 | 0,195 | 0,92 |

  **„Naturalna szerokość” to parametr konstrukcji** (liniowa w paśmie, niezależna od gęstości). **Przebiegu na A100 NIE wysyłać** — policzyłby pasmo.
- **Co zostaje nieartefaktem [H]:** pasmo nie może być dowolnie wąskie — musi zawierać choć jednego kandydata, więc minimalne pasmo ∝ 1/n. Przy pasmie ustawianym najwęższym możliwym szerokość stałaby się wielkością strukturalną, **spodziewanie potęgową w n** → w sformułowaniu użytkownika: **szum, mostu tędy nie ma.**
- **Stosunek A/B odporny:** 1,49–1,51 przy każdym paśmie i każdej gęstości — mocna część gałęzi masy nietknięta.
- **Most masa ↔ logarytmy przez szerokość: ZAMKNIĘTY (brak).** Jeśli most istnieje, musi iść inną drogą (§F2: wyprowadzenie współczynników 1, ½, 0,57 z liczby kierunków wskazywania).

- **Stan:** dwie masy różniące się o połowę są **rozróżnialne w średniej z dokładnością ~0,5%**, niesione pamięcią i niezależne od ruchu; **pojedyncza trajektoria ma rozrzut ~15%**, więc na ogonach populacje się mieszają.

> **HISTORIA — plan krokowy sprzed poprawki 136; nie realizować jako następnego kroku (poprawka 142).** Wyniki etap6–9 wyżej bez zmian (status z poprawki 103).

- **Do przebiegu na Colab:** `etap7_masa_gpu.py` (N=12 mln, K=20 tys., L=20, 2 ziarna) ze zdaniami M0a, M0, M1, M2, M3 w nagłówku.

- **Wąskie gardło (kandydat 3):** najdłuższy łańcuch liczy się kwadratowo z liczbą elementów przedziału — duża próba wymaga innego algorytmu (np. przybliżenia przez czas własny × gęstość).

- **DAWNY NASTĘPNY KANDYDAT (nieaktualny, sprzeczny — patrz wyżej):** **samoodczyt bezpośredni** — jak często element trajektorii ma w swojej przeszłości **własny wcześniejszy element bez żadnych pośredników**. Własność samej linii świata, więc nie może zależeć od ruchu względem zespołu. Zdania do upadku: niezależność od prędkości (na własny krok), stabilność wzdłuż trajektorii, zerowa wartość dla „fotonowych” łańcuchów samych linków.

- **Do zrobienia przed rachunkiem:** zdefiniować samoodczyt jako wielkość mierzalną na strukturze (kandydat: częstość, z jaką element trajektorii zawiera w swojej przeszłości poprzedni własny zapis **bez pośredników z zewnątrz**), ustalić kontrole i zdania do upadku.

## §F2. LOGARYTMY — drugi temat (plan)

Logarytmy pojawiły się w v3.4 **wszędzie**: entropia po obcięciu (C4a.16), linki na element (C4a.19, 22), gęstość niewypełnialnych cykli (C4a.22), suma po pętlach (C4a.19), zakres pchnięć. Za każdym razem to **stosunek dwóch skal**: od najmniejszej do rozmiaru układu.
- **Hipoteza robocza [H] (asystent):** w języku informacji logarytm znaczy jedno — **liczbę bitów potrzebnych, żeby wskazać jedno miejsce spośród wielu**. Przewidywanie: wszystkie nasze logarytmy okażą się jednym zdaniem o **koszcie wskazania**, a różnić się będą tylko współczynnikiem = liczbą niezależnych kierunków wskazywania.
**WYNIK §F2 (v3.4) — WSZYSTKIE LOGARYTMY MAJĄ JEDNO ŹRÓDŁO.** W 1+1 (współrzędne stożkowe) para x≺y ma przedział o objętości uv; prawdopodobieństwo dokładnie k elementów wewnątrz = wᵏe⁻ʷ/k!, w = ρuv. Liczba par danego typu na element: ∫∫ρ f(ρuv) du dv = **∫du/u × ∫f(w)dw**. **Pierwszy czynnik = całka po pchnięciach (rapidity) = ln N** — to samo źródło co zdiagnozowane w C4a.19. Drugi = liczba zależna tylko od liczonej konfiguracji.

| wielkość z C4a | wyprowadzenie | współczynnik | zmierzone |
|---|---|---|---|
| linki na element | ∫e⁻ʷdw | **1** | 0,992 |
| ściany | ∫(w²/2)e⁻ʷdw × P(nieporównywalne)=½ | **½** | 0,506 |
| suma po pętlach | ½ × ⟨w²⟩(=12) × ⟨α²⟩ = 6⟨α²⟩ | **0,834** | 0,84 |
| niewypełnialne cykle | 1 − ½ × (ranga/F) | 0,571 | 0,57 |
| entropia po obcięciu | (1/3) × ½ (ε ∝ N^(−½)) | **1/6** | 0,17–0,19 |

- **Przewidywanie zapisane przed rachunkiem:** współczynnik pętli 6⟨α²⟩ = 0,84 ± 0,05. **PRZESZŁO:** ⟨α²⟩ = 0,13893 ± 0,00009 (Monte Carlo, 4 mln par; P(nieporównywalne) = 0,4997) → **0,834**, zmierzone 0,84.
- **Niewyprowadzone:** ranga/F = 0,857 (ułamek niezależnych ścian nad GF(2)) — zostaje wielkością zmierzoną.
- **W języku informacji:** ln N = liczba bitów potrzebna, żeby **wskazać pchnięcie** (układ odniesienia) z rozdzielczością wyznaczoną przez dyskretność. **Hipoteza „koszt wskazania” potwierdzona, z doprecyzowaniem: wskazuje się RAMĘ, nie miejsce.**
- **Wyjaśnia przegląd wymiarowy (§E):** w 1+1 grupa pchnięć jest jednowymiarowa, jej objętość to dη → logarytm; w 3+1 trzy wymiary, objętość rośnie wykładniczo z rapidity → **potęga** (zgodnie z linkami ~N^½). **Logarytm jest specyfiką 1+1, bo tam grupa pchnięć ma jeden wymiar.**
- **Most masa ↔ logarytmy:** przez szerokość zamknięty (§F1); przez ramę — **otwarty** (stan przed etap10): masa jest niesiona przez trajektorię, która wyznacza ramę; logarytm liczy koszt wskazania ramy. Do zbadania.

**MOST MASA ↔ LOGARYTMY PRZEZ RAMĘ — WYNIK (v3.4, `etap10_most_rama.py`, `etap10b_regula_mc.py`, CPU) [P][A].** Pytanie: z jaką rozdzielczością trajektoria **sama** wyznacza swoją ramę (pchnięcie η kolejnych kroków) i czy ta rozdzielczość zależy od liczby elementów na tyknięcie n = ρτ²/2 (1+1).
- **Literatura [L]:** swerves (Dowker–Henson–Sorkin; Philpott–Dowker–Sorkin) mają dyfuzję pędu ze **współczynnikiem wolnym**; wyprowadzenia skoku pchnięcia z liczenia elementów nie znaleziono.
- **Wyprowadzenie przed rachunkiem [A]:** w paśmie [τ(1−ε), τ(1+ε)] miara elementów to ρτ dτ dη, więc kandydaci w pchnięciu tworzą proces Poissona o gęstości λ = 2ερτ² = 4εn. Nadwyżka z odwrotnej nierówności trójkąta rośnie z |Δη|, więc reguła bierze najbliższego w pchnięciu; odległość ~ Exp(2λ) → **std(Δη) = 1/(4√2·ε·n)**.
- **Zdania do upadku:** P1 std·4√2εn = 1,00 ± 0,10 dla każdego n, ε; P2 wykładnik wobec n = −1,00 ± 0,05 (szum Poissona / dyfuzja dałyby −½); P3 przyrosty nieskorelowane (|r₁| < 0,05); kontrola: wybór losowy w paśmie → brak zależności od n.
- **Warunki:** d = 1+1, τ = 1, ρ = 2n, n ∈ {5, 15, 50, 150, 500} (2 dekady), ε ∈ {0,05; 0,10; 0,20}, K = 200 trajektorii × L = 16 kroków, 2 ziarna, okno |η| < 2,2, pudło 60 × 120 (do 7,2 mln elementów).

| ε | P2: wykładnik | P1: std·4√2εn (n = 5…500) | P3: r₁ | kontrola losowa |
|---|---|---|---|---|
| 0,05 | **−1,005** | 1,01–1,07 ✓ | −0,15 (n=5), potem ≤ 0,05 | 1,78–1,80, stała |
| 0,10 | **−1,004** | 1,10–1,13 — **upadło o włos** | −0,10 (n=5), potem ≤ 0,04 | 1,77–1,80 |
| 0,20 | **−0,989** | 1,34–1,59 — **upadło** | do ±0,09 | 1,75–1,79 |

- **P2 przeszło w całości** (trzy ε, dwie dekady). **Kontrola przeszła:** bez pamięci kierunku std nie zależy od n.
- **P1 upadło dla ε ≥ 0,1. Diagnoza PO FAKCIE [A] (oznaczona jako taka):** (i) sama reguła wyboru przy stałym tref daje 0,993–1,003 (`etap10b`, Monte Carlo bez przestrzeni) — to nie ona; (ii) pasmo liczone względem poprzedniego kroku sprawia, że tref błądzi multiplikatywnie (±ε na krok), a lokalna gęstość kandydatów to 4ε·ρ·tref²/2. **Po znormowaniu każdego kroku jego własnym tref: 0,997–1,034 dla wszystkich ε** (n = 50, 150; ziarno 1). Czyli prawo trzyma się **lokalnego** n; odchyłka P1 = rozrzut tref, parametr konstrukcji (ten sam mechanizm co poprawka 94).
- **P3:** przeszło dla n ≥ 15 przy ε ≤ 0,1; przy n = 5 ujemna korelacja (−0,10…−0,15) — dyskretność, kandydatów za mało; przy ε = 0,2 rozchwiane.
- **Odczyt — most [A][O]:** trajektoria rozróżnia ramy z rozdzielczością δη ∝ 1/n, więc liczba ram rozróżnialnych w zakresie R to ~R·n, a **koszt wskazania ramy = ln n + ln(4√2εR), współczynnik przy ln n równy 1**. Masa wchodzi pod logarytm: n = ρτ²/2 = (skala tyknięcia / skala dyskretności)², czyli w 1+1 **bity ramy = ln(ρ/m²) + const**. To ten sam typ zdania co §F2 (współczynnik = waga konfiguracji), z drugiej strony: tam ln N liczy ramy dostępne w strukturze, tu ln n liczy ramy, które trajektoria o danej masie sama wyróżnia.
- **Zgodność z literaturą [L]:** w propagatorach Johnstona (1+1) masa wchodzi przez m²/ρ — ten sam stosunek skal co 1/n.
- **Czego to NIE mówi:** skąd bierze się ε (pasmo tolerancji jest wyborem; współczynnik zależy od niego jak 1/ε, wykładnik nie). Wykładnik −1 jest wynikiem strukturalnym; stała nie.
- **Przewidywanie dla 3+1 (zapisane przed rachunkiem, niepoliczone):** kandydaci w H³ pchnięć, λ ∝ εn na jednostkę objętości pchnięć → **δη na składową ∝ (εn)^(−1/3)**, liczba ram ∝ n, więc **współczynnik przy ln n znów 1**. Zdanie do upadku: wykładnik std(Δη) wobec n w 3+1 = −0,33 ± 0,03.
- **3+1 — WYNIK (`etap10c_rama_3p1.py`, CPU, bez pudła) [P].** **Redukcja:** reguła patrzy tylko na pasmo wokół końca trajektorii; pasma kolejnych kroków są rozłączne (punkty nowego pasma leżą ~2τ od poprzedniego elementu), a sprinkling jest niezależny na rozłącznych obszarach i niezmienniczy względem pchnięć → każdy krok to niezależne losowanie w lokalnym układzie poprzedniego kroku, z miarą ρτ³dτ·sinh²r dr dΩ. W 1+1 ta redukcja zgadza się z pełnym przebiegiem (1,00–1,03 po lokalnym normowaniu). Wzór: rms(r) = √Γ(5/3)·((4π/3)λ₃)^(−1/3), λ₃ = ρτ⁴((1+ε)⁴−(1−ε)⁴)/4, n = ρπτ⁴/24. Warunki: n ∈ {3 … 3000} (3 dekady), ε ∈ {0,05; 0,1; 0,2}, 20 000 kroków na punkt.
  - **Q1 (wykładnik): −0,3315 / −0,3322 / −0,3326 — PRZESZŁO.** **Q2 (współczynnik): 0,983–1,006 — PRZESZŁO** (odchyłka tylko przy n = 3).
  - **Pełny sprinkling 3+1 — WYNIK (`etap11_rama_3p1_gpu.py` v2, Colab A100, przebieg użytkownika, ~70 min, szczyt 28 GB) [P].** Stała gęstość ρ = 22 918, 183 mln punktów, n ∈ {10, 30, 100, 300, 1000, 3000} (2,5 dekady), ε ∈ {0,05; 0,1; 0,2}, K = 2000 trajektorii × 3 przyrosty na punkt (6000 pomiarów; błąd statystyczny rms ≈ 0,9%), okno 4 × rms, ziarno 1. Wszystkie 2000 trajektorii żywe w każdym punkcie, obcięcie kubełków 0%.

| ε | **Q1** wykładnik (−0,333 ± 0,03) | **Q2** rms(r/wzór lokalny), n = 10…3000 (1,00 ± 0,05) | **Q3** max różnica wolne/szybkie (< 5%) | r1 (śr. po n) |
|---|---|---|---|---|
| 0,05 | **−0,3312** | 0,990–1,003 | 1,2% | +0,024 |
| 0,10 | **−0,3312** | 0,994–1,006 | 1,3% | +0,070 |
| 0,20 | **−0,3329** | 0,994–1,009 | 2,4% | +0,211 |

  - **Q1, Q2, Q3 — PRZESZŁY dla wszystkich 18 punktów.** Pełny sprinkling daje to samo co lokalne losowanie → **redukcja z etap10c stoi, wynik 3+1 stoi.** Wspólne punkty sprinklingu nie wnoszą korelacji między krokami.
  - **Surowe rms / wzór nominalny** (z tau0, nie z lokalnego tref): 0,99–1,01 przy ε = 0,05, do 1,037 przy ε = 0,2 — rozrzut tref, ten sam mechanizm co poprawka 96, w 3+1 słabszy (wykładnik ⅓ tłumi).
  - **r1 — BEZ zdania przed przebiegiem; wyjaśnienie PO FAKCIE (`etap11b_r1_tref.py`) [A]:** korelacja kolejnych |skoków| rośnie z ε (+0,02 / +0,07 / +0,21), nie zależy od n. Hipoteza: dziedziczenie tref (pasmo względem poprzedniego kroku → dwa kolejne skoki losowane przy podobnej gęstości kandydatów ∝ tref⁴). Redukcja lokalna z łańcuchem tref jak w etap11 daje **+0,021 / +0,066 / +0,224** wobec GPU +0,024 / +0,070 / +0,211; **po lokalnym normowaniu r1 = +0,002 / −0,007 / +0,013**. Wyjaśnione w całości przez regułę (wybór konstrukcji), nie strukturę.
  - **Zastrzeżenie [A] — ZDJĘTE przez etap11:** po redukcji był to tylko test wyprowadzenia; pełny sprinkling 3+1 (wyżej) potwierdził redukcję.
  - **Wniosek dla mostu:** w 1+1 δη ∝ n^(−1), w 3+1 δη ∝ n^(−1/3) na promień w H³, ale **liczba ram rozróżnialnych przez trajektorię ∝ n w obu** → **koszt wskazania ramy = ln n + const, współczynnik 1 niezależnie od wymiaru**. W odróżnieniu od §F2 (ln N — specyfika 1+1) ten logarytm **przenosi się na 3+1**. Masa pod logarytmem: n = ρπτ⁴/24 ∝ (skala tyknięcia/skala dyskretności)⁴ = ρ/m⁴ (tempo ≡ masa ∝ 1/τ).

**SKĄD ε — SKAN ε → 0 (v3.4, `etap12_eps_granica.py`, CPU) [H][P][A].**
- **Pytanie [H] (użytkownik):** w sumie Fokkera (C4a.14–15) stała zależała od szerokości warstwy Δ, a okazało się, że to błąd przybliżenia δ(s²), który znika przy cienkiej warstwie. Tu r1 rośnie z ε, a stała od ε zależy, więc ε może grać tę samą rolę. Test: skan ε w dół. Skończona granica → ε jest regularyzacją i pytanie „skąd ε” znika. Brak granicy → ε niesie prawdziwą skalę.
- **Różnica wobec Fokkera, zapisana przed rachunkiem [A]:** tam zależność od Δ była błędem przybliżenia. Tu zależność od ε jest **dokładna**: ε wchodzi wyłącznie przez λ = εn (liczba kandydatów na jednostkę pchnięcia). Przewidywanie: test rozdzieli dwie rzeczy. Stała przy stałym n granicy nie ma, a artefakty ε (r1, odchyłka surowego współczynnika) znikają jak Δ u Fokkera.
- **Warunki:** redukcja lokalna potwierdzona pełnym sprinklingiem (etap10, etap11), łańcuch tref jak w etap11 (krok 0 + 3 kroki pamięci), n = 2000, ε ∈ {0,2; 0,1; 0,05; 0,02; 0,01; 0,005} (1,6 dekady), K = 20 000 × 3 przyrosty, d = 1+1 i 3+1.

| ε | 1+1: surowy/wzór | 1+1: r1 | 1+1: E4 iloczyn (0,1021) | 3+1: surowy/wzór | 3+1: r1 | σ(tk/tref) = ε/√3 |
|---|---|---|---|---|---|---|
| 0,2 | 1,101 | +0,075 | 0,112 ✗ | 0,974 | +0,216 | ✓ (1+1), 0,1127 wobec 0,1155 (3+1) |
| 0,1 | 1,016 | +0,015 | 0,104 | 0,991 | +0,065 | ✓ |
| 0,05 | 1,008 | +0,003 | 0,103 | 0,999 | +0,014 | ✓ |
| 0,02 | 0,996 | −0,003 | 0,102 | 0,999 | +0,009 | ✓ |
| 0,01 | 1,003 | −0,004 | 0,102 | 1,001 | −0,003 | ✓ |
| 0,005 | 1,001 | +0,002 | 0,102 | 0,999 | −0,001 | ✓ |

- **E1 — stała przy stałym n NIE ma granicy (PRZESZŁO, na granicy tolerancji):** wykładnik skoku wobec ε: **−0,980** w 1+1 (przewidywane −1,00 ± 0,02) i **−0,342** w 3+1 (−0,333 ± 0,01). Oba na krawędzi pasma. Odchyłkę ciągnie punkt ε = 0,2, gdzie surowy współczynnik niesie artefakt tref (1,10 / 0,97). Po lokalnym normowaniu wszystkie punkty dają 0,995–1,006.
- **E2 — artefakt znika (PRZESZŁO):** surowy współczynnik przy ε ≤ 0,01: 1,003 / 1,001 (1+1), 1,001 / 0,999 (3+1). Odchyłka < 1%.
- **E3 — r1 → 0 (PRZESZŁO):** przy ε ≤ 0,02 |r1| ≤ 0,009 (maksimum 0,0090 w 3+1 przy ε = 0,02, na granicy). Czyli r1 zachowuje się jak Δ u Fokkera: to artefakt, który znika.
- **E4 — iloczyn niezależny od ε (1+1): PRZESZŁO dla ε ≤ 0,1** (0,102–0,104 przy przewidywanym 0,1021), **UPADŁO przy ε = 0,2** (0,112, +10%; ten sam artefakt tref). σ(tk/tref) = ε/√3 dokładnie.
- **3+1, PO FAKCIE (nie było zdania):** odpowiednik E4 to σ(tk/tref)·rms³·n = Γ(5/3)^(3/2)/(64√3) = 0,00774. Wyszło 0,00767–0,00775 dla ε ≤ 0,05 i 0,0067 przy ε = 0,2.
- **Odpowiedź na pytanie [A]: ε NIE jest regularyzacją, ale też nie niesie osobnej skali.** Stała nie ma granicy (E1), więc według kryterium użytkownika ε jest prawdziwym parametrem. Tyle że jest to **rozdzielczość tempa** trajektorii, czyli ostrość masy: σ(tk/tref) = ε/√3. Za każde zaostrzenie tempa trajektoria płaci rozmyciem ramy, a iloczyn obu rozdzielczości ustala samo n: w 1+1 σ_tempo·δη = 1/(4√6·n), w 3+1 σ_tempo·rms³ = 0,00774/n. **Budżet rozróżnialności jest jeden (n); ε mówi tylko, jak trajektoria dzieli go między masę a ramę.** Pytanie „skąd ε” zmienia się w „co ustala ten podział”. Nie znika, ale przestaje być pytaniem o nową skalę.
- **Pułapka nazewnicza [A]:** iloczyn stały przy wymianie ostrości masy na ostrość ramy **wygląda** jak relacja nieoznaczoności. Ta nazwa jest pułapką (nr 5 z listy: etykieta zamiast rachunku). To zdanie o liczbie kandydatów w paśmie, a nie o operatorach. Porównanie z mechaniką kwantową byłoby osobnym krokiem, z literaturą najpierw.
- **Artefakty ε znikają jak u Fokkera:** r1 i surowa odchyłka współczynnika. Oba biorą się z dziedziczenia tref.

**CO USTALA PODZIAŁ BUDŻETU n MIĘDZY MASĘ A RAMĘ (v3.4, `etap13_podzial_budzetu.py`, CPU) [A][P].**
- **B1 — rachunek [A]:** suma bitów tempa i ramy **nie zależy od ε** (1+1: ln(1/σ_t) + ln(R/δη) = ln(4√6·R·n); w 3+1 analogicznie, bo liczba ram ∝ εn, a σ_t ∝ ε). **Żadna zasada „maksimum informacji” nie wybiera podziału**, bo podział jest informacyjnie zdegenerowany. To stoi.
- **Kandydat [A][?] — wybór przez trwałość (hipoteza, nie wynik):** tempo błądzi, var(ln tref) rośnie o ε²/3 na krok, więc L_t = 3/ε². Rama błądzi, więc L_f = 1/rms². Maksimum min(L_t, L_f) daje ε* = 0,553·n^(−½) w 1+1, czyli ε*τ = 0,78·ρ^(−½), a w 3+1 ε*τ = 0,85·ρ^(−¼). Odczyt byłby taki: bezwzględna ostrość tyknięcia = skala dyskretności, niezależnie od masy i wymiaru.
- **Zdania do upadku (o założeniach kandydata):** B2 brak dryfu ln tref (|dryf|·L_t < 0,2); B3 nachylenie var(ln tref) = ε²/3 ± 10%; B4 ⟨r_L²⟩ = L·rms² ± 10%; B5 L_t/L_f = 1 przy ε*, 16 przy ε*/2, 1/16 przy 2ε*. Warunki: n = 200, K = 400, L = 1500 kroków, ε ∈ {ε*/2, ε*, 2ε*}.
- **Wynik: KANDYDAT UPADA NA ZAŁOŻENIACH.** B2 upadło (dryf·L_t = 0,20–0,31 w 1+1 i **1,7–2,3 w 3+1**). B3 w 1+1 wyszło 0,87–1,01, w 3+1 0,95–1,33 (mieszane). B4 i B5 upadły całkowicie (B4: 0,03–27 000 zamiast 1).
- **Diagnoza (zmierzona, K = 2000, 30 kroków):** ln tref ma **systematyczny dryf dodatni** (tyknięcie się wydłuża, masa maleje), **dokładnie ∝ ε²**: 1+1 +0,00017 / +0,00090 / +0,00335, 3+1 +0,00143 / +0,00572 / +0,02275 na krok przy ε = 0,05 / 0,1 / 0,2. To **0,50 (1+1) i 0,69 (3+1)** tego, co daje sama miara pasma ρτ^(d−1)dτ (ε²/6 i 5ε²/6); resztę znosi selekcja, która woli krótszy krok. Dryf i dyfuzja mają ten sam rząd ε², więc **w 3+1 tempo przesuwa się o czynnik ~e^1,7, zanim zdąży się rozmyć**. Do tego ostrość ramy zależy od bieżącego tempa (n_efektywne = n·tref^d), więc **budżet n nie jest zachowany wzdłuż trajektorii**, a przy rozproszonym tref średnie kwadraty są zdominowane przez ogony (stąd B4 rzędu 10⁴).
- **Wniosek [A]:** pytanie o podział budżetu jest **przedwczesne**. Najpierw reguła musi zachowywać tempo średnio, czyli pasmo bez dryfu (np. asymetryczne, z E[Δ ln tref] = 0). To jest wybór konstrukcji do zrobienia i sprawdzenia, zanim pytanie o podział będzie miało sens.
- **Związek z §F1 (PO FAKCIE, zgodność znaku i rzędu, nie ilościowa):** „dryf 0,94–0,95” tempa na 20 krokach w etap8/9 ma ten sam znak (tempo maleje). Z samego dryfu przy ε = 0,1 w 3+1 wychodzi e^(−0,11) ≈ 0,89. Różnica z 0,94–0,95 niewyjaśniona (inne szczegóły reguły w etap8/9).

**PASMO BEZ DRYFU — REGUŁA R-KĄT (v3.4, `etap15_pasmo_bez_dryfu.py`, CPU) [A][P].**
- **Ograniczenie:** pamięć musi zostać jednokrokowa. Pasmo względem pierwszego tyknięcia (v3 z etap7/8) usuwa dryf, ale wymusza A/B = 1,5, a główny wynik §F1 był niewymuszony właśnie dzięki pamięci jednego kroku.
- **Reguła R-KĄT (wybór konstrukcji, wyprowadzony, nie dopasowany):**
  - prostota to **najmniejsze względne pchnięcie r** między krokami, cosh r = (tpc² − tref² − tk²)/(2·tref·tk), czyli same objętości przedziałów. Wybór nie faworyzuje długości kroku;
  - pasmo logarytmiczne s = ln(tk/tref) ∈ [δ−ε, δ+ε], z przesunięciem **δ = −(ε·cth(dε) − 1/d)**. Kandydaci mają gęstość ∝ e^(ds), więc E[s] = 0 **dokładnie**;
  - r i tk są niezależne w mierze Poissona, więc wybrany tk ma rozkład samej miary pasma.
- **Zdania do upadku i wyniki (v2: K = 4000, 40 kroków, n = 200; ε = 0,05 / 0,1 / 0,2):**
  - **D1 dryf ln tref = 0 — PRZESZŁO:** wszystkie 6 punktów zgodne z zerem (|z| ≤ 1,52). Stary dryf (etap13) jest wykluczony na 10–40σ w 5 punktach. W 1+1 przy ε = 0,05 test ma za małą moc (stary dryf wykluczony tylko na 1,4σ). Pierwotne kryterium „|dryf|·L_t < 0,05” było niewykonalne statystycznie przy K = 400. Zastąpiłem je porównaniem z szumem po awarii v1 i przed przebiegiem v2.
  - **D2 var(ln tref) rośnie liniowo z nachyleniem var_s — PRZESZŁO:** 0,957–1,019 (±5%; 0,957 na krawędzi).
  - **D3 rms skoku ramy = wzór — PRZESZŁO:** 0,997–1,002 (wszystkie kroki, każdy znormowany przy własnym tref).
- **B5′ (L_t/L_f przy ε*, ε*/2, 2ε*) — UPADŁO w częściowym v1** (1+1: 21 / 2,2 / 2,6 przy przewidywanych 16 / 1 / 1/16; 3+1: 6,1 / 1,6), potem awaria pamięci (okno kandydatów rośnie wykładniczo przy małym tref). **Wycofane PO FAKCIE**, z dwóch powodów: (i) ostrość ramy zależy od bieżącego tempa (n_ef = n·tref^d), więc „L_f” nie jest jedną liczbą (w 3+1 w czasie L_t n_ef zmienia się o e^(±4)); (ii) zrównanie L_t z L_f wymaga umownej jednostki (e-krotność tyknięcia wobec jednostki pchnięcia), więc stała ε* jest umowna.
- **Co zostaje z kandydata „trwałość” [A][?]:** skalowanie nie zależy od umowy. Przy L_t ∝ ε^(−2) (D1, D2) i L_f ∝ (εn)^(2/(d−1)) (etap10–12) zrównanie przy dowolnym stosunku daje **ε*·τ ∝ ρ^(−1/d)**, czyli bezwzględna ostrość tyknięcia jest rzędu skali dyskretności w każdym wymiarze. To warunek **lokalny** (w każdym kroku). Obserwacja [?]: sugeruje pasmo o **bezwzględnej** szerokości ~ℓ zamiast względnej ε. Niesprawdzone, a samo kryterium trwałości pozostaje hipotezą.
- **§F1 przy R-KĄT — WYNIK (`etap16_masa_rkat_gpu.py`, Colab A100, przebieg użytkownika, 2 ziarna, K = 20 000, po filtrze ścian ~10–11 tys. na populację) [P].**

| | F1 A/B (1,500 ± 0,010) | F2 kor(v) A / B (< 0,05) | F2 szybkie/wolne A / B (1,00 ± 0,02) | F3 dryf A / B (1,00 ± 0,02) | F4 rozrzut / przewid. A / B (1 ± 0,15) |
|---|---|---|---|---|---|
| ziarno 1 | **1,523 ✗** | +0,023 ✓ / **+0,212 ✗** | 1,008 ✓ / **1,092 ✗** | **1,050 ✗** / **1,032 ✗** | **1,009 / 1,004 ✓** |
| ziarno 2 | **1,530 ✗** | +0,026 ✓ / **+0,186 ✗** | 1,014 ✓ / **1,084 ✗** | **1,056 ✗** / **1,030 ✗** | **1,015 / 1,011 ✓** |

  - **F4 PRZESZŁO (1,004–1,015):** rozrzut tempa ~15% to w całości błądzenie ln tref przy pamięci jednokrokowej. „Naturalna szerokość masy” jest złożeniem pasma i błądzenia w czasie (uzupełnia poprawkę 94).
  - **F1, F3 UPADŁY w obu ziarnach; F2 upadło dla B** (gorzej niż w etap8).
  - **Diagnoza PO FAKCIE (`etap16b_okno_diagnoza.py`, redukcja lokalna bez okna) [A][P]:**
    - Hipoteza 1 („okno obcina już pierwszy krok”) **odrzucona:** poza oknem 0,03%.
    - Hipoteza 2 (dopisana po wyniku 1): **przy gęstości z etap8 tyknięcie mieści n_A ≈ 0,31 i n_B ≈ 1,55 elementu, więc skok pchnięcia na krok ma rms 0,73 (A) i 0,44 (B), a pchnięcie trajektorii błądzi o ~2–3 jednostki w 19 krokach.** Bez okna mediana prędkości końcowej wynosi 0,98 (A) i 0,85 (B). **Okno z etap8/16 (dt < 3h w czasie pudła, zasięg ~2h) odcina kroki 1–6 / 7–12 / 13–18: A 9,6% / 53,5% / 79,2%, B 1,5% / 18,1% / 41,3%;** 92% łańcuchów A ma co najmniej jeden krok poza oknem. **Potwierdzona.**
    - Czyli od około 7. kroku **trajektorię kształtuje okno w układzie pudła**, a nie reguła. To jest właśnie układ zewnętrzny, który etap7 miał usunąć. Kierunek zgadza się z wynikami: okno odcina długie dt, więc skraca tyknięcie (F3 > 1, silniej dla rzadszego A) i zawyża tempo A (F1 > 1,5).
  - **KONSEKWENCJA DLA §F1 (etap7–9) [A] — WNIOSEK, NIE POMIAR:** tamte przebiegi miały te same gęstości i to samo okno, a reguła najmniejszej nadwyżki wybiera najbliższego w pchnięciu tak samo. **Wyniki „tempo niezależne od v do 0,9” i „A/B = 1,507” zostały więc uzyskane w reżimie, w którym dominuje okno pudła. Nie są ustalone jako własność porządku.** Status obniżony do: zmierzone w konkretnym oknie, do powtórzenia. Bezpośrednio sprawdzone tylko dla R-KĄT (etap16/16b). Dla reguły nadwyżki to wnioskowanie z tego samego mechanizmu.
  - **Dlaczego nie powtórzyć długich łańcuchów w gęstym reżimie:** przy n_A ~ 300 i 12–20 krokach pudło musiałoby mieć ~10⁹–10¹⁰ punktów. Droga wykonalna: **walidacja redukcji lokalnej dla R-KĄT na krótkich łańcuchach** (etap17, niżej). W samej redukcji niezależność tempa od v jest dokładna z niezmienniczości, a A/B i dryf wynikają z miary pasma.
- **REDUKCJA LOKALNA JEST TWIERDZENIEM, NIE PRZYBLIŻENIEM [T][A] (v3.4, po uwadze użytkownika [H]: „1,5 h na A100 to więcej obliczeń niż Grossmann przez 8 lat — to nie jest dobry znak”).**
  - **(i) Kolejne pasma są rozłączne dokładnie.** Weźmy x z pasma poprzedniego kroku (τ(p,x) ∈ τ[1−ε, 1+ε]) leżące w przyszłości tip. Z odwrotnej nierówności trójkąta τ(p,x) ≥ τ(p,tip) + τ(tip,x) ≥ 2τ(1−ε) > τ(1+ε) dla ε < 1/3. Sprzeczność. To samo zachodzi dla wszystkich wcześniejszych pasm (są jeszcze dalej), więc każde pasmo jest nowym kawałkiem sprinklingu, niezależnym od poprzednich (Poisson na rozłącznych obszarach).
  - **(ii) Rozkład na iloczyn.** W paśmie d⁴x = τ³dτ·dV_H (długość kroku × przestrzeń pchnięć H³), więc kandydaci to proces Poissona na H³ z niezależnymi znakami τ o gęstości ∝ τ³ (twierdzenie o znakowaniu). R-KĄT wybiera po samym pchnięciu, więc **znak τ wybranego punktu ma rozkład miary pasma i nie zależy od r**. Stąd G1 (E[s] = 0 z definicji δ), G2 (var s = var_s) i G4 (niezależność) są **twierdzeniami**. G3 to rozkład najbliższego punktu Poissona w H³ (wzór z etap10c).
  - **(iii) Niezależność tempa od prędkości** wynika z niezmienniczości miary względem pchnięć. Jest dokładna.
  - **Konsekwencja:** na nieskończonym sprinklingu R-KĄT daje tempo błądzące bez dryfu, z rozrzutem var_s na krok, niezależnie od v. Zdania §F1 dla R-KĄT wynikają z twierdzenia. **Etap17 WYCOFANY przed uruchomieniem:** sprawdzałby tylko implementację okna w pudle. Etap11 (~70 min na A100) potwierdził w praktyce twierdzenie, które dało się zapisać w trzech linijkach; potwierdzenie ma wartość kontroli kodu, a nie wyniku o strukturze.
  - **Co to mówi o etap16:** jedyne, co w skończonym przebiegu może złamać redukcję, to okno w układzie pudła, i dokładnie to się stało. Porażka F1/F3 w etap16 to więc porażka pudła, a nie reguły.

**WYPROWADZENIE ranga/F — ROZPOZNANIE STRUKTURY H₂ (v3.4, `etap14_h2_struktura.py`, `etap14b_h2_liczniki.py`, CPU) [P][A].**
- **Cel poprawiony [A]:** 0,857 to wartość przy skończonym N (N = 16–32 tys.). Granica z ekstrapolacji (C4a.22, odczyt A) wynosi 0,833–0,843, a z przyrostów na podwojenie N (dim H₂/el ≈ 0,076·ln N, F/el ≈ 0,48·ln N) około 0,84. Wyprowadzać trzeba **granicę 1 − c_H/c_F**, gdzie c_F = ½ jest już wyprowadzone w §F2.
- **Z czego składa się H₂ (N = 3000, 1+1):** dim H₂ = 1030. Po redukcji wag baza to **1028 zamkniętych powierzchni z 4 ścian na 6 elementach** (plus jedna z 6 i jedna z 8 ścian). **Wszystkie 4-ścienne powierzchnie (1782) mają rangę 1028**, więc H₂ jest rozpięte przez „ośmiościany”. Są dwa typy:
  - **typ I „2-2-2”:** dwa dolne, para środkowa, dwa górne; wszystkie 4 ściany mają tę samą parę środkową;
  - **typ II „1-2-2-1”:** przedział x≺y, w którym dwa dolne i dwa górne tworzą motyl (każdy dolny ≺ każdy górny).
- **Kawałek wyprowadzony [A]:** typ II w najprostszej postaci (przedział z dokładnie 4 elementami w układzie motyla) ma współczynnik przy ln N = ∫(w⁴/4!)e^(−w)dw × P(4 punkty tworzą motyl) = **1 × 1/24** (P z permutacji: jedna z 24). Zmierzone przyrosty #II/N na podwojenie: 0,033 i 0,031, czyli ≈ 0,046 na jednostkę ln N (przewidywane 0,0417; zakres N 1000–8000, poniżej dwóch dekad).
- **Co blokuje pełne wyprowadzenie:** zamkniętych powierzchni jest więcej niż wymiarów. Przy N = 3000 jest 1782 czterościennych, rang 1028, czyli 754 zależności. Rangi: typ I 544 (z 874), typ II 524 (z 565), I+II razem 908. Pozostałe 120 wymiarów dają powierzchnie typu II, w których przedział x≺y zawiera dodatkowe elementy. Wyprowadzenie to **liczenie lokalnych konfiguracji z włączeniami–wyłączeniami**: każda liczba to czysta całka typu ∫du/u × waga, ale trzeba policzyć też konfiguracje zależności. Program jest wykonalny, ale długi.

- **Test:** sprawdzić, czy współczynniki przy ln N z C4a.19 i 22 (1 dla linków, ½ dla ścian, 0,57 dla defektów) dają się wyprowadzić z liczby stopni swobody wskazania, zamiast być dopasowane.

# §E — DYSCYPLINA

## Przegląd wymiarowy — co z 2D przenosi się na 3+1 [A] (v3.4)

2D (literaturowe: jeden kierunek przestrzenny + czas) wybiera się, bo relacja jest iloczynem dwóch porządków liniowych, propagator to ½·C i małe N wystarcza na dekadę. **Każdy z tych powodów czyni 2D wyjątkowym, a nie uproszczonym.**

| wynik z C4a | przenosi się na 3+1? |
|---|---|
| porządek nie widzi pchnięcia przy ustalonej objętości | **tak** (niezmienniczość Lorentza, niezależna od wymiaru) |
| suma Fokkera z miarą i odległością z porządku | prawdopodobnie, z inną potęgą wagi; niesprawdzone |
| odległość z nakładania przyczynowego | **tak** (BK dla dowolnego d) |
| logarytm we wszystkich licznikach linków | **nie** — w 3+1 linki/el ~ N^(1/2) (prawo 2−2/d, C2): **potęga** |
| reguła „logarytm = ślad cięcia” (niżej) | **zagrożona** — w 3+1 rozbieżność pchnięć jest potęgą i reguła uznałaby ją za zwykłą gęstość |
| błądzenie łańcucha 2/3 (KPZ) | **nie** — specyfika 1+1 |
| stosunki 0,856 / 0,60 | **nie** — własność grafu linków w 2D |
| brak pola magnetycznego | nie dotyczy — w 1+1 go nie ma |
| logarytm entropii 1/6 | **nie** — specyfika CFT w 2D |

**Zarzut z ramy (użytkownik + asystent) — najmocniejszy:** w 2D jest **jeden** kierunek przestrzenny, więc **nie ma miejsca na triadę**. 2D nie jest uproszczoną wersją badanej struktury, tylko strukturą pozbawioną składnika, od którego zaczyna się reszta. **Dodatkowo:** w 2D działanie Einsteina–Hilberta jest topologiczne, więc przejście krystaliczne w 2D rzędach (Surya 2012; Glaser–O'Connor–Surya 2018) nie odpowiada niczemu w 3+1. **Reguła wzrostu musi być projektowana od razu dla 3+1.**

## Reguła językowa dla Ø [H] (użytkownik, v3.4)

**Ø nie może być podmiotem zdania z orzeczeniem o cesze.** Zamiast „Ø ma cechę Y” wolno tylko: „**od strony otoczenia X** Ø wygląda w naszym opisie jako Y”. Opis pośredni jest dozwolony, bo niesie informację, skąd patrzymy; opis bezpośredni zawsze jest projekcją — tym samym mechanizmem co opinia (stan aparatu przypisany obiektowi). Lekarstwo to samo co przy opinii: **cofnąć przypisanie i oddać cechę relacji.** Sprawdzenie mechaniczne: każde zdanie z Ø jako podmiotem i orzeczeniem o cesze przepisać tak, by podmiotem było otoczenie lub relacja.
Naruszenia dotąd: poprawka 65 (podział Ø na „punkty kontaktu” i „brzegi hierarchii”), wcześniej rozmowa 5 („superpozycja to miejsce, gdzie relacja jest, ale nic nie odróżnione”).

## Sztuki czy miara [H] — reguła z v3.4

1. **Test.** Liczba jest dopuszczalna tylko wtedy, gdy nie rośnie z gęstością. Jeśli rośnie, jest **gęstością**, nie liczbą: pomnóż przez potęgę $t_P$ wynikającą z wymiaru i sprawdź, czy wynik przestaje zależeć od N.
2. **Warunek falsyfikowalności.** Potęga musi być **przewidziana z wymiaru przed rachunkiem**, nie dopasowana po. Inaczej każdy szereg potęgowy da się „unormować” i reguła niczego nie zabrania.
3. **Wyjątek (ważny w 2D — w 3+1 zagrożony, patrz przegląd wymiarowy).** Logarytmu nie unormuje żadna potęga $t_P$. **Logarytm jest znakiem, że cięcie już zostało zrobione** (entropia: bez obcięcia gęstość, wykładnik +1,10; po podwójnym obcięciu $0{,}188\pm0{,}065$ razy $\ln N$ — C4a.16).

Dotąd: pętle (Pellegrin), pary między liniami świata (C4a.11/14/15), fragmenty otoczenia (C4a.8) — wszystkie rozbieżne jako sztuki. Bliźniaki (A3a) **nie są** kontrprzykładem: prawo $n^{k-(k-1)d}$ samo jest normalizacją. Mody w podzbiorze **nie należą** do tej serii — tam problemem było niezerowe centrum algebry, a lekarstwem redukcja symplektyczna (C4a.2).

## Reguły

**Nowe w v3.2 (na górze, bo najczęściej łamane):**

- **Nie przejmować interpretacji [H] (użytkownik, v3.4).** Formalizmy i wyniki są gotowe; nowy jest tylko sposób patrzenia, którego w literaturze nie ma. Dlatego przed każdym rachunkiem i przed każdym pytaniem wziętym z literatury: **co właściwie chcemy policzyć** i co ta wielkość albo to pytanie **zakłada w swojej interpretacji** (kierunek, cechę obiektu, zewnętrzny parametr, gotową czasoprzestrzeń, podział układ/otoczenie). Jeśli zakłada — przełożyć na relacje albo odrzucić. Z literatury bierzemy formalizm i wynik, nie pytanie. **Złamane:** porządek w R6 z kolejności budowania (poprawka 106); „zgodność kierunku bez hipotezy przeszłości” (110); estymator Myrheima–Meyera użyty na sieci, choć zakłada sprinkling w Minkowskim (kalibracja C5); krzywizna Olliviera na skali ogniwa, gdzie z twierdzenia nie zbiega (105).
- **Sprawdzić literaturę przed rachunkiem, nie po.** Sprawdzenie kosztuje zapytanie, rachunek kosztuje sesję. W rozmowie 4 odkryto koło cztery razy: Glaser–Surya (lokalność, 2013), Minz (bliźniaki, 2024), Boguñá–Krioukov (odległość przez nakładanie, 2024), Sorkin–Yazdi (prawo objętościowe). Wszystkie jednym zapytaniem.
- **Rachunek bez zdania, które mogłoby przez niego upaść, nie jest rachunkiem.** Kryterium z A0 stosuje się do własnych przebiegów, nie tylko do cudzych publikacji. Znaczna część rozmowy 4 to były pomiary bez tezy.
- **Wniosek z zakresu węższego niż dekada nie jest wnioskiem.** Trzykrotnie w v3.2 wniosek odwrócił się po poszerzeniu zakresu: siatka Fibonacciego, zdegenerowane d=2, przedczynnik przy L.
- **Związać skalowanie parametru to za mało — trzeba przeskanować każdy parametr, który ustawiłeś sam.** L związano jako $n^{1/d}$, stałą zostawiono na 1, i to ona niosła wynik.
- **Wymiar wkładany na górze skryptu nie jest wymiarem zmierzonym.** `sprinkle(n, d, ...)` sprawia, że „wszystko wychodzi funkcją d" jest po części tautologią.
- **Celem jest klasa nieodróżnialności, nie „jeden element".** Mierzenie, kiedy element daje się wskazać jednoznacznie, to kryterium z zewnątrz. Ø jest w pliku od A3 i nie było używane jako cel.
- **Tam, gdzie skończony rozmiar psuje dopasowania, szukać wielkości progowych zamiast ciągłych.** Próg jest liczbą całkowitą i nie da się go przesunąć o kilkanaście procent (A9d). **Zastrzeżenie: obowiązuje w przestrzeni konforemnie płaskiej; pod krzywizną próg się rozmywa zamiast przeskakiwać** (§D, fala pp).
- **Obciążenie estymatora zależy od struktury**, więc porównania między strukturami przy stałej liczbie prób są obciążone (poprawka nr 11).
- **Zagnieżdżone obcięcia jednego losowania nie są niezależnymi pomiarami.** Pięć punktów `P[:n]` z jednego sprinklingu wyglądało na stabilność, a było jedną realizacją czytaną pięć razy.
- **Duży koszt obliczeń to sygnał ostrzegawczy [H] (użytkownik, v3.4).** Zanim coś pójdzie na godziny GPU, zapytać: czy to nie jest twierdzenie, które da się udowodnić, albo czy koszt nie wynika z zewnętrznego układu, który sami wkładamy (pudło, okno, siatka)? Wykryte w §F2: etap11 potwierdzał twierdzenie; etap16 był zdominowany przez okno pudła.
- **Nie traktować ramy sztywno.** Rama jest propozycją (§R). Czytanie ilustracji (przypowieść o kropkach) jako specyfikacji dało kandydata wybranego ze złego powodu.

**Z wcześniejszych wersji:**

- **Kontrole graniczne przed rachunkiem, nie po.** Jeśli nie da się takiej wypisać, rachunek jest niesprawdzalny.
- **Kontrole łapią błędy rachunku. Nie łapią błędów pojęciowych.**
- **Liczba bez warunków nie jest wynikiem.** n, d, estymator, liczba prób.
- **Zgodność dwóch wielkości związanych tożsamością nie jest potwierdzeniem.** To sprawdzenie dzielenia.
- **Dwa błędy potrafią się znieść i wyprodukować zgodność.**
- **Poprawka może przenieść błąd o piętro, zamiast go usunąć.** Po każdej poprawce pytać: czy nowe zdanie coś wyróżnia, czy jest prawdziwe o wszystkim.
- **Zepsuty kod potrafi dawać wynik bliższy teorii niż poprawny.** Z₂: 0,42–0,44 (zepsuty) wobec 0,4407 (teoria) i 0,450 (poprawny).
- **Rachunek nie chroni przed złym odczytaniem własnego rachunku.**
- **Nazwa jest miejscem, gdzie najczęściej wchodzi błąd.**
- **Nie zamieniać obserwacji strukturalnej w falsyfikowalną hipotezę, żeby ją obalić.**
- **Rozdzielać policzone od zinterpretowanego.**
- **Wyniki negatywne najcenniejsze do audytu.**
- **Aksjomaty ustalone niezależnie od pytania**, do którego są stosowane.
- **„Prostota" jako kryterium akceptacji jest ryzykowna.** Aktualne zastosowanie odpadło razem z plateau (poprawka nr 12).
- **Struktura vs treść.** Logika relacyjna działa na poziomie warunków możliwości orzekania. Konkretny rozkład (np. Poisson) to już treść i podlega falsyfikacji.
- **Porządkowanie idzie przed liczeniem.**

## Rejestr poprawek — 

| # | co | gdzie | kto |
|---|---|---|---|
| 1 | Ø rozbite na rodzaje; należy do otoczenia | A3 | **użytkownik** |
| 2 | horyzont nie jest końcem relacji | A5 | **użytkownik** |
| 3 | Ø ≠ zbiór pusty ZFC | A3 | **użytkownik** |
| 4 | otoczenie mierzone w trzech różnych jednostkach | A8 / C2 | **użytkownik** |
| — | „zerowe otoczenie chwili zero" wbrew własnemu estymatorowi | A8 | **użytkownik** |
| 5 | f(d) vs ułamek — zgodność z dwóch znoszących się błędów | A4b | asystent (audyt v2) |
| 6 | poprawka nr 2 przeniosła błąd o piętro | A5 | asystent (audyt v2) |
| 7 | 3,18 i 10,3 to dwie różne wielkości pod jedną nazwą | A2 | asystent (v3) |
| — | korelacja 0,87–0,96 zestawiona z innej struktury | A4b / B2 | asystent (v3) |
| 8 | pole horyzontu jako $n^{0,75}$ — objętość zamiast pola | A4e | **użytkownik** |
| 9 | „dwie drogi do f" to jedno wyrażenie | A4b | **użytkownik** |
| 10 | (1−f)·d to kolano, nie zbieżność | A4c | **użytkownik** |
| **11** | **zakres walidacji SIS; obciążenie rośnie z n i zależy od struktury** | **A4** | **asystent (v3.2)** |
| **11a** | **Księżyc 2,65×10⁶² → 1,43×10⁶²; łamie własne prawo $M^2$** | **A5b** | **asystent (v3.2)** |
| **12** | **f jest funkcją ułamka uporządkowania ⇒ (1−f)d nie jest niezależne** | **A4c** | **asystent (v3.2)** |
| **13** | **0,700 to f(≈5,5); obszar nie był interwałem przyczynowym** | **A4b** | **asystent (v3.2)** |
| **14** | **poprawka nr 10 odwrócona — brak kolana, zbieżność do 1,542−0,661/d** | **A4c** | **asystent (v3.2)** |
| **15** | **perkolacja „blisko krzywej" to znany fałszywy alarm** | **A9a** | **asystent (v3.2, po literaturze)** |
| **16** | **L: związano skalowanie, nie sprawdzono stałej** | **A9d / §D** | **asystent (v3.2)** |
| **16a** | **sito $a+bd$ wycinało połowę przypadków; $a+b/d$ równie naturalne** | **§C** | **asystent (v3.2, po literaturze)** |
| **17** | **test odkształceniowy mierzy jeden z dwóch znoszących się członów** | **A11e** | **asystent (v3.2)** |
| **17a** | **C1: przeszkodą nie jest etykieta, tylko brak wewnętrznego cięcia** | **C1** | **asystent (v3.2)** |
| **18** | **d=2 jest zdegenerowane w trzech opublikowanych sensach — nie nadaje się na przypadek walidujący** | **A9e** | **asystent (v3.2, po literaturze)** |
| **19** | **rama traktowana sztywno; przypowieść czytana jako specyfikacja** | **§R** | **użytkownik** |
| **20** | **rachunek bez zdania, które może przez niego upaść, nie jest rachunkiem** | **§E** | **użytkownik** |
| 20a | poprawka w A5a była bez numeru — nadany w v3.4 | A5a | asystent (v3.4) |
| — | **błędna kontrola KR (ułamek 3/8, nie „prawie same pary przestrzenne") — złapana PRZED rachunkiem** | A9a | asystent (v3.2) |
| — | **przepełnienie uint8 w liczeniu linków, zależne od d (10,7% fałszywych przy d=2, 0,0% przy d=4)** | C1 | asystent (v3.2) |
| — | **siatka Fibonacciego: $m^*$ przesuwało się o jedno oczko na podwojenie n, dając pozorny wykładnik 0,65 przy każdym d** | A9e | asystent (v3.2) |
| — | **średnia z rozmiaru klasy zamiast średniej z logarytmu — krzywe niemonotoniczne** | A9e | asystent (v3.2) |
| — | **nadajniki na stałym promieniu nakładały się w d=2** | A9d | asystent (v3.2) |
| 21 | 4D = 3D + dynamika + pamięć; „rozbieżność” rozmowy i pliku była różnicą zapisu | R1a, pułapka 5 | **użytkownik** (v3.3) |
| 22 | propozycja „faza = płaszczyzny iΔ” to mody skalarne, nie pole EM | Dalej otwarte | asystent (v3.3, po literaturze) |
| 23 | pętla z dwóch łańcuchów p→q jest tylko elektryczna (Pellegrin) | Dalej otwarte | asystent (v3.3, po literaturze) |
| 24 | test plateau: reszta ≠ dopełnienie przyczynowe; globalne obcięcie daje fałszywe plateau | §D, C4 | asystent (v3.3) |
| — | falsyfikator „różne wyniki = nieporównywalne” źle postawiony — trzeba wzajemnego wykluczenia | R1a | **użytkownik** (v3.3) |
| — | „tło oddzieli się, bo inne pochodzenie” → zamienione na dwa przebiegi i zdania 3–5 | C4 | **użytkownik** + asystent (v3.3) |
| 25 | schemat Eulera łamał komutatory; „test znaku” był artefaktem | C4a.1 | asystent (v3.4) |
| 26 | ujemna I(S:F) z niekomutujących podukładów, nie z obcięcia; przewidywanie „obcięcie strukturalne” upadło | C4a.2 | asystent (v3.4) |
| 27 | test reguły sumy na plastrze źle postawiony — plaster nie jest dopełnieniem S | C4a.3 | **użytkownik** (v3.4) |
| 28 | „Σ I(S:Fᵢ) ≥ I(S:P) zawsze” fałszywe (redundancja/synergia); znak informacji interakcyjnej odwrócony | C4a.4 | asystent (v3.4) |
| 29 | „zgodne z QBM” za mocne — przebieg był przy s=1 | C4a.4 | asystent (v3.4) |
| 30 | brak asymetrii orientacji = artefakt szybkiego oscylatora (ωτ≈10 rad) | C4a.5 | asystent (v3.4) |
| 31 | wzrost wykładnika z δ = artefakt różnych zakresów s (ucięcia) | C4a.6 | asystent (v3.4) |
| 32 | „forma s^(2δ) UPADŁA” przedwczesne — δ=0,5 poza zasięgiem rozdzielczości | C4a.6 | asystent (v3.4, po lekturze źródła) |
| 33 | test małego δ źle postawiony — niepełne otoczenie | C4a.6 | asystent (v3.4) |
| 34 | odniesienie asymptotyczne 2H_S zamiast dokładnego 1+e^(2δH) | C4a.7 | asystent (v3.4) |
| 35 | seria N na składowych zafałszowana wzrostem fragmentów | C4a.7 | asystent (v3.4) |
| 36 | „większe fragmenty → niższe nachylenie” — w dużej części rozrzut z dowolnego wyboru linków | C4a.8 | asystent (v3.4) |
| 37 | pole bez wzbudzenia ≡ Ø — ściśnięcie zapisuje w pustce; potrzebny zespół przesunięć | C4a.9 | **użytkownik** (v3.4) |
| 38 | samo przesunięcie nie zmienia entropii (kowariancja) — konieczny rozrzut V_d | C4a.9 | asystent (v3.4) |
| 39 | plateau nie wyznacza skali: najmniejszy wystarczający fragment = 1 link przy każdym N | C4a.10 | asystent (v3.4) |
| 40 | link ≠ dyskretny stożek dla odległych zdarzeń (wysycenie) | C4a.11 | asystent (v3.4) |
| 41 | kontrola z koronami źle postawiona (czwórki zamiast pętli z linków) | C4a.11 | asystent (v3.4) |
| 42 | „foton = łańcuch linków przy stożku” fałszywe — rozmycie nie maleje z gęstością | C4a.13 | asystent (v3.4) |
| 43 | fala NIE należy do Ø — słowo „fala” zakłada wzbudzenie; do Ø należy pole | C4a.13 | **użytkownik** (v3.4) |
| 44 | **punkt 11 błędny**: liczone pary zamiast ważenia miarą; ważona suma Fokkera nie rozbiega się z N | C4a.14 | asystent (v3.4) |
| 45 | resztkowa zależność od Δ to błąd przybliżenia δ(s²), nie dyskretność (zbieżność po Δ/d², rozrzut 3,8%) | C4a.15 | asystent (v3.4) |
| 46 | kryterium „sztuki czy miara”; bliźniaki i mody w podzbiorze wyjęte z serii | C4a.16 | **użytkownik** (v3.4) |
| 47 | uproszczone obcięcie ≠ podwójne obcięcie SY; współczynnik 0,18 niepotwierdzony | C4a.16 | asystent (v3.4) |
| 48 | λ liczone wprost z W zamiast przez ν=(iΔ)⁻¹R — stąd ujemne entropie; po poprawce wynik 0,188±0,065 | C4a.16c | asystent (v3.4) |
| — | pytanie „czy skala Sorkina ma odpowiednik w porządku, czy jest importem” | C4a.12 | **użytkownik** (v3.4) |
| — | żądanie powtórzenia z pełnym podwójnym obcięciem przed zapisaniem zgodności | C4a.16 | **użytkownik** (v3.4) |
| — | pomiar dwóch stosunków naraz; filtr R>1,02 a zakres dopasowania; test rozmiaru fragmentu | C4a.7 | **użytkownik** (v3.4) |
| — | streszczenie QBM: niezmienniczość kształtu dotyczy ściśnięcia i czasu, nie rozmiaru otoczenia | C4a.4 | asystent (po lekturze) |
| 49 | wynik 0,188 wisiał na jednej wartości c; skan pokazuje nachylenie od +0,66 (c=0,5) do +0,045 (c=3) | C4a.16c | **użytkownik** + asystent (v3.4) |
| — | czas: przeszłości nie ma, jest zapis w strukturze, odczyt zawsze teraz; zapis nierównomierny (ostry vs rozproszony) | R1a | **użytkownik** (v3.4) |
| — | granice Ø jako relacja jednostronna: niezmienniczość od środka, nieosiągalność drogą ciągłą, przejście tylko jako zdarzenie w jednym kierunku | R1a | **użytkownik** (idea) + asystent (zapis) (v3.4) |
| — | skróty myślowe dozwolone, jeśli czytelnik wie, że to skróty; słownik skrótów z odczytem relacyjnym w „Jak czytać” | Jak czytać | **użytkownik** (zasada) + asystent (słownik) (v3.4) |
| — | reguła językowa: Ø nie może być podmiotem zdania z orzeczeniem o cesze; opis wolno tylko pośrednio, od strony otoczenia | §E, pułapka 1 | **użytkownik** (v3.4) |
| 69 | v2: geometria odłączona od czasu; v3, v5: zakleszczenie (odczyt zjada front); v4: relaksacja przez partnera partnera tworzy skróty, narodziny na brzegu geometrycznym tworzą huby | C5 | asystent (v3.4) |
| — | krawędź = front informacyjny (Ø z przodu, otoczenie z tyłu) — [H] przeskok, niewyprowadzony (status nadany przez użytkownika) | C5 | **użytkownik** (v3.4) |
| 70 | asystent nazwał hipotezę frontu „spójnym obrazem” i zbudował na niej reguły bez oznaczenia statusu; **przemianował wynik negatywny z literatury (mały świat) na „wymóg inflacji”** — przeklasyfikowanie po fakcie; wycofane, zostaje wersja warunkowa | C5 | **użytkownik** (wykrył) / asystent (błąd) (v3.4) |
| — | dylatacja grawitacyjna = stosunek tempa odczytu dwóch czytających; przesunięcie ku czerwieni = rozproszenie zapisu; ten sam wiersz tabeli granic Ø co v → c | R1a | **użytkownik** (pytanie) + asystent (przekład) (v3.4) |
| — | czarne dziury jako pytanie otwarte; OTW najpierw oczyścić z interpretacji; ujęcie informacyjne | Dalej otwarte | **użytkownik** (v3.4) |
| — | **zasada metody: korzystamy z istniejącej nauki oczyszczonej z interpretacji; nie mnożymy hipotez; zmiana sposobu patrzenia jako wkład** (+ dyscyplina: zostaje mierzalne i strukturalne, odpada narracja — asystent) | Jak czytać | **użytkownik** (v3.4) |
| — | **c = prędkość przekazu informacji, nie pokonywania dystansu**; rozwiązanie dychotomii: ta sama relacja przed odczytem (nieograniczona walencja) i po nim (skończona) | C5, słownik | **użytkownik** (v3.4) |
| — | **nieskończone c = pole EM bez wzbudzeń — fundament ramy**; rozstrzygnięcie musi nastąpić na poziomie światła; pole EM w próżni i jego wzbudzenia = „relacja przestrzeni” | C5 | **użytkownik** (v3.4) |
| — | **nieskończone c = pole EM bez wzbudzeń; pole EM w próżni i fale EM = relacja przestrzeni; dychotomia rozstrzyga się na poziomie światła** | C5, R1a | **użytkownik** (v3.4) |
| 76 | **test na poziomie światła: warstwa odczytów w sprinklingu ma wymiar 3,01 i skończoną walencję, a tło zachowuje nieograniczoną walencję i niezmienniczość Lorentza — dychotomia rozwiązana w jednej strukturze**; kontrola losowa daje płaski profil | C5 | **użytkownik** (kierunek) + asystent (test) (v3.4) |
| — | dlaczego nie więcej wymiarów: przy czterech punktach odczyt ma już minimalną pojemność na zmianę i pamięć; nic nie wymaga piątego; 3D jako strukturalne minimum | C5 | **użytkownik** (v3.4) |
| 80 | rodzina „powielanie węzła” nie daje rozmaitości przy żadnej liczbie połączeń — teza o triadzie wciąż oparta na jednej rodzinie; potwierdza: rozmaitość wymaga wstawiania pomiędzy, nie doklejania | C5 | **użytkownik** (przebieg) + asystent (v3.4) |
| 79 | test „więcej partnerów”: przy >3 połączeniach dwa pomiary wymiaru przestają się zgadzać — struktura przestaje być rozmaitością; zgodność tylko dla triady (2) i triady z pamięcią (3) | C5 | asystent (v3.4) |
| 91 | piąta pułapka: minimum τ(p,c) preferuje małe kroki; prostota = nadwyżka z odwrotnej nierówności trójkąta | §F1 | asystent (v3.4) |
| 167 | **stan zespołu — zestawienie po 166** (tabela z końca sesji 3, [91] zapisu; w sesji 3 niewpisana): funkcje (3 sprzężenia; 9 Yukaw tylko jako stosunki = odczyt B; λ); współczynniki z ramy (niewyprowadzone: grupa, pokolenia, 3/2(Y_u†Y_u − Y_d†Y_d)); pojęcia zdefiniowane (R1f-4); 19 odczytów = spójność; jedno trafienie (λ, β_λ na końcu Plancka → m_H, m_t); dwa nietrafione (Pendleton–Ross, Hill); nieustalone (e : μ : τ, hierarchia, stałe z całości); otwarte; „Gdzie zaczynać” 3–4 uzupełnione | §F1, Gdzie zaczynać | **użytkownik** („chyba nie został zapisany w sesji 3”) + asystent (v3.5) |
| 166 | **stosunki e : μ : τ — dwa odczyty; rama ich nie ustala:** A = faza na własne tyknięcie (R1f-3, masa biegunowa), B = Yukawy przy wspólnej rozdzielczości (R1d, §F1 poziom 2) — **cicha zmiana odczytu w 154 pkt 3 (błąd asystenta):** „bez skali” uzasadnione na B, Koide liczony na A; etap23 (PDG 2024; Antusch–Hinze–Saad 2025): B stoi (≤ 1,1·10⁻⁴ na 14 dekadach), A ≠ B o 1,00 / 1,88 / 2,91% (jedna pętla QED do ~2%), Q_A = 2/3 − 2,2·10⁻⁶ (−0,43σ), Q_B = 2/3 + 1,16·10⁻³ (63σ); δ = 2/9 tylko na A; zdanie po zdaniu: 0 warunków na 2 stosunki (≡ pełne → Y = 0; S₃L × S₃R → (0, 0, 3k); natura przeczy → e, μ, τ odróżnialne wyłącznie przez relację z tłem); Froggatt–Nielsen dopasowane albo nowe byty (zamyka „Następne” ze 150); pytanie Sumino źle postawione po filtrze; pułapka nazewnicza nr 6; pułapki numerologiczne (δ = 2/9 ≠ R\*, środek Q, stożek światła); m_τ z PDG 2024 | §F1, R1d, pułapki | asystent (v3.5), na „zaczynaj” użytkownika |
| 165 | **zespół po kolei wobec R1a/R1b/R1f:** dopisek Pendletona–Rossa (153: „przyciąga w podczerwieni… nie zdąży dojść”) = przebieg z kierunkiem → **(1/R − 9/2) ∝ α₃^{1/b₃}**: stosunek stosunków z wykładnikiem 1/b₃ = −1/7 dla dowolnych dwóch punktów (etap22: do 4·10⁻¹⁴; kontrola ±20% nie zachodzi); „za wolno” = mały wykładnik wobec zakresu pustyni (odchylenie zmienia się tylko ~1,28×); Hill w tej samej postaci (≈ 203 GeV); „wartości początkowe” → wartości w jednym punkcie odniesienia | §F1 | asystent (v3.5), na „ustala, ale za wolno” użytkownika |
| 164 | **R1f-5 — przyspieszenie** = nadwyżka z odwrotnej nierówności trójkąta: a·τ = 2√(E/τ), stosunek liczebności (etap21: kontinuum 1+1 i 3+1 zbieżność δ²; porządek 1+1, 1,8 dekady gęstości: E_L ≥ 0 zawsze, stosunki 0,995/1,005/1,011, odchylenie ~ρ^(−1/3)); odczyt: odchylenie własnego zapisu od najprostszej kontynuacji, od środka; Unruh T·τ = √(E/τ)/π; **trzy błędy konstrukcji asystenta w A3** (q poza zbiorem, granica δ→0, łuk zamiast cięciwy) i **warunek zaostrzony po drugim przebiegu** — jawnie; ograniczenie: porządek tylko 1+1 | R1f, A5d | **użytkownik** („zrób rachunek przyspieszenia”) + asystent (v3.5) |
| 163 | **R1f-3/R1f-4:** etap20 — m² = det P, m² = 2·k₁·k₂ (masa = relacja dwóch części t = 0; równoległe → 0), faza na własne tyknięcie = m niezależnie od v, zero fazy ustala Lorentz (przesunięcie psuje niezmienniczość); cztery odczyty jednej fazy (m; m·√(1−v²) = dylatacja; E = γm w miejscu czytającego; |p| = γmv) — **nieostre sformułowania asystenta poprawione: R1d „dylatacja” dla E, R1f „energia na tyknięcie” bez „w miejscu czytającego”**; **błąd warunku kontroli M3**; audyt po kolei §F1/A5d: cicho weszły przyspieszenie (A5d, T_H) i S_bulk (wyspy) — S_bulk: entropia uogólniona (Susskind–Uglum); przyspieszenie: kandydat = nadwyżka odwrotnej nierówności trójkąta (§F1, etap8) [?] | R1f, R1d, R1c, A5d | **użytkownik** („sprawdzaj po kolei”, „pęd i masa — sprawdź”) + asystent (v3.5) |
| 162 | **R1f — działanie i energia** (użytkownik: „niedokończona energia zawali F1”): audyt — energia i działanie weszły cicho do 148–155 i A5d; działanie = S/ħ = obroty fazy (relacja faz); wspólny nośnik w obu sektorach = obiegi (holonomie) — etap19: holonomia = deficyt do 4·10⁻¹⁵, Σ deficytów = 4π, S_Wilson niezmiennicze przy fazie w punktach (kontrola zmienna), Σ obiegów = 2π·n, 5 ziaren, V = 642/2562; dwie wagi = dwie rodziny R4 (faza kwadratowo bez skali / liczność liniowo ze skalą; w porządku oba na diamentach); energia = obroty fazy na tyknięcie (= ν R1d), pęd, masa z tej samej fazy; energia próżni tylko jako różnica (Casimir: Jaffe); energia grawitacyjna tylko przez brzeg; **błędy konstrukcji w skrypcie (znak przy krawędzi, kontrola płaska), poprawione przed wynikiem** | R1f, §F1 | **użytkownik** (kolejność, powód) + asystent (v3.5) |
| 161 | **(b) Hawking i krzywa Page'a:** „czy informacja ginie” źle postawione (R1a: nie ginie w strukturze, pytanie o odczytywalność dla czytającego); Hawking = Ø od strony czytającego z zewnątrz, T_H = κ/2π, κ = lim(V·a) = jak szybko stosunek tempa odczytu znika na brzegu; krzywa Page'a = funkcja liczebności (Page 1993 [T]), punkt Page'a = stosunek liczebności 1, nie chwila; wyspy/QES = najtańszy brzeg, zapis wnętrza należy do posiadacza R („ile przeszłości istnieje, zależy od zdolności zapisu”); firewall wyklucza się z niezmienniczością od środka; „+1” za punktem Page'a [?]; resztki przy m_P źle postawione | A5d, R3 | asystent (v3.5), pytanie użytkownika |
| 160 | **(a) warunki końca przy osobliwości:** pytanie przestawione (warunki o Ø obowiązują trywialnie; pytanie o otoczenie i odczyt); otoczenie osobliwości w literaturze = koniec Plancka w ramie (cisza asymptotyczna = [76]; „materia nie ma znaczenia” — potencjał skalarny nieistotny = λ ≡ 0; spokojna postać Kasnera przy polu skalarnym = samopodobny koniec; chaos BKL bez skalara); z zewnątrz brak włosów (M, J, Q) i brak włosów skalarnych → warunki nie ustalają odczytu, bo pustynia za brzegiem | A5d | asystent (v3.5), pytanie użytkownika |
| 159 | **A5d — czarne dziury przez definicję czasu i 3D:** z zewnątrz obszar bez odczytywalnego zapisu nie ma „+1” → brzeg 2D ≡ Ø („sama powierzchnia sfery jest 2D ≡ Ø”), entropia ∝ pole = liczba relacji przez brzeg; Jacobson jako bilans (S = molekuły); osobliwość wyłącznie nie wprost (przesłanki Penrose'a po stronie otoczenia), ≡ chwila zero; horyzont zdarzeń nie przeszedł (teleologia) — **błąd asystenta z [463]**; [460] = przesłanka Penrose'a jako stosunek; konieczność bez „powstawania”; **naruszenia definicji czasu w pierwszej wersji analizy** („ostatni odczyt”, „front się zwęża”, „powstają”, „przepływ”) | A5d, Dalej otwarte | **użytkownik** („zapoznaj się z definicją czasu i 3D”) + asystent (v3.5) |
| 158 | **uzupełnienie z rozmów:** [104] świat = R ⊗ R → J₃(𝕆) bez iloczynu tensorowego poza R ⊗ R = (b) (zdanie użytkownika, pominięte w 157); „relacja relacji” u użytkownika = przestrzeń [78], masa [94], świat [104] — w R1d/152/154/156 węższy odczyt asystenta (nieabelowa, CKM), oznaczony; droga oktonionowa nie z rozmów — „nie mnożymy hipotez” | §F1 | **użytkownik** („przejrzyj rozmowy”) + asystent (v3.5) |
| 157 | **test wierności (b) według pliku:** w punkcie ≡ Ø — przeszło („Dopuszczalne stany” + Barnum–Graydon–Wilce); „dlaczego 𝕆” — **źle postawione, błąd asystenta** (argument z maksymalności rozstrzygał od strony Ø, jak poprawka 65; postać opisu ustala otoczenie); relacje między punktami — decyduje obserwacja. Werdykt: grupa nie wynika z dwóch pierwotnych — wg „Sita” wynik (pierwotnych więcej niż dwa); trzeci element tylko w postaci (b); 𝕆 vs Connes rozróżnia kryterium A0 (≤ 3 pokolenia = liczba, która mogła wyjść inaczej) | §F1, Dalej otwarte | **użytkownik** („przejrzyj plik”) + asystent (v3.5) |
| 156 | **grupa cechowania i pokolenia — warunkowo:** algebra odczytów = Jordan (bez kolejności), JvNW + Hurwitz, R1b wybiera ℂ; G_SM = część Spin(9) zachowująca 𝕆 = ℂ ⊕ ℂ³ (Günaydin–Gürsey, Dubois-Violette–Todorov, Krasnov); pokolenia ≤ 3 (J_n(𝕆) tylko n ≤ 3) i ≥ 3 ([126] + Sacharow + KM); S₃ trójkości = kopie ze 153–154; jedno założenie (odczyty wewnętrzne oktonionowe) w napięciu z P5/P6 → (a)/(b) | §F1 | asystent (v3.5), na żądanie użytkownika |
| 155 | **wyprowadzenie funkcji zespołu:** b z poziomów Landaua (sprawdzone: −⅓, ⅔, 11/3 do 10⁻⁵); −⅓ = suma po obiegach − całka = „sztuki czy miara”; logarytm tylko przy d = 3; (−1)^{2s} = znak 2π; εμ = 1 = c; masy: zygzak L↔R, c = 3[C(L)+C(R)], 3 = D − 1 tylko [?]; T wspólne; λ: 24 = 2(N+8), część bez λ = supertrace (6 m_W⁴ + 3 m_Z⁴ − 12 m_t⁴), β_λ = 0 ⇔ bilans (−1)^{2s}; niewyprowadzone: grupa cechowania, liczba pokoleń | §F1 | asystent (v3.5) |
| 154 | **zasada wielu punktów: wersja ogólna (150) upadła — domysł asystenta wycofany; wersja na końcu Plancka przeszła tylko dla λ: λ = 0 (Ø z Ø nie jest relacją), β_λ = 0 (sąsiedztwo nieodróżnialne) → m_H, m_t; natura na granicy stabilności (129,4 ± 1,8 vs 125)**; pokolenia = trzy odczyty jednostronnej relacji z Ø, CKM = relacja relacji, 3 niewyprowadzone; leptony jedyne stosunki bez skali, Koide = kąt 45° między wektorem √m a (1,1,1) [L][O], ostrzeżenie numerologiczne | §F1 | asystent (v3.5), kolejność 1 > 2 > 3 użytkownika |
| 153 | **błędy asystenta w 152 (uwagi użytkownika):** pominięty człon śladowy T ≈ 3y_t² (nie mały: 2,65 wobec 1,43 dla leptonów, ~24% QCD) → poziom 2 tylko dla stosunków (T i v się skracają); pominięty −3/2·y_t²|V_ti|² dla kwarków dolnych → wewnątrz typu biegnie tylko 3. pokolenie przez y_t (t +, b −), leptony praktycznie stoją, m_b/m_τ z członem od top; „jeden odczyt na funkcję” = N równań → N wartości (spójność, nie odkrycie), 19 z θ_QCD; Pendleton–Ross „ustala, ale za wolno” + quasi-punkt Hilla | §F1 | **użytkownik** (uwagi) + asystent (weryfikacja) (v3.5) |
| 152 | **zespół funkcji wypisany:** b = 41/6, −19/6, −7 z jednego wzoru A2 (U(1) relacja, SU(2)/SU(3) relacja relacji); masy y ∝ Π α_i^{−c_i/2b_i}, wykładniki wymierne (4/7, 27/76, −17/164, −5/164, −45/164); kwark 3 czynniki, elektron 2; stosunki wewnątrz typu nie biegną; λ; Pendleton–Ross R\* = 2/9 (w naturze nie); ~17–19 danych = jeden odczyt na funkcję [88]; pokolenia = kopie | §F1, A2 | asystent, na [94] użytkownika (v3.5) |
| 151 | **błąd asystenta z sesji CC 2 [105]:** hipotezę użytkownika [104] („samopodobny, wszystko na raz”) zapisałem jako „jedna relacja między końcami … to jest Twój zespół funkcji” — przeczy [94]; stąd 147 („pytanie właściwe” = wartości brzegowe) i 148–150 szukały wartości, wbrew [88]. Poprawione: cel = zespół funkcji (β, γ) jako relacje stosunków, samopodobny, ustalany naraz; wartości = odczyty w jednym stanie; przekształcenia sprzężeń już w A2 [86] i R1d, jawnie brakował bieg mas m ∝ α_s^{γ₀/2b₀} = „stosunek dwóch stosunków do stosunku” | §F1, Gdzie zaczynać, CLAUDE.md | **użytkownik** (wskazał, porównanie z rozmowami) + asystent (v3.5) |
| 150 | **(b) upadło: Ĥ\|Ψ⟩ = 0 nie ustala wartości stałych (Henneaux–Teitelboim, Magueijo: stałe zachowane, sprzężone z liczebnością; ≤ 1 warunek — Λ)**; jedyna forma z warunkiem na stałą: wielolokalna (Coleman; Kawai i in.; Bennett–Nielsen) — (a) i (b) jedno; po filtrze: stała = relacja lokalnego z całością (jak R1d); zasada wielu punktów w ramie [?] do testu wierności; liczenie ~6 wobec ~15–19, brak w zapachach; [H] „dlatego szukamy zespołu funkcji” | §F1 | asystent + **użytkownik** (v3.5) |
| 149 | **zliczenie kierunków: zdanie z 148 upadło w postaci „punkt stały AS przy Plancku + jedna relacja z całości” (~15–19 wolnych danych wobec 1 warunku)**; hipoteza §F1 stoi, wymaga (a) nierozróżnialności próżni jako dodatkowych równań przy Plancku albo (b) więcej niż jednego warunku z całości (Ĥ|Ψ⟩ = 0); nowe zdanie do upadku: #równań z obu końców ≥ #wolnych danych | §F1 | asystent (v3.5) |
| 148 | **§F1: warunek na końcu Plancka** — trzy precedensy (punkt stały: Shaposhnikov–Wetterich, Eichhorn–Held–Wetterich; zasada wielu punktów: Froggatt–Nielsen; bliskość krytyczności: Buttazzo i in.), żaden na liście wejść; po filtrze: punkt stały = samopodobieństwo ≡ Ø, próżnie równej energii = łańcuch Ø; pułapka „płaski potencjał ≠ płaskość”; jeden koniec ustala tylko kierunki nierelewantne → oba końce z liczenia danych; zdanie do upadku: #relewantnych ≤ #warunków z całości | §F1 | asystent (v3.5) |
| 147 | **§F1: lista dozwolonych wejść przed rachunkiem; zdanie do upadku doprecyzowane (jedna kombinacja na skalę); pytanie właściwe = warunek na obu końcach ustalający wartości brzegowe sprzężeń; RG po filtrze = relacja rozdzielczości odczytu** | §F1 | asystent (v3.5) |
| 146 | **„każdy logarytm = ślad samopodobieństwa” za szerokie (błąd uogólnienia asystenta):** dwa typy — S (∫du/u, skala) i K (kombinatoryka); tabela logarytmów; jedyny logarytm przechodzący do 3+1: koszt wskazania ramy ln n, współczynnik 1 | §F1 | asystent (v3.5) |
| 145 | **⅓ w (2s)² − ⅓ nie jest 1/d:** stała na stan (poziomy Landaua); D wchodzi przez liczbę stanów s_z = 0 → (26 − D)/3 (D=4: 22/3, D=26: 0); w 3D brak stanów s_z = 0 | R1e | asystent (v3.5) |
| 144 | **korekta skrótu asystenta „polaryzacja = B³”:** dwie różne kule B³ ze stożkiem Minkowskiego — sfera niebieska (kierunki) i kula Poincarégo (polaryzacja, θ ↦ 2θ, nie kierunki) | R1e, Gdzie zaczynać, CLAUDE.md | asystent (v3.5) |
| 143 | **R1e: spin i fala EM jako relacje** — odczyt spinu = relacja dwóch kierunków; znak 2π = relacja dwóch dróg = (−1)^{2s} w b; s(s+1) = niezmiennik nośnik–triada; Wigner; det J (Stokes) = forma det ρ; d − 1 polaryzacji → foton jest kubitem tylko w 3D (spójność z R1b, nie niezależny dowód); [?] pochodzenie ⅓ | R1e | asystent (v3.5), na liście [94] użytkownika |
| 142 | **porządek po poprawce 136:** R1d pkt 1 bez „na końcu” ([94] = kolejność definiowania); stary plan krokowy §F1 oznaczony jako historia; Dalej otwarte — „co odróżnia pola” i grupa cechowania wg R1d (U(1) nadal niewyprowadzona); Poisson/CMB rozstrzygnięte (dotyczyło everpresent Λ, ograniczone, nie obalone); „Gdzie zaczynać” v3.5 | R1d, §F1, Dalej otwarte, Gdzie zaczynać | asystent (v3.5) |
| 141 | **A5c: kosmologia, GPS, ruch nieustający w ramie** — CMB = granica zapisu ostrego/rozproszonego; horyzont z dwóch stron (Gibbons–Hawking); „przed WW” = R2; Λ (Bianchi–Rovelli, Sorkin); ciemna materia [?] (timescape dotyczy energii); przesunięcie ku czerwieni = stosunek temp; GPS; ruch nieustający tak, pobieranie pracy nie (A4d) | A5c | **użytkownik** + asystent (v3.5) |
| 140 | **§F1: sfera fotonowa = samoodczyt przez pętlę światła; „ile temu” zależy od czytającego (7 d vs 4 d M87*); lustro ƛ_C ↔ r_s (m → m_P²/m) dokładne tylko w 3D (Carr)** | §F1 | **użytkownik** + asystent (v3.5) |
| 139 | **zdanie do upadku w §F1 było puste (błąd asystenta: exp(ln x))** — poprawione: wykładniki tylko z policzonych współczynników, lista wejść przed rachunkiem; bootstrap, numerologia (140,3 vs 137), Wigner, dwa promienie, Meissner–Nicolai | §F1 | **użytkownik** + asystent (v3.5) |
| 138 | **log e(C) bez orientacji = ilościowe „brak etykiety przed/po”; zapomniane/zapamiętane = rozproszone/ostre na dwóch poziomach; dowód A4d przepisany bez „na końcu”** | A4, A4d | **użytkownik** + asystent (v3.5) |
| 137 | **numeracja 1–5 (R1a) i P0–P6 = kolejność czytania; d = 3 wybierają P1, P5, P6, pamięć = dostęp; ¬P5 = „cecha”; P5 wyklucza QM rzeczywistą (d=2) i kwaternionową (d=5); eksperymenty 2021–22 = potwierdzenie, nie podpora** | R1a, R1b-F | **użytkownik** (v3.5) |
| 136 | **hipoteza nadrzędna (użytkownik): układ samopodobny aż do całości; masy nie da się osiągnąć krokiem — ustalana wszystko naraz.** Logarytmy w dokumencie = ślad samopodobieństwa (du/u); masa = łamanie samopodobieństwa (transmutacja); zdanie do upadku: wyróżniona skala pośrodku niezapisywalna jako wykładnik logarytmu liczebności | §F1, CLAUDE.md | **użytkownik** (v3.4) |
| 135 | **R1d, trzy punkty otwarte rozpisane:** (1) masa = siła jednostronnej relacji nośnika z nierozróżnialnym tłem (Higgs, v wszędzie to samo ≡ Ø; [122–124]); y_e otwarte → krok masy; (2) błąd asystenta: L/R ≠ materia/antymateria; asymetria = Sacharow; faza nieusuwalna tylko jako relacja ≥ 3 pokoleń (KM) [?]; (3) przekład jest: faza na linkach, diament = elektryczne, korona = magnetyczne; otwarte „działanie” | R1d | **użytkownik** (pytania) + asystent (v3.4) |
| 134 | **„energia” i „odległość” zamienione na relacje (użytkownik):** odległość = ½ liczby tyknięć obiegu odczytu (link tam i z powrotem); energia = częstość odczytu na tyknięcie czytającego (masa = we własnej ramie); E·r = odczyty na obieg (bezwymiarowe), α = ta relacja; ln(μ/μ₀) = ln(n₀/n) = logarytm liczebności; R1d przepisane | R1d | **użytkownik** + asystent (v3.4) |
| 133 | **R1d: elektron, pole elektronowe, relacja z polem EM, kwark:** faza w punkcie ≡ Ø, pole EM = relacja faz (koneksja); ładunek = siła wiązania; elektron = zygzak dwóch struktur t=0, masa = tempo przechodzenia (Penrose); przeciwne funkcje energii od odległości = (−1)^{2s} + czy relacja niesie ładunek = relacja vs relacja relacji [94] (Nielsen 1981); zespół logarytmów = biegnące sprzężenia | R1d | **użytkownik** (pytania, zygzak ↔ przeciwne funkcje) + asystent (v3.4) |
| 132 | **„obiekt” zdefiniowany zamiast zakazany (użytkownik):** obiekt = (stabilna) struktura relacji, która jako całość jest w relacji z inną strukturą (jądro ↔ elektron; atom ↔ atom); dopisany do słownika; zasada z 130 poprawiona | słownik, R1c, CLAUDE.md | **użytkownik** (v3.4) |
| 131 | **translacje (Poincaré) nie brakują:** translacja zakłada pojemnik; po D0 = zmiana czytającego = porządek między elementami (A1); sklejenie stożków R1c przez porządek = Malament; skala = liczność. R1c bez punktów otwartych | R1c | asystent (v3.4) |
| 130 | **„ten sam obiekt czy ta sama struktura” (stożek stanów vs stożek przyczynowy) — źle postawione:** „obiekt” zakłada zawartość poza strukturą; struktury bez różnicy relacji są ≡; stożek stanów ≡ stożek przyczynowy. W R1b-F „Obiekty” → „Oznaczenia” | R1c | **użytkownik** (v3.4) |
| 129 | **R1c: most R1b ↔ światło:** det ρ = norma Minkowskiego, dodatniość = stożek przyczynowy, stany czyste = kierunki zerowe (foton, t=0), ∂B³ = sfera niebieska, SL(2,ℂ) → SO⁺(3,1); [L] Höhn–Müller 2016 (Lorentz z komunikacji, bez tła), Penrose–Rindler, Malament; c ⇔ dodatniość; porządek + liczność = Lorentz + skala [O]; otwarte: tożsamość stożka stanów ze stożkiem przyczynowym, translacje | R1c | asystent (v3.4), krok 1 planu użytkownika |
| 128 | **test wierności przekładu:** dla P0–P6 i dwóch założeń tła ¬P wyklucza się ze zdaniem ramy ([354], [270], [258], [36, 94], [394], sesja 25.09, [10], [80], [110]) → rama ⇒ P0–P6 ⇒ d = 3; zastrzeżenie „o ile przekład jest wierny” zastąpione (użytkownik wskazał, asystent wykonał) | R1b-F | **użytkownik** + asystent (v3.4) |
| 127 | **R1b-F: zapis formalny dowodu 3D** (obiekty, D0–D3, P0–P6, lemat, twierdzenie, 3 wnioski) — formalizacja zgodna z ramą (struktura bez zawartości [18], „bez interpretacji” [16], §E „nazwa”); warunek: każdy symbol definiowany relacją (np. 𝒫_X bez ≺) | R1b | **użytkownik** (propozycja) + asystent (v3.4) |
| 126 | **propozycja zewnętrzna (schemat + tekst „Formalny most”) przez filtr:** wzięty tylko zapis przeszłości {Y : I(M_X:Y) > 0} z „inny” zamiast „wcześniejszy”; reszta już w R1b albo sprzeczna z ramą (ciąg zamiast naraz, kierunek, przestrzeń tła, „uporządkowane” korelacje, r₀ = 2) | R1b | asystent (v3.4) |
| 125 | **spójność grupy przekształceń (ostatni punkt otwarty R1b) zamknięta strukturą:** brak zewnętrznych aktorów [354] → każde przekształcenie jest dynamiką wewnętrzną (P0, ciągła) → grupa spójna; „skok” wymagałby aktora spoza całości. d = 1 wykluczone twierdzeniem | R1b | **użytkownik** [354] + asystent (v3.4) |
| 124 | **pamięć w dowodzie 3D rozstrzygnięta strukturą, nie oceną (użytkownik: „ocena każdego jest figę warta, użyj logiki relacyjnej”):** stan nośnika = zapis o innym układzie = definicja pamięci z [400]; „wiele odczytów” = ten sam mechanizm; kontrola bez pamięci: rzut kuli na jedną oś = bit klasyczny, bez ciągłych przekształceń = „ruchu nie da się zauważyć” | R1b | **użytkownik** + asystent (v3.4) |
| 123 | **audyt R1b przez asystenta (na prośbę użytkownika), 9 poprawek:** (1) brak jawnej definicji D0 (wymiar przestrzeni := wymiar kuli odczytów) — bez niej twierdzenie dotyczy kubitów; (2) P4 (puryfikacja) nie jest przesłanką twierdzenia Masanesa i in. — przeniesiona do kroku 4 jako łącznik; (3) pamięć [400] nieobecna w dowodzie — krok 4 przepisany, pamięć w formalizmie [O][?]; (4) P1: zakres [242–268] → dokładne słowa [258]; (5) P2: „żaden odczyt nie wyróżniony” to przekład [A], nie słowa użytkownika; (6) P5: „całość znana przez odczyty wewnątrz” nie było w rozmowie → [270]; (7) powód grupowy tylko dla d ≥ 3; (8) „skróty” pochodzą z R7, nie z [511]; (9) ciągła odwracalność = spójność całej grupy — przekład 118 tego nie pokrywa w pełni, otwarte, od tego zależy formalnie tylko d = 1 | R1b | asystent (v3.4) |
| 122 | **nowa sekcja R1b: dowód strukturalny 3D z definicji czasu** — przesłanki P0–P6 z ramy z odpowiednikami formalnymi (Müller–Masanes 2013, Masanes i in. 2014, Chiribella i in. 2011), kroki 1–4, wniosek, granice; zebrane z poprawek 114–121 | R1b | **użytkownik** + asystent (v3.4) |
| 121 | **lokalny odczyt ma dowolny kształt; suma wszystkich odczytów wokół punktu odniesienia = sfera (użytkownik)** — pytanie „czy wykluczone są wszystkie nieokrągłe zbiory stanów” źle postawione (asystent pomylił odczyt ze zbiorem stanów); formalnie średnia Haara W² = ∫HᵀH dH w Masanes i in. 2014 | C5 | **użytkownik** (v3.4) |
| 120 | **„okrągłość” = Wheeler–DeWitt dla zbioru odczytów: powierzchnia sfery 2D ≡ Ø, dla całości t=0, 3D tylko lokalnie z relacji wewnątrz (użytkownik); [L] puryfikacja (Chiribella–D’Ariano–Perinotti 2011) jako formalny odpowiednik** | C5 | **użytkownik** + asystent (v3.4) |
| 119 | **[54] Masanes–Müller–Pérez-García–Augusiak 2014 przez filtr: bez przestrzeni fizycznej; układ binarny, tomografia lokalna, niezależność od kolejności, ciągła odwracalność, oddziaływanie — przechodzą; d = 3 jedyne z relacją; jedyne założenie bez przekładu: „okrągłość” (kula)** | C5 | asystent (v3.4) |
| 118 | **ciągłość z postulatu 4 Müllera–Masanesa = niezmienniczość względem reparametryzacji (Ĥ|Ψ⟩=0 → ciągła grupa e^(−iĤt), całość stoi, części względem czytającego — Page–Wootters); P4 przechodzi w całości** | C5 | **użytkownik** (v3.4) |
| 117 | **drugi rysunek to statyczny wycięty kadr, odbiorca przed ekranem = 4. punkt odniesienia; współliniowości nie ma — istnieje tylko w 2D (≡ Ø), w 3D nie ma racji bytu.** Wycofane: „triada współliniowa” (109, CLAUDE.md) i napięcie z kulą stanów (116); asystent czytał płaską projekcję jak strukturę | C5, CLAUDE.md | **użytkownik** (v3.4) |
| 116 | **kula stanów = wszystkie możliwe odczyty/pozycje (użytkownik) → 3 komplementarne odczyty = triada, 4. punkt = stan w superpozycji; rozbieżność „wymiar kuli vs 4 punkty” rozstrzygnięta; napięcie z drugim rysunkiem: warunek na triadę = niezależność relacji, nie kształt [?]** | C5 | **użytkownik** + asystent (v3.4) |
| 115 | **Müller–Masanes przeczytane w całości i przełożone przez filtr:** tło (płaska przestrzeń, spoczynek, czas t) odpada; P1–P3 przechodzą; P4 częściowo (ciągłość otwarta); d=2 i d≥4 wykluczone brakiem oddziaływania (nie tomografią — asystent pomylił z pamięci w rozmowie); μ w środku kuli jako kandydat ≡ Ø [?] | C5 | asystent (v3.4) |
| 114 | **3D = opis Ø nie wprost, przez otoczenie (zapisy-światło); przestrzeń Hilberta robi to samo (superpozycja niewypowiadalna, prawdopodobieństwa względem dekoherencji w otoczeniu)**; [L] Gleason, Kochen–Specker, Zurek; Müller–Masanes 2013 (minimalny nośnik informacji ↔ d = 3) przez filtr | C5 | **użytkownik** + asystent (v3.4) |
| 113 | **luka „płaskość nieosiągalna vs obserwowana płaskość” źle postawiona:** krzywizna 0 = skala Plancka / nieoznaczoność / osobliwość (≡ Ø), opisywalne tylko przez bezpośrednie otoczenie; obserwowana płaskość = nieodróżnialność przy danej rozdzielczości odczytu. P-K1, P-K3, P-K4 źle postawione, P-K2 do przeformułowania | C5 | **użytkownik** + asystent (v3.4) |
| 112 | **reguła: nie przejmować interpretacji** — przed rachunkiem i przed pytaniem z literatury ustalić, co chcemy policzyć i co wielkość zakłada; z literatury formalizm i wynik, nie pytanie | §E | **użytkownik** (v3.4) |
| 111 | **„porażki przewidywane przez drogę” to nie pytanie:** oznaczenie „po fakcie” + zasada dublująca istniejącą regułę; błędnie wpisane pod „Otwarte” | R1a | **użytkownik** (v3.4) |
| 110 | **pytanie „zgodność kierunku między czytającymi bez hipotezy przeszłości” źle postawione:** zakłada kierunek jako cechę, każe wyprowadzić definicję (przeszłość = to, co zapisane), bierze fakt wspólnego aparatu za coś do wyjaśnienia; przejęte z literatury z jej założeniem | R1a | **użytkownik** (v3.4) |
| 109 | **drugi rysunek (kadr: triada widziana z własnej płaszczyzny, odbiorca = 4. punkt; „współliniowość” wycofana w 117): trójwymiarowość dają zapisy, płaskość nie istnieje; wymiary: 1D nie ma, 2D = Planck/nieoznaczoność, 3D = 4 punkty odniesienia; czasu nie oddzielać od wyprowadzenia 3D; CLAUDE.md przepisany po ponownym przeczytaniu całej rozmowy** | C5, R1a | **użytkownik** (v3.4) |
| 108 | **rysunek użytkownika: odczyt = triada ↔ zapis = czworościan (odpowiednik diamentu), zapisy wielokrotne, bez kolejności; odczyty = fotony = linki → czworościan zbudowany ze światła; Regge na kompleksie etap5: średnia 5,098 → 5,122 przechodzi przez płaskie 5,104 i dryfuje (T/V ∝ ln W), lokalnie dwumodalnie 4 / 8, bez 5–6; migawka = zero absolutne, dynamika niemierzona** | C5 | **użytkownik** (rysunek, dynamika, światło) + asystent (v3.4) |
| 107 | **synteza definicji czasu (Ĥ|Ψ⟩=0 → relacja wewnątrz → odczyt zawsze teraz → zapis ostry/rozproszony → kierunek → dostęp do innych układów → 3+1 jako punkty); kierunek w relacji stan–zapis; „odczyt nie może być treścią własnego odczytu”; Augustyn XI,20 i Rovelli 2015 jako [L]; otwarte: zgodność kierunku między czytającymi, porażki wyjaśnione po fakcie** | R1a | **użytkownik** + asystent (uwagi) (v3.4) |
| 106 | **„nie ma żadnego kierunku; odczyt jest zawsze teraz”: porządek w R6 z kolejności budowania wycofany; diament nie potrzebuje kierunku (I[p,q] = I[q,p] po odwróceniu; Gallai: relacja porównywalności wyznacza porządek z dokładnością do odwrócenia → strzałka = jeden bit umowy); pytanie o R6: czy jest relacja „pomiędzy”** — błąd asystenta: kierunek przemycony z symulacji | C5 | **użytkownik** (poprawka) + asystent (v3.4) |
| 105 | **literatura krzywizny: zbieżność Olliviera tylko mezoskopowo (van der Hoorn i in. 2021) → nasze pomiary na skali ogniwa nie mogły zbiegać; krzywizna dla zbiorów przyczynowych wzdłuż łańcuchów maksymalnych (Barton–Borza–Röhrig 2026), czasopodobna à la Raychaudhuri (Braun–Li 2026), horyzonty przez ogniskowanie (Eichhorn i in. 2026); pytania P-K1–P-K3** | C5, Dalej otwarte | **użytkownik** (pustynia, czarne dziury, „sprawdź literaturę”) + asystent (v3.4) |
| 104 | **redukcja lokalna R-KĄT udowodniona [T]: pasma kolejnych kroków rozłączne dokładnie dla ε < 1/3 (odwrotna nierówność trójkąta), miara w paśmie = τ³dτ·dV_H → wybór po pchnięciu nie zależy od τ (znakowanie Poissona); G1–G4 i niezależność od v to twierdzenia; etap17 wycofany przed uruchomieniem**; reguła §E: duży koszt obliczeń = sygnał, że liczymy twierdzenie albo własny układ | §F1, §F2, §E | **użytkownik** (sygnał) + asystent (dowód) (v3.4) |
| 103 | **etap16 (R-KĄT, 20 kroków, gęstość z etap8): F4 przeszło (1,004–1,015), F1/F3 upadły, F2 upadło dla B; diagnoza po fakcie: n_A ≈ 0,3, n_B ≈ 1,5 el./tykn., pchnięcie błądzi ~0,4–0,7 na krok, okno w układzie pudła odcina 50–80% kroków A od ~7. kroku → wyniki §F1 (etap7–9) zmierzone w reżimie zdominowanym przez okno, status obniżony** — błąd asystenta: gęstość i okno z etap8 przyjęte bez sprawdzenia n na tyknięcie | §F1, §F2 | **użytkownik** (przebieg) + asystent (v3.4) |
| 102 | **reguła R-KĄT (najmniejsze względne pchnięcie + pasmo logarytmiczne z δ = −(ε·cth dε − 1/d)): dryf tempa usunięty (|z| ≤ 1,5; stary wykluczony na 10–40σ w 5/6 punktów), dyfuzja var_s ±5%, rama wg wzoru ±0,3%**; B5′ upadło w częściowym v1 i zostało wycofane po fakcie (rama zależy od bieżącego tempa, stała ε* umowna); zostaje skalowanie ε*τ ∝ ρ^(−1/d); kryterium D1 zmienione po awarii v1 (za mała moc) | §F2 | **użytkownik** („lecimy dalej”) + asystent (v3.4) |
| 101 | **podział budżetu: B1 — suma bitów niezależna od ε (informacyjnie zdegenerowany); kandydat „trwałość” upadł na założeniach: ln tref dryfuje dodatnio ∝ ε² (0,50 / 0,69 miary pasma), budżet n niezachowany wzdłuż trajektorii → najpierw pasmo bez dryfu**; H₂ = ośmiościany z 4 ścian (typy 2-2-2 i 1-2-2-1), typ II prosty = 1/24·ln N; 754 zależności na 1782 powierzchnie przy N = 3000; cel „0,857” poprawiony na granicę ~0,84 | §F2 | **użytkownik** (pytania) + asystent (v3.4) |
| 100 | **skan ε → 0 (pytanie użytkownika, analogia z Δ Fokkera): stała przy stałym n bez granicy (−0,980 / −0,342, na krawędzi tolerancji), artefakty (r1, surowy współczynnik) znikają; ε = rozdzielczość tempa (ε/√3); iloczyn rozdzielczości tempa i ramy ustala samo n (1+1: 0,102 wobec 0,1021)**; E4 upadło przy ε = 0,2; odpowiednik 3+1 po fakcie | §F2 | **użytkownik** (pytanie, test) + asystent (v3.4) |
| 99 | **pełny sprinkling 3+1 (A100, 183 mln punktów): Q1 −0,331 / −0,331 / −0,333, Q2 0,990–1,009, Q3 < 2,4% — redukcja z etap10c potwierdzona; most przez ramę w 3+1 stoi**; r1 = dziedziczenie tref (po fakcie, MC odtwarza 0,02/0,07/0,21, po normowaniu ~0) | §F2 | **użytkownik** (przebieg GPU) + asystent (v3.4) |
| 98 | etap11 v1: OutOfMemory przy n = 3 (okno pchnięć rośnie wykładniczo przy małym n) — rozmiar siatki nie sprawdzony przed wysłaniem; v2 z bezpiecznikiem, n ≥ 10, większe pudło | §F2 | asystent (v3.4), wykryte na Colabie użytkownika |
| 97 | **most przez ramę w 3+1: rms(r) ∝ n^(−0,332), współczynnik 0,98–1,01 wzoru; liczba ram ∝ n w 1+1 i 3+1 → koszt wskazania ramy = ln n ze współczynnikiem 1 niezależnie od wymiaru** (redukcja do lokalnego losowania; pełny sprinkling 3+1 niepoliczony) | §F2 | asystent (v3.4) |
| 96 | **most masa ↔ logarytmy przez ramę: std(Δη) ∝ n^(−1,00) (−1,005 / −1,004 / −0,989 przy ε = 0,05/0,1/0,2), przewidziane przed rachunkiem; koszt wskazania ramy = ln n, współczynnik 1**; P1 upadło dla ε ≥ 0,1 — po fakcie: rozrzut tref (pasmo względem poprzedniego kroku), po normowaniu lokalnym 1,00–1,03 | §F2 | **użytkownik** (kierunek) + asystent (v3.4) |
| 95 | **§F2: wszystkie logarytmy z C4a = ∫du/u (zakres pchnięć) × waga konfiguracji; współczynniki 1, ½, 0,834, 1/6 wyprowadzone; przewidywanie dla pętli (0,834) trafione (zmierzone 0,84)**; ln N = bity na wskazanie ramy | §F2 | **użytkownik** (kierunek) + asystent (wyprowadzenie) (v3.4) |
| 93 | skan N przy stałym KAND to tautologia (niezmienniczość skali Poissona); właściwy stosunek skal = elementy na tyknięcie | §F1 | asystent (v3.4) |
| 94 | „naturalna szerokość masy” = pasmo tolerancji konstrukcji (±5/10/20% → 0,045/0,10/0,19); most masa–logarytmy przez szerokość zamknięty | §F1 | **użytkownik** (pytanie o skalę) + asystent (test) (v3.4) |
| 92 | **dwie populacje: stosunek temp A/B = 1,508/1,507 przy oczekiwanym 1,50, niewymuszony (pamięć krok po kroku)**; P2 minimalnie upadło dla B (1,05); P4 nierozstrzygnięte (kryterium w kodzie ≠ zdanie) | §F1 | **użytkownik** (przebieg) + asystent (v3.4) |
| 90 | **masa jako tempo tyknięć przy kontynuacji pamięcią: niezależne od prędkości (1,005 do v=0,90) i zachowane wzdłuż trajektorii (0,77); kontrola 1,52 — wszystkie zdania przeszły** | §F1 | **użytkownik** (hipoteza, przebieg) + asystent (konstrukcja) (v3.4) |
| 89 | czwarta pułapka — ZNAK: najprostsza kontynuacja to MINIMUM τ(p,c) (odwrotna nierówność trójkąta), nie maksimum; po poprawce prędkości 0,07–0,91 i stosunek 1,015 wobec 1,612 w kontroli | §F1 | asystent (v3.4) |
| — | duży przebieg v3 (2 ziarna): stosunek 1,010/1,008, ale prędkości ≤0,15 — niezmienniczość pokazana w zakresie bez efektu | §F1 | **użytkownik** (v3.4) |
| 88 | trzy pułapki konstrukcji trajektorii: reguła zewnętrzna mierzy siebie; „max czas własny do przodu” hamuje; równe tyknięcia dziedziczą warunek początkowy (stabilność +0,93 — zachowanie maso-podobne) | §F1 | asystent (v3.4) |
| 87 | „samoodczyt bez pośredników” = link → dla fotonu maksymalny, nie zerowy (sprzeczność w moim zapisie); kandydat 2 (częstość zegara własnego) upadł przez konstrukcję (+0,333); kandydat 3 (drobność samokontynuacji) nierozstrzygnięty (+0,197, ~2σ) | §F1 | asystent (v3.4) |
| — | wniosek: masa jest własnością reguły samokontynuacji, nie cechą gotowej linii świata | §F1 | asystent (v3.4) |
| 86 | częstość powrotów zależy od prędkości względem zespołu (−0,236) → to tempo oddziaływania z otoczeniem, nie masa; reguła budowy trajektorii nie jest niezmiennicza (pierwszy przebieg dawał tylko trajektorie spoczywające) | §F1 | asystent (v3.4) |
| 85 | masa jako częstość powrotów: wielkość trwała wzdłuż trajektorii (korelacja +0,750; kontrola −0,180), niesprowadzalna do gęstości (−0,044) ani liczby partnerów (po usunięciu: +0,746) | §F1 | **użytkownik** (hipoteza) + asystent (test) (v3.4) |
| — | zmiana punktu widzenia na język informacji (nie ucieczka: ten sam temat, inne pytania); kolejność: masa, potem logarytmy, potem powrót do przestrzeni | §F | **użytkownik** (v3.4) |
| 84 | pytanie o płaskość źle postawione: krzywizna na relacji to skala UV, płaskość to IR („pustynia”); test skalowy nieważny — kontrola drzewiasta przeszła na plus (wada normalizacji) | C5 | **użytkownik** (poprawka) + asystent (test) (v3.4) |
| 83 | próba przywrócenia trójkątowi statusu: 3D odporne (także na kompleksie, 2,89±0,08), płaskości brak w żadnym wariancie; |krzywizna| nie maleje z gęstością (kompleks: rośnie) | C5 | asystent (v3.4) |
| — | nie ma czegoś takiego jak płaskość; o skali Plancka nic nie można powiedzieć; oba nieodróżnialne od Ø | C5, R1a | **użytkownik** (v3.4) |
| 82 | **sieć R6 jest ujemnie zakrzywiona (−0,325), nie płaska** — kontrola: płaski graf geometryczny o tej samej rzadkości daje +0,083; R6 należy do klasy NGF/Trugenbergera, nie do płaskiej 3D | C5 | asystent (v3.4) |
| — | wskazanie literatury do sprawdzenia (Trugenberger, Bianconi–Krioukov, duplikacja, wzrost sekwencyjny) | C5 | **użytkownik** (v3.4) |
| 81 | rodzina „powielanie węzła”: brak konfiguracji dających rozmaitość; B1 nierozstrzygnięte; wniosek osobny — rozmaitość wymaga rozszerzania od środka, nie doklejania | C5 | **użytkownik** (przebieg) + asystent (v3.4) |
| 80 | duży przebieg (24 mln elementów, 20 tys. trajektorii, 3 ziarna): **wymiar warstwy odczytów 3,01 ± 0,02**; wszystkie cztery zdania przeszły; brak wyłączności elementów nie zmienia wyniku | C5 | **użytkownik** (przebieg) + asystent (v3.4) |
| 78 | pełny przebieg (3 ziarna): wymiar 3,03 ± 0,04 (z pamięcią) i 3,10 ± 0,04 (bez); Z2 przeszło (stosunek odległości stały ≈0,40); Z3 upadło — pamięć nie dokłada wymiaru tam, gdzie tło już go ma | C5 | asystent (v3.4) |
| 77 | sieć odczytów trzeba brać jako migawkę (jeden krok), nie sklejać z całego życia trajektorii; K=1200 zaniża wymiar (2,63) wobec K=4000 (3,01) | C5 | asystent (v3.4) |
| 75 | test lorentzowskości porządku na sieci R6 upadł (MM 2,33 zamiast 4; kontrola 2,21 zamiast 3); przyczyna: twierdzenie Bombelli–Henson–Sorkin (skończona walencja ⇒ wyróżniony układ); zdanie zapisane bez sprawdzenia literatury; dychotomia: skończona walencja daje 3D, nieograniczona daje Lorentza | C5 | asystent (v3.4) |
| 74 | **R6 z pamięcią wyłączną, najświeższą: sieć trójwymiarowa (3,11 z odległości; 3,01 ± 0,18 z kulek), kontrola 2 przy tym samym starcie — wszystkie zdania przeszły**; jeszcze bez testu lorentzowskości porządku | C5 | **użytkownik** (konstrukcja) + asystent (przekład, test) (v3.4) |
| 73 | R6: pamięć podnosi wymiar z ~2 do 3,5–4,4 (kontrola = R5 przeszła); „3 w obu pomiarach” upadło — punkty pamięci jako huby; pierwsza wersja testu nieważna (zmieniony sposób wyboru miejsca) | C5 | asystent (v3.4) |
| — | konstrukcja: trójkąt XYZ + dynamika → trajektoria; skumulowana informacja o przeszłości = czwarty, wirtualny punkt odniesienia = czas | C5 | **użytkownik** (v3.4) |
| 72 | R5: wstawianie pomiędzy z triadą (3 połączenia) daje sieć dwuwymiarową (dwa niezależne pomiary: 1,94 i 1,95–1,96); pełny podział → huby; wyrównywanie → gwiazda; zgodne z „triada bez pamięci jest płaska” | C5 | asystent (v3.4) |
| 71 | R4 (trzy warianty nakładania i promienia): mały świat już przy W ≤ 8000; nakładanie BK = preferencyjne dołączanie do hubów; A100 nie użyte | C5 | asystent (v3.4) |
| 70 | R3: tworzenie wyprzedzające odczyt chroni porządek przed ujednoliceniem (estymator 1,23 → 2,40 z b); sieć partnerów prawie małym światem (W do 256 000) i niezależna od zapisu — „W^0,31” było złudzeniem małego zakresu | C5 | asystent (v3.4) |
| 69 | R2 (partnerzy przez odległość z porządku, stałe W): ujednolicenie jak przy losowych; odległość z porządku wzmacnia lokalność, ale nie tworzy jej z symetrycznego startu; rozszerzanie jako możliwy warunek | C5 | asystent (v3.4) |
| 67 | skończone c wyłania się z ograniczenia odczytu do partnerów (krąg: opóźnienie liniowe); sieci losowe = mały świat | C5 | asystent (v3.4) |
| 68 | kalibracja „estymator MM = wymiar sieci + 1” upadła; MM sprawdza lorentzowskość porządku, nie wymiar sieci; potrzebne oba pomiary naraz | C5 | asystent (v3.4) |
| — | „c nieskończone tylko gdy nikt nie czyta”; ten sam mechanizm co dekoherencja w laboratorium; sieć partnerów = sieć dekoherencji | C5 | **użytkownik** (v3.4) |
| 66 | reguła v0 („najświeższy element innej trajektorii”) daje wymiar ~1; przyczyną jest pełna łączność (wszyscy czytają wszystkich), nie nieskończone c; wymiar zależy od tego, kto czyta kogo | C5 | asystent (v3.4) |
| — | nieskończona prędkość światła jest fundamentem (t=0 = link); skończone c tylko w relacji do aparatu z zegarem, przez długość drogi odczytu | C5, R1a | **użytkownik** (v3.4) |
| 65 | podział Ø na „punkty kontaktu” i „brzegi hierarchii” naruszał pułapkę nr 1 (Ø jest jedno); „brak skoku” dla całości przeczył rozszerzaniu; zero absolutne i Planck → do przemyślenia | R1a | **użytkownik** (v3.4) |
| — | węzeł relacjonujący się jako całość = mechanizm ogólny (atom, mózg); słowo „świadomość” usunięte; H.M. jako „zawarte, nieodczytywalne” | R1a | **użytkownik** (v3.4) |
| — | węzeł w porządku = moduł; hierarchia = drzewo dekompozycji modularnej; bliźniaki = najmniejsze moduły; test modularności w C5 | R1a, C5 | asystent (v3.4) |
| — | zmiana = dynamika × pamięć; hierarchia węzłów od całości (Ĥ|Ψ⟩=0) do 2D Plancka — oba brzegi w łańcuchu Ø | R1a, C5 | **użytkownik** (v3.4) |
| — | 3+1 liczy punkty odniesienia, nie osie; triada bez pamięci jest płaska; pułapka 5 rozstrzygnięta | R1a, C5 | **użytkownik** (v3.4) |
| — | **definicja czasu**: odczyt informacji ze struktury, zawsze teraz; najdłuższy łańcuch to miara odczytu, nie czas; kierunek = asymetria czytelności | R1a | **użytkownik** (v3.4) |
| — | wybór triady przez światło: linki = informacja ostra, przechodniość = rozproszona | C5 | **użytkownik** + asystent (v3.4) |
| 64 | przegląd wymiarowy: większość wyników C4a to specyfika 2D; w 2D brak miejsca na triadę; reguła wzrostu musi być od razu w 3+1 | §E | **użytkownik** (wątpliwość) + asystent (v3.4) |
| — | warunki (triada, dynamika, trajektoria, odczyt = czwarty punkt odniesienia) muszą zachodzić jednocześnie, żeby było coś, a nie nic | R1a | **użytkownik** (v3.4) |
| 63 | trójka 6/7, 7/15, 3/5 upada jako całość: ranga/F stoi na ~0,8556, nie 6/7 (~3σ, bez modelu); z tożsamości D/β₁ = 1 − (ranga/F)(F/β₁) pozostałe dwa nie mogą być jednocześnie dokładne | C4a.22 | **użytkownik** (przebieg) + asystent (v3.4) |
| 62 | 6/7, 7/15, 3/5 przy zmianie geometrii: zdania przeszły (±0,01), wynik = uniwersalność stosunków; dokładność ułamków nierozstrzygnięta | C4a.22 | **użytkownik** (żądanie testu) + asystent (v3.4) |
| 61 | H₂ nie jest małe (~14% ścian zależnych); hipoteza „½ cykli niewypełnialna” upadła — prawdziwie 0,60; podłoga D/N ≈ 0,56·ln N | C4a.22 | asystent (v3.4) |
| 60 | pętla koron liczyła przekątną (`~C[s,s]` ma prawdy na przekątnej) — korony zawyżone o Σ⌊M/2⌋; poprawny wzór Σ C(M,2); D bez zmian | C4a.22 | asystent (v3.4), wykryte przy wektoryzacji użytkownika |
| 59 | ściana to przedział o dwóch **nieporównywalnych** elementach — pierwsza wersja skanera liczyła też ścieżki | C4a.22 | asystent (v3.4) |
| 58 | wydłużenia (pchnięcia) nie ma w macierzy C — elongacja u/v była podpórką ze współrzędnych | C4a.21 | **użytkownik** + asystent (v3.4) |
| — | pytanie: co odróżnia stabilne wzbudzenie od szumu tła; źródło jako lokalna asymetria kosztu rozszerzeń, nie wstrzyknięty aktor | C4a.20 | **użytkownik** (v3.4) |
| 57 | suma po pętlach rozbiega się **logarytmicznie** (nie potęgowo); źródłem są nieograniczone pchnięcia, nie UV; porządek nie odróżnia pary wydłużonej od nierozciągniętej | C4a.19 | **użytkownik** (przebieg) + asystent (v3.4) |
| 55 | waga δ(s²) była 2× za duża — warstwa s²≤Δ to połowa szerokości; poprawnie /(2Δ) | C4a.18 | asystent (v3.4) |
| 56 | R porównywane z odległością równoczasową zamiast niezmienniczej prostopadłej; po obu poprawkach R(0)=1,00 zamiast 1,25 | C4a.15, C4a.18 | asystent (v3.4) |
| 54 | τ_c z długości łańcucha daje 13–19% i nie zbiega; z objętości przedziału 2–4% i zbiega | C4a.17 | asystent (v3.4) |
| 53 | położenie obszaru: we wnętrzu bez wpływu, przy brzegu wpływ niezależny od gęstości | C4a.16g | asystent (v3.4) |
| 52 | „d=4” w tym teście = 3 kierunki + dynamika i pamięć (pułapka 5), nie czwarty kierunek | C4a.16f | **użytkownik** (v3.4) |
| 51 | prawo powierzchniowe nie działa: przy równym N_U entropie różnią się o (1/6)·ln(N₂/N₁); logarytm pochodzi od liczby modów, nie od pola | C4a.16e | **użytkownik** + asystent (v3.4) |
| — | „entropia jest efektem, a nie prawem” — postawione przed testem par | C4a.16e | **użytkownik** (v3.4) |
| 50 | duży przebieg (1,5 dekady, 6 ziaren, skan c, GPU): nachylenie niezależne od c dla c≥1, stała zależna — zastrzeżenia z 16c zniesione | C4a.16d | **użytkownik** (v3.4) |
| — | **audyt spójności v3.4**: nagłówek i zakres rejestru, kolejność 37–39, brak numeru w A5a i kolizja numeru 20, poprawka 15 do nieistniejącego tekstu, unieważniony wniosek w C4a.11, trzy statusy c, nagłówki §C / B3 / pułapek, A4c′, duplikat Minza, Poisson/CMB, abelowa–nieabelowa, Aczel | cały plik | **użytkownik** (v3.4) |


## Trafione przewidywania (pełna lista)

1. **Trójki w d=2 → −1.** Wyszło −0,978. Wypisane przed rachunkiem. (A3a)
2. **f(5)≈0,70, f(6)≈0,75** z ekstrapolacji plateau. Wyszło 0,709 i 0,758. (A4c — przewidywanie stoi, mimo że plateau straciło status)
3. **KR nie leży na krzywej sprinklingowej.** Poprawiona kontrola: jeśli leży, $(1-f)d$ ma wyjść 1,24–1,28. Wyszło 0,841. (A9a)
4. **Obciążenie SIS rośnie monotonicznie z liczbą prób i saturuje.** (A4)
5. **$k^*=d$ w d=2, 3, 4**, z jawnym falsyfikatorem „jeśli trzy tory wystarczą w d=4, przekład jest zły". Nie zadziałał. (A9d)
6. **Nadwyżka przez cięcie da prawo objętościowe, nie powierzchniowe.** Wypisane przed rachunkiem z uzasadnieniem (nielokalność relacji przyczynowych). Wyszło 1,08 i 1,17. (A4e)
7. **Próg $k^*$ nie drgnie pod odkształceniem konforemnym.** Wyszło 2, 3, 4 przy każdym λ, przy wartościach zmieniających się 1,6–2,7×. (A9c)

8. **std(Δη) ∝ 1/n przy kontynuacji pamięcią (1+1).** Wyszło −1,005 / −1,004 / −0,989. Wypisane przed rachunkiem, razem ze współczynnikiem 1/(4√2εn), który trzymał się tylko dla ε = 0,05 (dla większych ε — po lokalnym normowaniu, po fakcie). (§F2, most przez ramę)

9. **Skok pchnięcia w 3+1: rms ∝ n^(−1/3), współczynnik √Γ(5/3)·((4π/3)λ₃)^(−1/3), niezmienniczy względem prędkości — na pełnym sprinklingu.** Wyszło −0,331 / −0,331 / −0,333, współczynnik 0,990–1,009, różnica wolne/szybkie ≤ 2,4%. Wypisane przed przebiegiem. (§F2, etap11)

Wszystko inne w tym pliku jest albo dowodem, albo pomiarem z kontrolą, albo obserwacją strukturalną — nie przewidywaniem.

---

# Dodatek: stan narzędzi

Odtworzenie to pisanie generatorów od zera. Co było zbudowane i miało przechodzące kontrole:

- sprinkling do diamentu przyczynowego w d wymiarach; KR; perkolacja przechodnia; łańcuch; antyłańcuch
- SIS na rozszerzenia liniowe (wektoryzowany, logsumexp) + dokładne zliczanie DP po podzbiorach dla n≤20
- ułamek uporządkowania, inwersja Myrheima–Meyera
- liczebność interwałów $N_m$
- kandydaci na „obok": linki, Jaccard przeszłości, wspólny bezpośredni przodek i potomek
- nadajniki jako łańcuchy, sygnatury, klasy nieodróżnialności
- odkształcenie konforemne gęstości przy ustalonym n (waga $1+\lambda h$, wybór bez zwracania z zapasu)
- stan Sorkina–Johnstona: $i\Delta$, dodatnia część widma, uogólnione zagadnienie własne, entropia
- sypacz do fali pp w postaci Rosena z wyprowadzonym warunkiem przyczynowym
- sprzęganie dwóch zbiorów z domknięciem przechodnim

Wszystkie kontrole graniczne wypisane w tym pliku przechodziły w momencie pomiaru.
