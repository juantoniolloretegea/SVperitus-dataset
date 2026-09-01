# Expediente D0 — Auditoría material de estudios candidatos, primera ronda

**Versión:** 0.1  
**Corte:** 31 de agosto de 2026  
**Director:** Juan Antonio Lloret Egea  
**Estatuto:** respaldo interno append-only; candidato no adoptado  
**Puerta:** D0/D0-L abiertas  
**Autorización asistencial:** ninguna  
**Cuentas creadas:** ninguna  
**Microdatos descargados:** ninguno  

---

## 1. Objeto y límite

Este expediente conserva la primera auditoría a nivel de **estudio concreto y versión pública declarada** dentro del proceso de constitución gradual del dominio médico de inmunología.

No constituye:

1. el dominio clínico completo de inmunología;
2. una ontología clínica;
3. una selección definitiva de parámetros, entidades o fuentes;
4. una validación biomédica o asistencial;
5. una autorización para diagnóstico, tratamiento, profilaxis o seguimiento;
6. una proyección a matrices, arrays, lenguaje formal, IR o implementación;
7. una modificación del flujo gobernado ni de los documentos doctrinales.

Los estudios examinados son **testigos de materialidad y de límites**, no fronteras del dominio. IMMUNO-1 e IMMUNO-2 no se utilizan como criterio de inclusión ni como medida de exhaustividad.

La unidad auditable de esta ronda es:

> **estudio × versión pública × población × operación declarada × variables y desenlaces declarados × paquete material × derechos de uso**

La descripción de un repositorio, una nota de liberación y una publicación no acreditan por sí solas el contenido efectivo del paquete depositado.

---

## 2. Reglas de decisión

### 2.1. Estados D0

| Código | Condición | Consecuencia permitida |
|---|---|---|
| `D0-E` | Evidencia material adecuada, accesible y versionada para el recorte y la operación declarados | Puede iniciarse la auditoría del diccionario y la correspondencia paramétrica |
| `D0-R` | Conocimiento clínicamente justificado sin datos adecuados localizados | Se conserva como residual empírico; no se elimina por falta de observabilidad |
| `D0-F` | Sólo existe posibilidad de demostración formal o metodológica | No puede presentarse como validación biomédica ni asistencial |
| `D0-B` | Acceso, licencia, granularidad, materialidad o calidad incompatibles con la operación declarada | El uso queda bloqueado para esa fuente, versión y operación |

Los estados pertenecen a una fuente, versión, población y operación. No son propiedades eternas del estudio ni del conocimiento médico.

### 2.2. D0-L

D0-L debe comprobar separadamente:

1. derecho de consulta o acceso;
2. derecho de tratamiento para la finalidad declarada;
3. derecho de redistribución;
4. elegibilidad para que una unidad de IA de terceros vea los datos;
5. restricciones de entorno seguro, residencia o credencial;
6. prohibiciones de reidentificación y combinación de conjuntos.

La ausencia de autorización expresa para IA de terceros se registra como **D0-L no superada**. No se reescribe automáticamente como prohibición si la norma no la contiene.

### 2.3. Separaciones obligatorias

Se mantienen sin fusión:

- conocimiento clínico profesional;
- variable declarada;
- dato realmente depositado;
- estado del episodio;
- publicación científica;
- metadatos del repositorio;
- paquete descargable;
- autorización jurídica de uso;
- autorización asistencial.

Asimismo:

- dato ausente no equivale a observación inadmisible;
- observación inadmisible no equivale a conocimiento no constituido;
- disponibilidad de una variable no autoriza su interpretación en otra población;
- cobertura de un estrato no equivale a cobertura del dominio;
- farmacovigilancia no prueba causalidad, incidencia ni riesgo individual;
- una fuente molecular no reconstruye por sí sola una trayectoria clínica.

---

## 3. Adversarial previa del expediente

