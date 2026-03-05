"""
IMMUNO-1/normative_engine.py
=============================
Motor normativo SVperitus–IMMUNO-1  |  versión 0.1

Profilaxis infecciosa y vacunación en adultos con neoplasias hematológicas
e inmunosupresión. Documento 7 de la serie «De SVcustos a SVperitus».

─────────────────────────────────────────────────────────────────────────────
ADVERTENCIA CLÍNICA
  Este motor es una PRÓTESIS COGNITIVA auxiliar para ordenar evidencia
  y visibilizar certeza e incertidumbre. NO sustituye el criterio clínico
  del especialista ni constituye una recomendación terapéutica.

REGLA DURA DE IMPLEMENTACIÓN
  Si un campo clínico está ausente (None), el parámetro se marca "U".
  Nunca se imputa "0" por defecto ante ausencia de datos.

ESTADO DEL MOTOR
  v0.1 — revisado y validado por Watson 400 / Juan Antonio Lloret Egea.
  Abierto a revisión adversarial sobre casos tipo antes de generación
  de dataset sintético completo.
─────────────────────────────────────────────────────────────────────────────

Autor: Juan Antonio Lloret Egea  |  ORCID: 0000-0002-6634-3351
ISSN 2695-641X  |  CC BY-NC-ND 4.0
"""

from __future__ import annotations
from typing import Any

# Tipo de retorno de cada función de parámetro
Ternary = str  # "0" | "1" | "U"

# ── Constantes del módulo ─────────────────────────────────────────────────────
N         = 25
THRESHOLD = 19   # T(25) = floor(7·25/9) = 19
CLASSES   = ("NO_APTO", "INDETERMINADO", "APTO")


# ══════════════════════════════════════════════════════════════════════════════
# UTILIDAD INTERNA
# ══════════════════════════════════════════════════════════════════════════════

def _get(case: dict, key: str) -> Any:
    """
    Devuelve case[key] si existe y no es None; en otro caso None.
    Centraliza el acceso para que ningún parámetro falle silenciosamente.
    """
    return case.get(key, None)


# ══════════════════════════════════════════════════════════════════════════════
# CAPA 1 — ESTADO INMUNITARIO BASAL
# ══════════════════════════════════════════════════════════════════════════════

def P01(case: dict) -> Ternary:
    """
    P01 — Neutropenia actual y riesgo de neutropenia prolongada.

    Campos del caso:
      anc_actual                      (float | None)  células/µL
      anc_expected_nadir              (float | None)  células/µL nadir previsto
      neutropenia_duration_days_expected (int | None) días de neutropenia < 500 previstos

    Regla v0.1 (validada):
      1  si ANC actual < 500
         o ANC nadir previsto < 500 y duración prevista ≥ 7 días
      0  si ANC actual ≥ 1000
         y (ANC nadir previsto ≥ 1000 o ausente o duración prevista < 7 días)
      U  en el resto (ANC 500–999, duración incierta, datos ausentes)
    """
    anc      = _get(case, "anc_actual")
    expected = _get(case, "anc_expected_nadir")
    duration = _get(case, "neutropenia_duration_days_expected")

    # Sin ningún dato de ANC → U
    if anc is None and expected is None:
        return "U"

    # Criterio fuerte de 1
    if anc is not None and anc < 500:
        return "1"
    if expected is not None and expected < 500 and duration is not None and duration >= 7:
        return "1"

    # Criterio de 0: ANC actual ≥ 1000 y sin nadir problemático previsto
    nadir_safe = (expected is None or expected >= 1000 or duration is None or duration < 7)
    if anc is not None and anc >= 1000 and nadir_safe:
        return "0"

    return "U"


