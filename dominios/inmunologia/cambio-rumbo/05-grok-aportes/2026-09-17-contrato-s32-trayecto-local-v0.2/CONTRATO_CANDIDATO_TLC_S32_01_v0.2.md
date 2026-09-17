# Contrato candidato TLC-S32-01 · trayecto local de consulta, autorización, salida y persistencia

**Versión:** 0.2  
**Identificador:** TLC-S32-01  
**Estatuto:** contrato candidato documental. No es interfaz congelada, no habilita el flujo y no cierra S32 ni BIS-03.  
**Seguimiento:** S32, en ejecución. No se asigna identificador RETP.  
**Naturaleza de los datos de ensayo previstos:** sintéticos y ficticios, sin uso clínico.

Un candidato v0.1 del mismo identificador permanece depositado en la carpeta hermana `2026-09-17-contrato-s32-trayecto-local/`. Esta versión no lo modifica. Precisa tres objetos que no se confunden: el esquema de admisión del estudio BIS-03, el sello intra-proceso R1-4 y `AdmissibilityState`.

## 1. Identificación y relación con S32

Este contrato constituye el siguiente paso de S32 exigido por el parte de privacidad y seguridad, apartado 11.7, tras la correspondencia revisada con C17 (RETP-2026-249). Desarrolla un único trayecto local completo que cubre, de forma conjunta, las cuatro etapas comunes: consulta, autorización, salida y persistencia.

Cubre de §11.7:

- la identificación de componente e interfaz de cada etapa del trayecto local;
- identidad, finalidad, recurso, destinatario y permiso aplicables a ese trayecto;
- condiciones de admisión y comprobaciones anteriores al efecto;
- comportamiento ante revocación, reintentos y concurrencia;
- información permitida en la salida, los errores y la evidencia;
- persistencia, conservación, supresión y restauración, con plazos no inventados;
- resultado esperado, criterio de aceptación y observador.

Queda pendiente de §11.7 y de las puertas de §8:

- la habilitación material del flujo y cualquier ensayo de privacidad;
- la resolución expresa de las opciones condicionadas (API externa y consulta federada) y la exclusión ya fijada del entrenamiento federado;
- los contratos de los demás flujos de la matriz (ingesta clínica masiva, telemetría CYB, banco ejecutable de privacidad);
- el responsable efectivo, la base jurídica del tratamiento, la EIPD cuando proceda y los plazos de conservación del flujo;
- la constitución de host, transporte, bus y persistencia durable R2.

## 2. Cortes y fuentes

| Objeto | Corte o identidad | Uso |
|---|---|---|
| Lenguaje SV, rama `main` | `03578e3c3919d38ed1ae1dbc686d36ea9147c0b6` | Cabeza vigente al preparar este candidato; coincide con el corte de referencia del encargo. |
| Parte S32 | blob `518cc9a311bac9c9be8db7933c7e42bea0efcac6` | §§7–8 y 11, en especial 11.5 y 11.7. |
| Estudio BIS-03 | blob `48a425ddd89aed43269068af967c4ed77a9d4a0c` | Flujos, esquema de admisión §7 y pares P01–P10. |
| Expediente predecisional v0.4 | blob `602d1c5ad33a27da1eb76ce2e72400de0902f42f` | EP01–EP18; §§3–5; C17 en §8. |
| Ampliación atómica v0.3 | blob `80ff6cd7febb0610b2f42e5a5846a84af3b46cba` | Condiciones de C01–C16. |
| Acta de relevo OP-CYB-001 | blob `54d72e794b13f5b785f76121f641768351046a8d` | RS01–RS12; REQ-CYB-001–009; adenda §12. |
| Contrato R2-0 | blob `8faa1028e04a1e4fdd7d10bea63c74064abaccf3` | Fronteras de persistencia; R2 permanece abierto; R2-1 no iniciado. |
| Núcleo `sv_core` | mismo corte del Lenguaje | Permiso R1-4, traza R1-5, admisibilidad de captura, Frame celular. |
| Pilares 05/09 | blob `044f89f7c826f0ba52c58ee8ff19572e7b3b2187` | Host, bus y transporte no constituidos; `U` distinto de fallo técnico. |
| Acta de perfiles 06/09 | blob `1df9b818f3f531f628fe0e89dd2c497b5da52d4d` | Terna representación/dominio/soporte; vía pública trazada de R1. |
| Acta de transición OP-IMM-001 | blob `44f8fda87856ab16007195cab324d40a758e506a` | `EJECUCION_TECNICA_NO_VALIDA`; adendas §§12–30. |

