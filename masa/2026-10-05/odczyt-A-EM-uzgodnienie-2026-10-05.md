# Odczyt A: uzgodnienie masy z pełną odpowiedzią i granica uzyskanego wyniku

Data rozpoczęcia: 05.10.2026; weryfikacja i zapis: 06.10.2026, Europe/Warsaw. Kontynuacja `pary-M-O-EM-2026-10-05.md`, punkt 2. **Status: wynik częściowy; pełnego kwantowego odczytu konkretnej pary z EM nie obliczono.**

Użytkownik zlecił dokończenie przejścia do A. Wykonano jawną jednopętlową część pędową energii własnej EM i jej uzgodnienie z parametrem masowym; sprawdzono odczyt pełnego swobodnego pakietu 3D oraz ograniczenie identyfikacji przy nieustalonym przygotowaniu. Te kontrole nie zastępują brakującej odpowiedzi aparatu SM. Żadnego z poniższych rachunków nie przedstawiam jako wyprowadzenia Yukaw ani jako zamknięcia pełnej funkcji masy.

**Najistotniejsza konsekwencja dla dalszego rachunku:** gdy zachowujemy sumę amplitud, na fazę całego porównania wpływa także nierówne tłumienie poszczególnych wkładów. Rozdział „najpierw odjąć fazę EM, potem odczytać masę” nie działa ogólnie. Masa już uwzględniona w A/B wymaga przy tym odjęcia odpowiadającej jej wstawki od reszty poprawki EM, nie usunięcia całej propagacji EM.

## 1. Zakres, wejścia i warunek rozstrzygnięcia

Podstawa czasu i 3D z R1a–R1c oraz poprawki 166, 178, 185–191, 198–208 pozostają punktem wyjścia. Nie rozdzielamy powstawania czasu, przestrzeni i masy na etapy. Współrzędne i pędy poniżej są reprezentacją istniejącego formalizmu w relacji do O. Parametr `n` nazywa różnicę wskazań ustalonego czytającego; nie jest uprzednią osią czasu. Dopiero uzasadnione przejście do własnego zliczenia nośnika pozwala utożsamić odpowiedni odczyt z A.

**Przyjęte składniki:** diagonalny naładowany fermion Diraca; zwykłe działanie QED jako fotonowy sektor wcześniejszego rachunku SM; standardowa regularyzacja wymiarowa i odjęcie MS-bar; cechowanie Feynmana do wyliczenia funkcji dwupunktowej; ta sama konwencja odwrotności `slash(p) − m − Σ` co w raporcie L/R. Nie zakładamy ostrego dokładnego modu naładowanego nośnika. Wyliczenie EM jest wektorowe; nie oznacza zrównania pełnych słabych wag L i R.

`μ = m/E_O`, `Π = p/E_O`, `q = Q/E_O` są bezwymiarowe. Q jest argumentem renormalizacji. α(Q) pozostaje funkcją; nie podstawiono jej zmierzonej wartości. Liczby w kontrolach są jawnie zadanymi danymi syntetycznymi.

**Spodziewam się:** przejście między parametryzacją przez masę biegnącą a przez A zachowa tę samą pełną odpowiedź w zadeklarowanym rzędzie, jeśli odjęta zostanie tylko już uwzględniona wstawka masowa. Przy znanym przygotowaniu odczyt pełnego pakietu może pozwolić odzyskać parametr, mimo że jego nachylenie fazy nie jest tym parametrem.

**Zdanie o upadku:** zamknięcie punktu 2 odpada, jeżeli trzeba zastąpić nieobliczoną odpowiedź aparatu przez 1, wyjąć jeden czynnik EM przed sumę amplitud, nazwać wskazanie O własnym zliczeniem każdego składnika pakietu albo ponownie doliczyć tę samą część masową EM. Symboliczny wzór na nieobliczone operatory przejścia nie liczy się jako wykonany rachunek aparatu.

## 2. Co rzeczywiście ma być porównywane

Zachowujemy wcześniejsze wielkości

\[
K_{10}=\operatorname{Tr}(F T_1\varrho T_0^\dagger),\qquad
P_b=\operatorname{Tr}(F T_b\varrho T_b^\dagger).
\]

T obejmuje przygotowanie, sterowanie, propagację, wymagane relacje EM oraz odczyt. F nie jest domyślnie jednością. Dla stanu czystego można wprowadzić amplitudy

