# Marco técnico de responsabilidad, trazabilidad, reproducibilidad y criticidad de OP-IMM-001 / Q0 v0

**Versión:** 0.1  
**Fecha:** 3 de septiembre de 2026  
**Estatuto:** requisito técnico específico del universo; no implementado ni validado  
**Uso con datos reales:** prohibido  
**Consejo u opinión clínica automatizados:** prohibidos

## 1. Objeto y límites

Este documento fija las condiciones que tendría que satisfacer una implementación de `OP-IMM-001 / Q0 v0` para que sus transformaciones fueran atribuibles, auditables y exactamente reproducibles. No convierte el universo en producto sanitario, no declara conformidad normativa, no acredita seguridad o eficacia y no autoriza su uso asistencial.

El objeto clínico canónico es el [Expediente predecisional de información clínica pertinente, versión 1.1](../../universos-clinicos/01-evaluacion-predecisional-riesgo-infeccioso-antes-inmunosupresion-adultos/Expediente_predecisional_de_informacion_clinica_pertinente_antes_de_iniciar_tratamiento_inmunosupresor_en_adultos_v1.1_2026-09-03.md). Sus veintisiete parámetros constituyen un subconjunto formalizado. No cubren por sí solos el cribado infeccioso habitual previo a la inmunosupresión y no permiten estimar una probabilidad individual de infección.

En este documento, **debe** expresa una condición obligatoria; **no debe**, una prohibición; y **puede**, una facultad que no altera las obligaciones.

## 2. Principios no negociables

1. El inmunólogo conserva la soberanía clínica y la responsabilidad sobre la decisión individual.
2. Esa soberanía no absorbe la responsabilidad del fabricante, proveedor, responsable del despliegue, responsable del tratamiento de datos ni autor de una regla.
3. La IA no es sujeto de autoridad ni de responsabilidad. Su intervención no puede ocultar ni transferir la responsabilidad de personas y organizaciones identificables.
4. Toda salida normativa debe derivarse de reglas clínicas aprobadas, versionadas y ejecutadas de forma determinista.
5. Con la misma identidad de ejecución debe obtenerse exactamente la misma salida canónica, incluidos los textos de opinión o consejo si alguna versión futura los autorizase.
6. Un componente generativo, probabilístico o no explicable no puede integrar la cadena normativa que produzca estados, prioridades, vetos, opiniones o consejos clínicos.
7. La falta de una fuente, herramienta, conexión, dependencia o configuración no autoriza una aproximación, sustitución o respuesta alternativa: invalida la ejecución.
8. La trazabilidad debe permitir reconstruir la derivación completa sin recurrir a la memoria del modelo, a un chat ni a una explicación posterior.

## 3. Identidad completa de una ejecución

Dos ejecuciones son iguales sólo si coincide byte por byte la siguiente tupla:

`<Universo_ID_y_version, finalidad_prevista_version, entrada_canonica_hash, manifiesto_de_fuentes_hash, reglas_clinicas_hash, configuracion_hash, programa_ejecutable_hash, dependencias_hash, terminologias_y_versiones, jurisdiccion, instante_indice, estado_humano_autorizado_hash>`

Cada elemento debe resolverse antes de ejecutar. Un valor ausente, implícito, recuperado de memoria o determinado por la disponibilidad del momento produce `EJECUCION_TECNICA_NO_VALIDA`.

### 3.1 Entrada canónica

La entrada debe serializarse mediante un contrato publicado que establezca tipos, unidades, codificación, orden, tratamiento de valores nulos, zona horaria, precisión temporal, normalización Unicode y representación decimal. Se conservarán sus bytes y su resumen criptográfico. Dos historias semánticamente parecidas no se presumirán idénticas.

### 3.2 Salida canónica

La salida debe tener una serialización canónica única. Para una identidad de ejecución idéntica deben coincidir sus bytes y su resumen criptográfico. La igualdad aproximada, la equivalencia semántica o una redacción diferente no pasan.

Si alguna versión futura autoriza recomendaciones u opiniones, sus frases normativas deben proceder de plantillas cerradas, identificadas y versionadas. La redacción generativa libre queda prohibida en la salida autorizada.

### 3.3 Fuentes y tiempo

