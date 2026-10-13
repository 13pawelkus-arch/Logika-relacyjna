# Pochodzenie wagi masowej EM: rachunek i granica wyprowadzenia

09.10.2026. Rozpoczęcie zadania po poleceniu użytkownika: „zacznij od pochodzenia wag”. Punkt wyjścia: §F0, 155 B, 213–214, 217–219, 246–247 i R1b–R1f pliku głównego. Podstawa czasu i 3D jest przyjęta; stosujemy ją do istniejącego rachunku.

## Zapis przed kontrolami rachunkowymi

**Spodziewam się:** znany jednopętlowy współczynnik masowy EM można prześledzić do osobnych kontrakcji członu masowego i kinetycznego oraz do wag po połączeniu propagatorów. Algebra `𝟙, σ` pozwoli zapisać kontrakcje z `𝟙` jako normowaniem, bez czytania go jako czwartego odczytu komplementarnego. Zmiana cechowania powinna zmieniać podział między oba człony, zachowując ich masową kombinację.

**Zdanie o upadku przekładu:** jeśli do uzyskania współczynnika trzeba policzyć normowanie jako czwarty kierunek tego samego rodzaju co odczyty `σ`, pominąć jeden człon propagatora lub dobrać jego wagę do znanej liczby, taki przekład do ramy upada. Zgodność ze znanym wynikiem QED jest kontrolą rachunku, nie nowym testem teorii.

**Osobne, mocniejsze pytanie:** czy wszystkie składniki potrzebne do tego rachunku wynikają z samej podstawy R1a–R1c? Przyjętego działania i reguły pętlowej nie wolno uznać za wyprowadzone tylko dlatego, że algebra licznika ma zapis w ramie.

**Wejścia:** nośnik Diraca jako para L/R, algebra Pauliego i forma determinantowa R1b–R1c, minimalny wektorowy wierzchołek QED, kanoniczne jądra Diraca i Maxwella, standardowa reguła jednej pętli i przesuwalna regularyzacja, schemat MS-bar do porównania z perturbacyjnym parametrem masowym A. Ładunek `Q` i znana pomiarowo `α` są danymi dopuszczonymi przez 253. Nie dodajemy nowych pól ani oddziaływań.

**Odczyt i zakres:** porównanie współczynnika masowego z kinetycznym w tym samym jądrze oraz dwóch opisów A/B przy wspólnym odniesieniu czytającego. Wszystkie argumenty są ilorazami względem tego odniesienia. Parametr na powłoce jest obiektem jednopętlowego rachunku; nie zastępuje pełnego kwantowego protokołu pary z 215 ani dokładnego pojedynczego stanu naładowanego sektora QED. Wynik dotyczy wektorowego wkładu EM, nie całego SM, części hadronowej ani wszystkich wag Yukawy.

## 1. Wynik i jego status

**[A][T][L] przy jawnych wejściach QED:** waga 3 pochodzi z porównania członu masowego i kinetycznego w tym samym jądrze. W cechowaniu Feynmana są to 4 i −1. W dowolnym liniowym cechowaniu kowariantnym są to odpowiednio `3 + ξ` i `−ξ`, więc ich kombinacja jest równa 3. Nie jest to liczba fizycznych polaryzacji ani wniosek z liczenia czasu jako osi.

Kontrakcje licznika można odtworzyć z algebry `𝟙, σ` R1b–R1c na parze L/R. Waga parametru całkowania wynika z kanonicznych propagatorów. Całka po częstości i modach daje wspólny czynnik pętlowy. **Pochodzenie operatorowe zidentyfikowano; wyprowadzenie wszystkich przyjętych składników działania z R1a–R1c pozostaje otwarte.** To rozdzielenie trzech poziomów z 217: algebra, przyporządkowanie działaniu, pochodzenie tego przyporządkowania.

Znany współczynnik nie jest nowym wynikiem fizyki. Zyskiem tej pracy jest usunięcie błędnego uzasadnienia przez `D−1`, wskazanie koniecznych wag oraz wyznaczenie dokładnego miejsca pozostałego wejścia modelowego.

## 2. Zapis bez jednostek i dwa człony jednego jądra

Niech `E_O` oznacza wspólne odniesienie fazowe czytającego. Używamy tylko ilorazów:

