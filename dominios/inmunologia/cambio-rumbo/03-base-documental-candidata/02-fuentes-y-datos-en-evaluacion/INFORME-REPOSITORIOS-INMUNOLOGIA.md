# Repositorios de datos anonimizados en inmunología

**Informe de fuentes · versión 2, corregida tras adversarial**
Fecha de consulta de todas las fuentes: **31 de agosto de 2026**
Encargo: localizar repositorios con datos anonimizados específicos de inmunología; leer sus normas, la forma de carga y descarga, la vigencia de los datos y el uso permitido.

---

## 0 · Advertencia de método

Todo lo que figura como dato ha sido leído contra la página abierta en la fecha indicada. Lo que es lectura mía va marcado como lectura. Lo que no he podido cerrar va como **U** con la causa escrita.

Esta versión 2 sustituye a una entrega anterior que contenía cinco defectos materiales, registrados en el §1 para que no se repitan.

---

## 1 · Correcciones sobre la entrega anterior

| # | Defecto | Corrección aplicada |
|---|---|---|
| 1 | Se filtraron candidatos por idioma, coste y derecho de redistribución, criterios que no formaban parte del encargo | Se restituyen todas las fuentes con su ficha completa; el uso permitido se informa, no se usa como criba |
| 2 | Se afirmó que DR67 era el último release publicado de ImmPort; era una lectura del calendario de próximos releases | Se declara **U** sobre cuál es el último release efectivamente publicado (véase §4) |
| 3 | Cifras de 2024 (estudios en ImmPort; pacientes en BIFAP) servidas sin fecha | Toda cifra lleva ahora la fecha de la fuente que la sostiene |
| 4 | IEDB descartada por juicio de pertinencia clínica no solicitado | IEDB restituida con ficha propia (§2.7) |
| 5 | Cobertura limitada a cinco recursos | Añadida FlowRepository (§2.2); frente no examinado declarado en §7 |

---

## 2 · Fichas por repositorio

### 2.1 · ImmPort — Immunology Database and Analysis Portal (NIAID/DAIT)

`https://www.immport.org` · documentación en `https://docs.immport.org`

**Objeto.** Archivo de datos de investigación inmunológica generados sobre todo por investigadores financiados por NIAID/DAIT, con extensión a otros programas del NIH y a investigadores de financiación privada. Incluye información a nivel de sujeto: diseño del estudio, acontecimientos adversos, valoraciones, intervenciones, pruebas de laboratorio, historia clínica y experimentos. Según nota del NIAID de **agosto de 2024**, más de 1.000 estudios, más de 160 áreas de enfermedad y 35 tipos de dato.

**Acceso.** Registro gratuito. La mayoría de los estudios están abiertos a cualquier usuario registrado. La autenticación es obligatoria para descargar.

**Uso permitido — cláusula 2.4 del acuerdo de usuario.** El proveedor del dato sigue siendo su propietario. El usuario puede emplear los datos para cualquier fin lícito no prohibido en el resto del acuerdo, tiene derecho sin restricción a usarlos y distribuirlos, y debe garantizar que toda redistribución se produzca en términos equivalentes a los de ese mismo acuerdo.

**Otras cláusulas relevantes.**

- **1.1** — No intentar identificar a ningún individuo ni entidad, ni por sí solo ni combinando estos datos con otros. Si se descubriera una identidad de forma inadvertida: no hacer uso de ese conocimiento, notificarlo al responsable de programa del NIAID y no comunicarlo a nadie más.
- **2.5** — Ni NIAID ni Peraton representan que los datos o análisis disponibles en ImmPort sean adecuados para fines de diagnóstico humano, para informar decisiones de tratamiento, ni para ningún otro fin, y no aceptan responsabilidad alguna por tal uso.
- **3.2.3** — Obligación de reconocimiento en toda publicación, citando el sitio de Shared Data, el número de accession del estudio (SDYxxxx) y su título.
- **3.1** — Ley federal aplicada por los tribunales federales del Distrito de Columbia.

**Identificador citable.** Cada estudio lleva DOI propio con prefijo `10.21430`. Ejemplo verificado: SDY3324 → `10.21430/M35OC5U8Z7`.

**Versión y congelación.** Los estudios nuevos se hacen públicos mediante un proceso mensual de *data release* con número secuencial (DR64, DR65…). Cada estudio ofrece un paquete completo `SDYXXX_DRXX_ALL_DATA.zip` correspondiente a una versión concreta de release, y el manifiesto de descarga incluye columna `MD5_CHECKSUM` por fichero. Existen, por tanto, número de versión, paquete cerrado y hash por fichero suministrados por el propio repositorio.

