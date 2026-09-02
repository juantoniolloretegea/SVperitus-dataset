# Adversarial interna del modelo matemático de parámetros — INMUNO v0.3

- **Fecha:** 02-09-2026
- **Compuerta:** `NA0-MATH`
- **Objeto principal:** `Contrato_matematico_parametro_atomico_matriz_ruta_INMUNO_v0.3_2026-09-02.md`
- **Registro computable:** `Registro_precursor_parametros_INMUNO_v0.1_2026-09-02.xlsx`
- **Estatuto:** `ADVERSARIAL_INTERNA_NO_SUSTITUYE_REVISION_EXTERNA`

## 1. Identidad calculada

| Objeto | Bytes | SHA-256 |
|---|---:|---|
| Contrato matemático v0.3 | 15 627 | `5fce31d5d9f5c8d979171c1d91bd47a2a97fdb90fbef990fa8d3d1fda41c1f37` |
| Registro precursor v0.1 | 20 864 | `bd7b168db7348293766ff06742d1eeb22c311672459f1f13ab3f9aff4c872f81` |

## 2. Regla de suficiencia

No basta comprobar que el texto contiene definiciones. Cada ataque debe intentar construir un contraejemplo que permita una mezcla, duplicación, compensación, cierre infinito o adopción prematura. El ataque sólo pasa cuando el contrato obliga a detectar o rechazar ese contraejemplo.

## 3. Ataques A–N

| Ataque | Contraejemplo material | Resultado exigido | Resultado |
|---|---|---|---|
| A · identidad estable | el mismo déficit recibe dos identificadores porque aparece en dos operaciones | conservar `Parametro_ID`; variar sólo `alpha_v` | `PASA` |
| B · falsa relatividad | una operación redefine el sujeto o predicado del parámetro para reutilizarlo | nueva identidad candidata; no proyección artificial | `PASA` |
| C · observable convertido en átomo | cada valor de laboratorio se declara parámetro aunque no tenga decisión propia | mantenerlo como observable del transductor | `PASA` |
| D · compuesto con un solo campo | un campo informático resume estado, intervención y control | `COMPUESTO_A_DESDOBLAR` | `PASA` |
| E · átomo con varios observables | dos evidencias alternativas de una sola proposición se fuerzan a ser dos parámetros | permitir varios observables si no hay independencia clínica | `PASA` |
| F · U oculta | una subproposición indeterminada se cierra por el estado favorable de otra | desdoblar o conservar `U`; nunca compensar | `PASA` |
| G · duplicación matricial | dos matrices copian el mismo parámetro y lo recalculan | un propietario; referencia tipada desde la otra | `PASA` |
| H · mayoría clínica | 19 estados favorables compensan un veto crítico | bloquear la salida afectada | `PASA` |
| I · resumen opaco | el frame resumen elimina una `U` visible en un frame constitutivo | proyección no pasa; exigir reversibilidad | `PASA` |
| J · dimensión prefijada | se agregan candidatos para completar una matriz `(25,5)` | rechazar relleno dimensional | `PASA` |
| K · piloto como autoridad | un `Pxx` simple hereda estatuto atómico | mantenerlo como señal histórica | `PASA` |
| L · pregunta como parámetro | las 32 preguntas G2 se incorporan directamente a `A_v` | mantener cero parámetros autorizados | `PASA` |
| M · cierre infinito | cualquier novedad obliga a reabrir todo el universo | cerrar versión y abrir suceso trazable sólo para afectados | `PASA` |
| N · determinismo degradado | una reejecución produce otro frame pero se acepta por equivalencia clínica | `REPRODUCIBILIDAD_NO_PASA` | `PASA` |

### Prueba adicional · identidad frente a uso

Contraejemplo: el mismo parámetro participa en dos operaciones y la omisión posee consecuencias diferentes. Crear dos parámetros duplicaría la identidad; imponer una consecuencia universal falsearía ambos contextos. El contrato conserva un solo `Parametro_ID` y exige dos registros `u(p,O)` con activación, función, consecuencia, criticidad, fuentes, versión y autoridad propias. El contraejemplo queda absorbido.

## 4. Pruebas de ablación decisivas

### 4.1. Separación de estado, U y consecuencia

Supuesto atacado: un candidato `q` contiene dos proposiciones `a` y `b`.

- Si puede existir `a=1, b=0`, existe divergencia de estado.
- Si puede existir `a=U, b∈{0,1}`, existe `U` separable.
- Si omitir `a` y omitir `b` producen consecuencias o funciones de ruta distintas, existe separabilidad clínica.

En cualquiera de los tres casos, retirar una de las partes deja una decisión distinta y `q` no es atómico. El contrato lo clasifica como `COMPUESTO_A_DESDOBLAR`.

### 4.2. Límite inferior de división

Supuesto atacado: un parámetro se divide en cada analito, documento, fecha o campo que lo demuestra.

