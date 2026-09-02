# Adversarial interna de reparación y cierre — NA0 INMUNO v0.2

- **Fecha:** 02-09-2026
- **Antecedente externo:** `PASA_CON_REPAROS`, Claude, sobre commit `46152c6d16090cba2210baf6ac33c29ec7841b08`
- **Objeto:** comprobar las reparaciones literales `R-01` a `R-03` y la rectificación del falso positivo P11
- **Dictamen:** `CIERRE_CONDICIONAL_SATISFECHO`

## 1. Identidad reparada

| Objeto v0.2 | SHA-256 |
|---|---|
| Contrato semántico | `3950fbbe49f69b97a4e3ae6a6702ecf6416135dd2710baec9925a93c0d2b750a` |
| Protocolo adversarial transversal | `db03dce43881133ab33f2b8e234af78fcc428dffa210347fa9b35660d709945c` |
| Cribado estructural de pilotos | `45758243ba12c22bb9d9d04d6b1f819d0cddc0931fdf85215a3ecd6e6ee08af3` |
| Recepción de la auditoría externa | `fb020aa76a86e9f54b8141ecbac5880e389c789426c808e7b8f6966d4524ebc0` |
| Copia de control `FTD-AE-IMM-SV/0.3` | `8d682a24b6ee24151d7f4382037ca34962b60cc0da2a97b67850c112291e8f4a` |

## 2. Regresión dirigida v0.1 → v0.2

### `R-01`

El contrato sustituye únicamente, en la prueba de atomicidad, consecuencia y ruta plenas por:

- `consecuencia ex ante provisional`;
- `función de ruta provisional`.

La secuencia mantiene la constitución plena después de adjudicar la identidad. Se elimina la lectura circular señalada por Claude.

### `R-02`

El protocolo añade en `G5-ATM` la parada literal:

> si G4 conserva la consecuencia en `U`, A4 se aplaza y la salida obligatoria es `U_REQUIERE_ADJUDICACION`, nunca `ATÓMICO`

No existe ruta alternativa de cierre favorable.

### `R-03`

El contrato fija las rutas públicas exactas de:

- Gramática superficial 0.2;
- Representación Intermedia 0.3;
- puerta pública del Lenguaje SV.

La corrección sólo mejora la localización. No cambia ni propone cambiar el lenguaje.

## 3. Rectificación P11

La copia de control recibida y la depositada son idénticas byte a byte:

- 37925 bytes;
- 812 líneas;
- SHA-256 `8d682a24…e8f4a`;
- una sola coincidencia material de la fila `IMMUNO-1/P11`.

La duplicación descrita en v0.1 no existía. La causa fue el solapamiento de la línea 230 en dos intervalos de salida. El cribado v0.2 retracta la afirmación y conserva la causa; no reescribe ni elimina v0.1.

## 4. Invariantes preservados

- 50 posiciones históricas: 25+25.
- 19 funciones de una clave y 31 multiclave.
- Ocho familias de colisión.
- `IMMUNO-2/P02` compuesto declarado.
- `IMMUNO-2/P24` agregado oculto tras una entrada.
- `IMMUNO-2/P25` puente derivado.
- `T(25)=19` no ratificado.
- Cero parámetros clínicos adjudicados.
- Cero consecuencias clínicas plenas constituidas.
- Cero matrices o rutas constituidas.
- Cero cambios en motores, YAML, compositor y Lenguaje SV.

## 5. Adversarial de las reparaciones

| Ataque | Resultado |
|---|---|
| Declarar `ATÓMICO` con consecuencia en `U` | bloqueado por `R-02` |
| Usar una consecuencia plena inexistente para definir identidad | bloqueado por `R-01` |
| Presentar ruta futura como ya constituida | bloqueado por `R-01` |
| Citar Gramática o IR sin ruta | reparado por `R-03` |
| Mantener el falso positivo P11 | retractado y fuente depositada |
| Alterar silenciosamente v0.1 | no: v0.1 permanece intacta |
| Introducir cambios clínicos mediante la reparación | no hallado |
| Invadir el Lenguaje SV | no hallado |

## 6. Dictamen y efecto

Las condiciones literales impuestas por la auditoría externa quedan satisfechas y la regresión no revela cambios ajenos a ellas. `NA0` queda cerrada en v0.2 y habilita exclusivamente la apertura de una operación clínica testigo en `G1-OP`.

No habilita `G2-SEM` hasta que la operación supere su adversarial propia. No constituye parámetros, consecuencias plenas, matrices, rutas ni autorización asistencial.
