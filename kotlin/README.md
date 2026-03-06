# SVperitus — Cliente Kotlin

> **Estado:** implementación inicial prevista.
> Kotlin se reserva como **capa cliente e integradora**, no como nueva fuente de verdad normativa.
> Próximo paso: construir un cliente web que consuma el motor Rust/WASM ya existente para IMMUNO-1.

---

## Qué hay aquí

Este directorio está destinado a la **línea Kotlin de SVperitus**.

Su función no es redefinir la lógica clínica de IMMUNO-1 ni duplicar el motor normativo, sino proporcionar una **interfaz de uso** capaz de:

- recoger la entrada del usuario,
- estructurar el caso clínico,
- invocar el motor normativo ya existente,
- presentar el resultado de forma clara y auditable.

En la arquitectura actual del proyecto:

- **Python** sigue siendo la fuente canónica de verdad normativa,
- **Rust** actúa como port técnico del motor,
- **Kotlin** queda reservado para la experiencia cliente y la integración futura.

---

## Principio rector (NO negociable)

> Kotlin no redefine P01–P25.
> Kotlin no introduce criterio clínico nuevo.
> Kotlin consume el motor normativo ya existente y presenta su salida.

Si Kotlin discrepa de Python o Rust, Kotlin no corrige la lógica:
debe revisar la integración.

---

## Objetivo de esta línea Kotlin

La meta es construir un **cliente web** —y, más adelante, potencialmente móvil o de escritorio— que permita:

1. introducir un caso IMMUNO-1 mediante formulario,
2. enviarlo al motor normativo,
3. recibir:
   - vector P01–P25,
   - conteos `n0 / n1 / nU`,
   - clase global `APTO / INDETERMINADO / NO_APTO`,
   - explicación del resultado,
   - y representación visual en polígono polar.

---

## Motor que consumirá Kotlin

La línea Kotlin está pensada para consumir, preferentemente, el **motor Rust/WASM** ya existente en el proyecto.

### Recursos ya disponibles

- **Demo Rust/WASM de IMMUNO-1**
  https://juantoniolloretegea.github.io/SVperitus-dataset/rust/wasm-demo/

- **README de Rust**
  ../rust/README.md

- **Repositorio principal**
  ../README.md

---

## Alcance actual

Por ahora, este directorio define la **ruta de integración Kotlin**, pero todavía no contiene una app funcional cerrada.

La implementación prevista será inicialmente:

- **cliente web Kotlin**
- conectado al motor Rust/WASM
- sin reimplementar la lógica normativa

---

## Arquitectura prevista

```text
kotlin/
└── imm1_client/
    ├── README.md
    ├── src/
    │   └── ...
    └── build/   (generado)

## Arquitectura lógica

Formulario Kotlin
      ↓
Caso estructurado (JSON / modelo equivalente)
      ↓
Motor Rust/WASM
      ↓
Resultado evaluado
      ↓
Salida visual + polígono polar
