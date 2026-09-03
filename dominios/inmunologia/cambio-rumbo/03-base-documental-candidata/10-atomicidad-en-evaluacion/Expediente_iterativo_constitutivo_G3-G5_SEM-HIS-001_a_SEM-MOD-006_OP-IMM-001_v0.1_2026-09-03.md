# Expediente iterativo constitutivo G3–G5 — SEM-HIS-001 a SEM-MOD-006 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Base exacta:** `f2121e8a048a2ba6ab7d8c6dd35b3f2ae7b15b69`
- **Operación:** `OP-IMM-001`
- **Universo:** `Q0 v0`, 32 raíces exactas
- **Tramo:** `SEM-HIS-001`–`SEM-HIS-005`, `SEM-MOD-001`–`SEM-MOD-006`
- **Puertas:** `G3-OBS → G4-CON → G5-ATM` por raíz
- **Entrada autorizada:** `|A0| = 6`
- **Criterio de parada:** `|A0| = 20`
- **Estatuto:** `EXPEDIENTE_SUSTANTIVO_SECUENCIAL_CERRADO`
- **Efecto clínico:** ninguno
- **Autorización asistencial:** ninguna

## 0. Regla de ejecución

La corrección precedente dejó cuatro candidatos en `U_REQUIERE_REGLA`; no se recuperan para completar una cuota. Por ello, alcanzar veinte parámetros exige catorce adopciones nuevas, no diez.

El tramo sigue el orden de `Q0`. Cada raíz cierra observables, consecuencias y atomicidad antes de pasar a la siguiente. Los nuevos parámetros son deliberadamente documentales o comparativos: representan un diagnóstico, acontecimiento, procedimiento o soporte expresamente verificado, pero no lo diagnostican de novo.

```text
AFIRMACION_CLINICA_VERIFICADA_Y_DOCUMENTADA = OBJETO_REPRESENTABLE
CODIGO_O_MENCION_AISLADA = INSUFICIENTE
REPRESENTACION =/= VERDAD_BIOLOGICA_UNIVERSAL
```

La fuente clínica debe preceder al estado. Texto generado, lista de problemas no verificada, código sin contexto o inferencia desde medicación producen `U`, no `1`.

## 1. Fuentes transversales

| Fuente_ID | Fuente | Uso autorizado |
|---|---|---|
| `SRC-HM-001` | HL7 FHIR R5 `Condition` | condición documentada, estado clínico y de verificación, inicio, resolución, evidencia y procedencia |
| `SRC-HM-002` | HL7 FHIR R5 `Encounter` | clase, periodo, estado, servicio y motivo de un encuentro; no demuestra por sí solo gravedad o infección |
| `SRC-HM-003` | HL7 FHIR R5 `Procedure` | procedimiento, estado, momento, sujeto, motivo y resultado; no demuestra por sí solo exposición infecciosa |
| `SRC-HM-004` | HL7 FHIR R5 `Observation` | medición o afirmación con método, tiempo, interpretación y procedencia; no sustituye diagnóstico |
| `SRC-HM-005` | HL7 FHIR R5 `DiagnosticReport` | informe diagnóstico y resultados enlazados; conserva conclusión y versión |
| `SRC-HM-006` | WHO ICD-11 | identidad terminológica versionada de condiciones; el código no constituye verificación clínica |
| `SRC-HM-007` | ECDC, terminología de resistencia antimicrobiana adquirida | identidad declarada de fenotipos resistentes; no confunde colonización con infección |
| `SRC-HM-008` | KDIGO 2024 CKD Guideline | marco de enfermedad renal crónica y tratamiento sustitutivo; no se importan decisiones terapéuticas |
| `SRC-HM-009` | ESC 2026 Heart Failure Guideline | marco versionado de insuficiencia cardiaca; se usa como referencia de identidad, no para diagnosticar desde datos parciales |
| `SRC-HM-010` | consenso GLIM | evaluación explícita de malnutrición mediante criterio e instrumento registrados; no se presume desde peso aislado |
| `SRC-HM-011` | `NA0-MATH` v0.3 | atomicidad, `U`, ablación, procedencia y reproducción |

Enlaces:

- https://hl7.org/fhir/R5/condition.html
- https://hl7.org/fhir/R5/encounter.html
- https://hl7.org/fhir/R5/procedure.html
- https://hl7.org/fhir/R5/observation.html
- https://hl7.org/fhir/R5/diagnosticreport.html
- https://icd.who.int/
- https://www.ecdc.europa.eu/en/publications-data/directory-guidance-prevention-and-control/antimicrobial-resistance
- https://kdigo.org/guidelines/ckd-evaluation-and-management/
- https://www.escardio.org/guidelines/clinical-practice-guidelines/all-esc-practice-guidelines/heart-failure/
- https://doi.org/10.1016/j.clnu.2018.08.002

