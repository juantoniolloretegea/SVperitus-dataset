# Lote observacional `G3-S2` — cuantificación del compartimento linfocitario en `OP-IMM-001` v0.1

- **Fecha:** 02-09-2026
- **Rama:** `dominio-inmunologia`
- **Puerta:** `G3-OBS`
- **Estatuto:** `OBSERVABLES_Y_NORMALIZADORES_CANDIDATOS_NO_ADJUDICADOS`
- **Operación:** `OP-IMM-001`
- **Pregunta de origen:** `SEM-HUE-001`
- **Base matemática:** contrato `NA0-MATH` v0.3
- **Perímetro:** evidencia cuantitativa del compartimento linfocitario; no función inmunitaria, diagnóstico, riesgo ni decisión asistencial

## 1. Decisión del lote

La expresión «estado linfocitario» no se reduce a un único número. Un recuento total, una subpoblación, un recuento absoluto por volumen y una proporción pueden divergir y no son sustitutos de una función celular.

`G3-S2` constituye una medición linfocitaria trazable como objeto compuesto por observables separables. Todavía no decide si existe una alteración, no adopta intervalos de referencia como regla universal y no convierte ningún resultado en `PARAMETRO_ATOMICO`.

Este corte es deliberadamente no vacunal. Una fuente puede proceder de un documento cuyo contexto sea vacunación, pero sólo se utiliza el pasaje general que distingue números, subpoblaciones y función inmunitaria; no se importa ninguna recomendación vacunal.

## 2. Fuentes aplicadas

| Fuente_ID | Fuente y versión | Localizador | Función en este lote |
|---|---|---|---|
| `OBS-LYM-SRC-001` | CDC, *Altered Immunocompetence*, página actualizada 26-06-2024, consultada 02-09-2026 | `General Principles`, párrafos sobre estudios de laboratorio de inmunidad humoral y celular | sostiene la separación entre número de linfocitos, concentraciones y proporciones de subpoblaciones y ensayos de función; no aporta umbral ni decisión |
| `OBS-LYM-SRC-002` | Clinical and Laboratory Standards Institute, `H42-A2`, segunda edición, publicada 22-05-2007 y reafirmada en 2017 | `Abstract` y `Scope` públicos | sostiene que la comparabilidad de la enumeración depende del proceso y control analíticos; justifica conservar muestra, método, calidad y procedencia, sin reproducir en este objeto todo el expediente técnico del laboratorio ni fijar intervalos universales |
| `OBS-LYM-SRC-003` | EuroFlow, *Standardized EuroFlow Protocols*, consultado 02-09-2026 | protocolos de PID e inmunomonitorización; valores de referencia en porcentajes v1.2 (12-2024) y números absolutos v1.3 (07-2026) | confirma que porcentaje y número absoluto son productos diferenciados y versionados; no se incorporan sus valores al lote |

Enlaces fijados:

- `OBS-LYM-SRC-001`: https://www.cdc.gov/vaccines/hcp/imz-best-practices/altered-immunocompetence.html
- `OBS-LYM-SRC-002`: https://clsi.org/shop/standards/h42/
- `OBS-LYM-SRC-003`: https://euroflow.org/protocols/

## 3. Entidad observacional

Cada fila representa una medición de una población linfocitaria en una muestra y un instante determinados:

```text
E_LYM_Q = <
  Medicion_Linfocitaria_ID,
  Especimen,
  Instante_de_muestra,
  Poblacion_objetivo,
  Definicion_de_poblacion,
  Tipo_de_magnitud,
  Valor_original,
  Unidad,
  Metodo_de_enumeracion,
  Estado_de_calidad,
  Contexto_de_referencia,
  Procedencia_por_campo,
  Version
>
```

La identidad no corresponde a la persona ni a la etiqueta «linfopenia». Corresponde a una medición concreta. Varias mediciones pueden compartir muestra, población o instante sin fusionarse.

## 4. Observables candidatos

