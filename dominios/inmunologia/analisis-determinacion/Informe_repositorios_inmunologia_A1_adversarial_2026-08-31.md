# Informe A1 — repositorios de inmunología
## Adversarial + fichas normativas
**Corte:** 31-08-2026  
**Autor del inventario:** unidad Grok, subordinada al autor humano  
**Estatuto:** inventario y ataque. Ninguna fuente adoptada. Ninguna cuenta creada. Ningún dataset descargado.  
**Base factual:** `Inventario_repositorios_inmunologia_A1_2026-08-31.xlsx` y las páginas de norma leídas ese día.  
**Régimen:** no inferir. Fecha + fuente + contenido declarado. Opinión fuera.

---

# Parte I — Adversarial

Veredicto ternario por flanco: **resiste / colapsa / no demostrado**.

El objeto atacado no es «existen repositorios de inmunología». Eso resiste. El objeto atacado es la tesis implícita de que el inventario A1 ya suministra *datos anonimizados usables* para constituir o contrastar el dominio clínico operativo de las semillas (profilaxis antiinfecciosa / riesgo infeccioso en inmunosupresión farmacológica no trasplante).

Esa tesis **colapsa**.

---

## I.1 Confundir «inmunología» con el episodio de las semillas

**Veredicto: colapsa.**

Las once fuentes son de inmunología en sentido institucional o molecular. Ninguna declara, en la norma leída, el episodio de las semillas.

| ID | Objeto declarado en su sede | Objeto de las semillas |
|---|---|---|
| R03 ESID, R04 USIDNET, R05 REDIP | IEI / PID / errores innatos | Inmunosupresión farmacológica adquirida |
| R06 TrialShare | Ensayos ITN de tolerancia inmune | Profilaxis / riesgo en IS no trasplante |
| R02 ImmuneSpace | Vacunación, infección, medicación, enfermedad inmunomediada a nivel de sistemas | El mismo recorte estrecho de IS farmacológica |
| R07 IEDB, R08 OAS, R09 AIRR/iReceptor, R11 VDJdb | Epítopo, repertorio BCR/TCR | Historia clínica de profilaxis |
| R10 FlowRepository | FCS de manuscritos MIFlowCyt | Parámetros clínicos de episodio |
| R01 ImmPort | Agregado heterogéneo de estudios NIAID/DAIT | *No auditado estudio a estudio* |

Un revisor clínico duro no acepta «hay 189.000 sujetos en ImmPort» como evidencia de cobertura del paciente oncohematológico inmunosuprimido en profilaxis. La cardinalidad del portal no es la cardinalidad del episodio.

**Lo que resiste:** el inventario no adoptó esas fuentes como dominio.  
**Lo que colapsaría el frente:** usar R03–R05 como «datos de inmunología españoles/europeos» para tensionar IMMUNO-1/2.

---

## I.2 «Anonimizado» no es un predicado único

**Veredicto: colapsa si se unifica; resiste si se mantiene la tabla de identificabilidad.**

Lo leído no es un solo régimen:

| Régimen leído | Dónde | Consecuencia operativa |
|---|---|---|
| Safe Harbor HIPAA (edad >89→90, quitar fechas/IDs/centros) | ImmPort, TrialShare | Desidentificado *según ese método*. Reidentificación prohibida por acuerdo. No es anonimato GDPR. |
| Seudónimo; clave en el centro documentador | ESID Center Agreement v4.4 (23-08-2024); PIC GDPR v4.0 | **No es anónimo.** Es seudónimo. Cesión con doble seudonimización y contrato de proyecto. |
| Consentimiento + acreditación de investigador | REDIP / RePER / LOPDGDD | Registro de pacientes. El manual V5 2024 limita la descarga al rol. |
| Waiver of consent + doble des-ID (v2) frente a consentimiento (v1) | USIDNET | Dos objetos jurídicos en el mismo nombre. |
| Dato de literatura / secuencia | IEDB, OAS, VDJdb, AIRR | No hay «paciente a anonimizar» en el mismo sentido. El riesgo está en metadatos del estudio fuente. |
| Keywords FCS no esenciales | FlowRepository | Des-ID de archivo de instrumento, no de historia clínica. |

