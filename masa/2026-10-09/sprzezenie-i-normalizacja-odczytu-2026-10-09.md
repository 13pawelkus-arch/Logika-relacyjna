# Sprzężenie i normalizacja tego samego odczytu — krok 260

09.10.2026. Kontynuacja 257–259 po doprecyzowaniu celu przez użytkownika: rama ma porządkować istniejącą fizykę aż do miejsca, w którym zmienia sposób prowadzenia formalizmu, a nie tylko nazwy. Źródła projektu: R1a–R1c razem; 179, 206–207, 213, 257–259. Definicje czasu i 3D stanowią podstawę. Nie dodajemy osi czasu ani nowych składników fizycznych.

## Zapis przed rachunkiem i kontrolami

**Spodziewam się:** gdy pełną relację opisujemy tylko przez wybrane kanały odczytu, eliminacja pozostałych kanałów ustala jednocześnie zredukowany propagator, jego sprzężenie EM oraz normalizację. Sprzężenie musi obejmować również przejścia przez kanały wyeliminowane z zapisu. Zredukowany propagator połączony z pozostawionym bez redukcji wierzchołkiem może naruszyć tę zgodność. Zachowana pełna redukcja powinna odtworzyć odpowiedź pierwotnego jądra bez nowych wag.

**Zdanie o upadku:** równość tej konstrukcji z pierwotną odpowiedzią upada, jeśli przy tych samych przygotowaniach i efektach rzut pełnej odpowiedzi z jedną lub dwiema wstawkami EM różni się od odpowiedzi wyprowadzonej przez różniczkowanie całego dopełnienia Schura. Silniejsza teza, że po eliminacji zawsze wystarcza dawny wierzchołek, upada już na jednym dokładnym naruszeniu tożsamości Wardowskiej lub normalizacji pełnego stanu. Nie są to testy wyboru całego działania z ramy.

**Wejścia:** jedna zadana, kowariantna rodzina pełnych jąder \(\mathcal K[a]\), jej podział na podprzestrzenie kanałów \(\mathcal P\oplus\mathcal Q\), oraz przygotowanie i efekt aparatu. Podział zachowuje transformacje fazowe: rzutniki komutują z nimi. a oznacza istniejącą relację EM, a nie zewnętrznego aktora dodanego do całości; różniczkowanie jest sposobem porównania konfiguracji tej relacji. Dla jawnego zastosowania wybieramy kanoniczny, kwadratowy sektor L/R z 257, ze stałym parametrem \(\eta\) i równym ładunkiem EM obu chiralności. Wybór tej rodziny, wartości \(\eta\), stanu pola, reguły pętli i pełnego protokołu pary nie zostaje przez kontrolę wyprowadzony.

**Odczyt:** pełna amplituda między nazwanym przygotowaniem i efektem O, następnie jej porównanie z drugą amplitudą w tym samym protokole. Sam propagator ani pojedynczy wierzchołek nie jest odczytem masy. Eliminacja Q jest eliminacją amplitud w jądrze; nie jest śladem częściowym, utratą informacji ani fizycznym usunięciem jednej chiralności. Nie przypisujemy wnętrza samemu Ø.

**Argumenty:** \(\omega\) i \(\mathbf p\) są częstością fazową i odczytami komplementarnymi odniesionymi do wspólnego wskazania O. \(\omega\) stoi przy \(\mathbb1_2\), a \(\mathbf p\) przy \(\boldsymbol\sigma\). Przykład spektralny jest warunkowy dla nazwanego jednorodnego sektora; nie wyprowadza transformacji Fouriera na całym porządku 179 ani gotowej areny. Zespolone argumenty służą rachunkowi odwrotności; nie wybierają automatycznie korelatora Feynmanowskiego ani stanu.

**Co ma się zmienić w formalizmie:** badamy wspólną redukcję jądra, sprzężenia oraz końców amplitudy. W 257 samo cechowanie ustalało tylko skurcz wierzchołka; w 259 dopełnienie Schura ustalało pełne jądro. Tutaj sprawdzamy, jak ta sama eliminacja przenosi całą zadaną odpowiedź EM, również jej składniki poprzeczne. Nie wyznacza to poprzecznej odpowiedzi nieznanej pełnej rodziny \(\mathcal K[a]\) z samego \(\mathcal K[0]\).

