# Registro D0 de cobertura del dominio de inmunología

**Corte:** 31 de agosto de 2026  
**Versión:** 0.1  
**Estatuto:** documento interno de taller; no constituye ontología clínica, selección de fuentes, validación biomédica ni autorización asistencial.  
**Estado:** D0 en curso; cero repositorios adoptados; no se han creado cuentas, solicitado accesos ni descargado microdatos.

---

## 1. Corrección de alcance

El objeto ya no es comprobar exclusivamente IMMUNO-1 e IMMUNO-2. El objeto es constituir gradualmente el **dominio completo de inmunología**, sin presumir que:

1. los dos prototipos lo agotan o lo dimensionan;
2. un único repositorio puede cubrirlo;
3. la suma nominal de varios repositorios equivale a cobertura clínica;
4. la ausencia de datos elimina conocimiento profesional;
5. la presencia de datos autoriza una regla clínica;
6. la disponibilidad de agregados prueba consecuencias individuales;
7. la prioridad de un parámetro puede fijarse mediante una única cifra descontextualizada.

La unidad auditable de D0 pasa a ser:

> **recorte clínico × estrato de evidencia × población × operación declarada × fuente versionada**

D0 no se supera de una vez para toda la inmunología. Se registra por recortes y mantiene residual explícito.

---

## 2. Adversariales externas incorporadas

| Entrada | Procedencia | SHA-256 | Resultado |
|---|---|---|---|
| `f5307e05-6c78-410d-9761-a0a3e1adc6b2.md` | Grok | `98c09dd1590dd42a4aa2945e0e8f05d0dd52d176a11736d4ce5ce34f44c15ab4` | No pasa el flujo v2 como camino único; conserva precauciones locales |
| `37c77b88-c0a7-4937-8d41-4668b70e5f5c.md` | Claude | `d3d7fac464d59934814f1f9487976f25132cbc89239fe3f2f53779e240b69b5b` | Apto con reparos bloqueantes y defectos materiales |

### 2.1. Reparos convergentes adoptados en el flujo v3

- eliminación de `n=b²` como ley general;
- separación de `xᵢⱼ` —dato clínico crudo—, `sⱼ` —estado ternario— y `a₁ⱼ` —elemento de la fila constitutiva—;
- exclusión expresa de R2, IR, semántica e implementación del Lenguaje;
- sustitución del camino único por tres carriles: conocimiento profesional, evidencia y representación formal;
- D0 por recortes y con cuatro salidas: evidencia material, residual profesional, demostración formal o bloqueo;
- nueva puerta D0-L para determinar si una unidad de IA puede ver legalmente los datos;
- separación entre derecho de acceso, derecho de redistribución y declaración pública de disponibilidad;
- temporalidad dividida en fecha absoluta, orden relativo, origen temporal e identidad del origen entre estudios;
- transformaciones de desidentificación auditadas por variable;
- U sólo mediante regla versionada y autorizada, nunca por defecto de insuficiencia;
- lista de revisión degradada a instrumento de control: no es criterio de saturación;
- estado de las casillas declarado como temporal; retirada del botón de impresión y de dependencias de red;
- formulaciones de la unidad de IA convertidas en propuestas, no decisiones adoptadas.

### 2.2. Puntos que permanecen reservados al director

- reapertura, conservación o eventual redimensionamiento de los prototipos;
- estatuto técnico exacto del segundo índice de `(25,5)` y `(9,3)` según la fuente canónica;
- selección del motor de referencia;
- adopción de una fuente o cohorte;
- cualquier interfaz futura con el Lenguaje.

---

## 3. Estados de la puerta D0

| Código | Estado | Consecuencia permitida |
|---|---|---|
| `D0-E` | Existe evidencia material adecuada, accesible y versionada para el recorte | Puede iniciarse auditoría de diccionario y correspondencia paramétrica |
| `D0-R` | Conocimiento clínicamente justificado sin datos adecuados localizados | Se conserva en el inventario profesional como residual empírico |
| `D0-F` | Sólo puede construirse una demostración formal o metodológica | No se presenta como validación biomédica ni asistencial |
| `D0-B` | Acceso, licencia, granularidad o calidad incompatibles | El recorte queda bloqueado para esa fuente y ese uso |

Estos estados no son propiedades eternas del conocimiento: pertenecen a una versión, una fuente, una población y una operación declarada.

---

## 4. Estratos provisionales de evidencia

