# Catálogo atómico de OP-CYB-001

**Versión 0.2. 24 definiciones. 9 de septiembre de 2026.**

Las fichas constituyen el registro actual del universo. El estado se calcula sólo cuando el sujeto, la referencia, el método y la evidencia son admisibles. Falta de aplicabilidad, rechazo de evidencia y fallo técnico se conservan fuera del alfabeto 0/1/U. Cada uso incorpora su propio horizonte y sus consecuencias. La atribución de atomicidad procede del método de este proyecto, no de una declaración de los autores de las fuentes.

| Parámetro | Denominación | Versión |
| --- | --- | --- |
| P01 | Necesidad de reiniciar el sistema | 0.2 |
| P02 | Terminación satisfactoria comunicada de la instalación | 0.1 |
| P03 | Reinicio íntegro realizado | 0.1 |
| P04 | Necesidad de reiniciar un programa | 0.1 |
| P05 | Terminación de la generación anterior de un proceso | 0.1 |
| P06 | Identidad objetivo de la imagen utilizada | 0.2 |
| P07 | Resultado favorable de una comprobación individual | 0.2 |
| P08 | Retirada satisfactoria comunicada de la actualización | 0.1 |
| P09 | Cambio posterior de un componente binario | 0.1 |
| P10 | Restauración previa comunicada | 0.1 |
| P11 | Creación de una nueva generación de proceso | 0.1 |
| P12 | Valor efectivo de configuración objetivo | 0.1 |
| P13 | Identidad objetivo del artefacto almacenado | 0.2 |
| P14 | Cambio posterior de configuración | 0.1 |
| P15 | Necesidad de otra acción de terminación | 0.2 |
| P16 | Valor persistente de configuración objetivo | 0.1 |
| P17 | Inicialización del proceso completada | 0.1 |
| P18 | Habilitación de un parche en ejecución | 0.1 |
| P19 | Estado objetivo de parche en una tarea | 0.1 |
| P20 | Referencia vigente a un recurso anterior | 0.1 |
| P21 | Contenido objetivo de una entrada de caché | 0.1 |
| P22 | Selección del objetivo para la próxima carga | 0.1 |
| P23 | Sincronización satisfactoria comunicada del archivo | 0.1 |
| P24 | Operación diferida de archivo pendiente | 0.1 |


## P01. Necesidad de reiniciar el sistema

**Identidad:** `PAR-CYB-REINICIO-SISTEMA-REQUERIDO-001`, versión 0.2.

**Sujeto y proposición.** Un sistema y un episodio de instalación terminada. Al finalizar la instalación, su regla o resultado individual aplicable exigía reiniciar íntegramente el sistema.

| Estado | Condición |
| --- | --- |
| 1 | Exigencia explícita. |
| 0 | Ausencia de exigencia explícitamente acreditada. |
| U | Requisito desconocido o contradictorio. |


**Observación y límites.** Perfil WUA conservado: resultado individual orcSucceeded y RebootRequired. Perfil documental adicional: instrucción específica del producto, aplicabilidad acreditada y requisito histórico explícito; nunca se deduce del consejo general de NIST.

**Conocimiento y relación necesarios.** La finalización del instalador y la activación del cambio son momentos diferentes. El requisito histórico se contrasta con el reinicio posterior, P03.

**Consecuencia de omisión.** Sin este enlace puede declararse corregida una instancia que todavía utiliza el estado anterior. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** La ausencia de evidencia del requisito no justifica ordenar un reinicio.

**Variación independiente y retirada del parámetro.** La instalación exige reiniciar tanto antes como después de que el reinicio se complete. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P03.

**Prueba de partición.** El carácter íntegro identifica el reinicio exigido; no reúne reinicio y cumplimiento.

**Procedencia.** T002, T003, T004, T006; T001 §2.3.2. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P02. Terminación satisfactoria comunicada de la instalación

**Identidad:** `PAR-CYB-INSTALACION-EXITO-COMUNICADO-001`, versión 0.1.

**Sujeto y proposición.** Un intento individual de instalación. El emisor comunicó terminación satisfactoria sin calificación de errores.

| Estado | Condición |
| --- | --- |
| 1 | Estado terminal satisfactorio sin errores según el contrato del emisor. |
| 0 | Estado terminal de fallo, aborto o éxito con errores. |
| U | Resultado terminal ausente o contradictorio. |


**Observación y límites.** WUA: orcSucceeded se distingue de SucceededWithErrors, Failed y Aborted. NotStarted e InProgress no pertenecen al perfil terminal.