\[
\mathcal A_b(a)=\langle a|\sqrt F T_b|\Psi\rangle,
\quad K_{10}=\sum_a\mathcal A_1(a)\mathcal A_0(a)^*.
\]

Stan mieszany obsługuje dodatkowa suma lub puryfikacja. Indeks a zawiera wszystkie nierozróżnione wyniki, także spin, odrzut i fotony. Przy wspólnym fizycznym przygotowaniu naładowanym nie oznacza to stanu gołego leptonu odłączonego od prawa Gaussa.

W rozwinięciu względem fotonowej poprawki do ustalonego kanału bez dodatkowych fotonów radiacyjnych:

\[
\begin{aligned}
K_{10}={}&\sum_a\mathcal A_1^{(0)}(a)\mathcal A_0^{(0)}(a)^*\\
&+\sum_a\left[
\mathcal A_1^{(2)}(a)\mathcal A_0^{(0)}(a)^*
+\mathcal A_1^{(0)}(a)\mathcal A_0^{(2)}(a)^*\right]\\
&+\sum_{a,\lambda}\int\frac{d^3k}{(2\pi)^3 2\omega_k}
\mathcal A_{1,\lambda}^{(1)}(a;k)
\mathcal A_{0,\lambda}^{(1)}(a;k)^*
+O(e^4).
\end{aligned}
\]

Superskrypt oznacza rząd dodatkowego sprzężenia radiacyjnego. Wymagane wspólne ubranie EM musi być już uzgodnione w amplitudach; ten zapis nie jest pozwoleniem na zignorowanie korelacji początkowych. Wkład wirtualny obejmuje właściwe diagramy energii własnej, wierzchołków, wymiany z aparatem i kontrczłony. Jednofotonowy składnik zachowuje odrzut i obie polaryzacje. W wyższym rzędzie dochodzą dalsze końcowe liczności. Nie twierdzimy, że samo wypisanie tej sumy dowodzi jej skończoności w podczerwieni.

To znana struktura porównania inkluzywnego, zastosowana do obu ramion. **Nie obliczono tu wszystkich amplitud tej sumy dla konkretnego O.** Wyliczony w następnym punkcie składnik dwupunktowy jest jednym z jej wejść.

## 3. Jawny pędowy wkład EM i odjęcie już uwzględnionej masy

### 3.1. Wynik poza powłoką

**Spodziewam się:** pozostaną oba współczynniki Diraca i zależność od całego Π². **Zdanie o upadku:** błąd znaku, brak skończonego członu z `ε × biegun UV` albo niezgodność z całką parametryczną odbiera wynikowi status.

W cechowaniu Feynmana, po odjęciu MS-bar, własny rachunek standardowego diagramu daje

\[
\widehat\Sigma_\gamma(\Pi;\mu,q)=
\frac{\alpha(q)}{4\pi}\int_0^1dx\,
\left\{(-2x\slashed\Pi+4\mu)
\ln\frac{q^2}{(1-x)(\mu^2-x\Pi^2)-i0}
+2x\slashed\Pi-2\mu\right\}.
\tag{1}
\]

Pochodzenie: po połączeniu mianowników i przesunięciu pędu w pętli licznik wynosi
`(−2x + 2ε) slash(Π) + (4 − 2ε) μ`. Ostatnie dwa człony (1) pochodzą z iloczynu części proporcjonalnej do ε i bieguna UV. Wcześniejszy raport obliczał projekcję masową tej całki; tutaj zachowano pełne dwa współczynniki przy dowolnym Π².

Niech `z = Π²/μ²`, `L = ln(q²/μ²)` i `ℓ(z) = ln(1−z−i0)`. Wtedy

\[
\widehat\Sigma_\gamma=
\frac{\alpha}{4\pi}\left[a(z)\slashed\Pi+\mu b(z)\right],
\]

\[
\begin{aligned}
a(z)&=-L-1-\frac1z+
\left(1-\frac1{z^2}\right)\ell(z),\\
b(z)&=4L+6+4\frac{1-z}{z}\ell(z).
\end{aligned}
\tag{2}
\]

Przy z=0 używa się ciągłych granic: `a(0)=−L−1/2`, `b(0)=4L+2`. Przy z=1: `a(1)=−L−2`, `b(1)=4L+6`.

