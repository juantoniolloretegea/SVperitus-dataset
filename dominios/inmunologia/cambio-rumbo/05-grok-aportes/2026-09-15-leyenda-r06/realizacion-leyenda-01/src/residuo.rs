//! Residuo, antialiasing admitido y causas B.6.
//! Residue, admitted antialiasing and B.6 rejection causes.

use crate::atribucion::union_geometrica;
use crate::parametros::Parametros;
use crate::plantillas::Mascara;
use std::collections::BTreeSet;

pub struct Residuo {
    pub i_aa: BTreeSet<(u32, u32)>,
    pub i_res: BTreeSet<(u32, u32)>,
    pub r_abs: u32,
    pub r_rel: f64,
    pub componentes: Vec<BTreeSet<(u32, u32)>>,
}

pub fn calcular(
    tinta_banda: &BTreeSet<(u32, u32)>,
    aceptadas: &[Mascara],
) -> Residuo {
    let m_expl = union_geometrica(aceptadas);
    let mut h_expl = BTreeSet::new();
    for m in aceptadas {
        h_expl.extend(m.anillo());
    }
    let tinta_expl: BTreeSet<(u32, u32)> = m_expl.intersection(tinta_banda).cloned().collect();
    let vecindad_tinta_expl = vecindad4(&tinta_expl);
    let mut i_aa = BTreeSet::new();
    for p in tinta_banda {
        if h_expl.contains(p) && vecindad_tinta_expl.contains(p) {
            i_aa.insert(*p);
        }
    }
    let mut i_res = BTreeSet::new();
    for p in tinta_banda {
        if !m_expl.contains(p) && !i_aa.contains(p) {
            i_res.insert(*p);
        }
    }
    let r_abs = i_res.len() as u32;
    let r_rel = r_abs as f64 / (tinta_banda.len().max(1) as f64);
    let componentes = componentes4(&i_res);
    Residuo {
        i_aa,
        i_res,
        r_abs,
        r_rel,
        componentes,
    }
}

pub fn adicion_inadmisible(res: &Residuo, p: &Parametros, plantilla_no_asignada: bool) -> bool {
    if plantilla_no_asignada {
        return true;
    }
    if res.r_rel > p.rho || res.r_abs > p.r_max {
        return true;
    }
    res.componentes.iter().any(|c| c.len() as u32 >= p.a_min)
}

fn vecindad4(s: &BTreeSet<(u32, u32)>) -> BTreeSet<(u32, u32)> {
    let mut o = BTreeSet::new();
    for &(x, y) in s {
        o.insert((x, y));
        if x > 0 {
            o.insert((x - 1, y));
        }
        o.insert((x + 1, y));
        if y > 0 {
            o.insert((x, y - 1));
        }
        o.insert((x, y + 1));
    }
    o
}

fn componentes4(s: &BTreeSet<(u32, u32)>) -> Vec<BTreeSet<(u32, u32)>> {
    let mut resto = s.clone();
    let mut out = Vec::new();
    while let Some(&start) = resto.iter().next() {
        let mut pila = vec![start];
        let mut comp = BTreeSet::new();
        resto.remove(&start);
        while let Some((x, y)) = pila.pop() {
            comp.insert((x, y));
            let vecinos = [
                (x.wrapping_sub(1), y),
                (x + 1, y),
                (x, y.wrapping_sub(1)),
                (x, y + 1),
            ];
            for v in vecinos {
                if resto.remove(&v) {
                    pila.push(v);
                }
            }
        }
        out.push(comp);
    }
    out
}
