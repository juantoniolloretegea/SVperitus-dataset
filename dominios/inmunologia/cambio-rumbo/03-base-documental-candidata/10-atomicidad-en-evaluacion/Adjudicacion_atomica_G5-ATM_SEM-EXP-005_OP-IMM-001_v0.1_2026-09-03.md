# Adjudicación atómica G5-ATM — SEM-EXP-005 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Puerta:** `G5-ATM/SEM-EXP-005`
- **Operación:** `OP-IMM-001`
- **Raíz:** `SEM-EXP-005`
- **Base exacta:** `2da9c95da7d2a9b419a08885f16e57b081319934`
- **Contrato:** `NA0-MATH` v0.3
- **Manifiesto de terminación:** `OP-IMM-001 / Q0 v0`, 03-09-2026
- **Estatuto:** `ADJUDICACION_ATOMICA_CERRADA_MIXTA`
- **Efecto clínico:** ninguno
- **Autorización asistencial:** ninguna

## 0. Objeto

Este artefacto ejecuta la prueba de atomicidad de:

> `SEM-EXP-005`: ¿Está caracterizada por separado la exposición sistémica a glucocorticoides cuando forme parte de la propuesta o conserve efecto para el episodio?

La raíz combina dos tiempos y dos predicados que no son equivalentes:

1. inclusión de un glucocorticoide sistémico en la exposición terapéutica propuesta;
2. persistencia clínicamente pertinente de un efecto debido a una exposición real anterior o concurrente.

La adjudicación determina si alguno puede entrar en la tabla autorizada `A0`. No clasifica dosis alta, inmunosupresión, riesgo, contraindicación, seguridad vacunal, necesidad de profilaxis ni efecto residual.

La adversarial forma parte de este mismo objeto. No se crea orden, recepción ni documentación auxiliar.

## 1. Dependencias cerradas

La raíz dispone de:

- `G2-SEM`: pregunta `SEM-EXP-005`;
- `G3-OBS`: entidad de exposición `E_GC`, diez observables, cuatro normalizadores y once causas de `U`;
- `G4-CON`: cinco consecuencias candidatas sobre representación, traslado entre finalidades, seguridad y efectividad vacunales y valoración preventiva de neumonía por *Pneumocystis jirovecii*;
- cierre y recepción ya registrados de `G3-S1` y `G4-S1`;
- contrato matemático `NA0-MATH` v0.3;
- y universo finito `Q0 v0`.

Las consecuencias de seguridad vacunal, efectividad y valoración preventiva continúan siendo potenciales y dependientes de reglas posteriores. No se transforman en rutas o intervenciones por esta adjudicación.

## 2. Material observacional y tipos

La entidad de entrada es:

```text
E_GC = <
  Exposicion_GC_ID,
  Agente,
  Formulacion,
  Via,
  Estado_de_ejecucion,
  Expresion_de_dosis,
  Pauta,
  Inicio_planificado,
  Fin_planificado,
  Eventos_administrados,
  Fin_real_documentado,
  Procedencia_por_campo,
  Version
>
```

Los campos no se convierten automáticamente en parámetros.

| Objeto | Tipo en esta adjudicación | Función |
|---|---|---|
| `Exposicion_GC_ID` | `CONTROL` | identidad del registro |
| `Agente` | `OBSERVABLE_IDENTITARIO` | identifica la sustancia declarada |
| `Formulacion` | `CONTEXTO_FARMACEUTICO` | condiciona liberación y absorción |
| `Via` | `CONTEXTO_DE_CLASIFICACION` | impide equiparar uso local y sistémico |
| `Estado_de_ejecucion` | `CONTROL_TEMPORAL_Y_DOCUMENTAL` | preserva propuesta, prescripción y administración |
| `Expresion_de_dosis` | `OBSERVABLE_DE_MAGNITUD` | alimenta `SEM-EXP-002` |
| `Pauta` | `OBSERVABLE_DE_MAGNITUD_Y_TIEMPO` | alimenta `SEM-EXP-002` y `SEM-EXP-003` |
| `Inicio_planificado` | `CONTEXTO_TEMPORAL` | delimita la propuesta |
| `Fin_planificado` | `CONTEXTO_TEMPORAL` | distingue plan cerrado, abierto y desconocido |
| `Eventos_administrados` | `OBSERVABLE_DE_EJECUCION` | prueba administraciones, no efecto persistente |
| `Fin_real_documentado` | `CONTROL_TEMPORAL` | no se infiere desde la última administración |
| `Procedencia_por_campo` | `CONTROL_DE_TRAZABILIDAD` | evidencia anterior a la conclusión |
| `Version` | `CONTROL_DE_CONFIGURACION` | fija identidad y reglas aplicables |

