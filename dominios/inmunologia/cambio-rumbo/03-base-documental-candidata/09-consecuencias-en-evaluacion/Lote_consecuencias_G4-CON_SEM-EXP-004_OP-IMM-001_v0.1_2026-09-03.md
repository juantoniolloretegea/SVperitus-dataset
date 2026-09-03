# Consecuencias G4-CON — SEM-EXP-004 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Puerta:** `G4-CON/SEM-EXP-004`
- **Operación:** `OP-IMM-001`
- **Raíz:** `SEM-EXP-004`
- **Base exacta:** `cd994c5eb9aed3b0aee8f98b3327057387cfe302`
- **Dependencia:** `G3-OBS/SEM-EXP-004` v0.1
- **Estatuto:** `CONSECUENCIAS_CANDIDATAS_CERRADAS`
- **Efecto clínico:** ninguno
- **Autorización asistencial:** ninguna

## 0. Objeto

Se constituyen las consecuencias candidatas de representar incorrectamente una exposición inmunomoduladora adicional, concurrente o previa, y de declarar su actividad para el episodio sin una regla específica.

La cadena exigida es:

```text
exposicion y hecho documentados o U
  -> error de identidad, cobertura, hecho, duplicacion, tiempo, magnitud o finalidad
  -> daño epistemologico inmediato
  -> dependencia posterior contaminada
  -> consecuencia para el experto
  -> consecuencia potencial para el paciente, condicionada y no atribuible
```

La coexistencia de exposiciones no constituye por sí sola interacción, adición, sinergia, riesgo alto ni contraindicación. La ausencia de una exposición en una historia incompleta tampoco constituye ausencia clínica.

La adversarial está integrada. No se crea documentación auxiliar.

## 1. Fuentes aplicadas y límites

| Fuente_ID | Fuente | Función en G4 |
|---|---|---|
| `CON-IMMEXP-SRC-001` | Organización Mundial de la Salud, *Medication Without Harm* | sostiene que los errores pueden producirse en prescripción, transcripción, dispensación, administración y monitorización, y que las situaciones de polifarmacia son un área prioritaria; no atribuye un daño individual en este corte |
| `CON-IMMEXP-SRC-002` | AHRQ PSNet, *Medication Reconciliation* | sostiene que historias incompletas y cambios no intencionados pueden ocasionar omisiones, duplicaciones o dosis incorrectas y exponer a acontecimientos adversos; conserva la evidencia mixta sobre beneficio clínico generalizable de la conciliación |
| `CON-IMMEXP-SRC-003` | HL7 FHIR R5, `MedicationStatement`, `MedicationAdministration` y `MedicationRequest` | sostiene la separación documental entre declaración, administración y solicitud; no constituye actividad biológica ni causalidad |
| `CON-IMMEXP-SRC-004` | CDC, *Altered Immunocompetence* | demuestra, para la finalidad vacunal, que la seguridad, efectividad y temporización dependen del tipo y grado de inmunosupresión y de terapias específicas; no se transporta como regla universal de `OP-IMM-001` |

Enlaces:

- `CON-IMMEXP-SRC-001`: https://www.who.int/initiatives/medication-without-harm
- `CON-IMMEXP-SRC-002`: https://psnet.ahrq.gov/primer/medication-reconciliation
- `CON-IMMEXP-SRC-003a`: https://hl7.org/fhir/R5/medicationstatement.html
- `CON-IMMEXP-SRC-003b`: https://hl7.org/fhir/R5/medicationadministration.html
- `CON-IMMEXP-SRC-003c`: https://hl7.org/fhir/R5/medicationrequest.html
- `CON-IMMEXP-SRC-004`: https://www.cdc.gov/vaccines/hcp/imz-best-practices/altered-immunocompetence.html

Las fuentes sostienen peligro general, discrepancias y dependencia de finalidad. No permiten sumar exposiciones en una puntuación, fijar ventanas universales ni afirmar que una discrepancia concreta haya causado un desenlace.

## 2. Clases de consecuencia

