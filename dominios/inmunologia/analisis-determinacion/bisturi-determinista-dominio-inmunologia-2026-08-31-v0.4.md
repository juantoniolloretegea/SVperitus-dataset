# Bisturí determinista para el dominio de inmunología

**Versión:** 0.4  
**Corte:** 31 de agosto de 2026  
**Estatuto:** candidata interna; no adoptada.  
**Cierre externo:** pendiente de adversarial de Grok y decisión expresa del director.  
**Ámbito:** constitución y operación segura de conocimiento inmunológico modular.  
**Fuera de alcance:** R2, IR, semántica e implementación del Lenguaje.

---

## 0. Cadena append-only de antecedentes

```text
v0.1  RECHAZADA
      Permitía justificar una salida retrospectivamente.

v0.2  INSUFICIENTE
      Constituía consecuencias de alternativas,
      pero no empezaba por las consecuencias de ignorar conocimiento obligatorio.

v0.3  INSUFICIENTE COMO CIERRE
      Incorporaba conocimiento exigido, error y consecuencias,
      pero no formalizaba completamente:
      - congelación del conocimiento;
      - clausura modular mínima;
      - matrices ternarias;
      - composición dirigida;
      - disciplina crítica de U.

v0.4  CANDIDATA ACTUAL
      Integra los cinco elementos anteriores.
```

Ninguna versión anterior se reescribe, elimina ni presenta como aprobada.

## 1. Principio rector

```text
O SABE PARA ESTA OPERACIÓN Y ESTE EPISODIO,
O NO SABE.
```

```text
NO SABER
≠ permiso para inferir
≠ permiso para aprender durante el episodio
≠ permiso para completar huecos
≠ permiso para generar una explicación convincente
≠ permiso para aconsejar
```

```text
NO SABER
→ localizar la carencia
→ determinar el error que permite
→ determinar sus consecuencias
→ informar al experto
→ bloquear, diferir o escalar según regla autorizada
```

## 2. Predicado operacional de conocimiento

Sea:

```text
M  = versión congelada del conocimiento y reglas
O  = operación clínica declarada
E  = episodio congelado
Λ  = clausura modular mínima autorizada para O,E
Kᵣ = conocimiento requerido por O,E,Λ
Kᵥ = conocimiento presente, vigente, válido y aplicable
U꜀ = estados U críticos dentro de Λ
Cᵥ = composiciones necesarias autorizadas y validadas
```

```text
SABE(M,O,E) ⇔
  Kᵣ ⊆ Kᵥ
  ∧ Cᵥ = COMPLETA
  ∧ U꜀ = ∅
  ∧ todos los controles obligatorios = PASS
  ∧ el acta predecisional de consecuencias está sellada
```

```text
IF SABE(M,O,E) = FALSE:
    NO_CONSEJO
    NO_AFIRMACIÓN_DECISORIA
    ABSTENERSE_O_ESCALAR
```

`SABE` es relativo a operación, episodio, población, escenario, ventana temporal y versión. No declara conocimiento universal de inmunología.

## 3. Congelación del conocimiento

### 3.1. Liberación operativa

```text
RELEASE_M = {
  domain_release,
  knowledge_requirements_release,
  matrix_catalog_release,
  composition_graph_release,
  rule_release,
  consequence_catalog_release,
  evidence_cutoff,
  governance_controls_release,
  canonical_renderer_release,
  release_root_hash,
  clinical_authority,
  authorization_event_id
}
```

### 3.2. Invariante durante el episodio

```text
FOR every event t in episode E:
    RELEASE_M(t) = RELEASE_M(t0)
```

Durante el episodio queda prohibido:

```text
ONLINE_LEARNING
WEIGHT_UPDATE
RULE_CREATION
RULE_REPAIR
DOMAIN_EXPANSION
MATRIX_CREATION
COMPOSITION_DISCOVERY
AUTOMATIC_MEMORY_FROM_PATIENT
AUTOMATIC_MEMORY_FROM_EXPERT_CORRECTION
UNAUTHORIZED_RETRIEVAL_TO_FILL_GAPS
```

### 3.3. Conocimiento nuevo detectado durante el episodio

