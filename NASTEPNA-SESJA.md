# Pierwsza wiadomość do następnej sesji

**Do wklejenia przez użytkownika jako pierwsza wiadomość.** Plik jest nadpisywany na końcu każdej sesji —
nie dopisywać do niego, nie streszczać w nim ramy. Niesie **bieżący krok**, nie framework.

Powód (30.09): start sesji daje ~82 tys. znaków zakazów, mapy i wyprowadzenia czasu/3D, a bieżąca robota
(A11d, 66,5 tys.) nie jest w tym wcale. Ta wiadomość wypełnia tę dziurę. Nie zastępuje plików.

---

**Bierzemy krok 1: stopnie wzbudzenia dla znanego O (174).**

Najpierw `git pull`.

**Przeczytaj `### A11d` w całości** (66 tys. znaków), nie grepem. Tam stoją bloki 169–182 i tam jest
wszystko, co do tego kroku potrzebne.

**Nie czytaj teraz `## R1a` ani `## §F1`** (86 tys. znaków). Ranking nie musi być porównawczy: A11d nazywa
krok 1 otwartą kontynuacją w **pięciu niezależnych miejscach** (170, 174, 179, 180, 186). To argument
absolutny — żeby go obalić, trzeba podważyć te pięć miejsc, a nie pokazać, że gdzie indziej też jest coś
dobrego. §F1 przeczytasz, gdy weźmiemy krok 2; czytane teraz to wejściowy koszt kroku 2 zapłacony dwa razy.

**Czym ta wielkość jest — już ustalone, nie szukać od nowa.** To **D Englerta z 173, ale między
zawartościami, a nie między drogami**: rozróżnialność stanów O przy zawartości M i przy M ≡ Ø. A z 169:
**D = 0 ⇔ entropia względna = 0**. Czyli to jest ta sama wielkość, którą 170 policzyło z O = wszystko
(i dlatego wyszedł ln N), postawiona dla **znanego** O.

**Struktura do liczenia jest gotowa i kompletna:** 179 pkt 5–8 — kubit na każdym linku (nie kopia
w elemencie, zakaz klonowania), element = relacja dwóch nośników, faza na własne tyknięcie, drugi nośnik
zapisujący tyknięcia. 179 mówi wprost, że liczb na niej jeszcze nie liczono.

**Zdanie do upadku — trzy rozstrzygnięcia, każde jest wynikiem.** Uwaga: „zależy od N” znaczy dwie różne
rzeczy i trzeba je rozdzielić **przed** rachunkiem:

- zależy od **|M|** (liczba elementów modułu — własność pary (M, O)) → **wynik o module**, to nie jest pojemnik;
- zależy od czegokolwiek, co **nie jest własnością pary (M, O)** (gęstość, objętość, pudło) → wg [290]
  dosłownie: *„Liczba jest dopuszczalna tylko wtedy, gdy nie rośnie z gęstością. Jeśli rośnie, jest gęstością,
  a nie liczbą, i wymaga miary.”* → **miara, nie sztuki**; odpada jako liczba;
- nie zależy od żadnego z dwóch → **jest liczbą** i można ją podać.

W 170 `ln N` miało N = liczbę wsypanych punktów, czyli wielkość pojemnika. Jeśli tu wyjdzie ∝ log|M|,
to **nie jest to samo zdanie** i nie wolno czytać tego jako powrotu 186.

**Co niepewne, a nie zostało sprawdzone:** czy na strukturze z 179 gałąź „gęstość” w ogóle ma sens — tam nie
ma pudła, więc może być pusta. Jeśli okaże się pusta, zostają dwa rozstrzygnięcia, nie trzy.

**Kolejność dalszych kroków, po korekcie:** krok 3 (a·b dla konkretnych par) stoi **za** krokiem 1 — wymaga
tej samej struktury z 179 plus wybrania pary.

**Przed wpisem do ramy, dwie rzeczy, których czytanie sekcji nie łapie:**
1. Pytanie ze `STOP.md`: **co rama po tym wpisie pozwala albo czego zabrania, czego nie pozwalała przedtem?**
   Brak odpowiedzi = nie ma wpisu.
2. Ścieżka, nie sam wniosek: `python3 narzedzia/wypowiedzi.py 'wzbudzen|milcz' --wymiana --po 3`.
   Bez `--wymiana` szukanie oddaje wniosek, który i tak stoi w pliku.

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
