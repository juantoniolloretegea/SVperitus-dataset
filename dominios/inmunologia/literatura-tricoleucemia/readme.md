# Fuentes documentales sobre tricoleucemia

## Objetivo

Esta colección reúne dos fuentes sobre leucemia de células pilosas, también denominada tricoleucemia, en un formato HTML común, legible sin conexión y con procedencia verificable. Su finalidad es facilitar la recuperación documental, la localización de pasajes y el estudio comparado de respuestas fundamentadas en fuentes explícitas. La uniformidad de presentación permite reducir diferencias instrumentales de lectura entre una página web y un PDF; no establece equivalencia de contenido, fecha, destinatario ni fuerza de la evidencia.

La preparación constituye una actuación de conservación y acceso documental. No incorpora por sí misma conocimiento validado al Sistema Vectorial, no sustituye la recepción científica de las fuentes ni acredita aptitud clínica de un modelo. La fuente NCI se relaciona con el material utilizado en ensayos documentales de GPT-OSS Safeguard; esta captura nueva no sustituye ni se declara idéntica a la caché prefijada de una prueba anterior.

## Fuentes conservadas

| Carpeta | Fuente y destinatario | Fecha declarada por la fuente | Contenido |
|---|---|---|---|
| [NCI: versión para profesionales](nci-pdq-profesionales/index.html) | Instituto Nacional del Cáncer; profesionales de salud | 14 de noviembre de 2024; captura del 3 de octubre de 2026 | Artículo íntegro, cinco secciones principales, bibliografía, fecha y condiciones de uso; respuesta HTML original |
| [LLS: hoja informativa](lls-hoja-informativa-2018/index.html) | Sociedad de Lucha contra la Leucemia y el Linfoma; pacientes, cuidadores y profesionales médicos | Agosto de 2018, según «FS16S 8/18» | Diez páginas convertidas a HTML, texto con localizadores, reproducciones visuales y PDF original aportado |

La primera fuente es [Tratamiento de la leucemia de células pilosas (PDQ®)–Versión para profesionales de salud](https://www.cancer.gov/espanol/tipos/leucemia/pro/tratamiento-celulas-pilosas-pdq), publicada originalmente por el Instituto Nacional del Cáncer. Se conserva como captura histórica, no como una publicación oficial mantenida al día. La descarga comprende el artículo y la respuesta HTML recibida; los documentos externos citados no forman parte de la descarga.

La segunda fuente es *Leucemia de células peludas*, hoja informativa FS16-S de LLS. El [PDF original aportado](lls-hoja-informativa-2018/original/hairy-cell-leukemia.pdf) está conservado íntegramente en esta colección y dispone de [descarga directa verificada](https://raw.githubusercontent.com/juantoniolloretegea/SVperitus-dataset/488d597fa1999a1fc2eb6538fd610a36046f6f01/dominios/inmunologia/literatura-tricoleucemia/lls-hoja-informativa-2018/original/hairy-cell-leukemia.pdf). Es el archivo utilizado para la conversión. La referencia externa antes indicada se retira como vía de descarga tras comprobarse su indisponibilidad; no se atribuye identidad a otra edición del editor. La huella SHA-256 identifica inequívocamente el original conservado.

## Organización y acceso

Cada carpeta contiene `index.html`, una hoja de estilo local común, `documento.json` con el texto y sus localizadores, `ficha.json` con la procedencia, `cotejo.json` con las comprobaciones y `MANIFIESTO-SHA256.json` con tamaños y huellas. La subcarpeta `original` conserva la fuente sin modificación. La carpeta de LLS añade las diez reproducciones visuales para contrastar la disposición de cada página.

Las dos vistas HTML se leen sin conexión y sin ejecutar programas dentro de la página. Los enlaces a fuentes externas se conservan como referencias. GitHub presenta el código de los archivos HTML; para ver el documento compuesto se descarga la carpeta y se abre `index.html` en un navegador. Debe mantenerse la estructura relativa de archivos. Los enlaces entre ambas fuentes requieren conservar juntas sus dos carpetas.

## Método de preparación y comprobación

En el documento NCI se conserva íntegro el texto del artículo, incluidos títulos, listas, referencias y notas. Se ajustan las direcciones relativas y los enlaces internos de las citas para su lectura local. Se comprueba la igualdad del texto antes y después de la transformación, normalizando exclusivamente espacios, y la existencia de los destinos internos. El artículo capturado no contiene imágenes que precisen una descarga adicional. La navegación general y los servicios del sitio se mantienen en la respuesta HTML original, pero no son necesarios para leer la vista documental.

En el PDF se extrae la capa de texto sin reconocimiento óptico. Se reconstruye el orden de lectura por página: cabecera, columna izquierda, columna derecha y pie. Se preservan todas las páginas, los bloques y la referencia a su posición original. Las viñetas de la tipografía simbólica se expresan con símbolos Unicode equivalentes; esta transformación queda declarada en la ficha. Se cotejan la cobertura de caracteres por página y la correspondencia entre el texto estructurado y el HTML, y se revisa visualmente la disposición. Los elementos gráficos sin caracteres extraíbles se conservan en el original y en las reproducciones de página.

La numeración documental de páginas del PDF comienza en **0**; la numeración impresa comienza en **1**. El índice 9 corresponde a la página impresa 10. En la fuente web se utilizan identificadores de sección, sin atribuirle páginas físicas. La ausencia de una página siguiente no acredita, por sí sola, que se hayan leído las anteriores. Las afirmaciones, fechas y referencias de ambas fuentes se conservan sin actualización clínica ni conciliación entre ellas.

## Alcance y límites de comparación

La proximidad temática no convierte las fuentes en observaciones independientes ni garantiza equivalencia de alcance. Difieren en fecha, propósito editorial y destinatarios; el documento de LLS incluye referencias al PDQ. La comparación debe conservar la atribución de cada pasaje, distinguir coincidencias y discrepancias y considerar la fecha de publicación. Una divergencia no debe resolverse fusionando los textos o corrigiendo silenciosamente una fuente histórica.

La conformidad documental se limita a identificación, conservación, extracción y presentación. No demuestra vigencia terapéutica, exactitud clínica de todas las afirmaciones ni capacidad de un sistema para aplicarlas a un caso. La lectura ordinaria de estas dos copias puede realizarse mediante HTML y texto estructurado; su preparación no incorpora un lector PDF al recorrido del SV ni modifica sus componentes.

## Autoría, atribución y condiciones de uso

El texto y los elementos de terceros conservan sus autores y condiciones originales. Para la fuente NCI se mantienen la atribución, el enlace al original y sus [condiciones de reutilización](https://www.cancer.gov/espanol/politicas/derechos-de-autor-y-uso). El PDF y su conversión conservan la atribución a LLS. La licencia de esta organización documental no se extiende a contenidos ajenos ni sustituye sus condiciones.

El pie siguiente se aplica a la organización de la colección, los metadatos y la presentación elaborados para esta edición.

© 2026 Juan Antonio Lloret Egea. Algunos derechos reservados. | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ – La Biblia de la IA™ | ISSN 2695-6411 | Licencia Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0).
