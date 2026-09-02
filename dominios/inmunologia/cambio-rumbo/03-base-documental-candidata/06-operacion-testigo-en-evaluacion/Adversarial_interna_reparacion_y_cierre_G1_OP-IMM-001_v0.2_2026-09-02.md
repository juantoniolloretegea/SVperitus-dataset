# Adversarial interna de reparación y cierre G1 — OP-IMM-001 v0.2

- **Fecha:** 02-09-2026
- **Antecedente externo:** `PASA`, Claude, sobre commit `3c8444b8ca549a90fc10d52bb6abf1465fb23d83`
- **Objeto:** comprobar la reparación literal de `R-01`
- **Dictamen:** `CIERRE_CONDICIONAL_SATISFECHO`

## 1. Reparación ejecutada

La v0.2 precisa en la pregunta canónica y en `PERFIL_PREDECISIONAL_SELLADO` que:

- la suficiencia se aprecia en G1 a juicio del médico autorizado;
- no existe todavía una regla automática de suficiencia;
- y dicha regla sólo podrá constituirse mediante G2–G5.

No se usa el juicio humano de G1 como sustituto de las reglas posteriores ni se afirma que el sellado autorice tratamiento.

## 2. Regresión dirigida v0.1 → v0.2

Cambios materiales permitidos:

1. versión y estatuto;
2. antecedente de auditoría externa;
3. precisión `R-01` en la pregunta canónica;
4. precisión `R-01` en el estado `PERFIL_PREDECISIONAL_SELLADO`;
5. sección de reparación y cierre;
6. numeración correlativa del glosario;
7. eliminación de la condición futura «si G1 supera auditoría», ya satisfecha.

Se preservan sin cambio material:

- sujeto y población;
- propuesta real de inicio;
- ámbito positivo y negativo;
- cuatro requisitos de inicio;
- cuatro salidas estructurales;
- horizonte predecisional;
- autoridad humana;
- seis familias orientativas;
- exclusiones funcionales;
- 24 registros profesionales;
- contrato de dependencia para G2;
- prohibición de posiciones de matriz en G2.

## 3. Ataques a la reparación

| Ataque | Resultado |
|---|---|
| convertir el juicio médico en algoritmo | bloqueado por texto literal |
| mantener una suficiencia automática implícita | bloqueado por referencia expresa a G2–G5 |
| presentar el sellado como indicación o autorización | sigue prohibido |
| introducir voluntad del paciente como adjudicación del riesgo | no introducido; corresponde a una compuerta asistencial posterior |
| convertir el caso particular del Director en patrón | no introducido |
| anticipar preguntas, observables o consecuencias | no hallado |
| alterar catálogo, pilotos o Lenguaje SV | no hallado |

## 4. Efecto

El reparo externo queda satisfecho sin alterar la identidad clínica de la operación. `G1-OP` queda cerrada en v0.2 y habilita exclusivamente la apertura de `G2-SEM` para formular preguntas candidatas.

No habilita observables o reglas G3, consecuencias plenas G4, atomicidad G5, matrices, composiciones, frames, cohortes ni cambios del Lenguaje SV.
