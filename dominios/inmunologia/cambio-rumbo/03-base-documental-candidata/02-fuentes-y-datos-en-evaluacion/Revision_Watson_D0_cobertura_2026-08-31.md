# Revisión del corte Watson D0 / D0-L sobre el paquete v0.2

**Pieza:** informe de conversación Watson (2A→2B→D0→D0-L).  
**Contraste:** CSVs/XLSX v0.2 + inventario A1.  
**No se descarga microdato. No se reescribe v0.2. No se adopta D0.**

---

## 0. Veredicto

Las **cifras del paquete** resisten al recuento sobre fichero.  
La **conclusión** (ecosistema amplio ≠ recorte clínico constituido) resiste.  
D0-E = 0, campos de método/unidad/tiempo/desenlace/N = «no comprobado» en las 40 filas: resiste.  
La tabla de colisión D0↔matriz es una **correspondencia propuesta** entre un registro D0 que **no está en artifacts** y A1/v0.2, que **sí** comparten numeración. Dos espacios de nombres son la higiene correcta. No se unen listas con `R03` desnudo.  
SDY3324: candidato declarado; no leído aquí; no es D0-E. Esta unidad no abre ImmPort.

---

## 1. Cifras — comprobadas en disco

| Comprobación Watson | Disco v0.2 | ¿Cuadra? |
|---|---|---|
| 64 parámetros | 64 | sí |
| 27 entidades | 27 | sí |
| 50 relaciones | 50 pares (entity_id, parameter_id) únicos | sí |
| 40 filas de cobertura | 40 | sí |
| 21 parámetros sin relación | 21: P-AU-005, P-CLI-001, P-CLI-002, P-CLI-007, P-CMP-002/003/004, P-HEM-001/002, P-HLH-003, P-IEI-006, P-INF-002, P-IS-003/004, P-LAB-001…005, P-TX-003, P-VIR-005 | sí |
| 1 entidad sin relación | E-IEI-AAE | sí |
| 37 de 50 relaciones sin fila de cobertura | 50−13 pares cubiertos = 37 | sí |
| 0/40 unidad y método | `has_unit_and_method` = no comprobado × 40 | sí |
| 0/40 anclaje temporal | `has_temporal_anchor` = no comprobado × 40 | sí |
| 0/40 desenlace | `has_outcome` = no comprobado × 40 | sí |
| 0/40 medicación concomitante | idem | sí |
| 0/40 tratamiento de ausencias | `missingness_documented` = no comprobado × 40 | sí |
| 0/40 población aplicable | `applicable_population` = no comprobado × 40 | sí |
| 0/40 diccionario y versión | `dictionary_and_version` = no leído estudio a estudio × 40 | sí |
| 0/40 N material | `effective_n_records` = no contado — prohibido inventar N × 40 | sí |

Pares cobertura no huérfanos de relación: 0. Toda fila C-* apunta a un par que existe en relaciones. El agujero es el inverso: 37 relaciones sin C-*.

---

## 2. D0-B = 29 y «11 sin resolución» — cuadra con `coverage_status`

De las 40 filas:

- `inaccesible` = **21**  
- `no aplicable` / `no aplicable como cobertura del episodio` / `no aplicable al parámetro clínico` = **8**  
- resto (`no buscado` y variantes) = **11**

21 + 8 = 29. Watson llama D0-B a esas 29. Las 11 restantes son exactamente las que A1 ya dejó en «no buscado estudio a estudio». No hay D0-E.

Las etiquetas D0-E / D0-R / D0-F / D0-B son de su estratificación. No están en v0.2. El contenido numérico sí.

---

## 3. Identificadores — dos hechos, no uno

**Hecho 1 (disco).** A1 `01_Inventario` y la matriz v0.2 usan el **mismo** mapa:

