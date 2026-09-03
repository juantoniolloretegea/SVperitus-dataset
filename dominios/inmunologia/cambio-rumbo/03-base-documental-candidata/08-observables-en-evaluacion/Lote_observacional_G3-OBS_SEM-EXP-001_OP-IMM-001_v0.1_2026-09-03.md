# Lote observacional G3-OBS — SEM-EXP-001 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Puerta:** `G3-OBS/SEM-EXP-001`
- **Operación:** `OP-IMM-001`
- **Raíz:** `SEM-EXP-001`
- **Base exacta:** `25d4b8ba8c1e980b737bb85167010f48c58633f6`
- **Estatuto:** `OBSERVABLES_Y_NORMALIZADORES_CANDIDATOS_CERRADOS`
- **Perímetro:** identidad del tratamiento inmunosupresor sistémico primario propuesto; no clasificación de riesgo, indicación ni decisión
- **Efecto clínico:** ninguno
- **Autorización asistencial:** ninguna

## 0. Pregunta gobernante

> `SEM-EXP-001`: ¿Está identificado el tratamiento inmunosupresor sistémico primario propuesto?

La pregunta exige distinguir:

1. una propuesta terapéutica de una prescripción, dispensación o administración;
2. un medicamento o componente de un régimen completo;
3. el papel primario declarado de una posición accidental en una lista;
4. la identidad farmacológica de la interpretación clínica de inmunosupresión;
5. y una versión vigente de una propuesta sustituida, cancelada o parcial.

Este lote constituye los observables necesarios. No convierte códigos, nombres, solicitudes o clasificaciones en parámetros clínicos.

La adversarial está integrada en el mismo objeto. No se crea documentación auxiliar.

## 1. Fuentes externas aplicadas

| Fuente_ID | Fuente | Corte | Función exacta |
|---|---|---|---|
| `OBS-TXP-SRC-001` | Organización Mundial de la Salud, sistema de clasificación Anatómica, Terapéutica y Química | página oficial consultada 03-09-2026 | sostiene que las sustancias activas se agrupan por órgano o sistema y propiedades terapéuticas, farmacológicas y químicas, en cinco niveles; no decide papel primario, propuesta individual ni pertinencia para `OP-IMM-001` |
| `OBS-TXP-SRC-002` | HL7 FHIR R5, `MedicationRequest` | versión 5.0.0 consultada 03-09-2026 | distingue la solicitud u orden de medicación del uso comunicado mediante otros recursos; aporta un posible transporte de estado, intención, medicación, pauta y autoría; no constituye semántica clínica |
| `OBS-TXP-SRC-003` | Agencia Europea de Medicamentos, servicios SPOR de sustancias, productos, organizaciones y datos de referencia | portal oficial consultado 03-09-2026 | aporta infraestructura de identidad y datos de referencia; no prueba por sí sola que dos registros sean clínicamente intercambiables ni que un producto sea el tratamiento primario |

Enlaces:

- `OBS-TXP-SRC-001`: https://www.who.int/tools/atc-ddd-toolkit/atc-classification
- `OBS-TXP-SRC-002`: https://hl7.org/fhir/medicationrequest.html
- `OBS-TXP-SRC-003`: https://spor.ema.europa.eu/

Estas fuentes se usan para identidad, separación de estados y transporte. La decisión de qué tratamiento es primario y pertinente pertenece a la propuesta clínica autorizada.

## 2. Entidad observacional

Cada propuesta terapéutica se representa mediante:

```text
E_TX_PRIMARY = <
  Propuesta_ID,
  Version_propuesta,
  Estado_propuesta,
  Intencion_documental,
  Instante_de_corte,
  Regimen_completo_declarado,
  Componente_ID,
  Sustancias_activas_declaradas,
  Producto_o_preparacion,
  Forma_farmaceutica,
  Via_planificada,
  Papel_en_regimen,
  Clasificacion_sistemica_declarada,
  Clasificacion_inmunosupresora_declarada,
  Autoridad_de_propuesta,
  Vigencia,
  Procedencia_por_campo
>
```

Una fila identifica un componente dentro de una propuesta versionada. Un régimen con varios componentes conserva varias filas enlazadas al mismo `Propuesta_ID`; no se fusiona en una etiqueta única.

`Regimen_completo_declarado` es un control de cobertura. No afirma que la propuesta sea correcta, indicada o definitiva.

## 3. Observables candidatos

