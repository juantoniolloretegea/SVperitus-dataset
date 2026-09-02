# Lote de consecuencias `G4-S2` — errores sobre cuantificación linfocitaria en `OP-IMM-001` v0.1

- **Fecha:** 02-09-2026
- **Rama:** `dominio-inmunologia`
- **Puerta:** `G4-CON`
- **Estatuto:** `CONSECUENCIAS_CANDIDATAS_NO_ADJUDICADAS`
- **Operación:** `OP-IMM-001`
- **Dependencia cerrada:** `G3-S2` v0.1
- **Perímetro:** consecuencias de omitir, fusionar o interpretar indebidamente la cuantificación linfocitaria representable en `E_LYM_Q`

## 1. Decisión del lote

Una cifra linfocitaria no es todavía una proposición clínica. Antes de atribuirle significado deben conservarse población, definición, tipo de magnitud, unidad, método, muestra, tiempo, calidad, referencia y procedencia.

La cadena obligatoria es:

```text
observable o U afectada
  -> error definido
  -> daño epistemológico inmediato
  -> finalidad clínica afectada
  -> asociación clínica potencial, sólo si la fuente la sostiene
```

El último eslabón no transforma asociación en causalidad. Tampoco permite trasladar un resultado poblacional a una persona, adoptar el umbral de un estudio, inferir función, diagnosticar o recomendar una actuación.

El lote contiene exactamente cinco consecuencias candidatas. Es deliberadamente no vacunal.

## 2. Clases separadas

| Clase | Qué constituye | Qué no constituye |
|---|---|---|
| `CONSECUENCIA_EPISTEMOLOGICA` | pérdida o falsificación del conocimiento por identidad, magnitud, tiempo, calidad o inferencia inválidos | daño clínico consumado, causalidad o decisión |
| `ASOCIACION_CLINICA_POTENCIAL_NO_CAUSAL` | consecuencia cuya pertinencia para la valoración clínica se apoya en una asociación poblacional trazada | predicción individual, umbral universal, etiología, diagnóstico o indicación |

Las clases no se compensan. La segunda sólo puede activarse después de una primera cadena correcta y conserva explícitamente población, diseño, confusión residual y límites de transporte.

## 3. Fuentes aplicadas

| Fuente_ID | Fuente y versión | Localizador | Función exacta |
|---|---|---|---|
| `CON-LYM-SRC-001` | Warny et al., *Lymphopenia and risk of infection and infection-related death in 98,344 individuals from a prospective Danish population-based study*, PLOS Medicine 2018 | DOI `10.1371/journal.pmed.1002685`; PMID `30383787`; `Abstract`, `Conclusions`, `Methods: Blood lymphocyte count` y limitaciones | sostiene una asociación entre la categoría definida en esa cohorte y hospitalización por infección y muerte relacionada con infección; declara que no puede deducirse causalidad; no aporta regla universal ni predicción para `OP-IMM-001` |
| `CON-LYM-SRC-002` | CDC, *Altered Immunocompetence*, actualizada 26-06-2024, consultada 02-09-2026 | `General Principles`, párrafos sobre estudios de inmunidad celular | sostiene que números linfocitarios, concentraciones/proporciones de subpoblaciones y ensayos de proliferación o función son objetos diferentes; no sostiene una inferencia clínica desde el recuento |
| `CON-LYM-SRC-003` | CLSI `H42-A2`, segunda edición, publicada 22-05-2007 y reafirmada 06-2017 | ficha pública, `Abstract` y `Scope` | sostiene la dependencia de muestra, proceso, calibración, análisis, calidad y comparabilidad; declara fuera de alcance intervalos generales; no aporta significado clínico individual |

Enlaces fijados:

- `CON-LYM-SRC-001`: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002685
- `CON-LYM-SRC-002`: https://www.cdc.gov/vaccines/hcp/imz-best-practices/altered-immunocompetence.html
- `CON-LYM-SRC-003`: https://clsi.org/shop/standards/h42/

Las fuentes internas de gobierno son `G3-S2` v0.1 y `NA0-MATH` v0.3. Ordenan la cadena; no sustituyen la evidencia clínica.

## 4. Consecuencias candidatas

### 4.1. `CON-LYM-ID-001` — estado falso por fusión de poblaciones o definiciones

- **Clase:** `CONSECUENCIA_EPISTEMOLOGICA`.
- **Entrada afectada:** `OBS-LYM-003`, `OBS-LYM-004`; `U(POBLACION)` y `U(DEFINICION_POBLACION)`.
- **Error:** tratar linfocitos totales y una subpoblación como sustituibles, o fusionar etiquetas iguales con definiciones no demostradas como equivalentes.
- **Daño inmediato:** se atribuye a una población un resultado que pertenece a otra, o se oculta una discrepancia material.
- **Dirección:** falso positivo o falso negativo.
- **Salida permitida:** conservar las mediciones separadas y producir `U` o bloqueo de la operación afectada.
- **Fuente y localizador:** `CON-LYM-SRC-002`, `General Principles`; `CON-LYM-SRC-003`, `Abstract` y `Scope`.
- **Límite:** no clasifica alteración, función o riesgo.

