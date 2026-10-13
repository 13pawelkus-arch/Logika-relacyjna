# Kiedy zegar przenosi fazę: L, odstęp energii i wspólne korelacje

12.10.2026. Kontynuacja punktu 4 po doprecyzowaniu: badany proces wraz ze swoimi relacjami pełni rolę zegara; jego dynamika już zachodzi. Zadanie: sprawdzić podejrzenie użytkownika, że fazę przenosi tylko zegar o odpowiednim L.

**Wynik:** w równomiernej rodzinie z punktu 4 faza przechodzi przez dany odczyt, gdy obsadzony odcinek odniesienia obejmuje pary poziomów o wymaganej różnicy energii. Dla różnicy k odstępów drabiny warunek to L>k, a współczynnik wynosi max(L−k,0)/L. Nie wybrano jednego L ani równości L przygotowania i kolejnego odczytu. Samo L nie wystarcza: liczą się korelacje energetyczne, ich profil i dopasowanie do konkretnego instrumentu. W pełnym procesie faza może być odczytywalna wyłącznie we wspólnej korelacji, mimo diagonalnych lokalnych stanów obu odniesień.

**Kontrola:** PASS — 168 dokładnych kontroli. Sprawdzono pełne unitarne instrumenty, zachowanie energii oraz tożsamość efektu na całej dozwolonej podprzestrzeni wejść. Wzory nie pochodzą z dopasowania do kilku faz. Oczekiwanie i warunki upadku zapisano przed wykonaniem kontroli w `zalozenia-przed-kontrola.md`.

## 1. Znaczenie L i zakres tego sprawdzenia

L oznacza parametr odniesienia z punktu 4: długość obsadzonego odcinka drabiny energetycznej. W wyjściowej rodzinie wszystkie te poziomy były równomiernie obsadzone, a ich fazy narastały liniowo. Nie utożsamiamy tego L z najdłuższym łańcuchem z A2 ani z zewnętrznym czasem. Zmiana przygotowania na korelowane lub nierównomierne wymaga jawnego wskazania, co nadal oznacza L; tutaj pozostaje długością dostępnego odcinka, a profil amplitud zapisujemy oddzielnie.

Używamy tego samego relacyjnego pytania Z i unitarnego instrumentu z punktu 4. W bazie energii:

\[
H_S=k\varepsilon|1\rangle\langle1|,
\qquad H_A=\varepsilon N_A,
\qquad n=0,\ldots,L+2k-1,
\qquad H_R=0.
\]

k jest dodatnią liczbą całkowitą: wymaganym odstępem energii S wyrażonym w odstępach drabiny odniesienia. Ten sektor addytywnej energii i ta realizacja instrumentu pozostają jawnymi założeniami badanego procesu. \(\varepsilon\) nie jest tutaj wyprowadzoną masą.

Operację domykamy unitarnie w sektorach stałej energii k·s+n, bez sklejenia górnego i dolnego brzegu. Obsadzamy poziomy od k do k+L−1, więc każdy możliwy pojedynczy transfer energii ±k ma miejsce w drabinie. Przygotowanie i kolejny zapis używają dwóch wskazanych odniesień; nie zakładamy nieograniczonego używania jednego niezmienionego zasobu.

Wydzielenie S, odniesień p,o oraz wskaźników oznacza role we wspólnym procesie. Nie jest wyprowadzeniem osobnego napędu, źródła dynamiki ani obserwowalnego pełnego „stanu teraz”. Ustalenia R1a i 258 o wewnętrznej dynamice oraz globalnym zerze pozostają podstawą interpretacji.

## 2. Przenoszenie fazy wymaga dopasowanego przesunięcia

Niech \(T_{-k}|n\rangle=|n-k\rangle\) dla dostępnych poziomów, a poza drabiną wynik będzie zerowy. Dla przygotowania odniesienia o macierzy \(\rho_A\) współczynnik odczytu w naszym jednolitym instrumencie jest

\[
c_k=\operatorname{tr}(\rho_A T_{-k})
=\sum_n (\rho_A)_{n+k,n}.
\tag{1}
\]

