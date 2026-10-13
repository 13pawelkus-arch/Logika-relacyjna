# Dynamiczny odczyt, zapis i swoboda fazy — pierwszy test

12.10.2026. Punkt wyjścia: R1a–R1c, 179, 207, 258–260 i 263 w `logika-relacyjna-v3.5.md`. Rachunek: wyprowadzenie i kontrola symboliczna asystenta. Znane narzędzia matematyczne oznaczono w źródłach na końcu.

**Wynik:** w opisanym niżej procesie można objąć jednym rachunkiem przygotowanie, trzy odczyty komplementarne, zegar, niesiony zapis i powstanie odpowiedzi czytającego. Wagi odpowiedzi są wtedy związane z fazą i z faktycznym zapisem powstającym w otoczeniu. Te sprawdzone warunki dopuszczają jednak ciągłą rodzinę faz. Jest to wynik dla jawnej realizacji kwantowej, nie dowód niewystarczalności całej ramy.

**Korekta kryterium testu:** dwie różne odpowiedzi dwóch poprawnych procesów nie dowodzą istnienia dwóch różnych praw. Oba procesy mogą realizować tę samą regułę, przy różnych relacjach oddziaływania. Obecny rachunek bada swobodę konkretnej relacji `U_q` z 259. Regułę zespolonych amplitud i odczytu kwantowego przyjmuje z R1b; nie wyprowadza jej na nowo i nie porównuje z odmienną regułą.

## 1. Co dokładnie podlega kontroli

Oczekiwanie, warunek obalenia i mapowanie na zdania ramy zapisano przed uruchomieniem kontroli w `zalozenia-przed-kontrola.md`.

| Zdanie lub warunek źródłowy | Realizacja w teście | Zakres wyniku |
|---|---|---|
| R1b: domknięta triada odczytów | Trzy operatory wyrażone przez relacje par; dokładna algebra Pauliego | Nie utożsamiamy liczby nośników z wymiarem przestrzeni |
| R1a, 207: informacja o stanie nie jest stanem | Zapis wyniku jest korelacją; jego lokalny odczyt nie wyznacza faz pełnego stanu | Częściowość wykazana nieiniektywnością kanału, bez argumentu o pojemności |
| R1a, D2: niesienie informacji | Wynik przygotowania zostaje w strukturze i jest czytany razem z nowym wynikiem | Bez zapisu przygotowania sygnał fazowy znika |
| 179: relacje nośników i moduły | Badana interakcja jest relacją pary; operacje aparatu są jawnymi modułami | Mikroskopowego mechanizmu sterowania wszystkimi modułami nie wyprowadzono z ramy |
| 258: globalny więz i lokalna dynamika | Cały sektor spełnia trzy zerowe więzy spinu, choć zmieniają się jego relacje wewnętrzne | Globalny singlet jest wyborem sektora |
| Brak czasu zewnętrznego | Wspólny operator spójności zegara i całego procesu | Konstrukcja zegara historii jest jawnie przyjęta |
| 259–260: wspólne pochodzenie wag i odpowiedzi | Wszystkie wyniki liczone z tych samych operacji przygotowania, oddziaływania i odczytu | Nie wolno zmienić amplitudy, pozostawiając resztę procesu bez zmiany |

Wektory użyte w rachunku opisują warunkowe korelacje. Nie zakłada się, że któryś nośnik chwyta pełny „stan teraz” ani że globalny wektor jest dostępny wewnętrznemu czytającemu. Zegar, zapis i obiekt są rolami części jednej realizacji. Rozdzielenie symboli w rachunku nie nadaje im niezależności ontologicznej.

## 2. Więcej relacji wewnątrz globalnego zera

Dwa nośniki w pojedynczym singlecie nie wystarczały: wszystkie `U_q` z 259 działały na nim identycznie. Bierzemy cztery nośniki. Ich sektor całkowitego spinu zero ma dwa niezależne stany:

