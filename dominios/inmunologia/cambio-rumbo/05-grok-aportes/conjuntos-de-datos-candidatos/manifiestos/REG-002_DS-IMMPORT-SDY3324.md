# Manifiesto de conjunto candidato

## Identidad

- Registro_ID: REG-002
- Dataset_ID: DS-IMMPORT-SDY3324
- Nombre: ImmPort SDY3324 paquete ACV01
- Versión o fecha: deposito citado por paper; DR60 2026-08-31 Assays None / Clinical None
- Repositorio y responsable: ImmPort Shared Data / NIAID / Data Provider
- URL, DOI o accession: SDY3324; DOI 10.21430/M35OC5U8Z7; paper 10.1172/jci.insight.191266; NCT05000216
- Jurisdicción: Estados Unidos
- Fecha de verificación: 2026-09-01

## Finalidad y diseño originales

- Finalidad original: Repositorio de datos del ensayo ACV01. Esta fila es el paquete, no el registro NCT.
- Tipo de estudio o fuente: ensayo_repositorio
- Unidad observacional: sujeto ImmPort (no inspeccionado)
- Poblacion: misma poblacion declarada que NCT05000216; N material del zip NO inspeccionado
- Criterios de inclusión: no leidos en diccionario ImmPort
- Criterios de exclusión: no leidos en diccionario ImmPort
- Tamaño de cohorte: DR60 nota 148; paper 279/148/140/141; CT.gov 258. No armonizar.
- Periodo de observación: no leido en paquete
- Seguimiento: no leido en paquete

## Contenido comprobado

- Variables inmunológicas: NO COMPROBADAS. DR60 Assays: None.
- Intervenciones o exposiciones: declaradas en paper/NCT; no leidas en diccionario del zip
- Desenlaces: anti-RBD en paper; no comprobado en deposito
- Temporalidad: desconocida en deposito
- Nivel de agregación: individual desidentificado declarado por ImmPort; no verificado en este paquete
- Diccionario o esquema: NO LEIDO. Pagina /shared/study/{SDY} cascaron JS (17538 bytes identicos para 7 accesiones, 2026-09-01). API estudio 401 sin token (expediente 31-08).
- Datos faltantes: diccionario, unidades, ausencias, medicacion concomitante, desenlace depositado
- Transformaciones y derivaciones declaradas: desconocidas

## Cobertura y límites

- Familias clínicas candidatas cubiertas: ninguna familia cubierta en D0-E
- Familias no cubiertas: todas las variables de deposito; D0-E=0
- Variables necesarias ausentes: todas las variables de deposito; D0-E=0
- Aplicabilidad: nula para constituir dominio; no sustituye perimetro clinico humano
- Limitaciones: publicacion distinto de contenido material del deposito
- Residual: RSD-02 PJP; P-VAC viva; G1 abiertos
- Riesgo de ocultación de sucesos singulares por agregación: si si N o totales se leen como cobertura de dominio

## Gobierno D0-L

- Acceso: cuenta + aceptacion del acuerdo; cuenta no creada
- Autorización: no conferida para microdato ni para adopcion
- Licencia: ImmPort User Agreement https://docs.immport.org/home/agreement/ ss 1.1, 2.4, 2.5
- Redistribución: s2.4 permite redistribuir bajo terminos conmensurables; NO implica IA ni tratar; zip no copiado
- Elegibilidad para tratamiento mediante IA: NO_AUTORIZADA_EN_ESTA_RONDA. Cuenta y acuerdo no ejecutados; términos específicos de IA no comprobados. ImmPort §2.5 excluye diagnóstico y decisiones de tratamiento; no es cláusula de IA.
- Anonimización: Safe Harbor declarado por ImmPort; no auditado en este paquete
- Riesgo de reidentificacion: reidentificar prohibido s1.1; riesgo no cuantificado aqui
- Datos personales presentes: no auditados en deposito; esta ronda no incorpora microdato
- Procedimiento reproducible de obtencion: NO EJECUTADO. Receta: cuenta ImmPort + acuerdo + SDY3324 + leer data dictionary del zip. Prohibido en esta ronda.
- Huella criptográfica, si procede: no procede (sin exportacion)

## Separación epistémica

- Asociaciones que el conjunto permite estudiar: ninguna verificada sobre microdato en esta ronda
- Causalidad demostrada por la fuente: NINGUNA
- Inferencias prohibidas: armonizar N; tratar; cerrar umbral; imputar variables; fusionar familias por rotulo; convertir metadato NCT en deposito
- Consecuencias clínicas constituidas: NINGUNA

## Dictamen candidato

- Estado: ACCESO_PENDIENTE
- Motivo: Ronda 1 de identificación y cribado documental cerrada; CANDIDATO_NO_ADOPTADO; D0-E=0
- Condiciones pendientes: diccionario primario, D0-L completo por finalidad, autorizacion humana expresa antes de cualquier zip
- Fuente primaria de verificación: docs.immport.org/home/agreement 2026-09-01; DR60 expediente D0 2026-08-31; paper JCI Insight e191266; D0L_bloqueo
- Revisor: Grok 2026-09-01