```text
APPEND NEW_KNOWLEDGE_CANDIDATE
APPEND CURRENT_EPISODE_NOT_UPDATED
ABSTAIN if the candidate affects safety or admissibility

OUTSIDE CURRENT EPISODE:
  source verification
  → clinical review
  → adversarial
  → validation
  → authorization
  → new RELEASE_M+1
  → new episode
```

La corrección del inmunólogo es evidencia para revisión; no aprendizaje automático.

## 4. Representación matricial

### 4.1. Fila constitutiva

Para cada módulo formal `Cₖ`:

```text
Aᵏ = (aᵏ₁ⱼ),  j = 1,...,nₖ
Aᵏ ∈ Σ^(1×nₖ)
Σ = {0,1,U}
```

```text
|Σ^nₖ| = 3^nₖ
```

Consecuencias matemáticas:

```text
(9,3)  no es una matriz 3×3.
       Su fila formal tiene 9 posiciones.
       Su espacio ternario contiene 3^9 configuraciones.

(25,5) no es una matriz 5×5.
       Su fila formal tiene 25 posiciones.
       Su espacio ternario contiene 3^25 configuraciones.
```

El segundo componente de los descriptores canónicos no se redefine en este documento. Su estatuto exacto permanece vinculado a la fuente canónica y a la autoridad competente.

### 4.2. Elemento formal

```text
aᵏ₁ⱼ = {
  element_id,
  matrix_id,
  row_index = 1,
  column_index = j,
  clinical_knowledge_id,
  admissibility_rule_id,
  constitution_rule_id,
  consequence_if_ignored_ids[],
  criticality_class,
  input_interface_ids[],
  output_interface_ids[],
  validation_ids[]
}
```

El valor `{0,1,U}` sólo se constituye mediante regla autorizada. No se asigna por semejanza, probabilidad, completado lingüístico ni decisión libre del modelo.

## 5. Contrato de módulo formal

```text
Cₖ = {
  matrix_id,
  matrix_release,
  Aᵏ,
  bounded_clinical_domain,
  permitted_operations[],
  required_knowledge_ids[],
  admitted_input_types[],
  emitted_output_types[],
  rule_ids[],
  consequence_ids[],
  residual_ids[],
  criticality_map,
  U_policy,
  input_interfaces[],
  output_interfaces[],
  validation_scope,
  clinical_authority,
  content_hash
}
```

Un módulo no puede declarar capacidad fuera de `bounded_clinical_domain` ni ejecutar una operación no incluida en `permitted_operations`.

## 6. Clausura modular mínima

### 6.1. Grafo autorizado

```text
Gᶜ = (C, T)

C = módulos formalmente autorizados
T = interfaces de composición autorizadas
```

### 6.2. Semillas de operación

```text
SEED(O,E) = módulos declarados por regla clínica
            como necesarios para iniciar la operación O
            en el episodio E.
```

### 6.3. Clausura

```text
Λ(O,E) = least authorized closure containing SEED(O,E)
         and every declared dependency required by their interfaces.
```

Condiciones simultáneas:

```text
MINIMALITY:
  ningún módulo ajeno a una dependencia autorizada entra en Λ.

SUFFICIENCY:
  ninguna dependencia obligatoria queda fuera de Λ.

VERSION_IDENTITY:
  todos los módulos e interfaces pertenecen a RELEASE_M.
```

```text
IF MINIMALITY fails:
    reject GLOBAL_OR_EXCESSIVE_ACTIVATION

IF SUFFICIENCY fails:
    reject UNSAFE_UNDERCOVERAGE
```

La clausura evita:

```text
activar todo el dominio → ruido, coste y abstención permanente;
activar menos de lo exigido → omisión clínica peligrosa.
```

## 7. Composición dirigida y tipada

### 7.1. Interfaz

```text
Tᵢⱼ = {
  interface_id,
  source_matrix_id = Cᵢ,
  target_matrix_id = Cⱼ,
  source_output_element_ids[],
  target_input_element_ids[],
  type_contract,
  admissibility_rule_ids[],
  transfer_rule_ids[],
  order,
  preconditions[],
  postconditions[],
  consequence_ids[],
  failure_consequence_ids[],
  validation_ids[],
  interface_release,
  clinical_authority,
  content_hash
}
```

### 7.2. Operación

```text
Cᵢ ⊙[Tᵢⱼ] Cⱼ
```

Sólo existe si:

