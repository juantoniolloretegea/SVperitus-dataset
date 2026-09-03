# Adjudicación G5-ATM — SEM-EXP-003 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Puerta:** `G5-ATM/SEM-EXP-003`
- **Operación:** `OP-IMM-001`
- **Raíz:** `SEM-EXP-003`
- **Base exacta:** `de0ec41439fc73d3749d588ce2e4c64e127780e0`
- **Contrato:** `NA0-MATH` v0.3
- **Manifiesto de terminación:** `OP-IMM-001 / Q0 v0`, 03-09-2026
- **Estatuto:** `ADJUDICACION_CERRADA_COMO_CONTROL_NO_PARAMETRIZABLE`
- **Efecto clínico:** ninguno
- **Autorización asistencial:** ninguna

## 0. Objeto

Se adjudica:

> `SEM-EXP-003`: ¿Está caracterizada la duración planificada de la exposición primaria?

La raíz pregunta por la caracterización temporal de una propuesta terapéutica. No pregunta todavía si la duración supera un umbral, conserva un efecto, produce inmunosupresión, modifica el riesgo ni activa una intervención.

El objetivo es decidir si la duración planificada constituye un parámetro clínico ternario o un observable temporal gobernado por un control de suficiencia.

La adversarial queda integrada en este artefacto. No se crea documentación auxiliar.

## 1. Dependencias y correspondencia G4

`G3-S1` distingue:

- inicio planificado;
- fin planificado;
- final abierto por decisión;
- final desconocido;
- eventos administrados;
- fin real documentado;
- duración planificada;
- duración real observada;
- y recencia.

La normalización candidata es:

```text
N_GC_DUR(E_GC, h) ->
  <Tipo_duracion, Inicio, Fin_o_corte, Valor, Unidad_temporal, Estado> | U
```

Las consecuencias de `G4-S1` aplicables son:

| Consecuencia | Aplicación a duración |
|---|---|
| `CON-GC-REP-001` | impide usar el plan como exposición real o la última administración como cierre |
| `CON-GC-PUR-001` | impide trasladar ventanas y umbrales entre finalidades |
| `CON-GC-VAC-SAF-001` | declara una posible finalidad posterior; no aporta aquí su ventana |
| `CON-GC-VAC-EFF-001` | conserva cronología y posible efecto sobre efectividad; no constituye regla |
| `CON-GC-PJP-001` | conserva una finalidad preventiva distinta; no aporta umbral universal |

Esta tabla ejecuta la delimitación por raíz dentro del objeto sustantivo. No abre otro lote G4.

## 2. Separaciones obligatorias

### 2.1. Duración planificada

Intervalo previsto entre el inicio y el fin declarados en la propuesta. Puede estar:

- cerrado;
- condicionado;
- abierto por decisión;
- o indeterminado.

### 2.2. Duración real observada

Intervalo reconstruible a partir de sucesos administrados admisibles y de un cierre real documentado. No se deduce de la mera prescripción.

### 2.3. Recencia documental

Intervalo entre la última administración conocida y el horizonte. No demuestra que la exposición haya finalizado ni que persista su efecto.

### 2.4. Persistencia de efecto

Proposición clínica dependiente de agente, formulación, vía, dosis, pauta, duración, finalidad y fuentes específicas. Quedó correctamente en:

```text
CAND-GC-EFECTO-VIGENTE-001 = U_REQUIERE_ADJUDICACION
```

Ninguna de estas cuatro realidades sustituye a las restantes.

## 3. Forma lógica de la pregunta

«Duración planificada caracterizada» significa:

```text
inicio_planificado_admisible
AND (
  fin_planificado_admisible
  OR abierto_por_plan_explicito
  OR condicion_de_final_explicita
)
AND estado_de_ejecucion_preservado
AND precision_temporal_declarada
AND procedencia_pasa
AND version_pasa
AND conflicto_no_bloqueante
```

Es una condición de aptitud documental para aplicar futuras reglas. No es un predicado clínico sobre la magnitud, el efecto o el riesgo de la exposición.

## 4. Prueba de atomicidad

| Condición de `NA0-MATH` | Resultado | Motivo |
|---|---|---|
| identidad | pasa como control | suficiencia de la representación temporal |
| estado único | no pasa como parámetro clínico | una duración caracterizada no posee significado clínico independiente de finalidad |
| `U` propia | pasa como control | inicio, fin, precisión, estado o procedencia pueden faltar |
| consecuencia separable | no funda átomo | las consecuencias clínicas dependen de usos posteriores |
| función separable | control previo | habilita o bloquea transductores temporales |
| variación independiente | no basta | cambiar el intervalo no decide por sí solo un estado clínico |
| ablación | pasa como control | retirarlo permitiría aplicar reglas sin tiempo admisible |
| no partición material | no procede como átomo | plan, realidad, recencia y efecto deben permanecer tipados |
| reproducibilidad | posible para el control | exige entrada, esquema y horizonte canónicos |
| procedencia | obligatoria | se conserva antes del cálculo |