No son todavía la taxonomía clínica del dominio. Son clases de dato necesarias para comprobar si los repositorios pueden sostener afirmaciones distintas.

| ID | Estrato | Unidad dominante | Pregunta que permite comprobar |
|---|---|---|---|
| E01 | Fenotipo y episodio clínico | Paciente/episodio | Qué condición, manifestación o contexto estaba presente |
| E02 | Curso longitudinal y desenlace | Suceso/visita | Qué ocurrió antes, durante y después |
| E03 | Exposición, intervención y tratamiento | Administración/decisión | Qué se indicó, administró, suspendió o modificó |
| E04 | Laboratorio inmunológico y serología | Resultado/muestra | Qué magnitud o estado inmunológico fue medido |
| E05 | Inmunofenotipo y citometría | Célula/población/muestra | Qué poblaciones celulares y marcadores se observaron |
| E06 | Repertorio adaptativo BCR/TCR | Clon/secuencia | Qué diversidad, clonotipo o especificidad se detectó |
| E07 | Antígeno, epítopo y presentación | Interacción/ensayo | Qué reconocimiento inmunológico está documentado |
| E08 | Genética, genómica, HLA y KIR | Variante/alelo/sujeto | Qué base heredada o somática se observó |
| E09 | Transcriptómica, célula única y espacial | Célula/tejido/gen | Qué estado molecular y localización se midieron |
| E10 | Proteómica y metabolómica | Proteína/metabolito/muestra | Qué perfil molecular derivado se midió |
| E11 | Tejido, histología y atlas anatómico | Muestra/estructura | Dónde se localiza el fenómeno y con qué referencia tisular |
| E12 | Ensayo clínico y datos observacionales | Participante/cohorte | Qué evidencia comparativa o de práctica real existe |
| E13 | Farmacovigilancia y seguridad | Notificación/caso | Qué señales se notificaron, sin inferir causalidad ni incidencia |
| E14 | Registro clínico especializado | Paciente/centro | Qué fenotipos y seguimiento reúne una comunidad clínica |
| E15 | Nomenclatura y referencia | Entidad/código/secuencia | Cómo se identifica y versiona un concepto; no valida por sí solo el episodio |

---

## 5. Universo provisional de fuentes: 30 candidatos

### 5.1. Fuentes ya compiladas en A1

| ID | Fuente | Estratos candidatos | Acceso dominante | Limitación nuclear |
|---|---|---|---|---|
| R01 | ImmPort | E01–E05, E08–E12 | Público/registro/API según operación | La descripción del estudio no prueba depósito de sujetos, ensayos o valoraciones clínicas |
| R02 | ImmuneSpace | E04, E05, E09, vacunación | Público/registro; hereda estudio primario | Capa analítica; no sustituye la auditoría de ImmPort ni del estudio |
| R03 | ITN TrialShare | E01–E05, E12 | Cuenta y política del portal | Acceso y redistribución no son equivalentes; versión rectora pendiente |
| R04 | FlowRepository | E05 | Público por experimento | FCS y metadatos; no reconstruye por sí solo curso clínico |
| R05 | IEDB | E07 | Público, con reservas de terceros | Evidencia curada de epítopos; no cohorte clínica longitudinal |
| R06 | OAS | E06 | Público por unidad de datos | Repertorio BCR; contexto clínico heterogéneo o limitado |
| R07 | AIRR Data Commons / iReceptor | E06 | Heterogéneo por repositorio | Federación con condiciones y granularidades no uniformes |
| R08 | VDJdb | E06, E07 | Público; licencia por cerrar | Especificidad TCR; no episodio asistencial |
| R09 | ESID Registry | E01, E02, E08, E14 | Proyecto/contrato/centro | Centrado en errores innatos de la inmunidad; no descarga abierta general |
| R10 | USIDNET | E01, E02, E08, E14 | Agregados o consulta aprobada | Versiones y DUA no unificados en la auditoría inicial |
| R11 | REDIP / RePER | E01, E02, E08, E14 | Profesional o rol acreditado | Registro español especializado; acceso y granularidad pendientes |
| R12 | PhysioNet / MIMIC-IV | E01–E03, E12 | Acreditado y acuerdo específico | No es repositorio inmunológico; datos restringidos no pueden enviarse a IA externa |
| R13 | Vivli | E01–E04, E12 | Propuesta, revisión y posible entorno seguro | La plataforma no garantiza que exista un ensayo inmunológico concreto utilizable |
| R14 | BIFAP | E01–E03, E12 | Procedimiento AEMPS | Granularidad, enlace y permiso dependen del proyecto aprobado |

