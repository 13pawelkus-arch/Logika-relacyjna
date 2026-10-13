# Wspólny rachunek A/B w drugim rzędzie wektorowego QED — krok 262

09.10.2026. Kontynuacja 261 na polecenie użytkownika: dokończyć wspólny rachunek, a potem wrócić do uzasadnienia konstrukcji z ramy.

## Zapis przed kontrolami

**Oczekiwanie:** pełny dwupętlowy sektor wektorowego QED składa się z grafów bez zamkniętej pętli fermionowej, jednej fermionowej VP z 261, kontrczłonów i iteracji warunku masowego. Po zgodnym przeliczeniu parametrów powinien dawać jedno przejście między masą biegunową A i masą MS-bar B. W różnicy jednakowo naładowanych kanałów wspólne stałe się skracają, lecz pełna zależność od progów zostaje.

**Warunek upadku rachunku:** po wyrażeniu wszystkich składników w tym samym schemacie różnica indywidualnych pełnych dopasowań nie zgadza się z funkcjonałem VP z 261 plus pozostałym wkładem; albo rozwinięcia przez masy A i B nie są wzajemnie odwrotne do O(α²); albo zależność od wspólnego μ nie znosi się do tego rzędu. Dodatkowa kontrola niezależna: pełna funkcja dwóch mas wobec opublikowanej postaci analitycznej i znanych granic.

**Wejścia i zakres:** ta sama kanoniczna minimalna wektorowa rodzina QED, stan próżni, korelator i regulator co w 257–261; skończony zbiór dodatnich mas Diraca, ładunki i krotności. α jest dopuszczoną daną (253). Wykorzystujemy znane obliczone współczynniki dwupętlowych całek QED; podamy ich źródła oraz oddzielimy je od wykonanego tutaj złożenia, zmiany zmiennych i kontroli. Wynik obejmuje pełne dopasowanie masowe O(α²) w tej rodzinie, bez wkładów słabych, Yukaw, QCD i bez wyprowadzenia wyboru działania z ramy. Czas i 3D pozostają przyjętą podstawą.

**Odczyt:** A = perturbacyjny parametr na powłoce M_i; B = m_i(μ) w MS-bar. Najpierw indywidualne dopasowanie, następnie R_A=M_i/M_j i R_B=m_i/m_j dla jednakowych ładunków. To parametr masowy; pełny eksperymentalny protokół O z 215 nie jest zastępowany przez samą pozycję bieguna.

## 1. Wynik, który domyka krok 261

Niech `a₀=α₀/π`, `r=R_B=m_i/m_j`, `z_f=m_f/m_j`, `c_f=N_{c,f}Q_f²`. Wszystkie masy B są w jednym MS-bar przy tym samym μ. Dla jednakowych zewnętrznych ładunków Q pełne masowe dopasowanie wektorowego QED do drugiego rzędu wynosi

\[
\boxed{\ln\frac{R_A}{R_B}
=\left[-\frac32Q^2a_0+\frac{33}{16}Q^4a_0^2\right]\ln R_B
+\frac{Q^2a_0^2}{12}\sum_f c_f\mathcal H(R_B,z_f)
+O(a_0^3).}
\tag{1}
\]

`H` jest dokładnie pełną funkcją progową z 261. Ostatni składnik jest wcześniej policzoną VP; nowy w złożonym wyniku jest cały pozostały wkład `33Q⁴a₀² ln R_B/16`. Jego współczynnik obejmuje prawidłowe przeliczenie argumentu masy. Stałe dwupętlowe są zachowane w indywidualnym dopasowaniu poniżej i dopiero potem skracają się w tym stosunku.

W notacji średniej odpowiedzi z 261 to samo równanie ma postać

\[
\ln\frac{R_A}{R_B}
=-\frac{3Q^2}{2\pi}\int_{m_j}^{m_i}\frac{dM}{M}\,\bar\alpha_f(M)
+\frac{33Q^4}{16}\left(\frac{\alpha_0}{\pi}\right)^2\ln R_B
+O(\alpha_0^3),
\tag{2}
\]

gdzie `barα_f` zawiera α₀ i jednopętlową zmianę efektywnej α, rozwiniętą do O(α₀²), z pełnym widmem. `M` w tej całce jest zmienną całkowania z 261, nie parametrem μ. Wagi nie zostały dopasowane do mas leptonów.

## 2. Co obejmuje „pełny drugi rząd” w tym kroku

