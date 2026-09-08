# Lote atómico P02–P10 · OP-CYB-001 / Q0 v0.1

**Fecha:** 08-09-2026. **Base:** apertura/adopción `2454cb1080c2f824bd3b8115cb31729db8f2d7e8`, cuyo padre es el expediente inicial `b8e5943cce29e10851c5829a84c117044a1eb906`. **Libro principal:** `CATALOGO_CURRICULAR_CIBERSEGURIDAD_v0.5.xlsx`, hojas 45–55.

**Resultado de la unidad:** nueve adjudicaciones `PARAMETRO_ATOMICO_EN_PERFIL_DOCUMENTAL`, que junto al primer parámetro forman un registro de **diez**. P01 fue adoptado por Dirección en el [acta](ACTA_APERTURA_Y_ADOPCION_PRIMER_PARAMETRO_v0.1.md). Los nueve nuevos se entregan con dictamen favorable y límites explícitos; no se inventa su aprobación nominal humana anticipada. El universo está abierto en constitución y no se declara apto para cierre operacional.

## 1. Qué se ha hecho y con qué precedencia

El [manifiesto](MANIFIESTO_ALCANCE_COBERTURA_TERMINACION_OP_CYB_001_Q0_v0.1.md) fija nueve raíces y 31 distinciones. Se han escogido nueve predicados relevantes para interpretar instalación, completitud, estado activo, comprobación y cambios posteriores. No se ha ampliado el inventario ni supuesto que diez parámetros resuelven diez distinciones exhaustivamente. QCY-04-D3/D4 y otras preguntas amplias conservan cobertura parcial en la hoja 52.

Las fuentes T001–T006 del primer parámetro se conservan. Siete capturas primarias adicionales, T007–T013, delimitan Fast Startup, cargador DLL, Restart Manager, historia de actualización y límites de MODULEINFO. Su contenido técnico se leyó antes de preparar los testigos. Las guías educativas R025, R033 y R035 siguen aportando comprensión de procesos/memoria/ficheros, continuidad y juicio de riesgo; una API no sustituye esa formación.

La generalidad de NIST acredita la necesidad de distinguir aplicación, activación, comprobación y monitorización; **no suministra valores de un caso concreto**. Un requisito de fabricante, un registro de ciclo de vida o una evidencia de imagen activa debe tener identidad, regla de adquisición y admisión propias. En este lote esos objetos de episodio son testigos sintéticos, no registros de activos reales.

## 2. Contrato común de los perfiles documentales

Cada ficha declara un predicado y su horizonte. Identidad del activo, componente, instalación/intento, fuente/version y corte son controles/contexto; no se cuentan como átomos adicionales. Cuando se cita un proceso se exige identidad de generación, no sólo PID. Las huellas identifican bytes, no la verdad de la observación ni un código cargado por sí mismas.

El ensayo conserva separadamente:

- dato válido que determina 1 o 0;
- ausencia declarada, conflicto o insuficiencia observacional que dan U;
- configuración del uso no constituida;
- no admisión por identidad/forma;
- fuera de perfil;
- fallo técnico de captura, sin salida alternativa del dominio.

Las causas de U son diagnósticos del perfil; no amplían `Tri={0,1,U}`. Un resultado de instalación fallida es un hecho profesional, distinto del fallo del observador. El lector documental no introduce capacidades productivas del Lenguaje ni reinstaura el compilador Python retirado.

Un testigo positivo de existencia puede ser suficiente aunque el resto del registro sea parcial. Para negar que ocurrió un evento en un intervalo se necesita cobertura acreditada de ese intervalo. Si un registro es parcial y no contiene testigo positivo, el resultado es U. Las fuentes generales no certifican cobertura, fidelidad del reloj, autenticidad o exhaustividad de ningún registro real: esas capacidades de admisión permanecen pendientes.

Los contratos preservan bytes/lexemas antes de cualquier transformación. El perfil de imagen ensaya dos tokens SHA-256 sintéticos canónicos de 64 caracteres hexadecimales minúsculos. **No calcula la huella de una imagen en memoria** ni iguala hash de fichero con memoria (relocaciones, ASLR y modificaciones necesitan método propio). Las fórmulas mantienen originales textuales; las comprobaciones de sintaxis por bloques hexadecimales no sustituyen la identidad por un número.

Las codificaciones del ensayo están visibles en 55. Son representaciones documentales de hechos supuestos admitidos; no son enums universales SV. No se permite que un conector convierta una fuente insuficiente en testigo suficiente cambiando esa etiqueta: la validación material de su adquisición deberá constituirse y probarse aparte.

## 3. Adjudicaciones
### P02 · Éxito comunicado de instalación

**Identidad:** `PAR-CYB-INSTALACION-EXITO-COMUNICADO-001` v0.1. **Distinción:** `QCY-03-D2`. **Perfil:** `WUA-RESULTADO-INDIVIDUAL-0.1`.

> La operación individual de instalación identificada comunicó terminación satisfactoria sin el calificador de errores del emisor.

