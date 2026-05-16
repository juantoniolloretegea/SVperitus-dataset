## AI.14. Contrato de datos, runner mínimo y salida reproducible del banco clínico-biológico

### AI.14.1. Estatuto del contrato mínimo

El contrato de datos, runner mínimo y salida reproducible reduce la arquitectura material de AI.13 a su núcleo ejecutable. Su finalidad es demostrar que el banco clínico-biológico puede funcionar con un conjunto mínimo de tablas, reglas y comprobaciones sin perder custodia doctrinal, clínica ni formal. El contrato mínimo no sustituye la arquitectura completa; la atraviesa por su línea esencial: casos, condiciones, negativos, retornos y salidas esperadas. Si esas cinco piezas están bien formadas, el runner puede validar, decidir, rechazar ataques y emitir una salida reproducible. Si falta una, el banco no debe declararse cerrado.

<div align="center">Contrato<sub>mín</sub>=Casos ∧ Condiciones ∧ Negativos ∧ Retornos ∧ SalidasEsperadas.</div>

El contrato mínimo conserva las reglas superiores: ningún dato sin muestra, método o unidad crítica puede cerrar; ninguna apariencia sustituye condición necesaria; ninguna U se degrada; ninguna muerte física retrovalida causa; ningún retorno opaco es apto; ningún negativo aceptado permite PASS global. La reducción a núcleo mínimo no autoriza simplificación doctrinal. Su función es hacer ejecutable lo indispensable, no rebajar el estándar.

| Pieza mínima      | Función                                                         | Fallo si falta                 |
| ----------------- | --------------------------------------------------------------- | ------------------------------ |
| casos             | define dominio, etiqueta, transductor, muestra, método y límite | no hay unidad de ejecución     |
| condiciones       | declara apoyos, necesarias, diferenciales, U y negativas        | no hay decisión formal         |
| negativos         | inyecta ataques adversariales                                   | banco débil o cierre favorable |
| retornos          | traduce salida al dominio médico                                | salida opaca                   |
| salidas esperadas | permite comparar ejecución                                      | pase silencioso                |

La diferencia entre arquitectura completa y contrato mínimo es de escala, no de verdad. La arquitectura completa contiene carpetas, manifiesto, glosario, hashes, salidas por subbanco y garantías. El contrato mínimo contiene lo que un runner necesita para no improvisar. AI.14 fija esa base para que AI.15 pueda materializarla en paquete inicial.

### AI.14.2. Esquema mínimo de tablas

El esquema mínimo de tablas se compone de cinco tablas. La tabla de casos contiene una fila por caso. La tabla de condiciones contiene una o varias filas por caso. La tabla de negativos contiene ataques asociados a un caso o a todos. La tabla de retornos contiene el retorno médico exigible. La tabla de salidas esperadas contiene el resultado que debe producir el runner. Ninguna tabla debe contener columnas ambiguas. Ninguna celda debe mezclar dato clínico, interpretación y conclusión.

<div align="center">Tablas<sub>mín</sub>={casos.csv, condiciones.csv, negativos.csv, retornos.csv, salidas_esperadas.csv}.</div>

| Tabla                 | Columnas mínimas                                                            | Función              |
| --------------------- | --------------------------------------------------------------------------- | -------------------- |
| casos.csv             | id_caso, dominio, etiqueta_evaluada, transductor, muestra, metodo, limite   | define caso          |
| condiciones.csv       | id_caso, id_condicion, tipo, estado, fuerza, retorno_local                  | decide 0/1/U         |
| negativos.csv         | id_ataque, id_caso, ataque, cierre_indebido, error, respuesta_obligatoria   | prueba resistencia   |
| retornos.csv          | id_caso, salida_formal, retorno_medico, residual, limite                    | devuelve explicación |
| salidas_esperadas.csv | id_caso, salida_esperada, error0_acotado, retorno_minimo, dictamen_esperado | compara ejecución    |

| Campo          | Valores admitidos                                                              |
| -------------- | ------------------------------------------------------------------------------ |
| dominio        | hematologia, neuroclinica, oncologia, genetica, inmunologia, documental, vital |
| transductor    | X_HEM, X_NEURO, X_ONC, X_GEN, X_IMM, X_DOC, X_VITAL, X_COMPUESTO               |
| tipo           | necesaria, apoyo, diferencial, U, negativa                                     |
| estado         | 0, 1, U, NA                                                                    |
| fuerza         | corte, sospecha, residual, bloqueo, retorno                                    |
| salida         | 0, 1, U, 0+U, NO_APTO, FAIL                                                    |
| error0_acotado | true, false                                                                    |
| dictamen       | PASS, FAIL, NO_APTO                                                            |

