# Documento 8 — Compilador doctrinal y célula meta SV(9,3)-IA

> **Estado:** Publicado. Release 2 disponible en PubPub (itvia.online).  
> Release 3 en preparación (cerrará tensiones identificadas en revisión adversarial).

Este documento integra SVcustos y SVperitus en una visión unificada
y presenta la **célula meta SV(9,3)-IA** de integridad del modelo de IA.

**Publicación:**  
https://www.itvia.online/pub/compilador-doctrinal-y-celula-meta-sv93-ia/release/2

**Serie:**  
«De SVcustos, el marco (framework) de intrusión, hasta SVperitus: agentes especializados»  
ISSN 2695-6411 · CC BY-NC-ND 4.0  
Autor: Juan Antonio Lloret Egea · ORCID: 0000-0002-6634-3351

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