**Resultado:** `SEM-EXP-003` no es `PARAMETRO_ATOMICO`. Es `CONTROL` y, conforme al manifiesto, termina dentro de la clase `NO_PARAMETRIZABLE`.

## 5. Control constituido

Identificador:

```text
CTRL-EXP-DUR-001
```

Proposición de control:

> La duración planificada de la exposición primaria está representada mediante inicio, final cerrado, condición de final o apertura deliberada, con precisión, estado, procedencia y versión suficientes para el esquema y horizonte aplicables.

Función:

```text
C_EXP_DUR_v0.1(X, esquema, h) ->
  CONTROL_PASA
  | CONTROL_NO_PASA
  | U_CONTROL
  | EJECUCION_TECNICA_NO_VALIDA
```

### 5.1. `CONTROL_PASA`

Exige conjuntamente:

1. propuesta vigente e identificada;
2. inicio planificado con precisión suficiente;
3. fin planificado, condición de final o `ABIERTO_POR_PLAN` explícitos;
4. distinción entre planificación y ejecución real;
5. esquema temporal aplicable;
6. horizonte declarado;
7. procedencia por campo;
8. versión fijada;
9. ausencia de conflicto bloqueante.

Una duración abierta por decisión puede pasar el control como **duración planificada abierta**. No se convierte en una cifra.

### 5.2. `CONTROL_NO_PASA`

Se produce ante defecto demostrado:

- fin anterior al inicio sin regla que lo explique;
- unidad temporal incompatible;
- mezcla de propuesta y administración;
- última administración utilizada como fin real;
- precisión falsamente aumentada;
- versión o procedencia incorrectas;
- o aplicación de un esquema temporal ajeno.

No significa duración breve, efecto ausente ni riesgo bajo.

### 5.3. `U_CONTROL`

Se produce cuando:

- falta el inicio;
- no puede distinguirse `ABIERTO_POR_PLAN` de `U_FIN`;
- el final o su condición son ambiguos;
- la propuesta es parcial;
- el horizonte no está fijado;
- existe conflicto no adjudicado;
- el esquema temporal del agente no está constituido;
- o la procedencia es insuficiente.

No genera una duración por defecto ni una abstención global.

## 6. Regla de cálculo permitida

Cuando inicio y fin planificados son admisibles y utilizan una convención temporal versionada:

```text
D_plan = diferencia_temporal_versionada(inicio, fin)
```

El resultado conserva:

```text
<
  valor_original_de_inicio,
  valor_original_de_fin,
  precision,
  convencion_de_intervalo,
  valor_derivado,
  unidad,
  procedencia,
  version
>
```

No se permite:

- redondear para alcanzar un umbral;
- completar un fin abierto;
- sustituir fecha de prescripción por inicio;
- deducir duración real desde el plan;
- ni convertir duración en persistencia de efecto.

Un valor derivado continúa siendo observable, no parámetro clínico.

## 7. Cobertura y límites

La especialización material disponible corresponde a glucocorticoides sistémicos mediante `E_GC`. Para otros tratamientos primarios sin esquema temporal constituido:

```text
CTRL-EXP-DUR-001 = U_CONTROL(ESQUEMA_NO_CONSTITUIDO)
```

No se abre un hijo por agente. Tampoco se declara que todos los tratamientos compartan la misma semántica temporal.

Quedan fuera:

- umbrales de duración;
- ventanas de inmunosupresión;
- tiempo hasta recuperación;
- vida media farmacológica;
- dosis acumulada;
- equivalencia entre agentes;
- duración «prolongada»;
- riesgo infeccioso;
- reglas vacunales;
- reglas de profilaxis;
- y persistencia del efecto inmunológico.

## 8. Adversarial integrada

### A. Duración numérica convertida en parámetro

**Ataque:** el número de días debe ocupar una posición ternaria.

**Resultado:** rechazado. Es un observable que sólo adquiere significado dentro de un predicado clínico versionado.

### B. Abierto por plan igual a dato ausente

**Ataque:** `ABIERTO_POR_PLAN` se serializa como `U_FIN`.

**Resultado:** rechazado. Uno es una decisión documentada; el otro, ausencia de conocimiento.

### C. Plan igual a exposición real

**Ataque:** duración prevista demuestra duración administrada.

