# Adversarial, encaje técnico y solicitud de valoración de OP-IMM-001 al Lenguaje SV

**Fecha:** 3 de septiembre de 2026  
**Emisor:** dominio de Inmunología — `OP-IMM-001 / Q0 v0`  
**Destinatario:** unidad responsable del Lenguaje de computación SV  
**Repositorio emisor:** `SVperitus-dataset`, rama `dominio-inmunologia`  
**Corte del Lenguaje SV consultado:** `SV-lenguaje-de-computacion`, `main` `3c122d1f79a1fcf7f9c3f02db5e7534b4efb7c2d`  
**Naturaleza:** solicitud de valoración; no modifica el Lenguaje SV, no abre una fase suya y no autoriza desarrollo

## 1. Finalidad

Esta solicitud pide al Lenguaje SV que determine, con evidencia de su realización vigente, qué necesidades de `OP-IMM-001`:

1. puede representar o ejecutar hoy;
2. puede satisfacer mediante extensiones compatibles con su arquitectura actual;
3. dependen de fases ya previstas pero no cerradas;
4. pertenecen al motor, a conectores, a infraestructura, a gestión de calidad, a validación clínica o a la organización sanitaria y no al lenguaje;
5. deben diferirse hasta una revisión universal posterior, sin quedar ocultas ni bloquear injustificadamente el trabajo presente.

No se solicita un sistema perfecto en la primera iteración. Se solicita una delimitación rigurosa que permita continuar tanto el Lenguaje SV como el dominio de Inmunología sin presentar como disponible ninguna garantía pendiente.

## 2. Documentos de entrada

La valoración debe leer conjuntamente:

- [Expediente clínico de OP-IMM-001, versión 1.1](../../universos-clinicos/01-evaluacion-predecisional-riesgo-infeccioso-antes-inmunosupresion-adultos/Expediente_predecisional_de_informacion_clinica_pertinente_antes_de_iniciar_tratamiento_inmunosupresor_en_adultos_v1.1_2026-09-03.md);
- [Marco técnico de responsabilidad, trazabilidad, reproducibilidad y criticidad de OP-IMM-001, versión 0.1](Marco_tecnico_de_responsabilidad_trazabilidad_reproducibilidad_y_criticidad_OP-IMM-001_v0.1_2026-09-03.md);
- el presente documento;
- las especificaciones, contratos, pruebas y registros de deuda vigentes del Lenguaje SV en el corte declarado.

No se autoriza deducir capacidades desde títulos, fases abiertas o intenciones. Toda afirmación debe acompañarse de un localizador y, cuando proceda, de una prueba reproducible.

---

# Parte I. Adversarial de la conclusión previa

## 3. Tesis atacada

La conclusión sometida a ataque afirmaba que, antes de crear un segundo universo, debían completarse:

1. una infraestructura técnica transversal verificable; y
2. un expediente técnico-regulatorio específico de `OP-IMM-001`.

La preocupación que originó esa conclusión era correcta: una documentación clínica rigurosa no garantiza por sí misma persistencia, interoperabilidad, recuperación, seguridad, trazabilidad ni conformidad. Sin embargo, la precedencia absoluta propuesta puede ser errónea.

## 4. Ataques y resultado

| Ataque | Contraejemplo | Resultado |
|---|---|---|
| Bloqueo prematuro | Esperar a completar certificación, DICOM, continuidad material y validación clínica antes de constituir otro universo paralizaría la obtención de requisitos que precisamente deben informar esas soluciones | La precedencia absoluta no pasa |
| Arquitectura por una sola muestra | Diseñar toda la infraestructura desde `OP-IMM-001` podría universalizar particularidades del primer universo | Deben existir más universos antes del cierre universal |
| Traslado al lenguaje | Pedir al lenguaje copias de seguridad, responsabilidad legal o validación clínica confundiría semántica, motor, plataforma y organización | La asignación debe separarse |
| Sobredimensionamiento inicial | Exigir desde ahora alta disponibilidad, imagen médica completa o ejecución exactamente una vez aunque este universo no las utilice impondría coste sin requisito clínico constituido | Cada propiedad requiere aplicabilidad justificada |
| Deuda silenciosa | Continuar sin registrar los elementos diferidos permitiría que una ausencia futura se presentase como capacidad | Todo diferimiento debe quedar identificado y bloqueado para uso |
| Prototipo convertido en producto | Una interfaz mínima podría circular como herramienta clínica por tener buena documentación | Debe permanecer prohibido el uso real mientras falten validación y autorización |
| Duplicación de R2 | Crear en Inmunología otra teoría de persistencia ignoraría el contrato `SEC.0-M` y la fase R2 del Lenguaje SV | Inmunología debe aportar requisitos y casos de fallo, no un segundo núcleo |
| Universalidad prematura | Pretender fijar hoy todos los metadatos y terminologías internacionales desconoce jurisdicciones, versiones y nuevos universos | Debe fijarse un perfil mínimo versionado y conservar la deuda universal |
| Excusa de fase futura | Etiquetar todo como «revisión final» dejaría sin contrato el desarrollo actual | Hay un mínimo obligatorio presente |
| Regulación congelada | Esperar al final para considerar clasificación, calidad o riesgos generaría una reconstrucción retrospectiva inaceptable | El expediente regulatorio debe crecer desde ahora, aunque no se cierre |

