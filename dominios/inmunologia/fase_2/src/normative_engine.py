"""
IMMUNO-2/normative_engine.py
=============================
Motor normativo SVperitus–IMMUNO-2  |  versión 0.1

Estratificación del riesgo de infección grave en adultos con
inmunosupresión farmacológica sistémica no trasplante.

Serie: «Células del Sistema Vector ternario en inmunología clínica»

─────────────────────────────────────────────────────────────────────────────
ADVERTENCIA CLÍNICA
  Este motor es una PRÓTESIS COGNITIVA auxiliar para ordenar evidencia
  y visibilizar certeza e incertidumbre. NO sustituye el criterio clínico
  del especialista ni constituye una recomendación terapéutica.

REGLA DURA DE IMPLEMENTACIÓN
  Si un campo clínico está ausente (None), el parámetro se marca "U".
  Nunca se imputa "0" por defecto ante ausencia de datos.

ESTADO DEL MOTOR
  v0.1 — Capa 1 revisada en profundidad. Capas 2–5 con criterios
  preliminares, pendientes de cotejo individual.
  Abierto a revisión adversarial.

POBLACIÓN DIANA
  Adultos (≥18 años) en tratamiento activo o reciente (≤6 meses) con
  bDMARDs, tsDMARDs o IS convencionales mayores, con o sin corticoides.
  Exclusiones: TOS, TPH/CAR-T, quimioterapia citotóxica pura, VIH primario.
─────────────────────────────────────────────────────────────────────────────

Autor: Juan Antonio Lloret Egea  |  ORCID: 0000-0002-6634-3351
ISSN 2695-6411  |  CC BY-NC-ND 4.0
"""

from __future__ import annotations
from typing import Any

Ternary = str  # "0" | "1" | "U"

# ── Constantes del módulo ─────────────────────────────────────────────────────
N         = 25
THRESHOLD = 19   # T(25) = floor(7·25/9) = 19
CLASSES   = ("NO_APTO", "INDETERMINADO", "APTO")


# ══════════════════════════════════════════════════════════════════════════════
# UTILIDAD INTERNA
# ══════════════════════════════════════════════════════════════════════════════

def _get(case: dict, key: str) -> Any:
    """Devuelve case[key] si existe y no es None; en otro caso None."""
    return case.get(key, None)


# ══════════════════════════════════════════════════════════════════════════════
# CAPA 1 — TERRENO BASAL DEL HUÉSPED (P01–P05)
# Ref principal: Roberts & Fishman, CID 2021 (net state of immunosuppression)
# ══════════════════════════════════════════════════════════════════════════════

def P01(case: dict) -> Ternary:
    """
    P01 — Edad.

    Campos:  age (int | None)

    Regla:
      0  si 18–64 años
      1  si ≥65 años
      U  si edad no verificable

    Ref: Curtis 2012 (tasa 14.2/100pa en ≥65 vs 4.8 en <65).
         ORAL Surveillance (NEJM 2022). RABBIT risk score.
    """
    age = _get(case, "age")
    if age is None:
        return "U"
    if age >= 65:
        return "1"
    if age >= 18:
        return "0"
    return "U"  # <18 fuera de población diana


def P02(case: dict) -> Ternary:
    """
    P02 — Comorbilidad cardiometabólica y renal.

    Campos:
      dm_complicated      (bool | None)  DM con HbA1c ≥8% o complicaciones
      hba1c               (float | None)
      heart_failure_nyha   (int | None)   clase NYHA (0=no, 2,3,4)
      egfr                (float | None)  mL/min/1.73m²
      ischemic_heart_event_12m (bool | None)

    Regla:
      1  si ≥1 de: DM complicada (HbA1c≥8%), ICC ≥II NYHA, ERC eGFR<60,
         cardiopatía isquémica con evento <12m
      0  si ninguna, o comorbilidad menor bien controlada
      U  si comorbilidades no evaluadas, eGFR o HbA1c no disponibles en 6m
    """
    dm   = _get(case, "dm_complicated")
    hba1c = _get(case, "hba1c")
    nyha = _get(case, "heart_failure_nyha")
    egfr = _get(case, "egfr")
    event = _get(case, "ischemic_heart_event_12m")

    # Si no hay ningún dato → U
    if all(v is None for v in [dm, hba1c, nyha, egfr, event]):
        return "U"

    # Criterios de 1
    if dm is True:
        return "1"
    if hba1c is not None and hba1c >= 8.0:
        return "1"
    if nyha is not None and nyha >= 2:
        return "1"
    if egfr is not None and egfr < 60:
        return "1"
    if event is True:
        return "1"

    # Si hay datos suficientes y ninguno dispara 1 → 0
    has_metabolic_data = (dm is not None or hba1c is not None)
    has_renal_data = (egfr is not None)
    if has_metabolic_data and has_renal_data:
        return "0"

    return "U"