```
A1/v0.2 R01 ImmPort
A1/v0.2 R02 ImmuneSpace
A1/v0.2 R03 ESID
A1/v0.2 R04 USIDNET
A1/v0.2 R05 REDIP
A1/v0.2 R06 TrialShare
A1/v0.2 R07 IEDB
A1/v0.2 R08 OAS
A1/v0.2 R09 AIRR/iReceptor
A1/v0.2 R10 FlowRepository
A1/v0.2 R11 VDJdb
```

Por eso, contra **este** inventario, «R03 = ESID» no choca.

**Hecho 2 (declaración Watson).** Existe un Registro D0 con permutación (D0-R03 = TrialShare, D0-R09 = ESID, etc.). Ese fichero **no está** en artifacts. No se audita su contenido aquí.

Higiene: prefijo de espacio (`A1:R03` ≠ `D0:R03`). `R03` desnudo en una unión sí corrompería procedencia. Watson no ha modificado archivos; correcto. La correspondencia, si se escribe, es append-only y **otra** tabla. No se reetiquetan las 40 filas.

La adversarial previa que decía «colisión D0↔Grok no demostrable» queda así: no demostrable **en disco**; Watson ahora entrega el mapa conceptual. El mapa no se aplica hasta que D0 esté como archivo versionado.

---

## 4. Fuentes — alineadas con A1, con altas nuevas

Lo ya leído en A1 y que Watson reitera, sin contradicción:

- ImmPort UA 2.5: no diagnóstico ni tratamiento; 2.1 sin garantía.  
- ESID v4.4: seudónimo + consentimiento + acuerdo de centro.  
- USIDNET: waiver, campos mínimos, no minería del registro, no incidencia/prevalencia.  
- REDIP/RePER: acreditación + consentimiento.  
- IEDB/OAS/AIRR/VDJdb: objeto molecular ≠ episodio clínico de IgG/PJP.

Altas que **no** están en las 11 filas de A1:

- BIFAP (AEMPS): candidato longitudinal. Acceso por proyecto autorizado, no dump.  
- MIMIC / PhysioNet: Watson lo saca de IA externa. Coherente con D0-L.  
- CELLxGENE, HCA, HuBMAP, PRIDE, MetaboLights: profundidad ómica, no trayectoria de decisión.  
- AEMS / VAERS / EudraVigilance: señal ≠ causalidad ni riesgo individual.

No se adoptan. No se descargan. Meterlas en A1 exigiría una **fila nueva versionada** (A1 v0.2 o D0), no un append silencioso sobre el xlsx del 31-08.

---

## 5. D0-L

«Ninguna de las 40 filas supera D0-L» es coherente con `legal_access` + `access_status`: cero combinaciones comprobadas de acceso + autorización + licencia + elegibilidad para IA. Shared Data descargable ≠ autorización para motor externo (ImmPort 2.5 + D0-L). No se discute.

---

## 6. SDY3324

Watson lo nombra como primer estudio concreto (vacuna adicional SARS-CoV-2 en AIIRD con MMF/MTX/depleción B).  
En esta unidad **no** se abrió ImmPort ni se leyó el diccionario. Un ensayo publicado con ese diseño existe (p. ej. JCI Insight `e191266`, 2025). La equivalencia ensayo ↔ accesión `SDY3324` **no está verificada aquí**. Estatuto que él declara: pendiente, no D0-E. Se mantiene.

Descender a estudio × población × variables × desenlace × derechos es el siguiente grano. No lo ejecuta esta unidad sin orden de abrir una cuenta o un estudio.

---

## 7. Lo que no sigue de este corte

- Constituir recorte clínico.  
- Asignar D0-R (exige conocimiento clínico constituido; no lo hay).  
- Tratar 40 filas como cobertura empírica.  
- Unir A1 y D0 por `Rnn` desnudo.  
- Pasar SDY3324 a IA externa.  
- Reescribir v0.2 para «arreglar» los 21 parámetros huérfanos.

Los 21 sin relación y E-IEI-AAE ya estaban en la recepción. Siguen siendo residual de **catálogo**, distinto del residual empírico D0-B.