\[
|0_L\rangle=|s\rangle_{12}|s\rangle_{34},\qquad
|1_L\rangle=\frac{|t_+t_-\rangle-|t_0t_0\rangle+|t_-t_+\rangle}{\sqrt3}.
\]

Tutaj \(s=(|01\rangle-|10\rangle)/\sqrt2\), \(t_0=(|01\rangle+|10\rangle)/\sqrt2\), \(t_+=|00\rangle\), \(t_-=|11\rangle\). Litera L oznacza kod wewnętrznych relacji; nie chiralność L/R z 260.

Każdy wektor w tym sektorze spełnia

\[
J_i|\psi\rangle=0,\qquad
J_i=\tfrac12\sum_{a=1}^4\sigma_i^{(a)},\quad i=1,2,3.
\]

Każdy pojedynczy nośnik ma stan zredukowany \(I/2\). Różnice zapisują się w relacjach między nośnikami. To mocniejsza realizacja punktu 258 niż symetria tylko jednego wybranego wektora.

Nie potrzeba zewnętrznej osi pomiarowej. Niech \(E_{ab}\) oznacza zamianę dwóch nośników. W powyższym sektorze:

\[
E_{12}=-Z_L,\qquad E_{23}=\tfrac12(Z_L+\sqrt3X_L),
\]

\[
X_L=\frac{2E_{23}+E_{12}}{\sqrt3},\qquad
Y_L=\frac{[Z_L,X_L]}{2i}.
\]

Operatory \(X_L,Y_L,Z_L\) spełniają dokładnie tę samą algebrę domknięcia co w R1b. Są pytaniami o relacje par, a ich nieprzemienność jest istotna. Jest to zastosowanie przyjętej algebry; nie niezależne wyprowadzenie geometrii fizycznej.

## 3. Ta sama relacja pary co w 259

Na nośnikach 2–3 działa

\[
U_q=P_s^{23}+qP_t^{23},\qquad q=e^{i\theta}.
\]

Cały czteronośnikowy sektor pozostaje singletowy. W bazie jego relacji operator ma postać

\[
U_q\big|_L=\frac14
\begin{pmatrix}
1+3q&\sqrt3(q-1)\\
\sqrt3(q-1)&3+q
\end{pmatrix}.
\tag{1}
\]

Współczynniki tej macierzy wynikają z projektorów pary i ich nakładania z przygotowaniem. Nie dopisano niezależnych wag.

Po warunkowym przygotowaniu \(|0_L\rangle\) otrzymujemy

\[
U_q|0_L\rangle=a_q|0_L\rangle+b_q|1_L\rangle,
\quad a_q=\frac{1+3q}{4},\quad b_q=\frac{\sqrt3(q-1)}4.
\tag{2}
\]

Przygotowanie to trzeba jeszcze wytworzyć i zachować jego zapis. To robi następny krok.

## 4. Przygotowanie i czytający wewnątrz procesu

Używamy modułów \(S,E,R,B,O\). S zawiera badane relacje; E jest ich partnerem przygotowania; R niesie wynik przygotowania; B niesie nowy wynik; O zapisuje wynik ich porównania. R, B i O nie są kopiami całego S. Każdy taki dwustanowy moduł może być zakodowany w tej samej postaci singletowej co powyżej, również stopnie swobody zegara.

Jawny warunek brzegowy dla tego fragmentu procesu:

\[
|\chi_0\rangle=
\frac{|0_L0_L\rangle_{SE}+|1_L1_L\rangle_{SE}}{\sqrt2}
|000\rangle_{RBO}.
\]

S samo ma tu \(I/2\). Warunek brzegowy opisuje nazwane relacje wejściowe; nie stanowi pierwszego stanu świata ani wyniku wyprowadzonego z ramy.

Sześć relacji aparatu:

| Przejście konfiguracji zegara | Operacja i jej treść |
|---|---|
| 0 → 1 | \(V_1=\mathrm{CNOT}_{S\to R}\): powstaje zapis relacyjnego wyniku przygotowania |
| 1 → 2 | \(V_2=U_q\): badana relacja pary |
| 2 → 3 | \(V_3=W_k\): relacyjny analizator jednego z trzech odczytów |
| 3 → 4 | \(V_4=\mathrm{CNOT}_{S\to B}\): powstaje nowy zapis |
| 4 → 5 | \(V_5=\mathrm{CNOT}_{R\to O}\): niesiony wynik uczestniczy w odczycie |
| 5 → 6 | \(V_6=\mathrm{CNOT}_{B\to O}\): O niesie różnicę wyników, \(O=R\oplus B\) |

Przy \(k=z\) mamy \(W_z=I\); pozostałe analizatory spełniają \(W_k^\dagger Z_LW_k=\sigma_{k,L}\). Ich osie zdefiniowano przez relacje z punktu 2.

Wynik R=0 przygotowuje S warunkowo w \(|0_L\rangle\). Nie potrzeba szczególnego stanu wejściowego: dla każdego \(\rho\) o niezerowym prawdopodobieństwie tej gałęzi

\[
P_0\rho P_0=\rho_{00}P_0.
\]

Przy splątaniu z otoczeniem analogicznie pozostaje \(P_0\otimes\tau_E\). Warunkowanie oznacza pytanie o niesiony wynik; żadna gałąź nie jest usuwana z pełnego procesu przez zewnętrznego selektora.

Sieć niesienia jest acykliczna. Kolejne CNOT zapisują rozróżnialne wyniki w wybranym pytaniu. Dla superpozycji wytwarzają korelacje, nie kopię dowolnego stanu. Na przykład \((|0\rangle+|1\rangle)/\sqrt2\) i \((|0\rangle+i|1\rangle)/\sqrt2\) dają ten sam lokalny zapis \(I/2\), choć pełne korelacje są różne. To jawna częściowość odczytu.

Istnienie realizacji logicznych operacji w sektorach singletowych przy użyciu oddziaływań par jest znanym wynikiem [2]. Obecny skrypt sprawdza jawne operatory modułów i ich sprzężenie do zegara. Nie konstruuje kompletnego mikroskopowego sterownika oddziaływań z samych zdań ramy.

**Uzupełnienie po audycie punktu 4, 12.10.2026:** powyższy CNOT jest idealizacją instrumentu. Jeśli dodatkowo wymagać zachowania addytywnej energii z generatorem \(H_S=\varepsilon P_t^{23}\), dokładny powtarzalny zapis \(Z_L\) jest niedopuszczalny dla \(\varepsilon\ne0\). W raporcie `punkt4-przygotowanie-energia-zapis-2026-10-12.md` skonstruowano w jego miejsce przybliżony instrument z wewnętrznym odniesieniem fazowym, dokładnie zachowujący energię. Jego odpowiedź zależy od \(\Theta=\theta+\phi_p-\phi_o\) oraz od koherencji odniesień. Wspólny postęp fazy modułu i dopasowanego odniesienia znosi się w wyniku. Dalsze twierdzenia tego pierwszego raportu o swobodzie q odnoszą się do zmian relacji przy ustalonych fizycznych odniesieniach, nie do wspólnego postępu całej konstrukcji. Oryginalny rachunek pozostaje kontrolą nazwanej idealizacji.

## 5. Zegar jest częścią wspólnego więzu

Nie uruchamiamy układu według zewnętrznego parametru t. Stany \(|n\rangle_C\) oznaczają siedem rozróżnialnych konfiguracji wewnętrznego zegara. Jest to skończony fragment procesu; nie idealny zegar z dokładną kanoniczną relacją położenia i pędu.

Niech \(|\chi_{n+1}\rangle=V_{n+1}|\chi_n\rangle\). Wspólne korelacje opisujemy przez

\[
|\Psi_q\rangle=\frac1{\sqrt7}\sum_{n=0}^{6}|n\rangle_C|\chi_n(q)\rangle.
\tag{3}
\]

Wprowadźmy