**Sujeto:** Activo, actualización/revisión e intento individual de instalación; correspondencia índice–colección original. **Horizonte:** Resultado terminal de aquel intento. Un resultado de otro intento no lo modifica.

**G3 — observación:** IUpdateInstallationResult.ResultCode; HResult se conserva como evidencia separada. No es HRESULT de la llamada de captura.

| Estado | Contrato |
|---|---|
| 1 | orcSucceeded. |
| 0 | orcSucceededWithErrors, orcFailed u orcAborted; 0 niega esta proposición, no afirma que nada se instaló. |
| U y controles | Resultado ausente o conflicto de resultados terminales admitidos. NotStarted/InProgress quedan fuera del perfil terminal. |

**G4 — conocimiento y consecuencia:** Omitir estado final o normalizar éxito con errores como éxito pleno hace parecer completada una fase no acreditada. Persistencia potencial sólo si la corrección dependía de lo que falló; no se deduce ausencia total de instalación ni explotación. El exceso contrario también importa: Tratar el fallo de instalación como caída del sistema SV borra un hecho útil para el experto.

**Función separable:** Separar el resultado profesional comunicado de completitud, efecto y fallo del observador.

**Variación independiente:** Puede variar el resultado de un intento con igual necesidad de cierre y mismo estado activo aportado por un intento previo. No se mantiene artificialmente admitido P01 cuando falta orcSucceeded.

**Ablación AB-L10-02:** se comparan mundos con el mismo resto semántico declarado y distinto estado del predicado. Se retiran el estado y toda pista lateral que lo recodifique. La obligación del caso positivo es: «Puede conservarse el éxito comunicado de ESTE intento como evidencia de esa fase; aún faltan completitud y efecto.». En el negativo: «Debe conservarse el resultado distinto de éxito pleno e investigarse su alcance antes de presentar ESTA fase como satisfactoria.». Ambas conservan los límites de la ficha y no emiten una actuación.

**Intento de partición/duplicación:** No crear tres átomos uno-por-enum. El observable completo conserva errores; el uso pide exactamente éxito comunicado sin ese calificador.

**Límite material:** No acredita que el parche haya tomado efecto. El perfil P01 sigue exigiendo orcSucceeded y no se amplía.

**Fuentes/localizadores:** T004 Constants; T005; T006; R025. Los originales se identifican en 43/53 y los inventarios vinculados. Las fuentes profesionales justifican la necesidad y la semántica; los resultados de episodio sólo proceden de los testigos declarados.

**G5:** `PARAMETRO_ATOMICO_EN_PERFIL_DOCUMENTAL`. Identidad, único estado, U propia, consecuencia, función, independencia, ablación, partición, reproducción y procedencia constan individualmente en 49. Propiedad matricial: pendiente G6; adopción nominal de esta ficha: pendiente.

### P03 · Reinicio completo realizado

**Identidad:** `PAR-CYB-REINICIO-SISTEMA-REALIZADO-001` v0.1. **Distinción:** `QCY-04-D2`. **Perfil:** `EVENTO-REINICIO-COMPLETO-0.1`.

> Se completó al menos un reinicio íntegro del sistema anfitrión después del resultado de instalación y no después del corte.

**Sujeto:** Mismo anfitrión/instalación; evento de arranque y corte identificados, sin confundir huésped VM con anfitrión físico. **Horizonte:** Intervalo (fin de instalación, corte]. El orden debe estar acreditado; no se infiere de la mera fecha de captura.

**G3 — observación:** Dossier de arranque con identidad del sistema, clase de arranque, orden y completitud admitidos. No existe aquí un capturador de eventos validado.

| Estado | Contrato |
|---|---|
| 1 | Testigo de reinicio completo terminado en el intervalo. |
| 0 | Registro con cobertura acreditada del intervalo sin tal evento; sólo arranque híbrido con cobertura completa también niega esta proposición. |
| U y controles | Registro parcial sin testigo positivo, clase de arranque no probada, orden incierto o conflicto. |

**G4 — conocimiento y consecuencia:** Equiparar apagado/encendido híbrido con reinicio completo puede dar por satisfecha una condición pendiente. Sólo afecta al cierre si esa instalación necesitaba dicho reinicio; ni el reinicio completo garantiza la corrección. El exceso contrario también importa: Omitir un reinicio ya realizado puede inducir repetición e interrupción evitables, según servicio y ventana.

**Función separable:** Aportar satisfacción de la condición de reinicio del sistema, sin reescribir el requisito histórico.

**Variación independiente:** Mismo P01=1: un mundo posee un reinicio posterior y otro no. El requisito histórico sigue siendo 1 en ambos.

**Ablación AB-L10-03:** se comparan mundos con el mismo resto semántico declarado y distinto estado del predicado. Se retiran el estado y toda pista lateral que lo recodifique. La obligación del caso positivo es: «Puede citarse el evento posterior como satisfacción de la condición específica de reinicio íntegro; falta verificar efecto.». En el negativo: «La condición de reinicio íntegro no queda satisfecha en el intervalo examinado; no puede declararse completitud por esa vía.». Ambas conservan los límites de la ficha y no emiten una actuación.

