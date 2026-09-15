# Dependencias directas y transitivas

Declaradas en `Cargo.toml` y fijadas en `Cargo.lock`. Árbol observado en `evidencias/ARBOL_DEPENDENCIAS.txt`.

## Directas

| Crate | Función en este prototipo | Relación con el captor histórico |
|---|---|---|
| `png` 0.17.16 | Decodificar PNG acotado | Distinto de `tiny-skia` 0.12.0. Ambos leen PNG. No acredita independencia. |
| `fontdue` 0.9.4 | Rasterizar glifos del vocabulario | Distinto de resvg 0.48.1. Comparte el TTF contratado. |

## Transitivas observadas al compilar

Del decodificador: `bitflags`, `crc32fast`, `cfg-if`, `fdeflate`, `simd-adler32`, `flate2`, `miniz_oxide` 0.8.9 y 0.9.1, `adler2`.

Del rasterizador de glifos: `hashbrown`, `allocator-api2`, `equivalent`, `foldhash`, `ttf-parser`, `core_maths`, `libm`.

`flate2` aparece también en cotejos históricos de contenedores del Lenguaje. Esa coincidencia de nombre no se interpreta aquí como fallo común medido.

resvg 0.48.1 y tiny-skia 0.12.0 **no** son dependencias de este prototipo.