Sólo podrán consultarse fuentes incluidas en el manifiesto de la ejecución, mediante la versión, localizador y copia o resumen criptográfico autorizados. No se admite una actualización silenciosa ni sustituir una fuente inaccesible por otra semejante. Una nueva fuente o versión obliga a crear una configuración nueva y conserva reproducible la anterior.

## 4. Conducta ante fallos

Ante cualquier indisponibilidad o discordancia, la ejecución debe finalizar sin estado clínico, sin perfil, sin opinión y sin consejo. Su única salida será un parte técnico estructurado con `EJECUCION_TECNICA_NO_VALIDA`, la fase afectada, el componente exacto, la evidencia del fallo y la versión del entorno.

Quedan prohibidos:

- continuar con datos parciales no previstos;
- usar la memoria de un modelo o resultados de una ejecución distinta;
- cambiar de conector, fuente, terminología, modelo o versión sin constituir otra identidad de ejecución;
- presentar `0`, `1` o `U` clínicos cuando la ejecución técnica no fue válida;
- suavizar el fallo mediante prosa, estimaciones o advertencias añadidas al resultado.

Una copia local sólo es admisible cuando figura expresamente en el manifiesto y su resumen criptográfico coincide. En caso contrario no es una fuente válida.

## 5. Registro de trazabilidad

Cada ejecución válida o fallida debe producir un registro inmutable que contenga, como mínimo:

| Campo | Contenido obligatorio |
|---|---|
| Identidad | Identificador de ejecución, universo y versiones de la tupla completa |
| Entrada | Bytes canónicos, hash, procedencia, instante y autoridad que los suministra |
| Fuentes | Identificador, versión, localizador, fragmento utilizado, hash y fecha de vigencia |
| Reglas | Identificador, versión, autoridad clínica, operandos y hash del conjunto ejecutado |
| Configuración | Jurisdicción, centro, ventanas, tablas, instrumentos y hashes |
| Programa | Compilación, dependencias, sistema de ejecución y hashes verificables |
| Transformaciones | Secuencia ordenada de operaciones y estados intermedios clínicamente pertinentes |
| Parámetros | Para cada parámetro: entradas usadas, regla aplicada, resultado y justificación estructurada |
| Pérdidas | Detector activado, distinción no reconstruible y efecto sobre el cierre |
| Intervención humana | Persona y función autorizadas, decisión, motivo, fecha y firma o sello verificable |
| Fallos | Componente, fase, código, evidencia y confirmación de ausencia de salida clínica |
| Salida | Bytes canónicos, hash, plantilla textual y estado de autorización |

Una explicación redactada después de la ejecución no sustituye este registro. Debe ser posible reproducir el resultado a partir de los objetos identificados y comprobar cada paso sin consultar una conversación.

## 6. Responsabilidades

| Responsable | Obligaciones que no puede trasladar |
|---|---|
| Autoridad clínica del universo | Finalidad prevista, reglas, fuentes clínicas, criticidad, validación clínica y adjudicación de incertidumbres |
| Fabricante o proveedor técnico | Diseño, calidad del programa, verificación, ciberseguridad, gestión de riesgos, versiones, vigilancia y corrección de defectos |
| Organización sanitaria que despliega | Configuración local, integración, accesos, formación, seguimiento, continuidad y respuesta ante incidentes |
| Responsable y encargado del tratamiento | Licitud, finalidad, minimización, seguridad, conservación, derechos y demás obligaciones de protección de datos |
| Profesional responsable del paciente | Interpretación del caso, comprobación de suficiencia y decisión asistencial final |
| Desarrollador | Implementación fiel y prueba técnica; no puede inventar reglas, prioridades ni equivalencias clínicas |

La aceptación humana de una salida no sanea un cálculo opaco, una configuración incompleta o una ejecución técnicamente inválida.

## 7. Admisibilidad de IA y programas

Para formar parte de la cadena normativa, un componente debe:

- ejecutar una especificación cerrada y versionada;
- exponer todas las entradas, reglas, transformaciones y estados intermedios pertinentes;
- permitir reproducción independiente exacta;
- producir una salida canónica invariable;
- fallar de forma cerrada;
- superar las pruebas y revisiones aplicables al riesgo del universo.

