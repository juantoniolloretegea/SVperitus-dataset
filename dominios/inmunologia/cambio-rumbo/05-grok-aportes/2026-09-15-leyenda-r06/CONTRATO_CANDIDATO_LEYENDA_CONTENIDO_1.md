# Contrato candidato LEYENDA-CONTENIDO/1

**Estado:** candidato. No implementa el comprobador. No autoriza campañas, rasterizaciones ni mutantes.

**Perfil de artefacto:** `SV-PNG16-LEYENDA/1` — PNG 320×360, 8 bit, fondo blanco, resvg 0.48.1, DejaVu Sans de huella `ae7b7855e115a5966d8b1b3f80f254ccc117ec86f9965e202ee2940453837280`, leyenda del fixture histórico de dieciséis vértices. No es un reconocedor general de texto.

**Cortes de lectura**

- Lenguaje: `juantoniolloretegea/SV-lenguaje-de-computacion` · `e9e4a359bd3d54e2e397c4747f11b7c69d6fbb2f`
- Laboratorio: `juantoniolloretegea/SV-matematica-semantica-cuaternaria` · `86441ad4d375e31737dfcead0b1fd9cd52161883`

## A. Propiedad y frontera

**Propiedad.** En la banda de leyenda del PNG efectivamente recibido, las tres cláusulas visibles, de izquierda a derecha, deben ser:

`0` ↔ radio `1` · `1` ↔ radio `2` · `U` ↔ radio `3`

Ese convenio procede de `CONTRATO_SVG_CONSUMO.md`. No se deriva del hash del PNG R01 ni del texto del SVG de entrada como juez.

**Entrada.** Bytes de un PNG y el identificador de perfil. El SVG, sus metadatos y sus hashes aportan procedencia y expectativa auxiliar; el veredicto se emite sobre píxeles.

**Salidas técnicas (no son Tri):**

| Código | Significado |
|---|---|
| `CORRESPONDENCIA_CONFORME` | Las tres parejas etiqueta–radio coinciden con el convenio. |
| `DISCORDANCIA_CONTENIDO` | Perfil admisible y leyenda legible, pero al menos una pareja no es la del convenio (caso R06). |
| `LEYENDA_AUSENTE` | Banda sin tinta suficiente para tres cláusulas. |
| `LEYENDA_ILEGIBLE` | Hay tinta, pero no se localizan las tres etiquetas o un radio asociado. |
| `FUERA_DE_PERFIL` | Firma PNG, dimensiones, fondo o cuota distintos de `SV-PNG16-LEYENDA/1`. |
| `FALLO_LECTURA` | No se abre, no se decodifica o se excede la cuota (1 000 000 B). |

Ninguno de estos códigos se traduce a `Tri.U`. No se modifica el alfabeto SV. El comprobador no interpreta sentido clínico, P1 ni autoridad.

## B. Referencia independiente y algoritmo

**Nombre del método.** Reconocimiento óptico restringido y transparente de seis fragmentos literales, en la banda de leyenda del perfil. Quedan excluidos el OCR de vocabulario abierto, el OCR opaco y cualquier modelo de lenguaje como juez.

**Origen de la expectativa.** Convenio recibido: `0→radio 1`, `1→radio 2`, `U→radio 3`.

**Cadena de funciones (propuesta; no precomprometida).**

1. **Decodificación.** Abrir el PNG, comprobar firma y lienzo 320×360, extraer la banda B=[15,310)×[318,344). Tinta: alfa >0 y RGB ≠(255,255,255).
2. **Síntesis de plantillas.** Con el TTF contratado y un rasterizador de glifos distinto de resvg, producir máscaras de `0:`, `1:`, `U:`, `radio 1`, `radio 2` y `radio 3`. Tamaño tipográfico s y umbral de tinta de plantilla tau_t: parámetros de cualificación.
3. **Puntuación.** Para cada plantilla T y cada abscisa entera x admisible en B, S(T,x)=|M_T ∩ M_B(x)| / |M_T|, fracción de píxeles de tinta de T que coinciden con tinta en B alineada en x.
4. **Localización con exclusividad.** Sea theta el umbral mínimo de aceptación. Un candidato de etiqueta es un máximo local de S con S≥theta.
   - Separación: dos candidatos distan al menos d_min píxeles; si no, se conserva el de mayor S.
   - Exclusividad entre etiquetas: un mismo intervalo no adjudica dos etiquetas; prevalece la de mayor S.
   - Empate: si |S_a-S_b|≤epsilon y ambas superan theta, el resultado es `LEYENDA_ILEGIBLE`.
   - Ausencia: si una etiqueta exigida no tiene S≥theta, `LEYENDA_ILEGIBLE`, o `LEYENDA_AUSENTE` si la tinta de banda es menor que n_min.
5. **Asociación etiqueta–radio.** Ordenar etiquetas por abscisa. El intervalo del radio de la etiqueta i es (x_i+w_i, x_{i+1}) o el borde derecho de B. Se asigna a lo sumo un dígito, con las mismas reglas de exclusividad y empate.
6. **Lectura de la banda completa.** Se exige exactamente tres cláusulas; zona compatible con el separador ` | `; ningún fragmento adicional con S≥theta fuera de esas cláusulas; ninguna pareja distinta del convenio. Localizar los fragmentos esperados ignorando el resto de la banda no basta.

