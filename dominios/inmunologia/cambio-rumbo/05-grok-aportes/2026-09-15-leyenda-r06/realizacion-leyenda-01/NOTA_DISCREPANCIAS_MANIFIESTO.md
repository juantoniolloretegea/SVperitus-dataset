# Discrepancias del manifiesto de origen y variantes conservadas

El manifiesto `MANIFIESTO.tsv` del corte `5e3c29bf` se conserva sin modificación.

| Ruta | Declarado | Observado en `5e3c29bf` | Causa atribuible |
|---|---|---|---|
| PROTOCOLO_CUALIFICACION.md | 4407 B, SHA `c5be9527…` | 4379 B, SHA `6233cde1…` | El texto local usaba signos tipográficos y fórmulas que el depósito no reprodujo byte a byte. Ambas variantes están en `evidencias/variantes/`. Rige el texto depositado para aquella recepción; rige `PROTOCOLO_CUALIFICACION_02.md` para la tanda finita. |
| src/regiones.rs | 774 B, SHA `587987ab…` | 775 B, SHA `044d2953…` | Un carácter adicional en el comentario de W (`\\` frente a la variante local). Ambas en `evidencias/variantes/`. El fuente de trabajo es la variante depositada de 775 B. |
| src/main.rs, src/png_lectura.rs, src/reconocimiento.rs | filas del manifiesto | ausentes del árbol | Los originales locales conservan las huellas declaradas. Quedan en `evidencias/originales-ausentes/` y, corregidos según §10.2, en `src/`. |

No se reconstruye un protocolo histórico distinto del depositado. No se presenta la variante local de 4407 B como el archivo publicado en `5e3c29bf`.
