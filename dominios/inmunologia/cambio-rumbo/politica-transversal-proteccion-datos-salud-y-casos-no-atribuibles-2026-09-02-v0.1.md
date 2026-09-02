# Política transversal de protección de datos de salud y casos no atribuibles v0.1

- **Fecha:** 02-09-2026
- **Estatuto:** `RECTOR_DE_PROTECCION`
- **Aplicación:** prospectiva a todo objeto nuevo o modificado del dominio de inmunología
- **Ámbito:** repositorio público, revisiones externas, artefactos intercambiados y servicios de inteligencia artificial

## 1. Regla constitutiva

Ningún objeto público contendrá datos de salud de una persona real identificada o razonablemente identificable. La prohibición comprende la identificación directa y la reidentificación por combinación de datos, relaciones, cargos, cronologías, centros, tratamientos, diagnósticos, sucesos clínicos, metadatos o contexto externo.

La seudonimización no se tratará como anonimización. Sustituir un nombre por un cargo, inicial, alias, identificador o descripción relacional no saca el dato del ámbito de protección cuando la persona pueda ser singularizada directa o indirectamente.

## 2. Casos permitidos en objetos públicos

Sólo podrán utilizarse:

1. casos sintéticos construidos para probar una regla y no derivados narrativamente de una persona concreta;
2. contraejemplos abstractos sin atribución personal, institucional o temporal reidentificadora;
3. datos agregados cuya desagregación no permita razonablemente identificar a una persona;
4. información publicada en fuentes científicas o normativas, citada para su finalidad bibliográfica y sin añadir vínculos reidentificadores.

Un caso sintético no conservará una combinación singular de diagnóstico, tratamiento, fecha, centro, secuencia asistencial, resultado o conducta que reproduzca la huella de un caso real conocido.

## 3. Contenido prohibido

No se publicarán:

- nombres, iniciales, alias, identificadores clínicos o administrativos;
- cargos, relaciones o funciones usados como sustitutos de identidad en conexión con información sanitaria;
- hospitales, profesionales, localidades o fechas vinculables a un episodio individual;
- diagnósticos, tratamientos, pruebas, resultados o decisiones enlazados a una persona real;
- citas de conversación, relatos autobiográficos o historiales aportados para razonar;
- combinaciones de cuasi-identificadores que permitan singularización;
- datos bajo acuerdo de uso, acceso restringido o deber de confidencialidad;
- metadatos ocultos, propiedades documentales, comentarios, historial de revisión, nombres de archivo, EXIF o campos de hoja de cálculo que revelen lo anterior.

Tampoco se redactarán negaciones protectoras que, al negar la presencia de una persona o caso concreto, revelen o refuercen precisamente ese vínculo. La protección se expresará siempre como regla general e impersonal.

## 4. Separación entre conocimiento y dato de paciente

Las estructuras del dominio, preguntas, parámetros, consecuencias, rutas y frames se construirán a partir de conocimiento profesional, evidencia autorizada y casos sintéticos adversariales. Un relato clínico real puede motivar una pregunta durante el trabajo privado, pero no se trasladará, resumirá, citará ni hará reconocible en el objeto público.

La trazabilidad científica conservará fuente, versión, localizador y decisión metodológica. No conservará la identidad de quien aportó un ejemplo clínico ni una cadena que permita reconstruirla.

La arquitectura separará tres planos que no se fusionan:

| Plano | Contenido | Régimen |
|---|---|---|
| conocimiento público | dominio, fuentes, estructuras y casos sintéticos | publicable tras compuerta de privacidad |
| configuración institucional | protocolos internos, capacidades, circuitos y reglas locales | acceso restringido y versionado por institución |
| episodio clínico | datos identificables o seudonimizados de una persona atendida | entorno asistencial autorizado, mínimo privilegio y trazabilidad de acceso |

La customización del episodio puede consultar los tres planos dentro del entorno autorizado, pero no los convierte en un único almacén ni autoriza transportar información del episodio al plano público.

## 5. Compuerta previa a publicación

Antes de cada publicación o actualización pública se ejecutará una revisión separada sobre:

1. texto visible;
2. tablas, fórmulas, comentarios y celdas ocultas;
3. nombres de archivos, carpetas e identificadores;
4. propiedades de documentos y hojas de cálculo;
5. imágenes y metadatos EXIF;
6. archivos comprimidos y manifiestos;
7. mensajes de commit y descripciones;
8. informes adversariales externos antes de incorporarlos;
9. posibilidad de reidentificación por combinación con la autoría, el repositorio y otras fuentes públicas.

Los estados posibles son:

| Estado | Efecto |
|---|---|
| `PRIVACIDAD_PASA` | puede continuar la publicación del objeto |
| `PRIVACIDAD_REPARAR` | se detiene la publicación hasta eliminar o generalizar el contenido |
| `PRIVACIDAD_U` | la identificabilidad no puede descartarse; no se publica |
| `PRIVACIDAD_NO_PASA` | contiene información incompatible con el repositorio público |

## 6. Revisiones externas y servicios de IA

Las órdenes de auditoría serán impersonales. Las respuestas externas no se incorporarán mecánicamente: antes pasarán por la compuerta de privacidad y, si procede, se registrará una recepción normalizada que preserve el resultado técnico sin reproducir datos o atribuciones innecesarias.

No se introducirán datos clínicos reales en un servicio externo de IA, aunque estén seudonimizados, salvo entorno expresamente habilitado, base jurídica, contrato, control de acceso y evaluación de protección adecuados. La disponibilidad técnica de un conector o cuenta no constituye autorización para tratar datos sanitarios.

