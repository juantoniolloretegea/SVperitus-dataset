# Evaluación predecisional del riesgo infeccioso antes de iniciar tratamiento inmunosupresor en adultos

## Descripción clínica, parámetros constitutivos, fuentes de autoridad, interoperabilidad y garantías jurídicas

**Universo clínico:** OP-IMM-001 / Q0 v0  
**Edición:** 1.0 · 3 de septiembre de 2026  
**Ámbito:** personas adultas en quienes se proyecta iniciar tratamiento inmunosupresor  
**Naturaleza:** documento clínico-técnico de referencia; no sustituye la valoración médica, no prescribe tratamiento y no constituye autorización asistencial.

## 1. Finalidad

Este documento describe de forma autosuficiente el conjunto de información que debe estar disponible, identificada y clínicamente contextualizada antes de valorar el riesgo infeccioso asociado al inicio de un tratamiento inmunosupresor en una persona adulta. Su finalidad es evitar que una decisión de elevada trascendencia dependa de datos implícitos, menciones aisladas, códigos descontextualizados o inferencias no verificadas.

La evaluación concluye en un **perfil predecisional estructurado**. Dicho perfil no determina por sí mismo si el tratamiento está indicado, si puede iniciarse, qué prevención debe prescribirse ni cuál es la conducta terapéutica correcta. Es un documento de apoyo para el facultativo responsable y conserva de manera visible los datos desconocidos, contradictorios, desactualizados o no aplicables.

El universo comprende **27 parámetros** agrupados en seis ámbitos clínicos: contexto y autoridad asistencial; exposición prevista; estado inmunitario; barreras y dispositivos; antecedentes asistenciales e infecciosos; y enfermedades o circunstancias modificadoras. No existe una puntuación total ni se admite que un dato favorable compense una carencia crítica.

## 2. Población, momento clínico y exclusiones

### 2.1 Población destinataria

Personas de 18 años o más con una propuesta documentada de tratamiento inmunosupresor sistémico. La fecha de referencia es el momento predecisional inmediatamente anterior a la decisión clínica de inicio. Cada dato conserva su propia fecha, periodo de validez y fuente; no se aplica una antigüedad universal a resultados analíticos, diagnósticos, dispositivos, ingresos o procedimientos.

### 2.2 Exclusiones del alcance

Quedan fuera de este universo, salvo futura constitución expresa:

- población pediátrica;
- trasplante de órgano sólido o de progenitores hematopoyéticos;
- quimioterapia oncohematológica y terapias celulares, incluida CAR-T;
- valoración diagnóstica integral de una inmunodeficiencia;
- selección del inmunosupresor, determinación de dosis o pauta;
- prescripción de profilaxis, vacunación, antimicrobianos o retirada de dispositivos;
- declaración de aptitud general para recibir tratamiento.

Cuando una persona pertenezca a uno de estos ámbitos, el resultado apropiado no es forzar la aplicación, sino declarar la falta de aplicabilidad y remitir a la autoridad clínica correspondiente.

## 3. Forma de valoración

Cada parámetro admite tres conclusiones clínicas documentales:

- **Presente:** la proposición definida para el parámetro está demostrada mediante información suficiente, vigente, aplicable y verificable.
- **Ausente:** existe una revisión suficientemente completa y pertinente que permite negar la proposición; el silencio de la historia clínica nunca basta.
- **Indeterminado:** faltan datos, cobertura, temporalidad, aplicabilidad, verificación o concordancia; también se utiliza ante conflicto no resuelto.

“Presente” no siempre significa enfermedad biológica demostrada. En los parámetros expresamente documentales significa que una condición, un acontecimiento, una autoridad o una restricción constan de forma verificable. Un código diagnóstico aislado, una medicación, una cifra analítica o una frase sin procedencia no adquieren por ello valor probatorio suficiente.

## 4. Los 27 parámetros

### 4.1 Contexto clínico, responsabilidad y condiciones de ejecución

#### 1. Inicio programado del tratamiento inmunosupresor (`PAR-IMMUNO-START-PLAN-DOC-001`)

Determina si existe una fecha o un intervalo de inicio documentado, vigente y vinculado inequívocamente al tratamiento propuesto. Deben constar tratamiento, intención, autor, fecha de emisión, situación del plan, precisión temporal y procedencia. “Presente” exige programación explícita; “ausente” exige una declaración igualmente explícita de que el inicio todavía no está programado. El mero silencio, una prioridad clínica sin fecha, una orden cancelada o un conflicto entre documentos determinan indeterminación. No informa de urgencia, conveniencia ni indicación.

