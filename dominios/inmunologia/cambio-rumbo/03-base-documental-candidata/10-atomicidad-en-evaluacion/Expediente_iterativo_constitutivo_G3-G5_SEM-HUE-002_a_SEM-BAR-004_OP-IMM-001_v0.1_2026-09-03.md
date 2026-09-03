# Expediente iterativo constitutivo G3–G5 — SEM-HUE-002 a SEM-BAR-004 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Base exacta:** `6ab57e9fdcad0c584a77401f72feaa75fa4e7294`
- **Operación:** `OP-IMM-001`
- **Universo:** `Q0 v0`, 32 raíces exactas
- **Tramo:** `SEM-HUE-002`, `SEM-HUE-003`, `SEM-HUE-004`, `SEM-HUE-005`, `SEM-BAR-001`, `SEM-BAR-002`, `SEM-BAR-003`, `SEM-BAR-004`
- **Puertas ejecutadas:** `G3-OBS → G4-CON → G5-ATM`, sin inversión dentro de cada raíz
- **Estatuto:** `EXPEDIENTE_SUSTANTIVO_SECUENCIAL_CERRADO`
- **Efecto clínico:** ninguno
- **Autorización asistencial:** ninguna

## 0. Objeto, método y límite

Este expediente continúa de manera iterativa el corte `OP-IMM-001 / Q0 v0` hasta que el conjunto autorizado alcance diez parámetros. No selecciona raíces por facilidad de adopción: continúa el orden material del bloque huésped y después el bloque barrera o dispositivo.

La economía documental no altera la secuencia. Cada transacción de raíz contiene, en este orden:

1. entrada procedente de `G2-SEM`;
2. cierre observacional `G3-OBS`;
3. cierre de consecuencias candidatas `G4-CON`;
4. prueba de atomicidad `G5-ATM`;
5. actualización de `A0` sólo después del cierre de las dependencias anteriores.

La raíz siguiente no se considera ejecutada hasta que la anterior tiene salida terminal. La agrupación material no fusiona raíces, no crea una puerta nueva y no permite usar una conclusión posterior como premisa anterior.

El criterio de parada es:

```text
|A0| = 10 parametros adoptados
```

No significa diez valores positivos, diez decisiones clínicas ni diez resultados de paciente. Este expediente constituye tipos de parámetro y sus transductores ternarios; no los evalúa sobre un caso real.

## 1. Fuentes y autoridad

| Fuente_ID | Fuente | Función permitida |
|---|---|---|
| `SRC-HB-001` | HL7 FHIR R5, `Observation` | estructura de medición o afirmación: código, sujeto, tiempo, estado, valor, método, espécimen, interpretación, intervalo y procedencia; no diagnóstico |
| `SRC-HB-002` | HL7 FHIR R5, `Condition` | estructura de una condición documentada, verificación y temporalidad; no constituye verdad clínica por codificación |
| `SRC-HB-003` | HL7 FHIR R5, `DeviceUsage` | estructura de uso o presencia documentada de dispositivo; no demuestra infección ni indicación de retirada |
| `SRC-HB-004` | LOINC `2465-3` | identidad de IgG expresada como masa/volumen en suero o plasma; no fija intervalo universal |
| `SRC-HB-005` | LOINC `751-8` | identidad del recuento absoluto de neutrófilos en sangre; no fija por sí solo neutropenia, gravedad o actuación |
| `SRC-HB-006` | CLSI EP28 | disciplina para establecer y verificar intervalos de referencia; no importa un intervalo entre poblaciones o métodos |
| `SRC-HB-007` | CDC, *Altered Immunocompetence*, General Best Practices for Immunization | reconoce la asplenia anatómica y funcional como condiciones de inmunocompetencia alterada para decisiones preventivas posteriores; no constituye aquí una pauta vacunal |
| `SRC-HB-008` | CDC, *Guidelines for the Prevention of Intravascular Catheter-Related Infections* | fundamenta que tipo, localización, duración y manipulación del acceso son distinciones materiales; no convierte presencia en infección |
| `SRC-HB-009` | contrato `NA0-MATH` v0.3 | identidad, estados `0/1/U`, ablación, propiedad única, procedencia y reproducción |
| `SRC-HB-010` | `BRG-IMMEXP-HISTORY-001` | contextualiza exposición previa o concurrente a inmunoglobulina; no cuantifica aporte exógeno |

Enlaces de control:

- https://hl7.org/fhir/R5/observation.html
- https://hl7.org/fhir/R5/condition.html
- https://hl7.org/fhir/R5/deviceusage.html
- https://loinc.org/2465-3
- https://loinc.org/751-8
- https://clsi.org/standards/products/method-evaluation/documents/ep28/
- https://www.cdc.gov/vaccines/hcp/imz-best-practices/altered-immunocompetence.html
- https://www.cdc.gov/infection-control/hcp/intravascular-catheter-related-infection/

Los estándares de intercambio identifican objetos y transportan afirmaciones. La validez clínica procede de la regla explícita, la fuente profesional autorizada, su aplicabilidad y la procedencia anterior a la conclusión.

