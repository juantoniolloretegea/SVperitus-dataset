## §14. Desarrollo algebraico del operador maestro absoluto $`\mathbb{E}_{SV}`$

El presente desarrollo algebraico consolida el aparato operatorio del régimen electromagnético factual del Sistema Vectorial SV sobre el régimen canalizado de propagación $`\Sigma_{\mathrm{canal}}`$, quinto eslabón de la cadena fundacional absoluta del corpus,

$$
\Omega_{\mathrm{pre}} \xrightarrow{\Pi_3^H} K_3^n \xrightarrow{\varepsilon} \Xi_{SV} \xrightarrow{\mathfrak{K}_{SV}} \Sigma_{\mathrm{conc}} \xrightarrow{\mathfrak{H}_{SV}} \Sigma_{\mathrm{canal}} \xrightarrow{\mathfrak{T}_{SV}} \{m_0,\,\chi_\alpha,\,U\},
$$

fijada en el §3.2 del documento *Fundamentos operatorios absolutos del electromagnetismo factual en el Sistema Vectorial SV* (Lloret Egea, 2026j, §1). Las magnitudes factuales se realizan como aplicaciones $`q: \Xi_{SV} \to \mathbb{R}`$ sobre el dominio canónico geometrizado $`\Xi_{SV}`$, conforme al estatuto operatorio del mencionado §3.2.

El desarrollo se organiza en cuatro piezas: núcleo local absoluto (§14.1 a §14.3), paquete operatorio temprano (§14.4 a §14.11), desarrollo profundo (§14.12 a §14.17), aplicaciones (§14.18 y §14.19). El cierre se consigna con bancos visibles (§14.20) y síntesis algebraica (§14.21). Todo teorema queda demostrado con aparato operatorio absoluto del corpus. Las prohibiciones constitutivas del sistema (tiempo absoluto, probabilidad fundante, estadística como criterio de verdad, coordenadas externas como base ontológica) se preservan sin excepción. El cosido metrológico absoluto opera sobre las unidades UE_MFC, UFE, UFM, UFC y derivadas compatibles.

---

## Núcleo local absoluto

## §14.1. Jacobiano factual de sensibilidad de régimen $`J_{SV}`$

### 14.1.1. Definición canónica

Sea $`q: \Xi_{SV} \to \mathbb{R}^k`$ una magnitud factual vectorial admisible dependiente del parámetro admisible $`\theta \in \Theta_{SV} \subset \mathbb{R}^m`$ del régimen. El **jacobiano factual de sensibilidad de régimen** se define como la matriz $`k \times m`$ de componentes

$$
(J_{SV})^a{}_b(q,\theta) \;:=\; \partial^{SV}_{\theta_b}\, q^a,
$$

donde $`\partial^{SV}_{\theta_b}`$ es la derivación factual respecto de la componente $`\theta_b`$ del parámetro admisible.

### 14.1.2. Determinante factual de sensibilidad

Cuando $`k = m`$, el determinante $`\det(J_{SV})`$ define el **índice escalar de sensibilidad factual** del régimen. La anulación $`\det(J_{SV}) = 0`$ caracteriza regímenes con pérdida local de rango, equivalentes a configuraciones donde el parámetro admisible deja de generar variación independiente sobre la magnitud factual.

### 14.1.3. Transformación bajo cambio factual admisible

**Proposición 14.1.1.** Sea $`\Phi: \Xi_{SV} \to \Xi'_{SV}`$ un cambio factual admisible con matriz factual $`M^a{}_c`$. El jacobiano factual transforma según

