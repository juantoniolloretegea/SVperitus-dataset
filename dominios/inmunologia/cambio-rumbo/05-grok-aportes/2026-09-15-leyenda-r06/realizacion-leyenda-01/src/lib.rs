//! Prototipo experimental LEYENDA-CONTENIDO/4.
//! Experimental prototype for LEYENDA-CONTENIDO/4.
//!
//! Compilar no cualifica el reconocedor. Q1/Q2 no se ejecutan en esta entrega.

pub mod diagnostico;
pub mod parametros;
pub mod plantillas;
pub mod png_lectura;
pub mod reconocimiento;
pub mod regiones;
pub mod residuo;
pub mod sha256;

use crate::diagnostico::Diagnostico;
use crate::parametros::Parametros;
use crate::plantillas::Sintetizador;
use crate::png_lectura::leer_y_decodificar;
use crate::reconocimiento::{reconocer, Informe};
use std::path::Path;

pub const HUELLA_TTF: &str = plantillas::HUELLA_TTF_CONTRATADA;

pub fn procesar_png(png: &Path, ttf: &[u8], p: &Parametros) -> Informe {
    let lectura = leer_y_decodificar(png);
    match lectura.diagnostico {
        Diagnostico::CorrespondenciaConforme => {}
        otro => {
            return Informe {
                diagnostico: otro,
                detalle: lectura.detalle,
                pares: vec![],
            };
        }
    }
    let Some(lienzo) = lectura.lienzo else {
        return Informe {
            diagnostico: Diagnostico::FalloDecodificacion,
            detalle: "sin lienzo tras decodificacion".into(),
            pares: vec![],
        };
    };
    let sintetizador = match Sintetizador::cargar(ttf) {
        Ok(s) => s,
        Err(e) => {
            return Informe {
                diagnostico: Diagnostico::FalloLectura,
                detalle: e,
                pares: vec![],
            };
        }
    };
    reconocer(&lienzo, &sintetizador, p)
}
