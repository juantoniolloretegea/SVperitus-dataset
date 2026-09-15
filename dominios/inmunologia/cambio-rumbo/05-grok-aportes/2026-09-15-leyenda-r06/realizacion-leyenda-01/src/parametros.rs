//! Parámetros de cualificación explícitos. Ninguno está validado.
//! Explicit qualification parameters. None are validated.

use std::fmt;
use std::fs;
use std::path::Path;

const CLAVES: &[&str] = &[
    "n_min",
    "theta",
    "epsilon",
    "rho",
    "r_max",
    "a_min",
    "s_px",
    "tau_t",
    "d_min",
    "g_min",
    "w_sep_min",
    "w_sep_max",
    "paso_x",
    "max_rasterizaciones",
    "max_pixeles_mascara",
];

#[derive(Clone, Debug, PartialEq)]
pub struct Parametros {
    pub n_min: u32,
    pub theta: f64,
    pub epsilon: f64,
    pub rho: f64,
    pub r_max: u32,
    pub a_min: u32,
    pub s_px: f32,
    pub tau_t: u8,
    pub d_min: u32,
    pub g_min: u32,
    pub w_sep_min: u32,
    pub w_sep_max: u32,
    pub paso_x: u32,
    pub max_rasterizaciones: u32,
    pub max_pixeles_mascara: u32,
}

impl Parametros {
    pub fn desde_archivo(path: &Path) -> Result<Self, String> {
        let texto = fs::read_to_string(path).map_err(|e| format!("lectura parametros: {e}"))?;
        Self::analizar(&texto)
    }

    pub fn analizar(texto: &str) -> Result<Self, String> {
        let mut mapa = std::collections::BTreeMap::<String, String>::new();
        for (i, linea) in texto.lines().enumerate() {
            let linea = linea.trim();
            if linea.is_empty() || linea.starts_with('#') {
                continue;
            }
            let Some((k, v)) = linea.split_once('=') else {
                return Err(format!("linea {}: se espera clave=valor", i + 1));
            };
            let k = k.trim().to_string();
            let v = v.trim().to_string();
            if !CLAVES.contains(&k.as_str()) {
                return Err(format!("clave desconocida: {k}"));
            }
            if mapa.contains_key(&k) {
                return Err(format!("clave repetida: {k}"));
            }
            mapa.insert(k, v);
        }
        for c in CLAVES {
            if !mapa.contains_key(*c) {
                return Err(format!("falta parametro obligatorio: {c}"));
            }
        }
        let f64_de = |k: &str| -> Result<f64, String> {
            let x: f64 = mapa[k]
                .parse()
                .map_err(|_| format!("{k} no es un real"))?;
            if !x.is_finite() {
                return Err(format!("{k} no es finito"));
            }
            Ok(x)
        };
        let f32_de = |k: &str| -> Result<f32, String> {
            let x: f32 = mapa[k]
                .parse()
                .map_err(|_| format!("{k} no es un real"))?;
            if !x.is_finite() {
                return Err(format!("{k} no es finito"));
            }
            Ok(x)
        };
        let u32_de = |k: &str| {
            mapa[k]
                .parse::<u32>()
                .map_err(|_| format!("{k} no es un entero no negativo"))
        };
        let u8_de = |k: &str| {
            mapa[k]
                .parse::<u8>()
                .map_err(|_| format!("{k} no es un entero 0..255"))
        };
        let p = Self {
            n_min: u32_de("n_min")?,
            theta: f64_de("theta")?,
            epsilon: f64_de("epsilon")?,
            rho: f64_de("rho")?,
            r_max: u32_de("r_max")?,
            a_min: u32_de("a_min")?,
            s_px: f32_de("s_px")?,
            tau_t: u8_de("tau_t")?,
            d_min: u32_de("d_min")?,
            g_min: u32_de("g_min")?,
            w_sep_min: u32_de("w_sep_min")?,
            w_sep_max: u32_de("w_sep_max")?,
            paso_x: u32_de("paso_x")?,
            max_rasterizaciones: u32_de("max_rasterizaciones")?,
            max_pixeles_mascara: u32_de("max_pixeles_mascara")?,
        };
        if !(0.0..=1.0).contains(&p.theta) {
            return Err("theta debe estar en [0,1]".into());
        }
        if !(0.0..=1.0).contains(&p.epsilon) {
            return Err("epsilon debe estar en [0,1]".into());
        }
        if !(0.0..=1.0).contains(&p.rho) {
            return Err("rho debe estar en [0,1]".into());
        }
        if p.s_px <= 0.0 {
            return Err("s_px debe ser positivo y finito".into());
        }
        if p.w_sep_min > p.w_sep_max {
            return Err("w_sep_min > w_sep_max".into());
        }
        if p.paso_x == 0 {
            return Err("paso_x debe ser >= 1".into());
        }
        if p.max_rasterizaciones == 0 {
            return Err("max_rasterizaciones debe ser >= 1".into());
        }
        p.comprobar()?;
        Ok(p)
    }

