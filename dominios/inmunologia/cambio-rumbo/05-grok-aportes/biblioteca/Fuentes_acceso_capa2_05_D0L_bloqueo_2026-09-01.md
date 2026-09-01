# Acceso 5 de 5 — D0-L (bloqueo, no alta)

Corte: 01-09-2026. No se crea cuenta. No se descarga microdato. D0-E permanece 0.

## Qué es D0-L
Combinación comprobada, por conjunto × versión × finalidad, de: acceso + autorización + licencia aplicable + elegibilidad para tratamiento por IA.  
Dato público descargable ≠ D0-L. Metadato de ensayo ≠ paquete inspeccionado.

## Lo que no se abre en este corte
| Fuente | Por qué no hay «acceso» que habilitar |
|---|---|
| ImmPort | Acuerdo: datos no adecuados para diagnóstico o tratamiento humano. Autenticación para paquete. SDY3324/3274 y el resto del expediente v0.1 no inspeccionados. Assays/Clinical Assessments en DR60: None. |
| TrialShare / ITN | Cuenta. Régimen de uso por IA no comprobado. RAVE candidato, no D0-E. |
| dbGaP | Autorización NIH por estudio. No pedida. |
| PIDTC REDCap (CCHMC) | 6901/6902 closed May 2025; extract-only interno. No dump público. |
| ESID-R / USIDNET / REDIP | Clase C/D en inventario A1. REDIP no es descarga abierta. |
| HCE / FHIR / LIS | Episodio real. Prohibido. |

## Lo que sí se puede usar sin D0-L
- ClinicalTrials.gov API v2 (NCT, brazos, desenlaces declarados): https://clinicaltrials.gov/data-api/api
- Lecturas públicas ya hechas: paper ACV01 (SDY3324 / NCT05000216), paper ARTIST (SDY3274). N tipado por fase; 140/141 no armonizado.
- PubMed / Cochrane / EULAR / ACIP / CIMA / IUIS / BOE de los accesos 1–4.

## Estado heredado (no reabrir cifras)
- D0-E: 0 filas.
- 0/40 campos de cobertura comprobados en v0.2.
- Expediente D0 v0.1 = sinopsis, no auditoría material cerrada.
- ImmPort 2.5 y TrialShare: no uso para tratar.

## Estatuto
Este «acceso 5» es el residual empírico consciente. Constituye consecuencia de *no* tener cohorte autorizada: no se puede validar umbral, incidencia ni episodio con microdatos.  
No se salta con más APIs. No se pide clave ImmPort.