Dla czystego pomocniczego zapisu \(|\chi\rangle=\sum_n a_n|n\rangle\) jest to \(c_k=\sum_n a_n^*a_{n+k}\). Efekt wyniku wskaźnika 0 ma w bazie energii postać

\[
E_0=\frac12\left[
I+Z_{\parallel}
+\frac{\sqrt3}{2}
\begin{pmatrix}0&c_k^*\\c_k&0\end{pmatrix}
\right],
\qquad Z_{\parallel}=\operatorname{diag}(-1/2,1/2).
\tag{2}
\]

W tym zapisie współczynnik przy składowej fazowej oraz charakter przygotowania są wynikiem tego samego instrumentu zachowującego energię. Nie dopisujemy c_k po wyliczeniu odpowiedzi.

Dopasowanie energetyczne wynika bezpośrednio z \([V,H_S+H_A]=0\): element macierzy mieszający \(|1,n\rangle\) z \(|0,m\rangle\) może być niezerowy tylko przy \(m-n=k\). Jeśli różnica energii S nie występuje jako różnica poziomów tego odniesienia, ta operacja nie ma kanału wymiany potrzebnego do wybranego odczytu. Sprawdzono drabinę o sześciu poziomach: różnice 1 i 2 mają odpowiednio pięć i cztery pary, a różnice 1/2 i √2 nie mają żadnej. To wniosek dla wskazanego wspólnego widma i prawa zachowania, nie zakaz innych widm lub innych realizacji procesu.

Podział koherencji według różnic energii jest zgodny z rozkładem na mody w [1, §III B, równania (4)–(6); §IV B, równanie (16)]. Stosujemy część wynikającą z symetrii, bez dodawania kąpieli termicznej.

## 3. Co ustala L w rodzinie z poprzedniego rachunku

Dla równomiernego liniowego przygotowania

\[
|\chi_{L,\phi}\rangle
=\frac1{\sqrt L}\sum_{n=k}^{k+L-1}e^{in\phi}|n\rangle
\]

nakładają się dokładnie max(L−k,0) par. Stąd

\[
c_k=\nu_{L,k}e^{ik\phi},
\qquad \nu_{L,k}=\frac{\max(L-k,0)}{L}.
\tag{3}
\]

| L | k=1: \(\nu_{L,1}\) | k=2: \(\nu_{L,2}\) |
|---:|---:|---:|
| 1 | 0 | 0 |
| 2 | 1/2 | 0 |
| 3 | 2/3 | 1/3 |
| 4 | 3/4 | 1/2 |

W badanym wcześniej procesie k=1: L=1 nie przenosi fazy przez to odniesienie, a każde L≥2 daje niezerowy kontrast. Przy k=2 próg wynosi L=3. Jest to wymóg zgodności zakresu odniesienia z procesem, a nie wybór jednego szczególnego L.

Dla dwóch iloczynowo przygotowanych odniesień i badanej dodatkowej względnej operacji \(U_q=\operatorname{diag}(1,q)\), \(q=e^{i\theta}\), pełny wynik to

\[
p(O=0\mid R=0)
=\frac58+\frac38\nu_{L_p,k}\nu_{L_o,k}
\cos\!\left[\theta+k(\phi_p-\phi_o)\right].
\tag{4}
\]

Oznaczenie fazy jest takie jak w punkcie 4: chodzi o fazę względną całego porównania. Wspólny postęp faz S i jego odniesień nie staje się dodatkowym sygnałem. Dla tej równomiernej rodziny faza jest odczytywalna, gdy oba L przekraczają k; równość L_p=L_o nie jest wymagana. Przykład L_p=2,L_o=3,k=1 daje \(p=5/8+(1/8)\cos\Theta\).

Idealny kontrast tej rodziny wymaga granicy L→∞. Skończone L daje niezerową, lecz słabszą zależność od fazy. Nie oznacza to wyprowadzenia częściowości odczytu z pojemności: częściowość z poprawki 207 i dokładność wybranego pytania w konkretnym aparacie to różne twierdzenia.