## 2. Transacción 1 — SEM-HUE-002

### 2.1. Entrada

> ¿Existe una alteración cuantitativa de inmunoglobulina G pertinente para el episodio?

`G3-OBS/SEM-HUE-002` ya está cerrado en la base con una entidad, quince observables, cinco normalizadores y quince causas tipadas de `U`. La concentración total permanece separada de subclases, anticuerpos específicos, función humoral, fracción gamma, componente monoclonal y aporte exógeno.

### 2.2. G4-CON — consecuencias candidatas

| Consecuencia_ID | Omisión o error | Consecuencia potencial | Límite |
|---|---|---|---|
| `CON-IGG-ID-001` | sustituir IgG total por fracción, subclase o anticuerpo específico | clasificación de un objeto distinto como si fuese la magnitud requerida | no diagnostica inmunodeficiencia |
| `CON-IGG-REF-001` | aplicar intervalo no concordante con método, población o versión | falso estado de alteración o falsa normalidad | no fija rango universal |
| `CON-IGG-TIME-001` | usar medición no vigente o resultado sustituido | perfil referido a un estado temporal incorrecto | no fija ventana clínica |
| `CON-IGG-EXO-001` | ignorar o imputar cuantitativamente inmunoglobulina exógena | atribución no demostrada del valor observado | no calcula producción endógena |
| `CON-IGG-FUNC-001` | equiparar concentración con competencia humoral | falsa clausura de `SEM-HUE-003` | no valora respuesta específica |

Estas consecuencias son candidatas de representación y uso futuro. No son causalidad individual, riesgo cuantificado, indicación de reposición ni pauta preventiva.

```text
G4-CON/SEM-HUE-002 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 2.3. G5-ATM — adjudicación

La raíz contiene direcciones cuantitativas con consecuencias potencialmente distintas. Para evitar un parámetro multiafirmativo, sólo se adopta en este corte el predicado de déficit cuantitativo relativo a una referencia aplicable. El exceso queda como residuo, porque `OP-IMM-001` no ha constituido todavía una función necesaria para usarlo.

#### PAR-IGG-DEF-Q-001

> La concentración documentada de IgG total es inferior al límite inferior de un intervalo de referencia aplicable, versionado y concordante con analito, propiedad, espécimen, método y población.

```text
I_IGG_DEF_Q_v0.1(X, h) -> {0,1,U}
```

- `1`: medición final o válidamente corregida, vigente para `h`, por debajo del límite aplicable, sin conflicto material y con procedencia completa.
- `0`: medición válida y vigente igual o superior al límite inferior aplicable; no significa competencia humoral normal.
- `U`: identidad, valor, unidad, método, espécimen, referencia, aplicabilidad, vigencia, calidad, aporte exógeno material o procedencia no permiten resolver.
- fallo técnico: `EJECUCION_TECNICA_NO_VALIDA`.

La ablación impide distinguir un déficit cuantitativo de IgG de la ausencia de medición o de la función específica. El parámetro no contiene causa, persistencia, gravedad, diagnóstico, riesgo, indicación ni tratamiento.

```text
PAR-IGG-DEF-Q-001 = PARAMETRO_ATOMICO
IGG_POR_ENCIMA_DEL_LIMITE_SUPERIOR = RESIDUAL_PARA_VERSION_POSTERIOR
G5-ATM/SEM-HUE-002 = CERRADA_MIXTA
A0_2 = {PAR-GC-PLAN-SYS-001, PAR-IGG-DEF-Q-001}
```

## 3. Transacción 2 — SEM-HUE-003

### 3.1. G3-OBS — respuesta humoral específica

Entidad finita:

```text
E_HUM_SPEC = <
  Evaluacion_ID,
  Antigeno_o_panel,
  Exposicion_inductora,
  Fecha_y_hora_de_exposicion,
  Especimen,
  Metodo_y_plataforma,
  Resultado_por_componente,
  Unidad_o_escala,
  Momento_de_muestra,
  Criterio_interpretativo,
  Poblacion_y_finalidad,
  Estado_y_calidad,
  Contexto_de_inmunoglobulina_exogena,
  Procedencia_por_campo,
  Version
>
```

Observables candidatos cerrados: identidad de evaluación; antígeno o panel; exposición inductora documentada; momento de exposición; relación muestra–exposición; espécimen; método; resultado por componente; unidad o escala; criterio interpretativo; población; finalidad; estado; calidad; aporte exógeno; procedencia; versión. Son diecisiete campos finitos y no originan subraíces.

Separaciones obligatorias:

1. anticuerpo específico medido no equivale a protección clínica completa;
2. concentración total de IgG no equivale a respuesta específica;
3. vacuna prescrita, administrada y respuesta evaluable son sucesos distintos;
4. una determinación aislada no demuestra incremento, persistencia ni memoria;
5. criterios para un antígeno, panel, ensayo o finalidad no se transportan a otro;
6. inmunoglobulina exógena puede afectar la interpretación sin permitir una resta inventada.

Normalizadores: `N_HUM_SPEC_ID`, `N_HUM_SPEC_TIME`, `N_HUM_SPEC_RESULT`, `N_HUM_SPEC_CRITERION` y `N_HUM_SPEC_EXOGENO`. Todos devuelven objeto normalizado o `U`; ninguno produce por sí solo suficiencia clínica.

```text
G3-OBS/SEM-HUE-003 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 3.2. G4-CON

