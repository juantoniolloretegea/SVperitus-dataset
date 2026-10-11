# Prioridades documentales, Universo propietario y Universos relacionados

**Versión 1.0 · 11 de octubre de 2026 · Original en español.**

**Estado:** especificación documental para su incorporación al sistema. Su publicación no acredita que las funciones descritas estén implementadas, verificadas o disponibles en producción.

<a id="inicio-contenido-documental"></a>

## 1. Finalidad y ámbito

Esta especificación establece cómo clasificar los documentos de un Universo, determinar su precedencia y registrar su relación con otros Universos del Sistema Vectorial SV. La clasificación corresponde a un responsable cualificado y autorizado, antes de que los documentos se utilicen en consultas. El experto que consulta una IA ya evaluada no debe resolver estos registros en cada pregunta.

La finalidad es reducir errores de selección y de interpretación mediante reglas explícitas, reproducibles y auditables. Estas reglas ordenan fuentes; no descubren por sí mismas contradicciones, no certifican la verdad científica de una afirmación y no sustituyen la evaluación de una respuesta.

La precedencia actúa sobre afirmaciones incompatibles relativas al mismo asunto y ámbito de aplicación. Dos documentos pueden complementarse: una descripción general y otra más detallada no constituyen necesariamente una contradicción. La menor prioridad no convierte el conocimiento pertinente de un documento en prescindible.

La clasificación documental tampoco modifica la arquitectura del SV ni sus autoridades. Registrar, clasificar, consultar, transformar y suministrar un documento a una IA son operaciones distintas, sujetas a sus permisos y licencias.

## 2. Identidad del documento y pertenencia a un Universo

Cada documento tiene una identidad estable. Sus ediciones se distinguen mediante su referencia, fecha de publicación, procedencia y huella del original. Una representación de lectura o un fragmento preparado para una consulta permanecen vinculados a la edición de la que proceden.

El **Universo propietario** es el único Universo al que se asigna la responsabilidad documental principal. Se selecciona en el catálogo de Universos existente. Esta propiedad es organizativa: no equivale a titularidad de derechos de autor, no concede permisos y no convierte automáticamente el documento en maestro.

Los **Universos relacionados** son los demás Universos en los que ese documento tiene una relación de conocimiento declarada. Son opcionales y pueden ser varios. Cada relación remite a la misma identidad documental; no genera una copia independiente del original.

Un Universo puede ser propietario de muchos documentos. Un documento puede relacionarse con varios Universos y un Universo puede recibir relaciones de varios documentos. Por tanto, además de la pertenencia única, existe una relación múltiple entre documentos y Universos.

## 3. Ficha y ayuda para la clasificación

El campo **«Prioridad de documentos para la IA»** es obligatorio para cada incorporación de una edición al uso de un Universo. No tiene valor preseleccionado. Su ayuda debe mostrar estas tres opciones:

| Prioridad | Denominación | Significado |
| --- | --- | --- |
| 1 | Documento maestro | Fuente que el responsable designa como referencia principal para la materia y el ámbito declarados. |
| 2 | Documento relacionado de fuente diferente | Fuente independiente del documento maestro: otra autoría, entidad, editorial o procedencia. Permite aportar conocimiento y contrastarlo. |
| 3 | Anexo al documento maestro | Documento complementario vinculado expresamente a un maestro y a su edición. Amplía o desarrolla su contenido. |

**«Documento relacionado» y «Universo relacionado» designan relaciones diferentes.** El primero identifica una clase de fuente; el segundo, un destino de relación documental.

La ficha debe permitir registrar o consultar:

| Dato | Regla |
| --- | --- |
| Identidad y edición | Referencia inequívoca al documento y al original conservado. |
| Universo propietario | Uno y sólo uno, seleccionado expresamente. |
| Dominio del Universo | Se obtiene del catálogo y se muestra al seleccionar el Universo. |
| Universos relacionados | Selección opcional, sin repeticiones y sin incluir al propietario. |
| Prioridad en cada Universo de uso | Selección expresa entre 1, 2 y 3; no se hereda automáticamente del Universo propietario. |
| Fecha de publicación | Corresponde a la edición; se conserva su fuente y la precisión disponible. |
| Maestro del anexo | Obligatorio para prioridad 3, con identificación de su edición. |
| Orden de desempate | Se establece visualmente sólo cuando coinciden prioridad y fecha. |
| Orden de Universos relacionados | Se establece visualmente dentro de la lista de relaciones del documento. |

