# Adjudicación atómica G5-ATM — SEM-EXP-004 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Puerta:** `G5-ATM/SEM-EXP-004`
- **Operación:** `OP-IMM-001`
- **Raíz:** `SEM-EXP-004`
- **Base exacta:** `8d143e6682211a875392e1135de9c769e7b33e96`
- **Contrato:** `NA0-MATH` v0.3
- **Manifiesto de terminación:** `OP-IMM-001 / Q0 v0`, 03-09-2026
- **Estatuto:** `ADJUDICACION_ATOMICA_CERRADA_MIXTA_CON_PUENTE_Y_U_TIPADA`
- **Efecto clínico:** ninguno
- **Autorización asistencial:** ninguna

## 0. Objeto y dictamen nuclear

Se adjudica:

> `SEM-EXP-004`: ¿Está identificada cualquier otra exposición inmunomoduladora concurrente o previa que siga siendo clínicamente activa para este episodio?

La raíz une dos predicados no equivalentes:

1. existe y está representada una exposición adicional distinta del tratamiento primario;
2. dicha exposición conserva un efecto clínicamente pertinente para una finalidad y horizonte.

El primero produce un puente constitutivo positivo y utilizable. El segundo no puede cerrarse como parámetro universal: necesita identificar exposición, efecto y regla específica. La raíz queda particionada una sola vez y termina sin agregar exposiciones ni fabricar un estado global de inmunosupresión.

La adversarial está integrada. No se crea orden, recepción ni documentación auxiliar.

## 1. Dependencias cerradas

La prueba recibe:

- `G3-OBS/SEM-EXP-004`: dos entidades, dieciocho observables, cinco normalizadores y dieciséis causas de `U`;
- `G4-CON/SEM-EXP-004`: siete consecuencias separadas sobre identidad, cobertura, hecho, duplicación, tiempo, magnitud y finalidad;
- `BRG-TXP-PRIMARY-001`, para establecer respecto de qué propuesta una exposición es adicional;
- `NA0-MATH` v0.3;
- y `Q0 v0`.

La regla candidata `I_IMMEXP_ACTIVE_v` continúa no constituida. Ni las fuentes de transporte ni las consecuencias generales aportan un transductor clínico.

## 2. Clasificación de los objetos de G3

| Objeto | Tipo adjudicado | Motivo |
|---|---|---|
| `E_IMM_EXP` | `ENTIDAD_OBSERVACIONAL` | identifica una exposición sin emitir estado clínico |
| `F_IMM_EXP` | `HECHO_OBSERVACIONAL` | conserva propuesta, orden, declaración, administración o suspensión |
| `N_IMMEXP_ID` | `NORMALIZADOR_IDENTITARIO` | mantiene componentes y correspondencias |
| `N_IMMEXP_EVENTOS` | `NORMALIZADOR_DE_SECUENCIA` | ordena hechos sin fusionar su naturaleza |
| `N_IMMEXP_COBERTURA` | `CONTROL_DE_COBERTURA` | impide inferir ausencia desde silencio |
| `N_IMMEXP_ULTIMO` | `NORMALIZADOR_TEMPORAL` | obtiene el último hecho demostrado, no el fin del efecto |
| `N_IMMEXP_VIGENCIA_INPUT` | `PREPARADOR_DE_DOMINIO` | reúne insumos para una regla futura |
| `I_IMMEXP_ACTIVE_v` | `TRANSDUCTOR_CLINICO_NO_CONSTITUIDO` | requiere agente, efecto, finalidad, horizonte y autoridad |

Ningún observable, normalizador o control entra por traslación en `A0`.

## 3. Ataque de atomicidad de la raíz

### 3.1. Estado único

Puede existir una exposición adicional bien documentada y ser desconocida su actividad; puede estar demostrada una administración y faltar magnitud; o puede existir una regla para una finalidad que no sea aplicable a otra.

**Resultado:** la raíz no admite un estado único `0/1/U` sin pérdida.

### 3.2. U propia

Identidad, cobertura, naturaleza del hecho, deduplicación, tiempo, magnitud y finalidad poseen causas de `U` independientes. La actividad de dos exposiciones distintas también puede divergir.

**Resultado:** un único estado agregado ocultaría qué exposición y dependencia deben repararse.

### 3.3. Consecuencia separable

