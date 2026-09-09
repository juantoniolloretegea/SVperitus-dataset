# Acta de ampliación atómica y cobertura de OP-CYB-001

**Versión 0.3 · 9 de septiembre de 2026.** Sucesión motivada del inventario de 24 definiciones. Trabajo documental autorizado; adopción para un consejo real y permisos materiales no derivados de esta acta.

## 1. Adjudicación y criterios

Se conservan literalmente P01–P24 del catálogo v0.8. Se adjudican P25–P32 porque cada definición expresa una relación individual identificada, tiene condiciones de 1, 0 y U, conserva observación y consecuencias propias y admite variación independiente de otras relaciones pertinentes. La coincidencia con un resultado calculable no convierte una conclusión compuesta en átomo.

La procedencia admisible de las referencias, el ámbito aplicable y el perfil de observación se resuelven antes de interpretar un valor. NO_ADMISION, NO_APLICABLE y FALLO_TECNICO son resultados del procedimiento documental externo, no valores añadidos a Tri. Dentro del dominio, el alfabeto permanece 0, 1 y U. El 1 de P29 expresa revocación que afecta al acto y no es un resultado favorable.

Las relaciones se refieren a objetos previamente fijados. Una pertenencia individual no acredita todos los permisos de una persona; una desigualdad entre titulares no acredita independencia institucional completa. Un uso posterior no altera la identidad de una definición. El número 32 no constituye ni dimensiona células; se conserva SV(9,3) como mínimo sin leerlo como 3×3, sin relleno ni redondeo.

## 2. Contratos de las ocho definiciones

### P25 · Vinculación de un acto con una sesión

Identidad estable: `PAR-CYB-ACTO-SESION-VINCULADOS-001`. Versión 0.1.

| Elemento | Contrato |
| --- | --- |
| Sujeto | Un acto individual y una sesión identificada del sistema que lo ejecutó |
| Proposición | El acto identificado está vinculado a la sesión de referencia por la relación de atribución admitida. |
| Valor 1 | Relación explícita y coherente entre ese acto y esa sesión. |
| Valor 0 | Relación completa que atribuye el acto a otra sesión y excluye la de referencia. |
| Indeterminación U | Sólo consta un nombre, la relación está incompleta o hay atribuciones incompatibles. |
| Observación y perfil | Identificadores de acto, sesión y emisor; referencia del registro de correlación y perfil de observación. El nombre de cuenta o la proximidad temporal no bastan. El resultado de autenticación se registra aparte como uso específico de P07; no demuestra quién controló físicamente una credencial robada. |

**Conocimiento y consecuencia.** Autenticar una sesión y atribuirle un acto son relaciones diferentes. Acto → sesión → principal declarado; la correspondencia con persona responsable exige evidencia propia, sin publicar esa identidad en la vista general. Si se omite ese enlace: Un cambio ejecutado por otra sesión puede atribuirse al técnico legítimo y ocultar la intervención ajena. El exceso también tiene un límite: Una atribución incompleta no permite acusar a una persona ni borrar el resultado técnico observado.

**Independencia frente a P02 y P07/autenticación.** Dos instalaciones satisfactorias y una misma sesión autenticada; sólo una conserva la relación de ejecución con esa sesión. **Partición examinada.** La identidad compuesta identifica un acto; se adjudica una sola arista, no toda la cadena de responsabilidad.

Fundamento profesional: N01 art. 24, anexo II op.acc.1 y op.exp.8; N09, gestión de usuarios; ADJ1 §2.3. Localizadores y enlaces en la [bibliografía](BIBLIOGRAFIA_DE_PRESION_OP_CYB_001_v0.3.md). La fuente no enumera este átomo; la adjudicación es propia.

### P26 · Competencia del emisor de una autorización

Identidad estable: `PAR-CYB-EMISOR-COMPETENTE-001`. Versión 0.1.