La adversarial se realizó antes de fijar esta versión. Su objeto fue determinar si el expediente podía conservarse como respaldo sin aparentar una validación inexistente.

### 3.1. Ataque sanitario, clínico y médico

| Ataque | Resultado | Corrección incorporada |
|---|---|---|
| Convertir unos pocos estudios en representación del dominio completo | Colapsa | Los estudios se declaran testigos parciales; el dominio permanece abierto |
| Usar variables vacunales, serológicas o de trasplante fuera de su población y protocolo | Colapsa | Toda afirmación queda ligada a estudio, población, intervención y ventana |
| Tratar la existencia del dato como autorización clínica | Colapsa | Se separan evidencia de investigación y autorización asistencial |
| Inferir consecuencias clínicas individuales desde agregados o señales | Colapsa | No se aceptan causalidad, incidencia ni riesgo individual sin diseño adecuado |
| Omitir conocimiento profesional porque no aparece en un repositorio | Colapsa | La falta de datos no elimina el conocimiento; podrá conservarse como D0-R cuando el corpus clínico lo justifique |

### 3.2. Ataque de ingeniería de procesos

| Ataque | Resultado | Corrección incorporada |
|---|---|---|
| Confundir descripción del estudio con archivos depositados | Colapsa | La materialidad exige paquete, fichero, diccionario, versión y recuentos |
| Confundir cuenta gratuita con uso irrestricto | Colapsa | D0-L descompone acceso, tratamiento, redistribución e IA de terceros |
| Dar por inspeccionado un paquete no abierto | Colapsa | Todos los paquetes no inspeccionados quedan expresamente abiertos o bloqueados en este corte |
| Fusionar identificadores de repositorios heterogéneos | Colapsa | Se conservan nombre, versión y accession de cada fuente |
| Reescribir entradas previas al corregirlas | Colapsa | Las correcciones se añaden; no sustituyen registros anteriores |

### 3.3. Ataque lógico enlazado

| Ataque | Resultado | Corrección incorporada |
|---|---|---|
| Armonizar por aritmética poblaciones cribadas, asignadas, vacunadas y analizadas | Colapsa | Cada N queda tipado por función y fuente |
| Suponer que publicación, nota de release y paquete se acreditan mutuamente | Colapsa | Se conservan como tres capas independientes |
| Convertir D0-L no superada en prohibición no escrita | Colapsa | Se diferencia «no comprobado» de «prohibido» |
| Tratar `Assays: None` como prueba de ausencia clínica absoluta | Colapsa | Se registra como metadato de la nota de liberación; el paquete sigue pendiente |
| Proyectar esta ronda a una formalización o composición | Colapsa | La ronda termina en D0/D0-L; no entra en transducción ni composición |

### 3.4. Veredicto adversarial

**Pasa con correcciones incorporadas.** Es admisible como expediente interno de respaldo. No pasa como validación del dominio, evidencia asistencial, catálogo clínico constituido ni autorización de procesamiento por IA.

---

## 4. Estudios candidatos auditados

### 4.1. SDY3324 — ACV01

**Objeto declarado.** Vacunación adicional frente a SARS-CoV-2 en personas con enfermedades autoinmunes tratadas con inmunosupresores y respuesta serológica previa negativa, subóptima o baja. Cohortes definidas por micofenolato/ácido micofenólico, metotrexato o terapia de depleción de linfocitos B.  
**Registro:** NCT05000216.  
**Liberación pública examinada:** ImmPort DR60.  
**Publicación asociada:** JCI Insight, DOI `10.1172/jci.insight.191266`.  
**Desenlace primario publicado:** cambio de anticuerpos frente al dominio de unión al receptor de Wuhan-Hu-1 a las cuatro semanas.  
**Seguimiento secundario publicado:** acontecimientos adversos, COVID-19 y actividad de la enfermedad autoinmune hasta 48 semanas.

#### Poblaciones tipadas