**Intento de partición/duplicación:** Fecha, identificador y tipo son condiciones de identidad del evento. No se adjudica un parámetro por cada campo; el predicado es existencia del evento completo.

**Límite material:** Fast Startup es contraejemplo Windows 10, no regla universal de toda plataforma. Reinicio solicitado, comienzo del arranque o uptime aislado no bastan.

**Fuentes/localizadores:** T001 §2.3.2; T007 Summary/More information; R025. Los originales se identifican en 43/53 y los inventarios vinculados. Las fuentes profesionales justifican la necesidad y la semántica; los resultados de episodio sólo proceden de los testigos declarados.

**G5:** `PARAMETRO_ATOMICO_EN_PERFIL_DOCUMENTAL`. Identidad, único estado, U propia, consecuencia, función, independencia, ablación, partición, reproducción y procedencia constan individualmente en 49. Propiedad matricial: pendiente G6; adopción nominal de esta ficha: pendiente.

### P04 · Reinicio de software requerido

**Identidad:** `PAR-CYB-REINICIO-SOFTWARE-REQUERIDO-001` v0.1. **Distinción:** `QCY-04-D3`. **Perfil:** `REQUISITO-SOFTWARE-INDIVIDUAL-0.1`.

> La instrucción específica admitida para completar esta instalación exigía reiniciar el software identificado.

**Sujeto:** Un software identificable y su alcance de ejecución en un anfitrión; instalación e instrucción/version. No una lista de aplicaciones. **Horizonte:** Requisito documentado al resultado de instalación, conservado como hecho histórico.

**G3 — observación:** Cláusula o resultado específico del instalador/fabricante con alcance identificable que exige o niega ese reinicio. El párrafo genérico de NIST no suministra ese dato.

| Estado | Contrato |
|---|---|
| 1 | Requisito positivo explícito y aplicable al software identificado. |
| 0 | Negación explícita de ese requisito, con el mismo alcance. |
| U y controles | Instrucción ausente, formulación ambigua o conflicto de instrucciones admitidas. Falta de contrato de aplicabilidad es configuración pendiente, no Tri. |

**G4 — conocimiento y consecuencia:** Leer sólo P01=0 puede ocultar que un software requiere reinicio para liberar/cambiar recursos de ejecución. Una corrección puede seguir incompleta si depende de ese cambio; la fuente concreta debe establecer la dependencia. No todo software exige reinicio. El exceso contrario también importa: Convertir cualquier archivo en uso en mandato de reinicio inventa obligación e impacto.

**Función separable:** Conservar una obligación relativa al software, independiente del reinicio del sistema.

**Variación independiente:** Un software reiniciable puede requerir reinicio sin exigir reiniciar el OS; dos paquetes con P01=0 pueden diferir en este requisito.

**Ablación AB-L10-04:** se comparan mundos con el mismo resto semántico declarado y distinto estado del predicado. Se retiran el estado y toda pista lateral que lo recodifique. La obligación del caso positivo es: «Hay que obtener evidencia de cumplimiento del reinicio de ESTE software antes de declarar satisfecha esa obligación.». En el negativo: «Esta instrucción no impone reiniciar ESTE software; no se debe inventar esa obligación desde el resultado del sistema.». Ambas conservan los límites de la ficha y no emiten una actuación.

**Intento de partición/duplicación:** Requisito y cumplimiento son estados distintos. No se agrupan redespliegue, cambio de configuración y reinicio bajo un único booleano de «otros cambios».

**Límite material:** Sólo cubre este predicado de D3. Redespliegue/configuración y múltiples softwares permanecen pendientes; no se contabilizan como cubiertos.

**Fuentes/localizadores:** T001 §2.3.2; T009 cuerpo técnico; R025. Los originales se identifican en 43/53 y los inventarios vinculados. Las fuentes profesionales justifican la necesidad y la semántica; los resultados de episodio sólo proceden de los testigos declarados.

**G5:** `PARAMETRO_ATOMICO_EN_PERFIL_DOCUMENTAL`. Identidad, único estado, U propia, consecuencia, función, independencia, ablación, partición, reproducción y procedencia constan individualmente en 49. Propiedad matricial: pendiente G6; adopción nominal de esta ficha: pendiente.

### P05 · Generación previa de proceso terminada

**Identidad:** `PAR-CYB-GENERACION-PROCESO-TERMINADA-001` v0.1. **Distinción:** `QCY-04-D4`. **Perfil:** `TERMINACION-GENERACION-PROCESO-0.1`.

> Terminó la ejecución de la generación de proceso identificada después del ancla de instalación y no después del corte.

**Sujeto:** Un proceso previo: anfitrión, ámbito de proceso, identidad de generación y episodio. Un PID aislado no identifica una generación. **Horizonte:** Intervalo (ancla de instalación declarada, corte]; el ancla debe fijarse antes del contraste y no moverse para producir 1.

