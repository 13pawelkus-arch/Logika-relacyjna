# Pary (M,O), amplituda i warunek odczytu funkcji masy

Data: 04.10.2026. Kontynuacja `mapa-odczytu-skladnikow-masy-2026-10-04.md`.

## Wynik i jego zakres

Para (M,O) daje kanał odczytu. Z przygotowań i zliczeń dostępnych O można odzyskać kwadratowe porównania odpowiedzi, także ich część zespoloną. **Nie daje to automatycznie pojedynczej amplitudy przejścia ani macierzy Yukawy.** Różnica odczytu wobec Ø jest ponadto innym obiektem niż dodatnia kontrakcja amplitud.

Nowe ograniczenie przekładu: uzasadnieniem prostego przejścia od stosunków odpowiedzi własnych do stosunków Yukaw jest jednakowa waga czytającego na przestrzeni tych odpowiedzi. Dla stosunku dwóch takich stosunków wspólny czynnik może być inny w każdej parze: skraca się osobno. Waga zależna od kierunku odpowiedzi nie skraca się tą operacją.

To jest wyprowadzenie operacji i kryterium poprawnego przekładu w QM użytej już w 198–202. Nie wyprowadzono wartości mas, hierarchii zapachów ani współczynników pętlowych. 206 i 207 pozostają zamknięte; 166 i 208 obowiązują.

## Oczekiwania i zdania o upadku — przed rachunkami

**P1 — odczyt pary. Spodziewam się:** dla ustalonego kanału pary i ustalonego rodzaju zapisu w O częstość ma postać dodatniej formy kwadratowej na przygotowaniu. **Zdanie o upadku:** użycie tej postaci upada, jeżeli porównywane próby zmieniają kanał, sprzężenie, przygotowanie odniesienia albo niekontrolowaną historię pary. Nie zakładamy, że dowolny powtarzany eksperyment sam utrzymuje te warunki.

**P2 — porównanie fazowe. Spodziewam się:** dwa przygotowania osobne i ich połączenie z fazami 0 oraz π/2 wystarczą do odzyskania zespolonego elementu odpowiedzi. **Zdanie o upadku:** rekonstrukcja upada, jeżeli O nie ma dostępu do tych koherencji albo przygotowania nie zachowują tego samego kanału. Faza ma odniesienie w O; nie jest nadana wnętrzu M.

**P3 — amplituda i różnica. Spodziewam się:** dodatnia odpowiedź ma reprezentację Grama, ale różnica wobec Ø na ogół jej nie ma. **Zdanie o upadku:** pierwszy wniosek upada przy braku dodatniości; drugi zostałby obalony, gdyby różnica z zamkniętego przykładu 198 była dodatnia dla każdego przygotowania. Kontrola wybrana przed sprawdzeniem: kanał fazowy c=0 wobec c=1, odczyt |+⟩⟨+|.

**P4 — wagi. Spodziewam się:** warunkiem zachowania wszystkich kwadratowych porównań jest skalarna kompresja wagi czytającego na przestrzeń odpowiedzi; to mniej niż wymaganie identyczności na całej przestrzeni wyjść. **Zdanie o upadku:** twierdzenie upada, jeżeli istnieje para wektorów odpowiedzi, dla której forma ważona nie jest tym samym skalarnym wielokrotnością formy nieważonej. Kontrola negatywna: amplitudy diag(1/4,1/2), waga diag(1,1/4).

**P5 — stosunki stosunków. Spodziewam się:** przy skalarnych wagach w dwóch blokach podwójny stosunek usuwa je niezależnie, nawet jeśli są różne. **Zdanie o upadku:** przejście do stosunków Yukaw upada, jeżeli waga w choć jednym bloku zależy od odpowiedzi, któryś mianownik znika albo przyjęte rozdzielenie pełnej amplitudy na wspólny czynnik i Yukawę nie zachodzi.

