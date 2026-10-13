# Test 128: prąd EM, człon kontaktowy i miara pary

**Data:** 13 października 2026 r.  
**Status:** osobne sprawdzenie kandydatów testu 128. Wyniki rachunkowe i warunki dalszego wyprowadzenia; materiał do oceny przed ewentualnym wpisem do ramy.

## 1. Pytanie i wynik

Celem jest sprawdzenie trzech ruchów potrzebnych do domknięcia odpowiedzi EM rodziny odczytu, a następnie funkcji

\[
F_\gamma(r)=\frac13\int_0^{1/4}\widehat\rho(t)\frac{r\,dt}{1+rt},
\qquad
\widehat\rho(t)=\sqrt{1-4t}(1+2t).
\]

Ten dokument sprawdza kandydatów reguł wykluczających dodatkowe składniki odpowiedzi. Nie ustanawia jeszcze wyprowadzenia całego \(F_\gamma\).

| Sprawdzenie | Wynik | Zakres |
| --- | --- | --- |
| Czy cały człon kontaktowy \(\Xi\) daje wyłącznie \(D(0)\)? | Nie uzasadniono takiego przypisania. | W kanonicznej redukcji L/R powstaje stały lokalny tensor wierzchołka. Jego wkład do pełnego odczytu trzeba jednak liczyć razem z pozostałymi składnikami. |
| Czy dwie wstawki fazy na jednym elemencie dają tylko \(Q^2h_\ell\)? | Tak, dla pojedynczego zorientowanego bloku \(t_\ell=e^{iQa}h_\ell\), gdy \(h_\ell\) nie zależy od fazy. | Pochodna pełnego unitarnego kontaktu ma również \(\Xi\). Sama liczba łańcuchów nie ustala rzędu w sprzężeniu EM. |
| Czy czynnik \(f(m^2)\) w normalizacji miary pary się kasuje? | Tak, dokładnie. | Kasuje się konwencja normalizacji bazy przy zgodnym przeskalowaniu stanów i amplitud. Pozostają fizyczne wagi, stan wejściowy i wybór prądu. |

Podstawą kandydatów są: R1d — faza końca jest nieodczytywalna, faza porównania siedzi na linku; 177 — obieg wymaga dwóch łańcuchów między tymi samymi odczytami; 179 — relacje zachodzą tam, gdzie zachodzi niesienie; 257 — kowariancja transportu wynikająca z nieodczytywalności fazy końca. R1c i 204 dotyczą zmiany czytającego i zliczenia niezależnego od jego wyboru.

Ważne jest rozróżnienie trzech obiektów: **zorientowanego bloku transportu** \(t_\ell\), **pełnego kontaktu unitarnego** \(u_\ell\) i **pełnej odpowiedzi EM** po złożeniu kontaktów, propagacji, stanu i profili odczytu. Równość dotycząca jednego z nich wymaga osobnego przejścia, aby stała się twierdzeniem o następnym.

## 2. Człon kontaktowy i redukcja L/R

### 2.1. Co daje rachunek w klasie kanonicznej

Rozważmy nazwaną klasę operatorów L/R, przy \(m\ne0\):

\[
K=\begin{pmatrix}-m\mathbb1&L\\R&-m\mathbb1\end{pmatrix},
\qquad
S=\frac{LR-m^2\mathbb1}{m}.
\]

Wyznaczniki różnią się czynnikiem niezależnym od źródła, więc ich pochodne logarytmiczne są takie same. Przyjmujemy liniową zależność od źródła:

\[
L_{,\mu}=Q\Sigma_\mu,
\qquad R_{,\mu}=Q\overline\Sigma_\mu,
\qquad L_{,\mu\nu}=R_{,\mu\nu}=0,
\]

przy

\[
\Sigma_0=\overline\Sigma_0=\mathbb1,
\qquad \Sigma_i=\sigma_i,
\qquad \overline\Sigma_i=-\sigma_i.
\]

Tożsamość macierzy Pauliego daje

\[
\Sigma_\mu\overline\Sigma_\nu+
\Sigma_\nu\overline\Sigma_\mu=2g_{\mu\nu}\mathbb1,
\qquad g=\operatorname{diag}(1,-1,-1,-1).
\]

Symbol \(g\) jest tutaj skrótem tej tożsamości algebraicznej. Ten rachunek nie dodaje osobnej areny, na której miałyby zachodzić relacje.

Druga pochodna operatora zredukowanego wynosi

\[
\boxed{
S_{,\mu\nu}=\frac{2Q^2}{m}g_{\mu\nu}\mathbb1.
}
\]

Jest to stały lokalny tensor wierzchołka w tej klasie. Pełna druga pochodna logarytmu wyznacznika ma jednak dwa składniki:

\[
\boxed{
\partial_\mu\partial_\nu\ln\det K
=\operatorname{Tr}\left[
S^{-1}S_{,\mu\nu}
-S^{-1}S_{,\mu}S^{-1}S_{,\nu}
\right].
}
\]

Ich suma odtwarza zapis przed redukcją:

\[
-\operatorname{Tr}\left[
K^{-1}K_{,\mu}K^{-1}K_{,\nu}
\right],
\]

ponieważ \(K_{,\mu\nu}=0\). W kontroli dokładnej sprawdzono wszystkie 16 par indeksów dla trzech skończonych przykładów blokowych: łącznie 48 zgodności pełnego i zredukowanego rachunku.

**Stałość wierzchołka nie oznacza, że można przypisać mu samodzielną stałą w skalarnej odpowiedzi \(D\).** Człon \(\operatorname{Tr}(S^{-1}S_{,\mu\nu})\) sam nie jest ogólnie poprzeczny. Warunek poprzeczności dotyczy kompletnej sumy. Nie można więc najpierw przydzielić temu składnikowi osobnego \(D(z)\), a dopiero potem wykorzystać poprzeczności do ograniczenia jego postaci.

Nie utożsamiamy też automatycznie wierzchołka powstałego z redukcji Schura z \(\Xi\) z pochodnych kontaktu unitarnego. Są to różne reprezentacje pochodnych; porównanie wymaga zachowania pełnego odczytu.

### 2.2. Czego nie wyklucza poprzeczność

Poprzeczność dopuszcza tensor

\[
\Pi_{\mu\nu}(q)=
(q^2g_{\mu\nu}-q_\mu q_\nu)
(C_0+C_1q^2).
\]

Nie wymusza \(C_1=0\). Samo odjęcie wartości przy zerowym transferze również nie usuwa członu liniowego w zmiennej skalarnej. Aby wykluczyć taki człon, potrzebne jest ograniczenie pełnej odpowiedzi — na przykład uzasadniony warunek wzrostu \(D(z)/z\to0\) — albo reguła kontaktów, z której takie ograniczenie wynika.

### 2.3. Dlaczego 179 nie wystarcza w proponowanej postaci

Kandydat brzmiał: człon bez części absorpcyjnej zmienia odczyt, choć nic nie jest niesione, więc narusza 179. Problemem jest utożsamienie **niesienia** z **otwartym kanałem produkcji pary**.

Prosty diagnostyczny przykład zamkniętego kanału daje po eliminacji

\[
\Sigma(\zeta)=\frac{g^2}{\zeta-M}.
\]

Poniżej jego bieguna odpowiedź jest rzeczywista. Po odjęciu wartości odniesienia pozostaje jednak

\[
\Sigma'(0)=-\frac{g^2}{M^2}\ne0.
\]

To podważa wniosek „brak absorpcji w danym zakresie oznacza brak niesienia”. Nie jest to przykład globalnego wielomianu bez części absorpcyjnej przy wszystkich skalach ani kontrmodel całej ramy.

Drugie rozróżnienie dotyczy zmiennych odczytu. Kontakt lokalny w fazach linków może zyskać zależność od argumentu po przyporządkowaniu faz do profilu źródła. Dla przykładowego profilu

\[
w(\omega)=\int_0^1e^{i\omega u}\,du
\]

mamy

\[
|w(\omega)|^2=
\frac{2(1-\cos\omega)}{\omega^2}
=1-\frac{\omega^2}{12}+\frac{\omega^4}{360}+\cdots.
\]

To kontrola samego przejścia od faz do argumentu odczytu. Nie dowodzi istnienia dodatkowego poprzecznego wielomianu w fizycznym \(F_\gamma\).