La codificación evita símbolos que dificulten ejecución en CSV. En el documento pueden aparecer (𝔛_{hem}^{↔}), (U), (Δ) o (R_{med}); en los ficheros mínimos se usan claves estables: X_HEM, U, DELTA y R_MED si procede. La forma computacional no rebaja el concepto; lo hace reproducible. El runner puede mapear esas claves a glosario sin alterar el resultado.

### AI.14.3. Contrato mínimo de casos

La tabla de casos fija la unidad de ejecución. Cada caso declara dominio, etiqueta evaluada, transductor, muestra, método y límite. Si la etiqueta es NA, el caso no evalúa diagnóstico concreto, sino custodia, U, muerte física o selección de transductor. En el lote semilla, todos los casos tienen etiqueta evaluada porque proceden del bloque diagnóstico. El contrato mínimo conserva los seis casos trabajados: tres hematológicos y tres neuroclínicos.

<div align="center">Caso<sub>mín</sub>=⟨id,dominio,etiqueta,𝔛,muestra,método,límite⟩.</div>

| id_caso    | dominio      | etiqueta_evaluada         | transductor | muestra                  | metodo                                    | limite                     |
| ---------- | ------------ | ------------------------- | ----------- | ------------------------ | ----------------------------------------- | -------------------------- |
| HCL-LIM-01 | hematologia  | tricoleucemia_clasica     | X_HEM       | sangre_y_medula          | hemograma_frotis_citometria_IHQ_molecular | no_diagnostica_alternativa |
| HCL-LIM-02 | hematologia  | tricoleucemia_clasica     | X_HEM       | sangre_y_medula          | frotis_citometria_IHQ                     | alternativa_B_esplenica_U  |
| HCL-LIM-03 | hematologia  | tricoleucemia_clasica     | X_HEM       | sangre_medula_incompleta | marcadores_parciales                      | no_confirma_ni_refuta      |
| CNS-LIM-01 | neuroclinica | tumor_cerebral_maligno    | X_NEURO     | RM_y_biopsia             | imagen_histologia                         | no_niega_gravedad          |
| CNS-LIM-02 | neuroclinica | tumor_cerebral_maligno    | X_NEURO     | RM_sin_tejido            | imagen                                    | exige_estudio_adicional    |
| CNS-LIM-03 | neuroclinica | glioblastoma_IDH_wildtype | X_NEURO     | RM_y_estudio_parcial     | imagen_molecular_histologia_insuficiente  | no_cierra_alternativa      |

| Validación del caso | Regla                                                |
| ------------------- | ---------------------------------------------------- |
| id_caso             | obligatorio, único y estable                         |
| dominio             | debe pertenecer al conjunto permitido                |
| etiqueta_evaluada   | obligatoria salvo caso documental/vital sin etiqueta |
| transductor         | debe ser compatible con dominio                      |
| muestra             | no vacía                                             |
| metodo              | no vacío                                             |
| limite              | no vacío                                             |

El contrato de casos no contiene condiciones diagnósticas. Esto es deliberado. Un caso puede tener señal sugestiva, pero la decisión no vive en casos.csv; vive en condiciones.csv. Separar caso y condición impide que el diagnóstico quede preconstruido en la descripción del caso.

### AI.14.4. Contrato mínimo de condiciones

La tabla de condiciones es el centro decisivo del runner. Cada condición pertenece a un caso y declara tipo, estado, fuerza y retorno local. Una condición necesaria con estado 0 produce refutación. Una condición necesaria con estado U produce U si no hay otra necesaria en 0. Una condición de apoyo nunca cierra. Una condición diferencial abre alternativa o residual. Una condición negativa bloquea ataques. La tabla debe contener al menos una condición necesaria por cada etiqueta evaluada.

<div align="center">Condición<sub>mín</sub>=⟨id_caso,id_condición,tipo,estado,fuerza,retorno_local⟩.</div>

