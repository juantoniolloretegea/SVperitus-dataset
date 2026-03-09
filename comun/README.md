# Común

Núcleo formal compartido entre todos los dominios del Agente Especializado.

| Archivo | Descripción | Estado |
|---|---|---|
| `polygons.py` | Generación del polígono polar (RADIUS_MAP invariante) | Activo |
| `io_utils.py` | Utilidades de entrada/salida | Activo |
| `gamma.py` | Función de criticidad Γ(v) = m − μ | Se incorpora junto con el motor de fase 2 |

## Función de criticidad Γ(v)

Contribución original de la serie SVperitus. Matemática exacta, sin estadística.

Γ(v) clasifica la indeterminación de un vector ternario:

- **Γ < 0** → Irreducible. Ni resolviendo todas las U se alcanza clasificación.
- **Γ = 0** → Fronteriza. Cada U es decisiva.
- **Γ > 0** → Resoluble. Γ indica cuántas U pueden salir desfavorables sin perder la clasificación.

Implementada en Python (referencia canónica) y en JavaScript (cliente web). No portada a Rust por decisión del consenso de lenguajes.