La prioridad pertenece al uso del documento en un Universo: una fuente puede ser principal en uno y complementaria en otro. La fecha de publicación, en cambio, es un dato de la edición y no cambia según el Universo.

Los permisos, la licencia, el alcance de uso y la revisión de las representaciones siguen formando parte de la gestión documental. Esta especificación no los sustituye.

## 4. Precedencia determinista dentro de un Universo

Entre las ediciones aplicables y autorizadas para una consulta, se aplica este orden:

1. **Prioridad:** 1 antes que 2, y 2 antes que 3.
2. **Fecha de publicación:** a igual prioridad, prevalece la edición publicada más recientemente.
3. **Orden de desempate confirmado:** a igual prioridad y fecha, prevalece el documento situado antes por el responsable.

La fecha de incorporación al sistema, la descarga o la modificación del archivo no sustituyen la fecha de publicación. La preferencia por actualidad es una regla documental adoptada; no demuestra por sí sola que una fuente reciente sea científicamente mejor.

La fecha debe contrastarse con la publicación o con una referencia acreditada. Si falta o su precisión no permite resolver una comparación, no se inventará un día ni se utilizará otra fecha de forma encubierta. La nueva incorporación permanecerá pendiente para ese uso hasta que el responsable resuelva y documente el dato necesario. El sistema no altera por ello la configuración anterior válida.

El orden se calcula y conserva en el sistema. No se deja a la IA decidirlo ni reinterpretarlo. La reproducibilidad se refiere a la selección y precedencia documentales con los mismos datos y permisos; no promete respuestas idénticas del modelo.

### Empates: una operación visual

Al seleccionar un Universo, el responsable puede ver los documentos existentes, abrir sus referencias y consultar sus prioridades y fechas. Los grupos empatados se muestran juntos y disponen de **«Subir»** y **«Bajar»**.

La persona ordena la lista y confirma el resultado. El sistema conserva posiciones únicas; no exige recordar códigos ni introducir números de desempate. Una ordenación visual por título u otra columna sólo facilita la consulta y no cambia la precedencia.

El movimiento que resuelve un empate queda limitado a su grupo. No permite colocar una prioridad 3 por delante de una prioridad 1 ni anular la regla de fecha. La incorporación de un nuevo miembro a un empate exige confirmar su posición: no se le atribuye preferencia por el orden de carga.

### Complementos, rectificaciones y discrepancias

La precedencia no debe ocultar una discrepancia pertinente ni impedir utilizar detalles compatibles de otras fuentes. Cuando una respuesta dependa de una discrepancia, debe identificar las fuentes, sus ediciones y la regla aplicada.

Un anexo que **rectifica** al maestro requiere un tratamiento expreso. No se admite como simple complemento subordinado si esa clasificación haría prevalecer el contenido ya corregido. El responsable debe identificar la rectificación y la referencia maestra vigente, que debe declarar expresamente la rectificación aplicable mediante su vínculo, conservando ambos originales. Mientras esa relación no esté resuelta, el conjunto no se habilita como si fuera coherente. Esta cautela no añade una cuarta prioridad ni autoriza a reescribir la fuente.

## 5. Selección y orden de los Universos relacionados

La selección se realiza mediante un desplegable del catálogo, con **nombre, código y dominio visibles**. El responsable no necesita memorizar códigos. Antes de confirmar, puede consultar los documentos del Universo elegido y reconocer el contexto en el que está incorporando la fuente.

El Universo propietario se muestra por separado. La lista de Universos relacionados permite añadir, retirar, subir y bajar relaciones. **La posición gráfica confirmada manda:** la primera expresa mayor preferencia que la siguiente dentro de esa lista. El sistema guarda ese mismo orden; no puede mostrar uno y suministrar otro.

Este orden:

- Pertenece a ese documento y a esa lista de relaciones.
- No constituye una jerarquía universal entre todos los Universos.
- No modifica la prioridad que el documento tiene en cada Universo.
- No obliga a recorrer todos los Universos ni a hacerlo secuencialmente.
- No concede acceso a otro dominio ni autorización de suministro.

Si una consulta reúne varios Universos, las precedencias locales no bastan para declarar automáticamente un vencedor global. Deben conservarse el Universo de procedencia, la clasificación y el alcance de cada fuente. Una incompatibilidad entre esos contextos no se resuelve suponiendo que el propietario o el primer Universo relacionado tiene siempre razón.