Las siete consecuencias de G4 muestran que omitir una exposición, duplicar un hecho, alterar su magnitud o transportar una ventana entre finalidades contaminan operaciones diferentes.

**Resultado:** la separación material es obligatoria.

### 3.4. Función

La historia representada sirve de puente factual. La actividad clínica, en cambio, sería una propiedad de un efecto específico de una exposición para un horizonte; no una propiedad universal del registro.

**Resultado:** existen dos hijos funcionalmente distintos.

## 4. Partición finita

```text
SEM-EXP-004
  ├─ CAND-IMMEXP-HISTORY-001
  └─ CAND-IMMEXP-ACTIVE-001
```

| Candidato | Pregunta terminal |
|---|---|
| `CAND-IMMEXP-HISTORY-001` | ¿Está constituido, respecto del tratamiento primario, el conjunto individualizado y deduplicado de exposiciones adicionales y sus hechos, con cobertura y residuo explícitos? |
| `CAND-IMMEXP-ACTIVE-001` | Para una exposición y un efecto explícitamente identificados, ¿ese efecto continúa clínicamente vigente bajo una regla versionada y aplicable al horizonte? |

La partición utiliza las distinciones de G2–G4 y reduce estrictamente `rho`. No crea una raíz por fármaco, efecto, fuente o finalidad.

## 5. CAND-IMMEXP-HISTORY-001

### 5.1. Naturaleza

El candidato no pregunta por riesgo ni por efecto biológico. Constituye la referencia factual de exposiciones adicionales que otras proposiciones podrán consumir.

**Tipo:** `PUENTE_CONSTITUTIVO_COMPUESTO`.

Identificador adoptado:

```text
BRG-IMMEXP-HISTORY-001
```

### 5.2. Salida canónica

```text
BRG-IMMEXP-HISTORY-001(
  BRG-TXP-PRIMARY-001,
  {E_IMM_EXP},
  {F_IMM_EXP},
  corte,
  version
) ->
  HISTORIA_ADICIONAL_CONSTITUIDA
  | HISTORIA_ADICIONAL_PARCIAL_CON_RESIDUO
  | SIN_EXPOSICION_ADICIONAL_EN_COBERTURA_COMPLETA
  | U_HISTORIA_ADICIONAL
  | EJECUCION_TECNICA_NO_VALIDA
```

### 5.3. Condiciones

`HISTORIA_ADICIONAL_CONSTITUIDA` exige:

1. tratamiento primario de referencia constituido;
2. cobertura de historia declarada completa para el corte;
3. identidades farmacológicas y hechos suficientemente determinados;
4. propuesta, orden, declaración y administración separadas;
5. deduplicación por enlaces de procedencia, no por similitud nominal;
6. tiempo, magnitud y precisión originales conservados;
7. conflictos y fuentes visibles;
8. procedencia anterior a la salida.

`HISTORIA_ADICIONAL_PARCIAL_CON_RESIDUO` conserva exposiciones demostradas, fuentes no cubiertas y límites de uso. No permite concluir ausencia de otras exposiciones.

`SIN_EXPOSICION_ADICIONAL_EN_COBERTURA_COMPLETA` sólo existe cuando la cobertura está declarada completa y no aparece ninguna exposición diferente del tratamiento primario. No equivale a ausencia de cualquier antecedente médico ni a riesgo nulo.

`U_HISTORIA_ADICIONAL` identifica el campo, exposición o fuente que impide utilizar limpiamente la historia.

### 5.4. Por qué no es parámetro

La salida es un conjunto estructurado, posiblemente vacío o parcial, no una proposición clínica atómica. Sus elementos conservan identidades, hechos y `U` independientes. El puente queda fuera de `A0`.

## 6. CAND-IMMEXP-ACTIVE-001

### 6.1. Proposición candidata restringida

> Un efecto inmunológico explícitamente identificado de una exposición farmacológica adicional concreta permanece clínicamente vigente para el horizonte conforme a una regla versionada y aplicable.

La identidad potencial de un futuro parámetro no puede ser «exposición activa» sin declarar qué efecto se evalúa. Un mismo agente puede conservar un efecto relevante para una finalidad y no otro, y distintas finalidades pueden emplear ventanas diferentes.

### 6.2. Dominio mínimo requerido

