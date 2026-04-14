# INYECCION_C5b_ANALISIS_SVG

## Objeto
Analizador estructural de SVG de entrada. Solo detecta y propone. Nunca ejecuta.

## Principio soberano
El soberano es el humano. El agente detecta, mide y presenta opciones acotadas.
Ninguna opción se aplica sin confirmación humana explícita.
Esta inyección no ejecuta ninguna corrección bajo ninguna circunstancia.

## Declaración de separación de canales — situación de Fase 1

El sistema opera con dos canales distintos que coexisten en Fase 1 sin estar conectados:

**Canal 1 — intención en lenguaje natural:**
El campo "Contexto en lenguaje natural" + "Restricciones duras" alimentan a `parseIntent`,
que evalúa la coherencia de la intención sobre el dominio gráfico-semántico de la figura.
Este canal opera sobre el SIGNIFICADO de la corrección solicitada.

**Canal 2 — análisis estructural del artefacto SVG (C5b):**
Cuando el archivo de entrada es un SVG, `analyzeSvg` detecta problemas técnicos
en la geometría del artefacto (overflow de texto, márgenes insuficientes) y ofrece
tres opciones acotadas para resolverlos. Este canal opera sobre la ESTRUCTURA TÉCNICA
del fichero SVG, no sobre la intención semántica del usuario.

**Separación deliberada:**
Los dos canales actúan sobre objetos distintos y no se alimentan mutuamente en Fase 1.
La conexión entre ellos (ejecutar la opción estructural elegida sobre el artefacto real,
verificarla contra el contrato de intención) es arquitectura de Fase 2, ya diseñada en
`diseno_c4/05_capas_no_destructivas/` y `diseno_c4/07_acoplamiento_herramienta/`.

Esta separación no viola el SV porque ambos canales son honestos sobre su alcance:
el Canal 1 produce un informe de intención; el Canal 2 produce propuestas estructurales.
Ninguno de los dos produce una imagen corregida — eso es Fase 2.

**Lo que el corrector hace**
- Detecta overflow horizontal: `text.length × C5B_CHAR_FACTOR × font-size > viewBox_width`
- Calcula opciones O1 (reducir font-size), O2 (dividir línea), O3 (reformular — solo humano)
- Produce `correction_proposals.json` en el bundle y accordion visible en el panel
- NO modifica el SVG de entrada bajo ninguna circunstancia

**Lo que el corrector NO hace**
- No modifica el contenido del texto (solo atributos estructurales)
- No ejecuta ninguna de las opciones propuestas
- No conecta con el canal de intención libre
- No produce imagen corregida

## Factor heurístico declarado
`C5B_CHAR_FACTOR = 0.55` (estimación sans-serif). P25=U (Reproducibilidad laboratorial).

## Límite declarado
Si la corrección necesaria no está entre las tres opciones propuestas,
el AE-GD2-SV en Fase 1 no puede llevarla a cabo.

## Archivos afectados
- `web/public/app.js` — función `analyzeSvg()` + integración en `run()`
