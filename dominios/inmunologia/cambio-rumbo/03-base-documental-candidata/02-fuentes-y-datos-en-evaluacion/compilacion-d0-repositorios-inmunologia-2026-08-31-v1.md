# Compilación D0 de repositorios de inmunología

**Corte:** 31 de agosto de 2026  
**Versión:** 1.1  
**Estatuto:** documento interno de taller; no constituye sección del preprint, adopción de fuente, autorización de acceso ni recomendación asistencial.  
**Estado de la puerta D0:** **ABIERTA / NO SUPERADA**.  
**G0:** no se ha creado cuenta, firmado DUA, solicitado acceso ni descargado microdato.

---

## 1. Objeto

Cruzar los dos estudios independientes aportados por las unidades Claude y Grok, conservar sus diferencias y establecer qué repositorios merecen una auditoría estudio a estudio antes de constituir el dominio clínico.

Este documento no usa el nombre de un repositorio como prueba de cobertura. Distingue:

1. existencia del recurso;
2. régimen jurídico y técnico de acceso;
3. disponibilidad de datos individuales;
4. correspondencia con el episodio clínico;
5. presencia material de variables y desenlaces;
6. aptitud para validación de investigación;
7. aptitud asistencial, que no se presume.

---

## 2. Entradas preservadas

| Entrada | Procedencia | SHA-256 |
|---|---|---|
| `ae816e80-9c35-4ad5-8d9a-710f6dcaa486.md` | Unidad Claude, versión 2 corregida tras adversarial | `15f3c4550dd992b89d2fa3906b58efef4106b32acbe2fb3585a7eed1ba3d659f` |
| `c19e3012-c2b4-4b26-a4d0-59d91193f276.md` | Unidad Grok, Informe A1 adversarial + fichas normativas | `e92f6cf87ee0d224898ff77acb3446489b36572bbd0045bceb838c1c0c424974` |

Ninguna entrada ha sido modificada. Las correcciones de esta compilación se registran aquí, no se escriben retrospectivamente sobre los informes de origen.

---

## 3. Resultado del cruce

### 3.1. Coincidencia nuclear

Ambos informes sostienen, por vías independientes, lo siguiente:

- existen repositorios institucionales de inmunología y datos clínicos relacionados;
- «anonimizado», «desidentificado», «seudonimizado» y «dato molecular sin paciente» no son equivalentes;
- el acceso al portal no demuestra disponibilidad del episodio clínico necesario;
- ninguna cláusula leída autoriza por sí misma el uso asistencial;
- la cobertura debe verificarse estudio a estudio, variable a variable y desenlace a desenlace;
- IMMUNO-1 e IMMUNO-2 no quedan validados por el inventario;
- la puerta empírica permanece abierta.

### 3.2. Aportaciones complementarias

Claude aporta con mayor detalle:

- MIMIC-IV/PhysioNet, Vivli y BIFAP;
- la restricción expresa de PhysioNet frente al envío de datos a servicios de modelos de lenguaje;
- dos candidatos concretos de ImmPort: SDY3324 y SDY3274;
- mecanismos de empaquetado, versionado, hashes y desidentificación de ImmPort.

Grok aporta con mayor detalle:

- ImmuneSpace, ESID, USIDNET, REDIP/RePER, OAS, AIRR/iReceptor y VDJdb;
- la separación jurídica entre Safe Harbor, seudonimización europea, registro de pacientes y datos moleculares;
- el ataque explícito contra la identificación de «inmunología» con el episodio de las semillas;
- la clasificación entre acceso abierto, cuenta, acreditación, comité y contrato.

---

## 4. Universo consolidado: 14 recursos

