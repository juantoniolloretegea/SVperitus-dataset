# Protocolo de evaluación documental de tricoleucemia
## EVAL-PDQ-HCL-25-20260929 · revisión 1 · 29 de septiembre de 2026

**Estado: preparación del banco; no instalado ni ejecutado.** La ronda pertenece a S39 mediante TT-0016 y se conserva en la rama existente dominio-inmunologia de SVperitus-dataset, dentro de tes-examenes-conocimientos/ronda-01-pdq-tricoleucemia-20260929. Su incorporación al servidor corresponde a una actuación posterior coordinada con la recepción de la corrección del supervisor. Esta preparación no interrumpe esa corrección ni acredita su finalización.

## Objeto y límites

Evaluar respuestas observables, fidelidad a la fuente, uso efectivo del MCP y capacidad de relacionar condiciones explícitas. No inferir estados mentales ni confundir fluidez, recuerdo o coincidencia verbal con comprensión demostrada. Los casos son sintéticos. Un resultado favorable pertenece exclusivamente a este banco, esta versión de la fuente y esta configuración: no cualifica asistencia clínica real, toda la inmunología, el universo OP-IMM-001 ni el conjunto del modelo.

Es un instrumento experimental propio, basado en un documento del NCI; no es un examen oficial del NCI. Se utiliza la denominación «NCI» —Instituto Nacional del Cáncer— para la fuente identificada.

## Fuente congelada y procedencia

Documento: pdq-nci-hcl-es, versión para profesionales de salud.
URL de procedencia: https://www.cancer.gov/espanol/tipos/leucemia/pro/tratamiento-celulas-pilosas-pdq

La caché declara actualización editorial de **14/11/2024** y recuperación en **2026-09-26T12:20:31Z**. Esa diferencia se conserva; descargar en 2026 no actualiza su contenido clínico. El banco se contrasta con la caché del expediente, no con una sustitución posterior de la página pública.

