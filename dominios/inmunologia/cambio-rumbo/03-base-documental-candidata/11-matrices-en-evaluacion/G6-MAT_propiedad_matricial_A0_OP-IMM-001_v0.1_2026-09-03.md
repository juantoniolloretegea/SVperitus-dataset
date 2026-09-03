# G6-MAT — propiedad matricial total y única de A0 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Base exacta:** `b1020aa7c722edaa9a549e614eab0eaf1497d902`
- **Operación:** `OP-IMM-001`
- **Entrada:** `A0 v0.1`, 27 parámetros
- **Puerta:** `G6-MAT`
- **Estatuto:** `PROPIEDAD_MATRICIAL_CERRADA`
- **Efecto clínico:** ninguno

## 1. Regla

Se aplica `owner_v : A0 -> M_v` con un propietario exacto por parámetro. Las matrices se derivan de función y dependencia; no de dimensiones históricas. No se resume ningún vector por mayoría, suma, promedio o puntuación.

## 2. Matrices propietarias

| Matriz_ID | Finalidad propia | Parámetros |
|---|---|---|
| `M-CTX-AUTH-001` | contexto temporal, nosológico, asistencial e institucional del episodio | 6 |
| `M-EXP-001` | exposición inmunosupresora propuesta ya constituida | 1 |
| `M-HOST-001` | estado inmunitario del huésped | 3 |
| `M-BARRIER-001` | barreras materiales y biomateriales | 2 |
| `M-HISTORY-001` | historia infecciosa y exposición sanitaria | 6 |
| `M-MODIFIER-001` | comorbilidad, reserva y modificadores generales | 9 |
| **Total** |  | **27** |

## 3. Función de propiedad completa

| Parámetro_ID | Matriz propietaria |
|---|---|
| `PAR-IMMUNO-START-PLAN-DOC-001` | `M-CTX-AUTH-001` |
| `PAR-BASE-DX-DOC-001` | `M-CTX-AUTH-001` |
| `PAR-EPISODE-LEAD-DOC-001` | `M-CTX-AUTH-001` |
| `PAR-IMMUNO-PART-DOC-001` | `M-CTX-AUTH-001` |
| `PAR-LOCAL-PROTOCOL-APPLICABLE-001` | `M-CTX-AUTH-001` |
| `PAR-EXEC-CONSTRAINT-DOC-001` | `M-CTX-AUTH-001` |
| `PAR-GC-PLAN-SYS-001` | `M-EXP-001` |
| `PAR-IGG-DEF-Q-001` | `M-HOST-001` |
| `PAR-SPL-ANAT-ABS-001` | `M-HOST-001` |
| `PAR-ANC-DEF-Q-001` | `M-HOST-001` |
| `PAR-IV-DEVICE-PRESENT-001` | `M-BARRIER-001` |
| `PAR-IMPLANT-PRESENT-001` | `M-BARRIER-001` |
| `PAR-INF-HOSP-HIST-001` | `M-HISTORY-001` |
| `PAR-INF-ORGSUP-HIST-001` | `M-HISTORY-001` |
| `PAR-OI-DOC-HIST-001` | `M-HISTORY-001` |
| `PAR-MDRO-COL-DOC-001` | `M-HISTORY-001` |
| `PAR-ACUTECARE-ENC-HIST-001` | `M-HISTORY-001` |
| `PAR-INV-PROC-HIST-001` | `M-HISTORY-001` |
| `PAR-DM-DOC-ACTIVE-001` | `M-MODIFIER-001` |
| `PAR-HF-DOC-ACTIVE-001` | `M-MODIFIER-001` |
| `PAR-CKD-DOC-ACTIVE-001` | `M-MODIFIER-001` |
| `PAR-KRT-ACTIVE-001` | `M-MODIFIER-001` |
| `PAR-BRONCHIECTASIS-DOC-ACTIVE-001` | `M-MODIFIER-001` |
| `PAR-RESP-SUPPORT-ACTIVE-001` | `M-MODIFIER-001` |
| `PAR-CIRRHOSIS-DOC-ACTIVE-001` | `M-MODIFIER-001` |
| `PAR-MALNUTRITION-ASSESS-POS-001` | `M-MODIFIER-001` |
| `PAR-FRAILTY-ASSESS-POS-001` | `M-MODIFIER-001` |

## 4. Referencias cruzadas sin duplicación

| Referencia_ID | Origen | Destino | Función |
|---|---|---|---|
| `REF-START-EXP-001` | `PAR-IMMUNO-START-PLAN-DOC-001` | `M-EXP-001` | punto índice de vigencia; no duplica estado |
| `REF-KRT-HOST-001` | `PAR-KRT-ACTIVE-001` | `M-HOST-001` | contexto de interpretación renal; no representa inmunidad |
| `REF-RESP-HISTORY-001` | `PAR-RESP-SUPPORT-ACTIVE-001` | `M-HISTORY-001` | consecuencia/reserva; no equivale a infección previa |
| `REF-PROTOCOL-ALL-001` | `PAR-LOCAL-PROTOCOL-APPLICABLE-001` | composición | restricción institucional; no altera estados clínicos |

Una referencia sólo lee el estado canónico y conserva su `U`. No existe recálculo en destino.

## 5. Vectores primarios

```text
S(M-CTX-AUTH-001) = (s21,s22,s23,s24,s25,s26)
S(M-EXP-001) = (s1)
S(M-HOST-001) = (s2,s3,s4)
S(M-BARRIER-001) = (s5,s6)
S(M-HISTORY-001) = (s7,s8,s9,s10,s11,s12)
S(M-MODIFIER-001) = (s13,s14,s15,s16,s17,s18,s19,s20,s27)
```

Cada `s_i ∈ {0,1,U}`. No existe salida resumida `g_i` en G6.

## 6. Controles fuera de A0

`SEM-RUT-001` permanece control de salida y la edad en fecha índice, operando contextual. No son celdas de relleno ni parámetros encubiertos.

## 7. Configuración pendiente

Los parámetros OI, MDRO, nutrición y fragilidad conservan propietario, aunque su capacidad automática de `0/1` esté bloqueada. Propiedad no equivale a ejecutabilidad. Sus estados de episodio serán `U_CONFIGURACION_NO_ADMITIDA` hasta que exista paquete registrado.

## 8. Adversarial integrada

- Duplicar CKD dentro de huésped: rechazado; se usa referencia.
- Fusionar CKD y KRT: rechazado; pueden divergir.
- Doble contabilizar CKD+KRT: no existe suma ni puntuación.
- Fusionar bronquiectasias y soporte: rechazado.
- Incluir edad para completar dimensión: rechazado.
- Convertir seis matrices en `SV(36,6)`: rechazado; 27 no es 36 y no se rellena.
- Hacer matriz de una pregunta o consecuencia: rechazado.
- Dar dos propietarios a un parámetro: rechazado.
- Tratar configuración pendiente como ausencia del parámetro: rechazado.
- Ocultar `U` en un resumen: no existe resumen en esta puerta.

```text
DOMINIO(owner_v) = A0
|DOMINIO(owner_v)| = 27
PROPIETARIOS_ASIGNADOS = 27
DUPLICADOS = 0
SIN_PROPIETARIO = 0
MATRICES = 6
G6-MAT = CERRADA
G7-RUT = NO_ABIERTA
```