Retirar una relación no borra el documento. Cambiar de propietario exige una decisión expresa y registrada. No puede suprimirse un Universo dejando documentos sin propietario.

## 6. Incorporación, cambios y entrega a la IA

El recorrido previsto es sencillo:

1. Identificar el documento y su edición.
2. Seleccionar el Universo propietario y comprobar el dominio mostrado.
3. Consultar los documentos existentes y asignar la prioridad y la fecha acreditada.
4. Añadir, si procede, Universos relacionados, su orden y la clasificación del documento en cada uno.
5. Resolver los empates y las relaciones de anexos.
6. Revisar y confirmar la ficha; tramitar por separado los permisos de uso y suministro.

Una edición nueva se registra como tal. No sustituye silenciosamente el original ni modifica retrospectivamente las consultas anteriores. Deben revisarse los usos y autorizaciones afectados antes de emplearla.

Una consulta debe conservar qué ediciones, relaciones, prioridades y órdenes se aplicaron, junto con las autorizaciones y el contenido efectivamente preparado. La presentación gráfica por sí sola no basta: la información de precedencia tiene que acompañar de forma explícita al material suministrado.

La autorización de suministro corresponde a las figuras habilitadas en el dominio; el Árbitro-Director aplica esa decisión. La retirada de una autorización impide nuevas entregas, aunque una preparación anterior estuviera terminada. Los antecedentes de consultas ya realizadas se conservan.

La IA no puede modificar estas reglas a partir de instrucciones contenidas en un documento. Si falta material necesario, existe una discrepancia no resuelta o el alcance no permite concluir, la respuesta debe expresar esa limitación. La existencia de una clasificación no garantiza que el modelo la respete: su aplicación y la respuesta obtenida requieren comprobación.

## 7. Integridad y trazabilidad

La confirmación debe conservar conjuntamente la ficha, sus relaciones, las posiciones y la actuación correspondiente. Una interrupción no debe dejar media ordenación aplicada. Si otro responsable modifica la ficha durante una revisión, se debe advertir la diferencia y exigir una nueva confirmación, sin sobrescribirla silenciosamente.

Cada actuación conserva quién tenía autoridad, qué cambió, cuándo lo hizo, su motivo y los valores anteriores y posteriores. El acceso a ese historial respeta los permisos aplicables; la trazabilidad no exige publicar datos personales en los documentos de consulta general.

Deben impedirse, antes de activar un uso:

- La ausencia de propietario, los Universos inexistentes y las relaciones duplicadas.
- La inclusión del propietario entre los Universos relacionados.
- Las prioridades sin asignación expresa o fuera de los tres valores admitidos.
- Las fechas no resueltas, los empates pendientes y las posiciones repetidas.
- Los anexos sin maestro y edición identificados.
- Las sustituciones silenciosas de ediciones o los cambios sin autoridad suficiente.

La protección del registro reduce errores de almacenamiento y de operación. No convierte una clasificación humana equivocada en correcta.

## 8. Relación con las futuras rutas de conocimiento

Las referencias entre documentos y Universos preparan información útil para desarrollar las rutas de conocimiento del SV. **La importancia de una ruta depende de las consecuencias de omitir conocimiento necesario**, no exclusivamente de la prioridad de un documento ni de la posición de una relación.

El futuro recorrido puede requerir varios Universos, dependencias y bifurcaciones. Su algoritmo y sus criterios de validación deben definirse en su fase correspondiente, tras completar la constitución de los Universos del dominio conforme al proceso aplicable.

Esta especificación no define ese algoritmo, no declara rutas críticas operativas y no introduce puntuaciones de criticidad. Aporta identificadores estables, pertenencia, relaciones y trazabilidad que podrán utilizarse posteriormente. La lista ordenada de Universos relacionados no equivale a una ruta validada ni acredita por sí sola que se haya considerado todo el conocimiento necesario.

## 9. Persistencia prevista y comprobación de la implementación