| Consecuencia_ID | Omisión o error | Consecuencia potencial |
|---|---|---|
| `CON-HUM-ID-001` | mezclar antígenos, paneles o ensayos | atribuir a un objeto una respuesta de otro |
| `CON-HUM-TIME-001` | ignorar relación temporal con exposición | interpretar una muestra no evaluable |
| `CON-HUM-CRIT-001` | trasladar criterio entre paneles o finalidades | falsa suficiencia o falsa alteración |
| `CON-HUM-EXO-001` | ignorar aporte exógeno material | atribución endógena no demostrada |
| `CON-HUM-PROT-001` | equiparar resultado analítico con protección | falsa conclusión clínica y preventiva |

```text
G4-CON/SEM-HUE-003 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 3.3. G5-ATM

#### PAR-HUM-SPEC-ALTER-001

> Una evaluación documentada de respuesta humoral específica satisface el estado de respuesta alterada conforme al criterio versionado aplicable al antígeno o panel, ensayo, población, momento y finalidad declarados.

```text
I_HUM_SPEC_ALTER_v0.1(X, h, finalidad) -> {0,1,U}
```

- `1`: evaluación completa y válida que satisface el criterio explícito de alteración.
- `0`: evaluación completa y válida que no lo satisface; no significa protección total ni inmunidad esterilizante.
- `U`: exposición inductora, cronología, panel, resultado, método, criterio, aplicabilidad, calidad, aporte exógeno o procedencia insuficientes o discordantes.

El criterio forma parte de la entrada versionada, no del identificador universal. La ablación elimina una distinción que IgG total y vacunación administrada no pueden reconstruir.

```text
PAR-HUM-SPEC-ALTER-001 = PARAMETRO_ATOMICO
G5-ATM/SEM-HUE-003 = PARAMETRO_ATOMICO
A0_3 = A0_2 + {PAR-HUM-SPEC-ALTER-001}
```

## 4. Transacción 3 — SEM-HUE-004

### 4.1. G3-OBS — anatomía y función esplénicas

La pregunta contiene dos predicados separables. Se constituyen dos entidades enlazables, no intercambiables:

```text
E_SPL_ANAT = <Estado_anatomico, procedimiento_o_imagen, extension, lateralidad,
              fecha_relevante, estado_de_verificacion, procedencia, version>

E_SPL_FUNC = <Afirmacion_funcional, metodo_o_fundamento, resultado,
              criterio_interpretativo, fecha_relevante, estado_de_verificacion,
              procedencia, version>
```

Observables finitos: presencia anatómica; esplenectomía total o parcial; remanente documentado; fecha; fuente anatómica; afirmación funcional; prueba o fundamento; resultado; criterio; temporalidad; verificación; conflicto; procedencia; versión.

Queda prohibido inferir función desde tamaño, esplenomegalia, infiltración, cirugía parcial o imagen anatómica aislada. También se prohíbe inferir anatomía ausente desde una afirmación funcional.

```text
G3-OBS/SEM-HUE-004 = OBSERVABLES_CANDIDATOS_CERRADOS_CON_PARTICION_FINITA
```

### 4.2. G4-CON

| Consecuencia_ID | Error | Consecuencia potencial |
|---|---|---|
| `CON-SPL-ANAT-001` | omitir ausencia anatómica o confundir parcial con total | perfil preventivo incompleto o incorrecto |
| `CON-SPL-FUNC-001` | asumir función por presencia anatómica | falsa normalidad funcional |
| `CON-SPL-SIZE-001` | usar tamaño como función | clasificación no demostrada |
| `CON-SPL-MIX-001` | colapsar anatomía y función | pérdida de estados divergentes y de `U` propia |

La repercusión sobre vacunación, educación, profilaxis, urgencia febril o tratamiento pertenece a G7 y a la autoridad clínica; no se constituye aquí.

```text
G4-CON/SEM-HUE-004 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 4.3. G5-ATM

#### PAR-SPL-ANAT-ABS-001

> Existe ausencia anatómica completa del bazo, documentada y verificada para el horizonte del episodio.

```text
I_SPL_ANAT_ABS_v0.1(X,h) -> {0,1,U}
```

`1` exige ausencia completa verificada; `0` exige presencia anatómica documentada y no afirma función; `U` cubre procedimiento o anatomía parcial, fuente insuficiente, conflicto, temporalidad o verificación no resolubles.

#### PAR-SPL-FUNC-LOSS-001