**Relevancia:** fija el momento respecto del cual se juzgan vigencia de analíticas, proximidad de ingresos o procedimientos y posibilidad material de completar evaluaciones.  
**Fuentes:** HL7 FHIR R5 `CarePlan` y `MedicationRequest`; documento profesional que origine la propuesta.

#### 2. Diagnóstico de base vinculado a la propuesta (`PAR-BASE-DX-DOC-001`)

Comprueba que el diagnóstico o problema clínico que motiva la inmunosupresión está documentado, verificado, vigente y enlazado con la propuesta terapéutica. No vuelve a diagnosticar la enfermedad ni valida la indicación. “Ausente” sólo es posible si una fuente profesional declara expresamente que la propuesta no se vincula a una entidad de base; la falta ordinaria de información es indeterminada.

**Relevancia:** la enfermedad de base puede modificar el riesgo infeccioso, la urgencia, la selección de pruebas y la interpretación de antecedentes.  
**Fuentes:** HL7 FHIR R5 `Condition`, `CarePlan` y `MedicationRequest`; diagnóstico emitido por profesional autorizado.

#### 3. Responsable clínico principal del episodio (`PAR-EPISODE-LEAD-DOC-001`)

Identifica al profesional o servicio que conserva la responsabilidad principal del episodio asistencial. Deben constar identidad profesional o institucional, función, periodo de responsabilidad, estado y fuente. Una lista de participantes sin asignación de responsabilidad no basta.

**Relevancia:** impide que una evaluación incompleta quede sin destinatario clínico y delimita quién debe integrar el perfil con la indicación y el plan terapéutico.  
**Fuentes:** HL7 FHIR R5 `Encounter`, `EpisodeOfCare` y `CareTeam`; normativa organizativa y registros asistenciales locales.

#### 4. Participación documentada de Inmunología (`PAR-IMMUNO-PART-DOC-001`)

Registra si el servicio o especialista de Inmunología interviene formalmente en el episodio, con indicación de función, emisor, receptor, fecha y estado de la interconsulta o participación. No presupone que Inmunología sea responsable principal ni transfiere competencias desde otra especialidad.

**Relevancia:** diferencia la responsabilidad asistencial de la función consultiva o interpretativa y evita atribuir a Inmunología decisiones que pertenecen al prescriptor.  
**Fuentes:** HL7 FHIR R5 `ServiceRequest`, `Encounter` y `CareTeam`; registros institucionales de interconsulta.

#### 5. Protocolo local aplicable (`PAR-LOCAL-PROTOCOL-APPLICABLE-001`)

Comprueba la existencia de un protocolo institucional vigente que sea aplicable a la población, tratamiento, indicación, ámbito y fecha del episodio. Deben conservarse título, versión, fecha de vigencia, institución responsable, alcance y localizador. La mera existencia de un protocolo general no demuestra aplicabilidad.

**Relevancia:** las recomendaciones internacionales requieren adaptación a epidemiología, cartera de servicios, resistencias, circuitos de derivación y normativa locales.  
**Fuentes:** protocolo aprobado por la institución competente; EULAR 2022 como orientación clínica suprainstitucional.

#### 6. Restricción material de ejecución (`PAR-EXEC-CONSTRAINT-DOC-001`)

Identifica una limitación vigente y verificada que afecte materialmente a la ejecución: disponibilidad de prueba o fármaco, tiempo, acceso, capacidad del centro, contraindicación logística o requisito regulatorio. Deben constar naturaleza, alcance, responsable, inicio, final previsto y procedencia. No altera los hechos clínicos ni convierte una necesidad no atendible en una necesidad inexistente.

**Relevancia:** permite distinguir incertidumbre clínica de imposibilidad operativa y evita presentar como completa una evaluación que no pudo realizarse.  
**Fuentes:** información institucional verificable, autorización de cartera, farmacia, laboratorio o dirección clínica.

### 4.2 Exposición inmunosupresora prevista

#### 7. Glucocorticoide sistémico incluido en el plan (`PAR-GC-PLAN-SYS-001`)

