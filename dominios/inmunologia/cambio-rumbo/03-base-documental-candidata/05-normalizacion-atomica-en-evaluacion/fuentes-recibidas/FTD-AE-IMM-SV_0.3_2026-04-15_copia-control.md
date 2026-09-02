# FTD-AE-IMM-SV/0.3
## Ficha Técnica de Diseño del **Agente Especializado en Inmunología del Sistema Vectorial SV**

**Autor:** Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351  **Sello editorial:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | **Publicación:** IA eñ™ — La Biblia de la IA™ | **ISSN:** 2695-6411 | **Licencia:** CC BY-NC-ND 4.0 | **Lugar y fecha:** Madrid, 15/04/2026

---

## 0. Estatuto, rango y dictamen

**Naturaleza:** documento interno de diseño, subordinado al estrato documental soberano de agentes especializados del Sistema Vectorial SV.

**Rango:** pre-ITI específica. Ficha de diseño orientada a fijar el estado correcto del agente antes de la ITI propia, del cierre laboratorial y de la eventual publicación específica.

**Nombre canónico del agente:** **Agente Especializado en Inmunología del Sistema Vectorial SV**.

**Acrónimo técnico interno:** **AE-IMM-SV**.

**Lenguaje de referencia inicial del nuevo panel:** HTML/JavaScript en shell web estática local, destinada a orquestar el panel experto–agente y a consumir de forma visible los motores normativos ya existentes.

**Base normativa y técnica ya materializada:**
- motor normativo Python en `agentes/inmunologia/fase_1/src/normative_engine.py` y `agentes/inmunologia/fase_2/src/normative_engine.py`;
- configuración YAML en `imm_n25.yaml` e `imm2_n25.yaml`;
- superficies de uso ya materializadas: `aplicaciones/demo_web/index.html` y `aplicaciones/demo_wasm/index.html` para `IMMUNO-1`, `aplicaciones/cliente_kotlin/index.html` como integración mínima real Kotlin → Rust/WASM para `IMMUNO-1`, y `aplicaciones/demo_wasm/compositor.html` como composición visible `IMMUNO-1 → IMMUNO-2`;
- línea Rust/WASM ya materializada parcialmente y cliente Kotlin mínimo real ya publicado.

**Régimen operativo inicial del nuevo panel:** local, sin backend remoto, shell web estática autocontenida, sin dependencia de red para el flujo canónico, centrada en evaluación ternaria interactiva, consejo del agente y trazabilidad soberana.

**Estado del diseño:** apto para inicio del **Hito 1 del panel experto–agente**; no apto todavía para declarar implementación cerrada del agente ni publicación externa.

**Custodia basal:** **bajo custodia basal suficiente**, conforme a `especificaciones/patron_agente_especializado/README.md` y `especificaciones/custodia_basal_del_diseno/README.md`.

### Dictamen

La presente ficha fija el perfil de diseño del AE-IMM-SV de forma compatible con:

- el **Estatuto del universo de sucesos, admisibilidad suficiente y composición tipada de agentes especializados en el Sistema Vectorial SV**;
- **Fundamentos, exigencias y arquitectura general de los agentes especializados en el Sistema Vectorial SV: formulación transversal desde el caso director del Agente Especializado en Inmunología**;
- la **Instrucción Técnica de Implementación Específica de Agente Especializado en el Sistema Vectorial SV (ITI V.1)**;
- la **Carta Magna de autogobierno de agentes especializados en el SV (V.1)**;
- el **Documento 7** del ámbito inmunológico, correspondiente al estado históricamente publicado como `IMMUNO-1`;
- el **Documento 8 — Compilador doctrinal y célula meta SV(9,3)-IA**, en su estatuto correcto de documento de cierre de la serie y no como simple puntero local a `IMMUNO-2` o al compositor;
- la sede canónica actual del agente en `agentes/inmunologia/`;
- y la custodia estructural del diseño ya asentada en el ecosistema SV.

No define el suceso, no sustituye a la ITI, no gobierna dinámicamente el agente y no autoriza cierre operativo. Su función exacta es fijar, en términos ortodoxos SV, el diseño del agente antes de su ITI específica, antes del laboratorio cerrado del nuevo panel y antes de su eventual publicación.

---

## I. Justificación constitutiva

La necesidad que da lugar al agente no es utilitaria ni secundaria. El ámbito inmunológico comparece en `SVperitus` como **caso director canónico** del agente especializado y ha empujado materialmente la arquitectura por fases, la tipificación de dominio, la composición serie y el problema real del acoplamiento entre evaluación formal y asistencia experta.

Las necesidades concretas que justifican formalmente el agente son:

1. la evaluación estructurada de 25 parámetros clínicos en dos dominios inmunológicos relacionados, `IMMUNO-1` e `IMMUNO-2`, bajo la regla `T(25)=19`;
2. la visualización continua del estado de la célula como polígono SV legible por el experto humano;
3. la interacción visible entre experto y agente mediante una célula NLP real, con transductor explícito, horizonte declarado y preservación de `U` legítima;
4. el registro trazable de juicios y ajustes soberanos del experto;
5. la coordinación entre Fase I y Fase II mediante el parámetro puente `P25` de `IMMUNO-2`;
6. la articulación posterior con la célula meta `SV(9,3)-IA` en el plano correcto del Documento 8;
7. y la necesidad de distinguir con limpieza entre lo ya materializado en demos, motores y compositor, y lo que todavía no existe: el **panel experto–agente** plenamente gobernado por célula NLP, consejo del agente y banco de sucesos soberano.