def P02(case: dict) -> Ternary:
    """
    P02 — Linfopenia significativa / depleción T.

    Campos del caso:
      cd4_count                    (float | None)  células/µL  [rama preferente]
      lymphocyte_total             (float | None)  células/µL  [proxy si CD4 ausente]
      t_cell_depleting_therapy_12m (bool  | None)

    Regla v0.1 (validada):
      Rama CD4 (preferente si disponible):
        1  si CD4 < 200
        0  si CD4 ≥ 500 y sin terapia depletora T
        U  si CD4 200–499, o depletora T presente, o CD4 ausente con lymph ausente

      Rama linfocitos totales (solo si CD4 ausente):
        1  si lymph < 500
        0  si lymph ≥ 1000 y sin terapia depletora T
        U  si lymph 500–999

    NOTA v0.1: linfocitos totales son proxy imperfecto del riesgo T-celular.
    En v0.2 valorar separar en dos parámetros independientes.
    """
    cd4       = _get(case, "cd4_count")
    lymph     = _get(case, "lymphocyte_total")
    depleting = _get(case, "t_cell_depleting_therapy_12m")

    # Rama CD4 (preferente)
    if cd4 is not None:
        if cd4 < 200:
            return "1"
        if cd4 >= 500 and depleting is not True:
            return "0"
        return "U"  # CD4 200–499, o depletora presente

    # Rama proxy linfocitos totales
    if lymph is not None:
        if lymph < 500:
            return "1"
        if lymph >= 1000 and depleting is not True:
            return "0"
        return "U"

    return "U"


def P03(case: dict) -> Ternary:
    """
    P03 — Hipogammaglobulinemia relevante.

    Campos del caso:
      igg_mgdl                       (float | None)  mg/dL
      bacterial_infections_severe_12m (int  | None)  número de episodios

    Regla v0.1 (validada):
      1  si IgG < 400
         o IgG 400–699 con ≥ 2 infecciones bacterianas graves en 12 meses
      0  si IgG ≥ 700 y < 2 infecciones bacterianas graves
      U  si IgG 400–699 sin historia clara, o IgG ausente
    """
    igg    = _get(case, "igg_mgdl")
    infect = _get(case, "bacterial_infections_severe_12m")

    if igg is None:
        return "U"

    if igg < 400:
        return "1"

    if 400 <= igg < 700:
        if infect is not None and infect >= 2:
            return "1"   # zona gris agravada por historia infecciosa
        return "U"

    # igg >= 700
    if infect is None or infect < 2:
        return "0"
    return "U"  # IgG ≥ 700 pero con historia recurrente: zona gris


def P04(case: dict) -> Ternary:
    """
    P04 — Función esplénica / asplenia.

    Campos del caso:
      anatomic_asplenia             (bool | None)
      functional_hyposplenism       (bool | None)
      encapsulated_vaccines_complete (bool | None)
      asplenia_prophylaxis          (bool | None)

    Regla v0.1 (corrección acordada):
      "0" solo cuando asplenic=False Y hyposplenism=False (bazo funcionante confirmado).
      Si uno es False y el otro None → U.
      Si hay asplenia/hipoesplenismo:
        vacunas OK → 0  (plan preventivo correcto)
        vacunas no OK o sin datos → 1

    NOTA: evalúa adecuación del PLAN PREVENTIVO, no el riesgo residual biológico.
    Asplenia bien gestionada = 0 (plan correcto), no = ausencia de riesgo.
    """
    asplenic     = _get(case, "anatomic_asplenia")
    hyposplenism = _get(case, "functional_hyposplenism")
    vaccine_ok   = _get(case, "encapsulated_vaccines_complete")
    prophylaxis  = _get(case, "asplenia_prophylaxis")

    # Bazo claramente funcionante: ambos False confirmados
    if asplenic is False and hyposplenism is False:
        return "0"

    # Un campo False y el otro None → estado esplénico incompleto
    if (asplenic is False and hyposplenism is None) or \
       (asplenic is None and hyposplenism is False):
        return "U"

    # Sin ningún dato
    if asplenic is None and hyposplenism is None:
        return "U"

    # Asplenia o hipoesplenismo presente (cualquiera True)
    if asplenic is True or hyposplenism is True:
        if vaccine_ok is True:
            return "0"   # plan preventivo correcto
        if vaccine_ok is False or vaccine_ok is None:
            return "1"

    return "U"


