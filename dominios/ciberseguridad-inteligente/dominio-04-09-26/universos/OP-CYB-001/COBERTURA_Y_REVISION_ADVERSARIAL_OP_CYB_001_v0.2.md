# Cobertura y revisión adversarial del primer universo

**OP-CYB-001, versión 0.2. 9 de septiembre de 2026.**

## 1. Criterio de cierre

La revisión no se limita a comprobar que exista una referencia para cada pregunta. Busca diferencias de estado, incertidumbre, función o consecuencia que quedarían ocultas. Cada candidato debe recibir resolución. El catálogo contiene 24 definiciones; los 36 candidatos siguientes no añaden identidades porque tienen otra función o porque su partición ya está representada. Esta revisión es interna y no se presenta como arbitraje externo.

## 2. Veinte ámbitos examinados

### A01. Correspondencia del caso

Activo, componente, revisión, arquitectura, episodio y vulnerabilidad. **Representación:** C01. La igualdad nominal no acredita identidad; las precondiciones de plataforma se resuelven antes de activar los parámetros. **Fundamento:** T001 §3.2; B03 §§3.3–3.6.

### A02. Autenticidad y custodia

Autoría, delegación, integridad, revocación, caducidad y adquisición. **Representación:** C02, C14. Una firma válida no implica autorización; una huella correcta no autentica al productor. Cada requisito se comprueba por separado. **Fundamento:** T001 §2.3.1; B03 §§3.7, 3.13, 3.15, 3.25.

### A03. Resultado de instalación

Intento individual, resultado terminal y errores parciales. **Representación:** P02, C03. Se conserva el resultado completo del emisor y la correspondencia con el elemento instalado. **Fundamento:** T004–T006.

### A04. Reinicio del sistema

Exigencia histórica, evento posterior y clase íntegra. **Representación:** P01, P03. La necesidad y su cumplimiento no se fusionan. **Fundamento:** T002; T007.

### A05. Reinicio de programas

Terminación, sustitución, inicialización y recursos compartidos. **Representación:** P04, P05, P11, P17, P20. La cadena completa impide aceptar la sola creación o terminación como reinicio suficiente. **Fundamento:** T009; T014–T016.

### A06. Estado de ejecutables

Artefacto almacenado, imagen utilizada y selección de carga. **Representación:** P06, P13, P22. Tres estados independientes, con perfil específico para bibliotecas, núcleo o firmware. **Fundamento:** T008; B02 §4; B03 §§3.10–3.13.

### A07. Configuración

Valor efectivo, persistente e historia de cambios. **Representación:** P12, P14, P16. Las claves se individualizan; la configuración no se reduce al archivo completo. **Fundamento:** B01 §§3.2–3.4; F018 §3.4.

### A08. Parche en ejecución

Habilitación, estado por tarea y dirección de transición. **Representación:** P18, P19, C05. Se distinguen los estados por tarea y se cubren las tareas pertinentes; -1 no se convierte en 0. **Fundamento:** B04 §§3–5.

### A09. Estado residual

Referencias antiguas y contenido de caché utilizable. **Representación:** P20, P21. Se sigue cada consumidor y recurso pertinente. La palabra caché no justifica una limpieza indiscriminada. **Fundamento:** T016; B05 §4; B11.

### A10. Escritura y diferimiento

Sincronización comunicada y operaciones de archivo pendientes. **Representación:** P13, P23, P24. Lectura, sincronización y programación diferida conservan evidencias separadas. **Fundamento:** B06; B07; B12.

### A11. Otros efectos exigidos

Configuración, despliegue, activación y adaptación del estado. **Representación:** P15 y registro de clases. No se admite una clase nueva por texto libre; cada efecto se asigna al estado que lo acredita. **Fundamento:** T001 §2.3.2; B05 §§2–4.

### A12. Corrección íntegra

Cambios necesarios, dependencias y criterio funcional de corrección. **Representación:** P07, C04, C06. Cada obligación de corrección se verifica; compilar o reconocer un fragmento no cierra el conjunto. **Fundamento:** B08 §1; B09 §1; F018 §4.3.

