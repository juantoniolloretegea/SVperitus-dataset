# Recepción y cierre de auditoría externa — `G3-S1` corticoides en `OP-IMM-001` v0.1

- **Fecha:** 02-09-2026
- **Rama:** `dominio-inmunologia`
- **Commit auditado:** `3117bcebac5280acf9b9878efa4d40a9fa67edf0`
- **Línea base:** `0d885602721d495bdfba87631f44eb2afbe98645`
- **Dictamen externo recibido:** `PASA`
- **Reparos:** ninguno
- **Estatuto de esta recepción:** `G3-S1_CERRADO`

## 1. Identidad recibida y confirmada

| Objeto auditado | Bytes | SHA-256 |
|---|---:|---|
| `Lote_observacional_G3-S1_corticoides_OP-IMM-001_v0.1_2026-09-02.md` | 13 716 | `49f15ef048230b3f8eb010bd11713121122102711efb8988b02156cc0221584c` |
| `Adversarial_interna_G3-S1_corticoides_OP-IMM-001_v0.1_2026-09-02.md` | 7 934 | `fad82e6467fc35dca9736edeeb5ca18c31becc95b0e8409870b3d1db41d95916` |

La auditoría externa calculó la misma identidad, comprobó el diff completo contra la línea base y confirmó que no se alteraron el catálogo v0.8, `Q0`, los lotes G2, el contrato matemático, los pilotos, la política de protección de datos, la ITI ni el Lenguaje SV.

## 2. Resultado material

Quedan cerrados para este recorte:

- tres preguntas G2 de origen: `SEM-EXP-002`, `SEM-EXP-003` y `SEM-EXP-005`;
- una entidad observacional `E_GC`;
- diez observables necesarios: `OBS-GC-001`–`OBS-GC-010`;
- cuatro normalizadores previos: `N_GC_ID`, `N_GC_MAG`, `N_GC_DUR` y `N_GC_REC`;
- once códigos de causa de `U`;
- procedencia por campo como metadato obligatorio, no como undécimo observable clínico.

Permanecen en cero las equivalencias, los umbrales, los parámetros atómicos, las matrices, las rutas y los frames.

## 3. Incertidumbres residuales aceptadas

### `U-RESIDUAL`

El efecto inmunológico residual, las equivalencias y los umbrales dependientes de finalidad no pertenecen a `G3-S1`. Su cierre exige una fuente versionada y una fase posterior competente. No se rellenan por memoria, promedio, dosis diaria definida ni inferencia generativa.

### `U-CODIGO`

`C_FORMULACION_VIA` puede mantenerse como código común mientras `Campo_afectado` preserve sin pérdida si la incertidumbre corresponde a formulación o a vía. Si una implementación perdiera esa distinción, el código deberá partirse antes de ser admisible.

Ninguna de estas incertidumbres constituye un reparo del lote auditado.

## 4. Decisión de puerta

`G3-S1` queda cerrado. Este cierre autoriza a abrir un lote `G4-CON` estrictamente acotado a las consecuencias de ignorar, confundir o trasladar indebidamente los observables ya constituidos para la exposición a glucocorticoides.

No autoriza:

- crear un umbral universal;
- adoptar una equivalencia farmacológica;
- prescribir vacunación o profilaxis;
- convertir un observable en parámetro atómico;
- diseñar matrices, rutas o frames;
- abrir `G5-ATM`;
- usar datos de episodios, personas o centros identificables.

## 5. Inmutabilidad

Los dos objetos auditados no se corrigen ni se reescriben. Toda consecuencia nueva se constituye en un lote posterior, con fuente, localizador, finalidad, cadena causal, incertidumbre y adversarial propios.

Esta recepción no constituye consejo, indicación, prescripción, autorización asistencial ni modificación del Lenguaje SV.