**Resultado:** rechazado mediante `CON-GC-REP-001`.

### D. Última administración igual a final

**Ataque:** el último evento conocido cierra la exposición.

**Resultado:** rechazado. Hace falta fin real explícito o regla autorizada.

### E. Recencia igual a efecto vigente

**Ataque:** una administración reciente demuestra inmunosupresión persistente.

**Resultado:** rechazado. `CAND-GC-EFECTO-VIGENTE-001` conserva `U`.

### F. Umbral vacunal convertido en duración universal

**Ataque:** una duración definida para vacuna viva gobierna cualquier finalidad.

**Resultado:** rechazado mediante `CON-GC-PUR-001`.

### G. Regla de PJP trasladada a vacunación

**Ataque:** el intervalo de una recomendación preventiva decide seguridad o efectividad vacunal.

**Resultado:** rechazado.

### H. Fin abierto completado por conveniencia

**Ataque:** asignar una duración máxima o esperada.

**Resultado:** rechazado. Se conserva apertura o `U`.

### I. Precisión inventada

**Ataque:** fecha aproximada convertida en instante exacto.

**Resultado:** rechazado. La precisión forma parte del observable.

### J. Control presentado como regla clínica

**Ataque:** `CONTROL_PASA` significa duración clínicamente aceptable.

**Resultado:** rechazado. Sólo certifica aptitud de la representación temporal.

### K. Trazabilidad confundida con validez

**Ataque:** un intervalo bien documentado demuestra una regla correcta.

**Resultado:** rechazado. La fuente de la regla clínica deberá validarse separadamente.

### L. Bloqueo global

**Ataque:** `U_CONTROL` obliga siempre a `ABSTENERSE_O_ESCALAR`.

**Resultado:** rechazado. Su criticidad depende de la ruta y finalidad aún no constituidas.

### M. Fusionar magnitud y duración

**Ataque:** `CTRL-EXP-MAG-001` cierra la duración.

**Resultado:** rechazado. Poseen campos, `U` y errores independientes.

### N. Descomposición infinita

**Ataque:** abrir hijos para duración planificada, real, recencia y efecto dentro de esta raíz.

**Resultado:** rechazado. La raíz pregunta sólo por el plan; los demás objetos ya están tipados como observables, normalizadores o candidato independiente en `U`.

### O. Forzar un segundo parámetro positivo

**Ataque:** adoptar «duración caracterizada» para aumentar `A0`.

**Resultado:** rechazado. Es un control, no una proposición clínica.

**Dictamen adversarial integrado:** `PASA`.

## 9. Recuentos

| Magnitud | Valor |
|---|---:|
| raíces examinadas | 1 |
| controles constituidos | 1 |
| parámetros adoptados | 0 |
| umbrales adoptados | 0 |
| ventanas clínicas adoptadas | 0 |
| duraciones imputadas | 0 |
| matrices abiertas | 0 |
| rutas abiertas | 0 |
| documentos auxiliares | 0 |

## 10. Efecto sobre el corte

El conjunto autorizado permanece:

```text
A0 = {PAR-GC-PLAN-SYS-001}
```

El control queda fuera de `A0`:

```text
CTRL-EXP-DUR-001 = CONTROL_CON_U_PROPIA
```

La raíz termina:

```text
G4-CON/SEM-EXP-003 = CUBIERTA_POR_MAPEO_DE_G4-S1
G5-ATM/SEM-EXP-003 = CERRADA_COMO_CONTROL
SEM-EXP-003 = CONTROL
MANIFIESTO_TERMINAL = NO_PARAMETRIZABLE
```

No se abre `G6-MAT`. Las tres raíces cubiertas materialmente por `G3-S1` han quedado adjudicadas:

- `SEM-EXP-005`: compuesto finito, un parámetro y una `U`;
- `SEM-EXP-002`: control de magnitud;
- `SEM-EXP-003`: control de duración.

La siguiente operación debe regresar al inventario de `Q0 v0` y seleccionar una raíz por dependencia clínica y cobertura, no para producir un resultado predeterminado.

## 11. Declaración

```text
CTRL-EXP-DUR-001 = CONTROL_CON_U_PROPIA
PARAMETROS_NUEVOS = 0
A0 = {PAR-GC-PLAN-SYS-001}
UMBRAL_TEMPORAL = NO_CONSTITUIDO
EFECTO_VIGENTE = U_REQUIERE_ADJUDICACION
TERMINACION = DEMOSTRADA
DETERMINISMO_NO_EQUIVALE_A_VALIDEZ_CLINICA
BUROCRACIA_AUXILIAR = NINGUNA
```
