//! Cotejo documental de la entrega TLC-S32-01 v0.1.
//! Biblioteca estándar. Git para identidad de blobs.
//! Uso: rustup run 1.98.0 rustc --edition=2021 COTEJO_ENTREGA.rs -o /tmp/cotejo-tlc
//!      RUSTC=$(rustup run 1.98.0 which rustc) /tmp/cotejo-tlc DIR_ENTREGA
//! No ejecuta casos de privacidad ni habilita el trayecto.
use std::fs;
use std::path::Path;
use std::process::{Command, ExitCode};

fn hash_object(path: &Path) -> Result<String, String> {
    let out = Command::new("git")
        .arg("hash-object")
        .arg(path)
        .output()
        .map_err(|e| format!("git: {e}"))?;
    if !out.status.success() {
        return Err(format!(
            "git hash-object {}: {}",
            path.display(),
            String::from_utf8_lossy(&out.stderr)
        ));
    }
    Ok(String::from_utf8_lossy(&out.stdout).trim().to_string())
}

fn must_contain(text: &str, needles: &[&str], label: &str) -> Result<(), String> {
    for n in needles {
        if !text.contains(n) {
            return Err(format!("{label}: falta {n}"));
        }
    }
    Ok(())
}

fn main() -> ExitCode {
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 2 {
        eprintln!("uso: cotejo DIR_ENTREGA");
        return ExitCode::from(2);
    }
    let dir = Path::new(&args[1]);
    let mut report = String::new();
    report.push_str("COTEJO TLC-S32-01 v0.1\n");
    report.push_str("Objeto: integridad documental del paquete candidato.\n");
    report.push_str("No es prueba de privacidad, Q1/Q2 ni E1–E16.\n");

    let rustc_bin = std::env::var("RUSTC").unwrap_or_else(|_| "rustc".into());
    let rustc = Command::new(&rustc_bin)
        .arg("-Vv")
        .output()
        .unwrap_or_else(|e| panic!("{rustc_bin}: {e}"));
    if !rustc.status.success() {
        eprintln!("rustc -Vv falló");
        return ExitCode::from(1);
    }
    let rustc_txt = String::from_utf8_lossy(&rustc.stdout);
    if !rustc_txt.contains("release: 1.98.0") {
        eprintln!("se exige rustc 1.98.0, obtenido:\n{rustc_txt}");
        return ExitCode::from(1);
    }
    report.push_str(&rustc_txt);
    report.push('\n');

    let files = [
        "CONTRATO_CANDIDATO_TLC_S32_01_v0.1.md",
        "CASOS_PREVISTOS_TLC_S32_01_v0.1.md",
        "NOTA_ENTREGA.md",
        "COTEJO_ENTREGA.rs",
        "ENTORNO_MINIMO.rs",
        "ENTORNO_MINIMO_SALIDA.txt",
    ];
    for f in files {
        let p = dir.join(f);
        if !p.is_file() {
            eprintln!("falta {f}");
            return ExitCode::from(1);
        }
        match hash_object(&p) {
            Ok(h) => report.push_str(&format!("BLOB {h} {f}\n")),
            Err(e) => {
                eprintln!("{e}");
                return ExitCode::from(1);
            }
        }
    }

    let contrato = fs::read_to_string(dir.join(files[0])).unwrap();
    if let Err(e) = must_contain(
        &contrato,
        &[
            "TLC-S32-01",
            "I-CONSULTA-LOCAL",
            "I-AUTORIZACION",
            "I-SALIDA-VISTA",
            "I-EVIDENCIA-MINIMA",
            "no ejecutado",
            "P01–P10",
            "C17",
            "03578e3c3919d38ed1ae1dbc686d36ea9147c0b6",
            "Decisiones pendientes concretas",
        ],
        "contrato",
    ) {
        eprintln!("{e}");
        return ExitCode::from(1);
    }
    if contrato.contains("RETP-2026-250") {
        eprintln!("el candidato no debe asignar RETP");
        return ExitCode::from(1);
    }

    let casos = fs::read_to_string(dir.join(files[1])).unwrap();
    for id in [
        "TLC-01", "TLC-02", "TLC-03", "TLC-04", "TLC-05", "TLC-06", "TLC-07", "TLC-08", "TLC-09",
        "TLC-10", "TLC-11", "TLC-12", "TLC-13", "TLC-14",
    ] {
        if !casos.contains(id) {
            eprintln!("falta caso {id}");
            return ExitCode::from(1);
        }
    }
    let pendientes = casos.matches("no ejecutado: implementación pendiente").count();
    if pendientes < 14 {
        eprintln!("cada caso debe declarar no ejecutado; encontrados {pendientes}");
        return ExitCode::from(1);
    }
    if casos.contains("prueba de privacidad superada") {
        eprintln!("no se admite declarar pruebas de privacidad superadas");
        return ExitCode::from(1);
    }

    let nota = fs::read_to_string(dir.join(files[2])).unwrap();
    if let Err(e) = must_contain(
        &nota,
        &[
            "03578e3c3919d38ed1ae1dbc686d36ea9147c0b6",
            "S32",
            "1.98.0",
            "COTEJO_ENTREGA.rs",
        ],
        "nota",
    ) {
        eprintln!("{e}");
        return ExitCode::from(1);
    }

    report.push_str("CONTROL contrato: marcadores presentes; sin RETP nuevo.\n");
    report.push_str("CONTROL casos: TLC-01..TLC-14; 14 no ejecutados.\n");
    report.push_str("CONTROL nota: cortes y entorno presentes.\n");
    report.push_str("DISPOSICION: paquete documental cotejado.\n");
    report.push_str("PRIVACIDAD: no ejecutada.\n");
    print!("{report}");
    ExitCode::SUCCESS
}
