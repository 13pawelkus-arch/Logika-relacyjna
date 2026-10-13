# α i masa z tego samego widma EM — krok 261

09.10.2026. Kontynuacja 254–260 po pytaniu „Wracamy do alfa?” i poleceniu „Ok zaczynaj”. Pracujemy na kanonicznym, wektorowym sektorze L/R określonym w 257 i 260. Definicje czasu i 3D oraz granica mówienia o Ø pozostają przyjętą podstawą.

## Zapis przed rachunkiem i kontrolami

**Spodziewam się:** dwie wariacje pełnego wyznacznika L/R odtworzą fermionową polaryzację próżni i pełny próg z 254–255. Eliminacja kanału zachowa tę odpowiedź dopiero wraz z wyznacznikiem R i kontaktem dwóch wstawek. To samo spektralne EM, bez niezależnej nowej wagi, będzie zasilało wkład z jedną wstawką polaryzacji do własnej energii. Porównanie dwóch nośników o jednakowym ładunku powinno usuwać wspólny lokalny wkład UV, zachowując skończoną zależność od stosunków progów.

**Zdanie o upadku przyporządkowania:** dla tej samej rodziny, stanu, regulatora i odejmowania redukcja L/R daje inną pełną polaryzację niż nieredukowany Dirac; albo ta sama waga spektralna nie odtwarza skończonej różnicy masowych projekcji wstawki. Niezgodność pełnych reprezentacji, części urojonej lub granic odrzuca ten rachunek. Zgodność nie wyprowadza wyboru QED z podstawy.

**Wejścia:** kanoniczna minimalna rodzina wektorowego QED z 257; znormalizowana próżnia i korelator Feynmanowski; wspólny regulator zachowujący przesunięcia i tożsamości wektorowe; dodatnie masy kanałów; ładunki i ich krotności; α odczytana przy zerowym transferze, używana jako nazwana dana renormalizacyjna zgodnie z 253. Wszystkie argumenty masowe i spektralne są ilorazami względem tego samego odniesienia O. Nie wyprowadzamy kanonicznego działania, przygotowania, reguły pętli ani wartości mas.

**Odczyt i zakres:** efektywna odpowiedź EM z wydzielonym wkładem fermionowym oraz perturbacyjne przejście parametrów masowych A/B. To nie jest jeszcze pełny protokół aparatu z 215. W drugim rzędzie rozpatrujemy sektor jednej renormalizowanej fermionowej wstawki polaryzacji, nie cały dwupętlowy SM. A oznacza parametr na powłoce, B masę MS-bar przy wspólnym argumencie; sprzężenie α będzie jawnie uzgodnione z jego schematem.

**Co ma się zmienić:** zamiast przypisywać osobno wagę do biegu α i do masowej wstawki, szukamy jednego jawnego funkcjonału tej samej odpowiedzi. Odtworzenie znanych funkcji jest kontrolą. Wynik nie zostanie nazwany wyborem hierarchii ani usunięciem wolnego parametru, jeżeli tych wniosków rachunek nie wymusi.

## 1. Wynik i jego zakres

**[T][L] w zadanym wektorowym QED:** pełne widmo fermionowej odpowiedzi EM ustala zarówno próg efektywnej α, jak i skończoną różnicę masowych projekcji jednej wstawki polaryzacji. Otrzymaliśmy jawny funkcjonał, z ustaloną wagą i argumentem:

\[
\Delta_{ij}^{\mathrm{VP},0}
=-\frac{Q^2}{4\pi}
\int_{m_j^2}^{m_i^2}\frac{du}{u}
\int_0^1 dx\,(4-2x)\,
\delta\alpha_f\!\left(\sqrt{u}\frac{1-x}{\sqrt{x}}\right).
\tag{1}
\]

Tu Q jest wspólnym ładunkiem porównywanych nośników, a \(\delta\alpha_f\) jest jednopętlową zmianą efektywnego sprzężenia względem \(\alpha_0\), rzędu \(\alpha_0^2\). Masy w granicach są parametrami B w wiodącym rzędzie. Nie są nowymi zmiennymi swobodnymi wstawki. Pełne progi pozostają w funkcji \(\delta\alpha_f\).

