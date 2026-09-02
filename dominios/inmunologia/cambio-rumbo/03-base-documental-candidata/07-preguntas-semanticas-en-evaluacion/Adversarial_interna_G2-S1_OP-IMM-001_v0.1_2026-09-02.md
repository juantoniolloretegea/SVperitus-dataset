# Adversarial interna G2-S1 — OP-IMM-001 v0.1

- **Fecha:** 02-09-2026
- **Puerta:** `G2-SEM`
- **Objeto:** primer lote semántico de 23 preguntas candidatas
- **Dictamen interno:** `PASA_PARA_AUDITORIA_EXTERNA`
- **Efecto máximo:** auditar G2-S1; no abrir `G3-OBS`

## 1. Ataques transversales

| Ataque | Intento de falsación | Resultado |
|---|---|---|
| Dependencia | introducir una pregunta interesante pero incapaz de cambiar el perfil o la ruta | cada candidata declara su dependencia con `OP-IMM-001` |
| Polisemia | usar «riesgo», «protección» o «adecuado» como si ya tuvieran umbral | evitados; los términos que exigen regla posterior quedan expresamente abiertos |
| Estado frente a exposición | mezclar condición del huésped con tratamiento propuesto | funciones y bloques separados |
| Estado frente a actuación | convertir antecedente o carencia en orden de prueba, vacuna o profilaxis | prohibido en cada frontera afectada |
| Control frente a parámetro | hacer de infección activa un vértice basal | `SEM-RUT-001` es control de salida, no estado del perfil |
| Contexto frente a riesgo | importar carga de enfermedad o urgencia como riesgo infeccioso | `SEM-CTX-001` sólo recibe el momento previsto; no copia sus determinantes |
| Código frente a autoridad | usar CIE-11, rareza o la etiqueta «inmunoterapia» para asignar especialidad o indicación | `SEM-CTX-002` conserva la tipificación como contexto y prohíbe esa inferencia |
| Coordinación frente a propiedad | convertir una necesidad inmunológica en liderazgo automático de Inmunología | `SEM-CTX-003` sólo registra la adjudicación profesional autorizada del episodio |
| Viabilidad frente a verdad clínica | convertir un protocolo o límite local en regla clínica universal o en ausencia de necesidad | `SEM-CTX-004` conserva la restricción institucional como contexto externo visible |
| Sinónimos | conservar dos preguntas idénticas por proceder de pilotos distintos | se crea una identidad candidata única para linfopenia, IgG, función esplénica y colonización |
| Colisión | forzar barreras, catéteres y prótesis dentro de una sola pregunta | separadas en cuatro candidatas |
| Herencia | trasladar `Pxx`, capas, estados o `T(25)=19` | no hallado |
| Matriz encubierta | presentar los seis bloques o veintitrés filas como dimensión | negado por texto y sin propiedad matricial |
| Consecuencia prematura | declarar daño clínico y gravedad antes de G4 | sólo consecuencia ex ante provisional común |
| Fuente prematura | elegir guía, prueba, umbral o ventana en G2 | no hallado |
| Paciente consumidor | introducir petición o preferencia como verdad clínica | excluido del lote y de la adjudicación del riesgo |

## 2. Ataques por familia

### 2.1. Ruta y contexto

- `SEM-RUT-001` no diagnostica infección: sólo formula si existe información que, bajo una regla autorizada futura, obliga a salir.
- `SEM-CTX-001` no decide la urgencia terapéutica. El calendario previsto es entrada de otra operación.
- `SEM-CTX-002` no diagnostica ni utiliza un código nosológico para decidir qué especialidad trata al paciente.
- `SEM-CTX-003` no presupone que Inmunología sea primera especialidad de contacto: distingue liderazgo, colaboración, interconsulta, participación diferida y ausencia de participación sin imponer la organización de un hospital o país.
- `SEM-CTX-004` no presupone que el procedimiento general sea ejecutable de la misma manera en todos los centros: exige identificar el protocolo y la capacidad locales sin permitir que éstos redefinan la verdad clínica.
- La condición de enfermedad rara se mantiene como posible metadato organizativo y no como estado del riesgo infeccioso.
- Una neoplasia correctamente tipada no vence la exclusión de quimioterapia citotóxica hematológica como régimen principal. Una propuesta terapéutica posterior distinta exige nueva adjudicación de alcance y no reescritura del episodio previo.
- El caso particular del Director no fija bazo, médula ósea, citometría ni participación del paciente como patrón.

### 2.2. Exposición propuesta

- identidad, magnitud y duración pueden divergir; no son sinónimos;
- exposiciones concurrentes no se suman todavía;
- glucocorticoides se aíslan porque los pilotos mezclaban exposición y evaluación preventiva;
- «conserve efecto» queda pendiente de regla temporal en G3 y no produce cierre en G2.

### 2.3. Estado del huésped

- linfopenia no hereda recuento, subpoblación ni umbral;
- IgG cuantitativa no equivale a competencia humoral funcional;
- respuesta humoral específica no equivale a vacunación administrada;
- anatomía esplénica y función esplénica permanecen bajo ataque: se admite que G3/G5 puedan separarlas.

### 2.4. Barreras y materiales