**G3 — observación:** Testigo de terminación vinculado a la generación; para ausencia, registro completo de su ciclo de vida en el intervalo.

| Estado | Contrato |
|---|---|
| 1 | Evento de terminación de aquella generación en el intervalo. |
| 0 | Ausencia acreditada de tal terminación en el intervalo. |
| U y controles | PID sin generación, registro incompleto, orden incierto o conflicto. Error de captura se registra fuera de Tri. |

**G4 — conocimiento y consecuencia:** Tomar la creación de otra instancia como cierre de la anterior puede dejar ejecución antigua concurrente ignorada. Relevancia cuando la condición de completitud exige liberar aquella ejecución; no se afirma que todos los recursos compartidos hayan quedado libres. El exceso contrario también importa: Repetir una terminación ya acreditada o actuar sobre un PID reutilizado puede afectar a otra ejecución.

**Función separable:** Conservar que la ejecución previa dejó de mantener sus recursos; no equipararlo con nuevo proceso operativo.

**Variación independiente:** Puede crearse una instancia nueva con la anterior aún viva, o terminar la anterior sin que arranque otra. P05 y P06 no se sustituyen.

**Ablación AB-L10-05:** se comparan mundos con el mismo resto semántico declarado y distinto estado del predicado. Se retiran el estado y toda pista lateral que lo recodifique. La obligación del caso positivo es: «Puede excluirse la continuidad de ejecución de AQUELLA generación después de su terminación; no se declara reinicio completo.». En el negativo: «La creación de otra instancia no elimina la ejecución previa; el consejo debe conservar pendiente su terminación cuando sea necesaria.». Ambas conservan los límites de la ficha y no emiten una actuación.

**Intento de partición/duplicación:** Se rechazó «reinicio del software realizado» como agregado de terminación y nueva ejecución útil. Aquí se adjudica sólo el evento de terminación; arranque y disponibilidad no se esconden.

**Límite material:** No satisface por sí solo P04. Reinicio íntegro, todas las instancias, redeploy y configuración continúan pendientes en D4.

**Fuentes/localizadores:** T009 cuerpo técnico; T008 loaded-module list; R025 IV tema 4. Los originales se identifican en 43/53 y los inventarios vinculados. Las fuentes profesionales justifican la necesidad y la semántica; los resultados de episodio sólo proceden de los testigos declarados.

**G5:** `PARAMETRO_ATOMICO_EN_PERFIL_DOCUMENTAL`. Identidad, único estado, U propia, consecuencia, función, independencia, ablación, partición, reproducción y procedencia constan individualmente en 49. Propiedad matricial: pendiente G6; adopción nominal de esta ficha: pendiente.

### P06 · Imagen objetivo activa

**Identidad:** `PAR-CYB-IMAGEN-OBJETIVO-ACTIVA-001` v0.1. **Distinción:** `QCY-05-D2`. **Perfil:** `IDENTIDAD-IMAGEN-CARGADA-0.1`.

> La imagen del componente cargada en la instancia evaluada al corte coincide con la imagen objetivo previamente fijada.

**Sujeto:** Una instancia/generación, un componente cargado, imagen objetivo, método de identidad admitido e instalación relacionada. **Horizonte:** Estado observado al corte de aquella instancia. No describe todas las instancias ni conserva vigencia frente a eventos futuros.

**G3 — observación:** Dos identidades exactas obtenidas con el mismo método admitido: imagen realmente cargada y objetivo fijado. La evidencia debe justificar correspondencia runtime–imagen; no basta leer el fichero por su ruta.

| Estado | Contrato |
|---|---|
| 1 | Identidades exactas iguales bajo ese método y alcance. |
| 0 | Identidad runtime acreditada distinta del objetivo. |
| U y controles | Sólo fichero en disco, ruta, nombre, dirección/puntero, tamaño o versión no inequívoca; captura insuficiente o contradictoria. |

**G4 — conocimiento y consecuencia:** Atribuir al proceso la imagen encontrada en disco o por nombre puede ocultar otra DLL resuelta/cargada. Persistencia potencial sólo si la imagen activa conserva el defecto relevante. Una imagen distinta puede ser otra corrección válida; no se decide aquí. El exceso contrario también importa: Tratar toda diferencia como vulnerabilidad probada puede provocar cambio o indisponibilidad innecesarios.

**Función separable:** Separar distribución en disco de qué código está activo en la instancia examinada.

**Variación independiente:** Igual instalación comunicada y terminación de proceso previo: distintas resoluciones del cargador pueden activar imágenes diferentes.

**Ablación AB-L10-06:** se comparan mundos con el mismo resto semántico declarado y distinto estado del predicado. Se retiran el estado y toda pista lateral que lo recodifique. La obligación del caso positivo es: «Puede acreditarse la identidad objetivo activa en ESTA instancia, conservando pendientes criterio de efecto y otras instancias.». En el negativo: «No puede atribuirse a ESTA instancia la imagen objetivo desde el fichero en disco; hay que determinar la adecuación de la imagen distinta.». Ambas conservan los límites de la ficha y no emiten una actuación.