## 5. Dictamen adversarial

**La conclusión previa NO PASA en su precedencia absoluta.** Pasa reformulada del modo siguiente:

> Antes de presentar `OP-IMM-001` como herramienta o de utilizarlo con datos reales deben completarse y demostrarse las garantías aplicables. Antes de continuar la constitución de otros universos sólo es obligatorio fijar el contrato de encaje, asignar responsabilidades, declarar capacidades y deudas, conservar trazabilidad de requisitos y prohibir el uso de toda función no demostrada.

La estrategia correcta tiene tres horizontes:

| Horizonte | Obligación |
|---|---|
| Ahora | Interfaz mínima, identidad, separación de fallos, trazabilidad de requisitos, registro de deudas y prohibición de uso clínico |
| Desarrollo incremental | Materialización y prueba de capacidades conforme aparezcan universos y riesgos concretos |
| Revisión universal | Armonización transversal, clasificación regulatoria final, interoperabilidad internacional completa, validación clínica, seguridad operacional y expediente de autorización |

La revisión universal deberá realizarse cuando el preprint haya pasado por revisión por pares y exista un conjunto suficiente de universos, implementaciones y objeciones externas. No podrá utilizarse esa espera para borrar requisitos ya conocidos.

---

# Parte II. Encaje técnico preliminar

## 6. Estado del Lenguaje SV leído

En el corte `3c122d1f79a1fcf7f9c3f02db5e7534b4efb7c2d`, el repositorio declara:

- gramática canónica 0.2 y perfiles fuente explícitos SVP-ES/SVP-EN;
- IR canónica 0.3;
- núcleo Rust compartido por destino nativo y WebAssembly;
- selección explícita de perfil, sin autodetección ni caída silenciosa;
- huella de los bytes fuente originales;
- R0 cerrado;
- R1 cerrado para autoridad, mediación, decisiones protegidas y trazas intra-proceso;
- R2 abierto para persistencia y continuidad material;
- R3 y R4 no iniciados;
- Garantías I y II en `NO_PROBADO`;
- serializador canónico completo no acreditado en la proyección Rust vigente;
- paridad textual exacta de todos los diagnósticos no acreditada;
- `ConflictOperator` y concurrencia en régimen general pendientes.

El contrato abstracto `SEC.0-M` ya distingue estado semántico, estado técnico, persistencia, vistas, fallos parciales, retroceso, clonación, bifurcación, recursos y recuperación. R2 es, por tanto, el lugar natural para valorar continuidad material; su apertura no demuestra todavía ninguna tecnología ni propiedad física.

## 7. Encaje por responsabilidad

