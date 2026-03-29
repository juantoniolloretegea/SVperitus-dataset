# IMMUNO-2 — Especificación P01–P25 (versión de trabajo)

**Módulo:** IMMUNO-2 – Estratificación del riesgo de infección grave en adultos
con inmunosupresión farmacológica sistémica no trasplante

**Célula:** SV(25,5) — n=25, b=5, T(25)=19

**Semántica:**
- 0 → Riesgo aceptable / situación favorable
- 1 → Riesgo elevado / situación desfavorable
- U → No valorable / información insuficiente

**Regla global:**
- n₁ ≥ 19 → NO_APTO
- n₀ ≥ 19 → APTO
- resto → INDETERMINADO

**Fecha:** 2026-03-06
**Estado:** Versión de trabajo con revisión profunda de la Capa 1.
Capas 2–5 con criterios iniciales pendientes de revisión especializada.

---

## Población diana

Adultos (≥18 años) en tratamiento activo o reciente (≤6 meses) con:
- bDMARDs (anti-TNF, anti-IL-6, anti-IL-17, anti-IL-23, anti-CD20, anti-integrinas)
- tsDMARDs (inhibidores de JAK)
- IS convencionales mayores (micofenolato, azatioprina, ciclofosfamida,
  MTX ≥15 mg/sem, ciclosporina, tacrolimus fuera de trasplante)
- Con o sin corticoides sistémicos

Exclusiones: TOS, TPH/CAR-T, quimioterapia citotóxica pura, VIH primario.

---

## CAPA 1 — Terreno basal del huésped (P01–P05)

Captura factores predisponentes individuales del marco "net state of
immunosuppression" (Roberts & Fishman, CID 2021).

### P01 — Edad

| Valor | Criterio |
|-------|----------|
| 0 | 18–64 años |
| 1 | ≥65 años |
| U | Edad no verificable |

**Ref:** Curtis JR et al., Arthritis Care Res 2012 (infection risk score:
tasa 14.2/100pa en ≥65 vs 4.8 en <65). ORAL Surveillance (NEJM 2022).
RABBIT risk score.

### P02 — Comorbilidad cardiometabólica y renal

| Valor | Criterio |
|-------|----------|
| 0 | Ninguna de: DM complicada, ICC ≥II NYHA, ERC eGFR<60, CI reciente. O comorbilidad menor bien controlada (DM con HbA1c <7.5%, eGFR ≥60) |
| 1 | ≥1 de: DM con HbA1c ≥8% o complicaciones, ICC ≥II NYHA, ERC eGFR <60, cardiopatía isquémica con evento <12m |
| U | Comorbilidades no evaluadas, eGFR o HbA1c no disponibles en últimos 6 meses |

**Ref:** Curtis 2012 (diabetes, CHD, CHF, PVD como componentes del score).
KDIGO 2024 (clasificación ERC). RABBIT (Strangfeld, Ann Rheum Dis 2011).

**Nota:** P02 es compuesto (DM+CV+ERC) deliberadamente. El score de Curtis
los agrupa. Separarlos consumiría 3 de 5 parámetros de la capa.

### P03 — Enfermedad pulmonar crónica

| Valor | Criterio |
|-------|----------|
| 0 | Sin neumopatía crónica estructural. Asma leve/moderada controlada sin exacerbaciones |
| 1 | EPOC con FEV₁ <70% predicho, EPI diagnosticada, bronquiectasias documentadas, o ≥1 exacerbación infecciosa respiratoria en 12m |
| U | Espirometría no realizada en paciente con síntomas respiratorios |

**Ref:** RABBIT risk score (enfermedad pulmonar crónica como variable
independiente). BSRBR-RA (infecciones respiratorias = localización principal).
Singh JA et al., Lancet 2015 (meta-análisis 106 ensayos).

**Nota:** FEV₁ <70% es criterio GOLD de obstrucción moderada+, no un umbral
de riesgo infeccioso validado per se. Decisión de diseño documentada.

### P04 — Hepatopatía crónica

| Valor | Criterio |
|-------|----------|
| 0 | Sin hepatopatía, o esteatosis simple sin fibrosis significativa (F0–F1) |
| 1 | Fibrosis ≥F2, cirrosis (cualquier Child-Pugh), VHB crónica activa, VHC con viremia detectable |
| U | Serología VHB/VHC no disponible, o función hepática no evaluada en paciente con factores de riesgo |

**Ref:** EULAR 2022 (Fragoulis et al.): cribado VHB/VHC obligatorio pre-DMARD.
Child-Pugh (Pugh et al., Br J Surg 1973). Roberts & Fishman CID 2021.

