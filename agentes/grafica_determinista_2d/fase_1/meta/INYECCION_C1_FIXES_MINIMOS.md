# INYECCIÓN C1 — FIXES MÍNIMOS DE ESTABILIZACIÓN

## Alcance

Parche quirúrgico y mínimo sobre la fase_1 del AE-GD2-SV para resolver incidencias puntuales detectadas en pruebas locales y alinear el carril web con el carril Python.

## Correcciones incluidas

1. `python/ae_gd2_sv/report.py`
   - `DictWriter(..., extrasaction='ignore')`
   - gradiente por diferencia finita consistente
   - `max_iter = len(QUALITY_PARAM_IDS)`
   - `events_flat.csv` exporta también `affected_params`

2. `web/public/app.js`
   - gradiente alineado con Python
   - iteración factual web alineada con el tamaño real del conjunto de calidad

3. `web/public/index.html`
   - rotulación actualizada de la inyección vigente
   - aviso explícito: en modo `corregir` se requiere archivo local

## Delimitación

Esta inyección no añade doctrina ni cambia la arquitectura del agente. Cierra únicamente fallos de implementación puntuales y deja la fase lista para reejecución material de pruebas.
