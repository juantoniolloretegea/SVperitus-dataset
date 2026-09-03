# Mapa finito de universos operacionales del catálogo profesional INMUNO v0.8

**Fecha:** 2026-09-03  
**Base:** `a7ec7d29a05f0297e221dc5064a4ab056aca2429`  
**Fuente cerrada:** `Catalogo_profesional_atomico_INMUNO_v0.8_2026-09-02.xlsx` (blob Git `f697877c39ead8dc6d124fd0ef66dae80b902d61`)  
**Estatuto:** `MAPA_FINITO_DE_OPERACIONES_CANDIDATAS`; no constituye Q0, consecuencia, parámetro, matriz, ruta, aptitud clínica ni autorización asistencial.

## 0. Pregunta y respuesta

La pregunta no es cuántos temas contiene la Inmunología, sino cuántos productos profesionales distintos exige el corpus internacional acotado a España, Reino Unido, Australia/Aotearoa Nueva Zelanda y Canadá.

Aplicando una misma regla de identidad a todo el catálogo resultan **32 universos operacionales candidatos**:

- 19 clínico-asistenciales;
- 8 diagnóstico-laboratoriales;
- 3 de sistema, calidad y seguridad;
- 2 de producción y transmisión de conocimiento.

`OP-IMM-001 / Q0 v0` ocupa uno de los 32 (`OPMAP-CL-01`). El número 32 es cardinalidad del mapa de productos, no cardinalidad de parámetros, competencias, enfermedades, técnicas, usos ni futuros Q0. No autoriza `32 × 27`.

## 1. Regla única de identidad

Una operación candidata es la tupla:

`<producto terminal, sujeto/objeto, disparador, autoridad, frontera, criterio de finalización>`.

Dos actividades se fusionan sólo si conservan los seis campos. Se separan cuando cambia al menos uno de estos tres campos fuertes: producto terminal, autoridad responsable o criterio de finalización. Población, entorno o técnica sólo separan si alteran materialmente el producto o la autoridad.

No cuentan como universos autónomos:

- conocimientos sin producto profesional;
- procedimientos aislados que son medios de una operación;
- comunicación, consentimiento, priorización, prescripción y decisión compartida, que son controles transversales;
- atención aguda, longitudinal o transición como meras etiquetas temporales; sí cuentan cuando producen un objeto terminal distinto;
- escalas de progresión, pruebas del residente y requisitos formativos;
- especialidades vecinas enumeradas como frontera.

## 2. Mapa cerrado de candidatos

### 2.1 Clínico-asistenciales (19)

