# Conectores validados 01-09-2026

Claves no se copian aquí ni al repo.

| Canal | Estado 01-09 | Para qué | No para qué |
|---|---|---|---|
| PubMed E-utilities | Vivo (clave NCBI) | PMID, MeSH, abstract | Umbral |
| Consensus MCP | Vivo (`https://mcp.consensus.app/mcp`) | Cribado 220 M | Sustituir PMID |
| OpenAlex | Vivo (plan free) | DOI, citas, obra | Cerrar G3 |
| openFDA | Vivo | SPL, señal FAERS | Incidencia / asistencia |
| ICD-11 WHO | Vivo (OAuth 3600 s) | Código MMS 2024-01 | Operación clínica |
| Europe PMC | Público, sin clave | OA / preprint | — |
| ClinicalTrials.gov v2 | Público, sin clave | NCT declarado | Microdato ImmPort |
| Semantic Scholar Graph API | Vivo (clave emitida 01-09-2026; consulta autenticada HTTP 200) | paperId, DOI, PMID, título, año; expansión bibliográfica | Fuente clínica; umbral; causalidad; sustituir PubMed |

Cupo S2 comprobado: 1 petición por segundo, acumulado entre extremos. Cabecera `x-api-key`. Atribución exigida por su licencia si hay publicación de resultados.

Prueba 01-09-2026: `GET /graph/v1/paper/PMID:25269391` → HTTP 200; DOI 10.1002/14651858.CD005590.pub3 (Stern 2014, ya fichado). No se volcó el JSON al repo.

ImmPort, TrialShare, dbGaP, PIDTC, ESID-R: ver acceso 5.