> Existe pérdida funcional esplénica documentada conforme a una afirmación o evaluación clínica autorizada, con fundamento, criterio y versión explícitos.

```text
I_SPL_FUNC_LOSS_v0.1(X,h) -> {0,1,U}
```

`1` exige criterio satisfecho y procedencia; `0` exige evaluación funcional válida que no lo satisface y no se obtiene de la mera presencia anatómica; `U` cubre ausencia de evaluación, fundamento, criterio, vigencia, verificación o concordancia.

Los dos parámetros varían independientemente, tienen `U` propias y su ablación elimina información no reconstruible por el otro. Ninguno prescribe una actuación.

```text
PAR-SPL-ANAT-ABS-001 = PARAMETRO_ATOMICO
PAR-SPL-FUNC-LOSS-001 = PARAMETRO_ATOMICO
G5-ATM/SEM-HUE-004 = COMPUESTO_PARTICIONADO_FINITO
A0_5 = A0_3 + {PAR-SPL-ANAT-ABS-001, PAR-SPL-FUNC-LOSS-001}
```

## 5. Transacción 4 — SEM-HUE-005

### 5.1. G3-OBS — compartimento neutrofílico

Entidad:

```text
E_ANC = <Medicion_ID, analito, propiedad, especimen, instante, valor_original,
         unidad_original, metodo, estado, calidad, intervalo_de_referencia,
         poblacion_y_condiciones, interpretacion_emitida, vinculo_de_serie,
         procedencia, version>
```

Quince observables y cuatro normalizadores quedan cerrados: identidad, magnitud/unidad, referencia aplicable y serie comparable. El recuento absoluto no se sustituye por leucocitos totales, porcentaje, formas inmaduras, morfología ni una etiqueta textual. Una serie no constituye duración ni trayectoria clínica.

La población y el intervalo se conservan de forma explícita. En particular, un recuento basal asociado al fenotipo Duffy nulo no puede reinterpretarse por un rango ajeno sin comprobar aplicabilidad. Esta cautela no constituye genotipo, etiología ni ausencia de riesgo.

```text
G3-OBS/SEM-HUE-005 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 5.2. G4-CON

| Consecuencia_ID | Omisión o error | Consecuencia potencial |
|---|---|---|
| `CON-ANC-ID-001` | usar porcentaje o leucocitos como ANC | estado cuantitativo falso |
| `CON-ANC-REF-001` | intervalo no aplicable | sobrediagnóstico o infradetección de descenso |
| `CON-ANC-TIME-001` | resultado no vigente o sustituido | perfil temporal incorrecto |
| `CON-ANC-TREND-001` | una medida como duración | falsa persistencia o recuperación |
| `CON-ANC-ACT-001` | cifra como actuación automática | salto desde medición a decisión |

```text
G4-CON/SEM-HUE-005 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 5.3. G5-ATM

#### PAR-ANC-DEF-Q-001

> El recuento absoluto documentado de neutrófilos es inferior al límite inferior de un intervalo de referencia aplicable y versionado para el método, población y condiciones declarados.

```text
I_ANC_DEF_Q_v0.1(X,h) -> {0,1,U}
```

`1` exige medición válida, vigente y por debajo del límite aplicable; `0` exige medición válida igual o superior y no significa función neutrofílica normal, etiología resuelta ni ausencia de riesgo; `U` cubre identidad, valor, unidad, espécimen, método, calidad, referencia, aplicabilidad, vigencia, discordancia o procedencia insuficientes.

El grado, la duración, la función, la causa, el nadir previsto y la actuación permanecen fuera del parámetro. La dirección alta no se adopta: puede ser relevante para `SEM-RUT-001`, pero no se ha constituido como necesidad propia del perfil basal.

```text
PAR-ANC-DEF-Q-001 = PARAMETRO_ATOMICO
ANC_POR_ENCIMA_DEL_LIMITE_SUPERIOR = REFERENCIA_A_SEM-RUT-001_O_RESIDUAL
G5-ATM/SEM-HUE-005 = CERRADA_MIXTA
A0_6 = A0_5 + {PAR-ANC-DEF-Q-001}
```

## 6. Transacción 5 — SEM-BAR-001

### 6.1. G3-OBS — integridad cutánea

Entidad:

```text
E_SKIN_BARRIER = <Evaluacion_ID, region, extension, profundidad_o_tipo,
                  estado_de_integridad, signos_asociados_documentados,
                  dispositivo_o_procedimiento_relacionado, instante,
                  metodo_de_evaluacion, estado_de_verificacion,
                  procedencia, version>
```

La piel se registra por región y evaluación. No se fusiona con mucosa, catéter, prótesis, infección, colonización, herida quirúrgica o diagnóstico dermatológico. La ausencia de evaluación no equivale a integridad.

