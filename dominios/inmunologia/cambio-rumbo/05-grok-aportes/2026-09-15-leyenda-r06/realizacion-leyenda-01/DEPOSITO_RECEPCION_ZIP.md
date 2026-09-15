# Depósito receptor del ZIP y continuidad

Fecha: 2026-09-15. Referencia de los fuentes de trabajo: `0e36549f4f6914b4fdb7dd36a1f5b4ba5b91c797`.

El [ZIP recibido](realizacion-leyenda-01-completo-2026-09-15.zip) queda depositado íntegro: 40.888 bytes; blob Git `40c5040d3932341a32804f2829848b75e4fbda22`; SHA-256 `e7d04f9afdd3da95cae921cf860d7902c2b9e016160c15aa190d51796325fb81`. Contiene 32 archivos y 6 entradas de directorio. El control CRC mediante unzip no encontró errores.

Los tres [originales históricos](evidencias/originales-ausentes/) coinciden con tamaños y SHA-256 del manifiesto de origen. Se depositan también las cuatro [variantes conservadas](evidencias/variantes/). No son reconstrucciones receptoras; proceden de los bytes del ZIP aportado.

Respecto del corte de referencia, 22 archivos del ZIP son idénticos, 3 difieren y 7 son adicionales. Las diferencias son:
- `PROTOCOLO_CUALIFICACION.md`: variante local de 4407 bytes frente a 4379 bytes del corte.
- `src/main.rs`: 2904 bytes frente a 2903; la variante del ZIP añade un LF final.
- `README.md`: 884 bytes frente a 852; el ZIP añade una referencia al índice.

Se conserva el ZIP original y sus variantes. Los fuentes de trabajo y el protocolo de aquel corte no se sobrescriben. Únicamente se actualiza este índice documental para enlazar la recepción.

## Inventario y evidencia

- [Manifiesto receptor corregido](MANIFIESTO_CORREGIDO.tsv): 33 objetos, correspondientes a los 25 archivos del corte de referencia, los 7 originales/variantes incorporados y el ZIP. Las filas del índice corresponden expresamente a su versión de aquel corte, anterior a la presente ampliación. No incluye su propia huella ni los documentos auxiliares creados en esta recepción; estos quedan identificados por el commit de depósito.
- [Fuente del cotejo Rust](evidencias/COTEJO_ZIP_RECEPCION.rs).
- [Salida completa](evidencias/COTEJO_ZIP_RECEPCION_SALIDA.txt).
- [Control CRC](evidencias/ZIP_CRC.txt).

Órdenes receptoras, Rust 1.98.0; compilación y cotejo con retorno cero:

```text
continuacion-auditoria/rust/bin/rustc --edition=2021 /tmp/sv_zip_recepcion/COTEJO_ZIP_RECEPCION.rs -o /tmp/sv_zip_recepcion/cotejo
/tmp/sv_zip_recepcion/cotejo upload/b3a1a4af-58f5-4e9b-8f17-40416ad877e2.zip /tmp/sv_zip_recepcion/realizacion-leyenda-01 /tmp/sv_leyenda_0e36549f
```

El primer argumento es el ZIP; el segundo, su directorio extraído; el tercero, los 25 archivos recuperados del corte de referencia. Se reutilizan las funciones históricas de identidad; no se declara validación criptográfica independiente.

## Punto de continuidad

La transferencia del código de trabajo y del respaldo histórico queda completada. La compilación limpia del reconocedor permanece pendiente: el intento receptor sobre `0e36549f` terminó al descargar `fdeflate 0.3.7`, con retorno 101 por transferencia de cero bytes en quince segundos. No acredita ni refuta la compilación del código.

El [registro receptor del intento](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/ef096c8f5f681926acbea17b6a7db619836bf3dc/docs/calidad/tuberias-ia/continuacion-15-09-2026/COMPILACION_RECEPTORA_0E36549F.txt) conserva el resultado. La entrada anterior del índice que menciona `evidencias/COMPILACION_LIMPIA.txt` describe una pieza pendiente y no un archivo depositado.

Siguiente acción: obtener las dependencias exactas de Cargo.lock y completar la compilación desde el corte remoto; después revisar las condiciones de §10.2 antes de cualificar. Q1/Q2 y E1–E16 no se ejecutaron. No se cambia el rumbo ni se abren otras sedes.
