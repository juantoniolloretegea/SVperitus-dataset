# Recepción de fdeflate y compilación del corte publicado

Fecha: 2026-09-15. **Compilación completada; retorno cero.** Corte compilado: `0e36549f4f6914b4fdb7dd36a1f5b4ba5b91c797`.

El [paquete fdeflate 0.3.7](evidencias/fdeflate-0.3.7.crate) aportado tiene 27.188 bytes, blob Git `439b2be226bbd38cd24f5f8199f7564ca97830e8` y SHA-256 `1e6853b52649d4ac5c0bd02320cddc5ba956bdb407c4b75a2c6b75bf51500f8c`. La huella calculada en Rust coincide con la de Cargo.lock del corte, antes de incorporarlo a la caché de Cargo.

La compilación se reanudó sobre los 25 archivos recuperados y cotejados del corte publicado, sin incorporar fuentes del ZIP ni modificar el código o Cargo.lock. Cargo descargó las restantes dependencias y finalizó `cargo build --locked --release` con retorno 0. Versión: rustc 1.98.0 (`88d9e12ae 2026-08-18`), cargo 1.98.0 (`797e8a9bc 2026-08-05`). La fase de compilación comunicó 16,55 segundos; esa cifra no representa el tiempo total de descarga y preparación.

Se volvió a cotejar la identidad de los 25 archivos del corte tras compilar: todos conservan tamaño y blob. Se generó el directorio de salida de Cargo; no se utilizó para modificar los insumos.

## Evidencias

- [Fuente Rust de admisión del paquete](evidencias/COTEJO_FDEFLATE.rs).
- [Huella observada y esperada](evidencias/COTEJO_FDEFLATE_SALIDA.txt).
- [Compilación limpia: versión, orden, salida y retorno](evidencias/COMPILACION_LIMPIA.txt).
- [Identidad posterior de los 25 archivos](evidencias/IDENTIDAD_TRAS_COMPILACION.txt).

Órdenes de admisión ejecutadas con retorno cero:

```text
continuacion-auditoria/rust/bin/rustc --edition=2021 /tmp/COTEJO_FDEFLATE.rs -o /tmp/cotejo_fdeflate
/tmp/cotejo_fdeflate upload/01b20454-b6ec-4c86-8cc5-8fb4e5222d59.crate /tmp/sv_leyenda_0e36549f/Cargo.lock
```

El paquete admitido se copió a la caché de Cargo con su nombre exacto. Para la compilación se seleccionó explícitamente el rustc anterior mediante RUSTC; CARGO_HTTP_TIMEOUT=15 y CARGO_NET_RETRY=0. Se utilizó la copia receptora en `/tmp/sv_leyenda_0e36549f`. El cotejo posterior reutiliza el [fuente receptor](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/ef096c8f5f681926acbea17b6a7db619836bf3dc/docs/calidad/tuberias-ia/continuacion-15-09-2026/COTEJO_RECEPCION_0E36549F.rs) y sus [entradas fijadas](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/ef096c8f5f681926acbea17b6a7db619836bf3dc/docs/calidad/tuberias-ia/continuacion-15-09-2026/ENTRADAS_RECEPCION_0E36549F.tsv).

Los intentos anteriores fallidos quedan conservados como antecedentes. El impedimento de descarga queda resuelto en esta ejecución, sin atribuir disponibilidad futura de la red.

**Siguiente paso:** revisión acotada de las condiciones de §10.2 del Acta 002 antes de la cualificación. La compilación no cualifica el reconocedor. Q1/Q2 y E1–E16 no se ejecutaron; no se ejecutó Python. No cambia el rumbo ni se cierra (p1+p3)-Bis.
