# Acta de rectificación metodológica y protocolo de constitución gobernada del dominio de inmunología

**Versión:** 0.1  
**Fecha de corte:** 31-08-2026  
**Director:** Juan Antonio Lloret Egea, Ingeniero Director  
**Estatuto:** candidata interna sometida a decisión expresa del Director  

## Declaración de alcance

Este documento fija una rectificación del método de trabajo empleado para acotar el dominio de inmunología. No constituye el dominio, no adopta parámetros, no valida consecuencias clínicas, no tipa matrices o *arrays*, no modifica el álgebra del Sistema Vectorial SV y no produce ninguna recomendación para el lenguaje de computación.

Su finalidad exclusiva es asegurar que el dominio se construya en el orden correcto: desde las competencias profesionales y las operaciones clínicas y de laboratorio hasta el conocimiento necesario, las consecuencias documentadas de su ignorancia o aplicación incorrecta, los datos empíricos y, solo después, su representación formal y su composición.

Quedan expresamente fuera de este documento:

- la adopción de IMMUNO-1 o IMMUNO-2 como dominio;
- el cierre de un número definitivo de parámetros;
- la atribución automática de competencias profesionales;
- la formulación de umbrales clínicos no constituidos;
- la modificación del lenguaje, de su representación intermedia o de su evolución;
- cualquier inferencia clínica destinada a completar conocimiento ausente;
- cualquier uso asistencial.

## 1. Motivo de la rectificación

El trabajo había comenzado a desplazarse desde la constitución del dominio hacia un inventario heterogéneo de parámetros, entidades, relaciones y repositorios. Ese desplazamiento produjo cuatro errores metodológicos:

1. se tomó una colección candidata de observaciones y acciones como aproximación al dominio profesional completo;
2. se mezclaron enfermedades, síndromes, estados iatrogénicos, complicaciones, fronteras institucionales y categorías diagnósticas;
3. se atribuyeron consecuencias clínicas con baja confianza y sin graduación individual suficiente;
4. se adelantó la representación formal antes de haber constituido las capacidades, operaciones y conocimientos que debía representar.

La rectificación no elimina los activos producidos. Los conserva como antecedentes *append-only*, pero suspende su capacidad para gobernar el dominio.

## 2. Perímetros normativos

### 2.1. Núcleo doctrinal inviolable

Son vinculantes y no pueden ser modificados por este trabajo:

1. **Fundamentos algebraico-semánticos del Sistema Vectorial SV**.
2. **Origen doctrinal, definición y alcance de la U en el Sistema Vectorial SV**.

De estos textos se conservan, entre otros, los siguientes invariantes:

- alfabeto ternario canónico `{0,1,U}`;
- `0 = Apto`, `1 = No_Apto` y `U = Indeterminado`;
- U como estado epistémico de no determinación actual, no como número, nulidad, probabilidad, promedio o comodidad;
- exigencia de fundamento suficiente y legítimo para clausurar U;
- trazabilidad de la salida inicial, de la intervención experta y de cualquier salida posterior;
- restricción de la unidad exacta simple `n = b²`, con `b ≥ 3`;
- cardinalidad del espacio exacto igual a `3^n`;
- composición algebraico-semántica tipada, sin operador binario universal;
- primacía decisional humana y subordinación de cualquier IA;
- exclusión de la probabilidad opaca como fundamento primario de decisión.

La estadística, la epidemiología y el tiempo pueden formar parte del conocimiento clínico, de los datos externos y de los estándares médicos. No se convierten por ello en primitivas internas del formalismo. La frontera entre ambos planos deberá quedar declarada.

### 2.2. Contexto algebraico de composición

El documento **Álgebra de composición intercelular del Sistema Vectorial SV** se mantiene como contexto formal subordinante. Solo podrá ser contravenido por ampliación expresamente autorizada o por error demostrado.

El dominio de inmunología no decidirá qué operador formal debe aplicarse. Primero constituirá dependencias clínicas, direcciones, condiciones de paso, vetos, transferencias y consecuencias. La unidad responsable del desarrollo formal decidirá posteriormente si esas relaciones son representables mediante operadores ya constituidos o si existe un residual.

### 2.3. Perímetro clínico y profesional

