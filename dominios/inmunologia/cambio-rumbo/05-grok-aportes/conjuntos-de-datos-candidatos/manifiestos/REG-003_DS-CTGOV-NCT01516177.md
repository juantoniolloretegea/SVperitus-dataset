# Manifiesto de conjunto candidato

## Identidad

- Registro_ID: REG-003
- Dataset_ID: DS-CTGOV-NCT01516177
- Nombre: ITN524ST / CTOT-12 ARTIST registro ClinicalTrials.gov
- Versión o fecha: consulta API v2 2026-09-01; COMPLETED; completion 2014-04
- Repositorio y responsable: ClinicalTrials.gov / NIAID (DAIT ITN524ST/CTOT-12)
- URL, DOI o accession: NCT01516177; https://clinicaltrials.gov/study/NCT01516177; API https://clinicaltrials.gov/api/v2/studies/NCT01516177
- Jurisdicción: Estados Unidos
- Fecha de verificación: 2026-09-01

## Finalidad y diseño originales

- Finalidad original: Registro observacional: prevalencia de firma de tolerancia ITN en receptores de rinon. No es el paquete ImmPort SDY3274. No es el paper ST507 2010.
- Tipo de estudio o fuente: cohorte_observacional_registro
- Unidad observacional: participante (declarado)
- Poblacion: receptores de primer trasplante renal
- Criterios de inclusión: primer rinon vivo o cadaver; Tx entre 1 y 5 anos; eGFR >=45 mL/min/1.73 m2 en ultimos 6 meses; consentimiento
- Criterios de exclusión: rechazo agudo cortico-resistente; >=2 episodios de rechazo agudo; rechazo agudo en el ultimo ano; neoplasia actual; otro organo; SIDA segun CDC
- Tamaño de cohorte: enrollment ACTUAL=250
- Periodo de observación: start 2010-09; completion 2014-04
- Seguimiento: time frame declarado 2 anos; al menos un time point de firma

## Contenido comprobado

- Variables inmunológicas: firma de tolerancia renal ITN declarada; detalle de genes/ensayos NO en esta fila
- Intervenciones o exposiciones: ninguna de ensayo; exposicion = trasplante e IS de mantenimiento no detallada en extracto
- Desenlaces: presencia de al menos un time point de la firma de tolerancia renal previamente identificada
- Temporalidad: observacional
- Nivel de agregación: metadato de registro
- Diccionario o esquema: el registro no es diccionario ImmPort
- Datos faltantes: ensayos moleculares reales del deposito
- Transformaciones y derivaciones declaradas: no aplicables al registro

## Cobertura y límites

- Familias clínicas candidatas cubiertas: F-TRASPLANTE-RENAL (diseno)
- Familias no cubiertas: F-IEI; F-PJP; vacuna; alergia; autoinmunidad no renal
- Variables necesarias ausentes: F-IEI; F-PJP; vacuna; alergia; autoinmunidad no renal
- Aplicabilidad: nula para constituir dominio; no sustituye perimetro clinico humano
- Limitaciones: no confundir con paper ST507 2010 distinto
- Residual: paquete ImmPort SDY3274 no leido
- Riesgo de ocultación de sucesos singulares por agregación: si si N o totales se leen como cobertura de dominio

## Gobierno D0-L

- Acceso: API v2 HTTP 200 2026-09-01
- Autorización: no conferida para microdato ni para adopcion
- Licencia: metadato NCT publico
- Redistribución: metadato si
- Elegibilidad para tratamiento mediante IA: NO_VERIFICADA. Términos específicos de IA del registro no comprobados. Citar metadato no equivale a tratar.
- Anonimización: n/a metadato
- Riesgo de reidentificacion: n/a metadato
- Datos personales presentes: no auditados en deposito; esta ronda no incorpora microdato
- Procedimiento reproducible de obtencion: GET https://clinicaltrials.gov/api/v2/studies/NCT01516177
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
- Fuente primaria de verificación: ClinicalTrials.gov API v2 2026-09-01; Expediente_D0 v0.1; Lectura_publica_SDY3274_ARTIST
- Revisor: Grok 2026-09-01
