# Jądro i wagi z jednej pełnej relacji — krok 259

09.10.2026. Kontynuacja 257 po przyjęciu doprecyzowania 258. Pochodzenie: wyprowadzenie asystenta [A][T]; kontrola dokładna [P]; standardowe narzędzia operatorowe [L]. Definicje czasu i 3D z R1a–R1c pozostają podstawą. Wszystkie argumenty i współczynniki poniżej są bezwymiarowe.

## Oczekiwanie i warunek upadku — przed kontrolami

**Spodziewam się:** po zadaniu pełnej relacji nośników i sposobu odczytu jądro odpowiedzi oraz względne wagi przejść wynikają z tej samej relacji. Nie trzeba wybierać ich osobno. Unitarność daje równanie sprawdzające całe przyporządkowanie, silniejsze niż symetria i druga wariacja rozpatrywane oddzielnie. Sam ostry więz globalny z 258 nadal nie wybiera konkretnej relacji.

**Zdanie o upadku:** konstrukcja upada, jeśli dla tego samego pełnego procesu, tych samych kanałów i tej samej normalizacji można niezależnie zmienić wagi przejść, zachowując całą odpowiedź. Test unitarnej realizacji upada, jeśli wyprowadzona macierz Grama nie jest dodatnia dla dowolnego zestawu argumentów i wejść. Twierdzenie o odtworzeniu wnętrza wymaga osiągalności z wejść; bez niej nie wolno twierdzić, że odczyt wyznacza całe wnętrze.

**Wejścia:** skończony, nazwany proces odwracalny na nośnikach R1b/179; jego pełny operator unitarny U; ortogonalny wybór kanałów wejścia/wyjścia i pozostałych kanałów; protokół zachowujący koherencję oraz normalizację. Dla szeregu jednego argumentu wybieramy sektor, w którym ta sama komórka relacji występuje w kolejnych spotkaniach. To jawny wybór sektora, nie twierdzenie o jednorodności wszystkich relacji. Skończoność przykładu nie jest skończoną pojemnością świata ani nowym N z 207.

**Odczyt:** różnica stanów własnych znanego O, wywołana przez pełną odpowiedź przy wskazanych przygotowaniach i efektach (206). Zespolona odpowiedź wymaga odniesienia fazowego i koherentnego porównania także między odczytami. Same liczby zdarzeń ani tomografia kanału w jednym ustawieniu nie wyznaczają wszystkich tych faz. Nie przypisujemy cech M na podstawie odczytu O.

**Zakres:** uzasadnienie przejścia od zadanej relacji do jądra i wag, oraz test dopuszczalności proponowanej odpowiedzi. Nie uznajemy wyboru rzeczywistych relacji, pełnego działania QED, modów, stanu swobodnego i reguły Wicka za wyprowadzone z samej ramy. O Ø nie stwierdzamy obecności ani nieobecności czegokolwiek.

## 1. Rozdzielenie kanałów i pełna odpowiedź

Na przestrzeni znanego procesu wybieramy rozkład ortogonalny \(\mathcal H=\mathcal P\oplus\mathcal Q\). Są to **podprzestrzenie kanałów**, nie automatycznie podukłady tensorowe M i O. Eliminacja amplitud Q nie jest śladem częściowym macierzy gęstości. Dla odczytu mieszanego trzeba zachować cały kanał i wszystkie odpowiednie składniki, nie jeden wybrany operator Krausa.

Zapis pełnej relacji:

\[
U=\begin{pmatrix}A&B\\C&D\end{pmatrix},\qquad U^\dagger U=UU^\dagger=I.
\]

U może być złożeniem znanych relacji par z 179. W rozpatrywanym powtarzalnym sektorze amplitudy spełniają

\[
\binom{y_n}{x_{n+1}}=U\binom{v_n}{x_n},\qquad x_0=0.
\]

\(v_n\) i \(y_n\) to przygotowanie i odpowiedź kanałów P, a \(x_n\) to amplituda w kanałach Q w tym nazwanym protokole. Warunek \(x_0=0\) określa przygotowanie procesu, nie zawartość nierozróżnialnej całości. n zlicza uporządkowane spotkania nośników; nie jest zewnętrzną osią czasu ani sekundą. Każde spotkanie ma własne miejsce w porządku. Powrót do tego samego typu kanału nie oznacza cyklu przyczynowego w 179.