**P6 — kompletne zliczenie. Spodziewam się:** suma prawdopodobieństw wszystkich wyników pełnego eksperymentu daje 1 i przez samo to zliczenie nie ujawnia sił poszczególnych odpowiedzi. **Zdanie o upadku:** wniosek upada, jeżeli pełny kanał nie zachowuje śladu albo lista wyników nie jest kompletna. Kontrola: identyczność i pełne defazowanie; odczyty |0⟩⟨0| oraz |1⟩⟨1|.

**Dane do kontroli algebry, ustalone przed jej wykonaniem.** Pełna amplituda syntetycznego przejścia T=[[1/4,i/8],[(1+i)/8,1/2]], waga F=diag(1,1/2). Do P5: dodatnie odpowiedzi zredukowane f=(1/4,3/8), g=(1/5,2/5), wspólne wagi kwadratowe odpowiednio 1/9 i 1/25. Oczekiwany kwadrat podwójnego stosunku: 16/9. Są to dane do kontroli kontrakcji, nie wartości fizycznych sprzężeń ani mas.

## 1. Co dokładnie należy do pary

W 198–202 wnętrze jest dla O dostępne przez kanał Λ. Zachowujemy właśnie ten zakres opisu: ustalone warunki przygotowania, sprzężenie i brzeg pary. Korzystanie z liniowego, całkowicie dodatniego kanału jest już częścią tego rachunku QM; nie wyprowadza się takiego kanału z samego słowa „relacja”. W szczególności nie zakładamy go bez sprawdzenia przy zmiennych korelacjach początkowych lub pamięci eksperymentu.

O przygotowuje stan ρ swoich nośników i zapisuje wynik opisany efektem F, 0≤F≤I. F jest operatorem tego konkretnego rozróżnienia w aparacie, nie nowym polem ani postulatem fizycznym. Rozdzielczość odczytu zapisujemy jak w R1d:

\[
s=\ln(n_0/n).
\]

Nie jest to czas zewnętrzny. Zależność od s oznacza porównanie przy innej liczności obiegu.

Przy częstości N_F/N_prób rozróżniamy skończony wynik statystyczny od prawdopodobieństwa, które opisuje teoria. W granicy poprawnego zliczania tego samego przygotowania:

\[
p_F(\rho;s)=\operatorname{Tr}\bigl[F\Lambda_{(M,O),s}(\rho)\bigr]
=\operatorname{Tr}\bigl[Q_{(M,O),F}(s)\rho\bigr],
\qquad Q=\Lambda^*(F).
\]

Gwiazdka oznacza tu odwzorowanie sprzężone względem śladu. To przepisanie tej samej reguły Borna. Ponieważ p_F jest prawdopodobieństwem dla każdego dopuszczalnego przygotowania, Q≥0, a w pełnym kanale zachowującym ślad także Q≤I.

**Nie dodano stanu wnętrza M.** Q opisuje zależność zapisu O od przygotowań O. Nie trzeba znać liczby elementów M ani odtwarzać jego obwodu. Pusty moduł ma własny kanał Λ_Ø; zgodnie z 200 nie zastępujemy go automatycznie identycznością.

Odtwarzanie wielu odpowiedzi dla różnych przygotowań nie dokłada czwartego parametru pojedynczemu stanowi nośnika. Trzy parametry z 199 opisują jeden stan; parametry kanału opisują zależność między przygotowaniami i odczytami. Nie utożsamiamy rozmiaru macierzy kanału z przestrzennym 3D.

**Źródło zakresu QM:** Chuang–Nielsen, równania (2.2)–(2.4) i procedura w §III [L1]. Warunki przygotowania są jawne, nie są wnioskiem o dowolnej parze.

## 2. Jak odzyskać zespolone porównanie z liczności

Niech |j⟩ i |k⟩ będą dwoma ortogonalnymi przygotowaniami rzeczywiście dostępnymi O w tym samym sektorze odczytu. Ich etykiety nie oznaczają położenia wewnątrz M. O musi mieć możliwość przygotowania także

\[
|jk;\theta\rangle=\frac{|j\rangle+e^{i\theta}|k\rangle}{\sqrt2}.
\]

To warunek operacyjny. Jeżeli reguły superselekcji lub brak odniesienia fazy uniemożliwiają te przygotowania danemu O, elementu zespolonego nie dopisujemy. Dodatkowe odniesienie fazy należy wtedy do opisu O i do warunków porównania [L2].

