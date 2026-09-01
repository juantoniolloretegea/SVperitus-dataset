# Acta adversarial de recepción del paquete candidato INMUNO v0.2

**Fecha de corte:** 2026-08-31  
**Naturaleza:** acta append-only; evaluación de integridad, trazabilidad y aptitud de entrada  
**Estado del dictamen:** cerrado para esta versión del paquete; no adopta contenido clínico  
**Perímetro:** cuatro pares CSV/XLSX y el memorando `1913b541-93bc-4561-a909-fa203f431c26.md`  
**Fuera de alcance:** modificación del lenguaje, IR, R2, dimensionamiento de matrices, composición y decisión clínica  

## 1. Dictamen blanco sobre negro

**INTEGRIDAD MATERIAL DEL PAQUETE: APTO CON UNA AUSENCIA DOCUMENTAL.**  
Los cuatro CSV coinciden exactamente con sus hojas principales en los cuatro XLSX; las claves primarias son únicas y no hay filas duplicadas.

**INCORPORACIÓN AL DOMINIO CLÍNICO DETERMINISTA: NO APTA.**  
No existe todavía validación clínica humana, evidencia empírica positiva, vocabulario controlado suficiente, procedencia bibliográfica auditable por elemento ni cierre de consecuencias. Las prioridades son propuestas de baja confianza y no pueden gobernar una recomendación clínica.

**USO AUTORIZABLE AHORA:** inventario candidato y cola de trabajo adversarial.  
**USO NO AUTORIZABLE AHORA:** matriz clínica adoptada, composición, consejo médico, regla de exclusión, jerarquización operativa o demostración experimental.

No se modifica ni se sustituye ninguno de los ficheros recibidos.

## 2. Material recibido y huellas

| Pieza | Registros principales | Columnas | SHA-256 |
|---|---:|---:|---|
| Universo candidato de parámetros CSV | 64 | 41 | `3027772c3792dde95dddca20f2b74b8937581b70fb6dacf65928c0a12085dafd` |
| Universo candidato de parámetros XLSX | 64 en `01_Parametros` | 41 | `95e1d8999035538b5c03058cbb0447202dabaa7d187b9ba3760ace7381b7a170` |
| Entidades tipificadas CSV | 27 | 24 | `87bd2b16cd64dfeb42ad2eb5694e1ff7b66cba331ce4adfce1233f5971f08a2f` |
| Entidades tipificadas XLSX | 27 en `01_Entidades` | 24 | `9b7c9b815ef78ccaadebb1e060196c5b652182ac59e841557a7d5105526d1667` |
| Relación parámetro–entidad CSV | 50 | 14 | `f71c55a8ee8d9857237d867304bdd061c0291b9d87200649ca731e6e5f7ea558` |
| Relación parámetro–entidad XLSX | 50 en hoja principal | 14 | `39fa87b78aaa6f760772400adfdc047c54188e4475c3efcf46a74a0ec9527eb8` |
| Cobertura de repositorios CSV | 40 | 24 | `c0c3e47a445644cbb6eec5d449308c47aecf993d8a23d1552aed4f369ac67f4e` |
| Cobertura de repositorios XLSX | 40 en hoja principal | 24 | `0835ceab8628ee10128e649420ae622609e5799e723169b929155fe087746ea0` |
| Memorando del paquete | — | — | `852ec85ff6769d2ad2b899d2ac98a079d5698ac9c68500bd224bc544cb1208d7` |

### Ausencia documental

El memorando declara un índice denominado `Paquete_Watson_INMUNO_v0.2_2026-08-31.xlsx`. Ese fichero no figura entre las piezas entregadas. La ausencia no invalida las cuatro tablas, pero impide declarar completo el paquete documental descrito por su propio memorando.

## 3. Pruebas de integridad material

| Prueba | Resultado | Dictamen |
|---|---|---|
| Paridad de datos CSV/XLSX | Coincidencia exacta en las cuatro tablas principales | PASA |
| Claves primarias vacías | 0 | PASA |
| Claves primarias duplicadas | 0 | PASA |
| Filas completas duplicadas | 0 | PASA |
| Referencias huérfanas desde relaciones | 0 parámetros; 0 entidades | PASA |
| Pares de cobertura ajenos a la tabla de relaciones | 0 | PASA |
| Fórmulas ocultas en XLSX | 0 en las hojas inspeccionadas | PASA |
| Coherencia de cifras del memorando | 64 parámetros, 27 entidades, 50 relaciones, 40 coberturas y 12 residuales confirmados | PASA |
| Índice general anunciado | No entregado | NO PASA |

## 4. Vacíos exactos

Sólo se detectan catorce celdas vacías en las cuatro tablas principales:

- Once `phenotype_codes` vacíos en entidades. No se presume error: deben distinguirse expresamente `no_aplica`, `desconocido` y `pendiente`.
- `P-CLI-002.residual_reason` vacío.
- `R-022.residual` vacío.
- `R-042.conditional_on` vacío.