To związek **wkładu do przejścia A/B**, a nie nowe równanie RG ani wyprowadzenie hierarchii. Zmienna u porównuje masowe projekcje dwóch kanałów. Nie jest rozdzielczością renormalizacji ani zewnętrznym czasem. Sama α w jednym punkcie nie wystarcza do obliczenia (1).

## 2. Pełny wyznacznik L/R i polaryzacja

Rodzinę z 260 zapisujemy jako

\[
\mathcal K[a]=
\begin{pmatrix}L[a]&-mI_2\\-mI_2&F[a]\end{pmatrix},
\quad R[a]=F[a]^{-1},\quad S_L[a]=L[a]-m^2R[a].
\]

Różniczkujemy **wspólną regularyzowaną konstrukcję**. Nie przypisujemy obu wyznacznikom osobnych teorii lub osobnych stanów:

\[
\ln\det\mathcal K=\ln\det F+\ln\det S_L.
\tag{2}
\]

Dwie wariacje dają sumę z 260:

\[
\operatorname{Tr}(GV_1GV_2)=
\operatorname{Tr}(RV_{R1}RV_{R2})
+\operatorname{Tr}(G_LV_{L1}G_LV_{L2})
+\operatorname{Tr}(G_LW_{L12}).
\tag{3}
\]

Są tu wyznacznik R, dwa pełne zredukowane wierzchołki i kontakt dwóch wstawek. Ich suma odtwarza nieredukowaną pętlę Diraca **przed całkowaniem**. Nie wystarczy zachować samego \(G_L\), a wyznacznik R nie ma wagi zero.

W swobodnym jednorodnym zapisie \(s=\omega^2-|\mathbf p|^2\):

\[
\det F=s,\qquad \det S_L=\frac{(s-m^2)^2}{s},
\qquad \det\mathcal K=(s-m^2)^2.
\tag{4}
\]

Osobliwość s=0 w rozdzielonych blokach znosi się w całości. Nie jest dodatkowym fizycznym kanałem. To samo zachowanie całości jest potrzebne do poprawnego progu odpowiedzi EM.

Macierze Diraca są zbudowane z bloków \(\mathbb1_2,\sigma_i\) jak w 256. Dla jednej pary L/R:

\[
\operatorname{tr}\!\left[
\Gamma^\mu(\slashed k+m)
\Gamma^\nu(\slashed k+\slashed q+m)\right]
=4\!\left[k^\mu(k+q)^\nu+k^\nu(k+q)^\mu
-g^{\mu\nu}\{k\cdot(k+q)-m^2\}\right].
\tag{5}
\]

Po połączeniu propagatorów i przesunięciu \(\ell=k+yq\) mamy \(\Delta=m^2-y(1-y)q^2\). Dla wspólnie regularyzowanych całek \(I_2=\int(\ell^2-\Delta+i0)^{-2}\):

\[
\int\frac{\ell^2}{(\ell^2-\Delta+i0)^2}
=\frac{d\Delta}{d-2}I_2.
\]

Współczynnik przy \(g^{\mu\nu}\) w (5), po całkowaniu części tensorowej, zawiera dokładnie

\[
\left(\frac2d-1\right)\frac{d\Delta}{d-2}
+m^2+y(1-y)q^2=2y(1-y)q^2.
\]

Razem z drugim członem daje tensor poprzeczny. **Waga \(y(1-y)\) wynika z licznika i produktu propagatorów.** Czynnik 4 jest śladem amplitud pary L/R; nie jest czwartym kierunkiem komplementarnym. Symbol d kontroluje regulator sumy po modach przyjętej reprezentacji QED; podstawy czasu i 3D z R1a–R1c nie zmieniamy.

## 3. Cała funkcja, progi i część urojona

Ustalamy znak skalara przez poprzeczny propagator proporcjonalny do \(1/[q^2(1+\Pi_R(q^2))]\). Przy \(\Pi_R(0)=0\) dla kanału f:

\[
\Pi_{R,f}(q^2)=\frac{\alpha_0c_f}{\pi}
\Phi\!\left(\frac{q^2}{m_f^2}\right),
\quad c_f=N_cQ_f^2,
\quad
\Phi(z)=-2\int_0^1dy\,y(1-y)
\ln[1-z\,y(1-y)-i0].
\tag{6}
\]

