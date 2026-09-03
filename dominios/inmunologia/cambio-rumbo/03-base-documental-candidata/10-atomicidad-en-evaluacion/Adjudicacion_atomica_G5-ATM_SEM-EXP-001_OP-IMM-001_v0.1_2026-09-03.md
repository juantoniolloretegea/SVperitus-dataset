# Adjudicación atómica G5-ATM — SEM-EXP-001 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Puerta:** `G5-ATM/SEM-EXP-001`
- **Operación:** `OP-IMM-001`
- **Raíz:** `SEM-EXP-001`
- **Base exacta:** `be7ba51716cd8dd01838ebdb136640381cd9b51d`
- **Contrato:** `NA0-MATH` v0.3
- **Manifiesto de terminación:** `OP-IMM-001 / Q0 v0`, 03-09-2026
- **Estatuto:** `ADJUDICACION_ATOMICA_CERRADA_COMO_PUENTE_CONSTITUTIVO_COMPUESTO`
- **Efecto clínico:** ninguno
- **Autorización asistencial:** ninguna

## 0. Objeto y dictamen nuclear

Se adjudica la raíz:

> `SEM-EXP-001`: ¿Está identificado el tratamiento inmunosupresor sistémico primario propuesto?

La expresión «tratamiento identificado» no designa una magnitud clínica ni una proposición atómica única. Resume una conjunción de identidad farmacológica, cobertura, versión, papel, estado y clasificación. Estas dimensiones pueden variar, fallar y producir consecuencias distintas.

El resultado positivo de esta puerta es un puente constitutivo que entrega a las raíces posteriores un objeto terapéutico explícito, versionado y trazado:

```text
BRG-TXP-PRIMARY-001
```

El puente no entra en `A0`, no emite riesgo y no autoriza una intervención. Su función es impedir que una pregunta clínica opere sobre un tratamiento supuesto, híbrido o inferido.

La adversarial está integrada. No se crea orden, recepción ni documento auxiliar.

## 1. Dependencias cerradas

La adjudicación recibe:

- `G3-OBS/SEM-EXP-001`: `E_TX_PRIMARY`, dieciséis observables, cuatro normalizadores y dieciséis causas de `U`;
- `G4-CON/SEM-EXP-001`: seis consecuencias separadas para identidad, cobertura, versión, papel, estado y clasificación;
- `NA0-MATH` v0.3;
- y el universo finito `Q0 v0`.

Ninguna dependencia convierte propuesta en administración, clasificación en indicación o trazabilidad en validez clínica.

## 2. Clasificación del material observacional

| Objeto | Tipo adjudicado | Función |
|---|---|---|
| `Propuesta_ID` | `CONTROL_IDENTITARIO` | mantiene unido el episodio documental |
| `Version_propuesta` | `CONTROL_DE_CONFIGURACION` | evita mezclar versiones |
| `Estado_propuesta` | `CONTROL_DOCUMENTAL` | separa borrador, propuesta, orden, cancelación y sustitución |
| `Intencion_documental` | `CONTROL_DE_INTENCION` | impide convertir plan en suceso |
| `Instante_de_corte` | `CONTEXTO_TEMPORAL` | fija la versión evaluable |
| `Regimen_completo_declarado` | `CONTROL_DE_COBERTURA` | permite distinguir ausencia de silencio |
| `Componente_ID` | `CONTROL_IDENTITARIO_LOCAL` | conserva componentes sin fusión |
| `Sustancias_activas_declaradas` | `OBSERVABLE_IDENTITARIO` | identifica la composición declarada |
| `Producto_o_preparacion` | `CONTEXTO_FARMACEUTICO` | conserva el producto sin sustituir a la sustancia |
| `Forma_farmaceutica` | `CONTEXTO_FARMACEUTICO` | condiciona la interpretación de identidad y vía |
| `Via_planificada` | `CONTEXTO_DE_CLASIFICACION` | permite evaluar el carácter sistémico |
| `Papel_en_regimen` | `CONTROL_DE_PAPEL` | conserva primario, concomitante, puente o pluralidad declarada |
| `Clasificacion_sistemica_declarada` | `CONTROL_CLINICO_VERSIONADO` | exige regla y autoridad para «sistémico» |
| `Clasificacion_inmunosupresora_declarada` | `CONTROL_CLINICO_VERSIONADO` | exige regla, finalidad y autoridad |
| `Autoridad_de_propuesta` | `CONTROL_DE_AUTORIDAD` | determina quién puede declarar la propuesta y su papel |
| `Vigencia` | `CONTROL_TEMPORAL_Y_DOCUMENTAL` | excluye propuestas sustituidas o canceladas |
| `Procedencia_por_campo` | `CONTROL_DE_TRAZABILIDAD` | sitúa evidencia antes de la salida |