Llamar a REDIP o ESID «repositorio de datos anonimizados que podemos usar» es falso respecto de las normas leídas.  
Llamar a IEDB «datos de pacientes anonimizados» es falso respecto de su objeto.

**Safe Harbor ≠ anonimato GDPR ≠ seudónimo de registro ≠ secuencia de repertorio.** Mezclarlos en una sola columna de «usables» no sobrevive revisión.

---

## I.3 «Podemos usarlos» choca con las cláusulas de uso

**Veredicto: colapsa como permiso de uso clínico o asistencial.**

Cláusulas leídas, no interpretadas:

1. **ImmPort User Agreement 2.5.** Los datos no son aptos para informar decisiones de tratamiento ni diagnóstico humano. NIAID/Peraton declinan responsabilidad por ese uso.
2. **ImmPort 1.1.** Prohibido identificar individuos o cruzar datasets para reidentificar. Incidente: no usar el conocimiento, notificar al Program Officer, no informarlo a nadie más.
3. **ImmPort 2.1.** Sin garantías de exactitud, integridad ni idoneidad.
4. **TrialShare Access Policy v2.0 (27-08-2019).** El usuario acepta no intentar identificar participantes.
5. **USIDNET PI Agreement 2019.** El registro no puede usarse para concluir incidencia o prevalencia. No se libera el archivo para *data mining* o revisión general.
6. **ESID v4.4.** Solo proyectos evaluados por el Registry Steering Group; confidencialidad indefinida; no reidentificar.
7. **IEDB Terms v3.** Dominio público / CC BY 4.0 *con reserva*: el submitter puede reclamar copyright o patente sobre su porción; NIAID no evalúa esas pretensiones.
8. **iReceptor noticia 23-08-2026.** Cobro a usuarios comerciales «durante el verano de 2026»; académicos gratis «at this time». El «at this time» es vigencia precaria, no licencia estable.

Ninguna de esas cláusulas autoriza un sistema asistencial, una recomendación de profilaxis o una validación clínica del array 1×25.  
Si el manuscrito futuro dice que «se apoya en repositorios internacionales de inmunología», un revisor pedirá *qué cláusula permite el uso pretendido*. Hoy esa frase no tiene soporte.

**Lo que resiste:** uso de investigación sobre el objeto *propio* de cada fuente, dentro de su acuerdo, sin pretensión asistencial.  
**Lo que colapsa:** tratar el inventario como banco de contrastación clínica del centinela.

---

## I.4 Descarga abierta frente a acreditación

**Veredicto: resiste la clasificación del inventario; colapsa cualquier lista plana de «once repositorios descargables».**

Sin comité / sin acreditación (norma leída):

- R07 IEDB (export semanal)
- R08 OAS (csv.gz / wget)
- R10 FlowRepository *si el experimento es público*
- R11 VDJdb (web/GitHub; licencia no leída)
- R01 ImmPort *Shared Data* tras registro + acuerdo
- R06 TrialShare *estudios publicados* tras cuenta + Terms
- R02 ImmuneSpace según portada (el primario ImmPort sigue 2.5)
- R04 USIDNET *agregados web*, no el microdato a medida
- R09 iReceptor: parcial, según repositorio miembro

Con comité, contrato o acreditación:

- R03 ESID — proyecto + Steering Group, o ser centro
- R05 REDIP — ficha + compromiso de confidencialidad + rol RePER
- R04 USIDNET — query a Steering Committee para microdatos; IRB para enrolar
- R06 — muestras (OSRP + MTA + IRB/exención)
- R01 — *controlled data*

REDIP está en España y no es abierto. Presentarlo junto a IEDB como «repositorios que podemos cargar» oculta la diferencia jurídica.

---

## I.5 ImmPort no está auditado estudio a estudio

