# Lote de consecuencias `G4-S1` — errores sobre exposición a glucocorticoides en `OP-IMM-001` v0.1

- **Fecha:** 02-09-2026
- **Rama:** `dominio-inmunologia`
- **Puerta:** `G4-CON`
- **Estatuto:** `CONSECUENCIAS_CANDIDATAS_NO_ADJUDICADAS`
- **Operación:** `OP-IMM-001`
- **Dependencia cerrada:** `G3-S1` v0.1
- **Perímetro:** consecuencias de ignorar, confundir o trasladar indebidamente la exposición a glucocorticoides ya representable en `E_GC`

## 1. Decisión del lote

Este lote no pregunta todavía qué dosis, pauta o duración hacen verdadera una proposición clínica. Pregunta algo anterior: **qué consecuencia verificable puede producir cada error de conocimiento que `G3-S1` ya permite distinguir**.

La cadena obligatoria es:

```text
observable o U afectada
  -> error u omisión definido
  -> daño epistemológico inmediato
  -> finalidad clínica afectada
  -> consecuencia clínica potencial, si la fuente la sostiene
```

No se permite saltar un eslabón. Una cita añadida a una conclusión no reconstruye la cadena. Una consecuencia clínica no se atribuye a un mero dato ausente si sólo está demostrado el daño epistemológico intermedio.

El lote es finito: contiene exactamente cinco consecuencias candidatas. No pretende enumerar todos los efectos adversos de los glucocorticoides ni todas las decisiones clínicas en las que intervienen.

## 2. Clases separadas

| Clase | Qué constituye | Qué no constituye |
|---|---|---|
| `CONSECUENCIA_EPISTEMOLOGICA` | pérdida, falsedad o traslado inválido del conocimiento que alimentaría una decisión | daño clínico consumado, indicación o causalidad individual |
| `CONSECUENCIA_CLINICA_POTENCIAL` | resultado clínico adverso que una fuente vincula a la finalidad y al error descritos | predicción individual, incidencia universal o certeza causal |

Las dos clases no se compensan ni se confunden. El daño epistemológico puede existir sin que llegue a producirse el daño clínico; cuando una cadena clínica está sostenida, ambos eslabones se conservan.

## 3. Fuentes clínicas aplicadas

| Fuente_ID | Fuente y versión | Localizador | Función exacta |
|---|---|---|---|
| `CON-GC-SRC-001` | CDC, *Altered Immunocompetence*, página actualizada 26-06-2024, consultada 02-09-2026 | `General Principles`, párrafos sobre seguridad y efectividad; `Live, Attenuated Viral and Bacterial Vaccines: Safety`; `Corticosteroids` | sostiene que la inmunocompetencia alterada afecta de forma distinta a seguridad de vacunas vivas y efectividad, y que la exposición a corticoides requiere cantidad, duración, absorción y pauta dependientes de finalidad |
| `CON-GC-SRC-002` | CDC, *Pneumocystis Pneumonia Basics*, página actualizada 24-04-2024, consultada 02-09-2026 | `Key points`, `Overview`, `Risk factors`, `Prevention` | sostiene que la neumonía por *Pneumocystis* es grave, puede ser mortal, se asocia a inmunodepresión incluida la farmacológica por corticoides y puede motivar valoración preventiva |
| `CON-GC-SRC-003` | Fragoulis et al., recomendaciones EULAR 2022 | Ann Rheum Dis. 2023;82:742–753; PMID 36328476; DOI 10.1136/ard-2022-223335; recomendación sobre profilaxis de *Pneumocystis jirovecii* | sostiene que la consideración de profilaxis se formula en un contexto clínico y de exposición definidos; no crea una regla universal ni se traslada a vacunación |

Enlaces fijados:

- `CON-GC-SRC-001`: https://www.cdc.gov/vaccines/hcp/imz-best-practices/altered-immunocompetence.html
- `CON-GC-SRC-002`: https://www.cdc.gov/pneumocystis-pneumonia/about/index.html
- `CON-GC-SRC-003`: https://pubmed.ncbi.nlm.nih.gov/36328476/

