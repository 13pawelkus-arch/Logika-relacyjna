# Porównania, amplitudy i wagi w funkcjach masy

Notatka robocza, 4 października 2026. Kontynuacja analizy współzależności funkcji. Pytanie: które porównania, amplitudy i wagi odczytu odpowiadają poszczególnym składnikom funkcji masy?

Zakres: przyporządkowanie w istniejącym formalizmie QM i Modelu Standardowego, jedna pętla, bez neutrinowych Yukaw i bez przekraczania progów. Rachunek nie wybiera wartości mas, sprzężeń ani CKM. Zamknięcia 198–202, 206 i 207 pozostają przesłankami; rozstrzygnięcia 166 i 208 obowiązują. Typ A i typ B odczytu pozostają rozdzielone.

Rozróżniamy: (1) algebraiczne konsekwencje porównań i QM, (2) przyporządkowanie operatorom użytym w rachunku SM, (3) otwarte wyprowadzenie tego przyporządkowania z podstawy relacyjnej. Poprawność punktu (2) nie zastępuje punktu (3). Macierze wewnętrznych kanałów nie są wymiarami przestrzennymi.

## Zapisy przed rachunkami

**M0 — amplitudy i ich powroty.** Spodziewam się: dla zredukowanego operatora amplitud Y, jego kolumny R_a=Y e_a mają macierz porównań X=Y†Y; przekątna sumuje moduły amplitud do wspólnych kanałów wyjściowych, a elementy poza przekątną porównują te amplitudy koherentnie. Zdanie o upadku: utożsamienie z X upada, jeżeli pomiędzy przejściami pozostaje zależny od kanału propagator lub inna metryka odczytu, której nie oddzielono. To nie jest ogólne utożsamienie dowolnego odczytu z Yukawą.

**M1 — siła odpowiedzi a znormalizowane nakładanie.** Spodziewam się: znormalizowana macierz nakładań kolumn nie ustala ich norm ani stosunków wartości singularnych. Zdanie o upadku: przykład odpada, jeśli dwa operatory o tym samym znormalizowanym Gramie muszą mieć te same stosunki wartości singularnych. Przed kontrolą wybieram Y1=diag(1,2,3), Y2=diag(1,3,5). To operatory syntetyczne do kontroli logicznej, nie masy ani model fizyczny.

**M2 — wagi mieszania.** Spodziewam się: dla X_u i X_d działających na wspólnej przestrzeni lewych kanałów, porównanie ich baz własnych daje V_ij=<u_i|d_j>, a odpowiedź X_d w kanale u_i wynosi sum_j y_dj²·|V_ij|². Wagi są kwadratami modułów amplitud i sumują się do jedności przy pełnych bazach. Zdanie o upadku: wniosek upada, jeśli rozkład spektralny daje inne wagi lub jeśli nie ma wspólnej przestrzeni porównań. Rozmiar macierzy nie jest przestrzennym 3D.

**M3 — zmiany sił odpowiedzi.** Spodziewam się: z równania 16π² Y′=Y B, przy hermitowskim B, wynika 16π² (ln y_i)′=<i|B|i>, dla dodatnich, prostych wartości singularnych. Człony krzyżowe Yukaw otrzymają wagi z M2, bez przybliżenia dominacji topu. Zdanie o upadku: wynik upada, jeśli pochodna wartości własnej X=Y†Y ma dodatkowy nieusuwalny człon od zmiany bazy albo nie zgadza się z rzutem B. Przy degeneracji należy użyć projektorów podprzestrzeni, a logarytm nie jest określony dla y_i=0.

**M4 — pochodzenie 3/2.** Spodziewam się: znane jednopętlowe wkłady Yukaw do zmian dwóch propagatorów i pełnego wierzchołka rozdzielą 3/2(X_u−X_d) na wkład wspólnego lewego kanału, prawego kanału i poprawkę wierzchołkową. Zdanie o upadku: rozdzielenie upada, jeśli po uzgodnieniu konwencji suma tych wkładów nie odtwarza pełnej beta-funkcji. Wkład wierzchołkowy zostanie tu wyznaczony jako różnica pełnego wyniku i znanych wkładów propagatorów; nie jest to niezależne obliczenie tego diagramu z podstawy relacyjnej.

**M5 — wagi cechowania.** Spodziewam się: suma kwadratów amplitud generatorów daje Casimir, a po przyjęciu jednopętlowego rachunku Yukaw suma wag lewego i prawego kanału daje współczynniki c_i z 152. Zdanie o upadku: mapowanie upada, jeśli operatory nie tworzą przyjętej reprezentacji albo suma norm nie daje jej Casimira. Czynnik 3 w c_i nie jest tu wyprowadzany z liczby kierunków.

