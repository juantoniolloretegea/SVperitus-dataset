# Auditoría contradictoria del documento de gobierno del dominio clínico de inmunología

**Objeto auditado:** `1788170602319_flujo-gobernado-inmunologia-determinista-v2.html`
**Tamaño:** 114.370 bytes
**SHA-256:** `5defe52812807b5679fe00730532cdb1fa1eb652332fd5ba219a25b0d49398ff`
**MD5:** `a70a566804d9250f50289c73dda46944`
**Título interno:** «Gobierno del dominio clínico de inmunología · Documento de gobierno · versión adversarial 2»
**Autoría del objeto:** unidad Watson
**Auditoría realizada por:** unidad Claude
**Fecha de auditoría:** 31 de agosto de 2026
**Naturaleza:** auditoría contradictoria. No es revisión por pares. No valida el dominio clínico ni sustituye decisión alguna del director.

---

## 0 · Alcance y método

Se ha auditado el fichero entregado, no una descripción de él. Procedimiento seguido:

1. Extracción del documento real, que viaja escapado dentro del atributo `srcdoc` de un `<iframe>` en el fichero exterior.
2. Lectura íntegra del texto visible: mapa rector, seis pestañas, tres paneles contradictorios, protocolo de repositorios y lista de cierre de veinte ítems.
3. Lectura del código: cinco bloques `<script>`, control de pestañas, persistencia, modo de resaltado e impresión.
4. Comprobación aritmética de las cardinalidades publicadas.
5. Contraste de los criterios del protocolo de repositorios contra las condiciones reales de las fuentes verificadas el 31 de agosto de 2026 en el informe `INFORME-REPOSITORIOS-INMUNOLOGIA.md`.

Cada hallazgo indica contra qué se contrasta. Lo que no he podido cerrar figura como **U** con su causa.

**U declarada de entrada, y condiciona el hallazgo B1.** No dispongo de los dos documentos que el propio objeto declara como su perímetro bibliográfico formal —*Fundamentos algebraico-semánticos del Sistema Vectorial SV* y *Origen doctrinal, definición y alcance de la U en el Sistema Vectorial SV*—. Fueron adjuntados a la unidad Watson, no a esta unidad. Por tanto no puedo comprobar si la notación `(n, b)` está definida en la doctrina ni con qué semántica. El hallazgo B1 se levanta, no se cierra.

---

## 1 · Cuadro de hallazgos

| Id | Severidad | Materia | Hallazgo en una línea |
|---|---|---|---|
| B1 | Bloqueante | Formal | Se publica como veredicto una relación algebraica generalizada a partir de dos casos |
| B2 | Bloqueante | Datos y publicación | El ítem 20 de la lista de cierre es insatisfacible con tres de las fuentes candidatas |
| B3 | Bloqueante | Legal y operativo | El flujo no contempla que la licencia del dato prohíba que el dato entre en la unidad de IA |
| M1 | Mayor | Gobernanza | Los tres paneles contradictorios se pisan, contra su propia regla de separación |
| M2 | Mayor | Gobernanza | Se registran veredictos de la unidad de IA como decisiones adoptadas |
| M3 | Mayor | Datos | El criterio temporal se escribió sin contraste con lo que las fuentes entregan realmente |
| M4 | Mayor | Datos | El criterio de población no contempla el recorte superior de edad |
| M5 | Mayor | Bibliografía | Las dos referencias formales no resuelven |
| M6 | Mayor | Trazabilidad | El documento incumple para sí mismo el versionado que exige a los demás |
| F1 | Material | Fichero | La afirmación de persistencia de la lista de cierre es falsa tal como se entrega |
| F2 | Material | Fichero | El botón «Imprimir» tiene alto riesgo de no hacer nada |
| A1 | Conforme | Aritmética | Cardinalidades correctas y bien distinguidas |
| F3 | Conforme | Fichero | Sin colisión de controladores, sin identificadores duplicados, recuento correcto |
| L1–L3 | Menor | Lengua | Anglicismo «adversarial», jerga «semilla» |
| O1–O2 | Observación | Doctrina y saldo | U sin horizonte resolutivo; columna vertebral que no debe negociarse |

