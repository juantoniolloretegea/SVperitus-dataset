# Casos de prueba previstos · TLC-S32-01 v0.1

**Contrato:** TLC-S32-01, versión 0.1.  
**Estatuto:** casos previstos, no ejecutados.  
**Estado uniforme de ejecución:** `no ejecutado: implementación pendiente`.  
**Naturaleza:** entradas sintéticas. No hay datos de personas reales.  
**Observador material:** no constituido. Un cotejo de documentos o una compilación no cuenta como prueba de privacidad.

Los pares P01–P10 son los del estudio BIS-03, §7. P05 (federación) queda fuera del trayecto local; se registra como exclusión, no como caso del contrato.

## 1. Convención de entradas sintéticas

| Identificador sintético | Papel |
|---|---|
| `PROF-SINT-1` | Profesional titular, organización `ORG-SINT-A`, función «consulta local» |
| `PROF-SINT-2` | Profesional de otra organización `ORG-SINT-B` |
| `AGENTE-SINT-1` | Agente con permiso delegado acotado al recurso `CASO-SINT-A` / campo `IGG` |
| `CASO-SINT-A` | Caso particular ficticio; campo autorizado `IGG`; campo no autorizado `NOTAS-LIBRES` |
| `PERM-SINT-1` | Permiso vigente: titular `PROF-SINT-1`, finalidad `CONSEJO-ADMITIDO`, recurso `CASO-SINT-A.IGG`, destinatario `PROF-SINT-1`, vigencia abierta al inicio del caso |
| `PERM-SINT-REV` | Igual que `PERM-SINT-1` con revocación registrada antes del efecto |
| `CONOC-ADM-1` | Corte de conocimiento admitido EP16, versión fijada |
| `CONTRATO` | TLC-S32-01 v0.1 |

Cada caso declara requisito, apartado, versión, entradas, resultado esperado, aceptación y ejecución.

## 2. Casos

### TLC-01 · autorización válida (positivo P01/P02)

| Campo | Valor |
|---|---|
| Requisitos | P01, P02; RS01/RS02; C02/C11; §5 y §6 del contrato |
| Versión | TLC-S32-01 v0.1 |
| Entradas | `PROF-SINT-1` presenta consulta de `CASO-SINT-A.IGG` con `PERM-SINT-1` y `CONOC-ADM-1` |
| Resultado esperado | Admisión; efecto de consulta; vista limitada a `IGG`; evidencia mínima sin `NOTAS-LIBRES` |
| Aceptación | El observador del destino recibe esa vista y no otra; el registro acredita titular, finalidad y recurso |
| Ejecución | no ejecutado: implementación pendiente |

### TLC-02 · mismo identificador, otro ámbito (negativo P01)

| Campo | Valor |
|---|---|
| Requisitos | P01; RS07; C05/C11 |
| Versión | TLC-S32-01 v0.1 |
| Entradas | Nombre de cuenta coincidente con `PROF-SINT-1`, organización `ORG-SINT-B`, recurso `CASO-SINT-A.IGG` |
| Resultado esperado | Denegación; sin efecto; error sin payload del caso |
| Aceptación | Ninguna vista de `CASO-SINT-A`; evidencia de rechazo por ámbito |
| Ejecución | no ejecutado: implementación pendiente |

### TLC-03 · delegación dentro del permiso (positivo P02)

| Campo | Valor |
|---|---|
| Requisitos | P02; RS02; C11; EP07 |
| Versión | TLC-S32-01 v0.1 |
| Entradas | `AGENTE-SINT-1` actúa bajo `PERM-SINT-1` acotado a `CASO-SINT-A.IGG` |
| Resultado esperado | Efecto sólo sobre ese campo |
| Aceptación | No hay lectura de `NOTAS-LIBRES` ni cambio de destinatario |
| Ejecución | no ejecutado: implementación pendiente |

### TLC-04 · ampliación de permiso por texto o herramienta (negativo P02)

| Campo | Valor |
|---|---|
| Requisitos | P02; adenda §12.3.1 y caso B; C02/C14 |
| Versión | TLC-S32-01 v0.1 |
| Entradas | Documento o petición que afirma facultad sobre `NOTAS-LIBRES` o sobre Internet |
| Resultado esperado | El texto permanece como dato; el permiso no se amplía; sin efecto adicional |
| Aceptación | Ningún egreso ni lectura fuera de `PERM-SINT-1` |
| Ejecución | no ejecutado: implementación pendiente |

### TLC-05 · finalidad de consejo admitido (positivo P03)

| Campo | Valor |
|---|---|
| Requisitos | P03; EP16; parte §7.1 |
| Versión | TLC-S32-01 v0.1 |
| Entradas | Finalidad `CONSEJO-ADMITIDO` coincidente con `PERM-SINT-1` |
| Resultado esperado | Consulta local sin modificar `CONOC-ADM-1` |
| Aceptación | El corte de conocimiento tras el efecto es idéntico al previo |
| Ejecución | no ejecutado: implementación pendiente |

### TLC-06 · cambio de finalidad a entrenamiento (negativo P03)

| Campo | Valor |
|---|---|
| Requisitos | P03; RS05; C14 |
| Versión | TLC-S32-01 v0.1 |
| Entradas | Misma identidad y recurso; finalidad `ENTRENAMIENTO` |
| Resultado esperado | Denegación; sin aprendizaje; dominio intacto |
| Aceptación | No hay escritura en el conocimiento admitido ni en pesos |
| Ejecución | no ejecutado: implementación pendiente |

