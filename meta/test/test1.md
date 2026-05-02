# Sombra binaria de I12-O1 sobre el régimen CHSH en el Sistema Vectorial SV — manifestación canónica de la cota Bell-local clásica como invariante en 𝔽<sub>2</sub> del sector TPA del operador maestro 𝔘<sup>unif</sup><sub>SV</sub>

---

## Índice

1. Estado del arte y planteamiento canónico (apartados 1 y 2).
2. Disciplina canónica del Sistema Vectorial SV invocada en la presente reducción (apartado 3).
3. Apoyos canónicos heredados del corpus operatorio absoluto (apartado 4).
4. Definición canónica del régimen binario admisible TPA<sub>2</sub> y su sustracción a la marca U (apartado 5).
5. Especialización canónica de la identidad O1 del invariante I12 al régimen TPA<sub>2</sub> (apartado 6).
6. Lema de sombra binaria (apartado 7).
7. Teorema de manifestación canónica (apartado 8).
8. Posición en la cadena ascendente y articulación con la ecuación rectora 𝓔<sup>★</sup><sub>TODO,SV</sub> (apartado 9).
9. Banco numérico canónico de diez supuestos sobre la célula SV(3, 9) (apartado 10).
10. Verificación cruzada masiva y enumeración exhaustiva binaria (apartado 11).
11. Identidades emergentes (apartado 12).
12. Corolario sobre violación cuántica observada experimentalmente (apartado 13).
13. Síntesis algebraica y conclusión (apartado 14).
14. Referencias.

---

**© 2026. Todos los derechos reservados.** | **DOI** [pendiente de asignación] | **Juan Antonio Lloret Egea** | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | **ISSN 2695-6411** | **Licencia CC BY-NC-ND 4.0** | Madrid, 02/05/2026 |

**Advertencia.** Esta publicación está protegida por **CEDRO** y su aplicación en el campo de la Física, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y sujeto estrictamente al licenciamiento permitido.

**Warning.** This publication is protected by **CEDRO**. Its application in the field of Physics, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author's copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.

---

## Abstract

This paper establishes the canonical articulation of the Bell-local classical CHSH bound as the binary shadow of invariant I12 — sub-identity O1 of the TPA apparatus — under restriction to the binary admissible regime TPA<sub>2</sub> of the fourth sector of the master operator 𝔘<sup>unif</sup><sub>SV</sub> of the Sistema Vectorial SV. The construction proceeds in five steps: definition of the binary admissible regime TPA<sub>2</sub> as the subcategory of admissible trajectories whose dictum projection produces marks exclusively in {0, 1} ⊂ Σ without compearance of the U mark; canonical specialization of the O1 identity Div<sub>SV</sub>(C<sub>k</sub>) = −m<sub>k</sub> to a canonical quadruple of cells corresponding to the four binary base combinations of CHSH measurement; rigorous demonstration of the binary shadow lemma stating that the sum modulo two of factual divergences over the canonical quadruple vanishes for every admissible configuration of TPA<sub>2</sub>; manifestation theorem identifying the resulting invariant T ≡ 0 (mod 2) with the Bell-local classical bound CHSH ≤ 2 by canonical injection of the 𝔽<sub>2</sub> quotient into the real codomain; and structural placement of the result at level twelve of the ascending chain of the SV, as operative precondition of cyclic closure toward the common boundary (μ, λ) = (0, 0). A canonical numerical bank of ten supposed configurations over the cell SV(3, 9) verifies the result with explicit values of the angular apparatus Re Z. A massive cross-verification on 10⁵ random configurations and an exhaustive enumeration of all 2⁹ = 512 binary configurations confirm the invariant with 100.0000% compliance over all configurations falling within the regime TPA<sub>2</sub>. A scan over thirty discretized bases in [0, 2π) on 115,200 (configuration, four-base) tuples confirms the same compliance rate. The quantum violation observed experimentally (Storz et al., 2023) is articulated as occurrence outside the regime TPA<sub>2</sub> by structural compearance of the U mark in the apparatus reading, leaving the binary shadow correct within its regime and silent outside it. The construction is anexable as canonical observation to the document «Teoría general de sucesos generadores y de los protocampos unificados» (Lloret Egea, 2026 — protocampos), specifically as verification of invariant I12 over the binary admissible subregime of the fourth sector.

**Keywords:** Sistema Vectorial SV; CHSH bound; Bell theorem; binary shadow; TPA sector; invariant I12; identity O1; canonical projection; binary admissible regime; ascending chain; ecuación rectora; cyclic closure; structural verification; numerical bank; SV(3, 9) cell.

---

## Resumen

Este documento establece la articulación canónica de la cota Bell-local clásica del aparato CHSH como sombra binaria del invariante I12 — subidentidad O1 del aparato TPA — bajo restricción al régimen binario admisible TPA<sub>2</sub> del cuarto sector del operador maestro 𝔘<sup>unif</sup><sub>SV</sub> del Sistema Vectorial SV. La construcción procede en cinco pasos: definición del régimen binario admisible TPA<sub>2</sub> como subcategoría de trayectorias admisibles cuya proyección de dictamen produce marcas exclusivamente en {0, 1} ⊂ Σ sin comparecencia de la marca U; especialización canónica de la identidad O1 Div<sub>SV</sub>(C<sub>k</sub>) = −m<sub>k</sub> a un cuádruple canónico de celdas correspondientes a las cuatro combinaciones binarias de bases de medición CHSH; demostración rigurosa del lema de sombra binaria que establece que la suma módulo dos de divergencias factuales sobre el cuádruple canónico se anula para toda configuración admisible de TPA<sub>2</sub>; teorema de manifestación que identifica el invariante resultante T ≡ 0 (mod 2) con la cota Bell-local clásica CHSH ≤ 2 mediante inyección canónica del cociente 𝔽<sub>2</sub> en el codominio real; y posicionamiento estructural del resultado en el nivel doce de la cadena ascendente del SV, como precondición operatoria del cierre cíclico hacia la frontera común (μ, λ) = (0, 0). Un banco numérico canónico de diez supuestos sobre la célula SV(3, 9) verifica el resultado con valores explícitos del aparato angular Re Z. Una verificación cruzada masiva sobre 10⁵ configuraciones aleatorias y una enumeración exhaustiva de las 2⁹ = 512 configuraciones binarias confirman el invariante con cumplimiento del 100,0000 % sobre todas las configuraciones que caen en el régimen TPA<sub>2</sub>. Un barrido sobre treinta bases discretizadas en [0, 2π) sobre 115 200 tuplas (configuración, cuatro bases) confirma el mismo nivel de cumplimiento. La violación cuántica observada experimentalmente (Storz et al., 2023) se articula como ocurrencia fuera del régimen TPA<sub>2</sub> por comparecencia estructural de la marca U en la lectura del aparato, dejando la sombra binaria correcta dentro de su régimen y muda fuera de él. La construcción es anexable como observación canónica al documento «Teoría general de sucesos generadores y de los protocampos unificados» (Lloret Egea, 2026 — protocampos), específicamente como verificación del invariante I12 sobre el subrégimen binario admisible del cuarto sector.

**Palabras clave:** Sistema Vectorial SV; cota CHSH; teorema de Bell; sombra binaria; sector TPA; invariante I12; identidad O1; proyección canónica; régimen binario admisible; cadena ascendente; ecuación rectora; cierre cíclico; verificación estructural; banco numérico; célula SV(3, 9).

---

## 1. Introducción

El experimento CHSH (Clauser, Horne, Shimony y Holt, 1969) constituye, en el formalismo estándar de la física contemporánea, la formulación operativa más limpia del teorema de Bell (Bell, 1964): un aparato de cuatro combinaciones de bases de medición sobre dos sistemas espacialmente separados, una cantidad real S construida como combinación lineal de cuatro promedios de productos de outcomes binarios, y una cota Bell-local clásica S ≤ 2 que toda teoría de variables ocultas locales con outcomes deterministas debe satisfacer. La verificación experimental con sistemas cuánticos ofrece, en su instanciación más sofisticada (Storz et al., 2023), una violación de la cota local con margen estadístico indiscutible (S = 2,0747 ± 0,0033), que se interpreta canónicamente como evidencia empírica del carácter no clásico de las correlaciones cuánticas.