```text
G3-OBS/SEM-BAR-001 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 6.2. G4-CON

Consecuencias candidatas: omitir una discontinuidad documentada (`CON-SKIN-OMI-001`), confundir lesión con infección (`CON-SKIN-INF-001`), fusionar regiones o versiones (`CON-SKIN-REG-001`) y trasladar un criterio de mucosa o dispositivo (`CON-SKIN-XFER-001`). Pueden producir un perfil de puerta de entrada incompleto o una infección falsamente afirmada; no determinan una actuación.

```text
G4-CON/SEM-BAR-001 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 6.3. G5-ATM

#### PAR-SKIN-BARRIER-LOSS-001

> Existe una pérdida de integridad cutánea pertinente documentada en una región y horizonte definidos, conforme a un criterio clínico autorizado y versionado.

```text
I_SKIN_BARRIER_LOSS_v0.1(X,h,finalidad) -> {0,1,U}
```

`1` exige criterio satisfecho; `0` exige evaluación suficiente de la cobertura declarada sin pérdida pertinente y no se obtiene del silencio; `U` cubre cobertura corporal, región, tipo, extensión, instante, criterio, verificación, conflicto o procedencia insuficientes.

El parámetro no afirma infección, colonización, etiología, gravedad, necesidad de cultivo, curación ni modificación terapéutica.

```text
PAR-SKIN-BARRIER-LOSS-001 = PARAMETRO_ATOMICO
G5-ATM/SEM-BAR-001 = PARAMETRO_ATOMICO
A0_7 = A0_6 + {PAR-SKIN-BARRIER-LOSS-001}
```

## 7. Transacción 6 — SEM-BAR-002

### 7.1. G3-OBS — integridad mucosa

Entidad:

```text
E_MUCOSA_BARRIER = <Evaluacion_ID, territorio_mucoso, extension,
                    tipo_de_alteracion, estado_de_integridad,
                    signos_asociados_documentados, instante,
                    metodo_de_evaluacion, estado_de_verificacion,
                    procedencia, version>
```

Territorios oral, orofaríngeo, gastrointestinal, respiratorio, genitourinario u otros declarados conservan identidad. No se deduce integridad global desde un único territorio. Mucositis, ulceración, inflamación, infección y síntomas no son equivalentes sin regla explícita.

```text
G3-OBS/SEM-BAR-002 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 7.2. G4-CON

Consecuencias candidatas: generalización desde un territorio (`CON-MUC-COV-001`), equiparar síntoma o inflamación a discontinuidad (`CON-MUC-ID-001`), confundir alteración con infección (`CON-MUC-INF-001`) y mezclar piel con mucosa (`CON-MUC-XFER-001`). No constituyen causalidad, intervención ni riesgo numérico.

```text
G4-CON/SEM-BAR-002 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 7.3. G5-ATM

#### PAR-MUCOSA-BARRIER-LOSS-001

> Existe una pérdida de integridad mucosa pertinente, documentada en un territorio y horizonte definidos conforme a un criterio clínico autorizado y versionado.

```text
I_MUCOSA_BARRIER_LOSS_v0.1(X,h,finalidad) -> {0,1,U}
```

`1` exige criterio satisfecho; `0` exige evaluación suficiente del territorio y cobertura declarados; `U` cubre territorio, cobertura, tipo, extensión, temporalidad, criterio, verificación, conflicto o procedencia insuficientes.

No afirma infección, translocación, colonización, diagnóstico, gravedad, tratamiento ni contraindicación.

```text
PAR-MUCOSA-BARRIER-LOSS-001 = PARAMETRO_ATOMICO
G5-ATM/SEM-BAR-002 = PARAMETRO_ATOMICO
A0_8 = A0_7 + {PAR-MUCOSA-BARRIER-LOSS-001}
```

## 8. Transacción 7 — SEM-BAR-003

### 8.1. G3-OBS — dispositivo intravascular

Entidad:

```text
E_IV_DEVICE = <Dispositivo_ID, tipo, localizacion, lateralidad,
               fecha_de_insercion, estado_de_presencia, finalidad,
               acceso_o_manipulacion_documentados, fecha_de_retirada,
               estado_de_verificacion, procedencia, version>
```

La presencia se separa de infección, colonización, permeabilidad, indicación, manejo, retirada y complicación. Un puerto, catéter central, línea periférica y otros tipos no se vuelven clínicamente equivalentes por compartir la categoría intravascular.

```text
G3-OBS/SEM-BAR-003 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 8.2. G4-CON

Consecuencias candidatas: omitir presencia (`CON-IVD-OMI-001`), confundir tipo o localización (`CON-IVD-ID-001`), mantener como presente un dispositivo retirado (`CON-IVD-TIME-001`) y equiparar presencia a infección (`CON-IVD-INF-001`). El error puede dejar incompleta la caracterización de barrera y exposición, pero no constituye retirada, cultivo o tratamiento.

```text
G4-CON/SEM-BAR-003 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 8.3. G5-ATM

#### PAR-IV-DEVICE-PRESENT-001

> Existe al menos un dispositivo intravascular presente y vigente en el horizonte predecisional, con identidad, tipo y localización documentados.

```text
I_IV_DEVICE_PRESENT_v0.1(X,h) -> {0,1,U}
```

