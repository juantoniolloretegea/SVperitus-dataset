# Recepción de auditoría externa G1 — OP-IMM-001 v0.1

- **Fecha:** 02-09-2026
- **Auditor externo declarado:** Claude
- **Commit material auditado:** `3c8444b8ca549a90fc10d52bb6abf1465fb23d83`
- **Dictamen recibido:** `PASA`
- **Condición de apertura de G2:** incorporar el reparo menor `R-01`
- **Procedencia:** respuesta aportada por el Director; no se presume firma criptográfica del auditor
- **Huella del texto recibido:** SHA-256 `7fe3011c1d22aea0e429f2841b1a613b8a97cfc624e95924e512cbe03c8b36ab`

## 1. Comprobaciones externas recibidas

Claude reprodujo los tres SHA-256 de la orden, confirmó el commit material y verificó la regresión contra su padre. Sólo se añadieron los tres objetos G1 y cuatro líneas al README rector. El XLSX v0.8, `agentes/inmunologia/`, motores, YAML, compositor, Lenguaje SV y `main` permanecieron intactos.

El auditor abrió el XLSX real y comprobó los 24 registros profesionales citados. Dictaminó que:

- `OP-IMM-001` es una operación singular y finita;
- las exclusiones poblacionales son reconocibles;
- la sospecha de infección activa produce salida y no diagnóstico;
- el sellado predecisional no equivale a seguridad, indicación o autorización terapéutica;
- las funciones profesionales permanecen separadas;
- las seis familias son orientaciones, no matrices;
- no se heredan `T(25)=19`, los 50 `Pxx` ni sus capas;
- y no se anticipan parámetros, consecuencias plenas, observables, vetos, matrices, rutas, frames, cohortes o cambios del Lenguaje SV.

## 2. Reparo recibido

### `R-01` · menor · precisión sobre suficiencia

La expresión «suficientemente caracterizado» puede aparentar una regla de suficiencia ya constituida. En G1 el sellado descansa únicamente en el juicio del médico autorizado; la regla automática sólo podrá constituirse en G2–G5.

Corrección exigida:

> suficientemente caracterizado a juicio del médico autorizado, sin regla de suficiencia automática, que se constituirá en G2–G5

El reparo no cambia sujeto, desencadenante, producto, alcance, horizonte, autoridad ni finales de la operación.

## 3. Incertidumbres legítimas confirmadas

| Identificador | Contenido | Puerta posterior |
|---|---|---|
| `U-G1-01` | clausura mínima del perfil | G2–G5 |
| `U-G1-02` | clases farmacológicas concretas | G2, sólo si cambian una pregunta |
| `U-G1-03` | ventanas de validez por observable | G3-OBS |
| `U-G1-04` | vetos y U críticas concretas | G4-CON/G5-ATM |

No son defectos de G1 y no pueden anticiparse mediante la reparación.

## 4. Efecto

La recepción por sí sola no cierra G1. El cierre requiere una versión v0.2 con la precisión literal, regresión dirigida y adversarial interna de reparación. Cumplida esa condición, el dictamen externo autoriza abrir `G2-SEM`, no `G3-OBS` ni ninguna fase posterior.

La auditoría no constituye protocolo clínico, guía de práctica, calculadora de riesgo, adopción asistencial ni decisión sobre un paciente.
