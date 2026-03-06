# SVperitus — Dataset para Entrenamiento de CNN

## Módulo demostrador IMMUNO-1

**Repositorio hermano de [SVcustos-dataset](https://github.com/juantoniolloretegea/SVcustos-dataset)**

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--6634--3351-green.svg)](https://orcid.org/0000-0002-6634-3351)

**Clasificación visual de vectores ternarios de competencias clínicas mediante polígonos polares y ResNet**

Documento 7 de la serie
*«De SVcustos, el marco (framework) de intrusión, hasta SVperitus: agentes especializados»*
**ISSN 2695-641X**

---

## Descripción

Este repositorio contiene el pipeline completo del primer módulo SVperitus:
profilaxis infecciosa y vacunación en adultos con neoplasias hematológicas
e inmunosupresión. Aplica la gramática algebraica ternaria de la familia SV
(heredada de SVcustos) a un dominio de conocimiento clínico experto.

Cada caso clínico se evalúa mediante un motor normativo de 25 parámetros
(P01–P25), se representa como un polígono polar 224×224 px y se clasifica
mediante una red neuronal convolucional (ResNet-34) que emula al motor.

> ⚠️ **ADVERTENCIA CLÍNICA:** Este sistema no ha sido validado en datos
> reales y no debe utilizarse para tomar decisiones clínicas. Es un
> demostrador experimental para investigación y docencia.

---

## Ejemplos de imágenes del dataset (n=25)

Cada vector ternario se transforma en un polígono polar de 25 ejes. Los vértices se colorean por valor: 🔴 1 (riesgo / inadecuado) · 🟢 0 (adecuado) · 🟡 U (indeterminado). La CNN se entrena sobre un estilo visual homogéneo entre clases, de modo que la información discriminativa no dependa de un color global de clase sino de la geometría y disposición de los valores del vector.

| NO_APTO (n₁ ≥ 19) | INDETERMINADO | APTO (n₀ ≥ 19) |
|---|---|---|
| ![NO_APTO 1](https://raw.githubusercontent.com/juantoniolloretegea/SVperitus-dataset/main/samples/sample_no_apto_1.png) | ![INDET 1](https://raw.githubusercontent.com/juantoniolloretegea/SVperitus-dataset/main/samples/sample_indeterminado_1.png) | ![APTO 1](https://raw.githubusercontent.com/juantoniolloretegea/SVperitus-dataset/main/samples/sample_apto_1.png) |
| ![NO_APTO 2](https://raw.githubusercontent.com/juantoniolloretegea/SVperitus-dataset/main/samples/sample_no_apto_2.png) | ![INDET 2](https://raw.githubusercontent.com/juantoniolloretegea/SVperitus-dataset/main/samples/sample_indeterminado_2.png) | ![APTO 2](https://raw.githubusercontent.com/juantoniolloretegea/SVperitus-dataset/main/samples/sample_apto_2.png) |


---

## Relación con SVcustos-dataset

Este repositorio es **hermano** de
[SVcustos-dataset](https://github.com/juantoniolloretegea/SVcustos-dataset),
que contiene el código y datos asociados a los Documentos 2–6 de la serie (SVcustos n=16, 25, 36, 49 y
el par SV(36,6)+SV(9,3)). Ambos repositorios comparten la gramática
algebraica SV y las convenciones visuales del polígono polar, pero son
completamente independientes en código, datos y motor normativo.

| Aspecto | SVcustos-dataset | SVperitus-dataset |
|---|---|---|
| Dominio | Detección de intrusiones en dispositivos | Competencias clínicas (conocimiento experto) |
| Docs. asociados | 2–6 | 7 |
| Clases | INTRUSIÓN / INDETERMINADO / NORMAL | NO_APTO / INDETERMINADO / APTO |
| Gramática SV | Compartida | Compartida |
| Polígono polar | Compartido | Compartido |
| Código y datos | Independientes | Independientes |


---

## Diseño del dataset

### Imágenes neutrales

Las imágenes de los polígonos polares usan un estilo visual neutro idéntico para todas las clases. El estilo visual global es homogéneo entre clases y la señal discriminativa no depende de un color global de clase sino de la geometría y de la disposición de los valores del vector.

* **Fondo:** oscuro uniforme (#0D1B2A)
* **Polígono:** contorno y relleno dorado (mismo para todas las clases)
* **Vértices:** coloreados por valor del parámetro (0=verde, 1=rojo, U=amarillo)
* **Anillos de referencia:** tres círculos discontinuos a radio 1, 2, 3
* **Resolución:** 224×224 px (entrada nativa de ResNet)

### Convención semántica (invariante)

| Valor | Significado clínico | Radio | Anillo |
|---|---|---|---|
| `0` | Situación adecuada / aceptable según guías | 1 | Interior (vértice más cercano al centro) |
| `1` | Riesgo alto / situación inadecuada | 2 | Medio |
| `U` | Información insuficiente / evidencia ambigua | 3 | Exterior (vértice más alejado del centro) |

Implementado como: `RADIUS_MAP = {"0": 1.0, "1": 2.0, "U": 3.0}`

### Regla de clasificación

Para un vector de 25 parámetros con valores ternarios {0, 1, U}:

* **NO_APTO:** n₁ ≥ 19 (donde n₁ = número de parámetros con valor 1)
* **APTO:** n₀ ≥ 19 (donde n₀ = número de parámetros con valor 0)
* **INDETERMINADO:** resto

Con:

> **umbral T = ⌊7n/9⌋ = ⌊7·25/9⌋ = 19**

### Reproducibilidad

La generación está diseñada para ser reproducible con `seed=42` y dependencias controladas.

---

## Célula SV(25,5) — Parámetros P01–P25

Los 25 parámetros se organizan en cinco capas de cinco parámetros cada una:

| Capa | Parámetros |
|---|---|
| 1 — Estado inmunitario basal | P01 Neutropenia · P02 Linfopenia/depleción T · P03 Hipogammaglobulinemia · P04 Función esplénica · P05 Barreras y catéteres |
| 2 — Neoplasia y tratamiento | P06 Fase de la neoplasia · P07 Quimioterapia · P08 Biológicos inmunosupresores · P09 TPH/CAR-T · P10 Corticoides sistémicos |
| 3 — Historia infecciosa | P11 Infecciones bacterianas graves · P12 IFD previa · P13 Virales crónicas/latentes · P14 Colonización MDR · P15 Exposición sanitaria |
| 4 — Estado vacunal | P16 Influenza · P17 Neumococo · P18 SARS-CoV-2 · P19 Hepatitis B · P20 Otras vacunas inactivadas |
| 5 — Profilaxis y seguimiento | P21 Profilaxis PJP · P22 Profilaxis antiviral · P23 Profilaxis antifúngica · P24 Profilaxis antibacteriana · P25 Plan de reevaluación |

La definición completa de cada parámetro (criterios 0/1/U, tablas detalladas y referencias) se encuentra en el [Documento 7](docs/Documento7_IMMUNO-1.md), especificación canónica de IMMUNO-1.

---

## Estructura del repositorio

```
SVperitus-dataset/
├── README.md                 ← Este archivo
├── LICENSE                   ← CC BY-NC-ND 4.0
├── requirements.txt          ← Dependencias Python
├── .gitignore                ← Excluye data/, models/, results/
│
├── common/
│   ├── __init__.py
│   ├── polygons.py           ← draw_polar_polygon(), RADIUS_MAP
│   └── io_utils.py           ← load_config(), CSV helpers
│
├── IMMUNO-1/
│   ├── config/
│   │   └── imm_n25.yaml     ← configuración canónica (n=25, T=19)
│   ├── normative_engine.py   ← motor canónico P01–P25
│   ├── generate_cases.py     ← generador sintético (muestreo por rechazo)
│   ├── generate_polygons.py  ← vectores → imágenes PNG 224×224
│   ├── train_resnet.py       ← ResNet34 + remapeo canónico de índices
│   └── evaluate.py           ← evaluación con orden canónico YAML
│
├── IMMUNO-2/                 ← spec P01–P25 definida (borrador 0, en revisión)
│
├── rust/
│   ├── svperitus_playground_v03_final.rs  ← prototipo Playground verificado (108/108 tests)
│   └── imm1_normative/       ← estructura Cargo (placeholder, se reemplazará)
│
├── kotlin/                   ← Fase 3: cliente Kotlin (placeholder)
│
├── samples/                  ← Muestras visuales (6 imágenes)
│
├── docs/
│   ├── Documento7_IMMUNO-1.md        ← especificación canónica
│   └── Documento8_Compilador_…md     ← placeholder Doc 8
│
├── data/                     ← (generado, no en git)
├── models/                   ← (generado, no en git)
└── results/                  ← (generado, no en git)
```

**Nota:** Las carpetas `data/`, `models/` y `results/` están excluidas de git (son regenerables ejecutando el pipeline en orden).

---

## Implementación Rust (prototipo Playground)

Existe un port inicial del motor normativo de IMMUNO-1 en Rust con paridad
técnica validada en [Rust Playground](https://play.rust-lang.org)
(108/108 tests: 6 paridad global + 100 frontera en 25 parámetros + 2 serde).
Se trata de un prototipo Playground; el siguiente paso es la migración al
workspace Cargo real. Python sigue siendo la fuente canónica de verdad.
Véase [rust/README.md](rust/README.md) para detalles y procedimiento de
verificación.

---

## Inicio rápido

### 1. Instalar dependencias

```
pip install -r requirements.txt
```

Para GPU (recomendado para entrenamiento):

```
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

### 2. Generar casos sintéticos

```
python IMMUNO-1/generate_cases.py
```

### 3. Generar imágenes polares

```
python IMMUNO-1/generate_polygons.py
```

Por defecto se crean 3.000 imágenes (1.000 por clase) con estructura tipo ImageFolder:

```
IMMUNO-1/data/
  train/
    NO_APTO/          (700 imágenes)
    INDETERMINADO/    (700 imágenes)
    APTO/             (700 imágenes)
  val/
    NO_APTO/          (150 imágenes)
    INDETERMINADO/    (150 imágenes)
    APTO/             (150 imágenes)
  test/
    NO_APTO/          (150 imágenes)
    INDETERMINADO/    (150 imágenes)
    APTO/             (150 imágenes)
```

### 4. Entrenar el modelo

```
python IMMUNO-1/train_resnet.py --epochs 30 --batch-size 32
```

### 5. Evaluar

```
python IMMUNO-1/evaluate.py --model IMMUNO-1/models/<modelo>.pth
```

---

## Cadena de autoridad del motor normativo

El sistema sigue un orden vinculante de precedencia:

1. **Documento 7** (texto canónico) — especificación definitiva
2. **normative_engine.py** — implementación Python del motor
3. **imm_n25.yaml** — punto único de verdad para configuración
4. **Conjunto de paridad** (casos con `explain()`) — verificación
5. **Ports Rust/Kotlin** — traducciones fieles, nunca fuentes de criterio clínico nuevo

Ningún script define reglas clínicas fuera del motor normativo Python.

---

## Serie documental

Este dataset forma parte de la serie «De SVcustos, el marco (framework) de intrusión, hasta SVperitus: agentes especializados», compuesta por 8 documentos:

| Doc. | Contenido | Código y datos |
|---|---|---|
| 1 | Marco conceptual y gramática algebraica SV | [Serie completa](https://www.itvia.online/de-svcustos-el-marco-framework-de-intrusion-hasta-svperitus-agentes-especializados) |
| 2–6 | SVcustos SV(16,4) a SV(49,7) + par | [SVcustos-dataset](https://github.com/juantoniolloretegea/SVcustos-dataset) |
| **7** | **SVperitus–IMMUNO-1 (este repositorio)** | **SVperitus-dataset** |
| 8 | Compilador SVcustos + SVperitus + Célula meta SV(9,3)-IA | — |


---

## Cita

Si desea citar este repositorio en un trabajo académico, puede usar un esquema genérico como:

```
@misc{lloret_svperitus_dataset,
  author       = {Lloret Egea, Juan Antonio},
  title        = {SVperitus-dataset: generación de imágenes polares ternarias
                  y entrenamiento de CNN para agentes especializados
                  de conocimiento clínico},
  year         = {2026},
  note         = {Repositorio de código y datos sintéticos asociado a la serie
                  «De SVcustos, el marco de intrusión, hasta SVperitus:
                  agentes especializados» — Documento 7 (IMMUNO-1)}
}
```

---

## Autor

**Juan Antonio Lloret Egea**
ORCID: [0000-0002-6634-3351](https://orcid.org/0000-0002-6634-3351)

Serie documental: «De SVcustos, el marco (framework) de intrusión, hasta SVperitus: agentes especializados»
ISSN 2695-641X · CC BY-NC-ND 4.0
