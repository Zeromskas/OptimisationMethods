# Užduotis
1. Kokia turėtų būti stačiakampio gretasienio formos dėžė, kad vienetiniam paviršiaus plotui jos tūris būtų maksimalus?
2. Suprogramuokite gradientinio nusileidimo, greičiausiojo nusileidimo ir deformuojamo simplekso algoritmus.
3. Laikant kintamaisiais dėžės priekinės ir galinės sienų plotų sumą, šoninių sienų plotų sumą, viršutinės ir apatinės sienų plotų sumą, aprašykite vienetinio dėžės paviršiaus ploto reikalavimą ir dėžės tūrio pakelto kvadratu funkciją.
4. Iš vienetinio paviršiaus ploto reikalavimo išveskite vieno iš kintamojo išraišką per kitus.
5. Aprašykite tikslo funkciją $f\left(X\right)$ taip, kad optimizavimo uždavinys būtų formuluojamas be apribojimų: $min\ f\left(X\right)$.
6. Išveskite ir aprašykite tikslo funkcijos gradiento funkciją.
7. Apskaičiuokite tikslo ir gradiento funkcijų reikšmes taškuose $X_0=(0, 0)$, $X_1=(1, 1)$ ir $X_m=(\frac{a}{10}, \frac{b}{10})$, čia a ir b – studento knygelės numerio "1x1xxab" skaitmenys.
8. Minimizuokite suformuluotą uždavinį naudojant suprogramuotus optimizavimo algoritmus pradedant iš taškų $X_0$, $X_1$ ir $X_m$.
9. Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius priklausomai nuo pradinio taško.
10. Vizualizuokite tikslo funkciją ir bandymo taškus.

# Darbo Priemonės
Darbui atlikti pasirinkau naudoti Python programavimo kalbą dėl didelio bibliotekų kiekio, funkcijų vizualizacijos galimybių ir paprastos sintaksės. Grafikų vizualizacijai naudojausi matplotlib.pyplot biblioteka.

# Tikslo funkcija
Apsibrėžkime stačiakampio gretasienio kraštines kaip a, b, c.
 
<img src="https://github.com/Zeromskas/OptimisationMethods/blob/b1a5b969c1394327bcf0ecce52e8e179d65e9cd4/2%20Optimisation%20Without%20Constraints/visualistion/1-rectangle.png" alt="Function Visualization" width="300">

Stačiakampio gretasienio paviršiaus plotas yra jo sienų plotų suma, o tūris – trijų kraštinių, einančių iš vienos viršūnės, sandauga. Šiuo atveju:
$$S=2ab+2bc+2ac \quad V=abc$$
Apsibrėžkime $x_1$, $x_2$ ir $x_3$ kaip šio stačiakampio gretasienio vienos prieš kitą esančių sienų plotų sumas:
$$x_1=2ab \quad	x_2=2ac \quad x_3=2bc$$
Tuomet šio vienetinio paviršiaus ploto gretasienio paviršiaus plotą galima apsirašyti taip:
$$S=x_1+x_2+x_3=1$$
Iš šios funkcijos išsireiškime $x_3$ per $x_1$ ir $x_2$:
$$x_3=1-x_1-x_2$$
Naudojant a, b ir c, stačiakampio gretasienio tūrio kvadratas būtų $$V^2(a,b,c)= (abc)^2 = a^2b^2c^2$$
Tačiau mums reiktų stačiakampio gretasienio tūrio kvadratą išsireikšti per  $x_1$, $x_2$ ir $x_3$. Skaičiuojant stačiakampio gretasienio vienos prieš kitą esančių sienų plotų sumų sandaugą gauname:
$$x_1\ast x_2\ast x_3=2ab\ast2bc\ast2ac=8a^2b^2c^2$$
Galime pastebėti, kad šios sandaugos rezultatas nuo $V^2\left(a,b,c\right)$ formule gauto rezultato skiriasi tik daugikliu 8, todėl stačiakampio gretasienio tūrio kvadratą nesunkiai galime apsirašyti formule:
$$V^2\left(x_1,x_2,x_3\right)=\frac{x_1\ast x_2\ast x_3}{8}$$
Pakeitus $x_3=1-x_1-x_2$ gauname tūrio kvadrato formulę su dviem kintamaisiais:
$$V^2\left(x_1,x_2\right)=\frac{x_1\ast x_2\ast{(1-x}_1-x_2)}{8}=\frac{x_1x_2-x_1^2x_2-x_1x_2^2}{8}$$
Kadangi ieškoma didžiausio tūrio, nors formuluojamas minimumo uždavinys, formulėje reikia prirašyti minuso ženklą (kuo mažesnis neigiamas tūrio kvadratas, tuo didesnis tūris):
$$minf\left(X\right)=-V^2\left(X\right)=-\frac{x_1x_2-x_1^2x_2-x_1x_2^2}{8}=\frac{x_1^2x_2+x_1x_2^2-x_1x_2}{8}$$
Iš šios tikslo funkcijos gaunami gradientai:
$$\nabla f\left(X\right)=\left(\frac{\partial f\left(X\right)}{\partial x_1},\ \frac{\partial f\left(X\right)}{\partial x_2}\right)=\left(\frac{2x_1x_2+x_2^2-\ x_2}{8},\ \frac{x_1^2+2x_1x_2-\ x_1}{8}\right)$$