**Conocimiento y relación necesarios.** Un resultado agregado puede ocultar el fallo de un elemento. La correspondencia entre elemento, intento y resultado precede a la interpretación.

**Consecuencia de omisión.** El experto podría aceptar una operación parcial como finalizada satisfactoriamente. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** El valor 0 no significa que no se modificase ningún componente.

**Variación independiente y retirada del parámetro.** Una instalación anterior puede mantener la imagen correcta aunque el intento actual falle. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P06.

**Prueba de partición.** Los códigos se conservan como observables; no se crea un parámetro por cada código.

**Procedencia.** T004–T006. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P03. Reinicio íntegro realizado

**Identidad:** `PAR-CYB-REINICIO-SISTEMA-REALIZADO-001`, versión 0.1.

**Sujeto y proposición.** Un sistema durante el intervalo posterior a la instalación. Se completó un reinicio íntegro después de la instalación y antes o en el instante de evaluación.

| Estado | Condición |
| --- | --- |
| 1 | Evento completo acreditado dentro del intervalo. |
| 0 | Historia completa sin ese evento. |
| U | Historia parcial, orden temporal incierto o conflicto. |


**Observación y límites.** Registro de arranque que acredite identidad, orden y clase. El ejemplo de Fast Startup corresponde a Windows 10.

**Conocimiento y relación necesarios.** El arranque híbrido puede conservar parte del estado del sistema. El evento completo satisface una obligación de reinicio, si esta existe.

**Consecuencia de omisión.** Equiparar un encendido híbrido a un reinicio íntegro puede conservar componentes anteriores. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** Repetir un reinicio ya acreditado puede interrumpir innecesariamente el servicio.

**Variación independiente y retirada del parámetro.** Con el mismo requisito, el reinicio puede haberse realizado o seguir pendiente. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P01.

**Prueba de partición.** Fecha y clase de arranque identifican un evento; no constituyen dos decisiones independientes.

**Procedencia.** T001 §2.3.2; T007. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P04. Necesidad de reiniciar un programa

**Identidad:** `PAR-CYB-REINICIO-SOFTWARE-REQUERIDO-001`, versión 0.1.

**Sujeto y proposición.** Un programa y una instalación. La instrucción aplicable exigía reiniciar el programa identificado para completar el cambio.

| Estado | Condición |
| --- | --- |
| 1 | Requisito explícito. |
| 0 | Declaración explícita de que no se requiere ese reinicio. |
| U | Instrucción insuficiente o contradictoria. |


**Observación y límites.** Instrucción específica, programa e instalación individualizados; Restart Manager ilustra el mecanismo, no fija la obligación del caso.

**Conocimiento y relación necesarios.** Un cambio puede requerir reiniciar un programa sin reiniciar el sistema. El requisito se enlaza con terminación, creación, inicialización e imagen utilizada.

**Consecuencia de omisión.** La instalación podría cerrarse mientras continúa el programa anterior. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** No se reinician todos los programas por analogía con uno afectado.

**Variación independiente y retirada del parámetro.** El sistema puede no requerir reinicio y el programa sí. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P01.

**Prueba de partición.** Una obligación para un programa; la ejecución de dicha obligación se descompone.

**Procedencia.** T001 §2.3.2; T009. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P05. Terminación de la generación anterior de un proceso

**Identidad:** `PAR-CYB-GENERACION-PROCESO-TERMINADA-001`, versión 0.1.

**Sujeto y proposición.** Una generación identificada de proceso. La generación anterior del proceso terminó durante el intervalo pertinente.

| Estado | Condición |
| --- | --- |
| 1 | Terminación acreditada. |
| 0 | Permanencia acreditada de esa generación o historia completa sin terminación. |
| U | Vida o terminación no acreditadas. |


**Observación y límites.** PID y tiempo exacto de creación, sistema y registro de terminación. No se usa el PID aislado.

**Conocimiento y relación necesarios.** Un identificador de proceso puede reutilizarse y terminar un padre no termina necesariamente sus hijos. La generación y sus consumidores se conservan por separado.

**Consecuencia de omisión.** Puede persistir ejecución anterior aunque se haya detenido el proceso nominalmente principal. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** No se terminan otros procesos únicamente por compartir un nombre.

**Variación independiente y retirada del parámetro.** El proceso anterior puede terminar sin que se cree su sustituto. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P11.

**Prueba de partición.** Identidad de generación y evento de terminación; los hijos tienen otras identidades.

**Procedencia.** T014; T016. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P06. Identidad objetivo de la imagen utilizada