`1` exige presencia vigente verificada; `0` exige cobertura explícitamente completa sin dispositivo presente; `U` cubre inventario parcial, identidad, tipo, localización, inserción o retirada, vigencia, conflicto, verificación o procedencia insuficientes.

No afirma infección asociada, colonización, necesidad de retirada, adecuación del acceso ni riesgo cuantificado.

```text
PAR-IV-DEVICE-PRESENT-001 = PARAMETRO_ATOMICO
G5-ATM/SEM-BAR-003 = PARAMETRO_ATOMICO
A0_9 = A0_8 + {PAR-IV-DEVICE-PRESENT-001}
```

## 9. Transacción 8 — SEM-BAR-004

### 9.1. G3-OBS — prótesis o biomaterial implantado

Entidad:

```text
E_IMPLANT = <Implante_ID, clase_y_tipo, material_si_consta,
             localizacion, fecha_de_implantacion, estado_de_presencia,
             finalidad, revision_o_retirada, estado_de_verificacion,
             procedencia, version>
```

Cada implante conserva identidad. Se separan presencia, infección, colonización, aflojamiento, fallo, indicación, revisión y retirada. Un implante no se convierte en catéter ni todos los biomateriales comparten consecuencia.

```text
G3-OBS/SEM-BAR-004 = OBSERVABLES_CANDIDATOS_CERRADOS
```

### 9.2. G4-CON

Consecuencias candidatas: omitir el implante (`CON-IMP-OMI-001`), perder tipo o localización (`CON-IMP-ID-001`), ignorar revisión o retirada (`CON-IMP-TIME-001`) y equiparar presencia a infección (`CON-IMP-INF-001`). Su uso concreto dependerá de matriz, ruta y finalidad posteriores.

```text
G4-CON/SEM-BAR-004 = CONSECUENCIA_CANDIDATA_CERRADA
```

### 9.3. G5-ATM

#### PAR-IMPLANT-PRESENT-001

> Existe al menos una prótesis o biomaterial implantado presente y vigente para el horizonte predecisional, con identidad, tipo y localización documentados.

```text
I_IMPLANT_PRESENT_v0.1(X,h) -> {0,1,U}
```

`1` exige presencia vigente verificada; `0` exige inventario explícitamente completo sin implante; `U` cubre cobertura parcial, identidad, tipo, localización, implantación, revisión o retirada, vigencia, conflicto, verificación o procedencia insuficientes.

No afirma infección, colonización, disfunción, riesgo cuantificado, necesidad de retirada, profilaxis ni cambio terapéutico.

```text
PAR-IMPLANT-PRESENT-001 = PARAMETRO_ATOMICO
G5-ATM/SEM-BAR-004 = PARAMETRO_ATOMICO
A0_10 = A0_9 + {PAR-IMPLANT-PRESENT-001}
```

Al alcanzarse `|A0| = 10`, la ejecución se detiene antes de `SEM-HIS-001`. No se abre `G6-MAT` por este expediente.

## 10. Registro canónico de los nueve parámetros nuevos

| Orden A0 | Parametro_ID | Sujeto | Predicado único | Transductor | No significa |
|---:|---|---|---|---|---|
| 2 | `PAR-IGG-DEF-Q-001` | medición válida de IgG total | inferior a referencia aplicable | `I_IGG_DEF_Q_v0.1` | competencia, causa, riesgo o reposición |
| 3 | `PAR-HUM-SPEC-ALTER-001` | evaluación específica válida | satisface criterio aplicable de alteración | `I_HUM_SPEC_ALTER_v0.1` | protección completa o pauta vacunal |
| 4 | `PAR-SPL-ANAT-ABS-001` | anatomía esplénica | ausencia completa documentada | `I_SPL_ANAT_ABS_v0.1` | pérdida funcional automática |
| 5 | `PAR-SPL-FUNC-LOSS-001` | función esplénica | pérdida documentada por criterio aplicable | `I_SPL_FUNC_LOSS_v0.1` | ausencia anatómica automática |
| 6 | `PAR-ANC-DEF-Q-001` | medición válida de ANC | inferior a referencia aplicable | `I_ANC_DEF_Q_v0.1` | función, causa, gravedad o actuación |
| 7 | `PAR-SKIN-BARRIER-LOSS-001` | evaluación cutánea | pérdida pertinente documentada | `I_SKIN_BARRIER_LOSS_v0.1` | infección o tratamiento |
| 8 | `PAR-MUCOSA-BARRIER-LOSS-001` | evaluación mucosa | pérdida pertinente documentada | `I_MUCOSA_BARRIER_LOSS_v0.1` | infección o integridad de otros territorios |
| 9 | `PAR-IV-DEVICE-PRESENT-001` | inventario intravascular | dispositivo presente y vigente | `I_IV_DEVICE_PRESENT_v0.1` | infección, retirada o riesgo cuantificado |
| 10 | `PAR-IMPLANT-PRESENT-001` | inventario de implantes | implante presente y vigente | `I_IMPLANT_PRESENT_v0.1` | infección, fallo o actuación |