**M6 — domknięcie na λ.** Spodziewam się: pełne jednopętlowe równanie λ używa tych samych macierzy poprzez Tr X_f oraz Tr X_f², z różnymi krotnościami i znakiem pętli fermionowej. Zdanie o upadku: przekład upada, jeśli po uwzględnieniu λ_źródła=2λ i g1_źródła²=(5/3)gY² nie otrzymamy konwencji pliku. Nie dokładamy μ² ani warunku zależnego od samego cięcia.

**M7 — stosunek całego zespołu.** Spodziewam się: wspólny człon T skróci się w stosunku Yukaw, lecz różnica wkładów własnych i mieszania pozostanie. Relacja między dwoma odczytami będzie iloczynem stosunków sprzężeń i czynnika z całki różnic Yukaw. Zdanie o upadku: postać upada, jeśli pochodna tak zapisanej relacji nie odtwarza pełnego równania stosunku w zadeklarowanym zakresie. Rozdzielczość s=ln(n0/n) nie jest czasem zewnętrznym.

**M8 — przejście B do A.** Spodziewam się: relacja mas A zawiera relację B oraz iloraz czynników przejścia między odczytami; wspólne v skraca się. Zdanie o upadku: skrócenie upada, jeśli czynniki są z różnych protokołów, schematów albo różnych odniesień. Sama tożsamość nie wyprowadza czynników przejścia. Nie rozszerzamy odczytu A leptonu na pojedynczy uwięziony kwark.

**Jawne dane syntetyczne do M2–M5, wybrane przed sprawdzeniem.** W standardowym zapisie unitarnym wybieram (c12,s12)=(3/5,4/5), (c23,s23)=(5/13,12/13), (c13,s13)=(15/17,8/17), δ=π/2. Dodatnie wartości singularne: u=(1/7,2/7,4/7), d=(1/9,2/9,5/9), e=(1/13,3/13,7/13). Sprzężenia kontrolne: gY=1/5, g2=1/4, g3=1/3. Przewidywanie: dokładna zgodność macierzowej i spektralnej postaci odpowiedzi, także po wspólnej zmianie bazy; zastąpienie |V|² przez V² ma ją złamać. Żadna liczba nie pochodzi z pomiaru.

## Źródła użyte do przyporządkowania

