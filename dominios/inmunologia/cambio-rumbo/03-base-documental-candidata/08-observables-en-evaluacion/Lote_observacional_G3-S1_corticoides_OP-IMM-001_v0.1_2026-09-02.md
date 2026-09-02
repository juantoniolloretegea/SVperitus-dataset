# Lote observacional `G3-S1` — exposición a glucocorticoides en `OP-IMM-001` v0.1

- **Fecha:** 02-09-2026
- **Rama:** `dominio-inmunologia`
- **Puerta:** `G3-OBS`
- **Estatuto:** `OBSERVABLES_Y_NORMALIZADORES_CANDIDATOS_NO_ADJUDICADOS`
- **Operación:** `OP-IMM-001`
- **Preguntas de origen:** `SEM-EXP-002`, `SEM-EXP-003`, `SEM-EXP-005`
- **Base matemática:** contrato `NA0-MATH` v0.3
- **Perímetro:** caracterización de la exposición sistémica a glucocorticoides; no evaluación del riesgo ni decisión asistencial

## 1. Decisión del lote

La exposición a glucocorticoides no se representa mediante una etiqueta única como «corticoide presente», «dosis alta» o «prednisona-equivalente». Esas formas mezclan hechos observables con una regla dependiente de finalidad.

El objeto de `G3-S1` es un **registro estructurado de exposición**. Conserva por separado identidad farmacológica, formulación, vía, estado de ejecución, magnitud, pauta y tiempo. Ninguno de estos campos es todavía un `PARAMETRO_ATOMICO`; son observables o metadatos obligatorios de observación.

Las reglas de riesgo vacunal, profilaxis infecciosa u otra finalidad se construirán después como usos distintos sobre el mismo registro. No se permite que el primer umbral encontrado se convierta en verdad universal.

## 2. Por qué el recorte es necesario

Tres fuentes muestran que la etiqueta «glucocorticoide» no basta:

1. El Centro Colaborador de la Organización Mundial de la Salud para Metodología de Estadísticas de Medicamentos separa los corticoides sistémicos de múltiples usos locales, distingue vías de administración y advierte que las preparaciones depot pueden tener dosis diarias definidas distintas por sus indicaciones. La dosis diaria definida no se adopta aquí como conversión clínica de riesgo.
2. Los Centers for Disease Control and Prevention declaran que la cantidad y duración necesarias para producir inmunosupresión no están bien definidas y, para seguridad de vacunas vivas, combinan absorción sistémica, dosis, duración y pauta; además separan tratamientos breves, alternos, sustitutivos y vías locales o inhaladas.
3. Las recomendaciones EULAR de 2022 sobre infecciones oportunistas formulan para profilaxis frente a *Pneumocystis jirovecii* un intervalo de dosis y duración distinto del utilizado en la regla vacunal.

La conclusión constitutiva no es adoptar ninguno de esos umbrales. Es demostrar que **finalidad, vía, magnitud, pauta y tiempo no pueden colapsarse**.

## 3. Fuentes aplicadas

| Fuente_ID | Fuente | Versión o corte | Localizador utilizado | Función en este lote |
|---|---|---|---|---|
| `OBS-GC-SRC-001` | WHO Collaborating Centre for Drug Statistics Methodology, ATC/DDD Index, `H02` y `H02AB` | actualización 20-01-2026 | apartados `H02`, `H02A`, `H02AB`; tabla por vía y notas de preparados depot | sostiene la separación de uso sistémico, uso local, vía y formulación; no aporta una equivalencia clínica de riesgo |
| `OBS-GC-SRC-002` | CDC, *Altered Immunocompetence* | página actualizada 26-06-2024, consultada 02-09-2026 | apartado `Corticosteroids` | demuestra que la regla vacunal combina dosis, duración, absorción sistémica y pauta, y que el propio umbral se declara dependiente de contexto |
| `OBS-GC-SRC-003` | Fragoulis et al., *2022 EULAR recommendations for screening and prophylaxis of chronic and opportunistic infections in adults with autoimmune inflammatory rheumatic diseases* | Ann Rheum Dis. 2023;82:742–753; PMID 36328476; DOI 10.1136/ard-2022-223335 | recomendación sobre profilaxis frente a *Pneumocystis jirovecii* | prueba de divergencia entre finalidades; no se convierte en regla de `OP-IMM-001` |

Enlaces fijados:

- `OBS-GC-SRC-001`: https://atcddd.fhi.no/atc_ddd_index/?code=H02AB&showdescription=yes
- `OBS-GC-SRC-002`: https://www.cdc.gov/vaccines/hcp/imz-best-practices/altered-immunocompetence.html
- `OBS-GC-SRC-003`: https://pubmed.ncbi.nlm.nih.gov/36328476/

## 4. Entidad observacional

Cada exposición se identifica mediante `Exposicion_GC_ID`. No identifica a una persona ni a un medicamento en abstracto: identifica una exposición propuesta, prescrita o administrada dentro del episodio autorizado.