Los cuatro normalizadores de G3 siguen siendo funciones técnicas. Ningún campo se convierte automáticamente en parámetro.

## 3. Prueba de atomicidad de la raíz

### 3.1. Estado único

Una propuesta puede tener sustancia identificada y carecer de cobertura; ser vigente y no tener papel primario declarado; o tener papel declarado sin clasificación sistémica suficientemente constituida.

**Resultado:** la raíz no admite un único estado sin ocultar diferencias materiales.

### 3.2. `U` propia

Las seis familias de `U` son independientes. Resolver identidad no resuelve versión; resolver papel no demuestra vigencia; resolver una clasificación no completa el régimen.

**Resultado:** una `U` agregada sería opaca e impediría reparar sólo la dependencia afectada.

### 3.3. Consecuencias separables

`CON-TXP-ID-001`, `CON-TXP-COV-001`, `CON-TXP-VER-001`, `CON-TXP-ROLE-001`, `CON-TXP-STATE-001` y `CON-TXP-CLASS-001` muestran daños epistemológicos y contaminaciones operacionales diferentes.

**Resultado:** la separación es obligatoria.

### 3.4. Función

La raíz no clasifica una propiedad del paciente ni de la exposición ejecutada. Constituye la referencia terapéutica sobre la que otras raíces preguntarán magnitud, duración, situación del huésped, evidencia y consecuencias.

**Resultado:** su tipo correcto es puente constitutivo, no parámetro clínico de `A0`.

### 3.5. Ablación

Eliminar el puente no elimina una magnitud clínica, pero permite que raíces posteriores seleccionen tratamientos por texto libre, orden de llegada o memoria del modelo.

**Resultado:** el objeto es necesario como dependencia gobernada, sin adquirir por ello estatuto de parámetro.

## 4. Partición finita y terminal

La raíz se descompone una sola vez según las seis consecuencias ya cerradas:

| Control terminal | Pregunta exacta | Salida |
|---|---|---|
| `CTL-TXP-ID-001` | ¿Están identificados sin fusión los componentes, sustancias, producto, forma y vía? | `SATISFECHO | U_IDENTIDAD_TRATAMIENTO` |
| `CTL-TXP-COV-001` | ¿La cobertura del régimen está declarada para esta versión? | `COMPLETO | PARCIAL | CONDICIONADO | U_COBERTURA_REGIMEN` |
| `CTL-TXP-VER-001` | ¿La versión y sus enlaces de sustitución están constituidos? | `SATISFECHO | U_VERSION_PROPUESTA` |
| `CTL-TXP-ROLE-001` | ¿El papel primario o la pluralidad primaria proceden de autoridad competente? | `PRIMARIO_DECLARADO | MULTIPLES_PRIMARIOS_DECLARADOS | SIN_PRIMARIO_DECLARADO | U_PAPEL_PRIMARIO` |
| `CTL-TXP-STATE-001` | ¿Estado, intención y vigencia permanecen separados y son aplicables al corte? | `SATISFECHO | U_ESTADO_O_VIGENCIA` |
| `CTL-TXP-CLASS-001` | ¿Las clasificaciones sistémica e inmunosupresora tienen regla, finalidad, versión y autoridad? | `SATISFECHO | U_CLASIFICACION_CLINICA` |

Son controles terminales del puente, no nuevas raíces de `Q0` ni posiciones de `A0`. No se subdividen en esta versión: sus campos son datos, contexto o procedencia ya enumerados en G3.

## 5. Constitución del puente

### 5.1. Salida canónica

```text
BRG-TXP-PRIMARY-001(E_TX_PRIMARY, h, v) ->
  TX_PRIMARY_CONSTITUIDO
  | TX_PRIMARY_PARCIAL_CON_RESIDUO
  | U_TX_PRIMARY
```

