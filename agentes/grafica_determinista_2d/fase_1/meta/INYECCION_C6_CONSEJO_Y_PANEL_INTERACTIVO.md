# INYECCION_C6_CONSEJO_Y_PANEL_INTERACTIVO

## Objeto
Panel de consejo del Agente 2D con carta R3, análisis matemático estructural
y polígono interactivo para exploración soberana del experto.

## Fundamento doctrinal
- Estatuto del universo de sucesos (ITVIA, 12/04/2026, ISSN 2695-6411)
- FTD AE-GD2-SV §VII — Universo de sucesos
- Carta R3: Lloret Egea, J.A. (ITVIA, 16/03/2026, ISSN 2695-6411)
- Carta Magna de autogobierno (ITVIA, 13/04/2026)

## Universo de sucesos del AE-GD2-SV (FTD §VII)
El único tipo de suceso que el panel de consejo puede registrar en el banco es:
  `registrar_override_humano_informado`

Todos los demás tipos del universo del agente son actos del sistema, no del experto.
La exploración en el polígono interactivo es silenciosa — no genera sucesos.

## Criterio de registro del override soberano
Se registra `registrar_override_humano_informado` si y solo si:
  1. El experto ha modificado un Pk con valor original ≠ '0' (parámetro crítico), Y
  2. El experto hace clic explícito en "Registrar override" para ese parámetro.

La exploración libre (toggle sin registrar) no genera sucesos en el banco.
Esto respeta la regla: "ni totalidad del mundo, ni rigidez inhabitable,
ni flexibilidad blanda" (Estatuto §2.7).

## Fichero nuevo: `web/public/consejo.html`
Se abre desde el botón "Ver consejo del Agente 2D ↗" del panel principal.
Lee datos del run desde `localStorage['ae_gd2_sv_consejo']`.

Secciones:
1. Estado de la célula (n₀, n₁, nᵤ, dictamen)
2. Corrector factual (gradiente, curvatura, residual, pasos)
3. Carta R3 (L₂, L₃, ΔL, Cz, Eρ, Ez, k(v)) para frame y gob
4. Consejo del Agente 2D (texto generado desde las matemáticas)
5. Sección explícita: "Interpretación de dominio: responsabilidad del experto soberano"
6. Polígono interactivo (exploración silenciosa) + tabla Pk
7. Banco de sucesos (solo overrides soberanos registrados explícitamente)

## Carta R3 implementada
Φ₃(Pᵢ=s) = (ρ(s)cosθᵢ, ρ(s)sinθᵢ, z(s))
z(0)=z(1)=0, z(U)=h=2.2 (convención de carta, no atributo semántico de U)
Ez = k(v)·h² — invariante exacto; rango independiente de h.

## Cambios en `web/public/app.js`
- `computeR3Metrics(cell, h)`: calcula L₂, L₃, ΔL, Cz, Eρ, Ez, k(v)
- `r3frame` y `r3gob` calculados en `run()`, añadidos al report
- Tras EXPORT_READY: datos guardados en `localStorage['ae_gd2_sv_consejo']`
- `consejoBtn` se habilita tras EXPORT_READY

## Cambios en `web/public/index.html`
- Botón "Ver consejo del Agente 2D ↗" (disabled hasta EXPORT_READY)
- Sublead actualizado a "Parche C6"

## También incluido en este ZIP
- Corrección de bug (operador + faltante en svgPropsHtml)
