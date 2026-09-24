# Logika relacyjna — instrukcja dla Claude

Ten plik wczytuje się automatycznie na starcie każdej sesji w tym repo. Cel: nie tłumaczyć kontekstu od nowa. **Rozmawiamy po polsku.**

## Czym jest projekt

Praca użytkownika (hotelarz, nie fizyk z zawodu, który od pierwszego zdania trzyma się bezwzględnie struktury logiki relacyjnej) z asystentem. **Porządkowanie struktury logicznej fizyki**, nie nowa fizyka: „Nie tworzymy nowych teorii ani nie mnożymy hipotez. Korzystamy z tego, co już jest (cała nauka to solidna baza), oczyszczonego z interpretacji. Zmiana sposobu patrzenia może być równie wielka jak nowe odkrycie.” Narzędzia: teoria zbiorów przyczynowych, stan Sorkina–Johnstona, reguły wzrostu, teoria informacji (§F).

## Pliki

| plik | co to |
|---|---|
| `logika-relacyjna-v3.4.md` | **Główny dokument, czytać najpierw.** Zasady, słownik, wyniki, poprawki (rejestr w §E), otwarte pytania. |
| `rozmowa/logika-relacyjna-rozmowa.md` | Pełny zapis rozmowy źródłowej (16–24.09.2026, 591 wiad.). **Przy każdym temacie pojęciowym czytać wypowiedzi użytkownika stąd (grep), bo dokument główny ich nie zawiera w całości.** Numery wiadomości [n] poniżej odnoszą się do tego pliku. |
| `rozmowa/claude-code-sesja-2026-09-24.md` | Zapis sesji w Claude Code (24–25.09.2026): przeniesienie projektu do repo, etap10–18, twierdzenie o redukcji lokalnej, synteza czasu, rysunki, przepisanie tego pliku. Numery [n] w nawiasach dotyczą tamtej rozmowy tylko wtedy, gdy wyraźnie napisano „sesja CC”. |
| `skrypty/etap*.py` | Skrypty rachunków (etap0–9 odtworzone z rozmowy; etap10–18 z sesji 25.09). |
| `rysunki/` | Rysunki użytkownika: `triada_z_zapisami.png`, `triada_z_zapisami_2.jpg`. |

## FUNDAMENT: rama użytkownika (czytać przed każdym krokiem, nie przeinaczać)

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
- **Rysunki 25.09:** punkty zapisu leżą na trajektoriach, **każdy łączy się naraz z całą triadą** (odczyt = czworościan), jest ich wiele, bez kolejności. Drugi rysunek: triada **współliniowa** (X, Z, Y na prostej), zapisy nad i pod nią: kształt triady nie ma znaczenia, trójwymiarowość dają zapisy. **„To nie znaczy, że płaskość w ogóle istnieje.”** Płaskość ≡ Ø, nieosiągalna [543].
- **Dowód ma być strukturalny** (nie dopuszcza innych przypadków), nie przez przykłady [66, 148].

**Węzły i „obserwator” [404–408]:** jądro atomu to węzeł interakcji; węzeł, który jako całość jest w relacji z innym węzłem, zyskuje punkt odniesienia (patrzy sam na siebie). Słowo „świadomość” do kosza. Henry Molaison: zmieniony aparat odczytu, ten sam mechanizm; przy 100% c i 0 s „przeskok fazowy” = stan nierozróżnialny od osobliwości.

**Kosmologia (hipoteza użytkownika, sam nazywa ją skokiem, nie krokiem [442, 448]):** „naszą” chwilę zero przenieść na krawędź rozszerzającego się wszechświata: z tyłu struktura (otoczenie), z przodu Ø (tam inflacja). **Czarne dziury:** „tam, gdzie tworzenie relacji nie wyprzedziło odczytywania?” [460], ale **najpierw oczyścić OTW z interpretacji** (nie mówi o zapadaniu, krzywiznach ani nieskończonych gęstościach), ujęcie informacyjne [462–466]. Kosmologiczna asymetria materii [126]. „Pomiędzy kwarkami a płaskością jest pustynia” [545]; w czarnej dziurze takie samo Ø w osobliwości i podobna pustynia od horyzontu [547].

