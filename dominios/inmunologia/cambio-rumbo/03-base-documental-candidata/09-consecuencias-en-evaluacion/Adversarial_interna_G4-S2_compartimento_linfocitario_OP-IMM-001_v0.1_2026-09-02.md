# Adversarial interna — `G4-S2` consecuencias de errores sobre cuantificación linfocitaria v0.1

- **Fecha:** 02-09-2026
- **Objeto:** `Lote_consecuencias_G4-S2_compartimento_linfocitario_OP-IMM-001_v0.1_2026-09-02.md`
- **Estatuto:** `ADVERSARIAL_INTERNA_NO_SUSTITUYE_AUDITORIA_EXTERNA`

## 1. Ataque de causalidad

**Contraejemplo:** la asociación observada se presenta como prueba de que la linfopenia causa una infección individual.

**Resultado:** no prospera. `CON-LYM-INF-001` conserva diseño observacional, población, confusión residual y la negación expresa de causalidad de la fuente.

## 2. Ataque de umbral universal

**Contraejemplo:** el punto de corte del estudio se adopta como definición universal de alteración.

**Resultado:** no prospera. El lote prohíbe importar el umbral, el intervalo y el algoritmo predictivo.

## 3. Ataque de transporte

**Contraejemplo:** una cohorte general danesa gobierna automáticamente a una persona bajo inmunosupresión, otra edad o población.

**Resultado:** no prospera. La salida máxima es asociación poblacional pendiente de regla; población y modificadores permanecen abiertos.

## 4. Ataque total–subpoblación

**Contraejemplo:** total normal borra una subpoblación baja, o una subpoblación sustituye al total.

**Resultado:** no prospera. `CON-LYM-ID-001` exige identidad y definición separadas.

## 5. Ataque absoluto–proporción

**Contraejemplo:** porcentaje y número absoluto se intercambian o uno se calcula sin todos los inputs.

**Resultado:** no prospera. `CON-LYM-MAG-001` conserva magnitud, unidad y método y produce `U` o rechazo.

## 6. Ataque cantidad–función

**Contraejemplo:** un recuento normal prueba competencia funcional o un recuento bajo prueba ausencia de función.

**Resultado:** no prospera. `CON-LYM-FUN-001` sólo permite `FUNCION_NO_CONSTITUIDA`.

## 7. Ataque temporal

**Contraejemplo:** un resultado antiguo se presenta como actual o dos puntos forman una tendencia causal.

**Resultado:** no prospera. `CON-LYM-TIME-001` separa muestra, instante, calidad, referencia y serie descriptiva.

## 8. Ataque de referencia local

**Contraejemplo:** el intervalo de un laboratorio, método o población se impone a otro.

**Resultado:** no prospera. La incompatibilidad produce `U(REFERENCIA)`; CLSI no sostiene intervalos generales.

## 9. Ataque de doble daño

**Contraejemplo:** todo dato ausente se declara daño clínico consumado.

**Resultado:** no prospera. Cuatro consecuencias son epistemológicas; la quinta sólo es asociación clínica potencial no causal y exige una medición válida y una futura regla.

## 10. Ataque de falso positivo ignorado

**Contraejemplo:** sólo se considera omitir una alteración y se ignora el daño de individualizar indebidamente una asociación.

**Resultado:** no prospera. `CON-LYM-INF-001` tiene dos direcciones: omisión y certeza fabricada.

## 11. Ataque de fuente decorativa

**Contraejemplo:** se formula el consejo y después se añade Warny et al. como cita.

**Resultado:** no prospera. La cadena exige fuente, localizador, población, diseño y límites antes de concluir.

## 12. Ataque de expansión clínica

**Contraejemplo:** el lote prescribe pruebas, intervención, seguimiento o derivación.

**Resultado:** no prospera. Todo ello está en residuos; el lote no define ninguna actuación.

## 13. Ataque de sesgo vacunal

**Contraejemplo:** el documento vuelve a usar vacunación como finalidad dominante.

**Resultado:** no prospera. Las cinco consecuencias son no vacunales; la fuente CDC sólo sostiene una distinción general entre cantidad, subpoblación y función.

## 14. Ataque de compensación

**Contraejemplo:** coste, tiempo o disponibilidad compensan una `U` clínica grave.

**Resultado:** no prospera. No crean causalidad ni cierran incertidumbre.

## 15. Ataque de determinismo y fallo

**Contraejemplo:** cambia el orden o la redacción de la salida con entradas idénticas; un fallo produce otra conclusión plausible.

**Resultado:** no prospera por contrato. La serialización debe coincidir byte a byte; el fallo sólo produce `EJECUCION_TECNICA_NO_VALIDA`.

## 16. Ataque de privacidad

**Contraejemplo:** un episodio o centro real se reutiliza para demostrar la asociación.

**Resultado:** no prospera. Los objetos son impersonales y no requieren datos atribuibles.

## 17. Recuentos internos

| Control | Esperado | Contado |
|---|---:|---:|
| consecuencias | 5 | 5 |
| epistemológicas | 4 | 4 |
| asociaciones clínicas potenciales no causales | 1 | 1 |
| fuentes externas | 3 | 3 |
| umbrales adoptados | 0 | 0 |
| diagnósticos o intervenciones | 0 | 0 |
| parámetros atómicos | 0 | 0 |
| matrices, rutas o frames | 0 | 0 |

## 18. Dictamen interno

`LISTA_PARA_AUDITORIA_EXTERNA`, no `G4-S2_CERRADO`.

La auditoría externa debe intentar falsar especialmente la frontera asociación–causalidad, el transporte desde población general, la separación cantidad–función y la doble dirección de `CON-LYM-INF-001`.
