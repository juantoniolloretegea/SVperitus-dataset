// ═══════════════════════════════════════════════════════════════════════
// SVperitus — IMMUNO-1 Normative Engine (Rust) — v0.3 FINAL PLAYGROUND
// Paste into https://play.rust-lang.org (Stable channel)
//
// Series: ISSN 2695-641X | CC BY-NC-ND 4.0
// Author: Juan Antonio Lloret Egea (ORCID 0000-0002-6634-3351)
//
// STATUS: Paridad básica validada. NO versión final cerrada.
//   - Lógica clínica CONGELADA: no se toca hasta cotejo adversarial médico.
//   - Próximo paso: migración a workspace Cargo real.
//
// COVERAGE:
//   - 6 global parity tests (Python ↔ Rust)
//   - Boundary tests for ALL 25 parameters (numeric + bool + enum)
//   - JSON serde round-trip test
//   - explain() with per-parameter trace
//   - P01–P25 order verification
//   - Centralized algebraic and clinical constants
// ═══════════════════════════════════════════════════════════════════════

use serde::{Deserialize, Serialize, Serializer, Deserializer};
use std::fmt;

// ─────────────────────────────────────────────────────────────────────
// CENTRALIZED CONSTANTS
// ─────────────────────────────────────────────────────────────────────

const N: usize = 25;
const B: usize = 5;
const T25: usize = 19;

const RADIUS_APT: f64 = 1.0;
const RADIUS_NOT_APT: f64 = 2.0;
const RADIUS_INDETERMINATE: f64 = 3.0;
const CANVAS_PX: u32 = 224;
const BG_COLOR: &str = "#0D1B2A";
const POLYGON_COLOR: &str = "#C9A84C";

mod clinical {
    pub const ANC_APT: i32 = 1500;
    pub const ANC_NOT_APT: i32 = 500;
    pub const LYMPH_APT: i32 = 1000;
    pub const LYMPH_NOT_APT: i32 = 200;
    pub const IGG_APT: i32 = 700;
    pub const IGG_NOT_APT: i32 = 400;
    pub const CORTICOID_APT: f64 = 7.5;
    pub const CORTICOID_NOT_APT: f64 = 20.0;
}

// ─────────────────────────────────────────────────────────────────────
// TERNARY + CLASSIFICATION (unchanged from v0.2)
// ─────────────────────────────────────────────────────────────────────

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
enum Ternary { Apt, NotApt, Indeterminate }

impl Ternary {
    fn from_str_canonical(s: &str) -> Option<Ternary> {
        match s { "0" => Some(Ternary::Apt), "1" => Some(Ternary::NotApt),
                  "U" => Some(Ternary::Indeterminate), _ => None }
    }
    fn as_str(&self) -> &'static str {
        match self { Ternary::Apt => "0", Ternary::NotApt => "1",
                     Ternary::Indeterminate => "U" }
    }
    fn radius(&self) -> f64 {
        match self { Ternary::Apt => RADIUS_APT, Ternary::NotApt => RADIUS_NOT_APT,
                     Ternary::Indeterminate => RADIUS_INDETERMINATE }
    }
}

impl fmt::Display for Ternary {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result { write!(f, "{}", self.as_str()) }
}

impl Serialize for Ternary {
    fn serialize<S: Serializer>(&self, s: S) -> Result<S::Ok, S::Error> {
        s.serialize_str(self.as_str())
    }
}

impl<'de> Deserialize<'de> for Ternary {
    fn deserialize<D: Deserializer<'de>>(d: D) -> Result<Self, D::Error> {
        let s = String::deserialize(d)?;
        Ternary::from_str_canonical(&s)
            .ok_or_else(|| serde::de::Error::custom(format!("invalid ternary '{}'", s)))
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum GlobalClass { NoApto, Indeterminado, Apto }

impl GlobalClass {
    fn to_idx(&self) -> u8 {
        match self { GlobalClass::NoApto => 0, GlobalClass::Indeterminado => 1, GlobalClass::Apto => 2 }
    }
    fn as_str(&self) -> &'static str {
        match self { GlobalClass::NoApto => "NO_APTO", GlobalClass::Indeterminado => "INDETERMINADO",
                     GlobalClass::Apto => "APTO" }
    }
}

fn threshold(n: usize) -> usize { (7 * n) / 9 }

fn count_ternary(v: &[Ternary]) -> (usize, usize, usize) {
    v.iter().fold((0,0,0), |(a,b,c), t| match t {
        Ternary::Apt => (a+1,b,c), Ternary::NotApt => (a,b+1,c),
        Ternary::Indeterminate => (a,b,c+1)
    })
}