**Veredicto: no demostrado** que ImmPort contenga el episodio de las semillas.

Hechos leídos: portal de inmunología; >1.400 estudios; liberación mensual; Shared vs Controlled.  
Hecho no leído: qué `SDY` cubren profilaxis antiinfecciosa en IS farmacológica no trasplante, en adultos con neoplasia hematológica o en la población de Fase II.

Sin esa auditoría, ImmPort es un *candidato de búsqueda*, no una fuente.  
Afirmar cobertura por el nombre del portal es inferencia. Está prohibida.

ImmuneSpace añade una capa (vacunación/sistemas) y hereda ImmPort. Tampoco sustituye la auditoría por estudio.

---

## I.6 Dos USIDNET bajo un nombre

**Veredicto: colapsa si se cita «USIDNET» sin versión.**

- **v1:** consentimiento; datos validados desidentificados; query por pregunta; acuerdo 2019 contra incidencia/prevalencia y contra minería del archivo.
- **v2 (descripción 2025 / enrolamiento desde ago-2024 en un sitio):** extracción EPIC, waiver of consent, doble des-ID; 1.145 pacientes en esa descripción.

No se ha leído un Data Use Policy v2 que derogue el acuerdo 2019.  
No se afirma que los agregados web sean v1, v2 o una mezcla.  
Citar USIDNET como censo norteamericano de IEI *usable para prevalencia* contradice el texto de 2019 todavía en mano.

---

## I.7 Estadística de registro frente a invariantes del formalismo

**Veredicto: colapsa como primitiva; resiste como referencia externa tipada si se declara la frontera.**

ESID, USIDNET y REDIP producen, por diseño, recuentos, historias naturales y agregados.  
USIDNET 2019 **prohíbe** concluir incidencia/prevalencia.  
El formalismo admite estadística de terceros y la prohíbe como primitiva del estado \(a_{1j}\).

Enlace: un porcentaje ESID no puede ser el valor de un elemento del array. Puede, como máximo, citarse en el plano consecuencial (Π4) *si* el autor autoriza esa fuente y se declara como medida externa.  
Hoy no hay autorización. Hoy no hay métrica de «aumento de criterios internacionales» ligada a ninguno de los once.

A4 del flujo («¿aumentan criterios clínicos medibles?») **sigue vacío**. El inventario no lo llena.

---

## I.8 Autocontención editorial

**Veredicto: colapsa** un manuscrito que remita al lector a ImmPort/ESID/REDIP como prueba del lema clínico.

Condiciones ya fijadas por el autor:

- bibliografía doctrinal limitada a Fundamentos y origen de U;
- el resto, dominio clínico real y autocontenido;
- no bibliografía que desconcierte a una revisión dura.

Consecuencia: si se usa un repositorio, el manuscrito tiene que cerrar *en sí* población, episodio, variables, régimen ético, fecha de corte y operación.  
«Datos de ImmPort» no es un método.  
«30.628 pacientes ESID» no es cobertura del episodio semilla.

Además, varias sumisiones activas (Orientation, non-closure, VII/JMP, JBHI, MIM v0.2.1) no se reabren con este inventario.

---

## I.9 Flancos operativos y de licencia no cerrados

| Flanco | Hecho leído | Riesgo si se ignora |
|---|---|---|
| FlowRepository disco | FAQ: suspensión temporal de *nuevos* experimentos para estabilizar descargas | La vía «anónima y abierta» puede no ser operable el día del uso |
| VDJdb licencia | URL públicos; ToU/SPDX **no leído** | Usarlo es aceptar una licencia no vista |
| IEDB terceros | Terms v3: pretensiones de submitters no evaluadas por NIAID | Un reuso comercial o de producto puede chocar con un submitter |
| iReceptor comercial | Cobro anunciado verano 2026, tarifa «soon» | Un uso no estrictamente académico puede quedar fuera |
| ImmuneSpace vs ImmPort 2.5 | Portada «freely available»; no hay cláusula que anule 2.5 | La capa de curación no lava la prohibición de uso terapéutico |
| REDIP Orphanet | Fichas con fechas distintas (2016 vs contactos IIER posteriores) | No unificar el censo por la ficha Orphanet |