**Intento de partición/duplicación:** El digest objetivo es contexto, no un átomo. Comparar identidad de imagen es una sola proposición; no se mezclan firma, autenticidad o efectividad del parche.

**Límite material:** MODULEINFO no entrega huella del código. No se define hash ingenuo de memoria (ASLR, relocaciones o modificaciones). El método productivo de identidad/captura sigue pendiente; aquí se ensaya el contrato sobre identidades documentales sintéticas.

**Fuentes/localizadores:** T001 §2.3.3; T008; T012–T013; R025 IV temas 4/5/6. Los originales se identifican en 43/53 y los inventarios vinculados. Las fuentes profesionales justifican la necesidad y la semántica; los resultados de episodio sólo proceden de los testigos declarados.

**G5:** `PARAMETRO_ATOMICO_EN_PERFIL_DOCUMENTAL`. Identidad, único estado, U propia, consecuencia, función, independencia, ablación, partición, reproducción y procedencia constan individualmente en 49. Propiedad matricial: pendiente G6; adopción nominal de esta ficha: pendiente.

### P07 · Resultado positivo de comprobación

**Identidad:** `PAR-CYB-COMPROBACION-POSITIVA-001` v0.1. **Distinción:** `QCY-05-D3`. **Perfil:** `COMPROBACION-CRITERIO-UNITARIO-0.1`.

> La comprobación individual identificada satisfizo el único criterio de aceptación previamente fijado para ella.

**Sujeto:** Una ejecución de comprobación, activo/componente, criterio unitario/version, método y evidencia. No una campaña ni un agregado de hallazgos. **Horizonte:** Resultado de aquella ejecución; una comprobación nueva recibe otra identidad y no modifica retrospectivamente este resultado.

**G3 — observación:** Informe con observación y criterio previos, resultado reproducible y alcance identificado. El informe debe enlazar evidencia, no contener sólo un sello «apto».

| Estado | Contrato |
|---|---|
| 1 | La observación satisface el criterio unitario admitido. |
| 0 | La observación no lo satisface, con prueba válida. |
| U y controles | Observación ausente, evidencia insuficiente o conflicto. Criterio compuesto o no fijado impide admisión al perfil, no produce un falso negativo. |

**G4 — conocimiento y consecuencia:** Cerrar desde la presencia del paquete o imagen prescindiendo del contraste puede atribuir un efecto no probado. El criterio debe ser pertinente y sensible al defecto que pretende observar. Positivo no demuestra por sí solo aptitud de todo OP-CYB-001. El exceso contrario también importa: Confundir prueba no ejecutable con resultado negativo inventa un fallo de corrección; ignorar alcance produce confianza excesiva.

**Función separable:** Conservar el resultado de una comprobación sin convertirlo en cierre global o ausencia universal de vulnerabilidades.

**Variación independiente:** Una imagen objetivo puede estar activa y la comprobación fallar por configuración; la misma imagen puede superar el criterio con configuración correcta.

**Ablación AB-L10-07:** se comparan mundos con el mismo resto semántico declarado y distinto estado del predicado. Se retiran el estado y toda pista lateral que lo recodifique. La obligación del caso positivo es: «Puede citarse el cumplimiento de ESTE criterio y su evidencia, sin extrapolar al cierre global.». En el negativo: «Debe preservarse el incumplimiento de ESTE criterio; la identidad de imagen no permite suprimirlo del consejo.». Ambas conservan los límites de la ficha y no emiten una actuación.

**Intento de partición/duplicación:** Si el criterio reúne resultados con incertidumbre/consecuencia separables es compuesto y queda fuera. Este parámetro sólo admite un predicado evaluativo unitario.

**Límite material:** La unidad no ha fijado un oráculo de explotación real ni ejecutado pruebas sobre activos. Valida el contrato documental del resultado, no la sensibilidad operacional del futuro criterio.

**Fuentes/localizadores:** T001 §2.3.3; R025; R035. Los originales se identifican en 43/53 y los inventarios vinculados. Las fuentes profesionales justifican la necesidad y la semántica; los resultados de episodio sólo proceden de los testigos declarados.

**G5:** `PARAMETRO_ATOMICO_EN_PERFIL_DOCUMENTAL`. Identidad, único estado, U propia, consecuencia, función, independencia, ablación, partición, reproducción y procedencia constan individualmente en 49. Propiedad matricial: pendiente G6; adopción nominal de esta ficha: pendiente.

### P08 · Retirada exitosa comunicada

**Identidad:** `PAR-CYB-RETIRADA-EXITOSA-COMUNICADA-001` v0.1. **Distinción:** `QCY-08-D1`. **Perfil:** `HISTORIA-RETIRADA-ACTUALIZACION-0.1`.

> Existe después de la instalación y hasta el corte una operación de retirada de esa actualización que comunica éxito.

**Sujeto:** Activo, actualización/revisión, episodio inicial y operación posterior de retirada identificada. **Horizonte:** Existencia histórica en (fin de instalación, corte]. Reinstalar después no borra el suceso.

