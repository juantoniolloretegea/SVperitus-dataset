# Lote semántico G2-S2 — OP-IMM-001 v0.1

- **Fecha:** 02-09-2026
- **Puerta:** `G2-SEM`
- **Antecedente:** `G2-S1_CERRADO`
- **Operación rectora:** `OP-IMM-001` v0.2
- **Estatuto:** `PREGUNTAS_CANDIDATAS_NO_ADJUDICADAS`
- **Objeto:** formular un segundo lote finito sobre compartimento neutrofílico y modificadores generales del huésped
- **Privacidad:** `PRIVACIDAD_PASA`; sólo casos abstractos y no atribuibles

## 1. Alcance y freno

`G2-S2` examina nueve preguntas excluidas de S1 que pueden modificar la interpretación del riesgo infeccioso, su consecuencia potencial o la ruta predecisional. No intenta completar todas las comorbilidades ni convertir diagnósticos generales en parámetros inmunológicos.

En esta puerta:

- no se asignan valores `0/1/U`;
- no se eligen pruebas, escalas o fuentes clínicas definitivas;
- no se fijan unidades, umbrales, ventanas ni reglas de pertinencia;
- no se constituye gravedad, causalidad o veto;
- no se adjudica atomicidad;
- no se asignan matrices, rutas críticas o frames;
- no se emite recomendación asistencial.

## 2. Procedencia

El lote responde a:

1. las exclusiones expresas de `G2-S1`;
2. la necesidad de atacar por separado los compuestos históricos de los pilotos;
3. la recomendación externa de continuar por compartimentos celulares, comorbilidades y reserva del huésped;
4. el límite de `OP-IMM-001`: sólo entra aquello que pueda cambiar el perfil o su ruta para la decisión concreta.

Los nombres y entradas de `IMMUNO-1` y `IMMUNO-2` son señales de búsqueda. No gobiernan las formulaciones y no transmiten estados, umbrales, ventanas o posiciones.

## 3. Funciones provisionales

| Función | Significado en G2-S2 |
|---|---|
| `CONTEXTO_BIOLOGICO` | condición de interpretación que no equivale por sí sola a riesgo cerrado |
| `ESTADO_DEL_HUESPED` | pregunta sobre un compartimento inmunológico del paciente |
| `MODIFICADOR_GENERAL` | condición clínica que puede alterar lectura, consecuencia o ruta sin convertirse automáticamente en déficit inmunitario |

## 4. Preguntas candidatas

| ID | Pregunta canónica candidata | Función provisional | Dependencia con `OP-IMM-001` | U propia posible | Exclusión expresa |
|---|---|---|---|---|---|
| `SEM-CTX-005` | ¿Está documentado el tramo de edad adulta pertinente para interpretar este episodio? | `CONTEXTO_BIOLOGICO` | la edad puede modificar referencias, reserva y lectura clínica sin alterar el límite adulto de la operación | edad, fecha de referencia o aplicabilidad desconocidas o discordantes | no convierte la edad cronológica en riesgo, fragilidad o contraindicación |
| `SEM-HUE-005` | ¿Existe una alteración del compartimento neutrofílico pertinente para el episodio? | `ESTADO_DEL_HUESPED` | el estado neutrofílico puede cambiar de manera independiente del linfocitario y del tratamiento propuesto | estado ausente, no vigente, discordante o no interpretable | no presupone recuento, función, duración, causa, umbral ni actuación |
| `SEM-MOD-001` | ¿Existe una condición metabólica pertinente que modifique la lectura del perfil infeccioso? | `MODIFICADOR_GENERAL` | una condición metabólica puede alterar susceptibilidad o evolución sin constituir por sí sola inmunodeficiencia | condición, control, vigencia o pertinencia desconocidos | no agrega diagnósticos metabólicos ni fija medida, umbral o tratamiento |
| `SEM-MOD-002` | ¿Existe una condición cardiovascular pertinente que modifique la consecuencia o la ruta del episodio? | `MODIFICADOR_GENERAL` | la reserva cardiovascular puede modificar tolerancia y escalado sin cambiar necesariamente la susceptibilidad inmunológica | condición, estabilidad, reserva o pertinencia desconocidas | no equivale a riesgo infeccioso, urgencia ni contraindicación automática |
| `SEM-MOD-003` | ¿Existe una alteración renal pertinente para la interpretación o ejecución del episodio? | `MODIFICADOR_GENERAL` | puede modificar reserva, exposición o viabilidad sin ser una decisión farmacológica | función, cronicidad, estabilidad o pertinencia desconocidas | no calcula función renal, ajusta dosis ni selecciona intervención |
| `SEM-MOD-004` | ¿Existe una condición pulmonar crónica pertinente que modifique el perfil o su consecuencia potencial? | `MODIFICADOR_GENERAL` | enfermedad y reserva respiratoria pueden divergir de otros modificadores y afectar la lectura | diagnóstico, función, estabilidad o pertinencia desconocidos | no diagnostica infección respiratoria, fija gravedad ni prescribe evaluación |
| `SEM-MOD-005` | ¿Existe una alteración hepática pertinente para la interpretación o ejecución del episodio? | `MODIFICADOR_GENERAL` | puede modificar reserva, exposición o viabilidad sin equivaler a inmunodeficiencia | función, cronicidad, estabilidad o pertinencia desconocidas | no calcula función hepática, ajusta dosis ni selecciona intervención |
| `SEM-MOD-006` | ¿Existe una alteración del estado nutricional pertinente para el episodio? | `MODIFICADOR_GENERAL` | el estado nutricional puede variar con independencia de la fragilidad y modificar reserva o susceptibilidad | estado, trayectoria, referencia o pertinencia desconocidos | no presupone escala, índice, etiología, umbral ni soporte nutricional |
| `SEM-MOD-007` | ¿Existe fragilidad o reducción de la reserva funcional pertinente para el episodio? | `MODIFICADOR_GENERAL` | la reserva funcional puede cambiar la tolerancia o la ruta aunque el estado nutricional sea distinto | estado basal, trayectoria, escala o pertinencia desconocidos | no equivale a edad, discapacidad, dependencia, nutrición ni decisión de limitar tratamiento |

