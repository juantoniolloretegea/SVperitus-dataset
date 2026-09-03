# Lote observacional G3-OBS — SEM-HUE-002 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Puerta:** `G3-OBS/SEM-HUE-002`
- **Operación:** `OP-IMM-001`
- **Raíz:** `SEM-HUE-002`
- **Base exacta:** `0b9cca677b71737a79a4a74dc0157930e0741395`
- **Estatuto:** `OBSERVABLES_Y_NORMALIZADORES_CANDIDATOS_CERRADOS`
- **Perímetro:** concentración cuantitativa de inmunoglobulina G total; no competencia humoral funcional
- **Efecto clínico:** ninguno
- **Autorización asistencial:** ninguna

## 0. Pregunta gobernante

> `SEM-HUE-002`: ¿Existe una alteración cuantitativa de inmunoglobulina G pertinente para el episodio?

Esta puerta constituye la medición cuantitativa de inmunoglobulina G total necesaria para una futura regla de alteración. No decide si el resultado es bajo, alto, clínicamente relevante, causal, protector o indicativo de tratamiento.

Permanecen separados:

1. inmunoglobulina G total;
2. subclases de IgG;
3. anticuerpos específicos frente a antígenos;
4. respuesta funcional a vacunación o infección;
5. fracción gamma o componente monoclonal;
6. inmunoglobulina exógena administrada;
7. y diagnóstico de inmunodeficiencia o gammapatía.

La adversarial está integrada. No se crea documentación auxiliar.

## 1. Fuentes externas aplicadas

| Fuente_ID | Fuente | Corte y función exacta |
|---|---|---|
| `OBS-IGG-SRC-001` | HL7 FHIR R5, `Observation` | versión 5.0.0; aporta estructura para código, sujeto, tiempo clínicamente relevante, estado, valor, ausencia de dato, interpretación, método, espécimen, intervalo de referencia y procedencia; no constituye diagnóstico ni regla clínica |
| `OBS-IGG-SRC-002` | LOINC `2465-3` | página oficial consultada 03-09-2026; identifica la propiedad «IgG [masa/volumen] en suero o plasma»; no fija intervalo, umbral ni pertinencia para `OP-IMM-001` |
| `OBS-IGG-SRC-003` | CLSI EP28, *Defining, Establishing, and Verifying Reference Intervals in the Clinical Laboratory* | referencia metodológica de intervalos; se usa para exigir población, método y versión del intervalo, no para adoptar un rango universal |
| `OBS-IGG-SRC-004` | `BRG-IMMEXP-HISTORY-001` | dependencia interna constituida; aporta exposición documentada a productos de inmunoglobulina cuando exista, sin atribuir cuánto del resultado es endógeno o exógeno |

Enlaces:

- `OBS-IGG-SRC-001`: https://hl7.org/fhir/R5/observation.html
- `OBS-IGG-SRC-002`: https://loinc.org/2465-3
- `OBS-IGG-SRC-003`: https://clsi.org/standards/products/method-evaluation/documents/ep28/

FHIR y LOINC transportan y distinguen el resultado. CLSI gobierna la disciplina de referencia. Ninguna fuente convierte el intervalo del laboratorio en una regla universal de alteración clínicamente pertinente.

## 2. Entidad observacional

```text
E_IGG_Q = <
  Medicion_IgG_ID,
  Analito,
  Propiedad_medida,
  Especimen,
  Instante_de_muestra,
  Valor_original,
  Unidad_original,
  Metodo_y_plataforma,
  Estado_del_resultado,
  Estado_de_calidad,
  Intervalo_de_referencia,
  Poblacion_y_condiciones_del_intervalo,
  Interpretacion_emitida,
  Contexto_de_inmunoglobulina_exogena,
  Vinculo_de_serie,
  Procedencia_por_campo,
  Version
>
```

Una fila representa una medición de IgG total. Un resultado de subclase, anticuerpo específico, inmunofijación, electroforesis o fracción gamma recibe otra identidad y no se introduce en `E_IGG_Q` como sustituto.

## 3. Observables candidatos

