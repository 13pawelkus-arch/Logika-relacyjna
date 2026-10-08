$$
f\in\ker(L-L^{\mathsf T})
\iff
\forall z:\quad
\sum_{y:\,z\lessdot y}f_y
=
\sum_{y:\,y\lessdot z}f_y.
$$

# Linki, separatory i jądro hop-stop — rozstrzygnięcie
Wynik: **(b)**. Separator linkowy sformułowany w pytaniu nie wyklucza dokładnych zależności między odczytami elementów niebędących bliźniakami. Upada również zawieranie jądra masowego w bezmasowym. Dla każdego odczytu a·b wymiar jądra jest taki sam, ale przestrzeń relacji może się zmieniać.

## Zakres i przedmiot odczytu

Rozpatrujemy dowolny skończony porządek i jego skierowaną macierz linków: L_xy = 1 wtedy i tylko wtedy, gdy x ⋖ y. Nie wybieramy rozsiewu, wymiaru areny, gęstości ani jednostek. Wspólny niezerowy czynnik a można usunąć przy badaniu jądra. Piszemy η = a·b; η oznacza odczyt z 206. Zależność od η jest badana warunkowo dla możliwych wartości odczytu, bez wyprowadzania czy wstawiania jego wartości.

$$
R_\eta=\frac{K_\eta-I}{a}
=L(I-\eta L)^{-1}
=\sum_{k\geq1}\eta^{k-1}L^k,
\qquad
\Delta_\eta=R_\eta-R_\eta^{\mathsf T}.
$$

Suma jest skończona przez nilpotentność L. Przy η = 0 mamy Δ_0 = L − Lᵀ. Badane relacje to wektory w ker Δ_η. Zgodnie z zakresem 171, w reprezentacji SJ dają one zerowe kombinacje pól/odczytów. W innych reprezentacjach wskazują kierunki centralne; wyzerowanie centrum jest osobnym wyborem reprezentacji.

**Spodziewam się:** prywatność linku jedynie wobec maksymalnych elementów nośnika nie wystarcza do odtworzenia dowodu 171. **Zdanie o upadku:** wystarczy jawny wektor jądra z nośnikiem bez bliźniaków i z prywatnym górnym linkiem dla każdego jego elementu maksymalnego. Dla zawierania jąder wystarczy wektor należący do ker Δ_η, a nienależący do ker Δ_0, przy η ≠ 0.

## 1. „≡” dla pełnych link-sąsiedztw

W skończonym porządku identyczne skierowane zbiory poprzedników i następników linkowych są równoważne identycznej całej przeszłości i przyszłości. Zatem propozycja (c), z nierównoważnością w drugą stronę, nie zachodzi w rozpatrywanym zakresie.

Jeśli F(x) oznacza ścisłą przyszłość, to:

$$
F(x)=\bigcup_{x\lessdot u}\bigl(\{u\}\cup F(u)\bigr).
$$

Ta sama lista bezpośrednich następników daje tę samą przyszłość. Analogicznie dla przeszłości. Odwrotnie: bezpośredni następnik jest minimalnym elementem F(x), a bezpośredni poprzednik — maksymalnym elementem przeszłości.

Dotyczy to tych samych zbiorów elementów, ze wskazanym kierunkiem, w całym porządku. Równość samych liczności sąsiedztw lub odczyt tylko przez wybrane otoczenie jest innym warunkiem.

## 2. Kontrprzykład dla separatorów linkowych

Osiem elementów, następujące linki i żadnych innych:

$$
p\lessdot u\lessdot x\lessdot z,
\qquad
q\lessdot v\lessdot y\lessdot w,
\qquad
q\lessdot z,
\qquad
p\lessdot w.
$$

Żaden wymieniony link nie ma elementu pośredniego. Porządek jest domknięciem przechodnim tych linków.

W kolejności (p,q,u,v,x,y,z,w) bierzemy:

$$
f=(1,-1,0,0,1,-1,0,0)^{\mathsf T}.
$$

