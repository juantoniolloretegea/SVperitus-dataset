//! Códigos de /4 §A y precedencia estricta.
//! Diagnostic codes of /4 §A and strict precedence.

use std::fmt;

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Diagnostico {
    FalloLectura,
    FueraDePerfilFormato,
    FalloDecodificacion,
    FueraDePerfilTransparencia,
    FueraDePerfilFondo,
    LeyendaAusente,
    LeyendaIlegible,
    DiscordanciaContenido,
    CorrespondenciaConforme,
}

impl Diagnostico {
    pub fn id(self) -> &'static str {
        match self {
            Self::FalloLectura => "FALLO_LECTURA",
            Self::FueraDePerfilFormato => "FUERA_DE_PERFIL_FORMATO",
            Self::FalloDecodificacion => "FALLO_DECODIFICACION",
            Self::FueraDePerfilTransparencia => "FUERA_DE_PERFIL_TRANSPARENCIA",
            Self::FueraDePerfilFondo => "FUERA_DE_PERFIL_FONDO",
            Self::LeyendaAusente => "LEYENDA_AUSENTE",
            Self::LeyendaIlegible => "LEYENDA_ILEGIBLE",
            Self::DiscordanciaContenido => "DISCORDANCIA_CONTENIDO",
            Self::CorrespondenciaConforme => "CORRESPONDENCIA_CONFORME",
        }
    }

    pub fn rango(self) -> u8 {
        match self {
            Self::FalloLectura => 1,
            Self::FueraDePerfilFormato => 2,
            Self::FalloDecodificacion => 3,
            Self::FueraDePerfilTransparencia => 4,
            Self::FueraDePerfilFondo => 5,
            Self::LeyendaAusente => 6,
            Self::LeyendaIlegible => 7,
            Self::DiscordanciaContenido => 8,
            Self::CorrespondenciaConforme => 9,
        }
    }
}

impl fmt::Display for Diagnostico {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str(self.id())
    }
}

/// Elige el código de menor rango (mayor prioridad).
pub fn precedencia(a: Diagnostico, b: Diagnostico) -> Diagnostico {
    if a.rango() <= b.rango() {
        a
    } else {
        b
    }
}
