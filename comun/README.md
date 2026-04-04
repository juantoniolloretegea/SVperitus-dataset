# Común

**Fecha y Versión: V.1 del conjunto**  
**Fecha:** 4 de abril de 2026  
**Versión del conjunto:** V.1 del conjunto  
**Autor del corpus:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Institución:** ITVIA — IA eñ™  
**ISSN:** 2695-6411  
**Licencia:** CC BY-NC-ND 4.0  
**Titularidad y autoría:** © Juan Antonio Lloret Egea, 2026. Este conjunto se distribuye con atribución explícita de autoría y bajo la licencia indicada, sin autorización para apropiación de la paternidad intelectual del Sistema Vectorial SV.  

---


Núcleo formal compartido entre todos los dominios del Agente Especializado.

| Archivo | Descripción | Estado |
|---|---|---|
| `polygons.py` | Generación del polígono polar (RADIUS_MAP invariante) | Activo |
| `io_utils.py` | Utilidades de entrada/salida | Activo |
| `gamma.py` | Función de criticidad Γ(v) = m − μ | Activo |

## Función de criticidad Γ(v)

Contribución original de la serie SVperitus. Matemática exacta, sin estadística.

Γ(v) clasifica la indeterminación de un vector ternario:

- **Γ < 0** → Irreducible. Ni resolviendo todas las U se alcanza clasificación.
- **Γ = 0** → Fronteriza. Cada U es decisiva.
- **Γ > 0** → Resoluble. Γ indica cuántas U pueden salir desfavorables sin perder la clasificación.

Implementada en Python (referencia canónica) y en JavaScript (cliente web). No portada a Rust por decisión del consenso de lenguajes.
