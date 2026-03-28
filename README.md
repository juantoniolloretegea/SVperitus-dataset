# SVperitus-dataset — Agentes Especializados del Sistema Vectorial SV

Repositorio marco de familias especializadas y de sus implementaciones contrastables y conformes al Sistema Vectorial SV.

## Ecosistema SV — ubicación de esta sede

**Función de la sede:** agentes especializados del ecosistema SV, organizados por fases de desarrollo, con sus artefactos, aplicaciones y piezas de uso contrastable.

**Distribución vigente de sedes**
- **Doctrina, jerarquía y puerta general del ecosistema:** `SV-matematica-semantica`
- **Lenguaje, contrato técnico y sede operativa del manual SVP:** `SV-lenguaje-de-computacion`
- **Origen observacional, datasets e intrusión:** `SVcustos-dataset`
- **Agentes especializados, fases, artefactos y aplicaciones de uso:** `SVperitus-dataset`

**Regla de no sustitución**  
Este repositorio no sustituye ni la doctrina superior ni la sede técnica del lenguaje. Su función es alojar agentes especializados, su desarrollo por fases y sus superficies de uso.

**Remisión**  
Para una vista general del ecosistema SV y de la relación entre sedes, consulte la puerta general materializada en `SV-matematica-semantica/docs/index.html`.

## Marco de lectura

El Sistema Vectorial SV evalúa situaciones complejas mediante una gramática ternaria estable: `0` (Apto), `1` (No_Apto), `U` (Indeterminado). A partir de un vector ternario se obtiene una clasificación determinista, una representación geométrica polar cerrada y, cuando procede, una capa de análisis algorítmico o de revisión experta.

**Autoridad normativa principal:** Fundamentos algebraico-semánticos del Sistema Vectorial SV  
**Colección pública de referencia:** Álgebra de composición intercelular del Sistema Vectorial SV

## Patrón común emergente del agente especializado

La evolución actual del ecosistema hace comparecer ya un patrón común de agente especializado que no debe confundirse con los parámetros propios de un dominio concreto.

Ese patrón común incluye, cuando el grado de madurez del agente lo justifique:

- desarrollo por fases;
- publicación, laboratorio y figuras de fase;
- artefactos adscritos a fase;
- monitor poligonal principal;
- lectura por SUCESOS;
- plano IA trazable;
- capa R³ auxiliar;
- y evidencia o cierre de trazabilidad.

**Importante.** El plano IA trazable no se considera privilegio exclusivo del Agente especializado en Seguridad Estructural. Su aparición allí debe leerse como primera implementación piloto de un patrón que, tipado y subordinado, podrá generalizarse al resto de agentes del ecosistema.

**Pieza de referencia interna:** `especificaciones/patron_agente_especializado/README.md`

## Condición basal de custodia del diseño

Dentro de `SVperitus`, la célula especializada de seguridad estructural no debe leerse sólo como un agente singular adicional. Su publicación vigente la formaliza para custodiar el diseño, el DSL, el laboratorio y la cadena visible de implementación del propio SV. Por ello, su estatuto correcto dentro del ecosistema de agentes es doble:

1. Agente especializado propio, actualmente en Fase I.
2. Custodia basal obligatoria del diseño para el nacimiento, faseado, estabilización y vigilancia de nuevos agentes y nuevas fases relevantes.

Esto significa que ningún nuevo agente especializado ni ninguna fase relevante deben presentarse como maduros, fiables o estructuralmente conformes sin quedar sometidos, de forma visible, a esta custodia basal.

Esta condición basal:

- no sustituye a la doctrina superior;
- no sustituye al lenguaje SV ni a su sede técnica;
- no autoriza a la célula de seguridad a crear doctrina nueva;
- pero sí actúa como guardarraíl obligatorio del diseño dentro del ecosistema de agentes.

