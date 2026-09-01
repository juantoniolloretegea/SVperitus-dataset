# Adversarial Watson de la entrega v3 y avance paralelo del perímetro inmunológico

**Corte:** 31 de agosto de 2026  
**Versión:** 0.1  
**Estatuto:** documento interno de control; no adopta ontología, fuente, parámetro, entidad, regla clínica ni cambio técnico.  
**Ámbito:** exclusivamente el flujo HTML v3 y el registro D0 v0.1. R2, IR, semántica e implementación del Lenguaje quedan fuera de alcance.

---

## 1. Entradas auditadas

| Entrada | SHA-256 |
|---|---|
| `flujo-gobernado-dominio-inmunologia-v3.html` | `b55faad4b900c6a01966c1588b4abeba3e7d1505a7fd5231b1338ab31d4bd23e` |
| `registro-d0-cobertura-dominio-inmunologia-2026-08-31-v0.1.md` | `3412cd3d35d0018b47f122caa54fe23226504d73f47c15c7efc3dbd4772fdce5` |

No se ha modificado ninguna de las dos entradas durante esta revisión.

## 2. Dictamen

> **NO PASA todavía como arquitectura rectora.**

El flujo v3 contiene mejoras materiales frente a v2 y puede conservarse como prototipo de inspección. Sin embargo, existe una contradicción bloqueante entre su tesis —tres carriles independientes— y su topología ejecutada —un único recorrido vertical que hace pasar la búsqueda de datos antes de constituir el corpus clínico—. Además, el registro D0 audita capas de evidencia, pero su título puede hacer creer que ya audita la cobertura del dominio clínico.

El trabajo puede continuar en paralelo en tareas no dependientes de esa topología. La clausura de v3 exige una nueva adversarial externa, al menos de Grok, y decisión expresa del director.

## 3. Hallazgos priorizados

| ID | Severidad | Hallazgo verificable | Consecuencia | Corrección propuesta, no adoptada |
|---|---|---|---|---|
| B01 | Bloqueante | El HTML declara carriles C, E y F, pero después los reduce a una cadena `1 → 2/D0 → 3 → 4 → 5 → 6 → 7`. El corpus clínico de autoridad aparece después de inventariar repositorios y superar D0. | Los datos disponibles pueden condicionar prematuramente qué conocimiento profesional se inventaría; contradice el residual profesional y la independencia de carriles. | Representar tres subflujos realmente paralelos. C y E nacen tras la autorización; se cruzan sólo en una puerta de correspondencia. F no comienza a representar hasta que exista entrada autorizada desde C/E. |
| B02 | Bloqueante | E01–E15 son modalidades o capas de evidencia, no una taxonomía clínica. El registro se titula «cobertura del dominio» aunque reconoce que no existe correspondencia completa. | Puede confundirse disponibilidad de tipos de dato con cobertura de inmunología. | Renombrar el objeto como «registro D0 de fuentes y estratos de evidencia» y añadir una tabla independiente de perímetros clínicos. |
| B03 | Bloqueante de gobierno | La sección 2.1 del registro afirma «reparos convergentes adoptados» y dice que se sustituyó el camino único, cuando la sustitución no se materializó y no consta cierre directorial de v3. | Convierte una propuesta de la unidad de IA en decisión y registra como cumplido un cambio incompleto. | Usar «implementados provisionalmente para contraste; pendientes de aceptación» y registrar por separado proponente, decisor, fecha y resolución. |
| M01 | Mayor | Las 30 entradas mezclan repositorios, registros clínicos, capas analíticas, atlas, nomenclaturas, registros de ensayos y farmacovigilancia. | «Fuente» sigue siendo demasiado grueso para comparar capacidades y derechos. | Añadir `source_kind`, `unit_of_access`, `subject_level`, `longitudinality`, `data_controller` y `governing_terms_version`. |
| M02 | Mayor | D2 exige validación externa, temporal o multicéntrica de forma global. | Impone una prueba clínica a operaciones puramente descriptivas o de referencia y puede diluir las pruebas realmente necesarias para alertas o apoyo asistencial. | Hacer D2 condicional a `declared_operation`; definir para cada operación validez, comparador, conjunto separado y umbral de aceptación. |
| M03 | Mayor | «Congelar requisitos antes de demostrar datos» se trata como bloqueo general. | Puede interpretarse como primacía del repositorio frente al conocimiento experto. | Permitir requisitos clínicos candidatos en C y factibilidad empírica en E, ambos provisionales; sólo la intersección autorizada fija qué se representa o valida. |
| M04 | Mayor | La rejilla `.ig-flow-row` tiene dos columnas, pero la cabecera contiene tres carriles. | La tercera tarjeta puede replegarse a otra fila; la visualización no expresa igualdad ni paralelismo. | Crear una rejilla explícita de tres columnas en escritorio y una leyenda de continuidad por carril. |
| M05 | Mayor | No se completó prueba visual renderizada en navegador; sólo se validaron estructura y sintaxis. | No está probado que pestañas, foco, impresión visual ni adaptación responsive funcionen como se declara. | Ejecutar prueba local en navegador real y conservar acta de evidencias visuales antes de cerrar v3.1. |
| m01 | Menor | El selector raíz y varios identificadores internos conservan `v2`. | Deriva de versión y riesgo de seleccionar el nodo incorrecto en mantenimiento. | Migrar identificadores a una versión neutral o v3.1, preservando unicidad. |

