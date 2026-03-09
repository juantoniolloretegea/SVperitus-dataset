"""
test_immuno2.py
===============
Tests de paridad para el motor normativo IMMUNO-2.

Casos obligatorios:
  1. APTO limpio (todo favorable)
  2. NO_APTO extremo (todo desfavorable)
  3. INDETERMINADO (mixto)
  4. Todo U (sin datos)
  + Tests por parámetro individual
"""

import sys
sys.path.insert(0, ".")

from normative_engine import (
    evaluate, classify, evaluate_and_classify, explain,
    P01, P02, P03, P04, P05,
    P06, P07, P08, P09, P10,
    P11, P12, P13, P14, P15,
    P16, P17, P18, P19, P20,
    P21, P22, P23, P24, P25,
    N, THRESHOLD, PARAM_IDS,
)

passed = 0
failed = 0

def check(name, got, expected):
    global passed, failed
    if got == expected:
        passed += 1
    else:
        failed += 1
        print(f"  FALLO: {name} → esperado {expected}, obtenido {got}")


# ══════════════════════════════════════════════════════════════════════════════
# CASO 1 — APTO LIMPIO
# Paciente joven, sin comorbilidades, IS convencional leve, todo favorable
# ══════════════════════════════════════════════════════════════════════════════

apto_case = {
    "age": 45,
    "dm_complicated": False, "hba1c": 5.5, "heart_failure_nyha": 0,
    "egfr": 90, "ischemic_heart_event_12m": False,
    "fev1_percent_predicted": 95, "ild_diagnosed": False,
    "bronchiectasis": False, "respiratory_exacerbation_12m": False,
    "fibrosis_stage": 0, "cirrhosis": False,
    "hbv_chronic_active": False, "hcv_viremia": False,
    "bmi": 24, "albumin": 4.2, "frailty_fried": 0,
    "main_is_drug": "conventional",
    "is_combination": "monotherapy",
    "prednisone_mg_day": 5.0, "prednisone_duration_weeks": 2,
    "recent_pulse_250mg": False,
    "is_duration_months": 3, "line_changes": 0,
    "lymphocyte_abs": 1500, "on_rituximab": False, "on_jaki": False,
    "skin_mucosa_intact": True,
    "central_venous_catheter": False,
    "prosthesis_recent": False, "prosthesis_infected": False,
    "major_surgery_30d": False,
    "asplenic": False,
    "hospitalization_48h_30d": False,
    "mdr_colonization_12m": False,
    "tb_endemic_exposure": "low",
    "respiratory_exposure_4w": False,
    "fungal_exposure": False,
    "severe_infection_12m": False,
    "igg_mg_dl": 900,
    "is_escalation_3m": False,
    "risk_eval_current": "complete",
    "immuno1_class": "APTO",
}

print("=== CASO 1: APTO LIMPIO ===")
v1, c1 = evaluate_and_classify(apto_case)
n0 = v1.count("0")
n1 = v1.count("1")
nU = v1.count("U")
check("clase global", c1, "APTO")
check("n0 >= 19", n0 >= 19, True)
check("n1", n1, 0)
check("nU", nU, 0)
check("longitud vector", len(v1), 25)
print(f"  Vector: n0={n0} n1={n1} nU={nU} → {c1}")


# ══════════════════════════════════════════════════════════════════════════════
# CASO 2 — NO_APTO EXTREMO
# Todo desfavorable
# ══════════════════════════════════════════════════════════════════════════════

no_apto_case = {
    "age": 78,
    "dm_complicated": True, "hba1c": 9.5, "heart_failure_nyha": 3,
    "egfr": 25, "ischemic_heart_event_12m": True,
    "fev1_percent_predicted": 45, "ild_diagnosed": True,
    "bronchiectasis": True, "respiratory_exacerbation_12m": True,
    "fibrosis_stage": 4, "cirrhosis": True,
    "hbv_chronic_active": True, "hcv_viremia": True,
    "bmi": 16, "albumin": 2.1, "frailty_fried": 4,
    "main_is_drug": "jaki",
    "is_combination": "triple",
    "prednisone_mg_day": 30, "prednisone_duration_weeks": 12,
    "recent_pulse_250mg": True,
    "is_duration_months": 36, "line_changes": 3,
    "lymphocyte_abs": 300, "on_rituximab": True, "on_jaki": True,
    "skin_mucosa_intact": False,
    "central_venous_catheter": True,
    "prosthesis_recent": True, "prosthesis_infected": True,
    "major_surgery_30d": True,
    "asplenic": True,
    "hospitalization_48h_30d": True,
    "mdr_colonization_12m": True,
    "tb_endemic_exposure": "high",
    "respiratory_exposure_4w": True,
    "fungal_exposure": True,
    "severe_infection_12m": True,
    "igg_mg_dl": 200,
    "is_escalation_3m": True,
    "risk_eval_current": "absent",
    "immuno1_class": "NO_APTO",
}