fn classify(v: &[Ternary]) -> GlobalClass {
    let t = threshold(v.len());
    let (n0, n1, _) = count_ternary(v);
    if n1 >= t { GlobalClass::NoApto }
    else if n0 >= t { GlobalClass::Apto }
    else { GlobalClass::Indeterminado }
}

// ─────────────────────────────────────────────────────────────────────
// IMMUNO-1 CASE (Serialize added for round-trip test)
// ─────────────────────────────────────────────────────────────────────

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
struct Immuno1Case {
    anc: Option<i32>, lymphocytes: Option<i32>, igg: Option<i32>,
    spleen_intact: Option<bool>, barriers_intact: Option<bool>,
    neoplasia_phase: Option<String>, chemo_active: Option<bool>,
    biologic_type: Option<String>, tph_cart: Option<String>,
    corticoid_mg: Option<f64>,
    severe_bacterial_12m: Option<bool>, prior_ifd: Option<bool>,
    chronic_viral: Option<String>, mdr_colonization: Option<bool>,
    recent_healthcare: Option<bool>,
    flu_vaccine: Option<String>, pneumo_vaccine: Option<String>,
    covid_vaccine: Option<String>, hepb_vaccine: Option<String>,
    other_vaccines: Option<String>,
    pjp_prophylaxis: Option<String>, antiviral_prophylaxis: Option<String>,
    antifungal_prophylaxis: Option<String>,
    antibacterial_prophylaxis: Option<String>,
    reevaluation_plan: Option<String>,
}

// ─────────────────────────────────────────────────────────────────────
// PARAMETER NAMES
// ─────────────────────────────────────────────────────────────────────

const PARAM_NAMES: [&str; 25] = [
    "P01_neutropenia", "P02_lymphopenia", "P03_hypogamma",
    "P04_splenic_fn", "P05_barriers",
    "P06_neoplasia_phase", "P07_chemotherapy", "P08_biologics",
    "P09_tph_cart", "P10_corticoids",
    "P11_severe_bact_12m", "P12_prior_ifd", "P13_chronic_viral",
    "P14_mdr_colonization", "P15_healthcare_exposure",
    "P16_flu_vaccine", "P17_pneumo_vaccine", "P18_covid_vaccine",
    "P19_hepb_vaccine", "P20_other_vaccines",
    "P21_pjp_prophylaxis", "P22_antiviral_proph", "P23_antifungal_proph",
    "P24_antibacterial_proph", "P25_reevaluation_plan",
];

// ─────────────────────────────────────────────────────────────────────
// EVAL FUNCTIONS P01–P25 (CLINICAL LOGIC FROZEN — DO NOT MODIFY)
// ─────────────────────────────────────────────────────────────────────