### 4.2. `CON-LYM-MAG-001` — estado falso por confusión de magnitud, unidad o método

- **Clase:** `CONSECUENCIA_EPISTEMOLOGICA`.
- **Entrada afectada:** `OBS-LYM-005`–`008`; `U(TIPO_MAGNITUD)`, `U(UNIDAD)` y `U(METODO)`.
- **Error:** intercambiar recuento absoluto y proporción, convertir sin todos los inputs o ocultar si el resultado es directo o calculado.
- **Daño inmediato:** se fabrica comparabilidad o se completa un valor que la evidencia no contiene.
- **Dirección:** falso positivo o falso negativo.
- **Salida permitida:** valores originales separados, `U` tipada o rechazo de la comparación.
- **Fuente y localizador:** `CON-LYM-SRC-003`, `Abstract` y `Scope`; lote `G3-S2`, §§5–7.
- **Límite:** no adopta fórmula, intervalo o umbral.

### 4.3. `CON-LYM-TIME-001` — estado actual o trayectoria falsos

- **Clase:** `CONSECUENCIA_EPISTEMOLOGICA`.
- **Entrada afectada:** `OBS-LYM-001`, `002`, `009`, `010`; `U(ESPECIMEN)`, `U(TIEMPO_MUESTRA)`, `U(CALIDAD)` y `U(REFERENCIA)`.
- **Error:** usar fecha de informe como fecha de muestra, presentar un resultado antiguo como actual, construir tendencia con puntos no comparables o aplicar una referencia incompatible.
- **Daño inmediato:** el expediente declara un estado o una evolución que no están sostenidos.
- **Dirección:** falso positivo, falso negativo o falsa trayectoria.
- **Salida permitida:** serie descriptiva sin inferencia, `U` o bloqueo.
- **Fuente y localizador:** `CON-LYM-SRC-003`, `Abstract` y `Scope`; lote `G3-S2`, §§5–9.
- **Límite:** no define vigencia, tendencia clínica ni frecuencia de repetición.

### 4.4. `CON-LYM-FUN-001` — función inmunitaria inventada desde cantidad

- **Clase:** `CONSECUENCIA_EPISTEMOLOGICA`.
- **Entrada afectada:** cualquier `E_LYM_Q` cuantitativa y `U(FUNCION_NO_OBSERVADA)` futura.
- **Error:** interpretar recuento o proporción normal como función conservada, o valor bajo como demostración de incapacidad funcional.
- **Daño inmediato:** se crea un estado funcional no medido y se contamina cualquier razonamiento que dependa de él.
- **Dirección:** falso positivo o falso negativo funcional.
- **Salida permitida:** declarar `FUNCION_NO_CONSTITUIDA` y mantener separada la medición cuantitativa.
- **Fuente y localizador:** `CON-LYM-SRC-002`, `General Principles`, separación entre números, subpoblaciones y pruebas de proliferación o función.
- **Límite:** no obliga a solicitar una prueba funcional ni niega su posible pertinencia.

### 4.5. `CON-LYM-INF-001` — asociación con infección omitida o indebidamente individualizada

- **Clase:** `ASOCIACION_CLINICA_POTENCIAL_NO_CAUSAL`.
- **Entrada afectada:** medición cuantitativa válida, población definida, referencia aplicable y horizonte compatibles, más modificadores del huésped aún no constituidos.
- **Error:** (a) omitir de la valoración una alteración cuantitativa genuina que pudiera ser pertinente; o (b) presentar una asociación poblacional como causa o pronóstico individual.
- **Daño epistemológico:** por defecto, se pierde una señal potencialmente relevante; por exceso, se fabrica certeza individual.
- **Asociación clínica sostenida:** en la cohorte general danesa de Warny et al., la categoría de linfopenia definida por el estudio se asoció con hospitalización por infección y muerte relacionada con infección.
- **Límite causal obligatorio:** el diseño observacional no permite deducir causalidad; la propia fuente lo declara.
- **Condiciones abiertas:** definición de alteración aplicable, edad, enfermedad, tratamiento, comorbilidad, serie temporal, subpoblación, función, horizonte, población de transporte y demás modificadores.
- **Salida permitida:** `ASOCIACION_POBLACIONAL_PERTINENTE_PENDIENTE_DE_REGLA` o `U`; nunca riesgo individual, diagnóstico o actuación.
- **Fuente y localizador:** `CON-LYM-SRC-001`, `Abstract`, `Conclusions`, definición del estudio y limitaciones.
- **Límite:** no incorpora sus puntos de corte, razones de riesgo ni algoritmo predictivo al dominio.