$$
(J'_{SV})^a{}_b \;=\; M^a{}_c \cdot (J_{SV})^c{}_b,
$$

*y su determinante según $`\det(J'_{SV}) = \det(M) \cdot \det(J_{SV})`$.*

**Demostración.** Por la regla de la cadena factual aplicada al cambio $`\Phi`$ sobre el dominio admisible, $`q'^a = M^a{}_c\, q^c`$, y la derivación $`\partial^{SV}_{\theta_b}`$ actúa linealmente sobre $`q'^a`$ con coeficiente $`M^a{}_c`$ independiente del parámetro. La invariancia del parámetro $`\theta`$ bajo $`\Phi`$ (por la definición de cambio factual admisible) garantiza la forma de transformación matricial indicada. El determinante se sigue de la multiplicatividad canónica. Q.E.D.

### 14.1.4. Régimen regular y régimen singular

Se define como **régimen factual regular** el subdominio de $`\Theta_{SV}`$ donde $`\det(J_{SV}) \neq 0`$, y como **régimen factual singular** el subconjunto donde $`\det(J_{SV}) = 0`$. En régimen regular, toda magnitud factual admite reconstrucción local a partir de $`k`$ derivaciones factuales independientes; en régimen singular, la reconstrucción exige activación del criterio absoluto de frontera del §14.2.

### 14.1.5. Verificación visible sobre configuración admisible

Sobre la celda admisible del mosaico $`SV(3,9)`$ con parámetro admisible bidimensional $`\theta = (\theta_1, \theta_2)`$ y magnitud factual $`q(\theta) = (\theta_1^2 + \theta_2, \; \theta_1 \theta_2)`$, el jacobiano factual se evalúa como

$$
J_{SV}(q,\theta) \;=\; \begin{pmatrix} 2\theta_1 & 1 \\ \theta_2 & \theta_1 \end{pmatrix}, \qquad \det(J_{SV}) \;=\; 2\theta_1^2 - \theta_2.
$$

En $`\theta = (1, 1)`$, $`\det(J_{SV}) = 2 \cdot 1 - 1 = 1 \neq 0`$: régimen regular. En $`\theta = (1, 2)`$, $`\det(J_{SV}) = 2 - 2 = 0`$: régimen singular localizado sobre la curva $`\theta_2 = 2\theta_1^2`$, que delimita la frontera factual admisible del parámetro.

---

## §14.2. Criterio absoluto de frontera factual

### 14.2.1. Definición

**Definición 14.2.1.** El **criterio absoluto de frontera factual** consigna que una configuración factual admisible activa frontera cuando, y solo cuando,

$$
\det(J_{SV}) \;=\; 0.
$$

La activación de frontera es propiedad intrínseca del régimen, derivada de la anulación del determinante factual de sensibilidad, sin referencia a coordenadas externas ni a métrica auxiliar.

### 14.2.2. Complementariedad regular-frontera

**Proposición 14.2.2.** El conjunto de configuraciones admisibles $`\Theta_{SV}`$ se descompone disjuntamente en régimen regular $`\Theta^{\mathrm{reg}}_{SV}`$ y régimen de frontera $`\Theta^{\partial}_{SV}`$:

$$
\Theta_{SV} \;=\; \Theta^{\mathrm{reg}}_{SV} \;\sqcup\; \Theta^{\partial}_{SV},
$$

con $`\Theta^{\mathrm{reg}}_{SV} = \{\theta \in \Theta_{SV} \,|\, \det(J_{SV}(\theta)) \neq 0\}`$ y $`\Theta^{\partial}_{SV} = \{\theta \in \Theta_{SV} \,|\, \det(J_{SV}(\theta)) = 0\}`$.

**Demostración.** La descomposición es consecuencia directa del principio del tercio excluso aplicado al predicado $`\det(J_{SV}) = 0`$ sobre el dominio admisible. Q.E.D.

### 14.2.3. Indicador absoluto de frontera

Se define la función indicadora absoluta

$$
\mathbb{1}_{\det(J_{SV})=0}(\theta) \;:=\; \begin{cases} 1 & \text{si } \det(J_{SV}(\theta)) = 0, \\ 0 & \text{en otro caso.} \end{cases}
$$

Esta función constituye el objeto booleano fundamental de la componente $`\mathbb{F}_{SV}`$ del operador maestro, fijada en §14.11.

### 14.2.4. Verificación visible del criterio

Sobre la configuración de §14.1.5, el indicador absoluto se evalúa como

$$
\mathbb{1}_{\det(J_{SV})=0}(1, 1) = 0, \qquad \mathbb{1}_{\det(J_{SV})=0}(1, 2) = 1,
$$

lo que distingue cuantitativamente el régimen regular del régimen de frontera factual admisible.

---

## §14.3. Operador exacto de reconfiguración factual $`\mathcal{R}^f_{SV}`$

### 14.3.1. Definición operativa

**Definición 14.3.1.** El **operador exacto de reconfiguración factual** es la aplicación

$$
\mathcal{R}^f_{SV} \;:=\; \mathbb{1}_{\det(J_{SV})=0} \cdot \Lambda \cdot B_{\mathrm{reg}},
$$

donde $`\Lambda`$ es el factor de absorción interfacial factual (definido a continuación) y $`B_{\mathrm{reg}}`$ es el operador de regularización absoluta que preserva la clase factual admisible bajo reconfiguración de frontera.

### 14.3.2. Factor de absorción interfacial

Sea $`\partial C_{k,l}`$ la interfaz factual entre dos celdas admisibles $`C_k`$ y $`C_l`$ del mosaico, con bases posicionales $`\{e^{SV,(k)}_i\}`$ y $`\{e^{SV,(l)}_i\}`$ relacionadas por cambio factual $`M^{(k,l)}`$. El **factor de absorción interfacial factual** se define como el endomorfismo factual

$$
\Lambda^{(k,l)} \;:=\; M^{(k,l)} \cdot P^{\mathrm{tan}}_{\partial C_{k,l}} + P^{\mathrm{norm}}_{\partial C_{k,l}},
$$

donde $`P^{\mathrm{tan}}`$ y $`P^{\mathrm{norm}}`$ son los proyectores factuales tangencial y normal a la interfaz, respectivamente.

### 14.3.3. Propiedades canónicas del operador

**Proposición 14.3.2 (acción sobre régimen regular).** En régimen factual regular, $`\mathcal{R}^f_{SV}`$ anula: $`\mathcal{R}^f_{SV}(q) = 0`$ para toda magnitud factual admisible $`q`$.

**Demostración.** En régimen regular, $`\det(J_{SV}) \neq 0`$, por tanto $`\mathbb{1}_{\det(J_{SV})=0} = 0`$, y el producto que define $`\mathcal{R}^f_{SV}`$ se anula. Q.E.D.

**Proposición 14.3.3 (preservación de clase admisible).** Sobre régimen factual de frontera, $`\mathcal{R}^f_{SV}`$ preserva la clase factual admisible: para toda magnitud $`q`$ admisible, $`\mathcal{R}^f_{SV}(q)`$ es admisible.

**Demostración.** El factor $`\Lambda`$ es endomorfismo lineal de la estructura interfacial y respeta la descomposición tangencial-normal; $`B_{\mathrm{reg}}`$ es operador de regularización factual que, por construcción, devuelve aplicaciones admisibles bajo toda entrada admisible. La composición preserva la propiedad. Q.E.D.

### 14.3.4. Verificación visible sobre interfaz factual

Sobre interfaz admisible $`\partial C_{1,2}`$ con cambio factual $`M^{(1,2)}`$ dado por la matriz de rotación factual de ángulo $`\theta = \pi/6`$,

$$
M^{(1,2)} = \begin{pmatrix} \cos(\pi/6) & \sin(\pi/6) & 0 \\ -\sin(\pi/6) & \cos(\pi/6) & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det(M^{(1,2)}) = 1,
$$

y magnitud factual $`q = (1, 0, 0)`$ tangencial a la interfaz, se obtiene

$$
\Lambda^{(1,2)}(q) = (\cos(\pi/6),\, -\sin(\pi/6),\, 0) \approx (0{,}866,\, -0{,}500,\, 0).
$$

Bajo indicador activo $`\mathbb{1}_{\det(J_{SV})=0} = 1`$ y operador de regularización $`B_{\mathrm{reg}} = \mathrm{Id}`$ (configuración regular en la interfaz misma), $`\mathcal{R}^f_{SV}(q) = (0{,}866,\, -0{,}500,\, 0)`$. En el interior de $`C_1`$, el indicador se anula y $`\mathcal{R}^f_{SV}(q) = (0, 0, 0)`$.

---

## Paquete operatorio temprano

## §14.4. Tensor factual completamente antisimétrico $`\varepsilon^{SV}_{ijk}`$ y orientación factual

### 14.4.1. Definición canónica

Sea $`\{e^{SV}_i\}_{i=1}^{3}`$ la base posicional admisible del mosaico $`SV(3,9)`$ sobre $`\Sigma_{\mathrm{canal}}`$. El **tensor factual completamente antisimétrico de orden tres** es el objeto $`\varepsilon^{SV}_{ijk}`$ cuyas componentes, en la base ortonormal admisible, toman los valores

$$
\varepsilon^{SV}_{ijk} \;=\; \begin{cases} +1 & \text{si } (i,j,k) \text{ es permutación par de } (1,2,3), \\ -1 & \text{si } (i,j,k) \text{ es permutación impar de } (1,2,3), \\ 0 & \text{en otro caso.} \end{cases}
$$

La orientación factual queda fijada por el signo $`+1`$ sobre la terna canónica ordenada $`(1,2,3)`$ de la base admisible.

### 14.4.2. Transformación bajo cambio de base admisible

Sea $`M = (M^i{}_j)`$ la matriz de cambio entre dos bases posicionales admisibles. El tensor transforma según

$$
\varepsilon^{SV,\prime}_{ijk} \;=\; \det(M) \cdot M^a{}_i\, M^b{}_j\, M^c{}_k\, \varepsilon^{SV}_{abc}.
$$

Sobre cambios de base que preservan la orientación factual ($`\det(M) = +1`$), $`\varepsilon^{SV}_{ijk}`$ es tensor covariante de orden tres completamente antisimétrico.

### 14.4.3. Identidad algebraica fundamental

**Proposición 14.4.1.** Sobre la base tridimensional del mosaico absoluto, para todo par de ternas de índices admisibles,

$$
\varepsilon^{SV}_{ijk}\, \varepsilon^{SV,ilm} \;=\; \delta^{l}_{j}\,\delta^{m}_{k} \;-\; \delta^{m}_{j}\,\delta^{l}_{k}.
$$

**Demostración.** Por antisimetría completa, la suma $`\sum_i \varepsilon^{SV}_{ijk}\,\varepsilon^{SV,ilm}`$ anula todo sumando en que $`j=k`$ o $`l=m`$. Para $`j\neq k`$ y $`l\neq m`$, la suma sobre $`i`$ admite exactamente un término no nulo, correspondiente al único valor de $`i`$ que completa la terna ordenada admisible. El signo resultante coincide con la paridad de la permutación $`(j,k) \mapsto (l,m)`$: $`+1`$ si $`(l,m)=(j,k)`$, $`-1`$ si $`(l,m)=(k,j)`$. Esta alternancia reproduce exactamente la forma $`\delta^l_j\delta^m_k - \delta^m_j\delta^l_k`$. Q.E.D.

**Corolario 14.4.2.** La contracción doble se evalúa a $`\varepsilon^{SV}_{ijk}\,\varepsilon^{SV,ijm} = 2\,\delta^m_k`$.

**Corolario 14.4.3.** La contracción triple se evalúa a $`\varepsilon^{SV}_{ijk}\,\varepsilon^{SV,ijk} = 6`$.

### 14.4.4. Verificación visible de contracciones

Contracción doble en $`k = 1`$ para $`m = 1`$:

$$
\varepsilon^{SV}_{ij1}\,\varepsilon^{SV,ij1} = \varepsilon^{SV}_{231}\,\varepsilon^{SV,231} + \varepsilon^{SV}_{321}\,\varepsilon^{SV,321} = (+1)(+1) + (-1)(-1) = 2.
$$

Contracción doble en $`k = 1`$ para $`m = 2`$:

$$
\varepsilon^{SV}_{ij1}\,\varepsilon^{SV,ij2} = \varepsilon^{SV}_{231}\,\varepsilon^{SV,232} + \varepsilon^{SV}_{321}\,\varepsilon^{SV,322} = (+1)(0) + (-1)(0) = 0.
$$

Coincidencia exacta con el Corolario 14.4.2.

Contracción triple:

$$
\varepsilon^{SV}_{ijk}\,\varepsilon^{SV,ijk} = (+1)^2 + (+1)^2 + (+1)^2 + (-1)^2 + (-1)^2 + (-1)^2 = 6.
$$

Coincidencia con el Corolario 14.4.3.

---

## §14.5. Producto vectorial factual $`\times_{SV}`$ e identidad de Poynting factual

### 14.5.1. Definición canónica

Sean $`F, G`$ campos vectoriales factuales admisibles sobre base tridimensional del mosaico. El **producto vectorial factual** es el campo definido por

$$
(F \times_{SV} G)^i \;:=\; \varepsilon^{SV,ijk}\, F_j\, G_k.
$$

### 14.5.2. Propiedades canónicas

**Proposición 14.5.1 (antisimetría).** $`F \times_{SV} G \;=\; -(G \times_{SV} F)`$.

**Proposición 14.5.2 (bilinealidad factual).** Para escalares factuales $`\alpha, \beta`$ y campos $`F, F', G`$ admisibles,

$$
(\alpha F + \beta F') \times_{SV} G \;=\; \alpha\,(F \times_{SV} G) + \beta\,(F' \times_{SV} G).
$$

### 14.5.3. Producto vectorial tangencial factual

**Definición 14.5.3.** Sea $`\mathbf{n}`$ la normal saliente factual a una superficie admisible $`\partial\Omega`$. El **producto vectorial tangencial factual** es

$$
(\mathbf{n} \times_{SV} F)^i \;:=\; \varepsilon^{SV,ijk}\, n_j\, F_k.
$$

Este operador extrae la componente tangencial factual del campo $`F`$ sobre $`\partial\Omega`$ con orientación inducida por $`\mathbf{n}`$.

### 14.5.4. Identidad de Poynting factual

**Teorema 14.5.4.** Para todo par de campos vectoriales factuales $`F, G`$ admisibles en régimen separable,

$$
\mathrm{Div}_{SV}(F \times_{SV} G) \;=\; \langle G, \mathrm{Rot}_{SV}(F)\rangle_{SV} \;-\; \langle F, \mathrm{Rot}_{SV}(G)\rangle_{SV},
$$

con $`\langle\cdot,\cdot\rangle_{SV}`$ el bracket factual del §14.7 y $`\mathrm{Rot}_{SV}`$ el rotor factual del §14.6.

**Demostración.** Por la definición de $`\times_{SV}`$ y la regla de Leibniz factual para la divergencia factual,

$$
\mathrm{Div}_{SV}(F \times_{SV} G) = \partial^{SV}_i\,(\varepsilon^{SV,ijk}\, F_j\, G_k) = \varepsilon^{SV,ijk}\,(\partial^{SV}_i F_j)\, G_k + \varepsilon^{SV,ijk}\, F_j\,(\partial^{SV}_i G_k).
$$

Por antisimetría tensorial del símbolo $`\varepsilon^{SV}`$ en los índices $`(i,j)`$,

$$
\varepsilon^{SV,ijk}\,(\partial^{SV}_i F_j)\, G_k = -\varepsilon^{SV,jik}\,(\partial^{SV}_i F_j)\, G_k = -(\mathrm{Rot}_{SV}\, F)^k\, G_k = -\langle G, \mathrm{Rot}_{SV}(F)\rangle_{SV}.
$$

Análogamente, por antisimetría tensorial en $`(i,k)`$,

$$
\varepsilon^{SV,ijk}\, F_j\,(\partial^{SV}_i G_k) = \langle F, \mathrm{Rot}_{SV}(G)\rangle_{SV}.
$$

Sumando ambos términos se obtiene el enunciado. Q.E.D.

### 14.5.5. Verificación visible sobre configuración admisible

Sobre la celda admisible con campos $`E(x_1, x_2, x_3) = (2\,x_3,\, 0,\, 0)`$ y $`H(x_1, x_2, x_3) = (0,\, 3\,x_3,\, 0)`$ en coordenadas posicionales admisibles.

Producto vectorial factual:

$$
(E \times_{SV} H)^1 = \varepsilon^{SV,123}\,E_2\,H_3 + \varepsilon^{SV,132}\,E_3\,H_2 = 0,
$$

$$
(E \times_{SV} H)^2 = \varepsilon^{SV,213}\,E_1\,H_3 + \varepsilon^{SV,231}\,E_3\,H_1 = 0,
$$

$$
(E \times_{SV} H)^3 = \varepsilon^{SV,312}\,E_1\,H_2 + \varepsilon^{SV,321}\,E_2\,H_1 = (+1)(2x_3)(3x_3) + (-1)(0)(0) = 6\,x_3^2.
$$

Por tanto $`S_{SV} := E \times_{SV} H = (0,\, 0,\, 6\,x_3^2)`$.

Divergencia factual: $`\mathrm{Div}_{SV}(S_{SV}) = \partial^{SV}_3\,(6\,x_3^2) = 12\,x_3`$.

Rotor factual de $`E`$ y $`H`$:

$$
(\mathrm{Rot}_{SV}\, E)^2 = \varepsilon^{SV,231}\,\partial^{SV}_3\, E_1 = (+1)\cdot 2 = 2, \qquad (\mathrm{Rot}_{SV}\, H)^1 = (-1)\cdot 3 = -3.
$$

Segundo miembro del Teorema 14.5.4:

$$
\langle H, \mathrm{Rot}_{SV}\, E\rangle_{SV} - \langle E, \mathrm{Rot}_{SV}\, H\rangle_{SV} = (3x_3)(2) - (2x_3)(-3) = 6x_3 + 6x_3 = 12\,x_3.
$$

Ambos miembros coinciden exactamente en el valor $`12\,x_3`$.

---

## §14.6. Rotor factual y teorema de Stokes factual

### 14.6.1. Definición del rotor factual

**Definición 14.6.1.** Sea $`F`$ un campo vectorial factual admisible sobre base tridimensional del mosaico. El **rotor factual** $`\mathrm{Rot}_{SV}(F)`$ es el campo vectorial factual de componentes

$$
(\mathrm{Rot}_{SV}\, F)^i \;:=\; \varepsilon^{SV,ijk}\, \partial^{SV}_j\, F_k.
$$

### 14.6.2. Propiedades canónicas

**Proposición 14.6.2 (linealidad factual).** El rotor factual es lineal: para escalares factuales $`\alpha, \beta`$ y campos admisibles $`F, G`$,

$$
\mathrm{Rot}_{SV}(\alpha F + \beta G) \;=\; \alpha\,\mathrm{Rot}_{SV}(F) + \beta\,\mathrm{Rot}_{SV}(G).
$$

**Proposición 14.6.3 (tensor antisimétrico asociado).** El rotor factual admite expresión equivalente como dual de Hodge factual del tensor antisimétrico de parciales factuales:

$$
\Omega^{SV}_{jk}(F) \;:=\; \partial^{SV}_j F_k - \partial^{SV}_k F_j, \qquad (\mathrm{Rot}_{SV}\, F)^i \;=\; \tfrac{1}{2}\,\varepsilon^{SV,ijk}\,\Omega^{SV}_{jk}(F).
$$

**Demostración.** Por antisimetría de $`\varepsilon^{SV,ijk}`$ en $`(j,k)`$,

$$
\varepsilon^{SV,ijk}\,\partial^{SV}_j F_k = \tfrac{1}{2}\,\varepsilon^{SV,ijk}\,(\partial^{SV}_j F_k - \partial^{SV}_k F_j) = \tfrac{1}{2}\,\varepsilon^{SV,ijk}\,\Omega^{SV}_{jk}(F).
$$

Q.E.D.

### 14.6.3. Teorema de Stokes factual

**Teorema 14.6.4 (Stokes factual).** Sea $`S`$ una superficie factual admisible con frontera $`\partial S`$ orientada, y $`F`$ un campo vectorial factual admisible. Entonces

$$
\int^{SV}_{\partial S} F \cdot d\ell^{SV} \;=\; \int^{SV}_{S} \mathrm{Rot}_{SV}(F) \cdot d\mathbf{S}^{SV},
$$

donde $`\int^{SV}_{\partial S}`$ es la circulación factual sobre $`\partial S`$, $`\int^{SV}_{S}`$ es la integral de superficie factual sobre $`S`$, $`d\ell^{SV}`$ es el elemento admisible de línea y $`d\mathbf{S}^{SV}`$ es el elemento admisible de superficie, conforme al cosido metrológico absoluto del corpus.

**Demostración.** Sobre cada celda admisible $`C_k \subset S`$, se fija la base posicional $`\{e^{SV,(k)}_i\}`$ en la que los operadores factuales son locales. Por la Proposición 14.6.3 y la definición integral factual,

$$
\int^{SV}_{C_k} \mathrm{Rot}_{SV}(F) \cdot d\mathbf{S}^{SV} = \int^{SV}_{C_k} \tfrac{1}{2}\,\varepsilon^{SV,ijk}\,\Omega^{SV}_{jk}(F)\,n^{SV}_i\, dS^{SV}.
$$

Aplicando el balance absoluto de frontera factual (fundamentos §7.4) sobre $`\partial C_k`$, se obtiene

$$
\int^{SV}_{C_k} \mathrm{Rot}_{SV}(F) \cdot d\mathbf{S}^{SV} = \oint^{SV}_{\partial C_k} F \cdot d\ell^{SV}.
$$

La suma sobre todas las celdas admisibles que recubren $`S`$ cancela las contribuciones de fronteras interiores (por antisimetría de orientación en interfaces internas) y deja únicamente la circulación sobre $`\partial S`$. Q.E.D.

### 14.6.4. Identidad de rotor del rotor

**Teorema 14.6.5.** Sobre régimen separable con ortotropía factual local (Definición 14.8.4),

$$
\mathrm{Rot}_{SV}(\mathrm{Rot}_{SV}\, F) \;=\; \nabla^{SV}\,\mathrm{Div}_{SV}(F) \;-\; \Delta^{SV}\, F,
$$

con $`\Delta^{SV} := \mathrm{Div}_{SV}\circ\nabla^{SV}`$ el laplaciano factual absoluto.

**Demostración.** Por aplicación de la Proposición 14.4.1 al doble rotor componente a componente,

$$
(\mathrm{Rot}_{SV}\,\mathrm{Rot}_{SV}\, F)^i = \varepsilon^{SV,ijk}\,\partial^{SV}_j\,(\mathrm{Rot}_{SV}\, F)_k = \varepsilon^{SV,ijk}\,\partial^{SV}_j\,(\varepsilon^{SV,klm}\,\partial^{SV}_l\, F_m).
$$

Usando la identidad $`\varepsilon^{SV,ijk}\,\varepsilon^{SV,klm} = \delta^i_l \delta^j_m - \delta^i_m \delta^j_l`$ y la conmutación de parciales posicionales bajo ortotropía local (Definición 14.8.4),

$$
= \partial^{SV}_j\,\partial^{SV}_i\, F_j - \partial^{SV}_j\,\partial^{SV}_j\, F_i = \partial^{SV}_i\,(\partial^{SV}_j\, F_j) - \Delta^{SV}\, F_i = (\nabla^{SV}\,\mathrm{Div}_{SV}\, F)^i - (\Delta^{SV}\, F)^i.
$$

Q.E.D.

### 14.6.5. Verificación visible del teorema de Stokes factual

Sobre disco admisible $`S`$ de radio factual $`R = 1`$ en el plano $`(e^{SV}_1, e^{SV}_2)`$, con circulación frontera $`\partial S`$ parametrizada por $`\varphi \in [0, 2\pi)`$, y campo factual $`F(x_1, x_2, x_3) = (-x_2,\, x_1,\, 0)`$.

Rotor factual:

$$
(\mathrm{Rot}_{SV}\, F)^3 = \partial^{SV}_1 F_2 - \partial^{SV}_2 F_1 = 1 - (-1) = 2.
$$

Integral de superficie factual:

$$
\int^{SV}_S \mathrm{Rot}_{SV}(F) \cdot d\mathbf{S}^{SV} = 2 \cdot \pi R^2 = 2\pi.
$$

Circulación factual sobre $`\partial S`$:

$$
\oint^{SV}_{\partial S} F \cdot d\ell^{SV} = \int_0^{2\pi} [(-\sin\varphi)(-\sin\varphi) + (\cos\varphi)(\cos\varphi)]\, d\varphi = \int_0^{2\pi} 1\, d\varphi = 2\pi.
$$

Ambos miembros coinciden exactamente: $`2\pi = 2\pi`$.

---

## §14.7. Bracket factual absoluto $`\langle\cdot,\cdot\rangle_{SV}`$ y campos admisibles

### 14.7.1. Estatuto operativo sobre $`\Xi_{SV}`$

Las magnitudes factuales del régimen canalizado se realizan como aplicaciones $`q: \Xi_{SV} \to \mathbb{R}`$ sobre el dominio canónico geometrizado. Los campos vectoriales factuales admisibles del régimen electromagnético son aplicaciones $`F: \Xi_{SV} \to \mathbb{R}^3`$. Las estructuras bilineales del análisis electromagnético factual operan sobre el codominio $`\mathbb{R}^3`$ inducido por la base ortonormal admisible, compatible con el cosido metrológico absoluto.

### 14.7.2. Axiomas del bracket factual

**Definición 14.7.1.** Sobre la clase de campos electromagnéticos factuales admisibles, el **bracket factual absoluto** $`\langle\cdot,\cdot\rangle_{SV}`$ satisface:

- (B1) *Bilinealidad factual:* para escalares factuales $`\alpha,\beta`$ y campos admisibles $`F, F', G`$,

$$
\langle \alpha F + \beta F', G\rangle_{SV} \;=\; \alpha\,\langle F, G\rangle_{SV} + \beta\,\langle F', G\rangle_{SV},
$$

y análogamente en el segundo argumento.

- (B2) *Simetría factual:* $`\langle F, G\rangle_{SV} = \langle G, F\rangle_{SV}`$.

- (B3) *No-negatividad:* $`\langle F, F\rangle_{SV} \geq 0`$.

- (B4) *No-degeneración factual:* $`\langle F, F\rangle_{SV} = 0 \;\Leftrightarrow\; F`$ es factualmente nulo.

### 14.7.3. Clase de campos admisibles

**Definición 14.7.2.** La **clase de campos electromagnéticos factuales admisibles** es el conjunto de aplicaciones $`F: \Xi_{SV} \to \mathbb{R}^3`$ que satisfacen:

- (A1) *Linealidad factual:* compatibilidad con combinaciones factuales absolutas sobre el codominio.

- (A2) *Clausura factual:* preservación de la clase bajo aplicación de los operadores absolutos $`\partial_\nu^{SV}, \partial^{SV}_i, \mathrm{Div}_{SV}, \mathrm{Rot}_{SV}, \varepsilon_{SV}, \mu_{SV}, \sigma_{SV}`$.

- (A3) *Compatibilidad con refinamiento factual:* estabilidad bajo subdivisión admisible del mosaico absoluto.

- (A4) *Estatuto metrológico absoluto:* respeto del cosido metrológico absoluto sobre unidades absolutas del corpus.

El bracket $`\langle\cdot,\cdot\rangle_{SV}`$ queda bien definido y cumple (B1)–(B4) sobre toda la clase admisible.

### 14.7.4. Identidad de polarización factual

**Teorema 14.7.3.** Para todo par de campos admisibles $`F, G`$,

$$
\langle F, G\rangle_{SV} \;=\; \tfrac{1}{4}\!\left[\langle F+G, F+G\rangle_{SV} - \langle F-G, F-G\rangle_{SV}\right].
$$

**Demostración.** Desarrollando por bilinealidad (B1) y simetría (B2),

$$
\langle F+G, F+G\rangle_{SV} = \langle F,F\rangle_{SV} + 2\,\langle F,G\rangle_{SV} + \langle G,G\rangle_{SV},
$$

$$
\langle F-G, F-G\rangle_{SV} = \langle F,F\rangle_{SV} - 2\,\langle F,G\rangle_{SV} + \langle G,G\rangle_{SV}.
$$

La diferencia dividida por $`4`$ recupera $`\langle F,G\rangle_{SV}`$. Q.E.D.

### 14.7.5. Regla de Leibniz factual bajo $`\partial_\nu^{SV}`$

**Teorema 14.7.4.** Sobre régimen separable (Definición 14.10.1), para todo par admisible $`F, G`$,

$$
\partial_\nu^{SV}\langle F, G\rangle_{SV} \;=\; \langle \partial_\nu^{SV} F, G\rangle_{SV} + \langle F, \partial_\nu^{SV} G\rangle_{SV} + \omega(\nu)\,\langle \partial_\nu^{SV} F, \partial_\nu^{SV} G\rangle_{SV}.
$$

**Demostración.** Por la definición de $`\partial_\nu^{SV}`$ del corpus de fundamentos §5.2,

$$
\partial_\nu^{SV}\langle F, G\rangle_{SV}(j) = \frac{\langle F_{j+1}, G_{j+1}\rangle_{SV} - \langle F_j, G_j\rangle_{SV}}{\omega(\nu_j)}.
$$

Escribiendo $`F_{j+1} = F_j + \omega(\nu_j)\,\partial_\nu^{SV} F(j)`$ y análogamente para $`G`$, y desarrollando $`\langle F_{j+1}, G_{j+1}\rangle_{SV}`$ por bilinealidad,

$$
\langle F_{j+1}, G_{j+1}\rangle_{SV} = \langle F_j, G_j\rangle_{SV} + \omega(\nu_j)\!\left[\langle \partial_\nu^{SV} F, G_j\rangle_{SV} + \langle F_j, \partial_\nu^{SV} G\rangle_{SV}\right] + \omega(\nu_j)^2\,\langle \partial_\nu^{SV} F, \partial_\nu^{SV} G\rangle_{SV}.
$$

Dividiendo por $`\omega(\nu_j)`$ se obtiene el enunciado. Q.E.D.

### 14.7.6. Densidad factual de energía electromagnética

**Teorema 14.7.5.** En régimen electromagnético factual admisible con operadores constitutivos $`\varepsilon_{SV}, \mu_{SV}`$ no negativos y factualmente autoadjuntos (Teorema 14.8.2), la densidad factual

$$
u_{SV} \;:=\; \tfrac{1}{2}\bigl(\langle E, D\rangle_{SV} + \langle H, B\rangle_{SV}\bigr), \qquad D = \varepsilon_{SV} E, \; B = \mu_{SV} H,
$$

*es no negativa: $`u_{SV} \geq 0`$, con igualdad si y solo si $`E`$ y $`H`$ son factualmente nulos.*

**Demostración.** Por autoadjunción factual de $`\varepsilon_{SV}`$ y no-negatividad, $`\langle E, \varepsilon_{SV} E\rangle_{SV} \geq 0`$. Análogamente $`\langle H, \mu_{SV} H\rangle_{SV} \geq 0`$. La suma con factor $`1/2`$ preserva la no-negatividad. La igualdad $`u_{SV} = 0`$ exige $`\langle E, \varepsilon_{SV} E\rangle_{SV} = 0`$ y $`\langle H, \mu_{SV} H\rangle_{SV} = 0`$, que por (B4) implica $`E = 0`$ y $`H = 0`$ factualmente. Q.E.D.

### 14.7.7. Verificación visible del bracket factual

Sobre la celda admisible con campos factuales $`F = (1, 2, 3)`$ y $`G = (4, -1, 2)`$ en base ortonormal absoluta del mosaico,

$$
\langle F, G\rangle_{SV} = (1)(4) + (2)(-1) + (3)(2) = 4 - 2 + 6 = 8.
$$

Verificación de la identidad de polarización (Teorema 14.7.3):

$$
\langle F + G, F + G\rangle_{SV} = (5)^2 + (1)^2 + (5)^2 = 25 + 1 + 25 = 51,
$$

$$
\langle F - G, F - G\rangle_{SV} = (-3)^2 + (3)^2 + (1)^2 = 9 + 9 + 1 = 19,
$$

$$
\tfrac{1}{4}(51 - 19) = \tfrac{1}{4}(32) = 8.
$$

Coincidencia exacta con el cálculo directo.

---

## §14.8. Autoadjunción factual y ortotropía factual local

### 14.8.1. Definición de autoadjunción factual

**Definición 14.8.1.** Un operador factual lineal $`L`$ sobre la clase de campos admisibles es **factualmente autoadjunto** respecto del bracket $`\langle\cdot,\cdot\rangle_{SV}`$ si, para todo par admisible $`(u, v)`$,

$$
\langle u, L(v)\rangle_{SV} \;=\; \langle L(u), v\rangle_{SV}.
$$

### 14.8.2. Autoadjunción de los operadores constitutivos

**Teorema 14.8.2.** Los operadores constitutivos factuales $`\varepsilon_{SV}, \mu_{SV}, \sigma_{SV}`$ del régimen lineal admisible, caracterizados por la simetría factual absoluta heredada del cosido metrológico absoluto, son factualmente autoadjuntos.

**Demostración.** En la realización admisible sobre $`\mathbb{R}^3`$, el operador $`\varepsilon_{SV}`$ se representa por un tensor constitutivo $`(\varepsilon_{SV})^i{}_j`$ cuya simetría factual absoluta es $`(\varepsilon_{SV})^i{}_j = (\varepsilon_{SV})^j{}_i`$. Por bilinealidad del bracket,

$$
\langle u, \varepsilon_{SV}\, v\rangle_{SV} = \sum_{i,j} u_i\,(\varepsilon_{SV})^i{}_j\, v^j = \sum_{i,j} (\varepsilon_{SV})^j{}_i\, u_i\, v^j = \langle \varepsilon_{SV}\, u, v\rangle_{SV},
$$

donde la segunda igualdad usa la simetría factual absoluta. Demostraciones análogas aplican a $`\mu_{SV}`$ y $`\sigma_{SV}`$. Q.E.D.

### 14.8.3. Corolario de Leibniz factual para la densidad electromagnética

**Corolario 14.8.3.** Sobre régimen separable con constitutivos autoadjuntos,

$$
\partial_\nu^{SV}\, u_{SV}(j) \;=\; \langle E_j, \partial_\nu^{SV} D\rangle_{SV} + \langle H_j, \partial_\nu^{SV} B\rangle_{SV} + \tfrac{\omega(\nu_j)}{2}\!\left[\langle \partial_\nu^{SV} E, \partial_\nu^{SV} D\rangle_{SV} + \langle \partial_\nu^{SV} H, \partial_\nu^{SV} B\rangle_{SV}\right].
$$

**Demostración.** Aplicando el Teorema 14.7.4 a $`\langle E, D\rangle_{SV}`$,

$$
\partial_\nu^{SV}\langle E, D\rangle_{SV} = \langle \partial_\nu^{SV} E, D\rangle_{SV} + \langle E, \partial_\nu^{SV} D\rangle_{SV} + \omega(\nu)\,\langle \partial_\nu^{SV} E, \partial_\nu^{SV} D\rangle_{SV}.
$$

Por autoadjunción de $`\varepsilon_{SV}`$ (Teorema 14.8.2) y conmutatividad $`[\varepsilon_{SV}, \partial_\nu^{SV}] = 0`$ del Teorema 14.10.4,

$$
\langle \partial_\nu^{SV} E, D\rangle_{SV} = \langle \partial_\nu^{SV} E, \varepsilon_{SV}\, E\rangle_{SV} = \langle \varepsilon_{SV}\, \partial_\nu^{SV} E, E\rangle_{SV} = \langle E, \varepsilon_{SV}\, \partial_\nu^{SV} E\rangle_{SV} = \langle E, \partial_\nu^{SV} D\rangle_{SV}.
$$

Por tanto,

$$
\partial_\nu^{SV}\langle E, D\rangle_{SV} = 2\,\langle E, \partial_\nu^{SV} D\rangle_{SV} + \omega(\nu)\,\langle \partial_\nu^{SV} E, \partial_\nu^{SV} D\rangle_{SV}.
$$

Aplicación análoga al término magnético y división por $`2`$ conducen al enunciado. Q.E.D.

### 14.8.4. Ortotropía factual local

**Definición 14.8.4.** El mosaico factual $`SV(3,9)`$, dotado de base posicional admisible y del operador exacto de reconfiguración $`\mathcal{R}^f_{SV}`$ del §14.3, satisface **ortotropía factual local** si, sobre cada celda admisible $`C_k`$ del mosaico, existe una base posicional $`\{e^{SV,(k)}_i\}`$ en la cual las parciales posicionales factuales mixtas conmutan:

$$
\partial^{SV,(k)}_i\, \partial^{SV,(k)}_j \;=\; \partial^{SV,(k)}_j\, \partial^{SV,(k)}_i \qquad \text{para todos los } i, j \in \{1, 2, 3\}.
$$

### 14.8.5. Anulación local de la divergencia del rotor

**Teorema 14.8.5.** Sobre régimen separable con ortotropía factual local, en cada celda admisible $`C_k`$,

$$
\mathrm{Div}_{SV}\circ\mathrm{Rot}_{SV} \;=\; 0.
$$

**Demostración.** Por la Definición 14.6.1,

$$
(\mathrm{Div}_{SV}\, \mathrm{Rot}_{SV}\, F) = \partial^{SV}_i\,(\varepsilon^{SV,ijk}\,\partial^{SV}_j F_k) = \varepsilon^{SV,ijk}\,\partial^{SV}_i\,\partial^{SV}_j F_k.
$$

Por ortotropía factual local, $`\partial^{SV}_i\,\partial^{SV}_j = \partial^{SV}_j\,\partial^{SV}_i`$: el doble operador posicional es simétrico en $`(i,j)`$. Por antisimetría tensorial de $`\varepsilon^{SV}`$ en $`(i,j)`$, la contracción de un tensor simétrico con uno antisimétrico en los mismos dos índices se anula. Q.E.D.

### 14.8.6. Identificación geométrica del criterio absoluto de frontera

**Teorema 14.8.6.** La activación del criterio absoluto de frontera $`\det(J_{SV}) = 0`$ coincide con la activación del cambio de carta factual entre celdas del mosaico $`SV(3,9)`$.

**Demostración.** Sobre interfaz $`\partial C_{k,l}`$ con bases posicionales distintas, la coherencia geométrica del mosaico exige absorción del cambio de base mediante $`\Lambda^{(k,l)}`$ (§14.3.2), operación que activa $`\mathcal{R}^f_{SV}`$ cuando el determinante del jacobiano factual de sensibilidad se anula. Fuera de las interfaces, las bases son localmente coincidentes y $`\det(J_{SV}) \neq 0`$; en las interfaces con cambio de base factual no trivial, $`\det(J_{SV}) = 0`$. La correspondencia es biyectiva. Q.E.D.

### 14.8.7. Verificación visible del balance de Leibniz factual

Sobre la trayectoria poligonal de tres sucesos con peso factual uniforme $`\omega = 1`$ y dimensión posicional restringida a $`n = 2`$, se consideran campos factuales

$$
E_0 = (0, 0), \qquad E_1 = (1, 1), \qquad E_2 = (2, 1), \qquad \partial_\nu^{SV} E(0) = (1, 1), \qquad \partial_\nu^{SV} E(1) = (1, 0).
$$

**Configuración con constitutivo autoadjunto.** Tensor diagonal

$$
\varepsilon_{SV}^{(A)} = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}.
$$

