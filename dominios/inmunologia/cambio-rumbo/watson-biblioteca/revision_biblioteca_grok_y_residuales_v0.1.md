# Revisión de la biblioteca de Grok y residuales — v0.1

**Objeto revisado:** `05-grok-aportes/biblioteca`, siete archivos leídos íntegramente en la rama `dominio-inmunologia`.  
**Dictamen:** aprovechable como expediente focal de acceso y como primer lote PJP/IUIS; no apta todavía como biblioteca del dominio inmunológico completo.

## Material que resiste

1. Los localizadores BOE de Inmunología y Alergología son exactos y preservan correctamente la frontera entre especialidades.
2. El expediente Cochrane separa muerte por PJP, mortalidad por todas las causas, incidencia, eventos adversos y NNT. Esa separación evita una falsa afirmación global de reducción de mortalidad.
3. El expediente IUIS corrige una confusión material: 508 genes monogénicos no son 559 entidades fenotípicas y ninguno de esos recuentos debe transformarse automáticamente en parámetros.
4. El bloqueo D0-L evita presentar registros cerrados o metadatos de ensayos como cohortes clínicas ya inspeccionadas.
5. La prohibición de guardar claves en el repositorio es correcta.

## Reparos

### R1 — Cobertura clínica insuficiente

La biblioteca se concentra en PJP, vacunación, cotrimoxazol, IEI y acceso a repositorios. No cubre el dominio profesional ya identificado: inmunología básica aplicada, inmunodeficiencias secundarias, autoimunidad, autoinflamación, complemento, inmunoterapia, trasplante, malignidad linfoide, alergia como frontera, laboratorio, genética, citometría, HLA, calidad, comunicación crítica y seguimiento.

### R2 — Estados de conexión inexactos

Consensus figura como `Vivo` sin consulta material comprobada. CIE-11 figura con MMS `2024-01`, mientras que la API oficial devolvió `2026-01` como versión más reciente. El estado de acceso debe ser empírico y fechado.

### R3 — Objetos heterogéneos bajo el rótulo biblioteca

Coexisten literatura, programas, conectores e impedimentos internos. Todos son útiles, pero no cumplen la misma función epistemológica. Deben separarse para impedir que un canal de búsqueda o un residual de acceso adquiera apariencia de fuente clínica.

### R4 — Metadatos no uniformes

No todas las entradas fijan versión, jurisdicción, población, desenlace, diseño, estado de lectura, objeto admitido y objeto prohibido. Sin esos campos no puede automatizarse una auditoría rigurosa.

### R5 — Terminología e interoperabilidad ausentes

No están integradas SNOMED CT, la versión fijada de CIE-11, HL7 FHIR ni la distinción entre clasificación, terminología y transporte. Esta ausencia es material porque el catálogo deberá mapear conceptos sin dejar que el estándar de intercambio determine el conocimiento.

### R6 — No existe matriz de cobertura por familias

Cinco accesos no permiten saber qué familias del conocimiento obligatorio están documentadas, cuáles sólo tienen currículo y cuáles carecen todavía de evidencia de consecuencias.

## Residuales declarados para Watson-biblioteca

| Residual | Estado |
|---|---|
| Catálogo profesional español atomizado | Pendiente; el BOE es tronco, no desglose suficiente |
| Integración controlada ACLI + HSST/STP | Candidata; debe preservar rol médico frente a científico |
| Consecuencias por conocimiento obligatorio | Prácticamente abiertas salvo ejemplos focales |
| Cohortes abiertas y aptas para tratamiento | No constituidas |
| SNOMED CT | Edición, licencia, jurisdicción y mapeo pendientes |
| FHIR | R5 comprobado; perfiles y recursos del caso de uso pendientes |
| CIE-11 | Acceso operativo; mapeo de entidades pendiente; versión de adopción no decidida |
| PJP | Eficacia documentada en poblaciones seleccionadas; indicación universal no cerrada |
| Cobertura integral del dominio | Abierta |

## Consecuencia metodológica

La biblioteca de Grok no debe descartarse ni promoverse a biblioteca total. Se conserva como contribución especializada. Watson-biblioteca aporta el índice transversal, corrige los estados de acceso y deja preparada la futura relación:

`conocimiento obligatorio → operación → contexto → competencia → fuente profesional → evidencia de consecuencia → terminología → dato verificable`

Esta relación sigue siendo candidata. No se ha realizado ninguna proyección a matrices ni al Lenguaje SV.