## 5. Tabla de conjunción

| Consecuencia_ID | Eslabón mínimo | Error | Salida máxima en G4 |
|---|---|---|---|
| `CON-LYM-ID-001` | población + definición | fusión o sustitución | `U` o bloqueo epistemológico |
| `CON-LYM-MAG-001` | magnitud + valor + unidad + método | conversión o comparación falsa | `U` o rechazo |
| `CON-LYM-TIME-001` | muestra + tiempo + calidad + referencia | estado o trayectoria falsos | serie descriptiva o `U` |
| `CON-LYM-FUN-001` | medición cuantitativa | función inferida sin observable | `FUNCION_NO_CONSTITUIDA` |
| `CON-LYM-INF-001` | medición válida + futura regla y contexto | omisión o individualización indebida | asociación poblacional trazada o `U` |

Esta tabla no es una ruta clínica. Sólo declara dependencias mínimas y límites de salida.

## 6. Reglas de causalidad, transporte y `U`

1. Asociación poblacional no equivale a causa individual.
2. El umbral usado por un estudio no se convierte en intervalo universal ni en transductor.
3. Una cohorte de población general no se traslada automáticamente a una persona inmunosuprimida, a otra población o a una subpoblación linfocitaria.
4. Recuento cuantitativo no demuestra función.
5. Resultado aislado no demuestra persistencia ni trayectoria.
6. Un valor dentro de una referencia no excluye una alteración no medida; uno fuera no establece etiología.
7. Una `U` crítica no se rellena por plausibilidad, promedio, memoria del modelo o búsqueda libre.
8. Costes, tiempo y disponibilidad no compensan una incertidumbre clínica grave ni crean causalidad.

## 7. Procedencia previa a la conclusión

Toda instancia futura debe serializar, antes de emitir la salida:

```text
<
  Consecuencia_ID,
  Observable_ID_o_U,
  valor_original_y_procedencia,
  error_definido,
  Fuente_ID_clinica,
  localizador,
  poblacion_y_diseno,
  finalidad,
  transicion,
  limites_de_transporte_y_causalidad,
  incertidumbres,
  version,
  autoridad
>
```

Una cita añadida después no reconstruye la cadena. Si falta un eslabón exigible, la consecuencia no es admisible como explicación clínica.

## 8. Canonicalización y reproducción

Ante la misma entrada canónica, horizonte, fuentes, versiones, finalidad y autoridad:

- deben coincidir consecuencia, cadena, `U`, localizadores, límites y orden;
- la serialización debe coincidir byte a byte;
- una variación material debe producir otra entrada canónica;
- un fallo técnico sólo produce `EJECUCION_TECNICA_NO_VALIDA`.

Este contrato no autoriza a un modelo generativo actual a emitir consejo si no demuestra la reproducción exigida.

## 9. Residuos deliberados

Quedan fuera:

- ensayos de función linfocitaria;
- definición clínica de alteración pertinente;
- etiologías y diagnósticos;
- intervalos o umbrales universales;
- riesgos absolutos, probabilidades y pronóstico individual;
- decisiones sobre pruebas, tratamiento, prevención o derivación;
- reglas por enfermedad, fármaco, centro o población;
- toxicidad, costes y organización asistencial;
- parámetros atómicos, matrices, rutas, composiciones y frames.

## 10. Regla de cierre

`G4-S2` sólo puede cerrarse si una auditoría externa confirma simultáneamente:

1. exactamente cinco consecuencias y dos clases;
2. cuatro consecuencias epistemológicas y una asociación clínica potencial no causal;
3. correspondencia con observables y `U` de `G3-S2`;
4. separación de población, definición, magnitud, unidad, método, tiempo, calidad y referencia;
5. separación estricta entre cantidad y función;
6. ausencia de causalidad o predicción individual desde la cohorte;
7. no adopción del umbral, efecto o algoritmo del estudio;
8. procedencia anterior a la conclusión;
9. reproducción byte a byte, privacidad y finitud;
10. ausencia de diagnóstico, intervención, parámetro, matriz, ruta o frame.

## 11. Efecto y límites

Este lote abre `G4-CON` sólo para las consecuencias de errores en la cuantificación linfocitaria. No modifica `G3-S2`, no abre `G5-ATM` y mantiene sus objetos como candidatos no adjudicados.

Es impersonal y no contiene episodios, personas o centros identificables. No constituye diagnóstico, pronóstico, interpretación de laboratorio, recomendación, indicación, prescripción, prueba obligatoria ni autorización asistencial. No modifica el Lenguaje SV.
