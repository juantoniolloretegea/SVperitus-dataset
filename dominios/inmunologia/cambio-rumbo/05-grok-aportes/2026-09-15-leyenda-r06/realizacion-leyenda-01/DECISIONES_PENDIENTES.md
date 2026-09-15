# Decisiones pendientes · realizacion-leyenda-01

Identificadas para poder implementar sin cerrarlas en silencio.

| Pasaje | Hecho | Decisión necesaria |
|---|---|---|
| Contrato §B.1 vocabulario «separador» | El SVG histórico (`MUESTRA_SVG_PRODUCIDA.svg` @ `e9e4a359…`) escribe `0: radio 1 \| 1: radio 2 \| U: radio 3`. | Confirmar que la plantilla de separador es U+007C. El prototipo adopta esa lectura como **candidata**. |
| Contrato §C.7 filas 334–337 | No fija la convención de y de fontdue (baseline frente a caja). | Definir el anclaje vertical exacto del rasterizador de glifos. |
| Contrato §B.4 empate | Requiere comparar S de dos plantillas que comparten un píxel. | Conservar S junto a cada máscara aceptada. El prototipo trata todo solapamiento de aceptadas como `LEYENDA_ILEGIBLE`. |
| TTF contratado 759 720 B, huella `ae7b7855…` | La distribución pública 2.37 midió 757 076 B y otra huella. | Localizar el archivo exacto de custodia. No se adjunta un TTF distinto. |
| Independencia de códec | `png` ≠ `tiny-skia` | Ensayo de fallo común (misma corrupción PNG) pendiente. No se declara independencia. |
| Búsqueda exhaustiva B.6.2 | Recorre x×filas×vocabulario residual | Acotar el paso espacial si el tiempo de hijo se cualifica. |

Las partes independientes ya entregadas: lectura y cuota, IHDR, opacidad, fondo W, regiones, fórmulas de S/residuo, precedencia, CLI sin valores implícitos.