### A13. Alcance de observación

Permisos, sensibilidad, falso positivo y falso negativo. **Representación:** C02, C06. Casos favorables y desfavorables independientes del resultado esperado; límites de acceso explícitos. **Fundamento:** F018 §§4.3, 6.5, 7.3.

### A14. Instancias y dependencias

Réplicas, copias, huéspedes, anfitriones y componentes compartidos. **Representación:** C05 y usos independientes. Cada sujeto posee su propio estado; el recorrido termina al cubrir todas las relaciones pertinentes o declarar una frontera responsable. **Fundamento:** T001 §3.2; B01 §3.3.3.

### A15. Pérdida de vigencia

Retirada, cambio binario, cambio de clave y restauración. **Representación:** P08, P09, P10, P14, C07. El cambio y retorno se conserva; una modificación sólo afecta a la evidencia dependiente de ella. **Fundamento:** T001 §2.3.4; B01 §3.3.4.

### A16. Efecto funcional y datos

Disponibilidad, integridad, compatibilidad y funciones requeridas. **Representación:** P07 por criterio; C08. Los criterios se separan; una prueba de disponibilidad no sustituye una prueba de integridad. **Fundamento:** B01 §3.3.3; B10 §3.2.

### A17. Alternativas y recuperación

Completar, aplazar con medidas, sustituir, aislar o recuperar. **Representación:** C09; P07 por comprobación. Se comparan resultados y perjuicios; ninguna alternativa cambia el hecho de si la corrección está acreditada. **Fundamento:** T001 §§3.3–3.5; B10 §§3.4, 4.3.

### A18. Tiempo y autorización

Ventana, duración, dependencias de recuperación y permiso. **Representación:** C10, C11. Una ventana disponible no constituye autorización; un permiso vencido no se conserva como vigente. **Fundamento:** B01 §§3.3.1–3.3.2; B10 §3.2.

### A19. Proporcionalidad

Coste total, valor protegido, perjuicio de actuar y de omitir. **Representación:** C08, C12. Se conserva la incertidumbre económica y lo no monetizable; no se sustituye el valor del servicio por el precio del equipo. **Fundamento:** R035; T001 §3.1; B10 §3.2.

### A20. Explicación y gobierno

Fuentes, reglas, evidencia, incertidumbre, consecuencias y destinatario. **Representación:** C13, C14. El informe permite reconstruir el consejo; no se presenta como Frame SV antes de constituir su representación legítima. **Fundamento:** Acta del español; instrucción aprobada; contrato de atomicidad.

## 3. Registro cerrado de clases de acción

Las clases organizan obligaciones y pruebas; no son parámetros ni autorizaciones de ejecución. Si una actuación exige varios efectos independientes, conserva los usos de cada estado. Una nueva semántica no puede incorporarse por un campo libre.

| Clase | Acción | Obligación | Estados de cumplimiento |
| --- | --- | --- | --- |
| AC01 | Reinicio del sistema | P01 | P03; P06 cuando corresponda |
| AC02 | Reinicio de un programa | P04 | P05, P11, P17, P06, P20 y P07 por función exigida |
| AC03 | Modificación de configuración | P15 | P12, P16, P14; P07 por efecto requerido |
| AC04 | Sustitución o despliegue de artefacto | P15 | P13, P06, P22, P23; C05 para instancias |
| AC05 | Aplicación de parche durante la ejecución | P15 | P18, P19, P20, P21; P07 por condición correctora |
| AC06 | Operación diferida de archivo | P15 | P24, P13, P23 y la condición de ejecución pertinente |
| AC07 | Actualización de estado derivado o compartido | P15 | P20, P21 y P07 por cada invariante funcional |
| AC08 | Activación de imagen de firmware | P15 | P13, P22, P06; P07 por compatibilidad y efecto requeridos |


**AC01.** Un reinicio solicitado no es un reinicio completado.

**AC02.** No se exige detener consumidores ajenos al programa.

**AC03.** Una clave por estado y ámbito.