Determina si la propuesta contiene un glucocorticoide de acción sistémica, conforme a una clasificación farmacológica versionada. Deben constar principio activo, vía, intención, pauta propuesta, fechas, situación de la prescripción y fuente. No se infiere exposición efectiva desde una mera posibilidad ni se calcula con este parámetro dosis equivalente, duración acumulada o riesgo individual.

**Relevancia:** dosis y duración de glucocorticoides forman parte de la valoración de infecciones oportunistas; EULAR señala el beneficio potencial de profilaxis frente a *Pneumocystis jirovecii* en determinados intervalos de prednisolona equivalente, sin que este parámetro importe automáticamente dichos umbrales.  
**Fuentes:** documento de prescripción; clasificador farmacológico institucional; EULAR 2022 sobre cribado y profilaxis de infecciones en enfermedades reumáticas inflamatorias autoinmunes.

### 4.3 Estado inmunitario del huésped

#### 8. Déficit cuantitativo de inmunoglobulina G (`PAR-IGG-DEF-Q-001`)

Compara una medición válida de IgG total en suero o plasma con el intervalo de referencia aplicable al método, población y laboratorio. Deben constar LOINC 2465-3 o equivalencia demostrada, valor, unidad original, espécimen, método, fecha, estado del resultado, intervalo, procedencia y posible administración reciente de inmunoglobulina. “Presente” significa valor inferior al límite aplicable; “ausente”, valor dentro o por encima de dicho límite; cualquier discordancia o intervalo no aplicable determina indeterminación.

No representa competencia humoral específica, causa, repercusión clínica ni indicación de reposición. Un intervalo de otro laboratorio o de otra población no puede trasladarse sin validación.

**Fuentes:** LOINC 2465-3; CLSI EP28; HL7 FHIR R5 `Observation` y `DiagnosticReport`.

#### 9. Ausencia anatómica completa del bazo (`PAR-SPL-ANAT-ABS-001`)

Determina si existe ausencia anatómica completa verificada mediante antecedente quirúrgico, imagen u otra fuente clínica suficiente. Deben conservarse procedimiento, extensión, lateralidad cuando proceda, remanente descrito, fecha, verificación y procedencia. La esplenectomía parcial o una anatomía incierta son indeterminadas. La presencia anatómica permite negar únicamente la ausencia completa; no demuestra función esplénica normal.

**Relevancia:** la asplenia anatómica es una condición clínicamente relevante para prevención de infecciones por microorganismos encapsulados y planificación vacunal, sin que este parámetro prescriba ninguna vacuna.  
**Fuentes:** CDC, *Altered Immunocompetence*; HL7 FHIR R5 `Procedure` y `ImagingStudy`/`DiagnosticReport`.

#### 10. Déficit cuantitativo del recuento absoluto de neutrófilos (`PAR-ANC-DEF-Q-001`)

Compara un recuento absoluto de neutrófilos válido con el intervalo de referencia aplicable. Deben constar LOINC 751-8 o equivalencia demostrada, valor absoluto, unidad, método, fecha, intervalo, calidad y procedencia. El porcentaje de neutrófilos, el recuento leucocitario total o una etiqueta automática de laboratorio no sustituyen el recuento absoluto.

No expresa etiología, función neutrofílica, gravedad, duración ni conducta clínica. Un resultado inferior al intervalo local constituye el estado cuantitativo definido, no una decisión terapéutica.

**Fuentes:** LOINC 751-8; CLSI EP28; HL7 FHIR R5 `Observation` y `DiagnosticReport`.

### 4.4 Barreras, accesos y material implantado

#### 11. Dispositivo intravascular presente (`PAR-IV-DEVICE-PRESENT-001`)

Registra la presencia vigente de un catéter o dispositivo intravascular con tipo, localización, fecha de inserción, finalidad, situación y procedencia. “Ausente” requiere un inventario explícitamente completo y vigente; la ausencia de mención es indeterminada. La presencia no equivale a infección, colonización, disfunción ni indicación de retirada.

**Relevancia:** tipo, localización, duración y manipulación modifican la evaluación del riesgo relacionado con catéteres y la interpretación de episodios infecciosos.  
**Fuentes:** CDC, guía para prevención de infecciones relacionadas con catéter intravascular; HL7 FHIR R5 `DeviceUsage` y `Procedure`.

#### 12. Implante presente (`PAR-IMPLANT-PRESENT-001`)