## 4. Triple adversarial

### 4.1. Sanitaria, clínica y médica

1. **Falsa exhaustividad:** cubrir fenotipo, laboratorio, ómicas y desenlace no significa cubrir errores innatos, autoinmunidad, alergia, trasplante, infección, vacunación o inmuno-oncología.
2. **Consecuencia sin contexto:** un parámetro no posee por sí solo una consecuencia fija. La omisión depende de población, escenario, ventana temporal, operación, alternativas disponibles y acción que se deja de ejecutar.
3. **Disponibilidad no equivale a legitimidad clínica:** que una variable esté depositada no valida su umbral, ensayo, interpretación ni transferibilidad.
4. **Silencio peligroso:** si una entidad clínica no tiene datos adecuados, debe persistir en el residual profesional; no desaparecer del dominio.
5. **Doble destinatario:** toda omisión debe distinguir daño posible al paciente y consecuencia profesional/operativa para el experto. No son sustituibles.
6. **No contaminación terapéutica:** una relación entre parámetro y entidad no autoriza diagnóstico, pronóstico, tratamiento ni alerta hasta que la operación y sus pruebas estén declaradas.

**Resultado clínico:** no pasa todavía; B01 y B02 pueden producir un dominio sesgado por observabilidad y una apariencia de cobertura no demostrada.

### 4.2. Ingeniería de procesos, sin decidir lo clínico

1. El objeto de control debe ser `recorte clínico × operación × población × estrato × fuente/version`, no una lista global de repositorios.
2. Los carriles requieren estados independientes, colas de trabajo separadas y una interfaz de unión explícita; una cadena vertical no implementa paralelismo.
3. Cada fuente necesita tipo, release, unidad accesible, responsable, licencia/DUA y cuatro derechos separados: acceso, procesamiento local, exposición a IA y redistribución.
4. Un resultado negativo de búsqueda debe registrar consulta, fecha, filtros y alcance; «no encontrado» no equivale a «no existe».
5. La prueba visual del HTML es parte del entregable interactivo y no puede sustituirse por validación de sintaxis.
6. Ningún CSV externo debe entrar como tabla maestra: primero se valida esquema, duplicados, procedencia, definiciones y estatuto de cada fila.

**Resultado de proceso:** no pasa todavía; la arquitectura declarada no coincide con el grafo operativo ni con su presentación.

### 4.3. Lógica enlazada entre clínica y proceso