def P03(case: dict) -> Ternary:
    """
    P03 — Enfermedad pulmonar crónica.

    Campos:
      fev1_percent_predicted   (float | None)
      ild_diagnosed            (bool | None)   enfermedad pulmonar intersticial
      bronchiectasis           (bool | None)
      respiratory_exacerbation_12m (bool | None)

    Regla:
      1  si EPOC FEV₁<70%, o EPI, o bronquiectasias, o ≥1 exacerbación en 12m
      0  si sin neumopatía crónica estructural
      U  si espirometría no realizada en paciente con síntomas
    """
    fev1   = _get(case, "fev1_percent_predicted")
    ild    = _get(case, "ild_diagnosed")
    bronch = _get(case, "bronchiectasis")
    exac   = _get(case, "respiratory_exacerbation_12m")

    if all(v is None for v in [fev1, ild, bronch, exac]):
        return "U"

    if fev1 is not None and fev1 < 70:
        return "1"
    if ild is True:
        return "1"
    if bronch is True:
        return "1"
    if exac is True:
        return "1"

    # Datos presentes, ningún criterio de 1
    if any(v is not None for v in [fev1, ild, bronch]):
        return "0"

    return "U"


def P04(case: dict) -> Ternary:
    """
    P04 — Hepatopatía crónica.

    Campos:
      fibrosis_stage     (int | None)    F0–F4
      cirrhosis          (bool | None)
      hbv_chronic_active (bool | None)
      hcv_viremia        (bool | None)

    Regla:
      1  si fibrosis ≥F2, o cirrosis, o VHB crónica activa, o VHC con viremia
      0  si sin hepatopatía, o esteatosis simple F0–F1
      U  si serologías VHB/VHC no disponibles o función hepática no evaluada
    """
    fib  = _get(case, "fibrosis_stage")
    cirr = _get(case, "cirrhosis")
    hbv  = _get(case, "hbv_chronic_active")
    hcv  = _get(case, "hcv_viremia")

    if all(v is None for v in [fib, cirr, hbv, hcv]):
        return "U"

    if cirr is True:
        return "1"
    if fib is not None and fib >= 2:
        return "1"
    if hbv is True:
        return "1"
    if hcv is True:
        return "1"

    if any(v is not None for v in [fib, hbv, hcv]):
        return "0"

    return "U"


def P05(case: dict) -> Ternary:
    """
    P05 — Estado nutricional y fragilidad.

    Campos:
      bmi             (float | None)
      albumin         (float | None)  g/dL
      frailty_fried   (int | None)    criterios Fried cumplidos (0–5)

    Regla:
      1  si IMC<18.5 o >35, o albúmina <3.0, o fragilidad ≥3 criterios Fried
      0  si IMC 18.5–30, albúmina ≥3.5, sin fragilidad
      U  si IMC o albúmina no disponibles, o fragilidad no evaluada en ≥70a
    """
    bmi   = _get(case, "bmi")
    alb   = _get(case, "albumin")
    frail = _get(case, "frailty_fried")

    if all(v is None for v in [bmi, alb, frail]):
        return "U"

    if bmi is not None and (bmi < 18.5 or bmi > 35):
        return "1"
    if alb is not None and alb < 3.0:
        return "1"
    if frail is not None and frail >= 3:
        return "1"

    if bmi is not None and 18.5 <= bmi <= 30:
        if alb is not None and alb >= 3.5:
            return "0"

    return "U"


