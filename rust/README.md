# SVperitus IMMUNO-1 — Implementación Rust (prevista)

> **Estado:** Planificado. Directorio reservado. No implementado todavía.
> La implementación de referencia canónica es Python (`IMMUNO-1/normative_engine.py`).

---

## Propósito

Fase 2 de la hoja de ruta SVperitus–IMMUNO-1: implementación del motor
normativo en **Rust** para uso en entornos de alto rendimiento, sistemas
embebidos o contextos donde Python no es viable.

---

## Principio rector (NO negociable)

> **Cualquier cambio en el motor normativo debe hacerse primero en el
> documento formal y en `normative_engine.py` (Python).**
> Rust es un port de la implementación Python, no una fuente de verdad.
> No está autorizado a introducir reglas nuevas ni a modificar umbrales.

---

## Estructura prevista

```
rust/
└── imm1_normative/        ← crate Rust del motor normativo IMMUNO-1
    ├── Cargo.toml
    ├── src/
    │   ├── lib.rs          ← funciones P01–P25 + aggregate()
    │   ├── engine.rs       ← lógica normativa (port bit-a-bit de normative_engine.py)
    │   └── config.rs       ← lectura de imm_n25.yaml (n, threshold, class_to_idx)
    └── tests/
        └── parity_tests.rs ← tests de paridad contra casos exportados desde Python
```

---

## Protocolo de equivalencia

La implementación Rust debe superar un test de paridad que:

1. Lea un conjunto de casos exportados desde Python en JSON
   (`cases_parity_test.json`, generado con `normative_engine.explain()`).
2. Evalúe cada caso con el motor Rust.
3. Compare vector ternario y clase global con los valores de referencia Python.
4. Exija **100% de coincidencia** (equivalencia bit-a-bit en los resultados
   de clasificación ternaria).

---

## Interfaz de entrada/salida prevista

```rust
// Entrada: caso clínico serializado como JSON
// Salida:  vector ternario P01–P25 + clase global
pub fn evaluate(case_json: &str) -> Result<EvaluationResult, EngineError>;

pub struct EvaluationResult {
    pub vector: [Ternary; 25],  // "0" | "1" | "U"
    pub class:  GlobalClass,    // NoApto | Indeterminado | Apto
    pub counts: Counts,         // n0, n1, nU
}
```

---

## Referencia cruzada

- Motor normativo Python: `IMMUNO-1/normative_engine.py`
- Configuración canónica: `IMMUNO-1/config/imm_n25.yaml`
- Documento formal: `docs/Documento7_IMMUNO-1.md`

---

*Este directorio se poblará en la Fase 2 de implementación.*