**AC04.** La carga y la durabilidad no se deducen de una ruta de archivo.

**AC05.** La cobertura de tareas y el estado compartido se comprueban separadamente.

**AC06.** Ausencia de pendiente no acredita que la operación terminase con éxito.

**AC07.** No se oculta una nueva clase de estado en un resultado global; las variables de configuración se asignan a P12/P16.

**AC08.** Perfil específico del dispositivo; una imagen descargada no acredita su activación.

## 4. Resolución de candidatos adicionales

### R01. Activo correctamente identificado

**Resolución:** Contexto. **Destino:** C01. Es la identidad que hace admisible el caso; su defecto no representa el estado de la corrección.

### R02. Actualización aplicable

**Resolución:** Control. **Destino:** C01. La conjunción de arquitectura, precursor, versión y condiciones se resuelve antes de activar; no se comprime en un átomo.

### R03. Firma válida

**Resolución:** Control. **Destino:** C02. La admisión distingue comprobación criptográfica, identidad del firmante y autorización.

### R04. Huella coincidente de evidencia

**Resolución:** Control. **Destino:** C02. Identifica bytes de prueba; no es el estado del activo ni autentica el productor.

### R05. Prueba procedente de autoridad válida

**Resolución:** Control. **Destino:** C02. Controla qué evidencia se admite y conserva su motivo de rechazo.

### R06. Referencia normativa vigente

**Resolución:** Control. **Destino:** C14. La revisión del conocimiento requiere decisión humana y no altera Tri.

### R07. Todos los archivos actualizados

**Resolución:** Composición. **Destino:** P13; C05. Cada archivo mantiene su estado; se exige cobertura del conjunto.

### R08. Todo el software reiniciado

**Resolución:** Composición. **Destino:** P04, P05, P11, P17, P20. Agrupa obligaciones e instancias independientes.

### R09. Proceso actualmente vivo

**Resolución:** Derivable en el perfil. **Destino:** P05, P11; historia de generación. Para una generación con nacimiento y terminación completamente conocidos, la vida al corte se deriva. Si falta historia, la proposición no adquiere evidencia nueva por cambiarle el nombre.

### R10. PID nuevo

**Resolución:** Observable. **Destino:** P11; T014. Un PID aislado no identifica una generación nueva.

### R11. Programa saludable

**Resolución:** Composición. **Destino:** P07 por función; C06. Disponibilidad, corrección funcional e integridad pueden variar independientemente.

### R12. Versión textual correcta

**Resolución:** Observable. **Destino:** P06, P13. Una etiqueta no sustituye la identidad y el método exigidos.

### R13. Firmware correcto

**Resolución:** Composición. **Destino:** P06, P13, P22, P07; C01. Almacenamiento, selección, utilización y corrección son diferentes.

### R14. Dirección de memoria reiniciada

**Resolución:** Observable. **Destino:** P20. El valor numérico de una dirección no acredita identidad, vigencia ni uso del recurso.

### R15. Caché completamente limpia

**Resolución:** Composición. **Destino:** P21; C05. La pertinencia se establece por entradas y consumidores; vacío no significa correcto.

### R16. Parche completo en todas las tareas

**Resolución:** Composición. **Destino:** P19; C05. Conjunción de estados por tarea, no parámetro adicional.

### R17. Transición terminada sin riesgo

**Resolución:** Composición. **Destino:** P19, P20; C06. Estado de transición y seguridad de la operación no se fusionan.

### R18. Valor -1 de patch_state

**Resolución:** Fuera del perfil. **Destino:** P19. Fuera de transición no se interpreta como ausencia de parche. Es un estado del mecanismo que cambia la activación del perfil.

### R19. Retirada y reversión equivalentes

**Resolución:** Desestimado. **Destino:** P08, P10, P09, P14. Los mecanismos e historias difieren; no se crea un átomo que los equipare.

### R20. Corrección íntegra de la vulnerabilidad

**Resolución:** Composición. **Destino:** C04, C05, C06; P07. Es el resultado profesional que se debe justificar; hacerlo átomo ocultaría sus requisitos.

