# G8-ITI — Instrucción Técnica de Implementación y laboratorio / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Base exacta:** `1d6968167126462608708a7dc8c3621fb4b451b6`
- **Puerta:** `G8-ITI`
- **Operación:** `OP-IMM-001`
- **Alcance:** contrato técnico y laboratorio abstracto no atribuible
- **Estatuto:** `ITI_ESPECIFICA_Y_LABORATORIO_CERRADOS_PARA_CONTRASTE`
- **Datos clínicos reales:** ninguno
- **Autorización asistencial:** ninguna

## 1. Entradas canónicas

```text
OperationEnvelope = <
  operation_id = OP-IMM-001,
  operation_version,
  episode_id_pseudonimo_local,
  subject_reference_local,
  index_time,
  scope_evidence[],
  proposal,
  authority,
  source_manifest[],
  rule_manifest[],
  configuration_manifest[],
  payload_hash
>
```

El identificador del sujeto no sale del entorno asistencial autorizado. El laboratorio sólo usa casos sintéticos abstractos sin fechas, centros, edades exactas ni combinaciones reidentificables.

## 2. Objetos técnicos mínimos

```text
ParameterResult = <
  parameter_id,
  parameter_version,
  activation,
  state: 0|1|U,
  u_cause?,
  observable_refs[],
  transducer_id,
  source_refs[],
  configuration_id?,
  trace_hash
>

MatrixProjection = <
  matrix_id,
  ordered_parameter_results[],
  references[],
  u_events[],
  veto_events[],
  version
>

HumanAdjudication = <
  adjudication_id,
  u_event_id,
  decision,
  motive,
  clinician_role,
  timestamp,
  provenance
>

OperationResult = <
  output,
  matrix_projection_refs[],
  summary_frame,
  authority,
  unresolved_u[],
  restrictions[],
  trace_root_hash,
  serialization_version
>
```

## 3. Validación previa

Orden obligatorio:

1. esquema y codificación;
2. versión de operación;
3. integridad de manifiestos;
4. huellas de fuentes y configuraciones;
5. referencias y sujeto;
6. alcance;
7. control de proceso infeccioso activo;
8. transductores;
9. matrices;
10. U, vetos y adjudicación humana;
11. salida y frames;
12. serialización canónica.

Un fallo 1–5 produce `EJECUCION_TECNICA_NO_VALIDA`. No llega a los transductores ni se traduce en U clínica.

## 4. Determinismo y serialización

- UTF-8;
- normalización Unicode NFC;
- claves y colecciones en orden normativo;
- números sin representación alternativa;
- tiempos con zona explícita;
- identificadores estables;
- ausencia diferenciada de `null`, `U` y campo no aplicable;
- SHA-256 sobre bytes canónicos;
- sin reloj, aleatoriedad, red ni orden de llegada dentro del núcleo de evaluación.

Misma entrada, manifiestos y versiones deben producir mismos estados, traza, salida y bytes.

## 5. Regla de configuraciones

Los registros OI, MDRO, nutrición y fragilidad están vacíos en v0.1. Cualquier intento de obtener `0/1` con un paquete no registrado falla clínicamente a `U_CONFIGURACION_NO_ADMITIDA`; si se declara un ID registrado inexistente, el hash no coincide o el cargador falla, el resultado es técnico no válido.

## 6. Autoridad humana

El motor puede:

- evaluar transductores autorizados;
- detectar faltas y conflictos;
- formar U y vetos;
- proyectar matrices;
- comprobar condiciones del sellado;
- reproducir la traza.

No puede:

- diagnosticar infección;
- decidir indicación o inicio;
- declarar no crítica una U;
- sustituir autoridad;
- alterar fuentes, paquetes o reglas;
- completar datos;
- generar una recomendación clínica.

La firma humana se valida como autoridad y decisión registral, no como garantía de verdad biológica.

## 7. Privacidad

- mínimo privilegio y finalidad;
- ejemplos sintéticos;
- no incluir nombre, centro, fecha completa, combinación singular o texto libre real en trazas de prueba;
- referencias locales opacas;
- separación entre identidad asistencial y paquete exportable;
- abstención de exportar cuando la desidentificación no sea suficiente.

## 8. Banco de laboratorio

| Caso | Ataque | Resultado esperado |
|---|---|---|
| `LAB-001` | caso fuera de alcance | `FUERA_DE_ALCANCE` |
| `LAB-002` | sujeto/propuesta incompletos | `ABSTENERSE_O_ESCALAR` |
| `LAB-003` | posible infección activa | `ABSTENERSE_O_ESCALAR` |
| `LAB-004` | los 27 estados trazados, sin U material | candidato a sellado humano |
| `LAB-005` | una U crítica | `U_CRITICA_NO_CERRADA` |
| `LAB-006` | U no crítica sin motivo | adjudicación inválida |
| `LAB-007` | U no crítica firmada y visible | puede continuar a sellado |
| `LAB-008` | OI con clasificación no registrada | U, nunca 0/1 |
| `LAB-009` | tabla MDRO con hash distinto | ejecución técnica no válida |
| `LAB-010` | cribado nutricional positivo | no diagnostica malnutrición |
| `LAB-011` | edad usada como fragilidad | U/rechazo del transductor |
| `LAB-012` | diagnóstico principal como causa de ingreso | U de atribución |
| `LAB-013` | CKD y KRT positivas | dos estados, sin suma |
| `LAB-014` | protocolo local contradice necesidad | restricción visible, sin cambiar estado clínico |
| `LAB-015` | mismo caso con orden de campos diferente | mismos bytes canónicos |
| `LAB-016` | fallo de conector | técnico no válido, no U |
| `LAB-017` | resumen elimina una U | frame no conforme |
| `LAB-018` | IA intenta sellar | autoridad inválida |
| `LAB-019` | médico sella perfil | no implica iniciar tratamiento |
| `LAB-020` | replay exacto | misma raíz de traza |

## 9. Resultado del laboratorio contractual

Los veinte casos se han recorrido contra las reglas declarativas de G6–G8. No se ejecuta software clínico ni se atribuye rendimiento a un motor aún no implementado.

```text
CASOS_CONTRATO = 20
RESULTADOS_ESPERADOS_UNICOS = 20
COLISIONES_LOGICAS_DETECTADAS = 0
SALIDAS_ASISTENCIALES = 0
EJECUCION_SOFTWARE_CLINICO = NO
CONFORMIDAD_DECLARATIVA = PASA
```

## 10. Criterios de implementación futura

Una implementación sólo podrá llamarse conforme cuando:

- valide los 27 transductores y las seis matrices;
- reproduzca los 20 casos y sus variantes negativas;
- demuestre paridad de serialización;
- rechace autoridad inválida;
- preserve U y fallo técnico;
- produzca frames reversibles;
- supere revisión de privacidad y seguridad;
- y no emita consejo terapéutico.

## 11. Cierre

```text
G8-ITI = CERRADA_COMO_CONTRATO_TECNICO
LABORATORIO_DECLARATIVO = PASA
LABORATORIO_EJECUTABLE = NO_CONSTITUIDO
G9-EMP = HABILITADA_PARA_PREGUNTA_Y_CONTRASTE
APTITUD_CLINICA = NO_DECLARADA
```

G8 no afirma que exista una aplicación validada. Constituye lo necesario para que una implementación futura pueda ser falsada.
