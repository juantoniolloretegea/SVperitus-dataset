//! Cotejo auxiliar de identidad SHA-256. No es un banco SV.
//! Cadena exigida: rustc 1.98.0. Sin dependencias externas.
#![forbid(unsafe_code)]

fn rotr(x: u32, n: u32) -> u32 {
    x.rotate_right(n)
}

fn sha256(data: &[u8]) -> [u8; 32] {
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
    while (msg.len() % 64) != 56 {
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
        let mut a = h[0];
        let mut b = h[1];
        let mut c = h[2];
        let mut d = h[3];
        let mut e = h[4];
        let mut f = h[5];
        let mut g = h[6];
        let mut hh = h[7];
        for i in 0..64 {
            let s1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25);
            let ch = (e & f) ^ ((!e) & g);
            let t1 = hh
                .wrapping_add(s1)
                .wrapping_add(ch)
                .wrapping_add(K[i])
                .wrapping_add(w[i]);
            let s0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22);
            let maj = (a & b) ^ (a & c) ^ (b & c);
            let t2 = s0.wrapping_add(maj);
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
    let mut out = [0u8; 32];
    for (i, v) in h.iter().enumerate() {
        out[i * 4..i * 4 + 4].copy_from_slice(&v.to_be_bytes());
    }
    out
}

fn hex_of(d: &[u8; 32]) -> String {
    d.iter().map(|b| format!("{b:02x}")).collect()
}

fn hex_eq(got: &str, expected: &str) -> bool {
    got.eq_ignore_ascii_case(expected)
}

fn read_file(path: &str) -> Result<Vec<u8>, String> {
    std::fs::read(path).map_err(|e| format!("{path}: {e}"))
}

fn report(id: &str, path: &str, got: &str, expected: Option<&str>, extra: &str) {
    match expected {
        Some(exp) => {
            let ok = hex_eq(got, exp);
            println!(
                "CASO\t{id}\truta={path}\thuella={got}\tesperada={exp}\tigual={ok}\t{extra}"
            );
        }
        None => {
            println!("CASO\t{id}\truta={path}\thuella={got}\tesperada=NO_DECLARADA\tigual=NA\t{extra}");
        }
    }
}