## 1. Jedna redukcja jądra i sprzężenia [T]

Zapiszmy pełne jądro w kanałach P i Q:

\[
\mathcal K[a]=\begin{pmatrix}A[a]&B[a]\\C[a]&F[a]\end{pmatrix},
\qquad R[a]=F[a]^{-1},
\qquad S[a]=A[a]-B[a]R[a]C[a].
\tag{1}
\]

S jest dopełnieniem Schura, nie nowym postulowanym działaniem. Zachowujemy odwrotność F dokładnie, bez obcinania przejść. Gdy odwrotności istnieją, \(G_P=S^{-1}=P\mathcal K^{-1}P\). Eliminacja ma zakres określony przez te odwrotności; osobliwy blok wymaga pełnej odpowiedzi lub jej regularnej granicy.

Pierwsza wariacja całego (1), z \(\delta R=-R\delta F R\), daje

\[
\boxed{\delta S=\delta A-\delta BRC-BR\delta C+BR\delta FR C.}
\tag{2}
\]

Każdy wyraz pochodzi z jednego miejsca tej samej relacji: odczytywanego kanału, wejścia, wyjścia lub propagacji przez Q. Jeżeli \(\delta\mathcal K=-eV\delta a\), wierzchołek zredukowany jest \(V_P=-\delta S/(e\delta a)\). Nie jest to po prostu rzut \(PVP\).

W zapisie z dwoma argumentami, k po stronie wyjścia i p po stronie wejścia:

\[
\boxed{V_P(k,p)=V_A(k,p)-V_B(k,p)R(p)C(p)
-B(k)R(k)V_C(k,p)
+B(k)R(k)V_F(k,p)R(p)C(p).}
\tag{3}
\]

Można to zapisać przez mapy odtwarzające pominiętą amplitudę:

\[
E(p)=\binom{I}{-R(p)C(p)},\qquad
\widetilde E(k)=(I,-B(k)R(k)),
\qquad V_P(k,p)=\widetilde E(k)V(k,p)E(p).
\tag{4}
\]

Dla rzeczywistych argumentów hermitowskiego jądra \(\widetilde E=E^\dagger\). Przy argumentach zespolonych nie zastępujemy jej automatycznie sprzężeniem hermitowskim; zachowujemy podaną analityczną kolejność.

**Dowód pełnej zgodności Wardowskiej.** Z \(\mathcal K(p)E(p)=(S(p),0)^T\) oraz \(\widetilde E(k)\mathcal K(k)=(S(k),0)\), dla wspólnego skalarnego ładunku Q:

\[
q\cdot V=Q[\mathcal K(k)-\mathcal K(p)]
\quad\Longrightarrow\quad
\boxed{q\cdot V_P=Q[S(k)-S(p)].}
\tag{5}
\]

To dokładny dowód na wszystkich argumentach z dziedziny, a nie dobór współczynników po wymaganiu (5). Składnik poprzeczny zadanej pełnej V także przechodzi przez (4). Pełna rodzina \(\mathcal K[a]\), nie samo \(\mathcal K[0]\), jest koniecznym wejściem tego przyporządkowania.

**Kowariancja przy skończonej zmianie faz.** Gdy rzutniki zachowują sektory fazowe, \(\mathcal K\to g\mathcal K g^{-1}\) daje \(S\to g_P Sg_P^{-1}\). Wynika to wprost z transformacji wszystkich czterech bloków. Nie wymaga przypisania współrzędnych węzłom ani uznania nieodczytywalnej fazy końca za cechę nośnika.

## 2. Odpowiedź z przygotowaniem i efektem [T]

Dla końców całkowicie w P mamy

\[
\boxed{G_P(k)V_P(k,p)G_P(p)
=P\mathcal K(k)^{-1}V(k,p)\mathcal K(p)^{-1}P.}
\tag{6}
\]

To pełna odpowiedź z jedną wstawką istniejącej relacji EM. Przy zadanych końcach j i f amplitudą jest \(f^\dagger G_Pj\), a zmianą amplitudy jest odpowiednie \(f^\dagger G_PV_PG_Pj\). Prawdopodobieństwo wymaga następnie całego protokołu i normalizacji. Do surowego G nadal nie stosujemy ograniczenia \(T^\dagger T\preceq I\) z 259.