Los códigos RS, REQ-CYB, EP y C pertenecen a OP-CYB-001. Los pares P01–P10 pertenecen al estudio BIS-03, §7. No designan los parámetros P01–P32 de OP-CYB-001. Esta regla desarrolla el Acta 001, §9.

## 3. Objeto del trayecto

**Nombre:** consulta profesional local de un caso particular, con autorización vigente al efecto, vista de salida y evidencia mínima.

**Uso cubierto:** aplicación del conocimiento admitido (EP16) a un caso particular seleccionado por el profesional. El profesional mantiene su trabajo principal y selecciona los datos pertinentes. Consultar sobre un caso no habilita Internet ni investigación externa.

**Uso no cubierto por este contrato:** API externa; consulta estadística federada; entrenamiento federado; ingesta masiva desde HCE u otro custodio; telemetría general de OP-CYB-001; publicación o exportación a un destinatario distinto del profesional peticionario; cualificación de leyenda Q1/Q2 o E1–E16.

Una consulta profesional general, sin recurso de caso particular, reutiliza las mismas etapas E2–E4. No se trata aquí como segundo trayecto; el recurso de caso particular es obligatorio en TLC-S32-01.

## 4. Tres objetos de admisión y permiso que no se sustituyen

Antes de las etapas, se fijan tres objetos ya existentes o diseñados. Ninguno implementa a los otros.

| Objeto | Qué cubre | Qué no cubre | Estado |
|---|---|---|---|
| Esquema de admisión BIS-03, §7 | `identidad ∧ finalidad ∧ recurso ∧ destinatario ∧ condiciones vigentes ∧ cuotas` para el acto de consulta | No es tipo de `sv_core`. No es sello R1. | Diseño; no materializado. Una condición desconocida impide el uso. |
| `Permit` / `decide_permit_traced` (R1-4 / R1-5) | Sello intra-proceso de un efecto protegido: forma, autoridad constituida, requisitos y D-A. Vía pública: `ProtectedDecisionContinuity` → `decide_permit_traced` → `mediate_traced_permit` → `execute_traced_mediated`. `decide_permit` no es API pública. | No autentica al profesional, no comprueba cuotas, no es vigencia durable entre procesos, no es autorización de privacidad del flujo. Una firma de transporte no demuestra procedencia gobernada ante un receptor remoto. | Constituido en `sv_core` en su alcance intra-proceso. |
| `AdmissibilityState` / `CaptureOutcome` | Admisión técnica de una observación de captura (`Ok`, `Degraded`, `NotAdmitted`). `Bottom` es fallo técnico de captura. Distinto de `Tri`. | No autoriza el acto. Una evidencia admisible puede acreditar un acto no autorizado (RS06; C02). | Constituido en `sv_core`. |

E2 exige el esquema de admisión, vigente al efecto. El sello R1 sólo podrá ligarse a ese acto cuando existan la fuente institucional (EP07) y la continuidad que lo reciba. Mientras falte esa ligadura, E2 no está realizado.

La consulta gramatical `consultar` / `QuerySpec` / `IrQueryContext` es representación declarativa. `context_wellformed` no ejecuta consultas. No es el servicio de E1.

## 5. Etapas, componentes e interfaces

