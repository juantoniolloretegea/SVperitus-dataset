# Contrato candidato LEYENDA-CONTENIDO/3

**Estado:** candidato. No implementa el comprobador. No autoriza campañas, rasterizaciones, síntesis de plantillas ni selección de umbrales por ensayo.

**Perfil de artefacto (heredado, no modificado):** `SV-PNG16-LEYENDA/1` — PNG 320×360, 8 bit, fondo blanco, resvg 0.48.1, DejaVu Sans `ae7b7855e115a5966d8b1b3f80f254ccc117ec86f9965e202ee2940453837280`, fixture histórico de dieciséis vértices. No es un reconocedor general de texto.

**Cortes de lectura:** Lenguaje de partida `e9e4a359bd3d54e2e397c4747f11b7c69d6fbb2f`; seguimiento consultado `5e6edf78d8714bbbd57253991e48ba993e79e7a8` (Acta 002); laboratorio `86441ad4d375e31737dfcead0b1fd9cd52161883`. Depósito antecedente: `SVperitus-dataset@18e7178e6ec7efbb10863f4d081422f94ef163c2`.

La identidad de bytes y la corrección del contenido visible son propiedades distintas. Este texto corrige los reparos LC2-01, LC2-02 y LC2-03 del Acta 002. No describe como observado ningún comportamiento no ensayado.

## A. Propiedad y frontera

**Propiedad.** En la banda B=[15,310)×[318,344) del PNG recibido deben observarse, de izquierda a derecha, exactamente las parejas 0↔1, 1↔2 y U↔3, unidas por los dos separadores visibles del convenio, y sin adición inadmisible de tinta según la sección B.

El convenio procede de `CONTRATO_SVG_CONSUMO.md`. La cadena de leyenda del fixture incluye el carácter separador entre cláusulas; exigir ese separador no altera el perfil: elimina la disyuntiva posterior «plantilla o hueco».

**Códigos (no son Tri), con precedencia estricta:**

1. `FALLO_LECTURA` — no hay bytes, error de E/S, o longitud bruta mayor que 1 000 000 B. Se decide antes de inspeccionar la firma.
2. `FUERA_DE_PERFIL` (formato) — firma distinta de PNG, IHDR ausente o inválido, lienzo distinto de 320×360 o profundidad distinta de 8 bit.
3. `FALLO_DECODIFICACION` — firma y cuota admisibles, pero el decodificador no reconstruye el mapa RGBA.
4. `FUERA_DE_PERFIL` (fondo) — el mapa decodificado no satisface el criterio de fondo de la sección C.4.
5. `LEYENDA_AUSENTE` — perfil válido y tinta de banda menor que n_min.
6. `LEYENDA_ILEGIBLE` — tinta suficiente, pero fallan la asociación de tres cláusulas, los separadores, un empate o una adición inadmisible.
7. `DISCORDANCIA_CONTENIDO` — tres cláusulas y dos separadores asignables, sin adición inadmisible, y al menos una pareja distinta del convenio.
8. `CORRESPONDENCIA_CONFORME` — tres cláusulas del convenio, dos separadores, y solo tolerancia de perfil en el residuo.

Ningún código se traduce a `Tri.U`.

## B. Tinta, tolerancia de perfil y adición inadmisible (LC2-01)

**Mapa de tinta.** Tras decodificar, un píxel pertenece a la tinta I si y solo si su alfa es 255 y su RGB es distinto de (255, 255, 255). M_B = I ∩ B.

**Máscaras.** Para cada plantilla aceptada T en su pose asignada:

- M_T es el conjunto de píxeles de tinta de la plantilla, sin dilatar.
- H_T es el anillo de un píxel (vecindad-4 de M_T menos M_T). Ese anillo modela el antialiasing; no es una zona donde cualquier marca quede absorbida.

**Atribución.** Cada píxel de M_B se atribuye a lo sumo a una cláusula o a un separador. Si dos plantillas aceptadas reclaman el mismo píxel de M_T, prevalece la de mayor S; si |S_a − S_b| ≤ epsilon, el resultado es `LEYENDA_ILEGIBLE`.

**Componente conexa.** En M_B se consideran componentes 4-conexas.

**Tolerancia de perfil** (variación admitida, no cualificada numéricamente):

- píxeles de M_B que caen en algún H_T y son 4-adyacentes a M_T de la misma plantilla (halo de antialiasing);
- polvo: componentes conexas de M_B menos la unión de los M_T con área estrictamente menor que a_min, siempre que el residuo total R_abs no supere r_max y R_rel no supere rho.

