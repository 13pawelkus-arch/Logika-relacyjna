# Jądra i wagi działania: co wymuszają relacje ramy

09.10.2026. Kontynuacja poprawki 256 na polecenie użytkownika: uzasadnić przyporządkowanie jawnych jąder i wag działaniu z relacji ramy. Źródła projektu: R1a–R1c, R1d-F, R1f-1, 169, 177–179, 204, 208, 213–214, 217 oraz 256. Podstawa czasu i 3D jest przyjęta i stosowana. Nie dodajemy do fizycznego modelu nowych pól, sprzężeń ani areny.

## Zapis przed nowymi rachunkami i kontrolami

**Spodziewam się:** nieodczytywalność fazy przypisanej samemu końcowi wymusi sposób przenoszenia amplitudy między końcami i zgodność wierzchołka z jądrem. Algebra R1b–R1c ustali macierzowe miejsca dla kinetyki i zygzaka L/R. W nazwanej klasie minimalnego działania pozwoli to odtworzyć kanoniczne składniki użyte w 256. Same symetrie mogą pozostawić funkcje odpowiedzi i pełne wagi obiegów nieustalone.

**Zdanie o upadku mocniejszego wyprowadzenia:** twierdzenie, że te przesłanki wybierają całe działanie oraz wszystkie jego wagi, upada, jeśli różne wagi tego samego obiegu zachowują sprawdzane niezmienniczości i tę samą drugą wariację, albo jeśli tożsamość wiążąca wierzchołek z jądrem zostawia niezerowy składnik. Przykłady testują wymienione przesłanki; nie są kontrmodelami całej podstawy ani propozycją rozszerzenia QED.

**Przyjęte składniki:** kwantowa algebra i zmiana czytającego z R1b–R1c; para L/R i relacja faz U(1) z R1d; odczyt sumy amplitud oraz faz obiegów z 177, z wagami zachowanymi zgodnie z 213. Dla klasyfikacji jąder w zapisie spektralnym osobno deklarujemy jednorodny sektor bez wyróżnionego kierunku, własne argumenty fazowe czytającego i istniejące przyporządkowanie L/R. Dla odtworzenia kanonicznego QED osobno badamy wybór lokalnego działania z najniższą liczbą pochodnych. Dla reguł pętlowych osobnym warunkiem będzie kanoniczna algebra modów oraz wybrany stan swobodny, dla którego zachodzi reguła Wicka. Nie utożsamiamy tych warunków z tomografią lokalną P5.

**Odczyt:** porównanie dwóch pełnych odpowiedzi przy tym samym przygotowaniu i efekcie O; jądro i wierzchołek są składnikami tej odpowiedzi, nie bezpośrednimi cechami M. Wszystkie argumenty spektralne są stosunkami do wspólnego odniesienia fazowego O. Brak odczytu tła nie zeruje propagatora. Wyjaśnienie kształtu jądra nie wybiera wartości stosunków mas ani pełnego protokołu 215.

## 1. Wynik: jądro i wierzchołek przestają być niezależnymi wejściami

**[A][T] w podanym zakresie:** nieodczytywalność fazy końca wymusza kowariancję transportu amplitudy, a jej różniczkowanie wiąże wierzchołek z odwrotnym propagatorem. Przy pierwszorzędowym jądrze Diraca daje to minimalny wierzchołek EM z tym samym współczynnikiem co kinetyka. Przy kwadratowym, dwupochodnym sektorze relacji faz otrzymujemy jądro Maxwella; na L/R jego fermionowy odpowiednik daje dokładnie mianownik i licznik z 256. Po przyjęciu kanonicznego stanu swobodnego reguły jednej pętli są kontrakcjami tych samych składników, a nie osobną listą dowolnych wag.

**Granica [A][T][O]:** sama zmiana odniesienia nie wybiera funkcji skalarnych pełnej odpowiedzi, poprzecznej części wierzchołka ani pełnego działania z jego drugiej wariacji. Odtworzenie kanonicznego QED wymaga nazwanego wyboru klasy działania i reprezentacji kwantowej. Wyprowadzenie tego wyboru z całej podstawy pozostaje niewykonane. Nie jest to twierdzenie, że w ramie nie ma dynamiki: istnienie dynamiki jest w R1a; badamy jej ilościową regułę wag.

