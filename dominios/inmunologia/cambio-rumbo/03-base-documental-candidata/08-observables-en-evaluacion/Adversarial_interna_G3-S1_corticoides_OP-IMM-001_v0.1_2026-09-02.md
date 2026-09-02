# Adversarial interna `G3-S1` — exposición a glucocorticoides en `OP-IMM-001` v0.1

- **Fecha:** 02-09-2026
- **Objeto:** `Lote_observacional_G3-S1_corticoides_OP-IMM-001_v0.1_2026-09-02.md`
- **Bytes:** 13 716
- **SHA-256:** `49f15ef048230b3f8eb010bd11713121122102711efb8988b02156cc0221584c`
- **Línea base:** commit `0d885602721d495bdfba87631f44eb2afbe98645`
- **Regla:** todo contraejemplo debe ser absorbido por texto expreso; la intención del autor no cuenta como evidencia

## 1. Tesis atacada

`G3-S1` sostiene que las preguntas `SEM-EXP-002`, `SEM-EXP-003` y `SEM-EXP-005` no autorizan un parámetro escalar de «riesgo por corticoides». Antes deben constituirse observables separados de identidad, vía, ejecución, dosis, pauta y tiempo, con procedencia por campo y `U` no cerrable por inferencia.

## 2. Ataques materiales

| Ataque | Contraejemplo | Fallo que debe impedirse | Absorción exigida |
|---|---|---|---|
| `A-GC-01` | misma dosis prescrita de prednisona, una aún no iniciada y otra ya administrada | presentar planificación como exposición real | `OBS-GC-004`, `009`; `U(EJECUCION, C_EJECUCION)` |
| `A-GC-02` | misma sustancia y dosis, vía oral frente a intraarticular | inferir la misma exposición sistémica | `OBS-GC-002`, `003`; `U(VIA, C_FORMULACION_VIA)` |
| `A-GC-03` | dosis diaria continua frente a dosis alterna | reducir ambas a una media diaria | `OBS-GC-006`; prohibición de promedio implícito |
| `A-GC-04` | pulsos separados y dosis continua con igual suma aritmética | considerar la suma como mismo patrón | eventos `OBS-GC-009` y pauta diferenciada |
| `A-GC-05` | plan sin fecha final porque es abierto frente a fecha final omitida | equiparar plan abierto con dato ausente | `ABIERTO_POR_PLAN` ≠ `U_FIN` |
| `A-GC-06` | orden documentada sin constancia de administración | fabricar eventos desde la orden | identidad independiente de `OBS-GC-009` |
| `A-GC-07` | lista de medicación y registro de administración discrepan | escoger el dato más conveniente | `U(CAMPO, C_CONFLICTO)`; conservación de ambos valores |
| `A-GC-08` | 1 mg/kg sin peso válido en el horizonte | convertir automáticamente a miligramos absolutos | `OBS-GC-005`; `U(DOSIS_UNIDAD_BASE, C_DOSIS_UNIDAD_BASE)` |
| `A-GC-09` | dexametasona expresada en miligramos y solicitud de prednisona-equivalente | usar una tabla implícita o memorizada | `U(EQUIVALENCIA, C_EQUIVALENCIA)` |
| `A-GC-10` | dosis diaria definida ATC usada como equivalencia inmunosupresora | convertir una medida estadística en regla clínica | exclusión expresa de DDD en §§2, 3 y 6 |
| `A-GC-11` | umbral CDC de vacunas vivas aplicado a profilaxis frente a *Pneumocystis* | universalizar una regla dependiente de finalidad | `U(FINALIDAD, C_FINALIDAD)`; divergencia de fuentes en §2 |
| `A-GC-12` | intervalo EULAR de profilaxis aplicado a seguridad vacunal | inversión del error anterior | misma barrera de finalidad |
| `A-GC-13` | última administración conocida usada para afirmar efecto residual activo | convertir recencia en farmacodinamia | `N_GC_REC` prohíbe esa inferencia |
| `A-GC-14` | tratamiento interrumpido y después reiniciado | medir una sola duración continua | eventos y estados separados; no rellenar intervalo |
| `A-GC-15` | combinación con dos glucocorticoides o formulaciones | ocultar componentes bajo un rótulo único | `OBS-GC-001` exige componentes separados |
| `A-GC-16` | cambio de fuente después del corte | mutar el lote sin versión | procedencia y versión obligatorias; reapertura posterior |
| `A-GC-17` | texto libre completa una vía o dosis ausente | cerrar `U` por plausibilidad | §8 prohíbe inferencia y búsqueda libre |
| `A-GC-18` | una petición de ejemplo recupera un episodio real | transportar información atribuible al objeto público | §12 impersonal; la política transversal de privacidad sigue gobernando |
| `A-GC-19` | los diez observables se convierten en diez parámetros | confundir medibilidad con atomicidad | estatuto G3 y contrato `NA0-MATH` |
| `A-GC-20` | se dibuja un frame o se asigna una matriz para ilustrar el lote | anticipar G6–G8 | residuos y límites de §§10–12 |