| ID | Recurso | Objeto dominante | Acceso principal | Relación provisional con las semillas | Estado D0 |
|---|---|---|---|---|---|
| D01 | ImmPort | Estudios NIAID/DAIT; datos clínicos, laboratorio y experimentos | Cuenta/acuerdo; parte compartida y parte controlada | Candidato de descubrimiento. Requiere auditoría SDY por SDY | No adoptado |
| D02 | ImmuneSpace | Capa de análisis de estudios HIPC, principalmente sobre ImmPort | Descarga/análisis; hereda el estudio primario | Candidato para vacunación e inmunología de sistemas; no sustituye la auditoría del estudio | No adoptado |
| D03 | ITN TrialShare | Datos desidentificados de ensayos ITN publicados y código de análisis | Cuenta; términos del portal | Candidato clínico. Política rectora vigente no cerrada documentalmente | No adoptado / U documental |
| D04 | FlowRepository | Ficheros FCS y metadatos MIFlowCyt | Descarga de experimentos públicos | Complemento citométrico; no historia clínica ni curso asistencial | No adoptado |
| D05 | IEDB | Epítopos, MHC, anticuerpo y célula T curados | Exportación abierta, con reservas de terceros | Complemento molecular; no cohorte clínica de pacientes | No adoptado |
| D06 | OAS | Repertorios BCR anotados | Descarga abierta de unidades de datos | Complemento molecular; no episodio de profilaxis | No adoptado |
| D07 | AIRR Data Commons / iReceptor | Repertorios BCR/TCR distribuidos | Acceso heterogéneo por repositorio | Complemento molecular; régimen no uniforme | No adoptado |
| D08 | VDJdb | TCR con especificidad antigénica | Web/GitHub | Complemento molecular; licencia no cerrada | No adoptado / U licencia |
| D09 | ESID Registry | Errores innatos de la inmunidad | Proyecto aprobado, contrato o centro | Objeto clínico distinto de inmunosupresión farmacológica adquirida | No adoptado |
| D10 | USIDNET | Errores innatos de la inmunidad; v1/v2 | Agregados web o consulta aprobada | Objeto distinto; versiones y DUA no unificados | No adoptado / U versión |
| D11 | REDIP / RePER | Registro español de inmunodeficiencias primarias | Profesional/rol acreditado | Objeto distinto; no descarga abierta | No adoptado |
| D12 | PhysioNet / MIMIC-IV | Historia clínica hospitalaria general | Credencial, formación y acuerdo específico | Posible fuente complementaria de curso clínico; no repositorio inmunológico específico | No adoptado / uso local obligatorio |
| D13 | Vivli | Datos individuales de ensayos clínicos de múltiples dominios | Propuesta, revisión y posible entorno seguro | Buscador potencial de ensayos concretos; no basta la plataforma general | No adoptado |
| D14 | BIFAP | Historia clínica de atención primaria y farmacoepidemiología española | Investigador/organismo y procedimiento AEMPS | Potencial para exposición farmacológica y resultados; condiciones y granularidad pendientes | No adoptado / U acceso |

### 4.1. Frentes todavía no examinados

- dbGaP, SRA y EGA, si el dominio exige datos genómicos que ImmPort no hospeda.
- UKPIN/UKPID, CEREDIH, LASID, J-PID y red Jeffrey Modell.
- Human Cell Atlas/CELLxGENE para compartimentos inmunitarios, si aparece una necesidad molecular concreta.

Estos recursos no deben añadirse por acumulación. Sólo se examinan cuando una necesidad clínica o variable candidata justifique su clase de dato.

---

## 5. Verificación oficial adicional realizada en esta compilación

### 5.1. Último release efectivo de ImmPort

La U de Claude sobre el último release queda resuelta.

La página oficial de notas contiene un documento material de **DR67**, con `Release Date: August 2026`, tres estudios nuevos y dos actualizados. El calendario oficial fija la fecha de publicación en **27-08-2026**.

- Notas DR67: <https://docs.immport.org/data/release/notes/DR67_DataRelease/>
- Calendario: <https://docs.immport.org/data/release/schedule/>

**Conclusión:** a fecha de corte, el último release efectivamente documentado es **DR67**. DR68 es futuro, previsto para 24-09-2026.

### 5.2. SDY3324 — ACV01

La fuente oficial confirma:

