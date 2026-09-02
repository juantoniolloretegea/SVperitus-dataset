# Operación clínica testigo en evaluación

Este directorio contiene la primera ejecución de `G1-OP`, puerta de definición de una operación clínica finita. Su base rectora es la compuerta `NA0` v0.2.

## Estado

- Una sola operación candidata: `OP-IMM-001`.
- Auditoría externa v0.1: `PASA` con un reparo menor de precisión.
- Reparación v0.2: `R-01` incorporado; `G1-OP` cerrada para abrir exclusivamente `G2-SEM`.
- Cero parámetros adjudicados.
- Cero consecuencias clínicas plenas.
- Cero matrices, composiciones o rutas constituidas.
- Cero búsquedas de cohortes.
- Cero modificaciones del Lenguaje SV.

La operación no avanza a `G2-SEM` hasta superar adversarial externa.

## Objetos

- `OP-IMM-001_constitucion_perfil_riesgo_infeccioso_preinmunosupresion_G1_v0.1_2026-09-02.md`
- `Adversarial_interna_G1_OP-IMM-001_v0.1_2026-09-02.md`
- `Orden_auditoria_externa_G1_OP-IMM-001_v0.1_2026-09-02.md`
- `Recepcion_auditoria_externa_G1_OP-IMM-001_v0.1_Claude_2026-09-02.md`
- `OP-IMM-001_constitucion_perfil_riesgo_infeccioso_preinmunosupresion_G1_v0.2_2026-09-02.md`
- `Adversarial_interna_reparacion_y_cierre_G1_OP-IMM-001_v0.2_2026-09-02.md`

## Glosario

| Forma | Significado |
|---|---|
| G1-OP | Puerta 1 de definición de la operación clínica. |
| G2-SEM | Puerta 2 de formulación semántica de preguntas candidatas. |
| NA0 | Compuerta cero de normalización atómica. |
| SV | Sistema Vectorial SV. |
| U | Estado indeterminado legítimo. |