| Observable_ID | Contenido | Regla de identidad | `U` propia |
|---|---|---|---|
| `OBS-IGG-001` | identificador de medición | cambia con el resultado fuente o su versión material | `U(MEDICION_ID, causa)` |
| `OBS-IGG-002` | analito | exige IgG total explícita; no «inmunoglobulinas» genéricas | `U(ANALITO, causa)` |
| `OBS-IGG-003` | propiedad medida | masa/volumen permanece separada de otras propiedades | `U(PROPIEDAD, causa)` |
| `OBS-IGG-004` | espécimen | suero, plasma u otro espécimen declarado no se fusionan sin equivalencia | `U(ESPECIMEN, causa)` |
| `OBS-IGG-005` | instante de muestra | conserva fecha, hora y precisión disponibles | `U(INSTANTE, causa)` |
| `OBS-IGG-006` | valor original | conserva cifra, comparador y precisión del informe | `U(VALOR, causa)` |
| `OBS-IGG-007` | unidad original | no se supone ni se completa por rango aparente | `U(UNIDAD, causa)` |
| `OBS-IGG-008` | método y plataforma | conserva principio analítico, instrumento o laboratorio cuando consten | `U(METODO, causa)` |
| `OBS-IGG-009` | estado del resultado | preliminar, final, corregido, cancelado o introducido por error | `U(ESTADO_RESULTADO, causa)` |
| `OBS-IGG-010` | estado de calidad | identifica rechazo, interferencia o limitación comunicada | `U(CALIDAD, causa)` |
| `OBS-IGG-011` | intervalo de referencia informado | conserva límites, unidades, tipo y texto originales | `U(INTERVALO, causa)` |
| `OBS-IGG-012` | población y condiciones del intervalo | edad, población, método y demás aplicabilidades declaradas | `U(APLICABILIDAD_INTERVALO, causa)` |
| `OBS-IGG-013` | interpretación emitida | alta, baja, normal u otra marca se conserva como afirmación de la fuente | `U(INTERPRETACION, causa)` |
| `OBS-IGG-014` | contexto de inmunoglobulina exógena | producto, hechos de administración y relación temporal cuando estén documentados | `U(APORTE_EXOGENO, causa)` |
| `OBS-IGG-015` | vínculo de serie | enlaza mediciones comparables sin inferir tendencia | `U(SERIE, causa)` |

`Procedencia_por_campo` y `Version` son obligatorios y no constituyen observables clínicos adicionales. Incluyen fuente, localizador, sistema, responsable, instante de captura y versión.

## 4. Separaciones obligatorias

1. IgG total no equivale a inmunoglobulinas totales.
2. IgG total no equivale a una subclase de IgG.
3. Concentración total no equivale a anticuerpo específico.
4. Anticuerpo específico no equivale a respuesta funcional completa.
5. Fracción gamma no equivale automáticamente a concentración de IgG.
6. Componente monoclonal no sustituye la cuantificación total.
7. Resultado dentro del intervalo no demuestra competencia humoral.
8. Resultado fuera del intervalo no demuestra por sí solo enfermedad, etiología o riesgo.
9. Marca «bajo» del laboratorio no constituye el transductor de `OP-IMM-001`.
10. Una medición aislada no constituye persistencia, trayectoria ni tendencia.
11. Dos mediciones con método o unidad distintos no se comparan por apariencia numérica.
12. Resultado final y resultado corregido no se mezclan.
13. Ausencia de valor no equivale a concentración adecuada ni alterada.
14. La administración de inmunoglobulina no permite atribuir automáticamente el valor medido a fracción endógena o exógena.
15. Cantidad de IgG no equivale a respuesta humoral específica de `SEM-HUE-003`.

## 5. Normalizadores candidatos

No producen todavía estados clínicos `0/1/U`.

### 5.1. Identidad de medición

```text
N_IGG_ID(E_IGG_Q) ->
  <IgG_total, propiedad, especimen, metodo, version> | U
```

Rechaza como sustitutos las subclases, la fracción gamma y los anticuerpos específicos.

### 5.2. Magnitud y unidad

```text
N_IGG_MAG(valor, unidad, regla_de_conversion_v) ->
  <valor_original, unidad_original, valor_canonico, unidad_canonica> | U
```

La conversión sólo cambia representación. No cambia intervalo, interpretación ni pertinencia.

### 5.3. Intervalo de referencia

```text
N_IGG_REF(intervalo, poblacion, metodo, laboratorio, version) ->
  intervalo_aplicable_documentado | U
```

No selecciona el intervalo más frecuente ni fabrica uno si el informe carece de él.

### 5.4. Serie comparable

```text
N_IGG_SERIES({E_IGG_Q}, criterios_v) ->
  mediciones_ordenadas_comparables + residuo | U
```

Ordena por instante y conserva cambios de método, espécimen, unidad, intervalo, estado y aporte exógeno. No infiere tendencia clínica.

### 5.5. Contexto de aporte exógeno

```text
N_IGG_EXOGENO(
  BRG-IMMEXP-HISTORY-001,
  instante_muestra,
  regla_contextual_v
) ->
  hechos_relevantes_documentados | SIN_HECHOS_EN_COBERTURA_COMPLETA | U
```

Este normalizador no resta una cantidad, no corrige el resultado y no decide si la medición refleja producción endógena.

