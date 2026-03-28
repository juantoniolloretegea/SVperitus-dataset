
# Célula especializada de seguridad estructural para la custodia del diseño, el DSL y los laboratorios del Sistema Vectorial SV

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Sello editorial:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)  
**Publicación:** IA eñ™ – La Biblia de la IA™  
**ISSN:** 2695-6411  
**Licencia:** CC BY-NC-ND 4.0  
**Lugar y fecha:** Madrid, 27 de marzo de 2026

***
## Resumen

Se formaliza una versión corregida de la célula especializada de seguridad estructural orientada a custodiar el propio diseño del Sistema Vectorial SV, su DSL, su laboratorio y su cadena visible de implementación. La propuesta no introduce semántica nueva ni desplaza la autoridad doctrinal del sistema. Se inscribe como piso subordinado a la doctrina suprema y se formula mediante una arquitectura compositiva de tres niveles: una célula de objetivos C_obj^9, una célula de base técnico-operativa C_base^9, una célula de custodia del diseño C_diseno^36 y dos compuertas conservadoras de resolución sobre el alfabeto ternario. La arquitectura integra, además, una carta geométrica auxiliar en ℝ³ para auditoría estructural no soberana, añade una tabla numerada completa de parámetros, incorpora pseudocódigo y laboratorio reproducible, presenta una correspondencia expositiva entre forma algebraica, tabla de resolución y diagrama funcional de compuerta SV, y eleva formalmente al carril doctrinal superior un conjunto de necesidades matemático-semánticas detectadas durante el trabajo pero no autorizadas todavía como matemática operativa local. La tesis central se conserva: la robustez del SV no debe confiarse a un backend ciego ni a una semántica implícita, sino a una arquitectura visible en la que el álgebra decide, la implementación obedece, la geometría audita y la indeterminación legítima se preserva.

**Palabras clave:** Sistema Vectorial SV; SVcustos; seguridad estructural; DSL; compuerta jerárquica; laboratorio reproducible; U; geometría auxiliar en ℝ³; objetivos de diseño.

***
## 1. Objeto

El objeto de este trabajo es formalizar una célula especializada capaz de custodiar el propio proceso de construcción del Sistema Vectorial SV. Dicha custodia no se limita al perímetro externo de intrusión. Debe alcanzar, con criterios materialmente observables, la fase de diseño, la fijación doctrinal, la transducción paramétrica, la coherencia repo–manuscrito–publicación, la compilación al DSL, el laboratorio de referencia y la trazabilidad de la resolución final.

El problema a resolver no es la seguridad informática en general. Es más preciso. Una arquitectura como el SV puede debilitarse de tres maneras distintas aunque su superficie externa parezca estable:

1. por apertura silenciosa de semántica no autorizada;
2. por separación entre doctrina, laboratorio y cadena de compilación;
3. por sustitución de la U legítima por una falsa certeza operacional.

La célula aquí formalizada nace para impedir esos tres modos de degradación.

***
## 2. Estatuto teórico

La célula especializada propuesta no constituye doctrina suprema ni revisión del álgebra madre. Su estatuto es subordinado. Opera dentro del Sistema Vectorial SV, no sobre él. Su misión es preservar el eje según el cual el humano diseña la interfaz, el álgebra fija el sustrato normativo y la implementación técnica obedece. No tiene legitimidad para introducir un cuarto polo semántico, ni para sustituir el horizonte de sucesos por tiempo desnudo, ni para degradar la indeterminación a mero déficit operativo.

En consecuencia, el presente trabajo adopta cuatro restricciones constitutivas:

- la terna canónica sigue siendo Σ = {0, 1, U};
- la ley estructural de célula sigue siendo n = b^2;
- toda composición debe declararse mediante relación semántica previa, codominio explícito y regla de resolución visible;
- la capa geométrica auxiliar en ℝ³ carece de soberanía semántica propia.

Estas restricciones no son accesorios formales. Son la condición de posibilidad para que un piso superior no destruya los cimientos inferiores.

***
## 3. Marco algebraico mínimo

Sea una célula SV una inscripción ternaria finita sobre una estructura de n posiciones con n = b^2, b ≥ 3. Cada posición toma valor en Σ = {0, 1, U}. En el dominio de este trabajo:

- **0** designa conformidad estructural, control suficiente o compatibilidad con el contrato visible;
- **1** designa violación estructural confirmada, compromiso o contradicción real con el contrato visible;
- **U** designa indeterminación honesta: ausencia de base suficiente para clausurar ni como 0 ni como 1.

Una célula especializada no modifica el sistema; lo instancia bajo un dominio tipado. Por ello, la custodia del diseño del SV debe formularse como arquitectura compositiva y no como desplazamiento doctrinal.

La forma general propuesta será:

```text
A_custodia = ⊗_{gate,T_cust}(C_diseno^36, S_suelo)
S_suelo    = ⊗_{gate,T_suelo}(C_obj^9, C_base^9)
```

con:

- `C_diseno^36`: célula de custodia del diseño, el DSL y el laboratorio;
- `C_obj^9`: célula de objetivos del frente en evaluación;
- `C_base^9`: célula de base técnico-operativa del soporte de trabajo;
- `S_suelo`: subsistema de suelo ya compuesto sobre objetivos y base;
- `⊗_{gate,T_*}`: compuerta jerárquica conservadora.

La arquitectura resultante no es una falsa SV(54) monolítica. Es una composición visible por pisos.

![Figura 1. Arquitectura de custodia por pisos](./figuras/figura_01_arquitectura_pisos.svg)

**Figura 1.** Arquitectura de custodia por pisos, con célula de objetivos, célula de base técnico-operativa, célula de custodia del diseño y compuertas conservadoras.

***
## 4. Principio de clasificación

Toda célula de codominio ternario fuerte se clasifica en K3 = {APTO, INDETERMINADO, NO_APTO}. Para una célula de tamaño n, se adopta el umbral clásico:

```text
T(n) = ⌊ 7n / 9 ⌋
```

De este modo:

- `T(9) = 7`
- `T(36) = 28`

La regla de clasificación de una célula C con valores vi ∈ {0, 1, U} es:

1. **NO_APTO** si `n1 ≥ T(n)`;
2. **APTO** si `n0 ≥ T(n)`;
3. **INDETERMINADO** en todo otro caso.

La arquitectura no admite que los valores U cuenten como 1, ni que la ausencia de observación se transforme en cierre favorable automático.

***
## 5. Compuertas de resolución

### 5.1. Compuerta del subsistema de suelo

La compuerta `T_suelo` resuelve la célula de objetivos y la célula de base técnico-operativa con política conservadora:

| C_obj \ C_base | APTO | INDETERMINADO | NO_APTO |
|---|---|---|---|
| **APTO** | APTO | INDETERMINADO | NO_APTO |
| **INDETERMINADO** | INDETERMINADO | INDETERMINADO | NO_APTO |
| **NO_APTO** | NO_APTO | NO_APTO | NO_APTO |

### 5.2. Compuerta final de custodia

La compuerta `T_cust` resuelve el resultado de la célula de diseño-laboratorio y el subsistema `S_suelo`:

