# Od połączenia L/R do odczytu A — propagacja, wagi i jawny wkład EM

Data: 04.10.2026. Kontynuacja `higgs-tlo-nierozroznialnosc-2026-10-04.md`.

**Wynik tego kroku:** masowy parametr odczytu A jest wyznaczany przez mianownik pełnej odpowiedzi L/R, a nie przez sam wierzchołek Yukawy ani przez produkcję h. W deklarowanym rachunku perturbacyjnym można już obliczyć część przejścia A/B: wkład EM zawiera α pomnożoną przez logarytm stosunku Yukaw. Pozostają skończone różnice słabe oraz uzgodnienie kompletnego protokołu odczytu fazy.

Nie jest to wyprowadzenie hierarchii Yukaw. Nie dopisano warunku na y, nowej skali cięcia ani składnika działania. Nie zmieniono plików źródłowych i nie nadano temu raportowi numeru poprawki.

## 1. Zakres i punkty odniesienia

- Z pliku: R1d, R1f-3, 166, 180, 198–202, 206–208. Czas, masa i domknięcie 3D nie są tu etapami chronologicznego powstawania świata.
- Z działania SM: diagonalny kanał naładowanego leptonu, przy braku Yukaw neutrinowych. Indeksy L/R są chiralne, nie przestrzenne. Nie przenosimy rachunku na odczyt A pojedynczego uwięzionego kwarka.
- Z poprzedniej korekty: h=0 nie usuwa masowego połączenia L/R. Nierozróżnialność tła nie oznacza zerowego operatora odpowiedzi i nie nadaje tłu odczytanych właściwości.
- E_O oznacza już istniejące odniesienie fazowe znanego czytającego. Π=p/E_O, q=Q/E_O i ν=v/E_O usuwają jednostki. Q jest argumentem wspólnego schematu renormalizacji; nie jest fizycznym cięciem.

Masa w sensie A z 166 zostaje tu użyta w jej **perturbacyjnym znaczeniu biegunowym**. Dokładnego pojedynczego modu fazy naładowanego nośnika nie przyjmujemy jako nowego postulatu; ograniczenie opisano w §5.

## 2. Pełna odwrotność chiralna

**Spodziewam się:** oba masowe połączenia oraz obie wagi propagacji pozostaną w mianowniku. **Zdanie o upadku:** przekład upada, jeśli podany propagator nie jest lewą i prawą odwrotnością jądra, albo jeśli wymaga zrównania wag L i R.

Dla jednego diagonalnego kanału zapisujemy renormalizowane jądro funkcji dwupunktowej:

\[
\widehat{\mathscr D}_i(\Pi)
=\slashed\Pi(a_{L,i}P_L+a_{R,i}P_R)
 -(b_{L,i}P_L+b_{R,i}P_R).
\]

Jest to zwykła struktura Diraca [L1], nie dodatkowe oddziaływanie. W konwencji odwrotności \(\slashed p-m_B-\Sigma\):

\[
a_{L,R}=1-\Sigma^{(A)}_{L,R},\qquad
b_{L,R}=\mu_B+\frac{\Sigma^{(B)}_{L,R}}{E_O},\qquad
\mu_{B,i}=\frac{y_i\nu}{\sqrt2}.
\]

Wszystkie funkcje są oceniane przy tym samym zadeklarowanym schemacie i odpowiednich argumentach. Σ obejmuje sumę składników działania oraz wymagane kontrczłony i uzgodnienie tła. Sam diagram h z wcześniejszego raportu nie wystarcza za tę sumę. Nazwa Σ nie zastępuje jej obliczenia.

Ponieważ \(P_L\slashed\Pi=\slashed\Pi P_R\), a współczynniki pojedynczego kanału są skalarami:

\[
\boxed{
\widehat S_i=E_OS_i
=i\frac{\slashed\Pi(a_LP_L+a_RP_R)+b_RP_L+b_LP_R}
 {d_i(\Pi^2)},\qquad
d_i(z)=z\,a_L(z)a_R(z)-b_L(z)b_R(z).
}
\]