## 6. Regla de alteración no constituida

La futura clasificación requerirá:

```text
I_IGG_Q_v(E_IGG_Q, contexto, h, finalidad) -> {0,1,U}
```

No puede ejecutarse todavía porque no se han constituido conjuntamente:

- finalidad clínica exacta dentro de `OP-IMM-001`;
- intervalo o criterio aplicable con población, método y versión;
- tratamiento de resultados corregidos, discordantes o seriados;
- vigencia temporal de la medición;
- interpretación del aporte exógeno;
- regla para valores con comparadores o límites de cuantificación;
- y autoridad de adopción.

La etiqueta emitida por el laboratorio se conserva como observable, pero no sustituye esta regla.

## 7. Causas tipadas de U

| Código | Activación | Efecto localizado |
|---|---|---|
| `C_IGG_ID` | medición o versión no identificadas | no se elige un resultado |
| `C_IGG_ANALITO` | analito genérico o ambiguo | no se presume IgG total |
| `C_IGG_PROPIEDAD` | propiedad no demostrada | no se mezclan magnitudes |
| `C_IGG_ESPECIMEN` | espécimen ausente o incompatible | no se transporta intervalo |
| `C_IGG_TIEMPO` | instante o precisión insuficientes | vigencia no evaluable |
| `C_IGG_VALOR` | valor ausente, censurado o ilegible | no se asigna estado |
| `C_IGG_UNIDAD` | unidad ausente o incompatible | no se convierte por plausibilidad |
| `C_IGG_METODO` | método necesario desconocido | comparabilidad o intervalo bloqueados |
| `C_IGG_ESTADO` | resultado preliminar, corregido o conflictivo | no se selecciona silenciosamente |
| `C_IGG_CALIDAD` | interferencia o rechazo comunicado | dato no alimenta salida limpia |
| `C_IGG_INTERVALO` | intervalo ausente o no versionado | no se fabrica umbral |
| `C_IGG_APLICABILIDAD` | población o método no concordantes | no se traslada referencia |
| `C_IGG_EXOGENO` | aporte exógeno desconocido cuando sea material | interpretación dependiente queda bloqueada |
| `C_IGG_SERIE` | resultados no comparables o discordantes | no se infiere trayectoria |
| `C_IGG_PROCEDENCIA` | fuente, localizador o versión insuficientes | el campo no se usa como evidencia limpia |

## 8. Proyección sobre SEM-HUE-002

```text
IgG_total inequívoca
  + valor y unidad
  + especimen, tiempo, metodo y calidad
  + referencia aplicable
  + contexto exogeno
  + procedencia
  -> entrada candidata para I_IGG_Q_v | U tipada
```

Todavía no se decide:

- si existe hipogammaglobulinemia o hipergammaglobulinemia clínicamente pertinente;
- si una alteración es primaria, secundaria, transitoria o persistente;
- si existe competencia humoral;
- si hay respuesta vacunal suficiente;
- si procede inmunoglobulina sustitutiva;
- ni si una actuación terapéutica debe modificarse.

## 9. Interoperabilidad subordinada

FHIR `Observation` puede transportar la medición y sus metadatos. LOINC `2465-3` puede identificar IgG expresada como masa/volumen en suero o plasma. Ninguno determina:

- el intervalo aplicable;
- la comparabilidad entre métodos;
- la vigencia clínica;
- la etiología;
- la función humoral;
- ni la acción posterior.

Una etiqueta de interpretación transportada se conserva con su fuente y versión; no se eleva automáticamente a estado SV.

## 10. Canonicalización y reproducción

Para la misma entrada, reglas y versiones:

1. se conserva valor, comparador, precisión y unidad originales;
2. toda conversión declara regla y resultado canónico;
3. los resultados se ordenan por instante, identificador y versión;
4. corregido sustituye sólo mediante vínculo explícito y el antecedente permanece;
5. intervalos distintos no se fusionan;
6. el contexto exógeno conserva hechos y residuo;
7. conflictos y `U` permanecen visibles;
8. la serialización coincide byte a byte.

Un fallo técnico produce `EJECUCION_TECNICA_NO_VALIDA`, no `U`, `0` o `1`.

## 11. Adversarial integrada

### A. IgG total igual a función humoral

**Ataque:** una concentración normal demuestra competencia.

**Resultado:** rechazado. `SEM-HUE-003` conserva identidad y evidencia propias.

### B. Subclase como sustituto

**Ataque:** una subclase permite reconstruir IgG total.

**Resultado:** rechazado. Analitos y propiedades permanecen separados.

### C. Fracción gamma como IgG

**Ataque:** electroforesis y cuantificación específica son intercambiables.