Un modelo generativo puede, en una fase separada y no normativa, proponer indicios para revisión. Esos indicios deben quedar en cuarentena, no pueden modificar una salida y sólo se incorporarán mediante una nueva regla aprobada y versionada. Si el modelo decide qué fuente usar, completa un dato, pondera una omisión, redacta consejo libre o cambia una salida, el sistema es `NO_APTO` para esa función.

## 8. Pérdida de conocimiento y criticidad

### 8.1 Distinción necesaria

La **consecuencia de representación** expresa qué distinción deja de poder reconstruirse cuando falta o se interpreta mal un parámetro. Es estable y detectable. La **criticidad clínica** expresa la importancia de esa pérdida en un episodio concreto; depende de reglas contextuales y de autoridad clínica.

No se permite convertir automáticamente una pérdida en daño, diagnóstico o recomendación. Tampoco se permite tratar todos los valores indeterminados como equivalentes. Mientras no exista una regla de criticidad autorizada para el episodio, el sistema debe conservar la pérdida y bloquear cualquier sello que requiera haberla resuelto; no puede inventar su importancia.

### 8.2 Registro por parámetro

| Parámetro | Distinción que se pierde si falta o se interpreta indebidamente | Detector mínimo | Estado y efecto actual |
|---|---|---|---|
| Inicio previsto de inmunosupresión | Momento índice y vigencia de los antecedentes | Fecha ausente, ambigua o posterior al cierre | Criticidad contextual pendiente; no se cierra un perfil temporal sin momento índice |
| Diagnóstico de base | Relación entre la evaluación y la indicación clínica documentada | Diagnóstico no trazable o mera inferencia desde tratamiento | Exige revisión; no diagnosticar por sustitución |
| Responsable del episodio | Autoridad responsable de integrar y adjudicar el perfil | Responsable ausente o no vigente | Impide el cierre atribuible del perfil |
| Participación de Inmunología | Existencia y alcance de intervención especializada | Consulta o informe no identificado | Se conserva como pérdida; no se presume participación |
| Protocolo local aplicable | Regla jurisdiccional y organizativa vigente | Protocolo ausente, incompatible o sin versión | Impide aplicar reglas que dependan de él |
| Restricción de ejecución | Diferencia entre una carencia clínica y una imposibilidad técnica | Dependencia, acceso o recurso no disponible | `EJECUCION_TECNICA_NO_VALIDA`; ninguna salida clínica |
| Glucocorticoide sistémico previsto | Activación de cuestiones específicas de exposición a glucocorticoides | Plan incompleto o clasificación no versionada | Contexto de dosis, duración y equivalencia aún no constituido; no inferir riesgo |
| Déficit cuantitativo de IgG | Estado cuantitativo humoral respecto del intervalo aplicable | Medición, unidad, método o intervalo incompatibles | `U`; criticidad contextual pendiente |
| Ausencia anatómica del bazo | Anatomía esplénica, distinta de función | Ausencia de documentación anatómica suficiente | `U`; no inferir función ni riesgo |
| Déficit cuantitativo de neutrófilos | Estado del recuento absoluto respecto del intervalo aplicable | Recuento, unidad, método o intervalo incompatibles | `U`; criticidad contextual pendiente |
| Dispositivo intravascular | Presencia de una vía intravascular vigente | Inventario incompleto o vigencia incierta | `U`; presencia no equivale a infección |
| Implante | Presencia de material implantado vigente | Inventario incompleto o identidad incierta | `U`; no se confunde con dispositivo intravascular |
| Ingreso atribuido a infección | Gravedad histórica vinculada causalmente a un episodio infeccioso | Coincidencia temporal sin atribución explícita | `U`; no fabricar causalidad |
| Soporte orgánico atribuido a infección | Repercusión orgánica atribuida, separada del ingreso | UCI, monitorización o gravedad sin vínculo explícito | `U`; no equiparar estancia y soporte |
| Infección oportunista documentada | Clasificación previa de oportunismo con contexto y versión | Etiqueta libre, lista universal o clasificación sin versión | Configuración pendiente; resolución automática prohibida |
| Colonización por microorganismo resistente | Colonización, organismo, resistencia y vigencia sin confundir infección | Tabla o ventana ausente; cobertura de cribado insuficiente | Configuración pendiente; resolución automática prohibida |
| Encuentro sanitario agudo reciente | Exposición sanitaria reciente dentro de una ventana definida | Ventana o encuentro no trazables | Sin ventana versionada, `U` |
| Procedimiento invasivo reciente | Exposición invasiva reciente dentro de una ventana definida | Ventana, procedimiento o fecha no trazables | Sin ventana versionada, `U` |
| Diabetes mellitus activa | Diagnóstico activo documentado, no una cifra aislada | Código histórico o dato metabólico sin vigencia clínica | `U`; no diagnosticar diabetes |
| Insuficiencia cardiaca activa | Diagnóstico activo documentado y vigente | Código o síntoma aislado | `U`; no inferir desde tratamiento o disnea |
| Enfermedad renal crónica activa | Diagnóstico renal crónico documentado | eGFR aislado o episodio agudo | `U`; se mantiene separada de tratamiento renal sustitutivo |
| Tratamiento renal sustitutivo activo | Terapia vigente, distinta del diagnóstico renal | Procedimiento histórico sin vigencia | `U`; evitar doble interpretación causal |
| Bronquiectasias activas | Diagnóstico estructural pulmonar activo | Síntoma, cultivo o imagen no adjudicados | `U`; no diagnosticar desde indicios |
| Soporte respiratorio activo | Modalidad de soporte vigente | Oxígeno puntual o antecedente sin vigencia | `U`; no inferir enfermedad causal |
| Cirrosis activa | Diagnóstico hepático activo documentado | Analítica o código aislados | `U`; no diagnosticar cirrosis |
| Malnutrición por evaluación diagnóstica | Resultado de un instrumento diagnóstico completo y versionado | Cribado, IMC aislado o instrumento incompleto | Configuración pendiente; resolución automática prohibida |
| Fragilidad por instrumento | Resultado de un instrumento de fragilidad completo y versionado | Impresión clínica libre o escala sin versión | Configuración pendiente; resolución automática prohibida |