Registra material implantado vigente —por ejemplo, prótesis o dispositivo— con tipo, localización, fecha, finalidad, revisión, retirada si procede, situación y procedencia. “Ausente” exige inventario clínico suficientemente completo. No presupone infección, fallo, contraindicación ni necesidad de intervención.

**Relevancia:** un implante puede cambiar el significado de bacteriemias previas, procedimientos y planes de seguimiento, pero requiere valoración específica.  
**Fuentes:** HL7 FHIR R5 `Device`, `DeviceUsage` y `Procedure`; documentación quirúrgica institucional.

### 4.5 Antecedentes infecciosos y asistenciales

#### 13. Infección previa causalmente vinculada a ingreso (`PAR-INF-HOSP-HIST-001`)

Determina si un episodio infeccioso verificado fue causa de ingreso hospitalario. Deben constar episodio, diagnóstico o agente cuando esté disponible, localización, fechas, ingreso, relación causal explícita, desenlace y procedencia. La coincidencia temporal entre un código infeccioso y una hospitalización no basta. El diagnóstico principal al alta sólo puede utilizarse si el perfil local lo reconoce como forma válida de atribución.

**Relevancia:** diferencia una infección ambulatoria de un antecedente con repercusión asistencial mayor.  
**Fuentes:** HL7 FHIR R5 `Condition`, `Encounter` y `DiagnosticReport`; informe de alta o documento clínico con atribución expresa.

#### 14. Infección previa causalmente vinculada a soporte orgánico (`PAR-INF-ORGSUP-HIST-001`)

Determina si una infección verificada requirió soporte orgánico, con modalidad, periodo y vínculo causal documentados. Una estancia en cuidados intensivos, monitorización o la palabra “grave” no sustituyen la identificación del soporte ni la atribución a la infección.

**Relevancia:** conserva una dimensión de repercusión distinta del ingreso; puede existir hospitalización sin soporte orgánico.  
**Fuentes:** HL7 FHIR R5 `Encounter`, `Procedure`, `Observation` y documentación clínica de cuidados críticos.

#### 15. Antecedente documentado de infección oportunista (`PAR-OI-DOC-HIST-001`)

Registra un episodio previo verificado que una fuente clínica autorizada ha clasificado expresamente como oportunista, con agente o diagnóstico, localización, contexto del huésped, fecha, sistema de clasificación y versión. No diagnostica oportunismo desde una lista universal de microorganismos ni desde texto libre no tipificado.

**Situación actual:** el tipo está constituido, pero la lista cerrada de clasificaciones admisibles todavía no está aprobada. Hasta entonces, la resolución automática debe permanecer indeterminada.  
**Fuentes:** EULAR 2022; sistemas de clasificación que sean aprobados expresamente para la población y finalidad; HL7 FHIR R5 `Condition` y `DiagnosticReport`.

#### 16. Colonización vigente por microorganismo multirresistente (`PAR-MDRO-COL-DOC-001`)

Compara un hallazgo microbiológico documentado con una tabla versionada de microorganismo y resistencia, y con una ventana temporal igualmente versionada. Deben constar organismo, sitio, condición de colonización —no infección ni contaminación—, método, fenotipo o genotipo, antimicrobianos ensayados, fecha y procedencia. “Ausente” requiere cribado con cobertura declarada suficiente.

**Situación actual:** no se ha aprobado la tabla ni la ventana operativa; el directorio del ECDC orienta hacia fuentes, pero no constituye por sí solo la configuración. Hasta su aprobación, la resolución automática es indeterminada.  
**Fuentes:** ECDC, directorio de prevención y control de resistencia antimicrobiana; EUCAST cuando el perfil local lo adopte; HL7 FHIR R5 `Observation`, `DiagnosticReport` y `Specimen`.

#### 17. Encuentro asistencial agudo dentro de la ventana pertinente (`PAR-ACUTECARE-ENC-HIST-001`)

Registra la existencia de una atención urgente, ingreso agudo o episodio equivalente que intersecta una ventana temporal explícita. Deben constar clase de encuentro, fechas, estado, servicio y motivo documentado. No demuestra infección ni gravedad. “Ausente” exige historia asistencial con cobertura suficiente para la ventana.

**Relevancia:** señala exposición reciente al sistema sanitario y acontecimientos que pueden requerir revisión antes del inicio terapéutico.  
**Fuentes:** HL7 FHIR R5 `Encounter`; registros hospitalarios y de urgencias.