**Resultado:** rechazado. La identidad analítica no coincide.

### D. Código LOINC como regla clínica

**Ataque:** `2465-3` fija normalidad o pertinencia.

**Resultado:** rechazado. Sólo identifica analito, propiedad y espécimen.

### E. Bandera del laboratorio como estado SV

**Ataque:** `L` produce `1` y ausencia de bandera produce `0`.

**Resultado:** rechazado. Falta regla aplicable, finalidad y autoridad.

### F. Intervalo universal

**Ataque:** adoptar el primer rango encontrado.

**Resultado:** rechazado. Deben conservarse población, método, laboratorio y versión.

### G. Unidad completada por magnitud aparente

**Ataque:** inferir mg/dL o g/L por el número.

**Resultado:** rechazado. La ausencia produce `U_UNIDAD`.

### H. Conversión que transporta interpretación

**Ataque:** convertir unidades permite conservar cualquier intervalo.

**Resultado:** rechazado. Conversión e intervalo son objetos distintos.

### I. Resultado más reciente por reloj

**Ataque:** seleccionar el de fecha mayor aunque sea preliminar o corregido.

**Resultado:** rechazado. Estado y vínculos de sustitución gobiernan.

### J. Una medición como tendencia

**Ataque:** un valor aislado demuestra descenso persistente.

**Resultado:** rechazado. La serie no infiere trayectoria.

### K. Inmunoglobulina administrada ignorada

**Ataque:** interpretar sin conservar aporte exógeno documentado.

**Resultado:** rechazado. El contexto se transporta cuando sea material.

### L. Inmunoglobulina administrada restada

**Ataque:** calcular producción endógena restando una cantidad supuesta.

**Resultado:** rechazado. No existe regla de atribución constituida.

### M. Valor bajo igual a diagnóstico

**Ataque:** una cifra fuera de rango constituye inmunodeficiencia.

**Resultado:** rechazado. Medición, alteración pertinente y diagnóstico son niveles diferentes.

### N. U igual a riesgo alto

**Ataque:** medición ausente produce automáticamente `1` o abstención global.

**Resultado:** rechazado. La criticidad pertenece a G7.

### O. Determinismo igual a validez

**Ataque:** la misma conversión reproducida demuestra la interpretación clínica.

**Resultado:** rechazado. Sólo demuestra fidelidad de representación.

### P. Abrir sublotes por método o intervalo

**Ataque:** cada laboratorio crea otra raíz.

**Resultado:** rechazado. Método e intervalo son instancias finitas de la entidad.

### Q. Salto de secuencia

**Ataque:** recomendar reposición, profilaxis o cambio terapéutico desde G3.

**Resultado:** rechazado. Faltan consecuencias, atomicidad, propiedad, uso y ruta.

**Dictamen adversarial integrado:** `PASA`.

## 12. Recuentos

| Magnitud | Valor |
|---|---:|
| raíces cubiertas | 1 |
| entidades observacionales | 1 |
| observables candidatos | 15 |
| metadatos obligatorios adicionales | 2 |
| normalizadores candidatos | 5 |
| causas tipadas de `U` | 15 |
| reglas de alteración constituidas | 0 |
| parámetros, matrices, rutas o frames | 0 |
| documentos auxiliares | 0 |

## 13. Regla de cierre

`G3-OBS/SEM-HUE-002` cierra si:

1. existe exactamente una entidad, quince observables y cinco normalizadores;
2. IgG total permanece separada de subclases, anticuerpos específicos, electroforesis y componentes monoclonales;
3. valor, unidad, espécimen, método, tiempo, estado y calidad se conservan;
4. el intervalo mantiene población, método, laboratorio y versión;
5. la etiqueta del laboratorio no se convierte en estado SV;
6. el aporte exógeno se contextualiza sin atribución cuantitativa inventada;
7. una serie no constituye tendencia;
8. las quince causas de `U` están localizadas;
9. reproducción, privacidad y finitud pasan;
10. no se constituye diagnóstico, umbral, riesgo, intervención, parámetro, matriz o ruta.

## 14. Efecto

```text
G3-OBS/SEM-HUE-002 = CERRADA
SEM-HUE-002 = OBSERVABLES_CANDIDATOS_CERRADOS
I_IGG_Q_v = NO_CONSTITUIDA
G4-CON/SEM-HUE-002 = NO_ABIERTA
G5-ATM/SEM-HUE-002 = NO_ABIERTA
A0 = {PAR-GC-PLAN-SYS-001}
```

La siguiente puerta es `G4-CON/SEM-HUE-002`: consecuencias de confundir cantidad total, función humoral, referencia, temporalidad o aporte exógeno. No se abrirá atomicidad antes de cerrarla.
