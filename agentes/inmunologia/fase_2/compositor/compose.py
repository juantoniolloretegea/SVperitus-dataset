"""
compositor/compose.py
=====================
Compositor serie: IMMUNO-1 → P25 → IMMUNO-2.

Ejecuta IMMUNO-1, inyecta su clase global como P25 de IMMUNO-2,
ejecuta IMMUNO-2, calcula Γ para ambos.

P25 es un conector experimental que demuestra que la gramática SV
permite enlazar células. No es una validación clínica de la
dependencia entre profilaxis y riesgo infeccioso.

Autor: Juan Antonio Lloret Egea  |  ORCID: 0000-0002-6634-3351
ISSN 2695-6411  |  CC BY-NC-ND 4.0
"""

from __future__ import annotations
import sys
import os

# Ajustar paths para importar módulos hermanos
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def compose(
    case_immuno1: dict,
    case_immuno2: dict,
    immuno1_engine,
    immuno2_engine,
    gamma_module=None,
) -> dict:
    """
    Ejecuta la composición serie IMMUNO-1 → P25 → IMMUNO-2.

    Parámetros
    ----------
    case_immuno1 : dict con campos clínicos de IMMUNO-1
    case_immuno2 : dict con campos clínicos de IMMUNO-2
                   (P25 / immuno1_class será inyectado automáticamente)
    immuno1_engine : módulo con evaluate(), classify(), explain()
    immuno2_engine : módulo con evaluate(), classify(), explain()
    gamma_module   : módulo con analyze() (opcional, para criticidad)

    Devuelve
    --------
    {
        "immuno1": {
            "vector": [...],
            "counts": {"n0":int, "n1":int, "nU":int},
            "class":  str,
        },
        "immuno2": {
            "vector": [...],
            "counts": {"n0":int, "n1":int, "nU":int},
            "class":  str,
            "bridge_value": str,  # "0", "1", o "U"
        },
        "gamma_immuno1": dict | None,  # análisis Γ si INDETERMINADO
        "gamma_immuno2": dict | None,
        "gamma_composition": dict | None,  # impacto de P25
    }
    """
    # ── Paso 1: evaluar IMMUNO-1 ──
    v1 = immuno1_engine.evaluate(case_immuno1)
    c1 = immuno1_engine.classify(v1)

    # ── Paso 2: traducir clase a valor puente ──
    bridge_map = {"APTO": "0", "NO_APTO": "1", "INDETERMINADO": "U"}
    bridge_value = bridge_map.get(c1, "U")

    # ── Paso 3: inyectar P25 en caso IMMUNO-2 ──
    case2_with_bridge = dict(case_immuno2)
    case2_with_bridge["immuno1_class"] = c1 if c1 != "INDETERMINADO" else None
    # Si IMMUNO-1 es INDETERMINADO, P25 recibe None → eval lo marca U

    v2 = immuno2_engine.evaluate(case2_with_bridge)
    c2 = immuno2_engine.classify(v2)

    # ── Paso 4: Γ (si módulo disponible) ──
    g1 = None
    g2 = None
    g_comp = None

    if gamma_module is not None:
        if c1 == "INDETERMINADO":
            g1 = gamma_module.analyze(v1)
        if c2 == "INDETERMINADO":
            g2 = gamma_module.analyze(v2)
        # Análisis de composición: ¿cuánto importa resolver IMMUNO-1?
        if c1 == "INDETERMINADO":
            g_comp = gamma_module.composition_gamma(v2, bridge_idx=24)

    return {
        "immuno1": {
            "vector": v1,
            "counts": {
                "n0": v1.count("0"),
                "n1": v1.count("1"),
                "nU": v1.count("U"),
            },
            "class": c1,
        },
        "immuno2": {
            "vector": v2,
            "counts": {
                "n0": v2.count("0"),
                "n1": v2.count("1"),
                "nU": v2.count("U"),
            },
            "class": c2,
            "bridge_value": bridge_value,
        },
        "gamma_immuno1": g1,
        "gamma_immuno2": g2,
        "gamma_composition": g_comp,
    }