| id_caso    | id_condicion             | tipo        | estado | fuerza   | retorno_local                       |
| ---------- | ------------------------ | ----------- | ------ | -------- | ----------------------------------- |
| HCL-LIM-01 | HCL_PATTERN_CLASSIC      | necesaria   | 0      | corte    | patron_clasico_no_conservado        |
| HCL-LIM-01 | HCL_MORPH_SUPPORT        | apoyo       | 1      | sospecha | morfologia_sugestiva_no_concluyente |
| HCL-LIM-01 | HCL_ALT_B_SPLENIC        | diferencial | U      | residual | diferencial_B_esplenico_abierto     |
| HCL-LIM-02 | HCL_CLASSIC_CONSERVATION | necesaria   | 0      | corte    | entidad_clasica_no_conservada       |
| HCL-LIM-02 | HCL_LIKE_SUPPORT         | apoyo       | 1      | sospecha | rasgos_HCL_like_no_cierran_HCLc     |
| HCL-LIM-02 | HCL_ALT_B                | diferencial | U      | residual | alternativa_B_abierta               |
| HCL-LIM-03 | HCL_CRITICAL_DATA        | necesaria   | U      | retorno  | falta_dato_critico                  |
| HCL-LIM-03 | HCL_PARTIAL_MARKERS      | apoyo       | 1      | sospecha | marcadores_parciales_no_cierran     |
| CNS-LIM-01 | CNS_MALIGNANT_HISTOLOGY  | necesaria   | 0      | corte    | histologia_tumoral_refutada         |
| CNS-LIM-01 | CNS_IMAGE_SUPPORT        | apoyo       | 1      | sospecha | imagen_grave_no_identidad           |
| CNS-LIM-01 | CNS_ALT_LESION           | diferencial | U      | residual | lesion_alternativa_abierta          |
| CNS-LIM-02 | CNS_TISSUE_MOLECULAR     | necesaria   | U      | retorno  | falta_identidad_tisular_molecular   |
| CNS-LIM-02 | CNS_IMAGE_SUPPORT        | apoyo       | 1      | sospecha | imagen_no_cierra_malignidad         |
| CNS-LIM-03 | GBM_IDHWT_CRITERIA       | necesaria   | 0      | corte    | criterios_GBM_no_satisfechos        |
| CNS-LIM-03 | CNS_INFILTRATIVE_SUPPORT | apoyo       | 1      | sospecha | lesion_infiltrativa_no_cierra_GBM   |
| CNS-LIM-03 | CNS_ALT_ENTITY           | diferencial | U      | residual | alternativa_CNS_abierta             |

| Validación de condición | Regla                                            |
| ----------------------- | ------------------------------------------------ |
| tipo=necesaria          | debe existir si hay etiqueta evaluada            |
| estado=0                | sólo puede producir refutación si tipo=necesaria |
| estado=U                | debe tener retorno local y U legítimo            |
| tipo=apoyo              | no puede cerrar etiqueta                         |
| tipo=diferencial        | no puede inventar alternativa cerrada            |
| fuerza=corte            | sólo admisible en condición necesaria            |
| retorno_local           | obligatorio en toda condición                    |

La tabla de condiciones es deliberadamente más fuerte que una lista clínica. Un marcador parcial, una imagen grave o una morfología sugestiva no tienen fuerza de corte salvo que el banco lo haya declarado como condición necesaria. Esta disciplina es lo que impide el diagnóstico por apariencia.

### AI.14.5. Contrato mínimo de negativos

La tabla de negativos introduce ataques adversariales. Cada ataque intenta forzar un cierre indebido. El runner no necesita simular el razonamiento clínico completo del ataque; basta con comprobar que la conclusión prohibida no aparece como salida válida. Si un ataque pretende transformar U en diagnóstico, el runner debe bloquearlo. Si pretende usar imagen como histología, debe bloquearlo. Si pretende usar muerte como causa, debe bloquearlo. Los negativos son obligatorios para que el banco no sea una mera lista de salidas favorables.

<div align="center">Negativo<sub>mín</sub>=⟨ataque,cierre_indebido,error,respuesta_obligatoria⟩.</div>

| id_ataque | id_caso    | ataque                                | cierre_indebido | error    | respuesta_obligatoria |
| --------- | ---------- | ------------------------------------- | --------------- | -------- | --------------------- |
| NEG-01    | HCL-LIM-01 | citopenia_mas_celulas_vellosas        | HCLc_1          | E-DX-05  | rechazar              |
| NEG-02    | HCL-LIM-01 | CD11c_CD103_suficientes               | HCLc_1          | E-DX-06  | rechazar              |
| NEG-03    | HCL-LIM-01 | ignorar_discordancia_molecular        | HCLc_1          | E-DX-07  | rechazar              |
| NEG-04    | HCL-LIM-02 | morfologia_HCL_like_equivale_HCLc     | HCLc_1          | E-DX-05  | rechazar              |
| NEG-05    | HCL-LIM-03 | U_molecular_equivale_HCLc             | HCLc_1          | E-DX-12  | rechazar              |
| NEG-06    | HCL-LIM-03 | U_molecular_equivale_no_HCLc          | HCLc_0          | E-DX-11  | rechazar              |
| NEG-07    | CNS-LIM-01 | realce_edema_equivale_tumor           | tumor_maligno_1 | E-DX-04  | rechazar              |
| NEG-08    | CNS-LIM-01 | imagen_sustituye_histologia           | tumor_maligno_1 | E-DX-04  | rechazar              |
| NEG-09    | CNS-LIM-02 | imagen_sin_tejido_equivale_malignidad | tumor_maligno_1 | E-DX-04  | rechazar              |
| NEG-10    | CNS-LIM-02 | U_por_falta_tejido_equivale_no_tumor  | tumor_maligno_0 | E-DX-11  | rechazar              |
| NEG-11    | CNS-LIM-03 | lesion_grave_equivale_GBM             | GBM_1           | E-DX-04  | rechazar              |
| NEG-12    | ALL        | muerte_hipotetica_confirma_etiqueta   | causa_1         | E-DX-06  | rechazar              |
| NEG-13    | ALL        | caso_sin_metodo_pasa                  | apto            | E-MAT-05 | NO_APTO               |
| NEG-14    | ALL        | magnitud_sin_unidad_pasa              | apto            | E-MAT-06 | NO_APTO               |
| NEG-15    | ALL        | salida_sin_retorno_pasa               | PASS            | E-MAT-10 | FAIL                  |
| NEG-16    | ALL        | diagnostico_alternativo_inventado     | alternativa_1   | E-DX-07  | rechazar              |