- estudio aleatorizado, multicéntrico, adaptativo y abierto;
- enfermedades autoinmunes bajo inmunosupresión farmacológica;
- micofenolato/ácido micofenólico, metotrexato y terapia de depleción B;
- reglas explícitas de mantenimiento o suspensión temporal del tratamiento;
- umbrales serológicos Roche Elecsys Anti-SARS-CoV-2 S;
- 148 sujetos en el release;
- DOI `10.21430/M35OC5U8Z7`;
- existencia del archivo completo `SDY3324_DR60_ALL_DATA.zip` en la página de descarga.

La misma nota oficial declara:

- `Assays: None`;
- `Clinical Assessments: None`.

**Dictamen:** es el candidato más próximo localizado hasta ahora para la semilla de vacunación en inmunosupresión farmacológica no trasplante. Sin embargo, no queda adoptado: debe inspeccionarse el manifiesto y el contenido real del paquete para saber si existen filas de sujetos, serologías, tratamientos, tiempos y resultados utilizables. La descripción del protocolo no sustituye al dato.

- Ficha: <https://immport.org/shared/study/SDY3324>
- Descarga/archivo: <https://immport.org/shared/study/SDY3324/download>
- Nota DR60: <https://docs.immport.org/data/release/notes/DR60_DataRelease/>

### 5.3. SDY3274 — ARTIST

La fuente oficial confirma:

- 250 receptores adultos de trasplante renal;
- inmunosupresión continuada y seguimiento observacional;
- objetivo centrado en firma de tolerancia operacional;
- `Assays: None` y `Clinical Assessments: None` en la nota del release.

**Dictamen:** no pertenece al recorte no trasplante de IMMUNO-2. Puede servir posteriormente como contraste de límites o composición, pero no como cohorte primaria de validación de esa semilla.

- Ficha: <https://immport.org/shared/study/SDY3274>
- Nota DR60: <https://docs.immport.org/data/release/notes/DR60_DataRelease/>

### 5.4. TrialShare: diferencia documental no resuelta

Claude identifica una `TrialShare Access and Usage Policy` v1.2 de 15-07-2013. Grok identifica una `Data Sharing Policy` v2.0 de 27-08-2019. La página oficial vigente confirma acceso a datos de estudios publicados mediante cuenta gratuita y declara datos individuales desidentificados, pero no expone en la lectura recuperada cuál de esos documentos gobierna hoy todos los usos.

No se unifican ambos títulos ni se presume derogación.

**Estado:** U documental hasta obtener y comparar literalmente ambos documentos, sus ámbitos y su vigencia.

- Página oficial actual: <https://www.immunetolerance.org/for-researchers/trialshare>

### 5.5. Criba de estudios concretos: publicación frente a depósito material

La búsqueda por título recuperó varios estudios clínicamente muy próximos a las semillas. La auditoría de sus notas oficiales de release cambia sustancialmente la valoración:

| Estudio | Afinidad clínica provisional | Declaración del estudio/publicación | Depósito declarado por ImmPort | Dictamen D0 |
|---|---|---|---|---|
| **SDY2351** | IMMUNO-1; mieloma múltiple, vacunación y posible disociación humoral/celular | Pacientes vacunados con mieloma múltiple; pregunta sobre respuestas B y T en seronegativos | **56 sujetos; 108 muestras ELISA; evaluación clínica `MM_Medical_History`; ELISPOT 0** | **Primer candidato material para IMMUNO-1.** Auditar manifiesto y diccionario; todavía no demuestra las variables exigidas por ITI V.1 ni los desenlaces |
| **SDY2248** | IMMUNO-1; NHL/CLL, anti-CD20 y vacunación | La descripción refiere 121 pacientes y mediciones longitudinales | En DR49: **0 sujetos; 0 muestras** de citometría, inmunoensayo múltiple y neutralización; sin evaluaciones clínicas | Registro de publicación en ese release, no cohorte utilizable demostrada. El portal actual indexa una cifra distinta; queda U de versionado hasta revisar manifiesto vigente |
| **SDY2389** | IMMUNO-1; CLL, anti-CD20, IVIg y fallo de respuesta | Cohorte publicada de 95 pacientes con CLL y 30 controles | En DR49.1: **0 sujetos; 0 muestras** en todos los ensayos; sin evaluaciones clínicas | Gran afinidad narrativa, depósito material no demostrado |
| **SDY2725** | IMMUNO-1; exposición acumulada a anti-CD20 | La publicación refiere 48 pacientes bajo depleción B y 10 controles | En DR52.1: **0 sujetos; 0 muestras** en los tres tipos de ensayo; sin evaluaciones clínicas | Registro de publicación; no candidato primario mientras no aparezca un depósito posterior verificable |
| **SDY2653** | IMMUNO-1/episodio oncohematológico; dosis de refuerzo | Ensayo prospectivo en cáncer; respuesta humoral, celular y neutralización | En DR51.2: **0 sujetos; 0 muestras** en cuatro tipos de ensayo; sin evaluaciones clínicas; sólo enlaza código y registro del ensayo | No confundir resultados publicados ni código analítico con microdatos depositados |
| **SDY2672** | IMMUNO-2; autoinmunidad e inmunosupresores | La publicación describe 463 pacientes; incluye depleción B, fingolimod, MMF y belimumab | En DR53.1: **0 sujetos; sin ensayos y sin evaluaciones clínicas**; enlaza material suplementario externo | El suplemento puede ser otra fuente, pero exige auditoría jurídica y material propia |
| **SDY3324** | IMMUNO-2; inmunosupresión farmacológica no trasplante | Ensayo ACV01 con 148 sujetos declarados | **148 sujetos**, pero `Assays: None` y `Clinical Assessments: None` | Candidato de protocolo/paquete; no se presume que contenga las variables necesarias |

Fuentes oficiales:

- DR49.1, SDY2351 y SDY2389: <https://docs.immport.org/data/release/notes/DR49.1_DataRelease/>
- DR49, SDY2248: <https://docs.immport.org/home/release_notes/DR49_DataRelease/>
- DR51.2, SDY2653: <https://docs.immport.org/home/release_notes/DR51.2_DataRelease/>
- DR52.1, SDY2725: <https://docs.immport.org/home/release_notes/DR52.1_DataRelease/>
- DR53.1, SDY2672: <https://docs.immport.org/home/release_notes/DR53.1_DataRelease/>
- DR60, SDY3324: <https://docs.immport.org/data/release/notes/DR60_DataRelease/>

**Regla adversarial incorporada:** el tamaño de muestra descrito en un resumen o publicación no es el número de sujetos depositados; la enumeración de métodos no es la presencia de muestras; una página de descarga no prueba que el paquete contenga las variables necesarias. Los tres niveles deben verificarse por separado y con versión fechada.

### 5.6. Límite técnico alcanzado sin credenciales

La documentación oficial actual indica que cada página de estudio ofrece un manifiesto preparado para descarga y que el inventario de disponibilidad puede consultarse mediante los servicios de ImmPort. El flujo de descarga por DRS y las operaciones que devuelven el inventario completo requieren autenticación mediante cuenta, OAuth o clave de API con los permisos correspondientes.

- Guía de descarga y formato del manifiesto: <https://docs.immport.org/download/>
- Endpoints de rutas de ficheros por estudio: <https://docs.immport.org/apidocumentation/shareddataapi/studyfilepaths/>
- Inventario previo y acceso a ficheros mediante el servidor oficial: <https://docs.immport.org/mcp/overview/>

**Consecuencia de gobierno:** la inspección material de los manifiestos de SDY2351 y SDY3324 queda detenida en G0. No se crea cuenta, no se solicita OAuth, no se genera clave y no se descarga paquete sin una orden expresa. Esta detención no es un fallo de evidencia: es la separación obligatoria entre descubrimiento público y acceso autorizado.

---

## 6. Clasificación funcional provisional

### 6.1. Prioridad de auditoría estudio a estudio