Odczyty osobne to p_j=Q_jj oraz p_k=Q_kk. Dla połączenia:

\[
p_{jk}(\theta)=\frac{p_j+p_k}{2}
+\operatorname{Re}\bigl(e^{i\theta}Q_{jk}\bigr).
\]

Stąd dokładnie:

\[
\boxed{
Q_{jk}=p_{jk}(0)-\frac{p_j+p_k}{2}
+i\left[\frac{p_j+p_k}{2}-p_{jk}(\pi/2)\right].
}
\]

Wszystkie p są stosunkami zliczeń w tym samym protokole. Jeden odczyt nie daje zespolonej amplitudy. Zespół odczytów pozwala odzyskać porównanie odpowiedzi; to zachowuje uwagę użytkownika o obrazie interferencyjnym powstającym z serii odczytów.

Procedura jest standardową operacją QM: fizyczne przygotowania pozwalają odzyskać również działanie na elementach pozadiagonalnych [L1, §III]. Wzór wyżej jest jej rzutem na jeden wybrany zapis F, nie pełną tomografią kanału.

**Status:** wyprowadzone porównanie odczytu przy nazwanych przygotowaniach. Nie wyprowadzono z samej podstawy, że każde wybrane j,k jest dla O koherentnie dostępne.

## 3. Która „amplituda” jest już dostępna

Z dodatniości Q istnieje reprezentacja

\[
Q=A_F^\dagger A_F,
\qquad Q_{jk}=\langle A_Fj|A_Fk\rangle.
\]

Można wybrać A_F=√Q. To **reprezentacja kwadratowych porównań**, a nie identyfikacja fizycznego wierzchołka. Zastąpienie A_F przez U A_F, dla izometrii na jego obrazie, pozostawia Q bez zmiany.

W znanej reprezentacji kanału Λ(ρ)=Σ_ℓ K_ℓρK_ℓ† ten sam zapis daje

\[
Q=\sum_\ell K_\ell^\dagger F K_\ell.
\]

Reprezentację Grama otrzymuje się, ustawiając bloki √F K_ℓ jeden pod drugim. Indeks ℓ jest indeksem reprezentacji operatorowej kanału. Nie nadajemy mu znaczenia elementu, nośnika albo obiektu wewnątrz M. Zmiana reprezentacji Krausa nie zmienia odczytu.

Jeżeli istnieje jeden koherentny operator przejścia T w rozpatrywanym kanale, mamy Q=T†FT. Z samego Q nie wynika jednak, że kanał ma jeden taki operator. Przykład: dla F=|0⟩⟨0| identyczność i pełne defazowanie dają dokładnie to samo Q=F dla wszystkich przygotowań. Przy wejściu |+⟩ pierwszy kanał zwraca stan czysty, drugi stan mieszany. Wybrany zapis F nie rozstrzyga o zachowanej koherencji.

Gdy pełny kanał jest operacyjnie dostępny, warunek jednego operatora można rozstrzygać na jego macierzy Choi, użytej już w 200–201:

\[
J_\Lambda=\sum_{jk}|j\rangle\langle k|\otimes\Lambda(|j\rangle\langle k|)
=\sum_\ell |K_\ell\rangle\!\rangle\langle\!\langle K_\ell|.
\]

J ma rząd jeden dokładnie wtedy, gdy wszystkie niezerowe wektory |K_ℓ⟩⟩ są proporcjonalne, czyli istnieje reprezentacja z jednym operatorem. To prosty warunek algebraiczny, nie założenie o wnętrzu. Nawet wtedy sam kanał nie wyznacza globalnej fazy T. Porównanie z osobną drogą odniesienia wymaga opisania takiego obiegu; zgodnie z 198 dołożenie drogi może zmienić sam kanał.

**Sprzężenie hermitowskie nie jest automatycznie fizycznym powrotem.** T†FT jest kontrakcją w rachunku prawdopodobieństwa. Operator rzeczywistego przejścia w drugą stronę trzeba uzyskać z tego samego działania i warunków przygotowania; sam zapis † go nie ustanawia.