El orden es estricto. Ninguna etapa posterior se ejecuta si la anterior no admite.

| Etapa | Operación | Componente | Interfaz | Estado de constitución |
|---|---|---|---|---|
| E1 | Recibir y clasificar la petición de consulta | Servicio de consulta local (sede funcional de §8) | `I-CONSULTA-LOCAL` | Pendiente de constitución como servicio de host. El Lenguaje puede representar los campos; no existe el servicio. S26-F01/F02 conservan pendiente la consulta por ocurrencia exacta y la resolución por instancia y posición; LIG no las sustituye. |
| E2 | Autorizar el acto antes del efecto | Admisor del esquema BIS-03, ligado a fuente institucional EP07; el sello R1-4/R1-5 sólo si esa ligadura existe | `I-AUTORIZACION` | El esquema no está materializado. El sello intra-proceso está constituido y no cubre por sí solo este acto. Proveedor de identidad, sesiones EP06 y ligadura con el profesional no están constituidos. |
| E3 | Emitir la vista de salida | Productor de informe de consulta | `I-SALIDA-VISTA` | Pendiente. `sv_core::frame` es el Frame celular de R0-7; no es esta salida. RS08 prohíbe denominar Frame a un informe sin arquitectura constituida. |
| E4 | Conservar evidencia mínima y no el contenido indebido | Persistencia R2 y custodia | `I-EVIDENCIA-MINIMA` | Contrato R2-0 abierto. R2-1 no iniciado. `DecisionTrace` es intra-proceso y no sustituye persistencia durable. S26-F06/F08 permanecen pendientes. |

El efecto de la consulta —lectura del conocimiento admitido y del subconjunto autorizado del caso— sólo puede producirse tras E2 y antes de E3. Ese efecto no constituye aprendizaje, promoción de conocimiento ni modificación autónoma de dominio, pesos o constitución (parte §7.1; P03).

Host, bus, transporte y perfil central de agente **no están constituidos** por el rector. Se enumeran como sedes pendientes, no como implementados.

Los nombres `I-CONSULTA-LOCAL`, `I-AUTORIZACION`, `I-SALIDA-VISTA` e `I-EVIDENCIA-MINIMA` son etiquetas documentales de este candidato. No existen como tipos, rasgos ni API de `sv_core`.

## 6. Identidad, finalidad, recurso, destinatario y permiso

Esquema de admisión del estudio BIS-03, §7:

```text
admitir = identidad válida
        ∧ finalidad autorizada
        ∧ recurso autorizado
        ∧ destinatario permitido
        ∧ condiciones vigentes
        ∧ cuotas disponibles
```

Una condición desconocida o incompleta impide el uso hasta resolverse. Este trayecto no puede habilitarse mientras las cuotas, la fuente de autoridad o los plazos aplicables permanezcan sin contrato.

| Campo | Valor en TLC-S32-01 | Fuente |
|---|---|---|
| Identidad | Profesional peticionario, con vínculo entre identidad institucional, cuenta y función (EP05). No se equipara al paciente ni a un nombre aportado por la llamada. | RS01; C02/C11; EP05/EP07 |
| Finalidad | Consejo asistido con conocimiento admitido sobre el caso particular, sin investigación externa y sin entrenamiento. | EP01; RS05; parte §7.1 |
| Recurso | Subconjunto del caso seleccionado por el profesional y explícitamente autorizado, más el corte de conocimiento admitido (EP16). No se hereda el acceso hospitalario del médico. | RS02/RS07; C05/C11/C15 |
| Destinatario | El mismo profesional peticionario. No hay publicación. | RS04; C15; EP15 |
| Permiso | Permiso sellado, limitado a operación, recurso, organización, destinatario y vigencia; fuente competente distinta de la petición. | R1-4; RS02; C11; EP07 |
| Condiciones vigentes | Permiso no revocado; conocimiento admitido no sustituido; sesión no caducada. | RS03; C07; EP06 |
| Cuotas | Pendiente de constitución. Mientras falte el contrato, el predicado «cuotas disponibles» no se da por cierto. | estudio §7; R2-5 |