```text
X_IMMEXP_ACTIVE = <
  Exposicion_ID,
  Identidad_farmacologica,
  Efecto_inmunologico_ID,
  Hechos_admisibles,
  Magnitud_y_patron,
  Inicio_y_fin_documentales,
  Ultimo_hecho_demostrado,
  Finalidad_o_uso,
  Horizonte,
  Regla_de_persistencia,
  Jurisdiccion,
  Autoridad,
  Procedencia,
  Version
>
```

### 6.3. Elementos no constituidos

Faltan en esta versión, de manera conjunta:

1. inventario finito de efectos inmunológicos necesarios para `OP-IMM-001`;
2. correspondencia versionada entre cada exposición y cada efecto;
3. hecho mínimo admisible para afirmar exposición real;
4. reglas de magnitud y patrón cuando sean necesarias;
5. ventana de persistencia por efecto;
6. tratamiento de suspensiones, exposiciones intermitentes y conflictos;
7. relación entre finalidad y regla sin transporte indebido;
8. transductor ejecutable;
9. fuentes clínicas específicas;
10. autoridad de adopción.

### 6.4. Adjudicación

```text
CAND-IMMEXP-ACTIVE-001 = U_ATOMICIDAD_NO_CONSTITUIDA
```

No se adopta una plantilla vacía como familia infinita de parámetros. La `U` es terminal para esta versión y sólo podrá revisarse mediante un objeto material que identifique efecto, regla y fuente sin ampliar silenciosamente `Q0 v0`.

La `U` no significa inactividad, actividad, riesgo alto, interacción, contraindicación ni obligación de abstenerse.

## 7. Relación con A0 y con las raíces ya adjudicadas

```text
A0 = {PAR-GC-PLAN-SYS-001}
```

`BRG-IMMEXP-HISTORY-001` no absorbe `PAR-GC-PLAN-SYS-001`. El parámetro de glucocorticoide propuesto conserva su identidad y puede ser una referencia útil para excluir del conjunto «adicional» aquello que ya forma parte del tratamiento primario.

Una exposición previa real a glucocorticoides con posible efecto vigente permanece bajo la `U` específica ya declarada como `CAND-GC-EFECTO-VIGENTE-001`; no se duplica dentro de `A0` ni se da por resuelta mediante el puente general.

`BRG-TXP-PRIMARY-001` y `BRG-IMMEXP-HISTORY-001` forman referencias constitutivas complementarias: propuesta primaria e historia adicional. Ninguna es matriz ni parámetro clínico.

## 8. Adversarial integrada

### A. Una posición por medicamento

**Ataque:** crear un parámetro para cada exposición encontrada.

**Resultado:** rechazado. La mera existencia del registro no define un predicado clínico atómico.

### B. Parámetro agregado de inmunosupresión total

**Ataque:** combinar todas las exposiciones en `0/1/U`.

**Resultado:** rechazado. No existen reglas de equivalencia, composición, pesos ni finalidad.

### C. Historia constituida igual a actividad

**Ataque:** el puente positivo hace verdadero `CAND-IMMEXP-ACTIVE-001`.

**Resultado:** rechazado. Hecho farmacológico y persistencia del efecto son distintos.

### D. Historia parcial igual a ausencia

**Ataque:** ninguna exposición visible produce conjunto vacío limpio.

**Resultado:** rechazado. La salida es parcial con residuo o `U`.

### E. Duplicar conservadoramente

**Ataque:** contar orden, declaración y administración como tres exposiciones por seguridad.

**Resultado:** rechazado. Fabrica concurrencia y viola procedencia.

### F. Deduplicar por nombre

**Ataque:** fusionar registros nominalmente similares.

**Resultado:** rechazado. Se exigen identidad, hechos y vínculos de derivación.

### G. Última dosis como transductor

**Ataque:** una fecha reciente produce `1` y una antigua produce `0`.

**Resultado:** rechazado. Falta efecto y regla de persistencia.

### H. Semivida como regla suficiente

**Ataque:** usar farmacocinética aislada para toda finalidad.

**Resultado:** rechazado. No constituye por sí sola vigencia inmunológica.

### I. Clase como efecto

**Ataque:** la etiqueta «inmunomodulador» identifica un único efecto.

**Resultado:** rechazado. El efecto debe ser explícito y versionado.

### J. Finalidad dentro de la identidad universal