| C_diseno \ S_suelo | APTO | INDETERMINADO | NO_APTO |
|---|---|---|---|
| **APTO** | APTO | INDETERMINADO | NO_APTO |
| **INDETERMINADO** | INDETERMINADO | INDETERMINADO | NO_APTO |
| **NO_APTO** | NO_APTO | NO_APTO | NO_APTO |

La simetría de ambas tablas no es un capricho visual. Expresa una misma disciplina: la custodia del diseño no puede declarar apto lo que el subsistema de suelo declara no apto, y el subsistema de suelo no puede blanquear un laboratorio o un DSL estructuralmente defectuosos.

***
## 6. Primer piso: célula de objetivos C_obj^9

La célula de objetivos sustituye en esta versión a la antigua lectura de perímetro externo. No evalúa tráfico ni sensores del mundo exterior. Evalúa si el frente en curso nace con suelo de necesidad, definición, verificación y disciplina bastante para entrar legítimamente en el carril SV. Sus nueve posiciones son:

- **O1. Línea clara de necesidad**: existe una necesidad explícita del frente y no una intuición vaga.
- **O2. Anclaje algebraico o matemático en SV**: el objetivo se apoya en base estructural ya contemplada por el SV.
- **O3. Alcance y fase declarados**: se declara si es continuidad de fase, nueva fase o bloque delimitado.
- **O4. Elementos constitutivos definidos desde el inicio**: los componentes mínimos están identificados.
- **O5. Estado del arte realizado**: consta revisión suficiente del frente correspondiente.
- **O6. Revisión del corpus SV aplicable**: se ha leído el suelo doctrinal y técnico pertinente del propio sistema.
- **O7. Base teórica suficiente**: existe soporte conceptual bastante para no operar por mera ocurrencia.
- **O8. Laboratorios y verificaciones definidos**: el frente nace con contraste material previsto.
- **O9. Integración con calidad y diseño reconocidos**: el objetivo ya queda enlazado con trazabilidad, calidad y criterios de diseño admitidos.

Su interés en esta arquitectura no es agotar el dominio del diseño, sino impedir que una pieza entre en el carril como si ya tuviera legitimidad constitutiva cuando aún no la ha fijado.

***
## 7. Segundo piso: célula de base técnico-operativa C_base^9

La célula de base técnico-operativa ya no describe una plataforma móvil concreta. Describe el suelo efectivo desde el que se observa, redacta, contrasta, ejecuta y preserva una pieza del ecosistema SV. No describe comportamiento funcional del dominio final; describe legitimidad y trazabilidad del soporte de trabajo.

### 7.1. Posiciones

- **Q1. Soporte de trabajo declarado**: repositorio, entorno, pieza y alcance objeto de custodia están identificados.
- **Q2. Repositorio fresco e identificado**: la fuente material usada es la vigente y verificable.
- **Q3. Árbol material completo y legible**: la estructura de archivos o artefactos es accesible y no fragmentaria.
- **Q4. Herramientas de edición y ejecución declaradas**: scripts, intérpretes, validadores, viewers o utilidades empleadas están identificados.
- **Q5. Dependencias externas declaradas**: servicios, conectores, permisos o software auxiliar visibles y delimitados.
- **Q6. Control de versiones y estado operativo visibles**: rama, release, borrador o copia material declarados con veracidad.
- **Q7. Separación efectiva entre laboratorio y backend**: no se endurece el backend por arrastre del laboratorio ni por entusiasmo semántico.
- **Q8. Evidencias de prueba y captura conservadas**: salidas, capturas, logs, PDF o equivalentes localizables.
- **Q9. Artefactos internos de diseño identificados**: no quedan restos decisivos opacos sin absorber, o bien quedan nombrados como tales.

### 7.2. Alcance de base y acceso real

En su versión corregida, `C_base^9` describe condiciones de base del trabajo material sobre documentos, repositorios, laboratorios, exportaciones, capturas y soportes de ejecución. La extensión a otros entornos exige traducir explícitamente cada posición Q1–Q9 a un canal funcional equivalente del soporte destino; en ausencia de tal traducción, la posición se conserva en U o en 0 por no aplicación, según corresponda.

Cada posición de `C_base^9` debe satisfacerse por uno de estos canales de observación:

- árbol real de archivos o repositorio fresco;
- manifiesto de dependencias, herramienta o servicio;
- captura material, PDF, render o log;
- ejecución local o trazabilidad equivalente.

Si el soporte no expone un canal legítimo de observación, la posición toma valor **U**. Si la posición no aplica por inexistencia estructural del subsistema, toma valor **0** por no aplicación. En ningún caso se simula observación.

***
## 8. Tercer piso: célula de custodia del diseño y del laboratorio C_diseno^36

La célula de custodia del diseño y del laboratorio constituye el núcleo nuevo del presente trabajo. Su función es vigilar si una pieza del ecosistema SV —documento, laboratorio, módulo de lenguaje, ejemplo, consulta, especificación o publicación— permanece dentro del carril visible y autorizado.

Se distribuye en seis capas de seis posiciones.

### 8.1. Capa A — anclaje doctrinal

- **A1. Filiación doctrinal explícita**: la pieza declara su dependencia del tronco doctrinal correcto.
- **A2. Límite superior explícito**: el límite superior humano y de no desviación está enunciado.
- **A3. Alfabeto correcto**: el artefacto no introduce valores extra-semánticos ni degrada la U.
- **A4. Horizonte de sucesos declarado**: cuando la pieza trata reevaluación, especifica el horizonte legítimo conforme al corpus canónico de la familia VII, en particular VII.3 sobre horizonte de sucesos y reevaluación discreta.
- **A5. Estatuto textual correcto**: distingue fundamento, pieza operativa, laboratorio o nota, sin usurpaciones.
- **A6. Bibliografía troncal suficiente**: la pieza cita el suelo doctrinal que usa efectivamente.

**Canales de acceso:** lectura del manuscrito, README, front matter, índice, bibliografía, notas doctrinales.

### 8.2. Capa B — captura y transducción

- **B1. Fuente material identificada**: cada observable decisivo tiene fuente nombrada.
- **B2. Vía de acceso declarada**: API, fichero, prueba, consulta, render o artefacto concreto.
- **B3. Criterio ternario explícito**: las condiciones de 0, 1 y U están escritas.
- **B4. No-aplica separado de U**: la pieza distingue imposibilidad estructural de incertidumbre legítima.
- **B5. Umbral o tabla visible**: no hay reglas de resolución ocultas.
- **B6. Repetibilidad local**: la observación puede repetirse en el mismo entorno o en entorno equivalente.

**Canales de acceso:** código, pseudocódigo, tablas, scripts, capturas, archivo de pruebas, especificación del parámetro.

### 8.3. Capa C — contrato del DSL y de compilación

- **C1. Traducibilidad a SVP**: el artefacto cabe en el carril del lenguaje sin inventar un metalenguaje oculto.
- **C2. Tipado visible**: codominio, semántica de salida y objetos estructurales están declarados.
- **C3. Composición explícita**: las relaciones entre células, dominios, agentes y consultas aparecen nombradas.
- **C4. Totalidad de tabla**: toda compuerta relevante está definida en todos los casos necesarios.
- **C5. Sin atajo opaco**: no existe comportamiento decisivo fuera del texto, la tabla y el laboratorio.
- **C6. Validabilidad previa a ejecución**: el artefacto puede ser rechazado antes de correr si rompe la gramática o la bienformación.

