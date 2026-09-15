# Protocolo previo de cualificación · realizacion-leyenda-01

**Estado.** Protocolo depositado. Esta entrega **no ejecuta** Q1 ni Q2. Compilar no cualifica el reconocedor. El contrato LEYENDA-CONTENIDO/4 y su adenda rigen; la precisión de Acta 002 §9.3 rige sobre el alcance del cotejo receptor §7.4.

## 1. Testigos (custodia privada)

No se publican en este directorio.

| ID | Repositorio | Commit | Paquete | Miembro | SHA-256 |
|---|---|---|---|---|---|
| Q1 = R01 | `juantoniolloretegea/SV-matematica-semantica-cuaternaria` | `86441ad4d375e31737dfcead0b1fd9cd52161883` | `laboratorio/tareas-watson/tuberias-ia/paridad-imagen-celula-matematica/estudio-nucleo-agentes/bis04-extension-perfiles-recursos-v0_1/EVIDENCIA_RASTER_CAPTOR.tar.gz` | `R01.png` | `3e9fae6d4844a07d0f1281d4974c5da1c5ce01c6dbc774be27b18f1735f7509d` |
| Q2 = R06 | mismo | mismo | mismo | `R06.png` | `829286631401c3208554a9f1f81bc091fa5355201490bd92ba72f9b0bb254827` |

Paquete: 4308172 bytes, blob `814619348801577afc28b8fb5be45f73e518d46c` (Acta 002 §9.2). No se descomprime en esta entrega.

TTF contratado (insumo público, no testigo raster): SHA-256 `ae7b7855e115a5966d8b1b3f80f254ccc117ec86f9965e202ee2940453837280`, 759720 bytes. Se suministra por `--fuente`. Esta entrega no lo adjunta: la copia 2.37 descargada públicamente midió 757076 bytes y otra huella; no se sustituye.

## 2. Selección de parámetros

Ningún valor está cualificado. El archivo `insumos/parametros.candidatos.txt` es un **punto inicial de retícula**, no un resultado.

Regla de generación (cuando se autorice la cualificación):

1. Fijar `s_px` en {12,0; 12,8; 13,6} y `tau_t` en {64, 96, 128}.
2. Para cada par, explorar `theta` en {0,70; 0,75; 0,80}, `epsilon` en {0,01; 0,02}, `d_min` en {6, 8, 10}, `g_min` en {1, 2, 3}, `w_sep` en [1,6] como intervalo.
3. `n_min` en {20, 40, 80}; `a_min` en {4, 8, 12}; `rho` en {0,05; 0,08; 0,12}; `r_max` en {16, 24, 40}.

Desempate (contrato /4 §C): `s_px` más próximo a 12,8; `theta` mayor; `rho` menor; `r_max` menor. Empate residual: la cualificación fracasa. No se altera el perfil para acomodar un resultado.

Límite: no más de 200 combinaciones en una tanda. Parada si Q1 no alcanza `CORRESPONDENCIA_CONFORME` en ninguna celda o si Q2 no alcanza `DISCORDANCIA_CONTENIDO` cuando Q1 sí es conforme.

## 3. Cuotas

| Recurso | Cuota |
|---|---|
| Lectura bruta del PNG | 1000000 B |
| Lienzo | 320×360, 8 bit |
| Memoria de trabajo del mapa | 320×360×4 B más máscaras de la banda |
| Filas de alineación | 334, 335, 336, 337 |
| Poses horizontales | x en [15, 310) |
| Combinaciones de retícula | ≤ 200 |
| Tiempo de hijo | no cualificado en este protocolo; se registrará al ejecutar |

## 4. Comandos previstos (aún no ejecutados sobre Q1/Q2)

Compilación de esta entrega (sí ejecutada; véase `evidencias/COMPILACION.txt`):

```
export RUSTC=/opt/sv-rust-1.98.0/bin/rustc
export CARGO=/opt/sv-rust-1.98.0/bin/cargo
"$CARGO" build --locked --release --manifest-path Cargo.toml
```

Cualificación, **cuando se autorice**:

```
./target/release/leyenda_contenido reconocer \
  --png RUTA_PRIVADA/R01.png \
  --fuente RUTA_PRIVADA/DejaVuSans.ttf \
  --parametros insumos/parametros.candidatos.txt
```

Esperado Q1: `CORRESPONDENCIA_CONFORME`. Esperado Q2: `DISCORDANCIA_CONTENIDO`. Cualquier otro código en Q1 o `CORRESPONDENCIA_CONFORME` en Q2 es fracaso de esa celda.

Éxito de la tanda: existe al menos una celda que cumple ambos esperados, seleccionada por el desempate, sin retocar el perfil.

Fracaso: ninguna celda conjunta, o empate residual.

Parada: no pasar a E1–E16; no ajustar umbrales tras ver Q2 para salvar Q1.

## 5. Separación Q / E

Q1 y Q2 cualifican parámetros. E1–E16 permanecen reservados. E1 sigue sin testigo material. Esta entrega no materializa evaluación.

## 6. Independencia

| Pieza | Función | Relación con el captor |
|---|---|---|
| `png` 0.17 | Decodificar PNG | Distinto de `tiny-skia` 0.12.0. No acredita independencia. Ambos consumen PNG. |
| `fontdue` 0.9 | Rasterizar glifos | Distinto de resvg 0.48.1. Comparte el TTF. |
| TTF DejaVu contratado | Insumo | Fallo común con resvg. |
| resvg 0.48.1 | Fuera de este comprobador | Productor histórico. |

## 7. Decisiones pendientes que bloquean partes del comportamiento

Véase `DECISIONES_PENDIENTES.md`. El código compilable no las cierra.