El acceso del experto a la HCE no concede automáticamente igual acceso al agente (parte §7.1). Una referencia íntegra no otorga facultades (RS02).

## 7. Condiciones de admisión y comprobaciones anteriores al efecto

Antes de producir el efecto de consulta deben cumplirse, en este orden:

1. **Captura de la petición.** Fallo técnico de captura → `EJECUCION_TECNICA_NO_VALIDA` / `CaptureOutcome::Bottom`. No produce `Tri.U`.
2. **Admisibilidad técnica de la evidencia aportada** (`AdmissibilityState`). Distinta de la autorización del acto. Una evidencia admisible puede acreditar un acto no autorizado (RS06; C02; §11.3).
3. **Clasificación del contenido** (EP15): personal / no personal; categoría especial cuando conste; secreto; identificabilidad para el destinatario. La etiqueta «sintético», «local» o «artificial» no sustituye el examen de C16.
4. **Identidad y fuente de autoridad.** La raíz de permiso no puede ser un nombre suministrado por la llamada o por el agente (EP07).
5. **Finalidad, recurso y destinatario** según §6. Cambio de finalidad respecto del permiso → rechazo, sin efecto. Permiso insuficiente o ausente → rechazo, sin efecto.
6. **Vigencia al instante del efecto.** Emisión, registro, recepción y efecto se conservan separados (RS03). No hay retroactividad por defecto.
7. **Conocimiento admitido.** Versión de reglas y perfiles fijada antes de evaluar (EP16). Un cambio de corpus no se atribuye al corte anterior.

C08–C12 conservan sus condiciones particulares: una consulta no exige por sí sola un plan operativo ni una ventana de intervención (§11.5).

C16 exige contexto acreditado: entidad, jurisdicción, actividad, función, categoría, dimensiones, fecha y versión de la disposición. Este contrato no declara al SV sistema HCE, no lo conecta a MyHealth@EU y no determina la base jurídica del tratamiento. Esas decisiones corresponden al responsable competente y, cuando proceda, a su DPD. No se inventan aquí.

## 8. Revocación, reintentos y concurrencia

| Situación | Comportamiento exigido | Referencia |
|---|---|---|
| Revocación anterior al efecto | El efecto no se produce. La petición puede quedar registrada como rechazada. | P07; RS03; C07; REVOCA_O_SUSTITUYE |
| Revocación posterior al efecto | No borra la historia de la decisión. Puede exigir limitación o supresión del contenido protegido según la política aún no fijada. | expediente §5; C15 |
| Reintento de la misma petición autorizada | No crea un segundo permiso. Reutilización sólo si el contrato de acumulación lo admite (`AccumulationContract`). | R1; R2-4; P06 |
| Reintento tras denegación | Permanece denegado mientras no cambie el fundamento competente. | RS02 |
| Concurrencia de dos peticiones | Cada una exige su propia admisión. Ninguna carrera puede eludir revocación ni duplicar una liberación no permitida. | estudio §7; S26-F11 |
| Reentrega de transporte | No constituye nuevo ejercicio. `request_id` y `ExerciseRef` permanecen distintos. | R2-4 |
| Resultado material indeterminado | No equivale a `U` ni habilita reintento automático. | R2-0 §11; R2-4 (no iniciado) |

## 9. Información permitida en la salida, los errores y la evidencia

### 9.1. Salida (E3)

La salida es un **informe de consulta** dirigido al destinatario de §6. No es Frame celular. Generar no equivale a publicar (parte §8).

Contenido permitido, cuando el permiso lo cubra:

- resultado técnico del consejo sobre el recurso autorizado;
- incertidumbre, límites y obligaciones pendientes (EP18; C13);
- referencias al corte de conocimiento admitido;
- vista suficiente del caso, no el original completo (RS04; C15).

