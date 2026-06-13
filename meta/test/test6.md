# Determinación del radio y del volumen medio del universo observable: distancia relativa, patrón lunar y clausura geométrica auxiliar

## Índice

- I. Resumen
- II. Abstract
- III. Introducción al problema
- IV. Estado del arte
  - IV.I. Medición indirecta de dominios no recorridos
  - IV.II. Eratóstenes y la clausura geométrica de un dominio terrestre
  - IV.III. Medición astronómica por ángulo, paralaje y horizonte
  - IV.IV. Newton y la proyección matemática de leyes universales
  - IV.V. Universo observable, horizonte de observación y diámetro de contraste
  - IV.VI. Cosmometría contemporánea: CMB, expansión, BAO, cartografía 3D y misiones de gran escala
  - IV.VII. Metrología astronómica: año luz juliano y patrón lunar
  - IV.VIII. Posición del Sistema Vectorial SV ante la tradición de cálculo indirecto
- V. Alcance formal
- VI. Teorema de la recta generatriz del Universo Físico observable
- VII. Ecuación del teorema
- VIII. Demostración
- IX. Radio medio equivalente del Universo Físico observable
- X. Patrón lunar
- XI. Distancia relativa media desde el centro de la Tierra hasta el límite de la esfera equivalente del Universo Físico observable
- XII. Conclusión
- XIII. Bibliografía
  - XIII.I. Referencias internas del Corpus SV citadas
  - XIII.II. Referencias externas de contraste

## I. Resumen

Esta investigación determina el radio medio equivalente, el volumen esférico auxiliar, el patrón lunar y la distancia relativa media desde el centro de la Tierra hasta el límite de la esfera perfecta equivalente del Universo Físico observable, bajo la restricción formal `Ω_F ≠ 𝓣`. La determinación no mide la totalidad absoluta ni transforma el horizonte observable en borde ontológico; declara un dominio físico observable retornado, una clausura geométrica auxiliar, un modelo esférico equivalente, un transductor metrológico y un residual de lectura. En ese marco, el diámetro de contraste `93.000.000.000 ly`, el año luz juliano `1 ly = 9.460.730.472.580,8 km` y la distancia media Tierra–Luna `LD := 384.400 km` operan como magnitudes externas de contraste, no como fundamentos del Sistema Vectorial SV (Encyclopaedia Britannica, 2026b; International Astronomical Union, s. f.; National Aeronautics and Space Administration, s. f.).

La aportación formal se articula mediante el teorema de la recta generatriz del Universo Físico observable, denominada internamente `Recta-Ómicron SV16` (`Recta_Οmi_SV16`). Se declara un espacio afín tipado `𝔼_Ω^SV := E_A^SV × E_R^SV × E_D^SV`, un espacio vectorial residual asociado `𝓡_Ω^SV := V_A^SV × V_R^SV × V_D^SV`, un origen formal tipado `O_∅`, un punto terminal interno `P_Ω^SV`, un vector director `v_Ω := Δ(O_∅→P_Ω^SV)` y un tramo operativo `ℓ_{Ω,[0,1]}^SV`. La ecuación local `𝓖_Ω^SV(O;s)=0_Ω` no sustituye la ecuación rectora del SV: sólo declara cierre proyectivo dentro del dominio observable retornado, con pertenencia proyectiva `π_Ω(O) ∈ ℓ_{Ω,[0,1]}^SV` y no pertenencia material directa del objeto bruto a la recta (Lloret Egea, 2026a, 2026f, 2026g).

El resultado metrológico adoptado en esta clausura es `R̄_Ω = 46.500.000.000 ly = 439.923.966.975.007.200.000.000 km = 439.923.966.975.007.200.000.000.000 m`. El volumen esférico auxiliar queda expresado como `V_Ω = (4π/3)(R̄_Ω)^3`, y la distancia relativa media desde `C_⊕` hasta `∂S_Ω` coincide con `R̄_Ω` por definición del modelo esférico equivalente. En patrón lunar, la forma exacta es `R̄_Ω = (35.477.739.272.178.000.000 / 31) LD`, con lectura decimal `1.144.443.202.328.322.580,645161290323` distancias medias Tierra–Luna y cota de redondeo inferior a `0,1922 mm`. En escala larga española, el resultado equivale aproximadamente a `1,14` trillones de distancias medias Tierra–Luna; dicho de forma llana, algo más de un trillón de veces la distancia media entre la Tierra y la Luna.

## II. Abstract

This work determines the equivalent mean radius, auxiliary spherical volume, lunar-distance pattern, and mean relative distance from Earth’s centre to the boundary of the equivalent sphere assigned to the observable physical Universe, under the formal restriction `Ω_F ≠ 𝓣`. The calculation does not measure absolute totality and does not convert the observable horizon into an ontological edge. It declares a returned observable domain, an auxiliary geometric closure, an equivalent spherical model, a metrological transducer, and a controlled residual of reading. The adopted contrast values — `93,000,000,000 ly`, `1 ly = 9,460,730,472,580.8 km`, and `LD := 384,400 km` — are external metrological references and do not ground the Vectorial System SV (Encyclopaedia Britannica, 2026b; International Astronomical Union, s. f.; National Aeronautics and Space Administration, s. f.).

The formal core is the theorem of the generating line of the observable physical Universe, internally named `Recta-Ómicron SV16` (`Recta_Οmi_SV16`). The theorem declares a typed affine space, an associated residual vector space, a typed formal origin, an internal terminal point, a director vector and an operative return segment. Its local equation, `𝓖_Ω^SV(O;s)=0_Ω`, does not replace the governing equation of SV; it only states projective closure inside the declared observable domain. The result is an equivalent mean radius of `46,500,000,000 ly`, equivalent to `439,923,966,975,007,200,000,000 km`, with an auxiliary spherical volume determined by `V_Ω = (4π/3)(R̄_Ω)^3`. Expressed in mean Earth–Moon distances, the exact form is `(35,477,739,272,178,000,000 / 31) LD`, approximately `1.14` trillion mean Earth–Moon distances in the Spanish long scale.

## III. Introducción al problema

El problema de determinar el radio y el volumen medio del universo observable no puede formularse como una medición directa de una totalidad física recorrible. El universo observable se define por horizonte de observación, historia de propagación luminosa, expansión cosmológica y condiciones instrumentales de retorno; no por una frontera rígida accesible desde fuera. Por ello, toda determinación responsable debe distinguir entre totalidad absoluta, dominio observable, modelo geométrico auxiliar, unidad metrológica, transductor, residual y retorno. Esta distinción es especialmente necesaria cuando se adopta un diámetro de contraste ampliamente usado —aproximadamente `93.000.000.000 ly`— porque dicho valor no convierte el universo observable en totalidad de lo real ni en esfera material cerrada; sólo habilita una clausura esférica equivalente para cálculo, contraste y comunicación metrológica (Encyclopaedia Britannica, 2026b).

La cuestión se sitúa en una tradición científica antigua y muy sólida: calcular y acotar dominios que no se recorren materialmente. Eratóstenes no caminó la circunferencia terrestre para estimarla; utilizó diferencia angular, distancia entre lugares y una hipótesis geométrica sobre la curvatura terrestre. Hiparco no necesitó alcanzar la Luna para aproximar su distancia; trabajó con paralaje y relaciones geométricas. Al-Biruni no recorrió el diámetro terrestre; lo infirió desde altura, horizonte y trigonometría. Newton tampoco necesitó desplazarse por el sistema planetario para formular una ley de gravitación universal: convirtió observación, geometría, dinámica y formalización matemática en una proyección general de alcance físico (Encyclopaedia Britannica, 2026a, 2026c; Royal Society, 2014; Sparavigna, 2014).

En esta investigación, el Sistema Vectorial SV toma esa tradición de medición indirecta y la somete a sus propias condiciones de admisibilidad: dominio declarado, coordenación tipada, frontera, traza, residual, retorno y exclusión de la totalidad absoluta como objeto medible. La operación no consiste en importar sin mediación una cifra cosmológica, sino en declarar cómo una cifra externa de contraste puede entrar en una formulación interna sin gobernarla. Por tanto, la distancia relativa `D_rel^Ω(C_⊕,∂S_Ω;R̄_Ω,LD,𝓜_sph,𝔛_{SI↔SV})` no es una afirmación geocéntrica ni una cosmología cerrada: es una lectura radial externa de una clausura geométrica auxiliar, mediada por modelo, transductor y residual (Lloret Egea, 2026a, 2026c).

El propósito del documento es doble. Primero, fijar matemáticamente la recta generatriz y su tramo operativo de retorno para el Universo Físico observable, evitando toda confusión entre punto afín, vector director, residual y objeto físico bruto. Segundo, calcular de forma explícita el radio medio equivalente, el volumen esférico auxiliar y la distancia relativa en años luz, kilómetros, metros y distancias medias Tierra–Luna. De este modo, el texto produce un resultado legible para la metrología ordinaria sin abandonar las restricciones propias del SV: `Ω_F ≠ 𝓣`, no espacialización de `0_SV`, no clausura ontológica del horizonte observable y no conversión del patrón lunar en unidad constitutiva interna.

## IV. Estado del arte

### IV.I. Medición indirecta de dominios no recorridos

La historia de la ciencia muestra que la medición rigurosa no exige siempre recorrido material del dominio medido. Muchas magnitudes fundamentales han sido inferidas por sombra, ángulo, paralaje, curvatura, periodo, ley dinámica, expansión o patrón de escala. Esta tradición no rebaja el carácter científico del cálculo; al contrario, funda una parte esencial de la matemática aplicada a la astronomía, la geodesia y la cosmología. El punto decisivo no es tocar el límite del dominio, sino declarar adecuadamente el observador, el modelo, la unidad, el supuesto geométrico, el procedimiento de inferencia y el error residual. La presente determinación se inscribe en esa tradición, pero añade la restricción SV: ningún retorno metrológico externo puede confundirse con totalidad absoluta, fundamento ontológico o cierre físico no declarado (Lloret Egea, 2026a, 2026b).

### IV.II. Eratóstenes y la clausura geométrica de un dominio terrestre

Eratóstenes constituye el antecedente clásico más limpio para esta investigación porque calculó una magnitud global terrestre sin recorrer físicamente la circunferencia de la Tierra. Según la tradición conservada, comparó la incidencia solar en Syene y Alejandría, observó que en Alejandría el Sol formaba un ángulo aproximado de `7,2°` respecto de la vertical cuando en Syene los rayos caían verticalmente, y utilizó la distancia estimada entre ambas ciudades para inferir la circunferencia terrestre, obteniendo `250.000` estadios (Encyclopaedia Britannica, 2026a). La American Physical Society recuerda que la incertidumbre histórica sobre la longitud exacta del estadio afecta a la traducción moderna del resultado, pero sitúa el cálculo en el rango correcto de la circunferencia terrestre (American Physical Society, 2006).