| Elemento | Contrato |
| --- | --- |
| Sujeto | Un emisor, una facultad concreta y el instante de emisión de una autorización |
| Proposición | El emisor figura como titular de la facultad de conceder esa autorización en el registro institucional aplicable al instante de emisión. |
| Valor 1 | Correspondencia positiva con la atribución institucional vigente en ese instante. |
| Valor 0 | Registro completo que excluye expresamente esa facultad para el emisor. |
| Indeterminación U | Competencia, vigencia o registro institucional insuficientemente acreditados. |
| Observación y perfil | Anclaje de autoridad fijado por la organización competente; historial de atribuciones y facultad individual. La verificación de firma no crea competencia. La cadena de delegación se resuelve por aristas; su legitimidad conjunta no se oculta en este parámetro. |

**Conocimiento y consecuencia.** La identidad de un firmante no determina las facultades que le atribuye una organización. Emisor → facultad institucional; después se examinan alcance, tiempo y revocación del permiso emitido. Si se omite ese enlace: Un documento firmado por un proveedor o por un agente sin facultad puede presentarse como autorización institucional. El exceso también tiene un límite: No se presume incompetencia por falta de acceso del observador al registro; se conserva U.

**Independencia frente a P27.** Un emisor competente puede conceder permiso para otro activo; un emisor incompetente puede escribir un alcance aparentemente exacto. **Partición examinada.** La facultad individual se fija antes de consultar; no se agregan todas las competencias de la persona.

Fundamento profesional: N01 arts. 11, 21 y op.acc.4; N06 §2.1; N10 §1.1. Localizadores y enlaces en la [bibliografía](BIBLIOGRAFIA_DE_PRESION_OP_CYB_001_v0.3.md). La fuente no enumera este átomo; la adjudicación es propia.

### P27 · Pertenencia del acto al alcance de un permiso

Identidad estable: `PAR-CYB-ALCANCE-PERMISO-001`. Versión 0.1.

| Elemento | Contrato |
| --- | --- |
| Sujeto | Un permiso y un acto individual con recurso, acción, destinatario y finalidad declarados |
| Proposición | La tupla del acto pertenece al conjunto de actuaciones que declara el permiso de referencia. |
| Valor 1 | Pertenencia acreditada bajo la regla de alcance previamente fijada. |
| Valor 0 | Exclusión acreditada de la tupla del acto. |
| Indeterminación U | Finalidad, recurso, acción, destinatario o regla de pertenencia indeterminados. |
| Observación y perfil | Perfil documental PR-ALC/1: conjunto finito explícito de tuplas exactas. No admite comodines interpretados por el auxiliar. Las restricciones adicionales del permiso se conservan y evalúan separadamente; una política más rica requiere su perfil y no se aproxima por este conjunto. |

**Conocimiento y consecuencia.** Un permiso identifica aquello que permite; la posesión de una credencial no amplía ese alcance. Permiso → acto/recurso/finalidad; cada eslabón de delegación conserva su alcance y no puede ampliarlo. Si se omite ese enlace: Se puede legitimar un reinicio en otro servicio, una exportación de registros no prevista o el uso de credenciales por otro agente. El exceso también tiene un límite: La exclusión de este permiso no demuestra que no exista otro permiso aplicable; la cobertura de autorizaciones se comprueba aparte.

**Independencia frente a P26 y P28.** Un permiso auténtico emitido por autoridad competente puede estar vigente y excluir el activo o destinatario del acto. **Partición examinada.** Acción y recurso fijan el sujeto relacional de la pertenencia. Los incumplimientos de campos se explican; no se crean átomos por cada palabra de la tupla.

Fundamento profesional: N01 op.acc.4; N06 §2.1; N10 §§1.1 y 2.1; ADJ1 §2.3. Localizadores y enlaces en la [bibliografía](BIBLIOGRAFIA_DE_PRESION_OP_CYB_001_v0.3.md). La fuente no enumera este átomo; la adjudicación es propia.

### P28 · Inclusión temporal del acto en la vigencia declarada

Identidad estable: `PAR-CYB-INTERVALO-PERMISO-001`. Versión 0.1.

