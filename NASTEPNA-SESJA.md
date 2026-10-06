# Następny krok: zapytać `z` tym, czym 206 zapytało `a·b`

Krok 5 z listy w `CLAUDE.md`. Nic innego; krok 2 (zliczenie Ø-miejsc) i krok 4 (rura ilościowo) są
otwarte, ale **nie mieszać ich z tym**.

---

## Co jest na stole

Poprzednia sesja (CC 11) wzięła do ramy folder `masa/` — dziewięć kroków, które użytkownik przeszedł
sam 4–5.10. Poprawka **214** ustaliła, gdzie siedzi masa:

```
jądro:    D̂ = Π̸(a_L P_L + a_R P_R) − (b_L P_L + b_R P_R)
mianownik: d_i(z) = z·a_L(z)a_R(z) − b_L(z)b_R(z)
warunek:   z_i = b_L b_R / (a_L a_R)   — oceniane przy z = z_i, czyli SAMOUZGODNIONE
stąd:      (μ_{A,i}/μ_{A,j})² = [b_L b_R]_i/[b_L b_R]_j ÷ [a_L a_R]_i/[a_L a_R]_j
```

Ostatnia linia to **stosunek dwóch stosunków z nazwanymi odczytami** — 181 w pełnej postaci, w już
istniejącym formalizmie. To jest dobre. **Ale `z` wchodzi tam wkładane** — dokładnie w tej roli, w
jakiej `b = −m²V₀` stało w kroku 3, zanim 206 pokazało, że wkładanie nie robi roboty. I każde `p²` w
tych mianownikach przychodzi z areny, a 204 mówi, że arena nie niesie niczego. **Notatki `masa/`
pilnują, żeby rozmiar macierzy nie udawał wymiaru, ale tego pytania nie stawiają.**

---

## Czytać w całości, zanim cokolwiek

- **`### R1b-A`** (4,3 tys. znaków) — forma (i)/(ii) w oryginale. Krótkie, przeczytać dosłownie.
- **blok 206 w `### A11d`** („KROK 3 ZAMKNIĘTY…", 8,3 tys.) — ten sam ruch wykonany raz, razem z
  czterema błędami, które po drodze padły.
- **blok 214 w `### A11d`** („MASA SIEDZI W MIANOWNIKU…", 5,3 tys.) i **213** (4,3 tys.).
- **blok 181 w `### A11d`** (4,0 tys.) — bo tam stoi `ν²` odzyskiwane **dokładnie** ze stosunku dwóch
  odczytów o różnej głębokości, a `z = b_Lb_R/(a_La_R)` **już jest** iloczynem dwóch par wag.

**Nie czytać całego `A11d`** — ma 135 tys. znaków i reguła 195 jest tam już niewykonalna. To jest
znany defekt, nie przeoczenie: sekcja robi dwie roboty (aparat pary (M,O) i odczyty masy) i prosi się
o rozdzielenie. Osobna sprawa, nie ten krok.

---

## Zdanie, które ma upaść

> **`z` nie jest wejściem, jest odczytem — bo da się je odzyskać ze stosunku dwóch odczytów
> o różnej głębokości.**

Rozstrzygnięcia wypisane **z góry**, żeby nie dopasować wniosku po fakcie:

- **(a) Forma (i)/(ii) przechodzi.** Wtedy `z` jest odczytem, a `p²` w mianownikach jest pojemnikiem —
  tak jak `d` w 204. Postać z 214 stoi bez zmian, zmienia się jej **status**: samouzgodnienie nie jest
  wkładaniem, jest zapisem tego, że odczyt jest różnicą własnych stanów O (206).
- **(b) Któryś odczyt się różni i różnicy NIE da się przypisać układowi relacji wewnątrz M.** Wtedy
  pęka forma (i)/(ii) dla tego obiektu — **pierwszy taki przypadek** — i wynik jest o zakresie 204,
  nie o `z`. Byłoby to więcej warte niż sam krok.
- **(c) Pytanie jest źle postawione, bo `z` to nie jeden obiekt.** Biegun i argument funkcji
  `a`, `b` mogą być dwiema rzeczami pod jedną literą. Wtedy krok brzmi: najpierw rozdzielić, potem
  pytać. Precedens: 206 zespoliło dwie różne trójki (199 wobec 181) i tabela to policzyła.

---

## Jak NIE robić — z zapisanych błędów, nie z ostrożności

> **„Trzeba wyrzucać. Bo to że nigdy nie był. Tego śie dowiesz jak podasz strukturalny dowód.
> Cwaniaczku. Wczesniej tego nie powiesz"** (użytkownik, CC 9)

**Kolejność jest częścią wyniku.** Nie zaczynać od „`z` oczywiście jest odczytem, bo wszystko jest
odczytem". To zakłada tezę. Najpierw dowód, potem zdanie.

> **„Albo niosła, albo nie niosła. Dowód ma być strukturalny a nie bajdurzeniem o przykładach"**
> (użytkownik, CC 9)

**Nie wyliczać przypadków.** Lista „oto `z` w hop-stop, oto w propagatorze Diraca, oto w akcji
spektralnej" jest ilustracją. Forma (i)/(ii) jest wyczerpująca — albo przechodzi, albo pęka.

I trzeci, z 211, najświeższy: **sprawdzić, czy przesłanka domysłu jest po dowodzie jeszcze spełniona
przez cokolwiek.** W 201 dowód usunął przesłankę domysłu z 200, a ja zapisałem następnik jako
dowiedziony. Domysł był prawdziwy **pusto** — i dlatego przechodził każdą kontrolę.

---

## Co niepewne

**Czy forma (i)/(ii) stosuje się w ogóle do równania samouzgodnionego.** 204 i 206 przyłożono do
wejść **jawnych** (`C`, `b`): usuń i patrz, czy któryś odczyt się różni. Tutaj `z` stoi po obu
stronach. Czy „usuń `z`" jest wtedy dobrze postawione — **nie wiem**, i to jest pierwsza rzecz do
sprawdzenia, nie do założenia. Jeśli nie jest, krok zmienia się w: podać formę (i)/(ii) dla równania
niejawnego, albo pokazać, że się nie da.

**Czy odczytem jest `z`, czy tylko jego stosunek.** 181 mówi, że **stosunek** dwóch odczytów o różnej
głębokości odzyskuje `ν²` dokładnie. Nie mówi, że każdy czynnik osobno jest odczytem. Możliwe więc, że
ruch jest dostępny wyłącznie dla stosunku, a `z` nigdy nie było właściwym obiektem — i wtedy to jest
odpowiedź (c), nie porażka.

**Czego nie sprawdziłem w literaturze:** czy ktoś zapisał warunek bieguna bez parametru pędu —
po kształcie, nie po nazwie („pole mass without momentum parameter" nic nie da; raczej „self-consistent
… ratio of two … no reference scale").

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
