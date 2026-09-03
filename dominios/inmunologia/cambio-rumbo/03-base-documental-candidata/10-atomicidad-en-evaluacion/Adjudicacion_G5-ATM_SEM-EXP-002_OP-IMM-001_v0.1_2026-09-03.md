# Adjudicación G5-ATM — SEM-EXP-002 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Puerta:** `G5-ATM/SEM-EXP-002`
- **Operación:** `OP-IMM-001`
- **Raíz:** `SEM-EXP-002`
- **Base exacta:** `597f977bd3e54db39e741719177293794eaa1ec4`
- **Contrato:** `NA0-MATH` v0.3
- **Manifiesto de terminación:** `OP-IMM-001 / Q0 v0`, 03-09-2026
- **Estatuto:** `ADJUDICACION_CERRADA_COMO_CONTROL_NO_PARAMETRIZABLE`
- **Efecto clínico:** ninguno
- **Autorización asistencial:** ninguna

## 0. Objeto

Se adjudica la pregunta:

> `SEM-EXP-002`: ¿Está caracterizada la magnitud planificada de exposición al tratamiento primario?

El objeto no es decidir si la exposición es alta, baja, suficiente, inmunosupresora o peligrosa. Es determinar si «magnitud caracterizada» constituye un parámetro clínico ternario o un control previo sobre los observables que alimentarán parámetros dependientes de una finalidad.

La adversarial queda integrada. No se crea documento auxiliar.

## 1. Perímetro de evidencia y consecuencias

`G3-S1` desarrolló para glucocorticoides sistémicos:

- agente;
- vía y formulación;
- estado de ejecución;
- expresión de dosis;
- unidad y base;
- pauta;
- horizonte;
- y normalizador candidato `N_GC_MAG`.

La cobertura observacional concreta de esta versión se limita a glucocorticoides. No constituye una representación universal de la magnitud de todos los inmunosupresores.

Las consecuencias candidatas aplicables de `G4-S1` son:

| Consecuencia | Aplicación a esta raíz |
|---|---|
| `CON-GC-REP-001` | impide tratar dosis propuesta como administrada |
| `CON-GC-PUR-001` | impide trasladar equivalencias, promedios o umbrales entre finalidades |
| `CON-GC-VAC-SAF-001` | declara una finalidad posterior de seguridad; no aporta el transductor aquí |
| `CON-GC-VAC-EFF-001` | declara una finalidad posterior de efectividad; no aporta el transductor aquí |
| `CON-GC-PJP-001` | declara una finalidad preventiva posterior; no aporta el transductor aquí |

No es necesario abrir otro lote de consecuencias: la separación por raíz queda ejecutada en esta tabla dentro del objeto sustantivo.

## 2. Forma lógica

«Magnitud caracterizada» expresa una propiedad del expediente observacional:

```text
campos_minimos_presentes
AND unidades_admisibles
AND base_de_dosis_explicita
AND pauta_preservada
AND estado_y_horizonte_explicitos
AND procedencia_pasa
AND conflicto_no_bloqueante
```

No expresa todavía una propiedad clínica de la exposición. Los mismos valores pueden clasificarse de manera distinta según:

- agente;
- vía y formulación;
- finalidad;
- población;
- pauta;
- duración;
- concomitancia;
- y regla versionada.

Por tanto, la pregunta puede verificar si existe material suficiente para aplicar una regla futura, pero no puede sustituir esa regla.

## 3. Prueba frente al contrato NA0-MATH

| Condición | Resultado | Motivo |
|---|---|---|
| identidad | pasa como control | pregunta por suficiencia estructural de observables |
| estado único | no pasa como parámetro clínico | «caracterizada» no equivale a un estado de magnitud |
| `U` propia | pasa como control | puede faltar dosis, unidad, base, pauta o procedencia |
| consecuencia separable | no funda átomo | las consecuencias dependen de usos posteriores |
| función separable | control previo | habilita o bloquea transductores posteriores |
| variación independiente | no basta | un cambio numérico no cambia necesariamente el estado de caracterización |
| ablación | pasa como control | retirarlo permitiría aplicar reglas sobre datos incompletos |
| no partición material | no procede como átomo | los campos son observables, no subparámetros |
| reproducibilidad | posible para el control | exige esquema y entrada canónica |
| procedencia | obligatoria | anterior a toda salida |

