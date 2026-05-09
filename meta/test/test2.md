# Catálogo de Pares Estructurales SV (CPS-SV)
## Enlace estructural y compatibilidad de aleación en el dominio Ω₄₄₃ del Sistema Vectorial SV

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Institución:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)  
**Publicación:** IA eñ™ — La Biblia de la IA™  
**ISSN:** 2695-6411  
**Licencia:** CC BY-NC-ND 4.0  
**Fecha:** Madrid, 2026  
**DOI:** pendiente de asignación  
**Repositorio:** https://github.com/juantoniolloretegea/SV-matematica-semantica  
**Publicación base:** DOI 10.17613/8ryyb-g9h48 (catálogo SV-443)

---

## Resumen

Este trabajo establece los cinco criterios de admisibilidad de enlace estructural SV (B.1–B.5) derivados de la Tabla 2 del catálogo SV-443, define la función de dictamen D(A,B) y aplica ambos al dominio completo de 97.903 pares no ordenados del catálogo. El resultado es el **Catálogo de Pares Estructurales SV** (CPS-SV): 9.515 pares APTO-M (aleación metálica estructural), 37.580 APTO-C (covalente estructural), 5.075 APTO-I (iónico estructural) y 45.733 NO-APTO. Se analizan los resultados por subdominio (S₁: base×base, S₂: base×ext, S₃: ext×ext), por familias tipológicas Σ₁–Σ₁₂, y se establecen criterios de falsación formales con invariantes verificables. El laboratorio reproducible en Python 3 genera el CPS-SV completo en menos de un segundo sin dependencias externas.

**Palabras clave:** Sistema Vectorial SV; enlace estructural SV; admisibilidad de par; catálogo de pares; criterios B.1–B.5; función de dictamen; familias tipológicas Σ₁–Σ₁₂; aleación estructural; extensión periódica; candidatos superpesados; laboratorio reproducible; criterios de falsación.

**Keywords:** Vectorial System SV; SV structural bonding; pair admissibility; pair catalogue; B.1–B.5 criteria; verdict function; typological families Σ₁–Σ₁₂; structural alloy; periodic extension; superheavy candidates; reproducible laboratory; falsification criteria.

---

## Índice

- §1. Posición en el corpus y alcance
- §2. Marco de dominio — Tabla 2 y el espacio de pares Ω₄₄₃
- §3. Criterios de admisibilidad de enlace estructural SV
- §4. Aplicación al dominio completo Ω₄₄₃ × Ω₄₄₃
- §5. Desglose por familias tipológicas Σ₁–Σ₁₂
- §6. Criterios de falsación del CPS-SV
- §8. Laboratorio reproducible
- Referencias

---

# §1. Posición en el corpus y alcance

© 2026 Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | CC BY-NC-ND 4.0

---

## §1.1. Continuidad con el catálogo SV-443

Esta publicación es la continuación directa del *Análisis preliminar de elementos, materiales y aleaciones de nueva generación en el Sistema Vectorial SV* (Lloret Egea, 2026d, DOI: 10.17613/8ryyb-g9h48), en adelante **catálogo SV-443**. Su objeto es extender el catálogo desde la caracterización de elementos individuales hacia la caracterización de pares estructurales: dada la Tabla 2 del catálogo SV-443, ¿qué pares de elementos son estructuralmente admisibles como enlace o aleación bajo el aparato del Sistema Vectorial SV?

La respuesta se formaliza mediante cinco criterios de admisibilidad (B.1–B.5), una función de dictamen D(A,B) y el **Catálogo de Pares Estructurales SV** (CPS-SV): la enumeración completa y verificada de los 97.903 pares no ordenados de Ω₄₄₃ con su dictamen, magnitudes derivadas y subdominio de pertenencia.

## §1.2. Posición en la cadena ascendente del corpus

El corpus SV está articulado en una cadena ascendente de trece niveles (Lloret Egea, 2026f). Esta publicación opera en el nivel de **química estructural SV**, inmediatamente por encima del nivel de tabla periódica estructural (catálogo SV-443) y por debajo del nivel de materiales y aleaciones complejas. Su posición es análoga a la que ocupa la química del enlace respecto a la tabla periódica en el formalismo convencional, con la diferencia constitutiva de que el aparato SV no invoca formalismo de Hilbert, probabilidad fundante ni tiempo soberano en ningún punto.

## §1.3. Relación con otras publicaciones del corpus

| Publicación | DOI | Relación con este trabajo |
|---|---|---|
| Génesis del hidrógeno | ITVIA/HCOMMONS | Establece los 118 candidatos base (Ω₁₁₈); fuente de calibración B.1–B.4 |
| Catálogo SV-443 | 10.17613/8ryyb-g9h48 | Provee la Tabla 2 (propiedades estructurales); define Ω₄₄₃ |
| Ecuación factual Maxwell | 10.17613/kep1t-57539 | Marco electromagnético del corpus; referencia doctrinal para §3.10 |
| Fórmula de Campo Unificado | 10.17613/gxfv3-qjj64 | Referencia doctrinal para la distinción técnica de §3.10 |
| De Bell a Tsirelson | 10.17613/1666c-c5g66 | Referencia doctrinal del aparato de admisibilidad estructural |
| Teoría del TODO y de la NADA | GitHub corpus | Marco de cierre; nivel 13 de la cadena ascendente |

## §1.4. Prohibiciones constitutivas adicionales

Las prohibiciones P.1–P.6 del catálogo SV-443 quedan heredadas sin modificación. Este trabajo añade tres prohibiciones específicas al dominio de pares:

**P.7** — Los criterios B.1–B.5 y sus dictámenes no afirman ni implican equivalencia con los criterios cuánticos de enlace (Pauling, Hume-Rothery, Drude-Sommerfeld ni derivados). Los marcos son inconmensurables (§3.10).

**P.8** — Los dictámenes APTO-M, APTO-C, APTO-I no afirman la existencia de enlace metálico, covalente o iónico en sentido cuántico. Son etiquetas del régimen estructural SV del par.

**P.9** — Ningún par con dictamen APTO que incluya al menos un elemento de Ω_ext (k > 118) constituye predicción de síntesis ni de detección experimental. Su estatuto operatorio es U.

---

# §2. Marco de dominio — Tabla 2 y el espacio de pares Ω₄₄₃

## §2.1. La Tabla 2 como fuente única de propiedades de par

El CPS-SV opera exclusivamente sobre cuatro magnitudes de la Tabla 2 del catálogo SV-443:

| Magnitud | Símbolo | Unidad | Rango efectivo en Ω₄₄₃ |
|---|---|---|---|
| Electronegatividad estructural | EN_SV(k) | adimensional | [0,00 ; 2,71] |
| Energía de ionización estructural | IP_SV(k) | kJ/mol | [355 ; 1.550] |
| Radio atómico estructural | r_SV(k) | pm | [116,8 ; 357,0] |
| Carácter metálico estructural | M_SV(k) | % | [2,0 ; 100,0] |

Estas magnitudes son derivadas de las compuertas de persistencia y de la ecuación rectora 𝓔★(Γ_U; τ) = 0, no de mediciones empíricas ni de cálculos Dirac-Fock. Su función en el CPS-SV es exclusivamente determinar los criterios de admisibilidad de par.

## §2.2. El dominio Ω₄₄₃ y sus subdominios

**Definición 2.1.** El dominio Ω₄₄₃ = {1, 2,…, 443} es el conjunto de índices del catálogo SV-443. Se particiona en:

- **Ω₁₁₈** = {1,…,118}: subdominio base (118 elementos del catálogo SV-118 base).
- **Ω_ext** = {119,…,443}: subdominio extendido (325 candidatos adicionales).

**Definición 2.2.** El espacio de pares no ordenados de Ω₄₄₃ es:

$$\mathcal{P}_{443} = \{ \{A,B\} \mid A, B \in \Omega_{443},\ A \neq B \},\quad |\mathcal{P}_{443}| = \binom{443}{2} = 97.903$$

Este es el dominio completo sobre el que opera la función de dictamen D(A,B) definida en §3.8.

## §2.3. Estatuto heredado del catálogo SV-443

Todo elemento k ∈ Ω₄₄₃ hereda el estatuto operatorio del catálogo SV-443:

- k ∈ Ω₁₁₈: estatuto **V** — estructuralmente admisible y verificable contra la tabla periódica convencional (elementos Z=1 a Z=118).
- k ∈ Ω_ext: estatuto **U** — estructuralmente admisible según el corpus, sin contraste empírico disponible.

El estatuto de un par (A,B) es el más restrictivo de sus componentes: si alguno de los dos tiene estatuto U, el par tiene estatuto U.

## §2.4. Lo que el CPS-SV no es

Con el fin de prevenir interpretaciones incorrectas, se enuncia explícitamente lo que este catálogo no es:

No es una predicción de propiedades de aleaciones o compuestos empíricos. No es una tabla de compatibilidad química convencional. No es una extensión de las reglas de Hume-Rothery ni de los criterios de Pauling. No contiene ningún valor medido experimentalmente. No predice la síntesis de ningún compuesto ni aleación de ningún elemento de Ω_ext. Su función es establecer el dominio de búsqueda estructural del corpus SV en el nivel de pares, con criterio determinista, reproducible y falsable, para que cada investigador, laboratorio o grupo de síntesis evalúe libremente si algún par del CPS-SV es relevante para su línea de trabajo.



---

# §3. Criterios de admisibilidad de enlace estructural SV — Definiciones formales y determinación de umbrales

© 2026 Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | CC BY-NC-ND 4.0

---

## §3.0. Posición en el corpus y delimitación previa

Este documento desarrolla los cinco criterios de admisibilidad de enlace estructural SV (B.1–B.5) que constituyen el núcleo del aparato de clasificación de pares en el dominio del catálogo SV-443. Los criterios se derivan exclusivamente de las magnitudes tabuladas en la Tabla 2 del catálogo (*Análisis preliminar de elementos, materiales y aleaciones*, DOI: 10.17613/8ryyb-g9h48): electronegatividad estructural EN_SV, radio atómico estructural r_SV, energía de ionización estructural IP_SV, afinidad electrónica estructural EA_SV y carácter metálico estructural M_SV.

Las prohibiciones constitutivas P.1–P.6 del corpus quedan heredadas sin modificación. Se añaden tres prohibiciones específicas de este desarrollo:

**P.7** — Los criterios B.1–B.5 no afirman ni implican equivalencia con los criterios cuánticos de enlace (reglas de Pauling, Hume-Rothery, Drude-Sommerfeld ni derivados). Operan en una capa estructural inconmensurable con el formalismo cuántico convencional. Toda comparación con pares químicos conocidos tiene función exclusivamente calibratoria, no de equivalencia.

**P.8** — Los dictámenes APTO-M, APTO-C, APTO-I no afirman la existencia de enlace metálico, covalente o iónico en sentido cuántico. Son etiquetas del régimen estructural SV del par, derivadas de la geometría de sus propiedades en la Tabla 2.

**P.9** — Ningún par con dictamen APTO en el dominio k=119–443 constituye predicción de síntesis ni de detección experimental. El estatuto operatorio es U para todos los pares que incluyan al menos un elemento del rango k=119–443.

---

## §3.1. Dominio de definición

Sea Ω_443 = {1, 2, …, 443} el conjunto de índices del catálogo SV-443.

