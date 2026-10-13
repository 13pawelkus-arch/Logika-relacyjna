20. ## Odpowiedź progowa pary: przekład prądu L/R, miary i rekonstrukcji przyczynowej

Kierunek pracy: **przekład rachunków literatury na ramę**. R1a–R1c pozostają ustaloną podstawą projektu; poniżej kontrolujemy przyporządkowania użyte w nowym rachunku.

**Wynik.** Ogon miary z §19 jest dokładnie znormalizowaną wagą progową pary z 255/261. W klasie punktowego bilinearnego prądu wektorowego rachunek na macierzach 2×2 wyprowadza dwie wagi E² oraz jedną m². Kontrola dla punktowego nośnika bez spinu daje β³/4. Nie potrzeba do tych obliczeń pełnej neutralnej rodziny kontaktów ani obrotu Wicka. Pozostają osobne przyporządkowania: wybór właśnie tego prądu, pełnego kanału pary i jego miary oraz warunki rekonstrukcji odpowiedzi z części absorpcyjnej. Nie utożsamiamy ich z koniecznością wybrania całego działania.

**Odczyt i zakres.** Badamy inkluzywną produkcję swobodnej pary o jednakowych masach m, odczytaną względem punktowego bezmasowego kanału fermionowego, w tym samym wiodącym rzędzie wektorowej odpowiedzi EM. Zachowujemy wszystkie stany spinowe pary i ten sam ładunek w odniesieniu. Nie włączamy oddziaływań końcowej pary, dodatkowych kanałów ani wyższych poprawek do prądu do definicji jednopętlowego F_γ. Zastosowanie sumy po całym kanale do konkretnego aparatu wymaga odczytu inkluzywnego; wybiórczy efekt lub przygotowanie nie zostaje przez nią zastąpione.

**Oczekiwanie i zdanie o upadku.** Wskazany prąd ma dać wagę β[1+m²/(2E²)], a skalar β³/4. Mocniejsze zdanie użytkownika wymaga ponadto testu 128: pokazać, z którym konkretnym zdaniem R1b–R1d/R1f wyklucza się odmienny prąd, miara lub rekonstrukcja. Zgodność rachunku w jednej klasie nie zastępuje tego testu.

### 20.1. Ogon miary jest wagą produkcji pary

Z miary wyznaczonej w §19 zachowujemy t∈[0,1/4] i

\[
d\nu_\gamma(t)=\frac{4t}{\sqrt{1-4t}}\,dt,
\qquad \widehat\rho(t)=\sqrt{1-4t}(1+2t).
\tag{20.1}
\]

Dokładnie

\[
\frac{d}{dt}\frac{\widehat\rho(t)}3
=-\frac{4t}{\sqrt{1-4t}},
\qquad
\nu_\gamma([t,1/4])=\frac{\widehat\rho(t)}3.
\tag{20.2}
\]

Oba końce wynoszą odpowiednio 1/3 i 0. Całkowanie przez części, przy ln(1+rt)=0 w t=0, daje

\[
F_\gamma(r)
=\int_0^{1/4}\ln(1+rt)\,d\nu_\gamma(t)
=\frac13\int_0^{1/4}\widehat\rho(t)\frac{r\,dt}{1+rt}.
\tag{20.3}
\]

To tożsamość funkcji; x(1−x) jest argumentem miary w jednym zapisie tej samej odpowiedzi. Nie staje się przez to elementem kontaktu ani własnością obiektu.

Dla k≥1 integracja ogona daje

\[
\mu_k=\frac{k}{3}\int_0^{1/4}t^{k-1}\widehat\rho(t)\,dt
=\frac{2[(k+1)!]^2}{(2k+3)!},
\qquad \mu_0=\frac13.
\tag{20.4}
\]

Sprawdzono dokładnie μ₀…μ₉; pierwsze cztery są 1/3, 1/15, 1/70, 1/315. Miara celu jest dodatnia i bez atomu w t=0. Jak w §19, sam logarytm nie widzi ewentualnego atomu w zerze; jego masa wymaga dodatkowego ustalenia normalizacji.

Po t=m²/s oraz Q²=m²r otrzymujemy

\[
F_\gamma(Q^2/m^2)
=\frac{Q^2}{3}\int_{4m^2}^{\infty}
\frac{ds}{s(s+Q^2)}\widehat\rho(m^2/s)
=\frac13\int_{4m^2}^{\infty}\frac{ds}{s}
\frac{Q^2}{s+Q^2}\widehat\rho(m^2/s).
\tag{20.5}
\]

Ten zapis jest bezpośrednim miejscem wagi pary ρ_f z 261, po usunięciu α₀c_f/(3π), i normalizacji otwartego kanału μμ w 255. `ds/s` jest miarą porównań multiplikatywnych tego rodzaju, który analizuje 212. Nie wynika z samej addytywności porównań cały czynnik Q²/(s+Q²): pochodzi on z rekonstrukcji omawianej w §20.6. Dla stałej wagi ρ̂=1 całka daje ln(1+r/4)/3. Próg zmienia skończoną część i momenty, zachowując współczynnik wiodącego logarytmu.

