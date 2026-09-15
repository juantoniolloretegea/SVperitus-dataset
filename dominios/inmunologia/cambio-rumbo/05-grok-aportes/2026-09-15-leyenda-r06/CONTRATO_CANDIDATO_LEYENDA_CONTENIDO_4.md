# Contrato candidato LEYENDA-CONTENIDO/4

**Estado:** candidato. No implementa el comprobador. No autoriza campañas, rasterizaciones, síntesis de plantillas ni selección de umbrales por ensayo.

**Perfil de artefacto (heredado, no modificado):** `SV-PNG16-LEYENDA/1` — PNG 320×360, profundidad de 8 bit por muestra, fondo blanco opaco, resvg 0.48.1, DejaVu Sans `ae7b7855e115a5966d8b1b3f80f254ccc117ec86f9965e202ee2940453837280`, fixture histórico de dieciséis vértices. No es un reconocedor general de texto. Este acto no altera el perfil. Si un testigo histórico resultara incompatible con la opacidad aquí exigida, esa incompatibilidad se declararía; no se ampliaría el perfil.

**Cortes de lectura:** Lenguaje de partida `e9e4a359bd3d54e2e397c4747f11b7c69d6fbb2f`; recepción de /3 en Acta 002 §6, corte `4ab5c0f3b13cecaaf7eba45298d9aa5f1a709dba`; laboratorio `86441ad4d375e31737dfcead0b1fd9cd52161883`. Depósito de partida: `SVperitus-dataset@b73c2b28f6a8899b2024eb3f9dee975bc8037016`.

La identidad de bytes y la corrección del contenido visible son propiedades distintas. Este texto corrige LC2-01 y LC2-03, incorpora de forma autónoma la tabla de independencia y conserva la solución documental de LC2-02. No describe como observado ningún comportamiento no ensayado.

## A. Propiedad, regiones y códigos

**Regiones geométricas.** Se definen sobre el lienzo discreto L=[0,320)×[0,360) y no dependen del color observado:

| Símbolo | Definición | Papel |
|---|---|---|
| G=[0,320)×[0,318) | Franja superior | Dibujo autorizado de la figura de dieciséis vértices |
| B=[15,310)×[318,344) | Banda de leyenda | Dibujo autorizado de la leyenda |
| W=L\\(G ∪ B) | Resto del lienzo | Fondo exigido blanco y opaco |

W=[0,320)×[344,360) ∪ [0,15)×[318,344) ∪ [310,320)×[318,344).

**Propiedad.** En B deben observarse, de izquierda a derecha, exactamente las parejas 0↔1, 1↔2 y U↔3, unidas por los dos separadores visibles del convenio, sin adición inadmisible según la sección B. En W no debe haber tinta. El convenio procede de `CONTRATO_SVG_CONSUMO.md`. La cadena histórica de leyenda incluye el carácter separador; exigir ese separador no altera el perfil.

**Códigos (no son Tri), precedencia estricta:**

1. `FALLO_LECTURA` — no hay bytes, error de E/S, o longitud bruta mayor que 1 000 000 B. Antes de la firma.
2. `FUERA_DE_PERFIL` (formato) — firma distinta de PNG, IHDR ausente o inválido, lienzo distinto de 320×360, o profundidad distinta de 8 bit por muestra de color.
3. `FALLO_DECODIFICACION` — firma y cuota admisibles, pero el decodificador no reconstruye el mapa de muestras.
4. `FUERA_DE_PERFIL` (transparencia) — el mapa reconstruido contiene alguna muestra de alfa distinta de 255. El perfil heredado es opaco; la profundidad de 8 bit no implica por sí sola opacidad. La transparencia total no se interpreta como blanco.
5. `FUERA_DE_PERFIL` (fondo) — algún píxel de W no es RGB (255,255,255).
6. `LEYENDA_AUSENTE` — perfil válido y |M_B| < n_min.
7. `LEYENDA_ILEGIBLE` — tinta suficiente en B, pero fallan la asociación de tres cláusulas, los separadores, un empate o una adición inadmisible.
8. `DISCORDANCIA_CONTENIDO` — tres cláusulas y dos separadores asignables, sin adición inadmisible, y al menos una pareja distinta del convenio.
9. `CORRESPONDENCIA_CONFORME` — tres cláusulas del convenio, dos separadores y solo tolerancia de perfil en el residuo.

Ningún código se traduce a `Tri.U`.

## B. Máscaras, coincidencia, residuo y adición (LC2-01)

### B.1. Tinta observada y máscaras geométricas

Tras decodificar un mapa opaco, la tinta observada I es el conjunto de píxeles de L con RGB distinto de (255,255,255). M_B = I ∩ B.