**Status:** uzyskano dodatnią kontrakcję i warunek, kiedy może ona dotyczyć pojedynczej amplitudy przejścia. Nie nazwano √Q Yukawą.

## 4. Dlaczego różnicy wobec Ø nie wolno zastąpić gramem

Z 206 odczyt jest różnicą własnych stanów O. Dla zapisu F:

\[
\Delta p_F(\rho)=\operatorname{Tr}[F(\Lambda-\Lambda_\varnothing)(\rho)]
=\operatorname{Tr}[\Delta Q_F\rho],
\qquad \Delta Q_F=Q_F-Q_{\varnothing,F}.
\]

Q_F oraz Q_Ø,F są dodatnie. **Ich różnica nie musi być dodatnia.**

Kontrola z istniejącego kanału fazowego 198: Λ_c mnoży element ρ_01 przez c, a ρ_10 przez c̄. Dla F=|+⟩⟨+|:

\[
Q_c=\frac12\begin{pmatrix}1&\bar c\\c&1\end{pmatrix},
\qquad
\Delta Q=Q_c-Q_1=
\frac12\begin{pmatrix}0&\bar c-1\\c-1&0\end{pmatrix}.
\]

Wartości własne różnicy to ±|c−1|/2. Przy c=0:

\[
\Delta p_F(|+\rangle)=-\frac12,
\qquad \Delta p_F(|-\rangle)=+\frac12.
\]

To zmiana udziału wyników, a nie ujemne prawdopodobieństwo. Nie istnieje A z ΔQ=A†A dla tego przykładu. Maksymalna rozróżnialność pozostaje D=|c−1|/2, zgodnie z 198; dodatnia liczba D nie odzyskuje całej macierzy różnicy ani jej fazowych porównań.

**Co zmienia ten wynik:** wyklucza przekład „odczyt wobec Ø = Y†Y” bez dalszego rozdzielenia. Jeżeli konkretny rodzaj przejścia jest niemożliwy przy Ø i Q_Ø,F=0, przeszkoda dodatniości znika. To musi jednak wynikać z wybranego przejścia, nie z ogólnego symbolu Ø. Nie wystarcza też jeszcze do identyfikacji Yukawy.

To nie ponowny test 198. Jest to kontrola i odrzucenie zbyt szerokiego utożsamienia w naszym przekładzie do funkcji masy.

## 5. Dokładny warunek usunięcia wag czytającego

Warunkowe połączenie z poprzednią mapą jest następujące. Jeżeli z istniejącego działania SM i opisu wybranego przejścia uzyskano pełną, koherentną amplitudę

\[
T_f(s)=h_f(s)Y_f(s),
\]

gdzie h_f jest tym samym skalarem dla całego porównywanego bloku, to

\[
Q_f=|h_f|^2Y_f^\dagger F_fY_f.
\]

Y_f jest tutaj znanym zredukowanym wierzchołkiem teorii; nie został otrzymany przez nazwanie √Q. Pełna amplituda zawiera przygotowanie, propagację, czynniki spinowe i kinematykę. Ich sprowadzenie do jednego h_f jest warunkiem rachunku, a nie konsekwencją samego użycia wspólnego O. Dla kilku niesprowadzalnych operatorów przejścia trzeba zachować sumę kontrakcji.

Nie trzeba wymagać F_f=I na wszystkich wyjściach. Potrzebny jest dokładnie warunek

\[
\boxed{Y_f^\dagger F_fY_f=w_fY_f^\dagger Y_f,\qquad w_f>0.}
\]

Niech S_f=im Y_f, a P_S będzie rzutem na tę przestrzeń odpowiedzi. Warunek jest równoważny

\[
P_SF_fP_S=w_fP_S.
\]

**Dowód:** pierwsza równość mówi, że ⟨Y_fv|(F_f−w_fI)|Y_fu⟩=0 dla wszystkich przygotowań u,v. Ich obrazy przebiegają S_f, więc kompresja F_f−w_fI do S_f jest zerowa. W drugą stronę podstawienie daje od razu równość kontrakcji. Dowód nie wymaga odwracalności Y_f ani identyczności F_f poza S_f.