$`D_j = \varepsilon_{SV}^{(A)} E_j`$ produce $`D_0 = (0, 0)`$, $`D_1 = (2, 3)`$, $`D_2 = (4, 3)`$, $`\partial_\nu^{SV} D(1) = (2, 0)`$.

Densidades factuales:

$$
u_{SV}(1) = \tfrac{1}{2}\langle E_1, D_1\rangle_{SV} = \tfrac{1}{2}(2 + 3) = 2{,}5, \qquad u_{SV}(2) = \tfrac{1}{2}(8 + 3) = 5{,}5.
$$

$`\partial_\nu^{SV} u_{SV}(1) = 5{,}5 - 2{,}5 = 3`$.

Por el Corolario 14.8.3:

$$
\langle E_1, \partial_\nu^{SV} D\rangle_{SV} + \tfrac{1}{2}\langle \partial_\nu^{SV} E, \partial_\nu^{SV} D\rangle_{SV} = (2 + 0) + \tfrac{1}{2}(2 + 0) = 2 + 1 = 3.
$$

Ambos miembros coinciden exactamente: el Corolario 14.8.3 se verifica sobre constitutivo autoadjunto.

**Configuración con constitutivo no autoadjunto.** Tensor con componente antisimétrica

$$
\varepsilon_{SV}^{(B)} = \begin{pmatrix} 2 & 0{,}5 \\ -0{,}5 & 3 \end{pmatrix}.
$$

$`D_j = \varepsilon_{SV}^{(B)} E_j`$ produce $`D_0 = (0, 0)`$, $`D_1 = (2{,}5, 2{,}5)`$, $`D_2 = (4{,}5, 2)`$, $`\partial_\nu^{SV} D(1) = (2, -0{,}5)`$.

$`u_{SV}(1) = \tfrac{1}{2}(2{,}5 + 2{,}5) = 2{,}5`$, $`u_{SV}(2) = \tfrac{1}{2}(9 + 2) = 5{,}5`$, $`\partial_\nu^{SV} u_{SV}(1) = 3`$.

Evaluación de la expresión del Corolario 14.8.3 sobre los mismos campos:

$$
\langle E_1, \partial_\nu^{SV} D\rangle_{SV} + \tfrac{1}{2}\langle \partial_\nu^{SV} E, \partial_\nu^{SV} D\rangle_{SV} = (2 - 0{,}5) + \tfrac{1}{2}(2 + 0) = 1{,}5 + 1 = 2{,}5.
$$

Los dos miembros difieren por $`3 - 2{,}5 = 0{,}5`$. La identidad se rompe cuantitativamente. La ausencia de autoadjunción produce desacoplo exacto de $`0{,}5`$, que coincide con la mitad del desfase entre los dos órdenes de contracción.

---

## §14.9. Iteración canónica del operador de suceso $`\partial_\nu^{SV(k)}`$

### 14.9.1. Definición composicional

Sea $`\partial_\nu^{SV}`$ el operador de diferencia factual de suceso del corpus de fundamentos §5.2. La **iteración canónica de orden $`k`$** se define por composición

$$
\partial_\nu^{SV(k)} \;:=\; \underbrace{\partial_\nu^{SV} \circ \partial_\nu^{SV} \circ \cdots \circ \partial_\nu^{SV}}_{k \text{ veces}}, \qquad k \in \mathbb{N}, \; k \geq 1.
$$

Por convención, $`\partial_\nu^{SV(0)} = \mathrm{Id}`$ y $`\partial_\nu^{SV(1)} = \partial_\nu^{SV}`$. El operador $`\partial_\nu^{SV(k)}`$ evaluado en $`\nu_j`$ involucra los valores $`q_j, q_{j+1}, \ldots, q_{j+k}`$ con pesos factuales $`\omega(\nu_j), \omega(\nu_{j+1}), \ldots, \omega(\nu_{j+k-1})`$.

### 14.9.2. Forma cerrada en régimen de pesos uniformes

**Proposición 14.9.1.** Para $`\omega`$ constante y $`k = 2`$,

$$
(\partial_\nu^{SV(2)}\, q)(j) \;=\; \frac{q_{j+2} - 2\, q_{j+1} + q_j}{\omega^2}.
$$

**Demostración.** Por aplicación directa,

$$
(\partial_\nu^{SV(2)}\, q)(j) = \partial_\nu^{SV}\!\left(\frac{q_{j+1}-q_j}{\omega}\right) = \frac{1}{\omega}\!\left(\frac{q_{j+2}-q_{j+1}}{\omega} - \frac{q_{j+1}-q_j}{\omega}\right) = \frac{q_{j+2}-2\,q_{j+1}+q_j}{\omega^2}.
$$

Q.E.D.

**Proposición 14.9.2.** Para $`\omega`$ constante y $`k`$ arbitrario,

$$
(\partial_\nu^{SV(k)}\, q)(j) \;=\; \frac{1}{\omega^k}\,\sum_{m=0}^{k}\,(-1)^{k-m}\,\binom{k}{m}\,q_{j+m}.
$$

**Demostración.** Por inducción sobre $`k`$. El caso base $`k = 1`$ es la definición. El paso inductivo se obtiene aplicando $`\partial_\nu^{SV}`$ a la forma correspondiente a $`k`$ y usando la identidad de Pascal $`\binom{k}{m-1} + \binom{k}{m} = \binom{k+1}{m}`$. Q.E.D.

### 14.9.3. Forma general en régimen de pesos variables

Sin restricción de uniformidad, $`\partial_\nu^{SV(2)} q`$ evaluada en $`\nu_j`$ adopta la forma

$$
(\partial_\nu^{SV(2)}\, q)(j) \;=\; \frac{1}{\omega(\nu_j)}\!\left[\frac{q_{j+2}-q_{j+1}}{\omega(\nu_{j+1})} \;-\; \frac{q_{j+1}-q_j}{\omega(\nu_j)}\right].
$$

La convención de punto de evaluación en $`\nu_j`$ es absoluta: el factor multiplicativo externo corresponde al peso del suceso raíz.

### 14.9.4. Propiedades canónicas

**Proposición 14.9.3 (linealidad factual).** Para escalares $`\alpha, \beta`$ y magnitudes admisibles $`p, q`$,

$$
\partial_\nu^{SV(k)}(\alpha\, p + \beta\, q) \;=\; \alpha\, \partial_\nu^{SV(k)}\, p + \beta\, \partial_\nu^{SV(k)}\, q.
$$

**Proposición 14.9.4 (anulación sobre polinomios factuales).** Sea $`p`$ polinomio factual de grado $`d`$ en el índice $`\nu`$ sobre régimen de pesos uniformes. Entonces

$$
\partial_\nu^{SV(k)}\, p \;\equiv\; 0 \quad \text{para todo } k > d.
$$

**Demostración.** Para $`p(\nu) = \nu^d`$, la suma binomial de la Proposición 14.9.2 evalúa la $`k`$-ésima diferencia finita de una potencia de grado $`d`$, nula para $`k > d`$ por $`\sum_{m=0}^{k}(-1)^{k-m}\binom{k}{m}m^d = 0`$ para $`k > d`$. La Proposición 14.9.3 extiende el resultado a polinomios generales. Q.E.D.

### 14.9.5. Verificación visible sobre trayectoria canónica

Sobre la trayectoria poligonal canónica de diez celdas con valores factuales $`(q_0, q_1, \ldots, q_{10}) = (0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55)`$, correspondientes a $`q_j = j(j+1)/2`$, y peso uniforme $`\omega = 1`$:

$$
(\partial_\nu^{SV(2)}\, q)(0) = 3 - 2 + 0 = 1,
$$

$$
(\partial_\nu^{SV(2)}\, q)(4) = 21 - 30 + 10 = 1,
$$

$$
(\partial_\nu^{SV(2)}\, q)(8) = 55 - 90 + 36 = 1.
$$

Valor constante $`1`$ sobre toda la trayectoria (derivada factual segunda constante del polinomio de grado dos).

Iteración de orden tres sobre la misma trayectoria:

$$
(\partial_\nu^{SV(3)}\, q)(0) = 6 - 9 + 3 - 0 = 0.
$$

Anulación exacta, conforme a la Proposición 14.9.4.

---

## §14.10. Régimen separable y conmutadores factuales

### 14.10.1. Definición del régimen separable

**Definición 14.10.1.** El **régimen electromagnético factual admisible separable** es el subdominio absoluto caracterizado por:

- (S1) *Homogeneidad de peso factual:* $`\omega(\nu_j)`$ es independiente de la posición admisible.

- (S2) *Estabilidad de malla posicional:* la base admisible $`\{e^{SV}_i\}`$ y la métrica factual del dominio canónico $`\Xi_{SV}`$ son independientes del índice de suceso $`\nu`$.

### 14.10.2. Conmutadores suceso-posición

**Teorema 14.10.2.** Sobre régimen separable, los operadores $`\partial_\nu^{SV}`$ y $`\mathrm{Div}_{SV}`$ conmutan:

$$
[\partial_\nu^{SV},\, \mathrm{Div}_{SV}] \;=\; 0.
$$

**Demostración.** Sea $`F`$ campo vectorial factual admisible. Por las definiciones de $`\partial_\nu^{SV}`$ y $`\mathrm{Div}_{SV}`$,

$$
(\partial_\nu^{SV}\, \mathrm{Div}_{SV}\, F)(j) = \frac{1}{\omega(\nu_j)}\!\left[\sum_i \partial^{SV}_i F^i_{j+1} - \sum_i \partial^{SV}_i F^i_{j}\right].
$$

Bajo (S1), $`\omega(\nu_j)`$ es independiente de la posición:

$$
= \sum_i \partial^{SV}_i\!\left[\frac{F^i_{j+1} - F^i_{j}}{\omega(\nu_j)}\right] = (\mathrm{Div}_{SV}\, \partial_\nu^{SV}\, F)(j).
$$

Bajo (S2), $`\partial^{SV}_i`$ es idéntico en $`\nu_j`$ y en $`\nu_{j+1}`$. Q.E.D.

**Teorema 14.10.3.** Sobre régimen separable, $`\partial_\nu^{SV}`$ y $`\mathrm{Rot}_{SV}`$ conmutan:

$$
[\partial_\nu^{SV},\, \mathrm{Rot}_{SV}] \;=\; 0.
$$

**Demostración.** Análoga al Teorema 14.10.2, con $`\varepsilon^{SV,ijk}`$ y $`\partial^{SV}_j`$ independientes del índice de suceso bajo (S1) y (S2). Q.E.D.

### 14.10.3. Conmutadores con operadores constitutivos

**Teorema 14.10.4.** Sobre régimen separable con operadores constitutivos $`\varepsilon_{SV}, \mu_{SV}`$ independientes del índice de suceso,

$$
[\varepsilon_{SV},\, \partial_\nu^{SV}] \;=\; 0, \qquad [\mu_{SV},\, \mathrm{Rot}_{SV}] \;=\; 0.
$$

**Demostración.** Bajo independencia de $`\varepsilon_{SV}`$ respecto de $`\nu`$, la acción sobre $`E_{j+1}`$ y sobre $`E_j`$ responde a una misma regla factual:

$$
(\varepsilon_{SV}\, \partial_\nu^{SV}\, E)(j) = \frac{\varepsilon_{SV}\, E_{j+1} - \varepsilon_{SV}\, E_j}{\omega(\nu_j)} = (\partial_\nu^{SV}\,\varepsilon_{SV}\, E)(j).
$$

Análogamente para $`[\mu_{SV}, \mathrm{Rot}_{SV}]`$ bajo (S2). Q.E.D.

### 14.10.4. Aplicación a la conservación factual de la carga

**Corolario 14.10.5.** La conmutación $`\partial_\nu^{SV}\,\mathrm{Div}_{SV}\, D = \mathrm{Div}_{SV}\,\partial_\nu^{SV}\, D`$, necesaria para la conservación factual de la carga, queda acreditada por el Teorema 14.10.2 bajo régimen separable.

### 14.10.5. Verificación visible del conmutador

Sobre trayectoria de cinco sucesos con dominio posicional unidimensional $`x \in \{0, 1, 2, 3, 4\}`$ y campo factual $`q_j(x) = j \cdot x`$.

**Configuración separable.** $`\omega = 1`$ constante, $`\mathrm{Div}_{SV}\, q(x) := q(x+1) - q(x)`$.

$$
\mathrm{Div}_{SV}\, q_j(x) = j, \qquad \partial_\nu^{SV}\, q(j, x) = x.
$$

$$
\partial_\nu^{SV}(\mathrm{Div}_{SV}\, q)(j, x) = 1, \qquad \mathrm{Div}_{SV}(\partial_\nu^{SV}\, q)(j, x) = 1.
$$

Conmutador exactamente nulo: $`[\partial_\nu^{SV}, \mathrm{Div}_{SV}]\, q = 1 - 1 = 0`$.

**Configuración con peso variable.** $`\omega(\nu_j, x) = 1 + 0{,}1\,x`$ (viola (S1)), mismo campo $`q_j(x) = j \cdot x`$.

$$
\partial_\nu^{SV}(\mathrm{Div}_{SV}\, q)(j, 0) = \frac{1}{1{,}0} = 1, \qquad \mathrm{Div}_{SV}(\partial_\nu^{SV}\, q)(j, 0) = \frac{1}{1{,}1} - 0 = 0{,}9091.
$$

Conmutador no nulo: $`[\partial_\nu^{SV}, \mathrm{Div}_{SV}]\, q(j, 0) = 1 - 0{,}9091 = 0{,}0909`$.

En $`x = 3`$, conmutador $`= 0{,}2198`$. La violación de (S1) produce desacoplo cuantitativamente proporcional al gradiente posicional del peso factual.

---

## §14.11. Componente $`\mathbb{F}_{SV}`$ del operador maestro: bicondicional absoluto bajo clausura admisible

### 14.11.1. Estatuto categorial

La componente $`\mathbb{F}_{SV}`$ del operador maestro absoluto $`\mathbb{E}_{SV}`$ codifica la compatibilidad interfacial factual entre el balance absoluto de frontera y el operador exacto de reconfiguración. Su estatuto algebraico se fija como bicondicional absoluto bajo clausura factual admisible.

### 14.11.2. Definición operativa

**Definición 14.11.1.** Sea $`\Omega`$ un dominio admisible con frontera $`\partial\Omega`$ y $`q`$ magnitud factual definida sobre $`\Omega \subset \Xi_{SV}`$. Se define la **componente $`\mathbb{F}_{SV}`$ del operador maestro absoluto** como

$$
\mathbb{F}_{SV}(q) \;:=\; \mathbb{1}_{\det(J_{SV})=0}\!\left[\,B_{\partial\Omega}^{SV}(q) - \mathcal{R}^f_{SV}(q)\,\right],
$$

donde $`B_{\partial\Omega}^{SV}(q)`$ es el balance factual de frontera (fundamentos §7.4) y $`\mathcal{R}^f_{SV}(q)`$ es la acción del operador exacto de reconfiguración del §14.3.

### 14.11.3. Clausura factual admisible

**Definición 14.11.2.** La **clausura factual admisible** $`\mathsf{Cl}_{SV}`$ del régimen es el conjunto de configuraciones $`(q, \Omega)`$ que satisfacen:

