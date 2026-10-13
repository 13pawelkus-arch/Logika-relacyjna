# Globalny więz, lokalne fluktuacje i odczyt warunkowy

09.10.2026. Doprecyzowanie R1a i dalszej pracy po poprawce 257; poprawka 258.

## 1. Co doprecyzował użytkownik

**[H]** Argument o autonomii dynamiki nie ma opierać się na trzeciej zasadzie termodynamiki. Chodzi o możliwość odczytywalnej zmiany w relacjach wewnętrznych bez dodawania zewnętrznego napędu. Nierozróżnialność od Ø nie pozwala wypowiadać wprost ani obecności, ani nieobecności czegoś w Ø.

> Symetria całości nie oznacza braku struktury wewnętrznej.
> Całość może mieć dokładnie zerowy generator i zerową nieoznaczoność tego generatora, a jej części nadal mogą mieć niezerowe fluktuacje, nieoznaczoność.

**Dokładny zapis zera w analizowanej analogii:** generator zeruje stan, `G|Ψ⟩=0`. Na tym stanie jego średnia i wariancja są dokładnie zerowe. Nie ustanawia to `G=0` jako operatora na całej przestrzeni stanów ani zerowania generatorów części. WDW jest tu odwołaniem do więzu, a Page–Wootters do odczytu warunkowego. Ani zero więzu, ani zerowa wariancja nie są definicją temperatury.

## 2. Odczyt, wejścia, oczekiwanie i warunek upadku

**Odczyt:** prawdopodobieństwo wyniku na S warunkowane wskazaniem C, czyli relacja wyników dwóch nazwanych nośników. C jest częścią układu i pełni rolę zegara. Wszystkie fazy i generatory poniżej są bezwymiarowe; θ jest wskazaniem okresowego zegara, a nie dodatkową osią ani parametrem zewnętrznego ruchu.

**Wejścia przykładu:** dwa nośniki kubitowe i algebra Pauliego z R1b; wybór kolektywnych generatorów `J_i=(σ_i⊗𝟙+𝟙⊗σ_i)/2`; znormalizowany stan singletowy; wskazana rodzina efektów odczytu C. To konstrukcja w istniejącym formalizmie, bez nowych pól, areny i jednostek. Wybór tych generatorów i stanu nie jest przedstawiany jako wyprowadzenie konkretnego działania QED ani całego stanu świata z R1a.

**Spodziewam się:** globalny więz będzie dokładny, wszystkie `Var(J_i)` zerowe, lokalne wariancje po `1/4`, a odpowiedź warunkowa zależna od wskazania C. Wariancje części zostaną zniesione przez ich ujemną kowariancję. Sama obecność tych wariancji nie wystarczy jeszcze do wyboru wag ani zapewnienia zmiennego odczytu dla każdego przygotowania.

**Zdanie o upadku:** przykład nie realizuje zamierzonego mechanizmu, jeżeli więz wyzeruje również lokalne wariancje albo odczyt warunkowy singletu okaże się stały dla całej rodziny wskazań C. Silniejsze zdanie „globalny więz i lokalne fluktuacje same wybierają dynamikę lub wagi” upada, jeśli istnieją różne dopuszczalne przygotowania z tym samym więzem i wariancjami, lecz różnymi odczytami warunkowymi.

## 3. Wariancja sumy nie jest sumą wariancji

Niech `G_C` i `G_S` oznaczają już operatory na obu czynnikach wspólnej przestrzeni, więc komutują. Dla znormalizowanego stanu z `G|Ψ⟩=0`, gdzie `G=G_C+G_S`, mamy

$$
\langle G\rangle=0,\qquad \operatorname{Var}(G)=0.
$$

Jednocześnie

$$
\operatorname{Var}(G)=\operatorname{Var}(G_C)+\operatorname{Var}(G_S)
+2\operatorname{Cov}(G_C,G_S).
$$

Z więzu wynika `G_S|Ψ⟩=−G_C|Ψ⟩`. Średnie mają przeciwne znaki, a wektory odchylenia od średniej także są przeciwne. Stąd dokładnie

$$
\operatorname{Var}(G_C)=\operatorname{Var}(G_S)=v,\qquad
\operatorname{Cov}(G_C,G_S)=-v.
$$

Nie wynika `v=0`. Dla `v>0` suma nadal wynosi `v+v−2v=0`. To twierdzenie na równaniach; liczby w przykładzie służą wyłącznie kontroli.