Wprowadźmy argument szeregu z, przy \(\lvert z\rvert<1\). Jest to narzędzie sumowania liczby przejść, **nie dodatkowe sprzężenie hop-stop**. Na brzegu koło fazowe opisuje koherentne porównanie względem wskazanego odniesienia O; wnętrze dysku pozwala prowadzić rachunek bez problemów zbieżności. Z równań komórki dostajemy

\[
X(z)=(I-zD)^{-1}C,\qquad
\boxed{T(z)=A+zB(I-zD)^{-1}C}.
\tag{1}
\]

Dokładniej, dla szeregów wejść i wyjść \(y(z)=T(z)v(z)\), natomiast wewnętrzny szereg to \(x(z)=zX(z)v(z)\). Stąd

\[
T(z)=A+\sum_{n\ge1}z^n\,BD^{n-1}C.
\tag{2}
\]

**Wagi odpowiedzi to \(BD^{n-1}C\), nie niezależne liczby dopisane do jądra.** Macierze C, D i B opisują odpowiednio wejście do pomijanych kanałów, kolejne przejścia w nich i wyjście. Są amplitudami; mogą być zespolone i mieć znaki. Dodatniość dotyczy pełnego odczytu i macierzy Grama, nie każdej amplitudy osobno.

Unitarność daje też dla dowolnej skończonej sekwencji

\[
\sum_{n=0}^{N}\|v_n\|^2
=\sum_{n=0}^{N}\|y_n\|^2+\|x_{N+1}\|^2.
\tag{3}
\]

Nie tracimy normy całości, choć część odpowiedzi może pozostać w kanałach nieobjętych danym odczytem. To rachunek na określonym procesie, nie wniosek o Ø.

Jeżeli poszczególne n zostają rozróżnione i zapisane w niezależnych kanałach aparatu, odczyt sumuje odpowiednie prawdopodobieństwa. Suma amplitud (2) opisuje inny, jawnie **koherentny** protokół. Nie wolno przechodzić między nimi bez wskazania aparatu.

## 2. Równanie wierności i test wag

Bez rozwijania ani obcinania (1) mamy

\[
U\binom{v}{zX(z)v}=\binom{T(z)v}{X(z)v}.
\]

Zachowanie iloczynu skalarnego dla dwóch takich wektorów daje

\[
\boxed{I-T(w)^\dagger T(z)
=(1-\bar wz)X(w)^\dagger X(z)}.
\tag{4}
\]

Zdefiniujmy

\[
\mathcal G(w,z)=\frac{I-T(w)^\dagger T(z)}{1-\bar wz}.
\tag{5}
\]

Dla dowolnych \(z_1,\ldots,z_m\) wewnątrz dysku i wektorów \(v_1,\ldots,v_m\):

\[
\sum_{i,j}v_i^\dagger\mathcal G(z_i,z_j)v_j
=\left\|\sum_jX(z_j)v_j\right\|^2\ge0.
\tag{6}
\]

To dowód na **wszystkich argumentach**, nie wniosek z prób. Dla jednego argumentu \(T(z)^\dagger T(z)\preceq I\). Dla wielu dostajemy dodatkowe zgodności między różnymi ustawieniami. Ujemna macierz (5) wyklucza znormalizowaną realizację unitarną proponowanej odpowiedzi w tym protokole. Dodatniość skończonej listy prób jest tylko konieczną kontrolą, nie pełnym dowodem dopuszczalności ani wyboru działania.

Na brzegu, gdzie istnieje odwrotność w (1), \(T(z)^\dagger T(z)=I\). Przy biegunach należy zbadać granicę i sektory osiągalne. Nie usuwać części urojonych ani wag przed sprawdzeniem (4).

**Wierność wobec ramy:** przy niezmienionej pełnej relacji zmiana (2) łamie składanie amplitud tej relacji. Proponowana odpowiedź łamiąca (6) nie może być jej częściowym odczytem z zachowaną normą. To konkretny test dla 128. Nie jest to jeszcze dowód, że wszystkie procesy dozwolone przez ramę mają ten sam U.