def P05(case: dict) -> Ternary:
    """
    P05 — Integridad de barreras y dispositivos vasculares.

    Campos del caso:
      mucositis_grade      (int  | None)  grado OMS/NCI 0–4
      skin_ulcers_relevant (bool | None)
      cvc_present          (bool | None)
      cvc_complications    (bool | None)

    Regla v0.1:
      1  si mucositis ≥ 2, o úlceras relevantes, o CVC con complicaciones
      0  si mucositis < 2 y sin úlceras y (sin CVC o CVC sin complicaciones)
      U  si información incompleta o contradictoria
    """
    mucositis    = _get(case, "mucositis_grade")
    ulcers       = _get(case, "skin_ulcers_relevant")
    cvc          = _get(case, "cvc_present")
    cvc_complic  = _get(case, "cvc_complications")

    if mucositis is None and ulcers is None and cvc is None:
        return "U"

    # Criterios de 1
    if mucositis is not None and mucositis >= 2:
        return "1"
    if ulcers is True:
        return "1"
    if cvc is True and cvc_complic is True:
        return "1"

    # Criterio de 0: todo controlado
    mucositis_ok = mucositis is not None and mucositis < 2
    ulcers_ok    = ulcers is False or ulcers is None
    cvc_ok       = (cvc is False) or (cvc is True and cvc_complic is False)

    if mucositis_ok and ulcers_ok and cvc_ok:
        return "0"

    return "U"


# ══════════════════════════════════════════════════════════════════════════════
# CAPA 2 — NEOPLASIA Y TRATAMIENTO INMUNOSUPRESOR
# ══════════════════════════════════════════════════════════════════════════════

def P06(case: dict) -> Ternary:
    """
    P06 — Tipo y fase de la neoplasia hematológica.

    Campos del caso:
      hematology_phase (str | None)
        Valores esperados: 'induction' | 'consolidation' | 'relapse_high_risk'
                           | 'maintenance' | 'chronic_stable'

    Regla v0.1:
      1  si inducción, consolidación o recaída de alto riesgo
      0  si mantenimiento o fase crónica/estable
      U  si fase no caracterizada o None

    NOTA: P06 y P07 tienen correlación esperada (inducción → quimio intensa).
    Son parámetros independientes pero no ortogonales.
    """
    HIGH_RISK  = {"induction", "consolidation", "relapse_high_risk"}
    LOW_RISK   = {"maintenance", "chronic_stable"}

    phase = _get(case, "hematology_phase")
    if phase is None:
        return "U"
    if phase in HIGH_RISK:
        return "1"
    if phase in LOW_RISK:
        return "0"
    return "U"


def P07(case: dict) -> Ternary:
    """
    P07 — Intensidad y cronología de la quimioterapia.

    Campos del caso:
      chemo_intensity        (str   | None)  'high' | 'standard' | 'low'
      days_since_last_chemo  (int   | None)  días

    Regla v0.1 (validada):
      1  si intensidad 'high' Y días ≤ 30
      0  si intensidad 'low'  Y días > 90
      U  en todos los demás casos:
           - 'standard' sin importar cronología
           - 'high' pero no reciente (> 30 días)
           - 'low' pero reciente (≤ 90 días)
           - cualquier campo None

    NOTA: correlación esperada con P06 (ver P06).
    """
    intensity  = _get(case, "chemo_intensity")
    days_since = _get(case, "days_since_last_chemo")

    if intensity is None or days_since is None:
        return "U"

    if intensity == "high" and days_since <= 30:
        return "1"
    if intensity == "low" and days_since > 90:
        return "0"

    return "U"


def P08(case: dict) -> Ternary:
    """
    P08 — Terapias biológicas dirigidas inmunosupresoras.

    Campos del caso:
      anti_cd20_12m               (bool | None)
      btk_inhibitor_12m           (bool | None)
      pi3k_inhibitor_12m          (bool | None)
      viral_screening_documented  (bool | None)

    Regla v0.1:
      Si hay cualquier terapia de riesgo en últimos 12 meses:
        screening documentado → 0
        screening ausente     → 1
        terapia presente pero sin detalle de screening → U
      Si no hay ninguna terapia de riesgo → 0
      Si todos los campos son None → U
    """
    anti_cd20   = _get(case, "anti_cd20_12m")
    btki        = _get(case, "btk_inhibitor_12m")
    pi3ki       = _get(case, "pi3k_inhibitor_12m")
    screening   = _get(case, "viral_screening_documented")

    if anti_cd20 is None and btki is None and pi3ki is None:
        return "U"

    if anti_cd20 is True or btki is True or pi3ki is True:
        if screening is True:
            return "0"
        if screening is False:
            return "1"
        return "U"   # terapia presente pero screening no documentado

    return "0"   # ninguna terapia de riesgo en últimos 12 meses


