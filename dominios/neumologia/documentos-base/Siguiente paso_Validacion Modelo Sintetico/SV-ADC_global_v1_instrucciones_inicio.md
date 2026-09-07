# SV-ADC(global) v1 — paquete de arranque
## Archivos principales
- `SV-ADC_global_v1_documento_maestro.docx`
- `SV-ADC_global_v1_seed.csv`
- `SV-ADC_global_v1_seed.json`
- `SV-ADC_global_v1_instrucciones_inicio.md`

## Decisión de arquitectura
`SV-ADC(global) v1 = [SV-ADC_L(25,5) + SV-ADC_V(16,4)] + SV-ADC_META(9,3) + Γ_ADC + compositor secuencial`

- `SV-ADC_L(25,5)`: sospecha clínico-lesional estructurada.
- `SV-ADC_V(16,4)`: validez confirmatoria diagnóstica.
- `SV-ADC_META(9,3)`: integridad/clasificabilidad automática del caso.
- `Γ_ADC-L`, `Γ_ADC-V`, `Γ_ADC-GLOBAL`: criticidad activa de la indeterminación.
- `composer_state`: progresión diagnóstica útil o bloqueo.

## Semántica común
- `0`: no apoyo / no suficiencia / no progresión según el campo.
- `1`: apoyo / suficiencia / progresión útil según el campo.
- `U`: indeterminado, no consta, no evaluable o conflicto no resuelto.

## Reglas maestras
1. La célula L no confirma por sí sola.
2. La célula V no cierra ignorando discordancias mayores.
3. La meta-célula puede bloquear un cierre aunque L y V sean localmente fuertes.
4. `GLOBAL_HIGH` sólo existe si L y V son favorables y META no bloquea.
5. `GLOBAL_LOW` sólo existe si L y V son negativos y META no tensa/bloquea.
6. Todo lo demás cae en `GLOBAL_U`.

## Uso recomendado
Este paquete sirve como fuente de verdad para:
- generación del dataset sintético;
- render polar canónico;
- preentrenamiento de la CNN de doble rama sobre L/V y control META;
- futuras revisiones expertas.

## Colaboración con Claude o con un chat nuevo
La jerarquía de autoridad debe ser:
1. Documento maestro `.docx`
2. CSV semilla (tabla maestra de campos)
3. JSON semilla (arquitectura + plantilla + reglas resumidas)
4. Este Markdown como guía de arranque

Cualquier cambio semántico en un campo o en una regla debe generar nueva versión.

## Nota doctrinal
La personalidad adicional respecto a la primera fase neumológica no viene de más parámetros manuales, sino de tres capas de segundo orden: `SV-ADC_META(9,3)`, `Γ_ADC` y el `compositor secuencial`.
