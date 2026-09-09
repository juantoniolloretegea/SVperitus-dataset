# Justificación científica de la selección paramétrica de OP-CYB-001

**Versión 0.4 · 9 de septiembre de 2026.** Matriz de argumentos, soporte bibliográfico, alternativas y límites. Las 32 definiciones se conservan con sus identidades y perfiles; esta edición refuerza su justificación y el enlace con el expediente predecisional.

## 1. Pregunta y método de selección

La pregunta profesional es qué información permite al experto valorar la evidencia y la legitimidad de una corrección por actualización en un ámbito declarado. No se pretende producir una medida universal de seguridad. La selección sigue la base educativa ya inventariada: España, mediante el Grado en Ingeniería de la Ciberseguridad de la URJC, con complementos internacionales motivados. El grado elegido es un vector universitario del proyecto, no un currículo nacional único ni una clasificación de superioridad internacional.

La formación en sistemas permite distinguir archivo, proceso, imagen cargada, configuración y estado derivado. La formación en auditoría exige procedencia y límites del observador; la de gestión del riesgo relaciona errores con servicios y consecuencias. Estas funciones se localizan en R025, R032 y R035. Las actividades de presión EDP01–EDP06 de v0.3 son propuestas didácticas del proyecto, no transcripciones de programas docentes.

Se aplican cinco decisiones documentales: identificar una pregunta indivisible en el perfil; precisar sujeto y horizonte; demostrar una distinción frente a una alternativa; enlazar su omisión y su uso excesivo con consecuencias; y declarar fuente, observables y condiciones de no conclusión. Un número conveniente de posiciones o la frecuencia de una palabra en una guía no son criterios de selección.

Las fuentes cumplen funciones diferentes: el currículo justifica conocimiento de base; una publicación profesional explica la necesidad; una especificación define un resultado o mecanismo; una norma aplicable determina obligaciones; un estudio empírico acota un problema observado en su población. Ninguna fuente externa prescribe esta lista exacta de 32 parámetros. La selección y la adjudicación documental son resultados del proyecto, abiertos a refutación. Esta revisión no se presenta como revisión sistemática exhaustiva de literatura ni como validación comparada de utilidad operacional.

## 2. Argumentación por parámetro

Los contratos de 0, 1, U, admisión y no aplicabilidad permanecen en el catálogo principal y sus actas. Las siguientes fichas no redefinen esos valores. Las consecuencias son mecanismos de error propuestos para el contraste; no tasas medidas de daño.

### P01. Necesidad de reiniciar el sistema

**Proposición:** Al finalizar la instalación, su regla o resultado individual aplicable exigía reiniciar íntegramente el sistema.

**Conocimiento y elección:** La finalización del instalador y la activación del cambio son momentos diferentes. La instalación exige reiniciar tanto antes como después de que el reinicio se complete.

**Alternativa examinada y unidad:** El carácter íntegro identifica el reinicio exigido; no reúne reinicio y cumplimiento.

**Consecuencia de omitirla:** Sin este enlace puede declararse corregida una instancia que todavía utiliza el estado anterior. **Consecuencia del uso excesivo:** La ausencia de evidencia del requisito no justifica ordenar un reinicio.

**Perfil y límite:** Perfil WUA conservado: resultado individual orcSucceeded y RebootRequired. Perfil documental adicional: instrucción específica del producto, aplicabilidad acreditada y requisito histórico explícito; nunca se deduce del consejo general de NIST.

