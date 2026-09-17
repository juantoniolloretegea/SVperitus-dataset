# Nota de entrega · contrato candidato TLC-S32-02 v0.1

## Fuentes y cortes

Repositorio de consulta: `juantoniolloretegea/SV-lenguaje-de-computacion`. Corte de referencia y cabeza de `main` al preparar la entrega: `03578e3c3919d38ed1ae1dbc686d36ea9147c0b6`. Ambos coinciden; no hubo avance de `main` que debiera examinarse por separado.

Piezas rectoras leídas en ese corte: `AGENTS.md`; pilares de 05/09/2026; acta de perfiles, contratos y ensamblaje de 06/09/2026; acta de transición desde OP-IMM-001 de 03/09/2026, con adendas §§12–30. En `docs/calidad/tuberias-ia/`: obligación y recepción de Rust S29; estudio BIS-03; parte de privacidad y seguridad, apartados 11 y 11.7. Fuentes primarias de §11.1, leídas en `SVperitus-dataset@bbac1b44b1d3b845305e9cde492a08221206d631`: expediente predecisional v0.4 (C17 en §8), ampliación atómica v0.3 y acta de relevo con adenda §12. Contrato R2-0, blob `8faa1028e04a1e4fdd7d10bea63c74064abaccf3`. Interfaces de `sv_core` en `permission.rs`, `decision_trace.rs` y `admissibility.rs`.

La correspondencia de C17 incorporada en RETP-2026-249 se toma como antecedente. No se reabre ni se modifica.

En `SVperitus-dataset`, rama `dominio-inmunologia`, ya existían las carpetas `2026-09-17-contrato-s32-trayecto-local/` (TLC-S32-01 v0.1) y `2026-09-17-contrato-s32-trayecto-local-v0.2/` (TLC-S32-01 v0.2). Esta entrega usa la carpeta `2026-09-17-contrato-s32-trayecto-local-ligadura/` y no modifica esos bytes. La carpeta de ligadura conservaba ya la comprobación mínima de entorno; este depósito completa el paquete documental.

## Relación con S32

S32 permanece en ejecución. Esta entrega desarrolla el siguiente paso de §11.7: un contrato candidato del trayecto local común y sus casos previstos, con ligadura a componentes constituidos y a C17. No cierra S32 ni BIS-03. No ejecuta Q1/Q2 ni E1–E16. No asigna identificador RETP ni actualiza Sucesos, mapas, estados del flujo ni componentes constituidos.

Cubre de §11.7 el contrato y los casos del trayecto local. Deja pendientes la habilitación, los ensayos, las opciones condicionadas, el responsable efectivo, los plazos, C16 del uso seleccionado y las realizaciones E1, E3, E4 y la materialización de E2 como esquema de admisión ligado a EP07. El sello intra-proceso R1-4/R1-5 no cubre por sí solo el acto.

## Entorno y comprobaciones realizadas

Sistema: Debian GNU/Linux 12 (bookworm), `x86_64`. Herramientas: Git 2.39.5, curl 7.88.1, tar, xz, gcc 12.2.0, GNU ld 2.40. Lectura y depósito en GitHub comprobados mediante el conector; identidad autenticada coincidente con el titular de los repositorios.

Existía rustup 1.29.1 con la cadena `1.98.0-x86_64-unknown-linux-gnu` y un predeterminado 1.98.1. Se seleccionó de forma explícita 1.98.0:

```text
rustup run 1.98.0 rustc -Vv
rustup run 1.98.0 cargo -V
```

Resultado: rustc 1.98.0 (88d9e12ae 2026-08-18), commit `88d9e12ae178fab0fb5cc050a94da85685d449ea`, LLVM 22.1.8; cargo 1.98.0 (797e8a9bc 2026-08-05). SHA-256 del binario `rustc` de esa cadena: `3690cc576ede140504698405d5d8fa3826aaadbe71699c6c4ed0a565d6f493e2`.

Comprobación mínima en directorio temporal, biblioteca estándar únicamente, código de terminación 0, salida `ok-minimo`. Acredita el entorno de esta sesión. No acredita pruebas de privacidad del SV. No se instalaron bibliotecas por anticipación.

La lógica propia de cotejo está en `COTEJO_ENTREGA.rs`. Debe invocarse con `RUSTC` apuntando al compilador 1.98.0. Git, rustup, el conector GitHub y el enlazador del sistema se declaran como herramientas de coordinación, no como realización Rust del trayecto.

## Resultados

- Contrato candidato TLC-S32-02 v0.1, con etapas, interfaces ligadas a `sv_core` sin sobreafirmar su constitución, permisos, revocación, salida, persistencia y pendientes explícitos. Las etiquetas `I-*` son documentales; `QuerySpec` no es el servicio de E1.
- Diecinueve casos previstos, positivos y negativos, enlazados a P01–P04 y P06–P10, a C16, a `CaptureOutcome`/`AdmissibilityState` y a las relaciones DESIGNA/ACEPTA_ENCARGO, incluido permiso insuficiente o ausente. Todos en estado «no ejecutado: implementación pendiente».
- Cotejo documental del paquete ejecutado con Rust 1.98.0.

## Limitaciones

No existe implementación del servicio de consulta, de la ligadura con la fuente institucional de autoridad, del productor de la vista ni del almacén durable. Por ello no se han ejecutado los casos de privacidad. Host, bus y transporte siguen sin constituir. Los plazos de conservación no se han inventado. La EIPD y la base jurídica permanecen a cargo del responsable competente.

## Archivos entregados

Carpeta `dominios/inmunologia/cambio-rumbo/05-grok-aportes/2026-09-17-contrato-s32-trayecto-local-ligadura/`:

1. `CONTRATO_CANDIDATO_TLC_S32_02_v0.1.md`
2. `CASOS_PREVISTOS_TLC_S32_02_v0.1.md`
3. `NOTA_ENTREGA.md`
4. `COTEJO_ENTREGA.rs`
5. `COTEJO_ENTREGA_SALIDA.txt`
6. `ENTORNO_MINIMO.rs`
7. `ENTORNO_MINIMO_SALIDA.txt`
