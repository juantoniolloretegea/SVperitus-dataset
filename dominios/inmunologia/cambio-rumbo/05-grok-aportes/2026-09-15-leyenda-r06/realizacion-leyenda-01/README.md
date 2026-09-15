# realizacion-leyenda-01

Prototipo experimental, separado del núcleo, del comprobador candidato LEYENDA-CONTENIDO/4.

**No cualifica el método. Compilar no es ejecutar Q1/Q2.**

## Contenido

- `src/` — lectura PNG, regiones, plantillas, residuo, reconocimiento, CLI.
- `PROTOCOLO_CUALIFICACION.md` — qué se ejecutará después y bajo qué cuotas.
- `DECISIONES_PENDIENTES.md` — ambigüedades no cerradas.
- `insumos/parametros.candidatos.txt` — retícula inicial, no validada.
- `evidencias/COMPILACION.txt` — rustc 1.98.0, comandos y códigos de retorno.

## Compilación

Rust 1.98.0. Dependencias: `png` 0.17 (decodificador) y `fontdue` 0.9 (glifos).

```
cargo build --locked --release
```

## Reconocimiento (no ejecutado aquí)

Requiere el TTF contratado y un PNG de 320×360. Los testigos R01/R06 permanecen en custodia privada.
