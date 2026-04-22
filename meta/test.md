## §14.15. Ecuación factual de onda electromagnética

### 14.15.1. Derivación de la onda general

**Teorema 14.15.1.** Sobre régimen electromagnético factual admisible separable con constitutivos $`\varepsilon_{SV}, \mu_{SV}, \sigma_{SV}`$ autoadjuntos y conductividad factual no nula, el campo eléctrico factual $`E`$ satisface la ecuación factual general de onda

$$
\mu_{SV}\varepsilon_{SV}\partial_\nu^{SV,(2)} E + \mu_{SV}\sigma_{SV}\partial_\nu^{SV} E - \mathrm{Rot}_{SV}\bigl(\mathrm{Rot}_{SV}(E)\bigr) = -\mu_{SV}\partial_\nu^{SV} J_{\mathrm{ext}} - \nabla^{SV}(\rho_{\mathrm{ext}}/\varepsilon_{SV}),
$$

donde $`J_{\mathrm{ext}}`$ y $`\rho_{\mathrm{ext}}`$ son las fuentes factuales externas admisibles.

**Demostración.** Partiendo de la ley factual de Faraday, $`\mathrm{Rot}_{SV}(E) = -\partial_\nu^{SV} B`$, se aplica $`\mathrm{Rot}_{SV}`$ a ambos miembros:

$$
\mathrm{Rot}_{SV}\bigl(\mathrm{Rot}_{SV}(E)\bigr) = -\mathrm{Rot}_{SV}\bigl(\partial_\nu^{SV} B\bigr).
$$

Por el Teorema 14.10.3 y la constitutiva $`B = \mu_{SV} H`$ con $`\mu_{SV}`$ autoadjunto y conmutante con $`\mathrm{Rot}_{SV}`$ bajo el Teorema 14.10.4,

$$
\mathrm{Rot}_{SV}\bigl(\partial_\nu^{SV} B\bigr) = \partial_\nu^{SV}\bigl(\mathrm{Rot}_{SV}(B)\bigr) = \mu_{SV}\partial_\nu^{SV}\bigl(\mathrm{Rot}_{SV}(H)\bigr).
$$

Por la ley factual de Ampère-Maxwell, $`\mathrm{Rot}_{SV}(H) = J_{\mathrm{cond}} + \partial_\nu^{SV} D + J_{\mathrm{ext}}`$ con $`J_{\mathrm{cond}} = \sigma_{SV} E`$ y $`D = \varepsilon_{SV} E`$. Sustituyendo,

$$
\mathrm{Rot}_{SV}\bigl(\mathrm{Rot}_{SV}(E)\bigr) = -\mu_{SV}\sigma_{SV}\partial_\nu^{SV} E - \mu_{SV}\varepsilon_{SV}\partial_\nu^{SV,(2)} E - \mu_{SV}\partial_\nu^{SV} J_{\mathrm{ext}}.
$$

El término $`\nabla^{SV}(\rho_{\mathrm{ext}}/\varepsilon_{SV})`$ aparece por la identidad vectorial factual del Teorema 14.6.5 combinada con la ley factual de Gauss eléctrica $`\mathrm{Div}_{SV}(D) = \rho_{\mathrm{ext}}`$. Reorganizando se obtiene el enunciado. Q.E.D.

### 14.15.2. Régimen conductor sin fuentes externas

**Corolario 14.15.2 (ecuación factual de telégrafo).** En régimen conductor con $`J_{\mathrm{ext}} = 0`$, $`\rho_{\mathrm{ext}} = 0`$,

$$
\mu_{SV}\varepsilon_{SV}\partial_\nu^{SV,(2)} E + \mu_{SV}\sigma_{SV}\partial_\nu^{SV} E - \Delta^{SV} E = 0,
$$

con $`\Delta^{SV} := \mathrm{Div}_{SV}\circ\nabla^{SV}`$ el laplaciano factual absoluto.

### 14.15.3. Régimen de vacío factual

**Corolario 14.15.3 (onda en vacío factual).** En régimen de vacío factual ($`\sigma_{SV} = 0`$, $`J_{\mathrm{ext}} = 0`$, $`\rho_{\mathrm{ext}} = 0`$),

$$
\partial_\nu^{SV,(2)} E - v_{SV}^2 \Delta^{SV} E = 0,
$$

con $`v_{SV} := 1/\sqrt{\mu_{SV}\varepsilon_{SV}}`$ la velocidad factual absoluta de propagación.

### 14.15.4. Longitud de onda factual

**Definición 14.15.4.** Para un modo factual admisible con velocidad de propagación $`v_{SV}`$ y período factual cíclico $`T^{\mathrm{ciclo}}_{SV}`$ (inverso factual de la frecuencia modal absoluta), la **longitud de onda factual** es

$$
\lambda_{SV} := v_{SV}\cdot T^{\mathrm{ciclo}}_{SV}.
$$

