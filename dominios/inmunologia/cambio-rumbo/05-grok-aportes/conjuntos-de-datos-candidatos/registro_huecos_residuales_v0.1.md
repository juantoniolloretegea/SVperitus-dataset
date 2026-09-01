# Registro de huecos, residuales e incompatibilidades — ronda 1

Corte: 2026-09-01. Estatuto de todo lo aqui: CANDIDATO_NO_ADOPTADO.
Cero microdatos en el repositorio. Cero claves. Sin PR. Sin main.

Bibliotecas consultadas antes de buscar fuera:
- 05-grok-aportes/biblioteca (BOE, guias, Cochrane pub3, IUIS 508!=559, D0-L bloqueo, conectores)
- cambio-rumbo/watson-biblioteca/catalogo_fuentes_v0.1.csv (DATA-IMMPort BLOQUEADA; DATA-CTGOV CANDIDATA; DATA-OPENFDA VERIFICADA_ACCESO)
- Expediente_D0_estudios_candidatos_v0.1_2026-08-31
- Consulta_PIDTC_bases_2026-08-31
No se anadio literatura nueva a watson-biblioteca.

## Resultado
- 12 filas inventario (conjunto x version x finalidad).
- 12 manifiestos segun plantilla_manifiesto_conjunto_v0.1.md.
- Estados D0-L usados (lista permitida del README): EVALUADO (2 metadatos NCT), ACCESO_PENDIENTE (3), IDENTIFICADO (5), NO_ADMISIBLE (2). Ningun ADMISIBLE_CANDIDATO.
- D0-E sigue 0.

## Verificados en fuente primaria esta ronda
| ID | Fuente primaria | Resultado |
|---|---|---|
| REG-001 | ClinicalTrials.gov API v2 NCT05000216 HTTP 200 | TERMINATED; enrollment ACTUAL 258; whyStopped: continued enrollment hurdles; no armonizar con 279/148/140/141 |
| REG-003 | ClinicalTrials.gov API v2 NCT01516177 HTTP 200 | COMPLETED; enrollment ACTUAL 250; no es ST507 2010 |
| REG-002 / REG-004 | Acuerdo ImmPort ss 1.1, 2.4, 2.5 + DR60 | ACCESO_PENDIENTE; s2.5 excluye diagnostico y tratamiento; diccionario no leido |
| REG-011 | openFDA event.json meta HTTP 200 | last_updated 2026-07-30; vigilancia no es cohorte |
| SDY3324/3274/1414/621/218/1845/1039 paginas /shared/study | HTTP 200, 17538 bytes identicos | cascaron JS; no es diccionario |

## Identificados sin ficha primaria
REG-005 a REG-009 (SDY1414, 621, 218, 1845, 1039): accesiones del expediente 31-08. N citados no recontados.

## No admisibles
- REG-010 PIDTC 6901/6902: closed May 2025; sin dump abierto.
- REG-011 FAERS: senal, no incidencia ni cohorte.

## Huecos de dominio (no se cubren)
- F-IEI: cohorte abierta comprobada ausente (D0-GAP-IEI). IUIS 508 genes / 559 fenotipos no sustituye.
- F-PJP: ningun conjunto trae evento PJP + IS + umbral (RSD-02 abierto). Cochrane CD005590.pub3 y EULAR AIIRD no son microdato.
- Vacuna viva / ventana 30 d: ACV01 es refuerzo no vivo; el registro excluye vacuna viva reciente o prevista.
- Complemento, autoinflamacion, laboratorio rutinario ES, HLA SOT operativo.

## Incompatibilidades
- Publicacion distinto de deposito (SDY3324 paper vs DR60 Assays None).
- N no intercambiables (258 / 279 / 148 / 140 / 141).
- Acceso publico NCT distinto de autorizacion ImmPort distinto de elegibilidad IA.
- Pagina ImmPort /shared/study/{SDY} no es diccionario.
- Dato publico descargable no es D0-L.

## Prohibiciones respetadas
Sin descarga de paquetes. Sin claves en repo. Sin PR. Sin main. Sin consecuencias clinicas. Sin componentes SV. Sin armonizacion de rotulos.
