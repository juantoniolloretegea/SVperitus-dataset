# Conectores, APIs y fronteras — v0.1

**Corte:** 01-09-2026.  
**Regla:** `instalado`, `autenticado`, `consultado` y `apto para una finalidad` son estados distintos. No se almacenan secretos.

| Canal | Estado comprobado por Watson | Objeto útil | Frontera obligatoria |
|---|---|---|---|
| PubMed E-utilities | Consulta autenticada operativa | PMID, MeSH, metadatos, estrategias reproducibles | El índice no sustituye al artículo |
| OpenAlex REST API | Clave aceptada; JSON y coste devueltos | Grafo de obras, DOI, citas, autores e instituciones | Citas no equivalen a calidad ni causalidad |
| openFDA | Clave aceptada; endpoint FAERS consultado; actualización 2026-07-30 | Etiquetado, farmacovigilancia, retiradas y señales | FAERS no permite incidencia ni causalidad y es jurisdicción estadounidense |
| OMS ICD API | OAuth 2.0 aceptado; API v2; español; token temporal; MMS consultada | CIE-11 Foundation/MMS, URI, códigos, jerarquía y versión | No es conocimiento, competencia ni recomendación; no sustituye SNOMED CT |
| Consensus | Aplicación instalada y habilitada; acción de búsqueda no expuesta en esta sesión | Búsqueda semántica y contraevidencia cuando quede invocable | No declarar `vivo` hasta completar una consulta; no sustituye fuente primaria |
| Elicit | Aplicación instalada y habilitada; llamada material no verificada | Extracción estructurada de estudios | La síntesis no constituye evidencia sin verificar el artículo |
| SciSpace | Aplicación instalada y habilitada; llamada material no verificada | Cribado de métodos, resultados y conclusiones | No es fuente clínica ni autoridad |
| ClinicalTrials.gov API v2 | Endpoint público identificado; prueba material Watson pendiente | Registro y metadatos de ensayos | Registro no equivale a resultado; no contiene necesariamente microdatos |
| Europe PMC | Endpoint público identificado; prueba material Watson pendiente | Acceso abierto y metadatos | No confundir disponibilidad con calidad o aplicabilidad |
| Semantic Scholar Graph API | Clave emitida 01-09-2026; consulta autenticada Grok HTTP 200 sobre PMID:25269391 | paperId, DOI, PMID, título, año | No es fuente clínica; cupo 1 pet/s; atribución si se publican resultados; no sustituye PubMed |
| SNOMED CT releases | Punto oficial identificado; paquete/edición/licencia no adoptados | Versiones terminológicas | No usar una edición sin fijar jurisdicción, licencia y versión |
| HL7 FHIR | Especificación R5 5.0.0 comprobada | Transporte, perfiles, Provenance, AuditEvent | No resuelve por sí solo semántica clínica ni lógica de composición |

## Corrección respecto del registro de Grok

1. `Consensus MCP = Vivo` no está demostrado por una consulta material en esta sesión. El estado correcto es `instalado/habilitado; invocación pendiente`.
2. `ICD-11 MMS 2024-01` no debe quedar como versión corriente. La API de la OMS devolvió `2026-01` como última versión el 01-09-2026. La adopción futura deberá fijar expresamente una versión, no consumir `latest`.
3. `OpenAlex`, `openFDA` y `OMS ICD API` sí pasaron autenticación y consulta mínima de lectura.
4. Un conector operativo no autoriza una afirmación médica ni el tratamiento de datos.
5. Semantic Scholar: la fila nueva registra emisión de clave y una consulta Graph API autenticada (01-09-2026). Watson no ha repetido esa llamada en esta sesión. El estado no equivale a fuente clínica adoptada.

## Orden de uso

1. Formular la necesidad desde el catálogo profesional o la ruta crítica.
2. Buscar en PubMed y ampliar mediante OpenAlex.
3. Usar Consensus, Elicit o SciSpace únicamente como apoyo cuando exista llamada material y el resultado sea verificable.
4. Recuperar y leer la fuente primaria.
5. Registrar sólo la afirmación que la fuente permite, junto con población, desenlace, jurisdicción y límites.
6. Utilizar CIE-11, SNOMED CT o FHIR después de constituir el concepto clínico; nunca para inventarlo.