El dominio médico no se deriva del nombre SV ni de IMMUNO-1 o IMMUNO-2. Se delimita mediante fuentes profesionales y clínicas autorizadas, con jurisdicción, versión y función declaradas.

El programa oficial español de Inmunología constituye el anclaje jurisdiccional inicial para España. Define una especialidad mixta de laboratorio y clínica, con competencias comunes para titulaciones de acceso diferentes y actividades clínicas específicas para médicos. El programa oficial español de Alergología constituye una frontera profesional independiente y parcialmente solapada.

Los currículos de otras jurisdicciones se utilizarán como contraste de cobertura y actualización, nunca como sustitución silenciosa del perímetro español. Una competencia británica, canadiense, estadounidense o austral no se atribuirá automáticamente a un especialista español ni se fusionará con otra competencia por semejanza terminológica.

Los programas formativos delimitan conocimiento, habilidades, responsabilidad y práctica esperada. No prueban por sí solos la magnitud de una consecuencia clínica. Las consecuencias deberán respaldarse mediante evidencia clínica específica y vigente.

## 3. Objeto que debe constituirse

El objeto primario no es una lista de parámetros. Es un dominio profesional-operativo formado por objetos de tipos distintos y enlazados con trazabilidad completa.

| Tipo | Definición | No debe confundirse con |
|---|---|---|
| Autoridad | Organismo que emite una fuente o norma | Evidencia clínica individual |
| Jurisdicción | Ámbito territorial y regulatorio | Universalidad médica |
| Función profesional | Rol desde el que se ejecuta o supervisa una actividad | Título genérico de “inmunólogo” |
| Capacidad | Actividad profesional compleja que debe poder desempeñarse | Tema de estudio |
| Conocimiento | Contenido que debe estar constituido antes de una operación | Dato de un paciente |
| Habilidad | Actuación demostrable, interpretable y evaluable | Afirmación teórica |
| Operación | Acto clínico, diagnóstico, terapéutico, preventivo, analítico o de supervisión | Resultado aislado |
| Presentación | Problema o patrón que inicia una evaluación | Diagnóstico confirmado |
| Entidad | Enfermedad, síndrome o estado definido por una fuente versionada | Parámetro o complicación |
| Observación | Hecho obtenido en un episodio | Regla de decisión |
| Parámetro | Unidad semántica mínima necesaria para una operación | Familia clínica completa |
| Relación | Dependencia tipada entre objetos | Asociación narrativa |
| Consecuencia | Daño o fallo documentado bajo condiciones explícitas | Justificación retrospectiva |
| Residual | Contenido identificado que no puede adoptarse todavía | Ausencia inexistente |

Ningún objeto podrá cambiar de tipo para resolver una carencia. Una frontera institucional no se registrará como enfermedad; una intervención no se registrará como biomarcador; una advertencia no se declarará como habilidad; una consecuencia no sustituirá a la evidencia que la sostiene.

## 4. Arquitectura correcta del dominio

La constitución seguirá ocho estratos ordenados.

### Estrato 1. Autoridad, jurisdicción y función

Para cada fuente se registrarán como mínimo:

- organismo emisor;
- jurisdicción;
- profesión o vía de acceso;
- versión y fecha de vigencia;
- ámbito asistencial o de laboratorio;
- responsabilidades propias, compartidas y excluidas;
- condición de fuente oficial, estándar profesional, guía clínica, clasificación o estudio.

No habrá una figura universal y no tipada de “el inmunólogo”. El dominio distinguirá, al menos, el núcleo común de laboratorio, la función médica clínica, las competencias compartidas y las fronteras interdisciplinares.

### Estrato 2. Capacidades profesionales

Cada capacidad deberá formularse como una actividad verificable. Entre las clases iniciales que deben ser extraídas de los programas oficiales se encuentran:

- selección, realización, validación e interpretación de pruebas inmunológicas;
- emisión de informes y asesoramiento clínico-laboratorial;
- reconocimiento, evaluación y seguimiento de inmunodeficiencias primarias y secundarias;
- evaluación de autoinmunidad, autoinflamación, hipersensibilidad y enfermedad inmunomediada;
- histocompatibilidad, trasplante e inmunogenética;
- administración y seguimiento de terapias inmunológicas;
- vacunación e inmunoprofilaxis en poblaciones especiales;
- calidad, seguridad, acreditación y dirección de laboratorio;
- coordinación multidisciplinar, transición asistencial y comunicación;
- investigación, revisión crítica y actualización controlada del conocimiento.

