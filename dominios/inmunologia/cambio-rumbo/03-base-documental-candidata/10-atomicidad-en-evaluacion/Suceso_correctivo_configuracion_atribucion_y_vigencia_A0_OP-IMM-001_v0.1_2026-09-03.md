# Suceso correctivo de configuración y vigencia — A0 / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Base exacta:** `2f3492d34807c745bed981005b143656fe17da0b`
- **Operación:** `OP-IMM-001`
- **Entrada:** `|A0| = 20`
- **Naturaleza:** corrección material append-only
- **Efecto:** conserva los veinte tipos atómicos; restringe su capacidad de emitir `0/1`
- **Puertas posteriores:** `G6-MAT` y `G7-RUT` no abiertas
- **Efecto clínico:** ninguno

## 0. Defecto corregido

La revisión externa mostró una diferencia que el expediente precedente no hacía suficientemente fuerte:

```text
OPERANDO_EXPLICITO =/= CONFIGURACION_CLINICAMENTE_ADMISIBLE
DETERMINISMO =/= VALIDEZ
PAQUETE_COMPLETO_PERO_NO_ADMITIDO -> U
PAQUETE_MALFORMADO_O_NO_REPRODUCIBLE -> EJECUCION_TECNICA_NO_VALIDA
```

Una tabla, ventana, taxonomía, escala o lógica aportada por la entrada no se vuelve clínicamente admisible por ser explícita. Este suceso fija el cierre fail-safe. No inventa umbrales ni convierte una fuente bibliográfica en transductor.

## 1. Regla transversal de paquetes

Todo transductor configurable de `A0` recibe un `PaqueteConfiguracion_v` canónico:

```text
PaqueteConfiguracion_v = <
  Paquete_ID,
  Objeto_clinico,
  Fuente_ID,
  Titulo,
  Version_o_fecha,
  Localizador_exacto,
  Poblacion,
  Finalidad,
  Criterios_de_aplicabilidad,
  Entradas_requeridas,
  Regla_operacional,
  Estados_admisibles,
  Regla_de_U,
  Autoridad_de_adopcion,
  SHA256_contenido_canonico
>
```

Sólo puede ejecutarse un paquete cuyo `Paquete_ID` figure en el registro cerrado del parámetro y cuyo contenido coincida con su huella. Un paquete ausente del registro, aunque sea íntegro y determinista, produce `U_CONFIGURACION_NO_ADMITIDA`. La ausencia clínica de un operando produce `U`; la imposibilidad técnica de cargar, validar o reproducir un paquete registrado produce `EJECUCION_TECNICA_NO_VALIDA`. Ninguno de esos estados puede convertirse en `0`.

Los registros pueden ampliarse únicamente mediante versión append-only posterior. En este corte no existe admisión por semejanza, autoridad aparente, popularidad, etiqueta, texto libre ni paquete aportado ad hoc.

## 2. Atribución infección → ingreso o soporte orgánico

Para `PAR-INF-HOSP-HIST-001` y `PAR-INF-ORGSUP-HIST-001`, la relación admisible es:

```text
REL-ATRIB-v0.1 = <
  Relacion_ID,
  Episodio_infeccioso_ID,
  Destino_ID,
  Tipo = MOTIVO_DE_INGRESO | SOPORTE_REQUERIDO_POR_EPISODIO,
  Asercion_o_campo_fuente,
  Autor_profesional,
  Fecha,
  Procedencia,
  Version
>
```

Puede constituir el enlace:

1. una referencia estructurada desde `Encounter.reason.value` al objeto infeccioso, cuando el uso y el perfil local versionado declaren motivo de ingreso; o
2. una aserción clínica profesional explícita, firmada y trazable, que relacione el episodio con el ingreso o con una modalidad identificada de soporte.

No constituyen atribución: proximidad temporal; aparición en el mismo encuentro; `Encounter.diagnosis` sin uso causal; diagnóstico principal de facturación; estancia en UCI; gravedad textual; antibiótico; oxígeno aislado; ni inferencia del motor.

```text
RELACION_ADMISIBLE_Y_VERIFICADA -> puede evaluar 1
COBERTURA_COMPLETA_SIN_RELACION -> puede evaluar 0
CUALQUIER_OTRO_CASO -> U_ATRIBUCION
```

