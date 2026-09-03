# Suceso correctivo de consolidación A0 — criterios clínicos no ligados / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Rama:** `dominio-inmunologia`
- **Base exacta:** `1dd4236e72e2b9f9b8dec9bd371f71c327138f0f`
- **Objeto afectado:** `Expediente_iterativo_constitutivo_G3-G5_SEM-HUE-002_a_SEM-BAR-004_OP-IMM-001_v0.1_2026-09-03.md`
- **Puerta:** reparación append-only de `G5-ATM`
- **Estatuto:** `CORRECCION_MATERIAL_CERRADA`
- **Efecto clínico:** ninguno
- **Autorización asistencial:** ninguna

## 0. Motivo y efecto

La revisión externa comparada detectó que cuatro proposiciones clínicamente separables habían sido contadas como parámetros adoptados aunque sus transductores remitían a un «criterio autorizado y versionado» sin `Fuente_ID`, localizador, versión, población y regla operacional ligados.

Una fuente que demuestra pertinencia del objeto no constituye necesariamente el criterio que permite decidirlo. En consecuencia:

```text
FUENTE_REAL != TRANSDUCTOR_CLINICO_CONSTITUIDO
PROPOSICION_ATOMICA_CANDIDATA != PARAMETRO_AUTORIZADO_EN_A0
```

Este suceso no reescribe ni elimina el antecedente. Lo conserva como estado histórico y sustituye prospectivamente sólo sus cuatro adjudicaciones defectuosas y el recuento derivado de `A0`.

## 1. Comprobación de los cuatro objetos

### 1.1. Respuesta humoral específica

Objeto anterior: `PAR-HUM-SPEC-ALTER-001`.

La bibliografía confirma que una respuesta específica puede diferir de la concentración total de inmunoglobulinas, pero también que no existe una definición uniforme de título protector y que la interpretación depende de vacuna, antígeno, serotipo, método, cronología, población y finalidad. La fuente CDC citada en el expediente enumera los anticuerpos específicos como pruebas útiles, pero no proporciona el transductor general declarado.

```text
CAND-HUM-SPEC-ALTER-001 = U_REQUIERE_REGLA
PAR-HUM-SPEC-ALTER-001 = NO_ADOPTADO
```

No se sustituye el hueco por un diagnóstico textual ni por una etiqueta del laboratorio.

### 1.2. Pérdida funcional esplénica

Objeto anterior: `PAR-SPL-FUNC-LOSS-001`.

La asplenia funcional es materialmente distinta de la ausencia anatómica. Sin embargo, las fuentes describen métodos no equivalentes —cuerpos de Howell–Jolly, recuento de eritrocitos con depresiones y técnicas de medicina nuclear— con sensibilidades, umbrales y ámbitos diferentes. CDC reconoce la condición y sus consecuencias preventivas, pero no constituye un transductor diagnóstico general.

```text
CAND-SPL-FUNC-LOSS-001 = U_REQUIERE_REGLA
PAR-SPL-FUNC-LOSS-001 = NO_ADOPTADO
```

`PAR-SPL-ANAT-ABS-001` permanece intacto. Anatomía y función no se fusionan.

### 1.3. Pérdida de integridad cutánea

Objeto anterior: `PAR-SKIN-BARRIER-LOSS-001`.

FHIR `Observation` permite transportar región, tiempo, método, valor, interpretación y procedencia. No determina qué extensión, profundidad, lesión, cobertura corporal o finalidad constituye una «pérdida pertinente» para `OP-IMM-001`. El expediente no ligó otro criterio profesional.

```text
CAND-SKIN-BARRIER-LOSS-001 = U_REQUIERE_REGLA
PAR-SKIN-BARRIER-LOSS-001 = NO_ADOPTADO
```

La estructura G3 y las consecuencias G4 permanecen válidas.

### 1.4. Pérdida de integridad mucosa

Objeto anterior: `PAR-MUCOSA-BARRIER-LOSS-001`.

No existe en las fuentes ligadas una regla que transforme de manera general territorio, tipo, extensión y temporalidad en pérdida mucosa pertinente. Las definiciones de lesión de barrera mucosa empleadas para vigilancia de infecciones del torrente sanguíneo son finalistas y poblacionales; no pueden transportarse como definición universal del estado mucoso basal.

