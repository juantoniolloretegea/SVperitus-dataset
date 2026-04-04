# SVperitus — IMMUNO-1 Kotlin Client

**Fecha y Versión: V.1 del conjunto**  
**Fecha:** 4 de abril de 2026  
**Versión del conjunto:** V.1 del conjunto  
**Autor del corpus:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Institución:** ITVIA — IA eñ™  
**ISSN:** 2695-6411  
**Licencia:** CC BY-NC-ND 4.0  
**Titularidad y autoría:** © Juan Antonio Lloret Egea, 2026. Este conjunto se distribuye con atribución explícita de autoría y bajo la licencia indicada, sin autorización para apropiación de la paternidad intelectual del Sistema Vectorial SV.  

---


> **Estado:** integración mínima real Kotlin → Rust/WASM implementada y publicada en GitHub Pages.

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

El cliente carga directamente el motor Rust/WASM disponible en `../demo_wasm/pkg/svperitus_wasm.js`.

### Referencias directas

- **Demo Rust/WASM de IMMUNO-1**  
  https://juantoniolloretegea.github.io/SVperitus-dataset/aplicaciones/demo_wasm/

- **Cliente Kotlin publicado**  
  https://juantoniolloretegea.github.io/SVperitus-dataset/aplicaciones/cliente_kotlin/

- **README de Rust**  
  ../../entornos/rust/README.md

- **README principal del repositorio**  
  ../../README.md

---

## Qué demuestra este cliente

- Carga el módulo WASM real, lo inicializa y lo expone en `window.__wasm`
- Main.kt espera a que el motor esté listo, habilita botones
- Construye un caso fijo de demostración como JSON válido IMMUNO-1
- Llama a `evaluate_immuno1(json)` del WASM real, parsea y muestra resultado
- Botones "Ejecutar caso demo" y "Mostrar engine_info()"
- No se usa iframe ni mock: la respuesta procede del motor Rust/WASM real

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