La enseñanza metodológica de Eratóstenes no reside sólo en el número obtenido, sino en la estructura de su operación: dos puntos accesibles, un fenómeno común, una diferencia angular, una hipótesis geométrica global y una extrapolación controlada. La Tierra no fue medida por recorrido total, sino por clausura geométrica del dominio a partir de señales locales. Esta estructura es relevante para el presente trabajo porque la clausura esférica auxiliar del Universo Físico observable tampoco exige recorrer su límite; exige declarar el dominio `Ω_F`, el modelo `𝓜_sph`, el radio equivalente `R̄_Ω`, la unidad externa y el residual de retorno.

### IV.III. Medición astronómica por ángulo, paralaje y horizonte

La tradición antigua y medieval ofrece otros ejemplos de acotación de dominios no recorridos. Hiparco calculó la distancia lunar mediante paralaje, y Britannica recoge que determinó una distancia de aproximadamente `59` radios ecuatoriales terrestres, en relación próxima al valor moderno medio de `60,2` radios terrestres (Encyclopaedia Britannica, 2026c). Al-Biruni propuso un método geodésico distinto: estimar el radio terrestre a partir de la altura de una montaña y el ángulo de depresión del horizonte, usando trigonometría; su procedimiento muestra de nuevo que una magnitud global puede inferirse desde una configuración local y una geometría declarada, aun con limitaciones instrumentales y atmosféricas (Sparavigna, 2014).

Estos antecedentes establecen una continuidad epistemológica clara: el dominio puede ser mayor que el recorrido disponible, siempre que exista una mediación formal suficientemente declarada. La presente determinación no toma esos ejemplos como autoridad numérica para el universo observable; los toma como patrón metodológico: una magnitud global se calcula por estructura, no por posesión física del borde. En lenguaje SV, ello exige dominio, coordenación, unidad, frontera o límite equivalente, residual y retorno.

### IV.IV. Newton y la proyección matemática de leyes universales

Newton representa un segundo antecedente decisivo, no geodésico sino dinámico: la formulación matemática puede proyectar una ley física de alcance universal sin exigir presencia material en todos los puntos del dominio. La Royal Society describe la *Philosophiae Naturalis Principia Mathematica* como la obra que definió durante largo tiempo la comprensión del universo físico, y Cambridge University Library conserva materiales vinculados a la primera edición y a la transmisión textual del *Principia* (Royal Society, 2014; Cambridge University Library, s. f.). La relevancia para este documento es precisa: Newton no necesitó salir de su mesa, su papel y su pluma para visualizar una proyección de Ley de Gravitación Universal; necesitó geometría, dinámica, observación heredada, formalización y control lógico del dominio.

Esta analogía no convierte la presente determinación en una ley dinámica newtoniana. Sólo subraya una condición general de la ciencia matemática: el cálculo formal puede alcanzar dominios no recorridos cuando el aparato conceptual es público, reproducible, tipado y contrastable. En este documento, esa exigencia se expresa por la recta generatriz, el vector director `v_Ω`, el tramo operativo `ℓ_{Ω,[0,1]}^SV`, la ecuación de cierre `𝓖_Ω^SV(O;s)=0_Ω` y la clausura esférica auxiliar que permite calcular `R̄_Ω` y `V_Ω`.

### IV.V. Universo observable, horizonte de observación y diámetro de contraste

La cosmología contemporánea distingue entre universo observable y universo completo. Britannica define el universo observable como la región que puede observarse efectiva o teóricamente con ayuda de tecnología, y lo diferencia del universo total, que podría ser infinito y carecer de bordes espaciales; la misma fuente sitúa el diámetro del universo observable en aproximadamente `93.000 millones de años luz`, con radio de algo más de `46.000 millones de años luz` desde la Tierra por efecto de la expansión espacial (Encyclopaedia Britannica, 2026b). Esta distinción coincide con la restricción principal del presente trabajo: `Ω_F ≠ 𝓣`.

Por tanto, el valor `93.000.000.000 ly` no debe leerse como frontera absoluta del ser ni como diámetro de la totalidad. Es una convención de contraste para el dominio observable retornado. El SV no convierte ese valor en fundamento; lo admite como entrada externa bajo condición de modelo, unidad, transductor, residual y dictamen. La esfera perfecta equivalente `∂S_Ω` es una clausura geométrica auxiliar, no una superficie física rígida.

### IV.VI. Cosmometría contemporánea: CMB, expansión, BAO, cartografía 3D y misiones de gran escala

La ciencia actual estudia el tamaño, la historia y la estructura del universo observable mediante múltiples retornos: fondo cósmico de microondas, parámetros cosmológicos, supernovas, oscilaciones acústicas bariónicas, lentes gravitacionales, cartografía de galaxias y grandes sondeos espectroscópicos. Planck 2018 consolidó un conjunto de parámetros cosmológicos de alta precisión dentro del modelo ΛCDM, incluyendo `H₀ = 67,4 ± 0,5 km s−1 Mpc−1` y `Ω_m = 0,315 ± 0,007`, mostrando que el tamaño observable depende de un aparato cosmológico y no de una regla física extendida hasta un borde material (Planck Collaboration et al., 2020).

Euclid, por su parte, está diseñado para explorar la composición y evolución del universo oscuro mediante un mapa tridimensional de la estructura a gran escala, observando miles de millones de galaxias hasta `10.000 millones de años luz` y más de un tercio del cielo; ESA explicita que la misión estudia cómo se ha expandido el universo y cómo se ha formado la estructura cósmica, con el fin de inferir propiedades de energía oscura, materia oscura y gravedad (European Space Agency, s. f.-a, s. f.-b). DESI, desde otro plano instrumental, utiliza oscilaciones acústicas bariónicas como regla estándar cosmológica, y sus resultados DR2 de 2025 reúnen mediciones basadas en tres años de operación, con especial atención a la historia de expansión y a las posibles tensiones en la interpretación de la energía oscura (Dark Energy Spectroscopic Instrument, 2025).

Estos programas no sustituyen la presente determinación SV. Su valor aquí es de estado del arte: muestran que la cosmometría contemporánea trabaja mediante patrones, reglas estándar, mapas, modelos y retornos instrumentales, no mediante acceso directo a una frontera material final. La determinación SV conserva esta disciplina de contraste, pero añade una capa formal propia: no se acepta ningún valor cosmológico sin dominio, unidad, modelo, residual, transductor y exclusión explícita de la totalidad absoluta.

### IV.VII. Metrología astronómica: año luz juliano y patrón lunar

La metrología externa de este documento usa dos referencias principales. La primera es el año luz juliano: la IAU indica que el año luz es la distancia recorrida por la luz en vacío durante un año juliano, con valor `9.460.730.472.580,8 km`, y precisa que el año juliano equivale a `365,25` días, es decir, `31.557.600` segundos (International Astronomical Union, s. f.). La segunda es la distancia media Tierra–Luna: NASA Space Place fija la distancia media en `238.855` millas, equivalentes a `384.400 km`, y recuerda que la órbita lunar no es circular perfecta, por lo que el valor debe leerse como media (National Aeronautics and Space Administration, s. f.).

Ambas referencias son externas y auxiliares. El año luz permite traducir el radio medio equivalente a kilómetros y metros; la distancia media Tierra–Luna permite ofrecer una escala humana de lectura sin convertir `LD` en unidad constitutiva del SV. La precisión del resultado lunar se conserva en forma fraccionaria exacta y se acompaña de una cota explícita de error decimal.

### IV.VIII. Posición del Sistema Vectorial SV ante la tradición de cálculo indirecto

El SV no se limita a repetir el gesto histórico de la medición indirecta. Lo formaliza mediante una disciplina de admisibilidad: toda magnitud debe declarar dominio, tipo, frontera o límite equivalente, unidad, retorno, residual y dictamen. Por eso el presente documento no dice que el universo observable “sea” una esfera perfecta, ni que el centro terrestre sea centro cosmológico, ni que `0_SV` se espacialice. Dice que, si el dominio `Ω_F` se devuelve bajo una clausura esférica auxiliar, entonces puede declararse un radio medio equivalente, un volumen auxiliar, un patrón lunar y una distancia relativa desde `C_⊕` hasta `∂S_Ω`.

La consecuencia es una continuidad fuerte con la ciencia histórica y contemporánea, pero sin subordinación conceptual. Eratóstenes, Hiparco, Al-Biruni y Newton muestran que la ciencia puede calcular dominios no recorridos; Planck, Euclid y DESI muestran que la cosmometría actual sigue operando por patrones, mapas, inferencias y retornos. El SV exige, además, que ningún retorno se convierta en totalidad y que ningún modelo auxiliar se tome como borde ontológico. Ésta es la razón por la que el radio, el volumen, el patrón lunar y la distancia relativa se formulan como clausura geométrica auxiliar dentro del dominio observable retornado, no como medición del TODO.

## V. Alcance formal

Esta determinación pertenece a la teoría de la distancia absoluta y relativa entre observables del Universo. Su objeto no es medir la totalidad absoluta, ni convertir el Universo Físico observable en totalidad de lo real, sino formular una clausura geométrica auxiliar aplicable al dominio `Ω_F` cuando éste se toma como Universo Físico observable retornado dentro del Sistema Vectorial SV (Lloret Egea, 2026a).

La restricción que gobierna todo el desarrollo es:

`Ω_F ≠ 𝓣`,

donde `𝓣` designa la totalidad absoluta. En consecuencia, el cálculo del radio medio equivalente, del volumen esférico auxiliar, del patrón lunar y de la distancia relativa desde el centro de la Tierra hasta el límite de la esfera equivalente no mide el TODO, no mide la totalidad de lo real, no espacializa `0_SV`, no convierte el origen formal en centro métrico y no transforma el horizonte observable en borde absoluto. Lo que se declara es una clausura geométrica auxiliar dentro de un dominio observable retornado, con magnitud, unidad, modelo, transductor, residual y retorno metrológico explícitos (Lloret Egea, 2026a, 2026b).

La distancia absoluta conserva su régimen propio:

`D_abs^{SV}(p_i,0_SV)`,

