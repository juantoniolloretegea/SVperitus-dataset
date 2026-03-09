"""
test_parity_rust.py
===================
Genera casos de paridad Python vs Rust para IMMUNO-2, meta-célula y compositor.

Ejecutar: python test_parity_rust.py
Produce: parity_cases.json

Después de compilar el WASM, verificar en navegador o Node.js
que cada caso produce la misma salida que Python.

Autor: Juan Antonio Lloret Egea  |  ORCID: 0000-0002-6634-3351
ISSN 2695-6411  |  CC BY-NC-ND 4.0
"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

import normative_engine as imm2
import gamma as gamma_mod
import meta_engine as meta
import compose as comp

# Importar IMMUNO-1 si está disponible; si no, usar stub
try:
    # Intentar cargar desde la estructura del repo
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "dominios", "inmunologia", "fase_1", "src"))
    import normative_engine as imm1
    HAS_IMM1 = True
except ImportError:
    HAS_IMM1 = False


def make_imm2_case(**kwargs):
    """Crea un caso IMMUNO-2 con todos los campos, rellenando None por defecto."""
    defaults = {
        "age": None, "dm_complicated": None, "hba1c": None,
        "heart_failure_nyha": None, "egfr": None, "ischemic_heart_event_12m": None,
        "fev1_percent_predicted": None, "ild_diagnosed": None,
        "bronchiectasis": None, "respiratory_exacerbation_12m": None,
        "fibrosis_stage": None, "cirrhosis": None,
        "hbv_chronic_active": None, "hcv_viremia": None,
        "bmi": None, "albumin": None, "frailty_fried": None,
        "main_is_drug": None, "is_combination": None,
        "prednisone_mg_day": None, "prednisone_duration_weeks": None,
        "recent_pulse_250mg": None,
        "is_duration_months": None, "line_changes": None,
        "lymphocyte_abs": None, "on_rituximab": None, "on_jaki": None,
        "skin_mucosa_intact": None, "central_venous_catheter": None,
        "prosthesis_recent": None, "prosthesis_infected": None,
        "major_surgery_30d": None, "asplenic": None,
        "hospitalization_48h_30d": None, "mdr_colonization_12m": None,
        "tb_endemic_exposure": None, "respiratory_exposure_4w": None,
        "fungal_exposure": None,
        "severe_infection_12m": None, "igg_mg_dl": None,
        "is_escalation_3m": None, "risk_eval_current": None,
        "immuno1_class": None,
    }
    defaults.update(kwargs)
    return defaults


def make_meta_state(**kwargs):
    defaults = {
        "weights_integrity": None, "dataset_provenance": None,
        "access_control": None, "adversarial_tests": None,
        "telemetry_active": None, "environment_isolation": None,
        "immutable_logging": None, "human_oversight": None,
        "supply_chain_integrity": None,
    }
    defaults.update(kwargs)
    return defaults


def eval_imm2(case):
    """Evalúa caso IMMUNO-2 y devuelve dict de resultado."""
    vector = imm2.evaluate(case)
    cls = imm2.classify(vector)
    return {
        "vector": vector,
        "n0": vector.count("0"),
        "n1": vector.count("1"),
        "nU": vector.count("U"),
        "global_class": cls,
    }


def eval_meta(state):
    """Evalúa meta-célula y devuelve dict de resultado."""
    vector = meta.evaluate(state)
    cls = meta.classify(vector)
    return {
        "vector": vector,
        "n0": vector.count("0"),
        "n1": vector.count("1"),
        "nU": vector.count("U"),
        "global_class": cls,
        "vetoed": cls == "INTRUSIÓN",
    }


def generate_cases():
    """Genera todos los casos de paridad."""
    cases = []

    # ─── IMMUNO-2: Caso todo vacío → todo U → INDETERMINADO ───
    c = make_imm2_case()
    r = eval_imm2(c)
    cases.append({
        "id": "imm2_all_none",
        "module": "immuno2",
        "input": c,
        "expected": r,
    })

    # ─── IMMUNO-2: Caso APTO (19+ ceros) ───
    c = make_imm2_case(
        age=40, dm_complicated=False, egfr=90.0, hba1c=6.0,
        fev1_percent_predicted=95.0,
        fibrosis_stage=0, hbv_chronic_active=False,
        bmi=24.0, albumin=4.0,
        main_is_drug="conventional", is_combination="monotherapy",
        prednisone_mg_day=5.0,
        is_duration_months=3,
        lymphocyte_abs=1500.0,
        skin_mucosa_intact=True, central_venous_catheter=False,
        prosthesis_recent=False, major_surgery_30d=False,
        asplenic=False,
        hospitalization_48h_30d=False, mdr_colonization_12m=False,
        tb_endemic_exposure="low", respiratory_exposure_4w=False,
        fungal_exposure=False,
        severe_infection_12m=False, igg_mg_dl=800.0,
        is_escalation_3m=False, risk_eval_current="complete",
        immuno1_class="APTO",
    )
    r = eval_imm2(c)
    cases.append({
        "id": "imm2_apto_full",
        "module": "immuno2",
        "input": c,
        "expected": r,
    })

    # ─── IMMUNO-2: Caso NO_APTO (19+ unos) ───
    c = make_imm2_case(
        age=70, dm_complicated=True,
        ild_diagnosed=True,
        cirrhosis=True,
        bmi=16.0,
        main_is_drug="jaki", is_combination="triple",
        prednisone_mg_day=20.0,
        is_duration_months=12, line_changes=2,
        lymphocyte_abs=300.0,
        skin_mucosa_intact=False, central_venous_catheter=True,
        prosthesis_infected=True, major_surgery_30d=True,
        asplenic=True,
        hospitalization_48h_30d=True, mdr_colonization_12m=True,
        tb_endemic_exposure="high", respiratory_exposure_4w=True,
        fungal_exposure=True,
        severe_infection_12m=True, igg_mg_dl=200.0,
        is_escalation_3m=True, risk_eval_current="absent",
        immuno1_class="NO_APTO",
    )
    r = eval_imm2(c)
    cases.append({
        "id": "imm2_no_apto_full",
        "module": "immuno2",
        "input": c,
        "expected": r,
    })

    # ─── IMMUNO-2: Caso mixto INDETERMINADO ───
    c = make_imm2_case(
        age=50,
        dm_complicated=False, egfr=70.0,
        main_is_drug="jaki",
        lymphocyte_abs=600.0, on_jaki=True,
        skin_mucosa_intact=True,
        hospitalization_48h_30d=True,
        severe_infection_12m=False,
        immuno1_class="INDETERMINADO",
    )
    r = eval_imm2(c)
    cases.append({
        "id": "imm2_mixed_indet",
        "module": "immuno2",
        "input": c,
        "expected": r,
    })

    # ─── IMMUNO-2: Test P08 corticoides — dosis 7.5, duración 4 ───
    c = make_imm2_case(prednisone_mg_day=7.5, prednisone_duration_weeks=4)
    r = eval_imm2(c)
    cases.append({
        "id": "imm2_p08_75_4w",
        "module": "immuno2",
        "input": c,
        "expected": r,
    })

    # ─── IMMUNO-2: Test P08 corticoides — dosis 7.5, sin duración ───
    c = make_imm2_case(prednisone_mg_day=7.5)
    r = eval_imm2(c)
    cases.append({
        "id": "imm2_p08_75_no_dur",
        "module": "immuno2",
        "input": c,
        "expected": r,
    })

    # ─── IMMUNO-2: Test P08 pulso ───
    c = make_imm2_case(recent_pulse_250mg=True)
    r = eval_imm2(c)
    cases.append({
        "id": "imm2_p08_pulse",
        "module": "immuno2",
        "input": c,
        "expected": r,
    })

    # ─── IMMUNO-2: Test P05 — IMC bajo ───
    c = make_imm2_case(bmi=17.0)
    r = eval_imm2(c)
    cases.append({
        "id": "imm2_p05_low_bmi",
        "module": "immuno2",
        "input": c,
        "expected": r,
    })

    # ─── IMMUNO-2: Test P09 — duración larga sin cambios ───
    c = make_imm2_case(is_duration_months=30, line_changes=0)
    r = eval_imm2(c)
    cases.append({
        "id": "imm2_p09_long_stable",
        "module": "immuno2",
        "input": c,
        "expected": r,
    })

    # ─── IMMUNO-2: Test P10 — linfopenia con rituximab ───
    c = make_imm2_case(lymphocyte_abs=700.0, on_rituximab=True)
    r = eval_imm2(c)
    cases.append({
        "id": "imm2_p10_lymph_rtx",
        "module": "immuno2",
        "input": c,
        "expected": r,
    })

    # ─── IMMUNO-2: Test P22 — IgG zona gris ───
    c = make_imm2_case(igg_mg_dl=500.0)
    r = eval_imm2(c)
    cases.append({
        "id": "imm2_p22_igg_grey",
        "module": "immuno2",
        "input": c,
        "expected": r,
    })

    # ─── IMMUNO-2: Test P25 — puente APTO ───
    c = make_imm2_case(immuno1_class="APTO")
    r = eval_imm2(c)
    cases.append({
        "id": "imm2_p25_apto",
        "module": "immuno2",
        "input": c,
        "expected": r,
    })

    # ─── IMMUNO-2: Test P25 — puente NO_APTO ───
    c = make_imm2_case(immuno1_class="NO_APTO")
    r = eval_imm2(c)
    cases.append({
        "id": "imm2_p25_no_apto",
        "module": "immuno2",
        "input": c,
        "expected": r,
    })

    # ─── META: Todo normal ───
    s = make_meta_state(
        weights_integrity=True, dataset_provenance=True,
        access_control=True, adversarial_tests=True,
        telemetry_active=True, environment_isolation=True,
        immutable_logging=True, human_oversight=True,
        supply_chain_integrity=True,
    )
    r = eval_meta(s)
    cases.append({
        "id": "meta_all_normal",
        "module": "meta",
        "input": s,
        "expected": r,
    })

    # ─── META: Todo comprometido ───
    s = make_meta_state(
        weights_integrity=False, dataset_provenance=False,
        access_control=False, adversarial_tests=False,
        telemetry_active=False, environment_isolation=False,
        immutable_logging=False, human_oversight=False,
        supply_chain_integrity=False,
    )
    r = eval_meta(s)
    cases.append({
        "id": "meta_all_intrusion",
        "module": "meta",
        "input": s,
        "expected": r,
    })

    # ─── META: Todo desconocido ───
    s = make_meta_state()
    r = eval_meta(s)
    cases.append({
        "id": "meta_all_unknown",
        "module": "meta",
        "input": s,
        "expected": r,
    })

    # ─── META: Mixto (7 buenos, 2 malos → NORMAL) ───
    s = make_meta_state(
        weights_integrity=True, dataset_provenance=True,
        access_control=True, adversarial_tests=True,
        telemetry_active=True, environment_isolation=True,
        immutable_logging=True,
        human_oversight=False, supply_chain_integrity=False,
    )
    r = eval_meta(s)
    cases.append({
        "id": "meta_7ok_2bad",
        "module": "meta",
        "input": s,
        "expected": r,
    })

    # ─── META: Mixto (7 malos, 2 buenos → INTRUSIÓN) ───
    s = make_meta_state(
        weights_integrity=False, dataset_provenance=False,
        access_control=False, adversarial_tests=False,
        telemetry_active=False, environment_isolation=False,
        immutable_logging=False,
        human_oversight=True, supply_chain_integrity=True,
    )
    r = eval_meta(s)
    cases.append({
        "id": "meta_7bad_2ok",
        "module": "meta",
        "input": s,
        "expected": r,
    })

    # ─── META: Fronterizo (5 buenos, 2 malos, 2 U → INDETERMINADO) ───
    s = make_meta_state(
        weights_integrity=True, dataset_provenance=True,
        access_control=True, adversarial_tests=True,
        telemetry_active=True,
        environment_isolation=False, immutable_logging=False,
    )
    r = eval_meta(s)
    cases.append({
        "id": "meta_indeterminate",
        "module": "meta",
        "input": s,
        "expected": r,
    })

    return cases


def main():
    cases = generate_cases()
    total = len(cases)
    imm2_count = sum(1 for c in cases if c["module"] == "immuno2")
    meta_count = sum(1 for c in cases if c["module"] == "meta")

    output = {
        "generator": "test_parity_rust.py",
        "description": "Casos de paridad Python vs Rust/WASM para IMMUNO-2 y meta-célula",
        "total_cases": total,
        "immuno2_cases": imm2_count,
        "meta_cases": meta_count,
        "cases": cases,
    }

    with open("parity_cases.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Generados {total} casos de paridad ({imm2_count} IMMUNO-2, {meta_count} meta)")
    print(f"Archivo: parity_cases.json")

    # Resumen de resultados esperados
    for c in cases:
        cls = c["expected"]["global_class"]
        vetoed = c["expected"].get("vetoed", "")
        veto_str = f" (vetoed={vetoed})" if vetoed != "" else ""
        print(f"  {c['id']:30s} → {cls}{veto_str}")


if __name__ == "__main__":
    main()
