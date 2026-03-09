//! SVperitus — Motor normativo Rust compilado a WebAssembly
//!
//! IMMUNO-1: 108/108 tests de paridad (CONGELADO).
//! IMMUNO-2: port fiel de normative_engine.py fase 2.
//! Meta-célula SV(9,3)-IA: integridad del sistema.
//! Compositor serie: IMMUNO-1 → P25 → IMMUNO-2.
//!
//! Retrocompatible: evaluate_immuno1() y engine_info() no se tocan.
//! Nuevos entry points: evaluate_immuno2(), meta_evaluate(), compose().
//!
//! Γ(v) NO se porta a Rust — se queda en Python y JavaScript.
//!
//! Autor: Juan Antonio Lloret Egea · ORCID 0000-0002-6634-3351
//! ISSN 2695-6411 · CC BY-NC-ND 4.0

use wasm_bindgen::prelude::*;
use serde::{Deserialize, Serialize};

// ═══════════════════════════════════════════════════════════
// CONSTANTS
// ═══════════════════════════════════════════════════════════

const N25: usize = 25;
const T25: usize = 19;
const N9: usize = 9;
const T9: usize = 7;

// IMMUNO-1 clinical thresholds (FROZEN)
const ANC_APT: i32 = 1500;
const ANC_NOT_APT: i32 = 500;
const LYMPH_APT: i32 = 1000;
const LYMPH_NOT_APT: i32 = 200;
const IGG_APT: i32 = 700;
const IGG_NOT_APT: i32 = 400;
const CORTICOID_APT: f64 = 7.5;
const CORTICOID_NOT_APT: f64 = 20.0;

// ═══════════════════════════════════════════════════════════
// TERNARY TYPE
// ═══════════════════════════════════════════════════════════

#[derive(Debug, Clone, Copy, PartialEq)]
enum Ternary { Apt, NotApt, Indeterminate }

impl Ternary {
    fn as_str(&self) -> &'static str {
        match self { Ternary::Apt => "0", Ternary::NotApt => "1",
                     Ternary::Indeterminate => "U" }
    }
    fn radius(&self) -> f64 {
        match self { Ternary::Apt => 1.0, Ternary::NotApt => 2.0,
                     Ternary::Indeterminate => 3.0 }
    }
}

// ═══════════════════════════════════════════════════════════
// SHARED OUTPUT STRUCTURES
// ═══════════════════════════════════════════════════════════

#[derive(Serialize)]
struct TraceEntry {
    param: String,
    value: String,
    radius: f64,
}

#[derive(Serialize)]
struct EvalOutput {
    vector: Vec<String>,
    n0: usize,
    n1: usize,
    #[serde(rename = "nU")]
    n_u: usize,
    global_class: String,
    class_idx: u8,
    trace: Vec<TraceEntry>,
    engine: String,
}

fn build_trace(results: &[Ternary], names: &[&str]) -> Vec<TraceEntry> {
    results.iter().enumerate().map(|(i, &v)| {
        TraceEntry {
            param: names[i].to_string(),
            value: v.as_str().to_string(),
            radius: v.radius(),
        }
    }).collect()
}

fn classify_n25(results: &[Ternary]) -> (&'static str, u8) {
    let n1 = results.iter().filter(|&&v| v == Ternary::NotApt).count();
    let n0 = results.iter().filter(|&&v| v == Ternary::Apt).count();
    if n1 >= T25 { ("NO_APTO", 0u8) }
    else if n0 >= T25 { ("APTO", 2u8) }
    else { ("INDETERMINADO", 1u8) }
}

fn build_eval_output(results: &[Ternary], names: &[&str], engine: &str) -> EvalOutput {
    let n0 = results.iter().filter(|&&v| v == Ternary::Apt).count();
    let n1 = results.iter().filter(|&&v| v == Ternary::NotApt).count();
    let n_u = results.iter().filter(|&&v| v == Ternary::Indeterminate).count();
    let (global_class, class_idx) = classify_n25(results);
    EvalOutput {
        vector: results.iter().map(|v| v.as_str().to_string()).collect(),
        n0, n1, n_u,
        global_class: global_class.to_string(),
        class_idx,
        trace: build_trace(results, names),
        engine: engine.to_string(),
    }
}

const PARAM_NAMES_25: [&str; N25] = [
    "P01","P02","P03","P04","P05","P06","P07","P08","P09","P10",
    "P11","P12","P13","P14","P15","P16","P17","P18","P19","P20",
    "P21","P22","P23","P24","P25",
];

const META_PARAM_NAMES: [&str; N9] = [
    "M1","M2","M3","M4","M5","M6","M7","M8","M9",
];

// ╔═══════════════════════════════════════════════════════════╗
// ║           IMMUNO-1 — FROZEN, DO NOT MODIFY               ║
// ╚═══════════════════════════════════════════════════════════╝