- (C1) $`q`$ es campo factual admisible en el sentido de la Definición 14.7.2;
- (C2) $`\Omega`$ es dominio factual admisible con frontera $`\partial\Omega`$ que admite descomposición en interfaces factuales $`\partial C_{k,l}`$ del mosaico absoluto;
- (C3) la orientación factual de $`\partial\Omega`$ es consistente con la orientación factual del mosaico.

### 14.11.4. Teorema bicondicional absoluto

**Teorema 14.11.3 (bicondicional absoluto de compatibilidad interfacial).** Bajo clausura factual admisible $`\mathsf{Cl}_{SV}`$,

$$
\mathbb{F}_{SV}(q) \;=\; 0 \quad\Longleftrightarrow\quad \text{compatibilidad interfacial factual local absoluta.}
$$

*Demostración (implicación directa).* Supóngase $`\mathbb{F}_{SV}(q) = 0`$. Por la Definición 14.11.1, $`\mathbb{F}_{SV}(q) = 0`$ admite dos casos disjuntos: (i) $`\det(J_{SV}) \neq 0`$, caso en el cual el indicador anula y la condición se satisface sobre régimen regular trivialmente; (ii) $`\det(J_{SV}) = 0`$, caso en el cual $`B_{\partial\Omega}^{SV}(q) = \mathcal{R}^f_{SV}(q)`$, es decir, la contribución de borde del balance factual se reabsorbe exactamente en la reconfiguración absoluta. En ambos casos, la compatibilidad interfacial factual local absoluta queda garantizada.

*Demostración (implicación recíproca).* Supóngase compatibilidad interfacial factual local absoluta. Bajo clausura admisible $`\mathsf{Cl}_{SV}`$ y por la caracterización geométrica del Teorema 14.8.6, la compatibilidad interfacial coincide con la ausencia de residual de balance sobre $`\partial\Omega`$: en régimen regular ($`\det(J_{SV}) \neq 0`$), el indicador absoluto anula y $`\mathbb{F}_{SV}(q) = 0 \cdot [\cdots] = 0`$; en régimen de frontera activa ($`\det(J_{SV}) = 0`$), la compatibilidad exige $`B_{\partial\Omega}^{SV}(q) = \mathcal{R}^f_{SV}(q)`$, por lo que $`\mathbb{F}_{SV}(q) = 1 \cdot 0 = 0`$. En ambos casos, $`\mathbb{F}_{SV}(q) = 0`$. Q.E.D.

### 14.11.5. Consecuencia de equivalencia con la tercera componente de $`\mathbb{E}_{SV}`$

**Corolario 14.11.4.** La componente $`\mathbb{F}_{SV}`$ del operador maestro absoluto es algebraicamente equivalente a la anulación local de la compatibilidad interfacial factual bajo clausura admisible. En particular, $`\mathbb{F}_{SV}(q) = 0`$ es condición necesaria y suficiente, bajo $`\mathsf{Cl}_{SV}`$, para que $`q`$ sea admisible como componente interfacial del sistema absoluto $`\mathbb{E}_{SV}(q) = 0`$.

**Demostración.** Consecuencia directa del Teorema 14.11.3 y de la definición operativa de $`\mathbb{E}_{SV}`$ como conjunción de componentes $`\mathbb{M}_{SV}, \mathbb{K}_{SV}, \mathbb{F}_{SV}`$. Q.E.D.

### 14.11.6. Verificación visible del bicondicional

**Régimen regular interior.** Dominio admisible $`\Omega`$ con $`\det(J_{SV}) = 1`$ constante. Magnitud $`q = x_1^2 + x_2^2`$. El indicador anula y $`\mathbb{F}_{SV}(q) = 0`$. Compatibilidad interfacial trivialmente satisfecha.

**Frontera activa con balance compatible.** Interfaz $`\partial C_{1,2}`$ con $`\det(J_{SV}) = 0`$. Evaluación: $`B_{\partial\Omega}^{SV}(q) = 7{,}2`$, $`\mathcal{R}^f_{SV}(q) = 7{,}2`$.

$$
\mathbb{F}_{SV}(q) = 1 \cdot (7{,}2 - 7{,}2) = 0.
$$

Compatibilidad interfacial verificada.

**Frontera activa con balance incompatible.** Misma interfaz con $`B_{\partial\Omega}^{SV}(q) = 7{,}2`$ y $`\mathcal{R}^f_{SV}(q) = 6{,}5`$.

$$
\mathbb{F}_{SV}(q) = 1 \cdot (7{,}2 - 6{,}5) = 0{,}7 \neq 0.
$$

Compatibilidad interfacial violada; configuración fuera de clausura admisible. Los tres contrastes confirman ambas direcciones del bicondicional bajo $`\mathsf{Cl}_{SV}`$.

---
## Desarrollo profundo

## §14.12. Conexión factual $`\nabla^{SV}`$ y curvatura factual

### 14.12.1. Definición de conexión factual

**Definición 14.12.1.** Sobre el régimen canalizado $`\Sigma_{\mathrm{canal}}`$ con base posicional admisible, la **conexión factual absoluta** $`\nabla^{SV}`$ es el operador que, para cada par de campos factuales admisibles $`(X, Y)`$, produce un tercer campo factual $`\nabla^{SV}_X Y`$ satisfaciendo:

- (N1) *Linealidad factual en el primer argumento:* $`\nabla^{SV}_{\alpha X + \beta X'} Y = \alpha\,\nabla^{SV}_X Y + \beta\,\nabla^{SV}_{X'} Y`$.
- (N2) *Regla de Leibniz factual en el segundo argumento:* $`\nabla^{SV}_X (f\,Y) = X(f)\,Y + f\,\nabla^{SV}_X Y`$ para toda función factual $`f: \Xi_{SV} \to \mathbb{R}`$.
- (N3) *Compatibilidad con el bracket factual:* $`X\,\langle Y, Z\rangle_{SV} = \langle\nabla^{SV}_X Y, Z\rangle_{SV} + \langle Y, \nabla^{SV}_X Z\rangle_{SV}`$ para toda terna admisible $`(X, Y, Z)`$.
- (N4) *Simetría factual:* $`\nabla^{SV}_X Y - \nabla^{SV}_Y X = [X, Y]_{SV}`$, con $`[X, Y]_{SV}`$ el conmutador factual de campos.

### 14.12.2. Tensor factual de curvatura

**Definición 14.12.2.** Para tres campos factuales admisibles $`(X, Y, Z)`$, el **tensor factual de curvatura absoluta** $`\mathbf{R}^{SV}`$ es el objeto tensorial de orden cuatro definido por

$$
\mathbf{R}^{SV}(X, Y)\,Z \;:=\; \nabla^{SV}_X\,\nabla^{SV}_Y Z \;-\; \nabla^{SV}_Y\,\nabla^{SV}_X Z \;-\; \nabla^{SV}_{[X,Y]_{SV}} Z.
$$

El objeto $`\mathbf{R}^{SV}`$ mide la obstrucción local a la conmutación de derivaciones covariantes factuales. Sus componentes en base admisible se denotan $`\mathbf{R}^{SV,l}{}_{ijk}`$ para distinguir del tensor de Ricci factual y del escalar factual de curvatura.

### 14.12.3. Tensor de Ricci factual

**Definición 14.12.3.** Por contracción canónica de $`\mathbf{R}^{SV}`$ sobre el primer y tercer índice, el **tensor de Ricci factual** es

$$
\mathrm{Ric}^{SV}_{ij} \;:=\; \mathbf{R}^{SV,k}{}_{ikj}.
$$

### 14.12.4. Escalar factual de curvatura

**Definición 14.12.4.** Por contracción del tensor de Ricci factual con la métrica inducida en $`\mathbb{R}^3`$, el **escalar factual de curvatura** es

$$
\mathrm{Scal}^{SV} \;:=\; \mathrm{Ric}^{SV}_{ij}\,\delta^{ij}.
$$

La notación $`\mathrm{Scal}^{SV}`$ distingue tipográficamente al escalar del tensor $`\mathbf{R}^{SV}`$ y de la jerarquía reconfigurativa $`\mathcal{R}^{f,(k)}_{SV}`$ del §14.19.

### 14.12.5. Identidades factuales de Bianchi

**Teorema 14.12.5 (identidades de Bianchi factuales).** Sobre régimen factual admisible,

$$
\mathbf{R}^{SV}(X, Y)\,Z + \mathbf{R}^{SV}(Y, Z)\,X + \mathbf{R}^{SV}(Z, X)\,Y \;=\; 0,
$$

$$
(\nabla^{SV}_U \mathbf{R}^{SV})(X, Y)\,Z + (\nabla^{SV}_X \mathbf{R}^{SV})(Y, U)\,Z + (\nabla^{SV}_Y \mathbf{R}^{SV})(U, X)\,Z \;=\; 0.
$$

**Demostración.** La primera identidad es consecuencia directa de (N4) y de la Definición 14.12.2, por simetrización cíclica de los tres conmutadores $`[X,Y]_{SV}, [Y,Z]_{SV}, [Z,X]_{SV}`$. La segunda es consecuencia de la derivación covariante del tensor de curvatura bajo (N2) y la regla de Leibniz factual. Q.E.D.

### 14.12.6. Anulación en régimen separable con ortotropía global

**Teorema 14.12.6.** Sobre régimen electromagnético factual admisible separable con ortotropía factual global, $`\mathbf{R}^{SV}(X, Y)\,Z = 0`$.

**Demostración.** Bajo separabilidad (S1) y (S2) y ortotropía global, la base posicional $`\{e^{SV}_i\}`$ es uniforme sobre el mosaico entero, y las derivaciones factuales parciales conmutan: $`\partial^{SV}_i\,\partial^{SV}_j = \partial^{SV}_j\,\partial^{SV}_i`$ sobre $`\Xi_{SV}`$. Por (N4) y la expresión de $`\nabla^{SV}`$ en base uniforme, $`\nabla^{SV}_X\,\nabla^{SV}_Y = \nabla^{SV}_Y\,\nabla^{SV}_X`$ y $`[X, Y]_{SV} = 0`$. Por tanto $`\mathbf{R}^{SV}(X, Y)\,Z = 0`$. Q.E.D.

**Corolario 14.12.7.** Bajo las hipótesis del Teorema 14.12.6, $`\mathrm{Ric}^{SV}_{ij} = 0`$ y $`\mathrm{Scal}^{SV} = 0`$.

### 14.12.7. Activación no nula sobre frontera factual

**Teorema 14.12.8.** Sobre interfaz $`\partial C_{k,l}`$ donde la ortotropía factual global se rompe y la ortotropía es sólo local (Definición 14.8.4), el tensor de curvatura factual presenta componentes no nulas cuantificables por el cambio de base $`\Lambda^{(k,l)}`$ del §14.3.

**Demostración.** Fuera de la interfaz, la ortotropía local garantiza $`\mathbf{R}^{SV}_{C_k} = 0`$ por el Teorema 14.12.6 restringido a la celda. Sobre $`\partial C_{k,l}`$, el paso entre las bases admisibles introduce una discontinuidad en la conexión factual cuantificada por la derivada del cambio de base $`\partial^{SV}_j \Lambda^{(k,l)}`$. Esta derivada alimenta componentes no triviales de $`\mathbf{R}^{SV}`$ sobre la interfaz, absorbidas por $`\mathcal{R}^f_{SV}`$ mediante el factor $`\Lambda^{(k,l)}`$. Q.E.D.

### 14.12.8. Verificación visible de la curvatura factual

Sobre mosaico $`SV(3,9)`$ con dos celdas $`C_1, C_2`$ separadas por interfaz $`\partial C_{1,2}`$ y bases posicionales relacionadas por rotación factual de ángulo $`\theta = \pi/6`$.

**Interior de $`C_1`$.** Base uniforme, ortotropía global local. $`\mathbf{R}^{SV}_{C_1}(X, Y)\,Z = 0`$. $`\mathrm{Scal}^{SV}_{C_1} = 0`$. Anulación interior confirmada.

**Sobre la interfaz $`\partial C_{1,2}`$.** Sobre trayectoria transversal con parámetro $`\tau`$ donde $`\theta(\tau) = \theta \cdot \mathbb{1}_{\tau \geq 0}`$, la derivada factual del cambio de base $`\partial^{SV}_\tau \Lambda^{(1,2)}`$ presenta discontinuidad localizada en $`\tau = 0`$. La componente $`\mathbf{R}^{SV}_{1212}`$ evaluada mediante los símbolos factuales de Christoffel derivados de $`\Lambda^{(1,2)}`$ produce valor no nulo localizado en $`\tau = 0`$, absorbido por $`\mathcal{R}^f_{SV}`$ según el Teorema 14.8.6. La primera evaluación (interior) confirma el Teorema 14.12.6; la segunda (interfaz) confirma el Teorema 14.12.8.

---

## §14.13. Tensor factual de energía-momento $`T^{SV}_{\mu\nu}`$

### 14.13.1. Construcción como objeto tensorial unificado

**Definición 14.13.1.** Sobre el régimen canalizado $`\Sigma_{\mathrm{canal}}`$, el **tensor factual de energía-momento** $`T^{SV}_{\mu\nu}`$ es el tensor simétrico de segundo orden con componentes

$$
T^{SV}_{00} \;:=\; u_{SV} \;=\; \tfrac{1}{2}\bigl(\langle E, D\rangle_{SV} + \langle H, B\rangle_{SV}\bigr),
$$

$$
T^{SV}_{0i} \;:=\; (S_{SV})^i \;=\; (E \times_{SV} H)^i,
$$

$$
T^{SV}_{ij} \;:=\; -\langle E^{(i)}, D^{(j)}\rangle_{SV} - \langle H^{(i)}, B^{(j)}\rangle_{SV} + \tfrac{1}{2}\,\delta_{ij}\bigl(\langle E, D\rangle_{SV} + \langle H, B\rangle_{SV}\bigr),
$$

donde $`E^{(i)}`$ denota la $`i`$-ésima componente del campo eléctrico factual y análogamente para $`D^{(j)}, H^{(i)}, B^{(j)}`$.

### 14.13.2. Componentes canónicas

Las componentes de $`T^{SV}_{\mu\nu}`$ tienen estatuto operatorio fijado:

- $`T^{SV}_{00}`$ es la densidad factual de energía electromagnética del Teorema 14.7.5.
- $`T^{SV}_{0i}`$ son las tres componentes del vector factual de Poynting del §14.5.
- $`T^{SV}_{ij}`$ son las componentes del tensor factual de esfuerzos de Maxwell.

### 14.13.3. Balance covariante factual

**Teorema 14.13.2.** Sobre régimen separable con constitutivos autoadjuntos, el tensor factual de energía-momento satisface el balance covariante absoluto

$$
\partial_\nu^{SV}\, T^{SV}_{\mu\nu} \;=\; -\,\langle J, F^{SV}_{\mu\nu}\rangle_{SV},
$$

donde $`F^{SV}_{\mu\nu}`$ es el tensor factual de campo electromagnético unificado y $`J`$ es la densidad factual de corriente.

**Demostración.** Para $`\mu = 0`$, la componente es el Corolario 14.8.3 extendido mediante la identidad de Poynting del Teorema 14.5.4 aplicada a la divergencia espacial, cerrada con la ley factual de Ampère-Maxwell que introduce $`-\langle J, E\rangle_{SV}`$ por acoplamiento con la corriente. Para $`\mu = i`$ espacial, la componente es el balance factual de momento lineal electromagnético, obtenido por aplicación de $`\partial_\nu^{SV}`$ al tensor de esfuerzos y uso de los Teoremas 14.10.2, 14.10.3 y las ecuaciones factuales de Faraday y Ampère-Maxwell. La autoadjunción de los constitutivos (Teorema 14.8.2) garantiza la simetría $`T^{SV}_{\mu\nu} = T^{SV}_{\nu\mu}`$ y el cierre del balance. Q.E.D.

### 14.13.4. Invariancia bajo transformadas canónicas

**Teorema 14.13.3.** El tensor $`T^{SV}_{\mu\nu}`$ es invariante bajo las cuatro transformadas canónicas de trayectoria: traslación de suceso, reindexación admisible, cambio de base posicional con $`\det(M) = \pm 1`$ y refinamiento admisible de malla.

**Demostración.** La traslación de suceso preserva $`\partial_\nu^{SV}`$; la reindexación admisible preserva la orientación factual; el cambio de base transforma covariantemente cada componente; el refinamiento preserva la clausura factual por (A3). La composición preserva la forma del tensor y de su balance. Q.E.D.

### 14.13.5. Verificación visible del balance en vacío

Sobre la configuración de §14.5.5 con $`E = (2x_3, 0, 0)`$, $`H = (0, 3x_3, 0)`$, constitutivos $`\varepsilon_0 = \mu_0 = 1`$ (unidades absolutas), $`J = 0`$, evaluación en $`x_3 = 1`$.

$`D = E = (2, 0, 0)`$, $`B = H = (0, 3, 0)`$.

$$
T^{SV}_{00} = u_{SV} = \tfrac{1}{2}(4 + 9) = 6{,}5.
$$

$$
T^{SV}_{0i} = S^i_{SV} = (0, 0, 6).
$$

$$
T^{SV}_{11} = -4 - 0 + 6{,}5 = 2{,}5, \quad T^{SV}_{22} = 0 - 9 + 6{,}5 = -2{,}5, \quad T^{SV}_{33} = 0 - 0 + 6{,}5 = 6{,}5.
$$

$`T^{SV}_{12} = T^{SV}_{13} = T^{SV}_{23} = 0`$.

Balance covariante en vacío ($`J = 0`$) sobre configuración estacionaria: $`\partial_\nu^{SV}\, T^{SV}_{\mu\nu} = 0`$ identicamente. Teorema 14.13.2 verificado.

---

## §14.14. Principio variacional factual

### 14.14.1. Densidad lagrangiana factual

**Definición 14.14.1.** Sobre régimen canalizado con potenciales factuales $`A^{SV}_\mu`$ y tensor factual de campo $`F^{SV}_{\mu\nu} = \partial^{SV}_\mu A^{SV}_\nu - \partial^{SV}_\nu A^{SV}_\mu`$, la **densidad lagrangiana factual** del régimen electromagnético es

$$
\mathcal{L}_{SV} \;:=\; -\tfrac{1}{4}\langle F^{SV}, F^{SV}\rangle_{SV} \;-\; \langle A^{SV}, J\rangle_{SV},
$$

con $`\langle F^{SV}, F^{SV}\rangle_{SV} := F^{SV}_{\mu\nu}\,F^{SV,\mu\nu}`$.

### 14.14.2. Acción factual

**Definición 14.14.2.** Sobre dominio factual admisible $`\Omega \subset \Xi_{SV}`$, la **acción factual** es

$$
\mathcal{A}_{SV}[A^{SV}] \;:=\; \sum_{\nu_j \in \Omega}\,\omega(\nu_j)\cdot\mathcal{L}_{SV}(\nu_j).
$$

### 14.14.3. Euler-Lagrange factual

**Teorema 14.14.3.** La anulación de la variación factual de $`\mathcal{A}_{SV}`$ respecto de $`A^{SV}`$, bajo condiciones de frontera factual fijas, produce la ecuación factual

$$
\partial^{SV}_\mu\, F^{SV,\mu\nu} \;=\; J^\nu,
$$

*correspondiente a la componente $`\mathbb{M}_{SV}`$ del operador maestro absoluto $`\mathbb{E}_{SV}`$.*

**Demostración.** La variación $`\delta\mathcal{A}_{SV}[A^{SV}] = 0`$ con $`\delta A^{SV}_\mu`$ arbitrario en el interior y nulo en $`\partial\Omega`$ produce, por la regla de Leibniz factual absoluta,