**Normalizacja wobec 155.** Dla spin½ wyrażenie (2s_z)²−1/3 daje 2/3. Współczynnik μ₀=1/3 stoi przy ln r=ln(Q²/m²), a d ln r/d ln Q=2. Przy δα=α₀²F_γ/π wiodąca pochodna po ln Q wynosi 2α₀²/(3π). Zgodność wymaga zachowania tego czynnika 2; nie utożsamiamy rozkładu spin/orbita w stałym polu z rozkładem kierunków prądu pary.

### 20.2. Macierze relacji pary: wyznacznik i zygzak

W opisie czytającego parę ustalamy kierunek n jako odniesienie i używamy macierzy z R1c/R1f:

\[
P_\pm=E\mathbb1\pm p\,n\!\cdot\!\sigma,
\quad \det P_\pm=m^2,
\quad P_++P_-=2E\mathbb1,
\quad s=\det(2E\mathbb1)=4E^2.
\tag{20.6}
\]

To zapis relacji nośników; nie dodaje areny. Dla n=e₃ możemy użyć dodatnich pierwiastków

\[
A=\sqrt{P_+}=\operatorname{diag}(a,b),\quad
B=\sqrt{P_-}=\operatorname{diag}(b,a),
\quad a=\sqrt{E+p},\quad b=\sqrt{E-p}.
\tag{20.7}
\]

Z ich iloczynu wynika

\[
AB=m\mathbb1,\qquad
\frac mE=\frac{\sqrt{(E+p)(E-p)}}{[(E+p)+(E-p)]/2},
\qquad \beta=\frac pE=\sqrt{1-\frac{m^2}{E^2}}.
\tag{20.8}
\]

Średnia geometryczna i arytmetyczna dotyczą dwóch wartości własnych macierzy relacji; nie dwóch nowych zegarów. Przekład m/E jako stosunku własnego tyknięcia do odczytu czytającego korzysta z R1d-134 i R1f-3. L/R pozostają składnikami jednego nośnika, a nie nazwami końców transportu ani materii/antymaterii.

W kanonicznym opisie masowego zygzaka rozwiązania obu orientacji kanału pary można zapisać

\[
u(p)=\begin{pmatrix}B\xi\\ A\xi\end{pmatrix},\qquad
v(-p)=\begin{pmatrix}A\eta\\-B\eta\end{pmatrix}.
\tag{20.9}
\]

Spełniają odpowiednie blokowe równania masowe z P_± i sprzężeniem m oraz u†u=v†v=2E przy jednostkowych ξ,η. Tę realizację swobodnego kanału i jego dualnego odczytu nazywamy jawnie. Nie zastępuje ona dowodu, że dowolna rodzina kontaktów realizuje właśnie taki kanał.

### 20.3. Punktowy prąd: wagi 1,1,(m/E)² z samej algebry 2×2

W klasie bilinearnego prądu wektorowego, zależnego od spinorów w jednym kontakcie i bez dodatkowych wstawek pochodnych, dwa bloki chiralne mają postać L†barσ^μL i R†σ^μR. Są to standardowe mapy spinorów na wektor; ich macierze składają się z 𝟙 i σ_i z R1b. Masa wiąże L z R. Generator EM diag(q_L,q_R) zachowuje to sprzężenie wtedy, gdy q_L=q_R dla m≠0. Wektorowy prąd o wspólnym ładunku ma zatem równe współczynniki obu bloków. Różny współczynnik dawałby prąd osiowy, którego masa nie zachowuje.

**Istotny zakres:** powyższe ustala prąd w nazwanej klasie bez wstawek pochodnych. Nie jest dowodem wykluczającym wszystkie prądy o tej samej całkowitej fazie EM. Symbol γ^μ można złożyć z tej algebry; jego zapis sam w sobie nie dodaje nowego spinora ani areny. Wybór tej klasy odpowiedzi to osobna kwestia (§20.7).

Po podstawieniu (20.9) do tego prądu otrzymujemy, do wspólnego znaku,

\[
J^0=\xi^\dagger(BA-AB)\eta=0,
\qquad J_i=-\xi^\dagger M_i\eta,
\qquad M_i=A\sigma_iB+B\sigma_iA.
\tag{20.10}
\]

Macierze dają dokładnie

\[
M_1=2E\sigma_1,\quad M_2=2E\sigma_2,
\quad M_3=2m\sigma_3.
\tag{20.11}
\]

Pełna suma po obu bazach spinowych to norma macierzy, a nie założenie o równym przygotowaniu spinów konkretnego aparatu:

\[
\sum_{\xi,\eta}|J_i|^2=\operatorname{tr}(M_iM_i^\dagger)
=8\,(E^2,E^2,m^2)_i.
\tag{20.12}
\]

Względem dwóch kierunków bezmasowego odniesienia otrzymujemy

\[
\frac{2E^2+m^2}{2E^2}=1+\frac12(m/E)^2.
\tag{20.13}
\]

Po obrocie odniesienia pełny tensor ma postać

\[
\sum J_iJ_j^*=8(E^2\delta_{ij}-p^2n_in_j).
\tag{20.14}
\]

Uśrednienie orientacji względem czytającego daje tę samą wagę. Zapis zaproponowany przez użytkownika jest **ilorazem całek po c∈[−1,1]**, nie tożsamością punktową:

\[
\frac{\int_{-1}^{1}[(1+c)^2+(1-c)^2+2(1-\beta^2)(1-c^2)]\,dc}{16/3}
=\frac{3-\beta^2}{2}.
\tag{20.15}
\]

W tej klasie trop m/E staje się dokładną tożsamością amplitud. Nie interpretujemy jednak podłużnej wagi jako pojedynczego policzonego kontaktu L↔R: jest macierzowym skutkiem pełnego parowego prądu i sprzężenia masowego. Liczba dwóch kierunków w granicy β→1 jest zgodna z R1e; tutaj są one kierunkami prądu względem n, a nie utożsamionymi z nim stanami źródła. Przy β→0 tensor staje się izotropowy.

### 20.4. Kontrola ujemna: nośnik bez spinu

Dla punktowego skalarnego prądu o tym samym ładunku J_i=(p_1−p_2)_i=2pn_i. Nie ma sumy po dwóch spinorowych bazach. Po odczycie poprzecznym względem osi czytającego k, z c=n·k,

\[
W_0(c)=4p^2(1-c^2),\qquad
W_{1/2,\mathrm{ref}}(c)=8E^2(1+c^2).
\tag{20.16}
\]

Przy tej samej dwuciałowej mierze stosunek wynosi

\[
R_0=\beta\,
\frac{\int_{-1}^{1}W_0(c)\,dc}{\int_{-1}^{1}W_{1/2,\mathrm{ref}}(c)\,dc}
=\frac{\beta^3}{4}.
\tag{20.17}
\]

Kontrola przeszła dokładnie. Droga odróżnia skalar od spin½, gdy używa odpowiednich punktowych prądów. Nie uzasadnia to jeszcze wyboru tych prądów dla wszystkich realizacji ramy. Literaturowa kontrola: CLEO, hep-ex/0510005, równanie (2), po ustawieniu punktowego skalarnego form factor na 1; nie korzystamy z modelu struktury mezonu.

### 20.5. Czynnik β jako stosunek miar kanału pary

Na ustalonej dodatniej orbicie det P=m² grupa SL(2,ℂ) działa przechodnio; stabilizatorem spoczynkowego odniesienia jest SU(2). Niezmiennicza miara pełnej orbity jest określona do stałego czynnika. W macierzowych etykietach P=E𝟙+p·σ jest to standardowa miara powłoki d³p/(2E). Jej użycie jako miary relacji nie wymaga przestrzeni jako osobnego pojemnika.

Trzeba jednak odróżnić **miarę pełnej orbity** od rzeczywistych wag przygotowania, aparatu i liczności kanałów. Niezmienniczość nie dowodzi, że dowolny konkretny odczyt obejmuje całą orbitę z tą miarą. Właśnie to przyporządkowanie musi być sprawdzone w ramie.

W standardowej miarze iloczynowej swobodnej pary i przy zachowanej sumie P_1+P_2 radialny rachunek w d kierunkach daje

\[
\Phi_2\ \propto\ \int\frac{p^{d-1}dp}{4E_p^2}
\delta(\sqrt{s}-2E_p)
=\frac{p^{d-2}}{8E},
\qquad E=\sqrt{s}/2.
\tag{20.18}
\]

Przy tym samym s i masach odniesienia 0, stałe normowania i E znoszą się:

\[
\frac{\Phi_2(s;m)}{\Phi_2(s;0)}=\beta^{d-2}=\beta\quad(d=3).
\tag{20.19}
\]

To daje (b) w tej nazwanej realizacji pełnego kanału. Wykładnik d−2 jest tym samym zliczeniem liczby kierunków pozostałych po ustaleniu relacji pary, które przy d=3 wynosi 1. Nie zastępuje dowodu dotyczącego logarytmu: miara ds/s w (20.5) i radialny jakobian w (20.18) pełnią różne funkcje. R1b nie uzasadnia automatycznie przeniesienia miary powłoki na dowolne skończone zliczenia kontaktów.

### 20.6. Co porządek niesienia daje w rekonstrukcji przyczynowej

§19.4 daje odpowiedź inkluzywną R_ℓk=0 dla k>ℓ, komutator prądów dla k<ℓ oraz kontakt diagonalny dla k=ℓ. Ten wynik nie korzysta z obrotu Wicka ani z dodatniej reprezentacji propagatora z 263.

Dla stacjonarnej rodziny odczytów, gdy odpowiedź zależy od różnicy indeksów kontaktów j≥0, zbieżna funkcja H(z)=Σ_{j≥0}h_jz^j jest analityczna w swojej tarczy zbieżności. To bezpośredni odpowiednik rekonstrukcji analitycznej z porządku niesienia. **Przyczynowość sama nie utożsamia jednak z tej racji argumentu z z niezmiennikiem pary s ani z radarową rozdzielczością.** Potrzebne jest wskazane przyporządkowanie rodziny odczytu do tych argumentów; jak w §17, faza a nie staje się po prostu q/m.

Jeżeli z tego przyporządkowania otrzymano odpowiedź D(z) analityczną poza cięciem pary [4m²,∞), rzeczywistą pod sprzężeniem i z D(z)/z→0 na dużych konturach, to Cauchy dla raz odjętej funkcji daje