W kanonicznym wektorowym QED do energii własnej O(e⁴) należą dwa fotony na linii zewnętrznego fermionu (graf zagnieżdżony i skrzyżowany), jedna pętla fermionowa w propagatorze fotonu oraz odpowiednie kontrczłony. Wyznaczenie bieguna wymaga ponadto iteracji energii własnej O(e²). Wkład typu `Q_i⁴` pochodzi z części bez zamkniętej pętli fermionowej; `Q_i²c_f` pochodzi z jednej VP. Przy tej samej rodzinie nie ma dodatkowej niezależnej wagi.

Redukcja L/R z 260 zachowuje ten komplet. Dla źródeł w kanale L pełny, znormalizowany korelator można formalnie zapisać

\[
\langle G_{LL}\rangle=
\frac{\int\mathcal Da\,e^{iS_\gamma[a]}
\det F[a]\det S_L[a]\,S_L[a]^{-1}}
{\int\mathcal Da\,e^{iS_\gamma[a]}\det F[a]\det S_L[a]}.
\tag{3}
\]

Regulator, stan i kontrczłony są wspólne. Tożsamości `det K=det F det S_L` i `(K⁻¹)_{LL}=S_L⁻¹` zachodzą dla całej rodziny, więc ich rozwinięcie do czwartego rzędu w sprzężeniu, z dwiema kontrakcjami fotonowymi, zachowuje wszystkie składniki O(e⁴). Przy pracy bezpośrednio w zredukowanym opisie trzeba zachować również wyższe kontakty generowane przez `S_L[a]` oraz rozwinięcie mianownika normalizującego. Równość nie jest założeniem, że jeden z wyznaczników znika. Dla ogólnych końców odczytu obowiązuje ich wspólna redukcja z 260.

Rachunek 262 domyka **perturbacyjne dopasowanie parametru masowego O(α²)**. Pełny pozapowłokowy operator energii własnej, odpowiedź rzeczywistego aparatu oraz sektory słabe, Yukawy i hadronowe SM są szerszymi zadaniami. Dwupętlowa polaryzacja wnosi do efektywnej α zmianę O(α³), więc nie jest potrzebna do masowego O(α²).

## 3. Iteracja warunku masowego

Przy zapisie

\[
G^{-1}(p)=\slashed p[1-\Sigma_V(p^2)]-m[1+\Sigma_S(p^2)]
\]

biegun spełnia `M[1−Σ_V(M²)]=m[1+Σ_S(M²)]`. Zdefiniujmy

\[
\Sigma_V=a v_1+a^2v_2+\cdots,\quad
\Sigma_S=a s_1+a^2s_2+\cdots,\quad
M/m=1+a d_1+a^2d_2+\cdots.
\]

Rozwinięcie w tym samym regulatorze daje, przy argumentach `p²=m²`, 

\[
d_1=v_1+s_1,
\qquad d_2=v_2+s_2+d_1v_1+2m^2d_1(v_1'+s_1').
\tag{4}
\]

Pochodne pochodzą z `M²=m²(1+2ad₁+...)`. Dopiero komplet, z kontrczłonami, daje skończone dopasowanie; nie przypisujemy osobnych skończonych wartości potencjalnie rozbieżnym częściom (4).

Do złożenia używamy opublikowanego, już zrenormalizowanego wyniku `m/M`. Jego odwrócenie wymaga także `L_M=ln(μ²/M²)=L_m−2 ln(M/m)`. Ten ostatni krok zmienia wynik na O(a²). **Nie dodajemy (4) ponownie do opublikowanego dopasowania:** byłoby to podwójne policzenie iteracji. Równanie (4) wyjaśnia jej miejsce w obliczeniu pętlowym, a zmiana `L_M→L_m` tłumaczy już gotowy wynik na zmienne B.

## 4. Indywidualne dopasowanie z pełnymi progami

Ustalmy teraz `a=α_B(μ)/π`, `L_i=ln(μ²/m_i²)`, `z_{fi}=m_f/m_i`. Zamiana mas wewnętrznych A na B w samym składniku O(a²) daje dopiero O(a³), przy ustalonych dodatnich stosunkach.

Znany wynik w zmiennych A ma postać

\[
\frac{m_i(\mu)}{M_i}=1-aQ_i^2 f(L_{A,i})+
a^2\left\{Q_i^4 g(L_{A,i})+
Q_i^2\sum_fc_f\left[-v(z^A_{fi})+\frac{13}{24}L_{A,i}+\frac18 L_{A,i}^2\right]\right\}+O(a^3),
\tag{5}
\]

