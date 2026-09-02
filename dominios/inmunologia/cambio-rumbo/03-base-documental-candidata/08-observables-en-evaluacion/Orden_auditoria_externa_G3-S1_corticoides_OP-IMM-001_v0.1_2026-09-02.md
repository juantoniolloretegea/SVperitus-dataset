# Orden única de auditoría externa — `G3-S1` corticoides en `OP-IMM-001` v0.1

## 1. Objeto exacto

Audite el contenido material de estos dos objetos en la rama `dominio-inmunologia`:

| Objeto | Bytes | SHA-256 |
|---|---:|---|
| `Lote_observacional_G3-S1_corticoides_OP-IMM-001_v0.1_2026-09-02.md` | 13 716 | `49f15ef048230b3f8eb010bd11713121122102711efb8988b02156cc0221584c` |
| `Adversarial_interna_G3-S1_corticoides_OP-IMM-001_v0.1_2026-09-02.md` | 7 934 | `fad82e6467fc35dca9736edeeb5ca18c31becc95b0e8409870b3d1db41d95916` |

Directorio:

`dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/08-observables-en-evaluacion/`

Línea base: commit `0d885602721d495bdfba87631f44eb2afbe98645`.

Calcule de nuevo bytes y SHA-256. Identifique el commit candidato y compruebe su diff completo contra la línea base. La orden queda fuera del objeto auditado.

## 2. Regla de suficiencia

No basta con confirmar que el texto parece prudente. Para cada ataque B–J debe construir al menos un contraejemplo material y comprobar si el articulado lo absorbe sin recurrir a intención, conocimiento implícito o una fase futura no declarada.

La adversarial interna orienta, pero no es prueba. No copie su dictamen.

## 3. Ataque A — identidad y regresión

Compruebe:

1. identidad exacta de ambos objetos;
2. que el diff sólo añade el lote, su adversarial, esta orden y la referencia mínima en el índice rector;
3. que no cambian catálogo v0.8, `Q0`, lotes G2, contrato matemático, pilotos, política de privacidad, ITI ni Lenguaje SV;
4. que siguen existiendo 32 preguntas precursoras, cero parámetros atómicos y cero matrices.

## 4. Ataque B — suficiencia y función de las fuentes

Abra y contraste las tres fuentes declaradas:

- WHO Collaborating Centre, ATC/DDD `H02` y `H02AB`;
- CDC, *Altered Immunocompetence*, apartado `Corticosteroids`;
- Fragoulis et al., recomendaciones EULAR 2022, PMID 36328476, DOI 10.1136/ard-2022-223335.

Determine:

1. si WHO separa uso sistémico, usos locales, vías y preparados depot;
2. si CDC combina, para su finalidad vacunal, absorción sistémica, dosis, duración y pauta;
3. si EULAR utiliza para profilaxis frente a *Pneumocystis jirovecii* un intervalo distinto;
4. si esa divergencia basta para rechazar un umbral universal sin que el lote adopte regla clínica alguna;
5. si una dosis diaria definida ATC ha sido correctamente excluida como tabla de equivalencia inmunosupresora.

Toda afirmación debe indicar fuente, versión, localizador y evidencia encontrada. Si una fuente no puede abrirse, declare `U_ACCESO` para esa comprobación; no complete por memoria.

## 5. Ataque C — entidad observacional

Intente falsar la tupla `E_GC`.

Compruebe si oculta bajo un campo único objetos que pueden variar de forma independiente. Ataque especialmente:

- agente frente a formulación;
- formulación frente a vía;
- plan frente a prescripción y administración;
- dosis frente a pauta;
- inicio frente a fin;
- duración planificada frente a real;
- última administración frente a persistencia del efecto.

Si falta un campo material, identifíquelo y demuestre el caso que no puede representarse. No proponga terminologías o estándares de interoperabilidad: no están abiertos en este corte.

## 6. Ataque D — diez observables candidatos

Verifique que existen exactamente `OBS-GC-001`–`OBS-GC-010`, sin duplicados ni huecos.

Para cada observable, aplique:

1. variación independiente;
2. retirada o ablación;
3. `U` propia por campo;
4. diferencia entre dato clínico y metadato de procedencia;
5. posible fusión o partición material.

Clasifique cada uno como:

- `OBSERVABLE_NECESARIO`;
- `METADATO_OBLIGATORIO`;
- `DUPLICADO`;
- `COMPUESTO_A_REVISAR`;
- `U_NO_ADJUDICABLE`.

No convierta ningún observable en parámetro atómico.

## 7. Ataque E — planificación y ejecución