### R21. Sin hallazgos de vulnerabilidad

**Resolución:** Resultado de prueba. **Destino:** P07; C06. Sólo tiene sentido con cobertura y sensibilidad; no acredita ausencia universal.

### R22. Conjunto de dependencias completo

**Resolución:** Control. **Destino:** C05. La cobertura debe acreditarse mediante inventario y fronteras, no por un booleano autodeclarado.

### R23. Observador suficientemente sensible

**Resolución:** Control. **Destino:** C06. Se demuestra por pruebas pertinentes; no se permite que el resultado se autentique a sí mismo.

### R24. Permiso para intervenir

**Resolución:** Control humano. **Destino:** C11. Se conserva el acto de autorización, su alcance y vigencia; la IA no crea esa autoridad.

### R25. Ventana suficiente

**Resolución:** Juicio y contexto. **Destino:** C10. Depende de tiempos, dependencias y recuperación; sus magnitudes permanecen separadas.

### R26. Coste proporcionado

**Resolución:** Juicio humano. **Destino:** C12. No se convierte una valoración multicriterio en un estado técnico ni en suma arbitraria.

### R27. Disponibilidad tras actualizar

**Resolución:** Resultado de prueba. **Destino:** P07 por criterio; C08. Se comprueba la función concreta y el horizonte; no se presume por inicialización.

### R28. Datos íntegros tras migrar

**Resolución:** Composición de criterios. **Destino:** P07 por invariante; AC07. Los invariantes se fijan antes de probar y se separan si generan consecuencias independientes.

### R29. Reversión segura garantizada

**Resolución:** Composición y referencia. **Destino:** C09; P07; C05. Requiere capacidad de recuperación y alcance propios; no es permiso ni resultado del cambio.

### R30. Durabilidad física garantizada

**Resolución:** Composición de garantías. **Destino:** P23; C02; C06. El retorno de una operación no acredita todos los supuestos del dispositivo y del modelo de fallo.

### R31. Sin operación pendiente, luego aplicada

**Resolución:** Desestimado. **Destino:** P24, P13. La cancelación ofrece un contraejemplo; ausencia de pendiente no implica éxito.

### R32. OT actualizado con reglas IT

**Resolución:** Fuera de alcance. **Destino:** CYO-14. El proceso físico y su autoridad exigen otro universo; la frontera se declara.

### R33. Modelo de IA robusto después de actualizar

**Resolución:** Fuera de alcance sustantivo. **Destino:** CYO-23; C09. OP-CYB-001 puede seguir su artefacto de software; robustez, sesgo y privacidad necesitan criterios del universo de IA.

### R34. Nuevo CVE obliga a cambiar automáticamente

**Resolución:** Desestimado. **Destino:** C14. La adquisición externa no modifica por sí sola el conocimiento admitido.

### R35. Puntuación única de seguridad

**Resolución:** Desestimado. **Destino:** C13. Ocultaría incertidumbres, condiciones y consecuencias no compensables.

### R36. Parámetro adicional para completar 25 posiciones

**Resolución:** Desestimado. **Destino:** Doctrina SV. La geometría no crea una distinción profesional; no se añade relleno.

## 5. Correspondencia con las 31 distinciones antecedentes

La identidad de las distinciones iniciales se conserva. Las nuevas definiciones profundizan los requisitos de cumplimiento y de estado, sin crear por ello una operación diferente. La columna siguiente identifica ámbitos completos de revisión, no una nueva causa de incertidumbre.

