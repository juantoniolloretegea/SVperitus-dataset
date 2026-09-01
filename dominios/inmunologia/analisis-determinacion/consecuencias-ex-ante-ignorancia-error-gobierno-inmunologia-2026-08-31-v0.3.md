# Consecuencias ex ante de ignorancia, omisión y error en inmunología

**Versión:** 0.3  
**Corte:** 31 de agosto de 2026  
**Estatuto:** propuesta para decisión del director.  
**Antecedentes append-only:**  
`v0.1` = **RECHAZADA** por justificación retrospectiva.  
`v0.2` = **INSUFICIENTE** por centrar el contraste en acciones sin constituir primero las consecuencias de ignorar conocimiento obligatorio.  
**Fuera de alcance:** R2, IR, semántica e implementación del Lenguaje.

---

## 0. Objeto

```text
NO responder:
«¿Por qué ha decidido esto la IA?»

RESPONDER ANTES DE DECIDIR:
«¿Qué conocimiento exige esta operación?»
«¿Qué conocimiento falta, está contradicho, desactualizado o no es aplicable?»
«¿Qué error puede producir cada carencia?»
«¿Qué consecuencias tendría ese error?»
«¿Qué consecuencias tiene cada alternativa?»
«¿Qué gobierno y controles se han ejecutado?»
«¿Qué consecuencias acepta asumir el experto después de recibir esta información?»
```

El «porqué» no se genera. Queda implícito en la cadena material:

```text
CONOCIMIENTO EXIGIDO
→ ESTADO DE COBERTURA
→ DEFECTO DE CONOCIMIENTO
→ MODO DE ERROR
→ DECISIÓN/ACCIÓN AFECTADA
→ CONSECUENCIA
→ INFORMACIÓN AL EXPERTO
→ DECISIÓN HUMANA
```

## 1. Invariante append-only

```text
NO UPDATE
NO DELETE
NO OVERWRITE
NO RETROACTIVE INSERT
```

El estado visible siempre se deriva de sucesos:

```text
STATE_n = FOLD(EVENT_0, EVENT_1, ..., EVENT_n)
```

Una corrección no altera el suceso previo:

```text
EVENT_j = {
  event_type: CORRECTION,
  corrects_event_id: EVENT_i,
  corrected_payload,
  authority,
  external_time,
  previous_event_hash
}

EVENT_i remains intact.
```

Una nueva evidencia posterior a la certificación no corrige el episodio:

```text
NEW_EVIDENCE
→ CLOSE current episode as historically unchanged
→ OPEN new episode_id
→ recompute from the beginning
```

## 2. Unidad de conocimiento exigido

```text
knowledge_requirement_id
preferred_label
clinical_perimeter_id
entity_scope
parameter_scope
clinical_operation
population_scope
scenario_scope
temporal_scope
required_skill
required_interpretation
omission_failure_modes[]
authority_source
authority_version
effective_period
criticality_class
```

Ninguna IA crea o elimina requisitos durante el episodio.

## 3. Estado de cobertura del conocimiento

Para cada requisito `kr`:

```text
COVERAGE(kr,S) =
  PRESENT_VALID
  PRESENT_PARTIAL
  ABSENT
  UNKNOWN
  CONTRADICTED
  OUTDATED
  NOT_APPLICABLE
```

Cada estado exige:

```text
coverage_event_id
knowledge_requirement_id
patient_snapshot_id
status
fact_ids[]
evidence_ids[]
rule_ids[]
contradiction_ids[]
residual_ids[]
authority_status
external_time
event_hash
```

Prohibiciones:

```text
ABSENT ≠ negative clinical finding
UNKNOWN ≠ absence of risk
CONTRADICTED ≠ resolved
OUTDATED ≠ applicable
PRESENT_PARTIAL ≠ sufficient
missing data ≠ U
```

## 4. Modo de error por conocimiento ignorado

Para cada `kr` cuyo estado no sea `PRESENT_VALID` o `NOT_APPLICABLE`, se constituye antes de decidir:

```text
failure_mode_id
knowledge_requirement_id
coverage_status
failure_type
affected_operation
trigger_conditions[]
preventive_controls[]
detection_controls[]
patient_consequence_ids[]
expert_consequence_ids[]
system_consequence_ids[]
rule_ids[]
evidence_ids[]
unknown_ids[]
authority_status
```

Tipos mínimos de fallo:

```text
OMISSION_OF_REQUIRED_CHECK
FALSE_REASSURANCE
FALSE_EXCLUSION
FALSE_INCLUSION
MISCLASSIFICATION
WRONG_TIMING
WRONG_ESCALATION
UNNECESSARY_INTERVENTION
CONTRAINDICATED_ACTION
MISSED_INTERACTION
MISSED_MONITORING
UNSUPPORTED_CERTAINTY
```

