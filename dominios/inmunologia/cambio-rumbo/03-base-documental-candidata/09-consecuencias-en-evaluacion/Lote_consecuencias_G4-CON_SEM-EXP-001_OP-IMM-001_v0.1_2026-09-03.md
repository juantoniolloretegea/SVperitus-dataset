# Consecuencias G4-CON — SEM-EXP-001 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Puerta:** `G4-CON/SEM-EXP-001`
- **Operación:** `OP-IMM-001`
- **Raíz:** `SEM-EXP-001`
- **Base exacta:** `61e560fe5e88d89b62e8876e2699299fabd89c8e`
- **Dependencia:** `G3-OBS/SEM-EXP-001` v0.1
- **Estatuto:** `CONSECUENCIAS_CANDIDATAS_CERRADAS`
- **Efecto clínico:** ninguno
- **Autorización asistencial:** ninguna

## 0. Objeto

Este artefacto constituye las consecuencias candidatas de identificar de forma incorrecta, incompleta, no vigente o funcionalmente falsa el tratamiento inmunosupresor sistémico primario propuesto.

La cadena exigida es:

```text
observable o U
  -> error de identidad, cobertura, version, papel o estado
  -> daño epistemologico inmediato
  -> operacion o regla posterior afectada
  -> consecuencia para el experto
  -> consecuencia potencial para el paciente, sólo si la evidencia la sostiene
```

No se atribuye daño clínico directamente a un código, un campo ausente o una discrepancia. Las consecuencias clínicas permanecen condicionadas a que el error atraviese controles posteriores y afecte una decisión o actuación.

La adversarial queda integrada. No se crea documentación auxiliar.

## 1. Fuentes aplicadas

| Fuente_ID | Fuente | Corte y localizador | Función |
|---|---|---|---|
| `CON-TXP-SRC-001` | Organización Mundial de la Salud, *Medication Without Harm* | página oficial consultada 03-09-2026; presentación del reto mundial y dominios de seguridad | sostiene que los errores pueden aparecer en prescripción, transcripción, dispensación, administración y monitorización y pueden ocasionar daño grave, discapacidad o muerte; no cuantifica el riesgo de este corte |
| `CON-TXP-SRC-002` | AHRQ PSNet, *Medication Reconciliation* | revisión editorial 15-12-2024; apartados `Background` y `Current Context` | sostiene que listas incompletas o cambios no intencionados pueden producir omisiones, duplicaciones o dosis incorrectas y exponer a acontecimientos adversos; también declara que el efecto clínico y la eficacia generalizable de la conciliación son variables |
| `CON-TXP-SRC-003` | HL7 FHIR R5, `MedicationRequest` | versión 5.0.0, `Boundaries and Relationships` | sostiene la separación entre solicitud u orden y uso comunicado; se utiliza como frontera de transporte, no como evidencia de daño |
| `CON-TXP-SRC-004` | Organización Mundial de la Salud, clasificación Anatómica, Terapéutica y Química | página oficial consultada 03-09-2026, estructura del sistema | sostiene la clasificación de sustancias en grupos y niveles; no sostiene papel primario, indicación o intercambiabilidad |

Enlaces:

- `CON-TXP-SRC-001`: https://www.who.int/initiatives/medication-without-harm
- `CON-TXP-SRC-002`: https://psnet.ahrq.gov/primer/medication-reconciliation
- `CON-TXP-SRC-003`: https://hl7.org/fhir/medicationrequest.html
- `CON-TXP-SRC-004`: https://www.who.int/tools/atc-ddd-toolkit/atc-classification

Las fuentes 1 y 2 sostienen peligro general y tipos de discrepancia. No permiten afirmar que una discrepancia determinada haya causado daño a una persona ni que la corrección documental reduzca por sí sola desenlaces clínicos.

## 2. Clases

