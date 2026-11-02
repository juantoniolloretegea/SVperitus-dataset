# Supervisión y auditoría de sistemas: expedientes, herramientas y asistencia subordinada

2 de noviembre de 2026 · Revisión documental 1.0.

Este capítulo define los requisitos de supervisión y auditoría del Agente Especializado en Ciberseguridad Inteligente. La habilitación efectiva se declara para cada instalación mediante su cobertura recibida, configuración y límites. Esta especificación no acredita por sí misma supervisión permanente, prevención activa ni recepción de todas las capacidades descritas.

## Autoridad y ámbito

El operador es la persona autorizada que utiliza el Agente Especializado en Ciberseguridad Inteligente. El **Perfil defensor (PD)** identifica la función del modelo de inteligencia artificial (IA), subordinada al operador y al gobierno determinista del SV. No es una cuenta administrativa ni sustituye al agente completo. La observación y la conservación necesarias deben continuar aunque el modelo no esté conectado o el panel esté cerrado; su continuidad se comprueba en la recepción.

Se distinguen el ámbito propio de operación y el ámbito externo objeto de intervención. El primero comprende recursos expresamente asignados a la instalación; el segundo exige identificar el titular, los recursos, las operaciones y la autorización del trabajo. Un dominio de conocimiento, un dominio administrativo y una red son objetos diferentes. El conocimiento del agente no concede permisos sobre una infraestructura. Se conserva la [definición común de alcance y acceso](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/main/agentes/ALCANCE-Y-ACCESO.md).

La supervisión transversal puede proteger recursos de Inmunología y otros dominios instalados bajo el SV. No concede acceso recíproco a expedientes, documentos, credenciales ni conversaciones. El modelo sólo recibe el contenido específicamente autorizado para su actuación. Una función administrativa, una lectura de seguridad y una intervención conservan permisos distintos.

## Expediente y trazabilidad

Toda actuación se vincula a un expediente estable, con ámbito interno o externo y finalidad de supervisión, auditoría preventiva o respuesta a incidentes. Su registro identifica quién autorizó, quién ejecutó, motivo, titular y límites técnicos, vigencia, condiciones de interrupción, herramientas y versiones, fuentes admitidas, datos tratados y destino de las evidencias. La extensión de alcance se registra antes de su uso; no se deduce de que una dirección sea alcanzable.

Se conservan por separado autorización, ejecución, observación y resultado. Cada evidencia identifica recurso, fuente, instante del suceso y de adquisición, integridad y relación con el original. Para los procesos se distingue su identificador de su instancia concreta de creación. Las pérdidas, duplicados, conflictos de atribución y periodos sin observación permanecen visibles.

En un sistema externo se comprueba qué observación existe y desde cuándo. La instalación actual de un programa no prueba su presencia durante un incidente anterior. Los registros aportados por terceros mantienen esa procedencia. La falta de registros no demuestra ausencia de actividad ni se transforma en un resultado satisfactorio.

## Adquisición común y contrato de evidencia

La adquisición integra las fuentes del sistema operativo, los procesos, las comunicaciones y los lectores de hardware cuya cobertura haya sido comprobada. Puede distribuirse entre procesos separados para reducir privilegios. Los instrumentos del examen y el panel consultan esa capacidad común mediante permisos delimitados por recurso, finalidad y periodo. Una frecuencia extraordinaria o una nueva fuente requiere configuración expresa y comprobación; no cambia silenciosamente otra operación.

Cada flujo conserva un contrato mínimo de evidencia:

- Recurso, ámbito, fuente, versión del recolector y configuración efectiva.
- Identidad del arranque y, para procesos, identificador y momento de creación.
- Tiempo del suceso, adquisición y recepción, zona horaria y calidad de sincronización; secuencia y tiempo monotónico dentro de una ejecución, cuando estén disponibles.
- Tipo de dato, unidad, frecuencia efectiva, muestreo, agregación, filtros, capacidad de las colas y pérdidas conocidas o desconocidas.
- Procedencia directa o aportada por terceros, transformaciones y relación con los originales conservados.
- Integridad, acceso, conservación, rotación, cobertura de copia y condiciones de recuperación.