**Canales de acceso:** fuente `.svp`, IR, parser, validator, lowering, tablas de codominio, suite de conformidad.

### 8.4. Capa D — concordancia documental y registral

- **D1. Paridad repo–manuscrito**: lo afirmado por el manuscrito existe en el árbol material.
- **D2. Índices y README coherentes**: la sede pública no miente por omisión o desactualización.
- **D3. Referencias de figuras y laboratorios válidas**: no hay rutas rotas ni recursos fantasma.
- **D4. Autoría y metadatos completos**: autor, ORCID, ISSN, licencia, versión, fecha y lugar están explícitos.
- **D5. Estado declarado veraz**: borrador, laboratorio, publicación o réplica se nombran con precisión.
- **D6. Registro de trazabilidad suficiente y sin artefactos internos de diseño no absorbidos**: la pieza puede situarse en el ecosistema sin residuos decisivos opacos.

**Canales de acceso:** árbol de repositorio, manifiesto de archivos, render, revisión de enlaces, registros públicos.

### 8.5. Capa E — laboratorio y verificación

- **E1. Implementación de referencia existente**: Python o equivalente visible y ejecutable.
- **E2. Ejemplos canónicos completos**: al menos un caso apto, uno no apto y uno indeterminado.
- **E3. Casos adversariales**: el laboratorio no sólo confirma; también intenta romper la pieza.
- **E4. Salida trazable**: el laboratorio devuelve clases, recuentos, razones y no sólo una etiqueta final.
- **E5. QA de presentación**: tablas, figuras y resultados pueden revisarse sin ambigüedad material.
- **E6. Persistencia de U**: el laboratorio conserva explícitamente la U cuando no hay base de cierre.

**Canales de acceso:** scripts, notebook, CLI, resultados serializados, render, inspección estructural de salida.

### 8.6. Capa F — realidad de despliegue y límites

- **F1. Dependencias externas declaradas**: MDM, entitlements, companion, privilegios, sandbox u otras condiciones de despliegue.
- **F2. Frontera jurídica y de uso**: la pieza delimita su contexto legítimo de despliegue.
- **F3. No promesa de cobertura total**: no se vende como producto absoluto ni como backend ya cerrado.
- **F4. Compatibilidad de soporte**: se explicitan familias, plataformas o contextos donde aplica.
- **F5. Capa geométrica subordinada**: la R³ se usa como auditoría, no como soberana semántica.
- **F6. Salida para terceros**: el artefacto puede ser leído y evaluado por especialistas sin recurrir a claves internas.

**Canales de acceso:** secciones de aplicabilidad, notas de despliegue, laboratorio, manuscrito final, especificación de alcance.

![Figura 2. Célula de custodia del diseño por capas](./figuras/figura_02_celula_diseno_capas.svg)

**Figura 2.** Célula de custodia del diseño C_diseno^36, organizada en seis capas y treinta y seis posiciones verificables.

***
## 9. Semántica de la célula de custodia del diseño

En C_diseno^36:

- **0** significa que la posición concreta satisface el contrato visible del SV;
- **1** significa que la posición concreta incurre en infracción estructural, contradicción o ausencia de suelo indispensable;
- **U** significa que no existe base suficiente para concluir, bien porque el artefacto no expone aún la prueba, bien porque la observación depende de soporte externo no disponible.

Esta semántica convierte la custodia en un dominio paramétrico real, no en una auditoría literaria difusa. Cada una de las treinta y seis posiciones es verificable por documento, repo, script, parser, render o salida de laboratorio.

***
## 10. Carta geométrica auxiliar en ℝ³

Sobre cada célula y sobre cada resultado compuesto puede aplicarse una carta auxiliar en ℝ³. Su uso en este trabajo es estrictamente subordinado. No decide clase. Audita forma.

La elevación del polígono cumple cuatro funciones:

1. separar geométricamente las posiciones U del plano de determinación estricta;
2. detectar asimetrías, concentraciones sectoriales y colapsos por capas;
3. reforzar la adversarial sobre secuencias de laboratorio y respuestas de compuerta;
4. documentar patrones estructurales persistentes que en R² quedan visualmente comprimidos.

Las salidas mínimas exigibles de esta capa son:

- centroide;
- masa relativa de U;
- dispersión angular por capas;
- irregularidad de borde;
- y variación entre estados sucesivos cuando el horizonte de sucesos así lo exija.

El resultado geométrico puede tensar una lectura, nunca sustituirla.

***
## 11. Cánones de protección del DSL del SV

La célula de custodia del diseño no surge en vacío. Debe aprender de la historia seria de los lenguajes, compiladores, métodos formales y verificadores, sin copiar semánticas ajenas. De ese estado del arte se extraen doce cánones.

### Canon 1 — especificación soberana

La semántica del SV debe prevalecer sobre cualquier compilador o backend. El compilador no crea la verdad del lenguaje; la implementa.

### Canon 2 — verificación previa a ejecución

Ningún artefacto debe ejecutarse sin pasar antes por verificación de estructura, codominio, compuertas y dependencias visibles.

### Canon 3 — zonas de escape visibles

Si existiera algún mecanismo excepcional de apertura, éste debería quedar sintácticamente señalado y auditado. No caben atajos implícitos equivalentes a un `unsafe` silencioso.

### Canon 4 — perfiles normativos

El DSL debe poder ofrecer perfiles de uso restringidos según criticidad: laboratorio, pieza doctrinal, despliegue restringido, seguridad o equivalentes.

### Canon 5 — preservación semántica como horizonte

Cada lowering relevante del lenguaje debe aspirar a preservar las propiedades ya fijadas arriba. Mientras la prueba formal completa no exista, debe haber al menos trazabilidad y prueba diferencial.

### Canon 6 — IR estratificado

La estructura del lenguaje debe mantener una separación no reversible entre especificación, evaluación, consulta y ejecución. La mezcla de planos es vulnerabilidad semántica.

### Canon 7 — parser y serialización no ambiguos

Toda entrada y toda salida del lenguaje deben evitar representaciones maleables. Un artefacto semánticamente igual no debe poder esconderse en múltiples formas opacas no equivalentes a efectos de auditoría.

### Canon 8 — verificador con corpus propio

Todo cambio del validator, de las tablas o del lowering debe venir acompañado de casos de prueba nuevos y específicos.

### Canon 9 — laboratorio encapsulado

Los laboratorios deben ejecutarse con capacidades mínimas y con dependencia explícita del soporte. El laboratorio no puede convertirse en backend clandestino.

### Canon 10 — trazabilidad de la U

La U es un invariante lingüístico. El lenguaje debe impedir que la indeterminación se degrade a favor o en contra sin regla escrita previa.

### Canon 11 — reevaluación por suceso

La reevaluación del sistema debe venir dada por sucesos declarados, no por duración vaga o paso de tiempo sin estructura, de acuerdo con el aparato canónico de la familia VII y, en particular, con VII.3 sobre horizonte de sucesos y reevaluación discreta.

### Canon 12 — lectura para terceros

Toda pieza significativa del lenguaje y del laboratorio debe ser legible por terceros especialistas sin acceso a rituales internos, ni a memoria conversacional, ni a la intención subjetiva del implementador.

