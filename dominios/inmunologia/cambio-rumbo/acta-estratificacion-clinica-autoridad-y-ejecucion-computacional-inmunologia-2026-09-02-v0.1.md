# Acta de estratificación clínica, autoridad y ejecución computacional del dominio de inmunología

- **Versión:** 0.1
- **Fecha de corte:** 02-09-2026
- **Estatuto:** `RECTOR_DE_ARQUITECTURA_CLINICA_Y_EJECUCION`
- **Rama de trabajo:** `dominio-inmunologia`
- **Aplicación:** prospectiva a la normalización atómica, matrices, rutas, configuración institucional, episodios clínicos e implementación computacional

## 0. Objeto

Esta acta fija la separación obligatoria entre:

1. el núcleo general y transversal del dominio;
2. la composición clínica de ese núcleo;
3. la configuración propia de una institución sanitaria;
4. la instanciación protegida de un episodio clínico;
5. y la ejecución computacional subordinada.

Su finalidad es impedir dos inversiones de autoridad:

- que una decisión de programación determine, simplifique o sustituya una decisión clínica o semántica;
- que una singularidad institucional o individual se incorpore al núcleo general como si fuera conocimiento universal.

El dominio se orienta a la práctica clínica real. Debe ayudar al profesional autorizado que atiende un problema concreto, sin sustituir su juicio, sin ocultar incertidumbre y sin convertir la interacción en una carga administrativa adicional.

## 1. Relevancia y necesidad

Un sistema técnicamente correcto puede ser clínicamente inválido si su arquitectura se construye de espaldas a la práctica asistencial. Entre los fallos previsibles se encuentran:

- escoger como unidad computacional una entidad que no corresponde a una unidad clínica diferenciable;
- fusionar preguntas que producen decisiones distintas;
- imponer una dimensión por conveniencia de almacenamiento o interfaz;
- convertir la disponibilidad local de una prueba en necesidad clínica universal;
- omitir una dependencia crítica porque resulta difícil de representar;
- transformar una incertidumbre legítima en un valor por exigencia del programa;
- anteponer coste, velocidad o comodidad técnica a una restricción clínica no compensable;
- y presentar al profesional un inventario completo cuando sólo necesita conocer excepciones, ausencias o rutas activas.

La prevención de estos fallos no puede confiarse a la buena intención de una persona ni a la capacidad inferencial de un modelo. Debe quedar constituida mediante capas, autoridades, contratos y bloqueos verificables.

## 2. Exactitud y límite declarado

La atomización será exacta respecto del corte semántico declarado: cada unidad deberá tener identidad, frontera y criterio de diferenciación suficientes para no confundirse con otra unidad del mismo corte.

`EXACTA` no significa:

- exhaustiva para toda la medicina;
- definitiva frente a nueva evidencia;
- independiente del contexto clínico de activación;
- ni convertida todavía en observable, parámetro, matriz o decisión.

Un elemento permanece en `U` cuando no existe fundamento suficiente para constituir su frontera, dependencia o valor. La presión por terminar una implementación no autoriza a cerrar esa `U`.

## 3. Las cinco capas obligatorias

### 3.1. Capa A — núcleo atómico transversal

Contiene unidades semánticas generales, sus relaciones, fuentes, límites y procedencia. No contiene valores de pacientes, nombres de instituciones, marcas comerciales ni decisiones locales.

Un átomo declara qué distinción debe poder conservar el sistema. En las fases posteriores podrá relacionarse con observables y parámetros, pero no hereda automáticamente los `Pxx`, umbrales o dimensiones de los pilotos.

### 3.2. Capa B — composición clínica

Determina qué átomos o matrices deben concurrir para una operación clínica, bajo qué condiciones, con qué puentes, vetos, dependencias y preservaciones de `U`.

Esta capa contiene la lógica de las rutas. No contiene todavía los valores de un episodio individual ni permite a la inteligencia artificial improvisar una ruta alternativa.