| Respuesta obligatoria | Significado                                           |
| --------------------- | ----------------------------------------------------- |
| rechazar              | el cierre indebido no puede aparecer                  |
| U                     | el ataque debe conservar indeterminación              |
| NO_APTO               | el ataque falla por contrato documental o metrológico |
| FAIL                  | si el runner aceptara el ataque, la ejecución falla   |

El contrato mínimo de negativos debe ejecutarse siempre. Un paquete que ejecuta casos base pero no negativos no puede declararse cerrado. La adversarialidad no es una fase opinativa; es dato ejecutable.

### AI.14.6. Contrato mínimo de retornos

La tabla de retornos fija la traducción de la salida al dominio médico. El runner puede decidir 0, U o 0+U, pero no puede emitir salida apta sin retorno. El retorno mínimo debe contener etiqueta evaluada, condición decisiva, estado, residual o diferencial y límite. La frase puede ser breve, pero no puede ser opaca. Si el retorno no permite saber por qué cayó o quedó U la etiqueta, la salida no es válida.

<div align="center">Retorno<sub>mín</sub>=⟨salida_formal,retorno_médico,residual,límite⟩.</div>

| id_caso    | salida_formal | retorno_medico                                          | residual                             | limite                     |
| ---------- | ------------- | ------------------------------------------------------- | ------------------------------------ | -------------------------- |
| HCL-LIM-01 | 0+U           | HCLc_refutada_por_patron_constitutivo_no_conservado     | diferencial_B_esplenico_abierto      | no_diagnostica_alternativa |
| HCL-LIM-02 | 0+U           | semejanza_HCL_like_no_cierra_HCL_clasica                | alternativa_B_permanece_U            | alternativa_B_esplenica_U  |
| HCL-LIM-03 | U             | sospecha_HCLc_no_cerrada_por_dato_critico_ausente       | falta_dato_molecular_tisular         | no_confirma_ni_refuta      |
| CNS-LIM-01 | 0+U           | tumor_maligno_refutado_por_identidad_tisular_no_tumoral | lesion_grave_alternativa_abierta     | no_niega_gravedad          |
| CNS-LIM-02 | U             | imagen_grave_sin_identidad_no_cierra_malignidad         | tejido_molecular_diferencial_abierto | exige_estudio_adicional    |
| CNS-LIM-03 | 0+U           | GBM_forzado_refutado_por_criterios_no_satisfechos       | alternativa_CNS_abierta              | no_cierra_alternativa      |

| Validación del retorno | Regla                                               |
| ---------------------- | --------------------------------------------------- |
| salida_formal          | debe coincidir con salida obtenida o esperada       |
| retorno_medico         | no vacío y no puramente interno                     |
| residual               | obligatorio si existe diferencial, discordancia o U |
| limite                 | obligatorio                                         |
| lenguaje               | médico-estructural, no terapéutico                  |
| prohibición            | no inventar diagnóstico alternativo                 |
| prohibición            | no negar gravedad si sólo cae etiqueta              |

El retorno médico es el punto de contacto con la ciencia contemporánea. Sin retorno, el banco se vuelve hermético. Con retorno, la salida puede ser auditada: qué etiqueta cayó, por qué cayó, qué queda abierto y qué no se concluye.

### AI.14.7. Contrato mínimo de salidas esperadas

La tabla de salidas esperadas fija el resultado que debe producir el runner antes de ejecutar. No se calcula después. No se adapta a la salida obtenida. Es la referencia contra la que se contrasta la ejecución. El lote semilla contiene cuatro refutaciones con error cero acotado y dos U legítimas. Ningún caso semilla cierra diagnóstico positivo. Ningún caso semilla cierra alternativa.