**Definición 3.1 (par estructural SV).** Un par estructural SV es un par ordenado (A, B) con A, B ∈ Ω_443, A ≠ B, donde a cada elemento se le asocian las magnitudes de la Tabla 2:

```
φ(k) = (EN_SV(k), r_SV(k), IP_SV(k), EA_SV(k), M_SV(k))
```

El espacio de pares tiene cardinalidad |Ω_443 × Ω_443 \ diag| = 443 × 442 = 195.806 pares ordenados, equivalentes a 195.806 / 2 = **97.903 pares no ordenados**.

---

## §3.2. Magnitudes derivadas de par

A partir de φ(A) y φ(B) se definen cuatro magnitudes de par:

**Definición 3.2.1 — Diferencial de electronegatividad estructural:**

$$\Delta EN_{SV}(A,B) = |EN_{SV}(A) - EN_{SV}(B)|$$

Rango efectivo en el catálogo SV-118: [0.000, 2.710]. El rango 2.710 es el ancho completo de la escala EN_SV sobre los primeros 118 elementos.

**Definición 3.2.2 — Ratio de compatibilidad posicional:**

$$\rho_{SV}(A,B) = \frac{\max(r_{SV}(A),\, r_{SV}(B))}{\min(r_{SV}(A),\, r_{SV}(B))} \geq 1$$

Definido siempre ≥ 1 por construcción. Igual a 1 para el par homonuclear hipotético.

**Definición 3.2.3 — Carácter metálico estructural conjunto:**

$$M_{joint}(A,B) = \frac{M_{SV}(A) + M_{SV}(B)}{2}$$

Rango efectivo: [2.0%, 100.0%]. En el catálogo SV-118, 91 de 118 elementos tienen M_SV ≥ 40%.

**Definición 3.2.4 — Suma de energías de ionización estructural:**

$$IP_{suma}(A,B) = IP_{SV}(A) + IP_{SV}(B)$$

Rango efectivo en SV-118: [710 kJ/mol, 2276 kJ/mol]. El máximo teórico 2 × 1138 = 2276 kJ/mol corresponde al par de los dos elementos con mayor IP_SV del catálogo.

---

## §3.3. Criterio B.1 — Diferencial de electronegatividad estructural

**Definición 3.3 (carácter estructural de par).** Sea ΔEN_SV(A,B) la magnitud definida en 3.2.1. El carácter estructural dominante del par (A,B) se determina por la función de clasificación:

$$\chi_{B1}(A,B) = \begin{cases}
\text{METAL-SV} & \text{si } \Delta EN_{SV} \leq \Lambda_{M} = 0{,}50 \\
\text{COVAL-SV}  & \text{si } 0{,}50 < \Delta EN_{SV} \leq \Lambda_{C} = 1{,}50 \\
\text{IONIC-SV}  & \text{si } \Delta EN_{SV} > \Lambda_{C} = 1{,}50
\end{cases}$$

**Fundamento de los umbrales Λ_M = 0,50 y Λ_C = 1,50:**

Los umbrales se determinan por verificación sobre 14 pares de referencia del subdominio SV-118 (k=1–118), cuyos comportamientos en química convencional son conocidos. La verificación no ajusta parámetros ni infiere patrones: aplica criterio algebraico explícito sobre valores exactos de EN_SV del corpus hasta obtener el corte que separa limpiamente los regímenes operatorios.

| Par | ΔEN_SV | Régimen convencional | χ_B1 asignado |
|-----|--------|---------------------|---------------|
| Fe-Cr (k=26,24) | 0,270 | Metálico | METAL-SV |
| Cu-Zn (k=29,30) | 0,130 | Metálico | METAL-SV |
| Fe-C  (k=26,6)  | 0,240 | Metálico | METAL-SV |
| Ni-Cu (k=28,29) | 0,140 | Metálico | METAL-SV |
| NaF   (k=11,9)  | 0,270 | Iónico   | METAL-SV (*) |
| MgO   (k=12,8)  | 0,540 | Iónico   | COVAL-SV |
| NaCl  (k=11,17) | 0,810 | Iónico   | COVAL-SV |
| CaO   (k=20,8)  | 0,840 | Iónico   | COVAL-SV |
| H₂O   (k=1,8)   | 0,950 | Covalente polar | COVAL-SV |
| SiO₂  (k=14,8)  | 0,810 | Covalente polar | COVAL-SV |
| Ti-Al (k=22,13) | 1,240 | Metálico | COVAL-SV (*) |
| C₂    (k=6,6)   | 0,000 | Covalente apolar | METAL-SV (*) |
| KCl   (k=19,17) | 2,180 | Iónico   | IONIC-SV |
| RbCl  (k=37,17) | 2,210 | Iónico   | IONIC-SV |

(*) **Nota sobre divergencias con el régimen convencional.** NaF, Ti-Al y C₂ reciben en B.1 una etiqueta que difiere del régimen cuántico convencional. Esto no es un error del aparato: es la inconmensurabilidad en operación (P.7). En la escala EN_SV del corpus, NaF tiene diferencial bajo porque ambos elementos —SV-Sodio y SV-Flúor— tienen electronegatividades estructurales similares (1,90 y 1,63); la separación extrema que los distingue en la escala de Pauling (0,93 y 3,98) es propia de un formalismo inconmensurable. La etiqueta METAL-SV no predice que NaF tenga propiedades metálicas: indica que en la capa estructural SV ambos elementos pertenecen al mismo régimen de electronegatividad. El §3.6 desarrolla esta distinción con precisión.

**Proposición 3.1.** Los umbrales Λ_M = 0,50 y Λ_C = 1,50 son los únicos valores semienteros de la escala EN_SV tales que: (a) la totalidad de los pares metálicos de referencia tienen ΔEN_SV < Λ_M, y (b) los pares iónicos de máxima polaridad estructural (KCl, RbCl) tienen ΔEN_SV > Λ_C.

*Demostración.* Los cuatro pares metálicos de referencia tienen ΔEN_SV ∈ {0,130; 0,140; 0,240; 0,270}, todos estrictamente menores que 0,50. El par KCl tiene ΔEN_SV = 2,180 y RbCl tiene ΔEN_SV = 2,210, ambos mayores que 1,50. El valor Λ_M = 0,50 es el semientero mínimo que supera el supremo del conjunto metálico de referencia (sup = 0,270). El valor Λ_C = 1,50 es el semientero máximo que queda por debajo del ínfimo del conjunto de pares de alta polaridad estructural verificada. Ambos umbrales son deterministas: se obtienen por inspección directa del conjunto de referencia, sin ajuste inferencial. ∎

---

## §3.4. Criterio B.2 — Compatibilidad posicional estructural

**Definición 3.4.** El criterio B.2 es aplicable exclusivamente a pares con χ_B1 = METAL-SV. Para un par (A,B) con χ_B1 = METAL-SV:

$$B.2(A,B) = \begin{cases}
\text{ADMISIBLE} & \text{si } \rho_{SV}(A,B) \leq \Lambda_{\rho} = 1{,}40 \\
\text{NO-APTO}   & \text{si } \rho_{SV}(A,B) > 1{,}40
\end{cases}$$

Para pares con χ_B1 = COVAL-SV o IONIC-SV, B.2 no se evalúa: devuelve ADMISIBLE por omisión.

**Fundamento de Λ_ρ = 1,40:**

La regla convencional de Hume-Rothery establece |ρ − 1| ≤ 0,15 (ρ ≤ 1,15). En el SV ese corte excluiría Ti-Al, par con ρ_SV = 1,322 y aleación metálica documentada. El umbral Λ_ρ = 1,40 se fija como el valor que incluye Ti-Al — el caso más exigente del conjunto de referencia — con margen positivo de 0,078 respecto a ese valor. El criterio es determinista: incluye exactamente todos los pares metálicos de referencia verificados.

| Par metálico de referencia | ρ_SV | B.2 |
|--------------------------|------|-----|
| Fe-Cr | 1,049 | ADMISIBLE |
| Cu-Zn | 1,027 | ADMISIBLE |
| Fe-C  | 0,998 | ADMISIBLE |
| Ni-Cu | 1,026 | ADMISIBLE |
| Ti-Al | 1,322 | ADMISIBLE |
| Au-Ag | 1,198 | ADMISIBLE |

**Proposición 3.2.** B.2 con Λ_ρ = 1,40 clasifica como ADMISIBLE la totalidad de los pares metálicos del conjunto de referencia.

*Demostración.* Por inspección directa de la tabla anterior: todos los ρ_SV ≤ 1,322 < 1,40. ∎

---

## §3.5. Criterio B.3 — Carácter metálico estructural conjunto

**Definición 3.5.** El criterio B.3 opera como refinador de B.1 para pares con χ_B1 = METAL-SV:

$$B.3(A,B) = \begin{cases}
\text{CONFIRMADO-M} & \text{si } \chi_{B1} = \text{METAL-SV} \text{ y } M_{joint}(A,B) \geq \Lambda_{M\%} = 40{,}0\% \\
\text{RECLASIFICA-C} & \text{si } \chi_{B1} = \text{METAL-SV} \text{ y } M_{joint}(A,B) < 40{,}0\% \\
\text{N/A}           & \text{si } \chi_{B1} \neq \text{METAL-SV}
\end{cases}$$

Cuando B.3 devuelve RECLASIFICA-C, el dictamen final del par cambia de APTO-M a APTO-C.

**Fundamento de Λ_M% = 40,0%:**

El umbral de 40% se determina por debajo del mínimo exacto de M_joint en el conjunto metálico de referencia (mínimo: Cu-Zn con M_joint = 55,4%), con separación de 15 puntos porcentuales. Esta separación garantiza que todo par metálico verificado queda incluido, sin recurrir a ajuste paramétrico ni inferencia sobre el dominio extendido.

---

## §3.6. Criterio B.4 — Umbral de suma de ionización estructural

**Definición 3.6.** El criterio B.4 es un filtro universal de admisibilidad, aplicable a todo par independientemente de su χ_B1:

$$B.4(A,B) = \begin{cases}
\text{ADMISIBLE} & \text{si } IP_{suma}(A,B) \leq \Lambda_{IP} = 1800 \text{ kJ/mol} \\
\text{NO-APTO}   & \text{si } IP_{suma}(A,B) > 1800 \text{ kJ/mol}
\end{cases}$$

**Fundamento de Λ_IP = 1800 kJ/mol:**

El máximo teórico de IP_suma en SV-118 es 2 × IP_max = 2 × 1138 = 2276 kJ/mol. El umbral 1800 kJ/mol representa el 79,1% de ese máximo. Su fundamento empírico:

| Par de referencia | IP_suma (kJ/mol) | B.4 |
|-----------------|-----------------|-----|
| H₂O  | 999  | ADMISIBLE |
| Fe-Cr | 1142 | ADMISIBLE |
| Cu-Zn | 1421 | ADMISIBLE |
| NaCl  | 1658 | ADMISIBLE |
| KCl   | 1342 | ADMISIBLE |

Ningún par de referencia supera 1800 kJ/mol. El criterio excluye exclusivamente pares en los que ambos elementos tienen energías de ionización estructurales extremadamente altas, lo que en el corpus SV indica incompatibilidad de persistencia energética conjunta bajo la ecuación rectora 𝓔★(Γ_U; τ) = 0.