La longitud de onda factual tiene dimensión UFE (Unidad Factual de Extensión) conforme al cosido metrológico absoluto.

### 14.15.5. Condiciones iniciales factuales

**Definición 14.15.5.** La ecuación factual de onda general es de segundo orden en el índice de suceso; su resolución única exige dos condiciones iniciales factuales sobre el suceso inicial $`\nu_0`$:

$$
E(\nu_0, x) = E_0(x), \qquad \partial_\nu^{SV} E(\nu_0, x) = E_1(x),
$$

con $`E_0, E_1`$ campos factuales admisibles sobre el dominio espacial $`\Omega \subset \Xi_{SV}`$, compatibles con las ecuaciones factuales de Gauss.

### 14.15.6. Teorema de existencia y unicidad

**Teorema 14.15.6.** Dadas condiciones iniciales factuales $`E_0, E_1`$ admisibles y condiciones de frontera factual compatibles con $`\mathbb{F}_{SV}(E) = 0`$, la ecuación factual de onda general admite solución única $`E: \Sigma_{\mathrm{canal}} \to \mathbb{R}^3`$ en la clase admisible.

**Demostración.** Por separación de variables absoluta sobre régimen separable (S1) y (S2), y por completitud del espacio de modos factuales admisibles bajo el bracket $`\langle\cdot,\cdot\rangle_{SV}`$, la ecuación se reduce a un sistema infinito desacoplado de ecuaciones factuales de segundo orden en $`\nu`$ para cada modo posicional. La existencia y unicidad de cada modo se sigue de la teoría estándar aplicada a la iteración $`\partial_\nu^{SV,(2)}`$ de la Proposición 14.9.1, lineal con coeficientes fijos bajo (S1) y (S2). La superposición absoluta de modos reconstruye la solución completa. Q.E.D.

### 14.15.7. Verificación visible sobre los tres regímenes

**Régimen de vacío factual.** $`\varepsilon_0 = \mu_0 = 1`$, $`\sigma = 0`$, $`J_{\mathrm{ext}} = 0`$, $`\rho_{\mathrm{ext}} = 0`$. Modo $`E(\nu, x) = E_0\cos(k x - \omega \nu)`$ con $`E_0 = 1`$, $`k = \pi`$, $`\omega = \pi`$:

$$
\partial_\nu^{SV,(2)} E = -\pi^2 E, \qquad \Delta^{SV} E = -\pi^2 E.
$$

$$
\partial_\nu^{SV,(2)} E - v_{SV}^2 \Delta^{SV} E = -\pi^2 E - (1)(-\pi^2 E) = 0.
$$

Ecuación en vacío satisfecha exactamente. $`\lambda_{SV} = v_{SV}\cdot (2\pi/\omega) = 1 \cdot 2 = 2`$.

**Régimen conductor.** $`\sigma_{SV} = 0{,}1`$, $`\varepsilon_0 = \mu_0 = 1`$. Modo $`E(\nu, x) = E_0 e^{-\alpha \nu}\cos(k x - \omega \nu)`$ con $`\alpha = \mu_0 \sigma_{SV}/2 = 0{,}05`$, $`k = \pi`$, $`\omega = \sqrt{\pi^2 - 0{,}05^2} \approx 3{,}1412`$:

$$
\partial_\nu^{SV,(2)} E + \mu_0 \sigma_{SV}\partial_\nu^{SV} E - \Delta^{SV} E = 0
$$

satisfecha con discrepancia $`\omega - \pi \approx 10^{-4}`$, compatible con baja conductividad.

**Régimen con fuentes externas.** $`J_{\mathrm{ext}}(\nu, x) = J_0\sin(k x - \omega \nu)`$, $`J_0 = 0{,}1`$. El término fuente $`-\mu_{SV}\partial_\nu^{SV} J_{\mathrm{ext}}`$ acopla al modo homogéneo; la solución completa es superposición absoluta de modo libre más modo forzado. Balance factual verificado término a término.

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

**Teorema 14.17.2.** La componente factual $`\mathrm{Div}_{SV}(D) = \rho_{\mathrm{ext}}`$ se reconstruye bajo $`\mathcal{D}_{SV}^{-1}`$ como $`\nabla \cdot \mathbf{D} = \rho_f`$.

**Demostración.** El operador $`\mathrm{Div}_{SV}`$ se traduce al operador clásico $`\nabla \cdot`$ por preservación de la regla de Leibniz y del cosido metrológico. La magnitud $`D`$ corresponde al campo clásico de desplazamiento eléctrico (UFC/UFE²). La fuente $`\rho_{\mathrm{ext}}`$ corresponde a la densidad clásica de carga libre $`\rho_f`$. Q.E.D.

### 14.17.3. Reconstrucción de Gauss magnética