La lista puede ampliarse por autoridad clínica; la IA no puede reducirla.

## 5. Consecuencia del error

```text
error_consequence_id
failure_mode_id
affected_party = PATIENT | EXPERT | SYSTEM
consequence_type
clinical_manifestation_or_operational_effect
temporal_window
severity_class_if_authorized
reversibility
preventability
detection_opportunity
required_response
evidence_ids[]
rule_ids[]
contradiction_ids[]
external_probability_if_available
probability_source
unknown_ids[]
authority_status
```

Separaciones obligatorias:

```text
SEVERITY ≠ PROBABILITY
PROBABILITY ≠ CERTAINTY
LOW_FREQUENCY ≠ LOW_CONSEQUENCE
AGGREGATE ≠ INDIVIDUAL_CASE
PATIENT_CONSEQUENCE ≠ EXPERT_CONSEQUENCE
TRACE_INTEGRITY ≠ CLINICAL_VALIDITY
```

## 6. Matrices previas a la decisión

### 6.1. Matriz de conocimiento y error

```text
MK = KNOWLEDGE_REQUIREMENTS × COVERAGE_STATUS × FAILURE_MODES × ERROR_CONSEQUENCES
```

### 6.2. Matriz de alternativas y consecuencias

```text
MA = AUTHORIZED_ACTIONS × CONSEQUENCE_AXES × CONSEQUENCES
```

### 6.3. Matriz de gobierno

```text
MG = REQUIRED_CONTROLS × EXECUTION_STATUS × EVIDENCE_OF_EXECUTION
```

Estados de control:

```text
EXECUTED_PASS
EXECUTED_FAIL
NOT_EXECUTED
NOT_APPLICABLE
UNKNOWN
```

```text
IF MK incomplete OR MA incomplete OR MG incomplete:
    ABSTENERSE(PREDECISION_CONSTITUTION_INCOMPLETE)
```

## 7. Pregunta constitutiva de la unidad

Para cada decisión candidata `d`:

```text
BEFORE(d):

1. required_knowledge(d)
2. coverage_state(required_knowledge(d))
3. failure_modes_of_nonvalid_knowledge(d)
4. patient_consequences_of_each_failure(d)
5. expert_consequences_of_each_failure(d)
6. system_consequences_of_each_failure(d)
7. consequences_of_d(d)
8. consequences_of_not_d(d)
9. consequences_of_every_authorized_alternative(d)
10. controls_executed_and_failed(d)
11. decisive_unknowns_and_residual(d)
12. facts_that_would_change_admissibility_or_choice(d)
```

```text
IF BEFORE(d) is not complete and sealed:
    d cannot exist.
```

## 8. Acta predecisional de consecuencias

```text
PREDECISION_CONSEQUENCE_RECORD = {
  record_id,
  episode_id,
  patient_snapshot_hash,
  declared_operation,
  domain_release,
  knowledge_requirements_release,
  coverage_events_root_hash,
  failure_modes_root_hash,
  error_consequences_root_hash,
  authorized_actions_release,
  action_consequences_root_hash,
  governance_controls_root_hash,
  contradictions_root_hash,
  unknowns_root_hash,
  residual_root_hash,
  rule_release,
  evidence_cutoff,
  parity_result,
  completeness_result,
  sealed_before_any_decision: TRUE,
  authority,
  signature,
  event_hash
}
```

```text
IF sealed_before_any_decision != TRUE:
    ABSTENERSE(RETROSPECTIVE_CONSTITUTION_FORBIDDEN)
```

## 9. Información al experto

Antes de aceptar una decisión, el experto recibe el objeto canónico:

```text
EXPERT_INFORMATION = {
  knowledge_present_valid[],
  knowledge_partial[],
  knowledge_absent[],
  knowledge_unknown[],
  knowledge_contradicted[],
  knowledge_outdated[],
  errors_enabled_by_each_defect[],
  patient_consequences[],
  expert_consequences[],
  system_consequences[],
  alternatives_and_consequences[],
  contraindications_and_vetoes[],
  critical_singular_cases[],
  failed_or_unexecuted_controls[],
  residual[],
  facts_that_would_change_the_decision[],
  predecision_record_id
}
```

Condición de suficiencia informativa:

```text
The expert must not be asked merely:
  «Do you accept?»

The expert must receive:
  «These are the specific knowledge deficits, possible errors,
   patient consequences, professional consequences, alternatives,
   unknowns and failed controls attached to this episode.»
```

## 10. Decisión humana append-only

Acciones permitidas:

```text
ACKNOWLEDGE_INFORMATION
REQUEST_ADDITIONAL_KNOWLEDGE
REQUEST_ADDITIONAL_TEST_OR_DATA
DEFER
ESCALATE
REJECT_CANDIDATE
ACCEPT_CANDIDATE
REOPEN_AS_NEW_EPISODE
```

Suceso:

```text
HUMAN_DECISION_EVENT = {
  human_decision_id,
  episode_id,
  professional_role,
  decision_type,
  selected_action_id_if_any,
  accepted_consequence_ids[],
  unresolved_unknown_ids[],
  acknowledged_failed_control_ids[],
  patient_preference_event_id_if_applicable,
  predecision_record_id,
  external_time,
  signature,
  previous_event_hash,
  event_hash
}
```

`ACKNOWLEDGE_INFORMATION` no equivale a `ACCEPT_CANDIDATE`.

## 11. Responsabilidad: tres objetos separados

| Objeto | Qué puede registrar el sistema | Qué no puede constituir por sí mismo |
|---|---|---|
| Responsabilidad decisoria registral | Quién recibió qué información, qué consecuencias conoció y qué decisión firmó | Validez clínica automática |
| Responsabilidad profesional | Rol, competencia declarada, controles exigidos y actuación realizada | Estándar profesional completo fuera del corpus autorizado |
| Responsabilidad jurídica | Hechos, versiones, información, decisiones y trazas disponibles para evaluación | Imputación, culpa, causalidad jurídica, exoneración o transferencia automática de responsabilidad |

```text
INFORMED_EXPERT_DECISION
≠ blanket assumption of legal liability
≠ release of provider, institution, developer or data controller
≠ patient informed consent
```

La atribución jurídica depende del ordenamiento, del producto, del uso previsto, de los roles y del caso. El acta aporta prueba material; no dicta la consecuencia jurídica.

## 12. Supresión del «porqué» abstracto

Consulta no admitida como método de auditoría:

```text
WHY_FREE_TEXT(decision_id)
```

Respuesta permitida:

```text
RETURN EXISTING_PREDECISION_CONSEQUENCE_RECORD(decision_id)
```

El sistema no genera una explicación nueva. Devuelve exclusivamente sucesos y relaciones constituidos antes de decidir:

```text
knowledge_requirement_id
→ coverage_event_id
→ failure_mode_id
→ error_consequence_id
→ control_event_id
→ alternative_action_id
→ predecision_record_id
→ human_decision_event_id
```

## 13. Igualdad entre motores de IA

Los motores sólo pueden devolver identificadores canónicos existentes.

```text
ENGINE_RESULT(e) = {
  knowledge_requirement_ids,
  coverage_event_ids,
  failure_mode_ids,
  error_consequence_ids,
  contradiction_ids,
  unknown_ids,
  control_event_ids,
  authorized_action_ids
}
```

```text
PARITY(e1,e2) := canonicalize(ENGINE_RESULT(e1))
                 = canonicalize(ENGINE_RESULT(e2))
```

```text
IF PARITY = FALSE:
    APPEND ENGINE_DIVERGENCE
    ABSTENERSE
```

Ningún motor redacta la información clínica final. La interfaz la representa desde objetos canónicos y sucesos sellados.

## 14. Algoritmo

```text
INPUT:
  frozen patient snapshot S
  declared operation O
  authorized knowledge requirements KRv
  authorized actions Av
  authorized rules Rv
  versioned evidence Ev
  governance controls GCv

OUTPUT:
  HUMAN_DECISION_WITH_PREDECISION_RECORD
  OR ABSTENERSE(reason_codes[])

CEIOG(S,O):

01  APPEND REQUEST_RECEIVED
02  APPEND SNAPSHOT_FROZEN
03  load KRv for S,O
04  IF KRv not closed by clinical authority:
05      APPEND KNOWLEDGE_SPACE_NOT_CLOSED
06      RETURN ABSTENERSE

07  FOR each kr IN KRv:
08      determine COVERAGE(kr,S)
09      APPEND coverage event
10      IF coverage != PRESENT_VALID and coverage != NOT_APPLICABLE:
11          load every authorized failure mode for kr
12          FOR each failure mode:
13              load patient, expert and system consequences
14              APPEND each relation and its evidence/rule

15  load every authorized action in Av
16  evaluate consequences of action, non-action and every alternative
17  APPEND all consequence events

18  execute every required governance control in GCv
19  APPEND pass, fail, not-executed, unknown or not-applicable

20  verify MK, MA and MG completeness
21  IF incomplete:
22      APPEND PREDECISION_CONSTITUTION_INCOMPLETE
23      RETURN ABSTENERSE

24  run canonical parity across required engines
25  IF divergence:
26      APPEND ENGINE_DIVERGENCE
27      RETURN ABSTENERSE

28  APPEND and seal PREDECISION_CONSEQUENCE_RECORD
29  assert no decision event exists earlier in episode
30  IF assertion fails:
31      APPEND RETROSPECTIVE_CONSTITUTION_FORBIDDEN
32      RETURN ABSTENERSE

33  render EXPERT_INFORMATION from sealed events only
34  APPEND INFORMATION_PRESENTED_TO_EXPERT
35  receive human action
36  APPEND HUMAN_DECISION_EVENT

37  IF decision requires new fact, rule, consequence or control:
38      APPEND REOPEN_REQUIRED
39      OPEN new episode_id
40      RETURN ABSTENERSE for current episode

41  RETURN HUMAN_DECISION_WITH_PREDECISION_RECORD
```