![Figura 3. Compuertas conservadoras y cánones del DSL](./figuras/figura_03_compuertas_canonos.svg)

**Figura 3.** Compuertas conservadoras de seguridad y custodia, junto con los doce cánones de protección del DSL.

***
## 12. Laboratorio mínimo reproducible

Los artefactos de esta sección se alojan, en la estructura de este paquete y del repositorio, en las rutas relativas `./laboratorio/celula_custodia_sv_release2.py` y `./laboratorio/testigo_minimo_custodia_sv_release2.svp`. Las figuras del manuscrito se alojan en `./figuras/`.

El laboratorio mínimo debe demostrar cuatro hechos:

1. que la arquitectura compuesta es operable sin semántica oculta;
2. que la compuerta conserva la U y no fabrica cierre;
3. que la custodia del diseño puede evaluarse como dominio paramétrico real;
4. que la salida devuelve clase, recuentos y umbrales con trazabilidad suficiente.


### 12.1. Pseudocódigo de referencia legible para terceros

El pseudocódigo de esta sección no sustituye a la implementación de referencia. Su función es permitir lectura estructural por terceros sin exigir conocimiento previo de Python.

```text
ORDER = { APTO < INDETERMINADO < NO_APTO }

funcion threshold(n):
    devolver ⌊ 7n / 9 ⌋

funcion classify_cell(vector):
    contar n0, n1, nU
    t = threshold(longitud(vector))
    si n1 ≥ t: devolver NO_APTO
    si n0 ≥ t: devolver APTO
    devolver INDETERMINADO

funcion gate(left, right):
    si left == NO_APTO o right == NO_APTO: devolver NO_APTO
    si left == INDETERMINADO o right == INDETERMINADO: devolver INDETERMINADO
    devolver APTO

funcion evaluate_architecture(obj9, base9, dis36):
    cls_obj = classify_cell(obj9)
    cls_base = classify_cell(base9)
    s_suelo = gate(cls_obj, cls_base)
    cls_dis = classify_cell(dis36)
    a_custodia = gate(cls_dis, s_suelo)
    devolver clases, recuentos, umbrales y salidas de compuerta
```

### 12.2. Implementación de referencia en Python

```python
from __future__ import annotations

import json
from typing import Iterable

ORDER = {"APTO": 0, "INDETERMINADO": 1, "NO_APTO": 2}


def threshold(n: int) -> int:
    return (7 * n) // 9


def summarize_cell(values: Iterable[object]) -> dict[str, int | str]:
    values = list(values)
    n = len(values)
    n1 = sum(v == 1 for v in values)
    n0 = sum(v == 0 for v in values)
    nU = n - n0 - n1
    t = threshold(n)
    if n1 >= t:
        cls = "NO_APTO"
    elif n0 >= t:
        cls = "APTO"
    else:
        cls = "INDETERMINADO"
    return {
        "n": n,
        "n0": n0,
        "n1": n1,
        "nU": nU,
        "threshold": t,
        "class": cls,
    }


def gate(left: str, right: str) -> str:
    table = {
        ("APTO", "APTO"): "APTO",
        ("APTO", "INDETERMINADO"): "INDETERMINADO",
        ("APTO", "NO_APTO"): "NO_APTO",
        ("INDETERMINADO", "APTO"): "INDETERMINADO",
        ("INDETERMINADO", "INDETERMINADO"): "INDETERMINADO",
        ("INDETERMINADO", "NO_APTO"): "NO_APTO",
        ("NO_APTO", "APTO"): "NO_APTO",
        ("NO_APTO", "INDETERMINADO"): "NO_APTO",
        ("NO_APTO", "NO_APTO"): "NO_APTO",
    }
    return table[(left, right)]


def evaluate_architecture(obj9, base9, dis36) -> dict[str, object]:
    c_obj = summarize_cell(obj9)
    c_base = summarize_cell(base9)
    s_suelo = gate(c_obj["class"], c_base["class"])
    c_dis = summarize_cell(dis36)
    a_custodia = gate(c_dis["class"], s_suelo)
    return {
        "C_obj": c_obj,
        "C_base": c_base,
        "S_suelo": s_suelo,
        "C_diseno": c_dis,
        "A_custodia": a_custodia,
    }


def run_cases() -> dict[str, dict[str, object]]:
    caso_1 = evaluate_architecture(
        obj9=[0] * 9,
        base9=[0] * 9,
        dis36=[0] * 36,
    )
    assert caso_1["A_custodia"] == "APTO"

    caso_2 = evaluate_architecture(
        obj9=[0] * 9,
        base9=[1] * 9,
        dis36=[0] * 36,
    )
    assert caso_2["A_custodia"] == "NO_APTO"

    caso_3 = evaluate_architecture(
        obj9=[0] * 9,
        base9=[0] * 9,
        dis36=[0] * 20 + [1] * 8 + ["U"] * 8,
    )
    assert caso_3["A_custodia"] == "INDETERMINADO"

    caso_4 = evaluate_architecture(
        obj9=[0] * 6 + ["U"] * 3,
        base9=[0] * 9,
        dis36=[0] * 36,
    )
    assert caso_4["A_custodia"] == "INDETERMINADO"

    return {
        "caso_1_custodia_apta": caso_1,
        "caso_2_base_no_apta": caso_2,
        "caso_3_diseno_indeterminado": caso_3,
        "caso_4_objetivos_indeterminados": caso_4,
    }


if __name__ == "__main__":
    print(json.dumps(run_cases(), ensure_ascii=False, indent=2))
```

### 12.3. Esqueleto mínimo en SVP

```svp
codomain K3 = { APTO, NO_APTO, INDETERMINADO };

output_semantics SemK3 {
  APTO -> "Clasificación fuerte favorable";
  NO_APTO -> "Clasificación fuerte desfavorable";
  INDETERMINADO -> "Sin clasificación fuerte";
}

cellspec C_OBJ {
  b: 3;
  codomain: K3;
  semantics: SemK3;
  role: Base;
}

cellspec C_BASE {
  b: 3;
  codomain: K3;
  semantics: SemK3;
  role: Base;
}

cellspec C_DIS {
  b: 6;
  codomain: K3;
  semantics: SemK3;
  role: Base;
}

cellstate S_OBJ {
  spec: C_OBJ;
  vector: [Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero];
}

cellstate S_BASE {
  spec: C_BASE;
  vector: [Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero];
}

cellstate S_DIS {
  spec: C_DIS;
  vector: [Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero,
           Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero,
           Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero, Zero];
}

admissibility_table TSUELO {
  input_codomains: [K3, K3];
  output_codomain: K3;
  table: {
    (APTO, APTO) -> APTO;
    (APTO, NO_APTO) -> NO_APTO;
    (APTO, INDETERMINADO) -> INDETERMINADO;
    (NO_APTO, APTO) -> NO_APTO;
    (NO_APTO, NO_APTO) -> NO_APTO;
    (NO_APTO, INDETERMINADO) -> NO_APTO;
    (INDETERMINADO, APTO) -> INDETERMINADO;
    (INDETERMINADO, NO_APTO) -> NO_APTO;
    (INDETERMINADO, INDETERMINADO) -> INDETERMINADO;
  }
}

admissibility_table TCUST {
  input_codomains: [K3, K3];
  output_codomain: K3;
  table: {
    (APTO, APTO) -> APTO;
    (APTO, NO_APTO) -> NO_APTO;
    (APTO, INDETERMINADO) -> INDETERMINADO;
    (NO_APTO, APTO) -> NO_APTO;
    (NO_APTO, NO_APTO) -> NO_APTO;
    (NO_APTO, INDETERMINADO) -> NO_APTO;
    (INDETERMINADO, APTO) -> INDETERMINADO;
    (INDETERMINADO, NO_APTO) -> NO_APTO;
    (INDETERMINADO, INDETERMINADO) -> INDETERMINADO;
  }
}

semantic_relation R_DECL {
  kind: DeclaredRelation;
}

graph G_CUST {
  nodes: [C_OBJ, C_BASE, C_DIS];
  edges: [];
  relation: R_DECL;
  regime: Simple;
}

let E_OBJ = evaluate(S_OBJ);
let E_BASE = evaluate(S_BASE);
let G_SUELO = gate([E_OBJ, E_BASE], using: TSUELO);
let E_DIS = evaluate(S_DIS);
let G_FINAL = gate([E_DIS, G_SUELO], using: TCUST);
```