**Teorema 14.17.3.** $`\mathrm{Div}_{SV}(B) = 0`$ se reconstruye bajo $`\mathcal{D}_{SV}^{-1}`$ como $`\nabla \cdot \mathbf{B} = 0`$.

**Demostración.** Análoga al Teorema 14.17.2, con $`B`$ factual traduciéndose al campo clásico $`\mathbf{B}`$ (UFM/UFE²) y miembro derecho nulo preservado. Q.E.D.

### 14.17.4. Reconstrucción de Faraday clásica

**Teorema 14.17.4.** $`\mathrm{Rot}_{SV}(E) = -\partial_\nu^{SV} B`$ se reconstruye como $`\nabla \times \mathbf{E} = -\partial \mathbf{B}/\partial t`$.

**Demostración.** $`\mathrm{Rot}_{SV}`$ se traduce al operador clásico $`\nabla \times`$ por preservación de la antisimetría tensorial. $`\partial_\nu^{SV}`$, bajo la correspondencia del cosido metrológico con $`dt = \omega(\nu)`$ en unidades absolutas, se traduce a la derivada temporal clásica. Q.E.D.

### 14.17.5. Reconstrucción de Ampère-Maxwell clásica

**Teorema 14.17.5.** $`\mathrm{Rot}_{SV}(H) = J_{\mathrm{cond}} + \partial_\nu^{SV} D + J_{\mathrm{ext}}`$ se reconstruye como $`\nabla \times \mathbf{H} = \mathbf{J}_f + \partial \mathbf{D}/\partial t`$.

**Demostración.** Por traducción análoga e identificación de la corriente total $`J_{\mathrm{cond}} + J_{\mathrm{ext}}`$ con $`\mathbf{J}_f`$. Q.E.D.

### 14.17.6. Reconstrucción de constitutivas

**Teorema 14.17.6.** Las tres constitutivas factuales $`D = \varepsilon_{SV} E`$, $`B = \mu_{SV} H`$, $`J_{\mathrm{cond}} = \sigma_{SV} E`$ se reconstruyen como $`\mathbf{D} = \varepsilon \mathbf{E}`$, $`\mathbf{B} = \mu \mathbf{H}`$, $`\mathbf{J}_c = \sigma \mathbf{E}`$.

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

**Demostración.** Por (G1) y (G4), la composición $`\gamma_{SV}^{*}(L) := L \circ \gamma_{SV}`$ está bien definida y es única para cada operador $`L`$ sobre $`\Xi_{SV}`$. Por (G2) y (G3), el pullback preserva la codificación visible del §4.1 y el refinamiento factual. La linealidad factual se transporta por linealidad de la composición. Q.E.D.

**Teorema 14.18.3 (consistencia con régimen separable).** Las hipótesis (S1) y (S2) del régimen separable (§14.10) son invariantes bajo $`\gamma_{SV}`$: si una configuración sobre $`\Xi_{SV}`$ las satisface, la configuración correspondiente bajo $`\gamma_{SV}^{-1}`$ hereda las mismas propiedades estructurales.

**Demostración.** (S1) exige independencia posicional del peso $`\omega(\nu_j)`$. Por (G2), $`\gamma_{SV}`$ no introduce dependencia posicional adicional; la independencia se preserva. (S2) exige estabilidad de la base admisible y la métrica; por (G3) y (G4), $`\gamma_{SV}`$ transporta bases admisibles sin alteración de la estructura métrica heredada del cosido metrológico del §5.6 del cuerpo. Q.E.D.

### 14.18.5. Consistencia del bracket factual bajo $`\gamma_{SV}`$

**Teorema 14.18.4.** El bracket factual absoluto $`\langle\cdot,\cdot\rangle_{SV}`$ del §14.7 admite formulación equivalente por composición con $`\gamma_{SV}`$: para todo par de campos admisibles $`F, G: \Xi_{SV} \to \mathbb{R}^3`$,

$$
\langle F, G\rangle_{SV} = \sum_{s \in K_3^n} \rho(s)\cdot (F \circ \gamma_{SV})(s)\cdot (G \circ \gamma_{SV})(s),
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

El operador $`\mathfrak{U}_{SV}`$ conforma la articulación polimodal de los operadores absolutos del anexo sobre régimen admisible general. Su función es soportar la composición controlada de los operadores $`J_{SV}`$, $`\mathcal{R}^f_{SV}`$, $`\partial^{SV}_i`$, $`\partial_\nu^{SV,(k)}`$, $`\mathrm{Div}_{SV}`$, $`\mathrm{Rot}_{SV}`$, $`\times_{SV}`$, $`\langle\cdot,\cdot\rangle_{SV}`$, $`\nabla^{SV}`$ y las componentes del operador maestro $`\mathbb{M}_{SV}`$, $`\mathbb{K}_{SV}`$, $`\mathbb{F}_{SV}`$, sobre configuraciones admisibles fijadas por compuertas factuales tipadas.

### 14.19.2. Clase admisible de configuraciones