Cada registro canónico incluye además: `Version_parametro=0.1`, familia, dominio de observables de su transacción, estados `{0,1,U}`, fuentes aplicadas, procedencia por campo anterior a la conclusión y autoridad de `OP-IMM-001`. La tabla no sustituye las reglas completas anteriores.

### 10.1. Prueba consolidada de atomicidad

| Prueba `NA0-MATH` | Resultado en los nueve parámetros | Evidencia de cierre |
|---|---|---|
| identidad | pasa | cada identificador tiene un sujeto y un predicado canónicos |
| estado único | pasa | cada evaluación responde una sola proposición ternaria |
| `U` propia | pasa | las causas están limitadas al dominio de observables y criterio de cada transductor |
| consecuencia separable | pasa | las consecuencias permanecen en G4 y ninguna se incorpora al valor del parámetro |
| función separable | pasa | ningún parámetro decide riesgo, intervención, ruta, autoridad o compensación |
| variación independiente | pasa | los pares IgG/función humoral, anatomía/función esplénica, piel/mucosa y dispositivo/implante pueden divergir |
| ablación | pasa | retirar cualquiera elimina una distinción no reconstruible por los otros nueve |
| no partición material pendiente | pasa con residuos explícitos | exceso de IgG y ANC quedan fuera del hijo adoptado; la raíz esplénica termina en dos hijos exhaustivos para su distinción declarada |
| reproducibilidad | pasa por contrato | mismas entradas, criterios y versiones producen el mismo estado y serialización |
| procedencia | pasa por construcción | todo campo decisivo exige origen y versión anteriores a la conclusión |

La prueba no certifica que el criterio clínico externo sea verdadero o útil. Certifica que, una vez autorizado y versionado, el sistema lo aplica sin cambiar la proposición, rellenar ausencias ni ocultar `U`.

## 11. Adversarial integrada

### A. Cuota positiva

**Ataque:** rebajar criterios para alcanzar diez parámetros.

**Resultado:** rechazado. Se recorren raíces contiguas por orden; exceso de IgG, exceso de ANC y acciones clínicas quedan fuera cuando no pasan necesidad o atomicidad.

### B. Parámetro igual a valor positivo

**Ataque:** contar sólo parámetros cuyo estado del paciente sea `1`.

**Resultado:** rechazado. Se constituyen tipos ternarios; no existe caso clínico evaluado.

### C. Intervalo universal

**Ataque:** fijar un umbral numérico único de IgG o ANC.

**Resultado:** rechazado. Método, población, espécimen, laboratorio, finalidad y versión gobiernan la aplicabilidad.

### D. Etiqueta de laboratorio como verdad SV

**Ataque:** transportar `L`, `H` o “anormal” directamente.

**Resultado:** rechazado. La interpretación fuente es observable; el transductor exige referencia aplicable y procedencia.

### E. Cantidad igual a función

**Ataque:** IgG cuantitativa resuelve respuesta específica; ANC resuelve función neutrofílica.

**Resultado:** rechazado. Son predicados distintos; la función no se infiere.

### F. Protección desde anticuerpo

**Ataque:** un resultado específico `0` demuestra protección completa.

**Resultado:** rechazado. Sólo niega el criterio de alteración dentro del panel, método, tiempo y finalidad declarados.

### G. Vacunación administrada igual a respuesta

**Ataque:** registro de vacuna sustituye muestra y criterio.

**Resultado:** rechazado. Exposición inductora y respuesta son sucesos distintos.

### H. Bazo presente igual a función conservada

**Ataque:** anatomía cierra función en `0`.

**Resultado:** rechazado. Los parámetros esplénicos varían independientemente.

### I. Esplenomegalia igual a hipofunción

**Ataque:** tamaño, infiltración o diagnóstico de base sustituyen evaluación funcional.

**Resultado:** rechazado. Producen contexto o `U`, nunca cierre automático.

### J. Duffy como corrección automática

**Ataque:** ascendencia o apariencia permiten cambiar el intervalo de ANC.

**Resultado:** rechazado. Sólo una condición documentada y una referencia aplicable pueden intervenir; no se infiere genotipo.

### K. Una medición igual a persistencia

**Ataque:** una IgG o ANC aislada fija trayectoria y vigencia futura.

**Resultado:** rechazado. Serie, comparabilidad y ventana permanecen separadas.

### L. Lesión igual a infección

**Ataque:** pérdida cutánea o mucosa produce infección presente.

**Resultado:** rechazado. Barrera, colonización e infección son objetos diferentes.

### M. Cobertura corporal falsa

**Ataque:** una región cutánea o territorio mucoso normal produce `0` global.

**Resultado:** rechazado. `0` exige cobertura declarada suficiente; lo parcial produce `U` localizada.

### N. Dispositivo igual a infección

**Ataque:** presencia intravascular produce infección asociada o retirada.

**Resultado:** rechazado. El parámetro sólo afirma presencia vigente.

