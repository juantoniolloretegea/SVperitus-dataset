# Fronteras de resolución en células ternarias estratificadas: profilaxis de infecciones, vacunación e integridad de sistemas de IA

**Autor:** Juan Antonio Lloret Egea  
**Titulación y función:** Ingeniero en Electrónica y Automática; Director del Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA), Madrid, España  
**ORCID:** 0000-0002-6634-3351  
**Correo electrónico:** juanantoniolloret@itvia.es  
**Fecha:** 20 de agosto de 2026  
**Estado editorial:** versión original del autor; prepublicación no revisada por pares  
**DOI:** [10.21428/39829d0b.739ed2b6](https://doi.org/10.21428/39829d0b.739ed2b6)

> Esta versión no constituye una guía de práctica clínica, un sistema clínico validado ni una recomendación diagnóstica o terapéutica. Las expresiones «frontera de resolución» y «resolución» se refieren en este trabajo a resolución representacional, no a la resolución de un valor ternario U.

**Palabras clave:** informática biomédica; representación del conocimiento; métodos formales; vacunación; inteligencia artificial

## Resumen

**Objetivo.** Definir, dentro de una cadena finita de representación de un estado ternario estratificado, el nivel más alto desde el que una operación especificada sigue siendo recuperable de forma exacta, y verificar fronteras distintas en dos dominios definidos.

**Materiales y métodos.** Se formalizaron cuatro niveles: estado etiquetado, conteos ternarios por capas, conteos ternarios globales y clase terminal tipada. La recuperabilidad exacta exige una aplicación explícita de recuperación. Una frontera no terminal se verifica mediante estados realizables conforme a las reglas que coinciden en el nivel siguiente, pero difieren respecto de la operación. La construcción se aplicó a una célula inmunológica de 25 parámetros y a una célula independiente de integridad de sistemas de IA con 9 parámetros.

**Resultados.** Las operaciones seleccionadas en inmunología sobre etiquetas de vacunación, localización por capas, número de U y clase terminal presentaron fronteras 0, 1, 2 y 3. Las operaciones seleccionadas de forma independiente en integridad realizaron los mismos cuatro niveles con semántica distinta y sin utilizar U en el testigo de nivel 2. Cada frontera no terminal dispuso de una aplicación de recuperación y de un par separador realizable conforme a las reglas.

**Discusión.** Operaciones distintas sobre un mismo estado pueden exigir niveles de representación diferentes. Las fronteras son relativas al espacio de estados realizados y a la cadena declarada; no son óptimos universales. La insuficiencia representacional no modifica el estado ternario.

**Conclusión.** Las fronteras de resolución específicas de la operación permiten verificar si una agregación conserva las distinciones requeridas por una operación posterior determinada.

## Antecedentes y relevancia

La informática biomédica depende cada vez más de representaciones que comprimen, agregan o reorganizan información estructurada sin perder aquello que las operaciones posteriores necesitan. La dificultad central no consiste en determinar si una representación más rica contiene más información, sino en establecer si una distinción concreta sigue siendo recuperable después de la agregación. En consonancia con ello, trabajos recientes sobre informática biomédica han subrayado la necesidad de investigación teórica en representación del conocimiento, razonamiento y arquitectura como complemento de la construcción empírica de sistemas.[1] Los formalismos de guías clínicas ya distinguen niveles conceptuales, computables e implementables de representación,[2] pero la mera existencia de varios niveles no identifica por sí sola el punto en el que una operación determinada deja de ser exactamente recuperable.

Diversas teorías consolidadas abordan preguntas relacionadas. En interpretación abstracta, los cocientes dirigidos por propiedades identifican la parte de un dominio abstracto útil para calcular una propiedad determinada.[3] El aprendizaje basado en conjuntos formaliza representaciones invariantes frente a permutaciones,[4] mientras que arquitecturas clínicas recientes basadas en conjuntos restauran expresamente información sobre el tipo de variable que un tratamiento indiferenciado del conjunto puede perder.[5] Trabajos más recientes han estudiado abstracciones exactas relevantes para una decisión y representaciones suficientes dependientes de la función de pérdida.[6,7] En conjunto, estas líneas muestran que la relevancia depende de la propiedad, la operación, la decisión, la distribución o la pérdida que se pretenda conservar. El presente trabajo estudia un objeto más acotado: una cadena finita de representación fijada de antemano por la semántica del dominio y el nivel de esa cadena a partir del cual una operación concreta deja de ser exactamente recuperable. No busca entre todas las abstracciones posibles ni trata la cadena declarada como un cociente canónico.

Esta distinción es importante en sistemas de información clínica porque la agregación puede borrar etiquetas sin volver incoherente el estado agregado. Dos estados de vacunación pueden tener conteos idénticos y, sin embargo, situar los valores no nulos en vacunas diferentes; dos estados de integridad pueden tener los mismos conteos globales y localizar el control comprometido en capas funcionales diferentes. Que esa pérdida sea aceptable depende de la operación posterior. Una clase terminal puede ser plenamente suficiente para una interfaz que solo transporte dicha clase y, al mismo tiempo, insuficiente para una operación local que todavía requiera la identidad de una coordenada o un conteo que la clase terminal ya no expone.

El estudio se apoya en construcciones previas del Sistema Vectorial SV que especificaron una célula inmunológica de 25 parámetros para profilaxis de infecciones y vacunación,[8] una célula independiente de integridad de sistemas de IA con 9 parámetros,[9] la semántica algebraica de las células ternarias etiquetadas,[10] la transducción tipada al alfabeto ternario[11] y un operador de consulta limitado por dominio cuyo alcance declarado identifica la parte de la arquitectura de la que depende una respuesta.[12] Otra prepublicación del SV formalizó la no clausura certificada y la revisión en sistemas de resolución finita.[13] Ese trabajo aborda la certificación de la no clausura y la revisión en estructuras de resolución finita; el presente estudio pregunta, en cambio, hasta dónde puede avanzar la agregación dentro de una cadena fija de representación de una célula ternaria constituida antes de que una operación determinada deje de ser exactamente recuperable. Los trabajos anteriores aportan células y semánticas preexistentes; ninguno define la frontera de representación específica de la operación estudiada aquí.

Este entorno resulta especialmente útil en informática biomédica porque las etiquetas incluidas en una capa clínica no tienen por qué ser intercambiables. La vacunación frente a la gripe y la vacunación antineumocócica, por ejemplo, son objetos clínicos diferenciados en las recomendaciones actuales de vacunación oncológica.[14] Por ello, un conteo por capas puede ser suficiente para una operación e insuficiente para otra. El presente artículo no reivindica una nueva lógica ternaria, un nuevo teorema de dependencia funcional ni una abstracción universalmente óptima. Formula una pregunta acotada: dentro de una cadena de representación declarada, ¿cuál es el mayor índice desde el que cada operación especificada todavía puede recuperarse exactamente?

## Objetivo

El objetivo fue definir una frontera de resolución verificable y específica de la operación para una cadena declarada de cuatro niveles, y determinar dicha frontera para operaciones seleccionadas en dos dominios constituidos de forma independiente: profilaxis de infecciones y vacunación en adultos inmunodeprimidos, y controles de integridad de un sistema de IA. Como objetivo secundario, se preservó la compatibilidad con arquitecturas en las que las células se conectan mediante interfaces especificadas explícitamente, sin convertir en obligatoria ninguna composición celular.

## Materiales y métodos

### Marco formal

Sea Σ = {0, 1, U}. Sea D_c un dominio previamente especificado, I un conjunto finito de parámetros etiquetados y C: D_c → Σ^I una aplicación celular determinista. El espacio de estados realizados es X = C(D_c) ⊆ Σ^I. En este trabajo, «constituido» significa que la semántica de los parámetros y las regiones de regla utilizadas para producir valores ternarios quedaron fijadas antes del presente análisis de fronteras. Los resultados se demuestran sobre X y no sobre el espacio ambiente Σ^I; en consecuencia, cada par separador utilizado debe ser realizable conforme a las reglas declaradas del dominio. Los símbolos 0, 1 y U son valores ternarios atómicos. El testigo U utilizado en los resultados principales procede de una condición observada incluida en una región de regla publicada de IMMUNO-1; ningún testigo principal utiliza como U una entrada ausente o pendiente.

Para las estratificaciones cuadradas utilizadas en las dos realizaciones, n = b² e I se divide en capas etiquetadas I₁,…,I_b, cada una con b parámetros. Esta partición en capas constituye estructura declarada del dominio; no se deduce de n = b². No se presupone simetría por permutación ni intercambiabilidad dentro de una capa. Para un estado v ∈ X y una capa Iⱼ, n₀,ⱼ(v), n₁,ⱼ(v) y nU,ⱼ(v) designan los números de valores 0, 1 y U de esa capa. Los conteos globales n₀(v), n₁(v) y nU(v) se definen de forma análoga. Para cualquier entero positivo r, Aᵣ es el conjunto de ternas de enteros no negativos (a₀, a₁, aU) cuyas componentes suman r.

Se utilizan cuatro niveles de representación y sus índices se ordenan, únicamente dentro de esta cadena, como 0 < 1 < 2 < 3. F₀: X → X es la identidad. F₁ devuelve la lista ordenada de ternas de conteos ternarios de las capas declaradas. F₂: X → A_n devuelve la terna global de conteos ternarios. Para cada realización, K_D designa su codominio terminal declarado y c_D: X → K_D su clasificador por umbral; se fija F₃ = c_D. Las etiquetas terminales publicadas de IMMUNO-1 son `APTO`, `NO_APTO` e `INDETERMINADO`, mientras que la realización de integridad utiliza `NORMAL`, `INTRUSION` e `INDETERMINATE`. Estas etiquetas terminales no son elementos de Σ. F₂ se obtiene de F₁ mediante suma componente a componente y F₃ es una función determinista de F₂. Por tanto, existen aplicaciones deterministas de agregación rⱼ tales que Fⱼ₊₁ = rⱼ ∘ Fⱼ para j = 0, 1, 2. F₁ conserva el orden de las capas, pero no la identidad de las coordenadas dentro de cada capa.

### Recuperabilidad funcional exacta y frontera

Para una operación Q: X → Y, la recuperabilidad funcional exacta desde el nivel j significa que existe una aplicación explícita qⱼ: Fⱼ(X) → Y tal que Q = qⱼ ∘ Fⱼ. A lo largo de este trabajo, «resolución» en «frontera de resolución» significa resolución representacional, no la operación del SV que resuelve un valor ternario U. La recuperabilidad es una propiedad matemática de factorización y no afirma que exista un entorno de ejecución de software que implemente Q.

Para la cadena declarada ℱ = (F₀, F₁, F₂, F₃), la frontera se define por la condición Q = qⱼ ∘ Fⱼ y por:

ℓ(X, ℱ; Q) = max { j ∈ {0, 1, 2, 3} : Q = qⱼ ∘ Fⱼ para alguna qⱼ }.

### Monotonía de la cadena y verificación de la frontera

Como Fⱼ₊₁ = rⱼ ∘ Fⱼ, la recuperabilidad desde el nivel j + 1 implica recuperabilidad desde el nivel j. Dado que F₀ es la identidad sobre X, el conjunto de niveles recuperables es un segmento inicial no vacío {0,…,ℓ}; por ello, el máximo de la definición existe y es único dentro de la cadena declarada.

Para j < 3, la verificación de una frontera consta de qⱼ y de dos estados x, y ∈ X tales que Fⱼ₊₁(x) = Fⱼ₊₁(y), pero Q(x) ≠ Q(y). Si Q factorizara a través de Fⱼ₊₁, la igualdad de Fⱼ₊₁ en x e y obligaría a la igualdad de Q, lo que contradice el testigo. La aplicación de recuperación y el par separador establecen, por tanto, la frontera. Para j = 3 basta la aplicación de recuperación, porque no existe un nivel posterior. Se trata de un procedimiento elemental de verificación, no de una reivindicación de novedad sobre dependencia funcional.

Para una familia finita de operaciones 𝒬 = {Q₁,…,Qᵣ}, se registra el perfil abreviado Λ_X(𝒬) = (ℓ_X(Q₁),…,ℓ_X(Qᵣ)), donde ℓ_X(Q) abrevia ℓ(X,ℱ;Q) cuando la cadena ℱ está fijada. El perfil es solo un resumen de las operaciones elegidas, el espacio de estados realizados y la cadena declarada; no es un estado clínico ni de integridad y no se afirma que sea invariante frente a cambios en el dominio o en la cadena de representación.

### Realización IMMUNO-1

La primera realización utiliza la célula inmunológica SV(25,5), publicada el 5 de marzo de 2026.[8] Su dominio es la profilaxis de infecciones y la vacunación en adultos con neoplasias hematológicas e inmunosupresión. Los 25 parámetros etiquetados se organizan en cinco capas publicadas: estado inmunitario basal (P01-P05), neoplasia y tratamiento (P06-P10), historia infecciosa (P11-P15), estado vacunal (P16-P20) y profilaxis/seguimiento (P21-P25). El umbral terminal es T = 19. La construcción de origen se diseñó como demostrador teórico-técnico y no ha sido validada en una cohorte de pacientes. Las guías actuales de oncología y enfermedades infecciosas abordan por separado la vacunación y la profilaxis antimicrobiana en esta población.[14,15]

Todos los estados IMMUNO-1 utilizados aquí se establecen mediante sustitución directa en regiones de regla publicadas; la ejecución de software no se utiliza como evidencia de las fronteras. La Tabla suplementaria S1 ofrece una asignación basal conjuntamente compatible y las sustituciones empleadas por los cinco testigos no basales; la Nota suplementaria S1 audita las condiciones cruzadas entre coordenadas relevantes para la realizabilidad conjunta; y la Tabla suplementaria S2 enumera los estados completos de 25 coordenadas. La única U utilizada en los resultados principales es P02 = U para un recuento observado de CD4 de 350 células/µL, valor perteneciente a la región publicada 200-499. Se trata de un valor ternario constituido por regla conforme a la especificación publicada de IMMUNO-1; el presente estudio no vuelve a demostrar condiciones operativas posteriores de certificación de no clausura.

### Realización de integridad de sistemas de IA

La segunda realización utiliza una célula de integridad SV(9,3) publicada de forma independiente.[9] Sus tres capas declaradas son: integridad del modelo (M1-M3: integridad de pesos, procedencia del conjunto de datos y control de acceso), seguridad operativa (M4-M6: pruebas adversariales, telemetría y aislamiento de entornos) y supervisión/cadena de suministro de software (M7-M9: registro inmutable, supervisión humana e integridad de la cadena de suministro). El umbral terminal es T = 7. Conforme a la especificación publicada de integridad, un valor booleano presente `True` se transforma en 0 —verificado y conforme— y `False` en 1 —comprometido—. Todos los estados testigo incluyen explícitamente las nueve entradas booleanas; no se necesita ninguna entrada U. La Tabla suplementaria S3 contiene el diccionario completo y los estados testigo.

### Localidad celular e interfaces

La construcción de frontera es local a una célula y a una cadena de representación especificada. Un conector entre células es una aplicación tipada separada con entrada y salida declaradas.[16] Si una interfaz transforma además una representación fuente Fⱼ mediante una aplicación φ, el componente receptor recibe H = φ ∘ Fⱼ; cualquier afirmación de recuperación exacta aguas abajo debe factorizar, por tanto, a través de H, salvo que se declare explícitamente información adicional. Los resultados presentes no imponen una topología celular universal. Se aplican a una célula local y a su cadena de representación declarada, y cualquier consecuencia sobre interfaces es relativa a la información efectivamente transmitida.

### Tabla 1. Niveles declarados de representación en la cadena de cuatro niveles

| Nivel | Aplicación y salida | Distinciones conservadas | Información eliminada respecto del nivel anterior |
|---|---|---|---|
| 0 | F₀(v) = v; estado etiquetado en X | Todas las etiquetas de coordenadas y todos los valores ternarios | Ninguna |
| 1 | F₁(v) = lista ordenada de ternas por capa (n₀,ⱼ, n₁,ⱼ, nU,ⱼ) | Identidad de la capa y conteos ternarios dentro de cada capa declarada | Identidad de las coordenadas dentro de una capa |
| 2 | F₂(v) = (n₀, n₁, nU) | Conteos ternarios globales | Localización por capas |
| 3 | F₃(v) = clase terminal por umbral | Solo la clase terminal declarada | Conteos globales exactos |

El orden de índices 0 < 1 < 2 < 3 es local a esta cadena declarada; no constituye una ordenación universal de todas las representaciones posibles.

## Resultados

### Fronteras en inmunología

Se evaluaron cuatro operaciones sobre el espacio de estados realizados de IMMUNO-1.

Primero, Q_vac(v) = (v(P16),…,v(P20)) devuelve el estado etiquetado de los cinco parámetros de vacunación. Se recupera desde F₀ por proyección de coordenadas. En el par de frontera, x_vac tiene P16 = 1, P17 = P18 = P19 = 0 y P20 = 1; y_vac tiene P16 = 0, P17 = 1, P18 = P19 = 0 y el mismo P20 = 1. En ambos estados, P20 = 1 se genera por la misma condición de regla independiente: administración de una vacuna viva bajo una contraindicación activa. Todas las demás coordenadas satisfacen las regiones comunes de 0. Por ello, ambas capas de vacunación presentan conteos (3,2,0), y las demás capas son idénticas, de modo que F₁(x_vac) = F₁(y_vac), mientras que Q_vac difiere. En consecuencia, ℓ_X(Q_vac) = 0.

Segundo, Q_loc(v) devuelve el conjunto de capas declaradas que contienen al menos un 1 o una U. Desde F₁ se recupera seleccionando los índices de capa cuya segunda o tercera componente de conteo es distinta de cero. Un estado realizable conforme a las reglas presenta P02 = 1 por un recuento observado de CD4 inferior a 200 células/µL, mientras P21 permanece en 0 mediante profilaxis activa y correcta frente a PJP y todas las demás coordenadas permanecen en regiones de 0. El estado emparejado presenta P25 = 1 porque no existe un plan explícito de reevaluación, con todas las demás coordenadas en regiones de 0. Ambos estados tienen F₂ = (24,1,0), pero Q_loc devuelve {1} y {5}, respectivamente. Por tanto, ℓ_X(Q_loc) = 1. Q_loc es una operación estructural de localización y no se presenta como una actuación clínica derivada de una guía.

Tercero, Q_U(v) = nU(v) se recupera desde la tercera componente de F₂. El estado de referencia tiene F₂ = (25,0,0), F₃ = `APTO` y Q_U = 0. Un segundo estado realizable conforme a las reglas difiere en el nivel ternario únicamente en P02, donde un recuento observado de CD4 de 350 células/µL produce U conforme a la regla publicada; sus conteos globales son (24,0,1). Como 24 ≥ 19, su clase terminal también es `APTO`, pero Q_U = 1. Por tanto, ℓ_X(Q_U) = 2. Este testigo no identifica U con ausencia de datos: la observación de CD4 está presente y el valor no binario procede de la región de regla declarada. Finalmente, Q_class = F₃ tiene frontera 3 por identidad sobre la representación terminal. La familia de operaciones seleccionada realiza constructivamente Λ_IMM = (0,1,2,3), únicamente respecto de este espacio de estados y de esta cadena.

### Tabla 2. Fronteras específicas de la operación en la realización IMMUNO-1

| Operación | Reconstrucción exacta | Par separador en el nivel siguiente | Frontera |
|---|---|---|---:|
| Q_vac = (P16,…,P20) | Proyección desde F₀ | Mismo F₁; conteos de la capa de vacunación (3,2,0), pero vectores etiquetados (1,0,0,0,1) y (0,1,0,0,1) | 0 |
| Q_loc = capas que contienen 1 o U | Desde F₁, seleccionar las capas con a₁,ⱼ + aU,ⱼ > 0 | Mismo F₂ = (24,1,0); Q_loc = {1} frente a {5} | 1 |
| Q_U = nU | Tercera componente de F₂ | Mismo F₃ = `APTO`; nU = 0 frente a 1 | 2 |
| Q_class = F₃ | Identidad sobre F₃(X) | No existe un nivel declarado posterior | 3 |

Cada estado separador está respaldado por el certificado estático de sustitución de reglas de la Tabla suplementaria S1 y la Nota suplementaria S1. Los estados completos de 25 coordenadas se ofrecen en la Tabla suplementaria S2.

### Fronteras en integridad de sistemas de IA

La célula de integridad realiza de forma independiente los cuatro niveles mediante operaciones diferentes y un umbral distinto.

Sea Q_model(m) = (m(M1), m(M2), m(M3)). Un estado completamente observado tiene comprometido únicamente M1 y otro únicamente M2. Los conteos de su primera capa son (2,1,0) en ambos casos, las demás capas son idénticas y Q_model distingue los estados; por tanto, su frontera es 0.

Sea Q_layer(m) el conjunto de capas de integridad que contienen al menos un control comprometido. Un estado con solo M1 = 1 y un estado con solo M4 = 1 tienen ambos F₂ = (8,1,0), pero Q_layer devuelve {1} y {2}; su frontera es 1. Sea Q_comp(m) = n₁(m). Un estado completamente observado con M1-M3 comprometidos presenta F₂ = (6,3,0), mientras que un segundo estado con M1-M4 comprometidos presenta F₂ = (5,4,0). Ningún conteo alcanza el umbral 7, de modo que ambos poseen clase terminal `INDETERMINATE`, pero Q_comp vale 3 y 4. Por tanto, su frontera es 2 sin utilizar ninguna entrada U. La clase terminal de integridad tiene frontera 3. Las operaciones seleccionadas de integridad realizan constructivamente Λ_AI = (0,1,2,3).

La igualdad de ambos perfiles no se interpreta como un invariante entre dominios. Las familias de operaciones se seleccionaron deliberadamente para ejercitar niveles distintos de la cadena declarada. Las realizaciones de inmunología e integridad difieren en semántica de parámetros, número de capas, dimensión, umbral y operación de nivel 2. Lo único compartido es el procedimiento de verificación: una aplicación positiva de recuperación en un nivel y un par separador realizable conforme a las reglas en el siguiente.

### Tabla 3. Fronteras específicas de la operación en la realización de integridad de sistemas de IA

| Operación | Reconstrucción exacta | Par separador en el nivel siguiente | Frontera |
|---|---|---|---:|
| Q_model = (M1,M2,M3) | Proyección desde F₀ | Mismo F₁; un compromiso en la capa 1, pero M1 frente a M2 | 0 |
| Q_layer = capas que contienen un control comprometido | Desde F₁, seleccionar las capas con a₁,ⱼ > 0 | Mismo F₂ = (8,1,0); Q_layer = {1} frente a {2} | 1 |
| Q_comp = n₁ | Segunda componente de F₂ | Misma clase terminal `INDETERMINATE`; n₁ = 3 frente a 4 | 2 |
| Q_meta = F₃ | Identidad sobre F₃(X) | No existe un nivel declarado posterior | 3 |

Todos los testigos de integridad utilizan explícitamente las nueve entradas booleanas; no se utiliza ninguna U en el par de frontera de nivel 2.

## Discusión

Este estudio aísla un problema de representación que puede quedar oculto cuando la agregación se trata como una simplificación genérica. Un mismo estado constituido puede admitir varias operaciones legítimas, y dichas operaciones no tienen por qué tolerar la misma pérdida de etiquetas, localización por capas o información de conteo global. Las familias de operaciones seleccionadas realizan constructivamente los cuatro niveles de una misma cadena declarada: algunas operaciones exigen el estado etiquetado completo; otras sobreviven a la agregación por capas o al conteo global; y únicamente una operación sobre la clase terminal sobrevive al colapso final.

El resultado no debe interpretarse como una nueva teoría de estadísticos suficientes ni como una búsqueda de la representación universalmente más gruesa. Los cocientes dirigidos por propiedades de la interpretación abstracta,[3] los cocientes exactos de decisión[6] y las representaciones suficientes en sentido bayesiano[7] formulan preguntas relacionadas, pero diferentes, acerca de la información relevante para una propiedad, una decisión, una distribución o una pérdida. Aquí la cadena de representación queda fijada antes de probar la operación. Como en Materiales y métodos, «resolución» significa aquí resolución representacional, no resolución de un valor ternario U. La frontera es el mayor índice de esa cadena especificada para el que todavía puede exhibirse recuperación funcional exacta. Una cadena distinta, o un cambio en el espacio de estados realizados, puede producir una frontera diferente. Esta restricción es deliberada: las representaciones biomédicas suelen diseñarse por razones semánticas, de flujo de trabajo, interoperabilidad o gobernanza que no tienen por qué coincidir con un cociente matemáticamente canónico.

El resultado sobre vacunación etiquetada ilustra la importancia clínica de esta distinción. Un mismo conteo de capa puede corresponder a una alteración relacionada con la gripe más una segunda condición vacunal, o a una alteración neumocócica más esa misma segunda condición. Las recomendaciones actuales de vacunación en cáncer tratan la vacunación antigripal y la antineumocócica como objetos clínicos distintos,[14] por lo que la identidad borrada por el conteo de capa sigue siendo necesaria para Q_vac. Esto es coherente con una observación más amplia sobre representaciones de aprendizaje automático: la invariancia por permutación solo es útil cuando la intercambiabilidad está justificada,[4] y los modelos clínicos basados en conjuntos pueden necesitar restaurar la estructura de tipos de variables que una representación indiferenciada del conjunto pierde.[5] El presente resultado es determinista, no empírico, pero hace explícito el mismo riesgo representacional respecto de la operación especificada.

El resultado sobre el conteo de U aborda una pérdida diferente. La clase terminal puede seguir siendo `APTO` mientras aparece un valor U en el estado subyacente. En este estudio, U no es una puntuación de confianza, una probabilidad ni un marcador de trabajo inconcluso. El testigo utiliza un valor observado de CD4 que la regla publicada de IMMUNO-1 sitúa en una región no binaria. Trabajos posteriores del SV formalizaron condiciones operativas de certificación de no clausura,[13] pero esas condiciones posteriores no se vuelven a demostrar aquí; la prueba actual solo necesita el valor ternario devuelto por la región de regla publicada de IMMUNO-1. No se introduce ningún subtipo de U y el alfabeto ternario permanece atómico.

La realización independiente de integridad demuestra que la construcción de cuatro niveles no depende de U: su operación de nivel 2 cuenta controles comprometidos y todas las entradas de los testigos están presentes. Esta realización no es una capa obligatoria de una célula clínica ni una extensión de IMMUNO-1; es un dominio independiente utilizado para mostrar que la construcción de frontera no queda confinada a la semántica de parámetros clínicos. El trabajo contemporáneo sobre IA clínica concede una importancia creciente a la documentación estructurada y auditable de los sistemas y a la integridad de su ciclo de vida,[17] pero un dictamen de integridad y un dictamen de dominio clínico responden a preguntas diferentes. La construcción local de frontera conserva esa separación.

La misma localidad aclara las afirmaciones sobre interfaces. Si una interfaz transmite únicamente H = φ ∘ Fⱼ, la recuperación exacta aguas abajo debe evaluarse respecto de H y no respecto de información que existía aguas arriba pero no fue transmitida. Una representación puede ser plenamente adecuada para un propósito de interfaz e insuficiente para otra operación. De modo recíproco, si un componente posterior utiliza información adicional S, la afirmación pertinente es Q = q(H,S), no recuperación desde H por sí sola. La insuficiencia representacional es una propiedad del par representación-operación; no modifica el estado ternario subyacente ni autoriza a reconstruir como resultado fuerte una distinción que la representación ha borrado.

Varias limitaciones delimitan el resultado. IMMUNO-1 es un demostrador teórico-técnico publicado previamente, no un sistema de apoyo a la decisión clínica validado; aquí no se evalúan cohortes de pacientes, desenlaces clínicos, calibración ni recomendaciones terapéuticas. Los umbrales y reglas paramétricas se heredan de las células publicadas y no se revalidan en este artículo. Q_loc y Q_layer son controles estructurales, no recomendaciones clínicas ni de gobernanza. La frontera es relativa al espacio de estados realizados y a los cuatro niveles declarados, y no demuestra optimalidad global frente a otras representaciones posibles. Por último, la realizabilidad es esencial: como X = C(D_c) puede ser un subconjunto estricto de Σ^I, los vectores simbólicos arbitrarios no bastan como contraejemplos. Por ello, el material suplementario proporciona un certificado estático y basado en reglas de realizabilidad conjunta para cada estado separador de IMMUNO-1.

Dentro de estos límites, la construcción ofrece una disciplina formal práctica para informática biomédica: antes de sustituir un estado estructurado rico por una representación agregada, puede declararse explícitamente la operación posterior, aportarse una aplicación de recuperación exacta y someterse la frontera de agregación siguiente a un par realizable conforme a las reglas. El resultado es una afirmación local y auditable sobre adecuación representacional, en lugar de la presunción de que un mismo nivel de detalle sirve para todas las tareas.

## Conclusión

Las fronteras de resolución específicas de la operación proporcionan una forma finita y verificable de declarar qué conserva una agregación determinada y qué destruye. En una célula inmunológica especificada previamente y en una célula independiente de integridad de sistemas de IA, las operaciones seleccionadas realizan constructivamente los cuatro niveles de un mismo patrón declarado de representación, y cada frontera no terminal queda respaldada por una aplicación explícita de recuperación y un par separador realizable conforme a las reglas. El resultado es deliberadamente local: no selecciona una representación universalmente óptima ni prescribe cómo deben conectarse las células. Su utilidad consiste en hacer explícita la pérdida de información representacional antes de sustituir un estado rico por su agregado.

## Referencias

1. Stead WW, Aliferis CF, Bastarache L, et al. Theory and practice in biomedical informatics: a framework for discovery. *J Am Med Inform Assoc.* 2026;33(8):1532-1537. doi:10.1093/jamia/ocag079.
2. Boxwala AA, Peleg M, Tu S, et al. GLIF3: a representation format for sharable computer-interpretable clinical practice guidelines. *J Biomed Inform.* 2004;37(3):147-161. doi:10.1016/j.jbi.2004.04.002.
3. Cortesi A, Filé G, Winsborough WH. The quotient of an abstract interpretation. *Theor Comput Sci.* 1998;202(1-2):163-192. doi:10.1016/S0304-3975(97)00137-0.
4. Zaheer M, Kottur S, Ravanbakhsh S, et al. Deep Sets. En: *Advances in Neural Information Processing Systems 30.* Curran Associates; 2017:3391-3401.
5. Lee J, Lee K, Kim C, et al. Structure-Aware Set Transformers: Temporal and Variable-Type Attention Biases for Asynchronous Clinical Time Series. arXiv [prepublicación]. 2026. doi:10.48550/arXiv.2603.06605.
6. Simas T. Decision Quotient: A Regime-Sensitive Complexity Theory of Exact Relevance Certification. arXiv [prepublicación]. 2026. doi:10.48550/arXiv.2603.14689.
7. Sevetlidis V. Bayes-Sufficient Representations in Supervised Learning. arXiv [prepublicación]. 2026. doi:10.48550/arXiv.2606.04045.
8. Lloret Egea JA. De SVcustos, el marco de intrusión, hasta SVperitus: IMMUNO-1—Profilaxis infecciosa y vacunación. Célula SV(25,5). IA eñ. Publicado el 5 de marzo de 2026. doi:10.21428/39829d0b.272c2f67.
9. Lloret Egea JA. Compilador de fundamentos y célula meta SV(9,3)-IA. IA eñ. Publicado el 7 de marzo de 2026. doi:10.21428/39829d0b.3d7a0dce.
10. Lloret Egea JA. Fundamentos algebraico-semánticos del Sistema Vectorial SV. IA eñ. Publicado el 9 de marzo de 2026. doi:10.21428/39829d0b.b0cf9a13.
11. Lloret Egea JA. Álgebra de composición intercelular del marco SV—IV. Transducción al alfabeto ternario e interfaz paramétrica del sistema. IA eñ. Publicado el 11 de marzo de 2026. doi:10.21428/39829d0b.5c31d534.
12. Lloret Egea JA. Álgebra de composición intercelular—V. Invariantes, agentes especializados y operador de consulta del sistema. IA eñ. Publicado el 11 de marzo de 2026. doi:10.21428/39829d0b.82f5fca3.
13. Lloret Egea JA. Certified non-closure in finite resolution systems: operational certificates, conservative morphisms and revision complexity. IA eñ. Publicado el 8 de agosto de 2026. doi:10.21428/39829d0b.f0892864.
14. Kamboj M, Bohlke K, Baptiste DM, et al. Vaccination of adults with cancer: ASCO guideline. *J Clin Oncol.* 2024;42(14):1699-1721. doi:10.1200/JCO.24.00032.
15. Taplitz RA, Kennedy EB, Bow EJ, et al. Antimicrobial prophylaxis for adult patients with cancer-related immunosuppression: ASCO and IDSA clinical practice guideline update. *J Clin Oncol.* 2018;36(30):3043-3054. doi:10.1200/JCO.18.00374.
16. Lloret Egea JA. Álgebra de composición intercelular del marco SV-I. Transmisión en serie por parámetro puente. IA eñ. Publicado el 10 de marzo de 2026. doi:10.21428/39829d0b.399c03b0.
17. Lohachab A, Jung F, Rommes S, et al. SMART: structured, meaningful, auditable, responsible, and transparent documentation for clinical AI. *J Am Med Inform Assoc.* Publicado en línea el 19 de agosto de 2026. doi:10.1093/jamia/ocag117.

---

# Material suplementario

Estas tablas y notas reproducen únicamente las regiones de regla publicadas y las asignaciones formales de testigos necesarias para verificar el artículo. No son casos de pacientes, no constituyen recomendaciones clínicas y no dependen de ejecución de software ni de artefactos ejecutables como evidencia.

## Tabla suplementaria S1. Diccionario de parámetros IMMUNO-1 utilizado en el estudio

**Abreviaturas:** ANC, recuento absoluto de neutrófilos; BTKi, inhibidor de la tirosina cinasa de Bruton; CAR-T, linfocito T con receptor quimérico de antígeno; TPH, trasplante de progenitores hematopoyéticos; IFD, enfermedad fúngica invasora; MDR, multirresistente; PJP, neumonía por *Pneumocystis jirovecii*. Las condiciones basales seleccionadas son elecciones específicas compatibles con las reglas, no recomendaciones clínicas alternativas. El estudio no utiliza ausencia de datos como testigo de U.

| Parámetro | Capa | Significado | Región 0 conjuntamente compatible elegida para d° | Sustitución del testigo utilizada en este estudio |
|---|---:|---|---|---|
| P01 | 1 | Neutropenia | ANC 1500 células/µL; sin nadir previsto <500 células/µL durante ≥7 días | — |
| P02 | 1 | Linfopenia/depleción T | CD4 600 células/µL; sin terapia activa depletora de células T | x_loc: CD4 150 células/µL → 1; y_U: CD4 observado 350 células/µL → U |
| P03 | 1 | Hipogammaglobulinemia | IgG 800 mg/dL; sin infección bacteriana grave recurrente | — |
| P04 | 1 | Función esplénica | Ausencia de asplenia anatómica y de hipoesplenismo funcional | — |
| P05 | 1 | Barreras/catéteres | Mucositis grado 0; sin ulceración cutánea relevante; sin catéter venoso central complicado | — |
| P06 | 2 | Fase de la neoplasia | Mantenimiento o fase crónica estable | — |
| P07 | 2 | Quimioterapia | Tratamiento de baja intensidad sin quimioterapia intensiva en los 90 días previos | — |
| P08 | 2 | Biológicos inmunosupresores | Sin exposición relevante a anti-CD20/BTKi/PI3Ki en el periodo declarado; cribado viral documentado | — |
| P09 | 2 | TPH/CAR-T | TPH autólogo >2 años antes, con programa activo de profilaxis y revacunación | — |
| P10 | 2 | Corticoides sistémicos | Equivalente de prednisona 5 mg/día durante 1 semana; evaluación y manejo del riesgo documentados | — |
| P11 | 3 | Infecciones bacterianas graves | Sin infección bacteriana grave en los 12 meses previos | — |
| P12 | 3 | IFD previa/contexto de alto riesgo | Sin IFD previa y sin contexto actual de alto riesgo de IFD | — |
| P13 | 3 | Infección viral crónica/latente | Cribado viral completo con plan de manejo apropiado y documentado | — |
| P14 | 3 | Colonización MDR | Sin colonización MDR conocida | — |
| P15 | 3 | Exposición sanitaria reciente | Sin hospitalización prolongada ni ingreso reciente en UCI | — |
| P16 | 4 | Vacunación antigripal estacional | Vacunado en la temporada actual; sin contraindicación en conflicto | x_vac: no vacunado en la temporada actual sin contraindicación documentada → 1 |
| P17 | 4 | Vacunación antineumocócica | Secuencia completa de vacunación antineumocócica | y_vac: no consta secuencia de vacunación antineumocócica → 1 |
| P18 | 4 | Vacunación frente a SARS-CoV-2 | Pauta primaria y refuerzos actualizados | — |
| P19 | 4 | Vacunación frente a hepatitis B | Serie completa frente a hepatitis B con anti-HBs ≥10 UI/L | — |
| P20 | 4 | Otras condiciones vacunales relevantes | Calendario vacunal adecuado; ninguna vacuna viva administrada bajo contraindicación activa | x_vac e y_vac: la misma administración de vacuna viva bajo contraindicación activa → 1 |
| P21 | 5 | Profilaxis frente a PJP | No se cumplen criterios de indicación de profilaxis frente a PJP | x_loc: se consideran cumplidos los criterios y se mantiene profilaxis activa y correcta → 0 |
| P22 | 5 | Profilaxis/monitorización antiviral | Profilaxis o monitorización antiviral adecuada y documentada | — |
| P23 | 5 | Profilaxis antifúngica | Sin contexto de alto riesgo de IFD; estado de profilaxis compatible con esa región 0 | — |
| P24 | 5 | Profilaxis antibacteriana en neutropenia | Sin neutropenia prolongada de alto riesgo; política razonada de profilaxis documentada | — |
| P25 | 5 | Plan estructurado de reevaluación | Plan explícito de reevaluación con periodicidad definida y revisión de vacunación | y_loc: ausencia de plan explícito de reevaluación; manejo puramente reactivo → 1 |

## Nota suplementaria S1. Certificado estático de realizabilidad conjunta

Se define d° imponiendo simultáneamente las condiciones basales seleccionadas de la Tabla suplementaria S1. Estas condiciones son conjuntamente compatibles. Las condiciones cruzadas entre coordenadas relevantes para los testigos quedan fijadas expresamente: P12 y P23 comparten un contexto sin IFD previa y sin alto riesgo fúngico; P11 y P15 utilizan ausencia de sus sucesos desencadenantes, por lo que P25 puede fijarse de manera independiente en 1 en y_loc; P21 se mantiene en 0 mediante profilaxis activa y correcta frente a PJP cuando P02 cambia a 1 en x_loc; y P04 queda fijado por la confirmación de un bazo funcionante con independencia de las sustituciones de la capa vacunal. Los cinco testigos no basales se obtienen exclusivamente mediante las sustituciones declaradas en la Tabla S1, con el ajuste de la región 0 de P21 recién indicado para x_loc. Por tanto, cada testigo constituye una única asignación conjuntamente satisfacible conforme a las reglas publicadas y no un empalme coordenada por coordenada. No se utiliza ejecución de programas para establecer la pertenencia a X. Los estados completos resultantes se enumeran en la Tabla suplementaria S2.

## Tabla suplementaria S2. Seis estados constituidos de IMMUNO-1 utilizados en C0-C2

| Parámetro | v° | x_vac | y_vac | x_loc | y_loc | y_U |
|---|---:|---:|---:|---:|---:|---:|
| P01 | 0 | 0 | 0 | 0 | 0 | 0 |
| P02 | 0 | 0 | 0 | 1 | 0 | U |
| P03 | 0 | 0 | 0 | 0 | 0 | 0 |
| P04 | 0 | 0 | 0 | 0 | 0 | 0 |
| P05 | 0 | 0 | 0 | 0 | 0 | 0 |
| P06 | 0 | 0 | 0 | 0 | 0 | 0 |
| P07 | 0 | 0 | 0 | 0 | 0 | 0 |
| P08 | 0 | 0 | 0 | 0 | 0 | 0 |
| P09 | 0 | 0 | 0 | 0 | 0 | 0 |
| P10 | 0 | 0 | 0 | 0 | 0 | 0 |
| P11 | 0 | 0 | 0 | 0 | 0 | 0 |
| P12 | 0 | 0 | 0 | 0 | 0 | 0 |
| P13 | 0 | 0 | 0 | 0 | 0 | 0 |
| P14 | 0 | 0 | 0 | 0 | 0 | 0 |
| P15 | 0 | 0 | 0 | 0 | 0 | 0 |
| P16 | 0 | 1 | 0 | 0 | 0 | 0 |
| P17 | 0 | 0 | 1 | 0 | 0 | 0 |
| P18 | 0 | 0 | 0 | 0 | 0 | 0 |
| P19 | 0 | 0 | 0 | 0 | 0 | 0 |
| P20 | 0 | 1 | 1 | 0 | 0 | 0 |
| P21 | 0 | 0 | 0 | 0 | 0 | 0 |
| P22 | 0 | 0 | 0 | 0 | 0 | 0 |
| P23 | 0 | 0 | 0 | 0 | 0 | 0 |
| P24 | 0 | 0 | 0 | 0 | 0 | 0 |
| P25 | 0 | 0 | 0 | 0 | 1 | 0 |

Representaciones derivadas: v° tiene F₂ = (25,0,0) y F₃ = `APTO`. x_vac e y_vac tienen F₁ idéntico, con conteos de la capa de vacunación (3,2,0). x_loc e y_loc tienen ambos F₂ = (24,1,0). y_U tiene F₂ = (24,0,1) y F₃ = `APTO`. Los estados son asignaciones formales de reglas, no narraciones de pacientes. Su realizabilidad conjunta queda establecida de forma estática en la Nota suplementaria S1.

## Tabla suplementaria S3. Diccionario de integridad de sistemas de IA y estados testigo completamente observados

Para todos los controles, `False` se transforma en 1 —comprometido—. Todos los estados testigo siguientes proporcionan explícitamente cada campo booleano; no se utiliza `None` ni ningún campo ausente.

| Control | Capa | Significado | Campo booleano | Criterio `True` → 0 |
|---|---:|---|---|---|
| M1 | 1 | Integridad de pesos | weights_integrity | Hash/firma de los pesos del modelo verificados |
| M2 | 1 | Procedencia del conjunto de datos | dataset_provenance | Trazabilidad y licencia del conjunto de datos verificadas |
| M3 | 1 | Control de acceso | access_control | Identidades y permisos correctamente gestionados |
| M4 | 2 | Pruebas adversariales | adversarial_tests | Comprobaciones de robustez adversarial verificadas |
| M5 | 2 | Telemetría | telemetry_active | Monitorización de inferencia activa |
| M6 | 2 | Aislamiento de entornos | environment_isolation | Separación desarrollo/preproducción/producción verificada |
| M7 | 3 | Registro inmutable | immutable_logging | Registro operativo inmutable activo |
| M8 | 3 | Supervisión humana | human_oversight | Circuitos de revisión humana activos |
| M9 | 3 | Cadena de suministro de software | supply_chain_integrity | Integridad de dependencias verificada |

| Control | m° | x_model | y_model | x_layer | y_layer | x_comp | y_comp |
|---|---:|---:|---:|---:|---:|---:|---:|
| M1 | 0 | 1 | 0 | 1 | 0 | 1 | 1 |
| M2 | 0 | 0 | 1 | 0 | 0 | 1 | 1 |
| M3 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| M4 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| M5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| M6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| M7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| M8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| M9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F₂ | (9,0,0) | (8,1,0) | (8,1,0) | (8,1,0) | (8,1,0) | (6,3,0) | (5,4,0) |
| F₃ | `NORMAL` | `NORMAL` | `NORMAL` | `NORMAL` | `NORMAL` | `INDETERMINATE` | `INDETERMINATE` |

## Nota suplementaria S2. Verificación de frontera

Fíjese j ∈ {0,1,2}. Supóngase Q = qⱼ ∘ Fⱼ para una aplicación explícita de recuperación y supóngase que x, y ∈ X satisfacen Fⱼ₊₁(x) = Fⱼ₊₁(y), pero Q(x) ≠ Q(y). Si existiera una aplicación qⱼ₊₁ con Q = qⱼ₊₁ ∘ Fⱼ₊₁, entonces Q(x) = qⱼ₊₁(Fⱼ₊₁(x)) = qⱼ₊₁(Fⱼ₊₁(y)) = Q(y), en contradicción con el testigo. Como Fⱼ₊₁ = rⱼ ∘ Fⱼ, la recuperabilidad desde un nivel posterior implica recuperabilidad desde cada nivel precedente; y, como F₀ es la identidad, los niveles recuperables forman un segmento inicial no vacío. La aplicación de recuperación en el nivel j y el par separador en el nivel j + 1 establecen, por tanto, la frontera declarada. Este argumento verifica la frontera; no reivindica un nuevo teorema de factorización.