1. `estrato de evidencia ≠ perímetro clínico ≠ entidad ≠ parámetro ≠ operación`.
2. `fuente candidata ≠ fuente adoptada ≠ dato elegible para IA ≠ evidencia válida para una operación`.
3. `relación entity–parameter ≠ causalidad ≠ consecuencia de omisión`.
4. `prioridad 1–20 ≠ criticidad clínica ≠ gravedad ≠ urgencia ≠ disponibilidad empírica`.
5. `ausencia en datos ≠ ausencia en conocimiento ≠ U`.
6. C y E pueden avanzar en paralelo; ninguna salida de C o E puede convertirse en F sin una intersección autorizada y versionada.

**Resultado lógico:** no pasa todavía porque el diagrama afirma (6) pero su secuencia ejecuta dependencia `E → C`.

## 5. Controles que sí superan esta revisión

- IMMUNO-1 e IMMUNO-2 quedan como prototipos de contraste y no como dominio.
- La notación clínica `xᵢⱼ`, la notación de estado `sⱼ` y la fila formal `a₁ⱼ` están separadas.
- No se utiliza `n=b²` como ley general.
- U no nace de un dato faltante: exige una regla versionada y autorizada.
- D0-L separa acceso, uso por IA, procesamiento local y redistribución.
- Los datos restringidos no entran por defecto en una unidad de IA.
- R2, IR, semántica e implementación del Lenguaje están expresamente fuera de alcance.
- El HTML no depende de recursos externos ni conserva el estado de casillas entre sesiones.

Estos aciertos no compensan B01–B03.

---

## 6. Tarea paralela continuada: perímetros clínicos candidatos

### 6.1. Estatuto

La tabla siguiente **no es una taxonomía adoptada ni pretende exhaustividad**. Es un instrumento de auditoría para comprobar qué áreas quedarían mudas al cruzar los futuros CSV. Sus filas son candidatos de cobertura respaldados por organismos oficiales; corresponde a autoridad clínica decidir inclusión, partición, solapamientos y nomenclatura.

