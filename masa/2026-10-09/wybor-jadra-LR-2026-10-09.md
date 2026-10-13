# Wybór jądra L/R: dodatniość, lokalna klasa i równoważność zapisów

09.10.2026. Krok 263, po ukończeniu masowego dopasowania 262. Polecenie użytkownika: zacząć badanie, czy relacje ramy uzasadniają przyjętą konstrukcję. Źródła projektu: R1a–R1c razem, R1d, 128, 179, 206–208, 213, 217, 222 i 257–262. Czas i 3D pozostają podstawą tej pracy. Nie wprowadzamy nowych fizycznych pól, cząstek ani danych pomiarowych.

## 1. Pytanie, oczekiwanie i zakres

Zapowiedziane pytanie dotyczyło konieczności jednogradientowej kinetyki i stałego sprzężenia L/R. Trzeba je najpierw odnieść do pełnego odczytu: rząd pochodnych sam w sobie zależy od sposobu zapisu.

**Spodziewam się…** tę samą relację Diraca można zapisać przy użyciu jądra drugiego rzędu, jeśli zachowamy źródła, sprzężenia, normę i wyznacznik. Natomiast dla ustalonego pełnego spinora, przy dodatniej reprezentacji spektralnej i dokładnie wielomianowym jądrze, wyższe pochodne mogą być wykluczone. Wówczas rząd i stałość współczynników wynikają z tych warunków, a nie z hasła „najprostsze działanie”.

**Zdanie o upadku…** konieczność pierwszego rzędu jako jedynej formy zapisu upada, jeśli zapis drugiego rzędu daje te same pełne odpowiedzi. Twierdzenie w klasie wielomianowej upada, jeśli niekonstantne rzeczywiste wielomiany a(s), b(s) dopuszczają niezerową nieujemną wektorową miarę spektralną odwrotności, w podanej niżej reprezentacji bez odejmowań. Wyprowadzenia z całej ramy nie ma, dopóki nie uzasadnimy wyboru tej klasy, pola i stanu.

**Odczyt:** odpowiedź między określonym przygotowaniem i efektem O, wraz z normowaniem, oraz funkcjonał zamkniętych odpowiedzi EM. Sama macierz jądra, bez wskazania źródeł i sprzężeń, nie jest odczytem. Przekształcenie reprezentacji musi zachować relację opisaną w 179 i 206.

**Jawne wejścia do twierdzenia:** jednorodny wyjściowy sektor kwadratowy jednego pełnego spinora L/R; wektorowy, parzysty przypadek z 257; standardowy adjoint tego spinora; dodatnia przestrzeń stanów z wybranym stanem próżniowym i warunkiem spektralnym; niezerowa miara wektorowa, dla której poniższa całka istnieje bez odejmowań; dokładnie wielomianowe odwrotne jądro w tej reprezentacji. Nie zakładamy z góry jednego bieguna, konkretnej masy ani skończonej całkowitej wagi spektralnej.

Wielomianowość oznacza tu dokładną lokalną, skończonego rzędu reprezentację różniczkową w jednorodnym sektorze. Nie jest tomografią lokalną P5, nie jest definicją relacji par i nie jest uciętym szeregiem efektywnym. Dodatniości nie przypisujemy automatycznie pełnemu propagatorowi naładowanego pola w cechowaniu kowariantnym. Twierdzenie dotyczy nazwanego dodatniego sektora wyjściowego, nie całego oddziałującego QED.

Pierwotny zapis oczekiwań sporządzono przed kontrolami. Poniższy dowód obejmuje całą klasę stopni; skończone przykłady sprawdzają znaki i granice zakresu.

## 2. Wynik w skrócie

**[A][T], warunkowo:** dla pełnego spinora o jądrze

\[
K_0(p)=a(s)\slashed p-b(s),\qquad s=p^2,
\]

przy wejściach z §1 dodatniość wymusza

\[
a(s)=a_0>0,\qquad b(s)=b_0\in\mathbb R,
\qquad K_0=a_0(\slashed p-\eta),\quad \eta=b_0/a_0.
\]

