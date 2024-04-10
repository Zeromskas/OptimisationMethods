**Užduotis**

1. Suprogramuokite vienmačio optimizavimo intervalo dalijimo pusiau, auksinio pjūvio ir Niutono metodo algoritmus.
2. Aprašykite tikslo funkciją $f\left(x\right)=\left(x^2-a\right)^2/b-1$, čia $a$ ir $b$ – studento knygelės numerio “11\*ab” skaitmenys. Jei $b$ yra 0, susumuokite visus kortelės numerio skaitmenis, skaičiuokite rezultato skaitmenų sumą ir taip darykite tol, kol gausite vienženklį skaičių, jį ir imkite kaip b.
3. Minimizuokite šią funkciją intervalo dalijimo pusiau ir auksinio pjūvio metodais intervale $\left[0,10\right]$ iki tikslumo ${10}^{-4}$ bei Niutono metodu nuo $x_0\ =5$ kol žingsnio ilgis didesnis už ${10}^{-4}$.
4. Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius.
5. Vizualizuokite tikslo funkciją ir bandymo taškus.

Darbui atlikti pasirinkau naudoti Python programavimo kalbą dėl didelio bibliotekų kiekio, funkcijų vizualizacijos galimybių ir paprastos sintaksės. Grafikų vizualizacijai naudojausi matplotlib.pyplot biblioteka.

**Darbo eiga**
Mano studento kodas yra „**\***74“, todėl nagrinėjau funkciją:
$f\left(x\right)=\left(x^2-7\right)^2/4-1$

**Rezultatai**
Žemiau pateikiamos optimizavimo vizualizacijos su bandymo taškais ir rezultatais bei rezultatai

_Intervalo dalijimo pusiau metodas_

_Auksinio pjūvio metodas_

_Niutono metodas_

_Optimizavimo metodų rezultatai_

|                                      | Intervalo dalijimas pusiau | Auksinis pjūvis     | Niutono Metodas                            |
| ------------------------------------ | -------------------------- | ------------------- | ------------------------------------------ |
| minx                                 | 2.6457595825195312         | 2.645749407855196   | 2.6457513110648363                         |
| f(x)                                 | -0.9999999995210798        | -0.9999999999746446 | -1.0                                       |
| Iteracijos                           | 17                         | 26                  | 6                                          |
| Tikslo funkcijų/išvestinių kvietimai | 35                         | 26                  | 12(po 6 pirmos ir antros eilės išvestines) |
| Laikas s $*10^5$                     | 3.409                      | 2.789               | 1.717                                      |

**Išvados**
Remiantis duomenimis, gautais taikant intervalo dalijimo pusiau, aukso pjūvio ir Niutono metodus, akivaizdu, kad Niutono metodas funkcijos $f\left(x\right)=\left(x^2-7\right)^2/4-1$ atveju efektyviausiai konverguoja link funkcijos minimumo taško. Niutono metodas pasiekia artimiausią aproksimaciją funkcijos minimumo taškui per mažiausiai iteracijų bei funkcijų kvietimų skaičių ir per trumpiausią skaičiavimo laiką.
Tačiau Niutono metodas turi ir savo minusų tam tikrais atvejais, pavyzdžiui jei funkcijos išvestinė lygi 0, tai metodas sustoja, nors taškas nebūtinai yra funkcijos minimumas arba jei antroji išvestinė lygi 0, skaičiavimai negali būti tęsiami, nes vyksta dalyba iš 0.
Niutono metodo rezultatui ir efektyvumui daug įtakos turėjo ir pasirinktas pradinis taškas $x_0=5$. Jeigu jis būtų parinktas klaidingai, Niutono metodas galėjo nekonverguoti ir užsiciklinti tarp dviejų taškų, todėl šį metodą reikėtų naudoti atsargiai, arba kombinuoti jį su kitais metodais, norint išlaikyti greitį, neaukojant patikimumo.
