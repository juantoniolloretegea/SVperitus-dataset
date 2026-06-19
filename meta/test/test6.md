---
article:
  doi: 10.21428/39829d0b.981b7276
  elocation-id: framework-basado-en-imagenes-parametrizadas-sobre-resnet-para-identificar-intrusiones-en-smartwatches-u-otros-dispositivos-afines
author:
- Juan Antonio Lloret Egea
- Celia Medina Lloret
- Adrián Hernández González
- Diana Díaz Raboso
- Carlos Campos
- Kimberly Riveros Guzmán
- Luis Miguel Cortés Carballo
- Héctor Miguel Terrés Lloret
- Miguel Hermoso Hernando
- Instituto tecnológico virtual IAeñ™
bibliography: /tmp/tmp-20HGrGCjtRm7ZA.json
copyright:
  link: "https://creativecommons.org/licenses/by-nc-nd/4.0/"
  text: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0
    International License
  type: CC-BY-NC-ND
csl: /app/dist/server/server/utils/citations/citeStyles/apa-7th-edition.csl
date:
  day: 24
  month: 07
  year: 2021
journal:
  publisher-name: IA eñ™ --- La Biblia de la IA™ · ISSN 2695-6411 ·
    Instituto Tecnológico Virtual de la Inteligencia Artificial para el
    Español (ITVIA).
  title: IA eñ ™