Este dominio excede el estatuto de script auxiliar, demo aislada o formulario electrónico y justifica formalización propia como agente especializado del SV.

---

## II. Objeto del agente

El AE-IMM-SV tiene por objeto **evaluar, asesorar estructuralmente, coordinar fases y registrar** el estado inmunológico de pacientes adultos bajo inmunosupresión farmacológica, en dos dominios de riesgo infeccioso, mediante células ternarias `SV(25,5)` con parámetros clínicamente justificados, polígono visible como referencia continua del experto, célula NLP de acoplamiento conversacional y banco de sucesos `append-only`.

El agente no emite diagnóstico clínico soberano, no sustituye al experto humano en la valoración semántica del caso y no introduce tiempo soberano, estadística, inferencia opaca ni heurística no declarada.

---

## III. Delimitación positiva

En el **Hito 1 del panel experto–agente**, el agente puede ocuparse de:

1. presentación interactiva de los 25 parámetros de `IMMUNO-1` y `IMMUNO-2` con sus reglas `0/1/U` explícitas;
2. consumo visible del motor normativo ya existente de Fase I y Fase II;
3. visualización del polígono `SV(25,5)` como referencia continua del experto;
4. dictamen global con regla `T(25)=19`: `APTO` (`n0 ≥ 19`), `NO_APTO` (`n1 ≥ 19`), `INDETERMINADO` (resto);
5. célula NLP de 9 posiciones con transductor explícito, horizonte declarado y polígono propio visible;
6. panel de consejo del agente con lectura estructural del estado de la célula;
7. banco de sucesos con registro del tipo `registrar_override_humano_informado`;
8. coordinación entre Fase I y Fase II mediante lectura disciplinada del parámetro puente `P25`;
9. diagrama de flujo con nodo principal y subprocedimientos etiquetados;
10. laboratorio reproducible mínimo del nuevo panel.

---

## IV. Delimitación negativa obligatoria

En su estado actual y en el Hito 1 del panel, el agente:

- no emite diagnóstico clínico ni terapéutico soberano;
- no asigna verdad semántica al caso por sí solo;
- no sustituye al experto humano en la clausura de `U` legítima;
- no usa backend remoto en el régimen canónico;
- no depende de Internet durante el flujo local correcto;
- no aprende de corpus ni recalibra parámetros por retroalimentación implícita;
- no estima probabilidades ni calcula frecuencias estadísticas;
- no introduce tiempo soberano, inferencia opaca, heurística no declarada, minería de datos ni bayesianismo;
- no convierte el lenguaje natural del experto en orden ejecutiva directa;
- no reescribe el estado histórico del repositorio ni presenta como inexistentes las superficies ya materializadas;
- no confunde subpuertas editoriales del agente y de sus fases con el futuro panel operativo experto–agente;
- y no permite que `P25` de `IMMUNO-2` se fije sin dictamen previo válido de `IMMUNO-1`.

---

## V. Arquitectura celular del agente

### V.1. Célula de Fase I — IMMUNO-1

```text
C_imm1^25     b = 5, n = b² = 25, T(25) = 19
```

**Dominio:** profilaxis infecciosa y vacunación en adultos con neoplasias hematológicas e inmunosupresión.

**Capas:**
- Capa 1: estado inmunitario basal (`P01–P05`)
- Capa 2: neoplasia de base y tratamiento inmunosupresor (`P06–P10`)
- Capa 3: historia infecciosa y colonización (`P11–P15`)
- Capa 4: estado vacunal (`P16–P20`)
- Capa 5: profilaxis y seguimiento (`P21–P25`)

**Semántica ternaria de trabajo:**
- `0` → situación adecuada / aceptable según regla explícita;
- `1` → situación de riesgo alto o claramente inadecuada;
- `U` → información insuficiente, no verificable o zona gris.

### V.2. Célula de Fase II — IMMUNO-2

```text
C_imm2^25     b = 5, n = b² = 25, T(25) = 19
```

**Dominio:** estratificación del riesgo de infección grave en adultos con inmunosupresión farmacológica sistémica no trasplante.

**Población diana declarada:** adultos (≥18 años) en tratamiento activo o reciente (≤6 meses). Exclusiones: TOS, TPH/CAR-T, quimioterapia citotóxica pura, VIH primario.

**Capas:**
- Capa 1: terreno basal del huésped (`P01–P05`)
- Capa 2: carga y tipo de inmunosupresión (`P06–P10`)
- Capa 3: barreras, dispositivos y anatomía crítica (`P11–P15`)
- Capa 4: exposición epidemiológica documentable (`P16–P20`)
- Capa 5: protección residual, historia infecciosa y puente con `IMMUNO-1` (`P21–P25`)

**Semántica ternaria de trabajo:**
- `0` → riesgo aceptable / situación favorable;
- `1` → riesgo elevado / situación desfavorable;
- `U` → no valorable / información insuficiente.

