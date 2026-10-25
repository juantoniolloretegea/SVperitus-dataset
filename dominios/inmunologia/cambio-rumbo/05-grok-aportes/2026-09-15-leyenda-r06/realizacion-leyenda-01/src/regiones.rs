//! Regiones geométricas del perfil SV-PNG16-LEYENDA/1.
//! Geometric regions of profile SV-PNG16-LEYENDA/1.
//! No dependen del color observado.

pub const ANCHO: u32 = 320;
pub const ALTO: u32 = 360;
pub const CUOTA_LECTURA: u64 = 1_000_000;

#[inline]
pub fn en_lienzo(x: u32, y: u32) -> bool {
    x < ANCHO && y < ALTO
}

/// G = [0,320)×[0,318)
#[inline]
pub fn en_figura(x: u32, y: u32) -> bool {
    en_lienzo(x, y) && y < 318
}

/// B = [15,310)×[318,344)
#[inline]
pub fn en_banda(x: u32, y: u32) -> bool {
    x >= 15 && x < 310 && y >= 318 && y < 344
}

/// W = L \\ (G ∪ B)
#[inline]
pub fn en_fondo_exigido(x: u32, y: u32) -> bool {
    en_lienzo(x, y) && !en_figura(x, y) && !en_banda(x, y)
}

pub const FILAS_ALINEACION: [u32; 4] = [334, 335, 336, 337];

// SPDX-License-Identifier: CC-BY-NC-ND-4.0
// © 2026 Juan Antonio Lloret Egea. Algunos derechos reservados. | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ – La Biblia de la IA™ | ISSN 2695-6411 | Licencia Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0).
// https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.es
