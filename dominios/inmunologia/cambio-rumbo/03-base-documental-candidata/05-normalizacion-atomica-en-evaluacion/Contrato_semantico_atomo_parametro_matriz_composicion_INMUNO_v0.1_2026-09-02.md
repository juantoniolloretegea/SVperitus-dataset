# Contrato semántico de átomo, parámetro, matriz y composición — INMUNO v0.1

- **Fecha:** 02-09-2026
- **Director:** Juan Antonio Lloret Egea, Ingeniero Director
- **Rama:** `dominio-inmunologia`
- **Compuerta:** `NA0`
- **Estatuto:** `CANDIDATO_PARA_AUDITORIA_EXTERNA`
- **Base profesional:** catálogo INMUNO v0.8, SHA-256 `d9535ac933ce4eb2e35a5017c7f74f0f4b8b9e8806802b933e050ce603cfa68a`

## 1. Decisión canónica

En el dominio clínico de inmunología, **átomo y parámetro no son dos clases de objeto paralelas**.

El objeto almacenado es el **parámetro clínico**. `ATÓMICO` es el estatuto que obtiene un parámetro cuando supera las pruebas de indivisibilidad para una operación, población, horizonte temporal, regla ternaria y consecuencia declarados.

Por tanto:

```text
parámetro candidato + pruebas superadas -> parámetro atómico
parámetro candidato + prueba fallida    -> compuesto, contexto, control, puente o U
```

No se crea una segunda ontología de “átomos” debajo de los parámetros. Tampoco se adopta “molécula” como entidad canónica: puede utilizarse como analogía pedagógica para una composición, pero no como tipo registral.

## 2. Definiciones obligatorias

### 2.1. Observable

Dato bruto o hecho verificable antes de la regla de dominio. Puede proceder de historia, exploración, laboratorio, imagen, procedimiento, tratamiento o fuente documental autorizada.

Se representa como `x`. Un observable no posee por sí mismo el valor ternario del parámetro.

### 2.2. Regla o transductor de dominio

Regla explícita, versionada y trazable que transforma observables admisibles en un estado:

```text
I_p(x_1, ..., x_k; operación, población, horizonte) -> {0, 1, U}
```

La regla debe declarar qué cierra `0`, qué cierra `1` y qué obliga a preservar `U`.

### 2.3. Parámetro clínico candidato

Proposición clínica evaluable que puede influir en una operación concreta. Todavía no se presume indivisible.

### 2.4. Parámetro clínico atómico

Parámetro candidato que, en el corte declarado:

1. tiene un único sujeto semántico;
2. responde a una sola pregunta clínica gobernable;
3. produce un único estado `0/1/U` sin ocultar estados incompatibles;
4. tiene una regla explícita y reproducible;
5. admite `U` propia sin que otra proposición quede indebidamente cerrada;
6. posee consecuencia de omisión o error trazable;
7. puede variar sin arrastrar obligatoriamente otro parámetro;
8. no mezcla estado, exposición, actuación y control salvo que sean evidencia inseparable de la misma proposición;
9. mantiene identidad estable dentro de la misma versión;
10. no puede dividirse en dos proposiciones con decisión, `U`, consecuencia o ruta independientes sin perder información clínica relevante.

La multiplicidad de observables no demuestra por sí sola composición. Varios observables pueden ser evidencias alternativas o conjuntas de una única proposición. A la inversa, un único campo informático puede ocultar una valoración compuesta.

### 2.5. Parámetro compuesto

Objeto que falla al menos una prueba de atomicidad porque contiene dos o más proposiciones gobernables de forma independiente. Debe descomponerse o pasar a composición tipada; no puede conservarse como un único vértice sólo por conveniencia dimensional.

### 2.6. Contexto

Condición que delimita la interpretación o activación de parámetros, pero no es necesariamente un parámetro evaluable de la matriz activa.

### 2.7. Control

Comprobación de adecuación, documentación, seguimiento o gobierno. No debe fundirse con el estado clínico al que controla si ambos pueden divergir.

### 2.8. Puente

Referencia tipada a la salida gobernada de otra matriz o composición. No duplica sus parámetros y no se presenta como observación basal del paciente.

### 2.9. Matriz clínica

Conjunto gobernado de parámetros atómicos pertenecientes a una misma pregunta u operación y dotado de regla de estado propia. Cada parámetro canónico tiene una sola matriz propietaria. Otras matrices sólo pueden referenciarlo mediante relaciones tipadas o proyecciones declaradas.

La dimensión resulta del contenido constituido; no lo determina. `SV(9,3)`, `SV(25,5)` o `SV(36,6)` son formas posibles, no moldes que deban rellenarse.

### 2.10. Composición y ruta crítica

La composición es una operación tipada, dirigida y trazable entre matrices o sus salidas. No es suma informal ni promedio de vértices.

Una ruta crítica declara nodos obligatorios, orden, condiciones de activación, vetos no compensables, tratamiento de `U` y consecuencias de omisión, inversión o cierre ilegítimo.

### 2.11. Frame

Representación legible para el inmunólogo del estado de una matriz. Cada matriz activa posee su propio frame. Una composición puede producir un frame resumen derivado, pero éste no reemplaza los frames constitutivos ni borra sus `U`.

## 3. Prueba de corte: cuándo dejar de dividir

Un candidato deja de dividirse cuando concurren todas estas condiciones:

```text
una pregunta clínica
+ una regla ternaria
+ una U independiente
+ una consecuencia trazable
+ una función única en la ruta
+ ausencia de subdecisiones clínicamente útiles
= parámetro atómico en ese corte
```

La división adicional se rechaza si sólo produce detalles sin estado, consecuencia, `U` o función de ruta independientes. La agregación se rechaza si permite que una parte compense u oculte otra.

Esta clausura es relativa a:

- operación clínica;
- población;
- horizonte temporal;
- versión de fuentes y reglas;
- y autoridad humana declarada.

No se declara indivisibilidad metafísica ni exhaustividad permanente.

## 4. Secuencia refinada

Esta acta refina únicamente el orden interno de las fases 2–4 del acta rectora de continuidad v0.1:

1. seleccionar un objeto profesional ya cerrado;
2. formular la operación clínica en la que puede intervenir;
3. proponer una o más preguntas clínicas candidatas;
4. declarar observables y fuentes admisibles;
5. redactar la consecuencia ex ante provisional de ignorancia, error u omisión;
6. atacar la atomicidad mediante divergencia, ablación, `U` independiente y consecuencia independiente;
7. adjudicar `ATÓMICO`, `COMPUESTO`, `CONTEXTO`, `CONTROL`, `PUENTE`, `NO_PERTINENTE` o `U_REQUIERE_ADJUDICACION`;
8. constituir plenamente la consecuencia sólo para los objetos que sobrevivan;
9. asignar propiedad matricial sin duplicación;
10. constituir composiciones, rutas y frames;
11. comprobar representabilidad en el Lenguaje SV sin modificarlo;
12. someter cada cierre a adversarial externa.

La consecuencia provisional del paso 5 sirve como test de identidad. No autoriza asistencia ni queda adoptada hasta superar su compuerta específica.

## 5. No compensación y anexos operativos

Salud, seguridad y lógica clínica gobiernan la decisión. Un riesgo clínico grave no puede compensarse matemáticamente con ahorro, disponibilidad, rapidez o conveniencia administrativa.

Coste, tiempo, camas, capacidad del centro y carga de trabajo se registran porque existen y pueden condicionar la ejecución material. Se conservan en un anexo operativo de salida:

```text
decisión clínica gobernada -> implicaciones operativas
implicaciones operativas -/-> modificación automática de la decisión clínica
```

El tiempo clínico que modifica riesgo, validez, ventana diagnóstica o tratamiento pertenece a la ruta clínica. El tiempo administrativo pertenece al anexo.

## 6. Papel de la IA

La inteligencia artificial puede localizar, comprobar, comparar, ejecutar pruebas, mantener trazas y presentar frames. No puede:

- inventar un parámetro ausente;
- cerrar una `U` por plausibilidad;
- cambiar una ruta durante el episodio;
- consultar Internet libremente y convertir el resultado en decisión;
- aprender implícitamente del episodio;
- ni incorporar una guía nueva sin cuarentena, dos filtros, adjudicación humana y nuevo suceso versionado.

Durante la praxis, la IA permanece en retaguardia y responde con la clausura mínima necesaria. Sólo puede interrumpir de forma proactiva ante un veto de seguridad previamente constituido y trazable.

## 7. Relación con el Lenguaje SV

La Gramática superficial 0.2 y la Representación Intermedia 0.3 se usan como prueba de representabilidad. Desde inmunología sólo se podrá declarar:

- `YA_REPRESENTABLE`;
- `REPRESENTABLE_POR_COMPOSICION`;
- `PERTENECE_A_BIBLIOTECA_DE_DOMINIO`;
- `REQUISITO_CANDIDATO_DE_LENGUAJE`;
- `RESIDUAL_NO_REPRESENTABLE`.

Ninguna de estas etiquetas modifica el lenguaje. En particular, que la representación intermedia actual disponga de un campo de criticidades vacío no autoriza a rellenarlo sin una producción, esquema o decisión de las unidades responsables.

## 8. Freno de mano

Una operación se cierra para una versión cuando:

- todos sus parámetros activos tienen identidad y estado;
- no existe `U` crítica sin tratamiento permitido;
- las consecuencias y vetos están trazados;
- la composición es reproducible;
- el frame muestra la clausura mínima sin ocultar incertidumbre;
- la paridad de motores se satisface;
- y la auditoría externa de la compuerta es favorable.

Una novedad posterior no prolonga indefinidamente el análisis: abre una nueva versión o un suceso `REOPEN_REQUIRED`. Cualquier fallo crítico produce `ABSTENERSE` para el objeto u operación afectados.

## 9. Resultado de esta versión

Este contrato fija el vocabulario candidato y el método de corte. No adjudica todavía ningún `Pxx` de `IMMUNO-1` o `IMMUNO-2`, no constituye matrices nuevas, no valida `T(25)=19`, no declara consecuencias clínicas y no autoriza asistencia.

## 10. Glosario de continuidad

| Forma | Significado |
|---|---|
| IA | Inteligencia artificial. |
| IR | Representación intermedia del Lenguaje SV. |
| SV | Sistema Vectorial SV. |
| U | Estado indeterminado legítimo por información insuficiente, no verificable o no clausurable. |
| `NA0` | Compuerta cero de normalización atómica; fija método y superficie de ataque antes de adjudicar parámetros. |
