# Lote observacional G3-OBS — SEM-EXP-004 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Puerta:** `G3-OBS/SEM-EXP-004`
- **Operación:** `OP-IMM-001`
- **Raíz:** `SEM-EXP-004`
- **Base exacta:** `1b7ddd37978e4d794234c5be1b2b54d2c49d1d77`
- **Estatuto:** `OBSERVABLES_Y_NORMALIZADORES_CANDIDATOS_CERRADOS`
- **Perímetro:** otras exposiciones inmunomoduladoras farmacológicas, concurrentes o previas; no inventario terapéutico general
- **Efecto clínico:** ninguno
- **Autorización asistencial:** ninguna

## 0. Pregunta gobernante y corte

> `SEM-EXP-004`: ¿Está identificada cualquier otra exposición inmunomoduladora concurrente o previa que siga siendo clínicamente activa para este episodio?

La raíz contiene dos objetos que deben permanecer separados:

1. el hecho documental de una exposición adicional propuesta, comunicada o administrada;
2. su posible actividad clínica para una finalidad y horizonte determinados.

Este lote constituye los observables del primer objeto y los insumos necesarios para evaluar posteriormente el segundo. No deduce persistencia inmunológica por proximidad temporal, mecanismo supuesto, semivida farmacocinética aislada, pertenencia de clase o memoria del modelo.

La adversarial está integrada. No se crea documentación auxiliar.

## 1. Fuentes externas aplicadas

| Fuente_ID | Fuente | Corte y función exacta |
|---|---|---|
| `OBS-IMMEXP-SRC-001` | HL7 FHIR R5, `MedicationStatement` | versión 5.0.0; distingue una declaración de uso actual, pasado o futuro, de una administración formal; conserva fuente, periodo efectivo, derivación y pauta, pero puede ser menos precisa |
| `OBS-IMMEXP-SRC-002` | HL7 FHIR R5, `MedicationAdministration` | versión 5.0.0; aporta el suceso formal de administración y sus detalles; no demuestra por sí solo persistencia del efecto |
| `OBS-IMMEXP-SRC-003` | HL7 FHIR R5, `MedicationRequest` | versión 5.0.0; aporta solicitud u orden e intención; no equivale a consumo o administración |
| `OBS-IMMEXP-SRC-004` | Agencia Europea de Medicamentos, SPOR/ISO IDMP | página oficial consultada 03-09-2026; apoya identidad de sustancia, producto, organización y referencias; no constituye equivalencia clínica, mecanismo ni vigencia del efecto |

Enlaces:

- `OBS-IMMEXP-SRC-001`: https://hl7.org/fhir/R5/medicationstatement.html
- `OBS-IMMEXP-SRC-002`: https://hl7.org/fhir/R5/medicationadministration.html
- `OBS-IMMEXP-SRC-003`: https://hl7.org/fhir/R5/medicationrequest.html
- `OBS-IMMEXP-SRC-004`: https://www.ema.europa.eu/en/human-regulatory-overview/research-development/data-medicines-iso-idmp-standards-overview/substance-product-organisation-referential-spor-master-data

FHIR se utiliza como frontera de transporte entre declaración, solicitud y administración. SPOR se utiliza para identidad regulatoria. Ninguna de estas fuentes decide si una exposición continúa inmunológicamente activa para `OP-IMM-001`.

## 2. Entidades observacionales

Cada exposición adicional se representa mediante una cabecera y uno o más hechos enlazados:

```text
E_IMM_EXP = <
  Exposicion_ID,
  Identidad_farmacologica,
  Producto_forma_via,
  Papel_respecto_del_tratamiento_primario,
  Clasificacion_inmunomoduladora_declarada,
  Autoridad_de_clasificacion,
  Cobertura_de_historia,
  Procedencia_por_campo,
  Version
>
```