| Clase | Alcance |
|---|---|
| `CONSECUENCIA_EPISTEMOLOGICA` | pérdida o falsificación de identidad, cobertura, cronología o procedencia |
| `CONSECUENCIA_OPERACIONAL_CANDIDATA` | activación, omisión, duplicación o aplicación fuera de finalidad de una regla posterior |
| `CONSECUENCIA_CLINICA_POTENCIAL_NO_ATRIBUIBLE` | posible efecto si el error atraviesa controles posteriores, modifica una decisión o actuación y no es interceptado |

Toda consecuencia operacional conserva un daño epistemológico anterior. Ninguna consecuencia potencial es un pronóstico individual.

## 3. Consecuencias candidatas

### 3.1. `CON-IMMEXP-ID-001` — exposición atribuida al objeto farmacológico equivocado

- **Clase primaria:** `CONSECUENCIA_EPISTEMOLOGICA`.
- **Entrada:** `OBS-IMMEXP-001`–`007`; `U` de identidad, producto, vía, papel o clasificación.
- **Error:** fusionar sustancias o combinaciones, sustituir producto por sustancia, inferir vía o atribuir inmunomodulación por nombre o código.
- **Daño epistemológico:** el expediente representa una exposición distinta de la documentada.
- **Consecuencia para el experto:** aplica una regla de persistencia, interacción o prevención al agente equivocado, o deja de aplicarla al correcto.
- **Consecuencia potencial para el paciente:** evaluación preventiva omitida, innecesaria o mal dirigida si el error alcanza una decisión.
- **Salida máxima G4:** `U_IDENTIDAD_EXPOSICION_ADICIONAL` o bloqueo localizado.
- **Límite:** no declara qué fármaco es inmunomodulador ni qué regla le corresponde.

### 3.2. `CON-IMMEXP-COV-001` — historia parcial tratada como ausencia

- **Clase primaria:** `CONSECUENCIA_EPISTEMOLOGICA`.
- **Entrada:** `OBS-IMMEXP-014`–`018`; `U(COBERTURA_HISTORIA)`.
- **Error:** considerar exhaustiva una lista parcial o circunscrita a un sistema y asignar ausencia a lo no registrado.
- **Daño epistemológico:** desaparecen exposiciones adicionales potencialmente pertinentes.
- **Consecuencia para el experto:** construye el perfil predecisional sobre una historia farmacológica falsamente completa.
- **Consecuencia potencial para el paciente:** omisión de una comprobación, vigilancia o ajuste posterior que dependiera de la exposición no recogida.
- **Fuente:** `CON-IMMEXP-SRC-002`, omisiones y acceso incompleto a listas previas.
- **Salida máxima G4:** `U_COBERTURA_HISTORIA`; nunca `SIN_OTRAS_EXPOSICIONES` por silencio.
- **Límite:** una historia completa tampoco demuestra por sí sola actividad clínica.

### 3.3. `CON-IMMEXP-EVT-001` — intención, declaración y administración confundidas

- **Clase primaria:** `CONSECUENCIA_EPISTEMOLOGICA`.
- **Entrada:** `OBS-IMMEXP-008`–`010`, `014`–`016`.
- **Error:** convertir solicitud en administración, declaración en suceso formal o suspensión documental en prueba de desaparición del efecto.
- **Daño epistemológico:** se fabrica o elimina una exposición real.
- **Consecuencia para el experto:** calcula recencia y aplicabilidad sobre un hecho de naturaleza o certeza incorrectas.
- **Consecuencia potencial para el paciente:** evaluación temporal o preventiva innecesaria u omitida si el hecho falso gobierna una actuación.
- **Fuentes:** `CON-IMMEXP-SRC-003` y `CON-IMMEXP-SRC-001`.
- **Salida máxima G4:** `U_NATURALEZA_DEL_HECHO`.
- **Límite:** FHIR delimita transporte y no decide actividad inmunológica.

### 3.4. `CON-IMMEXP-DUP-001` — un mismo hecho contado como exposiciones independientes