Nie należy stosować \(T^\dagger T\preceq I\) wprost do surowego propagatora pola \(D^{-1}\). Propagator nie jest znormalizowaną macierzą przejścia aparatu. Najpierw trzeba wyprowadzić przyporządkowanie propagatora, przygotowań i efektów do pełnego odczytu.

## 3. Ile wnętrza wyznacza pełna odpowiedź?

Niech przestrzeń osiągalna będzie

\[
\mathcal R=\operatorname{span}\{D^nCv:n\ge0,\ v\in\mathcal P\}.
\]

W skończonym przypadku jest ona zamknięta i D-niezmiennicza. U odwzorowuje \(\mathcal P\oplus\mathcal R\) w siebie. Unitarność i równość wymiarów czynią ten podzbiór redukującym: jego dopełnienie nie sprzęga się z wejściami ani wyjściami P. Można ograniczyć realizację do \(\mathcal P\oplus\mathcal R\).

**Twierdzenie w tym zakresie:** dwie skończone realizacje unitarne z tą samą pełną zespoloną funkcją T i osiągalnymi całymi przestrzeniami Q różnią się wyłącznie unitarnym wyborem bazy w Q.

Dowód: z (4) ta sama T wyznacza te same iloczyny skalarne wszystkich \(X(z)v\). Przyporządkowanie \(X_1(z)v\mapsto X_2(z)v\) jest dobrze określoną izometrią na ich liniowych kombinacjach. Rozwinięcie \(X(z)=\sum_{n\ge0}z^nD^nC\) pokazuje, że rozpinają przestrzenie osiągalne. Otrzymujemy operator unitarny W. Porównanie współczynników daje \(C_2=WC_1\), \(D_2W=WD_1\). Z \(T_2=T_1\) wynika \(A_2=A_1\) oraz \(B_2W=B_1\), ponieważ współczynniki \(D_1^nC_1v\) rozpinają Q. Zatem

\[
U_2=(I\oplus W)U_1(I\oplus W^\dagger).
\tag{7}
\]

Tu „minimalna realizacja” oznacza osiągalność z **nazwanych wejść**, nie najprostsze działanie jako dodatkowy aksjomat. Rząd pełnej macierzy Grama mierzy wymiar osiągalnej realizacji w tym protokole; nie liczbę wszystkich nośników M ani pojemność przestrzeni z 207.

To nie unieważnia 179, 205 ani zdania „informacja o stanie nie jest stanem”. Niewidoczne sektory pozostają nieokreślone przez T. Ponadto poznanie pojedynczego kanału \(\rho\mapsto\Lambda(\rho)\) nie jest poznaniem całej koherentnej funkcji T(z) z fazami porównanymi między argumentami. Nie uzyskaliśmy dostępu do całej rzeczywistości.

## 4. Przykład zgodny z globalnym zerem 258

**Dodatkowe oczekiwanie, zapisane przed kontrolą równań komutacji:** w izotropowym sektorze dokładnie dwóch nośników, bez dodatkowego kierunku, wymaganie komutacji ze wszystkimi wspólnymi obrotami powinno ograniczyć pełną relację do dwóch kanałów: singletowego i trypletowego. Zdanie o upadku: istnieje operator komutujący ze wszystkimi J_i poza rozpięciem projektorów tych dwóch kanałów. To skończony układ liniowy na wszystkich 16 zespolonych współczynnikach operatora, nie próbkowanie relacji. Izotropia całego operatora jest jawnym warunkiem sektora; nie wynika z samej niezmienniczości jednego stanu.

Na dwóch nośnikach bierzemy projektor singletu

\[
P_s=\frac12\begin{pmatrix}
0&0&0&0\\0&1&-1&0\\0&-1&1&0\\0&0&0&0
\end{pmatrix},\qquad P_t=I-P_s,
\quad U_q=P_s+qP_t,\quad\lvert q\rvert=1.
\]