**Dokładna klasa odtworzenia:** bilinearna kinetyka L/R z jednym gradientem i stałym skalarnym sprzężeniem L/R; kwadratowa część cechowania z dwoma gradientami; zależność części fermionowej od A wyłącznie przez transport tej kinetyki, bez osobno zadanego sprzężenia do F; reprezentacja kanonicznych modów z wybranym stanem swobodnym. Minimalność tutaj nazywa te konkretne ograniczenia. Nie wyprowadzamy zakazu wszystkich pozostałych odpowiedzi przez samo słowo „lokalność”.

## 2. Transport faz na relacjach — bez wyboru swobodnych wag

Niech `g_x=exp(iQχ_x)` będzie zmianą konwencji fazy przy końcu x. Z R1d sama ta konwencja nie jest odczytywalna. Amplituda porównania `ψ̄_x U_xy ψ_y` ma więc pozostać ta sama przy `ψ_x→g_xψ_x`. To wymusza

$$
U_{xy}\longmapsto g_xU_{xy}g_y^{-1}.
$$

Tutaj `U_xy` mapuje amplitudę z y do x. Transport kolejno po tej samej drodze składa się mnożeniem. Nie utożsamiamy transportów po różnych drogach: ich różnica daje obieg. Dla dwóch dróg od y do x,

$$
W_{12}=U_{\gamma_1}U_{\gamma_2}^{-1},
$$

fazy końców wypadają. Jest to dokładnie obiekt odczytu interferencyjnego z 177. Odwrócenie orientacji obiegu w U(1) daje sprzężenie zespolone.

Na relacji bilinearnego jądra możemy pisać `D_xy=h_xyU_xy`, gdzie `h_xy` jest neutralną wagą i macierzową mapą amplitud. Wówczas

$$
D_{xy}\longmapsto g_xD_{xy}g_y^{-1}.
$$

**Wymuszona jest zgodność fazowa, nie `h_xy=1`.** Nierówne wagi przygotowania i transportu z 213 zostają. Transformacja końców nie może wybrać tych wag, bo skraca się przy każdym `h_xy`. Wybrana relacja nie jest fizycznym powrotem tylko dlatego, że w rachunku występuje sprzężenie hermitowskie.

Jeśli transport ma opis różniczkowy względem argumentów odczytu O, zachowanie powyższej równości wymaga pochodnej kowariantnej. Przy konwencji `D_μ=∂_μ+ie₀QA_μ` i `ψ→exp(iQχ)ψ`, mamy `A_μ→A_μ−∂_μχ/e₀`. Pierwszy rząd tej samej mapy daje sprzężenie z koneksją. Istnienie takiego opisu i rząd różniczkowy jądra są warunkami przekładu; nie wynikają z samego przestawienia faz końców.

## 3. Co ustala algebra R1b–R1c w jądrze fermionowym

Używamy `P=p/E_O`, `s=(P⁰)²−|P|²`. Nie dodajemy osi czasu: `P⁰` jest częstością fazową przy odniesieniu O. Nieznormalizowany odczyt ma postać `P=P⁰𝟙+P·σ`, a

$$
\bar P=P^0\mathbb1-P\cdot\sigma,\qquad
P\bar P=\bar PP=s\mathbb1_2.
$$

To wymusza macierzową kontrakcję i formę determinantową, nie równanie pola samo w sobie. R1d przyporządkowuje dwa typy spinora parze L/R. Przy tym przyporządkowaniu i bez dodatkowego wyróżnionego kierunku najogólniejsze jądro spektralne ma miejsca

$$
\mathcal D(P)=
\slashed P\,[a_L(s)P_L+a_R(s)P_R]
-[b_L(s)P_L+b_R(s)P_R].
$$

Nie zakładamy tutaj równości chiralności. `P_L,P_R` są rzutami na L/R; ich etykiety nie są kierunkami przestrzennymi. Skalarna mapa na irredukowalnym spinorze musi być proporcjonalna do `𝟙₂`; wektorowy blok o jednym argumencie ma formę `P` lub `P̄`, z funkcją niezmiennika s. W przyjętej bazie:

$$
\mathcal D=
\begin{pmatrix}
-b_L\mathbb1_2&a_R\bar P\\
a_LP&-b_R\mathbb1_2
\end{pmatrix}.
$$

Wprost przez mnożenie bloków, dla `d(s)≠0`:

$$
\mathcal D^{-1}=
\frac1{d(s)}
\begin{pmatrix}
b_R\mathbb1_2&a_R\bar P\\
a_LP&b_L\mathbb1_2
\end{pmatrix},
\quad d(s)=s\,a_La_R-b_Lb_R,
\quad\det\mathcal D=d(s)^2.
$$

Odtwarza to miejsce funkcji masowej z 214. Macierzowy kształt jest związany przez algebrę; funkcje `a_L,a_R,b_L,b_R` nie zostały przez tę tożsamość wybrane.

**Kanoniczne ograniczenie:** jeśli wybieramy lokalną kinetykę o jednym gradiencie fazy, skalarne sprzężenie L/R oraz wektorowy, jednakowo znormalizowany sektor EM, mamy `a_L=a_R=Z_ψ`, `b_L=b_R=M`. Po normalizacji `η=M/Z_ψ`:

$$
\mathcal D_0=\slashed P-\eta,
\qquad
\mathcal D_0^{-1}=\frac{\slashed P+\eta}{s-\eta^2}.
$$

To wyprowadzenie odwrotności z relacji bloków, nie założenie licznika niezależne od mianownika. **Jednogradientowość i stałość tych współczynników w swobodnym jądrze pozostają wyborem klasy.** Nie usuwają zależności spektralnej pełnego jądra po uwzględnieniu oddziaływań.

## 4. Jądro relacji faz i dwie fizyczne polaryzacje

W jednorodnym sektorze, bez dodatkowego kierunku stanu lub otoczenia, symetryczna lorentzowska forma dwupunktowa wektora ma postać

$$
\mathcal K_{\mu\nu}(P)=A(s)g_{\mu\nu}+B(s)P_\mu P_\nu.
$$

Zmiana `A_μ` o gradient jest zmianą opisu faz końców. W części nieustalającej cechowania musi być kierunkiem zerowym jądra. Stąd

$$
P^\mu\mathcal K_{\mu\nu}=0
\ \Longrightarrow\ A(s)+sB(s)=0,
\qquad
\mathcal K_{\mu\nu}=H(s)(P_\mu P_\nu-sg_{\mu\nu}).
$$

To równanie dla całego s, nie losowanie wartości. **Wymuszona jest forma poprzeczna; `H(s)` pozostaje.** Dla jądra lokalnego z dwoma gradientami i niezerową swobodną sztywnością `H=Z_A` jest stałe. Wówczas jądro wynika z `−Z_AF_{μν}F^{μν}/4`. Druga lorentzowska forma kwadratowa, `F_{μν}F̃^{μν}`, jest abelowym członem brzegowym w topologicznie trywialnym sektorze ze stałym współczynnikiem; nie zmienia tego lokalnego jądra. Nie wydajemy tu werdyktu o wszystkich sektorach brzegowych.

Ustalenie cechowania daje dodatkowo `−Z_A(P·A)²/(2ξ)`. Na podprzestrzeni `s≠0`, dla `ξ≠0`, zapis przez rzuty `P_T=g−PP/s`, `P_\parallel=PP/s` daje jądro `−Z_As(P_T+ξ⁻¹P_\parallel)` i odwrotność

$$
-\frac1{Z_As}(P_T+\xi P_\parallel)
=-\frac1{Z_As}\left[g-(1-\xi)\frac{PP}{s}\right].
$$

To propagator z 256 po określeniu przepisu na bieguny. Landau jest granicą `ξ→0`, a nie odwróceniem nieustalonego jądra. Rzut w zapisie kowariantnym sam nie jest przestrzenią polaryzacji fotonu: na powłoce, po więzie i równoważności cechowania, są dwa fizyczne stany z R1e. Nie wraca wyjaśnienie trójki przez `D−1`.