```text
source types match
∧ target types match
∧ direction is authorized
∧ order is authorized
∧ preconditions hold
∧ transfer rule is deterministic
∧ consequences are constituted
∧ validation scope matches E,O
```

### 7.3. No conmutatividad por defecto

```text
Cᵢ ⊙ Cⱼ ≠ Cⱼ ⊙ Cᵢ
```

La igualdad sólo puede declararse mediante prueba y autorización específicas.

### 7.4. Paradas de composición

```text
UNREGISTERED_INTERFACE
TYPE_MISMATCH
WRONG_DIRECTION
WRONG_ORDER
PRECONDITION_FAILURE
UNVALIDATED_TRANSFER
CONSEQUENCE_NOT_CONSTITUTED
RELEASE_MISMATCH
```

Cualquiera de ellas produce:

```text
APPEND COMPOSITION_REJECTED
ABSTENERSE
```

La IA no ensaya rutas alternativas de composición durante el episodio.

## 8. Disciplina de U

### 8.1. Constitución válida

```text
U(aᵏ₁ⱼ) is valid only if:
  authorized_rule_id exists
  ∧ rule applies to E,O
  ∧ U_reason_id exists
  ∧ consequence_ids are attached
  ∧ criticality_class is attached
  ∧ resolution_or_escalation_route exists
```

### 8.2. Prohibiciones

```text
U ≠ missing datum by identity
U ≠ retrieval failure
U ≠ model uncertainty phrase
U ≠ low probability
U ≠ disagreement hidden
U ≠ convenient abstention without consequence
U ≠ permission to continue
```

### 8.3. U dentro y fuera de la clausura

```text
U_ACTIVE = { U(aᵏ₁ⱼ) | Cₖ ∈ Λ(O,E) }

U_CRITICAL = { u ∈ U_ACTIVE |
               u.criticality_class blocks O
               OR u intersects a mandatory dependency path }
```

```text
IF U_CRITICAL ≠ ∅:
    APPEND CRITICAL_NONCLOSURE
    INFORM consequences
    ABSTENERSE_OR_ESCALAR according to authorized rule
```

```text
U outside Λ(O,E):
    remains registered
    does not invalidate O by identity
```

### 8.4. U cómoda de motor

```text
IF a model emits U without rule, reason, consequence and route:
    APPEND UNAUTHORIZED_U
    APPEND ENGINE_NONCONFORMITY
    exclude that engine result from the episode
    ABSTENERSE if no conforming governed result remains
```

No se utiliza una tasa global de U como sustituto de su análisis local y crítico.

## 9. Conocimiento exigido y consecuencias de ignorancia

Para cada `knowledge_requirement_id` activo:

```text
KNOWLEDGE_STATUS =
  PRESENT_VALID
  PRESENT_PARTIAL
  ABSENT
  UNKNOWN
  CONTRADICTED
  OUTDATED
  NOT_APPLICABLE
```

Si el estado no es `PRESENT_VALID` ni `NOT_APPLICABLE`:

```text
knowledge defect
→ authorized failure modes
→ affected decision/action
→ patient consequences
→ expert consequences
→ system consequences
→ control or stop
```

### 9.1. Modos mínimos de error

```text
MISSED_DISEASE
FALSE_EXCLUSION
FALSE_INCLUSION
MISCLASSIFICATION
INAPPROPRIATE_TREATMENT
OMITTED_NECESSARY_TREATMENT
CONTRAINDICATED_TREATMENT
MISSED_INTERACTION
WRONG_TIMING
MISSED_ESCALATION
INADEQUATE_MONITORING
MISSED_COMPLICATION
FALSE_REASSURANCE
UNSUPPORTED_CERTAINTY
```

### 9.2. Consecuencias clínicas mínimas que el catálogo debe poder representar

```text
disease_not_detected
disease_detected_late
disease_inappropriately_treated
necessary_treatment_omitted
avoidable_toxicity
avoidable_interaction
lost_therapeutic_window
complication_not_prevented
follow_up_failure
irreversible_harm
hospitalization
disability
death
```

La inclusión de un tipo no afirma que ocurra en un caso concreto. Cada relación exige regla, evidencia, población, escenario y autoridad.

## 10. Consecuencias de alternativas

```text
Aᵛ(O,E) = conjunto cerrado y versionado de alternativas autorizadas
```