### 12.4. Rutas canónicas del bloque reproducible en GitHub

A efectos de réplica canónica del bloque reproducible en GitHub, este manuscrito debe convivir con dos carpetas hermanas, `./figuras/` y `./laboratorio/`, preservando su vecindad relativa. Esta mención se incorpora aquí con finalidad documental y de verificabilidad pública: no modifica el régimen de importación operativo de plataformas editoriales, pero sí fija la organización canónica del paquete técnico asociado.

Las rutas relativas de referencia del bloque son las siguientes:

**Figuras**

```text
./figuras/figura_01_arquitectura_pisos.svg
./figuras/figura_02_celula_diseno_capas.svg
./figuras/figura_03_compuertas_canonos.svg
./figuras/figura_04_flujo_iso5807_custodia.svg
./figuras/figura_05_actividad_uml_custodia.svg
./figuras/figura_06_diagrama_funcional_compuertas_conservadoras.svg
./figuras/figura_07_celulas_poligonales_objetivos_base_custodia.svg
./figuras/figura_08_correspondencia_compuerta_sv.svg
```

**Laboratorio**

```text
./laboratorio/celula_custodia_sv_release2.py
./laboratorio/testigo_minimo_custodia_sv_release2.svp
./laboratorio/salida_casos_canonicos_release2.json
./laboratorio/pseudocodigo_custodia_release2.txt
./laboratorio/checklist_sprint_release2.md
```

En consecuencia, la réplica canónica del bloque no debe leerse como un conjunto plano de archivos, sino como una unidad documental y técnica organizada por rutas relativas estables entre manuscrito, figuras y laboratorio.

## 13. Casos canónicos

### Caso 1 — custodia apta

- `C_obj^9 = APTO`
- `C_base^9 = APTO`
- `C_diseno^36 = APTO`

Entonces:

```text
S_suelo = APTO      A_custodia = APTO
```

Interpretación: la pieza está anclada doctrinalmente, sus parámetros son reales, su compuerta es total, el laboratorio reproduce, la salida es legible y no existe fractura registral o de compilación relevante.

### Caso 2 — objetivos aptos, base no apta

- `C_obj^9 = APTO`
- `C_base^9 = NO_APTO`
- `C_diseno^36 = APTO`

Entonces:

```text
S_suelo = NO_APTO      A_custodia = NO_APTO
```

Interpretación: aunque el frente esté bien definido y el manuscrito sea correcto, el suelo técnico-operativo no es legítimo o no es trazable. No cabe cierre favorable.

### Caso 3 — suelo aceptable, diseño indeterminado

- `C_obj^9 = APTO`
- `C_base^9 = APTO`
- `C_diseno^36 = INDETERMINADO`

Entonces:

```text
S_suelo = APTO      A_custodia = INDETERMINADO
```

Interpretación: el frente y su base no fuerzan rechazo, pero la pieza no aporta todavía base suficiente de custodia del diseño, del DSL o del laboratorio.

### Caso 4 — objetivos indeterminados con base apta

- `C_obj^9 = INDETERMINADO`
- `C_base^9 = APTO`
- `C_diseno^36 = APTO`

Entonces:

```text
S_suelo = INDETERMINADO      A_custodia = INDETERMINADO
```

Interpretación: la U se conserva y la compuerta no fabrica cierre favorable cuando el propio frente no ha fijado aún su suelo de objetivos con suficiencia.

***
## 14. Implementación real y acceso a parámetros

La presente arquitectura excluye artefactos sintéticos mediante una regla simple: toda posición debe poder asociarse a un canal real de observación o declararse U/0 con honestidad estructural.

### 14.1. Canales reales admitidos

- documentos y manuscritos;
- repositorios y árbol material de archivos;
- scripts y salidas de CLI;
- parser, validator, lowering e IR;
- render e inspección material de tablas, figuras y referencias;
- APIs, servicios o artefactos del soporte técnico cuando formen parte del dominio declarado;
- ficheros de configuración, propiedades de entorno, manifiestos, capturas, logs o telemetría equivalente.

### 14.2. Canales no admitidos

- intuición sin soporte material;
- semántica basada en estadística, minería de datos, inferencia opaca o elementos no autorizados por el marco SV, incluido el tiempo desnudo cuando se lo pretende elevar a criterio soberano;
- deducción no declarada en la pieza;
- equivalentes funcionales no explicitados;
- laboratorio no reproducible por un tercero competente.

***
## 15. Programa de despliegue por bloques

La célula especializada queda en condiciones de desplegarse por bloques cerrables.

### Bloque 1 — documento base

Define la arquitectura, la semántica de las posiciones, las compuertas y la capa geométrica auxiliar.

### Bloque 2 — laboratorio Python

Ejecuta clasificación por células, compuertas, exportación de trazas y métricas geométricas auxiliares.

### Bloque 3 — prueba SVP

Comprueba que la arquitectura cabe en el carril del lenguaje sin crear metalenguaje clandestino.

### Bloque 4 — colección pública y réplica doctrinal

Publica el manuscrito, el laboratorio, los ejemplos y la réplica en sede de repositorio con índices y referencias coherentes, preservando la vecindad relativa entre `./figuras/` y `./laboratorio/`.

La arquitectura no queda rehén de imposibles porque cada bloque puede ejecutarse con los artefactos ya disponibles: texto, código, repositorio, compuertas visibles y rutas de observación material.

***
## 16. Tabla general numerada de parámetros

La tabla siguiente reúne las cincuenta y cuatro posiciones de la arquitectura completa.