| ID | Producto terminal | Sujeto y disparador | Frontera / finalización | Anclas del catálogo |
|---|---|---|---|---|
| `OPMAP-CL-01` | Perfil predecisional de riesgo infeccioso antes de inmunosupresión | Adulto con inmunosupresión prevista | Termina en perfil trazado; no prescribe | `OP-IMM-001`; S-CIP-02/04; CA-SCP-07/09 |
| `OPMAP-CL-02` | Clasificación diagnóstica y plan inicial de inmunodeficiencia | Sospecha de IEI o inmunodeficiencia secundaria | No incluye seguimiento ni terapia concreta | ES-INM-CONT-082; AUNZ-KG-02; CA-SCP-06 |
| `OPMAP-CL-03` | Plan longitudinal de inmunodeficiencia | Inmunodeficiencia ya establecida | Termina en seguimiento/reevaluación versionados | AUNZ-G08; CA-OP-10; S-CIP-02 |
| `OPMAP-CL-04` | Evaluación inmunológica coordinada de autoinmunidad/autoinflamación | Presentación indiferenciada o enfermedad establecida | Inmunología no sustituye la especialidad de órgano | ES-INM-CONT-083; AUNZ-KG-03; CMP-006; F-03 |
| `OPMAP-CL-05` | Diagnóstico diferencial y plan de hipersensibilidad/alergia | Sospecha alérgica o simulador | En España mantiene frontera con Alergología | S-CIP-01; ES-INM-CONT-084; AUNZ-KG-04; CMP-011 |
| `OPMAP-CL-06` | Adjudicación de alergia a medicamentos y plan de evitación/uso | Reacción medicamentosa | Provocación/desensibilización son medios o rutas posteriores | PROC-02/03/05; CA-OP-05; F-11 |
| `OPMAP-CL-07` | Adjudicación de alergia alimentaria y plan | Reacción o sospecha alimentaria | Provocación alimentaria bajo autoridad propia | PROC-01/04; CA-OP-05 |
| `OPMAP-CL-08` | Adjudicación y plan de alergia respiratoria/cutánea | Presentación respiratoria, nasal, ocular o cutánea | Conserva interfaces Neumología, Dermatología y ORL | PROC-09/10/11; CA-OP-01/02; F-05/06/12 |
| `OPMAP-CL-09` | Plan de inmunoterapia específica | Alergia confirmada con indicación candidata | Termina en selección/seguimiento, no en mera administración | PROC-06/07; S-CIP-05-U03; CA-OP-06 |
| `OPMAP-CL-10` | Manejo agudo y plan postepisodio de anafilaxia | Anafilaxia presente o documentada | Separa estabilización del seguimiento pero conserva un expediente único enlazado | S-CIP-05-U06/U08/U09; PROC-08 |
| `OPMAP-CL-11` | Clasificación y plan de angioedema | Episodio recurrente/agudo de angioedema | C1-inhibidor es intervención, no identidad diagnóstica | S-CIP-05-U02; AUNZ-KG-04 |
| `OPMAP-CL-12` | Plan de vacunación individualizado | Inmunodeficiencia, inmunosupresión o reacción previa | Familia propia; termina en indicación/contraindicación y seguimiento | ES-INM-CONT-091; AUNZ-KG-06; CMP-004 |
| `OPMAP-CL-13` | Evaluación inmunológica de infección crónica/recurrente | Infección persistente o patrón recurrente | No equivale al perfil pre-inmunosupresión | ES-INM-CONT-085; CA-SCP-07; F-04 |
| `OPMAP-CL-14` | Evaluación inmunológica reproductiva, gestacional o neonatal | Embarazo, reproducción o periodo neonatal | Candidato condicionado a autoridad y frontera local | CA-SCP-03; CMP-007 |
| `OPMAP-CL-15` | Evaluación y seguimiento inmunológico de trasplante | Candidato o receptor de órgano/hematopoyético | No sustituye decisión del programa de trasplante | ES-INM-CONT-086; AUNZ-KG-05; CA-OP-10; F-08 |
| `OPMAP-CL-16` | Evaluación de crioglobulinemia/paraproteinemia | Hallazgo o sospecha clínica/laboratorial | Conserva interfaz Hematología | ES-INM-CONT-087; F-07 |
| `OPMAP-CL-17` | Plan y seguimiento de reposición con inmunoglobulina | Déficit con indicación candidata | Producto específico y administración trazable | ES-INM-CONT-088; S-CIP-05-U01; CA-OP-07 |
| `OPMAP-CL-18` | Plan y seguimiento de inmunomodulación, biológicos o inmunosupresión | Enfermedad con terapia candidata o iniciada | No absorbe el perfil previo `CL-01`; incluye respuesta y daño | ES-INM-CONT-089/090; S-CIP-05-U05/U07/U11; CA-SCP-09/10 |
| `OPMAP-CL-19` | Expediente de transición pediatría-adulto | Adolescente/joven con enfermedad inmunológica | Termina en transferencia efectiva de responsabilidad | S-CIP-06; AUNZ-G06; F-02 |

### 2.2 Diagnóstico-laboratoriales (8)

