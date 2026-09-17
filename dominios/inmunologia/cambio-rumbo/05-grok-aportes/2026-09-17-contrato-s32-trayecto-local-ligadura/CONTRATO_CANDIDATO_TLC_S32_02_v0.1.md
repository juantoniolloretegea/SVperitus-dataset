# Contrato candidato TLC-S32-02 · trayecto local completo con ligadura a interfaces constituidas

**Versión:** 0.1  
**Identificador:** TLC-S32-02  
**Estatuto:** contrato candidato documental. No congela interfaz, no habilita el flujo y no cierra S32 ni BIS-03.  
**Seguimiento:** S32, en ejecución. No se asigna identificador RETP.  
**Naturaleza de los datos de ensayo previstos:** sintéticos y ficticios, sin uso clínico.

## 1. Identificación, relación con S32 y con TLC-S32-01

Este contrato constituye el siguiente paso de S32 exigido por el parte de privacidad y seguridad, apartado 11.7, tras la correspondencia revisada con C17 (RETP-2026-249). Desarrolla **un único trayecto local completo** de consulta, autorización, salida y persistencia.

En la misma carpeta de aportes existen los candidatos [TLC-S32-01 v0.1](../2026-09-17-contrato-s32-trayecto-local/CONTRATO_CANDIDATO_TLC_S32_01_v0.1.md) y [TLC-S32-01 v0.2](../2026-09-17-contrato-s32-trayecto-local-v0.2/CONTRATO_CANDIDATO_TLC_S32_01_v0.2.md). TLC-S32-02 no los sobrescribe. Añade la ligadura a tipos y funciones **constituidos** de `sv_core` en el corte del Lenguaje, la constitución de C17 leída en el expediente v0.4 §8, y las fronteras de R2-0 que el trayecto no puede eludir.

Cubre de §11.7:

- componente e interfaz de cada etapa, con estado de constitución explícito;
- identidad, finalidad, recurso, destinatario y permiso;
- admisión y comprobaciones anteriores al efecto;
- revocación, reintentos, concurrencia y consumo;
- información permitida en salida, errores y evidencia;
- persistencia, conservación, supresión y restauración, sin plazos inventados;
- resultado esperado, criterio de aceptación y observador.

Queda pendiente de §11.7 y de las puertas de §8:

- habilitación material y cualquier ensayo de privacidad;
- resolución expresa de API externa y consulta federada; el entrenamiento federado permanece excluido;
- contratos de ingesta clínica masiva, telemetría CYB y banco ejecutable de privacidad;
- responsable efectivo, base jurídica, EIPD cuando proceda y plazos del flujo;
- host, transporte, bus y persistencia durable R2.

## 2. Cortes y fuentes

| Objeto | Corte o identidad | Uso |
|---|---|---|
| Lenguaje SV, rama `main` | `03578e3c3919d38ed1ae1dbc686d36ea9147c0b6` | Cabeza vigente; coincide con el corte de referencia del encargo. |
| Parte S32 | blob `518cc9a311bac9c9be8db7933c7e42bea0efcac6` | §§7–8 y 11, en especial 11.3, 11.5 y 11.7. |
| Estudio BIS-03 | blob `48a425ddd89aed43269068af967c4ed77a9d4a0c` | Flujos, esquema de admisión §7 y pares P01–P10. |
| Expediente predecisional v0.4 | blob `602d1c5ad33a27da1eb76ce2e72400de0902f42f` | EP01–EP18; §§3–5; constitución de C17 en §8. |
| Ampliación atómica v0.3 | blob `80ff6cd7febb0610b2f42e5a5846a84af3b46cba` | Condiciones de C01–C16. |
| Acta de relevo OP-CYB-001 | blob `54d72e794b13f5b785f76121f641768351046a8d` | RS01–RS12; REQ-CYB; adenda §12. |
| Contrato R2-0 | blob `8faa1028e04a1e4fdd7d10bea63c74064abaccf3` | Fronteras de persistencia; R2 permanece abierto. |
| `sv_core` | mismo corte del Lenguaje | `Permit`, `decide_permit_traced`, `AdmissibilityState`, `CaptureOutcome`. |

Los códigos RS, REQ-CYB, EP y C pertenecen a OP-CYB-001. Los pares P01–P10 pertenecen al estudio BIS-03, §7. No designan los parámetros P01–P32 de OP-CYB-001.

## 3. Objeto del trayecto

**Nombre:** consulta profesional local de un caso particular, con autorización vigente al efecto, vista de salida y evidencia mínima.

