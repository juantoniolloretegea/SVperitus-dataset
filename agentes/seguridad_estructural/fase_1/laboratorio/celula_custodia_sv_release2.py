"""Laboratorio mínimo reproducible para la release 2 de la célula especializada de custodia del SV."""
from __future__ import annotations

import json
from typing import Iterable

ORDER = {"APTO": 0, "INDETERMINADO": 1, "NO_APTO": 2}


def threshold(n: int) -> int:
    return (7 * n) // 9


def summarize_cell(values: Iterable[object]) -> dict[str, int | str]:
    values = list(values)
    n = len(values)
    n1 = sum(v == 1 for v in values)
    n0 = sum(v == 0 for v in values)
    nU = n - n0 - n1
    t = threshold(n)
    if n1 >= t:
        cls = "NO_APTO"
    elif n0 >= t:
        cls = "APTO"
    else:
        cls = "INDETERMINADO"
    return {
        "n": n,
        "n0": n0,
        "n1": n1,
        "nU": nU,
        "threshold": t,
        "class": cls,
    }


def gate(left: str, right: str) -> str:
    table = {
        ("APTO", "APTO"): "APTO",
        ("APTO", "INDETERMINADO"): "INDETERMINADO",
        ("APTO", "NO_APTO"): "NO_APTO",
        ("INDETERMINADO", "APTO"): "INDETERMINADO",
        ("INDETERMINADO", "INDETERMINADO"): "INDETERMINADO",
        ("INDETERMINADO", "NO_APTO"): "NO_APTO",
        ("NO_APTO", "APTO"): "NO_APTO",
        ("NO_APTO", "INDETERMINADO"): "NO_APTO",
        ("NO_APTO", "NO_APTO"): "NO_APTO",
    }
    return table[(left, right)]


def evaluate_architecture(obj9, base9, dis36) -> dict[str, object]:
    c_obj = summarize_cell(obj9)
    c_base = summarize_cell(base9)
    s_suelo = gate(c_obj["class"], c_base["class"])
    c_dis = summarize_cell(dis36)
    a_custodia = gate(c_dis["class"], s_suelo)
    return {
        "C_obj": c_obj,
        "C_base": c_base,
        "S_suelo": s_suelo,
        "C_diseno": c_dis,
        "A_custodia": a_custodia,
    }


def run_cases() -> dict[str, dict[str, object]]:
    caso_1 = evaluate_architecture(
        obj9=[0] * 9,
        base9=[0] * 9,
        dis36=[0] * 36,
    )
    assert caso_1["A_custodia"] == "APTO"

    caso_2 = evaluate_architecture(
        obj9=[0] * 9,
        base9=[1] * 9,
        dis36=[0] * 36,
    )
    assert caso_2["A_custodia"] == "NO_APTO"

    caso_3 = evaluate_architecture(
        obj9=[0] * 9,
        base9=[0] * 9,
        dis36=[0] * 20 + [1] * 8 + ["U"] * 8,
    )
    assert caso_3["A_custodia"] == "INDETERMINADO"

    caso_4 = evaluate_architecture(
        obj9=[0] * 6 + ["U"] * 3,
        base9=[0] * 9,
        dis36=[0] * 36,
    )
    assert caso_4["A_custodia"] == "INDETERMINADO"

    return {
        "caso_1_custodia_apta": caso_1,
        "caso_2_base_no_apta": caso_2,
        "caso_3_diseno_indeterminado": caso_3,
        "caso_4_objetivos_indeterminados": caso_4,
    }


if __name__ == "__main__":
    print(json.dumps(run_cases(), ensure_ascii=False, indent=2))