\[
B_n=\langle n+1|\otimes I-\langle n|\otimes V_{n+1},
\quad G_q=\sum_{n=0}^{5}B_n^\dagger B_n.
\tag{4}
\]

Wtedy, dla każdego \(|q|=1\), dokładnie

\[
G_q\ge0,\qquad G_q|\Psi_q\rangle=0.
\]

Nie ma osobnego równania dla przygotowania, innego dla pamięci i jeszcze innego dla czytającego: wszystkie wchodzą do (4). Wektor (3) jest matematycznym zapisem procesu, zgodnym z rozróżnieniem z 258 między globalnym więzem i wewnętrzną dynamiką. Nie jest przedmiotem pełnego samoodczytu. Sprzężenie hermitowskie w (4) zapewnia zgodność amplitud; nie dodaje cyklu do skierowanej sieci niesienia.

Efekt wskazanego zdarzenia można uczynić zgodnym z więzem. Dla projektora \(P_{\rm hist}\) na przestrzeń dozwolonych historii efekt \(F=P_{\rm hist}EP_{\rm hist}\) spełnia \([G_q,F]=0\) i daje na (3) to samo prawdopodobieństwo co E. Sprawdzono to również na pełnych macierzach 224 × 224. Zgodność nie opiera się zatem wyłącznie na użyciu efektu niekomutującego z więzem.

**Dokładne miejsce pozostającego założenia:** operacje \(V_j\) i sposób ich powiązania z C są wejściem konstrukcji (4). Istnienie takiego G dla rodziny q dowodzi spójności tej realizacji. Samo nazwanie G „domknięciem” nie dowodzi, że wyraża ono wszystkie konsekwencje nierozdzielności z R1a–R1c.

## 6. Wynik odczytu i rzeczywista rozróżnialność faz

Czytający porównuje aktualnie dostępne O, R i C. Dla analizatora z:

\[
\boxed{
p_q(O=0\mid C=6,R=0)
=\frac{|1+3q|^2}{16}
=\frac{5+3\cos\theta}{8}.
}
\tag{5}
\]

Przy tym \(p(C=6,R=0)=1/14\), więc warunkowanie jest dobrze określone.

| Faza tej samej badanej pary | Odczyt (5) |
|---|---:|
| \(\theta=\pi/2\), \(q=i\) | \(5/8\) |
| \(\theta=\pi\), \(q=-1\) | \(1/4\) |

W obu przypadkach aparat, zapis przygotowania, znaczenie zdarzenia i wskazanie zegara są te same. Różnica jest bezwymiarowa; nie znika po zmianie jednostek. Same zestawy prawdopodobieństw też są różne, więc nie jest to tylko zamiana nazw dwóch wyników.

Jeden odczyt nie rozróżnia \(\theta\) od \(-\theta\). Po uwzględnieniu odczytów komplementarnych otrzymujemy

\[
r_x=\frac{\sqrt3}{4}(1-\cos\theta),\qquad
r_y=\frac{\sqrt3}{2}\sin\theta,\qquad
r_z=\frac{1+3\cos\theta}{4}.
\tag{6}
\]

Każda składowa wynika z odpowiedniego pełnego procesu zapisu: \(p_k(O=0\mid C=6,R=0)=(1+r_k)/2\). Są to odrębne kompatybilnie przygotowane próby; nie jednoczesne ostre pomiary trzech niekomutujących wielkości. W tej klasie odpowiedzi odtwarzają

\[
q=\frac{4r_z-1}{3}+i\frac{2r_y}{\sqrt3}.
\]

Zatem swoboda q jest obserwowalną różnicą relacji, a nie ukrytą zmianą bazy całej konstrukcji. Gdyby zmieniać bazę, trzeba by równocześnie przekształcić wszystkie fizycznie nazwane przygotowania i efekty, zgodnie z 260.

Po pominięciu niesionego przygotowania R każdy analizator daje \(p(B=0\mid C=6)=1/2\), niezależnie od q. Czytelność fazy należy do relacji aktualnego wyniku z zapisem.

## 7. Co zmienia faktyczne powstanie zapisu o kanałach

