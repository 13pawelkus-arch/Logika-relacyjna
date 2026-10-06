# Następny krok: przenieść warunek `𝒢` z 212 na `α_i` i `y_f` — albo nazwać przeszkodę

Krok 2 z listy w `CLAUDE.md`, w postaci, jaką mu dała 212. Nic innego; krok 4 (rura ilościowo) i nowe
`[?]` z 221 są otwarte, ale **nie mieszać ich z tym**.

---

## Co jest na stole

212 postawiła **drugi warunek konieczny na zespół** — pierwszy dała 208 (ustalone są tylko
samorelacje). Ten jest innego rodzaju: nie o wartościach, tylko o **wspólnej realizowalności rodziny
funkcji**. Dla jednej koherentnej rodziny znormalizowanych zapisów macierz Grama `Γ_zap` musi być
dodatnia półokreślona, więc oprócz `‖κ_{ij}‖ ≤ 1`:

```
𝒢 = det Γ_zap = 1 − Σ_cykl‖κ_{ij}‖² + 2Re(κ₁₂κ₂₃κ₃₁) ≥ 0
a na granicy wewnętrznej s*:   𝒢(s*) = 0  ⟹  𝒢′(s*) = 0
```

Kontrole 212 (wybrane przed rachunkiem): trójka `9/10, 9/10, −9/10` — każda para dopuszczalna, rodzina
**nie** (`𝒢 = −361/125`); dodatnia `3/5, 9/25, 3/5` → `𝒢 = 256/625`; rodzina `R_3(s) = (e_1+e_2+se_3)/√(2+s²)`
→ `𝒢 = s²/(2+s²)`, `𝒢′ = 4s/(2+s²)²`, oba zero w `s = 0`.

**To jest warunek, który wycina rodziny funkcji, nie wybierając żadnej wartości — bez cięcia, bez
jednostek, bez pojemnika.** Dokładnie ten rodzaj, którego zespół potrzebuje.

**I dokładnie tu 212 się zatrzymała, własnymi słowami (cytat z bloku, nie odsyłacz):**

> „**Zakres, bez którego byłoby to za mocne:** dotyczy **nakładań zapisów w jednym koherentnym
> protokole**. `𝒢 = 0` znaczy liniową zależność zapisów — **nie** jest automatycznie Ø,
> nierozróżnialnością, skalą Plancka ani `λ = 0`; żadnego utożsamienia z 154, 183 ani 208 tu nie
> wykonano. **Przeniesienie warunku na `α_i` albo `y_f` wymaga najpierw wyprowadzenia ich związku z tymi
> nakładaniami, a tego nie ma.**”

Krok to ta ostatnia linijka. Nie „policzyć `𝒢` dla zespołu” — **podać związek odczytów zespołu
z nakładaniami zapisów, albo pokazać, że go nie ma.**

---

## Czytać w całości, zanim cokolwiek

- **blok 212 w `## §F1`** (4,3 tys. znaków, zaczyna się „CO WYMUSZA SAMA STRUKTURA PORÓWNAŃ”) — krótkie,
  przeczytać dosłownie, razem z czterema podpunktami i z kontrolą niewystarczalności na końcu
  (`q_1 = e^{s²}, q_2 = 1, q_3 = e^s`: same tożsamości porównań **nie** wymuszają relacji potęgowej z 152).
- **blok 208 w `### A11d`** — bo tam jest kryterium rodzaju (relacja wobec wielkości) i werdykt
  „ustalone są tylko samorelacje, warunek konieczny a nie wystarczający”.
- **`## §F1` w całości** (92,4 tys. znaków) — tak, w całości; tam stoi zestawienie „STAN ZESPOŁU” (167),
  wypisanie zespołu (152–153), λ na końcu Plancka (154) i 183 o granicach Ø. **Bez tego nie wiadomo,
  do czego warunek miałby się przenieść.**

**Nie czytać `### A11d` w całości** — 135 tys. znaków, reguła 195 jest tam niewykonalna. Znany defekt,
nie przeoczenie: sekcja robi dwie roboty (aparat pary (M, O) i odczyty masy) i prosi się o rozdzielenie.
Osobna sprawa, nie ten krok.

---

## Zdanie, które ma upaść

> **Odczyty zespołu (`α_i`, `y_f`) są nakładaniami zapisów w jednym koherentnym protokole, więc
> `𝒢 ≥ 0` z `𝒢′(s*) = 0` jest warunkiem na zespół.**

Rozstrzygnięcia wypisane **z góry**:

- **(a) Związek da się podać.** Wtedy zespół ma drugi warunek konieczny, który wycina rodziny funkcji —
  i trzeba natychmiast sprawdzić, czego wycina **za dużo**: 212 ostrzega, że `𝒢 = 0` to zależność
  liniowa, a **nie** Ø, więc utożsamienie z 154 albo 183 byłoby tym samym błędem co „2D = Ø” w 206.
