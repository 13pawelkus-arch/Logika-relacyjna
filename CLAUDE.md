# Logika relacyjna — instrukcja dla Claude

Ten plik wczytuje się automatycznie na starcie każdej sesji w tym repo. Jego celem jest to, żeby nie trzeba było tłumaczyć kontekstu od nowa.

## Czym jest projekt

Wspólna praca użytkownika (hotelarz, nie fizyk z zawodu — ale trzyma się bezwzględnie struktury logiki relacyjnej od pierwszego zdania o fałszywości opinii i faktów) z asystentem. Cel: **porządkowanie struktury logicznej fizyki**, nie nowa fizyka. Narzędzia głównie z teorii zbiorów przyczynowych (causal sets): sprinkling, przedziały, linki, stan Sorkina–Johnstona, reguły wzrostu. Od v3.4 zmiana języka opisu na **język informacji** (zapis, odczyt, dostępność) — §F.

**Rozmawiamy po polsku.**

## Pliki

| plik | co to |
|---|---|
| `logika-relacyjna-v3.4.md` | **Główny dokument — czytać najpierw.** Zasady pracy + słownik + wszystkie wyniki, poprawki i otwarte pytania. Aktualizowany i nadpisywany w miarę postępu. |
| `rozmowa/logika-relacyjna-rozmowa.md` | Pełny zapis rozmowy źródłowej z claude.ai (16–24.09.2026, 591 wiadomości). Po kontekst do konkretnego tematu — szukać tu (grep), bo dokument główny **nie zawiera wszystkiego** (uwaga ogólna na początku dokumentu). |
| `skrypty/etap*.py` | Skrypty rachunków, odtworzone z rozmowy (ostatnie wersje). Nazwy zgadzają się z odwołaniami w dokumencie. Duże przebiegi użytkownik puszcza na **Google Colab (A100)**, małe liczy asystent sam. |

## Zasady pracy (skrót — pełne w dokumencie: „Jak czytać”, „Przed liczeniem”, §E)

- **Zasada metody:** nie tworzymy nowych teorii ani nie mnożymy hipotez. Korzystamy z istniejącej nauki, **oczyszczonej z interpretacji** — zostaje to, co mierzalne lub strukturalne; odpada narracja.
- **Najpierw literatura, potem rachunek.** Sprawdzenie kosztuje zapytanie, rachunek kosztuje sesję (koło odkryto już 4 razy).
- **Przed każdym rachunkiem zapisać zdanie, które mogłoby przez niego upaść**, i kontrole graniczne. Rachunek bez tego nie jest rachunkiem.
- **Cztery pola przy każdym wyniku:** wartość · kontrola, która przeszła · co by go obaliło · czyja teza. Liczba bez warunków (n, d, estymator, liczba prób) nie jest wynikiem.
- **Znaczniki:** pochodzenie [H] użytkownik · [A] asystent · [L] literatura; ugruntowanie [T] dowód · [P] rachunek · [O] obserwacja strukturalna · [?] domysł.
- **Wniosek z zakresu węższego niż dekada nie jest wnioskiem.** Każdy parametr ustawiony ręcznie trzeba przeskanować.
- **Poprawki stoją przy wyniku, którego dotyczą**; rejestr poprawek w §E to tylko spis (numerowany — kontynuować numerację).
- **Pułapki nazewnicze** (lista pięciu w dokumencie): Ø jest absolutne — różni je tylko relacja otoczenia; „Ø ma cechę…” to zawsze skrót.
- **Werdykty zostawiać na koniec** — dopóki trwa analiza, nie zamykać tematów przedwcześnie. Ale podsumowania mają być **stanowcze i jednoznaczne** (użytkownik to wytknął).
- **Własne błędy zaznaczać jawnie** w rejestrze (np. „kryterium w kodzie było ostrzejsze niż zdanie zapisane przed rachunkiem”).

## Styl odpowiedzi

- Konkretnie, bez lania wody. Tabela wyników + co przeszło / co upadło / co otwarte.
- **Duży koszt obliczeń = sygnał ostrzegawczy** (użytkownik): przed godzinami GPU sprawdzić, czy to nie twierdzenie do udowodnienia albo koszt własnego pudła/okna.
- **Rachunki dłuższe niż kilka minut na CPU (tu ~pół godziny i więcej) — od razu na GPU (Colab), nie liczyć lokalnie** (użytkownik, 25.09). Lokalnie tylko szybkie sprawdzenie, że kod działa.
- Kod dla Colaba: gotowy do wklejenia, z parametrami na górze, checkpointami, oszczędny w pamięci GPU (A100 40 GB — był OutOfMemory przy dużych macierzach).
- Nie zakładać, że użytkownik zna żargon — skróty myślowe wolno, ale ze słownikiem (tabela na początku dokumentu).