Contenido prohibido en la salida:

- campos del caso no cubiertos por el permiso;
- secretos de sesión, credenciales o tokens (EP06);
- datos de otro caso o de otro destinatario;
- instrucciones halladas en documentos como si fueran facultad (adenda §12.3.1);
- promoción del resultado a conocimiento de dominio.

### 9.2. Errores

Los errores visibles no pueden servir de canal de egreso (P04). Se distinguen, sin conversión automática a `Tri.U`:

| Causa | Estatuto |
|---|---|
| Petición mal formada | Rechazo de interfaz; sin efecto |
| Identidad o permiso insuficientes | Denegación; sin efecto |
| Finalidad distinta | Denegación; sin efecto |
| Recurso fuera de cobertura | Denegación; sin efecto |
| Revocación vigente | Denegación; sin efecto |
| Fallo técnico | `EJECUCION_TECNICA_NO_VALIDA` |
| Evidencia admisible insuficiente | `U` sólo bajo el contrato que lo prevea |

El mensaje de error no incluye fragmentos del caso, URL con identificadores clínicos ni cabeceras de depuración con payload.

### 9.3. Evidencia (P10)

La evidencia mínima debe permitir auditar la decisión: identidad, finalidad, recurso, destinatario, disposición (admitido/denegado), instantes de emisión y efecto, corte de conocimiento y versión de este contrato. No contiene el payload prohibido del caso. El acceso al registro está limitado (P10). `DecisionTrace` intra-proceso no es ese registro durable.

## 10. Persistencia, conservación, supresión y restauración

### 10.1. Qué se persiste

Se separan dos clases (parte §8; expediente §5; R2-0 §4):

1. **Historia de decisiones:** evidencia mínima de §9.3. Append-only respecto de un adversario y una infraestructura declarados; no reescribe el juicio anterior (CORRIGE añade asiento, no borra).
2. **Contenido protegido del caso:** sólo el subconjunto autorizado, con retención y supresión gobernadas. Append-only no determina retención ilimitada.

`DecisionTrace` intra-proceso no es `AStore`. Una vista, caché o índice no adquiere autoridad (R2-0 §5; S26-F07). Bytes íntegros no equivalen a estado vigente.

### 10.2. Plazos

Los plazos de conservación, supresión y limitación **no se fijan en este candidato**. Dependen de la finalidad y de las obligaciones aplicables (C15/C16; RGPD arts. 5 y 17, cuando procedan). Inventarlos excedería la competencia de este contrato. Mientras falten, el trayecto no se habilita.

### 10.3. Supresión y restauración

| Operación | Exigencia | Estado |
|---|---|---|
| Supresión o limitación autorizada | No puede presentarse el original como si siguiera disponible | Pendiente de realización R2-3 |
| Restauración | Preserva consumo y revocación; no revive permiso revocado ni contenido cuya conservación ya no procede | Pendiente; S26-F08; P08 |
| Confirmación durable de escritura | Respuesta perdida no prueba reversión; escritura aceptada no prueba durabilidad | Pendiente; S26-F06 |
| Copia Git pública | No recibe contenido personal protegido | Obligación documental ya vigente (estudio §5) |
| Huella | No garantiza anonimato ni sustituye la supresión del original | C15; estudio §3 |

## 11. Resultado esperado, criterio de aceptación y observador

**Resultado esperado del trayecto positivo:** el profesional titular, con permiso vigente, obtiene únicamente la vista autorizada del caso particular y del conocimiento admitido; se registra evidencia mínima sin payload prohibido; no hay egreso lateral ni aprendizaje.

**Criterio de aceptación material:** evidencia positiva y negativa del flujo completo, con fixtures artificiales, oráculo independiente, versión de interfaz y observador del efecto (estudio §7). Ese criterio **no está satisfecho**: no existe aún la implementación que permita ejecutarlo. Los casos previstos permanecen no ejecutados.