**Desidentificación (Safe Harbor).** ImmPort declara:

- redondear a 90 toda edad mayor de 89, dejando comentario de que se ha hecho;
- **no registrar fechas** en sus plantillas: todos los puntos temporales y calendarios se refieren al día 0 del estudio, o al día que designe el proveedor;
- no registrar subdivisiones geográficas por debajo del nivel de estado;
- no capturar en plantilla los identificadores de sujeto enumerados en Safe Harbor;
- no mostrar ni exportar los identificadores de origen de sujeto, muestra o muestra experimental.

**Vías de carga y descarga.** Interfaz web (fichero suelto, carrito con ZIP y URL firmada de siete días, y paquete `ALL_DATA`); API de Shared Data; API GA4GH DRS con URL firmada de S3 o flujo directo; y cliente de línea de órdenes con clave API y fichero de manifiesto. El navegador antiguo basado en Aspera se retira en julio de 2026.

**Límites declarados.** ImmPort no suele aceptar ni compartir datos humanos de genotipado GWAS ni de secuenciación de nueva generación; recomienda dbGaP o SRA para eso.

**Subconjunto de acceso controlado.** Los estudios IMPACC SDY1760 y SDY2112 migran a AccessClinicalData@NIAID con fecha declarada de 20 de mayo de 2026. Ese sistema exige verificación de identidad IAL2 conforme a NOT-OD-25-159, solicitud de acceso revisada por empleados federales y firma de acuerdo de uso; admite ID.me, Login.gov o cuenta de correo del NIH, y no admite Gmail ni otras cuentas personales. La autorización tiene vigencia de doce meses y debe renovarse anualmente.

---

### 2.2 · FlowRepository (ISAC)

`https://flowrepository.org`

**Objeto.** Base pública de experimentos de citometría de flujo, consultable y descargable, anotada conforme a la norma MIFlowCyt. Se usa principalmente como lugar de depósito de los datos de hallazgos publicados en revistas con revisión por pares del campo de la citometría. Financiada por la International Society for Advancement of Cytometry.

**Acceso.** Los términos declaran que el repositorio puede ser usado por cualquier individuo para cualquier fin. Los conjuntos públicos son consultables y descargables.

**Uso permitido.** ISAC declara que no impone restricciones al uso ni a la redistribución de los datos disponibles a través de sus servicios. Advierte, sin embargo, que parte de los datos originales puede estar sujeta a derechos de patente, autor u otros derechos de propiedad intelectual de terceros, y que corresponde al usuario asegurarse de no infringirlos; ISAC no valida esas reclamaciones ni concede permiso irrestricto sobre los datos. Exige atribución cuando sus servicios o datos se incorporen a otro producto o servicio.

**Garantías.** Datos y bases de datos se ofrecen «tal cual», sin representación sobre exactitud ni sobre idoneidad para ningún uso. Responsabilidad limitada a cien dólares. Ley del Estado de Maryland; foro en el condado de Montgomery, Maryland.

**Registro de uso.** ISAC conserva registros de uso para revisión científica y planificación, y puede difundir volúmenes totales de uso a terceros.

**Límite de fondo, como lectura.** El objeto depositado es el fichero FCS y su anotación MIFlowCyt, es decir, medida de citometría con sus metadatos experimentales. No es historia clínica ni curso asistencial.

---

### 2.3 · ITN TrialShare (Immune Tolerance Network, NIAID)

`https://www.itntrialshare.org`

**Objeto.** Datos y código de análisis que sustentan los manuscritos publicados por la ITN, en alergia y asma, trasplante de órgano y enfermedad autoinmune, incluida la diabetes tipo 1. Datos a nivel de participante, desidentificados. La ITN declara poner a disposición los datos subyacentes de todos los estudios publicados, con independencia de que el resultado fuera positivo o negativo.

**Acceso.** Creación de cuenta gratuita. Los usuarios externos se autorregistran sin aprobación previa y obtienen acceso de lectura a los datos de estudios liberados públicamente. Se exige correo electrónico válido y ser mayor de dieciocho años. Las cuentas externas se desactivan tras un año de inactividad; después hay que reactivarlas.

Existe una figura de colaborador, sujeta a aprobación de la dirección de la ITN, que puede dar acceso a estudios internos donde no se ha retirado toda la información de salud protegida.

