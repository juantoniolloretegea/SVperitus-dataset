# SVperitus — IMMUNO-1 Kotlin Client / src

Este directorio queda reservado para el código fuente del primer cliente Kotlin de IMMUNO-1.

## Función prevista

Aquí vivirá la implementación de la interfaz Kotlin encargada de:

- recoger la entrada del usuario,
- estructurar el caso IMMUNO-1,
- invocar el motor Rust/WASM,
- recibir el resultado evaluado,
- y mostrar la salida de forma clara y visual.

## Principio de diseño

La lógica clínica no se implementa aquí.

`src/` no redefine:

- los parámetros P01–P25,
- la semántica 0/1/U,
- la regla T(25)=19,
- ni la clasificación global.

Todo eso pertenece al motor normativo ya existente.

## Papel de este código

El código de `src/` deberá encargarse de:

1. la interfaz,
2. la transformación de entrada,
3. la llamada al motor,
4. la recepción del resultado,
5. la representación visual.

## Flujo lógico

```text
Formulario
   ↓
Caso estructurado
   ↓
Motor Rust/WASM
   ↓
Resultado evaluado
   ↓
Presentación visual
```

## Estado actual

Por ahora, este directorio sólo fija la función de la futura implementación.
El siguiente paso será añadir el primer archivo real del cliente.