Jednogradientowość i stałość sprzężenia L/R przestają być osobnymi założeniami **wewnątrz tej klasy**. Nie wybrano samej klasy z R1a–R1c. Wartość |η| i stosunki takich wartości pozostają nieustalone. Zerowe η też jest dopuszczone przez samo twierdzenie; nie wyprowadza ono masywności czytającego.

**[A][T][L]:** tę samą konstrukcję dla η≠0 można przepisać na drugi rząd z dokładnie tymi samymi odpowiedziami. Dlatego ramie można przyporządkowywać fizyczną klasę równoważnych pełnych realizacji, a nie samą liczbę pochodnych w wybranej macierzy. Jest to zastosowanie kryterium odczytu z 179/206 i ostrzeżenia 222 o ocenianiu zależności zamiast formy zapisu.

To nie twierdzenie o nowości w literaturze. Użyte narzędzia są znane; poniżej podajemy własny krótki dowód warunkowego ograniczenia oraz jawne kontrole pełnego odczytu.

## 3. Dlaczego dodatnia miara nie może znikać w ten sposób

Piszemy propagator bez wspólnego czynnika i jako

\[
G(p)=K_0^{-1}(p)=\slashed p\,F_v(s)+F_s(s),
\qquad F_v(s)=\frac{a(s)}{s a(s)^2-b(s)^2}.
\]

Indeksy v i s oznaczają część wektorową i skalarną, nie odczyty A/B. Dodatnia reprezentacja widmowa ma postać

\[
G(p)=\int_{[0,\infty)}
\frac{\slashed p\,d\rho_v(t)+d\rho_s(t)}{s-t+i0},
\qquad d\rho_v\geq0,\quad \rho_v\ne0.
\]

To określony korelator w określonym stanie. Stożek R1c sam nie wybiera przepisu i0 ani tego przygotowania — 257.

Pochodzenie dodatniości: widmo funkcji ⟨ψψ†⟩ jest sumą macierzy vv† po stanach pośrednich. W czasopodobnej ramie spoczynkowej blok widmowy ma formę √t dρ_v I + dρ_s γ⁰. Jego dodatniość daje √t dρ_v ± dρ_s≥0, a więc dρ_v≥0 i |dρ_s|≤√t dρ_v; dla składowej bezmasowej tę samą nieujemność współczynnika wektorowego daje niezerowe p na stożku. Nie zakładamy dodatniości każdej składowej macierzy G. To znany argument spektralny; postać sumy dodatnich macierzy dla spinora jest np. w [L3], równania (2.18), (2.25)–(2.28). Warianty z niedodatnią przestrzenią stanów trzeba traktować osobno — [L4].

Dla rzeczywistego przestrzennego argumentu s=−x, x>0, określmy

\[
h(x):=-F_v(-x)
=\frac{a(-x)}{x a(-x)^2+b(-x)^2}
=\int_{[0,\infty)}\frac{d\rho_v(t)}{x+t}.
\]

Nie wykonywaliśmy obrotu Wicka ani nie wywodzimy struktury z czterech osi euklidesowych. Używamy niezmiennika s ze stożka R1c, po stronie przestrzennej. Wszystkie argumenty można wyrazić względem tego samego odniesienia czytającego.

Stąd

\[
xh(x)=\int\frac{x}{x+t}\,d\rho_v(t).
\]

Funkcja x/(x+t) jest niemalejąca w x. Ponieważ miara jest niezerowa i nieujemna, xh(x)>0 i nie może zbiegać do zera przy x→∞. Z twierdzenia o zbieżności monotonicznej granicą jest całkowita waga ρ_v([0,∞)), dodatnia lub nieskończona. **Nie trzeba zakładać jej wartości 1 ani skończoności.**

To jest rozstrzygające ograniczenie całej odpowiedzi spektralnej, mocniejsze od samego h(x)>0 przy każdym przestrzennym argumencie.

## 4. Dowód dla wszystkich wielomianów

Niech n=deg a≥0. Dla b≠0 niech k=deg b≥0; przypadek b=0 pomijamy w drugim członie maksimum. a=0 nie może reprezentować niezerowego dodatniego spinora: F_v=0 wyzerowałoby ρ_v, a warunek dodatniości również ρ_s.