Do otrzymania (2) wystarczają całki

\[
\int_0^1\ln(1-zx-i0)dx=-1-\frac{1-z}{z}\ell(z),
\]
\[
\int_0^1x\ln(1-zx-i0)dx
=-\frac14-\frac1{2z}+\frac{z^2-1}{2z^2}\ell(z).
\]

Sprawdzenie z literaturą: po przełożeniu konwencji F oraz M z [L3], wzory (62)–(63), przy ξ=1 i po odjęciu UV otrzymujemy te same współczynniki. To odtworzenie znanego diagramu, **nie nowy wynik fizyczny ani wyprowadzenie struktury SM z podstawy projektu**. Funkcja dwupunktowa poza powłoką jest zależna od cechowania. Dopiero całe porównanie z wierzchołkami i aparatem jest kandydatem na fizyczny odczyt.

### 3.2. Część zawarta już w A/B

Projekcja masowa daje

\[
\delta\mu_\gamma=
\frac{\alpha}{4\pi}\mu[a(1)+b(1)]
=\frac{\alpha}{4\pi}\mu(4+3L).
\tag{3}
\]

Jest to dokładnie wkład EM policzony w `LR-odczyt-A-dopasowanie-2026-10-04.md`. Nie liczymy go jako drugiego odkrycia. Nowe zastosowanie: gdy w propagacji używa się już parametru `μ_A = μ + δμ_γ + …`, reszta funkcji dwupunktowej musi mieć postać

\[
\boxed{\widehat\Sigma_{\gamma,\mathrm{res}}
=\widehat\Sigma_{\gamma,\overline{\rm MS}}
-\delta\mu_\gamma\,\mathbf1.}
\tag{4}
\]

Argumenty w (4) można zmienić z μ na μ_A w członie jednopętlowym z błędem następnego rzędu, z dala od obszarów wymagających dodatkowego wznowienia szeregu. Jest to masowy schemat na powłoce przy zachowanej konwencji normalizacji pola; **nie narzucamy residuum równego 1**. W pełnym SM analogicznie trzeba rozliczyć pozostałe już uwzględnione składniki dopasowania. Wyliczenie (1)–(4) obejmuje tylko sektor EM.

W (2) zamienia się tylko

\[
b(z)\longmapsto b_{\rm res}(z)
=L+2+4\frac{1-z}{z}\ell(z).
\tag{5}
\]

Nie zeruje się ani a(z), ani zależności od z, ani ciągłej części odpowiedzi. Na powłoce znika projekcja masowa, nie cała macierz. Na przykład przy `z=1−ε`:

\[
\sqrt z\,a(z)+b_{\rm res}(z)
=\varepsilon\left(2\ln\varepsilon+\frac L2\right)
+O(\varepsilon^2\ln\varepsilon).
\tag{6}
\]

Pozostaje zachowanie progowe. Nie zamieniamy tego zależnego od cechowania rachunku perturbacyjnego w samodzielny dowód dokładnego widma naładowanego sektora QED.

## 4. Jak ta sama poprawka wchodzi do całego K

**Spodziewam się:** wstawka masowa zadziała na całe przejścia obu stron. **Zdanie o upadku:** wzór jest niewystarczający, jeżeli różniczkuje tylko jedną wydzieloną fazę i pomija zależność propagacji oraz sprzężeń z aparatem.

Przy tej samej specyfikacji przygotowania, sterowania i efektu zapisu oznaczmy pełną odpowiedź najniższego rzędu przez `K⁽⁰⁾(μ;θ)`. Symbol θ zbiera te relacje aparatu, które są utrzymywane przy zmianie parametryzacji masy; nie jest nowym sprzężeniem teorii. Gdy masa zmienia się w kilku miejscach konstrukcji, pochodna obejmuje je wszystkie przy ustalonych niezależnych danych protokołu.

W jednym rzędzie EM:

\[
K=K^{(0)}(\mu)+K_\gamma^{[1],\overline{\rm MS}}(\mu)+\cdots.
\]

Zmiana parametryzacji na `μ_A=μ+δμ_γ` daje

\[
\boxed{
K=K^{(0)}(\mu_A)+
\left[K_\gamma^{[1],\overline{\rm MS}}(\mu_A)
-\delta\mu_\gamma\,\partial_\mu K^{(0)}(\mu_A)\right]
+\cdots .}
\tag{7}
\]