print("\n=== CASO 2: NO_APTO EXTREMO ===")
v2, c2 = evaluate_and_classify(no_apto_case)
n0 = v2.count("0")
n1 = v2.count("1")
nU = v2.count("U")
check("clase global", c2, "NO_APTO")
check("n1 >= 19", n1 >= 19, True)
check("n0", n0, 0)
check("nU", nU, 0)
print(f"  Vector: n0={n0} n1={n1} nU={nU} → {c2}")


# ══════════════════════════════════════════════════════════════════════════════
# CASO 3 — INDETERMINADO (mixto)
# Algunos favorables, algunos desfavorables, algunos sin dato
# ══════════════════════════════════════════════════════════════════════════════

indet_case = {
    "age": 55,
    "dm_complicated": False, "hba1c": 6.0, "heart_failure_nyha": 0,
    "egfr": 75, "ischemic_heart_event_12m": False,
    "fev1_percent_predicted": 80, "ild_diagnosed": False,
    "bronchiectasis": False, "respiratory_exacerbation_12m": False,
    "fibrosis_stage": 0, "cirrhosis": False,
    "hbv_chronic_active": False, "hcv_viremia": False,
    "bmi": 25, "albumin": 3.8, "frailty_fried": 0,
    "main_is_drug": "jaki",           # → 1
    "is_combination": "monotherapy",   # → 0
    "prednisone_mg_day": 10, "prednisone_duration_weeks": 8,
    "recent_pulse_250mg": False,       # → 1 (≥7.5 ≥4 weeks)
    "is_duration_months": 12, "line_changes": 2,   # → 1
    "lymphocyte_abs": 600, "on_rituximab": False, "on_jaki": True,  # → 1 (<750 + JAKi)
    "skin_mucosa_intact": True,        # → 0
    "central_venous_catheter": False,  # → 0
    "prosthesis_recent": False,        # → 0
    "major_surgery_30d": False,        # → 0
    "asplenic": False,                 # → 0
    "hospitalization_48h_30d": True,   # → 1
    "mdr_colonization_12m": False,     # → 0
    "tb_endemic_exposure": "low",      # → 0
    "respiratory_exposure_4w": False,  # → 0
    "fungal_exposure": False,          # → 0
    "severe_infection_12m": True,      # → 1
    "igg_mg_dl": 550,                  # → U (zona gris)
    "is_escalation_3m": True,          # → 1
    "risk_eval_current": "gaps",       # → 1
    "immuno1_class": "INDETERMINADO",  # → U
}

print("\n=== CASO 3: INDETERMINADO ===")
v3, c3 = evaluate_and_classify(indet_case)
n0 = v3.count("0")
n1 = v3.count("1")
nU = v3.count("U")
check("clase global", c3, "INDETERMINADO")
check("n0 < 19", n0 < 19, True)
check("n1 < 19", n1 < 19, True)
check("nU > 0", nU > 0, True)
print(f"  Vector: n0={n0} n1={n1} nU={nU} → {c3}")
print(f"  Vector detallado: {v3}")


# ══════════════════════════════════════════════════════════════════════════════
# CASO 4 — TODO U (sin datos)
# ══════════════════════════════════════════════════════════════════════════════

empty_case = {}

print("\n=== CASO 4: TODO U ===")
v4, c4 = evaluate_and_classify(empty_case)
n0 = v4.count("0")
n1 = v4.count("1")
nU = v4.count("U")
check("clase global", c4, "INDETERMINADO")
check("n0", n0, 0)
check("n1", n1, 0)
check("nU", nU, 25)
print(f"  Vector: n0={n0} n1={n1} nU={nU} → {c4}")


# ══════════════════════════════════════════════════════════════════════════════
# TESTS POR PARÁMETRO INDIVIDUAL
# ══════════════════════════════════════════════════════════════════════════════

print("\n=== TESTS POR PARÁMETRO ===")

# P01 — Edad
check("P01 joven", P01({"age": 45}), "0")
check("P01 mayor", P01({"age": 70}), "1")
check("P01 None",  P01({}), "U")

# P02 — Comorbilidad
check("P02 sano", P02({"dm_complicated": False, "egfr": 90}), "0")
check("P02 DM",   P02({"dm_complicated": True}), "1")
check("P02 ERC",  P02({"egfr": 40}), "1")
check("P02 None", P02({}), "U")

# P03 — Pulmonar
check("P03 sano", P03({"fev1_percent_predicted": 90, "ild_diagnosed": False}), "0")
check("P03 EPOC", P03({"fev1_percent_predicted": 55}), "1")
check("P03 EPI",  P03({"ild_diagnosed": True}), "1")
check("P03 None", P03({}), "U")

# P04 — Hepatopatía
check("P04 sano",     P04({"fibrosis_stage": 0, "hbv_chronic_active": False}), "0")
check("P04 cirrosis", P04({"cirrhosis": True}), "1")
check("P04 None",     P04({}), "U")

# P05 — Nutrición
check("P05 sano",   P05({"bmi": 24, "albumin": 4.0}), "0")
check("P05 desnut", P05({"bmi": 16}), "1")
check("P05 fragil", P05({"frailty_fried": 4}), "1")
check("P05 None",   P05({}), "U")