**Zakres:** wariancje wymagają znormalizowanego stanu i określonych drugich momentów. Nie liczymy ich bezpośrednio na nieznormalizowanym, uogólnionym wektorze idealnego zegara ciągłego ani na formalnym rozwiązaniu WDW bez określonego iloczynu skalarnego. Poniższy przykład jest skończony i znormalizowany, więc ta trudność w nim nie występuje.

## 4. Przykład z dokładną symetrią całości

Weźmy

$$
|\Psi^-\rangle=\frac{|0\rangle_C|1\rangle_S-|1\rangle_C|0\rangle_S}{\sqrt2},
\qquad
J_i=\frac{\sigma_i\otimes\mathbb1+\mathbb1\otimes\sigma_i}{2}.
$$

Dla każdego z trzech komplementarnych odczytów

$$
J_i|\Psi^-\rangle=0.
$$

Singlet jest niezmienniczy pod każdym wspólnym obrotem `U⊗U`, `U∈SU(2)`. Mamy zatem dokładną symetrię względem całej tej grupy, a nie tylko brak zmiany pod jednym wybranym obrotem.

Po ograniczeniu do części:

$$
\rho_C=\rho_S=\frac{\mathbb1}{2},\qquad
\langle\sigma_i\rangle_C=\langle\sigma_i\rangle_S=0,
\qquad \operatorname{Var}_C(\sigma_i)=\operatorname{Var}_S(\sigma_i)=1.
$$

Dla generatorów części `σ_i/2` wariancje wynoszą więc `1/4`. Ponadto

$$
\langle\sigma_i\otimes\sigma_j\rangle=-\delta_{ij}.
$$

W szczególności `Cov(σ_i/2⊗𝟙,𝟙⊗σ_i/2)=−1/4`, zatem

$$
\operatorname{Var}(J_i)=\frac14+\frac14+2\left(-\frac14\right)=0.
$$

Wariancje lokalne nie są szumem dodanym do globalnego zera. Są częścią tej samej korelacji, która zapewnia jego dokładność. Stan z zerowym generatorem globalnym może więc mieć niezerową nieoznaczoność komplementarnych odczytów części.

**Operator a więz:** przykładowo `J_3=diag(1,0,0,−1)` w bazie `00,01,10,11`. Jest niezerowym operatorem; zeruje konkretny stan i cały jego sektor zerowy. Utożsamienie więzu z operatorem zerowym usunęłoby treść, która wiąże części.

## 5. Odczyt Page’a–Woottersa bez zewnętrznej osi czasu

Jako wskazania okresowego zegara C wybierzmy

$$
|\chi_\theta\rangle=
\frac{e^{-i\theta/2}|0\rangle+e^{i\theta/2}|1\rangle}{\sqrt2},
\qquad E_\theta=|\chi_\theta\rangle\langle\chi_\theta|.
$$

Efekty można odczytywać jako rodzinę binarnych odczytów `(E_θ,𝟙−E_θ)`. Można też zebrać je w jeden kowariantny odczyt fazy

$$
M_C(d\theta)=\frac{E_\theta}{\pi}\,d\theta,
\quad 0\le\theta<2\pi,
\qquad \int M_C(d\theta)=\mathbb1.
$$

To rozróżnienie jest istotne: dowolne dwa wskazania θ nie są ortogonalnymi stanami dwustanowego zegara. Nie zakładamy doskonałego zegara na nieograniczonej prostej; zegar jest okresowy i ma ograniczony zakres odczytu.

Warunkowanie stanu singletowego daje, z dokładnością do wspólnej fazy,

$$
|\psi_S(\theta)\rangle=
\frac{e^{-i\theta/2}|0\rangle-e^{i\theta/2}|1\rangle}{\sqrt2}
=e^{-i(\sigma_3/2)\theta}|-\rangle.
$$

Zatem

$$
\langle\sigma_1\rangle_{S|\theta}=-\cos\theta,\qquad
\langle\sigma_2\rangle_{S|\theta}=-\sin\theta,\qquad
\langle\sigma_3\rangle_{S|\theta}=0,
$$

oraz

$$
P(+_1|\theta)=\frac{1-\cos\theta}{2}.
$$

Gęstość wskazania C wynosi `1/(2π)`, a wspólna gęstość wyniku `+₁` i θ wynosi `(1−cosθ)/(4π)`. Ich iloraz daje powyższy odczyt warunkowy. Sam marginalny odczyt S ma prawdopodobieństwo `1/2`, niezależne od θ.

