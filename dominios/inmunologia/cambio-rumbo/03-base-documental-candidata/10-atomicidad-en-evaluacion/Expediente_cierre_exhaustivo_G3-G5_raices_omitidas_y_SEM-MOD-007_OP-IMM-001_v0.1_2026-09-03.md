# Expediente de cierre exhaustivo G3–G5 — raíces omitidas y SEM-MOD-007 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Base exacta:** `7b5b948ef2d7e0a21e6dded46a39d434f1363d76`
- **Operación:** `OP-IMM-001`
- **Universo:** `Q0 v0`, 32 raíces exactas
- **Entrada:** `|A0| = 20`
- **Tramo material:** `SEM-RUT-001`, `SEM-CTX-001`–`SEM-CTX-005`, `SEM-MOD-007`
- **Puertas:** `G3-OBS → G4-CON → G5-ATM` por raíz
- **Estatuto:** `EXPEDIENTE_SUSTANTIVO_DE_RECONCILIACION_Y_CIERRE_EXHAUSTIVO`
- **Efecto clínico:** ninguno
- **Autorización asistencial:** ninguna

## 0. Hallazgo de integridad y regla de reparación

La comprobación completa del árbol posterior al hito `|A0|=20` mostró que `SEM-RUT-001` y `SEM-CTX-001`–`SEM-CTX-005` estaban formuladas en G2, pero no tenían objeto material localizado que les asignara estados terminales G3, G4 y G5. `SEM-MOD-007` permanecía expresamente sin abrir.

Por tanto, era incorrecto declarar 31 de 32 raíces recorridas. El estado real de entrada era:

```text
RAICES_Q0 = 32
RAICES_CON_G3_G4_G5_LOCALIZADOS = 25
RAICES_OMITIDAS_EN_LA_EJECUCION = 6
RAIZ_SIGUIENTE_NO_ABIERTA = SEM-MOD-007
```

Este expediente no reescribe ni antedata los objetos anteriores. Repara la cobertura append-only: recorre primero las seis raíces omitidas en su orden canónico y después la raíz terminal. Antes de conservar el cierre, verifica que ninguna conclusión precedente dependiera de fingir resueltas esas raíces.

El defecto es de secuenciación registral y cobertura, no de contenido de los veinte parámetros ya constituidos: G6, G7, aptitud clínica y decisión asistencial seguían cerradas; ningún valor de paciente fue calculado y ninguna ruta utilizó las raíces omitidas.

## 1. Fuentes y contratos aplicables

| Fuente_ID | Objeto | Uso autorizado |
|---|---|---|
| `SRC-CLOSE-001` | HL7 FHIR R5 `Encounter` | motivo, diagnóstico relacionado, periodo, participantes y servicio; transporte, no adjudicación |
| `SRC-CLOSE-002` | HL7 FHIR R5 `Condition` | condición, estado, verificación, inicio, resolución y procedencia |
| `SRC-CLOSE-003` | HL7 FHIR R5 `CarePlan` y `MedicationRequest` | plan, intención, periodo y propuesta documentada; no indicación |
| `SRC-CLOSE-004` | Clinical Frailty Scale, versión 2.0, Dalhousie University | identidad y advertencias de uso del instrumento; no aplicación universal |
| `SRC-CLOSE-005` | `NA0-MATH` v0.3 | atomicidad, `U`, ablación y reproducción |
| `SRC-CLOSE-006` | manifiesto terminal `OP-IMM-001 / Q0 v0` | cardinalidad, terminación y estados permitidos |
| `SRC-CLOSE-007` | suceso correctivo de configuración `7b5b948e…` | operando explícito ≠ configuración admisible |

Enlaces:

- https://hl7.org/fhir/R5/encounter.html
- https://hl7.org/fhir/R5/condition.html
- https://hl7.org/fhir/R5/careplan.html
- https://hl7.org/fhir/R5/medicationrequest.html
- https://www.dal.ca/sites/gmr/our-tools/clinical-frailty-scale.html

## 2. SEM-RUT-001 — posible proceso infeccioso en curso

### 2.1. G3-OBS

```text
E_ACTIVE_INF_QUERY = <
  Evaluacion_ID,
  signos_y_sintomas_documentados,
  observaciones,
  diagnosticos_y_estado,
  pruebas_y_estado,
  tratamiento_en_curso,
  profesional_evaluador,
  conclusion_emitida,
  fecha_indice,
  procedencia,
  version
>
```