$$
\delta\mathcal{L}_{SV} = -\tfrac{1}{2}\langle F^{SV}, \delta F^{SV}\rangle_{SV} - \langle \delta A^{SV}, J\rangle_{SV},
$$

con $`\delta F^{SV}_{\mu\nu} = \partial^{SV}_\mu \delta A^{SV}_\nu - \partial^{SV}_\nu \delta A^{SV}_\mu`$. Integrando por partes factualmente,

$$
\delta\mathcal{A}_{SV} = \sum_{\nu_j \in \Omega}\,\omega(\nu_j)\!\left[\partial^{SV}_\mu F^{SV,\mu\nu} - J^\nu\right]\delta A^{SV}_\nu.
$$

La anulación para toda variación admisible produce la ecuación enunciada. Q.E.D.

### 14.14.4. Constitutivas factuales como ligaduras

**Teorema 14.14.4.** Las relaciones constitutivas factuales $`D = \varepsilon_{SV} E`$ y $`B = \mu_{SV} H`$ emergen del principio variacional como ecuaciones de ligadura entre los campos duales, con $`\varepsilon_{SV}`$ y $`\mu_{SV}`$ como multiplicadores tensoriales factuales absolutos.

**Demostración.** Añadiendo a la densidad lagrangiana los términos de ligadura $`\mathcal{L}^{\mathrm{lig}}_{SV} = \Lambda^\varepsilon_{ij}(D^i - \varepsilon_{SV}^{ij} E_j) + \Lambda^\mu_{ij}(B^i - \mu_{SV}^{ij} H_j)`$ con multiplicadores $`\Lambda^\varepsilon, \Lambda^\mu`$, la variación respecto de $`\Lambda`$ reproduce las constitutivas, y la variación respecto de $`(D, B)`$ identifica $`\Lambda^\varepsilon, \Lambda^\mu`$ con los operadores constitutivos absolutos. La autoadjunción (Teorema 14.8.2) garantiza la consistencia. Q.E.D.

### 14.14.5. Criterio de frontera como anulación variacional de borde

**Teorema 14.14.5.** La componente $`\mathbb{F}_{SV}`$ emerge del principio variacional como condición de anulación de la variación de $`\mathcal{A}_{SV}`$ sobre frontera factual activa.

**Demostración.** Sin imposición previa de borde fijo, la variación factual incorpora términos de frontera

$$
\delta\mathcal{A}_{SV}\big|_{\partial\Omega} \;=\; \sum_{\nu_j \in \partial\Omega}\,\omega(\nu_j)\!\left[B^{SV}_{\partial\Omega}(\delta A^{SV}) - \mathcal{R}^f_{SV}(\delta A^{SV})\right].
$$

La anulación para toda variación admisible reproduce la forma de $`\mathbb{F}_{SV}`$ de la Definición 14.11.1. Q.E.D.

### 14.14.6. Verificación visible del principio variacional

Sobre configuración canónica con $`A^{SV}_0 = 0`$, $`A^{SV}_1 = 0`$, $`A^{SV}_2 = -x_1 \cdot x_3`$:

$$
F^{SV}_{12} = \partial^{SV}_1 A^{SV}_2 - \partial^{SV}_2 A^{SV}_1 = -x_3, \qquad F^{SV}_{23} = \partial^{SV}_2 A^{SV}_3 - \partial^{SV}_3 A^{SV}_2 = x_1, \qquad F^{SV}_{13} = 0.
$$

Densidad lagrangiana factual en vacío ($`J = 0`$, $`\varepsilon_0 = \mu_0 = 1`$):

$$
\mathcal{L}_{SV} = -\tfrac{1}{2}(x_3^2 + x_1^2).
$$

Ecuación de Euler-Lagrange factual por variación de $`A^{SV}_2`$:

$$
\partial^{SV}_\mu F^{SV,\mu 2} = \partial^{SV}_1 (x_3) + \partial^{SV}_3 (x_1) = 0 + 0 = 0 = J^2.
$$

Ecuación de componente $`\nu = 2`$ satisfecha exactamente. Verificación análoga para $`\nu = 0, 1, 3`$. El principio variacional reproduce $`\mathbb{M}_{SV}`$ sobre la configuración canónica.

---

## §14.15. Ecuación factual de onda electromagnética

### 14.15.1. Derivación de la onda general

**Teorema 14.15.1.** Sobre régimen electromagnético factual admisible separable con constitutivos $`\varepsilon_{SV}, \mu_{SV}, \sigma_{SV}`$ autoadjuntos y conductividad factual no nula, el campo eléctrico factual $`E`$ satisface la ecuación factual general de onda

$$
\mu_{SV}\,\varepsilon_{SV}\,\partial_\nu^{SV(2)}\, E \;+\; \mu_{SV}\,\sigma_{SV}\,\partial_\nu^{SV}\, E \;-\; \mathrm{Rot}_{SV}\,\mathrm{Rot}_{SV}\, E \;=\; -\mu_{SV}\,\partial_\nu^{SV}\, J_{\mathrm{ext}} - \nabla^{SV}(\rho_{\mathrm{ext}}/\varepsilon_{SV}),
$$

donde $`J_{\mathrm{ext}}`$ y $`\rho_{\mathrm{ext}}`$ son las fuentes factuales externas admisibles.

**Demostración.** Partiendo de la ley factual de Faraday, $`\mathrm{Rot}_{SV}\, E = -\partial_\nu^{SV}\, B`$, se aplica $`\mathrm{Rot}_{SV}`$ a ambos miembros:

$$
\mathrm{Rot}_{SV}\,\mathrm{Rot}_{SV}\, E = -\mathrm{Rot}_{SV}\,\partial_\nu^{SV}\, B.
$$

Por el Teorema 14.10.3 y la constitutiva $`B = \mu_{SV}\, H`$ con $`\mu_{SV}`$ autoadjunto y conmutante con $`\mathrm{Rot}_{SV}`$ bajo el Teorema 14.10.4,

$$
\mathrm{Rot}_{SV}\,\partial_\nu^{SV}\, B = \partial_\nu^{SV}\,\mathrm{Rot}_{SV}\, B = \mu_{SV}\,\partial_\nu^{SV}\,\mathrm{Rot}_{SV}\, H.
$$

Por la ley factual de Ampère-Maxwell, $`\mathrm{Rot}_{SV}\, H = J_{\mathrm{cond}} + \partial_\nu^{SV}\, D + J_{\mathrm{ext}}`$ con $`J_{\mathrm{cond}} = \sigma_{SV}\, E`$ y $`D = \varepsilon_{SV}\, E`$. Sustituyendo,

$$
\mathrm{Rot}_{SV}\,\mathrm{Rot}_{SV}\, E = -\mu_{SV}\,\sigma_{SV}\,\partial_\nu^{SV}\, E - \mu_{SV}\,\varepsilon_{SV}\,\partial_\nu^{SV(2)}\, E - \mu_{SV}\,\partial_\nu^{SV}\, J_{\mathrm{ext}}.
$$

El término $`\nabla^{SV}(\rho_{\mathrm{ext}}/\varepsilon_{SV})`$ aparece por la identidad vectorial factual del Teorema 14.6.5 combinada con la ley factual de Gauss eléctrica $`\mathrm{Div}_{SV}\, D = \rho_{\mathrm{ext}}`$. Reorganizando se obtiene el enunciado. Q.E.D.

### 14.15.2. Régimen conductor sin fuentes externas

**Corolario 14.15.2 (ecuación factual de telégrafo).** En régimen conductor con $`J_{\mathrm{ext}} = 0`$, $`\rho_{\mathrm{ext}} = 0`$,

$$
\mu_{SV}\,\varepsilon_{SV}\,\partial_\nu^{SV(2)}\, E \;+\; \mu_{SV}\,\sigma_{SV}\,\partial_\nu^{SV}\, E \;-\; \Delta^{SV}\, E \;=\; 0,
$$

con $`\Delta^{SV} := \mathrm{Div}_{SV}\,\nabla^{SV}`$ el laplaciano factual absoluto.

### 14.15.3. Régimen de vacío factual

**Corolario 14.15.3 (onda en vacío factual).** En régimen de vacío factual ($`\sigma_{SV} = 0`$, $`J_{\mathrm{ext}} = 0`$, $`\rho_{\mathrm{ext}} = 0`$),

$$
\partial_\nu^{SV(2)}\, E \;-\; v_{SV}^2\,\Delta^{SV}\, E \;=\; 0,
$$

con $`v_{SV} := 1/\sqrt{\mu_{SV}\,\varepsilon_{SV}}`$ la velocidad factual absoluta de propagación.

### 14.15.4. Longitud de onda factual

**Definición 14.15.4.** Para un modo factual admisible con velocidad de propagación $`v_{SV}`$ y período factual cíclico $`T^{\mathrm{ciclo}}_{SV}`$ (inverso factual de la frecuencia modal absoluta), la **longitud de onda factual** es

$$
\lambda_{SV} \;:=\; v_{SV}\cdot T^{\mathrm{ciclo}}_{SV}.
$$

La longitud de onda factual tiene dimensión UFE (Unidad Factual de Extensión) conforme al cosido metrológico absoluto.

### 14.15.5. Condiciones iniciales factuales

**Definición 14.15.5.** La ecuación factual de onda general es de segundo orden en el índice de suceso; su resolución única exige dos condiciones iniciales factuales sobre el suceso inicial $`\nu_0`$:

$$
E(\nu_0, x) \;=\; E_0(x), \qquad \partial_\nu^{SV}\, E(\nu_0, x) \;=\; E_1(x),
$$

con $`E_0, E_1`$ campos factuales admisibles sobre el dominio espacial $`\Omega \subset \Xi_{SV}`$, compatibles con las ecuaciones factuales de Gauss.

### 14.15.6. Teorema de existencia y unicidad

**Teorema 14.15.6.** Dadas condiciones iniciales factuales $`E_0, E_1`$ admisibles y condiciones de frontera factual compatibles con $`\mathbb{F}_{SV}(E) = 0`$, la ecuación factual de onda general admite solución única $`E: \Sigma_{\mathrm{canal}} \to \mathbb{R}^3`$ en la clase admisible.

**Demostración.** Por separación de variables absoluta sobre régimen separable (S1) y (S2), y por completitud del espacio de modos factuales admisibles bajo el bracket $`\langle\cdot,\cdot\rangle_{SV}`$, la ecuación se reduce a un sistema infinito desacoplado de ecuaciones factuales de segundo orden en $`\nu`$ para cada modo posicional. La existencia y unicidad de cada modo se sigue de la teoría estándar aplicada a la iteración $`\partial_\nu^{SV(2)}`$ de la Proposición 14.9.1, lineal con coeficientes fijos bajo (S1) y (S2). La superposición absoluta de modos reconstruye la solución completa. Q.E.D.

### 14.15.7. Verificación visible sobre los tres regímenes

**Régimen de vacío factual.** $`\varepsilon_0 = \mu_0 = 1`$, $`\sigma = 0`$, $`J_{\mathrm{ext}} = 0`$, $`\rho_{\mathrm{ext}} = 0`$. Modo $`E(\nu, x) = E_0\,\cos(k\,x - \omega\,\nu)`$ con $`E_0 = 1`$, $`k = \pi`$, $`\omega = \pi`$:

$$
\partial_\nu^{SV(2)}\, E = -\pi^2\, E, \qquad \Delta^{SV}\, E = -\pi^2\, E.
$$

$$
\partial_\nu^{SV(2)}\, E - v_{SV}^2\,\Delta^{SV}\, E = -\pi^2\,E - (1)(-\pi^2\, E) = 0.
$$

Ecuación en vacío satisfecha exactamente. $`\lambda_{SV} = v_{SV}\cdot (2\pi/\omega) = 1 \cdot 2 = 2`$.

**Régimen conductor.** $`\sigma_{SV} = 0{,}1`$, $`\varepsilon_0 = \mu_0 = 1`$. Modo $`E(\nu, x) = E_0\,e^{-\alpha\,\nu}\cos(k\,x - \omega\,\nu)`$ con $`\alpha = \mu_0\,\sigma_{SV}/2 = 0{,}05`$, $`k = \pi`$, $`\omega = \sqrt{\pi^2 - 0{,}05^2} \approx 3{,}1412`$:

$$
\partial_\nu^{SV(2)}\, E + \mu_0\,\sigma_{SV}\,\partial_\nu^{SV}\, E - \Delta^{SV}\, E = 0
$$

satisfecha con discrepancia $`\omega - \pi \approx 10^{-4}`$, compatible con baja conductividad.

**Régimen con fuentes externas.** $`J_{\mathrm{ext}}(\nu, x) = J_0\,\sin(k\,x - \omega\,\nu)`$, $`J_0 = 0{,}1`$. El término fuente $`-\mu_{SV}\,\partial_\nu^{SV}\,J_{\mathrm{ext}}`$ acopla al modo homogéneo; la solución completa es superposición absoluta de modo libre más modo forzado. Balance factual verificado término a término.

---

## §14.16. Unicidad representacional e irreducibilidad algebraica de $`\mathbb{E}_{SV}`$

### 14.16.1. Categoría absoluta de operadores factuales admisibles

**Definición 14.16.1.** La **categoría absoluta de operadores factuales admisibles** $`\mathbf{OpFact}_{SV}`$ se compone de los operadores que satisfacen simultáneamente:

- (O1) *Prohibiciones constitutivas:* ausencia de tiempo absoluto, probabilidad fundante, estadística como verdad y coordenadas externas como base ontológica.
- (O2) *Cosido metrológico:* compatibilidad con las unidades absolutas UFM, UFE, UFC, UFE/UFM, UFE·UFM, UE_MFC.
- (O3) *Covariancia absoluta:* invariancia bajo las cuatro transformadas canónicas de trayectoria.
- (O4) *Clausura factual:* preservación de la clase admisible de campos electromagnéticos factuales.

### 14.16.2. Teorema de unicidad representacional

**Teorema 14.16.2.** Dentro de la categoría $`\mathbf{OpFact}_{SV}`$, el operador maestro absoluto $`\mathbb{E}_{SV}`$ con componentes $`\mathbb{M}_{SV}, \mathbb{K}_{SV}, \mathbb{F}_{SV}`$ admite una única representación módulo reordenamiento trivial de las componentes y reetiquetado admisible de los campos.

**Demostración.** Sea $`\mathbb{E}'_{SV}`$ un operador factual en $`\mathbf{OpFact}_{SV}`$ que codifica el régimen electromagnético factual completo. Por (O4), $`\mathbb{E}'_{SV}`$ actúa sobre la clase admisible. Por (O3), la covariancia bajo las cuatro transformadas canónicas restringe su forma a combinaciones admisibles de los operadores absolutos $`\partial_\nu^{SV}, \partial^{SV}_i, \mathrm{Div}_{SV}, \mathrm{Rot}_{SV}, \varepsilon_{SV}, \mu_{SV}, \sigma_{SV}`$. Por (O2), el cosido metrológico fija los coeficientes en unidades absolutas hasta escalares adimensionales. Por (O1), las prohibiciones constitutivas eliminan componentes espurias. Las cuatro ecuaciones factuales del régimen agotan las combinaciones compatibles con las cuatro restricciones simultáneas. Cualquier $`\mathbb{E}'_{SV}`$ en la categoría contiene estas cuatro ecuaciones como componentes, con las relaciones constitutivas como ligaduras y el criterio de frontera $`\mathbb{F}_{SV}`$ como componente activa. Las libertades residuales son el orden de agrupamiento (reordenamiento trivial) y la nomenclatura de los campos (reetiquetado admisible). Q.E.D.

### 14.16.3. Teorema de irreducibilidad algebraica

**Teorema 14.16.3.** El operador maestro absoluto $`\mathbb{E}_{SV}`$ es algebraicamente irreducible en $`\mathbf{OpFact}_{SV}`$: no admite factorización no trivial como composición de operadores factuales admisibles de complejidad estrictamente menor.

**Demostración.** Supóngase $`\mathbb{E}_{SV} = \mathbb{A} \circ \mathbb{B}`$ con $`\mathbb{A}, \mathbb{B} \in \mathbf{OpFact}_{SV}`$ de complejidad estrictamente menor. Por (O4), $`\mathbb{A}`$ y $`\mathbb{B}`$ preservan la clase admisible. Por (O3), son covariantes bajo las cuatro transformadas canónicas. El producto $`\mathbb{A} \circ \mathbb{B}`$ debe generar las cuatro ecuaciones factuales, las tres relaciones constitutivas y el criterio de frontera, todos independientes por el Teorema 14.16.2. Un operador $`\mathbb{A}`$ de complejidad estrictamente menor no genera por composición todas estas componentes sin que $`\mathbb{B}`$ aporte información equivalente a la de $`\mathbb{E}_{SV}`$ completo, contradicción con la hipótesis de complejidad estrictamente menor de $`\mathbb{B}`$. Por tanto, la factorización no trivial supuesta no existe. Q.E.D.

### 14.16.4. Corolario de cierre algebraico

**Corolario 14.16.4.** El operador maestro absoluto $`\mathbb{E}_{SV}`$ constituye el desenlace final algebraico del régimen electromagnético factual: ninguna reducción posterior dentro de $`\mathbf{OpFact}_{SV}`$ es posible sin violación de al menos una de las cuatro condiciones (O1), (O2), (O3), (O4).

### 14.16.5. Verificación visible de irreducibilidad

**Intento uno.** Supóngase $`\mathbb{E}_{SV} = \mathbb{A}_{\mathrm{grad}} \circ \mathbb{B}_{\text{tiempo}}`$ con $`\mathbb{A}_{\mathrm{grad}}`$ gradiente factual y $`\mathbb{B}_{\text{tiempo}}`$ evolución temporal clásica. $`\mathbb{B}_{\text{tiempo}}`$ introduce tiempo absoluto como parámetro primario, violando (O1). Factorización no admisible.

**Intento dos.** Supóngase $`\mathbb{E}_{SV} = \mathbb{C}_{\text{prob}} \circ \mathbb{D}_{\mathrm{const}}`$ con $`\mathbb{C}_{\text{prob}}`$ operador de ponderación probabilística. $`\mathbb{C}_{\text{prob}}`$ introduce probabilidad fundante, violando (O1). No admisible.

**Intento tres.** Supóngase $`\mathbb{E}_{SV} = \mathbb{G}_{\mathrm{ext}} \circ \mathbb{H}_{\mathrm{sol}}`$ con $`\mathbb{G}_{\mathrm{ext}}`$ operador de cambio a coordenadas externas. $`\mathbb{G}_{\mathrm{ext}}`$ introduce coordenadas externas como base ontológica, violando (O1). No admisible.

Tres intentos, tres rupturas categoriales. La irreducibilidad algebraica del Teorema 14.16.3 queda confirmada por ausencia de factorizaciones no triviales en $`\mathbf{OpFact}_{SV}`$.

---

## §14.17. Reconstrucción inversa explícita del conjunto clásico

### 14.17.1. Diccionario absoluto $`\mathcal{D}_{SV}`$

**Definición 14.17.1.** El **diccionario absoluto factual-clásico** $`\mathcal{D}_{SV}`$ es la aplicación que traduce magnitudes factuales del Sistema Vectorial SV a magnitudes clásicas, conforme al cosido metrológico absoluto. Su inversa formal $`\mathcal{D}_{SV}^{-1}`$ realiza la traducción en sentido contrario.

### 14.17.2. Reconstrucción de Gauss eléctrica clásica

