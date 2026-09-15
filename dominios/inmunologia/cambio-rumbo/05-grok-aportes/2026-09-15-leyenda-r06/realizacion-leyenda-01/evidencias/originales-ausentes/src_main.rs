//! Interfaz de línea de órdenes del prototipo LEYENDA-CONTENIDO/4.
//! Command-line interface of the LEYENDA-CONTENIDO/4 prototype.

use leyenda_contenido::parametros::Parametros;
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
    let huella = sha256_hex(&ttf);
    if !huella.eq_ignore_ascii_case(HUELLA_TTF) {
        eprintln!("TTF huella {huella} distinta de la contratada {HUELLA_TTF}");
        return ExitCode::from(1);
    }
    let inf = procesar_png(&PathBuf::from(&png), &ttf, &huella, &p);
    println!("DIAGNOSTICO\t{}", inf.diagnostico);
    println!("DETALLE\t{}", inf.detalle);
    for (e, r) in inf.pares {
        println!("PAR\t{e}\t{r}");
    }
    ExitCode::SUCCESS
}

fn sha256_hex(data: &[u8]) -> String {
    // Copia mínima de FIPS 180-4 para cotejar el TTF. No sustituye al cotejo histórico.
    fn rotr(x: u32, n: u32) -> u32 {
        x.rotate_right(n)
    }
    const K: [u32; 64] = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4,
        0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe,
        0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f,
        0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc,
        0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,
        0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116,
        0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7,
        0xc67178f2,
    ];
    let mut h: [u32; 8] = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab,
        0x5be0cd19,
    ];
    let bit_len = (data.len() as u64).saturating_mul(8);
    let mut msg = data.to_vec();
    msg.push(0x80);
    while msg.len() % 64 != 56 {
        msg.push(0);
    }
    msg.extend_from_slice(&bit_len.to_be_bytes());
    for chunk in msg.chunks_exact(64) {
        let mut w = [0u32; 64];
        for i in 0..16 {
            w[i] = u32::from_be_bytes(chunk[i * 4..i * 4 + 4].try_into().unwrap());
        }
        for i in 16..64 {
            let s0 = rotr(w[i - 15], 7) ^ rotr(w[i - 15], 18) ^ (w[i - 15] >> 3);
            let s1 = rotr(w[i - 2], 17) ^ rotr(w[i - 2], 19) ^ (w[i - 2] >> 10);
            w[i] = w[i - 16]
                .wrapping_add(s0)
                .wrapping_add(w[i - 7])
                .wrapping_add(s1);
        }
        let (mut a, mut b, mut c, mut d, mut e, mut f, mut g, mut hh) =
            (h[0], h[1], h[2], h[3], h[4], h[5], h[6], h[7]);
        for i in 0..64 {
            let t1 = hh
                .wrapping_add(rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25))
                .wrapping_add((e & f) ^ ((!e) & g))
                .wrapping_add(K[i])
                .wrapping_add(w[i]);
            let t2 = (rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22))
                .wrapping_add((a & b) ^ (a & c) ^ (b & c));
            hh = g;
            g = f;
            f = e;
            e = d.wrapping_add(t1);
            d = c;
            c = b;
            b = a;
            a = t1.wrapping_add(t2);
        }
        h[0] = h[0].wrapping_add(a);
        h[1] = h[1].wrapping_add(b);
        h[2] = h[2].wrapping_add(c);
        h[3] = h[3].wrapping_add(d);
        h[4] = h[4].wrapping_add(e);
        h[5] = h[5].wrapping_add(f);
        h[6] = h[6].wrapping_add(g);
        h[7] = h[7].wrapping_add(hh);
    }
    h.iter().flat_map(|v| v.to_be_bytes()).map(|b| format!("{b:02x}")).collect()
}