def P09(case: dict) -> Ternary:
    """
    P09 — Trasplante hematopoyético (TPH) / CAR-T.

    Campos del caso:
      hsct_allogeneic_years_ago            (float | None)
      hsct_autologous_years_ago            (float | None)
      cart_years_ago                       (float | None)
      gvhd_moderate_severe_active          (bool  | None)
      prophylaxis_revaccination_program    (bool  | None)

    Regla v0.1 (corrección acordada: None en todos los campos → U, no 0):
      TPH alogénico < 2 años, o EICH activa, o CAR-T < 1 año:
        programa OK → 0
        programa ausente/no documentado → 1
      TPH autólogo > 2 años con programa OK → 0
      Todos los campos TPH/CAR-T son None → U
        (no se puede confirmar ausencia de procedimiento)
    """
    hsct_allo  = _get(case, "hsct_allogeneic_years_ago")
    hsct_auto  = _get(case, "hsct_autologous_years_ago")
    cart       = _get(case, "cart_years_ago")
    gvhd       = _get(case, "gvhd_moderate_severe_active")
    program_ok = _get(case, "prophylaxis_revaccination_program")

    # Corrección v0.1: todos None → U (no se puede confirmar ausencia)
    if hsct_allo is None and hsct_auto is None and cart is None:
        return "U"

    # TPH alogénico
    if hsct_allo is not None:
        if hsct_allo < 2 or gvhd is True:
            return "1" if not program_ok else "0"
        if hsct_allo >= 2 and gvhd is False and program_ok is True:
            return "0"
        return "U"

    # CAR-T
    if cart is not None:
        if cart < 1:
            return "1" if not program_ok else "0"
        return "U"

    # TPH autólogo
    if hsct_auto is not None:
        if hsct_auto > 2 and program_ok is True:
            return "0"
        return "U"

    return "U"


def P10(case: dict) -> Ternary:
    """
    P10 — Glucocorticoides sistémicos.

    Campos del caso:
      prednisone_equivalent_mgday    (float | None)
      corticosteroid_duration_weeks  (int   | None)
      pjp_risk_assessed              (bool  | None)

    Regla v0.1 (validada; semántica aclarada):
      pjp_risk_assessed=True significa «riesgo evaluado Y manejo correcto».

      1  si dosis ≥ 20 mg/día durante ≥ 4 semanas Y riesgo NO evaluado/gestionado
      0  si dosis ≥ 20 mg/día durante ≥ 4 semanas Y riesgo SÍ evaluado/gestionado
         o si dosis ≤ 10 mg/día o duración < 2 semanas
      U  si datos ausentes o zona intermedia (10–19 mg ó 2–3 semanas)
    """
    dose  = _get(case, "prednisone_equivalent_mgday")
    weeks = _get(case, "corticosteroid_duration_weeks")
    pjp   = _get(case, "pjp_risk_assessed")

    if dose is None or weeks is None:
        return "U"

    if dose >= 20 and weeks >= 4:
        if pjp is False or pjp is None:
            return "1"
        return "0"   # riesgo presente pero evaluado y gestionado correctamente

    if dose <= 10 or weeks < 2:
        return "0"

    return "U"   # zona intermedia 10–19 mg o 2–3 semanas


# ══════════════════════════════════════════════════════════════════════════════
# CAPA 3 — HISTORIA INFECCIOSA Y COLONIZACIÓN
# ══════════════════════════════════════════════════════════════════════════════