\[
D(z)-D(0)=\frac z\pi\int_{4m^2}^{\infty}
\frac{\operatorname{Im}D(s+i0)}{s(s-z)}\,ds.
\tag{20.20}
\]

Przy Im D(s+i0)=πρ̂(m²/s)/3, D(0)=0 oraz F(r)=−D(−m²r) jest to (20.5). Dodatniość ρ̂ jest normą wskazanego inkluzywnego kanału pary; nie zakładamy tu dodatniej reprezentacji spektralnej całego cechowanego propagatora.

**Kontakt pozostaje sprawdzalną swobodą.** Zmiana D(z)→D(z)+c z/m² dla rzeczywistego c zachowuje część absorpcyjną, D(0)=0 oraz przyczynową podporę (jest lokalną wstawką kontaktową). Zmienia F(r) o c r. Wyklucza ją warunek D(z)/z→0, a nie sam warunek „brak odpowiedzi przed kontaktem”. Także po wskazaniu całego ρ̂ trzeba więc uzasadnić zakres odejmowań i usunięcie pozostałych kontaktów. W §19 istnieje ich jawne miejsce: druga wariacja Ξ_ℓ tego samego kontaktu.

### 20.7. Wybór prądu: γ jest przekładalne, ale swoboda poprzeczna pozostaje

Ogólny zachowany prąd wektorowy kanału spin½, przy standardowym parzystym odczycie, można zapisać dwoma funkcjami:

\[
\Gamma^\mu=F_1(s)\gamma^\mu
+\frac{iF_2(s)}{2m}\sigma^{\mu\nu}q_\nu,
\qquad \tau=\frac{s}{4m^2}=\frac{E^2}{m^2}.
\tag{20.21}
\]

Jest to porównawczy zapis mapy między spinorami i wektorem; γ składa się z macierzy użytych w §20.3. Drugi składnik jest poprzeczny: q_μσ^{μν}q_ν=0. Tożsamość transportu faz nie wyznacza przez to F₂. Relacja z obiegiem F już występuje w R1d; samo pole jako koneksja nie jest dowodem zerowania wszystkich jej spinowych odczytów. Warunki hermitowskości i wspólnego ładunku także nie zastępują tego dowodu.

Ten sam rachunek 2×2, bez zmiany A,B i masy, daje

\[
M_i=F_1(A\sigma_iB+B\sigma_iA)
+F_2\frac Em(A\sigma_iA+B\sigma_iB).
\tag{20.22}
\]

Zatem

\[
G_M=F_1+F_2,\qquad G_E=F_1+\tau F_2,
\qquad
\widehat\rho=\beta\left[|G_M|^2+\frac{m^2}{2E^2}|G_E|^2\right].
\tag{20.23}
\]

Cel odpowiada F₁=1, F₂=0 w tym rzędzie. Postać dwóch funkcji i ich wag skontrolowano także wobec Chen–Yan–Xie, Chin. Phys. C 49 (2025) 023102, równania (2)–(5), (9). Ten artykuł stosuje ją do baryonu; nie przenosimy modelu baryonowego ani poprawek końcowych na elektron. Algebra map spin½ i wektora jest przedmiotem porównania.

**Dokładna diagnostyka limitów i dodatniości.** Tylko na fizycznym przedziale t∈[0,1/4] bierzemy rodzinę testową

\[
F_1=1,\quad F_2=16\lambda t^2(1-4t),
\quad G_M=1+16\lambda t^2(1-4t),
\quad G_E=1+4\lambda t(1-4t).
\tag{20.24}
\]

Przy t=0 i t=1/4 ma te same odpowiednie limity co cel: ρ̂→1 przy dużej rozdzielczości, brak wagi podłużnej przy m/E→0 i izotropowy prąd na progu. Daje ten sam μ₀=1/3. Natomiast

\[
\mu_1(\lambda)=\frac1{15}+\frac{4\lambda}{315}
+\frac{124\lambda^2}{135135}.
\tag{20.25}
\]

Dla λ=1/100 jest to 3223633/48262500≠1/15. Również dodatnia miara −dρ̂/3 zostaje zachowana: po x=4t licznik jej gęstości ma postać xQ(x), a Q ma sześć ściśle dodatnich współczynników Bernsteina na [0,1], wypisanych w kontroli. Zatem dodatniość, oba limity i pierwszy współczynnik logarytmu nie wybierają kształtu celu.

**Zakres diagnostyki jest istotny:** λ nie jest proponowanym nowym sprzężeniem fizycznym. Nie skonstruowano całej relacji kontaktów, jej stanu i analitycznego przedłużenia spełniającego wszystkie przesłanki ramy. To nie kontrmodel całej ramy. Rachunek wykazuje niewystarczalność wymienionych warunków na prąd, miarę i limity do wyboru całego progu; dla mocniejszego zdania nadal potrzebny jest test 128. Nie wystarczy nazwać odmienny składnik „dołożonym”: trzeba wskazać konkretną relację ramy, którą narusza.

### 20.8. Werdykt i dokładne następne zadanie