Nie ma powodu utożsamiać pełnej `H(s)` ze stałą `Z_A`. W istniejącym QED odpowiedź pętli i progi dają jej zależność od ilorazów; F0 ją zachowuje. „Bez niezależnej skali” nie usuwa tych stosunków. Warunek na dwa gradienty dotyczy wybranego działania wyjściowego, nie całej funkcji po uwzględnieniu oddziaływań.

## 5. Wierzchołek jako pochodna tego samego jądra

Różniczkujemy `D^g_xy=g_xD_xyg_y⁻¹` przy infinitesymalnej zmianie χ. W opisie spektralnym, przy zgodnym przyporządkowaniu prądu, otrzymujemy dla wierzchołka z wyjętym sprzężeniem e:

$$
q_\mu\mathcal V^\mu(k,p)
=Q[\mathcal D(k)-\mathcal D(p)],\qquad q=k-p.
$$

To tożsamość Wardowska: wierzchołek i jądro niosą tę samą zmianę odniesienia. Dla pełnych funkcji kwantowych wymaga ona również nieanomalnej realizacji relacji faz; w wektorowym QED jest zachowana przez zgodny rachunek. Nie wyprowadzamy przez nią grupy U(1) ani reprezentacji Q.

**Kanoniczny przypadek:** dla `D=Z_ψP̸−M` część bez dodatkowych gradientów wynosi `V^μ=QZ_ψΓ^μ`. Nie można zmienić jej względnej wagi niezależnie od kinetyki. Dla działania

$$
S_{\rm min}=\int\left[
Z_\psi\bar\psi i\Gamma^\mu(\partial_\mu+ie_0QA_\mu)\psi
-M\bar\psi\psi-\frac{Z_A}4F_{\mu\nu}F^{\mu\nu}\right]
$$

przy dodatnich `Z_ψ,Z_A` normalizacje `ψ_c=√Z_ψψ`, `A_c=√Z_AA` dają `η=M/Z_ψ`, `e=e₀/√Z_A`, `α=e₀²/(4πZ_A)`. Dlatego skalarny wybór normy spinora nie jest osobnym sprzężeniem EM. Znana α dopuszczona w 253 ustala odpowiednią relację współczynników, nie zostaje wyprowadzona. W zapisie działania całka i argumenty odnoszą się do przyjętej reprezentacji odczytów; nie nadają arenie niezależnej zawartości.

**Pełna odpowiedź:** w parzystym wektorowym przypadku `D(P)=A(s)P̸−B(s)`, jedna regularna część wierzchołka spełniająca tę samą tożsamość ma postać

$$
\mathcal V_L^\mu=Q\left\{
\frac{A(k^2)+A(p^2)}2\Gamma^\mu
+(k+p)^\mu\left[
\frac{A(k^2)-A(p^2)}{k^2-p^2}\frac{\slashed k+\slashed p}2
-\frac{B(k^2)-B(p^2)}{k^2-p^2}\right]\right\}.
$$

Iloczyn z q daje dokładnie różnicę D, ponieważ `q·(k+p)=k²−p²`. Przy równych niezmiennikach ilorazy różnicowe przechodzą w pochodne, jeśli A i B są różniczkowalne. To zapis Ball–Chiu; określenie „podłużna” oznacza rolę w tożsamości, nie rzut całego wektora na q.

Równanie dopuszcza ponadto `V_T`, z `q_μV_T^μ=0`. Przykładowy niezerowy tensor `σ^{μν}q_ν` ma zerową kontrakcję przez antysymetrię. W istniejącym QED części poprzeczne są obliczane z tego samego działania. **Nie dodajemy wolnego członu Pauliego do modelu.** W przykładzie pokazujemy wyłącznie, że sama tożsamość nie wybiera ich funkcji. Nie wolno też ustawić pełnego `V_T=0` tylko dlatego, że odtworzono minimalny wierzchołek wyjściowy.