def P11(case: dict) -> Ternary:
    """
    P11 — Infecciones bacterianas graves previas (últimos 12 meses).

    Campos del caso:
      serious_bacterial_infections_12m  (int  | None)
      prophylaxis_plan_reviewed         (bool | None)

    Regla v0.1:
      0  si sin episodios
      1  si ≥ 1 episodio Y plan no revisado
      0  si ≥ 1 episodio Y plan revisado
      U  si datos insuficientes

    NOTA v0.1: redundancia parcial con P25 (plan de monitorización).
    Anotar para análisis de independencia en v0.2.
    """
    episodes    = _get(case, "serious_bacterial_infections_12m")
    plan_review = _get(case, "prophylaxis_plan_reviewed")

    if episodes is None:
        return "U"
    if episodes == 0:
        return "0"
    # episodes >= 1
    if plan_review is True:
        return "0"
    if plan_review is False or plan_review is None:
        return "1"
    return "U"


def P12(case: dict) -> Ternary:
    """
    P12 — Infección fúngica invasora (IFD) previa o contexto de riesgo alto.

    Campos del caso:
      invasive_fungal_infection_history  (bool | None)
      ifi_high_risk_context              (bool | None)
      antifungal_prophylaxis_adequate    (bool | None)

    Regla v0.1 (corrección acordada):
      P12 refleja la «cicatriz» de IFD y el riesgo actual:
        IFD previa + profilaxis adecuada → U
          (antecedente irreversible; la cobertura reduce pero no anula el riesgo)
        IFD previa + profilaxis inadecuada → 1
        Sin IFD previa, contexto alto riesgo + profilaxis inadecuada → 1
        Sin IFD previa, contexto alto riesgo + profilaxis adecuada → 0
        Sin IFD previa, sin contexto de riesgo mayor → 0
      U si información insuficiente

    NOTA: P23 es el evaluador de la adecuación de la profilaxis.
    P12 y P23 comparten campos pero tienen propósito distinto:
    P12 = cicatriz/riesgo histórico; P23 = cobertura actual.
    """
    ifi_history   = _get(case, "invasive_fungal_infection_history")
    high_risk_cx  = _get(case, "ifi_high_risk_context")
    antifungal    = _get(case, "antifungal_prophylaxis_adequate")

    if ifi_history is None and high_risk_cx is None:
        return "U"

    # IFD previa
    if ifi_history is True:
        if antifungal is True:
            return "U"   # cicatriz presente; cobertura reduce pero no anula riesgo
        return "1"       # IFD previa sin cobertura adecuada

    # Sin IFD previa, pero contexto de riesgo alto
    if high_risk_cx is True:
        if antifungal is True:
            return "0"
        return "1"

    # Sin IFD previa y sin contexto de riesgo mayor
    return "0"


def P13(case: dict) -> Ternary:
    """
    P13 — Infecciones virales crónicas / latentes relevantes.

    Campos del caso:
      chronic_viral_infection_active       (bool | None)
      hbv_carrier                          (bool | None)
      anti_cd20_12m                        (bool | None)  [ref. cruzada con P08]
      viral_prophylaxis_monitoring_ok      (bool | None)

    Regla v0.1:
      1  si infección crónica activa O portador VHB con anti-CD20
         Y sin plan de profilaxis/monitorización
      0  si cribado completo y plan correcto, o sin infecciones relevantes
      U  si cribado incompleto o plan no documentado pese a hallazgos
    """
    chronic_viral = _get(case, "chronic_viral_infection_active")
    hbv           = _get(case, "hbv_carrier")
    anti_cd20     = _get(case, "anti_cd20_12m")
    plan_ok       = _get(case, "viral_prophylaxis_monitoring_ok")

    if chronic_viral is None and hbv is None:
        return "U"

    high_risk = chronic_viral is True or (hbv is True and anti_cd20 is True)

    if high_risk:
        if plan_ok is True:
            return "0"
        return "1"

    if plan_ok is True or (chronic_viral is False and hbv is False):
        return "0"

    return "U"