```text
E_GC = <
  Exposicion_GC_ID,
  Agente,
  Formulacion,
  Via,
  Estado_de_ejecucion,
  Expresion_de_dosis,
  Pauta,
  Inicio_planificado,
  Fin_planificado,
  Eventos_administrados,
  Fin_real_documentado,
  Procedencia_por_campo,
  Version
>
```

`Estado_de_ejecucion` distingue como mínimo `PROPUESTO`, `PRESCRITO`, `INICIADO`, `ADMINISTRADO`, `INTERRUMPIDO`, `FINALIZADO` y `U_ESTADO`. El conjunto describe la relación documental con la exposición; no describe eficacia, toxicidad ni riesgo.

Un final planificado deliberadamente abierto se registra como `ABIERTO_POR_PLAN`. Un final ausente o ambiguo se registra como `U_FIN`; ambos estados no son equivalentes.

## 5. Observables candidatos

| Observable_ID | Contenido mínimo | Tipo | Regla de identidad | `U` propia |
|---|---|---|---|---|
| `OBS-GC-001` | agente glucocorticoide | identidad farmacológica | una sustancia activa declarada; una combinación exige componentes separados | `U(AGENTE, causa)` |
| `OBS-GC-002` | formulación | texto o identidad verificable de la preparación | cambia si la formulación altera liberación, absorción o interpretación temporal | `U(FORMULACION_VIA, causa)` |
| `OBS-GC-003` | vía de administración | vía documentada | sistémica y local no se infieren una de otra | `U(FORMULACION_VIA, causa)` |
| `OBS-GC-004` | estado de ejecución | valor controlado con fecha de corte | propuesto, prescrito y administrado no se sustituyen entre sí | `U(EJECUCION, causa)` |
| `OBS-GC-005` | expresión de dosis por administración | `<valor, unidad, base>` | la base distingue dosis absoluta, por peso u otra expresión declarada | `U(DOSIS_UNIDAD_BASE, causa)` |
| `OBS-GC-006` | pauta prescrita o propuesta | frecuencia y patrón expresados sin promedio implícito | diario, alterno, intermitente y eventos de pulso permanecen distinguibles | `U(PAUTA, causa)` |
| `OBS-GC-007` | inicio planificado | instante o fecha con precisión declarada | no se sustituye por la fecha de prescripción | `U(TIEMPO, causa)` |
| `OBS-GC-008` | fin planificado | instante, fecha, `ABIERTO_POR_PLAN` o `U_FIN` | abierto por decisión y desconocido son estados distintos | `U(TIEMPO, causa)` |
| `OBS-GC-009` | evento administrado | `<instante, agente, formulación, vía, dosis, procedencia>` | cada administración verificable es un evento; no se inventa desde la orden | `U(EVENTO, causa)` |
| `OBS-GC-010` | fin real documentado | instante o fecha con precisión declarada | exige un cierre explícito; la última administración conocida no demuestra por sí sola que la exposición haya finalizado | `U(TIEMPO, causa)` |

`Procedencia_por_campo` no es un undécimo observable clínico. Es metadato obligatorio de cada valor: `Fuente_ID`, localizador, instante de captura, autoría o sistema autorizado y versión.

## 6. Dominios de valor derivados candidatos

El lote admite cuatro normalizadores previos. No son todavía los transductores finales `I_p^v : X_p × Contexto -> {0,1,U}` porque aún no existe un parámetro adjudicado.

### 6.1. Identidad y vía

```text
N_GC_ID(E_GC) -> <Agente, Formulacion, Via> | U
```

No transforma una vía local en sistémica por plausibilidad. Tampoco utiliza el grupo ATC como sustituto de la exposición real.

### 6.2. Magnitud documentada

```text
N_GC_MAG(E_GC, h) -> <Agente, Via, Dosis, Unidad, Base, Pauta, Estado, h> | U
```

No calcula prednisona-equivalente, no promedia pulsos, no confunde dosis propuesta con administrada y no convierte automáticamente una dosis por peso en dosis absoluta.

### 6.3. Duración

```text
N_GC_DUR(E_GC, h) -> <Tipo_duracion, Inicio, Fin_o_corte, Valor, Unidad_temporal, Estado> | U
```

`Tipo_duracion` distingue `PLANIFICADA` y `REAL_OBSERVADA`. Una pauta abierta puede producir una duración planificada abierta, pero nunca una cifra cerrada. La duración real observada se acota por los eventos admisibles; sólo un cierre explícito constituye el fin real del tratamiento. Última administración y fin real permanecen separados.

### 6.4. Recencia

```text
N_GC_REC(E_GC, h) -> <Ultima_administracion, Intervalo_hasta_h, Precision> | U
```

La última administración se obtiene del máximo temporal de `OBS-GC-009`; no se confunde con `OBS-GC-010`. La recencia no declara que el tratamiento haya finalizado ni que el efecto inmunológico siga activo. Esas inferencias requieren evidencia o reglas posteriores dependientes de agente, pauta, finalidad y fuente.

## 7. Proyección sobre las preguntas G2