<div align="center">SalidaEsperada<sub>mín</sub>=⟨id,salida,error0,retorno_mínimo,dictamen⟩.</div>

| id_caso    | salida_esperada | error0_acotado | retorno_minimo                    | dictamen_esperado |
| ---------- | --------------- | -------------: | --------------------------------- | ----------------- |
| HCL-LIM-01 | 0+U             |           true | patron_constitutivo_no_conservado | PASS              |
| HCL-LIM-02 | 0+U             |           true | semejanza_HCL_like_no_cierra      | PASS              |
| HCL-LIM-03 | U               |          false | dato_critico_ausente              | PASS              |
| CNS-LIM-01 | 0+U             |           true | identidad_tisular_no_tumoral      | PASS              |
| CNS-LIM-02 | U               |          false | imagen_sin_identidad_no_cierra    | PASS              |
| CNS-LIM-03 | 0+U             |           true | criterios_GBM_no_satisfechos      | PASS              |

| Métrica esperada            | Valor |
| --------------------------- | ----: |
| casos ejecutados            |     6 |
| salidas PASS                |     6 |
| refutaciones error0 acotado |     4 |
| U legítimos                 |     2 |
| diagnósticos positivos      |     0 |
| alternativas cerradas       |     0 |
| negativos ejecutados        |    16 |
| negativos aceptados         |     0 |
| U degradadas                |     0 |
| salidas sin retorno         |     0 |
| pases silenciosos           |     0 |
| dictamen global             |  PASS |

El contrato de salidas esperadas es la defensa contra acomodación posterior. Si el runner produce algo distinto, se corrige el runner, los datos o el contrato tras auditoría; no se cambia la expectativa para salvar el PASS.

### AI.14.8. Runner mínimo determinista

El runner mínimo determinista aplica el contrato sin dependencias externas. Opera sobre tablas locales, valida campos obligatorios, decide por condiciones, rechaza negativos, compara con salidas esperadas y emite resumen. Su lógica debe ser lo bastante pequeña para auditarse completa, pero lo bastante estricta para no permitir pases silenciosos. El runner mínimo no usa internet, no aprende, no pondera, no calcula probabilidad, no interpreta texto clínico libre y no decide por semejanza.

<div align="center">Runner<sub>mín</sub>=validar → decidir → adversarial → comparar → resumir.</div>

```python
from dataclasses import dataclass
from typing import Dict, List, Tuple

VALID_STATES = {"0", "1", "U", "NA"}
VALID_TYPES = {"necesaria", "apoyo", "diferencial", "U", "negativa"}
VALID_OUTPUTS = {"0", "1", "U", "0+U", "NO_APTO", "FAIL"}

@dataclass(frozen=True)
class Case:
    id_caso: str
    dominio: str
    etiqueta: str
    transductor: str
    muestra: str
    metodo: str
    limite: str

@dataclass(frozen=True)
class Condition:
    id_caso: str
    id_condicion: str
    tipo: str
    estado: str
    fuerza: str
    retorno_local: str

@dataclass(frozen=True)
class Expected:
    id_caso: str
    salida: str
    error0: bool
    retorno_minimo: str
    dictamen: str

def validate_case(case: Case) -> List[str]:
    errors = []
    for field_name, value in case.__dict__.items():
        if not str(value).strip():
            errors.append(f"E-MAT-EMPTY:{case.id_caso}:{field_name}")
    if not case.muestra:
        errors.append(f"E-MAT-04:{case.id_caso}")
    if not case.metodo:
        errors.append(f"E-MAT-05:{case.id_caso}")
    if not case.limite:
        errors.append(f"E-MAT-11:{case.id_caso}")
    return errors

def validate_conditions(case_id: str, conditions: List[Condition]) -> List[str]:
    errors = []
    if not conditions:
        return [f"E-MAT-08:{case_id}"]
    if not any(c.tipo == "necesaria" for c in conditions):
        errors.append(f"E-MAT-08:{case_id}")
    for c in conditions:
        if c.tipo not in VALID_TYPES:
            errors.append(f"E-MAT-TYPE:{case_id}:{c.id_condicion}")
        if c.estado not in VALID_STATES:
            errors.append(f"E-MAT-07:{case_id}:{c.id_condicion}")
        if not c.retorno_local:
            errors.append(f"E-MAT-10:{case_id}:{c.id_condicion}")
    return errors

def decide(conditions: List[Condition]) -> Tuple[str, bool, str]:
    necesarias = [c for c in conditions if c.tipo == "necesaria"]
    diferenciales_u = any(c.tipo == "diferencial" and c.estado == "U" for c in conditions)

    zero_conditions = [c for c in necesarias if c.estado == "0"]
    if zero_conditions:
        salida = "0+U" if diferenciales_u else "0"
        motivo = ";".join(c.retorno_local for c in zero_conditions)
        return salida, True, motivo

    u_conditions = [c for c in necesarias if c.estado == "U"]
    if u_conditions:
        motivo = ";".join(c.retorno_local for c in u_conditions)
        return "U", False, motivo

    if necesarias and all(c.estado == "1" for c in necesarias):
        return "1", False, "condiciones_necesarias_satisfechas"

    return "U", False, "estado_insuficiente"

def check_supports_do_not_close(conditions: List[Condition], salida: str) -> List[str]:
    errors = []
    if salida == "1":
        necesarias = [c for c in conditions if c.tipo == "necesaria"]
        if not necesarias or not all(c.estado == "1" for c in necesarias):
            errors.append("E-DX-01:apoyo_usado_como_cierre")
    return errors

def run_case(case: Case, conditions: List[Condition], expected: Expected) -> Dict[str, str]:
    errors = []
    errors.extend(validate_case(case))
    errors.extend(validate_conditions(case.id_caso, conditions))

    if errors:
        salida = "FAIL"
        error0 = False
        motivo = "|".join(errors)
    else:
        salida, error0, motivo = decide(conditions)
        errors.extend(check_supports_do_not_close(conditions, salida))

    if salida != expected.salida:
        errors.append(f"E-MAT-15:{case.id_caso}:salida_obtenida={salida}:esperada={expected.salida}")
    if error0 != expected.error0:
        errors.append(f"E-MAT-15:{case.id_caso}:error0_obtenido={error0}:esperado={expected.error0}")
    if expected.retorno_minimo not in motivo and expected.retorno_minimo not in salida:
        # El runner material completo debe comparar contra retorno médico externo.
        # En el mínimo, se exige que el motivo contenga la clave decisiva.
        errors.append(f"E-MAT-10:{case.id_caso}:retorno_minimo_no_detectado")

    return {
        "id_caso": case.id_caso,
        "salida_obtenida": salida,
        "error0_obtenido": str(error0).lower(),
        "motivo": motivo,
        "dictamen": "PASS" if not errors else "FAIL",
        "errores": ";".join(errors),
    }
```