def P14(case: dict) -> Ternary:
    """
    P14 — Colonización por patógenos multirresistentes (MDR).

    Campos del caso:
      mdr_colonization_known    (bool | None)
      mdr_management_strategy   (bool | None)

    Regla v0.1:
      0  si no hay colonización conocida
      1  si colonización conocida Y sin estrategia de manejo
      0  si colonización conocida Y con estrategia definida
      U  si información fragmentaria
    """
    mdr_known = _get(case, "mdr_colonization_known")
    strategy  = _get(case, "mdr_management_strategy")

    if mdr_known is None:
        return "U"
    if mdr_known is False:
        return "0"
    # mdr_known is True
    if strategy is True:
        return "0"
    return "1"


def P15(case: dict) -> Ternary:
    """
    P15 — Exposición sanitaria reciente.

    Campos del caso:
      prolonged_hospitalization_recent  (bool | None)
      icu_admission_recent              (bool | None)
      prophylactic_plan_adjusted        (bool | None)

    Regla v0.1:
      1  si hospitalización prolongada o ingreso UCI reciente Y plan no ajustado
      0  si plan ajustado, o sin exposición sanitaria relevante
      U  si historia asistencial incompleta

    NOTA v0.1: redundancia parcial con P25; anotar para análisis en v0.2.
    """
    prolonged = _get(case, "prolonged_hospitalization_recent")
    icu       = _get(case, "icu_admission_recent")
    adjusted  = _get(case, "prophylactic_plan_adjusted")

    if prolonged is None and icu is None:
        return "U"

    if prolonged is True or icu is True:
        if adjusted is True:
            return "0"
        return "1"

    return "0"


# ══════════════════════════════════════════════════════════════════════════════
# CAPA 4 — ESTADO VACUNAL
# ══════════════════════════════════════════════════════════════════════════════

def P16(case: dict) -> Ternary:
    """
    P16 — Vacunación frente a influenza estacional.

    Campos del caso:
      flu_vaccine_current_season      (bool | None)
      flu_vaccine_contraindicated     (bool | None)

    Regla v0.1:
      0  si vacunado O contraindicado explícitamente
      1  si no vacunado sin contraindicación
      U  si estado desconocido
    """
    vaccinated      = _get(case, "flu_vaccine_current_season")
    contraindicated = _get(case, "flu_vaccine_contraindicated")

    if contraindicated is True:
        return "0"
    if vaccinated is True:
        return "0"
    if vaccinated is False:
        return "1"
    return "U"


def P17(case: dict) -> Ternary:
    """
    P17 — Vacunación frente a neumococo.

    Campos del caso:
      pneumococcal_sequence_complete  (bool | None)
        True = PCV20 o PCV13+PPSV23 con intervalos correctos

    Regla v0.1:
      0  si secuencia completa
      1  si ninguna vacunación registrada
      U  si datos parciales
    """
    sequence_ok = _get(case, "pneumococcal_sequence_complete")

    if sequence_ok is True:
        return "0"
    if sequence_ok is False:
        return "1"
    return "U"


def P18(case: dict) -> Ternary:
    """
    P18 — Vacunación frente a SARS-CoV-2.

    Campos del caso:
      sars_cov2_boosters_current      (bool | None)
      high_risk_hematologic_patient   (bool | None)

    Regla v0.1 (corrección acordada):
      boosters_ok=True → 0 siempre (sin importar nivel de riesgo).
      Alto riesgo + boosters no OK → 1.
      Resto → U.

    NOTA: evalúa pauta primaria + refuerzos recientes, no solo pauta primaria.
    """
    boosters_ok = _get(case, "sars_cov2_boosters_current")
    high_risk   = _get(case, "high_risk_hematologic_patient")

    if boosters_ok is True:
        return "0"

    if high_risk is True and boosters_ok is False:
        return "1"

    return "U"


