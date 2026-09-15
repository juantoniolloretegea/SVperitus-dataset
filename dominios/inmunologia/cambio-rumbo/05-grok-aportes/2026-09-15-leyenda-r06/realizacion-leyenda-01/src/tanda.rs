//! Selección de la tanda de 27 celdas según /4 §C.
//! Grid selection of the 27 cells per /4 §C.
//! Q1 y Q2 permanecen la cualificación de §F; no se ejecutan aquí.

use crate::parametros::Parametros;

pub const S_REF: f64 = 12.8;

#[derive(Clone, Debug, PartialEq)]
pub struct Celda {
    pub orden_origen: u32,
    pub p: Parametros,
}

#[derive(Clone, Debug, PartialEq, Eq)]
pub enum Seleccion {
    Unica,
    EmpateResidual,
}

fn dist_s(p: &Parametros) -> f64 {
    (p.s_px as f64 - S_REF).abs()
}

/// Orden de /4 §C: s más próximo a 12,8; theta mayor; rho menor; r_max menor.
fn cmp_f64(a: f64, b: f64) -> std::cmp::Ordering {
    if (a - b).abs() <= 1e-4 {
        std::cmp::Ordering::Equal
    } else {
        a.partial_cmp(&b).unwrap_or(std::cmp::Ordering::Equal)
    }
}

pub fn cmp_c(a: &Celda, b: &Celda) -> std::cmp::Ordering {
    cmp_f64(dist_s(&a.p), dist_s(&b.p))
        .then_with(|| cmp_f64(b.p.theta, a.p.theta))
        .then_with(|| cmp_f64(a.p.rho, b.p.rho))
        .then_with(|| a.p.r_max.cmp(&b.p.r_max))
}

fn casi_igual(x: f64, y: f64) -> bool {
    (x - y).abs() <= 1e-4
}

pub fn claves_c_iguales(a: &Celda, b: &Celda) -> bool {
    casi_igual(dist_s(&a.p), dist_s(&b.p))
        && casi_igual(a.p.theta, b.p.theta)
        && casi_igual(a.p.rho, b.p.rho)
        && a.p.r_max == b.p.r_max
}

/// Entre las celdas que ya superaron Q1 y Q2 (§F), elige según §C.
/// No ejecuta Q1 ni Q2.
pub fn elegir(superaron: &[Celda]) -> Result<Celda, Seleccion> {
    if superaron.is_empty() {
        return Err(Seleccion::EmpateResidual);
    }
    let mut v = superaron.to_vec();
    v.sort_by(cmp_c);
    if v.len() >= 2 && claves_c_iguales(&v[0], &v[1]) {
        return Err(Seleccion::EmpateResidual);
    }
    Ok(v[0].clone())
}

pub fn parsear_reticula(tsv: &str) -> Result<Vec<Celda>, String> {
    let mut out = Vec::new();
    for (i, linea) in tsv.lines().enumerate() {
        if i == 0 || linea.trim().is_empty() {
            continue;
        }
        let c: Vec<&str> = linea.split('\t').collect();
        if c.len() < 16 {
            return Err(format!("fila {}: columnas insuficientes", i + 1));
        }
        let texto = format!(
            "n_min={}\ntheta={}\nepsilon={}\nrho={}\nr_max={}\na_min={}\ns_px={}\ntau_t={}\nd_min={}\ng_min={}\nw_sep_min={}\nw_sep_max={}\npaso_x={}\nmax_rasterizaciones={}\nmax_pixeles_mascara={}\n",
            c[3], c[2], c[4], c[5], c[6], c[7], c[1], c[8], c[9], c[10], c[11], c[12], c[13], c[14], c[15]
        );
        let p = Parametros::analizar(&texto)?;
        let orden: u32 = c[0]
            .parse()
            .map_err(|_| format!("fila {}: orden", i + 1))?;
        out.push(Celda {
            orden_origen: orden,
            p,
        });
    }
    Ok(out)
}

#[cfg(test)]
mod pruebas {
    use super::*;

    fn celda(s: f32, theta: f64, rho: f64, r_max: u32) -> Celda {
        let texto = format!(
            "n_min=40\ntheta={theta}\nepsilon=0.02\nrho={rho}\nr_max={r_max}\na_min=8\ns_px={s}\ntau_t=96\nd_min=8\ng_min=2\nw_sep_min=1\nw_sep_max=6\npaso_x=1\nmax_rasterizaciones=20\nmax_pixeles_mascara=80\n"
        );
        Celda {
            orden_origen: 0,
            p: Parametros::analizar(&texto).unwrap(),
        }
    }

    #[test]
    fn prefiere_s_proximo_a_128() {
        let a = celda(12.0, 0.80, 0.08, 24);
        let b = celda(12.8, 0.70, 0.08, 24);
        let g = elegir(&[a, b]).unwrap();
        assert!((g.p.s_px - 12.8).abs() < f32::EPSILON);
    }

    #[test]
    fn a_igual_s_prefiere_theta_mayor() {
        let a = celda(12.8, 0.70, 0.08, 24);
        let b = celda(12.8, 0.80, 0.08, 24);
        let g = elegir(&[a, b]).unwrap();
        assert!((g.p.theta - 0.80).abs() < 1e-12);
    }

    #[test]
    fn empate_residual_en_claves_c() {
        let a = celda(12.8, 0.80, 0.08, 24);
        let b = celda(12.8, 0.80, 0.08, 24);
        assert_eq!(elegir(&[a, b]), Err(Seleccion::EmpateResidual));
    }

    #[test]
    fn doce_y_trece_seis_empatan_distancia_si_theta_igual() {
        let a = celda(12.0, 0.80, 0.08, 24);
        let b = celda(13.6, 0.80, 0.08, 24);
        assert_eq!(elegir(&[a, b]), Err(Seleccion::EmpateResidual));
    }

    #[test]
    fn a_igual_s_y_theta_prefiere_rho_menor() {
        let a = celda(12.8, 0.80, 0.10, 24);
        let b = celda(12.8, 0.80, 0.08, 24);
        let g = elegir(&[a, b]).unwrap();
        assert!((g.p.rho - 0.08).abs() < 1e-12);
    }

    #[test]
    fn a_igual_s_theta_rho_prefiere_r_max_menor() {
        let a = celda(12.8, 0.80, 0.08, 32);
        let b = celda(12.8, 0.80, 0.08, 24);
        let g = elegir(&[a, b]).unwrap();
        assert_eq!(g.p.r_max, 24);
    }

    #[test]
    fn n_min_no_desempata_claves_c() {
        let texto = |n: u32| {
            format!(
                "n_min={n}\ntheta=0.80\nepsilon=0.02\nrho=0.08\nr_max=24\na_min=8\ns_px=12.8\ntau_t=96\nd_min=8\ng_min=2\nw_sep_min=1\nw_sep_max=6\npaso_x=1\nmax_rasterizaciones=20\nmax_pixeles_mascara=80\n"
            )
        };
        let a = Celda {
            orden_origen: 16,
            p: Parametros::analizar(&texto(20)).unwrap(),
        };
        let b = Celda {
            orden_origen: 17,
            p: Parametros::analizar(&texto(40)).unwrap(),
        };
        assert_eq!(elegir(&[a, b]), Err(Seleccion::EmpateResidual));
    }
}
