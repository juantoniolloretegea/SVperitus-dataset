"""
test_compositor_meta.py
=======================
Tests del compositor serie y la meta-celula.
Usa mock engines para aislar la logica del compositor.
Portable: no depende de rutas absolutas del entorno.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import gamma as gamma_module
import meta_engine
from compose import compose
import normative_engine as immuno2_real

passed = 0
failed = 0

def check(name, got, expected):
    global passed, failed
    if got == expected:
        passed += 1
    else:
        failed += 1
        print(f"  FALLO: {name} -> esperado {expected}, obtenido {got}")

class MockEngine:
    """Motor mock que devuelve un vector fijo controlado por el test."""
    N = 25
    THRESHOLD = 19
    def __init__(self, vector):
        self._vector = vector
    def evaluate(self, case):
        return list(self._vector)
    def classify(self, vector):
        n1 = vector.count("1")
        n0 = vector.count("0")
        if n1 >= 19: return "NO_APTO"
        if n0 >= 19: return "APTO"
        return "INDETERMINADO"

# ── META-CELULA ──
print("=== META-CELULA ===")

state_ok = {k: True for k in ["weights_integrity","dataset_provenance","access_control","adversarial_tests","telemetry_active","environment_isolation","immutable_logging","human_oversight","supply_chain_integrity"]}
v_ok, c_ok = meta_engine.evaluate_and_classify(state_ok)
check("meta ok -> NORMAL", c_ok, "NORMAL")
check("meta ok n0=9", v_ok.count("0"), 9)
check("meta not vetoed", meta_engine.is_vetoed(state_ok), False)

state_fail = {k: False for k in state_ok}
v_f, c_f = meta_engine.evaluate_and_classify(state_fail)
check("meta fail -> INTRUSION", c_f, u"INTRUSIÓN")
check("meta fail n1=9", v_f.count("1"), 9)
check("meta vetoed", meta_engine.is_vetoed(state_fail), True)

v_e, c_e = meta_engine.evaluate_and_classify({})
check("meta vacio -> INDET", c_e, "INDETERMINADO")
check("meta vacio nU=9", v_e.count("U"), 9)

exp = meta_engine.explain(state_ok)
check("explain vetoed", exp["vetoed"], False)
check("explain threshold", exp["threshold"], 7)

v_meta_mix = ["0"]*4 + ["1"]*2 + ["U"]*3
g_meta = gamma_module.analyze(v_meta_mix, n=9)
check("meta gamma=0 (frontier)", g_meta["gamma"], 0)

# ── COMPOSITOR: IMMUNO-1 APTO -> P25=0 ──
print("\n=== COMPOSITOR: IMMUNO-1 APTO -> P25=0 ===")

mock1_apto = MockEngine(["0"]*25)

case2 = {
    "age": 45, "dm_complicated": False, "hba1c": 5.5, "heart_failure_nyha": 0,
    "egfr": 90, "ischemic_heart_event_12m": False,
    "fev1_percent_predicted": 95, "ild_diagnosed": False,
    "bronchiectasis": False, "respiratory_exacerbation_12m": False,
    "fibrosis_stage": 0, "cirrhosis": False, "hbv_chronic_active": False, "hcv_viremia": False,
    "bmi": 24, "albumin": 4.2, "frailty_fried": 0,
    "main_is_drug": "conventional", "is_combination": "monotherapy",
    "prednisone_mg_day": 3.0, "prednisone_duration_weeks": 2, "recent_pulse_250mg": False,
    "is_duration_months": 3, "line_changes": 0,
    "lymphocyte_abs": 1500, "on_rituximab": False, "on_jaki": False,
    "skin_mucosa_intact": True, "central_venous_catheter": False,
    "prosthesis_recent": False, "prosthesis_infected": False,
    "major_surgery_30d": False, "asplenic": False,
    "hospitalization_48h_30d": False, "mdr_colonization_12m": False,
    "tb_endemic_exposure": "low", "respiratory_exposure_4w": False, "fungal_exposure": False,
    "severe_infection_12m": False, "igg_mg_dl": 900, "is_escalation_3m": False,
    "risk_eval_current": "complete",
}

r = compose({}, case2, mock1_apto, immuno2_real, gamma_module)
check("I1 APTO", r["immuno1"]["class"], "APTO")
check("bridge=0", r["immuno2"]["bridge_value"], "0")
check("I2 APTO", r["immuno2"]["class"], "APTO")
check("P25=0", r["immuno2"]["vector"][24], "0")
check("g1 None", r["gamma_immuno1"], None)
check("g2 None", r["gamma_immuno2"], None)
print(f"  I1:{r['immuno1']['class']} -> P25={r['immuno2']['bridge_value']} -> I2:{r['immuno2']['class']}")

# ── COMPOSITOR: IMMUNO-1 NO_APTO -> P25=1 ──
print("\n=== COMPOSITOR: IMMUNO-1 NO_APTO -> P25=1 ===")

mock1_na = MockEngine(["1"]*25)
r2 = compose({}, case2, mock1_na, immuno2_real, gamma_module)
check("I1 NO_APTO", r2["immuno1"]["class"], "NO_APTO")
check("bridge=1", r2["immuno2"]["bridge_value"], "1")
check("P25=1", r2["immuno2"]["vector"][24], "1")
print(f"  I1:{r2['immuno1']['class']} -> P25={r2['immuno2']['bridge_value']} -> I2:{r2['immuno2']['class']}")

# ── COMPOSITOR: IMMUNO-1 INDETERMINADO -> P25=U ──
print("\n=== COMPOSITOR: IMMUNO-1 INDET -> P25=U + gamma ===")

mock1_ind = MockEngine(["0"]*10 + ["1"]*5 + ["U"]*10)
case2m = dict(case2)
case2m["main_is_drug"] = "jaki"
case2m["is_escalation_3m"] = True
case2m["igg_mg_dl"] = 550

r3 = compose({}, case2m, mock1_ind, immuno2_real, gamma_module)
check("I1 INDET", r3["immuno1"]["class"], "INDETERMINADO")
check("bridge=U", r3["immuno2"]["bridge_value"], "U")
check("P25=U", r3["immuno2"]["vector"][24], "U")
check("g1 present", r3["gamma_immuno1"] is not None, True)
check("gcomp present", r3["gamma_composition"] is not None, True)

if r3["gamma_immuno1"]:
    print(f"  Gamma I1: {r3['gamma_immuno1']['gamma']} ({r3['gamma_immuno1']['classification']})")
if r3["gamma_composition"]:
    gc = r3["gamma_composition"]
    print(f"  Comp: G2(P25=0)={gc['gamma_bridge_0']}, G2(P25=1)={gc['gamma_bridge_1']}, dG={gc['delta_gamma']}")

# ── P25 NO SE SOBREESCRIBE ──
print("\n=== P25 no override ===")
case2x = dict(case2)
case2x["immuno1_class"] = "APTO"
r4 = compose({}, case2x, mock1_na, immuno2_real, gamma_module)
check("P25 respeta I1", r4["immuno2"]["vector"][24], "1")

# ── RESUMEN ──
print(f"\n{'='*60}")
print(f"  RESULTADO: {passed} pasados, {failed} fallados de {passed+failed}")
print(f"{'='*60}")
if failed > 0:
    sys.exit(1)