#[derive(Deserialize)]
struct Immuno1Case {
    anc: Option<i32>,
    lymphocytes: Option<i32>,
    igg: Option<i32>,
    spleen_intact: Option<bool>,
    barriers_intact: Option<bool>,
    neoplasia_phase: Option<String>,
    chemo_active: Option<bool>,
    biologic_type: Option<String>,
    tph_cart: Option<String>,
    corticoid_mg: Option<f64>,
    severe_bacterial_12m: Option<bool>,
    prior_ifd: Option<bool>,
    chronic_viral: Option<String>,
    mdr_colonization: Option<bool>,
    recent_healthcare: Option<bool>,
    flu_vaccine: Option<String>,
    pneumo_vaccine: Option<String>,
    covid_vaccine: Option<String>,
    hepb_vaccine: Option<String>,
    other_vaccines: Option<String>,
    pjp_prophylaxis: Option<String>,
    antiviral_prophylaxis: Option<String>,
    antifungal_prophylaxis: Option<String>,
    antibacterial_prophylaxis: Option<String>,
    reevaluation_plan: Option<String>,
}

fn imm1_eval_p01(c: &Immuno1Case) -> Ternary {
    match c.anc { None => Ternary::Indeterminate,
        Some(v) if v >= ANC_APT => Ternary::Apt,
        Some(v) if v < ANC_NOT_APT => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn imm1_eval_p02(c: &Immuno1Case) -> Ternary {
    match c.lymphocytes { None => Ternary::Indeterminate,
        Some(v) if v >= LYMPH_APT => Ternary::Apt,
        Some(v) if v < LYMPH_NOT_APT => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn imm1_eval_p03(c: &Immuno1Case) -> Ternary {
    match c.igg { None => Ternary::Indeterminate,
        Some(v) if v >= IGG_APT => Ternary::Apt,
        Some(v) if v < IGG_NOT_APT => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn imm1_eval_p04(c: &Immuno1Case) -> Ternary {
    match c.spleen_intact { None => Ternary::Indeterminate,
        Some(true) => Ternary::Apt, Some(false) => Ternary::NotApt }
}
fn imm1_eval_p05(c: &Immuno1Case) -> Ternary {
    match c.barriers_intact { None => Ternary::Indeterminate,
        Some(true) => Ternary::Apt, Some(false) => Ternary::NotApt }
}
fn imm1_eval_p06(c: &Immuno1Case) -> Ternary {
    match c.neoplasia_phase.as_deref() { None => Ternary::Indeterminate,
        Some("remission") => Ternary::Apt,
        Some("active") | Some("relapse") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn imm1_eval_p07(c: &Immuno1Case) -> Ternary {
    match c.chemo_active { None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt, Some(false) => Ternary::Apt }
}
fn imm1_eval_p08(c: &Immuno1Case) -> Ternary {
    match c.biologic_type.as_deref() { None => Ternary::Indeterminate,
        Some("none") => Ternary::Apt, Some("anti_cd20") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn imm1_eval_p09(c: &Immuno1Case) -> Ternary {
    match c.tph_cart.as_deref() { None => Ternary::Indeterminate,
        Some("none") => Ternary::Apt,
        Some("allo_tph") | Some("cart") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn imm1_eval_p10(c: &Immuno1Case) -> Ternary {
    match c.corticoid_mg { None => Ternary::Indeterminate,
        Some(mg) if mg < CORTICOID_APT => Ternary::Apt,
        Some(mg) if mg >= CORTICOID_NOT_APT => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn imm1_eval_p11(c: &Immuno1Case) -> Ternary {
    match c.severe_bacterial_12m { None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt, Some(false) => Ternary::Apt }
}
fn imm1_eval_p12(c: &Immuno1Case) -> Ternary {
    match c.prior_ifd { None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt, Some(false) => Ternary::Apt }
}
fn imm1_eval_p13(c: &Immuno1Case) -> Ternary {
    match c.chronic_viral.as_deref() { None => Ternary::Indeterminate,
        Some("none") => Ternary::Apt, Some("active") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn imm1_eval_p14(c: &Immuno1Case) -> Ternary {
    match c.mdr_colonization { None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt, Some(false) => Ternary::Apt }
}
fn imm1_eval_p15(c: &Immuno1Case) -> Ternary {
    match c.recent_healthcare { None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt, Some(false) => Ternary::Apt }
}
fn imm1_eval_vaccine(v: &Option<String>) -> Ternary {
    match v.as_deref() { None => Ternary::Indeterminate,
        Some("current") => Ternary::Apt, Some("none") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn imm1_eval_p16(c: &Immuno1Case) -> Ternary { imm1_eval_vaccine(&c.flu_vaccine) }
fn imm1_eval_p17(c: &Immuno1Case) -> Ternary { imm1_eval_vaccine(&c.pneumo_vaccine) }
fn imm1_eval_p18(c: &Immuno1Case) -> Ternary { imm1_eval_vaccine(&c.covid_vaccine) }
fn imm1_eval_p19(c: &Immuno1Case) -> Ternary {
    match c.hepb_vaccine.as_deref() { None => Ternary::Indeterminate,
        Some("immune") => Ternary::Apt, Some("non_immune") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn imm1_eval_p20(c: &Immuno1Case) -> Ternary {
    match c.other_vaccines.as_deref() { None => Ternary::Indeterminate,
        Some("complete") => Ternary::Apt, Some("incomplete") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn imm1_eval_prophylaxis(v: &Option<String>) -> Ternary {
    match v.as_deref() { None => Ternary::Indeterminate,
        Some("adequate") => Ternary::Apt, Some("inadequate") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn imm1_eval_p21(c: &Immuno1Case) -> Ternary { imm1_eval_prophylaxis(&c.pjp_prophylaxis) }
fn imm1_eval_p22(c: &Immuno1Case) -> Ternary { imm1_eval_prophylaxis(&c.antiviral_prophylaxis) }
fn imm1_eval_p23(c: &Immuno1Case) -> Ternary { imm1_eval_prophylaxis(&c.antifungal_prophylaxis) }
fn imm1_eval_p24(c: &Immuno1Case) -> Ternary { imm1_eval_prophylaxis(&c.antibacterial_prophylaxis) }
fn imm1_eval_p25(c: &Immuno1Case) -> Ternary {
    match c.reevaluation_plan.as_deref() { None => Ternary::Indeterminate,
        Some("structured") => Ternary::Apt, Some("absent") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}

const IMM1_EVALUATORS: [fn(&Immuno1Case) -> Ternary; N25] = [
    imm1_eval_p01, imm1_eval_p02, imm1_eval_p03, imm1_eval_p04, imm1_eval_p05,
    imm1_eval_p06, imm1_eval_p07, imm1_eval_p08, imm1_eval_p09, imm1_eval_p10,
    imm1_eval_p11, imm1_eval_p12, imm1_eval_p13, imm1_eval_p14, imm1_eval_p15,
    imm1_eval_p16, imm1_eval_p17, imm1_eval_p18, imm1_eval_p19, imm1_eval_p20,
    imm1_eval_p21, imm1_eval_p22, imm1_eval_p23, imm1_eval_p24, imm1_eval_p25,
];

/// Internal: evaluate IMMUNO-1 case, return results vector
fn eval_immuno1_internal(case: &Immuno1Case) -> Vec<Ternary> {
    IMM1_EVALUATORS.iter().map(|f| f(case)).collect()
}

// ═══════════════════════════════════════════════════════════
// IMMUNO-1 WASM ENTRY POINTS — FROZEN, IDENTICAL OUTPUT
// ═══════════════════════════════════════════════════════════

/// Evaluate a clinical case (IMMUNO-1). Input: JSON. Output: JSON.
#[wasm_bindgen]
pub fn evaluate_immuno1(json_input: &str) -> String {
    let case: Immuno1Case = match serde_json::from_str(json_input) {
        Ok(c) => c,
        Err(e) => return format!("{{\"error\":\"{}\"}}", e),
    };

    let results = eval_immuno1_internal(&case);
    let output = build_eval_output(&results, &PARAM_NAMES_25, "Rust (WebAssembly)");
    serde_json::to_string(&output).unwrap_or_else(|e| format!("{{\"error\":\"{}\"}}", e))
}

/// Engine info (IMMUNO-1)
#[wasm_bindgen]
pub fn engine_info() -> String {
    r#"{"engine":"Rust (WebAssembly)","module":"IMMUNO-1","n":25,"threshold":19,"parity":"108/108"}"#.to_string()
}

// ╔═══════════════════════════════════════════════════════════╗
// ║           IMMUNO-2 — PORT FROM PYTHON                    ║
// ║           normative_engine.py v0.1                       ║
// ╚═══════════════════════════════════════════════════════════╝

#[derive(Deserialize)]
struct Immuno2Case {
    // Capa 1 — Terreno basal del huésped
    age: Option<i32>,
    dm_complicated: Option<bool>,
    hba1c: Option<f64>,
    heart_failure_nyha: Option<i32>,
    egfr: Option<f64>,
    ischemic_heart_event_12m: Option<bool>,
    fev1_percent_predicted: Option<f64>,
    ild_diagnosed: Option<bool>,
    bronchiectasis: Option<bool>,
    respiratory_exacerbation_12m: Option<bool>,
    fibrosis_stage: Option<i32>,
    cirrhosis: Option<bool>,
    hbv_chronic_active: Option<bool>,
    hcv_viremia: Option<bool>,
    bmi: Option<f64>,
    albumin: Option<f64>,
    frailty_fried: Option<i32>,
    // Capa 2 — Carga y tipo de inmunosupresión
    main_is_drug: Option<String>,
    is_combination: Option<String>,
    prednisone_mg_day: Option<f64>,
    prednisone_duration_weeks: Option<i32>,
    recent_pulse_250mg: Option<bool>,
    is_duration_months: Option<i32>,
    line_changes: Option<i32>,
    lymphocyte_abs: Option<f64>,
    on_rituximab: Option<bool>,
    on_jaki: Option<bool>,
    // Capa 3 — Barreras, dispositivos y anatomía crítica
    skin_mucosa_intact: Option<bool>,
    central_venous_catheter: Option<bool>,
    prosthesis_recent: Option<bool>,
    prosthesis_infected: Option<bool>,
    major_surgery_30d: Option<bool>,
    asplenic: Option<bool>,
    // Capa 4 — Exposición epidemiológica documentable
    hospitalization_48h_30d: Option<bool>,
    mdr_colonization_12m: Option<bool>,
    tb_endemic_exposure: Option<String>,
    respiratory_exposure_4w: Option<bool>,
    fungal_exposure: Option<bool>,
    // Capa 5 — Protección residual, historia infecciosa y puente
    severe_infection_12m: Option<bool>,
    igg_mg_dl: Option<f64>,
    is_escalation_3m: Option<bool>,
    risk_eval_current: Option<String>,
    immuno1_class: Option<String>,  // P25 bridge
}

// ── IMMUNO-2 eval functions P01–P25 ────────────────────────

/// P01 — Edad
fn imm2_eval_p01(c: &Immuno2Case) -> Ternary {
    match c.age {
        None => Ternary::Indeterminate,
        Some(a) if a >= 65 => Ternary::NotApt,
        Some(a) if a >= 18 => Ternary::Apt,
        Some(_) => Ternary::Indeterminate, // <18 fuera de población diana
    }
}

/// P02 — Comorbilidad cardiometabólica y renal
fn imm2_eval_p02(c: &Immuno2Case) -> Ternary {
    let all_none = c.dm_complicated.is_none()
        && c.hba1c.is_none()
        && c.heart_failure_nyha.is_none()
        && c.egfr.is_none()
        && c.ischemic_heart_event_12m.is_none();
    if all_none { return Ternary::Indeterminate; }

    if c.dm_complicated == Some(true) { return Ternary::NotApt; }
    if let Some(h) = c.hba1c { if h >= 8.0 { return Ternary::NotApt; } }
    if let Some(n) = c.heart_failure_nyha { if n >= 2 { return Ternary::NotApt; } }
    if let Some(e) = c.egfr { if e < 60.0 { return Ternary::NotApt; } }
    if c.ischemic_heart_event_12m == Some(true) { return Ternary::NotApt; }

    let has_metabolic = c.dm_complicated.is_some() || c.hba1c.is_some();
    let has_renal = c.egfr.is_some();
    if has_metabolic && has_renal { return Ternary::Apt; }

    Ternary::Indeterminate
}

/// P03 — Enfermedad pulmonar crónica
fn imm2_eval_p03(c: &Immuno2Case) -> Ternary {
    let all_none = c.fev1_percent_predicted.is_none()
        && c.ild_diagnosed.is_none()
        && c.bronchiectasis.is_none()
        && c.respiratory_exacerbation_12m.is_none();
    if all_none { return Ternary::Indeterminate; }

    if let Some(fev1) = c.fev1_percent_predicted { if fev1 < 70.0 { return Ternary::NotApt; } }
    if c.ild_diagnosed == Some(true) { return Ternary::NotApt; }
    if c.bronchiectasis == Some(true) { return Ternary::NotApt; }
    if c.respiratory_exacerbation_12m == Some(true) { return Ternary::NotApt; }

    if c.fev1_percent_predicted.is_some()
        || c.ild_diagnosed.is_some()
        || c.bronchiectasis.is_some()
    {
        return Ternary::Apt;
    }

    Ternary::Indeterminate
}

/// P04 — Hepatopatía crónica
fn imm2_eval_p04(c: &Immuno2Case) -> Ternary {
    let all_none = c.fibrosis_stage.is_none()
        && c.cirrhosis.is_none()
        && c.hbv_chronic_active.is_none()
        && c.hcv_viremia.is_none();
    if all_none { return Ternary::Indeterminate; }

    if c.cirrhosis == Some(true) { return Ternary::NotApt; }
    if let Some(f) = c.fibrosis_stage { if f >= 2 { return Ternary::NotApt; } }
    if c.hbv_chronic_active == Some(true) { return Ternary::NotApt; }
    if c.hcv_viremia == Some(true) { return Ternary::NotApt; }

    if c.fibrosis_stage.is_some()
        || c.hbv_chronic_active.is_some()
        || c.hcv_viremia.is_some()
    {
        return Ternary::Apt;
    }

    Ternary::Indeterminate
}

/// P05 — Estado nutricional y fragilidad
fn imm2_eval_p05(c: &Immuno2Case) -> Ternary {
    let all_none = c.bmi.is_none()
        && c.albumin.is_none()
        && c.frailty_fried.is_none();
    if all_none { return Ternary::Indeterminate; }

    if let Some(b) = c.bmi { if b < 18.5 || b > 35.0 { return Ternary::NotApt; } }
    if let Some(a) = c.albumin { if a < 3.0 { return Ternary::NotApt; } }
    if let Some(f) = c.frailty_fried { if f >= 3 { return Ternary::NotApt; } }

    if let Some(b) = c.bmi {
        if (18.5..=30.0).contains(&b) {
            if let Some(a) = c.albumin {
                if a >= 3.5 { return Ternary::Apt; }
            }
        }
    }

    Ternary::Indeterminate
}

/// P06 — Tipo de fármaco IS principal
fn imm2_eval_p06(c: &Immuno2Case) -> Ternary {
    match c.main_is_drug.as_deref() {
        None => Ternary::Indeterminate,
        Some("jaki") | Some("anti_cd20")
            | Some("cyclophosphamide") | Some("alemtuzumab") => Ternary::NotApt,
        Some("conventional") => Ternary::Apt,
        Some(_) => Ternary::Indeterminate,
    }
}

/// P07 — Combinación de inmunosupresores
fn imm2_eval_p07(c: &Immuno2Case) -> Ternary {
    match c.is_combination.as_deref() {
        None => Ternary::Indeterminate,
        Some("multiple_major") | Some("triple") => Ternary::NotApt,
        Some("monotherapy") | Some("standard_combo") => Ternary::Apt,
        Some(_) => Ternary::Indeterminate,
    }
}

/// P08 — Dosis equivalente de corticoides sistémicos
fn imm2_eval_p08(c: &Immuno2Case) -> Ternary {
    if c.prednisone_mg_day.is_none() && c.recent_pulse_250mg.is_none() {
        return Ternary::Indeterminate;
    }
    if c.recent_pulse_250mg == Some(true) { return Ternary::NotApt; }
    if let Some(dose) = c.prednisone_mg_day {
        if dose >= 15.0 { return Ternary::NotApt; }
        if dose >= 7.5 {
            match c.prednisone_duration_weeks {
                Some(w) if w >= 4 => return Ternary::NotApt,
                None => return Ternary::Indeterminate,
                _ => {} // duration < 4: fall through
            }
        }
        if dose < 7.5 { return Ternary::Apt; }
    }
    Ternary::Indeterminate
}

/// P09 — Duración acumulada de inmunosupresión
fn imm2_eval_p09(c: &Immuno2Case) -> Ternary {
    let dur = match c.is_duration_months {
        None => return Ternary::Indeterminate,
        Some(d) => d,
    };
    let changes = c.line_changes;

    if dur > 6 {
        if let Some(ch) = changes {
            if ch >= 1 { return Ternary::NotApt; }
        }
    }
    if dur <= 6 && (changes.is_none() || changes == Some(0)) {
        return Ternary::Apt;
    }
    if dur > 24 && (changes.is_none() || changes == Some(0)) {
        return Ternary::Apt;
    }
    Ternary::Indeterminate
}

/// P10 — Linfopenia relevante
fn imm2_eval_p10(c: &Immuno2Case) -> Ternary {
    let lymph = match c.lymphocyte_abs {
        None => return Ternary::Indeterminate,
        Some(l) => l,
    };
    if lymph < 500.0 { return Ternary::NotApt; }
    if lymph < 750.0 && (c.on_rituximab == Some(true) || c.on_jaki == Some(true)) {
        return Ternary::NotApt;
    }
    if lymph >= 1000.0 { return Ternary::Apt; }
    Ternary::Indeterminate
}

/// P11 — Integridad de piel y mucosas
fn imm2_eval_p11(c: &Immuno2Case) -> Ternary {
    match c.skin_mucosa_intact {
        None => Ternary::Indeterminate,
        Some(true) => Ternary::Apt,
        Some(false) => Ternary::NotApt,
    }
}

/// P12 — Catéteres venosos centrales
fn imm2_eval_p12(c: &Immuno2Case) -> Ternary {
    match c.central_venous_catheter {
        None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt,
        Some(false) => Ternary::Apt,
    }
}

/// P13 — Prótesis y biomateriales
fn imm2_eval_p13(c: &Immuno2Case) -> Ternary {
    if c.prosthesis_recent.is_none() && c.prosthesis_infected.is_none() {
        return Ternary::Indeterminate;
    }
    if c.prosthesis_infected == Some(true) { return Ternary::NotApt; }
    if c.prosthesis_recent == Some(true) { return Ternary::NotApt; }
    if c.prosthesis_recent == Some(false) { return Ternary::Apt; }
    Ternary::Indeterminate
}

/// P14 — Cirugía mayor reciente
fn imm2_eval_p14(c: &Immuno2Case) -> Ternary {
    match c.major_surgery_30d {
        None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt,
        Some(false) => Ternary::Apt,
    }
}

/// P15 — Esplenectomía o hipoesplenismo funcional
fn imm2_eval_p15(c: &Immuno2Case) -> Ternary {
    match c.asplenic {
        None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt,
        Some(false) => Ternary::Apt,
    }
}

/// P16 — Hospitalización reciente
fn imm2_eval_p16(c: &Immuno2Case) -> Ternary {
    match c.hospitalization_48h_30d {
        None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt,
        Some(false) => Ternary::Apt,
    }
}

/// P17 — Colonización por MDR
fn imm2_eval_p17(c: &Immuno2Case) -> Ternary {
    match c.mdr_colonization_12m {
        None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt,
        Some(false) => Ternary::Apt,
    }
}

/// P18 — Residencia o estancia en zona endémica de TB
fn imm2_eval_p18(c: &Immuno2Case) -> Ternary {
    match c.tb_endemic_exposure.as_deref() {
        None => Ternary::Indeterminate,
        Some("high") | Some("contact") => Ternary::NotApt,
        Some("low") => Ternary::Apt,
        Some(_) => Ternary::Indeterminate,
    }
}

/// P19 — Exposición respiratoria de alto riesgo
fn imm2_eval_p19(c: &Immuno2Case) -> Ternary {
    match c.respiratory_exposure_4w {
        None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt,
        Some(false) => Ternary::Apt,
    }
}

/// P20 — Exposición a entornos de alto riesgo fúngico
fn imm2_eval_p20(c: &Immuno2Case) -> Ternary {
    match c.fungal_exposure {
        None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt,
        Some(false) => Ternary::Apt,
    }
}

/// P21 — Historia de infecciones graves recientes
fn imm2_eval_p21(c: &Immuno2Case) -> Ternary {
    match c.severe_infection_12m {
        None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt,
        Some(false) => Ternary::Apt,
    }
}

/// P22 — Inmunoglobulinas séricas (IgG)
fn imm2_eval_p22(c: &Immuno2Case) -> Ternary {
    match c.igg_mg_dl {
        None => Ternary::Indeterminate,
        Some(igg) if igg >= 700.0 => Ternary::Apt,
        Some(igg) if igg < 400.0 => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate, // 400–699: zona gris
    }
}

/// P23 — Intensificación reciente del régimen IS
fn imm2_eval_p23(c: &Immuno2Case) -> Ternary {
    match c.is_escalation_3m {
        None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt,
        Some(false) => Ternary::Apt,
    }
}

/// P24 — Evaluación integral de riesgo infeccioso
fn imm2_eval_p24(c: &Immuno2Case) -> Ternary {
    match c.risk_eval_current.as_deref() {
        None => Ternary::Indeterminate,
        Some("complete") => Ternary::Apt,
        Some("gaps") | Some("absent") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate,
    }
}

/// P25 — Puente con IMMUNO-1
fn imm2_eval_p25(c: &Immuno2Case) -> Ternary {
    match c.immuno1_class.as_deref() {
        None => Ternary::Indeterminate,
        Some("APTO") => Ternary::Apt,
        Some("NO_APTO") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate, // INDETERMINADO → U
    }
}

const IMM2_EVALUATORS: [fn(&Immuno2Case) -> Ternary; N25] = [
    imm2_eval_p01, imm2_eval_p02, imm2_eval_p03, imm2_eval_p04, imm2_eval_p05,
    imm2_eval_p06, imm2_eval_p07, imm2_eval_p08, imm2_eval_p09, imm2_eval_p10,
    imm2_eval_p11, imm2_eval_p12, imm2_eval_p13, imm2_eval_p14, imm2_eval_p15,
    imm2_eval_p16, imm2_eval_p17, imm2_eval_p18, imm2_eval_p19, imm2_eval_p20,
    imm2_eval_p21, imm2_eval_p22, imm2_eval_p23, imm2_eval_p24, imm2_eval_p25,
];

/// Internal: evaluate IMMUNO-2 case, return results vector
fn eval_immuno2_internal(case: &Immuno2Case) -> Vec<Ternary> {
    IMM2_EVALUATORS.iter().map(|f| f(case)).collect()
}

// ╔═══════════════════════════════════════════════════════════╗
// ║           META-CÉLULA SV(9,3)-IA                         ║
// ╚═══════════════════════════════════════════════════════════╝

#[derive(Deserialize)]
struct MetaState {
    weights_integrity: Option<bool>,
    dataset_provenance: Option<bool>,
    access_control: Option<bool>,
    adversarial_tests: Option<bool>,
    telemetry_active: Option<bool>,
    environment_isolation: Option<bool>,
    immutable_logging: Option<bool>,
    human_oversight: Option<bool>,
    supply_chain_integrity: Option<bool>,
}

fn meta_eval_bool(v: Option<bool>) -> Ternary {
    match v {
        None => Ternary::Indeterminate,
        Some(true) => Ternary::Apt,
        Some(false) => Ternary::NotApt,
    }
}

fn meta_eval_m1(s: &MetaState) -> Ternary { meta_eval_bool(s.weights_integrity) }
fn meta_eval_m2(s: &MetaState) -> Ternary { meta_eval_bool(s.dataset_provenance) }
fn meta_eval_m3(s: &MetaState) -> Ternary { meta_eval_bool(s.access_control) }
fn meta_eval_m4(s: &MetaState) -> Ternary { meta_eval_bool(s.adversarial_tests) }
fn meta_eval_m5(s: &MetaState) -> Ternary { meta_eval_bool(s.telemetry_active) }
fn meta_eval_m6(s: &MetaState) -> Ternary { meta_eval_bool(s.environment_isolation) }
fn meta_eval_m7(s: &MetaState) -> Ternary { meta_eval_bool(s.immutable_logging) }
fn meta_eval_m8(s: &MetaState) -> Ternary { meta_eval_bool(s.human_oversight) }
fn meta_eval_m9(s: &MetaState) -> Ternary { meta_eval_bool(s.supply_chain_integrity) }

const META_EVALUATORS: [fn(&MetaState) -> Ternary; N9] = [
    meta_eval_m1, meta_eval_m2, meta_eval_m3, meta_eval_m4, meta_eval_m5,
    meta_eval_m6, meta_eval_m7, meta_eval_m8, meta_eval_m9,
];

fn eval_meta_internal(state: &MetaState) -> Vec<Ternary> {
    META_EVALUATORS.iter().map(|f| f(state)).collect()
}

fn classify_meta(results: &[Ternary]) -> (&'static str, bool) {
    let n1 = results.iter().filter(|&&v| v == Ternary::NotApt).count();
    let n0 = results.iter().filter(|&&v| v == Ternary::Apt).count();
    if n1 >= T9 { ("INTRUSIÓN", true) }
    else if n0 >= T9 { ("NORMAL", false) }
    else { ("INDETERMINADO", false) }
}

#[derive(Serialize)]
struct MetaOutput {
    vector: Vec<String>,
    n0: usize,
    n1: usize,
    #[serde(rename = "nU")]
    n_u: usize,
    global_class: String,
    vetoed: bool,
    trace: Vec<TraceEntry>,
}

fn build_meta_output(results: &[Ternary]) -> MetaOutput {
    let n0 = results.iter().filter(|&&v| v == Ternary::Apt).count();
    let n1 = results.iter().filter(|&&v| v == Ternary::NotApt).count();
    let n_u = results.iter().filter(|&&v| v == Ternary::Indeterminate).count();
    let (global_class, vetoed) = classify_meta(results);
    MetaOutput {
        vector: results.iter().map(|v| v.as_str().to_string()).collect(),
        n0, n1, n_u,
        global_class: global_class.to_string(),
        vetoed,
        trace: build_trace(results, &META_PARAM_NAMES),
    }
}

// ╔═══════════════════════════════════════════════════════════╗
// ║           COMPOSITOR SERIE                               ║
// ║           IMMUNO-1 → P25 → IMMUNO-2 + Meta-célula        ║
// ╚═══════════════════════════════════════════════════════════╝

#[derive(Serialize)]
struct Immuno2Output {
    vector: Vec<String>,
    n0: usize,
    n1: usize,
    #[serde(rename = "nU")]
    n_u: usize,
    global_class: String,
    class_idx: u8,
    bridge_value: String,
    trace: Vec<TraceEntry>,
    engine: String,
}

#[derive(Serialize)]
struct ComposeOutput {
    immuno1: EvalOutput,
    immuno2: Immuno2Output,
    meta: MetaOutput,
    system_status: String,
}

// ╔═══════════════════════════════════════════════════════════╗
// ║           NEW WASM ENTRY POINTS                          ║
// ╚═══════════════════════════════════════════════════════════╝

/// Evaluate a clinical case (IMMUNO-2). Input: JSON. Output: JSON.
#[wasm_bindgen]
pub fn evaluate_immuno2(json_input: &str) -> String {
    let case: Immuno2Case = match serde_json::from_str(json_input) {
        Ok(c) => c,
        Err(e) => return format!("{{\"error\":\"{}\"}}", e),
    };
    let results = eval_immuno2_internal(&case);
    let output = build_eval_output(&results, &PARAM_NAMES_25, "Rust (WebAssembly) IMMUNO-2");
    serde_json::to_string(&output).unwrap_or_else(|e| format!("{{\"error\":\"{}\"}}", e))
}

/// Evaluate meta-cell SV(9,3)-IA. Input: JSON. Output: JSON.
#[wasm_bindgen]
pub fn meta_evaluate(json_input: &str) -> String {
    let state: MetaState = match serde_json::from_str(json_input) {
        Ok(s) => s,
        Err(e) => return format!("{{\"error\":\"{}\"}}", e),
    };
    let results = eval_meta_internal(&state);
    let output = build_meta_output(&results);
    serde_json::to_string(&output).unwrap_or_else(|e| format!("{{\"error\":\"{}\"}}", e))
}

/// Compositor serie: IMMUNO-1 → P25 → IMMUNO-2 + meta-célula.
/// Inputs: three JSON strings. Output: combined JSON.
///
/// El compositor evalúa IMMUNO-1, inyecta la clase global como P25
/// de IMMUNO-2, evalúa IMMUNO-2 con el puente, y evalúa la meta-célula.
///
/// Si la meta-célula devuelve INTRUSIÓN, system_status = "vetoed".
/// Si INDETERMINADO, system_status = "supervised".
/// Si NORMAL, system_status = "valid".
///
/// Γ(v) NO se calcula aquí — se calcula en JavaScript en el cliente.
#[wasm_bindgen]
pub fn compose(json_immuno1: &str, json_immuno2: &str, json_meta: &str) -> String {
    // ── Paso 1: evaluar IMMUNO-1 ──
    let case1: Immuno1Case = match serde_json::from_str(json_immuno1) {
        Ok(c) => c,
        Err(e) => return format!("{{\"error\":\"IMMUNO-1: {}\"}}", e),
    };
    let results1 = eval_immuno1_internal(&case1);
    let (class1, _) = classify_n25(&results1);

    // ── Paso 2: traducir clase a valor puente ──
    let bridge_value = match class1 {
        "APTO" => "0",
        "NO_APTO" => "1",
        _ => "U",
    };

    // ── Paso 3: evaluar IMMUNO-2 con puente inyectado ──
    let mut case2: Immuno2Case = match serde_json::from_str(json_immuno2) {
        Ok(c) => c,
        Err(e) => return format!("{{\"error\":\"IMMUNO-2: {}\"}}", e),
    };
    // Inyectar puente: si INDETERMINADO, P25 = None → eval lo marca U
    case2.immuno1_class = match class1 {
        "APTO" => Some("APTO".to_string()),
        "NO_APTO" => Some("NO_APTO".to_string()),
        _ => None,
    };
    let results2 = eval_immuno2_internal(&case2);
    let (class2, class2_idx) = classify_n25(&results2);

    // ── Paso 4: evaluar meta-célula ──
    let meta_state: MetaState = match serde_json::from_str(json_meta) {
        Ok(s) => s,
        Err(e) => return format!("{{\"error\":\"Meta: {}\"}}", e),
    };
    let results_meta = eval_meta_internal(&meta_state);
    let (meta_class, vetoed) = classify_meta(&results_meta);

    // ── Paso 5: determinar estado del sistema ──
    let system_status = if vetoed {
        "vetoed"
    } else if meta_class == "INDETERMINADO" {
        "supervised"
    } else {
        "valid"
    };

    // ── Construir salida ──
    let n0_2 = results2.iter().filter(|&&v| v == Ternary::Apt).count();
    let n1_2 = results2.iter().filter(|&&v| v == Ternary::NotApt).count();
    let nu_2 = results2.iter().filter(|&&v| v == Ternary::Indeterminate).count();

    let output = ComposeOutput {
        immuno1: build_eval_output(&results1, &PARAM_NAMES_25, "Rust (WebAssembly) IMMUNO-1"),
        immuno2: Immuno2Output {
            vector: results2.iter().map(|v| v.as_str().to_string()).collect(),
            n0: n0_2,
            n1: n1_2,
            n_u: nu_2,
            global_class: class2.to_string(),
            class_idx: class2_idx,
            bridge_value: bridge_value.to_string(),
            trace: build_trace(&results2, &PARAM_NAMES_25),
            engine: "Rust (WebAssembly) IMMUNO-2".to_string(),
        },
        meta: build_meta_output(&results_meta),
        system_status: system_status.to_string(),
    };

    serde_json::to_string(&output).unwrap_or_else(|e| format!("{{\"error\":\"{}\"}}", e))
}

/// Extended engine info — returns info for all modules
#[wasm_bindgen]
pub fn engine_info_v2() -> String {
    r#"{"engine":"Rust (WebAssembly)","modules":{"immuno1":{"n":25,"threshold":19},"immuno2":{"n":25,"threshold":19},"meta":{"n":9,"threshold":7}},"compositor":"series","gamma":"not_ported_use_js"}"#.to_string()
}