| N | Función documental | Fuente pública |
|---:|---|---|
| 279 | personas cribadas en la etapa 1 | Publicación |
| 148 | asignadas a cohorte inmunosupresora: 25 MMF/MPA + 28 MTX + 95 BCDT | Publicación y DR60 |
| 140 | vacunadas en el momento basal: 82 BNT162b2 + 48 mRNA-1273 + 10 Ad26.COV2.S | Publicación |
| 141 | suma de poblaciones analíticas del resumen: 22 + 26 + 93 | Resumen de la publicación |

La familia de discrepancias es **asignada/vacunada/analizada**, no únicamente 140/141. No se infiere la causa de las diferencias 25→22, 28→26, 95→93 ni 140↔141. Resolverlas exige el paquete, el diagrama de flujo de participantes y las reglas analíticas efectivamente depositadas.

#### Tres capas independientes

1. La publicación declara que los datos son accesibles en ImmPort bajo SDY3324.
2. DR60 declara 148 sujetos, `Assays: None` y `Clinical Assessments: None`.
3. El paquete SDY3324 no ha sido inspeccionado.

Ninguna capa acredita materialmente a las otras.

**Estado:** no D0-E; D0-B en este corte por materialidad no inspeccionada y operación limitada a lectura pública. D0-L no superada.  
**No cierra:** vacunación viva, ventanas ajenas al protocolo, profilaxis frente a *Pneumocystis jirovecii*, umbrales universales de inmunosupresión, G1 ni configuraciones prototipo.

### 4.2. SDY3274 — ARTIST / ITN524ST / CTOT-12

**Objeto declarado.** Estudio observacional multicéntrico de receptores adultos de trasplante renal entre uno y cinco años después del trasplante, con distintos regímenes inmunosupresores.  
**Registro:** NCT01516177.  
**Liberación:** ImmPort DR60.  
**Sujetos declarados:** 250.  
**Procedimientos descritos:** tres visitas anuales, datos clínicos, sangre periférica/PBMC, RT-qPCR dirigida a `IGKV1D-13` y `IGKV4-1`, y citometría multiparamétrica de subpoblaciones B.

La nota pública describe esas medidas, pero enumera `Assays: None` y `Clinical Assessments: None`. Esta divergencia impide identificar, sin abrir el paquete, qué variables y resultados fueron efectivamente depositados.

**Estado:** no D0-E; D0-B en este corte por falta de inspección material y diccionario. D0-L no superada.  
**Uso potencial no adoptado:** tolerancia en trasplante y efectos de la inmunosupresión. No representa por sí solo inmunología del trasplante ni autoriza decisiones de minimización terapéutica.

### 4.3. SDY218 — CoFAR3, inmunoterapia oral con huevo

**Objeto declarado.** Ensayo pediátrico aleatorizado de inmunoterapia oral con huevo frente a placebo, con escalado, mantenimiento y provocaciones alimentarias para distinguir desensibilización y tolerancia clínica según el protocolo.  
**Registro:** NCT00461097.  
**Liberación inicial/actualización pública:** DR3, actualizado en DR58 según la ficha pública.  
**Duración declarada:** hasta 48 meses.

La existencia de provocaciones alimentarias y seguimiento convierte el estudio en candidato clínico relevante para alergia alimentaria. No se han inspeccionado el paquete, el diccionario, las definiciones de acontecimientos adversos ni los datos individuales.

**Estado:** no D0-E; D0-B en este corte por paquete no inspeccionado. D0-L no superada.  
**Límite:** no extrapolar a otros alérgenos, edades, pautas o mecanismos de reacción.

### 4.4. SDY621 — registro ADRN-02 de dermatitis atópica

**Objeto declarado.** Registro clínico multicéntrico para estudiar marcadores genéticos asociados a susceptibilidad a infecciones en dermatitis atópica y facilitar la identificación de participantes para futuros estudios.  
**Registro:** NCT01494142.  
**Liberación examinada:** DR65.  
**Sujetos declarados:** 3.611.  
**Metadatos de liberación:** `Assays: None`; `Clinical Assessments: None`.