| Necesidad de OP-IMM-001 | Encaje preliminar | Responsable principal | Estado preliminar |
|---|---|---|---|
| Valores ternarios y abstención | Semántica y ejecución SV | Lenguaje SV | Capacidad de base existente; falta demostrar el perfil clínico |
| Separar `U` clínica de fallo técnico | Contratos diagnósticos y ejecución | Lenguaje SV + motor | Compatible y exigido; integración pendiente |
| Identidad de fuente y reglas | IR, serialización y manifiestos | Lenguaje SV + dominio | Parcial; contrato de identidad completo pendiente |
| Autoridad clínica y decisión humana | Formas protegidas y registro de autoridad | Lenguaje SV + dominio + organización | Base intra-proceso existente; despliegue pendiente |
| Trazas de derivación | Observable y registro de ejecución | Lenguaje SV + motor | Parcial intra-proceso; persistencia pendiente |
| Persistencia, recuperación y bifurcación | R2 y plataforma material | Lenguaje SV + motor + infraestructura | R2 abierto; no demostrado |
| Exactitud byte a byte de toda salida | Serializador canónico y pruebas entre destinos | Lenguaje SV | No demostrada para el conjunto requerido |
| FHIR, terminologías clínicas y DICOM | Perfiles y adaptadores externos con referencias representables | Dominio + motor/conectores | No debe incorporarse como semántica clínica universal del núcleo |
| Interpretación de imagen médica | Aplicación clínica especializada y validada | Módulo de imagen + autoridad clínica | Fuera del alcance actual de OP-IMM-001 y del núcleo lingüístico |
| Copias de seguridad, base de datos, suministro eléctrico | Arquitectura operacional | Motor, infraestructura y organización | No es función exclusiva del lenguaje; R2 debe expresar invariantes aplicables |
| Gestión de calidad y riesgos | Sistema organizativo y expediente del producto | Fabricante/proveedor | Fuera del lenguaje, aunque sus pruebas aporten evidencia |
| Clasificación y autorización | Procedimiento jurídico-regulatorio | Fabricante, organismo y autoridades | Fuera del lenguaje |
| Validación clínica | Estudios y evaluación clínica | Promotor y autoridades clínicas | Fuera del lenguaje |

## 8. Mínimo que debe resolverse ahora

Sin detener la evolución del lenguaje ni del dominio, la respuesta debe determinar si hoy pueden fijarse:

1. una envolvente versionada para identificar universo, finalidad, reglas, configuración, fuentes, terminologías, programa y entrada;
2. una representación inequívoca de resultado clínico, indeterminación clínica y ejecución técnica inválida;
3. un registro de derivación por parámetro, incluida la distinción perdida;
4. una referencia verificable a objetos externos FHIR, DICOM o terminológicos sin atribuirles autoridad semántica automática;
5. una salida canónica cuyo alcance de igualdad esté explícitamente delimitado;
6. un conjunto pequeño de casos de conformidad de `OP-IMM-001`, exclusivamente sintéticos;
7. un manifiesto de capacidades y deudas que impida confundir prototipo, compilación y aptitud clínica.

Si alguno no cabe hoy, debe decirse si requiere una extensión compatible, R2, R3/R4, SV-motor o una decisión del dominio. No se solicita implementarlo en esta respuesta.

## 9. Lo que no debe exigirse ahora como cierre

No es condición para continuar constituyendo el dominio:

- obtener certificación ISO;
- cerrar la clasificación conforme al Reglamento (UE) 2017/745 o al Reglamento (UE) 2024/1689;
- disponer de una infraestructura hospitalaria de alta disponibilidad;
- integrar imagen médica cuando ningún parámetro del universo la consume;
- demostrar utilidad o seguridad clínicas con pacientes;
- fijar todos los perfiles FHIR, terminologías y jurisdicciones del dominio internacional;
- resolver R2, R3, R4 o las Garantías I y II por anticipado;
- crear una ontología clínica universal dentro del lenguaje.

Estas materias deben permanecer en el registro de obligaciones futuras con su disparador de apertura. No pueden presentarse como cumplidas ni desaparecer por no bloquear el trabajo actual.

---

# Parte III. Solicitud formal al Lenguaje SV

## 10. Pregunta principal

¿En qué medida el Lenguaje SV vigente puede representar, comprobar y ejecutar de forma determinista el contrato de `OP-IMM-001`, y qué modificaciones, fases o componentes externos son necesarios para alcanzar progresivamente una herramienta clínica internacional, auditable y susceptible de autorización?

## 11. Forma obligatoria de la respuesta

Para cada requisito del apartado 12, la unidad del Lenguaje SV deberá asignar exactamente uno de estos estados:

| Estado | Significado |
|---|---|
| `DISPONIBLE_HOY_DEMOSTRADO` | Existe en el corte declarado y se aporta prueba y localizador |
| `REPRESENTABLE_HOY_NO_INTEGRADO` | La semántica o estructura existe, pero OP-IMM-001 todavía no la usa ni la prueba |
| `EXTENSION_COMPATIBLE_NECESARIA` | Puede añadirse sin alterar fundamentos, previa especificación y pruebas |
| `FASE_FUTURA_YA_PREVISTA` | Pertenece a R2, R3, R4 u otra fase identificada |
| `RESPONSABILIDAD_DE_OTRO_COMPONENTE` | Corresponde al motor, conector, infraestructura, dominio u organización |
| `DECISION_ARQUITECTONICA_REQUERIDA` | Existen alternativas con consecuencias materiales que debe resolver el Director |
| `NO_APLICABLE_JUSTIFICADO` | No corresponde al universo o al lenguaje, con motivo verificable |
| `NO_ADMISIBLE` | Contradice la semántica, las garantías o la separación de responsabilidades |
| `NO_DETERMINADO` | No hay evidencia suficiente; debe indicarse qué falta para resolverlo |

No se admitirán `sí`, `compatible`, `previsto` o `se puede` sin estado, alcance, evidencia y límites.

Cada fila deberá contener:

`Requisito_ID | estado | capacidad actual | localizador | prueba | límite | componente responsable | dependencia | horizonte | siguiente decisión`

## 12. Requisitos que deben valorarse

### A. Identidad y determinismo

1. `REQ-IMM-LSV-001`: representar la identidad completa de ejecución definida en el marco técnico de `OP-IMM-001`.
2. `REQ-IMM-LSV-002`: conservar los bytes fuente y sus hashes sin normalización silenciosa.
3. `REQ-IMM-LSV-003`: producir una salida canónica con igualdad byte a byte para identidad de ejecución idéntica.
4. `REQ-IMM-LSV-004`: determinar qué parte de la salida ya es canónica en Rust nativo y WebAssembly y qué parte sigue limitada a la referencia Python.
5. `REQ-IMM-LSV-005`: impedir que locale, orden de mapas, reloj, plataforma, concurrencia o mensajes variables alteren la salida normativa.
6. `REQ-IMM-LSV-006`: prohibir prosa generativa libre en toda salida clínica autorizada; valorar plantillas cerradas y versionadas.

### B. Estados, fallos y cierre

7. `REQ-IMM-LSV-007`: representar sin colisión `0`, `1`, `U`, dato no admitido, regla no constituida, configuración ausente y ejecución técnica inválida.
8. `REQ-IMM-LSV-008`: garantizar que un fallo técnico nunca se transforme en `U`, `0`, `1`, consejo o perfil parcial.
9. `REQ-IMM-LSV-009`: representar bloqueo, abstención, adjudicación humana y reapertura sin reescritura retrospectiva.
10. `REQ-IMM-LSV-010`: ligar comprobación y efecto al mismo estado material para impedir decisiones sobre datos sustituidos durante la ejecución.
11. `REQ-IMM-LSV-011`: definir el comportamiento ante interrupción en cada frontera de efecto, incluido el caso de efecto externo incierto.

### C. Trazabilidad y responsabilidad

12. `REQ-IMM-LSV-012`: registrar por parámetro entradas, regla, fuentes, transformaciones, estados intermedios y resultado.
13. `REQ-IMM-LSV-013`: registrar la distinción clínica que no puede reconstruirse cuando un parámetro queda indeterminado.
14. `REQ-IMM-LSV-014`: permitir criticidad contextual sólo mediante regla clínica versionada y autoridad identificada.
15. `REQ-IMM-LSV-015`: impedir que una intervención humana sanee silenciosamente una ejecución técnicamente inválida.
16. `REQ-IMM-LSV-016`: identificar autor, organización, delegación, revisión, firma, revocación y versión de toda regla o adjudicación.
17. `REQ-IMM-LSV-017`: producir un paquete de auditoría reproducible sin depender de chats, memoria del modelo o explicación posterior.

### D. Persistencia y continuidad

18. `REQ-IMM-LSV-018`: persistencia autoritativa de estados, decisiones, fuentes, configuraciones y trazas.
19. `REQ-IMM-LSV-019`: recuperación después de caída de proceso, sistema o suministro sin fabricar continuidad.
20. `REQ-IMM-LSV-020`: detección de escritura parcial, corrupción, retroceso, clonación y bifurcación.
21. `REQ-IMM-LSV-021`: distinción entre copia, réplica, vista, respaldo y estado autoritativo.
22. `REQ-IMM-LSV-022`: política para reanudación, repetición idempotente y efecto externo de estado incierto.
23. `REQ-IMM-LSV-023`: asignación entre R2, SV-motor, almacenamiento, sistema operativo y organización sanitaria.
24. `REQ-IMM-LSV-024`: requisitos mínimos que el lenguaje debe imponer a una plataforma sin prescribir prematuramente una tecnología.

