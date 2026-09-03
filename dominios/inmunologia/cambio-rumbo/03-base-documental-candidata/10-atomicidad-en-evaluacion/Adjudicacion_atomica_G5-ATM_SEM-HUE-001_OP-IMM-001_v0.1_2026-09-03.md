# Adjudicación atómica G5-ATM — SEM-HUE-001 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Puerta:** `G5-ATM/SEM-HUE-001`
- **Operación:** `OP-IMM-001`
- **Raíz:** `SEM-HUE-001`
- **Base exacta:** `51397af0573958d7d0988ee5a670f6f9d40b29d4`
- **Contrato:** `NA0-MATH` v0.3
- **Manifiesto de terminación:** `OP-IMM-001 / Q0 v0`, 03-09-2026
- **Estatuto:** `ADJUDICACION_ATOMICA_CERRADA_CON_U_HIJAS`
- **Efecto clínico:** ninguno
- **Autorización asistencial:** ninguna

## 0. Objeto

Este artefacto ejecuta la prueba de atomicidad de la raíz:

> `SEM-HUE-001`: ¿Existe una alteración cuantitativa del compartimento linfocitario pertinente para el episodio?

La operación no decide si una persona presenta una alteración, no adopta intervalos, umbrales, poblaciones obligatorias, riesgos, diagnósticos o actuaciones. Determina únicamente si la raíz puede gobernarse como un solo parámetro y qué objetos hijos, si existen, admiten adjudicación con el conocimiento actualmente constituido.

La adversarial forma parte de este mismo objeto. No se crea orden, recepción ni artefacto auxiliar.

## 1. Cierre incorporado de la dependencia G4-CON

La auditoría externa comunicada para `G4-S2` verificó:

- identidad del lote de 13 023 bytes y SHA-256 `f94983a51bac907deeb2c7b152b0b9316260196b5b8b5bdf347a5ca6b57750e9`;
- cinco consecuencias candidatas;
- cuatro consecuencias epistemológicas y una asociación clínica potencial no causal;
- ausencia de hallazgos fatales, mayores o menores;
- preservación de cero parámetros, matrices, rutas y frames;
- y declaración `G4-S2_CERRABLE`.

El manifiesto terminal posterior eliminó la congelación causada exclusivamente por la indeterminación del alcance. En consecuencia, dentro de este primer acto sustantivo posterior queda registrada:

```text
G4-CON/SEM-HUE-001 = CERRADA_COMO_DEPENDENCIA_DE_PRUEBA_ATOMICA
```

Este cierre no convierte ninguna consecuencia candidata en regla operacional, veto, causalidad, predicción individual o actuación.

## 2. Entradas constituidas

### 2.1. Entidad observacional

`G3-OBS/SEM-HUE-001` definió una medición linfocitaria:

```text
E_LYM_Q = <
  Medicion_Linfocitaria_ID,
  Especimen,
  Instante_de_muestra,
  Poblacion_objetivo,
  Definicion_de_poblacion,
  Tipo_de_magnitud,
  Valor_original,
  Unidad,
  Metodo_de_enumeracion,
  Estado_de_calidad,
  Contexto_de_referencia,
  Procedencia_por_campo,
  Version
>
```

### 2.2. Consecuencias candidatas

| Identificador | Error evitado |
|---|---|
| `CON-LYM-ID-001` | fusión de poblaciones o definiciones |
| `CON-LYM-MAG-001` | confusión de magnitud, unidad o método |
| `CON-LYM-TIME-001` | estado actual o trayectoria falsos |
| `CON-LYM-FUN-001` | función inmunitaria inventada desde cantidad |
| `CON-LYM-INF-001` | omisión de una asociación potencial o individualización indebida |

Estas consecuencias permiten probar separabilidad. No aportan por sí mismas el transductor que clasifique una alteración.

## 3. Clasificación de los objetos de G3

Los componentes de `E_LYM_Q` no se convierten por traslación automática en parámetros del Sistema Vectorial SV.