El objeto conserva datos y una conclusión profesional anterior si existe. Fiebre, biomarcador, cultivo, antimicrobiano, código, alerta o modelo aislados no constituyen infección activa. Esta operación no diagnostica ni trata un proceso agudo.

```text
G3-OBS/SEM-RUT-001 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 2.2. G4-CON

| Consecuencia_ID | Error | Consecuencia potencial |
|---|---|---|
| `CON-RUT-ACT-INF-001` | absorber posible infección activa en el perfil basal | continuar una operación cuyo presupuesto predecisional puede no cumplirse |
| `CON-RUT-ACT-DX-001` | diagnosticar desde señal aislada | salida falsa de la operación |
| `CON-RUT-ACT-NEG-001` | silencio = ausencia | falsa continuidad |
| `CON-RUT-ACT-AUTH-001` | motor decide infección o tratamiento | invasión de autoridad clínica |

```text
G4-CON/SEM-RUT-001 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 2.3. G5-ATM

La raíz es un control de salida anterior al perfil, no una propiedad basal susceptible de pertenecer a `A0`. Su eventual ejecución necesita una regla clínica autorizada y pertenece a G7 o a otra operación diagnóstica. Convertirla ahora en parámetro mezclaría estado del paciente, autoridad y ruta.

```text
G5-ATM/SEM-RUT-001 = NO_PARAMETRIZABLE
OBJETO_CONSERVADO = CONTROL_DE_SALIDA_PENDIENTE_DE_G7
A0_20 = SIN_CAMBIO
```

## 3. SEM-CTX-001 — momento previsto de inicio

### 3.1. G3-OBS

```text
E_START_PLAN = <Plan_ID, tratamiento_propuesto_ID, fecha_o_intervalo_previsto,
                precision_temporal, estado_del_plan, autor, fecha_de_emision,
                procedencia, version>
```

Se distingue fecha exacta, intervalo, prioridad narrativa y ausencia de programación. El calendario procede de la decisión terapéutica de origen.

```text
G3-OBS/SEM-CTX-001 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 3.2. G4-CON

Perder el punto índice (`CON-CTX-START-001`) impide evaluar vigencias y ventanas; transformar prioridad narrativa en fecha (`CON-CTX-START-002`) crea precisión falsa; usar un plan cancelado (`CON-CTX-START-003`) referencia un episodio inexistente.

```text
G4-CON/SEM-CTX-001 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 3.3. G5-ATM

#### PAR-IMMUNO-START-PLAN-DOC-001

> Existe un momento o intervalo de inicio propuesto, vigente, trazable y explícitamente ligado al tratamiento primario del episodio.

```text
I_START_PLAN_DOC_v0.1(X) -> {0,1,U}
```

`1` exige vínculo, estado vigente, autor, tiempo y precisión; `0` exige que el plan verificado declare expresamente que el inicio aún no está programado; `U` cubre silencio, prioridad no temporal, conflicto, cancelación incierta, vínculo o procedencia insuficientes. El valor no expresa urgencia ni conveniencia clínica.

```text
PAR-IMMUNO-START-PLAN-DOC-001 = PARAMETRO_ATOMICO_DOCUMENTAL
G5-ATM/SEM-CTX-001 = PARAMETRO_ATOMICO
A0_21 = A0_20 + {PAR-IMMUNO-START-PLAN-DOC-001}
```

## 4. SEM-CTX-002 — entidad nosológica de base

### 4.1. G3-OBS

```text
E_BASE_DX = <Condicion_ID, denominacion, codigo_y_sistema, version_terminologica,
             estado_clinico, verificacion, relacion_con_propuesta,
             profesional, procedencia, version>
```

Código, sospecha, rareza, especialidad y motivo terapéutico no se fusionan.

```text
G3-OBS/SEM-CTX-002 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 4.2. G4-CON

Identidad equivocada (`CON-CTX-DX-ID-001`), versión perdida (`CON-CTX-DX-V-001`), diagnóstico no verificado (`CON-CTX-DX-VER-001`) o inferencia desde el fármaco (`CON-CTX-DX-DRUG-001`) pueden contextualizar falsamente el episodio.

```text
G4-CON/SEM-CTX-002 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 4.3. G5-ATM

#### PAR-BASE-DX-DOC-001

> La entidad nosológica que motiva la propuesta consta verificada, versionada y enlazada explícitamente al episodio.

```text
I_BASE_DX_DOC_v0.1(X,codigos_v) -> {0,1,U}
```

