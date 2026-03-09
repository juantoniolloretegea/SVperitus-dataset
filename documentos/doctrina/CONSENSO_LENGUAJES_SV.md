# CONSENSO SOBRE LENGUAJES DE PROGRAMACIÓN DEL SISTEMA VECTORIAL SV

**Autor:** Juan Antonio Lloret Egea · ORCID 0000-0002-6634-3351
**Fecha:** 09/03/2026
**Versión:** 1.1.0
**Estado:** Documento doctrinal estable
**Licencia:** CC BY-NC-ND 4.0
**ISSN:** 2695-6411

---

## 1. Principio rector

El Sistema Vectorial SV no dicta un lenguaje de programación. Dicta una disciplina formal que algunos lenguajes expresan mejor que otros.

Del marco se derivan **condiciones de legitimidad**, no una imposición de lenguaje concreto. La elección de lenguajes es pragmática, subordinada a esas condiciones y abierta a evolución futura. Ningún lenguaje puede proclamarse como constitutivo del sistema.

Este principio es coherente con el agnosticismo del backbone formulado en los *Fundamentos algebraico-semánticos del Sistema Vectorial SV* (§8.3) y con la subordinación de toda tecnología — incluida la inteligencia artificial — al marco formal, no a la inversa.

---

## 2. Dos planos de verdad

### 2.1. Verdad normativa doctrinal

Reside en el paper fundacional y en la especificación estable del marco. Dice **qué debe ocurrir**: qué es una célula, cómo se evalúa, qué operadores son lícitos, qué precondiciones deben cumplirse, qué invariantes son constitutivos.

Sin esta capa, el código podría convertirse en costumbre sin fundamento.

### 2.2. Verdad operativa ejecutable

Reside en la implementación de referencia y en la suite de conformidad cruzada. Garantiza **qué está ocurriendo** en el código: que la implementación se comporta de acuerdo con la especificación, que los ports producen los mismos resultados y que ningún lenguaje traiciona la semántica del marco.

Sin esta capa, el paper puede decir qué debe ocurrir, pero no garantiza por sí solo qué está ocurriendo.

### 2.3. El puente entre ambas

Los **tests de conformidad cruzada** actúan como puente de fidelidad entre la verdad normativa y la verdad operativa. Cualquier implementación en cualquier lenguaje se valida contra la misma batería de tests derivada de la especificación. Si pasa, es legítima. Si no pasa, no lo es — independientemente de la elegancia del lenguaje.

La fortaleza del sistema está en tener ambos planos, unidos por pruebas de conformidad.

---

## 3. Condiciones de legitimidad (C1–C8)

Un lenguaje es candidato legítimo para implementar el núcleo del Sistema Vectorial SV si satisface las siguientes condiciones necesarias. La elección final entre candidatos legítimos depende de criterios pragmáticos, de ecosistema y de dominio.

### C1 — Representación ternaria semántica

El lenguaje debe poder representar los tres estados {0, 1, U} como un tipo de dato con semántica propia. Lo ideal es un tipo algebraico enumerado (enum, sealed class, tipo de dato algebraico). Lo mínimo aceptable es una constante con nombre y una convención documentada.

### C2 — Funciones puras con aritmética entera exacta

El lenguaje debe permitir funciones sin estado mutable y con aritmética entera exacta.

### C3 — Capacidad de expresar precondiciones tipadas

El lenguaje debe permitir codificar las precondiciones de los operadores de composición de forma verificable (preferiblemente en tiempo de compilación, aceptablemente en tiempo de ejecución con tests).

### C4 — Capacidad de generar representación visible

El lenguaje (o su ecosistema) debe poder calcular y dibujar el polígono polar: aritmética de punto flotante y salida gráfica.

### C5 — Portabilidad a entornos de usuario final

El lenguaje (o su ecosistema) debe poder llegar al usuario final: web, escritorio, móvil o embebido, según el dominio.

### C6 — Agnosticismo: el lenguaje no es constitutivo

Ningún lenguaje puede proclamarse como «el lenguaje del Sistema Vectorial SV». Puede ser el lenguaje de una implementación de referencia, o el lenguaje de un dominio concreto, pero el marco trasciende a cualquier lenguaje particular.

### C7 — Auditabilidad semántica de U

El lenguaje y su ecosistema deben garantizar que el tercer estado (U) permanezca explícito, visible y no degradado a un entero disfrazado dentro del motor. No basta con que el tipo exista; la implementación no debe traicionar internamente la semántica epistémica de U.

### C8 — Conformidad cruzada