Las fuentes de gobierno internas son el lote `G3-S1` v0.1 y el contrato matemático `NA0-MATH` v0.3. Definen la forma de representación y trazabilidad; no sustituyen la evidencia clínica.

## 4. Consecuencias candidatas

### 4.1. `CON-GC-REP-001` — exposición real falsamente representada

- **Clase:** `CONSECUENCIA_EPISTEMOLOGICA`.
- **Entrada afectada:** `OBS-GC-004`, `007`, `008`, `009`, `010`; `U(EJECUCION)`, `U(EVENTO)` y `U(TIEMPO)`.
- **Error:** presentar como administrada una exposición sólo propuesta o prescrita; presentar como completa una pauta interrumpida; o usar el plan como sustituto de los eventos y del fin real.
- **Daño inmediato:** el expediente declara una exposición real que no ocurrió, o no declara la que ocurrió.
- **Dirección:** falso positivo o falso negativo, según el error.
- **Finalidad afectada:** cualquier regla posterior que dependa de exposición real, duración o recencia.
- **Consecuencia clínica:** no se predica una única consecuencia clínica universal. La salida correcta es bloqueo o `U` en la regla afectada hasta reparar la representación.
- **Trazabilidad:** lote `G3-S1`, §§4–6 y 8–9.
- **Límite:** no permite estimar riesgo, elegir intervención ni graduar gravedad individual.

### 4.2. `CON-GC-PUR-001` — clasificación falsa por traslado entre finalidades

- **Clase:** `CONSECUENCIA_EPISTEMOLOGICA`.
- **Entrada afectada:** `OBS-GC-001`–`006`, `N_GC_ID`, `N_GC_MAG`, `N_GC_DUR`; `U(EQUIVALENCIA)` y `U(FINALIDAD)`.
- **Error:** usar una dosis diaria definida, una equivalencia no versionada, un promedio de pauta o un umbral construido para una finalidad como si gobernara otra.
- **Daño inmediato:** clasificación falsa de la exposición para la pregunta clínica concreta.
- **Dirección:** falso positivo o falso negativo.
- **Finalidad afectada:** seguridad vacunal, efectividad vacunal, valoración de profilaxis u otra que se constituya después.
- **Consecuencia clínica:** depende de la finalidad; no se agrega aquí en un único daño ni se compensa entre finalidades.
- **Trazabilidad:** `CON-GC-SRC-001`, apartado `Corticosteroids`; `CON-GC-SRC-003`, recomendación de profilaxis; lote `G3-S1`, §§2, 6.2 y 8.
- **Límite:** no adopta conversión, umbral o etiqueta de «alto riesgo».

### 4.3. `CON-GC-VAC-SAF-001` — omisión de una condición relevante para seguridad de vacuna viva

- **Clase:** `CONSECUENCIA_CLINICA_POTENCIAL`.
- **Entrada afectada:** identidad, vía, ejecución, magnitud, pauta y duración de `E_GC`, con procedencia válida.
- **Error:** un falso negativo de exposición inmunosupresora impide que la evaluación de seguridad reconozca una posible inmunocompetencia alterada.
- **Daño epistemológico:** no se activa o se contamina la evaluación específica de seguridad de una vacuna viva.
- **Consecuencia clínica potencial:** administración en un contexto en el que pueden producirse complicaciones graves por replicación no controlada del microorganismo atenuado.
- **Dirección dominante:** falso negativo.
- **Gravedad candidata:** `ALTA_POTENCIAL`; no es puntuación ni predicción individual.
- **Fuente y localizador:** `CON-GC-SRC-001`, `General Principles`, `Live, Attenuated Viral and Bacterial Vaccines: Safety` y `Corticosteroids`.
- **Condiciones que permanecen abiertas:** vacuna concreta, agente, vía, magnitud, pauta, duración, función inmune, ventana temporal y regla aplicable.
- **Límite:** no declara contraindicación, no selecciona vacuna y no fija intervalo.