`1` verifica la afirmación y el enlace; no diagnostica ni valida la indicación. `0` sólo es admisible si una fuente profesional declara que la propuesta no se vincula a una entidad de base; la ausencia ordinaria es `U`.

```text
PAR-BASE-DX-DOC-001 = PARAMETRO_ATOMICO_DOCUMENTAL
G5-ATM/SEM-CTX-002 = PARAMETRO_ATOMICO
A0_22 = A0_21 + {PAR-BASE-DX-DOC-001}
```

## 5. SEM-CTX-003 — dirección asistencial y participación de Inmunología

### 5.1. G3-OBS

Se separan:

```text
E_EPISODE_LEAD = <Episodio_ID, profesional_o_servicio, rol, alcance,
                  inicio, fin, autoridad, procedencia, version>
E_IMMUNO_PART = <Solicitud_o_acuerdo_ID, rol_inmunologia, alcance,
                 estado, momento, emisor, receptor, procedencia, version>
```

La dirección del episodio y la participación de Inmunología pueden variar independientemente.

```text
G3-OBS/SEM-CTX-003 = OBSERVABLES_CANDIDATOS_CERRADOS_CON_PARTICION_FINITA
```

### 5.2. G4-CON

Omitir liderazgo (`CON-CTX-LEAD-001`) deja autoridad indeterminada; inferir participación por diagnóstico o nombre del tratamiento (`CON-CTX-IMM-INF-001`) atribuye competencia indebidamente; mezclar consulta y dirección (`CON-CTX-ROLE-001`) altera responsabilidades.

```text
G4-CON/SEM-CTX-003 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 5.3. G5-ATM

#### PAR-EPISODE-LEAD-DOC-001

> Consta una adjudicación asistencial vigente del profesional o servicio que dirige el episodio, con rol y alcance identificados.

#### PAR-IMMUNO-PART-DOC-001

> Consta una solicitud o acuerdo vigente de participación de Inmunología, con rol, alcance y momento identificados.

```text
I_EPISODE_LEAD_DOC_v0.1(X) -> {0,1,U}
I_IMMUNO_PART_DOC_v0.1(X) -> {0,1,U}
```

En ambos, `0` exige negación o exclusión profesional explícita dentro de una cobertura suficiente; silencio, organigrama, diagnóstico, rareza, petición unilateral o práctica local no documentada producen `U`.

```text
PAR-EPISODE-LEAD-DOC-001 = PARAMETRO_ATOMICO_DOCUMENTAL
PAR-IMMUNO-PART-DOC-001 = PARAMETRO_ATOMICO_DOCUMENTAL
G5-ATM/SEM-CTX-003 = COMPUESTO_PARTICIONADO_FINITO
A0_24 = A0_22 + {PAR-EPISODE-LEAD-DOC-001, PAR-IMMUNO-PART-DOC-001}
```

## 6. SEM-CTX-004 — protocolo institucional y ejecución local

### 6.1. G3-OBS

```text
E_LOCAL_PROTOCOL = <Protocolo_ID, titulo, version, centro_y_ambito,
                    aplicabilidad_emitida, fecha_vigencia, localizador,
                    autoridad, procedencia, hash>
E_EXEC_CONSTRAINT = <Restriccion_ID, recurso_o_capacidad, estado,
                     alcance, inicio, fin, fuente_responsable,
                     consecuencia_de_ejecucion_declarada, procedencia, version>
```

Protocolo, verdad clínica, disponibilidad, capacidad, necesidad y decisión se conservan separados.

```text
G3-OBS/SEM-CTX-004 = OBSERVABLES_CANDIDATOS_CERRADOS_CON_PARTICION_FINITA
```

### 6.2. G4-CON

Aplicar protocolo ajeno o obsoleto (`CON-CTX-PROT-001`), equiparar limitación con ausencia de necesidad (`CON-CTX-CAP-001`), ocultar restricción (`CON-CTX-HIDE-001`) o presentar factibilidad como indicación (`CON-CTX-IND-001`) puede falsear la ruta.

```text
G4-CON/SEM-CTX-004 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 6.3. G5-ATM

#### PAR-LOCAL-PROTOCOL-APPLICABLE-001

> Existe un protocolo institucional vigente cuya autoridad ha declarado aplicabilidad al episodio y cuyo contenido está identificado y versionado.

#### PAR-EXEC-CONSTRAINT-DOC-001

> Existe una restricción local vigente, verificada y material para ejecutar la actuación propuesta, con recurso, alcance y fuente responsable identificados.