Jeśli przygotowanie lub efekt ma także składniki w Q, trzeba przenieść również końce. Z dokładnej odwrotności blokowej:

\[
j_{\rm eff}=j_P-BRj_Q,\qquad
f_{\rm eff}^\dagger=f_P^\dagger-f_Q^\dagger RC,
\]
\[
\boxed{f^\dagger\mathcal K^{-1}j
=f_{\rm eff}^\dagger S^{-1}j_{\rm eff}+f_Q^\dagger Rj_Q.}
\tag{7}
\]

Wariant odpowiedzi EM jest wariacją całego (7), również efektywnych końców i ostatniego członu. Gdy fizyczne przygotowanie zależy od zmienianej konfiguracji, jego własna wariacja też pozostaje. Nie można zamienić rzeczywistego aparatu w projektor na L tylko dla wygody rachunku. (6) określa zakres takiego wyboru, a (7) jego pełne rozszerzenie.

## 3. Jawny sektor L/R z 257 [T][P]

Przyjmujemy kanoniczną rodzinę minimalnego wektorowego sprzężenia EM z 257. Po pomnożeniu odwrotnego propagatora Diracowskiego przez stały blok \(\gamma^0\), bez zmiany jego fizycznych zer, otrzymujemy jądro hamiltonowskiej odwrotności:

\[
\mathcal K_0(P)=\begin{pmatrix}L(P)&-\eta I_2\\-\eta I_2&F(P)\end{pmatrix},
\quad L=\omega I_2+\mathbf p\cdot\boldsymbol\sigma,
\quad F=\omega I_2-\mathbf p\cdot\boldsymbol\sigma.
\tag{8}
\]

\(\gamma^0\) zbudowane jest z bloków \(I_2\), a \(\omega\) jest częstością fazową odczytu; nie jest czwartą σ. \(G=\mathcal K_0^{-1}\) jest tutaj odwrotnością jądra hamiltonowskiego. Wybranie konkretnego korelatora kwantowego wymaga jeszcze stanu i odpowiedniej granicy. \(\eta\) jest zadanym bezwymiarowym parametrem masowym, nie wartością wyprowadzoną z relacji.

Eliminując zapis R, dostajemy przy \(s=\omega^2-|\mathbf p|^2\ne0\):

\[
R(P)=F(P)^{-1},\qquad
\boxed{S_L(P)=L(P)-\eta^2R(P)},
\qquad
\boxed{G_L(P)=\frac{\omega I_2-\mathbf p\cdot\boldsymbol\sigma}{s-\eta^2}}.
\tag{9}
\]

Zachowaliśmy obie chiralności w pełnej odpowiedzi. Zniknął tylko jawny blok R w zapisie. Surowa macierz \(G_L\) nie jest ani całym propagatorem Diraca, ani unormowaną amplitudą aparatu.

Niech z wierzchołków wyłączono eQ. W tej bazie

\[
\Gamma_L^0=\Gamma_R^0=I_2,\qquad
\Gamma_L^i=-\sigma_i,\qquad \Gamma_R^i=+\sigma_i,
\]
\[
\boxed{V_L^\mu(k,p)=Q\big[\Gamma_L^\mu+
\eta^2R(k)\Gamma_R^\mu R(p)\big].}
\tag{10}
\]

Przez \(q\cdot V=q_0V^0-\sum_iq_iV^i\) dostajemy dokładnie (5). Drugi człon (10) jest sprzężeniem podczas przejścia przez wyeliminowany z zapisu kanał. Ma tę samą \(\eta\) i tę samą odwrotność F co (9). Nie jest nowym swobodnym sprzężeniem ani dopisaną anomalią magnetyczną.

**Jawny upadek pozostawienia dawnego wierzchołka.** Przy \(\mathbf p=\mathbf k=0\), \(\eta=1\), \(\omega_p=3\), \(\omega_k=4\):

\[
S_L(4)-S_L(3)=\frac{13}{12}I_2,
\quad V_L^0/Q=\frac{13}{12}I_2,
\quad \Gamma_L^0=I_2.
\tag{11}
\]

Zredukowane jądro ze starym wierzchołkiem narusza Wardowskie porównanie o \(I_2/12\). To dokładne naruszenie dla tej samej relacji, nie rezultat przybliżenia ani innej teorii.