- **Clase primaria:** `CONSECUENCIA_OPERACIONAL_CANDIDATA`.
- **Entrada:** `OBS-IMMEXP-001`, `008`, `012`, `014`–`016`; vínculos `Derivado_de`.
- **Error:** contar por separado una orden, una declaración derivada y su administración; o duplicar el mismo suceso entre sistemas.
- **Daño epistemológico:** se multiplica artificialmente la historia de exposición.
- **Consecuencia para el experto:** interpreta una única exposición como concurrencia, repetición o carga combinada.
- **Consecuencia potencial para el paciente:** escalado innecesario de evaluaciones o modificación indebida de una actuación futura si la duplicación no se intercepta.
- **Fuente:** `CON-IMMEXP-SRC-003`, distinción y enlace entre recursos.
- **Salida máxima G4:** `U_DEDUPLICACION_DE_HECHOS`.
- **Límite:** deduplicar no autoriza a fusionar hechos genuinamente distintos.

### 3.5. `CON-IMMEXP-TIME-001` — actividad declarada por cronología insuficiente

- **Clase primaria:** `CONSECUENCIA_OPERACIONAL_CANDIDATA`.
- **Entrada:** `OBS-IMMEXP-010`, `012`, `013`, `018`; `U` de tiempo, último hecho, suspensión, horizonte o regla.
- **Error:** equiparar última administración, suspensión o intervalo farmacocinético aislado con fin del efecto; o mantener indefinidamente una exposición como activa.
- **Daño epistemológico:** se falsifica la vigencia clínica para el horizonte.
- **Consecuencia para el experto:** incluye o excluye una exposición de una regla sin ventana específica por agente y finalidad.
- **Consecuencia potencial para el paciente:** temporización o selección incorrectas de una actuación posterior, condicionadas a la regla concreta.
- **Fuente:** `CON-IMMEXP-SRC-004`, dependencia de terapia, tipo y grado de inmunosupresión para una finalidad definida.
- **Salida máxima G4:** `U_ACTIVIDAD_TEMPORAL`.
- **Límite:** no adopta intervalos del CDC fuera de su finalidad ni fija una ventana propia.

### 3.6. `CON-IMMEXP-MAG-001` — magnitud o patrón falsos usados para determinar persistencia

- **Clase primaria:** `CONSECUENCIA_OPERACIONAL_CANDIDATA`.
- **Entrada:** `OBS-IMMEXP-011`, `012`, `016`; `U(MAGNITUD)`.
- **Error:** promediar pautas, trasladar equivalencias, confundir dosis propuesta con administrada o ignorar un patrón intermitente.
- **Daño epistemológico:** se presenta una exposición cuantitativa que no ocurrió o no está demostrada.
- **Consecuencia para el experto:** aplica una regla dependiente de magnitud o pauta sobre entradas falsas.
- **Consecuencia potencial para el paciente:** clasificación y actuación posteriores erróneas si la magnitud adulterada cruza un criterio aplicable.
- **Fuentes:** `CON-IMMEXP-SRC-001`, etapas del uso; `CON-IMMEXP-SRC-002`, dosis incorrectas.
- **Salida máxima G4:** `U_MAGNITUD_EXPOSICION_ADICIONAL`.
- **Límite:** no constituye equivalencia, umbral ni suma de dosis.

### 3.7. `CON-IMMEXP-PUR-001` — regla válida para una finalidad transportada a otra

- **Clase primaria:** `CONSECUENCIA_OPERACIONAL_CANDIDATA`.
- **Entrada:** material de `N_IMMEXP_VIGENCIA_INPUT`; finalidad, horizonte, regla y versión.
- **Error:** utilizar una ventana o clasificación concebida para vacunación, una infección concreta u otra decisión como definición universal de «actividad».
- **Daño epistemológico:** se borra la dependencia de finalidad del efecto clínicamente pertinente.
- **Consecuencia para el experto:** obtiene respuestas reproducibles pero aplicadas a la pregunta equivocada.
- **Consecuencia potencial para el paciente:** recomendación preventiva, temporización o evaluación inadecuadas si la regla trasladada gobierna la actuación.
- **Fuente:** `CON-IMMEXP-SRC-004`, utilizada como demostración de especificidad de finalidad, no como regla universal.
- **Salida máxima G4:** `U_FINALIDAD_O_REGLA_NO_APLICABLE`.
- **Límite:** no niega reutilización cuando una equivalencia entre finalidades haya sido constituida y versionada.

