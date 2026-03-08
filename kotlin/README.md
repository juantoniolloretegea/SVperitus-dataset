# SVperitus — Línea Kotlin

> **Estado:** cliente Kotlin con integración mínima real contra el motor Rust/WASM, publicado en GitHub Pages.  
> Kotlin se mantiene como **capa cliente e integradora**, no como nueva fuente de verdad normativa.  
> El cliente concreto de IMMUNO-1 vive en `imm1_client/`.

---

## Qué es este directorio

Este directorio corresponde a la **línea Kotlin de SVperitus**.

Su función es servir como espacio padre para los clientes e integraciones Kotlin del proyecto, manteniendo una separación clara respecto de:

- **Python**, que sigue siendo la fuente canónica de verdad normativa,
- **Rust**, que actúa como port técnico y motor evaluador,
- **Kotlin**, que organiza la experiencia de uso, la integración y la presentación.

---

## Qué no hace Kotlin

Kotlin no:

- redefine P01–P25,
- introduce criterio clínico nuevo,
- sustituye a Python como autoridad normativa,
- ni reemplaza a Rust como motor cuando el flujo depende de Rust/WASM.

Si Kotlin discrepa de Python o Rust, el problema debe entenderse como un problema de integración, no de autoridad normativa.

---

## Estado actual

La línea Kotlin dispone de:

- un primer cliente `imm1_client/`,
- integración real contra el motor Rust/WASM (sin iframe, sin mock),
- una ruta pública en GitHub Pages,
- compilación y despliegue mediante GitHub Actions.

El cliente carga el módulo WASM directamente, construye un caso IMMUNO-1 de demostración, invoca `evaluate_immuno1()` del motor Rust real y muestra el resultado con `engine_info()`, vector P01–P25, conteos n0/n1/nU, clase global y JSON bruto.

Todavía **no constituye** una familia completa de clientes Kotlin ni una integración final cerrada con formulario clínico propio, pero sí un puente real demostrable y verificable.

---

## Subdirectorio activo

### `imm1_client/`

Contiene el cliente Kotlin/JS asociado a IMMUNO-1 con puente real al motor Rust/WASM.

- Kotlin construye el caso,
- Rust lo evalúa,
- Kotlin muestra el resultado,
- Python sigue siendo la fuente canónica de verdad.

**README operativo del cliente:**  
`./imm1_client/README.md`

**Cliente publicado:**  
https://juantoniolloretegea.github.io/SVperitus-dataset/kotlin/imm1_client/

---

## Arquitectura de alto nivel

```text
Usuario
   ↓
Cliente Kotlin (construye caso JSON)
   ↓
Motor Rust/WASM (evaluate_immuno1)
   ↓
Resultado evaluado (JSON)
   ↓
Presentación visual (Kotlin)
```

---

## Regla de oro

> Kotlin organiza la experiencia de uso.  
> Rust evalúa.  
> Python sigue siendo la fuente canónica de verdad.

---

## Referencia cruzada

- Línea Rust: `../rust/README.md`
- Cliente activo: `./imm1_client/README.md`
- Motor Python IMMUNO-1: `../IMMUNO-1/normative_engine.py`
- Configuración: `../IMMUNO-1/config/imm_n25.yaml`
- Documento 7: `../docs/Documento7_IMMUNO-1.md`