FHIR R5 se usa como estructura de transporte, no como prueba automática de causalidad:
https://hl7.org/fhir/R5/encounter.html

## 3. Clasificación documental de infección oportunista

`PAR-OI-DOC-HIST-001` conserva su identidad documental. No diagnostica oportunismo.

El registro inicial de sistemas clasificatorios ejecutables queda deliberadamente cerrado y vacío:

```text
REG-OI-ADM-v0.1 = {}
```

Hasta que una versión posterior incorpore una clasificación profesional con población, contexto del huésped, taxonomía, versión, localizador y huella, el parámetro no puede emitir `0` ni `1` por ejecución automática.

Una nota profesional previa puede conservarse como evidencia candidata, pero no entra automáticamente en el registro. Texto libre no tipado, lista universal de microorganismos, código aislado, inferencia por huésped y clasificación generada por IA producen `U_CLASIFICACION_OI_NO_ADMITIDA`.

```text
PAR-OI-DOC-HIST-001 = PARAMETRO_ATOMICO_DOCUMENTAL_CON_CONFIGURACION_PENDIENTE
CAPACIDAD_0_1_AUTOMATICA = BLOQUEADA
```

Esta restricción no elimina el tipo de `A0`; impide que una etiqueta clínicamente abierta sea tratada como transductor ya autorizado.

## 4. Colonización por microorganismo multirresistente

Para `PAR-MDRO-COL-DOC-001` se separan dos paquetes:

```text
TABLA_MDRO_v = <PaqueteConfiguracion_v, microorganismos, mecanismos_o_fenotipos,
                metodo_admisible, taxonomia, reglas_de_coincidencia>
VENTANA_COLONIZACION_v = <PaqueteConfiguracion_v, punto_indice,
                          inicio, fin, inclusividad, excepciones>
```

El directorio ECDC previamente citado sólo localiza posibles fuentes; no constituye una tabla ni una ventana. Por tanto:

```text
REG-MDRO-TABLA-ADM-v0.1 = {}
REG-MDRO-VENTANA-ADM-v0.1 = {}
```

Sin ambos paquetes registrados no se emite `0` ni `1`: se obtiene `U_REGLA_MDRO_NO_CONSTITUIDA`. Un paquete registrado con huella errónea, tabla ilegible o versión incoherente produce `EJECUCION_TECNICA_NO_VALIDA`.

Colonización, infección, contaminación y resistencia permanecen separadas. La ausencia de hallazgo sólo puede producir `0` cuando, además de los paquetes, exista cobertura de cribado explícita y suficiente.

Fuente de orientación no operacionalizada:
https://www.ecdc.europa.eu/en/publications-data/directory-guidance-prevention-and-control/antimicrobial-resistance

## 5. Evaluación diagnóstica de malnutrición

El consenso GLIM queda identificado como fuente clínica primaria:

- Cederholm T, et al. *GLIM criteria for the diagnosis of malnutrition – A consensus report from the global clinical nutrition community*. Clinical Nutrition. 2019;38:1–9.
- DOI: https://doi.org/10.1016/j.clnu.2018.08.002
- Texto público: https://pmc.ncbi.nlm.nih.gov/articles/PMC6438340/

GLIM exige una evaluación diagnóstica posterior al cribado y, para el diagnóstico, al menos un criterio fenotípico y uno etiológico. Sin embargo, el artículo no constituye por sí solo una implementación: método de masa muscular, unidades, puntos de corte, población y reglas de aplicabilidad deben fijarse en el paquete exacto.

```text
REG-NUT-DX-ADM-v0.1 = {}
```

Hasta adoptar una implementación completa y reproducible, `PAR-MALNUTRITION-ASSESS-POS-001` conserva el tipo pero emite `U_INSTRUMENTO_NUTRICIONAL_NO_ADMITIDO`. MUST, NRS-2002 u otro cribado positivo no sustituyen el diagnóstico; IMC, pérdida ponderal, ingesta o inflamación aislados tampoco.