Cada plantilla T del vocabulario cerrado {0:, 1:, U:, radio 1, radio 2, radio 3, separador} se sintetiza en una pose x. Su máscara geométrica M_T^geom(x) es el conjunto de píxeles donde esa síntesis deposita tinta, con independencia de I.

El anillo geométrico H_T(x) es la vecindad-4 de esa máscara, sin ella. Por construcción, todo píxel de H_T(x) es 4-adyacente a M_T^geom(x). Esa adyacencia es geométrica y no afirma que el píxel sea tinta observada ni que pertenezca a la plantilla aceptada.

La tinta de plantilla observada en esa pose es I ∩ M_T^geom(x). Un píxel p es 4-adyacente a tinta de plantilla observada si y solo si p pertenece a la vecindad-4 de I ∩ M_T^geom(x). Esta relación no equivale a p ∈ H_T(x).

### B.2. Coincidencia

S(T,x) = |M_T^geom(x) ∩ I| / max(|M_T^geom(x)|, 1).

El numerador cuenta cobertura de la plantilla por tinta observada. No cuenta tinta ajena. S no decide por sí sola la conformidad.

### B.3. Conjuntos de explicación y residuo

Sean T_1,…,T_k las plantillas aceptadas (tres cláusulas y dos separadores) en sus poses asignadas. M_expl es la unión de sus máscaras geométricas. H_expl es la unión de sus anillos geométricos.

Antialiasing admitido I_AA: tinta observada en B ∩ H_expl que es 4-adyacente a I ∩ M_expl.

Residuo I_res = M_B \ (M_expl ∪ I_AA).
R_abs = |I_res|. R_rel = R_abs / max(|M_B|, 1).

Las componentes conexas se calculan exclusivamente sobre I_res, con conectividad-4. No se calculan sobre M_B ni sobre I_AA. Una componente de tinta de plantilla que toque un píxel de anillo no se clasifica como residuo: ese píxel, si es 4-adyacente a I ∩ M_expl, pertenece a I_AA; si no lo es, pertenece a I_res y se evalúa aparte.

### B.4. Atribución y empates

Cada píxel de M_expl se atribuye a lo sumo a una plantilla aceptada. Si dos plantillas aceptadas contienen el mismo píxel, prevalece la de mayor S; si |S_a − S_b| ≤ epsilon, el resultado es `LEYENDA_ILEGIBLE`.

### B.5. Tolerancia de perfil

Admitida, y no cualificada numéricamente: todo píxel de I_AA; cada componente de I_res con área estrictamente menor que a_min, siempre que R_abs ≤ r_max y R_rel ≤ rho. La tolerancia no basta para emitir `CORRESPONDENCIA_CONFORME`: siguen exigiendo las tres parejas y los dos separadores.

### B.6. Adición inadmisible

Obliga a no emitir `CORRESPONDENCIA_CONFORME`. Si las tres cláusulas del convenio son asignables, el código es `LEYENDA_ILEGIBLE`.

1. Alguna componente de I_res tiene área al menos a_min.
2. Alguna plantilla del vocabulario no asignada alcanza S ≥ theta en B.
3. R_rel > rho o R_abs > r_max.

Fronteras de E2 (especificadas; no materializadas):

| Caso | Condición sobre I_res | Esperado |
|---|---|---|
| E2a | Existe componente de área ≥ a_min contenida en B \ (M_expl ∪ H_expl) | `LEYENDA_ILEGIBLE` |
| E2b | Existe componente de área ≥ a_min que intersecta H_expl (marca en el anillo geométrico que no es I_AA) | `LEYENDA_ILEGIBLE` |
| E2c | No hay componente de área ≥ a_min, R_abs ≤ r_max, R_rel ≤ rho, tres parejas y dos separadores | `CORRESPONDENCIA_CONFORME` |
| E2d | R_rel > rho o R_abs > r_max, aunque cada componente sea menor que a_min | `LEYENDA_ILEGIBLE` |

E2b no exige un píxel de H_T que no sea 4-adyacente a M_T^geom: esa exigencia es vacía. Exige tinta residual en el anillo que no es 4-adyacente a la tinta de plantilla observada.

theta, epsilon, rho, r_max, a_min, n_min, s, tau_t, d_min, g_min, w_sep min y w_sep max son parámetros de cualificación, no valores validados.

## C. Algoritmo y fondo (LC2-03)