## Gdzie skończyliśmy (24.09.2026)

- **§F1 Masa:** masa jako tempo samoodczytu trajektorii przy kontynuacji pamięcią. Przeszła test niezmienniczości do v≈0,9; dwie populacje (tyknięcie 0,4h i 0,6h) dają stosunek **1,507–1,508** przy oczekiwanym 1,50 (`etap8_masa_populacje.py`). Szerokość masy (~15%) okazała się **artefaktem pasma tolerancji**, nie strukturą (`etap9_masa_skala.py`, poprawki 93–94) → most masa–logarytmy **przez szerokość zamknięty**.
- **§F2 Logarytmy:** wszystkie logarytmy z C4a mają jedno źródło — całkę po pchnięciach (rapidity) = ln N; współczynniki wyprowadzone (linki 1, ściany ½, pętle 6⟨α²⟩=0,834 — przewidywanie zapisane przed rachunkiem przeszło). Logarytm = koszt **wskazania ramy**; w 3+1 zamiast logarytmu potęga.
- **Most masa ↔ logarytmy przez ramę (etap10, 10b, 10c — policzone na CPU):** trajektoria rozróżnia ramy z rozdzielczością δη ∝ n^(−1) w 1+1 i n^(−1/3) w 3+1 (przewidziane przed rachunkiem, przeszło); liczba ram ∝ n w obu → koszt wskazania ramy = ln n, współczynnik 1, **niezależnie od wymiaru**. P1 w 1+1 upadło dla ε ≥ 0,1 — po fakcie: rozrzut tref (poprawka 96). **Pełny sprinkling 3+1 na A100 (etap11 v2) potwierdził redukcję: Q1–Q3 przeszły w 18/18 punktach**; r1 wyjaśnione dziedziczeniem tref (etap11b, po fakcie). Rejestr do 104.
- **Skan ε → 0 (etap12):** ε nie jest regularyzacją (stała bez granicy), ale nie niesie nowej skali: ε = rozdzielczość tempa (ε/√3), a iloczyn rozdzielczości tempa i ramy ustala samo n. Artefakty (r1, surowy współczynnik) znikają przy ε → 0, jak Δ u Fokkera.
- **Podział budżetu (etap13):** informacyjnie zdegenerowany (suma bitów niezależna od ε). Kandydat „trwałość” upadł, bo reguła ma dryf tempa ∝ ε² (tyknięcie się wydłuża; w 3+1 czynnik ~e^1,7 w czasie rozmycia), więc n nie jest zachowane wzdłuż trajektorii.
- **H₂ (etap14):** rozpięte przez ośmiościany z 4 ścian (typy 2-2-2 i 1-2-2-1); typ II prosty = 1/24·ln N wyprowadzony; pełne ranga/F wymaga włączeń–wyłączeń (754 zależności na 1782 powierzchnie przy N = 3000). Cel to granica ~0,84, a nie 0,857.
- **Reguła R-KĄT (etap15):** najmniejsze względne pchnięcie + pasmo logarytmiczne przesunięte o δ = −(ε·cth dε − 1/d) usuwa dryf tempa (D1–D3 przeszły). Podział budżetu: stała ε* jest umowna, zostaje skalowanie ε*τ ∝ ρ^(−1/d).
- **etap16 (R-KĄT, 20 kroków) — F4 przeszło, F1/F3 upadły:** przy gęstości z etap8 (n_A ≈ 0,3, n_B ≈ 1,5 el./tykn.) okno w układzie pudła kształtuje trajektorie od ~7. kroku (etap16b). **Wyniki §F1 z etap7–9 mają obniżony status** (poprawka 103). Redukcja lokalna dla R-KĄT jest **twierdzeniem** (pasma rozłączne dla ε < 1/3, miara τ³dτ·dV_H, znakowanie Poissona). Etap17 wycofany.
- **Następne otwarte:** (1) pasmo o bezwzględnej szerokości ~ℓ [?]; (2) dokończenie rachunku H₂: współczynniki typu I, typu II z dodatkowymi elementami i zależności; czarne dziury (po oczyszczeniu OTW z interpretacji). Pełna lista: „Dalej otwarte” w dokumencie.

## Na koniec każdej sesji

Zaktualizować `logika-relacyjna-v3.4.md` (albo podbić wersję), dopisać poprawki do rejestru, zaktualizować sekcję „Gdzie skończyliśmy” w tym pliku, commit + push.
