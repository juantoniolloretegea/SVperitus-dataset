# Constitución y agotamiento del primer universo de ciberseguridad inteligente

**OP-CYB-001. Evaluación de la evidencia de corrección de una vulnerabilidad mediante actualización de un activo informático. Versión 0.2. 9 de septiembre de 2026.**

## Resumen

Se presenta la constitución del primer universo como un conjunto finito de 24 parámetros atómicos, con nueve incorporaciones respecto del registro anterior. El objeto profesional es aconsejar al experto sobre la suficiencia de la evidencia para cerrar una corrección por actualización. La investigación distingue los estados de instalación, ejecución, almacenamiento, configuración, referencias, caché e historia, y los relaciona con las consecuencias de omitir conocimiento necesario. La terminación se fundamenta en la revisión de veinte ámbitos de necesidad, ocho clases de acción y 36 candidatos adicionales resueltos mediante composición, contexto, control, derivación o exclusión motivada. La enumeración histórica de 31 distinciones se conserva y se amplía en profundidad; no se utiliza como límite para detener la investigación.

El resultado constituye un cierre del inventario paramétrico del perímetro definido. No se acredita por ello la eficacia de una actualización real ni la ejecución del universo por el Lenguaje SV. Esta diferencia no se emplea para interrumpir la búsqueda de parámetros: ambas cuestiones se han examinado por separado. La decisión sobre el siguiente trabajo —contraste con el Lenguaje o constitución de un segundo universo— corresponde al Director.

## 1. Problema profesional y rectificación del antecedente

