# SVperitus — IMMUNO-1 Kotlin Client

> **Estado:** cliente Kotlin/JS inicial ya publicado en GitHub Pages.  
> Este subdirectorio contiene la primera implementación visible de IMMUNO-1 como **capa de interfaz**, organizada alrededor del motor Rust/WASM ya existente.

---

## Qué es

`imm1_client/` es el primer cliente Kotlin de SVperitus para IMMUNO-1.

Su objetivo es ofrecer una **interfaz de uso clara y estructurada** que permita:

- introducir o preparar un caso,
- transformarlo en un caso evaluable,
- invocar el motor normativo,
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

- **Cliente Kotlin publicado**  
  https://juantoniolloretegea.github.io/SVperitus-dataset/kotlin/imm1_client/

- **README de Rust**  
  ../../rust/README.md

- **README principal del repositorio**  
  ../../README.md

---

## Objetivo funcional mínimo

La versión funcional de este cliente debe permitir:

1. introducir o preparar valores de entrada,
2. construir el caso estructurado,
3. invocar el motor Rust/WASM,
4. recibir:
   - vector P01–P25,
   - conteos `n0 / n1 / nU`,
   - clase global `APTO / INDETERMINADO / NO_APTO`,
   - explicación del resultado,
5. representar o integrar el polígono polar.

---

## Arquitectura lógica prevista

```text
UI Kotlin
   ↓
Formulario o caso preparado
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

## Alcance actual

En este momento, `imm1_client/` ya dispone de:

- estructura mínima de proyecto Kotlin/JS,
- compilación y despliegue mediante GitHub Actions,
- ruta pública en GitHub Pages,
- y una primera verificación visible de que Kotlin está activo como cliente.

Todavía **no constituye una integración cerrada y completa del ciclo Kotlin → Rust/WASM con formulario clínico propio**, pero ya no está en fase meramente reservada o vacía.

---

## Estado actual y siguiente hito

El siguiente hito ya no es “crear la estructura mínima”, sino **cerrar una comprobación explícita y visible del ciclo Kotlin → Rust/WASM**, de modo que el usuario pueda verificar que:

1. Kotlin recoge o prepara un caso,
2. Kotlin invoca el motor Rust/WASM real,
3. Rust devuelve la evaluación,
4. y Kotlin muestra exactamente esa respuesta.

Después de esa comprobación, el paso siguiente será evolucionar el cliente hacia una interfaz propia más completa, con formulario, salida estructurada y visualización integrada.

---

## Estructura mínima actual

```text
imm1_client/
├── README.md
├── build.gradle.kts
├── settings.gradle.kts
├── gradle.properties
├── index.html
└── src/
    └── ...
```

---

## Regla de oro

> Kotlin organiza la experiencia de uso.  
> Rust evalúa.  
> Python sigue siendo la fuente canónica de verdad.
