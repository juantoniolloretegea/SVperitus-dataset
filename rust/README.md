# SVperitus — Motor Normativo en Rust

> **Estado:** Paridad técnica del prototipo Playground validada (108/108 tests).
> Lógica clínica CONGELADA — no se modifica hasta cotejo adversarial médico.
> Próximo paso: migración a workspace Cargo real con crates separados.

---

## Qué hay aquí

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| `svperitus_playground_v03_final.rs` | Motor IMMUNO-1 completo en Rust (archivo único, verificable en [Rust Playground](https://play.rust-lang.org)) | 108/108 tests |
| `imm1_normative/` | Estructura Cargo placeholder (se reemplazará por workspace real) | Placeholder |

## Resultados de paridad (v0.3 final)

```
Global parity:     6/6 passed
Boundary tests:  100/100 passed (all 25 parameters)
Serde tests:       2/2 passed
TOTAL:           108/108 passed
```

Verificado en Rust Playground (Stable 1.94.0, Edition 2024). Esta verificación corresponde al entorno Playground; la migración al workspace Cargo definitivo es el siguiente paso.

## Qué demuestra

- La semántica ternaria (0/1/U) ha mostrado equivalencia entre Python y Rust en los tests de paridad definidos
- La regla T(25)=19 ha producido clasificaciones equivalentes entre Python y Rust en los tests ejecutados
- Los 25 parámetros P01-P25 tienen tests de frontera en todos sus umbrales
- La serialización JSON (serde) hace round-trip sin pérdida
- El orden P01-P25 está blindado con test explícito
- Las constantes algebraicas y clínicas están centralizadas
- `explain()` produce traza auditable por parámetro

## Cómo verificar

1. Abrir [play.rust-lang.org](https://play.rust-lang.org)
2. Seleccionar Stable channel
3. Copiar el contenido de `svperitus_playground_v03_final.rs`
4. Pegar en el editor y pulsar Run
5. Verificar: `108/108 passed`

## Principio rector (NO negociable)

> Python es la fuente de verdad normativa. Rust es un port fiel.
> El port Rust NUNCA introduce criterio clínico nuevo.
> Si Python y Rust discrepan, Python tiene razón.

Cadena de autoridad:

1. Documento formal
2. `normative_engine.py` (Python)
3. YAML de configuración
4. Parity tests
5. **Port Rust** (este directorio)

## Arquitectura prevista (workspace Cargo)

Cuando se migre del Playground a Cargo real:

```
rust/
├── Cargo.toml                    ← workspace
├── svperitus-core/               ← invariantes compartidas (Ternary, classify, RADIUS_MAP)
├── imm1-normative/               ← motor IMMUNO-1 (25 eval functions)
├── imm2-normative/               ← motor IMMUNO-2 (futuro)
└── parity-runner/                ← verificador de paridad JSON
```

`svperitus-core` es compartido por todos los módulos y sólo debe modificarse
por decisión arquitectónica explícita.

## Referencia cruzada

- Motor Python IMMUNO-1: `IMMUNO-1/normative_engine.py`
- Configuración: `IMMUNO-1/config/imm_n25.yaml`
- Documento 7: `docs/Documento7_IMMUNO-1.md`
- Spec IMMUNO-2: `IMMUNO-2/IMMUNO2_P01-P25_spec.md`