fn eval_p01(c: &Immuno1Case) -> Ternary {
    match c.anc { None => Ternary::Indeterminate,
        Some(v) if v >= clinical::ANC_APT => Ternary::Apt,
        Some(v) if v < clinical::ANC_NOT_APT => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn eval_p02(c: &Immuno1Case) -> Ternary {
    match c.lymphocytes { None => Ternary::Indeterminate,
        Some(v) if v >= clinical::LYMPH_APT => Ternary::Apt,
        Some(v) if v < clinical::LYMPH_NOT_APT => Ternary::NotApt,
        Some(_) => Ternary::Indeterminate }
}
fn eval_p03(c: &Immuno1Case) -> Ternary {
    match c.igg { None => Ternary::Indeterminate,
        Some(v) if v >= clinical::IGG_APT => Ternary::Apt,
        Some(v) if v < clinical::IGG_NOT_APT => Ternary::NotApt,
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
        Some(mg) if mg < clinical::CORTICOID_APT => Ternary::Apt,
        Some(mg) if mg >= clinical::CORTICOID_NOT_APT => Ternary::NotApt,
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

// ─────────────────────────────────────────────────────────────────────
// EVALUATE + EXPLAIN
// ─────────────────────────────────────────────────────────────────────

struct EvalResult { vector: Vec<Ternary>, n0: usize, n1: usize, n_u: usize, class: GlobalClass }

fn evaluate(case: &Immuno1Case) -> EvalResult {
    let vector: Vec<Ternary> = EVALUATORS.iter().map(|f| f(case)).collect();
    let (n0, n1, n_u) = count_ternary(&vector);
    let class = classify(&vector);
    EvalResult { vector, n0, n1, n_u, class }
}

fn print_explain(case_id: &str, case: &Immuno1Case) {
    let r = evaluate(case);
    println!("  ┌─ EXPLAIN: {}", case_id);
    for (i, &v) in r.vector.iter().enumerate() {
        let sym = match v { Ternary::Apt => "✓", Ternary::NotApt => "✗", Ternary::Indeterminate => "?" };
        println!("  │ {} {} = {}", sym, PARAM_NAMES[i], v);
    }
    println!("  │ ── Counts: n0={} n1={} nU={}", r.n0, r.n1, r.n_u);
    println!("  └─ Class: {} (idx={})", r.class.as_str(), r.class.to_idx());
}

// ─────────────────────────────────────────────────────────────────────
// HELPERS
// ─────────────────────────────────────────────────────────────────────

const BASE_JSON: &str = r#"{"anc":3000,"lymphocytes":1500,"igg":900,"spleen_intact":true,"barriers_intact":true,"neoplasia_phase":"remission","chemo_active":false,"biologic_type":"none","tph_cart":"none","corticoid_mg":0.0,"severe_bacterial_12m":false,"prior_ifd":false,"chronic_viral":"none","mdr_colonization":false,"recent_healthcare":false,"flu_vaccine":"current","pneumo_vaccine":"current","covid_vaccine":"current","hepb_vaccine":"immune","other_vaccines":"complete","pjp_prophylaxis":"adequate","antiviral_prophylaxis":"adequate","antifungal_prophylaxis":"adequate","antibacterial_prophylaxis":"adequate","reevaluation_plan":"structured"}"#;

fn base_case() -> Immuno1Case { serde_json::from_str(BASE_JSON).unwrap() }

// ─────────────────────────────────────────────────────────────────────
// GLOBAL PARITY TESTS
// ─────────────────────────────────────────────────────────────────────

struct ParityTest { id: &'static str, json: &'static str, vec: [&'static str; N],
    n0: usize, n1: usize, nu: usize, class: &'static str, idx: u8 }

fn run_parity(t: &ParityTest) -> bool {
    let case: Immuno1Case = serde_json::from_str(t.json).unwrap();
    let r = evaluate(&case);
    let exp: Vec<Ternary> = t.vec.iter().map(|s| Ternary::from_str_canonical(s).unwrap()).collect();
    let ok = r.vector == exp && r.n0 == t.n0 && r.n1 == t.n1 && r.n_u == t.nu
        && r.class.as_str() == t.class && r.class.to_idx() == t.idx;
    if ok { println!("  PASS  {:30}  [n0={:2} n1={:2} nU={:2} → {}]", t.id, r.n0, r.n1, r.n_u, r.class.as_str()); }
    else {
        println!("  FAIL  {}", t.id);
        for (i,(a,e)) in r.vector.iter().zip(exp.iter()).enumerate() {
            if a != e { println!("         {}: got={} exp={}", PARAM_NAMES[i], a, e); }
        }
    }
    ok
}

fn global_tests() -> Vec<ParityTest> { vec![
    ParityTest { id: "APTO_CLEAN_001", json: BASE_JSON,
        vec: ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        n0:25, n1:0, nu:0, class:"APTO", idx:2 },
    ParityTest { id: "NO_APTO_EXTREME_001", json: r#"{"anc":200,"lymphocytes":100,"igg":250,"spleen_intact":false,"barriers_intact":false,"neoplasia_phase":"relapse","chemo_active":true,"biologic_type":"anti_cd20","tph_cart":"allo_tph","corticoid_mg":40.0,"severe_bacterial_12m":true,"prior_ifd":true,"chronic_viral":"active","mdr_colonization":true,"recent_healthcare":true,"flu_vaccine":"none","pneumo_vaccine":"none","covid_vaccine":"none","hepb_vaccine":"non_immune","other_vaccines":"incomplete","pjp_prophylaxis":"inadequate","antiviral_prophylaxis":"inadequate","antifungal_prophylaxis":"inadequate","antibacterial_prophylaxis":"inadequate","reevaluation_plan":"absent"}"#,
        vec: ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        n0:0, n1:25, nu:0, class:"NO_APTO", idx:0 },
    ParityTest { id: "INDETERMINADO_MIXED_001", json: r#"{"anc":800,"lymphocytes":500,"igg":500,"spleen_intact":true,"barriers_intact":true,"neoplasia_phase":"remission","chemo_active":false,"biologic_type":"other","tph_cart":"auto_tph","corticoid_mg":10.0,"severe_bacterial_12m":false,"prior_ifd":false,"chronic_viral":"controlled","mdr_colonization":false,"recent_healthcare":false,"flu_vaccine":"outdated","pneumo_vaccine":"outdated","covid_vaccine":"outdated","hepb_vaccine":"unknown","other_vaccines":"unknown","pjp_prophylaxis":"na","antiviral_prophylaxis":"adequate","antifungal_prophylaxis":"adequate","antibacterial_prophylaxis":"adequate","reevaluation_plan":"partial"}"#,
        vec: ["U","U","U","0","0","0","0","U","U","U","0","0","U","0","0","U","U","U","U","U","U","0","0","0","U"],
        n0:11, n1:0, nu:14, class:"INDETERMINADO", idx:1 },
    ParityTest { id: "EDGE_19_ZEROS_001", json: r#"{"anc":2000,"lymphocytes":1200,"igg":800,"spleen_intact":true,"barriers_intact":true,"neoplasia_phase":"remission","chemo_active":false,"biologic_type":"none","tph_cart":"none","corticoid_mg":0.0,"severe_bacterial_12m":false,"prior_ifd":false,"chronic_viral":"none","mdr_colonization":false,"recent_healthcare":false,"flu_vaccine":"current","pneumo_vaccine":"current","covid_vaccine":"current","hepb_vaccine":"immune","other_vaccines":"unknown","pjp_prophylaxis":"na","antiviral_prophylaxis":null,"antifungal_prophylaxis":null,"antibacterial_prophylaxis":null,"reevaluation_plan":null}"#,
        vec: ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","U","U","U","U","U","U"],
        n0:19, n1:0, nu:6, class:"APTO", idx:2 },
    ParityTest { id: "EDGE_19_ONES_001", json: r#"{"anc":200,"lymphocytes":100,"igg":250,"spleen_intact":false,"barriers_intact":false,"neoplasia_phase":"relapse","chemo_active":true,"biologic_type":"anti_cd20","tph_cart":"allo_tph","corticoid_mg":40.0,"severe_bacterial_12m":true,"prior_ifd":true,"chronic_viral":"active","mdr_colonization":true,"recent_healthcare":true,"flu_vaccine":"none","pneumo_vaccine":"none","covid_vaccine":"none","hepb_vaccine":"non_immune","other_vaccines":"complete","pjp_prophylaxis":"adequate","antiviral_prophylaxis":"adequate","antifungal_prophylaxis":"adequate","antibacterial_prophylaxis":"adequate","reevaluation_plan":"structured"}"#,
        vec: ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","0","0","0","0","0"],
        n0:6, n1:19, nu:0, class:"NO_APTO", idx:0 },
    ParityTest { id: "ALL_UNKNOWN_001", json: r#"{"anc":null,"lymphocytes":null,"igg":null,"spleen_intact":null,"barriers_intact":null,"neoplasia_phase":null,"chemo_active":null,"biologic_type":null,"tph_cart":null,"corticoid_mg":null,"severe_bacterial_12m":null,"prior_ifd":null,"chronic_viral":null,"mdr_colonization":null,"recent_healthcare":null,"flu_vaccine":null,"pneumo_vaccine":null,"covid_vaccine":null,"hepb_vaccine":null,"other_vaccines":null,"pjp_prophylaxis":null,"antiviral_prophylaxis":null,"antifungal_prophylaxis":null,"antibacterial_prophylaxis":null,"reevaluation_plan":null}"#,
        vec: ["U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U"],
        n0:0, n1:0, nu:25, class:"INDETERMINADO", idx:1 },
]}

// ─────────────────────────────────────────────────────────────────────
// BOUNDARY TESTS — ALL 25 PARAMETERS
// ─────────────────────────────────────────────────────────────────────

struct BT { name: &'static str, idx: usize, exp: Ternary, case: Immuno1Case }

fn boundary_tests() -> Vec<BT> {
    let mut t = Vec::new();

    // P01 ANC: numeric boundaries
    for (n,v,e) in [("P01=499",499,Ternary::NotApt),("P01=500",500,Ternary::Indeterminate),
        ("P01=1499",1499,Ternary::Indeterminate),("P01=1500",1500,Ternary::Apt)] {
        let mut c=base_case(); c.anc=Some(v); t.push(BT{name:n,idx:0,exp:e,case:c}); }
    { let mut c=base_case(); c.anc=None; t.push(BT{name:"P01=None",idx:0,exp:Ternary::Indeterminate,case:c}); }

    // P02 Lymphocytes: numeric boundaries
    for (n,v,e) in [("P02=199",199,Ternary::NotApt),("P02=200",200,Ternary::Indeterminate),
        ("P02=999",999,Ternary::Indeterminate),("P02=1000",1000,Ternary::Apt)] {
        let mut c=base_case(); c.lymphocytes=Some(v); t.push(BT{name:n,idx:1,exp:e,case:c}); }
    { let mut c=base_case(); c.lymphocytes=None; t.push(BT{name:"P02=None",idx:1,exp:Ternary::Indeterminate,case:c}); }

    // P03 IgG: numeric boundaries
    for (n,v,e) in [("P03=399",399,Ternary::NotApt),("P03=400",400,Ternary::Indeterminate),
        ("P03=699",699,Ternary::Indeterminate),("P03=700",700,Ternary::Apt)] {
        let mut c=base_case(); c.igg=Some(v); t.push(BT{name:n,idx:2,exp:e,case:c}); }
    { let mut c=base_case(); c.igg=None; t.push(BT{name:"P03=None",idx:2,exp:Ternary::Indeterminate,case:c}); }

    // P04 Spleen: bool boundaries
    for (n,v,e) in [("P04=true",Some(true),Ternary::Apt),("P04=false",Some(false),Ternary::NotApt),
        ("P04=None",None,Ternary::Indeterminate)] {
        let mut c=base_case(); c.spleen_intact=v; t.push(BT{name:n,idx:3,exp:e,case:c}); }

    // P05 Barriers: bool
    for (n,v,e) in [("P05=true",Some(true),Ternary::Apt),("P05=false",Some(false),Ternary::NotApt),
        ("P05=None",None,Ternary::Indeterminate)] {
        let mut c=base_case(); c.barriers_intact=v; t.push(BT{name:n,idx:4,exp:e,case:c}); }

    // P06 Neoplasia: enum
    for (n,v,e) in [("P06=remission","remission",Ternary::Apt),("P06=active","active",Ternary::NotApt),
        ("P06=relapse","relapse",Ternary::NotApt),("P06=unknown","unknown",Ternary::Indeterminate)] {
        let mut c=base_case(); c.neoplasia_phase=Some(v.into()); t.push(BT{name:n,idx:5,exp:e,case:c}); }
    { let mut c=base_case(); c.neoplasia_phase=None; t.push(BT{name:"P06=None",idx:5,exp:Ternary::Indeterminate,case:c}); }

    // P07 Chemo: bool
    for (n,v,e) in [("P07=false",Some(false),Ternary::Apt),("P07=true",Some(true),Ternary::NotApt),
        ("P07=None",None,Ternary::Indeterminate)] {
        let mut c=base_case(); c.chemo_active=v; t.push(BT{name:n,idx:6,exp:e,case:c}); }

    // P08 Biologics: enum
    for (n,v,e) in [("P08=none","none",Ternary::Apt),("P08=anti_cd20","anti_cd20",Ternary::NotApt),
        ("P08=anti_tnf","anti_tnf",Ternary::Indeterminate),("P08=other","other",Ternary::Indeterminate)] {
        let mut c=base_case(); c.biologic_type=Some(v.into()); t.push(BT{name:n,idx:7,exp:e,case:c}); }
    { let mut c=base_case(); c.biologic_type=None; t.push(BT{name:"P08=None",idx:7,exp:Ternary::Indeterminate,case:c}); }

    // P09 TPH/CART: enum
    for (n,v,e) in [("P09=none","none",Ternary::Apt),("P09=allo_tph","allo_tph",Ternary::NotApt),
        ("P09=cart","cart",Ternary::NotApt),("P09=auto_tph","auto_tph",Ternary::Indeterminate)] {
        let mut c=base_case(); c.tph_cart=Some(v.into()); t.push(BT{name:n,idx:8,exp:e,case:c}); }
    { let mut c=base_case(); c.tph_cart=None; t.push(BT{name:"P09=None",idx:8,exp:Ternary::Indeterminate,case:c}); }

    // P10 Corticoids: numeric
    for (n,v,e) in [("P10=7.4",7.4,Ternary::Apt),("P10=7.5",7.5,Ternary::Indeterminate),
        ("P10=19.9",19.9,Ternary::Indeterminate),("P10=20.0",20.0,Ternary::NotApt)] {
        let mut c=base_case(); c.corticoid_mg=Some(v); t.push(BT{name:n,idx:9,exp:e,case:c}); }
    { let mut c=base_case(); c.corticoid_mg=None; t.push(BT{name:"P10=None",idx:9,exp:Ternary::Indeterminate,case:c}); }

    // P11 Severe bacterial: bool
    for (n,v,e) in [("P11=false",Some(false),Ternary::Apt),("P11=true",Some(true),Ternary::NotApt),
        ("P11=None",None,Ternary::Indeterminate)] {
        let mut c=base_case(); c.severe_bacterial_12m=v; t.push(BT{name:n,idx:10,exp:e,case:c}); }

    // P12 Prior IFD: bool
    for (n,v,e) in [("P12=false",Some(false),Ternary::Apt),("P12=true",Some(true),Ternary::NotApt),
        ("P12=None",None,Ternary::Indeterminate)] {
        let mut c=base_case(); c.prior_ifd=v; t.push(BT{name:n,idx:11,exp:e,case:c}); }

    // P13 Chronic viral: enum
    for (n,v,e) in [("P13=none","none",Ternary::Apt),("P13=active","active",Ternary::NotApt),
        ("P13=controlled","controlled",Ternary::Indeterminate)] {
        let mut c=base_case(); c.chronic_viral=Some(v.into()); t.push(BT{name:n,idx:12,exp:e,case:c}); }
    { let mut c=base_case(); c.chronic_viral=None; t.push(BT{name:"P13=None",idx:12,exp:Ternary::Indeterminate,case:c}); }

    // P14 MDR colonization: bool
    for (n,v,e) in [("P14=false",Some(false),Ternary::Apt),("P14=true",Some(true),Ternary::NotApt),
        ("P14=None",None,Ternary::Indeterminate)] {
        let mut c=base_case(); c.mdr_colonization=v; t.push(BT{name:n,idx:13,exp:e,case:c}); }

    // P15 Healthcare: bool
    for (n,v,e) in [("P15=false",Some(false),Ternary::Apt),("P15=true",Some(true),Ternary::NotApt),
        ("P15=None",None,Ternary::Indeterminate)] {
        let mut c=base_case(); c.recent_healthcare=v; t.push(BT{name:n,idx:14,exp:e,case:c}); }

    // P16 Flu vaccine: enum
    for (n,v,e) in [("P16=current","current",Ternary::Apt),("P16=none","none",Ternary::NotApt),
        ("P16=outdated","outdated",Ternary::Indeterminate)] {
        let mut c=base_case(); c.flu_vaccine=Some(v.into()); t.push(BT{name:n,idx:15,exp:e,case:c}); }
    { let mut c=base_case(); c.flu_vaccine=None; t.push(BT{name:"P16=None",idx:15,exp:Ternary::Indeterminate,case:c}); }

    // P17 Pneumo: same pattern as P16
    for (n,v,e) in [("P17=current","current",Ternary::Apt),("P17=none","none",Ternary::NotApt),
        ("P17=outdated","outdated",Ternary::Indeterminate)] {
        let mut c=base_case(); c.pneumo_vaccine=Some(v.into()); t.push(BT{name:n,idx:16,exp:e,case:c}); }
    { let mut c=base_case(); c.pneumo_vaccine=None; t.push(BT{name:"P17=None",idx:16,exp:Ternary::Indeterminate,case:c}); }

    // P18 Covid: same pattern
    for (n,v,e) in [("P18=current","current",Ternary::Apt),("P18=none","none",Ternary::NotApt),
        ("P18=outdated","outdated",Ternary::Indeterminate)] {
        let mut c=base_case(); c.covid_vaccine=Some(v.into()); t.push(BT{name:n,idx:17,exp:e,case:c}); }
    { let mut c=base_case(); c.covid_vaccine=None; t.push(BT{name:"P18=None",idx:17,exp:Ternary::Indeterminate,case:c}); }

    // P19 HepB
    for (n,v,e) in [("P19=immune","immune",Ternary::Apt),("P19=non_immune","non_immune",Ternary::NotApt),
        ("P19=unknown","unknown",Ternary::Indeterminate)] {
        let mut c=base_case(); c.hepb_vaccine=Some(v.into()); t.push(BT{name:n,idx:18,exp:e,case:c}); }
    { let mut c=base_case(); c.hepb_vaccine=None; t.push(BT{name:"P19=None",idx:18,exp:Ternary::Indeterminate,case:c}); }

    // P20 Other vaccines
    for (n,v,e) in [("P20=complete","complete",Ternary::Apt),("P20=incomplete","incomplete",Ternary::NotApt),
        ("P20=unknown","unknown",Ternary::Indeterminate)] {
        let mut c=base_case(); c.other_vaccines=Some(v.into()); t.push(BT{name:n,idx:19,exp:e,case:c}); }
    { let mut c=base_case(); c.other_vaccines=None; t.push(BT{name:"P20=None",idx:19,exp:Ternary::Indeterminate,case:c}); }

    // P21 PJP prophylaxis
    for (n,v,e) in [("P21=adequate","adequate",Ternary::Apt),("P21=inadequate","inadequate",Ternary::NotApt),
        ("P21=na","na",Ternary::Indeterminate)] {
        let mut c=base_case(); c.pjp_prophylaxis=Some(v.into()); t.push(BT{name:n,idx:20,exp:e,case:c}); }
    { let mut c=base_case(); c.pjp_prophylaxis=None; t.push(BT{name:"P21=None",idx:20,exp:Ternary::Indeterminate,case:c}); }

    // P22 Antiviral proph
    for (n,v,e) in [("P22=adequate","adequate",Ternary::Apt),("P22=inadequate","inadequate",Ternary::NotApt),
        ("P22=na","na",Ternary::Indeterminate)] {
        let mut c=base_case(); c.antiviral_prophylaxis=Some(v.into()); t.push(BT{name:n,idx:21,exp:e,case:c}); }
    { let mut c=base_case(); c.antiviral_prophylaxis=None; t.push(BT{name:"P22=None",idx:21,exp:Ternary::Indeterminate,case:c}); }

    // P23 Antifungal proph
    for (n,v,e) in [("P23=adequate","adequate",Ternary::Apt),("P23=inadequate","inadequate",Ternary::NotApt),
        ("P23=na","na",Ternary::Indeterminate)] {
        let mut c=base_case(); c.antifungal_prophylaxis=Some(v.into()); t.push(BT{name:n,idx:22,exp:e,case:c}); }
    { let mut c=base_case(); c.antifungal_prophylaxis=None; t.push(BT{name:"P23=None",idx:22,exp:Ternary::Indeterminate,case:c}); }

    // P24 Antibacterial proph
    for (n,v,e) in [("P24=adequate","adequate",Ternary::Apt),("P24=inadequate","inadequate",Ternary::NotApt),
        ("P24=na","na",Ternary::Indeterminate)] {
        let mut c=base_case(); c.antibacterial_prophylaxis=Some(v.into()); t.push(BT{name:n,idx:23,exp:e,case:c}); }
    { let mut c=base_case(); c.antibacterial_prophylaxis=None; t.push(BT{name:"P24=None",idx:23,exp:Ternary::Indeterminate,case:c}); }

    // P25 Reevaluation plan
    for (n,v,e) in [("P25=structured","structured",Ternary::Apt),("P25=absent","absent",Ternary::NotApt),
        ("P25=partial","partial",Ternary::Indeterminate)] {
        let mut c=base_case(); c.reevaluation_plan=Some(v.into()); t.push(BT{name:n,idx:24,exp:e,case:c}); }
    { let mut c=base_case(); c.reevaluation_plan=None; t.push(BT{name:"P25=None",idx:24,exp:Ternary::Indeterminate,case:c}); }

    t
}

// ─────────────────────────────────────────────────────────────────────
// MAIN
// ─────────────────────────────────────────────────────────────────────

fn main() {
    println!("╔═══════════════════════════════════════════════════════════╗");
    println!("║  SVperitus — IMMUNO-1 Parity Runner v0.3 FINAL           ║");
    println!("║  Rust vs Python — Playground Edition                      ║");
    println!("║  Clinical logic FROZEN — do not modify until review       ║");
    println!("╚═══════════════════════════════════════════════════════════╝");

    // 1. Algebraic invariants
    println!("\n── Algebraic Invariants ──");
    assert_eq!(threshold(N), T25); assert_eq!(T25, 19); assert_eq!(threshold(9), 7);
    println!("  ✓ N={} B={} T({})={} T(9)={}", N, B, N, T25, threshold(9));
    println!("  ✓ RADIUS: 0→{} 1→{} U→{}", RADIUS_APT, RADIUS_NOT_APT, RADIUS_INDETERMINATE);
    println!("  ✓ Canvas={}px BG={} Poly={}", CANVAS_PX, BG_COLOR, POLYGON_COLOR);

    // 2. P01–P25 order
    println!("\n── Parameter Order ──");
    assert_eq!(EVALUATORS.len(), N); assert_eq!(PARAM_NAMES.len(), N);
    for (i, n) in PARAM_NAMES.iter().enumerate() {
        assert!(n.starts_with(&format!("P{:02}_", i+1)), "order broken at {}", i);
    }
    println!("  ✓ 25 evaluators in canonical order P01–P25");

    // 3. JSON serde round-trip
    println!("\n── Serde Round-Trip ──");
    let original = base_case();
    let json_str = serde_json::to_string(&original).unwrap();
    let roundtrip: Immuno1Case = serde_json::from_str(&json_str).unwrap();
    assert_eq!(original, roundtrip, "serde round-trip failed");
    // Also test null case
    let null_json = r#"{"anc":null,"lymphocytes":null,"igg":null,"spleen_intact":null,"barriers_intact":null,"neoplasia_phase":null,"chemo_active":null,"biologic_type":null,"tph_cart":null,"corticoid_mg":null,"severe_bacterial_12m":null,"prior_ifd":null,"chronic_viral":null,"mdr_colonization":null,"recent_healthcare":null,"flu_vaccine":null,"pneumo_vaccine":null,"covid_vaccine":null,"hepb_vaccine":null,"other_vaccines":null,"pjp_prophylaxis":null,"antiviral_prophylaxis":null,"antifungal_prophylaxis":null,"antibacterial_prophylaxis":null,"reevaluation_plan":null}"#;
    let null_case: Immuno1Case = serde_json::from_str(null_json).unwrap();
    let null_rt: Immuno1Case = serde_json::from_str(&serde_json::to_string(&null_case).unwrap()).unwrap();
    assert_eq!(null_case, null_rt, "null serde round-trip failed");
    println!("  ✓ Full case: serialize → deserialize = identical");
    println!("  ✓ Null case: serialize → deserialize = identical");

    // 4. Global parity
    println!("\n── Global Parity (Python ↔ Rust) ──");
    let gt = global_tests();
    let (mut gp, mut gf) = (0u32, 0u32);
    for t in &gt { if run_parity(t) { gp+=1; } else { gf+=1; } }

    // 5. Boundary tests ALL 25 params
    println!("\n── Boundary Tests (all 25 parameters) ──");
    let bt = boundary_tests();
    let (mut bp, mut bf) = (0u32, 0u32);
    for b in &bt {
        let r = evaluate(&b.case);
        let actual = r.vector[b.idx];
        if actual == b.exp {
            println!("  PASS  {:20} {} = {}", b.name, PARAM_NAMES[b.idx], actual);
            bp += 1;
        } else {
            println!("  FAIL  {:20} exp={} got={}", b.name, b.exp, actual);
            bf += 1;
        }
    }

    // 6. Explain demo
    println!("\n── Explain Demo ──");
    let mixed: Immuno1Case = serde_json::from_str(r#"{"anc":800,"lymphocytes":500,"igg":500,"spleen_intact":true,"barriers_intact":true,"neoplasia_phase":"remission","chemo_active":false,"biologic_type":"other","tph_cart":"auto_tph","corticoid_mg":10.0,"severe_bacterial_12m":false,"prior_ifd":false,"chronic_viral":"controlled","mdr_colonization":false,"recent_healthcare":false,"flu_vaccine":"outdated","pneumo_vaccine":"outdated","covid_vaccine":"outdated","hepb_vaccine":"unknown","other_vaccines":"unknown","pjp_prophylaxis":"na","antiviral_prophylaxis":"adequate","antifungal_prophylaxis":"adequate","antibacterial_prophylaxis":"adequate","reevaluation_plan":"partial"}"#).unwrap();
    print_explain("INDETERMINADO_MIXED_001", &mixed);

    // Summary
    let tp = gp + bp; let tf = gf + bf; let serde_tests = 2u32;
    let total = tp + serde_tests; // serde tests always pass if we got here
    println!("\n═══════════════════════════════════════════════════════════");
    println!("  Global parity:   {:3}/{} passed", gp, gp+gf);
    println!("  Boundary tests:  {:3}/{} passed", bp, bp+bf);
    println!("  Serde tests:       2/2 passed");
    println!("  ─────────────────────────────────");
    println!("  TOTAL:           {:3}/{} passed", total, total + tf);
    println!("═══════════════════════════════════════════════════════════");
    if tf > 0 { println!("\n  ✗ SOME TESTS FAILED."); }
    else {
        println!("\n  ✓ ALL TESTS PASSED. Paridad completa validada.");
        println!("    Clinical logic FROZEN. Next: Cargo workspace + adversarial review.");
    }
}
