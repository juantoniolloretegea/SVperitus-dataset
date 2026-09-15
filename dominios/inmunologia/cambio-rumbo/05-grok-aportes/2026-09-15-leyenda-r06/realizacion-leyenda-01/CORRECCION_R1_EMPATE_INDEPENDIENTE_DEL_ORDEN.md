# Corrección R1 · empate independiente del orden

**Estado.** Aplicada sobre el prototipo experimental. El contrato candidato LEYENDA-CONTENIDO/4, su adenda, los parámetros de trabajo y la retícula de 27 celdas no se modifican. Q1, Q2 y E1–E16 no se ejecutan. El reconocedor sigue sin cualificar.

**Sede.** `dominios/inmunologia/cambio-rumbo/05-grok-aportes/2026-09-15-leyenda-r06/realizacion-leyenda-01`, rama `dominio-inmunologia`.

**Corte de partida.** Fuentes R1–R4 completas en `fdc211fec991b062bc5cd8668536e0c6f7f6a76f`. Esta corrección sustituye únicamente el criterio de empate de `src/atribucion.rs`.

## Hecho

`atribuir` contrastaba cada máscara nueva solo con el dueño vigente del píxel. Si un tercero con S estrictamente mayor cubría el mismo píxel y se evaluaba antes que el par próximo, el empate entre las otras dos quedaba sin declarar y el resultado era `Exclusiva`.

Eso incumple /4 §B.4: si *dos* plantillas aceptadas contienen el mismo píxel y `|Sa−Sb|≤epsilon`, el código es `LEYENDA_ILEGIBLE`, con independencia de que una tercera plantilla tenga S mayor.

## Fundamento

/4 §B.4 exige atribución a lo sumo a una plantilla y rechazo por epsilon entre *cualquier* par que comparta el píxel. /4 §B.3 fija `M_expl` como unión geométrica; el residuo no se calcula sobre el mapa exclusivo.

## Cambio

`atribuir` reúne, por píxel, las puntuaciones de todas las máscaras que lo cubren y compara todos los pares. Un solo par con `|ΔS|≤epsilon` produce `Empate`. Si ningún par empató, `mapa_exclusivo` sigue atribuyendo el píxel a la plantilla de mayor S. `residuo::calcular` continúa usando `union_geometrica`.

## Contraejemplo

Tres máscaras sobre el píxel (11, 320); `epsilon = 0,05`:

| Máscara | S |
|---|---|
| A | 0,80 |
| B | 0,95 |
| C | 0,82 |

`|SA−SC| = 0,02 ≤ 0,05`. Las seis permutaciones de `{A,B,C}` deben declarar `Empate`. El criterio anterior solo lo hacía en las permutaciones que enfrentaban A y C antes de que B quedara como dueño.

Control sin empate: A = 0,70, B = 0,95, C = 0,80, mismo `epsilon`. Ningún par cumple `|ΔS|≤epsilon`. El píxel compartido se atribuye a B y la unión geométrica conserva los píxeles exclusivos de A y de C.

## Evidencia

- `cargo test --locked`: 18 pruebas, retorno 0. Incluye `empate_en_las_seis_permutaciones` y `control_sin_empate_atribuye_al_mayor_s`.
- `cargo build --locked --release`: retorno 0.
- Rust 1.98.0. Órdenes y salidas: `evidencias/ORDENES_R1_ORDEN.txt`, `evidencias/PRUEBAS_R1_ORDEN.txt`, `evidencias/COMPILACION_R1_ORDEN.txt`.

## Alcance e impacto

El reconocedor declara ahora `LEYENDA_ILEGIBLE` ante cualquier par aceptado que comparta un píxel con diferencia de S no mayor que epsilon, sea cual sea el orden de las máscaras. La atribución al mayor S y la unión geométrica del residuo no cambian cuando no hay empate.

## Límites

Siguen vigentes los de `SUBSANACION_R1_R4.md`: TTF en custodia, independencia de códec no acreditada, retícula de 27 celdas con empate residual posible en s = 12,8 y theta = 0,80, Q1/Q2 no ejecutados.

## Estado

Prototipo compilable. Reconocedor no cualificado. Campaña Q/E no abierta.