Warunek dotyczy zachowania całej macierzy kwadratowych porównań. Równość samych stosunków wartości własnych może wystąpić także przypadkiem przy nieskalarnej wadze; nie dowodzi przez to poprawności całego przekładu. Nie twierdzimy też, że każde pojedyncze F daje właściwy odczyt. W rzeczywistym porównaniu trzeba zachować wybrany wynik, kinematykę i pozostałe wagi. Wspólny czytający może czytać różne odpowiedzi z różną wagą.

**Kontrola negatywna:** Y=diag(1/4,1/2), F=diag(1,1/4). Wtedy

\[
Y^\dagger Y=\operatorname{diag}(1/16,1/4),
\qquad Y^\dagger FY=\operatorname{diag}(1/16,1/16).
\]

Stosunek zredukowanych amplitud wynosi 1/2, a pierwiastek stosunku odpowiedzi ważonych wynosi 1. Nie uratuje tego samo skasowanie skalarnego h. Jest to syntetyczna kontrola przekładu, bez danych pomiarowych.

**Związek z 180–181:** tam wspólny h skraca się w wyznaczonym, skalarnym bloku propagatora modułu. Rząd jeden tego bloku nie jest twierdzeniem o dowolnym kanale QM ani dowolnej macierzy zapachów. Właśnie to trzeba wykazać przy przejściu do konkretnego wierzchołka; nie przenosimy twierdzenia przez podobieństwo zapisu.

## 6. Kiedy wychodzą stosunki stosunków

Przy powyższym warunku dodatnie odpowiedzi własne q_fi, czyli wartości własne Q_f, spełniają

\[
q_{fi}(s)=\zeta_f(s)y_{fi}(s)^2,
\qquad \zeta_f=|h_f|^2w_f>0.
\]

Dlatego stosunek w jednym bloku daje odczyt B:

\[
\sqrt{\frac{q_{fi}}{q_{fj}}}=\frac{y_{fi}}{y_{fj}}.
\]

q_fi są odpowiedziami własnymi, nie dowolnie wybranymi elementami diagonalnymi w bazie przygotowań. Do ich odzyskania potrzebne są wcześniej ustalone porównania koherentne w dostępnej przestrzeni wejść. Jeżeli O nie ma tego dostępu, nie dopisujemy mu pełnego widma Q.

Teraz cztery dodatnie odczyty dają

\[
\boxed{
\mathcal R(s)=
\sqrt{\frac{q_{fi}(s)/q_{fj}(s)}{q_{gk}(s)/q_{g\ell}(s)}}
=\frac{y_{fi}(s)/y_{fj}(s)}{y_{gk}(s)/y_{g\ell}(s)}.
}
\]

**ζ_f nie musi być równe ζ_g.** Każde skraca się we własnym stosunku. To dokładna korzyść z drugiego poziomu porównania: nie wymaga wspólnego skalarnego unormowania między blokami. Nadal wymaga wspólnej wagi wewnątrz każdego bloku i właściwego przyporządkowania amplitud. ζ_f(s) i ζ_g(s) mogą być funkcjami rozdzielczości: skrócenie zachodzi w każdym odczycie, o ile warunek obowiązuje w całym zadeklarowanym zakresie.

Forma logarytmiczna jest równoważna:

\[
\ln\mathcal R(s)=\frac12\left[
\ln q_{fi}(s)-\ln q_{fj}(s)-\ln q_{gk}(s)+\ln q_{g\ell}(s)
\right].
\]

Wyprowadzone jest prawo porównania. Funkcje q(s) i ich dynamika pozostają do policzenia z tego samego działania. Wprowadzenie s nie wyprowadza jeszcze funkcji beta, Casimirów, współczynnika 3/2 ani wartości CKM. Nie ma tu warunku wybierającego hierarchię mas.

Odczyt A nadal wymaga przejścia opisanego w 166 i w M8 poprzedniej mapy; nie przypisujemy pojedynczemu uwięzionemu kwarkowi własnego odczytu A.