## 2. SEM-HIS-001 — antecedente de infección grave

### 2.1. G3-OBS

```text
E_INF_HIST = <Episodio_ID, diagnostico_infeccioso, microorganismo_y_sitio,
              inicio_y_fin, encuentro_asociado, ingreso_atribuido,
              soporte_organico_atribuido, tratamiento_documentado,
              desenlace, estado_de_verificacion, procedencia, version>
```

La raíz se observa mediante episodios identificados. Se separan infección, ingreso, cuidados intensivos, soporte orgánico, tratamiento parenteral, desenlace y etiqueta textual «grave». Una hospitalización no prueba por sí sola que la infección fuera la causa; el vínculo debe ser explícito.

```text
G3-OBS/SEM-HIS-001 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 2.2. G4-CON

| Consecuencia_ID | Error | Consecuencia potencial |
|---|---|---|
| `CON-HIS-SEV-ID-001` | fusionar episodios | gravedad o recurrencia falsas |
| `CON-HIS-SEV-ATTR-001` | atribuir ingreso a infección sin vínculo | antecedente grave falso |
| `CON-HIS-SEV-SUP-001` | omitir soporte orgánico ligado | pérdida de una señal material de consecuencia previa |
| `CON-HIS-SEV-DX-001` | código o antibiótico como infección confirmada | clasificación no demostrada |

```text
G4-CON/SEM-HIS-001 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 2.3. G5-ATM

#### PAR-INF-HOSP-HIST-001

> Existe al menos un episodio infeccioso previo, verificado, que motivó un ingreso hospitalario atribuido explícitamente a dicho episodio.

```text
I_INF_HOSP_HIST_v0.1(X,h_hist) -> {0,1,U}
```

`1` exige episodio e ingreso enlazados causalmente por la fuente; `0` exige historia de cobertura suficiente sin episodio de ese tipo; `U` cubre cobertura, identidad, atribución, periodo, verificación, conflicto o procedencia insuficientes.

#### PAR-INF-ORGSUP-HIST-001

> Existe al menos un episodio infeccioso previo, verificado, durante el cual se documentó soporte de uno o más órganos atribuido al episodio.

```text
I_INF_ORGSUP_HIST_v0.1(X,h_hist) -> {0,1,U}
```

El soporte debe identificarse y enlazarse; estancia en UCI, monitorización o gravedad textual no lo sustituyen. `0` exige cobertura suficiente; `U` preserva atribución o soporte inciertos.

Los dos parámetros no son redundantes: puede existir ingreso por infección sin soporte orgánico. El segundo añade una consecuencia previa no reconstruible desde el primero. Ninguno fija riesgo futuro, sepsis retrospectiva ni actuación.

```text
PAR-INF-HOSP-HIST-001 = PARAMETRO_ATOMICO
PAR-INF-ORGSUP-HIST-001 = PARAMETRO_ATOMICO
G5-ATM/SEM-HIS-001 = COMPUESTO_PARTICIONADO_FINITO
A0_8 = A0_6 + {PAR-INF-HOSP-HIST-001, PAR-INF-ORGSUP-HIST-001}
```

## 3. SEM-HIS-002 — antecedente de infección oportunista

### 3.1. G3-OBS

```text
E_OI_HIST = <Episodio_ID, diagnostico, agente, sitio, contexto_del_huesped,
             clasificacion_como_oportunista, fuente_de_clasificacion,
             inicio_y_fin, verificacion, procedencia, version>
```

Se conserva la clasificación emitida por una fuente clínica autorizada. No se genera una taxonomía universal: un microorganismo puede producir enfermedad oportunista o no oportunista según huésped, sitio y contexto.

```text
G3-OBS/SEM-HIS-002 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 3.2. G4-CON

Omitir contexto (`CON-OI-CTX-001`), confundir colonización con infección (`CON-OI-COL-001`), convertir una lista fija de microorganismos en verdad universal (`CON-OI-TAX-001`) o perder verificación (`CON-OI-VER-001`) puede crear u ocultar falsamente el antecedente.

```text
G4-CON/SEM-HIS-002 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 3.3. G5-ATM

#### PAR-OI-DOC-HIST-001

> Existe un episodio infeccioso previo verificado y clasificado explícitamente como oportunista por una fuente clínica autorizada, con agente o diagnóstico, sitio, contexto y versión identificados.