Esta relación es un índice de extracción, no una adopción exhaustiva.

### Estrato 3. Conocimientos y habilidades

Para cada capacidad se separarán:

- conocimientos de mecanismos inmunológicos;
- conocimientos de presentaciones y entidades;
- conocimiento de indicaciones, contraindicaciones y limitaciones;
- conocimientos preanalíticos, analíticos y postanalíticos;
- habilidad para obtener información clínica;
- habilidad para seleccionar y realizar una prueba;
- habilidad para validar, interpretar y comunicar un resultado;
- habilidad para formular y ejecutar una actuación;
- habilidad para reconocer el límite propio y transferir o escalar;
- nivel de supervisión o autonomía exigido;
- evidencia aceptada de competencia.

Un texto como “no confundir A con B” no bastará como habilidad. Deberá transformarse, mediante fuente explícita, en una actuación evaluable: distinguir, seleccionar, interpretar, excluir, confirmar, tratar, vigilar, informar o escalar.

### Estrato 4. Operaciones

Toda operación tendrá un identificador estable y deberá declarar:

- finalidad;
- función profesional autorizada;
- población y contexto;
- presentación o entidad de entrada;
- conocimiento previo requerido;
- observaciones obligatorias;
- observaciones condicionales;
- exclusiones y contraindicaciones;
- secuencia o dependencias;
- salida permitida;
- condición de abstención;
- responsable de la decisión final.

La suficiencia será relativa a una operación concreta. El sistema podrá conocer suficientemente una operación y no otra. Se prohíbe tanto fingir conocimiento como producir una alarma universal por cualquier ausencia irrelevante.

### Estrato 5. Consecuencias

La consecuencia se constituirá *ex ante*, antes de que una operación pueda emitir una salida utilizable. No se admitirá una explicación narrativa construida después de conocer el resultado.

Cada registro de consecuencia contendrá:

| Campo | Contenido obligatorio |
|---|---|
| Objeto omitido o mal aplicado | Conocimiento, habilidad, observación, regla, orden o actuación |
| Tipo de fallo | Ignorancia, omisión, interpretación errónea, aplicación fuera de contexto, composición indebida o actuación tardía |
| Condiciones de aplicabilidad | Población, presentación, entidad, tratamiento, estado y marco asistencial |
| Efecto inmediato | Fallo diagnóstico, terapéutico, preventivo, analítico o de seguimiento |
| Consecuencia para el paciente | Daño clínico documentado, graduado y condicionado |
| Consecuencia para el experto | Pérdida de información, error de decisión, incumplimiento de estándar o necesidad de escalado |
| Fuente | Documento clínico primario o guía autorizada, con localizador y versión |
| Fuerza | Sistema de graduación declarado; sin promedios encubiertos |
| Conflicto | Concordancias, discrepancias y límites entre fuentes |
| Estado | Propuesto, verificado, disputado, adoptado, sustituido o retirado prospectivamente |

Las consecuencias no se expresarán como causalidades absolutas cuando la fuente solo respalde aumento de riesgo, asociación o posibilidad condicionada. Se distinguirán cuatro fallos que no son equivalentes:

1. conocimiento no constituido;
2. dato del episodio ausente o inadmisible;
3. conocimiento aplicado de forma incorrecta;
4. conocimiento correcto compuesto en orden o contexto incorrectos.

### Estrato 6. Observaciones y parámetros

Un parámetro solo podrá proponerse después de identificar la operación que lo necesita. Para ser admisible deberá cumplir simultáneamente:

1. indivisibilidad clínica suficiente;
2. función explícita dentro de una operación;
3. nombre y definición inequívocos;
4. tipo de dato y valores permitidos;
5. unidad, método, espécimen o fuente, cuando proceda;
6. población y rango contextual, cuando proceda;
7. anclaje de episodio o ventana externa, cuando proceda;
8. fuente clínica y versión;
9. consecuencia documentada de omisión, error o aplicación indebida;
10. estado de evidencia y residual;
11. jurisdicción y función profesional;
12. relación con datos empíricos reales.