Esas dos clases no bastan, por sí solas, para declarar conformidad: siguen exigiendo las tres parejas y los dos separadores.

**Adición inadmisible** (obliga a no emitir `CORRESPONDENCIA_CONFORME`; el código es `LEYENDA_ILEGIBLE` si las cláusulas no pueden asignarse o si, pudiendo asignarse las del convenio, existe adición):

- cualquier componente conexa de área al menos a_min que no esté contenida en la unión de los M_T;
- cualquier marca interior al anillo H_T que forme componente propia de área al menos a_min (no 4-adyacente a M_T);
- cualquier coincidencia S ≥ theta con una plantilla del vocabulario cerrado que no sea la asignada a esa pose;
- R_rel > rho o R_abs > r_max, aunque cada componente sea menor que a_min.

Una marca alojada solo en H_T y 4-adyacente a M_T, de área inferior a a_min, no es adición: es tolerancia de perfil. Una marca exterior a la unión de M_T y H_T con área inferior a a_min y residuo total bajo umbral tampoco es adición. E2 no puede exigir rechazo de ese polvo: ese rechazo contradiría los umbrales. El caso E2 se parte en fronteras (sección F).

Los símbolos theta, epsilon, rho, r_max, a_min, n_min, s, tau_t, d_min, g_min, w_sep min, w_sep max y f_min son parámetros de cualificación, no valores validados.

## C. Algoritmo y fondo (LC2-03)

1. Lectura bruta y cuota → `FALLO_LECTURA`.
2. Firma e IHDR → `FUERA_DE_PERFIL` (formato).
3. Decodificación del mapa RGBA → `FALLO_DECODIFICACION`.
4. **Fondo, después de decodificar y antes de la leyenda.**
   - Región de fondo comprobada: F = L \ B, con L = [0,320)×[0,360), más el criterio de partición en todo L.
   - Partición de cada píxel de L:
     - fondo: alfa = 0, o alfa = 255 y RGB = (255,255,255);
     - tinta: alfa = 255 y RGB distinto de blanco;
     - resto (alfa en (0,255), o combinaciones no cubiertas): `FUERA_DE_PERFIL` (fondo).
   - Transparencia total (alfa = 0) se interpreta como fondo blanco y no entra en I.
   - Tinta semitransparente no pertenece al perfil opaco de 8 bit: `FUERA_DE_PERFIL` (fondo).
   - Marco: en la franja de 2 px del borde de L que no intersecta B, el número de píxeles de fondo debe ser al menos f_min; en caso contrario, `FUERA_DE_PERFIL` (fondo). Este umbral no está cualificado; no se afirma un recuento observado sobre R01.
5. Banda y n_min → `LEYENDA_AUSENTE`.
6. Alineación vertical de plantillas en las filas enteras 334, 335, 336 y 337. Mayor S; empate no superior a epsilon entre filas → `LEYENDA_ILEGIBLE`.
7. Localización horizontal con exclusividad y d_min; intervalos semiabiertos.
8. Separadores según la sección D.
9. Residuo y adiciones según la sección B.
10. Decisión según la precedencia de la sección A.

Si varias tuplas superan la cualificación, se elige una sola por el orden lexicográfico ya fijado en LEYENDA-CONTENIDO/2: s más próximo a 12,8 px; theta mayor; rho menor; r_max menor. Empate residual: la cualificación fracasa. No se altera el perfil para acomodar un resultado.

## D. Régimen único de separadores (LC2-02)

El convenio visible incluye el fragmento separador entre cláusulas consecutivas. El régimen es uno solo: **separador obligatorio por plantilla**. Queda derogada la alternativa «plantilla o hueco no superior a w_sep».

Condiciones geométricas, todas ellas necesarias:

1. Existen exactamente dos aceptaciones de la plantilla de separador, S ≥ theta, ordenadas por abscisa s1 < s2.
2. Tras ordenar las tres cláusulas por abscisa c1 < c2 < c3, se cumple c1 < s1 < c2 < s2 < c3.
3. La distancia horizontal entre el extremo derecho de ci y el izquierdo de si, y entre el extremo derecho de si y el izquierdo de c(i+1), es al menos g_min (no hay contacto).
4. La anchura del intervalo que contiene a si está en [w_sep min, w_sep max].

Esperados de frontera (casos especificados, no materializados):