```text
I_OI_DOC_HIST_v0.1(X,h_hist) -> {0,1,U}
```

El transductor no diagnostica oportunismo: verifica una afirmación clínica anterior con sujeto, contexto y procedencia. `0` exige historia de cobertura suficiente sin episodio clasificado; `U` cubre clasificación ausente, taxonomía no ligada, infección no verificada, contexto, tiempo, conflicto o procedencia insuficientes.

```text
PAR-OI-DOC-HIST-001 = PARAMETRO_ATOMICO
G5-ATM/SEM-HIS-002 = PARAMETRO_ATOMICO_DOCUMENTAL
A0_9 = A0_8 + {PAR-OI-DOC-HIST-001}
```

## 4. SEM-HIS-003 — patrón de infecciones recurrentes

### 4.1. G3-OBS

Se constituye `E_INF_SERIES`: episodios verificados, identidad, sitio, agente si consta, inicio, resolución, separación entre episodios, fuente, cobertura y versión. El normalizador ordena y detecta posibles duplicados; no decide recurrencia.

```text
G3-OBS/SEM-HIS-003 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 4.2. G4-CON

Las consecuencias de fusionar recaída, persistencia y episodio nuevo; contar duplicados; escoger una ventana oportunista; o usar registros incompletos quedan cerradas como `CON-REC-ID-001`, `CON-REC-DUP-001`, `CON-REC-WIN-001` y `CON-REC-COV-001`.

```text
G4-CON/SEM-HIS-003 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 4.3. G5-ATM

No existe en las fuentes ligadas una única regla de número, intervalo, sitio y contexto que constituya «patrón recurrente» para toda `OP-IMM-001`. Adoptar una cifra general reproduciría el defecto reparado.

```text
CAND-INF-RECURRENT-001 = U_REQUIERE_REGLA
G5-ATM/SEM-HIS-003 = U_ATOMICIDAD_NO_CONSTITUIDA
A0_9 = SIN_CAMBIO
```

## 5. SEM-HIS-004 — colonización con resistencia pertinente

### 5.1. G3-OBS

```text
E_MDRO_COL = <Hallazgo_ID, microorganismo, muestra_y_sitio,
              estado_colonizacion, metodo, fenotipo_o_genotipo_resistencia,
              antimicrobianos_probados, fecha, estado_del_resultado,
              criterio_de_vigencia, verificacion, procedencia, version>
```

Colonización, infección y contaminación permanecen separadas. La etiqueta `MDRO` no sustituye organismo, resistencia, método, sitio y versión taxonómica.

```text
G3-OBS/SEM-HIS-004 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 5.2. G4-CON

Confundir colonización con infección (`CON-COL-INF-001`), resistencia inferida desde tratamiento (`CON-COL-AMR-001`), hallazgo remoto como vigente (`CON-COL-TIME-001`) o muestra no atribuible (`CON-COL-SITE-001`) puede producir rutas diagnósticas o preventivas erróneas.

```text
G4-CON/SEM-HIS-004 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 5.3. G5-ATM

#### PAR-MDRO-COL-DOC-001

> Existe colonización verificada por un microorganismo con resistencia documentada y clasificada como pertinente bajo una regla taxonómica y temporal versionada para el episodio.

```text
I_MDRO_COL_DOC_v0.1(X,h,regla_v) -> {0,1,U}
```

La regla recibe una tabla explícita de microorganismo–resistencia y una ventana; no delega en un criterio desconocido. `1` exige coincidencia reproducible; `0` exige cobertura de cribado declarada suficiente y ningún hallazgo vigente; `U` cubre cribado incompleto, estado colonización/infección, sitio, resistencia, método, vigencia, taxonomía, conflicto o procedencia.

```text
PAR-MDRO-COL-DOC-001 = PARAMETRO_ATOMICO
G5-ATM/SEM-HIS-004 = PARAMETRO_ATOMICO
A0_10 = A0_9 + {PAR-MDRO-COL-DOC-001}
```

## 6. SEM-HIS-005 — exposición sanitaria previa

### 6.1. G3-OBS

Entidades independientes:

```text
E_ACUTE_ENC = <Encuentro_ID, clase, nivel_asistencial, inicio, fin,
               estado, motivo_documentado, procedencia, version>

E_INV_PROC = <Procedimiento_ID, tipo, invasividad_declarada, sitio,
              inicio, fin, estado, encuentro, procedencia, version>
```

Una hospitalización y un procedimiento invasivo pueden divergir. Consulta, urgencias, ingreso, residencia, hospital de día y atención domiciliaria no se fusionan. El procedimiento no se infiere desde facturación o medicación.