Nośnik to {p,q,x,y}; jego elementy maksymalne to x oraz y. Element z ma link od x i nie ma linku od y; element w ma link od y i nie ma linku od x. Są więc separatorami zgodnie z definicją podaną w pytaniu. Nad z i w nie ma elementów nośnika.

Sprawdzenie warunku jądra w każdym elemencie:

| Element | Suma wag po linkach nad | Suma wag po linkach pod |
| --- | --- | --- |
| p | f_u + f_w = 0 | 0 |
| q | f_v + f_z = 0 | 0 |
| u | f_x = 1 | f_p = 1 |
| v | f_y = −1 | f_q = −1 |
| x | f_z = 0 | f_u = 0 |
| y | f_w = 0 | f_v = 0 |
| z | 0 | f_x + f_q = 0 |
| w | 0 | f_y + f_p = 0 |

Zatem Δ_0 f = 0, mimo obu separatorów. Wszystkie osiem pełnych skierowanych profili linkowych jest różnych; nie ma pary bliźniaków.

W sensie kryterium SJ z 171:

$$
\boxed{\varphi_p+\varphi_x=\varphi_q+\varphi_y.}
$$

To nie jest różnica dwóch równych odczytów: jest to równość sum odczytów czterech rozróżnialnych elementów.

### Co nie przechodzi z dowodu 171

Dla macierzy C separator odczytuje przeszłość x razem z klasą x, a równanie w x pozwala odjąć wagę tej przeszłości. Dla L równanie w x dotyczy bezpośrednich poprzedników x. Bezpośredni poprzednik x nie może zarazem mieć linku do z, gdy x ⋖ z — pośredniczy wtedy x.

W przykładzie z odczytuje x i q. Element q nie jest maksymalny w nośniku, więc dozwala go zaproponowana definicja separatora; nie leży jednak w przeszłości x. Wagi x i q znoszą się. Analogicznie w odczytuje y i p.

Aby sam wiersz separatora wymuszał zerową sumę w klasie x, trzeba izolować tę klasę wobec całego aktualnego nośnika lub osobno dowieść zerowej sumy pozostałych wag. Wykluczenie pozostałych elementów maksymalnych nie wystarcza.

### Co linki niosą dokładnie

Nazwą tej zależności jest **równość sum skierowanych profili linkowych**. Przy ℓ_r = Δ_0 e_r mamy:

$$
\ell_p+\ell_x=\ell_q+\ell_y.
$$

Dla macierzy wszystkich relacji C ta sama kombinacja nie jest zerowa:

$$
(C-C^{\mathsf T})f
=(1,-1,0,0,-1,1,-1,1)^{\mathsf T}.
$$

Nie pojawia się informacja niezawarta w porządku: linki są jednoznacznie wyznaczone przez skończony porządek. Dwie konstrukcje wag zachowują inne dokładne zależności odczytów. Równe wagi na wszystkich relacjach nie zachowują wykazanej równowagi samych linków.

W ramach identyfikacji bezmasowego odczytu z jądrem linkowym jest to zdanie o dokładnych relacjach odczytów dla światła. Nie jest potrzebny opis historii światła między odczytami.

Kontrprzykład nie wymaga końca dalszych relacji: można przedłużać porządek nad z i w, nadając nowym współczynnikom f wartość zero. Warunek linkowy pozostanie spełniony. Jest to zero współczynników kombinacji liniowej; nie oznacza identyfikacji nowych elementów z Ø.

## 3. Dokładne twierdzenie dla odczytu η = a·b

Niech B_η = I − ηL. Nilpotentność daje det B_η = 1 dla każdej skończonej wartości η.

$$
\begin{aligned}
B_\eta^{\mathsf T}\Delta_\eta B_\eta
&=(I-\eta L^{\mathsf T})L
  -L^{\mathsf T}(I-\eta L)\\
&=L-L^{\mathsf T}.
\end{aligned}
$$

Stąd:

$$
\boxed{
\Delta_\eta
=B_\eta^{-\mathsf T}\Delta_0 B_\eta^{-1},
\qquad
\ker\Delta_\eta=B_\eta\ker\Delta_0.
}
$$

