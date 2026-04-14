# Agente Especializado en Gráfica Determinista 2D del Sistema Vectorial SV — Fase 1

Este directorio materializa el arranque ejecutable de la Fase 1 del AE-GD2-SV dentro de `SVperitus-dataset`.

## Alcance de esta entrega

- shell web estática con Panel interactivo SV–Usuario
- secuencia soberana `S0, S1, ..., Sn`
- cuarentena local, finita y sin espera de red
- compuerta NLP subordinada (`UserContextPacket -> GraphicIntentDraft -> GraphicIntentConfirmed`)
- generación de `C_frame^25` y `C_gob^25`
- auditoría descargable en HTML, JSON y CSV
- banco de sucesos técnico exportable (`events.jsonl`, índices y logs)
- bundle ZIP local desde la propia web
- referencia Python mínima para reproducir el mismo bundle fuera del navegador

## Estructura

- `ficha/`: cierre de diseño de Hito 1
- `contratos/`: esquemas JSON de entrada, intención, IR y auditoría
- `web/`: implementación estática para GitHub Pages
- `python/`: CLI mínima de referencia
- `laboratorio/`: casos congelados para la Fase 1
- `auditoria/`: plantillas y notas de dictamen
- `actas/`: acoplamiento hacia lenguaje y motor

## Observaciones

La autoridad del agente queda en la tríada:

1. secuencia soberana `S0..Sn`
2. polígonos visibles por suceso
3. bundle técnico `append-only`
