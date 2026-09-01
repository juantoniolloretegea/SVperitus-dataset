# T4 — Procedencia no es trazabilidad

**Corte:** 31-08-2026.  
**Estatuto:** nota lateral. No tipa SV. No constituye acta predecisional. No descarga datasets.  
**Textos de anclaje internos:** Origen de U §6.4 y §11.5; Fundamentos §6.4; lema Documento V (operador de consulta); hecho de trabajo «Provenance is not traceability» (Futurium, 3-08-2026).  
**Textos externos fichados:** W3C PROV-DM (2013); FHIR Provenance; ProvCaRe (Sahoo et al., 2019).

---

## 1. Tres objetos

| Objeto | Qué registra | Fuente de la definición usada aquí |
|---|---|---|
| **Procedencia (provenance)** | Quién/qué produjo un recurso, con qué entidades y actividades, cuándo. Cadena de origen del *dato o del artefacto*. | W3C PROV-DM: «information about entities, activities, and people involved in producing a piece of data or thing». FHIR Provenance: «who, what, when for a set of resources». |
| **Trazabilidad SV de un juicio** | Qué parámetros se evaluaron, en qué estado 0/1/U, qué U quedó sin resolver, qué vía de resolución se usó (experto / suceso / medición), qué consulta se emitió. Cadena del *cierre o del no-cierre*. | Origen §6.4 y §11.5; Fundamentos §6.4. Documento V (consulta) no leído en texto íntegro en esta pasada: se cita el lema, no se inventa el operador. |
| **Acta predecisional** | Registro inmutable *antes* de la decisión humana: consecuencias de ignorancia ya constituidas + paradas. | Pieza de gobierno del bisturí v0.4 (candidata, no adoptada). No es PROV. |

PROV puede anotar que un valor de IgG salió del laboratorio X el día D. Eso no dice si el sistema podía cerrar 0 o 1 sobre profilaxis PJP.

## 2. Hechos externos, no lemas

- W3C publicó PROV como Recommendation en 2013 (PROV-DM, PROV-O).  
- FHIR define el recurso Provenance «with close consideration for W3C Provenance».  
- ProvCaRe (Sahoo et al., *J Biomed Inform* / 2019) extiende PROV a reproducibilidad de estudios biomédicos. Objeto: metadatos de estudio, no sentencia clínica ternaria.  
- El proyecto ya separó los términos el 3-08-2026 («Provenance is not traceability»). Esta nota no inaugura la distinción; la ficha para que Qwen/Watson no usen FHIR Provenance como si fuera el acta.

## 3. Lo que no se puede decir

- Que un log FHIR Provenance «cumple» Origen §6.4.  
- Que W3C PROV es el operador de consulta del Documento V (el texto V no está leído aquí).  
- Que la ausencia de Provenance equivale a U. U no es metadato de origen (Origen §7 y §12.2).

## 4. Uso en INMUNO

A1 ya leyó normas de repos. Eso es procedencia de *acceso* (quién puede ver qué, bajo qué DUA). No es trazabilidad de un episodio. ImmPort 2.5 y TrialShare prohíben uso para tratar: eso es derecho de uso, tampoco es U.

RSD-02 no se cierra con un registro de procedencia de una guía. Las familias T2 chocan en disparador y en fuerza; esa colisión es de contenido, no de quién firmó el PDF.
