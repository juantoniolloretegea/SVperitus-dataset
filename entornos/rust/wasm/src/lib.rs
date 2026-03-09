//! SVperitus IMMUNO-1 — Motor normativo Rust compilado a WebAssembly
//!
//! Misma lógica que svperitus_playground_v03_final.rs (108/108 tests).
//! Expuesto al navegador via wasm-bindgen.
//! Lógica clínica CONGELADA — no modificar hasta cotejo adversarial.

use wasm_bindgen::prelude::*;
use serde::{Deserialize, Serialize};

// ═══════════════════════════════════════════════════════════
// CONSTANTS (centralized, identical to playground v0.3)
// ═══════════════════════════════════════════════════════════

const N: usize = 25;
const T25: usize = 19;

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
// CASE STRUCTURE
// ═══════════════════════════════════════════════════════════

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

// ═══════════════════════════════════════════════════════════
// EVAL FUNCTIONS P01-P25 (FROZEN — identical to playground)
// ═══════════════════════════════════════════════════════════

fn eval_p01(c: &Immuno1Case) -> Ternary {
    match c.anc { None => Ternary::Indeterminate,
        Some(v) if v >= ANC_APT => Ternary::Apt,
        Some(v) if v < ANC_NOT_APT => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn eval_p02(c: &Immuno1Case) -> Ternary {
    match c.lymphocytes { None => Ternary::Indeterminate,
        Some(v) if v >= LYMPH_APT => Ternary::Apt,
        Some(v) if v < LYMPH_NOT_APT => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn eval_p03(c: &Immuno1Case) -> Ternary {
    match c.igg { None => Ternary::Indeterminate,
        Some(v) if v >= IGG_APT => Ternary::Apt,
        Some(v) if v < IGG_NOT_APT => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn eval_p04(c: &Immuno1Case) -> Ternary {
    match c.spleen_intact { None => Ternary::Indeterminate,
        Some(true) => Ternary::Apt, Some(false) => Ternary::NotApt }
}
fn eval_p05(c: &Immuno1Case) -> Ternary {
    match c.barriers_intact { None => Ternary::Indeterminate,
        Some(true) => Ternary::Apt, Some(false) => Ternary::NotApt }
}
fn eval_p06(c: &Immuno1Case) -> Ternary {
    match c.neoplasia_phase.as_deref() { None => Ternary::Indeterminate,
        Some("remission") => Ternary::Apt,
        Some("active") | Some("relapse") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn eval_p07(c: &Immuno1Case) -> Ternary {
    match c.chemo_active { None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt, Some(false) => Ternary::Apt }
}
fn eval_p08(c: &Immuno1Case) -> Ternary {
    match c.biologic_type.as_deref() { None => Ternary::Indeterminate,
        Some("none") => Ternary::Apt, Some("anti_cd20") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn eval_p09(c: &Immuno1Case) -> Ternary {
    match c.tph_cart.as_deref() { None => Ternary::Indeterminate,
        Some("none") => Ternary::Apt,
        Some("allo_tph") | Some("cart") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn eval_p10(c: &Immuno1Case) -> Ternary {
    match c.corticoid_mg { None => Ternary::Indeterminate,
        Some(mg) if mg < CORTICOID_APT => Ternary::Apt,
        Some(mg) if mg >= CORTICOID_NOT_APT => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn eval_p11(c: &Immuno1Case) -> Ternary {
    match c.severe_bacterial_12m { None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt, Some(false) => Ternary::Apt }
}
fn eval_p12(c: &Immuno1Case) -> Ternary {
    match c.prior_ifd { None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt, Some(false) => Ternary::Apt }
}
fn eval_p13(c: &Immuno1Case) -> Ternary {
    match c.chronic_viral.as_deref() { None => Ternary::Indeterminate,
        Some("none") => Ternary::Apt, Some("active") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn eval_p14(c: &Immuno1Case) -> Ternary {
    match c.mdr_colonization { None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt, Some(false) => Ternary::Apt }
}
fn eval_p15(c: &Immuno1Case) -> Ternary {
    match c.recent_healthcare { None => Ternary::Indeterminate,
        Some(true) => Ternary::NotApt, Some(false) => Ternary::Apt }
}
fn eval_vaccine(v: &Option<String>) -> Ternary {
    match v.as_deref() { None => Ternary::Indeterminate,
        Some("current") => Ternary::Apt, Some("none") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn eval_p16(c: &Immuno1Case) -> Ternary { eval_vaccine(&c.flu_vaccine) }
fn eval_p17(c: &Immuno1Case) -> Ternary { eval_vaccine(&c.pneumo_vaccine) }
fn eval_p18(c: &Immuno1Case) -> Ternary { eval_vaccine(&c.covid_vaccine) }
fn eval_p19(c: &Immuno1Case) -> Ternary {
    match c.hepb_vaccine.as_deref() { None => Ternary::Indeterminate,
        Some("immune") => Ternary::Apt, Some("non_immune") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn eval_p20(c: &Immuno1Case) -> Ternary {
    match c.other_vaccines.as_deref() { None => Ternary::Indeterminate,
        Some("complete") => Ternary::Apt, Some("incomplete") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn eval_prophylaxis(v: &Option<String>) -> Ternary {
    match v.as_deref() { None => Ternary::Indeterminate,
        Some("adequate") => Ternary::Apt, Some("inadequate") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn eval_p21(c: &Immuno1Case) -> Ternary { eval_prophylaxis(&c.pjp_prophylaxis) }
fn eval_p22(c: &Immuno1Case) -> Ternary { eval_prophylaxis(&c.antiviral_prophylaxis) }
fn eval_p23(c: &Immuno1Case) -> Ternary { eval_prophylaxis(&c.antifungal_prophylaxis) }
fn eval_p24(c: &Immuno1Case) -> Ternary { eval_prophylaxis(&c.antibacterial_prophylaxis) }
fn eval_p25(c: &Immuno1Case) -> Ternary {
    match c.reevaluation_plan.as_deref() { None => Ternary::Indeterminate,
        Some("structured") => Ternary::Apt, Some("absent") => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}

const EVALUATORS: [fn(&Immuno1Case) -> Ternary; N] = [
    eval_p01, eval_p02, eval_p03, eval_p04, eval_p05,
    eval_p06, eval_p07, eval_p08, eval_p09, eval_p10,
    eval_p11, eval_p12, eval_p13, eval_p14, eval_p15,
    eval_p16, eval_p17, eval_p18, eval_p19, eval_p20,
    eval_p21, eval_p22, eval_p23, eval_p24, eval_p25,
];

const PARAM_NAMES: [&str; N] = [
    "P01","P02","P03","P04","P05","P06","P07","P08","P09","P10",
    "P11","P12","P13","P14","P15","P16","P17","P18","P19","P20",
    "P21","P22","P23","P24","P25",
];

// ═══════════════════════════════════════════════════════════
// OUTPUT
// ═══════════════════════════════════════════════════════════

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

#[derive(Serialize)]
struct TraceEntry {
    param: String,
    value: String,
    radius: f64,
}

// ═══════════════════════════════════════════════════════════
// WASM ENTRY POINTS
// ═══════════════════════════════════════════════════════════

/// Evaluate a clinical case. Input: JSON string. Output: JSON string.
#[wasm_bindgen]
pub fn evaluate_immuno1(json_input: &str) -> String {
    let case: Immuno1Case = match serde_json::from_str(json_input) {
        Ok(c) => c,
        Err(e) => return format!("{{\"error\":\"{}\"}}", e),
    };

    let results: Vec<Ternary> = EVALUATORS.iter().map(|f| f(&case)).collect();
    let n0 = results.iter().filter(|&&v| v == Ternary::Apt).count();
    let n1 = results.iter().filter(|&&v| v == Ternary::NotApt).count();
    let n_u = results.iter().filter(|&&v| v == Ternary::Indeterminate).count();

    let (global_class, class_idx) = if n1 >= T25 {
        ("NO_APTO", 0u8)
    } else if n0 >= T25 {
        ("APTO", 2u8)
    } else {
        ("INDETERMINADO", 1u8)
    };

    let trace: Vec<TraceEntry> = results.iter().enumerate().map(|(i, &v)| {
        TraceEntry {
            param: PARAM_NAMES[i].to_string(),
            value: v.as_str().to_string(),
            radius: v.radius(),
        }
    }).collect();

    let output = EvalOutput {
        vector: results.iter().map(|v| v.as_str().to_string()).collect(),
        n0, n1, n_u,
        global_class: global_class.to_string(),
        class_idx,
        trace,
        engine: "Rust (WebAssembly)".to_string(),
    };

    serde_json::to_string(&output).unwrap_or_else(|e| format!("{{\"error\":\"{}\"}}", e))
}

/// Engine info
#[wasm_bindgen]
pub fn engine_info() -> String {
    r#"{"engine":"Rust (WebAssembly)","module":"IMMUNO-1","n":25,"threshold":19,"parity":"108/108"}"#.to_string()
}