## 15. Pruebas de aceptación

```text
A01. Se genera un porqué libre después de decidir -> FAIL.
A02. Se añade una consecuencia después de decidir -> episodio no reparable; nuevo episodio.
A03. Se modifica un suceso previo -> FAIL.
A04. Se elimina una carencia porque luego apareció el dato -> FAIL.
A05. Falta un conocimiento obligatorio y no existe modo de error asociado -> FAIL.
A06. Existe modo de error sin consecuencia para el paciente -> FAIL, salvo NOT_APPLICABLE autorizado.
A07. Existe modo de error sin consecuencia para el experto -> FAIL, salvo NOT_APPLICABLE autorizado.
A08. La IA declara que UNKNOWN no implica riesgo -> FAIL.
A09. Dos IAs devuelven relaciones distintas -> ENGINE_DIVERGENCE y abstención.
A10. El experto sólo ve una casilla «aceptar» -> FAIL.
A11. El experto recibe déficits, errores, consecuencias, alternativas y controles antes de decidir -> requisito cumplido.
A12. Se confunde aceptación profesional con consentimiento del paciente -> FAIL.
A13. Se presenta la firma como transferencia de responsabilidad jurídica -> FAIL.
A14. Se oculta un control no ejecutado -> FAIL.
A15. Una estadística agregada oculta una consecuencia singular documentada -> FAIL.
A16. El registro es íntegro pero la regla clínica es inválida -> FAIL clínico independiente.
A17. La decisión humana precede al acta predecisional -> FAIL.
A18. Una corrección conserva original, vínculo y nueva versión -> PASS append-only.
```

## 16. Fórmula de suficiencia

```text
DECISION_ADMISSIBLE :=
  KNOWLEDGE_SPACE_CLOSED
  ∧ COVERAGE_RECORDED_FOR_ALL_REQUIREMENTS
  ∧ FAILURE_MODES_CONSTITUTED_FOR_ALL_DEFECTS
  ∧ CONSEQUENCES_CONSTITUTED_FOR_ALL_FAILURE_MODES
  ∧ ALL_AUTHORIZED_ALTERNATIVES_CONTRASTED
  ∧ GOVERNANCE_CONTROLS_RECORDED
  ∧ ENGINE_PARITY
  ∧ PREDECISION_RECORD_SEALED
  ∧ EXPERT_FULLY_INFORMED
  ∧ HUMAN_DECISION_APPENDED
```

```text
IF any term = FALSE:
    ABSTENERSE
```

## 17. Referencias normativas de frontera

| Referencia | Alcance utilizado |
|---|---|
| [Reglamento (UE) 2024/1689, texto consolidado a 27-07-2026](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng) | Supervisión humana y conservación de registros bajo el control del responsable del despliegue; no se infiere aquí la calificación regulatoria concreta del sistema |
| [Ley 41/2002, de autonomía del paciente](https://www.boe.es/buscar/act.php?id=BOE-A-2002-22188) | Información clínica, opciones disponibles, decisión del paciente y documentación asistencial; no confundir con la decisión profesional interna |
| [Ley 44/2003, de ordenación de las profesiones sanitarias](https://www.boe.es/buscar/act.php?id=BOE-A-2003-21340) | Competencia y actualización profesional; no determina por sí sola una imputación jurídica en un episodio concreto |

## 18. Decisiones reservadas al director

```text
D01. Autorizar o rechazar CEIOG.
D02. Definir la autoridad que cierra el espacio de conocimiento por operación.
D03. Definir el catálogo de modos de error y consecuencias.
D04. Definir criticidad y controles de parada.
D05. Definir el contenido mínimo mostrado al experto.
D06. Definir qué actos requieren información y consentimiento del paciente.
D07. Definir la auditoría jurídica separada.
D08. Autorizar cualquier interfaz futura con unidades técnicas.
```

No se adopta ninguna decisión en este documento.