| ID | Producto terminal | Objeto y disparador | Frontera / finalización | Anclas del catálogo |
|---|---|---|---|---|
| `OPMAP-LAB-01` | Estrategia de selección e interpretación de pruebas | Pregunta clínica recibida | Termina en informe/asesoría con límites y `U`; no en técnica | S-CIP-03/07; ES-INM-ROL-003/004; CA-SCP-08 |
| `OPMAP-LAB-02` | Informe de inmunoproteínas, respuesta humoral y complemento | Muestra/pregunta humoral | Incluye cuantificación y función; conserva operandos separados | ES-INM-ACT-002/003/005/007; ES-INM-CONT-061/062 |
| `OPMAP-LAB-03` | Informe de inmunofenotipo y función celular | Muestra/pregunta celular | Fenotipo, proliferación, fagocito y citotoxicidad son componentes | ES-INM-ACT-015–021; CA-OP-03 |
| `OPMAP-LAB-04` | Informe de autoanticuerpos | Sospecha de autoinmunidad | Patrones y especificidades; no diagnostica por sí solo | ES-INM-CONT-066–069; F-03/09/10 |
| `OPMAP-LAB-05` | Informe de sensibilización/alergia in vitro | Sospecha de hipersensibilidad | No sustituye historia, provocación ni diagnóstico clínico | ES-INM-ACT-003/004; CA-SCP-08; CMP-011 |
| `OPMAP-LAB-06` | Informe de histocompatibilidad y aloinmunidad | Donante/receptor, trasplante o asociación HLA | Tipaje, anticuerpos y prueba cruzada; autoridad del programa preservada | ES-INM-ACT-022/023; ES-INM-CONT-070–075 |
| `OPMAP-LAB-07` | Informe molecular/genético inmunológico | Sospecha genética, cribado o clonabilidad | Incluye TREC, variantes y reordenamientos; consentimiento y límites obligatorios | ES-INM-ACT-024/025; ES-INM-CONT-077–080; CA-OP-04; CMP-009 |
| `OPMAP-LAB-08` | Decisión documentada sobre ensayo/repertorio | Nueva prueba, cambio de método o demanda | Termina en validación, rechazo o uso condicionado | S-CIP-07-U06/U08/U10–U13; S-CIP-08-U09/U10/U12–U14 |

### 2.3 Sistema, calidad y seguridad (3)

| ID | Producto terminal | Disparador | Finalización | Anclas del catálogo |
|---|---|---|---|---|
| `OPMAP-SYS-01` | Ruta/protocolo asistencial interdisciplinar | Variabilidad, interfaz o necesidad de coordinación | Protocolo versionado, responsables y frontera | S-CIP-04-U01–U05; ES-INM-ACT-027 |
| `OPMAP-SYS-02` | Estado gobernado del servicio/laboratorio | Ciclo de gestión o acreditación | Recursos, repertorio, calidad, regulación y revisión | S-CIP-08-U01–U11; ES-INM-CONT-092/093; ES-INM-ACT-036/039/040 |
| `OPMAP-SYS-03` | Suceso de seguridad y respuesta correctiva | Complicación, daño, incidente o incumplimiento | Investigación, comunicación, corrección y seguimiento | CA-SCP-10; CMP-010; G-CIP-02; ES-INM-CONT-094/095 |

### 2.4 Producción y transmisión de conocimiento (2)

| ID | Producto terminal | Disparador | Finalización | Anclas del catálogo |
|---|---|---|---|---|
| `OPMAP-KN-01` | Proyecto de investigación o mejora evaluable | Pregunta científica/de calidad | Protocolo, análisis y comunicación; nunca autorización asistencial | ES-INM-ROL-005; ES-INM-ACT-029–031; CA-SCP-04; AUNZ-G04 |
| `OPMAP-KN-02` | Episodio de docencia/supervisión con evaluación | Necesidad formativa | Objetivo, observación, retroalimentación y decisión formativa | ES-INM-ACT-032–035; AUNZ-G03; T-01–T-14 |