# Minimali tikslo funkcijos reikšmė
Norint rasti minimalią funkcijos reikšmę reikia tikrinti būtinąją minimumo sąlygą (funkcijos gradientas lygus nuliui):
$$\nabla f\left(X\right)=0$$
$$\frac{2x_1x_2+x_2^2-x_2}{8}=0 \quad \frac{x_1^2+2x_1x_2-x_1}{8}=0$$ 

$$2x_1x_2+x_2^2-x_2=0 \quad x_1^2+2x_1x_2-x_1=0$$
$$x_2x_1+x_2-1=0 \quad x_1^2x_2+x_1-1=0$$ 

$x_1=0$ arba $x_2=0$ netinka, nes tokiu atveju stačiakampio tūris $V=0$, o toks stačiakampis neegzistuoja.
$$2x_1+x_2-1=0 \quad 2x_2+x_1-1=0$$
$$x_2=1-2x_1$$
$$x_1+2\left(1-x_1\right)-1=0$$
$$-3x_1+1=0$$
$$x_1=\frac{1}{3}	\quad x_2=1-2x_1=\frac{1}{3}	\quad x_3=1-x_1-x_2=\frac{1}{3}$$

Radome tikslo funkcijos kritinį tašką, tačiau nežinome, ar jis yra minimumas. Tam išsiaiškinti tikrinsime pakankamą minimumo sąlygą: Hesės matrica teigiamai apibrėžta.

```math
H(X)=\frac{1}{8} \begin{bmatrix}2x_2 & 2x_1+2x_2-1 \\\ 2x_1+2x_2-1 & 2x_1 \\\end{bmatrix}
```
```math
H(X^\ast)=\frac{1}{8} \begin{bmatrix}\frac{2}{3} & \frac{2}{3}+\frac{2}{3}-1 \\\ \frac{2}{3}+\frac{2}{3}-1&\frac{2}{3}\\\end{bmatrix} = \frac{1}{24} \begin{bmatrix}2&1\\1&2\\\end{bmatrix}
```

Hesės matrica yra teigiamai apibrėžta, jei $\left|A-\lambda\ast I\right|=0$ visos $\lambda>0$
```math
\left|\begin{bmatrix}2-\lambda&1\\1&2-\lambda\\\end{bmatrix}\right|=\left(2-\lambda\right)^2-1=0
```
$$\lambda^2-4\lambda+4-1=0$$
$$\lambda^2-4\lambda+3=0$$
$$\lambda=3	\lambda=1$$
$X=\left(\frac{1}{3},\frac{1}{3}\right)$ patenkina būtinąsias ir pakankamąsias minimumo sąlygas, todėl jis ir yra tikslo funkcijos lokalusis minimumas.

_1 lentelė. Tikslo funkcijos ir gradiento reikšmės taškuose_
|              | $f(X)$     | $\nabla f(X)$   |
| ------------ | ---------- | --------------- |
| X=(0, 0)     | 0          | (0, 0)          |
| X=(1, 1)     | 0.125      | (0.25, 0.25)    |
| X=(0.7, 0.4) | 0.0035     | (0.04, 0.04375) |
| X=(1/3, 1/3) | -0.0046296 | (0, 0)          |

# Tikslo funkcijos optimizavimas
Dvimatės funkcijos lokaliajam minimumui rasti parašiau 3 algoritmus:
- Gradientinio nusileidimo
- Greičiausio nusileidimo
- Deformuoto simplekso
Toliau pateikiami funkcijos minimizavimo minėtais algoritmai rezultatai. Kiekvienas algoritmas bandytas nuo šių pradinių taškų: (0, 0), (1, 1) ir (0.7, 0.4).