| Elemento | Contrato |
| --- | --- |
| Sujeto | Un permiso y el intervalo de ejecución de un acto individual |
| Proposición | Todo el intervalo posible del acto queda comprendido en el intervalo de vigencia declarado por ese permiso. |
| Valor 1 | Inclusión completa para todos los tiempos compatibles con la evidencia admitida. |
| Valor 0 | La evidencia demuestra que el acto no quedó íntegramente incluido. |
| Indeterminación U | La incertidumbre del reloj o de los extremos permite tanto inclusión como incumplimiento. |
| Observación y perfil | Perfil PR-TIEMPO/1: intervalos cerrados, escala común y precisión declarada; enteros decimales exactos conservados como texto. No confundir hora del registro, del sellado, de observación y del acto. Límites abiertos o reglas de zona horaria requieren otro perfil explícito. |

**Conocimiento y consecuencia.** La fecha escrita en un documento y el tiempo acreditado de la actuación no son intercambiables. Intervalo del acto frente a vigencia; la emisión previa y la revocación se contrastan por separado. Si se omite ese enlace: Un acto posterior a la caducidad puede aconsejarse como autorizado, o puede ignorarse que el permiso caducó durante la actuación. El exceso también tiene un límite: La superposición incierta no se transforma en infracción demostrada ni en permiso vigente.

**Independencia frente a P29 y P30.** El intervalo puede estar incluido en la vigencia nominal aunque el permiso ya estuviera revocado o se hubiese emitido después con fecha retroactiva. **Partición examinada.** La inclusión de un intervalo es una relación única. Sus extremos son observables del mismo objeto temporal, no dos permisos.

Fundamento profesional: N03B arts. 41.1–2 y 42.1; N03C art. 1, puntos 41–42; N06 §2.1; N01 op.exp.8. Localizadores y enlaces en la [bibliografía](BIBLIOGRAFIA_DE_PRESION_OP_CYB_001_v0.3.md). La fuente no enumera este átomo; la adjudicación es propia.

### P29 · Revocación que afecta a la actuación

Identidad estable: `PAR-CYB-REVOCACION-AFECTA-001`. Versión 0.1.

| Elemento | Contrato |
| --- | --- |
| Sujeto | Un permiso, un acto y el historial competente de revocación |
| Proposición | Existe una revocación efectiva de ese permiso no posterior al final del acto. |
| Valor 1 | Revocación pertinente inequívocamente efectiva antes de terminar el acto o durante él. |
| Valor 0 | Historia completa que acredita ausencia de revocación pertinente hasta el final del acto. |
| Indeterminación U | Historia incompleta, efectividad desconocida o solapamiento temporal que impide resolver. |
| Observación y perfil | PR-TIEMPO/1; se distinguen emisión, publicación, recepción y efecto de la revocación. La regla jurídica o institucional determina el efecto. La revocación posterior al final no se aplica retroactivamente por el simple hecho de conocerla después. Una nueva concesión posee otra identidad. |

**Conocimiento y consecuencia.** El intervalo nominal de un permiso puede seguir abierto después de su retirada. Revocación → permiso → actos afectados en su horizonte; se conserva la historia anterior. Si se omite ese enlace: Una sesión o agente puede seguir figurando como autorizado después de la retirada de su facultad. El exceso también tiene un límite: No se invalida retroactivamente un acto anterior por una revocación posterior, salvo regla explícita aplicable.

**Independencia frente a P28.** Un permiso no caducado puede estar revocado; un permiso caducado puede no haber sufrido revocación alguna. **Partición examinada.** Existencia de un suceso de revocación pertinente, con cobertura del historial. No reúne caducidad y revocación.

Fundamento profesional: N09, gestión de usuarios; N06 §2.1; N01 op.acc.1 y op.acc.4. Localizadores y enlaces en la [bibliografía](BIBLIOGRAFIA_DE_PRESION_OP_CYB_001_v0.3.md). La fuente no enumera este átomo; la adjudicación es propia.

### P30 · Precedencia de la emisión de una autorización

Identidad estable: `PAR-CYB-AUTORIZACION-PREVIA-001`. Versión 0.1.

