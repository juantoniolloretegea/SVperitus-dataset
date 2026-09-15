# Revisión previa a la cualificación · realizacion-leyenda-01

**Alcance.** Lectura estática de los fuentes publicados en `SVperitus-dataset@78d87137ee195ca81bdf4471084b7039a05f164a`, rama `dominio-inmunologia`, contrastados con LEYENDA-CONTENIDO/4, su adenda de cierre documental y el Acta 002, §10.2 y §14. No se han modificado fuentes, contratos, parámetros ni dependencias. No se han ejecutado Q1, Q2 ni E1–E16.

**HEAD comprobado.** Coincidente con el corte de referencia. No había cambios posteriores que conservar.

**Compilación.** Se toma como acreditada la de Acta 002 §14 y `RECEPCION_FDEFLATE_Y_COMPILACION.md`: Rust 1.98.0, `cargo build --locked --release`, retorno 0 sobre el corte `0e36549f`. Esta revisión no la repite.

**Método.** Cada hallazgo se clasifica como *lectura* (constatable en el texto) o *ensayo* (exige ejecución sobre testigos). El contrato permanece candidato.

## 1. Atribución por S, empates, residuo y plantillas no asignadas

**Requisito.** /4 §B.4: cada píxel de `M_expl` se atribuye a lo sumo a una plantilla aceptada; si dos la contienen, prevalece la de mayor S; si `|Sa−Sb|≤epsilon`, `LEYENDA_ILEGIBLE`. /4 §B.3: `M_expl` es la unión de las máscaras aceptadas; el residuo se calcula sobre `I_res`. /4 §B.6.2 y adenda §1: una plantilla del vocabulario no asignada con `S≥theta` en B impide `CORRESPONDENCIA_CONFORME`.

**Ubicación.**

- Puntuación: `src/plantillas.rs`, `coincidencia` (S = |máscara ∩ tinta| / |máscara|).
- Almacenamiento de S: `src/plantillas.rs`, campo `Mascara.puntuacion`; asignación en `src/reconocimiento.rs` al construir candidatos.
- Empate: `src/reconocimiento.rs`, `empate_atribucion`.
- Filtro intrafamilia: `src/reconocimiento.rs`, `no_solapadas`.
- Residuo y B.6: `src/residuo.rs`, `calcular` y `adicion_inadmisible`.
- B.6.2: `src/reconocimiento.rs`, bucle sobre `VOCABULARIO` no usado en `aceptadas`.

**Conclusión (lectura).**

1. S se calcula conforme a §B.2 y se conserva en la máscara.
2. `empate_atribucion` solo declara `LEYENDA_ILEGIBLE` cuando hay intersección de píxeles y `|Sa−Sb|≤epsilon`. Si hay intersección y la diferencia de S supera epsilon, **no** atribuye el píxel a la plantilla de mayor S: ambas máscaras permanecen en `aceptadas` y `calcular` une todos sus píxeles en `M_expl`.
3. `no_solapadas` opera por familia (etiquetas, radios, separadores) y descarta un candidato si intersecta a uno ya elegido o si `|Δx|<d_min`. No implementa la atribución por mayor S. Entre familias distintas el solapamiento no se filtra ahí; queda para `empate_atribucion`, que tampoco reparte píxeles.
4. El residuo de `src/residuo.rs` coincide con §B.3 en I_AA (anillo geométrico ∩ vecindad-4 de la tinta de plantilla) e I_res. Las componentes se calculan solo sobre I_res. B.6.1 y B.6.3 están en `adicion_inadmisible`. B.6.2 está implementado como búsqueda posterior de vocabulario no asignado con `S≥theta`.
5. La adenda §1 (E2c no se reduce a umbrales de residuo) está cubierta en el flujo: `adicion_inadmisible(..., no_asignada)` se evalúa antes de emitir conformidad.

**Pendiente.** Corrección mínima propuesta: construir `M_expl` atribuyendo cada píxel compartido a la plantilla de mayor S y, solo entonces, calcular I_AA e I_res; mantener el rechazo por epsilon. El comportamiento ante solapamiento interfamilia con `|ΔS|>epsilon` no está ensayado.

## 2. Huella sobre los bytes TTF

**Requisito.** Acta 002 §10.2.3: la identidad debe calcularse sobre los bytes TTF utilizados, sin una huella textual separable que pueda omitirse. /4 fija `ae7b7855e115a5966d8b1b3f80f254ccc117ec86f9965e202ee2940453837280`.

**Ubicación.**