**Uso permitido — y aquí está la diferencia decisiva con ImmPort.** Los términos declaran que nada en el acuerdo constituye, de forma expresa o implícita, una concesión de licencia ni de otros derechos por parte de la ITN o del NIAID. Y añaden que sólo los usuarios de TrialShare pueden acceder a los datos de protocolo a través del sistema, quedando estrictamente prohibida su distribución a usuarios no autorizados.

**Otras cláusulas.** No intentar reidentificar a los participantes combinando la información del sistema con otras fuentes. Los usuarios son los únicos responsables de la exactitud de cualquier uso derivado. Toda publicación debe cumplir la política de publicaciones de la ITN y reconocer TrialShare por cita, agradecimiento o coautoría. Se repite, con redacción prácticamente idéntica a la de ImmPort, que ni ITN ni NIAID representan que los datos o análisis sean adecuados para diagnóstico humano ni para informar decisiones de tratamiento.

**Vigencia del documento rector.** La *TrialShare Access and Usage Policy* consultable es la **versión 1.2, fechada el 15 de julio de 2013**. Los enlaces internos que cita apuntan a rutas antiguas del sitio. La página de términos de uso no muestra fecha. Que sea la versión publicada no implica que haya sido sustituida ni que no esté en vigor: es lo que hay publicado. Comprobar su vigencia exige preguntar a la ITN.

**Transparencia de método.** La ITN se compromete a facilitar el código fuente de los análisis de los informes y visualizaciones publicados en TrialShare, en el propio sistema o a petición.

---

### 2.4 · PhysioNet · MIMIC-IV (MIT Laboratory for Computational Physiology)

`https://physionet.org`

**Objeto.** Base de historia clínica electrónica hospitalaria. No es un repositorio de inmunología, pero es la fuente con curso clínico real y notas, y contiene por tanto pacientes inmunodeprimidos y episodios infecciosos. Se incluye por eso y con esa advertencia.

**Acceso.** Gratuito pero acreditado: formación en protección de sujetos humanos (CITI, con su propio ciclo de caducidad), firma del acuerdo de uso del recurso concreto, y credencial activa de PhysioNet. La credencial se concede una vez y no está ligada a un solo conjunto, pero cada recurso de acceso acreditado exige su propia firma. PhysioNet advierte actualmente de retrasos significativos en la tramitación de solicitudes por cambios de personal en su grupo.

**Uso permitido — PhysioNet Credentialed Health Data License 1.5.0.** El licenciatario no intentará identificar a ningún individuo ni institución referida en los datos restringidos; extremará el cuidado para evitar revelar tales identidades en cualquier publicación o comunicación; y **no compartirá el acceso a los datos con nadie más**. Las obligaciones sobreviven a la terminación del acuerdo. Datos «tal cual», sin garantía.

**Consecuencia operativa que hay que tener escrita.** PhysioNet ha publicado que su acuerdo prohíbe expresamente compartir el acceso a los datos con terceros, incluido enviarlos a través de API o usarlos en plataformas en línea, y que los datos de MIMIC no deben ser almacenados ni retenidos por servicios de modelos de lenguaje de terceros. Traducido a nuestra forma de trabajar: **datos de MIMIC no pueden pegarse en una unidad de IA de terceros, ni en Claude ni en Watson.** Si esta fuente entrara, el tratamiento del dato sería local y sólo el agregado que el director decidiera podría circular.

**Redistribución.** No permitida. Un coautor sin credencial propia no puede recibir los datos. La declaración de disponibilidad de datos de un manuscrito debe remitir al procedimiento de acceso de PhysioNet, no prometer entrega directa.

---

### 2.5 · Vivli

`https://vivli.org`

**Objeto.** Plataforma sin ánimo de lucro de datos de ensayo clínico a nivel de participante, agnóstica respecto de enfermedad, país, patrocinador y financiador. El listado de estudios disponibles es público.

**Acceso y coste.** Solicitar datos es gratuito y está abierto a cualquiera; no hace falta ser miembro. El entorno seguro de investigación se cobra a partir de un plazo determinado, típicamente tras doce meses de uso. Según reportaje de 2019, la tarifa entonces era de doce o veinticinco dólares por día según modalidad de membresía; **U** sobre la tarifa vigente en 2026, no verificada.