Kropki obejmują pozostałe składniki SM oraz wyższy rząd, z właściwym uzgodnieniem każdego z nich. Kγ w (7) oznacza **cały** wkład EM do tego samego porównania: wirtualny i realny, z tym samym F. Nie jest samą funkcją wpływu dwóch klasycznych prądów. W tej pracy Kγ dla konkretnego aparatu **nie zostało wyliczone**; (7) ustala jednoznacznie sposób rozliczenia części masowej.

Dla niezależnych od μ granicznych ρ i F:

\[
\partial_\mu K^{(0)}=
\operatorname{Tr}\!\left[F(\partial_\mu T_1^{(0)})\varrho T_0^{(0)\dagger}
+F T_1^{(0)}\varrho(\partial_\mu T_0^{(0)\dagger})\right].
\tag{8}
\]

Jeśli fizycznie określone przygotowanie lub zapis także zmieniają swoją reprezentację z μ, zachowuje się ich pochodne. Dla swobodnego jądra Diraca

\[
h(\boldsymbol\Pi)=\boldsymbol\alpha_D\cdot\boldsymbol\Pi+\beta\mu,
\quad U(n)=e^{-ihn},
\]

\[
\partial_\mu U(n)=-i\int_0^n ds\ U(n-s)\beta U(s).
\tag{9}
\]

To wstawka między propagacjami. Przy niezerowym pędzie nie jest ona `−inU`. W pełnej amplitudzie odpowiada jej standardowa wstawka masowa Diraca. Stała liczba `D` mnożąca pojedynczą fazę nie zastępuje (8)–(9) bez dodatkowego uzasadnienia.

Równanie (7) jest zmianą schematu w znanej teorii, a nie nowym prawem. Jego praktyczny skutek dla tego kroku jest konkretny: **nie wolno mnożyć propagatora, którego parametr zawiera już (3), przez drugi nieodjęty wkład tej samej energii własnej.** Odjęcie całej funkcji EM również byłoby błędem: usunęłoby zmiany kształtu odpowiedzi, wymiany z O i emisje.

## 5. Dlaczego samo odjęcie fazy radiacyjnej nadal nie wystarcza

Zachowajmy dla przejrzystości indeks r obejmujący pary historii i wszystkie wymagane kontrakcje. Już w podklasie, w której warunkowe stany radiacyjne są koherentne i ich nakładania mają postać `exp(−Γ+iΦ)`, otrzymujemy:

\[
K=\sum_r w_r\,e^{-\Gamma_r+i\Phi_r},\qquad
K_0=\sum_r w_r.
\tag{10}
\]

w zawiera pełne amplitudy i wagi odczytu; na ogół jest zespolone. To reprezentacja zależności, nie policzona suma dla aparatu. Przy małych Γ,Φ i `K₀≠0`, z dala od zer powodujących utratę kontroli rozwinięcia,

\[
\delta\arg K
=\operatorname{Re}\frac{\sum_r w_r\Phi_r}{K_0}
-\operatorname{Im}\frac{\sum_r w_r\Gamma_r}{K_0}
+O(\alpha^2).
\tag{11}
\]

**Drugi człon jest potrzebny.** Tłumienie zmienia względne udziały interferujących amplitud, więc może zmienić argument ich sumy. Jest zerowe jako wkład do fazy, gdy Γ jest rzeczywiście wspólne, ale nie ogólnie. Nie wolno zastąpić tych zespolonych kontrakcji zwykłą średnią prawdopodobieństw.

### Jawna kontrola, zachowująca ślad po fotonach

**Spodziewam się:** nierówne rzeczywiste nakładania radiacyjne przesuną fazę sumy dwóch wkładów. **Zdanie o upadku:** wynik upada, jeżeli wymaga odrzucenia końcowych fotonów albo nie jest realizowalny przez poprawne stany i efekt.

Weźmy amplitudę ramienia odniesienia `|0⟩` i amplitudę zachowanego wyjścia drugiego ramienia

\[
|\mathcal A_1\rangle=\frac{|0\rangle-i|\beta\rangle}{2},
\qquad \beta=\sqrt{2\ln2}\ \text{rzeczywiste}.
\]