# P06 — Tipo IS
check("P06 conv", P06({"main_is_drug": "conventional"}), "0")
check("P06 JAKi", P06({"main_is_drug": "jaki"}), "1")
check("P06 None", P06({}), "U")

# P07 — Combinación
check("P07 mono",   P07({"is_combination": "monotherapy"}), "0")
check("P07 triple", P07({"is_combination": "triple"}), "1")
check("P07 None",   P07({}), "U")

# P08 — Corticoides
check("P08 bajo", P08({"prednisone_mg_day": 3.0}), "0")
check("P08 alto", P08({"prednisone_mg_day": 20.0}), "1")
check("P08 pulso", P08({"recent_pulse_250mg": True}), "1")
check("P08 None", P08({}), "U")

# P09 — Duración IS
check("P09 nuevo",     P09({"is_duration_months": 3, "line_changes": 0}), "0")
check("P09 refract",   P09({"is_duration_months": 12, "line_changes": 2}), "1")
check("P09 estable24", P09({"is_duration_months": 30, "line_changes": 0}), "0")
check("P09 None",      P09({}), "U")

# P10 — Linfopenia
check("P10 normal",    P10({"lymphocyte_abs": 1500}), "0")
check("P10 grave",     P10({"lymphocyte_abs": 300}), "1")
check("P10 jaki_low",  P10({"lymphocyte_abs": 600, "on_jaki": True}), "1")
check("P10 None",      P10({}), "U")

# P11–P15 — Barreras
check("P11 intact", P11({"skin_mucosa_intact": True}), "0")
check("P11 broken", P11({"skin_mucosa_intact": False}), "1")
check("P12 no CVC", P12({"central_venous_catheter": False}), "0")
check("P12 CVC",    P12({"central_venous_catheter": True}), "1")
check("P13 none",   P13({"prosthesis_recent": False}), "0")
check("P13 recent", P13({"prosthesis_recent": True}), "1")
check("P14 no",     P14({"major_surgery_30d": False}), "0")
check("P14 yes",    P14({"major_surgery_30d": True}), "1")
check("P15 spleen", P15({"asplenic": False}), "0")
check("P15 aspl",   P15({"asplenic": True}), "1")

# P16–P20 — Exposición
check("P16 no",  P16({"hospitalization_48h_30d": False}), "0")
check("P16 yes", P16({"hospitalization_48h_30d": True}), "1")
check("P17 no",  P17({"mdr_colonization_12m": False}), "0")
check("P17 yes", P17({"mdr_colonization_12m": True}), "1")
check("P18 low", P18({"tb_endemic_exposure": "low"}), "0")
check("P18 hi",  P18({"tb_endemic_exposure": "high"}), "1")
check("P19 no",  P19({"respiratory_exposure_4w": False}), "0")
check("P19 yes", P19({"respiratory_exposure_4w": True}), "1")
check("P20 no",  P20({"fungal_exposure": False}), "0")
check("P20 yes", P20({"fungal_exposure": True}), "1")

# P21–P25 — Protección y puente
check("P21 no",    P21({"severe_infection_12m": False}), "0")
check("P21 yes",   P21({"severe_infection_12m": True}), "1")
check("P22 ok",    P22({"igg_mg_dl": 900}), "0")
check("P22 low",   P22({"igg_mg_dl": 300}), "1")
check("P22 gray",  P22({"igg_mg_dl": 550}), "U")
check("P23 no",    P23({"is_escalation_3m": False}), "0")
check("P23 yes",   P23({"is_escalation_3m": True}), "1")
check("P24 ok",    P24({"risk_eval_current": "complete"}), "0")
check("P24 gaps",  P24({"risk_eval_current": "gaps"}), "1")
check("P25 apto",  P25({"immuno1_class": "APTO"}), "0")
check("P25 na",    P25({"immuno1_class": "NO_APTO"}), "1")
check("P25 indet", P25({"immuno1_class": "INDETERMINADO"}), "U")
check("P25 None",  P25({}), "U")

# ══════════════════════════════════════════════════════════════════════════════
# TEST: explain() produce estructura correcta
# ══════════════════════════════════════════════════════════════════════════════

print("\n=== TEST explain() ===")
exp = explain(apto_case)
check("explain tiene vector", "vector" in exp, True)
check("explain tiene counts", "counts" in exp, True)
check("explain tiene class", "class" in exp, True)
check("explain tiene threshold", "threshold" in exp, True)
check("explain threshold", exp["threshold"], 19)
check("explain class apto", exp["class"], "APTO")
check("explain 25 params", len(exp["vector"]), 25)

# ══════════════════════════════════════════════════════════════════════════════
# RESUMEN
# ══════════════════════════════════════════════════════════════════════════════

print(f"\n{'='*60}")
print(f"  RESULTADO: {passed} pasados, {failed} fallados de {passed+failed}")
print(f"{'='*60}")

if failed > 0:
    sys.exit(1)