- Plik główny v3.5 (7): R1d–R1f; 177, 180–181 z ograniczeniem 194; 198–208; §F1, zwłaszcza 152–155, 166–167, 183.
- Luo–Xiao, [Two-loop Renormalization Group Equations in the Standard Model](https://arxiv.org/abs/hep-ph/0207271): działanie (1), jednopętlowe Yukawy (3)–(5), λ (9), definicje śladów. Używamy jednopętlowej części i jawnie przeliczamy konwencje.
- Jenkins–Manohar–Trott, [Renormalization Group Evolution of the Standard Model Dimension Six Operators II: Yukawa Dependence](https://arxiv.org/abs/1310.4838): wyłącznie zwykłe anomalne wymiary pól SM w (A.2). Operatory wymiaru sześć nie wchodzą do rachunku.
- Bednyakov–Pikelner–Velizhanin, [Three-loop SM beta-functions for matrix Yukawa couplings](https://arxiv.org/abs/1406.7171): (16)–(17), rozdzielenie renormalizacji propagatorów i wierzchołka oraz uwaga o zmianach bazy. Nie przenosimy trzech pętli do rachunku jednopętlowego.

## Wynik

Przyporządkowanie można ustalić dokładnie na poziomie istniejącego rachunku. Jego rdzeń to trzy różne operacje na amplitudach: **powrót do tego samego kanału, rzut na kanały drugiego odczytu oraz zamknięcie sumy po wszystkich kanałach**. Dają odpowiednio wkład własny Yukawy, wkład partnerów z wagami mieszania oraz wspólny ślad T. Wkłady cechowania są analogicznymi kontrakcjami amplitud generatorów.

Wynik nie utożsamia dowolnego zliczenia z Yukawą. Wskazuje dokładnie, jakiego rodzaju porównania musi odtworzyć przekład odczytu, aby zgadzał się z użytym formalizmem. Współczynniki działania są odczytem B z 166; przejście do A pozostaje osobnym, znanym w teorii rachunkiem.

### M0. Co reprezentuje amplitudę

W konwencji Luo–Xiao operator \(Y_u\) odwzorowuje lewy kanał kwarkowy na prawy kanał typu u; \(Y_d\) działa z tej samej lewej przestrzeni do prawego kanału typu d. \(Y_e\) działa analogicznie dla leptonów. Ich wspólne lewe przestrzenie wynikają z przyjętego działania SM, nie z liczby parametrów pojedynczego odczytu w 199.

Element \(A_{\alpha a}=(Y_f)_{\alpha a}\) jest **zredukowanym współczynnikiem amplitudy wierzchołka** wiążącego lewy i prawy kanał z H albo \(\widetilde H\). Nie jest samodzielnym prawdopodobieństwem. Pełna amplituda procesu zawiera również spinory, przygotowanie, propagatory, kinematykę i odpowiedź aparatu. Oddzielenie wspólnych czynników i kanoniczne unormowanie pól są częścią przyporządkowania modelowego.

Dla \(R_a=Y_f e_a\):

\[
(X_f)_{ab}=(Y_f^\dagger Y_f)_{ab}
=\sum_\alpha A_{\alpha a}^*A_{\alpha b}
=\langle R_a|R_b\rangle.
\]

- \((X_f)_{aa}\) sumuje kwadraty modułów odpowiedzi do wspólnych kanałów końcowych.
- \((X_f)_{ab}\), dla a≠b, porównuje odpowiedzi koherentnie przez te same kanały końcowe.
- Składanie L→R i R→L daje ten sam rodzaj kwadratowej kontrakcji. Kierunek składania i wspólna przestrzeń muszą pozostać jawne.

Przy pozostawionej metryce odczytu W dostajemy \(Y_f^\dagger W Y_f\), a przy propagatorze pośrednim P — \(Y_f^\dagger P Y_f\). W=P=𝟙 nie wynika z samego użycia jednego O. **To miejsce, w którym najłatwiej przemycić wspólność czynnika**, analogicznie do ograniczenia 180–181 w poprzedniej analizie.

**Status:** algebra QM oraz warunkowe przyporządkowanie zredukowanemu wierzchołkowi SM. Macierz Y opisuje relacje kanałów; nie przypisuje cech wnętrzu M.

### M1. Gdzie leży siła odpowiedzi, a gdzie znormalizowane nakładanie

Przy niezerowych kolumnach:

\[
I_a=\|R_a\|^2,\qquad
\kappa_{ab}=\frac{\langle R_a|R_b\rangle}{\sqrt{I_a I_b}},
\qquad
(X_f)_{ab}=\sqrt{I_a I_b}\,\kappa_{ab}.
\]

Wcześniejsza dodatniość Grama dotyczyła \(\kappa\), czyli **znormalizowanych porównań**. Tutaj X zawiera jeszcze **siły odpowiedzi** \(I_a\). Dla trzech kolumn \(\det X=I_1 I_2 I_3\det\kappa\). Dodatniość jest zachowana przy niezależnym dodatnim przeskalowaniu kolumn i nie ustala samych norm.

Wybrane wcześniej Y1 i Y2 mają tę samą znormalizowaną macierz Grama 𝟙, ale różne siły odpowiedzi oraz różne stosunki wartości singularnych. Kontrola przeszła.

Pierwiastki wartości własnych \(X_f\) oznaczamy \(y_{fi}\ge0\). W przyjętym modelu są to wartości singularne Yukawy. Przy wspólnym czynniku Higgsa stosunek odczytów B ma postać

\[
r^{B}_{fi,fj}=\frac{y_{fi}}{y_{fj}}.
\]

**Status:** ścisła algebra po przyjęciu reprezentacji amplitud przez Y. Znormalizowanego nakładania nie wolno zamienić w siłę odpowiedzi ani w stosunek mas bez tego przejścia. Kontrola nie wybiera żadnej hierarchii.

### M2. Dlaczego wkład partnera ma wagę \(|V_{ij}|^2\)

Niech \(u_i\) i \(d_j\) tworzą ortonormalne bazy odpowiedzi własnych \(X_u\) i \(X_d\) na wspólnej lewej przestrzeni:

\[
X_u=\sum_i y_{ui}^2|u_i\rangle\langle u_i|,\qquad
X_d=\sum_j y_{dj}^2|d_j\rangle\langle d_j|.
\]

Porównanie obu baz to amplituda

\[
V_{ij}=\langle u_i|d_j\rangle.
\]

W działaniu SM tak zdefiniowana niezgodność baz pojawia się w naładowanym prądzie słabym jako CKM. Rzut odpowiedzi partnera na kanał u_i daje

\[
\boxed{\langle u_i|X_d|u_i\rangle
=\sum_j y_{dj}^2|V_{ij}|^2.}
\]

Analogicznie:

\[
\langle d_j|X_u|d_j\rangle
=\sum_i y_{ui}^2|V_{ij}|^2.
\]

**Rozdzielenie amplitudy i wagi:** V jest amplitudą zmiany odniesienia; \(|V|^2\) jest jej wagą w takim rzucie; \(y^2\) jest siłą odpowiedzi partnera. Sama waga mieszania nie jest jego masą.

Unitarność pełnej zmiany bazy daje \(\sum_j|V_{ij}|^2=1\) i \(\sum_i|V_{ij}|^2=1\). W realnym procesie z W amplituda zawiera ponadto \(g_2/\sqrt2\) oraz czynniki spinowe i kinematyczne. Częstości surowych zdarzeń nie są automatycznie tymi wagami: dostępność kanałów, kinematyczne wagi procesów i odpowiedź detektora trzeba uwzględnić w danym porównaniu.

Fazy nie zostały usunięte. Produkty \(V_{ij}V_{kj}^*V_{kl}V_{il}^*\) mogą mieć niezerową część urojoną. Wybrana przed rachunkiem syntetyczna macierz ma taki produkt; nie jest to wniosek o zmierzonym CKM.

**Status:** kwadrat modułu wynika z rzutowania w QM. Istnienie dwóch wskazanych baz, ich wspólnej przestrzeni oraz przyporządkowanie prądowi W pochodzą z działania SM. Wyprowadzono rodzaj wagi, nie wartości CKM.

### M3. Pełne funkcje biegu bez przybliżenia dominacji topu

Stosujemy \(s=\ln(n_0/n)\), konwencję §F1 i hiperładunek \(g_Y\). Nie jest to argument czasu zewnętrznego. W jednej pętli:

\[
16\pi^2Y_u'=Y_uB_u,\qquad
B_u=T-G_u+\frac32(X_u-X_d),
\]
\[
16\pi^2Y_d'=Y_dB_d,\qquad
B_d=T-G_d+\frac32(X_d-X_u),
\]
\[
16\pi^2Y_e'=Y_eB_e,\qquad
B_e=T-G_e+\frac32X_e,
\]

gdzie skalary T i G mnożą macierz jednostkową,

\[
T=3\operatorname{Tr}X_u+3\operatorname{Tr}X_d+
\operatorname{Tr}X_e,\qquad
G_f=\sum_{a=Y,2,3}c_a(f)g_a^2.
\]

**Skąd pochodna wartości singularnej.** Z \(X=Y^\dagger Y\) i hermitowskiego B:

\[
16\pi^2X'=BX+XB.
\]

Dla prostej wartości własnej \(x_i=y_i^2>0\):

\[
16\pi^2 x_i'=2x_i\langle i|B|i\rangle,\qquad
\boxed{16\pi^2(\ln y_i)'=\langle i|B|i\rangle.}
\]

Różniczkowanie unormowania wektora własnego usuwa jego pochodną z pochodnej wartości własnej. Zmiana bazy nie jest dodatkową siłą. Przy degeneracji porównuje się projektory odpowiednich podprzestrzeni.

Po użyciu M2 otrzymujemy:

\[
\boxed{
16\pi^2(\ln y_{ui})'=T-G_u+
\frac32\left[y_{ui}^2-\sum_j|V_{ij}|^2y_{dj}^2\right],
}
\]
\[
\boxed{
16\pi^2(\ln y_{dj})'=T-G_d+
\frac32\left[y_{dj}^2-\sum_i|V_{ij}|^2y_{ui}^2\right],
}
\]
\[
\boxed{
16\pi^2(\ln y_{e\ell})'=T-G_e+\frac32y_{e\ell}^2.
}
\]

Nie ma tu liczby wybranej z tablic mas ani założenia \(|V_{tb}|^2=1\). Człon topu w kanale dolnym j to jeden składnik pełnej sumy:

\[
-\frac32\,y_t^2|V_{tj}|^2.
\]

Pozostałych składników nie wolno usunąć przed uzasadnieniem przybliżenia.

**Status:** pełny rzut znanych jednopętlowych równań SM na odpowiedzi własne. Co jest wyprowadzone w tej pracy: rzut i jego wagi. Co przyjęto ze źródła: działania pól, pełne beta-funkcje i współczynniki w nich.

### M4. Co dokładnie składa się na \(3/2\)

Zwykłe jednopętlowe wkłady Yukaw do anomalnych wymiarów pól, z (A.2) Jenkins–Manohar–Trott, zapisane bez wspólnego \(1/(16\pi^2)\):

\[
\gamma_Q^{(Y)}=\frac12(X_u+X_d),\quad
\gamma_{u_R}^{(Y)}=Y_uY_u^\dagger,\quad
\gamma_{d_R}^{(Y)}=Y_dY_d^\dagger,\quad
\gamma_H^{(Y)}=T.
\]

Dla leptonów \(\gamma_L^{(Y)}=X_e/2\), \(\gamma_{e_R}^{(Y)}=Y_eY_e^\dagger\). Użyte wzory dotyczą zwykłych pól SM. Nie wchodzą tu operatory rozszerzające działanie.

Wkłady propagatorów do zmiany wierzchołka u mają postać

\[
\gamma_{u_R}^{(Y)}Y_u+
Y_u\gamma_Q^{(Y)}+TY_u
=Y_u\left[\frac32X_u+\frac12X_d+T\right].
\]

Porównanie z pełnym wynikiem M3 pozostawia w poprawce wierzchołkowej

\[
Y_u(-2X_d).
\]

Dlatego na poziomie tych wkładów:

| Kanał odczytu u | Wkład po sprowadzeniu na wspólną lewą przestrzeń |
|---|---|
| Prawy propagator | \(+X_u\) |
| Wspólny lewy propagator | \(+\frac12X_u+\frac12X_d\) |
| Propagator Higgsa | \(+T\) |
| Poprawka wierzchołkowa, jako reszta | \(-2X_d\) |
| Suma zależna od Yukaw | \(+T+\frac32X_u-\frac32X_d\) |

Dla d role u i d zamieniają się. Dla leptonu, bez Yukawy neutrinowej, ta jednopętlowa reszta wierzchołkowa Yukaw jest zerowa, a dwie nogi dają \(X_e+X_e/2=3X_e/2\).

**Znaczenie:** \(3/2\) nie jest prawdopodobieństwem ani wagą CKM. Jest współczynnikiem zmiany amplitudy, złożonym z poprawek do propagatorów i wierzchołka. Ujemny wkład nie oznacza ujemnego prawdopodobieństwa. Nie wystarczy go nazwać „przeciwnym hiperładunkiem”, aby odtworzyć rachunek.

**Status:** rozdzielenie istniejącego wyniku na wskazane kanały renormalizacji. Wartości \(1/2\) i 1 pochodzą z obliczeń pól. Wartość −2 otrzymano tu przez odjęcie znanych wkładów od znanego pełnego wyniku — to kontrola i lokalizacja brakującego przejścia, a nie niezależne wyprowadzenie całego \(3/2\) z podstawy.

### M5. Te same amplitudy cechowania, dwa różne zliczenia

Po oddzieleniu wspólnych czynników procesowych zredukowana amplituda cechowania ma postać

\[
\mathcal A^A_{\beta\alpha}=g_a(t^A)_{\beta\alpha}.
\]

Są dwie różne kontrakcje tej samej tabeli amplitud:

**1. Przy ustalonym kanale nośnika, suma po wyjściach i generatorach:**

\[
\sum_{\beta,A}|\mathcal A^A_{\beta\alpha}|^2
=g_a^2 C_a(R).
\]

To Casimir \(C_a(R)\) dla przyjętej reprezentacji nieprzywiedlnej. Tę kontrakcję niosą wagi cechowania lewego i prawego kanału Yukawy:

\[
c_a(f)=3[C_a(L_f)+C_a(R_f)].
\]

**2. Przy ustalonych kanałach cechowania, suma po całej reprezentacji:**

\[
\sum_{\alpha,\beta}
(\mathcal A^A_{\beta\alpha})^*\mathcal A^B_{\beta\alpha}
=g_a^2T_a(R)\delta^{AB}.
\]

To indeks \(T_a(R)\), który wchodzi w zmianę sprzężenia \(b_a\). Różnica \(C(R)\) i \(T(R)\) jest różnicą tego, co ustalono jako odniesienie i po czym sumowano; nie są dwiema niezależnie dobranymi wagami.

Dla U(1) operatorem jest hiperładunek razy 𝟙. Dla przyjętych reprezentacji SM:

| Typ | \(c_Y\) | \(c_2\) | \(c_3\) | Rodzaj porównania |
|---|---:|---:|---:|---|
| u | \(17/12\) | \(9/4\) | 8 | Lewy i prawy kanał, oba z kolorem |
| d | \(5/12\) | \(9/4\) | 8 | Lewy i prawy kanał, oba z kolorem |
| e | \(15/4\) | \(9/4\) | 0 | Lewy i prawy kanał, bez koloru |

Ta tabela odtwarza 152. Nie jest nową predykcją. Przyjęto reprezentacje, hiperładunki oraz współczynnik jednopętlowej zmiany amplitudy. Fakt, że Casimir jest sumą kwadratów odpowiedzi, nie wyprowadza czynnika 3.

W \(b_a\) dochodzą wagi spinowe, statystyka i samooddziaływanie nośników relacji (155 A). To wkłady do odpowiedzi kwantowej i zmiany sprzężenia, nie dodatnie prawdopodobieństwa alternatyw. Znaku ekranowania lub antyekranowania nie można uzyskać przez samo policzenie dodatnich norm.

**Status:** kontrakcje amplitud wynikają z algebry przyjętej reprezentacji. Grupa, reprezentacje oraz pętlowe współczynniki pozostają osobno nazwanymi przesłankami.

### M6. Co wraca do funkcji λ

Wspólny ślad:

\[
T=\sum_{f=u,d,e}d_{\rm col}(f)\operatorname{Tr}X_f
=3\sum_i y_{ui}^2+3\sum_j y_{dj}^2+
\sum_\ell y_{e\ell}^2
\]

sumuje siły odpowiedzi wszystkich kanałów na wspólną relację Higgsa. Tutaj \(d_{\rm col}(f)=3\) dla sektorów kwarkowych oznacza krotność koloru, a nie liczbę kierunków ani liczbę pokoleń. Dla leptonów ta krotność wynosi 1. Wartości śladu nie wyprowadza samo jego istnienie.

Funkcja λ czyta również kontrakcję czwartego rzędu:

\[
\mathcal H_4=3\operatorname{Tr}X_u^2+
3\operatorname{Tr}X_d^2+\operatorname{Tr}X_e^2.
\]

Dla dowolnej bazy:

\[
\operatorname{Tr}X_f^2
=\sum_{a,b}|\langle R_a|R_b\rangle|^2
=\sum_i y_{fi}^4.
\]

To suma kwadratów porównań odpowiedzi, a nie kwadrat ich łącznej sumy. Zamiana \(\operatorname{Tr}X^2\) na \((\operatorname{Tr}X)^2\) dołożyłaby inne relacje.

Po uzgodnieniu konwencji Luo–Xiao z plikiem pełne równanie ma postać:

\[
16\pi^2\lambda'
=24\lambda^2+4\lambda T-2\mathcal H_4
-3\lambda(3g_2^2+g_Y^2)
+\frac38[2g_2^4+(g_2^2+g_Y^2)^2].
\]

Przy pozostawieniu tylko topu \(-2\mathcal H_4\) daje \(-6y_t^4\), jak 155 D. Nie przyjęto tu tego uproszczenia. Czynnik 3 jest krotnością koloru; znak minus pochodzi z pętli fermionowej. Konwersja wszystkich współczynników z λ_źródła=2λ i \(g_{1,\mathrm{źródła}}^2=(5/3)g_Y^2\) przeszła dokładnie.

**Status:** rachunek warunkowy istniejącego sektora Higgsa, z identyfikacją porównań czwartego rzędu. Przy jednej pętli λ nie pojawia się w M3: czyta Yukawy i cechowanie, ale jej bezpośredni wkład do ich beta-funkcji zaczyna się wyżej. Warunków z 154 i 208 nie rozszerzono na normy Y ani CKM.

### M7. Funkcja masy jako wspólna relacja tych odpowiedzi

Niech \(S_f\) oznacza odpowiedni nawias Yukaw z M3 wraz z czynnikiem \(3/2\). Wtedy

\[
16\pi^2(\ln y_f)'=T-G_f+S_f.
\]

Dla dwóch porównywalnych odczytów B:

\[
\boxed{
16\pi^2(\ln r_{fg}^B)'=
-\sum_a[c_a(f)-c_a(g)]g_a^2+
S_f-S_g.
}
\]

Wspólne T skraca się. W stosunku fizycznych współczynników masowych skraca się również wspólny czynnik v. Różnice wkładów własnych i rzutów na partnerów pozostają.

Dla dwóch kanałów dolnych j,k:

\[
16\pi^2\left(\ln\frac{y_{dj}}{y_{dk}}\right)'
=\frac32\left[
y_{dj}^2-y_{dk}^2-
\sum_i y_{ui}^2(|V_{ij}|^2-|V_{ik}|^2)
\right].
\]

Dla dwóch leptonów a,b, bez neutrinowych Yukaw:

\[
16\pi^2\left(\ln\frac{y_{ea}}{y_{eb}}\right)'
=\frac32(y_{ea}^2-y_{eb}^2).
\]

To pokazuje zakres „stoją” z 153: praktyczna małość zmian nie jest tożsamościowym zerem. Nie trzeba wstawiać danych, aby zobaczyć ten podział.

Z \(\alpha_a=g_a^2/(4\pi)\) i \(\alpha_a'=b_a\alpha_a^2/(2\pi)\) otrzymujemy \(p_a(f)=-c_a(f)/(2b_a)\). Dla niezerowych b_a i dodatnich skończonych sprzężeń, w jednym zakresie bez progów:

\[
\boxed{
\frac{r^B_{fg}(s_2)}{r^B_{fg}(s_1)}
=\prod_a\left[\frac{\alpha_a(s_2)}{\alpha_a(s_1)}\right]^{
p_a(f)-p_a(g)}
\exp\!\left[
\frac{1}{16\pi^2}\int_{s_1}^{s_2}(S_f-S_g)\,ds
\right].
}
\]

Całka zawiera te same y i V, których zmiany rozpatrujemy. Jest to zespół współzależny. Bez uzasadnionego uproszczenia nie wolno zamienić tej części w stały wykładnik ani usunąć mieszania.

**Status:** ścisłe przepisanie jednopętlowego zespołu. Nie dobiera funkcji do pomiarów i nie ustala wartości odniesienia. Konkretne p_a nadal mają pochodzenie modelowe.

### M8. Co trzeba uwzględnić, gdy pytamy o masę w sensie A

W 166 odczyt A jest samoodczytem fazy, a B jest współczynnikiem działania przy wspólnej rozdzielczości. W zadeklarowanym perturbacyjnym rachunku leptonów nazwijmy wynik przejścia

\[
\mathcal Z_f^{AB}(s)=
\frac{m_f^A}{y_f(s)v(s)/\sqrt2}.
\]

Wtedy:

\[
\boxed{
\frac{m_f^A}{m_g^A}
=\frac{y_f(s)}{y_g(s)}
\frac{\mathcal Z_f^{AB}(s)}{\mathcal Z_g^{AB}(s)}.
}
\]

Wspólne v wypada. \(\mathcal Z^{AB}\) jest nazwą wyniku przejścia, który liczy się z już obecnych oddziaływań i definicji odczytu; nie jest dodatkowym swobodnym sprzężeniem. Samo zapisanie ilorazu nie oblicza tego wyniku.

Przejście korzysta z pełnej funkcji dwupunktowej, poprawek do propagatora i uzgodnienia definicji pól. Dlatego względne poprawki EM z 166 są częścią relacji między odczytami. Nie wolno przenieść wzoru dla mas biegunowych leptonów na pojedynczy uwięziony kwark; B pozostaje tam właściwym obiektem zespołu.

**Status:** algebraiczne rozdzielenie A/B. Żadna nowa wartość masy ani warunek hierarchii nie został otrzymany.

## Mapa końcowa

| Składnik funkcji | Jakie porównanie wykonuje | Amplituda / waga | Co jest ustalone, a co warunkowe |
|---|---|---|---|
| Odczyt B \(y_f/y_g\) | Porównanie sił odpowiedzi własnych dwóch kanałów wobec wspólnego odniesienia | Pierwiastki wartości własnych \(Y^\dagger Y\); wspólny czynnik Higgsa wypada | Iloraz ścisły; reprezentacja przez Y pochodzi z modelu |
| Własny wkład Yukawy | Powrót przez własny kanał L↔R | \(y_f^2\), w biegu z wagą \(+3/2\) | Kwadratowa kontrakcja ścisła; \(3/2\) jest wynikiem pętlowym |
| Wkład partnerów u/d | Rzut odpowiedzi drugiego typu na bieżący kanał | \(\sum_j y_j^2|V_{ij}|^2\), w biegu z wagą \(-3/2\) | \(|V|^2\) wynika z rzutu; struktura wspólnej lewej przestrzeni i znak są modelowe |
| Wspólny T | Suma odpowiedzi wszystkich kanałów na wspólną relację Higgsa | \(\sum_f d_{\rm col}(f)\operatorname{Tr}Y_f^\dagger Y_f\) | Ślad niezależny od bazy; jego obecność i krotności wynikają z działania |
| Cechowanie w zmianie masy | Suma odpowiedzi na generatory przy ustalonym kanale nośnika, dla L i R | \(g_a^2C_a(R)\), łącznie \(c_a=3(C_L+C_R)\) | Kontrakcja ścisła w reprezentacji; grupa i czynnik pętlowy przyjęte |
| Bieg samego sprzężenia | Suma po nośnikach reprezentacji przy ustalonym kanale cechowania | \(T_a(R)\) ze śladu generatorów; dalej wagi spinowe i statystyczne | Inny rodzaj kontrakcji tej samej amplitudy; zawartość pól warunkowa |
| λ | Porównanie odpowiedzi na relację Higgsa, w tym zamknięcie czwartego rzędu | \(T\), \(\mathcal H_4\), kwadratowe produkty cechowania, samoczłon \(24\lambda^2\) | Zidentyfikowane składniki znanej beta-funkcji; nie nowy warunek na Y |
| Przejście do A | Porównanie samoodczytu fazy z odczytem współczynnika przy wspólnej rozdzielczości | \(\mathcal Z_f^{AB}/\mathcal Z_g^{AB}\) | Musi pochodzić z odpowiedniego rachunku propagatora; definicja nie zastępuje obliczenia |

## Związek z obiegami 177 i z wagą z 206

Amplitudy alternatyw składają się w QM przez kolejne operatory przejść. Ich odczyt zawiera kwadraty modułów i koherentne porównania par, jak w 177. W obecnym przyporządkowaniu amplitudy otrzymują indeksy kanałów i różne siły odpowiedzi. Zapis z jednostkowymi wagami każdej drogi jest szczególnym zakresem; nie odtwarza automatycznie Yukaw.

Kwadratowa kontrakcja L→R→L wskazuje miejsce formalizmu, w którym pojawia się odpowiedź proporcjonalna do \(Y^\dagger Y\). Jeżeli pozostaje propagator pośredni, jest to \(Y^\dagger P Y\), z jego własną wagą i z sumą po kanałach. **Nie otrzymano z tego uniwersalnej równości \(a\cdot b=-y_f^2\).** Skalarna suma po drogach z 180–181, operator Diraca i operator Yukawy muszą być połączone przy zachowaniu propagacji, indeksów i wspólnego odczytu. Wspólna postać dwóch zmian nie ustala normalizacji ani wag pośrednich.

206 zamyka rodzaj obiektu \(a\cdot b\): to odczyt układu relacji, nie parametr areny. Obecna mapa nie zmienia tego rozstrzygnięcia. Pokazuje, że przy odczycie wielokanałowym trzeba rozdzielić normę odpowiedzi, koherentne porównanie i krotność kanałów, zanim nazwie się wynik składnikiem funkcji masy.

## Co zostało zrobione, a jakie przejście pozostaje otwarte

**Zrobione:** wskazano operacje porównania odpowiadające składnikom funkcji; wyprowadzono wagi mieszania bez danych CKM; zidentyfikowano oddzielne role norm amplitud, Casimirów, indeksów i śladów; rozpisano cały jednopętlowy zespół bez przybliżenia dominacji topu; zlokalizowano \(3/2\) w poprawkach do propagatorów i wierzchołka; zachowano przejście A/B.

**Otwarte:** wyprowadzenie z 179–207 konkretnego zredukowanego wierzchołka, jego wspólnej metryki odczytu i propagacji pośredniej, tak aby uzyskać te same kontrakcje oraz współczynniki pętlowe bez przyjęcia ich jako dodatkowych przesłanek. Szczególnie wyraźne miejsce: czy odczyt odtwarza wkłady lewego propagatora, prawego propagatora i wierzchołka oddzielnie, których suma daje \(3/2\). Rzut i dodatniość same tego współczynnika nie ustalają.

To pytanie dotyczy przekładu struktury, nie poszukiwania zmierzonych wartości \(y_e\), CKM czy hierarchii. Nie dodano warunku ramy na odczyt, który według 208 nie jest samorelacją.

## Kontrola

Skrypt [sprawdzenie-mapy-masy-2026-10-04.py](sprawdzenie-mapy-masy-2026-10-04.py) wykonuje rachunek na dokładnych ułamkach i wymiernych liczbach zespolonych, bez bibliotek zewnętrznych. Przeszło 27 kontroli. Obejmują:

- dwie różne siły odpowiedzi przy tym samym Gramie znormalizowanym;
- rozkład spektralny z wagami \(|V|^2\), obie sumy unitarności oraz odrzucenie \(V^2\);
- dziewięć pochodnych logarytmicznych, również po wspólnej zmianie bazy u/d;
- reszty wierzchołkowe po odjęciu znanych wkładów propagatorów;
- Casimiry przyjętych reprezentacji i odtworzenie współczynników 152;
- przeliczenie konwencji λ i kontrakcję czwartego rzędu;
- pełne różnice stosunków oraz skrócenie wspólnej normalizacji A/B;
- kontrolę, że zależna od kanału metryka zmienia \(Y^\dagger Y\).

**Wynik autokontroli:** oczekiwania zachowane w zadeklarowanych zakresach; kontrole negatywne odrzuciły niewłaściwą wagę i pominiętą metrykę. Żaden pomiar nie wybrał struktury ani współczynnika. Wynik jest mapą działania istniejącego zespołu i wskazaniem dokładnego miejsca jego niewyprowadzonego jeszcze przekładu.