# ══════════════════════════════════════════════════════════════════════════════
# CAPA 2 — CARGA Y TIPO DE INMUNOSUPRESIÓN (P06–P10)
# Ref principal: ORAL Surveillance (NEJM 2022), Curtis 2012, Singh 2015
# Estado: criterios preliminares, pendientes de cotejo
# ══════════════════════════════════════════════════════════════════════════════

def P06(case: dict) -> Ternary:
    """
    P06 — Tipo de fármaco inmunosupresor principal.

    Campos:
      main_is_drug  (str | None)  "conventional", "jaki", "anti_cd20",
                                   "cyclophosphamide", "alemtuzumab", "other"

    Regla:
      1  si JAKi, anti-CD20, ciclofosfamida o alemtuzumab
      0  si IS convencional en monoterapia a dosis estándar
      U  si fármaco no documentado o no clasificable
    """
    drug = _get(case, "main_is_drug")
    if drug is None:
        return "U"
    if drug in ("jaki", "anti_cd20", "cyclophosphamide", "alemtuzumab"):
        return "1"
    if drug == "conventional":
        return "0"
    return "U"


def P07(case: dict) -> Ternary:
    """
    P07 — Combinación de inmunosupresores.

    Campos:
      is_combination  (str | None)  "monotherapy", "standard_combo",
                                     "multiple_major", "triple"

    Regla:
      1  si ≥2 IS mayores simultáneos o triple terapia
      0  si monoterapia o bDMARD + MTX estándar
      U  si régimen no documentado
    """
    combo = _get(case, "is_combination")
    if combo is None:
        return "U"
    if combo in ("multiple_major", "triple"):
        return "1"
    if combo in ("monotherapy", "standard_combo"):
        return "0"
    return "U"


def P08(case: dict) -> Ternary:
    """
    P08 — Dosis equivalente de corticoides sistémicos.

    Campos:
      prednisone_mg_day      (float | None)
      prednisone_duration_weeks (int | None)
      recent_pulse_250mg     (bool | None)  ≥250mg metilprednisolona en último mes

    Regla:
      1  si ≥7.5 mg/d mantenida ≥4 semanas, o ≥15 mg/d cualquier duración,
         o pulsos recientes
      0  si sin corticoides, o <7.5 mg/d <4 semanas
      U  si dosis no documentada
    """
    dose     = _get(case, "prednisone_mg_day")
    duration = _get(case, "prednisone_duration_weeks")
    pulse    = _get(case, "recent_pulse_250mg")

    if dose is None and pulse is None:
        return "U"

    if pulse is True:
        return "1"
    if dose is not None and dose >= 15:
        return "1"
    if dose is not None and dose >= 7.5:
        if duration is not None and duration >= 4:
            return "1"
        if duration is None:
            return "U"
    if dose is not None and dose < 7.5:
        return "0"

    return "U"


def P09(case: dict) -> Ternary:
    """
    P09 — Duración acumulada de inmunosupresión.

    Campos:
      is_duration_months  (int | None)
      line_changes        (int | None)  cambios de línea por fallo/toxicidad

    Regla:
      1  si IS continua >6 meses con ≥1 cambio de línea
      0  si inicio reciente ≤6 meses (primer régimen), o estable >24 meses sin complicaciones
      U  si duración no documentable
    """
    dur    = _get(case, "is_duration_months")
    changes = _get(case, "line_changes")

    if dur is None:
        return "U"

    if dur > 6 and changes is not None and changes >= 1:
        return "1"
    if dur <= 6 and (changes is None or changes == 0):
        return "0"
    if dur > 24 and (changes is None or changes == 0):
        return "0"

    return "U"


