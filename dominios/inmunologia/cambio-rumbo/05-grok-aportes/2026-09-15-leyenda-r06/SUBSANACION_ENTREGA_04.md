# Subsanación de la entrega 04 · LEYENDA-CONTENIDO/4

**Sede:** `juantoniolloretegea/SVperitus-dataset`, rama `dominio-inmunologia`, directorio `dominios/inmunologia/cambio-rumbo/05-grok-aportes/2026-09-15-leyenda-r06/`.

**Partida:** `SVperitus-dataset@b73c2b28f6a8899b2024eb3f9dee975bc8037016`.

**Recepción leída:** Acta 002 §6, Lenguaje `4ab5c0f3b13cecaaf7eba45298d9aa5f1a709dba`.

**Estado:** depositado para auditoría. El contrato permanece candidato.

## Matriz

| Reparo | Resultado en /4 | Secciones | Fundamento | Límite |
|---|---|---|---|---|
| LC2-01 | Máscara geométrica, anillo geométrico y tinta observada son conjuntos distintos. La adyacencia a la máscara geométrica no equivale a la adyacencia a la tinta de plantilla observada. Las componentes se calculan solo sobre I_res. I_AA no entra en esas componentes. Fórmulas de S, R_abs y R_rel restituidas. E2b ya no exige un píxel de anillo no adyacente a la máscara geométrica. | §B, §F | Acta 002 §6.2, tres dificultades de /3 | Parámetros sin cualificar; E2a–E2d no materializados |
| LC2-02 | Conservado: dos separadores por plantilla, orden y distancias, hueco vacío insuficiente | §D, E12–E14 | Acta 002 §6.2 recibe /3 en alcance documental | Umbrales geométricos sin cualificar |
| LC2-03 | G, B y W se trazan por geometría, no por color. Blancura exigida solo en W. Alfa distinta de 255 = FUERA_DE_PERFIL (transparencia), después de decodificar y antes del fondo. No se interpreta alfa 0 como blanco. El perfil opaco no se amplía. | §A, §C.4–C.5, E15–E16 | Acta 002 §6.2 | Este acto no inspecciona alfa de R01; si un testigo histórico fuera semitransparente, sería incompatibilidad testigo–perfil, no un cambio de perfil |
| Autonomía | Tabla de independencia incorporada. Fórmulas y regiones en el propio texto | §B.2–B.3, §E | Acta 002 §6.2 punto 3 | — |

## Archivos nuevos autorizados

`CONTRATO_CANDIDATO_LEYENDA_CONTENIDO_4.md`, `SUBSANACION_ENTREGA_04.md`, `COTEJO_ENTREGA_04.rs`, `COTEJO_ENTREGA_04_SALIDA.txt`, `MANIFIESTO_ENTREGA_04.tsv`.

No se modifican archivos anteriores.

## Evidencia histórica referenciada, no reconstruida

| Recurso | Sede | Commit | Ruta | Huella SHA-256 |
|---|---|---|---|---|
| Contrato /3 | SVperitus-dataset | `b73c2b28…` | `…/CONTRATO_CANDIDATO_LEYENDA_CONTENIDO_3.md` | `9e9937dd11ab74c4ccab2b02f958668daa9677344bce3de5a19ac2d95e858105` |
| Subsanación 03 | SVperitus-dataset | `b73c2b28…` | `…/SUBSANACION_ENTREGA_03.md` | `88ca1bb77524fcf09842082a47db9839dd4417c7dd61a037e0aadfb276ff5e3c` |
| Cotejo identidad, fuente | SVperitus-dataset | `18e7178e…` | `…/cotejo_identidad_sha256.rs` | `6698383e5e768cf32da6b0d79f283c550810cc6c0c428f6bfc816679ec6098df` |
| Acta 002 §6 | SV-lenguaje-de-computacion | `4ab5c0f3…` | `docs/calidad/tuberias-ia/continuacion-15-09-2026/ACTA_002_…md` | no calculada en este acto |
| R01.png, R06.png | laboratorio `86441ad4…`, paquete raster | miembros citados | `3e9fae6d…` / `82928663…` | custodia privada; no se adjunta |

El cotejo receptor de /3 citado en Acta 002 §6.3 (`COTEJO_RECEPCION_LEYENDA_03.rs`) no se reconstruye aquí. Su huella se toma del acta; el fuente no se deposita de nuevo.

## Lo que este acto no resuelve

Reconocedor, cualificación, E1 material, Bis, S26, campañas y lectura de píxeles de los PNG históricos.