Dla każdego q: U jest unitarne, \([U_q,J_i]=0\), \(U_qP_s=P_s\), \(J_iP_s=0\). Singlet i jego lokalne wariancje/kowariancje pozostają dokładnie takie jak w 258. Zachowana jest pełna symetria wspólnych obrotów, nie tylko jedna wybrana oś.

**W tej nazwanej klasie to wszystkie możliwości.** Komutacja z J_3 najpierw zachowuje jego przestrzenie własne: \(\lvert00\rangle\), rozpięcie \(\lvert01\rangle,\lvert10\rangle\), oraz \(\lvert11\rangle\). Operatory \(J_1\pm iJ_2\) łączą trzy stany trypletowe, więc komutujący operator ma na nich ten sam współczynnik. Singlet jest zerowany przez wszystkie J_i i ma osobny współczynnik. Otrzymujemy

\[
[U,J_i]=0\ (i=1,2,3)\quad\Longleftrightarrow\quad
U=u_sP_s+u_tP_t.
\tag{8a}
\]

Unitarność wymaga \(\lvert u_s\rvert=\lvert u_t\rvert=1\). Dodatkowy warunek **UΨ_s=Ψ_s**, silniejszy niż zachowanie samego projektora stanu, ustala \(u_s=1\); wtedy pozostaje właśnie U_q. Analogicznie hermitowski generator z \([H,J_i]=0\) i \(HΨ_s=0\) ma postać **H=ηP_t**, η rzeczywiste. η nie jest tu wyprowadzoną masą: to nieustalona wartość generatora w drugim kanale.

To warunkowy wybór klasy relacji z symetrii całego operatora, mocniejszy od warunku dotyczącego jednego singletowego przygotowania. Nie rozciągamy go na relacje z kierunkiem odczytu, dodatkowymi odniesieniami ani na pełne jądra Diraca i Maxwella. Wszystkie równania komutacji mają rząd 14 i dwuwymiarowe rozwiązanie rozpięte przez P_s,P_t; kontrola poniżej rozwiązuje cały układ dokładnie.

Wybieramy kanały P: \(00,01\), Q: \(10,11\). Przy \(a=(1+q)/2\), \(b=(q-1)/2\):

\[
A=\operatorname{diag}(q,a),\quad D=\operatorname{diag}(a,q),\quad
B=\begin{pmatrix}0&0\\b&0\end{pmatrix},\quad
C=\begin{pmatrix}0&b\\0&0\end{pmatrix}.
\]

Wynika

\[
\boxed{T_q(z)=\operatorname{diag}\left(q,\frac{a-qz}{1-az}\right)}.
\tag{8}
\]

Przy q różnym od 1 przestrzeń osiągalna w Q jest jednowymiarowa; drugi kanał Q nie jest osiągalny. Macierz Grama ma rząd 1. Ewentualny biegun jego niezależnej fazy w pełnym zapisie nie jest biegunem odpowiedzi (8).

Kontrole użyją dokładnych wartości syntetycznych \(q=i\) i \(q=(3+4i)/5\). Obie relacje zachowują ten sam singlet i wszystkie trzy ostre więzy, a dają różne pełne odpowiedzi. Przy z=1:

\[
T_q(1)=\operatorname{diag}(q,1).
\]

Przy przygotowaniu P w \(\lvert+\rangle=(1,1)^T/\sqrt2\) i odczycie efektu \(\lvert+\rangle\langle+\rvert\) prawdopodobieństwo to \((1+\operatorname{Re}q)/2\): odpowiednio **1/2 i 4/5**. Są to różne odczyty względnej fazy przez wskazany aparat, nie pomiary fazy absolutnej.

**Znaczenie:** sam stan z więzem nie wybiera reakcji na wszystkie inne przygotowania. Zmiana q zmienia relację U; nie zmienia wagi przy zachowaniu wszystkich relacji. Rodzina nie jest kontrmodelem całej ramy ani postulatem nowego sprzężenia fizycznego.

