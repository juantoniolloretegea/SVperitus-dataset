# Protección desde el arranque y preservación del núcleo del SV

28 de octubre de 2026 · Versión 0.1 · Objetivo arquitectónico del Agente Especializado en Ciberseguridad Inteligente.

## Estatuto y finalidad

El objetivo es proteger una instalación autorizada desde las primeras etapas verificables de su arranque, durante la inicialización de sus dispositivos y a lo largo de su funcionamiento. Comprende amenazas automatizadas, incluidas las que utilicen inteligencia artificial. La función defensiva permanece subordinada al gobierno determinista del Sistema Vectorial SV.

Esta especificación incorpora un objetivo de desarrollo; no acredita una defensa instalada en firmware, una capacidad de control del procesador ni una autorización de producción. Su **custodia basal está todavía indeterminada**: se han identificado sus relaciones doctrinales, pero faltan contratos de realización, comprobaciones materiales y recepción competente. Se aplica el [patrón común del agente](../../especificaciones/patron_agente_especializado/README.md) y la [custodia basal del diseño](../../especificaciones/custodia_basal_del_diseno/README.md).

La definición completa se mantiene en esta sede del agente. El dominio y los libros relacionados remiten a ella sin reproducirla. El Universo OP-CYB-001 conserva su objeto, inventario y versión; no se amplía por esta especificación.

## Fronteras materiales que deben distinguirse

| Frontera | Objetivo | Condición de comprobación |
| --- | --- | --- |
| Arranque de la plataforma | Establecer una cadena verificable desde el firmware y la inicialización de los dispositivos hasta el entorno que ejecuta el SV. | Plataforma, versiones, raíces de confianza, componentes comprobados, mecanismos de protección, detección y recuperación identificados. |
| Procesador, memoria y periféricos locales | Impedir que una operación no autorizada altere el núcleo, sus entradas admitidas o los controles de ejecución. | Privilegios, protección de memoria, acceso directo de dispositivos a memoria, controladores y límites efectivos comprobados para ese equipo. |
| Red | Disponer de protección, como mínimo, en la capa de enlace de datos —capa 2 del modelo OSI—, además de los controles necesarios en otras capas. | Interfaces y segmentos propios identificados; observación y aplicación efectiva de la política en el punto de red autorizado. |
| Aplicaciones y modelos | Someter cada petición y actuación a identidad, alcance, evidencia, autorización y límites. | Comprobación del recorrido completo, incluida la frontera de salida, la cancelación y el registro de efectos. |

El POST es una comprobación de arranque ejecutada por el firmware BIOS/UEFI. La CMOS conserva tradicionalmente parámetros de configuración; no debe confundirse con el programa de arranque ni con un alojamiento general para un modelo. En plataformas UEFI deben precisarse las fases y componentes efectivamente disponibles. Incorporar una función temprana de protección exige mecanismos admitidos por la plataforma y, cuando corresponda, cooperación del fabricante.

La capa 2 protege relaciones de enlace de datos. No designa el nivel de privilegio del procesador, el firmware ni una posición inferior del lenguaje máquina. Tampoco concede visibilidad o autoridad sobre toda una red desde un único equipo. La cobertura se acredita por frontera y dispositivo.

El objetivo de protección temprana no exige alojar un modelo generativo en BIOS/UEFI. La parte temprana de confianza deberá ser mínima, verificable y determinista. La asistencia de un modelo, si se autoriza, se ejecutará fuera de esa base de confianza y no será una dependencia necesaria para que funcionen las protecciones esenciales.

## Autoridad del núcleo y posición de la inteligencia artificial

La [frontera normativa del Lenguaje SV](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/main/FRONTERA_NORMATIVA_LENGUAJE_SV_v0.md) conserva su prevalencia. Esta aplicación no modifica el alfabeto {0, 1, U}, las leyes algebraicas, el umbral canónico, las dimensiones admisibles, los contratos de composición, la criticidad ni la trayectoria. Ningún modelo adquiere una excepción por ejercer como Perfil defensor (PD).

El requisito de inaccesibilidad del núcleo se expresa mediante obligaciones comprobables: ningún modelo recibe acceso directo de lectura o escritura a su memoria o almacenamiento privado, facultad para sustituir sus programas o reglas, credenciales de administración, claves de confianza, ni capacidad para alterar el registro o concederse permisos. Sólo podrán circular los datos expresamente admitidos por la tubería y sus contratos. Un resultado autorizado puede comunicarse por esa frontera; ello no concede acceso al interior del núcleo.

La arquitectura distinguirá:

1. **Captura y admisibilidad.** Los adaptadores autorizados obtienen observaciones con origen, identidad de componente, intervalo, versión, integridad y límite de cobertura.
2. **Evaluación determinista.** La transducción y el recorrido del Lenguaje SV aplican los contratos constituidos. Las observaciones o propuestas de un modelo no se convierten por sí mismas en hechos, valores ni órdenes.
3. **Aplicación de la decisión.** Un componente de actuación separado, implementado en Rust, ejecuta únicamente operaciones expresamente permitidas, delimitadas y vigentes. La aprobación de una propuesta no le concede un intérprete general ni autoridad sobre el núcleo.
4. **Comprobación del efecto.** Una observación independiente contrasta lo ocurrido y conserva el resultado, la discrepancia o la insuficiencia. Ni el modelo que propuso la acción ni el componente que la realizó pueden darse por recibidos por su propia declaración.