entendida como referencia formal restringida de un observable declarado respecto del origen formal `0_SV`, sin convertir este origen en punto espacial, instante físico, Big Bang ni centro métrico. Por tanto, esta determinación no formula:

`d(Ω_F,0_SV)=R̄_Ω`.

La distancia relativa que se declara responde a otra estructura lógico-formal. Expresado de manera formal:

`D_rel^Ω(C_⊕,∂S_Ω;R̄_Ω,LD,𝓜_sph,𝔛_{SI↔SV})`.

Donde `C_⊕` designa el centro de la Tierra tomado como punto metrológico de referencia del retorno externo; `∂S_Ω` designa el límite de la esfera perfecta equivalente del Universo Físico observable; `R̄_Ω` designa el radio medio equivalente bajo clausura geométrica auxiliar; `LD` designa la distancia media Tierra–Luna usada como patrón externo auxiliar; `𝓜_sph` designa el modelo geométrico declarado de esfera perfecta equivalente; y `𝔛_{SI↔SV}` designa el retorno metrológico entre las unidades externas de contraste y la lectura interna del SV (Lloret Egea, 2026a, 2026c).

Los términos `C_⊕` y `∂S_Ω` pertenecen al retorno metrológico externo de la clausura auxiliar, no al espacio afín interno `𝔼_Ω^SV` sin mediación. Su admisión en la fórmula de distancia relativa exige el modelo declarado `𝓜_sph`, el patrón externo `LD` cuando proceda, y el transductor `𝔛_{SI↔SV}`. De esta forma, la lectura externa no se mezcla directamente con la coordenación interna del teorema, sino que queda mediada por retorno, unidad, modelo y residual declarados (Lloret Egea, 2026a, 2026c).

Esta investigación no calcula una distancia de la totalidad, sino una distancia relativa declarada dentro del dominio observable retornado. No calcula una edad, radio o profundidad impuestos por la ciencia contemporánea como fuente de verdad; utiliza datos externos sólo como conjunto de contraste, retorno metrológico y lectura metrológica externa cuando el SV declara el transductor correspondiente.

En el plano físico de contraste, `93.000.000.000 ly` entra como convención declarada de diámetro esférico equivalente del universo observable; `1 ly = 9.460.730.472.580,8 km` entra como conversión metrológica del año luz juliano; y `LD := 384.400 km` entra como patrón lunar auxiliar. Ninguno de estos valores funda el SV. Todos ellos operan como retornos externos bajo dominio, unidad, modelo, residual y transductor declarados (Encyclopaedia Britannica, 2026b; International Astronomical Union, s. f.; National Aeronautics and Space Administration, s. f.).

## VI. Teorema de la recta generatriz del Universo Físico observable

La recta generatriz definida en este teorema recibe, dentro de la nomenclatura interna del Sistema Vectorial SV, la denominación `Recta-Ómicron SV16`, con forma abreviada `Recta_Οmi_SV16`. Esta denominación identifica de manera estable la recta asociada al cierre uniparamétrico del Universo Físico observable retornado, y mantiene continuidad nominal con la formulación SV16-Ómicron ya fijada en trabajos previos del SV (Lloret Egea, 2026d, 2026e).

La denominación `Recta-Ómicron SV16` no interviene como premisa física, no introduce una constante, no modifica la ecuación local `𝓖_Ω^SV(O;s)=0_Ω`, no altera el cálculo del radio medio equivalente, no funda el patrón lunar y no convierte esta determinación cosmométrica en una derivación química. Su función es nominal y clasificatoria: nombrar la recta generatriz del dominio `Ω_F` una vez declarados el espacio afín tipado, el vector director, el tramo operativo, el residual y el retorno metrológico.

La continuidad nominal se vincula con la formulación SV16-Ómicron recogida en *Directed determination of the chemical element SV-399 — Actinium (Ac) + 3 Oganesson (Og) + Tungsten/Wolfram (W): Spain and Portugal as priority prospecting targets — (SV16-Ómicron)*, DOI: https://doi.org/10.21428/39829d0b.11d9224e, y con *Determinación dirigida del elemento químico SV-399 — Actinio (Ac) + 3 Oganesón (Og) + Tungsteno/Wolframio (W)*, DOI: https://doi.org/10.21428/39829d0b.5211d837. Estas referencias cumplen aquí una función de trazabilidad nominal interna, no de fundamento físico del teorema (Lloret Egea, 2026d, 2026e).

Sea `Ω_F` el Universo Físico observable considerado como dominio físico realizado dentro del Sistema Vectorial SV, con la restricción expresa:

`Ω_F ≠ 𝓣`,

donde `𝓣` designa la totalidad absoluta. El dominio `Ω_F` no se identifica con el TODO absoluto del SV, ni con la totalidad de lo real, ni con un exterior físico desde el cual pudiera medirse la totalidad. Se trata de un dominio observable retornado, interno y formulable (Lloret Egea, 2026a, 2026b).

Sea:

`𝔼_Ω^SV := E_A^SV × E_R^SV × E_D^SV`

el espacio afín tipado de coordenación interna del Universo Físico observable, cuyos puntos tienen la forma:

`X = (A_X, R_X, D_X)`.

`E_A^SV` es el dominio afín tipado de edades SV de retorno, `E_R^SV` es el dominio afín tipado de escalas radiales de retorno y `E_D^SV` es el dominio afín tipado de profundidades de retorno. La terna `(A,R,D)` no se toma como espacio euclídeo físico ordinario ni como métrica externa no declarada, sino como producto afín tipado de tres magnitudes internas de retorno: `A`, edad SV del observable retornado; `R`, escala radial de retorno declarada por el SV; y `D`, profundidad de retorno declarada por el SV.

Cada componente tipada admite origen, unidad interna declarada y acción escalar de retorno. Por tanto, toda expresión que use acción escalar sobre el punto terminal se entiende componente a componente dentro de cada dominio tipado, no como mezcla material indiferenciada de edad, radio y profundidad.

El espacio vectorial residual asociado al producto afín tipado se declara como:

`𝓡_Ω^SV := V_A^SV × V_R^SV × V_D^SV`.

Donde `V_A^SV`, `V_R^SV` y `V_D^SV` designan los espacios vectoriales asociados a los dominios afines tipados `E_A^SV`, `E_R^SV` y `E_D^SV`. Por tanto, la diferencia entre puntos del espacio afín `𝔼_Ω^SV` no se interpreta como un nuevo punto afín, sino como residual tipado en `𝓡_Ω^SV`.

Estas tres coordenadas no se toman de la ciencia contemporánea como fuente de verdad, sino que pertenecen a la formulación interna del SV. La ciencia contemporánea sólo podrá entrar después como conjunto de datos de contraste, retorno metrológico o transducción externa (Lloret Egea, 2026a, 2026c).

Por la formulación SV de edades relativas, la totalidad absoluta no admite edad física; el dominio observable retornado sí admite edad concreta de retorno. Por la Línea del Umbral SV, la recta no se reduce al origen: el origen formal reúne potencial nulo e intensidad nula, mientras que un punto no nulo situado sobre una directriz conserva intensidad positiva. Esta distinción permite separar `O_∅=(0_A,0_R,0_D)` del punto terminal interno `P_Ω^SV`, sin confundir neutralidad formal con realización de dominio (Lloret Egea, 2026f, 2026g).

Se fija, por tanto, el punto terminal interno del observable físico retornado:

`P_Ω^SV = (A_Ω^SV, R_Ω^SV, D_Ω^SV)`,

donde `A_Ω^SV` es la edad SV del observable retornado y `R_Ω^SV`, `D_Ω^SV` son las coordenadas internas de escala radial de retorno y profundidad de retorno asociadas al mismo dominio. Ninguna de estas tres coordenadas se toma como valor impuesto por la cosmología contemporánea. Su función es estructural: declarar el cierre uniparamétrico del observable físico retornado en el espacio `𝔼_Ω^SV`.

Sea:

`O_∅ = (0_A,0_R,0_D)`,

el origen formal tipado de coordenación. Este origen no se toma como cuerpo físico, instante temporal, vacío sustancial, totalidad absoluta ni geometría fundante. Es sólo el punto nulo formal desde el cual se escribe la coordenación interna del producto afín tipado.

Se define el vector director asociado al desplazamiento desde el origen formal tipado hasta el punto terminal interno como:

`v_Ω := Δ(O_∅→P_Ω^SV) = P_Ω^SV − O_∅ ∈ 𝓡_Ω^SV`.

La igualdad anterior se entiende como diferencia afín entre dos puntos de `𝔼_Ω^SV`, cuyo resultado pertenece al espacio vectorial residual asociado `𝓡_Ω^SV`. En la carta afín tipada con origen `O_∅`, el vector `v_Ω` tiene coordenadas:

`v_Ω ≡ Coord(P_Ω^SV) = (A_Ω^SV, R_Ω^SV, D_Ω^SV)`.

Esta identificación es coordenada y dependiente del origen formal tipado declarado; no reduce el punto afín `P_Ω^SV` a un residual indiferenciado.

La Línea del Umbral SV fija que toda recta admisible posee directriz y que todo tránsito entre dominios exige dirección, dominio, frontera, traza, residual y retorno. En consecuencia, la recta generatriz del Universo Físico observable no se introduce como imagen geométrica aislada, sino como directriz local de retorno en el espacio `𝔼_Ω^SV`, subordinada a la ecuación rectora superior del Sistema Vectorial SV (Lloret Egea, 2026g).

Si:

`P_Ω^SV ≠ O_∅`,

entonces:

`v_Ω = Δ(O_∅→P_Ω^SV) ≠ 0_Ω`.

Por geometría afín, un punto inicial y un vector director no nulo determinan una única recta. Por tanto, existe una única recta generatriz completa que pasa por `O_∅` y `P_Ω^SV`:

`ℓ_Ω^SV(s) := O_∅ + s v_Ω`,

con:

`s ∈ ℝ`.

Sustituyendo el vector director declarado:

`ℓ_Ω^SV(s) := O_∅ + s Δ(O_∅→P_Ω^SV)`,

con:

`s ∈ ℝ`.

El tramo operativo de retorno del dominio observable retornado se define como:

`ℓ_{Ω,[0,1]}^SV(s) := O_∅ + s v_Ω`,

con:

`0 ≤ s ≤ 1`.

En la carta afín tipada con origen `O_∅`, y sólo como abreviatura coordenada, puede escribirse:

`ℓ_Ω^SV(s)=sP_Ω^SV`.

Del mismo modo, el tramo operativo puede escribirse abreviadamente como:

`ℓ_{Ω,[0,1]}^SV(s)=sP_Ω^SV`,

con:

`0 ≤ s ≤ 1`.

En forma coordenada, el tramo operativo queda:

`ℓ_{Ω,[0,1]}^SV(s) = (sA_Ω^SV, sR_Ω^SV, sD_Ω^SV)`,

con:

`0 ≤ s ≤ 1`.

Esta recta no afirma que todo objeto físico bruto tenga como radio real o distancia real las coordenadas de `ℓ_Ω^SV`. Afirma que todo observable físico admisible del Universo Físico observable, incluido el propio dominio `Ω_F` cuando es tratado como observable retornado, posee una proyección interna de retorno que puede cerrar sobre el tramo operativo de la recta generatriz.

Se distingue, por tanto, entre dominio de retorno declarable y dominio de admisibilidad proyectiva.

Sea:

`Ω_F^ret ⊂ Ω_F`

el conjunto de observables físicos con dominio, retorno y triple interno declarable. Formalmente:

`O ∈ Ω_F^ret ⇔ Dom(O) ∧ Ret(O) ∧ π_Ω(O)=(A(O),R(O),D(O)) declarado`.

Si falta dominio, retorno o coordenación interna suficiente, el caso no se fuerza: queda en `U`, entendida aquí como indeterminación honesta de no cierre.

Sea, para todo `O ∈ Ω_F^ret`:

`π_Ω(O) = (A(O), R(O), D(O)) ∈ 𝔼_Ω^SV`,

la proyección interna de retorno de `O`.

La aplicación `π_Ω` se entiende como aplicación interna de retorno y proyección estructural, no como proyección ortogonal euclídea. No presupone métrica externa no declarada ni distancia perpendicular en un espacio físico ordinario.

La ecuación canónica local del teorema, subordinada a la ecuación rectora superior `𝓔★_TODO,SV(Γ_U;τ)=0`, es la ecuación vectorial tipada de residual proyectivo:

`𝓖_Ω^SV(O;s) := π_Ω(O) − ℓ_{Ω,[0,1]}^SV(s)`.

Como:

`ℓ_{Ω,[0,1]}^SV(s)=O_∅+s v_Ω`,

también puede escribirse:

`𝓖_Ω^SV(O;s) := π_Ω(O) − (O_∅+s v_Ω)`.

En la carta afín tipada con origen `O_∅`, esta misma ecuación admite la abreviatura coordenada:

`𝓖_Ω^SV(O;s) := π_Ω(O) − sP_Ω^SV`.

En forma coordenada tipada:

`𝓖_Ω^SV(O;s) := (A(O)−sA_Ω^SV, R(O)−sR_Ω^SV, D(O)−sD_Ω^SV)`.

Su codominio residual no es el propio producto afín `E_A^SV × E_R^SV × E_D^SV`, sino el espacio vectorial asociado:

`𝓖_Ω^SV(O;s) ∈ 𝓡_Ω^SV := V_A^SV × V_R^SV × V_D^SV`.

El cero residual tipado es:

`0_Ω := (0_A^V,0_R^V,0_D^V)`.

Por tanto, el cierre proyectivo local se escribe:

`𝓖_Ω^SV(O;s) = 0_Ω`.

Con:

`P_Ω^SV = (A_Ω^SV, R_Ω^SV, D_Ω^SV)`,

`π_Ω(O) = (A(O), R(O), D(O))`,

`0 ≤ s ≤ 1`,

`P_Ω^SV ≠ O_∅`.

La ecuación `𝓖_Ω^SV(O;s)=0_Ω` no es ecuación rectora del Sistema Vectorial SV. Es la ecuación local de cierre proyectivo del Universo Físico observable retornado. Su función es subordinada: no compite con `𝓔★_TODO,SV(Γ_U;τ)=0`, sino que opera dentro del dominio observable declarado.

Se dice que un observable `O` pertenece al dominio de admisibilidad proyectiva `Ω_F^adm` si y sólo si pertenece al dominio de retorno declarable y existe un único parámetro `s_O ∈ [0,1]` que anula el residual proyectivo. Formalmente:

`O ∈ Ω_F^adm ⇔ O ∈ Ω_F^ret ∧ ∃! s_O ∈ [0,1] : 𝓖_Ω^SV(O;s_O)=0_Ω`.

Esto equivale a:

`O ∈ Ω_F^adm ⇔ O ∈ Ω_F^ret ∧ ∃! s_O ∈ [0,1] : π_Ω(O) − ℓ_{Ω,[0,1]}^SV(s_O)=0_Ω`.

En la carta afín tipada con origen `O_∅`, esta condición admite la escritura abreviada:

`O ∈ Ω_F^adm ⇔ O ∈ Ω_F^ret ∧ ∃! s_O ∈ [0,1] : π_Ω(O) − s_OP_Ω^SV = 0_Ω`.

En tal caso:

`π_Ω(O) = ℓ_{Ω,[0,1]}^SV(s_O)`.

Y, en forma coordenada abreviada:

`π_Ω(O) = s_OP_Ω^SV`.

Por tanto:

`π_Ω(O) ∈ ℓ_{Ω,[0,1]}^SV ⊂ ℓ_Ω^SV`.

La pertenencia material directa:

`O ∈ ℓ_Ω^SV`

sólo se admite cuando el objeto ya ha sido formulado como punto de retorno uniparamétrico en `𝔼_Ω^SV`. En los demás casos, lo correcto es la pertenencia proyectiva:

`π_Ω(O) ∈ ℓ_{Ω,[0,1]}^SV`.

Si el punto proyectado pertenece a `ℓ_{Ω,[0,1]}^SV` y las tres componentes de `P_Ω^SV` son no nulas, entonces una sola coordenada determina el parámetro `s_O` y, por tanto, determina las otras dos coordenadas internas de retorno. La condición de no nulidad terminal no se formula por producto de magnitudes heterogéneas, sino por conjunción tipada:

`A_Ω^SV ≠ 0_A ∧ R_Ω^SV ≠ 0_R ∧ D_Ω^SV ≠ 0_D`.

Bajo esta condición, se obtiene:

si se introduce `A(O)`, entonces:

`s_O = A(O)/A_Ω^SV`;

si se introduce `R(O)`, entonces:

`s_O = R(O)/R_Ω^SV`;

si se introduce `D(O)`, entonces:

`s_O = D(O)/D_Ω^SV`.

Una vez determinado `s_O`, quedan declaradas las tres coordenadas proyectivas:

`A(O) = s_OA_Ω^SV`,

`R(O) = s_OR_Ω^SV`,

`D(O) = s_OD_Ω^SV`.

La forma normalizada de la proyección se define como terna de razones adimensionales normalizadas:

`π̂_Ω(O) := (ρ_A(O),ρ_R(O),ρ_D(O))`.

Con:

`ρ_A(O):=A(O)/A_Ω^SV`.

`ρ_R(O):=R(O)/R_Ω^SV`.

`ρ_D(O):=D(O)/D_Ω^SV`.

Estas razones no mezclan materialmente edad, radio y profundidad; sólo comparan cada coordenada con su propio terminal tipado. Bajo cierre proyectivo:

`π̂_Ω(O) = (s_O,s_O,s_O)`.

Esta forma normalizada explicita que la proyección cerrada conserva una sola directriz interna de retorno: las tres coordenadas tipadas no se confunden entre sí, pero sus razones normalizadas coinciden en el parámetro único `s_O`.

Por tanto, todo observable físico admisible posee una proyección interna de retorno sobre el tramo operativo de la recta generatriz del Universo Físico observable, y en esa proyección una coordenada no nula determina las otras dos. La ciencia contemporánea no funda este resultado; sólo puede contrastarlo, traducirlo o devolverlo en unidades externas cuando el SV declare el transductor correspondiente.

## VII. Ecuación del teorema

La ecuación local única que sostiene el teorema de la recta generatriz del Universo Físico observable es:

`𝓖_Ω^SV(O;s) := π_Ω(O) − ℓ_{Ω,[0,1]}^SV(s) = 0_Ω`.

Con:

`ℓ_{Ω,[0,1]}^SV(s)=O_∅+s Δ(O_∅→P_Ω^SV)`,

`π_Ω(O) = (A(O), R(O), D(O))`,

`P_Ω^SV = (A_Ω^SV, R_Ω^SV, D_Ω^SV)`,

`0 ≤ s ≤ 1`,

`0_Ω=(0_A^V,0_R^V,0_D^V)`.

En la carta afín tipada con origen `O_∅`, la ecuación puede escribirse abreviadamente como:

`𝓖_Ω^SV(O;s) := π_Ω(O) − sP_Ω^SV = 0_Ω`.

En forma desarrollada:

`𝓖_Ω^SV(O;s) = (A(O), R(O), D(O)) − s(A_Ω^SV, R_Ω^SV, D_Ω^SV) = (0_A^V,0_R^V,0_D^V)`.

Equivalente en coordenadas residuales, pero no como tres fórmulas independientes:

`A(O) − sA_Ω^SV = 0_A^V`,

`R(O) − sR_Ω^SV = 0_R^V`,

`D(O) − sD_Ω^SV = 0_D^V`.

La forma coordenada se subordina a la ecuación vectorial única. Por tanto, la formulación local no es una terna de ecuaciones rectoras, sino una sola ecuación vectorial de residual nulo:

`𝓖_Ω^SV(O;s)=0_Ω`.

El cierre proyectivo completo exige existencia y unicidad del parámetro:

`∃! s_O ∈ [0,1] : 𝓖_Ω^SV(O;s_O)=0_Ω`.

Bajo la condición de no nulidad de las tres componentes terminales:

`A_Ω^SV ≠ 0_A ∧ R_Ω^SV ≠ 0_R ∧ D_Ω^SV ≠ 0_D`,

la misma ecuación permite recuperar el parámetro desde cualquiera de las tres razones adimensionales normalizadas:

`ρ_A(O) = ρ_R(O) = ρ_D(O) = s_O`.

Esto equivale a:

`s_O = A(O)/A_Ω^SV = R(O)/R_Ω^SV = D(O)/D_Ω^SV`.

Esta igualdad de cocientes no es una segunda ecuación local, ni una ecuación rectora paralela. Es la forma normalizada y despejada de `𝓖_Ω^SV(O;s)=0_Ω` bajo condición de no nulidad.

