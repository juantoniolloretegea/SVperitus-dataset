# Adversarial interna — `G4-S1` consecuencias de errores sobre glucocorticoides v0.1

- **Fecha:** 02-09-2026
- **Objeto:** `Lote_consecuencias_G4-S1_corticoides_OP-IMM-001_v0.1_2026-09-02.md`
- **Estatuto:** `ADVERSARIAL_INTERNA_NO_SUSTITUYE_AUDITORIA_EXTERNA`

## 1. Hipótesis de falsación

El lote falla si convierte prudencia verbal en prueba, si salta del dato ausente al daño clínico, si adopta una regla de decisión encubierta o si amplía el dominio para completar una historia clínica imaginada.

## 2. Ataque A — cierre G3 inexistente

**Contraejemplo:** abrir consecuencias sobre observables que todavía no hubieran superado auditoría.

**Resultado:** no prospera. La recepción fija `G3-S1_CERRADO`, conserva las dos identidades auditadas y no altera los objetos primarios.

## 3. Ataque B — consecuencia como sinónimo de error

**Contraejemplo:** afirmar que una pauta mal registrada ya produjo infección o fracaso vacunal.

**Resultado:** no prospera. `CON-GC-REP-001` constituye sólo daño epistemológico. Las consecuencias clínicas exigen finalidad y fuente propias.

## 4. Ataque C — salto causal

**Contraejemplo:** convertir una exposición desconocida en certeza de complicación grave.

**Resultado:** no prospera. Las consecuencias clínicas son potenciales, conservan condiciones abiertas y no predicen causalidad individual.

## 5. Ataque D — fusión de seguridad y efectividad

**Contraejemplo:** usar una posible respuesta vacunal subóptima como prueba de inseguridad de una vacuna no viva, o usar seguridad como prueba de efectividad.

**Resultado:** no prospera. `CON-GC-VAC-SAF-001` y `CON-GC-VAC-EFF-001` tienen finalidad, daño y límites distintos.

## 6. Ataque E — umbral universal encubierto

**Contraejemplo:** importar el umbral del apartado CDC sobre vacunas vivas para decidir profilaxis de PJP.

**Resultado:** no prospera. `CON-GC-PUR-001` identifica precisamente ese traslado como error; `CON-GC-PJP-001` mantiene abiertas magnitud, duración y modificadores.

## 7. Ataque F — DDD o equivalencia como regla clínica

**Contraejemplo:** usar una dosis diaria definida o una tabla recordada de prednisona-equivalente para cerrar `U`.

**Resultado:** no prospera. El lote no contiene ninguna tabla de conversión y exige `U(EQUIVALENCIA)` si faltan versión, finalidad y procedencia.

## 8. Ataque G — profilaxis implícita

**Contraejemplo:** leer `CON-GC-PJP-001` como indicación automática de profilaxis.

**Resultado:** no prospera. La consecuencia es omitir la valoración cuando corresponda; no adopta medicamento, dosis, umbral, duración ni decisión.

## 9. Ataque H — gravedad compensable

**Contraejemplo:** neutralizar `ALTA_POTENCIAL` mediante ahorro, disponibilidad o conveniencia institucional.

**Resultado:** no prospera. La criticidad con un eslabón en `U` no se declara ausente ni se compensa. Costes y organización permanecen fuera del corte.

## 10. Ataque I — falso positivo ignorado

**Contraejemplo:** interpretar que sólo los falsos negativos pueden causar daño.

**Resultado:** no prospera. `CON-GC-REP-001` y `CON-GC-PUR-001` declaran ambas direcciones. El lote no inventa una intervención ni toxicidad para completar el falso positivo.

## 11. Ataque J — fuente decorativa

**Contraejemplo:** formular primero la consecuencia y añadir una URL genérica después.

**Resultado:** no prospera. Cada consecuencia clínica identifica fuente, localizador, finalidad y transición; §7 exige su serialización antes de la conclusión.

## 12. Ataque K — fuente que no sostiene la fuerza afirmada

**Contraejemplo:** afirmar incidencia universal de PJP o certeza de complicación vacunal a partir de páginas que sólo describen posibilidad y contexto.

**Resultado:** no prospera en el texto. No se ofrecen tasas universales; se usa `potencial`, se conservan condiciones abiertas y la gravedad no es probabilidad.

## 13. Ataque L — expansión infinita

**Contraejemplo:** incorporar toxicidad de profilaxis, todos los efectos adversos de glucocorticoides y toda organización hospitalaria por ser asuntos relevantes.

**Resultado:** no prospera. §9 enumera esos residuos y exige otra dependencia semántica para abrirlos. El lote termina en cinco consecuencias.

## 14. Ataque M — determinismo nominal

**Contraejemplo:** dos ejecuciones con la misma entrada producen cadenas, orden o consecuencias diferentes y ambas se aceptan.

**Resultado:** no prospera por contrato. §8 exige identidad byte a byte; el fallo produce `EJECUCION_TECNICA_NO_VALIDA`. La implementación futura deberá demostrarlo materialmente.

## 15. Ataque N — privacidad

**Contraejemplo:** usar un episodio real o el nombre de un centro para ilustrar la consecuencia.

**Resultado:** no prospera. Los objetos son impersonales y el lote no necesita ejemplos de pacientes para constituir sus clases.

## 16. Ataque O — atomización prematura

**Contraejemplo:** convertir una consecuencia en parámetro, propietario de matriz, ruta o frame.

**Resultado:** no prospera. Todos esos objetos permanecen en cero y `G5-ATM` sigue cerrada.

## 17. Recuentos internos

| Control | Esperado | Contado |
|---|---:|---:|
| consecuencias candidatas | 5 | 5 |
| epistemológicas | 2 | 2 |
| clínicas potenciales | 3 | 3 |
| fuentes clínicas | 3 | 3 |
| umbrales adoptados | 0 | 0 |
| equivalencias adoptadas | 0 | 0 |
| intervenciones prescritas | 0 | 0 |
| parámetros atómicos | 0 | 0 |
| matrices, rutas o frames | 0 | 0 |

## 18. Dictamen interno

`LISTA_PARA_AUDITORIA_EXTERNA`, no `G4-S1_CERRADO`.

La prueba externa deberá abrir las fuentes, intentar falsar cada cadena y decidir si el lote conserva la diferencia entre error, daño epistemológico, finalidad y consecuencia clínica potencial.
