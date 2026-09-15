# Contrato candidato LEYENDA-CONTENIDO/2

**Estado:** candidato. No implementa el comprobador. No autoriza campañas, rasterizaciones, síntesis de plantillas ni selección de umbrales por ensayo.

**Perfil de artefacto (heredado, no modificado):** `SV-PNG16-LEYENDA/1` — PNG 320×360, 8 bit, fondo blanco, resvg 0.48.1, DejaVu Sans `ae7b7855e115a5966d8b1b3f80f254ccc117ec86f9965e202ee2940453837280`. No es un reconocedor general.

**Cortes de lectura:** Lenguaje `e9e4a359bd3d54e2e397c4747f11b7c69d6fbb2f`; laboratorio `86441ad4d375e31737dfcead0b1fd9cd52161883`.

La identidad de bytes (cotejo SHA-256) y la corrección del contenido visible son propiedades distintas. Un PNG cuya huella coincida con R01 no demuestra, por ese solo hecho, que un reconocedor lea la leyenda.

## A. Propiedad y frontera

**Propiedad.** En la banda B=[15,310)×[318,344) del PNG recibido deben observarse, de izquierda a derecha, exactamente las parejas 0↔1, 1↔2, U↔3, sin tinta residual atribuible a otro vocabulario del perfil.

**Códigos (no son Tri):**

| Código | Ámbito |
|---|---|
| `FALLO_LECTURA` | No hay bytes, error de E/S, o longitud bruta > 1 000 000 B. Se decide antes de inspeccionar la firma. |
| `FUERA_DE_PERFIL` | Firma distinta de PNG, IHDR ausente o inválido, lienzo distinto de 320×360, profundidad distinta de 8 bit, o fondo incompatible con blanco #ffffff. |
| `FALLO_DECODIFICACION` | Firma y cuota admisibles, pero el decodificador no reconstruye el mapa de píxeles. |
| `LEYENDA_AUSENTE` | Perfil válido y tinta de banda menor que n_min. |
| `LEYENDA_ILEGIBLE` | Tinta suficiente, pero no hay exactamente tres cláusulas asociables, hay empate, separador incumplido o residuo no explicado. |
| `DISCORDANCIA_CONTENIDO` | Tres cláusulas legibles, residuo bajo el umbral, y al menos una pareja distinta del convenio. |
| `CORRESPONDENCIA_CONFORME` | Tres cláusulas, separadores, parejas del convenio y residuo no superior al umbral. |

Ningún código se traduce a `Tri.U`.

## B. Medida conjunta: coincidencia y residuo

La razón S(T,x)=|M_T ∩ M_B(x)| / |M_T| solo mide cobertura de la plantilla. No cuenta tinta ajena. Se añade:

- M_B: píxeles de tinta en B (alfa > 0 y RGB distinto de (255,255,255)).
- M_expl: unión, sin doble atribución, de los píxeles de las plantillas aceptadas en sus abscisas y cotas verticales asignadas, dilatados 1 px en ambas direcciones para antialiasing.
- Residuo absoluto R_abs = |M_B \ M_expl|.
- Residuo relativo R_rel = R_abs / max(|M_B|, 1).

Reglas:

1. Un píxel de M_B se atribuye a lo sumo a una cláusula.
2. Superposición de dos plantillas aceptadas sobre el mismo píxel: se atribuye a la de mayor S; si el empate no supera epsilon, `LEYENDA_ILEGIBLE`.
3. Tinta que no alcanza theta con ninguna plantilla del vocabulario cerrado {0:, 1:, U:, radio 1, radio 2, radio 3, separador} cuenta como residuo.
4. Si R_rel > rho o R_abs > r_max, el resultado no puede ser `CORRESPONDENCIA_CONFORME`. Si las tres parejas son las del convenio, el código es `LEYENDA_ILEGIBLE` (contenido supernumerario). Si el residuo impide asignar tres cláusulas, `LEYENDA_ILEGIBLE`. `DISCORDANCIA_CONTENIDO` exige tres cláusulas asignables y residuo bajo umbral con al menos una pareja falsa.
5. Marcas ajenas al vocabulario (puntos, trazos, glifos de otro juego) son residuo, no texto ignorado.

Los símbolos theta, epsilon, rho, r_max, n_min, s, tau_t, d_min y w_sep son parámetros de cualificación, no valores validados.

## C. Algoritmo determinista

