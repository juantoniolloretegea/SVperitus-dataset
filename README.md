# SVperitus-dataset

Repositorio de agentes especializados del Sistema Vectorial SV. Aloja el desarrollo por fases de cada agente, sus artefactos contrastables, sus superficies de uso y la memoria mínima de calidad aplicada de esta sede.

## Ecosistema SV — ubicación de esta sede

**Función de la sede:** agentes especializados, fases, artefactos y aplicaciones de uso contrastable del ecosistema SV.

**Distribución vigente de sedes**
- **Doctrina, autoridad normativa y puerta general del ecosistema:** `SV-matematica-semantica`
- **Lenguaje, contrato técnico y sede operativa del manual SVP:** `SV-lenguaje-de-computacion`
- **Origen observacional, datasets e intrusión:** `SVcustos-dataset`
- **Agentes especializados, fases, artefactos y aplicaciones de uso:** `SVperitus-dataset`

**Regla de no sustitución**
Este repositorio no sustituye ni la sede doctrinal ni la sede técnica del lenguaje. Su función es aplicada: organizar agentes con obligaciones y servicios diferenciados, sus fases, sus artefactos y sus aplicaciones de uso.

> [!NOTE]
> Para una vista general del ecosistema SV y de la relación entre sedes, consulte la puerta general del ecosistema materializada en `SV-matematica-semantica/docs/index.html`.

> [!NOTE]
> Para entrar en esta sede desde una vista ordenada —con función de la sede, ruta de lectura y accesos humanos directos a agentes y fases— consulte la <a href="https://juantoniolloretegea.github.io/SVperitus-dataset/" target="_blank" rel="noopener noreferrer">página web de entrada y navegación de SVperitus-dataset</a>.

Autor: Juan Antonio Lloret Egea · ORCID 0000-0002-6634-3351  
ISSN: 2695-6411  
Licencia: CC BY-NC-ND 4.0

## Agentes y fases activas

| Pieza | Estatuto actual | Entrada humana recomendada |
|---|---|---|
| Agente especializado en Seguridad Estructural | Agente especializado propio y custodia basal visible del diseño | <a href="https://juantoniolloretegea.github.io/SVperitus-dataset/agentes/seguridad_estructural/" target="_blank" rel="noopener noreferrer">puerta del agente</a> |
| Seguridad estructural — Fase I | Primera fase materializada del agente | <a href="https://juantoniolloretegea.github.io/SVperitus-dataset/agentes/seguridad_estructural/fase_1/" target="_blank" rel="noopener noreferrer">puerta de fase</a> |
| Portal web local de Seguridad Fase I | Monitor, SUCESOS, IA trazable, R³ auxiliar y evidencia | <a href="https://juantoniolloretegea.github.io/SVperitus-dataset/agentes/seguridad_estructural/fase_1/artefactos_web/" target="_blank" rel="noopener noreferrer">portal web local</a> |
| Agente especializado en Inmunología | Agente especializado con desarrollo por fases | <a href="https://juantoniolloretegea.github.io/SVperitus-dataset/agentes/inmunologia/" target="_blank" rel="noopener noreferrer">puerta del agente</a> |

## Organización canónica de esta sede

La organización de referencia de `SVperitus-dataset` sigue el eje:

```text
agentes → fases → artefactos → aplicaciones
```

Las superficies históricas conservadas en `aplicaciones/` no sustituyen las puertas canónicas alojadas en `agentes/`.

## Agente de seguridad estructural — criterio de lectura

La seguridad estructural no introduce soberanía nueva dentro del ecosistema SV. Su estatuto correcto es doble:

1. agente especializado propio, con obligaciones y servicios definidos;
2. custodia basal visible del diseño para el nacimiento, faseado y estabilización de nuevos agentes o nuevas fases sensibles.

Por ello, la lectura recomendada de su frente es:

1. `agentes/seguridad_estructural/index.html`
2. `agentes/seguridad_estructural/fase_1/index.html`
3. `agentes/seguridad_estructural/fase_1/artefactos_web/index.html`

## Marco de lectura del repositorio

El Sistema Vectorial SV trabaja con una gramática ternaria estable: `0` (Apto), `1` (No_Apto) y `U` (Indeterminado). Los agentes especializados de esta sede no alteran esa base; la aplican en carriles tipados, con fases, artefactos y superficies de lectura humana o de apoyo técnico.

## Calidad mínima y remisión operativa

La memoria mínima de calidad local de esta sede reside en:

- `docs/calidad/README.md`
- `docs/calidad/NOTA_DE_ALCANCE_DEL_CONTROL_DE_CALIDAD_EN_SVPERITUS_2026_03_28.md`
- `docs/calidad/REGISTRO_MINIMO_DE_HITOS_Y_CIERRES_SVPERITUS.csv`
- `docs/calidad/DEUDA_VIVA_MINIMA_SVPERITUS.csv`
- `docs/calidad/REGISTRO_MINIMO_DE_ACTUACIONES_POR_BLOQUE_Y_SEDE_SVPERITUS.csv`

> **Regla de alcance**
> El control mínimo local de `SVperitus` no desplaza la sede logística fuerte de calidad y trazabilidad técnica del ecosistema, que sigue residiendo en `SV-lenguaje-de-computacion/docs/calidad/`.

## Estructura del repositorio

```text
SVperitus-dataset/
├── README.md
├── index.html                       ← Puerta general propia de esta sede
├── agentes/
│   ├── seguridad_estructural/       ← Puerta del agente y fases visibles
│   └── inmunologia/                 ← Puerta del agente y fases visibles
├── aplicaciones/                    ← Superficies de uso y espejos históricos controlados
├── documentos/                      ← Documentación transversal aplicada
├── especificaciones/                ← Patrón común, custodia basal y piezas subordinadas
├── docs/                            ← Calidad mínima local y soporte auxiliar
└── entornos/                        ← Clientes y entornos de ejecución o ensayo
```
