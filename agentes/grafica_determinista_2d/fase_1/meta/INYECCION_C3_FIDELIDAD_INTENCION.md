# INYECCION_C3_FIDELIDAD_INTENCION

## Objeto
Parche mínimo C3 del AE-GD2-SV Fase I.

## Alcance
1. Hacer más literal la traducción entre la nota del usuario y el borrador de intención.
2. Evitar que `footer` quede preservado por defecto cuando el usuario lo pide como objeto de corrección.
3. Detectar restricciones negativas tanto en texto libre como en restricciones duras.
4. Rechazar la ejecución cuando el mismo objeto aparezca simultáneamente en `modify` y `preserve`.

## Delimitación negativa
Este parche no toca célula, contratos, bundle, banco técnico ni corrector factual más allá de mejorar la fidelidad del paso `packet -> draft`.

## Archivo afectado
- `web/public/app.js`
