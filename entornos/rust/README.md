# SVperitus — Motor Normativo en Rust

> **Estado:** IMMUNO-1 congelado (108/108 tests). IMMUNO-2, meta-célula y compositor portados y verificados (19/19 paridad WASM vs Python). Compilación a WASM automatizada por GitHub Actions.

---

## Qué hay aquí

| Archivo / ruta | Descripción | Estado |
|---|---|---|
| `wasm/src/lib.rs` | Motor unificado: IMMUNO-1 + IMMUNO-2 + meta-célula + compositor serie | Verificado |
| `wasm/Cargo.toml` | Configuración del crate WASM (wasm-bindgen + serde) | Activo |
| `svperitus_playground_v03_final.rs` | Motor IMMUNO-1 en archivo único (verificable en Rust Playground) | 108/108 tests |
| `imm1_normative/` | Estructura Cargo placeholder (futuro workspace) | Placeholder |

## Entry points WASM

El módulo `wasm/src/lib.rs` expone 6 funciones al navegador:

| Función | Módulo | Entrada | Salida |
|---|---|---|---|
| `evaluate_immuno1(json)` | IMMUNO-1 | Caso clínico JSON | Vector + clase + traza |
| `engine_info()` | IMMUNO-1 | — | Info del motor |
| `evaluate_immuno2(json)` | IMMUNO-2 | Caso clínico JSON | Vector + clase + traza |
| `meta_evaluate(json)` | Meta-célula | Estado del sistema JSON | Vector + clase + veto |
| `compose(json1, json2, jsonM)` | Compositor | Tres JSON | Resultado combinado |
| `engine_info_v2()` | Todos | — | Info completa |

`evaluate_immuno1()` y `engine_info()` son retrocompatibles: misma API, misma salida que antes del port de IMMUNO-2.

## Verificación

### Paridad WASM vs Python (19 tests automáticos)

Abrir en navegador: [Tests de paridad](https://juantoniolloretegea.github.io/SVperitus-dataset/aplicaciones/demo_wasm/test_parity_wasm.html)

19 casos (13 IMMUNO-2 + 6 meta-célula) verificados contra los resultados del motor Python de referencia. Incluye casos de frontera para P08 (corticoides), P09 (duración IS), P10 (linfopenia + rituximab), P22 (IgG zona gris) y P25 (puente).

### Playground IMMUNO-1 (108 tests)

1. Abrir [Rust Playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2024)
2. Copiar `svperitus_playground_v03_final.rs`
3. Pulsar Run
4. Verificar: `108/108 passed`

## Demos en vivo

| Demo | Descripción |
|---|---|
| [IMMUNO-1 interactivo](https://juantoniolloretegea.github.io/SVperitus-dataset/aplicaciones/demo_wasm/) | Formulario P01–P25, polígono polar, motor Rust/WASM |
| [Compositor IMMUNO-1 → IMMUNO-2](https://juantoniolloretegea.github.io/SVperitus-dataset/aplicaciones/demo_wasm/compositor.html) | Dos células enlazadas + meta-célula + Γ(v) en JavaScript |
| [Tests de paridad](https://juantoniolloretegea.github.io/SVperitus-dataset/aplicaciones/demo_wasm/test_parity_wasm.html) | 19/19 verificación automática WASM vs Python |

## Compilación

La compilación de Rust a WASM está automatizada por GitHub Actions (`.github/workflows/build-wasm.yml`). Cada push a `entornos/rust/wasm/` dispara el build, que deposita los artefactos en `aplicaciones/demo_wasm/pkg/`.

No es necesario compilar localmente.

## Principio rector

> Python es la fuente de verdad normativa. Rust es un port fiel.
> El port Rust no introduce criterio clínico nuevo.
> Si Python y Rust discrepan, Python tiene razón.

Cadena de autoridad:

1. Documento formal publicado
2. Motor normativo Python
3. YAML de configuración
4. Tests de paridad
5. Port Rust (este directorio)

## Nota sobre Γ(v)

La función de criticidad Γ(v) no se porta a Rust. Se calcula en Python (referencia canónica) y en JavaScript (cliente web). Esta decisión responde al consenso de lenguajes: Γ se porta a compilado por criterio contextual (carga, latencia, despliegue), no por umbral fijo. Para n=25, la enumeración exacta se ejecuta en milisegundos en JavaScript.

## Referencia cruzada

- Motor Python IMMUNO-1: `dominios/inmunologia/fase_1/src/normative_engine.py`
- Motor Python IMMUNO-2: `dominios/inmunologia/fase_2/src/normative_engine.py`
- Compositor Python: `dominios/inmunologia/compositor/compose.py`
- Meta-célula Python: `meta/meta_engine.py`
- Γ(v) Python: `comun/gamma.py`
- Configuración IMMUNO-1: `dominios/inmunologia/fase_1/config/imm_n25.yaml`
- Configuración IMMUNO-2: `dominios/inmunologia/fase_2/config/imm2_n25.yaml`
- Configuración meta-célula: `meta/config/meta_n9.yaml`
- Tests de conformidad: `especificaciones/conformidad/`
