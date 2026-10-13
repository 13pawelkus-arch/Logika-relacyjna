# Punkt 4: przygotowanie, energia i zapis wewnętrznego czytającego

12.10.2026. Rozwinięcie punktu 4 raportu `test-domkniecia-2026-10-12.md`. Podstawa projektu: R1a–R1c łącznie, R1f-2, D2, 179, 207, 258–260.

**Wynik:** idealny CNOT z poprzedniego modelu jest poprawną operacją kwantową, ale sam nie stanowi energetycznego domknięcia aparatu. W nazwanym sektorze z addytywną, zachowaną energią taki dokładny i powtarzalny zapis badanego odczytu jest niedopuszczalny. Zbudowano jego przybliżoną realizację z wewnętrznym odniesieniem fazowym, dokładnie zachowującą energię. Pełny wynik zależy od fazy względnej całego porównania oraz od koherencji odniesień przygotowania i odczytu.

**Doprecyzowanie poprzedniego wniosku o fazie:** zmiana fazy badanego modułu przy niezmienionych fizycznych odniesieniach może być rozróżnialna. Wspólnego postępu fazy modułu i odniesienia nie wolno traktować tak samo — znosi się w odczycie. Obecny rachunek rozdziela te dwa przypadki.

## 1. Co w punkcie 4 było już wybrane

Warunek D2 z pliku głównego wymaga rzeczywistej korelacji z innym układem. Nie ustala konkretnego instrumentu pomiarowego. Wcześniejszy punkt 4 wybrał dodatkowo:

| Wybór modelu | Co wnosi |
|---|---|
| Moduły S, E, R, B, O i ich połączenia | Nazwany układ wejść, zapisów i porównania |
| Gotowe stany wskaźników R, B, O | Warunki brzegowe aparatu |
| Idealny CNOT | Ostry, powtarzalny zapis jednej obserwabli |
| Analizatory \(W_k\) | Konkretną kalibrację komplementarnych odczytów |
| \(P_0\rho P_0\) | Instrument Lüdersa dla ostrego pytania; nie każdą możliwą realizację zapisu |
| Kolejne kontakty z zegarem historii | Konkretny program procesu, wpisany do jego operatora spójności |

Ostrość jednego pytania nie oznacza pełnego zapisu stanu i nie narusza sama przez się 207. Problem energetyczny powstaje dopiero po porównaniu wybranego zapisu z generatorem tej samej konstrukcji.

**Zakres dodatkowego sprawdzenia:** przyjmujemy sektor, w którym energia rozdzielonych modułów jest addytywna i operacja aparatu ją zachowuje. Nie wywodzimy globalnej addytywnej energii z samego braku zewnętrznego czasu. R1f-2 wyraźnie wymaga tu nazwanych warunków. Gdy energia oddziaływania pozostaje istotna na brzegach procesu, trzeba objąć ją rachunkiem; poniższy argument dla sumy energii części nie stosuje się wtedy automatycznie.

## 2. Dokładne ograniczenie idealnego zapisu

Pozostajemy w czteronośnikowym sektorze singletowym poprzedniego testu. Badana rodzina ma postać \(U_q=P_s^{23}+qP_t^{23}\). Wybieramy generator

\[
H_S=\varepsilon P_t^{23},\qquad
P_t^{23}\big|_L=\frac14
\begin{pmatrix}3&\sqrt3\\\sqrt3&1\end{pmatrix},
\qquad \varepsilon>0.
\]

\(\varepsilon\) jest odstępem energetycznym w tym modelu, nie wyprowadzoną masą cząstki. Wskazanie aparatu dotyczy relacyjnego \(Z_L=-E_{12}\). Mamy

\[
[H_S,Z_L]=-i\frac{\sqrt3}{2}\varepsilon Y_L\ne0.
\tag{1}
\]

Niech cały aparat A obejmuje również jego odniesienia. Dokładny powtarzalny zapis niezmieniający stanów własnych Z miałby działać jako

\[
V\bigl(|0_L\rangle|r\rangle_A\bigr)=|0_L\rangle|r_0\rangle_A,
\qquad
V\bigl(|1_L\rangle|r\rangle_A\bigr)=|1_L\rangle|r_1\rangle_A,
\]

