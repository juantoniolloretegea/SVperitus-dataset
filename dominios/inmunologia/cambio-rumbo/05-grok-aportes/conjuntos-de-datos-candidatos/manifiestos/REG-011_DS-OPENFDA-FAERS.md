# Manifiesto de conjunto candidato

## Identidad

- Registro_ID: REG-011
- Dataset_ID: DS-OPENFDA-FAERS
- Nombre: openFDA drug/event FAERS
- Versión o fecha: API event last_updated 2026-07-30; consulta 2026-09-01; results.total 20692690
- Repositorio y responsable: openFDA / FDA
- URL, DOI o accession: https://api.fda.gov/drug/event.json; terms https://open.fda.gov/terms/; license https://open.fda.gov/license/
- Jurisdicción: Estados Unidos
- Fecha de verificación: 2026-09-01

## Finalidad y diseño originales

- Finalidad original: farmacovigilancia de notificaciones espontaneas. No es cohorte clinica.
- Tipo de estudio o fuente: vigilancia_agregada
- Unidad observacional: informe de caso
- Poblacion: notificantes FAERS; no cohorte definida
- Criterios de inclusión: no aplica (notificacion espontanea)
- Criterios de exclusión: no aplica
- Tamaño de cohorte: no es cohorte; total de informes en meta API no es incidencia
- Periodo de observación: historico FAERS
- Seguimiento: no

## Contenido comprobado

- Variables inmunológicas: no estructuradas como panel clinico
- Intervenciones o exposiciones: farmaco notificado
- Desenlaces: reaccion adversa notificada; no causalidad
- Temporalidad: fecha de informe distinto de tiempo de episodio
- Nivel de agregación: agregado / informe
- Diccionario o esquema: esquema openFDA publico
- Datos faltantes: denominador poblacional
- Transformaciones y derivaciones declaradas: curacion FDA

## Cobertura y límites

- Familias clínicas candidatas cubiertas: ninguna familia como cohorte
- Familias no cubiertas: incidencia; causalidad; episodio
- Variables necesarias ausentes: incidencia; causalidad; episodio
- Aplicabilidad: nula para constituir dominio; no sustituye perimetro clinico humano
- Limitaciones: senal distinto de riesgo individual
- Residual: no cierra RSD-02
- Riesgo de ocultación de sucesos singulares por agregación: si si N o totales se leen como cobertura de dominio

## Gobierno D0-L

- Acceso: API publica HTTP 200 2026-09-01 (sin volcar microdatos al repo)
- Autorización: no conferida para microdato ni para adopcion
- Licencia: openFDA license; disclaimer: do not rely on openFDA to make decisions regarding medical care
- Redistribución: segun license openFDA; esta fila no copia informes
- Elegibilidad para tratamiento mediante IA: NO_VERIFICADA. Términos específicos de IA no comprobados. El disclaimer openFDA excluye decisión asistencial; no es cláusula de IA.
- Anonimización: informes publicos FAERS
- Riesgo de reidentificacion: bajo en agregado; no evaluado caso a caso
- Datos personales presentes: no auditados en deposito; esta ronda no incorpora microdato
- Procedimiento reproducible de obtencion: GET https://api.fda.gov/drug/event.json (meta only esta ronda)
- Huella criptográfica, si procede: no procede (sin exportacion)

## Separación epistémica

- Asociaciones que el conjunto permite estudiar: ninguna verificada sobre microdato en esta ronda
- Causalidad demostrada por la fuente: NINGUNA
- Inferencias prohibidas: armonizar N; tratar; cerrar umbral; imputar variables; fusionar familias por rotulo; convertir metadato NCT en deposito
- Consecuencias clínicas constituidas: NINGUNA

## Dictamen candidato

- Estado: NO_ADMISIBLE
- Motivo: Ronda 1 de identificación y cribado documental cerrada; CANDIDATO_NO_ADOPTADO; D0-E=0
- Condiciones pendientes: diccionario primario, D0-L completo por finalidad, autorizacion humana expresa antes de cualquier zip
- Fuente primaria de verificación: openFDA API 2026-09-01; watson-biblioteca DATA-OPENFDA; Conectores_validados_2026-09-01
- Revisor: Grok 2026-09-01