Są to wyjściowe amplitudy po koherentnym połączeniu dwóch składników, nie próba przypisania pojedynczej drodze stanu pośredniego. Współczynnik `1/2` zachowuje fizyczne wagi; drugie wyjście można dołączyć, by domknąć unitarny interferometr. Stan koherentny daje `⟨0|β⟩=1/2`. Poszczególne nakładania radiacyjne to 1 oraz 1/2, oba z fazą zero. Bez tego rozróżnienia radiacyjnego i po jego uwzględnieniu:

\[
K_0=\frac{1-i}{2},\quad K=\frac12-\frac i4,
\quad\arg(K/K_0)=0{,}3217505544.
\tag{12}
\]

`P₀=1`, `P₁=1/2` i `|K|²=5/16≤P₀P₁`. Ślad po 40 stanach liczności odtwarza wynik; błąd normowania stanu koherentnego jest na poziomie precyzji maszynowej. To dokładna kontrola algebry odczytu, **nie pełny rachunek QED aparatu**. Zbiorczy mod stanu koherentnego nie jest redukcją przestrzeni fizycznej do 1+1.

W konsekwencji nawet znajomość wszystkich Φ nie wystarcza do usunięcia wpływu EM z fazy K. Trzeba znać ich kontrakcję z Γ, propagacją i F. To rozwinięcie zakresu ostrzeżenia z poprzedniego raportu, a nie twierdzenie o dodatkowym oddziaływaniu.

## 6. Pełny swobodny pakiet 3D: kontrola właściwego rodzaju odczytu

**Spodziewam się:** zachowane rozłożenie pędów i nierówna waga dadzą fazę zależną od n; znając oba, będzie można odzyskać syntetyczny parametr. **Zdanie o upadku:** niezgodność kwadratur albo konieczność ustawienia F=1 odbierają tej kontroli wartość.

W swobodnym dodatnioenergetycznym sektorze Diraca, z unormowanym spinem, przyjmujemy rozkład pędów G o średniej zero i szerokościach `(0,22; 0,31; 0,39)` oraz efekt

\[
f(\boldsymbol\Pi)=0{,}35+0{,}4\frac{|\boldsymbol\Pi|^2}{1+|\boldsymbol\Pi|^2}.
\]

To jawne dane kontrolnego przygotowania i zapisu, nie struktura nośnika wyprowadzona z podstawy. `0≤f≤1`, f nie jest stałe. Dla dwóch swobodnych opóźnień:

\[
K_0(n;\mu)=\int_{\mathbb R^3}d^3\Pi\ G(\boldsymbol\Pi)f(\boldsymbol\Pi)
e^{-in\sqrt{\mu^2+|\boldsymbol\Pi|^2}},
\quad P_0=P_1=\int Gf.
\tag{13}
\]

Obie ewolucje są zachowane; n jest różnicą wskazań O. **Nie przypisujemy całemu pakietowi jednej klasycznej drogi ani jednej różnicy własnych długości D.** To nie jest pełny model sterowania dwiema drogami starego raportu, tylko kontrola kwantowej propagacji.

Przy zadanym `μ=1,1`:

| n | `−Im[(∂ₙK₀)/K₀]` | Parametr w dyspersji |
|---:|---:|---:|
| 1 | 1,23426971825 | 1,1 |
| 2 | 1,23156795348 | 1,1 |
| 4 | 1,22155894454 | 1,1 |
| 8 | 1,19173479747 | 1,1 |

To wciąż odczyt względem O. Różnica nie dowodzi zmiany masy: wskazuje wpływ zachowanego rozkładu pędów i wag. Dopasowanie pełnych rzeczywistych i urojonych części (13), przy **znanym** G i f, odzyskuje `1,10000000000001`. To odzyskanie zadanego wejścia na danych syntetycznych, nie przewidywanie masy i nie rozwiązanie Yukaw. Kwadratury 40³ i 64³ różnią się w K o najwyżej `1,31·10⁻¹³` dla tych czterech n; zachowano wszystkie trzy składowe pędu.

## 7. Co może i czego nie może ustalić samo K

**Spodziewam się:** bez ustalenia przygotowania ogólny sygnał fazowy nie wybierze masy jednoznacznie. **Zdanie o upadku:** kontrprzykład musi używać znormalizowanych pakietów 3D i tego samego dopuszczalnego efektu, bez ujemnych wag prawdopodobieństwa.

