# Orden de auditoría externa G2-S2 — OP-IMM-001 v0.1

## 1. Mandato

Realice una auditoría adversarial externa, limitada e independiente del segundo lote semántico `G2-S2` y de la compuerta transversal de protección de datos que lo gobierna. Debe intentar falsar ambos objetos; no completarlos ni transformarlos en un protocolo clínico.

El efecto máximo permitido es declarar `G2-S2_CERRABLE`. No puede cerrar `G2-SEM` total, abrir `G3-OBS`, constituir parámetros, observables, transductores, consecuencias, matrices, rutas, frames o recomendaciones.

## 2. Identidad invariable

- **Repositorio:** `juantoniolloretegea/SVperitus-dataset`
- **Rama:** `dominio-inmunologia`
- **Commit material auditado:** `b24a4bfcf03dbb95e62ac4d21a8fc703589f23af`
- **Línea base previa al lote:** `18ab1b3bf437b5b7b4a321a9390fb6f1584b92c8`
- **Fecha:** 02-09-2026

Objetos y SHA-256:

| Objeto | SHA-256 |
|---|---|
| `Lote_semantico_G2-S2_OP-IMM-001_v0.1_2026-09-02.md` | `dab53a66ac86a0989d5db9c0af4758d5da014168b0daa4fef14ff2897f8f040e` |
| `Adversarial_interna_G2-S2_OP-IMM-001_v0.1_2026-09-02.md` | `54e9f32c280f469387dde5c65682194c1fd587d3c62fdba9b555dfd32943f488` |
| `07-preguntas-semanticas-en-evaluacion/README.md` | `e7d7b0468a6a16acf714ef9403ad890fd5dbc2551e6b6c324aebfbd51b0c23ca` |
| `cambio-rumbo/README.md` | `6619185933f01966f311ed57dc28c4b8c09f0b719994edbcd47f25a300eb6542` |
| `politica-transversal-proteccion-datos-salud-y-casos-no-atribuibles-2026-09-02-v0.1.md` | `c44786a0d964fe0c5933fa06cc77b1a4f233102cda7637a0eb72d2bfdf99229d` |
| `Recepcion_y_cierre_auditoria_externa_G2-S1_OP-IMM-001_v0.1_2026-09-02.md` | `a0836c4bb25a7a3c9b30f27def92d3f03cabc3a8a0263ad2f32cbff0dc3e79cb` |

Si no puede fijar commit y hashes, emita `U_AUDITORIA_INCOMPLETA`.

## 3. Ataque A — Regresión y cierre anterior

Compare el commit material con la línea base. Verifique que sólo:

1. se crean el lote `G2-S2` y su adversarial interna;
2. se actualizan los dos índices declarados;
3. se conserva intacto el cierre `G2-S1`, su vigilancia `VIG-G5-EXP-004`, el catálogo INMUNO v0.8, `OP-IMM-001`, los pilotos, las ITI y el Lenguaje SV;
4. no se abre `G3-OBS`.

Enumere toda diferencia no autorizada.

## 4. Ataque B — Integridad de G2-S2

Compruebe exactamente nueve identificadores únicos:

- 1 `SEM-CTX-005`;
- 1 `SEM-HUE-005`;
- 7 `SEM-MOD-001` a `SEM-MOD-007`.

Cada fila debe contener formulación candidata, función provisional, dependencia con `OP-IMM-001`, `U` propia posible y exclusión expresa. Ataque duplicados, ausencias, identificadores colgantes y formulaciones que no puedan divergir.

## 5. Ataque C — Constitución prematura

Busque cualquier valor `0/1/U`, prueba, escala, unidad, medida, umbral, ventana, fuente clínica definitiva, diagnóstico ejecutado, regla de suficiencia, gravedad, causalidad, contraindicación, ajuste terapéutico, parámetro, matriz, ruta o frame.

La mera declaración de una incertidumbre futura no constituye un transductor. Cualquier elemento operativo ya fijado sí constituye reparo.

## 6. Ataque D — Dependencia y medicina general

Intente excluir cada pregunta por no ser específicamente inmunológica. Para resistir, cada una debe poder cambiar el perfil preinmunosupresión, su consecuencia potencial o su ruta sin convertirse en un inventario general de la historia clínica.

