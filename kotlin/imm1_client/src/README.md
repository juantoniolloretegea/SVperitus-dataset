# SVperitus — IMMUNO-1 Kotlin Client / src

Este directorio contiene el código fuente del cliente Kotlin de IMMUNO-1.

## Contenido actual

- `main/kotlin/Main.kt` — Bridge Kotlin/JS → Rust/WASM (Watson F.1–F.5)
- `main/resources/index.html` — Template HTML para build Gradle

## Función

`Main.kt` implementa el puente real entre el cliente Kotlin y el motor Rust/WASM:

1. Espera a que el motor WASM esté cargado (`engine-ready`)
2. Construye un caso fijo de demostración como JSON válido IMMUNO-1
3. Llama a `window.__wasm.evaluate_immuno1(json)` del motor Rust real
4. Parsea y muestra la respuesta: clase global, conteos, vector, JSON bruto
5. Expone `engine_info()` para verificación

## Principio de diseño

La lógica clínica **no** se implementa aquí.

`src/` no redefine:

- los parámetros P01–P25,
- la semántica 0/1/U,
- la regla T(25)=19,
- ni la clasificación global.

Todo eso pertenece al motor normativo ya existente (Python → Rust/WASM).

## Flujo lógico

```text
Main.kt (Kotlin/JS)
   ↓
Caso JSON de demostración
   ↓
window.__wasm.evaluate_immuno1(json)
   ↓
Resultado evaluado (JSON)
   ↓
Presentación visual en DOM
```