| Nº | Piso | Posición | Nombre | Explicación |
|---:|---|---|---|---|
| 1 | Primer piso | O1 | Línea clara de necesidad | Existe una necesidad explícita del frente y no una intuición vaga. |
| 2 | Primer piso | O2 | Anclaje algebraico o matemático en SV | El objetivo se apoya en base estructural ya contemplada por el SV. |
| 3 | Primer piso | O3 | Alcance y fase declarados | Se declara si es continuidad de fase, nueva fase o bloque delimitado. |
| 4 | Primer piso | O4 | Elementos constitutivos definidos desde el inicio | Los componentes mínimos están identificados. |
| 5 | Primer piso | O5 | Estado del arte realizado | Consta revisión suficiente del frente correspondiente. |
| 6 | Primer piso | O6 | Revisión del corpus SV aplicable | Se ha leído el suelo doctrinal y técnico pertinente del propio sistema. |
| 7 | Primer piso | O7 | Base teórica suficiente | Existe soporte conceptual bastante para no operar por mera ocurrencia. |
| 8 | Primer piso | O8 | Laboratorios y verificaciones definidos | El frente nace con contraste material previsto. |
| 9 | Primer piso | O9 | Integración con calidad y diseño reconocidos | El objetivo queda enlazado con trazabilidad, calidad y criterios de diseño admitidos. |
| 10 | Segundo piso | Q1 | Soporte de trabajo declarado | Repositorio, entorno, pieza y alcance objeto de custodia están identificados. |
| 11 | Segundo piso | Q2 | Repositorio fresco e identificado | La fuente material usada es la vigente y verificable. |
| 12 | Segundo piso | Q3 | Árbol material completo y legible | La estructura de archivos o artefactos es accesible y no fragmentaria. |
| 13 | Segundo piso | Q4 | Herramientas de edición y ejecución declaradas | Scripts, intérpretes, validadores, viewers o utilidades empleadas están identificados. |
| 14 | Segundo piso | Q5 | Dependencias externas declaradas | Servicios, conectores, permisos o software auxiliar visibles y delimitados. |
| 15 | Segundo piso | Q6 | Control de versiones y estado operativo visibles | Rama, release, borrador o copia material declarados con veracidad. |
| 16 | Segundo piso | Q7 | Separación efectiva entre laboratorio y backend | No se endurece el backend por arrastre del laboratorio ni por entusiasmo semántico. |
| 17 | Segundo piso | Q8 | Evidencias de prueba y captura conservadas | Salidas, capturas, logs, PDF o equivalentes localizables. |
| 18 | Segundo piso | Q9 | Artefactos internos de diseño identificados | No quedan restos decisivos opacos sin absorber, o bien quedan nombrados como tales. |
| 19 | Tercer piso | A1 | Filiación doctrinal explícita | La pieza declara su dependencia del tronco doctrinal correcto. |
| 20 | Tercer piso | A2 | Límite superior explícito | El límite superior humano y de no desviación está enunciado. |
| 21 | Tercer piso | A3 | Alfabeto correcto | El artefacto no introduce valores extra-semánticos ni degrada la U. |
| 22 | Tercer piso | A4 | Horizonte de sucesos declarado | Cuando la pieza trata reevaluación, especifica el horizonte legítimo conforme al corpus canónico. |
| 23 | Tercer piso | A5 | Estatuto textual correcto | Distingue fundamento, pieza operativa, laboratorio o nota, sin usurpaciones. |
| 24 | Tercer piso | A6 | Bibliografía troncal suficiente | La pieza cita el suelo doctrinal que usa efectivamente. |
| 25 | Tercer piso | B1 | Fuente material identificada | Cada observable decisivo tiene fuente nombrada. |
| 26 | Tercer piso | B2 | Vía de acceso declarada | API, fichero, prueba, consulta, render o artefacto concreto. |
| 27 | Tercer piso | B3 | Criterio ternario explícito | Las condiciones de 0, 1 y U están escritas. |
| 28 | Tercer piso | B4 | No-aplica separado de U | La pieza distingue imposibilidad estructural de incertidumbre legítima. |
| 29 | Tercer piso | B5 | Umbral o tabla visible | No hay reglas de resolución ocultas. |
| 30 | Tercer piso | B6 | Repetibilidad local | La observación puede repetirse en el mismo entorno o en entorno equivalente. |
| 31 | Tercer piso | C1 | Traducibilidad a SVP | El artefacto cabe en el carril del lenguaje sin inventar un metalenguaje oculto. |
| 32 | Tercer piso | C2 | Tipado visible | Codominio, semántica de salida y objetos estructurales están declarados. |
| 33 | Tercer piso | C3 | Composición explícita | Las relaciones entre células, dominios, agentes y consultas aparecen nombradas. |
| 34 | Tercer piso | C4 | Totalidad de tabla | Toda compuerta relevante está definida en todos los casos necesarios. |
| 35 | Tercer piso | C5 | Sin atajo opaco | No existe comportamiento decisivo fuera del texto, la tabla y el laboratorio. |
| 36 | Tercer piso | C6 | Validabilidad previa a ejecución | El artefacto puede ser rechazado antes de correr si rompe la gramática o la bienformación. |
| 37 | Tercer piso | D1 | Paridad repo–manuscrito | Lo afirmado por el manuscrito existe en el árbol material. |
| 38 | Tercer piso | D2 | Índices y README coherentes | La sede pública no miente por omisión o desactualización. |
| 39 | Tercer piso | D3 | Referencias de figuras y laboratorios válidas | No hay rutas rotas ni recursos fantasma. |
| 40 | Tercer piso | D4 | Autoría y metadatos completos | Autor, ORCID, ISSN, licencia, versión, fecha y lugar están explícitos. |
| 41 | Tercer piso | D5 | Estado declarado veraz | Borrador, laboratorio, publicación o réplica se nombran con precisión. |
| 42 | Tercer piso | D6 | Registro de trazabilidad suficiente y sin artefactos internos de diseño no absorbidos | La pieza puede situarse en el ecosistema sin residuos decisivos opacos. |
| 43 | Tercer piso | E1 | Implementación de referencia existente | Python o equivalente visible y ejecutable. |
| 44 | Tercer piso | E2 | Ejemplos canónicos completos | Al menos un caso apto, uno no apto y uno indeterminado. |
| 45 | Tercer piso | E3 | Casos adversariales | El laboratorio no sólo confirma; también intenta romper la pieza. |
| 46 | Tercer piso | E4 | Salida trazable | El laboratorio devuelve clases, recuentos, umbrales y salida de compuerta. |
| 47 | Tercer piso | E5 | QA de presentación | Tablas, figuras y resultados pueden revisarse sin ambigüedad material. |
| 48 | Tercer piso | E6 | Persistencia de U | El laboratorio conserva explícitamente la U cuando no hay base de cierre. |
| 49 | Tercer piso | F1 | Dependencias externas declaradas | MDM, entitlements, companion, privilegios, sandbox u otras condiciones de despliegue. |
| 50 | Tercer piso | F2 | Frontera jurídica y de uso | La pieza delimita su contexto legítimo de despliegue. |
| 51 | Tercer piso | F3 | No promesa de cobertura total | No se vende como producto absoluto ni como backend ya cerrado. |
| 52 | Tercer piso | F4 | Compatibilidad de soporte | Se explicitan familias, plataformas o contextos donde aplica. |
| 53 | Tercer piso | F5 | Capa geométrica subordinada | La R³ se usa como auditoría, no como soberana semántica. |
| 54 | Tercer piso | F6 | Salida para terceros | El artefacto puede ser leído y evaluado por especialistas sin recurrir a claves internas. |

***
## 17. Diagramas operativos y correspondencia expositiva de compuertas SV