## 3. Ataques de separabilidad

### 3.1. Magnitud frente a duración

Caso: misma dosis y pauta, pero un plan de tres días y otro deliberadamente abierto.

Resultado exigido: `N_GC_MAG` coincide; `N_GC_DUR` diverge. Si el sistema devuelve un único estado, el lote no pasa.

### 3.2. Duración planificada frente a real

Caso: plan de catorce días, administración confirmada sólo durante dos.

Resultado exigido: la duración planificada conserva catorce días; la real observada se limita a los eventos admisibles. Ninguna sustituye a la otra.

### 3.3. Identidad frente a vía

Caso: misma sustancia en preparación oral y local.

Resultado exigido: agente coincidente, vía divergente; no se concluye exposición sistémica de la preparación local.

### 3.4. Recencia frente a actividad clínica

Caso: última administración conocida, pero ausencia de regla constituida sobre persistencia del efecto.

Resultado exigido: recencia calculable; actividad inmunológica `U`. La primera no cierra la segunda.

### 3.5. Registro específico frente a pregunta genérica

Caso: `SEM-EXP-002` y `003` pueden caracterizarse para un tratamiento primario no glucocorticoide.

Resultado exigido: el lote sólo proyecta esas preguntas cuando la exposición incluye glucocorticoide; no redefine el universo farmacológico de `OP-IMM-001`.

## 4. Ataques a procedencia y determinismo

Se ejecutarán al menos estas pruebas:

1. permutar el orden de eventos sin alterar sus claves canónicas;
2. repetir exactamente la misma entrada, fuentes, horizonte y versiones;
3. introducir dos eventos con el mismo instante y distinta procedencia;
4. cambiar sólo una vía, una unidad o el estado de ejecución;
5. eliminar un localizador de fuente;
6. hacer fallar una herramienta de normalización.

Resultados exigidos:

- las pruebas 1 y 2 producen serialización idéntica byte a byte;
- la prueba 3 conserva ambos eventos y un orden determinista;
- la prueba 4 hace visible la diferencia material en salida y traza;
- la prueba 5 produce `U` de procedencia, no un valor limpio;
- la prueba 6 produce `EJECUCION_TECNICA_NO_VALIDA`.

## 5. Comprobación de no constitución prematura

El objeto debe contener exactamente:

- diez observables candidatos;
- cuatro normalizadores previos;
- once códigos de causa de `U`;
- cero umbrales adoptados;
- cero equivalencias adoptadas;
- cero parámetros atómicos;
- cero consecuencias clínicas plenas;
- cero matrices, rutas, composiciones o frames.

La aparición de un valor clínico en una fuente sólo sirve como contraejemplo de finalidad. No puede entrar como regla del lote.

## 6. Incertidumbres legítimas

| U_ID | Objeto pendiente | Puerta de resolución |
|---|---|---|
| `U-G3S1-01` | fuente y tabla autorizada de equivalencia entre glucocorticoides | lote posterior específico; no G3-S1 |
| `U-G3S1-02` | reglas de riesgo por finalidad | `G4-CON` y regla posterior |
| `U-G3S1-03` | efecto inmunológico residual por agente y pauta | fuente clínica y consecuencia específica |
| `U-G3S1-04` | si algún observable sostiene una proposición gobernable independiente | `G4-CON` y `G5-ATM` |
| `U-G3S1-05` | matriz propietaria y forma del frame | `G6-MAT` y `G8-FRA` |

## 7. Dictamen interno

`PASA_INTERNA`

Los contraejemplos quedan absorbidos por el texto del lote y no se ha introducido una regla asistencial. El cierre externo debe intentar demostrar que la entidad `E_GC` es un compuesto mal gobernado, que algún observable está duplicado, que una `U` puede desaparecer o que una regla de finalidad se ha colado como hecho.

## 8. Declaración

Esta adversarial no cierra `G3-S1`, no autoriza equivalencias, umbrales, consecuencias, parámetros, matrices, rutas o frames y no abre `G4-CON` ni `G5-ATM`.
