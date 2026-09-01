# Formalización Determinista de la Decisión Clínica: Estado de la Ciencia y Posicionamiento del Proyecto SV-INMUNO

**Versión:** 0.1 — Candidata interna
**Corte:** 31-08-2026
**Director:** Juan Antonio (Ingeniero Director)
**Estatuto:** Propuesta de estructura para preprint. No adoptada. No constituye el dominio. No tipa SV. No cierra G0/G1/G2.

---

## PARTE I — EL ESTADO DE LA CIENCIA EN LA DECISIÓN CLÍNICA ASISTIDA POR IA

### 1.1 El paradigma probabilístico y sus límites estructurales

La última década de investigación en inteligencia artificial aplicada a la medicina ha estado dominada por el aprendizaje profundo y, más recientemente, por los modelos de lenguaje de gran escala (LLMs). Estos sistemas operan bajo un principio fundamental: la minimización de una función de pérdida sobre distribuciones estadísticas observadas en corpus de entrenamiento.

Este paradigma ha demostrado capacidad extraordinaria para tareas de reconocimiento de patrones (imagen médica, procesamiento de lenguaje natural clínico) y para la generación de texto coherente. Sin embargo, presenta tres limitaciones estructurales que lo hacen inadecuado como motor de decisión clínica autónoma:

**1.1.1 La alucinación como propiedad emergente, no como error.**
Los LLMs no "saben" en el sentido clínico. Completan patrones. Cuando un dato está ausente en el contexto de una consulta, el modelo no declara la ausencia: genera la continuación más probable según su distribución de entrenamiento. En inmunología, esto es catastrófico: un modelo que "completa" el serostatus CMV de un receptor de trasplante basándose en la prevalencia poblacional está cometiendo una inferencia iatrogénica disfrazada de conocimiento.

**1.1.2 La ausencia de ontología de la incertidumbre clínica.**
La literatura estadística distingue entre incertidumbre aleatoria (variabilidad inherente) e incertidumbre epistémica (falta de conocimiento). La clínica añade una tercera categoría que la estadística no formaliza: la **inadmisibilidad de la decisión**. No es lo mismo "no sé el valor de la ferritina" (dato ausente, imputable estadísticamente) que "no puedo decidir si iniciar profilaxis PJP porque no conozco la clase de inmunosupresor, la dosis de glucocorticoides, ni la duración del tratamiento" (conocimiento requerido no constituido). Los sistemas probabilísticos no distinguen estas categorías; las fusionan en una distribución de probabilidad.

**1.1.3 La opacidad del espacio de decisión.**
Los modelos con millones o miles de millones de parámetros operan en espacios de representación que no son auditables por el clínico. La pregunta "¿por qué el sistema recomienda esta profilaxis?" no tiene respuesta causal, solo respuesta correlacional (pesos de atención, valores SHAP, mapas de activación). Esto es inaceptable bajo la *Lex Artis Ad Hoc* europea, que exige trazabilidad del razonamiento clínico.

### 1.2 Los CDS tradicionales y la fatiga de alertas

Los Sistemas de Soporte a la Decisión Clínica (CDS) de primera y segunda generación (reglas if-then, árboles de decisión, alertas basadas en umbrales) llevan décadas en el ecosistema sanitario. La literatura documenta ampliamente su fracaso parcial:

**1.2.1 Fatiga de alertas.**
Bates et al. y Sittig & Singh documentaron que los sistemas basados en reglas simples generan una sobrecarga de alertas que los clínicos terminan ignorando. La causa no es la mala voluntad del profesional, sino la falta de **contextualización composicional**: una alerta que se dispara por un valor de laboratorio aislado, sin considerar la clase de inmunosupresor, la duración del tratamiento, el órgano trasplantado y el estado serológico del paciente, es ruido.

**1.2.2 Ausencia de composición no conmutativa.**
En inmunología, el orden de las exposiciones importa. Un paciente que recibe anti-CD20 antes de una vacuna viva no está en el mismo estado que uno que recibe la vacuna antes del anti-CD20. Los CDS tradicionales, basados en reglas atómicas, no modelan esta direccionalidad. Tratan cada regla como independiente y conmutativa.