## 7. Dlaczego suma wszystkich zliczeń nie rozwiązuje masy

Dla kompletnego zestawu zapisów Σ_r F_r=I i pełnego kanału zachowującego ślad:

\[
\sum_r Q_r=\Lambda^*(I)=I,
\qquad \sum_r p_r(\rho)=1.
\]

Nie należy utożsamiać tej pełnej sumy z kontrakcją jednego zredukowanego wierzchołka. Wszystkie wyniki obejmują także pozostałe przejścia i zapis braku wybranego zdarzenia. Dla wyodrębnionej gałęzi przejścia jej całkowite prawdopodobieństwo może być niejednostkowe, bo ta gałąź nie zachowuje śladu osobno.

**Co ten wynik wyklucza:** usunięcie zależnych wag przez policzenie absolutnie wszystkiego i nazwanie wyniku siłą Yukawy. Pełna suma usuwa rozróżnienie, które miało być czytane. Potrzebny jest konkretny, uzasadniony teorią rodzaj przejścia i zachowanie warunków jego porównania.

## Mapa statusów

| Wielkość | Co O rzeczywiście porównuje | Co zostało uzyskane | Co pozostaje przyjęte albo otwarte |
|---|---|---|---|
| p_j | Liczność wyniku wobec liczności prób przy przygotowaniu j | Rzeczywista odpowiedź diagonalna Q_jj | Stały protokół i wybrany zapis F |
| Q_jk | Odpowiedzi osobne oraz koherentne z fazami 0 i π/2 | Zespolona kontrakcja odpowiedzi | Dostęp O do obu koherencji |
| A_F | Reprezentacja Q jako Grama | Normy i nakładania reprodukujące wybrany odczyt | Nie jest sama przez się fizycznym wierzchołkiem |
| T | Pełne koherentne przejście wybranego kanału | Możliwe po uzasadnieniu jednego operatora przejścia | Pełny kanał, jego przygotowanie i odniesienie fazy |
| ΔQ | Zapis przy M wobec zapisu przy Ø | Hermitowska, na ogół nieokreślona znakowo różnica | Nie wolno zastąpić jej A†A |
| y_fi/y_fj | Odpowiedzi własne jednego bloku | √(q_fi/q_fj) przy skalarnym ważeniu | T=hY oraz warunek kompresji F na przestrzeń odpowiedzi |
| R | Stosunek dwóch stosunków odpowiedzi własnych | Usunięcie dwóch niezależnych wspólnych unormowań | Te same warunki wewnątrz każdego bloku, dodatnie mianowniki |
| Funkcje masy | Zależność tych porównań od liczności obiegu | Dopuszczalna bezwymiarowa postać logarytmiczna | Konkretne amplitudy przejścia i ich pełna odpowiedź pętlowa |

## Kontrola wykonania

Przed uruchomieniem ustalono powyższe oczekiwania i dane syntetyczne. Wykonano siedem celowych sprawdzeń dokładnej algebry liczb wymiernych:

1. Rekonstrukcja kontrakcji z czterech przygotowań reprodukuje bezpośrednie ważenie amplitud T. **Pierwotne oczekiwanie niezerowej części urojonej UPADŁO:** wybrana F=diag(1,1/2) daje Q_01=1/32, więc wkłady urojone znoszą się dokładnie. Ta kontrola sama nie sprawdziła znaku części urojonej. Nie zmieniono danych, żeby ukryć to niepowodzenie.
2. Wybrane T jest poprawnym operatorem gałęzi: T†T≤I; z F≥0 otrzymuje się poprawne prawdopodobieństwa.
3. Różnica wobec Ø ma dodatni i ujemny odczyt dla dwóch przygotowań — utożsamienie jej z gramem upada.
4. Jedno Q nie odróżnia identyczności od pełnego defazowania, mimo różnej czystości zwracanych stanów.
5. Nieskalarna waga zmienia stosunek odpowiedzi i jest odrzucana przez kryterium P4.
6. Dwa niezależne skalarne unormowania skracają się w podwójnym stosunku; jego kwadrat wynosi dokładnie 16/9.
7. Pełne zliczenie dwóch wyników daje I dla obu kanałów z P6.