| Observable_ID | Contenido | Regla de identidad | `U` propia |
|---|---|---|---|
| `OBS-TXP-001` | identificador de la propuesta | cambia si el sistema autorizado declara otro episodio o propuesta | `U(PROPUESTA_ID, causa)` |
| `OBS-TXP-002` | versión de la propuesta | una sustitución o enmienda crea otra versión | `U(VERSION_PROPUESTA, causa)` |
| `OBS-TXP-003` | estado documental | borrador, propuesta, orden, cancelación y sustitución permanecen separados | `U(ESTADO_PROPUESTA, causa)` |
| `OBS-TXP-004` | intención documental | conserva propuesta, plan, orden u otra intención declarada | `U(INTENCION, causa)` |
| `OBS-TXP-005` | instante de corte | fija qué versión y estado pueden considerarse vigentes | `U(CORTE_TEMPORAL, causa)` |
| `OBS-TXP-006` | cobertura del régimen | declara completo, parcial, condicionado o desconocido | `U(COBERTURA_REGIMEN, causa)` |
| `OBS-TXP-007` | identificador de componente | no se deduce de su posición ordinal | `U(COMPONENTE_ID, causa)` |
| `OBS-TXP-008` | sustancia o componentes activos | una combinación conserva cada componente y su relación | `U(SUSTANCIA, causa)` |
| `OBS-TXP-009` | producto o preparación | no sustituye automáticamente a la sustancia activa | `U(PRODUCTO, causa)` |
| `OBS-TXP-010` | forma farmacéutica | se conserva cuando modifica identidad o interpretación | `U(FORMA, causa)` |
| `OBS-TXP-011` | vía planificada | una vía no se infiere desde el producto si admite varias | `U(VIA, causa)` |
| `OBS-TXP-012` | papel en el régimen | primario, concomitante, puente, rescate u otro papel declarado | `U(PAPEL_REGIMEN, causa)` |
| `OBS-TXP-013` | clasificación sistémica declarada | conserva fuente, regla y versión; no se infiere por nombre | `U(SISTEMICA, causa)` |
| `OBS-TXP-014` | clasificación inmunosupresora declarada | conserva quién la declaró, para qué operación y bajo qué regla | `U(INMUNOSUPRESORA, causa)` |
| `OBS-TXP-015` | autoridad de la propuesta | profesional o sistema autorizado y función | `U(AUTORIDAD, causa)` |
| `OBS-TXP-016` | vigencia | vigente, sustituida, cancelada, condicionada o desconocida en el corte | `U(VIGENCIA, causa)` |

`Procedencia_por_campo` es obligatoria y no constituye un decimoséptimo observable clínico. Contiene fuente, localizador, sistema o autoría, instante de captura y versión.

## 4. Separaciones obligatorias

1. Propuesta no equivale a prescripción.
2. Prescripción no equivale a dispensación.
3. Dispensación no equivale a administración.
4. Sustancia activa no equivale a producto comercial.
5. Producto no determina siempre una única vía.
6. Código ATC no prueba que un componente sea primario.
7. Pertenencia a un grupo farmacológico no constituye indicación.
8. La primera fila no es necesariamente el tratamiento primario.
9. Un régimen parcial no permite inferir ausencia de otros componentes.
10. Cancelado, sustituido y no documentado no son equivalentes.
11. «Sistémico» y «local» requieren vía y formulación suficientemente identificadas.
12. «Inmunosupresor» debe conservar la regla, finalidad y autoridad que sostienen esa clasificación.
13. Un nombre comercial no resuelve por sí solo sustancia, combinación, forma o vía.
14. Dos códigos distintos no prueban diferencia clínica; un mismo código no prueba intercambiabilidad.

## 5. Normalizadores candidatos

No producen todavía estados clínicos `0/1/U`.

### 5.1. Identidad de componente

```text
N_TX_COMPONENT(E_TX_PRIMARY) ->
  <Componente_ID, Sustancias, Producto, Forma, Via, Codigos, Versiones> | U
```

Conserva identificadores originales y relaciones de composición. No selecciona un código «preferente» por disponibilidad.

### 5.2. Régimen versionado

```text
N_TX_REGIMEN({E_TX_PRIMARY}, Propuesta_ID, Version, h) ->
  <Componentes_ordenados, Cobertura, Estado, Intencion, Vigencia, Autoridad> | U
```

Ordena por identificador canónico de componente. El orden de captura no crea prioridad clínica.

### 5.3. Papel primario

```text
N_TX_PRIMARY({E_TX_PRIMARY}, regla_de_papel_v) ->
  Componente_primario_declarado
  | MULTIPLES_PRIMARIOS_DECLARADOS
  | SIN_PRIMARIO_DECLARADO
  | U
```

No elige el componente de mayor dosis, el primero, el más costoso ni el más conocido. Si la propuesta admite legítimamente varios componentes primarios, conserva la pluralidad; no fuerza unicidad.