Cuando sean clínicamente admisibles debe considerar:

```text
ACTUAR
NO_ACTUAR
DIFERIR
OBTENER_INFORMACIÓN_ADICIONAL
ESCALAR
```

Para cada `a ∈ Aᵛ`:

```text
CONSEQ(a) = {
  intended_effects[],
  direct_harms[],
  omission_harms[],
  delay_harms[],
  irreversible_harms[],
  contraindications[],
  interactions[],
  monitoring_requirements[],
  patient_consequences[],
  expert_consequences[],
  system_consequences[],
  singular_cases[],
  unknowns[],
  residual[]
}
```

```text
NO free weighting
NO free scoring
NO narrative tie-break
NO priority 1–20 as decision function
```

Alternativas incomparables permanecen incomparables. El sistema no inventa una preferencia.

## 11. Núcleo determinista y papel de la IA

### 11.1. Núcleo

El núcleo consume exclusivamente:

```text
frozen facts
external time as explicit typed data
third-party statistical results with source and scope
authorized matrices
authorized interfaces
authorized rules
authorized consequences
authorized governance controls
```

```text
TIME is not an internal primitive.
STATISTICS is not an internal primitive.
```

El tiempo externo puede ordenar o contextualizar hechos únicamente mediante campos explícitos y reglas versionadas. Un resultado estadístico externo conserva método, población, fecha, incertidumbre y procedencia; no sustituye el dato singular ni autoriza por sí mismo una decisión.

Produce:

```text
canonical identifiers
matrix states
composition events
consequence relations
stop codes
predecision record
```

### 11.2. Unidad de IA auxiliar

Puede:

```text
locate candidate source material
map language to existing canonical identifiers
detect candidate contradictions for governed verification
display existing objects
```

El acceso de la unidad de IA a datos queda además subordinado a la puerta jurídica y técnica D0-L. Los datos restringidos no se exponen a una IA externa por defecto.

No puede:

```text
learn online
infer missing clinical knowledge
create facts
create rules
create matrices
create interfaces
discover compositions
assign U freely
invent consequences
weight alternatives
close contradictions
select a decision outside authorized rules
render unbound clinical prose
```

### 11.3. Potencia computacional

```text
MORE_MODELS
MORE_PARAMETERS
MORE_TOKENS
MORE_AGENTS
MORE_COMPUTE
MORE_DATA_CENTRES
```

no implica:

```text
MORE_AUTHORIZED_KNOWLEDGE
MORE_CLINICAL_COMPETENCE
MORE_VALIDITY
MORE_SAFETY
PERMISSION_TO_INFER
```

## 12. Paridad entre motores

Todas las unidades reciben:

```text
same episode hash
same RELEASE_M
same Λ(O,E)
same matrices
same interfaces
same rules
same consequence catalog
same canonical output schema
```

Resultado canónico:

```text
ENGINE_RESULT(e) = {
  mapped_fact_ids,
  active_matrix_ids,
  active_element_ids,
  composition_event_ids,
  knowledge_status_ids,
  U_ids,
  consequence_ids,
  contradiction_ids,
  stop_codes
}
```

```text
PARITY(e₁,e₂) ⇔
canonicalize(ENGINE_RESULT(e₁))
= canonicalize(ENGINE_RESULT(e₂))
```

```text
IF PARITY = FALSE:
    APPEND ENGINE_DIVERGENCE
    ABSTENERSE
```

La interfaz clínica se genera desde objetos canónicos. No se encarga a cada IA una versión verbal.

## 13. Secuencia predecisional obligatoria

```text
t00 REQUEST_RECEIVED
t01 RELEASE_LOCKED
t02 EPISODE_SNAPSHOT_FROZEN
t03 OPERATION_DECLARED
t04 SEED_MODULES_SELECTED
t05 MINIMAL_CLOSURE_CONSTITUTED
t06 CLOSURE_SUFFICIENCY_VERIFIED
t07 REQUIRED_KNOWLEDGE_ENUMERATED
t08 KNOWLEDGE_STATUS_CONSTITUTED
t09 MATRIX_ELEMENTS_CONSTITUTED
t10 COMPOSITIONS_EXECUTED
t11 U_CRITICALITY_EVALUATED
t12 IGNORANCE_FAILURE_MODES_CONSTITUTED
t13 ERROR_CONSEQUENCES_CONSTITUTED
t14 ALTERNATIVE_CONSEQUENCES_CONSTITUTED
t15 GOVERNANCE_CONTROLS_EXECUTED
t16 ENGINE_PARITY_VERIFIED
t17 PREDECISION_RECORD_SEALED
t18 EXPERT_INFORMATION_RENDERED
t19 EXPERT_DECISION_APPENDED
t20 EPISODE_OUTPUT_SEALED
```