La Línea del Umbral SV confirma la estructura de esta ecuación local: toda recta posee directriz; todo tránsito admisible exige vector director; todo cierre exige residual nulo o residual gobernado. En este teorema, `v_Ω = Δ(O_∅→P_Ω^SV)` actúa como vector director local del retorno proyectivo, y `𝓖_Ω^SV(O;s)=0_Ω` declara anulación del residual proyectivo entre la proyección interna del observable y el tramo operativo de la recta generatriz del dominio observable retornado (Lloret Egea, 2026g).

La forma normalizada:

`π̂_Ω(O)=(s_O,s_O,s_O)`

es la lectura tipada de la directriz única. No identifica edad, radio y profundidad como magnitudes materiales iguales; declara que, una vez normalizadas por sus terminales propios, las tres razones internas de retorno coinciden en un mismo parámetro estructural.

## VIII. Demostración

Sea:

`𝔼_Ω^SV := E_A^SV × E_R^SV × E_D^SV`

el espacio afín tipado de coordenación interna del Universo Físico observable en el SV. Sus elementos son triples de retorno:

`X = (A_X, R_X, D_X)`.

Sea:

`𝓡_Ω^SV := V_A^SV × V_R^SV × V_D^SV`

el espacio vectorial residual asociado al producto afín tipado `𝔼_Ω^SV`.

Sea:

`O_∅ = (0_A,0_R,0_D)`,

el origen formal tipado de coordenación. Sea:

`P_Ω^SV = (A_Ω^SV, R_Ω^SV, D_Ω^SV)`,

el punto terminal interno del observable físico retornado. Por hipótesis:

`P_Ω^SV ≠ O_∅`.

Se define:

`v_Ω := Δ(O_∅→P_Ω^SV) = P_Ω^SV − O_∅ ∈ 𝓡_Ω^SV`.

Como `P_Ω^SV ≠ O_∅`, se obtiene:

`v_Ω ≠ 0_Ω`.

En la carta afín tipada con origen `O_∅`, el vector director tiene coordenadas:

`v_Ω ≡ Coord(P_Ω^SV) = (A_Ω^SV, R_Ω^SV, D_Ω^SV)`.

Esta equivalencia es una identificación coordenada del vector director asociado al desplazamiento desde el origen formal tipado hasta el punto terminal interno, no una reducción del punto afín `P_Ω^SV` a residual indiferenciado.

La Línea del Umbral SV fija que una recta conserva una dirección propia y que el origen formal no agota la recta cuando existe intensidad positiva en puntos no nulos. En la recta polar `μ=λ`, el vector directriz `υ_U^SV=(1,1)` conserva la igualdad polar sin reducir todo punto al origen. De modo análogo, en el espacio `𝔼_Ω^SV`, el vector `v_Ω = Δ(O_∅→P_Ω^SV)` actúa como directriz local de la recta generatriz del observable retornado: todo punto del tramo operativo `O_∅+s v_Ω`, con `0≤s≤1`, conserva la orientación uniparamétrica de retorno respecto del punto terminal interno.

En geometría afín, un punto inicial y un vector director no nulo determinan una recta. Por tanto, existe la recta completa:

`ℓ_Ω^SV(s) = O_∅ + s v_Ω`,

con:

`s ∈ ℝ`.

Sustituyendo:

`v_Ω = Δ(O_∅→P_Ω^SV)`,

resulta:

`ℓ_Ω^SV(s) = O_∅ + s Δ(O_∅→P_Ω^SV)`,

con:

`s ∈ ℝ`.

En la carta afín tipada con origen `O_∅`, esta expresión admite la abreviatura coordenada:

`ℓ_Ω^SV(s)=sP_Ω^SV`.

El tramo operativo de retorno queda definido por restricción del parámetro:

`ℓ_{Ω,[0,1]}^SV(s)=O_∅+s v_Ω`,

con:

`0≤s≤1`.

En forma coordenada:

`ℓ_{Ω,[0,1]}^SV(s) = (sA_Ω^SV, sR_Ω^SV, sD_Ω^SV)`,

con:

`0 ≤ s ≤ 1`.

Queda probada la existencia de la recta generatriz completa y del tramo operativo de retorno.

Para demostrar la unicidad, supóngase que existen dos rectas `ℓ_1` y `ℓ_2` que pasan por `O_∅` y por `P_Ω^SV`. Toda recta que pasa por esos dos puntos tiene como vector director un vector proporcional a:

`Δ(O_∅→P_Ω^SV)`.

Pero:

`Δ(O_∅→P_Ω^SV) = v_Ω`,

y este vector es no nulo en `𝓡_Ω^SV`. Por tanto, `ℓ_1` y `ℓ_2` pasan por el mismo punto y poseen vectores directores proporcionales al mismo vector no nulo. Luego tienen el mismo soporte geométrico:

`ℓ_1 = ℓ_2`.

La recta generatriz es, por tanto, única.

Se define ahora el dominio de retorno declarable:

`Ω_F^ret ⊂ Ω_F`.

Un observable `O` pertenece a `Ω_F^ret` si declara dominio, retorno y triple interno de retorno:

`π_Ω(O) = (A(O), R(O), D(O)) ∈ 𝔼_Ω^SV`.

Esta proyección no afirma que el objeto físico bruto `O` pertenezca materialmente a la recta. Sólo declara el triple interno de retorno con el que el SV evalúa el observable en el espacio `𝔼_Ω^SV`. Si falta dominio, retorno o coordenación suficiente, el caso permanece en `U`.

Se introduce la ecuación local de cierre proyectivo:

`𝓖_Ω^SV(O;s) := π_Ω(O) − ℓ_{Ω,[0,1]}^SV(s)`.

Como:

`ℓ_{Ω,[0,1]}^SV(s)=O_∅+s v_Ω`,

se obtiene:

`𝓖_Ω^SV(O;s) := π_Ω(O) − (O_∅+s v_Ω)`.

En la carta afín tipada con origen `O_∅`, esta expresión admite la escritura abreviada:

`𝓖_Ω^SV(O;s) := π_Ω(O) − sP_Ω^SV`.

En forma residual tipada:

`𝓖_Ω^SV(O;s) := (A(O)−sA_Ω^SV, R(O)−sR_Ω^SV, D(O)−sD_Ω^SV)`.

Por tratarse de una diferencia entre puntos del espacio afín tipado, se cumple:

`𝓖_Ω^SV(O;s) ∈ 𝓡_Ω^SV`.

El cierre se produce si y sólo si existe un único parámetro `s_O ∈ [0,1]` tal que:

`𝓖_Ω^SV(O;s_O)=0_Ω`.

Es decir:

`π_Ω(O) − ℓ_{Ω,[0,1]}^SV(s_O) = 0_Ω`.

Por tanto:

`π_Ω(O) = ℓ_{Ω,[0,1]}^SV(s_O)`.

En la carta afín tipada con origen `O_∅`, esta igualdad admite la forma abreviada:

`π_Ω(O) = s_OP_Ω^SV`.

De ello se sigue:

`π_Ω(O) ∈ ℓ_{Ω,[0,1]}^SV`.

Como:

`ℓ_{Ω,[0,1]}^SV ⊂ ℓ_Ω^SV`,

también se cumple:

`π_Ω(O) ∈ ℓ_Ω^SV`.

Por tanto:

`∀O ∈ Ω_F^adm, π_Ω(O) ∈ ℓ_{Ω,[0,1]}^SV ⊂ ℓ_Ω^SV`.

Queda demostrado el cierre proyectivo por definición constructiva de admisibilidad y por unicidad de la recta afín generada por `O_∅` y `P_Ω^SV`.

Debe observarse que no se ha demostrado ni afirmado que el objeto físico bruto `O` pertenezca materialmente a la recta. Lo que se demuestra es que su proyección interna de retorno, una vez cerrado el residual local `𝓖_Ω^SV`, pertenece al tramo operativo de la recta generatriz. Por tanto, la forma correcta es:

`π_Ω(O) ∈ ℓ_{Ω,[0,1]}^SV`,

no:

`O ∈ ℓ_Ω^SV`,

salvo que previamente se declare que `O` ya está siendo tratado como punto proyectivo de retorno.

Demostrada la pertenencia proyectiva, se prueba ahora la determinación de dos coordenadas por una sola. Sea:

`π_Ω(O) = (A(O), R(O), D(O))`.

Como `π_Ω(O) ∈ ℓ_{Ω,[0,1]}^SV`, existe `s_O ∈ [0,1]` tal que:

`π_Ω(O) = ℓ_{Ω,[0,1]}^SV(s_O)`.

En la carta afín tipada con origen `O_∅`:

`π_Ω(O) = s_OP_Ω^SV`.

Sustituyendo:

`(A(O), R(O), D(O)) = s_O(A_Ω^SV, R_Ω^SV, D_Ω^SV)`.

Por igualdad de coordenadas:

`A(O) = s_OA_Ω^SV`,

`R(O) = s_OR_Ω^SV`,

`D(O) = s_OD_Ω^SV`.

Supóngase que se conoce `A(O)` y que:

`A_Ω^SV ≠ 0_A`.

Entonces:

`s_O = A(O)/A_Ω^SV`.

Sustituyendo ese valor de `s_O` en las otras dos coordenadas:

`R(O) = (A(O)/A_Ω^SV)R_Ω^SV`,

`D(O) = (A(O)/A_Ω^SV)D_Ω^SV`.

Luego `A(O)` determina `R(O)` y `D(O)` dentro de la proyección sobre `ℓ_{Ω,[0,1]}^SV`.

Supóngase ahora que se conoce `R(O)` y que:

`R_Ω^SV ≠ 0_R`.

Entonces:

`s_O = R(O)/R_Ω^SV`.

Sustituyendo:

`A(O) = (R(O)/R_Ω^SV)A_Ω^SV`,

`D(O) = (R(O)/R_Ω^SV)D_Ω^SV`.

Luego `R(O)` determina `A(O)` y `D(O)` dentro de la proyección sobre `ℓ_{Ω,[0,1]}^SV`.

Supóngase finalmente que se conoce `D(O)` y que:

`D_Ω^SV ≠ 0_D`.

Entonces:

`s_O = D(O)/D_Ω^SV`.

Sustituyendo:

`A(O) = (D(O)/D_Ω^SV)A_Ω^SV`,

`R(O) = (D(O)/D_Ω^SV)R_Ω^SV`.

Luego `D(O)` determina `A(O)` y `R(O)` dentro de la proyección sobre `ℓ_{Ω,[0,1]}^SV`.

Queda demostrado que, si las tres componentes terminales de `P_Ω^SV` son no nulas en sus tipos respectivos, cualquiera de las tres coordenadas no nulas de un punto proyectado determina el parámetro `s_O` y, con él, las otras dos coordenadas internas de retorno.