Mianownik h(x) jest sumą x a(−x)²+b(−x)². Jego najwyższe potęgi mają stopnie 2n+1 i 2k, które nie mogą się równać. Nie występuje znoszenie ich wiodących współczynników. Zatem

\[
xh(x)\sim c\,x^{n+1-\max(2n+1,2k)}.
\]

- Jeśli n≥1, wykładnik jest nie większy niż −n<0.
- Jeśli n=0, ale k≥1, wykładnik jest nie większy niż 1−2k<0.

W obu przypadkach xh(x)→0, sprzecznie z §3. Wspólne czynniki a i b ani ich ewentualne skracanie w odwrotności nie zmieniają tej asymptotyki. Zostają wyłącznie a=a₀ i b=b₀ stałe, a dodatniość wymaga a₀>0. Wtedy

\[
G(p)=\frac1{a_0}\frac{\slashed p+\eta}{s-\eta^2+i0},
\quad d\rho_v=\frac1{a_0}\delta(t-\eta^2)dt,
\quad d\rho_s=\frac\eta{a_0}\delta(t-\eta^2)dt.
\]

Pojedynczy biegun jest **wnioskiem w tej klasie**, a nie ukrytym założeniem dowodu. Wspólna dodatnia normalizacja a₀ przenosi się razem ze źródłami i normą. Jak w 257, nie jest nowym niezależnym sprzężeniem EM.

**Znaczenie:** przy zadanej lokalnej klasie wyjściowej nie trzeba osobno postulować najniższego rzędu pochodnych. Odpowiedź z wyższym rzędem nie spełnia nazwanego warunku dodatniej realizacji. To nie zakaz wyższych pochodnych w każdym poprawnym zapisie fizyki.

## 5. Dwa testy granicy wyniku

**Dokładne wyższe pochodne przy niezmienionym pełnym spinorze.** Syntetyczny przykład a(s)=1, b(s)=s+3/16 daje

\[
G(p)=2\frac{\slashed p+1/4}{s-1/16}
-2\frac{\slashed p+3/4}{s-9/16}.
\]

Oba bieguny mają dodatnie kwadraty mas, lecz waga wektorowa drugiego jest −2. Zwykłe sprawdzenie rzeczywistych dodatnich mas ani h(x)>0 nie wykryłoby problemu. Dodatnia miara go wykrywa. Parametry są syntetyczne; nie proponujemy dodatkowych fizycznych cząstek ani modyfikacji QED.

**Po zdjęciu wielomianowości dodatniość nie wybiera Diraca.** Diagnostyczna suma

\[
G(p)=\frac12\frac{\slashed p+1}{s-1}
+\frac12\frac{\slashed p+2}{s-4}
\]

ma dodatnie wagi, natomiast jej odwrotność ma

\[
a(s)=\frac{s-5/2}{s-9/4},\qquad
b(s)=\frac{3s/2-3}{s-9/4}.
\]

Nie są wielomianami. xh(x)→1, więc test spektralny przechodzi. To świadek niezbędności założenia matematycznego, nie model całej ramy ani propozycja dwóch nowych pól. W szczególności nie dowodzi niewystarczalności całej podstawy. Biegun odwrotnego jądra przy s=9/4 nie jest nowym biegunem G.

Nie wolno stosować dowodu do skończonego obcięcia efektywnego szeregu: jego zachowanie przy x→∞ wykraczałoby poza zakres przybliżenia. Nie wolno też usuwać funkcji pętlowych z 261–262 — tam badamy odpowiedź po uwzględnieniu innych kanałów, a nie dokładne wielomianowe jądro swobodnego sektora.

## 6. Pierwszy i drugi rząd mogą oznaczać dokładnie ten sam odczyt

Znany zapis drugiego rzędu fermionów jest równoważny Diracowi, także dla zewnętrznych fermionów [L1–L2]. Tutaj sprawdzamy to wprost na blokach, aby kryterium wyboru zachowywało źródła O z 179/206. To zastosowanie redukcji z 260 do stałego bloku masowego, a nie drugie wyprowadzenie ogólnego dopełnienia Schura.