**G3 — observación:** Historia admitida: identidad, Operation, ResultCode y orden. QueryHistory por sí solo no demuestra que su historia sea íntegra.

| Estado | Contrato |
|---|---|
| 1 | Operación uoUninstallation con orcSucceeded, correctamente vinculada y posterior. |
| 0 | Ninguna operación así en historia cuya cobertura del intervalo está acreditada. |
| U y controles | Cobertura parcial sin positivo, éxito con errores sin conclusión suficiente sobre retirada, orden incierto o conflicto. |

**G4 — conocimiento y consecuencia:** Reutilizar el éxito de instalación sin mirar retiradas posteriores puede mantener evidencia superada. Puede reintroducirse el defecto si se retiró lo que lo corregía y no existe corrección alternativa; la retirada comunicada no prueba ese daño. El exceso contrario también importa: Tratar una retirada fallida o antigua como retirada posterior exitosa inventa pérdida de corrección.

**Función separable:** Activar reexamen del cierre frente a una retirada comunicada, conservando diferencia entre resultado comunicado y estado actual.

**Variación independiente:** Puede haber retirada y reinstalación con idéntica imagen activa final; o no haber retirada con esa misma imagen.

**Ablación AB-L10-08:** se comparan mundos con el mismo resto semántico declarado y distinto estado del predicado. Se retiran el estado y toda pista lateral que lo recodifique. La obligación del caso positivo es: «Hay que enlazar la retirada comunicada y su eventual corrección posterior; el éxito inicial aislado no justifica continuidad.». En el negativo: «No se impone reexamen por una retirada exitosa en ESTE intervalo acreditadamente cubierto; otras causas permanecen abiertas.». Ambas conservan los límites de la ficha y no emiten una actuación.

**Intento de partición/duplicación:** No se crea un átomo para cada resultado de retirada. La semántica del suceso permanece separada de la integridad de la historia y del estado actual.

**Límite material:** Cubre retirada comunicada, no toda reversión posible de D1. La ausencia del paquete en inventario no prueba esta causa.

**Fuentes/localizadores:** T001 §§2.3.2/2.3.4; T010–T011; T004. Los originales se identifican en 43/53 y los inventarios vinculados. Las fuentes profesionales justifican la necesidad y la semántica; los resultados de episodio sólo proceden de los testigos declarados.

**G5:** `PARAMETRO_ATOMICO_EN_PERFIL_DOCUMENTAL`. Identidad, único estado, U propia, consecuencia, función, independencia, ablación, partición, reproducción y procedencia constan individualmente en 49. Propiedad matricial: pendiente G6; adopción nominal de esta ficha: pendiente.

### P09 · Cambio posterior del componente

**Identidad:** `PAR-CYB-CAMBIO-COMPONENTE-POSTERIOR-001` v0.1. **Distinción:** `QCY-08-D2`. **Perfil:** `HISTORIA-CAMBIO-COMPONENTE-0.1`.

> Ocurrió al menos un cambio de identidad binaria del componente desde la comprobación de referencia hasta el corte.

**Sujeto:** Activo y componente lógico, referencia verificada, cadena de eventos y criterio de identidad binaria fijados. **Horizonte:** Intervalo (comprobación de referencia, corte]. Se conserva el evento aunque después se vuelva a la imagen anterior.

**G3 — observación:** Testigo de transición entre identidades distintas bajo el mismo método, con orden y enlace al componente; ausencia exige cobertura suficiente.

| Estado | Contrato |
|---|---|
| 1 | Transición acreditada; también cambio seguido de retorno a identidad inicial. |
| 0 | Ninguna transición en historia acreditadamente completa. |
| U y controles | Sólo comparación de estados extremos, hueco del registro, identidad binaria insuficiente u orden incierto. |

**G4 — conocimiento y consecuencia:** Comparar sólo versiones finales puede ocultar cambios y retornos que afecten a la evidencia intermedia. El cambio puede invalidar la inferencia desde la prueba anterior; no demuestra por sí mismo nueva vulnerabilidad ni fallo del componente. El exceso contrario también importa: Cambio de etiqueta de catálogo sin cambio binario no se convierte en evento de este parámetro.

**Función separable:** Conservar el antecedente que obliga a revisar la transportabilidad de una comprobación anterior.

**Variación independiente:** Estado final objetivo igual en ambos mundos: en uno hubo sustitución y retorno, en otro no. P06 no determina P09.

**Ablación AB-L10-09:** se comparan mundos con el mismo resto semántico declarado y distinto estado del predicado. Se retiran el estado y toda pista lateral que lo recodifique. La obligación del caso positivo es: «Hay que examinar si la comprobación anterior sigue siendo transportable tras el cambio, aunque después se haya vuelto a la misma imagen.». En el negativo: «No hay objeción por cambio binario en ESTE intervalo cubierto; no se deduce ausencia de cambios de configuración u otras causas.». Ambas conservan los límites de la ficha y no emiten una actuación.