---

## I.10 Jurisdicción

**Veredicto: no demostrado** un régimen único de reutilización.

- ImmPort / ImmuneSpace / TrialShare / IEDB: EE. UU., HIPAA / NIH / dominio público.
- ESID: GDPR, clave en el centro.
- REDIP: LOPDGDD + GDPR + convenio BOE + RePER.
- OAS: CC BY 4.0, Oxford.
- iReceptor: Canadá + red AIRR.

Un trabajo hecho desde España sobre REDIP no se rige por el User Agreement de ImmPort.  
Un export IEDB no se rige por RePER.  
Fusionar jurisdicciones en «datos abiertos de inmunología» es un error de proceso.

---

## I.11 Qué sobreviviría a un revisor duro

**Resiste**, si se mantiene así:

1. El inventario es una lista de *candidatos* con norma citada.
2. Tres clases no se mezclan: registro IEI controlado; ensayo desidentificado con cláusula de no tratamiento; dato molecular/repertorio/FCS.
3. Las semillas no quedan cubiertas por el inventario.
4. A4 (métrica empírica) permanece abierta.
5. G0 permanece: no hay cuenta, no hay DUA, no hay descarga.

**Colapsa** en cuanto se escriba cualquiera de estas frases:

- «Existen repositorios anonimizados de inmunología que ya podemos usar para validar el dominio.»
- «REDIP aporta la cohorte española.»
- «ImmPort cubre el paciente inmunosuprimido.»
- «ESID demuestra el daño de omitir un parámetro.»
- «Los datos son anónimos.»

---

## I.12 Dictamen

El inventario A1 **resiste** como mapa de normas.  
**Colapsa** como base empírica del dominio clínico operativo y como prueba de A4.  
**No demostrado:** existencia de un solo estudio o registro, entre los once, que contenga el episodio de las semillas con variables de profilaxis/riesgo y régimen de reuso compatible con un manuscrito autocontenido.

No se recomienda —y no se ejecuta— alta, DUA ni descarga.

---

# Parte II — Fichas de repositorio

Las fichas copian lo leído el 31-08-2026. No amplían el objeto.

---

## R01 — ImmPort (NIAID / DAIT)

- **URL:** https://www.immport.org/shared/search  
- **Norma:** https://docs.immport.org/home/agreement/  
- **Desidentificación:** https://docs.immport.org/datasubmission/general/deidentification/  
- **Descarga CLI:** https://docs.immport.org/filedownload/tool/  
- **API:** https://www.immport.org/data/query/v3/api-docs  
- **Calendario:** https://docs.immport.org/home/datareleaseschedule/  
- **Objeto:** estudios de inmunología (ensayos, citometría, expresión, resultados). FAQ a mayo 2026: >1.400 estudios, 189k+ sujetos, 179 enfermedades, >5.100 experimentos, >7,6 millones de resultados.  
- **Identificabilidad:** Safe Harbor HIPAA en plantillas; edad >89 → 90; no exporta IDs fuente de sujeto/muestra; GWAS/NGS humano se deriva a dbGaP/SRA.  
- **Cómo cargar:** registro gratuito; aceptar User Agreement; Shared Data por web, API (Bearer) o `downloadImmPortData.sh usuario contraseña ruta|manifiesto`. Controlled: aprobación adicional.  
- **Vigencia:** liberación pública mensual (DR59–DR66 documentados dic-2025 a jul-2026). Cada estudio tiene su propio periodo.  
- **Permitido:** propósito legal no prohibido; redistribución bajo términos conmensurables (cláusula 2.4).  
- **Prohibido / condicionado:** reidentificar (1.1); diagnóstico o decisiones de tratamiento (2.5); sin garantías (2.1).  
- **Jurisdicción:** EE. UU., NIAID/NIH.  
- **Estado:** no adoptado. No auditado `SDY` a `SDY` respecto del episodio semilla.