Dla niezerowego stałego η i operatorów kinetycznych L[a], R[a] piszemy

\[
\mathscr D[a]=\begin{pmatrix}-\eta I&L[a]\\R[a]&-\eta I\end{pmatrix},
\qquad \mathscr Q[a]=L[a]R[a]-\eta^2I.
\]

Nie wymagamy LR=RL. Z równania 𝒟ψ=j otrzymujemy dokładnie

\[
\psi_L=\mathscr Q^{-1}(\eta j_L+Lj_R),\qquad
\psi_R=(R\psi_L-j_R)/\eta.
\]

Zatem

\[
\mathscr D^{-1}=\begin{pmatrix}
\eta\mathscr Q^{-1}&\mathscr Q^{-1}L\\
R\mathscr Q^{-1}&(R\mathscr Q^{-1}L-I)/\eta
\end{pmatrix}.
\]

Równość dotyczy całej macierzy, więc zachowuje każde ustalone przygotowanie i efekt, po ich zgodnym zapisaniu. W bilinearnej odpowiedzi źródłowej przychodzą jednocześnie:

\[
\bar j\mathscr D^{-1}j
=\eta(\bar j_L+\bar j_RR/\eta)\mathscr Q^{-1}
(j_L+Lj_R/\eta)-\bar j_Rj_R/\eta.
\]

Ostatni człon jest kontaktem źródłowym. Pominięcie go zmienia odpowiedź. Nie można zastąpić 𝒟⁻¹ przez 𝒬⁻¹, pozostawiając stare końce, adjoint i normę.

Dla rozwiązań bez źródeł odtworzenie ψ_R=Rψ_L/η zachowuje też dodatnią normę pełnego Diraca: w obrazie hamiltonowskim jest to całka z ψ_L†ψ_L+(Rψ_L)†(Rψ_L)/η² na tym samym przekroju czytającego, z tymi samymi warunkami brzegowymi. Drugi rząd ma odpowiednie dodatkowe dane Cauchy'ego, które odtwarzają eliminowane składowe; nie dopisuje niezależnych stanów ponad pełnego Diraca. Zachowana norma nie jest naiwną normą samej zmiennej drugiego rzędu. Warunki rzeczywistości i zewnętrzne końce w takim zapisie omawia [L2].

W regularizacji, w której wykonujemy tę samą całkę Gaussa, zachodzi

\[
\det\mathscr D=\det(-\eta I)\det(\mathscr Q/\eta)
=\det(-\mathscr Q).
\]

Jest to dokładna tożsamość dla skończonych macierzy; w teorii pola przenosimy ją przez tę samą regulowaną całkę i zgodne kontrczłony, nie przez dowolne niezależne definicje nieskończonych wyznaczników. Zachowujemy przepis brzegowy odziedziczony z pełnej teorii. Przejście jest osobliwe przy η=0; bezmasowy przypadek trzeba opisać osobno. Zmienna masa lub tło Higgsa również wymaga dodatkowych członów, nie prostego podstawienia η(x).

## 7. Sprzężenie EM i kontakty nie są dodatkowymi wagami

Przy D_μ=∂_μ+ieQ a_μ, Π_μ=iD_μ oraz σ^{μν}=i[γ^μ,γ^ν]/2 mamy

\[
[\Pi_\mu,\Pi_\nu]=-ieQF_{\mu\nu},\qquad
(\slashed\Pi)^2=\Pi^2-\frac{eQ}{2}\sigma^{\mu\nu}F_{\mu\nu}.
\]

Stąd blok drugiego rzędu zawiera ustalony składnik spinowy oraz kontakt dwóch pól a z Π². Współczynnik spinowy został odziedziczony po minimalnym pełnym jądrze. Nie wyprowadziliśmy minimalnego sprzężenia z ramy, nie ustawiliśmy anomalii magnetycznej na zero i nie wybraliśmy tym argumentem całej poprzecznej części pełnego wierzchołka.