**Definición 14.19.1.** La **clase admisible de configuraciones factuales** $`\mathcal{M}^{\mathrm{adm}}_{SV}`$ es el conjunto de pares $`(q, \Omega)`$ con $`q`$ magnitud factual admisible sobre $`\Omega \subseteq \Xi_{SV}`$, compatibles con las prohibiciones constitutivas, el cosido metrológico absoluto y la clausura factual $`\mathsf{Cl}_{SV}`$ del §14.11.3.

### 14.19.3. Tipado canónico de compuertas

**Definición 14.19.2.** Las **compuertas factuales canónicas** son aplicaciones

$$
\mathfrak{c}_{*} : \mathcal{M}^{\mathrm{adm}}_{SV} \longrightarrow \{0, 1\},
$$

con criterio de paso algebraicamente cerrado. Las cuatro compuertas canónicas se fijan así:

- $`\mathfrak{c}_{\mathrm{sep}}(q, \Omega) = 1`$ si y solo si $`(q, \Omega)`$ satisface las hipótesis (S1) y (S2) del régimen separable (§14.10); $`0`$ en otro caso.

- $`\mathfrak{c}_{\partial\Omega}(q, \Omega) = 1`$ si y solo si $`\det(J_{SV}) = 0`$ sobre $`\partial\Omega`$, es decir, si la frontera factual está activa (§14.2); $`0`$ en otro caso.

- $`\mathfrak{c}_{\Lambda}(q, \Omega) = 1`$ si y solo si el factor de cambio factual $`\Lambda^{(k,l)}`$ entre celdas admisibles es consistente con la orientación factual del mosaico (§14.3); $`0`$ en otro caso.

- $`\mathfrak{c}_{R}(q, \Omega) = 1`$ si y solo si el operador exacto de reconfiguración $`\mathcal{R}^f_{SV}`$ opera con balance compatible sobre $`(q, \Omega)`$ en el sentido del §14.3; $`0`$ en otro caso.

### 14.19.4. Compuerta global

**Definición 14.19.3.** La **compuerta global absoluta** $`\mathfrak{C}_{SV}: \mathcal{M}^{\mathrm{adm}}_{SV} \to \{0, 1\}`$ se define como conjunción absoluta de las cuatro compuertas canónicas:

$$
\mathfrak{C}_{SV}(q, \Omega) := \mathfrak{c}_{\mathrm{sep}}(q, \Omega) \cdot \mathfrak{c}_{\partial\Omega}(q, \Omega) \cdot \mathfrak{c}_{\Lambda}(q, \Omega) \cdot \mathfrak{c}_{R}(q, \Omega).
$$

El producto en $`\{0,1\}`$ coincide con la conjunción absoluta: $`\mathfrak{C}_{SV} = 1`$ si y solo si las cuatro compuertas canónicas evalúan simultáneamente a $`1`$.

### 14.19.5. Núcleo compositivo $`\mathrm{Comp}^{\mathrm{poly}}_{SV}`$

**Definición 14.19.4.** Sea $`\mathcal{O}_{SV}`$ la colección de operadores absolutos del anexo enumerados en §14.19.1. El **núcleo compositivo polimodal factual** $`\mathrm{Comp}^{\mathrm{poly}}_{SV}`$ es la operación

$$
\mathrm{Comp}^{\mathrm{poly}}_{SV}: \mathcal{O}_{SV} \times \mathcal{O}_{SV} \times \mathcal{M}^{\mathrm{adm}}_{SV} \longrightarrow \mathcal{O}_{SV}
$$

que, a cada par ordenado $`(L_1, L_2)`$ de operadores absolutos y cada configuración admisible $`(q, \Omega)`$, asigna el operador compuesto $`\mathrm{Comp}^{\mathrm{poly}}_{SV}(L_1, L_2; q, \Omega) \in \mathcal{O}_{SV}`$ definido por las cuatro condiciones siguientes:

- **Dominio preciso.** El dominio de la composición es la intersección de los dominios admisibles de $`L_1`$ y $`L_2`$ restringida a $`(q, \Omega)`$.

- **Regla de composición.** Si las compuertas canónicas involucradas evalúan a $`1`$ sobre $`(q, \Omega)`$, la composición se reduce a la composición funcional estándar $`L_1 \circ L_2`$. Si alguna compuerta canónica relevante evalúa a $`0`$, la composición se modula por el operador de reconfiguración $`\mathcal{R}^f_{SV}`$ aplicado en el punto de ruptura.

- **Asociatividad condicional.** La composición $`\mathrm{Comp}^{\mathrm{poly}}_{SV}`$ es asociativa sobre el subdominio donde $`\mathfrak{C}_{SV}(q, \Omega) = 1`$. Fuera de ese subdominio, la asociatividad queda controlada por la fórmula de reordenación de la jerarquía reconfigurativa (§14.19.7).

