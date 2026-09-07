# Retorno acotado de Inmunología al Lenguaje SV: contrato documental, fidelidad y pérdidas de OP-IMM-001 / Q0 v0

**Fecha:** 7 de septiembre de 2026. **Versión documental:** 0.1. **Ámbito:** fila 6/G-H, exclusivamente OP-IMM-001 / Q0 v0. **Destinatario del relevo:** unidad del Lenguaje de computación SV, fila 7.

**Dictamen:** devolución ordinaria fundada por **suficiencia no acreditada para ejecutar Q0**. Se completa I1–I8 en el alcance documental autorizado. Se acredita fidelidad y se demuestran pérdidas en los espacios documentales finitos expresamente ensayados; ninguna de esas pruebas acredita ejecución clínica, transducción productiva ni una representación SV suficiente de la operación completa.

El resultado requiere respuesta de Lenguaje sobre sus carencias identificadas. La ausencia de esa realización no impide la devolución. Tras este paquete, **Inmunología queda en pausa controlada**. No se abre otro universo, Ciberseguridad, álgebra, K2 ni R2/R3/R4. No se modifica el repositorio del Lenguaje.

## 1. Autoridad, identidad y contenido del paquete

La autorización y los criterios de terminación proceden de [IMM-ACTA, §§3–4 y 8](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/ACTA_PAUSA_RETORNO_ACOTADO_Y_RELEVO_AL_LENGUAJE_SV_2026-09-04.md). La lectura de sus antecedentes se subordina a la recepción del 07/09: no se repite la reparación histórica de PR #60 ni se vuelve a K1. La regla de salida aplicable es §8.5: el contraste debe devolver también pérdidas o insuficiencias, con responsable, sin un cierre favorable ficticio.

| Objeto | Identidad exacta |
|---|---|
| Repositorio y rama de trabajo | `juantoniolloretegea/SVperitus-dataset`, `dominio-inmunologia` |
| Commit de entrada de Inmunología | `d4d6c81cb9aab5194abc8e61212c0d63877a0b9c` |
| Árbol de entrada | `42d0ee9831ecea36ea6807b645d8d6a61230d8b0` |
| Corte clínico sustantivo preservado | `3bea6b714be3bd1330e6ca6bbbc228b0eb9c065d` |
| Corte recibido de Lenguaje | `bc3b22c9e9319e8f191390c8cfe9fa1577904d87` |
| Árbol recibido de Lenguaje | `51d0215604b84519361aea6749a3d17811a1307e` |
| PR #76 integrada | Cabeza `2f5499299c99557ddc3b89f3adc66c4b4d8d3427`; integración `bc3b22c9…` |
| Commit de salida | Commit de incorporación de este archivo y sus seis anexos, con padre único `d4d6c81…`; localizador inequívoco indicado debajo |

El historial de incorporación identifica la salida sin autorreferencia circular: `git log --diff-filter=A --format=%H --` seguido de la ruta completa de este documento. El commit de salida incorpora el paquete y el relevo en el acta existente; no modifica los antecedentes clínicos ni fusiona esta rama con `main`.

**Verificación ejecutada de identidad.** Los 44 archivos fuente seleccionados coinciden en longitud, SHA-256 y objeto blob Git con los árboles de entrada. [fuentes.json](fuentes.json) conserva repositorio, commit, ruta, enlace fijo, bytes, ambas huellas y alcance de lectura de cada fuente. El cotejo desde el corte clínico sustantivo sólo encuentra cambios de navegación y del acta de pausa; no cambios del contenido clínico. Las fuentes rectoras, el contrato F, FFL-E, F-IF y la constitución de los 27 quedan identificados en ese inventario.

