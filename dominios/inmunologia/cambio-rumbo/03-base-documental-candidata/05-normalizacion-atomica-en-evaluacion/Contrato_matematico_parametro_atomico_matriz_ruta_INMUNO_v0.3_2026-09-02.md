# Contrato matemático de parámetro atómico, matriz y ruta — INMUNO v0.3

- **Fecha:** 02-09-2026
- **Rama:** `dominio-inmunologia`
- **Compuerta:** `NA0-MATH`
- **Estatuto:** `RECTOR_DE_NORMALIZACION_MATEMATICA`
- **Base profesional:** catálogo INMUNO v0.8, SHA-256 `d9535ac933ce4eb2e35a5017c7f74f0f4b8b9e8806802b933e050ce603cfa68a`
- **Antecedente:** contrato semántico INMUNO v0.2
- **Ámbito:** identidad, atomicidad, propiedad matricial, composición, ruta, frame y regla de cierre

## 1. Decisión de diseño

En este dominio, **átomo y parámetro no son objetos distintos**. El objeto canónico es el `PARAMETRO_ATOMICO`.

Una pregunta, un campo de formulario, una prueba, una observación o una posición histórica `Pxx` no son parámetros atómicos por el mero hecho de existir. Son material candidato o evidencia. Sólo entra en la tabla autorizada aquello que supera las pruebas de identidad, separabilidad, trazabilidad y consecuencia de este contrato.

La identidad atómica es estable. La operación clínica no redefine qué es el parámetro: sólo determina si ese parámetro está activo, inactivo o pendiente de adjudicación para el episodio y horizonte declarados.

```text
identidad del parámetro    = estable dentro de la versión autorizada
activación del parámetro   = dependiente de operación, episodio y horizonte
valor del parámetro        = 0, 1 o U conforme a un transductor versionado
```

## 2. Objetos y niveles

| Nivel | Objeto | Función | No debe confundirse con |
|---|---|---|---|
| E0 | `OBSERVABLE` | dato o hecho verificable que alimenta una regla | parámetro |
| E1 | `PREGUNTA_CANDIDATA` | proposición aún no adjudicada | átomo autorizado |
| E2 | `PARAMETRO_ATOMICO` | proposición clínica indivisible y gobernable | prueba, campo o puntuación |
| E3 | `MATRIZ` | conjunto propietario de parámetros con una finalidad clínica común | saco de variables |
| E4 | `COMPOSICION` | relación tipada entre matrices o salidas | suma o promedio informal |
| E5 | `RUTA_CRITICA` | subgrafo obligatorio con condiciones, vetos y tratamiento de `U` | recomendación generativa |
| E6 | `FRAME` | proyección fiel y legible de una matriz | fuente de verdad independiente |

## 3. Universo autorizado y versionado

Para una versión `v`, la tabla autorizada de parámetros es el conjunto finito:

```text
A_v = {p_1, p_2, ..., p_n}
```

En la analogía de la tabla periódica, `Parametro_ID` cumple la función del número atómico: identifica de forma unívoca, pero no es una magnitud clínica ni una puntuación. La tabla se ordena por `Familia`, `Subfamilia` e identidad; esa clasificación facilita búsqueda y composición, pero no determina valor, criticidad, matriz ni ruta.

Cada `p ∈ A_v` se representa por la tupla:

```text
p = <
  Parametro_ID,
  Version_parametro,
  Proposicion_canonica,
  Sujeto_semantico,
  Predicado_clinico,
  Familia,
  Subfamilia,
  Dominio_de_observables,
  Transductor_versionado,
  Estado_admisible,
  Fuentes_aplicadas,
  Vinculos_de_procedencia
>
```

`Estado_admisible = {0, 1, U}`. La `U` es un estado legítimo de información insuficiente, conflictiva, no vigente o no clausurable; no es un valor intermedio ni una autorización para completar por plausibilidad.

El `Parametro_ID` no cambia por activarse en otra operación o matriz. Si cambia materialmente la proposición, el sujeto, el predicado o la regla de identidad, se crea una nueva identidad o una nueva versión explícita; no se recicla el identificador para esconder el cambio.

La función y la consecuencia no se convierten en propiedades universales únicas del parámetro. Se registran en cada uso autorizado:

```text
u(p,O) = <
  Parametro_ID,
  Operacion_ID,
  Regla_de_activacion,
  Matriz_propietaria_o_referencia,
  Funcion_en_ruta,
  Consecuencias_de_error_u_omision,
  Criticidad_y_vetos,
  Horizonte,
  Fuentes_aplicadas,
  Version,
  Autoridad
>
```

El mismo parámetro puede participar en varias operaciones con funciones o consecuencias distintas sin adquirir otra identidad. Cada uso debe quedar separado, versionado y trazable.

## 4. Observable, transductor y parámetro

Sea `X_p` el dominio de observables admisibles de `p`. El transductor autorizado es:

```text
I_p^v : X_p × Contexto_permitido -> {0, 1, U}
```

Un parámetro puede requerir uno o varios observables. Esto no lo hace compuesto si todos alimentan una sola proposición y no originan decisiones, incertidumbres o consecuencias independientes.

Un observable tampoco se convierte en parámetro sólo porque sea medible. La pregunta es clínica: si retirar ese dato destruye una evidencia pero no una decisión gobernable independiente, el dato permanece como observable.

## 5. Activación sin redefinición

Para una operación `O`, un episodio `e` y un horizonte `h`, se define:

```text
alpha_v(p, O, e, h) -> {ACTIVO, INACTIVO, U_ACTIVACION}
```

La función `alpha_v`, constituida dentro del registro de uso autorizado, selecciona el subconjunto pertinente:

```text
A_v(O,e,h) = {p ∈ A_v | alpha_v(p,O,e,h) = ACTIVO}
```

Esta selección no altera la identidad, la consecuencia ni el transductor de `p`. Si la operación exige una proposición diferente, no se proyecta artificialmente el parámetro existente: se propone otro candidato y se somete a la misma compuerta.

## 6. Prueba de atomicidad

Un candidato `q` sólo recibe `PARAMETRO_ATOMICO` cuando concurren todas las condiciones siguientes:

1. **Identidad:** una proposición canónica, un sujeto semántico y un predicado clínico.
2. **Estado único:** un solo estado `0/1/U` no oculta estados incompatibles.
3. **U propia:** la falta o conflicto de información puede preservarse sin cerrar otra proposición.
4. **Consecuencia separable:** dentro de un uso, el error u omisión no oculta consecuencias correspondientes a subproposiciones independientes.
5. **Función separable:** dentro de un uso, el objeto no reúne funciones de ruta que puedan variar de forma independiente.
6. **Variación independiente:** puede cambiar sin obligar lógicamente al cambio de otro parámetro.
7. **Ablación:** retirarlo de una composición puede alterar una decisión o clausura identificable.
8. **No partición material:** no existe una división útil en dos proposiciones gobernables por separado.
9. **Reproducibilidad:** la misma entrada canónica, fuentes y versiones produce el mismo estado y la misma traza.
10. **Procedencia:** fuente, versión, localizador y evidencia están vinculados antes de la conclusión.

Formalmente, `q` es compuesto si existe una partición no trivial `q -> (a,b)` tal que:

```text
independencia_estado(a,b)
OR independencia_U(a,b)
OR independencia_consecuencia(a,b)
OR independencia_funcion_ruta(a,b)
```

y la separación conserva información clínicamente útil. En ese caso, `q` no puede mantenerse unido por conveniencia dimensional, visual o informática.

La división se detiene cuando ninguna partición adicional produce estado, `U`, consecuencia o función de ruta independientes. No se desciende hasta componentes físicos o terminológicos que carezcan de significado clínico gobernable.

Varias consecuencias derivadas de la misma proposición no obligan a dividir el parámetro si no corresponden a subestados independientes. Del mismo modo, que un parámetro cumpla funciones distintas en dos operaciones no lo vuelve compuesto: exige dos registros `u(p,O)`, no dos átomos.

## 7. Estatutos exhaustivos del candidato

Antes de ejecutar la adjudicación, un objeto conserva el estado de ciclo `CANDIDATO_NO_ADJUDICADO`. Este rótulo no es un resultado de la prueba, no equivale a `U_REQUIERE_ADJUDICACION` y no permite la entrada en `A_v`. Al terminar la prueba se sustituye por exactamente uno de los siete estatutos siguientes.