| Distinción | Necesidad | Representación concreta |
| --- | --- | --- |
| QCY-01-D1 | Identidad del activo | C01 |
| QCY-01-D2 | Componente y configuración | C01, C05; P06, P12, P13, P16 |
| QCY-01-D3 | Referencia de vulnerabilidad | C01, C14 |
| QCY-01-D4 | Aplicabilidad de la actualización | C01, C02 |
| QCY-02-D1 | Identidad del episodio | C01, C03, C07 |
| QCY-02-D2 | Integridad de la evidencia | C02 |
| QCY-02-D3 | Procedencia y admisión | C02, C11, C14 |
| QCY-03-D1 | Operación individual | C03 |
| QCY-03-D2 | Resultado terminal comunicado | P02; C03 |
| QCY-03-D3 | Errores asociados | C03; P07 por criterio afectado |
| QCY-04-D1 | Necesidad de reinicio del sistema | P01 |
| QCY-04-D2 | Reinicio íntegro realizado | P03 |
| QCY-04-D3 | Otros cambios requeridos | P04, P15; C04; AC01–AC08 |
| QCY-04-D4 | Cumplimiento de los cambios | P05, P06, P07, P11–P13, P16–P24; C04, C05 |
| QCY-05-D1 | Criterio de comprobación | C06 |
| QCY-05-D2 | Estado utilizado y estados relacionados | P06, P12, P13, P16–P24; C05, C07 |
| QCY-05-D3 | Resultado de la comprobación | P07; C06 |
| QCY-06-D1 | Servicio afectado | C05, C08 |
| QCY-06-D2 | Dependencias | C05; P20 por relación pertinente |
| QCY-06-D3 | Consecuencias de interrupción | C08, C10, C12 |
| QCY-07-D1 | Alternativas | C09 |
| QCY-07-D2 | Ventana temporal | C10 |
| QCY-07-D3 | Autoridad para actuar | C11 |
| QCY-07-D4 | Balance de coste y valor | C08, C12 |
| QCY-08-D1 | Retirada y reversión | P08; P06, P13, P18, P19 según mecanismo; C07 |
| QCY-08-D2 | Cambio posterior de componente | P09, P14; C07 |
| QCY-08-D3 | Restauración anterior | P10; C07, C09 |
| QCY-09-D1 | Cobertura de dependencias | C05 |
| QCY-09-D2 | Incertidumbres | U propia de cada parámetro; C02, C06, C13 |
| QCY-09-D3 | Justificación del consejo | C13, C14 |
| QCY-09-D4 | Destinatario responsable | C11, C13 |


## 5.1. Contratos revisados de contexto, evidencia y gobierno

Estos controles no son parámetros ocultos: se especifica qué verifican y qué contraejemplo impide darlos por satisfechos. Sus resultados se conservan separados.

### C01. Identidad y aplicabilidad

Identificar activo, componente, vulnerabilidad, actualización, episodio y horizonte. Resolver por separado las condiciones del aviso aplicable: plataforma, arquitectura, versión, precursor y configuración. Si falta una condición decisiva, la aplicabilidad queda sin resolver. Una exclusión exige evidencia de que la regla no corresponde al caso. **Contraejemplo:** Nombre coincidente en otro equipo; paquete para otra arquitectura; condición desconocida. **Fundamento:** T001 §3.2; B03 §§3.3–3.6.

### C02. Admisión de evidencia

Conservar original, origen, productor, método, versión, permisos de observación, ámbito, instante, precisión, normalización y cadena de custodia. Verificar separadamente integridad, autenticidad y autorización. Conservar magnitudes exactas antes de conversión. Un defecto de admisión no se transforma en un estado del activo. **Contraejemplo:** Huella rehecha sobre evidencia falsificada; firma válida de autor no autorizado; lector sin permisos; tipo cambiado. **Fundamento:** T001 §2.3.1; F018 §7.4; B03 §§3.13, 3.15, 3.25.

### C03. Correspondencia e interpretación de resultados

Vincular cada resultado al intento y elemento originales. Conservar códigos y errores completos. Un éxito con errores exige analizar qué efectos se produjeron; no prueba éxito íntegro ni ausencia total de modificación. El fallo de instalación es un hecho distinto del fallo al observarla. **Contraejemplo:** Índice de otra colección; éxito agregado con elemento fallido; confusión entre error de operación y de lectura. **Fundamento:** T004–T006.

### C04. Integridad de obligaciones