**Uso cubierto:** aplicación del conocimiento admitido (EP16) a un caso particular seleccionado por el profesional. Consultar sobre un caso no habilita Internet ni investigación externa. La aplicación no aprende por el camino ni modifica autónomamente conocimiento, pesos o constitución de dominio.

**Uso no cubierto:** API externa; consulta estadística federada; entrenamiento federado; ingesta masiva desde HCE; telemetría general de OP-CYB-001; publicación a un destinatario distinto del profesional peticionario; cualificación de leyenda Q1/Q2 o E1–E16.

El recurso de caso particular es obligatorio en TLC-S32-02. Una consulta profesional general reutilizaría E2–E4, pero no se constituye aquí como segundo trayecto.

## 4. Etapas, componentes e interfaces

El orden es estricto. Ninguna etapa posterior se ejecuta si la anterior no admite.

| Etapa | Operación | Componente | Interfaz | Estado de constitución |
|---|---|---|---|---|
| E1 | Recibir y clasificar la petición | Servicio de consulta local (sede funcional de §8) | `I-CONSULTA-LOCAL` | Pendiente de constitución como servicio de host. El Lenguaje puede representar campos; el servicio no existe. |
| E2 | Autorizar antes del efecto | Admisor del esquema BIS-03, ligado a fuente institucional EP07; el sello R1-4/R1-5 sólo si esa ligadura existe | `I-AUTORIZACION` | El esquema de admisión **no** está materializado. El sello intra-proceso está constituido (`decide_permit_traced` en `rust/sv_core/src/decision_trace.rs`) y **no cubre por sí solo** este acto. Proveedor de identidad, sesiones EP06 y ligadura con el profesional no están constituidos. |
| E3 | Emitir la vista de salida | Productor de informe de consulta | `I-SALIDA-VISTA` | Pendiente. `sv_core::frame` es el Frame celular de R0-7; no es esta salida. RS08 prohíbe denominar Frame a un informe sin arquitectura constituida. |
| E4 | Conservar evidencia mínima y no el contenido indebido | Persistencia R2 y custodia | `I-EVIDENCIA-MINIMA` | Contrato R2-0 abierto. `DecisionTrace` es intra-proceso y no sustituye `AStore`. S26-F01/F02/F06/F08 permanecen pendientes. |

El efecto de consulta —lectura del conocimiento admitido y del subconjunto autorizado del caso— sólo puede producirse tras E2 y antes de E3.

Los nombres `I-CONSULTA-LOCAL`, `I-AUTORIZACION`, `I-SALIDA-VISTA` e `I-EVIDENCIA-MINIMA` son etiquetas documentales de este candidato. No existen como tipos, rasgos ni API de `sv_core`.

La consulta gramatical `consultar` / `QuerySpec` / `IrQueryContext` es representación declarativa. `context_wellformed` no ejecuta consultas. No es el servicio de E1.

Host, bus, transporte y perfil central de agente **no están constituidos** por el rector.

### 4.1. Ligadura a tipos constituidos de `sv_core`

Estos tipos existen y se reutilizan. No se presentan como el servicio de consulta ni como persistencia durable.

| Tipo o función | Sede | Función en el trayecto | Límite |
|---|---|---|---|
| `CaptureOutcome<T>` (`Observation` / `Bottom`) | `rust/sv_core/src/admissibility.rs` | Fallo técnico de captura anterior a toda admisión. `Bottom` no pertenece a `Tri`. | No clasifica el contenido ni autoriza el acto. |
| `AdmissibilityState` (`Ok` / `Degraded` / `NotAdmitted`) | mismo módulo | Admisibilidad técnica de la evidencia. Distinta de autorización. `NotAdmitted` no es `Tri::U`. | Una evidencia admisible puede acreditar un acto no autorizado (§11.3; C02). |
| `decide_permit` → `PermitDecision::{Granted, NotGranted}` | `permission.rs` | Función pública de sellado intra-proceso. `NotGranted` no es autoridad negativa ni ejecuta efectos. | No autentica al profesional, no comprueba cuotas ni vigencia durable. La vía pública conforme de R1-5 no parte de esta función aislada. |
| `PermitRejection` | `permission.rs` | `RefutedRequirements` / `NotVerifiableRequirements`. | No pertenece a `Tri`. |
| `decide_permit_traced` → `TracedPermitDecision` | `decision_trace.rs` | Única entrada pública de decisión protegida de R1-5. D-R o D-N quedan trazados sin fabricar un `Permit` negativo. | Continuidad `ProtectedDecisionContinuity` intra-proceso. `DecisionTraceRef` no representa tiempo, vigencia ni identidad durable entre procesos. |
| `AccumulationContract` | `authority` | Reutilización y acumulación del permiso. | Sin contrato de cuota, «cuotas disponibles» no se da por cierto. |