**Resultado:** no cumple la definición de `PARAMETRO_ATOMICO`. Cumple la función contractual de `CONTROL`.

En el vocabulario terminal del manifiesto, `CONTROL` pertenece a la clase `NO_PARAMETRIZABLE`: no entra en `A0`. Se conserva el rótulo más específico de `NA0-MATH`.

## 4. Control constituido

Identificador:

```text
CTRL-EXP-MAG-001
```

Proposición de control:

> El registro de magnitud de la exposición propuesta contiene, para el agente y uso declarados, los observables mínimos exigidos por el esquema versionado, con unidades, base, pauta, estado, horizonte y procedencia admisibles, sin conflicto bloqueante.

Salida:

```text
C_EXP_MAG_v0.1(X, esquema, h) ->
  CONTROL_PASA
  | CONTROL_NO_PASA
  | U_CONTROL
  | EJECUCION_TECNICA_NO_VALIDA
```

### 4.1. `CONTROL_PASA`

Sólo cuando:

1. el esquema aplicable al agente y versión declara sus campos mínimos;
2. todos los campos exigidos están presentes;
3. valor, unidad y base son sintáctica y semánticamente admisibles;
4. la pauta se conserva sin promedio implícito;
5. propuesta, prescripción y administración no se confunden;
6. el horizonte está fijado;
7. la procedencia pasa;
8. no existe conflicto material.

### 4.2. `CONTROL_NO_PASA`

Cuando existe un defecto demostrado, como:

- unidad incompatible;
- base de dosis contradictoria;
- pauta inválida según el esquema;
- estado de ejecución falsamente representado;
- procedencia rota;
- o aplicación de un esquema que no corresponde al agente o finalidad.

No significa dosis baja, ausencia de riesgo ni exposición irrelevante.

### 4.3. `U_CONTROL`

Cuando la suficiencia no puede decidirse por:

- agente ambiguo;
- esquema no constituido para ese agente;
- dosis, unidad, base o pauta ausentes;
- plan parcial;
- conflicto no adjudicado;
- horizonte desconocido;
- o cobertura documental no demostrada.

No produce una salida clínica conservadora. Impide alimentar el transductor afectado.

## 5. Especialización disponible y límite de cobertura

Para glucocorticoides sistémicos, `G3-S1` permite instanciar el control con:

```text
X_GC_MAG = <
  Agente,
  Formulacion,
  Via,
  Expresion_de_dosis,
  Unidad,
  Base,
  Pauta,
  Estado_de_ejecucion,
  Horizonte,
  Procedencia,
  Version
>
```

Esta especialización no permite:

- calcular prednisona-equivalente;
- promediar pulsos;
- acumular dosis;
- clasificar «dosis alta»;
- inferir efecto;
- aplicar un umbral vacunal;
- decidir valoración preventiva de PJP;
- ni transportar una regla a otro glucocorticoide, vía o finalidad.

Para agentes no cubiertos por un esquema observacional constituido:

```text
CTRL-EXP-MAG-001 = U_CONTROL(ESQUEMA_NO_CONSTITUIDO)
```

No se genera una serie abierta de hijos por fármaco en esta versión.

## 6. Objetos no adoptados

| Objeto | Estatuto |
|---|---|
| valor de dosis | `OBSERVABLE` |
| unidad | `CONTROL_METROLOGICO` |
| base de dosis | `CONTROL_SEMANTICO` |
| pauta | `OBSERVABLE_ESTRUCTURADO` |
| dosis media | `NO_CONSTITUIDA` |
| dosis acumulada | `NO_CONSTITUIDA` |
| prednisona-equivalente | `U_EQUIVALENCIA` |
| «dosis alta» | `U_REGLA_DEPENDIENTE_DE_FINALIDAD` |
| magnitud inmunosupresora | `U_REGLA_DEPENDIENTE_DE_FINALIDAD` |
| riesgo infeccioso | `NO_PERTENECE_A_ESTA_PUERTA` |

Ninguno entra en `A0`.

## 7. Adversarial integrada

### A. Número medible convertido en parámetro

**Ataque:** la dosis existe y, por tanto, debe ocupar una posición ternaria.

**Resultado:** rechazado. Es un observable numérico; necesita una proposición y un transductor dependientes de finalidad.

### B. Caracterización confundida con normalidad

**Ataque:** `CONTROL_PASA` equivale a exposición aceptable.

**Resultado:** rechazado. Sólo certifica aptitud estructural de la entrada.