```text
F_IMM_EXP = <
  Hecho_ID,
  Exposicion_ID,
  Tipo_de_hecho,
  Estado_e_intencion,
  Instante_o_periodo,
  Dosis_y_pauta_originales,
  Fuente_de_informacion,
  Derivado_de,
  Certeza_documental,
  Procedencia_por_campo,
  Version
>
```

`Tipo_de_hecho` conserva como mínimo:

```text
PROPUESTA | SOLICITUD_U_ORDEN | DECLARACION_DE_USO | DISPENSACION |
ADMINISTRACION | SUSPENSION_DOCUMENTADA | CANCELACION | OTRO_TIPADO
```

No se fusionan hechos diferentes en una etiqueta «medicación activa».

## 3. Observables candidatos

| Observable_ID | Contenido | Regla de identidad | `U` propia |
|---|---|---|---|
| `OBS-IMMEXP-001` | identificador de exposición | cambia si no puede demostrarse continuidad del mismo objeto farmacológico | `U(EXPOSICION_ID, causa)` |
| `OBS-IMMEXP-002` | sustancia o combinación declarada | cada componente y su relación permanecen visibles | `U(SUSTANCIA, causa)` |
| `OBS-IMMEXP-003` | producto o preparación | no sustituye automáticamente a la sustancia | `U(PRODUCTO, causa)` |
| `OBS-IMMEXP-004` | forma farmacéutica | se conserva cuando modifica identidad o exposición | `U(FORMA, causa)` |
| `OBS-IMMEXP-005` | vía | no se infiere si el producto admite varias | `U(VIA, causa)` |
| `OBS-IMMEXP-006` | papel respecto del tratamiento primario | concomitante, previo, puente, rescate u otro papel declarado | `U(PAPEL, causa)` |
| `OBS-IMMEXP-007` | clasificación inmunomoduladora declarada | exige regla, finalidad, versión y autoridad | `U(CLASIFICACION, causa)` |
| `OBS-IMMEXP-008` | tipo de hecho | conserva propuesta, orden, declaración, administración y suspensión | `U(TIPO_HECHO, causa)` |
| `OBS-IMMEXP-009` | estado e intención del hecho | no convierte una intención en ejecución | `U(ESTADO_INTENCION, causa)` |
| `OBS-IMMEXP-010` | instante o periodo | conserva comienzo, fin, apertura y precisión originales | `U(TIEMPO, causa)` |
| `OBS-IMMEXP-011` | dosis y pauta originales | no calcula equivalencias ni promedios implícitos | `U(MAGNITUD, causa)` |
| `OBS-IMMEXP-012` | último hecho de administración demostrado | se elige por hechos enlazados, no por una mención narrativa aislada | `U(ULTIMA_ADMINISTRACION, causa)` |
| `OBS-IMMEXP-013` | suspensión o cancelación documentada | no prueba desaparición del efecto biológico | `U(SUSPENSION, causa)` |
| `OBS-IMMEXP-014` | fuente de información | paciente, profesional, organización o registro, sin igualar autoridades | `U(FUENTE_INFORMACION, causa)` |
| `OBS-IMMEXP-015` | vínculo de derivación | enlaza declaración con solicitud, dispensación o administración cuando exista | `U(DERIVACION, causa)` |
| `OBS-IMMEXP-016` | certeza documental | directo, comunicado, derivado, contradictorio o desconocido | `U(CERTEZA_DOCUMENTAL, causa)` |
| `OBS-IMMEXP-017` | cobertura de la historia farmacológica | completa para el corte, parcial, condicionada o desconocida | `U(COBERTURA_HISTORIA, causa)` |
| `OBS-IMMEXP-018` | horizonte de `OP-IMM-001` | instante predecisional frente al que se evaluará vigencia | `U(HORIZONTE, causa)` |

`Procedencia_por_campo` es obligatoria y no constituye un decimonoveno observable clínico. Incluye fuente, localizador, sistema, instante de captura, autoría o informante y versión.

## 4. Separaciones obligatorias