Si la pieza retirada sólo elimina una evidencia posible y no crea un estado, `U`, consecuencia o función de ruta independientes, la división adicional no supera la prueba. La pieza permanece en `Dominio_de_observables`.

### 4.3. No compensación

Supuesto atacado: un vector contiene un veto crítico y numerosos estados favorables.

Eliminar la regla de no compensación permitiría una salida favorable por mayoría. Con la regla vigente:

```text
VETO_CRITICO = 1 -> NO_EJECUTAR_SALIDA_AFECTADA
```

El resultado global no puede borrar el veto. La ablación demuestra que la regla es material y necesaria.

## 5. Recuentos computados

El registro precursor contiene:

| Objeto | Resultado |
|---|---:|
| Preguntas candidatas | 32 |
| G2-S1 | 23 |
| G2-S2 | 9 |
| Familias | 7 |
| Distribución | `1/5/5/5/4/5/7` |
| Posiciones piloto | 50 |
| Familias de colisión | 8 |
| Parámetros atómicos autorizados | 0 |
| Matrices constituidas | 0 |

La hoja `Pilotos_50` diferencia señal recogida, mapeo compuesto, pendiente de otro lote, agregado no reutilizable y puente no atómico. Ninguna correspondencia hereda valores, umbrales, reglas o atomicidad.

## 6. Cobertura y residuo visible

El registro conserva como pendientes, sin declararlos irrelevantes:

- inmunización y protección;
- profilaxis;
- exposiciones geográficas, respiratorias y ambientales;
- seguimiento posterior;
- y los despieces específicos aún no constituidos.

El residuo impide una falsa declaración de exhaustividad y permite cerrar el corte sin ocultar trabajo futuro.

## 7. Privacidad y autoridad

Los dos objetos son impersonales y no contienen datos de episodios, personas o centros. No transforman experiencia individual en regla ni permiten reutilizar historias clínicas como ejemplos. La decisión clínica permanece fuera de esta compuerta y la implementación no adquiere autoridad para crear, fusionar o graduar parámetros.

## 8. Regresión conceptual contra v0.2

El cambio material deliberado es uno:

```text
v0.2: atomicidad formulada como relativa a operación, población y horizonte
v0.3: identidad atómica estable; operación, episodio y horizonte gobiernan activación y valor
```

Se conservan: distinción observable/transductor/parámetro, estado ternario, consecuencia, propietario matricial único, referencia tipada, composición dirigida, frame por matriz, no compensación y freno de mano versionado.

## 9. Incertidumbres legítimas

- `U-01`: ninguna de las 32 preguntas ha pasado todavía por observables, transductor, consecuencia plena y adjudicación de atomicidad.
- `U-02`: los tamaños y propietarios de las matrices no existen hasta disponer de parámetros autorizados.
- `U-03`: las rutas críticas y frames normalizados no existen hasta constituir matrices y transiciones.

Estas `U` no son fallos del contrato; son los límites que impiden adelantarse a fases no ejecutadas.

## 10. Dictamen interno

`PASA_INTERNA_Y_REPARO_EXTERNO_CERRADO`

El modelo es finito, no duplica identidades, distingue evidencia de parámetro, impide composición por conveniencia, conserva `U` y vetos, y ofrece una regla de cierre verificable. La auditoría externa declaró cerrables `NA0-MATH`, la integridad de `Q0` y `G2-S2`, con un único reparo menor: distinguir el estado previo de los siete resultados de adjudicación. La reparación queda aplicada mediante definición expresa y encabezado inequívoco. El siguiente lote acotado de `G3-OBS` queda apto para apertura, pero este objeto no lo constituye ni abre `G5-ATM`.

### Cierre del reparo externo R1

Ataque: interpretar `CANDIDATO_NO_ADJUDICADO` como octavo estatuto final o sustituirlo prematuramente por `U_REQUIERE_ADJUDICACION`.

Corrección aplicada:

1. el contrato lo define como estado de ciclo anterior a la prueba;
2. el XLSX denomina la columna `Estado previo a adjudicación`;
3. las 32 filas conservan `CANDIDATO_NO_ADJUDICADO`;
4. ninguna fila recibe `U_REQUIERE_ADJUDICACION` sin haber sido adjudicada;
5. las nueve filas G2-S2 pasan exclusivamente a `CERRADO_SEMANTICAMENTE` en su columna propia.

La ablación confirma la necesidad: sin la palabra `previo`, el rótulo puede confundirse con el resultado; sustituyéndolo por `U_REQUIERE_ADJUDICACION`, se fingiría una prueba aún no ejecutada. La reparación evita ambos fallos.

## 11. Declaración

Esta adversarial no constituye parámetros, observables, consecuencias clínicas, matrices, rutas o frames; no modifica el Lenguaje SV y no autoriza asistencia.
