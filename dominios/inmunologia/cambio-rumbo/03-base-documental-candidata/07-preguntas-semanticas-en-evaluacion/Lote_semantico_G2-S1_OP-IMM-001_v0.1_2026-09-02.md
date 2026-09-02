# Lote semántico G2-S1 — OP-IMM-001 v0.1

- **Fecha:** 02-09-2026
- **Puerta:** `G2-SEM`
- **Operación rectora:** `OP-IMM-001` v0.2
- **Estatuto:** `PREGUNTAS_CANDIDATAS_NO_ADJUDICADAS`
- **Objeto:** formular el primer lote finito de preguntas clínicas sin constituir todavía parámetros

## 1. Regla de esta puerta

Una pregunta entra en `G2-S1` sólo si puede cambiar la caracterización del perfil predecisional o la ruta estructural de `OP-IMM-001`. En esta puerta:

- no se asignan valores `0/1/U`;
- no se eligen pruebas ni fuentes clínicas definitivas;
- no se fijan unidades, umbrales o ventanas;
- no se constituye una consecuencia clínica plena;
- no se adjudica atomicidad;
- no se asigna propiedad matricial.

La mención de una posible `U` sólo demuestra que la pregunta admite falta o conflicto de información propio. No constituye aún su transductor.

## 2. Procedencia y límite de las semillas

El lote parte de:

1. la dependencia exigida por `OP-IMM-001` v0.2;
2. las colisiones y mezclas detectadas por `NA0` en los pilotos `IMMUNO-1` y `IMMUNO-2`;
3. la pertinencia profesional ya constituida en el catálogo INMUNO v0.8.

Los `Pxx` históricos sólo señalan dónde atacar. No son fuente clínica definitiva, no gobiernan la redacción y no conservan identificador, umbral, capa, matriz o estado.

## 3. Funciones semánticas provisionales

Las funciones siguientes ayudan a impedir mezclas; no son estatutos finales de atomicidad:

| Función | Significado en G2 |
|---|---|
| `CONTROL_DE_SALIDA` | pregunta que puede apartar el caso hacia otra operación |
| `CONTEXTO_EXTERNO` | dato de otra decisión clínica que delimita el episodio sin integrar el riesgo |
| `EXPOSICION_PROPUESTA` | aspecto de la inmunosupresión planificada que puede modificar la lectura |
| `ESTADO_DEL_HUESPED` | proposición sobre una función o condición del paciente |
| `BARRERA_O_DISPOSITIVO` | proposición sobre una puerta de entrada o material clínico |
| `HISTORIA_O_EXPOSICION` | proposición retrospectiva o contextual con posible relevancia actual |

## 4. Preguntas candidatas G2-S1

### 4.1. Fronteras de ruta y tiempo

| ID | Pregunta canónica candidata | Función provisional | Dependencia con `OP-IMM-001` | U propia posible | Exclusión expresa |
|---|---|---|---|---|---|
| `SEM-RUT-001` | ¿Existe información compatible con un proceso infeccioso en curso que, conforme a una regla clínica autorizada, obligue a salir de `OP-IMM-001`? | `CONTROL_DE_SALIDA` | impide absorber un problema agudo dentro del perfil basal | información ausente, discordante o no valorable | no diagnostica, clasifica ni trata la infección |
| `SEM-CTX-001` | ¿Está documentado el momento clínicamente previsto para el inicio propuesto de la inmunosupresión? | `CONTEXTO_EXTERNO` | delimita el horizonte al que debe referirse el perfil | fecha o prioridad no fijada o contradictoria | no decide la urgencia ni reproduce la carga de la enfermedad que la origina |
| `SEM-CTX-002` | ¿Están identificadas la entidad nosológica de base que motiva la propuesta terapéutica y la terminología versionada con la que se registra? | `CONTEXTO_EXTERNO` | evita interpretar la exposición fuera de la enfermedad y del corte terminológico declarados | diagnóstico provisional, discordante, no tipado o sin versión | no diagnostica, no adjudica indicación y ningún código asigna por sí solo una especialidad responsable |

`SEM-CTX-001` recibe una salida de la decisión terapéutica de origen. El tamaño esplénico, la infiltración medular u otros determinantes de necesidad o urgencia pertenecen a esa operación externa; no se importan como riesgo infeccioso por el solo hecho de haber condicionado el calendario.

`SEM-CTX-002` tampoco convierte la condición de enfermedad rara en estado clínico del perfil. Esa condición puede activar metadatos o circuitos organizativos —por ejemplo, derivación, centro experto, registro o investigación—, pero no modifica por sí sola el riesgo biológico, la indicación ni la competencia profesional. Del mismo modo, llamar «inmunoterapia» a un tratamiento no atribuye automáticamente su indicación o administración a un servicio de Inmunología.

La tipificación tampoco vence el ámbito negativo de G1. Si la propuesta principal es quimioterapia citotóxica de una neoplasia hematológica, el episodio queda fuera de `OP-IMM-001`. Una propuesta terapéutica posterior materialmente distinta no reabre ni reescribe el episodio anterior: exige nueva adjudicación de alcance y, cuando proceda, un nuevo episodio versionado.

