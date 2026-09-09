# Revisión adversarial de identidad, autoridad y protección de datos en OP-CYB-001

**Versión 0.3 · 9 de septiembre de 2026 · Watson, unidad de Ciberseguridad Inteligente.** Trabajo autorizado por el Director. Revisión interna documental; no se presenta como auditoría independiente, certificación normativa ni ensayo de una infraestructura.

## 1. Dictamen y alcance de la rectificación

**La pretensión de cobertura completa del corte de 24 parámetros no resiste las nuevas presiones. Sus 24 definiciones técnicas se conservan; se incorporan ocho distinciones atómicas de gobierno de la actuación, hasta 32 definiciones documentales.** Se revisan los controles de evidencia, autoridad y explicación y se añaden los de protección de datos y aplicabilidad normativa. La revisión no deshace una actualización ni autoriza una intervención: mejora el conocimiento con el que se debe fundamentar el consejo al experto.

El objeto antecedente es el catálogo v0.8 y su expediente v0.2 en `SVperitus-dataset`, rama `dominio-ciberseguridad-inteligente`, commit `ee10ebe7fa058dfd1158f9753952712b854f87cc`. El nuevo catálogo principal es [Excel v0.9](../../catalogo-profesional/CATALOGO_CURRICULAR_CIBERSEGURIDAD_v0.9.xlsx). El libro v0.8 permanece congelado. Esta sucesión rectifica la suficiencia de su cobertura de autoridad y datos; no modifica retrospectivamente sus definiciones, pruebas o huellas.

La operación continúa siendo OP-CYB-001: fundamentar un consejo sobre la evidencia de corrección de una vulnerabilidad por actualización en un activo, componente, episodio y horizonte identificados. Su ámbito comprende también la legitimidad de las actuaciones examinadas y la protección de sus pruebas. No se abre un universo distinto para apartar estas obligaciones ni se absorbe toda la investigación de incidentes, la gestión de identidades o el derecho sanitario.

## 2. Contraejemplo decisivo

Considérense dos expedientes sintéticos con los mismos hechos técnicos: instalación satisfactoria, reinicio requerido completado, imagen objetivo utilizada y comprobación correctora favorable. En el primero, el permiso comprende la actuación; en el segundo, comprende otro activo. Los valores técnicos permanecen iguales y el consejo debe distinguirlos: el segundo expediente no permite respaldar la legitimidad de ese acto con ese permiso.

El defecto previo no consistía en ignorar por completo la palabra «autoridad»: C11 ya la mencionaba. Consistía en considerar suficiente esa mención sin constituir las relaciones que la hacen contrastable. Competencia del emisor, alcance, vigencia, revocación y emisión previa pueden variar independientemente. Tampoco basta con excluir como inadmisible toda evidencia que relate una actuación no autorizada: así se perdería precisamente la prueba de la infracción.

La reparación separa tres juicios. Primero, si una prueba se obtuvo y conserva de forma admisible. Segundo, qué estado técnico o suceso demuestra. Tercero, qué facultad amparaba al actor para realizar ese acto. Una prueba auténtica puede acreditar un resultado técnico satisfactorio y una actuación no autorizada. El permiso del observador, el permiso del ejecutor y la admisión humana del conocimiento tienen sujetos y finalidades distintos.

## 3. Método y evidencia examinada

Se leyeron íntegramente los tres PDF facilitados: CCN-STIC 813, 30 páginas; Cloudflare sobre SaaS, 12 páginas; y la guía del CEPD, 26 páginas. En los enlaces se contrastaron los artículos y apartados identificados en la [bibliografía de esta revisión](BIBLIOGRAFIA_DE_PRESION_OP_CYB_001_v0.3.md). Las lecturas dirigidas no se presentan como lectura de todos los documentos enlazados por cada sitio. Las copias de terceros no se republican en este expediente; se conservan sus identidades, localizadores y límites de lectura.

La revisión sigue pregunta, observable, consecuencia de omisión y contraste de independencia antes de adjudicar un átomo. Dieciséis candidatos adicionales se resuelven sin crear nuevas identidades paramétricas. Las fuentes justifican necesidades profesionales; **la adjudicación de P25–P32 es trabajo propio**, no una lista de parámetros promulgada por el ENS o NIST. Los esperados de los ensayos se fijaron en un archivo separado antes de ejecutar el observador documental.