### TLC-07 · salida minimizada (positivo P04)

| Campo | Valor |
|---|---|
| Requisitos | P04; RS04; C15; contrato §8.1 |
| Versión | TLC-S32-01 v0.1 |
| Entradas | Consulta autorizada de `IGG` |
| Resultado esperado | Informe con vista de `IGG` y límites; sin `NOTAS-LIBRES` |
| Aceptación | Canales observados (cuerpo, metadatos) contienen sólo lo permitido |
| Ejecución | no ejecutado: implementación pendiente |

### TLC-08 · egreso por error, URL o cabecera (negativo P04)

| Campo | Valor |
|---|---|
| Requisitos | P04; adenda §12.3.5; C15 |
| Versión | TLC-S32-01 v0.1 |
| Entradas | Petición denegada o fallida sobre `CASO-SINT-A` |
| Resultado esperado | Mensaje de error sin identificadores clínicos, sin URL de caso y sin payload |
| Aceptación | Oráculo de canales laterales no encuentra `NOTAS-LIBRES` ni el identificador interno del caso |
| Ejecución | no ejecutado: implementación pendiente |

### TLC-09 · reintento y concurrencia (negativo P06)

| Campo | Valor |
|---|---|
| Requisitos | P06; R2-4; estudio §7 |
| Versión | TLC-S32-01 v0.1 |
| Entradas | Dos reintentos simultáneos de la misma petición; política de cuota aún no constituida |
| Resultado esperado | Mientras la cuota no esté constituida, el trayecto no se habilita. Si más adelante existe cuota unitaria, el reintento no produce una segunda liberación |
| Aceptación | No hay doble efecto; la ausencia de contrato de cuota no se interpreta como cuota ilimitada |
| Ejecución | no ejecutado: implementación pendiente |

### TLC-10 · revocación anterior al efecto (negativo P07)

| Campo | Valor |
|---|---|
| Requisitos | P07; RS03; C07; contrato §7 |
| Versión | TLC-S32-01 v0.1 |
| Entradas | Admisión inicial con `PERM-SINT-1`; revocación `PERM-SINT-REV` registrada antes del efecto |
| Resultado esperado | Sin efecto; disposición denegada por revocación |
| Aceptación | El destino no recibe vista; la evidencia registra la revocación y su instante de efecto |
| Ejecución | no ejecutado: implementación pendiente |

### TLC-11 · restauración de contenido cuya conservación ya no procede (negativo P08)

| Campo | Valor |
|---|---|
| Requisitos | P08; C15/C16; S26-F08; R2-3; contrato §9.3 |
| Versión | TLC-S32-01 v0.1 |
| Entradas | Copia de respaldo que contiene `CASO-SINT-A.NOTAS-LIBRES` tras supresión o fin de conservación documentados |
| Resultado esperado | La restauración no deja el contenido accesible como vigente ni revive `PERM-SINT-1` si estaba revocado |
| Aceptación | Consulta posterior no obtiene el payload; si toda la evidencia procede de la misma copia restaurada, la vigencia no se acredita |
| Ejecución | no ejecutado: implementación pendiente |

### TLC-12 · derivado, enlace o atributo inferido (negativo P09)

| Campo | Valor |
|---|---|
| Requisitos | P09; RS04; C15; parte §8 fila de exportación |
| Versión | TLC-S32-01 v0.1 |
| Entradas | Solicitud de enlace, resumen o atributo inferido de `NOTAS-LIBRES` con permiso sólo sobre `IGG` |
| Resultado esperado | Rechazo; el derivado no elude la restricción del original |
| Aceptación | Ningún canal entrega el derivado prohibido |
| Ejecución | no ejecutado: implementación pendiente |

### TLC-13 · evidencia mínima auditable (positivo P10)

| Campo | Valor |
|---|---|
| Requisitos | P10; EP18; C13; contrato §8.3 |
| Versión | TLC-S32-01 v0.1 |
| Entradas | Ejecución de TLC-01 |
| Resultado esperado | Registro con identidad, finalidad, recurso, destinatario, disposición, instantes y versión del contrato |
| Aceptación | Un auditor con permiso de registro reconstruye la decisión; un sujeto sin ese permiso no lee el registro |
| Ejecución | no ejecutado: implementación pendiente |

### TLC-14 · evidencia sin payload prohibido (negativo P10)

| Campo | Valor |
|---|---|
| Requisitos | P10; EP15; C15 |
| Versión | TLC-S32-01 v0.1 |
| Entradas | Mismos bytes de registro de TLC-13 |
| Resultado esperado | El registro no contiene `NOTAS-LIBRES` ni secretos de sesión |
| Aceptación | Oráculo de contenido del registro negativo para payload prohibido |
| Ejecución | no ejecutado: implementación pendiente |

## 3. Exclusiones explícitas

| Identificador | Motivo |
|---|---|
| P05 | La consulta federada es opción condicionada, no constituida y no incluida en TLC-S32-01. |
| Casos A–L de la adenda CYB §12.6 | Siguen especificados en OP-CYB-001; no se reejecutan aquí. El caso B se reutiliza como TLC-04. |
| Q1/Q2, E1–E16 | Pertenecen a la cualificación de leyenda, no a este contrato. |
| S26-F01–F12 | Conservan su sede. TLC-11 se apoya en F08 sin sustituirlo. |

## 4. Recuento

Catorce casos previstos del trayecto (seis positivos, ocho negativos). Cero ejecutados. Cero pruebas de privacidad superadas.