fn main() {
    let mut fallos = 0u32;

    // Vectores FIPS 180-4 / NIST
    let vectores: &[(&str, &[u8], &str)] = &[
        ("V_VACIO", b"", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
        ("V_ABC", b"abc", "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"),
        (
            "V_56",
            b"abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq",
            "248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1",
        ),
    ];
    for (id, data, exp) in vectores {
        let got = hex_of(&sha256(data));
        let ok = hex_eq(&got, exp);
        if !ok {
            fallos += 1;
        }
        println!("VECTOR\t{id}\thuella={got}\tesperada={exp}\tigual={ok}");
    }
    if fallos != 0 {
        eprintln!("FALLO_VECTOR: el calculo SHA-256 no coincide con NIST; no se cotejan testigos.");
        std::process::exit(2);
    }

    struct Item {
        id: &'static str,
        path: &'static str,
        expected: Option<&'static str>,
        extra: &'static str,
    }
    let items = [
        Item {
            id: "TAR_EVIDENCIA",
            path: "/tmp/EVIDENCIA_RASTER_CAPTOR_86441ad4.tar.gz",
            expected: Some("2af2487c24c08cd1f73addc74a6c2bceaffbabfa69b0123289915b02a2ce29b3"),
            extra: "comunicada_transporte_previo",
        },
        Item {
            id: "R01_PNG_PAQUETE",
            path: "/tmp/wit_R01.png",
            expected: Some("3e9fae6d4844a07d0f1281d4974c5da1c5ce01c6dbc774be27b18f1735f7509d"),
            extra: "documental_IDENTIDADES_y_RESULTADOS",
        },
        Item {
            id: "MUESTRA_PNG",
            path: "/tmp/MUESTRA_RASTER_PRODUCIDA.png",
            expected: Some("3e9fae6d4844a07d0f1281d4974c5da1c5ce01c6dbc774be27b18f1735f7509d"),
            extra: "documental_igual_R01",
        },
        Item {
            id: "ENTRADA_SVG_PAQUETE",
            path: "/tmp/wit_entrada.svg",
            expected: Some("e5a9f9bc6df9b4f59a2a0cb908046239fda11ebbc247577b8e8c32b268a8c578"),
            extra: "documental_IDENTIDADES_SVG",
        },
        Item {
            id: "MUESTRA_SVG",
            path: "/tmp/MUESTRA_SVG_PRODUCIDA.svg",
            expected: Some("e5a9f9bc6df9b4f59a2a0cb908046239fda11ebbc247577b8e8c32b268a8c578"),
            extra: "documental_igual_entrada",
        },
        Item {
            id: "R06_PNG",
            path: "/tmp/wit_R06.png",
            expected: Some("829286631401c3208554a9f1f81bc091fa5355201490bd92ba72f9b0bb254827"),
            extra: "comunicada_transporte_previo_no_en_IDENTIDADES",
        },
        Item {
            id: "R06_SVG",
            path: "/tmp/wit_R06.svg",
            expected: Some("6dec0798aece0d08be42701fd0856f3c92cc2ba5dc5b2250490f46ce8c5f87a3"),
            extra: "comunicada_transporte_previo_no_en_IDENTIDADES",
        },
        Item {
            id: "IDENTIDADES_TXT",
            path: "/tmp/wit_IDENTIDADES.txt",
            expected: Some("417bab155f87aaf3c8f9188cefd93498c93c5983e3cde9d7df76ebd964dfa178"),
            extra: "comunicada_transporte_previo",
        },
    ];

    let mut disc = 0u32;
    for it in items {
        match read_file(it.path) {
            Ok(b) => {
                let got = hex_of(&sha256(&b));
                report(it.id, it.path, &got, it.expected, it.extra);
                if let Some(exp) = it.expected {
                    if !hex_eq(&got, exp) {
                        disc += 1;
                    }
                }
            }
            Err(e) => {
                println!(
                    "CASO\t{}\truta={}\thuella=ERROR\tesperada={:?}\tigual=ERROR\t{e}",
                    it.id, it.path, it.expected
                );
                disc += 1;
            }
        }
    }

    let r01 = read_file("/tmp/wit_R01.png").ok();
    let muestra_png = read_file("/tmp/MUESTRA_RASTER_PRODUCIDA.png").ok();
    let entrada = read_file("/tmp/wit_entrada.svg").ok();
    let muestra_svg = read_file("/tmp/MUESTRA_SVG_PRODUCIDA.svg").ok();
    let r06p = read_file("/tmp/wit_R06.png").ok();
    let r06s = read_file("/tmp/wit_R06.svg").ok();

    let eq_png = matches!((&r01, &muestra_png), (Some(a), Some(b)) if a == b);
    let eq_svg = matches!((&entrada, &muestra_svg), (Some(a), Some(b)) if a == b);
    let ne_r06_png = matches!((&r01, &r06p), (Some(a), Some(b)) if a != b);
    let ne_r06_svg = matches!((&entrada, &r06s), (Some(a), Some(b)) if a != b);
    println!("IGUALDAD\tR01_paquete==MUESTRA_png\t{eq_png}");
    println!("IGUALDAD\tentrada_paquete==MUESTRA_svg\t{eq_svg}");
    println!("DISTINTOS\tR01_png!=R06_png\t{ne_r06_png}");
    println!("DISTINTOS\tentrada_svg!=R06_svg\t{ne_r06_svg}");

    if !eq_png || !eq_svg {
        disc += 1;
    }
    if !ne_r06_png || !ne_r06_svg {
        disc += 1;
    }

    println!("RESUMEN\tvectores_nist=ok\tdiscrepancias_testigo={disc}");
    if disc != 0 {
        std::process::exit(1);
    }
}