```text
t00 < t01 < ... < t20
```

```text
IF any fact, rule, matrix, composition, consequence or control
is added after t17:
    current episode is not repaired
    APPEND REOPEN_REQUIRED
    OPEN new episode_id
```

## 14. Acta predecisional

```text
PREDECISION_RECORD = {
  record_id,
  episode_id,
  release_root_hash,
  patient_snapshot_hash,
  declared_operation,
  seed_matrix_ids[],
  active_closure_matrix_ids[],
  closure_proof_hash,
  required_knowledge_root_hash,
  knowledge_status_root_hash,
  matrix_state_root_hash,
  composition_events_root_hash,
  U_events_root_hash,
  ignorance_failure_modes_root_hash,
  error_consequences_root_hash,
  alternative_consequences_root_hash,
  governance_controls_root_hash,
  contradictions_root_hash,
  unknowns_root_hash,
  residual_root_hash,
  engine_parity_result,
  completeness_result,
  sealed_before_expert_decision = TRUE,
  clinical_authority,
  signature,
  event_hash
}
```

## 15. Información obligatoria al inmunólogo

```text
EXPERT_FRAME = {
  operation,
  active_matrices_and_order[],
  knowledge_present_valid[],
  knowledge_partial[],
  knowledge_absent[],
  knowledge_unknown[],
  knowledge_contradicted[],
  knowledge_outdated[],
  critical_U[],
  errors_enabled_by_each_defect[],
  patient_consequences[],
  expert_consequences[],
  alternative_consequences[],
  contraindications_and_vetoes[],
  singular_critical_data[],
  passed_controls[],
  failed_controls[],
  unexecuted_controls[],
  residual[],
  facts_that_would_change_admissibility[],
  predecision_record_id
}
```

No se presenta únicamente:

```text
confidence score
risk score
recommendation sentence
accept button
```

## 16. Decisión humana

```text
PERMITTED_HUMAN_EVENTS = {
  ACKNOWLEDGE_INFORMATION,
  REQUEST_ADDITIONAL_KNOWLEDGE,
  REQUEST_ADDITIONAL_DATA,
  DEFER,
  ESCALATE,
  REJECT_CANDIDATE,
  ACCEPT_CANDIDATE,
  REOPEN_AS_NEW_EPISODE
}
```

Reglas:

```text
ACKNOWLEDGE_INFORMATION ≠ ACCEPT_CANDIDATE

IF a hard clinical stop exists:
    the system remains abstained
    even if the expert acts clinically outside the system.

Expert correction:
    APPEND correction event
    current episode remains intact
    new release/episode required if operative state changes.
```

La firma registra información recibida y decisión adoptada. No transfiere automáticamente responsabilidad jurídica ni sustituye el consentimiento del paciente.

## 17. Registro append-only

```text
EVENT_i = {
  event_id,
  episode_id,
  event_type,
  actor_type,
  actor_id,
  external_time,
  payload_hash,
  previous_event_hash,
  release_root_hash,
  signature
}

EVENT_HASH_i = H(canonicalize(EVENT_i))
```

Invariantes:

```text
NO UPDATE
NO DELETE
NO OVERWRITE
NO BACKDATED INSERT
NO MUTABLE DECISION STATE
```

Corrección:

```text
CORRECTION_EVENT.corrects_event_id = prior event
prior event remains intact
```

## 18. Algoritmo integrado