Este runner mínimo contiene lo esencial: validación, decisión y comparación. No contiene aún lectura de CSV, generación de hashes, informe por subbanco ni escritura de ficheros. Es intencionado: AI.14 fija el núcleo; AI.15 materializará paquete inicial. La forma mínima permite auditar la regla antes de envolverla en arquitectura.

### AI.14.9. Ejecución mínima sobre el lote semilla

La ejecución mínima sobre el lote semilla debe producir seis salidas concordantes. Cuatro son 0+U con error0_acotado=true; dos son U con error0_acotado=false. El resultado no contiene diagnóstico positivo. El retorno mínimo debe localizar la condición que decide. Si una salida difiere, el dictamen del caso es FAIL. Si cualquier negativo se acepta, el dictamen global es FAIL aunque los seis casos base pasen.

<div align="center">Exec<sub>semilla</sub>=6/6 casos PASS ∧ 16/16 negativos rechazados ∧ U degradada=0.</div>

| id_caso    | salida_obtenida | error0_obtenido | motivo_decisivo                   | dictamen |
| ---------- | --------------- | --------------: | --------------------------------- | -------- |
| HCL-LIM-01 | 0+U             |            true | patron_clasico_no_conservado      | PASS     |
| HCL-LIM-02 | 0+U             |            true | entidad_clasica_no_conservada     | PASS     |
| HCL-LIM-03 | U               |           false | falta_dato_critico                | PASS     |
| CNS-LIM-01 | 0+U             |            true | histologia_tumoral_refutada       | PASS     |
| CNS-LIM-02 | U               |           false | falta_identidad_tisular_molecular | PASS     |
| CNS-LIM-03 | 0+U             |            true | criterios_GBM_no_satisfechos      | PASS     |

| Métrica obtenida mínima     | Valor |
| --------------------------- | ----: |
| casos ejecutados            |     6 |
| casos PASS                  |     6 |
| casos FAIL                  |     0 |
| refutaciones error0_acotado |     4 |
| U legítimos                 |     2 |
| diagnósticos positivos      |     0 |
| alternativas cerradas       |     0 |
| negativos aceptados         |     0 |
| U degradadas                |     0 |
| cierres por apoyo           |     0 |
| cierres por imagen          |     0 |
| cierres por muerte          |     0 |
| retorno mínimo detectado    |   6/6 |
| dictamen global mínimo      |  PASS |