Los nombres completos y las definiciones clínicas se encuentran en el expediente clínico canónico. Esta tabla no los sustituye. No contiene todavía reglas que permitan graduar la criticidad clínica de cada pérdida según el episodio: inventarlas o trasladarlas desde otro universo está prohibido.

### 8.3 Efecto sobre el cierre

Todo parámetro indeterminado debe generar un registro de pérdida con causa y evidencia faltante. Si una salida requiere esa distinción, el cierre queda bloqueado hasta adjudicación humana autorizada o nueva evidencia. Sólo una regla clínica versionada puede permitir que una indeterminación no bloquee una salida determinada; la decisión y su motivo deben quedar en la traza.

## 9. Normas y disposiciones: mapa de aplicabilidad, no declaración de conformidad

| Referencia | Materia que deberá evaluarse | Estado en esta versión |
|---|---|---|
| ISO/IEC 27001 | Sistema de gestión de seguridad de la información | `APLICABLE_PENDIENTE`; no certificado ni evaluado |
| ISO 13485 | Sistema de gestión de calidad de productos sanitarios, si la finalidad prevista lo sitúa en ese régimen | `APLICABLE_PENDIENTE_DE_CLASIFICACION` |
| ISO 14971 | Gestión de riesgos de producto sanitario | `APLICABLE_PENDIENTE_DE_CLASIFICACION` |
| IEC 62304 | Ciclo de vida del programa de producto sanitario | `APLICABLE_PENDIENTE_DE_CLASIFICACION` |
| IEC 81001-5-1 | Seguridad del ciclo de vida del programa sanitario | `APLICABLE_PENDIENTE` |
| ISO/IEC 42001 | Sistema de gestión de inteligencia artificial | `APLICABLE_PENDIENTE`; no sustituye validación clínica |
| Reglamento (UE) 2017/745 | Calificación y obligaciones de producto sanitario | `APLICABLE_PENDIENTE_DE_FINALIDAD_Y_CLASIFICACION` |
| Reglamento (UE) 2024/1689 | Obligaciones aplicables al sistema de IA | `APLICABLE_PENDIENTE_DE_CLASIFICACION` |
| Reglamento (UE) 2016/679 y Ley 41/2002 | Datos de salud, historia clínica y responsabilidades | `APLICABLE_PENDIENTE_DE_DESPLIEGUE` |