La cardinalidad no demuestra que existan variables operativas, desenlaces infecciosos o diccionario utilizable. Tampoco demuestra cobertura de la inmunología de barrera.

**Estado:** no D0-E; D0-B en este corte por materialidad no demostrada. D0-L no superada.

### 4.5. SDY1845 — ADRN-09, dupilumab y la interfaz huésped-microbiota

**Objeto declarado.** Ensayo multicéntrico, aleatorizado, doblemente enmascarado y controlado con placebo sobre seis semanas de dupilumab en adultos con dermatitis atópica moderada o grave, seguido de extensión abierta.  
**Liberación examinada:** DR65.  
**Elementos descritos:** acontecimientos adversos, medicación concomitante, historia clínica, exploración y gravedad de la dermatitis; sangre, orina, hisopos, tiras cutáneas y biopsias; medidas de barrera y comunidad microbiana.

La descripción ofrece una trayectoria potencialmente rica, pero el portal de descubrimiento consultado no mostró archivos descargables y el paquete de ImmPort no fue inspeccionado.

**Estado:** no D0-E; D0-B en este corte por falta de comprobación material. D0-L no superada.  
**Límite:** el estudio no constituye por sí solo el dominio de alergia, inmunidad de barrera ni microbiota.

### 4.6. SDY1414 — CTOTC-04, aloanticuerpos en trasplante cardiaco pediátrico

**Objeto declarado.** Estudio observacional multicéntrico de resultados en receptores pediátricos de trasplante cardiaco sensibilizados y no sensibilizados, con seguimiento antes y después del trasplante.  
**Registro:** NCT01005316.  
**Liberación examinada:** DR35.  
**Sujetos declarados:** 290.  
**Ensayos declarados:** 2.558 muestras Luminex xMAP.  
**Datos clínicos descritos:** exploración, pruebas rutinarias, acontecimientos adversos y graves, biopsias cuando estuvieran disponibles y visitas hasta tres años.

La nota de liberación declara ensayos, pero `Clinical Assessments: None`. No se ha verificado la correspondencia entre muestras, sujetos, visitas, aloanticuerpos, rechazo, pérdida del injerto y desenlaces.

**Estado:** no D0-E; D0-B en este corte por diccionario y paquete no inspeccionados. D0-L no superada.  
**Límite:** no autoriza decisiones sobre compatibilidad, desensibilización o inmunosupresión.

### 4.7. SDY1039 — SCOT, esclerosis sistémica

**Objeto declarado.** Ensayo multicéntrico, aleatorizado y abierto en esclerosis sistémica grave, comparando inmunosupresión intensa con trasplante autólogo de progenitores hematopoyéticos frente a ciclofosfamida intravenosa mensual.  
**Registro:** NCT00114530.  
**Liberación examinada:** DR25.  
**Sujetos declarados en ImmPort:** 75.  
**Seguimiento previsto:** hasta 72 meses después de la aleatorización.  
**Metadatos de liberación:** `Assays: None`; `Clinical Assessments: None`.

Las publicaciones asociadas declaran que los datos del ensayo son accesibles en ImmPort, pero el paquete no fue inspeccionado en esta operación.

**Estado:** no D0-E; D0-B en este corte por falta de verificación material. D0-L no superada.  
**Límite:** no se extraen reglas terapéuticas ni umbrales de selección.

### 4.8. RAVE en ITN TrialShare — candidato externo a la serie SDY de esta ronda

**Objeto declarado.** Ensayo aleatorizado, doblemente enmascarado y controlado, con 197 participantes, que comparó rituximab frente a ciclofosfamida para inducción de remisión en vasculitis asociada a ANCA grave. TrialShare declara ofrecer datos clínicos subyacentes, código analítico y documentación de estudios publicados.