θ porównuje wskazanie C z wybraną bazą odczytu S; nie oznacza fazy absolutnej w punkcie. Wynik można zapisać także przez obserwable stacjonarne względem globalnego więzu. Dla `G=J₃` i jego projektorów spektralnych `P_g` niech `𝒯_G(A)=Σ_gP_gAP_g`. Wówczas `𝒪_θ=𝒯_G(E_θ⊗F_{+₁})` komutuje z G, a w całym zerowym sektorze ma te same wartości oczekiwane co `E_θ⊗F_{+₁}`. Zależność warunkowa nie wymaga zatem niestacjonarności globalnej obserwabli.

| wskazanie θ | ⟨σ₁⟩ warunkowe | ⟨σ₂⟩ warunkowe | P(+₁\|θ) |
| --- | ---: | ---: | ---: |
| 0 | −1 | 0 | 0 |
| π/2 | 0 | −1 | 1/2 |
| π | 1 | 0 | 1 |
| 3π/2 | 0 | 1 | 1/2 |

Stan wspólny pozostaje ten sam. Różne wskazania jednego nośnika warunkują różne odczyty drugiego. θ jest etykietą wewnętrznego wskazania; powyższe równanie nie dodaje fizycznej osi czasu do trzech komplementarnych odczytów. Jest skończonym analogiem mechanizmu Page’a–Woottersa, a nie nowym wyprowadzeniem ustalonej w projekcie definicji czasu i 3D.

## 6. Co wybierają korelacje, a czego nie wybiera samo zero

W tym samym zerowym sektorze `J_3` rozważmy przygotowania

$$
\rho_\nu=\frac12\big(
|01\rangle\langle01|+|10\rangle\langle10|
+\nu|01\rangle\langle10|+\nu^*|10\rangle\langle01|
\big),\qquad |\nu|\le1.
$$

Parametr ν opisuje korelację w przygotowaniu, nie nowe sprzężenie fizyczne. Wartości własne na tym sektorze to `(1±|ν|)/2`, więc warunek `|ν|≤1` jest dokładnym warunkiem dodatniości. Dla wszystkich tych stanów:

- `J₃ρ_ν=ρ_νJ₃=0`;
- marginalne stany to `𝟙/2`;
- wariancje generatorów części wynoszą `1/4`, a kowariancja w kierunku 3 wynosi `−1/4`.

Tymczasem po tym samym odczycie C:

$$
\rho_{S|\theta}=\frac12
\begin{pmatrix}
1&\nu^*e^{-i\theta}\\
\nu e^{i\theta}&1
\end{pmatrix},
\qquad
r_1+ir_2=\nu e^{i\theta},\quad r_3=0.
$$

Dla `ν=−1` dostajemy singlet. Dla `ν=0` odczyt warunkowy jest stały i równy `𝟙/2`, mimo zachowania globalnego zera i lokalnych fluktuacji. Dla pozostałych ν zmienia się kontrast i faza odczytu. Komplementarność ogranicza dopuszczalny kontrast przez `|r|=|ν|≤1`; nie wybiera jednej wartości ν z samego więzu `J₃`.

**Silniejszy warunek ma silniejszą konsekwencję.** Jeżeli w tej konkretnej reprezentacji dwóch nośników wymagamy `J_i|Ψ⟩=0` dla wszystkich trzech i, stan jest jednoznacznie singletowy z dokładnością do wspólnej fazy. Z `J₃|Ψ⟩=0` mamy `|Ψ⟩=a|01⟩+b|10⟩`; z `J₁|Ψ⟩=0` wynika `a+b=0`, a z normowania `|a|=|b|=1/√2`. Tu pełna wskazana symetria ustala względne amplitudy. Nie przenosi to wag singletu na jądra QED ani nie dowodzi, że rama narzuca taki warunek dla każdego układu.

Jeszcze słabsza symetria stanu mieszanego, `[J_i,ρ]=0`, nie jest równoważna ostrym więzom `J_iρ=0`: stan `𝟙₄/4` jest niezmienniczy pod obrotami i ma `Var(J_i)=1/2`. Samo słowo „symetria” wymaga więc nazwania grupy i rozróżnienia niezmienniczości od zerowego sektora generatora.

## 7. Zakres odczytu w ramie i konsekwencja dla 257

**[O]** Ten rachunek opisuje znane relacje nazwanych części. Nie wykazuje, że „w Ø są fluktuacje”, ani że „w Ø ich nie ma”. `G|Ψ⟩=0` oznacza określony więz na skonstruowanym układzie, a nie brak wszystkich możliwych odczytów ani utożsamienie tego układu ze zbiorem pustym. Symetria całości sama nie znosi relacji wewnętrznych; nierozróżnialność całości nie uprawnia do twierdzenia o jej zawartości.