**Identidad:** `PAR-CYB-IMAGEN-OBJETIVO-ACTIVA-001`, versión 0.2.

**Sujeto y proposición.** Una imagen ejecutable utilizada por una instancia. La identidad de la imagen utilizada coincide con la identidad objetivo previamente admitida.

| Estado | Condición |
| --- | --- |
| 1 | Identidad completa y método pertinente coincidentes. |
| 0 | Identidad completa diferente. |
| U | Identidad parcial, lectura inconsistente o conflicto. |


**Observación y límites.** Win32: MODULEINFO no acredita identidad de contenido. Para núcleo o firmware se exige un método específico que identifique la imagen utilizada; la lectura de un archivo descargado no lo sustituye. La ampliación semántica de perfil se declara en v0.2.

**Conocimiento y relación necesarios.** La imagen utilizada puede diferir de la almacenada; el programa residente de un dispositivo también tiene un ámbito propio. Se relacionan imagen utilizada, almacenamiento, selección y consumidor.

**Consecuencia de omisión.** Una versión correcta en disco puede ocultar ejecución anterior en memoria o en un dispositivo. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** Una identidad diferente no demuestra por sí sola vulnerabilidad.

**Variación independiente y retirada del parámetro.** La imagen nueva puede estar almacenada mientras continúa utilizándose la anterior, o suceder lo contrario. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P13.

**Prueba de partición.** Una imagen y un consumidor. Biblioteca, núcleo y firmware no se cuentan de nuevo si conservan exactamente esta proposición.

**Procedencia.** T008; T012; T013; B02 §§3–4. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P07. Resultado favorable de una comprobación individual

**Identidad:** `PAR-CYB-COMPROBACION-POSITIVA-001`, versión 0.2.

**Sujeto y proposición.** Una ejecución válida de una prueba con un único criterio. La comprobación individual produjo el resultado favorable definido antes de ejecutarla.

| Estado | Condición |
| --- | --- |
| 1 | Resultado que satisface el criterio fijado. |
| 0 | Resultado válido que no lo satisface. |
| U | Resultado ausente, indeterminado o contradictorio. |


**Observación y límites.** Criterio y casos positivos/negativos anteriores al ensayo; umbral y alcance expresos. No sustituye los estados de P16–P24 ni permite introducir conocimiento nuevo durante el consejo.

**Conocimiento y relación necesarios.** Una comprobación puede no detectar una corrección incompleta. El resultado sólo se interpreta con el criterio, la cobertura y la sensibilidad propios del observador.

**Consecuencia de omisión.** Un informe sin hallazgos puede ocultar la incapacidad para observar el defecto residual. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** Un resultado desfavorable no autoriza una intervención automática.

**Variación independiente y retirada del parámetro.** Una identidad objetivo puede coexistir con fallo de una comprobación funcional independiente. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P06.

**Prueba de partición.** Es un resultado de prueba, no el estado universal de seguridad. Dos criterios independientes requieren dos usos identificados; una prueba compuesta no se convierte en átomo.

**Procedencia.** F018 §§4.3, 6.5, 7.3; T001 §2.3.3; B08 §1; B09 §1. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P08. Retirada satisfactoria comunicada de la actualización

**Identidad:** `PAR-CYB-RETIRADA-EXITOSA-COMUNICADA-001`, versión 0.1.

**Sujeto y proposición.** Un episodio de retirada posterior a la instalación. Se comunicó la retirada satisfactoria de la actualización dentro del intervalo observado.

| Estado | Condición |
| --- | --- |
| 1 | Evento de retirada satisfactoria acreditado. |
| 0 | Historia completa sin tal evento. |
| U | Historia insuficiente o conflicto. |


**Observación y límites.** Historia individual de actualización. La lista de eventos no acredita por sí misma cobertura completa.

**Conocimiento y relación necesarios.** La retirada es un acontecimiento histórico, incluso si después se reinstala. El acontecimiento obliga a revisar la vigencia de las pruebas afectadas.

**Consecuencia de omisión.** Se podría reutilizar una comprobación anterior a la retirada. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** Retirar una actualización no demuestra que todo el sistema haya vuelto a una versión vulnerable.

**Variación independiente y retirada del parámetro.** El archivo objetivo puede volver a estar presente tras una reinstalación sin borrar la retirada. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P13.

**Prueba de partición.** Existencia de un acontecimiento; no incluye el estado final ni la causa.

**Procedencia.** T010; T011; T001 §2.3.4. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P09. Cambio posterior de un componente binario

**Identidad:** `PAR-CYB-CAMBIO-COMPONENTE-POSTERIOR-001`, versión 0.1.