**Wynik pierwszego sprawdzenia:** stały wierzchołek w redukcji kanonicznej jest wyznaczony. Przypisanie całego \(\Xi\) wyłącznie do \(D(0)\) oraz wykluczenie \(c\,r\) nadal wymagają reguły dotyczącej kompletnej odpowiedzi EM.

## 3. Dwie wstawki na jednym linku i status prądu

### 3.1. Pojedynczy zorientowany blok

Dla

\[
t_\ell(a)=e^{iQa}h_\ell,
\qquad \partial_a h_\ell=0,
\]

rachunek jest dokładny:

\[
\partial_a t_\ell=iQt_\ell,
\qquad
\boxed{\partial_a^2t_\ell=-Q^2t_\ell.}
\]

Jeżeli dwa znaczniki źródła składają się na tę samą fazę, \(a=a_1+a_2\), pochodna mieszana jest również \(-Q^2t_\ell\). Po wyłączeniu czynników \(i\) i fazy pozostaje \(Q^2h_\ell\); nie powstaje nowy niezależny tensor anomalnego prądu w samym tym bloku.

Przeciwnie zorientowany blok ma fazę sprzężoną. Lokalna masa L/R przy wspólnym ładunku \(Q=q\mathbb1\) jest niezmiennicza pod wspólną fazą. Warunek \([Q,h_m]=0\) ustala tę niezmienniczość; sam nie ustala całego prądu EM ani wszystkich odczytów obiegów.

### 3.2. Pełny kontakt unitarny

Dla pełnego kontaktu definiujemy

\[
X=-iu^\dagger u',\qquad \Xi=X'.
\]

Z unitarności wynika

\[
\boxed{u^\dagger u''=-X^2+i\Xi.}
\]

Jeśli cały operator ma jedynie globalny czynnik fazowy,

\[
u(a)=e^{iQa}u_0,
\qquad u_0^\dagger u_0=\mathbb1,
\]

to \(X=Q\mathbb1\) oraz \(\Xi=0\). Sam taki czynnik nie odtwarza całego prądu produkcji pary.

Inaczej zachowuje się pełna ewolucja hermitowskiego transportu między końcami linku:

\[
h(a)=\theta
\begin{pmatrix}0&e^{iQa}\\e^{-iQa}&0\end{pmatrix},
\qquad u(a)=e^{-ih(a)}.
\]

Indeksy tej macierzy opisują **końce linku**, a nie chiralności L/R. Przy \(a=0\), z macierzami Pauliego \(\tau_i\) działającymi na tych indeksach,

\[
X=Q\bigl(\cos\theta\sin\theta\,\tau_y
-\sin^2\theta\,\tau_z\bigr),
\]

\[
\boxed{\Xi=Q^2\sin\theta\cos\theta\,\tau_x.}
\]

Dla dopuszczalnej macierzy zajęcia \(N=(\mathbb1+v\tau_x)/2\), \(|v|\le1\),

\[
\operatorname{Tr}(N\Xi)=vQ^2\sin\theta\cos\theta.
\]

Może więc istnieć niezerowy składnik natychmiastowy pełnego kontaktu, mimo że pochodne jego pojedynczego zorientowanego bloku są proporcjonalne do tego bloku. Dodanie komutującego lokalnego sprzężenia masowego L/R na osobnym indeksie nie zmienia tej tożsamości.

Ten przykład ustala rozróżnienie operatorów. Nie dowodzi wystąpienia nowego \(F_2\) ani dowolnego członu \(c\,r\) w kompletnej odpowiedzi EM.

W redukcji kanonicznej symetryczna suma dwóch wstawek abelowych daje tensor \(g_{\mu\nu}\mathbb1\). Część spinowa uporządkowanych iloczynów znosi się przy tym symetryzowaniu. Nie oznacza to braku magnetyzmu: \(g=2\) mieści się już w minimalnym prądzie \(F_1\).

### 3.3. Dwa łańcuchy nie ustalają jeszcze rzędu EM

177 dopuszcza odczyt interferencji dwóch niesionych ramion. Na przykład

\[
p=\frac{1+\cos(Q(a_1-a_2))}{2}
\]

ma

\[
\left.\partial_{a_1}^2p\right|_{a_1=a_2=0}
=-\frac{Q^2}{2}.
\]

Obieg uczestniczy więc już w odpowiedzi kwadratowej. Również

\[
\left.\partial_{a_1}
\left[\lambda\left(e^{iQ(a_1-a_2)}-1\right)\right]
\right|_{a_1=a_2=0}=iQ\lambda.
\]

Sama obecność drugiego łańcucha nie wymusza dodatkowego czynnika \(Q^2\) lub \(\alpha\). Te przykłady nie konstruują anomalnego prądu elektronu. Pokazują, że przejście od liczby łańcuchów do rzędu perturbacyjnego wymaga rachunku rzeczywistych wstawek i wewnętrznych propagacji EM.

**Wynik drugiego sprawdzenia:** tożsamość dwóch pochodnych fazy przechodzi dla pojedynczego zorientowanego bloku. W nazwanej klasie minimalnego prądu otrzymujemy \(F_1=1\), \(F_2=0\). Aby ten wynik wynikał z samej ramy, trzeba jeszcze wyprowadzić identyfikację transportu neutralnego z tym prądem oraz wykluczenie zależności od obiegu w danym rzędzie. Reguła 179 wymaga niesienia w drugim łańcuchu; nie daje sama jego kosztu w potęgach sprzężenia.

## 4. Kasowanie normalizacji miary pary

Niech \(f_m=f(m^2)>0\) zmienia konwencję normalizacji na jednej orbicie:

\[
d\mu'_m=f_m\,d\mu_m,
\qquad
|p,\sigma\rangle'=f_m^{-1/2}|p,\sigma\rangle.
\]

Zupełność pozostaje niezmieniona:

\[
\sum_\sigma\int d\mu'_m
|p,\sigma\rangle'\langle p,\sigma|'
=
\sum_\sigma\int d\mu_m
|p,\sigma\rangle\langle p,\sigma|
=\mathbb1.
\]

Dla dwóch nośników, przy ustalonym źródle lub stanie wejściowym,

\[
\mathcal M'=(f_1f_2)^{-1/2}\mathcal M,
\qquad
|\mathcal M'|^2=\frac{|\mathcal M|^2}{f_1f_2}.
\]

Jednocześnie

\[
d\mu'_1\,d\mu'_2=f_1f_2\,d\mu_1\,d\mu_2.
\]

Stąd

\[
\boxed{
d\mu'_1\,d\mu'_2\,|\mathcal M'|^2
=d\mu_1\,d\mu_2\,|\mathcal M|^2.
}
\]

Dla jednakowych mas czynnik \(f_m^2\) w miarze kasuje się z \(f_m^{-2}\) w kwadracie amplitudy. To dokładna równość, niezależna od wyboru \(f_m\).

**Co zostało usunięte:** dowolność normalizacji bazy i miary, gdy są zmieniane zgodnie z zupełnością.

**Co pozostaje:** fizyczna liczba gatunków, ich zajęcia, stan wejściowy, formfaktory prądu oraz sposób przygotowania odczytu. Pomnożenie samej miary bez przeskalowania stanów i amplitud byłoby zmianą fizycznego zliczenia.

Inkluzywność końcowego odczytu oznacza sumowanie po nieodczytywanych stanach końcowych. Nie wybiera stanu początkowego. W zapisie rodziny z wcześniejszego rachunku pozostaje

\[
N=R(\mathbb1+R)^{-1},
\]

wraz z wagami odpowiedzi zależnymi od zajęć, w szczególności różnicami \(\lambda_a-\lambda_b\). Sama inkluzywność nie ustanawia próżni ani stacjonarności.

**Wynik trzeciego sprawdzenia:** kasowanie \(f(m^2)\) jest domknięte jako rachunek konwencji normalizacji. Nie stanowi samodzielnego wyprowadzenia miary orbit ani wag fizycznej rodziny.

## 5. Miejsce następnego testu 128

Stan przed wykonaniem K1–K2. Sprawdzenie wskazanych przejść zapisano w §§7–9.

Pozostają dwa konkretne przejścia:

1. **Prąd w ustalonym rzędzie.** Wypisać składanie kontaktów i sposób liczenia wewnętrznych relacji EM. Wykazać, którą regułę narusza wstawka zależna od obiegu, gdy próbuje wejść do elementarnego prądu w tym samym rzędzie. Potrzebny jest związek między liczeniem kontaktów a potęgą sprzężenia; sama obecność dwóch łańcuchów nie wystarcza.
2. **Część kontaktowa pełnej odpowiedzi.** Zachować \(\Xi\), człony propagacyjne i profile aż do uzyskania kompletnego odczytu EM. Dopiero dla niego sprawdzić liczbę odejmowań oraz warunek wykluczający \(c\,r\). Jeżeli warunek wzrostu albo ograniczenie kontaktów wymaga osobnego wejścia, trzeba je tak nazwać.

Kasowanie normalizacji nie wymaga ponownego rachunku. Dalsze domknięcie \(F_\gamma\) zależy od tego, czy powyższe przejścia oraz właściwe wagi progowe pary wynikają z reguł ramy, czy pozostają nazwanym przyporządkowaniem fizycznym.

## 6. Źródła i zakres kontroli

Odwołania do ramy dotyczą R1c, R1d oraz wpisów 177, 179, 204, 257 w plikach `logika-relacyjna-v3.5.md` i `poprawki.md`. Oznaczenia pełnego kontaktu, redukcji i rodziny odczytu nawiązują do §§13, 15–16, 19–20 pliku `przyporzadkowanie-realizacji-dynamicznej-2026-10-12.md`; potrzebne definicje i równania podano tutaj jawnie.