```text
TX_PRIMARY_CONSTITUIDO = <
  Propuesta_ID,
  Version_propuesta,
  Instante_de_corte,
  Cobertura,
  Componentes_ordenados,
  Identidad_por_componente,
  Papel_primario_o_pluralidad,
  Clasificacion_sistemica,
  Clasificacion_inmunosupresora,
  Estado,
  Intencion,
  Vigencia,
  Autoridad,
  Procedencia_por_campo,
  Version_del_puente
>
```

### 5.2. Reglas de salida

`TX_PRIMARY_CONSTITUIDO` sólo se produce cuando los seis controles están satisfechos y el régimen está declarado completo para el uso y horizonte.

`TX_PRIMARY_PARCIAL_CON_RESIDUO` sólo se produce cuando la parcialidad está expresamente declarada y una operación posterior puede usar una parte identificada sin inferir exhaustividad. Debe transportar el residuo y no puede sustentar una conclusión que requiera régimen completo.

`U_TX_PRIMARY` conserva todas las causas materiales no resueltas. No equivale a ausencia de tratamiento, riesgo alto, contraindicación ni bloqueo global.

Un fallo del conector, terminología o serialización produce `EJECUCION_TECNICA_NO_VALIDA`, nunca una salida clínica.

### 5.3. Invariante de no compensación

Ningún control compensa a otro. Cinco controles satisfechos no convierten en limpio un régimen con identidad, cobertura, versión, papel, estado o clasificación indeterminados.

La salida parcial sólo habilita usos cuya dependencia esté íntegramente cubierta por la parte constituida. Esa admisibilidad deberá declararse en `u(p,O)` y, posteriormente, en G7; no se presume aquí.

## 6. Por qué no entra en A0

Un parámetro atómico de `A0` debe expresar una proposición con estado clínico propio y función separable. «Está identificado» describe la calidad constitutiva del objeto que alimenta esas proposiciones.

Convertir el puente en un parámetro `0/1/U` produciría tres errores:

1. `0` confundiría ausencia explícita de tratamiento con identificación deficiente;
2. `1` ocultaría qué componentes y clasificaciones quedaron constituidos;
3. `U` fusionaría seis causas reparables de manera independiente.

Por tanto:

```text
SEM-EXP-001 = PUENTE_CONSTITUTIVO_COMPUESTO_PARTICIONADO_FINITO
BRG-TXP-PRIMARY-001 = PUENTE_CONSTITUTIVO_ADOPTADO
A0_APORTADO_POR_ESTA_RAIZ = VACIO
```

Esto no es un `NO GO`: entrega una referencia terapéutica positiva y utilizable, pero impide atribuirle significado clínico no constituido.

## 7. Relación con el parámetro ya adoptado

`PAR-GC-PLAN-SYS-001` conserva su identidad y no es absorbido por el puente. Para evaluarlo, el puente puede aportar:

- propuesta y versión;
- cobertura;
- componentes identificados;
- vía y formulación;
- estado, vigencia y autoridad;
- y procedencia.

El transductor de `PAR-GC-PLAN-SYS-001` continúa decidiendo únicamente si la propuesta incluye un glucocorticoide sistémico identificado. El puente no decide esa proposición por sí solo ni convierte cualquier tratamiento primario en glucocorticoide.

## 8. Adversarial integrada

### A. Crear un parámetro por cada campo

**Ataque:** dieciséis observables producen dieciséis posiciones ternarias.

**Resultado:** rechazado. Son datos y controles; carecen de predicado clínico independiente en esta raíz.

### B. Crear un único parámetro «tratamiento identificado»

**Ataque:** comprimir las seis dimensiones en `0/1/U`.

**Resultado:** rechazado. Oculta estados y consecuencias independientes.

### C. Confundir puente con riesgo

**Ataque:** `TX_PRIMARY_CONSTITUIDO` equivale a inmunosupresión efectiva o riesgo infeccioso.

**Resultado:** rechazado. Sólo constituye la referencia terapéutica propuesta.

### D. Hacer verdadero el puente con un código

**Ataque:** ATC o un identificador de producto resuelven identidad, vía, papel y clasificación.

**Resultado:** rechazado. La clasificación transportada no sustituye autoridad clínica ni cobertura.

### E. Forzar un único primario

**Ataque:** seleccionar el primer componente cuando existen varios primarios declarados.