def P10(case: dict) -> Ternary:
    """
    P10 — Linfopenia relevante.

    Campos:
      lymphocyte_abs  (float | None)  células/µL
      on_rituximab    (bool | None)
      on_jaki         (bool | None)

    Regla:
      1  si linfocitos <500 mantenidos, o <750 en contexto de rituximab/JAKi
      0  si linfocitos ≥1000
      U  si recuento no disponible en últimos 3 meses
    """
    lymph = _get(case, "lymphocyte_abs")
    rtx   = _get(case, "on_rituximab")
    jaki  = _get(case, "on_jaki")

    if lymph is None:
        return "U"

    if lymph < 500:
        return "1"
    if lymph < 750 and (rtx is True or jaki is True):
        return "1"
    if lymph >= 1000:
        return "0"

    return "U"


# ══════════════════════════════════════════════════════════════════════════════
# CAPA 3 — BARRERAS, DISPOSITIVOS Y ANATOMÍA CRÍTICA (P11–P15)
# Ref principal: Fishman 2017, IDSA guidelines
# Estado: criterios preliminares, pendientes de cotejo
# ══════════════════════════════════════════════════════════════════════════════

def P11(case: dict) -> Ternary:
    """
    P11 — Integridad de piel y mucosas.

    Campos:
      skin_mucosa_intact  (bool | None)

    Regla:
      0  si piel y mucosas íntegras
      1  si úlceras, mucositis activa, heridas no cicatrizadas
      U  si no explorado o no documentado
    """
    intact = _get(case, "skin_mucosa_intact")
    if intact is None:
        return "U"
    return "0" if intact else "1"


def P12(case: dict) -> Ternary:
    """
    P12 — Catéteres venosos centrales y dispositivos intravasculares.

    Campos:
      central_venous_catheter  (bool | None)

    Regla:
      0  si sin catéter venoso central ni dispositivos intravasculares permanentes
      1  si port-a-cath, PICC, Hickman o catéter de hemodiálisis
      U  si presencia no verificable
    """
    cvc = _get(case, "central_venous_catheter")
    if cvc is None:
        return "U"
    return "1" if cvc else "0"


def P13(case: dict) -> Ternary:
    """
    P13 — Prótesis y biomateriales.

    Campos:
      prosthesis_recent   (bool | None)  implantada <12 meses
      prosthesis_infected (bool | None)  historia de infección periprotésica

    Regla:
      0  si sin prótesis, o prótesis >12 meses sin complicaciones
      1  si prótesis <12 meses, o historia de infección periprotésica
      U  si estado protésico no documentado
    """
    recent   = _get(case, "prosthesis_recent")
    infected = _get(case, "prosthesis_infected")

    if recent is None and infected is None:
        return "U"
    if infected is True:
        return "1"
    if recent is True:
        return "1"
    if recent is False:
        return "0"
    return "U"


def P14(case: dict) -> Ternary:
    """
    P14 — Cirugía mayor reciente.

    Campos:
      major_surgery_30d  (bool | None)

    Regla:
      0  si sin cirugía mayor en últimos 30 días
      1  si cirugía mayor en últimos 30 días
      U  si historial quirúrgico no disponible
    """
    surg = _get(case, "major_surgery_30d")
    if surg is None:
        return "U"
    return "1" if surg else "0"


def P15(case: dict) -> Ternary:
    """
    P15 — Esplenectomía o hipoesplenismo funcional.

    Campos:
      asplenic  (bool | None)

    Regla:
      0  si bazo presente y funcionante
      1  si esplenectomía o hipoesplenismo funcional documentado
      U  si función esplénica no evaluada en paciente con riesgo

    Nota: solapamiento aceptado con P04 de IMMUNO-1.
    """
    asp = _get(case, "asplenic")
    if asp is None:
        return "U"
    return "1" if asp else "0"


# ══════════════════════════════════════════════════════════════════════════════
# CAPA 4 — EXPOSICIÓN EPIDEMIOLÓGICA DOCUMENTABLE (P16–P20)
# Ref principal: Fishman 2017, IDSA 2024 AMR guidance, EULAR 2022
# Estado: criterios preliminares, pendientes de cotejo
# ══════════════════════════════════════════════════════════════════════════════