Iloczyn jądra i licznika w obu kolejnościach wynosi \(d_i\mathbf1\). Zamieniają się etykiety **b** w liczniku; etykiety **a** się nie zamieniają. \(\det\widehat{\mathscr D}_i=d_i^2\). W szczególności:

\[
P_L\widehat S_iP_L=\frac{ib_RP_L}{d_i},\qquad
P_R\widehat S_iP_R=\frac{ib_LP_R}{d_i}.
\]

To korelacje L/\(\bar R\) i R/\(\bar L\), a nie dwa dodatnie prawdopodobieństwa. Wagi a i b również nie są samodzielnymi zliczeniami zdarzeń.

Wzór zachowuje dowolne pędy w trzech kierunkach standardowego rachunku SM. Nie wykonano redukcji do 1+1. Jeśli pojawi się mieszanie zapachów, współczynniki będą macierzami i powyższy skalarny iloraz wymaga zastąpienia pełną odwrotnością macierzową; nie zakładamy ich przemienności.

## 3. Miejsce masy: iloraz dwóch iloczynów, oceniany samouzgodnionie

**Spodziewam się:** parametr biegunowy zależy od masowego połączenia podzielonego przez obie wagi kinetyczne; wspólne unormowanie nie ustali stosunków Yukaw. **Zdanie o upadku:** wyprowadzenie upada, jeśli pomija jedną wagę, wybiera argument funkcji na podstawie pomiaru albo uznaje brak prostego bieguna za jego istnienie.

Gdy w zadeklarowanym przybliżeniu występuje biegun \(z_i\), jego warunek wynosi:

\[
d_i(z_i)=0,\qquad
z_i=\frac{b_{L,i}(z_i)b_{R,i}(z_i)}
 {a_{L,i}(z_i)a_{R,i}(z_i)}.
\]

Dla rzeczywistego, dodatniego wyniku masowego \(z_i=\mu_{A,i}^2\); przy biegunie zespolonym trzeba najpierw wyodrębnić masę i szerokość z \(\sqrt{z_i}\). Poniższy rzeczywisty zapis nie usuwa szerokości pełnego propagatora.

Zapisujemy \(b_{L,R}=\mu_B(1+\chi_{L,R})\). Wtedy:

\[
\mu_{A,i}=\frac{y_i\nu}{\sqrt2}C_i^{AB},\qquad
\boxed{
(C_i^{AB})^2=
\left.\frac{(1+\chi_{L,i})(1+\chi_{R,i})}
 {(1-\Sigma^{(A)}_{L,i})(1-\Sigma^{(A)}_{R,i})}
\right|_{z=\mu_{B,i}^2(C_i^{AB})^2}.
}
\]

To równanie niejawne, a nie swobodnie dobierana funkcja. W M8 poprzedniej mapy odpowiednik C był tylko nazwany przez iloraz. Tutaj jego zależność od pełnej funkcji dwupunktowej jest określona.

W jednym rzędzie pętlowym, biorąc część dyspersyjną:

\[
C_i^{AB}=1+\frac12\operatorname{Re}
\left[\Sigma^{(A)}_{L,i}+\Sigma^{(A)}_{R,i}
+\chi_{L,i}+\chi_{R,i}\right]_{z=\mu_{B,i}^2}
+O(\text{dwie pętle}).
\]

Przy zwykłej relacji hermitowskiej między masowymi współczynnikami ten wzór odtwarza jednopętlową strukturę Diraca z [L1, (112)]. Nie wprowadzono pól ani symetrii modelu użytego przez tych autorów.

Dla dwóch kanałów w tym samym odniesieniu:

\[
\frac{\mu_{A,i}}{\mu_{A,j}}=
\frac{y_i}{y_j}\frac{C_i^{AB}}{C_j^{AB}},\qquad
\boxed{
\left(\frac{\mu_{A,i}}{\mu_{A,j}}\right)^2
=\frac{b_{L,i}b_{R,i}/(b_{L,j}b_{R,j})}
 {a_{L,i}a_{R,i}/(a_{L,j}a_{R,j})}.
}
\]