Enumerar las obligaciones específicas y sus efectos exigidos. Cada obligación se asigna a una de las ocho clases y a estados de cumplimiento individualizados. Una lista vacía exige evidencia de que no existen acciones adicionales. Ninguna obligación pertinente queda sustituida por un texto genérico de suficiencia. **Contraejemplo:** Sólo se comprueba un efecto de una acción compuesta; lista vacía sin fuente; nueva clase añadida durante el consejo. **Fundamento:** T001 §2.3.2; B01 §3.3.2.

### C05. Cobertura de sujetos y dependencias

Conservar conjuntos finitos de componentes, consumidores, instancias y relaciones pertinentes. Recorrer las dependencias hasta que no aparezcan sujetos nuevos, conservando ciclos sin repetir nodos. Cada frontera externa identifica responsable, contrato y evidencia o insuficiencia. Un límite de búsqueda alcanzado no prueba cobertura. **Contraejemplo:** Segunda réplica omitida; recurso compartido sin titular; ciclo de dependencias; inventario vacío injustificado. **Fundamento:** T001 §3.2; B01 §3.3.3; B04 §3.

### C06. Validez de la comprobación

Fijar antes de probar el criterio unitario, su referencia, condiciones, observador, alcance y tolerancias justificadas. Contrastar casos que deben distinguirse y registrar falsos positivos y negativos. El resultado de una prueba no acredita por sí mismo la sensibilidad de su observador. **Contraejemplo:** Escáner sin acceso; versión detectada sin corrección íntegra; dos herramientas con igual limitación; criterio elegido después del resultado. **Fundamento:** F018 §§4.3, 6.5, 7.3; B08 §1; B09 §1.

### C07. Vigencia y orden de los hechos

Relacionar cada evidencia con sus objetos, condiciones e intervalo. Examinar cambios posteriores sólo en las dependencias que afectan al criterio. Conservar cambio y retorno. Una nueva escritura puede dejar fuera de alcance una sincronización anterior. Una comprobación posterior pertinente puede renovar la evidencia sin borrar la historia. **Contraejemplo:** Extremos iguales con cambio intermedio; sincronización de otra escritura; restauración fuera del ámbito de la prueba. **Fundamento:** T001 §2.3.4; B01 §§3.3.4, 3.4; B06.

### C08. Impactos sobre servicios y datos

Identificar funciones protegidas y consecuencias de indisponibilidad, degradación, pérdida de integridad o exposición. Separar datos observados, hipótesis y valoración humana. Un objetivo de recuperación no es una recuperación demostrada. **Contraejemplo:** Equipo barato del que depende un servicio de alto valor; impacto no monetizado convertido en cero. **Fundamento:** B01 §3.3.3; B10 §3.2.

### C09. Comparación de alternativas

Describir completar, aplazar con medidas, sustituir, aislar o recuperar cuando sean pertinentes. Comparar el efecto corrector, los perjuicios y los requisitos de cada opción. Una medida compensatoria o una aceptación de riesgo no se presenta como corrección realizada. **Contraejemplo:** Aislamiento tratado como parche aplicado; restauración propuesta sin conocer su capacidad o alcance. **Fundamento:** T001 §§3.3–3.5; B10 §§3.4, 4.3.

### C10. Viabilidad temporal

Declarar ventana, duración de actuación, validación y recuperación, con dependencias y márgenes justificados. Las estimaciones desconocidas se mantienen abiertas. Este análisis sólo se activa si el consejo contempla una actuación pendiente. **Contraejemplo:** Duración de reinicio considerada sin tiempo de recuperación; ventana disponible confundida con permiso. **Fundamento:** B10 §3.2; B01 §3.3.2.

### C11. Autoridad concreta

Identificar responsable, acto autorizado, objeto, alcance temporal y restricciones. El consejo no crea autorización. La revocación o caducidad de un permiso impide tratarlo como vigente. La admisión del conocimiento corresponde a la autoridad humana competente del proyecto. **Contraejemplo:** Permiso para otro activo; autorización vencida; IA que se concede una excepción. **Fundamento:** B01 §§3.3.1–3.3.2; SV-IN y mandato humano posterior.

### C12. Proporcionalidad de coste y valor

