# Adenda sobre contrato epistémico, inferencia trazable y consecuencias de la inteligencia artificial en inmunología

- **Versión:** 0.1
- **Fecha de corte:** 02-09-2026
- **Estatuto:** `RECTOR_CANDIDATO_DE_EJECUCION_EPISTEMICA`
- **Rama de trabajo:** `dominio-inmunologia`
- **Acta que refina:** `acta-estratificacion-clinica-autoridad-y-ejecucion-computacional-inmunologia-2026-09-02-v0.1.md`
- **Aplicación:** ejecución clínica futura, generación de consejo, actualización del conocimiento y entrega de requisitos al Lenguaje SV

## 0. Objeto

Esta adenda completa el contrato de la capa E —ejecución computacional subordinada— mediante cuatro exigencias inseparables:

1. conocimiento de dominio preconstituido y suficiente para la operación;
2. prohibición de inferencia clínica opaca;
3. vinculación explícita entre razonamiento, error y consecuencias;
4. prohibición de emitir consejo sin trazabilidad justificativa completa.

La adenda no atribuye conciencia, intención ni conocimiento humano a la inteligencia artificial. Convierte esas exigencias en condiciones externas, verificables y no anulables por el modelo.

## 1. Conocimiento completo respecto de una operación

La inteligencia artificial no se apoyará en la presunción de que sus pesos, memoria conversacional o capacidad lingüística contienen «toda la inmunología».

Antes de ejecutar una operación clínica deberá disponer del corpus de dominio:

- cerrado para esa operación;
- versionado e identificado por huella;
- autorizado para el contexto de uso;
- suficiente respecto de las preguntas y dependencias obligatorias declaradas;
- con fuentes y localizadores vigentes;
- con sus incertidumbres explícitas;
- y con las consecuencias aplicables constituidas hasta el grado exigido por la operación.

El estado admisible se denomina:

`CORPUS_COMPLETO_RESPECTO_DE_LA_OPERACION`

No significa conocimiento universal, definitivo o exhaustivo de la inmunología. Significa que, para una operación identificada y un corte versionado, están presentes todos los objetos que el propio dominio declara obligatorios, y que cualquier hueco conocido permanece registrado como `U`.

### 1.1. Conocimiento externo al modelo

El conocimiento clínico gobernante residirá en objetos externos inspeccionables:

- átomos;
- relaciones tipadas;
- matrices;
- rutas;
- fuentes y localizadores;
- reglas de activación;
- consecuencias;
- restricciones;
- versiones;
- y sucesos de decisión.

La memoria paramétrica o conversacional del modelo no constituye fuente, regla ni autoridad. Puede facilitar lenguaje, recuperación o correspondencia candidata, pero ninguna de esas operaciones adquiere efecto clínico hasta quedar resuelta contra el corpus autorizado.

## 2. Suficiencia relativa previa

La ejecución sólo podrá comenzar cuando exista una declaración verificable:

`SUFICIENCIA_RELATIVA_CONSTITUIDA`

Como mínimo deberá vincular:

1. `Operacion_ID`;
2. versión y huella del corpus;
3. perímetro profesional y clínico aplicable;
4. conjunto de átomos y dependencias obligatorias;
5. rutas admitidas y prohibidas;
6. consecuencias constituidas;
7. incertidumbres conocidas;
8. configuración institucional vigente;
9. permisos y finalidad del episodio;
10. y autoridad habilitada para recibir la salida.

La ausencia de uno de esos elementos no se corrige mediante inferencia probabilística. Produce `U`, abstención o escalado según la regla aplicable.

## 3. Prohibición de inferencia clínica opaca

Ninguna inferencia tendrá efecto clínico por proceder de un modelo, por resultar plausible o por coincidir con una respuesta habitual.

Una transición clínicamente utilizable deberá estar previamente tipada o quedar sometida a validación antes de su uso. Su traza justificativa contendrá, como mínimo:

- identificadores de las entradas utilizadas;
- procedencia y estado de cada entrada;
- átomo, matriz y ruta activados cuando existan;
- identificador y versión de la regla aplicada;
- precondiciones satisfechas y no satisfechas;
- transformación ejecutada;
- resultado obtenido;
- alternativas excluidas y motivo;
- estados `U` preservados;
- consecuencias de acción, omisión, error o cierre ilegítimo que resulten aplicables;
- configuración institucional que condiciona la viabilidad;
- autoridad y finalidad de la salida;
- y sello de versión y tiempo.

Si una transición no puede producir esa traza, su resultado no es clínicamente admisible.

### 3.1. Doble registro obligatorio

La ejecución clínica conservará dos objetos diferentes y vinculados:

1. `CADENA_PRIVADA_DE_DELIBERACION`: registro confidencial de la secuencia deliberativa explícita producida por el modelo, incluidos pasos intermedios emitidos, hipótesis consideradas, descartes, llamadas a herramientas, resultados recuperados y mensajes de control que hayan intervenido materialmente;
2. `TRAZA_JUSTIFICATIVA_ESTRUCTURADA`: proyección canónica, reproducible y verificable de entradas, átomos, reglas, fuentes, transiciones, `U`, consecuencias, versiones y autoridad.

El primer objeto corresponde a la cadena privada de pensamiento del modelo en cuanto ésta se manifiesta como deliberación explícita y técnicamente capturable. Se denomina operativamente `CADENA_PRIVADA_DE_DELIBERACION` para no fingir acceso causal completo a activaciones internas no observables.

La cadena privada cumple una función forense y de auditoría. La traza estructurada cumple la función normativa y justificativa. Ninguna sustituye a la otra.

La cadena privada:

- no se mostrará por defecto al profesional ni a la persona atendida;
- se tratará con el mismo nivel de protección que el episodio cuando pueda contener o revelar datos de éste;
- tendrá acceso, conservación, finalidad y borrado gobernados;
- no se reutilizará como entrenamiento o memoria de otro episodio;
- y no se presentará como explicación causal completa de las activaciones internas del modelo.

El sistema sólo declarará capturada una cadena privada cuando el entorno técnico permita registrar materialmente la deliberación explícita. No fingirá acceso a estados internos no observables. Si no puede capturarla en una operación para la que sea obligatoria, conservará `CADENA_PRIVADA_U` y no emitirá consejo.

Ambos objetos se vincularán mediante identificadores de ejecución y de suceso. Una discrepancia material entre la cadena privada y la traza estructurada produce bloqueo, investigación y `U`; no se resuelve eligiendo la narración más convincente.

Una explicación narrativa generada después del resultado tampoco constituye trazabilidad si no reproduce los identificadores, reglas y sucesos realmente ejecutados. Añadir citas a posteriori no transforma una inferencia opaca en una transición gobernada.

## 4. Contrato de consecuencias

El sistema no presupone que la inteligencia artificial sea consciente de las consecuencias. Exige que cada operación consulte y preserve estructuras de consecuencias constituidas.

Para una salida clínica candidata deberán distinguirse, cuando sean aplicables:

- consecuencia de actuar;
- consecuencia de omitir;
- consecuencia de retrasar;
- consecuencia de seleccionar una ruta incorrecta;
- consecuencia de cerrar indebidamente una `U`;
- consecuencia de usar conocimiento caducado;
- y consecuencia de exceder autoridad, finalidad o ámbito de acceso.

La consecuencia deberá conservar fuente, mecanismo, condiciones, gravedad, límites, versión y autoridad de revisión. No se inventará durante el episodio para justificar una conclusión ya producida.

Cuando una consecuencia necesaria no esté constituida, el estado será:

`CONSECUENCIA_U`

Una `CONSECUENCIA_U` crítica impide emitir consejo y obliga a abstención o escalado.

## 5. Compuerta de consejo

El consejo de la inteligencia artificial no es decisión asistencial. Sólo puede presentarse como expediente de apoyo cuando concurran todas las condiciones siguientes:

```text
CONSEJO_ADMISIBLE =
    operacion_identificada
  ∧ corpus_vigente_y_suficiente
  ∧ entradas_trazables
  ∧ cadena_privada_de_deliberacion_capturada
  ∧ ruta_constituida
  ∧ transiciones_reproducibles
  ∧ consecuencias_evaluadas
  ∧ configuracion_institucional_vigente
  ∧ autoridad_y_finalidad_validas
  ∧ privacidad_superada
  ∧ ausencia_de_U_critica_no_permitida
```

Si una condición no se satisface, la salida será:

`NO_EMITIR_CONSEJO`

El sistema deberá indicar qué condición falta, qué `U` permanece y cuál es la vía autorizada de escalado o reparación. No rellenará el hueco con conocimiento latente, una búsqueda libre o una respuesta genérica.

## 6. Actualización y consulta externa

El corpus se constituye antes del episodio. No aprende ni se modifica silenciosamente durante la asistencia.

Una consulta externa solicitada y autorizada seguirá un procedimiento separado:

1. retirar de la consulta cualquier dato del episodio que no sea imprescindible y esté legítimamente autorizado;
2. limitar la búsqueda a fuentes y conectores permitidos;
3. registrar consulta, versión, fecha y resultado;
4. ingresar el hallazgo en cuarentena;
5. someterlo a los filtros documentales, clínicos, semánticos, de privacidad y de contradicción establecidos;
6. obtener aceptación por la autoridad correspondiente;
7. constituir un nuevo suceso versionado;
8. y sólo después habilitar su uso como conocimiento del dominio.

Un hallazgo externo no incorporado podrá mostrarse únicamente como evidencia externa pendiente, claramente separada del corpus vigente y sin alterar automáticamente la ruta. La consulta no transportará datos del episodio a Internet o a servicios externos fuera del régimen autorizado.

## 7. Forma mínima de la justificación

Toda salida candidata a consejo deberá poder proyectarse en un expediente con, al menos, los campos siguientes:

| Campo | Función |
|---|---|
| `Operacion_ID` | operación clínica a la que responde |
| `Corte_dominio` | versión y huella del corpus utilizado |
| `Entradas` | datos utilizados, procedencia, estado y autorización |
| `Objetos_activados` | átomos, matrices y relaciones realmente utilizados |
| `Ruta_ID` | ruta constituida, si existe |
| `Reglas_aplicadas` | identificadores y versiones de las transiciones |
| `Cadena_privada_ID` | vínculo con el registro confidencial de deliberación y ejecución |
| `U_preservadas` | incertidumbres no cerradas |
| `Consecuencias` | efectos aplicables de acción, omisión, retraso y error |
| `Contexto_institucional` | restricciones de viabilidad sin reescritura clínica |
| `Privacidad_y_acceso` | finalidad, rol, permisos y destino |
| `Salida` | resultado, abstención o escalado |
| `Autoridad_pendiente` | decisión profesional que no pertenece al sistema |

La representación final podrá ser concisa para no sobrecargar al profesional. La concisión de la interfaz no autoriza a perder la traza subyacente.

## 8. Invariantes de ejecución epistémica

