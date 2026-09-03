# G9-EMP — contraste empírico sistemático de adecuación / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Base exacta:** `5d8982c0a9dc7414a4eb0e77f7507292c972304e`
- **Puerta:** `G9-EMP`
- **Pregunta empírica:** ¿existe entre los doce conjuntos candidatos un conjunto admisible que permita contrastar sistemáticamente los 27 parámetros, las seis matrices o las cuatro salidas de OP-IMM-001?
- **Unidad:** conjunto × versión × finalidad
- **Microdatos tratados:** cero
- **Estatuto:** `NO_OBSERVABLE_EN_CONJUNTOS_ADMISIBLES_DEL_CORTE`

## 1. Material contrastado

Se contrastan de forma exhaustiva las doce filas de `inventario_candidatos_v0.1.csv`, sus manifiestos y `matriz_cobertura_conjunto_familia_v0.1.csv`. No se reabre una búsqueda mundial ni se elige un conjunto por interés.

Criterios mínimos:

1. población dentro del alcance de OP-IMM-001;
2. exposición inmunosupresora sistémica identificable;
3. tiempo predecisional reconstruible;
4. variables suficientes para una parte declarada de A0;
5. desenlace o referencia capaz de falsar el objeto;
6. diccionario y unidades;
7. procedencia y versión;
8. acceso y licencia compatibles;
9. uso analítico autorizado;
10. privacidad y riesgo de reidentificación evaluables.

La falta de cualquiera no se imputa.

## 2. Resultado por conjunto

| Registro | Resultado G9 | Causa decisiva |
|---|---|---|
| REG-001 NCT05000216 | `NO_DECIDE` | metadatos de diseño; sin episodio ni variables depositadas |
| REG-002 SDY3324 | `NO_OBSERVABLE` | acceso pendiente; diccionario/variables no leídos |
| REG-003 NCT01516177 | `FUERA_DE_ALCANCE` | trasplante renal y metadatos de diseño |
| REG-004 SDY3274 | `FUERA_DE_ALCANCE` | trasplante; paquete no inspeccionado |
| REG-005 SDY1414 | `FUERA_DE_ALCANCE` | trasplante cardiaco citado; ficha no leída |
| REG-006 SDY621 | `NO_OBSERVABLE` | accesión sin ficha primaria |
| REG-007 SDY218 | `FUERA_DE_ALCANCE` | inmunoterapia oral/alergología, no operación testigo |
| REG-008 SDY1845 | `NO_OBSERVABLE` | accesión sin ficha primaria |
| REG-009 SDY1039 | `NO_OBSERVABLE` | accesión sin ficha primaria |
| REG-010 PIDTC | `NO_OBSERVABLE` | sin extracción abierta; trasplante/IEI |
| REG-011 FAERS | `NO_DECIDE` | notificación espontánea sin denominador ni causalidad |
| REG-012 TrialShare | `NO_OBSERVABLE` | acuerdo y diccionario no inspeccionados |

## 3. Cobertura frente al objeto constituido

Ningún conjunto posee cobertura comprobada simultánea de:

- propuesta terapéutica y fecha índice;
- autoridad/contexto institucional;
- los tres parámetros de huésped;
- barreras y biomateriales;
- historia infecciosa con atribución;
- comorbilidad y reserva;
- U y causas;
- adjudicación humana de criticidad;
- y una de las cuatro salidas estructurales.

La cobertura parcial declarada en registros públicos corresponde a diseño, no a observación material. Publicación, registro, página web y depósito no son intercambiables.

## 4. Resultados admisibles

```text
APOYA = 0
MODULA = 0
CONTRADICE = 0
EVIDENCIA_CONFLICTIVA = 0
NO_OBSERVABLE = 6
FUERA_DE_ALCANCE = 4
NO_DECIDE = 2
```

Estos recuentos clasifican conjuntos, no personas ni parámetros.

## 5. Consecuencia epistemológica

No existe evidencia empírica autorizada en este corte para afirmar:

- sensibilidad, especificidad o calibración;
- utilidad clínica;
- reducción de daño;
- superioridad frente a guía + juicio;
- incidencia o causalidad;
- suficiencia de A0;
- validez de las rutas;
- ni aptitud asistencial.

Tampoco existe evidencia que contradiga los 27 tipos atómicos: falta observabilidad adecuada. Ausencia de cohorte no es confirmación ni refutación.

## 6. Falsadores constituidos para una ronda futura

Un conjunto futuro podrá atacar, al menos:

- porcentaje de parámetros evaluables sin imputación;
- frecuencia y causas de U;
- concordancia de transductores documentales con revisión profesional;
- divergencia entre ejecución repetida;
- errores de atribución infección→ingreso/soporte;
- clasificación de U crítica frente a médico independiente;
- pérdida de información por frames;
- proporción de episodios que terminan en cada salida;
- cambios de decisión atribuibles al expediente, sin convertirlos en causalidad no diseñada.

Requerirá protocolo, referencia profesional ciega cuando proceda, análisis de discrepancias, privacidad y autorización.

## 7. Ataques

- Usar N de un artículo como N del depósito: rechazado.
- Tratar registro de ensayo como microdato: rechazado.
- Descargar ImmPort sin acuerdo: rechazado.
- Usar trasplante para OP fuera de trasplante: rechazado.
- Inferir incidencia desde FAERS: rechazado.
- Simular pacientes para sustituir cohorte: rechazado.
- Presentar laboratorio declarativo como contraste clínico: rechazado.
- Convertir `NO_OBSERVABLE` en `CONTRADICE`: rechazado.
- Abrir otra búsqueda indefinida: rechazado por corte finito.

## 8. Cierre

```text
CONJUNTOS_CONTRASTADOS = 12/12
CONJUNTOS_ADMISIBLES_PARA_OP-IMM-001 = 0
MICRODATOS = 0
RESULTADO_G9 = NO_OBSERVABLE_EN_CONJUNTOS_ADMISIBLES_DEL_CORTE
VALIDACION_CLINICA = NO_REALIZADA
G9-EMP = TERMINAL_CON_NO_OBSERVABLE
G10-SV = HABILITADA_PARA_ENTREGA_DE_REQUISITOS
```

La puerta termina honestamente porque el universo candidato finito ha sido contrastado y ninguno permite ejecutar la pregunta. No se prolonga hasta encontrar un resultado favorable.