## 4. Tabla de conjunción

| Consecuencia_ID | Error | Daño inmediato | Salida máxima G4 |
|---|---|---|---|
| `CON-IMMEXP-ID-001` | identidad o clase falsa | exposición equivocada | `U_IDENTIDAD_EXPOSICION_ADICIONAL` |
| `CON-IMMEXP-COV-001` | historia parcial tratada como completa | exposición omitida | `U_COBERTURA_HISTORIA` |
| `CON-IMMEXP-EVT-001` | naturaleza del hecho falsa | exposición fabricada o eliminada | `U_NATURALEZA_DEL_HECHO` |
| `CON-IMMEXP-DUP-001` | doble conteo | concurrencia artificial | `U_DEDUPLICACION_DE_HECHOS` |
| `CON-IMMEXP-TIME-001` | vigencia inferida por fecha | actividad temporal falsa | `U_ACTIVIDAD_TEMPORAL` |
| `CON-IMMEXP-MAG-001` | magnitud o patrón adulterados | entrada cuantitativa falsa | `U_MAGNITUD_EXPOSICION_ADICIONAL` |
| `CON-IMMEXP-PUR-001` | traslado entre finalidades | regla aplicada fuera de dominio | `U_FINALIDAD_O_REGLA_NO_APLICABLE` |

No es una matriz ni una ruta. Las filas no se suman y ninguna autoriza una intervención.

## 5. Causalidad y autoridad

1. Una discrepancia documental puede no alcanzar nunca una decisión.
2. Una exposición adicional puede ser clínicamente irrelevante para una finalidad concreta.
3. Dos exposiciones coexistentes no demuestran interacción ni efecto combinado.
4. La autoridad documental acredita hechos; la autoridad clínica adopta la regla de actividad y su finalidad.
5. La consecuencia para el paciente requiere error no interceptado, dependencia material, decisión o actuación y desenlace.
6. La evidencia general sobre daño medicamentoso no cuantifica el riesgo individual de estas discrepancias.
7. La eficacia clínica de conciliar historias no se presume por corregir su representación.

## 6. Registro anterior a la conclusión

Toda instancia futura deberá serializar:

```text
<
  Consecuencia_ID,
  Exposicion_ID,
  Hecho_ID_o_conjunto,
  Observable_o_U,
  Error_definido,
  Daño_epistemologico,
  Dependencia_afectada,
  Consecuencia_experto,
  Consecuencia_paciente_condicionada,
  Finalidad,
  Horizonte,
  Fuente_ID,
  Localizador,
  Limites_causales,
  Autoridad,
  Version
>
```

Una cita posterior no repara una historia incompleta, un hecho duplicado ni una ventana aplicada fuera de finalidad.

## 7. Adversarial integrada

### A. Omitir exposición equivale a daño consumado

**Ataque:** toda exposición ausente de la lista ya produjo perjuicio.

**Resultado:** rechazado. Primero existe pérdida epistemológica; el daño exige propagación y actuación.

### B. Conciliación correcta garantiza beneficio

**Ataque:** corregir la historia mejora necesariamente desenlaces.

**Resultado:** rechazado. AHRQ describe evidencia clínica generalizable mixta.

### C. Más exposiciones equivale a más riesgo

**Ataque:** contar agentes produce una escala monotónica.

**Resultado:** rechazado. No hay regla de composición ni pesos constituidos.

### D. Duplicación conservadora

**Ataque:** ante duda, contar dos veces es más seguro.

**Resultado:** rechazado. Fabrica concurrencia y puede inducir actuaciones innecesarias.

### E. Silencio igual a ausencia

**Ataque:** una lista parcial sin otro inmunomodulador produce `0`.

**Resultado:** rechazado mediante `CON-IMMEXP-COV-001`.

### F. Solicitud igual a exposición real

**Ataque:** una orden basta para declarar efecto.

**Resultado:** rechazado mediante `CON-IMMEXP-EVT-001`.

