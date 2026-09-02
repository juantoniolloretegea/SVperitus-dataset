# Recepción y cierre de auditoría externa — `G4-S1` consecuencias sobre glucocorticoides v0.1

- **Fecha:** 02-09-2026
- **Rama:** `dominio-inmunologia`
- **Commit auditado:** `5bb70c1d7293913150f66aa79da77a3275cefbd8`
- **Línea base:** `3117bcebac5280acf9b9878efa4d40a9fa67edf0`
- **Dictamen externo recibido:** `PASA`
- **Reparos:** ninguno
- **Estatuto:** `G4-S1_CERRADO`

## 1. Identidad aceptada

| Objeto | Bytes | SHA-256 |
|---|---:|---|
| lote `G4-S1` | 14 792 | `9ccaf6a544a669c08678e72ea5d3cb8beac5db531db5d4ecf482d10830974e25` |
| adversarial interna | 5 784 | `29dbf86e7ffa87188936718e2a0db6090c23bd9aebdd748e05e4810347b9569d` |
| recepción `G3-S1` | 3 216 | `c83f8c04155aedd18c59841620d0efb2c2af1282cb5c3839631e3f06fd38dc7c` |

La auditoría confirmó el diff completo, la inmutabilidad de `G3-S1` y la ausencia de cambios en catálogo v0.8, `Q0`, G2, `NA0-MATH`, pilotos, política de protección, ITI y Lenguaje SV.

## 2. Resultado material

Quedan cerradas para este recorte cinco consecuencias:

- dos epistemológicas: `CON-GC-REP-001` y `CON-GC-PUR-001`;
- tres clínicas potenciales: `CON-GC-VAC-SAF-001`, `CON-GC-VAC-EFF-001` y `CON-GC-PJP-001`.

La auditoría confirmó que ninguna está duplicada, incurre en salto causal o prescribe una actuación. Permanecen en cero umbrales, equivalencias, intervenciones, parámetros atómicos, matrices, rutas y frames.

## 3. Incertidumbres residuales aceptadas

- `U-FP-INT`: consecuencias de falsos positivos ligadas a una intervención concreta; requieren fuente y lote propios.
- `U-REGLA`: vacuna, población, umbral y balance permanecen ligados al futuro uso `u(p,O)`.
- `U-RESIDUAL`: el efecto inmunológico residual no se infiere ni se rellena en este lote.

No son reparos y no se abren ahora.

## 4. Freno contra el sesgo del primer recorte

`G4-S1` demuestra una cadena completa, pero no es muestra representativa de la inmunología ni puede determinar la tabla de parámetros o el tamaño de una matriz. Dos de sus tres consecuencias clínicas pertenecen a vacunación porque esa finalidad permitió probar la separación entre seguridad y efectividad; no adquieren prioridad estructural sobre el resto del dominio.

Por ello, este cierre no abre `G5-ATM`. La continuación vuelve a `G3-OBS` con un recorte no vacunal del estado inmunitario del huésped. La atomización se aplaza hasta disponer de diversidad suficiente para impedir que el primer caso testigo gobierne el diseño.

## 5. Límites

Este cierre no autoriza asistencia, profilaxis, vacunación, prescripción, umbral, equivalencia, parámetro, matriz, ruta, frame ni modificación del Lenguaje SV. Es impersonal y no contiene episodios, personas o centros identificables.