### 3.3. Capa C — configuración institucional

Declara de manera versionada:

- cartera de servicios;
- pruebas y técnicas disponibles;
- circuitos de derivación;
- responsabilidades profesionales;
- protocolos internos;
- ventanas operativas;
- y restricciones materiales legítimas.

La configuración institucional condiciona la viabilidad y la forma de ejecutar una ruta, pero no altera el significado de los átomos ni convierte una limitación local en regla clínica universal.

### 3.4. Capa D — instanciación del episodio clínico

Contiene exclusivamente los valores, observaciones, temporalidad, preferencias clínicamente pertinentes y estados `U` de la persona atendida dentro de un episodio autorizado.

Esta capa está sometida a confidencialidad, mínimo privilegio, finalidad asistencial, trazabilidad de acceso y la política transversal de protección de datos. Sus valores no retroalimentan por sí solos el núcleo público ni se convierten en ejemplos reutilizables.

### 3.5. Capa E — ejecución computacional subordinada

La inteligencia artificial y el software:

- seleccionan únicamente rutas ya constituidas;
- reúnen los frames necesarios;
- aplican reglas declaradas;
- detectan ausencias, contradicciones y vetos;
- preservan `U`;
- explican la procedencia de cada salida;
- y se abstienen o escalan cuando falta autoridad, dato o regla.

No constituyen conocimiento clínico durante la ejecución, no sustituyen al profesional y no adquieren autoridad por haber calculado, recuperado o presentado una salida.

### 3.6. Regla terminológica sobre customización

En este dominio, `CUSTOMIZACION` no designa una modificación libre del conocimiento clínico. Se descompone obligatoriamente en:

1. `CONFIGURACION_INSTITUCIONAL`: adaptación declarativa, versionada y restringida al centro o red asistencial;
2. `INSTANCIACION_DE_EPISODIO`: asignación protegida de valores y estados a las posiciones previstas por el dominio para una persona atendida y una finalidad autorizada.

La presentación puede adaptarse al destinatario y al contexto, pero no modificar la indicación, el veto, la criticidad ni el significado clínico. Cualquier supuesta customización que no pueda clasificarse en uno de esos planos permanece en `U` y no se ejecuta.

## 4. Regla de no mutación entre capas

La relación entre las capas no es una mezcla ni una reescritura:

```text
resultado asistencial candidato =
    núcleo transversal
  + composición clínica aplicable
  + configuración institucional vigente
  + episodio clínico autorizado
  + permisos y bloqueos de ejecución
```

Cada término conserva su identidad y procedencia. En particular:

1. la institución configura, pero no redefine el núcleo;
2. el episodio instancia, pero no universaliza sus valores;
3. el software ejecuta, pero no crea autoridad clínica;
4. una restricción técnica o institucional no se disfraza de contraindicación clínica;
5. una necesidad clínica no se elimina porque el sistema todavía no pueda representarla;
6. una incompatibilidad entre capas produce `U`, abstención o escalado, nunca una aproximación silenciosa.

## 5. Distribución de autoridad

| Plano | Autoridad legítima | Competencia | Límite inviolable |
|---|---|---|---|
| clínico-profesional | profesionales y fuentes clínicas autorizadas | pertinencia, significado, consecuencias, suficiencia y decisión asistencial | no delegar la decisión clínica en software o estadística |
| semántico del dominio | procedimiento constitutivo trazable y revisión profesional | identidad, frontera, relaciones y composición de los objetos | no adoptar por mera conveniencia técnica |
| institucional | órganos y profesionales habilitados por la institución | protocolos, recursos, circuitos y permisos locales | no transformar una limitación local en verdad universal |
| ingeniería y seguridad | responsables técnicos competentes | representabilidad, corrección, seguridad, rendimiento, verificabilidad y bloqueo técnico | no modificar el contenido clínico para hacerlo programable |
| ejecución computacional | motor, lenguaje e inteligencia artificial dentro del contrato vigente | cálculo, recuperación autorizada, presentación, registro, abstención y escalado | ninguna autoridad clínica o semántica propia |
| episodio asistencial | profesional autorizado, con participación de la persona atendida conforme al marco aplicable | decisión concreta, información, consentimiento y seguimiento | no convertir preferencia en indicación ni omitirla cuando sea clínicamente pertinente |