En un sistema determinista, el vacío no puede tener tres significados implícitos. Cada caso debe quedar tipado antes de cualquier cierre.

## 5. Lo que el paquete hace bien

1. Se autodeclara **propuesta no adoptada** y no simula una validación que no existe.
2. Retira expresamente el universo previo de 138 supuestos parámetros y conserva el mapa MIR como perímetro separado.
3. Prohíbe dimensionar u ordenar matrices a partir de esta entrega.
4. Mantiene abiertos G1 y G2, y no declara cerrado el dominio.
5. Declara que no se descargaron datos ni se inspeccionaron microdatos.
6. Señala como bloqueadas las relaciones PJP `R-019` y `R-035`.
7. Reconoce que falta la adversarial clínica humana.
8. Mantiene ocho prioridades separadas y no fabrica un promedio.

Estas cautelas son correctas. No convierten el contenido en válido; impiden que sea utilizado indebidamente antes de validarlo.

## 6. Bloqueantes para la adopción

### B-01. Colisión de identificadores de repositorio

Los códigos `R01`–`R11` no conservan el significado del registro D0 anterior. Ejemplos:

| ID | Registro D0 | Paquete v0.2 |
|---|---|---|
| R03 | ITN TrialShare | ESID |
| R04 | FlowRepository | USIDNET |
| R05 | IEDB | REDIP |
| R06 | OAS | ITN TrialShare |
| R09 | ESID | AIRR/iReceptor |
| R10 | USIDNET | FlowRepository |
| R11 | REDIP | VDJdb |

**Consecuencia:** una unión por `repository_id` puede atribuir datos, restricciones o cobertura al repositorio equivocado sin producir un error informático visible.  
**Decisión:** prohibida la fusión con D0 hasta crear identificadores estables o con espacio de nombres y una tabla de equivalencias append-only.

### B-02. Procedencia bibliográfica insuficiente por elemento

Las tablas usan referencias abreviadas y versiones como `vigente al usar`, `guía`, `ficha`, `consenso`, `declarar criterios`, `método del laboratorio` o `protocolo del centro`. No constan de forma uniforme identificador persistente, versión exacta, fecha, página, tabla o regla extraída.

**Consecuencia:** un revisor o auditor no puede reproducir la regla que sustenta cada parámetro, umbral, entidad o relación.  
**Decisión:** ningún elemento puede cruzar a conocimiento congelado.

### B-03. Tipos y vocabularios no cerrados

- 24 valores libres de `domain_area` para 64 parámetros.
- 17 valores de `entity_type` para 27 entidades, muchos unitarios o compuestos.
- Aproximadamente 37 formulaciones de `relation_type` para 50 relaciones.
- Direcciones descritas casi siempre mediante frases singulares.
- Tipos de dato mixtos, por ejemplo `cuantitativo o categórico` y `cuantitativo + categórico`.

**Consecuencia:** dos implementaciones pueden interpretar el mismo registro de forma distinta, producir composiciones incompatibles o encubrir un dato faltante mediante una categoría libre.  
**Decisión:** no apto para cierre determinista.

### B-04. Falta de evidencia empírica positiva

- Los 27 registros de entidad tienen `data_status = no contrastado con microdatos`.
- De 40 filas de cobertura, 37 indican `no comprobado` y 3 `objeto distinto`.
- `effective_n_records` no contiene ningún N observado.
- No hay una sola fila que demuestre disponibilidad y medición efectiva del parámetro en el repositorio.

**Consecuencia:** no puede afirmarse cobertura empírica, aumento de criterio clínico ni posibilidad de reproducción experimental.  
**Decisión:** la llamada “matriz de cobertura” sólo es, en esta versión, una cola de auditoría negativa o pendiente.

### B-05. Relaciones sin graduación clínica

Las 50 relaciones tienen `evidence_strength = propuesta no graduada` y conflicto pendiente. El tipo y la dirección no pertenecen aún a catálogos cerrados.

**Consecuencia:** una relación puede existir sintácticamente y ser clínicamente falsa, insuficiente, contextual o no transportable.  
**Decisión:** ninguna relación puede gobernar una advertencia, exclusión o recomendación.

### B-06. Cobertura lógica incompleta

- Parámetros enlazados con alguna entidad: 43 de 64.
- Parámetros sin enlace: 21 de 64.
- Entidades enlazadas: 26 de 27.
- Entidad sin enlace: `E-IEI-AAE`.
- Pares parámetro–entidad sin fila de cobertura de repositorio: 37 de 50.

Los 21 parámetros sin enlace son:

`P-AU-005`, `P-CLI-001`, `P-CLI-002`, `P-CLI-007`, `P-CMP-002`, `P-CMP-003`, `P-CMP-004`, `P-HEM-001`, `P-HEM-002`, `P-HLH-003`, `P-IEI-006`, `P-INF-002`, `P-IS-003`, `P-IS-004`, `P-LAB-001`, `P-LAB-002`, `P-LAB-003`, `P-LAB-004`, `P-LAB-005`, `P-TX-003` y `P-VIR-005`.