$$
P=p/E_O,\quad K=k/E_O,\quad \eta=m/E_O,\quad \chi=q/E_O.
$$

`P⁰` i `K⁰` są częstościami fazowymi w opisie tego czytającego. Indeks 0 nie dodaje czwartego odczytu komplementarnego. `q` jest argumentem wspólnego opisu renormalizowanego; utożsamienie go z argumentem efektywnej α wymaga dopasowania schematów, jak w F0 i 255.

W wektorowym przypadku EM obie chiralności mają ten sam ładunek. W cechowaniu kowariantnym piszemy

$$
\widehat\Sigma(P)=a(P^2)\slashed P+b(P^2)\eta\mathbb1_4,
\qquad
\widehat{\mathcal D}(P)=(1-a)\slashed P-(1+b)\eta\mathbb1_4.
$$

Znormalizowany parametr masowy jest więc proporcjonalny do

$$
\eta\frac{1+b}{1-a}
=\eta[1+a+b]+O(\alpha^2).
$$

Waga masowa zawiera **oba** człony. W tym EM przypadku równość lewego i prawego wkładu wynika z wektorowego działania; nie zakładamy jej dla słabego sektora chiralnego. Samo `b` nie jest poprawką do odczytu masy po uwzględnieniu normalizacji kinetycznej. `a,b` tutaj nie są skokiem i zatrzymaniem z hop-stop ani efektami pomiarowymi z 213.

## 3. Kontrakcje z algebry Pauliego

Z R1b mamy

$$
\sigma_i\sigma_j=\delta_{ij}\mathbb1_2+i\epsilon_{ijk}\sigma_k,
\qquad
\sum_i\sigma_i A\sigma_i=2\operatorname{tr}(A)\mathbb1_2-A.
$$

Drugą tożsamość wystarczy sprawdzić na bazie `𝟙, σ₁, σ₂, σ₃`; liniowość daje ją dla każdej macierzy 2×2. Na części skalarnej ma wagę 3, na bezśladowej −1.

Dla przyjętej pary L/R budujemy macierze amplitud Diraca:

$$
\Gamma^0=\begin{pmatrix}0&\mathbb1_2\\\mathbb1_2&0\end{pmatrix},
\qquad
\Gamma^i=\begin{pmatrix}0&\sigma_i\\-\sigma_i&0\end{pmatrix},
\qquad
\slashed K=\Gamma^0 K^0-\Gamma^iK_i.
$$

`Γ⁰` jest zbudowana z bloków `𝟙₂`, lecz **nie jest `𝟙₄`**. Te macierze działają na amplitudach pary L/R; nie są czterema efektami pomiarowymi jednego nośnika. Ich rozmiar także nie jest liczbą osi przestrzennych. Znak kontrakcji jest formą determinantową R1c.

Zdefiniujmy

$$
\mathcal C(A)=\Gamma^0A\Gamma^0-\sum_i\Gamma^iA\Gamma^i.
$$

Wprost z bloków i tożsamości Pauliego:

$$
\mathcal C(\eta\mathbb1_4)=4\eta\mathbb1_4,
\qquad \mathcal C(\slashed K)=-2\slashed K.
$$

Dla drugiej równości bloki `B=K⁰𝟙+K·σ` i `A=K⁰𝟙−K·σ` dają `B−Σσ_iBσ_i=−2A` oraz `A−Σσ_iAσ_i=−2B`. Kontrakcja skalarna obejmuje blok jednostkowy oraz kontrakcję triady, z odpowiednimi znakami. **Nie dodaliśmy czwartej macierzy Pauliego.** Zmiana triady przez wspólne `U∈SU(2)` nie zmienia tych tożsamości.

W fizycznym liczniku jednopętlowym otrzymujemy zatem

$$
\mathcal C(\slashed P-\slashed K+\eta)
=-2(\slashed P-\slashed K)+4\eta.
$$

Przyporządkowanie tego licznika minimalnemu wierzchołkowi EM jest przyjętym składnikiem QED. Tożsamości macierzowe same nie wybierają działania.

## 4. Skąd waga x i wspólny czynnik pętli

Kanoniczne mianowniki to `A=K²+i0` oraz `B=(P−K)²−η²+i0`. Dokładnie

$$
\frac1{AB}=\int_0^1\frac{dx}{[xA+(1-x)B]^2}.
$$