\[
f(L)=1+\frac34L,\qquad
g(L)=C+\frac{21}{32}L+\frac9{32}L^2,
\]
\[
C=\frac7{128}-\frac{15}{8}\zeta(2)-\frac34\zeta(3)
+3\zeta(2)\ln2.
\tag{6}
\]

Pochodzenie [L]: współczynniki `C_F²` i `C_FT_F` w [Burnier i in., (3.9)](https://arxiv.org/abs/1709.07612), stałe granic w [Melnikov–van Ritbergen, (10)–(11)](https://arxiv.org/abs/hep-ph/9912391). Dla wektorowego QED odpowiadają im `Q_i⁴` oraz `Q_i²c_f`; część nieabelowa `C_FC_A` jest nieobecna. Pełna zależność od drugiej masy jest określona poniżej. Są to obliczone całki znanej teorii, użyte jako wejście [L], nie wyprowadzone z R1a–R1c.

Odwrócenie (5), razem ze zmianą argumentu logarytmu, daje

\[
\boxed{\frac{M_i}{m_i}=1+aQ_i^2 f(L_i)+a^2\left\{
Q_i^4 d(L_i)+Q_i^2\sum_fc_f
\left[v(z_{fi})-\frac{13}{24}L_i-\frac18L_i^2\right]
\right\}+O(a^3),}
\tag{7}
\]
\[
d(L)=f(L)^2-\frac32f(L)-g(L)
=-\frac{71}{128}+\frac{15}{8}\zeta(2)+\frac34\zeta(3)
-3\zeta(2)\ln2-\frac9{32}L+\frac9{32}L^2.
\tag{8}
\]

Składnik `−3f/2` w (8) wynika ze zmiany `L_A→L_B`. Dla logarytmu dopasowania trzeba ponadto odjąć połowę kwadratu pierwszego rzędu:

\[
\boxed{\ln\frac{M_i}{m_i}=aQ_i^2f(L_i)
+a^2\left\{Q_i^4\left[-1-C-\frac{33}{32}L_i\right]
+Q_i^2\sum_fc_f\left[v(z_{fi})-\frac{13}{24}L_i-\frac18L_i^2\right]\right\}+O(a^3).}
\tag{9}
\]

To również pełna postać indywidualna dla nierównych ładunków. W takiej sytuacji nie wolno używać skróconej formuły stosunku (1): należy odjąć dwa wyrażenia (9).

## 5. Funkcja dwóch mas i zgodność z 261

W pełnej postaci analitycznej

\[
v(z)=-\frac{71}{96}-\frac{\zeta(2)}2+\frac13 f_P(z),\qquad z>0,
\tag{10}
\]
\[
\begin{aligned}
f_P(z)={}&\frac32\ln^2z+\frac{\pi^2}{4}
-\frac32z^2\left(\ln z+\frac32\right)\\
&+\frac32(1+z)(1+z^3)
\left[\operatorname{Li}_2(-z)-\frac12\ln^2z+\ln z\ln(1+z)+\frac{\pi^2}{6}\right]\\
&+\frac32(1-z)(1-z^3)
\left[-\operatorname{Li}_2(1-z)-\frac12\ln^2z-\frac{\pi^2}{6}\right].
\end{aligned}
\tag{11}
\]

To [Hoang, dodatek D, (222)](https://arxiv.org/abs/hep-ph/0008102) z przeliczeniem współczynnika tej samej fermionowej VP. Tożsamość `Li₂(z)+ln z ln(1−z)=π²/6−Li₂(1−z)` zachowuje analityczną kontynuację i daje rzeczywistą formę dla każdego dodatniego z, także z>1. Nie odcinamy części funkcji przy z=1. Parametr masy na powłoce w tym sektorze QED jest rzeczywisty; pełna część urojona polaryzacji pozostaje w widmie z 261.

Odniesienie do tamtej całki jest jawne:

\[
\boxed{\mathcal H(r,z)=12[v(z/r)-v(z)]+13\ln r
-6\ln^2r+12\ln r\ln z.}
\tag{12}
\]

Wynika to z odjęcia (9) dla dwóch mas i uzgodnienia tego samego ładunku. W drugą stronę można określić v bez dilogarytmów:

\[
v(z)=\zeta(2)-\frac{143}{96}
+\frac{13}{12}\ln z+\frac12\ln^2z
+\frac1{12}\mathcal H(1/z,1).
\tag{13}
\]

Stała w (13) pochodzi ze znanego równomasowego dopasowania. Sama skończona różnica 261 nie ustala tej wspólnej stałej indywidualnego dopasowania; tutaj została jawnie dostarczona z obliczonego QED. W stosunku jednakowych ładunków znika.

Kontrole granic pełnej funkcji:

\[
v(0)=-\frac{71}{96}-\frac{\pi^2}{12},\qquad
v(1)=\frac{\pi^2}{6}-\frac{143}{96},
\]
\[
v(z)=v(0)+\frac{\pi^2}{4}z+O(z^2),\qquad z\to0^+,
\]
\[
v(z)=\frac12\ln^2z+\frac{13}{12}\ln z+\frac{89}{288}+o(1),
\qquad z\to\infty.
\tag{14}
\]

Przy μ=m_f ostatnia granica zostawia wkład `89/288` do `M_i/m_i`, zgodny z dopasowaniem masy po wyeliminowaniu ciężkiego fermionu w [Grozin, (7.45)](https://arxiv.org/abs/hep-ph/0508242). Dla dwóch jednakowo naładowanych lekkich nośników ta wspólna stała znika, a `H(r,z)→0` przy z→∞. Ciężki kanał ma więc różny status w indywidualnym parametrze MS-bar i w skończonej różnicy z 261. Granice są kontrolą; rachunek używa całego v lub H.

## 6. Jeden schemat sprzężenia i niezależność od μ

Niech `L_f=ln(μ²/m_f²)` oraz `S_Q=Σ_f c_f`. Jak w 261,

\[
a=a_0+\frac{a_0^2}{3}\sum_fc_fL_f+O(a_0^3).
\tag{15}
\]

Dla równych Q odjęcie (9), z (12), daje w MS-bar

\[
\ln\frac{R_A}{R_B}=
\left[-\frac32Q^2a+\frac{33}{16}Q^4a^2\right]\ln r
+\frac{Q^2a^2}{12}\sum_fc_f\left[\mathcal H(r,z_f)+6\ln r L_f\right]
+O(a^3).
\tag{16}
\]

Wstawienie (15) usuwa człon `6 ln r L_f` dokładnie i daje (1). α przy zerowym transferze oraz α MS-bar dają ten sam wynik do policzonego rzędu.

Silniejsza kontrola obejmuje też indywidualne masy, dla dowolnych ładunków. Niezależnie znane równania RG tej samej teorii są

\[
\frac{da}{d\ln\mu}=\frac23S_Qa^2+O(a^3),\qquad
\gamma_i=-\frac{d\ln m_i}{d\ln\mu}
=\frac32Q_i^2a+\left[\frac3{16}Q_i^4-\frac5{12}Q_i^2S_Q\right]a^2+O(a^3).
\tag{17}
\]

Źródło kontroli: [Grozin, (5.58), (5.68)](https://arxiv.org/abs/hep-ph/0508242), po odtworzeniu wag ładunku. Przy różniczkowaniu (9) trzeba użyć `dL_i/dlnμ=2+2γ_i`; pochodna v(z) daje dopiero O(a³). Część `Q_i⁴` daje `9/4−33/16=3/16`, a część `Q_i²c_f` daje `2/3−13/12=−5/12`; współczynniki przy L znoszą się. Otrzymujemy

\[
\frac{d}{d\ln\mu}\ln\frac{M_i}{m_i}=\gamma_i+O(a^3),
\qquad \frac{d\ln M_i}{d\ln\mu}=O(a^3).
\tag{18}
\]

Dla równych Q wspólny bieg mas znosi się także w `R_B` do tego rzędu. To kontrola całego dopasowania, nie tylko samej VP.

## 7. Odwrotne przejście i pułapka pominięcia iteracji

Zdefiniujmy

\[
\mathcal P(r,\{z_f\})=\frac{Q^2}{12}\sum_fc_f\mathcal H(r,z_f).
\]

Równanie (1) to `ln R_A=(1−3Q²a₀/2+33Q⁴a₀²/16)ln R_B+a₀²P_B+O(a₀³)`. Jego odwrotność jest

\[
\boxed{\ln R_B=
\left[1+\frac32Q^2a_0+\frac3{16}Q^4a_0^2\right]\ln R_A
-a_0^2\mathcal P(R_A,\{M_f/M_j\})+O(a_0^3).}
\tag{19}
\]

W składniku drugiego rzędu można już użyć mas A: ich różnica względem B wpływa dopiero na trzeci rząd. Natomiast taka podmiana w składniku pierwszego rzędu wymaga rozwinięcia. Dlatego zapis tego samego `ln(R_A/R_B)` przez `ln R_A` ma współczynnik `−3Q⁴a₀²/16`, podczas gdy zapis przez `ln R_B` ma `+33Q⁴a₀²/16`.

Test błędnego rachunku: odwrócenie (5) przy zamrożeniu `L_A=L_B` usuwa `−3f/2` z (8). Wtedy w zmiennych B wychodzi błędnie `−3/16` zamiast `33/16`; różnica to `9/4` przy `Q⁴a² ln r`. Ten błąd zostaje wykryty zarówno przez kontrolę odwrotności, jak i przez (18).

## 8. Kontrole i pochodzenie wyniku

Skrypt `AB-drugi-rzad-kontrola-2026-10-09.py` i wynik `.json`: **PASS**.

- Dokładne ułamki: odwrócenie logarytmów, `−3f/2`, przejście od `M/m` do jego logarytmu, współczynniki `33/16` i `−3/16`, odwrotność, zmiana schematu α i oba współczynniki γ.
- Osiem porównań całej całki spektralnej H z 261 i niezależnej postaci dilogarytmowej (12), dla progów lekkich, równych i ciężkich: największy błąd bezwzględny **1,40·10⁻¹¹**. Całka obejmuje pełny zakres spektralny.
- Precyzja dziesiętna 70 cyfr: równomasowy punkt, liniowy człon przy lekkiej masie, ciężki limit `89/288`, zamiana stron i składanie różnic. Postać funkcji obejmuje z>1 bez utraty kontynuacji.
- Pięć porównań różnicy indywidualnych dopasowań z pełnym wzorem stosunku, z różnymi ładunkami/krotnościami w pętlach i różnymi μ; także zgodność schematów α.
- Złożenie indywidualnego `B→A→B` dla trzech nośników oraz ewolucja danych według niezależnych RG (17). Po dwukrotnym zmniejszeniu a reszty maleją około ośmiokrotnie: są trzeciego rzędu, zgodnie z zakresem rachunku.
- Kontrola ujemna: pominięcie przeliczenia argumentu masy daje niewłaściwy współczynnik drugiego rzędu.

**Podział pracy:** [L] dostarcza renormalizowane współczynniki dwupętlowych całek i ich funkcję dwóch mas. [T] tutaj: wspólne złożenie z 261, tożsamość (12) w dopasowaniu, przeliczenie A/B, skrócenie wspólnych stałych, schematy i równania kontroli. [P] to wykonane kontrole algebraiczne i numeryczne. Nie wykonano od początku redukcji wszystkich surowych grafów dwupętlowych do całek bazowych ani niezależnego rachunku ich zależności od cechowania; użyto znanego pełnego zrenormalizowanego wyniku tego sektora. Kontrole nie są wyprowadzeniem wejść [L] z ramy.

## 9. Gdzie kończy się zadanie i co dalej

**Domknięte:** wspólny rachunek parametru masowego A/B do O(α²) w zadanym kanonicznym wektorowym QED, z pełnymi dodatnimi progami fermionowymi, iteracją, kontrczłonami zawartymi w dopasowaniu oraz uzgodnieniem α. Stwierdzenia w 261 o brakującym pozostałym wektorowym drugim rzędzie mają teraz historyczny zakres.

**Pozostaje do wyprowadzenia z ramy:** wybór tej rodziny działania/jąder, reprezentacji modów, przygotowania i reguły pętli; wartości mas i ich stosunków. Wagi tego dopasowania nie są dodatkowymi parametrami po przyjęciu teorii, lecz bilans niewyprowadzonych danych z 208 nie zmalał. Współczynnik `3/2` przy pierwszym rzędzie EM nie jest rozwiązaniem osobnego pytania o `3/2` Yukawy. Grupa, liczba pokoleń i [104] zachowują status.

**Zakres szerszego zespołu:** wynik nie jest pełnym dwupętlowym SM. Odpowiedź hadronowa, sektory słabe/Yukawy, mieszane poprawki i pełny protokół O wymagają ich własnych jąder i dopasowania. To nie przeszkadza uznać wybranego tutaj sektora masowego wektorowego QED za ukończony w drugim rzędzie.

**Następny kierunek zgodny z poleceniem użytkownika:** ocenić, czy konkretną konstrukcję używaną w (3)–(17) można uzasadnić relacjami ramy. Warunek testu: podać dokładnie wybraną własność działania i zdanie ramy naruszone przez jej zanegowanie. Dzisiejsze dopasowanie dostarcza określonego celu tej oceny; samo nie jest takim uzasadnieniem.