W tym samym swobodnym sektorze wybieramy znormalizowaną gęstość energii względem O:

\[
h(E)=\Theta(E-E_*)\frac{(E-E_*)^2}{2\kappa^3}
e^{-(E-E_*)/\kappa}.
\]

Dla **każdego** `0<μ<E_*` istnieje izotropowy pakiet pędowy

\[
|\psi_\mu(\boldsymbol\Pi)|^2=
\frac{h(E)}{4\pi |\boldsymbol\Pi|E},
\quad E=\sqrt{|\boldsymbol\Pi|^2+\mu^2}.
\tag{14}
\]

Poza podparciem h wartość wynosi zero. Ponieważ `dE=|Π|d|Π|/E`, całka `∫d³Π |ψμ|²=1`. Wybierzmy ten sam filtr energii `f(E)=f₀ exp[−b(E−E_*)]` na tym podparciu, z `0<f₀≤1`, `b≥0`; poniżej progu można go przedłużyć stałą f₀. Wtedy

\[
\boxed{K(n)=\frac{f_0e^{-iE_*n}}{(1+\kappa b+i\kappa n)^3},
\quad P_0=P_1=\frac{f_0}{(1+\kappa b)^3}.}
\tag{15}
\]

Wynik jest identyczny dla całej rodziny μ. Np. `μ=0,6` i `μ=1,1`, `E_*=1,5`, `κ=0,2`, `b=0,8`, `f₀=0,7`: bezpośrednie całki 3D z dokładnie wykonaną częścią kątową zgadzają się z (15) do `2,2·10⁻¹⁶` w sprawdzonych punktach. Samo długie oczekiwanie także nie rozwiązuje tego przykładu: asymptotyczne nachylenie fazy dąży do E_*, a nie do μ, bo przygotowanie nie ma podparcia przy pędzie zero.

**Ścisły zakres:** różne μ mają tutaj różne przygotowania pędowe. Kontrprzykład nie dotyczy ustalonego, znanego przygotowania i nie dowodzi niemożności pomiaru masy. Jest kontrolą sektora swobodnego, nie dowodem identyczności pełnych oddziałujących porównań QED. Pokazuje, dlaczego same wartości K i P nie określają pełnej pary oraz dlaczego nie można zagwarantować uniwersalnej procedury odzyskania A z ich fazy dla nieokreślonych wejść. Nie podważa definicji A na własne tyknięcie; w (15) n jest wskazaniem O, a brakującą informacją jest właśnie relacja tego odczytu do dyspersji i przygotowania nośnika.

## 8. Bilans kontroli i rzeczywisty stan punktu 2

| Sprawdzenie | Wynik | Zakres |
|---|---|---|
| (1) wobec (2), siedem z po obu stronach progu | błąd ≤ `4,8·10⁻¹³` | Jeden diagram, cechowanie Feynmana |
| Projekcja masowa reszty | zero algebraicznie i numerycznie | Rząd α |
| Propagator przed i po zmianie schematu | po zmniejszeniu parametru rozwinięcia dwukrotnie błąd maleje ok. 4 razy | Różnica następnego rzędu; test poza powłoką |
| Celowe ponowne dodanie części masowej | błąd maleje ok. 2 razy | Błąd już pierwszego rzędu |
| Wstawka masowa (9) wobec niezależnej pochodnej Frécheta | `1,1·10⁻¹⁵` | Pełna macierz Diraca przy niezerowym pędzie |
| Nierówne rzeczywiste tłumienie | przesunięcie fazy `0,3217505544` | Poprawne amplitudy i ślad po fotonach |
| Pełny pakiet 3D | odzyskany zadany parametr przy zachowanych wagach | Propagacja swobodna |
| Dwa przygotowania z (14) | identyczne K i P dla różnych μ | Brak kalibracji przygotowania |

Kontrole implementuje `odczyt-A-kontrola-2026-10-05.py`; pełne wyniki są w pliku JSON o tej samej podstawie nazwy. Nie uruchamiano obliczeń na rozsiewie, siatce świata ani fizycznym cięciu. Kwadratury są wyłącznie metodą liczenia jawnych całek.

**Zamknięte w zadeklarowanym zakresie:** sposób rozliczenia jednopętlowej części masowej EM przy przejściu do propagacji opisanej przez A — (4) i (7). Jawny pozostały wkład pędowy zapisano w (2), (5). Sprawdzono, dlaczego reszta odpowiedzi nie jest tylko dodawaną fazą.