### 5.4. Correspondencia terminológica

```text
N_TX_TERMINOLOGIA(identidades_originales, mapas_versionados) ->
  correspondencias_trazadas | U
```

Una correspondencia transporta identidad. No decide equivalencia clínica, sustitución, vía, papel ni pertinencia.

## 6. Reglas de U

```text
U_TXP = <
  Campo_afectado,
  Codigo_de_causa,
  Fuentes_ausentes_o_en_conflicto,
  Dependencia_afectada,
  Horizonte,
  Version
>
```

| Código | Activación | Efecto |
|---|---|---|
| `C_PROPUESTA_ID` | propuesta no identificada | no se agregan componentes |
| `C_VERSION_PROPUESTA` | versión ausente o contradictoria | no se elige silenciosamente la más reciente |
| `C_ESTADO_INTENCION` | estado o intención ambiguos | no se presenta orden como propuesta vigente ni viceversa |
| `C_CORTE_TEMPORAL` | horizonte insuficiente | no se adjudica vigencia |
| `C_COBERTURA_REGIMEN` | lista parcial o cobertura desconocida | la ausencia de un componente no produce `0` |
| `C_COMPONENTE_ID` | identidad local ambigua | no se fusionan filas |
| `C_SUSTANCIA` | sustancia o composición desconocidas | no se clasifica identidad farmacológica limpia |
| `C_PRODUCTO_FORMA` | producto o forma ambiguos | no se presume formulación |
| `C_VIA` | vía ausente o incompatible | no se clasifica exposición sistémica |
| `C_PAPEL_REGIMEN` | papel no declarado o conflictivo | no se elige tratamiento primario |
| `C_CLASIFICACION` | regla sistémica o inmunosupresora ausente | no se clasifica por plausibilidad |
| `C_AUTORIDAD` | autoría o competencia no demostradas | la propuesta no alimenta una salida autorizada |
| `C_VIGENCIA` | propuesta sustituida, cancelada o incierta | no se presenta como vigente |
| `C_EQUIVALENCIA` | mapas terminológicos discordantes | se conservan todos y se detiene la equivalencia afectada |
| `C_PROCEDENCIA` | falta fuente, localizador, captura o versión | el campo no se usa como evidencia limpia |
| `C_CONFLICTO` | fuentes admisibles discrepan sin precedencia | no se resuelve por preferencia técnica |

Ninguna `U` se cierra mediante memoria del modelo, nombre comercial, posición ordinal, frecuencia estadística o búsqueda libre.

## 7. Proyección sobre SEM-EXP-001

La pregunta sólo puede recibir material observacional limpio mediante:

```text
regimen versionado
  + cobertura declarada
  + identidad de componentes
  + papel primario declarado
  + clasificacion sistemica e inmunosupresora trazadas
  + autoridad y vigencia
  -> entrada candidata para futura proposicion | U tipada
```

Todavía no se decide:

- que exista un único componente primario;
- que el tratamiento sea adecuado;
- que la clasificación farmacológica baste para la operación;
- que la propuesta vaya a ejecutarse;
- ni que su presencia determine riesgo.

## 8. Interoperabilidad subordinada

Un recurso `MedicationRequest` puede transportar estado, intención, medicación, sujeto, autoría y pauta. No constituye por sí solo:

- cobertura completa del régimen;
- papel primario;
- inmunosupresión clínicamente pertinente;
- autorización para la operación;
- ni equivalencia con administración real.

ATC y SPOR pueden apoyar identidad y correspondencia. No sustituyen la fuente clínica autorizada de la propuesta.

La ausencia de un campo en un estándar de transporte no demuestra que el objeto clínico sea innecesario. Se registra como tensión futura para `G10-SV` sólo si la necesidad persiste después de constituirse; no modifica ahora el Lenguaje SV.

## 9. Canonicalización y reproducción

Para una misma propuesta, versión, corte, entradas y mapas:

1. los componentes se ordenan por `Componente_ID`;
2. se conserva cada identificador original y su sistema;
3. las sustancias de una combinación no se colapsan;
4. estado, intención y vigencia permanecen separados;
5. una pluralidad primaria declarada no se reduce;
6. los conflictos conservan todas las fuentes admisibles;
7. salida, `U`, residuos y serialización coinciden byte a byte.

Una variación de propuesta, versión, sustancia, forma, vía, papel, autoridad o vigencia produce otra entrada. Un fallo técnico sólo produce `EJECUCION_TECNICA_NO_VALIDA`.

## 10. Adversarial integrada

### A. Nombre comercial como identidad completa

**Ataque:** el texto del producto basta.