### E. Interoperabilidad clínica y metadatos

25. `REQ-IMM-LSV-025`: representar referencias externas con sistema, versión, código, URI, jurisdicción, vigencia y hash cuando proceda.
26. `REQ-IMM-LSV-026`: indicar qué metadatos deben formar parte de la semántica y cuáles deben permanecer en perfiles o conectores.
27. `REQ-IMM-LSV-027`: encaje con FHIR `Provenance` y `AuditEvent` sin identificar transporte con verdad clínica.
28. `REQ-IMM-LSV-028`: encaje de `Encounter`, `EpisodeOfCare`, `CareTeam`, `Observation`, `DiagnosticReport`, `ServiceRequest` e `ImagingStudy` como referencias externas perfiladas.
29. `REQ-IMM-LSV-029`: representación versionada de SNOMED CT, LOINC, UCUM, ICD-11 y terminologías locales, incluidas equivalencias no exactas y códigos retirados.
30. `REQ-IMM-LSV-030`: determinar si DICOM y DICOMweb deben ser opacos para el núcleo, verificables por hash y UID, o requieren alguna forma nueva.
31. `REQ-IMM-LSV-031`: impedir que el lenguaje interprete imágenes, códigos o informes sin una regla clínica constituida.

### F. Seguridad, calidad y regulación

32. `REQ-IMM-LSV-032`: identificar qué evidencias técnicas puede aportar el lenguaje a ISO 13485, ISO 14971, IEC 62304, IEC 81001-5-1, ISO/IEC 27001 e ISO/IEC 42001, sin declarar conformidad.
33. `REQ-IMM-LSV-033`: identificar qué obligaciones quedan necesariamente fuera del repositorio del lenguaje.
34. `REQ-IMM-LSV-034`: aportar trazabilidad entre requisito, riesgo, control, código, prueba y versión cuando corresponda al lenguaje.
35. `REQ-IMM-LSV-035`: cadena de construcción, dependencias, artefactos, distribución y carga; indicar relación con R3/R4 y Garantías I/II.
36. `REQ-IMM-LSV-036`: aislamiento de secretos, datos clínicos y registros; indicar límites del lenguaje y necesidades del entorno.
37. `REQ-IMM-LSV-037`: conservación, minimización y seudonimización sin degradar la trazabilidad clínica autorizada.
38. `REQ-IMM-LSV-038`: criterios técnicos que deben cumplirse antes de retirar la prohibición de usar datos reales.

### G. Producción incremental

39. `REQ-IMM-LSV-039`: proponer el mínimo experimento sintético de integración de los 27 parámetros que no abra uso clínico.
40. `REQ-IMM-LSV-040`: indicar qué subconjunto puede ensayarse hoy sin tocar gramática o IR.
41. `REQ-IMM-LSV-041`: identificar cualquier necesidad que obligue a cambiar gramática, IR, catálogo diagnóstico o serialización.
42. `REQ-IMM-LSV-042`: separar cambios reversibles de decisiones arquitectónicas difíciles de revertir.
43. `REQ-IMM-LSV-043`: estimar dependencias y orden técnico, no fechas ni compromisos de producción.
44. `REQ-IMM-LSV-044`: proponer puntos de revisión que permitan seguir constituyendo universos sin cerrar prematuramente la infraestructura universal.

## 13. Preguntas de bisturí

La respuesta deberá contestar expresamente:

1. ¿Puede la IR 0.3 representar los 27 parámetros, sus fuentes, su resultado ternario y la pérdida de distinción sin crear tipos nuevos?
2. ¿Puede representar la ejecución técnicamente inválida fuera de `Tri` con el detalle requerido?
3. ¿Qué objeto vigente conserva hoy la identidad completa de entrada, reglas, configuración, fuentes y programa?
4. ¿Qué salida es actualmente canónica y cuál no?
5. ¿Qué traza sobrevive hoy al proceso y cuál depende de R2?
6. ¿Qué parte de R2 puede reutilizar directamente los casos de fallo de `OP-IMM-001`?
7. ¿FHIR, DICOM y las terminologías deben tratarse como perfiles externos, dependencias persistentes, tipos de IR o combinaciones de ellos?
8. ¿Dónde reside la frontera exacta entre Lenguaje SV y SV-motor?
9. ¿Qué requisito de esta solicitud contradice o fuerza indebidamente la arquitectura vigente?
10. ¿Cuál es la integración mínima útil que puede demostrarse ahora sin afirmar aptitud clínica?