## 3. Cobertura del corpus

| Bloque del XLSX | Tratamiento en el mapa |
|---|---|
| Capacidades y 123 descriptores UK (`02`–`05`) | Distribuidos por producto entre CL, LAB, SYS y KN; los genéricos operan como controles transversales |
| 11 procedimientos (`06`–`08`) | Medios de `CL-06`–`CL-10`; no once universos automáticos |
| 14 pruebas formativas (`09`) | Evidencia de `KN-02`; no operaciones clínicas |
| 12 fronteras (`10`) | Guardarraíles de CL/LAB; ninguna especialidad vecina se importa como rama |
| Roles, contenidos y actividades ES (`14`–`19`) | Separación explícita de autoridad médica, laboratorio, Alergología y titulación |
| Metas/guías AU/NZ (`25`–`28`, `36`) | DO alimenta operaciones; KNOW delimita materia sin multiplicar universos; escalas no se convierten |
| Alcance/operaciones CA (`29`, `30`) | Corroboran productos clínicos, diagnósticos y de seguridad; no se copian uno-a-uno |
| Deltas (`31`) | Se preservan agudo/longitudinal/transición, vacunación, taxonomía moderna, ciclo vital, diagnóstico molecular y daño |
| Reutilización y derechos (`32`) | Sólo paráfrasis e identificadores; no reproducción del corpus fuente |

Cobertura estructural: **37/37 hojas clasificadas**. Cobertura semántica: cada familia adoptada o mantenida del catálogo tiene al menos un destino o un guardarraíl transversal. Esto no afirma que cada fila sea una operación ni que todas produzcan parámetros.

## 4. Ataques de grano

### A. Fusión indebida

1. `CL-01` no se fusiona con `CL-18`: perfil previo y seguimiento terapéutico terminan en productos distintos.
2. `CL-02` no se fusiona con `CL-03`: clasificación inicial y seguimiento longitudinal tienen distinto disparador y cierre.
3. `CL-05`–`CL-11` no se reducen a «alergia»: medicamento, alimento, inmunoterapia, anafilaxia y angioedema cambian autoridad, riesgo o producto.
4. `LAB-01` no absorbe `LAB-02`–`LAB-07`: la estrategia de pruebas y el informe analítico son productos distintos.
5. `LAB-06` no se fusiona con `CL-15`: histocompatibilidad informa; el programa clínico decide y sigue.
6. `SYS-02`, `KN-01` y `KN-02` no se funden con asistencia: gestión, investigación y evaluación formativa no autorizan decisiones clínicas.

Resultado: ninguna fusión reduce lícitamente el mapa por debajo de 32 con la evidencia v0.8.

### B. Fragmentación burocrática

1. Historia, exploración, diferencial, comunicación, consentimiento, priorización y prescripción se integran en la operación que sirven.
2. Los once procedimientos no generan once Q0: sólo separan cuando modifican producto/autoridad (`CL-06`–`CL-10`).
3. Atención aguda y longitudinal no duplican todas las enfermedades; sólo separan productos materialmente distintos (`CL-02/03`, `CL-10`).
4. Cada analito, técnica, autoanticuerpo, citocina o variante es operando o parámetro futuro, no universo.
5. España, Reino Unido, Canadá y AU/NZ no cuadruplican operaciones equivalentes; la jurisdicción se conserva en `u(p,O,j)` y en la autoridad.

Resultado: no se justifica elevar el recuento mediante filas, técnicas, años formativos o jurisdicciones.

### C. Huecos de cobertura

Se buscaron expresamente los huecos que la estimación inicial omitía: ciclo vital (`CL-14`), vacunación (`CL-12`), daño asistencial (`SYS-03`), transición (`CL-19`), molecular moderno (`LAB-07`), histocompatibilidad (`LAB-06`), gobierno del laboratorio (`SYS-02`) y producción/docencia (`KN-01/02`). Todos quedan visibles.