- `src/plantillas.rs`, `Sintetizador::cargar(&[u8])`: `sha256::hex(ttf)` frente a `HUELLA_TTF_CONTRATADA`.
- `src/lib.rs`, `procesar_png(png, ttf, p)`: no admite huella aparte; llama a `cargar(ttf)`.
- `src/main.rs`: calcula la misma huella antes de `procesar_png`; es un filtro adicional, no una vía de elusión.
- `src/sha256.rs`: FIPS 180-4 auxiliar. No es validación criptográfica independiente.

**Conclusión (lectura).** La entrada pública de la biblioteca no permite suministrar una huella distinta de la de los bytes. Un TTF con huella distinta no instancia el sintetizador. Queda por *ensayo* que un archivo de 759 720 B con esa huella exista en custodia y sea el mismo que usó resvg.

**Pendiente.** Localizar el TTF contratado en sede privada. No sustituirlo por otra revisión de DejaVu.

## 3. Admisión de parámetros y cotas

**Requisito.** §10.2.4: claves cerradas, rechazo de duplicados y de no finitos; cotas aplicadas antes de las operaciones que pretenden limitar.

**Ubicación.** `src/parametros.rs` (`analizar`, `desde_archivo`); `src/png_lectura.rs` (`CUOTA_LECTURA`); `src/reconocimiento.rs` (`max_rasterizaciones` antes de cada `raster`); `src/plantillas.rs` (`max_pixeles_mascara` **después** de rasterizar el glifo).

**Conclusión (lectura).**

| Control | Estado |
|---|---|
| Clave desconocida | Rechazo |
| Clave repetida | Rechazo |
| Clave ausente | Rechazo |
| Reales no finitos | Rechazo (`is_finite`) |
| `theta`, `epsilon`, `rho` ∈ [0,1] | Comprobado |
| `s_px` > 0 y finito | Comprobado |
| `paso_x ≥ 1`, `max_rasterizaciones ≥ 1` | Comprobado |
| Cuota PNG 1 000 000 B | Antes de `fs::read` completo: se consulta `metadata().len()` |
| `max_rasterizaciones` | Incremento y comparación **antes** de `raster` |
| `max_pixeles_mascara` | Se aplica **después** de `fontdue::rasterize` y del barrido del mapa; si se excede, se devuelve máscara vacía |

Defecto: `max_pixeles_mascara` no evita la rasterización; solo descarta el resultado. `Parametros::analizar` no está expuesto como constructor libre de archivo en la API pública, pero quien construya el struct a mano en Rust elude `analizar`. No hay constructor que fuerce las cotas.

**Pendiente.** Corrección mínima propuesta: interrumpir `raster` al superar la cota de píxeles durante el barrido, o rechazar la pose antes de rasterizar si la caja del glifo ya la excede. Ensayo de agotamiento de recursos: no ejecutado.

## 4. Retícula de 27 celdas, Q2 y cualificación

**Requisito.** §10.2.1: selección finita justificada, orden, aceptación, desempate y parada, sin ampliar la campaña. /4 §C *in fine*: si varias tuplas superan la cualificación, s más próximo a 12,8 px; theta mayor; rho menor; r_max menor; empate residual = fracaso de la cualificación. Q1/Q2 son la cualificación del método (§F), no la evaluación E1–E16.

**Ubicación.** `PROTOCOLO_CUALIFICACION_02.md`; `insumos/RETICULA_TANDA_01.tsv` (27 filas); `insumos/parametros.candidatos.txt`.

**Conclusión (lectura).**

- Justificación: producto 3×3×3 de `s_px` ∈ {12,0; 12,8; 13,6}, `theta` ∈ {0,70; 0,75; 0,80} y `n_min` ∈ {20; 40; 80}. Los demás parámetros permanecen fijos. No recorre las 39 366 celdas del protocolo 01.
- Orden del TSV: `s_px` ascendente, luego `theta` ascendente, luego `n_min` ascendente. Ese orden **no** es el de /4 §C (proximidad a 12,8; theta mayor).
- Éxito de una celda, según el protocolo 02: Q1 → `CORRESPONDENCIA_CONFORME` **y** Q2 → `DISCORDANCIA_CONTENIDO`.
- Parada: primera celda exitosa en el orden del TSV, o las 27 agotadas. Las celdas posteriores no se consideran.

**Q2 interviene en la selección.** Sí. Una celda que acierte Q1 y falle Q2 no se acepta. Por tanto, el testigo adversarial R06 participa en elegir los umbrales. Eso no es un ajuste retrospectivo de números ya vistos: el protocolo congela la retícula *antes* de ensayar. Sí es una **cualificación conjunta Q1+Q2**, no una cualificación solo sobre el control correcto seguida de una evaluación congelada sobre R06.

