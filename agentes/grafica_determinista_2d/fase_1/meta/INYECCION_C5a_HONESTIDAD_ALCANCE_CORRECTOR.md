# INYECCION_C5a_HONESTIDAD_ALCANCE_CORRECTOR

## Objeto
Parche C5a del AE-GD2-SV Fase I — honestidad sobre el alcance del corrector para archivos raster.

## Problema
Cuando el usuario sube un archivo PNG o JPG en modo `corregir`, el sistema ejecuta el corrector
factual y produce el bundle de auditoría sin incluir ninguna imagen procesada. La UI no advertía
de esta limitación, generando una expectativa no cumplida.

El bundle es correcto dentro del alcance declarado de Fase 1 (informe + paquete técnico).
El problema es que la palabra "corregir" y el flujo de ejecución no comunicaban al usuario
qué tipo de salida se estaba produciendo.

## Correcciones incluidas en `web/public/app.js`

### 1. Estado AVISO_ALCANCE en la cuarentena
Cuando el archivo es PNG o JPG y el modo es `corregir`, se emite un estado visible
en el log de cuarentena:

> `AVISO_ALCANCE · Archivo raster (PNG/JPG) · La salida es un informe de corrección
> especificada. La imagen procesada requiere executor externo — previsto en Fase 2.`

Este estado aparece en el `stateLog` durante la ejecución, antes de que el usuario
vea los resultados, en el momento en que la información es relevante.

### 2. Campo `correction_scope` en el report
El objeto `report` incluye ahora un campo `correction_scope` con tres valores posibles:

- `INFORME_ESPECIFICADO — imagen raster no procesada; executor externo requerido (Fase 2)`
  → cuando el archivo es PNG o JPG
- `SVG_CORREGIBLE — corrección estructural disponible en Fase 1`
  → cuando el archivo es SVG (preparado para el Paso 2, INYECCION_C5b)
- `CREACION — sin imagen de entrada`
  → cuando el modo es `crear`

Este campo queda registrado en el bundle (`resumen_ejecutivo.json` y `audit_report.json`),
haciendo la limitación trazable y auditable.

### 3. Visualización en la sección "Auditoría y banco"
La sección de auditoría del panel muestra ahora el campo `correction_scope` como
**Alcance de la corrección**, inmediatamente visible junto al dictamen y la exposición.

## Delimitación negativa
Este parche no altera el motor, la célula, los contratos, el corrector factual, el bundle,
ni ningún parámetro Pk. No cambia el procesamiento de la imagen. Solo añade información
de transparencia sobre el alcance de la corrección producida.

No constituye una corrección de la imagen. No introduce semántica sobre la figura.
No abre ningún carril hacia el executor externo — ese es el objeto de INYECCION_C5b.

## Archivos afectados
- `web/public/app.js`