To tożsamość całkowa, także przy `A=B`. Nie wybrano swobodnej wagi: zastąpienie `dx` przez dowolne `w(x)dx` zmieniłoby produkt propagatorów. Po przesunięciu `L=K−(1−x)P`:

$$
\Delta_x=(1-x)\eta^2-x(1-x)P^2,
\qquad
N=-2x\slashed P+2\slashed L+4\eta.
$$

Nieparzysty człon w `L` znosi się przy przesuwalnej regularyzacji; nie zerujemy przez to żadnego propagatora. Mianownik `L²−Δ_x+i0` pozostaje. Na tym etapie wagi członów to **`−2x` i `4`**.

Wspólny czynnik można uzyskać z całkowicie skończonej różnicy, bez obrotu Wicka. Dla dodatnich bezwymiarowych `d₁,d₂`:

$$
J(d_1,d_2)=-i\int\frac{d\omega\,d^3\ell}{(2\pi)^4}
\left[\frac1{(\omega^2-|\ell|^2-d_1+i0)^2}
-\frac1{(\omega^2-|\ell|^2-d_2+i0)^2}\right].
$$

Całka po częstości, przez bieguny jądra, daje `1/[4(|ℓ|²+d)^{3/2}]`. Po sumowaniu kierunków i całce radialnej:

$$
J=\frac1{8\pi^2}\int_0^\infty dl\,l^2
\left[(l^2+d_1)^{-3/2}-(l^2+d_2)^{-3/2}\right]
=\frac1{16\pi^2}\ln\frac{d_2}{d_1}.
$$

Ostatnią równość daje pierwotna `arsinh(l/√d)−l/√(l²+d)`. Regularyzowane osobne całki nie są użyte jako odczyty; różnica jest skończona. `ω` jest argumentem spektralnym propagatora, nie dodatkową osią tego samego rodzaju co trzy odczyty przestrzenne. Miara sumy po modach i normalizacja `2π` są tutaj składnikami przyjętej reprezentacji QED. Dwa wierzchołki dają `e²Q²`, więc cały czynnik to `αQ²/(4π)`.

Zmiana wspólnego argumentu odjęcia daje z tych samych jąder

$$
\widehat\Sigma_F(P;\chi_1)-\widehat\Sigma_F(P;\chi_2)
=\frac{\alpha Q^2}{4\pi}(-\slashed P+4\eta)
\ln\frac{\chi_1^2}{\chi_2^2}+O(\alpha^2).
$$

`α` w jednym punkcie wystarcza do współczynnika w tym rzędzie: jej zmiana w tej jednopętlowej różnicy wnosi wyższy rząd. Nie zastępujemy tym całej funkcji α w innych zadaniach.

## 5. Trójka i kontrola dowolnego cechowania

W cechowaniu Feynmana:

$$
\int_0^1(-2x)dx=-1,
\qquad \int_0^1 4dx=4,
\qquad a_{\log}+b_{\log}=4-1=3.
$$

Trójka jest wagą **po normalizacji masy przez człon kinetyczny**. Pominięcie kinetyki daje 4. Pół pochodzi z parametryzacji propagatorów; nie z dopasowania do wartości współczynnika.

Teraz pozostawmy dowolny parametr `ξ`, z propagatorem proporcjonalnym do

$$
\frac{g_{\mu\nu}-(1-\xi)K_\mu K_\nu/K^2}{K^2+i0},
\qquad \xi=1\text{ — Feynman},\quad \xi=0\text{ — Landau}.
$$

Podłużny licznik spełnia

$$
\frac{\slashed K(\slashed P-\slashed K+\eta)\slashed K}{K^2}
=\frac{2K\!\cdot\!P}{K^2}\slashed K-\slashed P-\slashed K+\eta.
$$

Przy wydzielaniu współczynnika logarytmicznego rozwinięcie mianownika ma człon `2K·P/K²`. Jego iloczyn z `−K̸` znosi pierwszy człon powyżej. Zostaje `−P̸+η` przy tym samym logarytmie. Nie użyto tu śladu rzutnika „na trzy kierunki poza pędem”. Stąd:

$$
a_{\log}(\xi)=-1+(1-\xi)=-\xi,
\qquad
b_{\log}(\xi)=4-(1-\xi)=3+\xi,
\qquad a_{\log}+b_{\log}=3.
$$

