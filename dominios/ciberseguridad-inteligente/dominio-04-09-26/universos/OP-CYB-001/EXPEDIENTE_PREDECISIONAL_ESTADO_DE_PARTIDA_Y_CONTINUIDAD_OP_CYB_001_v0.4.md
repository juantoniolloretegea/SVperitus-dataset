# Expediente predecisional de estado de partida, antecedentes y continuidad de OP-CYB-001

**Versión 0.4 · 9 de septiembre de 2026.** Universo: evidencia y legitimidad de la corrección de una vulnerabilidad mediante actualización. Destinatario: experto responsable de integrar el consejo en su organización. Base documental: `d616c0350379af5dddb8971d018c4f1086de03a8`. Esta edición complementa los 32 parámetros de v0.3 y precisa su contexto obligatorio.

## 1. El punto de partida

La evaluación parte del **primer estado observado y verificable pertinente**, comparado con la configuración de referencia aprobada, y del historial cuya cobertura pueda acreditarse. No presupone una instalación limpia, una autoridad heredada o un pasado completo. Si se empieza a documentar un sistema ya existente, se registra esa incorporación y el límite del conocimiento histórico. La observación de hoy puede establecer el estado de hoy; no reconstruye por sí sola quién hizo cada cambio anterior.

El expediente distingue tres fechas: el momento desde el que interesa conocer la historia, el primer momento para el que existe evidencia suficiente y el instante de evaluación. Una carencia entre los dos primeros se declara por su efecto sobre cada conclusión. No se exige recuperar un pasado infinito; tampoco se oculta un antecedente decisivo porque quede fuera de una captura conveniente. La elección del límite debe justificarse antes del dictamen.

La referencia de configuración es una especificación aprobada. La captura es evidencia sobre una realidad observada y puede mostrar desviaciones respecto de ella. Esa separación se apoya en [H01: §2.1.1; §3.1, inventario, pp. 25–28; §§3.2–3.4](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-128.pdf). La delimitación concreta EP01–EP18 es una propuesta documental de este dominio, no una lista prescrita literalmente por esa publicación.

## 2. Inventario que debe acompañar al consejo

Se desarrolla la presión del Director sobre escenario, inventario, censo, contabilidad, credenciales, registros de autoridad y perímetros. «Contabilidad» se emplea aquí como conciliación de identidades, actuaciones y efectos, además del balance económico que ya exige C12. No se supone que cuentas, credenciales, sesiones y permisos sean objetos intercambiables.