| Situación | Código |
|---|---|
| Faltan uno o ambos separadores, con tres cláusulas asignables | `LEYENDA_ILEGIBLE` |
| El intervalo intercláusula contiene otro glifo del vocabulario o un trazo de área al menos a_min en lugar del separador | `LEYENDA_ILEGIBLE` |
| Dos cláusulas a distancia menor que g_min, con o sin tinta intermedia | `LEYENDA_ILEGIBLE` |
| Hueco blanco entre cláusulas, sin plantilla de separador aceptada | `LEYENDA_ILEGIBLE` |
| Dos separadores en pose correcta junto a las tres parejas del convenio y sin adición | `CORRESPONDENCIA_CONFORME` |

Un hueco vacío no sustituye al separador. Esa regla no modifica el texto fuente del fixture: lo hace operativo.

## E. Independencia y límites

Se conserva la tabla de LEYENDA-CONTENIDO/2. Un nombre de crate distinto no demuestra independencia. No se instala ninguna dependencia en este acto.

Quedan fuera: P1/sentido, captor integrado, paridad visual completa, batería A–L de la adenda de ciberseguridad como ejecución, Bis, S26, implementación del reconocedor y cualificación de parámetros. E1 sigue sin testigo material.

## F. Cualificación y evaluación

**Cualificación (no es aceptación del método):**

| ID | Entrada histórica | Esperado |
|---|---|---|
| Q1 | R01 `3e9fae6d4844a07d0f1281d4974c5da1c5ce01c6dbc774be27b18f1735f7509d` | `CORRESPONDENCIA_CONFORME` |
| Q2 | R06 `829286631401c3208554a9f1f81bc091fa5355201490bd92ba72f9b0bb254827` | `DISCORDANCIA_CONTENIDO` |

**Evaluación reservada.** Casos especificados; no materializados aquí, salvo Q1 y Q2 como testigos históricos de cualificación:

| ID | Descripción | Esperado |
|---|---|---|
| E1 | Segundo PNG del perfil, distinto de R01, leyenda del convenio sin adición | `CORRESPONDENCIA_CONFORME` |
| E2a | Tres parejas del convenio y trazo o glifo ajeno en B, exterior a las máscaras y anillos, área al menos a_min | `LEYENDA_ILEGIBLE` |
| E2b | Tres parejas del convenio y marca en un anillo H_T, componente propia de área al menos a_min | `LEYENDA_ILEGIBLE` |
| E2c | Tres parejas del convenio, dos separadores, y solo polvo (componentes menores que a_min, R_abs ≤ r_max, R_rel ≤ rho) | `CORRESPONDENCIA_CONFORME` |
| E2d | Tres parejas del convenio y residuo total por encima de rho o de r_max, aunque cada componente sea menor que a_min | `LEYENDA_ILEGIBLE` |
| E3 | Cuarta cláusula visible en B | `LEYENDA_ILEGIBLE` |
| E4 | Tres parejas del convenio y fragmento adicional `0: radio 2` | `LEYENDA_ILEGIBLE` |
| E5 | R02 histórico, banda inferior sin tinta de leyenda | `LEYENDA_AUSENTE` |
| E6 | Dos cláusulas solamente | `LEYENDA_ILEGIBLE` |
| E7 | Primera etiqueta fuera del vocabulario | `LEYENDA_ILEGIBLE` |
| E8 | Primera pareja alterada, tres cláusulas, dos separadores, sin adición | `DISCORDANCIA_CONTENIDO` |
| E9 | No PNG o IHDR distinto de 320×360 | `FUERA_DE_PERFIL` (formato) |
| E10 | Longitud bruta mayor que 1 000 000 B | `FALLO_LECTURA` |
| E11 | Firma PNG y cuota admisibles con IDAT irrecuperable | `FALLO_DECODIFICACION` |
| E12 | Ausencia de uno o ambos separadores | `LEYENDA_ILEGIBLE` |
| E13 | Separador sustituido por otro glifo | `LEYENDA_ILEGIBLE` |
| E14 | Contacto entre cláusulas (distancia menor que g_min) | `LEYENDA_ILEGIBLE` |
| E15 | Píxel con alfa en (0, 255) | `FUERA_DE_PERFIL` (fondo) |
| E16 | Partición fondo/tinta incumplida o marco de fondo inferior a f_min | `FUERA_DE_PERFIL` (fondo) |

E1 permanece especificado hasta existir un segundo testigo. Q1 y Q2 no son el único control de evaluación.