| Objeto | Tipo adjudicado en este uso | Motivo |
|---|---|---|
| `Medicion_Linfocitaria_ID` | `CONTROL` | identidad del registro, no proposición clínica |
| `Especimen` | `CONTEXTO` | delimita la validez de la medición |
| `Instante_de_muestra` | `CONTEXTO` | fija horizonte y comparabilidad |
| `Poblacion_objetivo` | `CONTEXTO_IDENTITARIO` | sujeto semántico del futuro parámetro |
| `Definicion_de_poblacion` | `CONTROL_SEMANTICO` | impide equivalencias no demostradas |
| `Tipo_de_magnitud` | `DISCRIMINADOR_DE_PARTICION` | absoluto y proporción admiten estados independientes |
| `Valor_original` | `DATO` | entrada de un transductor, no proposición |
| `Unidad` | `CONTROL_METROLOGICO` | condición de admisibilidad y conversión |
| `Metodo_de_enumeracion` | `CONTROL_ANALITICO` | conserva comparabilidad y procedencia |
| `Estado_de_calidad` | `CONTROL_DE_ADMISION` | puede impedir que el dato alimente una conclusión |
| `Contexto_de_referencia` | `CONTEXTO_DE_REGLA` | no es por sí mismo una clasificación |
| `Procedencia_por_campo` | `CONTROL_DE_TRAZABILIDAD` | evidencia anterior a la conclusión |
| `Version` | `CONTROL_DE_CONFIGURACION` | fija la semántica aplicable |

`N_LYM_MEAS`, `N_LYM_PAIR`, `N_LYM_SERIES` y `N_LYM_REF` permanecen como normalizadores candidatos. No son parámetros ni transductores clínicos finales.

## 4. Ataque de atomicidad de la raíz

### 4.1. Estado único

La raíz no posee un estado único sin pérdida. Para una misma población y muestra pueden divergir:

- recuento absoluto;
- proporción;
- admisibilidad analítica;
- comparabilidad temporal;
- y función inmunitaria, que ni siquiera está observada.

**Resultado:** no pasa como átomo único.

### 4.2. U propia

La `U` del recuento absoluto puede diferir de la `U` de la proporción. Una unidad ausente puede impedir el primero sin impedir necesariamente la segunda; la falta de los insumos de cálculo puede afectar a un resultado derivado y no a uno medido directamente.

**Resultado:** existen `U` independientes.

### 4.3. Consecuencia separable

Confundir recuento absoluto y proporción activa `CON-LYM-MAG-001`. Fusionarlos puede producir falsos positivos o falsos negativos sin que ambos subestados cambien conjuntamente.

**Resultado:** la consecuencia exige separación.

### 4.4. Variación independiente

Un recuento absoluto y una proporción no están ligados por equivalencia lógica. Pueden variar de forma independiente según los demás componentes del recuento y el método aplicado.

**Resultado:** existe partición material útil.

### 4.5. Función

La función linfocitaria no es un subestado de la cantidad. `CON-LYM-FUN-001` exige mantenerla como `FUNCION_NO_CONSTITUIDA`; no se crea un hijo funcional dentro de esta raíz cuantitativa.

**Resultado:** exclusión obligatoria, no tercer parámetro.

### 4.6. Tiempo y trayectoria

El tiempo condiciona vigencia y comparabilidad. Una serie ordenada no constituye por sí sola persistencia, tendencia ni trayectoria clínica. En esta versión no existe una regla que demuestre que la trayectoria sea una proposición requerida e independiente para `OP-IMM-001`.

**Resultado:** contexto y residual potencial; no hijo atómico actual.

## 5. Partición finita

La raíz se particiona una sola vez por el discriminador material ya declarado `Tipo_de_magnitud`:

```text
SEM-HUE-001
  ├─ CAND-LYM-ABS-001
  └─ CAND-LYM-PROP-001
```

| Candidato | Proposición canónica candidata |
|---|---|
| `CAND-LYM-ABS-001` | Para una población linfocitaria explícitamente definida, ¿su recuento absoluto por volumen presenta, en el horizonte del episodio, el estado de alteración establecido por una regla clínica versionada y aplicable? |
| `CAND-LYM-PROP-001` | Para una población linfocitaria explícitamente definida, ¿su proporción presenta, en el horizonte del episodio, el estado de alteración establecido por una regla clínica versionada y aplicable? |

La población no se oculta dentro de un valor agregado. Cada futura instancia deberá identificarla de manera inequívoca. Este corte no enumera qué poblaciones son obligatorias para cada tratamiento o finalidad.