**Sujeto y proposición.** Un componente durante el intervalo posterior a su comprobación. La identidad binaria del componente cambió al menos una vez dentro del intervalo.

| Estado | Condición |
| --- | --- |
| 1 | Transición acreditada, aunque después se recupere la identidad original. |
| 0 | Historia completa sin transición. |
| U | Cobertura u orden insuficientes. |


**Observación y límites.** Historia completa para negar cambios. El intervalo y el ámbito del componente se fijan previamente.

**Conocimiento y relación necesarios.** Dos extremos iguales pueden ocultar una modificación intermedia. La vigencia de la prueba depende del componente y de su historia.

**Consecuencia de omisión.** Una comprobación antigua podría atribuirse indebidamente al estado actual. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** Un cambio irrelevante para el criterio no obliga a repetir todas las pruebas.

**Variación independiente y retirada del parámetro.** La misma identidad final puede provenir de una historia estable o de cambio y retorno. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P13.

**Prueba de partición.** La existencia de transición es única; cantidad, causa y actor se conservan como evidencia.

**Procedencia.** T001 §2.3.4; B01 §§3.3.4, 3.4. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P10. Restauración previa comunicada

**Identidad:** `PAR-CYB-RESTAURACION-PREVIA-COMUNICADA-001`, versión 0.1.

**Sujeto y proposición.** Un episodio de restauración y su objeto. Se comunicó restauración satisfactoria desde un estado capturado antes de la instalación.

| Estado | Condición |
| --- | --- |
| 1 | Restauración satisfactoria, origen anterior y alcance acreditados. |
| 0 | Historia completa que excluya tal restauración. |
| U | Origen, alcance o cobertura temporal no acreditados. |


**Observación y límites.** Registro de restauración con objeto, origen y resultado. No se ejecuta una recuperación.

**Conocimiento y relación necesarios.** Una restauración puede reintroducir estados anteriores por un mecanismo distinto de la desinstalación. Se revisan las pruebas de los objetos realmente restaurados.

**Consecuencia de omisión.** El experto podría aceptar una corrección basándose en pruebas anteriores a la restauración. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** La antigüedad de una copia no demuestra que todos sus componentes sean vulnerables.

**Variación independiente y retirada del parámetro.** Restaurar una máquina virtual puede no generar un evento de desinstalación. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P08.

**Prueba de partición.** Evento con procedencia temporal; no reúne restauración y vulnerabilidad.

**Procedencia.** T001 §2.3.4; B10 §§3.4.1, 4.3. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P11. Creación de una nueva generación de proceso

**Identidad:** `PAR-CYB-GENERACION-PROCESO-CREADA-001`, versión 0.1.

**Sujeto y proposición.** Una generación identificada de proceso. La generación se creó después de la instalación y no después del instante de evaluación.

| Estado | Condición |
| --- | --- |
| 1 | Creación acreditada dentro del intervalo. |
| 0 | Creación acreditada anterior o simultánea a la instalación. |
| U | Instante u orden desconocidos. |


**Observación y límites.** Registro de creación y orden temporal exacto. Una observación posterior al instante de evaluación no pertenece al caso.

**Conocimiento y relación necesarios.** Crear un proceso no acredita que haya terminado su inicialización. Creación, inicialización y utilización de la imagen se conservan como estados distintos.

**Consecuencia de omisión.** Podría aceptarse la mera terminación del proceso anterior sin comprobar su sustitución. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** No se crea otra instancia por ignorar una creación ya acreditada.

**Variación independiente y retirada del parámetro.** La generación anterior puede terminar con o sin creación posterior. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P05.

**Prueba de partición.** PID y tiempo son identidad; no se añade la inicialización al mismo parámetro.

**Procedencia.** T014; T015. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P12. Valor efectivo de configuración objetivo

**Identidad:** `PAR-CYB-VALOR-CONFIGURACION-EFECTIVO-OBJETIVO-001`, versión 0.1.

**Sujeto y proposición.** Una clave escalar en un consumidor. El valor efectivo de la clave coincide con el valor objetivo admitido.

| Estado | Condición |
| --- | --- |
| 1 | Mismo tipo y valor efectivo coincidentes. |
| 0 | Valor efectivo del mismo tipo diferente. |
| U | Valor efectivo desconocido o contradictorio. |


**Observación y límites.** Método específico de lectura efectiva y equivalencia tipada; ausencia sólo es valor si el esquema lo define.

**Conocimiento y relación necesarios.** Guardar una configuración no demuestra que el consumidor la haya incorporado. El valor efectivo se compara con el persistente, P16.