Construya al menos estos casos:

- dosis propuesta no prescrita;
- dosis prescrita no administrada;
- plan de catorce días con dos días administrados;
- tratamiento interrumpido y reiniciado;
- orden y registro de administración discordantes.

Compruebe que el lote no fabrica exposición real, no rellena intervalos y no sustituye duración real por duración planificada.

## 8. Ataque F — magnitud, pauta y tiempo

Ataque con:

- pauta diaria frente a alterna;
- pulsos frente a administración continua con la misma suma;
- pauta intermitente;
- dosis absoluta frente a dosis por peso sin peso válido;
- final `ABIERTO_POR_PLAN` frente a `U_FIN`;
- última administración conocida sin regla de efecto residual.

Compruebe que `N_GC_MAG`, `N_GC_DUR` y `N_GC_REC` preservan las diferencias y que ningún promedio o duración cerrada aparece sin regla.

## 9. Ataque G — equivalencia y finalidad

Intente introducir:

1. prednisona-equivalente mediante conocimiento memorizado;
2. dosis diaria definida ATC como equivalencia;
3. umbral CDC de vacunas vivas como regla de profilaxis;
4. intervalo EULAR de profilaxis como regla vacunal;
5. etiqueta «alto riesgo» sin consecuencia constituida.

El resultado correcto debe ser una `U` trazable o exclusión, nunca una clasificación clínica. Compruebe que el lote distingue normalizadores G3 de los futuros transductores finales `I_p^v` con salida `0/1/U`.

## 10. Ataque H — `U`, conflicto y procedencia

Verifique la forma `U_GC` y sus once códigos de causa. Construya casos de:

- dato ausente;
- unidad ambigua;
- vía conflictiva;
- dos fuentes admisibles discordantes;
- fuente sin localizador;
- fuente posterior al corte;
- texto libre plausible pero no verificable.

Compruebe que cada `U` identifica campo, causa, fuente u omisión, horizonte y versión; que la discordancia conserva ambos valores; y que la procedencia se vincula antes de la normalización.

## 11. Ataque I — determinismo y fallo técnico

Ejecute o modele materialmente:

1. dos ejecuciones idénticas;
2. eventos permutados con las mismas claves canónicas;
3. empate temporal con distinta procedencia;
4. cambio mínimo pero material de vía, unidad o estado;
5. fallo de una herramienta.

La misma entrada canónica debe producir salida, `U`, traza y serialización idénticas byte a byte. Una diferencia material debe permanecer visible. Un fallo técnico sólo puede producir `EJECUCION_TECNICA_NO_VALIDA`.

## 12. Ataque J — privacidad y no avance

Compruebe que los objetos son impersonales y no contienen episodios, personas o centros identificables.

Verifique que el lote no constituye:

- equivalencias o umbrales;
- consecuencias clínicas plenas;
- parámetros atómicos;
- matrices, rutas, composiciones o frames;
- recomendación o autorización asistencial;
- cambios de interoperabilidad o del Lenguaje SV.

`G3-S1` no puede abrir `G4-CON` ni `G5-ATM` por su mera existencia.

## 13. Recuentos obligatorios

Entregue recuento calculado de:

- tres preguntas G2 de origen;
- tres fuentes;
- una entidad `E_GC`;
- diez observables;
- cuatro normalizadores previos;
- once códigos de causa de `U`;
- cero equivalencias;
- cero umbrales;
- cero parámetros atómicos;
- cero matrices, rutas o frames.

## 14. Entrega

Emita una sola auditoría con:

1. identidad calculada y diff exacto;
2. dictamen `PASA`, `PASA_CON_REPAROS`, `NO_PASA` o `U_AUDITORIA_INCOMPLETA`;
3. tabla de ataques A–J;
4. contraejemplo material por ataque B–J;
5. clasificación individual de `OBS-GC-001`–`010`;
6. reparos numerados con severidad, objeto, texto, evidencia, consecuencia y corrección mínima;
7. incertidumbres residuales con operación exacta de cierre;
8. recuentos verificados;
9. declaración separada de si `G3-S1_CERRABLE`;
10. declaración expresa de que el dictamen no autoriza abrir `G4-CON` o `G5-ATM`.

## 15. Límites

- No escribir en GitHub.
- No abrir PR.
- No tocar `main`.
- No modificar los objetos.
- No buscar una cohorte ni abrir estado del arte.
- No diseñar la matriz, la ruta o el frame.
- No proponer dosis, profilaxis, vacunación o tratamiento.
- No usar episodios reales como ejemplos.
- No convertir prudencia verbal en prueba: falsar el objeto.