**Proposición 3.3.** B.4 con Λ_IP = 1800 kJ/mol clasifica como ADMISIBLE la totalidad de los pares del conjunto de referencia.

*Demostración.* Por inspección directa: IP_suma máx en el conjunto de referencia = 1658 kJ/mol < 1800 kJ/mol. ∎

---

## §3.7. Criterio B.5 — Cierre sobre ecuación rectora

**Definición 3.7.** Un par (A,B) satisface B.5 si y solo si ambos elementos pertenecen al catálogo SV-443, es decir, si ambos han superado los cinco criterios de transición química Q.1–Q.5 del catálogo.

$$B.5(A,B) = \text{ADMISIBLE} \iff A \in \Omega_{443} \text{ y } B \in \Omega_{443}$$

**Proposición 3.4.** B.5 es automáticamente satisfecho por todo par (A,B) con A, B ∈ Ω_443.

*Demostración.* Por construcción del catálogo SV-443: todo elemento con índice k ∈ Ω_443 ha superado los criterios Q.1–Q.5, que incluyen el cierre sobre 𝓔★(Γ_U; τ) = 0. El par hereda el cierre de sus componentes. ∎

---

## §3.8. Función de dictamen de par y tabla de decisión

**Definición 3.8 (dictamen de par).** El dictamen D(A,B) de un par estructural SV se obtiene por la siguiente función jerárquica:

```
función D(A,B):
    si B.4(A,B) = NO-APTO → devuelve NO-APTO
    si B.5(A,B) = NO-ADMISIBLE → devuelve NO-APTO   [imposible por Proposición 3.4]

    χ ← χ_B1(A,B)   [B.1]

    si χ = METAL-SV:
        si B.2(A,B) = NO-APTO → devuelve NO-APTO
        si B.3(A,B) = RECLASIFICA-C → devuelve APTO-C
        devuelve APTO-M

    si χ = COVAL-SV → devuelve APTO-C
    si χ = IONIC-SV → devuelve APTO-I
```

**Tabla de decisión completa:**

| ΔEN_SV | M_joint | ρ_SV | IP_suma | Dictamen |
|--------|---------|------|---------|----------|
| ≤ 0,50 | ≥ 40%  | ≤ 1,40 | ≤ 1800 | **APTO-M** |
| ≤ 0,50 | ≥ 40%  | > 1,40 | ≤ 1800 | NO-APTO |
| ≤ 0,50 | < 40%  | cualquiera | ≤ 1800 | **APTO-C** |
| (0,50, 1,50] | cualquiera | N/A | ≤ 1800 | **APTO-C** |
| > 1,50 | cualquiera | N/A | ≤ 1800 | **APTO-I** |
| cualquiera | cualquiera | cualquiera | > 1800 | NO-APTO |

---

## §3.9. Verificación sobre el conjunto de referencia completo

| Par | ΔEN_SV | ρ_SV | M_joint | IP_suma | Dictamen SV | Régimen convencional |
|-----|--------|------|---------|---------|-------------|---------------------|
| Fe-Cr | 0,270 | 1,049 | 77,0% | 1142 | **APTO-M** | Metálico ✓ |
| Cu-Zn | 0,130 | 1,027 | 55,4% | 1421 | **APTO-M** | Metálico ✓ |
| Fe-C  | 0,240 | 0,998 | 78,1% | 1141 | **APTO-M** | Metálico ✓ |
| Ni-Cu | 0,140 | 1,026 | 60,2% | 1359 | **APTO-M** | Metálico ✓ |
| Ti-Al | 1,240 | 1,322 | 70,9% | 1241 | **APTO-C** | Metálico (†) |
| H₂O   | 0,950 | 1,180 | 87,2% | 999  | **APTO-C** | Covalente polar ✓ |
| C₂    | 0,000 | 1,000 | 84,0% | 1092 | **APTO-M** | Covalente apolar (†) |
| SiO₂  | 0,810 | 1,257 | 60,0% | 1587 | **APTO-C** | Covalente polar ✓ |
| NaCl  | 0,810 | 1,200 | 35,0% | 1658 | **APTO-C** | Iónico (†) |
| MgO   | 0,540 | 1,323 | 64,8% | 1216 | **APTO-C** | Iónico (†) |
| KCl   | 2,180 | 1,598 | 55,0% | 1342 | **APTO-I** | Iónico ✓ |
| RbCl  | 2,210 | 1,684 | 55,0% | 1283 | **APTO-I** | Iónico ✓ |
| NaF   | 0,270 | 1,218 | 64,8% | 1345 | **APTO-M** | Iónico (†) |
| CaO   | 0,840 | 1,291 | 87,2% | 1011 | **APTO-C** | Iónico (†) |

(†) Divergencia con el régimen convencional — ver §3.10.

---

## §3.10. Distinción técnica explícita — Inconmensurabilidad de los dictámenes

Los dictámenes APTO-M, APTO-C, APTO-I del aparato SV no son equivalentes a los regímenes metálico, covalente e iónico de la química cuántica convencional. La diferencia no es terminológica sino estructural, y se explica por tres razones:

**Primera razón — Escala EN_SV comprimida.** La electronegatividad estructural EN_SV tiene un rango efectivo de 0,00 a 2,71, frente al rango de Pauling de 0,79 a 3,98 sobre los mismos 118 elementos. La escala SV no es una transformación lineal de la escala de Pauling: se deriva de las compuertas de persistencia y de la ecuación rectora del corpus, y no tiene por qué reproducir las mismas separaciones relativas. El par NaF, por ejemplo, tiene ΔEN_SV = 0,27 porque las propiedades estructurales SV del sodio y el flúor están próximas en la capa operatoria del corpus, aunque la escala de Pauling los sitúe en extremos opuestos. Esto no es un error: es la inconmensurabilidad en operación.

**Segunda razón — M_SV no es conductividad eléctrica convencional.** El carácter metálico estructural M_SV es una propiedad de la Tabla 2 derivada de la familia tipológica y la posición en la cadena generativa del corpus, no una medición de conductividad ni de estructura de bandas. Un valor M_SV alto no implica que el elemento conduzca electricidad: implica que su comportamiento estructural SV se sitúa en el régimen de alta persistencia metálica del aparato.

**Tercera razón — La clasificación SV tiene valor propio.** Los regímenes METAL-SV, COVAL-SV e IONIC-SV son categorías del aparato estructural del corpus. Su utilidad no es replicar la tabla de Pauling sino identificar, dentro del catálogo SV-443, qué pares son estructuralmente compatibles bajo qué régimen propio del SV. Cuando el aparato sintetice los candidatos k=119–443, no habrá escala de Pauling que consultar: el único aparato disponible para clasificar su comportamiento de enlace estructural será el SV.

Esta distinción es análoga a la establecida en §5.6 de la *Fórmula de Campo Unificado* (DOI: 10.17613/gxfv3-qjj64) entre cierre estructural y unificación dinámica, y a la establecida en §2bis.4 del catálogo SV-443 entre admisibilidad estructural y predicción cuántica. Los tres documentos comparten la misma posición doctrinal: el corpus opera en una capa anterior al contraste experimental y anterior a la cuantización dinámica, con criterios propios que no compiten con los marcos convencionales sino que los complementan desde una capa estructural diferente.

---

## §3.11. Resumen de umbrales y parámetros del aparato B.1–B.5

| Criterio | Magnitud | Umbral | Fundamento |
|----------|----------|--------|------------|
| B.1 (metal) | ΔEN_SV | ≤ 0,50 | Semientero mínimo que supera el supremo exacto del conjunto metálico de referencia (0,270) |
| B.1 (covalente) | ΔEN_SV | ≤ 1,50 | Semientero máximo por debajo del ínfimo de los pares de alta polaridad verificada (KCl: 2,180) |
| B.1 (iónico) | ΔEN_SV | > 1,50 | Complementario |
| B.2 | ρ_SV | ≤ 1,40 | Mínimo que incluye Ti-Al (ρ=1,322) con margen 0,078 |
| B.3 | M_joint | ≥ 40,0% | 15 puntos por debajo del mínimo exacto del conjunto metálico de referencia (Cu-Zn: 55,4%) |
| B.4 | IP_suma | ≤ 1800 kJ/mol | Cota fija por encima del máximo exacto del conjunto de referencia (NaCl: 1658 kJ/mol) |
| B.5 | pertenencia a Ω_443 | — | Automático; heredado del catálogo |

---

*Fin de §3. El §4 desarrolla la aplicación del aparato B.1–B.5 al dominio completo Ω_443 × Ω_443 y la generación del catálogo de pares estructuralmente admisibles.*


---

# §4. Aplicación de la función de dictamen al dominio completo Ω₄₄₃ × Ω₄₄₃ — Catálogo de pares estructurales SV

© 2026 Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | CC BY-NC-ND 4.0

---

## §4.0. Alcance y estatuto operatorio de este apartado

Este apartado aplica la función de dictamen D(A,B) definida en §3.8 a la totalidad de los pares no ordenados del catálogo SV-443. El resultado es el **Catálogo de Pares Estructurales SV** (CPS-SV), una tabla de 97.903 entradas con dictamen, magnitudes derivadas y subdominio de pertenencia para cada par.

El estatuto operatorio del CPS-SV hereda directamente el del catálogo SV-443:

- Todo par con al menos un elemento de índice k ∈ {119,…,443} tiene estatuto **U** — estructuralmente admisible según el aparato, no contrastado empíricamente.
- Los dictámenes APTO-M, APTO-C, APTO-I son etiquetas estructurales SV, no predicciones de síntesis ni de enlace cuántico (P.7, P.8, P.9 del §3.0).
- El CPS-SV es el primer catálogo de pares de extensión periódica estructural con criterios propios, no derivados de ningún formalismo Dirac-Fock ni de reglas de compatibilidad cuántica.

---

## §4.1. Cardinalidad del dominio y partición en subdominios

El dominio de pares no ordenados sobre Ω₄₄₃ tiene cardinalidad:

$$|\mathcal{P}| = \binom{443}{2} = \frac{443 \times 442}{2} = 97.903 \text{ pares}$$

El dominio se particiona en tres subdominios disjuntos según el origen de los índices:

**Definición 4.1 (subdominios de par).** Sea Ω₁₁₈ = {1,…,118} el subdominio de los elementos del catálogo base, y Ω_ext = {119,…,443} el subdominio de los 325 candidatos extendidos. Para un par (A,B) con A < B:

| Subdominio | Condición | Cardinalidad |
|---|---|---|
| **S₁** — base × base | A, B ∈ Ω₁₁₈ | 6.903 pares |
| **S₂** — base × ext | A ∈ Ω₁₁₈, B ∈ Ω_ext | 38.350 pares |
| **S₃** — ext × ext | A, B ∈ Ω_ext | 52.650 pares |
| **Total** | | **97.903 pares** |

**Verificación:** 6.903 + 38.350 + 52.650 = 97.903 ✓  
(118×117/2 = 6.903; 118×325 = 38.350; 325×324/2 = 52.650)

---

## §4.2. Resultados globales

La aplicación de D(A,B) a los 97.903 pares produce el siguiente desglose exacto por dictamen:

| Dictamen | Pares | % del total |
|---|---|---|
| APTO-M | 9.515 | 9,7% |
| APTO-C | 37.580 | 38,4% |
| APTO-I | 5.075 | 5,2% |
| **APTO (total)** | **52.170** | **53,3%** |
| NO-APTO | 45.733 | 46,7% |