| Clase | Alcance |
|---|---|
| `CONSECUENCIA_EPISTEMOLOGICA` | pérdida o falsificación del conocimiento necesario para representar la propuesta |
| `CONSECUENCIA_OPERACIONAL_CANDIDATA` | activación, omisión o bloqueo incorrectos de una regla posterior |
| `CONSECUENCIA_CLINICA_POTENCIAL_NO_ATRIBUIBLE` | daño posible sólo si el error se propaga hasta una decisión o actuación; no predicción ni causalidad individual |

Las tres clases son eslabones, no alternativas compensables. La presencia de un daño epistemológico no prueba que se haya producido daño clínico.

## 3. Consecuencias candidatas

### 3.1. CON-TXP-ID-001 — componente o sustancia equivocados

- **Clase primaria:** `CONSECUENCIA_EPISTEMOLOGICA`.
- **Entrada:** `OBS-TXP-007`–`011`; `U(COMPONENTE_ID)`, `U(SUSTANCIA)`, `U(PRODUCTO)`, `U(FORMA)`, `U(VIA)`.
- **Error:** fusionar componentes, confundir sustancia y producto, ocultar una combinación o adjudicar una vía no demostrada.
- **Daño epistemológico:** el expediente representa otra exposición distinta de la propuesta.
- **Consecuencia para el experto:** aplica o deja de aplicar preguntas, reglas y controles a un agente incorrecto.
- **Consecuencia potencial para el paciente:** evaluación preventiva omitida, innecesaria o mal dirigida; si el error alcanzara prescripción o administración, podría contribuir a daño relacionado con medicamentos.
- **Fuentes:** `CON-TXP-SRC-001`, etapas del uso; `CON-TXP-SRC-002`, omisiones, duplicaciones y dosis incorrectas.
- **Salida máxima:** `U_IDENTIDAD_TRATAMIENTO` o bloqueo de las reglas dependientes.
- **Límite:** no afirma que se haya prescrito o administrado un medicamento erróneo.

### 3.2. CON-TXP-COV-001 — régimen incompleto tratado como completo

- **Clase primaria:** `CONSECUENCIA_EPISTEMOLOGICA`.
- **Entrada:** `OBS-TXP-006` y conjunto de componentes; `U(COBERTURA_REGIMEN)`.
- **Error:** interpretar el silencio en una lista parcial como ausencia de otros tratamientos o utilizar una fuente incompleta como régimen exhaustivo.
- **Daño epistemológico:** se omiten exposiciones, duplicaciones o interacciones potencialmente pertinentes.
- **Consecuencia para el experto:** construye el perfil predecisional sobre un conjunto falso de exposiciones.
- **Consecuencia potencial para el paciente:** una valoración o intervención posterior puede quedar incompleta o resultar innecesaria; el efecto clínico concreto depende del componente omitido y de la decisión afectada.
- **Fuente:** `CON-TXP-SRC-002`, lista completa, omisiones y duplicaciones; la propia fuente declara límites variables de efectividad clínica.
- **Salida máxima:** `U_COBERTURA_REGIMEN`; nunca ausencia clínica inferida.
- **Límite:** no atribuye interacción, toxicidad o infección sin una regla específica.

### 3.3. CON-TXP-VER-001 — versión sustituida, cancelada o no vigente usada como activa

- **Clase primaria:** `CONSECUENCIA_EPISTEMOLOGICA`.
- **Entrada:** `OBS-TXP-002`–`005`, `016`; `U(VERSION_PROPUESTA)`, `U(ESTADO_PROPUESTA)`, `U(INTENCION)`, `U(VIGENCIA)`.
- **Error:** elegir por fecha una propuesta sin enlace de sustitución, conservar una propuesta cancelada o mezclar componentes de versiones distintas.
- **Daño epistemológico:** se fabrica un régimen que nunca estuvo vigente como unidad.
- **Consecuencia para el experto:** evalúa una exposición histórica, cancelada o híbrida como si gobernara el episodio.
- **Consecuencia potencial para el paciente:** retraso, repetición o dirección errónea de evaluaciones posteriores; sólo habrá daño medicamentoso si el error se propaga a una actuación.
- **Fuentes:** `CON-TXP-SRC-001`, errores a lo largo del proceso; `CON-TXP-SRC-003`, separación de estados e intención transportados.
- **Salida máxima:** `U_VERSION_O_VIGENCIA` o bloqueo de reglas dependientes.
- **Límite:** una fecha posterior no prueba sustitución y FHIR no decide vigencia clínica por sí solo.