**Parámetro puente `P25`:** recibe la clase global de `IMMUNO-1` inyectada por el compositor. Principio: integración sin duplicación.

### V.3. Célula NLP del agente

```text
C_nlp^9     b = 3, n = b² = 9
```

La célula NLP del AE-IMM-SV sigue la arquitectura de nueve posiciones conversacionales ya asentada en el ámbito NLP del SV. Sus posiciones cubren:

- `P1`: coherencia temática del frame conversacional (`θ`)
- `P2`: estado de la pregunta activa del experto (`π`)
- `P3`: curvatura/coherencia del frame (`κ`)
- `P4`: completitud de la información aportada (`η`)
- `P5`: alineación del input con el dominio (`γ`)
- `P6`: apropiabilidad del acto comunicativo (`α`)
- `P7`: estado del referente conversacional (`μ`)
- `P8`: solicitud explícita de acción (`χ`)
- `P9`: continuidad del proceso en curso (`ψ`)

El transductor `ℐ_NLP` mapea observables declarados a `{0,1,U}` con reglas explícitas. El horizonte `ℋ_NLP` declara los sucesos que pueden cerrar cada posición abierta. El polígono NLP de 9 vértices es referencia visual continua del estado conversacional.

**Regla de prudencia:** esta célula NLP se declara aquí como **exigencia de diseño del Hito 1**, no como componente ya consolidado del ecosistema inmunológico. Su puente serio con inmunología sigue siendo trabajo de implementación y verificación.

### V.4. Célula supervisora de gobernabilidad (proyectada)

La célula supervisora de gobernabilidad queda **proyectada**, pero **sin fórmula canónica cerrada todavía en esta ficha**.

Su función prevista para la ITI específica es vigilar, posición por posición, la suficiencia de los parámetros críticos, la preservación de `U` legítima y la posibilidad material de cierre bajo horizonte declarado. No duplica la célula de dominio; supervisa su gobernabilidad.

**Regla de prudencia:** mientras no exista formulación canónica materialmente asentada en el ecosistema inmunológico, esta ficha no introduce una notación algebraica nueva para dicha célula.

### V.5. Custodia estructural obligatoria

El agente queda subordinado a la custodia estructural asentada en la célula especializada de seguridad estructural:

```text
S_suelo    = ⊗_gate,T_suelo(C_obj^9, C_base^9)
A_custodia = ⊗_gate,T_cust(C_diseno^36, S_suelo)
```

Ningún cierre del AE-IMM-SV puede declararse apto sin dictamen de custodia estructural suficiente.

---

## VI. Parámetros críticos del agente — Fase I (IMMUNO-1)

Los 25 parámetros de `C_imm1^25`, leídos en alfabeto `{0,1,U}`, conservan la estructura ya materializada en el repositorio.

**Nota de fuente:** la tabla que sigue tiene función de síntesis de diseño. No sustituye ni al `normative_engine.py` ni a la configuración YAML ni a la documentación canónica de fase.

### Capa 1 — Estado inmunitario basal

| ID | Nombre | 0 | 1 | U |
|----|--------|---|---|---|
| P01 | Neutropenia | RAN adecuado / neutropenia ausente o leve transitoria | Neutropenia severa prolongada | Recuento no disponible o duración incierta |
| P02 | Linfopenia | Recuentos adecuados | Depleción severa | No valorado / zona gris |
| P03 | Inmunoglobulinas | IgG adecuada | IgG muy baja | Zona intermedia o no determinada |
| P04 | Esplenectomía / hipoesplenismo | Bazo funcionante | Asplenia o hipoesplenismo confirmado | Función esplénica no evaluada |
| P05 | Barreras y catéteres | Barreras íntegras | Mucositis activa o catéter de riesgo | No explorado |

### Capa 2 — Neoplasia de base y tratamiento inmunosupresor

| ID | Nombre | 0 | 1 | U |
|----|--------|---|---|---|
| P06 | Tipo y fase de la hemopatía | Remisión consolidada / bajo riesgo | Inducción, recaída o alto riesgo | Fase no clarificada |
| P07 | Intensidad de quimioterapia | Baja mielosupresión / mantenimiento | Alta mielosupresión | Régimen no documentado |
| P08 | Agentes biológicos | Sin biológico inmunosupresor activo | Agente de alto riesgo activo | Agente no identificado |
| P09 | TPH / CAR-T | Sin TPH ni CAR-T | TPH/CAR-T en curso o postrasplante precoz | Estado no evaluado |
| P10 | Corticoides sistémicos | Sin dosis relevante | Dosis/ duración de alto riesgo | Dosis no documentada |

### Capa 3 — Historia infecciosa y colonización

| ID | Nombre | 0 | 1 | U |
|----|--------|---|---|---|
| P11 | Infecciones bacterianas graves previas | Sin evento grave reciente | ≥1 evento grave reciente | Historial no disponible |
| P12 | Infecciones fúngicas invasoras | Sin IFI previa o activa | IFI previa o activa | No evaluado |
| P13 | Infecciones virales crónicas/latentes | Sin reactivación relevante | Reactivación con impacto de manejo | Estado no clarificado |
| P14 | Colonización por MDR | Sin MDR documentado | MDR documentado | Sin cribado suficiente |
| P15 | Exposición sanitaria reciente | Sin exposición relevante | Hospitalización o procedimiento reciente | No evaluado |