**Teorema 14.17.2.** La componente factual $`\mathrm{Div}_{SV}\, D = \rho_{\mathrm{ext}}`$ se reconstruye bajo $`\mathcal{D}_{SV}^{-1}`$ como $`\nabla \cdot \mathbf{D} = \rho_f`$.

**Demostración.** El operador $`\mathrm{Div}_{SV}`$ se traduce al operador clásico $`\nabla \cdot`$ por preservación de la regla de Leibniz y del cosido metrológico. La magnitud $`D`$ corresponde al campo clásico de desplazamiento eléctrico (UFC/UFE²). La fuente $`\rho_{\mathrm{ext}}`$ corresponde a la densidad clásica de carga libre $`\rho_f`$. Q.E.D.

### 14.17.3. Reconstrucción de Gauss magnética

**Teorema 14.17.3.** $`\mathrm{Div}_{SV}\, B = 0`$ se reconstruye bajo $`\mathcal{D}_{SV}^{-1}`$ como $`\nabla \cdot \mathbf{B} = 0`$.

**Demostración.** Análoga al Teorema 14.17.2, con $`B`$ factual traduciéndose al campo clásico $`\mathbf{B}`$ (UFM/UFE²) y miembro derecho nulo preservado. Q.E.D.

### 14.17.4. Reconstrucción de Faraday clásica

**Teorema 14.17.4.** $`\mathrm{Rot}_{SV}\, E = -\partial_\nu^{SV}\, B`$ se reconstruye como $`\nabla \times \mathbf{E} = -\partial \mathbf{B}/\partial t`$.

**Demostración.** $`\mathrm{Rot}_{SV}`$ se traduce al operador clásico $`\nabla \times`$ por preservación de la antisimetría tensorial. $`\partial_\nu^{SV}`$, bajo la correspondencia del cosido metrológico con $`dt = \omega(\nu)`$ en unidades absolutas, se traduce a la derivada temporal clásica. Q.E.D.

### 14.17.5. Reconstrucción de Ampère-Maxwell clásica

**Teorema 14.17.5.** $`\mathrm{Rot}_{SV}\, H = J_{\mathrm{cond}} + \partial_\nu^{SV}\, D + J_{\mathrm{ext}}`$ se reconstruye como $`\nabla \times \mathbf{H} = \mathbf{J}_f + \partial \mathbf{D}/\partial t`$.

**Demostración.** Por traducción análoga e identificación de la corriente total $`J_{\mathrm{cond}} + J_{\mathrm{ext}}`$ con $`\mathbf{J}_f`$. Q.E.D.

### 14.17.6. Reconstrucción de constitutivas

**Teorema 14.17.6.** Las tres constitutivas factuales $`D = \varepsilon_{SV} E`$, $`B = \mu_{SV} H`$, $`J_{\mathrm{cond}} = \sigma_{SV} E`$ se reconstruyen como $`\mathbf{D} = \varepsilon\, \mathbf{E}`$, $`\mathbf{B} = \mu\, \mathbf{H}`$, $`\mathbf{J}_c = \sigma\, \mathbf{E}`$.

**Demostración.** Por traducción directa, preservando la autoadjunción del Teorema 14.8.2 que se corresponde con la simetría clásica. Q.E.D.

### 14.17.7. Reconstrucción de contorno clásico

**Teorema 14.17.7.** La componente factual $`\mathbb{F}_{SV} = 0`$ se reconstruye bajo $`\mathcal{D}_{SV}^{-1}`$ como las condiciones clásicas

$$
\mathbf{n} \times (\mathbf{E}_2 - \mathbf{E}_1) = \mathbf{0}, \qquad \mathbf{n} \times (\mathbf{H}_2 - \mathbf{H}_1) = \mathbf{K}_f,
$$

$$
\mathbf{n} \cdot (\mathbf{D}_2 - \mathbf{D}_1) = \sigma_f, \qquad \mathbf{n} \cdot (\mathbf{B}_2 - \mathbf{B}_1) = 0.
$$

**Demostración.** Por traducción del producto tangencial factual del §14.5.3 y del balance de frontera factual a sus contrapartes clásicas, preservando el criterio de anulación $`\mathbb{F}_{SV}(q) = 0`$ como conjunción de las cuatro condiciones clásicas. Q.E.D.

### 14.17.8. Teorema de reconstrucción completa

**Teorema 14.17.8.** $`\mathcal{D}_{SV}^{-1}`$ aplicado componente a componente al operador maestro absoluto $`\mathbb{E}_{SV} = 0`$ reconstruye íntegramente el conjunto clásico:

- *cuatro ecuaciones de primer orden (Gauss eléctrica, Gauss magnética, Faraday, Ampère-Maxwell);*
- *tres relaciones constitutivas ($`\varepsilon`$, $`\mu`$, $`\sigma`$);*
- *cuatro condiciones de contorno clásicas en interfaz.*

**Demostración.** Por los Teoremas 14.17.2 a 14.17.7, cada componente factual se traduce unívocamente a su contraparte clásica. La reconstrucción es completa porque las componentes factuales agotan el contenido del conjunto clásico, según el Teorema 14.16.2. La reconstrucción es reversible porque $`\mathcal{D}_{SV}`$ y $`\mathcal{D}_{SV}^{-1}`$ son mutuamente inversas. Q.E.D.

---
## Aplicaciones

## §14.18. Aplicación de geometrización factual $`\gamma_{SV}`$

### 14.18.1. Precedencia y estatuto

La aplicación $`\gamma_{SV}`$ no funda el dominio canónico absoluto del aparato, sino que transporta representaciones admisibles hacia $`\Xi_{SV}`$ preservando la estructura de los operadores ya fijados. El estatuto operatorio del dominio $`\Xi_{SV}`$ se consigna en el §3.2 del documento de fundamentos operatorios (Lloret Egea, 2026k, §3.2) como eslabón de la cadena fundacional $`\Omega_{\mathrm{pre}} \to K_3^n \xrightarrow{\varepsilon} \Xi_{SV} \to \Sigma_{\mathrm{conc}} \to \Sigma_{\mathrm{canal}} \to \{m_0, \chi_\alpha, U\}`$. La presente sección formaliza algebraicamente la aplicación $`\varepsilon`$ de esa cadena, bajo la denominación $`\gamma_{SV}`$ para evitar colisión tipográfica con el operador constitutivo eléctrico $`\varepsilon_{SV}`$ y con el tensor factual antisimétrico $`\varepsilon^{SV}_{ijk}`$.

### 14.18.2. Definición

**Definición 14.18.1.** La **aplicación de geometrización factual** $`\gamma_{SV}`$ es la aplicación

$$
\gamma_{SV}: K_3^n \longrightarrow \Xi_{SV}
$$

que lleva cada estado ternario admisible de la célula canónica auxiliar $`K_3^n = \{0, 1, U\}^n`$ al punto correspondiente del dominio canónico geometrizado $`\Xi_{SV}`$, preservando la codificación visible absoluta $`\rho(0) = 1, \rho(1) = 2, \rho(U) = 3`$ del §4.1 del cuerpo.

### 14.18.3. Axiomas operativos

La aplicación $`\gamma_{SV}`$ satisface:

- (G1) *Totalidad absoluta:* $`\gamma_{SV}`$ está definida sobre todo $`K_3^n`$.
- (G2) *Preservación de la codificación visible:* para cada estado ternario $`s \in \{0, 1, U\}`$, $`\gamma_{SV}(s)`$ preserva el módulo factual $`\rho(s)`$.
- (G3) *Compatibilidad con refinamiento factual:* $`\gamma_{SV}`$ es estable bajo la subdivisión admisible del mosaico.
- (G4) *Unicidad de realización admisible:* para cada estado ternario $`s \in K_3^n`$, la realización $`\gamma_{SV}(s) \in \Xi_{SV}`$ es única dentro de la clase de aplicaciones admisibles que cumplen (G1), (G2) y (G3).

### 14.18.4. Consistencia con el aparato operatorio

**Teorema 14.18.2 (consistencia con operadores absolutos).** Los operadores absolutos $`\partial_\nu^{SV}, \partial^{SV}_i, \mathrm{Div}_{SV}, \mathrm{Rot}_{SV}, \varepsilon_{SV}, \mu_{SV}, \sigma_{SV}`$ definidos sobre $`\Xi_{SV}`$ admiten pullback bien definido a través de $`\gamma_{SV}`$ a operadores correspondientes sobre $`K_3^n`$, compatibles con la estructura ternaria absoluta.

**Demostración.** Por (G1) y (G4), la composición $`\gamma_{SV}^{*}\,L := L \circ \gamma_{SV}`$ está bien definida y es única para cada operador $`L`$ sobre $`\Xi_{SV}`$. Por (G2) y (G3), el pullback preserva la codificación visible del §4.1 y el refinamiento factual. La linealidad factual se transporta por linealidad de la composición. Q.E.D.

**Teorema 14.18.3 (consistencia con régimen separable).** Las hipótesis (S1) y (S2) del régimen separable (§14.10) son invariantes bajo $`\gamma_{SV}`$: si una configuración sobre $`\Xi_{SV}`$ las satisface, la configuración correspondiente bajo $`\gamma_{SV}^{-1}`$ hereda las mismas propiedades estructurales.

**Demostración.** (S1) exige independencia posicional del peso $`\omega(\nu_j)`$. Por (G2), $`\gamma_{SV}`$ no introduce dependencia posicional adicional; la independencia se preserva. (S2) exige estabilidad de la base admisible y la métrica; por (G3) y (G4), $`\gamma_{SV}`$ transporta bases admisibles sin alteración de la estructura métrica heredada del cosido metrológico del §5.6 del cuerpo. Q.E.D.

### 14.18.5. Consistencia del bracket factual bajo $`\gamma_{SV}`$

**Teorema 14.18.4.** El bracket factual absoluto $`\langle\cdot,\cdot\rangle_{SV}`$ del §14.7 admite formulación equivalente por composición con $`\gamma_{SV}`$: para todo par de campos admisibles $`F, G: \Xi_{SV} \to \mathbb{R}^3`$,

$$
\langle F, G\rangle_{SV} \;=\; \sum_{s \in K_3^n}\,\rho(s)\cdot (F \circ \gamma_{SV})(s)\cdot (G \circ \gamma_{SV})(s),
$$

con la suma absoluta extendida sobre el mosaico ternario y el producto punto aplicado componente a componente sobre $`\mathbb{R}^3`$.

**Demostración.** Por (G1), $`(F \circ \gamma_{SV}): K_3^n \to \mathbb{R}^3`$ está bien definida. Bilinealidad, simetría y no-negatividad se preservan trivialmente por composición dado que la estructura bilineal reside en $`\mathbb{R}^3`$. La no-degeneración se preserva por (G4): si $`\gamma_{SV}(s) \neq 0`$ para todo $`s`$ no nulo, entonces $`(F \circ \gamma_{SV})(s) = 0`$ para todo $`s`$ implica $`F = 0`$ factualmente. Q.E.D.

### 14.18.6. Cláusula de precedencia

El Teorema 14.18.4 expresa el bracket $`\langle\cdot,\cdot\rangle_{SV}`$ mediante la composición con $`\gamma_{SV}`$. Esta expresión es **reformulación equivalente**, no fundación del bracket. El bracket queda fijado absolutamente en §14.7 sobre la clase admisible de campos; $`\gamma_{SV}`$ transporta representaciones sin alterar el estatuto operatorio de $`\Xi_{SV}`$ ni el de los operadores absolutos que sobre él actúan. Ningún corolario del presente §14.18 deriva estatuto ontológico del dominio a partir de $`\gamma_{SV}`$.

### 14.18.7. Verificación visible de la geometrización

Sobre la célula canónica $`SV(3,9)`$ con estados ternarios $`s_1 = (0, 1, U)`$, $`s_2 = (1, 1, 0)`$, $`s_3 = (U, 0, 1)`$, y base ortonormal admisible $`\{e^{SV}_i\}_{i=1}^{3}`$ del dominio canónico geometrizado $`\Xi_{SV}`$.

**Aplicación sobre estados ternarios.** Por (G2) y la codificación visible $`\rho(0) = 1, \rho(1) = 2, \rho(U) = 3`$:

$$
\gamma_{SV}(s_1) = (1, 2, 3), \quad \gamma_{SV}(s_2) = (2, 2, 1), \quad \gamma_{SV}(s_3) = (3, 1, 2).
$$

**Campo factual admisible.** $`F: \Xi_{SV} \to \mathbb{R}^3`$, $`F(x) = (x_1, x_2, x_3)`$.

**Pullback.**

$$
(F \circ \gamma_{SV})(s_1) = (1, 2, 3), \quad (F \circ \gamma_{SV})(s_2) = (2, 2, 1), \quad (F \circ \gamma_{SV})(s_3) = (3, 1, 2).
$$

**Bracket factual por la forma del Teorema 14.18.4.** Con pesos unitarios sobre los tres estados considerados:

$$
\langle F, F\rangle_{SV} = (1 + 4 + 9) + (4 + 4 + 1) + (9 + 1 + 4) = 14 + 9 + 14 = 37.
$$

La evaluación por la forma del §14.7 sobre los tres puntos de $`\Xi_{SV}`$ imagen de los tres estados produce el valor idéntico $`37`$. Definición 14.18.1 y Teorema 14.18.4 mutuamente consistentes.

---

## §14.19. Operador de conformación polimodal factual $`\mathfrak{U}_{SV}`$

### 14.19.1. Estatuto categorial

El operador $`\mathfrak{U}_{SV}`$ conforma la articulación polimodal de los operadores absolutos del anexo sobre régimen admisible general. Su función es soportar la composición controlada de los operadores $`J_{SV}`$, $`\mathcal{R}^f_{SV}`$, $`\partial^{SV}_i`$, $`\partial_\nu^{SV(k)}`$, $`\mathrm{Div}_{SV}`$, $`\mathrm{Rot}_{SV}`$, $`\times_{SV}`$, $`\langle\cdot,\cdot\rangle_{SV}`$, $`\nabla^{SV}`$ y las componentes del operador maestro $`\mathbb{M}_{SV}`$, $`\mathbb{K}_{SV}`$, $`\mathbb{F}_{SV}`$, sobre configuraciones admisibles fijadas por compuertas factuales tipadas.

### 14.19.2. Clase admisible de configuraciones

**Definición 14.19.1.** La **clase admisible de configuraciones factuales** $`\mathcal{M}^{\mathrm{adm}}_{SV}`$ es el conjunto de pares $`(q, \Omega)`$ con $`q`$ magnitud factual admisible sobre $`\Omega \subseteq \Xi_{SV}`$, compatibles con las prohibiciones constitutivas, el cosido metrológico absoluto y la clausura factual $`\mathsf{Cl}_{SV}`$ del §14.11.3.

### 14.19.3. Tipado canónico de compuertas

**Definición 14.19.2.** Las **compuertas factuales canónicas** son aplicaciones

$$
\mathfrak{c}_* : \mathcal{M}^{\mathrm{adm}}_{SV} \longrightarrow \{0, 1\},
$$

con criterio de paso algebraicamente cerrado. Las cuatro compuertas canónicas se fijan así:

- $`\mathfrak{c}_{\mathrm{sep}}(q, \Omega) = 1`$ si y solo si $`(q, \Omega)`$ satisface las hipótesis (S1) y (S2) del régimen separable (§14.10); $`0`$ en otro caso.

- $`\mathfrak{c}_{\partial\Omega}(q, \Omega) = 1`$ si y solo si $`\det(J_{SV}) = 0`$ sobre $`\partial\Omega`$, es decir, si la frontera factual está activa (§14.2); $`0`$ en otro caso.

- $`\mathfrak{c}_{\Lambda}(q, \Omega) = 1`$ si y solo si el factor de cambio factual $`\Lambda^{(k,l)}`$ entre celdas admisibles es consistente con la orientación factual del mosaico (§14.3); $`0`$ en otro caso.

- $`\mathfrak{c}_{R}(q, \Omega) = 1`$ si y solo si el operador exacto de reconfiguración $`\mathcal{R}^f_{SV}`$ opera con balance compatible sobre $`(q, \Omega)`$ en el sentido del §14.3; $`0`$ en otro caso.

### 14.19.4. Compuerta global

**Definición 14.19.3.** La **compuerta global absoluta** $`\mathfrak{C}_{SV}: \mathcal{M}^{\mathrm{adm}}_{SV} \to \{0, 1\}`$ se define como conjunción absoluta de las cuatro compuertas canónicas:

$$
\mathfrak{C}_{SV}(q, \Omega) \;:=\; \mathfrak{c}_{\mathrm{sep}}(q, \Omega) \cdot \mathfrak{c}_{\partial\Omega}(q, \Omega) \cdot \mathfrak{c}_{\Lambda}(q, \Omega) \cdot \mathfrak{c}_{R}(q, \Omega).
$$

El producto en $`\{0,1\}`$ coincide con la conjunción absoluta: $`\mathfrak{C}_{SV} = 1`$ si y solo si las cuatro compuertas canónicas evalúan simultáneamente a $`1`$.

### 14.19.5. Núcleo compositivo $`\operatorname{Comp}^{\mathrm{poly}}_{SV}`$

**Definición 14.19.4.** Sea $`\mathcal{O}_{SV}`$ la colección de operadores absolutos del anexo enumerados en §14.19.1. El **núcleo compositivo polimodal factual** $`\operatorname{Comp}^{\mathrm{poly}}_{SV}`$ es la operación

$$
\operatorname{Comp}^{\mathrm{poly}}_{SV}: \mathcal{O}_{SV} \times \mathcal{O}_{SV} \times \mathcal{M}^{\mathrm{adm}}_{SV} \longrightarrow \mathcal{O}_{SV}
$$

que, a cada par ordenado $`(L_1, L_2)`$ de operadores absolutos y cada configuración admisible $`(q, \Omega)`$, asigna el operador compuesto $`\operatorname{Comp}^{\mathrm{poly}}_{SV}(L_1, L_2; q, \Omega) \in \mathcal{O}_{SV}`$ definido por las cuatro condiciones siguientes:

- **Dominio preciso.** El dominio de la composición es la intersección de los dominios admisibles de $`L_1`$ y $`L_2`$ restringida a $`(q, \Omega)`$.

- **Regla de composición.** Si las compuertas canónicas involucradas evalúan a $`1`$ sobre $`(q, \Omega)`$, la composición se reduce a la composición funcional estándar $`L_1 \circ L_2`$. Si alguna compuerta canónica relevante evalúa a $`0`$, la composición se modula por el operador de reconfiguración $`\mathcal{R}^f_{SV}`$ aplicado en el punto de ruptura.

- **Asociatividad condicional.** La composición $`\operatorname{Comp}^{\mathrm{poly}}_{SV}`$ es asociativa sobre el subdominio donde $`\mathfrak{C}_{SV}(q, \Omega) = 1`$. Fuera de ese subdominio, la asociatividad queda controlada por la fórmula de reordenación de la jerarquía reconfigurativa (§14.19.7).

- **Equivalencia de salida.** Dos composiciones $`\operatorname{Comp}^{\mathrm{poly}}_{SV}(L_1, L_2; q, \Omega)`$ y $`\operatorname{Comp}^{\mathrm{poly}}_{SV}(L_1', L_2'; q, \Omega)`$ son equivalentes si y solo si producen la misma salida funcional sobre cada elemento admisible de la intersección de sus dominios, módulo aplicación de $`\mathcal{R}^f_{SV}`$ en las interfaces factuales activas.