Los normalizadores `N_GC_ID`, `N_GC_MAG`, `N_GC_DUR` y `N_GC_REC` continúan siendo funciones técnicas. No son parámetros clínicos.

## 3. Partición de la raíz

La forma lógica de `SEM-EXP-005` es:

```text
PROPUESTA_INCLUYE_GC_SISTEMICO
OR
EXPOSICION_GC_REAL_CONSERVA_EFECTO_PERTINENTE
```

Ambas proposiciones pueden divergir:

- una propuesta nueva puede incluir glucocorticoide sin exposición previa;
- una exposición previa puede conservar efecto aunque la propuesta nueva no incluya glucocorticoide;
- una administración documentada no demuestra por sí sola persistencia del efecto;
- y un tratamiento propuesto no demuestra administración.

La raíz no admite un único estado `0/1/U` sin pérdida. Se particiona una vez:

```text
SEM-EXP-005
  ├─ CAND-GC-PLAN-SYS-001
  └─ CAND-GC-EFECTO-VIGENTE-001
```

La partición utiliza distinciones ya declaradas en `G2` y `G3`; no amplía `Q0`.

## 4. Candidato CAND-GC-PLAN-SYS-001

### 4.1. Proposición canónica

> La exposición terapéutica propuesta para el episodio incluye al menos un glucocorticoide cuya vía y formulación están documentadas como sistémicas conforme a la clasificación versionada aplicable.

### 4.2. Sujeto y predicado

| Elemento | Constitución |
|---|---|
| Sujeto semántico | exposición terapéutica propuesta y versionada de `OP-IMM-001` |
| Predicado clínico | incluye al menos un componente glucocorticoide sistémico identificado |
| Horizonte | propuesta vigente en el corte predecisional |
| Estados | `0`, `1`, `U` |
| Función | activar la caracterización específica de magnitud y duración sin clasificarlas |
| No significa | exposición administrada, inmunosupresión efectiva, dosis alta, riesgo o indicación |

### 4.3. Dominio de observables

El dominio mínimo exige:

```text
X_GC_PLAN_SYS = <
  Lista_completa_de_componentes_propuestos,
  Agente,
  Formulacion,
  Via,
  Estado_de_ejecucion,
  Inicio_planificado,
  Procedencia_por_campo,
  Version_del_plan,
  Version_de_clasificacion
>
```

La lista completa del tratamiento propuesto pertenece al expediente autorizado. Este objeto no presupone que la ausencia de una mención equivalga a ausencia terapéutica.

### 4.4. Transductor versionado

```text
I_GC_PLAN_SYS_v0.1(X, h) -> {0,1,U}
```

Produce `1` únicamente si concurren todas estas condiciones:

1. existe una propuesta o prescripción vigente para el episodio y horizonte;
2. al menos un componente posee agente identificado;
3. formulación y vía permiten clasificarlo como exposición sistémica;
4. la clasificación aplicada tiene fuente y versión;
5. cada campo decisivo tiene procedencia válida;
6. no existe conflicto material no resuelto.

Produce `0` únicamente si:

1. el conjunto de componentes de la propuesta está declarado completo para la versión y el horizonte;
2. ningún componente satisface la identidad de glucocorticoide sistémico;
3. no existe una fuente admisible contradictoria;
4. la ausencia es explícita dentro de un registro con cobertura suficiente.

Produce `U` si ocurre al menos una de estas condiciones:

- el plan es parcial o su cobertura no está certificada;
- agente, formulación o vía faltan o son ambiguos;
- no puede distinguirse uso sistémico de local;
- la propuesta o su versión no están vigentes;
- la procedencia es insuficiente;
- dos fuentes admisibles discrepan;
- o una clasificación técnica falla.

