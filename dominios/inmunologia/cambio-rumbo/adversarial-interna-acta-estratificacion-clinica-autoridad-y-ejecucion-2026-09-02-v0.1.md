# Adversarial interna del acta de estratificación clínica, autoridad y ejecución computacional

- **Versión:** 0.1
- **Fecha de corte:** 02-09-2026
- **Objeto atacado:** `acta-estratificacion-clinica-autoridad-y-ejecucion-computacional-inmunologia-2026-09-02-v0.1.md`
- **Método:** falsación semántica, clínica, institucional, técnica, operativa y de privacidad
- **Dictamen:** `PASA_PARA_CONSTITUCION_RECTOR`

## 1. Pregunta adversarial

¿La estratificación propuesta conserva la autoridad clínica y la identidad semántica sin inutilizar la ingeniería, ocultar restricciones reales, contaminar el núcleo con singularidades ni convertir el sistema en carga administrativa?

## 2. Ataques

| Ataque | Intento de falsación | Resultado | Evidencia en el acta |
|---|---|---|---|
| A · paciente convertido en átomo | introducir valores individuales en la definición general | resiste | §§3.1, 3.4 y `INV-01`–`INV-03` separan núcleo e episodio |
| B · hospital convertido en clínica universal | elevar un protocolo o recurso local a regla general | resiste | §3.3 y `INV-02` impiden que la configuración institucional redefina el núcleo |
| C · IA convertida en profesional | atribuir autoridad a quien calcula o presenta | resiste | §§3.5 y 5 limitan la IA a ejecución, explicación, abstención y escalado |
| D · programación por encima de la clínica | eliminar o fusionar una necesidad porque resulta incómoda de implementar | resiste | §§1, 5 y `INV-04` prohíben la sustitución semántica por conveniencia técnica |
| E · clínica por encima de la seguridad técnica | obligar a ejecutar un requisito inseguro o no verificable | resiste | §5.1 reconoce bloqueo técnico sin conceder autoridad clínica |
| F · aproximación silenciosa | ocultar una incompatibilidad entre capas y producir un resultado plausible | resiste | §4 exige `U`, abstención o escalado explícitos |
| G · administración como vector decisor | compensar riesgo clínico grave mediante coste, camas o demora | resiste | §6 separa viabilidad y lógica clínica y prohíbe la compensación |
| H · ignorancia de recursos reales | recomendar una vía general que el centro no puede ejecutar | resiste | §§3.3 y 6 obligan a configurar capacidad y mostrar el conflicto |
| I · medicina a demanda | confundir participación o consentimiento con elección clínicamente soberana | resiste | §5.2 reconoce participación sin convertir preferencia en indicación |
| J · interfaz invasiva | mostrar todo el catálogo en cada consulta | resiste | §7 impone retaguardia, excepción y divulgación progresiva |
| K · frame resumen encubridor | ocultar una `U` crítica bajo una vista agregada | resiste | §7 subordina el resumen a los frames constitutivos |
| L · experiencia convertida en evidencia | universalizar un caso conocido | resiste | §8 permite generar preguntas, pero exige formulación impersonal y contraste |
| M · fuga de datos | transportar el episodio al núcleo, ejemplos o memoria | resiste | §§3.4, 8, `INV-01`–`INV-03` y remisión a la política de protección |
| N · rol sanitario como acceso ilimitado | consultar registros ajenos al pedir ejemplos | resiste | `INV-11` remite a la jerarquía de fuentes y finalidad autorizada |
| O · congelación dogmática | impedir que nueva evidencia corrija la arquitectura | resiste | §§2, 8 y 11 permiten cambio explícito, versionado y adversarializado |
| P · avance prematuro | usar el acta para abrir observables o matrices | resiste | §10 declara expresamente que no abre `G3-OBS` ni constituye objetos posteriores |
| Q · customización como reescritura | alterar reglas clínicas bajo la etiqueta de adaptación | resiste | §3.6 sólo admite configuración institucional e instanciación protegida del episodio |
| R · pericia técnica como autoridad clínica | suponer que saber implementar permite decidir qué debe implementarse clínicamente | resiste | §5.1 declara nula la autoridad clínica y semántica de la implementación |

## 3. Contraejemplos de presión

### 3.1. Prueba no disponible localmente

Una ruta general exige conocer una variable, pero el centro no dispone de la prueba habitual.

- Resultado admisible: declarar la necesidad clínica, la carencia institucional y la alternativa autorizada o `U`.
- Resultado prohibido: borrar la necesidad o fingir que la indisponibilidad equivale a normalidad.

La arquitectura resiste por §§3.3, 4 y 6.

### 3.2. Requisito clínico no representable

La ingeniería demuestra que el lenguaje o motor vigente no puede expresar una dependencia sin pérdida.

- Resultado admisible: bloqueo técnico, expediente de requisito y conservación de `U`.
- Resultado prohibido: simplificar la dependencia sin autorización clínica y semántica.

La arquitectura resiste por §5.1 y `INV-12`.

### 3.3. Salida clínicamente extensa pero inútil

El sistema puede mostrar cien elementos trazables, aunque el episodio sólo activa dos vetos y una ausencia crítica.

- Resultado admisible: mostrar primero los tres elementos activos y permitir profundización.
- Resultado prohibido: trasladar al profesional la carga de buscar lo relevante.

La arquitectura resiste por §7.

### 3.4. Preferencia incompatible con la indicación

La persona atendida solicita una actuación que el profesional considera clínicamente improcedente.

- Resultado admisible: informar, documentar la preferencia y conservar la decisión clínica profesional.
- Resultado prohibido: convertir la preferencia en indicación automática.

La arquitectura resiste por §5.2.

## 4. Reparos

Ninguno.

## 5. Vigilancias para fases posteriores

1. `VIG-ARQ-01`: en `G3-OBS`, impedir que el observable elegido dependa exclusivamente de la disponibilidad de un centro.
2. `VIG-ARQ-02`: en la clasificación de matrices, verificar que la dimensión no nazca de una preferencia de interfaz o almacenamiento.
3. `VIG-ARQ-03`: en rutas críticas, separar formalmente veto clínico, bloqueo técnico y restricción institucional.
4. `VIG-ARQ-04`: en la entrega al Lenguaje SV, exigir prueba de preservación semántica extremo a extremo.
5. `VIG-ARQ-05`: en interfaces, medir carga cognitiva y evitar divulgación masiva por defecto.

## 6. Compuertas

- **Privacidad:** `PRIVACIDAD_PASA`. El objeto es impersonal y no contiene episodios, instituciones o personas atribuibles.
- **Constitución prematura:** `NO`. No crea preguntas, parámetros, observables, matrices, rutas ni decisiones asistenciales.
- **Contaminación del Lenguaje SV:** `NO`. Sólo formula un contrato de entrega futuro.
- **Autoridad clínica:** `PRESERVADA`.
- **Autoridad técnica:** `PRESERVADA_Y_LIMITADA_A_SU_PLANO`.

## 7. Dictamen

`PASA_PARA_CONSTITUCION_RECTOR`

El acta resiste la adversarial interna. Se recomienda su publicación como regla de arquitectura y su incorporación expresa a la próxima auditoría externa que examine el paso desde preguntas semánticas a observables.
