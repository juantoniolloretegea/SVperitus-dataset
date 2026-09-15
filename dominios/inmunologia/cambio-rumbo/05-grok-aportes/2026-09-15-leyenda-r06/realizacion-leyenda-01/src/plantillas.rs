//! Síntesis de plantillas del vocabulario cerrado con fontdue.
//! Closed-vocabulary template synthesis via fontdue.
//! El TTF contratado se suministra por ruta; no se sustituye.

use crate::parametros::Parametros;
use crate::regiones::{ALTO, ANCHO, en_banda};
use std::collections::BTreeSet;

pub const HUELLA_TTF_CONTRATADA: &str =
    "ae7b7855e115a5966d8b1b3f80f254ccc117ec86f9965e202ee2940453837280";

/// Lectura candidata del SVG histórico: el separador visible es U+007C.
/// Candidate reading of the historical SVG: the visible separator is U+007C.
pub const TEXTO_SEPARADOR: &str = "|";

pub const VOCABULARIO: &[&str] = &[
    "0:",
    "1:",
    "U:",
    "radio 1",
    "radio 2",
    "radio 3",
    TEXTO_SEPARADOR,
];

pub const ETIQUETAS: &[&str] = &["0:", "1:", "U:"];
pub const RADIOS: &[&str] = &["radio 1", "radio 2", "radio 3"];

#[derive(Clone, Debug)]
pub struct Mascara {
    pub texto: String,
    pub origen_x: i32,
    pub origen_y: i32,
    pub pixeles: BTreeSet<(u32, u32)>,
}

impl Mascara {
    pub fn anillo(&self) -> BTreeSet<(u32, u32)> {
        let mut h = BTreeSet::new();
        for &(x, y) in &self.pixeles {
            for (dx, dy) in [(-1i32, 0), (1, 0), (0, -1), (0, 1)] {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;
                if nx < 0 || ny < 0 {
                    continue;
                }
                let ux = nx as u32;
                let uy = ny as u32;
                if ux < ANCHO && uy < ALTO && !self.pixeles.contains(&(ux, uy)) {
                    h.insert((ux, uy));
                }
            }
        }
        h
    }
}

pub struct Sintetizador {
    font: fontdue::Font,
}

impl Sintetizador {
    pub fn cargar(ttf: &[u8], huella_hex: &str) -> Result<Self, String> {
        if !huella_hex.eq_ignore_ascii_case(HUELLA_TTF_CONTRATADA) {
            return Err(format!(
                "TTF distinto del contratado: {huella_hex} ≠ {HUELLA_TTF_CONTRATADA}"
            ));
        }
        let font = fontdue::Font::from_bytes(ttf, fontdue::FontSettings::default())
            .map_err(|e| format!("fontdue: {e}"))?;
        Ok(Self { font })
    }

    pub fn raster(&self, texto: &str, x0: i32, y_base: i32, p: &Parametros) -> Mascara {
        let mut pixeles = BTreeSet::new();
        let mut cursor = 0.0f32;
        for ch in texto.chars() {
            let (metrics, bitmap) = self.font.rasterize(ch, p.s_px);
            let ox = x0 + cursor as i32 + metrics.xmin;
            let oy = y_base - metrics.height as i32 - metrics.ymin;
            for row in 0..metrics.height {
                for col in 0..metrics.width {
                    let cov = bitmap[row * metrics.width + col];
                    if cov < p.tau_t {
                        continue;
                    }
                    let px = ox + col as i32;
                    let py = oy + row as i32;
                    if px < 0 || py < 0 {
                        continue;
                    }
                    let ux = px as u32;
                    let uy = py as u32;
                    if en_banda(ux, uy) {
                        pixeles.insert((ux, uy));
                    }
                }
            }
            cursor += metrics.advance_width;
        }
        Mascara {
            texto: texto.to_string(),
            origen_x: x0,
            origen_y: y_base,
            pixeles,
        }
    }
}

pub fn coincidencia(mascara: &Mascara, tinta: &BTreeSet<(u32, u32)>) -> f64 {
    if mascara.pixeles.is_empty() {
        return 0.0;
    }
    let cubiertos = mascara.pixeles.intersection(tinta).count();
    cubiertos as f64 / mascara.pixeles.len() as f64
}