**Conformidad recibida, no atribuida como prueba nueva.** La [Conformidad SVP de PR #76](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/actions/runs/34124242361) terminó correctamente sobre su cabeza. La comparación de esa cabeza con el commit integrado no contiene archivos diferentes. Los tres controles publicados en la integración (`build`, `report-build-status`, `deploy`) figuran como correctos; son controles de ese flujo y no se renombrarán como validación clínica. No se ha vuelto a compilar Rust ni ejecutado una nueva campaña nativa/WebAssembly. Sí se han ejecutado los observadores F-IF sobre sus archivos exactos del corte integrado. Las evidencias recibidas y los controles de integración se distinguen en `fuentes.json`.

| Archivo del paquete | Función |
|---|---|
| Este documento | Contrato, análisis semántico, dictamen, adversarial y devolución |
| [contraste.json](contraste.json) | 15 requisitos, 44 formulaciones, 81 enlaces revisados; los 27 parámetros con definiciones recibidas, reglas, procedencia, pérdidas y dependencias; aplicación de F-IF |
| [fuentes.json](fuentes.json) | Inventario de fuentes y cortes verificables |
| [testigos.json](testigos.json) | Ocho pares documentales, oráculos literales y doce comprobaciones de la realización pendiente |
| [verificar.mjs](verificar.mjs) | Verificador externo reproducible; no es compilador ni implementación clínica |
| [evidencia.json](evidencia.json) | Resultado determinista de las pruebas ejecutadas, con huellas de sus entradas |
| [ejecuciones_recibidas.json](ejecuciones_recibidas.json) | Salida de las dos órdenes originales F-IF ejecutadas localmente; conserva sus duraciones como registro técnico |

Los seis anexos sirven a la prueba y a la entrega estructurada; no constituyen seis actuaciones administrativas. El único expediente principal es éste. Las claves `GH-DOC`, `NEG` y `SP` identifican testigos y controles, no una tercera familia de requisitos.

## 2. Correspondencia semántica de los 15 requisitos y las 44 formulaciones

Se conserva la correspondencia recibida de [LSV-VAL, §5.1](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/dominios/inmunologia/VALORACION_TECNICA_Y_ENCAJE_DE_OP-IMM-001_CON_EL_LENGUAJE_SV_2026_09_03.md), contrastada con las formulaciones originales de [IMM-G10, §2](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/15-requisitos-lenguaje-sv/G10-SV_requisitos_demostrados_OP-IMM-001_v0.1_2026-09-03.md) e [IMM-REQ, §12](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/marco-tecnico-de-universos-subdominios-y-modulos/01-op-imm-001-informacion-preinmunosupresion-adultos/Solicitud_de_valoracion_y_encaje_tecnico_de_OP-IMM-001_con_el_Lenguaje_SV_2026-09-03.md). Su realización se interpreta mediante [LSV-F, §§6–6.1](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/arquitectura/CONTRATO_CANDIDATO_F_DOMINIO_REPRESENTACION_Y_SUFIENCIA_POR_OPERACION_2026_09_07.md), no mediante afirmaciones históricas sobre Python, referencias colgantes ya reparadas o transducción no habilitada.

El cruce contiene **81 enlaces**, 15 identificadores G10 distintos y 44 LSV distintos. Once formulaciones LSV no tienen padre exclusivo en la tabla: `010`, `020`, `021`, `023`, `024`, `030`, `032`, `036`, `042`, `043` y `044`. Son ampliaciones transversales ya existentes; no se eliminan ni se cuentan como capacidades realizadas. No se observa una duplicación que autorice suprimir un identificador. Los enlaces múltiples reflejan condiciones compartidas, no equivalencia completa entre todos sus extremos.

### 2.1 Revisión desde cada requisito G10

En esta tabla se abrevian únicamente los prefijos de los identificadores: `SV-001` significa `REQ-IMM-SV-001`; `LSV-007`, `REQ-IMM-LSV-007`. En el anexo se conservan completos, con clasificación, justificación y localizadores por **cada uno de los 81 enlaces**.

| Requisito | Formulaciones relacionadas | Relación revisada y límite |
| --- | --- | --- |
| SV-001 · estado ternario por parámetro | LSV-007, LSV-012, LSV-040 | Refinamiento. Los literales Tri no constituyen un resultado ni una transducción clínica por parámetro; DFL-005/K1-T. |
| SV-002 · composición ordenada de unidades y referencias | LSV-025, LSV-026, LSV-040, LSV-041 | Cobertura parcial. Los metadatos y el experimento no expresan por sí solos composición clínica ordenada: G10 conserva esa obligación propia. |
| SV-003 · supervisión humana de salida estructural | LSV-009, LSV-015, LSV-016, LSV-033 | Refinamiento. Autoría, revisión y firma refinan la supervisión; no prueban el flujo clínico ni su durabilidad. |
| SV-004 · `Frame` derivado de arquitectura existente | LSV-026, LSV-031, LSV-041 | Cobertura parcial. J-H0 y el cierre relacional ya fueron reparados; la derivación completa del resumen OP no se acredita con esas guardas. |
| SV-005 · procedencia, fuente, versión, localizador y hash | LSV-001, LSV-002, LSV-012, LSV-016, LSV-017, LSV-025, LSV-027, LSV-028, LSV-029, LSV-034, LSV-035, LSV-037 | Refinamiento. La procedencia se despliega en varias capas; privacidad/retención, construcción y persistencia no son equivalencias de fuente clínica. |
| SV-006 · causas tipadas de `U` sin nuevos valores | LSV-007, LSV-012, LSV-013, LSV-031 | Refinamiento. La causa tipada es externa al alfabeto. LSV-013 pide pérdida de distinción; no identifica U clínica con insuficiencia FFL-E. |
| SV-007 · fallo técnico separado de `U` clínica | LSV-007, LSV-008, LSV-011, LSV-015, LSV-017, LSV-019, LSV-022 | Cobertura parcial. LSV-008 expresa la prohibición central; interrupciones y recuperación añaden condiciones materiales. Ningún fallo pertenece al codominio OP. |
| SV-008 · adjudicación humana de `U` crítica/no crítica con motivo | LSV-009, LSV-014, LSV-015, LSV-016 | Refinamiento. La adjudicación es un suceso nuevo, con objeto, motivo, autoridad y alcance; no una clausura favorable implícita. |
| SV-009 · veto no compensable anterior al resumen | LSV-009, LSV-014, LSV-015, LSV-031 | Cobertura parcial. El orden previo al resumen y la no compensación siguen siendo obligación expresa G10; criticidad o supervisión no la sustituyen. |
| SV-010 · productor superficial de criticidades | LSV-014, LSV-041 | Cobertura parcial. LSV-014 regula la legitimidad clínica; G10-010 pide además productor superficial. Coinciden parcialmente, no son equivalentes completos. |
| SV-011 · matrices `(6,1,3,2,6,9)` sin relleno | LSV-026, LSV-039, LSV-040, LSV-041 | Cobertura parcial. Se mantiene U_NO_DECIDIDO; 27 nombres, seis grupos y nueve miembros no dan posiciones (C,j), célula ni codominio celular. |
| SV-012 · resumen reversible a seis frames y 27 parámetros | LSV-003, LSV-012, LSV-013, LSV-017, LSV-034, LSV-039, LSV-040 | Cobertura parcial. LSV-013 se refiere a indeterminación y pérdida; reversibilidad exige todo detalle necesario, incluso cuando no hay U. |
| SV-013 · manifiestos cerrados de configuración clínica | LSV-001, LSV-005, LSV-006, LSV-009, LSV-012, LSV-016, LSV-018, LSV-025, LSV-034 | Refinamiento. Identidad de configuración, catálogo, reglas, admisión y persistencia se refinan por separado; un operando presente no está adoptado. |
| SV-014 · una de cuatro salidas exclusivas sin consejo terapéutico | LSV-003, LSV-006, LSV-007, LSV-008, LSV-017, LSV-031, LSV-038, LSV-039 | Refinamiento. Catálogo y forma de salida son obligaciones del dominio; no convierten la salida terminal en Tri ni acreditan selección ejecutable. |
| SV-015 · reproducción byte a byte con orden canónico | LSV-002, LSV-003, LSV-004, LSV-005, LSV-017, LSV-035 | Cobertura parcial. LSV-003 fija la exigencia; LSV-004 es una pregunta histórica: Python está retirado. Paridad de proyección no equivale a salida OP canónica. |

Dos precisiones son materiales:

1. **SV-010 y LSV-014 no son equivalentes completos.** El primero exige un productor superficial de criticidades; el segundo exige legitimidad clínica contextual, regla y autoridad. Deben conservarse ambos. Una regla legítima no materializa el productor; un productor no constituye la regla.
2. **LSV-013 no agota la reversibilidad de SV-012.** La pérdida puede afectar una fuente, atribución, versión u orden aun cuando no aparezca una U. Una consulta de indeterminaciones no demuestra la recuperación íntegra de las dependencias del resumen.

La equivalencia normativa acotada de SV-007/LSV-008 y SV-015/LSV-003 conserva respectivamente la separación del fallo y la igualdad literal. No acredita por sí misma implementación. Las coberturas parciales de composición, derivación del resumen y veto previo conservan el contenido G10 como obligación propia, sin esconderlo bajo una referencia general a metadatos.

### 2.2 Cobertura inversa y clasificación de I4

Cada formulación tiene una sede, un estado y un testigo ejecutado o especificado. `REPRESENTACIÓN EXACTA DOCUMENTAL` se restringe al banco externo; `COMPOSICIÓN PENDIENTE` no afirma una composición SV ya ejecutable. En `contraste.json`, `inverse`, figuran además el texto literal original y todos los requisitos G10 relacionados.

| Formulación | Clasificación y sede | Realización, prueba y límite |
| --- | --- | --- |
| LSV-001 | Obligación del perfil; Lenguaje + perfil | Identidad completa documentada; ligadura ejecutable pendiente. SP-01 (sólo especificado). |
| LSV-002 | Obligación del perfil; Interfaz + Lenguaje | Conservar bytes y referente; comprobación local de 44 fuentes, sin custodia material acreditada. GH-DOC-05 (documental ejecutado). |
| LSV-003 | Obligación del perfil; Lenguaje + motor | Igualdad exacta exigida; el observador documental no es serializador OP. SP-08 (sólo especificado). |
| LSV-004 | Conflicto histórico precisado; Lenguaje | Referencia Python retirada; no interviene. Paridad clínica nueva no ejecutada. SP-08 (sólo especificado). |
| LSV-005 | Obligación del perfil; Lenguaje + motor | Contrato de normalización, orden e identidad; faltan ensayos de la realización OP. SP-08 (sólo especificado). |
| LSV-006 | Obligación del perfil; Dominio + Lenguaje | Cuatro salidas cerradas; sin consejo ni prosa generativa. Plantillas futuras no constituidas. SP-07 (sólo especificado). |
| LSV-007 | Conflicto histórico precisado; Dominio + Lenguaje | F §3.2 prevalece en esta interfaz: categorías de admisión y fallo fuera de Tri. GH-DOC-06 (documental ejecutado). |
| LSV-008 | Obligación del perfil; Lenguaje + motor | Ningún fallo genera salida clínica; se exige ensayo integrado, aún no disponible. SP-09 (sólo especificado). |
| LSV-009 | Composición pendiente; Lenguaje + autoridad | R1 no acredita flujo OP; adjudicación es suceso nuevo. GH-DOC-04 (documental ejecutado). |
| LSV-010 | Obligación de infraestructura; R2 + motor | Comprobación y efecto sobre misma identidad material; no ensayado en G/H. SP-11 (sólo especificado). |
| LSV-011 | Obligación de infraestructura; R2 + motor | Interrupción y efecto incierto; no autoriza reintento ni U. SP-11 (sólo especificado). |
| LSV-012 | Obligación del perfil; Dominio + interfaz + Lenguaje | Contrato individual para los 27; ejecución y ligaduras DFL-005 pendientes. GH-DOC-07 (documental ejecutado). |
| LSV-013 | Obligación del perfil; Dominio + interfaz | Distinción perdida individual trazada; criticidad clínica y pérdida representacional separadas. GH-DOC-01 (documental ejecutado). |
| LSV-014 | Obligación del perfil; Dominio + autoridad clínica | Regla contextual legítima previa; no inferida del parámetro, no constituida automáticamente aquí. GH-DOC-04 (documental ejecutado). |
| LSV-015 | Obligación del perfil; Lenguaje + autoridad | Acto humano no sanea fallo; preservar antecedente. SP-09 (sólo especificado). |
| LSV-016 | Obligación del perfil; Institución + interfaz + Lenguaje | Identidad, competencia, delegación y revocación; un nombre o hash no autentica autoridad. GH-DOC-04 (documental ejecutado). |
| LSV-017 | Obligación del perfil; Lenguaje + motor | Este paquete reproduce observaciones documentales, no un expediente asistencial ejecutado. SP-08 (sólo especificado). |
| LSV-018 | Obligación de infraestructura; R2 + motor + institución | Persistencia autoritativa no acreditada por archivos o ensayos en memoria. SP-11 (sólo especificado). |
| LSV-019 | Obligación de infraestructura; R2 + sistema operativo | Recuperación material pendiente; no se simula corte eléctrico como prueba hospitalaria. SP-11 (sólo especificado). |
| LSV-020 | Obligación de infraestructura; R2 + almacenamiento | Huella detecta alteración respecto de copia de confianza; no acredita detección de retroceso/clonación. SP-11 (sólo especificado). |
| LSV-021 | Obligación de infraestructura; R2 + institución | Distinguir fuente autoritativa, vista, respaldo y réplica; no dar autoridad a un hash. GH-DOC-05 (documental ejecutado). |
| LSV-022 | Obligación de infraestructura; R2 + motor | Idempotencia y efecto incierto requieren acto/permiso/materialidad ligados. SP-11 (sólo especificado). |
| LSV-023 | Obligación de frontera; Lenguaje + motor + infraestructura | Reparto de obligaciones explícito; resolución material diferida a su sede. SP-11 (sólo especificado). |
| LSV-024 | Obligación de frontera; Lenguaje | Contrato de soporte sin elegir proveedor; DFL-009 fila 9, no abierto aquí. SP-11 (sólo especificado). |
| LSV-025 | Obligación del perfil; Dominio + interfaz | Referencia completa y contenido; URI y código aislados son insuficientes. GH-DOC-01 (documental ejecutado). |
| LSV-026 | U_NO_DECIDIDO; Lenguaje + dominio | Metadatos necesarios identificados; su sede normativa no se deduce del almacenamiento JSON. SP-02 (sólo especificado). |
| LSV-027 | Obligación de interfaz; Interfaz clínica + Lenguaje | Procedencia y auditoría perfiladas; no se ejecuta conector FHIR en este retorno. GH-DOC-05 (documental ejecutado). |
| LSV-028 | Obligación de interfaz; Interfaz clínica + dominio | Recursos FHIR como referencias; ImagingStudy no aplica al corte actual. GH-DOC-02 (documental ejecutado). |
| LSV-029 | Obligación del perfil; Dominio + interfaz terminológica | Versiones, equivalencias y retirada; ninguna conversión automática nueva. SP-03 (sólo especificado). |
| LSV-030 | No aplicable en Q0 v0; Dominio | No hay consumidor DICOM/DICOMweb; no se hereda desde médula sintética. SP-12 (sólo especificado). |
| LSV-031 | Obligación del perfil; Dominio + Lenguaje | Código/documento no es interpretación; no hay transducción habilitada por K1-T. SP-03 (sólo especificado). |
| LSV-032 | Obligación de evidencia; Calidad + responsables de producto | Sólo evidencia técnica delimitada; no se evalúa ni declara conformidad regulatoria. SP-11 (sólo especificado). |
| LSV-033 | Obligación de frontera; Institución + responsables de producto | Autoridad clínica, uso previsto y obligaciones institucionales no recaen sólo en Lenguaje. SP-11 (sólo especificado). |
| LSV-034 | Obligación del perfil; Calidad + Lenguaje | Requisito-control-prueba-versión del paquete documentado; código OP inexistente no se inventa. SP-01 (sólo especificado). |
| LSV-035 | Obligación de infraestructura; R3/R4 + Calidad | Cadena de construcción y carga material pendiente; este banco no es distribución del producto. SP-11 (sólo especificado). |
| LSV-036 | Obligación de infraestructura; Entorno + institución | Sin datos reales ni secretos en testigos; aislamiento productivo no probado. SP-11 (sólo especificado). |
| LSV-037 | Obligación del perfil; Institución + interfaz | Minimización con procedencia suficiente; no ordenar conservación universal de datos. GH-DOC-05 (documental ejecutado). |
| LSV-038 | Obligación de evidencia; Institución + Calidad + dominio | Prohibición de uso real conservada; G/H no retira ninguna condición. SP-11 (sólo especificado). |
| LSV-039 | U_NO_DECIDIDO; Lenguaje + dominio | Inventario 27 completo para contraste documental; experimento integrado OP no habilitado. SP-02 (sólo especificado). |
| LSV-040 | Representación exacta documental; Interfaz documental | F-IF y ocho pares ejecutables como observadores externos; ninguna consulta SV por ello. GH-DOC-07 (documental ejecutado). |
| LSV-041 | Candidata a extensión; Lenguaje | DFL-005/006 y salida OP requieren decisión técnica; no modificar gramática o IR desde IMM. SP-04 (sólo especificado). |
| LSV-042 | Obligación de secuencia; Lenguaje + Director | Corrección documental reversible; cambio de semántica/realización necesita su propia identidad y prueba. SP-12 (sólo especificado). |
| LSV-043 | Obligación de secuencia; Lenguaje | Fila 7 recibe ahora; DFL-009 fila 9 y cierre operacional fila 13 conservados. SP-12 (sólo especificado). |
| LSV-044 | Obligación de secuencia; Director + sedes competentes | Pausa IMM tras devolución; ni otro universo ni otra fase por iniciativa propia. SP-12 (sólo especificado). |

El compilador Python queda retirado de este contraste. LSV-004 conserva su texto histórico para trazabilidad, con esa sucesión expresa de estado. Ningún auxiliar de este paquete actúa como compilador ni elude K1-T.

## 3. Contrato documental candidato del perímetro completo

**Identidad del candidato:** `PERFIL_DOCUMENTAL_CANDIDATO_OP-IMM-001_Q0_v0_GH_2026-09-07`, versión documental 0.1. Es un contrato externo candidato. No se presenta como construcción disponible de la representación intermedia, como nuevo perfil normativo del Lenguaje ni como programa SV.

### 3.1 Finalidad, población y objeto

La operación organiza un **expediente informativo predecisional** anterior al inicio de inmunosupresión sistémica en adultos, con sus condiciones, carencias, fuentes y responsabilidad clínica. No estima una probabilidad de infección, no diagnostica ni selecciona tratamiento. Conserva el alcance y las exclusiones de [IMM-G1](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/06-operacion-testigo-en-evaluacion/OP-IMM-001_constitucion_perfil_riesgo_infeccioso_preinmunosupresion_G1_v0.2_2026-09-02.md) y [IMM-CLIN, §§1–2](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/universos-clinicos/01-evaluacion-predecisional-riesgo-infeccioso-antes-inmunosupresion-adultos/Expediente_predecisional_de_informacion_clinica_pertinente_antes_de_iniciar_tratamiento_inmunosupresor_en_adultos_v1.1_2026-09-03.md).

No incluye pediatría, trasplante, terapias celulares, quimioterapia oncohematológica, diagnóstico inmunológico integral, selección o dosificación del inmunosupresor, profilaxis, vacunación ni autorización para tratar. Los cribados específicos y la clasificación completa de inmunosupresores que el expediente declara no constituidos siguen fuera del subconjunto formalizado. Recibir F-IF no cambia ese perímetro.

Además de los 27 parámetros, el contrato exige la caracterización de la propuesta completa —componentes, vía, intención, estado, magnitud, duración y exposición previa o concomitante—, edad en fecha índice, control `SEM-RUT-001`, autoridad y configuración. Son dependencias explícitas de la operación, no nuevos parámetros. Su ausencia impide afirmar suficiencia; no se reduce el plan a preguntar si contiene glucocorticoide. [IMM-CLIN, §1.2](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/universos-clinicos/01-evaluacion-predecisional-riesgo-infeccioso-antes-inmunosupresion-adultos/Expediente_predecisional_de_informacion_clinica_pertinente_antes_de_iniciar_tratamiento_inmunosupresor_en_adultos_v1.1_2026-09-03.md)

### 3.2 Inventario, uso, propiedad e instancia

Se conservan **27 tipos paramétricos**, con propietario único en seis agrupaciones externas `(6,1,3,2,6,9)`. `contraste.json`, `profile.parameters`, contiene, para cada uno: identidad, versión, definición clínica recibida íntegra, interpretación de presencia/ausencia/indeterminación, bibliografía recibida, regla y localizador, entrada necesaria, activación, pérdida y detector, consecuencias candidatas de la raíz, correctivos, estado de configuración y estado de ligadura. La bibliografía clínica se recibe del expediente identificado; este retorno no pretende haber revalidado sus recomendaciones ante fuentes clínicas nuevas.

| N.º y parámetro | Propietario y regla recibida | Entrada necesaria y configuración |
| --- | --- | --- |
| 1. `PAR-IMMUNO-START-PLAN-DOC-001` — Inicio programado del tratamiento inmunosupresor | `M-CTX-AUTH-001`; `I_START_PLAN_DOC_v0.1`, [IMM-G5-27 §3](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_cierre_exhaustivo_G3-G5_raices_omitidas_y_SEM-MOD-007_OP-IMM-001_v0.1_2026-09-03.md) | propuesta, intención, fecha/intervalo, precisión, estado y autor. Dependencias por instancia; ejecución SV no acreditada. |
| 2. `PAR-BASE-DX-DOC-001` — Diagnóstico de base vinculado a la propuesta | `M-CTX-AUTH-001`; `I_BASE_DX_DOC_v0.1`, [IMM-G5-27 §4](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_cierre_exhaustivo_G3-G5_raices_omitidas_y_SEM-MOD-007_OP-IMM-001_v0.1_2026-09-03.md) | diagnóstico profesional verificado, código/sistema/versión, vigencia y vínculo a propuesta. Dependencias por instancia; ejecución SV no acreditada. |
| 3. `PAR-EPISODE-LEAD-DOC-001` — Responsable clínico principal del episodio | `M-CTX-AUTH-001`; `I_EPISODE_LEAD_DOC_v0.1`, [IMM-G5-27 §5](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_cierre_exhaustivo_G3-G5_raices_omitidas_y_SEM-MOD-007_OP-IMM-001_v0.1_2026-09-03.md) | profesional/servicio, función, periodo y acto de atribución de responsabilidad. Dependencias por instancia; ejecución SV no acreditada. |
| 4. `PAR-IMMUNO-PART-DOC-001` — Participación documentada de Inmunología | `M-CTX-AUTH-001`; `I_IMMUNO_PART_DOC_v0.1`, [IMM-G5-27 §5](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_cierre_exhaustivo_G3-G5_raices_omitidas_y_SEM-MOD-007_OP-IMM-001_v0.1_2026-09-03.md) | solicitud, función consultiva, emisor/receptor, fecha y estado. Dependencias por instancia; ejecución SV no acreditada. |
| 5. `PAR-LOCAL-PROTOCOL-APPLICABLE-001` — Protocolo local aplicable | `M-CTX-AUTH-001`; `I_LOCAL_PROTOCOL_APPLICABLE_v0.1`, [IMM-G5-27 §6](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_cierre_exhaustivo_G3-G5_raices_omitidas_y_SEM-MOD-007_OP-IMM-001_v0.1_2026-09-03.md) | protocolo y versión, emisor, finalidad, población, jurisdicción y vigencia. Dependencias por instancia; ejecución SV no acreditada. |
| 6. `PAR-EXEC-CONSTRAINT-DOC-001` — Restricción material de ejecución | `M-CTX-AUTH-001`; `I_EXEC_CONSTRAINT_DOC_v0.1`, [IMM-G5-27 §6](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_cierre_exhaustivo_G3-G5_raices_omitidas_y_SEM-MOD-007_OP-IMM-001_v0.1_2026-09-03.md) | restricción institucional documentada, objeto afectado, periodo y autoridad; separada de fallo del evaluador. Dependencias por instancia; ejecución SV no acreditada. |
| 7. `PAR-GC-PLAN-SYS-001` — Glucocorticoide sistémico incluido en el plan | `M-EXP-001`; `I_GC_PLAN_SYS_v0.1`, [IMM-G5-GC §4](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Adjudicacion_atomica_G5-ATM_SEM-EXP-005_OP-IMM-001_v0.1_2026-09-03.md) | plan completo y vigente, agente/vía y N_GC_ID versionado; no administración inferida. Dependencias por instancia; ejecución SV no acreditada. |
| 8. `PAR-IGG-DEF-Q-001` — Déficit cuantitativo de inmunoglobulina G | `M-HOST-001`; `I_IGG_DEF_Q_v0.1`, [IMM-G5-10 §2](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HUE-002_a_SEM-BAR-004_OP-IMM-001_v0.1_2026-09-03.md) | IgG total, unidad, método, muestra, valor exacto, intervalo aplicable, estado/corrección, tiempo y exposición exógena. Dependencias por instancia; ejecución SV no acreditada. |
| 9. `PAR-SPL-ANAT-ABS-001` — Ausencia anatómica completa del bazo | `M-HOST-001`; `I_SPL_ANAT_ABS_v0.1`, [IMM-G5-10 §4](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HUE-002_a_SEM-BAR-004_OP-IMM-001_v0.1_2026-09-03.md) | documento profesional que adjudica ausencia completa, extensión/remanente y fecha; sin lectura automática de imágenes. Dependencias por instancia; ejecución SV no acreditada. |
| 10. `PAR-ANC-DEF-Q-001` — Déficit cuantitativo del recuento absoluto de neutrófilos | `M-HOST-001`; `I_ANC_DEF_Q_v0.1`, [IMM-G5-10 §5](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HUE-002_a_SEM-BAR-004_OP-IMM-001_v0.1_2026-09-03.md) | ANC absoluto, unidad, método, valor exacto, referencia, estado/corrección y tiempo. Dependencias por instancia; ejecución SV no acreditada. |
| 11. `PAR-IV-DEVICE-PRESENT-001` — Dispositivo intravascular presente | `M-BARRIER-001`; `I_IV_DEVICE_PRESENT_v0.1`, [IMM-G5-10 §8](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HUE-002_a_SEM-BAR-004_OP-IMM-001_v0.1_2026-09-03.md) | tipo, sitio, estado, inserción/retirada e inventario de cobertura explícita. Dependencias por instancia; ejecución SV no acreditada. |
| 12. `PAR-IMPLANT-PRESENT-001` — Implante presente | `M-BARRIER-001`; `I_IMPLANT_PRESENT_v0.1`, [IMM-G5-10 §9](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HUE-002_a_SEM-BAR-004_OP-IMM-001_v0.1_2026-09-03.md) | material, sitio, estado, implantación/retirada e inventario de cobertura explícita. Dependencias por instancia; ejecución SV no acreditada. |
| 13. `PAR-INF-HOSP-HIST-001` — Infección previa causalmente vinculada a ingreso | `M-HISTORY-001`; `I_INF_HOSP_HIST_v0.1`, [IMM-G5-20 §2](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HIS-001_a_SEM-MOD-006_OP-IMM-001_v0.1_2026-09-03.md) | episodio infeccioso, ingreso y REL-ATRIB-v0.1 con fuente/autor; no diagnóstico principal de facturación. Dependencias por instancia; ejecución SV no acreditada. |
| 14. `PAR-INF-ORGSUP-HIST-001` — Infección previa causalmente vinculada a soporte orgánico | `M-HISTORY-001`; `I_INF_ORGSUP_HIST_v0.1`, [IMM-G5-20 §2](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HIS-001_a_SEM-MOD-006_OP-IMM-001_v0.1_2026-09-03.md) | episodio, modalidad/periodo de soporte y REL-ATRIB-v0.1; UCI no lo sustituye. Dependencias por instancia; ejecución SV no acreditada. |
| 15. `PAR-OI-DOC-HIST-001` — Antecedente documentado de infección oportunista | `M-HISTORY-001`; `I_OI_DOC_HIST_v0.1`, [IMM-G5-20 §3](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HIS-001_a_SEM-MOD-006_OP-IMM-001_v0.1_2026-09-03.md) | clasificación profesional, huésped, agente/sitio, versión y REG-OI-ADM-v0.1. Registro de admisión vacío. |
| 16. `PAR-MDRO-COL-DOC-001` — Colonización vigente por microorganismo multirresistente | `M-HISTORY-001`; `I_MDRO_COL_DOC_v0.1`, [IMM-G5-20 §5](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HIS-001_a_SEM-MOD-006_OP-IMM-001_v0.1_2026-09-03.md) | colonización, organismo/método/sitio/resistencia, tabla y ventana aprobadas, cobertura del cribado. Registro de admisión vacío. |
| 17. `PAR-ACUTECARE-ENC-HIST-001` — Encuentro asistencial agudo dentro de la ventana pertinente | `M-HISTORY-001`; `I_ACUTECARE_ENC_HIST_v0.1`, [IMM-G5-20 §6](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HIS-001_a_SEM-MOD-006_OP-IMM-001_v0.1_2026-09-03.md) | episodio/encuentro, clase/estado/periodo, ventana con límites e inclusividad y cobertura. Dependencias por instancia; ejecución SV no acreditada. |
| 18. `PAR-INV-PROC-HIST-001` — Procedimiento invasivo dentro de la ventana pertinente | `M-HISTORY-001`; `I_INV_PROC_HIST_v0.1`, [IMM-G5-20 §6](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HIS-001_a_SEM-MOD-006_OP-IMM-001_v0.1_2026-09-03.md) | procedimiento verificado/invasividad/periodo, ventana con límites e inclusividad y cobertura. Dependencias por instancia; ejecución SV no acreditada. |
| 19. `PAR-DM-DOC-ACTIVE-001` — Diabetes mellitus activa y documentada | `M-MODIFIER-001`; `I_DM_DOC_ACTIVE_v0.1`, [IMM-G5-20 §7](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HIS-001_a_SEM-MOD-006_OP-IMM-001_v0.1_2026-09-03.md) | diagnóstico DM verificado, terminología y ACTIVE_v0.1 con semántica temporal aplicable. Dependencias por instancia; ejecución SV no acreditada. |
| 20. `PAR-HF-DOC-ACTIVE-001` — Insuficiencia cardiaca activa y documentada | `M-MODIFIER-001`; `I_HF_DOC_ACTIVE_v0.1`, [IMM-G5-20 §8](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HIS-001_a_SEM-MOD-006_OP-IMM-001_v0.1_2026-09-03.md) | diagnóstico HF verificado, terminología y ACTIVE_v0.1 con semántica temporal aplicable. Dependencias por instancia; ejecución SV no acreditada. |
| 21. `PAR-CKD-DOC-ACTIVE-001` — Enfermedad renal crónica activa y documentada | `M-MODIFIER-001`; `I_CKD_DOC_ACTIVE_v0.1`, [IMM-G5-20 §9](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HIS-001_a_SEM-MOD-006_OP-IMM-001_v0.1_2026-09-03.md) | diagnóstico CKD verificado, cronicidad y ACTIVE_v0.1; no eGFR aislado. Dependencias por instancia; ejecución SV no acreditada. |
| 22. `PAR-KRT-ACTIVE-001` — Tratamiento renal sustitutivo activo | `M-MODIFIER-001`; `I_KRT_ACTIVE_v0.1`, [IMM-G5-20 §9](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HIS-001_a_SEM-MOD-006_OP-IMM-001_v0.1_2026-09-03.md) | prestación o plan KRT explícito vigente, modalidad y calendario; separado de CKD. Dependencias por instancia; ejecución SV no acreditada. |
| 23. `PAR-BRONCHIECTASIS-DOC-ACTIVE-001` — Bronquiectasias activas y documentadas | `M-MODIFIER-001`; `I_BRONCHIECTASIS_DOC_v0.1`, [IMM-G5-20 §10](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HIS-001_a_SEM-MOD-006_OP-IMM-001_v0.1_2026-09-03.md) | diagnóstico profesional de bronquiectasias verificado y ACTIVE_v0.1. Dependencias por instancia; ejecución SV no acreditada. |
| 24. `PAR-RESP-SUPPORT-ACTIVE-001` — Soporte respiratorio crónico activo | `M-MODIFIER-001`; `I_RESP_SUPPORT_ACTIVE_v0.1`, [IMM-G5-20 §10](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HIS-001_a_SEM-MOD-006_OP-IMM-001_v0.1_2026-09-03.md) | prestación/plan respiratorio crónico vigente, modalidad y periodo; no oxígeno puntual. Dependencias por instancia; ejecución SV no acreditada. |
| 25. `PAR-CIRRHOSIS-DOC-ACTIVE-001` — Cirrosis activa y documentada | `M-MODIFIER-001`; `I_CIRRHOSIS_DOC_ACTIVE_v0.1`, [IMM-G5-20 §11](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HIS-001_a_SEM-MOD-006_OP-IMM-001_v0.1_2026-09-03.md) | cirrosis profesional verificada y ACTIVE_v0.1; no analítica aislada. Dependencias por instancia; ejecución SV no acreditada. |
| 26. `PAR-MALNUTRITION-ASSESS-POS-001` — Evaluación diagnóstica positiva de malnutrición | `M-MODIFIER-001`; `I_MALNUTRITION_ASSESS_POS_v0.1`, [IMM-G5-20 §12](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_iterativo_constitutivo_G3-G5_SEM-HIS-001_a_SEM-MOD-006_OP-IMM-001_v0.1_2026-09-03.md) | instrumento diagnóstico aprobado, versión/población, todos sus componentes/umbrales/lógica y evaluación completa. Registro de admisión vacío. |
| 27. `PAR-FRAILTY-ASSESS-POS-001` — Evaluación positiva de fragilidad | `M-MODIFIER-001`; `I_FRAILTY_ASSESS_POS_v0.1`, [IMM-G5-27 §8](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Expediente_cierre_exhaustivo_G3-G5_raices_omitidas_y_SEM-MOD-007_OP-IMM-001_v0.1_2026-09-03.md) | instrumento aprobado, versión/población, basalidad, componentes/regla/categoría y evaluación completa. Registro de admisión vacío. |

Las consecuencias `CON-…` enumeradas por raíz **no se adoptan automáticamente para todos sus hijos**. La definición individual y la distinción perdida de [IMM-TECH, §8.2](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/marco-tecnico-de-universos-subdominios-y-modulos/01-op-imm-001-informacion-preinmunosupresion-adultos/Marco_tecnico_de_responsabilidad_trazabilidad_reproducibilidad_y_criticidad_OP-IMM-001_v0.1_2026-09-03.md) delimitan el uso; una consecuencia de función esplénica no se atribuye a la ausencia anatómica por compartir raíz. La regla de criticidad contextual sigue pendiente de constitución cuando no exista regla aplicable identificada. No se convierte una justificación de atomicidad en veto operacional.

El mínimo documental de cobertura contabiliza los 27 miembros y todos sus usos pertinentes. Un uso no aplicable lleva causa y autoridad explícitas; no desaparece del inventario ni recibe `0`. El mínimo de una rama de ejecución depende de su operación y de las dependencias alcanzadas: determinar una exclusión ya acreditada no obliga a evaluar posteriormente todos los modificadores. Un fallo de una dependencia necesaria en la rama alcanzada impide la ejecución, sin ofrecer un perfil parcial como resultado válido.

**Instancias celulares:** no constituidas. No se asignan posiciones `(C,j)`, no se define `μ_C` a partir del orden del documento y no se crean células para acomodar el inventario. Compartición, alias y capturas alternativas necesitan una regla propia. Los estados documentales de presencia y ausencia tampoco se identifican por conveniencia con aptitud o no aptitud de un codominio celular. [LSV-F, §3.1](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/arquitectura/CONTRATO_CANDIDATO_F_DOMINIO_REPRESENTACION_Y_SUFIENCIA_POR_OPERACION_2026_09_07.md)

### 3.3 Captura, admisibilidad y transducción

Por cada entrada necesaria se exige la siguiente cadena, con contenido y versiones resolubles:

`documento externo autorizado W_j → captura φ_j → observación O_j o fallo O_j^⊥ → admisibilidad r_j → transducción τ_j, cuando esté constituida → uso y resultado`

El contrato común está en `profile.admission_contract`; cada parámetro aporta sus campos y su transductor documental recibido. No se sustituye la fuente por un nombre. La ligadura debe permitir recorrer `Parametro_ID/versión → fuente y localizador → observación → regla/configuración → instancia destinataria`, si ésta llega a constituirse. No se presume una correspondencia uno a uno por semejanza de nombres.

| Componente | Exigencia para Q0 | Estado recibido y efecto |
|---|---|---|
| `W_j` | Fuente y finalidad autorizadas; identidad, versión, contenido y contexto | Definido documentalmente por parámetro; no es acceso libre a una fuente viva |
| `φ_j` | Captura íntegra con bytes, procedencia, relación y tipo | Ejecutada sólo para archivos y paquetes sintéticos de este banco; no como captura clínica SV |
| `O_j / O_j^⊥` | Observación tipada o fallo separado | El fallo no completa una observación ni una posición con U |
| `r_j` | Población, finalidad, jurisdicción, tiempo, método, referencia y selección de fuente cuando correspondan | Configuración ausente, referente inválido o conflicto sin regla no son admisión positiva |
| `τ_j` | Regla total y determinista sobre observaciones admitidas, con partición y significado previos | Identidades de reglas recibidas; **K1-T no habilita observación → Tri para ninguno de los tres valores** |
| Ligadura | Identidad semántica, captura, regla e instancia sin ambigüedad | DFL-005 sigue pendiente; un inventario nominal no la resuelve |

No se resuelve una pluralidad de fuentes por «primera», «última» o fusión automática. Las alternativas y su selección deben estar constituidas. Una observación degradada sólo podría dar U con una regla legítima y pertenencia demostrada a su región de indeterminación; la etiqueta por sí sola no basta. [LSV-F, §3.2; LSV-IR, §2.4](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/arquitectura/CONTRATO_CANDIDATO_F_DOMINIO_REPRESENTACION_Y_SUFIENCIA_POR_OPERACION_2026_09_07.md)

### 3.4 Estados distintos y precisión de los antecedentes

| Categoría | Significado | Efecto permitido |
|---|---|---|
| Presente/ausente documental | Proposición recibida según su regla y cobertura | No es diagnóstico automático ni aptitud celular |
| U clínica legítima | La regla constituida, sobre entrada admitida, no permite clausura; causa y autoridad conservadas | Mantener la indeterminación y aplicar sólo el tratamiento de criticidad constituido |
| No aplicabilidad justificada | El uso no se activa por una condición explícita del episodio o del perímetro | Registro de causa; no `0`, no omisión silenciosa |
| Dato no admitido | La captura existe, pero no satisface la regla de admisión | No transducir; identificar causa y dependencia afectada |
| Regla/configuración no constituida | Falta una condición previa para evaluar | No emitir Tri por esa carencia; conservar la deuda documental |
| Insuficiencia representacional | La representación no acredita conservar lo que exige la consulta | Dictamen de pérdida o suficiencia no acreditada; no convertirlo en U clínica |
| Fallo técnico | Captura, contenido, referencia, ejecución o serialización técnicamente inválidos | **Ninguna salida clínica**; sólo registro técnico estructurado |

Se incorpora una precisión necesaria de precedencia: [IMM-G7, §§3, 5 y 7](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/12-rutas-en-evaluacion/G7-RUT_usos_composicion_y_rutas_OP-IMM-001_v0.1_2026-09-03.md), determinados rótulos de [IMM-CORR2](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Suceso_correctivo_configuracion_atribucion_y_vigencia_A0_OP-IMM-001_v0.1_2026-09-03.md), [IMM-G8](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/13-iti-y-laboratorio/G8-ITI_OP-IMM-001_v0.1_2026-09-03.md) y explicaciones clínicas recibidas conservaron remisiones de configuración ausente a U, o de `V-TECH-001` a `ABSTENERSE_O_ESCALAR`. **No son instrucciones de ejecución en la interfaz actual.** Rigen la separación de [IMM-TECH, §§3–4](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/marco-tecnico-de-universos-subdominios-y-modulos/01-op-imm-001-informacion-preinmunosupresion-adultos/Marco_tecnico_de_responsabilidad_trazabilidad_reproducibilidad_y_criticidad_OP-IMM-001_v0.1_2026-09-03.md), F §3.2 y la recepción §8. Los antecedentes no se borran; este contrato candidato impide reproducir esa colisión en una realización futura.

Los cuatro registros de admisión pendientes —infección oportunista, colonización resistente, malnutrición y fragilidad— siguen vacíos en el corte recibido. Permanecen los tipos constituidos y su deuda; **no se declara una ejecución que haya producido U por defecto**. Tampoco se afirma que los otros 23 sean plenamente ejecutables: conservan dependencias por instancia y la misma ausencia de ruta productiva SV.

El parámetro de restricción de ejecución distingue una **limitación institucional documentada** —hecho con fuente y autoridad— del **fallo real del evaluador**. Una limitación institucional no modifica una verdad clínica; un fallo del evaluador impide emitir el perfil. Se preserva así el significado clínico recibido sin usar ese parámetro como contenedor de errores técnicos.

### 3.5 Cuatro salidas y selección exclusiva

El codominio documental es exactamente el siguiente. Ninguna salida es consejo terapéutico ni autorización asistencial; ninguna se equipara automáticamente a `Tri`.

| Salida | Significado |
|---|---|
| `PERFIL_PREDECISIONAL_SELLADO` | Suficiencia informativa expresamente adjudicada por el médico, cumplidas las condiciones de cierre; no declara indicado, seguro ni autorizado el tratamiento |
| `U_CRITICA_NO_CERRADA` | Indeterminación clínica legítima material, crítica o pendiente de adjudicación según regla/autoridad constituidas |
| `FUERA_DE_ALCANCE` | Exclusión del ámbito positivamente establecida en una comprobación técnicamente válida |
| `ABSTENERSE_O_ESCALAR` | Condición clínica o de gobierno que impide el cierre y exige la actuación de la autoridad correspondiente; no absorbe fallos técnicos |

La selección candidata es total y no ambigua **sobre premisas ya constituidas y adjudicadas**, con la precedencia de G7 §§6–7. La tabla no constituye los detectores clínicos que producen esas premisas:

1. Una exclusión de alcance positiva selecciona `FUERA_DE_ALCANCE`.
2. Sin esa exclusión, alcance clínicamente no resuelto, identidad clínica o autoridad insuficientes, necesidad adjudicada de evaluación aguda o infección activa documentada seleccionan `ABSTENERSE_O_ESCALAR`.
3. Sin las condiciones anteriores, una U clínica material crítica o pendiente de adjudicación selecciona `U_CRITICA_NO_CERRADA`.
4. Sin las anteriores y con todas las condiciones de `R-SEAL-001` satisfechas y acto médico explícito de suficiencia, se selecciona `PERFIL_PREDECISIONAL_SELLADO`.
5. Si no concurre ninguna de las anteriores y falta el acto explícito de cierre, se conserva `ABSTENERSE_O_ESCALAR`.

Sólo se selecciona la primera condición aplicable; todas las causas y vetos detectados permanecen trazados. El rechazo técnico ocurre antes o durante cualquier paso y queda **fuera de esta tabla y de su codominio**. Una premisa cuya regla no esté constituida impide ejecutar la selección; no se fabrica su valor para hacer total un programa. La especificación está en `profile.terminal_selection`; el oráculo integrado `SP-07` queda especificado, no ejecutado.

### 3.6 Consecuencias, criticidad, supervisión y resumen

La distinción perdida, su detector documental y sus fuentes se conservan individualmente para los 27 parámetros. Cada uso activo debe enlazar su consecuencia G4 aplicable y, cuando exista, la regla operacional que fija su efecto. La criticidad es contextual: no se deduce de una etiqueta fija ni de un peso estadístico. No se constituye aquí una regla nueva de daño individual.

Un evento U legítimo debe conservar parámetro, causa, evidencia faltante, consecuencia aplicable, horizonte, posibilidad de resolución, autoridad y estado de adjudicación. La declaración humana de no criticidad conserva la U original y añade motivo, alcance, fecha, competencia y versión; no la convierte en `0`. La mera firma no sanea una ejecución inválida. El productor técnico de criticidad sigue pendiente en DFL-006. [IMM-G7, §4; IMM-TECH, §8](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/12-rutas-en-evaluacion/G7-RUT_usos_composicion_y_rutas_OP-IMM-001_v0.1_2026-09-03.md)

La composición conserva el orden y los seis propietarios de G6/G7, con los controles de alcance y posible infección activa, sin promedio, mayoría ni compensación de un veto. El resumen debe mostrar antes sus impedimentos de cierre y permitir recuperar cada dependencia necesaria: parámetro, regla, fuente, versión, U, consecuencia, autoridad y orden. La interfaz resumida se evalúa como representación propia; no basta que el dato exista en otro lugar no declarado. Las siete proyecciones clínicas recibidas no se presentan como siete `Frame` IR válidos ya realizados.

### 3.7 Identidad de ejecución, soporte y efectos

La identidad requerida es la tupla completa de [IMM-TECH, §3](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/marco-tecnico-de-universos-subdominios-y-modulos/01-op-imm-001-informacion-preinmunosupresion-adultos/Marco_tecnico_de_responsabilidad_trazabilidad_reproducibilidad_y_criticidad_OP-IMM-001_v0.1_2026-09-03.md): universo/versión, finalidad/versión, entrada canónica, fuentes, reglas, configuración, programa, dependencias, terminologías/versiones, jurisdicción, instante índice y estado humano autorizado. Cada objeto debe resolver contenido y procedencia. Un hash vincula bytes; no concede autoridad ni acredita que el almacenamiento no haya retrocedido.

La serialización candidata exige UTF-8 estricto, esquema y orden explícitos, fuentes originales intactas, decimales exactos con unidad, tiempo con zona y precisión, ventanas con extremos e inclusividad, y categorías distintas para ausencia, nulo, no aplicación, U y fallo. Una normalización Unicode sólo puede ser transformación explícita y versionada, conservando los bytes originales. No se convierte una igualdad semántica aproximada en igualdad literal.

**Toda ejecución válida con identidad completa idéntica debe producir exactamente los mismos bytes de salida canónica. Un fallo técnico no es una salida alternativa: determina que no existe ejecución clínica válida y sólo genera el registro técnico estructurado correspondiente.**

El registro técnico debe identificar ejecución o intento, fase, componente, causa, evidencia, versión y relación con operaciones afectadas. No admite `0`, `1`, U, perfil parcial, consejo ni texto improvisado como sustitutos. La realización y durabilidad de este registro integrado quedan pendientes de prueba.

El soporte efectivamente utilizado aquí es **un observador documental externo**, Node.js v24.19.0, biblioteca estándar y archivos F-IF identificados; sin consultas de red, modelos, relojes clínicos ni conectores durante los ensayos. Sus efectos son lectura de archivos y escritura de evidencia por el invocador. No constituye agente, no autentica clínicos y no confiere permiso asistencial. No existe soporte OP completo acreditado en este retorno.

## 4. Correspondencia con las construcciones disponibles del Lenguaje

La inspección se refiere a [LSV-IR](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/IR_CANONICA_BIENFORMACION_SV_v0_3.md), [LSV-TIPOS](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/rust/sv_core/src/ir.rs) y a su interpretación vigente en [LSV-F, §§3 y 6.1](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/arquitectura/CONTRATO_CANDIDATO_F_DOMINIO_REPRESENTACION_Y_SUFIENCIA_POR_OPERACION_2026_09_07.md). No se ha modificado ni compilado el Lenguaje para fabricar esta correspondencia.

| Necesidad de OP | Construcción o frontera recibida | Clasificación y evidencia |
|---|---|---|
| Inventario de 27 y mínimos por operación | `Domain.parameters` y listas de captura/admisibilidad | Obligación del perfil; J-D0 conserva nombres, DFL-005 no resuelve mínimos ni ligaduras. `GH-DOC-07`, `SP-01/02` |
| Destino de cada observación | `CaptureSpec.parameter_id`, cadenas de espacio y mapping; `AdmissibilitySpec` | Insuficiencia de ligadura completa a `(C,j)`; no asignación por ordinal. `SP-02/03` |
| Transducción clínica | `Ternarizer` nominal | Ruta productiva no habilitada para los tres valores; no extensión unilateral. `SP-03` |
| Cuatro salidas y su significado | `Codomain`, `OutputSemantics` | El catálogo tiene encaje declarativo; su existencia no implementa la selección OP. `SP-07` |
| Seis agrupaciones externas | `CellSpec`, `CellState` sólo para células constituidas | `U_NO_DECIDIDO`; no coerción de grupos a células. `NEG-07/08`, `SP-02` |
| Composición y referencia ordenada | `CompositionGraph`, `SemanticRelation`, `compose` | Composición pendiente de prueba para OP; `compose` no compone automáticamente `Agent/Domain`. `SP-02/06` |
| Proyecciones y resumen | `Horizon`, `Frame`, proyección y consultas cerradas | Reparación J-H0 recibida; insuficiente para toda derivación clínica y recuperación. `GH-DOC-01…08`, `SP-05` |
| Autoridad y adjudicación | `supervise`, `resolve`, referencias de supervisión | Representación por composición pendiente; R1 no acredita flujo material completo OP. `GH-DOC-04`, `SP-10` |
| Criticidad contextual | `Frame.criticalities`, productor superficial pendiente | Candidata a extensión bajo DFL-006; la regla clínica se constituye en su sede. `SP-04` |
| Fuente y metadatos clínicos | Referencias externas y políticas de `Domain` | Obligación de perfil/interfaz; cadenas opacas no acreditan interpretación. `GH-DOC-01/02/05/08` |
| Agente consumidor | `Agent`, `QuerySpec` | No constituido para este retorno. Ninguna cobertura universal inferida |
| Registro técnico y salida canónica | Diagnóstico/serialización más esquema del perfil y motor | Obligación de realización; no probada por paridad de proyecciones. `SP-08/09` |

**REQ-IMM-SV-011 permanece `U_NO_DECIDIDO`.** El corte aporta precisiones de identidad y controles, pero ninguna evidencia nueva que constituya las posiciones, transducción, codominio, operación y suficiencia de la agrupación de nueve miembros. La célula mínima sigue siendo `SV(9,3)`; ello no autoriza relleno, duplicación, mezcla ni células menores. La carencia no obliga a abandonar el dominio ni a remodelarlo para la máquina.

## 5. Aplicación motivada de F-IF a Q0

Se reciben las seis familias, 18 consultas y 54 filas de [LSV-FIF](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/arquitectura/F_IF_SEIS_TESTIGOS_SINTETICOS_Y_RELEVO_G_H_2026_09_07.md). Su necesidad se determina desde los consumidores de Q0, no desde la semejanza temática. En `contraste.json`, `f_if_applicability`, figuran las 18 consultas, consumidores, fuente y límite individual.

| Familia y aplicación | Consultas y necesidades | Límite y fuente |
| --- | --- | --- |
| IF-IMM-01 · APLICA_PARCIALMENTE | `Q01-unidad`: APLICA a identidad, unidad y referencia; el criterio artificial no es intervalo clínico; `Q01-correccion`: APLICA a validez/versión y enlace de sustitución del informe; `Q01-peticion`: APLICA como vínculo petición/muestra/episodio, insuficiente por sí solo | Faltan método, intervalo clínicamente aplicable y captura/transducción Q0; el producto finito IF no demuestra esos requisitos. [IMM-CLIN, §4.3, parámetros 8 y 10](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/universos-clinicos/01-evaluacion-predecisional-riesgo-infeccioso-antes-inmunosupresion-adultos/Expediente_predecisional_de_informacion_clinica_pertinente_antes_de_iniciar_tratamiento_inmunosupresor_en_adultos_v1.1_2026-09-03.md) |
| IF-IMM-02 · NO_APLICA_EN_Q0_V0 | `Q02-configuracion`: NO_APLICA; `Q02-informe`: NO_APLICA; `Q02-muestra`: NO_APLICA | El A0 recibido no consume paneles ni observación citométrica derivada. SEM-HUE-001 no suministra un parámetro citométrico adoptado. La utilidad general del patrón no crea un uso en Q0. [IMM-G6, §3](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/11-matrices-en-evaluacion/G6-MAT_propiedad_matricial_A0_OP-IMM-001_v0.1_2026-09-03.md) |
| IF-IMM-03 · NO_APLICA_EN_Q0_V0 | `Q03-informe`: NO_APLICA; `Q03-procedimiento`: NO_APLICA como consulta de médula ósea; `Q03-muestra`: NO_APLICA | No hay consumidor de médula/imagen digital. La asplenia usa documentación profesional ya adjudicada; el antecedente de procedimiento invasivo no requiere procesar médula. DICOM/LSV-030 siguen no aplicables. [IMM-CLIN, §4.3, parámetro 9, y §4.5, parámetro 18; recepción §8.4](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/universos-clinicos/01-evaluacion-predecisional-riesgo-infeccioso-antes-inmunosupresion-adultos/Expediente_predecisional_de_informacion_clinica_pertinente_antes_de_iniciar_tratamiento_inmunosupresor_en_adultos_v1.1_2026-09-03.md) |
| IF-IMM-04 · APLICA_PARCIALMENTE_COMO_DISTINCION_DOCUMENTAL | `Q04-constancia`: NO es una operación consumida: se recibe la prohibición de deducir administración desde orden; `Q04-cambio`: APLICA al estado/cambio del plan documental, sin ejecutar suspensión; `Q04-orden`: APLICA a identidad de propuesta; insuficiente sin estado, intención y versión | El contenido oncológico, resultado terapéutico y administración como ejecución están fuera de Q0. Traslado sólo de la distinción, con testigo propio GH-DOC-03; no herencia de reglas. [IMM-CLIN, §§1.2, 2.2 y parámetros 1 y 7](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/universos-clinicos/01-evaluacion-predecisional-riesgo-infeccioso-antes-inmunosupresion-adultos/Expediente_predecisional_de_informacion_clinica_pertinente_antes_de_iniciar_tratamiento_inmunosupresor_en_adultos_v1.1_2026-09-03.md) |
| IF-IMM-05 · APLICA_PARCIALMENTE | `Q05-episodio`: APLICA a identidad y periodo; no aporta por sí sola REL-ATRIB; `Q05-organizacion`: APLICA como contexto; servicio/organización no asignan autoridad ni causa; `Q05-ubicacion`: NO es una pregunta autónoma requerida; ubicación es contexto no sustituto de episodio | Q0 requiere además atribución, cobertura, autoridad y ventanas explícitas. No obliga a importar toda la familia ni a crear otro parámetro. [IMM-CORR2, §2; IMM-CLIN parámetros 3, 4 y 13–18](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/10-atomicidad-en-evaluacion/Suceso_correctivo_configuracion_atribucion_y_vigencia_A0_OP-IMM-001_v0.1_2026-09-03.md) |
| IF-IMM-06 · APLICA_A_PROCEDENCIA_Y_VIGENCIA | `Q06-historia`: APLICA a antecedentes, rectificaciones y procedencia según dependencia de cada resultado; `Q06-vigencia`: APLICA a fecha índice y reglas temporales propias, sin ventana universal; `Q06-expediente`: APLICA a identificación, insuficiente para reproducir historia | Historia previa necesaria no es seguimiento posterior al inicio. No exige toda historia clínica: sólo las dependencias declaradas. Persistencia/custodia material siguen R2/R3/R4. [IMM-TECH, §§3, 5, 8 y 11; IMM-CORR2 §6](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/d4d6c81cb9aab5194abc8e61212c0d63877a0b9c/dominios/inmunologia/marco-tecnico-de-universos-subdominios-y-modulos/01-op-imm-001-informacion-preinmunosupresion-adultos/Marco_tecnico_de_responsabilidad_trazabilidad_reproducibilidad_y_criticidad_OP-IMM-001_v0.1_2026-09-03.md) |

Para las aplicaciones parciales y de procedencia se exigen los campos por parámetro de §3.2, captura/admisión de §3.3, instante índice, regla temporal, identidad y ligadura de la instancia si se constituye. Ninguno de los testigos recibidos acredita por sí solo esas ligaduras clínicas. Se retienen las pérdidas pertinentes como necesidades de representación e interfaz.

En particular, una orden no se convierte en administración; ubicación o servicio no equivalen a episodio ni a autoridad; coincidencia temporal no constituye atribución de un ingreso; una vista vigente no reconstruye necesariamente antecedentes; disponer del hash de un informe no acredita su interpretación. Citometría, médula e imagen no se incorporan por analogía. DICOM y DICOMweb continúan no aplicables.

## 6. Testigos, pruebas ejecutadas y comprobaciones pendientes

### 6.1 Campaña F-IF recibida y reproducida

Se ejecutaron, sin modificar sus archivos ni esperados:

```sh
node tests/f_if/run.mjs
node --test tests/f_if/sensitivity.mjs
```

La primera orden reproduce exactamente la evidencia del corte: **6 familias, 48 estados documentales, 18 consultas, 54 filas; 36 juicios de suficiencia y 18 pérdidas en los espacios finitos declarados; 288 recuperaciones exactas, 144 con información lateral explícita y 24 controles técnicos**. SHA-256 de la evidencia recibida: `decaaabe1a1b166a0ef7c0764a63a9697278db97c19ba2489759fcc5173f1f8a`. La segunda orden supera **12 pruebas de sensibilidad**, sin fallos. Su salida está conservada en `ejecuciones_recibidas.json`.

La recuperación con información lateral acredita `(H,S)` en ese experimento, no H sola; el hash de S no prueba la seguridad o disponibilidad futura del soporte. Los 48 estados se construyen por el producto documental finito de F-IF; no son estados clínicos de Q0. Ninguna de sus 18 consultas se ofrece como operación SV ejecutable.

### 6.2 Ocho pares propios, relativos a necesidades documentales de Q0

Cada testigo declara exactamente dos paquetes, su espacio finito, consulta, esperados literales, representación completa F0 y reducción F1 que elimina únicamente el detalle necesario. El observador recupera desde bytes, sin conocer el identificador del estado ni consultar los esperados. Se acredita `H(x)=H(y)` y `Q_doc(x)≠Q_doc(y)`; una consulta de control sobre el contexto permanece recuperable desde esa misma reducción.

| Testigo | Distinción y operación documental | Límite |
| --- | --- | --- |
| GH-DOC-01 | Unidad, método y referencia de IgG/ANC | No permite tratar un mismo texto numérico como observación suficiente; no se compara ningún valor con un intervalo clínico. |
| GH-DOC-02 | Atribución profesional frente a mera coincidencia | Conservar el enlace adjudicado no diagnostica causalidad. Suprimirlo hace imposible consultar qué relación consta. |
| GH-DOC-03 | Estado de la propuesta, distinto de administración | Recupera la vigencia documental; no aplica pauta, suspensión ni infiere administración. |
| GH-DOC-04 | Adjudicación de una indeterminación, separada del valor | Recupera qué se escribió; las etiquetas sintéticas no prueban legitimidad clínica ni autentican al autor. No calcula criticidad. |
| GH-DOC-05 | Antecedente y enmienda frente a vista actual | La vista actual idéntica no permite recuperar historia causal/documental diferente. No acredita persistencia autoritativa. |
| GH-DOC-06 | Indeterminación clínica documentada frente a configuración no constituida | El banco recupera etiquetas exógenas, no ejecuta esa regla ni habilita nutrición; el registro admisible de OP continúa vacío. |
| GH-DOC-07 | Ligadura parámetro-observable pese a igual inventario | Ambas son cadenas documentales realizables; la segunda es una sonda de error, no una ligadura clínicamente admisible. El teorema de pérdida es documental, no clínico. Dos registros no son una célula. |
| GH-DOC-08 | Ventana y pertenencia de sus extremos | Conserva el operando temporal; no fija una ventana sanitaria, ni decide exposición clínica. |

Los paquetes son realizables como documentos sintéticos por construcción literal. **No se afirma que ambos miembros de cada par pertenezcan al espacio clínico admisible `X_Q0`**. En particular, una ligadura errónea se utiliza como sonda documental, no como paciente admisible. Por tanto, estos pares demuestran pérdidas de consultas documentales necesarias y refutan la suficiencia de ciertas simplificaciones; no constituyen un teorema de imposibilidad de Q0 ni una validación de su resultado clínico. Los testigos clínicos que requieren transducción o criticidad legítima quedan especificados.

Resultado: **16 recuperaciones positivas, 8 testigos de pérdida, 16 rechazos de recuperación tras pérdida, 16 controles positivos sobre la representación reducida y 19 mutaciones negativas rechazadas**. Se comprueban también captura inválida y no admisión por el observador recibido. Todos estos controles son documentales; no son rechazos ejecutados por el compilador SV.

### 6.3 Reproducción independiente de la evidencia local

Con los archivos de `fuentes.json` disponibles en dos directorios que conserven sus rutas de repositorio, ejecutar desde este paquete:

```sh
node verificar.mjs --inmunologia /cortes/imm --lenguaje /cortes/lsv > resultado-1.json
node verificar.mjs --inmunologia /cortes/imm --lenguaje /cortes/lsv > resultado-2.json
cmp resultado-1.json resultado-2.json
cmp resultado-1.json evidencia.json
```

Se realizaron dos invocaciones independientes. Coincidieron sus bytes y su SHA-256: **`6f66f8274a8c00351324ef153927fa8753d4b289a18188439f181449a34219af`**. La evidencia declara versión de Node, sistema y arquitectura como identidad del soporte del banco. Sus esperados son literales previos y no se regeneran desde la salida observada para obtener un resultado favorable. El verificador no lee `evidencia.json` para producir su respuesta: la comparación se realiza después.

La codificación compacta de JSON del banco conserva el orden declarado de campos; no demuestra que una futura implementación clínica normalice correctamente cualquier orden de mapa, decimal, reloj, Unicode o plataforma. Las duraciones de consola de las pruebas originales no forman parte de la evidencia canónica ni se presentan como objetivo de rendimiento.

### 6.4 Comprobaciones sólo especificadas

| Control pendiente | Positivo requerido | Negativo requerido y sede |
| --- | --- | --- |
| SP-01 · Identidad y referentes completos | Identidad completa única, todas las fuentes/reglas/entradas resolubles en la realización OP. | Cambiar hash, versión o referente; ausencia de manifiesto; la ejecución no produce salida clínica. DFL-005; interfaz/motor. |
| SP-02 · Instancias, propiedad y composición | Resolver cada ID a captura y a (C,j) si se constituye; orden de uso, régimen de compartición y μ_C explícitos. | Mismos 27 nombres con ligaduras permutadas; numerales homónimos; owner duplicado; nueve miembros sin célula. No aceptar por conteo. DFL-005; REQ-IMM-SV-011. |
| SP-03 · Admisibilidad y transducción | Partición total/disjunta B0/B1/BU sobre observaciones admitidas, con fuente, bordes y significado clínico constituido. | Bottom, NotAdmitted, configuración ausente, datos fuera de población o fuente no admitida: ningún Tri por defecto. K1-T; configuración de dominio. |
| SP-04 · Consecuencia y criticidad | Cadena parámetro-uso-consecuencia-regla-contexto-autoridad con productor legítimo y testigo clínico realizable. | Cambiar contexto o autoridad; misma etiqueta de parámetro no decide criticidad; firma humana no subsana fallo. DFL-006; dominio/autoridad. |
| SP-05 · Resumen reversible por operación | Recuperar las dependencias de cada consulta OP a partir de H; o de (H,S) declarada y disponible. | Igual H con diferente fuente, U, veto, versión, orden o atribución que OP requiera. No recuperar con acceso lateral oculto. DFL-005; FFL-E; interfaz. |
| SP-06 · Orden y no compensación | Validar alcance, control, autoridad y vetos antes del resumen; una condición favorable no cancela otra material. | Invertir orden o introducir promedio/mayoría; error antes de proyección: no perfil parcial utilizable. REQ-IMM-SV-002/009; Lenguaje/motor. |
| SP-07 · Cuatro salidas exclusivas | Con premisas ya adjudicadas y técnicamente válidas, aplicar exactamente la tabla total del contrato candidato. | Dos salidas, quinta salida clínica, sellado sin acto humano o inclusión de fallo técnico en Y_OP. REQ-IMM-SV-014; Lenguaje. |
| SP-08 · Reproducción exacta de OP | Misma tupla completa en realización identificada, salida y traza canónicas byte a byte en ejecución independiente y nativo/WASM pertinentes. | Orden de mapas, locale, reloj vivo, decimal redondeado o distinta dependencia cambian salida sin nueva identidad: rechazar. REQ-IMM-SV-015; Lenguaje/motor. |
| SP-09 · Fallo técnico separado | Registro técnico tipado identifica fase, componente, versión y evidencia; ninguna salida clínica asociada a ejecución fallida. | Cortar captura, verificación, evaluación o serialización; impedir 0/1/U, abstención clínica o perfil parcial por sustitución. REQ-IMM-SV-007; Lenguaje/motor. |
| SP-10 · Autoridad, revocación y sucesión | Acto humano nuevo enlazado a antecedente, con alcance y legitimidad verificados en la misma identidad. | Nombre sin acreditación, delegación vencida, revocación o modificación del antecedente. R1 integrado; institución/motor. |
| SP-11 · Materialidad y obligaciones externas | Plan de pruebas por soporte: efecto verificado/confirmado, durabilidad, restauración, permisos y cadena de construcción según PT aplicables. | Caída, corrupción, retroceso, efecto incierto, datos sustituidos y dependencia no autorizada; pruebas materiales en sede competente. R2/R3/R4; DFL-009 en fila 9; contrato operacional fila 13. |
| SP-12 · Perímetro y relevo | Consumos limitados a Q0 v0; DICOM/citometría/médula no adoptados; Lenguaje recibe fila 7 y IMM se pausa. | Importar una familia por nombre, inferir conformidad clínica de CI o abrir otro universo/fase. Recepción §8; Director y sedes competentes. |

Estas doce comprobaciones figuran con positivo, negativo, sede y estado `SOLO_ESPECIFICADO_NO_EJECUTADO` en `testigos.json`. No hay una realización clínica Q0 admisible con la que ejecutarlas de punta a punta en el corte recibido. Cuando un control documental prueba una parte, esa parte se identifica separadamente; no se eleva el resultado a prueba integrada.

No se han ejecutado nuevas pruebas de compilador, paridad nativa/WASM, conectores clínicos, autenticación profesional, corte eléctrico, corrupción de base de datos, restauración, efectos externos, aislamiento del entorno ni conformidad regulatoria. No se obtuvieron cohortes ni datos de pacientes. **G9 sigue `NO_OBSERVABLE`, con cero conjuntos admisibles.**

## 7. Dictamen por operación y representación

| Operación o alcance | Representación examinada | Dictamen | Límite |
|---|---|---|---|
| 18 consultas F-IF | F0/F1/F2 de sus seis espacios documentales | Se reproducen 36 suficiencias y 18 pérdidas | Sólo esos espacios y consultas; ninguna ejecución clínica ni SV |
| Ocho consultas documentales propias | F0 completa transmitida por H | Fidelidad exacta en los 16 estados enumerados | Recuperación literal, sin interpretación clínica |
| Las mismas ocho consultas | F1 sin el detalle requerido | Pérdida demostrada en ocho pares | No se afirma admisibilidad clínica de ambos miembros |
| Consulta de contexto de cada par | La misma F1 reducida | Suficiente en el espacio declarado | Demuestra que una pérdida no invalida todas las operaciones |
| `OP-IMM-001 / Q0 v0` completo | Candidato documental y construcciones disponibles de Lenguaje | **Suficiencia no acreditada** | Faltan ligaduras, realización de transducción, productor de criticidad y prueba de salida/composición integrada |
| `OP-IMM-001 / Q0 v0` sobre soporte productivo | Interfaz, motor, persistencia y entorno | **No probado; no disponible para asistencia** | Obligaciones materiales y autorización en sus sedes; no bloquean esta devolución |

No se declara que Q0 sea irrepresentable. Se declara exactamente qué no acredita el corte recibido. Tampoco se contabiliza un «no go» clínico como producto satisfactorio: **el producto terminado de esta fase es el contraste y su devolución**, con evidencia útil y carencias localizadas, no una herramienta clínica terminada.

## 8. Adversarial interna y precisiones incorporadas

Se ha atacado el paquete después de constituir sus oráculos. La adversarial combina pruebas ejecutadas del verificador con contraste documental razonado; no se presenta como revisión externa independiente ni como auditoría regulatoria.

| Ataque | Evidencia o hallazgo | Resultado y tratamiento |
|---|---|---|
| Cambiar fuente o corte manteniendo nombre | `NEG-15/16`, hashes y blobs; cortes exactos | Rechazo ejecutado de truncamiento y sustitución. El contenido sigue vinculado al corte, sin afirmar autoridad por hash |
| Omitir G10, LSV o un enlace múltiple | `NEG-01/02/03` | Rechazos ejecutados; 15/44/81 conservados |
| Tratar cada enlace como equivalencia | Lectura de SV-010/LSV-014 y SV-012/LSV-013 | **Hallazgo material incorporado:** coberturas parciales y obligación G10 propia preservadas |
| Inventar referente o duplicar propiedad | `NEG-04/05/06`, `GH-DOC-07` | Rechazos documentales y pérdida de ligadura demostrada; realización nuclear pendiente |
| Convertir nueve miembros en célula | `NEG-07/08`, F §3.1 | Rechazo ejecutado de la alteración del contrato; `U_NO_DECIDIDO` conservado |
| Reducir todo el plan a glucocorticoide | IMM-CLIN §1.2; §3.1 de este contrato | **Precisión incorporada:** propuesta completa como dependencia, sin crear parámetros |
| Importar citometría, médula o DICOM | Aplicación motivada §5, `NEG-14` | Exclusión documental conservada; negativo ejecutado contra consumidor inexistente |
| Confundir causalidad con coincidencia o orden con administración | `GH-DOC-02/03` | Distinción documental recuperada; no se afirma detector clínico causal |
| Recuperar detalle sólo desde una vista resumida | `GH-DOC-01…08`, F-IF | Ocho pérdidas propias y 18 recibidas reproducidas; no acceso lateral oculto |
| Exigir que ninguna reducción pierda nada | Controles positivos de las mismas F1 | Rechazado: suficiencia depende de la consulta |
| Contar recuperación con S como suficiencia de H | 144 recuperaciones F-IF con entrada conjunta | Se atribuyen a `(H,S)`; custodia material de S no acreditada |
| Convertir falta de regla o fallo en U/abstención clínica | F §3.2 frente a antecedentes G7/G8/correctivos; `GH-DOC-06`, `NEG-09/10` | **Hallazgo material incorporado:** separación actual expresa; realización integrada pendiente |
| Etiquetar una restricción institucional como fallo real del evaluador | Comparación definición clínica, IMM-TECH §8.2 y §§3–4 | **Precisión incorporada:** hecho institucional y fallo técnico conservan categorías distintas |
| Declarar que hay 23 parámetros clínicamente ejecutables | K1-T y cuatro registros vacíos | Rechazado documentalmente; los 27 conservan falta de ligadura/realización |
| Autenticar autoridad con nombre o permitir saneamiento retrospectivo | `GH-DOC-04`, G7 §4, IMM-TECH | Recuperación documental demostrada; autenticación y efecto humano integrado sólo especificados |
| Contabilizar un testigo de error como par clínico admisible | Dominio enumerado de `GH-DOC-07` | **Límite incorporado:** pérdida documental; testigo clínico pendiente. No conclusión sobre todo `X_Q0` |
| Afirmar salida OP desde una compilación o desde este banco | F §6.1; `NEG-11`, `NEG-13` | Rechazos documentales; CI recibida y pruebas ejecutadas separadas |
| Reabrir fase o esperar a resolver desde IMM una carencia nuclear | Recepción §8.5 | Devolución ordinaria inmediata al completar el paquete; fila 7 y pausa controlada |

**Resultado de I8:** el paquete supera la adversarial **como devolución documental fiel con insuficiencias atribuidas**. No supera ni pretende sustituir las pruebas pendientes de realización clínica. Los hallazgos materiales no se convierten en «cero hallazgos»: se incorporan las precisiones anteriores y se mantienen las deudas siguientes. No se requiere una auditoría de esta adversarial para devolver el control.

## 9. Deuda atribuida, aplicabilidad de soporte y condiciones de resolución

Se conservan los identificadores recibidos. Esta tabla es el inventario de resolución del retorno, no una nueva taxonomía de requisitos.

| Referencia existente | Carencia o necesidad conservada | Responsable y condición de resolución |
|---|---|---|
| DFL-005; SV-001/002/011/012; LSV-012/025/026/039/040 | Mínimo por operación, identidad de instancia y ligaduras; composición y recuperación OP no acreditadas | **Lenguaje**, fila 7: determinar realización o delimitar insuficiencia, con referente y prueba. **Dominio**, sólo mediante retorno identificado si necesita constituir células, usos o mapeos clínicos. No se impone geometría |
| K1-T; SV-001/006/013; LSV-007/031 | Ruta productiva observación → Tri no habilitada | **Lenguaje** decide y prueba la realización subordinada a la DSL. **Dominio/institución** constituyen reglas y admisión clínica; no las elige el compilador |
| IMM-CORR2; SV-013; LSV-001/014/025 | Cuatro registros de admisión vacíos, además de ventanas, referencias y otros operandos por instancia | **Autoridades del dominio e institución**: regla/configuración concreta, población, finalidad, versión y fuente. Carencia declarada para Lenguaje; no se pide que fabrique una tabla clínica ni se espera su resolución para devolver |
| DFL-006; SV-008/010; LSV-014/016/041 | Productor de criticidad pendiente y reglas clínicas contextuales no constituidas automáticamente | **Lenguaje**: productor y trazabilidad; **dominio/autoridad clínica**: significado, condiciones y legitimidad. `SP-04/10`; una parte no resuelve la otra |
| SV-004/009/012/014; LSV-009/012/017/031 | Derivación completa del resumen, orden/veto y selección de una salida OP | **Lenguaje/motor**, con contrato del dominio: comprobar `SP-05/06/07`. Reparación J-H0 y existencia del codominio no sustituyen esas pruebas |
| SV-007/015; LSV-002/003/005/008/011/015/017 | Serialización completa, separación de fallo y reproducción literal integrada | **Lenguaje/motor**, `SP-08/09`; diagnóstico y parte técnico estructurado con identidad completa. Conformidad y paridad pertinente sobre la candidata que lo realice |
| LSV-025…029/031/037 | Captura perfilada, metadatos, procedencia, temporalidad, referencia y transformaciones | **Interfaz/motor**, bajo constitución del **dominio** y contrato decidido por **Lenguaje**. Certificado por consulta; sin reglas nuevas por semejanza de códigos |
| LSV-010/018…024; F §7/PT10 y R2 | Estado autoritativo, comprobación/efecto, interrupción, recuperación, corrupción y retroceso | **Infraestructura, motor e institución**, en su fase. Las pruebas materiales no se ejecutaron aquí. Imprescindibles antes de ofrecer la operación que dependa de ellas |
| LSV-032…038; R3/R4; Garantías I/II | Construcción, carga, aislamiento, responsabilidades y evidencia de producto | **Calidad y responsables técnicos/organizativos** en sus sedes. No se declara conformidad normativa ni se abre una auditoría universal en G/H |
| DFL-009; LSV-024/043 | Elección y viabilidad de servicio nativo remoto/Cloudflare u otro soporte | **Fila 9**, después del primer universo de Ciberseguridad. No se convierte en requisito nuevo para devolver G/H |
| SV-011 | Relación de las seis agrupaciones con células | **`U_NO_DECIDIDO`**; requiere evidencia constitutiva y de representación nueva. Nueve miembros no bastan |
| G9-EMP | Contraste empírico clínico no observable; cero conjuntos admisibles | **Dominio**, en futura actuación expresamente autorizada. Los ensayos documentales no cubren esta deuda |

### 9.1 Aplicabilidad de PT01–PT14 sin abrir infraestructura

Se recibe la matriz referida por [F, §7](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/arquitectura/CONTRATO_CANDIDATO_F_DOMINIO_REPRESENTACION_Y_SUFIENCIA_POR_OPERACION_2026_09_07.md), sin presentar sus ensayos históricos como pruebas nuevas de este paquete:

| Obligaciones | Aplicación a OP-IMM-001 |
|---|---|
| PT01/PT03 | Aplican a constitución, cobertura, permisos y enlace de versiones. El contrato los identifica; la ligadura material sigue pendiente |
| PT02/PT04/PT13/PT14 | Aplican a fuente/perfil, integridad, diagnóstico, custodia semántica, cambios y destinos. Parte documental comprobada; evidencia material no atribuida |
| PT05/PT06/PT07 | Condicionales a un futuro registro, cierre, repetición, cancelación o efecto. Q0 no ejecuta tratamiento; registrar un acto no equivale a administrar. El banco externo no acredita permisos ni efectos clínicos |
| PT08/PT09 | Aplican al soporte que procese información protegida o recursos necesarios. Aislamiento y límites productivos no probados; no se fijan presupuestos universales |
| PT10 | Aplica a conservación de fuentes, estados, historia y actos. Archivos y hashes del banco no acreditan persistencia autoritativa |
| PT11/PT12 | Aplican a dependencias e interfaces conjuntas. Aquí se fija el soporte documental; falta evidencia conjunta del soporte OP |

Una garantía imprescindible no acreditada bloquea ofrecer la operación afectada, aunque su sede sea futura. No bloquea el relevo previsto de este dictamen ni autoriza saltarse la secuencia para resolverla.

## 10. Cierre de I1–I8 y devolución del control

| Paso | Entrega y alcance alcanzado |
|---|---|
| I1 | Cortes, árboles, 44 fuentes, huellas y conformidad recibida distinguidos de pruebas nuevas; §1 y `fuentes.json` |
| I2 | 15/44/81 revisados, once ampliaciones existentes conservadas, clasificaciones por enlace y cobertura inversa; §2 y `contraste.json` |
| I3 | Contrato documental completo respecto del perímetro, 27 objetos, dependencias, estados, autoridad y cuatro salidas; §3. La incompletud de realización está identificada |
| I4 | Correspondencia con construcciones, aplicación de seis familias/18 consultas y oráculos positivos/negativos/de pérdida; §§4–7. Ejecutado y especificado separados |
| I5 | `REQ-IMM-SV-011 = U_NO_DECIDIDO`, sin adaptación geométrica; §4 |
| I6 | Regla literal de igualdad y fallo fuera del codominio; dos ejecuciones documentales idénticas; §§3.4–3.7 y 6.3. Prueba OP integrada pendiente |
| I7 | Competencias y perímetro conservados; sin agente, asistencia, datos reales, escritura en Lenguaje ni otro universo; §§3 y 9 |
| I8 | Adversarial interna con hallazgos incorporados, límites explícitos y deuda atribuida; §§8–9 |

Se entrega **un retorno ordinario fundado**, no una devolución anticipada por falta de identidad: las fuentes decisivas para este contraste fueron accesibles y verificadas. La insuficiencia de realización se pudo localizar y contrastar honestamente. No se declara un cierre favorable de Q0 ni del Lenguaje.

**La unidad del Lenguaje SV recibe ahora la fila 7.** Debe incorporar o delimitar los hallazgos de su competencia, conservar las necesidades inmunológicas y fijar la candidata siguiente con las pruebas que le correspondan. Si precisa una constitución exclusivamente clínica, solicitará un retorno acotado con objeto y evidencia. Inmunología no espera aquí a implementar esa carencia ni continúa por actualización incidental de la rama.

**Estado de salida de Inmunología: PAUSA_CONTROLADA_TRAS_DEVOLUCION_GH.** El primer universo de Ciberseguridad y cualquier fase posterior sólo pueden recibir el relevo que establezca Lenguaje conforme a la secuencia. Este paquete no inicia esas actuaciones.

## 11. Localizadores y glosario

Las referencias `IMM-…` y `LSV-…` son claves del inventario de fuentes; no nuevas autoridades. `fuentes.json` permite obtener cada texto exacto sin memoria de conversaciones. El corpus clínico conserva sus fuentes y jerarquía recibidas. Las revisiones de normativa clínica, protección de datos o producto que correspondan a una futura puesta en servicio no se declaran ejecutadas en este retorno.

| Forma | Significado en este paquete |
|---|---|
| SV | Sistema Vectorial SV |
| DSL | Lenguaje específico de dominio; autoridad formal a la que se subordina su realización |
| IR | Representación intermedia del Lenguaje; este contrato JSON externo no la sustituye |
| Q0 | Versión finita del universo de preguntas de OP-IMM-001; no todo el dominio de Inmunología |
| A0 | Inventario atómico recibido para esa operación, con 27 tipos |
| U | Indeterminación clínica legítima cuando su constitución lo permita; distinta de una insuficiencia del proceso |
| F, FFL-E, F-IF, G/H, K1-T, R2/R3/R4 | Identificadores de contratos, controles o fases recibidos; sus títulos y cortes están en el inventario |
| FHIR | Fast Healthcare Interoperability Resources, estándar de intercambio HL7; no autoridad clínica por sí mismo |
| DICOM | Digital Imaging and Communications in Medicine; no aplicable como consumo de imagen en este corte |
| WASM | WebAssembly; no se ejecutó una nueva campaña de paridad en este retorno |
| H, S | Interfaz transmitida e información lateral declarada; la suficiencia se juzga sobre la entrada realmente utilizada |
| Oráculo | Resultado y criterio de aceptación fijados antes de ejecutar la prueba |

**Huellas de los anexos:**

| Archivo | Bytes | SHA-256 |
| --- | --- | --- |
| contraste.json | 362169 | `7b7865985f5b96cc98aeb4d02430a8a480513c4ce229aaffda48589ee3481b39` |
| fuentes.json | 47862 | `58962b2136e814b907ee8266b526ea2882ab7685dadb1b7e8f35b0e8da8d2248` |
| testigos.json | 31168 | `037944fe4ca28524d7e89403d08e881462f7ec349c21e7d9127ccf4c7c7b1f62` |
| verificar.mjs | 10841 | `2dfbf3692ae4f98875ebcc2bf893c333aa5f0e0e7927d70ed7e855a0d56d537e` |
| evidencia.json | 14770 | `6f66f8274a8c00351324ef153927fa8753d4b289a18188439f181449a34219af` |
| ejecuciones_recibidas.json | 2044 | `39a67e4307326686799bef7e820fbc66964fef3360920180b6252e1997590999` |