### 5.1. Autoridad técnica de bloqueo

La ausencia de autoridad clínica de la ingeniería no elimina su responsabilidad. Una implementación insegura, ambigua, no verificable o incapaz de preservar el significado debe bloquearse.

La competencia en programación, arquitectura de software o ciencia de datos no constituye competencia clínica. En los planos clínico y semántico, la autoridad decisoria de la implementación es nula: no puede crear, eliminar, fusionar, graduar ni reordenar un objeto por conveniencia computacional.

El bloqueo técnico no decide qué es clínicamente correcto. Declara que el requisito no puede ejecutarse de forma válida en el estado técnico presente. La salida correcta es reparar la implementación, reformular el contrato sin cambiar su significado o conservar `U`; nunca alterar silenciosamente la necesidad clínica.

### 5.2. Autoridad clínica final

La salida computacional es un expediente de apoyo. La decisión asistencial corresponde al profesional autorizado, que puede aceptarla, rechazarla, completarla o apartarse de ella conforme a la clínica y dejando la trazabilidad exigible.

La participación de la persona atendida forma parte de la asistencia y del consentimiento informado. No convierte la medicina en elección de consumo ni permite seleccionar una actuación clínicamente improcedente.

## 6. Costes, tiempos y recursos

Coste, disponibilidad, demora, ocupación y carga organizativa son datos relevantes para la viabilidad y deben poder representarse en la configuración institucional.

No pueden:

- compensar matemáticamente un riesgo clínico grave;
- degradar un veto clínico no compensable;
- presentarse como fundamento clínico de una omisión;
- ni ocultarse cuando determinan que una ruta no puede ejecutarse localmente.

Cuando una necesidad clínica y una restricción material entren en conflicto, el sistema deberá mostrar ambas por separado y activar la alternativa autorizada: derivación, escalado, sustitución clínicamente validada, demora justificada o `U`. La resolución administrativa del conflicto queda fuera de la autoridad de la inteligencia artificial.

## 7. Utilidad sin carga administrativa

La interfaz y los frames seguirán un principio de divulgación progresiva y relevancia clínica:

1. permanecer en retaguardia hasta ser invocados o hasta detectar una condición crítica autorizada;
2. mostrar primero vetos, contradicciones, ausencias críticas y estados `U`;
3. presentar únicamente las matrices y rutas activas para el episodio;
4. permitir profundizar desde el resumen hasta el átomo, fuente, localizador y suceso;
5. evitar diccionarios, listados exhaustivos y recomendaciones genéricas no solicitadas;
6. no repetir información ya confirmada salvo cambio, conflicto o caducidad;
7. registrar la operación sin trasladar al profesional tareas que el sistema pueda ejecutar de forma segura.

Podrá existir un frame resumen derivado, pero nunca sustituirá los frames constitutivos ni ocultará una `U` crítica.

## 8. Experiencia, evidencia y revisión

La experiencia clínica o técnica puede descubrir un problema, formular un contraejemplo o revelar una necesidad que los documentos no muestran con claridad. No se convierte por sí sola en regla universal ni se traslada como caso atribuible.

Toda generalización deberá pasar por:

1. formulación impersonal;
2. contraste con el corpus profesional y las fuentes aplicables;
3. separación entre conocimiento general, configuración institucional y episodio;
4. adversarial interna;
5. adversarial externa;
6. y, cuando proceda, contraste empírico y revisión profesional o por pares.

La revisión posterior puede confirmar, modular, refutar o dejar en `U` una decisión. Hasta entonces, las limitaciones del corte se declaran; no se ocultan ni se compensan mediante autoridad aparente.