**Consecuencia de omisión.** Puede persistir una condición insegura aunque el archivo de configuración parezca correcto. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** Una alternativa autorizada no se rechaza sólo por diferir de otro objetivo.

**Variación independiente y retirada del parámetro.** El valor persistente puede cambiar antes de que lo utilice el consumidor. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P16.

**Prueba de partición.** Una clave escalar. Un objeto con varias propiedades exige separación por significado.

**Procedencia.** T001 §2.3.2; F018 §3.4; B01 §3.2. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P13. Identidad objetivo del artefacto almacenado

**Identidad:** `PAR-CYB-ARTEFACTO-PERSISTENTE-OBJETIVO-001`, versión 0.2.

**Sujeto y proposición.** Un artefacto binario completo y su ubicación. La identidad del artefacto almacenado coincide con el objetivo admitido.

| Estado | Condición |
| --- | --- |
| 1 | Contenido completo coincidente según el método fijado. |
| 0 | Contenido completo diferente. |
| U | Lectura parcial o inconsistente. |


**Observación y límites.** Lectura consistente del objeto completo, incluido un objeto binario de firmware si existe un perfil admitido. No afirma durabilidad física frente a un fallo eléctrico.

**Conocimiento y relación necesarios.** Almacenamiento, utilización y selección de próxima carga son estados distintos. Se enlaza con P06, P22 y la sincronización comunicada P23.

**Consecuencia de omisión.** Puede aceptarse un estado que volverá a cargar un artefacto anterior. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** La discrepancia de identidad no acredita por sí sola un defecto de seguridad.

**Variación independiente y retirada del parámetro.** El archivo puede ser nuevo y la imagen utilizada antigua. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P06.

**Prueba de partición.** Un artefacto, no una colección. Su integridad no incorpora autenticidad ni corrección funcional.

**Procedencia.** T001 §§2.3.2–2.3.4; T008; B02 §4; B03 §§3.10, 3.13. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P14. Cambio posterior de configuración

**Identidad:** `PAR-CYB-CAMBIO-CONFIGURACION-POSTERIOR-001`, versión 0.1.

**Sujeto y proposición.** Una clave y su ámbito efectivo o persistente. El valor de la clave cambió después de la comprobación de referencia.

| Estado | Condición |
| --- | --- |
| 1 | Transición acreditada dentro del intervalo. |
| 0 | Historia completa sin transición. |
| U | Cobertura temporal o valores insuficientes. |


**Observación y límites.** Historia de valores tipados; cambio y retorno cuenta como cambio.

**Conocimiento y relación necesarios.** El cambio de configuración puede invalidar una prueba sin modificar el ejecutable. Sólo se revisan pruebas cuyo criterio depende de esa clave.

**Consecuencia de omisión.** Puede conservarse una conclusión que ya no corresponde a la configuración evaluada. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** Invalidar pruebas independientes produce trabajo sin fundamento.

**Variación independiente y retirada del parámetro.** Puede cambiar una clave sin cambiar ningún binario. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P09.

**Prueba de partición.** Un valor y un ámbito; efectivo y persistente llevan usos separados.

**Procedencia.** T001 §2.3.4; B01 §§3.3.4, 3.4. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P15. Necesidad de otra acción de terminación

**Identidad:** `PAR-CYB-OTRO-CAMBIO-UNITARIO-REQUERIDO-001`, versión 0.2.

**Sujeto y proposición.** Una acción unitaria distinta de los reinicios de P01 y P04. La instrucción aplicable exige esa acción para completar la actualización.

| Estado | Condición |
| --- | --- |
| 1 | Obligación específica explícita. |
| 0 | Declaración explícita de ausencia de esa obligación. |
| U | Obligación desconocida o contradictoria. |


**Observación y límites.** Registro cerrado de clases de acción y criterios de cumplimiento en esta versión. Prohibido añadir una acción semánticamente nueva por texto libre durante el consejo.

**Conocimiento y relación necesarios.** La actualización puede exigir configuración, sustitución, invalidación o activación adicionales. Cada acción se enlaza con sus estados de cumplimiento; el verbo no constituye evidencia.

**Consecuencia de omisión.** Puede confundirse recepción del paquete con terminación de todos los efectos exigidos. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** La lista de posibilidades no es una lista de acciones obligatorias para todos los casos.

**Variación independiente y retirada del parámetro.** Puede exigirse una configuración adicional sin reiniciar el sistema. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P01.

**Prueba de partición.** Sólo registra obligación. Una acción con resultados independientes se descompone antes de evaluarla.