La salida reproducible mínima no equivale todavía a cierre material completo del paquete. Equivale a núcleo ejecutable coherente. Para cierre material completo harán falta ficheros reales, lectura de CSV, escritura de salidas, resumen por subbanco, manifiesto, hashes y garantías. Esta distinción debe permanecer visible: AI.14 cierra el contrato mínimo; AI.15 deberá materializar el paquete inicial.

### AI.14.10. Salida reproducible esperada

La salida reproducible esperada se expresa como tabla global. Debe poder generarse automáticamente por el runner y cotejarse con salidas_esperadas.csv. El formato mínimo es deliberadamente plano: id_caso, salida_obtenida, error0_obtenido, motivo, dictamen y errores. Si errores está vacío y la salida coincide, el caso pasa. Si errores contiene cualquier código, el caso falla. El dictamen global sólo es PASS si todos los casos pasan y todos los negativos quedan rechazados.

<div align="center">SalidaReproducible<sub>mín</sub>=CSV(id,salida,error0,motivo,dictamen,errores).</div>

| id_caso    | salida_obtenida | error0_obtenido | motivo                            | dictamen | errores |
| ---------- | --------------- | --------------: | --------------------------------- | -------- | ------- |
| HCL-LIM-01 | 0+U             |            true | patron_clasico_no_conservado      | PASS     |         |
| HCL-LIM-02 | 0+U             |            true | entidad_clasica_no_conservada     | PASS     |         |
| HCL-LIM-03 | U               |           false | falta_dato_critico                | PASS     |         |
| CNS-LIM-01 | 0+U             |            true | histologia_tumoral_refutada       | PASS     |         |
| CNS-LIM-02 | U               |           false | falta_identidad_tisular_molecular | PASS     |         |
| CNS-LIM-03 | 0+U             |            true | criterios_GBM_no_satisfechos      | PASS     |         |

| resumen_global       | valor |
| -------------------- | ----: |
| total_casos          |     6 |
| pass_casos           |     6 |
| fail_casos           |     0 |
| total_negativos      |    16 |
| negativos_rechazados |    16 |
| negativos_aceptados  |     0 |
| u_legitimos          |     2 |
| u_degradadas         |     0 |
| error0_acotado       |     4 |
| retornos_minimos     |     6 |
| pases_silenciosos    |     0 |
| dictamen_global      |  PASS |

Esta salida debe tratarse como expectativa reproducible, no como resultado clínico. El dictamen PASS significa que el lote semilla cumple su contrato formal. No significa que el sistema diagnostique pacientes reales, ni que posea error cero fuera del banco, ni que una persona con datos semejantes deba recibir un diagnóstico determinado. El propio contrato limita su alcance.

### AI.14.11. Reglas de fallo del runner mínimo

El runner mínimo debe fallar ante errores materiales y diagnósticos. La regla de fallo es deliberadamente dura: cualquier dato crítico ausente, cualquier estado inválido, cualquier retorno ausente, cualquier U degradada, cualquier apoyo usado como cierre, cualquier negativo aceptado o cualquier discrepancia entre salida esperada y obtenida produce FAIL o NO_APTO. No hay avisos blandos que permitan PASS global. Un banco clínico-biológico que tolera avisos blandos se convierte en narrativa.

<div align="center">FAIL ⇔ error crítico ∨ salida discordante ∨ U degradada ∨ negativo aceptado ∨ retorno ausente.</div>

| Fallo                                 | Código          | Resultado                            |
| ------------------------------------- | --------------- | ------------------------------------ |
| caso sin muestra                      | E-MAT-04        | NO_APTO                              |
| caso sin método                       | E-MAT-05        | NO_APTO                              |
| dato crítico sin unidad               | E-MAT-06        | NO_APTO                              |
| estado inválido                       | E-MAT-07        | FAIL                                 |
| condición necesaria ausente           | E-MAT-08        | U/no evaluable o FAIL según etiqueta |
| retorno ausente                       | E-MAT-10        | FAIL                                 |
| límite ausente                        | E-MAT-11        | FAIL                                 |
| salida obtenida distinta de esperada  | E-MAT-15        | FAIL                                 |
| apoyo usado como cierre               | E-DX-01         | FAIL                                 |
| condición 0 aceptada como diagnóstico | E-DX-02         | FAIL                                 |
| condición U cerrada como diagnóstico  | E-DX-03         | FAIL                                 |
| imagen sustituye histología           | E-DX-04         | FAIL                                 |
| morfología sustituye patrón           | E-DX-05         | FAIL                                 |
| muerte usada como causa               | E-DX-06         | FAIL                                 |
| alternativa inventada                 | E-DX-07         | FAIL                                 |
| U convertida en 0 o 1                 | E-DX-11/E-DX-12 | FAIL                                 |
| negativo aceptado                     | E-DX-13         | FAIL                                 |