To dowód dla całego parametru, nie próbek jego wartości. W Landau samo `b` ma wagę 3, bo logarytmiczny wkład kinetyczny jest zero. Odczyt tej szczególnej postaci jako liczby kierunków nie wyjaśnia niezmiennej kombinacji ogólnej.

Pełny licznik zmiany cechowania ma też tożsamość Wardowską. Przy `X=P̸−η`, `Y=P̸−K̸−η`, `S=Y⁻¹`:

$$
\slashed K S\slashed K=X S X-X-\slashed K.
$$

Na zewnętrznych spinorach na powłoce składniki z `X` nie przesuwają perturbacyjnego parametru masowego; nieparzysty składnik znosi się w całce. **Poza powłoką odpowiedź podłużna pozostaje.** Nie wyciągamy z tego wniosku o residuum ani pełnej fazie pary. Nie wolno również skasować osobnej całki bez skali, zlewając jej część UV z IR; tożsamość dotyczy wspólnie regularyzowanego wyrażenia.

Kontrola względem literatury: [Grozin, arXiv:hep-ph/0508242](https://arxiv.org/abs/hep-ph/0508242), §3.8, równania (3.98)–(3.107). Parametr `a` tej pracy jest naszym `ξ`; ich `ξ` w (3.101) ma inną konwencję. Użyto znanego działania i współczynników do kontroli, nie interpretacji czasu autora.

## 6. Zapis kulombowski: dwie polaryzacje nie dają samej trójki

Propagator kulombowski rozdziela odpowiedź wynikającą z więzu Gaussa oraz poprzeczną:

$$
D_{00}\ \propto\ |K|^{-2},\qquad
D_{ij}\ \propto\ \frac{\delta_{ij}-K_iK_j/|K|^2}{K^2+i0}.
$$

Część kulombowska nie jest trzecią polaryzacją fotonu. Drugi licznik zawiera oba stany poprzeczne. Dla rachunku można go rozdzielić na część `δ_ij` (Gaunt) i **odejmowany rzut przestrzenny** `K_iK_j/|K|²`; obu trzeba użyć z pełnymi mianownikami.

Po wyjęciu wspólnego `αQ²/(4π)` oraz wspólnego logarytmu/pola UV otrzymujemy:

| część | przy `Γ⁰P⁰` | przy `Γ·P` | przy `η` | kombinacja masowa we własnej ramie |
|---|---:|---:|---:|---:|
| kulombowska | 0 | 4/3 | 2 | 2 |
| Gaunt | −3/2 | 1/2 | 3 | 3/2 |
| odejmowany rzut przestrzenny | 1/2 | −5/6 | −1 | −1/2 |
| razem | −1 | 1 | 4 | 3 |

To wagi po całkowaniu, nie liczby osi. Dla części kulombowskiej `2=∫₀¹dy/√y`, `4/3=∫₀¹(1−y)dy/√y`. W części Gaunta czynnik `∫₀¹(1−x)dx=1/2` daje dwie wagi kinetyczne. W rzucie: `−∫₀¹(1+x)dx+∫₀¹√y dy=−5/6` oraz `∫₀¹(1−x)dx=1/2`. Wagi masowe 3 i −1 pochodzą z kontrakcji odpowiednich liczników. Pominięcie rzutu daje we własnej ramie `7/2` zamiast 3.

Tabela daje `−P̸+4η`, również poza własną ramą: przy `P²=η²` jego projekcja masowa ma wagę 3. Dwie polaryzacje wraz ze swoim propagatorem dają we własnej ramie wagę 1, część kulombowska wagę 2. Nie odczytujemy tego sumowania jako konstrukcji 3D.

Źródło i kontrola jąder: [Lindgren, arXiv:1107.4669](https://arxiv.org/abs/1107.4669), równania (2), (8), (11), (16). Jego regulator `ε_L` spełnia `ε_L=2ε` naszej konwencji; wspólne pole UV jest to samo. W tabeli wydzielono wyłącznie współczynnik logarytmiczny. Pełną funkcję zachowuje podany w źródle operator, nie sama tabela.

Sprawdzono także skończoną projekcję **całego** masowo odjętego operatora (16), zamiast zakładać znikanie pozostałych części. Przy `s=|P|²/η²`, na powłoce, sprowadza się ona do

$$
\frac43s-(1+s)\mathcal J_0(s)+3s\mathcal J_2(s),
\quad
\mathcal J_0=2\int_0^1du\ln[1+s(1-u^2)],
\quad
\mathcal J_2=2\int_0^1du\,u^2\ln[1+s(1-u^2)].
$$

Dla `X(u)=1+s(1−u²)` pochodna `d[uX]/du=1+s−3su²`. Całkowanie przez części daje dokładnie `(1+s)𝒥₀−3s𝒥₂=4s/3`. Projekcja więc znika dla każdego `s≥0`, z zachowanymi wagami. Sam operator poza powłoką nie znika. Jest to kontrola zgodności dwóch cechowań przy przyjętym odjęciu masowym.

## 7. Zachowana pełna funkcja i skończona stała MS-bar

Współczynnik logarytmiczny nie uprawnia do zastąpienia całej funkcji samym logarytmem. W MS-bar pełny jednopętlowy wkład w cechowaniu Feynmana ma postać

$$
\widehat\Sigma_F^{\overline{\rm MS}}(P;\chi)=\frac{\alpha Q^2}{4\pi}
\int_0^1dx\left[
(-2x\slashed P+4\eta)\ln\frac{\chi^2}{\Delta_x-i0}
+2x\slashed P-2\eta\right].
$$

Mianownik progowy i część urojona pozostają. Ostatni człon pochodzi z części licznika zanikającej z regulatorem, pomnożonej przez jego biegun: w standardowej kontynuacji `ε` licznika daje `2ε(xP̸−η)`. Kontynuacja jest narzędziem schematu, nie nowym wymiarem ramy. Przy odjęciu bez tej części otrzymalibyśmy inny skończony schemat i potrzebowalibyśmy odpowiedniego dopasowania.

Na powłoce `Δ_x=(1−x)²η²`. Po projekcji:

$$
\frac{\delta\eta_A}{\eta_B}
=\frac{\alpha Q^2}{4\pi}
\left[3\ln\frac{\chi^2}{\eta_B^2}+4\right]+O(\alpha^2).
$$

Stała 4 ma inne pochodzenie niż wcześniejsza waga 4 w liczniku:

$$
-2\int_0^1(4-2x)\ln(1-x)dx=5,
\qquad \int_0^1(2x-2)dx=-1,
\qquad 5-1=4.
$$

Właśnie dlatego nie wolno zatrzymać fizycznego licznika przed dopasowaniem skończonego schematu i ogłosić stałej 5 jako wyniku MS-bar. Zgodność z 214 zachowana. Dla dwóch kanałów o tym samym ładunku EM stała 4 oraz jawny wspólny argument skracają się w różnicy; wagi progowe innych sektorów nie znikają przez ten fakt.

## 8. Co to daje funkcji masy i stosunkom współczynników

Nie zmieniając odczytu A przy zmianie wspólnego opisu B, z poprzedniego wzoru otrzymujemy, przy `t=ln(χ/χ₀)`:

$$
\frac{d\ln\eta_B}{dt}=-\frac{3Q^2}{2\pi}\alpha(t)+O(\alpha^2),
\qquad \gamma_m=\frac{6Q^2\alpha}{4\pi}+O(\alpha^2).
$$

Czynnik 2 pomiędzy wagą logarytmu i współczynnikiem biegu jest pochodną `ln χ²` po `ln χ`. Nie jest dodatkowym zliczeniem stanów. Zapis ma argument stosunku obiegów czytającego, nie upływu zewnętrznego czasu.

W zadanym zakresie jednej pętli QED, z ustalonym zbiorem aktywnych fermionów i bez przejścia przez progi:

$$
\frac{d\alpha}{dt}=\frac{2S_Q}{3\pi}\alpha^2,
\qquad S_Q=\sum_fN_cQ_f^2,
\qquad
\frac{d\ln\eta_f}{d\ln\alpha}=-\frac{9Q_f^2}{4S_Q}.
$$

Stąd

$$
\frac{\eta_f(t_2)}{\eta_f(t_1)}
=\left[\frac{\alpha(t_2)}{\alpha(t_1)}\right]^{-9Q_f^2/(4S_Q)}
$$

w tym nazwanym sektorze i rzędzie. Wykładnik jest stosunkiem dwóch policzonych współczynników: biegu masy i sprzężenia. Dla porównania dwóch kanałów różnicujemy wykładniki; przy tym samym ładunku wspólna część EM znosi się. Wartość stosunku mas w jednym odczycie nadal nie jest wybrana. Granice z 219 i 254 pozostają: zawartość pól jest wejściem, próg zmienia zakres, wyższe rzędy zmieniają postać.

Dla jednopętlowego wektorowego wkładu QCD ta sama kontrakcja spinorowa ma czynnik `C_R` zamiast `Q²` i daje `γ_m=6C_Rα_s/(4π)`. To warunkowe podstawienie przy zadanej reprezentacji; nie wyprowadzenie SU(3). Nie rozszerzamy go na wszystkie chiralne współczynniki Yukawy, dla których trzeba zachować także pozostałe propagatory i wierzchołki. Czynnik `3/2` z 217–218 pozostaje osobnym zadaniem.

## 9. Bilans pochodzenia i następny krok

| składnik | co zostało wykazane | co pozostaje wejściem |
|---|---|---|
| kontrakcje 4 i −2 | wynik algebry bloków `𝟙, σ`, niezależny od triady | przyporządkowanie parze L/R i minimalnemu prądowi Diraca |
| waga x i jej całka 1/2 | wymuszona przez tożsamość produktu propagatorów | kanoniczne jądra i reguła sumowania jednej pętli |
| kombinacja masowa 3 | wynik normalizacji kinetycznej; niezmienna przy zmianie cechowania | przyjęte działanie QED oraz zakres perturbacyjny |
| czynnik αQ²/(4π) | dwa wierzchołki i skończona całka po częstości/modach | normalizacja i miara przyjętej reprezentacji, Q i α |
| wykładnik względem α | eliminacja wspólnego argumentu z dwóch funkcji | aktywne nośniki, schemat i zakres bez progów |

**Werdykt:** przekład kontrakcji do `𝟙, σ` przeszedł warunkowo. Nie potrzebuje odczytu czasu jako osi. Mocniejszego zdania o wyprowadzeniu całego działania i reguły pętlowej z samej podstawy nie uzyskano; powtórne obliczenie znanej liczby nie zamyka tego pytania. W 155 B można zastąpić „pochodzenie nieznane” opisem powyższych operacji, zachowując „z samej ramy niewyprowadzone”. Bilans 208 i hipoteza [104] bez zmiany.

**Najbliższa luka w tym kierunku:** uzasadnienie przyporządkowania jawnych jąder i wag działaniu z relacji ramy. Osobny kolejny rachunek jednopętlowy: prześledzić `3/2` z 217 przez wszystkie wymagane propagatory i poprawkę wierzchołka. Pełny drugi rząd EM oraz kompletny protokół odczytu A nadal są osobnymi, niewykonanymi zadaniami.

## 10. Kontrole

Kod: `wagi-masy-EM-kontrola-2026-10-09.py`; wyniki: `wagi-masy-EM-kontrola-2026-10-09.json`. Wszystkie liczby kontrolne są syntetyczne.

- Dokładna algebra nad wymiernymi liczbami zespolonymi: tożsamość Pauliego na bazie, antykomutatory, oba liczniki i zmiana triady; dwie niezdegenerowane kontrole tożsamości Wardowskiej.
- Dokładne ułamki: wagi Feynmanowskie, wielomian w całym parametrze cechowania, stała skończona i trzy części kulombowskie. Dowody w tekście nie zależą od próbek.
- Sześć porównań skończonej całki radialnej z logarytmem: błąd bezwzględny do `6,94·10⁻¹⁸`.
- Siedem porównań pełnych funkcji Feynmanowskich z niezależnymi pierwotnymi, także ponad progiem z zachowaną częścią urojoną: błąd do `6,89·10⁻¹⁵`.
- Sześć kontroli skończonej projekcji całego operatora kulombowskiego na powłoce: reszta do `3,56·10⁻¹⁵`. Całkowanie przez części dowodzi zerowania dla całego zakresu.

Kontrole pominięć dają rozróżnialne błędne wyniki: 4 po opuszczeniu kinetyki, `7/2` bez rzutu przestrzennego i 5 po opuszczeniu skończonego składnika MS-bar. Nie przeprowadzono dopasowania danych pomiarowych ani pełnego rachunku kanału aparatu O.
