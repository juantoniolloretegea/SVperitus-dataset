//! Asignación de cláusulas y separadores. No ensayado sobre Q1/Q2.
//! Clause and separator assignment. Not exercised on Q1/Q2.

use crate::diagnostico::Diagnostico;
use crate::parametros::Parametros;
use crate::plantillas::{
    ETIQUETAS, RADIOS, Sintetizador, VOCABULARIO, coincidencia, TEXTO_SEPARADOR,
};
use crate::png_lectura::{tinta_en_banda, Lienzo};
use crate::regiones::FILAS_ALINEACION;
use crate::atribucion::{atribuir, Atribucion};
use crate::residuo::{adicion_inadmisible, calcular};
use std::collections::BTreeSet;

#[derive(Clone, Debug)]
pub struct Informe {
    pub diagnostico: Diagnostico,
    pub detalle: String,
    pub pares: Vec<(String, String)>,
}

pub fn reconocer(
    lienzo: &Lienzo,
    sintetizador: &Sintetizador,
    p: &Parametros,
) -> Informe {
    let tinta_vec = tinta_en_banda(lienzo);
    let tinta: BTreeSet<(u32, u32)> = tinta_vec.iter().copied().collect();
    if (tinta.len() as u32) < p.n_min {
        return Informe {
            diagnostico: Diagnostico::LeyendaAusente,
            detalle: format!("|M_B|={} < n_min={}", tinta.len(), p.n_min),
            pares: vec![],
        };
    }

    let mut etiquetas_ok = Vec::new();
    let mut radios_ok = Vec::new();
    let mut seps_ok = Vec::new();
    let mut rasters: u32 = 0;

    for &fila in &FILAS_ALINEACION {
        let mut x = 15u32;
        while x < 310 {
            for &txt in ETIQUETAS.iter().chain(RADIOS.iter()).chain([TEXTO_SEPARADOR].iter()) {
                rasters = rasters.saturating_add(1);
                if rasters > p.max_rasterizaciones {
                    return Informe {
                        diagnostico: Diagnostico::LeyendaIlegible,
                        detalle: format!("cuota max_rasterizaciones={}", p.max_rasterizaciones),
                        pares: vec![],
                    };
                }
                let mut m = sintetizador.raster(txt, x as i32, fila as i32, p);
                let s = coincidencia(&m, &tinta);
                m.puntuacion = s;
                if s + f64::EPSILON >= p.theta && !m.pixeles.is_empty() {
                    if txt == TEXTO_SEPARADOR {
                        seps_ok.push((s, m));
                    } else if ETIQUETAS.contains(&txt) {
                        etiquetas_ok.push((s, m));
                    } else {
                        radios_ok.push((s, m));
                    }
                }
            }
            x = x.saturating_add(p.paso_x);
        }
    }

    if empate_entre_filas(&etiquetas_ok, p)
        || empate_entre_filas(&radios_ok, p)
        || empate_entre_filas(&seps_ok, p)
    {
        return Informe {
            diagnostico: Diagnostico::LeyendaIlegible,
            detalle: "empate entre filas C.7".into(),
            pares: vec![],
        };
    }

    etiquetas_ok.sort_by(|a, b| b.0.partial_cmp(&a.0).unwrap_or(std::cmp::Ordering::Equal));
    radios_ok.sort_by(|a, b| b.0.partial_cmp(&a.0).unwrap_or(std::cmp::Ordering::Equal));
    seps_ok.sort_by(|a, b| b.0.partial_cmp(&a.0).unwrap_or(std::cmp::Ordering::Equal));

    let etiquetas = no_solapadas(etiquetas_ok, p);
    let radios = no_solapadas(radios_ok, p);
    let seps = no_solapadas(seps_ok, p);

    if etiquetas.len() != 3 || radios.len() != 3 || seps.len() != 2 {
        return Informe {
            diagnostico: Diagnostico::LeyendaIlegible,
            detalle: format!(
                "asignacion etiquetas={} radios={} separadores={}",
                etiquetas.len(),
                radios.len(),
                seps.len()
            ),
            pares: vec![],
        };
    }

    let mut eord = etiquetas.clone();
    eord.sort_by_key(|m| m.origen_x);
    let mut rord = radios.clone();
    rord.sort_by_key(|m| m.origen_x);
    let mut sord = seps.clone();
    sord.sort_by_key(|m| m.origen_x);

    for i in 0..2 {
        let w = (sord[i].pixeles.iter().map(|p| p.0).max().unwrap_or(0)
            .saturating_sub(sord[i].pixeles.iter().map(|p| p.0).min().unwrap_or(0)))
            + 1;
        if w < p.w_sep_min || w > p.w_sep_max {
            return Informe {
                diagnostico: Diagnostico::LeyendaIlegible,
                detalle: format!("anchura separador {i} = {w}"),
                pares: vec![],
            };
        }
    }

    // Orden c1 < s1 < c2 < s2 < c3 usando el origen de etiqueta como proxy de cláusula.
    if !(eord[0].origen_x < sord[0].origen_x
        && sord[0].origen_x < eord[1].origen_x
        && eord[1].origen_x < sord[1].origen_x
        && sord[1].origen_x < eord[2].origen_x)
    {
        return Informe {
            diagnostico: Diagnostico::LeyendaIlegible,
            detalle: "orden clausula-separador incumplido".into(),
            pares: vec![],
        };
    }

    for i in 0..3 {
        let gap_er = (rord[i].origen_x - eord[i].origen_x).unsigned_abs();
        if gap_er < p.g_min && rord[i].origen_x <= eord[i].origen_x {
            return Informe {
                diagnostico: Diagnostico::LeyendaIlegible,
                detalle: format!("radio {i} no a la derecha de su etiqueta"),
                pares: vec![],
            };
        }
    }

    let mut aceptadas = Vec::new();
    aceptadas.extend(eord.iter().cloned());
    aceptadas.extend(rord.iter().cloned());
    aceptadas.extend(sord.iter().cloned());

    if atribuir(&aceptadas, p) == Atribucion::Empate {
        return Informe {
            diagnostico: Diagnostico::LeyendaIlegible,
            detalle: "empate de atribucion B.4".into(),
            pares: vec![],
        };
    }

    let mut no_asignada = false;
    for &txt in VOCABULARIO {
        let usada = aceptadas.iter().any(|m| m.texto == txt);
        if usada {
            continue;
        }
        for &fila in &FILAS_ALINEACION {
            let mut x = 15u32;
            while x < 310 {
                rasters = rasters.saturating_add(1);
                if rasters > p.max_rasterizaciones {
                    return Informe {
                        diagnostico: Diagnostico::LeyendaIlegible,
                        detalle: format!("cuota max_rasterizaciones={}", p.max_rasterizaciones),
                        pares: vec![],
                    };
                }
                let m = sintetizador.raster(txt, x as i32, fila as i32, p);
                if coincidencia(&m, &tinta) + f64::EPSILON >= p.theta && !m.pixeles.is_empty() {
                    no_asignada = true;
                }
                x = x.saturating_add(p.paso_x);
            }
        }
    }

    let res = calcular(&tinta, &aceptadas);
    if adicion_inadmisible(&res, p, no_asignada) {
        return Informe {
            diagnostico: Diagnostico::LeyendaIlegible,
            detalle: format!(
                "adicion B.6 r_abs={} r_rel={:.4} no_asignada={no_asignada}",
                res.r_abs, res.r_rel
            ),
            pares: vec![],
        };
    }

    let pares: Vec<(String, String)> = eord
        .iter()
        .zip(rord.iter())
        .map(|(e, r)| (e.texto.clone(), r.texto.clone()))
        .collect();
    let convenio = [
        ("0:".to_string(), "radio 1".to_string()),
        ("1:".to_string(), "radio 2".to_string()),
        ("U:".to_string(), "radio 3".to_string()),
    ];
    if pares != convenio {
        return Informe {
            diagnostico: Diagnostico::DiscordanciaContenido,
            detalle: format!("pares observados: {pares:?}"),
            pares,
        };
    }
    Informe {
        diagnostico: Diagnostico::CorrespondenciaConforme,
        detalle: format!("R_abs={} R_rel={:.4}", res.r_abs, res.r_rel),
        pares,
    }
}

