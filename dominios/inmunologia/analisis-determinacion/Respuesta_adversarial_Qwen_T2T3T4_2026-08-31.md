# Respuesta a la adversarial de Qwen sobre el informe T2/T3/T4

**Pieza atacada por Qwen:** el resumen de chat de esta unidad (3 correcciones + RSD-02 + IDSA + T3 + T4).  
**Contraste real:** `T2_T3_familias_guia_y_cruce_2026-08-31.xlsx`, `T4_procedencia_no_es_trazabilidad_2026-08-31.md`, `Matriz_cobertura_repositorios_v0.2_2026-08-31.xlsx` (40 cruces **de repositorio**, otro objeto), `Universo_candidato_parametros_INMUNO_v0.2`.  
**Corte:** 31-08-2026. No adopción. No reescritura de v0.2. RSD-02 sigue bloqueante.

---

## 0. Veredicto sobre la adversarial

Resiste: exigir localizador explícito; exigir comprobación eviQ post-30-06-2025; señalar que el chat de T4 no añade objeto nuevo respecto de la nota archivada; ACIP en P-VAC-001 no se sustituye solo porque exista IDSA 2025.

Colapsa: tratar T3 = 20 como si fuera la matriz de cobertura de repos = 40. Son dos tablas. El error de conteo es de Qwen, no del fichero.

---

## 1. T3 no es C-001–C-040

| Objeto | Archivo | N | Qué cruza |
|---|---|---|---|
| Matriz cobertura repos v0.2 | `Matriz_cobertura_repositorios_v0.2` hoja `01_Cobertura` | 40 (C-001…C-040) | entidad/parámetro × **repositorio A1** |
| T3 cruce sparse | `T2_T3_…xlsx` hoja `03_Cruce_sparse` | 20 (X-01…X-20) | **cota MIR** × parámetro v0.2 × **familia de guía T2** |

Los 5 huecos/frontera de T3 son X-11 TREC, X-12 IgG, X-13 XM, X-14 anti-MBG, X-19 dos POE: **sin_guia_en_T2** o frontera. No pretenden existir en la matriz de ImmPort/ESID.

Que TREC e IgG sí tengan filas en la matriz de repos no contradice que T3 las marque sin guía PJP/vacuna estacional. Distinto eje.

E-FR-ALERGO está en entidades v0.2. T3 X-19 usa la cota MIR `FR-01`, no el `entity_id`. Qwen pide la conexión: queda anotada aquí. No se reescribe v0.2.

---

## 2. Localizadores (el chat los omitió; T2 no)

Comprobado de nuevo el 31-08-2026:

| Guía | Localizador | Versión / fecha que se puede afirmar hoy |
|---|---|---|
| Cochrane Stern | DOI **10.1002/14651858.CD005590.pub3** · CD005590 · PMID 25269391 · https://www.cochrane.org/evidence/CD005590_antibiotic-treatment-prevention-pneumocystis-pneumonia-pcp-non-hiv-immunocompromised-patients | Issue 10, 2014. Búsqueda de actualización 2022–2026 de **esta** revisión: no aparece `pub4`. Metanálisis 2024 de profilaxis PCP en **VIH** son otra población; no sustituyen CD005590. |
| ASCO/IDSA Taplitz | DOI **10.1200/JCO.18.00374** · PMID 30179565 · J Clin Oncol 2018;36:3043–3054 | 04-09-2018. Sin actualización ASCO/IDSA de ese título fichada aquí. |
| AST Fishman | DOI **10.1111/ctr.13587** · PMID 31077616 | Clin Transplant 2019. |
| EULAR AIIRD cribado | DOI **10.1136/ard-2022-223335** · PMID 36328476 · Ann Rheum Dis 2023;82:742–753 · epub 03-11-2022 | Rec. 8 = considerar. No se ha fichado un EULAR 2024/2025 que sustituya esa rec. 8. Ausencia de ficha ≠ «no existe»; queda `no_buscado` para un update AIIRD posterior. |
| EULAR AAV 2022 update | Ann Rheum Dis 2024;83:30–47 · ScienceDirect S000349672400387X | Update de manejo AAV, no de cribado AIIRD. Distinto artículo. |
| eviQ 220 | https://www.eviq.org.au/p/220 y URL larga `…/220-pneumocystis-jirovecii-pneumonia-pjp-prophyl` | **Version 6. Last reviewed 19 May 2023. Review due 30 June 2025. Status: Current.** Reléído 31-08-2026. No hay aviso de v7 en esa página. Jurisdicción: Cancer Institute NSW (Australia). |
| IDSA vacunas IC | https://www.idsociety.org/practice-guideline/Seasonal-RTI-Vaccinations-in-Immunocompromised-Patients | Publicado 17-10-2025; last updated 18-11-2025. |

Qwen tenía razón sobre el **chat**. No sobre el xlsx T2, que ya llevaba DOI/URL en `localizador` salvo AAV (ahora explicitado).

eviQ: la due date venció; la página sigue marcando v6 Current. Eso se declara. No se inventa v7.

---

## 3. Puntos de Qwen que se aceptan

- Ficha de chat incompleta sin localizador. Cerrado en §2.  
- eviQ debía releerse después del 30-06-2025. Hecho: sigue v6 Current.  
- T4 del chat = resumen de la nota ya archivada. No hay objeto nuevo. El matiz «RSD-02 es colisión de contenido, no de firma» ya está en T4 §4.  
- P-VAC-001 `evidence_source` = «ACIP IC; calendarios ES; POE vacunas». IDSA 2025 **no** sustituye ACIP por el hecho de existir. Anotar la coexistencia queda para una v0.3 **si el Director la pide**. v0.2 no se toca.  
- Abstención en episodio cuya indicación PJP dependa del umbral no cerrado: coherente con R-019 / R-035 y con Origen de U. No es cierre de RSD-02.

## 4. Puntos de Qwen que no se aceptan

- «El número 20 no coincide con 40» como error de T3.  
- Exigir que XM, anti-MBG y dos POE «aparezcan en la matriz de cobertura» para que T3 sea válido. Esa matriz no es el sitio de esas fronteras.  
- Tratar la ausencia de EULAR 2024 en la ficha como desactualización demostrada de AIIRD 2022. No está demostrada.  
- Pedir que este informe cite non-closure / Orientation / VII. Fuera de objeto (el propio Qwen lo concede en su §6).

## 5. Estado que no cambia

RSD-02 bloqueante. Cero umbrales. v0.2 congelada. G0 cerrado. T5 sigue: la adversarial se responde; no se fusionan objetos.