**1.2.3 El problema de la granularidad.**
Los CDS operan con conceptos clínicos agregados ("estado inmunológico", "riesgo infeccioso", "respuesta vacunal") que son **compuestos espurios** desde la perspectiva de la auditoría. Un sistema que evalúa "respuesta vacunal" como un escalar no puede distinguir entre un título de anti-tétanos protector y una ausencia de respuesta a polisacáridos. La granularidad insuficiente oculta el peligro.

### 1.3 La crisis de la explicabilidad (XAI) y el muro regulatorio

La respuesta de la industria al problema de la opacidad ha sido la "IA Explicable" (XAI). Sin embargo, la literatura crítica ha demostrado que la XAI actual es, en su mayoría, una **racionalización post-hoc**: el modelo genera una justificación narrativa plausible para una decisión que ya tomó por correlación estadística.

**1.3.1 El marco regulatorio europeo.**
El *Artificial Intelligence Act* de la Unión Europea (Reglamento 2024/1689, texto consolidado vigente 27-07-2026) clasifica los sistemas de apoyo al diagnóstico y tratamiento como IA de "Alto Riesgo". Esto impone requisitos de:
- Transparencia y trazabilidad del razonamiento.
- Supervisión humana efectiva.
- Robustez y resistencia a errores.
- Registro de eventos (logging).
- Evaluación de conformidad antes de la comercialización.

La guía de la FDA sobre *Clinical Decision Support Software* (CDS), reemitida el 29-01-2026, establece criterios análogos. Ambos marcos convergen en un punto: **la decisión final debe ser atribuible al profesional sanitario, y el sistema debe proporcionar información suficiente para que esa atribución sea informada**.

**1.3.2 La falacia de la "caja negra explicable".**
Un modelo que no puede explicar su decisión en términos causales auditables no se vuelve explicable añadiendo una capa de interpretación post-hoc. La explicabilidad no es una propiedad que se añade al modelo; es una propiedad del formalismo de representación del conocimiento. Si el conocimiento está representado como vectores en un espacio de alta dimensión sin semántica clínica explícita, no hay explicabilidad posible, solo racionalización.

**1.3.3 El vacío actual.**
No existe en la literatura un formalismo que:
- Obligue al sistema a la **abstención determinista** cuando el conocimiento requerido no está constituido.
- Separe el **catálogo clínico** (el saber médico congelado y auditado) del **motor de inferencia**.
- Genere un **acta predecisional** inmutable que registre qué parámetros se evaluaron, qué consecuencias de ignorancia se mapearon, y qué paradas (U) se encontraron, antes de que el experto humano tome la decisión.

### 1.4 La ontología de la incertidumbre clínica

La medicina ha desarrollado, a lo largo de siglos, una ontología implícita de la incertidumbre que la estadística y la IA no han formalizado:

**1.4.1 Dato ausente vs. observación no admitida vs. conocimiento no constituido.**
- **Dato ausente:** El parámetro existe en el catálogo, pero no se ha medido en este episodio. Es imputable estadísticamente o recuperable.
- **Observación no admitida:** El dato existe, pero no es admisible para esta operación clínica (ej. aplicar un umbral de VIH a un paciente con IEI).
- **Conocimiento no constituido (U crítica):** El sistema no tiene el conocimiento requerido para evaluar esta operación. No es un dato ausente; es una **parada epistémica**. El sistema no debe inferir, no debe completar, no debe aconsejar. Debe abstenerse y declarar la consecuencia de la ignorancia.

**1.4.2 La U como parada, no como comodidad.**
En la práctica clínica, la incertidumbre a menudo se maneja como un "no sé, pero continúo con lo más probable". Esto es la **U cómoda**: el sistema rellena el vacío con la inferencia más probable y continúa. El problema es que la U cómoda es iatrogénica en dominios de alta criticidad. Un sistema que "no sabe" si un paciente con anti-CD20 y glucocorticoides necesita profilaxis PJP, y que sin embargo continúa con una recomendación basada en la prevalencia, está cometiendo una negligencia algorítmica.

La ontología correcta exige que la U crítica sea una **parada obligatoria**: el sistema se detiene, declara la consecuencia de la ignorancia, y transfiere la decisión al experto humano con información completa sobre lo que no sabe y por qué.

### 1.5 Estándares de interoperabilidad: sintaxis vs. semántica