**Independencia por componentes.**

| Función | Componente propuesto | Relación con la campaña histórica |
|---|---|---|
| Expectativa | Tabla del convenio SVG | Independiente del PNG bajo prueba |
| Síntesis de glifos | `fontdue` 0.9.x (alternativa: `ab_glyph`) sobre el TTF contratado | Distinta de resvg 0.48.1 |
| Puntuación y asociación | Código específico de este contrato | No existe en el captor |
| Decodificación PNG | `tiny-skia` u otro decodificador | Puede coincidir con el captor: límite de independencia de códec |
| Fuente | TTF ya huellado | Compartida; es el tipo contratado |

No se instala ninguna dependencia por este documento.

## C. Hechos heredados, propuesta y parámetros

**Hechos heredados**

- Lienzo PNG 320×360, fondo blanco, resvg 0.48.1, DejaVu Sans `ae7b7855…`.
- Banda de presencia de leyenda del captor: 15≤x<310, 318≤y<344.
- Texto fuente de R01 y R06; ancla del `<text>`; `font-size` 320 000 en el `viewBox`.
- Convenio de radios y exclusión de OCR opaco o juez de modelo.

**Propuesta nueva (candidata; no se denomina precomprometida):** el reconocimiento óptico restringido, los códigos de salida, la lectura completa de la banda y la tabla de casos.

**Parámetros de cualificación (explícitos, no validados):** s, tau_t, theta, epsilon, d_min, n_min, w_sep. Candidatos de estudio para s: 12 y 13 px.

## D. Contraste previo, precedencia y casos

**Precedencia** (un solo código por entrada):

1. `FALLO_LECTURA`
2. `FUERA_DE_PERFIL`
3. `LEYENDA_AUSENTE`
4. `LEYENDA_ILEGIBLE`
5. `DISCORDANCIA_CONTENIDO`
6. `CORRESPONDENCIA_CONFORME`

| ID | Entrada | Esperado |
|---|---|---|
| L01 | PNG R01 `3e9fae6d4844a07d0f1281d4974c5da1c5ce01c6dbc774be27b18f1735f7509d` | `CORRESPONDENCIA_CONFORME` |
| L02 | PNG R06 `829286631401c3208554a9f1f81bc091fa5355201490bd92ba72f9b0bb254827` | `DISCORDANCIA_CONTENIDO` |
| L03 | PNG R02 histórico (banda inferior sin tinta de leyenda) | `LEYENDA_AUSENTE` |
| L04 | PNG especificado con solo la primera pareja alterada | `DISCORDANCIA_CONTENIDO` |
| L05 | PNG especificado con la primera etiqueta fuera del conjunto | `LEYENDA_ILEGIBLE` |
| L06 | PNG especificado con dos cláusulas solamente | `LEYENDA_ILEGIBLE` |
| L07a | No PNG o IHDR distinto de 320×360 | `FUERA_DE_PERFIL` |
| L07b | Flujo ilegible o longitud > 1 000 000 B | `FALLO_LECTURA` |

L03–L07 quedan especificados, no materializados. R03 y R04 no pertenecen a este contrato.

## Cualificación previa y congelación

1. Cualificación únicamente sobre L01 y L02, con malla de parámetros publicada a priori.
2. Éxito: una tupla produce L01 conforme y L02 discordante, sin empate. Fracaso: ninguna tupla de la malla lo cumple. No se amplía la malla para obtener un éxito.
3. Congelación de una sola tupla si hay éxito.
4. Evaluación separada de L03–L07 con la tupla congelada. Queda prohibido modificar parámetros para salvar un caso.

## E. Dependencia, límites y testigos

Dependencia nueva propuesta: `fontdue`, semántica de versión 0.9. Función: cubrir glifos del TTF contratado. No rasteriza SVG.

Límites: P1/sentido desde píxeles, captor integrado, paridad visual completa, pruebas A–L de la adenda de ciberseguridad no ejecutadas en este acto, Bis y S26 abiertos.

**Testigos localizados** (laboratorio `86441ad4…`, paquete `EVIDENCIA_RASTER_CAPTOR.tar.gz`):

| Testigo | Miembro o ruta | SHA-256 |
|---|---|---|
| Paquete | `…/EVIDENCIA_RASTER_CAPTOR.tar.gz` | `2af2487c24c08cd1f73addc74a6c2bceaffbabfa69b0123289915b02a2ce29b3` |
| R01 / muestra PNG | `evidencia/resultado/R01.png` | `3e9fae6d4844a07d0f1281d4974c5da1c5ce01c6dbc774be27b18f1735f7509d` |
| Entrada / muestra SVG | `evidencia/resultado/entrada.svg` | `e5a9f9bc6df9b4f59a2a0cb908046239fda11ebbc247577b8e8c32b268a8c578` |
| R06 PNG | `evidencia/resultado/R06.png` | `829286631401c3208554a9f1f81bc091fa5355201490bd92ba72f9b0bb254827` |
| R06 SVG | `evidencia/resultado/R06.svg` | `6dec0798aece0d08be42701fd0856f3c92cc2ba5dc5b2250490f46ce8c5f87a3` |

R06.png y R06.svg no figuran en `IDENTIDADES.txt`. El cotejo Rust de estas huellas está en `COTEJO_IDENTIDAD_SALIDA.txt`.