Las huellas encadenadas permiten contrastar alteraciones respecto de una referencia conservada; no acreditan autenticidad si el mismo actor puede reescribir registros y referencias. La custodia independiente se recibe conforme al riesgo y alcance. La telemetría puede contener datos personales: se limita su adquisición, consulta y exportación a lo necesario.

Las métricas del sistema, las trazas y el consumo de los modelos pueden correlacionarse mediante identidades y relojes documentados. El consumo de una cuenta compartida, de todo el equipo o de otro trabajo no se atribuye a un candidato sin evidencia específica. Se conservan valores originales y unidades; la terna corresponde al juicio definido, no sustituye la medición.

## Auditoría preventiva y respuesta a incidentes

La auditoría preventiva comprueba inventario, protecciones, permisos, observación, retención y recuperación; registra las mejoras y verifica las autorizadas. No presupone que haya ocurrido un incidente. La respuesta a un incidente delimita su periodo y conserva los originales; distingue la adquisición nueva de las evidencias históricas. Una herramienta instalada hoy no demuestra que estuviera funcionando cuando ocurrieron los hechos.

Las conclusiones distinguen observaciones, declaraciones de terceros, inferencias justificadas y extremos no comprobables. La causa de una laguna puede estar identificada —fuente no configurada, permisos, muestreo, rotación, pérdida o interrupción— o permanecer sin resolver. La **dinámica forense** significa análisis de biblioteca admitida y evidencias con procedencia verificable; no añade un modo del modelo ni acredita por sí misma validez pericial.

La inspección directa, el descubrimiento activo, la instalación de un recolector y los cambios de configuración son operaciones distintas y deben estar comprendidos en la autorización. En el ámbito externo se puede combinar adquisición directa y documentación entregada, sin confundir sus procedencias.

## Biblioteca, conocimiento conocido e investigación

Una vulnerabilidad o incidente ya documentados y admitidos deben incorporarse a la edición pertinente de la biblioteca, con procedencia, versión, condiciones de aplicación y revisión. Su consulta posterior no exige presentarlos permanentemente como investigación nueva. La mera publicación de un aviso no equivale, sin embargo, a su admisión: deben resolverse identidad, integridad, pertinencia, permisos y relación con los Universos constituidos.