W szczególności:

$$
\boxed{
\operatorname{rank}\Delta_\eta=\operatorname{rank}\Delta_0,
\qquad
\dim\ker\Delta_\eta=\dim\ker\Delta_0
\quad\text{dla każdego }\eta.
}
$$

Dla tej konstrukcji waga zatrzymań zmienia współczynniki dokładnych relacji; nie zmniejsza ich liczby.

Jeśli H = ker Δ_0, to dla η ≠ 0:

$$
\ker\Delta_\eta=H
\iff LH\subseteq H.
$$

Dowód: (I − ηL)H = H jest równoważne niezmienniczości H względem L; odwrotność na H istnieje dzięki nilpotentności. Warunek nie zależy od wyboru niezerowego η. Zatem albo jądro jest równe bezmasowemu dla wszystkich η, albo różni się od niego dla każdego η ≠ 0. Ponieważ wymiary są równe, zawieranie w H może zachodzić wyłącznie jako równość.

Różnice bliźniaków zawsze pozostają: dla identycznych pełnych sąsiedztw linkowych L(e_i − e_j) = Lᵀ(e_i − e_j) = 0. Jeśli całe H składa się z takich różnic, wszystkie jądra masowe są z nim identyczne.

Nie ma wartości η, na której zmieniałby się rząd całej Δ_η. Dla z góry ustalonego wektora f równania Δ_η f = 0 są skończonym układem wielomianów: albo obowiązują dla wszystkich η, albo tylko dla skończenie wielu rzeczywistych wartości η (być może żadnej). Rozstrzyga to algebra, bez próbkowania. Twierdzenie o stałym rzędzie nie narzuca stałości rang ograniczeń do wybranych podzbiorów odczytów.

## 4. Ten sam porządek obala zawieranie dla każdego η ≠ 0

W powyższym przykładzie Lf = e_u − e_v, zatem:

$$
f_\eta=B_\eta f
=f-\eta(e_u-e_v)
\in\ker\Delta_\eta.
$$

Jednocześnie:

$$
\Delta_0 f_\eta
=-\eta(1,-1,0,0,-1,1,0,0)^{\mathsf T}
\ne0\qquad(\eta\ne0).
$$

Zatem:

$$
\boxed{\ker\Delta_\eta\not\subseteq\ker\Delta_0
\quad\text{dla każdego }\eta\ne0.}
$$

Odpowiadająca dokładna relacja SJ ma postać:

$$
\boxed{
\varphi_p+\varphi_x-\varphi_q-\varphi_y
=\eta(\varphi_u-\varphi_v).
}
$$

Jej elementy maksymalne w nośniku nadal są x i y, z tymi samymi separatorami z i w. Także masowa wersja nie spełnia postulowanego twierdzenia o separatorach linkowych.

## Status względem dokumentu

171 zachowuje swój zapisany zakres dla C i swojej definicji separatora. Proponowane rozszerzenie na L z nową definicją separatora upada. Wynik ogólny dla hop-stop jest inny: jawne przeniesienie jądra przez I − (a·b)L i stały rząd dla wszystkich wartości odczytu.

181, po korekcie 194, oraz 206 są używane wyłącznie do identyfikacji a·b jako bezwymiarowej wagi odczytu. Żadna jego wartość nie została wyprowadzona, dopasowana ani przypisana wnętrzu jako odrębna cecha.

## Kontrola

Po dowodzie wykonano dokładną kontrolę na całkowitych współczynnikach macierzy i wielomianów, z eliminacją nad ułamkami wymiernymi. Sprawdzono: wszystkie podane krawędzie są linkami; osiem różnych profili; oba separatory; Δ_0 f = 0; niezerowe (C − Cᵀ)f; rząd Δ_0 równy 6 i wymiar jądra równy 2; każdy współczynnik tożsamości BᵀΔ_ηB = Δ_0 oraz Δ_ηf_η = 0. Nie losowano porządków ani wartości η.