## 14. Estrategia de respuesta y desarrollo

Se solicita una respuesta en tres capas:

### 14.1 Hoy

- inventario probado de capacidades;
- mapa de encaje de los 44 requisitos;
- experimento sintético mínimo, si es admisible;
- deudas y prohibiciones que deben permanecer visibles.

### 14.2 Desarrollo próximo

- dependencias con R2 y SV-motor;
- extensiones compatibles necesarias;
- pruebas de conformidad y de regresión que deberían añadirse;
- decisiones que requieren autorización del Director.

### 14.3 Revisión universal futura

- materias que sólo pueden cerrarse tras revisión por pares del preprint, más universos y evidencia empírica;
- interoperabilidad internacional completa;
- arquitectura material y de despliegue;
- clasificación regulatoria y expediente de calidad;
- validación clínica, seguridad y vigilancia;
- Garantías I y II y fases que resulten aplicables.

La tercera capa no debe bloquear las dos primeras, pero tampoco puede omitirse.

## 15. Entregable solicitado

Un único documento de valoración, sin modificar código, gramática, IR ni estados de fase, que contenga:

1. identidad exacta del corte leído;
2. tabla completa de los 44 requisitos;
3. respuestas a las diez preguntas de bisturí;
4. arquitectura de encaje Lenguaje–motor–dominio–infraestructura–organización;
5. capacidades actuales demostradas;
6. carencias actuales y fase responsable;
7. propuesta mínima de integración sintética;
8. decisiones reservadas al Director;
9. riesgos de sobreingeniería y de infradiseño;
10. dictamen final: `ENCAJA`, `ENCAJA_CON_CAMBIOS`, `NO_ENCAJA` o `NO_DETERMINADO`, con alcance.

## 16. Prohibiciones de la valoración

La unidad receptora no debe:

- declarar conformidad clínica o regulatoria;
- abrir R2, R3, R4 o una garantía mediante esta respuesta;
- implementar cambios sin autorización posterior;
- convertir un fallo técnico en `U`;
- introducir semántica clínica por conveniencia técnica;
- presumir que todos los universos tendrán los mismos requisitos;
- exigir que toda la arquitectura universal quede terminada ahora;
- relegar una deuda conocida al futuro sin identificador, responsable y disparador;
- confundir compilación, representación o prueba sintética con seguridad clínica;
- generar documentos auxiliares cuya única función sea recibir o confirmar la respuesta.

## 17. Criterio de aceptación de la respuesta

La respuesta será aceptable si permite decidir, sin inferencias:

- qué puede hacerse hoy;
- qué no puede hacerse hoy;
- qué debe cambiar en el lenguaje;
- qué corresponde a otro componente;
- qué puede diferirse sin riesgo de olvido;
- y cuál es el siguiente paso mínimo que produce evidencia real.

Una relación de aspiraciones, una colección de nombres de normas o una promesa de compatibilidad no pasa.

## 18. Estado resultante

```text
OP-IMM-001_CLINICA_DOCUMENTAL = CONSTITUIDA_EN_SU_ALCANCE
OP-IMM-001_USO_CON_DATOS_REALES = PROHIBIDO
OP-IMM-001_INTEGRACION_LENGUAJE = PENDIENTE_DE_VALORACION
LENGUAJE_SV_MODIFICADO_POR_ESTA_SOLICITUD = NO
FASE_NUEVA_ABIERTA = NO
DESARROLLO_AUTORIZADO = NO
CONTINUIDAD_DEL_DOMINIO = PERMITIDA_CON_DEUDA_VISIBLE
REVISION_UNIVERSAL_FINAL = DIFERIDA_CON_DISPARADOR_DECLARADO
```

La solicitud no impone al Lenguaje SV una solución. Le exige responder con precisión sobre su capacidad, sus límites y el encaje responsable de la necesidad clínica.