Rozszerzamy tę samą konstrukcję o moduł T, który wiąże kanały \(P_s^{23}\) i \(P_t^{23}\) ze stanami \(|e_s\rangle\) i \(|e_t\rangle\). To dodatkowa fizyczna relacja, a nie dopisane prawdopodobieństwo. Jej koherentne działanie można zapisać jako

\[
|\psi\rangle|0\rangle_T\longmapsto
P_s^{23}|\psi\rangle|e_s\rangle_T+
qP_t^{23}|\psi\rangle|e_t\rangle_T.
\]

Dla lokalnego odczytu nieobejmującego T, przy \(\kappa=\langle e_s|e_t\rangle\), dostajemy

\[
\boxed{p(O=0\mid c_{\rm odczytu},R=0)
=\frac58+\frac38\operatorname{Re}(q\kappa).}
\tag{7}
\]

Symbol \(c_{\rm odczytu}\) oznacza konfigurację po dodatkowej relacji z T i po porównaniu zapisów. Wspólny więz rozszerza się o odpowiadający jej człon (4).

Przy jednakowych stanach T mamy \(\kappa=1\) i wraca (5). Przy rozróżnialnych ortogonalnych zapisach mamy \(\kappa=0\): odpowiedź wynosi \(5/8\), niezależnie od fazy. Informacja o fazie nie została skasowana z całej konstrukcji; zmienił się jej dostępny lokalnie odczyt.

W skrypcie jawnie zrealizowano rodzinę \(\kappa=\mu=\cos\beta\), \(0\le\mu\le1\), za pomocą unitarnej kontrolowanej rotacji T. Dodatniość macierzy Grama stanów zapisu wymaga \(|\kappa|\le1\). Współczynnik interferencji nie jest swobodną wagą, jeśli ta relacja aparatu została już określona.

To daje również dokładne powiązanie z nieoznaczonością trzech odczytów tego kodu. Po uwzględnieniu T, a przed ich pomiarem:

\[
|\mathbf r|^2=\frac{1+3\mu^2}{4},\qquad
\boxed{\sum_{j=x,y,z}(\Delta\sigma_{j,L})^2
=\frac{11-3\mu^2}{4}.}
\tag{8}
\]

Przy \(\mu=1\) suma wynosi 2; przy \(\mu=0\) wynosi \(11/4\). Ten sam faktyczny zapis zmienia lokalną interferencję i lokalną nieoznaczoność. Wartości (8) nie są masą ani energią; nie utożsamiamy mieszaności kodu z masą fizyczną. Rachunek pozostaje zgodny ze wcześniejszym odróżnieniem tych pojęć w R1c i R1f.

## 8. Co potwierdzono, a czego ten test nie rozstrzyga

**Potwierdzono w tej realizacji:** nierozdzielne obliczenie procesu wiąże przygotowanie, fazę, zapis, wagi i częściowość odpowiedzi. Pominięcie któregokolwiek odpowiedniego sprzężenia zmienia wynik. Po uwzględnieniu całego wskazanego aparatu pozostaje rodzina \(q\in U(1)\), której różne elementy można rozróżnić wewnętrznie.

**Zakres, który pozostaje otwarty:** nie wykazano równoważności między całą treścią R1a–R1c i użytymi tu warunkami spójności operacyjnej. Przyjęto sektor kwantowy, moduły, korelację brzegową i konstrukcję zegara. Algebraiczna realizowalność aparatu nie wyprowadza jego występowania z ramy. Nie wybrano działania L/R lub EM, reguły pętli ani wartości mas i sprzężeń.

Trzeba odróżnić trzy pytania: czy określony proces ustala własne wagi — tutaj tak; czy sprawdzone warunki dopuszczają różne procesy — tutaj tak; czy z ramy wynika jedyna ogólna reguła ich budowania — tego test wewnątrz przyjętej QM sam nie rozstrzyga. Maksymalna ogólność opisu nie oznacza, że każde dopuszczalne zdarzenie ma mieć ten sam wynik.