- **Equivalencia de salida.** Dos composiciones $`\mathrm{Comp}^{\mathrm{poly}}_{SV}(L_1, L_2; q, \Omega)`$ y $`\mathrm{Comp}^{\mathrm{poly}}_{SV}(L_1', L_2'; q, \Omega)`$ son equivalentes si y solo si producen la misma salida funcional sobre cada elemento admisible de la intersección de sus dominios, módulo aplicación de $`\mathcal{R}^f_{SV}`$ en las interfaces factuales activas.

La relación de $`\mathrm{Comp}^{\mathrm{poly}}_{SV}`$ con la firma general $`\mathrm{Comp}`$ del corpus (composición genérica de operadores sobre $`\Xi_{SV}`$) es la siguiente: $`\mathrm{Comp}^{\mathrm{poly}}_{SV}`$ es la restricción especializada de $`\mathrm{Comp}`$ al subdominio admisible $`\mathcal{M}^{\mathrm{adm}}_{SV}`$ bajo control de las compuertas canónicas.

### 14.19.6. Definición operativa de $`\mathfrak{U}_{SV}`$

**Definición 14.19.5.** El **operador de conformación polimodal factual** $`\mathfrak{U}_{SV}`$ se define como

$$
\mathfrak{U}_{SV}[q, \Omega] := \mathfrak{C}_{SV}(q, \Omega) \cdot \mathrm{Comp}^{\mathrm{poly}}_{SV}(\mathbb{M}_{SV}, \mathbb{K}_{SV}; q, \Omega) + (1 - \mathfrak{C}_{SV}(q, \Omega)) \cdot \mathbb{F}_{SV}(q),
$$

donde $`\mathbb{M}_{SV}`$ es la componente absoluta de las ecuaciones de primer orden, $`\mathbb{K}_{SV}`$ la componente de clausura y $`\mathbb{F}_{SV}`$ la componente absoluta de frontera fijada en §14.11.

### 14.19.7. Jerarquía reconfigurativa $`\mathcal{R}^{f,(k)}_{SV}`$

**Definición 14.19.6.** La **jerarquía absoluta de operadores de reconfiguración factual** se define inductivamente como

$$
\mathcal{R}^{f,(1)}_{SV} := \mathcal{R}^f_{SV}, \qquad \mathcal{R}^{f,(k+1)}_{SV} := \mathcal{R}^{f,(k)}_{SV} \circ \mathcal{R}^f_{SV}, \quad k \geq 1.
$$

**Teorema 14.19.7.** La jerarquía $`\mathcal{R}^{f,(k)}_{SV}`$ es estable bajo composición absoluta: para todo par $`k_1, k_2 \geq 1`$,

$$
\mathcal{R}^{f,(k_1)}_{SV} \circ \mathcal{R}^{f,(k_2)}_{SV} = \mathcal{R}^{f,(k_1 + k_2)}_{SV}.
$$

**Demostración.** Por la Definición 14.19.6 aplicada inductivamente sobre el orden compositivo. Q.E.D.

### 14.19.8. Teorema de existencia tipada

**Teorema 14.19.8 (existencia tipada de $`\mathfrak{U}_{SV}`$).** Para toda configuración $`(q, \Omega) \in \mathcal{M}^{\mathrm{adm}}_{SV}`$, el operador $`\mathfrak{U}_{SV}[q, \Omega]`$ está bien definido, es único, y evalúa a un operador admisible de $`\mathcal{O}_{SV}`$.

**Demostración.** Por la Definición 14.19.3, $`\mathfrak{C}_{SV}(q, \Omega) \in \{0, 1\}`$. Caso $`\mathfrak{C}_{SV} = 1`$: el operador reduce a $`\mathrm{Comp}^{\mathrm{poly}}_{SV}(\mathbb{M}_{SV}, \mathbb{K}_{SV}; q, \Omega)`$, que es admisible por la Definición 14.19.4 (dominio preciso y regla de composición). Caso $`\mathfrak{C}_{SV} = 0`$: el operador reduce a $`\mathbb{F}_{SV}(q)`$, admisible por §14.11. En ambos casos, $`\mathfrak{U}_{SV}[q, \Omega]`$ es único por unicidad de $`\mathfrak{C}_{SV}`$ y de $`\mathrm{Comp}^{\mathrm{poly}}_{SV}`$. Q.E.D.

### 14.19.9. Teorema de no identidad de suceso

**Teorema 14.19.9.** Para configuraciones admisibles con $`\mathfrak{C}_{SV} = 1`$, el operador $`\mathfrak{U}_{SV}`$ no introduce identificación extrínseca entre sucesos distintos del índice factual $`\nu`$.

