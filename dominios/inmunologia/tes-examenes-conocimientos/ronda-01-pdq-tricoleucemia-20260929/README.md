# Ronda 01 · Tricoleucemia: evaluación documental gradual

**Identificador:** EVAL-PDQ-HCL-25-20260929/r1.  
**Estado:** banco preparado; evaluación del modelo pendiente.  
**Seguimiento:** [S39 — Ensayo de inteligencia artificial y observabilidad](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/main/docs/calidad/Inventario-sv/sucesos/SUCESOS_SV.md#s39), mediante [TT-0016](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/main/docs/calidad/Inventario-sv/tiques-tecnicos/TT-0016.md).

## Alcance y universo de conocimientos

Veinticinco preguntas originales, de respuesta breve y justificación documental, sobre la caché en español del [PDQ del NCI sobre leucemia de células pilosas, versión para profesionales](https://www.cancer.gov/espanol/tipos/leucemia/pro/tratamiento-celulas-pilosas-pdq). La captura declara actualización de 14/11/2024 y recuperación de 26/09/2026. Su identidad y custodia se fijan en el protocolo.

El universo operativo de esta ronda es **ese documento congelado**, incluidas sus limitaciones editoriales y probatorias. La ubicación en inmunología no convierte el banco en un examen de toda la disciplina ni en una realización completa de OP-IMM-001. Los casos son sintéticos; no se utilizan datos de pacientes.

Se examinan lectura, relación entre condiciones, interpretación de resultados, límites de la evidencia y autoridad de la fuente. Las respuestas permiten evaluar conducta observable y fundamentación, sin demostrar por sí solas comprensión interna ni seguridad clínica general.

## Contenido

- [Las 25 preguntas, en lectura directa](PREGUNTAS.md).
- [Preguntas para el candidato, formato estructurado](preguntas.json): 25 posiciones estables; se presentan de una en una mediante la interfaz admitida.
- [Protocolo](PROTOCOLO.md): procedencia, cinco niveles, reglas, aislamiento y condiciones de ejecución.
- [Clave de corrección, custodia privada](https://github.com/juantoniolloretegea/SV-sala-de-maquinas/blob/be36261c953ceebfc2b0bcf53e5a0e62d0a900b5/encargos-ejecucion/QWEN80-Q4K-ONECLOUD-20260929/anexos/ronda-01-pdq-hcl-20260929/CLAVE-CORRECCION.md): respuestas de referencia y criterios. **Reservada al evaluador; excluida del corpus MCP y de los permisos del proceso del modelo.**
- [Cálculo auxiliar en Rust](evaluar.rs): aplica la convención a adjudicaciones ya revisadas; genera un resultado JSON y su polígono.
- [Comprobación local](VERIFICACION.json): nueve pruebas sintéticas del cálculo; no son resultados de inferencia.

Cada nivel contiene cuatro preguntas críticas y una no crítica. Las cinco no críticas son P05, P10, P15, P20 y P25. Las restantes veinte son críticas.

La convención es **0 correcto, 1 erróneo, U indeterminado**. El umbral doctrinal es ⌊7×25/9⌋=19. Se conserva por separado la condición adicional: las veinte críticas deben estar en 0 para admitir la ronda. Un fallo técnico no se disfraza de U ni completa un vector ausente.

## Incorporación y retorno

El banco está previsto inicialmente para Qwen3-Next-80B-A3B-Instruct UQFF Q4K, en el ensayo nativo con acceso documental MCP sin Internet. Antes de ejecutarlo deben estar recibidos los controles instrumentales y constituida la sesión; la publicación no levanta el punto de parada de la corrección del supervisor.

La documentación se conservará también en la carpeta de evaluación del servidor y, por referencia y con resultados cuando existan, en la [sede del modelo](https://github.com/juantoniolloretegea/SV-motor/tree/main/laboratorio/ensayo-ia-y-observabilidad/modelos-de-ia/qwen/qwen3-next-80b-a3B-instruct) y en la entrega técnica del ensayo. **En esta preparación no se ha instalado la ronda en el servidor ni ejecutado preguntas.**

Las rondas posteriores tendrán carpeta e identidad propias dentro de tes-examenes-conocimientos; no reemplazarán enunciados ni claves de una ronda ejecutada. No se modifica la fuente del dominio ni se amplía el conocimiento admitido por publicar un test.

## Precisión del dictamen y de su representación · 29/09/2026

El resultado final de esta ronda se expresa como **Apto, No apto o U (indeterminación honesta)**. Las denominaciones anteriores «Admitido» y «No admitido» quedan sustituidas en la presentación y en el campo del dictamen final; la clasificación algebraica auxiliar se conserva separada para permitir el cotejo.

El vector completo conserva sus 25 posiciones y determina el polígono; el dictamen global por sí solo no basta para reconstruirlo. La futura GUI en egui permitirá examinar los frames y sus evidencias. Su implementación no forma parte de esta preparación.

La aptitud de un frame no se transfiere automáticamente al conjunto. La relación entre frames requiere el contrato del dominio, todavía no constituido aquí; el antecedente es el Universo 1. No se inventa una regla de composición ni se considera apto el dominio por superar esta ronda. U orientará una nueva ronda dirigida a esclarecer la indeterminación, conservando los intentos anteriores, sin repetición automática hasta obtener un aprobado.