```text
INPUT:
  request
  frozen episode E
  declared operation O
  authorized RELEASE_M

OUTPUT:
  GOVERNED_EXPERT_DECISION
  OR ABSTENERSE(reason_codes[])

BDI(E,O,M):

01  APPEND REQUEST_RECEIVED
02  LOCK RELEASE_M
03  FREEZE E
04  DECLARE O

05  SELECT authorized SEED(O,E)
06  CONSTITUTE Λ(O,E) from authorized dependency graph only
07  VERIFY minimality, sufficiency and version identity
08  IF verification fails:
09      APPEND CLOSURE_REJECTED
10      RETURN ABSTENERSE

11  ENUMERATE required knowledge Kᵣ for every Cₖ in Λ
12  CONSTITUTE knowledge status for every requirement

13  FOR each matrix Cₖ in authorized order:
14      CONSTITUTE every active aᵏ₁ⱼ by authorized rule
15      REJECT any model-created state

16  FOR each required interface Tᵢⱼ:
17      VERIFY type, direction, order, release and consequences
18      IF any check fails:
19          APPEND COMPOSITION_REJECTED
20          RETURN ABSTENERSE
21      EXECUTE deterministic transfer
22      APPEND COMPOSITION_EXECUTED

23  IDENTIFY every U_ACTIVE
24  VERIFY rule, reason, consequence, criticality and route
25  IF unauthorized U exists:
26      APPEND ENGINE_NONCONFORMITY
27      RETURN ABSTENERSE
28  IF U_CRITICAL exists:
29      APPEND CRITICAL_NONCLOSURE
30      CONSTITUTE its consequences
31      RETURN ABSTENERSE_OR_ESCALATE as authorized

32  FOR each active knowledge defect:
33      CONSTITUTE authorized failure modes
34      CONSTITUTE patient, expert and system consequences
35      IF a required consequence is missing:
36          APPEND CONSEQUENCE_CONSTITUTION_INCOMPLETE
37          RETURN ABSTENERSE

38  LOAD closed authorized alternatives Aᵛ
39  CONSTITUTE consequences of every alternative
40  IF alternatives or consequences incomplete:
41      APPEND ALTERNATIVE_CONTRAST_INCOMPLETE
42      RETURN ABSTENERSE

43  EXECUTE every governance control
44  APPEND every PASS, FAIL, UNKNOWN or NOT_EXECUTED
45  IF a blocking control != PASS:
46      RETURN ABSTENERSE

47  VERIFY engine parity where multiple engines participate
48  IF parity fails:
49      APPEND ENGINE_DIVERGENCE
50      RETURN ABSTENERSE

51  EVALUATE SABE(M,O,E)
52  CONSTITUTE and SEAL PREDECISION_RECORD
53  ASSERT no expert decision or advice event exists earlier
54  IF assertion fails:
55      APPEND RETROSPECTIVE_CONSTITUTION_FORBIDDEN
56      RETURN ABSTENERSE

57  RENDER EXPERT_FRAME from sealed canonical objects only
58  APPEND INFORMATION_PRESENTED
59  RECEIVE expert event
60  APPEND expert event

61  IF any operative object changes:
62      APPEND REOPEN_REQUIRED
63      OPEN new episode
64      RETURN current episode unchanged

65  SEAL episode output
66  RETURN GOVERNED_EXPERT_DECISION or recorded abstention
```

## 19. Respuesta de auditoría

No se genera un «porqué» libre.

```text
AUDIT(decision_event_id) returns existing immutable paths:

operation
→ active closure
→ matrix elements
→ ordered compositions
→ required knowledge
→ knowledge defects
→ U states
→ possible errors
→ consequences
→ alternatives
→ controls
→ information presented
→ expert decision
```

La auditoría lee lo que existía antes de decidir. No explica después ni añade razones.

## 20. Pruebas de aceptación y rechazo