| część | uzyskano | co pozostaje do przyporządkowania |
|---|---|---|
| Ogon miary / momenty | Dokładna tożsamość z wagą pary 255/261; μ₀…μ₉ | Nie wymaga nowego działania ani traktowania x(1−x) jak obiektu |
| (c), punktowy prąd | 1,1,(m/E)² z A,B i σ_i; γ przekładalne na tę algebrę | Wybór punktowego prądu w tym rzędzie: F₁=1, F₂=0 oraz inkluzywnego odczytu |
| (b), kanał pary | β ze standardowej niezmienniczej miary pełnej swobodnej pary | Przekład rzeczywistych zliczeń/kanałów na tę miarę; sam det P nie jest jej wagą |
| (a), porządek niesienia | Brak wpływu późniejszych kontaktów i warunkowa analityczna rekonstrukcja | Rodzina argumentów, stan zapewniający wskazaną stacjonarność/niezmienniczość, wzrost i kontakty/odejmowania |
| Kontrola bez spinu | β³/4 dokładnie | Ten wynik dotyczy wskazanego punktowego skalarnego prądu |

Nowa droga usuwa z §19 zbyt szerokie odczytanie przeszkody: **nie trzeba odtworzyć wszystkich neutralnych amplitud i całego działania, aby obliczyć ten wydzielony próg.** Potrzebne jest przyporządkowanie konkretnego prądu pary, jego pełnego kanału i rekonstrukcji do relacji ramy. §19 zachowuje swój wynik o ogólnej gaussowskiej rodzinie; nie stanowi dowodu konieczności tamtej metody dla F_γ.

Najbliższe zadanie jest węższe niż poprzednio: zastosować test 128 do odczytu EM pojedynczego kanału L/R — **czy jego reguła kontaktu w badanym rzędzie wymusza prąd (20.10), a wyklucza niezależne wstawki poprzeczne i czynniki formujące (20.21)**. Trzeba wykorzystać pełną regułę kontaktu/transportu i obiegi R1d, nie same limity β. Następnie osobno rozliczyć miarę pełnego kanału oraz kontakt Ξ w odczycie przyczynowym. Nie wracamy do ustanawiania czasu, 3D ani autonomii dynamiki.

### 20.9. Kontrole i odtwarzalność

Skrypt `check_step20.py` wykonał 244 dokładne tożsamości skalarne po rozwinięciu macierzy, w tym 108 elementów tensorów prądu przy 12 kombinacjach masowej relacji i obrotu. Sprawdził dokładnie momenty μ₀…μ₉, rozkład prądu z obiema funkcjami formującymi, kontrolę skalarną oraz dodatni certyfikat miary diagnostycznej. Cztery niezależne postacie całkowe porównano przy 80 cyfrach dla r=0,01; 0,1; 1; 4; 10; 100; 1000; maksymalna różnica w tym obliczeniu wyniosła 2,11·10⁻⁸¹. Dowodami tożsamości są równania wyżej; te kontrole nie dowodzą wyboru prądu i miary z ramy ani całego twierdzenia użytkownika.