**Zakres przygotowań jest istotny:** porównanie 1/2 i 4/5 używa przygotowania kanałów P innego niż singlet. Jeżeli wszystkie trzy ostre więzy J_i mają ograniczać każdy dopuszczalny stan całego układu dwóch nośników, jego przestrzeń fizyczna jest tutaj jednowymiarowa i oba U_q działają na niej identycznie. Nie otrzymaliśmy dwóch różnych odczytów tego samego singletu pod U_q. Przykład pokazuje swobodę operatora poza wskazanym stanem z więzem. Przeniesienie takiego testu na stan z aparatem wymaga określenia pełnej relacji aparatu i jej więzów; nie wykonano tego przez sam wybór P.

### Jawny upadek niezależnego przeważenia

Zachowajmy A, B, C, D, lecz podwójmy amplitudę każdej drogi przez Q:

\[
T_{\rm bad}(z)=A+2zB(I-zD)^{-1}C.
\]

Dla q=i, z=1 drugi składnik wynosi \(3/2-i/2\). Przy jednostkowym wejściu drugiego kanału i odpowiadającym mu efekcie daje **5/2**, co łamie normalizację odczytu. Ponowna normalizacja byłaby innym protokołem.

Upadek zachodzi też ściśle wewnątrz dysku: dla z=4/5 drugi składnik to \((29-11i)/26\), a

\[
1-\left\lvert\frac{29-11i}{26}\right\rvert^2=-\frac{143}{338}<0.
\tag{9}
\]

Jednopunktowa macierz (5) jest ujemna na tym wejściu. Tak przyporządkowane wagi nie dopuszczają żadnej znormalizowanej unitarnej realizacji w rozpatrywanym protokole. To dokładne odrzucenie, nie szukanie błędu na losowych próbach. Inne zmiany wag mogą odpowiadać innym procesom — samo to nie jest sprzecznością.

**Wspólna zgodność jest silniejsza niż normalizacja każdego odczytu osobno.** Dla trzech skalarnych argumentów z=(0,1/2,i/2) przypiszmy wartości T=(0,1/2,−i/2). Każda ma moduł nie większy od 1, ale macierz (5) ma wyznacznik −4/17. Taki zestaw odczytów nie może pochodzić z jednej pełnej relacji w tym protokole. Jest to warunek na wspólne pochodzenie całej odpowiedzi, nie tylko na pojedyncze prawdopodobieństwo.

## 5. Most do jądra kwadratowego: eliminacja tej samej relacji

Jeżeli mamy już określony hermitowski generator H w reprezentacji względem wskazanego wewnętrznego odczytu, jego rozkład ma postać

\[
H=\begin{pmatrix}A_H&B_H\\B_H^\dagger&C_H\end{pmatrix}.
\]

Pojedyncze U nie wybiera jednoznacznie H: logarytm unitarny ma różne gałęzie. Potrzebna jest pełna rodzina relacji i jej przyporządkowanie do odczytu. H w tej części jest jawnym wejściem; nie uzyskaliśmy dodatkowej osi czasu.

Dla bezwymiarowego argumentu spektralnego \(\zeta\) poza widmem \(C_H\) rozwiązanie części Q równania \((\zeta I-H)(v,x)^T=(j,0)^T\) daje

\[
x=(\zeta I-C_H)^{-1}B_H^\dagger v,
\]

\[
\boxed{D_{\rm eff}(\zeta)=\zeta I-A_H-
B_H(\zeta I-C_H)^{-1}B_H^\dagger}.
\tag{10}
\]

Jeżeli cała odwrotność istnieje, to

\[
P(\zeta I-H)^{-1}P\big|_{\mathcal P}=D_{\rm eff}(\zeta)^{-1}.
\tag{11}
\]

To eliminacja stacjonarna jednego jądra kwadratowego, czyli dopełnienie Schura. Dla rzeczywistego \(\zeta\) poza widmem wynika też ze stacjonarności odpowiedniej formy kwadratowej; dla zespolonego \(\zeta\) używamy jej analitycznej odwrotności. **Nie nazywamy tej formy wyprowadzonym fundamentalnym działaniem świata.**

Spektralny rozkład części Q ustala jednocześnie bieguny i ich wagi:

\[
\Sigma_P(\zeta)=B_H(\zeta I-C_H)^{-1}B_H^\dagger
=\sum_\lambda\frac{W_\lambda}{\zeta-\lambda},\qquad
\boxed{W_\lambda=B_H\Pi_\lambda B_H^\dagger\succeq0}.
\tag{12}
\]