### 4.4. `CON-GC-VAC-EFF-001` — omisión de una condición relevante para efectividad vacunal

- **Clase:** `CONSECUENCIA_CLINICA_POTENCIAL`.
- **Entrada afectada:** identidad, ejecución, magnitud, pauta, duración y recencia de `E_GC`, con procedencia válida.
- **Error:** un falso negativo o una cronología incorrecta hace que la evaluación de efectividad no reconozca el periodo de posible inmunocompetencia alterada.
- **Daño epistemológico:** la respuesta esperable y la necesidad de revisión posterior se valoran sobre una exposición falsa o incompleta.
- **Consecuencia clínica potencial:** respuesta vacunal subóptima y eventual necesidad de repetir la vacunación cuando corresponda conforme a una regla autorizada.
- **Dirección:** predominantemente falso negativo; puede existir falso positivo si se atribuye inmunosupresión inexistente.
- **Gravedad candidata:** `RELEVANTE_DEPENDIENTE_DE_CONTEXTO`.
- **Fuente y localizador:** `CON-GC-SRC-001`, `General Principles`, `Non-live Vaccines: Effectiveness` y `Corticosteroids`.
- **Condiciones que permanecen abiertas:** vacuna, estado inmunitario, exposición real, momento, regla de repetición y autoridad clínica.
- **Límite:** no prescribe aplazamiento, repetición o calendario.

### 4.5. `CON-GC-PJP-001` — omisión de la valoración preventiva de neumonía por *Pneumocystis*

- **Clase:** `CONSECUENCIA_CLINICA_POTENCIAL`.
- **Entrada afectada:** identidad, vía, ejecución, magnitud, pauta y duración de `E_GC`, además de los modificadores del huésped que se constituyan en otros lotes.
- **Error:** un falso negativo o una clasificación trasladada desde otra finalidad evita que se abra, cuando corresponda, la valoración específica de riesgo y prevención de neumonía por *Pneumocystis jirovecii*.
- **Daño epistemológico:** se pierde una oportunidad de evaluar una prevención clínicamente pertinente; no se afirma que toda exposición exija profilaxis.
- **Consecuencia clínica potencial:** riesgo grave no valorado de neumonía por *Pneumocystis*, infección que puede ser mortal.
- **Dirección dominante:** falso negativo; el falso positivo también puede conducir a intervenciones innecesarias, pero sus consecuencias exigen otro lote y no se inventan aquí.
- **Gravedad candidata:** `ALTA_POTENCIAL`.
- **Fuente y localizador:** `CON-GC-SRC-002`, `Key points`, `Overview`, `Risk factors` y `Prevention`; `CON-GC-SRC-003`, recomendación sobre profilaxis.
- **Condiciones que permanecen abiertas:** enfermedad subyacente, otros inmunosupresores, agente, exposición real, magnitud, duración, regla de riesgo, contraindicaciones y balance individual.
- **Límite:** no indica profilaxis, fármaco, dosis, umbral o duración.

## 5. Tabla de conjunción

| Consecuencia_ID | Observable o regla de origen | Error mínimo necesario | Finalidad | Salida permitida en G4 |
|---|---|---|---|---|
| `CON-GC-REP-001` | ejecución y tiempo reales | plan tratado como hecho o evento tratado como cierre | todas las posteriores | `U` o bloqueo de la regla afectada |
| `CON-GC-PUR-001` | magnitud, duración, equivalencia y finalidad | conversión o regla trasladada sin autoridad | dependiente de uso | `U(EQUIVALENCIA)` o `U(FINALIDAD)` |
| `CON-GC-VAC-SAF-001` | perfil de exposición + futura regla vacunal | falso negativo material | seguridad de vacuna viva | consecuencia potencial trazada; sin recomendación |
| `CON-GC-VAC-EFF-001` | perfil de exposición + futura regla vacunal | falso negativo o cronología falsa | efectividad vacunal | consecuencia potencial trazada; sin recomendación |
| `CON-GC-PJP-001` | perfil de exposición + futuros modificadores | falso negativo o regla impropia | valoración preventiva de PJP | consecuencia potencial trazada; sin profilaxis |

