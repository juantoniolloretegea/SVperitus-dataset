# Paquete Watson v0.2 — universo candidato INMUNO

**Corte:** 31-08-2026.  
**Estatuto:** propuesta de inventario. No adoptada. No es el dominio. No tipa SV. No cierra G0/G1/G2. Ninguna fuente A1 adoptada. Ningún dataset descargado.

## Qué se termina aquí

1. El CSV de 138 filas presentado como «parámetros del dominio» queda **retirado** (nombre y pretensión). El número no era un argumento de cobertura.
2. El universo v0.1 (23 filas) se conserva como rastro y deja de ser el frente de trabajo.
3. El mapa curricular MIR v0.1 (61 ítems) **sigue vigente como objeto distinto**: es temario, no parámetro operativo.

## Qué entrega este paquete

| Activo | Archivo | N | Pretensión prohibida |
|---|---|---|---|
| 1. Universo candidato de parámetros | `Universo_candidato_parametros_INMUNO_v0.2_2026-08-31.xlsx` + `.csv` | 64 | no es N del dominio |
| 2. Entidades tipificadas | `Entidades_inmunologicas_tipificadas_v0.2_2026-08-31.xlsx` + `.csv` | 27 | no es el censo IUIS |
| 3. Relación parámetro–entidad | `Relacion_parametro_entidad_v0.2_2026-08-31.xlsx` + `.csv` | 50 | no es el producto cartesiano |
| 4. Matriz de cobertura | `Matriz_cobertura_repositorios_v0.2_2026-08-31.xlsx` + `.csv` | 40 | no es cobertura completa de A1 |
| Índice | `Paquete_Watson_INMUNO_v0.2_2026-08-31.xlsx` | — | — |

Índice de residuales: 12 bloques en la hoja `02_Residual` del activo 1.

## Reglas de Watson aplicadas

- Ningún CSV inicial se presenta como «todos los parámetros del dominio».
- Nombre obligatorio: **universo candidato**, versionado, residual explícito.
- Una fila = parámetro clínicamente indivisible. No hay filas «estado inmunológico», «riesgo infeccioso» ni «respuesta vacunal».
- Ocho prioridades 1–20 (20 = máxima). No hay columna de promedio. No hay prioridad final calculada.
- Las clasificaciones oficiales se conservan con sistema + código + versión. No se fusionan ICD / SNOMED / Orphanet / OMIM / criterios.
- Las relaciones viven en tabla propia.
- Un repositorio no «contiene la inmunología». Si un área no aparece en A1, no desaparece del dominio clínico: pasa a residual y bloquea cobertura completa.
- Toda afirmación empírica queda `no buscado` / `no encontrado` / `inaccesible` salvo que A1 ya hubiera leído la norma. No se inventa N de registros.

## Acotado MIR (respuesta a la corrección previa)

El universo no es un ornamento de familias curriculares. Se acota por lo que un MIR de Inmunología en ES (POE SCO/3255/2006) o equivalente (IUIS 2024 I–X, ABAI, GMC/JRCPTB ACI) **tendría que saber medir o decidir**, convertido a parámetros operativos.

Eso no autoriza a copiar el temario como filas. El mapa curricular permanece en su archivo. Aquí solo hay magnitudes, ensayos, exposiciones, criterios versionados e intervenciones indivisibles.

## Prioridades: por qué no hay un 1–20 único

Un parámetro raro puede ser catastrófico (anti-MBG, TREC, XM CDC). Un parámetro universal puede ser poco discriminante (ANA 1:80). Equipararlos con una media introduce falsa precisión.

Las ocho escalas responden a preguntas distintas. La decisión de orden final queda para después de la revisión clínica adversarial (paso 9 de Watson). No se calcula aquí.

## Relación bloqueante

`R-019` y `R-035` (profilaxis PJP × IS farmacológica / PJP): la **indicación** no está cerrada. Queda residual `RSD-02`. No se autoriza umbral.

## Cobertura empírica (hechos de objeto, no de conveniencia)

- R03 ESID / R04 USIDNET / R05 REDIP: objeto IEI/PID. No cubren el episodio de IS farmacológica de las semillas.
- R01 ImmPort 2.5 / R06 TrialShare: reanálisis de ensayos; **no uso para tratar**.
- R07 IEDB, R08 OAS, R09 AIRR/iReceptor, R11 VDJdb: objeto molecular. No cubren IgG sérica de un episodio.
- Histocompatibilidad operativa SOT (ONT/UNOS) no está en A1 (`RSD-08`).
- Cribado TREC neonatal ES no está en A1 (`P-IEI-003`, empírico `no encontrado`).

## Secuencia Watson — estado

| Paso | Estado |
|---|---|
| 1. Delimitar áreas provisionales | hecho, no cerrado |
| 2. Universo candidato + inventario de fuentes en paralelo | hecho (este paquete + A1) |
| 3. Depurar compuestos y duplicados | hecho en v0.2; residual RSD-05 para la cola |
| 4. Tipificar entidades | hecho, candidato |
| 5. Relaciones parámetro–entidad | hecho, candidato |
| 6. Consecuencias de presencia / ausencia / ignorancia | columnas presentes; no armonizadas |
| 7. Cruzar con repositorios y microdatos | sparse, sin microdatos (ninguna descarga) |
| 8. Identificar vacíos y residual | 12 bloques declarados; lista no exhaustiva |
| 9. Revisión clínica adversarial humana | **no hecho** |
| 10. Decidir dimensiones, orden y composición de representaciones | **prohibido**. G0 cerrado. G1/G2 abiertos. |

## Lo que este paquete no autoriza

- No cierra U.
- No dimensiona vectores 1×n.
- No reabre ni congela las semillas IMMUNO-1/2.
- No condiciona R2.
- No adopta un repositorio.
- No declara exhaustividad.

Fin del informe.
