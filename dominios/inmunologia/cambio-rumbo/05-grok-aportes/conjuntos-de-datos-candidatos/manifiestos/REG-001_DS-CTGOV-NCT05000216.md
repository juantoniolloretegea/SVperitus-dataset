# Manifiesto de conjunto candidato

## Identidad

- Registro_ID: REG-001
- Dataset_ID: DS-CTGOV-NCT05000216
- Nombre: ACV01 registro ClinicalTrials.gov (NCT05000216)
- Versión o fecha: consulta API v2 2026-09-01; TERMINATED; completion 2024-03-28; whyStopped: continued enrollment hurdles
- Repositorio y responsable: ClinicalTrials.gov / NIAID (DAIT ACV01)
- URL, DOI o accession: NCT05000216; https://clinicaltrials.gov/study/NCT05000216; API https://clinicaltrials.gov/api/v2/studies/NCT05000216
- Jurisdicción: Estados Unidos
- Fecha de verificación: 2026-09-01

## Finalidad y diseño originales

- Finalidad original: Registro publico de ensayo de refuerzo COVID-19 en AIIRD no respondedores. Esta fila documenta metadato de diseno, no el paquete ImmPort.
- Tipo de estudio o fuente: ensayo_registro
- Unidad observacional: participante (declarado; microdato no inspeccionado)
- Poblacion: AIIRD adulto y pediatrico declarados: RA, SLE, penfigo vulgar, MS, SSc, pSLE, JIA, JDM, POMS con vacunacion COVID completa previa
- Criterios de inclusión: Adulto general: consentimiento; vacunacion COVID completa documentada >=4 y <=52 semanas antes de Stage 1 (o <=48 semanas Stage 2). Criterio completo en eligibilityModule.
- Criterios de exclusión: Entre otros: alergia grave a pauta COVID/PEG; neoplasia en quimio/inmunoterapia; enfermedad activa que impide retirar IS; SARS-CoV-2 <30 d o PCR+ screening; miocarditis/pericarditis <6 sem; infecciones cronicas activas; CVID o IGRT (nota pediatrica IVIG); Ac/plasma anti-SARS-CoV-2 <30 d; vacuna viva <2 meses o prevista; gestacion/lactancia. Texto integro en API.
- Tamaño de cohorte: enrollment ACTUAL=258. No armonizar con paper 279/148/140/141 ni DR60 N=148.
- Periodo de observación: start 2021-08-13; primaryCompletion 2023-06-22; completion 2024-03-28
- Seguimiento: desenlace primario declarado a semana 4 post-vacunacion

## Contenido comprobado

- Variables inmunológicas: declaradas: respuesta de anticuerpo protectora a sem 4. Variables depositadas NO leidas.
- Intervenciones o exposiciones: refuerzo mRNA-1273 / BNT162b2 / Ad26.COV2.S / monovalente AS03 / bivalentes; Continue o Withhold IS (MMF-MPA, MTX, B-cell depletion)
- Desenlaces: percent of Stage 1 adult / Stage 2 adult / pediatric participants with protective antibody response at week 4
- Temporalidad: longitudinal declarada; no comprobada en deposito
- Nivel de agregación: metadato de registro de ensayo
- Diccionario o esquema: el registro NCT no es diccionario ImmPort
- Datos faltantes: U_CAUSA_DECLARADA para microdato y diccionario de deposito
- Transformaciones y derivaciones declaradas: no aplicables al registro

## Cobertura y límites

- Familias clínicas candidatas cubiertas: F-AUTOIMM-AIIRD (diseno); F-VACUNA-IS (refuerzo no vivo + withhold IS)
- Familias no cubiertas: F-PJP; vacuna viva; F-IEI; diccionario ImmPort; N unificado
- Variables necesarias ausentes: F-PJP; vacuna viva; F-IEI; diccionario ImmPort; N unificado
- Aplicabilidad: nula para constituir dominio; no sustituye perimetro clinico humano
- Limitaciones: TERMINATED por hurdles de enrollment; 258 distinto de N paper
- Residual: publicacion distinto de deposito; DR60 Assays None
- Riesgo de ocultación de sucesos singulares por agregación: si si N o totales se leen como cobertura de dominio

## Gobierno D0-L

- Acceso: API v2 HTTP 200 sin clave 2026-09-01
- Autorización: no conferida para microdato ni para adopcion
- Licencia: metadato NCT de uso publico; no es licencia ImmPort
- Redistribución: metadato NCT si; microdato no forma parte de esta fila
- Elegibilidad para tratamiento mediante IA: NO_VERIFICADA. Términos específicos de IA del registro no comprobados. Citar metadato no equivale a tratar.
- Anonimización: no hay microdato en esta fila
- Riesgo de reidentificacion: no aplica a metadato de registro
- Datos personales presentes: no auditados en deposito; esta ronda no incorpora microdato
- Procedimiento reproducible de obtencion: GET https://clinicaltrials.gov/api/v2/studies/NCT05000216
- Huella criptográfica, si procede: no procede (sin exportacion)

## Separación epistémica

- Asociaciones que el conjunto permite estudiar: ninguna verificada sobre microdato en esta ronda
- Causalidad demostrada por la fuente: NINGUNA
- Inferencias prohibidas: armonizar N; tratar; cerrar umbral; imputar variables; fusionar familias por rotulo; convertir metadato NCT en deposito
- Consecuencias clínicas constituidas: NINGUNA

## Dictamen candidato

- Estado: EVALUADO
- Motivo: Ronda 1 de identificación y cribado documental cerrada; CANDIDATO_NO_ADOPTADO; D0-E=0
- Condiciones pendientes: diccionario primario, D0-L completo por finalidad, autorizacion humana expresa antes de cualquier zip
- Fuente primaria de verificación: ClinicalTrials.gov API v2 2026-09-01; Lectura_publica_SDY3324_ACV01_2026-08-31; Fuentes_acceso_capa2_05_D0L_bloqueo
- Revisor: Grok 2026-09-01
