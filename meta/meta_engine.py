"""
meta/meta_engine.py
===================
Motor normativo de la meta-célula SV(9,3)-IA.

9 parámetros de integridad del sistema de IA.
T(9) = ⌊7·9/9⌋ = 7.

Semántica:
  0 → parámetro de integridad verificado y conforme
  1 → parámetro de integridad comprometido
  U → no verificable

Clases:
  INTRUSIÓN (n₁ ≥ 7)     → confianza anulada, resultados no válidos
  NORMAL (n₀ ≥ 7)        → sistema confiable, resultados válidos
  INDETERMINADO           → supervisión reforzada

En producción, los parámetros se comprueban automáticamente por el sistema.
No los rellena un usuario.

Autor: Juan Antonio Lloret Egea  |  ORCID: 0000-0002-6634-3351
ISSN 2695-6411  |  CC BY-NC-ND 4.0
"""

from __future__ import annotations
from typing import Any

Ternary = str  # "0" | "1" | "U"

N         = 9
THRESHOLD = 7   # T(9) = floor(7·9/9) = 7
CLASSES   = ("INTRUSIÓN", "INDETERMINADO", "NORMAL")

PARAM_IDS = [f"M{i}" for i in range(1, 10)]

PARAM_NAMES = {
    "M1": "Integridad de pesos",
    "M2": "Procedencia del dataset",
    "M3": "Control de accesos",
    "M4": "Tests adversariales",
    "M5": "Telemetría",
    "M6": "Aislamiento de entornos",
    "M7": "Logging inalterable",
    "M8": "Supervisión humana",
    "M9": "Supply chain",
}


def _get(state: dict, key: str) -> Any:
    """Devuelve state[key] si existe y no es None; en otro caso None."""
    return state.get(key, None)


def M1(state: dict) -> Ternary:
    """M1 — Integridad de pesos: hash/firma verificado."""
    v = _get(state, "weights_integrity")
    if v is None: return "U"
    return "0" if v else "1"


def M2(state: dict) -> Ternary:
    """M2 — Procedencia del dataset: trazabilidad y licencia verificadas."""
    v = _get(state, "dataset_provenance")
    if v is None: return "U"
    return "0" if v else "1"


def M3(state: dict) -> Ternary:
    """M3 — Control de accesos: identidades y permisos gestionados."""
    v = _get(state, "access_control")
    if v is None: return "U"
    return "0" if v else "1"


def M4(state: dict) -> Ternary:
    """M4 — Tests adversariales: robustez verificada."""
    v = _get(state, "adversarial_tests")
    if v is None: return "U"
    return "0" if v else "1"


def M5(state: dict) -> Ternary:
    """M5 — Telemetría: monitorización de inferencias activa."""
    v = _get(state, "telemetry_active")
    if v is None: return "U"
    return "0" if v else "1"


def M6(state: dict) -> Ternary:
    """M6 — Aislamiento de entornos: dev/staging/producción separados."""
    v = _get(state, "environment_isolation")
    if v is None: return "U"
    return "0" if v else "1"


def M7(state: dict) -> Ternary:
    """M7 — Logging inalterable: registro inmutable activo."""
    v = _get(state, "immutable_logging")
    if v is None: return "U"
    return "0" if v else "1"


def M8(state: dict) -> Ternary:
    """M8 — Supervisión humana: circuitos de revisión activos."""
    v = _get(state, "human_oversight")
    if v is None: return "U"
    return "0" if v else "1"


def M9(state: dict) -> Ternary:
    """M9 — Supply chain: integridad de dependencias verificada."""
    v = _get(state, "supply_chain_integrity")
    if v is None: return "U"
    return "0" if v else "1"


_PARAM_FUNCTIONS = [M1, M2, M3, M4, M5, M6, M7, M8, M9]


def evaluate(state: dict) -> list[Ternary]:
    """Evalúa el estado del sistema y devuelve vector M1…M9."""
    return [fn(state) for fn in _PARAM_FUNCTIONS]


def classify(vector: list[Ternary]) -> str:
    """
    Clasifica el vector de la meta-célula.

    T(9) = 7

    Devuelve
    --------
    "INTRUSIÓN"     si n₁ ≥ 7  → confianza anulada
    "NORMAL"        si n₀ ≥ 7  → sistema confiable
    "INDETERMINADO" en el resto → supervisión reforzada
    """
    n1 = vector.count("1")
    n0 = vector.count("0")

    if n1 >= THRESHOLD:
        return "INTRUSIÓN"
    if n0 >= THRESHOLD:
        return "NORMAL"
    return "INDETERMINADO"


def evaluate_and_classify(state: dict) -> tuple[list[Ternary], str]:
    """Atajo: evalúa y clasifica."""
    vector = evaluate(state)
    return vector, classify(vector)


def is_vetoed(state: dict) -> bool:
    """
    Devuelve True si la meta-célula anula los resultados
    (INTRUSIÓN detectada).
    """
    _, cls = evaluate_and_classify(state)
    return cls == "INTRUSIÓN"


def explain(state: dict) -> dict:
    """Trazabilidad completa."""
    vector = evaluate(state)
    global_class = classify(vector)
    return {
        "vector":    dict(zip(PARAM_IDS, vector)),
        "counts":    {
            "n0": vector.count("0"),
            "n1": vector.count("1"),
            "nU": vector.count("U"),
        },
        "class":     global_class,
        "threshold": THRESHOLD,
        "vetoed":    global_class == "INTRUSIÓN",
    }