**Piezas de referencia interna:**
- `especificaciones/patron_agente_especializado/README.md`
- `especificaciones/custodia_basal_del_diseno/README.md`

## Arquitectura canónica ya abierta

La organización visible actual del repositorio conserva todavía trazas históricas en `dominios/`. La arquitectura canónica hacia la que se dirige `SVperitus` es, sin embargo:

**agentes especializados → fases → artefactos → aplicaciones**

El paso presente no elimina todavía los materiales históricos ni reubica por la fuerza todos los artefactos existentes. Lo que hace es abrir ya la sede canónica de agentes para que el repositorio deje de depender sólo de la capa transitoria `dominios/`.

```text
SVperitus-dataset/
│
├── agentes/ Sede canónica de agentes especializados
│ ├── inmunologia/
│ │ ├── fase_1/
│ │ ├── fase_2/
│ │ ├── fase_2/compositor/
│ │ └── index.html
│ └── seguridad_estructural/
│   └── fase_1/
│
├── especificaciones/ Verdad normativa verificable, puentes de aplicación y patrón común emergente
│ ├── nucleo/ Invariantes formales del SV y referencias nucleares de aplicación
│ ├── conformidad/ Tests de conformidad cruzada C8 (19 casos de paridad)
│ ├── esquemas/ Contratos YAML (JSON Schema)
│ ├── patron_agente_especializado/ Patrón común emergente del agente y de la capa IA trazable
│ └── custodia_basal_del_diseno/ Custodia basal obligatoria para agentes, fases y piezas sensibles
│
├── dominios/ Estado transitorio e histórico de lectura
│ └── inmunologia/ Ubicación material heredada mientras no se complete la migración canónica
│
├── comun/ Núcleo formal compartido (Capa A) + Γ(v)
├── meta/ Meta-célula SV(9,3)-IA (Capa A)
├── entornos/ Implementaciones por lenguaje (Capa A+B)
├── aplicaciones/ Despliegue al usuario (Capa B)
├── documentos/ Documentación y publicaciones relacionadas
└── muestras/ Datos de ejemplo
```

## Agentes ya identificados en sede canónica

### Agente especializado en Inmunología

Se abre ya su sede canónica en `agentes/inmunologia/`, organizada por fases y con subpuerta propia del agente.

- **Fase I:** corresponde al frente históricamente publicado como `IMMUNO-1`.
- **Fase II:** corresponde al frente `IMMUNO-2`, materializado en repositorio y con publicación específica todavía pendiente.
- **Compositor:** artefacto específico surgido del desarrollo de la Fase II; no constituye fase autónoma ni agente distinto.
- **Subpuerta del agente:** `agentes/inmunologia/index.html`

Mientras no se complete la migración material, el lector debe entender que la capa `dominios/inmunologia/` conserva todavía la ubicación histórica de trabajo.

### Agente especializado en Seguridad Estructural

Se abre ya su sede canónica en `agentes/seguridad_estructural/`.

- **Fase I:** corresponde al frente actualmente publicado como *Célula especializada de seguridad estructural para la custodia del diseño, el DSL y los laboratorios del Sistema Vectorial SV — Release 2*.
- Esta Fase I debe leerse simultáneamente como:
  - agente especializado propio;
  - y primera materialización de la custodia basal obligatoria del diseño dentro de `SVperitus`.

Las referencias actuales a `dominios/` deben leerse como estado transitorio del repositorio y no como taxonomía final del ecosistema.

La apertura de `agentes/` no implica todavía que todos los artefactos queden ya físicamente movidos. Implica que la lectura canónica correcta del repositorio ha dejado ya de ser ambigua.

## Primer dominio disponible: inmunología clínica