| Elemento | Contenido que debe quedar explícito | Destino | Consecuencia de omisión |
| --- | --- | --- | --- |
| EP01 · Servicio, finalidad y pregunta | Servicio protegido, destinatario experto, episodio y pregunta concreta: suficiencia de la evidencia y legitimidad de una corrección por actualización. | C01/C08/C13 | Consejo correcto para otro servicio o finalidad. |
| EP02 · Estado de referencia y estado observado | Configuración aprobada; captura observada con fuente, instante, generación, método, diferencias y vigencia. No se confunden la referencia deseada y el estado efectivo. | C01/C06/C07; P06/P12/P13/P16 | Dar por instalado o seguro aquello que sólo figura en el diseño. |
| EP03 · Comienzo de la historia disponible | Primer antecedente verificable; cobertura anterior acreditada, parcial o desconocida; razón del límite. La captura inaugural del expediente no es la creación del sistema. | C02/C07/C17 | Fabricar un pasado seguro y atribuirle una responsabilidad inexistente. |
| EP04 · Inventario de activos y consumidores | Hardware, firmware, software, bibliotecas, imágenes, réplicas, procesos, memoria, cachés y dependencias pertinentes; responsable de cada elemento y método de descubrimiento. | C01/C05; P05/P06/P11/P20–P22 | Una instancia no reconocida continúa expuesta y consume un componente anterior. |
| EP05 · Censo de principales y cuentas | Personas, servicios y agentes; vínculo entre identidad institucional, cuentas y función. Una cuenta compartida o dos alias requieren resolver la atribución, sin equiparar cantidad e identidad. | C05/C11; P25/P31 | Consejo dirigido a un titular equivocado o falsa separación de funciones. |
| EP06 · Credenciales y sesiones en curso | Identificador protegido, emisor, titular, ámbito, emisión, caducidad, revocación, renovación pendiente, sesiones y conexiones derivadas. No se registran secretos. Renovación y retirada tienen efectos distintos sobre sesiones existentes según el mecanismo. | C05/C07/C11/C15; P25–P30 | La baja de una cuenta se toma por cierre de una sesión todavía operativa. |
| EP07 · Fuentes competentes de autoridad | Política institucional, nombramientos, registro de atribuciones, concesiones y revocaciones, contrato o designación competente. Identificar custodio, corte, forma de consulta y fundamento de la fuente; no aceptar como raíz un nombre suministrado por la llamada o por el agente. | C02/C11/C16; P26–P30 | El atacante aporta a la vez su identidad y la supuesta autoridad que debe comprobarla. |
| EP08 · Obligaciones y asignaciones pendientes | Obligación individual, origen, resultado exigido, titular asignado, acto de designación, alcance, vigencia, aceptación si se exige, plazo, estado y destinatario de la incertidumbre. Se conserva el deber conocido aunque su titular no esté acreditado. | C04/C11/C13/C17; P01/P04/P15/P24 | El relevo conserva los archivos y pierde la obligación de completar, verificar o recuperar. |
| EP09 · Contabilidad de cambios y efectos | Conciliar por identidad el estado inicial, altas, bajas, sustituciones, cancelaciones, intentos y efectos con el estado final. Separar activos, cuentas, credenciales, sesiones y obligaciones; una suma de cantidades no demuestra coincidencia de miembros. | C03/C05/C07/C17 | Una operación repetida se contabiliza dos veces o una sesión ajena sustituye a la legítima sin cambiar el total. |
| EP10 · Origen y custodia de los registros | Acto, sesión ejecutora, productor del registro, firmante o sellador, recolector, custodio y analista, con roles diferenciados. Identificar archivo y entrada originales, transformaciones, copias, acceso y retención. | C02/C07/C15/C17; P25 | La firma del recolector atribuye falsamente al recolector el cambio que sólo recibió. |
| EP11 · Orden temporal y antecedentes | Relaciones con tipo, objetos exactos, respaldo y alcance: precedencia, derivación, causa acreditada, corrección, sustitución y recepción. Conservar incertidumbre de relojes, ramas simultáneas y antecedentes múltiples. | C07/C17; P09/P14/P28–P30 | Ordenar por llegada produce una causalidad o una autorización previa ficticias. |
| EP12 · Perímetros lógicos y físicos | Mapear acceso ordinario, administración, consola, plano de control, gestión fuera de banda, dispositivos físicos, entradas, salidas e integraciones. Declarar fronteras externas con evidencia y responsable. | C05/C06/C08/C16 | La consola o una salida directa eluden la protección comprobada para el acceso ordinario. |
| EP13 · Estado de las medidas de protección | Función preventiva, de detección, de contención o de recuperación; mecanismo, trayecto protegido, configuración efectiva, dependencias, última prueba y comportamiento cuando falla. Activa/pasiva es descripción contextual y no un criterio de suficiencia. | C05/C06/C09; P07/P12/P16 | Se da por disponible una protección instalada pero sin cobertura, o una copia que nunca se ha restaurado. |
| EP14 · Supuestos de seguridad de consecuencias elevadas | Puntos cuya pérdida afecta a múltiples funciones: autoridad raíz, tiempo, claves, consola, repositorio de prueba, identidad compartida, alimentación o recuperación. Vincular fallo supuesto, propagación, servicio y personas afectadas, evidencia y alternativa. | C05/C08/C09/C12 | Una dependencia común invalida varias protecciones que parecían independientes. |
| EP15 · Dato protegido y destinatario | Clasificación, finalidad, base aplicable, datos mínimos, acceso al original, vista por destinatario, retención y supresión. En este expediente todos los casos son sintéticos. | C02/C15/C16 | La auditoría expone datos de salud o identidades y se convierte en nueva causa de daño. |
| EP16 · Regla y conocimiento admitidos | Versiones de currículo, reglas, fuentes, perfiles y contratos fijadas antes de evaluar. Los sucesos nuevos se interpretan con esa regla; una regla nueva necesita adquisición y admisión humana separadas. | C14/C16 | Una revisión automática cambia el significado de una conclusión ya emitida. |
| EP17 · Alternativas y balance de coste y valor | Coste total, interrupción, recuperación, servicio protegido, derechos, alternativas y límite de lo conocido. No se monetiza como cero un daño no estimado ni se elude una obligación aplicable mediante ahorro. | C08–C12 | Una protección barata del equipo impone un perjuicio mayor al servicio o a personas. |
| EP18 · Cierre del episodio y entrega | Conclusiones por alcance, obligaciones pendientes, destinatario responsable, cambios que obligan a revisar y vínculo con el próximo episodio. Cerrar el expediente no equivale a autorizar la ejecución ni a certificar el sistema. | C13/C17 | El siguiente consejo parte de una conclusión sin sus límites y tareas pendientes. |