**Procedimiento.** Revisión en tres pasos: comprobación administrativa de que el formulario está completo y de que el equipo incluye un estadístico cualificado; revisión de viabilidad por el contribuyente del dato; y revisión de méritos de la propuesta por un panel independiente o comité científico. Después se ejecuta el acuerdo de uso y se prepara y sube el paquete anonimizado. El plazo medio declarado es de unos meses.

**Modalidad de entrega.** Según el miembro, por descarga o mediante escritorio remoto en entorno virtual seguro. Vivli mantiene los datos disponibles al menos diez años, salvo impedimento contractual.

---

### 2.6 · BIFAP (Agencia Española de Medicamentos y Productos Sanitarios)

`http://bifap.aemps.es`

**Objeto.** Base de datos para la Investigación Farmacoepidemiológica en el Ámbito Público: registros de historia clínica electrónica de atención primaria del Sistema Nacional de Salud, aportados por las comunidades autónomas que participan voluntariamente mediante convenio. Financiada y gestionada por la AEMPS. Creada en 2001.

**Volumen, con fecha.** Nota de la AEMPS de **2022**: doce millones de historias clínicas y más de cuarenta publicaciones científicas. Nota de la AEMPS de **2024**, al integrarse BIFAP en DARWIN EU, red de datos de la Agencia Europea de Medicamentos: veintidós millones de pacientes españoles y más de cien artículos publicados. Reportaje de diciembre de 2025: en once años se habían elaborado 126 proyectos de investigación, con la producción concentrada en cinco investigadores y tres instituciones, y la AEMPS declara estar impulsando medidas para facilitar el acceso.

**Acceso.** BIFAP da apoyo a las actividades propias de la AEMPS y está además disponible para la realización de estudios por investigadores adscritos a organismos públicos y por los médicos colaboradores. Quienes deseen utilizarla en proyectos de investigación deben darse de alta en la web y realizar cursos de formación sobre la base de datos.

**U con causa.** `bifap.aemps.es` rechaza el acceso automatizado. No he podido leer de primera mano las condiciones vigentes de acceso, el formulario de solicitud, ni el régimen de uso y publicación de resultados. Todo lo anterior procede de notas de la AEMPS y del Ministerio de Sanidad, no del propio portal.

---

### 2.7 · IEDB — Immune Epitope Database and Analysis Resource

`https://www.iedb.org`

**Objeto.** Recurso gratuito que cataloga datos experimentales de epítopos inmunes y su contexto: anticuerpo, célula T y unión a MHC, en enfermedad infecciosa, alergia, autoinmunidad y trasplante, en huésped vertebrado. Establecido en 2004 en el La Jolla Institute, financiado por NIAID.

**Volumen, con fecha.** Publicación de actualización de **2024**: más de 25.000 publicaciones curadas, 6,8 millones de ensayos y 1,6 millones de epítopos; curación de la literatura desde 1952 hasta el presente, con consulta de PubMed cada dos semanas.

**Naturaleza del dato.** Es dato experimental de epítopo y de ensayo, curado a partir de la literatura y de envíos directos. No es dato clínico a nivel de paciente.

**U con causa.** `iedb.org` rechaza el acceso automatizado. No he podido leer sus términos de uso literales. Lo anterior procede de la literatura publicada sobre el recurso y de su propia descripción indexada.

---

## 3 · Candidatos concretos localizados en ImmPort

Localizados al recorrer las notas de release. Ninguno está verificado en su página de estudio: lo que sigue procede de la nota de release, no del registro del estudio.

### SDY3324 — «COVID-19 booster vaccine in autoimmune disease non-responders (ACV01)»

- Publicado en **DR60**, release de **enero de 2026**. DOI `10.21430/M35OC5U8Z7`. Registro `NCT05000216`.
- Ensayo aleatorizado, multicéntrico, adaptativo y abierto que compara la respuesta inmunitaria a distintas dosis adicionales de vacuna COVID-19 en participantes con enfermedad autoinmune que requieren medicación inmunosupresora.
- Población adulta de la etapa 1: hasta 900 participantes previstos, con al menos una de cinco enfermedades: lupus eritematoso sistémico, artritis reumatoide, esclerosis múltiple, esclerosis sistémica y pénfigo.
- Cohortes definidas por régimen inmunosupresor: A, micofenolato de mofetilo o ácido micofenólico; B, metotrexato; C, cualquier terapia de depleción de células B en los dieciocho meses previos.
- Ramas de tratamiento con **regla explícita de suspensión temporal del inmunosupresor**: micofenolato, tres días antes y diez después de la dosis; metotrexato, al menos siete días antes y siete después, sin exceder veintiún días en total. La otra rama continúa sin alteración de pauta ni dosis.
- Umbrales serológicos declarados en el propio protocolo: respuesta subóptima definida como resultado Roche Elecsys Anti-SARS-CoV-2 S ≤ 200 U/mL; respuesta inmunitaria baja, > 200 y ≤ 2500 U/mL.
- Sujetos consignados en la nota: **148**.
- Publicación asociada: *Prospective SARS-CoV-2 additional vaccination in immunosuppressant-treated individuals with autoimmune diseases in a randomized controlled trial*, `10.1172/jci.insight.191266`, PubMed 41289027.