La superficie pública conforme de R1-5 recorre `decide_permit_traced`, `mediate_traced_permit` y `execute_traced_mediated` bajo `ProtectedDecisionContinuity`. Este trayecto **no** acredita mediación ni ejecución de un efecto clínico: el efecto de consulta permanece pendiente de E1/E3/E4 y de EP07.

## 5. Identidad, finalidad, recurso, destinatario y permiso

Esquema de admisión del estudio BIS-03, §7:

```text
admitir = identidad válida
        ∧ finalidad autorizada
        ∧ recurso autorizado
        ∧ destinatario permitido
        ∧ condiciones vigentes
        ∧ cuotas disponibles
```

Una condición desconocida o incompleta impide el uso. Este trayecto no se habilita mientras las cuotas, la fuente de autoridad o los plazos aplicables permanezcan sin contrato.

| Campo | Valor en TLC-S32-02 | Fuente |
|---|---|---|
| Identidad | Profesional peticionario, con vínculo entre identidad institucional, cuenta y función (EP05). No se equipara al paciente ni a un nombre aportado por la llamada. | RS01; C02/C11; EP05/EP07 |
| Finalidad | Consejo asistido con conocimiento admitido sobre el caso particular, sin investigación externa y sin entrenamiento. | EP01; RS05; parte §7.1 |
| Recurso | Subconjunto del caso seleccionado por el profesional y explícitamente autorizado, más el corte de conocimiento admitido (EP16). No se hereda el acceso hospitalario del médico. | RS02/RS07; C05/C11/C15 |
| Destinatario | El mismo profesional peticionario. No hay publicación. | RS04; C15; EP15 |
| Permiso | `Permit` sellado, limitado a operación, recurso, organización, destinatario y vigencia; fuente competente distinta de la petición. | R1-4; RS02; C11; EP07 |
| Condiciones vigentes | Permiso no revocado; conocimiento admitido no sustituido; sesión no caducada. | RS03; C07; EP06 |
| Cuotas | Pendiente de constitución. El predicado «cuotas disponibles» no se afirma. | estudio §7; R2-5; R2-0 §14 |

El acceso del experto a la HCE no concede automáticamente igual acceso al agente. Una referencia íntegra no otorga facultades (RS02).

## 6. Condiciones de admisión y comprobaciones anteriores al efecto

Antes de producir el efecto:

1. **Captura.** Fallo técnico → `CaptureOutcome::Bottom`. No produce `Tri.U`.
2. **Admisibilidad técnica** (`AdmissibilityState`). Distinta de la autorización del acto (§11.3; RS06; C02).
3. **Clasificación del contenido** (EP15). La etiqueta «sintético», «local» o «artificial» no sustituye el examen de C16.
4. **Contexto de aplicabilidad C16**, cuando el uso lo exija: entidad, jurisdicción, actividad, función, categoría, dimensiones, fecha y versión de la disposición. Un campo ausente **bloquea** la habilitación; no se rellena.
5. **Identidad y fuente de autoridad (EP07).** La raíz de permiso no puede ser un nombre suministrado por la llamada o por el agente.
6. **Finalidad, recurso y destinatario** según §5. Cambio de finalidad respecto del permiso → rechazo, sin efecto.
7. **Vigencia al instante del efecto.** Emisión, registro, recepción y efecto se conservan separados (RS03). No hay retroactividad por defecto.
8. **Conocimiento admitido (EP16).** Versión fijada antes de evaluar.

C08–C12 conservan sus condiciones particulares: una consulta no exige por sí sola un plan operativo ni una ventana de intervención (§11.5).

Este contrato no declara al SV sistema HCE, no lo conecta a MyHealth@EU y no determina la base jurídica del tratamiento. Esas decisiones corresponden al responsable competente y, cuando proceda, a su DPD. No se inventan aquí.

## 7. Revocación, reintentos, concurrencia y consumo