El acceso exige cuenta. La política publicada restringe la distribución a usuarios no autorizados y no representa los datos como adecuados para informar diagnóstico o decisiones de tratamiento. No se ha inspeccionado el paquete ni confirmado la vigencia de todas las condiciones publicadas.

**Estado:** candidato de alta prioridad material; no D0-E en esta operación. D0-B en este corte por acceso y paquete no inspeccionado. D0-L no superada.

---

## 5. Matriz comparativa del corte

| Estudio | Recorte provisional | Población declarada | Trayectoria clínica descrita | Materialidad pública comprobada | D0 | D0-L |
|---|---|---:|---|---|---|---|
| SDY3324 | Autoinmunidad, inmunosupresión y vacunación | 279/148/140/141, tipados | Sí | Publicación y metadatos; paquete no | D0-B en este corte | No superada |
| SDY3274 | Trasplante renal y tolerancia | 250 | Sí, tres visitas anuales | Descripción; metadatos discordantes; paquete no | D0-B en este corte | No superada |
| SDY218 | Alergia alimentaria e inmunoterapia oral | No fijado en esta ronda | Sí, hasta 48 meses | Protocolo/ficha; paquete no | D0-B en este corte | No superada |
| SDY621 | Dermatitis atópica e infección | 3.611 | Registro declarado | Sólo ficha; sin ensayos/evaluaciones enumerados | D0-B en este corte | No superada |
| SDY1845 | Dermatitis atópica, dupilumab y barrera | No fijado en esta ronda | Sí, hasta día 112 | Descripción; archivos no comprobados | D0-B en este corte | No superada |
| SDY1414 | Trasplante cardiaco pediátrico y aloanticuerpos | 290 | Sí, hasta tres años | 2.558 Luminex declarados; diccionario no | D0-B en este corte | No superada |
| SDY1039 | Esclerosis sistémica y trasplante autólogo | 75 | Sí, hasta 72 meses | Publicaciones/ficha; paquete no | D0-B en este corte | No superada |
| RAVE | Vasculitis ANCA e inmunomodulación | 197 | Sí, 18 meses publicados | Portal declara datos y código; paquete no | D0-B en este corte | No superada |

**Resultado:** cero estudios pasan D0-E y cero pasan D0-L en esta operación. No se asigna D0-R hasta que exista un corpus clínico profesional que justifique el conocimiento residual. No se asigna D0-F porque esta ronda no construye una demostración formal.

---

## 6. D0-L y consecuencias operativas

| Fuente | Acceso declarado | Redistribución | IA de terceros | Uso clínico/asistencial |
|---|---|---|---|---|
| ImmPort | Registro/autenticación para descarga; control adicional en determinados conjuntos | Permitida bajo términos equivalentes, según el acuerdo general | No comprobada expresamente | El acuerdo no representa los datos como adecuados para diagnóstico o decisiones de tratamiento |
| ITN TrialShare | Cuenta gratuita para estudios liberados | Prohibida a usuarios no autorizados según la política publicada | No comprobada expresamente | No representados como adecuados para diagnóstico o tratamiento |
| PhysioNet/MIMIC, como control jurídico | Credencial, formación y acuerdo del recurso | No permitida a terceros sin credencial propia | Prohibido compartir mediante API o servicios externos de modelos de lenguaje | Investigación bajo licencia; no fuente inmunológica específica |

Consecuencia: ningún microdato de estas fuentes puede introducirse en una unidad externa de IA hasta superar D0-L para la fuente, versión, estudio y operación concreta.

---

## 7. Consecuencias de una falsa cobertura

Estas consecuencias están formuladas como riesgos de proceso y seguridad; no son estimaciones de incidencia ni atribuciones causales sobre pacientes concretos.