Qué permite concluir un éxito de tanda: existe al menos una celda precomprometida que, sobre esos dos testigos históricos, produce el par de códigos esperados. No permite concluir independencia, paridad visual, validez de E1–E16 ni que los umbrales sean los únicos admisibles. Un fracaso de tanda no autoriza a ampliar la retícula ni a mover umbrales.

**Pendiente.** Decidir, antes de Q1/Q2, si rige el orden de /4 §C o el del TSV. Distinguir expresamente si Q2 es criterio de *selección* o de *evaluación posterior* con parámetros ya congelados por Q1. Ensayo: no ejecutado.

## 5. Separador, anclaje, paso espacial e independencia del códec

**Requisito.** §10.2.5–6 y /4 §D y §E. Separador obligatorio por plantilla; alineación en filas 334–337; no acreditar independencia por el mero nombre del crate.

**Ubicación.**

- Separador: `src/plantillas.rs`, `TEXTO_SEPARADOR = "|"` (U+007C); `DECISIONES_PENDIENTES.md`; `PROTOCOLO_CUALIFICACION_02.md`.
- Anclaje: `src/plantillas.rs`, `raster`, `y_base - metrics.height - metrics.ymin`; filas en `src/regiones.rs`, `FILAS_ALINEACION`.
- Paso B.6.2 y búsqueda: `src/reconocimiento.rs`, `paso_x` sobre x ∈ [15, 310) y las cuatro filas.
- Códec: `src/png_lectura.rs` (`png` 0.17); `DEPENDENCIAS.md`; `evidencias/ARBOL_DEPENDENCIAS.txt`.

**Conclusión (lectura).**

- El separador U+007C es una lectura del SVG histórico `MUESTRA_SVG_PRODUCIDA.svg` @ `e9e4a359`. /4 §A declara que exigir ese carácter no altera el perfil. La correspondencia contractual del *glifo visible* con U+007C no está medida sobre píxeles.
- El anclaje vertical toma la fila de alineación como línea base de fontdue. Es convención de implementación, no una cláusula del perfil. /4 §C.7 habla de alineación en esas filas y de empate entre filas; el prototipo recorre las cuatro y no implementa un empate específico *entre filas* distinto del empate general de S.
- El paso espacial de B.6.2 y de la búsqueda principal es el `paso_x` de la celda (1 en la retícula). No hay un paso distinto no documentado.
- Independencia del códec: **no acreditada**. `png` 0.17 ≠ `tiny-skia` 0.12.0 del captor. Ambos decodifican PNG. No hay contraste de componentes efectivos (Huffman/deflate, expansión de paleta, filtro de fila) ni de salidas sobre el mismo IDAT. `fdeflate` 0.3.7 está en el árbol transitivo de `png` y su identidad de paquete está cotejada; eso no demuestra independencia frente al captor.

**Pendiente.** Ensayo del glifo U+007C sobre R01; declaración de incompatibilidad si fontdue no reproduce la geometría de resvg. Contraste de decodificación: fuera de esta revisión.

## Defectos y correcciones mínimas propuestas

| Id | Defecto (lectura) | Corrección mínima propuesta | ¿Bloquea Q1/Q2? |
|---|---|---|---|
| R1 | Solapamiento interfamilia con `|ΔS|>epsilon` no atribuye el píxel al mayor S | Atribuir píxel a mayor S antes del residuo | Sí, respecto de §B.4 |
| R2 | `max_pixeles_mascara` actúa después de rasterizar | Cortar o rechazar antes o durante el barrido | No para Q1/Q2 si las plantillas del TTF caben; sí para la cota declarada |
| R3 | Orden de tanda distinto de /4 §C; Q2 es criterio de selección | Fijar por escrito el régimen que rige antes de ensayar | Sí, de procedimiento |
| R4 | Empate entre filas de §C.7 no está aislado | Documentar que el empate general de S lo cubre, o implementarlo | Condicionado a R3 |

No se aplican en este acto.

## Dictamen de preparación

La transferencia y la compilación del corte publicado están acreditadas por Acta 002 §14. El prototipo es compilable y su texto cubre lectura PNG, regiones, S, residuo, B.6.2, huella TTF sobre bytes y una retícula finita.

No está preparado para ejecutar Q1/Q2 como cualificación conforme a /4 mientras R1 y R3 permanezcan abiertos: R1 desvía la atribución contractual; R3 decide, sin resolución escrita, si R06 selecciona umbrales. R2 y R4 son limitados.

El reconocedor **no** está cualificado. (p1+p3)-Bis **no** está cerrado. E1 sigue sin testigo material. La independencia del códec sigue sin acreditarse.
