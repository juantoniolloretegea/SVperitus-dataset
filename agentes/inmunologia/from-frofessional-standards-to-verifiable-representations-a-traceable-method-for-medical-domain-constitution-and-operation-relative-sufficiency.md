# De los estándares profesionales a las representaciones verificables: un método trazable para la constitución del dominio médico y la suficiencia relativa a la operación

© 2026 Juan Antonio Lloret Egea. Algunos derechos reservados. | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ – La Biblia de la IA™ | ISSN 2695-6411 | Licencia Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0). Esta licencia se aplica exclusivamente a esta versión | Madrid, 26/08/2026
[**DOI:10.21428/39829d0b.76cf10ec**](https://doi.org/10.21428/39829d0b.76cf10ec)

## Resumen estructurado

**Antecedentes:** Trasladar conocimiento médico a un sistema computacional exige algo más que codificar reglas individuales. Un dominio médico computacional delimitado requiere un ámbito profesional explícito, reglas sometidas a gobierno clínico, criterios definidos para la admisión de observaciones, representaciones suficientes para el uso declarado y un mecanismo definido de revisión por un profesional cualificado que preserve la responsabilidad clínica.

**Objetivos:** Definir un método trazable para constituir dominios médicos y distinguir la cobertura del ámbito profesional, la fidelidad entre especificación e implementación y la suficiencia representacional relativa a la operación.

**Métodos:** Se utilizaron cuatro marcos oficiales de formación y acreditación en inmunología y alergología como fuentes profesionales de referencia delimitadas y diferenciadas de la evidencia clínica empleada para adoptar reglas operativas. El método se concretó en una representación finita de estados ternarios etiquetados y se examinó mediante el demostrador publicado [**IMMUNO-1**](https://juantoniolloretegea.github.io/SVperitus-dataset/aplicaciones/demo_wasm/index.html) y la especificación escrita y la implementación informática del módulo [**IMMUNO-2**](https://juantoniolloretegea.github.io/SVperitus-dataset/aplicaciones/demo_wasm/compositor.html) en desarrollo.

**Resultados:** El conjunto profesional de referencia abarcó un ámbito considerablemente mayor que los dos módulos computacionales, por lo que la cobertura implementada no podía equipararse a la cobertura de la especialidad. En P02, una entrada documentada con información parcial puso de manifiesto una discrepancia reproducible entre la especificación escrita aplicable a la implementación examinada y el resultado producido por el programa. De manera independiente, dos asignaciones de P02 con observación completa produjeron el mismo estado ternario por condiciones de regla diferentes; el estado escalar no permitía identificar qué condición había determinado el resultado si dicha información formaba parte de la operación declarada. Una transferencia experimental IMMUNO-1→IMMUNO-2 proporcionó el control inverso: la pérdida deliberada de información seguía siendo suficiente cuando la operación posterior solo requería la clase final transmitida.

**Conclusiones:** La fidelidad entre especificación e implementación y la suficiencia relativa a la operación son requisitos independientes dentro de la constitución del dominio médico. El razonamiento, la autoridad y la responsabilidad clínica permanecen en el experto humano cualificado; los componentes computacionales y de inteligencia artificial prestan apoyo subordinado.

**Palabras clave:** Informática médica; guías de práctica clínica; validación de programas informáticos; representación del conocimiento; alergología e inmunología

## Introducción

Las guías clínicas interpretables por ordenador han establecido métodos maduros para representar, verificar, ejecutar, integrar y mantener recomendaciones clínicas [1,2]. Los métodos de formalización rápida y las *SMART Guidelines* de la Organización Mundial de la Salud han acortado, además, el tránsito desde las recomendaciones narrativas hasta los flujos de trabajo computables, los elementos de datos, la lógica de apoyo a la decisión y los requisitos de implementación [3,4]. Estos enfoques demuestran que las recomendaciones médicas pueden expresarse de forma computable. Sin embargo, no resuelven por sí solos una cuestión previa de alcance: qué dominio profesional se ha declarado y qué parte de ese dominio representa un módulo computacional determinado.

Una segunda distinción surge una vez adoptadas las reglas. La **fidelidad entre especificación e implementación** pregunta si el programa informático ejecuta la regla escrita que sirve de referencia para la evaluación. La **suficiencia relativa a la operación** pregunta si una representación conserva las distinciones que necesita una operación declarada que utiliza dicha representación. Ambas propiedades son independientes. La teoría de determinación de consultas proporciona el principio formal general: una representación puede contener, o no, información suficiente para determinar el resultado de una consulta especificada [5]. Una implementación fiel puede ofrecer una representación demasiado reducida para una operación posterior, mientras que una representación informativamente rica puede estar implementada de forma incorrecta.

La tercera cuestión es el gobierno clínico. Los trabajos contemporáneos sobre inteligencia artificial aplicada a la salud destacan la trazabilidad, la integración en el flujo asistencial, la confianza calibrada, la supervisión efectiva y la capacidad real de intervención humana [6-8]. La analítica visual clínica dispone asimismo de enfoques consolidados para mostrar evidencia, incertidumbre y vías alternativas de razonamiento [9]. El requisito estudiado aquí es más limitado y estructural: el clínico cualificado debe recibir una representación que conserve las distinciones médicas etiquetadas necesarias para la operación clínica o experta declarada, sin tener que inspeccionar detalles internos de ejecución del programa. No se afirma que una visualización determinada mejore la cognición, la calidad de las decisiones o los resultados clínicos.

El presente estudio modela, por tanto, un estado computacional constituido como una fila de una matriz finita de datos etiquetados. Cada columna posee un significado médico declarado y cada fila registra el estado asignado a cada parámetro. Las publicaciones previas del **Sistema Vectorial (SV)** denominan *células* a estas estructuras finitas y definen una realización ternaria con los estados atómicos 0, 1 y U, junto con transducción basada en reglas, trazabilidad mediante sucesos, representación visual y restricciones aplicables a agentes especializados [14-18]. Estos elementos pertenecen a trabajos anteriores. La contribución del presente estudio consiste en integrar el ámbito profesional, la admisión de observaciones, la fidelidad entre especificación e implementación, la suficiencia relativa a la operación y la revisión humana cualificada en un único método auditable de constitución del dominio médico.

No se emplean pacientes ni cohortes. El estudio no formula afirmaciones diagnósticas, pronósticas, terapéuticas, de calibración ni de resultados clínicos, y no presenta IMMUNO-1 ni IMMUNO-2 como instrumentos de riesgo validados clínicamente.

## Objetivos

El objetivo principal fue definir un procedimiento trazable para constituir un dominio médico delimitado a partir de fuentes profesionales de referencia declaradas y evidencia clínica, y expresarlo mediante representaciones computacionales verificables. Los objetivos específicos fueron: (1) separar la cobertura del ámbito profesional de la evidencia clínica que sustenta las reglas operativas; (2) distinguir la fidelidad entre especificación e implementación de la cuestión independiente de si la propia especificación cumple los requisitos de admisión y no clausura aplicados en este estudio; (3) comprobar la suficiencia relativa a la operación sin deducir requisitos no declarados a partir del comportamiento del programa; (4) identificar las condiciones en las que una pérdida deliberada de información continúa siendo admisible; (5) establecer una propiedad precisa de recuperabilidad de la representación ternaria destinada al clínico sin formular afirmaciones sobre factores humanos; y (6) expresar los requisitos de implementación resultantes en términos comprensibles para lectores sin conocimiento previo del SV.

## Métodos

### Diseño del estudio y alcance epistémico

Este estudio de métodos formales e informática biomédica examina representaciones computacionales deterministas mediante estándares profesionales, guías clínicas, especificaciones publicadas, asignaciones formales a predicados de reglas declarados, implementaciones informáticas y requisitos declarados de representación. La constitución de un dominio médico **no** se modela como una función mecánica que transforme de manera única los documentos fuente en un sistema de reglas. Se trata de un proceso experto sometido a gobierno clínico en el que las fuentes se seleccionan, interpretan, delimitan y adoptan para una finalidad declarada. Las asignaciones formales utilizadas en este estudio son entradas construidas para comprobar reglas explícitas; no representan pacientes sintéticos.

Se realizó hasta el 26 de agosto de 2026 una búsqueda bibliográfica intensiva y orientada a mecanismos en bases de datos bibliográficas, plataformas editoriales, repositorios institucionales y de prepublicaciones, y otras fuentes académicas accesibles en la red. Las familias de búsqueda incluyeron guías interpretables por ordenador, digitalización de guías, representación formal del conocimiento, supervisión humana, visualización clínica, procedencia, determinación de consultas, suficiencia representacional e historiales de sucesos. No se trató de una revisión sistemática conforme a PRISMA; por ello, cualquier afirmación negativa sobre novedad queda limitada a la literatura identificada mediante esta búsqueda y a la fecha de corte declarada.

### Fuentes profesionales de referencia y constitución gobernada del dominio

Para un dominio médico candidato D se mantienen separados dos conjuntos de fuentes. `K_D^prof` designa las **fuentes profesionales de referencia declaradas**, utilizadas para identificar competencias pertinentes, poblaciones y alcance. `E_D^clin` designa las **fuentes de evidencia clínica** empleadas por expertos cualificados para adoptar reglas médicas operativas. Un marco formativo o de acreditación puede establecer que una competencia pertenece a la práctica profesional sin proporcionar un umbral clínico; una guía clínica puede respaldar un umbral sin definir el ámbito profesional completo de la especialidad.

La constitución gobernada se resume así:

`Constituir_H_D(K_D^prof, E_D^clin) ⇝ (Alcance_D, Π_D, Reglas_D, O_D, Q_D)`

`H_D` representa el gobierno clínico humano cualificado. `O_D` contiene las observaciones admitidas para la finalidad declarada y `Q_D`, las operaciones para las que se declara suficiente la representación. La flecha expresa un acto de constitución gobernado por expertos, no un resultado lógico único determinado automáticamente por los documentos fuente.

El caso de estudio en inmunología empleó cuatro marcos oficiales e independientes de formación o acreditación: el Royal Australasian College of Physicians (RACP), el Royal College of Physicians and Surgeons of Canada, el currículo de Allergy del General Medical Council británico y los requisitos de Allergy and Immunology del Accreditation Council for Graduate Medical Education [10-13]. La fuente del RACP se fechó de forma explícita porque su nuevo currículo de Immunology and Allergy fue aprobado en marzo de 2025 para su implantación a partir de 2027, mientras que los residentes incorporados con anterioridad permanecen sujetos al programa precedente [10]. Estas fuentes se seleccionaron como referencias profesionales independientes y delimitadas; no se presentan como representativas de todo el ámbito internacional ni como cobertura exhaustiva de la inmunología de laboratorio.

A cada competencia o requisito extraído se le asignan una población y una finalidad, seguidas de una situación explícita respecto del alcance, por ejemplo: representado por los módulos examinados; competencia profesional transversal; fuera de la población declarada; excluido expresamente del alcance presente; o no representado. Este procedimiento evita describir un módulo computacional limitado como si representara una especialidad completa.

![Figura 1. Constitución gobernada del dominio médico. Las fuentes profesionales de referencia y las fuentes de evidencia clínica permanecen diferenciadas. La admisión de las observaciones precede a la transducción ternaria y la representación destinada a la revisión experta permanece bajo gobierno clínico humano cualificado.](https://raw.githubusercontent.com/juantoniolloretegea/SV-matematica-semantica/main/documentos/celulas_especializadas_sv/inmunologia/publicaciones/from-frofessional-standards-to-verifiable-representations-a-traceable-method-for-medical-domain-constitution-and-operation-relative-sufficiency/imagenes/Figura1.png)

*Figura 1. Constitución gobernada del dominio médico. Las fuentes profesionales de referencia y las fuentes de evidencia clínica permanecen diferenciadas. La admisión de las observaciones precede a la transducción ternaria y la representación destinada a la revisión experta permanece bajo gobierno clínico humano cualificado.*

### Admisión, transducción y estado ternario

Las observaciones iniciales se someten a evaluación de admisión antes de la transducción mediante reglas:

`O_D^brutas →[Adm_D] O_D^adm →[τ_D] S_D`, con `S_D ∈ {0,1,U}^n`.

El método distingue el fallo técnico de captura, la adquisición pendiente y la no admisión de una U ternaria genuinamente constituida. Por tanto, U no puede asignarse por el mero hecho de que una información requerida no haya sido capturada o admitida. Esta distinción resulta pertinente para P02 porque la especificación escrita de IMMUNO-2 examinada en este estudio asigna determinada información no disponible a su condición U. Deben responderse, por ello, dos preguntas independientes. La primera es empírica y reproducible: ¿produce el programa, para la entrada examinada, el resultado establecido por la especificación escrita? La segunda es conceptual: ¿es compatible el tratamiento que esa especificación da a la información no disponible con el requisito declarado de que la admisión preceda a la asignación ternaria? La respuesta a la primera pregunta no determina la respuesta a la segunda.

Los fundamentos del SV, la transducción ternaria, la construcción de la interfaz visual, las restricciones de los agentes especializados y la semántica auditada basada en sucesos se han publicado por separado [14-18]. Trabajos posteriores formalizan la no clausura certificada y la distinción entre sustitución informativa y autoridad [19,20]. El presente estudio utiliza esas definiciones como antecedentes y no las presenta como resultados nuevos.

### Suficiencia relativa a la operación y representación destinada al clínico

Sean `R` una representación y `Q` una operación declarada. `R` es suficiente para `Q` sobre un dominio X cuando dos entradas que producen la misma representación no pueden producir resultados distintos bajo Q. Un contraejemplo tiene, por tanto, la forma:

`R(x) = R(y)` pero `Q(x) ≠ Q(y)`.

Un contraejemplo de este tipo demuestra insuficiencia exclusivamente para la operación especificada. No demuestra que dicha operación sea clínicamente necesaria.

Para la representación visual, supóngase que las etiquetas de los parámetros `P1,…,Pn` ocupan posiciones visuales fijas y que `r:{0,1,U}→ℝ` es una codificación radial, categórica e inyectiva. La representación abstracta

`Vis(S) = ((Pi, θi, r(Si))) para i = 1,…,n`

es inyectiva respecto del estado ternario etiquetado. Por construcción, las etiquetas de los parámetros y sus valores ternarios pueden recuperarse exactamente de la codificación abstracta. Este resultado se refiere únicamente a la representación formal. No demuestra ausencia de pérdida tras una conversión arbitraria a imagen, mayor rapidez de reconocimiento, menor carga cognitiva, mejores decisiones ni mejores resultados clínicos.

![Figura 2. Estado ternario sintético de 25 parámetros y representación radial destinada a la revisión experta. La posición radial es categórica y no representa una magnitud clínica.](https://raw.githubusercontent.com/juantoniolloretegea/SV-matematica-semantica/main/documentos/celulas_especializadas_sv/inmunologia/publicaciones/from-frofessional-standards-to-verifiable-representations-a-traceable-method-for-medical-domain-constitution-and-operation-relative-sufficiency/imagenes/Figura2.png)

*Figura 2. Estado ternario sintético de 25 parámetros y representación radial destinada a la revisión experta. La posición radial es categórica y no representa una magnitud clínica.*

### Módulos de inmunología y pruebas sobre P02

IMMUNO-1 es un demostrador técnico de 25 parámetros previamente publicado sobre profilaxis infecciosa y vacunación en adultos con neoplasias hematológicas e inmunosupresión [21]. Guías independientes de oncología y enfermedades infecciosas abordan la vacunación y la profilaxis antimicrobiana en adultos con inmunosupresión asociada al cáncer [22,23]. IMMUNO-2 es una representación de trabajo, también de 25 parámetros, para la estratificación del riesgo de infección grave en adultos que reciben inmunosupresión farmacológica sistémica no relacionada con trasplante. Continúa en desarrollo y la revisión especializada del conjunto completo de parámetros aún no ha finalizado. Ninguno de los dos módulos se considera en este estudio un instrumento predictivo validado clínicamente.

P02 es un parámetro compuesto de naturaleza cardiometabólica y renal. La especificación escrita examinada asigna 1 cuando se cumple cualquiera de los criterios positivos declarados relativos a diabetes, insuficiencia cardiaca, función renal o acontecimiento isquémico reciente; asigna 0 cuando no concurre ninguna condición positiva bajo las condiciones especificadas de comorbilidad controlada; y su condición U incluye expresamente la ausencia de información reciente sobre HbA1c o eGFR [24]. La implementación informática y la prueba de conformidad documentada se compararon directamente con estas reglas.

La suficiencia relativa a la operación se examinó de manera independiente mediante dos asignaciones formales con observación completa, ordenadas como `(dm_complicated, HbA1c, NYHA, eGFR, acontecimiento isquémico reciente)`:

`x_DM = (True, 7.0, 0, 90, False)`

`x_CKD = (False, 7.0, 0, 40, False)`

Ambas asignaciones producen `P02=1`, pero por motivos diferentes. En `x_DM`, `dm_complicated=True` satisface la condición de diabetes complicada; HbA1c=7.0 no alcanza el umbral independiente HbA1c≥8. En `x_CKD`, eGFR=40 satisface la condición renal. La comprobación de pérdida de información no depende, por tanto, de datos ausentes.

![Figura 3. P02 muestra dos pruebas metodológicas independientes. El panel A compara la especificación escrita con el resultado del programa ante una entrada documentada. El panel B utiliza asignaciones con observación completa para comprobar si el estado escalar de P02 permite identificar la condición de regla que determinó el resultado; esta segunda prueba solo es pertinente si tal identificación forma parte de la operación declarada.](https://raw.githubusercontent.com/juantoniolloretegea/SV-matematica-semantica/main/documentos/celulas_especializadas_sv/inmunologia/publicaciones/from-frofessional-standards-to-verifiable-representations-a-traceable-method-for-medical-domain-constitution-and-operation-relative-sufficiency/imagenes/Figura3.png)

*Figura 3. P02 muestra dos pruebas metodológicas independientes. El panel A compara la especificación escrita con el resultado del programa ante una entrada documentada. El panel B utiliza asignaciones con observación completa para comprobar si el estado escalar de P02 permite identificar la condición de regla que determinó el resultado; esta segunda prueba solo es pertinente si tal identificación forma parte de la operación declarada.*

### Control positivo: pérdida deliberada de información admisible

La composición experimental IMMUNO-1→IMMUNO-2 transfiere únicamente la clase final de IMMUNO-1 a P25 de IMMUNO-2 [24]. La descripción publicada identifica esta conexión como experimental y no la presenta como validación clínica de una relación causal o predictiva entre profilaxis y riesgo de infección grave. Por ello, se utiliza aquí exclusivamente como control metodológico positivo. Si la operación posterior requiere únicamente la clase final de IMMUNO-1, no es necesario transmitir su estado completo de 25 parámetros. La pérdida de información es admisible cuando las distinciones omitidas no son necesarias para la operación declarada.

### Implicaciones para la implementación en el SV

La especificación publicada del lenguaje declarativo del SV y su interfaz de consulta pública se describen en la referencia 25. El presente estudio no propone sintaxis ni primitivas nuevas. A los efectos del análisis realizado, los requisitos de implementación se limitan a tres puntos: las observaciones deben satisfacer los criterios de admisión antes de la transducción ternaria; el programa debe ejecutar la especificación escrita que sirve de referencia para su evaluación; y una representación debe conservar todas las distinciones necesarias para cada operación para la que se declara suficiente.

### Consideraciones éticas

No se recopilaron ni analizaron participantes humanos, historias clínicas, datos de cohortes, intervenciones clínicas ni conjuntos de datos derivados de pacientes. Las asignaciones formales son entradas construidas para examinar reglas declaradas. El estado ilustrativo de la Figura 2 no representa a un paciente ni constituye evidencia para una recomendación clínica. Por tanto, no resultaba aplicable una evaluación ética de investigación con seres humanos al trabajo aquí presentado.

## Resultados

### La cobertura del conjunto profesional de referencia declarado no equivale a la cobertura de la especialidad

Considerados en conjunto, los cuatro marcos profesionales declarados describen un ámbito que excede ampliamente el de los dos módulos de inmunología examinados. El marco del RACP, por ejemplo, incluye fundamentos de inmunología, inmunodeficiencias, enfermedades autoinmunitarias y autoinflamatorias, alergia e hipersensibilidad, trasplante, vacunación, razonamiento clínico, comunicación, prescripción, procedimientos, mejora de la calidad y otras actividades profesionales [10]. Los sistemas de competencias canadiense y estadounidense presentan una amplitud comparable, mientras que la contribución del GMC corresponde específicamente a un currículo de alergología [11-13]. En cambio, IMMUNO-1 e IMMUNO-2 abordan cuestiones delimitadas de profilaxis infecciosa, vacunación y riesgo de infección grave en poblaciones adultas definidas. La cobertura implementada no puede, por ello, equipararse al ámbito profesional descrito por el conjunto de referencia.

### P02 demuestra una discrepancia entre especificación e implementación

La especificación escrita de P02 y la implementación informática discrepan ante una entrada documentada con información parcial [24]. La prueba de conformidad contiene:

`P02({"dm_complicated": False, "egfr": 90}) == "0"`

pese a que no se proporciona HbA1c. La especificación escrita incluye expresamente la falta de información reciente sobre HbA1c entre las condiciones asignadas a U. La implementación puede, por tanto, devolver 0 para al menos una entrada documentada que la especificación escrita remite a su condición de información no disponible. Esto demuestra una discrepancia reproducible entre la especificación y la implementación examinadas.

Este resultado **no** demuestra que U sea la salida correcta conforme a los requisitos de admisión y no clausura aplicados en el presente estudio. La información no disponible, capturada de forma incompleta o no admitida debe tratarse primero en la fase de admisión y no puede convertirse automáticamente en una U ternaria genuina [18,19,25]. El tratamiento que la especificación concede a la información no disponible requiere, por tanto, una revisión independiente. La fidelidad del programa a una especificación escrita y la adecuación de la propia especificación son cuestiones distintas.

### La suficiencia de P02 depende de la operación declarada

Para las asignaciones con observación completa, `Tri_P02(x_DM) = Tri_P02(x_CKD) = 1`, aunque el valor queda determinado por condiciones de regla diferentes. Por consiguiente, el estado escalar P02 no puede, por sí solo, determinar una operación `Q_basis` definida como la identificación de la condición declarada que determinó dicho estado. Formalmente:

`Tri_P02(x_DM) = Tri_P02(x_CKD)` y `Q_basis(x_DM) ≠ Q_basis(x_CKD)`.

La representación escalar es, por tanto, insuficiente para `Q_basis`. Se trata de un resultado condicional. No demuestra que IMMUNO-2 deba permitir clínicamente la identificación de la condición determinante. Si la operación legítimamente declarada requiere únicamente el estado escalar P02, la representación escalar es suficiente para esa finalidad más restringida.

### La pérdida deliberada de información puede seguir siendo suficiente

La transferencia a P25 proporciona el control inverso. Omite de forma intencionada las distinciones correspondientes a los parámetros individuales de IMMUNO-1 y transmite únicamente su clase final. Si la operación posterior declarada solo requiere dicha clase, las distinciones omitidas carecen de relevancia para esa operación. La suficiencia relativa a la operación no implica, por tanto, una exigencia general de transmitir la representación más rica posible.

### La recuperabilidad del estado destinado al clínico se deriva de la codificación

Con etiquetas de parámetros fijas y una codificación categórica e inyectiva de 0, 1 y U, la representación abstracta `Vis(S)` mantiene una correspondencia biunívoca con el estado ternario etiquetado. La Figura 2 muestra un estado sintético de 25 parámetros con `n0=13`, `n1=5` y `nU=7`. Conforme a la regla declarada de umbral para el estado completo, `T(25)=19`; ni n0 ni n1 alcanzan 19, por lo que el estado sintético global permanece indeterminado. El umbral se aplica al estado completo, no a un parámetro individual. De este resultado no se infiere ninguna conclusión empírica sobre usabilidad o rendimiento clínico.

### Estado del conocimiento y alcance de los resultados

La búsqueda identificó trabajos previos sustanciales sobre guías computables, adaptación digital, determinación de consultas, supervisión humana y visualización clínica [1-9]. No se reivindica novedad para ninguno de esos mecanismos de manera aislada. Las publicaciones anteriores del SV ya habían descrito las células ternarias, la transducción, la representación visual, la semántica basada en sucesos, la no clausura, la autoridad y la pérdida de información en operaciones posteriores a la constitución de un estado etiquetado [14-20,26]. Dentro de la literatura identificada hasta el 26 de agosto de 2026, no se encontró un método materialmente equivalente que reuniera: (1) la definición explícita de un ámbito profesional de referencia antes de representar computacionalmente las reglas operativas; (2) una prueba directa de concordancia entre una especificación escrita y su implementación informática; y (3) una prueba de suficiencia relativa a la operación capaz de identificar pérdida de información durante las fases previas o en el propio momento de constitución del estado ternario. Se trata de un resultado acotado a la búsqueda bibliográfica realizada, no de una demostración de inexistencia universal.

Del presente caso de estudio no se deriva la necesidad de introducir nuevas primitivas en el lenguaje de programación. Los tres requisitos de implementación expuestos pueden expresarse ya como restricciones de admisión, conformidad y operaciones declaradas en la especificación publicada del lenguaje SV [25]. Si en el futuro surgiera un requisito médico que no pudiera representarse fielmente, sería necesario un análisis específico en el nivel del lenguaje; el presente estudio no formula tal afirmación.

## Discusión

La principal contribución es un método para determinar qué condiciones deben cumplirse antes de considerar que una representación computacional constituye una realización adecuada de un ámbito médico declarado. Los métodos existentes para guías clínicas interpretables por ordenador muestran cómo formalizar e implantar recomendaciones [1-4]. El requisito adicional que se introduce aquí consiste en hacer explícito el ámbito profesional de referencia antes de considerar que un módulo implementado representa una especialidad. Los estándares profesionales y la evidencia clínica desempeñan funciones distintas: las fuentes profesionales delimitan competencias, poblaciones y alcance, mientras que la evidencia clínica sustenta las reglas operativas adoptadas para la finalidad declarada.

P02 muestra por qué la fidelidad entre especificación e implementación requiere una comprobación expresa. La concordancia entre varias implementaciones seguiría siendo insuficiente si todas se apartaran de la especificación escrita que afirman ejecutar. A la inversa, la fidelidad no demuestra que la propia especificación sea adecuada. En P02 puede demostrarse que el programa discrepa de la regla escrita ante una entrada documentada, mientras que el tratamiento que esa regla concede a la información no disponible sigue sujeto al requisito independiente de que la admisión preceda a la asignación ternaria. Ambas evaluaciones responden a preguntas diferentes y no deben reducirse a un único juicio de corrección.

La suficiencia relativa a la operación aborda un problema distinto. Comprimir varias condiciones clínicas diferentes en un único estado escalar elimina necesariamente la información que identifica cuál de ellas determinó ese estado. Esto no constituye por sí mismo un defecto. La cuestión pertinente es si una operación legítimamente declarada necesita la distinción descartada. Las dos asignaciones de P02 con observación completa demuestran la pérdida de información sobre la condición determinante sin recurrir a datos ausentes; la transferencia a P25 demuestra que una reducción intencionada puede resultar plenamente adecuada cuando la operación posterior solo necesita la clase transmitida. Un trabajo anterior del SV estudió la pérdida de información dependiente de la operación una vez constituido un estado ternario etiquetado [26]. El método presente extiende el análisis a las fases precedentes: definición del ámbito profesional, admisión de observaciones y transducción.

El gobierno humano delimita el alcance clínico de estas comprobaciones formales. Una supervisión efectiva exige más que una presencia humana nominal [6-8]. En el método estudiado, la inteligencia artificial no se considera un decisor clínico cuya conclusión se limite a ser aprobada por un profesional. Los componentes computacionales y de inteligencia artificial pueden recuperar, estructurar, comparar, calcular o proponer información, mientras que el experto cualificado conserva la responsabilidad sobre la constitución del dominio médico, la interpretación, la revisión y las actuaciones clínicas con consecuencias para el paciente. El resultado relativo a la representación visual es deliberadamente limitado: el estado ternario etiquetado puede recuperarse de la codificación abstracta. Determinar si esa representación mejora el desempeño clínico exige investigación empírica posterior sobre factores humanos.

El método preserva asimismo la trazabilidad temporal. Una U genuinamente constituida puede permanecer sin clausura cuando la evidencia disponible y el mecanismo aplicable no justifican una resolución. Si una evidencia posterior permite una resolución sometida al gobierno establecido, un suceso ulterior puede registrarla sin modificar el estado previo como si la no clausura nunca hubiera existido [18,19]. Se trata de una propiedad lógica de la traza; el almacenamiento duradero y la conservación para auditoría constituyen requisitos de implementación diferentes.

El estudio presenta varias limitaciones. La inmunología es el único caso médico analizado; por tanto, será necesario evaluar el método en otras especialidades antes de establecer una aplicabilidad más amplia. Los cuatro marcos profesionales son referencias deliberadamente delimitadas y no demuestran una cobertura universal ni completa de la especialidad. IMMUNO-2 continúa en desarrollo y aún no ha finalizado la revisión especializada del conjunto completo de parámetros. El resultado de P02 relativo a la identificación de la condición determinante depende de que esa función forme parte de una operación declarada. El resultado visual se refiere a recuperabilidad formal, no a usabilidad. La búsqueda bibliográfica fue intensiva y orientada a mecanismos, pero no sistemática. Por último, la conclusión relativa al lenguaje público del SV queda restringida a los requisitos demostrados en este caso de estudio y no implica que el lenguaje sea completo.

## Conclusiones

Una representación computacional de un dominio médico no es adecuada por el mero hecho de que pueda codificarse una regla o de que un programa produzca una salida. Debe declararse el ámbito profesional; la evidencia clínica y el gobierno experto cualificado deben sustentar las reglas operativas; las observaciones deben satisfacer criterios explícitos de admisión antes de la asignación ternaria; el programa debe concordar con la especificación escrita que sirve de referencia para la evaluación; y cada representación debe conservar las distinciones necesarias para todas las operaciones que declare poder sostener. En el caso de estudio de inmunología, P02 demuestra tanto una discrepancia reproducible entre especificación e implementación como una pérdida condicional de información sobre la condición de regla que determina un estado escalar, mientras que la transferencia experimental a P25 muestra que una reducción deliberada de información puede ser plenamente admisible. El método propuesto es un procedimiento trazable de constitución y verificación del dominio, no un agente autónomo validado clínicamente.

## Disponibilidad de datos y código

Los resultados no se basan en datos de pacientes ni de cohortes. Las especificaciones e implementaciones de trabajo de inmunología están disponibles públicamente en el repositorio [**SVperitus-dataset**](https://github.com/juantoniolloretegea/SVperitus-dataset) de GitHub. Para reproducir exactamente la comparación de P02 se utilizó el *commit* `1b2838a1c594a1f84b543e7e9c333f9f8e8c55dd`; la prueba de conformidad pertinente es `especificaciones/conformidad/test_immuno2.py` [24]. La especificación publicada del lenguaje SV y su interfaz de consulta pública se identifican en la referencia 25.

## Referencias

1. Peleg M. Computer-interpretable clinical guidelines: a methodological review. J Biomed Inform. 2013;46(4):744-763. doi:10.1016/j.jbi.2013.06.009.

2. Boxwala AA, Peleg M, Tu S, et al. GLIF3: a representation format for sharable computer-interpretable clinical practice guidelines. J Biomed Inform. 2004;37(3):147-161. doi:10.1016/j.jbi.2004.04.002.

3. Nan S, Tang T, Feng H, et al. A Computer-Interpretable Guideline for COVID-19: Rapid Development and Dissemination. JMIR Med Inform. 2020;8(10):e21628. doi:10.2196/21628.

4. Mehl G, Tunçalp Ö, Ratanaprayul N, et al. WHO SMART guidelines: optimising country-level use of guideline recommendations in the digital age. Lancet Digit Health. 2021;3(4):e213-e216. doi:10.1016/S2589-7500(21)00038-8.

5. Nash A, Segoufin L, Vianu V. Views and Queries: Determinacy and Rewriting. ACM Trans Database Syst. 2010;35(3):Article 21. doi:10.1145/1806907.1806913.

6. Lekadir K, Frangi AF, Porras AR, et al; FUTURE-AI Consortium. FUTURE-AI: international consensus guideline for trustworthy and deployable artificial intelligence in healthcare. BMJ. 2025;388:e081554. doi:10.1136/bmj-2024-081554.

7. Strong J, Rogers H, Sun E, et al. Human-AI Collaboration in Healthcare: A Scoping Review. npj Digit Med. Published online June 20, 2026. doi:10.1038/s41746-026-02918-6.

8. van de Sande D, Economou-Zavlanos N, van Genderen ME. Meaningful oversight of medical AI beyond human in the loop. npj Digit Med. 2026;9:569. doi:10.1038/s41746-026-02971-1.

9. Müller J, Stoehr M, Oeser A, et al. A visual approach to explainable computerized clinical decision support. Comput Graph. 2020;91:1-11. doi:10.1016/j.cag.2020.06.004.

10. Royal Australasian College of Physicians. Clinical Immunology and Allergy - Advanced Training; Advanced Training in Immunology and Allergy curriculum standards. Nuevo currículo aprobado en marzo de 2025; implantación a partir de 2027. Consultado el 26 de agosto de 2026. https://www.racp.edu.au/trainees/advanced-training/clinical-immunology-and-allergy

11. Royal College of Physicians and Surgeons of Canada. Clinical Immunology and Allergy Competencies. Version 2.0. 2025. Effective July 1, 2025.

12. General Medical Council. Allergy curriculum. Current curriculum: Allergy curriculum 2021. Página publicada el 1 de marzo de 2023. Consultada el 26 de agosto de 2026. https://www.gmc-uk.org/education/standards-guidance-and-curricula/curricula/allergy-curriculum

13. Accreditation Council for Graduate Medical Education. ACGME Program Requirements for Graduate Medical Education in Allergy and Immunology. 2026. https://www.acgme.org/globalassets/pfassets/programrequirements/2026-prs/020_allergyimmunology_2026.pdf

14. Lloret Egea JA. Fundamentos algebraico-semánticos del Sistema Vectorial SV. IA eñ. Publicado el 9 de marzo de 2026. doi:10.21428/39829d0b.b0cf9a13. [Prepublicación en español].

15. Lloret Egea JA. Álgebra de composición intercelular del marco SV-IV. Transducción al alfabeto ternario e interfaz paramétrica del sistema. IA eñ. Publicado el 11 de marzo de 2026. doi:10.21428/39829d0b.5c31d534. [Prepublicación en español].

16. Lloret Egea JA. Formalización de una interfaz visual estructurada en el Sistema Vectorial SV. IA eñ. Publicado el 17 de marzo de 2026. doi:10.21428/39829d0b.b96fee32. [Prepublicación en español].

17. Lloret Egea JA. Fundamentos, exigencias y arquitectura general de los agentes especializados en el Sistema Vectorial SV: formulación transversal desde el caso director del Agente Especializado en Inmunología. IA eñ. Publicado el 12 de abril de 2026. doi:10.21428/39829d0b.183e10f3. [Prepublicación en español].

18. Lloret Egea JA. Semántica auditada en el Sistema Vectorial SV: formalización estructural basada en sucesos, transducción ternaria y clausura trazable. Prepublicación. Publicado el 17 de marzo de 2026. doi:10.21428/39829d0b.f471b07c. [En español].

19. Lloret Egea JA. Certified non-closure in finite resolution systems: operational certificates, conservative morphisms and revision complexity. IA eñ. Publicado el 8 de agosto de 2026. doi:10.21428/39829d0b.f0892864.

20. Lloret Egea JA. Informational Substitution Does Not Transfer Authority in AI-Assisted Decision Systems. Prepublicación. Publicado el 14 de agosto de 2026. doi:10.21428/39829d0b.d6cb2e1d.

21. Lloret Egea JA. De SVcustos, el marco de intrusión, hasta SVperitus: IMMUNO-1 - Profilaxis infecciosa y vacunación. Célula SV(25,5). IA eñ. Publicado el 5 de marzo de 2026. doi:10.21428/39829d0b.272c2f67. [Prepublicación en español].

22. Kamboj M, Bohlke K, Baptiste DM, et al. Vaccination of adults with cancer: ASCO guideline. J Clin Oncol. 2024;42(14):1699-1721. doi:10.1200/JCO.24.00032.

23. Taplitz RA, Kennedy EB, Bow EJ, et al. Antimicrobial prophylaxis for adult patients with cancer-related immunosuppression: ASCO and IDSA clinical practice guideline update. J Clin Oncol. 2018;36(30):3043-3054. doi:10.1200/JCO.18.00374.

24. Lloret Egea JA. SVperitus-dataset [programa informático y especificaciones]. GitHub. Repositorio: juantoniolloretegea/SVperitus-dataset. Análisis reproducible de P02: *commit* 1b2838a1c594a1f84b543e7e9c333f9f8e8c55dd, 24 de agosto de 2026. Consultado el 26 de agosto de 2026. https://github.com/juantoniolloretegea/SVperitus-dataset

25. Lloret Egea JA. SV-lenguaje-de-computacion [programa informático y especificación del lenguaje]. GitHub. Repositorio: juantoniolloretegea/SV-lenguaje-de-computacion. Interfaz pública accesible mediante navegador: https://lenguaje-sv.itvia.online/. Consultado el 26 de agosto de 2026. https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion

26. Lloret Egea JA. Resolution Frontiers in Stratified Ternary Cells: Infection Prophylaxis, Vaccination, and AI System Integrity. Prepublicación. Publicado el 20 de agosto de 2026. doi:10.21428/39829d0b.739ed2b6.


## Cláusulas legales generales de adscripción editorial, reserva de derechos y desarrollos derivados

Identificación editorial, bibliográfica y lingüística

Esta obra, publicación, anexo, trabajo derivado, archivo técnico, material complementario, desarrollo científico, contenido gráfico, tabla, cálculo, formulación, edición digital o cualquier otro contenido vinculado queda adscrito, salvo indicación expresa en contrario, a la publicación matriz:

De los Principios y Matemática y Filosofía del ConocimientoDOI: https://doi.org/10.21428/39829d0b.b6a73a9bInstituto Tecnológico Virtual de la Inteligencia Artificial para el Español®© 2020–2026 Juan Antonio Lloret EgeaLa Biblia de la IA — The Bible of AI® | ISSN 2695-6411

IA eñ™ opera como entorno editorial y suplemento interno de la publicación matriz La Biblia de la IA — The Bible of AI® | ISSN 2695-6411, bajo el sello del Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español® (ITVIA). Su autonomía organizativa no altera la identificación bibliográfica de la publicación matriz ni la titularidad intelectual de los contenidos incorporados, vinculados, derivados o publicados bajo su órbita editorial.

El objetivo principal de esta línea editorial es potenciar el español como lengua de producción, formalización, publicación y transmisión científico-técnica. Asimismo, se permite la publicación conjunta con lenguas vernáculas de la Unión Europea como lenguas secundarias o complementarias. Cuando se publique contenido en otra lengua, la versión española deberá estar presente conjuntamente, salvo imposibilidad técnica justificada o decisión editorial expresa.

Advertencia y reserva de derechos

Esta obra, incluida la totalidad de sus textos, formulaciones, estructura expositiva, tablas, cálculos, criterios de admisión, nomenclatura, dominios, tramos, residuales, retornos metrológicos, porcentajes, diferencias formales, archivos auxiliares, imágenes, portadas, materiales gráficos, bancos de contraste, documentación técnica, anexos, desarrollos complementarios y cualquier otro material que forme parte de ella o se publique vinculado a ella, queda protegida por los derechos de propiedad intelectual de su autor y, en su caso, por la gestión de derechos que corresponda a través de CEDRO u otra entidad competente.

Cualquier forma de explotación de la obra o de partes sustanciales de ella —incluidas su reproducción, distribución, comunicación pública, puesta a disposición, transformación, traducción, adaptación, incorporación a bases de datos, minería de textos y datos, entrenamiento o evaluación de sistemas automatizados, integración en productos, servicios, informes, software, modelos, catálogos, materiales docentes, materiales industriales, publicaciones técnicas, desarrollos empresariales, sistemas de inteligencia artificial o herramientas de análisis científico— sólo podrá realizarse conforme a la licencia indicada, con autorización expresa y por escrito de los titulares de derechos, o al amparo de una excepción legal aplicable.

La licencia indicada, CC BY-NC-ND 4.0, no autoriza usos comerciales, explotación empresarial, transformación distribuida, publicación de obras derivadas ni reutilización sustancial de la obra fuera de sus términos. La cita, la crítica científica, la revisión académica, el comentario, la referencia bibliográfica y el contraste independiente quedan permitidos dentro de los límites legales aplicables y con respeto a la autoría, integridad de la obra, licencia y condiciones de uso.

La aplicación, implementación, explotación técnica o incorporación de los resultados, fórmulas, tablas, nomenclatura, metodología, criterios de admisión, dominios, tramos, residuales, retornos, transductores, estructuras formales, sistemas de cálculo, matrices de análisis, reglas de recomposición, modelos de contraste, arquitecturas conceptuales o desarrollos científicos incluidos en esta obra queda reservada a la autorización expresa del autor cuando implique reproducción, transformación, comunicación pública, distribución, integración sustancial de la obra protegida, explotación comercial, desarrollo empresarial o uso no cubierto por la licencia.

Esta reserva alcanza, cuando proceda, a los campos de la física, matemática, cosmología, astronomía, química, biología, medicina, ingeniería, inteligencia artificial, ciencia de datos, metrología, docencia técnica, edición científica, modelización computacional, sistemas de evaluación científica, herramientas de análisis formal y cualquier otro ámbito de aplicación científica, técnica, editorial o industrial que reutilice sustancialmente la formulación protegida.

La presente reserva se formula sin perjuicio de los límites, excepciones y usos permitidos imperativamente por la ley. En la medida permitida por la legislación aplicable, cualquier controversia relativa a la explotación no autorizada, transformación, reutilización sustancial, comunicación pública, distribución, integración técnica, uso comercial, uso automatizado no autorizado, atribución indebida, alteración sustancial o vulneración de derechos sobre esta obra se someterá a la jurisdicción de los órganos competentes conforme al ordenamiento jurídico aplicable.

Notice and reservation of rights

This work, including the entirety of its texts, formulations, expository structure, tables, calculations, admission criteria, nomenclature, domains, intervals, residuals, metrological returns, percentages, formal differences, auxiliary files, images, covers, graphic materials, contrast datasets, technical documentation, annexes, supplementary developments and any other material forming part of it or published in connection with it, is protected by the intellectual property rights of its author and, where applicable, by the corresponding rights management through CEDRO or any other competent entity.

Any form of exploitation of the work or of substantial parts thereof —including reproduction, distribution, public communication, making available, transformation, translation, adaptation, incorporation into databases, text and data mining, training or evaluation of automated systems, integration into products, services, reports, software, models, catalogues, teaching materials, industrial materials, technical publications, business developments, artificial intelligence systems or scientific analysis tools— may only be carried out in accordance with the indicated licence, with the express written authorisation of the rights holders, or under an applicable statutory exception.

The indicated licence, CC BY-NC-ND 4.0, does not authorise commercial uses, business exploitation, distributed transformation, publication of derivative works or substantial reuse of the work outside its terms. Quotation, scientific criticism, academic review, commentary, bibliographic reference and independent contrast remain permitted within the applicable legal limits and with due respect for authorship, integrity of the work, licence and terms of use.

The application, implementation, technical exploitation or incorporation of the results, formulas, tables, nomenclature, methodology, admission criteria, domains, intervals, residuals, returns, transducers, formal structures, calculation systems, analytical matrices, recomposition rules, contrast models, conceptual architectures or scientific developments included in this work is reserved to the express authorisation of the author where it entails reproduction, transformation, public communication, distribution, substantial integration of the protected work, commercial exploitation, business development or any use not covered by the licence.

This reservation applies, where relevant, to the fields of physics, mathematics, cosmology, astronomy, chemistry, biology, medicine, engineering, artificial intelligence, data science, metrology, technical teaching, scientific publishing, computational modelling, scientific assessment systems, formal analysis tools and any other scientific, technical, editorial or industrial field that substantially reuses the protected formulation.

This reservation is made without prejudice to limitations, exceptions and uses that are mandatorily permitted by law. To the extent permitted by applicable law, any dispute concerning unauthorised exploitation, transformation, substantial reuse, public communication, distribution, technical integration, commercial use, unauthorised automated use, improper attribution, substantial alteration or infringement of rights over this work shall be subject to the jurisdiction of the competent courts and authorities under the applicable legal order.

Disposición sobre propiedad intelectual, desarrollos derivados, colaboración técnica y reserva de explotación

La formulación científica, técnica, matemática, conceptual, editorial o metodológica de esta obra puede dar lugar a desarrollos posteriores en ciencias formales, ciencias naturales, ciencias biomédicas, ingeniería, metrología, modelización matemática, análisis de dominios, sistemas de representación, transductores, criterios de admisión de datos externos, herramientas computacionales, aplicaciones docentes avanzadas, sistemas de evaluación científica, entornos editoriales, inteligencia artificial o integraciones técnicas en plataformas digitales.

La publicación, difusión o puesta a disposición de la obra no constituye cesión, licencia, autorización de explotación técnica ni renuncia a derechos de propiedad intelectual, industrial o de explotación sobre métodos, procedimientos, criterios técnicos, matrices de análisis, secuencias de cálculo, modelos de transducción, sistemas de decisión, estructuras de retorno, aplicaciones científicas, sistemas editoriales o desarrollos derivados que puedan resultar registrables, protegibles, explotables mediante licencia, transferencia, acuerdo de colaboración, investigación conjunta o secreto empresarial.

Cualquier universidad, laboratorio, centro tecnológico, entidad pública o privada, empresa, grupo de investigación, editor técnico, desarrollador de software, proveedor de sistemas de inteligencia artificial, institución educativa, plataforma editorial o entidad que pretenda ejecutar, validar, ampliar, adaptar, automatizar, integrar, explotar técnicamente o reutilizar sustancialmente la metodología, las fórmulas, las tablas, los criterios de admisión, las reglas de residual, los transductores, los dominios, los sistemas de cálculo, la arquitectura formal o la estructura general de esta obra deberá formalizar previamente un acuerdo escrito con el autor o con la entidad designada por éste cuando el uso proyectado exceda la cita, la crítica, la revisión académica, la lectura privada o el contraste independiente permitido por la ley y por la licencia.

El acuerdo podrá reconocer, según corresponda, participación técnica, preferencia de colaboración, coautoría científica, licencia, derechos de explotación, opción de desarrollo, cotitularidad de resultados derivados o condiciones específicas de transferencia científica y tecnológica, siempre que la contribución material de la parte colaboradora quede documentada y aceptada por escrito. La aceptación de archivos, lectura de la obra, comentario técnico, revisión interna, comunicación informal, cita, análisis automatizado no autorizado, uso interno no autorizado o recepción de materiales no generará por sí sola derechos de explotación, prioridad técnica, licencia implícita ni expectativa jurídica sobre los métodos, formulaciones, estructuras, criterios o desarrollos derivados.

Esta disposición no limita la crítica científica, la revisión académica, la comprobación independiente, la cita legítima ni los usos permitidos por la ley. Su finalidad es preservar la trazabilidad de autoría, la integridad formal de la obra, la eventual protección jurídica de desarrollos posteriores y la ordenación de futuras colaboraciones técnicas.

Provision on intellectual property, derived developments, technical collaboration and reservation of exploitation rights

The scientific, technical, mathematical, conceptual, editorial or methodological formulation of this work may give rise to subsequent developments in formal sciences, natural sciences, biomedical sciences, engineering, metrology, mathematical modelling, domain analysis, representation systems, transducers, criteria for admitting external data, computational tools, advanced teaching applications, scientific assessment systems, editorial environments, artificial intelligence or technical integrations in digital platforms.

Publication, dissemination or making available of the work does not constitute assignment, licence, authorisation for technical exploitation or waiver of intellectual, industrial or exploitation rights over methods, procedures, technical criteria, analytical matrices, calculation sequences, transduction models, decision systems, return structures, scientific applications, editorial systems or derived developments that may be registrable, protectable, exploitable through licensing, transfer, collaboration agreements, joint research or trade secrets.

Any university, laboratory, technology centre, public or private entity, company, research group, technical publisher, software developer, artificial intelligence system provider, educational institution, editorial platform or entity intending to execute, validate, expand, adapt, automate, integrate, technically exploit or substantially reuse the methodology, formulas, tables, admission criteria, residual rules, transducers, domains, calculation systems, formal architecture or general structure of this work must first formalise a written agreement with the author or with the entity designated by him where the intended use exceeds quotation, criticism, academic review, private reading or independent contrast permitted by law and by the licence.

The agreement may recognise, as appropriate, technical participation, collaboration preference, scientific co-authorship, licence, exploitation rights, development option, co-ownership of derived results or specific scientific and technology-transfer conditions, provided that the material contribution of the collaborating party is documented and accepted in writing. Acceptance of files, reading of the work, technical comment, internal review, informal communication, citation, unauthorised automated analysis, unauthorised internal use or receipt of materials shall not by itself generate exploitation rights, technical priority, implied licence or legal expectation over the methods, formulations, structures, criteria or derived developments.

This provision does not limit scientific criticism, academic review, independent verification, legitimate quotation or uses permitted by law. Its purpose is to preserve authorship traceability, the formal integrity of the work, possible legal protection of subsequent developments and the organisation of future technical collaborations.

Cláusula de adscripción lingüística y publicación multilingüe

El idioma principal de esta línea editorial es el español. La finalidad lingüística del Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español® y de IA eñ™ es promover el español como lengua de producción científica, técnica, filosófica, matemática, editorial y computacional.

La publicación conjunta en otras lenguas vernáculas de la Unión Europea podrá admitirse como modalidad secundaria, complementaria o comparativa, siempre que se conserve la versión española de forma conjunta, visible y suficientemente completa. La versión en otra lengua no sustituye por sí sola a la versión española ni desplaza la identificación editorial de la publicación matriz, salvo acuerdo o indicación editorial expresa.

Cuando existan versiones bilingües o multilingües, la versión española conservará la función de referencia editorial principal, salvo que una obra concreta declare otra regla por razones técnicas, jurídicas, académicas o de depósito. Las traducciones, adaptaciones lingüísticas, versiones abreviadas, resúmenes técnicos y materiales auxiliares deberán respetar la autoría, la integridad conceptual de la obra, la licencia aplicable y la adscripción bibliográfica a la publicación matriz.

Linguistic affiliation and multilingual publication clause

The primary language of this editorial line is Spanish. The linguistic purpose of the Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español® and IA eñ™ is to promote Spanish as a language of scientific, technical, philosophical, mathematical, editorial and computational production.

Joint publication in other vernacular languages of the European Union may be admitted as a secondary, complementary or comparative modality, provided that the Spanish version is preserved jointly, visibly and sufficiently. A version in another language does not by itself replace the Spanish version or displace the editorial identification of the parent publication, unless an express agreement or editorial indication provides otherwise.

Where bilingual or multilingual versions exist, the Spanish version shall retain the function of primary editorial reference, unless a specific work declares another rule for technical, legal, academic or deposit-related reasons. Translations, linguistic adaptations, abridged versions, technical summaries and auxiliary materials must respect authorship, the conceptual integrity of the work, the applicable licence and the bibliographic affiliation to the parent publication.