Kontrola literaturowa: [Kızılersü–Reenders–Pennington, hep-ph/9503238](https://arxiv.org/abs/hep-ph/9503238), równania (1), (7)–(11). Znana jest zgodność pełnego propagatora i części wierzchołka ustalonej tożsamością; używamy jej do kontroli własnej kontrakcji.

## 6. Druga wariacja nie wybiera całej wagi obiegu

Niech `W_c=e^{iθ_c}` oznacza odczytywalną relację dwóch transportów. Rozważamy, **wyłącznie jako test wskazanych warunków**, rodziny wag tego samego W:

$$
s_c=1-\operatorname{Re}W_c=1-\cos\theta_c,\qquad
f_\lambda(\theta_c)=\beta[s_c+\lambda s_c^2],
\quad\beta>0,\ \lambda\ge0.
$$

Wszystkie mają zmianę faz końców niewidoczną, nie zależą od orientacji obiegu, są analityczne, okresowe, nieujemne, znikają dokładnie przy `W_c=1` i nie potrzebują dodatkowego odniesienia jednostek. Są funkcjami już obecnego obiegu, nie fazami w punkcie. Wokół `θ=0`:

$$
f_\lambda(\theta)=\beta\left[
\frac{\theta^2}2+
\left(-\frac1{24}+\frac\lambda4\right)\theta^4
+O(\theta^6)\right].
$$

Zatem `f_λ″(0)=β` dla każdego λ, lecz `f_λ⁽⁴⁾(0)=β(−1+6λ)` i pełne wagi są inne. Przykładowo `θ=π/2` daje `f_λ=β(1+λ)`. Wartość nie jest wspólnym dodatkiem ani przeskalowaniem przy zachowaniu tej samej sztywności.

**Wniosek o dokładnym zakresie:** cechowanie, odwrócenie obiegu, dodatniość i zadana druga wariacja nie wybierają pełnej wagi Wilsona. To nie dowód, że każda z powyższych wag realizuje całą ramę, Lorentza, przyczynowość i właściwą kwantową teorię; tych przejść dla rodziny nie wykonano. λ nie jest nową daną fizycznego modelu ani propozycją zmiany QED. Jest świadkiem niewystarczalności wymienionego ciągu uzasadnienia. Sama znajomość Hessego nie odróżnia różnych funkcji.

Drugi poziom interferencji z 177 wymusza postać **odczytu** `|Σw_γe^{iφ_γ}|²`, z członami parami. Nie utożsamia tej liczby z działaniem `S[W]`. Zmiana funkcji działania nie dokłada trzeciego poziomu reguły Borna; są to różne miejsca w konstrukcji. Także `𝟙` w regule kompletności nie usuwa `w_γ` ani propagatorów.

Rodzina powyżej ma tę samą część kwadratową i — przy niezmienionym minimalnym sektorze fermionowym — ten sam wyjściowy wierzchołek ψψA. Dlatego **nie jest kontrprzykładem do trójki z 256**. Elektronowa poprawka jednej pętli używa właśnie tych dwóch jąder kwadratowych i dwóch wierzchołków ψψA. Niewyznaczenie pełnego działania jest mocniejszą luką niż niewyznaczenie składników potrzebnych do tego konkretnego rzędu. Bez mapy wszystkich obiegów na ten lokalny sektor nie orzekamy o dalszych rzędach rodziny.

## 7. Które reguły pętli są już wymuszone po wyborze kwantowej reprezentacji

W wybranej kanonicznej reprezentacji modów i stanie swobodnym, dla którego zachodzi Wick, propagatory są kontrakcjami tego samego działania kwadratowego. Dla skończonej liczby modów i uzgodnionego przepisu na całki:

$$
\frac{Z_B[J]}{Z_B[0]}=
\exp\left[-\frac i2J\mathcal K^{-1}J\right],
\qquad
\frac{Z_F[\bar\zeta,\zeta]}{Z_F[0,0]}=
\exp[-i\bar\zeta\mathcal D^{-1}\zeta].
$$

Obie równości wynikają z dopełnienia kwadratu, odpowiednio dla zmiennych zwykłych i antykomutujących. Różniczkowanie po źródłach daje wszystkie sparowania. Propagator bosonu to `iK⁻¹`, fermionu `iD⁻¹`; znaki i kontrakcje nie są osobnymi dopasowywanymi wagami. Nieskończoną reprezentację i przepis na granice trzeba jeszcze określić; wzory skończone nie wybierają ich same.

Rozwinięcie `exp(iS_int)` daje `1/2!` przy dwóch wierzchołkach. Dwie kolejności ich przyporządkowania w elektronowej poprawce znoszą tę dwójkę. Wstaje ta sama kontrakcja z 256:

$$
\Sigma(P)\ \propto\
e^2Q^2\int d\mu(K)\,
\Gamma^\mu\mathcal D_0^{-1}(P-K)\Gamma^\nu
(\mathcal K_0^{-1})_{\mu\nu}(K).
$$

Mianowniki i spin są zachowane. Znaki zamkniętej pętli fermionowej pochodzą z antykomutacji przy tym przyporządkowaniu; sam znak obrotu spinora o 2π nie stanowi tutaj niezależnego dowodu wszystkich reguł statystyki pola.

Miara wewnętrznej sumy jest regułą kompletności reprezentacji: `Σ_a|a⟩⟨a|=𝟙` albo jej wersją ciągłą. W przyjętym opisie Fourierowskim `∫dμ(P)e^{iP·X}=δ(X)` daje `dμ=dP⁰d³P/(2π)⁴`. Inna konwencja normy modów przesuwa czynniki między miarą i wierzchołkami, nie zmieniając całej kontrakcji. `P⁰` nadal jest argumentem fazowym. **To nie wyprowadza wyboru ciągłej reprezentacji ani jej jednorodności z samej podstawy.** Nie wolno pomylić kompletności z ustawieniem propagatora lub metryki efektu O na 𝟙 — 213.

Jądro nie wybiera też samo wszystkich funkcji Greena. Już dla `D₀=P̸−η` dodatek `(P̸+η)c(P)δ(s−η²)` jest rozwiązaniem jednorodnym, bo po mnożeniu dostajemy `(s−η²)δ(s−η²)=0`. To nie nowa cząstka ani nowa interakcja. Rodzaj odpowiedzi i przygotowanie ustalają warunki brzegowe/korelacyjne. Odpowiedź przyczynowa i korelator uporządkowany użyty w pętli są różnymi obiektami tego samego modelu; nie wolno wyprowadzić Feynmanowskiego `i0` z samej formy stożka.

Kontrola tego rozdzielenia bez zmiany działania: dla jednego kanonicznego modu, z fazą `z=exp(−iφ)` między odczytami i średnim obsadzeniem N, korelatory mają postać `G_>=(N+1)z+Nz*`, `G_<=(N+1)z*+Nz`. Ich różnica `z−z*` jest niezależna od N, same korelatory — zależne. Próżnia swobodna i stan quasi-free o `N=1` są różnymi przygotowaniami w tej samej algebrze; w drugim przypadku wagi obsadzeń mogą być `ρ_n=2^{−n−1}`. Przykład nie zamienia temperatury ani fazy modu w zewnętrzny czas. Pokazuje, dlaczego podanie jądra i komutatora nie zastępuje podania stanu użytego do kontrakcji.

**Miejsce nadal otwarte:** wybór przyporządkowania nośników sieci relacji do kanonicznych modów pola, stanu swobodnego i reguły pętlowej w tej reprezentacji. R1b daje algebrę stanów i odczytów; P5 — tomografię lokalną. Żadne z tych nazw samo nie zastępuje lokalności różniczkowego działania, jego rzędu ani tego wyboru stanu.

Kontrola standardowego działania i jego reguł: [Grozin, hep-ph/0508242](https://arxiv.org/abs/hep-ph/0508242), §3.1–3.3. To literatura kontrolna, nie przesłanka ustanawiająca czas i 3D.

## 8. Bilans przyporządkowania

| składnik 256 | co teraz uzasadniono | warunek, który pozostaje |
|---|---|---|
| bloki Diraca i miejsca kinetyki/L↔R | algebra `𝟙,σ`, kowariancja i istniejące przyporządkowanie chiralności | wybór lokalnego, jednogradientowego jądra; funkcje pełnej odpowiedzi |
| licznik i mianownik propagatora fermionowego | jedna odwrotność tej samej macierzy, nie niezależne dane | wartości współczynników oraz rodzaj funkcji Greena |
| minimalny wierzchołek EM | faza końców wiąże jego współczynnik z kinetyką | wybór tej klasy działania; pełna część poprzeczna i jej rachunek |
| tensor propagatora EM | forma poprzeczna z cechowania i kowariancji; odwrotność po ustaleniu cechowania | stałe H wyjściowe w dwupochodnym sektorze i pełna zależność progowa |
| α wobec normalizacji | `α=e₀²/(4πZ_A)`; norma spinora nie daje niezależnego e | znana wartość/funkcja α w zakresie 253, nie wynik z ramy |
| składniki i względne wagi pętli | Wick i rozwinięcie tego samego działania po wyborze reprezentacji/stanu | kanoniczne mody, stan oraz przypisanie ich relacjom |
| pełna waga obiegu | udowodniono, czego nie ustala sam Hessian | reguła wybierająca funkcję, nie tylko jej drugą wariację |

**Werdykt:** uzasadniono zależności między składnikami działania i odtworzono jądra 256 w nazwanej klasie. Mocniejszego wyprowadzenia wyboru tej klasy i pełnego działania z podstawy nie uzyskano. Formalne przesłanki nowej części są jawne, więc jej warunkowy wynik nie awansuje na poziom (3) z 217. Bilans 208, hierarchia Yukaw, grupa cechowania i [104] bez zmiany.

**Następne miejsce pracy w tym kierunku:** na relacjach z 179 wskazać operacyjną regułę, która wybiera kwadratowe jądro i kanoniczną reprezentację modów. Jej test wierności ma postać z 128: pokazać, gdzie zanegowanie reguły narusza konkretne zdanie ramy. „Najprostsze”, „lokalne” bez określenia znaczenia i „dwa stany fotonu” same tej luki nie zamykają. Osobno można badać pełną wagę obiegu; nie trzeba najpierw wyznaczyć wszystkich jej wyższych wariacji, żeby użyć warunkowego wyniku jednej pętli.

## 9. Kontrole

Przed wykonaniem kontroli ustalono powyższe oczekiwania, zakres oraz rodziny diagnostyczne. Kontrole algebraiczne nie stanowią dowodów wyboru działania z ramy. Dowody dla całych parametrów stoją wyżej; przykłady mają sprawdzać znaki, przyporządkowania bloków, granice i deklarowaną różnicę odpowiedzi.

Kod: `jadra-wagi-kontrola-2026-10-09.py`; wynik: `jadra-wagi-kontrola-2026-10-09.json`. Python 3, tylko biblioteka standardowa. **PASS**, całość nad wymiernymi liczbami zespolonymi:

- Zmiana czterech konwencji faz przy końcach, dwa transporty i nierówne wagi 1, 2: dokładna zgodność amplitudy, holonomii oraz znormalizowanego odczytu Borna.
- Trzy nieosobliwe, nierówne chiralne jądra: wzór na odwrotność sprawdzony niezależnie eliminacją Gaussa i wyznacznikiem, z kontrolą mnożenia z obu stron.
- Trzy jądra EM: poprzeczność i odwrotność po ustaleniu cechowania, dla czasopodobnych i przestrzennych argumentów. Dowód dla całego parametru stoi w §4.
- Szesnaście kontroli pełnej tożsamości Wardowskiej, także przy równych niezmiennikach; cztery kontrole granicy diagonalnej z pochodną jądra. Szesnaście kontroli niezerowej swobody poprzecznej. Funkcje użyte w kodzie są syntetyczne, nie fizycznymi funkcjami QED.
- Dwa różne zestawy normalizacji pól dają ten sam parametr η i sprzężenie e.
- Rodzina wag obiegu: ta sama druga wariacja, różne czwarte wariacje i pełne wartości — dokładne współczynniki szeregu, bez losowania równości.
- Ten sam komutator modu, różne korelatory przy dwóch przygotowaniach.

Nie używano danych pomiarowych mas ani dopasowania nowych stałych. Nie przeprowadzono rachunku pełnej odpowiedzi aparatu O, wyboru działania z całej podstawy, drugiej pętli ani `3/2` Yukawy. Wynik nie rozszerza się przez samą zgodność tych kontroli.