Quedan dos límites, no huecos silenciosos:

- alergia es parte del corpus internacional pero en España conserva autoridad propia; sus operaciones son `JURISDICCION_CONDICIONADA`, no competencias importadas;
- coagulación/fibrinólisis/calicreína–cininas y reproducción/embarazo/neonatal estaban bloqueadas hasta G3 en v0.8; aquí sólo se reserva su destino (`LAB-02` y `CL-14`), sin afirmar consecuencia ni parámetro.

## 5. Recuento y significado

| Magnitud | Valor | Qué significa |
|---|---:|---|
| Universos candidatos | **32** | Productos profesionales distinguibles por la regla de identidad |
| Clínicos | 19 | Incluye 1 ya recorrido: `OP-IMM-001` |
| Laboratorio | 8 | Informes/decisiones diagnósticas, no enfermedades |
| Sistema/seguridad | 3 | Protocolos, gobierno y corrección |
| Conocimiento | 2 | Investigación/mejora y docencia/supervisión |
| Q0 abiertos por este mapa | 0 | El mapa precede a cualquier nuevo G0/Q0 |
| Parámetros inferidos | 0 | No se extrapola desde los 27 de `OP-IMM-001` |

La anterior banda 20–30 con centro 24 queda sustituida: comprimía laboratorio, seguridad, investigación y docencia. El recuento defendible bajo la regla declarada es 32. No es una verdad ontológica sobre toda la Inmunología; es el mapa finito del corpus v0.8 y debe versionarse si cambia el corpus o la regla de identidad.

## 6. Adversarial integrada

| Ataque | Resultado |
|---|---|
| Contar enfermedades | Rechazado: se cuentan productos profesionales |
| Contar cada técnica | Rechazado: técnica es medio salvo cambio fuerte de producto/autoridad |
| Multiplicar por jurisdicción | Rechazado: se preserva autoridad sin duplicar identidad |
| Importar Alergología a España | Rechazado: frontera `CMP-011` y `ES-INM-ROL-009` |
| Omitir actividad no clínica | Rechazado: LAB/SYS/KN están en el corpus y producen objetos propios |
| Convertir conocimiento en operación | Rechazado: KNOW sólo delimita materia |
| Derivar parámetros por regla de tres | Rechazado: reutilización y `u(p,O)` impiden `32 × 27` |
| Abrir 31 Q0 automáticamente | Rechazado: cada candidato requiere G0 propio y puede fusionarse, bloquearse o caer |
| Declarar exhaustividad internacional absoluta | Rechazado: exhaustividad relativa a v0.8 y cuatro jurisdicciones |

`ADVERSARIAL_DE_MAPA = PASA_CON_LIMITES_EXPLICITOS`.

## 7. Regla de continuación

El mapa queda cerrado para revisión en **32 candidatos**. La siguiente operación no se elige por comodidad documental, sino por máxima capacidad de falsar la arquitectura de `OP-IMM-001`. Debe cambiar sustancialmente de producto y, preferentemente, de autoridad. Por ello la candidata metodológicamente más informativa es `OPMAP-LAB-01` o `OPMAP-LAB-06`, no otra variante inmediata de perfil clínico predecisional.

No se abre ninguna de ellas mediante este documento. La apertura requiere decisión del Director.

## 8. Declaraciones

- `MAPA_FINITO_OPERACIONES_v0.8 = 32_CANDIDATOS`.
- `OP_IMM_001_ES_UNO_DE_32 = SI`.
- `DOMINIO_PARAMETRICO_CERRADO = NO`.
- `SEGUNDO_Q0_ABIERTO = NO`.
- `MULTIPLICACION_32_POR_27_AUTORIZADA = NO`.
- `DOCUMENTACION_DERIVADA_NO_IMPERATIVA = PROHIBIDA`.