### 3.4. CON-TXP-ROLE-001 — papel primario falsamente atribuido

- **Clase primaria:** `CONSECUENCIA_OPERACIONAL_CANDIDATA`.
- **Entrada:** `OBS-TXP-012`, `015`; `U(PAPEL_REGIMEN)`, `U(AUTORIDAD)`.
- **Error:** elegir como primario el primer componente, el de mayor dosis, el clasificado en determinado grupo o el más conocido; o forzar unicidad ante una combinación primaria.
- **Daño epistemológico:** la arquitectura adjudica jerarquía clínica sin declaración autorizada.
- **Consecuencia para el experto:** prioriza y ordena preguntas sobre una exposición equivocada y puede relegar componentes codominantes.
- **Consecuencia potencial para el paciente:** perfil de riesgo incompleto o sesgado, con posibles evaluaciones omitidas o innecesarias.
- **Fuentes:** `CON-TXP-SRC-004` sólo clasifica sustancias y no sostiene papel; `CON-TXP-SRC-001` sostiene la relevancia general de errores de medicación.
- **Salida máxima:** `U_PAPEL_PRIMARIO` o `MULTIPLES_PRIMARIOS_DECLARADOS`.
- **Límite:** no declara cuál debe ser el tratamiento principal ni que deba existir uno solo.

### 3.5. CON-TXP-STATE-001 — propuesta, orden y administración confundidas

- **Clase primaria:** `CONSECUENCIA_OPERACIONAL_CANDIDATA`.
- **Entrada:** `OBS-TXP-003`, `004`, `016`; vínculos con eventos reales si existen.
- **Error:** presentar una propuesta como prescrita o administrada, o usar una administración histórica como prueba de inclusión en la propuesta vigente.
- **Daño epistemológico:** se transforma intención en suceso o suceso histórico en intención actual.
- **Consecuencia para el experto:** aplica reglas de exposición real a un plan no ejecutado, o ignora una exposición real porque sólo consulta la propuesta.
- **Consecuencia potencial para el paciente:** evaluación temporal, preventiva o de monitorización incorrecta; el daño concreto requiere una regla y actuación posteriores.
- **Fuentes:** `CON-TXP-SRC-003`, frontera entre solicitud y uso; `CON-TXP-SRC-001`, separación de etapas del uso de medicamentos.
- **Salida máxima:** `U_ESTADO_EJECUCION` o bloqueo localizado.
- **Límite:** no infiere administración, adherencia, efecto ni suspensión.

### 3.6. CON-TXP-CLASS-001 — clasificación farmacológica convertida en verdad clínica

- **Clase primaria:** `CONSECUENCIA_OPERACIONAL_CANDIDATA`.
- **Entrada:** `OBS-TXP-013`, `014`; `U(SISTEMICA)`, `U(INMUNOSUPRESORA)`, `U(CLASIFICACION)`.
- **Error:** utilizar pertenencia ATC, etiqueta comercial o mapa terminológico como demostración suficiente de exposición sistémica, inmunosupresión clínicamente pertinente o equivalencia.
- **Daño epistemológico:** una taxonomía de identidad se transforma en regla clínica sin finalidad, población, vía o autoridad.
- **Consecuencia para el experto:** activa o desactiva rutas utilizando una clasificación que no fue constituida para la operación.
- **Consecuencia potencial para el paciente:** evaluaciones preventivas innecesarias u omitidas; no se atribuye un desenlace concreto.
- **Fuente:** `CON-TXP-SRC-004`, alcance clasificatorio del sistema ATC; `G3-OBS/SEM-EXP-001`, separación de semántica y transporte.
- **Salida máxima:** `U_CLASIFICACION_CLINICA`.
- **Límite:** no niega utilidad de ATC para identidad y agrupación.