Custodia de referencia: [catálogo fijado](https://github.com/juantoniolloretegea/SV-sala-de-maquinas/blob/9773175b852fa5866fbaf73eebe618d570c3678b/respuestas-ejecucion/MCP-DOCUMENTAL-PREPARACION-20260926/entrega-05/emulacion-dominio-inmunologia/catalogo-pdq.json).

- SHA-256 catálogo: 94024658204c0607c5879f8cf263d6238d639494b5d9c266396c20f3e848a45d.
- SHA-256 HTML conservado: 00018ac31108eecc4709f0ce80439d4ca2d56b02262c5c334a184b9c0944e04d.
- Secciones: _1, _3, _13, _333 y _AboutThis_1. Sus huellas específicas figuran en la clave.
- Antes de ejecutar, cotejar las huellas contra la carpeta efectivamente autorizada al MCP y consignar las rutas reales. Si divergen, no ejecutar esta revisión ni adaptar respuestas silenciosamente.
- No se incorporan preguntas del antiguo cuestionario genérico de inmunología. No se siguen las referencias web del PDQ durante la consulta del modelo.
- Las preguntas evitan puntos ambiguos de la traducción: no evalúan la técnica concreta indicada para comprobar BRAF en el apartado pandémico ni la fase asignada al ensayo de dabrafenib/trametinib. Cualquier conflicto documental detectado posteriormente invalida el ítem afectado en esta revisión; no se penaliza al modelo por una clave defectuosa.

## Constitución del banco

25 posiciones fijas P01–P25; n=25 y b=5. No se trata de una matriz de cinco filas por cinco columnas ni de cinco células de tamaño cinco.

| Nivel | Posiciones | Objeto | Críticas | No crítica |
| --- | --- | --- | --- | --- |
| 1 | P01–P05 | Reconocimiento y lectura directa | P01–P04 | P05 |
| 2 | P06–P10 | Diferencias y restricciones explícitas | P06–P09 | P10 |
| 3 | P11–P15 | Aplicación a una condición sintética | P11–P14 | P15 |
| 4 | P16–P20 | Interpretación de resultados y límites | P16–P19 | P20 |
| 5 | P21–P25 | Integración y examen de afirmaciones excesivas | P21–P24 | P25 |

La graduación es una hipótesis de diseño, todavía sin calibración empírica. La criticidad responde a la selección solicitada de 20/5; debe recibirse antes de ejecutar. No se cambian pesos, orden, dificultad, clave o criticidad después de ver respuestas. Un error de diseño requiere nueva revisión y conserva el resultado anterior como antecedente.

## Presentación y aislamiento de la clave

Archivos:
- preguntas.json: instrucción común, enunciados y localizadores documentales. Entregar al modelo **una pregunta por petición**, no el banco completo.
- [CLAVE-CORRECCION.md, custodia privada](https://github.com/juantoniolloretegea/SV-sala-de-maquinas/blob/be36261c953ceebfc2b0bcf53e5a0e62d0a900b5/encargos-ejecucion/QWEN80-Q4K-ONECLOUD-20260929/anexos/ronda-01-pdq-hcl-20260929/CLAVE-CORRECCION.md): respuestas de referencia, ejemplos de error, criticidad y fundamento. Reservado al evaluador; no forma parte de esta carpeta pública.
- evaluar.rs: cálculo auxiliar en Rust a partir de adjudicaciones humanas; no interpreta medicina ni sustituye el núcleo del SV.

En el servidor se propone, sujeto al cotejo de rutas y usuarios reales, una carpeta independiente de prueba con subcarpetas entrada, evaluador y resultados. La clave queda fuera del corpus y del índice MCP, sin lectura por la identidad del motor, del MCP o del servicio web. La separación debe demostrarse con permisos o aislamiento efectivo; otra carpeta con el mismo permiso de lectura no basta. El acceso al escritorio no justifica exponerla al servicio web.

Antes de inferir, la ejecución preparará un pequeño índice de las páginas MCP que contienen cada localizador y cotejará sus intervalos y huellas mediante el lector aprobado. Se pueden entregar esos números de página junto con el enunciado: esta primera revisión evalúa interpretación con localización asistida, no una competición de búsqueda. No copiar la respuesta de referencia al mensaje. Si un ítem no cabe en los límites de recuperación o contexto, devolver el impedimento de instrumentación sin ampliar límites ni puntuarlo como U.

## Secuencia de ejecución futura

1. Recibir favorablemente la corrección del supervisor; conservar el punto de parada previo a la carga. Esta preparación no sustituye esa recepción.
2. Comprobar suficiencia instrumental de la carga, límites de memoria, aislamiento de Internet, MCP aprobado, custodia y acceso humano; no se presupone que estas comprobaciones ya sean favorables.
3. Cotejar y fijar huellas del banco, clave, fuente, motor y configuración antes de la primera pregunta. Documentar parámetros reales de generación; no atribuir determinismo a una semilla o temperatura por sí solas.
4. Ensayar de menor a mayor dificultad, en bloques de cinco y en orden P01–P25. Cada pregunta usa contexto nuevo, con la misma instrucción y fuente; no hereda respuestas ni correcciones de las anteriores.
5. Conservar petición original, contexto efectivo, llamadas y respuestas MCP, localizadores/huellas, salida original y telemetría correlacionada por identificador. La afirmación del modelo de haber leído no sustituye esas trazas.
6. La primera respuesta válida de cada ítem constituye el intento. Las repeticiones requieren motivo registrado y no reemplazan el intento anterior por el mejor. Un fallo técnico conserva su evidencia y no autoriza un reintento automático.
7. Corregir de forma independiente con la clave, sin utilizar al propio candidato como juez. Consignar fundamento y referencia de evidencia por cada posición. Una discrepancia de corrección se resuelve antes de cerrar el vector.
8. Sólo después de 25 adjudicaciones válidas producir el vector completo y su representación. Si se interrumpe la prueba, entregar resultados parciales con posiciones pendientes explícitas, sin completar artificialmente con U y sin emitir un frame de 25 posiciones.
9. Retornar a la recepción del ensayo S39 y a la prueba humana. El aseguramiento de imagen y la retirada de la instancia siguen bajo la autoridad exclusiva de la dirección.

Se mantienen los límites vigentes: CPU/Rust, excepciones criptográficas expresamente acotadas, sin intercambio a disco, objetivo de 50 GiB y límite duro previamente fijado, una secuencia, contexto total de 4096 tokens con entrada de hasta 3840 y salida de hasta 256, hasta cuatro llamadas MCP y cinco generaciones por consulta, 30 segundos por operación MCP y 900 segundos por consulta. El límite de carga de 3600 segundos y el presupuesto y plazo acumulados del encargo no se reinician por añadir este banco. No se amplían por iniciativa ejecutora.

## Adjudicación ternaria

**0:** contenido requerido correcto, sin contradicción relevante, con evidencia recuperada realmente por el MCP que lo respalda y una relación explicada brevemente. Se admiten sinónimos y síntesis equivalentes; no se exige copiar el texto.

**1:** al menos una afirmación relevante falsa o contraria a la fuente; inferencia no permitida presentada como conclusión cierta; cita fabricada o atribuida a un contenido que no contiene. Incluir también frases correctas no neutraliza ese error. La corrección debe indicar qué afirmación falla y por qué.

**U:** abstención auténtica, respuesta incompleta, ambigua o indeterminada que no permite acreditar 0 y no contiene una falsedad relevante demostrada. Una respuesta aparentemente acertada pero sin sustento comprobable queda U; no obtiene 0 por plausibilidad. Una explicación correcta del límite de la fuente puede obtener 0 cuando eso es precisamente lo preguntado: no se confunde reconocer un límite con no responder.

**Fuera de la terna del ítem:** caída del servicio, respuesta perdida, falta de registro, expiración técnica o pregunta/corpus no constituido. Es un intento inválido, no una respuesta U. No se usa U como relleno. Si hay respuesta genuina U conservada antes de otro fallo, sólo se puntúa cuando su integridad está acreditada.

Esta convención no es una suma de puntos positivos y negativos ni una resta de errores: se conserva cada valor y se cuentan sus apariciones.

## Umbral, clasificación y admisión

La referencia doctrinal consultada fija **T(n)=⌊7n/9⌋**; no 7n/7. Para n=25, T=19.

Clasificación algebraica auxiliar κ:
- NO_APTO si N1 ≥ 19.
- APTO si N0 ≥ 19.
- INDETERMINADO en los demás casos.

Condición adicional de admisión **de este ensayo**, separada de κ:
- Cualquier 1 crítico → NO_ADMITIDO.
- Ningún 1 crítico, pero algún U crítico → INDETERMINADO.
- Las 20 críticas en 0 y κ=APTO → ADMITIDO.

La exigencia de veinte críticas correctas ya implica N0≥20 y supera por sí sola el umbral de 19. Por tanto, con la distribución solicitada el umbral no añade una restricción independiente. Las cinco no críticas pueden contener 1 o U sin impedir la admisión, pero sus errores e indeterminaciones permanecen visibles. No denominarlas «sin importancia».

Ejemplos aritméticos, no resultados del modelo:
- 20 críticas correctas y 5 no críticas erróneas: κ=APTO; ADMITIDO.
- 24 correctas y 1 crítica errónea: κ=APTO; NO_ADMITIDO.
- 24 correctas y 1 crítica U: κ=APTO; admisión INDETERMINADA.

La regla de criticidad no reescribe la ley general del SV. El programa auxiliar tampoco constituye una recepción del núcleo: su función es aplicar de manera revisable este contrato experimental a correcciones ya realizadas.

## Vector y polígono

Mantener el orden P01–P25. Según los fundamentos consultados:
- ρ(0)=1; ρ(1)=2; ρ(U)=3.
- θᵢ=2π(i−1)/25.
- Vᵢ=(ρ(vᵢ)cos θᵢ, ρ(vᵢ)sin θᵢ).
- Cerrar V25 con V1.

La criticidad se registra como metadato; no cambia el radio. No se ordenan los vértices por resultado ni se interpreta el área como nota clínica. El SVG usa una transformación de coordenadas para mostrar el mismo polígono en pantalla. Cada resultado queda vinculado a banco, revisión, corpus, configuración, ejecución y evidencia de corrección. Un nuevo intento genera un resultado nuevo; no sobrescribe el anterior. No se ha generado un polígono del modelo porque aún no existen sus 25 respuestas.

## Uso del cálculo auxiliar

Compilar evaluar.rs con la cadena Rust admitida. Recibe un TSV con cabecera exacta:
pregunta[TAB]integridad[TAB]valor[TAB]fundamento[TAB]evidencia

Se exigen 25 filas ordenadas P01–P25. Integridad debe ser «valida»; valor, 0, 1 o U. Fundamento y referencia de evidencia deben estar presentes, sin tabuladores ni saltos de línea internos. La referencia identifica la evidencia custodiada; el programa comprueba su presencia formal, no su autenticidad ni su validez médica.

Invocación: evaluar adjudicaciones.tsv directorio-nuevo-de-resultados referencia-inmutable-de-ejecucion

La referencia de ejecución debe identificar el registro que fija modelo, configuración, corpus, banco, fechas, límites y evidencias. La salida incluye frame.json y poligono.svg. El directorio debe ser nuevo. El resultado es auxiliar y requiere cotejo receptor con los originales; la herramienta no verifica por sí sola el destino de las referencias. Conservar la entrada adjudicada junto con su manifiesto; el JSON incluye sus filas de fundamento y evidencia. No introducir datos clínicos reales ni secretos.

## Referencias doctrinales fijadas

- [Fundamentos: representación y umbral](https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/b8fd32978292d25adf9b87cf71e409005dce642c/documentos/fundamentos/README.md), apartados de polígono y clasificación por umbral.
- [Pilares y restricciones del Lenguaje](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/f8577f869e9e0bed85da9b6ce7b8e7b3b2cefa52/docs/calidad/PILARES_Y_RESTRICCIONES_DE_DISENO_DEL_LENGUAJE_DE_COMPUTACION_SV_2026_09_05.md), vector plano, identidad posicional, U y separación entre dominio y núcleo.
- [Léame primero de frame y trazabilidad](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/f8577f869e9e0bed85da9b6ce7b8e7b3b2cefa52/docs/calidad/tuberias-ia/frame-significado-humano-trazabilidad-y-fidelidad/LEAME_PRIMERO.md), significado humano, constitución y vínculo con la evidencia.

No se han modificado esas fuentes, los README históricos ni el mapa histórico. El README propio de esta ronda se crea por autorización expresa. El paquete se conserva en la sede autorizada del dominio; publicar la clave para su custodia no autoriza incorporarla al corpus consultable por el candidato. La documentación técnica y los resultados volverán también a la sede del modelo y a la entrega del ensayo cuando se produzcan.