### P05 — Estado nutricional y fragilidad

| Valor | Criterio |
|-------|----------|
| 0 | IMC 18.5–30, albúmina ≥3.5 g/dL (si disponible), sin criterios de fragilidad |
| 1 | IMC <18.5 o >35, o albúmina <3.0 g/dL, o fragilidad documentada (≥3 criterios Fried o equivalente) |
| U | IMC o albúmina no disponibles, o fragilidad no evaluada en paciente ≥70 años |

**Ref:** Roberts & Fishman CID 2021 (déficits nutricionales en net state).
Fried LP et al., J Gerontol 2001 (criterios fragilidad). ESPEN.

**Nota:** Albúmina <3.0 (no <3.5) para criterio 1: captura desnutrición
significativa, no hipoalbuminemia por inflamación. Decisión de diseño.

---

## CAPA 2 — Carga y tipo de inmunosupresión (P06–P10)

Eje central del riesgo. Traduce el régimen IS total en perfil de riesgo
estructurado, integrando evidencia diferencial por tipo de fármaco.

### P06 — Tipo de fármaco inmunosupresor principal

| Valor | Criterio |
|-------|----------|
| 0 | IS convencional en monoterapia a dosis estándar (MTX 15-25mg/sem, AZA ≤2mg/kg/d, LEF) sin corticoides significativos |
| 1 | tsDMARD (JAKi: tofacitinib, baricitinib, upadacitinib), o anti-CD20 (rituximab), o ciclofosfamida, o alemtuzumab |
| U | Fármaco no claramente documentado o no clasificable |

**Ref:** ORAL Surveillance (NEJM 2022): JAKi > anti-TNF en infecciones
oportunistas. Rituximab: hipogammaglobulinemia prolongada y riesgo infeccioso
acumulativo (Tony HP et al., Rheumatology 2011). Ciclofosfamida: IS profunda.

**Nota:** anti-TNF, anti-IL-6, anti-IL-17 se consideran riesgo intermedio;
no activan criterio 1 por sí solos. Esto es una simplificación deliberada
(la realidad es un gradiente), pero operacionaliza la evidencia actual.

### P07 — Combinación de inmunosupresores

| Valor | Criterio |
|-------|----------|
| 0 | Monoterapia o bDMARD + MTX a dosis estándar (combinación habitual, bien estudiada) |
| 1 | ≥2 IS mayores simultáneos (p.ej. MMF + tacrolimus, o biológico + MMF), o triple terapia (biológico + IS convencional + corticoide ≥7.5mg/d) |
| U | Régimen combinado no claramente documentado |

**Ref:** Singh JA et al., Lancet 2015: dosis altas de biológicos y terapia
combinada con DMARD incrementan riesgo (OR 1.90 para high-dose biologics).
EULAR 2024 JAKi consensus: comisoneo IS + JAKi eleva riesgo.

### P08 — Dosis equivalente de corticoides sistémicos

| Valor | Criterio |
|-------|----------|
| 0 | Sin corticoides, o prednisona <7.5 mg/día (o equivalente) durante <4 semanas |
| 1 | Prednisona ≥7.5 mg/día mantenida ≥4 semanas, o ≥15 mg/día cualquier duración, o pulsos recientes (≥250mg metilprednisolona en último mes) |
| U | Dosis no documentada o pauta irregular no cuantificable |

**Ref:** EULAR 2022: profilaxis PJP con prednisona ≥15-30mg/d >2-4 semanas.
Kawashima et al., Rheumatol Int 2017: incluso prednisona 1-4 mg/d aumenta
riesgo en pacientes bajo biológicos. Curtis 2012: dosis de GC como predictor
independiente en infection risk score.

**Nota:** El umbral 7.5 mg/d es más conservador que el de EULAR para PJP
(15mg) pero consistente con la evidencia de riesgo infeccioso general.

### P09 — Duración acumulada de inmunosupresión

| Valor | Criterio |
|-------|----------|
| 0 | Inicio reciente (≤6 meses) de primer régimen IS, o régimen estable >24 meses sin complicaciones infecciosas |
| 1 | IS continua >6 meses con ≥1 cambio de línea por fallo/toxicidad (sugiere enfermedad refractaria y exposición IS acumulada elevada) |
| U | Duración no documentable o historial farmacológico incompleto |

**Ref:** Galloway JB et al., Rheumatology 2011: mayor riesgo en primeros
6 meses, luego estabilización entre 24-36 meses. Bechman K et al., PMC 6443047:
múltiples líneas de bDMARD como predictor de infección.

### P10 — Linfopenia relevante