## 4. Tabla de conjunción

| Consecuencia_ID | Error | Daño inmediato | Salida máxima G4 |
|---|---|---|---|
| `CON-TXP-ID-001` | identidad farmacológica falsa | exposición equivocada | `U_IDENTIDAD_TRATAMIENTO` |
| `CON-TXP-COV-001` | lista parcial tratada como completa | omisión o duplicación invisible | `U_COBERTURA_REGIMEN` |
| `CON-TXP-VER-001` | propuesta no vigente | régimen histórico o híbrido | `U_VERSION_O_VIGENCIA` |
| `CON-TXP-ROLE-001` | jerarquía inferida | priorización falsa | `U_PAPEL_PRIMARIO` |
| `CON-TXP-STATE-001` | intención convertida en suceso | exposición real o propuesta falsas | `U_ESTADO_EJECUCION` |
| `CON-TXP-CLASS-001` | taxonomía convertida en clínica | activación sin regla | `U_CLASIFICACION_CLINICA` |

No es una ruta. Ninguna fila autoriza una intervención.

## 5. Autoridad y causalidad

1. La autoridad documental puede demostrar identidad y versión; no decide indicación.
2. La autoridad clínica declara el papel en el régimen; el sistema no lo deduce.
3. Un estándar de transporte no crea vigencia, administración ni pertinencia.
4. Un error epistemológico puede no alcanzar nunca al paciente.
5. La consecuencia clínica requiere una cadena adicional: error no interceptado, regla afectada, decisión o actuación y desenlace.
6. La Organización Mundial de la Salud sostiene que los errores de medicación pueden causar daño grave; no prueba que cualquiera de estas seis discrepancias lo cause en un episodio individual.
7. AHRQ declara riesgo de acontecimientos adversos por discrepancias y también incertidumbre sobre el impacto clínico generalizable de las intervenciones de conciliación. Ambos extremos se conservan.

## 6. Procedencia anterior a la conclusión

Toda instancia futura deberá serializar:

```text
<
  Consecuencia_ID,
  Propuesta_ID,
  Version_propuesta,
  Componente_ID_o_conjunto,
  Observable_o_U,
  Error_definido,
  Daño_epistemologico,
  Regla_posterior_afectada,
  Consecuencia_experto,
  Consecuencia_paciente_condicionada,
  Fuente_ID,
  Localizador,
  Limites_causales,
  Horizonte,
  Autoridad,
  Version
>
```

Una cita añadida después no repara una identidad, cobertura, versión, papel o estado no demostrados.

## 7. Adversarial integrada

### A. Error de código igual a daño clínico

**Ataque:** un código incorrecto demuestra lesión.

**Resultado:** rechazado. Primero produce daño epistemológico; el daño clínico exige propagación no interceptada.

### B. Discrepancia siempre dañina

**Ataque:** toda diferencia entre listas causa un acontecimiento adverso.

**Resultado:** rechazado. Puede ser intencionada, irrelevante o interceptada. AHRQ reconoce variabilidad del impacto.

### C. Corrección documental siempre beneficiosa

**Ataque:** conciliar el régimen garantiza mejores desenlaces.

**Resultado:** rechazado. La evidencia generalizable no permite esa afirmación universal.

### D. Clasificación ATC como papel primario

**Ataque:** el grupo determina jerarquía.

**Resultado:** rechazado. ATC clasifica sustancias; no declara función en una propuesta.

### E. FHIR como prueba de administración