**Osobliwa eliminacja.** Przy s=0 odwrotność F nie istnieje. Gdy \(\eta\ne0\), pełna odwrotność \(\mathcal K_0^{-1}\) może wtedy nadal istnieć, a ostatni wzór (9) jest regularny. Trzeba użyć pełnej macierzy lub tej regularnej granicy. Nie dopisywać dodatkowego fizycznego bieguna od samej eliminacji.

## 4. Ta sama relacja ustala normalizację i odczyt ładunku [T][P]

Dla zadanej hermitowskiej, niezależnej od \(\omega\) macierzy H oraz \(\mathcal K=\omega I-H\), odtworzenie pełnego modu ze składowej u w P daje \(\Psi=Eu\). Poza widmem bloku Q:

\[
\boxed{\partial_\omega S=E^\dagger E},\qquad
\boxed{\|\Psi\|^2=u^\dagger(\partial_\omega S)u.}
\tag{12}
\]

Przy blokach H: \(S=\omega I-H_{PP}-H_{PQ}(\omega I-H_{QQ})^{-1}H_{QP}\). Pochodna odwrotności ma znak minus, zatem \(\partial_\omega S=I+H_{PQ}(\omega I-H_{QQ})^{-2}H_{QP}\), dokładnie Gram mapy E. Nie jest to dowolnie dobrany czynnik renormalizacji.

W przykładzie L/R, na rzeczywistej dziedzinie:

\[
N_L(P)=I_2+\eta^2R(P)^2,
\qquad V_L^0(P,P)=QN_L(P).
\tag{13}
\]

Na masowym modzie w spoczynku, \(\omega=\eta>0\), dostajemy \(R=I_2/\eta\), \(N_L=2I_2\), oraz \(\Psi=(u,u)^T\). Przy normalizacji \(u^\dagger N_Lu=1\):

\[
\boxed{u^\dagger V_L^0u=Q},\qquad
u^\dagger Q\Gamma_L^0u=Q/2.
\tag{14}
\]

**Wniosek o formalizmie:** normowanie pełnego modu i wierzchołek jego zredukowanej odpowiedzi są dwoma odczytami tej samej pominiętej amplitudy. Nie wolno stosować pełnej normalizacji razem ze starym sprzężeniem ani normować u oddzielnie jak pełnego stanu. Dla jądra o dodatkowej zależności od częstości lub dla korelatora zależnego od stanu trzeba zachować pełną wariację i odpowiednią normę; nie rozszerzamy (12) bez tych warunków.

## 5. Dwie wstawki i wyznacznik: droga do odpowiedzi EM [T][P]

Nawet gdy pełne (8) zależy liniowo od relacji a, jego zredukowane jądro zawiera \(F[a]^{-1}\), więc ma ustalone wyższe wariacje. Oznaczając \(W_L^{\mu\nu}=-\delta_\mu\delta_\nu S_L/e^2\), przy liniowej pełnej rodzinie otrzymujemy jako operator, z zachowanymi splotami argumentów:

\[
\boxed{W_L^{\mu\nu}=Q^2\eta^2\big[
R\Gamma_R^\mu R\Gamma_R^\nu R+
R\Gamma_R^\nu R\Gamma_R^\mu R\big].}
\tag{15}
\]

To kontakt dwóch wstawek EM w opisie zredukowanym, wymuszony przejściami przez R. Pełny pierwotny sektor Diraca nie zyskuje nowego swobodnego członu \(A^2\). Przy tej samej rodzinie:

\[
\frac{\delta_1\delta_2G_L}{e^2}
=G_LV_1G_LV_2G_L+G_LV_2G_LV_1G_L+G_LW_{12}G_L.
\tag{16}
\]

Przykładowo jedna uporządkowana część ostatniego członu między k i p, z argumentem pośrednim l, ma jądro \(Q^2\eta^2R(k)\Gamma_R^\mu R(l)\Gamma_R^\nu R(p)\). Razem z sekwencją dwóch zredukowanych wierzchołków daje dokładnie rzut pełnego \(G(k)V^\mu G(l)V^\nu G(p)\). Obie kolejności trzeba zachować. „Dwie wstawki” nie oznaczają dwóch pętli.

**Zamknięty rachunek fermionowy.** Przy dodatkowo przyjętej regule gaussowskiego całkowania fermionów w kanonicznym działaniu, redukcja zachowuje także wyznacznik:

\[
\boxed{\det\mathcal K[a]=\det F[a]\,\det S_L[a].}
\tag{17}
\]

W skończonym rachunku macierzowym jest to dokładna tożsamość. Dla funkcjonalnego wyznacznika stosuje się ten sam regulator i przygotowanie w całej konstrukcji; rozdzielonych składników chiralnych nie wolno ogłaszać samodzielnie poprawnymi teoriami cechowania. Różnica \(\operatorname{Tr}\ln\mathcal K[a]-\operatorname{Tr}\ln\mathcal K[0]\) zachowuje zależny od a wkład \(\operatorname{Tr}\ln F\). Nierozróżnialność tła od strony O nie zeruje tej różnicy.

Pomijając wspólny znak oraz czynnik e² właściwe dla konwencji działania kwantowego, dwie wariacje logarytmu wyznacznika dają:

\[
\boxed{\operatorname{Tr}(GV_1GV_2)
=\operatorname{Tr}(RV_{R1}RV_{R2})
+\operatorname{Tr}(G_LV_{L1}G_LV_{L2})
+\operatorname{Tr}(G_LW_{L12}).}
\tag{18}
\]

Dowód: \(\delta\ln\det X=\operatorname{Tr}(X^{-1}\delta X)\), \(\delta_1\delta_2\ln\det X=\operatorname{Tr}(X^{-1}\delta_1\delta_2X-X^{-1}\delta_1X X^{-1}\delta_2X)\), a następnie (17), \(\delta_1\delta_2\mathcal K=0\), \(\delta_1\delta_2F=0\) i definicja W. Ślad obejmuje wszystkie odpowiednie kanały i argumenty; nie wyrzucamy części urojonych.

Przy syntetycznym \(\omega=3\), \(\mathbf p=0\), \(\eta=1\), dla dwóch wstawek normujących i po wyjęciu wspólnego Q², macierzowy współczynnik wynosi:

\[
\frac58=\underbrace{\frac29}_{\det F}
+\underbrace{\frac{25}{72}}_{\text{dwa wierzchołki zredukowane}}
+\underbrace{\frac1{18}}_{\text{kontakt z redukcji}}.
\tag{19}
\]

Pozostawienie samego \(\det S_L\) daje \(29/72\) zamiast \(5/8\). To współczynnik wariacji macierzowego wyznacznika, **nie prawdopodobieństwo i nie policzona fizyczna polaryzacja próżni**. W pełnym rachunku EM wszystkie trzy składniki należą do jednej odpowiedzi. Przy obliczeniu α nie wolno przypisać wyeliminowanemu kanałowi wagi zero.

## 6. Co zostało ustalone i gdzie jest następny krok

| Pytanie | Wynik 260 |
| --- | --- |
| Co przenosi eliminacja kanałów? | Całe zadane sprzężenie (3)–(4), jego wyższe wariacje, końce (7) i odpowiednią normalizację. Nie tylko mianownik propagatora. |
| Co dzieje się z poprzeczną częścią wierzchołka? | Zadana pełna część zostaje przeniesiona. Niezadanej części nie wybiera samo cechowanie ani jądro przy a=0. |
| Czy trzeba dołożyć nowe wagi po redukcji? | Nie przy ustalonej pełnej rodzinie. Wagi wynikają z odwrotności i wariacji tej rodziny. |
| Czy sprzężenie przez kanał R można pominąć w przykładzie L/R? | Nie: dokładne naruszenie Wardowskie (11), błędne Q/2 (14), brak wkładu w zamkniętej odpowiedzi (19). |
| Czy wybrano kanoniczne działanie, stan i η z podstawy? | Nie. Konstrukcja porządkuje jednoznaczne użycie zadanej rodziny oraz odrzuca niespójne redukcje. |
| Czy wykonano pełny protokół 215, polaryzację próżni lub masowy rachunek drugiego rzędu? | Nie. Kontrole obejmują pełne macierzowe odpowiedzi i wstawki; nie całki pętlowe ani rzeczywisty aparat. |

