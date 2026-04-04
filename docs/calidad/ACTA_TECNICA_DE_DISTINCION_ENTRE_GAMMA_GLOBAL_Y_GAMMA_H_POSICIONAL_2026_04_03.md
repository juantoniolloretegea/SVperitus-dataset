# Acta técnica de distinción entre criticidad global Γ(v) y clasificación posicional γ_H

**Fecha:** 2026-04-03
**Objeto:** fijar la distinción entre dos operadores distintos que comparecen en el ecosistema SV.

## 1. Objeto matemático

### 1.1 Γ(v) en SVperitus

Γ(v) es una medida de criticidad global del vector ternario. Su salida resume la factibilidad de clasificación del vector considerado como totalidad.

### 1.2 γ_H en SV-motor

`gamma_h_labels()` clasifica cada posición abierta `U` según el soporte del horizonte declarado en el dominio activo. Su salida es posicional y no global.

## 2. Regla de no-confusión

No debe compararse una salida global de Γ(v) con una salida posicional de γ_H como si ambos operadores fueran el mismo objeto semántico. Comparten léxico parcial (`irreducible`, `fronteriza`, `resoluble`), pero no comparten dominio, codominio ni función.

## 3. Consecuencia operativa

- Γ(v) puede indicar criticidad global sin que ello determine por sí solo la política de gobernanza del motor.
- γ_H puede bloquear un paso sensible por ausencia de soporte posicional aunque el vector global siga siendo clasificable bajo otra lectura.

## 4. Estado

La distinción queda fijada y deberá mantenerse explícita en futuras piezas de sincronización interrepositorio.