Una actualización puede haber terminado satisfactoriamente según el instalador y no haber producido todavía todos los efectos necesarios. El componente almacenado puede diferir del utilizado; un programa puede conservar valores anteriores; una tarea puede seguir ejecutando funciones previas; y una modificación posterior puede invalidar la evidencia que justificaba el cierre. La guía de planificación de actualizaciones de Souppaya y Scarfone distingue expresamente preparación, aplicación, comprobación y seguimiento. La comprobación debe considerar que el cambio se haya instalado y haya surtido efecto. [T001](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#t001)

El documento anterior incurrió en dos errores diferentes. En la presentación, empleó una redacción excesivamente abreviada y tablas mal formadas. En el método, trató la asignación de todas las preguntas a algún apartado como si demostrase que se habían agotado las distinciones profesionales. Además, permitió que las limitaciones de realización computacional interrumpieran una investigación conceptual todavía incompleta. La presente versión sustituye ese criterio de terminación y el dictamen que se apoyaba en él.

Se ha aplicado el acta obligatoria del español: redacción gramaticalmente completa, significado explícito, términos técnicos necesarios y distinción entre hechos, deducciones y trabajo pendiente. Los identificadores estables y los nombres oficiales de interfaces se conservan por su función de trazabilidad. La revisión de este expediente no se presenta como cierre de la obligación general de revisar todos los repositorios SV. [SV-ES](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#sv-es)

## 2. Perímetro y producto del universo

El universo examina un activo informático identificado, una vulnerabilidad concreta, una actualización y un episodio de instalación, dentro de un horizonte temporal declarado. Incluye los componentes, instancias y dependencias cuya consideración sea necesaria para valorar la corrección o las consecuencias del consejo. Comprende software de aplicación, sistema operativo y componentes de plataforma cuando existe un perfil de observación pertinente. Una regla de Windows no se aplica por analogía a Linux o al programa residente de un dispositivo.

El producto es un dictamen explicado al experto: evidencia suficiente para el cierre en el alcance declarado; evidencia insuficiente, con identificación de lo que falta; o exclusión fundada de la corrección examinada por falta de aplicabilidad. La exclusión no afirma que el activo carezca de otras vulnerabilidades. Un fallo técnico de observación o ejecución no constituye otra salida profesional: impide una ejecución válida y produce su registro técnico.

Se incluyen las consecuencias de completar la actuación, aplazarla, recuperar un estado o adoptar una alternativa. La valoración técnica de si una corrección está acreditada permanece separada de la decisión humana de aceptar un riesgo o autorizar una intervención. Una aceptación de riesgo no cambia un resultado de «corrección no acreditada» a «corregido».

Quedan fuera la ejecución material de cambios, la explotación de vulnerabilidades, la respuesta completa a incidentes, la restauración operativa y la intervención en procesos industriales. Sus resultados pueden ser referencias necesarias, con objeto, responsable y alcance explícitos. La robustez, privacidad y validez de un modelo de IA tampoco se deducen de que su biblioteca de software se haya actualizado: pertenecen a otra finalidad profesional del dominio.

## 3. Fundamento educativo y documental

### 3.1. País vector y formación de base

La base educativa sigue siendo España, mediante el Grado en Ingeniería de la Ciberseguridad de la Universidad Rey Juan Carlos, curso 2026–2027, con cuarenta asignaturas y 240 ECTS. Se trata de la elección de un plan concreto como referencia organizadora, no de la afirmación de que representa a todas las universidades españolas ni de un rango internacional de excelencia. Los complementos seleccionados de Reino Unido, Australia y Canadá permiten contrastar factores humanos, investigación, inteligencia de amenazas e IA. El catálogo conserva las reservas documentales de cada programa y no convierte sus créditos entre sistemas educativos.

Este universo exige especialmente comprender procesos, memoria, archivos y almacenamiento; ingeniería de software y dependencias; verificación técnica; riesgo y continuidad. La guía de Sistemas Operativos establece esa formación y sus prerrequisitos. Su aportación al universo no consiste en proporcionar una lista de términos, sino en permitir distinguir estados que un resultado del instalador no describe. Las guías de ingeniería y seguridad del software, gestión de riesgos y respuesta a incidentes sitúan esos estados en una decisión profesional con consecuencias. [R025](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#r025), [R023](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#r023), [R028](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#r028), [R033](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#r033), [R035](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#r035)

La secuencia educativa se conserva en el trabajo: primero se identifica qué conocimiento permite interpretar un hecho; después se formula la relación necesaria para el consejo; a continuación se examina la consecuencia de omitirla; sólo entonces se adjudica el parámetro. Las asignaturas, sus créditos y sus temas no se convierten automáticamente en universos o parámetros.

### 3.2. Función de las fuentes técnicas

La bibliografía distingue tres funciones. Las guías profesionales fundamentan qué debe comprobarse y por qué. La documentación de implementación determina el significado de una observación en una plataforma concreta. Los estudios empíricos contrastan simplificaciones que podrían conducir a una conclusión errónea. El método de atomicidad es una construcción del proyecto; no se atribuye a NIST, Microsoft, Linux o los autores de los estudios.

NIST SP 800-128 vincula el control del cambio con análisis de impacto, pruebas funcionales y de seguridad, autorización, verificación posterior y conservación de configuraciones anteriores. Su análisis incluye dependencias entre componentes y efectos sobre otras funciones. Estas exigencias fundamentan la cobertura de impactos y la prohibición de cerrar un cambio por su sola instalación. [B01](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#b01)

Dai y colaboradores estudian la presencia de parches completos en ejecutables Java y explican las limitaciones de reconocer únicamente un fragmento. Sun y colaboradores examinan modificaciones entrelazadas y muestran por qué separar cambios sin preservar sus dependencias puede dejar una corrección incompleta. Aquí se emplean esas observaciones como contraejemplos a dos simplificaciones; no se trasladan las tasas de sus experimentos a otras plataformas ni se adoptan sus herramientas como observadores validados del universo. [B08](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#b08), [B09](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#b09)

La documentación de Linux 6.8 distingue habilitación del parche y transición por tarea. La documentación de Windows diferencia creación e inicialización de procesos, referencias que sobreviven a su terminación, escritura almacenada en memoria y sincronización, y programación de operaciones diferidas. Estas fuentes permiten precisar los nuevos parámetros sin afirmar que las interfaces hayan sido ejecutadas en un activo real. [B04](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#b04), [T015](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#t015), [T016](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#t016), [B06](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#b06), [B07](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#b07), [B12](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#b12)

Las capturas nuevas se identifican por documento original, tamaño y huella. Las fuentes anteriores mantienen sus referencias de versión y procedencia. La adquisición para esta revisión es una actividad de investigación declarada: no autoriza a una IA consejera a actualizar el conocimiento durante un caso. La [bibliografía razonada](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md) identifica autoría, edición, localizador, aportación y límites.

## 4. Método de adjudicación y terminación

### 4.1. Qué se cuenta

Un parámetro representa una proposición profesional única, referida a un sujeto definido y evaluable mediante una regla versionada. Sus estados son 1, 0 y U: respectivamente, afirmación acreditada, negación acreditada e información admitida insuficiente o contradictoria. La interpretación concreta depende de la proposición; 1 no significa siempre «favorable» y 0 no significa «fallo técnico».

Un identificador, una fecha, una firma o un campo de un registro pueden ser necesarios sin constituir un parámetro. Un control determina la admisión, la adecuación o el gobierno de la evidencia. Una composición conserva estados independientes y establece su relación para una finalidad. La autoridad humana y el balance económico no se transforman en una puntuación técnica única.

Se aplican las diez condiciones del contrato de atomicidad: identidad, estado único, incertidumbre propia, consecuencia y función separables, variación independiente, efecto de la omisión, ausencia de partición material útil, reproducibilidad y procedencia. Cada ficha incluye el conocimiento requerido, su relación con otro estado y el perjuicio potencial de omitirlo. [SV-AT](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#sv-at)

Una definición puede tener varios usos en sujetos diferentes. Dos réplicas de un servicio no comparten por comodidad el mismo valor. Tampoco generan dos definiciones nuevas si la proposición es idéntica. Cada uso conserva sujeto, evidencia, horizonte, función y consecuencia. Los perfiles técnicos especifican cómo observar; no pueden modificar silenciosamente la proposición.

### 4.2. Búsqueda que permite terminar

La búsqueda se ha organizado por veinte ámbitos: identidad; autenticidad; instalación; reinicio del sistema; reinicio de programas; ejecutables; configuración; parche durante la ejecución; estado residual; escritura y diferimiento; otras acciones necesarias; corrección íntegra; observación; instancias y dependencias; vigencia; funciones y datos; alternativas; tiempo y autorización; proporcionalidad; explicación y gobierno.

Para cada ámbito se ha intentado construir un caso en el que todos los estados ya representados permanecen iguales, pero una distinción omitida cambia la suficiencia de la evidencia o una consecuencia relevante. Si la diferencia corresponde a una proposición independiente, se incorpora. Si es una combinación de estados, se explicita su composición. Si afecta a identidad, evidencia o permiso, se conserva en el control correspondiente. Una exclusión debe identificar el producto profesional distinto que exigiría incluirla.

La primera revisión incorporó nueve parámetros y precisó los usos de los anteriores. La segunda examinó las combinaciones, los límites de los perfiles y los 36 candidatos adicionales que se detallan en la [revisión de cobertura](COBERTURA_Y_REVISION_ADVERSARIAL_OP_CYB_001_v0.2.md). No quedó un candidato sin resolución dentro del perímetro. Las carencias de adquisición de evidencia de un activo concreto no se usaron para excluir un estado necesario del catálogo.

El agotamiento afirmado es constitutivo y relativo a esta versión del universo: todos los candidatos obtenidos mediante el procedimiento declarado tienen resolución y no se conserva una necesidad pertinente sin representación. No es un teorema sobre toda tecnología futura. Un contraejemplo posterior que revele una distinción independiente obligará a revisar la versión mediante decisión humana; nunca habilitará aprendizaje o ampliación automática durante el consejo.

## 5. Resultado paramétrico

| Conjunto | Resultado |
| --- | --- |
| P01–P15 | Quince identidades anteriores conservadas; redacción revisada y cambios de perfil o delimitación declarados. |
| P16–P24 | Nueve parámetros nuevos: configuración persistente, inicialización, habilitación del parche, estado por tarea, referencia a recurso anterior, entrada de caché, selección de carga, sincronización y operación diferida. |
| Total | 24 definiciones. No se ha añadido una posición para completar una dimensión geométrica. |


Las versiones 0.2 de P01, P06 y P13 explicitan perfiles documentales adicionales sin confundir plataformas. P07 precisa que registra el resultado de una prueba individual, no la seguridad general del activo. P15 queda limitado por un registro de ocho clases de acción y por sus estados de cumplimiento. La revisión no transforma una lectura de archivo, un retorno de función ni una prueba compuesta en una garantía general.

La [adjudicación completa de los 24 parámetros](CATALOGO_ATOMICO_OP_CYB_001_v0.2.md) contiene proposición, sujeto, estados, incertidumbre, método, fuentes, independencia y consecuencia. Las agrupaciones anteriores no reciben tamaños matriciales por el hecho de contener cierto número de elementos. SV(9,3) conserva su significado doctrinal y no se interpreta como una matriz cartesiana de tres filas por tres columnas. La cardinalidad del inventario no autoriza relleno, duplicación ni división artificial.

## 6. Consecuencias y suficiencia del consejo

La cadena que debe poder reconstruirse es: conocimiento previo pertinente; relación entre hechos; interpretación que de ella depende; consejo que cambiaría al omitirla; y consecuencia potencial bajo condiciones expresas. Por ejemplo, saber que una biblioteca almacenada puede diferir de la utilizada permite relacionar P13 con P06. Si se omite la relación, el experto podría recibir un consejo de cierre mientras la instancia conserva código anterior. El daño de seguridad sólo es potencial: depende de que ese código contenga la vulnerabilidad pertinente y de que concurran las condiciones necesarias para producir el perjuicio.

La misma disciplina se aplica al exceso de intervención. Si ya se ha acreditado el reinicio requerido, omitir el evento puede inducir otro reinicio. Si una modificación no afecta al criterio de una prueba, invalidarla indiscriminadamente puede generar trabajo e interrupciones sin justificación. El universo registra ambas direcciones del error.

### 6.1. Criterios de evidencia

Cada afirmación debe vincularse a identidad del sujeto, método, versión, instante o intervalo, alcance de observación, fuente de referencia y autoridad de admisión. Se conservan los bytes originales antes de cualquier normalización. Una huella acredita identidad de bytes; la autenticidad y la autorización requieren sus comprobaciones propias. La ausencia de registros sólo permite negar un acontecimiento cuando se acredita la cobertura necesaria del intervalo.

Una prueba favorable exige un criterio establecido antes del resultado y un observador capaz de distinguir los casos relevantes. La falta de permisos puede impedir observar la condición. Dos herramientas con una limitación compartida no acreditan independencia. La documentación de pruebas de NIST fundamenta estas cautelas; no proporciona por sí sola el criterio específico de cada vulnerabilidad. [F018](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#f018)

### 6.2. Impactos, alternativas y proporcionalidad

El análisis de impacto identifica qué servicio y qué personas, procesos o datos dependen del activo. El precio del equipo no equivale al valor de lo protegido. Se comparan el perjuicio de no completar la corrección y el de las actuaciones posibles, incluidos interrupción, recuperación, trabajo y dependencias. Las magnitudes desconocidas se conservan como tales; lo no monetizado no vale cero. NIST SP 800-34 vincula recursos, servicios y consecuencias de interrupción, y distingue objetivos de recuperación y tolerancia a la pérdida de datos. [B10](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#b10)

El principio establecido por el Director —la protección no puede costar más que lo protegido— exige definir el objeto de protección, el horizonte y qué costes se están comparando. No permite comparar el coste de una actuación con el precio de compra de un componente omitiendo el servicio que sostiene. Tampoco permite inventar probabilidades para justificar una intervención. Cuando las alternativas no son ordenables con la evidencia disponible, el consejo presenta esa incertidumbre al experto.

La autorización identifica actor, acto, ámbito y vigencia. Un consejo técnico favorable no es un permiso para actuar. La IA desempeña el papel de consejera vinculada al experto; no asume su responsabilidad ni decide por él. La explicación conserva fuentes, reglas, relaciones, incertidumbres y consecuencias. Su futura representación mediante un Frame deberá respetar la definición del SV; este informe no se denomina Frame por semejanza visual.

## 7. Comprobaciones efectuadas y límites de la evidencia

Se han ejecutado 64 casos sintéticos sobre los nueve perfiles nuevos, incluidos conflictos, falta de cobertura, diferencias de tipo, observaciones ajenas al perfil y fallos técnicos. Siete modificaciones deliberadamente incorrectas del observador documental fueron detectadas por casos concretos. Se conservan resultados esperados, entradas, resultados obtenidos y casos refutadores. Estas comprobaciones verifican distinciones documentales; no miden la sensibilidad de un capturador real ni la eficacia de un parche.

Las fichas contienen argumentos de variación independiente y de pérdida por omisión para los 24 parámetros. Son argumentos de diseño examinados en la revisión adversarial interna. No se presentan como revisión externa por pares ni como experimentos sobre sistemas reales. Los ensayos de versiones anteriores permanecen identificados como antecedentes y no se suman como si se hubieran vuelto a ejecutar en esta revisión.

La revisión de presentación exige tablas Markdown continuas, sin líneas en blanco entre encabezado y cuerpo, y textos legibles fuera de las tablas extensas. No se emplean delimitadores de LaTeX o KaTeX. La comprobación de fórmulas del Excel y de su representación se documenta en el anexo de verificación; no sustituye la evaluación científica del contenido.

## 8. Dimensión prevista del dominio y decisión siguiente

El mapa curricular contiene 29 agrupaciones de operaciones candidatas. Una agrupación no equivale necesariamente a un universo. El escenario central distingue 38 universos y calcula 551 parámetros únicos como estimación de planificación; su lectura prudente es aproximadamente 550. Los escenarios compacto y amplio dan 29 y 59 universos, con 286 y 1.062 parámetros. Estos valores no son recuentos constituidos ni intervalos estadísticos. La [estimación desglosada](ESTIMACION_DEL_DOMINIO_CIBERSEGURIDAD_v0.2.md) conserva supuestos, solapamientos y cálculos editables.

El primer universo aporta 24 definiciones ya examinadas. El segundo, si el Director decide constituirlo, debería aportar un contraste profesional distinto. La evaluación técnica de un sistema de IA, identificada en CYO-23, permitiría examinar robustez, población de uso, datos y criterios de validez, que este universo de actualización no pretende agotar. Los complementos educativos australianos sustentan esa pertinencia, sin decidir por sí solos la prioridad. [M002](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#m002), [M003](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#m003), [M004](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md#m004)

El expediente queda preparado para que el Director elija entre contrastar ahora la representación de este primer universo con el Lenguaje o completar primero un segundo. No se activa ninguna de esas opciones por una instrucción antecedente de otra unidad. La orden humana de concluir el primer universo y decidir después tiene precedencia.