To **konkretny krok w formalizmie istniejącej fizyki**: zastępowanie pełnej relacji jej częściowym zapisem odczytu jest jedną operacją na jądrze, sprzężeniu, normalizacji, końcach i — gdy stosujemy gaussowską regułę — wyznaczniku. Nie można zmienić tylko jednego z nich i uważać, że wciąż opisujemy tę samą relację. R1a–R1c i 206 określają, dlaczego interesuje nas właśnie taki pełny odczyt; algebra nie zmienia znanych praw QED.

Nie nazywamy samych tożsamości Schura, Wardowskich ani różniczkowania odwrotności nowym twierdzeniem fizycznym. Nie usunięto niezależnego parametru masowego lub sprzężenia z całej teorii. **Zmiana względem 257–259 jest konstruktywna:** mamy teraz jawny przepis przeniesienia EM do pełnego zredukowanego jądra L/R i test, który wykrywa użycie niepasujących wag.

**Następny krok w tej gałęzi:** zastosować wspólną wariację i redukcję do samouzgodnionego jądra pełnej odpowiedzi masowej oraz przygotowań/efektów konkretnego O. Warunki biegunowe, residua, sprzężenie i przejście A/B muszą pochodzić z tej samej rodziny. To zadanie jest odrębne od nadal otwartego wyboru pełnej rodziny relacji i wartości stosunków Yukaw z ramy. Nie wracamy do ustanawiania czasu i 3D ani do zakazu globalnego zera.

## 7. Kontrole i literatura

Skrypt `sprzezenie-i-normalizacja-kontrola-2026-10-09.py` używa wyłącznie biblioteki standardowej Python 3. Dokładne zespolone liczby wymierne zachowują σ₂ i części urojone. Cztery parametry η: 0, 1/3, 1, 2; cztery punkty z pełnym wektorem p, w tym zespolona częstość. Dane są syntetyczne, bez dopasowania do mas pomiarowych. Dowody na całych dziedzinach podano wyżej; kontrole wykrywają błędy realizacji wzorów.

| Kontrola | Zakres |
| --- | --- |
| Pełna odwrotność 4×4 wobec redukcji 2×2 | 16 przypadków; także jawny licznik i mianownik (9) |
| Ward przy skończonej różnicy argumentów | 64 pary, wszystkie cztery składowe; pełne i zredukowane jądro |
| Pełna odpowiedź z jedną wstawką | 256 porównań niezależnej odwrotności 4×4 z (6) |
| Dwie uporządkowane wstawki z różnymi argumentami | 256 porównań, wszystkie 16 par typów składowych; pełna propagacja i kontakt |
| Dowolne końce w obu sektorach | 16 pełnych amplitud (7) |
| Wierzchołki z niezerowymi blokami mieszającymi | 16 porównań (3)–(6) |
| Skończona zmiana faz końców | Kowariancja jądra i jego pełnej odwrotności |
| Norma i ładunek na modach masowych | 8 przygotowań, cztery wektory p i dwie składowe spinorowe; odtworzenie całego modu |
| Wyznacznik i zamknięte dwie wstawki | 16 faktoryzacji; 256 macierzowych współczynników (18), bez całkowania pętli |
| Dokładne niezgodności | Ward: 1/12; ładunek: Q/2; wyznacznik bez F: 29/72 zamiast 5/8 |
| Granice | 64 wierzchołki przy η=0; s=0: osobliwa eliminacja i regularna pełna odpowiedź |

Źródło narzędzia [L]: A. N. Kvinikhidze, B. Blankleider, [Gauging hadronic systems](https://arxiv.org/abs/nucl-th/9710039), Nucl. Phys. A 631, 559–563 (1998), [DOI](https://doi.org/10.1016/S0375-9474(98)00067-0). Dostępny abstrakt opisuje sprzęganie fotonu ze wszystkimi częściami równania i zachowanie prądu; metoda ma więc znany odpowiednik. Pełnego tekstu nie pobrano w tym kroku. Równania (1)–(19) wyprowadzono jawnie w notatce i sprawdzono niezależnymi odwrotnościami, bez przenoszenia hadronowego modelu ani jego interpretacji czasoprzestrzeni do ramy. Porównanie z tą metodą nie jest potwierdzeniem pierwszeństwa lub odrębności wyniku projektu.

**Status kontroli:** po wykonaniu pełnego skryptu — PASS, bez tolerancji numerycznej. Wyniki zapisane w `sprzezenie-i-normalizacja-kontrola-2026-10-09.json`.