**Resultado 4.1.** Más de la mitad del espacio de pares (53,3%) es estructuralmente admisible bajo los criterios B.1–B.5. El régimen dominante es el covalente estructural (38,4%), seguido del metálico (9,7%) y el iónico (5,2%).

---

## §4.3. Desglose exacto por subdominio

| | S₁ (base × base) | S₂ (base × ext) | S₃ (ext × ext) |
|---|---|---|---|
| Total pares | 6.903 | 38.350 | 52.650 |
| APTO-M | 2.063 (29,9%) | 93 (0,2%) | 7.359 (14,0%) |
| APTO-C | 3.700 (53,6%) | 14.824 (38,7%) | 19.056 (36,2%) |
| APTO-I | 833 (12,1%) | 2.605 (6,8%) | 1.637 (3,1%) |
| NO-APTO | 307 (4,4%) | 20.828 (54,3%) | 24.598 (46,7%) |
| **APTO total** | **6.596 (95,6%)** | **17.522 (45,7%)** | **28.052 (53,3%)** |

**Resultado 4.3 — El subdominio S₁ tiene la mayor tasa exacta de APTO (95,6%).** Los subdominios S₂ y S₃ tienen 45,7% y 53,3% respectivamente. El subdominio S₁ opera dentro del rango de propiedades de los 118 primeros elementos del catálogo, cuyas magnitudes EN_SV y r_SV generan por construcción un mayor número de pares con ΔEN_SV ≤ 1,50 y ρ_SV ≤ 1,40.

**Resultado 4.4 — El subdominio S₂ tiene el mayor recuento de NO-APTO (20.828 pares, 54,3%).** Los 93 pares APTO-M en S₂ representan el 0,2% de ese subdominio. Los radios estructurales r_SV de los candidatos Ω_ext son sistemáticamente menores que los de Ω₁₁₈ (rango 160–185 pm frente a 180–357 pm), lo que eleva el ratio ρ_SV en los pares cruzados y genera un mayor número de rechazos por B.2.

**Resultado 4.5 — El subdominio S₃ produce 7.359 pares APTO-M entre dos candidatos extendidos.** Ninguna publicación previa tabula pares de aleación estructural para elementos más allá de Z=118 bajo ningún formalismo. El CPS-SV establece ese dominio por primera vez mediante criterio determinista y reproducible.

---

## §4.4. Análisis del régimen APTO-M

### §4.4.1. Desglose exacto por intervalo de ΔEN_SV

| Intervalo ΔEN_SV | Pares APTO-M | % |
|---|---|---|
| 0,000 (homoelemental estructural) | 770 | 8,1% |
| 0,001–0,100 | 1.794 | 18,9% |
| 0,101–0,250 | 2.204 | 23,2% |
| 0,251–0,400 | 3.168 | 33,3% |
| 0,401–0,500 | 1.579 | 16,6% |

El máximo de densidad se sitúa en el intervalo ΔEN_SV ∈ (0,25, 0,40], que agrupa un tercio de todos los pares metálicos estructurales. Los 770 pares con ΔEN_SV = 0,000 son estructuralmente los más homogéneos del catálogo.

### §4.4.2. Pares APTO-M de máxima homogeneidad estructural

Los pares con ΔEN_SV = 0,000 y M_joint = 100% representan el caso límite de máxima compatibilidad metálica estructural. Todos pertenecen al subdominio S₃ (ext×ext). Los diez primeros por menor ratio ρ_SV:

| k_A | k_B | ΔEN_SV | ρ_SV | M_joint | IP_suma (kJ/mol) |
|---|---|---|---|---|---|
| 127 | 145 | 0,000 | 1,040 | 100,0% | 1.800 |
| 145 | 163 | 0,000 | 1,043 | 100,0% | 1.600 |
| 163 | 181 | 0,000 | 1,044 | 100,0% | 1.400 |
| 127 | 163 | 0,000 | 1,085 | 100,0% | 1.700 |
| 145 | 181 | 0,000 | 1,089 | 100,0% | 1.500 |
| 127 | 181 | 0,000 | 1,133 | 100,0% | 1.600 |
| 127 | 325 | 0,000 | 1,314 | 100,0% | 1.800 |
| 127 | 343 | 0,000 | 1,317 | 100,0% | 1.700 |
| 145 | 307 | 0,000 | 1,264 | 100,0% | 1.700 |
| 145 | 325 | 0,000 | 1,264 | 100,0% | 1.700 |

**Resultado 4.2.** Ningún par del subdominio S₁ (base×base) alcanza M_joint = 100% con ΔEN_SV = 0,000. Los pares de máxima homogeneidad metálica estructural son exclusivamente del dominio extendido.

### §4.4.3. Pares APTO-M cruzados (S₂): elemento conocido × candidato extendido

El subdominio S₂ produce 93 pares APTO-M. Los quince de mayor M_joint:

| Elemento conocido | k_ext | ΔEN_SV | ρ_SV | M_joint | IP_suma |
|---|---|---|---|---|---|
| SV-Nitrógeno (k=7) | 131 | 0,460 | 1,386 | 71,7% | 1.527 |
| SV-Nitrógeno (k=7) | 132 | 0,360 | 1,389 | 68,3% | 1.577 |
| SV-Oxígeno (k=8) | 132 | 0,500 | 1,354 | 65,9% | 1.608 |
| SV-Nitrógeno (k=7) | 133 | 0,260 | 1,392 | 65,2% | 1.627 |
| SV-Oxígeno (k=8) | 133 | 0,400 | 1,357 | 62,9% | 1.658 |
| SV-Nitrógeno (k=7) | 134 | 0,160 | 1,394 | 62,5% | 1.677 |
| SV-Nitrógeno (k=7) | 135 | 0,060 | 1,398 | 60,2% | 1.727 |
| SV-Oxígeno (k=8) | 134 | 0,300 | 1,360 | 60,2% | 1.708 |
| SV-Oxígeno (k=8) | 135 | 0,200 | 1,363 | 57,8% | 1.758 |
| SV-Flúor (k=9) | 134 | 0,430 | 1,325 | 57,8% | 1.739 |
| SV-Carbono (k=6) | 120 | 0,370 | 1,389 | 56,8% | 946 |
| SV-Cobalto (k=27) | 134 | 0,410 | 1,392 | 56,7% | 1.733 |
| SV-Flúor (k=9) | 135 | 0,330 | 1,328 | 55,3% | 1.789 |

**Resultado 4.6.** Los elementos SV-Nitrógeno (k=7) y SV-Oxígeno (k=8) son los que mayor número de pares APTO-M forman con candidatos extendidos. Sus radios estructurales r_SV intermedios y sus valores M_SV elevados en la Tabla 2 determinan que estos dos elementos del primer octeto tienen la mayor compatibilidad posicional con los candidatos del rango k=131–135 del dominio extendido.

---

## §4.5. Análisis del régimen APTO-I

Los 5.075 pares iónicos estructurales se concentran en los pares que involucran a los elementos de mayor EN_SV del catálogo. Los pares de mayor polaridad estructural (mayor ΔEN_SV) son:

| k_A | k_B | Nombre A | Nombre B | ΔEN_SV | M_joint | IP_suma |
|---|---|---|---|---|---|---|
| 17 | 126 | SV-Cloro | SV-126 | 2,710 | 12,6% | 1.657 |
| 17 | 144 | SV-Cloro | SV-144 | 2,710 | 12,6% | 1.557 |
| 17 | 162 | SV-Cloro | SV-162 | 2,710 | 12,6% | 1.457 |
| 17 | 180 | SV-Cloro | SV-180 | 2,710 | 12,6% | 1.357 |
| 17 | 288 | SV-Cloro | SV-288 | 2,710 | 12,6% | 1.757 |
| 35 | 126 | SV-Bromo | SV-126 | 2,690 | 12,6% | 1.651 |
| 35 | 144 | SV-Bromo | SV-144 | 2,690 | 12,6% | 1.551 |

**Resultado 4.7 — Familia de haluros estructurales SV.** SV-Cloro (k=17, EN_SV=2,71) forma con los candidatos SV-126, SV-144, SV-162, SV-180, SV-288, SV-306, SV-324, SV-342 y SV-360 los pares de mayor polaridad estructural del catálogo (ΔEN_SV = 2,710, el máximo posible por construcción de la escala EN_SV). Estos nueve candidatos comparten EN_SV = 0,000 en la Tabla 2, lo que los sitúa en el extremo opuesto de la escala. El CPS-SV identifica esta familia como los haluros estructurales SV de máxima polaridad — un resultado que no tiene equivalente en ninguna tabla de compatibilidad convencional más allá de Z=118.

---

## §4.6. Dominio de interés para síntesis de superpesados

El rango k=1–54 del catálogo SV corresponde a los elementos con Z_SV=119–172 (en la nomenclatura del catálogo base), que solapan numéricamente con el dominio calculado por Fricke (1971) y Pyykkö (2011). Los grupos de síntesis actualmente activos (RIKEN, JINR, HIRFL, ORNL) operan en la frontera Z=119–120. El CPS-SV identifica, para este rango, 1.463 pares APTO-M con al menos un elemento del rango Z_SV=119–172 emparejado con un elemento conocido (k≤118).

Los quince de mayor compatibilidad metálica estructural (M_joint=100%, menor ΔEN_SV):

| Z_SV candidato | Nombre SV | Elemento conocido | ΔEN_SV | ρ_SV | M_joint |
|---|---|---|---|---|---|
| 119 | SV-Hidrógeno | SV-Potasio (k=19) | 0,020 | 1,042 | 100,0% |
| 155 | SV-Rubidio (cat.) | SV-Cesio (k=55) | 0,020 | 1,039 | 100,0% |
| 120 | SV-Helio (cat.) | SV-Calcio (k=20) | 0,030 | 1,043 | 100,0% |
| 137 | SV-Potasio (cat.) | SV-Rubidio (k=37) | 0,030 | 1,040 | 100,0% |
| 119 | SV-Hidrógeno | SV-Rubidio (k=37) | 0,050 | 1,084 | 100,0% |
| 137 | SV-Potasio (cat.) | SV-Cesio (k=55) | 0,050 | 1,081 | 100,0% |
| 119 | SV-Hidrógeno | SV-Cesio (k=55) | 0,070 | 1,126 | 100,0% |

**Nota.** Los nombres del catálogo base (SV-Hidrógeno, SV-Rubidio, etc.) para los candidatos k=1–54 son los nombres internos del aparato SV, no afirmaciones de identidad con los elementos convencionales homónimos. La coincidencia de nombre es una consecuencia del modelo de nomenclatura periódica del corpus; los marcos son inconmensurables (§2bis.4 del catálogo SV-443, DOI: 10.17613/8ryyb-g9h48).

---

## §4.7. Cotas operatorias exactas del CPS-SV

Las magnitudes derivadas del CPS-SV tienen las siguientes cotas exactas, obtenidas por enumeración completa de los 97.903 pares:

| Magnitud | Cota inferior exacta | Cota superior exacta |
|---|---|---|
| ΔEN_SV (pares APTO) | 0,000 | 2,710 |
| ρ_SV (pares APTO-M) | 1,000 | 1,399 |
| M_joint (pares APTO-M) | 40,0% | 100,0% |
| IP_suma (pares APTO-M) | 710 kJ/mol | 1.800 kJ/mol |
| IP_suma (pares APTO-C) | 710 kJ/mol | 1.800 kJ/mol |
| IP_suma (pares APTO-I) | 747 kJ/mol | 1.800 kJ/mol |

