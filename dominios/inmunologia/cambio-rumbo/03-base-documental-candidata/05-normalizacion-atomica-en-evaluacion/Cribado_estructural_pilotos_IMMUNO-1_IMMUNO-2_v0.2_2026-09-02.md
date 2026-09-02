# Cribado estructural adversarial de los pilotos IMMUNO-1 e IMMUNO-2 v0.2

- **Fecha:** 02-09-2026
- **Compuerta:** `NA0`
- **Estatuto:** `MAPA_DE_ATAQUE_NO_CONSTITUTIVO`
- **Objetos leídos:** YAML, motores normativos Python y especificación P01–P25 disponibles en `agentes/inmunologia/`; copia de control de `FTD-AE-IMM-SV/0.3`, SHA-256 `8d682a24b6ee24151d7f4382037ca34962b60cc0da2a97b67850c112291e8f4a`
- **Regla:** un identificador `Pxx` histórico no equivale por sí solo a parámetro atómico ratificado

## 1. Resultado ejecutivo

Los pilotos contienen 50 posiciones nominales: 25 en `IMMUNO-1` y 25 en `IMMUNO-2`.

- 19 funciones leen un único campo de entrada.
- 31 funciones leen entre dos y cinco campos.
- El número de campos es una señal estructural, no un dictamen de atomicidad.
- Existen al menos ocho familias de colisión entre fases.
- `IMMUNO-2/P25` es una salida puente derivada de `IMMUNO-1`, no un observable clínico basal ordinario.
- La especificación de `IMMUNO-2/P02` declara expresamente que el parámetro es compuesto por conveniencia dimensional.
- La síntesis recibida de la pre-ITI `FTD-AE-IMM-SV/0.3` contiene una sola fila `IMMUNO-1/P11`. La afirmación contraria de v0.1 queda retractada: fue un falso positivo producido al solapar la línea 230 en dos intervalos de inspección (`1–230` y `230–360`).

Consecuencia: no procede trasladar las dos células `SV(25,5)` al dominio normalizado sin despiece, deduplicación y pruebas A1–A6.

## 2. Rectificación adversarial de v0.1

La fuente exacta contiene 812 líneas y una sola coincidencia material de la fila `IMMUNO-1/P11`. Su copia de control, idéntica byte a byte al archivo recibido, se conserva en:

`fuentes-recibidas/FTD-AE-IMM-SV_0.3_2026-04-15_copia-control.md`

La rectificación no altera los recuentos 25+25, 19/31, las ocho familias de colisión, la naturaleza compuesta de `IMMUNO-2/P02`, el agregado de `IMMUNO-2/P24`, el puente `IMMUNO-2/P25` ni la no ratificación de `T(25)=19`.

## 3. Alertas prioritarias

| Objeto | Señal adversarial | Ataque obligado |
|---|---|---|
| `IMMUNO-1/P04` | mezcla estado esplénico, cobertura vacunal y profilaxis | divergencia, U y consecuencia independientes |
| `IMMUNO-1/P05` | une barreras mucosas/cutáneas y catéter vascular | separación por familia y ruta |
| `IMMUNO-1/P08` | agentes biológicos más cribado viral | exposición frente a control |
| `IMMUNO-1/P09` | TPH, CAR-T, EICH, tiempo y programa de revacunación/profilaxis | despiece de tratamiento, estado y control |
| `IMMUNO-1/P10` | dosis/duración de corticoide más evaluación de riesgo PJP | exposición frente a control |
| `IMMUNO-1/P11–P15` | varios antecedentes se mezclan con revisión o estrategia de manejo | historia clínica frente a adecuación de actuación |
| `IMMUNO-1/P20` | adecuación de vacunas inactivadas y administración contraindicada de vacuna viva | dos preguntas y consecuencias potencialmente distintas |
| `IMMUNO-2/P02` | compuesto deliberado de diabetes, cardiopatía e insuficiencia renal | rechazar la conveniencia dimensional como justificación suficiente |
| `IMMUNO-2/P03–P05` | agregan enfermedades o estados heterogéneos | divergencia, U y consecuencia independientes |
| `IMMUNO-2/P08` | dosis, duración y pulsos de corticoides | decidir si son observables de una exposición única o subparámetros |
| `IMMUNO-2/P10` | recuento linfocitario condicionado por dos tratamientos | separar observable, contexto y regla |
| `IMMUNO-2/P24` | un solo campo informático resume una evaluación integral | atacar composición oculta pese a entrada única |
| `IMMUNO-2/P25` | clase global de otra célula | tipar como puente; prohibir duplicación y cierre sin dictamen origen válido |