## 4. To samo L może dawać różny odczyt

Dla L=3 i k=1 porównaliśmy trzy czyste profile oraz stan po usunięciu koherencji. Wektory poniżej opisują amplitudy kolejnych trzech obsadzonych poziomów przy wspólnym ustawieniu fazy:

| Przygotowanie odniesienia | Amplitudy / opis | \(c_1\) |
|---|---|---:|
| Równomierne liniowe | \((1,1,1)/\sqrt3\) | 2/3 |
| Inny profil wag | \((1/2,1/\sqrt2,1/2)\) | \(1/\sqrt2\) |
| Zniesienie w tym instrumencie | \((1,1,-1)/\sqrt3\) | 0 |
| Usunięta koherencja | równomierna mieszanina trzech energii | 0 |

Pierwszy, trzeci i czwarty przypadek mają ten sam rozkład energii, tę samą średnią i wariancję \(2\varepsilon^2/3\). Dają jednak różny sygnał fazowy. W trzecim przypadku składniki koherencji między sąsiadami znoszą się w sumie (1), ale \(c_2=-1/3\): ten sam profil odpowiada na odczyt wymagający innego odstępu.

**Ważny zakres:** zerowe c_1 w trzecim wierszu nie oznacza, że cały operator pierwszego modu koherencji jest zerowy. Poszczególne elementy pozostają niezerowe. Wynik mówi o ich nakładaniu w naszym jednolitym instrumencie; inny fizyczny odczyt może ważyć je inaczej. Nie przenosimy braku sygnału jednego pytania na „brak fazy w strukturze”.

Przy tych samych L_p=L_o=3 pełny wynik dla liniowego równomiernego przygotowania ma współczynnik kosinusa 1/6, dla drugiego profilu 3/16, a dla trzeciego przy k=1 — zero. L ogranicza możliwości, ale nie określa samodzielnie odpowiedzi.

## 5. Warunek dla całego procesu: faza może być wyłącznie w relacji

Wzór (4) dotyczy przygotowania iloczynowego. Dla dowolnego wspólnego przygotowania \(\rho_{po}\) obu odniesień, wspieranego na tych samych dozwolonych odcinkach, pełny efekt daje

\[
C_{po}^{(k)}
=\operatorname{tr}\!\left[
\rho_{po}(T_{-k}^{p}\otimes T_{+k}^{o})
\right],
\tag{5}
\]

\[
\boxed{
p(O=0\mid R=0)
=\frac58+\frac38\operatorname{Re}\!\left(q C_{po}^{(k)}\right).
}
\tag{6}
\]

Dla stanu iloczynowego \(C_{po}^{(k)}=c_k^p(c_k^o)^*\), więc odzyskujemy (4). W ogólnym przypadku taki iloczyn nie jest uprawniony. **Dla wybranego instrumentu konieczny i wystarczający warunek niestałej zależności od q to \(C_{po}^{(k)}\ne0\).** Skrypt sprawdza tożsamość pełnego efektu jako macierzy na całej dopuszczalnej podprzestrzeni odniesień. Obejmuje to dowolne stany mieszane i korelowane, a nie tylko sprawdzone przykłady.

Przykład dla k=1 oraz odcinków o L_p=L_o=2:

\[
|\Xi_\alpha\rangle
=\frac{|1\rangle_p|2\rangle_o
+e^{i\alpha}|2\rangle_p|1\rangle_o}{\sqrt2}.
\]

Każdy lokalny stan odniesienia jest diagonalny: \(\rho_p=\rho_o=I_2/2\), więc \(c_1^p=c_1^o=0\). Jednak

\[
(N_p+N_o)|\Xi_\alpha\rangle=3|\Xi_\alpha\rangle,
\qquad C_{po}^{(1)}=\frac12e^{i\alpha},
\]

\[
p=\frac58+\frac3{16}\cos(\theta+\alpha).
\tag{7}
\]