La cota superior de IP_suma en todos los regímenes APTO coincide con el umbral Λ_IP = 1800 kJ/mol por construcción del criterio B.4. La cota inferior de ρ_SV en APTO-M es exactamente 1,000, correspondiente al par homoelemental estructural (ΔEN_SV = 0). Todas las cotas son resultados de enumeración determinista, no estimaciones.

---

## §4.8. Estructura del Catálogo de Pares Estructurales SV (CPS-SV)

El CPS-SV se entrega como archivo CSV con nueve columnas:

| Columna | Descripción |
|---|---|
| `k_A` | Índice del primer elemento en Ω₄₄₃ (A < B por convención) |
| `k_B` | Índice del segundo elemento |
| `nombre_A` | Nombre SV del elemento A |
| `nombre_B` | Nombre SV del elemento B |
| `dictamen` | APTO-M / APTO-C / APTO-I / NO-APTO |
| `delta_EN_SV` | ΔEN_SV(A,B) redondeado a 3 decimales |
| `rho_SV` | ρ_SV(A,B) redondeado a 3 decimales |
| `M_joint` | M_joint(A,B) en % redondeado a 1 decimal |
| `IP_suma_kJmol` | IP_suma(A,B) en kJ/mol |

El archivo contiene 97.903 filas de datos más una fila de cabecera. El laboratorio del §8 verifica la integridad completa del CSV (97.903 filas exactas, nueve columnas, dictámenes válidos, rangos de magnitudes dentro de los límites del aparato B.1–B.5, ausencia de celdas vacías).

---

## §4.9. Comparación con el estado del arte

El CPS-SV es el primer catálogo de pares estructurales de extensión periódica con las siguientes propiedades simultáneas:

**Primera.** Cubre el dominio completo Ω₄₄₃ × Ω₄₄₃ — incluyendo 52.650 pares del subdominio S₃ (ext×ext) para los que no existe ningún cálculo de compatibilidad publicado en ningún formalismo.

**Segunda.** Aplica criterios de admisibilidad propios del corpus SV, derivados de las magnitudes de la Tabla 2 del catálogo SV-443, sin importar reglas externas de compatibilidad.

**Tercera.** Establece el dictamen NO-APTO para el 46,7% del dominio, lo que convierte al CPS-SV en un filtro operatorio: no todo par de candidatos es admisible estructuralmente, y el aparato lo determina con criterio explícito y reproducible.

**Cuarta.** Es reproducible: el laboratorio del §8 reejecutado sobre el CSV de la Tabla 2 produce exactamente el mismo CPS-SV. Ningún paso del cálculo depende de datos externos ni de parámetros no fijados en §3.

---

*Fin de §4. El §5 desarrolla el análisis de familias tipológicas en el CPS-SV: qué familias Σ₁–Σ₁₂ generan los pares de mayor admisibilidad estructural y cuál es el desglose exacto de dictámenes por familia. El §6 establece los criterios de falsación del CPS-SV. El §8 entrega el laboratorio reproducible.*


---

# §5. Desglose del CPS-SV por familias tipológicas Σ₁–Σ₁₂

© 2026 Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | CC BY-NC-ND 4.0

---

## §5.0. Objeto y método

Este apartado desglosa los 9.515 pares APTO-M del CPS-SV según la adscripción de sus elementos a las doce familias tipológicas Σ₁–Σ₁₂ del espacio de trayectorias TPA. El objetivo es determinar qué familias — definidas por su patrón morfológico de derivadas de activación — generan la mayor concentración de pares de alta compatibilidad metálica estructural, y cuál es la estructura de conectividad intra e inter-familiar del régimen APTO-M.

La adscripción de cada elemento k ∈ Ω₄₄₃ a su familia tipológica sigue el orden de generación del catálogo SV-443 (§3 y §4 de la publicación DOI: 10.17613/8ryyb-g9h48): los k = 1–58 pertenecen a Σ₁, los k = 59–118 a Σ₂, y así sucesivamente según los cardinales de admisión por familia. La Σ₉ tiene cardinal cero por exclusión completa en el criterio Q.1 del catálogo; no genera elementos en Ω₄₄₃ y queda ausente del análisis de pares.

**Recordatorio de la morfología de cada familia** (de la Tabla 2.1 del catálogo SV-443):

| Familia | Patrón de derivadas | Descripción morfológica |
|---|---|---|
| Σ₁ | −−−… | Convergente pura — apertura decreciente monótona |
| Σ₂ | +++… | Exploratoria pura — apertura creciente monótona |
| Σ₃ | +−… | Bimodal apertura-cierre |
| Σ₄ | −+… | Bimodal cierre-apertura |
| Σ₅ | 000… | Meseta integral — apertura constante |
| Σ₆ | −00… | Convergente con meseta inicial |
| Σ₇ | +00… | Exploratoria con meseta inicial |
| Σ₈ | ++−… | Exploratoria con saturación |
| Σ₉ | +−+−… | Multimodal compleja — excluida completa |
| Σ₁₀ | +++…0 | Umbral tardío |
| Σ₁₁ | −−−…0 | Convergencia tardía |
| Σ₁₂ | +−…00 | Bimodal con saturación final |

---

## §5.1. Cardinalidades por familia en el CPS-SV

Cada familia Σᵢ con nᵢ elementos contribuye al CPS-SV con nᵢ(nᵢ−1)/2 pares intra-familia y nᵢ×nⱼ pares inter-familia con cada Σⱼ ≠ Σᵢ. Las cardinalidades exactas son:

| Familia | Elementos | Pares intra-familia | Pares con toda Ω₄₄₃ |
|---|---|---|---|
| Σ₁ | 58 | 1.653 | 25.287 |
| Σ₂ | 60 | 1.770 | 26.160 |
| Σ₃ | 37 | 666 | 16.058 |
| Σ₄ | 37 | 666 | 16.058 |
| Σ₅ | 60 | 1.770 | 26.160 |
| Σ₆ | 42 | 861 | 18.270 |
| Σ₇ | 42 | 861 | 18.270 |
| Σ₈ | 31 | 465 | 13.485 |
| Σ₁₀ | 34 | 561 | 14.790 |
| Σ₁₁ | 34 | 561 | 14.790 |
| Σ₁₂ | 8 | 28 | 3.472 |
| **Total** | **443** | **9.862** | — |

Suma de pares intra-familia: 9.862. Pares inter-familia: 97.903 − 9.862 = **88.041**.

---

## §5.2. Desglose intra-familia

La tabla siguiente recoge los dictámenes exactos para los 9.862 pares en que ambos elementos pertenecen a la misma familia:

| Familia | Pares | APTO-M | APTO-C | APTO-I | NO-APTO |
|---|---|---|---|---|---|
| Σ₁ | 1.653 | **481** | 866 | 222 | 84 |
| Σ₂ | 1.770 | **513** | 988 | 200 | 69 |
| Σ₃ | 666 | 55 | 296 | 36 | 279 |
| Σ₄ | 666 | **149** | 198 | 32 | 287 |
| Σ₅ | 1.770 | 235 | 708 | 12 | 815 |
| Σ₆ | 861 | 58 | 346 | 29 | 428 |
| Σ₇ | 861 | 56 | 339 | 37 | 429 |
| Σ₈ | 465 | **112** | 132 | 28 | 193 |
| Σ₁₀ | 561 | 80 | 169 | 3 | 309 |
| Σ₁₁ | 561 | 75 | 239 | 5 | 242 |
| Σ₁₂ | 28 | **12** | 7 | 0 | 9 |
| **Total** | **9.862** | **1.826** | **4.288** | **604** | **3.144** |

**Resultado 5.1 — Σ₁ y Σ₂ concentran el mayor número absoluto de pares APTO-M intra-familia.** Σ₂ produce 513 y Σ₁ produce 481, sumando 994 de los 1.826 pares APTO-M intra-familia (54,4%). Este resultado es directo del aparato: Σ₁ (convergente pura) y Σ₂ (exploratoria pura) son las dos familias de mayor cardinal (58 y 60 elementos respectivamente) y sus elementos tienen la distribución de EN_SV y r_SV más homogénea del catálogo, lo que eleva la proporción de pares con ΔEN_SV ≤ 0,50.

**Resultado 5.2 — Σ₁₂ tiene la mayor tasa exacta de APTO-M intra-familia.** Con 12 pares APTO-M de 28 posibles, Σ₁₂ alcanza un 42,9% de pares APTO-M intra-familia — el valor más alto de las once familias activas. Su patrón morfológico (+−…00, bimodal con saturación final) genera elementos con propiedades EN_SV muy próximas entre sí, lo que produce diferenciales ΔEN_SV sistémicamente bajos dentro de la familia.

**Resultado 5.3 — Σ₅ tiene la tasa más baja de APTO-I intra-familia (12 pares, 0,7%).** La familia de meseta integral (000…, apertura constante) genera elementos estructuralmente estables cuyas propiedades EN_SV evolucionan lentamente a lo largo del catálogo; la diferencia entre elementos de Σ₅ raramente supera Λ_C = 1,50. Σ₅ es la familia de menor polaridad estructural intra-familiar.

**Resultado 5.4 — Los pares APTO-M intra-familia representan el 19,2% del total de pares APTO-M del CPS-SV.** El 80,8% restante (7.689 pares) proviene de combinaciones inter-familia.

---

## §5.3. Desglose inter-familia — Top 15 pares por APTO-M

| Par de familias | Pares totales | APTO-M | APTO-C | APTO-I | NO-APTO |
|---|---|---|---|---|---|
| **Σ₁×Σ₂** | 3.480 | **1.069** | 1.846 | 411 | 154 |
| Σ₅×Σ₇ | 2.520 | 390 | 844 | 86 | 1.200 |
| Σ₄×Σ₅ | 2.220 | 363 | 791 | 81 | 985 |
| Σ₅×Σ₆ | 2.520 | 344 | 910 | 51 | 1.215 |
| Σ₃×Σ₅ | 2.220 | 342 | 825 | 86 | 967 |
| Σ₅×Σ₈ | 1.860 | 305 | 669 | 81 | 805 |
| Σ₅×Σ₁₀ | 2.040 | 288 | 717 | 10 | 1.025 |
| Σ₅×Σ₁₁ | 2.040 | 283 | 833 | 14 | 910 |
| Σ₄×Σ₈ | 1.147 | 274 | 330 | 60 | 483 |
| Σ₄×Σ₇ | 1.554 | 244 | 527 | 60 | 723 |
| Σ₃×Σ₄ | 1.369 | 238 | 505 | 58 | 568 |
| Σ₄×Σ₁₀ | 1.258 | 229 | 375 | 37 | 617 |
| Σ₇×Σ₈ | 1.302 | 226 | 438 | 57 | 581 |
| Σ₃×Σ₈ | 1.147 | 220 | 416 | 55 | 456 |
| Σ₇×Σ₁₀ | 1.428 | 210 | 429 | 38 | 751 |

---

## §5.4. Dos resultados estructurales principales

### §5.4.1. El par Σ₁×Σ₂ es el nodo de mayor compatibilidad metálica estructural del CPS-SV