---

## R02 — ImmuneSpace (HIPC / NIAID DAIT)

- **URL:** http://immunespace.org/  
- **Estándares:** http://immunespace.org/hipc-data-standards/  
- **Objeto:** curación sobre ImmPort + GEO/SRA. Respuestas inmunes humanas a vacunación, infección, medicación, enfermedad inmunomediada. Portada ago-2026: 204 estudios, 89 enfermedades, 5,2M+ ensayos, 45 firmas.  
- **Cómo cargar:** interfaz Data Access; API de publicaciones `https://immunespace.org/api/parse_publications/0/10`. El estudio primario suele existir también como SDY ImmPort.  
- **Vigencia:** HIPC 1 (2010–2015), HIPC 2 (2015–2022), HIPC 3 (2022–2027). Immune Signatures Data Resource: 30 estudios ImmPort, 53 cohortes, 1405 participantes, 24 vacunas (PMC9584267).  
- **Permitido (portada):** «All data is freely available for download and analysis.»  
- **Condicionado:** no se leyó User Agreement propio que anule ImmPort 2.5.  
- **Estado:** no adoptado.

---

## R03 — ESID Registry

- **URL:** https://esid.org/working-parties/registry-working-party/esid-registry/  
- **Norma:** Center Agreement v4.4, 23-08-2024; PIC GDPR v4.0, 19-06-2024  
- **Contacto:** registry@esid.org  
- **Objeto:** registro europeo de IEI/PID. Informe 1994–2024: 30.628 pacientes. Tres niveles de dataset.  
- **Identificabilidad:** seudónimo; clave de reidentificación en el centro documentador. Versión coded: sin nombre, dirección ni fecha de nacimiento completa. PIC: año de nacimiento (mes solo hasta 12 años). Almacenamiento indefinido.  
- **Cómo cargar:** no hay paquete público. Ser centro (acuerdo + IRB local + GDPR) o proyecto aprobado por el Registry Steering Group + contrato.  
- **Vigencia:** cohorte 1994–2024; documentación al menos anual.  
- **Permitido:** análisis en proyectos concretos aprobados; publicaciones que preserven anonimato.  
- **Prohibido:** reidentificar; cesión a terceros no autorizados; aseguradoras; industria salvo consentimiento específico.  
- **Jurisdicción:** UE, GDPR.  
- **Estado:** no adoptado. Objeto ≠ semillas.

---

## R04 — USIDNET (v1 y v2)

- **URL:** https://usidnet.org/registry-data/ — https://www.usidnet.net/  
- **Norma leída:** PI Agreement mayo 2019; página NIAID del recurso; descripción v2 en JHI 2025 / preprint 2025  
- **Contacto:** contact@usidnet.org  
- **Objeto:** PI/IEI en EE. UU. y Canadá.  
- **v1:** consentimiento; datos validados desidentificados; query por pregunta.  
- **v2:** extracción EPIC, waiver of consent, doble desidentificación; 1.145 pacientes en la descripción de ago-2024.  
- **Cómo cargar:** agregados web en tiempo real sin query formal; microdatos mediante Request for Query al Steering Committee; centro enrolador requiere IRB.  
- **Permitido:** responder una pregunta de investigación con los campos que el comité juzgue pertinentes.  
- **Prohibido (acuerdo 2019):** concluir incidencia o prevalencia; minería del archivo completo.  
- **Estado:** no adoptado. No se ha leído un DUA v2 que derogue 2019.

---

## R05 — REDIP / RePER (ISCIII)