Źródła zakresu: R1b, R1c, R1d, R1f-3 oraz 155, 212, 255, 257, 260–263 pliku głównego; §§19.4–19.8 niniejszego raportu. Literatura kontrolna: [Chen–Yan–Xie, prąd i dwie funkcje formujące](https://csnsdoc.ihep.ac.cn/article/doi/10.1088/1674-1137/ad9259), [CLEO, skalarna produkcja pary, (2)](https://arxiv.org/pdf/hep-ex/0510005), [PDG 2025, kinematyka, (49.11–49.18)](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-kinematics.pdf). Literatura służy kontroli algebraicznych postaci i ich przekładu.

### 20.10. Pełny skrypt kontrolny

Python 3; wymagane pakiety `sympy` i `mpmath`.

```python
"""Threshold representation audit; conditional current/measure, no frame-only claim."""
from pathlib import Path
import json
import sys
sys.path.insert(0, str(Path(__file__).parent / 'deps'))
import mpmath as mp
import sympy as sp

checks = {}
exact_count = 0


def exact(label, expression):
    global exact_count
    value = sp.simplify(expression)
    assert value == 0, (label, value)
    exact_count += 1


def exact_matrix(label, expression):
    for entry in expression:
        exact(label, entry)


t, r, c, beta = sp.symbols('t r c beta', real=True)
rho = sp.sqrt(1-4*t)*(1+2*t)
tail = rho/3
exact('tail derivative', sp.diff(tail, t)+4*t/sp.sqrt(1-4*t))
exact('tail at zero', tail.subs(t, 0)-sp.Rational(1, 3))
exact('tail at threshold', tail.subs(t, sp.Rational(1, 4)))


def beta_integral(n, exponent):
    return sp.simplify(sp.gamma(n+1)*sp.gamma(exponent+1)
                       /sp.gamma(n+exponent+2)/4**(n+1))


moments = []
for k in range(10):
    value = 4*beta_integral(k+1, sp.Rational(-1, 2))
    target = 2*sp.factorial(k+1)**2/sp.factorial(2*k+3)
    exact('moment', value-target)
    if k:
        from_tail = sp.Rational(k, 3)*(beta_integral(k-1, sp.Rational(1, 2))
                                      +2*beta_integral(k, sp.Rational(1, 2)))
        exact('tail moment', value-from_tail)
    moments.append(str(value))

angular = (1+c)**2+(1-c)**2+2*(1-beta**2)*(1-c**2)
angular_ratio = sp.integrate(angular, (c, -1, 1))/sp.Rational(16, 3)
exact('angular average ratio', angular_ratio-(3-beta**2)/2)

sigma = [sp.Matrix([[0, 1], [1, 0]]),
         sp.Matrix([[0, -sp.I], [sp.I, 0]]),
         sp.diag(1, -1)]
eye = sp.eye(2)
a, b = sp.symbols('a b', positive=True)
E = (a*a+b*b)/2
p = (a*a-b*b)/2
m = a*b
A, B = sp.diag(a, b), sp.diag(b, a)
exact_matrix('mass closure', A*B-m*eye)
exact('shell determinant', E*E-p*p-m*m)
exact_matrix('normalization', A*A+B*B-2*E*eye)
pair_current = [A*s*B+B*s*A for s in sigma]
for i in range(3):
    expected = 2*(E if i < 2 else m)*sigma[i]
    exact_matrix('current without gamma notation', pair_current[i]-expected)
    weight = sp.trace(pair_current[i]*pair_current[i].conjugate().T)
    exact('spin sum', weight-8*(E*E if i < 2 else m*m))
exact_matrix('time component zero', A*B-B*A)

# The two Weyl blocks solve the canonical free mass relation.
U = B.col_join(A)
V = A.col_join(-B)
Pplus, Pminus = A*A, B*B
Kp = (-m*eye).row_join(Pminus).col_join(Pplus.row_join(-m*eye))
Kanti = (m*eye).row_join(Pplus).col_join(Pminus.row_join(m*eye))
exact_matrix('particle mass relation', Kp*U)
exact_matrix('antiparticle mass relation', Kanti*V)

# Exact arbitrary-direction check: tensor, not just its angular integral.
rotations = [eye, sp.Rational(3, 5)*eye+sp.I*sp.Rational(4, 5)*sigma[1],
             (eye+sp.I*(sigma[0]+sigma[1]+sigma[2]))/2]
tensor_entries = 0
for av, bv in [(1, 1), (2, 1), (3, 2), (5, 1)]:
    ev, pv, mv = E.subs({a: av, b: bv}), p.subs({a: av, b: bv}), av*bv
    for rotation in rotations:
        exact_matrix('rotation unitary', rotation*rotation.conjugate().T-eye)
        Ar = rotation*A.subs({a: av, b: bv})*rotation.conjugate().T
        Br = rotation*B.subs({a: av, b: bv})*rotation.conjugate().T
        direction = rotation*sigma[2]*rotation.conjugate().T
        n = [sp.trace(direction*s)/2 for s in sigma]
        js = [Ar*s*Br+Br*s*Ar for s in sigma]
        for i in range(3):
            for j in range(3):
                actual = sp.trace(js[i]*js[j].conjugate().T)
                expected = 8*(ev*ev*int(i == j)-pv*pv*n[i]*n[j])
                exact('rotated pair tensor', actual-expected)
                tensor_entries += 1

# General on-shell transverse current has two form factors.
f1, f2 = sp.symbols('f1 f2', real=True)
for i in range(3):
    Ji = f1*pair_current[i]+f2*(E/m)*(A*sigma[i]*A+B*sigma[i]*B)
    expected = 2*E*(f1+f2)*sigma[i] if i < 2 else 2*m*(f1+E*E/(m*m)*f2)*sigma[i]
    exact_matrix('Dirac and Pauli weights', Ji-expected)

# Equal EM charges commute with the zigzag mass generator.
qL, qR, theta = sp.symbols('qL qR theta', real=True)
hm = sp.Matrix([[0, theta], [theta, 0]])
Q = sp.diag(qL, qR)
exact_matrix('equal charge mass commutator', (Q*hm-hm*Q).subs(qR, qL))

# Scalar charge current, normalized to the same massless fermion channel.
scalar = 4*beta**2*(1-c*c)
fermion_reference = 8*(1+c*c)
scalar_ratio = beta*sp.integrate(scalar, (c, -1, 1))/sp.integrate(fermion_reference, (c, -1, 1))
exact('negative spin control', scalar_ratio-beta**3/4)

# The standard invariant product shell measure gives p^(d-2)/E.
# Its equal-total-energy ratio to m=0 is beta^(d-2), not its absolute scale.
d = sp.symbols('d', integer=True, positive=True)
phase_measure = p**(d-1)/(4*E*E)/(2*p/E)
exact('shell radial Jacobian', phase_measure-p**(d-2)/(8*E))

# Diagnostic family on the physical timelike interval only.
# It is NOT asserted to be a full model of the frame or a physical new coupling.
lam = sp.symbols('lambda', real=True)
F2 = 16*lam*t*t*(1-4*t)
GM = 1+F2
GE = 1+4*lam*t*(1-4*t)
poly = sp.expand(GM**2+2*t*GE**2)
rho_lam = sp.sqrt(1-4*t)*poly
exact('same UV endpoint', rho_lam.subs(t, 0)-1)
exact('same threshold currents GM', GM.subs(t, sp.Rational(1, 4))-1)
exact('same threshold currents GE', GE.subs(t, sp.Rational(1, 4))-1)
mu1_lam = sp.simplify(sum(coeff*beta_integral(power[0], sp.Rational(1, 2))/3
                          for power, coeff in sp.Poly(poly, t).terms()))
assert sp.simplify(mu1_lam-sp.Rational(1, 15)) != 0
diagnostic = {
    'F2_on_physical_interval': str(F2),
    'mu0': '1/3',
    'mu1': str(mu1_lam),
    'mu1_at_lambda_1_over_100': str(mu1_lam.subs(lam, sp.Rational(1, 100))),
    'scope': 'nonuniqueness of the specified current/kinematics/endpoints only; not a countermodel of the complete frame'
}

# Positivity of the diagnostic logarithmic measure is an exact inequality,
# certified by positive Bernstein coefficients on x=4t in [0,1].
x = sp.symbols('x', real=True)
poly_x = sp.expand(poly.subs({t: x/4, lam: sp.Rational(1, 100)}))
derivative_numerator = sp.expand(2*poly_x-4*(1-x)*sp.diff(poly_x, x))
positive_polynomial = sp.Poly(sp.cancel(derivative_numerator/x), x)
degree = positive_polynomial.degree()
bernstein = [sp.simplify(sum(positive_polynomial.nth(k)*sp.binomial(j,k)/sp.binomial(degree,k)
                            for k in range(j+1))) for j in range(degree+1)]
assert all(v > 0 for v in bernstein)
diagnostic['positive_measure_at_lambda_1_over_100'] = True
diagnostic['Bernstein_certificate'] = [str(v) for v in bernstein]

mp.mp.dps = 80
max_error = mp.mpf('0')
integrals = []
for value in ['0.01', '0.1', '1', '4', '10', '100', '1000']:
    rv = mp.mpf(value)
    feynman = 2*mp.quad(lambda x: x*(1-x)*mp.log1p(rv*x*(1-x)), [0, mp.mpf('.5'), 1])
    measure = mp.quad(lambda v: (1-v*v)/2*mp.log1p(rv*(1-v*v)/4), [0, 1])
    threshold = rv/3*mp.quad(lambda v: v*v*(3-v*v)/(4+rv*(1-v*v)), [0, 1])
    dispersion = rv/3*mp.quad(lambda sv: mp.sqrt(1-4/sv)*(1+2/sv)/(sv*(sv+rv)), [4, 8, 32, 128, mp.inf])
    error = max(abs(feynman-x) for x in [measure, threshold, dispersion])
    assert error < mp.mpf('1e-70'), (value, error)
    max_error = max(max_error, error)
    integrals.append({'r': value, 'F_gamma': mp.nstr(feynman, 35), 'max_error': mp.nstr(error, 8)})

output = {
    'status': 'PASS', 'exact_scalar_identities': exact_count,
    'rotated_spin_tensor_entries': tensor_entries, 'moments_mu_0_through_9': moments,
    'high_precision_digits': mp.mp.dps, 'max_integral_error': mp.nstr(max_error, 10),
    'four_representations': integrals, 'scalar_negative_control': 'beta^3/4',
    'current_diagnostic': diagnostic,
    'scope': 'algebra and conditional invariant phase-space/current reconstruction; causality assumptions and frame sufficiency require separate arguments'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(output, ensure_ascii=False, indent=2))
```

### 20.11. Wynik kontroli

```json
{
  "status": "PASS",
  "exact_scalar_identities": 244,
  "rotated_spin_tensor_entries": 108,
  "moments_mu_0_through_9": [
    "1/3",
    "1/15",
    "1/70",
    "1/315",
    "1/1386",
    "1/6006",
    "1/25740",
    "1/109395",
    "1/461890",
    "1/1939938"
  ],
  "high_precision_digits": 80,
  "max_integral_error": "2.108439589e-81",
  "four_representations": [
    {
      "r": "0.01",
      "F_gamma": "0.00066595343735301089104270903116556645",
      "max_error": "0.0"
    },
    {
      "r": "0.1",
      "F_gamma": "0.0065962785854315234666542940203596379",
      "max_error": "8.2360921e-84"
    },
    {
      "r": "1",
      "F_gamma": "0.060429542837771046295389056193435402",
      "max_error": "1.3177747e-81"
    },
    {
      "r": "4",
      "F_gamma": "0.19326127120459812004045783127815645",
      "max_error": "2.6355495e-82"
    },
    {
      "r": "10",
      "F_gamma": "0.35961177361937906861053305551233299",
      "max_error": "0.0"
    },
    {
      "r": "100",
      "F_gamma": "0.99849042599208434981476075550891209",
      "max_error": "1.0542198e-81"
    },
    {
      "r": "1000",
      "F_gamma": "1.7490147385349823193493969021709939",
      "max_error": "2.1084396e-81"
    }
  ],
  "scalar_negative_control": "beta^3/4",
  "current_diagnostic": {
    "F2_on_physical_interval": "16*lambda*t**2*(1 - 4*t)",
    "mu0": "1/3",
    "mu1": "124*lambda**2/135135 + 4*lambda/315 + 1/15",
    "mu1_at_lambda_1_over_100": "3223633/48262500",
    "scope": "nonuniqueness of the specified current/kinematics/endpoints only; not a countermodel of the complete frame",
    "positive_measure_at_lambda_1_over_100": true,
    "Bernstein_certificate": [
      "69/25",
      "72297/25000",
      "298183/100000",
      "60603/20000",
      "759/250",
      "3"
    ]
  },
  "scope": "algebra and conditional invariant phase-space/current reconstruction; causality assumptions and frame sufficiency require separate arguments"
}
```

## 21. Źródła


1. A. Kamenev, A. Levchenko, *Keldysh technique and non-linear sigma-model: basic principles and applications*, [arXiv:0901.3586](https://arxiv.org/abs/0901.3586), §§1.2, 2.1–2.3, 5.1–5.4. Narzędzie pełnego porównania i normowania; nie przenosimy do projektu zewnętrznego czasu ani modeli materii skondensowanej z dalszych części pracy.
2. G. Chiribella, G. M. D'Ariano, P. Perinotti, *Theoretical framework for quantum networks*, [arXiv:0904.4483](https://arxiv.org/abs/0904.4483). Sieci z przygotowaniami, pamięcią i instrumentami; pozycja wskazana już w 179.
3. Źródła projektu: regula-kompozycji-pelnego-odczytu-2026-10-12.md; logika-relacyjna-v3.5.md, 257–263; pary-M-O-EM-2026-10-05.md; LR-odczyt-A-dopasowanie-2026-10-04.md. Wyprowadzenia i kontrola obecnej kontynuacji opisane w §§6–10.
4. N. Aronszajn, *Theory of Reproducing Kernels*, Trans. Amer. Math. Soc. 68 (1950), 337–404, [wydawca AMS](https://www.ams.org/tran/1950-068-03/S0002-9947-1950-0051437-7/S0002-9947-1950-0051437-7.pdf). Odniesienie dla konstrukcji z dodatniego jądra; zastosowanie do przygotowań i efektów podano jawnie w §6. Nie przypisuje się publikacji tez o podstawie projektu.
5. M. Griesemer, D. Hasler, *On the Smooth Feshbach-Schur Map*, [arXiv:0704.3244](https://arxiv.org/abs/0704.3244), §1. Znane narzędzie eliminacji bloków. Kryterium wielomianowości w §8 oraz wariant rodzinny w §9 wyprowadzono tutaj; nie zgłasza się ich jako nowości wobec całej literatury.
6. Wcześniejsze pełne raporty: jadro-z-relacji-2026-10-09.md, §5; sprzezenie-i-normalizacja-odczytu-2026-10-09.md, §§1–4; wybor-jadra-LR-2026-10-09.md, zwłaszcza §§1, 3, 8–9. Obecny wynik precyzuje test pamięci pozostawiony otwarty w 263. Nie zmienia masowego dopasowania 262.

7. M. Vettorazzo, P. de Forcrand, *Electromagnetic fluxes, monopoles, and the order of the 4d compact U(1) phase transition*, [arXiv:hep-lat/0311006](https://arxiv.org/abs/hep-lat/0311006), §7.2, równania (46)–(49). Kontrola związku kwadratowej odpowiedzi fazowej ze sprzężeniem i znaczenia normalizacji; nie źródło podstawy relacyjnej ani operatora kontaktu tego projektu.

8. A. Grozin, *Lectures on QED and QCD*, [arXiv:hep-ph/0508242](https://arxiv.org/abs/hep-ph/0508242), §§3.2–3.4, w szczególności (3.14)–(3.15), (3.18)–(3.25). Kontrola rozdzielenia poprzeczności wynikającej z cechowania i obliczenia konkretnej fermionowej pętli. Nie jest dowodem pochodzenia operatora kontaktu z ramy.

9. S. Bravyi, *Lagrangian representation for fermionic linear optics*, [arXiv:quant-ph/0404180](https://arxiv.org/abs/quant-ph/0404180), §§II, IV, wzory (4)–(5), (17). Kontrola związku kwadratowych operatorów z liniowym transportem generatorów CAR oraz rozkładu Wicka. Nie źródło tez relacyjnych projektu.

10. D. J. Brod, E. F. Galvão, *Extending matchgates into universal quantum computation*, [arXiv:1106.1863](https://arxiv.org/abs/1106.1863), §II A i przypis 24. Kontrola rozróżnienia dowolnej unitarnej relacji zachowującej parzystość od podklasy z równymi wyznacznikami bloków. W §15 użyto tylko kryterium algebraicznego, bez przenoszenia modeli komputerów kwantowych do ramy.

11. I. Klich, *Full Counting Statistics: An elementary derivation of Levitov’s formula*, [arXiv:cond-mat/0209642](https://arxiv.org/abs/cond-mat/0209642), §2, wzory (8)–(12). Tożsamość śladu fermionowego i wyznacznika oraz reprezentacja algebry operatorów bilinearnych. §16 stosuje te tożsamości do pełnego przygotowania, obu gałęzi kontaktów i efektu; nie przenosi do ramy rezerwuarów ani zegara z zastosowania w publikacji.