| Elemento | Contrato |
| --- | --- |
| Sujeto | Una autorización identificada y el comienzo de un acto |
| Proposición | La emisión efectiva de la autorización precedió al comienzo de la actuación. |
| Valor 1 | La emisión ocurrió estrictamente antes de comenzar, con orden acreditado. |
| Valor 0 | La emisión ocurrió después de comenzar o fue simultánea según el perfil temporal exacto. |
| Indeterminación U | Los intervalos de incertidumbre no permiten establecer el orden estricto. |
| Observación y perfil | PR-TIEMPO/1; se compara tiempo de emisión acreditado con comienzo, no fecha redactada retrospectivamente. Este átomo sólo describe precedencia; el régimen de urgencia o autorización permanente es contexto y puede aportar otro permiso válido anterior. |

**Conocimiento y consecuencia.** Ratificar después y autorizar antes son sucesos distintos. Emisión → inicio del acto; plan, alcance y vigencia no sustituyen ese orden. Si se omite ese enlace: Una aprobación posterior puede encubrir que el experto no autorizó la actuación cuando todavía podía decidirla. El exceso también tiene un límite: Un acto urgente no se califica por automatismo: se examina si estaba amparado por una autorización permanente u otro régimen aplicable.

**Independencia frente a P28 y P32.** La vigencia nominal puede abarcar el acto y la aprobación ser posterior; un acto planificado puede seguir sin aprobación previa. **Partición examinada.** Una relación de precedencia entre dos sucesos; no se añade una valoración global de legalidad.

Fundamento profesional: N01 art. 21 y op.exp.5; N03B arts. 41–42; ADJ1 §§2.3 y 2.5. Localizadores y enlaces en la [bibliografía](BIBLIOGRAFIA_DE_PRESION_OP_CYB_001_v0.3.md). La fuente no enumera este átomo; la adjudicación es propia.

### P31 · Separación de los titulares de dos funciones

Identidad estable: `PAR-CYB-PRINCIPALES-DISTINTOS-001`. Versión 0.1.

| Elemento | Contrato |
| --- | --- |
| Sujeto | Dos funciones concretas de una actuación para las que se exige separación |
| Proposición | Los titulares acreditados de ambas funciones corresponden a principales institucionales distintos. |
| Valor 1 | Identidades canónicas distintas acreditadas por la referencia institucional. |
| Valor 0 | Ambas funciones se atribuyen al mismo principal, aunque utilice cuentas diferentes. |
| Indeterminación U | Se conocen cuentas o nombres, pero no puede resolverse la identidad canónica de los titulares. |
| Observación y perfil | La exigencia de separación se activa antes según categoría, medida o política aplicable. Se usa un par de funciones y titulares; otras incompatibilidades o independencia organizativa necesitan controles propios. Sin exigencia, el perfil es NO_APLICABLE, no Tri.1. |

**Conocimiento y consecuencia.** Dos cuentas no equivalen necesariamente a dos personas o autoridades independientes. Funciones → titulares → identidad canónica; el permiso de cada titular se examina por separado. Si se omite ese enlace: Una misma persona puede autorizar y ejecutar usando alias, aparentando una separación inexistente. El exceso también tiene un límite: No se impone doble control a todos los cambios ni se afirma independencia organizativa sólo por tener titulares distintos.

**Independencia frente a P26.** Dos titulares distintos pueden carecer de competencia; un titular competente puede asumir ambas funciones con cuentas diferentes. **Partición examinada.** Una desigualdad entre dos identidades canónicas. La independencia institucional más amplia sigue siendo compuesta.

Fundamento profesional: N01 anexo II op.acc.3, categoría MEDIA/ALTA; N09, gestión de usuarios. Localizadores y enlaces en la [bibliografía](BIBLIOGRAFIA_DE_PRESION_OP_CYB_001_v0.3.md). La fuente no enumera este átomo; la adjudicación es propia.

### P32 · Pertenencia de la actuación a un plan previo

Identidad estable: `PAR-CYB-ACTO-PREVISTO-001`. Versión 0.1.

