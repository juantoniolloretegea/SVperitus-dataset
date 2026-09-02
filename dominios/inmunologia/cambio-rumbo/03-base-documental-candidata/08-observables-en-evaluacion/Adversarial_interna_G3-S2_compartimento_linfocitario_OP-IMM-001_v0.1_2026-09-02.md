# Adversarial interna — `G3-S2` cuantificación del compartimento linfocitario v0.1

- **Fecha:** 02-09-2026
- **Objeto:** `Lote_observacional_G3-S2_compartimento_linfocitario_OP-IMM-001_v0.1_2026-09-02.md`
- **Estatuto:** `ADVERSARIAL_INTERNA_NO_SUSTITUYE_AUDITORIA_EXTERNA`

## 1. Ataque de sesgo vacunal

**Contraejemplo:** usar el contexto vacunal de una fuente para introducir una decisión de vacunación.

**Resultado:** no prospera. Sólo se usa la separación general entre número, subpoblación y función. El lote no contiene vacuna, pauta o consecuencia vacunal.

## 2. Ataque de escalar único

**Contraejemplo:** representar «estado linfocitario» mediante un único número.

**Resultado:** no prospera. `E_LYM_Q` exige población, definición, tipo de magnitud, unidad, tiempo y método.

## 3. Ataque total frente a subpoblación

**Contraejemplo:** un recuento linfocitario total normal cierra como normales todas las subpoblaciones.

**Resultado:** no prospera. Cada población tiene una medición distinta y `OBS-LYM-003` prohíbe la sustitución.

## 4. Ataque absoluto frente a porcentaje

**Contraejemplo:** dos muestras tienen el mismo porcentaje y distinto número absoluto; el sistema las declara equivalentes.

**Resultado:** no prospera. `OBS-LYM-005` separa tipos de magnitud y `N_LYM_PAIR` conserva ambos sin inferir equivalencia.

## 5. Ataque cuantitativo frente a funcional

**Contraejemplo:** una cifra dentro del intervalo de referencia se presenta como función inmunitaria competente.

**Resultado:** no prospera. Los ensayos funcionales están excluidos y una medición cuantitativa no los sustituye.

## 6. Ataque de definición de población

**Contraejemplo:** dos laboratorios usan la misma etiqueta pero definiciones o marcadores distintos y sus resultados se fusionan.

**Resultado:** no prospera. `OBS-LYM-004` conserva la definición y `C_DEFINICION_POBLACION` detiene la equivalencia no demostrada.

## 7. Ataque de método invisible

**Contraejemplo:** un valor directo y uno calculado desde dos plataformas se tratan como el mismo dato sin declarar inputs.

**Resultado:** no prospera. `OBS-LYM-008` y `C_METODO` exigen conservar base y dependencia de cálculo.

## 8. Ataque de tiempo

**Contraejemplo:** fecha de informe sustituye a fecha de muestra o un resultado antiguo se presenta como vigente.

**Resultado:** no prospera. `OBS-LYM-002` identifica el instante de muestra; la vigencia todavía no está constituida.

## 9. Ataque de calidad

**Contraejemplo:** un número marcado como no válido alimenta una futura regla.

**Resultado:** no prospera. `OBS-LYM-009` y `C_CALIDAD` lo detienen.

## 10. Ataque de referencia universal

**Contraejemplo:** aplicar automáticamente el intervalo de un laboratorio, edad, población o versión a otra medición.

**Resultado:** no prospera. `N_LYM_REF` exige compatibilidad y no clasifica por sí solo.

## 11. Ataque de trayectoria inventada

**Contraejemplo:** dos puntos se convierten en tendencia, causa o pronóstico.

**Resultado:** no prospera. `N_LYM_SERIES` sólo ordena; no interpola ni interpreta.

## 12. Ataque de `U` opaca

**Contraejemplo:** «resultado desconocido» sin indicar campo, causa o fuentes discordantes.

**Resultado:** no prospera. `U_LYM` exige campo, código, fuentes, horizonte y versión, con doce causas diferenciadas.

## 13. Ataque de atomización prematura

**Contraejemplo:** convertir uno de los diez observables en parámetro atómico por ser técnicamente pequeño.

**Resultado:** no prospera. El lote declara cero parámetros; tamaño de campo no prueba indivisibilidad clínica.

## 14. Ataque de determinismo y fallo

**Contraejemplo:** el orden de llegada cambia la serie o un fallo técnico produce un valor alternativo.

**Resultado:** no prospera por contrato. La orden canónica usa tiempo y procedencia; el fallo sólo produce `EJECUCION_TECNICA_NO_VALIDA`.

## 15. Ataque de privacidad

**Contraejemplo:** incorporar un informe real o datos de un centro para demostrar el esquema.

**Resultado:** no prospera. El lote es impersonal y no necesita registros atribuibles.

## 16. Recuentos internos

| Control | Esperado | Contado |
|---|---:|---:|
| preguntas G2 | 1 | 1 |
| fuentes | 3 | 3 |
| entidades | 1 | 1 |
| observables | 10 | 10 |
| normalizadores previos | 4 | 4 |
| causas de `U` | 12 | 12 |
| umbrales o diagnósticos | 0 | 0 |
| parámetros atómicos | 0 | 0 |
| matrices, rutas o frames | 0 | 0 |

## 17. Dictamen interno

`LISTA_PARA_AUDITORIA_EXTERNA`, no `G3-S2_CERRADO`.

La auditoría externa debe intentar falsar las separaciones con resultados absolutos y porcentuales discordantes, poblaciones homónimas definidas de modo distinto, mediciones directas y calculadas y referencias incompatibles.