La forma normalizada lo expresa de manera compacta. Defínase la terna de razones adimensionales normalizadas:

`π̂_Ω(O) := (ρ_A(O),ρ_R(O),ρ_D(O))`.

Con:

`ρ_A(O):=A(O)/A_Ω^SV`.

`ρ_R(O):=R(O)/R_Ω^SV`.

`ρ_D(O):=D(O)/D_Ω^SV`.

Como:

`A(O) = s_OA_Ω^SV`,

`R(O) = s_OR_Ω^SV`,

`D(O) = s_OD_Ω^SV`,

se obtiene:

`ρ_A(O)=s_O`.

`ρ_R(O)=s_O`.

`ρ_D(O)=s_O`.

Por tanto:

`π̂_Ω(O) = (s_O,s_O,s_O)`.

El cierre proyectivo equivale a la coincidencia de las tres razones normalizadas en una sola directriz uniparamétrica, sin identificar materialmente edad, radio y profundidad.

Puede formularse también por reducción al absurdo. Supóngase que existe un observable físico admisible `O* ∈ Ω_F^adm` tal que:

`π_Ω(O*) ∉ ℓ_{Ω,[0,1]}^SV`.

Pero, por definición de admisibilidad proyectiva:

`O* ∈ Ω_F^adm ⇔ O* ∈ Ω_F^ret ∧ ∃! s_O* ∈ [0,1] : 𝓖_Ω^SV(O*;s_O*)=0_Ω`.

Luego:

`π_Ω(O*) = ℓ_{Ω,[0,1]}^SV(s_O*)`.

Y todo punto de la forma `ℓ_{Ω,[0,1]}^SV(s)`, con `0≤s≤1`, pertenece al tramo operativo de la recta generatriz. Por tanto:

`π_Ω(O*) ∈ ℓ_{Ω,[0,1]}^SV`.

Contradicción. No existe, por tanto, observable físico admisible cuya proyección de retorno quede fuera del tramo operativo de la recta generatriz.

Supóngase ahora que existe un punto proyectado `π_Ω(O)` en el tramo operativo de la recta tal que una coordenada no nula no determina las otras dos. Pero, al pertenecer a `ℓ_{Ω,[0,1]}^SV`, el punto posee la forma:

`π_Ω(O) = ℓ_{Ω,[0,1]}^SV(s_O)`.

En la carta afín tipada con origen `O_∅`:

`π_Ω(O) = s_OP_Ω^SV`.

Como las tres componentes de `P_Ω^SV` son no nulas en sus tipos respectivos, cualquiera de las tres coordenadas permite despejar el mismo parámetro `s_O`. Una vez fijado `s_O`, las tres coordenadas quedan fijadas por multiplicación escalar tipada. La suposición contradice la forma paramétrica del tramo operativo de la recta.

Por tanto, una coordenada no nula determina las otras dos dentro de la proyección sobre `ℓ_{Ω,[0,1]}^SV`.

Queda demostrado que `ℓ_Ω^SV` existe y es única si `P_Ω^SV ≠ O_∅`; que el tramo operativo `ℓ_{Ω,[0,1]}^SV` ordena el cierre proyectivo del observable retornado; que todo observable físico admisible posee una proyección de retorno sobre ese tramo operativo; y que, en esa proyección, si las tres componentes terminales son no nulas en sus dominios tipados, una sola coordenada no nula determina el parámetro estructural y, por tanto, determina las otras dos coordenadas internas de retorno. La ecuación local `𝓖_Ω^SV(O;s)=0_Ω` no funda el SV ni sustituye la ecuación rectora `𝓔★_TODO,SV(Γ_U;τ)=0`; sólo declara cierre proyectivo dentro del dominio observable retornado. La ciencia contemporánea no funda el resultado; sólo podrá aportar conjunto de datos de contraste, retorno metrológico o transducción externa cuando el SV declare el operador correspondiente. c.q.d. del teorema.

## IX. Radio medio equivalente del Universo Físico observable

Una vez fijado el teorema de la recta generatriz del Universo Físico observable, la determinación del radio medio debe formularse como clausura geométrica auxiliar, no como fundamento externo del SV. El dominio `Ω_F` no se identifica con la totalidad absoluta `𝓣`; se trata de un dominio observable retornado, interno y formulable. Por tanto, el radio medio aquí calculado no mide el TODO absoluto, ni la totalidad de lo real, ni un exterior físico absoluto. Calcula el radio de la esfera perfecta que encerraría el mismo volumen declarado para el Universo Físico observable bajo retorno metrológico.

Por volumen medio se entiende aquí volumen esférico equivalente bajo clausura geométrica auxiliar: el volumen de una esfera perfecta cuyo volumen coincide con el volumen retornado que se decide representar mediante dicha clausura. No se trata de afirmar que el Universo Físico observable sea materialmente una esfera perfecta, ni que su frontera sea una superficie rígida, ni que el retorno metrológico externo agote la realidad del dominio.

Sea `V_Ω^SV` el volumen medio equivalente declarado para el dominio observable retornado. Se define el radio medio equivalente como:

`R̄_Ω^SV := (3V_Ω^SV / 4π)^(1/3)`.

De forma inversa:

`V_Ω^SV = (4π/3)(R̄_Ω^SV)^3`.

Esta definición no sustituye la recta generatriz `ℓ_Ω^SV`; la completa como clausura geométrica auxiliar de volumen. En el teorema, la coordenada radial terminal del punto interno del observable retornado se lee como:

`P_Ω^SV = (A_Ω^SV, R̄_Ω^SV, D_Ω^SV)`,

cuando la escala radial `R_Ω^SV` se especializa como radio medio equivalente de esfera perfecta. Por tanto:

`R_Ω^SV = R̄_Ω^SV`.

La ecuación local de cierre proyectivo conserva su forma:

`𝓖_Ω^SV(O;s) := π_Ω(O) − ℓ_{Ω,[0,1]}^SV(s) = 0_Ω`.

Con:

`P_Ω^SV = (A_Ω^SV, R̄_Ω^SV, D_Ω^SV)`.

La ciencia contemporánea no funda este resultado. Sólo entra como conjunto de datos de contraste cuando se declara un retorno metrológico externo. En ese retorno, si se adopta como diámetro esférico equivalente del universo observable:

`D̄_Ω^contraste := 93.000.000.000 ly`,

entonces el radio medio equivalente es:

`R̄_Ω^contraste = D̄_Ω^contraste / 2`.

Por tanto:

`R̄_Ω^contraste = 46.500.000.000 ly`.

Este valor no se presenta como radio cosmológico físico exacto independiente de toda convención, sino como valor exacto dentro de la convención declarada:

`D̄_Ω^contraste := 93.000.000.000 ly`.

El diámetro aproximado de `93.000.000.000 ly` se toma aquí como convención de retorno metrológico externo, apoyada en la estimación usual del diámetro del universo observable como aproximadamente `93.000 millones de años luz` (Encyclopaedia Britannica, 2026b).

Usando la conversión del año luz juliano:

`1 ly = 9.460.730.472.580,8 km`,

se obtiene:

`R̄_Ω^contraste = 46.500.000.000 × 9.460.730.472.580,8 km`.

El año luz se toma como distancia recorrida por la luz en vacío en un año juliano, con valor `9.460.730.472.580,8 km`, conforme a la descripción IAU (International Astronomical Union, s. f.).

Luego:

`R̄_Ω^contraste = 439.923.966.975.007.200.000.000 km`.

En metros:

`R̄_Ω^contraste = 439.923.966.975.007.200.000.000.000 m`.

Así, bajo la convención declarada de retorno metrológico externo, el radio medio equivalente del Universo Físico observable es:

`R̄_Ω = 46.500.000.000 ly`.

Equivalente a:

`R̄_Ω = 439.923.966.975.007.200.000.000 km`.

Equivalente a:

`R̄_Ω = 439.923.966.975.007.200.000.000.000 m`.

Este valor es exacto dentro de la convención declarada:

`D̄_Ω^contraste := 93.000.000.000 ly`.

Por tanto:

`R̄_Ω = D̄_Ω^contraste / 2 = 46.500.000.000 ly`.

La forma cerrada del volumen medio equivalente queda:

`V_Ω = (4π/3)(46.500.000.000 ly)^3`.

Como:

`46.500.000.000^3 = 100.544.625.000.000.000.000.000.000.000.000`,

entonces:

`V_Ω = 134.059.500.000.000.000.000.000.000.000.000π ly³`.

En notación científica:

`V_Ω ≈ 4,2116034034392086 × 10^32 ly³`.

En forma métrica compacta:

`V_Ω = (4π/3)(439.923.966.975.007.200.000.000 km)^3`.

Desarrollando el coeficiente exacto:

`V_Ω = 113.519.796.866.122.943.290.413.026.243.685.871.791.936.497.664.000.000.000.000.000.000.000.000π km³`.

En notación científica:

`V_Ω ≈ 3,5663295987161745 × 10^71 km³`.

En metros cúbicos:

`V_Ω = 113.519.796.866.122.943.290.413.026.243.685.871.791.936.497.664.000.000.000.000.000.000.000.000.000.000.000π m³`.

En notación científica:

`V_Ω ≈ 3,5663295987161745 × 10^80 m³`.

Este volumen se mantiene como clausura geométrica auxiliar de una esfera perfecta equivalente. El resultado no afirma que el Universo Físico observable sea materialmente una esfera perfecta, ni que su frontera sea una superficie física rígida, ni que el retorno externo agote la realidad del dominio. Afirma que, si el volumen retornado se equipara a una esfera perfecta, el radio medio equivalente queda determinado por la relación geométrica:

`R̄_Ω = (3V_Ω / 4π)^(1/3)`.

Con el retorno metrológico externo declarado, el valor final es:

`R̄_Ω = 46.500.000.000 ly = 439.923.966.975.007.200.000.000 km = 439.923.966.975.007.200.000.000.000 m`.

## X. Patrón lunar

El patrón lunar se incorpora como patrón auxiliar de distancia relativa, no como fuente del valor cosmológico ni como fundamento del SV. Su función es expresar el radio medio equivalente del Universo Físico observable en unidades de distancia media Tierra–Luna, de modo que el retorno metrológico externo pueda leerse mediante una escala astronómica próxima, intuitiva y controlada.

Se adopta como distancia media Tierra–Luna:

`LD := 384.400 km`,