```text
I_LOCAL_PROTOCOL_APPLICABLE_v0.1(X) -> {0,1,U}
I_EXEC_CONSTRAINT_DOC_v0.1(X) -> {0,1,U}
```

No se infiere aplicabilidad desde el centro ni restricción desde una demora. `0` exige declaración explícita de no aplicabilidad o inventario de ejecución con cobertura suficiente; de lo contrario, `U`. Ninguno modifica necesidad clínica ni prescribe alternativa.

```text
PAR-LOCAL-PROTOCOL-APPLICABLE-001 = PARAMETRO_ATOMICO_DOCUMENTAL
PAR-EXEC-CONSTRAINT-DOC-001 = PARAMETRO_ATOMICO_DOCUMENTAL
G5-ATM/SEM-CTX-004 = COMPUESTO_PARTICIONADO_FINITO
A0_26 = A0_24 + {PAR-LOCAL-PROTOCOL-APPLICABLE-001, PAR-EXEC-CONSTRAINT-DOC-001}
```

## 7. SEM-CTX-005 — tramo de edad adulta

### 7.1. G3-OBS

```text
E_AGE_INDEX = <fecha_nacimiento_o_edad_verificada, fecha_indice,
               precision, fuente, conflicto, procedencia, version>
```

La edad se calcula respecto de una fecha índice y conserva precisión y conflicto. Edad, fragilidad, discapacidad y reserva no son equivalentes.

```text
G3-OBS/SEM-CTX-005 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 7.2. G4-CON

Edad sin fecha índice (`CON-CTX-AGE-T0-001`), redondeo oculto (`CON-CTX-AGE-PREC-001`) o edad como sustituto de fragilidad (`CON-CTX-AGE-FRAIL-001`) pueden alterar aplicabilidad o fabricar un modificador.

```text
G4-CON/SEM-CTX-005 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 7.3. G5-ATM

La edad es una magnitud contextual, no una proposición clínica ternaria única. Partirla ahora exigiría umbrales dependientes de cada regla posterior y crearía parámetros por conveniencia. Se conserva como operando verificable para reglas cuya aplicabilidad lo requiera.

```text
G5-ATM/SEM-CTX-005 = NO_PARAMETRIZABLE
OBJETO_CONSERVADO = OPERANDO_EDAD_EN_FECHA_INDICE
A0_26 = SIN_CAMBIO
```

## 8. SEM-MOD-007 — fragilidad o reducción de reserva funcional

### 8.1. G3-OBS

```text
E_FRAILTY_ASSESS = <
  Evaluacion_ID,
  instrumento_ID,
  version,
  poblacion_y_aplicabilidad,
  estado_basal_requerido,
  componentes,
  valores,
  regla_de_combinacion,
  categoria_emitida,
  fecha,
  evaluador,
  verificacion,
  procedencia,
  hash_configuracion
>
```

Se separan fragilidad, dependencia funcional, discapacidad estable, cognición, comorbilidad, estado nutricional, enfermedad aguda y limitación terapéutica. Una puntuación sin versión o aplicada fuera de población no es un estado interpretable.

```text
G3-OBS/SEM-MOD-007 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 8.2. G4-CON

| Consecuencia_ID | Error | Consecuencia potencial |
|---|---|---|
| `CON-FRAIL-AGE-001` | edad = fragilidad | clasificación falsa |
| `CON-FRAIL-DIS-001` | discapacidad estable = fragilidad | penalización estructural indebida |
| `CON-FRAIL-ACUTE-001` | puntuar estado agudo como basal | reserva falsamente reducida |
| `CON-FRAIL-INST-001` | mezclar versiones o escalas | estado no reproducible |
| `CON-FRAIL-LIMIT-001` | fragilidad = limitación terapéutica | salto de autoridad y causalidad |

```text
G4-CON/SEM-MOD-007 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 8.3. G5-ATM

#### PAR-FRAILTY-ASSESS-POS-001

> Una evaluación profesional de fragilidad, verificada y aplicable, satisface el criterio positivo de un instrumento completo y versionado admitido para el episodio.

```text
I_FRAILTY_ASSESS_POS_v0.1(X,PaqueteFrailty_v) -> {0,1,U}
```

El instrumento, versión, población, estado basal, componentes, regla y categoría son operandos obligatorios. `1` exige paquete registrado y evaluación completa positiva; `0`, paquete registrado y evaluación completa no positiva; `U`, cualquier insuficiencia de aplicabilidad, basalidad, componentes, versión, configuración, evaluación, conflicto o procedencia.