La partición reduce estrictamente las distinciones no resueltas de la raíz y no introduce una nueva pregunta semántica, operación o familia. Satisface la medida de terminación del manifiesto.

## 6. Prueba individual de los hijos

### 6.1. `CAND-LYM-ABS-001`

| Condición de `NA0-MATH` | Resultado |
|---|---|
| identidad | pasa como plantilla condicionada a población definida |
| estado único | pasa en principio para absoluto separado |
| `U` propia | pasa |
| consecuencia separable | pasa mediante `CON-LYM-MAG-001`, `CON-LYM-TIME-001` y `CON-LYM-INF-001` |
| función separable | pasa; no incorpora función inmunitaria |
| variación independiente | pasa respecto de proporción |
| ablación | pasa provisionalmente: su omisión puede eliminar una señal cuantitativa potencialmente pertinente |
| no partición material | no demostrada para todas las poblaciones y usos |
| reproducibilidad | no ejecutable sin transductor final |
| procedencia | estructura disponible; regla clínica final ausente |

Faltan simultáneamente:

1. población o conjunto finito de poblaciones exigibles para el uso;
2. regla clínica de alteración aplicable;
3. intervalo, umbral o criterio admitido con su jurisdicción y versión;
4. horizonte de vigencia;
5. tratamiento de resultados discordantes;
6. transductor final `I_p^v`;
7. función exacta en `OP-IMM-001`.

**Estatuto:** `U_REQUIERE_ADJUDICACION`.

### 6.2. `CAND-LYM-PROP-001`

| Condición de `NA0-MATH` | Resultado |
|---|---|
| identidad | pasa como plantilla condicionada a población definida |
| estado único | pasa en principio para proporción separada |
| `U` propia | pasa |
| consecuencia separable | pasa mediante `CON-LYM-ID-001`, `CON-LYM-MAG-001` y `CON-LYM-INF-001` |
| función separable | pasa; no incorpora función inmunitaria |
| variación independiente | pasa respecto del absoluto |
| ablación | no demostrada universalmente para esta operación |
| no partición material | no demostrada para todas las poblaciones y usos |
| reproducibilidad | no ejecutable sin transductor final |
| procedencia | estructura disponible; regla clínica final ausente |

Faltan los mismos elementos de regla, población, horizonte, transductor y función; además, no está constituido que una proporción sea necesaria en todos los usos en los que pudiera serlo el recuento absoluto.

**Estatuto:** `U_REQUIERE_ADJUDICACION`.

## 7. Adjudicación exhaustiva

| Objeto | Estatuto |
|---|---|
| `SEM-HUE-001` | `COMPUESTO_PARTICIONADO_FINITO` |
| `CAND-LYM-ABS-001` | `U_REQUIERE_ADJUDICACION` |
| `CAND-LYM-PROP-001` | `U_REQUIERE_ADJUDICACION` |
| función linfocitaria | `NO_PERTENECE_A_ESTA_RAIZ_CUANTITATIVA` |
| trayectoria clínica | `NO_CONSTITUIDA_COMO_PROPOSICION_NECESARIA_EN_ESTA_VERSION` |
| `E_LYM_Q` | `ENTIDAD_OBSERVACIONAL_NO_PARAMETRO` |
| cuatro normalizadores | `FUNCIONES_TECNICAS_CANDIDATAS_NO_PARAMETROS` |

Ningún objeto entra todavía en el conjunto de parámetros atómicos adoptados `A0`.

## 8. Adversarial integrada

### Ataque A — convertir los diez observables en diez parámetros

**Intento:** asignar una posición a muestra, tiempo, población, valor, unidad, método, calidad y referencia.

**Resultado:** rechazado. Mezcla datos y controles con proposiciones clínicas y produciría estados ternarios sin predicado clínico propio.

### Ataque B — conservar «estado linfocitario» como átomo

**Intento:** un solo estado resume total, subpoblaciones, absoluto, proporción y función.

**Resultado:** rechazado. Existen variación, `U` y consecuencias independientes.

### Ataque C — adoptar el punto de corte de Warny et al.

**Intento:** usar la categoría del estudio como transductor de `OP-IMM-001`.

**Resultado:** rechazado. Es una definición de una cohorte poblacional; no constituye regla universal, transporte a inmunosupresión ni predicción individual.