**Intento de partición/duplicación:** Se retiró una primera formulación como desigualdad actual frente a referencia: podía duplicar el complemento de P06. La historia de transición aporta función separable.

**Límite material:** No abarca todo cambio de configuración de D2. Un cambio de catálogo externo conserva su estatuto propio y no modifica Tri automáticamente.

**Fuentes/localizadores:** T001 §§2.2/2.3.4; T008; R025; S018. Los originales se identifican en 43/53 y los inventarios vinculados. Las fuentes profesionales justifican la necesidad y la semántica; los resultados de episodio sólo proceden de los testigos declarados.

**G5:** `PARAMETRO_ATOMICO_EN_PERFIL_DOCUMENTAL`. Identidad, único estado, U propia, consecuencia, función, independencia, ablación, partición, reproducción y procedencia constan individualmente en 49. Propiedad matricial: pendiente G6; adopción nominal de esta ficha: pendiente.

### P10 · Restauración desde estado anterior comunicada

**Identidad:** `PAR-CYB-RESTAURACION-PREVIA-COMUNICADA-001` v0.1. **Distinción:** `QCY-08-D3`. **Perfil:** `HISTORIA-RESTAURACION-PREVIA-0.1`.

> Se comunicó la terminación satisfactoria de una restauración cuyo punto de origen fue capturado antes de la instalación evaluada.

**Sujeto:** Activo, trabajo de restauración, punto de recuperación, ámbito restaurado e instalación; identidades enlazadas. **Horizonte:** Restauración posterior al fin de instalación y no posterior al corte; punto de recuperación anterior al inicio de instalación.

**G3 — observación:** Registro del trabajo y manifiesto del punto recuperado, con éxito, ámbito y orden acreditados. El nombre «backup antiguo» no prueba el orden.

| Estado | Contrato |
|---|---|
| 1 | Trabajo satisfactorio referido a punto anterior y completado en el intervalo. |
| 0 | Ningún trabajo que cumpla la proposición en registro de cobertura suficiente. |
| U y controles | Fecha/origen del punto no acreditado, cobertura parcial, orden incierto o conflicto. |

**G4 — conocimiento y consecuencia:** Suponer continuidad desde la instalación ignorando una restauración puede mantener un cierre sobre un estado que ya no corresponde. El defecto puede reaparecer si el ámbito restaurado repuso estado vulnerable. Punto anterior no significa necesariamente vulnerable ni restauración total. El exceso contrario también importa: Tratar cualquier restauración como pérdida probada del parche obliga a una corrección que puede no ser necesaria.

**Función separable:** Exigir revisión del alcance de evidencia que pueda haber sido sustituido por recuperación de estado previo.

**Variación independiente:** Una restauración de configuración puede conservar el mismo binario; una sustitución binaria puede ocurrir sin restauración. P09 y P10 no se deducen uno del otro.

**Ablación AB-L10-10:** se comparan mundos con el mismo resto semántico declarado y distinto estado del predicado. Se retiran el estado y toda pista lateral que lo recodifique. La obligación del caso positivo es: «Hay que revisar qué evidencia quedó sustituida dentro del ámbito restaurado; no se presume retorno a vulnerabilidad.». En el negativo: «No se introduce una objeción por restauración desde punto previo en ESTE intervalo cubierto; las otras causas se valoran aparte.». Ambas conservan los límites de la ficha y no emiten una actuación.

**Intento de partición/duplicación:** Origen y destino fijan qué suceso se pregunta; no se agrupan su éxito comunicado, integridad efectiva y aptitud de la recuperación. Sólo el primero se adjudica.

**Límite material:** No acredita integridad del backup, disponibilidad del servicio o ausencia de compromiso. Esas consecuencias necesitan otras preguntas.

**Fuentes/localizadores:** T001 §§2.3.2/2.3.4; R033 IV tema 7; S018. Los originales se identifican en 43/53 y los inventarios vinculados. Las fuentes profesionales justifican la necesidad y la semántica; los resultados de episodio sólo proceden de los testigos declarados.

**G5:** `PARAMETRO_ATOMICO_EN_PERFIL_DOCUMENTAL`. Identidad, único estado, U propia, consecuencia, función, independencia, ablación, partición, reproducción y procedencia constan individualmente en 49. Propiedad matricial: pendiente G6; adopción nominal de esta ficha: pendiente.

## 4. Contraste y adversarial

Se ejecutaron **127 testigos nuevos** del contrato documental mediante fórmulas del Excel. Sus entradas y esperados se fijaron antes de evaluar esas fórmulas. Se reejecutaron además los 28 del primer parámetro, cuyo contrato permanece intacto. No se suman casos y ablaciones como si fueran observaciones de campo.

Se ejecutaron nueve ablaciones, cada una con un oráculo profesional explícito de obligación/cautela del consejo; no basta cambiar una etiqueta «verdadero» por «falso». En cada par, un observador mutado que omite el parámetro pierde la obligación diferenciada. Se comprobó asimismo que alterar un esperado produce una discordancia y que restaurarlo devuelve cero. Son pruebas de sensibilidad del observador documental, no de un escáner de vulnerabilidades, capturador o ejecución SV.