```text
G3-OBS/SEM-HIS-005 = OBSERVABLES_CANDIDATOS_CERRADOS_CON_PARTICION_FINITA
```

### 6.2. G4-CON

Consecuencias: perder clase o periodo (`CON-HC-ENC-001`), confundir contacto con ingreso (`CON-HC-CLASS-001`), inferir invasividad (`CON-HC-PROC-001`) y aplicar una ventana no versionada (`CON-HC-WIN-001`). Ninguna constituye colonización, infección o riesgo cerrado.

```text
G4-CON/SEM-HIS-005 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 6.3. G5-ATM

#### PAR-ACUTECARE-ENC-HIST-001

> Existe un encuentro previo de hospitalización aguda cuyo periodo intersecta la ventana de exposición sanitaria explícita y versionada del episodio.

```text
I_ACUTECARE_ENC_HIST_v0.1(X,ventana_v) -> {0,1,U}
```

#### PAR-INV-PROC-HIST-001

> Existe un procedimiento previo documentado como invasivo cuyo periodo intersecta la ventana de exposición sanitaria explícita y versionada del episodio.

```text
I_INV_PROC_HIST_v0.1(X,ventana_v) -> {0,1,U}
```

En ambos, `1` es intersección temporal con objeto válido; `0` exige historia de cobertura suficiente; `U` cubre clase, invasividad, periodo, ventana, identidad, estado, conflicto o procedencia. La ventana es un operando explícito, no un criterio clínico sin ligar.

```text
PAR-ACUTECARE-ENC-HIST-001 = PARAMETRO_ATOMICO
PAR-INV-PROC-HIST-001 = PARAMETRO_ATOMICO
G5-ATM/SEM-HIS-005 = COMPUESTO_PARTICIONADO_FINITO
A0_12 = A0_10 + {PAR-ACUTECARE-ENC-HIST-001, PAR-INV-PROC-HIST-001}
```

## 7. SEM-MOD-001 — condición metabólica

### 7.1. G3-OBS

`E_MET_COND` conserva diagnóstico, terminología, estado clínico y de verificación, inicio, resolución, evidencia, profesional responsable y versión. Medicación, glucemia aislada, obesidad y diagnóstico de diabetes no son equivalentes.

```text
G3-OBS/SEM-MOD-001 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 7.2. G4-CON

Omitir diabetes verificada puede perder un modificador material; inferirla desde fármaco o cifra aislada puede crearla falsamente. Control glucémico, complicaciones, tratamiento y gravedad permanecen separados.

```text
G4-CON/SEM-MOD-001 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 7.3. G5-ATM

#### PAR-DM-DOC-ACTIVE-001

> Existe un diagnóstico verificado y clínicamente activo de diabetes mellitus en el horizonte predecisional, identificado mediante terminología versionada.

```text
I_DM_DOC_ACTIVE_v0.1(X,h,codigos_v) -> {0,1,U}
```

`1` exige diagnóstico verificado, activo y perteneciente al conjunto explícito de códigos; `0` exige lista de problemas de cobertura suficiente sin diagnóstico activo; `U` cubre verificación, estado, terminología, horizonte, conflicto o procedencia. No diagnostica desde glucosa o HbA1c y no representa control metabólico.

```text
PAR-DM-DOC-ACTIVE-001 = PARAMETRO_ATOMICO_DOCUMENTAL
RESTO_CONDICIONES_METABOLICAS = RES-MOD-MET-OTHER-001
G5-ATM/SEM-MOD-001 = CERRADA_MIXTA
A0_13 = A0_12 + {PAR-DM-DOC-ACTIVE-001}
```

## 8. SEM-MOD-002 — condición cardiovascular

### 8.1. G3-OBS

`E_CV_COND` conserva diagnóstico, subtipo, estado, verificación, inicio, resolución, evidencia y versión. Insuficiencia cardiaca se separa de cardiopatía isquémica, arritmia, valvulopatía, hipertensión y factores de riesgo.

```text
G3-OBS/SEM-MOD-002 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 8.2. G4-CON

Confundir diagnósticos cardiovasculares puede modificar falsamente reserva, tolerancia o escalado; inferir insuficiencia cardiaca desde diurético, edema o fracción de eyección aislada es inadmisible.

