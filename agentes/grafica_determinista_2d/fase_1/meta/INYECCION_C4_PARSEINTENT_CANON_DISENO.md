# INYECCION_C4_PARSEINTENT_CANON_DISENO

## Objeto
Parche C4 del AE-GD2-SV Fase I + primeros módulos de diseño de arquitectura para la transición a C5.

## Correcciones en `web/public/app.js`

### Fix 1 — parseIntent: tres bugs cerrados

**A — Conflicto pos+neg silenciado:**  
Cuando una nota positiva (`corregir footer`) coincidía con una hard rule negativa (`Mantener footer`),
el objeto iba a `preserve` sin emitir `unresolved`. Ahora emite conflicto explícito y trazable.

**B — Lista negativa distribuida:**  
La frase `"No toque el título, el cartel, el fondo ni la composición"` no protegía a `fondo` ni a
`composición` porque los regex buscaban `"no tocar X"` contiguo. Solución: la nota se divide en
zona positiva (antes del primer operador negativo) y zona negativa (el resto). Los `pos` regex solo
evalúan la zona positiva. Probado con el run real de producción.

**C — Cobertura de regex incompleta + edge case negInHard:**  
Añadidas 12 variantes: `"no toque el X"`, `"no modificar X"`, `"X original"`, `"X intacto"`,
`"preservar X"`. Corregido el edge case en `negInHard` donde `t.pos` podía activar la condición
negativa para una hard rule que solo mencionaba el objeto sin verbo negativo.

### Fix 2 — Canon de color SV oficial
Los polígonos SVG del panel usaban colores pastel divergentes del canon oficial de `comun/polygons.py`.
Unificados:
- `0 = #4CAF50` (verde)
- `U = #FFC107` (ámbar)
- `1 = #F44336` (rojo)

Se añade leyenda mínima visible bajo los polígonos.

### Fix 3 — events_flat.csv con affected_params en bundle web
La columna `affected_params` faltaba en el bundle web (sí estaba en el Python desde C1).
Ahora se serializa como lista separada por `;` para compatibilidad CSV.

## Corrección en `web/public/index.html`
Sublead actualizado de "Parche C1" a "Parche C4".

## Nuevos ficheros de diseño en `diseno_c4/`

`diseno_c4/04_seleccion_multiple/multi_region_model.py`  
Modelo de datos para múltiples regiones con relaciones PRESERVE/MODIFY/EXCLUDE/DEPENDS_ON,
estado de progreso por región y estado global consolidado. El modelo soporta N regiones desde
Fase I; la UI puede exponer solo una sin cambiar el modelo subyacente.

`diseno_c4/05_capas_no_destructivas/nondestructive_layer.py`  
Arquitectura mínima no destructiva: SourceLayer (inmutable), EditLayer (por región autorizada),
CompositeSpec (especificación para el executor). Si la verificación falla, la capa se descarta
y la fuente permanece intacta.

`diseno_c4/07_acoplamiento_herramienta/sovereign_proxy.py`  
Patrón Proxy Soberano: ContractRequest (firmado por el SV), ContractResponse (del executor),
SovereignProxy (orquestador), DryRunExecutor, LocalFileExecutor e interfaz ExecutorAdapter.

## Delimitación
Este parche cierra únicamente los fallos de implementación identificados en la auditoría externa
(2026-04-14) y deposita los primeros módulos de diseño para C5. No altera la arquitectura de la
célula ni los contratos existentes.
