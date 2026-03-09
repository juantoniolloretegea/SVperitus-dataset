# SVperitus-dataset — Agentes Especializados basados en el Sistema Vectorial SV

Repositorio marco de familias especializadas y de sus implementaciones contrastables y conformes al marco.

El Sistema Vectorial SV evalúa situaciones complejas mediante una gramática ternaria estable: **0** (Apto), **1** (No_Apto), **U** (Indeterminado). A partir de un vector ternario se obtiene una clasificación determinista, una representación geométrica polar cerrada y, cuando procede, una capa de análisis algorítmico o de revisión experta.

**Autoridad normativa:** [Fundamentos algebraico-semánticos del Sistema Vectorial SV](https://www.itvia.online/pub/fundamentos-algebraico-semanticos-del-sistema-vectorial-sv/release/1) — v1.0.0, Release 1.

---

## Estructura del repositorio

```
SVperitus-dataset/
│
├── especificaciones/           Verdad normativa verificable
│   ├── nucleo/                 Definiciones formales del SV
│   ├── conformidad/            Tests de conformidad cruzada (C8)
│   └── esquemas/               Contratos YAML, validación
│
├── dominios/                   Familias de dominio (Capa C)
│   └── inmunologia/            Primer dominio disponible
│       ├── fase_1/             Célula IMMUNO-1: profilaxis antiinfecciosa
│       ├── fase_2/             Célula IMMUNO-2: riesgo infeccioso en IS
│       └── compositor/         Composición serie fase 1 → fase 2
│
├── comun/                      Núcleo formal compartido (Capa A)
│
├── meta/                       Meta-célula SV(9,3)-IA (Capa A)
│
├── entornos/                   Implementaciones por lenguaje (Capa A+B)
│   ├── python/                 Referencia canónica
│   ├── rust/                   Port verificable + WASM
│   └── kotlin/                 En observación
│
├── aplicaciones/               Despliegue al usuario (Capa B)
│   ├── demo_web/               Demo JavaScript
│   ├── demo_wasm/              Demo Rust/WASM
│   ├── cliente_kotlin/         Formulario interactivo
│   └── cuadernos/              Notebooks (futuro)
│
├── documentos/                 Documentación + DOIs
│   ├── doctrina/               Paper fundacional, Álgebra, Sentencia
│   └── serie/                  Documentos publicados (7, 8, 9...)
│
└── muestras/                   Datos de ejemplo
```

---

## Primer dominio disponible: inmunología clínica

- **Fase 1 (IMMUNO-1):** evaluación de profilaxis antiinfecciosa en pacientes con inmunosupresión farmacológica. SV(25,5), T(25)=19. Motor normativo completo, port Rust, WASM, demo web.
- **Fase 2 (IMMUNO-2):** evaluación de riesgo infeccioso en IS farmacológica no trasplante. SV(25,5), T(25)=19. Motor normativo, compositor serie, función de criticidad Γ(v), meta-célula SV(9,3)-IA.

---

## Regla de oro

> Ningún lenguaje ocupa el lugar semántico de una familia.
> Ninguna familia ocupa el lugar doctrinal del núcleo SVperitus.

---

## Serie

«De SVcustos, el marco (framework) de intrusión, hasta SVperitus: agentes especializados»

- [Documento 7 — IMMUNO-1](https://www.itvia.online/pub/de-svcustos-hasta-svperitus-documento-7-immuno-1)
- [Documento 8 — Compilador doctrinal y célula meta SV(9,3)-IA](https://www.itvia.online/pub/compilador-doctrinal-y-celula-meta-sv93-ia/release/2)
- [Fundamentos algebraico-semánticos del SV](https://www.itvia.online/pub/fundamentos-algebraico-semanticos-del-sistema-vectorial-sv/release/1)

---

## Autor

**Juan Antonio Lloret Egea**
ORCID: [0000-0002-6634-3351](https://orcid.org/0000-0002-6634-3351)

**ISSN:** 2695-6411
**Licencia:** CC BY-NC-ND 4.0

---

## Repositorios

- SVcustos-dataset (Docs 2–6): https://github.com/juantoniolloretegea/SVcustos-dataset
- SVperitus-dataset (Docs 7+): https://github.com/juantoniolloretegea/SVperitus-dataset