| ID candidato | Perímetro a someter a autoridad clínica | Qué obliga a comprobar | Anclaje institucional inicial |
|---|---|---|---|
| PC01 | Bases de inmunidad innata, adaptativa, regulación y tolerancia | Mecanismos y homeostasis sin convertirlos directamente en diagnósticos | [NIAID: panorama del sistema inmunitario](https://www.niaid.nih.gov/research/immune-system-overview); [NIAID: tolerancia inmunitaria](https://www.niaid.nih.gov/research/immune-tolerance) |
| PC02 | Errores innatos de la inmunidad | Clasificación versionada, fenotipo, genética, infección, autoinmunidad y tratamiento | [IUIS: Inborn Errors of Immunity Committee](https://iuis.org/committees/iei/) |
| PC03 | Inmunodeficiencias adquiridas o secundarias | Causa, reversibilidad, exposición, infección y respuesta inmune | [NIAID: trastornos del sistema inmunitario](https://www.niaid.nih.gov/research/immune-system-disorders) |
| PC04 | Autoinmunidad órgano-específica y sistémica | Pérdida de tolerancia, lesión de órgano, actividad, daño y respuesta terapéutica | [NIAID: enfermedades autoinmunes](https://www.niaid.nih.gov/diseases-conditions/autoimmune-diseases); [NIAMS: programa de autoinmunidad sistémica](https://www.niams.nih.gov/grants-funding/supported-scientific-areas/systemic-autoimmune-disease-biology-program) |
| PC05 | Autoinflamación e inflamación inmunomediada | Separar autoinflamación, autoimunidad, infección y fibrosis; capturar fenotipos raros | [NIAMS: programa de enfermedad autoinflamatoria](https://www.niams.nih.gov/grants-funding/supported-scientific-areas/scleroderma-fibrosis-and-autoinflammatory-disease-program) |
| PC06 | Alergia e hipersensibilidad | Alérgeno/exposición, órgano, mecanismo, gravedad, pruebas, evitación e inmunoterapia | [EAACI: secciones y grupos](https://eaaci.org/professionals/groups/) |
| PC07 | Inmunidad frente a infección y barreras/mucosas | Patógeno, tejido, respuesta protectora, inmunopatología, microbioma y persistencia | [NIAID: laboratorio de inmunidad del huésped y microbioma](https://www.niaid.nih.gov/research/lab-host-immunity-and-microbiome-lhim); [NIAID: sistema inmunitario](https://www.niaid.nih.gov/research/immune-system-overview) |
| PC08 | Vacunación e inmunidad inducida | Plataforma, pauta, respuesta, duración, fallo, seguridad y poblaciones especiales | [NIAID: investigación en vacunas](https://www.niaid.nih.gov/research/vaccines) |
| PC09 | Trasplante, aloinmunidad, tolerancia y enfermedad injerto contra huésped | Tipo de injerto, compatibilidad, rechazo, tolerancia, infección, inmunosupresión y desenlace | [NIAID: Allergy, Immunology & Transplantation](https://www.niaid.nih.gov/research/allergy-immunology-transplantation); [NIAID: Immune Tolerance Network](https://www.niaid.nih.gov/research/immune-tolerance-network) |
| PC10 | Inmunología tumoral e inmunoterapia oncológica | Inmunidad antitumoral, evasión, biomarcadores, respuesta, resistencia y toxicidad | [NCI: inmunología e inmunoterapia](https://ccr.cancer.gov/research/immunology-and-immunotherapy); [NCI: cartera de inmunología tumoral](https://www.cancer.gov/about-nci/organization/dcb/research-portfolio/ciher) |
| PC11 | Inmunoterapia, biológicos, inmunomodulación e inmunotoxicidad | Indicación, mecanismo, exposición, beneficio, infección, hipersensibilidad y reacciones inmunomediadas | [IUIS: Immunotherapy Committee](https://iuis.org/committees/ith/); [FDA: reacciones adversas inmunomediadas](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/characterizing-collecting-and-reporting-immune-mediated-adverse-reactions-cancer-immunotherapeutic) |
| PC12 | Complemento y efectores humorales | Vía, deficiencia/disregulación, infección, inflamación, biomarcadores y terapias dirigidas | [NHLBI: investigación sobre complemento e inflamación](https://www.nhlbi.nih.gov/science/complement-and-inflammation-research) |
| PC13 | Inmunología materno-fetal, neonatal y reproductiva | Tolerancia, placenta, transferencia, infección/vacunación, gestación y desenlaces materno-fetales | [NIAID/ORWH: mecanismos inmunes en la interfaz materno-fetal](https://grants.nih.gov/grants/guide/rfa-files/RFA-AI-23-027.html) |
| PC14 | Inmunidad pediátrica y desarrollo inmunitario | Edad, maduración, referencia específica y transición; no extrapolar automáticamente desde adultos | [EAACI: sección de pediatría](https://eaaci.org/section-group/pediatric/) |
| PC15 | Inmunosenescencia e inflamación asociada a la edad | Declive funcional, inflamación crónica, infección, vacunación, cáncer y comorbilidad | [NIA: envejecimiento, inmunidad e inflamación](https://www.nia.nih.gov/research/dab/workshops/workshop-advances-aging-immunity-and-chronic-inflammatory-disease) |
| PC16 | Inmunología diagnóstica y de laboratorio | Indicación, espécimen, método, control de calidad, intervalo/umbral, interferencias e interpretación | [NIAID: Laboratory of Clinical Immunology and Microbiology](https://www.niaid.nih.gov/research/lab-clinical-immunology-and-microbiology) |

### 6.2. Dimensiones transversales que no deben convertirse automáticamente en módulos clínicos

| Dimensión | Motivo de separación |
|---|---|
| Etapa vital | Modifica referencia, prevalencia, respuesta y consecuencias; atraviesa múltiples perímetros. |
| Órgano/tejido/barrera | Localiza el fenómeno, pero no define por sí solo el mecanismo ni la entidad. |
| Mecanismo inmunitario | Puede repetirse en entidades distintas y producir consecuencias diferentes. |
| Exposición/intervención | Medicamento, vacuna, infección, alérgeno o trasplante son contextos y pueden coexistir. |
| Escenario asistencial | Cribado, diagnóstico, urgencia, seguimiento, tratamiento e investigación requieren operaciones y pruebas diferentes. |
| Población y vulnerabilidad | Edad, gestación, inmunosupresión, comorbilidad y ascendencia pueden afectar validez y seguridad. |
| Tiempo externo | Debe figurar como dato explícito: inicio, secuencia, duración, ventana y fecha de referencia. No es una primitiva del núcleo. |
| Consecuencia de omisión | Debe tiparse por destinatario, acción perdida, reversibilidad, ventana y desenlace; no reducirse a una prioridad. |

## 7. Ajuste requerido para los futuros CSV de Grok y Claude

### 7.1. CSV de parámetros candidatos

Además del contenido ya encargado, conviene exigir como mínimo:

`parameter_id`, `preferred_label`, `definition`, `parameter_class`, `specimen_or_context`, `unit_or_scale`, `method_dependency`, `reference_dependency`, `population_scope`, `clinical_operation_candidate`, `source_citation`, `source_version`, `candidate_status`, `uncertainty_note`.

La prioridad 1–20 debe desdoblarse o acompañarse de campos independientes:

- criticidad de omisión para el paciente;
- criticidad profesional/operativa;
- urgencia o sensibilidad temporal;
- valor informativo para la operación declarada;
- factibilidad de observación;
- prioridad de validación empírica.

No se promediarán estas dimensiones para producir una verdad clínica única.

### 7.2. CSV de entidades tipificadas

No debe limitarse a «enfermedades». Debe identificar el tipo de entidad:

`entity_id`, `preferred_label`, `entity_type`, `parent_or_group`, `clinical_perimeter_candidate`, `mechanism_candidate`, `organ_or_tissue`, `life_stage`, `population_scope`, `diagnostic_or_classification_source`, `source_version`, `inclusion_rule`, `exclusion_rule`, `candidate_status`.

Tipos que deben poder distinguirse, sin afirmar que ésta sea una lista cerrada: enfermedad/síndrome, fenotipo, complicación, estado inmunitario, exposición, intervención, reacción adversa, proceso fisiológico y escenario asistencial.

### 7.3. Tablas de relación posteriores

No se unirá por texto ni por prioridad. La relación mínima sigue siendo:

`entity_id × parameter_id × relation_type × operation × population × temporal_window × consequence_id × evidence_id × review_status`.

Se necesita además una tabla propia de consecuencias:

`consequence_id × affected_party × omitted_knowledge_or_action × clinical_context × temporal_window × reversibility × outcome_type × evidence_source × authority_status`.

La tabla de cobertura de datos debe incorporar `source_kind` y mantener separados acceso, procesamiento local, elegibilidad para IA y redistribución.

## 8. Trabajo que puede seguir antes de la adversarial de Grok

1. Clasificar las 30 fuentes por `source_kind` sin adoptarlas.
2. Cruzar PC01–PC16 con E01–E15 usando sólo estados `candidato`, `no localizado` o `no aplicable`; nunca «cubierto» sin estudio y recorte concreto.
3. Preparar validadores de esquema para recibir los CSV, sin decidir el contenido clínico.
4. Registrar consultas públicas y resultados negativos con fecha y alcance.
5. Reservar B01–B03 para contraste de Grok y decisión del director antes de producir v3.1.

## 9. Parada explícita

No se ha modificado el HTML, el registro D0, la ITI, los prototipos ni el Lenguaje. No se han creado cuentas, solicitado accesos, descargado microdatos ni adoptado fuentes. La matriz PC01–PC16 sólo abre preguntas de cobertura; no cierra el dominio.