| Elemento | Contrato |
| --- | --- |
| Sujeto | Una actuación y la versión del plan fijada antes de ejecutarla |
| Proposición | El acto individual figura entre las actuaciones previstas por esa versión del plan. |
| Valor 1 | Pertenencia expresa al plan previo y a su ámbito. |
| Valor 0 | Plan previo completo que excluye el acto. |
| Indeterminación U | Plan incompleto, versión posterior presentada como previa o correspondencia indeterminada. |
| Observación y perfil | PR-PLAN/1: lista finita de actuaciones individualizadas; la existencia previa y procedencia del plan son admisión. La finalidad justificativa, razón del cambio y régimen de urgencia se conservan en el contexto. Fuera de un régimen que requiera contrastar un plan, el perfil no se activa. |

**Conocimiento y consecuencia.** Planificar una actuación, autorizarla y ejecutarla son hechos diferentes. Acto → plan previo → razón y dependencias; permiso y resultado técnico permanecen independientes. Si se omite ese enlace: Puede ocultarse un cambio ajeno al plan, omitiendo sus dependencias, ventana o efectos sobre un servicio regulado. El exceso también tiene un límite: Una actuación no planificada no es necesariamente ilícita: puede existir autorización urgente válida y debe explicarse su régimen.

**Independencia frente a P30 y P02.** Una actuación prevista puede no estar autorizada; una actuación urgente autorizada previamente puede no figurar en el plan ordinario. **Partición examinada.** Una pertenencia a un conjunto de actuaciones previamente fijado; no mide calidad del plan ni suficiencia de la planificación.

Fundamento profesional: N01 op.exp.5; B01 §§3.3.1–3.3.3; ADJ1 §2.3. Localizadores y enlaces en la [bibliografía](BIBLIOGRAFIA_DE_PRESION_OP_CYB_001_v0.3.md). La fuente no enumera este átomo; la adjudicación es propia.

## 3. Candidatos resueltos sin identidad nueva

| Candidato | Resolución | Justificación |
| --- | --- | --- |
| XA01 · Resultado de autenticación | Uso de P07 | Resultado de una comprobación con criterio y perfil propios; no se cuenta una identidad nueva por cambiar el criterio. |
| XA02 · Firma o sello criptográficamente válido | Admisión; P07 si su resultado es objeto del consejo | Verificación, confianza en emisor y competencia son diferentes. No se declara ejecutada criptografía en esta campaña. |
| XA03 · Huella de prueba coincidente | C02 | Fija bytes frente a una referencia confiable; no prueba identidad ni permiso. |
| XA04 · Delegación completa válida | C11 y composición de P26–P30 | Conjunto finito de aristas con raíces, alcance y restricciones; no es una proposición indivisible. |
| XA05 · Actuación legalmente autorizada | C11/C16 | Resultado compuesto y contextual; no se crea un booleano que oculte facultad, alcance, tiempo y excepciones. |
| XA06 · Datos anónimos | C15; contraste especializado | No es una propiedad deducible de suprimir nombres, cifrar o recibir un informe favorable. |
| XA07 · Tratamiento conforme al RGPD | C15/C16 | Conjunto de obligaciones y valoraciones jurídicas; no se reduce a una variable binaria. |
| XA08 · Consentimiento siempre obtenido | No universal | El consentimiento no es la única base; en salud deben justificarse la base del artículo 6 y la condición pertinente del artículo 9. |
| XA09 · DLP sin alertas | P07 por criterio y C06 | Conserva sólo el alcance y sensibilidad de esa comprobación. |
| XA10 · Todo el tráfico protegido | C05/C06 | Cobertura y propiedades por flujo, dirección y destino, incluidas salidas y rutas de elusión. |
| XA11 · Motivo del cambio suficiente | Contexto y juicio experto | La razón declarada puede ser falsa o insuficiente; pertenencia a plan y permiso no la acreditan. |
| XA12 · Independencia organizativa total | C11/C16 | P31 sólo distingue identidades de dos titulares; relaciones jerárquicas, conflictos e independencia de auditoría requieren más contexto. |
| XA13 · Sello cualificado siempre requerido | No universal | Se consulta la medida y perfil aplicables. No se traslada mp.info.4 nivel ALTO a todos los actos. |
| XA14 · Producto certificado, sistema conforme | Desestimado | La evaluación del componente no sustituye integración, configuración, alcance ni conformidad del sistema. |
| XA15 · Nuevo parámetro por cada agente o sesión | Uso de identidad existente | Distintas instancias conservan estados propios; no multiplican definiciones. |
| XA16 · Parámetro adicional para completar una célula | Desestimado | 32 no determina geometría, partición ni tamaño. No hay relleno ni células menores de SV(9,3). |