| Pregunta | Evidencia observacional mínima en este recorte | Resultado de G3-S1 |
|---|---|---|
| `SEM-EXP-002` | `OBS-GC-001`, `003`, `004`, `005`, `006` y horizonte | magnitud normalizable o `U` tipada; sin umbral clínico |
| `SEM-EXP-003` | `OBS-GC-004`, `007`, `008`, `009`, `010` y horizonte | duración planificada y real separables o `U` tipada |
| `SEM-EXP-005` | entidad `E_GC` completa en los campos aplicables | perfil observacional estructurado; no un escalar ni un parámetro único |

La retirada de `SEM-EXP-005` no elimina `SEM-EXP-002` o `SEM-EXP-003`; elimina la tipificación específica de glucocorticoides. La retirada de magnitud no elimina duración. La retirada de duración no elimina identidad o vía. Esta divergencia confirma que los tres objetos no son sinónimos.

## 8. Reglas de `U`

Toda incertidumbre observacional usa la forma:

```text
U_GC = <Campo_afectado, Codigo_de_causa, Fuentes_en_conflicto_o_ausentes, h, Version>
```

| Código de causa | Se activa cuando | Efecto |
|---|---|---|
| `C_AGENTE` | el agente falta o es ambiguo | no se calcula magnitud comparable ni equivalencia |
| `C_FORMULACION_VIA` | la formulación o la vía faltan o son ambiguas | no se clasifica exposición sistémica |
| `C_DOSIS_UNIDAD_BASE` | falta valor, unidad o base | magnitud indeterminada |
| `C_PAUTA` | frecuencia o patrón no permiten reconstrucción fiel | no se promedia ni se acumula |
| `C_TIEMPO` | inicio, fin, corte o última administración son insuficientes | duración o recencia indeterminadas según el campo afectado |
| `C_EJECUCION` | no puede distinguirse propuesta, prescripción y administración | no se presenta exposición real como confirmada |
| `C_EVENTO` | un evento carece de identidad, instante, dosis o fuente suficientes | el evento no alimenta la exposición real normalizada |
| `C_CONFLICTO` | dos fuentes admisibles discrepan sin regla de precedencia | se conservan ambos valores y se detiene la normalización afectada |
| `C_PROCEDENCIA` | falta fuente, localizador, corte o versión | el valor no se usa como evidencia limpia |
| `C_EQUIVALENCIA` | se solicita conversión sin tabla, versión, finalidad y procedencia constituidas | no se calcula prednisona-equivalente |
| `C_FINALIDAD` | se solicita «alto riesgo» sin consecuencia y regla constituidas | no se clasifica el riesgo |

Ninguna `U` se cierra con texto libre generado, búsqueda en Internet o valor por defecto.

## 9. Canonicalización y reproducción

Para una misma entrada canónica, horizonte, fuentes y versiones:

1. los campos se serializan en el orden de la tupla `E_GC`;
2. los eventos se ordenan por instante y, en empate, por `Fuente_ID` y localizador;
3. el valor original y su representación normalizada se conservan juntos;
4. ninguna conversión redondea sin regla explícita;
5. una discordancia no se resuelve por prioridad implícita;
6. la salida, las `U` y la traza deben ser idénticas byte a byte.

Una diferencia puramente sintáctica que la entrada canónica declare equivalente produce la misma salida. Una diferencia material —agente, vía, dosis, base, pauta, instante, estado o fuente— debe permanecer visible y puede cambiar la salida. Un fallo de herramienta produce `EJECUCION_TECNICA_NO_VALIDA`, no un resultado alternativo.

## 10. Residuos deliberados

No se constituyen en este lote:

- tablas de equivalencia entre glucocorticoides;
- dosis acumulada equivalente;
- reglas de «dosis alta»;
- efecto inmunológico residual;
- umbrales vacunales o de profilaxis;
- interacción con otros inmunosupresores;
- consecuencias clínicas plenas;
- parámetros atómicos;
- matrices, rutas, composiciones o frames.

Estos residuos no son olvido. Exigen, respectivamente, fuente de conversión versionada, finalidad clínica, consecuencia `G4-CON` o adjudicación posterior.

## 11. Regla de cierre de `G3-S1`

El lote sólo puede cerrarse si una auditoría confirma simultáneamente:

1. que los diez observables pueden variar independientemente cuando su significado clínico lo exige;
2. que planificación y administración no se fusionan;
3. que vía, formulación y pauta no se reducen a una dosis media;
4. que `ABIERTO_POR_PLAN` no equivale a dato ausente;
5. que toda conversión y todo umbral permanecen fuera;
6. que cada `U` conserva causa y efecto propios;
7. que la procedencia se vincula antes de normalizar;
8. que la reproducción determinista pasa;
9. y que no se ha abierto `G4-CON`, `G5-ATM` ni ninguna matriz.

## 12. Efecto y límites

`G3-S1` abre `G3-OBS` sólo para este recorte y deja sus objetos como candidatos. No modifica `Q0`, no añade elementos a la tabla autorizada `A_v` y mantiene en cero parámetros atómicos y matrices.

Este documento es impersonal. No contiene episodios, personas o centros identificables. No constituye recomendación, prescripción, profilaxis, pauta, equivalencia, umbral, riesgo individual, autorización asistencial ni modificación del Lenguaje SV.