No serán parámetros admisibles los compuestos vagos como “estado inmunológico”, “riesgo infeccioso” o “respuesta vacunal” si ocultan componentes clínicamente distintos.

La prioridad 1–20, si se mantiene, deberá conservar cada eje separado. No podrá promediarse para producir una prioridad única. Ninguna prioridad sustituirá a la consecuencia ni a la decisión humana de adopción.

### Estrato 7. Evidencia y datos

La comprobación empírica no se pospondrá hasta el final. Cada operación candidata deberá tener una ruta paralela de datos que determine:

- repositorio o cohorte;
- población incluida y excluida;
- variable real y diccionario;
- método y unidad;
- temporalidad externa;
- exposiciones y tratamientos concomitantes;
- desenlaces;
- datos ausentes;
- número efectivo de registros utilizables;
- condiciones legales y de publicación;
- correspondencia exacta con la operación y el parámetro;
- limitaciones de representatividad.

La existencia de un portal, registro o publicación no prueba que contenga el objeto clínico requerido. “No leído”, “no accesible”, “objeto distinto” y “no encontrado” serán estados diferentes.

Una operación sin datos adecuados podrá conservarse como conocimiento clínico, pero no podrá presentarse como validada empíricamente. La ausencia de cohortes no se rellenará mediante simulación o inferencia.

### Estrato 8. Representación y composición

Solo después de cerrar provisionalmente los estratos anteriores se propondrá una representación mediante matrices o *arrays*. En la notación médica o matemática se empleará `a_ij` para identificar el elemento de la fila `i` y la columna `j`.

La forma y el tamaño no se decidirán por conveniencia gráfica ni por prefijos temáticos. Se derivarán del número de parámetros adoptados, de su función, de sus dependencias y de las consecuencias de su composición.

La proyección formal deberá respetar los invariantes doctrinales. En particular, una unidad exacta simple tendrá `n = b²`, `b ≥ 3`, y un espacio de configuraciones de cardinalidad `3^n`. La representación no convierte una fila de `n` parámetros en una matriz cuadrada de otro orden.

La composición se evaluará como relación tipada. Antes de aceptar una unión deberán declararse:

- dirección;
- interfaz;
- parámetro o salida transferida;
- precondiciones;
- operador formal candidato, si corresponde;
- conmutatividad o no conmutatividad;
- consecuencia de invertir el orden;
- consecuencia de omitir un componente;
- condición de veto o parada;
- trazabilidad de la operación compuesta.

## 5. Régimen de conocimiento de la IA

Durante un episodio, el conocimiento autorizado permanecerá congelado en una versión identificable. La IA no podrá:

- aprender del episodio para modificar esa versión;
- completar conocimiento ausente por semejanza;
- importar un umbral desde otra enfermedad o jurisdicción;
- sustituir una observación ausente por prevalencia o probabilidad;
- racionalizar retrospectivamente una salida;
- utilizar la decisión del experto para alterar el acta predecisional.

Para cada operación, la IA deberá quedar en uno de dos estados:

- **conocimiento constituido para la operación:** dispone de la versión autorizada de todos los conocimientos, reglas, interfaces y consecuencias exigibles;
- **conocimiento no constituido para la operación:** falta al menos un elemento obligatorio o existe un conflicto bloqueante.

El segundo estado impide aconsejar. No impide informar al experto de:

- qué elemento no está constituido;
- qué operación queda bloqueada;
- qué consecuencias documentadas tiene decidir ignorando esa carencia;
- qué actuación de medición, revisión, consulta o escalado podría resolverla, si existe y está autorizada.

La U no será una salida cómoda. Tampoco se propagará indiscriminadamente. Solo afectará a la operación y a las dependencias para las que la carencia sea relevante según reglas constituidas.

## 6. Trazabilidad y régimen *append-only*

No se reescribirá ningún conocimiento, consecuencia, salida o decisión. Toda modificación generará un nuevo suceso enlazado con el anterior.

El registro mínimo deberá distinguir:

1. versión de conocimiento congelada;
2. operación solicitada;
3. hechos y observaciones admitidos;
4. hechos ausentes, inadmisibles o en conflicto;
5. conocimiento y habilidades requeridos;
6. consecuencias constituidas aplicables;
7. dependencias y orden evaluados;
8. estado de suficiencia de la operación;
9. salida predecisional del sistema o abstención;
10. *frame* mostrado al experto;
11. decisión humana posterior;
12. correcciones o impugnaciones, siempre como nuevos sucesos;
13. propuesta de actualización para una versión futura, nunca aprendizaje en curso.

La admisibilidad de la salida del sistema y el registro de la decisión humana son predicados distintos. La decisión del experto no valida retroactivamente una salida inadmisible; una salida gobernada tampoco sustituye a la decisión clínica humana.

El orden de sucesos será constitutivo. Una marca temporal externa podrá registrarse como metadato de terceros, pero no se convertirá por ello en primitiva interna.

## 7. Estatuto de los activos existentes

### 7.1. IMMUNO-1 e IMMUNO-2

Se conservan como cáscarones o semillas históricas. No agotan, deciden ni delimitan el dominio completo. Podrán utilizarse posteriormente como casos de prueba de cobertura o composición, nunca como fuente soberana del dominio.

### 7.2. Universo candidato de parámetros v0.2

Contiene 64 filas propuestas:

- 38 declaradas críticas;
- 24 declaradas condicionalmente críticas;
- 2 declaradas no críticas;
- 51 con estado empírico “no buscado”;
- 8 con estado “no encontrado”;
- 5 con estado “inaccesible”;
- 64 con confianza baja y sin adopción.

La columna `knowledge_or_skill` contiene principalmente advertencias, distinciones y relaciones abreviadas. No constituye todavía un catálogo formal de conocimientos y habilidades.

**Estatuto:** material candidato en cuarentena. Ninguna fila se elimina y ninguna fila se adopta.

### 7.3. Entidades tipificadas v0.2

Contiene 27 filas propuestas y mezcla clases ontológicas diferentes: entidades, síndromes, estados iatrogénicos, complicaciones, categorías diagnósticas y una frontera institucional.

**Estatuto:** inventario exploratorio pendiente de separación por tipo.

### 7.4. Relación parámetro-entidad v0.2

Contiene 50 relaciones. Todas están declaradas como propuestas no graduadas, pendientes y sin contraste adoptado con microdatos.

**Estatuto:** hipótesis de enlace no operativas.

### 7.5. Matriz de cobertura de repositorios v0.2

Contiene 40 cruces candidatos. Ninguno dispone todavía de número efectivo de registros verificado y la mayoría no tiene comprobación variable a variable, método, unidad, anclaje, desenlace o medicación concomitante.

**Estatuto:** mapa de búsqueda, no prueba empírica.

### 7.6. Flujo v3, registro D0 y bisturí v0.4

Se conservan como antecedentes de proceso. No gobiernan el rumbo corregido cuando contradigan:

- la restricción canónica `n = b²`;
- la semántica de U;
- la separación entre catálogo clínico, episodio y proyección formal;
- la separación entre salida predecisional y decisión humana;
- o la exigencia de operandos constituidos antes de presentar un algoritmo como evaluable.

## 8. Estados y transiciones permitidos

Cada objeto tendrá un estado explícito. Las transiciones no sobrescribirán el estado anterior.

| Estado | Significado |
|---|---|
| Identificado | Nombrado en una fuente o en el trabajo exploratorio |
| Extraído | Registrado literalmente con localizador |
| Tipado | Clase de objeto determinada sin conflicto |
| Contrastado | Comparado con fuentes independientes pertinentes |
| Disputado | Existe conflicto material no resuelto |
| Verificado | La afirmación y su fuente han superado revisión |
| Empíricamente mapeado | Existe correspondencia variable a variable con datos reales |
| Adoptado | Decisión expresa del Director tras revisión competente |
| Sustituido | Existe una versión posterior; la anterior permanece trazable |
| Rechazado | No se incorpora; se conserva el motivo |
| Residual | No puede cerrarse todavía sin inventar o exceder el perímetro |