### Capa 4 — Estado vacunal

| ID | Nombre | 0 | 1 | U |
|----|--------|---|---|---|
| P16 | Vacunación antigripal | Actualizada | Ausente o desactualizada | Estado desconocido |
| P17 | Vacunación antineumocócica | Secuencia adecuada | Pauta incompleta | No verificable |
| P18 | Vacunación frente a SARS-CoV-2 | Actualizada según guía | Ausente o desactualizada | Estado desconocido |
| P19 | Vacunación frente a hepatitis B | Protección documentada | Sin cobertura adecuada | Serología no disponible |
| P20 | Otras vacunas inactivadas | Indicadas al día | ≥1 vacuna indicada ausente | Estado no evaluado |

### Capa 5 — Profilaxis y seguimiento

| ID | Nombre | 0 | 1 | U |
|----|--------|---|---|---|
| P21 | Profilaxis frente a PJP | Adecuada y activa | Sin profilaxis con indicación | Indicación no evaluada |
| P22 | Profilaxis antiviral | Adecuada según indicación | Ausente con indicación | Indicación no evaluada |
| P23 | Profilaxis antifúngica | Adecuada según riesgo | Ausente con indicación | Riesgo no evaluado |
| P24 | Profilaxis antibacteriana | Adecuada en neutropenia de alto riesgo | Ausente con indicación | Riesgo no evaluado |
| P25 | Plan de reevaluación | Documentado y vigente | Ausente o desactualizado | No documentado |

---

## VII. Parámetros críticos del agente — Fase II (IMMUNO-2)

Los 25 parámetros de `C_imm2^25` conservan la estructura ya fijada en `IMMUNO2_P01-P25_spec.md`.

**Nota de fuente:** la tabla que sigue resume el diseño de fase. La fuente de detalle sigue siendo `IMMUNO2_P01-P25_spec.md`, junto con `imm2_n25.yaml` y el motor normativo correspondiente.

### Capa 1 — Terreno basal del huésped

| ID | Nombre | 0 | 1 | U |
|----|--------|---|---|---|
| P01 | Edad | Rango basal favorable | Edad de riesgo elevado | No verificable |
| P02 | Comorbilidad cardiometabólica y renal | Sin carga relevante | Carga relevante | No evaluada |
| P03 | Enfermedad pulmonar crónica | Sin neumopatía estructural | Neumopatía relevante | No evaluable |
| P04 | Hepatopatía crónica | Sin hepatopatía relevante | Fibrosis/cirrosis o viremia activa | No disponible |
| P05 | Estado nutricional y fragilidad | Adecuado | Fragilidad o desnutrición relevante | No evaluado |

### Capa 2 — Carga y tipo de inmunosupresión

| ID | Nombre | 0 | 1 | U |
|----|--------|---|---|---|
| P06 | Tipo de fármaco IS principal | Bajo/medio riesgo | Alto riesgo | No clasificable |
| P07 | Combinación de inmunosupresores | Monoterapia o combinación estándar | Combinación mayor de riesgo | No documentada |
| P08 | Dosis equivalente de corticoides | Sin dosis relevante | Dosis de riesgo | No documentada |
| P09 | Duración acumulada de IS | Inicio o estabilidad favorable | Historial desfavorable | Incompleto |
| P10 | Linfopenia relevante | Recuento favorable | Recuento de riesgo | No disponible |

### Capa 3 — Barreras, dispositivos y anatomía crítica

| ID | Nombre | 0 | 1 | U |
|----|--------|---|---|---|
| P11 | Integridad de piel y mucosas | Íntegras | Lesión / mucositis | No explorado |
| P12 | Catéteres venosos centrales | Ausentes | Presentes | No verificable |
| P13 | Prótesis y biomateriales | Sin riesgo relevante | Riesgo relevante | No documentado |
| P14 | Cirugía mayor reciente | Ausente | Presente | Historial no disponible |
| P15 | Esplenectomía o hipoesplenismo | Bazo presente | Asplenia / hipoesplenismo | No evaluado |

### Capa 4 — Exposición epidemiológica documentable

| ID | Nombre | 0 | 1 | U |
|----|--------|---|---|---|
| P16 | Hospitalización reciente | Ausente | Presente | No verificable |
| P17 | Colonización por MDR | Ausente | Presente | Sin cribado suficiente |
| P18 | Zona endémica de tuberculosis | Exposición basal baja | Exposición de alto riesgo | No evaluada |
| P19 | Exposición respiratoria de alto riesgo | Ausente | Presente | No evaluada |
| P20 | Exposición a entornos de alto riesgo fúngico | Ausente | Presente | No evaluada |

### Capa 5 — Protección residual, historia infecciosa y puente IMMUNO-1

| ID | Nombre | 0 | 1 | U |
|----|--------|---|---|---|
| P21 | Historia de infecciones graves recientes | Ausente | Presente | No disponible |
| P22 | Inmunoglobulinas séricas (IgG) | Adecuadas | Muy bajas | Intermedia / no determinada |
| P23 | Intensificación reciente del régimen IS | Ausente | Presente | No documentada |
| P24 | Evaluación integral de riesgo infeccioso | Documentada y vigente | Ausente o con vacíos | No verificable |
| P25 | Parámetro puente con IMMUNO-1 | `IMMUNO-1` apto y vigente | `IMMUNO-1` no apto o ausente/desactualizado | `IMMUNO-1` no aplicado o inaccesible |