1. Propuesta no equivale a exposición.
2. Orden no equivale a administración.
3. Declaración de uso no equivale a suceso formalmente administrado.
4. Última administración no equivale a fin de exposición.
5. Suspensión farmacológica no equivale a desaparición del efecto.
6. Semivida farmacocinética no equivale por sí sola a ventana inmunológica.
7. Pertenencia de clase no demuestra actividad para una finalidad concreta.
8. «Concomitante» y «previa» describen relación temporal, no efecto.
9. Una historia parcial no permite afirmar ausencia de otras exposiciones.
10. Un código compartido no demuestra equivalencia de sustancias, productos, vías o efectos.
11. Dosis propuesta, comunicada y administrada permanecen separadas.
12. Mecanismo farmacológico conocido no sustituye la regla clínica versionada.
13. Una exposición puede ser pertinente para una finalidad y no para otra.
14. Varias exposiciones no se colapsan en un único estado agregado.

## 5. Normalizadores candidatos

No producen estados clínicos `0/1/U`.

### 5.1. Identidad farmacológica

```text
N_IMMEXP_ID(E_IMM_EXP, mapas_versionados) ->
  identidad_trazada_por_componentes | U
```

Conserva sustancia, producto, forma, vía, identificadores originales y versiones. No decide equivalencia clínica.

### 5.2. Línea de hechos

```text
N_IMMEXP_EVENTOS({F_IMM_EXP}, Exposicion_ID) ->
  hechos_ordenados_sin_fusion | U
```

Ordena por tiempo, tipo e identificador canónico. No transforma una declaración en administración ni completa intervalos ausentes.

### 5.3. Cobertura de historia

```text
N_IMMEXP_COBERTURA(fuentes, corte) ->
  COMPLETA_DECLARADA | PARCIAL | CONDICIONADA | U
```

«Completa» exige declaración y perímetro de fuentes; no se deduce por número de registros.

### 5.4. Último suceso demostrado

```text
N_IMMEXP_ULTIMO({F_IMM_EXP}, tipo, h) ->
  hecho_demostrado | SIN_HECHO_EN_COBERTURA_COMPLETA | U
```

No estima la última dosis si faltan episodios ni convierte ausencia de registro en ausencia de exposición.

### 5.5. Insumos de vigencia clínica

```text
N_IMMEXP_VIGENCIA_INPUT(E_IMM_EXP, hechos, finalidad, h) ->
  <identidad, via, magnitud, patron, ultimo_hecho, finalidad, horizonte,
   regla_requerida, procedencia> | U
```

Este normalizador prepara el dominio de una futura regla. No devuelve `ACTIVA` ni `INACTIVA`.

## 6. Regla de actividad deliberadamente no constituida

La salida clínica futura requerirá una función separada:

```text
I_IMMEXP_ACTIVE_v(exposicion, finalidad, h, regla_especifica) -> {0,1,U}
```

En G3 no existen una regla universal, una ventana única ni una equivalencia transversal que permitan ejecutarla. Deberán especificarse, cuando corresponda:

- agente o conjunto de agentes;
- producto, formulación y vía relevantes;
- magnitud y patrón de exposición;
- hecho documental admisible;
- intervalo de persistencia;
- finalidad clínica;
- horizonte;
- conflictos y excepciones;
- fuente, jurisdicción y versión;
- y autoridad de adopción.

La ausencia de esta regla no invalida los observables. Impide exclusivamente afirmar actividad clínica.

## 7. Causas tipadas de U