```text
G4-CON/SEM-MOD-002 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 8.3. G5-ATM

#### PAR-HF-DOC-ACTIVE-001

> Existe un diagnóstico verificado y clínicamente activo de insuficiencia cardiaca en el horizonte predecisional, identificado mediante terminología versionada.

```text
I_HF_DOC_ACTIVE_v0.1(X,h,codigos_v) -> {0,1,U}
```

No calcula fenotipo, clase funcional, estabilidad, congestión ni riesgo. `0` exige cobertura diagnóstica suficiente; `U` conserva estado, verificación, identidad o vigencia inciertos.

```text
PAR-HF-DOC-ACTIVE-001 = PARAMETRO_ATOMICO_DOCUMENTAL
RESTO_CONDICIONES_CARDIOVASCULARES = RES-MOD-CV-OTHER-001
G5-ATM/SEM-MOD-002 = CERRADA_MIXTA
A0_14 = A0_13 + {PAR-HF-DOC-ACTIVE-001}
```

## 9. SEM-MOD-003 — alteración renal

### 9.1. G3-OBS

Se separan condición renal crónica documentada, mediciones de función, lesión renal aguda, estabilidad y tratamiento renal sustitutivo.

```text
E_RENAL_COND = <Condicion_ID, diagnostico_y_categoria, estado, verificacion,
                inicio, evidencia, estabilidad_declarada, procedencia, version>
E_KRT = <Terapia_ID, modalidad, estado, inicio, calendario_si_consta,
         acceso_relacionado, procedencia, version>
```

```text
G3-OBS/SEM-MOD-003 = OBSERVABLES_CANDIDATOS_CERRADOS_CON_PARTICION_FINITA
```

### 9.2. G4-CON

Consecuencias: diagnosticar cronicidad desde una medición (`CON-REN-CHR-001`), confundir AKI y CKD (`CON-REN-AKI-001`), omitir KRT activa (`CON-REN-KRT-001`) o usar estadio remoto (`CON-REN-TIME-001`). Ajuste farmacológico y actuación quedan fuera.

```text
G4-CON/SEM-MOD-003 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 9.3. G5-ATM

#### PAR-CKD-DOC-ACTIVE-001

> Existe enfermedad renal crónica verificada y clínicamente activa, documentada conforme a una clasificación versionada.

```text
I_CKD_DOC_ACTIVE_v0.1(X,h,codigos_v) -> {0,1,U}
```

No diagnostica CKD desde una eGFR aislada. Categoría y gravedad son observables separados.

#### PAR-KRT-ACTIVE-001

> Existe tratamiento renal sustitutivo activo y documentado en el horizonte predecisional, con modalidad y estado identificados.

```text
I_KRT_ACTIVE_v0.1(X,h) -> {0,1,U}
```

No infiere indicación, acceso, adecuación ni ajuste de dosis. Para ambos parámetros, `0` exige cobertura suficiente y `U` conserva estado, modalidad, vigencia, verificación o procedencia inciertos.

```text
PAR-CKD-DOC-ACTIVE-001 = PARAMETRO_ATOMICO_DOCUMENTAL
PAR-KRT-ACTIVE-001 = PARAMETRO_ATOMICO_DOCUMENTAL
G5-ATM/SEM-MOD-003 = COMPUESTO_PARTICIONADO_FINITO
A0_16 = A0_14 + {PAR-CKD-DOC-ACTIVE-001, PAR-KRT-ACTIVE-001}
```

## 10. SEM-MOD-004 — condición pulmonar crónica

### 10.1. G3-OBS

Se separan diagnóstico estructural, función pulmonar, síntomas, exacerbación, infección activa y soporte respiratorio.

```text
E_BRONCHIECTASIS = <Condicion_ID, diagnostico, evidencia, distribucion,
                    estado, verificacion, inicio, procedencia, version>
E_RESP_SUPPORT = <Soporte_ID, modalidad, indicacion_documentada, estado,
                  inicio, pauta, procedencia, version>
```

```text
G3-OBS/SEM-MOD-004 = OBSERVABLES_CANDIDATOS_CERRADOS_CON_PARTICION_FINITA
```

### 10.2. G4-CON

Omitir bronquiectasias puede perder una condición estructural pertinente; inferirlas desde tos o cultivos las crea falsamente. Omitir soporte respiratorio puede perder reserva o dependencia; el soporte no equivale a diagnóstico ni infección.