**Procedencia.** T001 §2.3.2; B01 §3.3.2. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P16. Valor persistente de configuración objetivo

**Identidad:** `PAR-CYB-VALOR-CONFIGURACION-PERSISTENTE-OBJETIVO-001`, versión 0.1.

**Sujeto y proposición.** Una clave escalar en su repositorio de configuración. El valor persistente de la clave coincide con el objetivo admitido.

| Estado | Condición |
| --- | --- |
| 1 | Valor persistente tipado coincidente. |
| 0 | Valor persistente tipado diferente. |
| U | Lectura persistente insuficiente o conflicto. |


**Observación y límites.** Lectura consistente del repositorio autoritativo, con tipo y objetivo fijados; no se infiere de la lectura efectiva.

**Conocimiento y relación necesarios.** Una configuración correcta en uso puede no conservarse para la próxima carga. P12 y P16 describen estados que pueden divergir.

**Consecuencia de omisión.** Una recarga posterior podría recuperar la configuración anterior. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** No se sobrescribe una configuración por confundir dos repositorios o ámbitos.

**Variación independiente y retirada del parámetro.** El consumidor conserva un valor nuevo mientras el repositorio vuelve al antiguo. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P12.

**Prueba de partición.** Un valor escalar persistente; la clave y su repositorio identifican el sujeto.

**Procedencia.** B01 §3.2; T001 §2.3.2; F018 §3.4. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P17. Inicialización del proceso completada

**Identidad:** `PAR-CYB-INICIALIZACION-PROCESO-COMPLETADA-001`, versión 0.1.

**Sujeto y proposición.** Una generación de proceso y un hito de inicialización. La generación alcanzó el hito de inicialización definido para su utilización.

| Estado | Condición |
| --- | --- |
| 1 | Hito terminal acreditado mediante señal específica. |
| 0 | Fallo terminal de inicialización o estado previo al hito acreditados. |
| U | Sin evidencia específica del hito. |


**Observación y límites.** Señal de inicialización propia del programa, identidad de generación e instante. El retorno de CreateProcessW no sirve como señal suficiente.

**Conocimiento y relación necesarios.** La creación puede preceder a fallos de carga e inicialización. P11 no implica P17; P17 tampoco demuestra salud funcional sostenida.

**Consecuencia de omisión.** Una instancia creada pero no inicializada podría presentarse como sustituto disponible. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** No se confunde una inicialización lenta con un fallo definitivo sin evidencia.

**Variación independiente y retirada del parámetro.** CreateProcessW puede devolver éxito y la inicialización terminar o fallar después. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P11.

**Prueba de partición.** Un hito unitario definido. Si reúne preparación de componentes independientes, se separan sus usos.

**Procedencia.** T015, Return value; R025. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P18. Habilitación de un parche en ejecución

**Identidad:** `PAR-CYB-PARCHE-EJECUCION-HABILITADO-001`, versión 0.1.

**Sujeto y proposición.** Un parche del núcleo identificado. El mecanismo de aplicación mantiene habilitado el parche identificado en el instante evaluado.

| Estado | Condición |
| --- | --- |
| 1 | Estado habilitado acreditado. |
| 0 | Estado deshabilitado acreditado. |
| U | Estado no observado o contradictorio. |


**Observación y límites.** Perfil Linux 6.8: enabled del parche. Se preservan identidad, instante y dirección de la transición.

**Conocimiento y relación necesarios.** La habilitación y la transición de las tareas son estados distintos. P18 se enlaza con P19 por tarea y con la cobertura de tareas.

**Consecuencia de omisión.** Podría confundirse habilitación con aplicación completa en todas las tareas. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** No se fuerza una transición por el mero hecho de encontrarla pendiente.

**Variación independiente y retirada del parámetro.** El estado habilitado puede cambiar al invertir una transición mientras una tarea conserva todavía el mismo estado de parche de referencia. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P19.

**Prueba de partición.** Un estado del mecanismo; la transición por tarea queda fuera de la proposición.

**Procedencia.** B04 §§3, 5.2, 5.4. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P19. Estado objetivo de parche en una tarea

**Identidad:** `PAR-CYB-TAREA-ESTADO-PARCHE-OBJETIVO-001`, versión 0.1.

**Sujeto y proposición.** Una tarea y una transición de parche identificadas. La tarea se encuentra en el estado de parche de referencia previamente admitido, durante la transición identificada.

