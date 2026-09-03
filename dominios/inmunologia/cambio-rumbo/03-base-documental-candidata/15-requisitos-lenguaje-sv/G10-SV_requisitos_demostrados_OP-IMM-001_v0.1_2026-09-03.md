# G10-SV — expediente de requisitos demostrados para el Lenguaje SV / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Base exacta de inmunología:** `809692af9571ee11972ccc2730620b5564d032b0`
- **Referencia observada del Lenguaje SV:** repositorio `SV-lenguaje-de-computacion`, rama `main`, commit `3c122d1f79a1fcf7f9c3f02db5e7534b4efb7c2d`
- **Puerta:** `G10-SV`
- **Operación:** `OP-IMM-001`
- **Estatuto:** `REQUISITOS_ENTREGADOS_SIN_MODIFICAR_EL_LENGUAJE`
- **Escritura en Lenguaje SV:** ninguna
- **Apertura de ronda técnica:** ninguna

## 1. Material observado

Se toma como cimiento la Gramática superficial mínima 0.2, la Representación intermedia canónica 0.3, los contratos de Frame y supervisión, y los casos de conformidad presentes en el commit citado. Esta puerta clasifica necesidades; no decide su implementación.

## 2. Resultado de correspondencia

| Requisito_ID | Necesidad demostrada por OP-IMM-001 | Clasificación |
|---|---|---|
| `REQ-IMM-SV-001` | estado ternario 0/1/U por parámetro | `YA_REPRESENTABLE` |
| `REQ-IMM-SV-002` | composición de varias unidades con orden y referencias | `REPRESENTABLE_POR_COMPOSICION` |
| `REQ-IMM-SV-003` | supervisión humana de una salida estructural | `YA_REPRESENTABLE` |
| `REQ-IMM-SV-004` | Frame derivado de arquitectura existente | `YA_REPRESENTABLE` |
| `REQ-IMM-SV-005` | procedencia clínica, fuente, versión, localizador y hash | `REQUIERE_ESQUEMA_DE_DOMINIO` |
| `REQ-IMM-SV-006` | causas tipadas de U sin convertirlas en valores nuevos | `REQUIERE_ESQUEMA_DE_DOMINIO` |
| `REQ-IMM-SV-007` | fallo técnico separado de U clínica | `YA_REPRESENTABLE` como separación normativa; serialización de dominio pendiente |
| `REQ-IMM-SV-008` | adjudicación humana U crítica/no crítica con motivo | `REQUIERE_ESQUEMA_DE_DOMINIO` |
| `REQ-IMM-SV-009` | veto no compensable anterior al resumen | `REQUIERE_ESQUEMA_DE_DOMINIO` |
| `REQ-IMM-SV-010` | productor superficial de criticidades | `CANDIDATA_A_EXTENSION_DEL_LENGUAJE` |
| `REQ-IMM-SV-011` | seis matrices propietarias de cardinalidad 6,1,3,2,6,9 sin relleno | `U_NO_DECIDIDO` |
| `REQ-IMM-SV-012` | resumen reversible hacia seis frames y 27 parámetros | `REPRESENTABLE_POR_COMPOSICION`, pendiente de prueba ejecutable |
| `REQ-IMM-SV-013` | manifiestos cerrados de configuración clínica | `REQUIERE_ESQUEMA_DE_DOMINIO` |
| `REQ-IMM-SV-014` | una de cuatro salidas exclusivas sin consejo terapéutico | `REQUIERE_ESQUEMA_DE_DOMINIO` |
| `REQ-IMM-SV-015` | reproducción byte a byte con orden canónico | `YA_REPRESENTABLE` como exigencia; perfil concreto pendiente |

## 3. Tensión principal: cardinalidad matricial

G6 produjo matrices semánticas de tamaños:

```text
(6, 1, 3, 2, 6, 9)
```

El cimiento observado exige celdas `SV(n,b)` con `n=b²` y `b≥3`. Sólo la matriz de nueve parámetros encaja directamente en `SV(9,3)`. Queda prohibido:

- rellenar las otras matrices;
- duplicar parámetros;
- dividir identidades para completar cuadrados;
- mezclar matrices semánticas sólo por geometría;
- o declarar que una lista irregular ya es una célula SV.

La necesidad exacta no es «permitir cualquier dimensión». Es determinar si una matriz clínica propietaria puede representarse como:

1. composición de unidades SV existentes;
2. esquema de dominio externo referenciado por un Frame;
3. proyección parcial con posiciones explícitamente no clínicas;
4. o nueva construcción del lenguaje.

No se elige aquí. Por ello:

```text
REQ-IMM-SV-011 = U_NO_DECIDIDO
CONFLICTO_CON_CIMIENTO = NO_DEMOSTRADO
REPRESENTABILIDAD_TOTAL = NO_DEMOSTRADA
```

## 4. Criticidad

La estructura de Frame reconoce criticidades, pero el corte observado contiene un caso de conformidad inválido `frame_criticality_no_producible.svp`, coherente con la ausencia de productor superficial constituido. OP-IMM-001 necesita producir eventos de criticidad a partir de U y vetos sin que la revisión clausure favorablemente por sí sola.

Esto es una candidata real a extensión, no una petición de implementación inmediata. Las unidades del Lenguaje deberán decidir si se resuelve por biblioteca, IR, construcción superficial o composición.

## 5. Esquema de dominio propuesto, no lenguaje

Los siguientes objetos pueden permanecer fuera del núcleo:

- `ParameterResult`;
- `MatrixProjection`;
- `U_EVENT`;
- `HumanAdjudication`;
- `PaqueteConfiguracion_v`;
- manifiestos de fuentes;
- códigos clínicos;
- consecuencias G4;
- autoridades y perfiles jurisdiccionales.

Su esquema deberá mapear estados y referencias a SV sin convertir terminología médica en palabras reservadas.

## 6. Casos de aceptación para las unidades del Lenguaje

1. representar seis propietarios sin duplicar los 27 parámetros;
2. conservar U con causa;
3. distinguir U clínica de fallo técnico;
4. impedir que supervisión de U genere 1 automáticamente;
5. preservar veto no compensable;
6. formar resumen reversible;
7. reproducir bytes en dos ejecuciones;
8. rechazar criticidad sin productor legítimo;
9. no convertir salida sellada en consejo terapéutico;
10. operar en perfiles léxicos español e inglés sin alterar identidad IR.

## 7. Límites de la entrega

Este expediente no:

- modifica gramática, IR, Rust, WebAssembly ni interfaz;
- abre R2, R3 u otra ronda;
- declara que el Lenguaje SV falla;
- inventa una primitiva;
- demuestra representabilidad completa;
- ni adopta el esquema de dominio.

## 8. Estado global de la secuencia

| Puerta | Estado |
|---|---|
| `G0-PRO` | cerrada en antecedentes |
| `G1-OP` | cerrada, OP-IMM-001 v0.2 |
| `G2-SEM` | 32 raíces cerradas |
| `G3-OBS` | 32/32 terminales |
| `G4-CON` | 32/32 terminales |
| `G5-ATM` | 32/32 terminales; `|A0|=27` |
| `G6-MAT` | 27 propietarios, seis matrices |
| `G7-RUT` | cuatro salidas y tratamiento de U constituidos |
| `G8-ITI` | contrato técnico y laboratorio declarativo cerrados; software no constituido |
| `G9-EMP` | terminal `NO_OBSERVABLE`; 0 conjuntos admisibles |
| `G10-SV` | requisitos clasificados y entregados |

## 9. Dictamen terminal del corte

```text
SECUENCIA_G0_G10 = RECORRIDA
Q0_V0 = AGOTADO
PARAMETROS_ATOMICOS = 27
MATRICES = 6
RUTAS_DE_SALIDA = 4
ITI_CONTRACTUAL = CERRADA
SOFTWARE_CLINICO = NO_CONSTITUIDO
VALIDACION_EMPIRICA = NO_OBSERVABLE
REQUISITOS_LENGUAJE = ENTREGADOS
REPRESENTABILIDAD_TOTAL_EN_SV = U_NO_DECIDIDO
APTITUD_CLINICA = NO_DECLARADA
AUTORIZACION_ASISTENCIAL = NINGUNA
DOMINIO_INTERNACIONAL_DE_INMUNOLOGIA = NO_CERRADO
```

El corte termina sin éxito clínico fingido y sin convertir la falta de cohorte o de representación geométrica en un fracaso global. El producto actual es una arquitectura constitutiva completa y falsable, no una herramienta asistencial validada.