```text
G4-CON/SEM-MOD-004 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 10.3. G5-ATM

#### PAR-BRONCHIECTASIS-DOC-ACTIVE-001

> Existe un diagnóstico verificado y clínicamente activo de bronquiectasias en el horizonte predecisional.

```text
I_BRONCHIECTASIS_DOC_v0.1(X,h,codigos_v) -> {0,1,U}
```

#### PAR-RESP-SUPPORT-ACTIVE-001

> Existe soporte respiratorio crónico activo y documentado en el horizonte predecisional, con modalidad y estado identificados.

```text
I_RESP_SUPPORT_ACTIVE_v0.1(X,h) -> {0,1,U}
```

Los transductores verifican objetos documentados; no diagnostican desde síntomas ni prescriben soporte. `0` exige cobertura suficiente y `U` preserva identidad, modalidad, estado, vigencia, verificación o procedencia inciertos.

```text
PAR-BRONCHIECTASIS-DOC-ACTIVE-001 = PARAMETRO_ATOMICO_DOCUMENTAL
PAR-RESP-SUPPORT-ACTIVE-001 = PARAMETRO_ATOMICO_DOCUMENTAL
RESTO_CONDICIONES_PULMONARES = RES-MOD-PULM-OTHER-001
G5-ATM/SEM-MOD-004 = COMPUESTO_PARTICIONADO_FINITO
A0_18 = A0_16 + {PAR-BRONCHIECTASIS-DOC-ACTIVE-001, PAR-RESP-SUPPORT-ACTIVE-001}
```

## 11. SEM-MOD-005 — alteración hepática

### 11.1. G3-OBS

`E_LIVER_COND` conserva diagnóstico, etiología si consta, estado, verificación, inicio, evidencia, descompensación documentada, procedencia y versión. Pruebas hepáticas alteradas no equivalen a cirrosis; cirrosis no equivale a descompensación actual.

```text
G3-OBS/SEM-MOD-005 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 11.2. G4-CON

Inferir cirrosis desde una cifra (`CON-LIV-DX-001`), perder verificación (`CON-LIV-VER-001`) o mezclar condición crónica y descompensación (`CON-LIV-DEC-001`) puede alterar reserva y ejecución. No se constituye ajuste farmacológico.

```text
G4-CON/SEM-MOD-005 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 11.3. G5-ATM

#### PAR-CIRRHOSIS-DOC-ACTIVE-001

> Existe un diagnóstico verificado y clínicamente activo de cirrosis hepática en el horizonte predecisional, identificado mediante terminología versionada.

```text
I_CIRRHOSIS_DOC_ACTIVE_v0.1(X,h,codigos_v) -> {0,1,U}
```

`1` exige condición verificada y activa; `0`, cobertura suficiente sin ella; `U`, identidad, verificación, estado, vigencia, conflicto o procedencia insuficientes. No representa etiología, estadio, descompensación ni actuación.

```text
PAR-CIRRHOSIS-DOC-ACTIVE-001 = PARAMETRO_ATOMICO_DOCUMENTAL
RESTO_CONDICIONES_HEPATICAS = RES-MOD-LIV-OTHER-001
G5-ATM/SEM-MOD-005 = CERRADA_MIXTA
A0_19 = A0_18 + {PAR-CIRRHOSIS-DOC-ACTIVE-001}
```

## 12. SEM-MOD-006 — estado nutricional

### 12.1. G3-OBS

```text
E_NUTR_ASSESS = <Evaluacion_ID, instrumento_y_version,
                 componentes_fenotipicos, componentes_etiologicos,
                 valores_y_unidades, criterio_y_umbral_explicitos,
                 resultado_emitido, fecha, aplicabilidad,
                 estado_de_verificacion, procedencia, version>
```

Peso, IMC, pérdida ponderal, ingesta, inflamación, masa muscular y diagnóstico de malnutrición no son equivalentes. El sistema conserva componentes; no completa los ausentes.

```text
G3-OBS/SEM-MOD-006 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 12.2. G4-CON

Consecuencias: diagnosticar desde IMC aislado (`CON-NUT-SINGLE-001`), mezclar instrumentos (`CON-NUT-INST-001`), ignorar aplicabilidad (`CON-NUT-APP-001`) o convertir cribado en diagnóstico (`CON-NUT-SCREEN-001`). El soporte nutricional no se constituye.