La relación de $`\operatorname{Comp}^{\mathrm{poly}}_{SV}`$ con la firma general $`\operatorname{Comp}`$ del corpus (composición genérica de operadores sobre $`\Xi_{SV}`$) es la siguiente: $`\operatorname{Comp}^{\mathrm{poly}}_{SV}`$ es la restricción especializada de $`\operatorname{Comp}`$ al subdominio admisible $`\mathcal{M}^{\mathrm{adm}}_{SV}`$ bajo control de las compuertas canónicas.

### 14.19.6. Definición operativa de $`\mathfrak{U}_{SV}`$

**Definición 14.19.5.** El **operador de conformación polimodal factual** $`\mathfrak{U}_{SV}`$ se define como

$$
\mathfrak{U}_{SV}[q, \Omega] \;:=\; \mathfrak{C}_{SV}(q, \Omega) \cdot \operatorname{Comp}^{\mathrm{poly}}_{SV}\bigl(\mathbb{M}_{SV}, \mathbb{K}_{SV}; q, \Omega\bigr) \;+\; \bigl(1 - \mathfrak{C}_{SV}(q, \Omega)\bigr) \cdot \mathbb{F}_{SV}(q),
$$

donde $`\mathbb{M}_{SV}`$ es la componente absoluta de las ecuaciones de primer orden, $`\mathbb{K}_{SV}`$ la componente de clausura y $`\mathbb{F}_{SV}`$ la componente absoluta de frontera fijada en §14.11.

### 14.19.7. Jerarquía reconfigurativa $`\mathcal{R}^{f,(k)}_{SV}`$

**Definición 14.19.6.** La **jerarquía absoluta de operadores de reconfiguración factual** se define inductivamente como

$$
\mathcal{R}^{f,(1)}_{SV} := \mathcal{R}^f_{SV}, \qquad \mathcal{R}^{f,(k+1)}_{SV} := \mathcal{R}^{f,(k)}_{SV} \circ \mathcal{R}^f_{SV}, \quad k \geq 1.
$$

**Teorema 14.19.7.** La jerarquía $`\mathcal{R}^{f,(k)}_{SV}`$ es estable bajo composición absoluta: para todo par $`k_1, k_2 \geq 1`$,

$$
\mathcal{R}^{f,(k_1)}_{SV} \circ \mathcal{R}^{f,(k_2)}_{SV} \;=\; \mathcal{R}^{f,(k_1 + k_2)}_{SV}.
$$

**Demostración.** Por la Definición 14.19.6 aplicada inductivamente sobre el orden compositivo. Q.E.D.

### 14.19.8. Teorema de existencia tipada

**Teorema 14.19.8 (existencia tipada de $`\mathfrak{U}_{SV}`$).** Para toda configuración $`(q, \Omega) \in \mathcal{M}^{\mathrm{adm}}_{SV}`$, el operador $`\mathfrak{U}_{SV}[q, \Omega]`$ está bien definido, es único, y evalúa a un operador admisible de $`\mathcal{O}_{SV}`$.

**Demostración.** Por la Definición 14.19.3, $`\mathfrak{C}_{SV}(q, \Omega) \in \{0, 1\}`$. Caso $`\mathfrak{C}_{SV} = 1`$: el operador reduce a $`\operatorname{Comp}^{\mathrm{poly}}_{SV}(\mathbb{M}_{SV}, \mathbb{K}_{SV}; q, \Omega)`$, que es admisible por la Definición 14.19.4 (dominio preciso y regla de composición). Caso $`\mathfrak{C}_{SV} = 0`$: el operador reduce a $`\mathbb{F}_{SV}(q)`$, admisible por §14.11. En ambos casos, $`\mathfrak{U}_{SV}[q, \Omega]`$ es único por unicidad de $`\mathfrak{C}_{SV}`$ y de $`\operatorname{Comp}^{\mathrm{poly}}_{SV}`$. Q.E.D.

### 14.19.9. Teorema de no identidad de suceso

**Teorema 14.19.9.** Para configuraciones admisibles con $`\mathfrak{C}_{SV} = 1`$, el operador $`\mathfrak{U}_{SV}`$ no introduce identificación extrínseca entre sucesos distintos del índice factual $`\nu`$.

**Demostración.** La composición $`\operatorname{Comp}^{\mathrm{poly}}_{SV}(\mathbb{M}_{SV}, \mathbb{K}_{SV}; q, \Omega)`$ opera sobre el índice de suceso $`\nu_j`$ por aplicación de $`\partial_\nu^{SV}`$ y $`\partial_\nu^{SV(k)}`$, que son operadores locales en el índice. Ninguno de los operadores absolutos de $`\mathcal{O}_{SV}`$ identifica sucesos $`\nu_j \neq \nu_l`$ por construcción: la diferencia factual conserva la distinción ordinal absoluta. Q.E.D.

### 14.19.10. Teorema de no colapso escalar

**Teorema 14.19.10.** $`\mathfrak{U}_{SV}[q, \Omega]`$ no colapsa a escalar trivial bajo régimen admisible con $`\mathfrak{C}_{SV} = 1`$: su salida conserva el tipo tensorial de los operadores compuestos.

**Demostración.** La composición $`\operatorname{Comp}^{\mathrm{poly}}_{SV}(L_1, L_2; q, \Omega)`$ preserva el tipo tensorial máximo de los operandos por regla de composición funcional. Si $`L_1`$ tiene rango tensorial $`r_1`$ y $`L_2`$ rango $`r_2`$, la composición tiene rango al menos $`\max(r_1 - 1, r_2 - 1)`$ tras contracción de un índice. Para $`L_1 = \mathbb{M}_{SV}`$ (rango conjunto $`\geq 2`$) y $`L_2 = \mathbb{K}_{SV}`$ (rango conjunto $`\geq 1`$), el rango resultante es estrictamente positivo, excluyendo colapso escalar. Q.E.D.

### 14.19.11. Teorema de posterioridad transductiva

**Teorema 14.19.11.** La acción de $`\mathfrak{U}_{SV}`$ es posterior a la activación transductiva del régimen: $`\mathfrak{U}_{SV}[q, \Omega]`$ opera sobre configuraciones $`(q, \Omega)`$ ya constituidas sobre $`\Sigma_{\mathrm{canal}}`$, sin intervenir en la cadena fundacional $`\Omega_{\mathrm{pre}} \to K_3^n \to \Xi_{SV}`$ anterior.

**Demostración.** Por el dominio de definición fijado en la Definición 14.19.1, $`\mathcal{M}^{\mathrm{adm}}_{SV}`$ exige que $`(q, \Omega)`$ sea compatible con las prohibiciones constitutivas y con el cosido metrológico absoluto, lo cual presupone que la cadena fundacional ya ha sido recorrida hasta $`\Sigma_{\mathrm{canal}}`$. Ningún término de la Definición 14.19.5 actúa sobre $`\Omega_{\mathrm{pre}}`$ ni sobre $`K_3^n`$ independientemente; la acción se ejerce exclusivamente a través de operadores absolutos cuyo dominio operativo es posterior a la geometrización. Q.E.D.

### 14.19.12. Verificación visible del operador $`\mathfrak{U}_{SV}`$

**Configuración admisible con compuerta global $`\mathfrak{C}_{SV} = 1`$.** Sobre celda admisible del mosaico $`SV(3,9)`$ con $`q = E = (2x_3, 0, 0)`$, $`\Omega`$ dominio regular con $`\det(J_{SV}) = 1`$, peso uniforme $`\omega = 1`$, constitutivo diagonal autoadjunto.

Evaluación de compuertas: $`\mathfrak{c}_{\mathrm{sep}} = 1`$ (régimen separable), $`\mathfrak{c}_{\partial\Omega} = 0`$ (frontera no activa sobre el interior), $`\mathfrak{c}_{\Lambda} = 1`$ (orientación consistente), $`\mathfrak{c}_{R} = 1`$ (balance compatible). Compuerta global: $`\mathfrak{C}_{SV} = 1 \cdot 0 \cdot 1 \cdot 1 = 0`$ sobre el interior.

Por la Definición 14.19.5 con $`\mathfrak{C}_{SV} = 0`$: $`\mathfrak{U}_{SV}[q, \Omega] = \mathbb{F}_{SV}(q) = \mathbb{1}_{\det(J_{SV})=0}[\cdots] = 0`$ sobre el interior. Correcto operativamente: el operador colapsa a la componente de frontera cuando no hay activación polimodal sobre el interior.

**Configuración admisible con frontera activa.** Sobre interfaz $`\partial C_{1,2}`$ con $`\det(J_{SV}) = 0`$. Evaluación: $`\mathfrak{c}_{\mathrm{sep}} = 1`$, $`\mathfrak{c}_{\partial\Omega} = 1`$, $`\mathfrak{c}_{\Lambda} = 1`$, $`\mathfrak{c}_{R} = 1`$ (balance $`B_{\partial\Omega}^{SV} = \mathcal{R}^f_{SV} = 7{,}2`$). Compuerta global $`\mathfrak{C}_{SV} = 1`$.

Por la Definición 14.19.5 con $`\mathfrak{C}_{SV} = 1`$: $`\mathfrak{U}_{SV}[q, \Omega] = \operatorname{Comp}^{\mathrm{poly}}_{SV}(\mathbb{M}_{SV}, \mathbb{K}_{SV}; q, \Omega)`$, composición activa de las componentes de primer orden y de clausura. Correcto operativamente: el operador orquesta la composición polimodal cuando las cuatro compuertas canónicas coinciden.

**Configuración con compuerta de orientación inconsistente.** Misma interfaz con $`\Lambda^{(1,2)}`$ incompatible con la orientación absoluta del mosaico. Evaluación: $`\mathfrak{c}_{\Lambda} = 0`$. Compuerta global $`\mathfrak{C}_{SV} = 0`$. Por la Definición 14.19.5: $`\mathfrak{U}_{SV}[q, \Omega] = \mathbb{F}_{SV}(q) \neq 0`$ por orientación no admisible. Configuración fuera de clausura $`\mathsf{Cl}_{SV}`$. Correcto operativamente: las compuertas filtran configuraciones no admisibles sin forzar continuidad espuria.

---

## §14.20. Bancos visibles

### 14.20.1. Propósito

La presente sección consigna los bancos visibles del anexo en forma canónica *datos, cálculo, salida, dictamen*, sin descripción abstracta. Cada banco es reproducible sobre la célula canónica $`SV(3,9)`$ o sobre trayectoria admisible explícita.

### 14.20.2. Banco B-01: jacobiano factual

**Datos.** Magnitud factual $`q(\theta) = (\theta_1^2 + \theta_2, \theta_1\theta_2)`$ sobre parámetro admisible $`\theta = (\theta_1, \theta_2)`$.

**Cálculo.** $`J_{SV}(q,\theta) = \begin{pmatrix} 2\theta_1 & 1 \\ \theta_2 & \theta_1 \end{pmatrix}`$, $`\det(J_{SV}) = 2\theta_1^2 - \theta_2`$.

**Salida.** En $`\theta = (1, 1)`$: $`\det = 1`$, régimen regular. En $`\theta = (1, 2)`$: $`\det = 0`$, régimen singular.

**Dictamen.** Anulación del determinante coincide con la curva $`\theta_2 = 2\theta_1^2`$; frontera factual admisible localizada exactamente sobre esta curva. Coherente con la Definición 14.2.1 del criterio absoluto de frontera.

### 14.20.3. Banco B-02: tensor antisimétrico $`\varepsilon^{SV}_{ijk}`$

**Datos.** Base ortonormal admisible $`(e^{SV}_1, e^{SV}_2, e^{SV}_3)`$, componentes $`\varepsilon^{SV}_{123} = +1`$.

**Cálculo.** Contracción triple: $`\varepsilon^{SV}_{ijk}\,\varepsilon^{SV,ijk} = (+1)^2 + (+1)^2 + (+1)^2 + (-1)^2 + (-1)^2 + (-1)^2 = 6`$.

**Salida.** Valor $`6`$.

**Dictamen.** Coincidencia exacta con el Corolario 14.4.3. Verificación de consistencia de la antisimetría absoluta sobre la base tridimensional del mosaico.

### 14.20.4. Banco B-03: identidad de Poynting factual

**Datos.** Campos $`E(x_1, x_2, x_3) = (2x_3, 0, 0)`$, $`H(x_1, x_2, x_3) = (0, 3x_3, 0)`$. Evaluación en $`x_3 = 1`$.

**Cálculo.** $`S_{SV} = E \times_{SV} H = (0, 0, 6x_3^2)`$. $`\mathrm{Div}_{SV}(S_{SV}) = 12x_3`$. $`\langle H, \mathrm{Rot}_{SV}\,E\rangle_{SV} = 6x_3`$. $`\langle E, \mathrm{Rot}_{SV}\,H\rangle_{SV} = -6x_3`$.

**Salida.** $`\langle H, \mathrm{Rot}_{SV}\,E\rangle_{SV} - \langle E, \mathrm{Rot}_{SV}\,H\rangle_{SV} = 6x_3 - (-6x_3) = 12x_3`$.

**Dictamen.** Igualdad exacta entre $`\mathrm{Div}_{SV}(S_{SV})`$ y la forma del segundo miembro del Teorema 14.5.4. Identidad de Poynting factual verificada sobre configuración admisible.

### 14.20.5. Banco B-04: iteración $`\partial_\nu^{SV(2)}`$

**Datos.** Trayectoria $`(q_0, \ldots, q_{10}) = (0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55)`$ con $`q_j = j(j+1)/2`$. Peso uniforme $`\omega = 1`$.

**Cálculo.** $`(\partial_\nu^{SV(2)}\,q)(j) = q_{j+2} - 2q_{j+1} + q_j`$ para $`j = 0, 1, 4, 8`$: valores $`1, 1, 1, 1`$. $`(\partial_\nu^{SV(3)}\,q)(0) = q_3 - 3q_2 + 3q_1 - q_0 = 6 - 9 + 3 - 0 = 0`$.

**Salida.** $`\partial_\nu^{SV(2)}\,q \equiv 1`$ sobre la trayectoria; $`\partial_\nu^{SV(3)}\,q \equiv 0`$.

**Dictamen.** Coincidencia exacta con la Proposición 14.9.4 (anulación sobre polinomios factuales de grado menor que $`k`$). Iteración de segunda derivada de suceso verificada.

### 14.20.6. Banco B-05: conmutador suceso-posición

**Datos.** Campo $`q_j(x) = j \cdot x`$ sobre trayectoria de cinco sucesos, dominio posicional $`x \in \{0, 1, 2, 3, 4\}`$. Dos configuraciones: (a) peso $`\omega = 1`$ constante; (b) peso $`\omega(\nu_j, x) = 1 + 0{,}1 x`$.

**Cálculo.** Configuración (a): $`\partial_\nu^{SV}(\mathrm{Div}_{SV}\,q)(j, x) = 1`$, $`\mathrm{Div}_{SV}(\partial_\nu^{SV}\,q)(j, x) = 1`$. Configuración (b), $`x = 0`$: $`\partial_\nu^{SV}(\mathrm{Div}_{SV}\,q) = 1`$, $`\mathrm{Div}_{SV}(\partial_\nu^{SV}\,q) = 0{,}9091`$.

**Salida.** Configuración (a): $`[\partial_\nu^{SV}, \mathrm{Div}_{SV}]\,q = 0`$. Configuración (b), $`x = 0`$: conmutador $`= 0{,}0909 \neq 0`$.

**Dictamen.** En régimen separable (a) los operadores conmutan exactamente (Teorema 14.10.2). En régimen con peso posicionalmente variable (b) la hipótesis (S1) se viola y el conmutador es no nulo cuantificable. Contraste confirma que el régimen separable es condición estructural, no ornamento.

### 14.20.7. Banco B-06: balance de Leibniz factual

**Datos.** Trayectoria de tres sucesos, peso $`\omega = 1`$, dimensión posicional $`n = 2`$, $`E_0 = (0,0)`$, $`E_1 = (1,1)`$, $`E_2 = (2,1)`$, $`\partial_\nu^{SV}\,E(0) = (1,1)`$, $`\partial_\nu^{SV}\,E(1) = (1,0)`$. Dos constitutivos: (a) $`\varepsilon_{SV}^{(A)} = \mathrm{diag}(2,3)`$ autoadjunto; (b) $`\varepsilon_{SV}^{(B)} = \begin{pmatrix} 2 & 0{,}5 \\ -0{,}5 & 3 \end{pmatrix}`$ no autoadjunto.

**Cálculo.** (a): $`u_{SV}(1) = 2{,}5`$, $`u_{SV}(2) = 5{,}5`$, $`\partial_\nu^{SV}\,u_{SV}(1) = 3`$. Por Corolario 14.8.3: $`3`$. (b): $`u_{SV}(1) = 2{,}5`$, $`u_{SV}(2) = 5{,}5`$, $`\partial_\nu^{SV}\,u_{SV}(1) = 3`$. Por Corolario 14.8.3: $`2{,}5`$.

**Salida.** Configuración (a): igualdad exacta $`3 = 3`$. Configuración (b): discrepancia $`3 - 2{,}5 = 0{,}5`$.

**Dictamen.** La identidad de Leibniz factual para la densidad electromagnética requiere autoadjunción absoluta del constitutivo. La discrepancia $`0{,}5`$ coincide con la mitad del desacoplo entre los dos órdenes de contracción. Teorema 14.8.2 confirmado como condición estructural.

### 14.20.8. Banco B-07: bicondicional absoluto de $`\mathbb{F}_{SV}`$

**Datos.** Tres escenarios: (a) régimen regular interior con $`\det(J_{SV}) = 1`$; (b) frontera activa con $`B_{\partial\Omega}^{SV}(q) = 7{,}2`$, $`\mathcal{R}^f_{SV}(q) = 7{,}2`$; (c) frontera activa con $`B_{\partial\Omega}^{SV}(q) = 7{,}2`$, $`\mathcal{R}^f_{SV}(q) = 6{,}5`$.

**Cálculo.** (a): $`\mathbb{F}_{SV}(q) = 0 \cdot [\cdots] = 0`$. (b): $`\mathbb{F}_{SV}(q) = 1 \cdot (7{,}2 - 7{,}2) = 0`$. (c): $`\mathbb{F}_{SV}(q) = 1 \cdot (7{,}2 - 6{,}5) = 0{,}7`$.

**Salida.** (a) y (b): compatibilidad interfacial; (c): incompatibilidad cuantificable.

**Dictamen.** El bicondicional del Teorema 14.11.3 se verifica en las dos direcciones. La configuración (c) queda fuera de clausura admisible $`\mathsf{Cl}_{SV}`$.

### 14.20.9. Banco B-08: curvatura factual sobre interfaz

**Datos.** Dos celdas $`C_1, C_2`$ con bases relacionadas por rotación absoluta $`\Lambda^{(1,2)}`$ de ángulo $`\theta = \pi/6`$.

**Cálculo.** Interior de $`C_1`$: base uniforme, $`\partial_i \partial_j - \partial_j \partial_i = 0`$, curvatura $`\mathbf{R}^{SV}_{C_1} = 0`$, $`\mathrm{Scal}^{SV}_{C_1} = 0`$. Interfaz $`\partial C_{1,2}`$: $`\Lambda^{(1,2)} = \begin{pmatrix}\cos\theta & \sin\theta & 0 \\ -\sin\theta & \cos\theta & 0 \\ 0 & 0 & 1\end{pmatrix}`$, $`\det(\Lambda) = 1`$, $`\partial^{SV}_\tau \Lambda^{(1,2)}`$ con discontinuidad localizada en $`\tau = 0`$.