Wszystkie m, q, \(\sqrt{s}\) i \(\omega,\mathbf p\) w tej notatce oznaczają ilorazy względem wspólnego odniesienia fazowego O. Zero w \(\Pi_R(0)\) jest zerowym transferem w warunku odejmowania; nie jest globalnym zerem generatora ani zerem absolutnym z dyskusji R1a.

Dla przestrzeniopodobnego transferu \(q^2=-q_E^2\) otrzymujemy:

\[
\Phi(-r)=-F_\gamma(r),\qquad
F_\gamma(r)=2\int_0^1dy\,y(1-y)
\ln[1+r\,y(1-y)].
\tag{7}
\]

Stąd w jednym rzędzie polaryzacji:

\[
\left[\frac1{\alpha_{\rm eff}(q_{E,1})}
-\frac1{\alpha_{\rm eff}(q_{E,2})}\right]_{\rm ferm}
=-\frac1\pi\sum_f c_f
\left[F_\gamma\!\left(\frac{q_{E,1}^2}{m_f^2}\right)
-F_\gamma\!\left(\frac{q_{E,2}^2}{m_f^2}\right)\right].
\tag{8}
\]

To pełny próg z 254–255, teraz wyprowadzony z zachowanej pętli L/R. W małym r: \(F_\gamma=r/15-r^2/140+\ldots\). Przy dużym r: \(F_\gamma=\tfrac13\ln r-\tfrac59+o(1)\). Tych granic nie podstawiamy do całej funkcji.

Nad progiem \(s\ge4m_f^2\) przecięcie logarytmu daje:

\[
\rho_f(s):=\frac1\pi\operatorname{Im}\Pi_{R,f}(s+i0)
=\frac{\alpha_0c_f}{3\pi}\mathcal R_f(s),
\quad
\mathcal R_f(s)=
\sqrt{1-\frac{4m_f^2}{s}}\left(1+\frac{2m_f^2}{s}\right)
\Theta(s-4m_f^2).
\tag{9}
\]

Przedział parametru y z ujemnym argumentem logarytmu to \([(1-\beta)/2,(1+\beta)/2]\). Całka po tym przedziale daje (9), a nie dowolną liczbę aktywnych stanów. Zachowana odpowiedź ma reprezentację:

\[
\Pi_R(q^2)=q^2\int_0^\infty
\frac{\rho(s)\,ds}{s(s-q^2-i0)},\qquad
\rho(s)=\sum_f\rho_f(s).
\tag{10}
\]