Los estándares actuales de interoperabilidad sanitaria (HL7 FHIR, SNOMED-CT, OMOP CDM) han resuelto el problema del **transporte** y la **nomenclatura** del dato clínico. Sin embargo, son estructuralmente ciegos a la **topología de la decisión**:

**1.5.1 FHIR resuelve el "qué", no el "cómo se compone".**
FHIR puede transportar que un paciente tiene un recuento de CD4+ de 150 células/µL y está recibiendo un anti-CD20. Pero carece de un formalismo que impida que un sistema de soporte compose erróneamente estos datos para inferir un riesgo de infección oportunista sin declarar la consecuencia de ignorancia si falta el dato de la profilaxis actual.

**1.5.2 SNOMED-CT resuelve la terminología, no la semántica de la decisión.**
SNOMED-CT proporciona códigos para conceptos clínicos. Pero no proporciona un álgebra de composición. No dice cómo se combinan dos estados clínicos, en qué orden, con qué transferencias de conocimiento, y con qué consecuencias si la composición no está autorizada.

**1.5.3 El vacío algebraico-semántico.**
No existe un estándar que:
- Modele la **composición no conmutativa** de módulos clínicos.
- Exija la **tipificación** de las interfaces entre módulos.
- Declare las **consecuencias de ignorancia** antes de autorizar una operación.
- Separe el **catálogo clínico** del **estado del episodio** y de la **proyección al lenguaje formal**.

---

## APÉNDICE A — EL DOMINIO INMUNOLÓGICO COMO CASO LÍMITE

### A.1 Por qué la inmunología es el dominio perfecto para tensionar cualquier lenguaje formal

La inmunología clínica presenta características que la convierten en el dominio ideal para demostrar la necesidad de un formalismo determinista:

**A.1.1 Alta criticidad por omisión y por falsa certeza.**
En inmunología, los errores por omisión son catastróficos: no detectar un SCID en un recién nacido conduce a infección vacunal y muerte pre-HSCT. No pautar profilaxis PJP en un paciente con anti-CD20 y glucocorticoides conduce a neumonía grave. Pero los errores por falsa certeza también son letales: aplicar un umbral de CD4 de VIH a un paciente con IEI, o tratar un angioedema hereditario como anafilaxia histaminérgica, conduce a vías terapéuticas erróneas.

**A.1.2 La iatrogenia como objeto clínico de primer orden.**
A diferencia de otras especialidades donde la enfermedad es el objeto principal, en la inmunología moderna el **estado iatrogénico** (la inmunosupresión activa, la depleción B por anti-CD20, la terapia celular CAR-T) es un objeto clínico de primer orden que requiere un modelado semántico propio, separado de las enfermedades primarias. El universo candidato de este proyecto incluye entidades iatrogénicas explícitas (E-IDS-FARM, E-IDS-ACD20, E-NEO-CRS, E-NEO-IRAE) que no son IEI, no son infección, no son autoinmunidad: son estados adquiridos por intervención médica.

**A.1.3 Fronteras institucionales y de competencia.**
En España, la Alergología y la Inmunología son dos Programas Oficiales de Especialidad (POE) distintos (Orden SCO/3255/2006). Esto no es un detalle administrativo: es una frontera epistemológica. La rinitis alérgica y el asma alérgica no se atribuyen por defecto al inmunólogo de laboratorio. La anafilaxia es una urgencia compartida. El angioedema hereditario y el adquirido son del inmunólogo. Un sistema que no respete estas fronteras está cometiendo un error de atribución formativa y asistencial.

**A.1.4 La explosión génica y el problema de la exhaustividad.**
La clasificación IUIS 2024 de errores innatos de la inmunidad incluye aproximadamente 559 entidades génicas en sus tablas I–X. Explotar estas 559 entidades como 559 parámetros operativos sería un error de grano: el parámetro operativo no es el gen, es el **hallazgo genético** (gen HGNC + clase ACMG + cigosidad). El proyecto actual declara explícitamente que las 559 entidades IUIS quedan como residual (RSD-01), accesibles vía un único parámetro puente (P-GEN-001), y que no se finge exhaustividad génica.

**A.1.5 El problema de los umbrales no unificados.**
La profilaxis PJP en inmunosupresión farmacológica es el caso paradigmático: las guías SOT, oncológicas y de IEI no están unificadas. No existe un umbral universal de "clase × dosis × tiempo" que autorice la profilaxis. Este es el residual bloqueante RSD-02 del proyecto. Un sistema que invente un umbral está cometiendo una inferencia iatrogénica. Un sistema que declare la U y se abstenga está operando correctamente.