## 9. Invariantes verificables

Toda entrega posterior deberá demostrar:

- `INV-01`: ningún dato individual forma parte del núcleo atómico;
- `INV-02`: ninguna regla institucional modifica la identidad de un átomo;
- `INV-03`: ningún valor del episodio se reutiliza como conocimiento general sin un procedimiento independiente y legítimo;
- `INV-04`: ninguna decisión clínica nace de una conveniencia de implementación;
- `INV-05`: ninguna limitación técnica se presenta como conclusión clínica;
- `INV-06`: ninguna salida de la inteligencia artificial carece de ruta, fuente y autoridad trazables;
- `INV-07`: toda `U` crítica permanece visible y no compensable;
- `INV-08`: coste y recursos informan viabilidad, pero no sustituyen la lógica clínica;
- `INV-09`: la presentación es proporcional a la necesidad del episodio y permite profundización;
- `INV-10`: toda divergencia entre capas produce bloqueo, abstención o escalado explícitos;
- `INV-11`: la petición de ejemplos respeta la jerarquía de fuentes y la finalidad autorizada;
- `INV-12`: la implementación puede bloquear por seguridad o incorrección, pero no reescribir el requisito clínico.

## 10. Efecto sobre las fases vigentes

Esta acta:

- gobierna desde este corte `G2-SEM` y las fases posteriores;
- obliga a clasificar toda singularidad como dimensión transversal, configuración institucional o valor de episodio;
- obliga a separar el significado clínico de su representación computacional;
- y deberá acompañar la futura entrega de requisitos al Lenguaje SV.

No:

- añade preguntas a `G2-S1` o `G2-S2`;
- constituye observables, parámetros, umbrales, ventanas, matrices, rutas o frames;
- cierra `G2-SEM`;
- abre `G3-OBS`;
- modifica el Lenguaje SV;
- ni autoriza asistencia clínica.

## 11. Criterio de cambio

Una modificación de esta arquitectura exige un suceso explícito, versionado y trazable que identifique:

- regla afectada;
- motivo;
- evidencia o contraejemplo;
- capas implicadas;
- riesgo introducido;
- adversarial interna;
- y auditoría externa cuando la modificación afecte autoridad, privacidad, seguridad o decisión clínica.

No cabe alteración por inferencia conversacional, conveniencia de programación, disponibilidad de una nueva herramienta o costumbre local no documentada.

## 12. Declaración

El dominio clínico determina qué debe preservarse y por qué; la ingeniería determina cómo representarlo y ejecutarlo con seguridad; la configuración institucional declara dónde y con qué medios puede aplicarse; el episodio aporta los valores autorizados; y el profesional conserva la decisión asistencial.

La inteligencia artificial ocupa una posición ejecutora, explicativa y subordinada. Su utilidad depende de la fidelidad con la que preserve esta jerarquía, no de la amplitud con la que pueda improvisar.

## 13. Glosario operativo

| Término | Significado en esta acta |
|---|---|
| átomo | unidad semántica diferenciable cuya identidad y frontera deben preservarse |
| núcleo transversal | conjunto general de átomos, relaciones, fuentes y límites sin valores individuales ni reglas locales |
| composición clínica | unión tipada de unidades necesarias para una operación, con dependencias, vetos y `U` |
| configuración institucional | declaración versionada de protocolos, recursos, circuitos y permisos locales |
| instanciación del episodio | asignación protegida de valores y estados del caso actual a posiciones ya definidas |
| frame | representación de una matriz o composición que conserva su estado y permite inspección trazable |
| `U` | indeterminación legítima que no puede cerrarse sin fundamento suficiente |
| `G2-SEM` | puerta de formulación semántica de preguntas candidatas |
| `G3-OBS` | puerta posterior de constitución de observables; permanece cerrada en este corte |
| Lenguaje SV | lenguaje de computación del Sistema Vectorial SV, cuyo repositorio no se modifica desde este frente |