- `INV-EPI-01`: ningún conocimiento latente del modelo gobierna por sí solo una salida clínica.
- `INV-EPI-02`: toda operación se vincula a un corpus versionado y con huella.
- `INV-EPI-03`: la completitud se declara respecto de una operación, nunca respecto de toda la inmunología.
- `INV-EPI-04`: toda transición clínicamente utilizable es identificable, reproducible y auditable.
- `INV-EPI-05`: ni la cadena privada ni una explicación o cita a posteriori sustituyen la traza justificativa estructurada.
- `INV-EPI-06`: toda consecuencia aplicable se vincula a fuente, mecanismo, condiciones y límites.
- `INV-EPI-07`: una `CONSECUENCIA_U` crítica impide consejo.
- `INV-EPI-08`: ninguna `U` crítica se cierra por valor predeterminado, imputación opaca o presión operativa.
- `INV-EPI-09`: ninguna consulta externa modifica el corpus durante el episodio sin cuarentena, filtros y aceptación.
- `INV-EPI-10`: ningún dato del episodio se reutiliza para aprendizaje o actualización sin finalidad y régimen independientes.
- `INV-EPI-11`: toda salida candidata identifica versión, entradas, ruta, reglas, consecuencias, `U` y autoridad pendiente.
- `INV-EPI-12`: la concisión del frame no reduce la trazabilidad disponible bajo inspección.
- `INV-EPI-13`: el profesional recibe un expediente de apoyo, no una decisión automática.
- `INV-EPI-14`: toda ejecución clínica conserva cadena privada de deliberación y traza justificativa estructurada, vinculadas por identificadores de suceso.
- `INV-EPI-15`: la ausencia o discordancia material de cualquiera de los dos registros bloquea el consejo.
- `INV-EPI-16`: la cadena privada se protege como dato del episodio y no se reutiliza como entrenamiento, memoria o ejemplo.

## 9. Efecto sobre el dominio vigente

Esta adenda refina prospectivamente la fila de ejecución computacional del acta de estratificación. La formulación completa pasa a ser:

| Plano | Condición rectora |
|---|---|
| inteligencia artificial | subordinada a rutas, fuentes y autorizaciones constituidas; opera sobre el corpus completo respecto de la operación; no realiza inferencia clínica opaca; conserva cadena privada de deliberación y traza justificativa estructurada; preserva consecuencias y no emite consejo sin ambos registros completos y concordantes |

No:

- declara completo el dominio actual;
- cierra `G2-SEM`;
- abre `G3-OBS`;
- constituye consecuencias clínicas concretas;
- crea parámetros, observables, matrices, rutas o frames;
- incorpora una fuente encontrada durante un episodio;
- modifica el Lenguaje SV;
- ni autoriza asistencia clínica.

## 10. Criterio de cierre

Esta adenda permanece como `RECTOR_CANDIDATO_DE_EJECUCION_EPISTEMICA` hasta superar adversarial interna y auditoría externa.

El cierre exigirá demostrar, al menos:

1. que no presume conocimiento universal;
2. que no confunde memoria del modelo con corpus autorizado;
3. que conserva una cadena privada de deliberación sin presentarla como prueba normativa ni como acceso completo a estados neuronales internos;
4. que la vincula con una justificación estructurada verificable y bloquea sus discordancias;
5. que impide consejo ante cadena privada, traza o consecuencia crítica incompletas;
6. que permite actualización sin aprendizaje silencioso durante el episodio;
7. y que no abre prematuramente objetos de fases posteriores.

## 11. Glosario

| Término | Significado |
|---|---|
| corpus | conjunto externo, versionado y autorizado de objetos de dominio |
| suficiencia relativa | completitud respecto de una operación y un corte declarados |
| inferencia opaca | resultado clínico cuyo tránsito real no puede reconstruirse mediante reglas y sucesos verificables |
| cadena privada de deliberación | registro confidencial de los pasos explícitos, herramientas, resultados y controles que intervinieron en la ejecución, sin pretensión de describir completamente activaciones neuronales internas |
| traza justificativa | expediente estructurado de entradas, reglas, transiciones, resultados, `U`, consecuencias y autoridad |
| consecuencia | efecto constituido de acción, omisión, demora, error o cierre ilegítimo bajo condiciones declaradas |
| consejo | salida explicativa de apoyo sometida a compuerta; no equivale a decisión clínica |
| cuarentena | estado en el que una fuente o hallazgo nuevo no puede gobernar la ejecución |

## 12. Declaración

La inteligencia artificial sólo es clínicamente útil cuando el dominio gobernante existe antes de la ejecución, se conservan y concuerdan la cadena privada de deliberación y la traza justificativa estructurada, cada transición puede reconstruirse y cada consecuencia aplicable permanece vinculada al razonamiento. La fluidez lingüística, la plausibilidad o la cita retrospectiva no sustituyen esas condiciones.