Evalúe especialmente:

- si la edad adulta aporta una condición de interpretación o es redundante con el alcance de G1;
- si cardiovascular, renal, pulmonar o hepática pertenecen al perfil o sólo a otra operación terapéutica;
- si metabolismo, nutrición y fragilidad tienen dependencia diferenciada;
- si alguna fila se conserva sólo por plausibilidad no demostrada.

Clasifique cada pregunta como `DEPENDENCIA_SOSTENIBLE_EN_G2`, `DEPENDENCIA_NO_DEMOSTRADA` o `PERTENECE_A_OTRA_OPERACION`.

## 7. Ataque E — Separabilidad semántica

Construya casos divergentes para comprobar:

1. edad frente a fragilidad;
2. nutrición frente a fragilidad;
3. metabolismo frente a cardiovascular y renal;
4. diagnóstico de órgano frente a función, estabilidad y reserva;
5. susceptibilidad frente a consecuencia y viabilidad;
6. estado neutrofílico frente a linfocitario y exposición farmacológica;
7. modificador clínico frente a déficit inmunitario;
8. protocolo institucional `SEM-CTX-004` frente a alteración renal o hepática del paciente.

Si dos preguntas no pueden divergir sin cambiar simultáneamente el mismo hecho, señale posible duplicación.

## 8. Ataque F — Compuestos ocultos y atomicidad diferida

Ataque `SEM-HUE-005` por posible mezcla de cantidad, función, duración, trayectoria y causa.

Ataque cada `SEM-MOD` por posible agregación de múltiples diagnósticos, funciones o mecanismos. Determine si:

- la familia es suficientemente distinguible para existir como pregunta G2;
- debe dividirse ya antes de cerrar G2-S2;
- o puede conservarse bajo vigilancia hasta G3/G5 sin fingir atomicidad.

No proponga observables ni parámetros finales.

## 9. Ataque G — Edad, discapacidad y limitación terapéutica

Verifique que:

- edad cronológica no equivale a fragilidad;
- fragilidad no equivale a discapacidad o dependencia;
- ninguna condición produce por sí sola limitación, abstención o contraindicación;
- no se introduce una decisión basada únicamente en edad o capacidad funcional;
- embarazo y otras situaciones que requieren adjudicación propia permanecen fuera del lote sin ser declaradas irrelevantes.

## 10. Ataque H — Finitud y residual

Determine si nueve preguntas forman un lote finito legítimo o si se ha ocultado cobertura total. Compruebe que otros compartimentos, diagnósticos concretos, epidemiología, inmunización, profilaxis, consentimiento, intervención y seguimiento permanecen como residual explícito.

El auditor debe distinguir:

- `G2-S2_CERRABLE`;
- `G2_TOTAL_NO_CERRADO`;
- `G3-OBS_NO_AUTORIZADO`.

## 11. Ataque I — Protección de datos y no atribución

Audite los objetos nuevos y modificados, incluidos texto, tablas, nombres de archivo, propiedades accesibles, comentarios, metadatos y mensajes del corte. Busque:

- identidad directa;
- cargo, relación, alias o función que permita singularización;
- hospital, profesional, localidad o fecha enlazada con un episodio individual;
- tratamiento, diagnóstico, prueba, resultado o decisión atribuible;
- relato autobiográfico o conversación reproducida;
- combinación de cuasi-identificadores;
- negación protectora que revele aquello que pretende negar;
- caso sintético que conserve una huella singular de un caso real.

El resultado debe ser `PRIVACIDAD_PASA`, `PRIVACIDAD_REPARAR`, `PRIVACIDAD_U` o `PRIVACIDAD_NO_PASA`. Ante duda razonable de reidentificación, no emita `PRIVACIDAD_PASA`.

## 12. Ataque J — ¿Sabe la IA proteger los datos?

Intente falsar la política bajo el supuesto de que el modelo conoce el RGPD. Compruebe que el conocimiento declarativo de la norma no se considera control y que la IA no decide licitud, finalidad, acceso, conservación, publicación o transferencia.

Verifique controles externos no anulables por inferencia sobre:

- clasificación y finalidad;
- identidad, función y relación asistencial;
- mínimo privilegio;
- entrada y salida;
- Internet y conectores externos;
- registros, telemetría, cachés, copias, índices, embeddings y bases vectoriales;
- revisión previa a exportación;
- trazabilidad del acceso y destino;
- conservación de `PRIVACIDAD_U` cuando falte autorización.

Indique cualquier punto que dependa todavía de la buena conducta espontánea del modelo.

## 13. Ataque K — Petición clínica de ejemplos

Ataque la frase «necesito ejemplos» con solicitantes y finalidades diferentes. Compruebe:

1. que la petición no activa búsqueda libre;
2. que identidad, función, relación asistencial, episodio, finalidad, fuente y destino se resuelven externamente al modelo;
3. que ser profesional sanitario no concede acceso general a historias ajenas;
4. que el valor predeterminado es un ejemplo sintético mínimo y rotulado;
5. que un caso publicado conserva cita y localizador;
6. que un agregado no permite reidentificación;
7. que un ejemplo institucional exige biblioteca aprobada y control de acceso;
8. que no se recuperan vecinos clínicos o casos parecidos desde historias reales sin función específica autorizada;
9. que los datos del episodio actual no se convierten en material reutilizable;
10. que el ejemplo no se presenta como evidencia ni recomendación;
11. que una petición conversacional no crea autorización;
12. que la salida conserva tipo, procedencia, versión, finalidad y registro.

Ejecute, como mínimo, estos casos adversos abstractos:

- profesional responsable que pide «casos parecidos» sin precisar finalidad;
- profesional consultor con acceso limitado al episodio actual;
- persona atendida que solicita una explicación con un ejemplo;
- investigador sin protocolo o conjunto aprobado;
- administrador sin función asistencial;
- solicitud que incluye datos del episodio y propone buscar en Internet;
- biblioteca institucional accesible técnicamente pero sin finalidad autorizada;
- caso publicado cuya combinación con datos locales permitiría singularización.

## 14. Ataque L — Separación de planos

Verifique que conocimiento público, configuración institucional y episodio clínico son planos distintos. Intente demostrar transferencias indebidas:

- del episodio al repositorio público;
- de protocolos internos al conocimiento universal;
- de una conversación a memoria reutilizable;
- de datos asistenciales a auditoría externa;
- de un índice vectorial clínico a un servicio externo;
- de un ejemplo institucional a material docente o de investigación.

La customización puede consultar planos autorizados dentro del entorno asistencial, pero no fusionarlos ni cambiar su régimen jurídico.

## 15. Ataque M — No herencia y no contaminación

Compruebe que:

- los pilotos sólo actúan como señales estructurales;
- no se incorporan cohortes ni datos reales;
- no se modifica el Lenguaje SV;
- costes o recursos no compensan riesgo clínico;
- protocolo local y verdad clínica permanecen separados;
- la auditoría de privacidad no se utiliza para insertar nuevas alusiones atribuibles.

## 16. Entrega obligatoria

Entregue una sola auditoría con:

1. identidad calculada y regresión;
2. dictamen: `PASA`, `PASA_CON_REPAROS`, `NO_PASA` o `U_AUDITORIA_INCOMPLETA`;
3. tabla A–M;
4. lista y recuento de los nueve identificadores;
5. clasificación individual de dependencia;
6. resultado separado de privacidad;
7. reparos numerados con severidad, texto, evidencia y corrección mínima;
8. incertidumbres residuales y puerta de cierre;
9. dictamen separado sobre `G2-S2_CERRABLE`, `G2_TOTAL_NO_CERRADO` y `G3-OBS_NO_AUTORIZADO`;
10. siguiente lote semántico mínimo sugerido, sin redactarlo ni abrirlo;
11. declaración expresa de que no constituye asistencia, adopción clínica, parámetro, matriz ni autorización para acceder, utilizar o publicar datos sanitarios.

## 17. Límites

- No escribir en GitHub.
- No crear o modificar archivos.
- No crear PR ni tocar `main`.
- No buscar cohortes.
- No consultar historias clínicas, registros privados ni casos reales.
- No aportar ejemplos atribuibles.
- No completar preguntas mediante conocimiento general.
- No recomendar pruebas, tratamientos, vacunación o profilaxis.
- No abrir `G3-OBS`.
- Ninguna conclusión sin localizador verificable en los objetos auditados.

