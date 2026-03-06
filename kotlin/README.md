# SVperitus — Línea Kotlin

> **Estado:** línea Kotlin activa, con un primer cliente Kotlin/JS ya publicado en GitHub Pages.  
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

La línea Kotlin ya no está en fase meramente prevista o reservada.

A fecha actual, dispone de:

- un primer cliente `imm1_client/`,
- una ruta pública en GitHub Pages,
- compilación y despliegue mediante GitHub Actions,
- y una primera base visible para demostrar el papel de Kotlin como cliente.

Todavía no constituye una familia completa de clientes Kotlin ni una integración final cerrada en todos los frentes, pero sí un punto de partida funcional y público.

---

## Subdirectorio activo

### `imm1_client/`

Contiene el primer cliente Kotlin/JS asociado a IMMUNO-1.

Su papel es servir como interfaz visible alrededor del motor Rust/WASM ya existente, manteniendo la separación de funciones:

- Kotlin prepara y muestra,
- Rust evalúa,
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
Cliente Kotlin
   ↓
Motor Rust/WASM
   ↓
Resultado evaluado
   ↓
Presentación visual
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