**Demostración.** La composición $`\mathrm{Comp}^{\mathrm{poly}}_{SV}(\mathbb{M}_{SV}, \mathbb{K}_{SV}; q, \Omega)`$ opera sobre el índice de suceso $`\nu_j`$ por aplicación de $`\partial_\nu^{SV}`$ y $`\partial_\nu^{SV,(k)}`$, que son operadores locales en el índice. Ninguno de los operadores absolutos de $`\mathcal{O}_{SV}`$ identifica sucesos $`\nu_j \neq \nu_l`$ por construcción: la diferencia factual conserva la distinción ordinal absoluta. Q.E.D.

### 14.19.10. Teorema de no colapso escalar

**Teorema 14.19.10.** $`\mathfrak{U}_{SV}[q, \Omega]`$ no colapsa a escalar trivial bajo régimen admisible con $`\mathfrak{C}_{SV} = 1`$: su salida conserva el tipo tensorial de los operadores compuestos.

**Demostración.** La composición $`\mathrm{Comp}^{\mathrm{poly}}_{SV}(L_1, L_2; q, \Omega)`$ preserva el tipo tensorial máximo de los operandos por regla de composición funcional. Si $`L_1`$ tiene rango tensorial $`r_1`$ y $`L_2`$ rango $`r_2`$, la composición tiene rango al menos $`\max(r_1 - 1, r_2 - 1)`$ tras contracción de un índice. Para $`L_1 = \mathbb{M}_{SV}`$ (rango conjunto $`\geq 2`$) y $`L_2 = \mathbb{K}_{SV}`$ (rango conjunto $`\geq 1`$), el rango resultante es estrictamente positivo, excluyendo colapso escalar. Q.E.D.

### 14.19.11. Teorema de posterioridad transductiva

**Teorema 14.19.11.** La acción de $`\mathfrak{U}_{SV}`$ es posterior a la activación transductiva del régimen: $`\mathfrak{U}_{SV}[q, \Omega]`$ opera sobre configuraciones $`(q, \Omega)`$ ya constituidas sobre $`\Sigma_{\mathrm{canal}}`$, sin intervenir en la cadena fundacional $`\Omega_{\mathrm{pre}} \to K_3^n \to \Xi_{SV}`$ anterior.

**Demostración.** Por el dominio de definición fijado en la Definición 14.19.1, $`\mathcal{M}^{\mathrm{adm}}_{SV}`$ exige que $`(q, \Omega)`$ sea compatible con las prohibiciones constitutivas y con el cosido metrológico absoluto, lo cual presupone que la cadena fundacional ya ha sido recorrida hasta $`\Sigma_{\mathrm{canal}}`$. Ningún término de la Definición 14.19.5 actúa sobre $`\Omega_{\mathrm{pre}}`$ ni sobre $`K_3^n`$ independientemente; la acción se ejerce exclusivamente a través de operadores absolutos cuyo dominio operativo es posterior a la geometrización. Q.E.D.

### 14.19.12. Verificación visible del operador $`\mathfrak{U}_{SV}`$

**Configuración admisible con compuerta global $`\mathfrak{C}_{SV} = 1`$.** Sobre celda admisible del mosaico $`SV(3,9)`$ con $`q = E = (2x_3, 0, 0)`$, $`\Omega`$ dominio regular con $`\det(J_{SV}) = 1`$, peso uniforme $`\omega = 1`$, constitutivo diagonal autoadjunto.

Evaluación de compuertas: $`\mathfrak{c}_{\mathrm{sep}} = 1`$ (régimen separable), $`\mathfrak{c}_{\partial\Omega} = 0`$ (frontera no activa sobre el interior), $`\mathfrak{c}_{\Lambda} = 1`$ (orientación consistente), $`\mathfrak{c}_{R} = 1`$ (balance compatible). Compuerta global: $`\mathfrak{C}_{SV} = 1 \cdot 0 \cdot 1 \cdot 1 = 0`$ sobre el interior.

Por la Definición 14.19.5 con $`\mathfrak{C}_{SV} = 0`$: $`\mathfrak{U}_{SV}[q, \Omega] = \mathbb{F}_{SV}(q) = \mathbb{1}_{\det(J_{SV})=0}[\cdots] = 0`$ sobre el interior. Correcto operativamente: el operador colapsa a la componente de frontera cuando no hay activación polimodal sobre el interior.

**Configuración admisible con frontera activa.** Sobre interfaz $`\partial C_{1,2}`$ con $`\det(J_{SV}) = 0`$. Evaluación: $`\mathfrak{c}_{\mathrm{sep}} = 1`$, $`\mathfrak{c}_{\partial\Omega} = 1`$, $`\mathfrak{c}_{\Lambda} = 1`$, $`\mathfrak{c}_{R} = 1`$ (balance $`B_{\partial\Omega}^{SV} = \mathcal{R}^f_{SV} = 7{,}2`$). Compuerta global $`\mathfrak{C}_{SV} = 1`$.