Funkcje kanału i są oceniane przy jego własnym \(z_i\), a kanału j przy \(z_j\). Drugi wzór daje konkretną postać **stosunku dwóch stosunków** w już istniejącym formalizmie. Nie dowodzi, że jest to jeszcze cała postulowana w projekcie funkcja masy: nie wyznacza y_i/y_j ani nie rekonstruuje jej z samych odczytów par.

Wspólne ν znika jako jawny prefaktor. Nie wolno usuwać go ze wszystkich argumentów C: w pełnym rachunku pozostają stosunki odpowiednich progów i rozdzielczości. Po zmianie jednostki E_O oba μ zmieniają się wspólnie, natomiast ich iloraz i C pozostają te same.

## 4. Rzeczywista część przejścia A/B: pełne dopasowanie i obliczony wkład EM

**Spodziewam się:** wspólna część normalizacji Higgsa skróci się w stosunku dwóch leptonów, lecz skończona różnica ich własnych odpowiedzi pozostanie. **Zdanie o upadku:** skrócenie upada, jeśli pełną różnicę słabą zastępuje się zerem albo utożsamia Yukawę SM z parametrem innej teorii efektywnej bez dopasowania.

Hempfling–Kniehl [L2] obliczyli pełne jednopętlowe dopasowanie Yukawy SM do masy biegunowej. Ich wynik można zapisać jako:

\[
y_i(Q)=\mathcal K\,M_i[1+\delta_i(Q)],\qquad
\delta_i=\delta_i^{W}+\delta_i^{\rm EM}
\quad\text{dla leptonów}.
\]

K jest wspólnym unormowaniem. W ich konwencji jest wyrażony przez stałą Fermiego. Nie przypisujemy jej wartości i nie używamy jej jako wejścia: K znika z porównania. Części słaba i EM są u nich oddzielnie skończone i niezależne od parametrów cechowania, przy zachowaniu całego wymaganego zestawu składników [L2, (2.12)–(2.14)].

Ich pełny wynik zawiera sumę wektorowej i skalarnej części fermionowej energii własnej, wspólne dopasowanie sektora W i procesu odniesienia oraz odjęcie UV. W **różnicy** δ_i−δ_j wspólne składniki się skracają. Pozostaje różnica fermionowych odpowiedzi z odpowiednim odjęciem MS-bar. Nie uzasadnia to wyzerowania pozostałych diagramów. W szczególności tadpoli nie usuwa się z każdego diagramu ręcznie: w tym dopasowaniu ich zniesienie wynika z pełnego rachunku.

Oznaczamy \(R_B=y_i/y_j\), \(R_A=M_i/M_j\). Algebra dopasowania daje:

\[
\ln R_A=\ln R_B-(\delta_i-\delta_j)
+O(\text{dwie pętle}).
\]

### 4a. Rachunek EM z zachowaniem licznika

**Spodziewam się:** po odjęciu regulatora wynik będzie zawierał stały składnik i logarytm q/μ_B, a różnica dwóch kanałów zachowa tylko logarytm ich stosunku. **Zdanie o upadku:** wynik upada, jeśli zależy od regulatora lub skończony człon został utracony przez przedwczesne uproszczenie licznika.

Liczymy jeden rząd EM, dla jednakowego modułu ładunku obu leptonów. W standardowym cechowaniu Feynmana i regularyzacji wymiarowej:

\[
\gamma^\alpha(\slashed k+m)\gamma_\alpha
=(2-d)\slashed k+d\,m,\qquad d=4-2\epsilon.
\]

ε jest parametrem standardowej regularyzacji rachunku, nie dodatkowym wymiarem świata ani ziarnem. Po połączeniu mianowników parametrem x i ocenie części masowej na powłoce, mianownik pętli zawiera \((1-x)^2m^2\). Waga licznika to \((4-2x)+\epsilon(2x-2)\). Część skończona przesunięcia masowego wynosi:

\[
c_i^{\rm EM}=\frac{\alpha}{4\pi}
\left\{
-\int_0^1(4-2x)\ln\!\left[(1-x)^2
\frac{\mu_{B,i}^2}{q^2}\right]dx
+\int_0^1(2x-2)dx
\right\}.
\]