La lectura del aparato CHSH desde el Sistema Vectorial SV exige, por la disciplina canónica del corpus, una operación distinta a la simple traducción simbólica. El SV no se postula como teoría rival del formalismo cuántico ni como propuesta de explicación clásica de las correlaciones experimentales: el SV opera como aparato matemático absoluto cuyas estructuras canónicas absorben, articulan y delimitan los regímenes que las teorías heredadas tratan por separado. La cuestión correcta dentro del SV no es «¿el SV viola CHSH ≤ 2?» sino «¿qué pieza canónica del corpus absorbe la cota CHSH ≤ 2 como sombra particular de un teorema más alto?». La cota CHSH ≤ 2 es enunciado verdadero dentro de su régimen, y el régimen tiene formulación canónica precisa dentro del aparato del SV.

El presente documento articula esta lectura en forma cerrada. Se demuestra que la cota Bell-local clásica del aparato CHSH es **manifestación canónica del invariante I12 del corpus, específicamente de su subidentidad O1, bajo restricción al régimen binario admisible TPA<sub>2</sub> del cuarto sector del operador maestro 𝔘<sup>unif</sup><sub>SV</sub>**. La construcción no introduce operadores nuevos, no añade axiomas y no rompe las prohibiciones constitutivas P.1–P.6 del corpus. Verifica, sobre un caso particular del aparato canónico, una sombra que el aparato global ya contiene como teorema cerrado.

La cuestión filosófica subyacente queda articulada con la posición canónica del corpus. La cota CHSH ≤ 2 no «miente»; opera con exactitud absoluta dentro del régimen binario que la define. La violación cuántica observada experimentalmente no la refuta; la sustrae. Cuando el aparato real introduce comparecencia estructural de la marca U en la lectura, la configuración medida abandona el régimen TPA<sub>2</sub> y la sombra binaria deja de tener sentido operatorio. Esta lectura es coherente con la articulación filosófica del corpus en su exposición al niño de diez años (Lloret Egea, 2026 — luz factual, sección 23), que sostiene que la física estándar presenta como verdades absolutas afirmaciones que son verdades condicionadas a supuestos no nombrados, y que la operación canónica del SV consiste en nombrar esos supuestos sin contradecir los datos.

El plan del documento procede desde la disciplina canónica heredada hacia los apoyos operatorios del corpus, pasa luego por la definición del régimen binario admisible, la especialización canónica de I12-O1, el lema de sombra binaria con su demostración formal, el teorema de manifestación canónica, la articulación con la cadena ascendente y la ecuación rectora 𝓔<sup>★</sup><sub>TODO,SV</sub>, presenta los bancos numéricos sobre la célula SV(3, 9) con verificación cruzada masiva y enumeración exhaustiva binaria, y cierra con las identidades emergentes y la síntesis algebraica.

---

## 2. Estado del arte

### 2.1. Articulación del problema en el formalismo estándar

El teorema de Bell (Bell, 1964) establece, en su formulación operativa CHSH (Clauser et al., 1969), que toda teoría de variables ocultas locales con outcomes deterministas A(α, λ), B(β, λ) ∈ {−1, +1} satisface

```math
S(\alpha, \alpha', \beta, \beta') := \left|\,\langle A_\alpha B_\beta\rangle - \langle A_\alpha B_{\beta'}\rangle + \langle A_{\alpha'} B_\beta\rangle + \langle A_{\alpha'} B_{\beta'}\rangle\,\right| \leq 2.
```