## Taškas (0, 0)
_2 lentelė Algoritmų konvergavimas iš taško (0, 0)_
| Metodas                   | Iteracijos | Tikslo funkcijos skaičiavimai | Gradiento skaičiavimai | Laikas       | Minimumas X                               | Minimumas f(X) | Vizualizacija                                                                                                                                                                                                                |
|---------------------------|------------|-------------------------------|------------------------|--------------|-------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Gradientinis nusileidimas | 1          | 0                             | 1                      | 5.72205e-06s | (0, 0)                                    | 0              | <img src="https://github.com/Zeromskas/OptimisationMethods/blob/b1a5b969c1394327bcf0ecce52e8e179d65e9cd4/2%20Optimisation%20Without%20Constraints/visualistion/2-gradient-0_0.png" alt="Function Visualization" width="300"> |
| Greičiausias nusileidimas | 1          | 0                             | 1                      | 2.6226e-06s  | (0, 0)                                    | 0              | <img src="https://github.com/Zeromskas/OptimisationMethods/blob/b1a5b969c1394327bcf0ecce52e8e179d65e9cd4/2%20Optimisation%20Without%20Constraints/visualistion/3-fastest-0_0.png" alt="Function Visualization" width="300">  |
| Deformuotas Simpleksas    | 29         | 61                            | 0                      | 0.000226974s | (0.3332883951013336, 0.33333327823900827) | -0.00462963    | <img src="https://github.com/Zeromskas/OptimisationMethods/blob/b1a5b969c1394327bcf0ecce52e8e179d65e9cd4/2%20Optimisation%20Without%20Constraints/visualistion/4-simplex-0_0.png" alt="Function Visualization" width="300">  |

## Taškas (1, 1)
_3 lentelė. Algoritmų konvergavimas iš taško (1, 1)_
| Metodas                   | Iteracijos | Tikslo funkcijos skaičiavimai | Gradiento skaičiavimai | Laikas       | Minimumas X                              | Minimumas f(X) | Vizualizacija |
|---------------------------|------------|-------------------------------|------------------------|--------------|------------------------------------------|----------------|---------------|
| Gradientinis nusileidimas | 16         | 0                             | 16                     | 0.000174761s | (0.3330303473132839, 0.3330303473132839) | -0.00462962    |   <img src="https://github.com/Zeromskas/OptimisationMethods/blob/b1a5b969c1394327bcf0ecce52e8e179d65e9cd4/2%20Optimisation%20Without%20Constraints/visualistion/5-gradient-1_1.png" alt="Function Visualization" width="300">            |
| Greičiausias nusileidimas | 2          | 58                            | 2                      | 7.70092e-05s | (0.3333346048990886, 0.3333346048990886) | -0.00462963    |    <img src="https://github.com/Zeromskas/OptimisationMethods/blob/b1a5b969c1394327bcf0ecce52e8e179d65e9cd4/2%20Optimisation%20Without%20Constraints/visualistion/6-fastest-1_1.png" alt="Function Visualization" width="300">            |
| Deformuotas Simpleksas    | 37         | 78                            | 0                      | 0.000249863s | (0.3333008954359039, 0.3333541868497003) | -0.00462963    |    <img src="https://github.com/Zeromskas/OptimisationMethods/blob/b1a5b969c1394327bcf0ecce52e8e179d65e9cd4/2%20Optimisation%20Without%20Constraints/visualistion/7-simplex-1_1.png" alt="Function Visualization" width="300">           |

## Taškas (0.7, 0.4)
_4 lentelė. Algoritmų konvergavimas iš taško (0.7, 0.4)_
| Metodas                   | Iteracijos | Tikslo funkcijos skaičiavimai | Gradiento skaičiavimai | Laikas       | Minimumas X                                | Minimumas f(X) | Vizualizacija |
|---------------------------|------------|-------------------------------|------------------------|--------------|--------------------------------------------|----------------|---------------|
| Gradientinis nusileidimas | 31         | 0                             | 31                     | 0.000175953s | (0.3346425479064759, 0.3320329585799615)   | -0.00462956    |   <img src="https://github.com/Zeromskas/OptimisationMethods/blob/b1a5b969c1394327bcf0ecce52e8e179d65e9cd4/2%20Optimisation%20Without%20Constraints/visualistion/8-gradient-0.7_0.4.png" alt="Function Visualization" width="300">            |
| Greičiausias nusileidimas | 29         | 957                           | 29                     | 0.00095892s  | (0.33451797345760564, 0.33215586095217065) | -0.00462957    |    <img src="https://github.com/Zeromskas/OptimisationMethods/blob/b1a5b969c1394327bcf0ecce52e8e179d65e9cd4/2%20Optimisation%20Without%20Constraints/visualistion/9-fastest-0.7_0.4.png" alt="Function Visualization" width="300">            |
| Deformuotas Simpleksas    | 33         | 69                            | 0                      | 0.000213146s | (0.33330784803767444, 0.33337187444609606) | -0.00462963    |  <img src="https://github.com/Zeromskas/OptimisationMethods/blob/b1a5b969c1394327bcf0ecce52e8e179d65e9cd4/2%20Optimisation%20Without%20Constraints/visualistion/10-simplex-0.7_0.4.png" alt="Function Visualization" width="300">             |