    /// Entrada pública: rechaza un valor construido sin `analizar`.
    pub fn comprobar(&self) -> Result<(), String> {
        if !self.theta.is_finite() || !(0.0..=1.0).contains(&self.theta) {
            return Err("theta no admisible".into());
        }
        if !self.epsilon.is_finite() || !(0.0..=1.0).contains(&self.epsilon) {
            return Err("epsilon no admisible".into());
        }
        if !self.rho.is_finite() || !(0.0..=1.0).contains(&self.rho) {
            return Err("rho no admisible".into());
        }
        if !self.s_px.is_finite() || self.s_px <= 0.0 {
            return Err("s_px no admisible".into());
        }
        if self.w_sep_min > self.w_sep_max {
            return Err("w_sep_min > w_sep_max".into());
        }
        if self.paso_x == 0 || self.max_rasterizaciones == 0 {
            return Err("cotas de busqueda no admisibles".into());
        }
        Ok(())
    }
}

#[cfg(test)]
mod pruebas {
    use super::*;

    #[test]
    fn rechaza_nan() {
        let e = Parametros::analizar(
            "n_min=1\ntheta=NaN\nepsilon=0.1\nrho=0.1\nr_max=1\na_min=1\ns_px=12.8\ntau_t=1\nd_min=1\ng_min=1\nw_sep_min=1\nw_sep_max=2\npaso_x=1\nmax_rasterizaciones=1\nmax_pixeles_mascara=1\n",
        );
        assert!(e.is_err());
    }

    #[test]
    fn rechaza_duplicado() {
        let e = Parametros::analizar(
            "n_min=1\nn_min=2\ntheta=0.5\nepsilon=0.1\nrho=0.1\nr_max=1\na_min=1\ns_px=12.8\ntau_t=1\nd_min=1\ng_min=1\nw_sep_min=1\nw_sep_max=2\npaso_x=1\nmax_rasterizaciones=1\nmax_pixeles_mascara=1\n",
        );
        assert!(e.is_err());
    }

    #[test]
    fn comprobar_rechaza_struct_manual() {
        let mut p = Parametros::analizar(
            "n_min=1\ntheta=0.5\nepsilon=0.1\nrho=0.1\nr_max=1\na_min=1\ns_px=12.8\ntau_t=1\nd_min=1\ng_min=1\nw_sep_min=1\nw_sep_max=2\npaso_x=1\nmax_rasterizaciones=1\nmax_pixeles_mascara=1\n",
        )
        .unwrap();
        p.s_px = f32::INFINITY;
        assert!(p.comprobar().is_err());
    }
}

impl fmt::Display for Parametros {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "n_min={} theta={} epsilon={} rho={} r_max={} a_min={} s_px={} tau_t={} d_min={} g_min={} w_sep=[{},{}] paso_x={} max_raster={} max_pix={}",
            self.n_min, self.theta, self.epsilon, self.rho, self.r_max, self.a_min,
            self.s_px, self.tau_t, self.d_min, self.g_min, self.w_sep_min, self.w_sep_max,
            self.paso_x, self.max_rasterizaciones, self.max_pixeles_mascara
        )
    }
}