### 5.2. Fuentes añadidas para ampliar al dominio completo

| ID | Fuente | Estratos candidatos | Acceso dominante | Limitación nuclear | Fuente oficial |
|---|---|---|---|---|---|
| R15 | dbGaP | E01, E08–E10, E12 | Mayoritariamente controlado | Fenotipo/genómica individual; cada estudio y consentimiento gobiernan el uso | <https://www.ncbi.nlm.nih.gov/gap/docs/submissionguide/> |
| R16 | European Genome-phenome Archive | E01, E08–E10, E12 | Comité de acceso por conjunto | Datos genéticos, fenotípicos y clínicos sensibles; acceso decidido por cada DAC | <https://ega-archive.org/about/ega/> |
| R17 | Gene Expression Omnibus | E09 y parte de E10 | Público | Genómica funcional; metadatos clínicos variables y no necesariamente longitudinales | <https://www.ncbi.nlm.nih.gov/geo/info/overview.html> |
| R18 | Sequence Read Archive | E06, E08, E09 | Público o protegido según estudio | Almacena secuencias crudas; los ficheros de ejecución no contienen por sí solos los metadatos del sujeto | <https://www.ncbi.nlm.nih.gov/sra/docs/> |
| R19 | CZ CELLxGENE Discover | E09 | Público y descargable | Datos celulares estandarizados; no equivale a historia clínica ni desenlace | <https://cellxgene.cziscience.com/> |
| R20 | Human Cell Atlas Data Portal | E09, E11 | Público con protección diferenciada de datos sensibles | Atlas y multi-ómica celular; referencia biológica, no cobertura clínica completa | <https://data.humancellatlas.org/> |
| R21 | HuBMAP | E09, E11 | Portal público; autenticación para ingestión | Atlas de tejido humano sano; utilidad principal de referencia anatómica y espacial | <https://portal.hubmapconsortium.org/> |
| R22 | PRIDE Archive | E10 | Público por conjunto | Proteómica por espectrometría; contexto clínico y trazabilidad al episodio dependen del depósito | <https://www.ebi.ac.uk/pride/archive/> |
| R23 | MetaboLights | E10 | Estudios públicos descargables | Metabolómica transversal; no específica de inmunología ni necesariamente clínica | <https://www.ebi.ac.uk/metabolights/> |
| R24 | IPD-IMGT/HLA | E08, E15 | Público, descargas/API | Secuencias y nomenclatura oficial HLA; no cohorte ni desenlace | <https://www.ebi.ac.uk/ipd/imgt/hla/> |
| R25 | Allele Frequency Net Database | E08, E15 | Público | Frecuencias poblacionales HLA/KIR/citocinas; agregados, no sujetos individuales | <https://www.allelefrequencies.net/> |
| R26 | NCI Genomic Data Commons | E01, E08–E10, E12 | Abierto y controlado | Oncología/genómica; no agota inmunología tumoral ni respuesta a inmunoterapia | <https://gdc.cancer.gov/access-data> |
| R27 | ClinicalTrials.gov | E03, E12, metadatos de IPD | API y descarga de registros | Ofrece registro y resultados resumidos; informar un plan de IPD no entrega los microdatos | <https://clinicaltrials.gov/data-api> |
| R28 | FDA AEMS/FAERS | E03, E13 | Panel y ficheros públicos | Notificación espontánea: no demuestra causalidad, incidencia ni perfil de seguridad | <https://www.fda.gov/drugs/fda-adverse-event-monitoring-system-aems/fda-adverse-event-monitoring-system-aems-public-dashboard> |
| R29 | VAERS | E03, E13 | Público bajo condiciones de uso | Notificaciones no verificadas; una notificación no prueba que la vacuna causara el evento | <https://www.cdc.gov/vaccine-safety-systems/vaers/index.html> |
| R30 | EudraVigilance / adrreports.eu | E03, E13 | Portal público y accesos diferenciados | Reacciones sospechadas; el portal público no equivale a microdatos clínicos adjudicados | <https://www.ema.europa.eu/en/human-regulatory-overview/research-development/pharmacovigilance-research-development/eudravigilance> |

## 6. Dictamen de cobertura por estrato

