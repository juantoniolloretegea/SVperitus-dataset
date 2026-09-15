//! Atribución exclusiva por mayor S ( /4 §B.4 ) sobre la unión geométrica ( §B.3 ).
//! Exclusive attribution by highest S over the geometric union.

use crate::parametros::Parametros;
use crate::plantillas::Mascara;
use std::collections::BTreeMap;

#[derive(Clone, Debug, PartialEq, Eq)]
pub enum Atribucion {
    Exclusiva,
    Empate,
}

/// Unión geométrica de las máscaras aceptadas: M_expl de §B.3.
pub fn union_geometrica(aceptadas: &[Mascara]) -> std::collections::BTreeSet<(u32, u32)> {
    let mut u = std::collections::BTreeSet::new();
    for m in aceptadas {
        u.extend(&m.pixeles);
    }
    u
}

/// Cada píxel de la unión se atribuye a la plantilla de mayor S.
/// Si *cualquier* par de plantillas que lo contienen cumple |Sa−Sb|≤epsilon,
/// Empate, con independencia del orden de las máscaras y de un tercero con S mayor.
pub fn atribuir(aceptadas: &[Mascara], p: &Parametros) -> Atribucion {
    let mut cubiertas: BTreeMap<(u32, u32), Vec<f64>> = BTreeMap::new();
    for m in aceptadas {
        for &pix in &m.pixeles {
            cubiertas.entry(pix).or_default().push(m.puntuacion);
        }
    }
    for puntuaciones in cubiertas.values() {
        for i in 0..puntuaciones.len() {
            for j in (i + 1)..puntuaciones.len() {
                if (puntuaciones[i] - puntuaciones[j]).abs() <= p.epsilon {
                    return Atribucion::Empate;
                }
            }
        }
    }
    Atribucion::Exclusiva
}

/// Mapa píxel → índice de plantilla atribuida. Vacío si hay empate.
pub fn mapa_exclusivo(
    aceptadas: &[Mascara],
    p: &Parametros,
) -> Result<BTreeMap<(u32, u32), usize>, Atribucion> {
    if atribuir(aceptadas, p) == Atribucion::Empate {
        return Err(Atribucion::Empate);
    }
    let mut dueno: BTreeMap<(u32, u32), (usize, f64)> = BTreeMap::new();
    for (i, m) in aceptadas.iter().enumerate() {
        for &pix in &m.pixeles {
            match dueno.get(&pix) {
                None => {
                    dueno.insert(pix, (i, m.puntuacion));
                }
                Some(&(_, sj)) => {
                    if m.puntuacion > sj {
                        dueno.insert(pix, (i, m.puntuacion));
                    }
                }
            }
        }
    }
    Ok(dueno.into_iter().map(|(k, (i, _))| (k, i)).collect())
}

#[cfg(test)]
mod pruebas {
    use super::*;
    use crate::parametros::Parametros;
    use crate::plantillas::Mascara;
    use std::collections::BTreeSet;

    fn p_eps(eps: f64) -> Parametros {
        Parametros::analizar(&format!(
            "n_min=1\ntheta=0.5\nepsilon={eps}\nrho=0.1\nr_max=10\na_min=4\ns_px=12.8\ntau_t=1\nd_min=1\ng_min=1\nw_sep_min=1\nw_sep_max=6\npaso_x=1\nmax_rasterizaciones=10\nmax_pixeles_mascara=100\n"
        ))
        .unwrap()
    }

    fn mascara(s: f64, pix: &[(u32, u32)]) -> Mascara {
        Mascara {
            texto: "t".into(),
            origen_x: 0,
            origen_y: 334,
            puntuacion: s,
            pixeles: pix.iter().copied().collect(),
        }
    }

    #[test]
    fn union_conserva_ambos_pixeles() {
        let a = mascara(0.9, &[(10, 320), (11, 320)]);
        let b = mascara(0.7, &[(11, 320), (12, 320)]);
        let u = union_geometrica(&[a, b]);
        assert_eq!(u.len(), 3);
        assert!(u.contains(&(11, 320)));
    }

    #[test]
    fn mayor_s_se_lleva_el_pixel_compartido() {
        let p = p_eps(0.02);
        let a = mascara(0.90, &[(10, 320), (11, 320)]);
        let b = mascara(0.70, &[(11, 320), (12, 320)]);
        let mapa = mapa_exclusivo(&[a, b], &p).unwrap();
        assert_eq!(mapa.get(&(11, 320)), Some(&0));
        assert_eq!(mapa.get(&(12, 320)), Some(&1));
    }

    #[test]
    fn empate_por_epsilon() {
        let p = p_eps(0.05);
        let a = mascara(0.80, &[(11, 320)]);
        let b = mascara(0.76, &[(11, 320)]);
        assert_eq!(atribuir(&[a, b], &p), Atribucion::Empate);
    }

    #[test]
    fn sin_solape_es_exclusiva() {
        let p = p_eps(0.02);
        let a = mascara(0.80, &[(10, 320)]);
        let b = mascara(0.80, &[(20, 320)]);
        assert_eq!(atribuir(&[a, b], &p), Atribucion::Exclusiva);
        let _ = BTreeSet::<(u32, u32)>::new();
    }

    /// Contraejemplo R1: A y C comparten píxel con |ΔS|≤epsilon; B lo cubre
    /// con S estrictamente mayor. El empate A–C no puede ocultarse.
    fn trio_contraejemplo() -> (Mascara, Mascara, Mascara) {
        let p = [(11u32, 320u32)];
        (
            mascara(0.80, &p),
            mascara(0.95, &p),
            mascara(0.82, &p),
        )
    }

    #[test]
    fn empate_en_las_seis_permutaciones() {
        let p = p_eps(0.05);
        let (a, b, c) = trio_contraejemplo();
        let ordenes: [&[Mascara]; 6] = [
            &[a.clone(), b.clone(), c.clone()],
            &[a.clone(), c.clone(), b.clone()],
            &[b.clone(), a.clone(), c.clone()],
            &[b.clone(), c.clone(), a.clone()],
            &[c.clone(), a.clone(), b.clone()],
            &[c.clone(), b.clone(), a.clone()],
        ];
        for (i, trio) in ordenes.iter().enumerate() {
            assert_eq!(
                atribuir(trio, &p),
                Atribucion::Empate,
                "permutacion {i} no declaró empate"
            );
        }
    }

    #[test]
    fn control_sin_empate_atribuye_al_mayor_s() {
        let p = p_eps(0.05);
        let a = mascara(0.70, &[(11, 320), (10, 320)]);
        let b = mascara(0.95, &[(11, 320)]);
        let c = mascara(0.80, &[(11, 320), (12, 320)]);
        let aceptadas = [a, b, c];
        assert_eq!(atribuir(&aceptadas, &p), Atribucion::Exclusiva);
        let mapa = mapa_exclusivo(&aceptadas, &p).unwrap();
        assert_eq!(mapa.get(&(11, 320)), Some(&1));
        let u = union_geometrica(&aceptadas);
        assert_eq!(u.len(), 3);
        assert!(u.contains(&(10, 320)));
        assert!(u.contains(&(11, 320)));
        assert!(u.contains(&(12, 320)));
    }
}