| Observable_ID | Contenido mínimo | Regla de identidad | `U` propia |
|---|---|---|---|
| `OBS-LYM-001` | tipo de muestra o material biológico | cambia si cambia el material del que procede la enumeración | `U(ESPECIMEN, causa)` |
| `OBS-LYM-002` | instante de obtención y precisión temporal | no se sustituye por fecha de informe o consulta | `U(TIEMPO_MUESTRA, causa)` |
| `OBS-LYM-003` | identidad de la población medida | linfocitos totales y cada subpoblación permanecen distinguibles | `U(POBLACION, causa)` |
| `OBS-LYM-004` | definición verificable de la población | conserva marcadores, estrategia o definición declarada sin presumir equivalencia entre métodos | `U(DEFINICION_POBLACION, causa)` |
| `OBS-LYM-005` | tipo de magnitud | distingue recuento absoluto expresado por volumen de proporción o porcentaje | `U(TIPO_MAGNITUD, causa)` |
| `OBS-LYM-006` | valor original comunicado | no se reemplaza por valor calculado o clasificado | `U(VALOR, causa)` |
| `OBS-LYM-007` | unidad original | una unidad ausente o incompatible impide la normalización | `U(UNIDAD, causa)` |
| `OBS-LYM-008` | método y base de enumeración | distingue medición directa, cálculo o combinación de plataformas cuando la fuente lo declare | `U(METODO, causa)` |
| `OBS-LYM-009` | estado de calidad o validez declarado por el laboratorio | no se infiere validez de la mera presencia de un número; resume la aceptación comunicada, no sustituye el expediente interno de preparación, calibración y control | `U(CALIDAD, causa)` |
| `OBS-LYM-010` | contexto de referencia comunicado y versionado | conserva intervalo, población de referencia y versión si existen; no los adopta como regla universal | `U(REFERENCIA, causa)` |

`Procedencia_por_campo` es metadato obligatorio, no un undécimo observable clínico. Incluye `Fuente_ID`, localizador, sistema o autoría autorizados, instante de captura y versión.

## 5. Separaciones obligatorias

1. Linfocitos totales no equivalen a una subpoblación.
2. Recuento absoluto por volumen y porcentaje no son intercambiables.
3. La etiqueta de población no sustituye su definición verificable.
4. Resultado directo y resultado calculado conservan método e inputs distintos.
5. Una medición cuantitativa no demuestra función linfocitaria.
6. Un resultado aislado no constituye trayectoria.
7. Un intervalo de referencia no constituye por sí solo relevancia clínica para `OP-IMM-001`.
8. Valor ausente, valor no válido y valor discordante producen causas de `U` diferentes.

## 6. Normalizadores previos candidatos

No son transductores finales `I_p^v` y no producen `0/1/U` sobre una proposición clínica.

### 6.1. Medición limpia

```text
N_LYM_MEAS(E_LYM_Q) -> <Poblacion, Definicion, Tipo, Valor, Unidad, Metodo, Tiempo, Calidad> | U
```

Conserva valor y unidad originales. No convierte porcentajes en valores absolutos ni reconstruye una población no declarada.

### 6.2. Pareado de magnitudes

```text
N_LYM_PAIR(Q_abs, Q_prop) -> <Muestra, Tiempo, Poblacion, Absoluto, Proporcion, Metodos> | U
```

Sólo parea resultados si muestra, tiempo y población son compatibles y la procedencia permite demostrarlo. No calcula el elemento ausente desde el presente sin una regla y todos sus inputs.

### 6.3. Serie temporal

```text
N_LYM_SERIES({E_LYM_Q}, h) -> secuencia_canonica_de_mediciones | U
```

Ordena por instante de muestra y claves de procedencia. No interpola, no atribuye causa y no transforma una secuencia en tendencia clínica.

### 6.4. Vinculación de referencia

```text
N_LYM_REF(E_LYM_Q, R_v) -> <Medicion, Referencia, Poblacion_aplicable, Version> | U
```

Vincula una referencia declarada si coincide la población, el tipo de magnitud, la unidad y el contexto. No clasifica automáticamente el resultado como normal o alterado.

## 7. Reglas de `U`

```text
U_LYM = <Campo_afectado, Codigo_de_causa, Fuentes_en_conflicto_o_ausentes, h, Version>
```

