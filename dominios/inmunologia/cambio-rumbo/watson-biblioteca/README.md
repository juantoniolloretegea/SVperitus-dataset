# Watson-biblioteca — dominio de inmunología

**Corte:** 01-09-2026  
**Estatuto:** biblioteca candidata, compartida y append-only. No constituye el dominio clínico, no adopta consecuencias, no tipa matrices y no modifica el Lenguaje SV.  
**Autoría operativa:** Watson, bajo dirección y adopción expresa del Ingeniero Director.

## Objeto

Conservar únicamente fuentes que aporten material comprobable a uno o más de estos objetos:

1. perímetro profesional obligatorio;
2. conocimiento o habilidad inmunológica;
3. operación clínica o de laboratorio;
4. progresión y prueba de competencia;
5. consecuencia documentada de ignorancia, omisión o actuación incorrecta;
6. terminología e interoperabilidad;
7. datos o metadatos aptos para contraste empírico.

Una fuente localizada por un buscador no entra por ese solo hecho. La fuente primaria es el objeto bibliográfico; PubMed, OpenAlex, Consensus, Elicit y SciSpace son canales de descubrimiento o extracción.

## Jerarquía funcional

| Capa | Objeto | Ejemplos |
|---|---|---|
| A1 | Autoridad jurídica o profesional | BOE, programa profesional, organismo regulador |
| A2 | Estándar o guía clínica institucional | EULAR, CDC/ACIP, RCPath, AEMPS |
| A3 | Evidencia clínica primaria o síntesis rigurosa | ensayo, cohorte, revisión sistemática |
| A4 | Terminología e interoperabilidad | CIE-11, SNOMED CT, HL7 FHIR |
| A5 | Datos, registros y metadatos | ClinicalTrials.gov, openFDA, repositorios autorizados |

Las capas no son una escala automática de calidad. Expresan función. Una guía puede definir conducta; una cohorte puede cuantificar un desenlace; una terminología sólo identifica o transporta conceptos.

## Estados

- `VERIFICADA_CONTENIDO`: documento leído y objeto pertinente comprobado.
- `VERIFICADA_ACCESO`: acceso o API comprobados, sin adopción de contenido clínico.
- `CANDIDATA`: localizador exacto, pendiente de lectura material para el uso declarado.
- `BLOQUEADA`: acceso, licencia, autorización o aptitud de uso no constituidos.
- `NO_APLICA_COMO_FUENTE`: herramienta útil que no puede sustentar una afirmación clínica.

## Archivos

| Archivo | Función |
|---|---|
| `catalogo_fuentes_v0.1.csv` | Registro legible por máquina de fuentes y fronteras |
| `conectores_y_fronteras_v0.1.md` | Estado comprobado de APIs y conectores, sin secretos |
| `revision_biblioteca_grok_y_residuales_v0.1.md` | Material aprovechable, defectos y vacíos de cobertura |

## Regla de versión

Toda incorporación futura debe fijar, cuando exista: identificador persistente, versión o fecha, jurisdicción, idioma, localizador exacto, objeto admitido, objeto no admitido, estado de verificación y fecha de corte. No se consumirá silenciosamente una versión `latest`.

## Regla de seguridad

No se almacenan claves, secretos, tokens, identificadores de cliente ni datos personales. Las credenciales se mantienen fuera del repositorio.