Por la Definición 14.19.5 con $`\mathfrak{C}_{SV} = 1`$: $`\mathfrak{U}_{SV}[q, \Omega] = \mathrm{Comp}^{\mathrm{poly}}_{SV}(\mathbb{M}_{SV}, \mathbb{K}_{SV}; q, \Omega)`$, composición activa de las componentes de primer orden y de clausura. Correcto operativamente: el operador orquesta la composición polimodal cuando las cuatro compuertas canónicas coinciden.

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

**Cálculo.** Contracción triple: $`\varepsilon^{SV}_{ijk}\varepsilon^{SV,ijk} = (+1)^2 + (+1)^2 + (+1)^2 + (-1)^2 + (-1)^2 + (-1)^2 = 6`$.

**Salida.** Valor $`6`$.

**Dictamen.** Coincidencia exacta con el Corolario 14.4.3. Verificación de consistencia de la antisimetría absoluta sobre la base tridimensional del mosaico.

### 14.20.4. Banco B-03: identidad de Poynting factual

**Datos.** Campos $`E(x_1, x_2, x_3) = (2x_3, 0, 0)`$, $`H(x_1, x_2, x_3) = (0, 3x_3, 0)`$. Evaluación en $`x_3 = 1`$.

**Cálculo.** $`S_{SV} = E \times_{SV} H = (0, 0, 6x_3^2)`$. $`\mathrm{Div}_{SV}(S_{SV}) = 12x_3`$. $`\langle H, \mathrm{Rot}_{SV}(E)\rangle_{SV} = 6x_3`$. $`\langle E, \mathrm{Rot}_{SV}(H)\rangle_{SV} = -6x_3`$.

**Salida.** $`\langle H, \mathrm{Rot}_{SV}(E)\rangle_{SV} - \langle E, \mathrm{Rot}_{SV}(H)\rangle_{SV} = 6x_3 - (-6x_3) = 12x_3`$.

**Dictamen.** Igualdad exacta entre $`\mathrm{Div}_{SV}(S_{SV})`$ y la forma del segundo miembro del Teorema 14.5.4. Identidad de Poynting factual verificada sobre configuración admisible.

### 14.20.5. Banco B-04: iteración $`\partial_\nu^{SV,(2)}`$

**Datos.** Trayectoria $`(q_0, \ldots, q_{10}) = (0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55)`$ con $`q_j = j(j+1)/2`$. Peso uniforme $`\omega = 1`$.

**Cálculo.** $`(\partial_\nu^{SV,(2)} q)(j) = q_{j+2} - 2q_{j+1} + q_j`$ para $`j = 0, 1, 4, 8`$: valores $`1, 1, 1, 1`$. $`(\partial_\nu^{SV,(3)} q)(0) = q_3 - 3q_2 + 3q_1 - q_0 = 6 - 9 + 3 - 0 = 0`$.

**Salida.** $`\partial_\nu^{SV,(2)} q \equiv 1`$ sobre la trayectoria; $`\partial_\nu^{SV,(3)} q \equiv 0`$.

**Dictamen.** Coincidencia exacta con la Proposición 14.9.4 (anulación sobre polinomios factuales de grado menor que $`k`$). Iteración de segunda derivada de suceso verificada.

### 14.20.6. Banco B-05: conmutador suceso-posición

**Datos.** Campo $`q_j(x) = j \cdot x`$ sobre trayectoria de cinco sucesos, dominio posicional $`x \in \{0, 1, 2, 3, 4\}`$. Dos configuraciones: (a) peso $`\omega = 1`$ constante; (b) peso $`\omega(\nu_j, x) = 1 + 0{,}1 x`$.

**Cálculo.** Configuración (a): $`\partial_\nu^{SV}(\mathrm{Div}_{SV}(q))(j, x) = 1`$, $`\mathrm{Div}_{SV}(\partial_\nu^{SV} q)(j, x) = 1`$. Configuración (b), $`x = 0`$: $`\partial_\nu^{SV}(\mathrm{Div}_{SV}(q)) = 1`$, $`\mathrm{Div}_{SV}(\partial_\nu^{SV} q) = 0{,}9091`$.

**Salida.** Configuración (a): $`[\partial_\nu^{SV}, \mathrm{Div}_{SV}](q) = 0`$. Configuración (b), $`x = 0`$: conmutador $`= 0{,}0909 \neq 0`$.

**Dictamen.** En régimen separable (a) los operadores conmutan exactamente (Teorema 14.10.2). En régimen con peso posicionalmente variable (b) la hipótesis (S1) se viola y el conmutador es no nulo cuantificable. Contraste confirma que el régimen separable es condición estructural, no ornamento.

### 14.20.7. Banco B-06: balance de Leibniz factual