**Następny konkretny punkt rozstrzygnięcia:** badać wierność zastąpienia nierozdzielnego domknięcia przez (4). Jeśli zdanie ramy wymusza dodatkową relację między badanym oddziaływaniem a budową przygotowania, zegara i czytającego, trzeba zapisać ją jako ograniczenie całej rodziny \(V_j(q)\) i wskazać, które q ją naruszają. Jeśli celem jest wybór samej reguły faz i wag, przedmiotem porównania muszą być różne reguły kompozycji na tych samych relacyjnie określonych danych, a nie same wartości q w jednej regule. Obecny przykład wyznacza dokładnie miejsce tego dalszego sprawdzenia.

## 9. Kontrole i odtworzenie rachunku

Skrypt `test-domkniecia-2026-10-12.py` liczy wszystkie macierze od definicji nośników. Wynik wykonania: **PASS — 166 kontroli dokładnych i 16 numerycznych**. Część symboliczna obejmuje dowolne \(|q|=1\); nie wyciąga wniosku o rodzinie z próbkowania faz. Osobno sprawdzono pełne macierze zegara dla \(q=i,-1\), z tolerancją \(10^{-11}\). Najniższe obliczone wartości własne G to około \(-3\cdot10^{-15}\), zgodnie z błędem zaokrągleń i dokładnym dowodem \(G\ge0\).

Kontrole obejmują globalne generatory, niezmienniczość sektora, triadę, unitarność, powstanie i przeniesienie zapisów, wszystkie trzy odczyty, wspólny więz, efekty komutujące z więzem oraz zależność od zapisu kanału. Dwa testy negatywne dają:

- Dwukrotne zwiększenie amplitudy \(b_q\) przy pozostawieniu reszty dla \(q=i\) daje normę \(17/8\). Tak zmienione wagi nie należą do tej samej znormalizowanej realizacji.
- Usunięcie sprzężenia zapisującego B daje czytającemu stałą odpowiedź 1 w gałęzi R=0. Aparat przestaje realizować pierwotnie nazwany odczyt.

Nierówne niezerowe wagi wskazań zegara można objąć odpowiednio zmienionym więzem; nie zmieniają warunkowego wyniku (5). Ich równość w (3) jest wyborem tej wersji zegara, nie ukrytym wyprowadzeniem z ramy.

Wymagania do uruchomienia: Python 3.10 lub nowszy, `sympy`, `numpy`. Polecenie: `python test-domkniecia-2026-10-12.py`. Skrypt zapisuje szczegółowy wynik w `test-domkniecia-2026-10-12.json`.

## Źródła i pochodzenie konstrukcji

1. Plik główny projektu, R1a–R1c, 179, 207, 258–260, 263. Poprzedni rachunek: `jadro-z-relacji-2026-10-09.md`, zwłaszcza zakres wniosku dotyczącego samego singletu.
2. D. Bacon, J. Kempe, D. A. Lidar, K. B. Whaley, [Universal Fault-Tolerant Computation on Decoherence-Free Subspaces](https://arxiv.org/abs/quant-ph/9909058). Znany czteronośnikowy kod singletowy, operatory relacji par oraz możliwość realizacji operacji kodowanych oddziaływaniami par. Macierze użyte tutaj wyliczono niezależnie w załączonym skrypcie.
3. V. Giovannetti, S. Lloyd, L. Maccone, [Quantum Time](https://arxiv.org/abs/1504.04215), część o pomiarach. Odniesienie dla objęcia aparatu i sekwencyjnych zapisów wspólnym opisem oraz odczytu prawdopodobieństw warunkowych. Nie źródło dowodu wyboru dynamiki z ramy.
4. D. Aharonov i in., [Adiabatic Quantum Computation is Equivalent to Standard Quantum Computation](https://arxiv.org/abs/quant-ph/0405098). Standardowe narzędzie historii obwodu i więzów propagacji. Własność (4) udowodniono tutaj bez przyjmowania tezy o ontologii czasu.