Cualquier lenguaje legítimo debe poder someterse a una batería común de tests de conformidad entre implementaciones, de forma que ningún lenguaje se juzgue solo por elegancia técnica, sino por su fidelidad al mismo comportamiento observable del Sistema Vectorial SV.

---

## 4. Arquitectura de capas

### Capa A — Núcleo formal

Implementa χ, Γ, los operadores de composición, las precondiciones.

Criterio principal: C1 + C2 + C3 + C7 + C8.

Un solo lenguaje como implementación de referencia. Los ports en otros lenguajes se validan contra la misma suite de conformidad.

### Capa B — Despliegue

Lleva el núcleo al usuario final (web, CLI, embebido, móvil).

Criterio principal: C4 + C5.

Puede ser el mismo lenguaje de Capa A (si compila a la plataforma objetivo) o diferente.

### Capa C — Aplicación de dominio

Integra el marco SV con el ecosistema específico del dominio.

Criterio principal: lo que el dominio exija. Cada dominio elige libremente.

---

## 5. Posición sobre los lenguajes actuales

### 5.1. Python

**Posición:** implementación de referencia legítima.

Python es adecuado por legibilidad, ecosistema, continuidad con el trabajo publicado y utilidad académica. Su sistema de tipos es débil para las precondiciones del álgebra, pero esa debilidad se compensa con la suite de conformidad (C8) y con disciplina de implementación. La verdad normativa reside en el paper, no en el código Python; Python la ejecuta, no la define.

### 5.2. Rust

**Posición:** mejor candidato técnico para el núcleo portable y verificable.

Su sistema de tipos (enums, traits, pattern matching exhaustivo) refleja naturalmente la estructura semántica del álgebra. Compila a WASM de forma madura. Es el candidato más fuerte para las capas A y B combinadas. Su debilidad es la curva de aprendizaje y la verbosidad.

### 5.3. Kotlin

**Posición:** lenguaje sin privilegio doctrinal, en observación.

No aporta función constitutiva al proyecto en su estado actual. No se expulsa del debate: queda como candidato pendiente de justificación por dominio real (cliente Android, capa JVM, interfaz local). Mientras tanto, no figura como pieza necesaria del núcleo.

### 5.4. JavaScript

**Posición:** necesario para interactividad web, no candidato a núcleo.

Ejecuta en todo navegador. Adecuado para lógica ligera. Sin sistema de tipos estático.

### 5.5. TypeScript

**Posición:** recomendación seria para la capa web.

Añade verificación de tipos sobre JavaScript sin coste de rendimiento. Permite reflejar las distinciones semánticas de la tupla (Ω, κ, ρ) en el código del cliente. No se eleva a doctrina universal, pero sí a recomendación fuerte para proyectos que aspiren a la auditabilidad que el marco exige.

### 5.6. Lenguajes futuros

**Posición:** la lista queda expresamente abierta.

Cualquier lenguaje que satisfaga C1–C8 es candidato legítimo. La elección depende del dominio. La incorporación de un lenguaje futuro no requiere revisión de este consenso, solo satisfacción de las condiciones y conformidad cruzada.

---

## 6. Posición sobre Γ

La función de criticidad Γ se implementa en la implementación de referencia (actualmente Python) y en JavaScript para el cliente web.

Su port a lenguaje compilado no se rige por una frontera fija del tamaño del espacio de indeterminación, sino por un criterio contextual que combina tres factores:

- **Carga real** del dominio de aplicación.
- **Exigencia de latencia** del entorno de despliegue.
- **Necesidad de ejecución fiable** en el contexto concreto (embebido, tiempo real, web pesada).

Cuando la combinación de estos factores lo justifique, Γ se porta a lenguaje compilado. Cuando no, permanece en la implementación de referencia y en JavaScript.

---

## 7. Convergencia notacional entre documentos

La versión 1.0.0 de este consenso identificaba cuatro puntos de divergencia notacional entre el texto fundacional y los documentos de implementación. Con la primera implementación del compositor, la meta-célula y la función Γ(v), la convergencia ha sido resuelta en los cuatro puntos.

### 7.1. Operador de serie: σ_{k,φ}

El paper fundacional (§7.8) define la composición en serie como σ_{k,φ}(Cⱼ, χᵢ(Cᵢ)), donde k es el parámetro puente y φ es el conector que traduce la salida de una célula al valor ternario del parámetro receptor.

**Resolución:** en la implementación, k = P25 (índice 24 del vector de IMMUNO-2) y φ es el mapa de traducción {APTO → 0, NO_APTO → 1, INDETERMINADO → U}. La función `compose()` en Python y `compose()` en Rust/WASM instancian σ_{k,φ} con estos valores concretos. El operador abstracto del paper y la función concreta del código son compatibles: el paper define la forma general, el código la instancia para un dominio.