La Clinical Frailty Scale v2.0 queda como fuente candidata identificada, no como regla universal de todos los adultos. Su existencia no autoriza extrapolarla a una persona joven, confundir discapacidad con fragilidad ni convertir su puntuación en decisión terapéutica.

De acuerdo con el correctivo precedente:

```text
REG-FRAILTY-ADM-v0.1 = {}
```

Hasta incorporar un paquete operacional con población, instrucciones, categorías, localizador y huella, el parámetro conserva el tipo pero su capacidad automática de `0/1` queda bloqueada:

```text
PAR-FRAILTY-ASSESS-POS-001 =
  PARAMETRO_ATOMICO_COMPARATIVO_CON_CONFIGURACION_PENDIENTE
CAPACIDAD_0_1_AUTOMATICA = BLOQUEADA
G5-ATM/SEM-MOD-007 = PARAMETRO_ATOMICO
A0_27 = A0_26 + {PAR-FRAILTY-ASSESS-POS-001}
```

## 9. Prueba de no invalidación retrospectiva

| Ataque | Resultado |
|---|---|
| los veinte parámetros usaron una fecha de inicio inventada | no: no se ejecutó ningún caso ni ventana |
| se atribuyó diagnóstico de base o especialidad | no: los parámetros previos no adjudican indicación ni autoridad |
| un protocolo local gobernó reglas clínicas | no: G6 y G7 permanecían cerradas |
| la edad produjo umbral | no: no había evaluación de caso |
| la omisión cambió identidades atómicas previas | no se localiza dependencia constitutiva |
| la omisión permitiría abrir G6 sin contexto | sí; por eso se repara antes de G6 |
| la reparación reescribe estados previos | no; añade parámetros contextuales y dos salidas no parametrizables |

```text
PARAMETROS_PREVIOS_INVALIDADOS = 0
DEPENDENCIAS_POSTERIORES_A_RECALCULAR = 0
APERTURA_G6_ANTES_DE_ESTE_CIERRE = PROHIBIDA
```

La no invalidación se limita a constitución atómica. No certifica suficiencia clínica ni anticipa propiedad matricial o ruta.

## 10. Registro de nuevos parámetros

| Orden | Parámetro_ID | Raíz | Naturaleza |
|---:|---|---|---|
| 21 | `PAR-IMMUNO-START-PLAN-DOC-001` | `SEM-CTX-001` | temporal documental |
| 22 | `PAR-BASE-DX-DOC-001` | `SEM-CTX-002` | contextual documental |
| 23 | `PAR-EPISODE-LEAD-DOC-001` | `SEM-CTX-003` | autoridad documentada |
| 24 | `PAR-IMMUNO-PART-DOC-001` | `SEM-CTX-003` | participación documentada |
| 25 | `PAR-LOCAL-PROTOCOL-APPLICABLE-001` | `SEM-CTX-004` | aplicabilidad documental |
| 26 | `PAR-EXEC-CONSTRAINT-DOC-001` | `SEM-CTX-004` | ejecución documental |
| 27 | `PAR-FRAILTY-ASSESS-POS-001` | `SEM-MOD-007` | comparativo pendiente de configuración |

`SEM-RUT-001` y `SEM-CTX-005` no aportan parámetros: cierran respectivamente como control de salida y operando escalar. No se fabrican átomos para aumentar el recuento.

## 11. Ledger exhaustivo de raíces

| Familia | Raíces | Cobertura terminal G3–G5 |
|---|---|---|
| Ruta | `SEM-RUT-001` | cerrada en este expediente |
| Contexto | `SEM-CTX-001`–`SEM-CTX-005` | cerradas en este expediente |
| Exposición | `SEM-EXP-001`–`SEM-EXP-005` | cerradas en adjudicaciones precedentes |
| Huésped | `SEM-HUE-001`–`SEM-HUE-005` | cerradas en adjudicación y expediente precedentes |
| Barrera o dispositivo | `SEM-BAR-001`–`SEM-BAR-004` | cerradas en expediente precedente |
| Historia o exposición | `SEM-HIS-001`–`SEM-HIS-005` | cerradas en expediente precedente |
| Modulación y prevención | `SEM-MOD-001`–`SEM-MOD-007` | 001–006 precedentes; 007 en este expediente |

```text
RAICES_Q0 = 32
RAICES_CON_G3_TERMINAL = 32
RAICES_CON_G4_TERMINAL = 32
RAICES_CON_G5_TERMINAL = 32
RAICES_NUEVAS = 0
RAICES_SIN_ESTADO_TERMINAL = 0
```

