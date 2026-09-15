# Subsanación de la entrega 02 · leyenda R06

**Sede:** `juantoniolloretegea/SVperitus-dataset`, rama `dominio-inmunologia`, directorio `dominios/inmunologia/cambio-rumbo/05-grok-aportes/2026-09-15-leyenda-r06/`.

**HEAD inicial de este encargo:** `ed6ade5e2285ecf3d058c20c9e074feb7a5066b6`. Coincide con el corte auditado. No había archivos `SUBSANACION_ENTREGA_02.md`, `CONTRATO_CANDIDATO_LEYENDA_CONTENIDO_2.md` ni `COTEJO_IDENTIDAD_REEJECUCION_02.txt`. Los cuatro archivos previos se han conservado.

**Estado:** depositado para auditoría. El contrato permanece candidato. No se declara resuelta la leyenda ni cerrado Bis o S26.

## Trazabilidad del cotejo auxiliar

No se conserva evidencia original que vincule el fuente compilado históricamente con el archivo depositado (ausencia del binario, del registro de compilación contemporáneo y de una huella del fuente tomada en aquel acto). El tamaño 9053 B no acredita esa vinculación.

Por ello se ejecutó una única repetición, identificada como ejecución nueva, documentada en `COTEJO_IDENTIDAD_REEJECUCION_02.txt`. El fuente compilado es el blob `67b8d61b7c3b8badeb38feef4345a21aa1347577` del corte `ed6ade5e…`. Cadena: rustc 1.98.0 `(88d9e12ae 2026-08-18)`, ruta `/opt/sv-rust-1.98.0/bin/rustc`. Entradas del laboratorio `86441ad4…` vía conector autenticado.

Resultado de la repetición: vectores NIST conformes; huellas de testigos iguales a las referencias ya comunicadas; R01 = muestra PNG; entrada = muestra SVG; R01 ≠ R06. Las huellas de R06 no están en `IDENTIDADES.txt`. Una huella SHA-256 del fuente calculada hoy (`6698383e…`) no se presenta como registro anterior.

## Tabla de reparos

| Reparo | Corrección | Archivo y apartado | Evidencia | Limitación pendiente |
|---|---|---|---|---|
| El tamaño no prueba que el `.rs` depositado sea el compilado históricamente | Declarar la falta de vínculo original y repetir el cotejo como ejecución nueva sobre el blob del corte | `COTEJO_IDENTIDAD_REEJECUCION_02.txt`; este informe, sección de trazabilidad | Blob Git coincidente; rustc 1.98.0; salida íntegra RC=0 | La ejecución histórica sigue sin registro original de compilación |
| Huellas de R06 ausentes en `IDENTIDADES.txt` | Conservar esa ausencia; no incorporarlas al manifiesto histórico | `COTEJO_IDENTIDAD_REEJECUCION_02.txt` | Texto de `IDENTIDADES.txt` y filas R06 del cotejo | El paquete histórico no documenta SHA-256 de R06 |
| La razón de intersección sobre tinta de plantilla ignora tinta no explicada | Medida de residuo R_abs, R_rel; reglas de atribución exclusiva, superposición y marcas ajenas | `CONTRATO_CANDIDATO_LEYENDA_CONTENIDO_2.md` §B | Solo especificación | Umbrales rho y r_max no cualificados; no hay implementación |
| Cualificación y evaluación mezcladas | Q1/Q2 solo cualifican; E1–E11 reservados, incluidos adversariales de residuo | Contrato v2 §D | Solo especificación | E1 carece aún de segundo testigo material |
| Solape entre `FALLO_LECTURA` y `FUERA_DE_PERFIL` | Cuota y E/S antes de la firma; perfil geométrico y de firma aparte; `FALLO_DECODIFICACION` para IDAT irrecuperable | Contrato v2 §A y §C | Solo especificación | Sin batería ejecutada sobre E9–E11 |
| Falta de determinismo (vertical, intervalos, empates, varias tuplas) | Filas 334–337; intervalos semiabiertos; regla de empate; orden lexicográfico a priori para una sola tupla | Contrato v2 §C | Solo especificación | Ninguna tupla está validada |
| Independencia afirmada por el nombre del crate | Inventario de fallos comunes (TTF, códec PNG); distinción identidad de bytes / contenido visible | Contrato v2 §E e introducción | Solo especificación | Independencia de códec no acreditada |

## Archivos añadidos en esta subsanación

- `SUBSANACION_ENTREGA_02.md` (este documento)
- `CONTRATO_CANDIDATO_LEYENDA_CONTENIDO_2.md`
- `COTEJO_IDENTIDAD_REEJECUCION_02.txt`

No se ha modificado el README ni los demás archivos del corte `ed6ade5e…`.

## Puntos no resueltos

- Cualificación de parámetros no ejecutada (prohibida en este encargo).
- Reconocedor no implementado.
- E1 sin segundo PNG independiente.
- Independencia respecto del decodificador PNG no demostrada.
- Pruebas A–L de la adenda de ciberseguridad no reejecutadas aquí.
- Bis, S26, GUI, Qwen y CYB no reabiertos.