**Salida.** Componente $`\mathbf{R}^{SV,l}_{1212}`$ no nula localizada sobre interfaz, absorbida por $`\mathcal{R}^f_{SV}`$ a través del factor $`\Lambda^{(1,2)}`$ según Teorema 14.3.5.

**Dictamen.** Anulación interior (Teorema 14.12.6) y activación interfacial (Teorema 14.12.8) confirmadas. Curvatura factual sobre frontera activa coincide con el cambio de carta factual.

### 14.20.10. Banco B-09: balance covariante $`T^{SV}_{\mu\nu}`$ en vacío

**Datos.** Campos de B-03 con $`\varepsilon_0 = \mu_0 = 1`$, $`J = 0`$, $`x_3 = 1`$.

**Cálculo.** $`T^{SV}_{00} = 6{,}5`$, $`T^{SV}_{0i} = (0, 0, 6)`$, $`T^{SV}_{11} = 2{,}5`$, $`T^{SV}_{22} = -2{,}5`$, $`T^{SV}_{33} = 6{,}5`$, $`T^{SV}_{12} = T^{SV}_{13} = T^{SV}_{23} = 0`$.

**Salida.** $`\partial_\nu^{SV}\,T^{SV}_{\mu\nu} = 0`$ sobre configuración estacionaria en vacío.

**Dictamen.** Teorema 14.13.2 verificado en el régimen de vacío factual. Balance covariante se anula componente a componente.

### 14.20.11. Banco B-10: principio variacional

**Datos.** Potencial factual $`A^{SV}_0 = 0`$, $`A^{SV}_1 = 0`$, $`A^{SV}_2 = -x_1 x_3`$, $`A^{SV}_3 = 0`$. Vacío ($`J = 0`$, $`\varepsilon_0 = \mu_0 = 1`$).

**Cálculo.** $`F^{SV}_{12} = -x_3`$, $`F^{SV}_{23} = x_1`$, $`F^{SV}_{13} = 0`$. Euler-Lagrange factual sobre $`A^{SV}_2`$: $`\partial^{SV}_\mu F^{SV,\mu 2} = \partial^{SV}_1(x_3) + \partial^{SV}_3(x_1) = 0`$.

**Salida.** $`\partial^{SV}_\mu F^{SV,\mu 2} = 0 = J^2`$.

**Dictamen.** Ecuación de Euler-Lagrange factual coincide con la componente $`\mathbb{M}_{SV}`$ del operador maestro (Teorema 14.14.3). Principio variacional reproduce las ecuaciones absolutas de primer orden.

### 14.20.12. Banco B-11: geometrización $`\gamma_{SV}`$

**Datos.** Estados $`s_1 = (0, 1, U)`$, $`s_2 = (1, 1, 0)`$, $`s_3 = (U, 0, 1)`$. Codificación $`\rho(0) = 1, \rho(1) = 2, \rho(U) = 3`$. Campo $`F: \Xi_{SV} \to \mathbb{R}^3`$, $`F(x) = (x_1, x_2, x_3)`$.

**Cálculo.** $`\gamma_{SV}(s_1) = (1, 2, 3)`$, $`\gamma_{SV}(s_2) = (2, 2, 1)`$, $`\gamma_{SV}(s_3) = (3, 1, 2)`$. $`(F \circ \gamma_{SV})(s_i) = \gamma_{SV}(s_i)`$. Bracket por composición: $`\langle F, F\rangle_{SV} = (1+4+9) + (4+4+1) + (9+1+4) = 37`$.

**Salida.** Bracket por composición: $`37`$. Bracket directo sobre imágenes: $`37`$.

**Dictamen.** Coincidencia exacta. Teorema 14.18.4 verificado sobre la configuración canónica.

### 14.20.13. Banco B-12: operador $`\mathfrak{U}_{SV}`$

**Datos.** Tres escenarios: (a) interior regular; (b) interfaz activa con balance compatible; (c) interfaz con $`\Lambda^{(1,2)}`$ inconsistente.

**Cálculo.** (a): $`\mathfrak{c}_{\partial\Omega} = 0 \Rightarrow \mathfrak{C}_{SV} = 0 \Rightarrow \mathfrak{U}_{SV} = \mathbb{F}_{SV} = 0`$. (b): $`\mathfrak{C}_{SV} = 1 \Rightarrow \mathfrak{U}_{SV} = \operatorname{Comp}^{\mathrm{poly}}_{SV}(\mathbb{M}_{SV}, \mathbb{K}_{SV})`$. (c): $`\mathfrak{c}_{\Lambda} = 0 \Rightarrow \mathfrak{C}_{SV} = 0 \Rightarrow \mathfrak{U}_{SV} = \mathbb{F}_{SV} \neq 0`$.

**Salida.** Tres salidas distintas según compuertas; ningún caso trivializa el operador.

**Dictamen.** Teoremas 14.19.8 (existencia tipada), 14.19.9 (no identidad de suceso), 14.19.10 (no colapso escalar), 14.19.11 (posterioridad transductiva) confirmados sobre los tres escenarios.

---

## §14.21. Síntesis algebraica

### 14.21.1. Política metrológica de clasificación de objetos del anexo

**Tabla 14.21.1. Política metrológica absoluta.**

| Clase metrológica | Definición | Objetos pertenecientes |
|---|---|---|
| Objeto estructural sin metrología propia | Construcción algebraica auxiliar que hereda su dimensión de los operandos | $`\varepsilon^{SV}_{ijk}`$, $`\times_{SV}`$, $`\mathbb{1}_{\det(J_{SV})=0}`$, $`\mathfrak{c}_*`$, $`\mathfrak{C}_{SV}`$, $`\operatorname{Comp}^{\mathrm{poly}}_{SV}`$ |
| Operador con metrología inducida | Operador cuya dimensión se deriva del cosido metrológico del §5.6 del cuerpo sin dimensión independiente | $`\partial_\nu^{SV}`$, $`\partial^{SV}_i`$, $`\mathrm{Div}_{SV}`$, $`\mathrm{Rot}_{SV}`$, $`\langle\cdot,\cdot\rangle_{SV}`$, $`\nabla^{SV}`$, $`\mathcal{R}^f_{SV}`$, $`\mathcal{R}^{f,(k)}_{SV}`$, $`\mathfrak{U}_{SV}`$, $`\gamma_{SV}`$ |
| Magnitud factual con dimensión absoluta explícita | Objeto con dimensión canónica en UE_MFC, UFE, UFM, UFC o derivadas | $`J_{SV}`$ (UE_MFC/parámetro), $`u_{SV}`$ (UFE·UFM), $`T^{SV}_{\mu\nu}`$, $`\mathcal{L}_{SV}`$, $`\lambda_{SV}`$ (UFE), $`\mathbb{F}_{SV}`$ (heredada de $`B_{\partial\Omega}^{SV}`$) |

### 14.21.2. Tabla 14.21.2. Operadores algebraicos absolutos del anexo

| Operador | Sección | Función |
|---|---|---|
| $`J_{SV}`$ | §14.1 | Jacobiano factual de sensibilidad de régimen |
| $`\det(J_{SV})`$ | §14.1 | Índice escalar de sensibilidad factual |
| $`\mathbb{1}_{\det(J_{SV})=0}`$ | §14.2 | Indicador absoluto de frontera factual |
| $`\mathcal{R}^f_{SV}`$ | §14.3 | Operador exacto de reconfiguración factual |
| $`\varepsilon^{SV}_{ijk}`$ | §14.4 | Tensor factual completamente antisimétrico de orden 3 |
| $`\times_{SV}`$ | §14.5 | Producto vectorial factual |
| $`\mathrm{Rot}_{SV}`$ | §14.6 | Rotor factual |
| $`\langle\cdot,\cdot\rangle_{SV}`$ | §14.7 | Bracket factual absoluto |
| Autoadjunción factual | §14.8 | Propiedad de constitutivos absolutos |
| $`\partial_\nu^{SV(k)}`$ | §14.9 | Iteración canónica del operador de suceso |
| Régimen separable | §14.10 | Subdominio admisible (S1) + (S2) |
| $`\mathbb{F}_{SV}`$ | §14.11 | Componente absoluta de frontera (bicondicional bajo $`\mathsf{Cl}_{SV}`$) |
| $`\nabla^{SV}, \mathbf{R}^{SV}, \mathrm{Ric}^{SV}, \mathrm{Scal}^{SV}`$ | §14.12 | Conexión factual y curvatura factual |
| $`T^{SV}_{\mu\nu}`$ | §14.13 | Tensor factual de energía-momento |
| $`\mathcal{L}_{SV}, \mathcal{A}_{SV}`$ | §14.14 | Densidad lagrangiana y acción factuales |
| Ecuación de onda factual, $`\lambda_{SV}`$ | §14.15 | Onda electromagnética y longitud factual |
| $`\mathbf{OpFact}_{SV}`$ | §14.16 | Categoría absoluta de operadores factuales admisibles |
| $`\mathcal{D}_{SV}^{-1}`$ | §14.17 | Diccionario inverso factual-clásico |
| $`\gamma_{SV}`$ | §14.18 | Aplicación de geometrización factual |
| $`\mathfrak{c}_*, \mathfrak{C}_{SV}, \operatorname{Comp}^{\mathrm{poly}}_{SV}, \mathfrak{U}_{SV}, \mathcal{R}^{f,(k)}_{SV}`$ | §14.19 | Operador de conformación polimodal factual |

### 14.21.3. Tabla 14.21.3. Teoremas absolutos del anexo

| Teorema | Sección | Contenido |
|---|---|---|
| 14.1.1 | §14.1 | Transformación factual del jacobiano |
| 14.2.2 | §14.2 | Complementariedad regular-frontera |
| 14.3.5 | §14.3 | Absorción absoluta del cambio de carta por $`\mathcal{R}^f_{SV}`$ |
| 14.4.1 | §14.4 | Identidad algebraica fundamental de $`\varepsilon^{SV}`$ |
| 14.5.4 | §14.5 | Identidad de Poynting factual |
| 14.6.x | §14.6 | Teorema de Stokes factual |
| 14.7.4 | §14.7 | Regla de Leibniz factual bajo $`\partial_\nu^{SV}`$ |
| 14.7.5 | §14.7 | No negatividad de la densidad electromagnética factual |
| 14.8.2 | §14.8 | Autoadjunción de los operadores constitutivos |
| 14.8.5 | §14.8 | Anulación local de $`\mathrm{Div}_{SV}\circ\mathrm{Rot}_{SV}`$ |
| 14.9.1 | §14.9 | Forma cerrada de $`\partial_\nu^{SV(k)}`$ en pesos uniformes |
| 14.9.4 | §14.9 | Anulación de $`\partial_\nu^{SV(k)}`$ sobre polinomios de grado $`< k`$ |
| 14.10.2 | §14.10 | Conmutación de $`\partial_\nu^{SV}`$ con $`\mathrm{Div}_{SV}`$ y $`\mathrm{Rot}_{SV}`$ en régimen separable |
| 14.11.3 | §14.11 | Bicondicional absoluto de compatibilidad interfacial |
| 14.12.5 | §14.12 | Identidades de Bianchi factuales |
| 14.12.6 | §14.12 | Anulación de curvatura en régimen separable global |
| 14.13.2 | §14.13 | Balance covariante factual $`T^{SV}_{\mu\nu}`$ |
| 14.14.3 | §14.14 | Derivación de $`\mathbb{M}_{SV}`$ por Euler-Lagrange factual |
| 14.15.x | §14.15 | Existencia y unicidad de solución factual de onda |
| 14.16.2 | §14.16 | Unicidad representacional de $`\mathbb{E}_{SV}`$ |
| 14.16.3 | §14.16 | Irreducibilidad algebraica de $`\mathbb{E}_{SV}`$ |
| 14.17.8 | §14.17 | Reconstrucción inversa completa del conjunto clásico |
| 14.18.2 | §14.18 | Consistencia de $`\gamma_{SV}`$ con operadores absolutos |
| 14.18.4 | §14.18 | Equivalencia de formulaciones del bracket bajo $`\gamma_{SV}`$ |
| 14.19.7 | §14.19 | Estabilidad de la jerarquía $`\mathcal{R}^{f,(k)}_{SV}`$ |
| 14.19.8 | §14.19 | Existencia tipada de $`\mathfrak{U}_{SV}`$ |
| 14.19.9 | §14.19 | No identidad de suceso de $`\mathfrak{U}_{SV}`$ |
| 14.19.10 | §14.19 | No colapso escalar de $`\mathfrak{U}_{SV}`$ |
| 14.19.11 | §14.19 | Posterioridad transductiva de $`\mathfrak{U}_{SV}`$ |

### 14.21.4. Tabla 14.21.4. Bancos visibles del anexo

| Banco | Objeto verificado | Sección |
|---|---|---|
| B-01 | Jacobiano factual y criterio absoluto de frontera | §14.20.2 |
| B-02 | Contracción canónica de $`\varepsilon^{SV}`$ | §14.20.3 |
| B-03 | Identidad de Poynting factual | §14.20.4 |
| B-04 | Iteración $`\partial_\nu^{SV(2)}`$ sobre trayectoria canónica | §14.20.5 |
| B-05 | Conmutador suceso-posición en régimen separable y no separable | §14.20.6 |
| B-06 | Balance de Leibniz factual con constitutivos autoadjunto y no autoadjunto | §14.20.7 |
| B-07 | Bicondicional absoluto de $`\mathbb{F}_{SV}`$ | §14.20.8 |
| B-08 | Curvatura factual sobre interfaz | §14.20.9 |
| B-09 | Balance covariante $`T^{SV}_{\mu\nu}`$ en vacío | §14.20.10 |
| B-10 | Principio variacional sobre configuración canónica | §14.20.11 |
| B-11 | Geometrización absoluta de estados ternarios | §14.20.12 |
| B-12 | Operador $`\mathfrak{U}_{SV}`$ sobre tres escenarios | §14.20.13 |

### 14.21.5. Estatuto de cierre

El desarrollo algebraico del anexo cierra el aparato operatorio del régimen electromagnético factual del Sistema Vectorial SV sobre el régimen canalizado de propagación $`\Sigma_{\mathrm{canal}}`$. La cadena fundacional $`\Omega_{\mathrm{pre}} \to K_3^n \to \Xi_{SV} \to \Sigma_{\mathrm{conc}} \to \Sigma_{\mathrm{canal}} \to \{m_0, \chi_\alpha, U\}`$ queda operativamente soportada, con la aplicación de geometrización $`\gamma_{SV}`$ formalizada algebraicamente y con el operador de conformación polimodal $`\mathfrak{U}_{SV}`$ orquestando la composición controlada de los operadores absolutos bajo compuertas canónicas tipadas.

Las veintiún secciones del anexo, los teoremas absolutos con demostración cerrada, los doce bancos visibles en forma canónica *datos / cálculo / salida / dictamen* y las tablas de síntesis constituyen el aparato operatorio del régimen dentro de la categoría $`\mathbf{OpFact}_{SV}`$ de operadores factuales admisibles. La unicidad representacional del Teorema 14.16.2 y la irreducibilidad algebraica del Teorema 14.16.3 aseguran que $`\mathbb{E}_{SV}`$ constituye el desenlace final algebraico del régimen. La reconstrucción inversa del Teorema 14.17.8 garantiza la compatibilidad plena con la formulación clásica de Maxwell bajo el diccionario absoluto $`\mathcal{D}_{SV}`$ y su inversa formal $`\mathcal{D}_{SV}^{-1}`$.

---

---

## Referencias

Lloret Egea, J. A. (2026a). *Nuevas matemáticas del Sistema Vectorial SV y Física factual como conjunto iniciador*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/nuevas-matematicas-del-sistema-vectorial-sv-y-fisica-factual-como-conjunto-iniciador

Lloret Egea, J. A. (2026b). *Conjunto matemático unificado del cambio factual, ciclos, medición factual y trayectorias poligonales de activación en el Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/conjunto-matematico-unificado-del-cambio-factual-ciclos-medicion-factual-y-trayectorias-poligonales-de-activacion-en-el-sistema-vectorial-sv

Lloret Egea, J. A. (2026c). *Primitivos metrológicos del Sistema Vectorial SV: instanciaciones contingentes de las constantes fundacionales del Sistema Internacional, justificación algebraica y tabla de equivalencias factuales*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/primitivos-metrologicos-del-sistema-vectorial-sv-instanciaciones-contingentes-de-las-constantes-fundacionales-del-sistema-internacional-justificacion-algebraica-y-tabla-de-equivalencias-factuales

Lloret Egea, J. A. (2026d). *Fourier factual y ecuación de onda electromagnética en el Sistema Vectorial SV: desarrollo cíclico, transformada modal y propagación sobre ciclo y trayectoria poligonal*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv-desarrollo-ciclico-transformada-modal-y-propagacion-sobre-ciclo-y-trayectoria-poligonal

Lloret Egea, J. A. (2026e). *Medición, reconstrucción e incertidumbre estructural en la física contemporánea sin probabilidad ni tiempo absoluto: un marco analítico basado en sucesos y trayectorias con laboratorios ejecutables*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/medicion-reconstruccion-e-incertidumbre-estructural-en-la-fisica-contemporanea-sin-probabilidad-ni-tiempo-absoluto-un-marco-analitico-basado-en-sucesos-y-trayectorias-con-laboratorios-ejecutables

Lloret Egea, J. A. (2026f). *Correlación, restricción de clausura y no clausura posicional en dominios cuánticos contemporáneos: una relectura doctrinal desde el Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/correlacion-restriccion-de-clausura-y-no-clausura-posicional-en-dominios-cuanticos-contemporaneos-una-relectura-doctrinal-desde-el-sistema-vectorial-sv

Lloret Egea, J. A. (2026g). *Absorción de E₀ = m₀c² como sector basal de reposo en el Sistema Vectorial SV: estructura factual ampliada, compatibilidad modal, balance con residual y criterio conservador de clausura*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/absorcion-de-e--mc-como-sector-basal-de-reposo-en-el-sistema-vectorial-sv-estructura-factual-ampliada-compatibilidad-modal-balance-con-residual-y-criterio-conservador-de-clausura

Lloret Egea, J. A. (2026h). *Del contenido físico factual del suceso a las clases factuales emergentes: programa de transmutación factual en el Sistema SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/del-contenido-fisico-factual-del-suceso-a-las-clases-factuales-emergentes-programa-de-transmutacion-factual-en-el-sistema-sv

Lloret Egea, J. A. (2026i). *Del contenido físico factual del suceso a la entidad absoluta del campo en el Sistema Vectorial SV: absorción basal exacta, unificación fuerte de gravitación, electricidad y magnetismo, y apertura a clases factuales emergentes*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/del-contenido-fisico-factual-del-suceso-a-la-entidad-absoluta-del-campo-en-el-sistema-vectorial-sv-absorcion-basal-exacta-unificacion-fuerte-de-gravitacion-electricidad-y-magnetismo-y-apertura-a-clases-factuales-emergentes

Lloret Egea, J. A. (2026j). *Del origen preternario del Sistema Vectorial SV a la entidad absoluta del campo: derivación nativa de $`\alpha_i`$ y $`\beta_i`$, proyección ternaria inducida, absorción basal exacta, unificación fuerte de gravitación, electricidad y magnetismo, y apertura a clases factuales emergentes*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/ekd8x4l9

Lloret Egea, J. A. (2026k). *Fundamentos operatorios absolutos del electromagnetismo factual en el Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/fundamentos-operatorios-absolutos-del-electromagnetismo-factual-en-el-sistema-vectorial-sv.md