**Reparo, antes de que lo formule otro.** La nota de release declara para este estudio `Assays: None` y `Clinical Assessments: None`. Constan diseño, cohortes y sujetos; no consta carga de datos de ensayo ni de valoraciones clínicas. **No debe darse por utilizable hasta abrir la página del estudio y su paquete `ALL_DATA`.**

### SDY3274 — ARTIST (ITN524ST/CTOT-12)

- Publicado en DR60. DOI `10.21430/M3K94KYHFN`. Registro `NCT01516177`. 250 sujetos.
- Estudio observacional multicéntrico en receptores adultos de trasplante renal entre uno y cinco años postrasplante, reclutados a través de un espectro de regímenes inmunosupresores: inhibidores de calcineurina, inhibidores de mTOR e inducción con Campath.
- La propia descripción sitúa el riesgo de infección y de neoplasia como coste de la inmunosupresión continuada.
- Misma advertencia: la nota declara `Assays: None` y `Clinical Assessments: None`.

---

## 4 · Vigencia de los datos

| Recurso | Mecanismo de actualización | Estado verificado hoy |
|---|---|---|
| ImmPort | Release mensual numerado; paquete `ALL_DATA` por versión; MD5 por fichero en el manifiesto | Calendario publicado: DR65 el 25-06-2026, DR66 el 30-07-2026, DR67 el 27-08-2026, DR68 el 24-09-2026. **U**: el listado de novedades del portal recuperado hoy anuncia como último el DR65 (25-06-2026). No queda establecido cuál es el último release efectivamente publicado |
| FlowRepository | Depósito asociado a publicación; sin calendario de release declarado | No verificado |
| ITN TrialShare | Liberación ligada a la publicación de manuscritos de la ITN | Política rectora fechada en 2013; vigencia no confirmada |
| PhysioNet | Versionado por recurso; licencia 1.5.0 | Módulo MIMIC-IV-ECHO v1.0.1 publicado el 25-08-2026 |
| Vivli | Datos conservados al menos diez años | Tarifa vigente no verificada |
| BIFAP | Aportación continuada de las CCAA participantes | No verificado; portal inaccesible a consulta automatizada |
| IEDB | Consulta de PubMed cada dos semanas | Cifras de 2024; términos no verificados |

---

## 5 · Cláusulas que obligan en cualquier manuscrito

1. **ImmPort 2.5 e ITN, redacción equivalente.** Los datos no se representan como adecuados para diagnóstico humano ni para informar decisiones de tratamiento. Cualquier trabajo que hable de apoyo a la decisión clínica debe declararlo antes de que lo haga un revisor.
2. **No reidentificación.** Cláusula presente en ImmPort, ITN y PhysioNet. Obliga también a lo que se publique: ninguna combinación de tablas puede permitir aislar a un sujeto.
3. **Atribución.** ImmPort exige citar sitio, accession y título del estudio. FlowRepository exige atribución. ITN exige cita, agradecimiento o coautoría y remisión de la referencia.
4. **Redistribución.** Permitida sin restricción por ImmPort (con la condición de términos equivalentes) y no restringida por FlowRepository (con la salvedad de derechos de terceros sobre el dato original). Prohibida por ITN TrialShare y por PhysioNet.

---

## 6 · Lectura (no dato)

La forma en que ImmPort desidentifica tiene consecuencias que afectan a cualquier formalización que se apoye en esos datos:

- **No hay fecha absoluta.** Todos los puntos temporales están referidos al día 0 del estudio, o al día que designe el proveedor. El tiempo llega ya relativizado a un origen declarado por un tercero, y ese origen puede no ser el mismo entre estudios.
- **La edad alta está colapsada.** Toda edad superior a 89 se registra como 90. Cualquier umbral por encima de esa cifra es inoperante en esta fuente.
- **No hay geografía por debajo del nivel de estado.** Ninguna estratificación territorial fina es posible.