Todo candidato examinado debe recibir exactamente uno de estos estatutos:

| Estatuto | Resultado |
|---|---|
| `PARAMETRO_ATOMICO` | entra en `A_v` |
| `COMPUESTO_A_DESDOBLAR` | genera candidatos hijos y no entra como átomo |
| `CONTEXTO` | condiciona activación o interpretación |
| `CONTROL` | verifica adecuación, documentación o gobierno |
| `PUENTE` | referencia una salida ya gobernada sin duplicarla |
| `NO_PERTINENTE` | queda fuera de la operación declarada |
| `U_REQUIERE_ADJUDICACION` | no puede clasificarse todavía |

Ningún candidato puede recibir dos estatutos finales. Una clasificación `U_REQUIERE_ADJUDICACION` mantiene abierta únicamente esa identidad; no impide cerrar las restantes.

## 8. Matrices: propiedad única y referencia

Sea `M_v = {M_1, ..., M_k}` el conjunto de matrices de la versión. Existe una función de propiedad:

```text
owner_v : A_v -> M_v
```

con exactamente un propietario por parámetro. Por tanto, para los conjuntos de parámetros propios `P_i` y `P_j`:

```text
i != j  =>  P_i ∩ P_j = vacío
```

Una matriz puede utilizar un parámetro propiedad de otra mediante una referencia tipada:

```text
REF <Parametro_ID, Matriz_origen, Version, Funcion_en_destino>
```

La referencia no duplica el parámetro, no recalcula su estado y no elimina su `U`. La dimensión de una matriz es consecuencia de los parámetros adjudicados; nunca se rellena una matriz para alcanzar de antemano `(9,3)`, `(25,5)`, `(36,6)` u otra forma histórica.

El estado primario de una matriz es el vector ordenado de sus parámetros:

```text
S(M_i) = (s_1, ..., s_m),  s_j ∈ {0,1,U}
```

Cualquier salida resumida requiere una función explícita `g_i`, versionada y atacada. No se admite mayoría, promedio o umbral por predominio como sustitución automática del vector.

## 9. Composición y ruta crítica

La arquitectura de una operación se representa como un hipergrafo dirigido y tipado:

```text
H_O = (V, E)
V = matrices, parámetros referenciados, controles y salidas
E = transiciones tipadas con condición, orden, autoridad y consecuencia
```

Una composición declara como mínimo:

```text
<Composicion_ID, Entradas, Regla, Orden, Condiciones,
 Tratamiento_U, Vetos, Salida, Fuentes, Version>
```

La ruta crítica `R_c(O)` es el subgrafo de elementos obligatorios para que la operación pueda emitir una salida admisible. Un veto o una `U` crítica no puede compensarse con otros estados favorables:

```text
VETO_CRITICO = 1  =>  NO_EJECUTAR_SALIDA_AFECTADA
U_CRITICA = 1 y sin tratamiento autorizado  =>  ABSTENERSE_O_ESCALAR
```

Los costes, tiempos administrativos, capacidad y disponibilidad pueden acompañar la salida como restricciones de ejecución. No modifican el estado clínico ni compensan vetos. El tiempo que cambia riesgo, vigencia o ventana clínica pertenece a la ruta clínica.

## 10. Frames y proyección

Cada matriz activa tiene un frame propio:

```text
F_i = projection(M_i, S(M_i), U_i, vetos_i, version_i)
```

Puede existir un frame resumen de la composición, pero debe ser una proyección derivada, reproducible y reversible hasta los frames constitutivos. El resumen no elimina parámetros, `U`, vetos, fuentes ni versiones.

La interfaz debe mostrar primero la clausura mínima necesaria: vetos, `U` críticas, ruta activa y consecuencia. El inventario completo permanece disponible en retaguardia y no se impone como carga rutinaria.

## 11. Regla finita de trabajo y freno de mano

Sea `Q_0` el conjunto finito de preguntas candidatas del corte. Para este corte:

```text
|Q_0| = 32
familias(Q_0) = (RUT=1, CTX=5, EXP=5, HUE=5, BAR=4, HIS=5, MOD=7)
```

Las 32 preguntas son candidatas semánticas, no parámetros autorizados. Las 50 posiciones de `IMMUNO-1` y `IMMUNO-2` son señales históricas de cobertura, colisión y composición; tampoco son parámetros autorizados.