P07 no se utiliza como comodín para ocultar conocimiento: el resultado de una comprobación de autenticación puede reutilizar esa definición, mientras que la relación real entre permiso y acto conserva su propia semántica. Un resultado favorable de una prueba de alcance y la pertenencia efectiva al alcance no son intercambiables sin acreditar el observador. La validez de un permiso completo reúne varias relaciones y restricciones; permanece como composición.

La antigua resolución R24 («permiso para intervenir» como control) continúa siendo correcta para la conclusión global, pero resultaba incompleta al no desarrollar sus relaciones individuales. R03–R05 conservan la distinción entre firma, integridad y procedencia; no excluyen una prueba por demostrar falta de permiso del ejecutor. La nueva resolución se superpone por sucesión explícita a esos antecedentes.

## 4. Contratos de cobertura y gobierno

| Control | Denominación | Contrato actual |
| --- | --- | --- |
| C01 | Identidad y aplicabilidad | Identificar activo, componente, vulnerabilidad, actualización, episodio y horizonte. Resolver por separado las condiciones del aviso aplicable: plataforma, arquitectura, versión, precursor y configuración. Si falta una condición decisiva, la aplicabilidad queda sin resolver. Una exclusión exige evidencia de que la regla no corresponde al caso. |
| C02 | Admisión de evidencia | Distinguir procedencia, integridad, autenticidad, legalidad de adquisición y permiso para observar de la legitimidad del acto observado. Una prueba admisible de una actuación no autorizada conserva el resultado técnico y permite registrar el incumplimiento. Si la adquisición no es admisible, conservar el registro de no admisión y tramitar la custodia competente, sin fabricar una salida del dominio. Los originales quedan bajo acceso y retención justificados; el expediente compartido usa una vista mínima trazable. |
| C03 | Correspondencia e interpretación de resultados | Vincular cada resultado al intento y elemento originales. Conservar códigos y errores completos. Un éxito con errores exige analizar qué efectos se produjeron; no prueba éxito íntegro ni ausencia total de modificación. El fallo de instalación es un hecho distinto del fallo al observarla. |
| C04 | Integridad de obligaciones | Enumerar las obligaciones específicas y sus efectos exigidos. Cada obligación se asigna a una de las ocho clases y a estados de cumplimiento individualizados. Una lista vacía exige evidencia de que no existen acciones adicionales. Ninguna obligación pertinente queda sustituida por un texto genérico de suficiencia. |
| C05 | Cobertura de sujetos y dependencias | Conservar la cobertura finita anterior y añadir principales humanos y de servicio, permisos, delegaciones, vías de administración, destinos de datos, repositorios de pruebas y flujos de salida pertinentes. Cada frontera externa conserva responsable, evidencia, contrato y alcance. Un servicio detrás de una pasarela no acredita que todo su tráfico saliente o sus integraciones pasen por ella. |
| C06 | Validez de la comprobación | Mantener criterio previo y sensibilidad propia. P07 puede registrar cada comprobación criptográfica o de autenticación cualificada, sin convertir su éxito en competencia, atribución personal cierta o autorización completa. El estado real del acto y la validez de su permiso exigen relaciones adicionales. Ausencia de alerta DLP no acredita anonimización ni ausencia de exfiltración. |
| C07 | Vigencia y orden de los hechos | Conservar cambio y retorno; añadir tiempos de acto, emisión, registro, sellado, recepción y efecto jurídico/institucional. Tratar intervalos de incertidumbre y fuentes de tiempo. Una revocación es evidencia del caso bajo regla fija, no aprendizaje de conocimiento. Reevaluar sólo las dependencias y el horizonte afectados. |
| C08 | Impactos sobre servicios y datos | Conservar funciones, datos y consecuencias; añadir confidencialidad de registros y telemetría, atribución falsa a una persona, acceso no autorizado y perjuicio a derechos. Separar posibilidad de daño, daño constatado y atribución causal. La conservación de trazabilidad no justifica difusión indiscriminada de identidades o datos de salud. |
| C09 | Comparación de alternativas | Describir completar, aplazar con medidas, sustituir, aislar o recuperar cuando sean pertinentes. Comparar el efecto corrector, los perjuicios y los requisitos de cada opción. Una medida compensatoria o una aceptación de riesgo no se presenta como corrección realizada. |
| C10 | Viabilidad temporal | Declarar ventana, duración de actuación, validación y recuperación, con dependencias y márgenes justificados. Las estimaciones desconocidas se mantienen abiertas. Este análisis sólo se activa si el consejo contempla una actuación pendiente. |
| C11 | Autoridad concreta | Componer identidad de principal, autenticación y atribución con competencia del emisor, alcance, vigencia, revocación, emisión previa y separación de funciones cuando proceda. La actuación prevista se distingue de la autorizada. Examinar cada arista de delegación, sus restricciones y el principal efectivo; no aceptar autoatribución de facultades por la IA. La autoridad humana del proyecto admite conocimiento; la organización competente concede permisos materiales, y ambos actos permanecen distintos. |
| C12 | Proporcionalidad de coste y valor | Conservar coste total y valor protegido por servicio y horizonte, incluidos derechos y daños no monetizados. Las alternativas deben satisfacer primero las obligaciones aplicables. No se convierte el precio del equipo en límite del valor protegido ni se permite omitir un requisito obligatorio por resultar caro. La decisión de suspender, sustituir o rediseñar el servicio corresponde al responsable competente. |
| C13 | Dictamen explicado | Conservar explicación reconstruible y distinguir resultado técnico, legitimidad de actuación, insuficiencias y consejo al experto. La explicación identifica referencias mínimas a pruebas y permisos, con vistas por destinatario; el acceso a la identidad personal detallada tiene control propio. El informe documental no se denomina Frame sin arquitectura SV constituida. Un fallo técnico no produce una salida alternativa del dominio. |
| C14 | Control de versiones del conocimiento | Fijar las fuentes y reglas antes de cada evaluación. Adquirir novedades en una actividad separada y someter su admisión a decisión humana. Los cambios de catálogos externos pueden exigir revisión, pero no sustituyen automáticamente el conocimiento ni añaden valores a Tri. |
| C15 | Protección de datos en pruebas y explicaciones | Fijar finalidad, responsable y encargado cuando proceda, categorías de datos, base del tratamiento y condición aplicable a datos de salud, destinatarios, accesos, transferencias, retención y supresión o bloqueo que corresponda. Justificar cada dato necesario; mantener separada y protegida la tabla de reidentificación. No llamar anónima a una vista seudonimizada. El dominio documental usa testigos sintéticos y no incorpora datos reales. Un original o una huella pueden seguir permitiendo vinculación y requieren evaluación. |
| C16 | Aplicabilidad de obligaciones y perfiles | Determinar entidad, jurisdicción, actividad, función, categoría y dimensiones del sistema, fecha relevante y versión de la disposición. Declarar requisitos activados y exclusiones justificadas. Separar ley, guía, norma técnica, evidencia educativa y propuesta de fabricante. La IA aplica conocimiento admitido; un texto nuevo exige adquisición y admisión humana separadas. |

## 5. Condición de cierre de la revisión

Los doce hallazgos tienen tratamiento y los dieciséis candidatos adicionales tienen resolución. P25–P32 poseen testigos positivos, negativos o de indeterminación según su perfil, con fronteras de admisión separadas. Las propiedades compuestas de privacidad, autorización completa, cobertura y eficacia del control no se declaran satisfechas por tener un nombre en una tabla: conservan contratos, responsables y pruebas pendientes.

La adjudicación termina este incremento documental. Las consecuencias descritas son potenciales y condicionadas al error y a su contexto; no se declaran incidentes, daños clínicos ni probabilidades observadas. Las 32 definiciones no acreditan ejecución de un consejo SV ni conformidad de un entorno regulado.