| Situación | Comportamiento exigido | Referencia |
|---|---|---|
| Revocación anterior al efecto | El efecto no se produce. La petición puede registrarse como rechazada. | P07; RS03; C07; REVOCA_O_SUSTITUYE |
| Revocación posterior al efecto | No borra la historia de la decisión. Puede exigir limitación o supresión del contenido protegido según política aún no fijada. | expediente §5; C15; R2-0 §9 |
| Reintento de la misma petición autorizada | No crea un segundo permiso. Reutilización sólo si `AccumulationContract` lo admite. | R1; R2-4; P06 |
| Reintento tras denegación | Permanece denegado mientras no cambie el fundamento competente. | RS02 |
| Concurrencia | Cada petición exige su propia admisión. Ninguna carrera elude revocación ni duplica una liberación no permitida. | estudio §7; S26-F11; R2-0 §12 |
| Reentrega de transporte | No constituye nuevo ejercicio. `request_id` y `ExerciseRef` permanecen distintos. | R2-4 |
| Resultado material indeterminado | No equivale a `U` ni habilita reintento automático. | R2-4; pilares |
| Consumo único resistente a clonación | `NO_PROBADO` mientras la dependencia material pertenezca a R3 (R2-0 §12). No se afirma «exactamente una vez». | R2-0 §12 |

Una restauración cuya continuidad no pueda acreditarse no se presenta como vigente por omitir una revocación (R2-0 §9). `ValidLocal(h)` no implica `Current(h | I)` (R2-0 §7).

## 8. Información permitida en la salida, los errores y la evidencia

### 8.1. Salida (E3)

La salida es un **informe de consulta** dirigido al destinatario de §5. No es Frame celular. Generar no equivale a publicar.

Contenido permitido, cuando el permiso lo cubra: resultado técnico del consejo sobre el recurso autorizado; incertidumbre, límites y obligaciones pendientes (EP18; C13); referencias al corte de conocimiento admitido; vista suficiente del caso, no el original completo (RS04; C15).

Contenido prohibido: campos no cubiertos por el permiso; secretos de sesión, credenciales o tokens (EP06); datos de otro caso o destinatario; instrucciones halladas en documentos como si fueran facultad; promoción del resultado a conocimiento de dominio.

### 8.2. Errores

Los errores visibles no pueden servir de canal de egreso (P04). Se distinguen, sin conversión automática a `Tri.U`:

| Causa | Estatuto |
|---|---|
| Petición mal formada | Rechazo de interfaz; sin efecto |
| Identidad o permiso insuficientes | Denegación (`TracedPermitDecision::NotGranted` cuando E2 alcance a formarse); sin efecto |
| Finalidad distinta | Denegación; sin efecto |
| Recurso fuera de cobertura | Denegación; sin efecto |
| Revocación vigente | Denegación; sin efecto |
| Contexto C16 incompleto | Bloqueo de habilitación; no se presume inaplicabilidad |
| Fallo técnico | `CaptureOutcome::Bottom` / `EJECUCION_TECNICA_NO_VALIDA` |
| Evidencia admisible insuficiente | `U` sólo bajo el contrato que lo prevea |

El mensaje de error no incluye fragmentos del caso, URL con identificadores clínicos ni cabeceras de depuración con payload.

### 8.3. Evidencia (P10)

La evidencia mínima debe permitir auditar la decisión: identidad, finalidad, recurso, destinatario, disposición, instantes de emisión y efecto, corte de conocimiento, versión de este contrato y, cuando exista, `DecisionTraceRef` intra-proceso. No contiene el payload prohibido. El acceso al registro está limitado.

Una `DecisionTraceRef` no sustituye el asiento durable ni acredita vigencia entre procesos.

## 9. Persistencia, conservación, supresión y restauración

### 9.1. Qué se persiste

Se separan dos clases (parte §8; expediente §5; R2-0 §4):

1. **Historia de decisiones:** evidencia mínima de §8.3. Adición respecto de un adversario y una infraestructura declarados; CORRIGE añade asiento, no borra.
2. **Contenido protegido del caso:** sólo el subconjunto autorizado, con retención y supresión gobernadas. La adición no determina retención ilimitada.

`DecisionTrace` intra-proceso no es `AStore`. Una vista, caché o índice no adquiere autoridad (R2-0 §5). `x ∉ View(AStore)` no implica `x ∉ AStore` salvo cobertura acreditada.

### 9.2. Plazos

Los plazos de conservación, supresión y limitación **no se fijan**. Dependen de la finalidad y de las obligaciones aplicables (C15/C16; RGPD arts. 5 y 17, cuando procedan). Inventarlos excedería la competencia de este contrato. Mientras falten, el trayecto no se habilita.

### 9.3. Supresión y restauración