---

## VIII. Universo de sucesos del agente

El universo de sucesos del AE-IMM-SV queda **provisionalmente cerrado para el Hito 1 del panel experto–agente**. El agente sólo puede generar, evaluar y resolver sucesos que recaigan sobre su dominio inmunológico y sobre la interacción custodial del nuevo panel.

### Sucesos operables iniciales

```text
evaluar_celula_imm1
 evaluar_celula_imm2
 consultar_estado_celula
 registrar_override_humano_informado
 rechazar_entrada_inadmisible
 exportar_resultado_tipado
 reevaluar_posicion
 coordinar_fases_via_p25
```

### Familias de suceso

**Suceso de evaluación:** recae sobre un parámetro o conjunto de parámetros de la célula activa.

**Suceso exógeno:** entra desde lenguaje natural, formulario o anotación libre, pero sólo tras tipado y traducción visible por la célula NLP.

**Suceso de coordinación:** conecta el dictamen de una fase con la entrada de otra (`P25`).

**Suceso soberano:** familia exclusiva del experto humano; `append-only`, irreversible y con justificación registrada.

---

## IX. Arquitectura de planos

El agente mantiene tres planos estrictamente separados.

### Plano interno

Aquí viven:
- los motores normativos Python de Fase I y Fase II;
- los YAML de configuración `imm_n25.yaml` e `imm2_n25.yaml`;
- las reglas `0/1/U` por posición;
- la célula NLP con su transductor y horizonte;
- el banco de sucesos `append-only`;
- el polígono `SV(25,5)` como proyección del estado de la célula;
- y el dictamen global con `T(25)=19`.

### Plano externo

Aquí viven:
- el lenguaje natural del experto;
- las anotaciones libres del usuario;
- los formularios de entrada con valores textuales sin tipar;
- y las fuentes externas de datos clínicos todavía no traducidas al alfabeto `{0,1,U}`.

### Plano de acoplamiento custodial

Aquí viven:
- la célula NLP (`ℐ_NLP + ℋ_NLP`);
- la traducción de observables a valores ternarios mediante reglas visibles;
- el control de ascenso y preservación de `U` legítima;
- el rechazo de entradas no tipables;
- y la autorización soberana del experto antes de cualquier cierre.

---

## X. Subpuertas ya existentes y panel operativo pendiente

### X.1. Subpuertas canónicas ya materializadas

La sede actual del agente y de sus fases ya contiene **subpuertas editoriales** en:

- `agentes/inmunologia/index.html`
- `agentes/inmunologia/fase_1/index.html`
- `agentes/inmunologia/fase_2/index.html`

Su función correcta es ayudar a la lectura humana del agente, sus fases y sus elementos vivos. **No constituyen todavía el panel experto–agente que esta ficha diseña.**

### X.2. Superficies de uso ya vivas del ecosistema inmunológico

El repositorio ya contiene superficies reales de uso, entre ellas:

- `aplicaciones/demo_web/index.html`  → demo interactiva IMMUNO-1
- `aplicaciones/demo_wasm/index.html` → demo Rust/WASM IMMUNO-1
- `aplicaciones/demo_wasm/compositor.html` → composición serie IMMUNO-1 → IMMUNO-2
- `aplicaciones/cliente_kotlin/index.html` → integración mínima real Kotlin → Rust/WASM

Estas superficies deben reconocerse como **trabajo material ya existente**. El nuevo panel no parte de cero; parte de ellas, pero con una finalidad distinta: integrar consejo, célula NLP, banco de sucesos soberano y flujo experto–agente.

### X.3. Panel operativo pendiente

Lo pendiente del Hito 1 no es una “primera página web” del ámbito inmunológico, sino el **panel experto–agente** con los siguientes elementos integrados:

1. panel principal operativo;
2. panel de consejo soberano del agente;
3. célula NLP activa y visible;
4. banco de sucesos `append-only`;
5. registro y confirmación de overrides soberanos;
6. y flujo principal con subprocedimientos etiquetados.

---

## XI. Arquitectura mínima de resolución del nuevo panel

El nuevo panel debe nacer con esta arquitectura mínima:

1. **Panel principal:** entrada de parámetros, selección de fase (`IMMUNO-1 / IMMUNO-2`), polígono SV visible, dictamen global, banco de sucesos y acceso a consejo.

2. **Panel de consejo:** estado de la célula activa (`n0`, `n1`, `nU`, dictamen), detalle por parámetro, justificación visible, célula NLP visible, análisis estructural y registro de ajuste soberano.

3. **Célula NLP activa:** posiciones `P1–P9`, polígono visible, transductor explícito, horizonte declarado y verificación de gobernabilidad.

4. **Motor normativo:** evaluación determinista local, sin llamadas de red, aplicando `T(25)=19` sobre el vector de 25 posiciones.

5. **Banco de sucesos `append-only`:** registro de operaciones del agente y de ajustes soberanos del experto.

---

## XII. Cadena de entrada del agente