```text
CAND-MUCOSA-BARRIER-LOSS-001 = U_REQUIERE_REGLA
PAR-MUCOSA-BARRIER-LOSS-001 = NO_ADOPTADO
```

La separación piel/mucosa permanece constituida.

## 2. Objetos conservados

Permanecen adoptados porque poseen una operación documental o cuantitativa decidible y `U` explícita:

| Orden vigente | Parametro_ID | Operación decidible |
|---:|---|---|
| 1 | `PAR-GC-PLAN-SYS-001` | inclusión documentada en plan completo y versionado |
| 2 | `PAR-IGG-DEF-Q-001` | comparación con límite inferior aplicable y versionado |
| 3 | `PAR-SPL-ANAT-ABS-001` | ausencia anatómica completa documentada y verificada |
| 4 | `PAR-ANC-DEF-Q-001` | comparación con límite inferior aplicable y versionado |
| 5 | `PAR-IV-DEVICE-PRESENT-001` | presencia vigente en inventario de cobertura explícita |
| 6 | `PAR-IMPLANT-PRESENT-001` | presencia vigente en inventario de cobertura explícita |

Para dispositivo e implante:

```text
COBERTURA_COMPLETA_NO_DECLARADA -> 0 INADMISIBLE; U OBLIGATORIA
```

No se predice que `U` sea empíricamente dominante; su frecuencia corresponde a `G9-EMP`.

## 3. Residuales identificados

| Residual_ID | Objeto | Estado |
|---|---|---|
| `RES-IGG-EXC-001` | concentración de IgG superior al límite superior aplicable | `RESIDUAL_PARA_VERSION_POSTERIOR` |
| `RES-ANC-EXC-001` | ANC superior al límite superior aplicable | `REFERENCIA_A_SEM-RUT-001_O_RESIDUAL_POSTERIOR` |

Los identificadores permiten recuperación posterior sin convertir los residuales en parámetros ni raíces nuevas.

## 4. Adversarial integrada

| Ataque | Resultado |
|---|---|
| conservar diez por cuota | rechazado; `A0` baja a seis |
| convertir la etiqueta clínica en transductor | rechazado; una afirmación no reemplaza la regla ausente |
| escoger un método esplénico como universal | rechazado; diferencias de sensibilidad y finalidad permanecen |
| transportar una definición de vigilancia a integridad mucosa general | rechazado |
| borrar el expediente antecedente | rechazado; corrección append-only |
| invalidar G3/G4 por el defecto de G5 | rechazado; observables y consecuencias continúan separados |
| convertir residual en raíz 33 | rechazado; `Q0` permanece en 32 |
| tratar `U` local como NO GO | rechazado; criticidad no abierta |

**Dictamen:** `PASA`.

## 5. Estado corregido

```text
A0 = {
  PAR-GC-PLAN-SYS-001,
  PAR-IGG-DEF-Q-001,
  PAR-SPL-ANAT-ABS-001,
  PAR-ANC-DEF-Q-001,
  PAR-IV-DEVICE-PRESENT-001,
  PAR-IMPLANT-PRESENT-001
}

|A0| = 6
CANDIDATOS_EN_U_REQUIERE_REGLA = 4
RESIDUALES_IDENTIFICADOS = 2
SIGUIENTE_RAIZ = SEM-HIS-001
G6-MAT = NO_ABIERTA
G7-RUT = NO_ABIERTA
```

## 6. Fuentes consultadas para la corrección

- CDC. *Altered Immunocompetence*. https://www.cdc.gov/vaccines/hcp/imz-best-practices/altered-immunocompetence.html
- Perez E, Bonilla FA, Orange JS, Ballow M. *Specific Antibody Deficiency: Controversies in Diagnosis and Management*. Frontiers in Immunology. 2017;8:586. https://pmc.ncbi.nlm.nih.gov/articles/PMC5439175/
- Kirkineska L, Perifanis V, Vasiliadis T. *Functional hyposplenism*. Hippokratia. 2014;18(1):7–11. https://pmc.ncbi.nlm.nih.gov/articles/PMC4103047/
- HL7. *FHIR R5 Observation*. https://hl7.org/fhir/R5/observation.html
- CDC/NHSN. Material sobre `MBI-LCBI`; usado sólo para demostrar finalidad específica, no como criterio general de integridad mucosa. https://stacks.cdc.gov/view/cdc/79237

La corrección no adopta ningún umbral, diagnóstico o intervención de estas fuentes.
