# Subsanación R1–R4 · realizacion-leyenda-01

**Estado.** Aplicada sobre el prototipo experimental. El contrato candidato LEYENDA-CONTENIDO/4 y su adenda no se modifican. Q1, Q2 y E1–E16 no se ejecutan. La retícula de 27 celdas no se amplía. El reconocedor sigue sin cualificar.

**Sede.** `dominios/inmunologia/cambio-rumbo/05-grok-aportes/2026-09-15-leyenda-r06/realizacion-leyenda-01`, rama `dominio-inmunologia`.

**Corte de partida de la revisión estática.** `00a8a1aebd99cb1ac2984146148d4c61d2edbfe1`, documento `REVISION_PREVIA_CUALIFICACION_01.md`.

**Compilación de esta entrega.** Rust 1.98.0, `cargo test --locked` (16 pruebas, retorno 0) y `cargo build --locked --release` (retorno 0). Órdenes y salidas en `evidencias/ORDENES_R1_R4.txt`, `evidencias/PRUEBAS_R1_R4.txt` y `evidencias/COMPILACION_R1_R4.txt`.

## Hecho

La revisión previa constató cuatro defectos de lectura respecto de /4 §B.4, §10.2.4, §C y §C.7. Este acto los cierra en el texto del prototipo y en pruebas unitarias dirigidas. No acredita el comportamiento sobre R01 ni R06.

## Cambios

| Id | Defecto de la revisión | Fundamento | Cambio | Ubicación | Pruebas |
|---|---|---|---|---|---|
| R1 | El solapamiento interfamilia con |ΔS| > epsilon no atribuía el píxel a la plantilla de mayor S; ambas máscaras permanecían en `M_expl` | /4 §B.4 y §B.3 | Cada píxel de la unión se atribuye a la plantilla de mayor S. Si |Sa−Sb| ≤ epsilon, el diagnóstico es `LEYENDA_ILEGIBLE`. `M_expl` del residuo sigue siendo la unión geométrica de las máscaras aceptadas | `src/atribucion.rs`; llamada en `src/reconocimiento.rs`; `src/residuo.rs` usa `union_geometrica` | `union_conserva_ambos_pixeles`; `mayor_s_se_lleva_el_pixel_compartido`; `empate_por_epsilon`; `sin_solape_es_exclusiva` |
| R2 | `max_pixeles_mascara` actuaba después de `fontdue::rasterize`; un `Parametros` construido a mano eludía `analizar` | Acta 002 §10.2.4 | La caja de `metrics` se contrasta con la cota **antes** de `rasterize`. `Parametros::comprobar` cubre la entrada pública y `procesar_png` la invoca | `src/plantillas.rs`; `src/parametros.rs`; `src/lib.rs` | `rechaza_nan`; `rechaza_duplicado`; `comprobar_rechaza_struct_manual` |
| R3 | El orden del TSV no era el de /4 §C; no estaba escrito si Q2 participa en la selección | /4 §C *in fine* y §F | Q1 y Q2 siguen siendo, ambas, la cualificación del método. Entre las celdas que ya la superaron se elige: s más próximo a 12,8 px; theta mayor; rho menor; r_max menor. Empate residual en esas cuatro claves: la cualificación fracasa. `n_min` no es clave. El TSV solo identifica la fila | `src/tanda.rs`; `PROTOCOLO_CUALIFICACION_02.md` | `prefiere_s_proximo_a_128`; `a_igual_s_prefiere_theta_mayor`; `a_igual_s_y_theta_prefiere_rho_menor`; `a_igual_s_theta_rho_prefiere_r_max_menor`; `empate_residual_en_claves_c`; `doce_y_trece_seis_empatan_distancia_si_theta_igual`; `n_min_no_desempata_claves_c` |
| R4 | El empate entre filas de §C.7 no estaba aislado | /4 §C.7 | Misma plantilla, misma abscisa y filas de alineación distintas con |ΔS| ≤ epsilon produce `LEYENDA_ILEGIBLE` antes del filtro intrafamilia | `src/reconocimiento.rs`, `empate_entre_filas` | `filas_distintas_mismo_x_empatan`; `filas_con_s_lejos_no_empatan` |

## Alcance

- El prototipo implementa la atribución exclusiva de §B.4 sin alterar la definición de `M_expl` de §B.3.
- Las cotas de admisión se aplican sobre la entrada pública y antes de la rasterización que pretenden limitar.
- La tanda autorizable permanece en 27 celdas. La selección entre supervivientes de Q1+Q2 sigue §C y no el orden de origen del TSV.
- Q1 y Q2 no se convierten en evaluación E1–E16. Un éxito de tanda, cuando se autorice, solo acreditará que alguna celda precomprometida produce el par de códigos de §F sobre los dos testigos históricos.

## Límites y deuda restante

1. **Empate residual de la retícula publicada.** En `insumos/RETICULA_TANDA_01.tsv`, rho y r_max son constantes. Las tres celdas con s = 12,8 y theta = 0,80 (órdenes 16, 17 y 18; n_min ∈ {20, 40, 80}) empatan en las cuatro claves de §C. Si más de una de ellas supera Q1 y Q2, la cualificación fracasa. `n_min` no desempata. No se amplía la retícula para evitarlo.
2. **TTF contratado.** La huella se calcula sobre los bytes leídos y se exige `ae7b7855e115a5966d8b1b3f80f254ccc117ec86f9965e202ee2940453837280`. El archivo de 759 720 B permanece en custodia privada.
3. **Independencia del códec.** No acreditada. `png` 0.17 ≠ `tiny-skia` 0.12.0 del captor; un nombre de crate distinto no demuestra independencia.
4. **Glifo separador y anclaje.** U+007C y la línea base de fontdue en las filas 334–337 son convenciones de implementación ya declaradas. La correspondencia geométrica con resvg no está medida sobre píxeles.
5. **Ensayo sobre testigos.** Q1, Q2 y E1–E16 no se han ejecutado. E1 sigue sin testigo material. (p1+p3)-Bis no está cerrado.
6. **Cota de píxeles en ensayo de agotamiento.** La caja de `metrics` evita `rasterize` cuando ya excede la cota; no se ha ensayado un TTF adverso que agote recursos dentro de la caja declarada.

## Decisión

R1–R4 quedan subsanados en el texto del prototipo y cubiertos por dieciséis pruebas unitarias. El contrato candidato no se acomoda a la implementación. La cualificación conjunta Q1+Q2 permanece autorizable solo cuando se disponga del TTF contratado y de los PNG R01 y R06, y solo sobre la retícula de 27 celdas ya congelada.

## Estado

Prototipo compilable. Reconocedor no cualificado. Campaña Q/E no abierta.

La comparación de empate de R1 se corrigió después de este acto: el criterio vigente es el de [CORRECCION_R1_EMPATE_INDEPENDIENTE_DEL_ORDEN.md](CORRECCION_R1_EMPATE_INDEPENDIENTE_DEL_ORDEN.md). El contrato, los parámetros y la retícula no cambian.