Un fallo de herramienta produce `EJECUCION_TECNICA_NO_VALIDA`, no `U`, `0` o `1`.

### 4.5. Prueba de atomicidad

| Condición de `NA0-MATH` | Resultado | Fundamento |
|---|---|---|
| identidad | pasa | sujeto y predicado únicos |
| estado único | pasa | sólo pregunta por inclusión en la propuesta |
| `U` propia | pasa | no cierra magnitud, duración, administración o efecto |
| consecuencia separable | pasa | un falso estado contamina la activación de reglas específicas |
| función separable | pasa | activa caracterización; no ejecuta finalidades posteriores |
| variación independiente | pasa | puede cambiar sin fijar dosis, duración o efecto |
| ablación | pasa | retirarlo impide decidir si deben activarse `SEM-EXP-002` y `SEM-EXP-003` para glucocorticoides |
| no partición material | pasa | agente, vía y formulación alimentan una sola proposición de inclusión sistémica |
| reproducibilidad | pasa por contrato | entradas y orden canónicos producen el mismo estado |
| procedencia | pasa | requerida por campo y antes de la conclusión |

### 4.6. Adjudicación

```text
CAND-GC-PLAN-SYS-001 = PARAMETRO_ATOMICO
```

Identificador adoptado:

```text
PAR-GC-PLAN-SYS-001
```

## 5. Registro canónico del parámetro adoptado

```text
p = <
  Parametro_ID = PAR-GC-PLAN-SYS-001,
  Version_parametro = 0.1,
  Proposicion_canonica =
    "La exposicion terapeutica propuesta para el episodio incluye
     al menos un glucocorticoide sistemico identificado",
  Sujeto_semantico = PROPUESTA_TERAPEUTICA_VERSIONADA_OP-IMM-001,
  Predicado_clinico = INCLUYE_GLUC0CORTICOIDE_SISTEMICO,
  Familia = EXPOSICION_PROPUESTA,
  Subfamilia = GLUCOCORTICOIDE_SISTEMICO,
  Dominio_de_observables = X_GC_PLAN_SYS,
  Transductor_versionado = I_GC_PLAN_SYS_v0.1,
  Estado_admisible = {0,1,U},
  Fuentes_aplicadas = {
    OBS-GC-SRC-001,
    OBS-GC-SRC-002,
    G3-OBS/SEM-EXP-005,
    G4-CON/SEM-EXP-005
  },
  Vinculos_de_procedencia = PROCEDENCIA_POR_CAMPO_ANTES_DE_CONCLUSION
>
```

La grafía `GLUCOCORTICOIDE` del valor canónico no modifica la denominación clínica ordinaria. El valor no se interpreta como riesgo, inmunosupresión efectiva o intervención.

## 6. Uso autorizado inicial en OP-IMM-001

```text
u(PAR-GC-PLAN-SYS-001, OP-IMM-001) = <
  Regla_de_activacion =
    propuesta terapeutica vigente dentro del episodio predecisional,
  Matriz_propietaria_o_referencia =
    PENDIENTE_G6_MAT,
  Funcion_en_ruta =
    activar caracterizacion especifica de magnitud y duracion,
  Consecuencias_de_error_u_omision = {
    CON-GC-REP-001,
    CON-GC-PUR-001,
    CON-GC-VAC-SAF-001,
    CON-GC-VAC-EFF-001,
    CON-GC-PJP-001
  },
  Criticidad_y_vetos =
    NO_CONSTITUIDOS_EN_G5,
  Horizonte =
    propuesta vigente en el corte predecisional,
  Fuentes_aplicadas = fuentes declaradas,
  Version = 0.1,
  Autoridad =
    autoridad clinica y documental declarada en OP-IMM-001
>
```

Las tres consecuencias clínicas potenciales no se activan directamente por el parámetro. Requieren sus propias reglas de finalidad, condiciones y autoridades. El uso de G5 sólo enlaza su posible dependencia y prohíbe olvidarlas.

## 7. Candidato CAND-GC-EFECTO-VIGENTE-001

### 7.1. Proposición candidata

> Una exposición sistémica real a glucocorticoides conserva un efecto inmunológico clínicamente pertinente para el episodio y horizonte declarados.

### 7.2. Ataque

Una administración documentada permite afirmar un suceso farmacológico. No permite por sí sola determinar:

- persistencia del efecto;
- magnitud del efecto inmunológico;
- equivalencia entre agentes;
- dependencia de dosis, pauta o duración;
- interacción con otras exposiciones;
- finalidad clínica para la que el efecto es pertinente;
- ni ventana de vigencia.

`N_GC_REC` calcula recencia documental, no efecto biológico. La última administración no constituye el fin real ni la desaparición del efecto.

### 7.3. Elementos ausentes

Faltan:

1. regla por agente, formulación y vía;
2. magnitud y pauta aplicables;
3. duración real o planificada pertinente;
4. función de equivalencia cuando sea necesaria;
5. ventana de efecto versionada;
6. finalidad clínica;
7. tratamiento de exposiciones concurrentes;
8. transductor final;
9. fuentes clínicas específicas para el uso.

### 7.4. Adjudicación

```text
CAND-GC-EFECTO-VIGENTE-001 = U_REQUIERE_ADJUDICACION
```

La `U` no produce riesgo alto, contraindicación, aplazamiento, profilaxis, repetición vacunal ni escalado automático.

## 8. Objetos deliberadamente no adoptados

| Objeto | Resultado |
|---|---|
| dosis por administración | observable de `SEM-EXP-002`, no parámetro en esta raíz |
| pauta | observable compartido con `SEM-EXP-002` y `SEM-EXP-003` |
| duración | objeto de `SEM-EXP-003` |
| recencia | normalizador temporal, no efecto |
| evento administrado | observable; no parámetro independiente en este uso |
| prednisona-equivalente | no constituida |
| dosis acumulada | no constituida |
| «dosis alta» | no constituida |
| inmunosupresión efectiva | no constituida |
| riesgo de infección | no constituido |
| regla vacunal | no constituida |
| valoración preventiva de PJP | no constituida como ruta |

## 9. Adversarial integrada

### Ataque A — hacer verdadero el parámetro por una palabra en texto libre

**Intento:** una nota contiene «corticoide».

**Resultado:** rechazado. Faltan agente, formulación, vía, estado, propuesta vigente, procedencia y versión.

### Ataque B — hacer falso el parámetro por silencio

**Intento:** el plan no menciona glucocorticoides; se asigna `0`.

**Resultado:** rechazado. `0` exige cobertura completa y ausencia explícita en la propuesta versionada. El silencio produce `U`.

### Ataque C — confundir propuesta con administración

**Intento:** `PAR-GC-PLAN-SYS-001 = 1` demuestra exposición real.

**Resultado:** rechazado. El predicado se limita a la propuesta; los eventos administrados permanecen separados.

### Ataque D — confundir inclusión con riesgo

**Intento:** parámetro `1` equivale a alto riesgo infeccioso.

**Resultado:** rechazado. No existe umbral, equivalencia, magnitud, duración ni regla de riesgo.

### Ataque E — usar una vía local como sistémica

**Intento:** pertenencia farmacológica basta para clasificar exposición sistémica.

**Resultado:** rechazado. Formulación y vía son condiciones del transductor; la ambigüedad produce `U`.

### Ataque F — trasladar finalidad

**Intento:** una regla de vacuna viva decide profilaxis frente a PJP, o viceversa.

**Resultado:** rechazado mediante `CON-GC-PUR-001`. El parámetro sólo activa caracterización común.

### Ataque G — adoptar umbral de CDC o EULAR

**Intento:** incluir en el parámetro dosis o duración tomadas de una finalidad concreta.

**Resultado:** rechazado. La identidad del parámetro es previa y neutral respecto de esas reglas.

### Ataque H — ocultar dosis y duración

**Intento:** un solo estado «incluye glucocorticoide» sustituye la magnitud y la duración.

**Resultado:** rechazado. `SEM-EXP-002` y `SEM-EXP-003` conservan identidad y `U` propias.

### Ataque I — adoptar efecto residual desde recencia

**Intento:** una administración reciente implica efecto inmunológico vigente.

**Resultado:** rechazado. `CAND-GC-EFECTO-VIGENTE-001` permanece en `U_REQUIERE_ADJUDICACION`.

### Ataque J — convertir la clasificación ATC en prueba asistencial completa

**Intento:** el código farmacológico decide vía, exposición real o pertinencia clínica.