1. Lectura bruta y cuota → `FALLO_LECTURA`.
2. Firma e IHDR → `FUERA_DE_PERFIL` (formato).
3. Decodificación → `FALLO_DECODIFICACION`.
4. Transparencia: si existe muestra de alfa distinta de 255 → `FUERA_DE_PERFIL` (transparencia). El perfil es opaco; no se admite alfa 0 como blanco.
5. Fondo: si algún píxel de W no es RGB (255,255,255) → `FUERA_DE_PERFIL` (fondo). La blancura se exige en W, definida geométricamente. En G y en B se admite tinta; no se usa el color observado para trazar esas fronteras.
6. |M_B| < n_min → `LEYENDA_AUSENTE`.
7. Alineación vertical en las filas 334, 335, 336 y 337. Mayor S; empate ≤ epsilon entre filas → `LEYENDA_ILEGIBLE`.
8. Localización horizontal con exclusividad y d_min.
9. Separadores según la sección D.
10. Residuo y adiciones según la sección B.
11. Decisión según la sección A.

Si varias tuplas superan la cualificación, se elige una sola: s más próximo a 12,8 px; theta mayor; rho menor; r_max menor. Empate residual: la cualificación fracasa. No se altera el perfil para acomodar un resultado.

## D. Régimen único de separadores (LC2-02, conservado)

El convenio visible incluye el fragmento separador entre cláusulas consecutivas. El régimen es uno solo: separador obligatorio por plantilla. Queda derogada la alternativa «plantilla o hueco».

Condiciones, todas necesarias:

1. Exactamente dos aceptaciones de la plantilla de separador, S ≥ theta, s1 < s2.
2. Cláusulas c1 < c2 < c3 y orden c1 < s1 < c2 < s2 < c3.
3. Distancia horizontal entre ci y si, y entre si y c(i+1), al menos g_min.
4. Anchura del intervalo de si en [w_sep min, w_sep max].

| Situación | Código |
|---|---|
| Faltan uno o ambos separadores, con tres cláusulas asignables | `LEYENDA_ILEGIBLE` |
| El intervalo intercláusula contiene otro glifo o un trazo residual de área al menos a_min | `LEYENDA_ILEGIBLE` |
| Distancia entre cláusulas menor que g_min | `LEYENDA_ILEGIBLE` |
| Hueco blanco sin plantilla de separador aceptada | `LEYENDA_ILEGIBLE` |
| Dos separadores correctos, tres parejas del convenio, sin adición | `CORRESPONDENCIA_CONFORME` |

Un hueco vacío no sustituye al separador.

## E. Independencia y límites

| Componente | Papel | Riesgo de fallo común |
|---|---|---|
| Convenio SVG | Expectativa | Ninguno respecto del PNG bajo prueba |
| TTF DejaVu contratado | Insumo de plantillas | Un defecto del TTF afecta a resvg y al rasterizador de glifos |
| Rasterizador de glifos distinto de resvg (fontdue 0.9 u ab_glyph) | Síntesis de plantillas | Independencia funcional respecto de la composición SVG; no independencia respecto del TTF |
| Decodificador PNG (tiny-skia u otro) | Lectura de píxeles | Si coincide con el captor, un error de códec es fallo común |
| resvg 0.48.1 | Fuera del comprobador | No es oráculo de esta propiedad |

Un nombre de crate distinto no demuestra independencia. No se instala ninguna dependencia en este acto.

Quedan fuera: P1/sentido, captor integrado, paridad visual completa, batería A–L de la adenda de ciberseguridad como ejecución, Bis, S26, implementación del reconocedor y cualificación de parámetros. E1 sigue sin testigo material.

## F. Cualificación y evaluación

**Cualificación (no es aceptación del método):**

| ID | Entrada histórica | Esperado |
|---|---|---|
| Q1 | R01, laboratorio 86441ad4, miembro R01.png, SHA-256 `3e9fae6d4844a07d0f1281d4974c5da1c5ce01c6dbc774be27b18f1735f7509d` | `CORRESPONDENCIA_CONFORME` |
| Q2 | R06, mismo paquete, miembro R06.png, SHA-256 `829286631401c3208554a9f1f81bc091fa5355201490bd92ba72f9b0bb254827` | `DISCORDANCIA_CONTENIDO` |

**Evaluación reservada:**

| ID | Descripción | Esperado |
|---|---|---|
| E1 | Segundo PNG del perfil, distinto de R01, leyenda del convenio sin adición | `CORRESPONDENCIA_CONFORME` |
| E2a–E2d | Según B.6 | Según B.6 |
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
| E14 | Contacto entre cláusulas | `LEYENDA_ILEGIBLE` |
| E15 | Alguna muestra de alfa distinta de 255 | `FUERA_DE_PERFIL` (transparencia) |
| E16 | Algún píxel de W no blanco opaco | `FUERA_DE_PERFIL` (fondo) |

E1 permanece especificado hasta existir un segundo testigo. Q1 y Q2 no son el único control de evaluación. Este acto no inspecciona los píxeles de R01 ni de R06.
