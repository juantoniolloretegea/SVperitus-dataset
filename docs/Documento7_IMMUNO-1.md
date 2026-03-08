# Documento 7 — SVperitus–IMMUNO-1

**SVperitus–IMMUNO-1: módulo demostrador de profilaxis infecciosa y vacunación
en neoplasias hematológicas**

*Documento 7 de la serie «De SVcustos, el marco (framework) de intrusión,
hasta SVperitus: agentes especializados»*

---

**Autor:** Juan Antonio Lloret Egea
**ORCID:** [0000-0002-6634-3351](https://orcid.org/0000-0002-6634-3351)
**ISSN:** 2695-6411
**Fecha:** 5 de marzo de 2026
**Licencia:** CC BY-NC-ND 4.0
**Repositorio SVperitus–IMMUNO-1:** repositorio hermano de
[SVcustos-dataset](https://github.com/juantoniolloretegea/SVcustos-dataset)

---

## Posición en la serie

Esta serie documental consta de ocho documentos que describen la evolución
del sistema vectorial ternario desde SVcustos (detección de intrusiones en
dispositivos) hasta SVperitus (agentes de conocimiento experto):

| Doc. | Contenido |
|---|---|
| 1 | Marco conceptual y gramática algebraica SV |
| 2 | SVcustos SV(16,4) — dataset y CNN |
| 3 | SVcustos SV(25,5) — dataset y CNN |
| 4 | SVcustos SV(36,6) — dataset y CNN |
| 5 | Células SV en par: SV(36,6) + SV(9,3) |
| 6 | SVcustos SV(49,7) — dataset y CNN |
| **7** | **SVperitus–IMMUNO-1 — módulo demostrador (este documento)** |
| 8 | Compilador SVcustos + SVperitus + Célula meta SV(9,3)-IA |

Los ocho documentos de la serie se publican en:
https://www.itvia.online/de-svcustos-el-marco-framework-de-intrusion-hasta-svperitus-agentes-especializados

El código y los datasets asociados a los Documentos 2–6 se encuentran en el
repositorio [SVcustos-dataset](https://github.com/juantoniolloretegea/SVcustos-dataset).

El presente Documento 7 corresponde al primer módulo SVperitus, cuyo código y
datos se encuentran en el repositorio hermano
[SVperitus-dataset](https://github.com/juantoniolloretegea/SVperitus-dataset),
sin modificar SVcustos-dataset en ningún punto. Los dos repositorios comparten
gramática algebraica y convenciones visuales, pero son completamente
independientes en código y datos.

---

## Resumen

Los adultos con neoplasias hematológicas sometidos a terapias inmunosupresoras
presentan un riesgo elevado de infecciones graves, en el que la adecuación de
la profilaxis, la vacunación y la monitorización longitudinal condiciona de
forma crítica la morbimortalidad. Las guías internacionales de referencia en
neutropenia febril, profilaxis antifúngica y vacunación del paciente
inmunocomprometido proporcionan recomendaciones sólidas, pero su aplicación
integrada caso a caso sigue siendo compleja en la práctica clínica diaria.

SVperitus–IMMUNO-1 es un demostrador teórico-técnico que aplica el marco
algebraico ternario de la familia SV (SVcustos + SVperitus) al dominio de la
profilaxis infecciosa y la vacunación en hematología. Define una célula de
conocimiento SV(25,5) en la que 25 parámetros clínicamente justificados,
organizados en cinco capas (estado inmunitario basal, neoplasia y tratamiento,
historia infecciosa, estado vacunal y profilaxis/seguimiento), se codifican en
valores 0 / 1 / U (Apto / No Apto / Indeterminado) a partir de criterios
explícitos derivados de guías y consensos. Sobre esta base se construye un
motor normativo que clasifica cada vector en Apto, Indeterminado o No Apto
mediante la regla estricta T(25) = 19, y un generador de casos sintéticos
auditables que explora de forma controlada el espacio combinatorio. Cada
vector se representa como un polígono polar interpretable en el que los radios
1, 2 y 3 corresponden, respectivamente, a 0, 1 y U. A partir de estas
imágenes, una red neuronal convolucional se entrena para emular al motor
normativo: no para crear un criterio nuevo, sino para permitir exploraciones
masivas del espacio 3²⁵ bajo un «oráculo» clínico transparente.

El sistema no ha sido validado en datos reales y no es una herramienta clínica
de decisión, sino una prótesis cognitiva experimental diseñada para: (1) hacer
visibles las zonas de certeza e incertidumbre; (2) apoyar la enseñanza y la
discusión de casos complejos; y (3) preparar el terreno para futuros agentes
expertos SVperitus más amplios, una vez se disponga de datos clínicos y
validación externa adecuados.

---

## Abstract

Adults with haematologic malignancies receiving immunosuppressive therapy are
at high risk of severe infections, where the adequacy of prophylaxis,
vaccination and longitudinal monitoring critically shapes morbidity and
mortality. International guidelines on febrile neutropenia, antifungal
prophylaxis and vaccination of immunocompromised patients provide robust
recommendations, yet their integrated, patient-level application remains
challenging in everyday practice.

SVperitus–IMMUNO-1 is a theoretical and technical proof-of-concept that applies
the ternary algebraic framework of the SV family (SVcustos + SVperitus) to the
domain of infectious prophylaxis and vaccination in haematology. It defines a
SV(25,5) knowledge cell in which 25 clinically grounded parameters, structured
into five layers (baseline immune status, malignancy and treatment, infectious
history, vaccination status, and prophylaxis/follow-up), are encoded as
0 / 1 / U (Fit / Unfit / Undetermined) using explicit criteria derived from
guidelines and expert consensus. On top of this, a normative engine assigns
each vector to Fit, Undetermined or Unfit using the strict threshold rule
T(25) = 19, and a synthetic, auditable case generator explores the
combinatorial space in a controlled way. Each vector is rendered as an
interpretable polar polygon where radii 1, 2 and 3 correspond to 0, 1 and U,
respectively. From these images, a convolutional neural network is trained to
emulate the normative engine — not to create new clinical rules, but to enable
large-scale exploration of the 3²⁵ space under a transparent clinical «oracle».

The system has not been validated on real-world data and is not a clinical
decision-making tool; instead, it is an experimental cognitive prosthesis
designed to (1) make zones of certainty and uncertainty visible, (2) support
teaching and case-based discussion in complex scenarios, and (3) lay the
groundwork for broader SVperitus expert agents once appropriate clinical
datasets and external validation become available.

---

> ⚠️ **ADVERTENCIA CLÍNICA**
>
> Este documento describe un marco teórico-técnico de apoyo cognitivo basado
> en lógica ternaria y visión por computador. **No es una guía de práctica
> clínica**, no ha sido validado en datos reales y **no debe utilizarse para
> tomar decisiones diagnósticas o terapéuticas sobre pacientes individuales**.
> Cualquier aplicación clínica requeriría un programa específico de validación,
> supervisión ética y actualización de umbrales.

---

## Agradecimientos

A todos los clínicos, inmunólogos, hematólogos, microbiólogos y especialistas
en enfermedades infecciosas que, con su trabajo y sus guías, han proporcionado
el sustrato de conocimiento sobre el que se construye este demostrador.

---

## Índice

1. [Introducción y motivación](#1-introducción-y-motivación)
2. [Gramática algebraica SVperitus — herencia de SVcustos](#2-gramática-algebraica-svperitus--herencia-de-svcustos)
3. [Módulo IMMUNO-1: dominio y alcance](#3-módulo-immuno-1-dominio-y-alcance)
4. [Definición formal del motor normativo](#4-definición-formal-del-motor-normativo)
5. [Estructura de los 25 parámetros](#5-estructura-de-los-25-parámetros)
6. [Representación en polígono polar](#6-representación-en-polígono-polar)
7. [Pipeline completo: del caso clínico al modelo CNN](#7-pipeline-completo-del-caso-clínico-al-modelo-cnn)
8. [Arquitectura del repositorio](#8-arquitectura-del-repositorio)
9. [Estrategia multilenguaje: Python, Rust y Kotlin](#9-estrategia-multilenguaje-python-rust-y-kotlin)
10. [Líneas futuras de investigación y desarrollo](#10-líneas-futuras-de-investigación-y-desarrollo)
11. [Próximo documento: Documento 8](#11-próximo-documento-documento-8)
12. [Referencias](#12-referencias)

---

## 1. Introducción y motivación

Los pacientes adultos con neoplasias hematológicas (leucemias agudas, linfomas,
mieloma múltiple, síndromes mielodisplásicos, entre otros) constituyen una
población con riesgo especialmente elevado de infecciones graves. La
combinación de inmunodeficiencia intrínseca de la enfermedad, mielosupresión
inducida por la quimioterapia, uso de terapias biológicas dirigidas a células
B o T y procedimientos como el trasplante de progenitores hematopoyéticos o la
terapia con células CAR-T configura un paisaje de riesgo complejo, dinámico y
difícil de sintetizar en la práctica diaria.

Las guías de referencia (ECIL, ESCMID, IDSA) proporcionan recomendaciones
sólidas en dominios específicos: profilaxis antibacteriana en neutropenia
prolongada, profilaxis antifúngica en pacientes de alto riesgo, vacunación
frente a neumococo, influenza, SARS-CoV-2 y otros patógenos prevenibles,
manejo de portadores de virus crónicos, entre otros. Sin embargo, el clínico
se enfrenta a menudo a la tarea de integrar, para un paciente concreto y en
un momento concreto del curso terapéutico, múltiples factores de riesgo y de
protección que no se presentan de forma naturalmente algebraica.

SVperitus–IMMUNO-1 aborda este problema mediante la gramática algebraica de la
familia SV: células de parámetros ternarios (0, 1, U), reglas estrictas de
clasificación global y representación polar interpretable. Su objetivo no es
predecir un evento aislado, sino capturar de forma estructurada la adecuación
global de la profilaxis infecciosa y el estado vacunal, señalando con claridad
cuáles son las áreas razonablemente cubiertas, cuáles son claramente inadecuadas
y cuáles permanecen en zona gris por falta de información o por evidencia
insuficiente. El resultado es un módulo de conocimiento que visualiza
simultáneamente adecuación, riesgo e incertidumbre.

### 1.1. Estado del arte en profilaxis infecciosa, vacunación e IA en hematología

La profilaxis infecciosa y la vacunación en pacientes con neoplasias
hematológicas se apoyan hoy en un cuerpo sólido de guías internacionales,
aunque disperso en múltiples documentos y centrado en situaciones clínicas
específicas.

En el ámbito de la fiebre y la neutropenia, las guías de las principales
sociedades científicas han establecido umbrales clásicos (neutrófilos < 500/µL,
duración esperada de la neutropenia, comorbilidad) como ejes de decisión para
el uso de antimicrobianos, la estratificación de riesgo y la selección de
pacientes candidatos a tratamiento ambulatorio. Sin embargo, la combinación
explícita de estos factores en un marco algebraico interpretable rara vez se
hace visible al clínico.

En profilaxis antifúngica, los consensos recientes han refinado los criterios
para indicar profilaxis primaria en distintos subgrupos (leucemia aguda,
síndromes mielodisplásicos de alto riesgo, trasplante alogénico, terapias
celulares) y para seleccionar fármacos en función del riesgo de enfermedad
fúngica invasora. El enfoque se desplaza desde algoritmos rígidos hacia
decisiones estratificadas por contexto, lo que evidencia la necesidad de
herramientas que integren múltiples dimensiones de riesgo de manera transparente.

En vacunación, las recomendaciones dirigidas a pacientes con cáncer han
reforzado la prioridad de la vacunación frente a SARS-CoV-2 y otros patógenos
prevenibles, pero la integración de calendarios vacunales complejos con
terapias inmunosupresoras y ventanas de seguridad sigue siendo un reto práctico.

En paralelo, la inteligencia artificial ha comenzado a ocupar un lugar relevante
en hematología y enfermedades infecciosas: existen modelos de aprendizaje
automático que utilizan datos de laboratorio y variables clínicas para
diagnóstico, estratificación pronóstica o predicción de complicaciones
infecciosas. Muchos de estos modelos muestran una discriminación prometedora,
pero comparten limitaciones importantes desde la perspectiva de SVperitus–
IMMUNO-1: dominan los enfoques puramente numéricos, la relación con las guías
es indirecta, el foco se sitúa en eventos agudos más que en la calidad
estructural de la profilaxis, y la incertidumbre derivada de datos faltantes o
evidencia ambigua no suele representarse de forma explícita.

SVperitus–IMMUNO-1 se sitúa como un enfoque complementario: parte de un motor
normativo explícito, construido desde guías y consensos, que opera sobre una
célula SV(25,5) con lógica ternaria, y utiliza la red neuronal como emulador
de ese criterio, no como fuente autónoma de reglas.

### 1.2. Resumen ejecutivo: qué es SVperitus–IMMUNO-1 y qué cabe esperar de él

**Qué es:** un módulo de conocimiento estructurado (SV(25,5)) que codifica,
de forma algebraica y visualmente interpretable, la adecuación de la profilaxis
infecciosa y la vacunación en adultos con neoplasias hematológicas, utilizando
criterios derivados de guías clínicas.

**Qué hace:** recibe un caso clínico estructurado, aplica 25 reglas normativas
ternarias 0/1/U, genera un polígono polar representable y asigna una clase
global Apto / Indeterminado / No Apto mediante la regla estricta T(25) = 19.
A partir de ahí, permite generar casos sintéticos, entrenar una CNN que emula
al motor normativo y explorar de forma masiva y transparente el impacto
combinado de cambios en profilaxis, vacunación y contexto clínico.

**Para qué sirve en esta fase:** como demostrador conceptual y herramienta de
apoyo cognitivo para investigación y docencia. Facilita la discusión
estructurada de casos, ayuda a identificar de forma explícita qué condiciones
están adecuadamente cubiertas, cuáles son claramente inadecuadas y dónde
domina la incertidumbre, y ofrece un marco reproducible para diseñar estudios
piloto y futuros agentes expertos.

**Qué no hace:** no ha sido validado con datos reales, no estima riesgos
individuales de eventos clínicos concretos, no reemplaza a ningún sistema de
soporte a la decisión clínica existente ni emite recomendaciones terapéuticas
automáticas. Cualquier uso clínico futuro exigirá validación específica,
supervisión ética y actualización de umbrales basada en evidencia.

---

## 2. Gramática algebraica SVperitus — herencia de SVcustos

SVperitus reutiliza la gramática algebraica de SVcustos sin modificar sus
invariantes fundamentales. La diferencia es semántica: SVcustos describe
vectores de superficie de ataque digital; SVperitus describe vectores de
conocimiento experto en dominios clínicos y científicos.

### 2.1. Invariantes algebraicas

| Concepto | Definición |
|---|---|
| Tamaño de célula | n = b², con b ≥ 3 |
| Espacio de estados | 3ⁿ |
| Valores por parámetro | Ternario: {0, 1, U} |
| Representación visual | Polígono polar de n ejes |
| Umbral global | T(n) = ⌊7n/9⌋ |

Para n = 25: T(25) = ⌊175/9⌋ = **19**

Regla de clasificación:

- n₁ ≥ T(n) → **No Apto**
- n₀ ≥ T(n) → **Apto**
- resto → **Indeterminado**

### 2.2. Semántica canónica de los valores ternarios

Esta sección concentra la convención definitiva de 0 / 1 / U para todo el
proyecto SVcustos + SVperitus. Es vinculante para toda implementación,
documento y material audiovisual:

```
0  →  Apto / situación adecuada / aceptable según guías
1  →  No Apto / situación inadecuada / de alto riesgo
U  →  Indeterminado / información insuficiente o evidencia ambigua
```

La misma convención desplegada con su correspondencia visual:

| Valor | Significado | Radio en polígono polar | Anillo |
|---|---|---|---|
| **`0`** | Apto / situación adecuada / aceptable según guías | 1 | Interior |
| **`1`** | No Apto / situación inadecuada / de alto riesgo | 2 | Medio |
| **`U`** | Indeterminado / información insuficiente o evidencia ambigua | 3 | Exterior |

Implementado en `common/polygons.py`:

```python
RADIUS_MAP = {"0": 1.0, "1": 2.0, "U": 3.0}
```

No existe ninguna otra convención válida en este proyecto. Cualquier
implementación que invierta o reordene los radios para `1` y `U` es errónea.

### 2.3. Semántica comparada SVcustos / SVperitus

| | SVcustos | SVperitus–IMMUNO-1 |
|---|---|---|
| Valor `0` | Superficie de ataque correctamente defendida | Situación preventiva adecuada según guías |
| Valor `1` | Vector de intrusión activo o grave | Situación claramente inadecuada o de alto riesgo |
| Valor `U` | Estado no evaluado o información incompleta | Información faltante o evidencia insuficiente |
| Mayoría de `1` | **INTRUSIÓN** | **NO_APTO** |
| Mayoría de `0` | **NORMAL** | **APTO** |
| Caso residual | **INDETERMINADO** | **INDETERMINADO** |

Los identificadores de clase en código y configuración son `NO_APTO`,
`INDETERMINADO`, `APTO`. En el texto científico se escriben «No Apto»,
«Indeterminado» y «Apto». Son la misma cosa.

---

## 3. Módulo IMMUNO-1: dominio y alcance

### 3.1. Dominio clínico

IMMUNO-1 se define sobre el dominio: **Profilaxis infecciosa y vacunación en
adultos con neoplasias hematológicas e inmunosupresión.**

Se centra en:

- Pacientes con leucemias agudas, linfomas, mieloma múltiple, síndromes
  mielodisplásicos y otras neoplasias hematológicas.
- Situaciones con riesgo significativo de infecciones bacterianas graves,
  enfermedad fúngica invasora, reactivación viral y enfermedades prevenibles
  por vacunación.
- Contextos de quimioterapia intensiva, terapias biológicas, inmunoterapia,
  trasplante de progenitores hematopoyéticos y terapia celular.

### 3.2. Alcance declarado

El módulo IMMUNO-1 no pretende cubrir todo el espectro de la inmunología
clínica. Se limita a 25 parámetros organizados en cinco capas que capturan
el núcleo de la profilaxis y la vacunación en este contexto. Está diseñado
para ser extensible: futuras células n = 36 o n = 49 podrían añadir
dimensiones adicionales (comorbilidad detallada, biomarcadores específicos,
patrones de resistencia local).

### 3.3. Estructura en capas

| Capa | Contenido |
|---|---|
| 1 | Estado inmunitario basal |
| 2 | Neoplasia y tratamiento |
| 3 | Historia infecciosa |
| 4 | Estado vacunal |
| 5 | Profilaxis y seguimiento |

Cada capa agrupa cinco parámetros Pₖ con criterios 0/1/U definidos
de forma explícita en `normative_engine.py`.

---

## 4. Definición formal del motor normativo

### 4.1. Archivos canónicos

El motor normativo canónico de IMMUNO-1 es `IMMUNO-1/normative_engine.py`.
Contiene las funciones `P01(case)` … `P25(case)`, la función
`evaluate_and_classify(case)` que devuelve el vector ternario y la clase
global, y `explain(case)` para trazabilidad completa.

La configuración formal (punto único de verdad para n, threshold, nombres de
clase y `class_to_idx`) es `IMMUNO-1/config/imm_n25.yaml`. Todos los scripts
del pipeline leen estos valores del YAML; ninguno los duplica como constante
local.

### 4.2. Principio de autoridad del motor

> `generate_cases.py` **no define clínica**: invoca el motor y rellena datos
> sintéticos alrededor de los criterios clínicos fijados en
> `normative_engine.py`.
>
> Cualquier implementación futura (Rust, Kotlin, etc.) debe ser
> **bit-a-bit equivalente** a este motor Python.
>
> **Todo cambio en las reglas normativas se hace primero en este documento
> formal y en `normative_engine.py`. Rust y Kotlin son ports, no fuentes
> de verdad.**

### 4.3. Función de agregación

Dado un caso clínico, el motor evalúa cada Pₖ (k = 1…25) y obtiene el
vector ternario V = (P₁, …, P₂₅), Pₖ ∈ {0, 1, U}.

Se calculan:
- **n₁** = #{k : Pₖ = `1`} — parámetros en situación inadecuada o de riesgo
- **n₀** = #{k : Pₖ = `0`} — parámetros en situación adecuada
- **nᵤ** = #{k : Pₖ = `U`} — parámetros indeterminados

Y se aplica con T(25) = 19:

| Condición | Clase |
|---|---|
| n₁ ≥ 19 | **No Apto** |
| n₀ ≥ 19 | **Apto** |
| resto | **Indeterminado** |

### 4.4. Trazabilidad

La función `explain(case)` devuelve el vector completo {P01..P25} con sus
valores 0/1/U, las razones textuales asociadas a cada decisión y la clase
global resultante. Toda decisión 0/1/U es trazable al campo clínico concreto
que la generó.

---

## 5. Estructura de los 25 parámetros

Los 25 parámetros se organizan en cinco capas de cinco parámetros cada una,
siguiendo la cuadrícula 5×5 de la célula n = 25. La implementación completa,
con todos los campos del `case` dict y sus umbrales exactos, está en
`normative_engine.py`.

**Regla dura de implementación:** si un campo clínico está ausente o no
documentado, el parámetro correspondiente se marca **U**. Nunca se imputa
`0` por defecto ante ausencia de datos.

### Capa 1 — Estado inmunitario basal

| Pₖ | Nombre | Criterio `1` (riesgo/inadecuado) | Criterio `0` (adecuado) | `U` |
|---|---|---|---|---|
| P01 | Neutropenia | ANC actual < 500, o nadir previsto < 500 con duración ≥ 7 días | ANC ≥ 1000 sin nadir problemático previsto | ANC 500–999, duración incierta o datos ausentes |
| P02 | Linfopenia / depleción T | CD4 < 200, o linfocitos totales < 500 | CD4 ≥ 500 sin terapia depletora T activa | CD4 200–499, zona gris o solo proxy de linfocitos disponible |
| P03 | Hipogammaglobulinemia | IgG < 400 mg/dL, o IgG 400–699 con ≥ 2 infecciones bacterianas graves en 12 meses | IgG ≥ 700 mg/dL sin historia infecciosa recurrente | IgG 400–699 sin historia clara, o IgG ausente |
| P04 | Función esplénica | Asplenia o hipoesplenismo sin vacunas frente a encapsulados ni profilaxis | Bazo anatómicamente presente y funcionante (ambos campos False confirmados) | Estado esplénico no completamente documentado |
| P05 | Barreras y catéteres | Mucositis ≥ grado 2, úlceras relevantes, o CVC con complicaciones | Sin alteración relevante de barreras ni CVC complicado | Información insuficiente sobre integridad de barreras |

### Capa 2 — Neoplasia y tratamiento inmunosupresor

| Pₖ | Nombre | Criterio `1` | Criterio `0` | `U` |
|---|---|---|---|---|
| P06 | Fase de la neoplasia | Inducción, consolidación o recaída de alto riesgo | Mantenimiento o fase crónica estable | Fase no caracterizada |
| P07 | Quimioterapia | Intensidad alta en los últimos 30 días | Intensidad baja con quimioterapia intensa > 90 días | Intensidad estándar o cronología ambigua |
| P08 | Biológicos inmunosupresores | Anti-CD20, BTKi o PI3Ki en los últimos 12 meses sin cribado viral documentado | Sin estas terapias en el período, o con cribado viral documentado | Terapia presente sin detalle de cribado |
| P09 | TPH / CAR-T | Alo-TPH < 2 años, EICH activa, o CAR-T < 1 año sin programa de profilaxis y revacunación | Sin procedimiento documentado, o auto-TPH > 2 años con programa activo | Todos los campos de procedimiento ausentes |
| P10 | Corticoides sistémicos | ≥ 20 mg/día equivalente prednisona durante ≥ 4 semanas sin riesgo PJP evaluado y gestionado | Dosis ≤ 10 mg/día o duración < 2 semanas, o dosis alta con riesgo correctamente evaluado y gestionado | Dosis/duración no documentadas o zona intermedia 10–19 mg / 2–3 semanas |

### Capa 3 — Historia infecciosa y colonización

| Pₖ | Nombre | Criterio `1` | Criterio `0` | `U` |
|---|---|---|---|---|
| P11 | Infecciones bacterianas graves (12 m) | ≥ 1 episodio en los últimos 12 meses sin revisión del plan profiláctico | Sin episodios, o episodios con plan revisado | Datos insuficientes sobre historia infecciosa |
| P12 | IFD previa o contexto de alto riesgo | IFD previa sin profilaxis adecuada, o contexto de alto riesgo sin cobertura | Sin historia de IFD ni contexto de riesgo elevado | IFD previa con profilaxis adecuada en curso (cicatriz presente; la cobertura reduce pero no anula el riesgo) |
| P13 | Infecciones virales crónicas o latentes | Infección viral crónica activa, o portador VHB con anti-CD20 activo, sin plan de profilaxis/monitorización | Cribado completo y plan de manejo correcto documentado | Cribado incompleto o plan no documentado pese a hallazgos |
| P14 | Colonización MDR | Colonización por patógeno multirresistente conocida sin estrategia de manejo | Sin colonización conocida, o colonización con estrategia definida | Información fragmentaria sobre colonización |
| P15 | Exposición sanitaria reciente | Hospitalización prolongada o ingreso en UCI recientes sin ajuste del plan profiláctico | Sin exposición sanitaria relevante reciente, o con plan ajustado | Historia asistencial reciente incompleta |

### Capa 4 — Estado vacunal

| Pₖ | Nombre | Criterio `1` | Criterio `0` | `U` |
|---|---|---|---|---|
| P16 | Influenza estacional | No vacunado en la temporada actual sin contraindicación documentada | Vacunado en la temporada actual, o vacunación contraindicada explícitamente | Estado vacunal desconocido |
| P17 | Neumococo | Sin secuencia de vacunación frente a neumococo registrada | Secuencia completa (PCV20, o PCV13 + PPSV23 con intervalos correctos) | Datos parciales de vacunación |
| P18 | SARS-CoV-2 | Paciente de alto riesgo hematológico sin pauta primaria ni refuerzos actualizados | Pauta primaria y refuerzos actualizados, o estado vacunal que garantiza cobertura | Estado vacunal no documentado o situación de riesgo no determinable |
| P19 | Hepatitis B | Serie incompleta, o serie completa con anti-HBs no protector sin revacunación | Serie completa con anti-HBs protector (≥ 10 UI/L), o no respondedor ya revacunado | Serie referida sin serología posterior |
| P20 | Otras vacunas inactivadas relevantes | Vacuna viva administrada con contraindicación activa, o calendario claramente inadecuado al perfil de riesgo | Calendario adecuado al perfil de inmunosupresión del paciente | Información vacunal muy parcial o no estructurada |

### Capa 5 — Profilaxis farmacológica y plan de seguimiento

| Pₖ | Nombre | Criterio `1` | Criterio `0` | `U` |
|---|---|---|---|---|
| P21 | Profilaxis frente a PJP | Criterios clínicos cumplidos sin profilaxis activa (TMP-SMX u alternativa) | Profilaxis activa y correcta, o criterios no cumplidos | Criterios de indicación no establecidos |
| P22 | Profilaxis antiviral (HSV/VZV ± CMV) | Indicada sin profilaxis activa ni monitorización de CMV | Esquema adecuado de profilaxis/monitorización, o profilaxis no indicada | Nivel de riesgo viral no determinable |
| P23 | Profilaxis antifúngica | Contexto de alto riesgo de IFD sin cobertura antifúngica adecuada en curso | Contexto de alto riesgo con profilaxis adecuada, o ausencia de contexto de riesgo elevado | Datos insuficientes para determinar riesgo o cobertura |
| P24 | Profilaxis antibacteriana en neutropenia | Neutropenia de alto riesgo y duración prolongada sin política de profilaxis antibacteriana documentada | Política documentada y razonada (incluyendo decisión explícita de no darla), o sin neutropenia de alto riesgo | Nivel de riesgo neutropénico no determinable |
| P25 | Plan estructurado de reevaluación | Sin plan de reevaluación explícito (gestión puramente reactiva) | Plan explícito con periodicidad definida que incluye revisión de vacunas y profilaxis | Plan existente pero incompleto o sin periodicidad definida |

### Notas de diseño del módulo IMMUNO-1

- **P04** evalúa la adecuación del plan preventivo frente a la asplenia, no
  el riesgo residual biológico irreducible. Una asplenia bien gestionada
  (vacunas y profilaxis correctas) puntúa `0`.
- **P10** usa `pjp_risk_assessed = True` en el código para indicar «riesgo
  evaluado Y manejo correcto documentado», no solo que el riesgo fue
  identificado.
- **P12 y P23** comparten información sobre la historia fúngica pero tienen
  propósito distinto: P12 recoge la cicatriz de infección fúngica invasora y
  el riesgo acumulado; P23 evalúa la adecuación de la cobertura antifúngica
  en el momento presente.
- **P11, P15 y P25** presentan solapamiento conceptual en la condición «plan
  profiláctico revisado». Se analizará su independencia efectiva en futuras
  revisiones clínicas, con posible fusión o redefinición si procede.

---

## 6. Representación en polígono polar

### 6.1. Convención canónica de valores y radios

La siguiente tabla es la convención definitiva, invariante para cualquier
representación visual —estática, interactiva o en vídeo— de SVperitus y
SVcustos:

| Valor | Significado clínico | Radio | Anillo visual |
|---|---|---|---|
| **`0`** | Situación adecuada / aceptable | **1** — interior | Vértice en el anillo más cercano al centro |
| **`1`** | Riesgo alto / situación inadecuada | **2** — medio | Vértice en el anillo intermedio |
| **`U`** | Información insuficiente / indeterminada | **3** — exterior | Vértice en el anillo más alejado del centro |

```python
RADIUS_MAP = {"0": 1.0, "1": 2.0, "U": 3.0}   # common/polygons.py
```

Cualquier implementación que invierta los radios para `1` y `U` es errónea.
No se admite ninguna otra asignación.

### 6.2. Geometría del polígono

- 25 ejes angularmente equiespaciados: separación de 360°/25 = 14,4° entre
  ejes consecutivos.
- Tres anillos de referencia a radios 1, 2 y 3 sobre cada eje.
- El vértice del eje k-ésimo se sitúa en el radio correspondiente al valor de
  Pₖ según la tabla anterior.
- Los vértices se unen formando el polígono cerrado.

### 6.3. Lectura visual del polígono

| Morfología del polígono | Interpretación |
|---|---|
| Predominantemente interior (radio 1) | Perfil globalmente Apto |
| Múltiples picos en radio 2 | Parámetros claramente inadecuados → candidato a No Apto |
| Radios frecuentes en 3 | Zonas de información faltante o evidencia ambigua → Indeterminado |

### 6.4. Estilo visual

Estilo neutro e idéntico para las tres clases (fondo oscuro `#0D1B2A`, ejes
discretos, polígono en color dorado `#C9A84C`, común con SVcustos). La CNN
aprende del patrón geométrico, no del color de clase.

### 6.5. Vídeo demostrativo

La generación del vídeo demostrativo es un desarrollo independiente que puede
mostrar, por ejemplo, la transición dinámica de un caso No Apto a Apto tras
corregir parámetros clave (profilaxis, vacunación, etc.). Se trata de una
pieza de divulgación y docencia, no de validación clínica, y requerirá una
fase de trabajo específica posterior a la consolidación del repositorio.

---

## 7. Pipeline completo: del caso clínico al modelo CNN

```
Caso clínico (dict de campos clínicos)
        │
        ▼  normative_engine.py
        │  P01–P25 + evaluate_and_classify()
        │  → vector ternario {0,1,U}²⁵ + clase global
        │
        ▼  generate_cases.py
        │  Muestreo por rechazo, semilla fija
        │  → dataset sintético balanceado en data/vectors/ (CSV)
        │    splits train / val / test  (70 / 15 / 15)
        │
        ▼  generate_polygons.py  +  common/polygons.py
        │  Vector ternario → imagen PNG 224×224 px
        │  Convención: 0 → radio 1, 1 → radio 2, U → radio 3
        │  → estructura ImageFolder en data/images/
        │
        ▼  train_resnet.py
        │  ResNet34 (preentrenada ImageNet)
        │  Remapeo índices disco → canónico vía target_transform
        │  CosineAnnealingLR, guardado del mejor modelo por val_acc
        │  → modelo .pth en models/
        │
        ▼  evaluate.py
           Remapeo índices disco → canónico (mismo patrón que entrenamiento)
           → accuracy + classification_report + matriz de confusión
             con orden canónico NO_APTO / INDETERMINADO / APTO
```

### 7.1. Coherencia de índices de clase en el pipeline

ImageFolder asigna índices por orden alfabético de carpetas en disco
(`APTO=0, INDETERMINADO=1, NO_APTO=2`). El orden canónico del YAML es
`NO_APTO=0, INDETERMINADO=1, APTO=2`. Tanto `train_resnet.py` como
`evaluate.py` resuelven esta discrepancia de forma explícita e idéntica:
construyen `idx_map = {índice_disco → índice_canónico}` desde el YAML y
aplican `target_transform = lambda idx: idx_map[idx]`. Desde ese momento,
la red y todas las métricas trabajan exclusivamente con índices canónicos.

### 7.2. Dataset sintético auditable

- Casos generados con distribución controlada entre Apto, Indeterminado y
  No Apto.
- Cada caso incluye: campos clínicos, vector SV(25), clase global y
  explicación (`engine.explain()`).
- Permite reproducir cualquier resultado del modelo a nivel de regla clínica.

### 7.3. Entrenamiento de la CNN

- Arquitectura base: ResNet-34 (preentrenada en ImageNet).
- Tarea: emular el motor normativo (clasificación Apto / Indeterminado /
  No Apto a partir de la imagen del polígono).
- Objetivo: explorar el espacio 3²⁵ bajo criterio clínico explícito, no
  descubrir reglas nuevas.

---

## 8. Arquitectura del repositorio

SVperitus–IMMUNO-1 vive en un **repositorio hermano** de SVcustos-dataset,
sin modificarlo en ningún punto. El repositorio hermano de referencia es:

> **https://github.com/juantoniolloretegea/SVcustos-dataset**

El propio repositorio de este módulo es
[SVperitus-dataset](https://github.com/juantoniolloretegea/SVperitus-dataset).
Ambos repositorios comparten la gramática algebraica SV y las convenciones
visuales del polígono polar, pero son completamente independientes en código,
datos y motor normativo.

```
SVperitus-dataset/
│
├── common/
│   ├── polygons.py          ← draw_polar_polygon()
│   │                           RADIUS_MAP: {"0":1.0, "1":2.0, "U":3.0}
│   └── io_utils.py          ← load_config(), save/load_vectors_csv()
│
├── IMMUNO-1/
│   ├── config/
│   │   └── imm_n25.yaml     ← PUNTO ÚNICO DE VERDAD
│   │                           n=25, threshold=19, class_to_idx
│   ├── normative_engine.py  ← motor canónico P01–P25
│   │                           evaluate_and_classify(), explain()
│   ├── generate_cases.py    ← generador sintético (invoca al motor)
│   ├── generate_polygons.py ← vectores → imágenes polares
│   ├── train_resnet.py      ← ResNet34 + remapeo canónico
│   └── evaluate.py          ← evaluación con orden canónico YAML
│
├── rust/imm1_normative/     ← Fase 2: port Rust (placeholder)
├── kotlin/                  ← Fase 3: cliente Kotlin (placeholder)
└── docs/
    ├── Documento7_IMMUNO-1.md   ← este documento
    └── Documento8_…             ← Compilador + Célula meta IA
```

Las carpetas `data/`, `models/` y `results/` están excluidas del repositorio
(`.gitignore`). Son regenerables íntegramente ejecutando el pipeline en orden.

---

## 9. Estrategia multilenguaje: Python, Rust y Kotlin

### Fase 1 — Python: implementación de referencia (estado actual)

Motor normativo canónico en `normative_engine.py`. Pipeline completo y
funcional. Python es y seguirá siendo la **fuente de verdad normativa**.
Todo cambio en las reglas P01–P25 se hace aquí primero.

### Fase 2 — Rust: port del motor normativo (planificada)

El crate `rust/imm1_normative/` recibirá un caso clínico en JSON, evaluará
P01–P25 y devolverá el vector ternario y la clase global, garantizando
**equivalencia bit a bit** con Python en el conjunto de casos exportados
con `engine.explain()`.

### Fase 3 — Kotlin: capa de integración cliente (planificada)

Capa de integración para aplicaciones móviles (Android/iOS vía KMP) u
otros front-ends que consuman el motor vía API. **Kotlin no redefine la
lógica P01–P25.**

### Principio de autoridad único

Todo cambio en las reglas normativas sigue obligatoriamente este orden:

1. Actualizar este documento formal.
2. Actualizar `normative_engine.py`.
3. Actualizar `imm_n25.yaml` si aplica.
4. Regenerar el conjunto de paridad.
5. Actualizar los ports Rust/Kotlin para mantener equivalencia.

---

## 10. Líneas futuras de investigación y desarrollo

### 10.1. Revisión clínica adversarial del motor normativo

Revisión sistemática por especialistas (hematólogos, infectólogos,
farmacólogos) mediante casos tipo evaluados con `engine.explain()`:

- Ajuste de umbrales numéricos (ANC, CD4, IgG, corticoides) con referencias
  explícitas por parámetro a guías ECIL/ESCMID/IDSA.
- Análisis de independencia efectiva entre P11, P15 y P25, con posible fusión
  o redefinición en futuras revisiones.
- Refinamiento de la distinción P12/P23 (cicatriz IFD vs. cobertura actual).
- Separación de CD4 y linfocitos totales en P02 como variables independientes,
  cuando la revisión clínica lo justifique.

### 10.2. Extensión a celdas de mayor tamaño (n = 36, 49)

La gramática SVperitus permite escalar sin modificar las invariantes
algebraicas. En IMMUNO-1, un n mayor permitiría añadir comorbilidad
detallada, biomarcadores o contexto organizativo. Requiere completar primero
la validación de IMMUNO-1 n = 25.

### 10.3. Validación externa con datos reales

- Diseño de formulario de captura estructurado a partir de los campos del
  `case` dict definido en `normative_engine.py`.
- Aprobación de comité de ética de investigación clínica.
- Comparación con juicio clínico de expertos independientes (kappa de Cohen).
- Análisis de sesgos del dataset sintético respecto a la distribución real.

### 10.4. Portabilidad a Rust y Kotlin

Véase Sección 9. El objetivo es un motor normativo portable y auditable, con
pruebas de paridad formales que garanticen la equivalencia entre
implementaciones en cualquier entorno.

### 10.5. Integración en la arquitectura SVperitus n = 625

IMMUNO-1 (n = 25) es el primer bloque constitutivo de la célula meta SVperitus
de 625 parámetros: 25 módulos especializados × 25 parámetros por módulo. Cada
módulo futuro añade un bloque con su propio motor normativo, sin modificar los
existentes.

### 10.6. Célula meta de integridad del modelo de IA — SV(9,3)-IA

El Documento 8 describirá una célula meta SV(9,3)-IA con 9 parámetros que
vigilan el ciclo de vida del propio modelo de IA. IMMUNO-1 está diseñado para
ser alojable bajo esta arquitectura de gobernanza. Véase la Sección 11 para
una vista previa.

### 10.7. Vídeo demostrativo

La producción del vídeo demostrativo —que mostrará la transición dinámica de
casos y la lectura clínica del polígono con la convención de la Sección 6.1—
se plantea como una fase posterior, una vez estabilizados el motor normativo
y el repositorio.

---

## 11. Próximo documento: Documento 8

El **Documento 8** cerrará la serie con dos contribuciones:

**Compilador SVcustos + SVperitus:** descripción formal del mecanismo de
composición que permite combinar células SV de dominios distintos (detección
de intrusiones + conocimiento experto clínico) bajo una gramática algebraica
unificada.

**Célula meta SV(9,3)-IA — integridad del modelo de IA:** una célula de
conocimiento con n = 9 (b = 3, T(9) = 7) y 9 parámetros que vigilan el
ciclo de vida del propio sistema de IA:

| Pₖ | Parámetro |
|---|---|
| P1 | Integridad de pesos (hash/firma del modelo) |
| P2 | Procedencia del dataset (trazabilidad y licencia) |
| P3 | Control de accesos (identidades y permisos) |
| P4 | Tests adversariales (robustez frente a entradas hostiles) |
| P5 | Telemetría (monitorización de inferencias en producción) |
| P6 | Aislamiento de entornos (dev / staging / producción) |
| P7 | Logging inalterable (registro inmutable de predicciones) |
| P8 | Supervisión humana (circuitos de revisión activos) |
| P9 | Cadena de suministro software (integridad de dependencias) |

Regla: T(9) = 7.

- n₁ ≥ 7 → **INTRUSIÓN** → confianza en el modelo **anulada**
- n₀ ≥ 7 → **NORMAL** → modelo operable con normalidad
- resto → **INDETERMINADO** → confianza suspendida, solo bajo supervisión reforzada

Esta célula meta es aplicable a cualquier módulo SVperitus, incluido IMMUNO-1,
proporcionando una capa de gobernanza transversal a toda la arquitectura SV.

---

## 12. Referencias

Las guías que fundamentan los umbrales del motor normativo de IMMUNO-1:

- **ECIL** (European Conference on Infections in Leukaemia): guías de
  profilaxis y tratamiento de la infección en pacientes con leucemia y
  neoplasias hematológicas (series actualizadas).
- **ESCMID**: guías de diagnóstico y tratamiento de infecciones fúngicas
  invasoras; guías de vacunación en pacientes inmunodeprimidos.
- **IDSA** (Infectious Diseases Society of America): *Clinical Practice
  Guidelines for Vaccination of the Immunocompromised Host*.
- **ASBMT / EBMT**: guías de profilaxis infecciosa y revacunación post-TPH
  y post-CAR-T.

Las referencias individuales por parámetro (autor, año, tabla o sección
exacta de la guía) se incorporarán en tablas específicas cuando se complete
la anotación necesaria para sustentar la revisión clínica adversarial
descrita en la Sección 10.1.

---

*Documento 7 de la serie «De SVcustos, el marco (framework) de intrusión,
hasta SVperitus: agentes especializados». ISSN 2695-6411.*

*Juan Antonio Lloret Egea | ORCID 0000-0002-6634-3351 | CC BY-NC-ND 4.0*