donde `LD` designa una distancia lunar media, esto es, la distancia media entre la Tierra y la Luna usada como patrón auxiliar de medida. La distancia media Tierra–Luna de `384.400 km` se toma como valor externo de contraste para el patrón lunar (National Aeronautics and Space Administration, s. f.).

Dado el radio medio equivalente declarado:

`R̄_Ω = 439.923.966.975.007.200.000.000 km`,

la distancia equivalente en patrón lunar se obtiene por:

`N_LD(R̄_Ω) := R̄_Ω / LD`.

Sustituyendo:

`N_LD(R̄_Ω) = 439.923.966.975.007.200.000.000 / 384.400`.

Por tanto, en forma exacta fraccionaria irreducible:

`N_LD(R̄_Ω) = 35.477.739.272.178.000.000 / 31 LD`.

Esta es la forma exacta del resultado. La expansión decimal ordinaria es periódica y no se agota en una escritura decimal finita. Para lectura decimal redondeada a 12 decimales:

`N_LD(R̄_Ω) ≈ 1.144.443.202.328.322.580,645161290323 LD`.

El error absoluto máximo introducido por este redondeo es:

`ε_red < 0,0000000000005 LD`.

Como:

`LD = 384.400 km`,

se obtiene:

`ε_red < 0,0000000000005 × 384.400 km`.

Por tanto:

`ε_red < 0,0000001922 km`.

En metros:

`ε_red < 0,0001922 m`.

En milímetros:

`ε_red < 0,1922 mm`.

Así, el radio medio equivalente del Universo Físico observable expresado en distancias medias Tierra–Luna queda, de forma exacta, como:

`R̄_Ω = (35.477.739.272.178.000.000 / 31) LD`.

Y, como lectura decimal redondeada con error de plano nulo:

`R̄_Ω ≈ 1.144.443.202.328.322.580,645161290323 LD`.

El diámetro esférico equivalente del dominio observable, bajo la misma convención, se expresa como:

`D̄_Ω = 2R̄_Ω`.

Por tanto:

`D̄_Ω = 93.000.000.000 ly`.

En kilómetros:

`D̄_Ω = 879.847.933.950.014.400.000.000 km`.

En patrón lunar:

`N_LD(D̄_Ω) = D̄_Ω / LD`.

Sustituyendo:

`N_LD(D̄_Ω) = 879.847.933.950.014.400.000.000 / 384.400`.

Por tanto, en forma exacta fraccionaria irreducible:

`N_LD(D̄_Ω) = 70.955.478.544.356.000.000 / 31 LD`.

Para lectura decimal redondeada a 12 decimales:

`N_LD(D̄_Ω) ≈ 2.288.886.404.656.645.161,290322580645 LD`.

El error absoluto máximo de esta lectura decimal redondeada también queda acotado por:

`ε_red < 0,0000000000005 LD`.

Por tanto:

`ε_red < 0,1922 mm`.

El patrón lunar conserva el mismo régimen de cautela que el resto de retornos metrológicos externos. No funda la edad del observable retornado, no determina por sí mismo la recta generatriz, no transforma la distancia Tierra–Luna en unidad interna constitutiva del SV y no convierte la clausura esférica auxiliar en forma material real del Universo Físico observable. Sólo expresa el radio medio equivalente ya calculado en una escala externa de distancia media Tierra–Luna.

El patrón lunar no mide el Universo Físico observable desde la Luna ni convierte la distancia Tierra–Luna en unidad constitutiva SV; sólo reexpresa el radio medio equivalente ya obtenido en una escala externa de lectura metrológica.

La cadena de retorno queda, por tanto:

`D̄_Ω^contraste := 93.000.000.000 ly`.

`R̄_Ω := D̄_Ω^contraste / 2 = 46.500.000.000 ly`.

`R̄_Ω = 439.923.966.975.007.200.000.000 km`.

`LD := 384.400 km`.

`R̄_Ω / LD = 35.477.739.272.178.000.000 / 31`.

En lectura decimal redondeada a 12 decimales:

`R̄_Ω / LD ≈ 1.144.443.202.328.322.580,645161290323`.

Por tanto, bajo la convención declarada de retorno metrológico externo y usando como patrón auxiliar la distancia media Tierra–Luna, el radio medio equivalente del Universo Físico observable es, exactamente:

`R̄_Ω = (35.477.739.272.178.000.000 / 31) distancias medias Tierra–Luna`.

Y, en lectura decimal con error de plano nulo:

`R̄_Ω ≈ 1.144.443.202.328.322.580,645161290323 distancias medias Tierra–Luna`.

## XI. Distancia relativa media desde el centro de la Tierra hasta el límite de la esfera equivalente del Universo Físico observable

La distancia relativa se introduce para cerrar explícitamente el componente anunciado en el título de la investigación. No constituye una magnitud fundacional nueva del SV, ni sustituye el radio medio equivalente `R̄_Ω`, ni altera el patrón lunar ya definido. Su función es declarar, siguiendo el teorema de la recta generatriz y la ecuación local `𝓖_Ω^SV(O;s)=0_Ω`, la distancia media de retorno desde el centro de la Tierra hasta el límite de la esfera perfecta equivalente asignada al Universo Físico observable.

Sea `C_⊕` el centro de la Tierra tomado como punto metrológico de referencia para la lectura relativa externa. En esta clausura geométrica auxiliar, el límite de la esfera perfecta equivalente del Universo Físico observable se denota por:

`∂S_Ω`.

Los términos `C_⊕` y `∂S_Ω` pertenecen al retorno metrológico externo de la clausura esférica auxiliar. No pertenecen sin mediación al espacio afín interno `𝔼_Ω^SV`. Su comparecencia se admite mediante el modelo geométrico declarado `𝓜_sph`, el retorno metrológico `𝔛_{SI↔SV}` y el cierre residual correspondiente.

La distancia relativa media desde `C_⊕` hasta `∂S_Ω` se define como:

`d_rel(C_⊕,∂S_Ω) := R̄_Ω`.

Esto no afirma que el centro de la Tierra sea fundamento cosmológico, centro ontológico del Universo ni origen absoluto del dominio `Ω_F`. Afirma sólo que, en el retorno metrológico externo propio del universo observable, el centro terrestre funciona como punto de lectura relativo desde el cual se expresa la distancia hasta el límite de la esfera equivalente. En el marco del teorema, esta lectura corresponde al tránsito radial completo desde el parámetro inicial de referencia hasta el cierre terminal del dominio observable retornado.

Expresado mediante el tramo operativo de la recta generatriz:

`ℓ_{Ω,[0,1]}^SV(s)=O_∅+s Δ(O_∅→P_Ω^SV)`,

con:

`0 ≤ s ≤ 1`,

el límite de la esfera equivalente corresponde al cierre terminal:

`s = 1`.

Por tanto, la distancia relativa radial completa desde el centro terrestre tomado como referencia externa hasta el límite de la esfera equivalente queda determinada por la coordenada radial terminal:

`d_rel(C_⊕,∂S_Ω) = R̄_Ω`.

Como en el apartado anterior se ha fijado, bajo convención declarada de retorno metrológico externo:

`R̄_Ω = 46.500.000.000 ly`,

entonces:

`d_rel(C_⊕,∂S_Ω) = 46.500.000.000 ly`.

Usando la conversión del año luz juliano:

`1 ly = 9.460.730.472.580,8 km`,

se obtiene:

`d_rel(C_⊕,∂S_Ω) = 46.500.000.000 × 9.460.730.472.580,8 km`.

Por tanto:

`d_rel(C_⊕,∂S_Ω) = 439.923.966.975.007.200.000.000 km`.

En metros:

`d_rel(C_⊕,∂S_Ω) = 439.923.966.975.007.200.000.000.000 m`.

Esta distancia relativa media coincide formalmente con el radio medio equivalente porque la esfera perfecta auxiliar se ha construido precisamente como esfera de radio `R̄_Ω`. La equivalencia no introduce una segunda magnitud, sino una segunda lectura del mismo retorno: primero como radio esférico equivalente del dominio observable; después como distancia relativa desde el centro terrestre de referencia hasta el límite de la esfera equivalente.

En forma compacta:

`d_rel(C_⊕,∂S_Ω) = R̄_Ω`.

Y, bajo la convención declarada:

`d_rel(C_⊕,∂S_Ω) = 46.500.000.000 ly`.

`d_rel(C_⊕,∂S_Ω) = 439.923.966.975.007.200.000.000 km`.

`d_rel(C_⊕,∂S_Ω) = 439.923.966.975.007.200.000.000.000 m`.

Para expresar esta distancia relativa en equivalencia de distancia media Tierra–Luna, se conserva el patrón auxiliar ya declarado:

`LD := 384.400 km`.

La distancia media Tierra–Luna de `384.400 km` se toma como valor externo de contraste para el patrón lunar.

Se define entonces:

`N_LD(d_rel) := d_rel(C_⊕,∂S_Ω) / LD`.

Sustituyendo:

`N_LD(d_rel) = 439.923.966.975.007.200.000.000 / 384.400`.

Por tanto, en forma exacta fraccionaria irreducible:

`N_LD(d_rel) = 35.477.739.272.178.000.000 / 31`.

Así, la distancia relativa media desde el centro de la Tierra hasta el límite de la esfera perfecta equivalente del Universo Físico observable es, exactamente:

`d_rel(C_⊕,∂S_Ω) = (35.477.739.272.178.000.000 / 31) LD`.

Para lectura decimal, con el mismo criterio de redondeo ya adoptado:

`d_rel(C_⊕,∂S_Ω) ≈ 1.144.443.202.328.322.580,645161290323 LD`.

El error absoluto máximo de esta lectura decimal redondeada queda acotado por:

`ε_red < 0,0000000000005 LD`.

Como:

`LD = 384.400 km`,

entonces:

`ε_red < 0,0000001922 km`.

En metros:

`ε_red < 0,0001922 m`.

En milímetros:

`ε_red < 0,1922 mm`.

Por tanto, la lectura decimal en distancias medias Tierra–Luna conserva error de plano nulo para esta clausura geométrica auxiliar.

La cadena final de la distancia relativa queda:

`d_rel(C_⊕,∂S_Ω) := R̄_Ω`.

`d_rel(C_⊕,∂S_Ω) = 46.500.000.000 ly`.

`d_rel(C_⊕,∂S_Ω) = 439.923.966.975.007.200.000.000 km`.

`d_rel(C_⊕,∂S_Ω) = 439.923.966.975.007.200.000.000.000 m`.

`d_rel(C_⊕,∂S_Ω) = (35.477.739.272.178.000.000 / 31) distancias medias Tierra–Luna`.