| Código | Se activa cuando | Efecto |
|---|---|---|
| `C_ESPECIMEN` | el material falta o es ambiguo | no se compara ni se agrupa la medición |
| `C_TIEMPO_MUESTRA` | falta instante o precisión suficiente | no se ordena ni se establece vigencia |
| `C_POBLACION` | la población falta o es ambigua | no se atribuye el resultado a una subpoblación |
| `C_DEFINICION_POBLACION` | faltan marcadores o definición necesarios para reconocerla | no se presume equivalencia semántica |
| `C_TIPO_MAGNITUD` | no se distingue absoluto, concentración o proporción | no se normaliza la magnitud |
| `C_VALOR` | el valor falta, es ilegible o no numérico cuando debe serlo | resultado indeterminado |
| `C_UNIDAD` | la unidad falta, es incompatible o ambigua | no se convierte ni compara |
| `C_METODO` | no puede conocerse si es directo, calculado o dependiente de otra plataforma | no se reconstruye la medición |
| `C_CALIDAD` | la fuente marca invalidez o la calidad requerida es desconocida | el valor no alimenta una conclusión limpia |
| `C_REFERENCIA` | la referencia falta, está desactualizada o no corresponde a población o magnitud | no se clasifica alteración |
| `C_CONFLICTO` | fuentes admisibles discrepan sin regla de precedencia | se conservan resultados y se detiene la operación afectada |
| `C_PROCEDENCIA` | falta fuente, localizador, corte o versión | el valor no se usa como evidencia limpia |

Ninguna `U` se cierra por plausibilidad, memoria del modelo, promedio, búsqueda libre o valor por defecto.

## 8. Proyección sobre `SEM-HUE-001`

`SEM-HUE-001` pregunta si existe una alteración cuantitativa pertinente del compartimento linfocitario. `G3-S2` sólo constituye la evidencia que permitiría formular después esa proposición:

```text
mediciones linfocitarias trazables
  + población y magnitud explícitas
  + tiempo, método, calidad y referencia aplicable
  -> entrada candidata para una futura regla | U tipada
```

No existe todavía la regla de «alteración», su horizonte, su criticidad o su consecuencia. Tampoco se decide qué población es obligatoria para cada uso.

## 9. Canonicalización y reproducción

Para una misma entrada, horizonte, fuentes y versiones:

1. los campos siguen el orden de `E_LYM_Q`;
2. las mediciones se ordenan por instante de muestra, `Fuente_ID` y localizador;
3. se conserva conjuntamente valor original y representación normalizada;
4. no se redondea, convierte o completa sin regla explícita;
5. un conflicto conserva todos los valores admisibles;
6. salida, `U`, traza y serialización deben coincidir byte a byte.

Una variación material de muestra, población, definición, magnitud, unidad, método, tiempo, calidad, referencia o fuente produce una entrada distinta. Un fallo técnico produce `EJECUCION_TECNICA_NO_VALIDA`.

## 10. Residuos deliberados

No se constituyen:

- función linfocitaria, proliferación o respuesta específica;
- interpretación morfológica;
- diagnóstico o etiología;
- intervalos universales, umbrales o gravedad;
- reglas por fármaco, enfermedad o finalidad;
- consecuencias clínicas;
- pruebas obligatorias o frecuencia de repetición;
- parámetros atómicos, matrices, rutas o frames;
- terminología de interoperabilidad.

## 11. Regla de cierre

`G3-S2` sólo puede cerrarse si una auditoría confirma simultáneamente:

1. exactamente diez observables y cuatro normalizadores;
2. separación de total, subpoblación, recuento absoluto por volumen y proporción;
3. separación entre cantidad y función;
4. procedencia por campo anterior a toda normalización;
5. método, calidad y referencia conservados sin convertirlos en conclusión;
6. doce causas de `U` con campo y efecto propios;
7. ausencia de umbral, diagnóstico o regla clínica;
8. reproducción byte a byte;
9. privacidad;
10. no apertura de `G4-S2` o `G5-ATM`.

## 12. Efecto y límites

`G3-S2` abre `G3-OBS` sólo para `SEM-HUE-001` y mantiene sus objetos como candidatos no adjudicados. No modifica `Q0`, `G3-S1` o `G4-S1` y mantiene en cero parámetros atómicos y matrices.

Es impersonal. No constituye diagnóstico, riesgo individual, prueba necesaria, interpretación de laboratorio, recomendación, autorización asistencial ni modificación del Lenguaje SV.