| Estado | Condición |
| --- | --- |
| 1 | Estado de la tarea igual a la referencia fijada antes de evaluar. |
| 0 | Estado de la tarea contrario al objetivo. |
| U | Observación insuficiente, conflicto o estado no interpretable en ese contexto. |


**Observación y límites.** Linux 6.8: patch_state 0/1 se compara con una referencia fijada previamente; la dirección de transición se conserva, pero no redefine esa referencia. El valor -1 fuera de transición no significa sin parche ni equivale a Tri.U; ese perfil no está activo.

**Conocimiento y relación necesarios.** Las tareas pueden transitar en momentos diferentes. Cada tarea tiene un uso independiente; un estado global no se copia a todas.

**Consecuencia de omisión.** Una tarea puede seguir utilizando funciones anteriores mientras otras ya han transitado. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** Se evita forzar o reiniciar tareas que ya alcanzaron el objetivo.

**Variación independiente y retirada del parámetro.** Con el mismo enabled, dos tareas pueden tener estados de parche distintos. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P18.

**Prueba de partición.** Una tarea y una transición. La conjunción sobre todas las tareas es una composición.

**Procedencia.** B04 §3. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P20. Referencia vigente a un recurso anterior

**Identidad:** `PAR-CYB-REFERENCIA-RECURSO-ANTERIOR-VIGENTE-001`, versión 0.1.

**Sujeto y proposición.** Un consumidor y un recurso de generación anterior. El consumidor mantiene una referencia utilizable al recurso anterior identificado.

| Estado | Condición |
| --- | --- |
| 1 | Referencia utilizable acreditada. |
| 0 | Ausencia acreditada de esa referencia en el consumidor. |
| U | Enumeración o validez de referencia insuficientes. |


**Observación y límites.** Identidad de generación, titular, ámbito y posibilidad de uso; ausencia exige enumeración completa del ámbito del consumidor.

**Conocimiento y relación necesarios.** La terminación de un proceso no elimina todas las referencias conservadas por otros consumidores. La referencia se enlaza con el consumidor y la obligación de sustituir el recurso.

**Consecuencia de omisión.** Puede persistir utilización del recurso anterior o ser insegura su retirada. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** No se retira un recurso todavía referenciado ni se confunde mera dirección numérica con referencia vigente.

**Variación independiente y retirada del parámetro.** El proceso principal puede terminar mientras otro consumidor conserva una referencia. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P05.

**Prueba de partición.** Una relación consumidor–recurso. La existencia de referencia y el contenido del recurso son estados diferentes.

**Procedencia.** T016; B04 §5.5; R025. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P21. Contenido objetivo de una entrada de caché

**Identidad:** `PAR-CYB-ENTRADA-CACHE-CONTENIDO-OBJETIVO-001`, versión 0.1.

**Sujeto y proposición.** Una entrada de caché y su consumidor. El contenido utilizable de la entrada coincide con el objetivo definido para ese consumidor.

| Estado | Condición |
| --- | --- |
| 1 | Contenido e identidad de entrada coincidentes con el objetivo. |
| 0 | Contenido utilizable diferente. |
| U | Entrada o contenido no observables de forma concluyente. |


**Observación y límites.** Perfil de caché de datos derivados: clave, generación, consumidor y criterio de identidad. La correspondencia entre origen y entrada debe estar documentada antes de usarla.

**Conocimiento y relación necesarios.** Un estado conservado en memoria puede diferir del que se volvería a cargar desde su origen. El origen correcto no determina por sí solo la entrada utilizada.

**Consecuencia de omisión.** El consumidor podría seguir tomando decisiones con estado anterior pese a la actualización del origen. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** No se vacía toda caché ni se confunde ausencia de entrada con contenido obsoleto.

**Variación independiente y retirada del parámetro.** El artefacto de origen puede ser idéntico y la entrada conservada diferente. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P13.

**Prueba de partición.** Una entrada con un contenido semánticamente indivisible. Configuración efectiva se remite a P12; código utilizado a P06, sin doble conteo.

**Procedencia.** B11, File Caching; B05 §4; R025. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P22. Selección del objetivo para la próxima carga

**Identidad:** `PAR-CYB-SELECCION-PROXIMA-CARGA-OBJETIVO-001`, versión 0.1.

**Sujeto y proposición.** Un punto de carga y su configuración de selección. La selección resuelta en el instante de evaluación designa el artefacto objetivo.

| Estado | Condición |
| --- | --- |
| 1 | Selección inequívoca del objetivo. |
| 0 | Selección inequívoca de otro artefacto. |
| U | Selección ambigua, cambiante o no resuelta. |


