# Revisión Watson — candidatos SDY y petición de expediente D0

**Pieza:** mensaje Watson al Director (congelar respaldo; no cerrar D0; pide autorización para «Expediente D0 — Auditoría material…»).  
**Esta unidad no genera ese expediente.**  
**No hay descarga. No hay cuenta ImmPort.**

---

## 0. Veredicto

El marco de la petición resiste: documento append-only, no dominio, no parámetros adoptados, no SV, una ficha por estudio con D0 / D0-L / consecuencia de uso indebido.

El contenido de las siete accesiones **no** está materialmente auditado. Dos accesiones aparecen en notas públicas de release ImmPort (DR60). El resto y las cifras 290 / 2.558 / 3.611 no se han podido recontar aquí: las URLs `/shared/study/SDY*` no entregan sinopsis sin autenticación.

Ningún candidato pasa D0-E ni D0-L. ImmPort 2.5 sigue vedando uso asistencial. El flanco IEI sigue vacío. Eso es correcto.

---

## 1. Accesiones — qué se ha podido contrastar sin login

| Accesión | Lo verificado en esta pasada | Lo no verificado |
|---|---|---|
| **SDY3324** | DR60 ImmPort: «SDY3324: COVID-19 booster vaccine in autoimmune disease non-responders (ACV01)». Ensayo abierto, multi-sitio, IS en AIIRD. | Diccionario, variables depositadas, N efectivo, DUA aplicado al paquete |
| **SDY3274** | DR60: «Associating Renal Transplantation With the ITN Signature of Tolerance (ARTIST) (ITN524ST/CTOT-12)». 250 sujetos en la nota de release. NCT01516177. En esa ficha de release: Assays None / Clinical Assessments None | Qué hay realmente en el paquete frente a la nota; régimen TrialShare/ITN vs ImmPort |
| **SDY1414** | URL ImmPort no entrega ficha sin auth. No hay hit bibliográfico que ate «SDY1414» a «290 pediátricos + 2.558 Luminex» | N, órgano, Luminex. CTOTC-04 existe como ensayo de corazón pediátrico; **no** se identifica aquí con SDY1414 |
| **SDY621** | No recontado. «3.611 sujetos» no contrastado | Identidad del estudio y N |
| **SDY218** | No recontado. OIT + provocaciones longitudinales no contrastadas en disco ImmPort | Identidad y diseño |
| **SDY1845** | No contrastada | — |
| **SDY1039** | No contrastada | — |

Regla: sinopsis de release ≠ depósito completo de variables. Watson lo dice. Se mantiene.

---

## 2. Lo que el texto acierta

- Estamos en grano estudio, no en lema de repositorio.  
- Metadatos declarados por ImmPort no equivalen a variables comprobadas.  
- Descarga y verificación exigen autenticación (docs.immport.org File Download Tool: usuario+contraseña).  
- TrialShare/RAVE: candidato de documentación de ensayo; cuenta + cláusula de IA no leídas.  
- 2.5 ImmPort: no diagnóstico ni tratamiento.  
- IEI sin cohorte abierta comprobada.  
- Molecular / farmacovigilancia / ensayo no sustituyen trayectoria clínica.  
- Pedir permiso expreso antes de crear el archivo: correcto.

## 3. Flancos del expediente si usted lo autoriza

No son vetos. Son condiciones de etiqueta:

1. Cada cifra (290, 2.558, 3.611, 250) lleva `fuente_de_la_cifra` = nota DR / página de estudio autenticada / paper / ImmuneSpace. Sin esa columna la cifra es sinopsis.  
2. Espacio de nombres `A1:R01` para ImmPort. No `R01` desnudo ni IDs del D0 permutado.  
3. SDY218 (si es OIT alimentaria) choca con E-FR-ALERGO / RSD-03. La ficha debe decir frontera de dos POE, no «dominio inmunológico cubierto».  
4. SDY1414 / corazón pediátrico toca RSD-08 (histocompatibilidad operativa no está en A1). Luminex DSA ≠ XM CDC operativo.  
5. IEI no se rellena con estos siete. El expediente debe llevar una fila explícita `IEI: sin candidato material en esta ronda`.  
6. D0-L por estudio: Shared Data + registro ImmPort ≠ autorización para IA externa. Hay que escribirlo en cada ficha, no una vez en portada.  
7. Consecuencia de uso indebido: al menos «uso asistencial de ImmPort 2.5» y «inferir umbral PJP / vacuna desde N de un SDY».  
8. No mezclar TrialShare-RAVE con ImmPort-SDY en la misma fila.

## 4. Esta unidad

No genera el expediente. No abre cuenta. No autentica ImmPort.  
Si usted autoriza a Watson, el objeto queda delimitado por el título que él propone y por las ocho condiciones de §3.  
Si autoriza a esta unidad un trabajo paralelo, sería solo plantilla vacía de columnas + las dos filas DR60 ya contrastadas, sin N inventado para las otras cinco.
