# Orden de auditoría externa limitada · acta de estratificación clínica, autoridad y ejecución computacional v0.1

## 1. Encargo

Audite adversarialmente el corte material indicado en esta orden. No redacte una arquitectura alternativa ni amplíe el dominio. Intente falsar la separación de capas, la distribución de autoridad y la utilidad operativa declaradas en el acta.

La auditoría debe comprobar el contenido real de los objetos y no limitarse a aceptar su adversarial interna.

## 2. Repositorio, rama y cortes exactos

- **Repositorio:** `juantoniolloretegea/SVperitus-dataset`
- **Rama:** `dominio-inmunologia`
- **Línea base:** `88445856dd2eb13b20975696f6151e6e4d9340f8`
- **Candidato material:** `ea18d5c7f9ecd51d17027d44f1cf281a1627b612`
- **Mensaje del candidato:** `Constituir la estratificación clínica y de ejecución`

El candidato material debe compararse directamente contra la línea base. El commit que incorpore esta orden queda fuera del objeto auditado.

## 3. Objetos y huellas

| Objeto | Bytes | SHA-256 |
|---|---:|---|
| `acta-estratificacion-clinica-autoridad-y-ejecucion-computacional-inmunologia-2026-09-02-v0.1.md` | 16 424 | `20a586fd96b6074e27bf34fbb087f35b8b27e2048686aafdb5be8285ffccd318` |
| `adversarial-interna-acta-estratificacion-clinica-autoridad-y-ejecucion-2026-09-02-v0.1.md` | 6 994 | `255e9d52961020251d340051d52ba4b76034dae00579aa645e4242be14ddfaf1` |
| `README.md` del directorio `cambio-rumbo` | 13 360 | `fd2a252c12815f2955ca6afebc42f6b735229d79a19fbd82a523815b6bf43a04` |

## 4. Límites

- No escribir en GitHub.
- No modificar archivos.
- No crear una rama o solicitud de incorporación.
- No tocar `main`.
- No reabrir el cierre profesional v0.8.
- No repetir la auditoría de `G2-S1` ni la de `G2-S2`.
- No constituir preguntas, observables, parámetros, umbrales, ventanas, matrices, rutas o frames.
- No abrir `G3-OBS`.
- No modificar ni proponer sintaxis para el Lenguaje SV.
- No utilizar relatos o datos de pacientes reales.
- No convertir una preferencia de diseño en criterio clínico.

## 5. Ataque A · identidad y regresión

Verifique:

1. identidad exacta del candidato material;
2. bytes y SHA-256 de los tres objetos;
3. diff completo contra la línea base;
4. que sólo se añaden el acta y su adversarial interna y se modifica el README rector;
5. que no cambian catálogos, hojas de cálculo, lotes G2, política de protección, pilotos, ITI ni Lenguaje SV.

Cualquier cambio adicional debe enumerarse y clasificarse.

## 6. Ataque B · separación y completitud de capas

Intente construir un caso en el que dos capas queden fusionadas o una responsabilidad no tenga ubicación inequívoca.

Compruebe por separado:

- núcleo atómico transversal;
- composición clínica;
- configuración institucional;
- instanciación del episodio clínico;
- ejecución computacional subordinada.

Para cada capa determine:

1. qué contiene;
2. qué no contiene;
3. qué autoridad puede modificarla;
4. qué dato puede entrar;
5. qué salida puede producir;
6. y si puede contaminar otra capa.

Falla si una singularidad individual o local puede modificar silenciosamente el núcleo general.

## 7. Ataque C · exactitud y falsa exhaustividad

Ataque la expresión «atomización exacta».

Determine si el acta diferencia suficientemente:

- exactitud relativa al corte semántico declarado;
- exhaustividad de la medicina;
- revisabilidad por nueva evidencia;
- y constitución posterior de observables o parámetros.

Falla si `EXACTA` puede interpretarse como verdad clínica completa, definitiva o independiente de `U`.

## 8. Ataque D · customización

Compruebe si `CUSTOMIZACION` queda cerrada sin ambigüedad como dos operaciones diferentes:

1. `CONFIGURACION_INSTITUCIONAL`;
2. `INSTANCIACION_DE_EPISODIO`.

Intente introducir bajo esa etiqueta:

- modificación de una indicación;
- rebaja de un veto;
- cambio de criticidad;
- alteración del significado de un átomo;
- personalización de conveniencia;
- o transporte de datos del episodio al núcleo.

Falla si cualquiera de esas operaciones puede ejecutarse sin bloqueo o `U`.

## 9. Ataque E · inversión de autoridad por ingeniería

Intente que una decisión de programación:

- cree o elimine una unidad clínica;
- fusione preguntas diferenciables;
- imponga una dimensión matricial;
- cierre una `U`;
- omita una dependencia difícil de representar;
- o transforme una limitación técnica en conclusión clínica.

Compruebe que la autoridad clínica y semántica de la implementación es nula y que la facilidad de programación no constituye evidencia.

## 10. Ataque F · negación indebida de la autoridad técnica

Ataque el extremo contrario. Determine si la subordinación clínica del software podría obligar a ejecutar una implementación:

- insegura;
- ambigua;
- no verificable;
- no representable;
- o semánticamente destructiva.