### O. Implante igual a catéter

**Ataque:** fusionar todos los biomateriales bajo una regla.

**Resultado:** rechazado. Identidad, tipo, localización y función permanecen; las consecuencias se adjudicarán en G7.

### P. Silencio igual a ausencia

**Ataque:** asignar `0` porque el expediente no menciona barrera, dispositivo o implante.

**Resultado:** rechazado. `0` exige cobertura explícita y suficiente; el silencio produce `U`.

### Q. `U` como NO GO global

**Ataque:** cualquier indeterminación bloquea automáticamente todo el tratamiento.

**Resultado:** rechazado. `U` es local; sólo G7 puede constituir criticidad, veto, escalado o abstención.

### R. Determinismo igual a validez

**Ataque:** reproducción byte a byte demuestra corrección clínica.

**Resultado:** rechazado. Sólo demuestra fidelidad a entradas, reglas y versiones.

### S. Parámetros administrativos

**Ataque:** contar cada campo, normalizador o control como parámetro.

**Resultado:** rechazado. Los nueve nuevos objetos poseen proposición clínica única, variación independiente, `U` propia y ablación material.

### T. Salto a matriz o ruta

**Ataque:** asignar criticidad, propiedad, compensación, vacuna, profilaxis o actuación dentro de G5.

**Resultado:** rechazado. `G6-MAT` y `G7-RUT` no se abren.

### U. Inversión interna de secuencia

**Ataque:** usar el parámetro adoptado para justificar retrospectivamente observables o consecuencias.

**Resultado:** rechazado. Cada transacción declara G3, después G4 y sólo entonces G5; las fuentes y reglas no dependen de la salida buscada.

### V. Expansión silenciosa de Q0

**Ataque:** convertir región, antígeno, método o tipo de implante en raíces nuevas.

**Resultado:** rechazado. Son instancias finitas de las entidades; `Q0` permanece en 32.

### W. Cierre prematuro al llegar a diez

**Ataque:** declarar completa `OP-IMM-001` o el dominio.

**Resultado:** rechazado. Sólo se alcanza un punto de revisión de `A0`; quedan raíces y puertas posteriores.

**Dictamen adversarial integrado:** `PASA`.

## 12. Recuentos y preservación de finitud

| Magnitud | Valor |
|---|---:|
| raíces ejecutadas en este expediente | 8 |
| estados terminales G3 nuevos | 7 |
| dependencia G3 previa reutilizada | 1 |
| estados terminales G4 nuevos | 8 |
| estados terminales G5 nuevos | 8 |
| parámetros nuevos | 9 |
| parámetros totales en A0 | 10 |
| particiones materiales nuevas | 3 (`SEM-HUE-002`, `SEM-HUE-004` y `SEM-HUE-005`) |
| parámetros forzados desde observables | 0 |
| umbrales numéricos universales | 0 |
| diagnósticos o intervenciones constituidos | 0 |
| matrices, rutas o frames abiertos | 0 |
| raíces nuevas de Q0 | 0 |
| documentos auxiliares | 0 |

En `SEM-HUE-002` y `SEM-HUE-005`, la dirección inferior termina como parámetro y la superior como residuo o referencia expresa fuera del hijo adoptado; en `SEM-HUE-004`, anatomía y función terminan en hijos distintos. En los tres casos cada hijo conserva un subconjunto estricto de las distinciones del padre, por lo que `rho(hijo) < rho(padre)`. Las restantes raíces terminan sin partición. Métodos, regiones, territorios, antígenos y tipos son instancias finitas, no nodos de descomposición.

## 13. Conjunto autorizado y punto de revisión

```text
A0 = {
  PAR-GC-PLAN-SYS-001,
  PAR-IGG-DEF-Q-001,
  PAR-HUM-SPEC-ALTER-001,
  PAR-SPL-ANAT-ABS-001,
  PAR-SPL-FUNC-LOSS-001,
  PAR-ANC-DEF-Q-001,
  PAR-SKIN-BARRIER-LOSS-001,
  PAR-MUCOSA-BARRIER-LOSS-001,
  PAR-IV-DEVICE-PRESENT-001,
  PAR-IMPLANT-PRESENT-001
}
```

```text
|A0| = 10
OBJETIVO_INTERMEDIO = ALCANZADO
SIGUIENTE_RAIZ_NO_ABIERTA = SEM-HIS-001
G6-MAT = NO_ABIERTA
G7-RUT = NO_ABIERTA
APTITUD_CLINICA_OP-IMM-001 = NO_DECLARADA
DOMINIO_INMUNOLOGIA = NO_CERRADO
DECISION_ASISTENCIAL = NINGUNA
```

La revisión en este punto debe comprobar sustancia, no cuota: si los diez parámetros conservan identidad clínica, no esconden una decisión, pueden producir `0/1/U` sin rellenar ausencias, y su ablación altera de manera demostrable el perfil predecisional. Hasta esa revisión, no se continúa con `SEM-HIS-001` ni se abre propiedad matricial.