Kontrola przekładu rachunku drugiego rzędu: A. G. Morgan, *Second Order Fermions in Gauge Theories*, [hep-ph/9502230](https://arxiv.org/abs/hep-ph/9502230), zwłaszcza konstrukcja operatora drugiego rzędu i wierzchołków z dwiema wstawkami. Źródło służy do sprawdzenia równoważności rachunków; nie ustanawia wyboru prądu przez ramę.

Kod w dodatku sprawdza tożsamości zorientowanego linku, pełnego kontaktu, redukcji L/R, poprzeczności przykładowego tensora, rozwinięcia profilu, pochodnej zamkniętego kanału i rzędu odpowiedzi interferencyjnej. Zapisany wynik: **PASS**, 851 dokładnych kontroli skalarnych, w tym sprawdzenia elementów macierzy; 48 zgodności pełnego i zredukowanego Hessianu. To licznik operacji kontrolnych, nie 851 niezależnych testów fizycznych.

Kasowanie normalizacji w §4 jest dowodem algebraicznym podanym jawnie; nie jest częścią licznika skryptu. Skończone przykłady nie dowodzą wyboru pełnej rodziny przez ramę ani znikania wielomianu w rzeczywistej skalarnej odpowiedzi EM.

## 7. K1 — czy minimalność kontaktu wynika z 179, 268 i 257?

**Stan przyjęty przed sprawdzeniem:** ogon miary \(\nu_\gamma([t,1/4])=\widehat\rho(t)/3\), wagi \(1,1,(m/E)^2\) w klasie punktowego prądu, kontrola \(\beta^3/4\) oraz kasowanie \(f(m^2)\) są ustalone. Odrzucone pozostają wnioski: „cały Ξ tylko do D(0)”, „179 wyklucza c·r przez brak absorpcji”, „drugi łańcuch zawsze oznacza rząd wyżej”.

Badane zaprzeczenie dotyczy pełnego kontaktu lub kontaktu efektywnego, nie samego elementu \(t_\ell(a_\ell)=e^{iQa_\ell}t_\ell(0)\) z §13.1. Ten element zależy tylko od \(a_\ell\) z konstrukcji. Pytanie brzmi, czy dopuszczalne złożenie może doprowadzić do \(\partial_{a_{\ell'}}T_\ell\ne0\), gdy drugi link należy do obiegu przez ℓ.

### 7.1. Co dokładnie wyklucza 268

Treść mostu wskazanego jako 268 odczytano w `regula-kompozycji-pelnego-odczytu-2026-10-12.md`, §2.4. Operacja na A,B ma jedyne zgodne liniowe rozszerzenie na nieuczestniczącego C:

\[
\operatorname{Ad}(U_{AB}\otimes\mathbb1_C).
\]

Jeżeli **ta sama izolowana operacja A,B**, przy tych samych pełnych danych wejściowych, miałaby bez dodatkowego niesienia zależeć od fazy C, naruszałaby tę regułę. To rzeczywiste wykluczenie testu 128.

Nie obejmuje ono jednak innego procesu:

\[
U_{AB}\,U_{BC},
\]

w którym najpierw B spotyka C, a potem niesie wynik do kontaktu A,B. Każde spotkanie zachowuje wymagane rozszerzenie na resztę. Zależność od wcześniejszej fazy może wejść przez stan uczestniczącego B albo przez redukcję modułu. Nazywanie zredukowanego modułu „jednym kontaktem” nie usuwa jego wcześniejszych relacji.

179 pkt 7 mówi, że zdarzenie wielu nośników jest modułem z par. Nie ogranicza zestawu dopuszczalnych operatorów każdej pary do minimalnego wierzchołka EM. Raport o kompozycji mówi wprost w §2.3: „Wybór konkretnego U_AB pozostaje treścią procesu”.

### 7.2. Rozstrzygnięcie gałęzi link–link

**W strukturze nośników z 179 i 268 spotkanie dwóch linków jest dopuszczalne.** Możliwe jest przeniesienie odczytywalnej fazy względnej stanu między nośnikami. Dokładny przykład stanowi

\[
U_{AB}=e^{i\pi/4}\,\mathrm{SWAP}\in SU(4),
\]

który realizuje

\[
\frac{|0\rangle+e^{i\phi}|1\rangle}{\sqrt2}
\otimes|0\rangle
\ \longmapsto\
e^{i\pi/4}|0\rangle\otimes
\frac{|0\rangle+e^{i\phi}|1\rangle}{\sqrt2}.
\]

To transfer stanu, a nie klonowanie. Operator komutuje również ze wspólnym obrotem \(R_\chi\otimes R_\chi\), gdzie \(R_\chi=\operatorname{diag}(1,e^{i\chi})\), i ma poprawne rozszerzenie na nieuczestniczącego C.

**Granica przykładu:** faza względna współczynników stanu nie jest automatycznie fazą koneksji EM. Aby ten kontakt przenosił holonomię konkretnego obiegu EM, trzeba wskazać, jak ta holonomia została niesiona i zakodowana w jego wejściach. Sprawdzenie nie ustanawia dowolnego kopiowania faz linków ani gotowego anomalnego prądu elektronu.

257 ogranicza postać takiej zależności: po wyłączeniu \(e^{iQa_\ell}\) musi ona być niezmiennicza względem faz końców. Dla obiegu \(\Phi_c=c^Ta\), z \(c^TD_0=0\), dowolna funkcja \(h_\ell(\Phi_c)\) spełnia ten warunek niezmienniczości. 257 nie wymusza jej stałości. 268 wymaga, aby zależność miała rzeczywistą drogę niesienia, a nie dodatkową wagę od nieuczestniczącego nośnika. Sam most nie zakazuje takiej drogi.

Nie można więc z wymienionych zdań wyprowadzić zakazu gałęzi (b). Nie można też na podstawie samej liczby linków orzec, że gałąź (a) jest rzędem wyżej: związek liczby wstawek z potęgą sprzężenia wymaga ustalenia wewnętrznych linii EM, ich końców i normalizacji propagacji.

**Liniowość ma trzy różne znaczenia:** liniowość map kwantowych z 268; abelowość relacji faz U(1); liniowość swobodnych równań EM. Pierwsze dwa nie ustanawiają trzeciego. Co więcej, sam wierzchołek Pauliego jest liniowy w sile pola, więc sama liniowość odpowiedzi na słabe źródło również go nie usuwa. Jeżeli używamy swobodnego kwadratowego sektora EM albo zakazu spinowego odczytu holonomii w elementarnym kontakcie, są to nazwane warunki klasy, dopóki nie wyprowadzimy ich z dalszej reguły ramy.

Kontrola literaturowa tego rozróżnienia: Niau Akmansoy–Medeiros, Phys. Rev. D 99, 115005 (2019), wstęp i §II, rozdzielają symetrię U(1) od liniowości równań oraz opisują zachowujące cechowanie nieliniowe sprzężenia fotonów. Nie przenosimy ich teorii do ramy; sprawdzamy zakres argumentu „U(1) oznacza brak oddziaływania link–link”.

### 7.3. Czy λ z §3.3 jest elementem Grama?

W §3.3 symbol \(\lambda\) pojawił się przy **zmianie amplitudy** \(\lambda(e^{iQ\Phi}-1)\), bez wskazania pełnej rodziny. Nie jest przez to automatycznie elementem Grama. Takie rozróżnienie można policzyć na jednym ustalonym module.

Niech

\[
B_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta\end{pmatrix},
\quad
U(\Phi)=B_\theta
\begin{pmatrix}e^{iQ\Phi}&0\\0&1\end{pmatrix}B_\theta^\dagger.
\]

Dla ustalonych przygotowania i efektu \(\rho=F=|0\rangle\langle0|\):

\[
\langle0|U(\Phi)|0\rangle
=1+\underbrace{\cos^2\theta}_{\lambda_{\rm amp}}
(e^{iQ\Phi}-1).
\]

Dwie amplitudy dróg mają moduły \(\cos^2\theta\) i \(\sin^2\theta\). Ich rzeczywisty Gram wynosi

\[
\Gamma=\begin{pmatrix}
\cos^4\theta&\cos^2\theta\sin^2\theta\\
\cos^2\theta\sin^2\theta&\sin^4\theta
\end{pmatrix}\succeq0,
\qquad \det\Gamma=0.
\]

Zatem

\[
\boxed{\Gamma_{12}=\lambda_{\rm amp}(1-\lambda_{\rm amp}).}
\]

Przy \(\theta=\pi/4\), \(\lambda_{\rm amp}=1/2\), natomiast \(\Gamma_{12}=1/4\). Po włączeniu fazy drogi do jej reprezentanta pełny element poza przekątną dostaje odpowiedni czynnik \(e^{\pm iQ\Phi}\); jego moduł pozostaje ustalony przez ten sam proces.

Prawdopodobieństwo jest

\[
p=\Gamma_{11}+\Gamma_{22}
+2\Gamma_{12}\cos(Q\Phi),
\qquad p''(0)=-2Q^2\Gamma_{12}.
\]

**Korekta statusu wcześniejszego argumentu:** nie ma wolnego λ, które można zmieniać przy zachowaniu tego samego pełnego procesu i jego Grama. θ, stan, efekt i niesione zapisy ustalają wagę. Jednocześnie 268 nie wymusza \(\Gamma_{12}=0\) i nie przypisuje temu istniejącemu porównaniu dodatkowej potęgi sprzężenia.

Ten przykład sprawdza λ i liczenie wstawek. Nie jest dowodem, że tak skonstruowany moduł stanowi wierzchołek Pauliego w fizycznym kanale elektronu.

### 7.4. Werdykt K1

**Zdanie „F₁=1, F₂=0 w badanym rzędzie wynikają z 179 pkt 7 + 268 + 257 bez dodatkowego wejścia” nie zostało uzasadnione przez te reguły.** Mają one mocniejszy wynik o zgodności zadanej operacji i jej kompozycji, lecz nie wybierają konkretnej operacji EM.

Wykluczone jest oddziaływanie fazy nieuczestniczącego nośnika bez drogi niesienia. Dopuszczony jest moduł z rzeczywistych spotkań par. Pozostaje wskazać regułę wybierającą minimalny spinowy prąd i określającą rząd, w którym mogą pojawić się inne odczyty holonomii. Przyjęcie „EM w tym rzędzie działa wyłącznie przez centralny generator Q na transporcie kinetyki” zamyka klasę warunkowo; jest właśnie regułą wyboru wymagającą uzasadnienia, a nie wnioskiem z samego zakazu zewnętrznej wagi.

## 8. K2 — pełna odpowiedź: W, VV, więzy fazowe i argument rodziny

### 8.1. Pełny podział drugiej wariacji

Dla jądra gaussowskiego \(K[a]\), przy stałych końcach i \(G=K^{-1}\), używamy algebraicznej tożsamości z §§13 i 16:

\[
\Gamma_{,\ell k}^{(2)}
=\operatorname{Tr}(G V_\ell G V_k-GW_{\ell k}),
\quad V_\ell=K_{,\ell},\quad W_{\ell k}=K_{,\ell k}.
\]

Nie potrzeba obrotu Wicka do różniczkowania tego wyznacznika. Jego późniejsze utożsamienie z właściwym jądrem EM wymaga odczytu z §13.3.

**Dwie pierwsze wstawki V mogą mieć tę samą etykietę ℓ.** Dlatego podział na „W z drugiej pochodnej kontaktu” oraz „VV wyłącznie z różnych kontaktów” nie jest kompletny. Pełna część VV zawiera również

\[
\operatorname{Tr}(GV_\ell GV_\ell).
\]

Można połączyć ten składnik z W w jeden blok tej samej etykiety. Trzeba wtedy odróżnić tak zdefiniowany blok od samego \(W_\ell^{\mu\nu}=\partial_\mu\partial_\nu T_\ell\).

Dokładna kontrola używa dwóch równoległych linków, z fazami \(a_1,a_2\):

\[
K=\begin{pmatrix}
3&e^{iQa_1}+e^{iQa_2}\\
e^{-iQa_1}+e^{-iQa_2}&3
\end{pmatrix},\qquad \Gamma=-\ln\det K.
\]

W punkcie \(a_1=a_2=0\):

\[
\mathsf W_{\rm vertex}=-\frac{4Q^2}{5}\mathbb1,
\quad
\mathsf V_{\rm all}=\frac{2Q^2}{5}
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]

\[
\Gamma^{(2)}=-\frac{2Q^2}{5}
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]

Pełna suma zeruje czystą zmianę odniesienia \((1,1)^T\). Pominięcie diagonalnego VV daje zamiast zera \(-2Q^2(1,1)^T/5\). To kontrola tożsamości i zakresu podziału; tego skończonego Hessianu nie nazywamy α.

W odpowiedzi **przyczynowej** z §19 zachodzi dodatkowe skrócenie między gałęziami. Przy niezależnych znacznikach kontaktów otrzymujemy pełny podział

\[
\mathcal R_{\ell k}
=\underbrace{\delta_{\ell k}
\left[\Phi_{\ell\ell}+\operatorname{tr}(N\Xi_\ell)\right]}_{\mathsf W_{\rm ret}}
+\underbrace{\mathbf1_{k<\ell}\,
 i\operatorname{tr}(N[X_\ell,X_k])}_{\mathsf V_{\rm ret}}.
\]

Dopiero w tej kombinacji wyrazy \(-X_\ell^2\) i odpowiadające im korelacje się znoszą. To wynik całego odczytu, a nie pominięcie VV diagonalnego na początku rachunku.

### 8.2. (i) Diagonalność W i profile

W pierwotnym opisie z niezależnymi lokalnymi fazami i stałymi danymi brzegowymi

\[
\partial_{a_\ell}\partial_{a_k}T_j=0
\quad\text{dla}\quad \ell\ne k.
\]

W takim opisie część pochodząca z drugiej wariacji pojedynczego kontaktu jest diagonalna w **etykietach faz kontaktów**. Po eliminacji modułu, przy zależności od obiegu rozważanej w K1 albo przy źródłozależnych końcach diagonalność nie jest automatyczna.

Niech przy ustalonym n przyporządkowanie źródła do faz będzie liniowe: \(a=B_n(z)A\). Wtedy

\[
\mathsf W_n^{\rm profile}(z)
=B_n(z)^\dagger\operatorname{diag}(w_{\ell,n})B_n(z).
\]

Jeśli z zmienia **tylko profil w tej samej ustalonej rodzinie kontaktów**, zależność W od z pochodzi wyłącznie z B. Gdy z lub n zmienia również neutralne kontakty, przygotowanie albo odczyt, mogą zmieniać się także \(w_{\ell,n}\). §19 nakazuje używać rzeczywistych \(u_n,R_n,S_n\); nie ustanawia ich stałości przez wszystkie n.

### 8.3. (ii) Ile ustala warunek czystej zmiany odniesienia

Dla pełnego zachowanego brzegu z §18 niezmienniczość daje

\[
(\mathsf W+\mathsf V)D_0=0,
\qquad D_0^T(\mathsf W+\mathsf V)=0.
\]

Dotyczy to pełnego jądra w danym odczycie. Przy zmianie odniesień na brzegu trzeba dołączyć pochodne przygotowania i efektu.

**Dokładny wynik dodatni.** Załóżmy, że każdy link ma jeden niezależny skalar fazy, \(\mathsf W=\operatorname{diag}(w_\ell)\), a każdy badany wiersz \((D_0)_{\ell\cdot}\) jest niezerowy. Jeżeli cała macierz \(\mathsf V\) jest znana, to

\[
w_\ell(D_0)_{\ell v}
=-(\mathsf VD_0)_{\ell v}
\]

jednoznacznie ustala \(w_\ell\), o ile równania są zgodne. Dowód: dwa rozwiązania różnią się diagonalną \(\Delta\mathsf W\); z \(\Delta\mathsf WD_0=0\) i niezerowego wiersza D₀ wynika \(\Delta w_\ell=0\).

Jeżeli dany kontakt nie uczestniczy w żadnej dostępnej wewnętrznej zmianie odniesienia, jego wiersz D₀ jest zerowy i ten argument go nie ustala. Dla wieloskładnikowych bloków kontaktowych mogą również pozostać składowe niewidoczne na obraz D₀.

**To nie jest twierdzenie, że VV przy zerowym argumencie ustala W przy wszystkich argumentach.** Równanie korzysta z pełnego \(\mathsf V\) dla tego samego odczytu. Zastąpienie go warunkiem \(\mathsf W=-\mathsf V(0)\) wymaga dodatkowo identyfikacji zerowego profilu z czystą zmianą odniesienia i niezmienności W przy zmianie argumentu. Stały profil na linkach nie jest zawsze czystą zmianą odniesienia — może mieć niezerową holonomię. W standardowym zapisie pędowym samo podstawienie q=0 do warunku poprzeczności daje 0=0; potrzebna jest kontrola granicy i struktury źródła.

### 8.4. Co zostaje po Pₙ

Dopiero dla kompletnej odpowiedzi w nazwanym kanale §13.3 odczytujemy

\[
D_n(z)=\frac{
 u_n(z)^\dagger[\mathsf W_n+\mathsf V_n](z)u_n(z)
}{u_n(z)^\dagger K_n^{(0)}(z)u_n(z)}.
\]

Diagonalność w etykietach kontaktów nie oznacza stałości tego ilorazu. Zależą od niego profil, struktura jednostkowa EM i rzeczywista rodzina n. Wspólny mnożnik profilu może się skrócić, jeżeli rzeczywiście jest wspólny dla licznika i mianownika; sama diagonalność nie ustanawia tego warunku.

Nawet gdy dodatkowe założenia pozwalają zapisać cały licznik jako \(v(z)-v(0)\), pozostaje dzielenie przez rzeczywistą strukturę EM. Nie nadajemy W osobnej fizycznej funkcji D przed poprzecznością.

Warunek fazowy dopuszcza na poziomie pełnego poprzecznego jądra zmianę

\[
\Delta\Gamma_n^{(2)}(z)=c\,r(z)K_n^{(0)}(z),
\qquad \mathcal P_n[\Delta\Gamma_n^{(2)}]=c\,r(z).
\]

To wskazuje składnik niewidoczny dla samych więzów fazowych i dla wartości przy r=0. Nie jest pozwoleniem na jego dopisanie do już ustalonego procesu: 268 nadal wiąże całą odpowiedź jego danymi. Aby taki składnik wykluczyć ze wszystkich dopuszczalnych realizacji, trzeba ograniczenia tej klasy, którego same więzy nie dostarczają.

### 8.5. (iii) Czy Gaussian ustanawia rezolwentę w argumencie rodziny?

§19 wyznacza dla każdego rzeczywistego n macierze X i wagi \(\lambda_a-\lambda_b\). Gaussowskość nie ustanawia jednorodności kontaktów, stacjonarności stanu ani jednej funkcji argumentu z łączącej różne n.

**Rezolwenta jest wyprowadzalna po zadaniu powtarzalnej klasy.** Niech każdy krok ma to samo u₀, \([N,u_0]=0\), a lokalny prąd x jest stały. W bazie

\[
u_0|a\rangle=e^{-i\epsilon_a}|a\rangle,
\qquad N|a\rangle=\lambda_a|a\rangle,
\]

odpowiedź dla różnicy kroków \(m\ge1\) ma postać

\[
R_m=i\sum_{a,b}(\lambda_a-\lambda_b)
|x_{ab}|^2e^{i(\epsilon_a-\epsilon_b)m}.
\]

Jej funkcja generująca, dla \(|\zeta|<1\), wynosi

\[
\boxed{
V(\zeta)=i\sum_{a,b}(\lambda_a-\lambda_b)|x_{ab}|^2
\frac{\zeta e^{i(\epsilon_a-\epsilon_b)}}
{1-\zeta e^{i(\epsilon_a-\epsilon_b)}}.
}
\]

To suma członów rezolwentowych operatora niesienia przez jeden krok. ε są fazami tego operatora, a nie dołożonymi energiami. ζ jest znacznikiem liczby kroków tej jednej sekwencji, nie automatycznie transferem s ani etykietą rodziny n.

Kontrola dwumodowa dla \(u_0=\operatorname{diag}(1,e^{-i\pi/3})\), \(x=\sigma_x\), \(N=\operatorname{diag}(\lambda_0,\lambda_1)\) daje

\[
V(\zeta)=\frac{\sqrt3(\lambda_0-\lambda_1)\zeta}
{1-\zeta+\zeta^2}.
\]

Sprawdzono sześć pierwszych współczynników z bezpośrednich komutatorów. Gaussowska, lecz niejednorodna sekwencja z kolejnymi skumulowanymi fazami \(0,\pi/3,\pi/2\) daje dwie odpowiedzi dla sąsiednich kontaktów: \(\sqrt3\) i 1 przy tej samej macierzy zajęć. Nie są funkcją samej różnicy etykiet. Gaussian sam nie daje więc powyższej jednowymiarowej rezolwenty.

Przyporządkowanie \(\zeta\leftrightarrow s\), właściwe profile i projekcja mogą zmienić zachowanie przy dużym s. Samo istnienie rezolwenty w ζ nie daje jeszcze oszacowania pełnej znormalizowanej odpowiedzi przy \(|s|\to\infty\).

### 8.6. K1 a liczba odejmowań

Z ustalonej mapy prądu z §20, dla \(F_1=1\), \(F_2=\kappa\):

\[
\widehat\rho_\kappa(t)=\beta
\left[(1+\kappa)^2+2t\left(1+\frac{\kappa}{4t}\right)^2\right],
\qquad \beta=\sqrt{1-4t}.
\]

Jeżeli κ utrzymujemy jako stałą aż do t=0, to

\[
\lim_{t\to0}t\widehat\rho_\kappa(t)=\frac{\kappa^2}{8},
\]

czyli przy dużym s waga rośnie jak s. Jednokrotnie odjęty składnik

\[
\frac13\int_0^{1/4}
\widehat\rho_\kappa(t)\frac{r\,dt}{1+rt}
\]

jest wtedy rozbieżny na krawędzi t=0. Po drugim odjęciu jądro całki zawiera \(t\widehat\rho_\kappa(t)\) i jest tam skończone, lecz współczynnik liniowy staje się daną odejmowania. To diagnostyka stałego κ przy wszystkich skalach; nie założenie, że rzeczywisty anomalny formfaktor QED pozostaje stały do nieskończonego s.

Dla **obu** warunków punktowego prądu \(F_1=1\), \(F_2=0\), \(\widehat\rho\to1\) i jednopodstawiona całka jest zbieżna. Samo \(F_2=0\) nie wystarcza, jeżeli \(F_1(s)\) może rosnąć.

**Zbieżność całki nie dowodzi jednoznaczności rekonstrukcji.** Funkcje

\[
D_c(r)=F_\gamma(r)+c\,r
\]

mają tę samą część absorpcyjną kanału pary i tę samą wartość odniesienia w r=0. Człon liniowy jest analityczną częścią kontaktową; nie zmienia wskazanego prądu produkcji pary. Przy interpretacji r jako kwadratu transferu odpowiada pochodnym kontaktowym odpowiedzi i nie jest wykluczany przez samo jej przyczynowe wsparcie.

Aby ustalić c=0 przez jednokrotne odejmowanie, trzeba uzasadnić dla **pełnej** odpowiedzi właściwą klasę analityczną i warunek na dużym konturze, przykładowo

\[
\boxed{\frac{D(s)-D(0)}s\longrightarrow0.}
\]

Wtedy granica usuwa człon liniowy; w klasie odpowiednio ograniczonej usuwa też wyższy wielomian. Bez ograniczenia wzrostu zakres niejednoznaczności nie musi kończyć się na c·r. Ustalona część dyspersyjna celu rośnie tylko jak \(\tfrac13\ln r\), ale jest to oszacowanie tej całki, nie niezależny dowód oszacowania całego D.

**Werdykt K2:** zdanie „przy F₂=0 pełna odpowiedź nie ma c·r bez dodatkowego wejścia” nie wynika ze sprawdzonych warunków. Po dołączeniu F₁=1 ustalono zbieżność części dyspersyjnej. Pozostaje ograniczenie wzrostu kompletnego odczytu. Przyporządkowanie argumentu krokowego do s jest odrębnym mostem: może przenieść już udowodnione oszacowanie, ale samo przemianowanie argumentu go nie ustanawia.

## 9. Bilans K1–K2 i zakres nowej kontroli

| Część | Status po sprawdzeniu |
| --- | --- |
| Zewnętrzna faza wpływa na izolowane U_AB bez udziału jej nośnika | Wykluczone przez rozszerzenie z 268. |
| Rzeczywiste spotkanie dwóch linków przenosi fazę względną stanu | Dopuszczone w strukturze par; realizacja jako konkretny transport holonomii EM wymaga przyporządkowania. |
| λ w zmianie amplitudy jest dowolną wagą tego samego procesu | Wykluczone. W ustalonej rodzinie jest wyznaczone; nie jest automatycznie tym samym elementem co Γ₁₂. |
| Diagonalność lokalnego W | Ustalona w pierwotnym opisie z niezależnymi lokalnymi fazami i stałymi końcami. |
| Diagonalne W ustalone przez całe VV i Ward | Ustalona jednoznaczność przy niezerowych odpowiednich wierszach D₀ oraz zgodności równań. |
| W ustalone przez samo VV(0) dla całej rodziny | Nie wynika bez dodatkowego warunku profili i zależności od argumentu. |
| Gaussian daje jedną rezolwentę w argumencie rodziny | Nie wynika. Rezolwenta krokowa jest wyprowadzona dla jawnie powtarzalnej stacjonarnej klasy. |
| F₁=1, F₂=0 wybierają pełne D bez c·r | Ustalają zbieżną część dyspersyjną; do jednoznaczności potrzebna jest kontrola całej części analitycznej. |

**Następne miejsce pracy** jest określone: wybór dopuszczalnego elementarnego spinowego odczytu holonomii w K1 oraz przyporządkowanie i oszacowanie pełnego znormalizowanego jądra w K2. 179, 268 i 257 ustalają nośniki zależności i ich zgodne składanie; nie wolno zastąpić nimi niewyprowadzonej reguły wyboru kontaktów lub warunku wzrostu.

Nowa kontrola: **PASS, 38 nazwanych tożsamości algebraicznych**. Sprawdzono rzeczywistą operację pary, jeden wspólny Gram dwóch dróg, wszystkie elementy przykładowego Hessianu i jego więzów fazowych, rezolwentę powtarzalnej sekwencji oraz oba zachowania progowe. Nie jest to dowód konstrukcji fizycznego wierzchołka Pauliego, wyprowadzenie pełnej rodziny elektronowej ani dowód ograniczenia wzrostu D. Kod i wynik znajdują się w dodatkach C i D.

Źródła kontroli zakresu:

- Projekt: `regula-kompozycji-pelnego-odczytu-2026-10-12.md`, §§2.3–2.4, 4–5; `przyporzadkowanie-realizacji-dynamicznej-2026-10-12.md`, §§13.1–13.4, 16.6, 18.1, 19.1–19.4, 20.7; R1d i wpisy 179, 257 w źródłach ramy. Numer 268 jest wskazaniem użytkownika do reguły kompozycji; jej treść sprawdzono w osobnym raporcie, nie dopisano tego numeru do starszej kopii `poprawki.md`.
- A. Kızılersü, M. Reenders, M. R. Pennington, *One Loop QED Vertex in Any Covariant Gauge: Its Complete Analytic Form*, [hep-ph/9503238](https://arxiv.org/abs/hep-ph/9503238). Kontrola rozdzielenia części ustalonej tożsamością Ward od swobody poprzecznej.
- P. Niau Akmansoy, L. G. Medeiros, *Constraining nonlinear corrections to Maxwell electrodynamics using γγ scattering*, [Phys. Rev. D 99, 115005](https://doi.org/10.1103/PhysRevD.99.115005). Kontrola rozróżnienia symetrii U(1), liniowości równań i oddziaływań fotonów; wstęp i §II.
- M. Sugawara, A. Kanazawa, *Subtractions in Dispersion Relations*, [Phys. Rev. 123, 1895](https://doi.org/10.1103/PhysRev.123.1895). Zakres potwierdzenia: abstrakt twierdzenia wiąże liczbę odejmowań z kontrolą analityczności i wzrostu. Algebra niejednoznaczności Fγ+c·r jest podana tutaj niezależnie.

## Dodatek A. Kod kontrolny

Wymaga Python 3 i pakietu `sympy`. Po zapisaniu bloku jako `check_candidates.py` uruchomienie `python3 check_candidates.py` zapisuje obok wynik `check_candidates.json`. W tej kopii usunięto wyłącznie odwołanie do lokalnego katalogu zależności; treść rachunku jest zachowana.

```python
"""Checks of proposed test-128 candidates; no source-framework writeback."""
from pathlib import Path
import json
import sympy as s

count=0
def zero(label,x):
    global count
    if isinstance(x,s.MatrixBase):
        for v in x: zero(label,v)
        return
    value=s.trigsimp(s.simplify(x))
    assert value==0,(label,value)
    count+=1

I=s.eye(2); O=s.zeros(2)
sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
Sigma=[I]+sig; Bars=[I]+[-v for v in sig]
Q,a,theta=s.symbols('Q a theta',real=True)
neutral=s.symbols('h')
t=s.exp(s.I*Q*a)*neutral
zero('one oriented link first derivative',s.diff(t,a)-s.I*Q*t)
zero('one oriented link second derivative',s.diff(t,a,2)+Q*Q*t)

# A scalar phase on the entire unitary has Xi=0.
u_global=s.exp(s.I*Q*a)*I
Xglobal=-s.I*u_global.conjugate().T*s.diff(u_global,a)
zero('whole-unitary scalar phase current',Xglobal-Q*I)
zero('whole-unitary scalar phase Xi',s.diff(Xglobal,a))

# End labels, NOT chirality labels. Additive commuting LR mass does not change
# this result. This is a full Hermitian link evolution, not the bare t block.
K=s.Matrix([[0,s.exp(s.I*Q*a)],[s.exp(-s.I*Q*a),0]])
u=s.cos(theta)*I-s.I*s.sin(theta)*K
u0=u.subs(a,0); up=s.diff(u,a).subs(a,0); upp=s.diff(u,a,2).subs(a,0)
X=-s.I*u0.conjugate().T*up
Xi=-s.I*(up.conjugate().T*up+u0.conjugate().T*upp)
Xtarget=Q*(s.cos(theta)*s.sin(theta)*sig[1]-s.sin(theta)**2*sig[2])
Xitarget=Q*Q*s.sin(theta)*s.cos(theta)*sig[0]
zero('endpoint link unitary',u0.conjugate().T*u0-I)
zero('full link current',X-Xtarget)
zero('full link Xi',Xi-Xitarget)
zero('second derivative identity',u0.conjugate().T*upp+X*X-s.I*Xi)
v=s.symbols('v',real=True)
N=(I+v*sig[0])/2
zero('nonzero instantaneous expectation',s.trace(N*Xi)-v*Q*Q*s.sin(theta)*s.cos(theta))

# Canonical LR Schur reduction: test the full determinant Hessian, all source
# directions, rather than assigning the induced contact a scalar polarization.
mode_exchange=sig[0]
seagull_samples=[]; schur_entries=0
def four(p):
    return sum((p[i]*Sigma[i] for i in range(4)),s.zeros(2))
def barfour(p):
    return sum((p[i]*Bars[i] for i in range(4)),s.zeros(2))
for mass,pa,pb in [(1,(3,0,0,1),(5,0,1,2)),
                   (2,(4,1,0,1),(6,0,2,1)),
                   (3,(5,1,1,0),(7,1,0,2))]:
    L=s.diag(four(pa),four(pb)); R=s.diag(barfour(pa),barfour(pb))
    e=s.eye(4); z=s.zeros(4)
    full=(-mass*e).row_join(L).col_join(R.row_join(-mass*e))
    G=full.inv(); S=(L*R-mass*mass*e)/mass; GS=S.inv()
    VL=[s.kronecker_product(mode_exchange,j) for j in Sigma]
    VR=[s.kronecker_product(mode_exchange,j) for j in Bars]
    VV=[z.row_join(VL[i]).col_join(VR[i].row_join(z)) for i in range(4)]
    Si=[(VL[i]*R+L*VR[i])/mass for i in range(4)]
    for mu in range(4):
        for nu in range(4):
            Sij=(VL[mu]*VR[nu]+VL[nu]*VR[mu])/mass
            eta=int(mu==nu)*(1 if mu==0 else -1)
            zero('induced contact tensor',Sij-s.Rational(2,mass)*eta*e)
            full_h=-s.trace(G*VV[mu]*G*VV[nu])
            contact=s.trace(GS*Sij)
            bubble=-s.trace(GS*Si[mu]*GS*Si[nu])
            zero('complete Schur Hessian',full_h-contact-bubble)
            schur_entries+=1
            if mu==nu==0:seagull_samples.append(str(contact))

# Transversality does not set the scalar coefficient or its slope.
q=s.Matrix(s.symbols('q0 q1 q2 q3',real=True)); metric=s.diag(1,-1,-1,-1)
q2=(q.T*metric*q)[0]
C0,C1=s.symbols('C0 C1',real=True)
transverse=(q2*metric-q*q.T)*(C0+C1*q2)
zero('constant and linear transverse structures',(q.T*metric)*transverse)

# A local contact in link-phase variables can acquire argument dependence
# when those phases are projected onto a source profile.
omega=s.symbols('omega',real=True)
profile_square=2*(1-s.cos(omega))/omega**2
profile_series=s.series(profile_square,omega,0,6).removeO()
zero('profile contact expansion',profile_series-(1-omega**2/12+omega**4/360))

# Closed transported channels are real below their pole, but change the read.
zeta,g,M=s.symbols('zeta g M',real=True,nonzero=True)
sigma=g*g/(zeta-M)
zero('closed channel slope',s.diff(sigma,zeta).subs(zeta,0)+g*g/M**2)

# Two carried arms already give order-Q^2 interference; number of paths is
# not, by itself, a count of additional internal EM propagators.
a1,a2=s.symbols('a1 a2',real=True)
prob=(1+s.cos(Q*(a1-a2)))/2
zero('two-chain interference order',s.diff(prob,a1,2).subs({a1:0,a2:0})+Q*Q/2)
lam=s.symbols('lambda',real=True)
holonomy=s.exp(s.I*Q*(a1-a2))
zero('holonomy current starts at one source insertion',s.diff(lam*(holonomy-1),a1).subs({a1:0,a2:0})-s.I*Q*lam)

out={'status':'PASS','exact_scalar_checks':count,
     'full_vs_reduced_hessians':schur_entries,
     'seagull_00_trace_samples':seagull_samples,
     'Xi_for_full_phase_hopping_unitary':'Q^2 sin(theta) cos(theta) tau_x',
     'Xi_for_global_phase_unitary':'0',
     'link_profile_square_series':str(profile_series),
     'closed_channel_slope_at_zero':'-g^2/M^2',
     'scope':'bare link jets, full contact identity, canonical LR reduction; no proof of a frame-selected scalar EM polynomial or perturbative-order identification'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
```

## Dodatek B. Zapisany wynik kontroli

```json
{
  "status": "PASS",
  "exact_scalar_checks": 851,
  "full_vs_reduced_hessians": 48,
  "seagull_00_trace_samples": [
    "104/133",
    "74/135",
    "2/5"
  ],
  "Xi_for_full_phase_hopping_unitary": "Q^2 sin(theta) cos(theta) tau_x",
  "Xi_for_global_phase_unitary": "0",
  "link_profile_square_series": "omega**4/360 - omega**2/12 + 1",
  "closed_channel_slope_at_zero": "-g^2/M^2",
  "scope": "bare link jets, full contact identity, canonical LR reduction; no proof of a frame-selected scalar EM polynomial or perturbative-order identification"
}
```

## Dodatek C. Kod kontroli K1–K2

Wymaga Python 3 i `sympy`. Po zapisaniu jako `check_k1_k2.py` uruchomienie zapisuje obok wynik JSON.

```python
"""Exact diagnostics for K1 and K2, with fixed operations and their own Grams.

These are algebraic scope checks, not a construction of the physical EM family.
Requires Python 3 and sympy. Writes check_k1_k2.json alongside this script.
"""
from pathlib import Path
import json
import sympy as s

checks = []


def zero(label, value):
    items = list(value) if isinstance(value, s.MatrixBase) else [value]
    for item in items:
        reduced = s.trigsimp(s.simplify(item))
        if reduced != 0:
            reduced = s.trigsimp(s.simplify(s.expand_complex(reduced)))
        assert reduced == 0, (label, reduced)
    checks.append(label)


I = s.eye(2)
sx = s.Matrix([[0, 1], [1, 0]])
sy = s.Matrix([[0, -s.I], [s.I, 0]])
sz = s.diag(1, -1)

# A real pair event transfers a relative phase; it is not cloning.
phi, chi = s.symbols('phi chi', real=True)
swap = s.Matrix([[1, 0, 0, 0], [0, 0, 1, 0],
                 [0, 1, 0, 0], [0, 0, 0, 1]])
pair = s.exp(s.I*s.pi/4)*swap
zero('pair unitary', pair.conjugate().T*pair-s.eye(4))
zero('pair determinant is one', pair.det()-1)
phase_rotation = s.diag(1, s.exp(s.I*chi))
joint_rotation = s.kronecker_product(phase_rotation, phase_rotation)
zero('pair respects joint U1 rotation', pair*joint_rotation-joint_rotation*pair)
initial = s.Matrix([1, 0, s.exp(s.I*phi), 0])/s.sqrt(2)
target = s.exp(s.I*s.pi/4)*s.Matrix([1, s.exp(s.I*phi), 0, 0])/s.sqrt(2)
zero('relative phase transferred by the pair event', pair*initial-target)
zero('spectator extension is unitary',
     s.kronecker_product(pair, I).conjugate().T*s.kronecker_product(pair, I)-s.eye(8))

# Two carried arms: amplitude coefficient is not the same as Gram overlap.
theta, phase, Q = s.symbols('theta phase Q', real=True)
c, b = s.cos(theta), s.sin(theta)
splitter = s.Matrix([[c, -b], [b, c]])
path0 = splitter*s.diag(1, 0)*splitter.T
path1 = splitter*s.diag(0, 1)*splitter.T
unitary = s.exp(s.I*Q*phase)*path0+path1
zero('carried two-path module is unitary', unitary.conjugate().T*unitary-I)
zero('amplitude lambda is cos(theta)^2',
     unitary[0, 0]-(1+c*c*(s.exp(s.I*Q*phase)-1)))
g11, g22, g12 = c**4, b**4, c*c*b*b
zero('two-path Gram has rank one', g11*g22-g12*g12)
zero('actual Gram overlap is lambda*(1-lambda)', g12-c*c*(1-c*c))
probability = s.expand(unitary[0, 0]*s.conjugate(unitary[0, 0]))
zero('probability uses that same Gram',
     probability-(g11+g22+2*g12*s.cos(Q*phase)))
zero('interference response is already order Q^2',
     s.diff(probability, phase, 2).subs(phase, 0)+2*Q*Q*g12)

# Two parallel oriented links. Their local reverse blocks are conjugate.
a1, a2 = s.symbols('a1 a2', real=True)
hop = s.exp(s.I*Q*a1)+s.exp(s.I*Q*a2)
kernel = s.Matrix([[3, hop], [s.conjugate(hop), 3]])
base = {a1: 0, a2: 0}
G = kernel.subs(base).inv()
V = [kernel.diff(a).subs(base) for a in (a1, a2)]
W = [[kernel.diff(a, d).subs(base) for d in (a1, a2)] for a in (a1, a2)]
contact = s.Matrix(2, 2, lambda i, j: -s.trace(G*W[i][j]))
bubble = s.Matrix(2, 2, lambda i, j: s.trace(G*V[i]*G*V[j]))
full = contact+bubble
explicit = s.hessian(-s.log(kernel.det()), (a1, a2)).subs(base)
zero('local W is contact diagonal', contact+s.Rational(4, 5)*Q*Q*I)
zero('VV has a nonzero same-contact contraction',
     bubble-s.Rational(2, 5)*Q*Q*s.ones(2))
zero('complete logdet Hessian', full-explicit)
gauge = s.Matrix([1, 1])
cycle = s.Matrix([1, -1])
zero('complete response annihilates pure gauge', full*gauge)
zero('completed contact plus off-diagonal VV',
     full-(-s.Rational(2, 5)*Q*Q*I+
           s.Rational(2, 5)*Q*Q*s.Matrix([[0, 1], [1, 0]])))
incomplete = contact + bubble - s.diag(bubble[0, 0], bubble[1, 1])
zero('omitting VV diagonal fails Ward by a definite amount',
     incomplete*gauge+s.Rational(2, 5)*Q*Q*gauge)

# Zero-argument Ward data do not fix a whole argument-dependent transverse part.
r, d0, d1 = s.symbols('r d0 d1', real=True)
transverse = (d0+d1*r)*cycle*cycle.T
zero('all transverse scalar slopes satisfy Ward', transverse*gauge)
zero('slope is invisible at zero argument',
     transverse.subs(r, 0)-d0*cycle*cycle.T)
zero('projection preserves the slope',
     (cycle.T*transverse*cycle)[0]/(cycle.T*(cycle*cycle.T)*cycle)[0]-(d0+d1*r))

# Gaussian response needs a homogeneous stationary sequence for a lag resolvent.
zeta = s.symbols('zeta')
n0, n1 = s.symbols('n0 n1', real=True)
unit_step = s.diag(1, s.exp(-s.I*s.pi/3))
N = s.diag(n0, n1)
lag_values = []
for m in range(1, 7):
    Xm = (unit_step.conjugate().T**m)*sx*(unit_step**m)
    answer = s.I*s.trace(N*(Xm*sx-sx*Xm))
    zero('retarded lag '+str(m), answer-2*(n0-n1)*s.sin(m*s.pi/3))
    lag_values.append(answer)
resolvent = s.sqrt(3)*(n0-n1)*zeta/(1-zeta+zeta*zeta)
series = s.series(resolvent, zeta, 0, 7).removeO()
for m, answer in enumerate(lag_values, 1):
    zero('resolvent coefficient '+str(m), series.coeff(zeta, m)-answer)

def transported(angle):
    step = s.diag(1, s.exp(-s.I*angle))
    return step.conjugate().T*sx*step

state = s.diag(1, 0)
X = [transported(angle) for angle in (0, s.pi/3, s.pi/2)]
near0 = s.I*s.trace(state*(X[1]*X[0]-X[0]*X[1]))
near1 = s.I*s.trace(state*(X[2]*X[1]-X[1]*X[2]))
zero('nonhomogeneous first adjacent response', near0-s.sqrt(3))
zero('nonhomogeneous second adjacent response', near1-1)

# Point-current and constant-Pauli threshold behavior, using the established map.
t = s.symbols('t', positive=True)
kappa = s.symbols('kappa', real=True)
beta = s.sqrt(1-4*t)
rho = beta*((1+kappa)**2+2*t*(1+kappa/(4*t))**2)
zero('constant Pauli high-energy weight', s.limit(t*rho, t, 0)-kappa*kappa/8)
zero('point current high-energy weight', s.limit(rho.subs(kappa, 0), t, 0)-1)
zero('one-subtraction near-edge divergence',
     s.limit(t*r*rho/(1+r*t), t, 0)-r*kappa*kappa/8)
zero('two-subtraction integrand finite at edge',
     s.limit(t*r*r*rho/(1+r*t), t, 0)-r*r*kappa*kappa/8)

output = {
    'status': 'PASS',
    'named_algebraic_checks': len(checks),
    'checks': checks,
    'two_path_example_at_theta_pi_over_4': {
        'amplitude_lambda': '1/2', 'Gram_12': '1/4'},
    'W_vertex': str(contact),
    'VV_including_diagonal': str(bubble),
    'full_response': str(full),
    'stationary_lag_resolvent': str(resolvent),
    'adjacent_nonhomogeneous_responses': [str(near0), str(near1)],
    'scope': 'pair transfer of relative state phase; fixed two-path Gram; Gaussian Hessian and Ward; stationary-step resolvent; threshold asymptotics. No proof of a frame-selected physical Pauli coupling or a scalar EM subtraction bound.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(output, ensure_ascii=False, indent=2))
```

## Dodatek D. Zapisany wynik kontroli K1–K2

```json
{
  "status": "PASS",
  "named_algebraic_checks": 38,
  "checks": [
    "pair unitary",
    "pair determinant is one",
    "pair respects joint U1 rotation",
    "relative phase transferred by the pair event",
    "spectator extension is unitary",
    "carried two-path module is unitary",
    "amplitude lambda is cos(theta)^2",
    "two-path Gram has rank one",
    "actual Gram overlap is lambda*(1-lambda)",
    "probability uses that same Gram",
    "interference response is already order Q^2",
    "local W is contact diagonal",
    "VV has a nonzero same-contact contraction",
    "complete logdet Hessian",
    "complete response annihilates pure gauge",
    "completed contact plus off-diagonal VV",
    "omitting VV diagonal fails Ward by a definite amount",
    "all transverse scalar slopes satisfy Ward",
    "slope is invisible at zero argument",
    "projection preserves the slope",
    "retarded lag 1",
    "retarded lag 2",
    "retarded lag 3",
    "retarded lag 4",
    "retarded lag 5",
    "retarded lag 6",
    "resolvent coefficient 1",
    "resolvent coefficient 2",
    "resolvent coefficient 3",
    "resolvent coefficient 4",
    "resolvent coefficient 5",
    "resolvent coefficient 6",
    "nonhomogeneous first adjacent response",
    "nonhomogeneous second adjacent response",
    "constant Pauli high-energy weight",
    "point current high-energy weight",
    "one-subtraction near-edge divergence",
    "two-subtraction integrand finite at edge"
  ],
  "two_path_example_at_theta_pi_over_4": {
    "amplitude_lambda": "1/2",
    "Gram_12": "1/4"
  },
  "W_vertex": "Matrix([[-4*Q**2/5, 0], [0, -4*Q**2/5]])",
  "VV_including_diagonal": "Matrix([[2*Q**2/5, 2*Q**2/5], [2*Q**2/5, 2*Q**2/5]])",
  "full_response": "Matrix([[-2*Q**2/5, 2*Q**2/5], [2*Q**2/5, -2*Q**2/5]])",
  "stationary_lag_resolvent": "sqrt(3)*zeta*(n0 - n1)/(zeta**2 - zeta + 1)",
  "adjacent_nonhomogeneous_responses": [
    "I*(-exp(I*pi/3) + exp(-I*pi/3))",
    "I*(-I*exp(-I*pi/3) - I*exp(I*pi/3))"
  ],
  "scope": "pair transfer of relative state phase; fixed two-path Gram; Gaussian Hessian and Ward; stationary-step resolvent; threshold asymptotics. No proof of a frame-selected physical Pauli coupling or a scalar EM subtraction bound."
}
```
