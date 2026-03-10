# Inmunología — Fase 2: IMMUNO-2

Estratificación del riesgo de infección grave en adultos con inmunosupresión farmacológica sistémica no trasplante.

Célula SV(25,5). T(25) = 19. 25 parámetros organizados en 5 capas de 5.

---

## Estado

| Componente | Estado |
|---|---|
| Especificación P01–P25 | Borrador 0. Capa 1 revisada. Capas 2–5 provisionales |
| Motor normativo Python | Implementado. 93/93 tests |
| Función Γ(v) | Implementada. 52/52 tests |
| Compositor serie | Implementado. 26/26 tests (con meta-célula) |
| Port Rust / WASM | Implementado. 19/19 paridad |
| Compositor web interactivo | Publicado |

## Relación con IMMUNO-1

| | IMMUNO-1 (fase 1) | IMMUNO-2 (fase 2) |
|---|---|---|
| Pregunta | ¿Está protegido? (profilaxis/vacunas) | ¿Cuál es su riesgo residual? |
| Población | Neoplasias hematológicas | IS farmacológica no trasplante |
| Estado | Sellado (108/108 tests) | Activo |
| Puente | — | P25 integra la clase global de IMMUNO-1 |

P25 es un conector experimental que demuestra el mecanismo de composición de la gramática SV. No es una validación clínica de la dependencia entre profilaxis y riesgo infeccioso.

## Contenido de esta carpeta

| Archivo | Descripción |
|---|---|
| `IMMUNO2_P01-P25_spec.md` | Especificación completa: 25 parámetros, 5 capas, criterios 0/1/U, referencias clínicas |
| `config/imm2_n25.yaml` | Punto único de verdad |
| `src/normative_engine.py` | Motor normativo P01–P25 (93/93 tests) |

## Exclusiones

Fuera del alcance de IMMUNO-2 (reservados a módulos futuros): TOS, TPH/CAR-T (cubierto por IMMUNO-1), quimioterapia citotóxica pura, VIH como causa primaria.

## Referencia cruzada

- IMMUNO-1: `../fase_1/`
- Compositor: `../compositor/`
- Función Γ(v): `../../../comun/gamma.py`
- Meta-célula: `../../../meta/`
- Port Rust: `../../../entornos/rust/wasm/src/lib.rs`
- Compositor web: `../../../aplicaciones/demo_wasm/compositor.html`
- Documento 7: `../../../documentos/serie/Documento7_IMMUNO-1.md`