Comparar costes totales pertinentes y valor del servicio protegido en un mismo horizonte y con unidades compatibles. Evitar doble cómputo y probabilidades inventadas. Conservar perjuicios no monetizados. Presentar al experto alternativas no ordenables con la evidencia disponible. **Contraejemplo:** Coste de seguridad comparado sólo con precio del equipo; suma de pérdidas que representan el mismo perjuicio. **Fundamento:** R035; T001 §3.1; B10 §3.2; principio del Director.

### C13. Dictamen explicado

Conservar la cadena entre pregunta, fuente, regla, observación, estado, relación, incertidumbre y consecuencia. Identificar el destinatario responsable y el alcance de suficiencia. Un fallo técnico produce registro técnico, sin salida alternativa del dominio. No denominar Frame a un informe sin representación SV constituida. **Contraejemplo:** Conclusión sin relación causal declarada; suma de estados heterogéneos; incertidumbre omitida. **Fundamento:** SV-IN; SV-AT.

### C14. Control de versiones del conocimiento

Fijar las fuentes y reglas antes de cada evaluación. Adquirir novedades en una actividad separada y someter su admisión a decisión humana. Los cambios de catálogos externos pueden exigir revisión, pero no sustituyen automáticamente el conocimiento ni añaden valores a Tri. **Contraejemplo:** Uso de latest; cambio de CVE equiparado a técnica retirada de otro catálogo; actualización silenciosa de criterio. **Fundamento:** SV-IN §§5.4–5.5; mandato del Director.

## 6. Objeciones y correcciones incorporadas

| Objeción | Corrección |
| --- | --- |
| La totalidad de preguntas etiquetadas demostraría agotamiento. | Se sustituyó por búsqueda de estados independientes en veinte ámbitos y por resolución de todos los candidatos. |
| La carencia de un capturador impediría acabar el inventario. | Se terminó el trabajo conceptual y se separó de la validación de una realización técnica. |
| P07 permitiría llamar comprobación a cualquier conocimiento desconocido. | El criterio debe estar fijado, ser unitario y pertenecer al registro; los estados propios de P16–P24 se explicitan. |
| P15 permitiría introducir cualquier actuación nueva. | Ocho clases declaradas, con obligaciones y estados de cumplimiento. No se admite ampliación semántica durante el consejo. |
| P13 probaría durabilidad física. | Se restringió su afirmación a identidad del artefacto observado; P23 y el modelo de almacenamiento tienen otro alcance. |
| patch_state=-1 se interpretaría como sin parche. | Se distingue ausencia de transición y se desactiva ese perfil; no se produce un 0 falso. |
| Una sincronización anterior seguiría siendo válida tras otra escritura. | Se exige la generación de escritura pertinente y se conserva el caso negativo. |
| Los parámetros se completarían hasta 25 para acomodar una matriz. | Candidato R36 desestimado. Se mantienen 24 definiciones derivadas de necesidad profesional. |
| Las estimaciones se presentarían como cantidades demostradas. | Se declaran escenarios de planificación, supuestos editables y ausencia de calibración estadística. |
| La decisión siguiente pertenecería automáticamente a otra unidad. | El acta reserva la elección al Director después de recibir el primer universo concluido. |


## 7. Resultado de los ensayos

El auxiliar documental ejecutó 64 casos sintéticos y detectó siete observadores deliberadamente defectuosos. Se comprueban estados, rechazos y separación de fallos. Los 24 argumentos de independencia constan en las fichas; no se confunden con ejecución sobre activos. El anexo reproducible conserva las entradas, los resultados esperados, las salidas y los identificadores de los casos refutadores.

## 8. Dictamen

El inventario paramétrico queda agotado en el perímetro profesional y en las clases semánticas de esta versión. No se mantiene una pregunta pertinente sin adjudicación ni se remite al Lenguaje la responsabilidad de buscar parámetros que corresponden al dominio. La validación operacional de capturadores y de la representación SV tiene otro objeto. El resultado queda expuesto a refutación mediante un contraejemplo profesional concreto y a actualización expresamente aprobada por el Director.