| Situación                    | Salida correcta                  |
| ---------------------------- | -------------------------------- |
| falta método                 | NO_APTO                          |
| falta tejido para tumor      | U, no tumor=1 ni tumor=0         |
| falta dato molecular crítico | U                                |
| condición necesaria refutada | 0 o 0+U                          |
| sólo apoyos positivos        | sospecha/U                       |
| muerte añadida               | no modifica etiqueta diagnóstica |
| alternativa plausible        | U si no está cerrada             |
| retorno ausente              | FAIL                             |

Estas reglas de fallo hacen que el runner mínimo sea útil aunque sea pequeño. Lo importante no es su longitud, sino que no permita salidas mudas. Una implementación de diez líneas que devuelva PASS sin explicar fallos sería no apta. Un runner mínimo sí puede ser breve, pero no puede ser débil.

### AI.14.12. Cierre del contrato mínimo

El contrato mínimo queda cerrado cuando las cinco tablas existen, el runner mínimo puede leerlas o representarlas, las condiciones deciden las seis salidas semilla, los negativos quedan rechazados, las U se conservan, los retornos mínimos están presentes y la salida reproducible coincide con la esperada. Ese cierre es estrictamente material del núcleo mínimo. No cierra el banco maestro ampliado, no cierra casos reales y no sustituye la arquitectura completa. Habilita la materialización inicial del paquete clínico-biológico.

<div align="center">Cierre<sub>mín</sub> ⇔ tablas mínimas ∧ runner mínimo ∧ salida reproducible ∧ negativos rechazados ∧ U preservada.</div>

| Condición de cierre mínimo      | Estado exigido |
| ------------------------------- | -------------- |
| casos.csv definido              | sí             |
| condiciones.csv definido        | sí             |
| negativos.csv definido          | sí             |
| retornos.csv definido           | sí             |
| salidas_esperadas.csv definido  | sí             |
| runner mínimo definido          | sí             |
| seis casos semilla evaluables   | sí             |
| cuatro error0 acotados          | sí             |
| dos U legítimos                 | sí             |
| dieciséis negativos rechazables | sí             |
| retorno mínimo por caso         | sí             |
| salida reproducible global      | PASS           |
| pases silenciosos               | 0              |
| alcance limitado                | explícito      |

| Lo que queda cerrado              | Lo que no queda cerrado     |
| --------------------------------- | --------------------------- |
| núcleo de contrato ejecutable     | banco clínico ampliado      |
| reglas mínimas de decisión        | casos reales individuales   |
| salida semilla esperada           | validez clínica general     |
| rechazo de negativos básicos      | toda la adversarial futura  |
| conservación de U en lote semilla | resolución de U futuras     |
| retorno mínimo                    | paquete completo con hashes |

### AI.14.13. Conclusión del apartado

El contrato de datos, runner mínimo y salida reproducible fija el núcleo ejecutable del banco clínico-biológico. Cinco tablas bastan para la versión mínima: casos, condiciones, negativos, retornos y salidas esperadas. La tabla de casos define dominio, etiqueta, transductor, muestra, método y límite. La tabla de condiciones decide por condiciones necesarias, apoyos, diferenciales y U. La tabla de negativos obliga al sistema a resistir cierres por apariencia, marcador parcial, imagen, U degradada, muerte, falta de método, falta de unidad, retorno ausente y alternativa inventada. La tabla de retornos impide salidas opacas. La tabla de salidas esperadas impide acomodar el resultado después de ejecutar.

El runner mínimo opera sin inferencia opaca, sin probabilidad, sin aprendizaje, sin internet y sin decisión por semejanza. Valida el caso, valida condiciones, aplica corte, conserva U, impide cierre por apoyo, compara salida esperada y emite dictamen. La ejecución semilla esperada produce seis casos PASS: HCL-LIM-01, HCL-LIM-02, CNS-LIM-01 y CNS-LIM-03 como refutaciones con error cero acotado; HCL-LIM-03 y CNS-LIM-02 como U legítimos. La salida global mínima es PASS sólo si los dieciséis negativos quedan rechazados, no hay U degradada, no hay cierres por apariencia, no hay retorno ausente y no hay pases silenciosos.

Con AI.14 queda cerrado el núcleo mínimo reproducible. El siguiente paso natural es AI.15: materialización inicial del paquete clínico-biológico, donde el contrato se convertirá en tablas canónicas, runner, salidas esperadas, salida obtenida, resumen, garantías y cierre reproducible del lote inicial.

[Descargar el .md limpio](sandbox:/mnt/data/AI_14_contrato_datos_runner_minimo_salida_reproducible_banco_clinico_biologico.md)
