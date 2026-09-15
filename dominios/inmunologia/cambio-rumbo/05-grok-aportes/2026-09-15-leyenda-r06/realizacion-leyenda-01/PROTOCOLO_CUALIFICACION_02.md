# Protocolo de cualificación 02 · realizacion-leyenda-01

Sustituye, para la tanda autorizable, la retícula abierta del protocolo depositado en `5e3c29bf`. Conserva testigos, cuotas de PNG y separación Q/E. No ejecuta Q1/Q2.

## Tanda finita

Archivo: `insumos/RETICULA_TANDA_01.tsv`. Exactamente 27 celdas. Los valores no se amplían.

## Cualificación §F

Q1 (R01 → `CORRESPONDENCIA_CONFORME`) y Q2 (R06 → `DISCORDANCIA_CONTENIDO`) son, ambas, la cualificación del método. Una celda *supera* la cualificación solo si produce ambos esperados. No se ajustan umbrales tras ver un resultado.

## Selección entre celdas que superaron (§C)

1. s más próximo a 12,8 px.
2. theta mayor.
3. rho menor.
4. r_max menor.
5. Empate residual en esas cuatro claves: la cualificación fracasa.

`n_min` no es clave de §C. Tres celdas (12,8; 0,80; n_min ∈ {20,40,80}) empatarían si las tres superaran Q1 y Q2.

No se recorre el TSV en el orden de origen para elegir ganadora. El orden de origen solo identifica la fila.

Parada: no se pasa a E1–E16. No se amplía la tanda.
