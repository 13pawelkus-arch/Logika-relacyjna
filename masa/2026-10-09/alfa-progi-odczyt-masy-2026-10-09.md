# α z pełnymi progami: co można odczytać o masach

09.10.2026. Sprawdzenie §F0 pliku „logika-relacyjna-v3.5.md”, z poprawkami 251–253. Status: [A][T] dla konsekwencji podanego jądra, [L] dla użytych funkcji perturbacyjnych i relacji dyspersyjnej, [P] dla kontroli. Korzystamy z dopuszczenia danych pomiarowych przez użytkownika (253).

Otrzymano trzy wyniki: warunkowy test rozróżnienia mas z kształtu odpowiedzi α; jednoznaczność ważonego zbioru progów przy dokładnej funkcji w zadanej rodzinie; bezwymiarową postać wkładu hadronowego, z doprecyzowaniem jego normalizacji. Nie przeprowadzono analizy pomiarów α ani pełnego rachunku własnej energii w drugim rzędzie.

## 1. Co wynika z czterech części F0

| część F0 | co jest dostępne | co można dostać teraz |
|---|---|---|
| Co wiemy | pełne jednopętlowe jądro fermionowe, wagi ładunków, relacja rozdzielczości i wspólne amplitudy dla biegu sprzężenia oraz mas | dokładne zależności między kształtem odpowiedzi α a stosunkami mas |
| Czego nie wiemy | grupa i liczba pokoleń nie są wyprowadzone; wyższe rzędy i odpowiedź hadronowa nie są wyprowadzone z ramy | określić jawnie, które składniki są danymi rachunku; część hadronową zapisać przez znaną odpowiedź R |
| Do czego α jest potrzebna przy masie | przejście A/B i wagi cechowania są już nazwane i policzone w jednym rzędzie | sprawdzić, gdzie α niesie rozróżnienie mas, a gdzie wspólny wkład znosi się w stosunku |
| Proponowane kroki | najbliższy jest pełny próg; następne są dopasowanie opisów, drugi rząd i pochodzenie grupy | wykonać rachunek pełnego progu i część przeglądu rodzaju obiektu z 208; pozostałych kroków nie uznawać za wykonane |

Znana wartość α w jednym punkcie i niezależnie znany kształt funkcji α to różne zasoby informacji. Pierwsza pozwala obliczać poprawki w nazwanym rzędzie. Dopiero druga może dostarczyć danych o położeniu progów. Funkcja obliczona z zadanych mas nie jest niezależnym pomiarem pozwalającym później ogłosić te same masy jako wyprowadzone.

## 2. Oczekiwanie, zdanie o upadku, wejścia

**Spodziewam się:** pełna jednopętlowa odpowiedź fermionowa wyznacza ważony zbiór stosunków mas do rozdzielczości, z dokładnością do nierozróżnialności etykiet i sumowania wag przy zbieżnych progach.

**Zdanie o upadku:** istnieją dwa różne ważone zbiory dodatnich, skończonych progów, które przy tym samym jądrze dają dokładnie tę samą różnicę odwrotności α na całym otwartym przedziale rozdzielczości.

**Wejścia przed rachunkiem:**

- podana w F0 funkcja $F_\gamma$, w jednym rzędzie fermionowej polaryzacji próżni;
- skończona, niezerowa liczba kanałów i dodatnie wagi $c_f=N_cQ_f^2$;
- dodatnie, skończone odczyty mas $m_f$;
- wspólne odniesienie czytającego $q_*>0$, odpowiadające własnemu obiegowi z R1d;
- wydzielona odpowiedź fermionowa w jednym schemacie; pozostałe wkłady pozostają osobnymi częściami.

Masy są tu parametrami rodziny odpowiedzi. W zadaniu odwrotnym szukamy ich stosunków z danej odpowiedzi. Nie wprowadzamy wartości zmierzonych mas jako danych tego zadania. W kontrolach stosujemy jawnie syntetyczne wartości.

Odczytem jest porównanie własnych odpowiedzi O przy dwóch rozdzielczościach. Jednoznaczność parametrów tej rodziny nie oznacza odzyskania stanu M.

Zakres $F_\gamma$ to podany w F0 dodatni argument przestrzeniopodobnej odpowiedzi. Czasopodobne progi i część urojona wymagają kontynuacji tej odpowiedzi. Nie utożsamiamy efektywnej α z pełnym progiem z α zdefiniowaną przez sprzężenia MS-bar bez dopasowania. B z 152 i 217 oraz odpowiedź efektywna użyta poniżej muszą zostać uzgodnione przed ich wspólnym użyciem.