### G. Suspensión igual a inactividad

**Ataque:** suspendido produce automáticamente `0` clínico.

**Resultado:** rechazado. La decisión documental y el efecto biológico son distintos.

### H. Última administración más semivida

**Ataque:** una suma temporal genérica cierra la actividad.

**Resultado:** rechazado. Falta regla específica por agente, efecto y finalidad.

### I. Regla vacunal universal

**Ataque:** el intervalo CDC gobierna cualquier salida de `OP-IMM-001`.

**Resultado:** rechazado mediante `CON-IMMEXP-PUR-001`.

### J. Nombre o código como inmunomodulación demostrada

**Ataque:** identidad regulatoria equivale a pertinencia clínica.

**Resultado:** rechazado mediante `CON-IMMEXP-ID-001`.

### K. Promedio de pauta

**Ataque:** una pauta variable se reduce a dosis media.

**Resultado:** rechazado mediante `CON-IMMEXP-MAG-001`.

### L. Bloqueo global por cualquier U

**Ataque:** una fecha dudosa detiene toda la operación.

**Resultado:** rechazado. Sólo bloquea dependencias que necesiten esa fecha con esa precisión.

### M. Consecuencia clínica decorativa

**Ataque:** añadir «puede causar infección» sin regla ni transición.

**Resultado:** rechazado. Cada consecuencia exige dependencia, actuación y límites causales.

### N. Determinismo como validez

**Ataque:** reproducir el mismo error de cronología lo convierte en correcto.

**Resultado:** rechazado. Fidelidad y validez se auditan por separado.

### O. Abrir ya rutas o intervenciones

**Ataque:** una consecuencia ordena profilaxis, vacuna o modificación terapéutica.

**Resultado:** rechazado. Faltan G5, G6 y G7.

### P. Deriva infinita

**Ataque:** crear una consecuencia por fármaco o por fuente.

**Resultado:** rechazado. Las siete clases cubren errores materiales finitos; los fármacos y fuentes son instancias.

### Q. Sistema satisfecho con U

**Ataque:** registrar incertidumbre sustituye la búsqueda de la exposición.

**Resultado:** rechazado. Cada `U` debe conservar causa, fuente faltante, dependencia y posibilidad de reparación; no acredita perfil completo.

**Dictamen adversarial integrado:** `PASA`.

## 8. Recuentos

| Magnitud | Valor |
|---|---:|
| consecuencias candidatas | 7 |
| epistemológicas primarias | 3 |
| operacionales candidatas primarias | 4 |
| afirmaciones de causalidad individual | 0 |
| reglas de composición | 0 |
| ventanas o umbrales adoptados | 0 |
| parámetros, matrices, rutas o frames | 0 |
| documentos auxiliares | 0 |

## 9. Regla de cierre

`G4-CON/SEM-EXP-004` cierra si:

1. existen exactamente siete consecuencias;
2. identidad, cobertura, naturaleza del hecho, duplicación, tiempo, magnitud y finalidad permanecen separadas;
3. cada consecuencia contiene daño epistemológico y efecto para el experto;
4. coexistencia no se convierte en interacción o suma de riesgo;
5. toda consecuencia para el paciente queda condicionada y no atribuible;
6. la evidencia de seguridad medicamentosa conserva sus límites;
7. CDC no se transporta fuera de la finalidad vacunal;
8. procedencia precede a la conclusión;
9. reproducción, privacidad y finitud pasan;
10. no se constituye parámetro, matriz, ruta, intervención o consejo.

## 10. Efecto

```text
G3-OBS/SEM-EXP-004 = CERRADA
G4-CON/SEM-EXP-004 = CERRADA
I_IMMEXP_ACTIVE_v = NO_CONSTITUIDA
G5-ATM/SEM-EXP-004 = NO_ABIERTA
A0 = {PAR-GC-PLAN-SYS-001}
```

La siguiente puerta es `G5-ATM/SEM-EXP-004`. Deberá separar la existencia de exposiciones adicionales, su representación y su actividad por finalidad sin crear un agregado «inmunosupresión total».