z \(\langle r_0|r_1\rangle=0\). Przy \([V,H_S+H_A]=0\) porównanie jednego elementu macierzowego przed i po operacji daje

\[
\langle0_L|H_S|1_L\rangle
=\langle0_L|H_S|1_L\rangle\langle r_0|r_1\rangle=0.
\]

Tymczasem lewa strona wynosi \(\sqrt3\varepsilon/4\). Założenia są więc sprzeczne. Dowód dotyczy wspólnego przygotowania aparatu dla obu wejść i operatorów o określonych elementach macierzowych; w zastosowanym skończonym modelu nie ma problemu dziedzin.

To konkretny przypadek ograniczenia Wignera–Arakiego–Yanasego [1], a nie nowe prawo wynikające z ramy. Kontrola symboliczna rozwiązała też cały układ dla dwustanowego wskaźnika:

\[
[\mathrm{CNOT},H_S\otimes I+I\otimes H_R]=0,
\quad H_R=a_0I+a_xX+a_yY+a_zZ.
\]

Wszystkie rozwiązania wymagają \(\varepsilon=0\), \(a_y=a_z=0\); nie naprawiają niezerowego generatora (1). **Nie jest to wybór fizycznego \(\varepsilon=0\). To odrzucenie idealizacji aparatu przy przyjętych warunkach.**

Wcześniejszy więz historii \(G_q\Psi_q=0\) tego testu nie zastępował: był zbudowany z zadanych operacji, bez sprawdzenia ich zgodności z tą energią części.

## 3. Aparat z jawnym odniesieniem fazowym

Odniesienie A ma poziomy energii

\[
H_A=\varepsilon N_A,\qquad n=0,1,\ldots,L+1.
\]

Pomocniczy zapis jego przygotowania to

\[
|\chi_{L,\phi}\rangle
=\frac1{\sqrt L}\sum_{n=1}^{L}e^{in\phi}|n\rangle.
\tag{2}
\]

To skończona rodzina stanów konkretnego odniesienia, nie założenie o pojemności świata. Wskaźnik R ma dwa rozróżnialne stany z tą samą energią. Można więc zapisać jego wynik bez wymuszania kolejnej wymiany energii za każdym przepisaniem klasycznego wyniku.

W bazie energetycznej S, oznaczonej \(s=0,1\), operacja działa w sektorach stałej sumy \(s+n\). Dla każdego sektora wewnętrznego stosujemy ten sam blok 4 × 4, obejmujący wskaźnik R. Na dwóch brzegach drabiny operację domykamy unitarnie. Nie zawijamy najwyższej energii na najniższą.

Z konstrukcji:

\[
\widetilde V^\dagger\widetilde V=I,
\qquad [\widetilde V,H_S+H_A+H_R]=0.
\tag{3}
\]

Operacja rozkłada się na trzy relacje par modułów:

\[
\widetilde V=R_{SA}^{\dagger}\,
\mathrm{CNOT}_{S_{\rm energia}\to R}\,R_{SA}.
\tag{4}
\]

Pierwsza i ostatnia mieszają S z A wyłącznie w sektorze tej samej sumy energii. Środkowa zapisuje etykietę energetyczną S w zdegenerowanym wskaźniku. Każda z trzech operacji osobno zachowuje tę samą energię. Ich złożenie realizuje przybliżony odczyt Z. Nie utożsamiamy par modułów z już wyprowadzoną mikroskopową realizacją na wszystkich nośnikach 179.

Pełna macierz i jej rozkład są wyliczone w skrypcie. Przygotowanie (2) nie dotyka brzegowych sektorów podczas danego odczytu, więc dowolność ich unitarnego domknięcia nie niesie otrzymanej liczby. Użyto osobnych odniesień dla przygotowania i kolejnego odczytu; nie założono nieograniczonego ponownego używania niezmienionego odniesienia.

## 4. Co faktycznie zostaje przygotowane i zapisane

Niech \(Z_{\parallel}\) będzie częścią \(Z_L\) diagonalną w bazie energii S, a \(Z_{\perp}=Z_L-Z_{\parallel}\). W bazie relacji:

\[
Z_{\parallel}=\frac{\sqrt3}{4}X_L+\frac14 Z_L.
\]

Nakładanie sąsiednich poziomów odniesienia (2) daje współczynnik

\[
\nu_L=\frac{L-1}{L}.
\]

