# INYECCIÓN B2 — CORRECTOR FACTUAL REAL

## Alcance

Esta inyección introduce el primer corrector factual real del AE-GD2-SV. Su objetivo es que el gradiente, el jacobiano, la residualidad modal y la metrología auxiliar dejen de ser sólo métricas informativas y pasen a gobernar materialmente la corrección piloto de la fase_1.

## Entradas de esta inyección

- Corrector factual iterativo sobre los parámetros críticos de calidad (`P16`–`P20`).
- Traza de corrección con política de parada por residual no decreciente.
- Secuencia soberana enriquecida con sucesos de corrección factual.
- Refuerzo de la CLI Python y de la shell web para exponer dictamen base, dictamen corregido y dictamen global.

## Salidas esperadas

- `correction_trace` en `report.json`.
- `dictamen_base`, `dictamen_corregido`, `dictamen_global`.
- `sovereign_sequence.csv` con estados intermedios de corrección.
- ZIP técnico con el banco exportable más la traza factual.

## Delimitación

Esta inyección no cierra todavía el corrector completo del agente sobre todos los dominios geométricos posibles. Cierra el piloto factual real sobre el núcleo de calidad material y deja el carril listo para la siguiente etapa de extensión.