### XII.1. Objeto de entrada canónico

```json
{
  "fase_activa": "IMMUNO-1 | IMMUNO-2",
  "parametros": {
    "P01": "0 | 1 | U",
    "P02": "0 | 1 | U",
    "...": "...",
    "P25": "0 | 1 | U"
  },
  "nota_libre_experto": "",
  "override_soberano": null
}
```

### XII.2. Traducción custodial

```text
NotaLibreExperto  → CelulaNLP (ℐ_NLP) → ObservablesDeclarados → ValoresTerminales
ParametrosFormulario → ValidacionTernaria → CeldaActiva
CeldaActiva → MotorNormativo → Dictamen
Dictamen   → BancoDeSucesos (append-only)
```

### XII.3. Principio operativo

El lenguaje natural del experto no constituye orden ejecutiva directa. Es fuente externa de intención que debe ser traducida por la célula NLP, expuesta y confirmada antes de cualquier modificación de la célula de dominio.

---

## XIII. Diagrama de flujo central del nuevo panel

```text
initApp()
  ↓
[Selección de fase: IMMUNO-1 / IMMUNO-2]
  ↓
subprocedimiento_carga_parametros
  → formulario P01–P25 con reglas explícitas por posición
  → valores iniciales: U en todas las posiciones
  ↓
subprocedimiento_nlp_entrada_libre
  → nota libre del experto → ℐ_NLP → observables declarados
  → polígono NLP actualizado
  → ℋ_NLP: posiciones abiertas y sucesos de cierre
  ↓
subprocedimiento_evaluacion_celula
  → motor normativo: aplicar T(25)=19
  → dictamen: APTO / NO_APTO / INDETERMINADO
  → conteos n0, n1, nU
  → polígono SV(25,5) actualizado
  ↓
[Dictamen emitido]
  → banco de sucesos: append evaluar_celula_immX
  → consejo del agente activado
  ↓
subprocedimiento_consejo_agente
  → estado estructural de la célula
  → posiciones críticas y U legítimas
  → análisis visible del agente
  ↓
[¿Ajuste soberano del experto?]
  Sí → subprocedimiento_override_soberano
       → confirmación visible del cambio
       → banco de sucesos: append registrar_override_humano_informado
       → reevaluación
  No → estado consolidado
  ↓
[¿Coordinar con fase complementaria?]
  Sí → subprocedimiento_coordinacion_p25
       → dictamen IMMUNO-1 → P25 de IMMUNO-2
  ↓
[Exportación opcional]
  → exportar_resultado_tipado
  → JSON: {fase, vector, dictamen, banco_sucesos}
```

**Subprocedimientos etiquetados:**
- `subprocedimiento_carga_parametros`
- `subprocedimiento_nlp_entrada_libre`
- `subprocedimiento_evaluacion_celula`
- `subprocedimiento_consejo_agente`
- `subprocedimiento_override_soberano`
- `subprocedimiento_coordinacion_p25`

---

## XIV. Exigencias de diseño

El diseño del nuevo panel debe satisfacer desde su primera versión:

- determinismo estructural: misma entrada, mismo dictamen;
- visibilidad del criterio de corrección: reglas `0/1/U` legibles por el experto;
- trazabilidad: entrada, evaluación y banco de sucesos auditables;
- célula NLP real: transductor con reglas explícitas, no tipado por palabras clave fijas;
- polígono como referencia continua del experto;
- preservación de `U` legítima;
- autoridad soberana del experto en la clausura de cambios;
- separación de planos: el lenguaje natural no actúa como orden ejecutiva directa;
- no contaminación semántica: el agente no emite juicio clínico soberano;
- subprocedimientos etiquetados y diagrama de flujo legible;
- y compatibilidad honesta con las superficies ya materializadas del ecosistema, sin borrarlas ni duplicarlas ficticiamente.

---

## XV. Banco de sucesos

### XV.1. Estructura de cada entrada

```json
{
  "run_id": "uuid",
  "timestamp": "ISO8601",
  "tipo_suceso": "evaluar_celula_imm1 | registrar_override_humano_informado | ...",
  "fase": "IMMUNO-1 | IMMUNO-2",
  "vector_antes": [...],
  "vector_despues": [...],
  "dictamen": "APTO | NO_APTO | INDETERMINADO",
  "n0": 0,
  "n1": 0,
  "nU": 0,
  "justificacion_experto": "",
  "agente_version": "AE-IMM-SV/0.3"
}
```

### XV.2. Régimen

- escritura `append-only`;
- sin corrección retroactiva;
- sin hash obligatorio en esta versión, previsto para iteraciones posteriores;
- referencia obligatoria a fase del agente y versión de la ficha.

---

## XVI. Frontera normativa específica del agente

**FGSV-AE-IMM/001**

La frontera normativa del agente debe impedir:

- que el lenguaje natural del experto actúe como orden ejecutiva directa sobre un parámetro;
- que la célula NLP cierre `U` por inferencia sin autorización soberana explícita;
- que el motor normativo sea sustituido por estimación estadística, probabilidad o heurística opaca;
- que el agente asigne verdad semántica al caso clínico;
- que se introduzcan tiempo soberano, estadística, inferencia opaca, minería de datos o bayesianismo por vía lateral;
- que el parámetro puente `P25` sea calculado sin haber ejecutado previamente `IMMUNO-1` o sin verificar la vigencia exigida;
- y que una subpuerta editorial o demo previa se haga pasar por el nuevo panel experto–agente sin declarar la diferencia de estatuto.