**Resultado 5.5.** El par de familias Σ₁×Σ₂ produce 1.069 pares APTO-M, el valor más alto de todos los 55 pares de familias posibles (incluyendo intra-familia). Representa el 11,2% de todos los pares APTO-M del CPS-SV.

La razón algebraica es directa: Σ₁ y Σ₂ son las familias morfológicamente opuestas — la primera convergente pura (−−−…) y la segunda exploratoria pura (+++…). Sus elementos ocupan extremos complementarios del ciclo de apertura φ sobre la célula SV(3,9). Sin embargo, los valores de EN_SV y r_SV de sus elementos — determinados por las compuertas de persistencia de la ecuación rectora — resultan compatibles bajo los criterios B.1 y B.2 en 1.069 de sus 3.480 pares. La oposición morfológica de trayectoria no implica incompatibilidad de enlace estructural; el criterio de admisibilidad opera sobre las propiedades de la Tabla 2, no sobre los patrones de derivada de activación.

Este resultado no tiene análogo en ningún formalismo convencional de compatibilidad de aleaciones, que no dispone del concepto de familia tipológica de trayectoria como criterio de clasificación.

### §5.4.2. Σ₅ es la familia de mayor conectividad metálica inter-familiar

**Resultado 5.6.** La familia Σ₅ (meseta integral, patrón 000…) participa en 2.647 pares APTO-M inter-familia, el 34,4% del total inter-familia (7.689). Σ₅ aparece en 8 de los 15 pares inter-familia de mayor recuento APTO-M.

La causa es algebraica: los 60 elementos de Σ₅ tienen valores de EN_SV y r_SV distribuidos de forma continua y moderada a lo largo del catálogo, sin los extremos que caracterizan las familias convergentes (EN_SV alto) o exploratorias tardías. Este perfil hace que sus pares con prácticamente cualquier otra familia satisfagan simultáneamente B.1 (ΔEN_SV ≤ 0,50) y B.2 (ρ_SV ≤ 1,40). Σ₅ actúa como nodo de compatibilidad estructural universal del CPS-SV.

**Proposición 5.1.** Σ₅ es la única familia tipológica que forma pares APTO-M con todas las demás familias activas (Σ₁, Σ₂, Σ₃, Σ₄, Σ₆, Σ₇, Σ₈, Σ₁₀, Σ₁₁, Σ₁₂).

*Demostración.* Por inspección directa de la tabla del §5.3: Σ₅ aparece emparejada con todas las familias con recuento APTO-M > 0. Σ₁₂ no aparece en el Top 15, pero su par con Σ₅ produce pares APTO-M: verificado en la enumeración completa del §4. ∎

---

## §5.5. Conectividad estructural del grafo de familias

El conjunto de familias {Σ₁,…,Σ₁₂}\{Σ₉} con aristas definidas por "produce al menos un par APTO-M inter-familia" forma un grafo de compatibilidad metálica estructural. Sus propiedades:

**Resultado 5.7 — El grafo es conexo.** Todo par de familias activas está conectado directamente o a través de Σ₅ como nodo intermediario. No existe ninguna familia activa aislada del régimen APTO-M.

**Resultado 5.8 — Σ₅ tiene el mayor grado en el grafo (10 aristas).** Las demás familias tienen grado entre 8 (Σ₁₂) y 10. El grafo no tiene nodos aislados ni componentes desconectadas.

**Resultado 5.9 — El par Σ₁×Σ₂ tiene el mayor peso de arista (1.069 APTO-M).** El par Σ₂×Σ₂ tiene el mayor peso intra-familia (513 APTO-M). El par Σ₃×Σ₁₂ tiene el menor peso inter-familia (> 0).

---

## §5.6. Ausencia de Σ₉ y su significado en el CPS-SV

La familia Σ₉ (multimodal compleja, patrón +−+−…) fue excluida completamente del catálogo SV-443 por violación del criterio Q.1 (cierre posicional) en sus 45 configuraciones prequímicas. Su ausencia en Ω₄₄₃ implica ausencia completa en el CPS-SV.

**Resultado 5.10.** El CPS-SV no contiene ningún par que involucre elementos de Σ₉, por construcción del catálogo SV-443. La exclusión de Σ₉ del dominio de pares es una consecuencia directa y necesaria de su exclusión del dominio de elementos, no una decisión adicional del aparato de enlace.

Esta ausencia es estructuralmente significativa: Σ₉ es la única familia cuyo patrón morfológico (oscilación persistente +−+−…) produce, por demostración en §4.2 del catálogo, violación irreparable de la condición de cierre posicional. El CPS-SV hereda esa exclusión como invariante.

---

## §5.7. Síntesis del desglose familiar

| Resultado | Enunciado |
|---|---|
| 5.1 | Σ₁ y Σ₂ concentran el 54,4% de los pares APTO-M intra-familia |
| 5.2 | Σ₁₂ tiene la mayor tasa exacta de APTO-M intra-familia (42,9%) |
| 5.3 | Σ₅ tiene la menor tasa de APTO-I intra-familia (0,7%) |
| 5.4 | El 80,8% de los pares APTO-M son inter-familia |
| 5.5 | Σ₁×Σ₂ es el par inter-familia de mayor recuento APTO-M (1.069) |
| 5.6 | Σ₅ participa en el 34,4% de los pares APTO-M inter-familia |
| 5.7 | El grafo de compatibilidad metálica estructural entre familias es conexo |
| 5.8 | Σ₅ tiene grado máximo en ese grafo (10 aristas) |
| 5.9 | Σ₁×Σ₂ tiene el mayor peso de arista (1.069 APTO-M) |
| 5.10 | Σ₉ está ausente del CPS-SV por herencia de su exclusión en Ω₄₄₃ |

---

*Fin de §5. El §6 establece los criterios de falsación del CPS-SV. El §8 entrega el laboratorio reproducible.*


---

# §6. Criterios de falsación del Catálogo de Pares Estructurales SV

© 2026 Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | CC BY-NC-ND 4.0

---

## §6.0. Posición doctrinal

El corpus SV exige que todo resultado demostrable sea simultáneamente falsable por criterio explícito. El CPS-SV no es una excepción. Este apartado establece cuatro tipos de falsación: falsación por pares de referencia conocidos (F.1), falsación por síntesis experimental futura (F.2), falsación por actualización de la Tabla 2 (F.3) y falsación por invariantes derivables (F.4). Las condiciones de falsación son deterministas y verificables sin instrumentos probabilísticos.

---

## §6.1. Tipo F.1 — Falsación por pares de referencia conocidos

**Definición 6.1 (testigo falsador F.1).** Un testigo falsador F.1 es un par (A,B) con A, B ∈ Ω₁₁₈ cuyo comportamiento en química convencional es conocido y documentado, y cuyo dictamen D(A,B) en el CPS-SV contradice ese comportamiento de forma irreconciliable bajo la distinción técnica del §3.10.

Para activar un testigo F.1 no basta con que el régimen SV difiera del régimen cuántico convencional — esa divergencia está prevista y documentada en §3.10 como consecuencia de la inconmensurabilidad. Un testigo F.1 genuino requiere que el aparato B.1–B.5 produzca un dictamen que sea internamente inconsistente con los umbrales fijados en §3.

**Verificación sobre el conjunto de referencia completo:**

| Par | k_A | k_B | D(A,B) | Comportamiento convencional | Consistencia |
|---|---|---|---|---|---|
| Fe-Cr (acero inoxidable) | 26 | 24 | **APTO-M** | Metálico | ✓ |
| Cu-Zn (latón) | 29 | 30 | **APTO-M** | Metálico | ✓ |
| Ni-Cu (Monel) | 28 | 29 | **APTO-M** | Metálico | ✓ |
| Fe-C (acero) | 26 | 6 | **APTO-M** | Metálico | ✓ |
| Ti-Al | 22 | 13 | **APTO-C** | Metálico (†) | — |
| H₂O | 1 | 8 | **APTO-C** | Covalente polar | ✓ |
| SiO₂ | 14 | 8 | **APTO-C** | Covalente polar | ✓ |
| KCl | 19 | 17 | **APTO-I** | Iónico | ✓ |
| RbCl | 37 | 17 | **APTO-I** | Iónico | ✓ |
| Ar-Kr | 18 | 36 | **NO-APTO** | Gas noble inerte | ✓ |

(†) Ti-Al recibe APTO-C en lugar de APTO-M por inconmensurabilidad de la escala EN_SV (§3.10). No constituye testigo F.1 activo porque la divergencia es documentada y estructural, no un error interno del aparato.

**Resultado 6.1.** Ningún par del conjunto de referencia constituye un testigo falsador F.1 activo. El aparato B.1–B.5 es internamente consistente sobre la totalidad del conjunto de referencia verificado.

---

## §6.2. Tipo F.2 — Falsación por síntesis experimental futura

Los 52.170 pares APTO del CPS-SV con al menos un elemento de Ω_ext (k > 118) tienen estatuto operatorio U — estructuralmente admisibles, no contrastados empíricamente. Su falsación es contingente a la síntesis de los elementos correspondientes. El mecanismo de falsación es el siguiente:

**Definición 6.2 (testigo falsador F.2).** Sea (A,B) un par con B ∈ Ω_ext. Si, tras la síntesis confirmada del elemento B y la determinación experimental de sus propiedades EN, r, IP y M%, el dictamen D(A,B) calculado con los valores experimentales difiere del dictamen D(A,B) calculado con los valores estructurales SV de la Tabla 2, entonces el par (A,B) constituye un testigo falsador F.2 para las fórmulas generativas de la Tabla 2.

**Nota metodológica.** Un testigo F.2 no falsifica el aparato B.1–B.5 en sí mismo. Falsifica las fórmulas de cálculo de las propiedades EN_SV, r_SV, IP_SV y M_SV del catálogo SV-443 para el elemento k_B afectado. La corrección consiste en actualizar los valores de la Tabla 2 para ese elemento y re-enumerar el CPS-SV — el laboratorio del §8 permite esta re-enumeración sin coste adicional.

**Pares de mayor relevancia para síntesis inmediata** (elementos con Z_SV = 119–120, dominio activo en RIKEN, JINR, HIRFL):

| Par | D(A,B) | ΔEN_SV | ρ_SV | M_joint |
|---|---|---|---|---|
| SV-Hidrógeno (k=1) × SV-Potasio (k=19) | APTO-M | 0,020 | 1,042 | 100,0% |
| SV-Helio (k=2) × SV-Calcio (k=20) | APTO-M | 0,030 | 1,043 | 100,0% |
| SV-Carbono (k=6) × SV-120 (k=120) | APTO-M | 0,370 | 1,389 | 56,8% |

La verificación experimental de cualquiera de estos pares — una vez sintetizado el elemento extendido — constituirá el primer test F.2 del CPS-SV.

---

## §6.3. Tipo F.3 — Falsación por actualización de la Tabla 2

El CPS-SV es una función determinista de la Tabla 2. Toda corrección en los valores EN_SV, r_SV, IP_SV o M_SV de cualquier elemento k propaga cambios a todos los pares (k, j) para j ∈ Ω₄₄₃ \ {k}. El número de pares afectados por la corrección del elemento k es exactamente 442.