**Resultado:** rechazado. La clasificación ayuda a la identidad del agente; no sustituye formulación, vía, ejecución o autoridad.

### Ataque K — falso parámetro administrativo

**Intento:** convertir cada campo de `E_GC` en una posición ternaria.

**Resultado:** rechazado. Los campos son observables, contexto o controles salvo que exista una proposición clínica independiente.

### Ataque L — ablación vacía

**Intento:** retirar `PAR-GC-PLAN-SYS-001` no cambia nada porque dosis y duración ya existen.

**Resultado:** rechazado. Sin el parámetro no existe activación gobernada que determine que las preguntas genéricas de magnitud y duración deben aplicarse específicamente al glucocorticoide incluido en la propuesta.

### Ataque M — parámetro dependiente de operación disfrazado de identidad universal

**Intento:** hacer que el identificador signifique «pertinente para OP-IMM-001».

**Resultado:** rechazado. La identidad sólo afirma inclusión en una propuesta terapéutica versionada. La pertinencia y función pertenecen a `u(p,O)`.

### Ataque N — cierre positivo por presión de demostrar A0 no vacío

**Intento:** rebajar cobertura, vía, procedencia o versión para conseguir el primer átomo.

**Resultado:** rechazado. Cada condición se deriva de G3, G4 y `NA0-MATH`; si falta, el transductor produce `U`. La adopción no depende de una cuota de resultados positivos.

### Ataque O — determinismo usado como validez clínica

**Intento:** la reproducción del transductor demuestra seguridad, efectividad o corrección médica.

**Resultado:** rechazado. Sólo demuestra fidelidad a la proposición de inclusión; las reglas clínicas posteriores requieren validación independiente.

### Ataque P — sistema que sólo emite NO GO

**Intento:** tratar todo dato incompleto como bloqueo global.

**Resultado:** rechazado. La `U` queda localizada en este parámetro y uso. No cierra otras raíces ni ordena abstención salvo que una ruta futura constituya su criticidad.

**Dictamen adversarial integrado:** `PASA`.

## 10. Recuentos

| Magnitud | Valor |
|---|---:|
| raíces examinadas | 1 |
| particiones | 1 |
| hijos terminales | 2 |
| parámetros atómicos adoptados | 1 |
| hijos en `U_REQUIERE_ADJUDICACION` | 1 |
| observables convertidos automáticamente en parámetros | 0 |
| umbrales o equivalencias adoptados | 0 |
| reglas clínicas de finalidad adoptadas | 0 |
| matrices abiertas | 0 |
| rutas abiertas | 0 |
| frames abiertos | 0 |
| intervenciones autorizadas | 0 |

## 11. Consecuencia para la secuencia

El conjunto autorizado recibe su primer elemento:

```text
A0 = {PAR-GC-PLAN-SYS-001}
```

Esto demuestra una adjudicación positiva, no la aptitud completa de `OP-IMM-001`, la validez de una regla de riesgo ni la superioridad del sistema.

La propiedad matricial no se decide en este documento. `PAR-GC-PLAN-SYS-001` queda pendiente de `G6-MAT`, pero el manifiesto exige cerrar primero la cobertura de raíces aplicables y no permite construir una matriz oportunista con un solo éxito local.

La secuencia continúa con las raíces `SEM-EXP-002` y `SEM-EXP-003`, cuyas dependencias observacionales ya existen en `G3-S1`, pero cuyas consecuencias candidatas deberán delimitarse por raíz antes de su adjudicación. No se salta directamente a matriz.

## 12. Declaración

```text
G5-ATM/SEM-EXP-005 = CERRADA_MIXTA
SEM-EXP-005 = COMPUESTO_PARTICIONADO_FINITO
PAR-GC-PLAN-SYS-001 = PARAMETRO_ATOMICO
CAND-GC-EFECTO-VIGENTE-001 = U_REQUIERE_ADJUDICACION
A0 = {PAR-GC-PLAN-SYS-001}
G6-MAT = TODAVIA_NO_ABRIBLE
TERMINACION = DEMOSTRADA
DETERMINISMO_NO_EQUIVALE_A_VALIDEZ_CLINICA
BUROCRACIA_AUXILIAR = NINGUNA
```