1. **ImmPort SDY2351**, como primer depósito con sujetos, muestras y una evaluación clínica declarados y por su proximidad a IMMUNO-1.
2. **ImmPort SDY3324**, por proximidad con IMMUNO-2, sometido a inspección de manifiesto porque no declara ensayos ni evaluaciones clínicas.
3. **ITN TrialShare**, buscando ensayos publicados que contengan profilaxis, vacunación, infecciones, exposición inmunosupresora y resultados individualizados.
4. **ImmuneSpace**, como capa de descubrimiento de estudios vacunales, siempre remitiendo al estudio y acuerdo primarios.
5. **Vivli**, mediante búsqueda de ensayos concretos y no por el nombre general de la plataforma.
6. **BIFAP**, sólo si se confirma que su acceso y granularidad permiten la pregunta farmacoepidemiológica propuesta.

### 6.2. Complementos no sustitutivos

- FlowRepository para citometría.
- IEDB para epítopos y ensayos inmunológicos curados.
- OAS, AIRR/iReceptor y VDJdb para repertorios adaptativos y especificidad antigénica.
- PhysioNet/MIMIC para curso hospitalario general, bajo tratamiento local y sin transferencia a modelos externos.

Un complemento molecular no demuestra por sí mismo profilaxis, decisión clínica, daño por omisión ni desenlace del paciente.

### 6.3. Fuera del episodio semilla actual

ESID, USIDNET y REDIP/RePER estudian principalmente errores innatos/inmunodeficiencias primarias. No se descartan del futuro dominio amplio, pero no se usan para simular cobertura del episodio de inmunosupresión farmacológica adquirida.

---

## 7. Puerta D0: condiciones pendientes

D0 sólo podrá superarse cuando exista, al menos para un episodio declarado:

1. repositorio y estudio concretos;
2. acceso lícito y reproducible;
3. unidad de análisis identificada;
4. diccionario de variables;
5. filas o muestras efectivamente disponibles;
6. exposición inmunosupresora documentada;
7. intervención o profilaxis documentada;
8. desenlace clínico o inmunológico preespecificado;
9. tiempo explícito y interpretable;
10. ausencia, pérdida y calidad auditables;
11. posibilidad de separar construcción y evaluación;
12. régimen de publicación y atribución compatible.

La presencia de una URL, un DOI o una cifra global de sujetos no satisface ninguna de estas doce condiciones por sí sola.

---

## 8. Próximo trabajo autorizado por el flujo, no ejecutado todavía

1. Obtener los manifiestos vigentes de **SDY2351** y **SDY3324** sin descargar microdatos y clasificar sus ficheros.
2. Resolver las discrepancias de versión y depósito de **SDY2248** y, si existiera actualización posterior, de SDY2389, SDY2725, SDY2653 y SDY2672.
3. Resolver la política documental vigente de TrialShare.
4. Buscar estudios concretos en TrialShare, ImmuneSpace y Vivli para los dos episodios semilla.
5. Sólo después, cruzar diccionarios de datos con los parámetros actuales de ITI V.1.
6. Mantener separados:
   - disponibilidad jurídica;
   - disponibilidad técnica;
   - adecuación clínica;
   - correspondencia paramétrica;
   - validación empírica.

No se abre cuenta, no se firma DUA y no se descarga dato individual sin orden expresa del titular.

---

## 9. Dictamen de corte

La unión de ambos informes mejora sustancialmente el mapa de fuentes y resuelve el último release de ImmPort. La criba posterior identifica **un primer depósito materialmente prometedor para IMMUNO-1 (SDY2351)**, pero no prueba todavía que su diccionario cubra el episodio ni que exista una cohorte utilizable para validar IMMUNO-1 o IMMUNO-2.

**SDY2351 es un candidato de datos, no una fuente adoptada.**  
**SDY3324 es un candidato de protocolo/paquete, no una fuente adoptada.**  
**SDY3274 no corresponde al recorte no trasplante.**  
**D0 continúa abierta.**