El ENS exige, dentro de su ámbito, inventario actualizado e identificación del responsable de los elementos, y diferencia funciones institucionales. El contrato conserva esas atribuciones y su aplicabilidad; no deduce facultades de un nombre de usuario. Véanse [arts. 11–12 y anexo II, op.exp.1 del RD 311/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191).

## 3. Qué puede acreditar cada registro

Un registro del instalador puede acreditar el resultado que ese emisor comunica bajo su contrato. La relación entre el acto y la sesión necesita correlación propia. El proveedor de identidad acredita extremos de autenticación dentro de su alcance; la fuente institucional competente acredita funciones y facultades. El gestor del cambio puede conservar plan y aprobación. El repositorio de auditoría acredita la recepción y conservación que pueda demostrar. Ninguno de estos papeles se presume por figurar en el mismo archivo.

Cada evidencia debe identificar el objeto original y su entrada, emisor, instante de producción, instante del hecho si consta, momento de recepción, método, versión, integridad comprobada, alcance de autenticidad, custodio, transformación y vínculo con el caso. Debe poder reconocerse una copia o vista y su original. No se publica por defecto toda esa información al destinatario del consejo: C15 exige una vista suficiente y autorizada.

La distinción entre originador, retransmisor y recolector se contrasta con [H07: §4; §§6.2–6.3; §7.1; §8](https://www.rfc-editor.org/rfc/rfc5424.txt). La gestión de fuentes inseguras y tiempos discordantes se apoya en [H02: §§2.1–2.3; §4.1, funciones y responsabilidades; §5.1](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-92.pdf). Estas especificaciones no convierten los registros en testigos infalibles.

## 4. Continuidad de la evidencia, de las facultades y de los deberes

**Un asiento añadido transmite información y puede documentar actos con efectos propios; la mera referencia a un asiento anterior no transmite responsabilidad.** Cuando exista una designación, delegación o sustitución competente, deben conservarse su fundamento, obligación, titular, ámbito y momento de efecto. La recepción de pruebas puede originar deberes de custodia conforme al régimen aplicable. Ello no identifica al custodio como ejecutor del cambio anterior ni determina la responsabilidad jurídica por ese cambio.

Se mantienen separadas cuatro cuestiones: qué ocurrió; quién intervino según la evidencia; quién tenía facultad o deber; y qué consecuencias jurídicas corresponde atribuir. Las tres primeras aportan información a la cuarta, pero el registro y la IA no la resuelven por sí solos. El experto integra el consejo dentro de sus competencias; las atribuciones de otras personas y organizaciones tampoco se extinguen por entregarle el informe.

Una obligación pendiente conserva identidad y origen. Un relevo documenta quién queda designado para atenderla y desde cuándo; si el procedimiento exige aceptación, ésta debe corresponder a la misma obligación y titular. Si no la exige, no se añade esa condición por comodidad informática. Un acuse de recibo de archivos no sustituye una designación. Si falta el titular, se informa de la obligación y de la asignación no acreditada, sin fabricar un responsable ni declarar extinguida la obligación.

La separación de relaciones se contrasta con [H03: §§5.1–5.3; en particular 5.3.2–5.3.4](https://www.w3.org/TR/2013/REC-prov-dm-20130430/). Su terminología de responsabilidad es descriptiva y no constituye una resolución jurídica ni una autorización de autoatribución de facultades por un agente SV. La custodia se contrasta con [H06: §2.3; §3.1.2, pp. 3-3–3-4; §3.1.3](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-86.pdf).

| Relación documental | Objetos enlazados | Qué acredita y qué debe conservar |
| --- | --- | --- |
| REFIERE | Documento a antecedente | Sólo referencia recuperable; no acredita causa, autorización ni sucesión de titular. |
| DERIVA_DE | Nueva evidencia a evidencia utilizada | Método y actividad de transformación; conservar original y relación con la vista. |
| PRECEDE_A | Suceso a suceso | Orden acreditado y precisión; no atribuye causalidad. |
| CAUSA_ACREDITADA | Suceso a efecto | Fuente y criterio causal explícitos; la proximidad temporal no basta. |
| CORRIGE | Asiento nuevo a afirmación anterior | Identificar exactamente qué se rectifica, por qué, con qué evidencia y desde qué momento; no borrar la afirmación histórica. |
| RECIBE_CUSTODIA | Custodio a evidencia recibida | Objeto, estado, integridad, momento y deberes de custodia propios; no reasigna el acto investigado. |
| DESIGNA | Acto competente a obligación y titular | Función, alcance, efecto, régimen de aceptación y vigencia; no nace de copiar el identificador del titular anterior. |
| ACEPTA_ENCARGO | Titular a obligación designada | Sólo opera si el procedimiento lo exige; una recepción genérica de archivos no basta. |
| REVOCA_O_SUSTITUYE | Acto competente a facultad o designación | Identidad, alcance y tiempo de efecto. No implica retroactividad ni exoneración jurídica universales. |

Las relaciones de esta tabla son un vocabulario del contrato externo de Ciberseguridad. No se han añadido al alfabeto SV, a su gramática ni a la IR. Una relación puede contener varios campos sin constituir un parámetro atómico compuesto: su función aquí es contextualizar y enlazar evidencias y responsabilidades.

## 5. Qué significa conservar una sucesión por adición

Cada versión conserva referencias exactas a los antecedentes pertinentes. Una rectificación identifica la afirmación afectada y publica el nuevo fundamento; una revocación conserva su tiempo de efecto. El registro histórico no se reescribe para fingir que el juicio anterior no existió. Las vistas autorizadas pueden cambiar conforme a las reglas de acceso y conservación.

La propiedad de sólo adición debe especificarse respecto de un adversario y una infraestructura: quién puede escribir, administrar, borrar, restaurar o presentar otra rama; cómo se conserva un punto de comparación independiente; y qué pérdida o sustitución se detecta. Encadenar huellas, por sí solo, no impide sustituir toda la cadena presentada ni demostrar que un hecho nunca registrado ocurrió. Tampoco acredita la verdad del contenido firmado si el emisor o su clave estaban comprometidos. RFC 5848 distingue garantías sobre mensajes enviados; no demuestra completitud del mundo observado ni responsabilidad jurídica.

Se admiten varios antecedentes, por ejemplo instalación, autorización, recepción de evidencia y cambio de custodio. El orden de llegada al recolector no se impone como orden causal. Una referencia recíproca entre recursos no se rechaza como si fuera necesariamente un ciclo temporal: sólo se aplican las restricciones del tipo de relación. El perfil de testigos comprueba precedencia estricta y derivaciones entre versiones; no es un validador completo de PROV. La comprobación de orden se contrasta con H04.

Si falta un antecedente decisivo, se conserva la carencia y no se acredita la conclusión dependiente. Si el capturador falla técnicamente, se registra ejecución técnica inválida, fuera de Tri. Si existe evidencia admisible pero insuficiente para una proposición, puede corresponder U bajo su contrato. Estas situaciones no son intercambiables.

La conservación por adición no establece retención ilimitada de datos personales. La política debe conciliar original, vistas, acceso, conservación y supresión o limitación aplicables. Incluso una huella puede permitir vinculación. Una actuación de supresión autorizada y documentada no puede presentarse como si el original siguiera disponible. C15/C16 siguen gobernando esta materia.

## 6. Seguridad activa, pasiva y supuestos de consecuencias elevadas

Los términos «activa» y «pasiva» no bastan para determinar la cobertura: su uso varía entre protección, detección y recuperación. Este expediente exige describir la función y el efecto verificable de cada medida. Comprueba también su estado antes del cambio, durante la transición y después. Un mecanismo instalado puede estar desactivado, excluir tráfico saliente o depender de la misma identidad comprometida que otro control.

La presión pertinente para OP-CYB-001 incluye una consola que evita la pasarela, una sesión que sobrevive a la renovación de credenciales, un repositorio de pruebas administrado por quien se audita, una fuente de tiempo común defectuosa y una recuperación cuyo material existe pero cuya restauración no está acreditada. Se registran las consecuencias posibles y la evidencia que permitiría contrastarlas. No se asignan probabilidades, puntuaciones ni causalidad real sin fuente y regla propias.

Estos son contextos y dependencias del cambio concreto. Diseñar una arquitectura completa de confianza cero, ejecutar una investigación forense integral o decidir la comunicación de datos para otra finalidad conserva producto, autoridad y terminación propios. La revisión no abre esos universos.

## 7. Ejemplo sintético de relevo

Una instalación informa éxito y la imagen observada coincide con la referencia. Queda pendiente verificar una réplica y retirar una sesión administrativa previa. La unidad A entrega los registros a la unidad B. B acusa recibo de los archivos.

El expediente conserva el éxito comunicado, las comprobaciones efectuadas y las dos tareas pendientes. El recibo acredita lo que indique su propio contrato de custodia. No permite afirmar que B ejecutó la instalación, que asumió el deber de verificar la réplica o que el titular anterior quedó exonerado. Para el encargo operativo se necesita su fuente de designación competente y el régimen de efecto. La retirada de la cuenta tampoco acredita por sí misma que la sesión haya terminado.

Si luego se acredita una designación eficaz a B, se incorpora como nuevo suceso, con su ámbito y aceptación cuando sea necesaria. La versión siguiente conserva el antecedente, el cambio de atribución y las incertidumbres restantes. El consejo explica a su destinatario qué puede concluir y qué decisión sigue siendo suya.

## 8. Efecto sobre el inventario

Se conservan **32 definiciones paramétricas**. Se incorpora **C17**, control compuesto de estado inicial y continuidad, que coordina C01–C16 y las relaciones anteriores. Hay 18 elementos de contexto y nueve clases documentales de relación; ninguna de esas cantidades representa células, matrices SV o átomos nuevos.

«Responsabilidad heredada», «sistema inicialmente seguro», «inventario fiable» y «perímetro protegido» no se adjudican como átomos generales. Reúnen condiciones independientes o requieren un régimen institucional. La obligación de documentarlas no desaparece: queda en EP01–EP18, C17 y sus testigos. El manifiesto de v0.3 debe leerse con esta precisión; su cierre documental no acreditaba historia completa de un sistema real.

La decisión entre valorar con Lenguaje el primer universo o constituir un segundo sigue siendo del Director. Este expediente permite someter al contraste las relaciones que antes quedaban implícitas; no ejecuta un relevo de unidad.
