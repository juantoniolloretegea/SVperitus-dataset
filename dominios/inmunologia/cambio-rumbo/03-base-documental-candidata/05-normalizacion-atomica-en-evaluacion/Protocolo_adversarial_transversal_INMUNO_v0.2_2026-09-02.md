# Protocolo adversarial transversal para la constitución del dominio INMUNO v0.2

- **Fecha:** 02-09-2026
- **Compuerta inicial:** `NA0`
- **Estatuto:** `RECTOR_DE_COMPUERTA_NA0`
- **Aplicación:** toda transformación desde corpus profesional hasta requisito semántico para el Lenguaje SV

## 1. Regla general

Ninguna salida se convierte en entrada constitutiva de la fase siguiente porque la haya producido la misma unidad que la diseñó. Toda transición conserva:

- ataque interno reproducible;
- evidencia y localizador;
- resultado por registro;
- incertidumbres explícitas;
- regresión contra el corte anterior;
- y auditoría externa en la compuerta de cierre.

Estados comunes:

| Estado | Efecto |
|---|---|
| `PASA` | Puede avanzar a la siguiente compuerta. |
| `PASA_CON_REPAROS` | Sólo avanza tras reparación y regresión verificadas. |
| `U_NO_CERRAR` | Conserva el objeto, pero prohíbe su cierre o uso crítico. |
| `RECHAZADO` | No entra en el corpus de la fase. |
| `REOPEN_REQUIRED` | Novedad posterior; exige nuevo episodio o versión. |
| `ABSTENERSE` | Fallo crítico; se detiene la operación afectada. |

No existe suma de reparos que compense un fallo clínico crítico.

## 2. Compuertas y ataques obligatorios

| Puerta | Objeto | Ataques mínimos | Salida exigida |
|---|---|---|---|
| `G0-PRO` | Corpus profesional | identidad, fuente primaria, localizador, versión, jurisdicción, frontera, duplicación y regresión | objeto profesional cerrado o rechazado |
| `G1-OP` | Operación clínica | paciente real, problema, población, horizonte, autoridad, inicio y final operacional | operación tipada y finita |
| `G2-SEM` | Pregunta candidata | ambigüedad, polisemia, mezcla de estado/exposición/acción/control, sinónimos y colisiones | formulación canónica candidata |
| `G3-OBS` | Observables y regla | disponibilidad, unidad, temporalidad, procedencia, discordancia, dato ausente y falsa precisión | transductor candidato y `U` legítima |
| `G4-CON` | Consecuencia ex ante | mecanismo causal, gravedad, alcance, fuente, exageración, circularidad y compensación económica | consecuencia candidata o `U` |
| `G5-ATM` | Atomicidad | divergencia interna, ablación, `U` independiente, consecuencia independiente, ruta independiente y campo compuesto | estatuto semántico por candidato; si G4 conserva la consecuencia en `U`, A4 se aplaza y la salida obligatoria es `U_REQUIERE_ADJUDICACION`, nunca `ATÓMICO` |
| `G6-MAT` | Matriz | propiedad única, duplicación, tamaño artificial, cobertura, dependencia escondida y parámetro huérfano | matriz candidata y referencias tipadas |
| `G7-COM` | Composición/ruta | dirección, orden, asociatividad asumida, ciclo, veto, cierre prematuro, propagación de `U` y fallo de puente | composición gobernada o abstención |
| `G8-FRA` | Frame | correspondencia uno-a-uno, ocultación de `U`, carga cognitiva, resumen engañoso, exceso de información y soberanía humana | frame mínimo verificable |
| `G9-LSV` | Representabilidad | gramática 0.2, representación intermedia 0.3, canonicalización, pérdida semántica, paridad de motores y expansión indebida | clasificación de compatibilidad, sin escritura |
| `G10-IA` | IA y actualización | alucinación, fuente sin versión, Internet directo, contaminación del episodio, aprendizaje implícito y mutación sin autoridad | propuesta en cuarentena o rechazo |
| `G11-EMP` | Contraste empírico | cohorte pertinente, enlace sujeto, sesgo, observable real, temporalidad, validez externa, contradicción y no-decisión | `APOYA`, `MODULA`, `CONTRADICE` o estado residual |
| `G12-REL` | Cierre de versión | identidad, cobertura, regresión total, pruebas negativas, trazas colgantes, acrónimos y límites | liberación candidata y orden externa |

## 3. Ataques determinantes de atomicidad

Cada candidato debe superar los seis ataques siguientes.

### A1. Divergencia

Construir un caso válido donde dos componentes internos tomen estados distintos. Si el parámetro exige ocultar esa divergencia bajo un único valor, es compuesto.

### A2. U independiente

Ocultar sólo una parte de la información. Si una subproposición queda `U` mientras otra puede cerrarse, deben separarse o representarse mediante composición explícita.

### A3. Ablación

Retirar un observable cada vez. Si al retirarlo cambia una decisión distinta de la pregunta nominal, el candidato mezcla funciones.

### A4. Consecuencia independiente

Preguntar si ignorar cada parte puede causar consecuencias distintas o exigir actuaciones diferentes. Una respuesta afirmativa impide la atomicidad conjunta salvo evidencia de inseparabilidad.

### A5. Ruta independiente

Preguntar si una parte puede activar, vetar o detener una ruta sin la otra. Si puede, ambas no deben ocupar un único vértice.

### A6. Sustitución semántica