def P19(case: dict) -> Ternary:
    """
    P19 — Vacunación frente a hepatitis B.

    Campos del caso:
      hbv_vaccine_series_complete      (bool | None)
      anti_hbs_protective              (bool | None)  ≥ 10 UI/L
      hbv_revaccinated_nonresponder    (bool | None)

    Regla v0.1:
      0  si serie completa Y anti-HBs protector
         o si no respondedor Y revacunado
      1  si serie incompleta
         o si serie completa Y anti-HBs no protector Y no revacunado
      U  si vacunación referida sin serología, o viceversa
    """
    vaccine_ok   = _get(case, "hbv_vaccine_series_complete")
    anti_hbs     = _get(case, "anti_hbs_protective")
    revaccinated = _get(case, "hbv_revaccinated_nonresponder")

    if vaccine_ok is None and anti_hbs is None:
        return "U"

    if vaccine_ok is False:
        return "1"

    if vaccine_ok is True:
        if anti_hbs is True:
            return "0"
        if anti_hbs is False:
            return "0" if revaccinated is True else "1"
        return "U"  # serie completa pero sin serología

    return "U"


def P20(case: dict) -> Ternary:
    """
    P20 — Otras vacunas inactivadas relevantes.

    Campos del caso:
      vaccine_calendar_adequate          (bool | None)
      live_vaccine_contraindicated_given (bool | None)

    Regla v0.1:
      1  si se administró vacuna viva contraindicada [error ya cometido,
         no mitigable; 1 = situación inadecuada en curso, no riesgo futuro]
      0  si calendario adecuado al perfil de riesgo
      1  si calendario claramente inadecuado
      U  si información muy parcial

    NOTA: live_vaccine_contraindicated_given=True → error irreversible ya ocurrido.
    """
    calendar_ok       = _get(case, "vaccine_calendar_adequate")
    live_vaccine_err  = _get(case, "live_vaccine_contraindicated_given")

    if live_vaccine_err is True:
        return "1"   # error irreversible en curso

    if calendar_ok is True:
        return "0"
    if calendar_ok is False:
        return "1"
    return "U"


# ══════════════════════════════════════════════════════════════════════════════
# CAPA 5 — PROFILAXIS FARMACOLÓGICA Y SEGUIMIENTO
# ══════════════════════════════════════════════════════════════════════════════

def P21(case: dict) -> Ternary:
    """
    P21 — Profilaxis frente a Pneumocystis jirovecii (PJP).

    Campos del caso:
      pjp_prophylaxis_criteria_met  (bool | None)
      pjp_prophylaxis_active        (bool | None)

    Regla v0.1:
      1  si criterios cumplidos Y sin profilaxis activa
      0  si criterios cumplidos Y profilaxis activa
         o si criterios no cumplidos (no la necesita)
      U  si no se puede establecer si los criterios se cumplen
    """
    criteria = _get(case, "pjp_prophylaxis_criteria_met")
    active   = _get(case, "pjp_prophylaxis_active")

    if criteria is None:
        return "U"
    if criteria is True:
        if active is True:
            return "0"
        return "1"
    return "0"   # criterios no cumplidos → no la necesita


def P22(case: dict) -> Ternary:
    """
    P22 — Profilaxis antiviral (HSV/VZV ± monitorización CMV).

    Campos del caso:
      antiviral_prophylaxis_indicated  (bool | None)
      antiviral_prophylaxis_active     (bool | None)
      cmv_monitoring_active            (bool | None)

    Regla v0.1:
      1  si indicada Y ni profilaxis activa ni monitorización CMV
      0  si indicada Y (profilaxis activa O monitorización CMV)
         o si no indicada
      U  si no se puede determinar el nivel de riesgo
    """
    indicated   = _get(case, "antiviral_prophylaxis_indicated")
    active      = _get(case, "antiviral_prophylaxis_active")
    cmv_monitor = _get(case, "cmv_monitoring_active")

    if indicated is None:
        return "U"
    if indicated is True:
        if active is True or cmv_monitor is True:
            return "0"
        return "1"
    return "0"


def P23(case: dict) -> Ternary:
    """
    P23 — Profilaxis antifúngica.

    Campos del caso:
      ifi_high_risk_context              (bool | None)  [ref. cruzada con P12]
      antifungal_prophylaxis_adequate    (bool | None)

    Regla v0.1 (propósito aclarado):
      P23 es el evaluador de la ADECUACIÓN DE LA COBERTURA ACTUAL.
      P12 registra el antecedente y la cicatriz.

      1  si contexto de riesgo alto Y profilaxis ausente o inadecuada
      0  si contexto de riesgo alto Y profilaxis adecuada
         o si no hay contexto de riesgo alto
      U  si riesgo intermedio o datos incompletos
    """
    high_risk_ifi = _get(case, "ifi_high_risk_context")
    prophylaxis   = _get(case, "antifungal_prophylaxis_adequate")

    if high_risk_ifi is None:
        return "U"
    if high_risk_ifi is True:
        if prophylaxis is True:
            return "0"
        if prophylaxis is False or prophylaxis is None:
            return "1"
    return "0"


