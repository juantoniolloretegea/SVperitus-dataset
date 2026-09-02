# Recepción de auditoría externa adversarial — compuerta NA0 INMUNO v0.1

- **Fecha:** 02-09-2026
- **Auditor externo declarado:** Claude
- **Objeto remoto auditado:** commit `46152c6d16090cba2210baf6ac33c29ec7841b08`
- **Dictamen recibido:** `PASA_CON_REPAROS`
- **Aptitud declarada:** apta para una operación clínica testigo una vez corregidos `R-01` a `R-03`
- **Procedencia:** respuesta aportada por el Director; no se presume firma criptográfica del auditor

## 1. Comprobaciones externas recibidas

Claude reprodujo:

- los cuatro SHA-256 de la orden;
- 25 parámetros YAML y 25 funciones `Pxx` por piloto;
- 19 funciones de una clave `_get` y 31 multiclave;
- las ocho familias de colisión;
- `IMMUNO-2/P02` como compuesto declarado;
- `IMMUNO-2/P24` como agregado oculto tras una entrada;
- `IMMUNO-2/P25` como puente derivado;
- 13 puertas, seis ataques de atomicidad y ocho meta-ataques;
- ausencia de cambios en motores, YAML, compositor y Lenguaje SV.

También confirmó que la regla histórica `T(25)=19` puede compensar un único estado crítico con diecinueve estados favorables. La conducta correcta es mantenerla no ratificada.

## 2. Reparos recibidos

| Reparo | Contenido | Tratamiento |
|---|---|---|
| `R-01` | posible circularidad al usar consecuencia y ruta plenas para decidir atomicidad | sustituir por consecuencia ex ante provisional y función de ruta provisional |
| `R-02` | falta de parada cuando G4 conserva la consecuencia en `U` | aplazar A4 y emitir `U_REQUIERE_ADJUDICACION`, nunca `ATÓMICO` |
| `R-03` | Gramática 0.2 e IR 0.3 sin localizador exacto en el contrato | fijar sus localizadores públicos exactos |

Los tres reparos son menores, literales y reparables sin reconsiderar la decisión canónica.

## 3. Incertidumbres recibidas y adjudicación

### U-01 · Lenguaje SV

Se cierra documentalmente en el contrato v0.2 mediante las rutas públicas exactas de Gramática superficial 0.2 y Representación Intermedia 0.3. No se afirma que inmunología pueda modificar esos objetos.

### U-02 · presunta duplicación de P11

La incertidumbre externa reveló un fallo de la adversarial interna, no de la pre-ITI. La copia recibida de `FTD-AE-IMM-SV/0.3` contiene una sola fila `IMMUNO-1/P11`.

La falsa duplicación se originó al imprimir dos intervalos solapados que incluían ambos la línea 230. El cribado v0.2 retracta expresamente la afirmación de v0.1 y deposita una copia de control verificable.

## 4. Efecto

La compuerta no se considera reparada por esta recepción. Su cierre requiere:

1. contrato v0.2 con `R-01` y `R-03`;
2. protocolo v0.2 con `R-02`;
3. cribado v0.2 con retractación de la falsa duplicación;
4. regresión que demuestre que no existe otro cambio material.

Cumplidos esos extremos, el dictamen externo habilita la apertura de una única operación clínica testigo en G1. No habilita parámetros, consecuencias plenas, matrices, rutas ni asistencia.