---

## 2 · Hallazgos bloqueantes

### B1 · Se publica como veredicto una relación algebraica generalizada a partir de dos casos

**Dónde.** Panel «Adversarial lógica enlazada», línea de veredicto: se afirma que deben distinguirse instancia, matriz de datos y espacio de estados, que una representación (9,3) no es una matriz 3 × 3 ni una (25,5) una matriz 5 × 5, y que **el segundo término b satisface n = b², pero no es número de filas**.

**Contraste 1 — aritmética.** La relación se cumple en los dos casos presentes: 9 = 3² y 25 = 5². Verificado.

**Contraste 2 — semántica registrada en la conversación de trabajo.** El segundo término se describe allí como número de **capas o estratos**: «SV(25,5), cinco capas y T(25)=19». Una cuenta de estratos y un parámetro que satisface n = b² son dos objetos distintos que coinciden numéricamente en las dos instancias fijadas por ITI V.1.

**Contraste 3 — falsabilidad.** La generalización se rompe con la primera célula cuyo número de parámetros no sea un cuadrado perfecto: treinta parámetros en cinco estratos ya la falsa. Publicada como ley en un manuscrito, se convierte en un error que un revisor puede exhibir sin esfuerzo.

**Agravante.** Precisamente en la instancia (9,3), el valor b = 3 coincide numéricamente con el cardinal del alfabeto ternario |Σ| = 3. El panel existe para impedir esa confusión y la reintroduce por otra puerta al bautizar el segundo índice con la letra reservada a la base.

**Severidad.** Bloqueante. Es una inferencia elevada a veredicto en el panel de máxima autoridad formal del documento.

**Corrección propuesta.** Enunciar el segundo índice por su semántica declarada —número de estratos— y, separadamente, registrar como propiedad observada de las dos instancias fijadas, no como ley, que en ambas ese número satisface n = b². Reservar la letra b, si se usa, exclusivamente para el cardinal del alfabeto.

**U.** No cierro este punto: exige leer *Fundamentos algebraico-semánticos del SV*, que no obra en mi poder.

---

### B2 · El ítem 20 de la lista de cierre es insatisfacible con tres de las fuentes candidatas

**Dónde.** Lista de cierre, ítem 20: «¿Datos, diccionario, reglas, código, versiones y eventos permiten repetir?». Y protocolo de repositorios, dimensión «Singulares», con parada si «el repositorio sólo ofrece agregados irreversibles».

**Contraste — condiciones verificadas el 31 de agosto de 2026.**

- **ITN TrialShare.** Sus términos declaran que nada en el acuerdo constituye, expresa o implícitamente, concesión de licencia ni de otros derechos, y que la distribución a usuarios no autorizados de datos obtenidos por el sistema está estrictamente prohibida.
- **PhysioNet, licencia acreditada 1.5.0.** El licenciatario no compartirá el acceso a los datos restringidos con nadie más.
- **ImmPort, cláusula 2.4.** El usuario tiene derecho sin restricción a usar y distribuir los datos, garantizando que la redistribución se produzca en términos equivalentes al propio acuerdo.

**Consecuencia.** El acceso a filas y el derecho a publicar filas son dos cosas distintas. El protocolo comprueba la primera y no comprueba la segunda. Con ITN o con PhysioNet, el ítem 20 no puede marcarse tal como está redactado: la declaración de disponibilidad de datos de un manuscrito debe remitir al procedimiento de acceso del custodio, no prometer entrega. Con ImmPort sí puede marcarse.

**Severidad.** Bloqueante, porque la lista de cierre es el instrumento de decisión del documento y contiene un ítem que tres de las cinco fuentes candidatas hacen imposible sin que el flujo lo advierta.