| Valor | Criterio |
|-------|----------|
| 0 | Linfocitos absolutos ≥1000/μL |
| 1 | Linfocitos absolutos <500/μL mantenidos, o <750/μL en contexto de rituximab o JAKi |
| U | Recuento linfocitario no disponible en últimos 3 meses |

**Ref:** EULAR 2022: linfopenia persistente como factor de riesgo de PJP.
Winthrop KL et al., Ann Rheum Dis 2020: linfopenia bajo baricitinib.
Roberts & Fishman CID 2021: recuentos de subpoblaciones T como marcadores
de riesgo infeccioso.

---

## CAPA 3 — Barreras, dispositivos y anatomía crítica (P11–P15)

Cuantifica brechas en barreras fisiológicas y presencia de superficies
no nativas que favorecen infección grave.

### P11 — Integridad de piel y mucosas

| Valor | Criterio |
|-------|----------|
| 0 | Piel y mucosas íntegras, sin heridas abiertas ni mucositis |
| 1 | Úlceras cutáneas crónicas, mucositis activa, heridas quirúrgicas no cicatrizadas, psoriasis extensa erosiva |
| U | No explorado o no documentado |

**Ref:** Fishman 2017: barreras anatómicas como componente del net state.
IDSA guidelines on skin and soft tissue infections.

### P12 — Catéteres venosos centrales y dispositivos intravasculares

| Valor | Criterio |
|-------|----------|
| 0 | Sin catéter venoso central, port-a-cath ni otros dispositivos intravasculares permanentes |
| 1 | Port-a-cath, PICC, catéter de Hickman o catéter de hemodiálisis implantado |
| U | Presencia de dispositivo no verificable |

**Ref:** Mermel LA et al., CID 2009 (IDSA guidelines on intravascular
catheter-related infections). Fishman 2017.

### P13 — Prótesis y biomateriales

| Valor | Criterio |
|-------|----------|
| 0 | Sin prótesis articulares, vasculares ni otros biomateriales implantados, o prótesis >12 meses sin complicaciones |
| 1 | Prótesis articular o vascular implantada <12 meses, o prótesis con historia de infección periprotésica previa |
| U | Estado protésico no documentado |

**Ref:** Berbari EF et al., CID 2010 (IDSA guidelines prosthetic joint
infection). Riesgo máximo en primer año post-implante.

### P14 — Cirugía mayor reciente

| Valor | Criterio |
|-------|----------|
| 0 | Sin cirugía mayor en los últimos 30 días |
| 1 | Cirugía mayor (torácica, abdominal, ortopédica mayor) en los últimos 30 días |
| U | Historial quirúrgico no disponible |

**Ref:** Goodman SM et al., ACR/AAHKS 2022 guideline on perioperative
management of DMARDs in elective surgery. La suspensión perioperatoria
de biológicos no elimina completamente el riesgo IS residual.

### P15 — Esplenectomía o hipoesplenismo funcional

| Valor | Criterio |
|-------|----------|
| 0 | Bazo presente y funcionante |
| 1 | Esplenectomía quirúrgica, o hipoesplenismo funcional documentado (drepanocitosis, irradiación esplénica, infiltración) |
| U | Función esplénica no evaluada en paciente con riesgo (p.ej. LES, linfoma previo) |

**Ref:** Rubin LG et al., CID 2014 (IDSA guidelines on asplenic patients).
Davies JM et al., BMJ 2011 (guidelines prevention infection in asplenia).

**Nota:** Solapamiento aceptado con P04 de IMMUNO-1 (Función esplénica).
IMMUNO-1 evalúa "¿está protegido el asplénico?"; IMMUNO-2 evalúa
"¿la asplenia eleva su riesgo basal?". Perspectivas distintas, documentado.

---

## CAPA 4 — Exposición epidemiológica documentable (P16–P20)

Incorpora las exposiciones epidemiológicas del marco de Fishman,
restringidas a variables objetivables con criterios 0/1/U reproducibles.

### P16 — Hospitalización reciente

| Valor | Criterio |
|-------|----------|
| 0 | Sin hospitalización ≥48h en los últimos 30 días |
| 1 | ≥1 hospitalización ≥48h en los últimos 30 días |
| U | Historial de ingresos no verificable |

**Ref:** Fishman 2017 (exposiciones nosocomiales). IDSA 2024 AMR guidance
(healthcare-associated infections como categoría de riesgo).

### P17 — Colonización conocida por microorganismos multirresistentes