Y una advertencia sobre el alcance de este informe: haber comprobado que un repositorio permite publicar no es haber comprobado que sus variables se correspondan con los parámetros de un dominio. Son dos verificaciones distintas y la que decide es la segunda. Este informe cubre la primera y deja abierta la segunda con dos candidatos nombrados en el §3.

---

## 7 · Frente abierto, nombrado

Recursos de inmunología no examinados en este informe, que deben cubrirse antes de dar la búsqueda por cerrada:

- **ImmuneSpace** — capa de análisis del Human Immunology Project Consortium sobre datos que residen también en ImmPort.
- **AIRR Data Commons / iReceptor** — repertorios de receptores inmunitarios adaptativos.
- **dbGaP** y **SRA** — recomendados por la propia ImmPort para el dato genómico que ella no acepta.
- **EGA** — European Genome-phenome Archive, acceso controlado europeo.

Comprobaciones pendientes con causa:

1. Cuál es el último *data release* efectivamente publicado en ImmPort.
2. Contenido real de SDY3324 y SDY3274: si el paquete `ALL_DATA` contiene datos de ensayo y valoraciones clínicas o sólo diseño y sujetos.
3. Si la verificación IAL2 de AccessClinicalData@NIAID admite identidad no estadounidense.
4. Condiciones vigentes de acceso a BIFAP y régimen aplicable a un investigador no adscrito a organismo público.
5. Términos de uso literales de IEDB.
6. Vigencia actual de la política de acceso de ITN TrialShare, fechada en 2013.
7. Tarifa vigente del entorno seguro de Vivli.

---

## 8 · Fuentes consultadas

Todas abiertas el 31 de agosto de 2026.

- ImmPort, acuerdo de usuario — `https://docs.immport.org/home/agreement/`
- ImmPort, desidentificación de sujetos — `https://docs.immport.org/datasubmission/general/deidentification/`
- ImmPort, notas de release — `https://docs.immport.org/data/release/`
- ImmPort, calendario de releases — `https://docs.immport.org/data/release/schedule/`
- ImmPort, notas de DR60 — `https://docs.immport.org/home/release_notes/DR60_DataRelease/`
- ImmPort, guía de descarga — `https://docs.immport.org/download/`
- ImmPort, datos de acceso controlado — `https://docs.immport.org/download/controlled/`
- NIAID, vigésimo aniversario de ImmPort (agosto de 2024) — `https://www.niaid.nih.gov/research/immport-data-repository-20th-anniversary`
- FlowRepository, términos de uso — `https://flowrepository.org/terms_of_service`
- ITN TrialShare, términos de uso — `https://www.itntrialshare.org/itn/Terms%20Of%20Use.html`
- ITN, política de acceso y uso de TrialShare, v1.2 (2013) — `https://www.immunetolerance.org/sites/default/files/ITN_TrialShare_Access_Use_Policy.pdf`
- ITN TrialShare, portada — `https://www.itntrialshare.org/`
- PhysioNet, portada y avisos — `https://physionet.org/`
- PhysioNet, licencia acreditada 1.5.0 — `https://physionet.org/content/mimiciv/view-license/0.4/`
- PhysioNet, uso responsable con modelos de lenguaje — `https://physionet.org/news/post/llm-responsible-use/`
- Vivli, solicitud de datos — `https://vivli.org/resources/requestdata/`
- Vivli, preguntas frecuentes sobre coste — `https://vivli.org/faq/is-there-a-cost-to-request-or-share-data-on-the-vivli-platform/`
- AEMPS, integración de BIFAP en DARWIN EU (2024) — `https://www.aemps.gob.es/informa/bifap-la-mayor-base-de-datos-espanola-de-registros-medicos-para-investigacion-independiente-se-integra-en-la-red-de-big-data-de-la-agencia-europea-de-medicamentos/`
- AEMPS, presente y futuro de BIFAP (2022) — `https://www.aemps.gob.es/la-aemps/presente-y-futuro-de-bifap-base-de-datos-para-la-investigacion-farmacoepidemiologica/`
- Ministerio de Sanidad, nota de prensa sobre BIFAP (2015) — `https://www.sanidad.gob.es/en/gabinete/notasPrensa.do?id=3617`
- IEDB, actualización 2024 — `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11701597/`

Dos fuentes rechazaron el acceso automatizado y quedan sin lectura directa: `bifap.aemps.es` e `iedb.org`.
