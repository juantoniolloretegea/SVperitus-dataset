# Subsanación R1–R4

Corte de partida: `00a8a1aebd99cb1ac2984146148d4c61d2edbfe1`. El contrato /4 no se modifica.

| Id | Cambio | Ubicación |
|---|---|---|
| R1 | Atribución exclusiva por mayor S; la unión geométrica de B.3 se conserva para el residuo | `src/atribucion.rs`, `src/residuo.rs`, `src/reconocimiento.rs` |
| R2 | Cota de píxeles antes de `rasterize` (caja de `metrics`); `Parametros::comprobar` en `procesar_png` | `src/plantillas.rs`, `src/parametros.rs`, `src/lib.rs` |
| R3 | Selección §C entre celdas que superaron Q1 y Q2; empate residual | `src/tanda.rs`, `PROTOCOLO_CUALIFICACION_02.md` |
| R4 | Empate entre filas §C.7 | `src/reconocimiento.rs`, `empate_entre_filas` |

Pruebas: 13, retorno 0. Compilación `--locked --release`, retorno 0. Q1/Q2 no ejecutados.

Pendiente concreto: si varias celdas de la retícula con s=12,8 y el mismo theta superan Q1 y Q2, §C declara empate residual porque `n_min` no es clave de selección.