| Valor | Criterio |
|-------|----------|
| 0 | Sin colonización conocida por MRSA, BLEE, EPC, VRE u otros MDR en los últimos 12 meses |
| 1 | Colonización documentada (frotis de vigilancia positivo o aislamiento clínico) por ≥1 microorganismo MDR en los últimos 12 meses |
| U | Sin cribado de colonización MDR realizado en paciente con exposición hospitalaria frecuente |

**Ref:** IDSA 2024 AMR guidance. ECDC surveillance protocols.
Tacconelli E et al., Clin Microbiol Infect 2014 (ESCMID guidelines
on MDR screening).

### P18 — Residencia o estancia en zona endémica de tuberculosis

| Valor | Criterio |
|-------|----------|
| 0 | Residencia en país de baja endemia TB (<10/100.000), sin viajes recientes a zonas de alta endemia |
| 1 | Residencia o estancia ≥1 mes en zona de alta endemia TB (≥40/100.000) en los últimos 2 años, o contacto estrecho documentado con caso de TB activa |
| U | Historia de viajes/residencia no recogida, o IGRA/TST no realizado pre-tratamiento |

**Ref:** EULAR 2022: cribado de TB latente recomendado pre-bDMARD/tsDMARD.
WHO TB incidence data. ECDC TB surveillance.

### P19 — Exposición documentada a infecciones respiratorias de alto riesgo

| Valor | Criterio |
|-------|----------|
| 0 | Sin exposición conocida a contactos con infecciones respiratorias de transmisión aérea en las últimas 4 semanas |
| 1 | Contacto estrecho documentado con caso confirmado de TB activa bacilífera, COVID-19 grave, influenza en contexto de brote nosocomial, u otra infección respiratoria de declaración obligatoria |
| U | Exposición no evaluable (p.ej. trabajador sanitario sin cribado post-exposición) |

**Ref:** CDC/ECDC guidelines on contact tracing. EULAR 2022: información al
paciente sobre post-exposure prophylaxis (VZV).

### P20 — Exposición a entornos de alto riesgo fúngico

| Valor | Criterio |
|-------|----------|
| 0 | Sin exposición a obras hospitalarias, excavaciones, cuevas, o entornos con riesgo documentado de esporas fúngicas |
| 1 | Exposición a obras de construcción/renovación en instalación sanitaria, o residencia en zona endémica de micosis dimórficas (histoplasmosis, coccidioidomicosis, blastomicosis), o brote fúngico documentado en unidad |
| U | Exposición ambiental no evaluada |

**Ref:** Kanamori H et al., CID 2015 (construction-related aspergillosis).
IDSA guidelines on endemic mycoses. ECIL guidelines on environmental controls.

---

## CAPA 5 — Protección residual, historia infecciosa y puente IMMUNO-1 (P21–P25)

No evalúa infección aguda (fiebre, sepsis). Recoge resiliencia inmunológica
residual, historia infecciosa y el vínculo con IMMUNO-1.

### P21 — Historia de infecciones graves recientes

| Valor | Criterio |
|-------|----------|
| 0 | Sin infección grave (que requiriese hospitalización o IV antibióticos) en los últimos 12 meses |
| 1 | ≥1 infección grave en los últimos 12 meses |
| U | Historial infeccioso no disponible o incompleto |

**Ref:** Bechman K, PMC 6443047: infección grave previa como predictor
independiente en todos los scores de riesgo (RABBIT, Curtis, BSRBR-RA).

### P22 — Inmunoglobulinas séricas (IgG)

| Valor | Criterio |
|-------|----------|
| 0 | IgG ≥700 mg/dL |
| 1 | IgG <400 mg/dL |
| U | IgG no determinada, o IgG 400-699 mg/dL (zona gris sin consenso firme) |

**Ref:** Roberts & Fishman CID 2021 (hipogammaglobulinemia como componente
del net state). EULAR 2022: monitorización de Ig en pacientes bajo rituximab.
Orange JS et al., JACI 2006 (umbral <400 para reposición).

**Nota:** La zona 400–699 se asigna a U, no a 0, porque la evidencia es
ambigua en este rango. El motor la trata como incertidumbre, no como riesgo
aceptable. Decisión de diseño conservadora.

### P23 — Intensificación reciente del régimen inmunosupresor

| Valor | Criterio |
|-------|----------|
| 0 | Régimen IS estable ≥3 meses sin cambios de dosis ni adiciones de fármacos |
| 1 | Adición de nuevo IS o escalada significativa de dosis en los últimos 3 meses (p.ej. paso a biológico, adición de MMF, aumento de corticoides >50%) |
| U | Historial de cambios de tratamiento no documentado |