## 4. Colisiones entre pilotos

| Familia | IMMUNO-1 | IMMUNO-2 | Riesgo |
|---|---|---|---|
| Linfopenia | `P02` | `P10` | duplicación con reglas y contextos distintos |
| Inmunoglobulina G | `P03` | `P22` | misma magnitud con función aparente distinta |
| Función esplénica | `P04` | `P15` | duplicación expresamente reconocida en el piloto |
| Barreras/catéter | `P05` | `P11`, `P12` | un compuesto histórico frente a dos posiciones |
| Corticoides | `P10` | `P08` | misma exposición con umbrales/contextos distintos |
| Infección grave previa | `P11` | `P21` | ventana y definición deben unificarse o tiparse |
| Colonización multirresistente | `P14` | `P17` | estado frente a estado más estrategia |
| Hospitalización/exposición sanitaria | `P15` | `P16` | contexto temporal y actuación mezclados |

Una colisión no implica que una posición deba desaparecer. Obliga a decidir si existe una identidad canónica compartida con proyecciones, dos parámetros diferentes o una relación tipada.

## 5. Inventario estructural completo

`Entradas` cuenta claves distintas obtenidas mediante `_get` en el motor histórico. `MULTI` no significa automáticamente compuesto y `SIMPLE` no significa automáticamente atómico.

| Piloto | ID | Nombre histórico | Entradas | Señal inicial |
|---|---|---|---:|---|
| IMMUNO-1 | P01 | Neutropenia | 3 | MULTI |
| IMMUNO-1 | P02 | Linfopenia | 3 | MULTI |
| IMMUNO-1 | P03 | Inmunoglobulinas | 2 | MULTI |
| IMMUNO-1 | P04 | Esplenectomía / hipoesplenismo | 4 | MULTI-ALERTA |
| IMMUNO-1 | P05 | Barreras y catéteres | 4 | MULTI-ALERTA |
| IMMUNO-1 | P06 | Tipo y fase de la hemopatía | 1 | SIMPLE |
| IMMUNO-1 | P07 | Intensidad de quimioterapia | 2 | MULTI |
| IMMUNO-1 | P08 | Agentes biológicos | 4 | MULTI-ALERTA |
| IMMUNO-1 | P09 | TPH / CAR-T | 5 | MULTI-ALERTA |
| IMMUNO-1 | P10 | Corticoides sistémicos | 3 | MULTI-ALERTA |
| IMMUNO-1 | P11 | Infecciones bacterianas graves previas | 2 | MULTI-ALERTA |
| IMMUNO-1 | P12 | Infecciones fúngicas invasoras | 3 | MULTI-ALERTA |
| IMMUNO-1 | P13 | Infecciones virales crónicas / latentes | 4 | MULTI-ALERTA |
| IMMUNO-1 | P14 | Colonización por microorganismos multirresistentes | 2 | MULTI-ALERTA |
| IMMUNO-1 | P15 | Exposición sanitaria reciente | 3 | MULTI-ALERTA |
| IMMUNO-1 | P16 | Vacunación antigripal | 2 | MULTI |
| IMMUNO-1 | P17 | Vacunación antineumocócica | 1 | SIMPLE |
| IMMUNO-1 | P18 | Vacunación frente a SARS-CoV-2 | 2 | MULTI |
| IMMUNO-1 | P19 | Vacunación frente a hepatitis B | 3 | MULTI |
| IMMUNO-1 | P20 | Otras vacunas inactivadas relevantes | 2 | MULTI-ALERTA |
| IMMUNO-1 | P21 | Profilaxis frente a Pneumocystis jirovecii | 2 | MULTI |
| IMMUNO-1 | P22 | Profilaxis antiviral | 3 | MULTI |
| IMMUNO-1 | P23 | Profilaxis antifúngica | 2 | MULTI |
| IMMUNO-1 | P24 | Profilaxis antibacteriana en neutropenia de alto riesgo | 2 | MULTI |
| IMMUNO-1 | P25 | Plan de reevaluación del riesgo y estado vacunal | 3 | MULTI |
| IMMUNO-2 | P01 | Edad | 1 | SIMPLE |
| IMMUNO-2 | P02 | Comorbilidad cardiometabólica y renal | 5 | COMPUESTO-DECLARADO |
| IMMUNO-2 | P03 | Enfermedad pulmonar crónica | 4 | MULTI-ALERTA |
| IMMUNO-2 | P04 | Hepatopatía crónica | 4 | MULTI-ALERTA |
| IMMUNO-2 | P05 | Estado nutricional y fragilidad | 3 | MULTI-ALERTA |
| IMMUNO-2 | P06 | Tipo de fármaco IS principal | 1 | SIMPLE |
| IMMUNO-2 | P07 | Combinación de inmunosupresores | 1 | SIMPLE |
| IMMUNO-2 | P08 | Dosis equivalente de corticoides | 3 | MULTI-REVISAR |
| IMMUNO-2 | P09 | Duración acumulada de IS | 2 | MULTI |
| IMMUNO-2 | P10 | Linfopenia relevante | 3 | MULTI-REVISAR |
| IMMUNO-2 | P11 | Integridad de piel y mucosas | 1 | SIMPLE |
| IMMUNO-2 | P12 | Catéteres venosos centrales | 1 | SIMPLE |
| IMMUNO-2 | P13 | Prótesis y biomateriales | 2 | MULTI |
| IMMUNO-2 | P14 | Cirugía mayor reciente | 1 | SIMPLE |
| IMMUNO-2 | P15 | Esplenectomía o hipoesplenismo | 1 | SIMPLE-COLISIÓN |
| IMMUNO-2 | P16 | Hospitalización reciente | 1 | SIMPLE-COLISIÓN |
| IMMUNO-2 | P17 | Colonización por MDR | 1 | SIMPLE-COLISIÓN |
| IMMUNO-2 | P18 | Zona endémica de tuberculosis | 1 | SIMPLE |
| IMMUNO-2 | P19 | Exposición respiratoria de alto riesgo | 1 | SIMPLE |
| IMMUNO-2 | P20 | Exposición a entornos de alto riesgo fúngico | 1 | SIMPLE |
| IMMUNO-2 | P21 | Historia de infecciones graves recientes | 1 | SIMPLE-COLISIÓN |
| IMMUNO-2 | P22 | Inmunoglobulinas séricas (IgG) | 1 | SIMPLE-COLISIÓN |
| IMMUNO-2 | P23 | Intensificación reciente del régimen IS | 1 | SIMPLE |
| IMMUNO-2 | P24 | Evaluación integral de riesgo infeccioso | 1 | SIMPLE-AGREGADO-OCULTO |
| IMMUNO-2 | P25 | Parámetro puente con IMMUNO-1 | 1 | PUENTE-DERIVADO |