El **Procedimiento Pasivo (P1)** utiliza biblioteca y evidencias previamente admitidas, sin navegación; el transporte mediante interfaz de programación de aplicaciones (API) requiere autorización independiente. El **Procedimiento Activo (P2)** permite investigar sólo dentro del alcance autorizado y mantiene sus hallazgos separados hasta su admisión. El protocolo acelerado flexibiliza únicamente condiciones configurables previamente aprobadas, con motivo y vigencia registrados; conserva aislamiento, integridad, autorización y protección del núcleo. La definición completa se mantiene en [Biblioteca y procedimientos](https://github.com/juantoniolloretegea/SV-motor/blob/main/laboratorio/ensayo-ia-y-observabilidad/biblioteca-y-procedimientos.md).

Los catálogos de amenazas convencionales y de actuaciones adversas de inteligencia artificial (IA) son fuentes versionadas de conocimiento. No constituyen una lista exhaustiva ni una autorización automática para ejecutar técnicas descritas.

Delimitar las fuentes admitidas no elimina el conocimiento previo del modelo ni acredita que carezca de otro conocimiento. La recepción comprueba el material entregado, las fuentes utilizadas y el cumplimiento del procedimiento; no presume un aislamiento de sus conocimientos de entrenamiento.

## Herramientas y fronteras de ejecución

El inventario de instrumentos declara función, versión, licencia, procedencia comprobada, privilegios, configuración efectiva, recursos autorizados y cobertura recibida. Distingue programas presentes, utilizados, recibidos y pendientes. La selección se justifica por necesidades concretas de procesos, comunicaciones, aplicaciones web, autenticación o evidencias; no por acumular una distribución completa.

Las herramientas de terceros pueden observar o intervenir mediante contratos acotados. El gobierno del SV, las autorizaciones, la admisibilidad, la interpretación constituida y la parada independiente permanecen en su realización en Rust. La salida de una herramienta o de un modelo es una entrada no confiable: no modifica controles ni se ejecuta como una instrucción. Estar escrito en Rust no constituye por sí solo una garantía de seguridad.

Una máquina virtual delimita un entorno y facilita su recuperación; no acredita aislamiento frente a todas las técnicas ni observación del hardware físico. Las pruebas de red deben acreditar los cruces permitidos y prohibidos, los servicios expuestos y la retirada de los recursos propios. La protección desde el arranque mantiene [su especificación y recepción separadas](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/main/agentes/ciberseguridad-inteligente/PROTECCION-DESDE-EL-ARRANQUE.md).

## Rutas, evidencia y representación

Los Universos, las dependencias obligatorias y las rutas se reutilizan cuando están constituidos para la operación. Una ruta pendiente se identifica como pendiente; no recibe ficticiamente U. El vector contiene las valoraciones de cuestiones expresamente definidas y el polígono representa ese mismo estado con su identidad y orden, sin sustituir la evidencia.

Cada posición debe permitir consultar pregunta, regla, fuente, condición crítica, valor y comprobación que lo sostiene. La explicación del modelo, su pronunciamiento ternario y la comprobación independiente se distinguen. Una puntuación comercial, una alerta o una ausencia de alertas no se convierte automáticamente en 0, 1 o U. Se aplican [Parámetros, rutas y evidencia](https://documentos-sv.itvia.online/dominios/universos/parametros-rutas.html) y [Consecuencias de la omisión](https://github.com/juantoniolloretegea/SV-motor/blob/main/laboratorio/ensayo-ia-y-observabilidad/modelos-de-ia/estandar-comparativo-o-benchmark/CONSECUENCIAS-Y-FUENTES.md).

## Presentación y recepción

La página anfitriona debe ofrecer ámbito y expediente, salud de fuentes, procesos y comunicaciones autorizados, cronología, biblioteca, herramientas y células relacionadas. La presentación distingue funcionamiento, pérdida de observación, incidencia y capacidad pendiente. Permite consultar sin habilitar por ello configuración o actuación, y mantiene el acceso al trabajo ya existente.

La recepción exige hechos verificables: continuidad sin modelo, permisos efectivos, aislamiento entre consumidores, adquisición contrastada, pérdida detectada, conservación y recuperación, acciones selectivas, plazos y parada independiente. Una recepción parcial sólo acredita su alcance. El ensayo consume las fuentes comunes que necesita; la implantación institucional completa no se convierte por analogía en condición de todos sus parámetros.

La preparación jurídica identifica la normativa aplicable, responsables, finalidad, conservación y vías de notificación. La trazabilidad técnica facilita su examen, pero no acredita por sí sola conformidad normativa, certificación ni validez pericial.

## Marco de referencia y lecturas relacionadas

La aplicabilidad depende de la institución, sus servicios, los datos y la jurisdicción. Se consideran la [Directiva sobre seguridad de las redes y sistemas de información (NIS2)](https://www.boe.es/buscar/doc.php?id=DOUE-L-2022-81963), el [Reglamento General de Protección de Datos (RGPD)](https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807) y, donde corresponda, el [Esquema Nacional de Seguridad (ENS)](https://www.boe.es/eli/es/rd/2022/05/03/311/con). Deben verificarse la transposición, las autoridades competentes y los plazos aplicables antes de una actuación real; no se confunden las notificaciones de incidentes con las de violaciones de datos personales.

Como referencias técnicas, el [Instituto Nacional de Estándares y Tecnología de Estados Unidos (NIST), publicación 800-115](https://csrc.nist.gov/pubs/sp/800/115/final), orienta la planificación de evaluaciones técnicas; la [publicación 800-61, revisión 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), trata la respuesta a incidentes. Su consulta no certifica cumplimiento ni convierte recomendaciones en obligaciones idénticas para todas las instituciones.

La guía de uso se consulta en el espacio autorizado del Gestor. Este capítulo conserva los requisitos comunes; las definiciones de alcance, procedimientos, rutas y custodia permanecen en sus fuentes enlazadas.

© 2026 Juan Antonio Lloret Egea. Algunos derechos reservados. | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ – La Biblia de la IA™ | ISSN 2695-6411 | Licencia Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0).
