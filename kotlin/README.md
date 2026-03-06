# SVperitus — Cliente Kotlin

> **Estado:** cliente Kotlin/JS inicial ya publicado en GitHub Pages.  
> Kotlin se mantiene como **capa cliente e integradora**, no como nueva fuente de verdad normativa.  
> Próximo paso: cerrar una comprobación visible y reproducible del ciclo **Kotlin → Rust/WASM** y evolucionar después hacia una interfaz propia más completa.

---

## Qué hay aquí

Este directorio corresponde a la **línea Kotlin de SVperitus**.

Su función no es redefinir la lógica clínica de IMMUNO-1 ni duplicar el motor normativo, sino proporcionar una **interfaz de uso** capaz de:

- recoger o preparar la entrada del usuario,
- estructurar el caso clínico,
- invocar el motor normativo ya existente,
- presentar el resultado de forma clara y auditable.

En la arquitectura actual del proyecto:

- **Python** sigue siendo la fuente canónica de verdad normativa,
- **Rust** actúa como port técnico del motor,
- **Kotlin** queda reservado para la experiencia cliente y la integración.

---

## Principio rector (NO negociable)

> Kotlin no redefine P01–P25.  
> Kotlin no introduce criterio clínico nuevo.  
> Kotlin consume el motor normativo ya existente y presenta su salida.

Si Kotlin discrepa de Python o Rust, Kotlin no corrige la lógica:
debe revisar la integración.

---

## Objetivo de esta línea Kotlin

La meta es construir un cliente web —y, más adelante, potencialmente móvil o de escritorio— que permita:

1. introducir o preparar un caso IMMUNO-1,
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

- **Cliente Kotlin publicado**  
  https://juantoniolloretegea.github.io/SVperitus-dataset/kotlin/imm1_client/

- **README de Rust**  
  ../rust/README.md

- **Repositorio principal**  
  ../README.md

---

## Alcance actual

En este momento, este directorio ya no está en fase meramente reservada.

La línea Kotlin dispone de:

- una primera estructura funcional,
- una ruta pública en GitHub Pages,
- compilación y despliegue mediante GitHub Actions,
- y una primera presencia visible como cliente.

Todavía **no constituye una integración cerrada y completa del ciclo Kotlin → Rust/WASM con formulario clínico propio**, pero ya no debe describirse como una vía únicamente prevista o vacía.

---

## Estado actual y siguiente hito

El siguiente hito ya no es “crear la estructura mínima”, sino **cerrar una comprobación explícita y visible del ciclo Kotlin → Rust/WASM**, de modo que el usuario pueda verificar que:

1. Kotlin recoge o prepara un caso,
2. Kotlin invoca el motor Rust/WASM real,
3. Rust devuelve la evaluación,
4. y Kotlin muestra exactamente esa respuesta.

Después de esa comprobación, el paso siguiente será evolucionar el cliente hacia una interfaz propia más completa, con formulario, salida estructurada y visualización integrada.

---

## Arquitectura prevista

```text
kotlin/
└── imm1_client/
    ├── README.md
    ├── src/
    │   └── ...
    └── build/   (generado)
```

### Arquitectura lógica

```text
Formulario o caso preparado en Kotlin
      ↓
Caso estructurado (JSON / modelo equivalente)
      ↓
Motor Rust/WASM
      ↓
Resultado evaluado
      ↓
Salida visual + polígono polar
```

---

## Qué no hará Kotlin

Kotlin no será:

- la fuente canónica de verdad,
- un tercer motor normativo,
- un lugar donde redefinir reglas clínicas,
- ni una validación médica del sistema.

Su papel es **cliente, integración y experiencia de uso**.

---

## Referencia cruzada

- Motor Python IMMUNO-1: `../IMMUNO-1/normative_engine.py`
- Configuración: `../IMMUNO-1/config/imm_n25.yaml`
- Línea Rust: `../rust/README.md`
- Documento 7: `../docs/Documento7_IMMUNO-1.md`
