# INYECCION_C2_FILE_MODE_Y_METRICAS

## Objeto
Parche mínimo C2 del AE-GD2-SV Fase I.

## Alcance
1. Sustituir la carga de `app.js` como módulo por carga clásica para permitir ejecución local bajo `file://`.
2. Poblar las salidas visibles ya declaradas en el HTML: `diffMetrics`, `modalMetrics`, `metroMetrics` y `sovereignJson`.

## Delimitación negativa
Este parche no reabre diseño, no altera contratos, no modifica la célula, no toca la lógica custodial ni el corrector factual más allá de exponer en la interfaz métricas ya calculadas.

## Archivos afectados
- `web/public/index.html`
- `web/public/app.js`