def P16(case: dict) -> Ternary:
    """
    P16 — Hospitalización reciente.

    Campos:
      hospitalization_48h_30d  (bool | None)

    Regla:
      0  si sin hospitalización ≥48h en últimos 30 días
      1  si ≥1 hospitalización ≥48h en últimos 30 días
      U  si historial de ingresos no verificable
    """
    hosp = _get(case, "hospitalization_48h_30d")
    if hosp is None:
        return "U"
    return "1" if hosp else "0"


def P17(case: dict) -> Ternary:
    """
    P17 — Colonización conocida por microorganismos multirresistentes.

    Campos:
      mdr_colonization_12m  (bool | None)

    Regla:
      0  si sin colonización MDR conocida en últimos 12 meses
      1  si colonización documentada (MRSA, BLEE, EPC, VRE)
      U  si sin cribado en paciente con exposición hospitalaria frecuente
    """
    mdr = _get(case, "mdr_colonization_12m")
    if mdr is None:
        return "U"
    return "1" if mdr else "0"


def P18(case: dict) -> Ternary:
    """
    P18 — Residencia o estancia en zona endémica de tuberculosis.

    Campos:
      tb_endemic_exposure  (str | None)  "low", "high", "contact"

    Regla:
      0  si baja endemia TB (<10/100.000), sin viajes a alta endemia
      1  si residencia/estancia ≥1 mes en alta endemia (≥40/100.000) en 2 años,
         o contacto estrecho con TB activa
      U  si historia de viajes no recogida, o IGRA/TST no realizado
    """
    tb = _get(case, "tb_endemic_exposure")
    if tb is None:
        return "U"
    if tb in ("high", "contact"):
        return "1"
    if tb == "low":
        return "0"
    return "U"


def P19(case: dict) -> Ternary:
    """
    P19 — Exposición documentada a infecciones respiratorias de alto riesgo.

    Campos:
      respiratory_exposure_4w  (bool | None)

    Regla:
      0  si sin exposición conocida en últimas 4 semanas
      1  si contacto estrecho documentado con TB bacilífera, COVID grave,
         influenza en brote nosocomial, u otra de declaración obligatoria
      U  si exposición no evaluable
    """
    exp = _get(case, "respiratory_exposure_4w")
    if exp is None:
        return "U"
    return "1" if exp else "0"


def P20(case: dict) -> Ternary:
    """
    P20 — Exposición a entornos de alto riesgo fúngico.

    Campos:
      fungal_exposure  (bool | None)

    Regla:
      0  si sin exposición a obras hospitalarias, excavaciones, zonas endémicas
      1  si exposición documentada a riesgo fúngico ambiental
      U  si exposición ambiental no evaluada
    """
    fungal = _get(case, "fungal_exposure")
    if fungal is None:
        return "U"
    return "1" if fungal else "0"


# ══════════════════════════════════════════════════════════════════════════════
# CAPA 5 — PROTECCIÓN RESIDUAL, HISTORIA INFECCIOSA Y PUENTE IMMUNO-1 (P21–P25)
# Estado: criterios preliminares, pendientes de cotejo
# ══════════════════════════════════════════════════════════════════════════════

def P21(case: dict) -> Ternary:
    """
    P21 — Historia de infecciones graves recientes.

    Campos:
      severe_infection_12m  (bool | None)

    Regla:
      0  si sin infección grave (hospitalización o IV) en últimos 12 meses
      1  si ≥1 infección grave en últimos 12 meses
      U  si historial infeccioso no disponible
    """
    inf = _get(case, "severe_infection_12m")
    if inf is None:
        return "U"
    return "1" if inf else "0"


def P22(case: dict) -> Ternary:
    """
    P22 — Inmunoglobulinas séricas (IgG).

    Campos:
      igg_mg_dl  (float | None)

    Regla:
      0  si IgG ≥700 mg/dL
      1  si IgG <400 mg/dL
      U  si IgG no determinada, o IgG 400–699 (zona gris sin consenso)
    """
    igg = _get(case, "igg_mg_dl")
    if igg is None:
        return "U"
    if igg >= 700:
        return "0"
    if igg < 400:
        return "1"
    return "U"  # zona 400–699: incertidumbre documentada