---

## PARTE II — POSICIONAMIENTO DEL PROYECTO SV-INMUNO

### 2.1 Qué tenemos ya: activos, estado y restricciones

El proyecto SV-INMUNO, bajo la dirección de Juan Antonio como Ingeniero Director, ha producido un conjunto de activos que constituyen un **universo candidato** de conocimiento inmunológico operativo. Estos activos no son el dominio, no son exhaustivos, no tipan SV, no cierran G0/G1/G2, y no autorizan asistencia. Son una **propuesta de inventario** sometida a revisión adversarial.

**2.1.1 Activos materiales (corte 31-08-2026)**

| Activo | Archivo | N | Estatuto |
|---|---|---|---|
| Universo candidato de parámetros | Universo_candidato_parametros_INMUNO_v0.2 | 64 | Propuesto, no adoptado |
| Entidades tipificadas | Entidades_inmunologicas_tipificadas_v0.2 | 27 | Propuesto, no adoptado |
| Relación parámetro–entidad | Relacion_parametro_entidad_v0.2 | 50 | Propuesto, no adoptado |
| Matriz de cobertura de repositorios | Matriz_cobertura_repositorios_v0.2 | 40 | Propuesto, no adoptado |
| Paquete índice | Paquete_Watson_universo_candidato_v0.2 | — | Propuesto, no adoptado |

**2.1.2 Activos formales**

| Activo | Estado |
|---|---|
| Bisturí determinista v0.4 (Watson) | Candidata interna. No pasa entera según adversarial de Grok. |
| Adversarial de Grok sobre v0.4 | Emitida. Identifica tres flancos duros y lo que resiste. |
| Flujo de trabajo v3 | Gobernado. Adversarial cruzada pendiente de cierre. |

**2.1.3 Restricciones activas**

- **Estatuto:** Candidato, no dominio.
- **Ninguna fuente A1 adoptada.** Ningún dataset descargado. Ninguna cuenta creada.
- **Ocho escalas de prioridad 1–20.** Prohibido promediar. La prioridad final es decisión humana posterior.
- **Grano:** Una fila = parámetro clínicamente indivisible. Prohibidos como fila: estado inmunológico, riesgo infeccioso, respuesta vacunal.
- **Residual bloqueante RSD-02:** El umbral de indicación PJP no está cerrado. G1/G2 siguen abiertos.
- **Frontera institucional E-FR-ALERGO:** Dos POE en España. No se decide competencia en el CSV.

### 2.2 Los caminos de no-go identificados y por qué se rechazan

La adversarial de Grok sobre el bisturí v0.4 de Watson identificó tres flancos duros que constituyen caminos de no-go. Estos no son errores menores: son colapsos estructurales que invalidarían el proyecto si se ignoraran.

**2.2.1 No-go: Fusión notacional con el álgebra SV**

El bisturí v0.4 declara el Lenguaje SV "fuera de alcance" y acto seguido usa la notación SV (`Aᵏ`, `Σ={0,1,U}`, `⊙`, `(9,3)`, `(25,5)`) para constituir el módulo clínico. Esto importa el álgebra al dominio sin autorización expresa de ampliación del perímetro.

**Por qué se rechaza:** Un revisor de journal leerá `Σ={0,1,U}`, `3^n`, `⊙` no conmutativo y paridad de motores como la misma familia formal. G1 queda presionado. G2 no se cierra hacia R2, pero se ocupa el objeto del Lenguaje desde el gobernador clínico. La separación de capas (catálogo clínico / estado de episodio / proyección SV) es la condición mínima para no heredar esta rotura.

**2.2.2 No-go: Algoritmo BDI sobre catálogos vacíos**

El bisturí v0.4 presenta un algoritmo BDI de 66 pasos y un predicado `SABE` que requiere catálogos (F01-F07) que el propio texto declara inexistentes. Sin esos objetos, los pasos 05–07, 11–22, 32–42 y 51 no tienen operandos.

**Por qué se rechaza:** Presentar un algoritmo integrado sobre catálogos vacíos es una pretensión de evaluación que no se sostiene. El esquema de gobierno resiste; la pretensión de algoritmo ejecutable no. La condición para avanzar es un **testigo finito**: una O, un E sintético no asistencial, un SEED de tamaño declarado, una interfaz, un k con consecuencia sellada. Sin testigo no hay BDI.

