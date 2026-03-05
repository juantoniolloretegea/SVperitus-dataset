# Documento 8 — Compilador SVcustos + SVperitus + Célula Meta IA

> **Estado:** Reservado. Se redactará tras consolidar el Documento 7.

Este documento integrará SVcustos y SVperitus en una visión unificada
y presentará la **célula meta SV(9,3)-IA** de integridad del modelo de IA.

Ver [Documento 7](./Documento7_IMMUNO-1.md) para el módulo prototipo IMMUNO-1.

---

## Célula meta SV(9,3)-IA (vista previa)

9 parámetros que vigilan el ciclo de vida del modelo de IA:

| # | Parámetro | Descripción |
|---|---|---|
| P1 | Integridad de pesos | Hash/firma de los pesos del modelo |
| P2 | Procedencia del dataset | Trazabilidad y licencia de los datos de entrenamiento |
| P3 | Control de accesos | Gestión de identidades y permisos |
| P4 | Tests adversariales | Robustez frente a entradas adversariales |
| P5 | Telemetría | Monitorización de inferencias en producción |
| P6 | Aislamiento de entornos | Separación entre dev/staging/producción |
| P7 | Logging inalterable | Registro inmutable de predicciones y decisiones |
| P8 | Supervisión humana | Circuitos de revisión humana activos |
| P9 | Supply chain | Integridad de dependencias y cadena de suministro software |

Regla: T(9) = 7

- n₁ ≥ 7 → **INTRUSIÓN** → confianza en el modelo **anulada**
- n₀ ≥ 7 → **NORMAL** → modelo operable con normalidad
- resto → **INDETERMINADO** → confianza suspendida, solo bajo supervisión reforzada

*Documento en elaboración.*