Se inspeccionaron `ir.rs` y `bindings.rs` del Lenguaje en el corte entregado. Su texto se cotejó con `main@66967a80a40f4e2781ef983bd725690db54c25c5` y el paquete técnico `ab61d9bb7a2002d3a4a389e292c2a9b0a850d264`. Se conserva el reparto de competencias de RETP-105. No se modificó el Lenguaje ni se ejecutó Rust en esta revisión; la herramienta Cargo no está disponible en la ruta de ejecución de este entorno.

## 4. Precisiones normativas que cambian el consejo

El ENS exige examinar su ámbito de aplicación y graduar medidas por categoría y dimensiones. La autorización formal, el control de acceso y la trazabilidad sustentan esta revisión. La separación de funciones de op.acc.3 se aplica a categorías MEDIA y ALTA; op.exp.5 regula gestión de cambios en esas categorías. El sellado cualificado de mp.info.4 corresponde al nivel ALTO de trazabilidad; no se impone por esa medida a todo reinicio. La actualización publicada de la consolidación consultada es de 6 de noviembre de 2024. La aplicación a un caso concreto exige su encuadre, incluida la prestación privada para el sector público cuando proceda. [N01](https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191)

El RGPD no impone anonimizar indiscriminadamente toda información necesaria para prestar asistencia. Exige justificar el tratamiento y proteger los datos. En salud deben examinarse la base del artículo 6 y la condición aplicable del artículo 9; el consentimiento no es la única posibilidad. Cifrado, seudonimización y anonimización no son equivalentes. [N02B](https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807), [N09](https://www.edpb.europa.eu/sme/be-compliant/secure-personal-data_es)

El sello de tiempo cualificado aporta las presunciones de su régimen sobre tiempo e integridad de los datos vinculados. No convierte en verdadera cualquier fecha narrada dentro de esos datos ni concede facultades al firmante. Se contrastaron los artículos 41–42 de eIDAS con su modificación de 2024. Por ello, el tiempo de emisión de un permiso se mantiene separado del de sellado de su documento. [N03B](https://www.boe.es/buscar/doc.php?id=DOUE-L-2014-81822), [N03C](https://www.boe.es/buscar/doc.php?id=DOUE-L-2024-80608)

La guía CCN recibida se titula **Ciberseguridad de espacios de datos**, abril de 2024. Su nombre de archivo conserva una denominación anterior que también persiste en el enlace oficial; no se atribuye el desajuste al Director. Su ámbito principal son los espacios centralizados. La referencia de 2024 al EHDS como propuesta es histórica: el Reglamento entró en vigor en marzo de 2025 y su aplicación se despliega por fases posteriores. No se proyectan automáticamente sobre septiembre de 2026 las obligaciones de esas fases. [ADJ1](https://www.ccn-cert.cni.es/es/seguridad-al-dia/novedades-ccn-cert/12941-actualizada-la-guia-ccn-stic-813-sobre-ciberseguridad-de-espacios-de-datos.html), [N04](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en)

## 5. Identidad, delegación y suplantación

Una llamada que afirma proceder del soporte no constituye evidencia suficiente del principal ni de sus facultades. Para un procedimiento real se debe recurrir al mecanismo de identificación y confirmación previamente admitido por la organización, con referencia obtenida de su directorio confiable y no de los datos que aporte el propio solicitante. Esta es una exigencia del contrato del caso, no un nuevo método de autenticación creado por Watson.

La cuenta declarada, la autenticación obtenida, la sesión, el principal institucional y la persona que controló físicamente la credencial se conservan como objetos diferentes. Una credencial sustraída puede superar una comprobación y seguir existiendo incertidumbre sobre la persona actuante. El consejo no convierte esa incertidumbre en imputación. NIST SP 800-63-4 aporta un marco para identidad humana y declara límites respecto de máquina a máquina, IoT y API; no se traslada íntegramente a los agentes por analogía. [N07](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-4.pdf)

Para servicios y agentes se mantiene una identidad propia y una cadena de facultades limitada. El principal representado y el actor efectivo permanecen distintos. RFC 8693 permite expresar esa distinción, pero no demuestra que una delegación concreta sea legítima; además, su término técnico *impersonation* no designa siempre fraude. El contrato de delegación de este expediente es una propuesta del dominio: raíz competente, aristas identificadas, alcance por arista, restricciones, horizonte y motivo de terminación. No se declara implementado por citar el protocolo. [N10](https://www.rfc-editor.org/rfc/rfc8693.txt)

La IA sigue siendo consejera vinculada al experto. No se atribuye personalidad ni responsabilidad jurídica a la IA en este diseño; las competencias y responsabilidades humanas e institucionales conservan su sede. El Director admite conocimiento del dominio; la autoridad competente del entorno concede permisos materiales. El consejo no sustituye ninguno de esos actos. Una revocación observada bajo una regla ya admitida es evidencia nueva del caso, no aprendizaje autónomo de conocimiento.

## 6. Protección de las pruebas y consecuencias de omitir conocimiento

La trazabilidad exige reconstrucción suficiente para el destinatario competente. El original que deba conservarse permanece bajo custodia, finalidad, acceso y plazo justificados. La explicación ordinaria usa una vista mínima enlazada con él. La eventual tabla que permita reidentificar a un técnico permanece separada y protegida. Esa vista sigue siendo seudonimizada si la persona es identificable; no se denomina anónima por haber retirado su nombre.

Esta separación tiene consecuencias: una explicación que copie una historia clínica completa para acreditar un reinicio puede introducir una exposición ajena al propósito del consejo; una explicación que borre toda posibilidad de atribución puede impedir la investigación competente. El diseño debe satisfacer ambos requisitos mediante vistas, permisos y custodia distintos. La historia documental del SV no justifica una retención indefinida de datos personales, y una huella también puede permitir vinculación. Son requisitos de C15, con aplicación jurídica concreta a cargo del responsable competente. [N09](https://www.edpb.europa.eu/sme/be-compliant/secure-personal-data_es)

La protección de un dispositivo se valora respecto del servicio, personas, datos y derechos de los que depende. Su precio no agota ese valor. La proporcionalidad compara alternativas admisibles y consecuencias de actuar u omitir; no autoriza a descartar una obligación aplicable porque cumplirla resulte caro. Ante inviabilidad, corresponde al responsable decidir entre rediseñar, sustituir, limitar o suspender el servicio, con fundamento suficiente.

## 7. Lo que aporta la documentación de Cloudflare

La arquitectura SASE aporta una presión útil de cobertura: un túnel que publica un servicio no garantiza por sí mismo que las conexiones iniciadas por ese servidor atraviesen la misma inspección. También deben distinguirse revisión por API de datos almacenados, inspección del tránsito y tratamiento posterior. La configuración del control, el tráfico que observa y el resultado de su comprobación son evidencias diferentes. [N05](https://developers.cloudflare.com/reference-architecture/architectures/sase/)

El documento comercial de SaaS se utiliza como pista para aplicaciones no inventariadas, integraciones y exposición de datos; no como prueba de eficacia ni conformidad. La ausencia de alertas de prevención de pérdida de datos —DLP— no demuestra anonimización ni ausencia general de exposición. Una inspección o un registro alojados en otro servicio introducen destinos de datos que también requieren evaluación. No se elige ni contrata una plataforma. [ADJ2](BIBLIOGRAFIA_DE_PRESION_OP_CYB_001_v0.3.md#adj2--cloudflare)

## 8. Hallazgos y reparación

| Hallazgo | Clase | Insuficiencia | Tratamiento |
| --- | --- | --- | --- |
| HP01 · Insuficiencia del cierre de 24 parámetros | Material | C11 y QCY-07-D3 mencionaban autoridad, pero no separaban hechos que pueden variar con el mismo estado técnico. | P25–P32 y control de composición de autoridad. |
| HP02 · Admisión de evidencia y legitimidad del acto | Material | La autorización para observar o custodiar no se confunde con el permiso del ejecutor observado. | C02 revisado: conservar el hecho técnico y el defecto de autorización sin excluir la prueba por ese defecto. |
| HP03 · Identidad, autenticación y atribución | Material | Una cuenta, un canal cifrado y un resultado de autenticación tienen alcances probatorios distintos. | P07 por criterio de autenticación; P25; identidad canónica y límites de atribución expresos. |
| HP04 · Delegación entre humano, servicio y agente | Material | Un agente necesita identidad propia y una delegación limitada; no hereda todas las facultades del usuario. | Cadena finita de permisos por arista, principal actuante y principal por cuya cuenta actúa. |
| HP05 · Tiempo y prueba del orden | Material | Hora del hecho, del registro y del sellado no son sinónimos. | P28–P30; incertidumbre temporal, fuente de reloj y alcance de la comprobación. |
| HP06 · Privacidad de las propias pruebas | Material | El registro de seguridad puede contener datos personales y datos de salud; la trazabilidad no legitima cualquier copia o retención. | C15: original bajo custodia competente; vistas mínimas por destinatario; retención y acceso justificados. |
| HP07 · Anonimización indebidamente inferida | Material | Seudonimizar o cifrar no acredita anonimización; quitar el nombre puede dejar una persona singularizable. | No introducir un átomo datos anónimos. Exigir evaluación de reidentificación, finalidad y contexto de publicación. |
| HP08 · Cobertura real de SASE y SaaS | Material | Un control configurado sólo puede acreditar el tráfico, datos y vías que observa. | C05/C06: dirección del flujo y recorrido real; separación CASB por API, inspección en tránsito y procesamiento posterior. |
| HP09 · Aplicabilidad normativa y edición | Material | Se distinguían referencias, pero faltaba el caso regulado explícito para el universo. | C16: jurisdicción, sujeto, servicio, categoría/dimensión, función, fecha y edición; motivar obligación o exclusión. |
| HP10 · Identidad del documento CCN recibido | Bibliográfico | El nombre del archivo conserva una denominación antigua, también presente en el enlace oficial. | Título real: Ciberseguridad de espacios de datos, CCN-STIC 813, abril de 2024; 30 páginas. |
| HP11 · Precisión aparente de la estimación | Metodológico | 29/38/59 eran sumas de hipótesis editoriales, no límites demostrados del dominio. | 59 productos candidatos explícitos y reglas de agrupación para cada escenario; presupuestos y reutilización separados. |
| HP12 · Autoridad preservada frente a autoridad ejecutada | Límite de capacidad | LIG/0.1 conserva referencias exactas; su contrato excluye autenticar, conceder permisos y producir Tri. | Requisitos por operación, sin afirmar un defecto del núcleo por una capacidad expresamente excluida. |


El [acta de ampliación atómica](AMPLIACION_ATOMICA_Y_COBERTURA_OP_CYB_001_v0.3.md) contiene los ocho contratos, consecuencias, argumentos de independencia y candidatos no añadidos. La reparación de HP01–HP09 es documental y verificable en esas definiciones y controles; no acredita que una infraestructura real los haga cumplir.

## 9. Resultados ejecutados y comprobaciones pendientes

Se ejecutaron **46 casos sintéticos**, con cero discordancias respecto de sus esperados, y once modificaciones deliberadamente incorrectas del observador, todas detectadas. Se comprobaron diez pares de expedientes con los mismos estados técnicos y una diferencia de gobierno o tratamiento de datos. Su reducción a estados técnicos pierde esa diferencia. Es una pérdida demostrada en la reducción documental definida por esta revisión; no se presenta como una pérdida probada de toda la IR ni de LIG/0.1.

Los casos cubren relaciones, intervalos exactos y con incertidumbre, historia incompleta, alias de identidad, alcance, permisos posteriores, plan ordinario y urgencia, tipos erróneos, no admisión y no aplicabilidad. Incluyen números que superan la precisión binaria de doble precisión. El auxiliar conserva enteros decimales exactos y no realiza una conversión intermedia a coma flotante.

No se ejecutaron autenticaciones reales, validaciones criptográficas de documentos o sellos, ataques de suplantación, pruebas SASE, consultas a datos sanitarios, ni transducción productiva SV. La revisión de código del Lenguaje es estática. Los once mutantes miden sensibilidad frente a errores definidos; no son una tasa de detección del mundo real. La revisión sigue siendo interna y no sustituye revisión externa por pares.

## 10. Sucesión y decisión siguiente

El corte queda cerrado para las presiones examinadas: 32 definiciones documentales, 16 controles y 16 candidatos de esta revisión resueltos sin nuevos átomos. Las ocho clases técnicas de acción anteriores permanecen; los hechos de identidad, tiempo, permiso y plan se aplican a cada actuación pertinente. No se declara una frontera metafísica inmune a nuevas fuentes o contraejemplos. Si aparece uno, se registra una sucesión explícita, como se ha hecho aquí.

El dictamen de capacidad es **suficiencia operacional SV no acreditada**, con necesidades representacionales y ejecutivas individualizadas. La [estimación y propuesta de contraste](ESTIMACION_Y_CONTRASTE_CON_LENGUAJE_v0.3.md) explica por qué el primer universo ampliado ya proporciona testigos para trabajar con el Lenguaje. La decisión de pasar ahora o constituir antes otro universo sigue siendo del Director. No se abre un segundo universo ni se efectúa un relevo operativo automático.
