# Cierre de auditoría externa — `NA0-MATH` y universo precursor `Q0` INMUNO v0.1

- **Fecha:** 02-09-2026
- **Candidato auditado:** `bef92dd102a170653c0beb39df21ccd5ad0849c8`
- **Línea base:** `9d08c1a8ea334be9689700fb957fb1928641b32c`
- **Orden externa:** commit `07bfd4e685226e1d2eff04e5548809fa07a1d686`, fuera del objeto auditado
- **Dictamen recibido:** `PASA_CON_REPAROS`
- **Reparos:** uno menor, cerrado en este corte
- **Estatuto final:** `NA0_MATH_Q0_G2_S2_CERRADOS`

## 1. Identidad auditada

| Objeto | Bytes | SHA-256 |
|---|---:|---|
| Contrato matemático v0.3 auditado | 15 303 | `5426e97f4ded65198f2e347beed2203e28b1a6da269f45b6e1e4e9e164d14640` |
| Registro precursor v0.1 auditado | 20 886 | `2fd702da9c4cb8766594a740a0212a965e4a83e423b828053a589d9612098120` |
| Adversarial interna v0.3 auditada | 7 899 | `aac9580d9de32893b518bc2011518339f494b64bed7bce9c65d073c86a6cae7f` |

La auditoría abrió el XLSX real, verificó sus cinco hojas, 30 fórmulas y ausencia de errores. Confirmó que el diff contra la línea base estaba limitado a los tres objetos y el índice rector.

## 2. Resultado material

La auditoría declaró:

```text
NA0_MATH_CERRABLE = SI
Q0_INTEGRIDAD_PASA = SI
G2_S2_CERRABLE = SI
G3_OBS_APTA_PARA_APERTURA = SI
```

Pasaron los ataques sobre identidad estable, registro de uso `u(p,O)`, separación de observable, pregunta, parámetro y compuesto, propiedad matricial única, referencias tipadas, no compensación, frames reversibles, dimensión no prefijada, cola finita, integridad del XLSX, privacidad, reproducibilidad y no avance prematuro.

## 3. Reparo R1

La columna `Estatuto atómico` contenía `CANDIDATO_NO_ADJUDICADO` en las 32 filas, mientras el contrato enumeraba siete estatutos exhaustivos de salida. El rótulo previo podía interpretarse como un octavo resultado final.

La alternativa de sustituir las 32 filas por `U_REQUIERE_ADJUDICACION` se rechaza: habría convertido la ausencia de prueba en un resultado de prueba.

La reparación adoptada es:

1. definir `CANDIDATO_NO_ADJUDICADO` como estado de ciclo anterior a la adjudicación;
2. declarar que no equivale a `U_REQUIERE_ADJUDICACION`;
3. renombrar la columna como `Estado previo a adjudicación`;
4. conservar las 32 filas sin estatuto atómico final;
5. reservar los siete estatutos para la salida efectiva de la prueba.

## 4. Efecto del dictamen sobre G2-S2

Las nueve preguntas `SEM-CTX-005`, `SEM-HUE-005` y `SEM-MOD-001`–`007` quedan `CERRADO_SEMANTICAMENTE`.

Este cierre significa que sus formulaciones son diferenciables, conservan `U` propia y no han incorporado pruebas, escalas, umbrales, actuaciones ni atomicidad prematura. No las convierte en parámetros.

Permanecen expresamente diferidas:

- la posible partición de `SEM-HUE-005` en cantidad, función, trayectoria o causa;
- las identidades internas que puedan existir dentro de los modificadores de órgano;
- la criticidad de `U` y las consecuencias clínicas;
- observables, transductores, matrices, rutas y frames.

## 5. Identidad después de la reparación

| Objeto | Bytes | SHA-256 |
|---|---:|---|
| Contrato matemático v0.3 reparado | 15 627 | `5fce31d5d9f5c8d979171c1d91bd47a2a97fdb90fbef990fa8d3d1fda41c1f37` |
| Registro precursor v0.1 reparado | 20 864 | `bd7b168db7348293766ff06742d1eeb22c311672459f1f13ab3f9aff4c872f81` |
| Adversarial interna v0.3 actualizada | 8 882 | `51e95c2c43506224db7ff70e66d64fb36cd55dfcfad15fb9ee8801448defbb2b` |

## 6. Regresión exigida y satisfecha

Los únicos cambios materiales respecto del candidato auditado son:

- estatuto rector del contrato;
- definición del estado previo;
- cierre semántico de las nueve filas G2-S2;
- encabezado inequívoco de la columna del XLSX;
- actualización del dictamen interno y del índice rector.

Permanecen invariantes:

- 32 candidatos únicos;
- distribución `23 + 9`;
- familias `1/5/5/5/4/5/7`;
- 50 posiciones piloto;
- ocho colisiones;
- cero parámetros atómicos autorizados;
- cero matrices constituidas;
- cero observables y consecuencias plenas constituidos;
- cero errores de fórmula.

## 7. Consecuencia operativa

`G3-OBS` queda apta para abrir un primer lote acotado mediante un acto posterior. No queda abierta por este documento. `G5-ATM` permanece cerrada.

El primer lote deberá constituir observables y transductores candidatos sin adjudicar todavía atomicidad, consecuencias plenas, matrices, rutas o frames.

## 8. Declaración

Este cierre es documental y metodológico. No constituye recomendación asistencial, parámetro clínico, observable, consecuencia clínica, matriz, ruta o frame; no modifica el Lenguaje SV y no contiene información atribuible a episodios, personas o centros.