Dla dwóch wariacji a, ponieważ L i R są liniowe:

\[
\delta_i\mathscr Q=(\delta_iL)R+L(\delta_iR),\qquad
\delta_j\delta_i\mathscr Q=(\delta_iL)(\delta_jR)+(\delta_jL)(\delta_iR).
\]

W szczególności równość zamkniętej odpowiedzi brzmi

\[
-\operatorname{Tr}(\mathscr D^{-1}\delta_j\mathscr D\,
\mathscr D^{-1}\delta_i\mathscr D)
=\operatorname{Tr}\left(\mathscr Q^{-1}\delta_j\delta_i\mathscr Q
-\mathscr Q^{-1}\delta_j\mathscr Q\,\mathscr Q^{-1}\delta_i\mathscr Q\right).
\]

Kontakt drugiej wariacji jest potrzebny nawet wtedy, gdy pełne jądro 𝒟 miało tylko liniowy wierzchołek. Źródła po redukcji również zależą od a i muszą być różniczkowane. Dokładne kontrole obejmują obie te rzeczy.

## 8. Co wynika z ramy, a co nadal jest wejściem

| Warunek lub wybór | Pochodzenie i wynik testu wierności |
|---|---|
| Porównujemy pełne odczyty, a nie samotne jądra | 179: O widzi kanał, nie wybrane wnętrze obwodu; 206: odczyt jest różnicą własnych stanów O. Dwa kompletne zapisy z identycznymi odpowiedziami nie są rozróżniane przez takie O. |
| Algebra spinora i niezmiennik s | Istniejące R1b–R1d i przyporządkowanie z 257. Nie wyprowadzamy ich ponownie. |
| Brak ujemnych norm w nazwanej realizacji odczytów | Dodatniość probabilistyczna jest wymagana. Przeniesienie jej na miarę konkretnego spinorowego korelatora wymaga jednak wskazanego pola, adjointu, stanu i warunku spektralnego. Ten most nie wynika z samego słowa „odczyt”. |
| Jeden pełny wektorowy sektor L/R, parzystość, jednorodny stan | To nazwany sektor QED z 257. Rama nie wybiera tu całego spektrum SM ani nie usuwa rozróżnienia słabego L/R. |
| Dokładnie wielomianowe odwrotne jądro i reprezentacja bez odejmowań | Pozostają hipotezami klasy. P5 nie jest lokalnością różniczkową; 179 nie daje skończonego rzędu w argumentach fazowych. Nie uzyskano testu, że zanegowanie tych hipotez łamie całą ramę. |
| Pierwszy rząd i stałe a,b w tej klasie | Wynik §§3–4. Nie trzeba przyjmować ich osobno po spełnieniu wszystkich wejść. |
| Wartość η i stosunki mas | Nie są wybrane: każde rzeczywiste η ma podaną dodatnią realizację spektralną. Masywność O z 206 nie ustala niezerowej wartości ani hierarchii. |
| Sprzężenie minimalne, jądro EM i stan użyty w pętlach | Pozostają warunkami 257. Przepisanie na drugi rząd zachowuje ich konsekwencje, nie wybiera tych wejść. |

**Co zostało rozstrzygnięte:** usunięto potrzebę osobnego założenia jednogradientowości i stałości współczynników po przyjęciu wskazanej dodatniej lokalnej klasy pełnego spinora. Jednocześnie odrzucono kryterium, które wybierałoby teorię po rzędzie dowolnej zredukowanej macierzy. Nie zmniejszyła się liczba niewyprowadzonych parametrów fizycznych z bilansu 208. Nie uzyskano pełnego przyporządkowania kanonicznych modów i stanu relacjom par.

## 9. Konsekwencja dla 262 i miejsce dalszej pracy

Zapis pierwszego i drugiego rzędu daje ten sam pełny funkcjonał fermionów przy dowolnym zewnętrznym a, jeżeli końce i wyznacznik są zachowane. Włączenie tego samego sektora fotonowego i tego samego schematu perturbacyjnego nie zmienia przez samą zmianę zapisu dopasowania 262. Nie liczymy po raz drugi dwóch pętli i nie przedstawiamy tej tożsamości jako niezależnej kontroli opublikowanych współczynników.