Se construyeron casos de divergencia conceptual:

- piel íntegra con mucosa alterada;
- mucosas íntegras con lesión cutánea;
- catéter presente sin prótesis;
- prótesis presente sin catéter.

Por ello no se conserva el compuesto histórico «barreras y catéteres».

### 2.5. Historia y exposición

- una infección puede ser grave sin ser oportunista;
- puede ser oportunista sin constituir recurrencia;
- puede existir recurrencia sin un único episodio grave;
- colonización no equivale a infección;
- exposición sanitaria no equivale a colonización.

Las tres preguntas de historia pueden compartir los mismos sucesos como fuente futura sin duplicarlos. La propiedad evaluada es distinta.

## 3. Casos adversos ejecutados

| Caso | Resultado exigido por el lote |
|---|---|
| infección sospechada hoy y antecedentes basales completos | salida por `SEM-RUT-001`; no se normaliza dentro del perfil |
| tratamiento identificado pero magnitud desconocida | `SEM-EXP-001` respondible; `SEM-EXP-002` conserva U futura independiente |
| duración conocida y combinación concurrente desconocida | `SEM-EXP-003` no cierra `SEM-EXP-004` |
| IgG cuantitativa disponible y respuesta específica desconocida | `SEM-HUE-002` no cierra `SEM-HUE-003` |
| esplenomegalia con función esplénica no constituida | `SEM-HUE-004` no se cierra por tamaño |
| piel íntegra y mucositis | `SEM-BAR-001` y `SEM-BAR-002` divergen |
| catéter presente sin infección | `SEM-BAR-003` no implica `SEM-RUT-001` |
| infección grave única no oportunista | `SEM-HIS-001` no cierra `SEM-HIS-002` ni `SEM-HIS-003` |
| colonización conocida sin infección | `SEM-HIS-004` no se convierte en diagnóstico |
| hospitalización previa sin colonización demostrada | `SEM-HIS-005` no cierra `SEM-HIS-004` |
| paciente solicita vacunación | no altera ninguna verdad clínica de `G2-S1`; la intervención pertenece a otra compuerta |
| código nosológico correcto, enfermedad rara y régimen principal excluido por G1 | `FUERA_DE_ALCANCE`; ni el código ni la rareza permiten reentrada |
| nueva propuesta farmacológica después de cerrar un episodio excluido | nueva adjudicación de alcance y versión; no mutación retrospectiva |
| Hematología dirige el episodio y solicita valoración inmunológica acotada | se registra dirección hematológica y participación consultiva de Inmunología; no se transfiere automáticamente el liderazgo |
| dos hospitales terciarios distribuyen de modo distinto la misma coordinación | se documenta la adjudicación vigente en cada episodio; la variación organizativa no altera por sí sola el estado biológico |
| la actuación clínicamente indicada no es ejecutable conforme al protocolo o los medios del centro | se muestra la incompatibilidad y se remite a decisión profesional sobre ruta, consulta o derivación; no se declara que la necesidad desaparece |
| un protocolo interno permite una actuación que el procedimiento general no sostiene | el protocolo local no crea por sí solo necesidad clínica ni autoridad para recomendarla |

## 4. Incertidumbres legítimas

| U | Contenido | Resolución permitida |
|---|---|---|
| `U-G2S1-01` | anatomía y función esplénica podrían requerir preguntas separadas | G3 y ataque de atomicidad G5 |
| `U-G2S1-02` | «efecto clínicamente activo» de exposición previa requiere ventana | G3-OBS |
| `U-G2S1-03` | «grave», «oportunista», «recurrente» y «pertinente» carecen aún de reglas operativas | G3-OBS y G4-CON |
| `U-G2S1-04` | el universo semántico total de la operación no está cerrado | lotes G2 posteriores |
| `U-G2S1-05` | la taxonomía operativa de liderazgo, participación compartida e interconsulta aún no está normalizada | lote posterior de gobernanza asistencial; no convertirla en parámetro de riesgo |
| `U-G2S1-06` | protocolo, versión, aplicabilidad y capacidades institucionales requieren una representación gobernada y local | lote posterior de contexto institucional; no incorporarlos a la matriz clínica |

Ninguna U se cierra por plausibilidad. Las tres primeras impiden usar las preguntas como parámetros; la cuarta impide declarar cobertura total.

## 5. Prueba de freno de mano

Se intentó añadir al lote:

- vacunación y profilaxis;
- comorbilidades generales;
- epidemiología ambiental;
- neutropenia;
- cohortes Nor-vaC, OCTAVE y SUCCEED;
- guías específicas de una enfermedad;
- parámetros derivados del caso particular del Director.

Se rechazó su incorporación en `G2-S1` porque no pertenece al objetivo acotado de este primer lote de colisiones. Se conserva como trabajo posterior posible, no como irrelevancia.

## 6. Dictamen

Las veintitrés preguntas son distinguibles como candidatas y mantienen separación entre estado, exposición, actuación, control y contexto. Ninguna ha sido convertida en parámetro, regla o matriz.

**Resultado: `PASA_PARA_AUDITORIA_EXTERNA`.**

No se abre `G3-OBS`. Tampoco se declara cerrado `G2-SEM` para toda `OP-IMM-001`.