**Resultado:** rechazado. Puede ocultar sustancia, combinación, forma, vía o versión.

### B. Código ATC como autoridad clínica

**Ataque:** el grupo farmacológico demuestra tratamiento inmunosupresor primario.

**Resultado:** rechazado. El código clasifica; no adjudica papel, propuesta ni pertinencia individual.

### C. Primera posición como tratamiento primario

**Ataque:** el primer componente de la lista gobierna.

**Resultado:** rechazado. El papel debe proceder de una declaración autorizada.

### D. Dosis mayor como prioridad

**Ataque:** el componente de mayor cantidad es el primario.

**Resultado:** rechazado. Magnitudes no asignan función clínica.

### E. Propuesta como administración

**Ataque:** `MedicationRequest` prueba exposición real.

**Resultado:** rechazado. Solicitud u orden y uso real son objetos distintos.

### F. Silencio como ausencia

**Ataque:** un régimen parcial sin glucocorticoide produce `0`.

**Resultado:** rechazado. Cobertura desconocida produce `U`.

### G. Código idéntico como intercambiabilidad

**Ataque:** dos registros con el mismo grupo son sustituibles.

**Resultado:** rechazado. Deben conservarse sustancia, producto, forma, vía y versión.

### H. Multiplicidad forzada a unicidad

**Ataque:** elegir un solo primario cuando la propuesta declara combinación primaria.

**Resultado:** rechazado. Se conserva pluralidad o se produce `U`.

### I. Versión más reciente elegida por reloj

**Ataque:** el sistema selecciona el registro de fecha posterior sin regla de sustitución.

**Resultado:** rechazado. La vigencia requiere enlace documental, no mera cronología.

### J. Clasificación inmunosupresora por plausibilidad

**Ataque:** el modelo reconoce el fármaco y completa la categoría.

**Resultado:** rechazado. Falta regla, versión, finalidad y autoridad.

### K. Interoperabilidad como semántica

**Ataque:** un campo FHIR determina el significado clínico completo.

**Resultado:** rechazado. FHIR transporta; no constituye el dominio.

### L. Exhaustividad farmacológica

**Ataque:** abrir inventario de todos los inmunosupresores antes de cerrar la entidad.

**Resultado:** rechazado. Este lote constituye el esquema, no una farmacopea mundial.

### M. Identidad convertida en riesgo

**Ataque:** tratamiento identificado equivale a riesgo infeccioso alto.

**Resultado:** rechazado. Faltan reglas de exposición, huésped, finalidad y consecuencia operacional.

### N. Fallo técnico convertido en U clínica

**Ataque:** error de terminología produce `U(INMUNOSUPRESION)`.

**Resultado:** rechazado. Produce `EJECUCION_TECNICA_NO_VALIDA` salvo que la entrada clínica sea materialmente indeterminada.

**Dictamen adversarial integrado:** `PASA`.

## 11. Recuentos

| Magnitud | Valor |
|---|---:|
| raíces cubiertas | 1 |
| observables candidatos | 16 |
| metadatos obligatorios adicionales | 1 |
| normalizadores candidatos | 4 |
| causas de `U` | 16 |
| parámetros adoptados | 0 |
| umbrales o riesgos adoptados | 0 |
| matrices, rutas o frames | 0 |
| documentos auxiliares | 0 |

## 12. Regla de cierre

`G3-OBS/SEM-EXP-001` sólo cierra si:

1. existen exactamente dieciséis observables y cuatro normalizadores;
2. propuesta, orden y administración están separadas;
3. sustancia, producto, forma y vía permanecen distinguibles;
4. el papel primario no se infiere del orden, dosis o código;
5. la cobertura del régimen se conserva antes de interpretar ausencias;
6. estado, intención, vigencia, autoridad y versión están trazados;
7. ATC, SPOR y FHIR permanecen subordinados como identidad o transporte;
8. las dieciséis causas de `U` no se rellenan por plausibilidad;
9. reproducción y privacidad pasan;
10. no se constituye parámetro, riesgo, intervención o modificación del Lenguaje SV.

## 13. Efecto y límites

```text
G3-OBS/SEM-EXP-001 = CERRADA
SEM-EXP-001 = OBSERVABLES_CANDIDATOS_CERRADOS
G4-CON/SEM-EXP-001 = NO_ABIERTA
G5-ATM/SEM-EXP-001 = NO_ABIERTA
A0 = {PAR-GC-PLAN-SYS-001}
```

La siguiente puerta es `G4-CON/SEM-EXP-001`: consecuencias de identificar erróneamente la propuesta, su versión, sus componentes o su papel primario. No se abrirá atomicidad antes de cerrar esa dependencia.