# Rezultatų išvados
Iš gautų optimizavimo rezultatų pastebėjau, kad:
- Taškas (0, 0) (_2 lentelė Algoritmų konvergavimas iš taško (0, 0)_) – Gradientinis ir greičiausias nusileidimai konverguoja iki taško, kuriame gradientas lygus 0 (kritinis taškas). Jeigu skaičiavimai prasideda nuo taško, tenkinančio šią sąlygą, algoritmas sustoja (kaip galime matyti gradientinio ir greičiausio nusileidimo atveju pasirinkus pradinį tašką kaip (0, 0)). Šie algoritmai ieško kritinio taško, o kadangi taškas (0,0) tenkina būtinąsias sąlygas, algoritmas sustoja. Tuo tarpu simplekso algoritmas puikiai konverguoja šiuo atveju, nes nenaudoja funkcijos gradiento, o taškus tikrina su tikslo funkcija
- Taškas (1, 1) (_3 lentelė. Algoritmų konvergavimas iš taško (1, 1)_) – Greičiausią konvergavimą gradientinio nusileidimo metodu tikrintų pradinių taškų atveju gavau su žingsnio daugikliu $\gamma=3.7$. Taško (1, 1) atveju gradientas yra (0.25, 0.25) (1 lentelė. Tikslo funkcijos ir gradiento reikšmės taškuose), todėl pirmu žingsniu lokalaus minimumo taškas yra peršokamas, tačiau po pirmos iteracijos pasiektame taške gradientas yra nukreiptas į kitą pusę ir yra žymiai mažesnis, todėl per kitas 15 iteracijų šis metodas sėkmingai konverguoja į lokalų minimumą (1/3, 1/3). Atliekant bandymus iš kitų taškų šis žingsnio daugiklis gali būti per didelis ir metodas gali nekonverguoti, todėl jį gali reikėti keisti siekiant rasti lokalų minimumą iš kitų pradinių taškų. Tuo tarpu gradientinis nusileidimas, kiekvienam žingsniui randa geriausią žingsnio daugiklį, todėl per 2 iteracijas sėkmingai konverguoja į lokalųjį minimumą, naudodamas mažiausiai gradiento skaičiavimų tačiau jis daug kartų kviečia tikslo funkciją ieškodamas optimalaus žingsnio daugiklio kiekvienos iteracijos metu, kas gali būti traktuojama kaip neigiama metodo savybė, kai tikslo funkcijos skaičiavimas yra sudėtingesnis nei gradiento skaičiavimas. Deformuoto simplekso algoritmas tikslo funkciją kviečia dar daugiau kartų taigi dažnai nėra optimaliausias konvergavimo metodas. Taip pat jis lengvai gali peršokti lokalųjį minimumą, ir konverguoti į kitą lokalųjį minimumą, jeigu nėra užtikrinti metodo apribojimai uždavinio sąlygoms.
- Taškas (0.7, 0.4) (_4 lentelė. Algoritmų konvergavimas iš taško (0.7, 0.4)_) – Šiuo atveju, gradientinio nusileidimo žingsnio daugiklį vėlgi pasirinkus $\gamma=3.7$ šis metodas atlieka tik vos daugiau iteracijų palyginus su greičiausiu nusileidimu, o kadangi greičiausiame nusileidime kviečiama žymiai daugiau tikslo funkcijų, jis skaičiavimo laiko aspektu gradientinis nusileidimas konverguoja greičiau. Deformuotas simpleksas konverguoja per panašų iteracijų kiekį, nereikalaudamas gradiento skaičiavimo ir tik 69 tikslo funkcijų kvietimų, todėl jis yra antras geriausias pasirinkimas šio pradinio taško atveju, pirmąją vietą užleisdamas gradientiniam nusileidimui dėl skaičiavimo laiko.

Apibendrinus šias išvadas, gradientinio ir greičiausio nusileidimo bei deformuoto simplekso algoritmus lyginti bendru atveju neįmanoma norint rasti greičiausiai konverguojantį iš jų. Šių algoritmų konvergavimo efektyvumas labai stipriai priklauso nuo tikslo funkcijos ypatybių, tikslo funkcijos ir gradiento skaičiavimo sudėtingumo santykio, bei pasirinkto pradinio taško, todėl reikėtų rinktis algoritmą pagal pradinių sąlygų ypatybes.
