# INYECCION_C4b_VIEWPORT_POLIGONO

## Objeto
Corrección arquitectónica del viewport del polígono SVG generado por el sistema.

## Alcance
El sistema corrige su PROPIO artefacto visual (la función `polygonSvg`).
No interviene sobre contenido del usuario.

## Problema
`viewBox="0 0 520 560"` insuficiente para el texto de atribución
(155 chars × 0.55 × fs9 = 767px > 520px).
La solución anterior (tspan) dividió arbitrariamente el texto, eliminó el prefijo
"Autor:" y redujo font-size sin mandato. Era corrección de síntoma, no de causa.

## Solución
Dimensionar el viewport para contener su contenido a las especificaciones declaradas.

Cálculo determinista y auditable:
  155 chars × 0.55 × 9px = 767px + 2×40px margen = 847px → **860px**

Cambios en `polygonSvg`:
- viewBox: `0 0 860 560`
- cx: 430 (centro de 860px)
- rect: width=858
- Título y subtítulo: x=430
- Leyenda: redistribuida a x=180, 360, 560
- Footer: línea única, `x="430"`, `font-size="9"`, prefijo "Autor:" restaurado

## Invariantes
- El texto no se divide, comprime ni trunca.
- El factor 0.55 es el estándar estadístico para sans-serif SVG (documentado).
- El polígono K3 (r0=140, cy=260) no cambia de forma ni de tamaño.
- La atribución CC BY-NC-ND 4.0 se preserva íntegra.

## Archivos afectados
- `web/public/app.js` — función `polygonSvg`