### Ataque D — usar el intervalo del laboratorio como verdad universal

**Intento:** fuera de intervalo = `1`; dentro = `0`.

**Resultado:** rechazado. Falta demostrar aplicabilidad a población, magnitud, método, finalidad y horizonte. Además, estar dentro no excluye alteraciones no medidas.

### Ataque E — inferir función desde cantidad

**Intento:** recuento normal = función preservada; recuento bajo = función incapaz.

**Resultado:** rechazado mediante `CON-LYM-FUN-001`.

### Ataque F — fabricar el absoluto desde una proporción

**Intento:** completar el valor ausente sin todos los insumos y reglas.

**Resultado:** rechazado mediante `CON-LYM-MAG-001`; se conserva `U`.

### Ataque G — crear un hijo por cada campo

**Intento:** continuar la descomposición hasta multiplicar parámetros administrativos.

**Resultado:** rechazado. Sólo se divide cuando existen estado, `U`, consecuencia o función clínica independientes. Los metadatos permanecen controles.

### Ataque H — análisis infinito

**Intento:** declarar ambos hijos nuevamente compuestos sin reducir una distinción finita.

**Resultado:** rechazado. Los hijos reciben salida terminal `U_REQUIERE_ADJUDICACION`; no generan otra partición en esta versión.

### Ataque I — abrir matriz por existir dos hijos

**Intento:** crear una matriz de cuantificación linfocitaria.

**Resultado:** rechazado. `A0` sigue vacío para esta raíz.

### Ataque J — convertir U en resultado conservador

**Intento:** tratar la falta de regla como ausencia de alteración o como señal automática de alto riesgo.

**Resultado:** rechazado. La salida es indeterminación de adjudicación, no `0`, `1`, consejo ni veto.

### Ataque K — abandonar el objetivo clínico

**Intento:** cerrar la raíz sin dejar identificada la consecuencia para el paciente y el experto.

**Resultado:** rechazado. Las cinco consecuencias de `G4-CON` se preservan; la falta de transductor impide su operacionalización, no suprime su relevancia.

### Ataque L — extender el corte

**Intento:** incorporar función, diagnóstico, etiología, vacunación, tratamiento o seguimiento.

**Resultado:** rechazado. Permanecen en sus raíces u operaciones correspondientes.

**Dictamen adversarial integrado:** `PASA`.

## 9. Recuentos

| Magnitud | Valor |
|---|---:|
| raíces examinadas | 1 |
| particiones de raíz | 1 |
| hijos terminales | 2 |
| observables convertidos en parámetros | 0 |
| parámetros atómicos adoptados | 0 |
| hijos en `U_REQUIERE_ADJUDICACION` | 2 |
| matrices abiertas | 0 |
| rutas abiertas | 0 |
| frames abiertos | 0 |
| umbrales adoptados | 0 |
| decisiones o intervenciones | 0 |

## 10. Consecuencia para la secuencia

La raíz `SEM-HUE-001` ha terminado su primera adjudicación de atomicidad. No queda abierta por análisis indefinido.

Las dos `U` hijas sólo podrán revisarse mediante evidencia y reglas que identifiquen materialmente población, finalidad, horizonte y transductor. Una fuente nueva no reabre esta versión de manera silenciosa.

Al no existir parámetros adoptados en esta raíz:

```text
G6-MAT/SEM-HUE-001 = NO_ABRIBLE
G7-RUT/SEM-HUE-001 = NO_ABRIBLE
```

La secuencia debe continuar con otra raíz de `Q0 v0` cuyas dependencias puedan constituirse, sin esperar a que estas dos `U` se cierren y sin ampliar el universo.

## 11. Declaración

```text
G4-CON/SEM-HUE-001 = CERRADA
G5-ATM/SEM-HUE-001 = CERRADA_CON_U_HIJAS
SEM-HUE-001 = COMPUESTO_PARTICIONADO_FINITO
CAND-LYM-ABS-001 = U_REQUIERE_ADJUDICACION
CAND-LYM-PROP-001 = U_REQUIERE_ADJUDICACION
A0_APORTADO_POR_ESTA_RAIZ = VACIO
TERMINACION = DEMOSTRADA
BUROCRACIA_AUXILIAR = NINGUNA
```