Waga jest Gramem sprzężeń z danym kanałem spektralnym, nie osobną poprawką dobraną po ustaleniu mianownika. \(\Pi_\lambda\) obejmuje cały podzbiór zdegenerowany; waga nie zależy od wyboru bazy w nim. Kanał niesprzęgnięty daje wagę 0. Dla \(\zeta=x+iy\), y>0:

\[
\operatorname{Im}\Sigma_P(\zeta)=
-yB_H\big[(xI-C_H)^2+y^2I\big]^{-1}B_H^\dagger\preceq0.
\tag{13}
\]

Momenty \(M_n=B_HC_H^nB_H^\dagger\) spełniają też \([M_{i+j}]_{i,j\ge0}\succeq0\) dla każdego skończonego bloku: to Gram wektorów \(C_H^iB_H^\dagger v_i\). Pełna odpowiedź zachowuje zależność spektralną i część urojoną. Sam pierwszy rząd zadanej relacji nie uprawnia do zastąpienia jej zredukowanej odpowiedzi wielomianem pierwszego rzędu.

**Granica zastosowania do 256–257:** \(\Sigma_P\) jest dopełnieniem konkretnego hermitowskiego generatora, nie automatycznie samą Feynmanowską energią własną fermionu. Dodatniość (12) nie dotyczy oddzielnie każdego współczynnika Diracowskiego ani każdej wagi pętli. Nie wybiera stanu, statystyki, Feynmanowskiego i0, oddziaływań wyższego rzędu ani reguły Wicka. Uzasadnienie ich przyporządkowania relacjom 179 pozostaje otwarte.

### Jawne dwa bieguny przy globalnym zerze

W tym samym przykładzie wybierzmy \(H=P_t\). \(HP_s=0\), H jest hermitowskie i komutuje ze wszystkimi \(J_i\). Dla powyższych kanałów:

\[
A_H=\operatorname{diag}(1,1/2),\quad
C_H=\operatorname{diag}(1/2,1),\quad
B_H=\begin{pmatrix}0&0\\1/2&0\end{pmatrix}.
\]

\[
\Sigma_P(\zeta)=\operatorname{diag}\left(0,\frac{1/4}{\zeta-1/2}\right),
\]

\[
\left[D_{\rm eff}(\zeta)^{-1}\right]_{22}
=\frac{\zeta-1/2}{\zeta(\zeta-1)}
=\frac12\left(\frac1\zeta+\frac1{\zeta-1}\right).
\tag{14}
\]

Oba bieguny i obie wagi 1/2 są z tej samej relacji. Zero generatora na singletowym stanie całości nie ustawia lokalnej odpowiedzi na zero. Dla \(\zeta=1/2\) eliminacja zapisana w (10) nie istnieje, choć rzut pełnej odwrotności ma regularną wartość: trzeba użyć (11) lub granicy (14). Nie nazywamy tych syntetycznych wartości masami cząstek.

## 6. Wynik i dokładnie pozostała luka

| Pytanie | Wynik w 259 |
|---|---|
| Jak przyporządkować jądro i wagi jednej zadanej pełnej relacji? | Przez eliminację pozostałych kanałów: (1)–(2) lub (10)–(12). Wagi nie są osobnym wyborem przy stałej relacji. |
| Jak odrzucić niespójne przyporządkowanie? | Sprawdzić pełne równanie (4), dodatniość (6), albo warunki spektralne (12)–(13) w odpowiedniej reprezentacji. Podwojenie wag daje dokładny upadek (9). |
| Czy pełna odpowiedź wyznacza relację? | Dla skończonej realizacji osiągalnej z wejść — do wewnętrznej zmiany bazy (7). Pełne fazy i protokół są konieczne. |
| Czy globalne ostre zero wybiera U i jądro? | Nie samo to: przykład (8) zachowuje wszystkie więzy singletu i różni odpowiedzi na inne przygotowania. |
| Czy wybrano rzeczywiste U, H i działanie QED z R1a–R1c? | Nie. Uzyskano regułę przyporządkowania i test wierności, nie wybór całej relacji. |