**Ataque:** `MedicationRequest` demuestra uso real.

**Resultado:** rechazado por la frontera oficial del recurso.

### F. Versión más reciente por reloj

**Ataque:** seleccionar el documento de fecha mayor.

**Resultado:** rechazado. Hace falta enlace de sustitución y vigencia.

### G. Régimen parcial igual a completo

**Ataque:** ausencia de un componente se interpreta como `0`.

**Resultado:** rechazado. Produce `U_COBERTURA_REGIMEN`.

### H. Un único primario forzado

**Ataque:** reducir una combinación codominante a un componente.

**Resultado:** rechazado. Se conserva pluralidad o `U`.

### I. Medicamento identificado igual a inmunosupresor pertinente

**Ataque:** identidad farmacológica activa directamente una ruta clínica.

**Resultado:** rechazado. Falta clasificación clínica con finalidad y autoridad.

### J. Propuesta convertida en exposición real

**Ataque:** intención equivale a suceso.

**Resultado:** rechazado. Activa `CON-TXP-STATE-001`.

### K. Consecuencia para el experto omitida

**Ataque:** registrar sólo un posible daño al paciente.

**Resultado:** rechazado. Cada consecuencia identifica pérdida de información, priorización falsa o regla contaminada para el experto.

### L. Consecuencia clínica decorativa

**Ataque:** añadir “podría causar daño” sin cadena.

**Resultado:** rechazado. Deben existir regla afectada, decisión o actuación y límites causales.

### M. Bloqueo global

**Ataque:** una `U` de producto detiene toda `OP-IMM-001`.

**Resultado:** rechazado. Sólo bloquea dependencias que requieran ese objeto; criticidad global pertenece a G7.

### N. Determinismo igual a validez

**Ataque:** la misma clasificación reproducida es clínicamente correcta.

**Resultado:** rechazado. Reproducción y validez se comprueban por separado.

### O. Consecuencias usadas ya como ruta

**Ataque:** `CON-TXP-*` ordena una prueba, vacuna, profilaxis o cambio terapéutico.

**Resultado:** rechazado. Son candidatas para atomicidad y usos posteriores.

**Dictamen adversarial integrado:** `PASA`.

## 8. Recuentos

| Magnitud | Valor |
|---|---:|
| consecuencias candidatas | 6 |
| epistemológicas primarias | 3 |
| operacionales candidatas primarias | 3 |
| afirmaciones de causalidad individual | 0 |
| intervenciones | 0 |
| parámetros | 0 |
| matrices, rutas o frames | 0 |
| documentos auxiliares | 0 |

Toda consecuencia operacional conserva daño epistemológico previo. Las consecuencias potenciales para el paciente son condicionadas y no atribuibles en este corte.

## 9. Regla de cierre

`G4-CON/SEM-EXP-001` cierra si:

1. existen exactamente seis consecuencias;
2. identidad, cobertura, versión, papel, estado y clasificación permanecen separadas;
3. cada consecuencia contiene efecto para el experto;
4. ningún dato ausente se convierte directamente en daño consumado;
5. WHO y AHRQ se citan con sus límites;
6. FHIR y ATC no se presentan como autoridades clínicas;
7. propuesta y administración no se fusionan;
8. procedencia precede a la conclusión;
9. reproducción, privacidad y finitud pasan;
10. no se constituye parámetro, intervención, matriz, ruta o frame.

## 10. Efecto

```text
G3-OBS/SEM-EXP-001 = CERRADA
G4-CON/SEM-EXP-001 = CERRADA
G5-ATM/SEM-EXP-001 = NO_ABIERTA
A0 = {PAR-GC-PLAN-SYS-001}
```

La siguiente puerta es `G5-ATM/SEM-EXP-001`. Deberá decidir si «tratamiento primario identificado» es parámetro, control, puente o compuesto, sin convertir identidad farmacológica en evaluación clínica.