- **Fase 1 (`IMMUNO-1`)**: evaluación de profilaxis antiinfecciosa en pacientes con inmunosupresión farmacológica. `SV(25,5)`, `T(25)=19`. Motor normativo completo, port Rust, WASM, demo web y 108/108 tests de paridad. Publicado.
- **Fase 2 (`IMMUNO-2`)**: evaluación de riesgo infeccioso en inmunosupresión farmacológica no trasplante. `SV(25,5)`, `T(25)=19`. Motor normativo, función de criticidad `Γ(v)`, compositor serie y meta-célula `SV(9,3)-IA`. Port Rust/WASM con paridad verificada.
- **Compositor serie**: `IMMUNO-1 → P25 → IMMUNO-2`. Demostración del mecanismo de composición de la gramática SV, con autocrítica documentada.
- **Función `Γ(v) = m − μ`**: clasifica la indeterminación en irreducible, fronteriza o resoluble, dentro de una matemática exacta sin estadística.

## Capa IA trazable y regla de encaje

La capa IA del agente especializado no constituye una autoridad independiente ni una vía para degradar la terna `{0,1,U}`. Su función es asistir al experto humano mediante consulta, simulación condicionada y devolución trazable.

En consecuencia:

- la historia `REAL` no se confunde con la rama `SIM`;
- la simulación no funda por sí sola nuevo `SUCESO` real;
- la IA no sustituye el motor normativo del dominio;
- y ninguna interacción conversacional puede cerrar `U` al margen del álgebra, de la doctrina y del experto.

Dentro de este repositorio, la terna `{0,1,U}` debe entenderse siempre bajo estas condiciones:

- la convención canónica de la terna permanece invariante;
- la `U` no se degrada a probabilidad, nulidad o inferencia opaca;
- la validación experta y el motor normativo del dominio prevalecen sobre cualquier automatismo;
- las salidas del sistema deben mantener trazabilidad y auditabilidad.

## Regla de interpretación en SVperitus

- Ningún lenguaje ocupa el lugar semántico de una familia.
- Ninguna familia ocupa el lugar doctrinal del núcleo SVperitus.
- Ningún agente nuevo debe consolidarse sin custodia basal del diseño.

## Demos en vivo

- `IMMUNO-1` interactivo: `Demo WASM`
- Compositor `IMMUNO-1 → IMMUNO-2`: `Compositor`
- Tests de paridad WASM vs Python: `19/19 tests`
- `IMMUNO-1` formulario Kotlin: `Cliente Kotlin`
- `IMMUNO-1` demo JavaScript: `Demo JS`

## Serie y referencias públicas

- De SVcustos, el marco (framework) de intrusión, hasta SVperitus: agentes especializados
- Documento 7 — `IMMUNO-1`
- Documento 8 — Compilador doctrinal y célula meta `SV(9,3)-IA`
- Célula especializada de seguridad estructural — Release 2
- Fundamentos algebraico-semánticos del SV
- La guía práctica del conocimiento profundo y la crítica de la razón pura
- Origen doctrinal, definición y alcance de la U en el Sistema Vectorial SV
- Colección pública: Álgebra de composición intercelular del Sistema Vectorial SV

## Regla editorial

Los documentos del sistema se publican canónicamente en `itvia.online`. Los repositorios contienen código, datos, artefactos de soporte y reflejos o puentes de aplicación. Por ello, este repositorio no sustituye la publicación canónica, sino que la acompaña dentro del entorno técnico y aplicado de `SVperitus`.

## Autor

Juan Antonio Lloret Egea  
ORCID: 0000-0002-6634-3351  
ISSN: 2695-6411  
Licencia: CC BY-NC-ND 4.0

## Repositorios

- `SVcustos-dataset` (Docs 2–6): `https://github.com/juantoniolloretegea/SVcustos-dataset`
- `SVperitus-dataset` (Docs 7+): `https://github.com/juantoniolloretegea/SVperitus-dataset`
- `SV-matematica-semantica` (repositorio padre doctrinal): `https://github.com/juantoniolloretegea/SV-matematica-semantica`
- `SV-lenguaje-de-computacion` (derivación técnica del lenguaje SVP): `https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion`
