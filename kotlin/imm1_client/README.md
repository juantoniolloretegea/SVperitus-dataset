# SVperitus — IMMUNO-1 Kotlin Client

> **Estado:** integración mínima real Kotlin → Rust/WASM implementada y publicada en GitHub Pages.  
> Cumple los criterios Watson F.1–F.5 y H.1–H.6.

---

## Qué es

`imm1_client/` es el cliente Kotlin de SVperitus para IMMUNO-1.

Demuestra **integración real** contra el motor Rust/WASM:

- carga el módulo WASM directamente (sin iframe),
- construye un caso IMMUNO-1 fijo de demostración,
- invoca `evaluate_immuno1()` del motor Rust real,
- muestra el resultado: clase global, conteos n0/n1/nU, vector P01–P25, JSON bruto,
- expone `engine_info()` para verificar que el motor responde.

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

## Motor que consume

El cliente carga directamente el motor Rust/WASM disponible en `../../rust/wasm-demo/pkg/svperitus_wasm.js`.

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

## Criterios Watson cumplidos

### Implementación (F.1–F.5)

- **F.1** Carga el módulo WASM real, inicializa, expone en `window.__wasm`
- **F.2** Main.kt espera `engine-ready`, lee `window.__wasm`, habilita botones
- **F.3** Caso fijo de demostración construido como JSON válido IMMUNO-1
- **F.4** Llama `evaluate_immuno1(json)` del WASM real, parsea y muestra resultado
- **F.5** Botones "Ejecutar caso demo" y "Mostrar engine_info()"

### Aceptación (H.1–H.6)

1. Cliente Kotlin carga y lo declara visualmente
2. Motor WASM real se inicializa desde página Kotlin
3. Kotlin llama realmente a `evaluate_immuno1()`
4. Respuesta visible procede del motor Rust/WASM real (no mock)
5. No se usa iframe como sustituto de integración
6. Documentación alineada con estado real

---

## Caso demo

El caso fijo de demostración es un paciente con:

- Buen recuento (ANC 2000, linfocitos 1200, IgG 800)
- Bazo y barreras intactos, remisión, sin quimio activa
- Vacunación parcial (gripe al día, COVID ausente, neumococo sin dato)
- Profilaxis mixta (PJP y antibacteriana adecuadas, antifúngica inadecuada)
- Resultado esperado: **INDETERMINADO** (conteos mixtos n0/n1/nU > 0)

Esto demuestra que la evaluación es real: un caso todo-0 o todo-1 sería trivial.

---

## Arquitectura lógica

```text
UI Kotlin
   ↓
Caso fijo de demostración (JSON)
   ↓
window.__wasm.evaluate_immuno1(json)
   ↓
Resultado JSON del motor Rust/WASM
   ↓
Presentación visual (clase, conteos, vector, JSON bruto)
```

---

## Siguiente hito

El siguiente paso es evolucionar el cliente hacia una **interfaz propia con formulario P01–P25**, de modo que el usuario pueda modificar los 25 parámetros y ver el resultado en tiempo real, incluyendo polígono polar.

---

## Estructura

```text
imm1_client/
├── README.md               ← Este archivo
├── build.gradle.kts        ← Kotlin/JS (IR)
├── settings.gradle.kts
├── gradle.properties
├── index.html              ← Página publicada con puente WASM real
└── src/
    ├── README.md
    └── main/
        ├── kotlin/Main.kt          ← Bridge Kotlin → WASM
        └── resources/index.html     ← Template para build Gradle
```

---

## Fórmula pública

**SÍ** se puede decir: "El cliente Kotlin inicial demuestra integración mínima real contra el motor Rust/WASM."

**NO** se puede decir: que el cliente está completo, que `imm1_normative` es operativo, ni que la arquitectura final está cerrada.

---

## Regla de oro

> Kotlin organiza la experiencia de uso.  
> Rust evalúa.  
> Python sigue siendo la fuente canónica de verdad.