- **URL:** https://redipsei.es/  
- **Alojamiento:** https://registroraras.isciii.es/  
- **Alta investigador:** registro.raras@isciii.es ; IIER-ISCIII, Pabellón 11, Avda. Monforte de Lemos 5, 28029 Madrid  
- **Norma:** LOPDGDD 3/2018; GDPR; convenio ISCIII–SEI–AEP–SEPAR BOE-A-2019-12746 y BOE-A-2023-24094; manual RePER V5 2024  
- **Objeto:** Registro Español de Inmunodeficiencias Primarias. Web: pacientes desde enero 1980; origen 1992/1993.  
- **Identificabilidad:** registro de pacientes con consentimiento (paciente/tutor o profesional autorizado). No es dataset abierto desidentificado.  
- **Cómo cargar:** ficha de investigador + compromiso de confidencialidad; extracción a Excel según rol. Investigador de enfermedad: solo sus pacientes. Administrador de enfermedad: todos.  
- **Vigencia:** serie desde 1980; noticia ISCIII 28-02-2024: rediseño y volcado retrospectivo.  
- **Permitido:** uso por profesionales acreditados en el marco RePER/REDIP.  
- **No leído:** licencia de reutilización abierta ni cesión a grupo externo no acreditado.  
- **Jurisdicción:** España.  
- **Estado:** no adoptado. No es descarga abierta. Objeto ≠ semillas.

---

## R06 — ITN TrialShare

- **URL:** https://www.itntrialshare.org/  
- **Política:** https://www.immunetolerance.org/for-researchers/trialshare  
- **Data Sharing Policy:** v2.0, 27-08-2019  
- **Muestras:** submissions@immunetolerance.org (formulario 18-10-2024)  
- **Objeto:** ensayos ITN de tolerancia inmune publicados; protocolos, CRF, laboratorios, inventario de muestras.  
- **Identificabilidad:** Safe Harbor (quitar PII/PHI; enmascarar IDs; desplazar/eliminar fechas; edad >89→90; quitar nombres de centro; enmascarar códigos si <5 por centro); revisión extra de combinaciones raras; revisión de consentimientos locales.  
- **Cómo cargar:** cuenta con correo + Terms of Use para estudios publicados. Muestras: OSRP + MTA + IRB o exención.  
- **Vigencia:** portal público desde agosto 2013; cada estudio al publicar el outcome primario.  
- **Permitido:** reanálisis de ensayos publicados; descarga offline.  
- **Prohibido:** reidentificar; publicar PII/PHI en el sistema.  
- **Estado:** no adoptado. Objeto ≠ semillas por declaración.

---

## R07 — IEDB

- **URL:** https://www.iedb.org/  
- **Términos:** https://www.iedb.org/terms_of_use_v3.php  
- **Export:** https://www.iedb.org/database_export_v3.php  
- **Objeto:** epítopos B/T, ligandos MHC, receptores, antígenos, ensayos de literatura o depósito. No es registro de pacientes.  
- **Cómo cargar:** XML / MySQL / CSV / TSV / XLSX / JSON semanales, sin cuenta.  
- **Licencia de datos:** dominio público gubernamental; CC BY 4.0 declarado desde mayo 2017; citar IEDB.  
- **Reserva:** material de terceros puede estar bajo copyright o patente del submitter; NIAID no evalúa esas pretensiones.  
- **Herramientas:** académicas abiertas; uso comercial de *tools* (no de datos) con licencia aparte.  
- **Estado:** no adoptado. No se ha descargado el export.

---

## R08 — OAS (Observed Antibody Space, OPIG Oxford)

- **URL:** https://opig.stats.ox.ac.uk/webapps/oas  
- **Documentación de descarga:** https://opig.stats.ox.ac.uk/webapps/oas/documentation/  
- **Objeto:** repertorios BCR anotados. Portada: >1.000 millones de secuencias, >80 estudios. Un resumen OPIG 2023 cita ~2,4×10⁹ unpaired y 1,5×10⁶ paired (cifras de fuentes distintas; no unificadas).  
- **Cómo cargar:** búsqueda + data-units `.csv.gz` o `bulk_download.sh` (wget). Volumen total declarado >700 GB.  
- **Licencia (portada):** CC BY 4.0.  
- **Vigencia:** actualización continua.  
- **Estado:** no adoptado.