### 17.1. Diagrama de flujo clásico

La Figura 4 presenta la lógica operativa global con simbología de diagrama de flujo clásico, útil para lectura de proceso y revisión por terceros.

![Figura 4. Diagrama de flujo clásico de la célula](./figuras/figura_04_flujo_iso5807_custodia.svg)

**Figura 4.** Diagrama de flujo clásico de la célula, trazado para lectura de proceso y documentación de decisión.

### 17.2. Diagrama de actividad UML

La Figura 5 presenta la misma lógica como actividad, separando capturas, clasificación, compuertas y cierre. Se utiliza para lectura de comportamiento y no como fuente soberana de la semántica.

![Figura 5. Diagrama de actividad UML de la célula](./figuras/figura_05_actividad_uml_custodia.svg)

**Figura 5.** Diagrama de actividad UML de la célula de custodia.

### 17.3. Diagrama funcional de compuertas conservadoras

La Figura 6 ofrece un diagrama funcional de las dos compuertas conservadoras de la arquitectura: la primera resuelve el suelo (`T_suelo`) y la segunda resuelve la custodia final (`T_cust`). Ninguna compuerta puede blanquear una entrada no apta; ninguna debe forzar cierre cuando entra U.

![Figura 6. Diagrama funcional de compuertas conservadoras](./figuras/figura_06_puertas_custodia.svg)

**Figura 6.** Diagrama funcional de las dos compuertas conservadoras y de su jerarquía de composición.

### 17.4. Correspondencia expositiva entre álgebra, tabla de resolución y diagrama funcional

La Figura 8 reúne, en una sola superficie, tres vistas complementarias de la misma arquitectura: la forma algebraica mínima, la tabla de resolución ternaria conservadora y el diagrama funcional por bloques. Su finalidad es únicamente expositiva. No introduce lógica binaria clásica, no equivale a una semántica binaria de validación y no altera el estatuto propio de la terna `{0,1,U}`.

![Figura 8. Correspondencia expositiva entre álgebra, tabla de resolución y diagrama funcional de compuerta SV](./figuras/figura_08_correspondencia_compuerta_sv.svg)

**Figura 8.** Correspondencia expositiva entre forma algebraica, tabla de resolución ternaria conservadora y diagrama funcional de compuerta SV.

### 17.5. Células poligonales y lenguaje visual compartido

La Figura 7 repone el elemento nuclear de lectura del Sistema Vectorial SV: la célula como polígono visible. No es un adorno gráfico. Es el punto en el que lectura humana y lectura de máquina pueden referirse al mismo objeto estructural sin saltar inmediatamente a fórmulas o metalenguajes. La célula de objetivos, la célula de base y la célula de custodia se muestran como polígonos regulares con codificación ternaria visible de sus posiciones.

![Figura 7. Células poligonales de objetivos, base y custodia](./figuras/figura_07_celulas_poligonales_sv.svg)

**Figura 7.** Células poligonales de objetivos, base y custodia, con composición visible hacia la resolución final.

***

## 18. Elementos ambiguos y criterios de desambiguación

### 18.1. Ambigüedades estructurales a vigilar

En este frente conviene tratar como términos ambiguos, salvo que se definan expresamente, al menos los siguientes:

- **nueva fase** frente a **continuidad de fase**;
- **borrador** frente a **publicación** frente a **réplica**;
- **prototipo** frente a **laboratorio mínimo reproducible**;
- **estándar reconocido** frente a **referencia inspiradora no normativa**;
- **artefacto interno de diseño** frente a **residuo opaco decisivo**;
- **no aplica** frente a **U**;
- **figura correcta** frente a **figura visualmente bonita pero semánticamente incorrecta**.

La regla operativa es simple: cuando una de estas parejas afecte a la clasificación, debe definirse en texto visible, tabla, pseudocódigo, script o salida trazable.

### 18.2. Criterios de alcance y control inspirados en normas reconocidas

Sin convertir este manuscrito en un expediente de certificación, la versión presente adopta criterios de alcance inspirados en normas reconocidas de seguridad de la información y de documentación de procesos:

1. **alcance declarado** del frente y de sus activos documentales;
2. **identificación explícita** de dependencias, herramientas, versiones y soportes;
3. **control de cambio y de estado** entre borrador, publicación, réplica y laboratorio;
4. **evidencia de ejecución o de observación** suficiente para sostener un 0, un 1 o una U;
5. **separación de entornos** entre pieza doctrinal, laboratorio y backend futuro;
6. **diagramación legible** con semántica visible y sin mezclar flujo clásico con actividad UML como si fueran un solo artefacto.

Estos criterios sirven como disciplina de diseño y revisión, no como sustitución de la doctrina del SV.

***
## 19. Checklist mínimo de sprint implicado

Un sprint sólo puede darse por bueno, en el dominio de esta célula, si responde afirmativamente a este checklist mínimo:

- [ ] El frente declara una necesidad explícita y su alcance de fase.
- [ ] El frente acredita anclaje algebraico o matemático en el SV.
- [ ] Existe revisión del corpus SV aplicable y estado del arte suficiente.
- [ ] Los laboratorios y verificaciones necesarias están declarados.
- [ ] La fuente material usada es fresca y verificable.
- [ ] El árbol de archivos, las dependencias y el estado operativo son visibles.
- [ ] No se ha endurecido backend, IR o semántica por arrastre silencioso.
- [ ] El manuscrito, el laboratorio y la publicación no se contradicen.
- [ ] Las figuras, tablas y referencias no tienen rutas fantasma ni rótulos engañosos.
- [ ] El laboratorio devuelve salida trazable y conserva la U cuando procede.
- [ ] Los artefactos internos de diseño no absorbidos no gobiernan la decisión.
- [ ] La pieza puede ser leída por terceros sin recurrir a claves privadas ni residuos internos decisivos no absorbidos.

***
## 20. Discusión

La célula especializada aquí presentada no debe interpretarse como una policía abstracta del sistema, sino como una disciplina de visibilidad. Su fuerza no procede de prometer omnisciencia. Procede de reducir el margen en el que una deriva semántica, una fractura compilatoria o un laboratorio ilusorio podrían pasar por desarrollo legítimo.

Ese resultado se obtiene mediante una decisión arquitectónica concreta:

1. fijar un suelo explícito de objetivos del frente;
2. añadir una célula explícita de base técnico-operativa;
3. construir por encima una célula de custodia del diseño y del laboratorio;
4. resolver por compuertas conservadoras;
5. someter la forma a auditoría geométrica auxiliar;
6. y dejar todo el contrato visible en texto, tabla, pseudocódigo y laboratorio reproducible.

La arquitectura es exigente, pero no imposible. Cada parámetro propuesto tiene o bien acceso real, o bien condición explícita de U, o bien no-aplicación estructural. Cada decisión relevante tiene soporte textual, algebraico o ejecutable. Cada compuerta es total. Cada piso declara su subordinación. La protección del SV no se delega así en promesas de backend futuro, sino en una cadena visible de diseño, verificación e implementación.

***

## 21. Necesidades matemático-semánticas detectadas y elevadas al carril doctrinal superior

### 21.1. Descubrimiento estructural