## 6. Ataque inicial al umbral histórico

Ambos pilotos usan `T(25)=19` y una clasificación por predominio de estados. Este cribado no valida esa regla.

Antes de reutilizarla debe probarse, como mínimo:

1. si un único parámetro clínicamente crítico puede quedar compensado por 19 estados favorables;
2. si la `U` crítica se oculta dentro de un resultado global;
3. si todos los vértices tienen peso y consecuencia comparables;
4. si el cambio de dimensión conserva el significado del umbral;
5. si `APTO` y `NO_APTO` son denominaciones clínicamente admisibles para la operación concreta.

Hasta superar esos ataques, `T(25)=19` permanece como regla histórica de los pilotos, no como regla del dominio normalizado.

## 7. Próxima unidad de trabajo permitida

Tras auditoría externa favorable de `NA0`, la siguiente tarea será elegir una única operación clínica testigo y ejecutar G1–G5 sobre sus candidatos, empezando por las colisiones y mezclas identificadas. No se clasificará todo el catálogo de una vez ni se abrirá una búsqueda de cohortes.

## 8. Límite

Este documento no declara que una posición sea clínicamente correcta o incorrecta. No modifica motores, YAML, compositor, pre-ITI ni Lenguaje SV. No autoriza asistencia.

## 9. Glosario de continuidad

| Forma | Significado |
|---|---|
| CAR-T | Linfocitos T modificados con receptor quimérico de antígeno. |
| EICH | Enfermedad de injerto contra huésped. |
| IgG | Inmunoglobulina G. |
| IS | Inmunosupresión o inmunosupresor, según el campo original del piloto. |
| MDR | Microorganismos multirresistentes. |
| PJP | Neumonía por *Pneumocystis jirovecii*. |
| TPH | Trasplante de progenitores hematopoyéticos. |
| U | Estado indeterminado legítimo. |
| YAML | Formato de datos legible usado por la configuración histórica de los pilotos. |