**Ref:** Galloway 2011: máximo riesgo infeccioso en primeros 6 meses de
terapia biológica. Strangfeld 2011: efecto tiempo-dependiente. La
intensificación reciente indica inestabilidad del régimen y período de
vulnerabilidad máxima.

### P24 — Intervalo desde última evaluación integral de riesgo infeccioso

| Valor | Criterio |
|-------|----------|
| 0 | Evaluación documentada de riesgo infeccioso (screening TB, serologías VHB/VHC, vacunación, profilaxis) realizada en los últimos 12 meses y vigente |
| 1 | Sin evaluación documentada de riesgo infeccioso en >12 meses, o evaluación realizada pero con gaps no resueltos (p.ej. IGRA pendiente, vacunación incompleta) |
| U | No se puede verificar si la evaluación se realizó |

**Ref:** EULAR 2022: screening recomendado pre-inicio y reevaluación periódica
al cambiar de clase de IS. Este parámetro captura el "proceso" de evaluación,
no el resultado (que es dominio de IMMUNO-1).

### P25 — Parámetro puente con IMMUNO-1

| Valor | Criterio |
|-------|----------|
| 0 | IMMUNO-1 clasifica al paciente como APTO y la evaluación es vigente (≤12 meses) |
| 1 | IMMUNO-1 clasifica NO_APTO, o la evaluación está desactualizada (>12 meses), o ausente cuando debería existir |
| U | IMMUNO-1 no aplicado porque no es aplicable (paciente fuera del alcance de IMMUNO-1) o información inaccesible |

**Ref:** Documento 7 (IMMUNO-1). Este parámetro integra el output global
de IMMUNO-1 sin duplicar su evaluación interna. Principio de módulos
independientes pero coordinables en la célula meta n=625.

---

## Solapamientos aceptados y documentados

| IMMUNO-2 | IMMUNO-1 | Justificación |
|----------|----------|---------------|
| P15 (Esplenectomía) | P04 (Función esplénica) | IMMUNO-1: ¿protegido? / IMMUNO-2: ¿riesgo elevado? |
| P10 (Linfopenia) | P02 (Linfopenia/depleción T) | IMMUNO-1: en contexto hematológico / IMMUNO-2: en contexto IS farmacológica no trasplante |
| P25 (Puente) | Todo IMMUNO-1 | Integración sin duplicación |

---

## Guías ancla principales

- Roberts MB, Fishman JA. CID 2021;73(7):e1302-e1317 (net state of IS)
- Fragoulis GE et al. Ann Rheum Dis 2023;82(6):742-753 (EULAR 2022)
- Curtis JR et al. Arthritis Care Res 2012;64:1480-9 (infection risk score)
- Ytterberg SR et al. NEJM 2022;386:316-326 (ORAL Surveillance)
- Singh JA et al. Lancet 2015;386:258-65 (meta-análisis 106 ensayos)
- Strangfeld A et al. Ann Rheum Dis 2011;70:1914-20 (RABBIT)
- Galloway JB et al. Rheumatology 2011;50:124-31 (BSRBR-RA)
- Bechman K et al. PMC 6443047 (prediction of infection risk review)
- Rubin LG et al. CID 2014 (IDSA asplenia guidelines)
- Fishman JA. Am J Transplant 2017;17:856-79 (infection in transplant, marco)

---

## Decisiones de diseño registradas

| # | Decisión |
|---|----------|
| D1 | Subdominio: estratificación riesgo infección grave, IS farmacológica no trasplante |
| D2 | Exclusiones: TOS, TPH/CAR-T, QT citotóxica, VIH primario |
| D3 | Un solo parámetro puente (P25) con IMMUNO-1 |
| D4 | No se evalúan signos de infección aguda |
| D5 | Reglas de oro: motor primero; umbrales anclados; riesgo ≠ agudo; puente sin redundancia |
| D6 | Esplenectomía en Capa 3: solapamiento aceptado con P04 IMMUNO-1 |
| D7 | Hereda hoja de ruta Rust/Kotlin del Doc 7 |
| D8 | case dict estructuralmente análogo al de IMMUNO-1 (JSON, funciones puras) |
| D9 | Texto descriptivo de referencia adoptado como descripción canónica |

---

## Siguiente paso para el hilo que continúe

1. Revisión capa por capa de umbrales y referencias (las Capas 2–5 requieren ajuste fino adicional).
2. Motor normativo Python: normative_engine.py con eval_p01()...eval_p25().
3. YAML: imm2_n25.yaml.
4. Casos sintéticos de prueba (APTO limpio, NO_APTO extremo, INDETERMINADO).
5. Generación de parity_tests/immuno2/.