| Operación | Exigencia | Estado |
|---|---|---|
| Supresión o limitación autorizada | No puede presentarse el original como si siguiera disponible | Pendiente de realización R2-3 |
| Restauración | Preserva consumo y revocación; no revive permiso revocado ni contenido cuya conservación ya no procede; no elige rama por `HEAD` o fecha mayor | Pendiente; S26-F08; P08; R2-0 §§7 y 9 |
| Copia Git pública | No recibe contenido personal protegido | Obligación documental vigente (estudio §5) |
| Huella | No garantiza anonimato ni sustituye la supresión del original | C15; estudio §3 |

C17 coordina C01–C16 y las nueve clases de relación del expediente §4. No convierte al SV en plataforma de autenticación ni acredita historia completa de un sistema real (expediente §8).

## 10. Resultado esperado, criterio de aceptación y observador

**Resultado esperado del trayecto positivo:** el profesional titular, con permiso vigente, obtiene únicamente la vista autorizada del caso particular y del conocimiento admitido; se registra evidencia mínima sin payload prohibido; no hay egreso lateral ni aprendizaje.

**Criterio de aceptación material:** evidencia positiva y negativa del flujo completo, con fixtures artificiales, oráculo independiente, versión de interfaz y observador del efecto (estudio §7). Ese criterio **no está satisfecho**. Los casos previstos permanecen no ejecutados.

**Observador previsto:** comprobador en Rust, biblioteca estándar, sobre entradas sintéticas; observación del efecto en destino (salida entregada y almacén). Hasta que existan E1, la ligadura E2 con EP07, el productor E3 y el `AStore` de E4, el observador no puede constituirse. Las comprobaciones de formato o compilación de esta entrega no son ese observador.

## 11. Correspondencia con C17 y con los flujos de §8

El expediente v0.4, §8, constituye C17 como **control compuesto de estado inicial y continuidad**, coordinador de C01–C16 y de las nueve clases documentales de relación: REFIERE, DERIVA_DE, PRECEDE_A, CAUSA_ACREDITADA, CORRIGE, RECIBE_CUSTODIA, DESIGNA, ACEPTA_ENCARGO y REVOCA_O_SUSTITUYE. Se conservan 32 definiciones paramétricas y 18 elementos de contexto; esas cantidades no son células, matrices ni átomos.

El trayecto aplica, en el alcance local, las filas de §11.5 «Consulta por persona», «Inferencia local» (aislamiento y ausencia de promoción), «Frame, documento o exportación» (generación frente a difusión) y «Registros, respaldos e historia».

Controles y requisitos pertinentes, con sus condiciones: RS01–RS08; REQ-CYB-001/004/007/009; EP01/EP05/EP06/EP07/EP15/EP16/EP17/EP18; C02/C07/C11/C13/C14/C15/C16. C17 interviene como coordinador de la evidencia del episodio, no como plataforma. C08–C12 no se activan por el mero hecho de consultar.

CAUSA_ACREDITADA exige fuente y criterio propios; la proximidad temporal no basta. DESIGNA y ACEPTA_ENCARGO no nacen de un acuse de recibo de archivos.

## 12. Decisiones pendientes concretas

1. Identificar la organización responsable del tratamiento y, cuando proceda, el apoyo del DPD.  
2. Determinar la base jurídica y, si hay categorías especiales, la condición adicional. No se presume el artículo 9 por el nombre del dominio.  
3. Decidir si procede EIPD antes de cualquier tratamiento personal.  
4. Fijar plazos de conservación y supresión del flujo.  
5. Constituir la fuente institucional de autoridad (EP07) y el régimen de sesiones (EP06).  
6. Constituir el contrato de cuotas o declarar expresamente que, sin él, el trayecto permanece inhabilitado.  
7. Completar el contexto C16 del uso seleccionado, o declarar la no habilitación mientras falte.  
8. Resolver inclusión o exclusión de API externa y de consulta federada antes del cierre documental de §5 del parte. El entrenamiento federado permanece excluido.  
9. Realizar E1, E3 y E4; ligar E2 a EP07.  
10. Disponer banco de fixtures de privacidad independiente de personas reales, con examen de C15/C16.  
11. Enlazar cada realización diferida necesaria con un seguimiento concreto antes de cerrar S32.

## 13. Relación documental para recepción posterior

Entrega candidata depositada en `SVperitus-dataset`, rama `dominio-inmunologia`, carpeta `dominios/inmunologia/cambio-rumbo/05-grok-aportes/2026-09-17-contrato-s32-trayecto-local-ligadura/`. No modifica el Lenguaje, OP-CYB-001, Sucesos, RETP, mapas ni componentes constituidos. No sustituye los bytes de TLC-S32-01. La recepción posterior, si procede, corresponde a S32 sobre el corte entonces vigente.