**Corrección propuesta.** Desdoblar la dimensión «Gobierno» del protocolo en tres columnas independientes: derecho de acceso; derecho de redistribución del subconjunto congelado; y qué puede prometer la declaración de disponibilidad de datos. El ítem 20 se reformula como «permiten repetir por un tercero con el mismo derecho de acceso», que es lo máximo que ITN y PhysioNet consienten.

---

### B3 · El flujo no contempla que la licencia prohíba que el dato entre en la unidad de IA

**Dónde.** Cabecera del mapa rector: «IA subordinada · Auxilia; no constituye el conocimiento ni adopta la decisión clínica». Y etapas 5A, 7A y la puerta final, que asignan trabajo a la IA sobre el dato.

**Contraste.** PhysioNet ha publicado que su acuerdo de uso prohíbe expresamente compartir el acceso a los datos con terceros, incluido enviarlos a través de API o usarlos en plataformas en línea, y que los datos de MIMIC no deben ser almacenados ni retenidos por servicios de modelos de lenguaje de terceros.

**Consecuencia.** Existe al menos una fuente candidata cuyo régimen impide que el dato atraviese a Watson o a Claude. El flujo regula minuciosamente la subordinación epistémica de la IA —qué puede concluir, qué no puede cerrar— y no regula en absoluto su **elegibilidad legal para ver el dato**. Es un punto ciego autorreferencial: el documento que gobierna el trabajo no pregunta si el trabajo, tal como se ejecuta, es lícito con esa fuente.

**Severidad.** Bloqueante, por consecuencia legal y porque afecta al método de trabajo, no sólo al contenido.

**Corrección propuesta.** Añadir una puerta inmediatamente después de D0, con tres salidas: *(a)* la licencia permite que el dato atraviese una unidad de IA de terceros; *(b)* sólo permite el paso de agregados producidos localmente; *(c)* no lo permite, y el tratamiento es exclusivamente local del experto. La salida elegida se declara en el manuscrito.

---

## 3 · Hallazgos mayores

### M1 · Los tres paneles se pisan, contra su propia regla de separación

El encargo exigía tres contradictorias sin invasión mutua. El documento lo declara en sus propias cabeceras y luego lo incumple en ambos sentidos:

- El panel clínico declara «No decide arquitectura informática» y a continuación dictamina que IMMUNO-1 e IMMUNO-2 «quedan degradadas correctamente a semillas experimentales». Eso es una resolución de estatuto y de alcance, es decir, arquitectura.
- El panel de ingeniería declara «No decide qué conocimiento inmunológico es correcto» y abre su tabla con el bloqueante «Confundir (n,b) con una matriz b × b», materia formal que el tercer panel vuelve a argumentar por extenso.

**Corrección propuesta.** El panel clínico enuncia la consecuencia clínica de presentar prototipos como cobertura completa —cosa que su tabla ya hace bien— y se detiene ahí. La resolución de estatuto corresponde al director. La confusión dimensional pertenece al panel lógico y aparece una sola vez.

### M2 · Se registran veredictos de la unidad de IA como decisiones adoptadas

Formulaciones como «quedan degradadas correctamente» o «La corrección necesaria es estructural» consignan como hecho consumado lo que es propuesta. El contexto raíz del proyecto establece que la IA propone, construye y audita, y que el director decide, aprueba y firma.

No es cosmético: un documento de gobierno que registra veredictos de IA como decisiones adoptadas no permite después reconstruir quién decidió qué, que es exactamente lo que el propio documento exige en su etapa 7B de trazabilidad material.

**Corrección propuesta.** Reformular en modo propositivo: «se propone degradar», «se propone como corrección estructural». La adopción se consigna como suceso separado, con fecha y firma.

### M3 · El criterio temporal se escribió sin contraste con lo que las fuentes entregan

**Dónde.** Protocolo de repositorios, dimensión «Tiempo»: debe documentarse «Fechas, orden de eventos, ventanas, censura y actualización», con parada si «existe fuga temporal o no puede establecerse precedencia».

**Contraste.** ImmPort declara que no registra fechas en sus plantillas y que todos los puntos temporales y calendarios se refieren al día 0 del estudio, o al día que designe el proveedor de datos.