#### 18. Procedimiento invasivo dentro de la ventana pertinente (`PAR-INV-PROC-HIST-001`)

Registra un procedimiento invasivo verificado cuyo periodo intersecta una ventana temporal explícita. Deben constar identidad, invasividad, estado, fecha, indicación documentada y procedencia. No prueba infección ni exposición microbiológica. La ausencia exige cobertura suficiente del historial de procedimientos.

**Relevancia:** aporta contexto para heridas, dispositivos, exposiciones sanitarias y temporalidad del inicio inmunosupresor.  
**Fuentes:** HL7 FHIR R5 `Procedure`; informes quirúrgicos y registros institucionales.

### 4.6 Enfermedades y circunstancias modificadoras

En los siete diagnósticos documentales siguientes, “presente” exige una condición verificada y activa en la fecha de referencia o sin resolución cuando el perfil temporal aplicable la considera vigente. “Ausente” exige cobertura suficiente de la lista clínica. Código, medicación, síntoma o resultado aislado no diagnostican la enfermedad.

#### 19. Diabetes mellitus activa y documentada (`PAR-DM-DOC-ACTIVE-001`)

Conserva tipo de diabetes, terminología versionada, estado clínico, verificación, inicio, resolución, evidencia, profesional responsable y procedencia. No representa control metabólico, complicaciones ni tratamiento.  
**Fuentes:** HL7 FHIR R5 `Condition`; ICD-11; documentación diagnóstica profesional; estándares clínicos de la American Diabetes Association como referencia de identidad y vigencia, no como diagnóstico automático.

#### 20. Insuficiencia cardiaca activa y documentada (`PAR-HF-DOC-ACTIVE-001`)

Registra insuficiencia cardiaca verificada, con subtipo si consta, sin inferirla desde disnea, edema, péptidos natriuréticos o medicación. No representa fracción de eyección, clase funcional, congestión ni estabilidad.  
**Fuentes:** guía vigente de la European Society of Cardiology sobre insuficiencia cardiaca; HL7 FHIR R5 `Condition`; ICD-11.

#### 21. Enfermedad renal crónica activa y documentada (`PAR-CKD-DOC-ACTIVE-001`)

Registra enfermedad renal crónica verificada y su categoría cuando conste. Una tasa de filtrado aislada o una lesión renal aguda no bastan. No infiere estadio, progresión, etiología ni ajuste farmacológico.  
**Fuentes:** KDIGO 2024, *Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease*; HL7 FHIR R5 `Condition`; ICD-11.

#### 22. Tratamiento renal sustitutivo activo (`PAR-KRT-ACTIVE-001`)

Registra diálisis, modalidad equivalente o tratamiento sustitutivo activo, con modalidad, situación, inicio, calendario cuando conste y procedencia. No infiere indicación, acceso vascular, adecuación ni ajuste de dosis. Se mantiene separado de la enfermedad renal crónica porque ambos estados pueden divergir y porque su repercusión clínica no es intercambiable.  
**Fuentes:** KDIGO 2024; HL7 FHIR R5 `Procedure` y `CarePlan`; documentación de Nefrología.

#### 23. Bronquiectasias activas y documentadas (`PAR-BRONCHIECTASIS-DOC-ACTIVE-001`)

Registra el diagnóstico verificado de bronquiectasias y su situación temporal. No lo infiere desde tos, esputo, infecciones respiratorias o una descripción radiológica aislada no adjudicada. No representa colonización, exacerbación ni función pulmonar.  
**Fuentes:** guía profesional vigente sobre bronquiectasias en adultos; HL7 FHIR R5 `Condition` y `DiagnosticReport`; ICD-11.

#### 24. Soporte respiratorio crónico activo (`PAR-RESP-SUPPORT-ACTIVE-001`)

Registra oxigenoterapia domiciliaria, ventilación no invasiva u otra modalidad crónica, con indicación documentada, modalidad, estado, inicio y procedencia. Una administración puntual de oxígeno durante un episodio agudo no basta. No infiere insuficiencia respiratoria ni prescribe soporte.  
**Fuentes:** HL7 FHIR R5 `DeviceUsage`, `Procedure` y `CarePlan`; documentación de Neumología o unidad responsable.

#### 25. Cirrosis activa y documentada (`PAR-CIRRHOSIS-DOC-ACTIVE-001`)