## 5. Separaciones obligatorias

1. Edad no equivale a fragilidad.
2. Nutrición no equivale a reserva funcional.
3. Condición metabólica no equivale a condición cardiovascular o renal.
4. Diagnóstico de órgano no equivale a función, estabilidad o reserva.
5. Modificar la consecuencia o la ruta no equivale a modificar el estado inmunológico.
6. Una limitación de ejecución no elimina la necesidad clínica y permanece separada del protocolo institucional ya formulado en `SEM-CTX-004`.
7. El estado neutrofílico no se cierra por el estado linfocitario ni por la identidad del inmunosupresor.

## 6. Ambigüedades legítimas

El término «pertinente» no contiene una regla secreta. En G2 sólo declara que la pregunta debe demostrar dependencia con el episodio. Su regla operativa, fuente y ventana deberán atacarse después.

`SEM-HUE-005` permanece deliberadamente bajo vigilancia: cantidad, función, trayectoria y causa podrían exigir preguntas o parámetros distintos. La formulación actual identifica la familia semántica; no la declara atómica.

Las condiciones metabólicas, cardiovasculares, renales, pulmonares y hepáticas pueden contener más de una identidad futura. Ninguna fila autoriza agregarlas en un único estado ni tratarlas como inventario exhaustivo.

## 7. Residual declarado

Permanecen fuera de `G2-S2`:

- otros compartimentos leucocitarios o hematológicos cuya dependencia diferenciada no se ha constituido;
- diagnósticos concretos dentro de cada familia modificadora;
- embarazo y otras situaciones fisiológicas que exigen una operación o adjudicación propia;
- discapacidad, dependencia social y soporte informal;
- inmunización, protección, profilaxis, epidemiología y exposición ambiental;
- consentimiento, preferencias e intervención;
- seguimiento posterior al inicio.

La exclusión significa `PENDIENTE_DE_OTRO_LOTE_O_OPERACION`, no irrelevancia.

## 8. Consecuencia ex ante provisional

Si una pregunta pertinente se omite, se mezcla o se cierra sin evidencia, el perfil puede confundir susceptibilidad, reserva, consecuencia y viabilidad, o presentar una ruta incompleta. Esta formulación es una alerta estructural, no una consecuencia clínica plena ni una clasificación de gravedad.

## 9. Regla de parada

`G2-S2` puede cerrarse sólo cuando:

1. las nueve preguntas sean diferenciables;
2. los compuestos históricos estén separados o bajo vigilancia expresa;
3. ningún diagnóstico, prueba o escala haya sido elegido prematuramente;
4. ningún modificador se convierta en contraindicación o recomendación;
5. la compuerta de privacidad confirme ausencia de casos atribuibles y metadatos clínicos;
6. una auditoría externa intente falsar estas condiciones.

Cerrar `G2-S2` no cierra `G2-SEM` y no autoriza `G3-OBS`.

## 10. Declaración

Este lote formula preguntas candidatas. No constituye historia clínica, protocolo, recomendación, calculadora de riesgo, parámetro, matriz ni decisión sobre una persona.

## 11. Glosario

| Forma | Significado |
|---|---|
| `G2-SEM` | Puerta de formulación semántica de preguntas candidatas. |
| `G3-OBS` | Puerta posterior de observables y reglas candidatas. |
| `G5-ATM` | Puerta posterior de adjudicación de atomicidad. |
| IA | Inteligencia artificial. |
| SV | Sistema Vectorial SV. |
| U | Estado indeterminado legítimo. |