No evaluado no significa falso, inexistente ni no aplicable.

## 9. Puertas de paso

### G0. Perímetro profesional

Pasa únicamente si están declaradas autoridad, jurisdicción, función y versión.

### G1. Capacidad y operación

Pasa únicamente si la capacidad se ha descompuesto en operaciones verificables, con responsabilidad y nivel de autonomía.

### G2. Conocimiento y habilidad

Pasa únicamente si cada operación dispone de conocimientos y habilidades explícitos, no de rótulos temáticos.

### G3. Consecuencia

Pasa únicamente si ignorancia, omisión, error y composición indebida tienen consecuencias condicionadas, graduadas y trazables. La ausencia de consecuencia demostrable no autoriza a inventarla.

### G4. Parámetros

Pasa únicamente si los parámetros son mínimos, semánticamente completos y necesarios para operaciones ya constituidas.

### G5. Evidencia empírica

Pasa únicamente si existe correspondencia real entre operación, parámetro, variable, población y desenlace. Puede declarar cobertura parcial o residual.

### G6. Representación y composición

Pasa únicamente si la forma respeta los invariantes doctrinales y cada composición tiene relación tipada y consecuencias de orden.

### G7. Revisión clínica y adopción

Pasa únicamente tras revisión por profesionales competentes y decisión expresa del Director. La IA no adopta.

### G8. Caso testigo

Antes de presentar un mecanismo integrado deberá existir, al menos:

- una operación concreta;
- un episodio sintético no asistencial;
- una versión finita de conocimiento;
- una interfaz tipada;
- una consecuencia sellada *ex ante*;
- una salida o abstención reproducible;
- y una decisión humana registrada después, sin retroacción.

Sin testigo finito no se declarará un algoritmo ejecutable ni un sistema clínicamente evaluado.

## 10. Adversarial de cierre del método

### 10.1. Sanitaria, clínica y médica

**Ataque:** usar un programa formativo como estándar clínico vigente y suficiente.  
**Defensa:** el programa delimita competencias; cada operación y consecuencia exige fuente clínica vigente.

**Ataque:** aplicar una competencia de otra jurisdicción como universal.  
**Defensa:** jurisdicción y función son campos obligatorios; las diferencias quedan como conflicto o residual.

**Ataque:** declarar catastrófica cualquier ausencia.  
**Defensa:** la consecuencia debe estar condicionada, graduada y ser relativa a una operación. Sin consecuencia aplicable no se propaga una alarma.

**Ataque:** omitir laboratorio, calidad o interpretación para centrarse solo en enfermedades.  
**Defensa:** el dominio comprende conocimiento básico, laboratorio, clínica, terapias, prevención, calidad, comunicación e investigación, conforme a los perímetros profesionales.

**Resultado:** apto como método; no apto todavía como dominio clínico constituido.

### 10.2. Ingeniería de procesos

**Ataque:** convertir una hoja candidata en fuente maestra.  
**Defensa:** las hojas existentes permanecen en cuarentena y solo pueden alimentar el registro de objetos identificados.

**Ataque:** reparar conflictos sobrescribiendo filas.  
**Defensa:** toda corrección produce un nuevo suceso y conserva el antecedente.

**Ataque:** cerrar primero la teoría y buscar después datos que la confirmen.  
**Defensa:** la ruta de datos avanza en paralelo desde la definición de cada operación.

**Ataque:** presentar un algoritmo sin catálogos constituidos.  
**Defensa:** G8 exige un testigo finito con operandos reales y consecuencias selladas.

**Resultado:** apto como proceso de constitución; no autoriza implementación.

### 10.3. Lógica enlazada

**Ataque:** confundir conocimiento no constituido con dato ausente.  
**Defensa:** son objetos y fallos distintos, con respuestas diferentes.

**Ataque:** convertir una consecuencia en explicación retrospectiva.  
**Defensa:** la consecuencia debe existir antes de la salida y formar parte de la cadena auditada.

**Ataque:** hacer depender la admisibilidad de la salida de la decisión posterior del experto.  
**Defensa:** ambos sucesos y predicados permanecen separados.

**Ataque:** imponer un único operador o un orden temático a todas las composiciones.  
**Defensa:** la relación clínica, la interfaz y las consecuencias del orden preceden a la selección formal.