**Co trzeba doprecyzować w R1a:** „nieosiągalność zera absolutnego” nie jest ogólnym zakazem zerowego globalnego generatora, zerowej wariancji lub dokładnej symetrii. Jej dotychczasowy sens przy rozróżnialnym odczycie należy zachować z podanym zakresem. Autonomia dynamiki oznacza, że odczyty wewnętrzne mogą być różne przy niezmienności stanu wspólnego, bez napędu z zewnątrz. R1a nadal czytamy razem z R1b–R1c; nie zmienia to definicji czasu, domknięcia 3D ani nieidentyczności stanu i informacji o stanie z 207.

**Co to daje dla wag:** warunkowanie przyporządkowuje amplitudy konkretnym relacjom i przygotowaniu. W ogólnym przykładzie z dopasowanymi widmami `|Ψ⟩=Σ_n c_n|−ε_n⟩_C|ε_n⟩_S` oraz wskazaniem C z amplitudami `d_n`, amplitudy warunkowe mają postać `c_nd_n*e^{−iε_nθ}`, z pełnym normowaniem. Wagi nie są oderwane od przygotowania i odczytu, ale globalny więz sam nie wybiera `c_n`, `d_n` ani widma `ε_n`. Nie używamy tego wzoru jako nowej reguły pętli.

| Zagadnienie | Wynik i granica |
| --- | --- |
| Zero globalne i lokalne fluktuacje | Zgodne dokładnie; znoszą się poprzez kowariancję. |
| Odczytywalna zmiana bez zewnętrznego napędu | Jawnie zrealizowana w relacji C–S, przy stałym stanie wspólnym. |
| Fluktuacje jako wystarczające źródło zmiennego odczytu | Nie: ν=0 zachowuje wariancje i daje stały odczyt warunkowy. |
| Nieoznaczoność jako ograniczenie wag przygotowania | Daje dopuszczalność `|ν|≤1`; silniejszy podany więz wybiera singlet w tej reprezentacji. |
| Pełne jądra i działanie z 257 | Wybór klasy i reguły ilościowej nadal niewyprowadzony. |
| α, hierarchia mas, bilans 208 i [104] | Status pozostaje bez zmiany; nie dodano nowego wyprowadzenia liczb. |

## 8. Kontrola

**PASS — dokładne ułamki zespolone, bez przybliżeń numerycznych.** Sprawdzono trzy kolektywne więzy singletu, dziewięć korelacji spinowych, marginalne stany, wariancje i kowariancje. Dla siedmiu przygotowań ν i pięciu dokładnych faz sprawdzono 35 odpowiedzi warunkowych, prawdopodobieństwa, nieoznaczoność oraz stacjonarną postać wspólnego efektu. Stan `𝟙₄/4` zachował symetrię i miał wariancję `1/2`; niedopuszczalne `ν=6/5` zostało rozpoznane przez ujemny wyznacznik bloku, mimo zachowania więzu `J₃ρ=0`. Dowodami są równania z §§3–6; skończony zestaw kontroli nie zastępuje tych dowodów ani nie wyprowadza działania i hierarchii mas.

## 9. Źródła i pochodzenie

- Doprecyzowanie użytkownika w bieżącej rozmowie, 09.10.2026 [H]; R1a (189b, 207), R1b, R1c oraz odczyt 206. Nie odnaleziono wcześniejszej niezapisanej wersji: tę analizę odtworzono z bieżącego doprecyzowania i matematyki.
- [Page–Wootters, *Evolution without evolution: Dynamics described by stationary observables*, Phys. Rev. D 27, 2885 (1983)](https://doi.org/10.1103/PhysRevD.27.2885): źródło mechanizmu; zweryfikowany abstrakt, nie deklarujemy ponownego przeczytania pełnego artykułu.
- [Giovannetti–Lloyd–Maccone, *Quantum Time*, arXiv:1504.04215v3, Phys. Rev. D 92, 045033 (2015)](https://arxiv.org/abs/1504.04215): §A, równania (1)–(5) — więz i odczyt warunkowy; (16) — rola wyboru zera; uwagi o normalizacji. Formalizm jest punktem porównania, nie zewnętrznym uzasadnieniem definicji czasu i 3D projektu.
- Przykład dwóch nośników, jego wariancje, rodzina ρ_ν i rozdzielenie zakresów wyprowadzono tutaj [A][T]. Nie utożsamiono go z pełnym działaniem pola, idealnym zegarem ciągłym ani stanem całości kosmologicznej.