Warunkowe ograniczenie jądra wyjściowego jest zgodne z użyciem w 262 kanonicznego K₀. Nie usuwa funkcji pełnej energii własnej, progów α ani odpowiedzi po eliminacji kanałów. Nie daje nowego równania na R_B ani zmiany współczynników dopasowania. Sama wartość η pozostaje dopuszczalnym stosunkiem odniesienia, który nie został wybrany przez dowód.

**Następna konkretna luka:** wykazać albo odrzucić przyporządkowanie relacjom 179/206 takiej dodatniej, jednorodnej realizacji spinorowej, w której dokładne wyjściowe odwrotne jądro jest wielomianem bez brakującej pamięci kanałów. Należy kontrolować wraz z nią stan, adjoint, źródła i regułę kontrakcji. Redukcje z 259–260 pokazują, dlaczego pominięte kanały na ogół pozostawiają zależność spektralną; sama nazwa „pełny L/R” nie dowodzi, że wszystkie istotne kanały już ujęto. To jest miejsce, gdzie potrzebny byłby nowy wniosek z ramy. W tym kroku takiego dowodu nie uzyskano.

## 10. Kontrole i literatura

Kod `wybor-jadra-LR-kontrola-2026-10-09.py`, wynik `.json`. **PASS**, dokładne zespolone ułamki, bez tolerancji i dopasowania danych. Primitives macierzowe przeniesiono z kontroli 260; nowe kontrole porównują bezpośrednią odwrotność z odtworzeniem drugiego rzędu.

- 16 relacji Clifforda; nieprzemienny test składnika spinowego na macierzy 8×8, który nie przechodzi po jego pominięciu.
- 3 pełne odwrotności i wyznaczniki; źródłowy kontakt sprawdzony na całej macierzy odpowiedzi.
- 12 pierwszych i 48 drugich wariacji pełnej odpowiedzi źródłowej; tyle samo porównań pochodnych logarytmu wyznacznika. Usunięcie kontaktu dwóch wstawek zmienia 12 z 48 badanych zamkniętych odpowiedzi.
- Dokładne tożsamości wielomianowe dla widma z wagami 2, −2 i dodatniego przykładu z odwrotnością niewielomianową.
- Kontrola nierówności stopni na 90 parach jest wyłącznie kontrolą zapisu. Dowodem dla wszystkich stopni pozostaje §4.

**[L1]** A. G. Morgan, *Second Order Fermions in Gauge Theories*, Phys. Lett. B 351 (1995), 249–256, [hep-ph/9502230](https://arxiv.org/abs/hep-ph/9502230). Znana równoważność formalizmów, także dla zewnętrznych fermionów; rachunek determinantów i wierzchołków.

**[L2]** J. Espin, K. Krasnov, *Second Order Standard Model*, Nucl. Phys. B 895 (2015), 248–271, [1308.1278](https://arxiv.org/abs/1308.1278). Używamy wyłącznie informacji o równoważnym zapisie fermionów, końcach i warunkach rzeczywistości. Nie przejmujemy proponowanych rozszerzeń ani unifikacji.

**[L3]** A. Ahmed et al., *General form of effective operators from hidden sectors*, [2412.15067](https://arxiv.org/abs/2412.15067), §2.2, równania (2.18), (2.25)–(2.28). Kontrola znanej konstrukcji spinorowej miary jako sumy dodatnich macierzy. Żaden ukryty sektor ani operator portalowy z tej pracy nie jest składnikiem naszego modelu. Ograniczenie wielomianów z §4 jest tutaj wyprowadzone jawnie; nie przypisujemy go tej publikacji.

**[L4]** P. Lowdon, *Non-perturbative constraints on the quark and ghost propagators*, [1711.07569](https://arxiv.org/abs/1711.07569), §2. Postać spinorowego rozkładu spektralnego i znaczenie niedodatniej przestrzeni stanów. Kontrola granicy stosowalności, nie przeniesienie rachunku na QCD.
