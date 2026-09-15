//! Lectura acotada y decodificación PNG.
//! Bounded read and PNG decode.
//! Usa el crate `png`, no tiny-skia.

use crate::diagnostico::Diagnostico;
use crate::regiones::{ALTO, ANCHO, CUOTA_LECTURA, en_fondo_exigido};
use std::fs;
use std::path::Path;

const FIRMA: &[u8] = b"\x89PNG\r\n\x1a\n";

pub struct Lienzo {
    pub ancho: u32,
    pub alto: u32,
    /// RGB por píxel, fila mayor.
    pub rgb: Vec<u8>,
    pub alfa: Vec<u8>,
}

pub struct Lectura {
    pub diagnostico: Diagnostico,
    pub detalle: String,
    pub lienzo: Option<Lienzo>,
}

pub fn leer_y_decodificar(path: &Path) -> Lectura {
    let meta = match fs::metadata(path) {
        Ok(m) => m,
        Err(e) => {
            return Lectura {
                diagnostico: Diagnostico::FalloLectura,
                detalle: format!("E/S: {e}"),
                lienzo: None,
            };
        }
    };
    if meta.len() > CUOTA_LECTURA {
        return Lectura {
            diagnostico: Diagnostico::FalloLectura,
            detalle: format!("longitud {} supera cuota {CUOTA_LECTURA}", meta.len()),
            lienzo: None,
        };
    }
    let bytes = match fs::read(path) {
        Ok(b) => b,
        Err(e) => {
            return Lectura {
                diagnostico: Diagnostico::FalloLectura,
                detalle: format!("E/S: {e}"),
                lienzo: None,
            };
        }
    };
    if bytes.len() < 8 || &bytes[..8] != FIRMA {
        return Lectura {
            diagnostico: Diagnostico::FueraDePerfilFormato,
            detalle: "firma distinta de PNG".into(),
            lienzo: None,
        };
    }
    decodificar(&bytes)
}

fn decodificar(bytes: &[u8]) -> Lectura {
    let mut decoder = png::Decoder::new(std::io::Cursor::new(bytes));
    decoder.set_transformations(png::Transformations::EXPAND | png::Transformations::STRIP_16);
    let mut reader = match decoder.read_info() {
        Ok(r) => r,
        Err(e) => {
            return Lectura {
                diagnostico: Diagnostico::FalloDecodificacion,
                detalle: format!("png::read_info: {e}"),
                lienzo: None,
            };
        }
    };
    let info = reader.info();
    if info.width != ANCHO || info.height != ALTO {
        return Lectura {
            diagnostico: Diagnostico::FueraDePerfilFormato,
            detalle: format!("lienzo {}x{}, se exige {ANCHO}x{ALTO}", info.width, info.height),
            lienzo: None,
        };
    }
    if info.bit_depth != png::BitDepth::Eight {
        return Lectura {
            diagnostico: Diagnostico::FueraDePerfilFormato,
            detalle: format!("profundidad {:?}", info.bit_depth),
            lienzo: None,
        };
    }
    let mut buf = vec![0u8; reader.output_buffer_size()];
    let frame = match reader.next_frame(&mut buf) {
        Ok(f) => f,
        Err(e) => {
            return Lectura {
                diagnostico: Diagnostico::FalloDecodificacion,
                detalle: format!("png::next_frame: {e}"),
                lienzo: None,
            };
        }
    };
    let (rgb, alfa, tiene_canal_alfa) = separar_canales(frame.color_type, frame.width, frame.height, &buf);
    if tiene_canal_alfa && alfa.iter().any(|&a| a != 255) {
        return Lectura {
            diagnostico: Diagnostico::FueraDePerfilTransparencia,
            detalle: "existe muestra de alfa distinta de 255".into(),
            lienzo: Some(Lienzo {
                ancho: frame.width,
                alto: frame.height,
                rgb,
                alfa,
            }),
        };
    }
    for y in 0..frame.height {
        for x in 0..frame.width {
            if en_fondo_exigido(x, y) {
                let i = ((y * frame.width + x) * 3) as usize;
                if rgb[i] != 255 || rgb[i + 1] != 255 || rgb[i + 2] != 255 {
                    return Lectura {
                        diagnostico: Diagnostico::FueraDePerfilFondo,
                        detalle: format!("W no blanco en ({x},{y})"),
                        lienzo: Some(Lienzo {
                            ancho: frame.width,
                            alto: frame.height,
                            rgb,
                            alfa,
                        }),
                    };
                }
            }
        }
    }
    Lectura {
        diagnostico: Diagnostico::CorrespondenciaConforme,
        detalle: "perfil geometrico y opacidad provisionales".into(),
        lienzo: Some(Lienzo {
            ancho: frame.width,
            alto: frame.height,
            rgb,
            alfa,
        }),
    }
}

fn separar_canales(
    color: png::ColorType,
    w: u32,
    h: u32,
    buf: &[u8],
) -> (Vec<u8>, Vec<u8>, bool) {
    let n = (w * h) as usize;
    let mut rgb = vec![255u8; n * 3];
    let mut alfa = vec![255u8; n];
    match color {
        png::ColorType::Rgb => {
            rgb.copy_from_slice(&buf[..n * 3]);
            (rgb, alfa, false)
        }
        png::ColorType::Rgba => {
            for i in 0..n {
                rgb[i * 3] = buf[i * 4];
                rgb[i * 3 + 1] = buf[i * 4 + 1];
                rgb[i * 3 + 2] = buf[i * 4 + 2];
                alfa[i] = buf[i * 4 + 3];
            }
            (rgb, alfa, true)
        }
        png::ColorType::Grayscale => {
            for i in 0..n {
                let g = buf[i];
                rgb[i * 3] = g;
                rgb[i * 3 + 1] = g;
                rgb[i * 3 + 2] = g;
            }
            (rgb, alfa, false)
        }
        png::ColorType::GrayscaleAlpha => {
            for i in 0..n {
                let g = buf[i * 2];
                rgb[i * 3] = g;
                rgb[i * 3 + 1] = g;
                rgb[i * 3 + 2] = g;
                alfa[i] = buf[i * 2 + 1];
            }
            (rgb, alfa, true)
        }
        other => {
            // EXPAND debería haber reducido paleta; si no, se trata como fallo más adelante.
            let _ = other;
            (rgb, alfa, false)
        }
    }
}

pub fn tinta_en_banda(lienzo: &Lienzo) -> Vec<(u32, u32)> {
    let mut out = Vec::new();
    for y in 318..344 {
        for x in 15..310 {
            let i = ((y * lienzo.ancho + x) * 3) as usize;
            if lienzo.rgb[i] != 255 || lienzo.rgb[i + 1] != 255 || lienzo.rgb[i + 2] != 255 {
                out.push((x, y));
            }
        }
    }
    out
}