**Observador previsto:** comprobador en Rust, con biblioteca estándar, sobre entradas sintéticas; observación del efecto en el destino (salida entregada y almacén). Hasta que existan el servicio E1, la ligadura E2 con fuente EP07 y el esquema de admisión, el productor E3 y el `AStore` de E4, el observador no puede constituirse. Las comprobaciones de formato o compilación de esta entrega no son ese observador.

## 12. Correspondencia con C17 y con los flujos de §8

El trayecto aplica, en el alcance local, las filas de §11.5 «Consulta por persona», «Inferencia local» en lo relativo a aislamiento y ausencia de promoción, «Frame, documento o exportación» en lo relativo a generación frente a difusión, y «Registros, respaldos e historia».

C17, constituido en el expediente v0.4, §8, es control compuesto de estado inicial y continuidad: coordina C01–C16 y las nueve relaciones documentales de §4. Interviene como coordinador de la evidencia del episodio, no como plataforma ni como átomo nuevo. No se adjudican como átomos generales «responsabilidad heredada», «sistema inicialmente seguro», «inventario fiable» ni «perímetro protegido».

Controles y requisitos pertinentes, con sus condiciones conservadas: RS01–RS08; REQ-CYB-001/004/007/009; EP01/EP05/EP06/EP07/EP15/EP16/EP17/EP18; C02/C07/C11/C13/C14/C15/C16. C08–C12 no se activan por el mero hecho de consultar.

Relaciones documentales aplicables al episodio (expediente §4), sin incorporarlas al alfabeto SV: REFIERE, DERIVA_DE, PRECEDE_A, CORRIGE, RECIBE_CUSTODIA, DESIGNA, ACEPTA_ENCARGO, REVOCA_O_SUSTITUYE. CAUSA_ACREDITADA exige fuente y criterio propios; la proximidad temporal no basta.

## 13. Decisiones pendientes concretas

1. Identificar la organización responsable del tratamiento y, cuando proceda, el apoyo del DPD.  
2. Determinar la base jurídica y, si hay categorías especiales, la condición adicional aplicable. No se presume el artículo 9 por el nombre del dominio.  
3. Decidir si procede EIPD antes de cualquier tratamiento personal.  
4. Fijar plazos de conservación y supresión del flujo.  
5. Constituir la fuente institucional de autoridad (EP07) y el régimen de sesiones (EP06).  
6. Constituir el contrato de cuotas o declarar expresamente que, sin él, el trayecto permanece inhabilitado.  
7. Resolver inclusión o exclusión de API externa y de consulta federada antes del cierre documental de §5 del parte. El entrenamiento federado permanece excluido.  
8. Realizar E1, E3 y E4; materializar E2 como esquema de admisión ligado a EP07, sin tomar el sello R1 por esa autorización.  
9. Disponer banco de fixtures de privacidad independiente de personas reales, con examen de C15/C16.  
10. Decidir si el contrato de consulta local exige la interfaz de ocurrencia exacta (S26-F01/F02). Hoy esa interfaz no existe; no se cierra F01/F02 de paso.  
11. Enlazar cada realización diferida necesaria con un seguimiento concreto antes de cerrar S32.  
12. Fijar, cuando exista tratamiento personal, que su evaluación no se difiere. Este candidato no afirma que no exista; deja la incógnita con sede.

## 14. Relación documental para recepción posterior

Entrega candidata depositada en `SVperitus-dataset`, rama `dominio-inmunologia`, carpeta `dominios/inmunologia/cambio-rumbo/05-grok-aportes/2026-09-17-contrato-s32-trayecto-local-v0.2/`. No modifica el Lenguaje, OP-CYB-001, Sucesos, RETP, mapas, componentes constituidos ni el candidato v0.1. La recepción posterior, si procede, corresponde a S32 sobre el corte entonces vigente.