### 7.2. Dominio de la función de evaluación χ

El paper fundacional (§7.3) define χᵢ : Cᵢ → Ωᵢ sin especificar Ωᵢ más allá de «codominio de salida de la célula».

**Resolución:** en la implementación, χᵢ se factoriza en dos pasos: `evaluate(case)` que produce el vector ternario, y `classify(vector)` que produce la clase global. El codominio Ωᵢ toma valores concretos según el dominio semántico de la célula: {APTO, NO_APTO, INDETERMINADO} para células clínicas, {NORMAL, INTRUSIÓN, INDETERMINADO} para la meta-célula de integridad. La factorización en dos pasos no contradice al paper — es una implementación legítima de la definición abstracta, coherente con la afirmación del §7.3 de que «χᵢ factoriza a través del vector interno y del motor normativo asociado».

### 7.3. Conteo de valores U: Nᵤ, nᵤ y m

El paper fundacional usa dos notaciones: Nᵤ (§5.1, mayúscula, coherente con N₀ y N₁) y nᵤ (§7.10, minúscula, al introducir Γ). Los documentos de implementación y la función `gamma.py` usan m(v).

**Resolución:** se adopta la siguiente convención. En textos formales y en el paper fundacional, Nᵤ o nᵤ son equivalentes y se refieren al número de componentes con valor U. En código y documentos de implementación, m es el símbolo preferido por brevedad y porque evita la ambigüedad del subíndice. La equivalencia es: Nᵤ(v) = nᵤ(v) = m(v) = número de valores U en v. Ninguna de las tres notaciones es incorrecta; m se prefiere en el plano operativo.

### 7.4. Rol estructural ρ y codificación visible ρ

El paper fundacional usa el símbolo ρ en dos sentidos: como codificación visible ρ : {0, 1, U} → {1, 2, 3} que asigna radios al polígono (§4.1), y como ρᵢ, el rol estructural de la célula en la tupla composable Cᵢ = (vᵢ, Ωᵢ, κᵢ, ρᵢ) (§7.2).

**Resolución:** se distinguen explícitamente. La codificación visible se implementa como RADIUS_MAP y no requiere más formalización: es un invariante constitutivo resuelto. El rol estructural ρᵢ toma valores concretos en la implementación del compositor: una célula puede ser «base» (IMMUNO-1, IMMUNO-2), «supervisora» (meta-célula, operador ▷) o «puente» (P25 como conector entre células). Estos valores no están formalizados como tipo enumerado en el código actual, pero están implícitos en la lógica del compositor y documentados en la arquitectura. La formalización explícita de ρᵢ como tipo queda abierta para cuando la composición multicelular lo exija.

---

## 8. Honestidad sobre el origen de las decisiones

Python, Rust y Kotlin no fueron decisiones derivadas del marco. Fueron decisiones pragmáticas de arranque: Python porque el autor lo domina y por su ecosistema científico; Rust porque compila a WASM y parecía sólido; Kotlin porque había un template disponible para un cliente web.

Declarar esto abiertamente es coherente con el espíritu del Sistema Vectorial SV. Si U existe para no fingir saber cuando no se sabe, la misma honestidad debe aplicarse a las decisiones de ingeniería. Lo que este consenso hace es transformar decisiones de oportunismo inicial en decisiones de arquitectura: ahora hay condiciones formales (C1–C8), capas diferenciadas (A/B/C), dos planos de verdad unidos por conformidad, y una posición documentada sobre cada lenguaje.

---

## 9. Síntesis

1. La verdad normativa doctrinal del Sistema Vectorial SV reside en el paper fundacional y en la especificación estable del marco.
2. La verdad operativa ejecutable reside en la implementación de referencia y en la suite de conformidad cruzada.
3. Ambas verdades se unen mediante tests de conformidad (C8).
4. Python es hoy la implementación de referencia por legibilidad y continuidad.
5. Rust es el mejor candidato técnico para el núcleo portable y verificable.
6. Kotlin queda sin privilegio doctrinal, en observación por dominio.
7. TypeScript es recomendación seria para la capa web.
8. La lista de lenguajes queda abierta, subordinada a C1–C8.
9. Γ se porta a compilado por criterio contextual (carga, latencia, despliegue), no por umbral fijo.
10. La convergencia notacional ha sido resuelta: σ_{k,φ} instanciado como compose(P25, φ), χᵢ factorizado como evaluate()+classify() con Ωᵢ concretos por dominio, m(v) adoptado como notación operativa de Nᵤ, y ρ diferenciado entre codificación visible (RADIUS_MAP) y rol estructural (base/supervisora/puente).
