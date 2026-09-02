# Adversarial interna G1 — OP-IMM-001 v0.1

- **Fecha:** 02-09-2026
- **Objeto:** definición de la primera operación clínica testigo
- **Dictamen interno:** `PASA_PARA_AUDITORIA_EXTERNA`
- **Efecto máximo:** permitir auditoría externa; no abrir todavía `G2-SEM`

## 1. Ataques ejecutados

| Ataque | Caso adverso | Resultado |
|---|---|---|
| Unidad operacional | iniciar, intensificar y seguir tratamiento podrían confundirse | la candidata conserva sólo el episodio previo al inicio; intensificación y seguimiento quedan fuera |
| Paciente real | una cohorte media sustituye al sujeto | rechazado: el sujeto es un paciente individual |
| Alcance poblacional | trasplante, CAR-T, quimioterapia hematológica o pediatría entran por semejanza | `FUERA_DE_ALCANCE`; requieren operación propia |
| Infección activa | fiebre o sospecha infecciosa se absorbe como simple factor de riesgo | sólo puede activar salida; diagnóstico y tratamiento pertenecen a otra operación |
| Autoridad | la IA o un frame decide iniciar el inmunosupresor | prohibido; cierre y decisión pertenecen al médico autorizado |
| Función profesional | interpretación de laboratorio se presenta como prescripción | guardarraíl jurisdiccional expreso |
| Umbral heredado | 19 estados favorables cierran pese a un riesgo crítico | `T(25)=19` no entra en la operación |
| U crítica | falta un elemento relevante y el sistema completa por plausibilidad | salida `U_CRITICA_NO_CERRADA` o `ABSTENERSE_O_ESCALAR` |
| Prescripción encubierta | caracterizar riesgo se convierte en elegir pruebas, vacunas o profilaxis | operaciones excluidas; puede señalarse una necesidad de información, pero no seleccionar ni ordenar su prueba |
| Horizonte | se impone la misma ventana a todos los datos | cada observable futuro conservará su validez específica |
| Coste y recursos | una prueba no disponible modifica el riesgo clínico | sólo puede generar anexo, imposibilidad material o escalado; no cambia la lectura clínica |
| Herencia de pilotos | las cinco capas o 50 `Pxx` pasan a ser la clausura | rechazado expresamente |
| Matriz prematura | las seis familias preliminares se convierten en seis matrices | prohibido por texto literal |
| Cohorte lateral | se abre Nor-vaC, OCTAVE, SUCCEED, BIFAP o ImmPort | diferido; G1 se sostiene en corpus profesional |
| Lenguaje SV | se propone una primitiva para representar la operación | fuera de alcance; cero escritura |

## 2. Ataque de suficiencia profesional

La operación no nace únicamente de `IMMUNO-2`. El catálogo v0.8 proporciona soporte convergente:

- España: interpretación clínica, función médica, inmunosupresión terapéutica y seguimiento;
- Reino Unido: inmunosupresores, profilaxis y complicaciones como contextos profesionales;
- Australia–Aotearoa Nueva Zelanda: razonamiento, prescripción, investigaciones y atención longitudinal como operaciones diferenciadas;
- Canadá: infección, terapéutica, seguridad, planificación y seguimiento.

El soporte demuestra pertinencia profesional, no eficacia clínica ni suficiencia de parámetros.

## 3. Prueba de final finito

La operación no termina cuando desaparece todo riesgo. Termina cuando el expediente predecisional queda sellado por autoridad humana, conserva las incertidumbres y no pretende resolver operaciones excluidas.

El análisis no puede prolongarse por una guía, cohorte o variable interesante que no tenga dependencia demostrada con la operación. Una novedad posterior al sellado abre `REOPEN_REQUIRED` en nueva versión.

## 4. Contraejemplos de parada

### C1. Paciente con sospecha de infección activa

La operación no diagnostica la infección ni recomienda tratamiento. Señala salida a la operación aguda correspondiente. Resultado: `FUERA_DE_ALCANCE` o escalado según regla futura.

### C2. Inicio urgente con dato crítico ausente

El sistema no convierte urgencia en certeza ni decide demorar/iniciar. Preserva `U_CRITICA_NO_CERRADA` y presenta el bloqueo al médico.

### C3. Recurso no disponible

La carencia material se registra aparte. No transforma un riesgo en aceptable. Si impide una ejecución segura, se informa y escala; no se recalcula la clínica a favor del presupuesto.

### C4. Paciente ya tratado que requiere seguimiento

No se fuerza dentro del episodio basal. Pertenece a una futura operación longitudinal.

## 5. Incertidumbres legítimas

| U | Razón | Puerta de resolución |
|---|---|---|
| `U-G1-01` | todavía no se conoce la clausura mínima del perfil | G2–G5, mediante preguntas, observables, consecuencias y atomicidad |
| `U-G1-02` | no se han fijado tratamientos o clases farmacológicas concretas | G2; sólo si la distinción cambia una pregunta clínica |
| `U-G1-03` | no se han fijado ventanas de validez por observable | G3-OBS |
| `U-G1-04` | no se han constituido vetos ni U críticas concretas | G4-CON y G5-ATM |

Estas incertidumbres no impiden definir la operación; impiden anticipar su contenido.

## 6. Dictamen

`OP-IMM-001` tiene sujeto, desencadenante, población, horizonte, autoridad, final y exclusiones suficientes para ser atacada externamente. No hereda matrices, parámetros ni umbrales.

**Resultado: `PASA_PARA_AUDITORIA_EXTERNA`.**

No se abre `G2-SEM` hasta dictamen externo favorable.