Reemplazar el nombre por su definición completa. Si aparecen conjunciones, alternativas heterogéneas, ventanas o actuaciones no visibles en el nombre, el objeto requiere despiece o justificación explícita.

## 4. Ataques a matrices y composiciones

### 4.1. Propiedad y no duplicación

Un parámetro tiene una sola identidad y una sola matriz propietaria. La repetición con distinto identificador es fallo. Una referencia tipada no lo es.

### 4.2. Prueba de tamaño

Eliminar la restricción `n=b²` y volver a agrupar por significado. Si cambia el contenido para recuperar un cuadrado, la matriz estaba dimensionada por conveniencia y no por clínica.

### 4.3. Prueba de orden

Permutar matrices y puentes. Si el resultado cambia, la composición debe declararse no conmutativa y fijar el orden. Si el orden no está documentado, no pasa.

### 4.4. Prueba de veto

Inyectar un fallo clínico crítico junto con numerosos estados favorables. Si el resultado global lo compensa, la composición es inadmisible.

### 4.5. Prueba de U

Inyectar `U` en un nodo crítico. Debe conservarse o conducir a la abstención/escalado previsto; nunca a cierre favorable por mayoría.

## 5. Ataques al frame y a la IA

El frame debe permitir al inmunólogo identificar en dos niveles —resumen y detalle bajo demanda—:

- estado global;
- parámetros o matrices que impiden cierre;
- `U` críticas;
- vetos;
- versión y horizonte;
- y rastro que justifica cada estado.

Se rechaza el frame si abruma con todo el catálogo, oculta la incertidumbre, presenta una media como seguridad o permite que el consejo de IA parezca orden soberana.

La IA se prueba con entradas adversas: fuente falsa, guía posterior al corte, texto clínico ambiguo, conflicto entre fuentes, dato ausente, intento de cerrar `U`, intento de alterar una regla durante el episodio y petición de recomendación fuera de autoridad. La salida correcta debe ser rechazo, cuarentena, solicitud de confirmación o abstención según el caso.

## 6. Ataque a factores operativos

Se ejecutarán casos en los que coste, tiempo administrativo, disponibilidad de camas o facilidad logística favorezcan la opción contraria a la ruta clínica.

El sistema debe:

1. conservar la decisión clínica sin compensarla;
2. registrar la dificultad en el anexo operativo;
3. informar al humano de la imposibilidad material;
4. escalar por la vía autorizada;
5. abstenerse si no existe ejecución clínica segura.

## 7. Evidencia y auditoría externa

Cada compuerta producirá:

1. manifiesto de objetos y hashes;
2. tabla de entradas y salidas por identificador;
3. batería positiva y negativa;
4. lista de `U` con causa;
5. diferencias contra la versión anterior;
6. reparaciones literales;
7. dictamen interno;
8. orden de auditoría externa que prohíba repetir asuntos ya cerrados y exija atacar los nuevos.

La unidad externa no podrá limitarse a recuentos. Deberá intentar falsar las decisiones materiales con contraejemplos reproducibles.

## 8. Paradas obligatorias

- Fallo de identidad o trazabilidad: `ABSTENERSE`.
- `U` crítica sin tratamiento: `ABSTENERSE_O_ESCALAR` según regla autorizada.
- Parámetro compuesto presentado como atómico: `U_NO_CERRAR` para la matriz afectada.
- Duplicación material entre matrices: `U_NO_CERRAR`.
- Veto compensado por agregación: `ABSTENERSE`.
- Pérdida de semántica al proyectar al lenguaje: `RESIDUAL_NO_REPRESENTABLE` y no modificación desde este frente.
- Novedad después del sellado predecisional: `REOPEN_REQUIRED`; nunca reescritura silenciosa.

## 9. Reparación de la auditoría externa

Esta versión incorpora `R-02` de la auditoría externa de NA0 v0.1: una consecuencia que permanezca en `U` después de G4 impide superar A4 y prohíbe declarar atomicidad. Los reparos `R-01` y `R-03` se reparan en el contrato semántico v0.2.

## 10. Aplicación inicial

La primera ejecución de este protocolo es el cribado estructural de `IMMUNO-1` y `IMMUNO-2`. Ese cribado identifica superficies de ataque; no adjudica atomicidad clínica ni valida los motores históricos.

## 11. Meta-adversarial del propio protocolo

El protocolo no queda exento de sus reglas. Su auditor externo deberá intentar demostrar:

1. que una puerta carece de objeto, criterio de salida o parada;
2. que un mismo fallo puede recibir dos estados incompatibles;
3. que el diseñador puede declararse `PASA` sin evidencia por registro;
4. que una reparación puede alterar silenciosamente una fase ya cerrada;
5. que una auditoría externa puede quedar sustituida por el recuento interno;
6. que un acrónimo, término o referencia impide reproducir el ataque;
7. que la batería permite compensar un veto clínico;
8. que el propio protocolo invade el Lenguaje SV.

Si alguno de estos contraejemplos prospera, `NA0` no pasa hasta que exista nueva versión reparada y regresión completa.

## 12. Glosario de continuidad

| Forma | Significado |
|---|---|
| IA | Inteligencia artificial. |
| SV | Sistema Vectorial SV. |
| U | Estado indeterminado legítimo; no equivale a cero, ausencia ni valor medio. |
| `NA0` | Compuerta cero de normalización atómica. |
| PJP | Neumonía por *Pneumocystis jirovecii*. |