1. Lectura bruta y cuota → posible `FALLO_LECTURA`.
2. Firma e IHDR → posible `FUERA_DE_PERFIL`.
3. Decodificación del mapa → posible `FALLO_DECODIFICACION`.
4. Banda y n_min → posible `LEYENDA_AUSENTE`.
5. Alineación vertical: para cada plantilla se evalúa S en las filas enteras 334, 335, 336 y 337 (el ancla del elemento text proyecta 336). Se toma la fila de mayor S. Empate no superior a epsilon entre filas distintas → `LEYENDA_ILEGIBLE`.
6. Localización horizontal con exclusividad y d_min; intervalos semiabiertos [x_i + w_i, x_{i+1}).
7. Separador entre cláusulas consecutivas: plantilla del separador con S ≥ theta, o hueco de tinta no superior a w_sep sin vocabulario extra.
8. Residuo según B.
9. Decisión según la precedencia de A.

Si varias tuplas de parámetros superan la cualificación, se elige una sola por orden lexicográfico fijado a priori: s más próximo a 12,8 px; en empate, theta mayor; en empate, rho menor; en empate, r_max menor. Si dos tuplas permanecen indistinguibles, la cualificación fracasa y no se congela ninguna. No se altera el perfil para acomodar un resultado.

## D. Cualificación y evaluación, conjuntos disjuntos

**Cualificación (solo ajuste de parámetros; no es aceptación del método):**

| ID | Entrada histórica | Esperado |
|---|---|---|
| Q1 | R01 `3e9fae6d…` | `CORRESPONDENCIA_CONFORME` |
| Q2 | R06 `82928663…` | `DISCORDANCIA_CONTENIDO` |

**Evaluación reservada (no se usa para elegir umbrales).** Casos especificados, no materializados en este acto:

| ID | Descripción | Esperado |
|---|---|---|
| E1 | Segundo PNG del mismo perfil, distinto de R01, con leyenda del convenio y sin residuo extra | `CORRESPONDENCIA_CONFORME` |
| E2 | PNG de perfil correcto con las tres parejas del convenio y un trazo o glifo ajeno en B | `LEYENDA_ILEGIBLE` |
| E3 | Cuarta cláusula visible en B además de las tres del convenio | `LEYENDA_ILEGIBLE` |
| E4 | Tres parejas del convenio y, a la vez, un fragmento `0: radio 2` adicional | `LEYENDA_ILEGIBLE` |
| E5 | R02 histórico (banda inferior sin tinta de leyenda) | `LEYENDA_AUSENTE` |
| E6 | Dos cláusulas solamente | `LEYENDA_ILEGIBLE` |
| E7 | Primera etiqueta fuera del vocabulario | `LEYENDA_ILEGIBLE` |
| E8 | Primera pareja alterada, tres cláusulas, residuo bajo umbral | `DISCORDANCIA_CONTENIDO` |
| E9 | No PNG o IHDR distinto de 320×360 | `FUERA_DE_PERFIL` |
| E10 | Longitud bruta > 1 000 000 B | `FALLO_LECTURA` |
| E11 | Firma PNG y cuota admisibles con IDAT irrecuperable | `FALLO_DECODIFICACION` |

Q1 y Q2 no se reutilizan como único control de evaluación. E1 permanece especificado hasta existir un segundo testigo independiente; su ausencia es una limitación, no un permiso para reutilizar Q1 como evaluación.

## E. Independencia y límites

| Componente | Papel | Riesgo de fallo común |
|---|---|---|
| Convenio SVG | Expectativa | Ninguno respecto del PNG bajo prueba |
| TTF DejaVu contratado | Insumo de plantillas | Defecto del TTF afecta a resvg y al rasterizador de glifos |
| Rasterizador de glifos distinto de resvg (`fontdue` 0.9 u `ab_glyph`) | Síntesis de plantillas | Independencia funcional respecto de la composición SVG; no independencia respecto del TTF |
| Decodificador PNG (`tiny-skia` u otro) | Lectura de píxeles | Si coincide con el captor, un error de códec es fallo común |
| resvg 0.48.1 | Fuera del comprobador | No es oráculo de esta propiedad |

Un nombre de crate distinto no demuestra independencia. No se instala ninguna dependencia en este acto.

Quedan fuera: P1/sentido, captor integrado, paridad visual completa, A–L de la adenda de ciberseguridad como batería ejecutada, Bis y S26.
