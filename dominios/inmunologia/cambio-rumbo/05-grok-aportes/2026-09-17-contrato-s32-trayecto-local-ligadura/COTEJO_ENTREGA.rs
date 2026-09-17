//! Cotejo documental de la entrega TLC-S32-02 v0.1.
//! Biblioteca estándar. Git para identidad de blobs.
//! Uso: rustup run 1.98.0 rustc --edition=2021 COTEJO_ENTREGA.rs -o /tmp/cotejo-tlc-02
//!      RUSTC=$(rustup +1.98.0 which rustc) /tmp/cotejo-tlc-02 DIR_ENTREGA
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
    report.push_str("COTEJO TLC-S32-02 v0.1\n");
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
        "CONTRATO_CANDIDATO_TLC_S32_02_v0.1.md",
        "CASOS_PREVISTOS_TLC_S32_02_v0.1.md",
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

    let contrato = fs::read_to_string(dir.join("CONTRATO_CANDIDATO_TLC_S32_02_v0.1.md"))
        .expect("contrato");
    let casos = fs::read_to_string(dir.join("CASOS_PREVISTOS_TLC_S32_02_v0.1.md")).expect("casos");
    let nota = fs::read_to_string(dir.join("NOTA_ENTREGA.md")).expect("nota");

    if let Err(e) = must_contain(
        &contrato,
        &[
            "TLC-S32-02",
            "I-CONSULTA-LOCAL",
            "I-AUTORIZACION",
            "I-SALIDA-VISTA",
            "I-EVIDENCIA-MINIMA",
            "decide_permit_traced",
            "CaptureOutcome",
            "AdmissibilityState",
            "03578e3c3919d38ed1ae1dbc686d36ea9147c0b6",
            "control compuesto de estado inicial y continuidad",
            "no se habilita",
            "etiquetas documentales",
            "QuerySpec",
            "no cubre por sí solo",
            "P01–P10",
        ],
        "contrato",
    ) {
        eprintln!("{e}");
        return ExitCode::from(1);
    }
    if contrato.contains("RETP-2026-250")
        || contrato.contains("S32 permanece cerrado")
        || contrato.contains("cierre de S32 ejecutado")
    {
        eprintln!("el contrato no debe asignar RETP nuevo ni cerrar S32");
        return ExitCode::from(1);
    }
    if let Err(e) = must_contain(
        &casos,
        &[
            "no ejecutado: implementación pendiente",
            "TLC-10",
            "TLC-11",
            "TLC-16",
            "TLC-18",
            "TLC-19",
            "P05",
        ],
        "casos",
    ) {
        eprintln!("{e}");
        return ExitCode::from(1);
    }
    let ejecutados = casos.matches("ejecutado: implementación ejecutada").count();
    if ejecutados != 0 {
        eprintln!("aparecen casos ejecutados");
        return ExitCode::from(1);
    }
    if let Err(e) = must_contain(
        &nota,
        &[
            "03578e3c3919d38ed1ae1dbc686d36ea9147c0b6",
            "S32 permanece en ejecución",
            "ok-minimo",
            "1.98.0",
        ],
        "nota",
    ) {
        eprintln!("{e}");
        return ExitCode::from(1);
    }

    report.push_str("RESULTADO: cotejo documental conforme.\n");
    report.push_str("PRIVACIDAD: no ejecutada.\n");
    print!("{report}");
    ExitCode::SUCCESS
}