Las proyecciones iguales de cada ablación **no son ejecuciones con identidad completa idéntica**: se ha retirado deliberadamente información semántica. No se atribuye con este ensayo una pérdida del Lenguaje, ni se afirma una segunda implementación semántica independiente. El registro de verificación conserva casos, salidas, pares y mutaciones.

La adversarial interna recoge veinte ataques en 51. Dos correcciones modificaron el contenido antes del cierre del dictamen:

1. Se rechazó tratar «reinicio del software realizado» como si terminación de la generación anterior y nueva ejecución útil fueran inseparables. P05 retiene sólo terminación; el resto queda pendiente.
2. Se rechazó definir P09 únicamente como desigualdad de la imagen actual frente a una referencia: podía duplicar el complemento de P06. P09 conserva la historia de cambios, incluido cambio y retorno.

Otros ataques impiden equiparar Fast Startup con reinicio íntegro, PID con generación, MODULEINFO con identidad de imagen, ausencia con no ocurrencia, retirada fallida con exitosa, fecha de backup con contenido vulnerable y criterio positivo con cierre universal. Se conserva como deuda material la adquisición/admisión productiva. No se presenta como auditoría externa ni como ausencia de deuda.

En la primera ejecución de ingeniería, el motor de fórmulas interpretó indebidamente un lexema de huella sólo numérico al aplicar funciones de texto. El escaneo de errores lo detectó. Se conservó el original textual y se corrigió la comprobación utilizando contexto textual explícito; la revisión final vuelve a contrastar tipos, ceros iniciales, fórmulas y resultados. El fallo del motor documental no se convirtió en valor U de la imagen ni en problema demostrado del Lenguaje SV.

## 5. Cobertura, dependencias y devolución al trabajo constitutivo

El registro tiene diez identidades únicas y **cero células, rutas o Frames**. El manifiesto técnico identifica archivos; el sustantivo gobierna alcance. Ninguno convierte el catálogo en agente ni atribuye aptitud operacional.

Las 31 distinciones de Q0 permanecen visibles una vez cada una. Hay diez enlaces a parámetros, de los que cinco se registran expresamente como cobertura parcial de su distinción; las otras adjudicaciones también están limitadas a su perfil. Las 21 distinciones sin parámetro enlazado continúan pendientes: este recuento no significa que sólo queden 21 problemas ni que toda distinción requiera un átomo.

Prioridades siguientes dentro del mismo universo: identidad/aplicabilidad y reglas de admisión de evidencia; criterios de comprobación con sensibilidad propia; cumplimiento íntegro del software y otros cambios; cobertura de instancias/dependencias; impactos, alternativas, ventana, autoridad y balance de coste/valor. Se resolverán según consecuencia de omitirlas, no por disponibilidad de una API. Las cardinalidades del catálogo editorial o de Inmunología no predicen el número de universos o matrices de Ciberseguridad.

La IA conserva su función de consejera: debe explicar qué conocimiento enlazó, qué evidencia utilizó, qué incertidumbre queda y qué consecuencia condiciona el consejo. El experto decide. Investigar fuentes nuevas para estas fichas no las adopta automáticamente para ejecución ni modifica el corte del conocimiento del agente. Una actualización exige evaluación y decisión humanas previas.

El Excel v0.5 sigue siendo el catálogo principal. No está cerrado, por lo que no se genera todavía la proyección textual normativa complementaria. Los JSON de casos y verificación son evidencia del ensayo, no sustitutos del catálogo.

## 6. Referencias directas

- [NIST SP 800-40 Rev.4, §§2.3.2–2.3.4](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-40r4.pdf): fases de aplicación, comprobación y seguimiento.
- [OperationResultCode](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/ne-wuapi-operationresultcode): resultado comunicado y éxito con errores.
- [Fast Startup y actualizaciones](https://learn.microsoft.com/en-us/troubleshoot/windows-client/setup-upgrade-and-drivers/updates-not-install-with-fast-startup): contraejemplo al apagado/encendido.
- [Restart Manager](https://learn.microsoft.com/en-us/windows/win32/rstmgr/about-restart-manager): procesos, archivos en uso y límites de autoridad/servicios críticos.
- [Orden de búsqueda DLL](https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order): resolución y coexistencia de módulos.
- [Historia de actualización](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/nn-wuapi-iupdatehistoryentry) y [UpdateOperation](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/ne-wuapi-updateoperation): identidad, operación y resultado separados.
- [GetModuleInformation](https://learn.microsoft.com/en-us/windows/win32/api/psapi/nf-psapi-getmoduleinformation) y [MODULEINFO](https://learn.microsoft.com/en-us/windows/win32/api/psapi/ns-psapi-moduleinfo): información devuelta y límites de identidad.

Las capturas conservan por separado fecha visible y metadato ms.date cuando difieren. Ninguna de esas fechas se confunde con una versión del sistema observado.