Przy wybranym wspólnym zerze fazy efekt wyniku R=0 wynosi

\[
E_0^{(L)}=\frac12\bigl(I+Z_{\parallel}+\nu_L Z_{\perp}\bigr).
\tag{5}
\]

Dla wejścia S o \(\rho_S=I/2\) prawdopodobieństwo R=0 nadal wynosi \(1/2\), ale warunkowy opis S względem tak ustawionego odniesienia jest

\[
\rho_{S\mid R=0}=E_0^{(L)}.
\tag{6}
\]

Przy skończonym L nie jest to projektor \(|0_L\rangle\langle0_L|\) z dawnego punktu 4. Przygotowanie i charakter odczytu zmieniły się razem, jako wynik tej samej pełnej operacji.

Dla idealnych wejść \(|0_L\rangle\), \(|1_L\rangle\) prawdopodobieństwo poprawnego zapisania tego konkretnego binarnego pytania wynosi

\[
p_{\rm poprawny}=1-\frac{3}{8L}.
\]

| L | \(\nu_L\) | Poprawny zapis pytania |
|---:|---:|---:|
| 1 | 0 | \(5/8\) |
| 2 | \(1/2\) | \(13/16\) |
| 4 | \(3/4\) | \(29/32\) |
| 8 | \(7/8\) | \(61/64\) |

L=1 nie oznacza braku jakiegokolwiek zapisu. Pozostaje informacja o części komutującej z energią. Znosi się zdolność tego odniesienia do przekazania fazy między różnymi energiami.

Ta dodatkowa nieostrość ma konkretną przyczynę w wybranym aparacie i prawie zachowania. Nie zastępuje częściowości z 207 argumentem o skończonej pojemności. Nawet idealny zapis jednego pytania nie jest całym stanem.

## 5. Odpowiedź jednego pełnego procesu

Odniesienie przygotowania oznaczamy p, odniesienie kolejnego odczytu o. Dla każdego z nich mamy \(L_a\), \(\nu_a=1-1/L_a\) i fazę \(\phi_a\). Między zapisami działa badana relacja \(U_q\), \(q=e^{i\theta}\).

Po obu relacjach zapisu wskaźnik O porównuje niesione R i B. Wskaźniki są zdegenerowane energetycznie, więc ich porównanie XOR zachowuje przyjętą energię. Wynik dla gałęzi R=0:

\[
\boxed{
p(O=0\mid c_{\rm odczytu},R=0)
=\frac58+\frac38\nu_p\nu_o
\cos\bigl(\theta+\phi_p-\phi_o\bigr).
}
\tag{7}
\]

\(c_{\rm odczytu}\) oznacza konfigurację procesu, w której oba zapisy i ich porównanie są już dostępne. Nowe operacje można wstawić do zegara historii wcześniejszego raportu. Ponieważ każda zachowuje tę samą energię K, jego operator spójności spełnia również \([G,I_C\otimes K]=0\). Jest to zgodność wybranych konstrukcji; program kontaktów nadal jest jawnie zadany.

Wzór (7) wyprowadzono z pełnych amplitud obu odniesień. Jego współczynnik interferencji nie został dopisany. Dla \(L_p=L_o=4\), przy tej samej kalibracji odniesień, dostajemy

\[
p=\frac58+\frac{27}{128}\cos\Theta,
\qquad \Theta=\theta+\phi_p-\phi_o.
\]

\(\Theta=\pi/2\) daje \(5/8\); \(\Theta=\pi\) daje \(53/128\). Obie relacje są dopuszczalne dla zbudowanych aparatów zachowujących energię. W granicy \(\nu_p,\nu_o\to1\), przy skalibrowanych odniesieniach, odzyskujemy wynik idealizacji z pierwszego raportu.

## 6. Która swoboda fazy znika po uwzględnieniu czytającego

W (7) odczytywalne jest \(\Theta\), nie oddzielne fazy jego składników. Wspólna zmiana zer faz \(\phi_p\mapsto\phi_p+\alpha\), \(\phi_o\mapsto\phi_o+\alpha\) niczego nie zmienia.

Jest też ważniejszy przypadek dynamiczny. Jeśli między przygotowaniem a odczytem rozpatrujemy tylko swobodny wspólny postęp modułu i dopasowanego odniesienia, oba otrzymują ten sam czynnik w:

\[
q=w,\qquad e^{i\phi_o}=w e^{i\phi_p}.
\]

Wtedy \(q e^{i(\phi_p-\phi_o)}=1\), więc

\[
p=\frac58+\frac38\nu_p\nu_o
\]

nie zależy od tego wspólnego postępu. Zmienianie samego q przy zatrzymanej fazie czytającego opisywałoby wówczas inny proces. Trzeba wskazać, jaka relacja fizyczna wytwarza taką różnicę.

To symetria tego dopasowanego porównania. Jest zgodna z różnymi odczytami warunkowymi i dynamiką relacji w pozostałych częściach procesu, tak jak globalny więz z 258.

Jeżeli oprócz wspólnego postępu występuje dodatkowe oddziaływanie względne, \(q=w e^{i\delta}\), w odpowiedzi pozostaje \(\cos\delta\). To rzeczywista różnica relacji, zgodna z ograniczeniem (3). **Uwzględnienie czytającego usuwa wspólny postęp z listy obserwowalnych swobód; nie ustala wartości dodatkowej fazy względnej.**

Odstęp \(\varepsilon\) jest generatorem fazy w tym modelu: przy konwencji ewolucji \(e^{-iH\tau/\hbar}\) czynnik swobodny wynosi \(w=e^{-i\varepsilon\Delta\tau/\hbar}\). \(\tau\) może tu służyć jako pomocnicza parametryzacja wspólnego przesunięcia; nie jest dodatkowym obserwowalnym czasem. Odczyty (7) wymagają wyłącznie wewnętrznych relacji. Rachunek nie wyprowadza wartości \(\varepsilon\), stosunków mas ani ogólnego działania.

## 7. Usunięcie ukrytego absolutnego odniesienia

Produkt stanów (2) z określonymi \(\phi_p,\phi_o\) był wygodnym zapisem obliczeniowym. Żeby nie pozostawić absolutnej fazy jako fizycznego wejścia, zastosowano rozkład na sektory całkowitej energii:

\[
\mathcal T(\rho)=\sum_E\Pi_E\rho\Pi_E.
\tag{8}
\]

Wszystkie pełne operacje i końcowe efekty zapisów komutują z tą samą energią, dlatego \(\operatorname{tr}(F\mathcal T(\rho))=\operatorname{tr}(F\rho)\). Skrypt sprawdził to bezpośrednio dla dwóch pełnych zapisów.

Rozkład (8) zachowuje fazy względne wewnątrz sektora. Dla pary odniesień, przy \(n+m=K\), amplituda

\[
e^{i(n\phi_p+m\phi_o)}
=e^{iK\phi_o}e^{in(\phi_p-\phi_o)}
\]

niesie tylko różnicę faz, bo pierwszy czynnik jest wspólny dla sektora. Takie korelacje stanowią treść przygotowania aparatu; nie są orientacją wobec zewnętrznego zegara.

**Ważne dla interpretacji przygotowania:** po (8) sam lokalny stan S w gałęzi R=0 jest diagonalny w bazie energii i nie zależy od \(\nu_p\). Mimo to wspólny odczyt nadal daje (7). Faza, która umożliwia dalszy odczyt, jest w relacjach S z odniesieniami. Przenoszenie całej tej treści do samodzielnego „przygotowanego stanu S” byłoby błędem. Równanie (6) opisuje S względem określonego odniesienia, a nie uchwycony stan absolutny.

Można też otrzymać ostry globalny więz. Po puryfikacji mieszaniny sektorów dodatkowym wewnętrznym rejestrem Q o energii \(E_{\max}-E\) stan wspólny spełnia

\[
(K+H_Q-E_{\max}I)|\Omega\rangle=0.
\]

Usunięcie Q przez ślad częściowy odtwarza (8). To konstrukcja zgodna z 258; nie dodaje zewnętrznego obserwatora i nie wymaga ujemnych fizycznych poziomów energii.

## 8. Energia, koherencja i nieoznaczoność

Dla pomocniczej rodziny czystych odniesień (2):

\[
(\Delta H_A)^2=\varepsilon^2\frac{L^2-1}{12},
\qquad \nu_L=1-\frac1L.
\]