### 4.2. Exposición inmunosupresora propuesta

| ID | Pregunta canónica candidata | Función provisional | Dependencia con `OP-IMM-001` | U propia posible | Exclusión expresa |
|---|---|---|---|---|---|
| `SEM-EXP-001` | ¿Está identificado el tratamiento inmunosupresor sistémico primario propuesto? | `EXPOSICION_PROPUESTA` | sin identidad de la exposición no puede referirse el perfil a la propuesta real | tratamiento no fijado, ambiguo o discordante | no elige ni recomienda el tratamiento |
| `SEM-EXP-002` | ¿Está caracterizada la magnitud planificada de exposición al tratamiento primario? | `EXPOSICION_PROPUESTA` | una misma identidad farmacológica puede tener exposiciones distintas | pauta incompleta, variable o no verificable | no fija dosis ni umbral de riesgo |
| `SEM-EXP-003` | ¿Está caracterizada la duración planificada de la exposición primaria? | `EXPOSICION_PROPUESTA` | duración e identidad pueden divergir y no deben colapsarse | duración abierta, condicional o no documentada | no define la ventana válida ni decide continuidad |
| `SEM-EXP-004` | ¿Está identificada cualquier otra exposición inmunomoduladora concurrente o previa que siga siendo clínicamente activa para este episodio? | `EXPOSICION_PROPUESTA` | una exposición adicional puede modificar el perfil sin cambiar el tratamiento primario | exposición, concurrencia o vigencia desconocida | «activa para el episodio» exige regla temporal posterior; no agrega todas las exposiciones en un único estado |
| `SEM-EXP-005` | ¿Está caracterizada por separado la exposición sistémica a glucocorticoides cuando forme parte de la propuesta o conserve efecto para el episodio? | `EXPOSICION_PROPUESTA` | los pilotos mezclaban dosis, duración y evaluación preventiva | exposición o vigencia desconocida | no calcula equivalencias, dosis de riesgo ni indicación preventiva |

`SEM-EXP-002`, `SEM-EXP-003` y `SEM-EXP-005` pueden compartir documentos de medicación, pero no son sinónimos: magnitud, duración e identidad específica pueden variar independientemente.

### 4.3. Estado inmunitario del huésped

| ID | Pregunta canónica candidata | Función provisional | Dependencia con `OP-IMM-001` | U propia posible | Exclusión expresa |
|---|---|---|---|---|---|
| `SEM-HUE-001` | ¿Existe una alteración cuantitativa del compartimento linfocitario pertinente para el episodio? | `ESTADO_DEL_HUESPED` | los pilotos duplicaban linfopenia con reglas y contextos distintos | estado no medido, no vigente o discordante | no presupone qué recuento, subpoblación o umbral la constituye |
| `SEM-HUE-002` | ¿Existe una alteración cuantitativa de inmunoglobulina G pertinente para el episodio? | `ESTADO_DEL_HUESPED` | los pilotos duplicaban la misma magnitud con funciones aparentes distintas | valor ausente, no vigente, discordante o no interpretable | no equivale a competencia humoral funcional ni a respuesta vacunal |
| `SEM-HUE-003` | ¿Existe una alteración de la respuesta humoral específica pertinente para el episodio? | `ESTADO_DEL_HUESPED` | una concentración global y una respuesta específica pueden divergir | respuesta no evaluada, no interpretable o no vigente | no equivale a vacunación administrada ni a inmunoglobulina G total |
| `SEM-HUE-004` | ¿Existe pérdida anatómica o funcional de la función esplénica pertinente para el perfil infeccioso? | `ESTADO_DEL_HUESPED` | corrige la duplicación de función esplénica entre pilotos | anatomía o función no documentada o discordante | el tamaño esplénico o la carga de enfermedad no bastan por sí solos para cerrar esta pregunta |

La alternativa anatómica o funcional de `SEM-HUE-004` se conserva como hipótesis de evidencias distintas para una misma función clínica. `G3-OBS` y `G5-ATM` deberán intentar demostrar que en realidad son preguntas separables.

### 4.4. Barreras y materiales clínicos

| ID | Pregunta canónica candidata | Función provisional | Dependencia con `OP-IMM-001` | U propia posible | Exclusión expresa |
|---|---|---|---|---|---|
| `SEM-BAR-001` | ¿Existe una alteración de la integridad cutánea pertinente para el perfil infeccioso? | `BARRERA_O_DISPOSITIVO` | piel y mucosas se colapsaban históricamente bajo una sola posición | estado cutáneo no valorado o no documentado | no incluye mucosas, catéteres o prótesis |
| `SEM-BAR-002` | ¿Existe una alteración de la integridad mucosa pertinente para el perfil infeccioso? | `BARRERA_O_DISPOSITIVO` | puede divergir de la integridad cutánea | estado mucoso no valorado o no documentado | no incluye piel, catéteres o prótesis |
| `SEM-BAR-003` | ¿Existe un dispositivo intravascular presente que sea pertinente para el perfil infeccioso del episodio? | `BARRERA_O_DISPOSITIVO` | separa dispositivo de lesión de barrera | presencia, tipo o vigencia no verificable | no presupone infección, colonización ni necesidad de retirada |
| `SEM-BAR-004` | ¿Existe una prótesis u otro biomaterial implantado pertinente para el perfil infeccioso del episodio? | `BARRERA_O_DISPOSITIVO` | evita hacer equivaler todo material a un catéter | presencia, tipo o vigencia no verificable | no presupone infección, colonización ni actuación |