---

## XVII. Catálogo preliminar de errores

### Célula de dominio

- `IMM-CEL-001` Vector incompleto: ≥1 posición sin valor declarado
- `IMM-CEL-002` Valor fuera de alfabeto: posición con valor distinto de `{0,1,U}`
- `IMM-CEL-003` Fase no seleccionada antes de evaluación

### Célula NLP

- `IMM-NLP-001` Transductor sin regla aplicable para observable declarado
- `IMM-NLP-002` `U` irreducible detectada por verificación de gobernabilidad
- `IMM-NLP-003` Cierre de `U` sin autorización soberana del experto

### Coordinación de fases

- `IMM-COORD-001` `P25` de `IMMUNO-2` fijado sin dictamen previo de `IMMUNO-1`
- `IMM-COORD-002` Dictamen de `IMMUNO-1` desactualizado usado en `P25`

### Banco de sucesos

- `IMM-BANCO-001` Suceso no registrado tras operación relevante
- `IMM-BANCO-002` Intento de modificación retroactiva del banco

### Frontera

- `IMM-FR-001` Entrada natural sin traducción por célula NLP
- `IMM-FR-002` Juicio clínico emitido por el agente sin experto
- `IMM-FR-003` Cierre de `U` por inferencia interna no declarada

---

## XVIII. Paquete técnico mínimo del nuevo panel

El nuevo panel debe nacer en un paquete autocontenido con:

- shell web estática (`index.html`, `consejo.html`, `app.js`, `style.css`);
- consumo visible de los motores normativos ya existentes;
- uso de los YAML ya existentes como base de reglas estructurales;
- sin llamadas de red en el flujo canónico;
- sin escritura persistente de lado servidor;
- y con `localStorage` del navegador como banco de sesión inicial.

**Nota de corrección factual:** esta exigencia no niega las demos ya existentes. Diseña una capa nueva y distinta sobre ellas.

---

## XIX. Laboratorio mínimo exigible del nuevo panel

No procede redactar la ITI específica del nuevo panel ni publicar la nueva capa interactiva sin haber superado antes un laboratorio mínimo.

### Casos mínimos

- `C1` evaluación `IMMUNO-1` caso `APTO`: vector íntegro favorable
- `C2` evaluación `IMMUNO-1` caso `NO_APTO`: `n1 ≥ 19`
- `C3` evaluación `IMMUNO-1` caso `INDETERMINADO`: `n0 < 19`, `n1 < 19`, `nU > 0`
- `C4` célula NLP: entrada libre del experto → observables declarados → polígono NLP
- `C5` override soberano: experto modifica `P07` de `U` a `1` → banco registra suceso
- `C6` coordinación `P25`: dictamen `IMMUNO-1 = APTO` → `P25` de `IMMUNO-2 = 0`
- `C7` rechazo de entrada no tipable: valor como “probablemente” → no se acepta
- `C8` preservación de `U`: `U` legítima no se cierra sin autorización del experto
- `C9` exportación: JSON con vector, dictamen y banco de sucesos
- `C10` ejecución íntegra offline del nuevo panel

### Evidencias mínimas

- pseudocódigo de cada subprocedimiento;
- implementación HTML/JS ejecutable;
- JSON de salida por caso;
- estado de polígono por caso;
- y banco de sucesos de prueba.

---

## XX. Condición de paso a la ITI específica del nuevo panel AE-IMM-SV

Sólo podrá abrirse la ITI específica del nuevo panel cuando existan materialmente:

- panel principal y panel de consejo operativos;
- integración visible con los motores normativos de ambas fases;
- célula NLP con transductor y horizonte funcionando;
- banco de sucesos `append-only` funcionando;
- laboratorio mínimo reproducible superado;
- coordinación `P25` verificada;
- y dictamen de custodia estructural sin contaminación semántica.

---

## XXI. Estado material correcto al cierre de esta ficha

### XXI.1. Hecho materialmente en el repositorio

```text
✅ Sede canónica del agente en agentes/inmunologia/
✅ Fase I e IMMUNO-1 materializados como fase del agente
✅ Fase II e IMMUNO-2 materializados como fase del agente
✅ Compositor adscrito a Fase II
✅ YAML de configuración imm_n25.yaml e imm2_n25.yaml
✅ Motores normativos Python de Fase I y Fase II
✅ Especificación P01–P25 de IMMUNO-2
✅ Subpuertas editoriales del agente y de sus fases
✅ Demo web IMMUNO-1
✅ Demo Rust/WASM IMMUNO-1
✅ Compositor visible IMMUNO-1 → IMMUNO-2
✅ Integración mínima real Kotlin → Rust/WASM
✅ Ficha de diseño del nuevo panel (este documento)
```

### XXI.2. Pendiente específico del Hito 1 de Agente-Inmunología1