**Consecuencia:** no puede demostrarse que el universo candidato cubra el dominio ni que cada elemento tenga una función clínica definida.  
**Decisión:** cierre G1/G2 prohibido.

### B-07. Prioridades no calibradas

Las ocho prioridades son numéricamente válidas y permanecen entre 1 y 20, pero los 64 parámetros declaran confianza baja, propuesta no armonizada y no adoptada. Su fuente es una fórmula general, no una justificación trazable por puntuación.

**Consecuencia:** una ordenación podría parecer exacta sin ser reproducible ni clínicamente consensuada.  
**Decisión:** las prioridades sirven para organizar revisión, no para gobernar conducta clínica ni seleccionar automáticamente matrices.

### B-08. Consecuencias todavía narrativas

El paquete incluye consecuencias clínicamente relevantes, pero no están cerradas como objetos verificables con sujeto afectado, daño, gravedad, reversibilidad, horizonte, condición de activación, alternativa descartada y fuente exacta.

**Consecuencia:** la IA no puede responder de forma única y auditable: “¿qué consecuencias tiene tomar esta decisión y no las alternativas?”.  
**Decisión:** no supera la puerta de consecuencia previa a la decisión del bisturí v0.4.

## 7. Hallazgos mayores no bloqueantes por sí solos

| Código | Hallazgo | Tratamiento requerido |
|---|---|---|
| M-01 | `R-042.conditional_on` vacío | Resolver si es incondicional o falta condición; no dejar implícito |
| M-02 | `R-022.residual` vacío | Declarar `ninguno`, `pendiente` o residual concreto |
| M-03 | `P-CLI-002.residual_reason` vacío | Completar o marcar explícitamente no aplicable |
| M-04 | Códigos fenotípicos vacíos | Sustituir vacío semántico por estado tipado |
| M-05 | Tipos de dato compuestos | Separar parámetros atómicos o declarar unión tipada con regla de resolución |
| M-06 | Jurisdicción genérica | Resolver fuente, versión y alcance por elemento |
| M-07 | Residual reconocido pero no agotado | Mantener abierto; no convertir la lista de 12 bloques en exhaustiva |

## 8. Evaluación contra el bisturí determinista v0.4

| Puerta | Exigencia | Resultado v0.2 |
|---|---|---|
| Congelación de conocimiento | Fuentes exactas, versión y reglas inmutables | NO PASA |
| Identidad estable | IDs sin colisión entre registros | NO PASA |
| Tipado atómico | Dominio, dato, estado y relación cerrados | NO PASA |
| Consecuencia previa | Consecuencia estructurada antes de toda salida | NO PASA |
| Cierre del módulo | Cobertura y residual justificados | NO PASA |
| Evidencia clínica | Revisión clínica humana documentada | NO PASA |
| Evidencia empírica | Datos accesibles y variables comprobadas | NO PASA |
| Integridad tabular | Paridad, claves y ausencia de duplicados | PASA |
| Append-only | Originales preservados; cambios como nuevas piezas | PASA EN RECEPCIÓN |

## 9. Orden obligatorio de saneamiento

Este orden no define matrices ni modifica el lenguaje. Sólo prepara material candidato para nuevas puertas de control.

1. **Congelar esta entrega:** registrar nombres, tamaños y huellas completas sin reescribirla.
2. **Resolver la identidad de repositorios:** crear un catálogo estable y un `crosswalk` D0 ↔ v0.2.
3. **Cerrar codebooks:** dominio, subdominio, tipo de entidad, tipo y dirección de relación, tipo de dato, estado de ausencia y jurisdicción.
4. **Crear registro de fuentes por elemento:** identificador persistente, versión, fecha, localizador y proposición exacta sustentada.
5. **Normalizar consecuencias:** una fila por consecuencia y alternativa, con condiciones y fuente.
6. **Resolver vacíos y tipos mixtos:** sin completar por inferencia.
7. **Adversarial clínica humana:** revisar parámetro, entidad y relación; graduar evidencia y conflicto.
8. **Auditar repositorios con datos realmente accesibles:** diccionario, variable, unidad, población, N efectivo y condiciones de uso.
9. **Recalcular cobertura y residual:** conservar resultados negativos; nunca sobreescribirlos.
10. **Sólo tras superar las puertas anteriores:** proponer módulos o matrices candidatas para autorización expresa.

## 10. Criterio de salida de esta acta

El paquete v0.2 queda admitido como **inventario candidato trazable**, no como conocimiento clínico incorporado. La siguiente operación segura es construir el catálogo de identidad y el registro de procedencia; cualquier dimensionamiento, composición, recomendación médica o inferencia queda bloqueado.

**No se ha tocado el lenguaje de programación ni se ha adoptado una sola fila clínica.**