Se propone conservar **[redb](https://docs.rs/redb/4.3.0/redb/)** como base de persistencia y aplicar estas reglas en Rust. redb proporciona almacenamiento transaccional de claves y valores; no es un gestor relacional que imponga automáticamente las relaciones aquí descritas. La aplicación debe comprobar las referencias, la unicidad, la autoridad y los órdenes.

No se justifica incorporar DuckDB únicamente para esta función. Su posible uso analítico puede evaluarse por separado si aparece una necesidad concreta. Esta decisión evita una sustitución sin beneficio demostrado; no constituye una comparación experimental de rendimiento entre motores.

Antes de declarar disponibles las funciones, la implementación debe acreditar al menos:

| Comprobación | Resultado exigido |
| --- | --- |
| Igual entrada documental y mismas autorizaciones | Misma precedencia calculada. |
| Incorporación y modificación de relaciones | Propietario único, referencias válidas y ausencia de duplicados. |
| Desempate y reordenación | Correspondencia entre posición confirmada, registro conservado y datos suministrados. |
| Fecha insuficiente o anexo rectificativo sin resolver | Nueva incorporación pendiente para el uso afectado. |
| Dos modificaciones concurrentes | Detección del cambio previo, sin sobrescritura inadvertida. |
| Interrupción durante una confirmación | Estado íntegro anterior o nuevo, con su actuación coherente. |
| Nueva edición o retirada de autorización | Antecedentes preservados y nuevas entregas sometidas al estado vigente. |
| Respuesta basada en varias fuentes | Referencias cotejables, complementos conservados y discrepancias pertinentes visibles. |

Estas comprobaciones se enuncian como requisitos pendientes de acreditación. El documento no comunica resultados de ensayos que no se hayan realizado.

<a id="fin-contenido-documental"></a>

## 10. Referencias documentales

- [Manifiesto de arquitectura, derechos, obligaciones, garantías y fundamentos del Sistema Vectorial SV, V1](../../MANIFIESTO_DE_ARQUITECTURA_DERECHOS_OBLIGACIONES_GARANTIAS_Y_FUNDAMENTOS_DEL_SISTEMA_VECTORIAL_SV_V1.md).
- [Acta de evaluación y recepción documental sobre rutas de conocimiento del SV, de 14 de septiembre de 2026](../ACTA_EVALUACION_Y_RECEPCION_DOCUMENTAL_RUTAS_CONOCIMIENTO_SV_2026_09_14.md).
- [Reglas, usos y descripciones documentales de documentos para el conocimiento de la IA](https://documentos-sv.itvia.online/documentacion/reglas-usos-descripciones-documentales/index.html). Referencia editorial: V.05. Fuentes del libro: [finalidad](https://github.com/IA-en/biblioteca-documental/blob/f30a94701d921d3734c109ccbe1c50c5db03c411/libros/visualizadores/src/finalidad.md), [entrega](https://github.com/IA-en/biblioteca-documental/blob/f30a94701d921d3734c109ccbe1c50c5db03c411/libros/visualizadores/src/entrega.md) y [revisión](https://github.com/IA-en/biblioteca-documental/blob/f30a94701d921d3734c109ccbe1c50c5db03c411/libros/visualizadores/src/revision.md).
- [Documentación de redb](https://docs.rs/redb/4.3.0/redb/).

## 11. Autoría, derechos y condiciones de uso

© 2026. Algunos derechos reservados. La identidad de la autoría, su atribución y los fundamentos de titularidad se conservan en la [declaración de derechos del repositorio](../../LICENSE) y en el [Manifiesto del Sistema Vectorial SV](../../MANIFIESTO_DE_ARQUITECTURA_DERECHOS_OBLIGACIONES_GARANTIAS_Y_FUNDAMENTOS_DEL_SISTEMA_VECTORIAL_SV_V1.md), a los que remite expresamente este documento.

**Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) · IA eñ™ – La Biblia de la IA™ · ISSN 2695-6411 · Identificador de autoría: [ORCID 0000-0002-6634-3351](https://orcid.org/0000-0002-6634-3351).**

Se aplica la licencia **Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0)**, conforme a la declaración del repositorio y a su [texto jurídico completo](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.es). Deben respetarse la atribución y las condiciones de uso no comercial y de distribución sin obras derivadas, salvo autorización específica del titular.

La cita, custodia o utilización documental no atribuye al receptor la autoría, la titularidad intelectual ni la paternidad del Sistema Vectorial SV. Este texto no modifica la arquitectura, los derechos, las obligaciones ni las reservas establecidos en el Manifiesto.

Las fuentes citadas y las herramientas conservan sus respectivas licencias. La clasificación o relación de un documento no amplía los derechos sobre su contenido, ni autoriza por sí sola su transformación o entrega a una IA.