La referencia oral a «ISO 2071» no se incorpora como requisito: corresponde a una norma retirada sobre óxido de aluminio y cinc y no guarda relación demostrada con este objeto. Si se pretendía otra norma, deberá identificarse por su designación exacta antes de aplicarla.

Cumplir una norma de gestión o seguridad no demuestra validez clínica, utilidad, calibración, ausencia de sesgo ni seguridad asistencial. Ninguna conformidad se presume por haber citado la norma.

## 10. Verificación y aceptación técnica

Antes de considerar apta una implementación deberán existir, al menos:

1. especificación ejecutable y revisada de cada regla;
2. corpus de conformidad con casos positivos, negativos, indeterminados, límites y fallos;
3. prueba independiente de serialización canónica;
4. repetición en entornos controlados con igualdad exacta de bytes;
5. pruebas de propiedades e invariantes sobre todo el dominio de entrada declarado o demostración formal cuando el espacio sea finito y enumerable;
6. prueba de que toda dependencia ausente conduce exclusivamente a ejecución inválida;
7. trazas reconstruibles y verificadas por un auditor ajeno al equipo de desarrollo;
8. gestión de riesgos, ciberseguridad, cambios e incidentes proporcional a la finalidad y clasificación aplicables;
9. validación clínica prospectiva y autorización independiente del desarrollo técnico.

Cualquier divergencia ante una identidad de ejecución igual es un fallo bloqueante. Un porcentaje alto de coincidencia no compensa una sola divergencia normativa.

## 11. Cambios, versiones y conservación

Todo cambio material en fuente, regla, configuración, terminología, jurisdicción, finalidad, población, programa, dependencia o plantilla crea una identidad nueva. Las ejecuciones anteriores, sus objetos y sus hashes deben conservarse reproducibles. Quedan prohibidos la actualización silenciosa, el reemplazo retrospectivo y la reinterpretación de una salida antigua con reglas nuevas.

La reutilización en otro universo exige evaluar de nuevo la aplicabilidad. Un módulo técnicamente idéntico puede tener criticidad, pruebas y condiciones de aceptación distintas.

## 12. Estado de OP-IMM-001 en esta fecha

| Capacidad | Estado |
|---|---|
| Subconjunto clínico de 27 tipos formalizados | `APLICABLE_Y_DEMOSTRADO` como constitución documental |
| Cobertura completa del cribado preinmunosupresión | `APLICABLE_PENDIENTE`; prohibido afirmar completitud |
| Reglas de OI, MDRO, malnutrición y fragilidad | `APLICABLE_PENDIENTE`; salida automática prohibida |
| Reglas contextuales de criticidad por parámetro | `APLICABLE_PENDIENTE`; no constituidas |
| Programa determinista conforme a este documento | `APLICABLE_PENDIENTE`; no existe prueba de implementación |
| Reproducibilidad exacta independiente | `APLICABLE_PENDIENTE` |
| Seguridad, calidad y conformidad regulatoria | `APLICABLE_PENDIENTE_DE_CLASIFICACION_Y_EVIDENCIA` |
| Validación clínica | `APLICABLE_PENDIENTE` |
| Uso con datos de pacientes | `PROHIBIDO` |
| Consejo u opinión clínica automatizados | `PROHIBIDO` |

## 13. Resultado de la adversarial de garantía y rumbo

El marco fue sometido, antes de su creación, a ataques de herencia indebida, duplicación, ambigüedad de identidad, fallos de disponibilidad, traslado de responsabilidad, certificación aparente, variabilidad generativa, actualización silenciosa, criticidad aplicada por analogía, cobertura clínica exagerada, privacidad y burocracia recursiva.

**Resultado: PASA CON CONDICIONES VINCULANTES.** Las condiciones están incorporadas como prohibiciones y pruebas en este documento. El rumbo es adecuado porque la nueva carpeta no añade una capa administrativa general: adjudica, universo por universo, quién responde, qué debe ser reproducible, qué pérdida se detecta y cuándo una ejecución no existe clínicamente. No autoriza la implementación ni el uso asistencial; permite iniciar el trabajo técnico controlado de `OP-IMM-001` sin atribuirle capacidades todavía no demostradas.
