# SVperitus — IMMUNO-1 Kotlin Client

> **Estado:** cliente inicial en preparación.
> Este subdirectorio queda reservado para la primera implementación Kotlin de IMMUNO-1 como **capa de interfaz**, consumiendo el motor Rust/WASM ya existente.

---

## Qué es

`imm1_client/` será el primer cliente Kotlin de SVperitus para IMMUNO-1.

Su objetivo es ofrecer una **interfaz de uso clara y estructurada** que permita:

- introducir un caso mediante formulario,
- transformarlo en un caso evaluable,
- enviarlo al motor normativo,
- recibir la salida evaluada,
- y mostrar el resultado de forma visual y auditable.

---

## Qué no es

Este cliente **no redefine** la lógica clínica de IMMUNO-1.

No es:

- una nueva fuente de verdad normativa,
- un tercer motor P01–P25,
- ni una implementación alternativa con criterio clínico propio.

La autoridad normativa sigue siendo:

1. Documento formal  
2. Motor Python  
3. Configuración YAML  
4. Parity tests  
5. Port Rust

Kotlin sólo **consume** el motor ya existente.

---

## Motor que consumirá

Este cliente está pensado para consumir, de forma preferente, el **motor Rust/WASM** ya disponible en el proyecto.

### Referencias directas

- **Demo Rust/WASM de IMMUNO-1**  
  https://juantoniolloretegea.github.io/SVperitus-dataset/rust/wasm-demo/

- **README de Rust**  
  ../../rust/README.md

- **README principal del repositorio**  
  ../../README.md

---

## Objetivo funcional mínimo

La primera versión de este cliente deberá permitir:

1. introducir valores mediante formulario,
2. construir el caso estructurado,
3. invocar el motor Rust/WASM,
4. recibir:
   - vector P01–P25,
   - conteos `n0 / n1 / nU`,
   - clase global `APTO / INDETERMINADO / NO_APTO`,
   - explicación del resultado,
5. representar el polígono polar.

---

## Arquitectura lógica prevista

```text
UI Kotlin
   ↓
Formulario IMMUNO-1
   ↓
Caso estructurado
   ↓
Motor Rust/WASM
   ↓
Resultado evaluado
   ↓
Salida visual + polígono
```

---

## Alcance inicial

La primera entrega de `imm1_client/` debe ser **mínima, clara y fiel**:

- cliente web,
- interfaz sencilla,
- sin duplicar lógica,
- sin tocar la semántica clínica,
- y alineado con la demo Rust/WASM ya existente.

---

## Próximo hito técnico

Tras este README, el siguiente paso será crear la estructura mínima del cliente, previsiblemente con:

```text
imm1_client/
├── README.md
├── src/
│   └── ...
└── build/   (generado)
```

y comenzar por una versión que reproduzca el flujo ya demostrado en la demo Rust/WASM:

- entrada,
- evaluación,
- salida,
- visualización.

---

## Regla de oro

> Kotlin organiza la experiencia de uso.
> Rust evalúa.
> Python sigue siendo la fuente canónica de verdad.