| Código | Activación | Efecto localizado |
|---|---|---|
| `C_IMMEXP_ID` | identidad o combinación ambiguas | no se fusiona la exposición |
| `C_IMMEXP_PRODUCTO_VIA` | producto, forma o vía insuficientes | no se traslada clasificación |
| `C_IMMEXP_PAPEL` | relación con el tratamiento primario desconocida | no se asigna concurrencia o antecedencia |
| `C_IMMEXP_CLASE` | regla inmunomoduladora ausente | no se clasifica por nombre |
| `C_IMMEXP_HECHO` | tipo, estado o intención ambiguos | no se afirma exposición real |
| `C_IMMEXP_TIEMPO` | inicio, fin o precisión insuficientes | no se calcula recencia limpia |
| `C_IMMEXP_MAGNITUD` | dosis o pauta necesarias ausentes | no se aplica regla dependiente |
| `C_IMMEXP_ULTIMO` | último suceso no demostrable | no se fabrica fecha terminal |
| `C_IMMEXP_SUSPENSION` | suspensión o cancelación conflictivas | no se supone continuidad ni cese |
| `C_IMMEXP_FUENTE` | informante o autoridad desconocidos | no se igualan afirmaciones |
| `C_IMMEXP_DERIVACION` | declaración no enlazada con su origen | se conserva menor certeza |
| `C_IMMEXP_COBERTURA` | historia parcial o desconocida | silencio no produce ausencia |
| `C_IMMEXP_CONFLICTO` | fuentes admisibles discrepan | no se elige por conveniencia |
| `C_IMMEXP_REGLA_ACTIVIDAD` | falta regla por agente y finalidad | actividad clínica queda en `U` |
| `C_IMMEXP_HORIZONTE` | corte predecisional no fijado | vigencia no evaluable |
| `C_IMMEXP_PROCEDENCIA` | falta localizador, captura o versión | el campo no alimenta conclusión limpia |

## 8. Proyección sobre SEM-EXP-004

```text
exposiciones individualizadas
  + hechos sin fusionar
  + cobertura declarada
  + tiempo y magnitud originales
  + finalidad y horizonte
  + regla especifica versionada
  -> material para futura adjudicacion de actividad | U tipada
```

Este lote no decide:

- qué familias farmacológicas deben buscarse universalmente;
- qué exposición modifica el riesgo;
- cuánto dura un efecto inmunológico;
- si dos agentes son equivalentes;
- si las exposiciones se suman, potencian o compensan;
- ni qué actuación corresponde.

## 9. Canonicalización y reproducción

Para la misma entrada, fuentes, corte y versiones:

1. las exposiciones se ordenan por `Exposicion_ID`;
2. los hechos se ordenan por tiempo, tipo e identificador;
3. la precisión temporal original se conserva;
4. los componentes de combinaciones no se colapsan;
5. todas las fuentes admisibles en conflicto permanecen visibles;
6. cada `U` conserva campo, causa y dependencia;
7. salida, residuos y serialización coinciden byte a byte.

Una fuente o versión distinta constituye otra entrada. Un fallo técnico produce `EJECUCION_TECNICA_NO_VALIDA`.

## 10. Adversarial integrada

### A. Lista de medicación igual a exposición completa

**Ataque:** cualquier lista permite afirmar ausencia de lo no mencionado.

**Resultado:** rechazado. La cobertura debe estar declarada; de otro modo existe `U_COBERTURA_HISTORIA`.

### B. Medicación «activa» en FHIR igual a efecto activo

**Ataque:** una etiqueta transportada resuelve la pregunta clínica.

**Resultado:** rechazado. El transporte de uso no constituye persistencia inmunológica.

### C. Orden igual a administración

**Ataque:** `MedicationRequest` demuestra exposición real.

**Resultado:** rechazado por separación de hechos.

### D. Declaración igual a administración formal

**Ataque:** `MedicationStatement` posee la misma precisión que `MedicationAdministration`.

**Resultado:** rechazado. Se conservan informante, derivación y certeza documental.

### E. Última dosis igual a fin del efecto

**Ataque:** la fecha del último suceso cierra la ventana inmunológica.

**Resultado:** rechazado. Falta `I_IMMEXP_ACTIVE_v`.

### F. Semivida como ventana universal

**Ataque:** una constante farmacocinética decide actividad clínica.

**Resultado:** rechazado. La finalidad y el tipo de efecto pueden exigir otra regla.

### G. Clase como verdad clínica

**Ataque:** ATC, SPOR o una etiqueta de clase demuestran inmunomodulación pertinente.

