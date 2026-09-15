//! Interfaz de línea de órdenes del prototipo LEYENDA-CONTENIDO/4.
//! Command-line interface of the LEYENDA-CONTENIDO/4 prototype.

use leyenda_contenido::parametros::Parametros;
use leyenda_contenido::sha256;
use leyenda_contenido::{procesar_png, HUELLA_TTF};
use std::env;
use std::fs;
use std::path::PathBuf;
use std::process::ExitCode;

fn ayuda() {
    eprintln!(
        "leyenda_contenido — prototipo experimental LEYENDA-CONTENIDO/4\n\
         \n\
         Uso:\n\
           leyenda_contenido ayuda\n\
           leyenda_contenido reconocer --png RUTA --fuente RUTA.ttf --parametros RUTA.txt\n\
         \n\
         No hay valores de parámetro implícitos. Compilar no cualifica el método.\n\
         Q1/Q2 no deben invocarse hasta que el protocolo de cualificación lo autorice."
    );
}

fn main() -> ExitCode {
    let mut args: Vec<String> = env::args().skip(1).collect();
    if args.is_empty() || args[0] == "ayuda" || args[0] == "--help" || args[0] == "-h" {
        ayuda();
        return ExitCode::from(2);
    }
    if args[0] != "reconocer" {
        eprintln!("orden desconocida: {}", args[0]);
        ayuda();
        return ExitCode::from(2);
    }
    args.remove(0);
    let mut png = None;
    let mut fuente = None;
    let mut parametros = None;
    let mut i = 0;
    while i < args.len() {
        match args[i].as_str() {
            "--png" => {
                png = args.get(i + 1).cloned();
                i += 2;
            }
            "--fuente" => {
                fuente = args.get(i + 1).cloned();
                i += 2;
            }
            "--parametros" => {
                parametros = args.get(i + 1).cloned();
                i += 2;
            }
            otro => {
                eprintln!("argumento no reconocido: {otro}");
                return ExitCode::from(2);
            }
        }
    }
    let (Some(png), Some(fuente), Some(parametros)) = (png, fuente, parametros) else {
        eprintln!("faltan --png, --fuente o --parametros");
        return ExitCode::from(2);
    };
    let p = match Parametros::desde_archivo(&PathBuf::from(&parametros)) {
        Ok(p) => p,
        Err(e) => {
            eprintln!("parametros: {e}");
            return ExitCode::from(2);
        }
    };
    let ttf = match fs::read(&fuente) {
        Ok(b) => b,
        Err(e) => {
            eprintln!("fuente: {e}");
            return ExitCode::from(1);
        }
    };
    let huella = sha256::hex(&ttf);
    if !huella.eq_ignore_ascii_case(HUELLA_TTF) {
        eprintln!("TTF huella {huella} distinta de la contratada {HUELLA_TTF}");
        return ExitCode::from(1);
    }
    let inf = procesar_png(&PathBuf::from(&png), &ttf, &p);
    println!("DIAGNOSTICO\t{}", inf.diagnostico);
    println!("DETALLE\t{}", inf.detalle);
    for (e, r) in inf.pares {
        println!("PAR\t{e}\t{r}");
    }
    ExitCode::SUCCESS
}
