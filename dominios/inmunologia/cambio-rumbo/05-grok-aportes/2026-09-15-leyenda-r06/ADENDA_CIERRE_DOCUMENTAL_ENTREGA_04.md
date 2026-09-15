# Adenda de cierre documental · entrega LEYENDA-CONTENIDO/4

**Estado.** Adenda vinculada al contrato candidato LEYENDA-CONTENIDO/4. No sustituye al contrato por una versión /5. No implementa el reconocedor ni autoriza campañas, síntesis de plantillas o ajuste de parámetros.

**Prioridad.** En caso de discrepancia, esta adenda prevalece sobre los pasajes de `CONTRATO_CANDIDATO_LEYENDA_CONTENIDO_4.md`, `SUBSANACION_ENTREGA_04.md`, `COTEJO_ENTREGA_04_SALIDA.txt` y `MANIFIESTO_ENTREGA_04.tsv` que precisa. El resto de /4 permanece vigente.

**Cortes.** Depósito de partida `SVperitus-dataset@ea4982398a42eba362f7bc7e9e00f5268f3058c9`. Recepción leída: Acta 002 §7, Lenguaje `146cb30e3cece036947081453d7e0982ca03a1cb`.

## 1. E2c

La fila E2c de /4 §F no puede leerse como «umbrales de residuo satisfechos, luego `CORRESPONDENCIA_CONFORME`».

Para emitir `CORRESPONDENCIA_CONFORME` en E2c deben concurrir, simultáneamente:

1. las condiciones generales del contrato: perfil válido, decodificación opaca, fondo conforme en W, tinta suficiente en B, tres cláusulas asignables del convenio 0↔1, 1↔2, U↔3, y dos separadores según §D;
2. la ausencia de **todas** las causas de adición inadmisible de /4 §B.6, incluida la plantilla no asignada de §B.6.2 (S ≥ theta en B para un miembro del vocabulario cerrado que no sea la pose asignada);
3. las condiciones residuales ya escritas en E2c: ninguna componente de I_res con área ≥ a_min, R_abs ≤ r_max y R_rel ≤ rho.

Los umbrales de residuo, por sí solos, no bastan. Una plantilla supernumeraria aceptada por §B.6.2 impide la conformidad aunque el residuo cuantificado sea bajo.

Esta precisión es documental. No se presenta como resultado de un ensayo.

## 2. Registro de ejecución

El fuente `COTEJO_ENTREGA_04.rs` imprime literalmente cada argumento recibido.

La línea depositada

`CMD=/tmp/cotejo_entrega_04 CONTRATO SUBSANACION RS`

es una **abreviatura mnemotécnica** de los tres archivos cotejados, no la invocación literal. Las líneas `ARCHIVO` de la misma salida contienen rutas absolutas bajo `/home/workdir/artifacts/`. Una invocación que pasara únicamente los tokens `CONTRATO`, `SUBSANACION` y `RS` no produciría esas rutas.

La invocación original completa no se conserva. Esa ausencia se declara. No se reconstruye una línea de comandos histórica ni se presenta otra ejecución como si fuera la original. El retorno 0 del programa acredita el cálculo de huellas sobre los archivos que figuran en `ARCHIVO`, no la igualdad entre dos descargas; esa igualdad la sostiene el cotejo receptor de Acta 002 §7.4.

## 3. Custodia

Se corrigen los campos desplazados de R01/R06 en `SUBSANACION_ENTREGA_04.md`. Los contenidos de los PNG y del paquete permanecen reservados; aquí solo constan sede, corte, ruta, miembro y huella.

| Testigo | Repositorio | Commit | Ruta del paquete | Miembro | SHA-256 |
|---|---|---|---|---|---|
| R01 | `juantoniolloretegea/SV-matematica-semantica-cuaternaria` | `86441ad4d375e31737dfcead0b1fd9cd52161883` | `laboratorio/tareas-watson/tuberias-ia/paridad-imagen-celula-matematica/estudio-nucleo-agentes/bis04-extension-perfiles-recursos-v0_1/EVIDENCIA_RASTER_CAPTOR.tar.gz` | `R01.png` | `3e9fae6d4844a07d0f1281d4974c5da1c5ce01c6dbc774be27b18f1735f7509d` |
| R06 | mismo | mismo | mismo paquete | `R06.png` | `829286631401c3208554a9f1f81bc091fa5355201490bd92ba72f9b0bb254827` |

Cotejo receptor de LEYENDA-CONTENIDO/3, ya depositado, no duplicado:

| Pieza | Repositorio | Commit de lectura | Ruta | Bytes | SHA-256 |
|---|---|---|---|---:|---|
| Fuente | `juantoniolloretegea/SV-lenguaje-de-computacion` | `146cb30e3cece036947081453d7e0982ca03a1cb` | `docs/calidad/tuberias-ia/continuacion-15-09-2026/COTEJO_RECEPCION_LEYENDA_03.rs` | 7960 | `0375a16d8e904b738e0f297ad1fa951b1e00c477d73db6a469296892fb237cd1` |
| Salida | mismo | mismo | `docs/calidad/tuberias-ia/continuacion-15-09-2026/COTEJO_RECEPCION_LEYENDA_03_SALIDA.txt` | 586 | `7152a1427240a200a57cc52e5798317134b010e00113faddb23ce3baddb4c887` |

Las huellas del cotejo /3 se toman de Acta 002 §6.3. El fuente no se vuelve a depositar en esta sede.

## 4. Conservación

Los catorce archivos existentes en `…/2026-09-15-leyenda-r06/` al corte `ea498239…` se conservan sin modificación. Esta entrega añade únicamente los dos archivos autorizados. No se crea herramienta nueva.