**Consecuencia.** En esa fuente la fecha absoluta está estructuralmente ausente, pero la precedencia relativa existe. Redactado como está, el criterio es ambiguo: puede detener la fuente entera o puede dejar pasar un origen temporal heterogéneo entre estudios, que es el riesgo real, porque el día 0 lo elige cada proveedor.

**Corrección propuesta.** Desdoblar en tres pruebas: existencia de fecha absoluta; existencia de orden relativo con origen declarado; e **identidad del origen entre estudios**. La tercera es la que puede invalidar una composición entre módulos construidos sobre estudios distintos.

### M4 · El criterio de población no contempla el recorte superior de edad

**Dónde.** Dimensión «Población»: país, centros, criterios de inclusión y exclusión, edad, enfermedad, tratamientos y periodo.

**Contraste.** ImmPort declara que redondea a 90 toda edad superior a 89, dejando comentario de que se ha hecho.

**Consecuencia.** Cualquier parámetro con umbral por encima de 89 —posible en un dominio centrado en inmunosupresión en adultos y en riesgo infeccioso del anciano— es incomprobable en esa fuente. El protocolo pide la variable, no su transformación.

**Corrección propuesta.** Añadir a la dimensión «transformaciones de desidentificación aplicadas a cada variable», con parada si un umbral declarado cae dentro de un rango recortado.

### M5 · Las dos referencias formales no resuelven

El perímetro bibliográfico cita los dos documentos doctrinales como «versión canónica suministrada», sin DOI, sin localizador y sin fecha. Comprobado por búsqueda en el objeto: no contiene ninguna cadena «DOI» ni «ISSN».

Un revisor hostil no puede recuperar «versión canónica suministrada». Y el propio documento exige autocontención en su ítem 19 y reproducibilidad en el 20.

**Corrección propuesta.** Dar a cada uno localizador resoluble y fecha, o declararlos expresamente como documentos internos no publicados. La segunda opción es legítima, pero cambia lo que pueden sostener en un manuscrito biomédico y debe decirse.

### M6 · El documento incumple para sí mismo el versionado que exige a los demás

Se llama «versión adversarial 2» y no lleva fecha, autor, identificador ni hash. Comprobado: el objeto no contiene ninguna fecha del año en curso. Exige a los demás versionar corpus, datos, diccionario, reglas, código, umbrales y salidas, y mantener registro *append-only*.

**Corrección propuesta.** Cabecera con fecha, autoría, identificador de versión y hash del propio fichero. Sin eso, la versión 3 no será comparable con la 2.

---

## 4 · Comprobación material del fichero entregado

### F1 · La afirmación de persistencia es falsa tal como se entrega

**Afirmación del documento.** En la lista de cierre: «Las marcas se guardan únicamente en este navegador».

**Lo que hace el código.** Las veinte casillas se serializan con `localStorage.setItem('ig-review-v2', …)` y se restauran con `localStorage.getItem`. La pestaña activa se guarda con `sessionStorage.setItem('ig-active-tab', …)`. Ambas operaciones están envueltas en `try { … } catch (_) {}`, es decir, fallan en silencio.

**Cómo se entrega.** El documento completo se monta dentro de `<iframe sandbox="allow-scripts" …>`. El atributo de aislamiento **no incluye `allow-same-origin`**. Un marco así opera con origen opaco, y el acceso a `localStorage` y `sessionStorage` lanza excepción de seguridad. El `catch` vacío la absorbe.

**Efecto.** Las marcas no se guardan. Al recargar, el contador vuelve a «0 de 20» y el usuario no recibe ningún aviso de que su trabajo se ha perdido. Lo mismo con la pestaña activa.

**Por qué importa aquí más que en otro sitio.** La regla de cierre del propio documento dice que una casilla pendiente no se compensa con prosa ni con prestigio bibliográfico. El instrumento que sostiene esa regla no conserva estado.