**Ataque:** usar U como cierre cómodo o propagarla universalmente.  
**Defensa:** U solo aparece donde no existe clausura legítima y afecta únicamente a las operaciones y dependencias tipadas pertinentes.

**Resultado:** apto como arquitectura lógica de trabajo; no constituye por sí solo una semántica clínica.

## 11. Próxima operación autorizable

El siguiente trabajo debe ser la extracción literal y trazable del corpus profesional en un registro no adoptivo. El orden será:

1. programa oficial español de Inmunología: núcleo común y función médica;
2. programa oficial español de Alergología: solapamientos y fronteras;
3. currículo británico ACLI: capacidades clínicas, terapéuticas, de enlace y laboratorio;
4. currículo austral: separación entre ser, hacer y saber, operaciones profesionales y guías de conocimiento;
5. marco canadiense: progresión de responsabilidad y competencia;
6. contraste posterior con certificaciones y clasificaciones internacionales pertinentes.

La extracción conservará el enunciado, localizador, función, jurisdicción, versión y tipo de objeto. No armonizará, no priorizará y no generará parámetros. Las discrepancias se entregarán al Director para decisión.

## 12. Criterio de cierre de esta acta

La rectificación queda metodológicamente cerrada si se acepta que:

1. el dominio no nace de IMMUNO-1, IMMUNO-2 ni de los 64 candidatos;
2. el dominio nace de capacidades y operaciones profesionalmente autorizadas;
3. el conocimiento y las habilidades se tipan antes que los parámetros;
4. las consecuencias se constituyen *ex ante* y no como relato retrospectivo;
5. la evidencia empírica avanza en paralelo, no como confirmación final decorativa;
6. la representación matricial y la composición son posteriores y subordinadas;
7. la IA no aprende ni infiere durante el episodio;
8. la decisión clínica sigue perteneciendo al experto humano;
9. toda la cadena es *append-only*;
10. ningún cierre futuro puede violar los documentos doctrinales inviolables.

## Fuentes de delimitación

### Doctrina vinculante

1. Lloret Egea, Juan Antonio. **Fundamentos algebraico-semánticos del Sistema Vectorial SV**. ITVIA, versión fundacional de referencia.
2. Lloret Egea, Juan Antonio. **Origen doctrinal, definición y alcance de la U en el Sistema Vectorial SV**. ITVIA, especificación transversal subordinada.

### Fuentes oficiales del perímetro profesional utilizadas en esta rectificación

1. España. Orden SCO/3255/2006, de 2 de octubre, por la que se aprueba y publica el programa formativo de la especialidad de Inmunología. Boletín Oficial del Estado. https://www.boe.es/buscar/doc.php?id=BOE-A-2006-18430
2. España. Orden SCO/3081/2006, de 20 de septiembre, por la que se aprueba y publica el programa formativo de la especialidad de Alergología. Boletín Oficial del Estado. https://www.boe.es/diario_boe/txt.php?id=BOE-A-2006-17620
3. Joint Royal Colleges of Physicians Training Board. **Allergy, Clinical and Laboratory Immunology 2021 Curriculum**. https://www.thefederation.uk/sites/default/files/Immunology%2520%2528Allergy%2520Clinical%2520and%2520Laboratory%2520%2520Immunology%2529%25202021%2520curriculum%2520FINAL.pdf
4. Royal Australasian College of Physicians. **Advanced Training Curriculum Standards: Immunology and Allergy**. https://elearning.racp.edu.au/pluginfile.php/112488/mod_resource/content/7/immunology-and-allergy-curriculum-standards.pdf
5. Royal College of Physicians and Surgeons of Canada. **Pathway to Competence in Clinical Immunology and Allergy**, versión 1.0, aplicable desde el 1 de julio de 2021. https://www.royalcollege.ca/content/dam/documents/ibd/clinical-immunology-and-allergy/pathway-to-competence-clinical-immunology-and-allergy-e.pdf

---

**Fin del documento.**  
**Estatuto de cierre:** candidata interna. Requiere decisión expresa del Director. No constituye el dominio, no adopta parámetros y no autoriza uso asistencial.
