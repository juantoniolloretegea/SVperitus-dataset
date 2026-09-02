# Recepción y cierre de auditoría externa G2-S1 — OP-IMM-001 v0.1

- **Fecha:** 02-09-2026
- **Commit material auditado:** `48b8a34c9f55832b7925a2391782e5d88c1b96bb`
- **Línea base G1:** `90938ec90bd086b69a0ffba683d23419cd8c8326`
- **Dictamen externo recibido:** `PASA`
- **Estatuto resultante:** `G2-S1_CERRADO`
- **Límite:** `G2_TOTAL_NO_CERRADO`; `G3-OBS` permanece bloqueada

## 1. Identidad y regresión aceptadas

La auditoría reprodujo los tres SHA-256 declarados, verificó los 23 identificadores únicos y confirmó que la regresión desde G1 se limita a los tres objetos de `07-preguntas-semanticas-en-evaluacion` y a la entrada correspondiente del índice rector. El catálogo INMUNO v0.8 permaneció idéntico.

## 2. Resultado A–J

| Ataque | Resultado recibido | Efecto registral |
|---|---|---|
| A · identidad y regresión | `PASA` | objeto exacto y cambio confinado |
| B · perímetro G2-S1 | `PASA` | no se constituyen parámetros ni reglas |
| C · integridad | `PASA` | 23 identificadores, distribución `1/4/5/4/4/5` |
| D · semántica abierta | `PASA` | términos operativos diferidos legítimamente |
| E · control y contexto | `PASA` | ruta, nosología, coordinación y viabilidad separadas |
| F · exposición propuesta | `PASA_CON_VIGILANCIA` | `SEM-EXP-004` queda bajo ataque posterior |
| G · estado del huésped | `PASA` | colisiones preservadas sin cierre prematuro |
| H · barreras e historia | `PASA` | propiedades separables y hechos compartibles |
| I · finitud | `PASA` | cierre del lote, no del universo semántico |
| J · no herencia | `PASA` | pilotos sin autoridad normativa |

## 3. Vigilancia R-01

`SEM-EXP-004` combina en su formulación una exposición concurrente y una exposición previa que conserve efecto clínico. La auditoría no lo considera defecto de G2 porque el lote prohíbe agregarlas en un estado y difiere la regla temporal.

Se constituye la siguiente deuda de prueba:

| ID | Puerta de destino | Ataque obligatorio |
|---|---|---|
| `VIG-G5-EXP-004` | `G5-ATM` | intentar separar exposición concurrente y exposición previa aún activa mediante ablación y casos divergentes |

La vigilancia no desdobla ahora la pregunta, no fija ventana y no constituye dos parámetros.

## 4. Cierre y límite

`G2-S1` queda cerrado porque sus 23 preguntas son diferenciables como candidatas, las colisiones prioritarias están declaradas y ninguna fila hereda estado, umbral o matriz de los pilotos.

El cierre no adjudica las preguntas como parámetros y no cierra `G2-SEM` para toda `OP-IMM-001`. Permanecen fuera de este lote, entre otros, compartimentos celulares adicionales, comorbilidades, epidemiología, inmunización, profilaxis, consentimiento, intervenciones y seguimiento.

Por tanto:

- `G2-S1_CERRABLE = SÍ`;
- `G2-S1_CERRADO = SÍ`;
- `G2_TOTAL_NO_CERRADO = SÍ`;
- `G3-OBS_AUTORIZADO = NO`.

## 5. Continuación autorizada

La continuación mínima es `G2-S2`, todavía dentro de la formulación semántica. Su perímetro inicial atacará compartimentos del huésped y modificadores generales excluidos de S1, sin crear observables, valores, umbrales, consecuencias, matrices ni recomendaciones.

Todo objeto posterior queda sometido antes de su publicación a la política transversal de protección de datos de salud y casos no atribuibles.

## 6. Declaración

Este cierre es registral y metodológico. No constituye adopción clínica, recomendación asistencial, observable, parámetro, transductor, consecuencia clínica, matriz, ruta, frame ni autorización para `G3-OBS`.