```text
B01. Cambio de conocimiento durante el episodio -> REJECT.
B02. Incorporación automática de corrección experta -> REJECT.
B03. Creación dinámica de matriz -> REJECT.
B04. Interpretar (9,3) como 3×3 -> REJECT.
B05. Interpretar (25,5) como 5×5 -> REJECT.
B06. Activar todos los módulos sin necesidad -> REJECT.
B07. Omitir dependencia obligatoria -> REJECT.
B08. Componer sin interfaz registrada -> REJECT.
B09. Invertir el orden sin autorización -> REJECT.
B10. Transferir parámetro con tipo incompatible -> REJECT.
B11. U sin regla -> ENGINE_NONCONFORMITY.
B12. U sin consecuencia -> ENGINE_NONCONFORMITY.
B13. U crítica y consejo emitido -> REJECT.
B14. U fuera de la clausura bloquea todo el dominio -> REJECT.
B15. Completar conocimiento ausente por inferencia -> REJECT.
B16. Más cómputo modifica admisibilidad -> REJECT.
B17. Dos motores producen objetos canónicos distintos -> ABSTENERSE.
B18. Falta consecuencia humana de un error crítico -> REJECT.
B19. Estadística oculta caso singular crítico -> REJECT.
B20. Consejo anterior al acta predecisional -> REJECT.
B21. Explicación posterior añade una razón -> REJECT.
B22. Experto sólo recibe puntuación y botón de aceptación -> REJECT.
B23. Experto acepta pese a hard stop y el sistema emite -> REJECT.
B24. Corrección sobrescribe un suceso -> REJECT.
B25. Nueva evidencia abre nueva versión y episodio -> PASS.
B26. Misma entrada y versiones producen mismo objeto -> PASS.
B27. Motor diferente, núcleo canónico idéntico -> mismo objeto o abstención.
B28. Conocimiento no requerido para O queda fuera de Λ -> PASS si sufficiency se conserva.
B29. Carencia activa produce error y consecuencias visibles -> PASS.
B30. Actuación clínica externa del experto no falsifica salida del sistema -> PASS append-only.
```

## 21. Condición final de admisibilidad

```text
OUTPUT_ADMISSIBLE ⇔
  RELEASE_LOCKED
  ∧ NO_ONLINE_LEARNING
  ∧ MINIMAL_CLOSURE_VALID
  ∧ CLOSURE_SUFFICIENT
  ∧ MATRIX_CONSTITUTION_VALID
  ∧ ORDERED_COMPOSITIONS_VALID
  ∧ NO_UNAUTHORIZED_U
  ∧ NO_CRITICAL_U
  ∧ KNOWLEDGE_DEFECT_CONSEQUENCES_COMPLETE
  ∧ ALTERNATIVE_CONSEQUENCES_COMPLETE
  ∧ GOVERNANCE_CONTROLS_PASS
  ∧ ENGINE_PARITY
  ∧ PREDECISION_RECORD_SEALED
  ∧ EXPERT_FULLY_INFORMED
  ∧ EXPERT_DECISION_APPENDED
```

```text
IF any term = FALSE:
    ABSTENERSE
```

## 22. Fronteras que esta versión no declara resueltas

```text
F01. Catálogo completo de módulos clínicos.
F02. Contenido definitivo de cada matriz.
F03. Estatuto canónico exacto del segundo componente de cada descriptor.
F04. Catálogo definitivo de interfaces y composiciones.
F05. Reglas clínicas y consecuencias por entidad/población/operación.
F06. Umbrales de criticidad y hard stop.
F07. Corpus de validación clínica y cohortes.
F08. Régimen regulatorio concreto del producto futuro.
F09. Atribución jurídica de responsabilidad.
F10. Interfaz futura con el Lenguaje.
```

Estas fronteras no se completan por inferencia.

## 23. Referencias externas de frontera

| Referencia | Alcance utilizado |
|---|---|
| [Reglamento (UE) 2024/1689, texto consolidado](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng) | Registro, supervisión humana y obligaciones del responsable del despliegue cuando resulten aplicables; no se prejuzga la clasificación del sistema |
| [FDA, Clinical Decision Support Software, guía final de 2026](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software) | Frontera del soporte a profesionales y necesidad de que el profesional pueda revisar la base de la recomendación; jurisdicción estadounidense |
| [IMDRF/SaMD WG/N41FINAL:2017](https://www.imdrf.org/documents/software-medical-device-samd-clinical-evaluation) | Evaluación clínica de software como producto sanitario |
| [Ley 41/2002](https://www.boe.es/buscar/act.php?id=BOE-A-2002-22188) | Información clínica, opciones y autonomía del paciente |
| [Ley 44/2003](https://www.boe.es/buscar/act.php?id=BOE-A-2003-21340) | Competencia y actualización de profesionales sanitarios |

## 24. Puerta pendiente

```text
STATUS(v0.4) = CANDIDATE_INTERNAL

TO_CLOSE:
  receive Grok adversarial
  → compare attack by attack
  → append findings
  → director decides
```

Hasta entonces:

```text
NO ADOPTION
NO CLAIM OF COMPLETENESS
NO LANGUAGE CHANGE
NO CLINICAL DEPLOYMENT
```