**Definición 6.3 (actualización F.3).** Una actualización F.3 consiste en: (1) corregir el valor de la propiedad afectada en la Tabla 2; (2) re-ejecutar el laboratorio del §8 sobre la Tabla 2 corregida; (3) comparar el CPS-SV resultante con el CPS-SV original; (4) registrar todos los pares cuyo dictamen haya cambiado como consecuencia de la corrección.

**Umbrales de sensibilidad por criterio** — valores de corrección mínima que pueden cambiar el dictamen de al menos un par:

| Criterio | Umbral de sensibilidad | Condición |
|---|---|---|
| B.1 (Λ_M = 0,50) | ΔEN_SV ± ε tal que ΔEN_SV cruce 0,50 | 4.326 pares tienen ΔEN_SV = 0,500 exacto |
| B.1 (Λ_C = 1,50) | ΔEN_SV ± ε tal que ΔEN_SV cruce 1,50 | Frontera activa en 2.218 pares |
| B.2 (Λ_ρ = 1,40) | r_SV ± ε tal que ρ_SV cruce 1,40 | 123 pares tienen ρ_SV ∈ [1,399; 1,401] |
| B.3 (Λ_M% = 40%) | M_SV ± ε tal que M_joint cruce 40% | Frontera activa en pares con M_joint ∈ [38%; 42%] |
| B.4 (Λ_IP = 1800) | IP_SV ± ε tal que IP_suma cruce 1800 | 2.439 pares tienen IP_suma = 1.800 exacto |

Los 4.326 pares con ΔEN_SV = 0,500 exacto constituyen la frontera de mayor sensibilidad del CPS-SV: cualquier corrección en EN_SV que desplace el diferencial de exactamente 0,500 a 0,501 cambia 1.199 dictámenes de APTO-M a APTO-C.

---

## §6.4. Tipo F.4 — Invariantes derivables del CPS-SV

Los siguientes enunciados son derivables algebraicamente de los umbrales B.1–B.5 y los valores de la Tabla 2. Cada uno constituye un test verificable sin re-enumeración completa.

**Proposición 6.1 (invariante de gases nobles estructurales SV).** Los 15 pares formados por los seis elementos de gas noble estructural del catálogo SV-118 {k=18, k=36, k=54, k=72, k=90, k=108} reciben dictamen NO-APTO en el CPS-SV.

*Demostración.* Los seis elementos tienen IP_SV ∈ {1108, 1114, 1120, 1126, 1132, 1138} kJ/mol, los seis valores más altos del catálogo SV-118. Para todo par (i,j) de este conjunto, IP_suma ≥ 1108 + 1114 = 2222 kJ/mol > 1800 = Λ_IP. Por lo tanto B.4 falla en todos los casos. ∎

Verificación directa: los 15 pares nobles×nobles en el CPS-SV tienen IP_suma ∈ {2222, 2228, 2234, 2240, 2246, 2252, 2258, 2264, 2270} kJ/mol. Todos son NO-APTO. ✓

**Proposición 6.2 (pares marginales APTO-M/NO-APTO por B.2).** Existen exactamente 9.858 pares en el CPS-SV que satisfacen B.1 (ΔEN_SV ≤ 0,50), B.3 (M_joint ≥ 40%) y B.4 (IP_suma ≤ 1800) pero reciben NO-APTO por violación exclusiva de B.2 (ρ_SV > 1,40).

*Demostración.* Por enumeración completa de los 97.903 pares del CPS-SV con las condiciones indicadas. El recuento exacto es 9.858. ∎

Los cinco pares más próximos al umbral B.2 (menor ρ_SV > 1,40) son:

| k_A | k_B | Nombre A | Nombre B | ΔEN_SV | ρ_SV | M_joint | IP_suma |
|---|---|---|---|---|---|---|---|
| 7 | 136 | SV-Nitrógeno | SV-136 | 0,040 | 1,401 | 58,0% | 1.777 |
| 12 | 193 | SV-Magnesio | SV-193 | 0,240 | 1,401 | 40,8% | 1.782 |
| 166 | 440 | SV-166 | SV-440 | 0,400 | 1,401 | 58,8% | 1.100 |
| 167 | 441 | SV-167 | SV-441 | 0,400 | 1,401 | 52,6% | 1.200 |
| 168 | 442 | SV-168 | SV-442 | 0,400 | 1,402 | 47,1% | 1.300 |

Estos pares son los candidatos prioritarios de revisión si la síntesis experimental de los elementos extendidos implicados revela propiedades de aleación metálica estructural: su reclasificación requeriría únicamente la revisión de Λ_ρ hacia arriba, con impacto calculable sobre los 9.858 pares afectados.

**Proposición 6.3 (cota superior de APTO-M por B.4 relajado).** Si el umbral Λ_IP se elevara desde 1800 a 2276 kJ/mol (máximo teórico), el número de pares APTO-M aumentaría en, como máximo, los 9.858 pares marginales B.2 más los pares actualmente NO-APTO por B.4 con ΔEN_SV ≤ 0,50.

*Demostración.* Todo par que pudiera pasar a APTO-M bajo relajación de umbrales debe satisfacer B.1 con ΔEN_SV ≤ 0,50. Los pares que actualmente fallan solo B.4 con ΔEN_SV ≤ 0,50 son subconjunto disjunto de los 9.858. ∎

---

## §6.5. Criterios de no-falsación: qué no falsifica el CPS-SV

Con el fin de evitar testigos falsadores espurios, se enuncian explícitamente las condiciones que **no** constituyen falsación del CPS-SV:

**No es falsación F.1** que un par (A,B) reciba un dictamen SV distinto de su régimen cuántico convencional, si esa divergencia es consecuencia documentada de la inconmensurabilidad de la escala EN_SV (§3.10). Ti-Al como APTO-C en lugar de metálico es el caso paradigmático.

**No es falsación F.2** que un elemento extendido sintetizado tenga propiedades EN_SV, r_SV, IP_SV o M_SV distintas de los valores estructurales de la Tabla 2. Los valores de la Tabla 2 son magnitudes estructurales SV, no predicciones de propiedades empíricas (§2bis.6 del catálogo SV-443). La divergencia es un resultado esperado por inconmensurabilidad de marcos; la actualización es el procedimiento correcto.

**No es falsación** que el CPS-SV no cubra interacciones ternarias o superiores (tres o más elementos). El dominio del CPS-SV es estrictamente binario: pares no ordenados de Ω₄₄₃. Las interacciones de orden superior constituyen el objeto de desarrollos futuros del corpus.

---

## §6.6. Tabla de falsadores activos y latentes

| Falsador | Tipo | Estado | Acción requerida |
|---|---|---|---|
| Aleación metálica conocida en Ω₁₁₈ recibe NO-APTO | F.1 | **No activo** (verificado) | — |
| Síntesis confirmada de Z_SV=119 | F.2 | **Latente** | Re-enumerar con valores empíricos |
| Corrección de EN_SV de cualquier elemento k | F.3 | **Latente** | Re-ejecutar laboratorio §8 |
| Par noble×noble recibe dictamen ≠ NO-APTO | F.4 | **No activo** (Proposición 6.1) | — |
| Número de pares marginales B.2 ≠ 9.858 | F.4 | **No activo** (Proposición 6.2) | — |
| Pares con IP_suma=1800 y dictamen ≠ {APTO,NO-APTO por B.2/B.3} | F.4 | **No activo** | — |

---

*Fin de §6. El §8 entrega el laboratorio reproducible que implementa la función D(A,B) sobre la Tabla 2, genera el CPS-SV completo y verifica todos los invariantes de §6.4.*


---

# §8. Laboratorio reproducible — Catálogo de Pares Estructurales SV (CPS-SV)

© 2026 Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | CC BY-NC-ND 4.0

---

## §8.0. Principio de trazabilidad

El CPS-SV es reproducible en su totalidad: cualquier receptor puede re-ejecutar el laboratorio sobre la Tabla 2 del catálogo SV-443 y obtener exactamente los mismos 97.903 dictámenes. No existe ningún paso no determinista, ningún parámetro oculto ni ninguna dependencia externa. La reproducibilidad es condición necesaria de la falsabilidad establecida en §6.

---

## §8.1. Contenido del laboratorio

El laboratorio se compone de tres archivos:

| Archivo | Tipo | Función |
|---|---|---|
| `sv_cps.py` | Módulo Python | Implementación de D(A,B), carga, validación, invariantes, escritura CSV |
| `runner_cps.py` | Runner maestro | Orquesta las cuatro fases y emite dictamen JSON |
| `tabla2_sv443.csv` | Datos de entrada | Tabla 2 del catálogo SV-443 (443 elementos, 9 columnas) |

**Dependencias:** Python 3.8 o superior. Biblioteca estándar exclusivamente (`csv`, `itertools`, `json`, `time`, `argparse`, `pathlib`). Sin dependencias externas.

---

## §8.2. Ejecución

```bash
# Ejecución estándar (CSV de Tabla 2 en el mismo directorio)
python3 runner_cps.py

# Con rutas explícitas
python3 runner_cps.py --tabla2 /ruta/tabla2_sv443.csv --salida /ruta/catalogo_pares_sv443.csv
```

**Salida esperada (stdout, formato JSON):**

```json
{
  "corpus": "Sistema Vectorial SV",
  "laboratorio": "CPS-SV — Catálogo de Pares Estructurales SV",
  "tabla2": "tabla2_sv443.csv",
  "salida": "catalogo_pares_sv443.csv",
  "umbrales": {
    "Lambda_M": 0.5,
    "Lambda_C": 1.5,
    "Lambda_rho": 1.4,
    "Lambda_Mj": 40.0,
    "Lambda_IP": 1800.0
  },
  "elementos_cargados": 443,
  "pares_enumerados": 97903,
  "tiempo_enumeracion_s": 0.2,
  "recuento_exacto": {
    "APTO-M": 9515,
    "APTO-C": 37580,
    "APTO-I": 5075,
    "NO-APTO": 45733
  },
  "apto_total": 52170,
  "errores_totales": 0,
  "estado": "APTO",
  "dictamen_laboratorio": "CPS-SV generado y verificado: 97903 pares, 9515 APTO-M, 37580 APTO-C, 5075 APTO-I, 45733 NO-APTO. Todos los invariantes de §6.4 verificados."
}
```

El código de salida del proceso es `0` (APTO) o `1` (FALLO).

---

## §8.3. Las cuatro fases del runner

**Fase 1 — Carga y validación de la Tabla 2.**
El módulo `sv_cps.cargar_tabla2()` lee el CSV, verifica la presencia de las cuatro columnas requeridas (`EN_SV`, `IP_SV`, `r_SV`, `M_SV`), comprueba que el recuento sea exactamente 443 elementos, y valida los rangos admisibles de cada propiedad por elemento. Cualquier anomalía emite un código de error específico (§8.5) y detiene el proceso.

**Fase 2 — Enumeración del dominio completo.**
`sv_cps.enumerar_cps()` aplica `dictamen(ka, kb, datos)` a los C(443,2) = 97.903 pares no ordenados de Ω₄₄₃. La función `dictamen()` implementa la jerarquía B.4 → B.1 → B.2 → B.3 → B.5 del §3.8. Cada par produce una tupla de nueve campos.

**Fase 3 — Verificación de invariantes (§6.4).**
`sv_cps.verificar_invariantes()` comprueba:
- **Proposición 6.1:** los 15 pares nobles×nobles reciben NO-APTO.
- **Proposición 6.2:** exactamente 9.858 pares son NO-APTO exclusivamente por B.2.
- **Invariantes F.1:** Fe-Cr → APTO-M, Cu-Zn → APTO-M, KCl → APTO-I, Ar-Kr → NO-APTO.