El núcleo deberá poder representar y verificar las condiciones de gobierno necesarias mediante sus construcciones admitidas. Los controladores de dispositivos, protocolos de red e inferencias permanecerán en componentes externos. Antes de proponer nueva gramática o representación intermedia se justificará qué obligación no puede expresarse con los contratos existentes. Una necesidad de integración no autoriza a introducir semántica implícita ni a modificar los invariantes.

## Terna, insuficiencia y continuidad de la protección

Cada condición evaluable necesita su pregunta, dominio observacional, reglas de admisibilidad y particiones de transducción. No se prescribe un valor universal para una ausencia de telemetría ni se convierte una incidencia instrumental en una calificación del candidato.

Cuando una condición constituida carezca de evidencia suficiente para asignar 0 o 1, se conservará U conforme a su contrato. Si falta una condición de autorización, la actuación dependiente no se habilitará. Ese bloqueo operativo no reescribe U como 1 ni sustituye la clasificación del SV. Las protecciones deterministas ya válidas deberán continuar conforme a su política recibida, sin depender de que un modelo responda.

La conservación de los invariantes es una obligación semántica. La resistencia frente a alteraciones de firmware, accesos físicos o errores de implementación es otra obligación, que exige mecanismos y pruebas materiales. No se declara invulnerabilidad absoluta ni se considera demostrada por utilizar Rust, firmware firmado o la terna matemática.

## Límites de la defensa y recuperación

La defensa actúa exclusivamente sobre activos y recursos propios o expresamente autorizados. No se extiende a los centros de proceso de datos de proveedores ni a sistemas de terceros por el origen de una amenaza.

La intervención debe identificar el dispositivo afectado, la operación permitida, su duración, el mecanismo de revocación, las consecuencias previsibles y el estado de recuperación. El principio del **dispositivo menos vital** orienta la elección del soporte de ensayo: emulación y dispositivos prescindibles cuando permitan comprobar el fenómeno. Una emulación acredita únicamente lo representado por su modelo; un disco de trabajo no aísla por sí mismo procesador, memoria, red ni firmware del equipo anfitrión.

Las copias de datos no restituyen por sí solas un firmware alterado ni reparan daños físicos. Antes de cualquier intervención de arranque o dispositivo deberá existir una vía de recuperación compatible, comprobada y separada de la función que se ensaya. La política de custodia documental y copias cifradas del SV conserva sus propias sedes y alcance.

## Recepción exigible y relación con el examen

La futura recepción deberá aportar, al menos:

- Modelo de amenazas y perímetro de activos, con exclusiones expresas.
- Identificación de la plataforma y de los mecanismos de arranque, protección de memoria, dispositivos y red realmente disponibles.
- Contratos de observación, transducción, actuación y registro, con límites de tiempo, capacidad y autoridad.
- Pruebas negativas de acceso al núcleo por una IA atacante y también por el Perfil defensor (PD), incluida una instrucción que pretenda alterar reglas, evidencia o permisos.
- Pruebas de observador ausente, dato obsoleto o repetido, pérdida de comunicación, parada del modelo y recuperación de una actuación incompleta.
- Controles legítimos que acrediten que la protección conserva las operaciones autorizadas.
- Evidencia de protección, detección y recuperación, con dictamen independiente para cada frontera. Lo no observado permanecerá declarado.

El examen de Ciberseguridad con SV(25,5) mantiene su constitución y criterios vigentes. La recepción de Q19 sobre caché, cuando se produzca, no demostrará por sí sola esta arquitectura de arranque ni ampliará el examen a escritura de firmware. Cualquier incorporación experimental posterior requerirá definición previa, medios suficientes y autorización correspondiente; no modifica retrospectivamente resultados.

## Fuentes y alcance de su uso

- [Frontera normativa del Lenguaje SV](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/main/FRONTERA_NORMATIVA_LENGUAJE_SV_v0.md), bloques A, B.6–B.7 y D: autoridad semántica y límites de automatización. La implementación y recepción vigentes deben comprobarse separadamente.
- [Código limpio y auditable](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/main/docs/calidad/tuberias-ia/continuacion-15-09-2026/CODIGO-LIMPIO-Y-AUDITABLE.md): condiciones del código, fronteras y evidencia.
- [Consecuencias de la omisión](https://github.com/juantoniolloretegea/SV-motor/blob/main/laboratorio/ensayo-ia-y-observabilidad/modelos-de-ia/estandar-comparativo-o-benchmark/CONSECUENCIAS-Y-FUENTES.md): relación entre omisión, consecuencia justificada, control y evidencia.
- [NIST SP 800-193, Platform Firmware Resiliency Guidelines](https://csrc.nist.gov/pubs/sp/800/193/final): referencia técnica para proteger firmware, detectar modificaciones no autorizadas y recuperar la plataforma. No acredita cumplimiento de una instalación del SV.
- [Especificaciones UEFI y Platform Initialization](https://uefi.org/specifications): referencia para distinguir las fases e interfaces del firmware de los servicios posteriores.
- [Microsoft: Secure Boot](https://learn.microsoft.com/en-us/windows-hardware/drivers/bringup/secure-boot): descripción de la comprobación de firmas en el recorrido de arranque; no equivale a autorización funcional ni demuestra ausencia de vulnerabilidades.

Las fuentes técnicas externas informan el diseño; no sustituyen la doctrina del SV. Consulta documental: 28 de octubre de 2026.

---

© 2026 Juan Antonio Lloret Egea. Algunos derechos reservados. | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ – La Biblia de la IA™ | ISSN 2695-6411 | Licencia Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0).