link-citations: true
title: "'Framework' basado en imágenes parametrizadas sobre ResNet para
  identificar intrusiones en 'smartwatches' u otros dispositivos afines.
  (Un eje singular de la publicación \"Estado del arte de la ciencia de
  datos en el idioma español y su aplicación en el campo de la
  Inteligencia Artificial\")"
uri: "https://www.itvia.online/pub/framework-basado-en-imagenes-parametrizadas-sobre-resnet-para-identificar-intrusiones-en-smartwatches-u-otros-dispositivos-afines"
---

![](https://assets.pubpub.org/a0otzted/31628063208706.png){#nv67mq8ah7c}

[CEDRO](https://www.cedro.org/english?lng=en)

© 2021. Juan Antonio Lloret Egea et al. | *La Biblia de la IA — The Bible of AI*™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | DOI: [10.21428/39829d0b.981b7276](https://doi.org/10.21428/39829d0b.981b7276)

<div id="nota-actualizacion-sv-20260619"></div>

> **Nota de actualización — 19/06/2026.** Esta release incorpora, al cierre de la Conclusión, una actualización de continuidad titulada **12.5.- Actualización de continuidad SV — 19/06/2026**. El cuerpo histórico de la publicación queda conservado como formulación técnica de 2020–2021; la actualización final declara su continuidad con el Sistema Vectorial SV madurado en 2026, la célula ternaria `{0,1,U}`, la imagen/frame, el suceso, las matemáticas factuales y la física factual.

# Abstracto

------------------------------------------------------------------------

Se ha definido un *framework*[^1]* *conceptual y algebraicamente,
inexistente hasta ahora en su morfología, y pionero en aplicación en el
campo de la Inteligencia Artificial (IA) de forma conjunta; e
implementado en laboratorio, en sus aspectos más estructurales, como un
modelo completamente operacional. Su mayor aportación a la IA a nivel
cualitativo es aplicar la conversión o transducción de parámetros
obtenidos con lógica ternaria[@eswiki:135730214] (sistemas
multivaluados)[^2] y asociarlos a una imagen, que es analizada mediante
una red residual artificial
ResNet34[@enwiki:1019286662]^,^[@nivqpd17x9a]^\ ^para que nos advierta
de una intrusión. El campo de aplicación de este *framework* va desde
*smartwaches*, *tablets* y PC\'s hasta la domótica basada en el estándar
KNX[@eswiki:134702414].

------------------------------------------------------------------------

### ~***Abstract\ note***~

~*The\ full\ version\ of\ this\ document\ in\ the\ English\ language\ will\ be\ available\ in\ this\ *~~[*link*](https://www.openscience.online/pub/framework-based-on-parameterized-images-on-resnet-to-identify-intrusions-in-smartwatches-or-other-related-devices/draft?access=9325jcgg)~~*.*~

------------------------------------------------------------------------

![Código QR de la publicación: \'Framework\' basado en imágenes
parametrizadas sobre ResNet para identificar intrusiones en
\'smartwatches\' u otros dispositivos
afines.](https://assets.pubpub.org/s5snixyn/71627022597226.png){#nc3u5osj2xx}

Código QR de la publicación

Este marco propone para la IA una ingeniería inversa de tal modo que
partiendo de principios matemáticos conocidos y revisables, aplicados en
una imagen gráfica en 2D para detectar intrusiones, sea escrutada la
privacidad y la seguridad de un dispositivo mediante la inteligencia
artificial para mitigar estas lesiones a los usuarios finales.

Asimismo se postula el *framework* de manera que cumpla con las mayores
expectativas de ser una herramienta útil para la sociedad y el ser
humano, alineado con el «[Dictamen del Comité Europeo de las Regiones --
Libro Blanco sobre la inteligencia artificial -- Un enfoque europeo
orientado a la excelencia y la
confianza](https://op.europa.eu/es/publication-detail/-/publication/12738974-40d7-11eb-b27b-01aa75ed71a1/language-es/format-PDF/source-search)»
y que contribuya a evitar la mala *praxis* de generar cajas
negras[@eswiki:129509224]en el empleo de la inteligencia
artificial[@eswiki:135284378] haciendo de ella algo inexplicable.

La confianza y la explicabilidad en la tecnología es un objetivo a
corto, medio y largo plazo para que la sociedad no quede empeñada en
manos de tecnologías espurias que hipotecan un desarrollo social
adecuado. «Estas tecnologías han ampliado las oportunidades de libertad
de expresión y de movilización social, cívica y política, pero suscitan
a la vez graves preocupaciones»[@eswiki:135434862].

------------------------------------------------------------------------

# I.-*Framework* {#i-framework}

## 1.- Justificación de la necesidad {#justificacin-de-la-necesidad}

Existe una amplia disponibilidad de dispositivos «inteligentes» que
todos tenemos a nuestro alcance, desde cámaras fotográficas digitales,
pasando por *tablets *y *smartwatches*. El problema ocurre cuando el
desconocimiento en el manejo de estos aparatos electrónicos se extiende
a un gran porcentaje de la población [@mónicasetién2017], pues ignoran
los riesgos que pueden acarrear. Si bien es cierto que un dispositivo
electrónico es **inteligente** por funcionar de forma interactiva y
autónoma, no debemos olvidar que para que **algo** aporte beneficios y
soluciones en situaciones concretas, ese **algo** debe conocer
previamente lo que está ocurriendo. Todo esto se traduce en una única
palabra: **datos**.

Uno de los dispositivos electrónicos que más se ha puesto de moda en los
últimos tiempos es el *smartwatch*. Los *smartwatches* tienen sensores
que identifican modelos o patrones de comportamiento humano junto con
técnicas de aprendizaje automático, el teorema de Bayes, el
procesamiento de datos o el también conocido como método k de los
vecinos más cercanos [@universityofhelsinki2021]. Estos procedimientos
generan un gran volumen de información con el que pretendemos cumplir el
objetivo de precisar en los resultados emitidos. Estos sensores son muy
útiles para monitorizar la actividad humana: caminar, montar en
bicicleta, *running *y subir o bajar escaleras
[@temp_id_16995488730594066].

El uso de *smartwatches *puede suponer una grave amenaza para la
seguridad de niños y adolescentes [@isabelrubio2019]. Los fallos de
seguridad más importantes de los relojes de bajo coste se producen en
las aplicaciones y en la conexión con los servidores que almacenan los
datos. Las marcas de *smartwatch *más* *utilizadas por menores que hemos
analizado son: Carl Kids Watch, hellOO! Children's Smart Watch,
SMA-WATCH-M2 y GATOR Watch. Los problemas más recurrentes que
encontramos son: fallos en la implementación de certificados para
conexiones seguras HTTPS [@ericclausing2018] e información relativa al
registro electrónico sin cifrar [@dennishenke2018]. Sin embargo, en
dispositivos de marcas más reconocidas como Nokia [@ericclausing2018],
Samsung o Huawei [@ericclausing2018], estos problemas no ocurren con
frecuencia, ya que se realizan a través de conexiones cifradas.

En este punto nos parece interesante comparar las características que
afectan a la seguridad de las diferentes marcas de relojes. Esta es una
forma de conocer el nivel de confianza que debemos depositar en cada una
de ellas. El criterio seguido para elegir las marcas es tener en cuenta
el mayor número de ventas del mercado: Samsung, Apple, Fitbit y Garmin.

![54](https://assets.pubpub.org/fma4qgfc/31625567334457.svg){#nzq110ize91}

Crédito de imagen: Seguridad en dispositivos Samsung y Apple por Adrián
Hernández, 2021, Mangosta
(<https://mangosta.org/seguridad-en-los-dispositivos-samsung-y-apple/>)

![](https://assets.pubpub.org/yjy9unxe/01625567427088.svg){#ndu3nz45bxv}

Crédito de imagen: Seguridad en dispositivos Fitbit y Garmin por Adrián
Hernández, 2021, Mangosta
(<https://mangosta.org/seguridad-en-dispositivos-fitbit-y-garmin/>)

En la recopilación de datos, Samsung es la única marca que no compila
información *online* de menores de 13 años [@foundation_mozilla2020].
Sin embargo, esto no ocurre con Apple [@foundation_mozilla2020], Fitbit
[@foundation_mozilla2020] y Garmin [@foundation_mozilla2020], que no
hacen distinción de edad. Asimismo, todas las marcas elegidas para
nuestro estudio comparten datos con terceros para analizar métricas y
comparar resultados. De acuerdo con estas referencia, **solo en Samsung
los datos de los usuarios son vendidos o alquilados**. **Al contrario de
lo que ocurre con Apple; pues es la única de las empresas analizadas que
no comparte datos con fines de publicidad y/o márquetin**. Por tanto,
llegamos a la conclusión de que todas las marcas, al final, realizan una
recopilación de datos no anónimos aunque con ciertos puntos de
disimilitud.

## 2.- Definición algebraica y cálculo del alcance del *framework*[@eswiki:136296078] {#definicin-algebraica-y-clculo-del-alcance-del-framework}

La sistemática empleada se basa en la dualidad o binomio de parámetros
determinantes de una intrusión & imagen asociada. La determinación de
cuáles han de ser estos parámetros debe ser fruto de la experiencia en
el campo de la ciberseguridad[@eswiki:136800781]^\ ^y que más adelante
nosotros propondremos y serán expuestos.

### 2.1.-Definición algebraica {#definicin-algebraica}

Dado un número determinado de parámetros de intrusión denominado «n»,
que es una sucesión numérica de términos
$\in \N$$\land  \hspace{0.1cm} a_n=b^2 \hspace{0.1cm}  /\hspace{0.1cm}  b \geq3$,
característico para cada una de las instancias del *framework* a
determinar; dado ($\vec P_x$), compuesto por un grupo de términos o
elementos vectores axiales dependiente de «n» →($\vec P_{x(1....n)}$)
cuyo modulo \|$\vec P_{x(1...n)}$\| sólo toma los valores ternarios del
intervalo cerrado \[0,1, U\]^\[1\]^, y un número máximo de vectores de
($\vec P_x$) denominado «m» $\in \Z$ →
$ [ \vec P_{1}, \vec P_{2},\vec P_{3}...\vec P_{m}] _0^{f: {n→m}}$
determinado su valor por $m=3^n$; y dada una sucesión numérica continua
de pares de términos ordenados (x~(1...n),\ ~y~i~) que aplican
biyectivamente que un elemento en el grupo ($\vec P;x$) tiene su imagen
en el grupo ($\vec Img; y$), /
$ \forall  \hspace{0.1cm}  término  \hspace{0.1cm} x →\hspace{0.1cm}y=x  \hspace{0.1cm} _\leq m$
$\wedge \hspace{0.1cm} i=(n-1, \hspace{0.1cm} n)$, definimos a este
*framework* como:

Un **S**istema **V**ector de **intrusión **→
$\vec SV_{intrusión}= {[\vec P x _{(1...n)}, \vec Img_{y_{i}}]_0^{3^{(n)}}}$.
Que cumple que una imagen asociada, o transducida, es función de un
*array* de parámetros (p) →{p1, p2, p3, p4... p~n~}; vectorizados cada
conjunto enésimo de éstos como ($\vec P_x$) / :
$\vec Img _{y_i}={f (\vec P{_{x(1...n)} })} _0^{3^{(n)}}$, y que para
cada uno de los vectores del conjunto ($\vec P_x$) tiene una relación
biyectiva [@eswiki:134043012]^\ ^con su imagen reflejada ($\vec Img_y$).

Así $(\vec Img_y)$ es la consecuencia de la transformación lineal del
sistema de vectores ($\vec P_x$), definido éste por el *array de*
parámetros de intrusión (p), y que se construye dinámicamente
$ \forall \hspace{0.1cm}x  \hspace{0.1cm} \leq m$ mediante la siguiente
expresión:

$ \hspace{0.1cm}\vec Img{_y} _i \Leftrightarrow  [\vec P_{x2} - \vec P_{x1}, \hspace{0.1cm}\vec P_{x3}-\vec P_{x2}, \hspace{0.1cm}\vec P_{x4} - \vec P_{x3},...,\vec P_{xn} - \vec P_{x({n-1})}, \vec  P_{x1}-\vec P_{xn}] \hspace{0.1cm} \forall \hspace{0.1cm}n  \hspace{0.1cm}  \in  \hspace{0.1cm}  \mathbb N .$

$ \forall \hspace{0.1cm}  \vec Img{_y} _i \Leftrightarrow  \vec P_{xn} - \vec P_{x({n-1})}$
$/  \hspace{0.1cm} \forall  \hspace{0.1cm}  término  \hspace{0.1cm} x →\hspace{0.1cm}y=x  \hspace{0.1cm} _\leq m$
$\wedge \hspace{0.1cm} i=(n-1, \hspace{0.1cm} n)$

-   La imagen poligonal cerrada, que asociará un determinado *array *de
    parámetros intrusivos, para que ésta sea valorada por la
    Inteligencia Artificial (IA), vendrá definida por la siguiente
    expresión vectorial:

> ### $(\hspace{0.1cm} \Sigma  _{j=1} ^{j=n}\hspace{0.1cm}  (\vec Px_n-\vec Px_{(n-1)}))-(\vec Px_1-\vec Px_n)=0$ {#r7493757925}

**A) DOMINIOS** DEL *FRAMEWORK*

1\) El dominio {D~1~}
$ \forall \hspace{0.1cm}   \vec P _{x(1...n)} \in  \hspace {0.1cm}  \vec \mathbb N   \hspace {0.1cm} \land: xn \in  [0,1,U].$

2\) El dominio {D~2~} de
$  \vec Img _{y_i}={f (\vec P{_{x(1...n)} })} _0^{3^{(n)}}  \in  \hspace{0.1cm} \vec \mathbb R^2 → \ f: \mathbb N→ \mathbb R^2 .
 $

3\) El domino {D~3~} del grupo ($\vec P_x$) $ \in  \vec \mathbb N^n $.

$(\vec Px) \Leftrightarrow (\vec P_1, \vec P_2, \vec P_3,...\vec P_m)  \hspace{0.1cm} / \hspace{0.1cm}  {D _1\hspace{0.1cm}[0,1,U]:\hspace{0.1cm}  \forall \hspace{0.1cm}\vec P_{x(1...n)} \in  \hspace{0.1cm} \vec \mathbb N} \land \forall \hspace{0.1cm}\vec P_x \hspace{0.1cm} \in  \vec \mathbb N^n$

4\) El domino {D~4~}$(\vec Img_y)  \in  \vec \mathbb R^n$.

**B) COORDENADAS POLARES DEL *****FRAMEWORK***

La transformación lineal anterior de $(\vec Img_y)$ constituiría una
línea vectorial poligonal cerrada. Que en coordenadas polares, de fácil
implementación mediante gráficos radiales[^3], implica para
$\vec P _{x(1...n)} $ un sistema generador de vectores
$\vec r= |mod|_\alpha$ de valor modular (0,1,U) y de ángulo $\alpha$
cuyo valor estará comprendido entre 0º y 360º dependiendo éste del
número de parámetros usados en el escaneo de la intrusión asociados a
sus ejes, y que para el caso de n=9 parámetros, y para una instancia
determinada «x»,
$ [ \vec P_{x1}, \vec P_{x2},\vec P_{x3}...\vec P_{x9}]$, $\alpha$
tendrá un valor (o un desfase entre los vectores del sistema)
($\vec P_{x (1...9)}\alpha$) de 40º → $=\frac{360º}{9}$.

#### 2.1.1.- Naturaleza de las dimensiones del **S**istema **V**ector de **intrusión** $\vec SV_{intrusión}= {[\vec P x _{(1...n)}, \vec Img_{y_{i}}]_0^{3^{(n)}}}$ {#naturaleza-de-las-dimensiones-del-sistema-vector-de-intrusin-vec-svintrusin-vec-p-x-1n-vec-imgyi03n}

Al utilizarse aquí, como propuesta inicial de representación, gráficos
radiales para generar imágenes y usar estos ejes a modo de radios
vectores de una circunferencia en el plano separados un cierto ángulo
$\alpha$ entre ellos, la parte que nos interesa, la gráfica, se ubica
por completo en la aplicación lineal $f: \mathbb N→ \mathbb R^2 $.

Ahora bien, atendiendo a las coordenadas de cada vector y su naturaleza
algebraica, la dimensión real sería la que sigue:

1\) El grupo de vectores $\vec P x _{(1...n)}$ {Dim~1~}$\N$=1.

2\) El grupo de vectores $ \vec Img{_y} _i $ {Dim~2~}$\R$=2.

3\) El grupo de vectores $\vec P_x$ {Dim~3~}$\N$=n.

4\) El grupo de vectores $ \vec Img_y$ {Dim~4~}$\R$=n.

#### 2.1.2.- Propiedades algebraicas de $\vec P x _{(1...n)}, \vec Img_{y_{i}}$que conforman $\vec SV_{intrusión}= {[\vec P x _{(1...n)}, \vec Img_{y_{i}}]_0^{3^{(n)}}}$ {#propiedades-algebraicas-de-vec-p-x-1n-vec-imgyique-conforman-vec-svintrusin-vec-p-x-1n-vec-imgyi03n}

Las propiedades a analizar para este sistema vectorial van desde:
elemento neutro[@eswiki:131211745], elemento
simétrico[@eswiki:121459292], propiedad asociativa[@eswiki:132607301],
conmutativa[@eswiki:135524092] y distributiva[@eswiki:134872045];
pasando por el análisis de $\vec P x _{(1...n)}, \vec Img_{y_{i}}$como
grupo abeliano[@eswiki:135904908], anillo[@eswiki:133536782],
cuerpo[@eswiki:136053014] y espacio vectorial[@eswiki:136483683]... Se
propone para una siguiente revisión de esta publicación su desarrollo,
comprobación y demostración. Asimismo se omite en esta revisión en
beneficio de una mayor conceptualización general del *framework* y de su
focalización en el desarrollo efectuado en el laboratorio.

### 2.1.3.- Inferencias de la definición algebraica  {#inferencias-de-la-definicin-algebraica}

A este modelo matemático así definido puede aplicársele la teoría del
Campo del Álgebra Lineal[@eswiki:136488075]. Asimismo a los gráficos
radiales, que encierran áreas en sus polígonos irregulares definidos por
sus vértices, se les puede operar algebraicamente aplicando el
determinante de Gauss o fórmula del área de
Gauss[@eswiki:130981824]^\ ^y sus propiedades adscritas. Y también,
propiedades de la lógica ternaria aplicable y del álgebra combinacional
de Boole[@eswiki:135850713]; entre otros... Por lo que el número de
teoremas y corolarios[@eswiki:134034994] a postular para este marco, y
su aplicación en la IA y la detección de intrusiones, es motivo aún de
un estudio amplio de posibilidades y vasto en posibles aplicaciones
diferentes de las que aquí se describirán o enunciarán.

![](https://assets.pubpub.org/0hd0530u/01626132349933.svg){#nhrzdztiibo}

Crédito imagen: Ejemplo de la fórmula del área de Gauss, Wikipedia,
[Isalar](https://commons.wikimedia.org/w/index.php?title=User:Isalar&action=edit&redlink=1 "User:Isalar (page does not exist)") derivative
work: [Nat2](https://commons.wikimedia.org/wiki/User:Nat2 "User:Nat2") ([talk](https://commons.wikimedia.org/wiki/User_talk:Nat2 "User talk:Nat2")) - [Polygon_area_formula.jpg](https://commons.wikimedia.org/wiki/File:Polygon_area_formula.jpg "File:Polygon area formula.jpg"),
Mangosta (<https://mangosta.org/formula-del-area-de-gauss/>)

### 2.2.- Cálculo del alcance y sistemática de uso {#clculo-del-alcance-y-sistemtica-de-uso}

El número máximo «m» de vectores posibles con el muestreo de n=9
parámetros y lógica ternaria (0,1,U) es de
→$\ m=3^9;→ \Delta \vec r_{(n=9)}=19.683$ vectores de intrusión. Que se
irían incrementando conforme aumentáramos el número de parámetros «n» de
16, a 25, 36, etc., siguiendo una lógica de matrices cuadradas y su
propia sucesión numérica definida anteriormente. Para un número n ≤9 no
queda suficientemente justificado el uso de la IA porque cualquier
lenguaje de programación mediante un algoritmo o librería específica
podría realizar esto de forma más o menos trivial, sin embargo, cuando
n\>9 sí queda justificada por la potencia de cálculo y la rapidez[^4] en
el manejo de datos masivos que tienen actualmente los sistemas gráficos
asociados a la inteligencia artificial [@nsohyl3k9oj]de acuerdo a la
tendencia actual de los proveedores de servicios, servidores y tarjetas
gráficas, por ejemplo, como Google o IBM; entre otros. Y sin duda esta
rapidez y potencia de la IA es totalmente diferenciadora en valores de
«n» superiores a 25, porque éste ya supondría →
$\ m=3^{25}; → \Delta \vec r_{(n=25)}=19.68347.288.609.443$ vectores...,
casi un billón de vectores. Lo que otorgaría al sistema una brillante
precisión en sus estimaciones de intrusión. La metodología para la
obtención de estos parámetros se propone inicialmente que sea mediante
la captura de reglas en *logs* de IDS's[@eswiki:134851998], y el empleo
de técnicas conocidas de monitorización de sistemas (*apps*, etc.); pero
esto obviamente es flexible y abierto a otra metodología de obtención y
el *framework *lo admitiría sin mayor problema.

Los parámetros de intrusión sirven como base para construir un modelo
gráfico de positivos, negativos y de entrenamiento explícitamente
separados y ordenados en unidades contenedoras, carpetas o directorios.
Para cada nueva identidad de parámetros e imagen, una vez transferida la
imagen a la unidad contenedora asignada, la inteligencia artificial
(previamente entrenada) nos determinará si es o no es una intrusión.
Asimismo para la decisión final de ¿si es o no es un intrusión?, el
marco propone adicionar la posibilidad de que un humano afirme que lo
dictaminado por la IA sea efectivamente una intrusión, o no. Supone por
tanto la inteligencia artificial una sonda que pone en sobre aviso y
escruta todas las intrusiones vía
$\vec SV_{intrusión}= {[\vec P x _{(1...n)}, \vec Img_{y_{i}}]_0^{3^{(n)}}}$para
que finalmente sea el técnico humano quien decida. Por otro lado la
gestión de una base de datos relacional de positivos ya declarados,
anexos al sistema que integre o encapsule el marco, conjuntamente con la
actuación de la IA para los positivos que no lo están aún, permitirá
generar una base de datos de conocimiento mejorada que irá creciendo de
acuerdo al número de peticiones de los usuarios que decidan utilizarlo.

## 3.- Definiciones singulares y un ejemplo

#### 3.1.- Definición en Programación Orientada a Objetos (POO)[@eswiki:135158380] {#definicin-en-programacin-orientada-a-objetos-poo}

Al *framework* que hemos creado le podemos abstraer la idea de que
definiría una clase denominada 'Intrusión', y la herencia de esta clase
en otra determinada, definida mediante 9 parámetros, a su vez generaría
la clase denominada 'Intrusión~base9~' , y que es factible de
implementar con cualquier lenguaje de programación existente
actualmente. Para cada instancia de esa clase, obtendríamos un objeto de
$\vec SV_{intrusión}= {[\vec P x _{(1...n)}, \vec Img_{y_{i}}]_0^{3^{(n)}}}$
para su posterior clasificación como intrusión \[*True*/*False*\].

#### 3.2.- Definición de 9 parámetros {#definicin-de-9-parmetros}

Estos nueve parámetros significan una instancia del marco general
descrito anteriormente. Por lo tanto heredaría todas las características
de éste. Y donde los valores (0,1,U) especifican: apagado o no usado,
encendido o en uso e indeterminado; respectivamente.

+-------------------+------------------------+-----------------------+
| **Núm. Parámetro  | **Definición del       | **Procedimiento de    |
| **^~(n=9)~^**     | parámetro**            | obtener recomendado** |
| asociado al       |                        |                       |
| **$ \ve           |                        |                       |
| c P x _{(1...n)}$ |                        |                       |
+===================+========================+=======================+
| n=1→P~x1\ ~       | Destino de *web* (url) | Regla                 |
|                   | desconocido o no       | Sno                   |
|                   | autorizado             | rt[@eswiki:134851797] |
|                   |                        | IDS o similar         |
+-------------------+------------------------+-----------------------+
| n=2→P~x2~         | Comunicación no        | " "                   |
|                   | cifrada (Https)^\[6\]^ |                       |
+-------------------+------------------------+-----------------------+
| n=3→P~x3~         | Traspaso de datos      | " "                   |
|                   | locales a otro         |                       |
|                   | almacenamiento         |                       |
+-------------------+------------------------+-----------------------+
| n=4→P~x4~         | Uso o conexión a       | Regla                 |
|                   | BS                     | Kism                  |
|                   | SID[@eswiki:134202370] | et[@eswiki:123352703] |
|                   | no permitida o         | -WIDS o similar       |
|                   | desconocida            |                       |
+-------------------+------------------------+-----------------------+
| n=5→P~x5~         | Uso o conexión a       | " "                   |
|                   | Puerto                 |                       |
|                   | Blueto                 |                       |
|                   | oth[@eswiki:136882805] |                       |
|                   | no permitida o         |                       |
|                   | desconocida            |                       |
+-------------------+------------------------+-----------------------+
| n=6→P~x6~         | Uso o conexión a       | " "                   |
|                   | GPS[@eswiki:136677430] |                       |
|                   | no permitida o no      |                       |
|                   | autorizada             |                       |
+-------------------+------------------------+-----------------------+
| n=7→P~x7~         | Uso o conexión a       | Monitor de sistema o  |
|                   | cámara no permitido o  | similar               |
|                   | desconocido            |                       |
+-------------------+------------------------+-----------------------+
| n=8→P~x8~         | Uso de dispositivo de  | " "                   |
|                   | audio (micro /         |                       |
|                   | altavoz) no permitido  |                       |
|                   | o desconocido          |                       |
+-------------------+------------------------+-----------------------+
| n=9→P~x9~         | Monitorización de      | " "                   |
|                   | parámetros físicos     |                       |
|                   | (velocidad,            |                       |
|                   | temperatura, batería)  |                       |
|                   | con resultado anormal  |                       |
+-------------------+------------------------+-----------------------+

#### 3.3.- Un ejemplo de aplicación {#un-ejemplo-de-aplicacin}

**De forma general se da
**$\vec Img _{y_i}={f (\vec P{_{x(1...n)} })} _0^{3^{(n)}}$ ,** veamos
un ejemplo cualquiera **con 9 parámetros de una imagen, en un instante
de tiempo T1 determinado para una instancia
$x=1;→ \vec Img 1{i}={f (\vec P{_{1 \hspace{0.1cm} (1...9)} })}$
→$\vec Img 1_i= f (\vec P1_1, \vec P1_2, \vec P1_3, \vec P1_4, \vec P1_5, \vec P1_6, \vec P1_7, \vec P1_8, \vec P1_9)$.
Y la imagen gráfica a escrutar por la inteligencia artificial se crearía
a partir de la transformación lineal siguiente:

$\vec Img1{_i} \Leftrightarrow  [\vec P1_2- \vec P1_1, \hspace{0.1cm}\vec P1_3-\vec P1_2, \hspace{0.1cm}\vec P1_4 -\vec P1_3,...,\vec P1_9- \vec P1_8, \vec P1_1- \vec P1_9]$
Y en la que los vectores parciales del vector ($\vec Img 1_{i}$) se
irían construyendo dinámicamente en el sentido de las agujas del reloj a
partir de los vectores $\vec P1_{(1...9)}$ con un desfase entre ellos de
40º.

$\vec Img1{_1}= \vec P1_2- \vec P1_1;\hspace {0.1cm} \vec Img1{_2}= \vec P1_3- \vec P1_2;\hspace {0.1cm} \vec Img1{_3}= \vec P1_4- \vec P1_3;\hspace {0.1cm} \vec Img1{_4}= \vec P1_5- \vec P1_4;\hspace {0.1cm} \vec Img1{_5}= \vec P1_6- \vec P1_5;\hspace {0.1cm} \vec Img1{_6}= \vec P1_7- \vec P1_6;\hspace {0.1cm} \vec Img1{_7}= \vec P1_8- \vec P1_7;\hspace {0.1cm}\vec Img1{_8}= \vec P1_9- \vec P1_8;\hspace {0.1cm} \vec Img1{_9}= \vec P1_1- \vec P1_9$

Por lo que asignando valores, previamente escaneados, al *array* de
parámetros (p1)=(0,1,U,0,1,1,0,U.0), éstos definirán de forma intrínseca
$( \vec P1_{(1...9)} )$, y su imagen gráfica asociada $\vec Img1{_i}$ se
construiría como la figura de abajo. Donde a nivel gráfico se ha
asignado el valor «3» a las indeterminaciones «U». Y «1» ó «2» que
corresponderían a los valores binarios de (0,1), respectivamente.

![](https://assets.pubpub.org/9ubofqlj/51626256322218.svg){#n8ihhnf47m1}

Crédito imagen: Ejemplo de captura de parámetros por Juan Antonio Lloret
Egea, 2021, Mangosta (<https://mangosta.org/i_parametros-3/>)

# II.- Laboratorio del *framework* {#ii--laboratorio-del-framework}

## 4.- Implementación de los 9 parámetros {#implementacin-de-los-9-parmetros}

#### 4.1.- Destino de url desconocido o no autorizado

> log tcp \$HOME_NET any -\> !DireccionIPConfianza any (sid: 1000001;
> rev: 001;)

> log tcp any any -\> !DireccionIPConfianza any (sid: 1000001; rev:
> 001;)

La regla puede ser definida de dos maneras, una inicial en la que
utilizamos la variable **"HOME_NET"** previamente definida, en la que
vamos a especificar cuál es nuestra red, o una segunda forma en la que
no especificamos la red que estamos utilizando sino que creamos la regla
con "any" y a pesar de ser menos eficiente en cuanto a recursos, nos
aseguramos de que funcione en cualquier situación. La regla puede leerse
de la siguiente forma: "Crea un *log *cuando se utilice el protocolo TCP
desde nuestra red para enviar paquetes desde cualquier puerto a una
dirección distinta a la dirección de confianza en cualquier puerto."

#### 4.2.- Comunicación no cifrada (https) {#comunicacin-no-cifrada-https}

> log tcp \$HOME_NET any -\> any any (content:\"http\"; sid: 1000002;
> rev: 001; )

> log tcp any any -\> any any (content:\"http\"; sid: 1000002; rev: 001;
> )

La regla puede ser definida de dos formas, una inicial en la que
utilizamos la variable "HOME_NET" previamente definida, en la que vamos
a especificar cuál es nuestra red o una segunda forma en la que no
especificamos la red que estamos utilizando sino que creamos la regla
con "any". Ésta, a pesar de ser menos eficiente en cuanto a recursos,
nos aseguramos de que funcione en cualquier situación. La regla puede
leerse de la siguiente manera: "Crea un log cuando se utilice el
protocolo TCP para enviar paquetes desde cualquier puerto a cualquier
dirección y puerto con contenido HTTP".

#### 4.3.- Traspaso de datos locales a otro almacenamiento

> log tcp \$HOME_NET !puerto_confianza -\> any any(sid: 1000003; rev:
> 001;)

> log tcp any !puerto_confianza -\> any any(sid: 1000003; rev: 001;)

La regla puede leerse de la siguiente manera: "Crea un log cuando se
utilice el protocolo TCP para enviar paquetes desde cualquier puerto que
no sea el de confianza a cualquier dirección y puerto.

#### 4.4.- Uso o conexión a BSSID no permitida o desconocida {#uso-o-conexin-a-bssid-no-permitida-o-desconocida}

Para dispositivos Windows, se puede utilizar Kismet* *o bien integrarlo
en Python, utilizando el modulo subprocess* *(a partir de Windows 7) que
nos permite obtener el estado de los procesos de los dispositivos y la
respuesta que nos ofrece el sistema operativo tras introducir una
sentencia en la consola del mismo. En este caso para conocer el BSSID al
que esta conectado el dispositivo utilizaremos: "netsh wlan show
interfaces", que nos devolverá entre otros muchos datos el BSSID al que
esta conectado el equipo. Si este BSSID no es un BSSID reconocido,
obtendremos un valor de "1" a la hora de realizar el gráfico posterior
que utilizará la Inteligencia Artificial para determinar si estamos ante
una intrusión o no. Si el BSSID es reconocido, almacenaremos un valor
"0" y si por el contrario no es posible determinarlo, tendremos un valor
indeterminado en este parámetro.

Para Android, se puede utilizar **WifiInfo**, clase definida por Google
para manejar las conexiones del dispositivo [@developersandroid2021] y
que tiene como herencia la clase Objeto [@developersandroid2021]. Además
se utilizará el método getBSSID () para obtener el el BSSID, en forma de
una dirección MAC de seis bytes: XX: XX: XX: XX: XX: XX. Nuevamente si
el BSSID es reconocido, se almacena como un "0", si no lo es, se
almacena como un "1". Además, si no es posible determinar el estado de
la conexión en el dispositivo, se almacenará como indeterminado.

#### 4.5.- Uso o conexión a Puerto Bluetooh no permitida o desconocida {#uso-o-conexin-a-puerto-bluetooh-no-permitida-o-desconocida}

Para dispositivos Windows, se puede utilizar Kismet o bien integrarlo en
Python, utilizando la librería PyBluez que nos permite obtener el estado
de la conexión bluetooth.

Para Android, se puede utilizar **BluetoothProfile***** ***interfaz
(colección de métodos y constantes), definida por Google para manejar el
Bluetooth en los dispositivos Android. Además necesitaremos utilizar
otra interfaz: **ServiceListener***** ***que nos permitirá listar de
manera más rápida los estados (constantes) que buscamos:

**STATE_CONNECTING*****:*** Dispositivo en estado de conexión.
**STATE_DISCONNECTING**: Dispositivo en estado de desconexión.
**STATE_CONNECTED**: Dispositivo conectado. \
**STATE_DISCONNECTED**: Dispositivo desconectado.

Estos estados pueden parecer iguales dos a dos, la diferencia es que en
los dos primeros obtendremos el estado de nuestra conexión Bluetooth, es
decir, si tenemos activado o no el Bluetooth, y en los dos últimos
recibiremos información sobre si nuestra conexión está o no activa. Sin
embargo, un dispositivo puede tener el Bluetooth activo pero no estar
conectado a ningún otro dispositivo [@2019].

#### 4.6.- Uso o conexión a GPS no permitida o no autorizada {#uso-o-conexin-a-gps-no-permitida-o-no-autorizada}

Para dispositivos Windows se puede utilizar Kismet o bien integrarlo en
Python, utilizando la librería gpsd que nos permite obtener la posición
del GPS al ejecutar el *script*. Si no existe conexión, no obtendremos
ninguna posición y por lo tanto podremos almacenar el valor como "0".
Por el contrario, si obtenemos una posición cualquiera, almacenaremos el
valor como "1".

Para Android se puede utilizar **GnssStatus.Callback*****,*** clase
definida por Google para manejar el sistema global de navegación por
satélite en los dispositivos Android. Otra de las posibilidades era
trabajar con **GpsStatus***** ***pero no se podría monitorizar
"GLONASS", "GALILEO","BEIDOU", etc. Por otra parte, utilizaremos el
método definido **onStarted() **que nos avisa cuando GNSS se activa y
**onStopped()**, su análogo para cuando el proceso se detiene [@2019].

#### 4.7.- Uso o conexión a cámara no permitido o desconocido {#uso-o-conexin-a-cmara-no-permitido-o-desconocido}

Para dispositivos Windows se utiliza la biblioteca cv2 en Python, que
nos permite tener control sobre los dispositivos de vídeo, en este caso
para comprobar si la cámara está activa o no, al ejecutar el fichero. En
el caso de que la cámara esté *online* para el entorno de pruebas nos
aparece un mensaje como este:

![](https://assets.pubpub.org/lw0tmmyd/61626780960729.png){#n7sabd5tudv}

Crédito de imagen: Salida por consola estado del cámara online

por Adrián Hernández, 2021, Mangosta
(<https://mangosta.org/i_parametros-2/>)

Y además, almacenaremos el valor como "1" en la variable determinada
para realizar el gráfico con el resto de parámetros. Si por el contrario
la cámara está *offline*, en el entorno de pruebas nos aparece el
siguiente mensaje:

![](https://assets.pubpub.org/8mm1sv33/31626780826856.png){#nrd0pg2ql92}

Image credit: Console output offline camera status

por Adrián Hernández, 2021, Mangosta
(<https://mangosta.org/ii_parametros-2/>)

En este caso se almacenaría el valor "0" a la hora de realizar el
gráfico.

Para dispositivos Android, utilizamos **android.hardware.camera2**
[@2019] y utilizamos el *callback *de Android:
**CameraDevice.StateCallback** [@2019]que incluye el método
***o*****nOpened(CameraDevice camera)*****, ***que nos devuelve si la
cámara esta abierta o no.

#### 4.8.- Uso de dispositivo de audio (micro / altavoz) no permitido o desconocido

Para dispositivos Windows, se utiliza Python y la biblioteca PyAudio, la
cual nos permite capturar una señal de audio a través del micrófono y
posteriormente visualizar su representación temporal [@n7ox5wnzj0p]. El
objetivo es capturar la onda de audio en el instante de tiempo que
consideremos y si esa onda no es plana, el micrófono estaría activo.

![](https://assets.pubpub.org/sl9s0xqm/01626781141637.png){#n8l9dzb867j}

Crédito de imagen: Estado del micrófono mediante el uso de las ondas de
audio

por Adrián Hernández, 2021, Mangosta
(<https://mangosta.org/iii_parametros-2/>)

Para Android, se puede utilizar **AudioManager*****, ***una*** ***clase
definida por Google para manejar el micrófono en los dispositivos
Android [@2021]. Además, necesitaremos utilizar la clase Context [@2021]
y la String AUDIO_SERVICE. Asimismo, podemos comprobar desde la API 11
de Android (correspondiente a HoneyComb - Android 3.O.x) si el micrófono
está en uso, utilizando la constante definida: MODE_IN_COMMUNICATION /
MODE_IN_CALL.

Los pasos a seguir para crear la estructura serían:

1.- Utilizar getSystemService(java.lang.String)

2.- Incluir la clase Context y la String AUDIO_SERVICE:
getSystemService(Context.AUDIO_SERVICE)

3.- Incluir la sentencia creada en el paso 2 en la clase AudioManager:
(AudioManager)context.getSystemService(Context.AUDIO_SERVICE).

4.- Actualmente el método getMode asociado a AudioManager nos ofrece 5
resultados:

MODE_NORMAL: No hay llamadas ni acciones establecidas.\
MODE_RINGTONE: Hay una petición al micrófono.\
MODE_CALL_SCREENING: Hay una llamada conectada pero el audio no está en
uso. \
MODE_IN_CALL: Hay una llamada telefónica.\
MODE_IN_COMMUNICATION: Existe alguna aplicación que está realizando
comunicaciones de audio/video o VoIP.

Por tanto si el método nos devuelve un "MODE_IN_CALL" o
"MODE_IN_COMMUNICATION", tendremos el micrófono activo.

#### 4.9.- Monitorización de parámetros físicos (velocidad, temperatura, batería) con resultado anormal {#monitorizacin-de-parmetros-fsicos-velocidad-temperatura-batera-con-resultado-anormal}

Para dispositivos Windows, se utilizará Python y la biblioteca psutil,
que nos permite monitorizar y recuperar información sobre el sistema
tales como CPU, RAM, uso de disco, red o batería. Además es
multiplataforma lo que nos permitirá en un futuro integrarla sobre
cualquier sistema operativo [@n14lax7txdf].

Se puede generar el *log *utilizando solo psutil y estableciendo a
partir de qué porcentaje de utilización y durante cuánto tiempo
sostenido. Este porcentaje sería considerado un uso anormal en los
parámetros físicos: velocidad, temperatura y batería. También si
queremos monitorizar en tiempo real lo que ocurre tanto con la CPU como
con la RAM, debemos utilizar la biblioteca Matplotlib para generar
gráficos a partir de datos contenidos en listas o *arrays*.

![](https://assets.pubpub.org/6iw9zu02/71626781601028.png){#n1m5xq2z858}

Crédito de imagen: Monitorización de parámetros físicos por Adrián
Hernández, 2021, Mangosta (<https://mangosta.org/iv_parametros-2/>)

#### 4.10.- Gráficos obtenidos tras analizar los parámetros {#grficos-obtenidos-tras-analizar-los-parmetros}

Los gráficos polares que obtenemos al controlar cada uno de los
parámetros y que le permiten a la Inteligencia Artificial clasificar las
imágenes y posteriormente predecir si se trata de una intrusión o no,
siguen este estilo:

![](https://assets.pubpub.org/5gyxzxzo/51626781828904.png){#nxq5rqpsfjf}

Crédito de imagen: Gráfico polar por Adrián Hernández, 2021, Mangosta
(<https://mangosta.org/vi_parametros-2/>)

## 5.-  Diagramación y sistemática en la implementación del *framework* {#diagramacin-y-sistemtica-en-la-implementacin-del-framework}

Para el diseño, la compilación y la ejecución del conjunto del
*framework* en laboratorio cabe plantearse diferentes posibilidades y el
empleo de lenguajes de programación. Por un lado está el uso propio de
la IA respecto a su entrenamiento y clasificación de imágenes, que
denominaremos sistemática (**S1**), y que en ella se ha utilizado
Python. Por otro lado se plantea el diseño de una BD de almacenamiento y
uso de datos; tanto para dispositivos conocidos ya determinados (si son
o no son positivos en intrusión) y también por determinar, para esta
sistemática (**S2**) se ha utilizado SQL. Y por último se hace preciso
la gestión propia del entorno en su conjunto o *shell *y su ensamblado
general, para esta sistemática (**S3**) se ha utilizado Java. (El
lenguaje SQL resulta singular en la sistemática S2. Para las
sistemáticas S1 y S3 podría usarse un único lenguaje de programación a
elegir entre Python y Java, cada uno con sus ventajas y desventajas
respecto al uso de la IA y respecto a los sistemas operativos objetivos
en dispositivos *smart*).

Inicialmente plantearemos los diagramas de flujo de la lógica a emplear,
general y singular; después adicionaremos algunos elementos
complementarios como el paso a paso del uso de la IA y el diseño de la
base de datos y finalmente plantearemos la codificación esencial de los
distintos lenguajes de programación que intervienen: SQL, Python y Java.

### 5.1.- Diagramación General del *framework* {#diagramacin-general-del-framework}

En este apartado abordaremos el esqueleto del proyecto. Para ello hemos
planteado la diagramación general, dividida en tres partes: la relativa
al usuario, la base de datos y la IA.. El principal objetivo es obtener
una visión global de los procedimientos acometidos, de tal forma que
podamos entender todos y cada uno de ellos.

![](https://assets.pubpub.org/oekkq0wb/21627033917365.svg){#n1vl0uuscj9}

Crédito de imagen: Diagrama de flujo general del framework por Diana
Díaz, 2021, Mangosta
(<https://mangosta.org/diagramacion-general-framework/>)

El diagrama general ha sido diseñado con la ayuda de la aplicación de
diagramación de código abierto Drawio [@2021]. Esta diagramación, en
concreto, contiene otros dos diagramas; la conexión Java con la base de
datos y el uso de* *fast.ai* *+ Google Colaboratory, también recogidos
en la leyenda de la parte inferior del diagrama.

En primer lugar, comenzamos con la instalación de la aplicación. Al
acceder a la app, el usuario es preguntado si desea que su dispositivo
sea analizado, en caso de afirmar su respuesta, el proceso continúa, de
no ser así, la aplicación se cierra. Si el proceso continúa, el usuario
debe introducir los datos requeridos: el tipo de dispositivo, la marca y
el modelo. Asimismo, se realiza una conexión en Java con la base de
datos, de manera que esta información sea cotejada y por consecuencia,
permita comprobar si este dispositivo se encuentra entre nuestros
registros y dispone de la información suficiente para realizar el
análisis. Si está registrado, se verifica con el histórico si el
dispositivo está realizando alguna acción sin consentimiento del
usuario. Por el contrario, si no está en la base de datos, se requiere
la autorización del usuario para seguir con el proceso. En caso de que
el usuario no consienta este análisis, la aplicación se cierra
inmediatamente. Además, la inteligencia artificial se emplea en este
punto para comprobar si existe algún riesgo de intrusión. Para llevar a
cabo este proceso, se realiza una captura de 9 parámetros
predeterminados, que asignándoles un modelo preentrenado ResNet34 con
fast.ai indica si realmente hay una intrusión. Con el resultado de la
IA, un profesional analizará los datos obtenidos y decidirá si son
coherentes. Si es así, los datos se almacenan en la base de datos y
posteriormente se le comunicaría al usuario, en caso contrario, estos
datos se descartarían.

### 5.2.- Diagramación de Java {#diagramacin-de-java}

En este punto se expone la diagramación Java, designada como sistemática
(**S3**). El objetivo principal de la diagramación de Java es definir,
por un lado, cómo Java accede a la base de datos mediante el *driver*
JDBC y, por otro lado, cómo efectúa una comprobación mediante una
consulta SQL.

![](https://assets.pubpub.org/lk87xwr7/21625581227274.svg){#nbvc9g7jidz}

Crédito de imagen: Diagrama de Java

por Kimberly Riveros, 2021, Mangosta
(<https://mangosta.org/diagramacion-de-java/>)

El *driver* JDBC, por sus siglas en inglés, (Java Database Connectivity)
facilita la conexión entre un sistema gestor de base de datos (SGBD) y
cualquier *software *que trabaje con Java [@ibm2013]*. *Además del
*driver* JDBC, hemos utilizado el sistema gestor MySQL para gestionar
los archivos de la base de datos y la herramienta phpMyAdmin, disponible
en XAMPP, para manejar la administración de MySQL. También, hemos
trabajado en el entorno de Java conjuntamente con Eclipse. Eclipse es un
*software *de entorno* *de desarrollo* *integrado para conectar la base
de datos con Java [@calendamaia2014]*. *Es importante añadir que en el
diseño de la diagramación de Java hemos utilizado como herramienta base
el programa Draw.io, al igual que se ha hecho en el resto de
diagramaciones (**S1, S2 **y **S3)**.

En el siguiente apartado explicaremos cómo se realiza la conexión entre
la base de datos y Java, tanto en local como en la nube, utilizando la
máquina virtual Eclipse. Una vez instalados todos los aplicativos, se
incluye el *driver* JDBC en nuestro proyecto de Eclipse. A modo de
recomendación, es conveniente tener creada la base de datos desde el
principio para evitar posibles errores de conexión.

![](https://assets.pubpub.org/f6au3o4x/21627034201059.svg){#nx0zs1sbahk}

Crédito de imagen: Conexión a la base de datos - Java por Kimberly
Riveros, 2021, Mangosta
(<https://mangosta.org/conexion-a-la-base-de-datos-java/>)

Posteriormente definimos en Eclipse el objeto "connection" para
establecer la conexión y le indicamos la ruta del servidor junto con la
base de datos a la que queramos acceder. Nosotros hemos llamado a la
base de datos "seguridad", tanto en local como en la nube. Además es
necesario especificar el usuario y la contraseña porque de lo contrario,
no sería posible acceder a ella. Por último, iniciamos la búsqueda del
*host* y el puerto en phpMyAdmin para incluirlos en la ruta y así
realizar la conexión desde la nube.

![](https://assets.pubpub.org/ryrcm470/41627034284629.svg){#nxwjocssrxl}

Acceso al código para docentes y estudiantes:
<https://mangosta.org/conexion-a-la-base-de-datos-java001/>

Cada conexión, en local o en la nube, es independiente entre sí, es
decir, cada una se hace en una clase distinta y lo único diferente que
tiene cada clase en Eclipse es la ruta.

![](https://assets.pubpub.org/5cl6yr1z/11627035540414.svg){#nc76tz9ghk3}

Crédito de imagen: Conexión a la base de datos Java

por Kimberly Riveros, 2021, Mangosta
(<https://mangosta.org/conexion-a-la-base-de-datos-java002/>)

Finalmente una vez comprobada la conexión de la base de datos, podemos
realizar las consultas que deseemos, escribiendo en lenguaje SQL. Por
ejemplo, ejecutamos una consulta con la ayuda de los objetos,
"Statement*"* y* "*Resulset*".* Como resultado se muestra por pantalla
la tabla y el registro, entre otras, pues éstas han sido llamadas desde
Eclipse.

Este punto será ampliado en el apartado relacionado con [la codificación
Java](#codificacin-java).

### 5.3.- Diagramación de Python {#diagramacin-de-python}

La diagramación de Python está dividida en dos, por un lado, la que hace
referencia a la conexión de la base de datos con Python y, por otro, la
que alude al uso de la inteligencia artificial en Python.

#### 5.3.1 - Diagramación conexión base de datos con Python {#diagramacin-conexin-base-de-datos-con-python}

La siguiente diagramación expone la manera de conectar la base de datos
mediante el lenguaje de programación Python, definida como sistemática
(**S1**) en la plataforma Google Colaboratory.

![](https://assets.pubpub.org/a95dde3x/51627035791754.svg){#nhdi3nk6xd5}

Crédito de imagen: Diagrama de Python por Diana Díaz, 2021, Mangosta
(<https://mangosta.org/diagramacion-conexion-base-de-datos-con-python/>)

Las herramientas utilizadas para llevar a cabo este procedimiento son:
Google Colaboratory, una aplicación de Google para crear entornos de
máquinas virtuales basado en Jupyter Notebook
[@óscarmartíndelafuentesanz2019]. Jupyter, un archivo de extensión IPYNB
que combina una multitud de celdas con código o texto Markdown
[@opensciencelabs]. El conector MySQL Connector/Python está escrito en
Python y nos permite conectarnos a una base de datos externa, sin
embargo, es necesario un medio de interacción. Por esta razón, hacemos
uso del paquete PyMySQL [@recursospython2015].

El siguiente paso es conectar la base de datos con Python. En primer
lugar, accedemos a Google Colab y creamos un cuaderno nuevo, el cual, de
forma automática, se convierte en un cuaderno Jupyter. Una vez abierto,
instalamos el conector MySQL Connector/Python con "pip", un sistema de
gestión de paquetes escrito en Python [@pip2021]. Una vez instalado, lo
importamos. De igual forma, el paquete PyMySQL debe ser instalado.
Llegados a este punto, si no nos ha dado ningún error durante el
proceso, ya tenemos todo preparado para la conexión a la base de datos
desde nuestro cuaderno de Google Colab. Para conectarnos creamos una
variable en la que mediante el paquete PyMySQL, alojamos la información
de la ruta: nombre, usuario, contraseña y nombre de la base de datos a
la que nos queremos conectar. Convertimos la variable en un cursor, ya
que mediante la misma, vamos a realizar una operación de búsqueda en la
base de datos. Teniendo el cursor podemos ejecutar sobre él la consulta
que queramos y, posteriormente, imprimirla por pantalla con el resultado
obtenido. Una vez ejecutadas todas las consultas requeridas, podemos
cerrar la conexión a la base de datos.

Este punto será ampliado en el apartado relacionado con [la codificación
Python](#codificacin-python).

#### 5.3.2 - Diagramación uso de Inteligencia Artificial en Python {#diagramacin-uso-de-inteligencia-artificial-en-python}

La diagramación que se muestra a continuación maqueta la forma de
detectar intrusiones, denominada sistemática (**S3**). La finalidad de
la diagramación del uso de la Inteligencia Artificial en Python es
estudiar las intrusiones a partir de imágenes focalizadas en el IDS. En
nuestro caso, hemos elegido imágenes de gatos y tigres. Asimismo, en el
[siguiente
apartado](#paso-a-paso-en-el-proceso-de-detectar-intrusiones-con-inteligencia-artificial-resnet34-cuadernos-jupyter-y-google-colaboratory)
están detallados los pasos a seguir para detectar intrusiones utilizando
ResNet34, cuadernos Jupyter y Google Colaboratory.

![](https://assets.pubpub.org/6myif3va/71625903421863.svg){#niycivfvyap}

Crédito de imagen: Diagramación uso de la inteligencia artificial en
Python

por Adrián Hernández, 2021, Mangosta
(<https://mangosta.org/diagramacion-uso-de-la-inteligencia-artificial-en-python/>)

Para llevar a cabo este procedimiento, hemos utilizado Drawio para hacer
el diagrama, Google Drive y Google Colaboratory, que incluye el lenguaje
de programación Python. Además de estas herramientas, trabajamos con
fast.ai, esto es, una biblioteca de aprendizaje profundo que permite la
carga de modelos preentrenados como ResNet34 para una posterior
clasificación de las imágenes [@2021]. Por tanto, no es necesario
descargar ningún tipo de *software*, pues todo estos procesos los
llevaremos a cabo en la nube.

Accedemos a Google Drive para crear tres carpetas: "*train*",
*"validation*" y *"test"*. Dentro de cada una de ellas, creamos dos
subcarpetas llamadas "gato" y "tigre" en las que se agruparán las
imágenes, dependiendo del grupo al que pertenezcan.

![](https://assets.pubpub.org/zjah810k/11626516224484.svg){#nhet2os55ue}

Crédito imagen: Almacenamiento imágenes de gatos por Kimberly Riveros,
2021, Mangosta (<https://mangosta.org/gatos/>)

![](https://assets.pubpub.org/3ovdns93/41626516567773.svg){#nezw99811ys}

Crédito imagen: Almacenamiento imágenes de gatos por Kimberly Riveros,
2021, Mangosta (<https://mangosta.org/tigres/>)

Posteriormente accedemos a Google Colaboratory y en la primera celda,
indicamos la ruta en la que estará ubicado nuestro *dataset *(conjunto
de imágenes). De esta forma, podremos entrenar el modelo con esas
imágenes. Por consiguiente, creamos el modelo preentrenado con la
arquitectura RestNet34. Cuando hablamos de modelo preentrenado, nos
referimos a un modelo que permite que otros modelos obtengan resultados
avanzados sin necesidad de disponer de grandes cantidades de cómputo,
tiempo y paciencia [@enriqueblanco2021]. Esta es una forma de encontrar
la técnica de entrenamiento adecuada. Por otro lado, si queremos usar el
modelo en un futuro, no tenemos que volver a entrenarlo. ResNet34, por
sus siglas en inglés (*residual neural network)*, es un modelo
preentrenado de ImageNet. ImageNet es un *software* de reconocimiento de
objetivos visuales [@2021]. Tanto ResNet34 como ImageNet nos ayudan a
mejorar el rendimiento y optimizar los resultados en lo que a la
detección de intrusiones se refiere.

El siguiente paso es realizar un ciclo de entrenamiento con un número
determinado de épocas para entrenarlo (v[éase en el apartado referido al
proceso de detectar intrusiones con Inteligencia
Artificial](#paso-a-paso-en-el-proceso-de-detectar-intrusiones-con-inteligencia-artificial-resnet34-cuadernos-jupyter-y-google-colaboratory)),
y así la Inteligencia Artificial pueda estudiar todo el conjunto de
imágenes. Para interpretar los resultados creamos una matriz de
confusión que nos ayudará a evaluar el rendimiento de nuestro modelo de
clasificación de imágenes. Esta matriz compara los valores reales con
los predichos y así, podremos ver cómo está funcionando nuestro modelo
en la identificación de imágenes. De hecho, en la siguiente
representación gráfica podemos comprobar que la inteligencia artificial
ha fallado únicamente en una imagen, pues clasifica esa imagen como un
tigre cuando en realidad es un gato.

![](https://assets.pubpub.org/u66wz9m9/51626516802440.svg){#n7y1r6esuom}

Crédito de imagen: Respuesta Inteligencia Artificial por Kimberly
Riveros, 2021, Mangosta
(<https://mangosta.org/i_respuesta-inteligencia-artificial/>)

![](https://assets.pubpub.org/l335zn31/41626516826424.svg){#nxt9aofiu63}

Crédito de imagen: Respuesta Inteligencia Artificial (matriz de
confusión) por Kimberly Riveros, 2021, Mangosta
(<https://mangosta.org/ii_respuesta-inteligencia-artificial/>)

## 6.- Paso a paso en el proceso de detectar intrusiones con Inteligencia Artificial: ResNet34, cuadernos Jupyter y Google Colaboratory

Google Colab es un entorno de trabajo que nos permite ejecutar cuadernos
Jupyter* *en el navegador. Entre sus ventajas destacamos la necesidad de
no configurarlo previamente y la obtención de acceso gratuito a GPU's*
*(Tesla T4 o Tesla K80). Por lo tanto, ofrece la posibilidad de entrenar
y utilizar la inteligencia artificial sin emplear recursos *hardware
*propios y/o pagar una suscripción para su uso.

Un cuaderno Jupyter* *es un documento que permite ejecutar celdas de
código en vivo, texto plano, ecuaciones, etc. La estructura que siguen
estos cuadernos es una lista ordenada de entrada/salida. El nombre
Jupyter* *proviene de: **Julia + *****Python *****+ R**, que son los
tres lenguajes de programación presentes en los cuadernos Jupyter. Los
dos componentes principales de Jupyter Notebook* *son un conjunto de
núcleos (*Interpreter*) y el *Dashboard*. De igual forma, cambiando el
núcleo del cuaderno podemos ejecutar otros lenguajes desde Google Colab
como podría ser Java.

Una vez que tenemos el conocimiento suficiente acerca de los componentes
que vamos a utilizar para dar forma a nuestra inteligencia artificial,
es el momento de explicar el procedimiento sobre cómo lo vamos a llevar
a cabo.

El primer paso es preparar el entorno de Google Colab, ya que por
defecto no vamos a poder acceder sin activarlo. Para ello, desde nuestro
Google Drive* *hacemos clic* *en Google Colaboratory.

![](https://assets.pubpub.org/hqbijbo1/21625590448284.png){#n27fzaesfo1}

Crédito imagen: Proceso de detectar intrusiones con Inteligencia
Artificial: ResNet34, cuadernos Jupyter y Google Colaboratory por Adrián
Hernández, 2021, Mangosta
(<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial/>)

O bien, si no nos aparece la opción, hacemos clic* *en la siguiente URL:
[**https://colab.research.google.com/**](https://colab.research.google.com/)

Una vez estemos dentro de Google Colab, tenemos los cuadernos
predeterminados por Google* *para iniciarnos en Python* *desde la nube.
Sin embargo, también podemos crear un cuaderno en blanco para empezar a
realizar las pruebas pertinentes. Para realizar esta acción, hacemos*
*clic* *en la opción: "Nuevo Cuaderno".

![](https://assets.pubpub.org/u5hqlvst/41625590474668.png){#nqrew2t3ogd}

Image credit: Process of detecting intrusions with Artificial
Intelligence: ResNet34, Jupyter Notebooks and Google Colaboratory by
Adrián Hernández, 2021, Mangosta
(<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial001/>)

Ahora, el nuevo cuaderno creado tiene la siguiente estructura:

![](https://assets.pubpub.org/thonthtt/11625590503302.png){#n9lsvzwq8he}

Crédito imagen: Proceso de detectar intrusiones con Inteligencia
Artificial: ResNet34, cuadernos Jupyter y Google Colaboratory por Adrián
Hernández, 2021, Mangosta
(<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial002/>)

La celda que nos aparece inicialmente nos permite escribir código en
Python y ejecutarlo directamente, utilizando el botón "*Play*", situado
en la misma celda.

![](https://assets.pubpub.org/o6iodv75/41625672705476.png){#nj2sza3awdu}

Crédito imagen: Proceso de detectar intrusiones con Inteligencia
Artificial: ResNet34, cuadernos Jupyter y Google Colaboratory por Adrián
Hernández, 2021, Mangosta
(<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial003/>)

Por defecto, Google Colaboratory* *no viene configurado para utilizar
GPU's, así que debemos prepararlo. Para ello, es necesario ir a la
opción de "Entorno de ejecución", "Cambiar tipo de entorno de
ejecución".

![](https://assets.pubpub.org/grxpwdtx/41625590526112.png){#nv7rg2srw9u}

Crédito imagen: Proceso de detectar intrusiones con Inteligencia
Artificial: ResNet34, cuadernos Jupyter y Google Colaboratory por Adrián
Hernández, 2021, Mangosta
(<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial004/>)

Una vez situados en la pestaña, hacer clic* *en el desplegable con la
palabra "*none" *y reemplazarlo por "GPU*"*.

![](https://assets.pubpub.org/jkvodkca/51625590541250.png){#noypf7es0j8}

Crédito imagen: Proceso de detectar intrusiones con Inteligencia
Artificial: ResNet34, cuadernos Jupyter y Google Colaboratory por Adrián
Hernández, 2021, Mangosta
(<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial005/>)

En este momento, Google asignará una GPU* *para nuestro cuaderno
Jupyter, la cual podremos comprobar, utilizando la siguiente instrucción
en una celda de código:

![](https://assets.pubpub.org/smlajwys/71625672875145.png){#n00wvggpne2}

Crédito imagen: Proceso de detectar intrusiones con Inteligencia
Artificial: ResNet34, cuadernos Jupyter y Google Colaboratory por Adrián
Hernández, 2021, Mangosta
(<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial006/>)

Como se puede apreciar en la imagen, nos asignan una Tesla T4, aunque
podría haber sido una Tesla K80, ya que son las dos GPU's* *que Google*
*ofrece de manera gratuita. Ahora, ya tenemos configurado el entorno de
Google Colab* *para trabajar sobre él con inteligencia artificial,
aunque para entrenar nuestro modelo necesitamos crear la estructura de
carpetas que vamos a utilizar. Esto se realizará desde Google Drive para
reducir su complejidad, pero podría realizarse en un equipo local,
configurando el entorno Colab* *para ello.

Para realizar las primeras pruebas, utilizamos imágenes de gatos y
tigres, persiguiendo que la inteligencia artificial sea capaz, dada una
imagen que nunca ha visto, de determinar si se trata de una imagen de un
tigre o de un gato. La estructura inicial consta de tres carpetas, a las
que podemos nombrar como queramos, pero que por comodidad, se recomienda
atribuirles la siguiente nomenclatura:

![](https://assets.pubpub.org/jlz0kdu3/41625738992031.png){#nuodpq8m408}

Crédito imagen: Proceso de detectar intrusiones con Inteligencia
Artificial: ResNet34, cuadernos Jupyter y Google Colaboratory por Adrián
Hernández, 2021, Mangosta
(<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial007/>)

Una carpeta *Test, *atribuida a las imágenes que la inteligencia
artificial nunca ha visto y servirá para comprobar que la IA es capaz de
clasificar correctamente las representaciones gráficas. Otra carpeta
*Train*, con fines de entrenar nuestro modelo. Y, en este caso, sí que
habrá una diferenciación entre tigres y gatos, y la inteligencia
artificial sabrá en cada caso si la imagen que está visualizando es un
gato o un tigre. Una carpeta llamada *Validation *que nos servirá para
validar nuestro modelo. También habrá una diferenciación dentro de la
misma. Esta carpeta nos permitirá conocer cómo clasificaría la
inteligencia artificial la imagen y lo que es realmente dicha imagen.
Dentro de las carpetas *Train *y *Validation*, tendremos la siguiente
estructura:

![](https://assets.pubpub.org/pi8k5t2y/71625739010200.png){#n70cpuejre3}

Crédito imagen: Proceso de detectar intrusiones con Inteligencia
Artificial: ResNet34, cuadernos Jupyter y Google Colaboratory por Adrián
Hernández, 2021, Mangosta
(<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial008/>)

Y dentro de cada carpeta, imágenes correspondientes a gatos o a tigres.
Las imágenes de cada carpeta deben ser distintas, además, cuanto mayor
número de figuras utilicemos, mayor precisión tendrá la inteligencia
artificial para clasificar otras representaciones gráficas.

Una vez creada la estructura de carpetas y preparado el entorno de
Google Colab, empezamos a trabajar con la inteligencia artificial. Para
ello, ejecutamos el código referente a conectar nuestro entorno de
Google Colab con Google Drive, donde se encuentran las carpetas que
servirán a la IA desde el cuaderno creado previamente.

![](https://assets.pubpub.org/wgns4eua/61625673067959.png){#nrjmse86ovr}

Acceso al código para docentes y estudiantes:
<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificialc001/>

Una vez asociados los dos entornos, definimos qué rutas se van a
utilizar, en este caso root_dir* *y base_dir.

![](https://assets.pubpub.org/pl2fhkbm/31625673138473.png){#nshewn8da40}

Acceso al código para docentes y estudiantes:
<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificialc002/>

De igual manera, definimos el *path*, es decir, la ruta de nuestro
directorio principal a utilizar.

![](https://assets.pubpub.org/txbrb2bk/51625673177577.png){#nno285zu8nw}

Acceso al código para docentes y estudiantes:
<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificialc003/>

Para realizar el entrenamiento del modelo de inteligencia artificial es
necesario importar fastai. Restnet34 debe su nombre a "*residual*
*network*" y se refiere a una red residual que fue introducida por
Microsoft en 2015. Una vez que conocemos fast.ai, importamos la
biblioteca:

![](https://assets.pubpub.org/is4al43k/11625673261162.png){#n8xy7hr9vb8}

Acceso al código para docentes y alumnos:
<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificialc004/>

Estas tres instrucciones sirven para importar las bibliotecas fastai* *y
fastai* *vision* *completas, además del "**error_rate**" de **fastai
metrics**. "Error_rate" sirve para determinar el grado de error en
nuestro modelo entrenado, es decir, para saber si según nuestros
criterios, debemos mejorar el modelo o por el contrario, el error
obtenido es asumible y podemos utilizar el modelo.

Una vez importadas las bibliotecas necesarias, comprobamos que nuestra
configuración del cuaderno sea correcta. Para ello, imprimimos en
pantalla una imagen aleatoria utilizando el *path *que hemos definido
previamente y con las siguientes instrucciones: **open_image**(y la ruta
de la imagen utilizando la variable *path*) e img.show*().*

![](https://assets.pubpub.org/az5lhdcj/11625673319553.png){#nijdz5g60do}

Crédito imagen: Proceso de detectar intrusiones con Inteligencia
Artificial: ResNet34, cuadernos Jupyter y Google Colaboratory por Adrián
Hernández, 2021, Mangosta
(<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial013/>)
(.) Acceso al código para docentes y alumnos:
<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificialc005/>

Cuando comprobamos que la imagen se muestra correctamente, creamos los
datos (muestra de imágenes) que nuestro modelo va a utilizar. Para
empezar, vamos a definir el batch size* *o tamaño de batch, que nos
permite indicar el número de imágenes que transitamos al mismo tiempo a
la memoria. Como medida preventiva, es recomendable no utilizar un batch
size* *muy alto o podríamos causar un error de memoria en la tarjeta
gráfica y por consiguiente, el detenimiento del proceso. Para definir el
tamaño de batch*, *escribimos el siguiente código:

![](https://assets.pubpub.org/aorskhqt/01625673401540.png){#nxf14e4rzz2}

Acceso al código para docentes y alumnos:
<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificialc006/>

En este caso el número 6, indica la cantidad de imágenes transitadas a
la memoria al mismo tiempo. Una vez hemos asignado el batch size,
asignamos los datos que vamos a utilizar, en este caso imágenes. Para
ello, utilizamos la siguiente celda de código:

![](https://assets.pubpub.org/hetwxijb/21625673441651.png){#nrs83eth2ab}

Acceso al código para docentes y alumnos:
<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificialc007/>

En esta celda definimos la variable *data*, partiendo de la estructura
de carpetas que hemos creado previamente (*Train, Validation *y *Test*)
e indicando que esas son las carpetas que se tendrían que utilizar para
sus variables predeterminadas: *train, valid *y *test*.

Ya definido el conjunto de datos que vamos a utilizar, inicializamos
nuestro modelo. Antes de eso, creamos el modelo y cargamos Resnet34,***
***utilizando el siguiente código:

![](https://assets.pubpub.org/0g00s3vf/11625673495268.png){#no31tj8wmwu}

Acceso al código para docentes y alumnos:
<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificialc008/>

Utilizamos cnn_learner*** ***y le indicamos el conjunto de datos a
utilizar (*data*), el modelo que vamos a utilizar (**models.resnet34**)
y además, queremos conocer el **error_rate***** ***importado
anteriormente de **fastai.metrics*****. ***Esta línea de código, por
tanto, nos sirve para crear y cargar nuestro modelo, por lo que el
siguiente paso es entrenarlo. Para eso utilizamos:

![](https://assets.pubpub.org/og8h3rlo/01625673657619.png){#n9h8ocj3m5s}

Acceso al código para docentes y alumnos:
<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificialc009/>

El número entre paréntesis indica el número de "***epoch***" que vamos a
utilizar para el entrenamiento. Pero, ¿qué es un *epoch*? Llamamos
*epoch *o época al proceso de pasar todos los datos por la Inteligencia
Artificial. En nuestro caso, todas las imágenes de la carpeta llamada
entrenamiento pasan por la inteligencia artificial. Al realizar un
entrenamiento con 6 épocas, todas las imágenes de la carpeta *Train
*pasarán 6 veces por la IA.

![](https://assets.pubpub.org/2kbzucnu/21625673719682.png){#nbw705ats9e}

Crédito imagen: Proceso de detectar intrusiones con Inteligencia
Artificial por Adrián Hernández, 2021, Mangosta
(<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial018/>)
(.) Acceso al código para docentes y alumnos:
<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial-resnet34-cuadernos-jupyter-y-google-colaboratoryc009bis/>

Al finalizar el entrenamiento obtendremos el error_rate* *final de
nuestro modelo de entrenamiento. En el caso de la imagen superior sería
0.003165 o del 0.31%, aproximadamente. Otra de las cuestiones es conocer
para qué sirve el error_rate*.**** ***Ofrece información sobre lo
preciso que es nuestro modelo y nos permite decidir si realizar un
entrenamiento con más épocas o utilizar el modelo. Si no estamos seguros
de cuánta precisión significa un error de 0.31%, podemos imprimir una
matriz de confusión donde se ve más claro utilizando:

![](https://assets.pubpub.org/6hmgt6c1/21625673809556.png){#nylqbxdui94}

Crédito imagen: Proceso de detectar intrusiones con Inteligencia
Artificial: ResNet34, cuadernos Jupyter y Google Colaboratory por Adrián
Hernández, 2021, Mangosta
(<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial-019/>)

En esta matriz de confusión se comparan el eje de abscisas (eje X), las
predicciones que realiza la Inteligencia Artificial (gatos o tigres) y
en el eje de ordenadas (eje Y), lo que realmente es la imagen. En este
caso, la IA acierta en 331 imágenes de gatos y 299 imágenes de tigres,
fallando en 2 imágenes en las que la IA predice que son gatos cuando
realmente son tigres. Por lo tanto, el error que partiría de esta matriz
de confusión sería de → $\frac{2}{632} = 0.316% $%.

Una vez consideramos que el error es asumible, procedemos a guardar el
modelo para poder utilizarlo más adelante. Este procedimiento se realiza
con la siguiente celda de código:

![](https://assets.pubpub.org/yvr8o8cj/11625673879783.png){#n8fj4nmgmoy}

Acceso al código para docentes y alumnos:
<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificialc010/>

Entre paréntesis, indicamos la ruta y el nombre con el que vamos a
guardar nuestro modelo. Una vez que el modelo está guardado, podemos
probar su funcionamiento con imágenes que nunca ha visto la IA. Para
este proceso, utilizamos una nueva celda de código que contiene la
siguiente información:

![](https://assets.pubpub.org/7awo0nbc/31625673925603.png){#n8ypt4x60qf}

Crédito imagen: Proceso de detectar intrusiones con Inteligencia
Artificial por Adrián Hernández, 2021, Mangosta
([https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial020/)](https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial020/)
(.) Acceso al código para docentes y alumnos:
<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificialc011/>

En este punto volvemos a utilizar el modelo almacenado en *learn *y le
pasamos la imagen de la carpeta *Test*, en este caso la 520. Podemos
imprimir la imagen dentro del propio Google Colab* *para verificar que
realmente se cumple lo que la IA va a predecir en el siguiente paso.
Para imprimir la imagen se utiliza **img.show(). **Para pedirle a la
inteligencia artificial que analice la imagen que hemos cargado,
tendremos que usar la siguiente línea de código:

![](https://assets.pubpub.org/z2gf5v1t/31625673976123.png){#nnjcvwpiwef}

Crédito imagen: Proceso de detectar intrusiones con Inteligencia
Artificial por Adrián Hernández, 2021, Mangosta
(<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificial021/>)
(.) Acceso al código para docentes y alumnos:
<https://mangosta.org/proceso-de-detectar-intrusiones-con-inteligencia-artificialc012/>

En este caso, volvemos a realizar una llamada a nuestro modelo con
*learn *y utilizamos predict(img) para utilizar el modelo entrenado. El
resultado en este caso nos lo ofrece como tensor(0)* *para los gatos y
emplea tensor(1)* *para los tigres. Además entre corchetes nos da la
probabilidad de que en este caso sea un tigre (99.9%).

## 7.- Creación y estructura de la base de datos {#creacin-y-estructura-de-la-base-de-datos}

Se ha creado una base de datos atendiendo a la necesidad de recoger los
datos que ofrecen los *smartwatches* u otros dispositivos afines para
comprobar si todos estos datos son autorizados y conocidos por el
usuario o por el contrario, se trata de un uso no autorizado. Para ello,
tenemos en cuenta dos factores: los datos que se necesitan para poder
acceder a la información del usuario y los datos que entrañan un riesgo
por acceder sin consentimiento. En este sentido, centramos el foco de
atención en los datos que recogen los* smartwatches*, ofreciendo una
tabla adicional (TSalud). 

La herramienta utilizada, al igual que en los diagramas anteriores, es
Drawio. También hemos usado el lenguaje SQL así como MySQL y
PhpmyAdmin. 

Dos de los pilares fundamentales de esta base de datos son la
importancia de los booleanos y la lógica trivalente, sobre la que
hablaremos más adelante. ¿Pero para qué valen los campos booleanos? ¿Por
qué hemos decidido emplearlos en nuestra base de datos? fundamentalmente
para encontrar información de calidad en el menor tiempo posible y
realizar búsquedas combinadas de varios términos [@2014].

Para clarificar posibles dudas sobre la base de datos, explicamos el
diseño y la estructuración de las 5 tablas. La primera tabla y principal
es "TDispositivo". Esta tabla se compone de 3 campos que recogen el ID
(número identificativo y que se encuentra en todas la tablas como hilo
conductor), el nombre de la marca (varchar) y el modelo (varchar). La
segunda tabla "TTipoDispositivo" dispone de 6 campos: ID, y otros 5
campos booleanos (*smartwatch*, PC portátil, PC sobremesa, *tablet* y
*smartphone*) que responderán con verdadero o falso en función del tipo
de dispositivo del que se trate. La tercera tabla "TAccesoNoAutorizado"
se compone de 4 campos: ID y otros 3 booleanos (cámara, micrófono y
GPS). En esta tabla se pretende conocer si el dispositivo tiene acceso a
alguno de estos 3. La cuarta tabla "TSalud" recoge un total de 8 campos:
el ID y siete booleanos, (frecuencia cardíaca, sueño, registro
automático de ejercicio, estrés, nivel de oxígeno, ciclo menstrual y
pasos). Se pretende que esta tabla nos informe sobre la información que
recoge el dispositivo. La quinta y última tabla es "TDeteccion" y tiene
tan sólo dos campos: ID y un booleano (positivo). Esta tabla es de gran
importancia porque en ella se almacenará, tras comprobar el resto de
datos de las otras tablas, si el dispositivo es positivo o no, es decir,
si tiene o no una intrusión.

**Diagrama entidad - relación**

![](https://assets.pubpub.org/jczr0eqd/31625578022603.png){#nezih2sai8y}

Crédito imagen: Diagrama entidad-relación por Diana Díaz, 2021, Mangosta
(<https://mangosta.org/diagrama-entidad-relacion/>)

Como podemos apreciar en la imagen este diagrama se compone de tres
elementos fundamentales:

● Entidad, representado como rectángulos que muestran los nombres de
nuestras tablas. Por ejemplo: TAccesoNoAutorizado.

● Atributos, con forma ovalada, definen las características de la
entidad. Siguiendo el ejemplo, aquí las vemos representados por nID,
lCamara, etc).

● Relaciones, con forma romboide, muestran las conexiones entre unas
entidades y otras. En este caso, la conexión entre una entidad y otra
sería: TDispositivo tiene TAccesoNoAutorizado). 

**Lógica trivalente**

Para el diseño de la base de datos nos hemos centrado en la velocidad de
las consultas, ya que es fundamental para un buen desarrollo del
proyecto. Por este motivo se utilizan campos booleanos. 

La lógica bivalente distingue dos valores: verdadero o falso,
representados por 1 y 0 respectivamente
[@dr.omarfélixcampohermosorodríguezetal.2015]. En este caso, iremos más
allá y aplicaremos la lógica ternaria o trivalente, es decir, un sistema
lógico en el que se presentan 3 valores: verdadero, falso o
indeterminado. El tercer valor se interpreta como la posibilidad de que
algo no sea ni verdadero ni falso, sino indefinido. En este contexto, el
indicador categorizado como indeterminado, pues muestra ausencia de
valor, se representa así: .

**Modelo Físico**

Una vez visualizado el diseño y analizada la estructura de las tablas,
estudiamos la base de datos desde el modelo físico, en el que observamos
que la primary *key* de todas las tablas es nID.

![](https://assets.pubpub.org/onl3fq5t/61625578104797.png){#nzuedy33pyd}

Crédito imagen: Modelo físico por Diana Díaz, 2021, Mangosta
(<https://mangosta.org/modelo-fisico-2/>)

**Uso de SQL y su sistema de gestión de base de datos**

SQL2 (*Structured Query Language *o lenguaje de consulta estructurada)
pasó a ser el estándar del Instituto Nacional Estadounidense de
Estándares (ANSI) en 1986 y de la Organización Internacional de
Normalización (ISO) en 1987 [@2021]. Ha adquirido tanta popularidad por
ser un lenguaje no procedimental, es decir, especifica qué quiere pero
no cómo ni dónde conseguirlo y es relacionalmente completo, pues permite
la realización de cualquier consulta de datos [@1998]. 

Ahora que ya sabemos cómo funciona SQL, podemos hablar del sistema de
gestión de base de datos (SGBD) que hemos utilizado. Para el desarrollo
de esta base de datos hemos decido usar en primera instancia MySQL. Se
trata de un SGBD relacional de código abierto. Se entiende por código
abierto (*open source*) a un modelo de desarrollo de *software,* basado
en la colaboración abierta que se enfoca más en los beneficios prácticos
como es el acceso al código fuente [@temp_id_8920240747831845], lo que
lo hace accesible y práctico. Por su extendido uso, es una opción fiable
y estandarizada. Por otra parte, SQLite* *[@2021] es de igual manera un
motor de base de datos con SQL integrado, pero su principal ventaja es
que no necesita un servidor para funcionar. Por este motivo, resulta
bastante atractivo para trabajar con aplicaciones como es nuestro caso.
Otra de las ventajas es el espacio que ocupa en el disco duro (\< 500kb)
y lo que hace factible que la base de datos sea gestionable dentro del
propio dispositivo en lugar de en nuestro servidor. 

Pero, ¿qué lo hace destacar frente a otras opciones como SQLite?  La
base de datos ha sido diseñada en su mayoría con campos *booleanos*. Sin
embargo, SQLite no dispone de esta opción. Entre sus clases de
almacenamiento la única opción posible sería la conversión de
*booleanos* a *integer*,* *ralentizando la base de datos. Asimismo se
trata de un sistema orientado a funcionar con poco tráfico, por lo que
si introducimos una gran cantidad de datos, quizás su sistema no fuera
todo lo eficiente que necesitaríamos. Por lo que consideramos mejor
continuar con el uso de MySQL*,* así como de nuestro servidor. 

**Representación de los de datos**

Para abordar este tema vamos a hablar sobre Ckan y Dkan. Se trata de
herramientas para la gestión de datos dentro de la *web*. Su éxito se
debe a que ambas son plataformas de código abierto, libre y gratuito. La
principal diferencia es que DKAN es una versión de CKAN desarrollada en
Drupal [@2021].

![](https://assets.pubpub.org/zec01diq/11625578194737.png){#nydgogns19p}

Crédito de imagen: Instantánea de Dkan, 2021, Autoría de National Health
Countil: <https://getdkan.org/>

Pero, ¿qué es drupal? Drupal es un *software* de gestión de contenidos
(CMS), configurable que permite múltiples servicios como publicación de
encuestas, foros, artículos e imágenes [@2021]. De igual forma es un
sistema dinámico que permite almacenar los datos en una base de datos y
editarlos en un entorno web.

![](https://assets.pubpub.org/jnr1rvsi/51625578254170.png){#ntlj2wq85sy}

Crédito de imagen: Instantánea de Drupal, 2021, Autoría de Drupal:
<https://www.drupal.org/>

Ahora que hemos visto que ambos son similares pero DKAN es una versión
*a priori *superior, consideramos más interesante el uso de esta
plataforma. Es necesario destacar que otro factor a tener en cuenta es
que CKAN tiene un consumo muy exigente de *hardware*, así como una
gestión ineficiente de seguridad tanto en usuarios como en recursos.
Consideramos importante el uso de una de estas plataformas para poder
ofrecer al usuario una perspectiva más clara de los datos y una
transparencia absoluta. Por esta misma razón, es una plataforma usada
por muchos gobiernos [@2021], como el de Australia o el de Canadá, entre
otros, así como instituciones sin ánimo de lucro.

## 8.- Codificación básica del *framework *en SQL, Python y Java {#codificacin-bsica-del-framework-en-sql-python-y-java}

### 8.1.- Codificación SQL {#codificacin-sql}

Para crear la base de datos hemos utilizado el código SQL. Como
apreciamos, necesitamos usar UTF-8, un formato de codificación de
caracteres* *Unicode e *ISO* 10646 [@2021]. El motivo de su uso es para
detectar si hay palabras registradas en la base de datos que contengan
caracteres especiales como el **uso de la Ñ,** por ejemplo en la palabra
**sueño**. Por otra parte la tabla TDispositivo (la última en el código)
es la que presenta las claves foráneas y así ser el punto de unión del
resto de tablas.

![](https://assets.pubpub.org/zj4ucxwz/51627036140694.jpeg){#nkae8itfery}

Crédito de imagen: Codificación SQL por Diana Díaz, 2021, Mangosta
(<https://mangosta.org/iii_codificacion-sql/>) (.) Acceso al código para
docentes y alumnos: <https://mangosta.org/codificacion-sql001/>

![](https://assets.pubpub.org/pdv53nz3/61627036795988.jpeg){#nwb4987fqzl}

Crédito de imagen: Codificación SQL por Diana Díaz, 2021, Mangosta
(<https://mangosta.org/iv_codificacion-sql/>) (.) Acceso al código para
docentes y alumnos: <https://mangosta.org/codificacion-sql002/>

### 8.2.- Codificación Java {#codificacin-java}

En este apartado se añade el código Java [@2021] con el que hemos
accedido a la base de datos llamada "seguridad", así como el resultado
de hacer una consulta en lenguaje SQL. En primer lugar, importamos la
librería java.sql para usar la base de datos desde Eclipse:

![](https://assets.pubpub.org/owyoi87v/01627037225052.svg){#n70dx683oos}

Crédito de imagen: Codificación Java por Kimberly Riveros, 2021,
Mangosta (<https://mangosta.org/viii_codificacion-java/>) (.) Acceso al
código para docentes y estudiantes:
<https://mangosta.org/codificacion-java/>

Más adelante, es necesario asegurarnos de que el *driver *JDBC esté
debidamente conectado. A continuación, establecemos la conexión con la
base de datos por medio de estas instrucciones:

![](https://assets.pubpub.org/p7r3aold/31627037492712.svg){#nc4z15wjcfz}

Crédito de imagen: Codificación Java por Kimberly Riveros, 2021,
Mangosta (<https://mangosta.org/ix_codificacion-java/>) (.) Acceso al
código para docentes y estudiantes:
<https://mangosta.org/codificacion-java001/>

La clase DriverManager tiene un método **String **que contiene la ruta
de la base de datos. Es importante recordar que para ello hemos
utilizado el conector JDBC para MySQL que instalamos en el apartado
referente a la diagramación de Java. Adicionalmente, lo hemos probado en
el servidor de base de datos de nuestro ordenador (*localhost*) y en la
nube, cambiando la ruta de la base de datos.

![](https://assets.pubpub.org/cshm9cw3/31627037871710.svg){#nvzt4xnqbrl}

Crédito de imagen: Codificación Java por Kimberly Riveros, 2021,
Mangosta (<https://mangosta.org/x_codificacion-java/>) (.) Acceso al
código para docentes y estudiantes:
<https://mangosta.org/codificacion-java-002/>

Por defecto, el servidor MySQL abre el puerto 3306. Es necesario
conectarse a este puerto si queremos consultar la base de datos que
hemos creado. Por consiguiente, creamos el objeto "Statement". Para
ello, seguimos el paso mostrado en la siguiente figura:

![](https://assets.pubpub.org/htuxv3y7/21627038019469.svg){#nbqntq9dofi}

Crédito de imagen: Codificación Java por Kimberly Riveros, 2021,
Mangosta (<https://mangosta.org/xi_codificacion-java/>) (.) Acceso al
código para docentes y estudiantes:
<https://mangosta.org/codificacion-java-003/>

Asimismo, el objeto "Resulset" nos permite obtener los resultados de la
consulta. En nuestro caso, nos mostrará todos los registros de la tabla
demandada, es decir, TDispositivo:

![](https://assets.pubpub.org/muv0jzkx/21627038200555.svg){#nlditt4u3nm}

Crédito de imagen: Codificación Java por Kimberly Riveros, 2021,
Mangosta (<https://mangosta.org/xii_codificacion-java/>) (.) Acceso al
código para docentes y estudiantes:
<https://mangosta.org/codificacion-java-004/>

Ahora, es necesario utilizar el bucle "while" y la variable
"miResultset" para obtener todos los resultados de nuestra consulta.

![](https://assets.pubpub.org/0bzjn5x0/01627038401615.svg){#nihg9dxdw8l}

Crédito de imagen: Codificación Java por Kimberly Riveros, 2021,
Mangosta (<https://mangosta.org/xiii_codificacion-java/>) (.) Acceso al
código para docentes y estudiantes:
<https://mangosta.org/codificacion-java-005/>

En caso de no establecer la conexión de la base de datos en eclipse, al
ejecutar se mostrará por pantalla: "No funciona". Realizados todos los
pasos, finalmente obtenemos la tabla con los registros que hemos
consultado:

![](https://assets.pubpub.org/3k3p56y3/61627038571730.svg){#n9150en9blq}

Crédito de imagen: Codificación Java por Kimberly Riveros, 2021,
Mangosta (<https://mangosta.org/codificacion-java-2/>)

### 8.3.- Codificación Python {#codificacin-python}

En este apartado se añade el código Python que hemos utilizado para
acceder a la base de datos llamada "seguridad", así como el resultado de
hacer una consulta en lenguaje SQL. En primer lugar, debemos instalar el
conector mysql-connector-python, un *driver* para comunicarse con
servidores MySQL [@2021].

![](https://assets.pubpub.org/wh9bwq66/71627038784686.jpeg){#niu56lzp8ph}

Crédito de imagen: Codificación Python por Kimberly Riveros y Diana
Díaz, 2021, Mangosta (<https://mangosta.org/i_codificacion-python/>) (.)
Acceso al código para docentes y alumnos:
(<https://mangosta.org/ii_codificacion-python/>)

Seguidamente, realizamos el mismo proceso con PyMySQL, otro paquete para
la interacción con bases de datos MySQL. Y, una vez instalado, lo
importamos.

![](https://assets.pubpub.org/9rg2zmi8/41627038978912.jpeg){#nngqfijeyyp}

Crédito de imagen: Codificación Python por Kimberly Riveros y Diana
Díaz, 2021, Mangosta (<https://mangosta.org/iii_codificacion-python/>)
(.) Acceso al código para docentes y alumnos:
(<https://mangosta.org/iv_codificacion-python/>)

![](https://assets.pubpub.org/uh3sh5vw/41627039441931.jpeg){#npnaru8b80e}

Crédito de imagen: Codificación Python por Kimberly Riveros y Diana
Díaz, 2021, Mangosta (<https://mangosta.org/x_codificacion-python-2/>)
(.) Acceso al código para docentes y alumnos:
(<https://mangosta.org/iv_codificacion-python/>)

Teniendo ya los paquetes necesarios, nos conectamos a la base de datos
"seguridad". Para ello, creamos una variable llamada "miConexión" y
mediante PyMySQL, almacenamos la ruta de la base de datos, el usuario,
la contraseña y el nombre de la base de datos. En definitiva, una serie
de información, necesaria para establecer la conexión con la base de
datos.

![](https://assets.pubpub.org/o8okcecj/21627111637287.jpeg){#nk40id2bivy}

Crédito de imagen: Codificación Python por Kimberly Riveros y Diana
Díaz, 2021, Mangosta (<https://mangosta.org/xi_codificacion-python/>)
(.) Acceso al código para docentes y alumnos:
(<https://mangosta.org/v_codificacion-python/>)

El siguiente paso es convertir esta variable en un cursor. Para eso,
ejecutamos el cursor con la consulta que deseemos realizar.

![](https://assets.pubpub.org/zl19ca89/71627112096520.jpeg){#nqmc4ia885m}

Crédito de imagen: Codificación Python por Kimberly Riveros y Diana
Díaz, 2021, Mangosta (<https://mangosta.org/xii_codificacion-python/>)
(.) Acceso al código para docentes y alumnos:
(<https://mangosta.org/vi_codificacion-python/>)

![](https://assets.pubpub.org/6j2wxpgi/11627112343971.jpeg){#n7vlkqwyc6d}

Crédito de imagen: Codificación Python por Kimberly Riveros y Diana
Díaz, 2021, Mangosta (<https://mangosta.org/xiii_codificacion-python/>)
(.) Acceso al código para docentes y alumnos:
(<https://mangosta.org/vii_codigo-python/>)

Ya, para terminar, imprimimos por pantalla el resultado de la consulta.
Y, una vez acabado el trabajo en la base de datos, cerramos la conexión.

![](https://assets.pubpub.org/d5zmlpny/21627112638078.jpeg){#njunkr5zawe}

Crédito de imagen: Codificación Python por Kimberly Riveros y Diana
Díaz, 2021, Mangosta (<https://mangosta.org/xiv_codificacion-python/>)
(.) Acceso al código para docentes y alumnos:
(<https://mangosta.org/viii_codificacion_python/>)

![](https://assets.pubpub.org/9l3y2l3v/11627112953790.jpeg){#nhgxc9f9u9d}

Crédito de imagen: Codificación Python por Kimberly Riveros, 2021,
Mangosta (<https://mangosta.org/x_codificacion-python/>)

![](https://assets.pubpub.org/u7k6giww/51627113251765.jpeg){#n6xca97js99}

Crédito de imagen: Codificación Python por Kimberly Riveros y Diana
Díaz, 2021, Mangosta (<https://mangosta.org/xv_codificacion-python/>)
(.) Acceso al código para docentes y alumnos:
(<https://mangosta.org/ix_codificacion-python/>)

# 9.-  *Interfaces*

Usaremos éstas para el *front-end*[@eswiki:131027640]* *de la aplicación
(UI / UX)[@eswiki:125607149] o la parte interactiva donde el usuario
interactúa con su aplicación y donde todas las entradas se dan a través
de esta capa. La usabilidad y el diseño del entorno de las *interfaces
*en los distintos modos de funcionamiento M1, M2 y M3 (que se definen
más adelante, en el pto 10.2) deben poder permitir un control parental y
de gestión de dispositivos suficiente. El diseño de la *interface *es un
elemento clave para un uso práctico y solvente del *framework*.

#### 9.1.- Kivy

Kivy[@enwiki:1020139848] técnicamente es sólo otra biblioteca de
Python. Pero no es una cualquiera. Es un marco para crear *interfaces
*de usuario que funciona en múltiples plataformas como Android, iOS,
Windows, Linux y macOS. Puede pensarse también como una alternativa a
React Native[@eswiki:136275946], Flutter[@eswiki:137059439],
Solar2D[@ncf29nymasr], etc.

Kivy fundamentalmente es para los amantes de Python y el *Machine
Learning*. Con la biblioteca Kivy la opción más acertada es usar
Conda[@eswiki:134327479]. Instalar Kivy con Conda es fácil:
«`conda install kivy -c conda-forge`». Posteriormente podremos compilar
una aplicación para iOS o Android a partir del código
fuente[@eswiki:137023172] y ejecutarla en un simulador para poder
visualizar su aspecto y resultado final.

#### 9.2.- Klotin

Kotlin[@eswiki:136347047] es un lenguaje de programación de
tipado[@eswiki:134202100] estático que corre sobre la máquina virtual de
Java[@eswiki:133005440] (JVM) y que también puede ser
compilado[@eswiki:133310275] a código fuente de JavaScript. Aunque no
tiene una sintaxis compatible con Java, Kotlin está diseñado para
interoperar con código Java y es conocido por ser utilizado en la
creación de aplicaciones de Android.

#### 9.3.- Elementos sociales y legales en el diseño de las *interfaces* {#elementos-sociales-y-legales-en-el-diseo-de-las-interfaces}

Lo que sigue son indicaciones específicas a la hora de codificar y
desarrollar los entornos gráficos y de comunicación con los usuarios de
este *framework*. Son premisas que en el inicio deben estar siempre
presentes para los desarrolladores para evitar lesivas modificaciones
técnicas futuras en los entornos finales implementados. El marco no debe
olvidar nunca su mayor objetivo: proteger en el mayor de los ámbitos y
favorecer la pluralidad social.

1.   Se deberá atender en su mayor extensión posible a criterios
    conceptuales y de uso en la igualdad de género[@eswiki:137034315] y
    accesibilidad[@eswiki:136463544] así como poner énfasis en evitar
    todo tipo de sesgo[@eswiki:134598719].

2.  El leguaje particularmente dirigido a menores de edad deberá ser
    cuidadosamente estudiado para un uso adecuado.

3.  El cumplimiento en la normativa de protección de
    datos[@eswiki:134505254] y otros que le resulten de aplicación
    deberá ser un imperativo presencial.

4.  En la medida de lo posible se debe proporcionar suficiente
    información educacional sobre ciberseguridad e inteligencia
    artificial.

# III.- Estadios y modos aplicables al *framework * y directrices de requerimientos mínimos {#iii--estadios-y-modos-aplicables-al-framework-y-directrices-de-requerimientos-mnimos}

La caracterización en estadios y modos de este marco se propone para
definir la infraestructura de sistemas y asegurar el nivel de
procesamiento adecuado y su velocidad para la ejecución en los distintos
dispositivos *smart* del mercado, así como para la descripción
generalizada de todos los instrumentos y herramientas asociadas.

## 10.1.- **Estadios**

###  10.1.1.- **Estadio 1 (E1)**: modo laboratorio y aprendizaje de la IA {#1011--estadio-1-e1-modo-laboratorio-y-aprendizaje-de-la-ia}

Es en este estadio donde caben configuraciones y ajustes básicas y
avanzadas. Las distintas configuraciones de marcos y modelos nos
ayudarán a optimizar y mejorar el resultado para que posteriormente éste
y su experiencia asociada sea aplicado al estadio (E2), o modo de
ejecución de la IA.

Para entrenar a la inteligencia artificial podemos partir desde cero o
realizar una transferencia de conocimientos con un modelo entrenado
previamente. También podemos plantear** modelos** específicos para las
imágenes, para lo que ResNet nos ofrece en general resultados muy
aceptables en la proporción de aciertos en una clasificación dada,
*accuracy*[@eswiki:134476868], o tasa de aciertos en la predicción.
Asimismo podemos usar diferentes **marcos**, donde los más conocidos son
Pytorh, Tensorflow, Fastai y Keras... Fastai es nuestro marco por
defecto.

### 10.1.2.- **Estadio 2 (E2)**: modo de ejecución de la IA {#estadio-2-e2-modo-de-ejecucin-de-la-ia}

Es el fruto del estadio E1. Este estado se define para un modelo
entrenado y guardado para su ejecución. No debe admitir configuraciones
avanzadas algunas.

## 10.2.- **Modos**

Los modos son los distintos sistemas de trabajo o maneras de operar que
pueden ser aplicados a este *framework* de cara a los diferentes
dispositivos inteligentes a los que les resulta de aplicación.

### 10.2.1.- **Modo 1(M1)**: modo autónomo o *standalone* {#modo-1m1-modo-autnomo-o-standalone}

Le resulta de aplicación el estadio E2. Su objeto de definición es que
éste pueda ser descargado y ejecutable como cualquier otra
app[@eswiki:136515532] del mercado. En él se ejecutarán mayoritariamente
*smartphone*, *tablets* y PC's. Se recomienda compatibilidad total del
modo M1 para los sistemas operativos Android 11 o superior; iOS 14.5.1 o
superior; sistema operativo Windows 10 o superior o MAX OS X 10.15 o
superior. Las características *hardware* mínimas serán las recomendadas
por los fabricantes de éstos.

### 10.2.2.- **Modo 2 (M2)**: modo enlazado o esclavo de otro dispositivo

Este modo se concibe para el emparejamiento o vinculación de como mínimo
dos dispositivos con tecnologías compatibles del tipo Bluetooth, WiFi u
otro mediante una app o un *software* satélite complementario para este
fin. Aquí es donde mayoritariamente se emplazarán la mayoría de los
*smartwatches* actuales, referenciados en el punto. 11.1x. Los
requerimientos mínimos aconsejados de *hardware *para el despliegue del
*framework *en modo M2 son: 4GB de memoria interna de almacenamiento,
512MB de RAM y Bluetooth 4.0.

### 10.2.3- **Modo 3 (M3)**: modo servidor o laboratorio de entrenamiento y aprendizaje

Concebido para operar principalmente en el estadio E1. Se concibe en
general el modo M3 para el diseño y gestión de la IA, así como el modo
que embebe y gestiona el** **modo M1** **y el modo M2 de todos los
dispositivos relacionados en torno a él. Éste es propio de una
infraestructura Cliente-Servidor[@eswiki:136561444]. En base a la
naturaleza de su ejecución establecemos dos clases:

#### A) Modo 3A: computación en la nube {#a-modo-3a-computacin-en-la-nube}

Análogo al sistema que nosotros hemos planteado en laboratorio\...
También puede ser implementado mediante una infraestructura *ad
hoc*[@eswiki:134602116]*, *propia de un proveedor de servicios del
*framework, *y asumir los gastos inherentes a su uso y despliegue. AWS
de Amazon, Google Cloud[@ndaf0crf7oy], Azure[@nst1n6bljg8]u otros son
posibles candidatos para este fin. Para la gestión completa del entorno
adicionalmente se ha de implementar un servidor XAMPP[@eswiki:136980231]
o similar en un *hosting* dedicado[@eswiki:129371461] y adecuar los
servicios para *Servlets *de Java[@eswiki:130748486] para la completa
operatividad*. *Para el modo 3B los requerimientos *hardware* han de
considerar como mínimo los usados en nuestra configuración gratuita en
laboratorio para garantizar un resultado satisfactorio de ejecución de
la IA, así como los indicados por los fabricantes del *software*
asociado a éste.

#### B) Modo 3B:  computación en local {#b-modo-3b-computacin-en-local}

Para poder trabajar en este modo podemos efectuar una instalación
local[@nyxzw3s03oq] con fastai y Anaconda o Miniconda bajo sistema
operativo Linux o Windows. Asimismo para la gestión propia de la BD se
ha de instalar Mysql o similar. Y Java JDK[@eswiki:127612910] para el
desarrollo y ejecución de la codificación en Java.

Para este modo 3B* *el *hardware* ha de ser más específico y exigente,
aunque no debería exceder los 2.500 ó 3.000 euros a precio actual de
mercado para una configuración óptima de un entorno de producción. Debe
ser capaz de ejecutar un *software* similar a Anaconda Enterprise 4 ó
5[@ng5s16bgqe5]. (Los requerimientos son CPU: 2 x 64-bit 2.8 GHz 8.00
GT/s CPUs; RAM: 32 GB (o 16 GB de 1600 MHz DDR3 RAM); 300 GB de
almacenamiento en disco y acceso a Internet). Se aconseja memoria RAM de
64 GB y un disco duro de característica similares o superiores a 970 EVO
Plus (1TB) de Samsung para todo el conjunto que supone el Modo 3B.

La GPU[@eswiki:136789325] es el componente que realizará la mayoría de
cálculos lentos y pesados en el proceso de entrenar a una red
convolucional[@eswiki:133245872]. Mayoritariamente estos cálculos son
multiplicaciones de matrices, convoluciones y funciones de
activación[@eswiki:135456532]. El *hardware *proporcionado por NVDIA,
por ejemplo, el modelo 2080 Ti[@nlv8u3nn8lv] con 13.45 TFLOPs y 11 GB de
memoria GDDR6 es una base sólida. Para la CPU la marca Intel es una
opción ineludible. La familia i7, el i7-10700k, puede ser una elección
garante.

# IV.- Campo de aplicación {#iv--campo-de-aplicacin}

Los entornos donde el marco puede ser implementado generarán
especificaciones propias para cada entorno. Principalmente
caracterizadas por el *hardware, *en la capa del modelo
OSI[@eswiki:136866499] que se opere, su sistema
operativo[@eswiki:136739718] y su conectividad a una red determinada e
Internet, y la conexión entre dispositivos propiamente dicha. Se debe
prestar una atención importante a la velocidad de ejecución del
*framework*, por lo que los procesos aplicables deben ser los más
imprescindibles y livianos que resulte posible y la velocidad aquélla
más óptima que pueda alcanzarse. Todo ello en el mejor balanceo de
rendimiento de consumos en general y tomando en cuenta las capacidades y
la morfología donde pretenda emplearse. Signifiquemos a continuación
algunos de estos entornos. Donde efectuaremos descripciones y propuestas
de *software* y de *hardware*, denotando que ni éstas son únicas ni
necesariamente imprescindibles en la implementación final.

## 11.1- *Smartwatches*

Un *smartwatch *puede suponer un estilo de vida, incluso un concepto de
libertad; son como una carcasa de reloj que porta y camufla tecnología
digital y se incorpora al sujeto como una prenda más diaria, un
*wearable* (tecnología vestible[@eswiki:135097635]); "La información que
se mueve contigo", fue el lema de Android Wear[@nim8r7v850m] en 2014. Y,
aparejado de la mano, o la muñeca en este caso, puede ir una grave
pérdida de la privacidad.

Un reloj inteligente tiene matices que marcarán la diferencia, por
ejemplo, su diseño, su tamaño, su *interface* de
usuario[@eswiki:136870624], si está o no está asociado a un teléfono
inteligente mediante *Bluetooth*, si el reloj dispone de tarjeta
SIM[@eswiki:136903552] o no la tiene, si puede ser gestionado como un
dispositivo más en red (WiFi)[@eswiki:136990965] o no, si realmente es
un reloj inteligente o una pulsera de activad
(*fitness*[@eswiki:136374583]*)*; o todo junto, o parte de éstos.

Una amalgama de *hardware* y de prestaciones y precios de mercado están
asociado a ellos y que determinarán elementos como la pantalla (de onda
acústica[@eswiki:135020295], resistiva o capacitiva según su
*touch*[@eswiki:136906035]*, *y también su panel:
LCD[@eswiki:136681390], IPS[@enwiki:1032094402],
AMOLED[@eswiki:128825659] o OLED[@eswiki:134639376]), los sensores que
incorpore, la memoria RAM, memoria interna de almacenamiento,
microprocesador (de fabricación propia, Qualcomm, ARM, MediaTek...),
duración de la batería, si incorporan audio y cámara fotográfica,
tecnología de comunicación y aproximación como NFC[@eswiki:137027882],
Wifi o RFID,[@eswiki:136651291] etc.

Podemos encontrarlos desde los precios más ínfimos (≈,\<) a 20 € en el
mercado chino en AliEspress (Tipmant Smartwatch) o en Amazon, hasta
precios que pueden rondar los 2.000€ (**TAG HEUER CONNECTED GOLF
EDITION)**[@njmtm77yw7d], incluso más caros.

Y si ponemos la mirada hacia el futuro a la hora de inclinarnos por
ciertos tipos de dispositivos, la clave diferenciadora pudiera estar en
si reemplazan al *smartphone*, en si pueden hacer y recibir llamadas
(mediante bandas LTE[@eswiki:136935484], por ejemplo, vinculada a la
democratización del 5G[@eswiki:136894678]) y al Internet de la Cosas
(IoT)[@eswiki:136582135].

Habitualmente llevan una versión reducida como sistema operativo de
Android, iOS o Linux (Wear OS[@eswiki:134169451],
WatchOS[@eswiki:137047449] y Tizen OS[@eswiki:136504269]) son los más
habituales. Esa tecnología digital es la plataforma donde puede
ejecutarse nuestro *framework*, en un entorno de S.O. reducido.

#### 11.1.1.*- Hardware *de algunos de los relojes inteligentes

+---+--------+---+------------+---+---+---+
| ~ | ~**P   | ~ | ~**Comunic | ~ | ~ | ~ |
| * | rocesa | * | aciones**~ | * | * | B |
| * | dor**~ | * |            | * | * | a |
| D |        | M |            | P | C | t |
| i |        | e |            | a | á | e |
| s |        | m |            | n | m | r |
| p |        | o |            | t | a | í |
| o |        | r |            | a | r | a |
| s |        | i |            | l | a | ~ |
| i |        | a |            | l | * |   |
| t |        | * |            | a | * |   |
| i |        | * |            | * | ~ |   |
| v |        | ~ |            | * |   |   |
| o |        |   |            | ~ |   |   |
| * |        |   |            |   |   |   |
| * |        |   |            |   |   |   |
| ~ |        |   |            |   |   |   |
+===+========+===+============+===+===+===+
| S | Dua    | 4 | Bluetooth  | 1 | 2 | 3 |
| a | l-Core | G | 4.0 LE     | . | . | 0 |
| m | 1 GHz  | B |            | 6 | 0 | 0 |
| s | Exyn   | m |            | 3 | M | m |
| u | os3250 | e |            | " | e | A |
| n |        | m |            | S | g | h |
| g |        | o |            | u | a |   |
| G |        | r |            | p | p |   |
| e |        | i |            | e | i |   |
| a |        | a |            | r | x |   |
| r |        | i |            | A | e |   |
| 2 |        | n |            | M | l |   |
|   |        | t |            | O | e |   |
|   |        | e |            | L | s |   |
|   |        | r |            | E |   |   |
|   |        | n |            | D |   |   |
|   |        | a |            | c |   |   |
|   |        | , |            | o |   |   |
|   |        | 5 |            | n |   |   |
|   |        | 1 |            | r |   |   |
|   |        | 2 |            | e |   |   |
|   |        | M |            | s |   |   |
|   |        | B |            | o |   |   |
|   |        | R |            | l |   |   |
|   |        | A |            | u |   |   |
|   |        | M |            | c |   |   |
|   |        |   |            | i |   |   |
|   |        |   |            | ó |   |   |
|   |        |   |            | n |   |   |
|   |        |   |            | d |   |   |
|   |        |   |            | e |   |   |
|   |        |   |            | 3 |   |   |
|   |        |   |            | 2 |   |   |
|   |        |   |            | 0 |   |   |
|   |        |   |            | x |   |   |
|   |        |   |            | 3 |   |   |
|   |        |   |            | 2 |   |   |
|   |        |   |            | 0 |   |   |
+---+--------+---+------------+---+---+---+
| S | Qu     | 4 | Bluetooth  | A |   | 3 |
| a | alcomm | G | 4.0,       | M |   | 0 |
| m | Snap   | B | Wi-Fi, 3G  | O |   | 0 |
| s | dragon | m |            | L |   | m |
| u | 400 a  | e |            | E |   | A |
| n | 1 GHz  | m |            | D |   | h |
| g |        | o |            | d |   |   |
| G |        | r |            | e |   |   |
| e |        | i |            | 2 |   |   |
| a |        | a |            | \ |   |   |
| r |        | i |            | " |   |   |
| S |        | n |            | y |   |   |
|   |        | t |            | 3 |   |   |
|   |        | e |            | 6 |   |   |
|   |        | r |            | 0 |   |   |
|   |        | n |            | x |   |   |
|   |        | a |            | 4 |   |   |
|   |        | , |            | 8 |   |   |
|   |        | 5 |            | 0 |   |   |
|   |        | 1 |            | p |   |   |
|   |        | 2 |            | í |   |   |
|   |        | M |            | x |   |   |
|   |        | B |            | e |   |   |
|   |        | R |            | l |   |   |
|   |        | A |            | e |   |   |
|   |        | M |            | s |   |   |
+---+--------+---+------------+---+---+---+
| [ | Exynos | 4 | Bluetooth, | s |   | 2 |
| S | 3250   | G | BT4.1,     | A |   | 5 |
| a |        | B | Wi-Fi, NFC | M |   | 0 |
| m |        | m |            | O |   | m |
| s |        | e |            | L |   | A |
| u |        | m |            | E |   | h |
| n |        | o |            | D |   |   |
| g |        | r |            | \ |   |   |
| G |        | i |            | 3 |   |   |
| e |        | a |            | 6 |   |   |
| a |        | i |            | 0 |   |   |
| r |        | n |            | X |   |   |
| S |        | t |            | 3 |   |   |
| 2 |        | e |            | 6 |   |   |
| ] |        | r |            | 0 |   |   |
| ( |        | n |            | ( |   |   |
| h |        | a |            | 3 |   |   |
| t |        | , |            | 0 |   |   |
| t |        | 5 |            | 2 |   |   |
| p |        | 1 |            | p |   |   |
| s |        | 2 |            | p |   |   |
| : |        | M |            | i |   |   |
| / |        | B |            | ) |   |   |
| / |        | R |            |   |   |   |
| w |        | A |            |   |   |   |
| w |        | M |            |   |   |   |
| w |        |   |            |   |   |   |
| . |        |   |            |   |   |   |
| s |        |   |            |   |   |   |
| a |        |   |            |   |   |   |
| m |        |   |            |   |   |   |
| s |        |   |            |   |   |   |
| u |        |   |            |   |   |   |
| n |        |   |            |   |   |   |
| g |        |   |            |   |   |   |
| . |        |   |            |   |   |   |
| c |        |   |            |   |   |   |
| o |        |   |            |   |   |   |
| m |        |   |            |   |   |   |
| / |        |   |            |   |   |   |
| e |        |   |            |   |   |   |
| s |        |   |            |   |   |   |
| / |        |   |            |   |   |   |
| w |        |   |            |   |   |   |
| e |        |   |            |   |   |   |
| a |        |   |            |   |   |   |
| r |        |   |            |   |   |   |
| a |        |   |            |   |   |   |
| b |        |   |            |   |   |   |
| l |        |   |            |   |   |   |
| e |        |   |            |   |   |   |
| s |        |   |            |   |   |   |
| / |        |   |            |   |   |   |
| g |        |   |            |   |   |   |
| e |        |   |            |   |   |   |
| a |        |   |            |   |   |   |
| r |        |   |            |   |   |   |
| - |        |   |            |   |   |   |
| s |        |   |            |   |   |   |
| 2 |        |   |            |   |   |   |
| / |        |   |            |   |   |   |
| s |        |   |            |   |   |   |
| p |        |   |            |   |   |   |
| e |        |   |            |   |   |   |
| c |        |   |            |   |   |   |
| s |        |   |            |   |   |   |
| / |        |   |            |   |   |   |
|   |        |   |            |   |   |   |
| " |        |   |            |   |   |   |
| n |        |   |            |   |   |   |
| u |        |   |            |   |   |   |
| l |        |   |            |   |   |   |
| l |        |   |            |   |   |   |
| " |        |   |            |   |   |   |
| ) |        |   |            |   |   |   |
| . |        |   |            |   |   |   |
|   |        |   |            |   |   |   |
| ~ |        |   |            |   |   |   |
| S |        |   |            |   |   |   |
| . |        |   |            |   |   |   |
| O |        |   |            |   |   |   |
| : |        |   |            |   |   |   |
| \ |        |   |            |   |   |   |
|   |        |   |            |   |   |   |
| T |        |   |            |   |   |   |
| i |        |   |            |   |   |   |
| z |        |   |            |   |   |   |
| e |        |   |            |   |   |   |
| n |        |   |            |   |   |   |
| ~ |        |   |            |   |   |   |
+---+--------+---+------------+---+---+---+
| [ | Singl  | 4 | Bluetooth  | L |   | 3 |
| M | e-Core | G | 4.0 LE /   | C |   | 2 |
| o | 1 GHz  | B | Bluetooth  | D |   | 0 |
| t | TI     | m | 4.2, Wi-Fi | d |   | m |
| o | OMAP 3 | e | b/g/n,     | e |   | A |
| 3 | **/    | m | NFC, GPS   | 1 |   | h |
| 6 | **Qua  | o | **/        | . |   | / |
| 0 | lcomm® | r | **GLONASS  | 5 |   | 3 |
| ] | Snapd  | i | / Beidou / | 6 |   | 5 |
| ( | ragon™ | a | Galileo    | \ |   | 5 |
| h | Wear   | i |            | " |   | m |
| t | 3100   | n |            | c |   | A |
| t |        | t |            | o |   | h |
| p |        | e |            | n |   |   |
| s |        | r |            | r |   |   |
| : |        | n |            | e |   |   |
| / |        | a |            | s |   |   |
| / |        | , |            | o |   |   |
| e |        | 5 |            | l |   |   |
| s |        | 1 |            | u |   |   |
| . |        | 2 |            | c |   |   |
| w |        | M |            | i |   |   |
| i |        | B |            | ó |   |   |
| k |        | R |            | n |   |   |
| i |        | A |            | d |   |   |
| p |        | M |            | e |   |   |
| e |        | * |            | 3 |   |   |
| d |        | * |            | 2 |   |   |
| i |        | / |            | 0 |   |   |
| a |        | * |            | x |   |   |
| . |        | * |            | 2 |   |   |
| o |        | 1 |            | 9 |   |   |
| r |        | G |            | 0 |   |   |
| g |        | B |            | , |   |   |
| / |        | R |            | 2 |   |   |
| w |        | A |            | 0 |   |   |
| i |        | M |            | 5 |   |   |
| k |        |   |            | p |   |   |
| i |        | + |            | p |   |   |
| / |        | 8 |            | i |   |   |
| M |        | G |            | , |   |   |
| o |        | B |            | L |   |   |
| t |        | M |            | C |   |   |
| o |        | e |            | D |   |   |
| _ |        | m |            | c |   |   |
| 3 |        | o |            | o |   |   |
| 6 |        | r |            | n |   |   |
| 0 |        | i |            | r |   |   |
|   |        | a |            | e |   |   |
| " |        | I |            | t |   |   |
| M |        | n |            | r |   |   |
| o |        | t |            | o |   |   |
| t |        | e |            | - |   |   |
| o |        | r |            | i |   |   |
|   |        | n |            | l |   |   |
| 3 |        | a |            | u |   |   |
| 6 |        |   |            | m |   |   |
| 0 |        |   |            | i |   |   |
| " |        |   |            | n |   |   |
| ) |        |   |            | a |   |   |
|   |        |   |            | c |   |   |
| ~ |        |   |            | i |   |   |
| S |        |   |            | ó |   |   |
| O |        |   |            | n |   |   |
| : |        |   |            | / |   |   |
| \ |        |   |            | 1 |   |   |
|   |        |   |            | . |   |   |
| W |        |   |            | 2 |   |   |
| e |        |   |            | \ |   |   |
| a |        |   |            | " |   |   |
| r |        |   |            | \ |   |   |
| \ |        |   |            | " |   |   |
|   |        |   |            | C |   |   |
| O |        |   |            | i |   |   |
| S |        |   |            | r |   |   |
| \ |        |   |            | c |   |   |
|   |        |   |            | u |   |   |
| b |        |   |            | l |   |   |
| y |        |   |            | a |   |   |
| \ |        |   |            | r |   |   |
|   |        |   |            | A |   |   |
| G |        |   |            | M |   |   |
| o |        |   |            | O |   |   |
| o |        |   |            | L |   |   |
| g |        |   |            | E |   |   |
| l |        |   |            | D |   |   |
| e |        |   |            | ( |   |   |
| ™ |        |   |            | 3 |   |   |
| ~ |        |   |            | 9 |   |   |
|   |        |   |            | 0 |   |   |
|   |        |   |            | x |   |   |
|   |        |   |            | 3 |   |   |
|   |        |   |            | 9 |   |   |
|   |        |   |            | 0 |   |   |
|   |        |   |            | ) |   |   |
+---+--------+---+------------+---+---+---+
| L | Qu     | 4 | Bluetooth  | 1 |   | 4 |
| G | alcomm | G | 4.0        | . |   | 0 |
| G | Snap   | B |            | 6 |   | 0 |
| W | dragon | m |            | 5 |   | m |
| a | 400 a  | e |            | \ |   | A |
| t | 1.2    | m |            | " |   | h |
| c | GHz    | o |            | I |   |   |
| h |        | r |            | P |   |   |
|   |        | i |            | S |   |   |
| ~ |        | a |            | L |   |   |
| S |        | i |            | C |   |   |
| O |        | n |            | D |   |   |
| : |        | t |            |   |   |   |
| \ |        | e |            |   |   |   |
|   |        | r |            |   |   |   |
| A |        | n |            |   |   |   |
| n |        | a |            |   |   |   |
| d |        | , |            |   |   |   |
| r |        | 5 |            |   |   |   |
| o |        | 1 |            |   |   |   |
| i |        | 2 |            |   |   |   |
| d |        | M |            |   |   |   |
| \ |        | B |            |   |   |   |
|   |        | R |            |   |   |   |
| 4 |        | A |            |   |   |   |
| . |        | M |            |   |   |   |
| 3 |        |   |            |   |   |   |
| \ |        |   |            |   |   |   |
|   |        |   |            |   |   |   |
| e |        |   |            |   |   |   |
| n |        |   |            |   |   |   |
| \ |        |   |            |   |   |   |
|   |        |   |            |   |   |   |
| a |        |   |            |   |   |   |
| d |        |   |            |   |   |   |
| e |        |   |            |   |   |   |
| l |        |   |            |   |   |   |
| a |        |   |            |   |   |   |
| n |        |   |            |   |   |   |
| t |        |   |            |   |   |   |
| e |        |   |            |   |   |   |
| ~ |        |   |            |   |   |   |
+---+--------+---+------------+---+---+---+
| L | Qu     | 4 | Bluetooth  | P |   | 4 |
| G | alcomm | G | 4.0        | - |   | 1 |
| G | Snap   | B |            | O |   | 0 |
| W | dragon | m |            | L |   | m |
| a | 400 a  | e |            | E |   | A |
| t | 1.2    | m |            | D |   | h |
| c | GHz    | o |            | d |   |   |
| h |        | r |            | e |   |   |
| R |        | i |            | 1 |   |   |
|   |        | a |            | . |   |   |
|   |        | i |            | 3 |   |   |
|   |        | n |            | \ |   |   |
|   |        | t |            | " |   |   |
|   |        | e |            | y |   |   |
|   |        | r |            | 3 |   |   |
|   |        | n |            | 2 |   |   |
|   |        | a |            | 0 |   |   |
|   |        | , |            | x |   |   |
|   |        | 5 |            | 3 |   |   |
|   |        | 1 |            | 2 |   |   |
|   |        | 2 |            | 0 |   |   |
|   |        | M |            | p |   |   |
|   |        | B |            | í |   |   |
|   |        | R |            | x |   |   |
|   |        | A |            | e |   |   |
|   |        | M |            | l |   |   |
|   |        |   |            | e |   |   |
|   |        |   |            | s |   |   |
+---+--------+---+------------+---+---+---+
| S | Qua    | 4 | Bluetooth  | 1 |   | 4 |
| o | d-core | G | 4.0, NFC   | . |   | 2 |
| n | ARM    | B |            | 6 |   | 0 |
| y | Cortex | m |            | \ |   | m |
| S | A7 a   | e |            | " |   | A |
| m | 1,2GHz | m |            | y |   | h |
| a |        | o |            | 3 |   |   |
| r |        | r |            | 2 |   |   |
| t |        | i |            | 0 |   |   |
| W |        | a |            | x |   |   |
| a |        | i |            | 3 |   |   |
| t |        | n |            | 2 |   |   |
| c |        | t |            | 0 |   |   |
| h |        | e |            | p |   |   |
| 3 |        | r |            | í |   |   |
|   |        | n |            | x |   |   |
|   |        | a |            | e |   |   |
|   |        | , |            | l |   |   |
|   |        | 5 |            | e |   |   |
|   |        | 1 |            | s |   |   |
|   |        | 2 |            |   |   |   |
|   |        | M |            |   |   |   |
|   |        | B |            |   |   |   |
|   |        | R |            |   |   |   |
|   |        | A |            |   |   |   |
|   |        | M |            |   |   |   |
+---+--------+---+------------+---+---+---+
| A | Qu     | 4 | Bluetooth  | A |   | 3 |
| s | alcomm | G | 4.0        | M |   | 6 |
| u | Snap   | B |            | O |   | 9 |
| s | dragon | m |            | L |   | m |
| Z | 400 a  | e |            | E |   | A |
| e | 1.2    | m |            | D |   | h |
| n | GHz    | o |            | t |   |   |
| W |        | r |            | o |   |   |
| a |        | i |            | u |   |   |
| t |        | a |            | c |   |   |
| c |        | i |            | h |   |   |
| h |        | n |            | s |   |   |
|   |        | t |            | c |   |   |
|   |        | e |            | r |   |   |
|   |        | r |            | e |   |   |
|   |        | n |            | e |   |   |
|   |        | a |            | n |   |   |
|   |        | , |            | c |   |   |
|   |        | 5 |            | a |   |   |
|   |        | 1 |            | p |   |   |
|   |        | 2 |            | a |   |   |
|   |        | M |            | c |   |   |
|   |        | B |            | i |   |   |
|   |        | R |            | t |   |   |
|   |        | A |            | i |   |   |
|   |        | M |            | v |   |   |
|   |        |   |            | a |   |   |
|   |        |   |            | d |   |   |
|   |        |   |            | e |   |   |
|   |        |   |            | 1 |   |   |
|   |        |   |            | . |   |   |
|   |        |   |            | 6 |   |   |
|   |        |   |            | 3 |   |   |
|   |        |   |            | \ |   |   |
|   |        |   |            | " |   |   |
|   |        |   |            | y |   |   |
|   |        |   |            | 3 |   |   |
|   |        |   |            | 2 |   |   |
|   |        |   |            | 0 |   |   |
|   |        |   |            | x |   |   |
|   |        |   |            | 3 |   |   |
|   |        |   |            | 2 |   |   |
|   |        |   |            | 0 |   |   |
|   |        |   |            | p |   |   |
|   |        |   |            | í |   |   |
|   |        |   |            | x |   |   |
|   |        |   |            | e |   |   |
|   |        |   |            | l |   |   |
|   |        |   |            | e |   |   |
|   |        |   |            | s |   |   |
+---+--------+---+------------+---+---+---+
| [ | Apple  | 8 | WiFi y GPS | R |   | H |
| A | S1     | G | de iPhone  | e |   | a |
| p |        | B |            | t |   | s |
| p |        | m |            | i |   | t |
| l |        | e |            | n |   | a |
| e |        | m |            | a |   | 1 |
| W |        | o |            | c |   | 8 |
| a |        | r |            | o |   | h |
| t |        | i |            | n |   | o |
| c |        | a |            | F |   | r |
| h |        | i |            | o |   | a |
| ] |        | n |            | r |   | s |
| ( |        | t |            | c |   | d |
| h |        | e |            | e |   | e |
| t |        | r |            | T |   | a |
| t |        | n |            | o |   | u |
| p |        | a |            | u |   | t |
| s |        | , |            | c |   | o |
| : |        | 5 |            | h |   | n |
| / |        | 1 |            |   |   | o |
| / |        | 2 |            |   |   | m |
| e |        | M |            |   |   | í |
| s |        | B |            |   |   | a |
| . |        | R |            |   |   |   |
| w |        | A |            |   |   |   |
| i |        | M |            |   |   |   |
| k |        |   |            |   |   |   |
| i |        |   |            |   |   |   |
| p |        |   |            |   |   |   |
| e |        |   |            |   |   |   |
| d |        |   |            |   |   |   |
| i |        |   |            |   |   |   |
| a |        |   |            |   |   |   |
| . |        |   |            |   |   |   |
| o |        |   |            |   |   |   |
| r |        |   |            |   |   |   |
| g |        |   |            |   |   |   |
| / |        |   |            |   |   |   |
| w |        |   |            |   |   |   |
| i |        |   |            |   |   |   |
| k |        |   |            |   |   |   |
| i |        |   |            |   |   |   |
| / |        |   |            |   |   |   |
| A |        |   |            |   |   |   |
| p |        |   |            |   |   |   |
| p |        |   |            |   |   |   |
| l |        |   |            |   |   |   |
| e |        |   |            |   |   |   |
| _ |        |   |            |   |   |   |
| W |        |   |            |   |   |   |
| a |        |   |            |   |   |   |
| t |        |   |            |   |   |   |
| c |        |   |            |   |   |   |
| h |        |   |            |   |   |   |
|   |        |   |            |   |   |   |
| " |        |   |            |   |   |   |
| A |        |   |            |   |   |   |
| p |        |   |            |   |   |   |
| p |        |   |            |   |   |   |
| l |        |   |            |   |   |   |
| e |        |   |            |   |   |   |
|   |        |   |            |   |   |   |
| W |        |   |            |   |   |   |
| a |        |   |            |   |   |   |
| t |        |   |            |   |   |   |
| c |        |   |            |   |   |   |
| h |        |   |            |   |   |   |
| " |        |   |            |   |   |   |
| ) |        |   |            |   |   |   |
+---+--------+---+------------+---+---+---+
| A | S6     | 3 | **LTE y    | R |   | H |
| p | 64-bit | 2 | UMTS,      | e |   | a |
| p | dua    | G | Wi-Fi,     | t |   | s |
| l | l-core | B | Bluetooth  | i |   | t |
| e |        | m | 5.0**      | n |   | a |
| W |        | e |            | a |   | 1 |
| a |        | m |            | O |   | 8 |
| t |        | o |            | L |   | h |
| c |        | r |            | E |   | o |
| h |        | i |            | D |   | r |
| S |        | a |            | L |   | a |
| e |        | i |            | T |   | s |
| r |        | n |            | P |   |   |
| i |        | t |            | O |   |   |
| e |        | e |            |   |   |   |
| s |        | r |            |   |   |   |
| 6 |        | n |            |   |   |   |
|   |        | a |            |   |   |   |
| ~ |        | , |            |   |   |   |
| S |        | 1 |            |   |   |   |
| O |        | G |            |   |   |   |
| : |        | B |            |   |   |   |
| \ |        |   |            |   |   |   |
|   |        |   |            |   |   |   |
| i |        |   |            |   |   |   |
| O |        |   |            |   |   |   |
| S |        |   |            |   |   |   |
| \ |        |   |            |   |   |   |
|   |        |   |            |   |   |   |
| 1 |        |   |            |   |   |   |
| 4 |        |   |            |   |   |   |
| \ |        |   |            |   |   |   |
|   |        |   |            |   |   |   |
| o |        |   |            |   |   |   |
| \ |        |   |            |   |   |   |
|   |        |   |            |   |   |   |
| p |        |   |            |   |   |   |
| o |        |   |            |   |   |   |
| s |        |   |            |   |   |   |
| t |        |   |            |   |   |   |
| e |        |   |            |   |   |   |
| r |        |   |            |   |   |   |
| i |        |   |            |   |   |   |
| o |        |   |            |   |   |   |
| r |        |   |            |   |   |   |
| ~ |        |   |            |   |   |   |
+---+--------+---+------------+---+---+---+

~Crédito\ figura\ 2:\ Versión\ actualizada\ mejorada\ de\ «Características\ ~~*hardware*~[@eswiki:133248752]~.\ Reloj\ inteligente.\ (2021,\ 15\ de\ febrero). ~~*Wikipedia,\ La\ enciclopedia\ libre*~~.\ Fecha\ de\ consulta:\ 13:44,\ julio\ 18,\ 2021\ desde ~~<https://es.wikipedia.org/w/index.php?title=Reloj_inteligente&oldid=133248752>~~.»~

> El *framework* para cualquier *smartwatch* debe asumir que el estadio
> de funcionamiento recomendado es el **estadio E2** (ejecución de la
> IA) y el **modo M2** (entrelazado). De forma dinámica, en función de
> la evolución de la tecnología asociada a un *smartwatch*, el modo M1
> (autónomo) pudiera ser también una opción viable a medio plazo.

## 11.2.- Otros dispositivos afines

### 11.2.1- *Smartphones, tablets *y PC's

En la actualidad estos dispositivos han evolucionado de forma
contundente en la gama media del sector, son garantes y suficientes en
general, con altas prestaciones tecnológicas y una baja economía de
coste asociadas. Aunque las *tablets* parece que no terminan de
conseguir un nicho final suficiente de mercado en función de algunos
medidores asociados ([Imagen 66](#ne9cvxx4kmc)). Son durísimos rivales
los *smartphones* y los PC's para ellas; porque, en comparación, en la
relación tecnología y precio éstas salen perdiendo probablemente. Las
*tablets* actualmente, ¿parecen más un 'capricho útil' que una necesidad
real del usuario?[@nirznberm9d]... No obstante fabricantes como
Microsoft tienden a unificar sistemas operativos como Windows 10 y
11[@ndmgp5n3jjb] para que su integración esté asegurada a estos tres
niveles o familias de dispositivos. Que todo sea escalable y
transversal. Un todo en uno.

> El *framework* para cualquier elemento del tipo *smartphone*, *tablet*
> o PC debe asumir que el estadio de funcionamiento recomendado para
> éstos es el **estadio E2** (ejecución de la IA) y el **modo M1**
> (autónomo).

![](https://assets.pubpub.org/4y9axx8d/21626768198889.png){#ne9cvxx4kmc}

**Crédito imagen:** «**Tendencias de Internet 2021. Estadísticas y
hechos por países». VPNMentor. URL:**
<https://es.vpnmentor.com/blog/tendencias-de-internet-estadisticas-y-datos-en-los-estados-unidos-y-el-mundo/>,
Mangosta (<https://mangosta.org/tendencias-2/>)

## 11.2.2.- Domótica {#domtica}

Hablar de domótica es hablar sobre todo de sus tipos de conexiones para
una aplicación total y real de ésta, conjuntamente con el
5G[@eswiki:136894678] y/o el IoT[@eswiki:136582135] y una estructura más
que probable en «*Bus*[@eswiki:136329481] inteligente».

![](https://assets.pubpub.org/0936zh4g/31626930087898.png){#na6ickiip83}

**Todos los sensores y actuadores están conectados a través de un cable
bus.** **El sistema completo es denominado "sistema bus"**. Crédito
imagen: «KNX Conocimientos básicos del estándar KNX». V9-14. KNX.org.
Accesado el 22/07/2021. Url:
<https://www.knx.org/wAssets/docs/downloads/Marketing/Flyers/KNX-Basics/KNX-Basics_es.pdf>,
Mangosta (<https://mangosta.org/conocimientos-basicos-2/>)

Actualmente todo un espacio de tecnología de comunicaciones inalámbricas
coexiste: Bluetooth, WiFi, RFID, NFC y otros. Aunque las morfologías de
conexión para la domótica aún están decidiéndose por parte de la
industria y de los estándares que se asocian, pugnan entre ellos
defiendo diferentes intereses.

Una línea de trabajo, por ejemplo, es ZigBee que persigue:
«Comunicaciones seguras con baja tasa de envío de datos y maximización
de la vida útil de sus baterías»[@eswiki:132106076]; o Z
-Wave[@eswiki:128015329]: «Una red en malla que utiliza ondas de
radio de baja energía para comunicarse de un aparato a otro, permitiendo
el control inalámbrico de electrodomésticos y otros dispositivos, como
control de iluminación, sistemas de seguridad, termostatos, ventanas,
cerraduras, piscinas y garaje abrepuertas»; o Sigfox[@eswiki:134809884]:
«Un operador de red global y creador de la red 0G fundado en 2009 que
implementa redes inalámbricas para conectar dispositivos de bajo consumo
como pueden ser medidores eléctricos, centrales de alarmas o relojes
inteligentes, que necesitan estar continuamente encendidos y enviando
pequeñas cantidades de datos».

Aun dentro de estos tiempos tecnológicos tan convulsos, a nivel de
estrategias y vaivenes, (como un estándar y un valor seguro del mercado
de las comunicaciones para los próximos 5 años), Bluetooth y WiFi
parecen las apuestas más seguras y estables durante este periodo: a
nivel tecnológico y comercial, claro. Y la mayoría de los dispositivos
actuales uno (Bluetooth), u otro (WiFi), o ambos, los implementan:
disponen de esta tecnología tan popular entre los usuarios y
fabricantes.

> El *framework* para cualquier elemento doméstico (diferente a
> *smartwatch*, *smartphone*, *tablet*, y PC) debe asumir que el estadio
> de funcionamiento recomendado para elementos domóticos es el **estadio
> E2** (ejecución de la IA), y disponibles ambos modos M1 (autónomo) &
> M2 (asociado).

#### 11.2.2.1 Dispositivos domóticos con Android & iOS {#dispositivos-domticos-con-android-ios}

Las aplicaciones *smarthome* son una evidencia. Son innegables. Y mucho
han contribuido sistemas operativos como Android e iOS. Y cualquier
dispositivo doméstico o *wearable* de los que hemos descrito aquí es
susceptible de implementar estos sistemas operativos. Y también pueden y
han de estar protegido por la implementación de nuestro *framework*. Que
de acuerdo a lo enunciado previamente puede ser 'montado' sobre estas
tecnologías.

> **Por citar algunas referencias**: Amazon Alexa, Casa, Smartthings,
> Google Home, LIFX, Houseinhand KNX, TaHoma by Somfy, Home Connect App,
> Smart Life, Philips Hue, etc.

#### 11.2.2.2- Elemento multiplataforma JRE (*Java Runtime Environment) *en dispositivos domóticos {#elemento-multiplataforma-jre-java-runtime-environment-en-dispositivos-domticos}

La máquina virtual Java[@eswiki:133005440], o JVM por sus siglas en
inglés, es un entorno multiplataforma ideado para ser portable con
independencia de los sistemas y el entorno que lo envuelva.

«La máquina virtual de Java puede estar implementada en *software*,
*hardware*, una herramienta de desarrollo o un navegador *web*; lee y
ejecuta código precompilado bytecode que es independiente de la
plataforma. La JVM provee definiciones para un conjunto de
instrucciones, un conjunto de registros, un formato para archivos de
clases, la pila, un heap con recolector de basura y un área de memoria.
Cualquier implementación de la JVM que sea aprobada por SUN debe ser
capaz de ejecutar cualquier clase que cumpla con la
especificación.»[@eswiki:133005440] .

Es este soporte independiente, por tanto, un entorno domótico objetivo
en la implementación de nuestro DIID (**D**etector de **I**ntrusiones
**I**nteligente **D**omótico).

#### 11.2.2.3- Descripción del estándar de domótica KNX como marco regulador para dispositivos domóticos {#descripcin-del-estndar-de-domtica-knx-como-marco-regulador-para-dispositivos-domticos}

El estándar de protocolo KNX[@eswiki:134702414] se cimenta básicamente
en el concepto de bus[@eswiki:136329481] inteligente, y su mejor
descripción es entenderlo como una «neurona central» que comunica todos
los elementos de una vivienda. Este tipo de conexión de dispositivos es
muy propicio para una mejor y mayor aplicación de la IA sin duda. La
estandarización (ISO/IEC 14543)[@nwapwwet53u] rige esta tipología.
Ambos, capacidad de aplicar la IA y la estandarización, constituyen una
plataforma ideal de aplicación para nuestro Detector de Intrusiones
Inteligente Domótico(DIID por su acrónimo), para la implementación y
aplicación de *framework* definido en este trabajo de investigación.

Estos elementos a proteger por el DIID o (DI)^2^ van desde:
Interruptores de luz • Teclados de regulación de luz • Detectores de
movimiento • Detectores de presencia• Contactos de ventanas y puertas •
Timbre de la puerta de entrada • Contadores de consumo de agua, gas,
electricidad y calor • Sensores de sobretensión • Sensores de
temperatura ambiente, interior y exterior • Sensores de temperatura en
circuitos de agua caliente y calefacción • Módulos para prefijar la
temperatura de consigna en las habitaciones • Sensores de luminosidad
interior y exterior • Sensores de viento para control de persianas y
toldos • Indicadores de estado o fallo en aparatos de línea blanca •
Sensores de fuga • Sensores de nivel • Receptor de radiofrecuencia en
cierre de puertas • Receptor de infrarrojos de mandos a distancia •
Lectores de huellas dactilares o tarjetas electrónicas para control de
acceso[@nclc2lsemo1]\... Y un largo etcétera de actuadores y módulos.

> Y todos ellos han de ser protegidos, y el *framework *implementado en
> un IDS inteligente es de aplicación necesaria aquí.

![](https://assets.pubpub.org/gu01824o/71626926965330.png){#n6gowobbo1h}

**KNXnet/IP en el modelo de referencia OSI**. Crédito imagen: «KNX
Conocimientos básicos del estándar KNX». V9-14. KNX.org. Accesado el
22/07/2021. Url:
<https://www.knx.org/wAssets/docs/downloads/Marketing/Flyers/KNX-Basics/KNX-Basics_es.pdf>,
Mangosta (<https://mangosta.org/estandar-knx/>)

Los ensayos realizados en laboratorio aportan el conocimiento suficiente
para inferir que el marco puede ser embebido en un
microcontrolador[@eswiki:134047878] de la familia PIC
18F[@n8cd7a12qs4],[@noovg1uymgt] PIC18F4550 u otro similar con la
sistemática de KNX[@nrcrvyyr4xa], apoyado por el diseño específico de
circuitería electrónica que implemente la lógica combinacional
necesaria.

![](https://assets.pubpub.org/j4824z67/21626932999454.png){#nry4gh8lqxl}

 **Montaje En** ***Protoboard*** **Del Sistema Pinguino.** Julio F. De
la Cruz G. Accesado el 22/07/200121. Url:
http://3.bp.blogspot.com/-JtZH7qb-j-w/UhLyWQdHLjI/AAAAAAAAAjQ/cjoKPWOIxsw/s1600/image7923.png,
Mangosta (<https://mangosta.org/montaje-en-protoboard/>)

El diseño de este dispositivo domótico DIID se concibe como una
*appliance*[@enwiki:996111977] que reúne como mínimo los requisitos
*hardware *de un *smartwatch* para embeber el estadio y modo de
funcionamiento inherente a éste anteriormente definidos, mediante un
*software* encapsulado o *firmware*[@eswiki:135687442].

Su filosofía de funcionamiento debe basarse en la técnica
*plug&play*[@eswiki:131957985] de modo que pudiera ser un elemento de
protección más, alojado entre los dispositivos propios de un cuadro
eléctrico de cualquier vivienda que alberga normalmente un
ICP[@eswiki:134683284], un diferencial[@eswiki:136420466] e
interruptores magnetotérmicos[@eswiki:136559713].

Concebido por tanto el dispositivo IDS domótico (DIID) como un elemento
más adicional de seguridad y protección en un hogar o un entorno laboral
que implementara el estándar KNX[@eswiki:134702414].

# V.- Conclusión {#v--conclusin}

Aquí se ha demostrado que el uso de la IA, en buena parte de sus
dimensiones, puede ser llevada a término con rigor académico, definible
en el campo de las matemáticas y usable en el del laboratorio; y que
puede ser pensada, razonada y aplicada.

El *framework* está motivado por la continua aparición y mejora de
dispositivos móviles en forma de s*martwatches*, *smartphones* y otros
similares que ha propiciado simultáneamente un creciente y desleal
interés en poner bajo la lupa y el control de los aplicativos a sus
usuarios. Éstos son presa de una abusiva injerencia en sus vidas para
telemedir y telegestionar sus hábitos en Internet, y también de
sustraerles de forma ofuscada datos personales como, por ejemplo, cuando
realizan deportes que precisan medir constantes vitales tales como
pulsaciones del corazón, presión arterial, nivel de oxígeno, etc. La
industria que los produce y los gestiona arteramente está canalizando
cada vez más esfuerzos económicos, así como ciencias como la
inteligencia artificial (IA), gestión de flujos de datos y estrategias
para que el resultado final apunte hacia la manipulación, venta y
secuestro de las vidas de los ciudadanos que las usan. Y todo ello con
un probable valedor y último propietario: la Inteligencia Artificial
(IA), llena de oscuridad y mecanismos internos oscuros o '*Black
Boxes*'\... Y de sociedades ingenuas, como la nuestra, que lo están
impulsando desconociendo probablemente la causa y el efecto final para
la humanidad.

## 12.1.- Corolario I

Podemos plantear este marco como un espacio generador de marcos, análogo
a un espacio vectorial[@eswiki:136483683] que genera subespacios
vectoriales[@eswiki:131144360]; y al
$\vec SV_{intrusión}= {[\vec P x _{(1...n)}, \vec Img_{y_{i}}]_0^{3^{(n)}}}$como
su sistema generador[@eswiki:120658623] homólogo, en pro de la
transparencia y la explicabilidad de tecnologías como la IA. Donde cada
variable analógica, ambigua, difícilmente definible, amplia de espectro
y pensamiento, y abrumadora en dimensiones, pueda ser escaneada en sus
parámetros más fundamentales como postula, demuestra y defiende este
*framework *en nuestra opinión. Aquellos parámetros iniciales que
incluso un niño se atrevería a dibujar de algo desconocido para él, un
monigote como si fuese un garabato, como un símbolo[@eswiki:135193010] o
como una primera idea de la niñez. Y a medida que el niño aprenda y
aumente 'sus parámetros' de definición y valores personales, entonces la
definición será más profunda, concisa y ajustada a su propia realidad.
De igual manera que se presenta en este marco, en sus cimientos. Para
que la inteligencia artificial sea algo que pueda ser explicable,
transparente y dentro del control humano. Porque una ingeniería inversa
siempre podría devolverla al mundo del *homo
sapiens*[@eswiki:136982750], nuestro mundo real con todas sus
imperfecciones y sus realidades.

## 12.2.- Corolario II

Por inferencia del corolario I, otra de las mayores preocupaciones
entorno al la inteligencia artificial, el sesgo
algorítmico[@eswiki:136371730]: de género, cultural, de raza, de
discapacidades individuales, de pensamientos e ideologías\... puede ser
mitigado. Tratando de alcanzar una sociedad más justa en valores. Al
lado de sus logros tecnológicos humanos.

## 12.3.- Corolario III

Por inferencia de los corolarios I y II, la Inteligencia Artificial (IA)
**puede ser educada humanamente** para un bien superior de los humanos.

#####     **¿Por qué y cómo?**  {#por-qu-y-cmo}

Puede ser educada porque podemos ser selectivos en aquellos parámetros
que queramos sesgar, (como se haría con la raza de un animal pura
sangre), y con ellos entrenar a la IA para que piense y decida en esa
línea determinada de razonamiento; de forma casi genética, puesto que
los parámetros supondrían *quasi* la síntesis genética en laboratorio
del pensamiento de una IA predefinida en función de qué sí y qué no
queremos tomar durante su periodo de entrenamiento.

Todo comportamiento humano, o pensamiento abstracto o entelequia de
algo, puede ser escaneado (garabateado) por este *framework* de acuerdo
a la expresión algebraica:

> $(\hspace{0.1cm} \Sigma  _{j=1} ^{j=n}\hspace{0.1cm}  (\vec Px_n-\vec Px_{(n-1)}))-(\vec Px_1-\vec Px_n)=0$
> .

Esto último, llevado a sus extremos más negativos y crueles con la
humanidad, al contrario del fin que persigue este *framework*, también
puede generar IA's peligrosas; algo sobre lo que movimientos sociales
nacionalistas en Alemania[@eswiki:137160412] y la teoría del
"superhombre" también reflexionaron: El *Übermensch*[@eswiki:137195283].
Toda ciencia siempre tiene dos caras: el buen uso y el mal uso para la
humanidad.

## 12.4.- Corolario IV

-   Teorema del existencialismo ene-dimensional

> Dado un *framework, *como el aquí descrito, todo un universo de
> posibilidades ene-dimensionales pueden ser plasmadas en planos
> gráficos que lo representen a éste en un instante T~1\ ~determinado
> para un entorno definido y observable. (En una imagen que vale más que
> mil palabras...).

**DEMOSTRACIÓN**

Las gráficas de este *framework* se ubican por completo en la aplicación
lineal $f: \mathbb N→ \mathbb R^2 $... Pero:

«\[...\] Atendiendo a las coordenadas de cada vector y su naturaleza
algebraica, la dimensión real sería la que sigue:

1\) El grupo de vectores $\vec P x _{(1...n)}$ {Dim~1~}$\N$=1.

2\) El grupo de vectores $ \vec Img{_y} _i $ {Dim~2~}$\R$=2.

3\) El grupo de vectores $\vec P_x$ {Dim~3~}$\N$=n.

4\) El grupo de vectores $ \vec Img_y$ {Dim~4~}$\R$=n. \[...\]».

Por lo que se puede inferir que al ser $ \vec Img_y$ {Dim~4~}$\R$
ene-dimensional, también puede pensarse un Universo teórico de
posibilidades, similar al nuestro existencial, e ilimitado si seguimos
el modelo expuesto aquí. Allí adonde más allá de $\vec R^3$ nuestra
propia existencia nos hace tiritar de dudas y escepticismo. Y que sin
embargo queda resulto en planos gráficos (como nuestra propia existencia
en fotografías de recuerdos) mediante $ \vec Img{_y} _i $
{Dim~2~}$\R$=2; que lo vuelve visual y existencial: terrenal ante
nuestros ojos. Si cabe afectado y/o compatible con el «Principio de
Indeterminación de Heisenberg»[@eswiki:136314920].

(Cqd: *Quod erat demonstrandum*)*.*

Y si algo hemos aprendido de la historia de la ciencia, es que mientras
la metafísica de los griegos[@eswiki:136738658] y otros pensadores
sembraban ideas y abstracciones cualitativas[@eswiki:136544957],
científicos y matemáticos como Galileo Galilei[@eswiki:137211807], Isaac
Newton[@eswiki:137096882], Laplace[@eswiki:137109507],
Leibniz[@eswiki:137109507] y otros «gigantes» lo llevaron al campo de lo
cuantificable[@eswiki:133597252] e infinitesimalmente
discreto[@eswiki:136277145] y medible. Al
existencialismo[@eswiki:136610666] matemático observable de Blaise
Pascal.

También hemos aprendido con sorpresa que una mente aniñada, curiosa y
despierta, puede suponer e intuir argumentos físicos y matemáticos
universales, sin necesidad de disponer de toda la información del
conjunto del que se compone 'un ente', como así ya lo hiciera
*Philosophiæ naturalis principia mathematica*[@eswiki:133706339] de
Newton; alguien que además alumbró el cálculo diferencial y vislumbró el
universo matemático en infinitésimos. Siguiendo la senda de su maestro,
Isaac Barrow[@eswiki:136666345].

> Maestros y alumnos son la esperanza de toda ciencia humana. El camino
> para aprender de los errores y el camino a seguir en el futuro. Y con
> ello entrenar y educar también a nuestros probables descendientes
> imperecederos, o mentes robotizadas, que denominados como
> «Inteligencia Artificial (IA)»... Y así garantizar un mañana
> humanamente tecnológico, y no, por el contrario, un mañana
> tecnológicamente humano; porque sería un grave error.


## 12.5.- Actualización de continuidad SV — 19/06/2026 {#actualizacion-de-continuidad-sv-20260619}

La presente actualización fija la continuidad formal entre la intuición técnica que sostuvo este *framework* —parámetros ternarios, imagen asociada, clasificación asistida por IA y decisión humana revisable— y el desarrollo maduro del **Sistema Vectorial SV** publicado en 2026. La publicación original ya contenía una idea rectora: una variable compleja puede descomponerse en parámetros discretos, proyectarse en una forma visible y someterse a lectura humana y maquinal. En 2026, esa intuición queda reordenada como célula SV: un vector finito de parámetros ternarios, con valores `0`, `1` y `U`, capaz de producir una imagen/frame trazable, comparable y auditable.

La continuidad no consiste en afirmar que el texto de 2020–2021 ya contuviera todo el SV plenamente constituido. Consiste en reconocer que aquí aparece una de sus direcciones iniciales: convertir un problema complejo en una imagen que el ser humano y la IA puedan leer conjuntamente. En la formulación madura, la imagen deja de ser sólo un recurso de clasificación sobre ResNet y pasa a ser una forma de representación estructural. La máquina procesa el vector; el ser humano reconoce la figura; la indeterminación queda visible bajo `U`; la decisión puede revisarse sin borrar la traza.

Esta evolución se expresa mediante la cadena:

`parámetros → célula ternaria → vector → imagen/frame → lectura humana y maquinal → suceso → dominio → residual → retorno`.

La creación posterior de las **matemáticas factuales del Sistema Vectorial SV** responde a una necesidad que este *framework* ya dejaba entrever: las herramientas estadísticas y temporales son útiles, pero no bastan para una lectura del hecho cuando se exige trazabilidad, dominio declarado, frontera, residual, no clausura honesta e intervención humana. El SV maduro no toma el tiempo como primitivo ni usa la probabilidad como sustituto de una clausura no demostrada. El tiempo puede servir como medida, registro o comparación; no funda por sí mismo el suceso. La unidad de lectura pasa a ser el suceso declarado en un dominio, con frontera, traza, residual y retorno.

Desde esta perspectiva, el *framework* de imágenes parametrizadas queda como antecedente técnico de una arquitectura más amplia. El problema original era detectar intrusiones en dispositivos mediante parámetros, imagen y red residual artificial. El problema general del SV es más extenso: enseñar a una IA o a un humanoide a operar sobre configuraciones trazables, sin caja negra, sin reescritura del pasado y sin ocultar la indeterminación; y, al mismo tiempo, proporcionar a la ciencia una forma de parametrizar dominios complejos —físicos, biológicos, químicos, cosmológicos, técnicos o materiales— mediante células, frames, sucesos, operadores, fronteras y retornos.

En esa ampliación aparecen documentos y líneas de desarrollo posteriores que ya no pertenecen sólo a una implementación de ciberseguridad, sino a una matemática propia del SV:

- **Nuevas matemáticas del Sistema Vectorial SV y Física factual como conjunto iniciador**: https://doi.org/10.21428/39829d0b.67195860

- **Tesauro de matemáticas del Sistema Vectorial SV**: https://doi.org/10.21428/39829d0b.9f868dc2

- **Conjunto matemático unificado del cambio factual, ciclos, medición factual y trayectorias poligonales de activación en el Sistema Vectorial SV**: https://doi.org/10.21428/39829d0b.2b3c9808

- **Fundamentos operatorios absolutos del electromagnetismo factual en el Sistema Vectorial SV**: https://doi.org/10.21428/39829d0b.0cb6137e

- **Álgebra de composición intercelular del Sistema Vectorial SV**: https://doi.org/10.21428/39829d0b.4ebab177

- Página de acceso de la publicación algebraica: https://www.itvia.online/algebra-de-composicion-intercelularl-sv

La aportación de esta actualización es, por tanto, situar el documento en su continuidad real: de un *framework* de imágenes parametrizadas para IA se pasa a un sistema formal que une terna, célula, vector, imagen, suceso, matemática factual y ciencia parametrizable. La imagen no sustituye al cálculo; lo hace visible. La célula no sustituye al mundo; lo parametriza bajo condiciones declaradas. La IA no funda la decisión; colabora dentro de una gramática trazable. El ser humano conserva la lectura, la revisión y la responsabilidad del cierre.

# VI.- Sistemas y servicios auxiliares implementados {#vi--sistemas-y-servicios-auxiliares-implementados}

[NextCloud](https://ciberseguridad.arboledalan.net/intranet/) y
[Gitlab](https://ciberseguridad.arboledalan.net/repositorio/users/sign_in)
para uso interno o externo de esta publicación.

# VII.- Declaración de conflicto de intereses {#vii--declaracin-de-conflicto-de-intereses}

Los autores declaran que a fecha de esta versión no tienen ningún
conflicto de intereses. Esta publicación no está subvencionada por
ningún proyecto que pudiera aportarle financiación, ni tampoco bajo el
patrocinio o esponsorización de ninguna marca u otra similar. Cada uno
de los autores se representa así mismo, y actúa de forma independiente.
Asimismo se declara la intención futura de lanzar un *software* definido
en la url mangosta.org, y que a su vez este dominio y su *hosting
*sirven como herramienta de esta publicación para lograr mejoras
técnicas limitadas en esta plataforma.

# VIII- Manifiesto del equipo de investigación que ha realizado este trabajo: docentes y estudiantes {#viii--manifiesto-del-equipo-de-investigacin-que-ha-realizado-este-trabajo-docentes-y-estudiantes}

> Una realidad científica ésta, sobre la ciberseguridad y la IA descrita
> aquí, que es palpable y auditable en un documento nacido fruto de la
> investigación y la educación. Porque la ciencia, opinamos, no debe ser
> un negocio para nadie más que para la sociedad y en beneficio de la
> humanidad, un signo de la mayor *loa* y respeto a todos los
> científicos que nos hicieron posible llegar hasta aquí en el
> conocimiento; aquellas mentes y hombros de «genios gigantes» sobre los
> que nos montamos y logramos caminar mucho más rápido todos.^~\ ~^
>
> ^**Juan\ Antonio\ Lloret\ Egea,**^^\ \ en\ nombre\ de\ todo\ el\ equipo\ de\ investigación.^

**Keywords**: #cienciaabierta, #openscience, #investigación, #research,
#IA, #AI, #inteligenciaartificial #artificialintelligence, #IDS,
#ciberseguridad, #cybersecurity #español #educación #education
#enseñanza #skills

Licencia: [Attribution-NonCommercial-NoDerivatives 4.0 International (CC
BY-NC-ND
4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

# IX.- Agradecimientos {#ix--agradecimientos}

-   IES La Arboleda, Alcorcón, Madrid. <http://www.laarboleda.es/> por
    contribuir con docentes del Departamento de Informática, y alumnado
    de 1º de Desarrollo de Aplicaciones Multiplataforma (DAM) y de 2º de
    Sistemas Microinformáticos en Red (SMR). Asimismo por el apoyo de
    todo el equipo directivo del instituto. Y por los recursos
    aportados, parte de éstos están / fueron expuestos en
    https://arboledalan.net/ciberseguridad/

-   Biblioteca Regional de Murcia, por la ayuda a la difusión de la
    actividad:
    https://bibliotecaregional.carm.es/agenda/presentacion-biblia-de-la-ia-ai-bible-publicacion-sobre-inteligencia-artificial/

-   A título póstumo a *sir* Isaac Newton, [@eswiki:137096882] por
    enseñarnos a mirar y educarnos en la manera de hacerlo: «He sido
    como un **niño** jugando a la **orilla del mar**, que se divierte al
    encontrar de vez en cuando un guijarro más suave que los demás o una
    concha más bonita, mientras el gran océano de la verdad se extiende
    sin descubrir ante mis ojos».

[^1]: Para no perjudicar al idioma español, se usará en adelante de
    forma indistinta la palabra «Framework» inglesa y la palabra «Marco»
    del idioma español.

[^2]: «La inteligencia artificial, AI (del inglés, *artificial
    intelligence*), es realmente el campo más prometedor, que ofrece una
    serie de ámbitos en los que se han utilizado sistemas de
    multivaluados, MVL (del inglés, *multi-valued logics*) debido a su
    posibilidad para abarcar un rango más amplio de estados.

    Una primera área de aplicación la encontramos muy relacionada con la
    posibilidad de representar preocupaciones, sentido común,
    razonamientos, etc. por medio herramientas matemáticas como
    conjuntos difusos y lógica difusa (del inglés, *fuzzy logic*).

    Una segunda área de aplicación, relacionada con la anterior viene
    dada por la automatización de datos y minería de conocimiento. Aquí,
    merecen especial mención los métodos de *clustering* (procedimiento
    basado en la unión de vectores que reúnen una determinada
    característica). En este contexto también se están desarrollando
    técnicas que automatizen sistemas MVL, así como en los métodos de la
    lógica de programación para dichos sistemas. Parte de esta tendencia
    se debe al desarrollo reciente de las lógicas de descripción
    generalizada, llamadas lógicas de descripción difusa, que permiten
    la inserción de herramientas técnicas (grados de verdad, conectivas,
    predicados graduales) procedentes de MVL.». Lógica trivalente.
    (2021, 22 de mayo). *Wikipedia, La enciclopedia libre*. Fecha de
    consulta: 14:58, julio 14, 2021
    desde <https://es.wikipedia.org/w/index.php?title=L%C3%B3gica_trivalente&oldid=135730214>.

[^3]: «Los gráficos radiales comparan varias variables cuantitativas y
    son útiles para visualizar qué variables tienen valores similares, o
    si existen valores atípicos entre las variables. Los gráficos
    radiales se componen de una secuencia de radios, con cada radio que
    representa una sola variable. Los gráficos radiales también son
    útiles para determinar qué variables están puntuando alto o bajo
    dentro de un conjunto de datos». Fuente: IBM, "Gráficos radiales"
    accesible en
    https://www.ibm.com/docs/es/spss-statistics/version-missing?topic=types-radar-charts

    \

[^4]: «Investigadores de la Universidad George Washington, junto con
    investigadores de la Universidad de California, Los Ángeles, y la
    startup de tecnología profunda Optelligence LLC, han desarrollado un
    acelerador de red neuronal convolucional óptico capaz de procesar
    grandes cantidades de información, del orden de petabytes, por
    segundo. Esta innovación, que aprovecha el paralelismo masivo de la
    luz, presagia una nueva era de procesamiento de señales ópticas para
    el aprendizaje automático con numerosas aplicaciones, que incluyen
    automóviles autónomos, redes 5G, centros de datos, diagnósticos
    biomédicos, seguridad de datos y más.». *Developing Smarter, Faster
    Machine Intelligence with Light.* Universidad George Washington.
    17/12/2020.