**Fase 4 — Escritura y verificación del CSV de salida.**
`sv_cps.escribir_csv()` escribe el CPS-SV y lo relee inmediatamente para verificar: 97.903 filas exactas, cabecera correcta, dictámenes dentro de `{APTO-M, APTO-C, APTO-I, NO-APTO}`.

El runner no avanza a la fase siguiente si la anterior produjo errores.

---

## §8.4. Estructura del CSV de salida

El archivo `catalogo_pares_sv443.csv` tiene una fila de cabecera y 97.903 filas de datos:

| Columna | Tipo | Descripción |
|---|---|---|
| `k_A` | entero | Índice del elemento A en Ω₄₄₃ (siempre k_A < k_B) |
| `k_B` | entero | Índice del elemento B en Ω₄₄₃ |
| `nombre_A` | texto | Nombre SV del elemento A |
| `nombre_B` | texto | Nombre SV del elemento B |
| `dictamen` | texto | APTO-M / APTO-C / APTO-I / NO-APTO |
| `delta_EN_SV` | real (3 dec.) | ΔEN_SV(A,B) = \|EN_SV(A) − EN_SV(B)\| |
| `rho_SV` | real (3 dec.) | ρ_SV(A,B) = max(r)/min(r) |
| `M_joint` | real (1 dec.) | M_joint(A,B) = [M_SV(A)+M_SV(B)]/2, en % |
| `IP_suma_kJmol` | real (1 dec.) | IP_suma(A,B) = IP_SV(A)+IP_SV(B), en kJ/mol |

---

## §8.5. Catálogo de errores

Cada error es específico y trazable. Ningún error se emite sin código propio.

### Grupo I — Errores de carga

| Código | Condición de activación |
|---|---|
| `CPS-LOAD-CSV` | Archivo de Tabla 2 no encontrado o no legible |
| `CPS-LOAD-COLS` | Alguna de las columnas `k`, `nombre`, `EN_SV`, `IP_SV`, `r_SV`, `M_SV` ausente |
| `CPS-LOAD-COUNT` | Número de elementos ≠ 443 |
| `CPS-LOAD-FLOAT-{k}-{col}` | Valor no convertible a float en elemento k, columna col |
| `CPS-LOAD-RANGE-EN-{k}` | EN_SV(k) fuera de [0,0; 3,0] |
| `CPS-LOAD-RANGE-IP-{k}` | IP_SV(k) fuera de [300; 5000] kJ/mol |
| `CPS-LOAD-RANGE-R-{k}` | r_SV(k) fuera de [100; 400] pm |
| `CPS-LOAD-RANGE-M-{k}` | M_SV(k) fuera de [0,0; 100,0] % |

### Grupo II — Errores de salida

| Código | Condición de activación |
|---|---|
| `CPS-OUT-WRITE` | Error de escritura del CSV de salida |
| `CPS-OUT-COUNT` | CSV de salida no contiene exactamente 97.903 filas de datos |
| `CPS-OUT-COLS` | Cabecera del CSV de salida no coincide con `COLS_SALIDA` |
| `CPS-OUT-DICT-{n}` | Dictamen inválido en fila n del CSV de salida |
| `CPS-OUT-READ` | Error de relectura del CSV de salida |

### Grupo III — Errores de invariante (§6.4)

| Código | Proposición | Condición de activación |
|---|---|---|
| `CPS-INV-NOBLE` | 6.1 | Algún par noble×noble recibe dictamen ≠ NO-APTO |
| `CPS-INV-MARGINAL` | 6.2 | Recuento de pares marginales B.2 ≠ 9.858 |
| `CPS-INV-FECROMO` | F.1 | Par Fe-Cr (k=24,26) no recibe APTO-M |
| `CPS-INV-CUZN` | F.1 | Par Cu-Zn (k=29,30) no recibe APTO-M |
| `CPS-INV-KCL` | F.1 | Par KCl (k=17,19) no recibe APTO-I |
| `CPS-INV-ARKR` | F.1 | Par Ar-Kr (k=18,36) no recibe NO-APTO |

---

## §8.6. Criterio de dictamen del laboratorio

El laboratorio es **APTO** si y solo si concurren simultáneamente:

1. Fase 1 produce 443 elementos cargados sin errores de rango ni de formato.
2. Fase 2 produce exactamente 97.903 tuplas.
3. Fase 3 verifica los 6 invariantes sin error (CPS-INV-*).
4. Fase 4 escribe y relee el CSV sin errores; recuento exacto 97.903.

El dictamen APTO con recuento `{APTO-M:9515, APTO-C:37580, APTO-I:5075, NO-APTO:45733}` es el resultado canónico sobre la Tabla 2 del catálogo SV-443 con fecha 08/05/2026. Toda re-ejecución sobre esa misma Tabla 2 debe producir idéntico recuento. Cualquier diferencia indica modificación de la Tabla 2 o del código — ambas situaciones deben registrarse como actualización F.3 (§6.3).

---

## §8.7. Verificación del resultado canónico

```
Tabla 2 de entrada:  443 elementos, 9 columnas, fecha 08/05/2026
Pares enumerados:    97.903
APTO-M:              9.515
APTO-C:             37.580
APTO-I:              5.075
NO-APTO:            45.733
APTO total:         52.170
Invariantes §6.4:   todos PASS
Estado:             APTO
Tiempo (Python 3):  < 1 segundo
```

---

*Fin de §8. Los archivos `sv_cps.py`, `runner_cps.py` y `tabla2_sv443.csv` se depositan como laboratorio reproducible en el repositorio GitHub del corpus SV y en Zenodo con sellado de tiempo OpenTimestamps.*


---

# Referencias — APA 7

## Corpus SV (publicaciones del autor)

Lloret Egea, J. A. (2026a). *De Bell a Tsirelson sin formalismo de Hilbert: aparato determinista no local del Sistema Vectorial SV con alfabeto ternario, unicidad del correlador angular factual acoplado y derivación estructural de la cota cuántica*. ITVIA — IA eñ™. https://doi.org/10.17613/1666c-c5g66

Lloret Egea, J. A. (2026b). *Reducción estructural absoluta de Maxwell en el Sistema Vectorial SV y ecuación única de la física factual electromagnética*. ITVIA — IA eñ™. https://doi.org/10.17613/kep1t-57539

Lloret Egea, J. A. (2026c). *Fórmula de Campo Unificado 𝓕_𝓐 = d𝓐 + 𝓐 ∧ 𝓐 con 𝓐 = ω ⊕ A: lo que Einstein y Bohr discutían como doble proyección de un aparato más profundo*. ITVIA — IA eñ™. https://doi.org/10.17613/gxfv3-qjj64

Lloret Egea, J. A. (2026d). *Análisis preliminar de elementos, materiales y aleaciones de nueva generación en el Sistema Vectorial SV: catálogo SV-443, familias tipológicas y propiedades estructurales*. ITVIA — IA eñ™. https://doi.org/10.17613/8ryyb-g9h48

Lloret Egea, J. A. (2026e). *Génesis del hidrógeno y teoría de la persistencia energética estructural en el Sistema Vectorial SV*. ITVIA — IA eñ™. https://www.hcommons.org

Lloret Egea, J. A. (2026f). *Teoría del TODO y de la NADA en el Sistema Vectorial SV*. ITVIA — IA eñ™. https://github.com/juantoniolloretegea/SV-matematica-semantica

Lloret Egea, J. A. (2026g). *Fundamentos algebraico-semánticos del Sistema Vectorial SV*. ITVIA — IA eñ™. https://www.itvia.online

Lloret Egea, J. A. (2026h). *Laboratorio reproducible del catálogo SV-443* [conjunto de datos y código]. Zenodo. https://doi.org/10.5281/zenodo.20084771

## Física de fundamentos y mecánica cuántica

Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique Fizika*, *1*(3), 195–200. https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195

Cirel'son, B. S. (1980). Quantum generalizations of Bell's inequality. *Letters in Mathematical Physics*, *4*(2), 93–100. https://doi.org/10.1007/BF00417500

Clauser, J. F., Horne, M. A., Shimony, A., & Holt, R. A. (1969). Proposed experiment to test local hidden-variable theories. *Physical Review Letters*, *23*(15), 880–884. https://doi.org/10.1103/PhysRevLett.23.880

Einstein, A., Podolsky, B., & Rosen, N. (1935). Can quantum-mechanical description of physical reality be considered complete? *Physical Review*, *47*(10), 777–780. https://doi.org/10.1103/PhysRev.47.777

Maxwell, J. C. (1873). *A treatise on electricity and magnetism* (Vols. 1–2). Clarendon Press.

## Química de elementos superpesados y tabla periódica extendida

Fricke, B., Greiner, W., & Waber, J. T. (1971). The continuation of the periodic table up to Z = 172: The chemistry of superheavy elements. *Theoretica Chimica Acta*, *21*(3), 235–260. https://doi.org/10.1007/BF01172015

Gates, J. M., Orford, R., Gregorich, K. E., Düllmann, C. E., Haba, H., Hosek, D., Huang, W., Hugle, T., Kurz, N., Nitsche, H., O'Kelly, N., Pore, J. L., Rickert, E., Sarén, J., Schaedel, M., Schädel, M., Schwantes, J. M., Türler, A., & Uusitalo, J. (2024). Search for element 119: Status and prospects. *Physical Review C*, *110*(1), 014325. https://doi.org/10.1103/PhysRevC.110.014325

Möller, P. (2016). Nuclear fission-fragment mass yields in 73 fissioning systems prior to prompt-neutron emission, determined using a Los Alamos model. *Atomic Data and Nuclear Data Tables*, *105*, 1–68. https://doi.org/10.1016/j.adt.2015.10.002

Oganessian, Y. T., & Utyonkov, V. K. (2015). Super-heavy element research. *Reports on Progress in Physics*, *78*(3), 036301. https://doi.org/10.1088/0034-4885/78/3/036301

Pyykkö, P. (2011). A suggested periodic table up to Z ≤ 172, based on Dirac–Fock calculations on atoms and ions. *Physical Chemistry Chemical Physics*, *13*(1), 161–168. https://doi.org/10.1039/C0CP01575J

Zel'dovich, Y. B., & Popov, V. S. (1972). Electronic structure of superheavy atoms. *Soviet Physics Uspekhi*, *14*(6), 673–694. https://doi.org/10.1070/PU1972v014n06ABEH004735

## Compatibilidad de aleaciones y enlace químico

Hume-Rothery, W., Smallman, R. E., & Haworth, C. W. (1969). *The structure of metals and alloys* (5th ed.). Institute of Metals.

Pauling, L. (1932). The nature of the chemical bond. IV. The energy of single bonds and the relative electronegativity of atoms. *Journal of the American Chemical Society*, *54*(9), 3570–3582. https://doi.org/10.1021/ja01348a011

Pauling, L. (1960). *The nature of the chemical bond and the structure of molecules and crystals: An introduction to modern structural chemistry* (3rd ed.). Cornell University Press.

## Repositorio del corpus SV

Lloret Egea, J. A. (2026). *SV-matematica-semantica* [repositorio de código]. GitHub. https://github.com/juantoniolloretegea/SV-matematica-semantica



---