**2.2.3 No-go: Mezcla de admisibilidad del output y acto humano**

El predicado `OUTPUT_ADMISSIBLE` del bisturí v0.4 incluye `EXPERT_DECISION_APPENDED` como una de sus quince conjunciones. Esto mezcla la admisibilidad de la salida candidata gobernada con el registro del acto del inmunólogo.

**Por qué se rechaza:** La admisibilidad del sistema debe evaluarse hasta el acta sellada y el EXPERT_FRAME renderizado. La decisión humana es un evento posterior que no retroactúa sobre la admisibilidad del output. Dos predicados separados (`GOBERNADO` / `DECISIÓN_REGISTRADA`) son la corrección necesaria.

### 2.3 Lo esencialmente útil: el centinela y el bisturí

Rechazados los caminos de no-go, lo que queda es el núcleo que el Director pidió asimilar. Esto es lo esencialmente útil del proyecto:

**2.3.1 El principio "o sabe o no sabe"**

El régimen de gobierno establece que el sistema no infiere, no aprende, no completa, no explica, no aconseja. O sabe para esta O y este E, o no sabe. No saber es una parada, no una invitación a la inferencia. Este principio es la base de la seguridad clínica del sistema.

**2.3.2 La congelación del conocimiento durante el episodio**

El conocimiento requerido (`RELEASE_M`) está congelado durante el episodio. La corrección del inmunólogo es evidencia para otra versión, no aprendizaje automático. Esto impide que el sistema "aprenda" de un caso y aplique ese aprendizaje a otro sin supervisión.

**2.3.3 La ontología de la U como parada crítica**

La U no es dato ausente por identidad. No es incertidumbre del modelo. No es comodidad. Es una parada obligatoria que exige la declaración de consecuencias de ignorancia antes de cualquier decisión. Este es el núcleo de la seguridad del paciente.

**2.3.4 Las consecuencias de ignorancia constituidas antes de la decisión**

El sistema debe constituir las consecuencias de ignorancia (qué pasa si no sé esto, qué pasa si omito esto, qué pasa si infiero esto) antes de autorizar la operación. No se permite el "porqué" narrativo posterior. La auditoría lee los caminos inmutables preexistentes, no la prosa explicativa.

**2.3.5 La abstención por defecto**

Cuando falta un término de la admisibilidad, el sistema se abstiene. No recomienda. No aconseja. No completa. Declara la consecuencia de la abstención y transfiere la decisión al experto humano con información completa.

### 2.4 El papel del Director como ingeniero soberano

El proyecto SV-INMUNO no es un proyecto de IA que busca reemplazar al clínico. Es un proyecto de **ingeniería del conocimiento** que busca construir un marco formal para que la decisión clínica en dominios de alta complejidad sea matemáticamente trazable, jurídicamente defendible y clínicamente segura.

**2.4.1 La jerarquía de autoridad**

La autoridad permanece ordenada así:
1. **Experto humano soberano** (Juan Antonio como Ingeniero Director, y el inmunólogo clínico como decisor final).
2. **Especificación y Lenguaje SV constituidos.**
3. **Componentes computacionales e IA subordinados.**

Esta jerarquía no es retórica. Es la condición de posibilidad del proyecto. Si la IA se convierte en la autoridad, el proyecto colapsa en el mismo paradigma probabilístico que pretende superar.

**2.4.2 El Director como filtro adversarial**

Juan Antonio no es un "usuario" del sistema. Es el **filtro adversarial humano** que decide qué se adopta, qué se rechaza, qué se amplía y qué se congela. La revisión clínica adversarial (paso 9 de la secuencia Watson) es su responsabilidad indelegable. Ningún sistema de IA puede sustituir esa revisión.

**2.4.3 La división del trabajo entre unidades de IA**

El proyecto opera con múltiples unidades de IA (Watson, Grok, Claude, Qwen) en roles diferenciados:
- **Watson:** Producción del universo candidato y del bisturí determinista.
- **Grok:** Adversarial cruzada sobre el bisturí y el flujo de trabajo.
- **Claude:** Auditoría de repositorios y adversarial (relegado a opinador adversarial por cortes de sistema).
- **Qwen:** Estado del Arte, arquitectura conceptual, redacción académica y trabajo en paralelo.