fn no_solapadas(
    cands: Vec<(f64, crate::plantillas::Mascara)>,
    p: &Parametros,
) -> Vec<crate::plantillas::Mascara> {
    let mut elegidas = Vec::new();
    for (s, m) in cands {
        if elegidas.iter().any(|o: &crate::plantillas::Mascara| {
            let dx = (m.origen_x - o.origen_x).unsigned_abs();
            dx < p.d_min || !m.pixeles.is_disjoint(&o.pixeles)
        }) {
            let _ = s;
            continue;
        }
        elegidas.push(m);
    }
    elegidas
}

/// /4 §C.7: misma plantilla y misma abscisa en dos filas con |ΔS|≤epsilon.
pub fn empate_entre_filas(cands: &[(f64, crate::plantillas::Mascara)], p: &Parametros) -> bool {
    for i in 0..cands.len() {
        for j in (i + 1)..cands.len() {
            let (si, a) = &cands[i];
            let (sj, b) = &cands[j];
            if a.texto == b.texto && a.origen_x == b.origen_x && a.origen_y != b.origen_y {
                if (si - sj).abs() <= p.epsilon {
                    return true;
                }
            }
        }
    }
    false
}

#[cfg(test)]
mod pruebas {
    use super::*;
    use crate::plantillas::Mascara;

    fn p() -> Parametros {
        Parametros::analizar(
            "n_min=1\ntheta=0.5\nepsilon=0.05\nrho=0.1\nr_max=10\na_min=4\ns_px=12.8\ntau_t=1\nd_min=1\ng_min=1\nw_sep_min=1\nw_sep_max=6\npaso_x=1\nmax_rasterizaciones=10\nmax_pixeles_mascara=100\n",
        )
        .unwrap()
    }

    fn m(texto: &str, x: i32, y: i32, s: f64) -> (f64, Mascara) {
        (
            s,
            Mascara {
                texto: texto.into(),
                origen_x: x,
                origen_y: y,
                puntuacion: s,
                pixeles: BTreeSet::new(),
            },
        )
    }

    #[test]
    fn filas_distintas_mismo_x_empatan() {
        let c = vec![m("0:", 20, 334, 0.80), m("0:", 20, 337, 0.76)];
        assert!(empate_entre_filas(&c, &p()));
    }

    #[test]
    fn filas_con_s_lejos_no_empatan() {
        let c = vec![m("0:", 20, 334, 0.90), m("0:", 20, 337, 0.70)];
        assert!(!empate_entre_filas(&c, &p()));
    }
}
