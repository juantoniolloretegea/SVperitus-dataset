# SVperitus — Motor Normativo en Rust

> **Estado:** Paridad técnica del prototipo Playground validada (108/108 tests).
> Lógica clínica CONGELADA — no se modifica hasta cotejo adversarial médico.
> Próximo paso: migración a workspace Cargo real con crates separados.

---

## Qué hay aquí

| Archivo / ruta | Descripción | Estado |
|---|---|---|
| `svperitus_playground_v03_final.rs` | Motor IMMUNO-1 completo en Rust (archivo único, verificable en [Rust Playground](https://play.rust-lang.org)) | 108/108 tests |
| `wasm-demo/` | Demo web interactiva del motor Rust/WASM en navegador | Publicada |
| `imm1_normative/` | Estructura Cargo placeholder (se reemplazará por workspace real) | Placeholder |

## Ejecutarlo ya en Rust (sin instalar nada)

Este directorio ofrece ahora **dos formas de ejecutar Rust**, según lo que el lector quiera comprobar.

### Opción A — Rust Playground (verificación técnica)

Use esta opción si quiere comprobar el motor normativo como archivo único y ver la salida de tests.

**Pasos**
1. Abra [Rust Playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2024)
2. Copie el contenido de `svperitus_playground_v03_final.rs`
3. Péguelo en el editor
4. Pulse **Run**
5. Verifique que la salida final muestre: `108/108 passed`

**Qué hace esta opción**
- Ejecuta el motor IMMUNO-1 en Rust como archivo único
- Comprueba la paridad técnica del prototipo frente a Python
- Verifica invariantes, tests globales, tests de frontera, serde y trazabilidad

**Cuándo usarla**
- Si quiere auditar el motor
- Si quiere ver los tests
- Si quiere comprobar la fidelidad técnica del port en Rust

---

### Opción B — Demo web Rust/WASM (uso interactivo)

Use esta opción si quiere rellenar un formulario, obtener una clasificación global y ver el polígono polar directamente en el navegador.

**Abrir demo**
- [Demo Rust/WASM de IMMUNO-1](https://juantoniolloretegea.github.io/SVperitus-dataset/rust/wasm-demo/)

**Qué hace esta opción**
- Carga el motor Rust compilado a WebAssembly en el navegador
- Recoge las respuestas del formulario
- Las transforma en un caso evaluable de IMMUNO-1
- Devuelve:
  - vector ternario P01–P25,
  - conteos `n0 / n1 / nU`,
  - clase global `APTO / INDETERMINADO / NO_APTO`,
  - representación visual en polígono polar

**Cuándo usarla**
- Si quiere ver Rust funcionando de forma interactiva
- Si quiere probar la lógica con una interfaz visual
- Si quiere enseñar el sistema sin entrar todavía en el código

**Alcance**

Esta demo es una interfaz pública del motor Rust en navegador.
No sustituye al motor canónico Python ni equivale a una validación clínica.

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
- La serialización JSON (`serde`) ha mostrado round-trip sin pérdida en los tests ejecutados
- El orden P01-P25 está blindado con test explícito
- Las constantes algebraicas y clínicas están centralizadas
- `explain()` produce una traza auditable por parámetro

## Cómo verificar

### Verificación técnica en Playground

1. Abrir [Rust Playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2024)
2. Seleccionar `stable`
3. Copiar el contenido de `svperitus_playground_v03_final.rs`
4. Pegar en el editor
5. Pulsar **Run**
6. Verificar la salida final: `108/108 passed`

### Ejecución interactiva en navegador

1. Abrir la [demo Rust/WASM de IMMUNO-1](https://juantoniolloretegea.github.io/SVperitus-dataset/rust/wasm-demo/)
2. Rellenar el formulario
3. Revisar:
   - clasificación global,
   - conteos `n0 / n1 / nU`,
   - vector P01–P25,
   - polígono polar
4. Confirmar que el comportamiento es coherente con la lógica esperada de IMMUNO-1

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