- **(b) Związku nie da się podać i przeszkoda jest nazywalna.** Wtedy **przeszkoda jest wynikiem**, nie
  porażką — i prawdopodobnie mówi, czego zespołowi brakuje, żeby być protokołem (np. że odczyty nie są
  jedną koherentną rodziną, bo mierzone są przy różnych rozdzielczościach; patrz 166 i warunek wspólnej
  rozdzielczości). To byłoby więcej warte niż (a).
- **(c) Pytanie źle postawione, bo „zapis” w 212 i „odczyt” w 208 to nie to samo pojęcie.** `Γ_zap`
  jest macierzą Grama **zapisów**, a 19 odczytów zespołu to **stosunki liczności**. Wtedy krok brzmi:
  najpierw powiedzieć, czym jest zapis dla odczytu zespołu, potem pytać. Precedens: 206 zespoliło dwie
  różne trójki pod jedną nazwą i tabela to policzyła; 221 rozdzieliło trzy obiekty pod literą `z`.

---

## Narzędzie zrobione w tej sesji (221) i pułapka, którą po drodze widziałem

221 dało kryterium: **parametr wpisany jawnie = notacja wolnego uchwytu, przypadek (ii) z R1b-A do
pokazania; niejawny punkt stały `x = Φ(x)` = przypadek (ii) już zapisany.** Powód: kandydat C musi
zmieniać się **przy ustalonych relacjach**, a zmiana wartości zadanej przez resztę wyprowadza z definicji
obiektu.

Na tym kroku to narzędzie ma jedno **konkretne** zastosowanie i jedno pozorne.

- **Konkretne:** `s*` w `𝒢(s*) = 0 ⟹ 𝒢′(s*) = 0`. Czy `s*` jest nastawiane, czy produkowane przez samo
  `𝒢`? Jeśli nastawiane — „granica wewnętrzna” jest wkładana i warunek trzeba przełożyć; jeśli
  produkowane — warunek jest odczytem i wolno go używać bez dodatkowej danej.
- **Pozorne, i to jest pułapka:** przesortować 19 odczytów zespołu na „nastawiane / produkowane”.
  **Tego nie robić** — odpowiedź jest trywialnie „wszystkie nastawiane”, bo to jest definicja wolnego
  parametru, i wyszłoby potwierdzanie (191) w nowej notacji. Sprawdziłem to w tej sesji i dlatego tego
  kroku tu nie ma.

---

## Jak NIE robić — z zapisanych błędów, nie z ostrożności

> **„Albo niosła, albo nie niosła. Dowód ma być strukturalny a nie bajdurzeniem o przykładach”**
> (użytkownik, CC 9)

Nie „oto `𝒢` dla trzech Yukaw, oto dla trzech sprzężeń”. Trzy przykłady nie są związkiem; związek albo
jest podany, albo pokazane, że go nie ma.

> **„Nie miałem na myśli tego co piszą w podręczniku w szkole podstawowej. Przeczytaj co na temat
> grawitacji mówi plik główny”** (użytkownik, CC 9)

Zanim szukasz w literaturze macierzy Grama dla sprzężeń — **przeczytaj, co o zapisie mówi plik**: 171
(zapis niesie dokładnie to, co ≡), 174 (wzbudzenie wobec milczenia), 179 (struktura minimalna). Dwa razy
już było tak, że odpowiedź stała w pliku, w sekcji, w której pracowałem.

I trzeci, najświeższy, z 211 i 221: **sprawdzić, czy po dowodzie przesłanka domysłu jest jeszcze
spełniona przez cokolwiek.** W 221 nie była — i dlatego następnika („`z` jest odczytem”) nie wpisano,
choć przeszedłby algebrę i filtr.

---

## Co niepewne

**Czy `α_i` i `y_f` w ogóle mogą być jedną koherentną rodziną.** 166 i 214 mówią, że odczyty A i B
różnią się rozdzielczością, a 221, że wspólna rozdzielczość jest przypadkiem (i) — nie niesie niczego.
Jeśli „jeden koherentny protokół” z 212 wymaga **jednej** rozdzielczości, to związek może nie istnieć
z powodu, który już stoi zapisany, i wtedy to jest (b), nie porażka. **Nie wiem, i to jest pierwsza rzecz
do sprawdzenia, nie do założenia.**

**Czy `κ_{ij}` ma w zespole desygnat.** W 212 `κ` to nakładanie dwóch znormalizowanych zapisów. Co jest
nakładaniem dwóch sprzężeń — nie wiem. Możliwe, że tabela amplitud z 217 (`C(R)` wobec `T(R)` — te same
amplitudy czytane dwa razy) jest tym miejscem, bo tam nakładania **są** jawne: `X_f = Y_f†Y_f = ⟨R_a‖R_b⟩`.
To jest jedyny trop, który widzę, i nie sprawdziłem go.

**Czego nie sprawdziłem w literaturze:** czy ktoś zapisał warunek dodatniej półokreśloności rodziny
jako warunek na zestaw stałych sprzężenia — po kształcie, nie po nazwie („Gram matrix” + „coupling
constants” nic nie da; raczej „positive semidefinite … family … simultaneously realizable”, albo
„determinant vanishes … derivative vanishes … boundary of the physical region”).

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