**Observación y límites.** Regla de resolución del cargador fijada y entradas completas; para bancos de firmware se exige su regla específica. No se extrapola la búsqueda de DLL a firmware.

**Conocimiento y relación necesarios.** El artefacto correcto puede estar presente sin ser el que selecciona el cargador. Selección, contenido almacenado e imagen utilizada se contrastan por separado.

**Consecuencia de omisión.** Una próxima carga podría volver al artefacto anterior aunque el objetivo esté disponible. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** No se elimina una copia legítima por confundir presencia y prioridad de selección.

**Variación independiente y retirada del parámetro.** Dos configuraciones de búsqueda pueden seleccionar archivos distintos con los mismos archivos almacenados. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P13.

**Prueba de partición.** Una relación de selección resuelta; no promete que ocurra una carga futura.

**Procedencia.** T008, Factors that affect searching; B03 §§3.10, 3.11, 3.21. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P23. Sincronización satisfactoria comunicada del archivo

**Identidad:** `PAR-CYB-SINCRONIZACION-ARCHIVO-EXITO-COMUNICADO-001`, versión 0.1.

**Sujeto y proposición.** Una operación de sincronización y un archivo. La operación de sincronización del archivo comunicó terminación satisfactoria.

| Estado | Condición |
| --- | --- |
| 1 | Resultado satisfactorio según el contrato de la operación. |
| 0 | Resultado de fallo según ese contrato. |
| U | Resultado no disponible o contradictorio. |


**Observación y límites.** Perfil FlushFileBuffers para un archivo y sistema admitidos. FlushViewOfFile no es evidencia equivalente; el modelo de almacenamiento y sus garantías permanecen expresos.

**Conocimiento y relación necesarios.** La escritura visible y la sincronización comunicada tienen alcances diferentes. P13 describe contenido leído; P23 describe un resultado de sincronización identificado.

**Consecuencia de omisión.** Una lectura correcta podría confundirse con acreditación de persistencia bajo el modelo de fallo aplicable. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** No se ordenan sincronizaciones repetidas sin necesidad ni se atribuye durabilidad física ilimitada.

**Variación independiente y retirada del parámetro.** La lectura del archivo puede ser correcta antes y después de una sincronización fallida. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P13.

**Prueba de partición.** Un resultado comunicado. Metadatos, datos y dispositivo requieren identificación del alcance, no una garantía agregada.

**Procedencia.** B06, Return value y Remarks; B07, Remarks; B11. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## P24. Operación diferida de archivo pendiente

**Identidad:** `PAR-CYB-OPERACION-DIFERIDA-ARCHIVO-PENDIENTE-001`, versión 0.1.

**Sujeto y proposición.** Una operación diferida de archivo identificada. La operación permanece pendiente en el mecanismo que debe ejecutarla.

| Estado | Condición |
| --- | --- |
| 1 | Entrada pendiente identificada y vigente. |
| 0 | Ausencia acreditada en una enumeración completa de ese mecanismo. |
| U | Lectura incompleta o correspondencia ambigua. |


**Observación y límites.** Perfil PendingFileRenameOperations: origen, destino, orden e instalación. No se modifica el registro ni se programa ninguna operación.

**Conocimiento y relación necesarios.** Aceptar una operación diferida no demuestra su ejecución. La pendiente se enlaza con el archivo, su identidad y la condición de ejecución.

**Consecuencia de omisión.** El experto podría dar por aplicada una sustitución que sólo fue programada. La consecuencia se refiere a un consejo potencialmente erróneo; no se declara un daño observado.

**Consecuencia del exceso.** La ausencia de pendiente tampoco demuestra éxito: la operación pudo cancelarse.

**Variación independiente y retirada del parámetro.** La instalación puede comunicar éxito con o sin operación diferida pendiente. Si se retira esta proposición, los restantes estados del ejemplo no permiten reconstruir la diferencia relevante para el consejo. Se contrasta especialmente con P02.

**Prueba de partición.** Una operación de un mecanismo, no todas las acciones pendientes del sistema.

**Procedencia.** B12, MOVEFILE_DELAY_UNTIL_REBOOT y Remarks. Véase la [referencia completa y sus límites](BIBLIOGRAFIA_RAZONADA_OP_CYB_001_v0.2.md).

## Uso responsable del registro

Los estados no se suman ni se promedian. P01=1 expresa una obligación, P08=1 un acontecimiento de retirada y P20=1 una referencia conservada; ninguno significa automáticamente que el caso sea favorable. La regla del caso conserva qué estados requiere, qué incertidumbres impiden cerrar y qué actuaciones sólo puede autorizar el experto.