Durante la formalización de esta célula y su contraste con el plano de uso se detectó un conjunto de necesidades de alto interés matemático y operativo cuyo potencial excede el perímetro legítimo de una célula especializada subordinada. Entre ellas destacan, al menos, las siguientes:

1. **cadencia observacional intra-SUCESO**;
2. **mayor densidad de cortes entre SUCESOS**;
3. **analítica continua fuerte**;
4. **derivada clásica soberana**;
5. **límite asintótico para cierre de U**.

Estas aperturas no se presentan aquí como matemática ya admitida del sistema. Se presentan como hallazgos estructurales detectados durante el trabajo, con valor potencial alto, pero todavía no autorizados como suelo normativo ni como herramienta local de clausura.

### 21.2. Razón de la no incorporación actual

La célula no puede incorporar por su cuenta esas aperturas sin alterar el reparto legítimo de autoridad del sistema. Hacerlo equivaldría, en distinto grado, a introducir matemática por vía operativa, reforzar indebidamente la soberanía de capas auxiliares, endurecer el carril de uso antes de tiempo o ejercer presión ilegítima sobre la conservación honesta de U.

Por esa razón, esta publicación mantiene las siguientes restricciones:

- no usa cadencia intra-SUCESO como criterio local de clasificación;
- no usa mayor densidad de cortes para reescribir retrospectivamente la historia válida;
- no usa analítica continua fuerte ni derivada clásica como semántica soberana de la célula;
- no usa límite asintótico alguno para forzar cierre favorable o desfavorable de U;
- y no traslada ninguna de esas hipótesis al backend futuro ni al carril N4/Uso.

### 21.3. Utilidad potencial futura y valor para el experto

La elevación formal de estas necesidades no es retórica. Si el carril doctrinal superior llegara a legitimarlas sin romper la primacía del SUCESO, la suficiencia local de la terna y la subordinación de la geometría auxiliar, el experto podría beneficiarse de una descripción más fina de trayectorias internas, de cortes más densos entre estados cercanos, de análisis más ricos sobre persistencias y fronteras, y de criterios más exigentes para distinguir entre apertura legítima y clausura prematura.

El interés de estas aperturas reside, por tanto, en ampliar la capacidad analítica del sistema sin reducirlo a continuidad indiscriminada ni a semántica importada desde marcos ajenos. Su valor futuro es real; su uso presente, en cambio, sigue prohibido mientras no exista respaldo doctrinal expreso.

### 21.4. Petición formal al carril doctrinal superior

Esta célula deja formulada una petición formal al carril doctrinal superior para que determine, con autoridad propia y sin arrastre operativo ilegítimo, si esas aperturas pueden o no ser incorporadas en el futuro al Sistema Vectorial SV.

La petición se formula con cuatro condiciones de protección:

1. que no se destruya la primacía del SUCESO como eje legítimo del cambio;
2. que la terna `{0,1,U}` conserve su suficiencia local mientras no se declare otra cosa por la autoridad competente;
3. que la geometría en ℝ³ siga siendo auxiliar y no soberana;
4. y que ninguna ampliación futura permita cerrar U por inercia estadística, continuidad tácita, extrapolación opaca o atajo asintótico no legitimado.

Hasta que exista una respuesta doctrinal superior, el estatuto correcto de estas aperturas es éste: **hallazgo relevante, utilidad potencial alta, prohibición operativa actual y elevación formal expresa**.

***

## 22. Conclusión

Se ha formalizado una versión corregida de la célula especializada de seguridad estructural apta para custodiar el diseño, el DSL y los laboratorios del Sistema Vectorial SV sin erosionar la doctrina suprema. La arquitectura resultante combina una célula de objetivos, una célula de base técnico-operativa, una célula de custodia de treinta y seis posiciones y dos compuertas conservadoras sobre codominio ternario fuerte. La capa geométrica auxiliar en ℝ³ refuerza la vigilancia sin alterar la semántica. El laboratorio mínimo demuestra que la pieza puede ejecutarse de forma visible en Python y expresarse en el carril SVP.

La consecuencia estructural es clara: el SV puede fortalecerse por pisos sin permitir que los pisos altos destruyan los cimientos bajos. La protección del sistema no exige opacidad; exige álgebra, disciplina de observación, compuertas totales, laboratorio reproducible y una conservación estricta de la U cuando el cierre no esté legitimado.

***
## Bibliografía

AdaCore. *SPARK Overview and User Resources*.

Backes, J., Ferrell, J., Grossman, D., et al. *EverParse: Verified Secure Zero-Copy Parsers for Authenticated Message Formats*. Microsoft Research.

Ellison, C., Roșu, G. *An Executable Formal Semantics of C with Applications*. K Framework.

He, K., Zhang, X., Ren, S., Sun, J. *Deep Residual Learning for Image Recognition*.

Leroy, X. *Formal Verification of a Realistic Compiler*. CompCert.

MISRA Consortium. *MISRA C* and compliance guidance.

Rust Project Developers. *The Rust Programming Language* and `rustc` mitigation notes.

SEI CERT. *CERT C Coding Standard*.

The Linux Kernel Documentation. *eBPF Verifier* and selftests documentation.

WebAssembly Community Group. *WebAssembly Core Specifications and Security Model*.

LLVM Project. *MLIR: Multi-Level Intermediate Representation*.

Lloret Egea, Juan Antonio. *Framework basado en imágenes parametrizadas sobre ResNet para identificar intrusiones en smartwatches u otros dispositivos afines*.

Lloret Egea, Juan Antonio. *De SVcustos, el marco de intrusión, hasta SVperitus: agentes especializados. Documento 1 de 8*. ITVIA. Disponible en la colección pública de ciberseguridad: https://www.itvia.online/ciberseguridad-collection

Lloret Egea, Juan Antonio. *Álgebra de composición intercelular del marco SV*.

Lloret Egea, Juan Antonio. *Álgebra de composición intercelular del marco SV — II. Gramática general de composición*.

Lloret Egea, Juan Antonio. *Álgebra de composición intercelular del marco SV — III. Horizonte de sucesos y reevaluación discreta*. ITVIA. Disponible en: https://www.itvia.online/pub/algebra-de-composicion-intercelular-del-marco-sv--iii-horizonte-de-sucesos-y-reevaluacion-discreta/release/2?readingCollection=4ebab177

Lloret Egea, Juan Antonio. *Álgebra de composición intercelular del marco SV — IV. Transducción al alfabeto ternario e interfaz paramétrica del sistema*.

Lloret Egea, Juan Antonio. *Álgebra de composición intercelular del marco SV — V. Invariantes, agentes especializados y operador de consulta del sistema*.

Lloret Egea, Juan Antonio. *Análisis del comportamiento geométrico del polígono del Sistema Vectorial SV: del plano cartesiano a una carta espacial afín auxiliar como vía de razonamiento para situaciones complejas*.



ISO. *ISO 5807:1985. Information processing — Documentation symbols and conventions for data, program and system flowcharts, program network charts and system resources charts*.

ISO/IEC. *ISO/IEC 27001:2022. Information security, cybersecurity and privacy protection — Information security management systems — Requirements*.

ISO/IEC. *ISO/IEC 27002:2022. Information security, cybersecurity and privacy protection — Information security controls*.

Object Management Group (OMG). *Unified Modeling Language (UML), Version 2.5.1*.