Oba lokalne opisy pomijają fazę, a wspólny odczyt ją zachowuje. Przy \(\theta+\alpha=0\) wynik wynosi 13/16, a przy π — 7/16. Usunięcie koherencji między \(|1,2\rangle\) i \(|2,1\rangle\) zachowuje wszystkie populacje i lokalne stany, lecz daje stałe 5/8.

Operator w (5) komutuje z sumą energii odniesień: jedno przesunięcie oddaje dokładnie energię pobieraną przez drugie. Faza α jest zatem relacją wewnątrz ostrego sektora wspólnej energii, nie orientacją wobec zewnętrznego zegara. Usunięcie koherencji pomiędzy różnymi całkowitymi energiami nie zmienia odczytu — sprawdzono to dla tego przykładu oraz dla równomiernego przygotowania iloczynowego.

To realizuje doprecyzowanie użytkownika: weryfikujemy proces wraz z relacjami jako zegar. Samo badanie lokalnego „zegara p” albo „zegara o” zgubiłoby informację potrzebną do następnego odczytu. Nie wyprowadzamy stąd dostępności całego wspólnego stanu dla czytającego.

## 6. Odpowiedź na podejrzenie i następny zakres pracy

Podejrzenie jest trafne jako warunek dopasowania odniesienia do badanego procesu. W liniowej równomiernej rodzinie to L>k. Silniejsze zdanie, że liczba L sama wybiera przenoszoną fazę, nie przeszło kontroli: inne profile i korelacje przy tym samym L dają inne wyniki. Ogólnym warunkiem dla tego pełnego odczytu jest niezerowy korelator (5).

Uzyskaliśmy konkretną zależność fazy i wagi z pełnej relacji przygotowania–zapisu–odczytu. Nie otwieramy ponownie ustalonej autonomii dynamiki. Dalszy audyt dotyczy tego, czy przyjęty instrument i jego korelator wiernie wyrażają domknięcie wymagane przez ramę, oraz co wynika z niego po zmianie realizacji procesu. Liczby 5/8 i 3/8 należą do użytego pytania i instrumentu; nie są wykazane jako uniwersalne wagi wszystkich procesów.

## 7. Kontrola i źródła

Skrypt `faza-L-kontrola-2026-10-12.py` wykonuje 168 kontroli dokładnych, wyłącznie z algebrą symboliczną. Wynik szczegółowy zapisuje w JSON o tej samej nazwie. Nowe sprawdzenia obejmują wymagane odstępy k=1,2,3; fazy są traktowane jako zespolone zmienne na okręgu jednostkowym. Dla każdego użytego instrumentu sprawdzono unitarność, zachowanie energii, zupełność wyników, efekt i przygotowanie. Dla pełnego procesu sprawdzono tożsamość operatorową także dla ogólnego korelowanego wejścia.

Dowody stanowią sektorowy warunek wymiany energii, zliczenie nakładających się par w (3) oraz tożsamość pełnego efektu w (6). Liczba kontroli nie jest samodzielnym dowodem ramy.

Kontynuowane wyniki: `punkt4-przygotowanie-energia-zapis-2026-10-12.md`, `test-domkniecia-2026-10-12.md`, poprawki 207 i 258 oraz R1a–R1f w `logika-relacyjna-v3.5.md`.

1. [Lostaglio, Korzekwa, Jennings, Rudolph — *Quantum coherence, time-translation symmetry and thermodynamics*, arXiv:1410.4572v2](https://arxiv.org/pdf/1410.4572). Sprawdzone: §III B, (4)–(6), oraz §IV B, (16), o rozkładzie i dopasowaniu różnic energii przy kowariantnym przetwarzaniu koherencji. Własne wzory dla instrumentu pochodzą z obecnej kontroli.
2. [Åberg — *Catalytic Coherence*, arXiv:1304.1060](https://arxiv.org/abs/1304.1060). Sprawdzony abstrakt jako odniesienie dla możliwości stosowania koherentnych odniesień przy zachowaniu energii; nie używamy tezy o nieograniczonej katalizie ani o braku narastających korelacji.