**Resultado:** rechazado. Identidad y clasificación clínica son planos distintos.

### H. Agregación de exposiciones

**Ataque:** varias exposiciones producen un único estado «inmunosuprimido».

**Resultado:** rechazado. Se preservan exposiciones, hechos y `U` independientes.

### I. Doble conteo

**Ataque:** una declaración derivada de una administración cuenta como dos exposiciones.

**Resultado:** rechazado mediante `Derivado_de` y `N_IMMEXP_EVENTOS`.

### J. Suspensión igual a efecto ausente

**Ataque:** estado suspendido produce `0` clínico.

**Resultado:** rechazado. Sólo prueba una decisión documental.

### K. Fecha imprecisa convertida en exacta

**Ataque:** «hace meses» se serializa como un día concreto.

**Resultado:** rechazado. Se conserva precisión original y `U` si la regla exige más.

### L. Inventario mundial antes de continuar

**Ataque:** enumerar todos los inmunomoduladores para cerrar G3.

**Resultado:** rechazado. El esquema es finito; las instancias pertenecen al episodio y las reglas específicas a puertas posteriores.

### M. U convertida en alto riesgo

**Ataque:** exposición desconocida produce automáticamente `1` o abstención global.

**Resultado:** rechazado. La criticidad y el alcance del bloqueo pertenecen a la ruta futura.

### N. Determinismo igual a validez

**Ataque:** la misma cronología reproducida prueba que la exposición sigue activa.

**Resultado:** rechazado. Sólo demuestra fidelidad de representación.

### O. Salto de secuencia

**Ataque:** usar ya los observables para indicar vacuna, profilaxis o cambio terapéutico.

**Resultado:** rechazado. Faltan G4, G5, propiedad, uso y ruta.

### P. Deriva infinita

**Ataque:** abrir un sublote por agente, fuente o suceso.

**Resultado:** rechazado. Son instancias de dos entidades finitas, no nuevas raíces ni sublotes.

**Dictamen adversarial integrado:** `PASA`.

## 11. Recuentos

| Magnitud | Valor |
|---|---:|
| raíces cubiertas | 1 |
| entidades observacionales | 2 |
| tipos mínimos de hecho | 8 |
| observables candidatos | 18 |
| metadatos obligatorios adicionales | 1 |
| normalizadores candidatos | 5 |
| causas tipadas de `U` | 16 |
| reglas de actividad clínica constituidas | 0 |
| parámetros, matrices, rutas o frames | 0 |
| documentos auxiliares | 0 |

## 12. Regla de cierre

`G3-OBS/SEM-EXP-004` cierra si:

1. existen exactamente dos entidades, dieciocho observables y cinco normalizadores;
2. exposición, propuesta, orden, declaración y administración permanecen separados;
3. la cobertura de historia precede a toda inferencia de ausencia;
4. identidad, forma, vía, magnitud, tiempo y procedencia no se colapsan;
5. la suspensión no se convierte en desaparición de efecto;
6. la regla de actividad permanece sin ejecutar;
7. cada exposición y hecho conserva identidad propia;
8. las dieciséis causas de `U` están localizadas;
9. reproducción, privacidad y finitud pasan;
10. no se constituye riesgo, intervención, parámetro, matriz, ruta o modificación del Lenguaje SV.

## 13. Efecto

```text
G3-OBS/SEM-EXP-004 = CERRADA
SEM-EXP-004 = OBSERVABLES_CANDIDATOS_CERRADOS
I_IMMEXP_ACTIVE_v = NO_CONSTITUIDA
G4-CON/SEM-EXP-004 = NO_ABIERTA
G5-ATM/SEM-EXP-004 = NO_ABIERTA
A0 = {PAR-GC-PLAN-SYS-001}
```

La siguiente puerta es `G4-CON/SEM-EXP-004`: consecuencias de omitir, duplicar, atribuir o declarar inactiva una exposición adicional sin base suficiente. No se abrirá atomicidad antes de cerrarla.