Registra cirrosis verificada, con etiología y descompensación cuando consten. Las pruebas hepáticas alteradas no equivalen a cirrosis; la cirrosis no equivale a descompensación actual. El parámetro no representa estadio, pronóstico ni actuación.  
**Fuentes:** guía profesional vigente de hepatopatía crónica/cirrosis; HL7 FHIR R5 `Condition`; ICD-11.

#### 26. Evaluación diagnóstica positiva de malnutrición (`PAR-MALNUTRITION-ASSESS-POS-001`)

Determina si una evaluación diagnóstica completa satisface un método previamente aprobado. Deben constar instrumento, versión, población, componentes, métodos de medición, umbrales, lógica de combinación, resultado, fecha y procedencia. Un cribado positivo, el índice de masa corporal, la pérdida de peso, la ingesta o la inflamación considerados aisladamente no constituyen el diagnóstico.

**Situación actual:** GLIM es la fuente clínica principal identificada y exige al menos un criterio fenotípico y uno etiológico tras el cribado; todavía no se ha aprobado una realización completa y reproducible para este universo. Hasta entonces, la resolución automática es indeterminada.  
**Fuentes:** Cederholm y colaboradores, consenso GLIM, *Clinical Nutrition* 2019;38:1–9, DOI 10.1016/j.clnu.2018.08.002; HL7 FHIR R5 `Observation` y `Condition`.

#### 27. Evaluación positiva de fragilidad (`PAR-FRAILTY-ASSESS-POS-001`)

Determina si una evaluación completa satisface un instrumento previamente aprobado para la población y situación basal. Deben constar instrumento, versión, población, estado basal, componentes, regla, categoría, fecha y procedencia. Edad, discapacidad estable, dependencia, deterioro cognitivo, malnutrición, enfermedad aguda o limitación terapéutica no son sinónimos de fragilidad. La valoración durante una descompensación aguda puede distorsionar el estado basal.

**Situación actual:** la Clinical Frailty Scale 2.0 está identificada como candidata, pero no se ha aprobado como regla universal para toda persona adulta de este universo. Hasta que exista una configuración admisible, la resolución automática es indeterminada.  
**Fuentes:** Clinical Frailty Scale 2.0, Dalhousie University; documentación geriátrica o multidisciplinar autorizada; HL7 FHIR R5 `Observation`.

## 5. Organización clínica del perfil

Los parámetros se presentan en seis apartados independientes:

| Apartado | Contenido | Número |
|---|---|---:|
| Contexto y autoridad | programación, diagnóstico de base, responsables, protocolo y restricciones | 6 |
| Exposición | glucocorticoide sistémico previsto | 1 |
| Estado inmunitario | IgG, anatomía esplénica y neutrófilos | 3 |
| Barreras y material | acceso intravascular e implantes | 2 |
| Antecedentes | gravedad infecciosa, oportunismo, resistencia, atención aguda y procedimientos | 6 |
| Modificadores | diabetes, corazón, riñón, respiratorio, hígado, nutrición y fragilidad | 9 |

La agrupación ordena la lectura; no fusiona parámetros ni crea una puntuación. Enfermedad renal crónica y tratamiento renal sustitutivo, por ejemplo, permanecen diferenciados aunque puedan coexistir. Lo mismo ocurre con bronquiectasias y soporte respiratorio, ingreso por infección y soporte orgánico, o dispositivo e infección.

## 6. Interoperabilidad y terminologías

### 6.1 HL7 FHIR R5

FHIR puede transportar y enlazar observaciones, diagnósticos, encuentros, procedimientos, planes, prescripciones, informes y dispositivos. Se emplean principalmente `Observation`, `DiagnosticReport`, `Condition`, `Encounter`, `Procedure`, `CarePlan`, `MedicationRequest`, `ServiceRequest`, `CareTeam`, `Device` y `DeviceUsage`.

FHIR no certifica por sí mismo la verdad clínica, la causalidad, la completitud ni la vigencia. Un recurso técnicamente válido puede contener información insuficiente o clínicamente inaplicable.

### 6.2 LOINC, ICD-11 y terminología microbiológica

LOINC identifica el analito o la observación, pero no aporta un intervalo universal ni convierte una marca de laboratorio en diagnóstico. ICD-11 proporciona identidad terminológica versionada; el código requiere verificación, sujeto, contexto y temporalidad. La terminología de resistencia del ECDC y los criterios de EUCAST sólo pueden operar cuando se adopten versiones, tablas y ventanas concretas.

