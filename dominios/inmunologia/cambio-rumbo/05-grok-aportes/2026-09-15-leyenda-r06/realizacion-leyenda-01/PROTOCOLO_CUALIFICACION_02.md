# Protocolo de cualificación 02 · realizacion-leyenda-01

Sustituye, para la tanda autorizable, la retícula abierta del protocolo depositado en `5e3c29bf`. Conserva testigos, cuotas de PNG y separación Q/E. No ejecuta Q1/Q2.

## Tanda finita

Archivo: `insumos/RETICULA_TANDA_01.tsv`. Exactamente 27 celdas. Orden: `s_px` ascendente, luego `theta` ascendente, luego `n_min` ascendente. Los demás parámetros permanecen fijos en la fila.

No se autoriza ampliar la tanda ni recorrer el producto cartesiano de 39 366 celdas.

## Aceptación, desempate y parada

- Éxito de una celda: Q1 → `CORRESPONDENCIA_CONFORME` y Q2 → `DISCORDANCIA_CONTENIDO`.
- Éxito de la tanda: la primera celda, en el orden del TSV, que cumpla ambos esperados.
- Desempate residual si varias celdas posteriores también cumplen: no se consideran; rige la primera.
- Fracaso: ninguna de las 27 celdas cumple el par de esperados.
- Parada: al primer éxito o al agotar las 27. No se pasa a E1–E16. No se ajustan umbrales tras ver Q2.

## Decisiones de implementación (no amplían el perfil)

1. Separador: U+007C, carácter presente en `MUESTRA_SVG_PRODUCIDA.svg` @ `e9e4a359…`.
2. Anclaje vertical: `y_base` es la fila de alineación (334–337) interpretada como línea base de fontdue. Convención de implementación.
3. TTF: únicamente el archivo de 759 720 B y huella `ae7b7855…`. La huella se calcula sobre los bytes leídos.
4. Paso espacial B.6.2: `paso_x` de la celda, filas 334–337.
5. Atribución: píxel en dos máscaras aceptadas → mayor `S`; si `|Sa−Sb|≤epsilon` → `LEYENDA_ILEGIBLE`.
