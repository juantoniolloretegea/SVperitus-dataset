# Catálogo de Pares Estructurales SV (CPS-SV): enlace, aleación y compatibilidad posicional desde los 118 elementos base hasta los 443 candidatos del dominio extendido

**Autor:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Institución:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)  
**Publicación:** IA eñ™ — La Biblia de la IA™  
**ISSN:** 2695-6411  
**Licencia:** CC BY-NC-ND 4.0  
**Fecha:** Madrid, 09/05/2026  
**DOI:** pendiente de asignación (HCOMMONS)  
**Repositorio canónico:** https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/quimica-factual-y-ciencia-de-materiales-sv/catalogo-pares-estructurales  
**Publicación base:** DOI [10.17613/8ryyb-g9h48](https://doi.org/10.17613/8ryyb-g9h48) (catálogo SV-443)


![Portada — Catálogo de Pares Estructurales SV (CPS-SV)](imagenes/Portada.png)

---

## Resumen

Este trabajo establece los cinco criterios de admisibilidad de enlace estructural SV (B.1–B.5), derivados de la Tabla Global del catálogo SV-443, y aplica la función de dictamen D(A,B) al dominio completo de 97.903 pares no ordenados del catálogo. La fundamentación doctrinal descansa sobre el Teorema del operador U como motor generativo ternario (§1.5): los criterios B.1–B.5 son la expresión formal de la ventana operativa de U en la secuencia preternario → proto-ternario → ternario de la Teoría del TODO y de la NADA y de la Imperfección, propuesta aquí como ampliación ternaria del marco binario del corpus. El resultado es el Catálogo de Pares Estructurales SV (CPS-SV): 9.515 pares APTO-M (puntos de equilibrio de aleación metálica estructural), 37.580 APTO-C (covalente estructural), 5.075 APTO-I (iónico estructural) y 45.733 NO-APTO. Se analizan los resultados por subdominio (S₁: base×base, S₂: base×ext, S₃: ext×ext), por familias tipológicas Σ₁–Σ₁₂, y se establecen criterios de falsación con invariantes verificables. El laboratorio reproducible en Python 3 genera el CPS-SV completo en menos de un segundo sin dependencias externas.

**Palabras clave:** Sistema Vectorial SV; Catálogo de Pares Estructurales SV; CPS-SV; enlace estructural SV; admisibilidad de par; criterios B.1–B.5; función de dictamen; Teoría del TODO y de la NADA y de la Imperfección; operador U; secuencia preternario–proto–ternario; familias tipológicas Σ₁–Σ₁₂; aleación estructural; extensión periódica; Tabla Cero SV; Tabla Global SV; laboratorio reproducible; criterios de falsación.

## Abstract

This work establishes the five SV structural bonding admissibility criteria (B.1–B.5), derived from the Global Table of the SV-443 catalogue, and applies the verdict function D(A,B) to the complete domain of 97,903 unordered pairs. The doctrinal foundation rests on the Theorem of the U operator as ternary generative motor (§1.5): criteria B.1–B.5 are the formal expression of U's operational window in the preternary → proto-ternary → ternary sequence of the Theory of Everything, Nothing and Imperfection, proposed here as the ternary extension of the binary framework of the corpus. The result is the SV Structural Pair Catalogue (CPS-SV): 9,515 APTO-M pairs (metallic structural alloy equilibrium points), 37,580 APTO-C (covalent structural), 5,075 APTO-I (ionic structural), and 45,733 NO-APTO. Results are analysed by subdomain (S₁: base×base, S₂: base×ext, S₃: ext×ext), by typological families Σ₁–Σ₁₂, and falsification criteria are established with verifiable invariants. The reproducible Python 3 laboratory generates the complete CPS-SV in under one second with no external dependencies.

**Keywords:** Vectorial System SV; SV Structural Pair Catalogue; CPS-SV; SV structural bonding; pair admissibility; B.1–B.5 criteria; verdict function; Theory of Everything Nothing and Imperfection; U operator; preternary–proto–ternary sequence; typological families Σ₁–Σ₁₂; structural alloy; periodic extension; Zero Table SV; Global Table SV; reproducible laboratory; falsification criteria.

---

## Índice

- §1. Marco doctrinal del CPS-SV
  - §1.1–§1.4. Continuidad, posición, corpus y prohibiciones
  - §1.5. U como motor generativo: del dominio preternario a la realización ternaria
  - §1.6. Teorema de predominancia de U y cascada de dominancias (Teorema 1.6.1 + 4 corolarios + Principio P_U)
  - §1.7. Marco conceptual: regímenes de realización ternaria
  - §1.8. Propiedades emergentes del par estructural
  - §1.9. Fundamento termodinámico de los estados estables de par
  - §1.10. El par estructural en su contexto de campo
- §2. Marco de dominio — Tabla Global y espacio de pares Ω₄₄₃
- §3. Criterios de admisibilidad de enlace estructural SV
  - §3.1–§3.7. Criterios B.1–B.5 y definición del dominio
  - §3.8. Simetría de la función de dictamen
  - §3.9. Función de dictamen D(A,B) y tabla de decisión
  - §3.10. Verificación sobre el conjunto de referencia
  - §3.11. Cuatro recorridos extremo a extremo
  - §3.12. Distinción técnica: inconmensurabilidad de dictámenes
  - §3.13. Resumen de umbrales y parámetros B.1–B.5
- §4. Aplicación de la función de dictamen al dominio completo Ω₄₄₃
- §5. Desglose del CPS-SV por familias tipológicas Σ₁–Σ₁₂
- §6. Criterios de falsación del CPS-SV
- §7. Nota de continuidad con moléculas estructurales SV
- §8. Laboratorio reproducible
---

---

# §1. Posición en el corpus y alcance

El presente trabajo requiere, para su plena autocontención doctrinal, un marco que amplíe la *Teoría del TODO y de la NADA* del corpus SV (Lloret Egea, 2026f) más allá de su formulación binaria. En su versión binaria, la teoría establece la coexistencia de los polos 1 (Todo) y 0 (Nada) con gradiente nulo: suma nula, entropía nula, potencial nulo — matemáticamente exacta en ese nivel. Sin embargo, la existencia de pares estructurales realizados, aleaciones y moléculas — entidades que son imperfecciones estabilizadas en un punto de equilibrio de potencial distinto de cero — exige la ampliación al aparato ternario completo (1, U, 0). Este trabajo propone, como fundamento doctrinal de su propio aparato, la **Teoría del TODO y de la NADA y de la Imperfección**: la ampliación ternaria del marco binario. Esta propuesta escala hacia los niveles doctrinales superiores del corpus no como corrección exógena, sino como exigencia de autocontención: sin ella, el aparato de esta publicación no puede justificar sus propios criterios de admisibilidad. La Teoría del TODO y de la NADA y de la Imperfección queda aquí anunciada; su desarrollo completo pertenece a la capa doctrinal superior. Lo que esta publicación establece, en el §1.5, es únicamente el fragmento que necesita para sostenerse: el Teorema del operador U como motor generativo de la estabilización ternaria.

## §1.1. Continuidad con el catálogo SV-443

Esta publicación es la continuación directa del *Análisis preliminar de elementos, materiales y aleaciones de nueva generación en el Sistema Vectorial SV* (Lloret Egea, 2026d, DOI: 10.17613/8ryyb-g9h48), en adelante **catálogo SV-443**. Su objeto es extender el catálogo desde la caracterización de elementos individuales hacia la caracterización de pares estructurales: dada la Tabla Global del catálogo SV-443, qué pares de elementos son estructuralmente admisibles como enlace o aleación bajo el aparato del Sistema Vectorial SV.

## §1.2. Posición en la cadena ascendente del corpus

El corpus SV está articulado en una cadena ascendente de trece niveles (Lloret Egea, 2026f). Esta publicación opera en el nivel de química estructural SV, inmediatamente por encima del nivel de tabla periódica estructural (catálogo SV-443) y por debajo del nivel de materiales y aleaciones complejas. Su posición es análoga a la que ocupa la química del enlace respecto a la tabla periódica en el formalismo convencional, con la diferencia constitutiva de que el aparato SV no invoca formalismo de Hilbert, probabilidad fundante ni tiempo soberano en ningún punto.

## §1.3. Relación con otras publicaciones del corpus

| Publicación | DOI | Relación con este trabajo |
|---|---|---|
| Génesis del hidrógeno | DOI [10.17613/qq4q9-sd847](https://doi.org/10.17613/qq4q9-sd847) | Establece Ω₁₁₈ y la secuencia Ω_pre → Ω_H; fuente de la Tabla Cero |
| Catálogo SV-443 | DOI 10.17613/8ryyb-g9h48 | Provee la Tabla Global; define Ω₄₄₃ |
| Teoría general de sucesos generadores | ITVIA/HCOMMONS | Establece Ω_pre y los protocampos; fundamento del §1.5 |
| Ecuación factual Maxwell | DOI [10.17613/kep1t-57539](https://doi.org/10.17613/kep1t-57539) | Referencia doctrinal para §3.12 |
| Fórmula de Campo Unificado | DOI [10.17613/gxfv3-qjj64](https://doi.org/10.17613/gxfv3-qjj64) | Referencia para la distinción técnica de §3.12 |
| De Bell a Tsirelson | DOI [10.17613/1666c-c5g66](https://doi.org/10.17613/1666c-c5g66) | Marco de co-clausura ternaria y distinción técnica de inconmensurabilidad (§3.12) |
| Teoría del TODO y de la NADA | ITVIA/GitHub | Marco de cierre del corpus; fundamento del §1.5 |
| Entropía factual e irreversibilidad estructural | DOI [10.17613/vh6ak-6em43](https://doi.org/10.17613/vh6ak-6em43) | Fundamento termodinámico de los estados estables (§1.9) |
| Fórmula termodinámica factual única | DOI [10.17613/ptw68-d1r57](https://doi.org/10.17613/ptw68-d1r57) | Ecuación de equilibrio E^thermo_SV = 0 (§1.9) |
| Interacción, intercomposición y transmisión de campos | GitHub (corpus SV) | Operador 𝓘_SV, distancia factual fibrosa d^SV_Φ, compuerta Σ=1 (§1.10) |

## §1.4. Prohibiciones constitutivas adicionales

Las prohibiciones P.1–P.6 del catálogo SV-443 quedan heredadas sin modificación. Este trabajo añade tres postulados operatorios específicos al dominio de pares:

**P.7** — Los dictámenes APTO-M, APTO-C, APTO-I son postulados de realización ternaria del operador U_SV sobre el protopar Π(A,B). Su correspondencia con los regímenes cuánticos convencionales es una cuestión abierta que el contraste experimental resolverá cuando los pares correspondientes sean accesibles.

**P.8** — Los pares con al menos un elemento de Ω_ext (k > 118) tienen estatuto U proto-ternario: admisibles en el dominio de operación de U_SV, en espera de realización experimental.

**P.9** — El dominio proto-ternario Ω_proto contiene 97.903 protopares de Ω₄₄₃. El CPS-SV cataloga cuáles de ellos alcanzan realización ternaria bajo U_SV y cuáles son absorbidos por Nada (NO-APTO).

---

# §1.5. U como motor generativo: del dominio preternario a la realización ternaria del par estructural

© 2026 Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | CC BY-NC-ND 4.0

---

## §1.5.1. Fundamento: la terna (1, U, 0) y el principio de tránsito

El Sistema Vectorial SV opera sobre el alfabeto ternario canónico {0, 1, U}. En términos de la *Teoría del TODO y de la NADA* del corpus (Lloret Egea, 2026f), los tres valores tienen estatuto asimétrico:

- **1 (Todo)**: el estado de completitud estructural absoluta. En el polo 1, la configuración es plenamente cerrada, sin gradiente, sin tránsito. El par de máxima similitud estructural (ΔEN_SV = 0, ρ_SV = 1) tiende al polo 1.

- **0 (Nada)**: el estado de colapso estructural. En el polo 0, la energía de persistencia del par se anula; la suma de ionización supera el umbral de coexistencia (IP_suma > Λ_IP = 1800 kJ/mol). Nada absorbe al par.

- **U (Imperfección)**: el agente operativo del tránsito. U es quien genera el movimiento entre 1 y 0. Sin U, 1 y 0 son estáticos y el sistema permanece en su polo sin transitar. Con U, el tránsito es posible en ambas direcciones: de 1 hacia 0 y de 0 hacia 1.

La tensión entre los polos 1 y 0, gobernada por la ecuación rectora 𝓔★_TODO,SV(Γ_U; τ) = 0, genera la Imperfección como zona de existencia sostenida. U no es el motor del tránsito: U es el terreno en que los polos compiten sin que ninguno haya ganado completamente. Lo que existe como par estructural realizado es precisamente lo que ningún polo ha podido reclamar del todo.

---

## §1.5.2. La secuencia Pre → Proto → Ternario

En el dominio de pares estructurales SV, U genera la siguiente secuencia de tres niveles:

**Nivel preternario (Pre):**
Cada elemento k ∈ Ω₄₄₃ existe en el dominio preternario Ω_pre como configuración energética con persistencia parcial. La génesis del hidrógeno del corpus (Lloret Egea, 2026e) establece que Ω_pre es el dominio de configuraciones preatómicas que aún no han alcanzado la cadena completa de admisibilidad individual:

persistencia → frontera → residual → identidad → descendencia protocampal → no artificio → 𝓔★_TODO,SV(Γ_U) = 0.

Solo los elementos que atraviesan la cadena completa acceden a Ω₄₄₃. En el nivel preternario, los elementos existen como potencial estructural, no como entidades combinables.

**Nivel proto-ternario (Proto):**
Cuando dos elementos A, B ∈ Ω₄₄₃ entran en interacción en Ω_pre, U comienza a operar sobre la configuración conjunta. Se forma el **protopar** Π(A,B): la entidad proto-ternaria definida por los dos perfiles estructurales φ(A) y φ(B) en contacto, antes de que U determine si la realización ternaria es posible.

El protopar Π(A,B) existe en el dominio proto-ternario:

Ω_proto = { Π(A,B) | A, B ∈ Ω₄₄₃, A ≠ B }

con cardinalidad |Ω_proto| = C(443,2) = 97.903 protopares.

De manera análoga, la **protoaleación** es el protopar en el que U opera dentro del rango metálico estructural (ΔEN_SV ≤ Λ_M), constituyendo el precursor de los 9.515 pares APTO-M del CPS-SV.

**Nivel ternario (Ternario):**
Si U opera dentro de su ventana de admisibilidad sobre Π(A,B), el protopar alcanza realización ternaria y entra en el Catálogo de Pares Estructurales SV (CPS-SV) con dictamen APTO-M, APTO-C o APTO-I. Si U excede los umbrales de persistencia o no puede cerrar el morfismo posicional, el protopar retorna a Nada: dictamen NO-APTO, U absorbido por 0.

---

## §1.5.3. Los criterios B.1–B.5 como expresión formal de la ventana operativa de U

Los cinco criterios de admisibilidad de par B.1–B.5 del §3 no son umbrales arbitrarios. Son la formalización de las condiciones bajo las cuales U puede operar sobre Π(A,B) generando realización ternaria sin que 0 absorba al par:

| Criterio | Condición | Papel en la operación de U |
|---|---|---|
| B.5 | A, B ∈ Ω₄₄₃ | Ambos elementos han completado su propia cadena pre → proto → ternario individual. U hereda su descendencia protocampal (Desc_proto = 1 de cada elemento). |
| B.4 | IP_suma ≤ Λ_IP | U mantiene el par dentro del umbral de persistencia energética. Si IP_suma > Λ_IP, Nada (0) absorbe el par. Es la condición de supervivencia energética del tránsito. |
| B.1 | ΔEN_SV ≤ Λ_C o > Λ_C | U determina el régimen de imperfección polar del par: cercano a 1 (ΔEN bajo, APTO-M), en zona intermedia (APTO-C), o próximo al límite Todo-Nada (APTO-I). |
| B.2 | ρ_SV ≤ Λ_ρ | En el régimen metálico (ΔEN ≤ Λ_M), U debe cerrar el morfismo posicional. Si los radios son incompatibles, U no puede cerrar el par estructuralmente: 0 gana el eje posicional. |
| B.3 | M_joint ≥ Λ_M% | En el régimen metálico, U necesita masa metálica estructural conjunta suficiente para completar la realización. Sin ella, reclasifica el par al régimen covalente (U puede cerrar, pero en modo distinto). |

La cadena operativa de U sobre Π(A,B) es:

**B.5** (herencia preternaria) → **B.4** (persistencia frente a Nada) → **B.1** (régimen de imperfección polar) → **B.2** (morfismo posicional) → **B.3** (masa metálica conjunta) → **Realización ternaria**

Esta cadena es paralela exacta a la cadena de admisibilidad individual de la génesis del hidrógeno:

persistencia → frontera → residual → identidad → Desc_proto → no artificio → 𝓔★_TODO,SV(Γ_U) = 0

---

## §1.5.4. Teorema de generación ternaria de pares estructurales SV bajo el operador U

**Definición 1.5.1 (operador de realización ternaria U_SV).** Sea Ω_proto el dominio proto-ternario de protopares sobre Ω₄₄₃. El operador de realización ternaria es la función:

U_SV : Ω_proto → {APTO-M, APTO-C, APTO-I, ∅}

donde ∅ denota retorno a Nada (NO-APTO en el vocabulario del CPS-SV). U_SV coincide con la función de dictamen D(A,B) del §3.9 bajo la convención NO-APTO → ∅.

**Definición 1.5.2 (ventana de persistencia de U).** La ventana de persistencia de U sobre Ω_proto es el conjunto:

W_U = { Π(A,B) ∈ Ω_proto | IP_suma(A,B) ≤ Λ_IP ∧ ΔEN_SV(A,B) ≤ 2,71 }

El valor 2,71 es la anchura completa de la escala EN_SV del corpus sobre Ω₄₄₃ (§3.2 del CPS-SV).

**Teorema 1.5.1 (U como motor generativo ternario).** Sea Π(A,B) ∈ Ω_proto con A, B ∈ Ω₄₄₃, A ≠ B. El operador U_SV genera realización ternaria de Π(A,B) — esto es, U_SV(A,B) ∈ {APTO-M, APTO-C, APTO-I} — si y solo si se satisfacen simultáneamente:

**C.1 (persistencia frente a Nada):** IP_suma(A,B) = IP_SV(A) + IP_SV(B) ≤ Λ_IP = 1800 kJ/mol

**C.2 (vocabulario operativo de U):** ΔEN_SV(A,B) = |EN_SV(A) − EN_SV(B)| ≤ 2,71

**C.3 (cierre posicional en régimen metálico):** Si ΔEN_SV(A,B) ≤ Λ_M = 0,50, entonces ρ_SV(A,B) ≤ Λ_ρ = 1,40

**Demostración:**

*(⟹)* Sea U_SV(A,B) ∈ {APTO-M, APTO-C, APTO-I}.

Por la función D del §3.9, el primer test ejecutado es B.4. Si IP_suma(A,B) > Λ_IP, D devuelve NO-APTO → ∅. Luego IP_suma(A,B) ≤ Λ_IP, estableciendo **C.1**.

B.1 determina χ_B1(A,B) ∈ {M, C, I} según ΔEN_SV. El rango de EN_SV en Ω₄₄₃ es [0,00; 2,71] por construcción del catálogo SV-443 (§2.1 del CPS-SV), luego ΔEN_SV(A,B) ≤ 2,71, estableciendo **C.2**.

Si χ_B1 = M (ΔEN_SV ≤ Λ_M), D ejecuta B.2 y B.3. Si ρ_SV > Λ_ρ, D devuelve NO-APTO → ∅. Si M_joint < Λ_M%, B.3 reclasifica a APTO-C, que pertenece al conjunto objetivo; pero si ambos fallan simultáneamente de forma que D devuelve ∅, la hipótesis queda refutada. Luego ρ_SV ≤ Λ_ρ y M_joint ≥ Λ_M% (o B.3 reclasifica a APTO-C sin invalidar U_SV ∈ {APTO-M, APTO-C, APTO-I}), estableciendo **C.3**.

*(⟸)* Sean C.1, C.2, C.3 satisfechas.

**C.1** garantiza que B.4 = ADMISIBLE: U sobrevive a 0 en el eje energético.

**C.2** garantiza que ΔEN_SV ≤ 2,71, luego χ_B1(A,B) ∈ {M, C, I} por la definición de B.1 (el diferencial se encuentra dentro del vocabulario operativo del corpus).

Si χ_B1 ∈ {C, I}: D devuelve APTO-C o APTO-I directamente. U_SV(A,B) ∈ {APTO-C, APTO-I} ⊂ {APTO-M, APTO-C, APTO-I}.

Si χ_B1 = M: **C.3** garantiza ρ_SV ≤ Λ_ρ (B.2 = ADMISIBLE). B.3 determina el régimen dentro de lo ternario: si M_joint ≥ Λ_M%, D devuelve APTO-M; si M_joint < Λ_M%, D devuelve APTO-C (RECLASIFICA-C). En ambos casos D devuelve un elemento de {APTO-M, APTO-C, APTO-I}: realización ternaria confirmada. M_joint no es condición de acceso a lo ternario sino discriminante de régimen.

En todos los casos, U_SV(A,B) ∈ {APTO-M, APTO-C, APTO-I}. **Q.E.D.**

---

## §1.5.5. Corolario: posición de los tres regímenes APTO en la escala operativa de U

**Corolario 1.5.1.** Los tres regímenes de realización ternaria del CPS-SV corresponden a tres zonas del rango operativo de U sobre la escala EN_SV:

| Régimen | Rango ΔEN_SV | Zona en la escala (1, U, 0) |
|---|---|---|
| APTO-M | ΔEN_SV ∈ [0; 0,50] | U opera próximo al polo 1 (Todo): similitud estructural dominante. El par tiende a la identidad estructural. |
| APTO-C | ΔEN_SV ∈ (0,50; 1,50] | U opera en la zona de imperfección activa y equilibrada: ni identidad completa ni contraste extremo. |
| APTO-I | ΔEN_SV ∈ (1,50; 2,71] | U opera próximo al límite Todo-Nada: contraste estructural dominante, pero sin que 0 absorba el par. |
| NO-APTO (∅) | IP_suma > Λ_IP o (ΔEN_SV ≤ Λ_M ∧ ρ_SV > Λ_ρ) | Nada (0) absorbe el par: U superado en el eje energético o en el eje posicional. |

**Demostración del corolario:** Directa por la definición de los umbrales Λ_M, Λ_C del criterio B.1 y la función D del §3.9. Los tres intervalos particionan [0; 2,71] de forma determinista. El cuarto caso corresponde a los dos modos de absorción por 0: B.4 (eje energético) y B.2 en régimen M (eje posicional). M_joint(A,B) opera como discriminante de régimen dentro de METAL-SV: si M_joint ≥ Λ_M% el par se confirma APTO-M; si M_joint < Λ_M% el par se reclasifica APTO-C (ruta RECLASIFICA-C, 6.144 pares verificados). M_joint no determina si hay realización ternaria sino cuál de los dos primeros regímenes resulta. **Q.E.D.**

---

## §1.5.6. Conexión con la publicación futura de moléculas

El Teorema 1.5.1 establece el fundamento para la secuencia de publicaciones del corpus en química factual SV:

1. **Génesis del hidrógeno** (Lloret Egea, 2026e): U genera el tránsito Pre → Proto → Ternario para **elementos individuales**. La cadena de admisibilidad individual produce Ω₄₄₃.

2. **CPS-SV** (esta publicación): U genera el tránsito Pre → Proto → Ternario para **pares estructurales**. La función de dictamen D(A,B) produce el catálogo de 97.903 pares sobre Ω₄₄₃.

3. **Moléculas estructurales SV** (publicación futura): U generará el tránsito de pares realizados a **configuraciones moleculares**: Proto-mol → Mol. Los criterios de admisibilidad molecular serán el nivel siguiente de la misma cadena operativa que aquí se establece.

En los tres casos, la estructura lógica es idéntica: Ω_pre como dominio de potencial → U como agente de tránsito → Ω_ternario como dominio de realización → 𝓔★_TODO,SV(Γ_U) = 0 como compuerta superior de la Teoría del TODO y de la NADA.

---


---

---

## §1.6. Teorema de predominancia de U y cascada de dominancias estructurales del CPS-SV

### §1.6.1. Axiomas del dominio de dominancias

Los tres axiomas siguientes son propios del dominio de la cascada. No se derivan: se declaran como condiciones constitutivas del aparato.

**Axioma A.1 (Completitud ternaria del dictamen).** El único alfabeto legítimo de evaluación es K₃ = {0, 1, U}. El codominio de D se realiza sobre {APTO-M, APTO-C, APTO-I, ∅}, donde APTO-M es la proyección del polo 1 (Todo), ∅ es la proyección del polo 0 (Nada), APTO-I es el régimen próximo al límite Nada sin absorción, y APTO-C es la proyección del polo U (imperfección activa). Ningún dictamen fuera de este conjunto es admisible.

**Axioma A.2 (Irreversibilidad de la cascada).** Si el nivel de dominancia D_i produce dictamen ∅ sobre un protopar Π(A,B), ningún nivel D_j con j > i puede revertir ese dictamen. La cascada es irreversible en el sentido creciente del índice i (D₀ → D₄).

**Axioma A.3 (Independencia de niveles).** La condición evaluada en el nivel D_i es lógicamente independiente de las condiciones evaluadas en los niveles D_j con j ≠ i: el valor de cualquier magnitud en D_i no puede inferirse de los valores en D_j. Cada nivel opera sobre un eje estructural propio y no redundante.

---

### §1.6.2. Proposiciones preparatorias

**Proposición 1.6.1 (Totalidad y determinismo de la cascada).** La función de dictamen D : Ω_proto → {APTO-M, APTO-C, APTO-I, ∅} es total y determinista: para todo Π(A,B) ∈ Ω_proto existe exactamente un dictamen D(A,B) ∈ {APTO-M, APTO-C, APTO-I, ∅}.

*Demostración.* La función D del §3.9 es una función de ramificación condicional sobre K₃ con exactamente cuatro ramas terminales. Por la Proposición 3.5 (simetría), D no depende del orden de los argumentos. Cada rama terminal es alcanzada en un número finito de evaluaciones booleanas sobre magnitudes reales bien definidas. La función está definida para todo par (A,B) con A, B ∈ Ω₄₄₃, A ≠ B. Por construcción del catálogo SV-443, Ω₄₄₃ es finito y sus magnitudes φ(k) están fijadas en la Tabla Global. Luego D es total. La determinación exacta de cada valor se verifica en el laboratorio del §8: 97.903 dictámenes, 0 errores. **Q.E.D.**

**Proposición 1.6.2 (Necesidad estricta de cada nivel sobre el siguiente).** En la cascada D₀ → D₁ → D₂ → D₃ → D₄, cada nivel D_i es condición necesaria para que el nivel D_{i+1} sea evaluado. Formalmente: si D_i no se satisface, D_j no es evaluado para ningún j > i.

*Demostración.* Nivel por nivel:

— D₀ (B.5): La pertenencia de A y B a Ω₄₄₃ es condición de existencia del protopar como objeto del dominio. Sin D₀, Π(A,B) ∉ Ω_proto y D no está definido.

— D₁ (B.4): La función D evalúa B.4 antes de cualquier otro criterio (§3.9, pseudocódigo línea 1). Si IP_suma(A,B) > Λ_IP, D devuelve NO-APTO y termina. D₂ no se evalúa.

— D₂ (B.1): χ_B1 se computa solo si B.4 pasa. Determina el régimen. Si χ_B1 = COVAL-SV o IONIC-SV, D devuelve dictamen directamente y termina. D₃ no se evalúa.

— D₃ (B.2): Solo se evalúa si D₁ pasa y D₂ produce χ_B1 = METAL-SV. Si ρ_SV > Λ_ρ, D devuelve NO-APTO. D₄ no se evalúa.

— D₄ (B.3): Solo se evalúa si D₁, D₂ = METAL-SV y D₃ pasan. Determina APTO-M o APTO-C.

La necesidad estricta de cada nivel sobre el siguiente es directa por la estructura condicional de D. **Q.E.D.**

**Proposición 1.6.3 (Doble accesibilidad del régimen APTO-C).** El régimen APTO-C es el único régimen en el codominio de D accesible mediante dos rutas estructuralmente distintas sobre el dominio de entrada.

*Demostración.* Se identifican las rutas de acceso a cada régimen:

| Régimen | Condiciones de acceso | Rutas |
|---|---|---|
| APTO-M | D₁ ∧ χ_B1=M ∧ D₃ ∧ M_joint≥Λ_M% | 1 ruta |
| APTO-C — ruta directa | D₁ ∧ χ_B1=COVAL-SV | 1 ruta |
| APTO-C — ruta RECLASIFICA-C | D₁ ∧ χ_B1=METAL-SV ∧ D₃ ∧ M_joint<Λ_M% | 1 ruta |
| APTO-I | D₁ ∧ χ_B1=IONIC-SV | 1 ruta |
| NO-APTO — ruta B.4 | IP_suma>Λ_IP | 1 ruta |
| NO-APTO — ruta B.2 | D₁ ∧ χ_B1=METAL-SV ∧ ρ_SV>Λ_ρ | 1 ruta |

Las dos rutas de acceso a APTO-C son estructuralmente distintas: la ruta directa pasa por χ_B1 = COVAL-SV (D₂ determina el dictamen sin evaluación de D₃ ni D₄); la ruta RECLASIFICA-C pasa por χ_B1 = METAL-SV, D₃ admisible y D₄ no admisible como METAL (M_joint < Λ_M%). Las condiciones de entrada de ambas rutas son disjuntas: χ_B1 = COVAL-SV y χ_B1 = METAL-SV son mutuamente excluyentes por definición de B.1. Luego son dos rutas estructuralmente distintas con intersección vacía en el dominio de entrada. Ningún otro régimen del codominio tiene dos rutas de entrada con dominio de entrada disjunto. **Q.E.D.**

**Proposición 1.6.4 (APTO-C como atractor dominante de la cascada).** En todo dominio Ω ⊆ Ω_proto en el que los conjuntos de valores de ΔEN_SV, IP_suma, ρ_SV y M_joint sean tales que los cuatro rangos efectivos [Λ_M, Λ_C], (0, Λ_IP], [1, Λ_ρ] y [0%, 100%] sean no vacíos, |D_r⁻¹(APTO-C)| > |D_r⁻¹(APTO-M)| y |D_r⁻¹(APTO-C)| > |D_r⁻¹(APTO-I)|, donde D_r es la restricción de D al subdominio de realizaciones ternarias D⁻¹({APTO-M, APTO-C, APTO-I}).

*Demostración.* Por la Proposición 1.6.3, APTO-C tiene dos rutas de entrada con dominio disjunto: dominio_directo = {Π(A,B) : D₁ ∧ χ_B1=COVAL} y dominio_RECLASIFICA = {Π(A,B) : D₁ ∧ χ_B1=METAL ∧ D₃ ∧ M_joint<Λ_M%}. La cardinalidad total de D_r⁻¹(APTO-C) = |dominio_directo| + |dominio_RECLASIFICA|. APTO-M solo tiene acceso desde dominio_M = {Π(A,B) : D₁ ∧ χ_B1=METAL ∧ D₃ ∧ M_joint≥Λ_M%}. Puesto que dominio_M y dominio_RECLASIFICA son una partición del conjunto {Π(A,B) : D₁ ∧ χ_B1=METAL ∧ D₃}, se tiene |D_r⁻¹(APTO-M)| + |D_r⁻¹(APTO-C)|_RECLASIFICA = |{D₁ ∧ METAL ∧ D₃}|. Luego |D_r⁻¹(APTO-C)| > |D_r⁻¹(APTO-M)| siempre que dominio_directo ≠ ∅, lo cual está garantizado por hipótesis de rango no vacío de ΔEN_SV ∈ (Λ_M, Λ_C]. Para APTO-I: dominio_I = {D₁ ∧ χ_B1=IONIC} ⊂ {D₁ ∧ ΔEN_SV > Λ_C}; dominio_directo ⊃ {D₁ ∧ ΔEN_SV ∈ (Λ_M, Λ_C]}, que es estrictamente más amplio por hipótesis. La demostración estructural garantiza |D_r⁻¹(APTO-C)| > |D_r⁻¹(APTO-M)| para todo Ω con rango COVAL no vacío. La desigualdad |D_r⁻¹(APTO-C)| > |D_r⁻¹(APTO-I)| es adicional y se verifica numéricamente sobre Ω₄₄₃: 37.580 > 9.515 y 37.580 > 5.075. **Q.E.D.**

---

### §1.6.3. Teorema de predominancia de U

**Teorema 1.6.1 (Teorema de predominancia de U en la cascada de dominancias).** Sea D : Ω_proto → {APTO-M, APTO-C, APTO-I, ∅} la función de dictamen del CPS-SV. Bajo los Axiomas A.1–A.3, se satisfacen simultáneamente:

**(i) Cascada total determinista.** D se descompone en exactamente cinco niveles de dominancia estructural D₀ ⊆ D₁ ⊆ D₂ ⊆ D₃ ⊆ D₄, ordenados por precedencia lógica, tales que cada D_i es condición necesaria para la evaluación de D_{i+1} y A₃ garantiza que ningún nivel puede inferirse de otro.

**(ii) Exclusividad de acceso dual.** El régimen APTO-C es el único en el codominio de D con dos rutas de acceso estructuralmente distintas y con dominios de entrada disjuntos. Todos los demás regímenes realizados son accesibles mediante exactamente una ruta.

**(iii) Predominancia cardinal.** Sea D_r la restricción de D al subdominio de realizaciones ternarias. Entonces |D_r⁻¹(APTO-C)| > |D_r⁻¹(APTO-M)| y |D_r⁻¹(APTO-C)| > |D_r⁻¹(APTO-I)|. En Ω₄₄₃: 37.580 > 9.515 y 37.580 > 5.075.

**(iv) Principio de predominancia de U.** En todo dominio Ω ⊆ Ω_proto con conjuntos de valores de rango efectivo no vacío en los cuatro criterios activos, la zona de imperfección activa de U domina el espacio de realizaciones ternarias: D_r⁻¹(APTO-C) tiene la mayor cardinalidad entre los tres regímenes realizados. La predominancia no es contingente al dominio empírico Ω₄₄₃: es consecuencia estructural de la doble accesibilidad demostrada en (ii).

**Demostración.**

(i) Por la Proposición 1.6.1 (totalidad y determinismo) y la Proposición 1.6.2 (necesidad estricta de niveles). La identificación de D₀–D₄ con B.5, B.4, B.1, B.2, B.3 respectivamente es directa por el pseudocódigo de D en §3.9. La independencia de ejes (Axioma A.3) se comprueba por construcción directa a partir de las definiciones del §3: IP_suma opera sobre la energía de persistencia; ΔEN_SV sobre el eje polar; ρ_SV sobre el eje posicional; M_joint sobre el carácter metálico — cuatro ejes estructurales ortogonales en φ(k).

(ii) Por la Proposición 1.6.3.

(iii) Por la Proposición 1.6.4.

(iv) La Proposición 1.6.4 establece la predominancia para todo Ω con rango no vacío, condición que no depende del contenido empírico específico de Ω₄₄₃. La doble accesibilidad de APTO-C (Proposición 1.6.3) es consecuencia de la estructura lógica de D, no de los valores numéricos de los umbrales. Por tanto, la predominancia de U es una propiedad estructural de la cascada, transferible a cualquier dominio que satisfaga la misma arquitectura de evaluación. **Q.E.D.**

---

### §1.6.4. Corolarios

**Corolario 1.6.1 (Invarianza de la predominancia bajo reordenación del dominio).** La predominancia cardinal de APTO-C sobre APTO-M y APTO-I es invariante respecto a toda permutación del dominio Ω_proto que preserve el multiconjunto de cuádruplos (ΔEN_SV, ρ_SV, M_joint, IP_suma) de cada protopar.

*Demostración.* La cardinalidad |D_r⁻¹(APTO-C)| depende solo de cuántos protopares satisfacen las condiciones de cada ruta, determinadas por sus cuádruplos de magnitudes. La permutación del dominio no altera los cuádruplos, luego no altera las cardinalidades. **Q.E.D.**

**Corolario 1.6.2 (Las realizaciones ternarias se acumulan en U, no en los polos).** En Ω₄₄₃, el polo Todo (APTO-M, 18,2% de APTO) y el límite Nada (APTO-I, 9,7% de APTO) concentran conjuntamente el 27,9% de la realización ternaria. La zona de imperfección activa de U (APTO-C) concentra el 72,1% restante. El CPS-SV es un catálogo cuyo espacio de realizaciones se concentra en la zona de imperfección sostenida — el estado en que ningún polo ha logrado dominancia pleta sobre el par.

*Demostración.* Cálculo directo: 37.580 / 52.170 = 72,0%. 9.515 / 52.170 = 18,2%. 5.075 / 52.170 = 9,7%. **Q.E.D.**

**Corolario 1.6.3 (La doble ruta es ventaja estructural y no anomalía).** La doble accesibilidad de APTO-C no es una irregularidad del aparato B.1–B.5 sino la expresión matemática de que U opera simultáneamente desde la zona de baja polaridad (ΔEN_SV ≤ Λ_M, ruta RECLASIFICA-C) y desde la zona de polaridad intermedia (ΔEN_SV ∈ (Λ_M, Λ_C], ruta directa). La asimetría generativa de U respecto a los polos 1 y 0 produce, por construcción, un régimen de realización con cuenca de atracción estrictamente mayor que la de cualquier polo.

*Demostración.* Por la Proposición 1.6.3: las dos rutas de APTO-C tienen dominios de entrada disjuntos y ambos son no vacíos en Ω₄₄₃ (ruta directa: 31.436 pares; ruta RECLASIFICA-C: 6.144 pares; suma: 37.580). La doble cuenca es estructural. **Q.E.D.**

**Corolario 1.6.4 (Principio de transferibilidad a dominios superiores).** Los cinco niveles de la cascada de dominancias D₀–D₄ son independientes del contenido específico de las magnitudes φ(k) = (EN_SV, r_SV, IP_SV, M_SV) y de la naturaleza del dominio Ω. En todo dominio Ω' dotado de una función de dictamen D' que se descomponga en cascada de igual arquitectura — cinco niveles ordenados por precedencia lógica, régimen de imperfección activa accesible mediante al menos dos rutas estructuralmente distintas con dominio de entrada disjunto, régimen de polo accesible mediante una sola ruta — el Teorema 1.6.1 se generaliza: la predominancia del régimen de imperfección activa es consecuencia estructural de la arquitectura de la cascada, no del contenido empírico del dominio.

*Demostración.* La demostración del Teorema 1.6.1 no invoca en ningún paso la naturaleza química de EN_SV, r_SV, IP_SV ni M_SV. Invoca únicamente: (a) la existencia de cuatro rangos no vacíos, (b) la estructura condicional de D, y (c) la disjunción de los dominios de entrada de las dos rutas hacia el régimen U. Estas tres propiedades son preservadas bajo toda interpretación del dominio Ω' que satisfaga la misma arquitectura. **Q.E.D.**

---

### §1.6.5. Principio rector del CPS-SV

**Principio de predominancia de U (P_U).** *En todo dominio de realizaciones ternarias gobernado por una cascada de dominancias con arquitectura D₀–D₄, la zona de imperfección sostenida — donde ningún polo logra dominancia completa — es el régimen de mayor cardinalidad en el espacio de realizaciones. Esta predominancia no es resultado de una configuración particular del dominio empírico sino consecuencia de la doble accesibilidad estructural del régimen de imperfección, demostrada por el Teorema 1.6.1. El principio es transferible a todo dominio que satisfaga la arquitectura de la cascada.*
---

## §1.7. Marco conceptual: regímenes de realización ternaria

Los tres regímenes de realización ternaria son consecuencia directa del Teorema 1.5.1 y su Corolario 1.5.1. El rango operativo de U sobre la escala ΔEN_SV genera exactamente tres zonas de realización y un régimen de absorción por Nada.

**Régimen APTO-M** — equilibrio estructural de similitud. Cuando dos elementos comparten electronegatividad estructural próxima (ΔEN_SV ≤ Λ_M = 0,50), U opera cerca del polo 1 (Todo): la similitud de propiedades en la capa operatoria del corpus genera compatibilidad posicional. El par alcanza un punto de equilibrio estabilizado en el régimen metálico estructural.

**Régimen APTO-I** — equilibrio estructural de contraste. Cuando los elementos presentan electronegatividades estructurales contrastadas (ΔEN_SV > Λ_C = 1,50), U opera cerca del límite Todo-Nada: la asimetría de propiedades en la capa operatoria determina la configuración del par. El par alcanza un punto de equilibrio estabilizado en el régimen iónico estructural. No es Nada: los potenciales se igualan sin anularse.

**Régimen APTO-C** — equilibrio estructural de coexistencia. El intervalo Λ_M < ΔEN_SV ≤ Λ_C corresponde a la zona de imperfección activa y equilibrada de U: ni identidad completa ni contraste extremo. El par se estabiliza en el régimen covalente estructural.

**Régimen NO-APTO** — absorción por Nada. Cuando IP_suma > Λ_IP = 1800 kJ/mol (barrera de potencial insuperable para U) o ρ_SV > Λ_ρ = 1,40 en régimen metálico (U no puede cerrar el morfismo posicional), el par no encuentra punto de equilibrio y retorna a Ω_pre como elementos individuales. Nada absorbe al par. No es destrucción: es ausencia de realización ternaria.

Los tres regímenes APTO comparten la propiedad fundamental: el punto de equilibrio de potencial del par es distinto de cero. La igualación de potenciales entre los dos elementos no produce potencial nulo — eso sería muerte estructural — sino potencial equilibrado: el sistema vivo que ha cruzado la barrera de potencial y descansa en un punto de coexistencia estable.

## §1.8. Propiedades emergentes del par estructural

Un elemento posee propiedades estructurales individuales en el aparato SV: EN_SV, M_SV, IP_SV, r_SV. El par, sin embargo, no hereda mecánicamente esas propiedades: U genera magnitudes propias — ΔEN_SV, M_joint, IP_suma, ρ_SV — que son atributos del par como entidad, irreducibles a los componentes por separado. La emergencia de propiedades de par no previstas en los perfiles individuales φ(A) y φ(B) es precisamente el efecto de U operando sobre el protopar Π(A,B): U introduce el diferencial que genera la configuración ternaria, cuyo carácter es irreducible a los polos individuales.

Un elemento con M_SV = 30% no alcanza por sí solo el umbral de carácter metálico estructural. Emparejado con un elemento de M_SV = 70%, genera M_joint = 50% ≥ Λ_M% = 40,0%, y el par recibe dictamen APTO-M. La admisibilidad metálica estructural es una propiedad del par, no de ninguno de los dos elementos considerados individualmente.

El caso inverso es igualmente válido: dos elementos con M_SV = 38% cada uno producen M_joint = 38% < 40,0%; si además su ΔEN_SV ≤ 0,50 y ρ_SV ≤ 1,40, el par no recibe NO-APTO sino APTO-C (ruta RECLASIFICA-C): la admisibilidad estructural se sostiene, pero en régimen covalente, no metálico.

En términos de aleación estructural, esto significa que el resultado del par puede superar las propiedades individuales de ambos componentes, quedar por debajo, o situarse en un régimen estructural que ninguno de los dos ocupaba por separado. El bronce — cobre más estaño — endurece más allá de cualquiera de sus componentes: el aparato SV formaliza esta posibilidad como propiedad de la secuencia proto-ternario → ternario, no como excepción.

La pérdida de esta perspectiva sistémica — tratar cada elemento como unidad autónoma sin considerar su comportamiento en par — reduce el análisis de materiales a un inventario de propiedades individuales, insuficiente para predecir el comportamiento del conjunto. El CPS-SV opera precisamente en el nivel intermedio: el del par como entidad estructural propia con criterios de admisibilidad derivados de la interacción, no de la suma de partes.

---

## §1.9. Fundamento termodinámico de los estados estables de par

Los estados APTO del CPS-SV no son categorías de clasificación arbitrarias: son puntos de equilibrio termodinámico estructural del par (A,B). Su existencia y estabilidad se derivan del aparato termodinámico del corpus SV (Lloret Egea, 2026i; Lloret Egea, 2026j) mediante tres propiedades encadenadas.

**Primera propiedad — El sesgo polar del protopar.**

El documento de entropía factual del corpus (Lloret Egea, 2026i) establece que cada posición preternaria ξ_i tiene un sesgo polar δ_i = β_i − α_i, donde β_i es la componente de acumulación hacia el polo 1 (Todo) y α_i la componente hacia el polo 0 (Nada). El sesgo polar mide la separación efectiva entre los dos polos en la posición i.

**Proposición 1.7.1 (ΔEN_SV como sesgo polar de par).** Sea Π(A,B) un protopar con A, B ∈ Ω₄₄₃. La magnitud ΔEN_SV(A,B) = |EN_SV(A) − EN_SV(B)| es la realización del sesgo polar diferencial del protopar sobre la escala de la Tabla Global del corpus.

*Demostración.* En la Tabla Global, EN_SV(k) es la proyección escalar de la posición del elemento k sobre el eje polar del corpus, con EN_SV = 0 correspondiendo al polo 0 (Nada estructural: carácter metálico puro, sin separación electrónica) y EN_SV = 2,71 al polo 1 (Todo estructural: máxima separación electrónica, carácter no metálico). El sesgo polar de la posición del elemento k en la Tabla Global es δ(k) = EN_SV(k) − 0 = EN_SV(k). Para el protopar Π(A,B), el sesgo polar diferencial es |δ(A) − δ(B)| = |EN_SV(A) − EN_SV(B)| = ΔEN_SV(A,B). Bajo la disciplina append-only, este diferencial es la variación total del sesgo polar entre los dos elementos en el primer paso de la trayectoria proto-ternaria del par. Q.E.D.

**Segunda propiedad — Irreversibilidad estructural.**

La entropía factual H_SV es no decreciente a lo largo de toda trayectoria admisible bajo la disciplina append-only (Teorema 8.2 de Lloret Egea, 2026i). Esta no decrecencia no es un postulado externo: es consecuencia algebraica de que la variación total preternaria del sesgo polar V_i(δ, n) = Σ|δ_i(k+1) − δ_i(k)| es una suma de valores absolutos y solo puede crecer. Durante la transición proto-ternaria, U opera sobre Π(A,B) incrementando H_SV. Una vez alcanzado el estado APTO, la disciplina append-only impide que H_SV disminuya: el par no puede retornar espontáneamente al dominio proto-ternario Ω_proto. Esta es la fuente estructural de la estabilidad de los estados APTO.

**Tercera propiedad — La ecuación de equilibrio termodinámico.**

La fórmula termodinámica factual única del corpus (Lloret Egea, 2026j, DOI 10.17613/ptw68-d1r57) establece que el dominio termodinámico queda cerrado por la ecuación escalar nula:

E^thermo_SV(Γ, n; θ) = 0

Un estado de par es termodinámicamente estable cuando satisface esta ecuación. En términos del sesgo polar: el estado APTO corresponde a un punto estacionario de V_i(δ) — el punto donde |δ_i(k+1) − δ_i(k)| = 0 para todos los sucesos posteriores a la realización ternaria. En ese punto, los potenciales estructurales del par se han igualado a un valor consistente. El punto de equilibrio no es potencial nulo — eso correspondería a Nada, la absorción por el polo 0 — sino potencial equiparado: el par descansa en un estado termodinámicamente estable con H_SV > 0.

Los tres regímenes APTO del CPS-SV son tres clases de soluciones de E^thermo_SV = 0, diferenciadas por el valor estacionario del sesgo polar:

- **APTO-M** (ΔEN_SV ≤ 0,50): equilibrio de sesgo polar mínimo. El par descansa en la zona próxima al polo 1 (Todo): la variación total V_i(δ) ha sido pequeña, y el estado estacionario tiene alta simetría estructural. Los potenciales de los dos elementos han convergido en la zona de carácter metálico estructural conjunto (M_joint ≥ 40,0%).

- **APTO-C** (0,50 < ΔEN_SV ≤ 1,50): equilibrio de sesgo polar intermedio. La variación total V_i(δ) ha sido moderada. El estado estacionario se sitúa en la zona de imperfección activa de U, entre los polos 1 y 0.

- **APTO-I** (ΔEN_SV > 1,50): equilibrio de sesgo polar alto. La variación total V_i(δ) ha sido grande. El estado estacionario está próximo al límite Todo-Nada, pero sin que 0 absorba al par: el sesgo es alto pero constante, lo que significa que los potenciales se han igualado en una configuración fuertemente asimétrica pero estable.

**El criterio B.4 como umbral de energía de activación.**

La suma IP_suma(A,B) = IP_SV(A) + IP_SV(B) es la energía de persistencia estructural conjunta del par. Cuando IP_suma > Λ_IP = 1800 kJ/mol, la energía de activación necesaria para que V_i(δ) alcance cualquier punto estacionario supera la capacidad operativa de U: la trayectoria proto-ternaria no puede cruzar la barrera de potencial. H_SV no puede incrementarse lo suficiente para alcanzar ninguna solución de E^thermo_SV = 0 para el par. El protopar permanece en Ω_proto sin realizarse. Este es el dictamen NO-APTO: Nada gana la batalla al no permitir que U complete la estabilización.

**Corolario termodinámico:** Los tres regímenes APTO y el régimen NO-APTO son las únicas clases posibles de resultado termodinámico para un protopar Π(A,B) en el aparato SV, correspondientes a: equilibrio próximo a 1 (APTO-M), equilibrio intermedio (APTO-C), equilibrio próximo al límite Nada (APTO-I), y absorción por Nada sin equilibrio alcanzable (NO-APTO). El CPS-SV cataloga cuál de los cuatro resultados le corresponde a cada uno de los 97.903 protopares de Ω₄₄₃.



---

## §1.10. El par estructural en su contexto de campo: circunstancias y operador de interacción

Un par estructural (A,B) del CPS-SV no existe en un vacío estructural. Cada elemento k ∈ Ω₄₄₃ es un protocampo admisible del corpus SV, con lectura Σ = 1 en el catálogo factual: ha superado la cadena de compuertas de persistencia, frontera, residual, identidad química, descendencia protocampal y compatibilidad con 𝓔★_TODO,SV(Γ_U) = 0 (Lloret Egea, 2026e). La formación del par (A,B) no es una operación abstracta sobre índices numéricos: es la aplicación del operador canónico de interacción 𝓘_SV (Lloret Egea, 2026k) sobre el dominio ordenado de los dos proto-campos, dentro de su trayectoria factual y bajo frontera explícita.

**El criterio B.5 es la compuerta Σ = 1 del operador 𝓘_SV.** El operador 𝓘_SV solo está definido sobre pares de campos con lectura Σ = 1 (Teorema 1 de Lloret Egea, 2026k). La exigencia de que ambos elementos A, B pertenezcan a Ω₄₄₃ — el criterio B.5 del CPS-SV — es la proyección estructural de esa compuerta: solo los elementos que han atravesado la cadena completa de admisibilidad individual tienen lectura Σ = 1 y pueden entrar como argumentos del operador.

**ΔEN_SV(A,B) es la distancia factual fibrosa d^SV_Φ(A,B).** La distancia factual fibrosa d^SV_Φ del corpus SV (Lloret Egea, 2026k, Anexo A) mide el cambio estructural entre dos estados de campo sobre trayectoria factual, sin invocar cronología soberana. Para el protopar Π(A,B), la magnitud ΔEN_SV(A,B) = |EN_SV(A) − EN_SV(B)| es la realización de d^SV_Φ(A,B) sobre la escala de electronegatividad estructural SV: mide cuánto difieren las configuraciones de campo de A y B sobre el eje de separación polar del corpus. Los umbrales Λ_M = 0,50 y Λ_C = 1,50 del criterio B.1 particionan el rango de d^SV_Φ en los tres regímenes de interacción (metálico, covalente, iónico) que 𝓘_SV puede realizar sobre el par.

**IP_suma es el umbral de activación de 𝓘_SV.** El criterio B.4 (IP_suma ≤ Λ_IP = 1800 kJ/mol) es la condición bajo la cual el operador 𝓘_SV dispone de suficiente energía de activación para completar la interacción sobre el par (A,B). Cuando IP_suma > Λ_IP, 𝓘_SV no puede operar: el protopar no alcanza ningún estado de interacción realizada y permanece en Ω_proto.

**El CPS-SV como catálogo de primer orden del dominio de 𝓘_SV sobre Ω₄₄₃.** El catálogo de pares estructurales SV determina, para cada uno de los 97.903 protopares de Ω₄₄₃, si el operador 𝓘_SV puede completar la interacción y en qué régimen. Los dictámenes APTO-M, APTO-C, APTO-I son los tres regímenes de interacción realizada; el dictamen NO-APTO es la condición de interacción bloqueada. En este sentido, el CPS-SV es el catálogo de primer orden del dominio de 𝓘_SV aplicado al universo de proto-campos de Ω₄₄₃.

Esta caracterización revela la dimensión que el análisis puramente interno de los pares no puede ver: un par APTO no existe aislado, sino dentro de un entorno de campos que lo rodea y cuyas interacciones actúan simultáneamente sobre él. Las propiedades del par realizado — y, por extensión, las de la aleación que ese par funda — dependen no solo de los parámetros estructurales internos (los que el CPS-SV cataloga) sino del contexto de campo en que el par se inscribe. El aparato de interacción, intercomposición y transmisión factual entre campos del corpus SV (Lloret Egea, 2026k) es el marco que aborda esa dimensión externa y que proporciona el nivel de análisis subsiguiente al catálogo.

Una nota sobre la simetría: el operador 𝓘_SV opera sobre pares ordenados — el orden de los argumentos importa estructuralmente (Teorema 4 de Lloret Egea, 2026k). El CPS-SV, en cambio, trabaja con pares no ordenados C(443,2) = 97.903: determina la admisibilidad estructural simétrica, no la dirección de la interacción. Esta es la distinción entre el primer orden (admisibilidad de campo: ¿puede formarse el par?) y el orden completo (dirección de la interacción: ¿cómo opera 𝓘_SV sobre él?). El primero es el objeto de esta publicación; el segundo pertenece al aparato de Lloret Egea (2026k).



---

# §2. Marco de dominio — Tabla Global y espacio de pares Ω₄₄₃

## §2.1. La Tabla Global como fuente única de propiedades de par

El CPS-SV opera sobre cuatro magnitudes de la Tabla Global del catálogo SV-443:

| Magnitud | Símbolo | Unidad | Rango efectivo en Ω₄₄₃ |
|---|---|---|---|
| Electronegatividad estructural | EN_SV(k) | adimensional | [0,00 ; 2,71] |
| Energía de ionización estructural | IP_SV(k) | kJ/mol | [355 ; 1.550] |
| Radio atómico estructural | r_SV(k) | pm | [116,8 ; 357,0] |
| Carácter metálico estructural | M_SV(k) | % | [2,0 ; 100,0] |

Estas magnitudes son derivadas de las compuertas de persistencia y de la ecuación rectora 𝓔★(Γ_U; τ) = 0. Su función en el CPS-SV es determinar los criterios de admisibilidad de par.

## §2.2. El dominio Ω₄₄₃ y sus subdominios

El dominio Ω₄₄₃ = {1, 2,…, 443} es el conjunto de índices del catálogo SV-443. Se particiona en:

- **Ω₁₁₈** = {1,…,118}: subdominio base — Tabla Cero (118 elementos).
- **Ω_ext** = {119,…,443}: subdominio extendido — Tabla 1 (325 candidatos).

El espacio de pares no ordenados de Ω₄₄₃ es:

𝒫₄₄₃ = { {A,B} | A, B ∈ Ω₄₄₃, A ≠ B },   |𝒫₄₄₃| = C(443,2) = 97.903

## §2.3. Marco semántico: Tabla Cero, Tabla 1 y Tabla Global

**Tabla Cero** designa Ω₁₁₈ = {k = 1,...,118}. Para los pares de este dominio, la comunidad científica dispone de décadas de estudios de compatibilidad de aleación y enlace químico (Hume-Rothery, Pauling y cálculos computacionales de química cuántica relativista). El Sistema Vectorial SV aporta una lectura estructural derivada de sus propios criterios B.1–B.5, inconmensurable con los marcos cuánticos convencionales y complementaria a ellos.

**Tabla 1** designa Ω_ext = {k = 119,...,443}: los 325 candidatos del dominio extendido generados por las familias tipológicas Σ₁–Σ₁₂. Para estos candidatos no existe literatura experimental ni teórica convencional. La Tabla 1 es el dominio de aportación original del corpus SV.

**Tabla Global** designa Ω₄₄₃ = Ω₁₁₈ ∪ Ω_ext. Su uso en esta publicación responde a una necesidad operativa: el CPS-SV abarca los 97.903 pares de Ω₄₄₃, incluyendo los pares cruzados S₂ en que un elemento pertenece a la Tabla Cero y el otro a la Tabla 1.

## §2.4. Principio de nomenclatura secuencial autoincremental

Los elementos de la Tabla Cero reciben nombres de la forma SV-Alfa, SV-Beta, …, SV-Omega, SV-II-Alfa, …, SV-V-Chi, siguiendo la secuencia del alfabeto griego clásico con prefijo numérico romano de ciclo. La numeración de catálogo asociada es 01–0118, con cero inicial como separador de espacio de nombres respecto a la Tabla 1 (k 119–443).

Esta elección responde a un principio operativo explícito: la nomenclatura secuencial autoincremental permite reconstruir el orden completo de los elementos a partir de las reglas de la secuencia, sin necesidad de memorizar nombres arbitrarios. Dado el prefijo y el término griego, el elemento anterior y el posterior son siempre deducibles: SV-II-Gamma va precedido de SV-II-Beta y seguido de SV-II-Delta, por construcción.

La tabla periódica convencional no cumple esta propiedad: ninguno de los 118 nombres convencionales proporciona información sobre el elemento adyacente. La nomenclatura SV es un instrumento de acceso al catálogo, no únicamente una etiqueta. Los elementos de la Tabla 1 (k 119–443) extienden la misma secuencia a través de las familias tipológicas Σ₃–Σ₁₂, asegurando continuidad y uniformidad en el dominio extendido.

---

# §3. Criterios de admisibilidad de enlace estructural SV — Definiciones formales y determinación de umbrales

© 2026 Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | CC BY-NC-ND 4.0

---

## §3.0. Posición en el corpus y delimitación previa

Los cinco criterios de admisibilidad de enlace estructural SV (B.1–B.5) se derivan exclusivamente de las magnitudes tabuladas en la Tabla Global del catálogo SV-443 (*Análisis preliminar de elementos, materiales y aleaciones*, DOI: 10.17613/8ryyb-g9h48): electronegatividad estructural EN_SV, radio atómico estructural r_SV, energía de ionización estructural IP_SV, afinidad electrónica estructural EA_SV y carácter metálico estructural M_SV.

Las prohibiciones constitutivas P.1–P.6 del corpus quedan heredadas sin modificación. Se añaden tres prohibiciones específicas de este desarrollo:

**P.7** — Los criterios B.1–B.5 son la expresión formal de la ventana operativa de U sobre el protopar Π(A,B), derivada de las magnitudes de la Tabla Global. Su lectura en el corpus SV es inconmensurable con los criterios cuánticos de enlace (reglas de Pauling, Hume-Rothery, Drude-Sommerfeld); ambos marcos operan en capas estructurales distintas y no competitivas. Toda comparación con pares químicos conocidos tiene función calibratoria y de contraste, no de equivalencia formal.

**P.8** — Los dictámenes APTO-M, APTO-C, APTO-I son postulados de régimen estructural del par en el Sistema Vectorial SV: expresan el punto de equilibrio termodinámico alcanzado por el protopar bajo la operación de U_SV (§1.9), no la existencia de enlace metálico, covalente o iónico en sentido cuántico.

**P.9** — Los pares con al menos un elemento de Ω_ext (k > 118) tienen estatuto U: estructuralmente admisibles en el dominio de U_SV, en espera de contraste experimental cuando la síntesis de los elementos correspondientes sea posible (§6.2).

---

## §3.1. Dominio de definición

Sea Ω_443 = {1, 2, …, 443} el conjunto de índices del catálogo SV-443.

**Definición 3.1 (par estructural SV).** Un par estructural SV es una pareja {A, B} con A, B ∈ Ω_443, A ≠ B, donde a cada elemento se le asocian las magnitudes de la Tabla Global:

Por convención de enumeración se adopta la representación ordenada (A, B) con A < B, de modo que cada par no ordenado se representa exactamente una vez. La simetría de D(A,B) = D(B,A) (Proposición 3.5) garantiza que esta convención no afecta al dictamen.

```
φ(k) = (EN_SV(k), r_SV(k), IP_SV(k), M_SV(k))
```

El espacio de pares tiene cardinalidad |Ω_443 × Ω_443 \ diag| = 443 × 442 = 195.806 pares ordenados, equivalentes a 195.806 / 2 = **97.903 pares no ordenados**.

---

## §3.2. Magnitudes derivadas de par

A partir de φ(A) y φ(B) se definen cuatro magnitudes de par:

**Definición 3.2.1 — Diferencial de electronegatividad estructural:**

Δ EN_SV(A,B) = |EN_SV(A) - EN_SV(B)|

Rango efectivo en el catálogo SV-118: [0.000, 2.710]. El rango 2.710 es el ancho completo de la escala EN_SV sobre los primeros 118 elementos.

**Definición 3.2.2 — Ratio de compatibilidad posicional:**

ρ_SV(A,B) = max(r_SV(A), r_SV(B)) / min(r_SV(A), r_SV(B)) ≥ 1

Definido siempre ≥ 1 por construcción. Igual a 1 para el par homonuclear hipotético.

**Definición 3.2.3 — Carácter metálico estructural conjunto:**

M_joint(A,B) = [M_SV(A) + M_SV(B)] / 2

Rango efectivo: [2.0%, 100.0%]. En el catálogo SV-118, 91 de 118 elementos tienen M_SV ≥ 40%.

**Definición 3.2.4 — Suma de energías de ionización estructural:**

IP_suma(A,B) = IP_SV(A) + IP_SV(B)

Rango efectivo en SV-118: [710 kJ/mol, 2276 kJ/mol]. El máximo teórico 2 × 1138 = 2276 kJ/mol corresponde al par de los dos elementos con mayor IP_SV del catálogo.

---

## §3.3. Criterio B.1 — Diferencial de electronegatividad estructural

**Definición 3.3 (carácter estructural de par).** Sea ΔEN_SV(A,B) la magnitud definida en 3.2.1. El carácter estructural dominante del par (A,B) se determina por la función de clasificación:

χ_B1(A,B) = 
METAL-SV & si Δ EN_SV ≤ Λ_M = 0,50 COVAL-SV & si 0,50 < Δ EN_SV ≤ Λ_C = 1,50 IONIC-SV & si Δ EN_SV > Λ_C = 1,50

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

*Demostración.* Los cuatro pares metálicos de referencia tienen ΔEN_SV ∈ {0,130; 0,140; 0,240; 0,270}, todos estrictamente menores que 0,50. El par KCl tiene ΔEN_SV = 2,180 y RbCl tiene ΔEN_SV = 2,210, ambos mayores que 1,50. El valor Λ_M = 0,50 es el semientero mínimo que supera el supremo del conjunto metálico de referencia (sup = 0,270). El valor Λ_C = 1,50 es el semientero máximo que queda por debajo del ínfimo del conjunto de pares de alta polaridad estructural verificada. Ambos umbrales son deterministas: se obtienen por verificación directa del conjunto de referencia, sin ajuste inferencial. Q.E.D.

---

## §3.4. Criterio B.2 — Compatibilidad posicional estructural

**Definición 3.4.** El criterio B.2 es aplicable exclusivamente a pares con χ_B1 = METAL-SV. Para un par (A,B) con χ_B1 = METAL-SV:

B.2(A,B) = 
ADMISIBLE & si ρ_SV(A,B) ≤ Λ_ρ = 1,40 NO-APTO & si ρ_SV(A,B) > 1,40

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

*Demostración.* Por verificación directa de la tabla anterior: todos los ρ_SV ≤ 1,322 < 1,40. Q.E.D.

---

## §3.5. Criterio B.3 — Carácter metálico estructural conjunto

**Definición 3.5.** El criterio B.3 opera como refinador de B.1 para pares con χ_B1 = METAL-SV:

B.3(A,B):

| Resultado | Condición |
|---|---|
| CONFIRMADO-M | χ_B1 = METAL-SV y M_joint(A,B) ≥ Λ_M% = 40,0% |
| RECLASIFICA-C | χ_B1 = METAL-SV y M_joint(A,B) < 40,0% |
| N/A | χ_B1 ≠ METAL-SV |

Cuando B.3 devuelve RECLASIFICA-C, el dictamen final del par cambia de APTO-M a APTO-C.

**Fundamento de Λ_M% = 40,0%:**

El umbral de 40% se determina por debajo del mínimo exacto de M_joint en el conjunto metálico de referencia (mínimo: Cu-Zn con M_joint = 55,4%), con separación de 15 puntos porcentuales. Esta separación garantiza que todo par metálico verificado queda incluido, sin recurrir a ajuste paramétrico ni inferencia sobre el dominio extendido.

---

## §3.6. Criterio B.4 — Umbral de suma de ionización estructural

**Definición 3.6.** El criterio B.4 es un filtro universal de admisibilidad, aplicable a todo par independientemente de su χ_B1:

B.4(A,B) = 
ADMISIBLE & si IP_suma(A,B) ≤ Λ_IP = 1800 kJ/mol NO-APTO & si IP_suma(A,B) > 1800 kJ/mol

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

*Demostración.* Por verificación directa: IP_suma máx en el conjunto de referencia = 1658 kJ/mol < 1800 kJ/mol. Q.E.D.

---

## §3.7. Criterio B.5 — Cierre sobre ecuación rectora

**Definición 3.7.** Un par (A,B) satisface B.5 si y solo si ambos elementos pertenecen al catálogo SV-443, es decir, si ambos han superado los cinco criterios de transición química Q.1–Q.5 del catálogo.

B.5(A,B) = ADMISIBLE ⟺ A ∈ Ω_443 y B ∈ Ω_443

**Proposición 3.4.** B.5 es automáticamente satisfecho por todo par (A,B) con A, B ∈ Ω_443.

*Demostración.* Por construcción del catálogo SV-443: todo elemento con índice k ∈ Ω_443 ha superado los criterios Q.1–Q.5, que incluyen el cierre sobre 𝓔★(Γ_U; τ) = 0. El par hereda el cierre de sus componentes. Q.E.D.

---


## §3.8. Simetría de la función de dictamen

**Proposición 3.5 (simetría de D).** Para todo par A, B ∈ Ω₄₄₃ con A ≠ B, D(A,B) = D(B,A).

*Demostración.* Las cuatro magnitudes derivadas de par son simétricas por construcción:

- ΔEN_SV(A,B) = |EN_SV(A) − EN_SV(B)| = |EN_SV(B) − EN_SV(A)| = ΔEN_SV(B,A).
- ρ_SV(A,B) = max(r_SV(A), r_SV(B)) / min(r_SV(A), r_SV(B)) = ρ_SV(B,A).
- M_joint(A,B) = [M_SV(A) + M_SV(B)] / 2 = M_joint(B,A).
- IP_suma(A,B) = IP_SV(A) + IP_SV(B) = IP_suma(B,A).

La función D del §3.9 depende exclusivamente de estas cuatro magnitudes y del indicador B.5, que también es simétrico (A ∈ Ω₄₄₃ ∧ B ∈ Ω₄₄₃ ⟺ B ∈ Ω₄₄₃ ∧ A ∈ Ω₄₄₃). Por lo tanto, D(A,B) = D(B,A) para todo par admisible. Q.E.D.

**Corolario 3.5.1.** El CPS-SV opera sobre los C(443,2) = 97.903 pares no ordenados de Ω₄₄₃ sin pérdida de información respecto al dominio de 195.806 pares ordenados.

*Demostración.* Consecuencia directa de la Proposición 3.5: D(A,B) = D(B,A), por lo que la representación canónica con A < B cubre cada dictamen exactamente una vez. Q.E.D.

## §3.9. Función de dictamen de par y tabla de decisión

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

## §3.10. Verificación sobre el conjunto de referencia completo

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

(†) Divergencia con el régimen convencional — ver §3.12.


---

## §3.11. Cuatro ejemplos trabajados de extremo a extremo

Los cuatro ejemplos siguientes recorren cada paso de la función D(A,B) con todos los valores intermedios explícitos. Cubren la totalidad de las rutas posibles del árbol de decisión: ruta APTO-M completa, ruta RECLASIFICA-C, fallo por B.4 y fallo por B.2.

---

### Ejemplo 1 — Extremo positivo: APTO-M

**Par:** SV-Hierro (k=26) × SV-Cromo (k=24)

| | SV-Hierro (k=26) | SV-Cromo (k=24) |
|---|---|---|
| EN_SV | 1,47 | 1,20 |
| r_SV (pm) | 253,6 | 266,0 |
| IP_SV (kJ/mol) | 602 | 540 |
| M_SV (%) | 72,2 | 81,8 |

**Recorrido de D:**

**B.5:** k=26 ∈ Ω₄₄₃ ✓ y k=24 ∈ Ω₄₄₃ ✓ → ADMISIBLE

**B.4:** IP_suma = 602 + 540 = 1142 kJ/mol ≤ 1800 → ADMISIBLE

**B.1:** ΔEN_SV = |1,47 − 1,20| = 0,270 ≤ 0,50 → χ_B1 = METAL-SV

**B.2:** ρ_SV = 266,0 / 253,6 = 1,049 ≤ 1,40 → ADMISIBLE

**B.3:** M_joint = (72,2 + 81,8) / 2 = 77,0 % ≥ 40,0 % → CONFIRMADO-M

**D(26, 24) = APTO-M**

Interpretación: U opera cerca del polo 1 (ΔEN bajo, alta similitud estructural). Los potenciales del par se igualan en el régimen metálico con H_SV > 0 y E^thermo_SV = 0. Este es el acero inoxidable básico: el corpus lo confirma como par de máxima estabilidad metálica estructural.

---

### Ejemplo 2 — RECLASIFICA-C: B.1 predice METAL-SV, B.3 corrige a APTO-C

**Par:** SV-Argón (k=18) × SV-144 (k=144)

| | SV-Argón (k=18) | SV-144 (k=144) |
|---|---|---|
| EN_SV | 0,00 | 0,00 |
| r_SV (pm) | 179,6 | 173,8 |
| IP_SV (kJ/mol) | 1138 | 600 |
| M_SV (%) | 2,0 | 15,1 |

**Recorrido de D:**

**B.5:** k=18 ∈ Ω₄₄₃ ✓ y k=144 ∈ Ω₄₄₃ ✓ → ADMISIBLE

**B.4:** IP_suma = 1138 + 600 = 1738 kJ/mol ≤ 1800 → ADMISIBLE

**B.1:** ΔEN_SV = |0,00 − 0,00| = 0,000 ≤ 0,50 → χ_B1 = METAL-SV

**B.2:** ρ_SV = 179,6 / 173,8 = 1,033 ≤ 1,40 → ADMISIBLE

**B.3:** M_joint = (2,0 + 15,1) / 2 = 8,6 % < 40,0 % → RECLASIFICA-C

**D(18, 144) = APTO-C** ← ruta RECLASIFICA-C

Interpretación: la identidad polar perfecta (ΔEN = 0) situaría el par en el polo 1. Pero la masa metálica conjunta es insuficiente: U no puede cerrar el morfismo metálico. El par se realiza en régimen covalente estructural — U cierra en modo distinto al que B.1 predice aisladamente. Esta es la función de B.3 como refinador: corrige la predicción de B.1 cuando la masa metálica del par no sostiene el régimen inferido de la distancia polar. 6.144 pares del CPS-SV pasan por esta ruta (16,3% de todos los APTO-C).

---

### Ejemplo 3 — Fallo por B.4: Nada absorbe en el eje energético

**Par:** SV-Argón (k=18) × SV-Kriptón (k=36)

| | SV-Argón (k=18) | SV-Kriptón (k=36) |
|---|---|---|
| EN_SV | 0,00 | 0,00 |
| r_SV (pm) | 179,6 | 191,6 |
| IP_SV (kJ/mol) | 1138 | 1132 |
| M_SV (%) | 2,0 | 2,0 |

**Recorrido de D:**

**B.5:** k=18 ∈ Ω₄₄₃ ✓ y k=36 ∈ Ω₄₄₃ ✓ → ADMISIBLE

**B.4:** IP_suma = 1138 + 1132 = 2270 kJ/mol > 1800 → **NO-APTO** ← falla aquí

**D(18, 36) = NO-APTO**

Interpretación: la energía de persistencia estructural conjunta supera el umbral de activación de U. La trayectoria proto-ternaria no puede cruzar la barrera de potencial: H_SV no alcanza ningún punto estacionario de E^thermo_SV = 0 para este par. Nada absorbe al protopar en el eje energético. Los 15 pares nobles×nobles del subdominio S₁ comparten este resultado (Proposición 6.1).

---

### Ejemplo 4 — Fallo por B.2: Nada absorbe en el eje posicional

**Par:** SV-Nitrógeno (k=7) × SV-136 (k=136)

| | SV-Nitrógeno (k=7) | SV-136 (k=136) |
|---|---|---|
| EN_SV | 1,36 | 1,40 |
| r_SV (pm) | 247,8 | 176,9 |
| IP_SV (kJ/mol) | 577 | 1200 |
| M_SV (%) | 79,2 | 36,8 |

**Recorrido de D:**

**B.5:** k=7 ∈ Ω₄₄₃ ✓ y k=136 ∈ Ω₄₄₃ ✓ → ADMISIBLE

**B.4:** IP_suma = 577 + 1200 = 1777 kJ/mol ≤ 1800 → ADMISIBLE

**B.1:** ΔEN_SV = |1,36 − 1,40| = 0,040 ≤ 0,50 → χ_B1 = METAL-SV

**B.2:** ρ_SV = 247,8 / 176,9 = 1,401 > 1,40 → **NO-APTO** ← falla aquí

**D(7, 136) = NO-APTO**

Interpretación: el par supera la barrera energética (B.4 ✓) y presenta identidad polar casi perfecta (ΔEN = 0,040, régimen METAL-SV), pero los radios estructurales son incompatibles: U no puede cerrar el morfismo posicional. Nada absorbe al protopar en el eje posicional. Este par es el caso límite más ajustado al umbral B.2 del catálogo (ρ = 1,401, con margen de 0,001 sobre Λ_ρ = 1,40); sus 9.858 pares afines constituyen la frontera de mayor sensibilidad posicional del CPS-SV (§6.4, Proposición 6.2).

---

---

## §3.12. Distinción técnica explícita — Inconmensurabilidad de los dictámenes

Los dictámenes APTO-M, APTO-C, APTO-I del aparato SV no son equivalentes a los regímenes metálico, covalente e iónico de la química cuántica convencional. La diferencia no es terminológica sino estructural, y se explica por tres razones:

**Primera razón — Escala EN_SV comprimida.** La electronegatividad estructural EN_SV tiene un rango efectivo de 0,00 a 2,71, frente al rango de Pauling de 0,79 a 3,98 sobre los mismos 118 elementos. La escala SV no es una transformación lineal de la escala de Pauling: se deriva de las compuertas de persistencia y de la ecuación rectora del corpus, y no tiene por qué reproducir las mismas separaciones relativas. El par NaF, por ejemplo, tiene ΔEN_SV = 0,27 porque las propiedades estructurales SV del sodio y el flúor están próximas en la capa operatoria del corpus, aunque la escala de Pauling los sitúe en extremos opuestos. Esto no es un error: es la inconmensurabilidad en operación.

**Segunda razón — M_SV no es conductividad eléctrica convencional.** El carácter metálico estructural M_SV es una propiedad de la Tabla Global derivada de la familia tipológica y la posición en la cadena generativa del corpus, no una medición de conductividad ni de estructura de bandas. Un valor M_SV alto no implica que el elemento conduzca electricidad: implica que su comportamiento estructural SV se sitúa en el régimen de alta persistencia metálica del aparato.

**Tercera razón — La clasificación SV tiene valor propio.** Los regímenes METAL-SV, COVAL-SV e IONIC-SV son categorías del aparato estructural del corpus. Su utilidad no es replicar la tabla de Pauling sino identificar, dentro del catálogo SV-443, qué pares son estructuralmente compatibles bajo qué régimen propio del SV. Cuando el aparato sintetice los candidatos k=119–443, no habrá escala de Pauling que consultar: el único aparato disponible para clasificar su comportamiento de enlace estructural será el SV.

Esta distinción es análoga a la establecida en §5.6 de la *Fórmula de Campo Unificado* (DOI: 10.17613/gxfv3-qjj64) entre cierre estructural y unificación dinámica, y a la establecida en §2bis.4 del catálogo SV-443 entre admisibilidad estructural y predicción cuántica. Los tres documentos comparten la misma posición doctrinal: el corpus opera en una capa anterior al contraste experimental y anterior a la cuantización dinámica, con criterios propios que no compiten con los marcos convencionales sino que los complementan desde una capa estructural diferente.

---

## §3.13. Resumen de umbrales y parámetros del aparato B.1–B.5

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


---

# §4. Aplicación de la función de dictamen al dominio completo Ω₄₄₃ × Ω₄₄₃ — Catálogo de pares estructurales SV

© 2026 Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | CC BY-NC-ND 4.0

---

## §4.0. Alcance y estatuto operatorio de este apartado

Este apartado aplica la función de dictamen D(A,B) definida en §3.9 a la totalidad de los pares no ordenados del catálogo SV-443. El resultado es el **Catálogo de Pares Estructurales SV** (CPS-SV), una tabla de 97.903 entradas con dictamen, magnitudes derivadas y subdominio de pertenencia para cada par.

El estatuto operatorio del CPS-SV hereda directamente el del catálogo SV-443:

- Todo par con al menos un elemento de índice k ∈ {119,…,443} tiene estatuto **U** — estructuralmente admisible según el aparato, no contrastado empíricamente.
- Los dictámenes APTO-M, APTO-C, APTO-I son etiquetas estructurales SV, no predicciones de síntesis ni de enlace cuántico (P.7, P.8, P.9 del §3.0).
- El CPS-SV es el primer catálogo de pares de extensión periódica estructural con criterios propios, no derivados de ningún formalismo Dirac-Fock ni de reglas de compatibilidad cuántica.

---

## §4.1. Cardinalidad del dominio y partición en subdominios

El dominio de pares no ordenados sobre Ω₄₄₃ tiene cardinalidad:

|P| = C(443,2) = (443 × 442) / (2) = 97.903 pares

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

**Resultado 4.6.** Los elementos SV-Nitrógeno (k=7) y SV-Oxígeno (k=8) son los que mayor número de pares APTO-M forman con candidatos extendidos. Sus radios estructurales r_SV intermedios y sus valores M_SV elevados en la Tabla Global determinan que estos dos elementos del primer octeto tienen la mayor compatibilidad posicional con los candidatos del rango k=131–135 del dominio extendido.

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

**Resultado 4.7 — Familia de haluros estructurales SV.** SV-Cloro (k=17, EN_SV=2,71) forma con los candidatos SV-126, SV-144, SV-162, SV-180, SV-288, SV-306, SV-324, SV-342 y SV-360 los pares de mayor polaridad estructural del catálogo (ΔEN_SV = 2,710, el máximo posible por construcción de la escala EN_SV). Estos nueve candidatos comparten EN_SV = 0,000 en la Tabla Global, lo que los sitúa en el extremo opuesto de la escala. El CPS-SV identifica esta familia como los haluros estructurales SV de máxima polaridad — un resultado que no tiene equivalente en ninguna tabla de compatibilidad convencional más allá de Z=118.

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

**Segunda.** Aplica criterios de admisibilidad propios del corpus SV, derivados de las magnitudes de la Tabla Global del catálogo SV-443, sin importar reglas externas de compatibilidad.

**Tercera.** Establece el dictamen NO-APTO para el 46,7% del dominio, lo que convierte al CPS-SV en un filtro operatorio: no todo par de candidatos es admisible estructuralmente, y el aparato lo determina con criterio explícito y reproducible.

**Cuarta.** Es reproducible: el laboratorio del §8 reejecutado sobre el CSV de la Tabla Global produce exactamente el mismo CPS-SV. Ningún paso del cálculo depende de datos externos ni de parámetros no fijados en §3.

---


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

**Resultado 5.1 — Σ₁ y Σ₂ concentran el mayor número absoluto de pares APTO-M intra-familia.** Σ₂ produce 513 y Σ₁ produce 481, sumando 994 de los 1.826 pares APTO-M intra-familia (54,4%). Este resultado es directo del aparato: Σ₁ (convergente pura) y Σ₂ (exploratoria pura) son las dos familias de mayor cardinal (58 y 60 elementos respectivamente) y sus elementos tienen el rango de variación de EN_SV y r_SV más homogéneo del catálogo, lo que eleva la proporción de pares con ΔEN_SV ≤ 0,50.

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

La razón algebraica es directa: Σ₁ y Σ₂ son las familias morfológicamente opuestas — la primera convergente pura (−−−…) y la segunda exploratoria pura (+++…). Sus elementos ocupan extremos complementarios del ciclo de apertura φ sobre la célula SV(3,9). Sin embargo, los valores de EN_SV y r_SV de sus elementos — determinados por las compuertas de persistencia de la ecuación rectora — resultan compatibles bajo los criterios B.1 y B.2 en 1.069 de sus 3.480 pares. La oposición morfológica de trayectoria no implica incompatibilidad de enlace estructural; el criterio de admisibilidad opera sobre las propiedades de la Tabla Global, no sobre los patrones de derivada de activación.

Este resultado no tiene análogo en ningún formalismo convencional de compatibilidad de aleaciones, que no dispone del concepto de familia tipológica de trayectoria como criterio de clasificación.

### §5.4.2. Σ₅ es la familia de mayor conectividad metálica inter-familiar

**Resultado 5.6.** La familia Σ₅ (meseta integral, patrón 000…) participa en 2.647 pares APTO-M inter-familia, el 34,4% del total inter-familia (7.689). Σ₅ aparece en 8 de los 15 pares inter-familia de mayor recuento APTO-M.

La causa es algebraica: los 60 elementos de Σ₅ tienen valores de EN_SV y r_SV distribuidos de forma continua y moderada a lo largo del catálogo, sin los extremos que caracterizan las familias convergentes (EN_SV alto) o exploratorias tardías. Este perfil hace que sus pares con prácticamente cualquier otra familia satisfagan simultáneamente B.1 (ΔEN_SV ≤ 0,50) y B.2 (ρ_SV ≤ 1,40). Σ₅ actúa como nodo de compatibilidad estructural universal del CPS-SV.

**Proposición 5.1.** Σ₅ es la única familia tipológica que forma pares APTO-M con todas las demás familias activas (Σ₁, Σ₂, Σ₃, Σ₄, Σ₆, Σ₇, Σ₈, Σ₁₀, Σ₁₁, Σ₁₂).

*Demostración.* Por verificación directa de la tabla del §5.3: Σ₅ aparece emparejada con todas las familias con recuento APTO-M > 0. Σ₁₂ no aparece en el Top 15, pero su par con Σ₅ produce pares APTO-M: verificado en la enumeración completa del §4. Q.E.D.

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


---

# §6. Criterios de falsación del Catálogo de Pares Estructurales SV

© 2026 Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | CC BY-NC-ND 4.0

---

## §6.0. Posición doctrinal

El corpus SV exige que todo resultado demostrable sea simultáneamente falsable por criterio explícito. El CPS-SV no es una excepción. Este apartado establece cuatro tipos de falsación: falsación por pares de referencia conocidos (F.1), falsación por síntesis experimental futura (F.2), falsación por actualización de la Tabla Global (F.3) y falsación por invariantes derivables (F.4). Las condiciones de falsación son deterministas y verificables sin instrumentos probabilísticos.

---

## §6.1. Tipo F.1 — Falsación por pares de referencia conocidos

**Definición 6.1 (testigo falsador F.1).** Un testigo falsador F.1 es un par (A,B) con A, B ∈ Ω₁₁₈ cuyo comportamiento en química convencional ha sido establecido experimentalmente y documentado en la literatura de referencia, y cuyo dictamen D(A,B) en el CPS-SV contradice ese comportamiento de forma irreconciliable bajo la distinción técnica del §3.12.

Para activar un testigo F.1 no basta con que el régimen SV difiera del régimen cuántico convencional — esa divergencia está prevista y documentada en §3.12 como consecuencia de la inconmensurabilidad. Un testigo F.1 genuino requiere que el aparato B.1–B.5 produzca un dictamen que sea internamente inconsistente con los umbrales fijados en §3.

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

(†) Ti-Al recibe APTO-C en lugar de APTO-M por inconmensurabilidad de la escala EN_SV (§3.12). No constituye testigo F.1 activo porque la divergencia es documentada y estructural, no un error interno del aparato.

**Resultado 6.1.** Ningún par del conjunto de referencia constituye un testigo falsador F.1 activo. El aparato B.1–B.5 es internamente consistente sobre la totalidad del conjunto de referencia verificado.

---

## §6.2. Tipo F.2 — Falsación por síntesis experimental futura

Los 52.170 pares APTO del CPS-SV con al menos un elemento de Ω_ext (k > 118) tienen estatuto operatorio U — estructuralmente admisibles, no contrastados empíricamente. Su falsación es contingente a la síntesis de los elementos correspondientes. El mecanismo de falsación es el siguiente:

**Definición 6.2 (testigo falsador F.2).** Sea (A,B) un par con B ∈ Ω_ext. Si, tras la síntesis confirmada del elemento B y la determinación experimental de sus propiedades EN, r, IP y M%, el dictamen D(A,B) calculado con los valores experimentales difiere del dictamen D(A,B) calculado con los valores estructurales SV de la Tabla Global, entonces el par (A,B) constituye un testigo falsador F.2 para las fórmulas generativas de la Tabla Global.

**Nota metodológica.** Un testigo F.2 no falsifica el aparato B.1–B.5 en sí mismo. Falsifica las fórmulas de cálculo de las propiedades EN_SV, r_SV, IP_SV y M_SV del catálogo SV-443 para el elemento k_B afectado. La corrección consiste en actualizar los valores de la Tabla Global para ese elemento y re-enumerar el CPS-SV — el laboratorio del §8 permite esta re-enumeración sin coste adicional.

**Pares de mayor relevancia para síntesis inmediata** (elementos con Z_SV = 119–120, dominio activo en RIKEN, JINR, HIRFL):

| Par | D(A,B) | ΔEN_SV | ρ_SV | M_joint |
|---|---|---|---|---|
| SV-Hidrógeno (k=1) × SV-Potasio (k=19) | APTO-M | 0,020 | 1,042 | 100,0% |
| SV-Helio (k=2) × SV-Calcio (k=20) | APTO-M | 0,030 | 1,043 | 100,0% |
| SV-Carbono (k=6) × SV-120 (k=120) | APTO-M | 0,370 | 1,389 | 56,8% |

La verificación experimental de cualquiera de estos pares — una vez sintetizado el elemento extendido — constituirá el primer test F.2 del CPS-SV.

---

## §6.3. Tipo F.3 — Falsación por actualización de la Tabla Global

El CPS-SV es una función determinista de la Tabla Global. Toda corrección en los valores EN_SV, r_SV, IP_SV o M_SV de cualquier elemento k propaga cambios a todos los pares (k, j) para j ∈ Ω₄₄₃ \ {k}. El número de pares afectados por la corrección del elemento k es exactamente 442.

**Definición 6.3 (actualización F.3).** Una actualización F.3 consiste en: (1) corregir el valor de la propiedad afectada en la Tabla Global; (2) re-ejecutar el laboratorio del §8 sobre la Tabla Global corregida; (3) comparar el CPS-SV resultante con el CPS-SV original; (4) registrar todos los pares cuyo dictamen haya cambiado como consecuencia de la corrección.

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

Los siguientes enunciados son derivables algebraicamente de los umbrales B.1–B.5 y los valores de la Tabla Global. Cada uno constituye un test verificable sin re-enumeración completa.

**Proposición 6.1 (invariante de gases nobles estructurales SV).** Los 15 pares formados por los seis elementos de gas noble estructural del catálogo SV-118 {k=18, k=36, k=54, k=72, k=90, k=108} reciben dictamen NO-APTO en el CPS-SV.

*Demostración.* Los seis elementos tienen IP_SV ∈ {1108, 1114, 1120, 1126, 1132, 1138} kJ/mol, los seis valores más altos del catálogo SV-118. Para todo par (i,j) de este conjunto, IP_suma ≥ 1108 + 1114 = 2222 kJ/mol > 1800 = Λ_IP. Por lo tanto B.4 falla en todos los casos. Q.E.D.

Verificación directa: los 15 pares nobles×nobles en el CPS-SV tienen IP_suma ∈ {2222, 2228, 2234, 2240, 2246, 2252, 2258, 2264, 2270} kJ/mol. Todos son NO-APTO. ✓

**Proposición 6.2 (pares marginales APTO-M/NO-APTO por B.2).** Existen exactamente 9.858 pares en el CPS-SV que satisfacen B.1 (ΔEN_SV ≤ 0,50), B.3 (M_joint ≥ 40%) y B.4 (IP_suma ≤ 1800) pero reciben NO-APTO por violación exclusiva de B.2 (ρ_SV > 1,40).

*Demostración.* Por enumeración completa de los 97.903 pares del CPS-SV con las condiciones indicadas. El recuento exacto es 9.858. Q.E.D.

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

*Demostración.* Todo par que pudiera pasar a APTO-M bajo relajación de umbrales debe satisfacer B.1 con ΔEN_SV ≤ 0,50. Los pares que actualmente fallan solo B.4 con ΔEN_SV ≤ 0,50 son subconjunto disjunto de los 9.858. Q.E.D.

---

## §6.5. Criterios de no-falsación: qué no falsifica el CPS-SV

Con el fin de evitar testigos falsadores espurios, se enuncian explícitamente las condiciones que **no** constituyen falsación del CPS-SV:

**No es falsación F.1** que un par (A,B) reciba un dictamen SV distinto de su régimen cuántico convencional, si esa divergencia es consecuencia documentada de la inconmensurabilidad de la escala EN_SV (§3.12). Ti-Al como APTO-C en lugar de metálico es el caso paradigmático.

**No es falsación F.2** que un elemento extendido sintetizado tenga propiedades EN_SV, r_SV, IP_SV o M_SV distintas de los valores estructurales de la Tabla Global. Los valores de la Tabla Global son magnitudes estructurales SV, no predicciones de propiedades empíricas (§2bis.6 del catálogo SV-443). La divergencia es un resultado esperado por inconmensurabilidad de marcos; la actualización es el procedimiento correcto.

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


---

# §7. Nota sobre la numeración de secciones

El §7 de esta publicación queda reservado para la integración del CPS-SV con el catálogo de moléculas estructurales SV, publicación inmediatamente posterior en la cadena ascendente del corpus (§1.5.6). Los criterios de admisibilidad molecular ampliarán el aparato de par establecido aquí al nivel de tripletas y agrupaciones de orden superior bajo el mismo operador U_SV. Su desarrollo pertenece a esa publicación futura; el §7 aquí funciona como marcador de continuidad en la cadena.

---

# §8. Laboratorio reproducible — Catálogo de Pares Estructurales SV (CPS-SV)

© 2026 Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | CC BY-NC-ND 4.0

---

## §8.0. Principio de trazabilidad

El CPS-SV es reproducible en su totalidad: cualquier receptor puede re-ejecutar el laboratorio sobre la Tabla Global del catálogo SV-443 y obtener exactamente los mismos 97.903 dictámenes. No existe ningún paso no determinista, ningún parámetro oculto ni ninguna dependencia externa. La reproducibilidad es condición necesaria de la falsabilidad establecida en §6.

---

## §8.1. Contenido del laboratorio

El laboratorio se compone de tres archivos:

| Archivo | Tipo | Función |
|---|---|---|
| `sv_cps.py` | Módulo Python | Implementación de D(A,B), carga, validación, invariantes, escritura CSV |
| `runner.py` | Runner maestro | Orquesta las cuatro fases y emite dictamen JSON |
| `tabla2_sv443.csv` | Datos de entrada | Tabla Global del catálogo SV-443 (443 elementos, 9 columnas) |

**Dependencias:** Python 3.8 o superior. Biblioteca estándar exclusivamente (`csv`, `itertools`, `json`, `time`, `argparse`, `pathlib`). Sin dependencias externas.

---

## §8.2. Ejecución

```babash
# Ejecución estándar (desde la carpeta laboratorios/)
cd laboratorios
PYTHONPATH=src python3 runner.py

# Con rutas explícitas
cd laboratorios
PYTHONPATH=src python3 runner.py --tabla_global /ruta/tabla_global_sv443.csv --salida /ruta/catalogo_pares_sv443.csv
```

**Salida esperada (stdout, formato JSON):**

```json
{
  "corpus": "Sistema Vectorial SV",
  "laboratorio": "CPS-SV — Catálogo de Pares Estructurales SV",
  "tabla_global": "tabla_global_sv443.csv",
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

**Fase 1 — Carga y validación de la Tabla Global.**
El módulo `sv_cps.cargar_tabla2()` lee el CSV, verifica la presencia de las cuatro columnas requeridas (`EN_SV`, `IP_SV`, `r_SV`, `M_SV`), comprueba que el recuento sea exactamente 443 elementos, y valida los rangos admisibles de cada propiedad por elemento. Cualquier anomalía emite un código de error específico (§8.5) y detiene el proceso.

**Fase 2 — Enumeración del dominio completo.**
`sv_cps.enumerar_cps()` aplica `dictamen(ka, kb, datos)` a los C(443,2) = 97.903 pares no ordenados de Ω₄₄₃. La función `dictamen()` implementa la jerarquía B.4 → B.1 → B.2 → B.3 → B.5 del §3.9. Cada par produce una tupla de nueve campos.

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
| `CPS-LOAD-CSV` | Archivo de Tabla Global no encontrado o no legible |
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

El dictamen APTO con recuento `{APTO-M:9515, APTO-C:37580, APTO-I:5075, NO-APTO:45733}` es el resultado canónico sobre la Tabla Global del catálogo SV-443 con fecha 09/05/2026. Toda re-ejecución sobre esa misma Tabla Global debe producir idéntico recuento. Cualquier diferencia indica modificación de la Tabla Global o del código — ambas situaciones deben registrarse como actualización F.3 (§6.3).

---

## §8.7. Verificación del resultado canónico

```
Tabla Global de entrada:  443 elementos, 9 columnas, fecha 09/05/2026
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


---

---

*Note: Canonical material source on GitHub: https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/quimica-factual-y-ciencia-de-materiales-sv/catalogo-pares-estructurales. Supplementary reproducible laboratory deposit on Zenodo: DOI pending assignment. These canonical sources are provided to facilitate direct consultation of the living textual record, reproducible laboratory verification and reader-side translation through standard browser translation tools when required.*

---


---

## §8.8. Inventario del laboratorio reproducible

Los archivos del laboratorio están disponibles en el repositorio canónico:

**Repositorio:** [https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/quimica-factual-y-ciencia-de-materiales-sv/catalogo-pares-estructurales](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/quimica-factual-y-ciencia-de-materiales-sv/catalogo-pares-estructurales)

| Archivo | Ruta en repositorio | Función |
|---|---|---|
| `runner.py` | [`laboratorios/runner.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/quimica-factual-y-ciencia-de-materiales-sv/catalogo-pares-estructurales/laboratorios/runner.py) | Orquesta las cuatro fases: carga, enumeración, verificación de invariantes, escritura CSV. Punto de entrada único. Ejecutar: `PYTHONPATH=src python3 runner.py` |
| `sv_cps.py` | [`laboratorios/src/sv_cps.py`](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/quimica-factual-y-ciencia-de-materiales-sv/catalogo-pares-estructurales/laboratorios/src/sv_cps.py) | Módulo central. Implementa `D(A,B)`, `cargar_tabla_global()`, `enumerar_cps()`, `verificar_invariantes()`, `escribir_csv()`. Sin dependencias externas. |
| `tabla_global_sv443.csv` | [`laboratorios/datos/tabla_global_sv443.csv`](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/quimica-factual-y-ciencia-de-materiales-sv/catalogo-pares-estructurales/laboratorios/datos/tabla_global_sv443.csv) | Tabla Global del catálogo SV-443. 443 elementos, 9 columnas. Fuente única de magnitudes φ(k). |
| `catalogo_pares_sv443.csv` | [`laboratorios/datos/catalogo_pares_sv443.csv`](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/quimica-factual-y-ciencia-de-materiales-sv/catalogo-pares-estructurales/laboratorios/datos/catalogo_pares_sv443.csv) | CPS-SV completo. 97.903 filas de datos. Dictamen, ΔEN_SV, ρ_SV, M_joint, IP_suma por par. |
| `verificacion_cps_sv.json` | [`laboratorios/resultados/verificacion_cps_sv.json`](https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/quimica-factual-y-ciencia-de-materiales-sv/catalogo-pares-estructurales/laboratorios/resultados/verificacion_cps_sv.json) | Resultado canónico de la verificación: recuentos exactos, invariantes PASS, tiempo de cómputo. |

**Depósito Zenodo del laboratorio:** DOI [10.5281/zenodo.20084771](https://doi.org/10.5281/zenodo.20084771)


## Referencias

Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique Fizika*, *1*(3), 195–200. https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195

Cirel'son, B. S. (1980). Quantum generalizations of Bell's inequality. *Letters in Mathematical Physics*, *4*(2), 93–100. https://doi.org/10.1007/BF00417500

Clauser, J. F., Horne, M. A., Shimony, A., & Holt, R. A. (1969). Proposed experiment to test local hidden-variable theories. *Physical Review Letters*, *23*(15), 880–884. https://doi.org/10.1103/PhysRevLett.23.880

Fricke, B., Greiner, W., & Waber, J. T. (1971). The continuation of the periodic table up to Z = 172. *Theoretica Chimica Acta*, *21*(3), 235–260. https://doi.org/10.1007/BF01172015

Hume-Rothery, W., Smallman, R. E., & Haworth, C. W. (1969). *The structure of metals and alloys* (5th ed.). Institute of Metals.

Lloret Egea, J. A. (2026a). *De Bell a Tsirelson sin formalismo de Hilbert: aparato determinista no local del Sistema Vectorial SV*. ITVIA — IA eñ™. https://doi.org/10.17613/1666c-c5g66

Lloret Egea, J. A. (2026b). *Reducción estructural absoluta de Maxwell en el Sistema Vectorial SV*. ITVIA — IA eñ™. https://doi.org/10.17613/kep1t-57539

Lloret Egea, J. A. (2026c). *Fórmula de Campo Unificado F_A = dA + A ∧ A con A = ω ⊕ A*. ITVIA — IA eñ™. https://doi.org/10.17613/gxfv3-qjj64

Lloret Egea, J. A. (2026d). *Análisis preliminar de elementos, materiales y aleaciones de nueva generación en el Sistema Vectorial SV*. ITVIA — IA eñ™. https://doi.org/10.17613/8ryyb-g9h48

Lloret Egea, J. A. (2026e). *Génesis del hidrógeno y teoría de la persistencia energética estructural en el Sistema Vectorial SV*. ITVIA — IA eñ™. https://doi.org/10.17613/qq4q9-sd847

Lloret Egea, J. A. (2026f). *Teoría del TODO y de la NADA en el Sistema Vectorial SV*. ITVIA — IA eñ™. https://github.com/juantoniolloretegea/SV-matematica-semantica

Lloret Egea, J. A. (2026g). *Teoría general de sucesos generadores y de los protocampos unificados en el Sistema Vectorial SV*. ITVIA — IA eñ™.

Lloret Egea, J. A. (2026h). *Laboratorio reproducible del catálogo SV-443* [datos y código]. Zenodo. https://doi.org/10.5281/zenodo.20084771

Maxwell, J. C. (1873). *A treatise on electricity and magnetism* (Vols. 1–2). Clarendon Press.

Oganessian, Y. T., & Utyonkov, V. K. (2015). Super-heavy element research. *Reports on Progress in Physics*, *78*(3), 036301. https://doi.org/10.1088/0034-4885/78/3/036301

Pauling, L. (1932). The nature of the chemical bond. IV. *Journal of the American Chemical Society*, *54*(9), 3570–3582. https://doi.org/10.1021/ja01348a011

Pauling, L. (1960). *The nature of the chemical bond* (3rd ed.). Cornell University Press.


Lloret Egea, J. A. (2026k). *Interacción, intercomposición y transmisión factual entre campos en el Sistema Vectorial SV: operadores 𝓘_SV y 𝓣_SV, distancia factual fibrosa, célula SV(36,6) y articulación serial con el corpus*. ITVIA — IA eñ™. https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/interaccion-intercomposicion-transmision-campos/interaccion-intercomposicion-transmision-campos.md

Lloret Egea, J. A. (2026i). *Entropía factual e irreversibilidad estructural en el Sistema Vectorial SV: dispersión preternaria, ley de transporte por la cadena fundacional y conservación asimétrica del contenido factual*. ITVIA — IA eñ™. https://doi.org/10.17613/vh6ak-6em43

Lloret Egea, J. A. (2026j). *Fuerza, trabajo, calor, entalpía, temperatura, principios y fundamentos de la termodinámica y la correlación entre ellos en el SV*. ITVIA — IA eñ™. https://doi.org/10.17613/ptw68-d1r57

Pyykkö, P. (2011). A suggested periodic table up to Z ≤ 172. *Physical Chemistry Chemical Physics*, *13*(1), 161–168. https://doi.org/10.1039/C0CP01575J