**Niezamknięte:** całe `Kγ` dla jednej określonej pary z aparatem, w tym rzeczywiste sprzężenia wytwarzające i łączące drogi, przygotowanie z wymaganymi relacjami EM, odpowiedź spinowa, odrzut, pakiet i rzeczywisty efekt F. Nie policzono pełnego przejścia dla starej pary z `D≠0`. Nie udowodniono skończoności jej całego odczytu w podczerwieni. **Punkt 2 nadal jest otwarty.**

Brak specyfikacji aparatu nie jest dowodem, że zadania nie da się rozwiązać. Można wybrać i jawnie zdefiniować konkretny protokół w istniejącym działaniu SM; będzie to nazwany rachunek warunkowy. W tej próbie takiego kompletnego protokołu nie skonstruowano. Zastąpienie go pakietem z (13), dowolną macierzą F lub nowym modelem zabawkowym nie uprawniałoby do ogłoszenia sukcesu.

**Konkretny warunek kontynuacji:** zanim rozpocznie się następną całkę EM, trzeba mieć określone wspólne przygotowanie, oba przejścia sterujące i efekt zapisu — oraz z tych samych składników wyprowadzić amplitudy bez dodatkowego fotonu i z fotonem, z odrzutem. Wtedy stosuje się (7) do całej sumy i sprawdza identyfikowalność A w tej parze. To specyfikacja relacji odczytu, nie dopisywanie mechanizmu do teorii.

## Źródła i wykorzystany zakres

- Pliki projektu: `punkt-wznowienia-2026-10-05.md`; R1a–R1c, §E i poprawki wskazane w §1; `LR-odczyt-A-dopasowanie-2026-10-04.md`; `yukawy-nu-roznica-slaba-odczyt-2026-10-04.md`; `pary-M-O-EM-2026-10-05.md`. Ich zamkniętych wyników nie nadano jako nowych poprawek.
- **[L1]** R. Hempfling, B. A. Kniehl, [Relation between the fermion pole mass and MS-bar Yukawa coupling in the standard model](https://bib-pubdb1.desy.de/record/392941/files/PhysRevD.51.1386.pdf), Phys. Rev. D 51, 1386 (1995), zwłaszcza (2.12)–(2.14). Użyty zakres: interpretacja perturbacyjnego parametru biegunowego i rozliczenie składników dopasowania. Bez wartości mas z pomiarów.
- **[L2]** C. DeLisle, P. C. E. Stamp, [Decoherence of a 2-Path System by Infrared Photons](https://arxiv.org/pdf/2211.05813), wersja z 2024 r., §II. Autorzy jawnie zastępują rodziny kwantowych dróg przez dwa prądy w odpowiednim przybliżeniu. Nie przeniesiono ich wyniku na pełny propagujący pakiet.
- **[L3]** A. Kızılersü, M. Reenders, M. R. Pennington, [One Loop QED Vertex in Any Covariant Gauge: Its Complete Analytic Form](https://arxiv.org/pdf/hep-ph/9503238), Phys. Rev. D 52, 1242 (1995), §3.1, (62)–(63), z definicjami (42), (48); (7)–(9) dla relacji propagatora z wierzchołkiem. Niezależnie sprawdzono postać dwóch funkcji poza powłoką. Współczynniki mają status znanego rachunku QED, nie nowego wyprowadzenia ramy.
- **[L4]** X. Feal, A. Tarasov, R. Venugopalan, [QED as a many-body theory of worldlines: I. General formalism and infrared structure](https://arxiv.org/pdf/2206.04188) oraz [II. All-order S-matrix formalism](https://arxiv.org/pdf/2211.15712). Użyty zakres: zachowanie spinowej propagacji, energii własnej, wymiany i emisji w jednym formalizmie. Dostępność formalnego zapisu nie zastępuje obliczenia konkretnej pary; nie przyjęto z tych prac dodatkowych składników teorii.

Ten raport zawiera wyprowadzenia i kontrole asystenta [A][P] w nazwanym zakresie znanej teorii [L]. Kontrprzykłady mają dowody algebraiczne w opisanych klasach. Nie zmieniono statusu podstawy użytkownika ani nie ustanowiono nowego numeru w rejestrze poprawek.