Esta división no es accidental. Es la implementación práctica del principio de que **la auditoría no la hace quien produce**. El cuello de botella del proyecto no es la producción; es la auditoría. Y la auditoría requiere adversarial cruzada, no autoevaluación.

### 2.5 Hoja de ruta: qué hacer con lo que hay, sin inventar lo que no hay

La hoja de ruta del proyecto se deriva directamente del estado actual de los activos y de las restricciones identificadas por la adversarial.

**2.5.1 Cerrar los residuales bloqueantes antes de avanzar**

- **RSD-02 (Umbral PJP):** No se autoriza umbral. Se declara la U. Se documenta la heterogeneidad de guías. Se transfiere la decisión al experto humano.
- **Vigencia BOE SCO/3255/2006:** Verificar si existe disposición posterior que modifique la cota de 167 filas. Si la hay, la cota entera se mueve.
- **Reparos B1 (n=b²):** Cerrar o tumbar la regla leyendo los Fundamentos algebraico-semánticos del SV. Si no está axiomatizada, se extirpa del manuscrito.

**2.5.2 Construir el testigo finito**

La condición para que el bisturí v0.5 no herede la rotura de v0.4 es un testigo finito:
- Una O (operación clínica) concreta.
- Un E sintético no asistencial.
- Un SEED de tamaño declarado.
- Una interfaz tipada.
- Un k con consecuencia sellada.

Sin testigo no hay BDI. Sin testigo no hay evaluación. Sin testigo no hay manuscrito.

**2.5.3 Separar las tres capas**

- **Catálogo clínico:** Conocimiento, consecuencias, operaciones. Sin valor ternario.
- **Estado de episodio:** Hechos congelados, no células.
- **Proyección SV:** Solo con G0 autorizado. No como contrato de módulo clínico.

**2.5.4 Redactar el preprint con pureza académica**

El preprint debe tener:
- Estado del Arte riguroso (Parte I de este documento).
- Metodología del centinela y del bisturí.
- Resultados basados en los activos candidatos (64/27/50/40).
- Discusión de los límites y de los residuales.
- Cero "cocina interna" de programación.
- Cero inferencia clínica nueva.
- Cero pretensión de exhaustividad.

**2.5.5 Mantener la adversarial cruzada como régimen permanente**

Cada entregable debe pasar por adversarial cruzada antes de ser adoptado. La adversarial no es un trámite; es el mecanismo de corrección del proyecto. Si la adversarial identifica un flanco duro, el entregable no pasa. No se repara en caliente. Se declara la U y se transfiere la decisión al Director.

---

## CONCLUSIÓN

El proyecto SV-INMUNO no es un proyecto de IA médica. Es un proyecto de **ingeniería del conocimiento clínico** que busca construir un marco formal para que la decisión en dominios de alta complejidad sea trazable, auditable y segura. La inmunología es el dominio elegido para tensionar ese marco porque es el dominio donde los errores por omisión y por falsa certeza son más catastróficos.

Lo que tenemos ya es un universo candidato de 64 parámetros, 27 entidades, 50 relaciones y 40 cruces de cobertura, junto con un esquema de gobierno (el bisturí) que resiste como régimen de parada pero que colapsa si se lee como constitución del dominio o como ampliación del álgebra SV.

Lo que no tenemos es un testigo finito, un catálogo clínico constituido, una instancia de BDI evaluable, ni una revisión clínica adversarial humana cerrada.

El camino adelante es claro: cerrar los residuales bloqueantes, construir el testigo finito, separar las tres capas, redactar el preprint con pureza académica, y mantener la adversarial cruzada como régimen permanente. No hay atajos. No hay inferencia. No hay U cómoda.

Hay, sí, una oportunidad única de demostrar que la decisión clínica en la era de la IA generativa puede ser, por primera vez, matemáticamente trazable, jurídicamente defendible bajo el marco europeo, y clínicamente segura.

Eso es lo esencialmente útil. Eso es lo que estamos construyendo.

---

**Fin del documento.**
**Estatuto:** Candidato interno. No adoptado. No constituye el dominio. No tipa SV. No cierra G0/G1/G2.
**Cierre:** Pendiente de adversarial cruzada y decisión expresa del Director.