No se presume que una IA conozca, recuerde o aplique correctamente el régimen de protección. Su capacidad para explicar una norma no constituye un control de seguridad. La IA no decide la licitud, finalidad, minimización, conservación, comunicación, publicación o transferencia de un dato sanitario.

Esas decisiones corresponden a controles externos al modelo y no anulables por inferencia:

- clasificación previa del dato y finalidad autorizada;
- control de acceso y mínimo privilegio;
- separación entre datos, configuración institucional y conocimiento público;
- filtrado de entrada y salida;
- prohibición por defecto de Internet y conectores externos durante un episodio clínico real;
- control de registros, telemetría, cachés, copias, índices, embeddings y bases vectoriales;
- revisión humana y técnica antes de cualquier exportación;
- registro auditable de acceso, transformación y destino.

Ante una duda, conflicto o ausencia de autorización, el sistema conserva `PRIVACIDAD_U`, bloquea la salida y no solicita al modelo que resuelva la incertidumbre mediante razonamiento probabilístico.

## 7. Solicitud de ejemplos durante la práctica clínica

La petición «necesito ejemplos» activa una operación gobernada y no una búsqueda libre. Antes de responder, controles externos al modelo verificarán:

1. identidad y función de quien solicita;
2. relación asistencial o finalidad autorizada;
3. episodio y ámbito de acceso;
4. clase de ejemplo necesaria;
5. fuente permitida y destino de la respuesta.

La condición de profesional sanitario no concede acceso general a historias ajenas ni autoriza nuevas finalidades, exportaciones o transferencias. El acceso se limita por necesidad, relación asistencial, función, institución y finalidad previamente habilitada.

### 7.1. Jerarquía de fuentes permitidas

| Prioridad | Tipo de ejemplo | Condición |
|---:|---|---|
| 1 | sintético | construido sin derivación narrativa de una persona real y rotulado `SINTETICO` |
| 2 | publicado | procedente de literatura pública autorizada, con cita y localizador, rotulado `PUBLICADO` |
| 3 | agregado | estadística o patrón no reidentificable y autorizado, rotulado `AGREGADO` |
| 4 | institucional | biblioteca expresamente aprobada, anonimizada o sometida al régimen jurídico y control de acceso aplicables, rotulada `INSTITUCIONAL_AUTORIZADO` |

La IA no consultará historias clínicas de otras personas, recuperará vecinos clínicos, reutilizará conversaciones, buscará coincidencias en registros asistenciales ni compondrá un caso a partir de datos reales salvo que exista una función institucional específica, autorizada, auditada y limitada a esa finalidad.

### 7.2. Uso del episodio actual

Los datos de la persona atendida pueden emplearse dentro de su propio episodio únicamente para la finalidad asistencial autorizada. No se convierten por ello en ejemplo reutilizable, material docente, caso público, memoria del sistema o entrada para otra consulta.

Cuando el ejemplo se destine a explicar una opción a la propia persona atendida, la salida se mantiene dentro del entorno asistencial y distingue con claridad:

- datos del episodio actual;
- ejemplo sintético ilustrativo;
- evidencia publicada;
- incertidumbre no resuelta.

### 7.3. Conducta de la IA

Si la finalidad o la fuente no están determinadas, la IA solicita aclaración o utiliza exclusivamente un ejemplo sintético mínimo. No inventa que un caso es real, no presenta un ejemplo como evidencia y no oculta su procedencia.

Cada respuesta con ejemplos conserva, como mínimo: tipo, fuente o generador autorizado, versión, finalidad, episodio cuando proceda, control de acceso y registro de salida. Ninguna petición conversacional puede levantar por sí sola estos límites.

## 8. Fuentes restringidas y datos de investigación

Los datos sujetos a acuerdo de uso, comité de acceso, secreto profesional, consentimiento o régimen de investigación permanecerán en el entorno autorizado. El repositorio público sólo podrá conservar metadatos no sensibles, referencias y resultados agregados permitidos por la fuente y por la normativa aplicable.

La apertura científica no prevalece sobre la confidencialidad ni convierte datos sanitarios en material libremente redistribuible.

## 9. Incidente o hallazgo posterior

Ante una posible exposición se detendrá la nueva difusión, se identificará el perímetro exacto y se decidirá la medida proporcional. La retirada del estado visible no se confundirá con borrado histórico: commits, cachés, forks, copias y artefactos externos se evaluarán por separado. Cualquier reescritura de historial requerirá una operación específica, controlada y verificada.

El registro público de la reparación será mínimo e impersonal; no repetirá el contenido que pretende proteger.

## 10. Base normativa

Esta política adopta un criterio preventivo compatible con:

- Reglamento (UE) 2016/679 —RGPD—: considerando 26; artículos 4, 5, 9, 25 y 32;
- Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales —LOPDGDD—;
- obligaciones adicionales de confidencialidad, secreto profesional, investigación biomédica y acuerdos de uso que resulten aplicables a cada fuente.

La política no constituye por sí sola una evaluación jurídica de un tratamiento concreto. Cuando exista dato real, acceso restringido, transferencia o duda de identificabilidad, la salida correcta es `PRIVACIDAD_U` y la operación pública se detiene.

## 11. Declaración

La protección de datos es una condición de entrada y publicación, no un añadido editorial posterior. Ninguna utilidad científica o técnica compensa la exposición de datos de salud identificables o razonablemente reidentificables.