En lectura decimal con error de plano nulo:

`d_rel(C_⊕,∂S_Ω) ≈ 1.144.443.202.328.322.580,645161290323 distancias medias Tierra–Luna`.

La distancia relativa queda así incorporada sin alterar la estructura del teorema: el cierre proyectivo `𝓖_Ω^SV(O;s)=0_Ω` fija la pertenencia al tramo operativo de la recta generatriz, denominado internamente `Recta-Ómicron SV16` (`Recta_Οmi_SV16`); la clausura esférica auxiliar fija `R̄_Ω`; y la distancia relativa desde el centro terrestre hasta el límite de la esfera equivalente no es una nueva fuente de verdad, sino la lectura radial externa de ese mismo `R̄_Ω` bajo retorno metrológico declarado.

En escala larga española, equivale aproximadamente a `1,14` trillones de distancias medias Tierra–Luna; dicho de forma llana, algo más de un trillón de veces la distancia media entre la Tierra y la Luna.

## XII. Conclusión

La determinación realizada fija un resultado matemático y metrológico bajo una restricción principal: `Ω_F ≠ 𝓣`. El Universo Físico observable se trata como dominio retornado y no como totalidad absoluta; el horizonte observable no se convierte en borde ontológico; el origen formal `0_SV` no se espacializa; y el centro de la Tierra `C_⊕` no se declara centro cosmológico, sino punto metrológico externo para la lectura relativa de una clausura esférica auxiliar. Con ello, el documento mantiene separadas tres capas que no deben confundirse: la formulación interna SV, la geometría auxiliar de retorno y los datos externos de contraste.

El estado del arte ha mostrado que esta forma de proceder no es una licencia especulativa, sino una estructura profunda de la ciencia. Eratóstenes calculó y acotó la circunferencia terrestre sin recorrerla, mediante diferencia angular, distancia entre puntos y clausura geométrica. Hiparco y Al-Biruni ofrecieron otras formas de inferir distancias o radios mediante paralaje, horizonte y trigonometría. Newton, desde otro plano, tampoco necesitó salir de su mesa, su papel y su pluma para visualizar una proyección de Ley de Gravitación Universal: necesitó una formalización capaz de convertir observación, geometría y dinámica en ley general. En reconocimiento a Eratóstenes, esta investigación conserva explícitamente ese principio: la ciencia puede calcular y acotar dominios sin necesidad de recorrerlos materialmente, siempre que declare el modelo, las unidades, el procedimiento y el residual.

La aportación propia del texto consiste en trasladar esa tradición al régimen SV de distancia absoluta y relativa entre observables. La recta generatriz del Universo Físico observable, denominada internamente `Recta-Ómicron SV16` (`Recta_Οmi_SV16`), no funciona como imagen decorativa ni como derivación química, sino como denominación estable de la recta asociada al cierre uniparamétrico del dominio `Ω_F`. Su estructura se apoya en el espacio afín tipado `𝔼_Ω^SV`, el espacio residual `𝓡_Ω^SV`, el origen formal `O_∅`, el punto terminal interno `P_Ω^SV`, el vector director `v_Ω := Δ(O_∅→P_Ω^SV)`, la recta completa `ℓ_Ω^SV` y el tramo operativo `ℓ_{Ω,[0,1]}^SV`. La pertenencia obtenida es proyectiva: `π_Ω(O) ∈ ℓ_{Ω,[0,1]}^SV`; no se afirma que el objeto físico bruto pertenezca materialmente a la recta.

La ecuación local `𝓖_Ω^SV(O;s)=0_Ω` queda situada correctamente: no es ecuación rectora del Sistema Vectorial SV ni sustituye la ecuación superior `𝓔★_TODO,SV(Γ_U;τ)=0`; sólo declara residual proyectivo nulo dentro del dominio observable retornado. Bajo la condición de no nulidad terminal, una sola coordenada no nula permite determinar el parámetro `s_O` y, con él, las otras dos coordenadas internas de retorno. La forma normalizada `π̂_Ω(O)=(s_O,s_O,s_O)` expresa coincidencia de razones adimensionales, no identidad material entre edad, radio y profundidad.

La clausura geométrica auxiliar ofrece el resultado cosmométrico buscado: bajo el diámetro externo de contraste `D̄_Ω^contraste := 93.000.000.000 ly`, el radio medio equivalente queda fijado como `R̄_Ω = 46.500.000.000 ly`, equivalente a `439.923.966.975.007.200.000.000 km` y a `439.923.966.975.007.200.000.000.000 m`. El volumen medio equivalente se expresa por `V_Ω = (4π/3)(R̄_Ω)^3`, con resultado en `ly³`, `km³` y `m³`. Ninguno de estos valores afirma que el Universo Físico observable sea materialmente una esfera perfecta; todos ellos pertenecen a la clausura geométrica auxiliar declarada.

El patrón lunar aporta una escala externa de lectura metrológica. La forma exacta `R̄_Ω = (35.477.739.272.178.000.000 / 31) LD` conserva la precisión del cálculo, mientras que la lectura decimal `1.144.443.202.328.322.580,645161290323 LD` ofrece una expresión manejable con cota de redondeo inferior a `0,1922 mm`. En escala larga española, el resultado equivale aproximadamente a `1,14` trillones de distancias medias Tierra–Luna; dicho de forma llana, algo más de un trillón de veces la distancia media entre la Tierra y la Luna.

La distancia relativa media desde `C_⊕` hasta `∂S_Ω` queda finalmente incorporada sin alterar el teorema: `d_rel(C_⊕,∂S_Ω) := R̄_Ω`. La igualdad no introduce una nueva magnitud fundacional, sino una lectura radial externa del mismo radio medio equivalente bajo modelo esférico auxiliar, patrón lunar opcional y retorno metrológico declarado. El resultado final es, por tanto, una determinación cerrada, tipada y trazable: radio, volumen, patrón lunar y distancia relativa quedan coordinados sin medir la totalidad absoluta, sin geocentrismo, sin espacialización del origen formal y sin convertir la cosmología contemporánea en fuente soberana de verdad para el SV.

## XIII. Bibliografía

### XIII.I. Referencias internas del Corpus SV citadas

Lloret Egea, J. A. (2026a). *Distancia absoluta y relativa entre observables del Universo*. IA eñ™ — La Biblia de la IA™. https://doi.org/10.21428/39829d0b.c394e160

Lloret Egea, J. A. (2026b). *Teoría del TODO y de la NADA en el Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. https://doi.org/10.17613/k3q1d-fjj45

Lloret Egea, J. A. (2026c). *Primitivos metrológicos del Sistema Vectorial SV: instanciaciones contingentes de las constantes fundacionales del Sistema Internacional, justificación algebraica y tabla de equivalencias factuales*. IA eñ™ — La Biblia de la IA™. https://doi.org/10.21428/39829d0b.c8ec692e

Lloret Egea, J. A. (2026d). *Directed determination of the chemical element SV-399 — Actinium (Ac) + 3 Oganesson (Og) + Tungsten/Wolfram (W): Spain and Portugal as priority prospecting targets — (SV16-Ómicron)*. IA eñ™ — La Biblia de la IA™. https://doi.org/10.21428/39829d0b.11d9224e

Lloret Egea, J. A. (2026e). *Determinación dirigida del elemento químico SV-399 — Actinio (Ac) + 3 Oganesón (Og) + Tungsteno/Wolframio (W)*. IA eñ™ — La Biblia de la IA™. https://doi.org/10.21428/39829d0b.5211d837

Lloret Egea, J. A. (2026f). *Edades relativas del universo observable y de sus objetos físicos*. IA eñ™ — La Biblia de la IA™. https://doi.org/10.21428/39829d0b.b56ed853

Lloret Egea, J. A. (2026g). *Línea del Umbral SV, circulación de retorno del dominio-universo y átomo formal de ascendencia no agotada*. IA eñ™ — La Biblia de la IA™. https://doi.org/10.21428/39829d0b.30dfd78b

### XIII.II. Referencias externas de contraste

American Physical Society. (2006, junio). *Eratosthenes measures Earth*. APS News. https://www.aps.org/apsnews/2006/06/eratosthenes-measures-earth

Cambridge University Library. (s. f.). *Newton Papers: Philosophiæ naturalis principia mathematica*. Cambridge Digital Library. https://cudl.lib.cam.ac.uk/view/MS-ROYALSOCIETY-00069/1

Dark Energy Spectroscopic Instrument. (2025, 19 de marzo). *DESI DR2 results: March 19 guide*. DESI. https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/

Encyclopaedia Britannica. (2026a). *Eratosthenes: Biography, discoveries, sieve, & facts*. Encyclopaedia Britannica. https://www.britannica.com/biography/Eratosthenes

Encyclopaedia Britannica. (2026b). *Observable universe: Definition, size, description, & facts*. Encyclopaedia Britannica. https://www.britannica.com/topic/observable-universe

Encyclopaedia Britannica. (2026c). *Hipparchus: Biography, discoveries, accomplishments, & facts*. Encyclopaedia Britannica. https://www.britannica.com/biography/Hipparchus-Greek-astronomer

European Space Agency. (s. f.-a). *Euclid*. ESA. https://www.esa.int/Science_Exploration/Space_Science/Euclid

European Space Agency. (s. f.-b). *Euclid overview*. ESA. https://www.esa.int/Science_Exploration/Space_Science/Euclid_overview

International Astronomical Union. (s. f.). *Measuring the Universe*. IAU. https://iauarchive.eso.org/public/themes/measuring/

National Aeronautics and Space Administration. (s. f.). *How far away is the Moon?* NASA Space Place. https://spaceplace.nasa.gov/moon-distance/

Planck Collaboration, Aghanim, N., Akrami, Y., Ashdown, M., Aumont, J., Baccigalupi, C., Ballardini, M., Banday, A. J., Barreiro, R. B., Bartolo, N., Basak, S., Battye, R., Benabed, K., Bernard, J.-P., Bersanelli, M., Bielewicz, P., Bock, J. J., Bond, J. R., Borrill, J., ... Zonca, A. (2020). *Planck 2018 results. VI. Cosmological parameters*. Astronomy & Astrophysics, 641, A6. https://www.aanda.org/articles/aa/full_html/2020/09/aa33910-18/aa33910-18.html

Royal Society. (2014, 16 de julio). *Principia*. The Royal Society. https://royalsociety.org/blog/2014/07/principia/

Sparavigna, A. C. (2014). *Al-Biruni and the mathematical geography*. HAL Open Science. https://hal.science/hal-02264631/document