## 3. Pełny próg daje momenty stosunków mas

Wprowadźmy wyłącznie bezwymiarowe porównania:

$$
s=(q/q_*)^2,\qquad u_f=(q_*/m_f)^2,\qquad c_f=N_cQ_f^2>0.
$$

Niech $h=1/\alpha$. Dla samego wkładu fermionowego:

$$
g(s):=\pi[h(q_*)-h(q_*\sqrt{s})]_{\rm ferm}
=\sum_f c_f\{F_\gamma(su_f)-F_\gamma(u_f)\}.
$$

Stała odniesienia znika w pochodnych. Nie trzeba znać absolutnego przesunięcia $h$.

Z podanej całki, przy $|r|<4$, wynika:

$$
F_\gamma(r)=\sum_{k\ge1}(-1)^{k+1}a_kr^k,
\qquad
a_k=\frac{2}{k}\int_0^1[x(1-x)]^{k+1}dx
=\frac{2[(k+1)!]^2}{k(2k+3)!}.
$$

Pierwsze cztery współczynniki to $1/15,\ 1/140,\ 1/945,\ 1/5544$. Zatem, w otoczeniu $s=0$ z $|s|\max u_f<4$:

$$
g(s)=g(0)+\sum_{k\ge1}(-1)^{k+1}a_kp_ks^k,
\qquad p_k:=\sum_f c_fu_f^k.
$$

W szczególności:

$$
p_1=15g'(0),\quad p_2=-70g''(0),\quad
p_3=\frac{315}{2}g'''(0),\quad p_4=-231g^{(4)}(0).
$$

To momenty odwrotnych kwadratów mas względem tego samego odczytu $q_*$. Granica $s=0$ służy tu do określenia analitycznych współczynników funkcji; nie jest postulatem wykonania odczytu przy nieskończonym obiegu. Dokładna funkcja na przedziale wyznacza te współczynniki analitycznie, lecz skończone dane z niepewnościami nie dają ich automatycznie dokładnie.

Ważne: $p_k$ nie są surowymi współczynnikami Taylora α. Trzeba najpierw usunąć znane $a_k$ wspólnego jądra. Sam pojedynczy próg ma ciągłą wagę parametru $x$; dopiero po tej operacji otrzymujemy momenty dyskretnych $u_f$.

## 4. Dokładny test nierówności mas

Przy $p_0=\sum_f c_f$ i $p_1>0$ zachodzi:

$$
p_0p_2-p_1^2
=\sum_{f<j}c_fc_j(u_f-u_j)^2\ge0.
$$

Dowód: rozwinąć oba iloczyny, usunąć składniki diagonalne i połączyć pary $(f,j)$ oraz $(j,f)$. Dodatnie wagi dają:

$$
p_0p_2=p_1^2
\quad\Longleftrightarrow\quad
u_f=u_j\ \text{dla wszystkich kanałów}
\quad\Longleftrightarrow\quad m_f/m_j=1.
$$

Można użyć bezwymiarowej kombinacji:

$$
\mathcal V_\alpha:=\frac{p_0p_2}{p_1^2}-1
=\frac{\sum_{f<j}c_fc_j(u_f-u_j)^2}{p_1^2}.
$$

Zmiana wspólnego miejsca zapisu $q_*\mapsto bq_*$ daje $p_k\mapsto b^{2k}p_k$ i pozostawia $\mathcal V_\alpha$ bez zmiany. Nie jest to twierdzenie o dowolnej zmianie aparatu lub sprzężenia.

**Zysk:** w tej rodzinie odpowiedzi kształt α daje dokładny test zrównania mas; samo asymptotyczne nachylenie go nie daje. $\mathcal V_\alpha<0$ wyklucza opis otrzymanych danych przez tę rodzinę dodatnich fermionowych wkładów.

Dodatniość wynika tutaj z $c_f>0$ i podanego jądra. Nie zakładamy dodatniości operatora różnicy odczytów (213). Testu nie przenosimy na całkowitą α z wkładem W, częścią hadronową i wyższymi rzędami.

## 5. Czy różne masy mogą dać całą tę samą funkcję?

**Nie, dla ważonego zbioru progów w tej zadanej rodzinie [T].**

Różnica dwóch skończonych zbiorów progów jest skończoną miarą ze znakami, na różnych dodatnich punktach $v_1,\ldots,v_M$, z wagami $d_j$. Identyczność funkcji na otwartym przedziale, przez analityczność, daje identyczność wszystkich $p_k$:

$$
\sum_{j=1}^M d_jv_j^k=0,\qquad k=1,\ldots,M.
$$

Macierz tego układu to macierz Vandermonde'a pomnożona kolumnowo przez niezerowe $v_j$. Jest odwracalna, więc wszystkie $d_j=0$. Ważone zbiory są te same.

Granica wyniku: przy tym samym progu widoczna jest suma wag. Przy jednakowych wagach zamiana etykiet kanałów nie zmienia funkcji. Nie wyprowadzamy liczby pokoleń, nie odtwarzamy wszystkich własności nośnika i nie dowodzimy stabilnego odzyskania progów ze skończonych, zaszumionych pomiarów.

Algebra momentów dodatnich miar jest znana; przykładowo [McCullough, Ricci, Riembau, arXiv:2312.03834](https://arxiv.org/abs/2312.03834), §II, omawiają ograniczenia momentów polaryzacji próżni. Powyżej użyto jedynie podanego $F_\gamma$ i jawnego dowodu dla skończonego zbioru, bez przyjmowania dodatkowej dynamiki z tej pracy.

## 6. Trzy naładowane kanały leptonowe: odzyskanie i osobny test

Przyjęcie trzech kanałów $e,\mu,\tau$ z $c_f=1$ jest wejściem SM, nie wnioskiem z przestrzennego 3D.

Z pierwszych trzech momentów:

$$
e_1=p_1,\qquad
e_2=\frac{p_1^2-p_2}{2},\qquad
e_3=\frac{p_1^3-3p_1p_2+2p_3}{6}.
$$

Ich trzy dodatnie pierwiastki, z krotnościami, daje:

$$
P(z)=z^3-e_1z^2+e_2z-e_3=0.
$$

Są to $u_1,u_2,u_3$, a odczyty stosunków mas mają postać:

$$
m_i/m_j=\sqrt{u_j/u_i}.
$$

Jeżeli wielomian nie ma trzech dodatnich rzeczywistych pierwiastków, dane momentów nie należą do tej trzykanałowej rodziny. Ponadto kolejne momenty muszą spełniać:

$$
p_{k+3}=e_1p_{k+2}-e_2p_{k+1}+e_3p_k.
$$

**Pierwszy dodatkowy test** po odzyskaniu trzech progów:

$$
p_4=\frac{p_1^4-6p_1^2p_2+3p_2^2+8p_1p_3}{6}.
$$

To jest zależność do sprawdzania na danych, a nie dodatkowy parametr do dopasowania. Przechodzenie testów nie wybiera wartości mas bez danych o funkcji.

Dwa momenty nie wystarczą nawet przy trzech jednostkowych wagach. Zbiory $u=(1,2,3)$ oraz $u=(17/7,19/7,6/7)$ mają te same $p_1=6$ i $p_2=14$, lecz różne $p_3$: odpowiednio $36$ oraz $11988/343$. Mają zatem ten sam $\mathcal V_\alpha$, a różne stosunki mas.

Kontrola syntetyczna: dla $u=(1,1/4,1/9)$ wielomian odzyskał $m_f/q_*=(1,2,3)$; błąd numeryczny był mniejszy niż $4.5\cdot10^{-16}$. To sprawdzenie procedury na ustalonych wejściach, nie wynik dla zmierzonych leptonów.

## 7. Część hadronowa: pełna waga i poprawne odniesienie

Źródła użytej postaci: [Cè i in., arXiv:2203.08676](https://arxiv.org/abs/2203.08676), równania (2)–(4), oraz [Bernecker–Meyer, arXiv:1107.4388](https://arxiv.org/abs/1107.4388), równania (5), (10), (11). Bierzemy relację dyspersyjną; nie przenosimy ich interpretacji czasu ani konstrukcji kraty.

Dla dodatnich rozdzielczości $q_1,q_2$ definiujemy $\chi=(q_1/q_2)^2$, $v=(\omega/q_2)^2$. Niech $\widehat R(v;q_2)$ oznacza tę samą odpowiedź spektralną zapisaną względem $q_2$. Po odjęciu dwóch odczytów i przeskalowaniu całki:

$$
[h(q_1)-h(q_2)]_{\rm had}
=-\frac{\chi-1}{3\pi}
\int_0^\infty
\frac{\widehat R(v;q_2)}{(v+\chi)(v+1)}\,dv.
$$

Całość jest bezwymiarowa. Zachowano oba argumenty, propagację i spektralną wagę. $\widehat R$ jest zerowe poniżej progu danego kanału; nie zerujemy korelatorów ani tła. Wkład opisuje odpowiedź hadronową, a nie pojedynczego wolnego kwarka.

**Doprecyzowanie skrótu w F0:** standardowe $R$ normalizuje przekrój hadronowy do punktowej odpowiedzi odniesienia. Fizyczny kanał $\mu\mu$ ma także wagę progową. W wiodącym rzędzie EM, przy zgodnych definicjach przekrojów i otwartym kanale:

$$
R(\omega)=
\frac{\sigma_{\rm had}(\omega)}{\sigma_{\mu\mu}(\omega)}
\,B_\mu(\omega),\qquad
B_\mu=\sqrt{1-4(m_\mu/\omega)^2}\,[1+2(m_\mu/\omega)^2].
$$

Zastąpienie $R$ samym fizycznym ilorazem przekrojów wymaga granicy $m_\mu/\omega\to0$; surowe zliczenia wymagają dodatkowo zachowania odpowiedzi aparatu. Poprawki radiacyjne trzeba uzgodnić z definicją użytej odpowiedzi. Jest to zastosowanie 213, nie automatyczne skrócenie wszystkiego przez użycie tego samego O.

**Po kryterium 208:** dla tej odejmowanej odpowiedzi mamy drugi odczyt, jawne stosunki i wagę, bez samego cięcia. Zapis jest relacyjny. Nie wyprowadzono jednak $\widehat R$ z ramy ani wartości α w punkcie odniesienia. Jeśli do wydzielenia części hadronowej użyto znanej masy odniesienia, trzeba zachować ten fakt w bilansie wejść zadania odwrotnego.

Kontrola: dla wolnego kanału, z $\eta=(m/q_2)^2$, użyto
$R(v)=\sqrt{1-4\eta/v}(1+2\eta/v)$ powyżej progu. Całka dyspersyjna i różnica dwóch pełnych $F_\gamma$ zgodziły się w 16 przypadkach do $4.8\cdot10^{-16}$. Zachowano wagę; nie sprawdzano jedynie granicy logarytmicznej.

## 8. Co to daje po stronie masy

W 152 i 217 trzy kanały leptonowe mają tę samą część cechowania. W nazwanym jednopętlowym zakresie SM:

$$
16\pi^2\frac{d}{dt}\ln(y_i/y_j)
=\frac32(y_i^2-y_j^2).
$$

Wspólny ślad i część cechowania znoszą się dokładnie. Pozostający człon Yukaw może być mały, ale nie został ustawiony na zero. **Sam wspólny bieg α nie wybiera hierarchii leptonów.**

Otrzymaliśmy zatem rozdzielenie:

- pełne progi α rozróżniają stosunki mas w zadanej rodzinie odpowiedzi;
- wspólny wkład cechowania do biegu mas nie wybiera stosunków wewnątrz typu;
- przejście A/B z 214 wiąże te odczyty z całym zespołem i nadal wymaga pełnych odpowiedzi, a nie tylko $R_B$;
- to nie zmienia bilansu 208 ani nie wyprowadza hipotezy [104].

Czynnik 3 w anomalnym wymiarze masy i wyprowadzenie wag poza jedną pętlą nadal są otwarte w ramie. Normalizacja $w_\gamma=3rF_\gamma'$ z 252 nie wyprowadza tamtego czynnika 3.

**Najbliższe domknięcie rachunkowe:** z tej samej odpowiedzi spektralnej skonstruować wstawkę polaryzacji próżni do własnej energii nośnika i porównać dwa odczyty mas A/B z zachowanymi wagami. Trzeba policzyć pozostałe wkłady tego rzędu i dopasowanie schematów. Dopiero wtedy można sprawdzić, czy wspólny rachunek wnosi zależność ponad odczyt znanych danych. To nie zostało wykonane w tym raporcie.

## 9. Kontrola i materiały

Kod: alfa-progi-kontrola-2026-10-09.py. Wyniki: alfa-progi-kontrola-2026-10-09.json.

Dokładne ułamki: osiem współczynników jądra, tożsamość wariancji na jawnych przypadkach, kontrprzykład dla dwóch momentów, współczynniki wielomianu i rekurencja do $p_7$. Kontrola numeryczna: odzyskanie syntetycznych stosunków, waga μμ oraz dwie niezależne postacie pełnego progu w 16 przypadkach. Dowód jednoznaczności jest algebraiczny i nie opiera się na tych próbkach.

W pliku głównym: §F0 i 152, 153, 208, 213, 214, 217, 218, 237. Nowe wpisy: 254 (momenty i zakres odczytu) oraz 255 (wkład hadronowy i normalizacja odniesienia).