Compruebe que la ingeniería puede bloquear la ejecución en su propio plano sin convertir ese bloqueo en decisión clínica. Falla si sólo existen las alternativas «implementar» o «decidir clínicamente» y no se preservan reparación, reformulación fiel, escalado o `U`.

## 11. Ataque G · inteligencia artificial como autoridad encubierta

Intente demostrar que la inteligencia artificial podría:

- improvisar rutas;
- seleccionar fuentes fuera del contrato;
- inferir valores ausentes;
- adoptar conocimiento durante el episodio;
- sustituir al profesional;
- o adquirir autoridad por presentar una salida convincente.

Verifique que sus operaciones quedan limitadas a cálculo, recuperación autorizada, presentación, registro, abstención y escalado.

## 12. Ataque H · configuración institucional

Use al menos cuatro contraejemplos:

1. prueba clínicamente pertinente no disponible en el centro;
2. protocolo local diferente del procedimiento general;
3. circuito de derivación distinto;
4. restricción temporal o material que impide ejecutar la ruta preferida.

Determine si el sistema conserva simultáneamente la necesidad clínica y la viabilidad local, sin presentar una limitación institucional como verdad universal.

## 13. Ataque I · episodio, participación y medicina a demanda

Compruebe que:

- los valores individuales sólo instancian posiciones previamente definidas;
- la temporalidad y las preferencias clínicamente pertinentes pueden representarse;
- la participación y el consentimiento no se confunden con indicación clínica;
- los datos del episodio no se convierten en conocimiento general;
- y la decisión asistencial final permanece en el profesional autorizado.

Falla si la persona atendida puede imponer una actuación clínicamente improcedente o si su participación desaparece del modelo.

## 14. Ataque J · costes, tiempos y recursos

Intente compensar un veto o riesgo clínico grave mediante:

- ahorro económico;
- disponibilidad de camas;
- rapidez;
- menor carga administrativa;
- o conveniencia organizativa.

Compruebe que esos factores informan la viabilidad, pero no sustituyen la lógica clínica. Verifique también que no se ignoran: ante conflicto debe existir presentación separada y alternativa autorizada, escalado o `U`.

## 15. Ataque K · utilidad y carga cognitiva

Intente convertir el sistema en una lista exhaustiva que el profesional deba revisar en cada episodio.

Compruebe que el acta exige:

- retaguardia por defecto;
- activación por operación o condición crítica autorizada;
- prioridad de vetos, contradicciones, ausencias y `U`;
- divulgación progresiva;
- profundización hasta fuente y suceso;
- y no repetición de información estable.

Declare cualquier requisito que siga siendo demasiado genérico para impedir una interfaz administrativamente invasiva.

## 16. Ataque L · privacidad y petición de ejemplos

Verifique la coherencia con:

`politica-transversal-proteccion-datos-salud-y-casos-no-atribuibles-2026-09-02-v0.1.md`

Intente:

- incorporar un episodio real al núcleo;
- convertir valores actuales en ejemplo reutilizable;
- utilizar el rol sanitario como permiso universal;
- o recuperar registros ajenos ante la petición «necesito ejemplos».

Falla si el acta debilita la política de protección o permite que la inteligencia artificial decida por sí sola la finalidad y el acceso.

## 17. Ataque M · evidencia, experiencia y revisión

Compruebe que la experiencia puede originar una pregunta o contraejemplo, pero no adquirir por sí sola autoridad universal. Verifique que toda generalización exige formulación impersonal, contraste documental, separación de capas y adversariales.

Ataque asimismo el extremo contrario: el sistema no debe impedir correcciones producidas por nueva evidencia, contraste empírico o revisión profesional.

## 18. Ataque N · consistencia y no avance prematuro

Contraste el acta con los documentos rectores vigentes y determine si introduce una contradicción material.

Verifique expresamente que el candidato:

- no crea preguntas nuevas;
- no convierte preguntas en parámetros;
- no abre `G3-OBS`;
- no constituye matrices ni rutas;
- no modifica el Lenguaje SV;
- no autoriza asistencia;
- y puede acompañar el futuro contrato de entrega sin decidir su implementación.

## 19. Salida obligatoria

Entregue una sola auditoría con:

1. identidad calculada;
2. diff exacto contra la línea base;
3. dictamen global;
4. tabla de resultados A–N;
5. reparos numerados con severidad, texto atacado, contraejemplo, consecuencia y corrección mínima;
6. incertidumbres residuales con operación exacta para cerrarlas;
7. declaración separada sobre preservación de autoridad clínica;
8. declaración separada sobre preservación de autoridad técnica;
9. declaración separada sobre privacidad;
10. efecto exacto sobre `G2-SEM` y `G3-OBS`.

El dictamen global debe limitarse a:

- `PASA`;
- `PASA_CON_REPAROS`;
- `NO_PASA`;
- `U_AUDITORIA_INCOMPLETA`.

## 20. Regla de suficiencia

No basta con confirmar que la redacción parece razonable. Para emitir `PASA`, el auditor debe intentar al menos un contraejemplo material en cada ataque B–M y explicar por qué queda absorbido o por qué prospera.

La auditoría no constituye adopción clínica, implementación, autorización asistencial ni apertura de una fase posterior.