**Soporte localizado:** [T002: Remarks](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/nf-wuapi-iupdateinstallationresult-get_rebootrequired); [T004: Constants](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/ne-wuapi-operationresultcode); [T006: Parameters; Remarks](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/nf-wuapi-iinstallationresult-getupdateresult); [T001: §§2.2–2.3, pp. 4–7; §§3.1–3.5](https://doi.org/10.6028/NIST.SP.800-40r4).

### P02. Terminación satisfactoria comunicada de la instalación

**Proposición:** El emisor comunicó terminación satisfactoria sin calificación de errores.

**Conocimiento y elección:** Un resultado agregado puede ocultar el fallo de un elemento. Una instalación anterior puede mantener la imagen correcta aunque el intento actual falle.

**Alternativa examinada y unidad:** Los códigos se conservan como observables; no se crea un parámetro por cada código.

**Consecuencia de omitirla:** El experto podría aceptar una operación parcial como finalizada satisfactoriamente. **Consecuencia del uso excesivo:** El valor 0 no significa que no se modificase ningún componente.

**Perfil y límite:** WUA: orcSucceeded se distingue de SucceededWithErrors, Failed y Aborted. NotStarted e InProgress no pertenecen al perfil terminal.

**Soporte localizado:** [T004: Constants](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/ne-wuapi-operationresultcode); [T005: Properties](https://learn.microsoft.com/en-us/windows/win32/wua_sdk/iupdateinstallationresult-properties); [T006: Parameters; Remarks](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/nf-wuapi-iinstallationresult-getupdateresult).

### P03. Reinicio íntegro realizado

**Proposición:** Se completó un reinicio íntegro después de la instalación y antes o en el instante de evaluación.

**Conocimiento y elección:** El arranque híbrido puede conservar parte del estado del sistema. Con el mismo requisito, el reinicio puede haberse realizado o seguir pendiente.

**Alternativa examinada y unidad:** Fecha y clase de arranque identifican un evento; no constituyen dos decisiones independientes.

**Consecuencia de omitirla:** Equiparar un encendido híbrido a un reinicio íntegro puede conservar componentes anteriores. **Consecuencia del uso excesivo:** Repetir un reinicio ya acreditado puede interrumpir innecesariamente el servicio.

**Perfil y límite:** Registro de arranque que acredite identidad, orden y clase. El ejemplo de Fast Startup corresponde a Windows 10.

**Soporte localizado:** [T007: Summary; More information](https://learn.microsoft.com/en-us/troubleshoot/windows-client/setup-upgrade-and-drivers/updates-not-install-with-fast-startup); [T001: §§2.2–2.3, pp. 4–7; §§3.1–3.5](https://doi.org/10.6028/NIST.SP.800-40r4).

### P04. Necesidad de reiniciar un programa

**Proposición:** La instrucción aplicable exigía reiniciar el programa identificado para completar el cambio.

**Conocimiento y elección:** Un cambio puede requerir reiniciar un programa sin reiniciar el sistema. El sistema puede no requerir reinicio y el programa sí.

**Alternativa examinada y unidad:** Una obligación para un programa; la ejecución de dicha obligación se descompone.

**Consecuencia de omitirla:** La instalación podría cerrarse mientras continúa el programa anterior. **Consecuencia del uso excesivo:** No se reinician todos los programas por analogía con uno afectado.

**Perfil y límite:** Instrucción específica, programa e instalación individualizados; Restart Manager ilustra el mecanismo, no fija la obligación del caso.

**Soporte localizado:** [T009: Texto principal](https://learn.microsoft.com/en-us/windows/win32/rstmgr/about-restart-manager); [T001: §§2.2–2.3, pp. 4–7; §§3.1–3.5](https://doi.org/10.6028/NIST.SP.800-40r4).

### P05. Terminación de la generación anterior de un proceso

**Proposición:** La generación anterior del proceso terminó durante el intervalo pertinente.

**Conocimiento y elección:** Un identificador de proceso puede reutilizarse y terminar un padre no termina necesariamente sus hijos. El proceso anterior puede terminar sin que se cree su sustituto.

**Alternativa examinada y unidad:** Identidad de generación y evento de terminación; los hijos tienen otras identidades.

**Consecuencia de omitirla:** Puede persistir ejecución anterior aunque se haya detenido el proceso nominalmente principal. **Consecuencia del uso excesivo:** No se terminan otros procesos únicamente por compartir un nombre.

**Perfil y límite:** PID y tiempo exacto de creación, sistema y registro de terminación. No se usa el PID aislado.

**Soporte localizado:** [T014: Members](https://learn.microsoft.com/en-us/windows/win32/api/restartmanager/ns-restartmanager-rm_unique_process); [T016: How Processes are Terminated](https://learn.microsoft.com/en-us/windows/win32/procthread/terminating-a-process).

### P06. Identidad objetivo de la imagen utilizada

**Proposición:** La identidad de la imagen utilizada coincide con la identidad objetivo previamente admitida.

**Conocimiento y elección:** La imagen utilizada puede diferir de la almacenada; el programa residente de un dispositivo también tiene un ámbito propio. La imagen nueva puede estar almacenada mientras continúa utilizándose la anterior, o suceder lo contrario.

**Alternativa examinada y unidad:** Una imagen y un consumidor. Biblioteca, núcleo y firmware no se cuentan de nuevo si conservan exactamente esta proposición.

**Consecuencia de omitirla:** Una versión correcta en disco puede ocultar ejecución anterior en memoria o en un dispositivo. **Consecuencia del uso excesivo:** Una identidad diferente no demuestra por sí sola vulnerabilidad.

**Perfil y límite:** Win32: MODULEINFO no acredita identidad de contenido. Para núcleo o firmware se exige un método específico que identifique la imagen utilizada; la lectura de un archivo descargado no lo sustituye. La ampliación semántica de perfil se declara en v0.2.

**Soporte localizado:** [T008: Factors that affect searching](https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order); [T012: Parameters; Remarks](https://learn.microsoft.com/en-us/windows/win32/api/psapi/nf-psapi-getmoduleinformation); [T013: Members](https://learn.microsoft.com/en-us/windows/win32/api/psapi/ns-psapi-moduleinfo); [B02: §§3–4](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-193.pdf).

### P07. Resultado favorable de una comprobación individual

**Proposición:** La comprobación individual produjo el resultado favorable definido antes de ejecutarla.

**Conocimiento y elección:** Una comprobación puede no detectar una corrección incompleta. Una identidad objetivo puede coexistir con fallo de una comprobación funcional independiente.

**Alternativa examinada y unidad:** Es un resultado de prueba, no el estado universal de seguridad. Dos criterios independientes requieren dos usos identificados; una prueba compuesta no se convierte en átomo.

**Consecuencia de omitirla:** Un informe sin hallazgos puede ocultar la incapacidad para observar el defecto residual. **Consecuencia del uso excesivo:** Un resultado desfavorable no autoriza una intervención automática.

**Perfil y límite:** Criterio y casos positivos/negativos anteriores al ensayo; umbral y alcance expresos. No sustituye los estados de P16–P24 ni permite introducir conocimiento nuevo durante el consejo.

**Soporte localizado:** [F018: §§3.4–3.6, 4.3, 6.5, 7.3–7.4](https://doi.org/10.6028/NIST.SP.800-115); [B08: §1, pp. 1147–1148; §§4–6 para el alcance del estudio](https://www.usenix.org/system/files/sec20-dai.pdf); [B09: §1, pp. 4521–4522; §7, evaluación; §8, discusión y límites](https://www.usenix.org/system/files/usenixsecurity25-sun-shiyu.pdf); [T001: §§2.2–2.3, pp. 4–7; §§3.1–3.5](https://doi.org/10.6028/NIST.SP.800-40r4).

### P08. Retirada satisfactoria comunicada de la actualización

**Proposición:** Se comunicó la retirada satisfactoria de la actualización dentro del intervalo observado.

**Conocimiento y elección:** La retirada es un acontecimiento histórico, incluso si después se reinstala. El archivo objetivo puede volver a estar presente tras una reinstalación sin borrar la retirada.

**Alternativa examinada y unidad:** Existencia de un acontecimiento; no incluye el estado final ni la causa.

**Consecuencia de omitirla:** Se podría reutilizar una comprobación anterior a la retirada. **Consecuencia del uso excesivo:** Retirar una actualización no demuestra que todo el sistema haya vuelto a una versión vulnerable.

**Perfil y límite:** Historia individual de actualización. La lista de eventos no acredita por sí misma cobertura completa.

**Soporte localizado:** [T010: Methods](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/nn-wuapi-iupdatehistoryentry); [T011: Constants](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/ne-wuapi-updateoperation); [T001: §§2.2–2.3, pp. 4–7; §§3.1–3.5](https://doi.org/10.6028/NIST.SP.800-40r4).

### P09. Cambio posterior de un componente binario

**Proposición:** La identidad binaria del componente cambió al menos una vez dentro del intervalo.

**Conocimiento y elección:** Dos extremos iguales pueden ocultar una modificación intermedia. La misma identidad final puede provenir de una historia estable o de cambio y retorno.

**Alternativa examinada y unidad:** La existencia de transición es única; cantidad, causa y actor se conservan como evidencia.

**Consecuencia de omitirla:** Una comprobación antigua podría atribuirse indebidamente al estado actual. **Consecuencia del uso excesivo:** Un cambio irrelevante para el criterio no obliga a repetir todas las pruebas.

**Perfil y límite:** Historia completa para negar cambios. El intervalo y el ámbito del componente se fijan previamente.

**Soporte localizado:** [T001: §§2.2–2.3, pp. 4–7; §§3.1–3.5](https://doi.org/10.6028/NIST.SP.800-40r4); [B01: §§3.2–3.4, pp. 30–44; apéndices E e I](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-128.pdf).

### P10. Restauración previa comunicada

**Proposición:** Se comunicó restauración satisfactoria desde un estado capturado antes de la instalación.

**Conocimiento y elección:** Una restauración puede reintroducir estados anteriores por un mecanismo distinto de la desinstalación. Restaurar una máquina virtual puede no generar un evento de desinstalación.

**Alternativa examinada y unidad:** Evento con procedencia temporal; no reúne restauración y vulnerabilidad.

**Consecuencia de omitirla:** El experto podría aceptar una corrección basándose en pruebas anteriores a la restauración. **Consecuencia del uso excesivo:** La antigüedad de una copia no demuestra que todos sus componentes sean vulnerables.

**Perfil y límite:** Registro de restauración con objeto, origen y resultado. No se ejecuta una recuperación.

**Soporte localizado:** [T001: §§2.2–2.3, pp. 4–7; §§3.1–3.5](https://doi.org/10.6028/NIST.SP.800-40r4); [B10: §3.2, pp. 15–19; §§3.4.1, 4.3](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf).

### P11. Creación de una nueva generación de proceso

**Proposición:** La generación se creó después de la instalación y no después del instante de evaluación.

**Conocimiento y elección:** Crear un proceso no acredita que haya terminado su inicialización. La generación anterior puede terminar con o sin creación posterior.

**Alternativa examinada y unidad:** PID y tiempo son identidad; no se añade la inicialización al mismo parámetro.

**Consecuencia de omitirla:** Podría aceptarse la mera terminación del proceso anterior sin comprobar su sustitución. **Consecuencia del uso excesivo:** No se crea otra instancia por ignorar una creación ya acreditada.

**Perfil y límite:** Registro de creación y orden temporal exacto. Una observación posterior al instante de evaluación no pertenece al caso.

**Soporte localizado:** [T014: Members](https://learn.microsoft.com/en-us/windows/win32/api/restartmanager/ns-restartmanager-rm_unique_process); [T015: Return value](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw).

### P12. Valor efectivo de configuración objetivo

**Proposición:** El valor efectivo de la clave coincide con el valor objetivo admitido.

**Conocimiento y elección:** Guardar una configuración no demuestra que el consumidor la haya incorporado. El valor persistente puede cambiar antes de que lo utilice el consumidor.

**Alternativa examinada y unidad:** Una clave escalar. Un objeto con varias propiedades exige separación por significado.

**Consecuencia de omitirla:** Puede persistir una condición insegura aunque el archivo de configuración parezca correcto. **Consecuencia del uso excesivo:** Una alternativa autorizada no se rechaza sólo por diferir de otro objetivo.

**Perfil y límite:** Método específico de lectura efectiva y equivalencia tipada; ausencia sólo es valor si el esquema lo define.

**Soporte localizado:** [T001: §§2.2–2.3, pp. 4–7; §§3.1–3.5](https://doi.org/10.6028/NIST.SP.800-40r4); [F018: §§3.4–3.6, 4.3, 6.5, 7.3–7.4](https://doi.org/10.6028/NIST.SP.800-115); [B01: §§3.2–3.4, pp. 30–44; apéndices E e I](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-128.pdf).

### P13. Identidad objetivo del artefacto almacenado

**Proposición:** La identidad del artefacto almacenado coincide con el objetivo admitido.

**Conocimiento y elección:** Almacenamiento, utilización y selección de próxima carga son estados distintos. El archivo puede ser nuevo y la imagen utilizada antigua.

**Alternativa examinada y unidad:** Un artefacto, no una colección. Su integridad no incorpora autenticidad ni corrección funcional.

**Consecuencia de omitirla:** Puede aceptarse un estado que volverá a cargar un artefacto anterior. **Consecuencia del uso excesivo:** La discrepancia de identidad no acredita por sí sola un defecto de seguridad.

**Perfil y límite:** Lectura consistente del objeto completo, incluido un objeto binario de firmware si existe un perfil admitido. No afirma durabilidad física frente a un fallo eléctrico.

**Soporte localizado:** [T001: §§2.2–2.3, pp. 4–7; §§3.1–3.5](https://doi.org/10.6028/NIST.SP.800-40r4); [T008: Factors that affect searching](https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order); [B02: §§3–4](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-193.pdf); [B03: §§3.2–3.15, 3.19, 3.21, 3.25; §4](https://www.rfc-editor.org/rfc/rfc9124.txt).

### P14. Cambio posterior de configuración

**Proposición:** El valor de la clave cambió después de la comprobación de referencia.

**Conocimiento y elección:** El cambio de configuración puede invalidar una prueba sin modificar el ejecutable. Puede cambiar una clave sin cambiar ningún binario.

**Alternativa examinada y unidad:** Un valor y un ámbito; efectivo y persistente llevan usos separados.

**Consecuencia de omitirla:** Puede conservarse una conclusión que ya no corresponde a la configuración evaluada. **Consecuencia del uso excesivo:** Invalidar pruebas independientes produce trabajo sin fundamento.

**Perfil y límite:** Historia de valores tipados; cambio y retorno cuenta como cambio.

**Soporte localizado:** [T001: §§2.2–2.3, pp. 4–7; §§3.1–3.5](https://doi.org/10.6028/NIST.SP.800-40r4); [B01: §§3.2–3.4, pp. 30–44; apéndices E e I](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-128.pdf).

### P15. Necesidad de otra acción de terminación

**Proposición:** La instrucción aplicable exige esa acción para completar la actualización.

**Conocimiento y elección:** La actualización puede exigir configuración, sustitución, invalidación o activación adicionales. Puede exigirse una configuración adicional sin reiniciar el sistema.

**Alternativa examinada y unidad:** Sólo registra obligación. Una acción con resultados independientes se descompone antes de evaluarla.

**Consecuencia de omitirla:** Puede confundirse recepción del paquete con terminación de todos los efectos exigidos. **Consecuencia del uso excesivo:** La lista de posibilidades no es una lista de acciones obligatorias para todos los casos.

**Perfil y límite:** Registro cerrado de clases de acción y criterios de cumplimiento en esta versión. Prohibido añadir una acción semánticamente nueva por texto libre durante el consejo.

**Soporte localizado:** [T001: §§2.2–2.3, pp. 4–7; §§3.1–3.5](https://doi.org/10.6028/NIST.SP.800-40r4); [B01: §§3.2–3.4, pp. 30–44; apéndices E e I](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-128.pdf).

### P16. Valor persistente de configuración objetivo

**Proposición:** El valor persistente de la clave coincide con el objetivo admitido.

**Conocimiento y elección:** Una configuración correcta en uso puede no conservarse para la próxima carga. El consumidor conserva un valor nuevo mientras el repositorio vuelve al antiguo.

**Alternativa examinada y unidad:** Un valor escalar persistente; la clave y su repositorio identifican el sujeto.

**Consecuencia de omitirla:** Una recarga posterior podría recuperar la configuración anterior. **Consecuencia del uso excesivo:** No se sobrescribe una configuración por confundir dos repositorios o ámbitos.

**Perfil y límite:** Lectura consistente del repositorio autoritativo, con tipo y objetivo fijados; no se infiere de la lectura efectiva.

**Soporte localizado:** [B01: §§3.2–3.4, pp. 30–44; apéndices E e I](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-128.pdf); [F018: §§3.4–3.6, 4.3, 6.5, 7.3–7.4](https://doi.org/10.6028/NIST.SP.800-115).

### P17. Inicialización del proceso completada

**Proposición:** La generación alcanzó el hito de inicialización definido para su utilización.

**Conocimiento y elección:** La creación puede preceder a fallos de carga e inicialización. CreateProcessW puede devolver éxito y la inicialización terminar o fallar después.

**Alternativa examinada y unidad:** Un hito unitario definido. Si reúne preparación de componentes independientes, se separan sus usos.

**Consecuencia de omitirla:** Una instancia creada pero no inicializada podría presentarse como sustituto disponible. **Consecuencia del uso excesivo:** No se confunde una inicialización lenta con un fallo definitivo sin evidencia.

**Perfil y límite:** Señal de inicialización propia del programa, identidad de generación e instante. El retorno de CreateProcessW no sirve como señal suficiente.

**Soporte localizado:** [T015: Return value](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw); [R025: II. Presentación; III. Resultados de aprendizaje; IV. Contenido](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285025&txtTitulacion=2285&txtCursoAcademico=2026-27).

### P18. Habilitación de un parche en ejecución

**Proposición:** El mecanismo de aplicación mantiene habilitado el parche identificado en el instante evaluado.

**Conocimiento y elección:** La habilitación y la transición de las tareas son estados distintos. El estado habilitado puede cambiar al invertir una transición mientras una tarea conserva todavía el mismo estado de parche de referencia.

**Alternativa examinada y unidad:** Un estado del mecanismo; la transición por tarea queda fuera de la proposición.

**Consecuencia de omitirla:** Podría confundirse habilitación con aplicación completa en todas las tareas. **Consecuencia del uso excesivo:** No se fuerza una transición por el mero hecho de encontrarla pendiente.

**Perfil y límite:** Perfil Linux 6.8: enabled del parche. Se preservan identidad, instante y dirección de la transición.

**Soporte localizado:** [B04: §3, Consistency model; §§5.2–5.5](https://www.kernel.org/doc/html/v6.8/livepatch/livepatch.html).

### P19. Estado objetivo de parche en una tarea

**Proposición:** La tarea se encuentra en el estado de parche de referencia previamente admitido, durante la transición identificada.

**Conocimiento y elección:** Las tareas pueden transitar en momentos diferentes. Con el mismo enabled, dos tareas pueden tener estados de parche distintos.

**Alternativa examinada y unidad:** Una tarea y una transición. La conjunción sobre todas las tareas es una composición.

**Consecuencia de omitirla:** Una tarea puede seguir utilizando funciones anteriores mientras otras ya han transitado. **Consecuencia del uso excesivo:** Se evita forzar o reiniciar tareas que ya alcanzaron el objetivo.

**Perfil y límite:** Linux 6.8: patch_state 0/1 se compara con una referencia fijada previamente; la dirección de transición se conserva, pero no redefine esa referencia. El valor -1 fuera de transición no significa sin parche ni equivale a Tri.U; ese perfil no está activo.

**Soporte localizado:** [B04: §3, Consistency model; §§5.2–5.5](https://www.kernel.org/doc/html/v6.8/livepatch/livepatch.html).

### P20. Referencia vigente a un recurso anterior

**Proposición:** El consumidor mantiene una referencia utilizable al recurso anterior identificado.

**Conocimiento y elección:** La terminación de un proceso no elimina todas las referencias conservadas por otros consumidores. El proceso principal puede terminar mientras otro consumidor conserva una referencia.

**Alternativa examinada y unidad:** Una relación consumidor–recurso. La existencia de referencia y el contenido del recurso son estados diferentes.

**Consecuencia de omitirla:** Puede persistir utilización del recurso anterior o ser insegura su retirada. **Consecuencia del uso excesivo:** No se retira un recurso todavía referenciado ni se confunde mera dirección numérica con referencia vigente.

**Perfil y límite:** Identidad de generación, titular, ámbito y posibilidad de uso; ausencia exige enumeración completa del ámbito del consumidor.

**Soporte localizado:** [T016: How Processes are Terminated](https://learn.microsoft.com/en-us/windows/win32/procthread/terminating-a-process); [B04: §3, Consistency model; §§5.2–5.5](https://www.kernel.org/doc/html/v6.8/livepatch/livepatch.html); [R025: II. Presentación; III. Resultados de aprendizaje; IV. Contenido](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285025&txtTitulacion=2285&txtCursoAcademico=2026-27).

### P21. Contenido objetivo de una entrada de caché

**Proposición:** El contenido utilizable de la entrada coincide con el objetivo definido para ese consumidor.

**Conocimiento y elección:** Un estado conservado en memoria puede diferir del que se volvería a cargar desde su origen. El artefacto de origen puede ser idéntico y la entrada conservada diferente.

**Alternativa examinada y unidad:** Una entrada con un contenido semánticamente indivisible. Configuración efectiva se remite a P12; código utilizado a P06, sin doble conteo.

**Consecuencia de omitirla:** El consumidor podría seguir tomando decisiones con estado anterior pese a la actualización del origen. **Consecuencia del uso excesivo:** No se vacía toda caché ni se confunde ausencia de entrada con contenido obsoleto.

**Perfil y límite:** Perfil de caché de datos derivados: clave, generación, consumidor y criterio de identidad. La correspondencia entre origen y entrada debe estar documentada antes de usarla.

**Soporte localizado:** [B11: Texto principal](https://learn.microsoft.com/en-us/windows/win32/fileio/file-caching); [B05: §§1–4](https://www.kernel.org/doc/html/v6.8/livepatch/system-state.html); [R025: II. Presentación; III. Resultados de aprendizaje; IV. Contenido](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285025&txtTitulacion=2285&txtCursoAcademico=2026-27).

### P22. Selección del objetivo para la próxima carga

**Proposición:** La selección resuelta en el instante de evaluación designa el artefacto objetivo.

**Conocimiento y elección:** El artefacto correcto puede estar presente sin ser el que selecciona el cargador. Dos configuraciones de búsqueda pueden seleccionar archivos distintos con los mismos archivos almacenados.

**Alternativa examinada y unidad:** Una relación de selección resuelta; no promete que ocurra una carga futura.

**Consecuencia de omitirla:** Una próxima carga podría volver al artefacto anterior aunque el objetivo esté disponible. **Consecuencia del uso excesivo:** No se elimina una copia legítima por confundir presencia y prioridad de selección.

**Perfil y límite:** Regla de resolución del cargador fijada y entradas completas; para bancos de firmware se exige su regla específica. No se extrapola la búsqueda de DLL a firmware.

**Soporte localizado:** [T008: Factors that affect searching](https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order); [B03: §§3.2–3.15, 3.19, 3.21, 3.25; §4](https://www.rfc-editor.org/rfc/rfc9124.txt).

### P23. Sincronización satisfactoria comunicada del archivo

**Proposición:** La operación de sincronización del archivo comunicó terminación satisfactoria.

**Conocimiento y elección:** La escritura visible y la sincronización comunicada tienen alcances diferentes. La lectura del archivo puede ser correcta antes y después de una sincronización fallida.

**Alternativa examinada y unidad:** Un resultado comunicado. Metadatos, datos y dispositivo requieren identificación del alcance, no una garantía agregada.

**Consecuencia de omitirla:** Una lectura correcta podría confundirse con acreditación de persistencia bajo el modelo de fallo aplicable. **Consecuencia del uso excesivo:** No se ordenan sincronizaciones repetidas sin necesidad ni se atribuye durabilidad física ilimitada.

**Perfil y límite:** Perfil FlushFileBuffers para un archivo y sistema admitidos. FlushViewOfFile no es evidencia equivalente; el modelo de almacenamiento y sus garantías permanecen expresos.

**Soporte localizado:** [B06: Return value; Remarks](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-flushfilebuffers); [B07: Remarks](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-flushviewoffile); [B11: Texto principal](https://learn.microsoft.com/en-us/windows/win32/fileio/file-caching).

### P24. Operación diferida de archivo pendiente

**Proposición:** La operación permanece pendiente en el mecanismo que debe ejecutarla.

**Conocimiento y elección:** Aceptar una operación diferida no demuestra su ejecución. La instalación puede comunicar éxito con o sin operación diferida pendiente.

**Alternativa examinada y unidad:** Una operación de un mecanismo, no todas las acciones pendientes del sistema.

**Consecuencia de omitirla:** El experto podría dar por aplicada una sustitución que sólo fue programada. **Consecuencia del uso excesivo:** La ausencia de pendiente tampoco demuestra éxito: la operación pudo cancelarse.

**Perfil y límite:** Perfil PendingFileRenameOperations: origen, destino, orden e instalación. No se modifica el registro ni se programa ninguna operación.

**Soporte localizado:** [B12: MOVEFILE_DELAY_UNTIL_REBOOT; MOVEFILE_WRITE_THROUGH; Remarks](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-movefileexw).

### P25. Vinculación de un acto con una sesión

**Proposición:** El acto identificado está vinculado a la sesión de referencia por la relación de atribución admitida.

**Conocimiento y elección:** Autenticar una sesión y atribuirle un acto son relaciones diferentes. Dos instalaciones satisfactorias y una misma sesión autenticada; sólo una conserva la relación de ejecución con esa sesión.

**Alternativa examinada y unidad:** La identidad compuesta identifica un acto; se adjudica una sola arista, no toda la cadena de responsabilidad.

**Consecuencia de omitirla:** Un cambio ejecutado por otra sesión puede atribuirse al técnico legítimo y ocultar la intervención ajena. **Consecuencia del uso excesivo:** Una atribución incompleta no permite acusar a una persona ni borrar el resultado técnico observado.

**Perfil y límite:** Identificadores de acto, sesión y emisor; referencia del registro de correlación y perfil de observación. El nombre de cuenta o la proximidad temporal no bastan. El resultado de autenticación se registra aparte como uso específico de P07; no demuestra quién controló físicamente una credencial robada.

**Soporte localizado:** [N01: Arts. 2–3, 11, 17, 21, 24; anexos I–II, op.acc.1/3/4, op.exp.4/5/8, mp.info.4](https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191); [N09: Riesgos; organización; usuarios; datos sensibles; seudonimización y anonimización; copia ADJ3, 26 páginas](https://www.edpb.europa.eu/sme/be-compliant/secure-personal-data_es).

### P26. Competencia del emisor de una autorización

**Proposición:** El emisor figura como titular de la facultad de conceder esa autorización en el registro institucional aplicable al instante de emisión.

**Conocimiento y elección:** La identidad de un firmante no determina las facultades que le atribuye una organización. Un emisor competente puede conceder permiso para otro activo; un emisor incompetente puede escribir un alcance aparentemente exacto.

**Alternativa examinada y unidad:** La facultad individual se fija antes de consultar; no se agregan todas las competencias de la persona.

**Consecuencia de omitirla:** Un documento firmado por un proveedor o por un agente sin facultad puede presentarse como autorización institucional. **Consecuencia del uso excesivo:** No se presume incompetencia por falta de acceso del observador al registro; se conserva U.

**Perfil y límite:** Anclaje de autoridad fijado por la organización competente; historial de atribuciones y facultad individual. La verificación de firma no crea competencia. La cadena de delegación se resuelve por aristas; su legitimidad conjunta no se oculta en este parámetro.

**Soporte localizado:** [N01: Arts. 2–3, 11, 17, 21, 24; anexos I–II, op.acc.1/3/4, op.exp.4/5/8, mp.info.4](https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191); [N06: Resumen y §2.1, pp. 6–7](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf); [N10: §1.1 y §2.1](https://www.rfc-editor.org/rfc/rfc8693.txt).

### P27. Pertenencia del acto al alcance de un permiso

**Proposición:** La tupla del acto pertenece al conjunto de actuaciones que declara el permiso de referencia.

**Conocimiento y elección:** Un permiso identifica aquello que permite; la posesión de una credencial no amplía ese alcance. Un permiso auténtico emitido por autoridad competente puede estar vigente y excluir el activo o destinatario del acto.

**Alternativa examinada y unidad:** Acción y recurso fijan el sujeto relacional de la pertenencia. Los incumplimientos de campos se explican; no se crean átomos por cada palabra de la tupla.

**Consecuencia de omitirla:** Se puede legitimar un reinicio en otro servicio, una exportación de registros no prevista o el uso de credenciales por otro agente. **Consecuencia del uso excesivo:** La exclusión de este permiso no demuestra que no exista otro permiso aplicable; la cobertura de autorizaciones se comprueba aparte.

**Perfil y límite:** Perfil documental PR-ALC/1: conjunto finito explícito de tuplas exactas. No admite comodines interpretados por el auxiliar. Las restricciones adicionales del permiso se conservan y evalúan separadamente; una política más rica requiere su perfil y no se aproxima por este conjunto.

**Soporte localizado:** [N01: Arts. 2–3, 11, 17, 21, 24; anexos I–II, op.acc.1/3/4, op.exp.4/5/8, mp.info.4](https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191); [N06: Resumen y §2.1, pp. 6–7](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf); [N10: §1.1 y §2.1](https://www.rfc-editor.org/rfc/rfc8693.txt).

### P28. Inclusión temporal del acto en la vigencia declarada

**Proposición:** Todo el intervalo posible del acto queda comprendido en el intervalo de vigencia declarado por ese permiso.

**Conocimiento y elección:** La fecha escrita en un documento y el tiempo acreditado de la actuación no son intercambiables. El intervalo puede estar incluido en la vigencia nominal aunque el permiso ya estuviera revocado o se hubiese emitido después con fecha retroactiva.

**Alternativa examinada y unidad:** La inclusión de un intervalo es una relación única. Sus extremos son observables del mismo objeto temporal, no dos permisos.

**Consecuencia de omitirla:** Un acto posterior a la caducidad puede aconsejarse como autorizado, o puede ignorarse que el permiso caducó durante la actuación. **Consecuencia del uso excesivo:** La superposición incierta no se transforma en infracción demostrada ni en permiso vigente.

**Perfil y límite:** Perfil PR-TIEMPO/1: intervalos cerrados, escala común y precisión declarada; enteros decimales exactos conservados como texto. No confundir hora del registro, del sellado, de observación y del acto. Límites abiertos o reglas de zona horaria requieren otro perfil explícito.

**Soporte localizado:** [N03B: Arts. 41.1–2 y 42.1; actualización en N03C](https://www.boe.es/buscar/doc.php?id=DOUE-L-2014-81822); [N03C: Art. 1, puntos 41–42](https://www.boe.es/buscar/doc.php?id=DOUE-L-2024-80608); [N06: Resumen y §2.1, pp. 6–7](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf).

### P29. Revocación que afecta a la actuación

**Proposición:** Existe una revocación efectiva de ese permiso no posterior al final del acto.

**Conocimiento y elección:** El intervalo nominal de un permiso puede seguir abierto después de su retirada. Un permiso no caducado puede estar revocado; un permiso caducado puede no haber sufrido revocación alguna.

**Alternativa examinada y unidad:** Existencia de un suceso de revocación pertinente, con cobertura del historial. No reúne caducidad y revocación.

**Consecuencia de omitirla:** Una sesión o agente puede seguir figurando como autorizado después de la retirada de su facultad. **Consecuencia del uso excesivo:** No se invalida retroactivamente un acto anterior por una revocación posterior, salvo regla explícita aplicable.

**Perfil y límite:** PR-TIEMPO/1; se distinguen emisión, publicación, recepción y efecto de la revocación. La regla jurídica o institucional determina el efecto. La revocación posterior al final no se aplica retroactivamente por el simple hecho de conocerla después. Una nueva concesión posee otra identidad.

**Soporte localizado:** [N01: Arts. 2–3, 11, 17, 21, 24; anexos I–II, op.acc.1/3/4, op.exp.4/5/8, mp.info.4](https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191); [N09: Riesgos; organización; usuarios; datos sensibles; seudonimización y anonimización; copia ADJ3, 26 páginas](https://www.edpb.europa.eu/sme/be-compliant/secure-personal-data_es); [N06: Resumen y §2.1, pp. 6–7](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf).

### P30. Precedencia de la emisión de una autorización

**Proposición:** La emisión efectiva de la autorización precedió al comienzo de la actuación.

**Conocimiento y elección:** Ratificar después y autorizar antes son sucesos distintos. La vigencia nominal puede abarcar el acto y la aprobación ser posterior; un acto planificado puede seguir sin aprobación previa.

**Alternativa examinada y unidad:** Una relación de precedencia entre dos sucesos; no se añade una valoración global de legalidad.

**Consecuencia de omitirla:** Una aprobación posterior puede encubrir que el experto no autorizó la actuación cuando todavía podía decidirla. **Consecuencia del uso excesivo:** Un acto urgente no se califica por automatismo: se examina si estaba amparado por una autorización permanente u otro régimen aplicable.

**Perfil y límite:** PR-TIEMPO/1; se compara tiempo de emisión acreditado con comienzo, no fecha redactada retrospectivamente. Este átomo sólo describe precedencia; el régimen de urgencia o autorización permanente es contexto y puede aportar otro permiso válido anterior.

**Soporte localizado:** [N01: Arts. 2–3, 11, 17, 21, 24; anexos I–II, op.acc.1/3/4, op.exp.4/5/8, mp.info.4](https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191); [N03B: Arts. 41.1–2 y 42.1; actualización en N03C](https://www.boe.es/buscar/doc.php?id=DOUE-L-2014-81822); [N03C: Art. 1, puntos 41–42](https://www.boe.es/buscar/doc.php?id=DOUE-L-2024-80608).

### P31. Separación de los titulares de dos funciones

**Proposición:** Los titulares acreditados de ambas funciones corresponden a principales institucionales distintos.

**Conocimiento y elección:** Dos cuentas no equivalen necesariamente a dos personas o autoridades independientes. Dos titulares distintos pueden carecer de competencia; un titular competente puede asumir ambas funciones con cuentas diferentes.

**Alternativa examinada y unidad:** Una desigualdad entre dos identidades canónicas. La independencia institucional más amplia sigue siendo compuesta.

**Consecuencia de omitirla:** Una misma persona puede autorizar y ejecutar usando alias, aparentando una separación inexistente. **Consecuencia del uso excesivo:** No se impone doble control a todos los cambios ni se afirma independencia organizativa sólo por tener titulares distintos.

**Perfil y límite:** La exigencia de separación se activa antes según categoría, medida o política aplicable. Se usa un par de funciones y titulares; otras incompatibilidades o independencia organizativa necesitan controles propios. Sin exigencia, el perfil es NO_APLICABLE, no Tri.1.

**Soporte localizado:** [N01: Arts. 2–3, 11, 17, 21, 24; anexos I–II, op.acc.1/3/4, op.exp.4/5/8, mp.info.4](https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191); [N09: Riesgos; organización; usuarios; datos sensibles; seudonimización y anonimización; copia ADJ3, 26 páginas](https://www.edpb.europa.eu/sme/be-compliant/secure-personal-data_es).

### P32. Pertenencia de la actuación a un plan previo

**Proposición:** El acto individual figura entre las actuaciones previstas por esa versión del plan.

**Conocimiento y elección:** Planificar una actuación, autorizarla y ejecutarla son hechos diferentes. Una actuación prevista puede no estar autorizada; una actuación urgente autorizada previamente puede no figurar en el plan ordinario.

**Alternativa examinada y unidad:** Una pertenencia a un conjunto de actuaciones previamente fijado; no mide calidad del plan ni suficiencia de la planificación.

**Consecuencia de omitirla:** Puede ocultarse un cambio ajeno al plan, omitiendo sus dependencias, ventana o efectos sobre un servicio regulado. **Consecuencia del uso excesivo:** Una actuación no planificada no es necesariamente ilícita: puede existir autorización urgente válida y debe explicarse su régimen.

**Perfil y límite:** PR-PLAN/1: lista finita de actuaciones individualizadas; la existencia previa y procedencia del plan son admisión. La finalidad justificativa, razón del cambio y régimen de urgencia se conservan en el contexto. Fuera de un régimen que requiera contrastar un plan, el perfil no se activa.

**Soporte localizado:** [N01: Arts. 2–3, 11, 17, 21, 24; anexos I–II, op.acc.1/3/4, op.exp.4/5/8, mp.info.4](https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191); [B01: §§3.2–3.4, pp. 30–44; apéndices E e I](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-128.pdf).

## 3. Necesidades que no se convierten en átomos nuevos

La revisión distingue dato, relación, condición de admisión, control compuesto y parámetro. Esa distinción exige conservar explícitamente la información; no permite relegarla a texto libre irrecuperable. La asignación de una obligación es una relación del contexto con titular, acto y vigencia. No equivale a una supuesta magnitud ternaria universal de responsabilidad jurídica. La legitimidad conjunta necesita además las condiciones de C11. La aceptación es condicional al régimen institucional y no se impone a toda designación.

| Candidata general no adoptada | Resolución concreta | Por qué no se añade un átomo |
| --- | --- | --- |
| Sistema inicialmente seguro | EP02/EP03 y parámetros específicos | Agrega propiedades de configuración, historia, amenaza y autoridad. |
| Responsabilidad heredada | DESIGNA, RECIBE_CUSTODIA, ACEPTA_ENCARGO; C11/C17 | Confunde evidencia, facultad, deber y consecuencia jurídica; no existe una transmisión única por referencia. |
| Inventario fiable | EP04–EP06/EP09; C05/C17 | Su suficiencia depende de alcance, método, identidad, tiempo y conciliación. |
| Perímetro protegido | EP12–EP14; C05/C06 | La protección cambia según trayecto, amenaza, mecanismo, generación y criterio. |
| Registro inmutable y verdadero | EP10/EP11; C02/C17 | Integridad, autenticidad, completitud, veracidad y retención son propiedades diferentes. |
| Todas las credenciales válidas | EP06; P25–P30; C05/C11 | Es una composición sobre un censo; cuentas, claves, permisos y sesiones no se sustituyen mutuamente. |

La decisión de conservar 32 definiciones responde a esta descomposición del contrato, no a una preferencia por el número. Los 32 casos nuevos prueban sólo partes documentales de ese contrato; el número de casos coincide accidentalmente con el número de definiciones. No constituyen una prueba de independencia completa de todos los parámetros ni de agotamiento de cualquier implementación futura.

## 4. Qué evidencia falta para una publicación científica

Existe justificación documental, comparación de significados y falsación de reducciones concretas. Falta contrastar capturadores reales, cobertura de inventarios, comportamiento ante fallos de infraestructura y eficacia del consejo en casos representativos. Los resultados de BScout (Java) y DisPatch (modificaciones de parches) se mantienen en sus propios alcances; no validan experimentalmente OP-CYB-001.

Un estudio posterior deberá declarar población de sistemas, perfiles incluidos y excluidos, procedimientos de captura, casos fallidos y no concluyentes, observador independiente, pérdidas medibles y costes del consejo. Las estimaciones de 29/38/59 universos y aproximadamente 290/550/1.060 definiciones siguen siendo escenarios de planificación no calibrados. No se convierten en resultados empíricos ni se recalculan por añadir campos de contexto.

## 5. Bibliografía utilizada y control de edición

Se conservan los identificadores de la biblioteca para permitir el cotejo con Excel. H01 es una nueva lectura de B01 con huella idéntica; no aumenta el número de obras. H02–H07 añaden seis obras técnicas. H08 sólo verifica el estado de borrador de una revisión. Las capturas identifican los bytes consultados; las URL pueden cambiar después. Las lecturas nuevas son dirigidas a los localizadores indicados. No se afirma haber leído íntegramente cada obra.

- **B01.** Johnson, A.; Dempsey, K.; Ross, R.; Gupta, S.; Bailey, D. (2011; actualización editorial de 10-10-2019). *[Guide for Security-Focused Configuration Management of Information Systems. NIST SP 800-128](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-128.pdf)*. Localizador: §§3.2–3.4, pp. 30–44; apéndices E e I. Configuración, efectos funcionales y de seguridad, autorización y cierre del cambio. La actualización de 2019 no introduce cambios técnicos.

- **B02.** Regenscheid, A. (2018, mayo). *[Platform Firmware Resiliency Guidelines. NIST SP 800-193](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-193.pdf)*. Localizador: §§3–4. Contraste de plataforma y firmware. No acredita un método universal de medición del firmware activo.

- **B03.** Moran, B.; Tschofenig, H.; Birkholz, H. (2022, enero). *[A Manifest Information Model for Firmware Updates in Internet of Things (IoT) Devices. RFC 9124](https://www.rfc-editor.org/rfc/rfc9124.txt)*. Localizador: §§3.2–3.15, 3.19, 3.21, 3.25; §4. Contraste informativo de identidad, autenticidad, precursor, selección y dependencias. No es una norma universal para todo activo IT.

- **B04.** The Linux Kernel development community (Linux 6.8.0). *[Livepatch](https://www.kernel.org/doc/html/v6.8/livepatch/livepatch.html)*. Localizador: §3, Consistency model; §§5.2–5.5. Habilitación y transición por tarea, con semántica explícita del estado -1 y límites del mecanismo.

- **B05.** The Linux Kernel development community (Linux 6.8.0). *[System State Changes](https://www.kernel.org/doc/html/v6.8/livepatch/system-state.html)*. Localizador: §§1–4. Compatibilidad entre parches y modificación de estado compartido; base para contrastar obligaciones adicionales.

- **B06.** Microsoft (Metadato ms.date=2018-12-05; captura de 09-09-2026). *[FlushFileBuffers function (fileapi.h)](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-flushfilebuffers)*. Localizador: Return value; Remarks. Resultado y alcance de una sincronización de archivo.

- **B07.** Microsoft (Metadato ms.date=2018-12-05; captura de 09-09-2026). *[FlushViewOfFile function (memoryapi.h)](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-flushviewoffile)*. Localizador: Remarks. Contraejemplo a equiparar escritura de páginas, metadatos y persistencia en el dispositivo.

- **B08.** Dai, J.; Zhang, Y.; Jiang, Z.; Zhou, Y.; Chen, J.; Xing, X.; Zhang, X.; Tan, X.; Yang, M.; Yang, Z. (2020). *[BScout: Direct Whole Patch Presence Test for Java Executables. 29th USENIX Security Symposium, pp. 1147–1164](https://www.usenix.org/system/files/sec20-dai.pdf)*. Localizador: §1, pp. 1147–1148; §§4–6 para el alcance del estudio. Estudio empírico sobre presencia íntegra de parches en ejecutables Java. Sus resultados no se transfieren a todas las plataformas ni validan este catálogo.

- **B09.** Sun, S.; Xing, Y.; Wang, X.; Wang, S.; Li, Q.; Sun, K. (2025). *[DisPatch: Unraveling Security Patches from Entangled Code Changes. 34th USENIX Security Symposium](https://www.usenix.org/system/files/usenixsecurity25-sun-shiyu.pdf)*. Localizador: §1, pp. 4521–4522; §7, evaluación; §8, discusión y límites. Estudio sobre dependencias de modificaciones de código. Compilar un fragmento separado no acredita que resuelva íntegramente la vulnerabilidad. La delimitación de un parche individual también requiere juicio experto.

- **B10.** Swanson, M.; Bowen, P.; Phillips, A.; Gallup, D.; Lynes, D. (2010; actualización de 11-11-2010). *[Contingency Planning Guide for Federal Information Systems. NIST SP 800-34 Rev. 1](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf)*. Localizador: §3.2, pp. 15–19; §§3.4.1, 4.3. Relación entre servicios, dependencias, impacto y recuperación. Un objetivo temporal no es un resultado medido.

- **B11.** Microsoft (Metadato ms.date=2018-05-31; captura de 09-09-2026). *[File Caching](https://learn.microsoft.com/en-us/windows/win32/fileio/file-caching)*. Localizador: Texto principal. Diferencia entre escrituras almacenadas en memoria y su sincronización; intercambio entre rendimiento y fiabilidad.

- **B12.** Microsoft (Metadato ms.date=2018-12-05; captura de 09-09-2026). *[MoveFileExW function (winbase.h)](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-movefileexw)*. Localizador: MOVEFILE_DELAY_UNTIL_REBOOT; MOVEFILE_WRITE_THROUGH; Remarks. Operaciones diferidas de archivo y límites de la confirmación de programación.

- **F018.** Scarfone, K.; Souppaya, M.; Cody, A.; Orebaugh, A. (2008, septiembre). *[Technical Guide to Information Security Testing and Assessment. NIST SP 800-115](https://doi.org/10.6028/NIST.SP.800-115)*. Localizador: §§3.4–3.6, 4.3, 6.5, 7.3–7.4. Alcance y límites de las pruebas, resultados falsos y tratamiento de evidencia.

- **H01.** Johnson, A.; Dempsey, K.; Ross, R.; Gupta, S.; Bailey, D. (2011; actualización de 10-10-2019). *[Guide for Security-Focused Configuration Management of Information Systems. NIST SP 800-128](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-128.pdf)*. Localizador: §2.1.1; §3.1, inventario, pp. 25–28; §§3.2–3.4. Mismo documento y mismos bytes que B01. Esta lectura amplía los localizadores hacia inventario, configuración de referencia y control de cambios. No se cuenta como nueva obra.

- **H02.** Kent, K.; Souppaya, M. (Septiembre de 2006). *[Guide to Computer Security Log Management. NIST SP 800-92](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-92.pdf)*. Localizador: §§2.1–2.3; §4.1, funciones y responsabilidades; §5.1. Diferencia fuentes y papeles en la gestión de registros. Advierte sobre registros de equipos comprometidos, relojes discordantes y cobertura desigual. Su antigüedad exige no adoptar sus tecnologías como selección actual.

- **H03.** Moreau, L.; Missier, P. (eds.); W3C Provenance Working Group (30-04-2013, W3C Recommendation). *[PROV-DM: The PROV Data Model](https://www.w3.org/TR/2013/REC-prov-dm-20130430/)*. Localizador: §§5.1–5.3; en particular 5.3.2–5.3.4. Distingue derivación, atribución, asociación y delegación. Es un modelo de procedencia; no adjudica consecuencias jurídicas. Su posibilidad descriptiva de autoasignación no se importa como autorización para la IA SV.

- **H04.** Cheney, J.; Missier, P.; Moreau, L. (eds.); De Nies, T. (30-04-2013, W3C Recommendation). *[Constraints of the PROV Data Model](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/)*. Localizador: §4, validación; comprobación de restricciones de orden; constraints 30, 36–38. Aporta contraste de orden parcial y límites de inferencia hacia antecedentes. El perfil de este expediente es propio y no constituye una implementación conforme de PROV.

- **H05.** Kelsey, J.; Callas, J.; Clemm, A. (Mayo de 2010). *[Signed Syslog Messages. RFC 5848](https://www.rfc-editor.org/rfc/rfc5848.txt)*. Localizador: §§7–8; especialmente 8.1, 8.3–8.8. Delimita autenticidad, repetición, pérdida, orden e integridad de mensajes enviados. Una clave comprometida permite firmar mensajes falsos. No se seleccionan aquí algoritmos, certificados ni una implementación.

- **H06.** Kent, K.; Chevalier, S.; Grance, T.; Dang, H. (Agosto de 2006). *[Guide to Integrating Forensic Techniques into Incident Response. NIST SP 800-86](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-86.pdf)*. Localizador: §2.3; §3.1.2, pp. 3-3–3-4; §3.1.3. Fundamenta custodia, adquisición, copias y documentación de actuaciones sobre la evidencia. La custodia no se identifica con la responsabilidad del suceso investigado. Es orientación técnica, no dictamen de admisibilidad judicial.

- **H07.** Gerhards, R. (Marzo de 2009). *[The Syslog Protocol. RFC 5424](https://www.rfc-editor.org/rfc/rfc5424.txt)*. Localizador: §4; §§6.2–6.3; §7.1; §8. Distingue originador, retransmisor y recolector; los campos y tiempos requieren interpretación. Un formato válido no acredita origen auténtico, cobertura ni veracidad.

- **H08.** NIST; Scarfone, K.; Souppaya, M. (11-10-2023; estado consultado 09-09-2026). *[Cybersecurity Log Management Planning Guide. SP 800-92 Rev. 1, Initial Public Draft](https://csrc.nist.gov/pubs/sp/800/92/r1/ipd)*. Localizador: Ficha institucional: estado editorial y fecha. Comprobación de edición. La página consultada presenta un borrador; no se lo cita como revisión final ni como sustitución consumada de H02. No se usa su articulado para seleccionar parámetros.

- **N01.** España. Consejo de Ministros (2022; consolidación consultada: 06-11-2024). *[Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad](https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191)*. Localizador: Arts. 2–3, 11, 17, 21, 24; anexos I–II, op.acc.1/3/4, op.exp.4/5/8, mp.info.4. Obligaciones diferenciadas por ámbito, categoría y dimensión; no impone sellado cualificado a cualquier acto.

- **N03B.** Parlamento Europeo y Consejo de la Unión Europea (2014; arts. 41–42 contrastados con modificación de 2024). *[Reglamento (UE) n.º 910/2014, identificación electrónica y servicios de confianza](https://www.boe.es/buscar/doc.php?id=DOUE-L-2014-81822)*. Localizador: Arts. 41.1–2 y 42.1; actualización en N03C. El sellado vincula datos y tiempo en su alcance; no acredita por sí mismo competencia ni verdad de todo lo narrado.

- **N03C.** Parlamento Europeo y Consejo de la Unión Europea (11-04-2024; publicación 30-04-2024). *[Reglamento (UE) 2024/1183, marco europeo de identidad digital](https://www.boe.es/buscar/doc.php?id=DOUE-L-2024-80608)*. Localizador: Art. 1, puntos 41–42. Suprime art. 41.3, añade art. 42.1 bis y sustituye art. 42.2; evita usar el régimen de desarrollo de 2014 como vigente.

- **N06.** Rose, S.; Borchert, O.; Mitchell, S.; Connelly, S. NIST (Agosto de 2020). *[Zero Trust Architecture. NIST SP 800-207](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf)*. Localizador: Resumen y §2.1, pp. 6–7. Separa autenticación y autorización y evita confiar por ubicación de red. La política dinámica del caso no autoriza aprendizaje automático del conocimiento SV.

- **N09.** Comité Europeo de Protección de Datos (Página y copia impresa consultadas 09-09-2026). *[Datos personales seguros. Guía de protección de datos para pequeñas empresas](https://www.edpb.europa.eu/sme/be-compliant/secure-personal-data_es)*. Localizador: Riesgos; organización; usuarios; datos sensibles; seudonimización y anonimización; copia ADJ3, 26 páginas. Ejemplos educativos sobre protección de datos; no sustituye al Reglamento ni certifica conformidad.

- **N10.** Jones, M.; Nadalin, A.; Campbell, B.; Bradley, J.; Mortimore, C. IETF (Enero de 2020). *[OAuth 2.0 Token Exchange. RFC 8693](https://www.rfc-editor.org/rfc/rfc8693.txt)*. Localizador: §1.1 y §2.1. El protocolo permite distinguir actor y sujeto. Su término impersonation también nombra un modo legítimo y no equivale siempre a suplantación fraudulenta.

- **R025.** Universidad Rey Juan Carlos (Curso 2026–2027). *[SISTEMAS OPERATIVOS. Guía docente del Grado en Ingeniería de la Ciberseguridad](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285025&txtTitulacion=2285&txtCursoAcademico=2026-27)*. Localizador: II. Presentación; III. Resultados de aprendizaje; IV. Contenido. Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

- **R032.** Universidad Rey Juan Carlos (Curso 2026–2027). *[AUDITORIA. Guía docente del Grado en Ingeniería de la Ciberseguridad](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285032&txtTitulacion=2285&txtCursoAcademico=2026-27)*. Localizador: II. Presentación; III. Resultados de aprendizaje; IV. Contenido. Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

- **R035.** Universidad Rey Juan Carlos (Curso 2026–2027). *[ANALISIS Y GESTION DEL RIESGO. Guía docente del Grado en Ingeniería de la Ciberseguridad](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285036&txtTitulacion=2285&txtCursoAcademico=2026-27)*. Localizador: II. Presentación; III. Resultados de aprendizaje; IV. Contenido. Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

- **T001.** Souppaya, M.; Scarfone, K. (2022, abril). *[Guide to Enterprise Patch Management Planning: Preventive Maintenance for Technology. NIST SP 800-40r4](https://doi.org/10.6028/NIST.SP.800-40r4)*. Localizador: §§2.2–2.3, pp. 4–7; §§3.1–3.5. Fundamento profesional del ciclo de actualización, de la verificación del efecto y del balance de recursos.

- **T002.** Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *[IUpdateInstallationResult::get_RebootRequired](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/nf-wuapi-iupdateinstallationresult-get_rebootrequired)*. Localizador: Remarks. Requisito individual de reinicio.

- **T004.** Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *[OperationResultCode](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/ne-wuapi-operationresultcode)*. Localizador: Constants. Semántica de los resultados de operación.

- **T005.** Microsoft (Metadato ms.date=2018-05-31; captura de 08–09-09-2026). *[IUpdateInstallationResult Properties](https://learn.microsoft.com/en-us/windows/win32/wua_sdk/iupdateinstallationresult-properties)*. Localizador: Properties. Separación de ResultCode, HResult y RebootRequired.

- **T006.** Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *[IInstallationResult::GetUpdateResult](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/nf-wuapi-iinstallationresult-getupdateresult)*. Localizador: Parameters; Remarks. Correspondencia con el índice original de la colección.

- **T007.** Microsoft (Metadato ms.date=2026-02-12; captura de 08–09-09-2026). *[Updates may not be installed with Fast Startup in Windows 10](https://learn.microsoft.com/en-us/troubleshoot/windows-client/setup-upgrade-and-drivers/updates-not-install-with-fast-startup)*. Localizador: Summary; More information. Diferencia entre inicio rápido y reinicio íntegro en ese perfil.

- **T008.** Microsoft (Metadato ms.date=2023-02-08; captura de 08–09-09-2026). *[Dynamic-link library search order](https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order)*. Localizador: Factors that affect searching. Selección de bibliotecas y efectos del contexto de carga.

- **T009.** Microsoft (Metadato ms.date=2018-05-31; captura de 08–09-09-2026). *[About Restart Manager](https://learn.microsoft.com/en-us/windows/win32/rstmgr/about-restart-manager)*. Localizador: Texto principal. Gestión de programas que usan archivos afectados.

- **T010.** Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *[IUpdateHistoryEntry interface](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/nn-wuapi-iupdatehistoryentry)*. Localizador: Methods. Datos de historia de actualización; no prueba automática de cobertura.

- **T011.** Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *[UpdateOperation](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/ne-wuapi-updateoperation)*. Localizador: Constants. Distinción entre instalación y desinstalación.

- **T012.** Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *[GetModuleInformation](https://learn.microsoft.com/en-us/windows/win32/api/psapi/nf-psapi-getmoduleinformation)*. Localizador: Parameters; Remarks. Información de módulo y permisos de observación.

- **T013.** Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *[MODULEINFO structure](https://learn.microsoft.com/en-us/windows/win32/api/psapi/ns-psapi-moduleinfo)*. Localizador: Members. Dirección, tamaño y punto de entrada; no identidad criptográfica.

- **T014.** Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *[RM_UNIQUE_PROCESS](https://learn.microsoft.com/en-us/windows/win32/api/restartmanager/ns-restartmanager-rm_unique_process)*. Localizador: Members. Identificación de proceso mediante PID y tiempo de creación.

- **T015.** Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *[CreateProcessW](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw)*. Localizador: Return value. Creación anterior a la terminación de la inicialización.

- **T016.** Microsoft (Metadato ms.date=2025-07-14; captura de 08–09-09-2026). *[Terminating a Process](https://learn.microsoft.com/en-us/windows/win32/procthread/terminating-a-process)*. Localizador: How Processes are Terminated. Procesos hijos y permanencia de objetos por referencias externas.

### Antecedentes de método

- [IMM-1: expediente de Inmunología](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/fe8adf76aa030ba5ff4997be5772b5de5e4452f3/dominios/inmunologia/marco-tecnico-de-universos-subdominios-y-modulos/01-op-imm-001-informacion-preinmunosupresion-adultos/Solicitud_de_valoracion_y_encaje_tecnico_de_OP-IMM-001_con_el_Lenguaje_SV_2026-09-03.md). Corte `fe8adf76aa030ba5ff4997be5772b5de5e4452f3`. Documento completo; segunda revisión dirigida a finalidad, responsabilidad, procedencia, límites y forma de valoración. Identidad y huella en el anexo.

- [IMM-2: expediente de Inmunología](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/fe8adf76aa030ba5ff4997be5772b5de5e4452f3/dominios/inmunologia/universos-clinicos/01-evaluacion-predecisional-riesgo-infeccioso-antes-inmunosupresion-adultos/Expediente_predecisional_de_informacion_clinica_pertinente_antes_de_iniciar_tratamiento_inmunosupresor_en_adultos_v1.1_2026-09-03.md). Corte `fe8adf76aa030ba5ff4997be5772b5de5e4452f3`. Documento completo; segunda revisión dirigida a finalidad, responsabilidad, procedencia, límites y forma de valoración. Identidad y huella en el anexo.

La primera solicitud de Inmunología examinaba un corte anterior del Lenguaje. Se toma su forma de exigir evidencia y separar responsabilidades; no se traslada su inventario de capacidades ni sus autorizaciones históricas a Ciberseguridad.