Los rótulos históricos no enteramente coincidentes con el vocabulario cerrado del manifiesto se interpretan por su declaración material —control, partición finita, cierre mixto o U tipada— y no abren trabajo nuevo. Su normalización registral pertenece al ledger, no exige reescritura.

## 12. Adversarial integrada

### A. Ocultar las seis raíces omitidas

Rechazado. Se identifican, se cuantifican y se recorren append-only.

### B. Declarar que sólo faltaba MOD-007

Rechazado por contraste directo con los objetos localizados en la rama.

### C. Invalidar automáticamente los veinte parámetros

Rechazado. No se había abierto matriz, ruta ni ejecución; la dependencia se prueba una a una.

### D. Fecha propuesta = urgencia o indicación

Rechazado. El parámetro sólo representa un plan temporal documentado.

### E. Código = diagnóstico de base

Rechazado. Se exige verificación, versión y enlace al episodio.

### F. Diagnóstico = especialidad responsable

Rechazado. Dirección y participación proceden de adjudicación asistencial externa.

### G. Consulta = dirección

Rechazado. Son roles separables.

### H. Protocolo local = verdad clínica

Rechazado. Sólo representa aplicabilidad institucional documentada.

### I. Demora = restricción material

Rechazado. Se exige objeto de restricción, alcance, vigencia y responsable.

### J. Edad = fragilidad

Rechazado. Edad queda como operando; fragilidad exige evaluación propia.

### K. Elegir CFS porque está disponible

Rechazado. Se identifica como candidata, pero el registro ejecutable queda vacío.

### L. Instrumento completo pero no admitido = valor

Rechazado. Produce `U_CONFIGURACION_NO_ADMITIDA`.

### M. Fragilidad = limitar tratamiento

Rechazado. No se constituye intervención, veto ni decisión.

### N. Todo observable debe ser parámetro

Rechazado. Ruta activa y edad cierran sin parámetro.

### O. A0 debe tener cardinalidad prevista

Rechazado. El resultado 27 emerge de la adjudicación; no fue cuota.

### P. Configuración pendiente elimina el tipo

Rechazado. Tipo y capacidad ejecutable son planos distintos y visibles.

### Q. Declarar aptitud clínica por agotar Q0

Rechazado. Agotar G3–G5 sólo habilita revisión de sustancia.

### R. Abrir G6 dentro del mismo objeto

Rechazado. G6 permanece cerrada.

**Dictamen adversarial integrado:** `PASA_CON_HALLAZGO_CORREGIDO_DE_SECUENCIA`.

## 13. Recuentos

| Magnitud | Valor |
|---|---:|
| raíces totales Q0 | 32 |
| raíces reparadas por omisión | 6 |
| raíz terminal recorrida | 1 |
| raíces procesadas en este objeto | 7 |
| parámetros de entrada | 20 |
| parámetros nuevos | 7 |
| parámetros totales | 27 |
| raíces sin parámetro en este objeto | 2 |
| registros de configuración vacíos nuevos | 1, fragilidad |
| parámetros previos invalidados | 0 |
| matrices / rutas / frames | 0 / 0 / 0 |
| nuevas raíces Q0 | 0 |
| documentos auxiliares | 0 |

## 14. Estado de parada

```text
Q0_V0_G3_G4_G5 = AGOTADO
|Q0| = 32
|A0| = 27
RAICES_PENDIENTES = 0
CONFIGURACIONES_CLINICAS_PENDIENTES = {
  OI,
  MDRO_TABLA,
  MDRO_VENTANA,
  NUTRICION,
  FRAGILIDAD
}
CONTROLES_PENDIENTES_DE_G7 = {SEM-RUT-001}
OPERANDOS_NO_PARAMETRIZADOS = {EDAD_EN_FECHA_INDICE}
G6-MAT = NO_ABIERTA
G7-RUT = NO_ABIERTA
APTITUD_CLINICA_OP-IMM-001 = NO_DECLARADA
DECISION_ASISTENCIAL = NINGUNA
DOMINIO_INTERNACIONAL_DE_INMUNOLOGIA = NO_CERRADO
```

Se detiene la secuencia para revisión externa del conjunto completo. Agotar las 32 raíces no demuestra suficiencia de `OP-IMM-001`, no autoriza ejecución sobre un paciente y no convierte los cinco tipos pendientes de configuración en reglas clínicas ejecutables.