**Następne konkretne miejsce pracy:** na relacjach par z 179 wskazać, które przygotowania, kanały i porównania faz odtwarzają pełne jądra L/R oraz EM z 257. Potem zastosować powyższe równania do tej samej odpowiedzi. Nie wolno najpierw przyjąć kanonicznego działania i uznać jego realizowalności za wyprowadzenie wyboru działania. α pozostaje znanym odczytem na obecnym etapie (253); trójka 256, bilans 208, [104], hierarchia, 3/2 i pełny drugi rząd zachowują swój status.

## 7. Kontrole i źródła narzędzi

Kontrole zostały zaplanowane po zapisaniu powyższego oczekiwania i zakresu, przed wykonaniem. Skrypt `jadro-z-relacji-kontrola-2026-10-09.py` używa tylko biblioteki standardowej i dokładnych liczb zespolonych o wymiernych składowych. **Wykonanie: PASS, bez tolerancji numerycznej.** Wynik zapisano w `jadro-z-relacji-kontrola-2026-10-09.json`. Sprawdzone są równania, nie wybór teorii z próbek.

| Kontrola | Wykonany zakres |
|---|---|
| Ostre więzy singletu i fluktuacje części | Wszystkie trzy J_i; lokalne wariancje 1/4, kowariancje −1/4; dwie relacje U_q komutujące ze wszystkimi J_i |
| Wybór klasy w izotropowym sektorze | Cały układ 48 równań zespolonych komutacji na 16 współczynnikach; rząd 14, rozwiązania rozpięte przez P_s,P_t; po HΨ_s=0 rząd 15, rozwiązania proporcjonalne do P_t |
| Pełna odpowiedź i Gram | Trzy procesy, w tym realizacja o całej osiągalnej przestrzeni Q; 75 par argumentów; trzy macierze 10×10 równe dokładnie E†E, rzędy 1, 1, 2 |
| Pełna propagacja i norma | 18 współczynników z niezależnej propagacji impulsem przez całe U; 12 kroków bilansu normy |
| Zmiana bazy Q | 15 porównań pełnej odpowiedzi i wewnętrznych amplitud po nietrywialnym obrocie Q |
| Brzeg i odczyt fazy | Sześć kontroli unitarności; odczyty 1/2 i 4/5 w podanym protokole |
| Odrzucenie niespójnych wag | 5/2, ujemny deficyt −143/338 i zestaw trzech osobno znormalizowanych wartości z wyznacznikiem Grama −4/17 |
| Dopełnienie Schura | Dwa hermitowskie generatory; dziesięć porównań z rzutem niezależnie odwróconej pełnej macierzy; sześć części urojonych w górnej półpłaszczyźnie |
| Pełne wagi spektralne | Dwie macierze momentów 8×8 równe E†E; dwie dodatnie macierze wag, trzy pełne sumy spektralne; cztery rozkłady (14) i regularny rzut przy ζ=1/2 |

Narzędzia porównawcze [L], bez importowania ich interpretacji czasu i przestrzeni:

- M. A. Dritschel, S. McCullough, [Test Functions, Kernels, Realizations and Interpolation](https://arxiv.org/abs/math/0612608), wprowadzenie i lemma 2.1: standardowe powiązanie funkcji przejścia, unitarnej realizacji i dodatnich jąder. W (1) kolejność bloków jest zamieniona względem zapisu autorów; dowód (4)–(7) podano wprost dla używanej konwencji.
- M. Griesemer, D. Hasler, [On the Smooth Feshbach–Schur Map](https://web.ma.utexas.edu/mp_arc/c/07/07-102.pdf), wprowadzenie, równanie (1): eliminacja bloków i odwrotność. Tu wystarcza zwykły ortogonalny, skończony rozkład; nie korzystamy z gładkich odcięć ani modelu nierelatywistycznego QED z tej pracy.

Równania (1)–(14) i zakres ich odniesienia do źródeł projektu są wyprowadzeniem tej noty; literatura potwierdza standardowe narzędzia, nie dowodzi wyboru ramy ani mas.