### 6.3 Procedencia y versiones

Cada conclusión debe permitir recuperar: fuente original, autor o institución, fecha, estado documental, método, versión, transformación realizada y relación con el episodio. Una actualización de fuente, protocolo, intervalo o configuración obliga a una nueva versión; no modifica retrospectivamente evaluaciones anteriores.

## 7. Autoridades clínicas, sanitarias y normativas consultadas

- European Alliance of Associations for Rheumatology (EULAR): cribado y profilaxis de infecciones crónicas y oportunistas antes de determinados tratamientos antirreumáticos e inmunosupresores.
- Centers for Disease Control and Prevention (CDC): inmunocompetencia alterada, asplenia y prevención de infecciones relacionadas con catéter intravascular.
- European Centre for Disease Prevention and Control (ECDC): resistencia antimicrobiana y control de microorganismos resistentes.
- Kidney Disease: Improving Global Outcomes (KDIGO): enfermedad renal crónica y tratamiento renal sustitutivo.
- European Society of Cardiology (ESC): insuficiencia cardiaca.
- Global Leadership Initiative on Malnutrition (GLIM): diagnóstico consensuado de malnutrición.
- Dalhousie University, Geriatric Medicine Research: Clinical Frailty Scale.
- Clinical and Laboratory Standards Institute (CLSI): establecimiento y verificación de intervalos de referencia.
- Regenstrief Institute: LOINC.
- World Health Organization: ICD-11.
- HL7 International: FHIR R5.
- Autoridades profesionales e institucionales que originan el diagnóstico, el plan terapéutico, la interconsulta, los protocolos y las restricciones locales.

## 8. Garantías éticas, jurídicas y de seguridad

### 8.1 Decisión y responsabilidad profesional

El perfil es informativo y predecisional. La indicación, consentimiento, prescripción, prevención, aplazamiento o inicio corresponden al profesional sanitario competente dentro de la organización asistencial. El sistema no debe ocultar desacuerdos, convertir información ausente en negativa ni presentar una clasificación documental como diagnóstico nuevo.

### 8.2 Autonomía del paciente e historia clínica

En España son aplicables la Ley 41/2002, básica reguladora de la autonomía del paciente y de derechos y obligaciones en materia de información y documentación clínica, así como la normativa autonómica y organizativa pertinente. La información debe ser comprensible, suficiente y proporcionada a la decisión; la historia debe permitir conocer la actuación realizada y sus responsables.

### 8.3 Protección de datos

Los datos de salud son categorías especiales conforme al Reglamento (UE) 2016/679. Su tratamiento requiere base jurídica, finalidad determinada, minimización, exactitud, limitación de acceso, seguridad y conservación proporcionada. Para investigación, demostración o evaluación técnica deben utilizarse datos anónimos o sintéticos siempre que sea posible; la seudonimización no equivale a anonimización.

### 8.4 Producto sanitario y sistemas de inteligencia artificial

La eventual incorporación a un programa que proporcione información empleada para decisiones diagnósticas o terapéuticas exige analizar su posible condición de producto sanitario conforme al Reglamento (UE) 2017/745 y su clasificación según finalidad prevista. También debe evaluarse el Reglamento (UE) 2024/1689 cuando el sistema entre en su ámbito. Este documento no declara conformidad regulatoria, eficacia, seguridad clínica ni puesta en servicio.

### 8.5 Registro de incertidumbre y fallos técnicos

Una carencia clínica se registra como indeterminación. Un fallo de carga, validación, conexión o reproducción es un fallo técnico y no puede presentarse como resultado clínico ausente ni indeterminado. Toda ejecución debe conservar versiones, fuentes, incidencias, correcciones y responsable de la revisión humana.

## 9. Límites científicos actuales

1. Los 27 parámetros no constituyen una escala validada ni un modelo pronóstico.
2. No se han establecido ponderaciones, probabilidades ni umbrales universales.
3. Cuatro parámetros requieren todavía una configuración clínica aprobada: infección oportunista, colonización multirresistente, malnutrición y fragilidad.
4. El contraste efectuado hasta la fecha es estructural y de disponibilidad de datos; no demuestra beneficio clínico comparado, calibración, discriminación ni impacto sobre resultados de salud.
5. La suficiencia documental no equivale a validez clínica, y la reproducción exacta de una operación no garantiza que sus premisas sean verdaderas o aplicables.
6. Antes de un uso clínico se requieren validación prospectiva, evaluación de usabilidad, análisis de errores, vigilancia, gobierno del cambio y autorización institucional y regulatoria que proceda.