| Estrato | ¿Existen fuentes candidatas? | ¿Cobertura clínica demostrada? | Riesgo dominante |
|---|---:|---:|---|
| E01–E03 clínico, curso e intervención | Sí | No | Fragmentación entre ensayos, registros y EHR; unidades y derechos incompatibles |
| E04–E05 laboratorio y citometría | Sí | No | Assay disponible sin episodio o episodio descrito sin resultados depositados |
| E06–E07 repertorio y epítopo | Sí | No | Profundidad molecular sin desenlace clínico individual |
| E08 genética/HLA/KIR | Sí | No | Datos sensibles controlados o frecuencias agregadas; no causalidad clínica por identidad |
| E09–E11 multi-ómica, célula única y tejido | Sí | No | Atlas y depósitos experimentales no sustituyen cohortes longitudinales |
| E12 ensayo/RWD | Sí | No | Acceso, población y declaración de disponibilidad varían por estudio |
| E13 seguridad | Sí | No | Notificación espontánea no permite inferir incidencia ni causalidad |
| E14 registros especializados | Sí, parcialmente auditados | No | Acceso restringido, ámbito patológico estrecho y modelos de datos heterogéneos |
| E15 nomenclatura/referencia | Sí | No aplicable | Sirve para identificar y versionar; no valida el episodio |

La existencia de candidatos en todos los estratos evita declarar un vacío absoluto. No autoriza a afirmar que la federación cubre todo el dominio: todavía no hay una sola correspondencia completa entre entidad, parámetro, episodio, dato, consecuencia y desenlace.

---

## 7. Interfaz con los futuros CSV

Cuando lleguen el CSV de parámetros y el CSV de entidades inmunológicas, no se fusionarán directamente. Se requerirán dos tablas de enlace:

### 7.1. Relación clínica

`entity_id × parameter_id × relation_type × population × temporal_window × consequence × evidence_source × review_status`

### 7.2. Cobertura empírica

`entity_id × parameter_id × episode_id × evidence_layer_id × repository_id × study_id × source_field × unit × time_origin × access_right × redistribution_right × ai_eligibility × material_count × data_status`

La prioridad 1–20 no se utilizará como clave de unión ni como prueba de importancia. Se conservarán por separado criticidad clínica, consecuencia de omisión, valor diagnóstico/operativo y prioridad de validación empírica.

---

## 8. Adversarial triple de esta ampliación

### 8.1. Sanitaria, clínica y médica

- Un atlas molecular no cubre una decisión clínica ni sus consecuencias.
- Un registro de notificaciones no prueba causalidad, incidencia ni riesgo individual.
- La ausencia de un parámetro en datos accesibles no autoriza a excluirlo del conocimiento profesional.
- La presencia de una variable no demuestra que su medición, umbral o interpretación sean válidos para otra población.
- La federación de fuentes puede ampliar observabilidad y, simultáneamente, aumentar incompatibilidad clínica.

### 8.2. Ingeniería de procesos

- «Repositorio» no es una unidad suficiente: deben identificarse estudio, release, fichero, diccionario y derecho de acceso.
- Fuentes abiertas, registradas, controladas y locales requieren rutas de trabajo distintas.
- Ningún microdato restringido puede entrar en una unidad de IA sin licencia explícitamente compatible.
- La repetibilidad puede exigir que un tercero solicite el mismo acceso; no exige redistribuir datos prohibidos.
- No se descargará material hasta existir orden, protocolo local, finalidad y registro de procedencia.

### 8.3. Lógica enlazada

- `conocimiento profesional ≠ variable observable ≠ dato depositado ≠ estado formal`.
- `cobertura de estratos ≠ cobertura del dominio`.
- `múltiples repositorios ≠ conjunto componible` si no coinciden unidad, población, origen temporal y semántica.
- `dato ausente ≠ U`; U exige regla versionada.
- `prioridad alta ≠ disponibilidad alta`; tampoco `frecuencia baja ≠ consecuencia baja`.

---

## 9. Siguiente puerta

Sin crear cuentas ni descargar datos, la siguiente ronda pública debe:

1. buscar fuentes o cohortes concretas dentro de los estratos E01–E15;
2. identificar áreas clínicas para las que sólo existen datos moleculares o agregados;
3. registrar por fuente las cuatro dimensiones jurídicas de D0-L;
4. preparar el esquema de unión con los CSV externos sin poblar relaciones clínicas por inferencia;
5. mantener como U documental cualquier licencia, versión o granularidad no comprobada.

**D0 permanece abierta. El dominio completo no está constituido ni cerrado.**