```text
G4-CON/SEM-MOD-006 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 12.3. G5-ATM

#### PAR-MALNUTRITION-ASSESS-POS-001

> Una evaluación nutricional diagnóstica, verificada y aplicable satisface el criterio positivo de malnutrición mediante un instrumento, componentes y umbrales explícitos y versionados.

```text
I_MALNUTRITION_ASSESS_POS_v0.1(X) -> {0,1,U}
```

Aquí la regla no remite a un criterio innominado: la entrada debe contener identificador del instrumento, versión, componentes requeridos, umbrales y lógica de combinación. `1` resulta de ejecutar esa lógica; `0` exige evaluación diagnóstica completa que no la satisface; `U` cubre instrumento, componentes, unidades, umbrales, aplicabilidad, verificación, conflicto o procedencia insuficientes.

No se acepta un cribado positivo como diagnóstico, ni se infiere intervención.

```text
PAR-MALNUTRITION-ASSESS-POS-001 = PARAMETRO_ATOMICO
G5-ATM/SEM-MOD-006 = PARAMETRO_ATOMICO
A0_20 = A0_19 + {PAR-MALNUTRITION-ASSESS-POS-001}
```

Al alcanzarse `|A0| = 20`, la secuencia se detiene. `SEM-MOD-007` no se abre.

## 13. Registro de los catorce parámetros nuevos

| Orden | Parametro_ID | Predicado único | Naturaleza |
|---:|---|---|---|
| 7 | `PAR-INF-HOSP-HIST-001` | infección previa causó ingreso | acontecimiento enlazado |
| 8 | `PAR-INF-ORGSUP-HIST-001` | infección previa requirió soporte orgánico | acontecimiento enlazado |
| 9 | `PAR-OI-DOC-HIST-001` | antecedente verificado clasificado oportunista | documental clínico |
| 10 | `PAR-MDRO-COL-DOC-001` | colonización resistente vigente bajo tabla explícita | documental-comparativo |
| 11 | `PAR-ACUTECARE-ENC-HIST-001` | ingreso agudo intersecta ventana | temporal documental |
| 12 | `PAR-INV-PROC-HIST-001` | procedimiento invasivo intersecta ventana | temporal documental |
| 13 | `PAR-DM-DOC-ACTIVE-001` | diabetes verificada activa | documental clínico |
| 14 | `PAR-HF-DOC-ACTIVE-001` | insuficiencia cardiaca verificada activa | documental clínico |
| 15 | `PAR-CKD-DOC-ACTIVE-001` | enfermedad renal crónica verificada activa | documental clínico |
| 16 | `PAR-KRT-ACTIVE-001` | tratamiento renal sustitutivo activo | documental clínico |
| 17 | `PAR-BRONCHIECTASIS-DOC-ACTIVE-001` | bronquiectasias verificadas activas | documental clínico |
| 18 | `PAR-RESP-SUPPORT-ACTIVE-001` | soporte respiratorio crónico activo | documental clínico |
| 19 | `PAR-CIRRHOSIS-DOC-ACTIVE-001` | cirrosis verificada activa | documental clínico |
| 20 | `PAR-MALNUTRITION-ASSESS-POS-001` | evaluación diagnóstica satisface regla explícita | comparativo versionado |

## 14. Prueba consolidada de atomicidad

| Condición `NA0-MATH` | Resultado |
|---|---|
| identidad | cada parámetro tiene sujeto y predicado únicos |
| estado único | `0/1/U` no oculta subestados independientes |
| `U` propia | cobertura, identidad, tiempo, verificación y procedencia se localizan por transductor |
| consecuencia separable | G4 permanece fuera del valor |
| función separable | no se incorporan riesgo, veto, intervención ni ruta |
| variación independiente | ingreso/soporte, encuentro/procedimiento, CKD/KRT y bronquiectasias/soporte pueden divergir |
| ablación | retirar cualquiera elimina una distinción no reconstruible por los demás |
| no partición material | cada hijo termina en una sola afirmación gobernable; restos quedan identificados |
| reproducción | mismas entradas, tablas, ventanas y versiones producen igual estado y traza |
| procedencia | toda afirmación o acontecimiento exige fuente anterior a la conclusión |

Los parámetros documentales no se presentan como diagnósticos computados. Su estado significa que una condición o acontecimiento clínico verificado consta con cobertura, vigencia y terminología suficientes. Esta limitación forma parte de su identidad y evita que una mención aislada se convierta en verdad clínica.

## 15. Adversarial integrada

### A. Recuperar los cuatro candidatos reparados por cuota

Rechazado. Permanecen en `U_REQUIERE_REGLA` y no figuran en `A0`.

### B. Contar preguntas o campos

Rechazado. Sólo entran proposiciones clínicas con transductor y ablación.

### C. Código igual a diagnóstico

Rechazado. Código sin verificación, estado, sujeto, tiempo y procedencia produce `U`.

### D. Medicación igual a enfermedad

Rechazado para diabetes, insuficiencia cardiaca, CKD, bronquiectasias y cirrosis.

### E. Hospitalización igual a infección grave

Rechazado. El ingreso debe estar atribuido explícitamente al episodio infeccioso.

### F. UCI igual a soporte orgánico

Rechazado. Se exige modalidad de soporte y vínculo con el episodio.

### G. Microorganismo igual a oportunismo

Rechazado. Se conserva la clasificación clínica con huésped, sitio y contexto.

### H. Colonización igual a infección

Rechazado. Son estados distintos y no compensables.

### I. Antibiótico igual a resistencia

Rechazado. Resistencia exige resultado y taxonomía explícitos.

### J. Silencio igual a `0`

Rechazado. `0` exige cobertura suficiente; de otro modo `U`.

### K. Ventana innominada

Rechazado. Las comparaciones temporales reciben una ventana explícita y versionada como operando.

### L. eGFR aislada igual a CKD

Rechazado. El parámetro representa condición crónica verificada, no diagnóstico inferido.

### M. Dispositivo igual a KRT

Rechazado. Acceso vascular no constituye modalidad renal activa.

### N. Síntoma igual a bronquiectasias

Rechazado. Se exige diagnóstico verificado.

### O. Oxígeno puntual igual a soporte crónico

Rechazado. Estado, modalidad, indicación y horizonte deben constar.

### P. Prueba hepática igual a cirrosis

Rechazado. No se diagnostica desde observaciones aisladas.

### Q. Cribado nutricional igual a diagnóstico

Rechazado. Se exige evaluación diagnóstica, componentes y lógica versionada.

### R. Criterio innominado

Rechazado. Los transductores documentales verifican afirmaciones existentes; los comparativos reciben códigos, tablas, ventanas o instrumentos completos como operandos identificados.

### S. Parámetro documental presentado como verdad biológica

Rechazado. La identidad declara expresamente qué fue verificado y documentado.

### T. `U` como NO GO global

Rechazado. Criticidad y tratamiento de `U` pertenecen a G7.

### U. Ajuste terapéutico desde modificador

Rechazado. No se calcula dosis, pauta, indicación ni contraindicación.

### V. Elegir raíces por positividad

Rechazado. Se recorren once raíces contiguas; `SEM-HIS-003` termina sin parámetro.

### W. Abrir G6 por alcanzar veinte

Rechazado. El punto requiere revisión externa y decisión del Director.

**Dictamen adversarial integrado:** `PASA`.

## 16. Recuentos

| Magnitud | Valor |
|---|---:|
| raíces recorridas | 11 |
| raíces con parámetro | 10 |
| raíces en `U_ATOMICIDAD_NO_CONSTITUIDA` | 1 |
| parámetros de entrada | 6 |
| parámetros nuevos | 14 |
| parámetros totales | 20 |
| candidatos reparados recuperados | 0 |
| diagnósticos inferidos por el sistema | 0 |
| umbrales universales nuevos | 0 |
| matrices, rutas o frames | 0 |
| nuevas raíces Q0 | 0 |
| documentos auxiliares | 0 |

## 17. Estado de parada

```text
A0 = {
  PAR-GC-PLAN-SYS-001,
  PAR-IGG-DEF-Q-001,
  PAR-SPL-ANAT-ABS-001,
  PAR-ANC-DEF-Q-001,
  PAR-IV-DEVICE-PRESENT-001,
  PAR-IMPLANT-PRESENT-001,
  PAR-INF-HOSP-HIST-001,
  PAR-INF-ORGSUP-HIST-001,
  PAR-OI-DOC-HIST-001,
  PAR-MDRO-COL-DOC-001,
  PAR-ACUTECARE-ENC-HIST-001,
  PAR-INV-PROC-HIST-001,
  PAR-DM-DOC-ACTIVE-001,
  PAR-HF-DOC-ACTIVE-001,
  PAR-CKD-DOC-ACTIVE-001,
  PAR-KRT-ACTIVE-001,
  PAR-BRONCHIECTASIS-DOC-ACTIVE-001,
  PAR-RESP-SUPPORT-ACTIVE-001,
  PAR-CIRRHOSIS-DOC-ACTIVE-001,
  PAR-MALNUTRITION-ASSESS-POS-001
}

|A0| = 20
OBJETIVO_INTERMEDIO = ALCANZADO
SIGUIENTE_RAIZ_NO_ABIERTA = SEM-MOD-007
G6-MAT = NO_ABIERTA
G7-RUT = NO_ABIERTA
APTITUD_CLINICA_OP-IMM-001 = NO_DECLARADA
DECISION_ASISTENCIAL = NINGUNA
```

La secuencia queda detenida para revisión de sustancia. Alcanzar veinte parámetros no demuestra suficiencia de la operación ni autoriza matriz, ruta o actuación.