**Resultado:** rechazado. El puente conserva pluralidad.

### F. Convertir propuesta en administración

**Ataque:** el tratamiento constituido demuestra exposición real.

**Resultado:** rechazado. Estado e intención permanecen explícitos.

### G. Tratar silencio como ausencia

**Ataque:** un componente no mencionado en un régimen parcial produce estado negativo.

**Resultado:** rechazado. Se conserva `U_COBERTURA_REGIMEN` o salida parcial con residuo.

### H. Elegir versión por fecha

**Ataque:** la propuesta más reciente por reloj gobierna.

**Resultado:** rechazado. Se exigen vínculos documentales de sustitución y vigencia.

### I. Compensar clasificación desconocida con identidad conocida

**Ataque:** una sustancia identificada se considera sistémica e inmunosupresora por plausibilidad.

**Resultado:** rechazado por no compensación.

### J. Usar salida parcial como completa

**Ataque:** una parte limpia habilita conclusiones que requieren el régimen entero.

**Resultado:** rechazado. Cada uso debe declarar su dependencia y el residuo.

### K. Bloquear todo por una `U` local

**Ataque:** cualquier campo indeterminado detiene `OP-IMM-001` completa.

**Resultado:** rechazado. Sólo se bloquean usos que dependan materialmente del campo.

### L. Convertir determinismo en validez

**Ataque:** reproducir el mismo puente demuestra corrección médica.

**Resultado:** rechazado. Demuestra fidelidad al contrato, no indicación ni seguridad.

### M. Abrir una matriz con controles

**Ataque:** asignar los seis controles a una matriz SV.

**Resultado:** rechazado. No son parámetros atómicos y no tienen propiedad matricial.

### N. Deriva analítica

**Ataque:** subdividir cada control en nuevas preguntas y prolongar indefinidamente G5.

**Resultado:** rechazado. La partición es terminal; los campos y causas están enumerados en G3 y no crean nuevas raíces.

### O. Sistema satisfecho con no resolver

**Ataque:** presentar `U_TX_PRIMARY` como producto final suficiente.

**Resultado:** rechazado. El producto positivo de esta puerta es el puente constituido o parcial con residuo; `U` exige causa, dependencia afectada y posibilidad de reparación. No acredita utilidad clínica completa.

**Dictamen adversarial integrado:** `PASA`.

## 9. Recuentos y terminación

| Magnitud | Valor |
|---|---:|
| raíces examinadas | 1 |
| particiones | 1 |
| controles terminales | 6 |
| puentes constitutivos adoptados | 1 |
| parámetros atómicos adoptados | 0 |
| nuevas raíces de Q0 | 0 |
| nuevas causas de U | 0 |
| matrices, rutas o frames abiertos | 0 |
| intervenciones autorizadas | 0 |
| documentos auxiliares | 0 |

La partición termina porque cada control corresponde exactamente a una consecuencia de G4 y opera sobre campos ya finitos de G3. Una fuente futura puede versionar reglas o resolver una `U`; no amplía silenciosamente esta versión.

## 10. Consecuencia para la secuencia

```text
G4-CON/SEM-EXP-001 = CERRADA
G5-ATM/SEM-EXP-001 = CERRADA_COMO_PUENTE_CONSTITUTIVO_COMPUESTO
BRG-TXP-PRIMARY-001 = ADOPTADO
A0 = {PAR-GC-PLAN-SYS-001}
G6-MAT = TODAVIA_NO_ABRIBLE
```

La cobertura de `Q0 v0` debe continuar por las raíces aplicables, respetando sus dependencias G3 y G4. El puente queda disponible para ellas sin adelantar matrices, rutas o decisiones.

## 11. Declaración

```text
SEM-EXP-001 = PUENTE_CONSTITUTIVO_COMPUESTO_PARTICIONADO_FINITO
BRG-TXP-PRIMARY-001 = PUENTE_CONSTITUTIVO_ADOPTADO
CONTROLES_TERMINALES = 6
A0_APORTADO_POR_ESTA_RAIZ = VACIO
A0 = {PAR-GC-PLAN-SYS-001}
TERMINACION = DEMOSTRADA
DETERMINISMO_NO_EQUIVALE_A_VALIDEZ_CLINICA
BUROCRACIA_AUXILIAR = NINGUNA
```