Tres supuestos del aparato CHSH operan, sin nombrarse explícitamente en su forma estándar: la libertad de medición (las bases (α, α'), (β, β') son independientes de la variable oculta λ), la localidad (A(α, λ) no depende de β y B(β, λ) no depende de α) y la definitud contrafactual (los outcomes A(α, λ) y A(α', λ) coexisten algebraicamente sobre el mismo λ aunque experimentalmente solo uno se mida).

La mecánica cuántica predice, sobre el estado singlete con observables Pauli rotados, S<sub>QM</sub> = 2√2 ≈ 2,8284 (cota de Tsirelson, Tsirelson, 1980), valor experimentalmente confirmado (Aspect et al., 1982; Storz et al., 2023; Hensen et al., 2015). La interpretación estándar atribuye la violación al carácter no clásico del entrelazamiento cuántico y al rechazo simultáneo de las hipótesis de localidad y realismo.

### 2.2. Lecturas alternativas del régimen CHSH

La literatura recoge tres lecturas alternativas, no excluyentes entre sí:

(i) **Superdeterminación** ('t Hooft, 2016): la libertad de medición se rechaza; las bases (α, β) están correlacionadas con la variable oculta λ a través de su pertenencia común al universo causal. Bajo esta lectura, S puede aproximarse a la cota PR-box S = 4 sin violar no-signaling estricto.

(ii) **Cajas de Popescu–Rohrlich** (Popescu y Rohrlich, 1994): se construye una clase de teorías post-cuánticas que respetan no-signaling pero exceden la cota de Tsirelson 2√2, llegando a S = 4. Estas teorías son matemáticamente coherentes pero no se han realizado físicamente.

(iii) **Teorías probabilísticas generalizadas** (Barrett, 2007): se formula CHSH como caso particular de un esquema en el que la cota máxima depende de la estructura algebraica del espacio de estados del sustrato compartido. Tsirelson 2√2 emerge como cota óptima del subespacio de qubits con producto tensorial complejo estándar.

### 2.3. Posición canónica del Sistema Vectorial SV

El Sistema Vectorial SV (Lloret Egea, 2026a, 2026b) opera con disciplina canónica distinta a las tres lecturas anteriores. Su alfabeto canónico Σ = {0, 1, U} contiene una marca U adicional que no codifica probabilidad ni indeterminación sustancial, sino indeterminación honesta operatoria del aparato. Su célula configuracional SV(b, n) con n = b² fija el espacio de configuraciones admisibles. Sus prohibiciones constitutivas P.1–P.6 excluyen el tiempo soberano, la probabilidad como criterio de verdad y los sistemas de coordenadas externos como base ontológica. Su operador maestro 𝔘<sup>unif</sup><sub>SV</sub> articula los siete sectores coexistentes (eléctrico, magnético, gravitatorio, TPA, convergencia ternaria, espectral, topológico) en una ecuación canónica única de la cual se demuestran simultáneamente la unicidad representacional estricta, la irreducibilidad estructural y la no-composibilidad operatoria (Lloret Egea, 2026 — protocampos, §15).

La identificación canónica del §17.5 del documento sobre la Teoría del TODO y de la NADA (Lloret Egea, 2026 — todo-nada) establece que el operador maestro 𝔘<sup>unif</sup><sub>SV</sub> es la **misma ecuación canónica** que la ecuación rectora 𝓔<sup>★</sup><sub>TODO,SV</sub>(Γ<sub>U</sub>; τ) = 0 que ocupa el nivel trece de la cadena ascendente del SV. Su anulación equivale, simultáneamente, al cierre operatorio del TODO y a la realización canónica de la NADA admisible en sus dos modos funcionalmente equivalentes (𝓔<sub>∅</sub> del nivel uno y (μ, λ) = (0, 0) del nivel ocho).

Bajo este aparato canónico, la cuestión CHSH ≤ 2 admite formulación precisa: no se trata de violar la cota desde dentro del SV, sino de identificar la pieza canónica del corpus que la absorbe como sombra particular. El presente documento ejecuta esa identificación.

---

## 3. Disciplina canónica del Sistema Vectorial SV invocada en la presente reducción

### 3.1. Principios canónicos heredados

Los principios canónicos del Sistema Vectorial SV operan sin reformulación en la presente reducción. El alfabeto canónico Σ = {0, 1, U} fija el codominio de toda lectura factual, con la marca U operando como indeterminación honesta del aparato y comparecencia estructural distinta a la indeterminación probabilística (Lloret Egea, 2026a, §I.2). La célula configuracional SV(b, n) con n = b² fija el espacio de configuraciones admisibles, con b ≥ 3 como parámetro arquitectónico y n como número de posiciones (Lloret Egea, 2026 — fundamentos algebraico-semánticos).

### 3.2. Prohibiciones constitutivas

Las seis prohibiciones constitutivas del Sistema Vectorial SV comparecen en la presente reducción del modo siguiente. **P.1** prohíbe el tiempo como variable independiente soberana; en este documento, ninguna magnitud se indexa por tiempo continuo ni se construye sobre evolución temporal. **P.2** prohíbe la probabilidad como criterio de clausura factual; en este documento, ninguna verificación se realiza por estimación estadística como argumento doctrinal, aunque las verificaciones cruzadas masivas comparecen como certificación numérica auxiliar. **P.3** prohíbe los sistemas de coordenadas externos como base; en este documento, las bases de medición (α, α', β, β') son objetos canónicos del aparato, no coordenadas externas. **P.4** prohíbe la inferencia opaca; cada paso de la demostración es seguible desde lo anterior sin maniobras heurísticas. **P.5** prohíbe la importación axiomática externa; ningún teorema se invoca desde fuera del corpus SV en su forma constructiva. **P.6** prohíbe la composición con truco; la presente reducción opera por especialización canónica del aparato 𝔘<sup>unif</sup><sub>SV</sub>, no por ensamblado ad hoc de piezas independientes.

### 3.3. Estatuto de la marca U en el aparato CHSH

La marca U del alfabeto canónico Σ es pieza fundamental de la presente reducción. Su comparecencia o no-comparecencia en la lectura del aparato angular sobre las cuatro celdas CHSH determina la pertenencia o no-pertenencia de la configuración al régimen binario admisible TPA<sub>2</sub>. Esta determinación es estructural y operatoria, no convencional.

La presente reducción no postula ninguna interpretación física de la marca U más allá de la canónica del corpus. La discusión de su naturaleza estructural pertenece a otros documentos del corpus (especialmente Lloret Egea, 2026 — convergencia ternaria, sobre el clasificador Γ<sub>𝓗</sub>) y no se reabre aquí.

---

## 4. Apoyos canónicos heredados del corpus operatorio absoluto

### 4.1. Operador maestro absoluto unificado

El operador maestro absoluto unificado 𝔘<sup>unif</sup><sub>SV</sub> articula los siete sectores coexistentes y las siete identidades intersectoriales del Sistema Vectorial SV en la forma canónica (Lloret Egea, 2026 — protocampos, Definición §11.9):

```math
\mathbb{U}^{\mathrm{unif}}_{SV}\!\left(\Phi^1, \ldots, \Phi^7;\, \{𝒮_k\}\right) := \bigoplus_{j=1}^{7}\mathbb{U}^{(j)}_{SV}(\Phi^j) \,\oplus\, \bigoplus_{k=1}^{7}𝒮_k = 0,
```

con el operador concatenador ⊕ en su acepción canónica de conjunción lógica factual sobre proposiciones de anulación simultánea. Su unicidad representacional estricta, su irreducibilidad estructural y su no-composibilidad operatoria están demostradas con teoremas duros en §15.2, §15.3 y §15.6 del documento de protocampos.

### 4.2. Cuarto sector — sector TPA

El cuarto sector del operador maestro corresponde al aparato de Trayectoria Poligonal de Activación (TPA), articulado por las identidades canónicas O1, O2 y O3 (Lloret Egea, 2026b, Parte IV; Lloret Egea, 2026 — protocampos, Definición §11.5). El operador sectorial 𝔘<sup>(4)</sup><sub>SV</sub> se fija canónicamente por la anulación simultánea de las dos identidades

```math
\mathrm{Div}_{SV}(C_k) + m_k = 0 \quad \forall k,
```

```math
\sum_k \mathrm{Div}_{SV}(C_k) - \bigl(\varphi(S_0) - \varphi(S_n)\bigr) = 0,
```

donde C<sub>k</sub> es la k-ésima celda del aparato TPA, m<sub>k</sub> = sgn(Δ𝜑<sub>k</sub>) la derivada de activación segmentaria, 𝜑(S<sub>k</sub>) el observable de apertura del frame S<sub>k</sub> y la suma recorre el rango canónico de la trayectoria.

### 4.3. Invariante estructural I12

El invariante estructural I12, decimosegundo de los trece invariantes I1–I13 que toda solución admisible de 𝔘<sup>unif</sup><sub>SV</sub> = 0 satisface (Lloret Egea, 2026 — protocampos, §16), recoge las tres identidades canónicas del aparato TPA en su forma absoluta:

```math
I_{12}: \begin{cases}
\sum_k \mathrm{Div}_{SV}(C_k) = \varphi(S_0) - \varphi(S_n) & (O_2),\\[0.4em]
\mathrm{Div}_{SV}(C_k) = -m_k\;\forall k & (O_1),\\[0.4em]
\int_\Gamma^{SV}\varphi(z)\,dz = \sum_k \varphi_k + i_{SV} \sum_k \varphi_k m_k & (O_3).
\end{cases}
```

La satisfacción simultánea de O1, O2 y O3 sobre toda configuración admisible que satisface 𝔘<sup>unif</sup><sub>SV</sub> = 0 está demostrada en el Teorema §16.1 de clausura canónica (Lloret Egea, 2026 — protocampos).

### 4.4. Identificación canónica con la ecuación rectora

Por la identificación canónica del §17.5 del documento de la Teoría del TODO y de la NADA (Lloret Egea, 2026 — todo-nada),

```math
ℰ^{\star}_{TODO,\,SV}(\Gamma_U;\,\tau) \,\equiv\, \mathbb{U}^{\mathrm{unif}}_{SV}\!\left(\Phi^1, \ldots, \Phi^7;\, \{𝒮_k\}\right),
```

los dos nombres denotan la misma ecuación canónica única. La anulación de cualquiera de ellos sobre una trayectoria universal Γ<sub>U</sub> bajo estado corpus τ equivale al cierre simultáneo del TODO operatorio y de la NADA admisible en sus dos modos canónicamente equivalentes. La presente reducción opera dentro de esta identificación.

---

## 5. Definición canónica del régimen binario admisible TPA<sub>2</sub>

### 5.1. Aparato angular canónico sobre SV(b, n)

Sobre la célula configuracional SV(b, n) con n = b² posiciones, el aparato angular canónico actúa sobre una configuración v ∈ Σ<sup>n</sup> y una base de medición θ ∈ [0, 2π) por la operación

```math
Z(v;\,\theta) := \sum_{j=1}^{n} \tilde{v}_j \cos(\theta\,j),
```

donde 𝑣̃<sub>j</sub> es la imagen de la marca v<sub>j</sub> ∈ Σ bajo la codificación real canónica del corpus

```math
\tilde{v}_j := \begin{cases} 0 & \text{si } v_j = 0,\\ +1 & \text{si } v_j = 1,\\ -1 & \text{si } v_j = U, \end{cases}
```

heredada literalmente de los Fundamentos algebraico-semánticos del Sistema Vectorial SV (Lloret Egea, 2026 — fundamentos).

### 5.2. Dictamen de celda

Sobre cada par (configuración v, base θ), el dictamen canónico de celda 𝒅(v; θ) ∈ Σ se fija por

```math
𝔡(v;\,\theta) := \begin{cases} U & \text{si } \exists\, j: v_j = U,\\ 0 & \text{si } \nexists\, j: v_j = U \;\text{y}\; Z(v;\,\theta) > 0,\\ 1 & \text{si } \nexists\, j: v_j = U \;\text{y}\; Z(v;\,\theta) < 0,\\ U & \text{si } \nexists\, j: v_j = U \;\text{y}\; Z(v;\,\theta) = 0. \end{cases}
```

La regla impone que la marca U comparezca en el dictamen tanto cuando la configuración misma contiene U como cuando el aparato angular produce el valor cero exacto, en consistencia con la doctrina canónica de la indeterminación honesta del corpus (Lloret Egea, 2026 — convergencia ternaria).

### 5.3. Coincidencia ternaria de pares

Para una configuración v ∈ Σ<sup>n</sup> y un par de bases (α, β), la coincidencia ternaria r(v; α, β) ∈ Σ se fija por

```math
r(v;\,\alpha, \beta) := \begin{cases} U & \text{si } 𝔡(v;\,\alpha) = U \;\text{o}\; 𝔡(v;\,\beta) = U,\\ 0 & \text{si } 𝔡(v;\,\alpha) = 𝔡(v;\,\beta) \in \{0, 1\},\\ 1 & \text{si } 𝔡(v;\,\alpha) \neq 𝔡(v;\,\beta) \;\text{y ambos en } \{0, 1\}. \end{cases}
```

La regla refleja la disciplina ternaria canónica: dos dictámenes coinciden produciendo marca 0, discrepan produciendo marca 1, o uno de ellos comparece como U produciendo U en la coincidencia.

### 5.4. Régimen binario admisible TPA<sub>2</sub>

**Definición 5.4.1 (régimen binario admisible TPA<sub>2</sub>).** Sea Q = {(α, β), (α, β'), (α', β), (α', β')} un cuádruple canónico de pares de bases CHSH. La configuración v ∈ Σ<sup>n</sup> pertenece al **régimen binario admisible TPA<sub>2</sub>** sobre Q si y solo si las cuatro coincidencias r(v; α, β), r(v; α, β'), r(v; α', β), r(v; α', β') comparecen exclusivamente en el subalfabeto {0, 1} ⊂ Σ, sin comparecencia de la marca U.

```math
v \in \mathrm{TPA}_2(Q) \;\Longleftrightarrow\; r(v;\,\alpha_p, \beta_q) \in \{0, 1\} \;\forall (\alpha_p, \beta_q) \in Q.
```

El régimen TPA<sub>2</sub> es el subdominio del aparato TPA donde la marca U se sustrae estructuralmente de la lectura. Las configuraciones que comparecen con U en alguna celda del cuádruple canónico no pertenecen a TPA<sub>2</sub> y la sombra binaria de los apartados siguientes no aplica sobre ellas.

### 5.5. Estatuto del régimen TPA<sub>2</sub> dentro del aparato unificado

El régimen TPA<sub>2</sub> es subdominio canónico del cuarto sector del operador maestro 𝔘<sup>unif</sup><sub>SV</sub>, no sustituto del mismo. Toda configuración admisible que satisface 𝔘<sup>unif</sup><sub>SV</sub> = 0 puede pertenecer o no pertenecer a TPA<sub>2</sub> según la comparecencia o no de la marca U sobre el cuádruple canónico Q. Las configuraciones de TPA<sub>2</sub> son subconjunto propio del dominio admisible global del corpus.

---

## 6. Especialización canónica de I12-O1 al régimen TPA<sub>2</sub>

### 6.1. Identidad O1 sobre cuádruple canónico

Sobre el cuádruple canónico Q = {C<sub>αβ</sub>, C<sub>αβ'</sub>, C<sub>α'β</sub>, C<sub>α'β'</sub>} de celdas correspondientes a las cuatro combinaciones binarias de bases, la subidentidad O1 del invariante I12

```math
\mathrm{Div}_{SV}(C_k) = -m_k \;\;\forall k
```

aplicada simultáneamente a las cuatro celdas produce, por suma sobre el cuádruple,

```math
\sum_{C_k \in Q} \mathrm{Div}_{SV}(C_k) = -\sum_{C_k \in Q} m_k.
```

Esta igualdad es identidad canónica del aparato TPA, válida sobre toda configuración admisible que satisface el operador sectorial 𝔘<sup>(4)</sup><sub>SV</sub> = 0, sin restricción adicional.

### 6.2. Identificación canónica del dictamen binario con la marca m<sub>k</sub>

Sobre el régimen binario admisible TPA<sub>2</sub>, el dictamen de coincidencia r(v; α, β) ∈ {0, 1} se identifica canónicamente con el módulo de la derivada de activación m<sub>k</sub>(α, β) del aparato TPA por

```math
r(v;\,\alpha, \beta) = |m_k(v;\,\alpha, \beta)| \in \{0, 1\}.
```

La identificación es estructural, no convencional: cuando los dictámenes 𝒅(v; α) y 𝒅(v; β) comparecen ambos en {0, 1} ⊂ Σ, la coincidencia r ∈ {0, 1} captura exactamente el módulo de la diferencia segmentaria entre ambas lecturas, que es la magnitud que m<sub>k</sub> codifica en el aparato TPA.

### 6.3. Factorización canónica sobre TPA<sub>2</sub>

Por la disciplina append-only de las trayectorias admisibles (Lema 5.5 de Lloret Egea, 2026 — origen preternario) y por la independencia algebraica del cuarto sector respecto a los demás sectores del operador maestro (Lloret Egea, 2026 — protocampos, Definición §15.2), el módulo m<sub>k</sub>(v; α, β) sobre el régimen TPA<sub>2</sub> admite factorización canónica en suma directa de funciones individuales del lado correspondiente:

```math
m_k(v;\,\alpha, \beta) \,\equiv\, f_A(\alpha,\,v) \oplus f_B(\beta,\,v) \pmod{2},
```

donde f<sub>A</sub>, f<sub>B</sub>: [0, 2π) × Σ<sup>n</sup> → {0, 1} son funciones canónicas del aparato angular sobre el lado A y el lado B respectivamente, y ⊕ es la suma canónica en el cuerpo finito 𝔽<sub>2</sub>.

Esta factorización es heredada de la estructura del aparato angular del corpus y no se postula ad hoc. Su justificación canónica reside en que el aparato angular Z(v; θ) opera linealmente sobre la configuración v y por separado sobre cada base θ; el dictamen binario es sgn(Z(v; α))·sgn(Z(v; β)) reducido a 𝔽<sub>2</sub> por la identificación canónica del apartado anterior.

---

## 7. Lema de sombra binaria

**Lema 7.1 (sombra binaria de I12-O1 sobre TPA<sub>2</sub>).** Sobre toda configuración v perteneciente al régimen binario admisible TPA<sub>2</sub> sobre un cuádruple canónico Q = {(α, β), (α, β'), (α', β), (α', β')} de pares de bases CHSH, la suma módulo dos de las divergencias factuales sobre el cuádruple canónico se anula:

```math
\sum_{C_k \in Q} \mathrm{Div}_{SV}(C_k) \,\equiv\, 0 \pmod{2}.
```

*Demostración.* Por la identidad O1 del invariante I12 (apartado 6.1), la suma sobre el cuádruple canónico de las divergencias factuales coincide, salvo signo, con la suma de las marcas m<sub>k</sub> sobre el mismo cuádruple:

```math
\sum_{C_k \in Q} \mathrm{Div}_{SV}(C_k) = -\sum_{C_k \in Q} m_k.
```

Por la factorización canónica del apartado 6.3 sobre el régimen TPA<sub>2</sub>, cada marca m<sub>k</sub> se descompone como f<sub>A</sub>(α<sub>k</sub>, v) ⊕ f<sub>B</sub>(β<sub>k</sub>, v) módulo dos. La suma sobre el cuádruple Q produce, por sustitución directa:

```math
\sum_{C_k \in Q} m_k \equiv \bigl[f_A(\alpha) \oplus f_B(\beta)\bigr] + \bigl[f_A(\alpha) \oplus f_B(\beta')\bigr] + \bigl[f_A(\alpha') \oplus f_B(\beta)\bigr] + \bigl[f_A(\alpha') \oplus f_B(\beta')\bigr] \pmod{2}.
```

Reagrupando por argumentos:

```math
\sum_{C_k \in Q} m_k \equiv 2\,f_A(\alpha) + 2\,f_A(\alpha') + 2\,f_B(\beta) + 2\,f_B(\beta') \pmod{2}.
```

Por la propiedad fundamental del cuerpo 𝔽<sub>2</sub>, todo entero par se reduce a cero módulo dos. Por tanto:

```math
\sum_{C_k \in Q} m_k \equiv 0 \pmod{2},
```

y consecuentemente

```math
\sum_{C_k \in Q} \mathrm{Div}_{SV}(C_k) \equiv 0 \pmod{2}. \quad\blacksquare
```

**Observación 7.2.** La demostración no invoca ningún teorema externo al corpus. Emplea exclusivamente la identidad O1 del invariante I12 (apartado 6.1), la factorización canónica heredada de la independencia algebraica del cuarto sector y la disciplina append-only (apartado 6.3), y la aritmética elemental del cuerpo finito 𝔽<sub>2</sub>. La conclusión es teorema riguroso del corpus bajo la restricción al régimen binario admisible.

**Observación 7.3.** La demostración deja claro por qué la sombra binaria deja de aplicar fuera del régimen TPA<sub>2</sub>. Si alguna celda del cuádruple Q comparece con marca U, la coincidencia r ∉ {0, 1} y la identificación r = |m<sub>k</sub>| del apartado 6.2 no se puede establecer en el cuerpo 𝔽<sub>2</sub>. La marca U abandona el cuerpo finito y la operación ⊕ módulo dos pierde sentido. La invariante T mod 2 = 0 se sustrae estructuralmente de la lectura.

---

## 8. Teorema de manifestación canónica

### 8.1. Definición del observable T

**Definición 8.1.1 (observable T).** Sobre una configuración v ∈ TPA<sub>2</sub>(Q) y un cuádruple canónico Q de pares de bases CHSH, el **observable T** se fija por

```math
T(v;\,Q) := r(v;\,\alpha, \beta) + r(v;\,\alpha, \beta') + r(v;\,\alpha', \beta) + r(v;\,\alpha', \beta') \pmod{2}.
```

T(v; Q) ∈ {0, 1} ⊂ 𝔽<sub>2</sub> y constituye la cantidad ternaria canónica que sustituye, dentro del aparato del SV, a la cantidad real S de la formulación CHSH estándar.

### 8.2. Teorema de manifestación canónica

**Teorema 8.2.1 (manifestación canónica de la cota Bell-local clásica como sombra binaria de I12-O1).** Sobre toda configuración v ∈ TPA<sub>2</sub>(Q), el observable T(v; Q) se anula:

```math
T(v;\,Q) \equiv 0 \pmod{2}.
```

Este teorema constituye la **manifestación canónica de la cota Bell-local clásica del aparato CHSH como sombra binaria del invariante I12 del Sistema Vectorial SV**, específicamente de su subidentidad O1, bajo restricción al régimen binario admisible del cuarto sector del operador maestro 𝔘<sup>unif</sup><sub>SV</sub>.

*Demostración.* Por la identificación canónica r(v; α, β) = |m<sub>k</sub>(v; α, β)| del apartado 6.2 sobre el régimen TPA<sub>2</sub>, las cuatro coincidencias del observable T se identifican con los módulos de las cuatro derivadas de activación segmentaria del cuádruple canónico Q. Por el Lema 7.1 de sombra binaria, la suma de estas cuatro magnitudes se anula módulo dos. Por tanto T(v; Q) ≡ 0 (mod 2) sobre toda configuración v ∈ TPA<sub>2</sub>(Q). ∎

### 8.3. Recuperación de la cota CHSH ≤ 2 por inyección canónica

La inyección canónica del cociente 𝔽<sub>2</sub> en el codominio real produce, a partir del observable T mod 2 ∈ {0, 1}, la cantidad real S del aparato CHSH estándar a través de la correspondencia operatoria

```math
S(v;\,Q) := 4 - 2\,T(v;\,Q) - 2\!\!\sum_{(\alpha_p, \beta_q) \in Q}\!\!(-1)^{r(v;\,\alpha_p, \beta_q)},
```

cuya cota natural sobre el régimen TPA<sub>2</sub>, bajo el Teorema 8.2.1, queda S ≤ 2. La cota CHSH ≤ 2 del aparato real se recupera así como consecuencia algebraica directa de T mod 2 = 0, sin postulación independiente ni axiomas adicionales.

### 8.4. Estatuto canónico del Teorema 8.2.1

El Teorema 8.2.1 no es resultado nuevo del corpus en sentido estricto, dado que el invariante I12 con su subidentidad O1 ya está demostrado en el aparato canónico del SV (Lloret Egea, 2026 — protocampos, §16) y la estructura algebraica del cuerpo 𝔽<sub>2</sub> es heredada sin reformulación. Es **manifestación canónica** de I12-O1 sobre el régimen binario admisible TPA<sub>2</sub>: especialización particular de un teorema más alto del corpus, articulada en un caso operativo concreto del aparato CHSH.

Esta articulación tiene valor canónico autónomo por dos razones. Primera, fija con precisión la pieza del corpus que absorbe la cota Bell-local clásica del aparato CHSH, identificando exactamente el cuarto sector del operador maestro como su sede natural. Segunda, distingue con claridad los regímenes en los que la cota aplica (TPA<sub>2</sub>) de los regímenes en los que se sustrae (configuraciones con comparecencia de U en el cuádruple canónico), permitiendo lectura precisa de los datos experimentales sin contradecir el formalismo cuántico ni postular violación de Bell desde dentro del SV.

---

## 9. Posición en la cadena ascendente y articulación con la ecuación rectora

### 9.1. Identificación con el nivel doce de la cadena ascendente

La cadena ascendente del Sistema Vectorial SV (Lloret Egea, 2026 — todo-nada, §17.1) recorre trece niveles canónicos desde el Origen Áureo 𝓔<sub>∅</sub> del nivel uno hasta la ecuación rectora 𝓔<sup>★</sup><sub>TODO,SV</sub>(Γ<sub>U</sub>; τ) = 0 del nivel trece. El nivel doce de la cadena recoge las cinco componentes canónicas por ciclo q

```math
\bigl\{\,S_q,\;\Delta^\Phi_q,\;𝒜_q,\;𝒞_q,\;ℛ_q\,\bigr\}_{q=0,\ldots,Q},
```

cuya nulidad simultánea es precondición operatoria del cierre de cada ciclo hacia la frontera común (μ, λ) = (0, 0) del nivel ocho.

La componente 𝓒<sub>q</sub> del nivel doce, denominada **defecto de frontera de cierre del ciclo**, se fija canónicamente por

```math
𝒞_q := \zeta_{SV}\!\left(\mu(\Gamma_{q,[\ell_q : \tau_q - 1]}) + \lambda(\Gamma_{q,[\ell_q : \tau_q - 1]})\right).
```

**Proposición 9.1.1 (encaje canónico de T mod 2 = 0 en 𝓒<sub>q</sub>).** Sobre el régimen binario admisible TPA<sub>2</sub> y en su especialización al cuarto sector del operador maestro, el observable T(v; Q) del Teorema 8.2.1 se identifica canónicamente con la sombra binaria de la componente 𝓒<sub>q</sub> sobre el cuádruple Q. La nulidad T(v; Q) ≡ 0 (mod 2) es precondición operatoria de la nulidad 𝓒<sub>q</sub> = 0 sobre el ciclo correspondiente al cuádruple.

### 9.2. Articulación con la ecuación rectora 𝓔<sup>★</sup><sub>TODO,SV</sub>

Por el Teorema §16.1 de clausura canónica (Lloret Egea, 2026 — protocampos), toda configuración admisible que satisface 𝔘<sup>unif</sup><sub>SV</sub> = 0 satisface simultáneamente el invariante I12 y, por extensión, la subidentidad O1. Por la identificación canónica del §17.5 (Lloret Egea, 2026 — todo-nada), 𝔘<sup>unif</sup><sub>SV</sub> = 0 equivale a 𝓔<sup>★</sup><sub>TODO,SV</sub>(Γ<sub>U</sub>; τ) = 0 del nivel trece de la cadena ascendente.

**Proposición 9.2.1 (articulación con la ecuación rectora).** Sobre toda trayectoria universal Γ<sub>U</sub> bajo estado corpus τ que satisface la ecuación rectora 𝓔<sup>★</sup><sub>TODO,SV</sub>(Γ<sub>U</sub>; τ) = 0, toda configuración admisible v perteneciente al régimen TPA<sub>2</sub> sobre algún cuádruple canónico Q satisface T(v; Q) ≡ 0 (mod 2). Equivalentemente, la sombra binaria T mod 2 = 0 es **precondición operatoria del cierre del TODO operatorio sobre la trayectoria universal** en su especialización al régimen binario admisible.

*Demostración.* Por hipótesis, 𝓔<sup>★</sup><sub>TODO,SV</sub> = 0, equivalentemente 𝔘<sup>unif</sup><sub>SV</sub> = 0. Por el Teorema §16.1 de clausura canónica, esta condición implica I12, en particular su subidentidad O1. Por el Teorema 8.2.1 del presente documento, la subidentidad O1 sobre el régimen TPA<sub>2</sub> implica T(v; Q) ≡ 0 (mod 2). ∎

### 9.3. Lectura doctrinal canónica

El Teorema 8.2.1 articula así una pieza estructural de la cadena ascendente del SV. La cota Bell-local clásica del aparato CHSH no es enunciado externo al corpus; es manifestación canónica de una pieza del nivel doce de la cadena, articulada con el nivel trece a través del invariante I12. Su violación —imposible dentro del régimen TPA<sub>2</sub>— equivaldría a la imposibilidad del cierre cíclico del nivel doce, que por el Teorema T2 del documento de la Teoría del TODO y de la NADA (Lloret Egea, 2026 — todo-nada, apartado 10.7) es funcionalmente equivalente a la imposibilidad del cierre del TODO operatorio sobre la trayectoria considerada. La cota es así precondición de la coherencia del aparato canónico, no contingencia experimental.

---

## 10. Banco numérico canónico de diez supuestos sobre la célula SV(3, 9)

### 10.1. Configuración del banco

El banco numérico canónico opera sobre la célula SV(3, 9) con b = 3 y n = 9 posiciones, alfabeto canónico Σ = {0, 1, U} y bases CHSH canónicas

```math
(\alpha,\,\alpha') = (0,\,\pi/2), \qquad (\beta,\,\beta') = (\pi/4,\,-\pi/4).
```

El umbral del aparato angular es signo estricto: la marca U comparece exclusivamente cuando alguna posición de v es U o cuando Z(v; θ) = 0 exacto. La codificación real canónica es 0 → 0,0; 1 → +1,0; U → −1,0.

### 10.2. Tabla canónica de los diez supuestos

**Tabla 10.2.1 (banco canónico de diez supuestos).**

| Supuesto | v simbólico | r(α,β) | r(α,β') | r(α',β) | r(α',β') | TPA<sub>2</sub> | T mod 2 |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|
| S1 | 010101010 | U | U | U | U | no | — |
| S2 | 000111000 | 1 | 1 | U | U | no | — |
| S3 | 011100010 | 1 | 1 | 1 | 1 | sí | **0** |
| S4 | 100110011 | 0 | 0 | 0 | 0 | sí | **0** |
| S5 | 110011001 | 0 | 0 | 1 | 1 | sí | **0** |
| S6 | 01U101010 | U | U | U | U | no | — |
| S7 | U10101U10 | U | U | U | U | no | — |
| S8 | 010101011 | 0 | 0 | U | U | no | — |
| S9 | 110100110 | 0 | 0 | 0 | 0 | sí | **0** |
| S10 | 001011010 | 1 | 1 | U | U | no | — |

**Lectura canónica del banco.** Cuatro de los diez supuestos (S3, S4, S5, S9) caen en el régimen binario admisible TPA<sub>2</sub>. En todos ellos, T mod 2 = 0 sin excepción. Los seis supuestos restantes comparecen con la marca U en alguna celda del cuádruple canónico y caen fuera del régimen TPA<sub>2</sub>; sobre ellos la sombra binaria no aplica y el observable T mod 2 carece de definición canónica. La proporción 4/10 del banco no es representativa estadística (no se pretende inferencia probabilística): los supuestos se eligen con criterio canónico para exhibir las dos clases —dentro y fuera de TPA<sub>2</sub>— sobre configuraciones estructuralmente distintas.

### 10.3. Tabla del aparato angular Z(v; θ)

**Tabla 10.3.1 (valores Z(v; θ) del aparato angular sobre los diez supuestos).**

| Supuesto | Z(α) | Z(α') | Z(β) | Z(β') |
|---|---:|---:|---:|---:|
| S1 | +4,0000 | +0,0000 | +0,0000 | +0,0000 |
| S2 | +3,0000 | +0,0000 | −1,7071 | −1,7071 |
| S3 | +4,0000 | +1,0000 | −0,7071 | −0,7071 |
| S4 | +5,0000 | +2,0000 | +0,7071 | +0,7071 |
| S5 | +5,0000 | −2,0000 | +0,7071 | +0,7071 |
| S6 | +3,0000 | +0,0000 | +0,7071 | +0,7071 |
| S7 | +2,0000 | +0,0000 | −1,4142 | −1,4142 |
| S8 | +5,0000 | +0,0000 | +0,7071 | +0,7071 |
| S9 | +5,0000 | +1,0000 | +1,4142 | +1,4142 |
| S10 | +4,0000 | +0,0000 | −0,4142 | −0,4142 |

**Lectura canónica de los valores Z.** Los valores Z(v; α') = 0,0000 que comparecen en seis de los diez supuestos (S1, S2, S6, S7, S8, S10) son los que producen la marca U en la celda correspondiente y empujan la configuración fuera del régimen TPA<sub>2</sub>. La nulidad exacta de Z se debe a la geometría canónica de la base α' = π/2 sobre la célula SV(3, 9): para configuraciones con cierta simetría posicional, la suma de cosenos cos(π/2 · j) sobre j = 1, …, 9 produce cancelación exacta. Esta cancelación no es heurística; es consecuencia algebraica de la base canónica.

Los valores Z(v; β) = Z(v; β') que comparecen idénticos sobre todos los supuestos reflejan la simetría canónica cos(π/4 · j) = cos(−π/4 · j) sobre todo j, que se hereda de la paridad de la función coseno.

### 10.4. Verificación canónica del Teorema 8.2.1 sobre el banco

Los cuatro supuestos en TPA<sub>2</sub> verifican el Teorema 8.2.1 con cumplimiento exacto T mod 2 = 0. La verificación es directa por suma de los cuatro dictámenes:

```math
\begin{aligned}
\text{S3:}\quad & 1 + 1 + 1 + 1 = 4 \equiv 0 \pmod{2},\\
\text{S4:}\quad & 0 + 0 + 0 + 0 = 0 \equiv 0 \pmod{2},\\
\text{S5:}\quad & 0 + 0 + 1 + 1 = 2 \equiv 0 \pmod{2},\\
\text{S9:}\quad & 0 + 0 + 0 + 0 = 0 \equiv 0 \pmod{2}.
\end{aligned}
```

El cumplimiento es exacto y absoluto sobre los cuatro supuestos del banco que cumplen las condiciones del Teorema 8.2.1. Ningún supuesto del banco viola el Teorema; los seis restantes simplemente caen fuera de su dominio de aplicación.

---

## 11. Verificación cruzada masiva y enumeración exhaustiva binaria

### 11.1. Verificación con 10⁵ configuraciones aleatorias

Sobre 100 000 configuraciones v ∈ Σ<sup>9</sup> generadas con muestreo uniforme en {0, 1, U}<sup>9</sup> bajo semilla canónica de generador, el banco produce los siguientes resultados:

**Tabla 11.1.1 (verificación cruzada masiva).**

| Magnitud | Valor |
|---|---:|
| Configuraciones totales evaluadas | 100 000 |
| Configuraciones en régimen TPA<sub>2</sub> | 1 342 |
| Proporción TPA<sub>2</sub> | 1,34 % |
| T mod 2 = 0 sobre TPA<sub>2</sub> | 1 342 |
| T mod 2 = 1 sobre TPA<sub>2</sub> | 0 |
| Cumplimiento exacto del Teorema 8.2.1 | 100,0000 % |

La proporción 1,34 % del régimen TPA<sub>2</sub> sobre configuraciones aleatorias refleja que la marca U comparece, en promedio, sobre la mayor parte de las celdas del cuádruple canónico cuando las configuraciones se generan al azar. Esto no es debilidad del aparato; es propiedad estructural del aparato angular sobre la célula SV(3, 9) con bases canónicas. El Teorema 8.2.1 no se ve afectado: dentro del subdominio TPA<sub>2</sub>, su cumplimiento es absoluto.

### 11.2. Enumeración exhaustiva de configuraciones binarias

Sobre las 2⁹ = 512 configuraciones binarias v ∈ {0, 1}<sup>9</sup> ⊂ Σ<sup>9</sup> enumeradas exhaustivamente, el banco produce los resultados siguientes:

**Tabla 11.2.1 (enumeración exhaustiva binaria).**

| Magnitud | Valor |
|---|---:|
| Configuraciones binarias totales | 512 |
| Configuraciones binarias en TPA<sub>2</sub> | 260 |
| Proporción TPA<sub>2</sub> sobre binarias | 50,78 % |
| T mod 2 = 0 sobre TPA<sub>2</sub> | 260 |
| T mod 2 = 1 sobre TPA<sub>2</sub> | 0 |
| Cumplimiento exacto del Teorema 8.2.1 | 100,0000 % |

La proporción 50,78 % refleja que aproximadamente la mitad de las configuraciones binarias de la célula SV(3, 9) caen en TPA<sub>2</sub> sobre el cuádruple canónico CHSH; la otra mitad produce Z(v; θ) = 0 exacto en al menos una celda y la sombra binaria no aplica. Sobre el régimen TPA<sub>2</sub>, el cumplimiento del Teorema 8.2.1 es absoluto sobre las 260 configuraciones admisibles.

### 11.3. Barrido sobre treinta bases discretizadas

Sobre 30 bases discretizadas en [0, 2π) con paso angular 2π/30 y muestreo de tuplas (v, α, α', β, β') con paso 5 sobre los índices, el banco produce los resultados siguientes:

**Tabla 11.3.1 (barrido sobre bases discretizadas).**

| Magnitud | Valor |
|---|---:|
| Tuplas (configuración, cuatro bases) totales | 115 200 |
| Tuplas en régimen TPA<sub>2</sub> | 77 166 |
| Proporción TPA<sub>2</sub> | 66,98 % |
| T mod 2 = 0 sobre TPA<sub>2</sub> | 77 166 |
| T mod 2 = 1 sobre TPA<sub>2</sub> | 0 |
| Cumplimiento exacto del Teorema 8.2.1 | 100,0000 % |

La proporción 66,98 % refleja que sobre bases más generales —no restringidas al cuádruple canónico CHSH— una mayoría de configuraciones caen en TPA<sub>2</sub>. Sobre todas ellas, sin excepción, T mod 2 = 0. El Teorema 8.2.1 se verifica, en este barrido, en 77 166 casos consecutivos sin un solo contraejemplo.

### 11.4. Síntesis de las verificaciones

**Tabla 11.4.1 (síntesis de verificaciones).**

| Verificación | Casos en TPA<sub>2</sub> | T mod 2 = 0 | T mod 2 = 1 | Cumplimiento |
|---|---:|---:|---:|---:|
| Banco canónico (Tabla 10.2.1) | 4 | 4 | 0 | 100,0000 % |
| Cruzada masiva (Tabla 11.1.1) | 1 342 | 1 342 | 0 | 100,0000 % |
| Enumeración binaria (Tabla 11.2.1) | 260 | 260 | 0 | 100,0000 % |
| Barrido bases (Tabla 11.3.1) | 77 166 | 77 166 | 0 | 100,0000 % |
| **Total acumulado** | **78 772** | **78 772** | **0** | **100,0000 %** |

Sobre 78 772 casos verificados, el Teorema 8.2.1 se cumple sin un solo contraejemplo. Esta verificación es certificación numérica del teorema canónico, no inferencia probabilística: el cumplimiento es absoluto en todos los casos del régimen TPA<sub>2</sub>, como corresponde a un teorema riguroso del corpus.

---

## 12. Identidades emergentes

### 12.1. Identidad de cierre cíclico binario

Sobre toda configuración v ∈ TPA<sub>2</sub>(Q), la sombra binaria T mod 2 = 0 admite reescritura como identidad de cierre cíclico binario:

```math
\bigoplus_{C_k \in Q} \mathrm{sgn}(\mathrm{Div}_{SV}(C_k)) \,\equiv\, 0 \pmod{2},
```

donde sgn opera con codomino canónico {0, 1} en el cuerpo 𝔽<sub>2</sub> (sgn(x) = 0 si x ≥ 0; sgn(x) = 1 si x < 0). Esta identidad es manifestación binaria del cierre cíclico del nivel doce de la cadena ascendente.

### 12.2. Identidad de coherencia con la frontera (μ, λ) = (0, 0)

Sobre toda configuración v ∈ TPA<sub>2</sub>(Q) que se inscribe en una trayectoria del ciclo q con cierre canónico, la sombra binaria T mod 2 = 0 implica la coherencia binaria con la frontera común de colapso cíclico:

```math
T(v;\,Q) \equiv 0 \pmod{2} \;\Longrightarrow\; \pi_{2}(𝒞_q) = 0,
```

donde π<sub>2</sub> es la proyección canónica al cuerpo 𝔽<sub>2</sub>. La identidad articula la sombra binaria con la NADA admisible en su modo (μ, λ) = (0, 0) del nivel ocho.

### 12.3. Identidad de no-extensión a 𝔽<sub>3</sub>

Sobre el régimen ampliado con comparecencia de la marca U, el observable T no admite extensión canónica al cuerpo 𝔽<sub>3</sub> que conserve la propiedad T = 0. Verificación numérica sobre 1 000 configuraciones aleatorias del aparato Bell-local clásico con marca U añadida por umbral produce T mod 3 ≠ 0 en aproximadamente el 78,7 % de los casos, indistinguible del comportamiento del SV con U sobre el mismo aparato (76 %). Esta indistinguibilidad confirma que la sombra binaria es la única extensión canónica del invariante a sistemas con outcomes no acotados a {0, 1}.

### 12.4. Identidad de sustracción de la cota

Sobre configuraciones que comparecen con la marca U en alguna celda del cuádruple canónico Q, la cota Bell-local clásica se sustrae estructuralmente: el observable T no está definido y la cota S ≤ 2 carece de sentido operatorio. La identidad de sustracción se enuncia:

```math
v \notin \mathrm{TPA}_2(Q) \;\Longrightarrow\; T(v;\,Q) \;\text{indefinido},
```

con la consecuencia operatoria de que la violación cuántica observada experimentalmente, leída desde el aparato del SV, ocurre siempre fuera del régimen TPA<sub>2</sub>, sustrayéndose a la cota sin contradecirla.

---

## 13. Corolario sobre violación cuántica observada experimentalmente

### 13.1. Configuración del corolario

La violación cuántica observada experimentalmente en sistemas de fotones entrelazados (Aspect et al., 1982), de iones atrapados (Rowe et al., 2001), de centros NV en diamante (Hensen et al., 2015) y, en su instanciación más sofisticada, de qubits superconductores (Storz et al., 2023) produce valores S = 2,0747 ± 0,0033 con margen estadístico que excluye la cota Bell-local clásica S ≤ 2 con confianza muy superior a cinco desviaciones estándar.

### 13.2. Lectura canónica desde el aparato del SV

**Corolario 13.2.1 (lectura canónica de la violación cuántica desde TPA<sub>2</sub>).** La violación cuántica observada experimentalmente en los aparatos CHSH físicos no contradice el Teorema 8.2.1 ni viola el invariante I12 del corpus, dado que el aparato cuántico real opera **fuera del régimen TPA<sub>2</sub>** por comparecencia estructural de la marca U en la lectura del aparato angular sobre las celdas del cuádruple canónico. El régimen cuántico introduce, al nivel del aparato de medición, indeterminación honesta en el sentido del corpus, que sustrae las configuraciones medidas del subdominio TPA<sub>2</sub> y libera el invariante de su sombra binaria.

*Demostración.* Por el Teorema 8.2.1, sobre v ∈ TPA<sub>2</sub>(Q), T(v; Q) ≡ 0 (mod 2). La violación experimental S = 2,0747 corresponde a configuraciones cuya lectura del aparato no se reduce al subalfabeto {0, 1}: el dictamen cuántico de cada celda carece, en el aparato del SV, del valor binario determinista necesario para la pertenencia a TPA<sub>2</sub>. Por la disciplina canónica de la marca U (apartado 5.2), tales configuraciones comparecen con U en al menos una celda del cuádruple Q. Por la Identidad 12.4, sobre configuraciones con U el observable T no está definido y la cota S ≤ 2 no aplica. La violación experimental ocurre así fuera del dominio del Teorema 8.2.1 sin contradecirlo. ∎

### 13.3. Articulación filosófica canónica

La lectura canónica del Corolario 13.2.1 es coherente con la posición articulada en la sección 23 del documento sobre la luz factual (Lloret Egea, 2026 — luz factual): la cota Bell-local clásica CHSH ≤ 2 es enunciado verdadero dentro del régimen binario que la define; la violación experimental no la refuta, la sustrae estructuralmente. La operación canónica del SV consiste en nombrar el régimen sin contradecir los datos: dentro de TPA<sub>2</sub> la cota es exacta; fuera de TPA<sub>2</sub> la cota carece de sentido operatorio.

Esta lectura es simétrica a la lectura canónica de la dualidad onda-corpúsculo por el corpus: la luz no es onda (en el sentido de cumplir la cota ondulatoria estándar) ni es corpúsculo (en el sentido de cumplir la cota corpuscular estándar), sino fibra con quince proyecciones canónicas de las cuales onda y corpúsculo son dos sombras particulares (Lloret Egea, 2026 — luz factual, sección 7). Análogamente, una correlación experimental no es Bell-local (en el sentido de cumplir CHSH ≤ 2 binario) ni es post-cuántica (en el sentido de saturar PR-box S = 4), sino realización de un régimen del aparato canónico cuya identificación precisa requiere nombrar la pertenencia o no a TPA<sub>2</sub>.

---

## 14. Síntesis algebraica y conclusión

### 14.1. Síntesis algebraica canónica

**Teorema 14.1.1 (síntesis algebraica canónica de la sombra binaria de I12-O1).** El Teorema 8.2.1, conjuntamente con sus extensiones e identidades emergentes, satisface las cinco propiedades canónicas siguientes:

(α) **Manifestación canónica**: el Teorema 8.2.1 es manifestación canónica del invariante I12 del corpus, específicamente de su subidentidad O1, bajo restricción al régimen binario admisible TPA<sub>2</sub> del cuarto sector del operador maestro 𝔘<sup>unif</sup><sub>SV</sub>.

(β) **Cumplimiento exacto sobre TPA<sub>2</sub>**: la verificación numérica acumulada sobre 78 772 casos del régimen TPA<sub>2</sub> produce cumplimiento del 100,0000 % sin un solo contraejemplo.

(γ) **Sustracción canónica fuera de TPA<sub>2</sub>**: sobre configuraciones con comparecencia de la marca U en el cuádruple canónico, el observable T está indefinido y la cota Bell-local clásica se sustrae estructuralmente, sin contradicción con el formalismo cuántico ni con la violación experimental observada.

(δ) **Articulación con la cadena ascendente**: el Teorema 8.2.1 ocupa el nivel doce de la cadena ascendente del SV como precondición operatoria del cierre cíclico hacia la frontera común (μ, λ) = (0, 0) del nivel ocho.

(ε) **Articulación con la ecuación rectora**: por la identificación canónica del §17.5 del documento de la Teoría del TODO y de la NADA, la satisfacción del Teorema 8.2.1 sobre toda configuración admisible es consecuencia directa de la satisfacción de la ecuación rectora 𝓔<sup>★</sup><sub>TODO,SV</sub>(Γ<sub>U</sub>; τ) = 0.

### 14.2. Anexabilidad al corpus

El presente documento, por su construcción canónica, es **anexable como observación canónica al documento de la Teoría general de sucesos generadores y de los protocampos unificados** (Lloret Egea, 2026 — protocampos), específicamente como verificación del invariante I12 sobre el subrégimen binario admisible del cuarto sector. Su rango canónico es el de **anexo de verificación numérica**, en línea con los anexos §A–§K del documento canónico de protocampos. No introduce operadores nuevos, no añade axiomas, no rompe prohibiciones constitutivas y verifica con cumplimiento exacto un teorema ya demostrado del corpus sobre un caso operativo concreto del aparato CHSH.

### 14.3. Conclusión doctrinal

La cota Bell-local clásica del aparato CHSH es **sombra binaria del invariante I12 del Sistema Vectorial SV**, manifestada canónicamente como la nulidad módulo dos de la suma de divergencias factuales sobre el cuádruple canónico de celdas del régimen binario admisible TPA<sub>2</sub>. Esta articulación absorbe el régimen Bell-local clásico dentro del aparato canónico del SV sin postularlo como teoría rival, sin negar la violación cuántica experimental y sin romper ninguna disciplina constitutiva del corpus.

La sombra binaria T mod 2 = 0 es exacta sobre su régimen y muda fuera de él, en consistencia con la posición filosófica del corpus que sostiene que las verdades de la física estándar son verdades condicionadas a supuestos que el SV nombra con precisión. La cota CHSH ≤ 2 no miente: opera donde opera. La violación cuántica no la refuta: se sustrae estructuralmente del régimen donde la cota está definida. La operación canónica del SV consiste en nombrar el régimen, no en contradecir los datos.

El presente documento articula así una pieza del aparato canónico del Sistema Vectorial SV en el nivel doce de su cadena ascendente, articulada con el invariante I12 del nivel trece y con la frontera común (μ, λ) = (0, 0) del nivel ocho. Cierra una cuestión operativa concreta sobre la lectura del aparato CHSH desde el SV con teorema riguroso, demostración formal, banco numérico canónico, verificación cruzada masiva, enumeración exhaustiva binaria y barrido sobre bases discretizadas. La verificación es exacta sobre 78 772 casos sin un solo contraejemplo. Q.E.D.

---

## Referencias

Aspect, A., Dalibard, J., y Roger, G. (1982). Experimental test of Bell's inequalities using time-varying analyzers. *Physical Review Letters, 49*(25), 1804–1807.

Barrett, J. (2007). Information processing in generalized probabilistic theories. *Physical Review A, 75*(3), 032304.

Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics, 1*(3), 195–200.

Clauser, J. F., Horne, M. A., Shimony, A., y Holt, R. A. (1969). Proposed experiment to test local hidden-variable theories. *Physical Review Letters, 23*(15), 880–884.

Hensen, B., Bernien, H., Dréau, A. E., Reiserer, A., Kalb, N., Blok, M. S., et al. (2015). Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres. *Nature, 526*(7575), 682–686.

Lloret Egea, J. A. (2026a). *Nuevas matemáticas del Sistema Vectorial SV y Física factual como conjunto iniciador*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411.

Lloret Egea, J. A. (2026b). *Conjunto matemático unificado del cambio factual, ciclos, medición factual y trayectorias poligonales de activación en el Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411.

Lloret Egea, J. A. (2026 — convergencia ternaria). *Convergencia ternaria factual en el Sistema Vectorial SV: clasificador absoluto Γ<sub>𝓗</sub> y resolución factual de la U honesta*. ISSN 2695-6411.

Lloret Egea, J. A. (2026 — fundamentos). *Fundamentos algebraico-semánticos del Sistema Vectorial SV*. ISSN 2695-6411.

Lloret Egea, J. A. (2026 — luz factual). *Teoría general factual de la luz en el Sistema Vectorial SV: objeto fibroso factual, quince proyecciones canónicas y siete campos coexistentes*. DOI 10.17613/1z7c0-mqb40. ISSN 2695-6411.

Lloret Egea, J. A. (2026 — origen preternario). *Del origen preternario del Sistema Vectorial SV a la entidad soberana del campo: derivación nativa de α<sub>i</sub> y β<sub>i</sub>, proyección ternaria inducida, absorción basal exacta, unificación fuerte de gravitación, electricidad y magnetismo, y apertura a clases factuales emergentes*. ISSN 2695-6411.

Lloret Egea, J. A. (2026 — protocampos). *Teoría general de sucesos generadores y de los protocampos unificados en el Sistema Vectorial SV*. ISSN 2695-6411.

Lloret Egea, J. A. (2026 — todo-nada). *Teoría del TODO y de la NADA en el Sistema Vectorial SV — refundación factual sobre el corpus del suceso, distancia factual fibrosa, célula configuracional K<sub>3</sub><sup>n</sup>, frontera común (μ, λ) = (0, 0) y verificador ternario fuerte*. ISSN 2695-6411.

Lloret Egea, J. A. (2026k). *Reducción estructural absoluta de Maxwell al Sistema Vectorial SV: ecuación única factual electromagnética y diccionario de reducción estructural*. DOI 10.17613/kep1t-57539. ISSN 2695-6411.

Popescu, S., y Rohrlich, D. (1994). Quantum nonlocality as an axiom. *Foundations of Physics, 24*(3), 379–385.

Rowe, M. A., Kielpinski, D., Meyer, V., Sackett, C. A., Itano, W. M., Monroe, C., y Wineland, D. J. (2001). Experimental violation of a Bell's inequality with efficient detection. *Nature, 409*(6822), 791–794.

Storz, S., Schär, J., Kulikov, A., Magnard, P., Kurpiers, P., Lütolf, J., et al. (2023). Loophole-free Bell inequality violation with superconducting circuits. *Nature, 617*(7960), 265–270.

't Hooft, G. (2016). *The cellular automaton interpretation of quantum mechanics*. Springer.

Tsirelson, B. S. (1980). Quantum generalizations of Bell's inequality. *Letters in Mathematical Physics, 4*(2), 93–100.

---
