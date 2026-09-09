# Acta de continuidad y relevo de OP-CYB-001 al Lenguaje SV

**Fecha:** 9 de septiembre de 2026.  
**Emisor:** unidad de Ciberseguridad inteligente, SVperitus-dataset, rama dominio-ciberseguridad-inteligente.  
**Destinatario:** unidad del Lenguaje de computación SV.  
**Estado:** relevo documental autorizado por el Director; contraste técnico receptor pendiente de ejecución.  
**Autoría y dirección:** Juan Antonio Lloret Egea. ORCID: 0000-0002-6634-3351.  
**Elaboración documental asistida:** Watson, bajo dirección y aprobación expresa del autor.  
**Institución:** ITVIA — IA eñ™. ISSN: 2695-6411. Licencia: CC BY-NC-ND 4.0.  
**Registro local:** SVP-ACT-2026-009; SVP-H-013.

## 1. Mandato y producto de relevo

El Director aprueba la tarea realizada, ordena consolidar el primer universo y dispone esta entrega para que el Lenguaje contraste sus capacidades frente al dominio de ciberseguridad inteligente. La publicación de esta acta y de la [consolidación en Calidad](../../../../../docs/calidad/ACTA_CONSOLIDACION_PRIMER_UNIVERSO_CIBERSEGURIDAD_INTELIGENTE_2026_09_09.md) está expresamente autorizada por trazabilidad y continuidad. Esta autorización se refiere a estas dos piezas; no aprueba anticipadamente futuras actas.

Se entrega **OP-CYB-001: evidencia y legitimidad de la corrección de una vulnerabilidad mediante actualización**, con 32 definiciones paramétricas, 17 controles, 18 elementos del estado de partida y nueve clases documentales de relación. Se entregan también el fundamento curricular, las fuentes, la justificación individual, los resultados de revisión y los requisitos antiguos y ampliados que siguen siendo pertinentes.

El siguiente trabajo es la recepción y el contraste del Lenguaje con este universo. Las condiciones de elección entre uno y dos universos de los documentos antecedentes quedan resueltas por la decisión humana presente. No se pide al receptor ratificar la existencia del universo, elegir de nuevo su currículo o constituir otro antes de estudiar éste. Una carencia concreta de definición profesional podrá motivar un retorno acotado; una limitación de representación no autoriza recortar el caso para acomodarlo al Lenguaje.

La entrega está publicada en la sede emisora para su incorporación trazada por la unidad receptora. La publicación no se presenta como recepción ya registrada en el repositorio del Lenguaje ni como ejecución de sus pruebas. Tampoco declara completado favorablemente un contraste I/J de la semántica o de la IR que todavía no se ha ejecutado en ese alcance.

## 2. Cortes, versiones y precedencia