```text
PAR-MALNUTRITION-ASSESS-POS-001 =
  PARAMETRO_ATOMICO_COMPARATIVO_CON_CONFIGURACION_PENDIENTE
CAPACIDAD_0_1_AUTOMATICA = BLOQUEADA
```

## 6. Vigencia transversal de la familia ACTIVE

Para `PAR-DM-DOC-ACTIVE-001`, `PAR-HF-DOC-ACTIVE-001`, `PAR-CKD-DOC-ACTIVE-001`, `PAR-KRT-ACTIVE-001`, `PAR-BRONCHIECTASIS-DOC-ACTIVE-001`, `PAR-RESP-SUPPORT-ACTIVE-001` y `PAR-CIRRHOSIS-DOC-ACTIVE-001`:

```text
ACTIVE_v0.1(X,t0) = 1
  sólo si existe objeto verificado, no entered-in-error,
  con estado clínico activo en t0 o sin resolución cuando
  la semántica versionada de la condición admite persistencia.

ACTIVE_v0.1(X,t0) = 0
  sólo si existe cobertura explícita suficiente y el objeto
  consta resuelto/inactivo o no existe dentro del inventario cubierto.

ACTIVE_v0.1(X,t0) = U
  si faltan estado, t0, verificación, semántica temporal,
  resolución, cobertura, procedencia o hay conflicto.
```

No se fija una ventana universal para enfermedades crónicas. El horizonte `h` determina la validez de la evidencia, no borra automáticamente una condición. Para KRT y soporte respiratorio, la actividad exige prestación vigente o plan activo explícito; un acceso, dispositivo, prescripción histórica o uso puntual no bastan.

FHIR `Condition.clinicalStatus`, `verificationStatus`, inicio y resolución son vehículos posibles; su mera presencia no sustituye el perfil local ni la adjudicación profesional:
https://hl7.org/fhir/R5/condition.html

## 7. No compensación y futura propiedad matricial

ERC y KRT permanecen parámetros distintos porque pueden divergir. Bronquiectasias y soporte respiratorio también. La futura G6 deberá asignar propietario único a cada parámetro; la futura G7 deberá impedir que la coocurrencia se sume como dos copias del mismo mecanismo o que una `U` se compense. Este suceso no anticipa matriz, peso ni ruta.

## 8. Adversarial integrada

| Ataque | Resultado |
|---|---|
| aportar una tabla arbitraria pero completa | `U_CONFIGURACION_NO_ADMITIDA` |
| cambiar bytes conservando el mismo ID | `EJECUCION_TECNICA_NO_VALIDA` |
| diagnóstico principal = causa de ingreso | rechazado |
| UCI = soporte atribuido | rechazado |
| microorganismo de una lista = oportunismo | rechazado |
| directorio ECDC = tabla MDRO | rechazado |
| cribado nutricional = diagnóstico GLIM | rechazado |
| código ACTIVE sin estado ni cobertura = 1 | rechazado |
| ausencia documental = 0 | rechazado |
| resolver incertidumbre técnica como U clínica | rechazado |
| bajar `|A0|` por configuración pendiente | rechazado: el tipo y su ejecutabilidad son planos distintos |
| abrir G6 desde este correctivo | rechazado |

**Dictamen adversarial:** `PASA`.

## 9. Efecto exacto

```text
|A0| = 20
TIPOS_ELIMINADOS = 0
PAR-OI-DOC-HIST-001 = CONFIGURACION_PENDIENTE
PAR-MDRO-COL-DOC-001 = CONFIGURACION_PENDIENTE
PAR-MALNUTRITION-ASSESS-POS-001 = CONFIGURACION_PENDIENTE
PAR-INF-HOSP-HIST-001 = ATRIBUCION_TIPADA_OBLIGATORIA
PAR-INF-ORGSUP-HIST-001 = ATRIBUCION_TIPADA_OBLIGATORIA
FAMILIA_ACTIVE = VIGENCIA_TRANSVERSAL_TIPADA
G6-MAT = NO_ABIERTA
G7-RUT = NO_ABIERTA
APTITUD_CLINICA_OP-IMM-001 = NO_DECLARADA
```

La corrección cierra el riesgo de aceptar configuraciones arbitrarias; no finge que las configuraciones clínicas aún ausentes hayan sido constituidas.