**Comprobación por el director, treinta segundos.** Abrir el fichero, marcar una casilla, recargar la página.

**Corrección propuesta.** O bien mantener el estado en memoria y decirlo («las marcas se pierden al recargar»), o bien exportar la lista a fichero mediante descarga generada en el propio marco, que sí funciona con origen opaco. La primera es honesta; la segunda es útil. La combinación actual es la única inaceptable: promete y no cumple.

### F2 · Alto riesgo de que «Imprimir» no haga nada

El botón invoca `window.print()`. En el modelo de aislamiento de `iframe`, esa llamada queda gobernada por el indicador de modales, que sólo se levanta con `allow-modals`; el envoltorio entregado no lo incluye.

**No lo he probado en navegador en este turno.** Riesgo alto, comprobación material pendiente: pulsar el botón. Si no abre el diálogo de impresión, o se añade el permiso al envoltorio o se retira el botón.

### F3 · Lo que pasa la auditoría técnica

Consignado porque una auditoría que sólo enumera defectos no es una auditoría.

- **Sin colisión de controladores.** El documento trae su propio manejador de pestañas y el entorno anfitrión trae otro genérico que actúa sobre `.nav[role="tablist"]`. La lista del documento usa la clase `ig-tabs`, de modo que el manejador genérico no la captura y no hay doble activación.
- **Sin identificadores duplicados.** Veinte identificadores, todos únicos.
- **Recuento correcto.** Veinte casillas y contador que declara veinte.
- **Accesibilidad de pestañas correcta.** Navegación con flechas, Inicio y Fin; `aria-selected` y `hidden` mantenidos en cada cambio; `aria-valuenow` y `aria-valuemax` actualizados en la barra de progreso.

---

## 5 · Comprobación aritmética

Verificada y **conforme**. No hay reparo.

| Enunciado del documento | Comprobación |
|---|---|
| n = 9, 3⁹ = 19.683 | 19.683 ✓ |
| n = 25, 3²⁵ = 847.288.609.443 | 847.288.609.443 ✓ |
| Instancia = vector fila 1 × n, no matriz b × b | Conforme con lo fijado por el director |
| Espacio de estados Sⁿ = Σⁿ, con Σ = {0,1,U}, |Sⁿ| = 3ⁿ | Conforme |

La distinción entre matriz clínica X = (aᵢⱼ), instancia ternaria s ∈ Σⁿ y espacio de estados es correcta y es lo mejor del documento. El reparo B1 no toca a esto: toca a la ley inventada sobre el segundo índice, no a las cardinalidades.

---

## 6 · Lengua y registro

- **L1.** «Adversarial» aparece diez veces, incluido el subtítulo «versión adversarial 2» y las tres cabeceras de panel. Es anglicismo no registrado; en español publicable, «contradictoria».
- **L2.** Conforme: «célula» aparece dos veces y sólo con el estatuto declarado de aclaración interna. No aparece «artefacto» ninguna vez. Ambas normas se respetan.
- **L3.** «Semilla» es jerga interna y, además, en un manuscrito dirigido a inmunólogos colisiona con el registro biológico. Propuesta: «prototipo» o «instancia de contraste».

---

## 7 · Observaciones

**O1 · U sin horizonte resolutivo.** La etapa 5A establece que la U sólo se resuelve por experto, acontecimiento relevante o medición suficiente. La doctrina recogida en la conversación de trabajo sostiene que irreducible, fronteriza y resoluble son propiedades de una posición respecto de un horizonte resolutivo, no clases de U. El conjunto de puertas del flujo no contiene ninguna prueba para una posición que no se resuelva por ninguno de los tres mecanismos. No es contradicción —el residual aparece en varias etapas— pero sí es una prueba que falta.

**O2 · Lo que sostiene el documento y no debe negociarse.** Una auditoría contradictoria tiene que decir también qué defiende. Esto:

- la inversión «datos antes que teoría», con la puerta D0 como condición de parada y no como recomendación;
- la separación entre el nulo de la capa de datos y la U constituida, con transducción explícita;
- la prohibición de reloj oculto, generador aleatorio y aprendizaje autónomo dentro del núcleo;
- la frontera tipada que deja pasar la estimación externa con población, método, fecha e incertidumbre, y no deja pasar la probabilidad convertida en certeza ni el promedio que sustituye a la observación singular;
- la conservación de filas, subgrupos y casos raros frente al agregado;
- la exigencia de autocontención sin el nombre SV;
- y la regla de cierre: una casilla pendiente no se compensa con prosa.

Esa es la columna vertebral y es correcta. Los hallazgos de este informe no la tocan.

---

## 8 · Dictamen

**APTO CON REPAROS BLOQUEANTES.**

El documento es un instrumento de gobierno serio, correctamente estructurado y con una inversión de orden —datos antes que teoría— que corrige un defecto real. No puede circular ni sostener la puerta D0 en su estado actual por tres razones: publica una regla algebraica generalizada desde dos casos (B1); contiene un criterio de cierre insatisfacible con la mayoría de las fuentes reales (B2); y no contempla que la licencia del dato pueda prohibir que el dato entre en las unidades de IA que ejecutan el flujo (B3).

A ello se suman dos defectos materiales del fichero, uno de los cuales convierte en falsa una afirmación explícita del propio documento (F1).

Nada de lo anterior es una decisión. Son reparos. La resolución corresponde al director.

---

## 9 · Reparos numerados para devolución

| Nº | Reparo | Acción exigida |
|---|---|---|
| 1 | B1 · n = b² como veredicto | Enunciar el segundo índice por su semántica; registrar la coincidencia como propiedad observada de dos instancias, no como ley; no reutilizar la letra b |
| 2 | B2 · ítem 20 insatisfacible | Desdoblar «Gobierno» en acceso, redistribución y declaración de disponibilidad; reformular el ítem 20 |
| 3 | B3 · elegibilidad legal de la IA | Nueva puerta tras D0 con tres salidas declarables |
| 4 | M1 · paneles que se pisan | Devolver cada materia a su panel; el estatuto lo resuelve el director |
| 5 | M2 · veredictos como decisiones | Reformular en modo propositivo |
| 6 | M3 · criterio temporal | Desdoblar en fecha absoluta, orden relativo con origen declarado e identidad del origen entre estudios |
| 7 | M4 · recorte de edad | Añadir transformaciones de desidentificación por variable |
| 8 | M5 · referencias que no resuelven | Localizador y fecha, o declaración expresa de documento interno no publicado |
| 9 | M6 · autoversionado | Fecha, autoría, versión y hash en cabecera |
| 10 | F1 · persistencia falsa | Decir la verdad sobre el estado, o implementar exportación a fichero |
| 11 | F2 · impresión | Comprobar en navegador; añadir permiso o retirar el botón |
| 12 | L1, L3 · lengua | «Contradictoria» por «adversarial»; sustituir «semilla» |

---

## 10 · Encaje con el informe de repositorios del 31 de agosto de 2026

El documento auditado declara, correctamente, que fija cómo buscar y no selecciona todavía ninguna fuente. El informe `INFORME-REPOSITORIOS-INMUNOLOGIA.md` de la misma fecha aporta el material con el que esa búsqueda puede ejercerse: siete fuentes con sus normas de acceso, uso permitido, mecanismo de versión y desidentificación, más dos candidatos concretos en ImmPort —SDY3324 (ACV01), vacunación bajo inmunosupresión farmacológica, y SDY3274 (ARTIST), trasplante renal bajo inmunosupresión— ambos con la advertencia de que su nota de publicación no declara carga de ensayos ni de valoraciones clínicas.

Los hallazgos B2, B3, M3 y M4 de esta auditoría nacen exactamente de ese contraste: son los puntos donde el protocolo de búsqueda, escrito sin fuentes delante, no resiste el encuentro con las condiciones reales de las fuentes.

La puerta D0 puede ejercerse ya. Con material, no con criterio abstracto.