def P23(case: dict) -> Ternary:
    """
    P23 — Intensificación reciente del régimen inmunosupresor.

    Campos:
      is_escalation_3m  (bool | None)

    Regla:
      0  si régimen estable ≥3 meses sin cambios
      1  si adición o escalada significativa en últimos 3 meses
      U  si historial de cambios no documentado
    """
    esc = _get(case, "is_escalation_3m")
    if esc is None:
        return "U"
    return "1" if esc else "0"


def P24(case: dict) -> Ternary:
    """
    P24 — Intervalo desde última evaluación integral de riesgo infeccioso.

    Campos:
      risk_eval_current  (str | None)  "complete", "gaps", "absent"

    Regla:
      0  si evaluación documentada y vigente (≤12 meses)
      1  si sin evaluación >12 meses, o con gaps no resueltos
      U  si no se puede verificar
    """
    ev = _get(case, "risk_eval_current")
    if ev is None:
        return "U"
    if ev == "complete":
        return "0"
    if ev in ("gaps", "absent"):
        return "1"
    return "U"


def P25(case: dict) -> Ternary:
    """
    P25 — Parámetro puente con IMMUNO-1.

    Campos:
      immuno1_class  (str | None)  "APTO", "NO_APTO", "INDETERMINADO"

    Regla:
      0  si IMMUNO-1 clasifica APTO y evaluación vigente (≤12 meses)
      1  si IMMUNO-1 clasifica NO_APTO, o evaluación desactualizada, o ausente
      U  si IMMUNO-1 no aplicado o información inaccesible

    NOTA: En modo compositor, este campo lo inyecta automáticamente
    el compositor a partir de la salida de IMMUNO-1. El usuario no
    lo rellena manualmente.
    """
    cls = _get(case, "immuno1_class")
    if cls is None:
        return "U"
    if cls == "APTO":
        return "0"
    if cls == "NO_APTO":
        return "1"
    return "U"  # INDETERMINADO o cualquier otro valor


# ══════════════════════════════════════════════════════════════════════════════
# MOTOR COMPLETO — vector y clasificación global
# ══════════════════════════════════════════════════════════════════════════════

_PARAM_FUNCTIONS = [
    P01, P02, P03, P04, P05,   # Capa 1
    P06, P07, P08, P09, P10,   # Capa 2
    P11, P12, P13, P14, P15,   # Capa 3
    P16, P17, P18, P19, P20,   # Capa 4
    P21, P22, P23, P24, P25,   # Capa 5
]

PARAM_IDS = [f"P{i:02d}" for i in range(1, 26)]


def evaluate(case: dict) -> list[Ternary]:
    """
    Evalúa el caso clínico y devuelve el vector ternario P01…P25.

    Parámetro
    ---------
    case : dict con los campos clínicos definidos en cada función P_k.

    Devuelve
    --------
    Lista de 25 strings, cada uno "0", "1" o "U".
    """
    return [fn(case) for fn in _PARAM_FUNCTIONS]


def classify(vector: list[Ternary]) -> str:
    """
    Clasifica el vector ternario según la regla SVperitus–IMMUNO-2.

    T(25) = 19

    Devuelve
    --------
    "NO_APTO"       si n₁ ≥ 19
    "APTO"          si n₀ ≥ 19
    "INDETERMINADO" en el resto
    """
    n1 = vector.count("1")
    n0 = vector.count("0")

    if n1 >= THRESHOLD:
        return "NO_APTO"
    if n0 >= THRESHOLD:
        return "APTO"
    return "INDETERMINADO"


def evaluate_and_classify(case: dict) -> tuple[list[Ternary], str]:
    """Atajo: evalúa el caso y devuelve (vector, clase_global)."""
    vector = evaluate(case)
    return vector, classify(vector)


def explain(case: dict) -> dict:
    """
    Devuelve un diccionario de trazabilidad completa para un caso.

    Devuelve
    --------
    {
      "vector":    {"P01": "0", "P02": "1", ...},
      "counts":    {"n0": int, "n1": int, "nU": int},
      "class":     "NO_APTO" | "INDETERMINADO" | "APTO",
      "threshold": 19,
    }
    """
    vector = evaluate(case)
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
    }