Normalizacja, znak oraz pełna część urojona zgadzają się z [Laporta–Jentschura, (26)–(29)](https://arxiv.org/abs/2403.07127). Używamy ich jednopętlowej funkcji do kontroli. Nie wykonaliśmy ich dwupętlowej polaryzacji.

## 4. To samo widmo we własnej energii

Jedna renormalizowana wstawka polaryzacji jest poprzeczna. Z (10):

\[
-\frac{\Pi_R(k^2)}{k^2}
=\int_0^\infty\frac{\rho(s)}s
\frac{ds}{k^2-s+i0}.
\tag{11}
\]

Ta tożsamość ustala całą wagę wstawki. Operator własnej energii można więc zapisać jako sumę jednopętlowych odpowiedzi z mianownikiem \(k^2-s+i0\) i pełnym rzutnikiem poprzecznym \(g_{\mu\nu}-k_\mu k_\nu/k^2\). Własna energia pojedynczego nośnika wymaga wspólnej regularyzacji i odjęcia masowego; osobne całkowanie jej części po s do nieskończoności nie jest skończonym odczytem.

Na zewnętrznych spinorach na powłoce część podłużna pomocniczego licznika nie przesuwa parametru masowego. Dowód zachowuje propagator:

\[
X=\slashed p-m,\quad Y=\slashed p-\slashed k-m,
\quad
\slashed kY^{-1}\slashed k=XY^{-1}X-X-\slashed k.
\]

Po projekcji \(Xu=0,\bar uX=0\) zostaje nieparzysty człon w k, którego wspólnie regularyzowana całka znika. **Poza powłoką i przy residuum pozostaje pełna część podłużna**; nie usuwamy jej z operatora.

Masową projekcję można zatem policzyć przez licznik wektorowy z 256. Dla parametru x ważącego mianownik fotonowy:

\[
\Delta_i(x,s)=xs+(1-x)^2m_i^2,\qquad
w_m(x)=4-2x.
\]

W regularyzacji wymiarowej człon licznika to
\(4-2x+2\epsilon(x-1)\). Po odjęciu wspólnego UV jednopętlowy pomocniczy współczynnik ma postać:

\[
C_i^{(1)}(s;\mu)
=\frac{\alpha_0Q_i^2}{4\pi}
\left[
\int_0^1dx\,(4-2x)\ln\frac{\mu^2}{xs+(1-x)^2m_i^2}-1
\right].
\tag{12}
\]

Stała −1 pochodzi z \(\epsilon\) razy biegun, jak w 214 i 256. Przy s=0 dostajemy dokładnie \(4+3\ln(\mu^2/m_i^2)\), nie 5. Różnica poniżej usuwa ten wspólny składnik i wspólny kontrczłon masowy.

## 5. Skończona różnica dwóch masowych odczytów

Dla **jednakowych ładunków** \(Q_i=Q_j=Q\), tej samej α i tej samej sumy kanałów f:

\[
\boxed{
\Delta_{ij}^{\mathrm{VP},0}
=\frac{\alpha_0^2Q^2}{12\pi^2}
\sum_f c_f
\int_{4m_f^2}^\infty\frac{ds}{s}\mathcal R_f(s)
\int_0^1dx\,(4-2x)
\ln\frac{xs+(1-x)^2m_j^2}
{xs+(1-x)^2m_i^2}.}
\tag{13}
\]

To wkład jednej fermionowej pętli w fotonie do
\(\ln(M_i/m_i)-\ln(M_j/m_j)\), gdzie \(M_i\) jest parametrem A na powłoce, a \(m_i=m_{B,i}(\mu)\). Równość ładunków jest konieczna do usunięcia wspólnego UV w tej prostej postaci. Pozostała lokalna renormalizacja masowa jest wspólna i znosi się w różnicy. Odjęcie polaryzacji przy zerowym transferze obejmuje również odpowiedni kontrczłon ładunku.

Dla ustalonego x>0 logarytm w (13) maleje jak 1/s. Po całkowaniu po x jest \(O(\ln s/s)\); wraz z ds/s daje zbieżny ogon \(O(\ln s/s^2)\). W dolnej granicy \(\mathcal R_f\) znika jak pierwiastek. Wszystkie masy są dodatnie, więc różnica jest skończona bez samego cięcia.

Przy
\[
r=\frac{m_i}{m_j},\qquad z_f=\frac{m_f}{m_j},\qquad t=\frac{s}{m_j^2}
\]
cały wynik jest funkcją stosunków:

\[
\Delta_{ij}^{\mathrm{VP},0}
=\frac{\alpha_0^2Q^2}{12\pi^2}\sum_f c_f\mathcal H(r,z_f),
\]
\[
\mathcal H(r,z)=
\int_{4z^2}^\infty\frac{dt}{t}
\sqrt{1-\frac{4z^2}{t}}\left(1+\frac{2z^2}{t}\right)
\int_0^1dx\,(4-2x)
\ln\frac{xt+(1-x)^2}{xt+r^2(1-x)^2}.
\tag{14}
\]

W szczególności \(\mathcal H(1,z)=0\), a dla r>1 jest ściśle ujemna przy niepustym dodatnim widmie. Wymiana zewnętrznych kanałów zmienia znak po przeskalowaniu z. Różnice dla trzech zewnętrznych mas składają się dokładnie. Odpowiedź zależy też od \(z_f\): sam \(R_B=r\) nie określa przejścia, zgodnie z 214.

Przykład syntetyczny r=2, z=1 daje \(\mathcal H=-2{,}5786332130675\). Przy r=2 i z=4 jest \(-0{,}4535757942621\). Wstawka ma tę samą wagę ładunku, a różni się przez próg. Liczby nie są dopasowaniem do leptonów.

## 6. Jawny funkcjonał tej samej α

Ze wspólnego widma:

\[
F_\gamma(q_E^2/m_f^2)
=\frac{q_E^2}{3}
\int_{4m_f^2}^\infty
\frac{\mathcal R_f(s)\,ds}{s(s+q_E^2)}.
\tag{15}
\]

Rozpisujemy logarytm z (13):

\[
\ln\frac{xs+(1-x)^2m_j^2}{xs+(1-x)^2m_i^2}
=-\int_{m_j^2}^{m_i^2}\frac{du}{u}
\frac{q_x^2(u)}{s+q_x^2(u)},
\quad q_x^2(u)=u\frac{(1-x)^2}{x}.
\tag{16}
\]

Po zastosowaniu (15) i zachowaniu kolejności odjęcia:

\[
\mathcal H(r,z)
=-3\int_1^{r^2}\frac{du}{u}
\int_0^1dx\,(4-2x)
F_\gamma\!\left(\frac{u(1-x)^2}{xz^2}\right).
\tag{17}
\]

Jednopętlowa zmiana efektywnego sprzężenia, rozwinięta do rzędu potrzebnego we wstawce, to

\[
\delta\alpha_f(q_E)
=\frac{\alpha_0^2}{\pi}\sum_f c_f
F_\gamma(q_E^2/m_f^2).
\tag{18}
\]

Równania (17)–(18) dają (1). Nie zamieniamy pełnej funkcji na logarytm ani nie wstawiamy resummowanej α poza ustalony rząd. Wprowadzając **nazwaną, znormalizowaną średnią tej odpowiedzi**

\[
\bar\alpha_f(M)
=\frac13\int_0^1dx\,(4-2x)
\left[\alpha_0+
\delta\alpha_f\!\left(M\frac{1-x}{\sqrt{x}}\right)\right],
\tag{19}
\]

można połączyć jednopętlowy EM i sektor VP:

\[
\boxed{
\left[\ln\frac{R_A}{R_B}\right]_{\text{jedna pętla EM + jedna VP}}
=-\frac{3Q^2}{2\pi}
\int_{m_j}^{m_i}\frac{dM}{M}\,\bar\alpha_f(M).}
\tag{20}
\]

Waga całki x jest dodatnia i ma całkę 3; jej argument jest ustalony przez dokładne mianowniki. W granicy pominięcia VP równanie (20) odtwarza
\(-3\alpha_0Q^2\ln R_B/(2\pi)\) z 214. To identyczność wybranych sektorów, **nie pełny drugi rząd**.

Formalizm zmienia się w konkretnym miejscu: **masowa wstawka nie ma osobnej dowolnej wagi względem α**. Zadaną pełną odpowiedź EM przepuszczamy przez ustalony funkcjonał. Sama liczba α(q*) nie zawiera tej informacji. Funkcja α obliczona z włożonych mas, a następnie użyta do odczytania tych samych mas, nadal nie jest ich wyprowadzeniem.

### Dlaczego nie wystarcza jedna uniwersalna rozdzielczość α

Argument \(q_x\) w (19) biegnie od 0 do nieskończoności. Nawet dla pojedynczego kanału nie istnieje stała κ, która zastępuje całą średnią przez \(F_\gamma(\kappa M^2/m_f^2)\) dla wszystkich stosunków. Dla a=\(M^2/m_f^2\):

\[
\frac13\int_0^1dx\,(4-2x)F_\gamma\!\left(a\frac{(1-x)^2}{x}\right)
=\begin{cases}
\dfrac{4a}{45}\ln(1/a)+O(a),&a\to0^+,\\[4pt]
\dfrac13\ln a-\dfrac{13}{18}+o(1),&a\to\infty.
\end{cases}
\tag{21}
\]

Pierwszy logarytm pochodzi z przedziału a≲x≲1, gdzie \(F_\gamma\simeq a(1-x)^2/(15x)\); część x≲a daje \(O(a)\). Druga granica używa
\(\int w_m dx=3\),
\(\int w_m\ln(1-x)dx=-5/2\),
\(\int w_m\ln x\,dx=-7/2\).
Stałe κ mogłoby dopasować drugą granicę (\(\ln\kappa=-1/2\)), lecz \(F_\gamma(\kappa a)\sim\kappa a/15\) nie ma pierwszego logarytmu. Zastąpienie średniej jednym punktem wymaga zatem dodatkowo wskazanego przybliżenia i zakresu.

Wektorowy QED w tym kroku jest zadaną rodziną na całym zakresie całki. Dane α tylko na ograniczonym przedziale nie ustalają całego funkcjonału. Przy przejściu do rzeczywistego zespołu SM trzeba uwzględnić dopasowanie elektrosłabe oraz pełną odpowiedź hadronową, zamiast przedłużać swobodne progi kwarkowe przez obszar nieperturbacyjny.

## 7. Uzgodnienie α z masowym schematem B

Dotąd używaliśmy \(\alpha_0\), czyli ładunku określonego przy zerowym transferze, oraz mas B w MS-bar przy wspólnym μ. Dla zadanego pełnego fermionowego QED jednopętlowe przejście sprzężenia jest:

\[
\alpha_B(\mu)=\alpha_0+
\frac{\alpha_0^2}{3\pi}
\sum_fc_f\ln\frac{\mu^2}{m_f^2}
+O(\alpha_0^3).
\tag{22}
\]

To odtworzenie [Grozin, §6.4, (6.40)](https://arxiv.org/abs/hep-ph/0508242), przy wspólnej definicji parametrów. Różnicę masową (13) trzeba uzgodnić z tą samą zmianą w jednopętlowym członie \(-3\alpha Q^2\ln r/(2\pi)\):

\[
\boxed{
\Delta_{ij}^{\mathrm{VP},B}=
\frac{\alpha_B^2Q^2}{12\pi^2}
\sum_f c_f\left[
\mathcal H(r,z_f)+6\ln r\ln\frac{\mu^2}{m_f^2}
\right].}
\tag{23}
\]

Różnica między (13) i (23) nie jest nowym sprzężeniem. Jest tym samym kontrczłonem ładunku użytym także w masowym rachunku. Przy
\(d\alpha_B/d\ln\mu=2\alpha_B^2\sum c_f/(3\pi)\)
pochodna jednopętlowego masowego członu znosi jawną pochodną (23). Sprawdzono dokładnie anulowanie wspólnego μ w tym fermionowym sektorze.

W granicy \(z_f\to0\), przy ustalonym r:

\[
\mathcal H(r,z_f)
=-6\ln r\ln(1/z_f^2)-6(\ln r)^2+13\ln r+o(1).
\tag{24}
\]

Po (22)–(23) zostaje
\(6\ln r\ln(\mu^2/m_j^2)-6(\ln r)^2+13\ln r\).
Dokładnie odpowiada różnicy znanych logarytmicznych współczynników
\(-13L/24-L^2/8\) sektora fermionowej pętli, gdzie \(L=\ln(\mu^2/m^2)\), w jednostkach \(\alpha_B^2Q^2c_f/\pi^2\). Kontrola: [Burnier i in., JHEP 11 (2017) 206, (3.9)](https://arxiv.org/abs/1709.07612), po wydzieleniu części \(C_FT_FN_f\), odwróceniu relacji masowej i przekładzie tego samego fermionowego grafu do wektorowego QED. Nie przenosimy ich modelu termicznego ani pozostałych wkładów QCD.

Stała −5/9 w (7) oraz stała −1 z licznika w (12) pozostają. Stała 4 z 214 nie została zmieniona. Małą masę wewnętrzną stosujemy wyłącznie jako kontrolę (24), a nie zastępstwo pełnego progu w (13).

## 8. Co zostało związane, a co pozostaje wejściem

| Pytanie | Wynik 261 |
| --- | --- |
| Czy pełna polaryzacja pochodzi z zachowanego L/R? | Tak, w kanonicznym sektorze z 257: (2)–(8), w tym wyznacznik R i kontakt. |
| Czy dwie wagi — α i masowej wstawki — trzeba podać osobno? | Nie po zadaniu tej samej rodziny i widma: (13), (17), (1) i (20) ustalają przyporządkowanie. |
| Czy zwykła wspólna jednopętlowa część cechowania wybiera hierarchię? | Nie. Dotychczasowy wynik 152, 217, 254 i 256 pozostaje. |
| Czy pełny próg wnosi zależność do przejścia dwóch jednakowo naładowanych mas? | Tak, (14) zależy od r oraz progów \(z_f\). Nie sprowadza się do jednej stałej α. |
| Czy uzyskaliśmy dodatkowy warunek wyznaczający r? | Nie. (20) jest zgodnym przejściem A/B dla zadanych parametrów, nie równaniem wybierającym ich wartości. |
| Czy samo \(R_B\) wystarcza do przejścia? | Nie. Potrzebna jest relacja z resztą widma, zgodnie z 214. |
| Czy mamy pełny drugi rząd i pełną α SM? | Nie. Policzyliśmy jedną fermionową VP we własnej energii oraz jej dopasowanie do α MS-bar. Pozostałe grafy, iteracja warunku masowego, inne sektory i protokół O pozostają. |
| Czy wybór działania, modów lub stanu wynika teraz z R1a–R1c? | Nie. Granica 257 i 260 bez zmiany. |

**Test z 191: co pozwala albo zabrania ten krok?** Pozwala obliczyć cały skończony sektor VP różnicy masowej z tej samej pełnej odpowiedzi EM i jawnych argumentów. Zabrania dobierania niezależnej wagi tej wstawki przy zachowaniu α, usuwania wyznacznika R/kontaktu oraz przedstawiania jednego podstawienia biegnącej α jako całego drugiego rzędu. Bilans wolnych danych z 208 nie maleje. Nie wyprowadzono hierarchii, grupy, liczby pokoleń ani 3/2 Yukawy.

**Następne miejsce:** dołączyć pozostały dwupętlowy wkład wektorowego QED do przejścia A/B z tego samego samouzgodnionego jądra. Zachować kinetykę, masę, iterację warunku na powłoce i dopasowanie α; sprawdzić, które związki pochodzą z działania, a które mogłyby być dodatkowym warunkiem z ramy. Potem uzgodnić z resztą zespołu elektrosłabego/hadronowego. Sam zamknięty przepis na zmianę parametrów nie stanowi jeszcze takiego warunku.

## 9. Kontrole

Samodzielny skrypt alfa-masa-kontrola-2026-10-09.py używa dokładnych zespolonych ułamków dla algebry oraz NumPy/SciPy dla całek. Dane są syntetyczne. Wynik: **PASS**.

| Kontrola | Zakres i wynik |
| --- | --- |
| Ślad Diracowski wobec jawnego licznika (5) | 128 dokładnych porównań; zachowane σ₂ i argumenty zespolone |
| Pełny zamknięty integrand wobec redukcji L/R | 128 dokładnych porównań, wszystkie 16 składowych; 64 niezerowe błędy po pozostawieniu samego zredukowanego bąbla |
| Wyznaczniki swobodnego L/R | Dokładne zniesienie osobliwości s=0 w iloczynie (4), przy masie 0 i 1 oraz zespolonych argumentach |
| Transwersalność po wspólnej regularyzacji | Dowód powyżej; 4 dokładne kontrole tożsamości skalarnych |
| Pełny próg przestrzeniopodobny | 7 argumentów; zgodność całki parametrowej, postaci zamkniętej i widma |
| Kontynuacja i część urojona | 11 argumentów: poniżej, na i powyżej progu oraz poza osią; największa niezgodność \(8{,}63\cdot10^{-13}\) |
| Wkład masowy: widmo wobec funkcjonału α | 6 par (r,z), pełne całki; największa niezgodność \(4{,}94\cdot10^{-13}\) |
| Odwrócenie i składanie różnic | Błędy \(4{,}44\cdot10^{-16}\), \(8{,}88\cdot10^{-16}\); równe masy dają dokładnie 0 |
| Zmiana wspólnego odniesienia | Wspólne przeskalowanie trzech mas nie zmienia argumentów ani wyniku |
| Mała masa wewnętrzna | z=0,01; 0,001; 0,0001; różnica od (24) maleje: −0,1467; −0,01479; −0,001480 |
| Ciężki kanał | z=1; 4; 16: \(\mathcal H(2,z)=-2{,}57863;-0{,}453576;-0{,}0526994\), zgodne z zanikiem po odjęciu przy zerowym transferze |
| Granice pełnej średniej α (21) | Przy \(a=10^{-3},10^{-5},10^{-7}\) iloraz przez \(a\ln(1/a)\) zbliża się do 4/45; przy \(a=10^2,10^4,10^6\) reszta dużego argumentu maleje do 0,001643. Jedno uniwersalne podstawienie nie odtwarza małego argumentu |
| Dopasowanie α i wspólny μ | Dokładna kontrola współczynnika konwersji i anulowania pochodnych |
| Znane logarytmy drugiego rzędu | Dokładna zgodność różnicy \(-13L/24-L^2/8\) z (23)–(24) |

Kontrole liczbowe mają wskazane tolerancje w skrypcie. Dowody tożsamości i zbieżności stoją w notatce; próbki nie zastępują ich zakresu. Pełne wyniki zapisano w alfa-masa-kontrola-2026-10-09.json.