## Zasady pracy (pełne w dokumencie: „Jak czytać”, „Przed liczeniem”, §E)

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
- **Zapis rozmowy z Claude Code:** przed końcem każdej sesji zamienić jej transkrypt (`~/.claude/projects/-home-user-Logika-relacyjna/*.jsonl`) na `rozmowa/claude-code-sesja-RRRR-MM-DD.md` (jak w pliku z 24.09) i wypchnąć — w Claude Code nie ma eksportu, a kontener znika po sesji.

## Oś projektu (podsumowanie użytkownika, 25.09.2026)

1. **Definicja czasu i c** (największa zmiana), zawsze razem z 3D.
2. **3D z triady + czwarty punkt (pamięć/zapis/czas)**: niedokończone. R6 z pamięcią wyłączną dał 3,11 / 3,01; krzywizna nie schodziła do zera → pustynia, czarne dziury, „przywrócenie trójkątowi statusu”.
3. **Zespół funkcji logarytmicznych (α, kwarki, elektrony) → masa**: boczna droga podjęta, bo na tym etapie dało się do niej wrócić; potem powrót do 3D.

## Gdzie skończyliśmy (25.09.2026, rejestr do 112)

**Masa i logarytmy (§F1, §F2):**
- Wszystkie logarytmy z C4a = całka po pchnięciach = ln N = **koszt wskazania ramy** (1+1).
- **Most masa ↔ logarytmy przez ramę** (etap10–11): trajektoria o n elementach na tyknięcie rozróżnia ~n ram; koszt wskazania ramy = ln n, współczynnik 1, w 1+1 i 3+1. Pełny sprinkling 3+1 na A100: 18/18.
- **ε = rozdzielczość tempa** (etap12); iloczyn rozdzielczości tempa i ramy ustala samo n; podział „budżetu” jest informacyjnie zdegenerowany (etap13).
- **Reguła R-KĄT** (najmniejsze względne pchnięcie + pasmo logarytmiczne z δ) usuwa dryf tempa (etap15). **Redukcja lokalna R-KĄT to twierdzenie [T]** (pasma rozłączne dla ε < 1/3, miara τ³dτ·dV_H, znakowanie Poissona).
- **Wyniki §F1 z etap7–9 mają obniżony status** (poprawka 103): przy n ≈ 0,3–1,5 elementu na tyknięcie trajektorie kształtowało okno pudła (etap16/16b).
- α w A2 to już logarytm liczebności: 1/α = (2/3πd)·ln(N_Λ/N) → N = N_Λ·e^(−(3πd/2)/α), forma transmutacji wymiarowej [O]; niezbadane.

**H₂ i ranga/F (etap14):** rozpięte przez ośmiościany z 4 ścian (typy 2-2-2 i 1-2-2-1); typ II prosty = 1/24·ln N; granica ~0,84, a nie 0,857; pełne wyprowadzenie wymaga włączeń–wyłączeń.

**Krzywizna i 3D (C5, 25.09):**
- Literatura: krzywizna Olliviera zbiega tylko mezoskopowo (van der Hoorn i in. 2021), więc pomiary na skali ogniwa nie mogły zejść do zera; krzywizna dla zbiorów przyczynowych wzdłuż łańcuchów (Barton–Borza–Röhrig 2026), czasopodobna à la Raychaudhuri (Braun–Li 2026), horyzonty przez ogniskowanie (Eichhorn i in. 2026), molekuły horyzontu ∝ pole.
- Diament nie potrzebuje kierunku (I[p,q] = I[q,p]; Gallai: strzałka = jeden bit umowy).
- Z rysunków: **odczyt = czworościan (triada + zapis)**, odczyty = wzbudzenia = fotony = linki (t=0), więc czworościan jest „zbudowany ze światła”.
- **Regge (etap18):** w sztywnym kompleksie średnia liczba czworościanów wokół krawędzi przechodzi przez płaskie 5,104 i dryfuje jak ln W; lokalnie 4 albo 8, nigdy „pomiędzy”. Sztywny kompleks = zero absolutne (wykluczone); **dynamika niemierzona**.

**Najbliższe kroki:**
1. **3D z czasem razem, na poziomie światła:** jak odczyty-linki (fotony) wokół triady dają 3D i dlaczego nie więcej. Zmierzyć, czy płaskość jako średnia po odczytach (dynamika) zamyka lukę z Regge. Dowód strukturalny, nie przykłady.
2. Czarne dziury po oczyszczeniu OTW z interpretacji (pytania P-K1–P-K3 w C5).
3. α i transmutacja wymiarowa w języku liczebności; dokończenie H₂; pasmo o bezwzględnej szerokości ~ℓ [?].