**Ataque:** definir el parámetro como «activo para OP-IMM-001».

**Resultado:** rechazado. La identidad estable exige efecto; el uso y finalidad pertenecen a `u(p,O)` y a la regla aplicable.

### K. Adoptar una plantilla vacía

**Ataque:** crear `PAR-IMMEXP-ACTIVE-*` sin inventario de efectos ni transductores.

**Resultado:** rechazado. Multiplicaría parámetros candidatos sin semántica ejecutable.

### L. U cómoda

**Ataque:** mantener toda la raíz indeterminada y no producir objeto útil.

**Resultado:** rechazado. Se adopta el puente factual con salidas completas, parciales, vacías limpias y `U` localizadas.

### M. No go global

**Ataque:** cualquier exposición incierta obliga a detener la operación.

**Resultado:** rechazado. La criticidad sólo puede fijarse por una ruta futura y por la dependencia material de cada salida.

### N. Falso go por trazabilidad

**Ataque:** hechos perfectamente trazados demuestran seguridad clínica.

**Resultado:** rechazado. Trazabilidad no sustituye regla, validez ni juicio autorizado.

### O. Abrir matriz con puentes

**Ataque:** introducir las exposiciones o el puente como operandos de G6.

**Resultado:** rechazado. G6 sólo opera sobre parámetros de `A0`.

### P. Deriva por agente, efecto o fuente

**Ataque:** abrir hijos sucesivos para cada instancia.

**Resultado:** rechazado. Las instancias viven dentro del puente; la candidata de actividad termina en `U_ATOMICIDAD_NO_CONSTITUIDA` para esta versión.

### Q. Convertir la U en conclusión clínica

**Ataque:** falta de regla equivale a actividad por precaución o a inactividad por defecto.

**Resultado:** rechazado. `U` no asigna `0`, `1`, consejo ni veto.

**Dictamen adversarial integrado:** `PASA`.

## 9. Recuentos y terminación

| Magnitud | Valor |
|---|---:|
| raíces examinadas | 1 |
| particiones | 1 |
| hijos terminales | 2 |
| puentes constitutivos adoptados | 1 |
| candidatos en `U_ATOMICIDAD_NO_CONSTITUIDA` | 1 |
| parámetros atómicos adoptados | 0 |
| exposiciones agregadas en un estado | 0 |
| matrices, rutas o frames abiertos | 0 |
| intervenciones autorizadas | 0 |
| documentos auxiliares | 0 |

La partición termina porque separa exactamente los dos predicados ya presentes en la pregunta: historia adicional y actividad clínica. Los hechos, agentes, efectos y fuentes son instancias o insumos, no nuevas raíces.

## 10. Consecuencia para la secuencia

```text
G4-CON/SEM-EXP-004 = CERRADA
G5-ATM/SEM-EXP-004 = CERRADA_MIXTA
SEM-EXP-004 = COMPUESTO_PARTICIONADO_FINITO
BRG-IMMEXP-HISTORY-001 = PUENTE_CONSTITUTIVO_ADOPTADO
CAND-IMMEXP-ACTIVE-001 = U_ATOMICIDAD_NO_CONSTITUIDA
A0 = {PAR-GC-PLAN-SYS-001}
G6-MAT = TODAVIA_NO_ABRIBLE
```

Las cinco raíces de exposición `SEM-EXP-001`–`SEM-EXP-005` quedan ahora con estatuto terminal en G5. La secuencia debe continuar con la siguiente familia de `Q0 v0` cuya dependencia G3 no esté cubierta, sin saltar a matriz.

## 11. Declaración

```text
SEM-EXP-004 = COMPUESTO_PARTICIONADO_FINITO
BRG-IMMEXP-HISTORY-001 = PUENTE_CONSTITUTIVO_ADOPTADO
CAND-IMMEXP-ACTIVE-001 = U_ATOMICIDAD_NO_CONSTITUIDA
A0_APORTADO_POR_ESTA_RAIZ = VACIO
A0 = {PAR-GC-PLAN-SYS-001}
FAMILIA_EXPOSICION_G5 = 5_DE_5_TERMINAL
TERMINACION = DEMOSTRADA
DETERMINISMO_NO_EQUIVALE_A_VALIDEZ_CLINICA
BUROCRACIA_AUXILIAR = NINGUNA
```