Są to kontrole przekładu i jego zakresu. Nie są eksperymentem ani wyprowadzeniem wartości fizycznych. Nie powtarzano 27 wcześniejszych kontroli.

**Dodatkowa kontrola znaku, postawiona po wykryciu znoszenia. Spodziewam się:** dla tego samego T i dodatkowego odczytu F=I w wybranej gałęzi przejścia część urojona nie znika, a przygotowanie z fazą π/2 odtwarza ją z właściwym znakiem. **Zdanie o upadku:** zgodność upada, jeżeli zliczenie amplitud i wzór rekonstrukcji dają różny znak albo wartość elementu pozadiagonalnego. F=I dotyczy tej gałęzi, której operator T nie zachowuje śladu osobno; nie jest pełnym zliczeniem eksperymentu z §7. Wynik dopisany po tej jednej kontroli.

**Wynik dodatkowej kontroli:** p_j=3/32, p_k=17/64, p_jk(0)=31/128, p_jk(π/2)=27/128. Rekonstrukcja daje Q_jk=1/16−i/32, zgodne dokładnie z bezpośrednim iloczynem kolumn T. Znak został sprawdzony. Pierwotne upadłe oczekiwanie pozostaje w zapisie; dodatkowa kontrola nie zmienia żadnej struktury fizycznej ani wartości pochodzącej z pomiaru.

## Następny rozstrzygający rachunek

W istniejącym działaniu SM trzeba wyodrębnić konkretny kanał L→R związany z H i porównać go przy tym samym odniesieniu O. Rachunek ma zachować pełną amplitudę, odpowiedź pustego modułu, propagację oraz rzeczywiste wagi zapisu. Jego wynik ma rozstrzygnąć, czy kontrakcja ma formę skalar razy Y†Y, czy pozostaje Y†FY albo suma kilku kontrakcji. Nie wolno dobierać F lub pomijać członów po to, żeby uzyskać pierwszą postać.

**Spodziewam się:** po uwzględnieniu znanych oddziaływań da się oddzielić wspólne unormowanie od porównań odpowiedzi własnych w jasno zadeklarowanym zakresie. **Zdanie o upadku:** jeśli pełna odpowiedź aparatu albo propagator pozostawia wagę zależną od kanału, utożsamienie prostego stosunku z masą B upada w tym zakresie; trzeba zachować tę wagę w funkcji. Wynik nie może zostać „naprawiony” zmierzonymi masami wstawionymi jako niewyprowadzone unormowanie.

Ten rachunek nie jest tu jeszcze wykonany. Obecny krok daje sposób jego zapisania i kryterium, które odrzuci błędne skrócenie przed przeniesieniem go do dalszych pięter.

## Źródła

- Plik główny: R1d, R1f-3; A11d — 179–181, 198–202, 206; 207 w R1a; 208; §F1 — 152, 155, 166. Poprawki i granice tych wpisów zachowano.
- Poprzednia analiza: `mapa-odczytu-skladnikow-masy-2026-10-04.md`, szczególnie M0, M1, M8 i ostatni otwarty krok.
- **[L1]** I. L. Chuang, M. A. Nielsen, *Prescription for experimental determination of the dynamics of a quantum black box*, arXiv:quant-ph/9610001, Journal of Modern Optics 44 (1997), 2455–2467. [Pełny tekst](https://arxiv.org/pdf/quant-ph/9610001). Użyto reprezentacji operatorowej i przygotowań z §III; wymiar Hilberta nie jest tu liczbą wymiarów przestrzeni.
- **[L2]** S. D. Bartlett, T. Rudolph, R. W. Spekkens, *Reference frames, superselection rules, and quantum information*, Reviews of Modern Physics 79 (2007), 555–609, arXiv:quant-ph/0610030. [Pełny tekst](https://arxiv.org/pdf/quant-ph/0610030). Użyto ograniczenia dostępu do koherencji oraz jawnego odniesienia fazy; §IV.A omawia włączenie odniesienia do opisu układu.