Wzrost L w tej konkretnej rodzinie poprawia odczyt niekomutujący z energią. Warunkowy opis (6) względem skalibrowanego odniesienia ma

\[
|\mathbf r|^2=\frac{1+3\nu_L^2}{4},
\qquad \sum_{j=x,y,z}(\Delta\sigma_{j,L})^2
=\frac{11-3\nu_L^2}{4}.
\]

Po usunięciu absolutnego odniesienia wielkości te trzeba odnosić do odpowiednich korelacji warunkowych; nie przypisywać ich bez zmiany lokalnemu S po (8).

**Sama wariancja energii nie ustala zdolności odczytu fazy.** Dodatkowa kontrola usunęła koherencję obu odniesień osobno, zachowując ich rozkłady i wariancje energii. Odpowiedź stała się wtedy \(5/8\), niezależnie od q. To inne działanie niż (8), które usuwa tylko absolutną fazę i zachowuje fazy względne. Wiążąc energię z odczytem, trzeba zachować te relacje, a nie tylko jedną liczbę wariancji.

## 9. Co ten krok zmienia

Punkt 4 pierwszego raportu pozostaje poprawnym modelem idealnego instrumentu. Nie stanowił jeszcze dowodu jego realizowalności przy wskazanym zachowaniu energii. Obecny krok daje dodatkowy warunek, który faktycznie coś wyklucza, oraz aparat, który ten warunek spełnia.

Wniosek „faza pozostaje swobodna” wymaga teraz pełniejszego zapisu: swobodna może pozostać **faza względna konkretnego oddziaływania**, przy wspólnie zdefiniowanych odniesieniach i zapisach. Wspólny postęp fazy oraz absolutne zero fazy nie są odczytywalnymi dodatkowymi parametrami.

Pozostają jawne wybory: sektor addytywnej energii, widmo odniesień, stan ich wzajemnej kalibracji, degeneracja wskaźników, realizacja operacji i program kontaktów. Nie udowodniono, że rama wybiera każdy z tych elementów ani ogólną regułę kwantową. Uzyskano konkretny krok od spójności macierzy do spójności fizycznego odczytu z jego energią i odniesieniem.

## 10. Odtworzenie i źródła

Kontrola: `punkt4-energia-zapis-kontrola-2026-10-12.py`; wynik szczegółowy: plik JSON o tej samej nazwie. **Wynik wykonania: PASS, 107 dokładnych kontroli.** Python 3.10 lub nowszy, `sympy`. Równania faz sprawdzane są symbolicznie na całym okręgu jednostkowym. Pełne skończone macierze sprawdzono dla L=1,2,3,4,8, a dwa zapisy dla par (1,1), (2,3), (4,4). Dowód wzorów ogólnych opiera się na rozkładzie na sektory i obliczonych nakładaniach, nie na ekstrapolacji z prób.

Oczekiwanie, kryterium obalenia i wybory zapisano wcześniej w `zalozenia-punkt4-przed-kontrola.md`.

1. M. Ozawa, [Conservation laws, uncertainty relations, and quantum limits of measurements](https://arxiv.org/abs/quant-ph/0112154), Phys. Rev. Lett. 88, 050402 (2002). Warunki ograniczenia WAY i powiązanie dokładności pomiaru z prawem zachowania. Użyty tutaj elementarny dowód nie wymaga ilościowego ograniczenia szumu z tej pracy.
2. T. Miyadera, H. Imai, [Wigner-Araki-Yanase theorem on Distinguishability](https://arxiv.org/abs/quant-ph/0605213), Phys. Rev. A 74, 024101 (2006). Rozróżnialność zapisów i stanu układu przy prawie zachowania.
3. J. Åberg, [Catalytic Coherence](https://arxiv.org/abs/1304.1060), Phys. Rev. Lett. 113, 150402 (2014). Odniesienie dla użycia koherencji energetycznej jako części aparatu. Nie wykorzystujemy tezy o nieograniczonym katalitycznym użyciu odniesienia; każde odniesienie w naszym procesie bierze udział w jednym instrumencie, a jego korelacje są zachowane.

Macierze skończonego aparatu, ich rozkład (4), obie operacje zapisu i wzór (7) zostały wyprowadzone i sprawdzone w załączonym skrypcie. Znane narzędzia nie są przedstawiane jako nowe prawa fizyki.