```text
❌ Panel experto–agente unificado del nuevo ámbito
❌ Panel de consejo soberano integrado
❌ Célula NLP real integrada al flujo inmunológico
❌ Banco de sucesos append-only operativo en el nuevo panel
❌ Registro visible de override soberano con reevaluación inmediata
❌ Laboratorio mínimo específico del nuevo panel
```

### XXI.3. Errores / solucionado / ambiguo

```text
Errores:
  (vacío en esta ficha de diseño)

Solucionado:
  - rectificación del estatuto de Documento 8
  - rectificación del estado real del repositorio
  - separación entre subpuertas editoriales y panel operativo pendiente
  - reconocimiento explícito de la línea Rust/WASM y del cliente Kotlin ya materializados
  - retirada de notación de gobernabilidad no suficientemente anclada
  - explicitación de que las tablas P01–P25 son síntesis de diseño y no nueva fuente de verdad normativa

Ambiguo:
  - alcance exacto del primer cierre laboratoral de la célula NLP una vez injertada en inmunología
  - forma final de convivencia entre la nueva capa JS del panel y las superficies históricas ya vivas
```

---

## XXII. Dictamen final de la ficha

**APTA PARA INICIO DEL HITO 1 DEL PANEL EXPERTO–AGENTE**  
**NO APTA TODAVÍA PARA DECLARAR IMPLEMENTACIÓN CERRADA DEL AGENTE**  
**NO APTA TODAVÍA PARA PUBLICACIÓN EXTERNA**  
**BAJO CUSTODIA BASAL SUFICIENTE**

La ficha técnica de diseño del AE-IMM-SV queda establecida en su versión `0.3` con:

- arquitectura celular explícita para ambas fases;
- parámetros `P01–P25` conservados y alineados con la sede material del repositorio;
- célula NLP declarada correctamente como exigencia de diseño del Hito 1;
- universo de sucesos provisionalmente cerrado para el panel;
- distinción expresa entre trabajo ya materializado y trabajo todavía pendiente;
- diagrama de flujo central con subprocedimientos etiquetados;
- catálogo preliminar de errores;
- y dictamen honesto sobre el punto real del agente.

Procede iniciar la implementación del panel en **Agente-Inmunología1**.

---

## XXIII. Cierre de Hito 1 — Apertura de Hito 2

**Fecha de cierre de Hito 1:** 15/04/2026 — Agente-Inmunología1

### Resultado de la revisión adversarial previa al cierre

```text
Errores en la FTD:
  [XV.2] Referencia residual "v0.2" corregida a "esta versión". Único
  cambio aplicado en esta versión consolidada.

Hallazgos de repo (no bloquean Hito 1):
  [normative_engine.py fase_1] ISSN "2695-641X" en lugar de "2695-6411".
  Typo pre-existente en el fichero del motor. Deuda viva del repo.
  → Etiqueta: deuda_issn_normative_engine_fase1

Verificaciones superadas:
  ✅ 14/14 rutas del repositorio presentes
  ✅ T(25) = floor(7·25/9) = 19 — correcto
  ✅ 5 capas × 5 parámetros = 25, ambas fases — correcto
  ✅ Universo de sucesos: 8 tipos, cobertura arquitecturalmente suficiente
  ✅ Diagrama de flujo: 6 subprocedimientos etiquetados, flujo canónico cerrado
  ✅ Separación subpuertas editoriales / panel operativo — declarada y correcta
```

### Estado declarado al cierre de Hito 1

**Hito 1 — Ficha Técnica de Diseño:** CERRADO ✅

```text
Hecho:
  ✅ FTD-AE-IMM-SV/0.3 consolidada y verificada
  ✅ Arquitectura celular explícita para Fase I (IMMUNO-1) y Fase II (IMMUNO-2)
  ✅ Parámetros P01–P25 de ambas fases alineados con repo
  ✅ Célula NLP declarada como exigencia de diseño del panel
  ✅ Universo de sucesos provisionalmente cerrado (8 tipos)
  ✅ Diagrama de flujo con nodo principal y 6 subprocedimientos etiquetados
  ✅ Catálogo preliminar de errores (5 familias, 13 códigos)
  ✅ Laboratorio mínimo de 10 casos definido
  ✅ Condición de paso a ITI específica declarada
  ✅ Custodia basal: bajo custodia basal suficiente

Deuda viva heredada (no bloquea):
  ⚠️ ISSN "2695-641X" en normative_engine.py fase_1 — etiqueta:
     deuda_issn_normative_engine_fase1
```

### Hito 2 — Panel experto–agente: ABIERTO

**Punto de partida:** implementación del panel principal con los 6 subprocedimientos etiquetados de la FTD §XIII.

**Primer hilo del Hito 2:** Agente-Inmunología1 (este hilo).

---

## Referencias mínimas

Lloret Egea, J. A. (2026a). *Documento 8 — Compilador doctrinal y célula meta SV(9,3)-IA*.

Lloret Egea, J. A. (2026b). *Patrón común emergente del agente especializado*.

Lloret Egea, J. A. (2026c). *Custodia basal del diseño en SVperitus*.

Lloret Egea, J. A. (2026d). *Agente especializado en Inmunología — sede canónica y fases I–II*.

Lloret Egea, J. A. (2026e). *Célula especializada de seguridad estructural para la custodia del diseño, el DSL y los laboratorios del Sistema Vectorial SV*.