---

## R09 — AIRR Data Commons + iReceptor Gateway

- **Gateway:** https://gateway.ireceptor.org  
- **Estándar:** https://docs.airr-community.org/  
- **Noticias:** https://gateway.ireceptor.org/news  
- **Objeto:** repositorios distribuidos de BCR/TCR que implementan ADC API. Metadatos de estudio / sujeto desidentificado / muestra / enfermedad. Altas T1D documentadas en 2025–2026 (p. ej. 280M TCR / 2072 repertorios; 325M TCR / 805 sujetos — cifras de las noticias, no recontadas aquí).  
- **Cómo cargar:** cuenta en la Gateway; consulta por metadatos; ADC API. Algunos repositorios exigen `client_name` / secreto o UMA 2.0.  
- **Vigencia:** vivo. Noticia 23-08-2026: cobro a comerciales en verano 2026; académicos gratis «at this time».  
- **Estado:** no adoptado. Acceso no uniforme.

---

## R10 — FlowRepository (ISAC / ICCS / ESCCA)

- **URL:** http://flowrepository.org/  
- **Guía:** http://flowrepository.org/quick_start_guide  
- **re3data:** https://doi.org/10.17616/r3r90q  
- **Objeto:** FCS anotados MIFlowCyt ligados a manuscritos.  
- **Identificabilidad:** des-ID de keywords FCS no esenciales, preferible en local antes de subir.  
- **Cómo cargar:** descarga anónima de experimentos *públicos* (web, FlowRepositoryR, plugin FlowJo). Registro OpenID solo para depositar. Privados: máximo 1 año o hasta publicar.  
- **Hecho operativo:** FAQ con suspensión temporal de creación de experimentos nuevos por falta de espacio, para estabilizar descargas existentes. No se leyó fecha de levantamiento.  
- **Estado:** no adoptado. Operabilidad de descarga a verificar el día que se autorice un uso.

---

## R11 — VDJdb

- **URL:** https://vdjdb.cdr3.net  
- **Código:** https://github.com/antigenomics/vdjdb-db  
- **Descripción:** NAR 2018, PubMed 28977646  
- **Objeto:** TCR con especificidad antigénica conocida (CDR3, epítopo, MHC, método).  
- **Cómo cargar:** navegador o clon del repositorio GitHub.  
- **Licencia:** **no leída** en esta pasada. No se afirma CC, MIT ni dominio público.  
- **Estado:** no adoptado. Cualquier uso exige leer la licencia antes.

---

# Parte III — Exclusiones y huecos (sin rellenar)

No se listan como específicos de inmunología, y no se ha leído su norma en esta orden: MIMIC, SIDIAP, CMBD, OpenSAFELY, BIFAP, UK Biobank general.

Existen como clase, norma no transcrita aquí: UKPIN/UKPID, CEREDIH, LASID, J-PID, red Jeffrey Modell, HCA/CELLxGENE (compartimento inmune).

Huecos internos: auditoría SDY de ImmPort; ToU de VDJdb; DUA v2 de USIDNET; cláusula ImmuneSpace frente a ImmPort 2.5; tarifa iReceptor comercial.

---

# Parte IV — Cierre

| Pregunta | Respuesta en este corte |
|---|---|
| ¿Hay repositorios de inmunología con norma leíble? | Sí. Once fichados. |
| ¿Hay datos «anonimizados» en un solo sentido jurídico? | No. |
| ¿Hay descarga abierta del episodio de las semillas? | No demostrado. |
| ¿Hay fuente española abierta de IDP? | No. REDIP es RePER con acreditación. |
| ¿Alguna fuente autoriza uso asistencial? | ImmPort 2.5 lo prohíbe de forma expresa. Ninguna otra lo autoriza en el texto leído. |
| ¿Se ha adoptado alguna? | No. |
| ¿Siguiente paso ejecutado? | Ninguno. G0 sigue cerrado. |

Fin del informe. El alta, el DUA o la descarga no salen de este archivo.