La fila no es una ruta clínica. Sólo declara qué piezas deberán estar presentes si una futura operación pretende usar la consecuencia.

## 6. Reglas de criticidad y `U`

1. `ALTA_POTENCIAL` no equivale a consecuencia individual segura ni a veto ya ejecutable.
2. Una consecuencia de gravedad potencial alta con un eslabón crítico en `U` no se declara ausente ni se compensa con costes, tiempo o disponibilidad.
3. La falta de una regla de activación impide transformar la consecuencia en consejo.
4. Seguridad y efectividad vacunales son consecuencias diferentes; una no sustituye ni compensa a la otra.
5. La relevancia para PJP no se deduce de una regla vacunal, ni la regla vacunal se deduce de PJP.
6. Un falso positivo puede ser dañino, pero no se le atribuye una intervención o efecto adverso concreto sin fuente y lote propios.

## 7. Procedencia previa a la conclusión

Toda instancia futura de una consecuencia deberá poder serializar antes de cualquier conclusión:

```text
<
  Consecuencia_ID,
  Observable_ID_o_U,
  valor_y_procedencia,
  error_definido,
  Fuente_ID_clinica,
  localizador,
  finalidad,
  transicion,
  incertidumbres,
  version,
  autoridad
>
```

Si falta alguno de los elementos exigibles, la consecuencia no puede usarse como explicación clínica. Una narración posterior o una cita añadida no subsanan la ausencia de la cadena.

## 8. Canonicalización y reproducción

Ante la misma entrada canónica, horizonte, fuentes, versiones, finalidad y autoridad:

- la misma consecuencia candidata se activa o permanece inactiva de forma idéntica;
- se conservan los mismos eslabones, `U`, localizadores y orden;
- la serialización debe ser idéntica byte a byte;
- una variación material debe quedar visible y producir una nueva entrada canónica;
- un fallo técnico produce `EJECUCION_TECNICA_NO_VALIDA`, nunca una conclusión alternativa.

Este requisito no autoriza todavía un motor generativo a emitir consejo. El camino normativo sólo admite ejecución que demuestre esa reproducción.

## 9. Residuos deliberados

Quedan fuera de `G4-S1`:

- consecuencias de falsos positivos ligadas a una intervención concreta;
- toxicidad de cualquier profilaxis;
- efectos adversos generales de glucocorticoides;
- interacción con otros inmunosupresores;
- equivalencias, umbrales e intervalos ejecutables;
- reglas por vacuna, enfermedad o institución;
- costes, disponibilidad y organización asistencial;
- incidencia, probabilidad o puntuación individual;
- parámetros atómicos, matrices, rutas, composiciones y frames.

Su exclusión no niega su relevancia. Impide que amplíen este corte sin una dependencia semántica constituida.

## 10. Regla de cierre

`G4-S1` sólo puede cerrarse si una auditoría externa confirma simultáneamente:

1. exactamente cinco consecuencias y dos clases;
2. separación entre daño epistemológico y daño clínico potencial;
3. fuente y localizador clínicos anteriores a la conclusión;
4. correspondencia con observables y `U` de `G3-S1`;
5. ausencia de salto causal desde dato ausente a daño consumado;
6. separación entre seguridad vacunal, efectividad y PJP;
7. ausencia de umbral, equivalencia, prescripción o intervención;
8. tratamiento conservador de la criticidad y de `U`;
9. determinismo byte a byte del contrato;
10. privacidad y no apertura de `G5-ATM`.

## 11. Efecto y límites

Este lote abre `G4-CON` sólo para este recorte y mantiene sus cinco objetos como candidatos no adjudicados. No modifica `G3-S1`, no constituye parámetros atómicos, no diseña matrices o rutas y no modifica el Lenguaje SV.

Es impersonal: no contiene episodios, personas o centros identificables. No constituye recomendación, indicación, prescripción, contraindicación, profilaxis, vacunación, predicción individual ni autorización asistencial.