1. **Falso D0-E.** Declarar evidencia material sin abrir el paquete puede constituir relaciones clínicas sobre variables inexistentes, no enlazables o sin unidad verificable.
2. **Población equivocada.** Trasladar una regla entre alergia pediátrica, autoinmunidad, trasplante, error innato de la inmunidad o inmunosupresión oncohematológica puede omitir modificadores críticos y producir una recomendación inaplicable.
3. **Temporalidad falsa.** Mezclar fecha absoluta, día relativo del estudio, ventana de exposición y orden de intervenciones puede invertir la relación entre inmunosupresión, vacunación, infección y respuesta.
4. **Falsa individualización.** Convertir agregados o asociaciones de cohorte en consecuencias individuales puede ocultar un dato singular clínicamente decisivo.
5. **Iatrogenia informativa.** Presentar una salida investigadora como orientación asistencial puede inducir al experto a confiar en una cobertura que el sistema no posee.
6. **Pérdida de trazabilidad.** Fusionar publicación, release y paquete impide reconstruir qué afirmación procedía de cada capa.
7. **Incumplimiento jurídico.** Introducir datos sujetos a cuenta, DUA o entorno seguro en una IA de terceros puede vulnerar condiciones de acceso y confidencialidad.
8. **Ocultación del residual.** Excluir conocimientos no observados en los repositorios puede borrar precisamente los supuestos raros de mayor consecuencia clínica.

La respuesta segura en este corte es abstenerse de adoptar parámetros o reglas y declarar el bloqueo material correspondiente.

---

## 8. Flancos todavía abiertos

1. Inspección autorizada de los paquetes y diccionarios de los estudios candidatos.
2. Resolución documental de las poblaciones asignada, vacunada y analizada de SDY3324.
3. Verificación por fichero de sujeto, intervención, evaluación, laboratorio, acontecimiento adverso, medicación concomitante, visita, muestra y desenlace.
4. Vigencia y alcance actual de la política de ITN TrialShare.
5. Elegibilidad expresa de IA de terceros en ImmPort, TrialShare, Vivli y cualquier entorno seguro.
6. Cohortes materiales de errores innatos de la inmunidad con trayectoria clínica y acceso compatible.
7. Cobertura clínica de inmunodeficiencias secundarias, inmunohematología, inmunología reproductiva, inmunología tumoral, autoinflamación, complemento, hipersensibilidades, inmunidad de mucosas y barrera, inmunoterapia, trasplante y complicaciones infecciosas, sin convertir esta enumeración en taxonomía adoptada.
8. Separación y enlace futuro entre datos clínicos, moleculares, nomenclatura y farmacovigilancia.
9. Corpus profesional que permita asignar D0-R sin usar ausencia de datos como criterio clínico.

D0 y D0-L permanecen abiertas. No existe todavía correspondencia completa y auditada entre entidad, parámetro, episodio, fuente, dato, consecuencia y desenlace.

---

## 9. Próxima operación permitida

Sin adoptar estudios ni descargar microdatos, la siguiente operación es preparar la solicitud de inspección material por estudio, especificando antes:

- finalidad de investigación;
- versión y accession;
- ficheros y diccionarios requeridos;
- campos mínimos de población, intervención, temporalidad y desenlace;
- régimen de acceso, redistribución y uso por IA;
- registro local de procedencia y huella;
- criterio de salida D0-E, D0-R, D0-F o D0-B.

La creación de cuentas, firma de acuerdos, descarga de paquetes o procesamiento de microdatos requiere autorización independiente del Director.

---

## 10. Procedencia append-only

Las siguientes entradas se conservan como fuentes independientes. Su incorporación no fusiona autorías ni reescribe el expediente D0 v0.1.