| Referencia | Corte y significado |
| --- | --- |
| Universo aprobado | SVperitus-dataset, dominio-ciberseguridad-inteligente, `b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89`. |
| Libro principal | [catálogo curricular Excel v0.10](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/catalogo-profesional/CATALOGO_CURRICULAR_CIBERSEGURIDAD_v0.10.xlsx), SHA-256 `76166a77373e7df2c23bfe5a6fe17bf3cc305305cce629e43da720d656d0bd45`. Cerrado e inalterado por este relevo. |
| Lenguaje de referencia | SV-lenguaje-de-computacion, main `66967a80a40f4e2781ef983bd725690db54c25c5`. |
| Contenido técnico recibido del Lenguaje | `ab61d9bb7a2002d3a4a389e292c2a9b0a850d264`; integración y entrega establecidas por RETP-105. |
| Versiones formales que se contrastan | [Gramática canónica 0.2](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/66967a80a40f4e2781ef983bd725690db54c25c5/GRAMATICA_SUPERFICIAL_MINIMA_SV_v0_2.md), [IR canónica 0.3](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/66967a80a40f4e2781ef983bd725690db54c25c5/IR_CANONICA_BIENFORMACION_SV_v0_3.md), perfiles fuente SVP-ES y SVP-EN, semántica única del Lenguaje y contratos vigentes identificados. |
| Gobierno técnico receptor | [Pilares y restricciones de diseño](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/66967a80a40f4e2781ef983bd725690db54c25c5/docs/calidad/PILARES_Y_RESTRICCIONES_DE_DISENO_DEL_LENGUAJE_DE_COMPUTACION_SV_2026_09_05.md); [acta técnica de perfiles, contratos y ensamblaje](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/66967a80a40f4e2781ef983bd725690db54c25c5/docs/calidad/ACTA_TECNICA_DE_PERFILES_CONTRATOS_Y_ENSAMBLAJE_DEL_LENGUAJE_SV_2026_09_06.md); [secuencia rectora, §§12–17 y relevos posteriores](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/66967a80a40f4e2781ef983bd725690db54c25c5/docs/dominios/inmunologia/ACTA_DE_CONFORMIDAD_DE_TRANSICION_SECUENCIAL_DESDE_OP-IMM-001_AL_LENGUAJE_SV_2026_09_03.md); [sucesión RETP-105 y deuda viva](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/66967a80a40f4e2781ef983bd725690db54c25c5/docs/calidad/REGISTRO_DEUDA_VIVA_DEL_FRENTE_FINAL_DEL_LENGUAJE_SV.md#relevo-retp-105). |

La precisión de versiones es necesaria: los documentos consultados asignan 0.2 a la gramática y 0.3 a la IR; describen una semántica única, sin una etiqueta autónoma «semántica 0.2». El mandato de someter a presión la semántica se conserva íntegramente: se examinará el significado y comportamiento exigidos por sus normas, además de la aceptación sintáctica y la estructura emitida. No basta con que una fuente compile.

El receptor identificará su corte efectivo si main avanza. Mantendrá el universo aprobado como referencia inmutable y explicará el incremento del Lenguaje que vaya a ensayar. Los estados antiguos de los documentos de secuencia se leen con sus sucesiones; RETP-105 gobierna la oferta recibida y las nuevas actas gobiernan este relevo. Ninguna mención histórica a una decisión todavía pendiente revoca la autorización humana presente.

## 3. Constitución profesional que debe conservarse

La pregunta profesional es qué permite sostener la corrección de una vulnerabilidad por actualización de un activo y qué legitimidad, límites y tareas pendientes acompañan a esa conclusión. Se evalúan un episodio y sus sujetos, con referencia, evidencia, regla, dependencias y horizonte identificados. La salida es consejo explicado al experto, quien mantiene la decisión dentro de sus competencias.

El inventario diferencia necesidad histórica, ejecución comunicada, estado utilizado, estado persistente, efectos por consumidor, comprobación, cambios posteriores y legitimidad. La arquitectura de hardware y software entra por sus efectos sobre la misma operación, con perfiles concretos; no se considera universal un método Win32 ni se traslada a Linux el contrato de un emisor distinto.

Los 32 parámetros están enumerados en la consolidación y definidos en las fichas enlazadas. Los controles y relaciones completan premisas necesarias del consejo: identidad y aplicabilidad, admisión, cobertura, criterio sensible, orden temporal, impactos, alternativas, autorización, coste y valor, protección de datos y continuidad. El estado inicial observado no sustituye a la referencia aprobada ni reconstruye la historia ausente.

La fuente educativa es España/URJC 2026–2027, con complementos delimitados de UNSW, Warwick, Guelph y Carnegie Mellon y contrastes profesionales adicionales. La justificación no descansa en contar controles o vulnerabilidades: enlaza conocimiento previo, error de razonamiento, proposición discriminante, evidencia y consecuencia. La IA no aprende nuevas reglas durante la evaluación ni actualiza el dominio por iniciativa propia.

El conocimiento sobre una tecnología y el soporte tecnológico utilizado para ejecutar el consejo son objetos diferentes. Un agente tampoco se identifica con su dominio. El catálogo no constituye por sí solo capacidades, permisos ni cobertura de un futuro agente.

## 4. Paquete de lectura y prueba

| Pieza | Uso imprescindible para el receptor |
| --- | --- |
| [Consolidación en Calidad](../../../../../docs/calidad/ACTA_CONSOLIDACION_PRIMER_UNIVERSO_CIBERSEGURIDAD_INTELIGENTE_2026_09_09.md) | Decisión humana, 32 definiciones, alcance, resultados, estimaciones y bibliografía de orientación. |
| [catálogo curricular Excel v0.10](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/catalogo-profesional/CATALOGO_CURRICULAR_CIBERSEGURIDAD_v0.10.xlsx) | Registro principal; conserva fuentes educativas y revisiones. Hoja 67_Parametros: P01–P24; 68_Consecuencias: consecuencias; 74_Ampliacion_atomica: P25–P32; hojas 81–84: partida, justificación, contraste y bibliografía. Los nombres de hoja y sus encabezados delimitan los contenidos. |
| [catálogo atómico 0.2](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/universos/OP-CYB-001/CATALOGO_ATOMICO_OP_CYB_001_v0.2.md) y [ampliación atómica 0.3](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/universos/OP-CYB-001/AMPLIACION_ATOMICA_Y_COBERTURA_OP_CYB_001_v0.3.md) | Proposiciones, sujetos, condiciones de 1/0/U, perfiles, fuentes, independencia y consecuencias. Deben leerse conjuntamente para obtener las 32 definiciones. |
| [expediente predecisional de partida y continuidad, revisión 0.4](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/universos/OP-CYB-001/EXPEDIENTE_PREDECISIONAL_ESTADO_DE_PARTIDA_Y_CONTINUIDAD_OP_CYB_001_v0.4.md) | EP01–EP18, C17 y las nueve relaciones: antecedente, orden, derivación, causa, corrección, custodia, designación, aceptación y revocación o sustitución. |
| [justificación científica individual, revisión 0.4](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/universos/OP-CYB-001/JUSTIFICACION_CIENTIFICA_DE_LA_SELECCION_PARAMETRICA_OP_CYB_001_v0.4.md) | Razón de cada selección, alternativas y límites de las fuentes. |
| [dictamen antecedente 0.1, apartado 8](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/universos/OP-CYB-001/DICTAMEN_TERMINACION_DOCUMENTAL_OP_CYB_001_v0.1.md) | REQ-CYB-001–009 y ensayo nominal anterior. Su recuento de quince y sus decisiones pendientes son históricos. |
| [estimación y contraste con el Lenguaje, revisión 0.3](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/universos/OP-CYB-001/ESTIMACION_Y_CONTRASTE_CON_LENGUAJE_v0.3.md) | RS01–RS08, producto profesional de cada escenario y presupuestos de parámetros. |
| [adversarial y solicitud de valoración, revisión 0.4](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/universos/OP-CYB-001/ADVERSARIAL_Y_SOLICITUD_DE_VALORACION_OP_CYB_001_v0.4.md) | RS09–RS12, HC01–HC07, 32 casos y ocho pares de continuidad. |
| [revisión adversarial de identidad, autoridad y datos 0.3](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/universos/OP-CYB-001/REVISION_ADVERSARIAL_IDENTIDAD_AUTORIDAD_Y_DATOS_OP_CYB_001_v0.3.md) | Presión regulada previa, 46 casos, once modificaciones del observador y diez pares documentales. |
| [anexo de revisión regulada](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/watson-biblioteca-ciber/ANEXO_PRESION_REGULADA_OP_CYB_001_v0.3.zip) y [anexo de continuidad](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/watson-biblioteca-ciber/ANEXO_CONTINUIDAD_OP_CYB_001_v0.4.zip) | Datos sintéticos, oráculos, resultados, inventarios y reproducción auxiliar. El segundo incluye las 32 definiciones y los 17 controles completos. |
| [manifiesto 0.3](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/watson-biblioteca-ciber/MANIFIESTO_ARCHIVOS_PRESION_REGULADA_v0.3.json) y [manifiesto 0.4](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/watson-biblioteca-ciber/MANIFIESTO_ARCHIVOS_CONTINUIDAD_v0.4.json) | Identidad de las piezas recibidas; cada manifiesto conserva su propio alcance. |
| [recepción de fila 7](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/watson-biblioteca-ciber/RECEPCION_FILA7.json) | Identificación y custodia de la oferta representacional que recibió Ciberseguridad. |

Las hojas del libro son localizadores documentales, no posiciones celulares. Los JSON de los anexos son proyecciones y datos auxiliares; su lectura no restablece el compilador Python retirado ni los convierte en una segunda realización soberana. Se reutilizarán los oráculos y datos existentes; una adaptación necesaria conservará los originales y una correspondencia explícita.

## 5. Correspondencia entre requisitos antiguos y actuales

REQ-CYB-001–009 son antecedentes técnicos que mantienen necesidades pertinentes. RS01–RS12 desarrollan especialmente identidad, gobierno, datos y continuidad. Los 21 identificadores no representan 21 capacidades disjuntas. Esta tabla conserva los nueve antecedentes y explicita sus correspondencias; no modifica sus identidades ni atribuye actualidad a los resultados históricos de su corte.

| Antecedente | Necesidad preservada | Correspondencia y precisión actual |
| --- | --- | --- |
| REQ-CYB-001 | Identidad y evidencia admitida | RS01, RS04, RS06 y RS09; conservar procedencia, original y admisión con objetos exactos. |
| REQ-CYB-002 | Estados independientes por sujeto y uso | RS07 y RS12; comprobar además la independencia de instancias y criterios mediante las ligaduras recibidas. |
| REQ-CYB-003 | Observación y transducción gobernadas | RS06; contrato K1-T y separación entre captura, admisión y Tri. |
| REQ-CYB-004 | Historia y vigencia de la evidencia | RS03, RS09, RS10 y RS12; conservar cambios intermedios, antecedentes y dependencias. |
| REQ-CYB-005 | Comprobación cualificada y sensibilidad | RS06 y RS12; condición propia del criterio y observador, no absorbida por la igualdad de bytes. |
| REQ-CYB-006 | Cobertura finita | RS07, RS09 y RS12; conjuntos y fronteras explícitos, terminación y justificación del vacío. |
| REQ-CYB-007 | Consejo y autoridad separados | RS02, RS05, RS08 y RS11; conservar impactos, alternativas, viabilidad y proporcionalidad. |
| REQ-CYB-008 | Magnitudes exactas y tipos | Transversal a RS03, RS06, RS09 y RS12; obligación propia de conservar literal, tipo, unidad, rango y exactitud. |
| REQ-CYB-009 | Justificación reconstruible y Frame legítimo | RS08, RS10 y RS11; significado, U, horizonte, consecuencia, destinatario y arquitectura cuando proceda. |

La independencia de instancias, la sensibilidad del criterio y la exactitud numérica requieren comprobaciones propias incluso cuando una fila RS tenga referencias correctas. Deben conservarse los bytes originales antes de cualquier conversión. Las restricciones del lector documental de números no se presentan como límite universal de Nat ni de todas las magnitudes del Lenguaje. Una conversión previa a coma flotante no puede usarse para reconstruir después una magnitud exacta.

## 6. Presión concreta sobre semántica y representación

| Requisito | Distinción profesional | Referentes del universo | Contraste solicitado |
| --- | --- | --- | --- |
| RS01 | Atribución de acto, sesión y principal | P25; C02/C11 | Recuperar los objetos y su vínculo; impedir que un nombre o resultado técnico atribuya identidad o responsabilidad. |
| RS02 | Autoridad y delegación limitada | P26/P27; C11 | Distinguir raíz competente, sujeto representado, actor, destinatario, recurso y finalidad; una referencia íntegra no otorga facultades. |
| RS03 | Tiempo, revocación y antecedentes | P28–P30; C07 | Conservar intervalos, precisión, emisión, registro y efecto; distinguir precedencia acreditada e incertidumbre sin retroactividad por defecto. |
| RS04 | Vistas de evidencia por finalidad y destinatario | C02/C13/C15 | Conservar original y vista, relación y condiciones de acceso; separar recuperabilidad documental y restricción material de difusión. |
| RS05 | Plan, razón y permiso de la actuación | P32; C08–C12 | Distinguir previsión, autorización y excepción urgente; conservar consecuencias y alternativas sin deducir ilicitud de toda desviación. |
| RS06 | Admisión, U y fallo técnico | C02/C06/C14; todos los perfiles | Admitir evidencia válida de un acto no autorizado cuando corresponda; separar no admisión, no aplicabilidad, insuficiencia y fallo de Tri. |
| RS07 | Cobertura de instancias, permisos y flujos | C05/C11/C15 | Detectar dependencias o trayectos omitidos, ámbitos incompatibles y conjuntos vacíos no acreditados. |
| RS08 | Explicación y salidas diferenciadas | C13; P02 frente a P25–P32 | Conservar resultado técnico, legitimidad, incertidumbre y consecuencias; no denominar Frame a un informe sin arquitectura constituida. |
| RS09 | Estado inicial y límite de la historia | EP01–EP04; C17; CT-01–05 | Recuperar por separado referencia aprobada, estado observado y pasado conocido; una captura posterior no acredita el estado anterior. |
| RS10 | Antecedentes múltiples y relaciones tipadas | EP10/EP11; C17; CT-06–11 | Conservar extremos, tipos y respaldo; distinguir referencia recíproca, precedencia estricta imposible y causalidad acreditada. |
| RS11 | Custodia, designación y obligación pendiente | EP07/EP08/EP10; CT-12–18 | Distinguir poder actuar, recibir pruebas y asumir un deber; conservar aceptación sólo cuando el régimen la exige y sin exoneración automática. |
| RS12 | Conciliación, cobertura y reevaluación selectiva | EP05/EP06/EP09/EP12–EP14/EP18; CT-19–32 | Conservar identidades por clase, efectos inciertos y prueba vinculada a generación; revisar sólo dependencias y tiempos pertinentes. |

Las condiciones de admisión y las relaciones se fijan por perfil y operación. Una observación válida de una instalación fallida no es un fallo del capturador. Una evidencia admisible puede mostrar una actuación no autorizada. Un 0 exige la evidencia negativa prevista por su contrato; el silencio no la sustituye. Un fallo técnico no produce Tri.U ni una salida alternativa del dominio.

Cada necesidad deberá recorrerse desde la fuente o contrato externo hasta análisis, representación, validación, serialización, ligadura, recuperación y uso por la operación que se pretenda acreditar. La salida del contraste identificará el último punto demostrado. Referenciar un documento puede conservar información suficiente para una operación concreta; esa suficiencia debe demostrarse mediante recuperación definida. Conservar una huella o un texto sin una interpretación comprobada no acredita aplicación de sus obligaciones.

## 7. Perfiles de idioma, dominio y soporte tecnológico

El acuerdo de perfiles se recibe como obligación arquitectónica vigente según [acta técnica de perfiles, contratos y ensamblaje](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/66967a80a40f4e2781ef983bd725690db54c25c5/docs/calidad/ACTA_TECNICA_DE_PERFILES_CONTRATOS_Y_ENSAMBLAJE_DEL_LENGUAJE_SV_2026_09_06.md), especialmente §§3–9, y la [especificación de perfiles fuente SVP-ES/SVP-EN](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/66967a80a40f4e2781ef983bd725690db54c25c5/ESPECIFICACION_NORMATIVA_PERFILES_FUENTE_SVP_ES_EN_v1_2026_08_29.md). Debe formar parte del estudio de OP-CYB-001 y de su ensamblaje.

| Componente | Disciplina compartida | Distinción y prueba propias |
| --- | --- | --- |
| Perfiles fuente español e inglés | Identidad, selección explícita, versión, procedencia y compatibilidad. | Dos superficies de una gramática, IR y semántica comunes. El ensamblaje mantiene nombre, bytes y perfil de cada unidad; no traduce datos de dominio ni concatena unidades borrando sus fronteras. |
| Perfil o constitución de dominio | Identidad y versión del conocimiento admitido; cobertura, referentes y relaciones explícitos. | OP-CYB-001 conserva significado profesional y reglas constituidas. Ensamblar archivos no constituye composición de dominios o agentes ni autoriza ampliar cobertura. |
| Perfil de soporte tecnológico | Identidad de realización, capacidades, requisitos, dependencias y condiciones verificables. | Conserva interfaces, recursos, aislamiento, persistencia, transporte y fallos. Su representación formal y su imposición material requieren comprobaciones diferentes. |

La analogía con ES/EN exige conservación y compatibilidad verificables; no permite implementar los perfiles de dominio como una simple traducción de etiquetas. Tampoco se presume que los tres componentes ya tengan contratos ejecutables completos. El marco está constituido; el acta de perfiles mantiene pendientes las realizaciones que no hayan sido acreditadas.

El ensamblaje deberá identificar las versiones efectivamente relacionadas, los requisitos y capacidades de cada componente y las ligaduras que soportan cada operación. Debe hacer visibles ausencia, colisión, incompatibilidad y transformación. El mismo nombre de parámetro no acredita igualdad de definición; la misma definición utilizada por dos sujetos no les impone el mismo estado. La sede formal —IR, meta-IR, contrato externo enlazado o combinación tipada— pertenece al diseño del Lenguaje y deberá justificarse por su capacidad de conservar y comprobar las obligaciones recibidas.

### 7.1. Necesidades tecnológicas aportadas por este universo

La tercera propuesta, el perfil tecnológico, recibe presión concreta del propio conocimiento de Ciberseguridad. OP-CYB-001 puede fundamentar requisitos de infraestructura sin convertirse por ello en una plataforma, un nuevo universo constituido o un permiso de despliegue.

| Necesidad de soporte | Presión del universo | Qué debe separar el receptor |
| --- | --- | --- |
| Identidad de lo efectivamente cargado | P06/P13/P22; EP02/EP04 | Artefacto disponible, componente utilizado y selección de próxima carga; coherencia documental y observación real. |
| Origen y continuidad de registros | C02/C07/C17; RS09–RS11 | Identidad, autenticidad, custodia, antecedentes, corrección y detección material de sustitución o bifurcación. |
| Autoridad y límites de las sesiones | P25–P32; C11; RS01–RS03 | Declaración de facultades, acreditación institucional e imposición material; revocar una cuenta no acredita fin de toda sesión. |
| Protección de datos y vistas | C15/C16; RS04/RS07 | Representación de la política, vista transmitida y controles efectivos de acceso, retención y difusión. |
| Conciliación y efectos inciertos | EP08/EP09/EP18; RS11/RS12 | Recepción de mensaje, actuación, resultado material y obligación pendiente; un tiempo de espera agotado no prueba ausencia de efecto ni repetición segura. |
| Cobertura, recuperación y coste | C05/C06/C08–C12; EP12–EP14/EP17 | Trayecto protegido, dependencia compartida, prueba válida, capacidad de recuperación y presupuesto; una declaración no prueba el conjunto. |

Estas necesidades se cotejarán con las obligaciones PT01–PT14 y la matriz del registro experimental 020 ya enlazadas por el acta rectora. No se crean catorce sustitutos ni se declara un perfil tecnológico ejecutable mediante esta tabla. La evidencia de los ensayos 012, 016 y 018 conserva sus condiciones originales. Una realización tecnológica deberá ensayarse en el laboratorio competente antes de promover sus garantías; no se exige desplegar una plataforma para efectuar el contraste representacional inicial.

DFL-009 comparece ahora por su oportunidad de evaluación tras el primer universo CYB: servicio nativo, aislamiento, identidad, recursos, fallos y coste. Se conserva su encargo y la evidencia disponible sin elegir por esta acta Cloudflare, Workers, .NET, FFI, WASM o cualquier proveedor. La evaluación tecnológica no sustituye el contraste de semántica e IR ni borra sus obligaciones.

## 8. Oferta recibida y fronteras de la prueba

RETP-105 acredita la integración de LIG/0.1, su contraste documental y las guardas estructurales H06/H07 en el alcance identificado. Esa parte de DFL-005 no se vuelve a declarar inexistente. La deuda general sobre campos, autoridad y capacidades adicionales conserva sus límites. La recepción tampoco acredita consultas CQ1–CQ6 completas, causalidad ejecutiva, continuidad persistente, productores de criticidad ni producción observación → Tri.

Las necesidades de K1-T, DFL-003/004/006 y las capacidades materiales R2/R3/R4 deben relacionarse con las operaciones de este universo. Registrar que una capacidad está fuera de la oferta no prueba que sea irrelevante para una operación que la necesita. La conclusión deberá decir qué alcance puede sostenerse y qué obligación impide ofrecer el restante.

No hay arquitectura celular CYB constituida por el recuento de 32. El contraste de contratos y recuperabilidad puede comenzar con objetos documentales propios y operaciones acotadas. Si una prueba exige una asignación celular de dominio que todavía falta, se identifica la necesidad constitutiva y se devuelve únicamente ese objeto. No se fabrican posiciones ni se declara una imposibilidad universal por no disponer de esa arquitectura.

El Lenguaje tiene competencia para diagnosticar incompatibilidades y proponer correcciones o alternativas formales. **No tiene potestad para cambiar la necesidad profesional, el perímetro o el conocimiento aprobado de Ciberseguridad.** La unidad de dominio tampoco establece por sí sola una nueva invariante universal. El Director mantiene la decisión soberana cuando una propuesta cambia el conocimiento o excede el encargo.

## 9. Trabajo receptor y forma del dictamen

El encargo permite iniciar la valoración con los documentos y datos entregados. No se añade una aprobación intermedia para lecturas, cotejos o preparación del contraste ya autorizado. Los cambios materiales del Lenguaje mantienen el régimen propio de su sede y sus competencias; esta acta no modifica su código.

1. **Fijar identidad y preguntas.** Registrar el corte del Lenguaje, el corte CYB y la operación concreta que se juzga. Reutilizar las fichas, requisitos, corpus y esperados originales.
2. **Construir la correspondencia.** Dar tratamiento expreso a REQ-CYB-001–009 y RS01–RS12, con solapamientos motivados; identificar dato, relación, regla, resultado y capa responsable.
3. **Contrastar representación y recuperación.** Mostrar qué conserva cada paso y qué puede recuperar la operación. Declarar información lateral, versión, disponibilidad y autoridad cuando sea necesaria; no atribuir al mensaje lo que sólo aporta esa información lateral.
4. **Comprobar perfiles y ensamblajes.** Preservar ES/EN y fronteras de unidades; contrastar el contrato del dominio y las necesidades de soporte sin equiparar los tres ensamblajes ni transferir permisos por composición.
5. **Ejecutar controles discriminantes.** Comprometer resultados esperados antes de la ejecución; incluir positivos, negativos y sensibilidad del observador. Para cada cambio funcional, aplicar las comprobaciones y destinos pertinentes exigidos en el Lenguaje. Un defecto común de la misma realización Rust no se excluye por paridad entre destinos.
6. **Atribuir las carencias.** Separar defecto normativo, defecto de implementación, defecto del comprobador, información constitutiva ausente y obligación material externa. Proponer el cambio mínimo probado o declarar la insuficiencia en su alcance; conservar diagnóstico y consecuencia.
7. **Devolver un dictamen único.** Entregar correspondencia completa, fuentes, versiones, artefactos, comandos, resultados, limitaciones y obligaciones pendientes, con su sede y siguiente actuación.

Para una pérdida informativa deberá demostrarse que dos casos admisibles y pertinentes, con respuestas profesionales diferentes bajo regla fijada, colisionan en la representación examinada o impiden la recuperación requerida. Los pares documentales entregados son punto de partida; no se presentan como estados celulares completos ni como pérdida de la IR antes de ensayarla. La suficiencia se acredita para operación, entradas y alcance declarados; una ausencia de contraejemplo sólo permite la conclusión que soporte la cobertura de la prueba.

Se distinguirán **pérdida demostrada**, **suficiencia acreditada en alcance declarado** y **contraste no concluyente**. No se exige encontrar una pérdida ni conservar artificialmente la IR si resulta insuficiente. El lenguaje puede proponer una extensión compatible, otra versión o una representación suficiente conforme a sus reglas, sin relajar la necesidad profesional para obtener un resultado favorable.

Toda ejecución válida con identidad completa idéntica deberá producir iguales bytes de salida canónica en el alcance constituido. Un fallo técnico implica ausencia de ejecución válida y sólo genera el registro técnico estructurado correspondiente; nunca constituye una salida alternativa del dominio. Los estados del procedimiento de auditoría no amplían el alfabeto 0, 1 y U.

## 10. Resultados disponibles y límites que acompañan a la entrega

Se reciben las campañas documentales de las revisiones 0.2, 0.3 y 0.4 con 64, 46 y 32 casos sintéticos, respectivamente, y sus pruebas de sensibilidad. Esta acta no las presenta como una muestra estadística ni como una nueva ejecución. La última revisión obtuvo dos resultados idénticos, SHA-256 `8d35d2a9d870c1a496b2018437aee47d5a7960b7ae8d36e4ddc244085965aa50`.

Los ocho pares de continuidad fijan sólo P02 y P06 a 1; los otros treinta parámetros no se instancian. Los diez pares regulados conservan su contrato propio. El ensayo nominal nativo anterior, descrito en el dictamen 0.1, probó transporte y rechazo en tres fuentes; una operación vacía y una referencia a un capturador no ejecutado no se elevan a ejecución CYB.

Permanecen sin acreditación operacional: sensores y capturadores reales del universo, autenticación y autoridad institucional real, política efectiva de difusión de datos, custodia material resistente al adversario, cobertura real de todas las instancias y trayectos, transducción productiva, arquitectura CYB y Frame ejecutado. Estas fronteras delimitan afirmaciones de capacidad; no paralizan por sí solas la valoración representacional.

La aprobación del Director cierra la condición de adopción de las definiciones en este expediente. Los deberes restantes de SVP-DV-004/005 conservan un alcance concreto y no se emplean para solicitar de nuevo la decisión entre uno y dos universos. Las obligaciones DFL del Lenguaje permanecen en su registro, con las sucesiones allí acreditadas.

## 11. Dimensión del dominio y criterio de continuidad

Los escenarios conservados son 29, 38 y 59 universos propuestos, con 288, 552 y 1.062 definiciones orientativas; se leen aproximadamente como 290, 550 y 1.060. Proceden de 59 productos candidatos, presupuestos adicionales e hipótesis de reutilización, no de universos ya constituidos. El cálculo y su sensibilidad están en [estimación y contraste con el Lenguaje, revisión 0.3](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/b3aa3f01c825bf6440e3f04aadc87cc7c7ee6d89/dominios/ciberseguridad-inteligente/dominio-04-09-26/universos/OP-CYB-001/ESTIMACION_Y_CONTRASTE_CON_LENGUAJE_v0.3.md) y en la consolidación en Calidad.

Estas cifras permiten planificar y apreciar alcance; no condicionan el contraste actual ni imponen un segundo universo. Si aparece una distinción profesional que no pueda instanciarse pertinentemente en OP-CYB-001, se expondrán objeto, consecuencia y carencia concreta a la autoridad de Ciberseguridad y al Director. Un incremento de cantidad sin una necesidad semántica distinta no constituye por sí solo esa demostración.

El retorno autorizado al Lenguaje es efectivo documentalmente con la publicación de esta acta en la rama emisora. Corresponde al receptor registrar su recepción y continuar el examen, conservando la secuencia y las obligaciones tecnológicas aplicables. Ciberseguridad permanece en pausa controlada hasta una candidata pertinente, una necesidad constitutiva demostrada o una nueva orden del Director. No se inicia otro universo por iniciativa de la IA.