## 10. Bibliografía y documentos normativos

1. Fragoulis GE, Nikiphorou E, Dey M, et al. 2022 EULAR recommendations for screening and prophylaxis of chronic and opportunistic infections in adults with autoimmune inflammatory rheumatic diseases. *Ann Rheum Dis*. Publicación electrónica 2022. DOI: [10.1136/ard-2022-223335](https://doi.org/10.1136/ard-2022-223335).
2. Centers for Disease Control and Prevention. [Altered Immunocompetence: General Best Practices for Immunization](https://www.cdc.gov/vaccines/hcp/imz-best-practices/altered-immunocompetence.html).
3. Centers for Disease Control and Prevention. [Guidelines for the Prevention of Intravascular Catheter-Related Infections](https://www.cdc.gov/infection-control/hcp/intravascular-catheter-related-infection/).
4. European Centre for Disease Prevention and Control. [Directory of guidance on prevention and control of antimicrobial resistance](https://www.ecdc.europa.eu/en/publications-data/directory-guidance-prevention-and-control/antimicrobial-resistance).
5. Kidney Disease: Improving Global Outcomes. [KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease](https://kdigo.org/guidelines/ckd-evaluation-and-management/).
6. European Society of Cardiology. [Clinical practice guidelines on heart failure](https://www.escardio.org/guidelines/clinical-practice-guidelines/all-esc-practice-guidelines/heart-failure/).
7. Cederholm T, Jensen GL, Correia MITD, et al. GLIM criteria for the diagnosis of malnutrition: a consensus report from the global clinical nutrition community. *Clinical Nutrition*. 2019;38:1–9. DOI: [10.1016/j.clnu.2018.08.002](https://doi.org/10.1016/j.clnu.2018.08.002).
8. Dalhousie University, Geriatric Medicine Research. [Clinical Frailty Scale, version 2.0](https://www.dal.ca/sites/gmr/our-tools/clinical-frailty-scale.html).
9. Clinical and Laboratory Standards Institute. [EP28: Defining, Establishing, and Verifying Reference Intervals in the Clinical Laboratory](https://clsi.org/standards/products/method-evaluation/documents/ep28/).
10. Regenstrief Institute. [LOINC 2465-3: IgG, mass concentration in serum or plasma](https://loinc.org/2465-3/).
11. Regenstrief Institute. [LOINC 751-8: neutrophils, absolute concentration in blood by automated count](https://loinc.org/751-8/).
12. HL7 International. [FHIR Release 5](https://hl7.org/fhir/R5/).
13. World Health Organization. [ICD-11 for Mortality and Morbidity Statistics](https://icd.who.int/).
14. Jefatura del Estado. [Ley 41/2002, de autonomía del paciente y documentación clínica](https://www.boe.es/buscar/act.php?id=BOE-A-2002-22188).
15. Parlamento Europeo y Consejo. [Reglamento (UE) 2016/679, General de Protección de Datos](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=es).
16. Parlamento Europeo y Consejo. [Reglamento (UE) 2017/745 sobre los productos sanitarios](https://eur-lex.europa.eu/eli/reg/2017/745/oj?locale=es).
17. Parlamento Europeo y Consejo. [Reglamento (UE) 2024/1689 por el que se establecen normas armonizadas en materia de inteligencia artificial](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=es).

## 11. Conclusión

El universo OP-IMM-001 define un expediente predecisional de riesgo infeccioso compuesto por 27 parámetros clínicos y documentales claramente diferenciados. Su principal garantía no consiste en producir una respuesta favorable o desfavorable, sino en impedir que una decisión de inicio se presente como suficientemente informada cuando persisten carencias relevantes, conflictos de procedencia, falta de autoridad o imposibilidad material de evaluación.

La documentación es completa respecto del objeto constituido y deliberadamente limitada respecto de lo que todavía no se ha demostrado. No autoriza el inicio ni la suspensión de ningún tratamiento, no sustituye guías clínicas específicas y no debe utilizarse con datos reales hasta completar las configuraciones pendientes, la validación empírica y las exigencias regulatorias e institucionales aplicables.
