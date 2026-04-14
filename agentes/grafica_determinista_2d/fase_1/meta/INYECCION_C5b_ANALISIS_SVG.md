# INYECCION_C5b_ANALISIS_SVG

## Objeto
Analizador estructural de SVG de entrada. Solo detecta y propone. Nunca ejecuta.

## Principio soberano
El soberano es el humano. El agente detecta, mide y presenta opciones acotadas.
Ninguna opción se aplica sin confirmación humana explícita.
Esta inyección no ejecuta ninguna corrección bajo ninguna circunstancia.

## Lo que hace
Cuando el usuario sube un archivo SVG en modo `corregir`:
1. Parsea el SVG (DOMParser — no modifica el original)
2. Detecta problemas en las regiones de `draft.modify`
3. Para cada problema calcula tres opciones concretas con sus parámetros exactos
4. Muestra las propuestas en el panel de auditoría
5. Incluye `correction_proposals.json` en el bundle

## Las tres opciones para footer con overflow horizontal
- **O1** Reducir font-size: calcula el valor exacto necesario. Avisa si queda por debajo del mínimo legible (7px).
- **O2** Dividir en dos líneas: calcula el punto de corte en límite de palabra más próximo a la mitad.
- **O3** Reformular el texto: calcula el máximo de caracteres permitidos. **El agente no puede ejecutar esta opción** — requiere decisión humana sobre el contenido.

## Límite declarado
> Si la corrección necesaria no está entre estas tres opciones,
> el AE-GD2-SV en Fase 1 no puede llevarla a cabo.

## Factor heurístico declarado
`C5B_CHAR_FACTOR = 0.55` (char_width ≈ 0.55 × font-size, sans-serif)
No es medida exacta. P25 (Reproducibilidad laboratorial) permanece en U.

## Salidas añadidas al bundle
- `01_informe_usuario/correction_proposals.json` — propuestas estructuradas con el
  campo `"invariante": "Ninguna propuesta ha sido ejecutada. El soberano decide."`

## Archivos afectados
- `web/public/app.js` — función `analyzeSvg()` + integración en `run()`

## Para archivos PNG/JPG
El AVISO_ALCANCE de C5a sigue activo. C5b solo opera sobre SVG.