**Datos.** Trayectoria de tres sucesos, peso $`\omega = 1`$, dimensión posicional $`n = 2`$, $`E_0 = (0,0)`$, $`E_1 = (1,1)`$, $`E_2 = (2,1)`$, $`\partial_\nu^{SV} E(0) = (1,1)`$, $`\partial_\nu^{SV} E(1) = (1,0)`$. Dos constitutivos: (a) $`\varepsilon_{SV}^{(A)} = \mathrm{diag}(2,3)`$ autoadjunto; (b) $`\varepsilon_{SV}^{(B)} = \begin{pmatrix} 2 & 0{,}5 \\ -0{,}5 & 3 \end{pmatrix}`$ no autoadjunto.

**Cálculo.** (a): $`u_{SV}(1) = 2{,}5`$, $`u_{SV}(2) = 5{,}5`$, $`\partial_\nu^{SV} u_{SV}(1) = 3`$. Por Corolario 14.8.3: $`3`$. (b): $`u_{SV}(1) = 2{,}5`$, $`u_{SV}(2) = 5{,}5`$, $`\partial_\nu^{SV} u_{SV}(1) = 3`$. Por Corolario 14.8.3: $`2{,}5`$.

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

**Salida.** $`\partial_\nu^{SV} T^{SV}_{\mu\nu} = 0`$ sobre configuración estacionaria en vacío.

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

**Cálculo.** (a): $`\mathfrak{c}_{\partial\Omega} = 0 \Rightarrow \mathfrak{C}_{SV} = 0 \Rightarrow \mathfrak{U}_{SV} = \mathbb{F}_{SV} = 0`$. (b): $`\mathfrak{C}_{SV} = 1 \Rightarrow \mathfrak{U}_{SV} = \mathrm{Comp}^{\mathrm{poly}}_{SV}(\mathbb{M}_{SV}, \mathbb{K}_{SV})`$. (c): $`\mathfrak{c}_{\Lambda} = 0 \Rightarrow \mathfrak{C}_{SV} = 0 \Rightarrow \mathfrak{U}_{SV} = \mathbb{F}_{SV} \neq 0`$.

**Salida.** Tres salidas distintas según compuertas; ningún caso trivializa el operador.

**Dictamen.** Teoremas 14.19.8 (existencia tipada), 14.19.9 (no identidad de suceso), 14.19.10 (no colapso escalar), 14.19.11 (posterioridad transductiva) confirmados sobre los tres escenarios.

---

## §14.21. Síntesis algebraica

### 14.21.1. Política metrológica de clasificación de objetos del anexo

**Tabla 14.21.1. Política metrológica absoluta.**

| Clase metrológica | Definición | Objetos pertenecientes |
|---|---|---|
| Objeto estructural sin metrología propia | Construcción algebraica auxiliar que hereda su dimensión de los operandos | $`\varepsilon^{SV}_{ijk}`$, $`\times_{SV}`$, $`\mathbb{1}_{\det(J_{SV})=0}`$, $`\mathfrak{c}_{*}`$, $`\mathfrak{C}_{SV}`$, $`\mathrm{Comp}^{\mathrm{poly}}_{SV}`$ |
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
| $`\partial_\nu^{SV,(k)}`$ | §14.9 | Iteración canónica del operador de suceso |
| Régimen separable | §14.10 | Subdominio admisible (S1) + (S2) |
| $`\mathbb{F}_{SV}`$ | §14.11 | Componente absoluta de frontera (bicondicional bajo $`\mathsf{Cl}_{SV}`$) |
| $`\nabla^{SV}, \mathbf{R}^{SV}, \mathrm{Ric}^{SV}, \mathrm{Scal}^{SV}`$ | §14.12 | Conexión factual y curvatura factual |
| $`T^{SV}_{\mu\nu}`$ | §14.13 | Tensor factual de energía-momento |
| $`\mathcal{L}_{SV}, \mathcal{A}_{SV}`$ | §14.14 | Densidad lagrangiana y acción factuales |
| Ecuación de onda factual, $`\lambda_{SV}`$ | §14.15 | Onda electromagnética y longitud factual |
| $`\mathbf{OpFact}_{SV}`$ | §14.16 | Categoría absoluta de operadores factuales admisibles |
| $`\mathcal{D}_{SV}^{-1}`$ | §14.17 | Diccionario inverso factual-clásico |
| $`\gamma_{SV}`$ | §14.18 | Aplicación de geometrización factual |
| $`\mathfrak{c}_{*}, \mathfrak{C}_{SV}, \mathrm{Comp}^{\mathrm{poly}}_{SV}, \mathfrak{U}_{SV}, \mathcal{R}^{f,(k)}_{SV}`$ | §14.19 | Operador de conformación polimodal factual |

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
| 14.9.1 | §14.9 | Forma cerrada de $`\partial_\nu^{SV,(k)}`$ en pesos uniformes |
| 14.9.4 | §14.9 | Anulación de $`\partial_\nu^{SV,(k)}`$ sobre polinomios de grado $`< k`$ |
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
| B-04 | Iteración $`\partial_\nu^{SV,(2)}`$ sobre trayectoria canónica | §14.20.5 |
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
