# Inmunología — Compositor serie

Composición en serie: IMMUNO-1 → P25 → IMMUNO-2, bajo supervisión de la meta-célula SV(9,3)-IA.

---

## Mecanismo

1. Se evalúa IMMUNO-1 con los datos del paciente.
2. La clase global de IMMUNO-1 se traduce al valor puente P25 de IMMUNO-2: APTO → 0, NO_APTO → 1, INDETERMINADO → U.
3. Se evalúa IMMUNO-2 con P25 inyectado. El usuario no puede modificar P25 manualmente.
4. La meta-célula verifica la integridad del sistema. Si detecta INTRUSIÓN, anula los resultados.
5. Se calcula Γ(v) para cada célula en INDETERMINADO.

## Operador formal

La composición utiliza el operador de sustitución σ(k,φ) descrito en los Fundamentos algebraico-semánticos del SV (§7.8). P25 es el parámetro k, y φ es el conector que traduce la clase de IMMUNO-1 al valor ternario de P25.

## Autocrítica documentada

P25 es un conector experimental. La relación clínica real entre profilaxis antiinfecciosa inadecuada y riesgo infeccioso elevado es más compleja que una dependencia lineal. La composición en serie demuestra que la gramática SV permite enlazar células; no valida la dependencia clínica.

Líneas futuras: composición en paralelo para células sin dependencia directa, composición pareada, resolución variable de n.

## Implementaciones

| Lenguaje | Archivo | Estado |
|---|---|---|
| Python | `compose.py` | 26/26 tests |
| Rust/WASM | `entornos/rust/wasm/src/lib.rs` → `compose()` | 19/19 paridad |
| Web interactiva | `aplicaciones/demo_wasm/compositor.html` | Publicada |

## Referencia cruzada

- IMMUNO-1: `../fase_1/`
- IMMUNO-2: `../fase_2/`
- Meta-célula: `../../../meta/`
- Función Γ(v): `../../../comun/gamma.py`
- Compositor web: `../../../aplicaciones/demo_wasm/compositor.html`