| Entrada | Función | SHA-256 |
|---|---|---|
| `registro-d0-cobertura-dominio-inmunologia-2026-08-31-v0.1.md` | Registro rector previo de D0 | `3412cd3d35d0018b47f122caa54fe23226504d73f47c15c7efc3dbd4772fdce5` |
| `ae816e80-9c35-4ad5-8d9a-710f6dcaa486.md` | Estudio de repositorios y normas | `15f3c4550dd992b89d2fa3906b58efef4106b32acbe2fb3585a7eed1ba3d659f` |
| `c19e3012-c2b4-4b26-a4d0-59d91193f276.md` | Adversarial y fichas A1 de Grok | `e92f6cf87ee0d224898ff77acb3446489b36572bbd0045bceb838c1c0c424974` |
| `0b00c161-f446-456b-b6fa-c9fa142cca2d.md` | Lectura pública independiente de SDY3324 | `252b7d7b5b4e06d9f9a916e3e90a08855d6fbed62a48c6c68ce4d2a37e078e8c` |
| `ae063050-ae6f-4771-907b-b11cc2f50629.md` | Revisión adversarial de Grok sobre la nota SDY3324 | `0206c87f4a56b7bc643ea2160fdb4e0e305da81bf1e1f0da033132b5bd74c074` |
| `flujo-gobernado-dominio-inmunologia-v3.html` | Flujo rector de trabajo | `b55faad4b900c6a01966c1588b4abeba3e7d1505a7fd5231b1338ab31d4bd23e` |

### Régimen de voces

- Las afirmaciones de Watson se registran como auditoría de esta unidad.
- Las afirmaciones de Grok se conservan como lectura o adversarial independiente.
- La coincidencia entre unidades aumenta control cruzado, pero no convierte una afirmación en dato clínico.
- Sólo el Director puede adoptar una conclusión, autorizar un acceso o cambiar el flujo.

---

## 11. Fuentes primarias públicas

### ImmPort y estudios

- Acuerdo de usuario de ImmPort: <https://docs.immport.org/home/agreement/>
- Opciones de descarga y contenido de los paquetes: <https://docs.immport.org/download/options/>
- Notas de DR60, SDY3324 y SDY3274: <https://docs.immport.org/data/release/notes/DR60_DataRelease/>
- Publicación ACV01: <https://insight.jci.org/articles/view/191266>
- Registro NCT05000216: <https://clinicaltrials.gov/study/NCT05000216>
- DR65, SDY621 y SDY1845: <https://docs.immport.org/data/release/notes/DR65_DataRelease/>
- DR4, SDY218: <https://docs.immport.org/data/release/notes/DR4_DataRelease/>
- Registro NCT00461097: <https://clinicaltrials.gov/study/NCT00461097>
- DR35, SDY1414: <https://docs.immport.org/data/release/notes/DR35_DataRelease/>
- DR25, SDY1039: <https://docs.immport.org/data/release/notes/DR25_DataRelease/>
- Registro NCT00114530: <https://clinicaltrials.gov/study/NCT00114530>

### TrialShare y control jurídico

- Descripción institucional de TrialShare: <https://www.immunetolerance.org/for-researchers/trialshare>
- RAVE y acceso a los datos subyacentes: <https://www.immunetolerance.org/news-immunetolerance-org/itn-achieves-scientific-manuscript-first---provides-open-interactive-access-to-clinical-trial-data-with-new-publication-rituximab-therapy-effective-for-anca-associated-vasculitis>
- Uso responsable de MIMIC con modelos de lenguaje: <https://physionet.org/news/post/llm-responsible-use/>

---

## 12. Cierre

La primera ronda demuestra que existen estudios clínicamente relevantes y potencialmente materiales en varios recortes de inmunología. No demuestra que sus paquetes contengan todas las variables requeridas, que sean componibles entre sí, que cubran el dominio completo ni que puedan ser procesados por una IA de terceros.

El resultado correcto es:

> **cero D0-E; cero D0-L superadas; D0/D0-L abiertas; ninguna adopción; ninguna descarga; ninguna inferencia clínica nueva.**

Este expediente conserva lo comprobado y, con igual importancia, lo que todavía no puede afirmarse.

**Fin de la versión 0.1.**
