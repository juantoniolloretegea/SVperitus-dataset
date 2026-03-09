# Meta-célula SV(9,3)-IA

Célula de integridad del sistema de inteligencia artificial. 9 parámetros (3 capas × 3). T(9) = 7.

No editable por el usuario. Determinada automáticamente por el sistema en producción. En el demostrador web existe un botón de simulación de intrusión con fines didácticos.

---

## Semántica de integridad (distinta de la semántica clínica)

La meta-célula conserva la semántica de integridad heredada de SVcustos (el marco de intrusión). Es distinta de la semántica de dominio (APTO / NO_APTO) porque la meta-célula no evalúa el contenido clínico sino la validez del propio sistema.

| Clase meta-célula | Significado | Efecto sobre los resultados de dominio |
|---|---|---|
| **NORMAL** (n₀ ≥ 7) | Sistema íntegro | Resultados de IMMUNO-1 e IMMUNO-2 válidos |
| **INTRUSIÓN** (n₁ ≥ 7) | Sistema comprometido | Resultados de IMMUNO-1 e IMMUNO-2 anulados |
| **INDETERMINADO** | No verificable | Resultados bajo supervisión reforzada |

## Parámetros

| ID | Nombre | Campo |
|---|---|---|
| M1 | Integridad de pesos | `weights_integrity` |
| M2 | Procedencia del dataset | `dataset_provenance` |
| M3 | Control de accesos | `access_control` |
| M4 | Tests adversariales | `adversarial_tests` |
| M5 | Telemetría | `telemetry_active` |
| M6 | Aislamiento de entornos | `environment_isolation` |
| M7 | Logging inalterable | `immutable_logging` |
| M8 | Supervisión humana | `human_oversight` |
| M9 | Cadena de suministro software | `supply_chain_integrity` |

## Contenido de esta carpeta

| Archivo | Descripción |
|---|---|
| `config/meta_n9.yaml` | Configuración YAML de la meta-célula |
| `meta_engine.py` | Motor normativo Python (pendiente de subir) |

## Referencia cruzada

- Configuración: `config/meta_n9.yaml`
- Motor Python: se sube junto con el motor de fase 2
- Port Rust: incluido en `entornos/rust/wasm/src/lib.rs` (funciones `meta_evaluate()`)
- Compositor: `dominios/inmunologia/compositor/`
- Documento 8: `documentos/serie/`