### C. Ausencia documental convertida en cero clínico

**Ataque:** falta dosis; se asigna «no alta».

**Resultado:** rechazado. Produce `U_CONTROL`.

### D. Primer umbral disponible

**Ataque:** adoptar el umbral de CDC como definición general de magnitud.

**Resultado:** rechazado. Su finalidad vacunal no gobierna PJP, otras vacunas ni riesgo general.

### E. Umbral EULAR trasladado

**Ataque:** usar una recomendación de profilaxis de PJP como regla universal.

**Resultado:** rechazado mediante `CON-GC-PUR-001`.

### F. Equivalencia no versionada

**Ataque:** convertir agentes a prednisona-equivalente por memoria o tabla sin finalidad.

**Resultado:** rechazado. `U_EQUIVALENCIA`.

### G. Promedio de pauta

**Ataque:** convertir pulsos, alternancia o intermitencia en dosis diaria media.

**Resultado:** rechazado. Se preserva la pauta original.

### H. Propuesta igual a administración

**Ataque:** la dosis planificada prueba exposición real.

**Resultado:** rechazado mediante `CON-GC-REP-001`.

### I. Control universal construido desde glucocorticoides

**Ataque:** aplicar `X_GC_MAG` a cualquier inmunosupresor.

**Resultado:** rechazado. La identidad del control es general, pero cada esquema de observables debe estar constituido.

### J. Descomposición infinita por agente

**Ataque:** abrir un hijo para cada fármaco posible.

**Resultado:** rechazado. La raíz termina como control; la ausencia de esquema produce `U_CONTROL`, no nuevos lotes raíz.

### K. Control presentado como producto clínico

**Ataque:** usar `CONTROL_PASA` en una salida al profesional como evaluación de riesgo.

**Resultado:** rechazado. Sólo habilita una regla clínica futura.

### L. No go sistemático

**Ataque:** cualquier campo ausente bloquea globalmente `OP-IMM-001`.

**Resultado:** rechazado. La `U` afecta únicamente al transductor cuyo esquema exige ese campo; su criticidad se decidirá en la ruta.

### M. Trazabilidad usada como validez

**Ataque:** campos perfectamente trazados implican regla clínica válida.

**Resultado:** rechazado. La trazabilidad certifica procedencia; la validez de la regla permanece independiente.

### N. Fusionar magnitud y duración

**Ataque:** una dosis correctamente caracterizada cierra `SEM-EXP-003`.

**Resultado:** rechazado. Duración conserva observables, `U` y consecuencias propias.

**Dictamen adversarial integrado:** `PASA`.

## 8. Recuentos

| Magnitud | Valor |
|---|---:|
| raíces examinadas | 1 |
| controles constituidos | 1 |
| parámetros atómicos adoptados | 0 |
| observables convertidos en parámetros | 0 |
| umbrales adoptados | 0 |
| equivalencias adoptadas | 0 |
| finalidades clínicas cerradas | 0 |
| matrices abiertas | 0 |
| rutas abiertas | 0 |
| documentación auxiliar | 0 |

## 9. Efecto sobre el conjunto autorizado

El conjunto de parámetros no cambia:

```text
A0 = {PAR-GC-PLAN-SYS-001}
```

`CTRL-EXP-MAG-001` se conserva en el registro de controles de `OP-IMM-001`, fuera de `A0`.

La raíz termina:

```text
G4-CON/SEM-EXP-002 = CUBIERTA_POR_MAPEO_DE_G4-S1
G5-ATM/SEM-EXP-002 = CERRADA_COMO_CONTROL
SEM-EXP-002 = CONTROL
MANIFIESTO_TERMINAL = NO_PARAMETRIZABLE
```

No se abre `G6-MAT`. La siguiente raíz materialmente preparada es `SEM-EXP-003`, duración planificada. Debe mantenerse separada de magnitud y recencia.

## 10. Declaración

```text
CTRL-EXP-MAG-001 = CONTROL_CON_U_PROPIA
PARAMETROS_NUEVOS = 0
A0 = {PAR-GC-PLAN-SYS-001}
UMBRAL_CLINICO = NO_CONSTITUIDO
EQUIVALENCIA = NO_CONSTITUIDA
SEM-EXP-003 = NO_CERRADA
TERMINACION = DEMOSTRADA
BUROCRACIA_AUXILIAR = NINGUNA
```