### 4.5. Historia infecciosa, colonización y exposición sanitaria

| ID | Pregunta canónica candidata | Función provisional | Dependencia con `OP-IMM-001` | U propia posible | Exclusión expresa |
|---|---|---|---|---|---|
| `SEM-HIS-001` | ¿Existe antecedente de infección grave pertinente para el episodio? | `HISTORIA_O_EXPOSICION` | una historia grave puede modificar la lectura basal | historia ausente, gravedad o pertinencia no adjudicables | no define todavía «grave», ventana ni microorganismo |
| `SEM-HIS-002` | ¿Existe antecedente de infección oportunista pertinente para el episodio? | `HISTORIA_O_EXPOSICION` | oportunismo y gravedad no son sinónimos y pueden divergir | clasificación o historia desconocida | no agrega infecciones graves no oportunistas |
| `SEM-HIS-003` | ¿Existe un patrón de infecciones recurrentes pertinente para el episodio? | `HISTORIA_O_EXPOSICION` | recurrencia no equivale a un único episodio grave | episodios incompletos o patrón no adjudicable | no fija número, intervalo o etiología |
| `SEM-HIS-004` | ¿Existe colonización conocida por un microorganismo con resistencia clínicamente pertinente para el episodio? | `HISTORIA_O_EXPOSICION` | separa estado de colonización de estrategia de manejo | estado, vigencia o resistencia no verificables | no prescribe cribado ni profilaxis y no equivale a infección activa |
| `SEM-HIS-005` | ¿Existe una exposición sanitaria previa pertinente para el episodio? | `HISTORIA_O_EXPOSICION` | hospitalización o procedimiento previo puede ser contexto sin convertirse en infección | exposición o ventana desconocida | no equivale a colonización, infección ni riesgo cerrado |

`SEM-HIS-001`, `SEM-HIS-002` y `SEM-HIS-003` pueden proyectarse sobre los mismos sucesos clínicos, pero preguntan por propiedades distintas. No se duplicará la historia: en fases posteriores deberán compartir hechos con relaciones tipadas.

## 5. Dependencia y consecuencia ex ante provisional

Para las veintiuna preguntas, la dependencia común es limitada:

> Si la pregunta pertinente se omite, se mezcla con otra o se cierra sin evidencia, el perfil predecisional puede representar de forma incompleta o engañosa el estado, la exposición o la ruta del paciente.

Ésta es una consecuencia ex ante provisional de error documental y clínico-estructural. No constituye todavía gravedad, mecanismo causal, veto ni consecuencia clínica plena; corresponde atacarlos en `G4-CON`.

## 6. Exclusiones del lote

`G2-S1` no incluye todavía:

- neutrófilos y otros compartimentos no afectados por las colisiones prioritarias de este lote;
- comorbilidades y modificadores generales del huésped;
- exposiciones geográficas, ambientales, ocupacionales o convivenciales;
- inmunización administrada, protección demostrada y estrategia vacunal;
- profilaxis antimicrobiana;
- suficiencia global del perfil;
- aceptación o rechazo del paciente;
- condición de enfermedad rara como supuesto parámetro clínico o regla automática de derivación;
- elección, indicación o ejecución de pruebas e intervenciones;
- ni seguimiento después del inicio.

La exclusión significa `PENDIENTE_DE_OTRO_LOTE_O_OPERACION`, no irrelevancia clínica.

## 7. Regla de parada del lote

El lote se cierra cuando:

1. las veintiuna preguntas tienen una formulación diferenciable;
2. ninguna hereda un estado, umbral o matriz de los pilotos;
3. las colisiones prioritarias quedan explícitas;
4. toda ambigüedad que dependa de observables o fuentes se remite a G3 sin fingir resolución;
5. y una adversarial externa confirma que no se ha constituido prematuramente un parámetro.

Cerrar `G2-S1` no cierra el universo completo de preguntas de `OP-IMM-001` ni autoriza `G3-OBS`.

## 8. Declaración

Este lote formula preguntas candidatas para evaluación estructural. No es protocolo asistencial, catálogo de pruebas, recomendación preventiva, calculadora de riesgo ni decisión sobre un paciente.

## 9. Glosario de continuidad

| Forma | Significado |
|---|---|
| `G2-SEM` | Puerta de formulación semántica de preguntas candidatas. |
| `G3-OBS` | Puerta posterior de observables y reglas candidatas. |
| IgG | Inmunoglobulina G. |
| IA | Inteligencia artificial. |
| SV | Sistema Vectorial SV. |
| U | Estado indeterminado legítimo. |