La cola de adjudicación se define así:

```text
Q_(t+1) = pendientes(Q_t) + hijos_de_compuestos(Q_t)
```

La versión puede cerrarse cuando:

1. todo elemento de la cola ha recibido un único estatuto;
2. todo `COMPUESTO_A_DESDOBLAR` tiene hijos identificados o una `U` explícita;
3. ningún candidato conserva una partición material no examinada;
4. todo átomo propuesto posee identidad, transductor y procedencia, y cada uso propuesto posee activación, consecuencia y función;
5. la propiedad matricial es total y única para los átomos adoptados;
6. toda referencia cruzada es tipada y no duplica estado;
7. toda ruta crítica trata vetos y `U` sin compensación;
8. la reproducción determinista y la adversarial pasan;
9. y el residuo queda enumerado, no oculto bajo una declaración de exhaustividad.

Una novedad posterior no prolonga indefinidamente el corte. Abre una nueva versión y sólo altera los objetos afectados mediante un suceso trazable.

## 12. Estado computado del corte actual

| Magnitud | Valor | Interpretación |
|---|---:|---|
| Preguntas candidatas G2-S1 | 23 | cerradas semánticamente; no atómicas |
| Preguntas candidatas G2-S2 | 9 | cerradas semánticamente tras auditoría externa; no atómicas |
| Total `Q_0` | 32 | universo precursor actual |
| Posiciones piloto leídas | 50 | antecedentes estructurales, no autoridad |
| Familias de colisión piloto | 8 | ataques obligados, no parámetros |
| Parámetros atómicos autorizados | 0 | `G5-ATM` no abierta |
| Matrices normalizadas | 0 | no constituidas |
| Rutas críticas normalizadas | 0 | no constituidas |

## 13. Secuencia de ejecución

1. cerrar el modelo matemático y su registro precursor;
2. cerrar conjuntamente la integridad de `Q_0` sin convertirlo en tabla autorizada;
3. constituir observables y transductores candidatos sólo para una familia acotada;
4. redactar consecuencias provisionales diferenciables;
5. ejecutar divergencia, ablación, `U` y partición;
6. adjudicar atomicidad;
7. asignar matrices propietarias;
8. componer rutas y frames;
9. comprobar representabilidad en el Lenguaje SV sin modificarlo;
10. someter el cierre a adversarial externa.

No se abre una búsqueda mundial ni una recopilación de cohortes en esta secuencia. Las fuentes nuevas sólo entran cuando una identidad concreta exige evidencia o cuando un suceso prospectivo reabre una regla.

## 14. Papel de la inteligencia artificial

La inteligencia artificial opera como ejecutor determinista subordinado a rutas, fuentes y autorizaciones constituidas. No inventa parámetros, no cierra `U`, no compensa vetos y no sustituye la decisión profesional.

Toda salida debe enlazar, antes de la conclusión:

```text
entrada -> parámetro -> regla -> fuente -> transición -> estado/U
        -> consecuencia -> versión -> autoridad -> salida/frame
```

Una cita añadida después del consejo no constituye trazabilidad. La reejecución independiente del mismo experimento canónico debe producir deliberación capturable, traza, estados, transiciones, salida, frames y serialización idénticos byte a byte. Cualquier diferencia produce `REPRODUCIBILIDAD_NO_PASA`; un fallo técnico produce `EJECUCION_TECNICA_NO_VALIDA`, nunca una salida clínica alternativa.

## 15. Límites

Este contrato no adjudica ninguna de las 32 preguntas, no constituye observables, consecuencias clínicas, parámetros, matrices, rutas o frames, no modifica el Lenguaje SV y no autoriza asistencia. No contiene datos de episodios, centros o personas.

## 16. Glosario de continuidad

| Forma | Significado |
|---|---|
| `NA0-MATH` | compuerta matemática previa a la adjudicación atómica |
| `G2-SEM` | formulación semántica de preguntas candidatas |
| `G3-OBS` | constitución posterior de observables y transductores |
| `G5-ATM` | adjudicación posterior de atomicidad |
| IA | inteligencia artificial |
| SV | Sistema Vectorial SV |
| U | estado indeterminado legítimo |