Druga całka jest skończonym śladem iloczynu ε z biegunem UV. Pominięcie jej zmieniłoby stałą z 4 na 5. Zachowując obie:

\[
\int_0^1(4-2x)dx=3,\quad
-2\int_0^1(4-2x)\ln(1-x)dx=5,\quad
\int_0^1(2x-2)dx=-1,
\]

\[
\boxed{c_i^{\rm EM}=\frac{\alpha(Q)}{4\pi}
\left[4+3\ln\frac{q^2}{\mu_{B,i}^2}\right].}
\]

Nie został regulator, metr ani sekunda. α jest funkcją argumentu odczytu, nie podstawioną liczbą. Ten wynik jest całym wkładem EM do jednopętlowego dopasowania masowego; nie jest kompletnym propagatorem ani jego residuum.

W konwencji [L2] \(\delta_i^{\rm EM}=-c_i^{\rm EM}\); wewnątrz jednopętlowej poprawki zastąpienie M przez parametr drzewowy zmienia wynik dopiero w następnym rzędzie. Zgodność znaku i współczynników sprawdzono też z [L3, (5)–(6)].

Zatem, zachowując \(\Delta^W_{ij}=\delta_i^W-\delta_j^W\):

\[
\boxed{
\ln R_A=\ln R_B
-\frac{3\alpha(Q)}{2\pi}\ln R_B
-\Delta^W_{ij}(Q)
+O(\text{dwie pętle}).
}
\]

Wspólna stała 4 i jawne ln q się skróciły. Został logarytm **stosunku**, a nie skala cięcia. Nie wykładniczamy tego wzoru jako wyniku we wszystkich rzędach.

To doprecyzowanie mechanizmu z 166, nie ponowne odkrycie zamkniętej tam różnicy A/B. Δ^W jest obliczalną różnicą istniejących diagramów SM, nie dodatkowym dopasowywanym sprzężeniem. W tym raporcie nie obliczono jej skończonej wartości dla pełnego zespołu.

Kontrola zmiany odniesienia w samym sektorze QED: \(d\ln m(Q)/d\ln Q=-3\alpha/(2\pi)\), podczas gdy \(d\ln C^{AB}/d\ln Q=+3\alpha/(2\pi)\) w tym rzędzie. Ich suma dla M znika. Nie podmieniamy tym pełnej beta-funkcji Yukawy SM z 153.

## 5. Biegun, amplituda i pełny odczyt pary nie są jednym wynikiem

**Spodziewam się:** stała waga pojedynczego modu skróci się w porównaniu kolejnych odczytów, lecz pełna superpozycja odpowiedzi zachowa wagi. **Zdanie o upadku:** przejście do jednego tempa fazy upada, jeśli wymaga wyrzucenia ciągłej części odpowiedzi, nieobecnego nakładania z czytającym albo odczytu fazy bez odniesienia.

Przy prostym biegunie z_i:

\[
\widehat S_i\sim
\frac{iN_i(z_i)}{d_i'(z_i)(z-z_i)},\qquad
d_i'=a_La_R+z(a_L'a_R+a_La_R')-b_L'b_R-b_Lb_R'.
\]

Pochodne wag mają znaczenie dla residuum. Źródło i czytający kontraktują cały licznik i residuum; czytający może mieć zerowe nakładanie z danym wkładem mimo jego obecności w funkcji dwupunktowej. Po przygotowaniu i odczycie pełna amplituda jest schematycznie:

\[
\mathcal A_i(n;M,O)=\int d\varepsilon\,
\mathcal W_i(\varepsilon;M,O)e^{-i\varepsilon n}.
\]

n liczy odczyty ustalonego zegara w parze; nie wprowadzamy zewnętrznej osi czasu. W reprezentacji standardowego działania odpowiada to transformacie z zachowanym przygotowaniem, propagacją, integracją po pędach i odczytem. W niejednorodnym protokole nie wolno przyjmować stałej wagi W bez sprawdzenia.

Odczytywalna faza jest fazą względem odniesienia, z potrzebnym zamknięciem porównania; sama faza amplitudy lokalnego naładowanego pola zależy od cechowania. Sam propagator nie definiuje jeszcze fizycznego protokołu tej fazy.

Dopiero dla pojedynczego wkładu w zadeklarowanym zakresie,
\(\mathcal A_i(n)=w_i e^{-(\gamma_i/2+i\mu_i)n}\), zachodzi:

\[
\frac{\mathcal A_i(n+1)}{\mathcal A_i(n)}
=e^{-\gamma_i/2-i\mu_i}.
\]

Stałe w_i znika, moduł zachowuje tłumienie, a faza daje μ modulo 2π. Wybór gałęzi wymaga uzasadnionej kontynuacji odczytu; nie obchodzimy okresowości z 198. μ odpowiada masie w odczycie wzdłuż własnej relacji, po uzgodnieniu czynnika czytającego z R1f-3/180.

Przy dodatkowej części \(\mathcal C_i(n)\) iloraz kolejnych amplitud zależy także od niej. Nie wolno jej skasować samą nazwą „masa”. Właśnie dlatego pełna definicja nie wynika z jednej poprawki ani z samego warunku d=0.

**Konkretne ograniczenie dokładności:** w dokładnym naładowanym sektorze QED prawo Gaussa i wkłady podczerwone nie pozwalają bez dodatkowego uzasadnienia przyjąć ostrego pojedynczego stanu własnego masy [L4]. Perturbacyjny parametr biegunowy użyty w 166 pozostaje użytecznym obiektem rachunku. Utożsamienie go z dokładną pojedynczą fazą całej pary wymaga odczytu obejmującego także nierozróżnione wkłady EM. Nie uzyskano tego tutaj przez przyjęcie niezerowego, skończonego residuum.

## 6. Mapa składników po tym kroku

| Element odpowiedzi | Co wnosi do funkcji | Co usuwa porównanie | Co pozostaje do ustalenia |
|---|---|---|---|
| b_L, b_R | Masowe połączenie L/R wraz z poprawkami | Wspólny jawny prefaktor ν w ilorazie kanałów | Stosunki Yukaw i zależności od progów |
| a_L, a_R | Obie wagi kinetyczne w warunku masowym | Tylko rzeczywiście wspólne czynniki | Różnice kanałów; nie wolno przyjąć a_L=a_R |
| C_i/C_j | Obliczone dopasowanie A/B | Wspólne unormowanie | Skończona różnica słaba i wyższe rzędy |
| α ln(y_i/y_j) | Jawny składnik EM przejścia A/B | Stała 4 i wspólne ln q w jednym rzędzie | Funkcja α zespołu, nie nowa wartość wejściowa |
| N_i/d_i' oraz źródło i odczyt | Amplituda i dostępność wkładu dla danej pary | Stała waga tylko w uzasadnionym ilorazie | Koherencja, nierozróżnione wyniki i pełny protokół |
| λ | Współzależność odpowiedzi sektora H w istniejących diagramach | Nie ma ogólnego skrócenia | Nie otrzymała roli warunku ustalającego Yukawy |

**Co jest nowym postępem:** znana definicja ilorazu A/B z M8 została związana z pełnym jądrem chiralnym; wyliczono skończony wkład EM z jego wagami; wskazano dokładnie, gdzie iloraz odczytów nie może automatycznie usuwać reszty propagacji. Wspólne ∅ nie zamieniło się w źródło substancji ani w zerowy operator.

**Co nadal jest otwarte:** wyprowadzenie wartości y_i/y_j i ν z podstawy projektu, skończona różnica słaba pełnego zespołu, operacyjne domknięcie samoodczytu fazowego z całym otoczeniem oraz przejście do masy złożonego nośnika z QCD. Odtworzenie poprawnego dopasowania SM samo tych punktów nie zamyka.

## 7. Kontrola rachunku bez danych pomiarowych

Przed uruchomieniem kontroli zapisano oczekiwania z §§2–5. Zdanie o upadku kontroli: błędna odwrotność, zgubiona waga, znak poprawki EM lub ukryta zmiana odniesienia unieważniają odpowiedni wniosek. Przykład z dwiema amplitudami jest kontrolą logiczną, nie modelem pełnego SM.

Wszystkie parametry poniżej są syntetyczne i zostały wybrane przed sprawdzeniem. Nie użyto mas ani sprzężeń z pomiaru. Algebra gamma używa pełnych macierzy 4×4 i niezerowych trzech składowych pędu. Kontrole dotyczą tylko nowego przekładu; nie powtarzają poprzednich zestawów.

Kod można uruchomić po skopiowaniu bloku do Pythona z NumPy i SciPy. Liczy wyłącznie kontrole wymienione w raporcie.

```python
import json
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

results = []
def check(name, condition, detail):
    results.append({"kontrola": name, "przeszlo": bool(condition),
                    "szczegol": float(detail)})
    if not condition:
        raise AssertionError((name, detail))

I2 = np.eye(2, dtype=complex)
I4 = np.eye(4, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
pauli = [np.array([[0, 1], [1, 0]], complex),
         np.array([[0, -1j], [1j, 0]], complex),
         np.array([[1, 0], [0, -1]], complex)]
gamma = [np.block([[I2, Z2], [Z2, -I2]])]
gamma += [np.block([[Z2, s], [-s, Z2]]) for s in pauli]
g5 = 1j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]
PL, PR = (I4-g5)/2, (I4+g5)/2
metric = [1, -1, -1, -1]
clifford_error = max(np.max(np.abs(gamma[u]@gamma[v] +
    gamma[v]@gamma[u] - (2*metric[u]*I4 if u == v else 0)))
    for u in range(4) for v in range(4))
check("Algebra gamma", clifford_error < 1e-13, clifford_error)

def slash(p):
    return p[0]*gamma[0] - sum(p[k]*gamma[k] for k in range(1, 4))

p = np.array([2.3, .4, -.7, 1.1])
p2 = p[0]**2 - np.dot(p[1:], p[1:])
aL, aR, bL, bR = .83+.07j, 1.17-.04j, .64+.11j, .79-.06j
ps = slash(p)
D = ps@(aL*PL+aR*PR) - bL*PL-bR*PR
N = ps@(aL*PL+aR*PR) + bR*PL+bL*PR
d = p2*aL*aR-bL*bR
check("Lewa odwrotnosc", np.max(abs(D@N/d-I4)) < 1e-12,
      np.max(abs(D@N/d-I4)))
check("Prawa odwrotnosc", np.max(abs(N@D/d-I4)) < 1e-12,
      np.max(abs(N@D/d-I4)))
check("Wyznacznik", abs(np.linalg.det(D)-d*d) < 1e-11,
      abs(np.linalg.det(D)-d*d))
Shat = 1j*N/d
check("L / bar R", np.max(abs(PL@Shat@PL-1j*bR*PL/d)) < 1e-12,
      np.max(abs(PL@Shat@PL-1j*bR*PL/d)))
check("R / bar L", np.max(abs(PR@Shat@PR-1j*bL*PR/d)) < 1e-12,
      np.max(abs(PR@Shat@PR-1j*bL*PR/d)))
wrongN = ps@(aR*PL+aL*PR)+bR*PL+bL*PR
wrong_error = np.max(abs(D@wrongN/d-I4))
check("Zla zamiana wag wykryta", wrong_error > .01, wrong_error)

unit_factor = 3.7
pnew = p/unit_factor
Dnew = slash(pnew)@(aL*PL+aR*PR)-(bL*PL+bR*PR)/unit_factor
check("Zmiana jednostki jadra", np.max(abs(Dnew-D/unit_factor)) < 1e-12,
      np.max(abs(Dnew-D/unit_factor)))

def matching_exact(eps):
    return math.sqrt((1+.44*eps)**2/((1-.31*eps)*(1+.18*eps)))
eps_values = [.01, .005, .0025]
errors = [abs(matching_exact(e)-(1+.505*e)) for e in eps_values]
orders = [errors[k]/errors[k+1] for k in range(2)]
check("Rozwiniecie jednopetlowe", all(3.8 < t < 4.2 for t in orders),
      max(abs(t-4) for t in orders))
muB = .7
eps = .01
muA = muB*matching_exact(eps)
root_error = abs(muA**2*(1-.31*eps)*(1+.18*eps)-
                 muB**2*(1+.44*eps)**2)
check("Warunek masowy", root_error < 1e-13, root_error)

def coeff(z):
    return 1-.04-.03*z, 1+.02-.01*z, .7*(1+.05+.04*z), .7*(1+.03-.02*z)
def denominator(z):
    al, ar, bl, br = coeff(z)
    return z*al*ar-bl*br
z0 = brentq(denominator, .1, 1.5, xtol=1e-14)
al, ar, bl, br = coeff(z0)
dprime = al*ar+z0*(-.03*ar-.01*al)-.028*br+.014*bl
dz = 1e-6
fd = (denominator(z0+dz)-denominator(z0-dz))/(2*dz)
check("Pochodne wszystkich wag", abs(fd-dprime) < 1e-9, abs(fd-dprime))
pv = np.array([.2, -.25, .3])
def numerator(z):
    al, ar, bl, br = coeff(z)
    pz = np.r_[math.sqrt(z+np.dot(pv, pv)), pv]
    return slash(pz)@(al*PL+ar*PR)+br*PL+bl*PR
residue = 1j*numerator(z0)/dprime
limit = dz*1j*numerator(z0+dz)/denominator(z0+dz)
residue_error = np.max(abs(limit-residue))
check("Residuum pelnego jadra", residue_error < 1e-5, residue_error)

# Calka EM, zachowana takze skonczona waga z epsilon razy biegun UV.
q = 1.6
y_i, y_j, nu = .31, .87, 1.1
mi, mj = y_i*nu/math.sqrt(2), y_j*nu/math.sqrt(2)
def loop_integral(mass, qref):
    def integrand(x):
        return -(4-2*x)*(2*math.log1p(-x)+2*math.log(mass/qref))+(2*x-2)
    return quad(integrand, 0, 1, epsabs=1e-10, epsrel=1e-10)[0]
integrals = [loop_integral(m, q) for m in [mi, mj]]
integral_error = max(abs(v-(4+3*math.log(q*q/(m*m))))
                     for m, v in zip([mi, mj], integrals))
check("Pelna calka EM", integral_error < 1e-9, integral_error)
eps_finite = quad(lambda x: 2*x-2, 0, 1)[0]
check("Skonczony slad regulatora", abs(eps_finite+1) < 1e-12,
      abs(eps_finite+1))
alpha = .011
ci, cj = [alpha*v/(4*math.pi) for v in integrals]
expected = -3*alpha/(2*math.pi)*math.log(y_i/y_j)
check("Logarytm stosunku A/B", abs((ci-cj)-expected) < 1e-11,
      abs((ci-cj)-expected))
ref_diffs = [alpha/(4*math.pi)*(loop_integral(mi, qr)-loop_integral(mj, qr))
             for qr in [.8, 1.6, 3.2]]
check("Wspolna rozdzielczosc skraca sie w czesci EM", np.ptp(ref_diffs) < 1e-11,
      np.ptp(ref_diffs))
normalized_error = abs(loop_integral(mi/unit_factor, q/unit_factor)-integrals[0])
check("Brak jednostki w calce EM", normalized_error < 1e-10, normalized_error)

def rg_error(alpha_value):
    k = 3*alpha_value/(2*math.pi)
    t = .4
    def M(tvalue):
        m = mi*math.exp(-k*tvalue)
        qr = q*math.exp(tvalue)
        return m*(1+alpha_value/(4*math.pi)*(4+3*math.log(qr*qr/(m*m))))
    return abs(math.log(M(t)/M(0)))
rg_order = rg_error(.004)/rg_error(.002)
check("Niezmiennosc masy do jednego rzedu QED", 3.8 < rg_order < 4.2,
      rg_order)

# Kontrola logiczna: dwa zachowane wklady nie sa pojedynczym modem.
mu0, mu1, gamma0, gamma1 = .42, .93, .03, .07
w0, w1 = .8+.3j, .15-.11j
def amplitude(n, first=w0, second=w1):
    return first*np.exp(-(.5*gamma0+1j*mu0)*n)+second*np.exp(-(.5*gamma1+1j*mu1)*n)
single = np.exp(-.5*gamma0-1j*mu0)
single_error = abs(amplitude(4, second=0)/amplitude(3, second=0)-single)
check("Stala waga pojedynczego modu znika", single_error < 1e-12, single_error)
ratios = [amplitude(n+1)/amplitude(n) for n in [0, 1, 3, 8]]
mode_difference = max(abs(r-single) for r in ratios)
check("Drugi wklad nie moze byc pominiety", mode_difference > .01, mode_difference)
ratio_variation = max(abs(r-ratios[0]) for r in ratios)
check("Pelna faza zalezy od zachowanych wag", ratio_variation > .01, ratio_variation)
scale = .7-.4j
scale_error = abs(amplitude(2, scale*w0, scale*w1)/amplitude(1, scale*w0, scale*w1)-ratios[1])
check("Wspolna skala amplitud znika", scale_error < 1e-12, scale_error)

print(json.dumps({"liczba_kontroli": len(results), "wyniki": results},
                 ensure_ascii=False, indent=2))
```

**Wynik uruchomienia:** 22/22 kontroli przeszło; czas około jednej sekundy. Błąd lewej i prawej odwrotności ≤4,5·10⁻¹⁶, wyznacznika ≤3,6·10⁻¹⁵, całki EM ≤3,6·10⁻¹⁵. Kontrola residuum przy skończonym przesunięciu z o 10⁻⁶ dała błąd 6,8·10⁻⁷. Reszta przy zmianie odniesienia QED zmniejszyła się w stosunku 3,99 po podzieleniu α przez dwa, zgodnie z pozostałością drugiego rzędu. Celowo błędna zamiana wag została wykryta. Zachowany drugi wkład zmienił iloraz amplitud i jego fazę.

To sprawdzenie algebry, wag i zakresu przybliżenia; nie pomiarowe potwierdzenie podstawy relacyjnej. Żadne oczekiwanie z tego zestawu nie upadło. Nie wykonano numerycznego obliczenia pełnej różnicy słabej ani kompletnego odczytu fazy w QED.

## Źródła i zakres ich użycia

- **Projekt:** `01-logika-relacyjna-v3.5-7-.md`, R1d, R1f-3, 153, 166, 180, 198–208; `02-poprawki-1-.md`; poprzednie raporty dotyczące mapy masy i korekty znaczenia Higgsa.
- **[L1]** M. Fox, W. Grimus, M. Löschner, [Renormalization and radiative corrections to masses in a general Yukawa model](https://arxiv.org/pdf/1705.09589), część 6, zwłaszcza (111)–(112). Użyto struktury dwupunktowej Diraca, bez nowych pól i symetrii ich modelu.
- **[L2]** R. Hempfling, B. A. Kniehl, [Relation between the fermion pole mass and MS-bar Yukawa coupling in the standard model](https://bib-pubdb1.desy.de/record/392941/files/PhysRevD.51.1386.pdf), Phys. Rev. D 51 (1995) 1386, hep-ph/9408313. Najpierw sprawdzono wyniki i podsumowanie; użyte dopasowanie (1.1), (2.12)–(2.14), bez ich liczbowych danych wejściowych, hipotez GUT i MSSM.
- **[L3]** Z.-z. Xing, H. Zhang, [On the Koide-like Relations for the Running Masses of Charged Leptons, Neutrinos and Quarks](https://arxiv.org/pdf/hep-ph/0602134), (5)–(6), tylko znak i współczynniki dopasowania EM. Nie użyto wartości mas ani warunku Koidego.
- **[L4]** D. Buchholz, [Gauss' law and the infraparticle problem](https://doi.org/10.1016/0370-2693(86)91110-X), Phys. Lett. B 174 (1986) 331–334. Sprawdzono oryginalną pracę, twierdzenie z podsumowania o stanach z ładunkiem i ostrym stanie własnym masy. Nie zastosowano redukcji do 1+1 ani modelu nierelatywistycznego.