def P24(case: dict) -> Ternary:
    """
    P24 — Profilaxis antibacteriana en neutropenia de alto riesgo.

    Campos del caso:
      high_risk_prolonged_neutropenia                (bool | None)
      antibacterial_prophylaxis_policy_documented    (bool | None)

    Regla v0.1:
      1  si neutropenia alto riesgo Y sin política documentada
      0  si neutropenia alto riesgo Y política documentada y razonada
         o si no hay neutropenia de alto riesgo
      U  si no se puede establecer el nivel de riesgo

    NOTA: «política documentada» incluye tanto profilaxis activa como
    decisión explícita de no darla (por resistencias locales u otra razón).
    """
    high_risk = _get(case, "high_risk_prolonged_neutropenia")
    policy    = _get(case, "antibacterial_prophylaxis_policy_documented")

    if high_risk is None:
        return "U"
    if high_risk is True:
        if policy is True:
            return "0"
        return "1"
    return "0"


def P25(case: dict) -> Ternary:
    """
    P25 — Plan estructurado de monitorización y reevaluación del riesgo.

    Campos del caso:
      risk_reassessment_plan_explicit     (bool | None)
      reassessment_periodicity_defined    (bool | None)
      reassessment_includes_vaccines      (bool | None)

    Regla v0.1:
      1  si no existe ningún plan explícito (todo reactivo)
      0  si plan explícito + periodicidad definida + incluye vacunas
      U  si plan existe pero incompleto (solo algunas revisiones sin sistema claro)

    NOTA v0.1: P25 tiene solapamiento conceptual con P11 y P15 en la
    condición «plan revisado». Anotar para análisis de independencia en v0.2.
    """
    plan_explicit      = _get(case, "risk_reassessment_plan_explicit")
    periodicity_set    = _get(case, "reassessment_periodicity_defined")
    includes_vaccines  = _get(case, "reassessment_includes_vaccines")

    if plan_explicit is None:
        return "U"
    if plan_explicit is False:
        return "1"
    # plan_explicit is True
    if periodicity_set is True and includes_vaccines is True:
        return "0"
    return "U"   # plan existe pero incompleto


# ══════════════════════════════════════════════════════════════════════════════
# MOTOR COMPLETO — vector y clasificación global
# ══════════════════════════════════════════════════════════════════════════════

# Tabla de funciones en orden P01–P25 (índice 0 = P01)
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
    Clasifica el vector ternario según la regla SVperitus–IMMUNO-1.

    T(25) = 19

    Devuelve
    --------
    "NO_APTO"       si n₁ ≥ 19
    "APTO"          si n₀ ≥ 19
    "INDETERMINADO" en el resto

    Orden de severidad: NO_APTO > INDETERMINADO > APTO
    """
    n1 = vector.count("1")
    n0 = vector.count("0")

    if n1 >= THRESHOLD:
        return "NO_APTO"
    if n0 >= THRESHOLD:
        return "APTO"
    return "INDETERMINADO"


def evaluate_and_classify(case: dict) -> tuple[list[Ternary], str]:
    """
    Atajo: evalúa el caso y devuelve (vector, clase_global).
    """
    vector = evaluate(case)
    return vector, classify(vector)


def explain(case: dict) -> dict:
    """
    Devuelve un diccionario de trazabilidad completa para un caso.

    Útil para depuración y para la revisión adversarial.

    Devuelve
    --------
    {
      "vector":  {"P01": "0", "P02": "1", ...},
      "counts":  {"n0": int, "n1": int, "nU": int},
      "class":   "NO_APTO" | "INDETERMINADO" | "APTO",
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
