# Fuerza, trabajo, calor, entalpía, temperatura, principios y fundamentos de la termodinámica y la correlación entre ellos en el SV

## Resumen

Se construye el dominio termodinámico factual del Sistema Vectorial SV como un régimen algebraico de sucesos, no temporal, trazable en ambos sentidos y cerrado por una única ecuación absoluta. El cierre parte del sustrato preternario de pares admisibles, pasa por la cadena factual canónica de irreversibilidad y fija, sin introducir semántica ajena al corpus, un fibrado termodinámico factual cuyas proyecciones recuperan trabajo, calor, fuerza, empuje, temperatura y entalpía como magnitudes derivadas. El documento determina explícitamente las proyecciones diferenciales directriz, residual y de indeterminación honesta; define la acumulación factual, el contenido interior, el contenido total y la lectura factual de frontera; y demuestra que la anulación de un defecto factual total es equivalente, simultáneamente, al balance factual del dominio, a la no decrecencia de la entropía factual, al cierre de fuerza y empuje, a la definición termométrica factual y a la descomposición interior–contorno de la entalpía factual. La ecuación absoluta del dominio queda así fijada como forma escalar nula, fibrosa por proyecciones, compatible con la disciplina semántica del SV y con la arquitectura de ecuación única ya asentada en otros dominios del corpus.

## Abstract

The factual thermodynamic domain of the Sistema Vectorial SV is constructed as an event-based, non-temporal algebraic regime, traceable in both directions and closed by a single absolute equation. The closure starts from the preternary substrate of admissible pairs, passes through the canonical factual chain of irreversibility, and fixes, without introducing semantics foreign to the corpus, a factual thermodynamic bundle whose projections recover work, heat, force, thrust, temperature and enthalpy as derived magnitudes. The document determines explicitly the directrix, residual and honest-indeterminacy differential projections; defines factual accumulation, interior content, total content and boundary factual reading; and proves that the vanishing of a total factual defect is simultaneously equivalent to factual balance, non-decrease of factual entropy, closure of force and thrust, factual thermometric definition and the interior–boundary decomposition of factual enthalpy. The absolute equation of the domain is thereby fixed as a scalar null form, fibrous by projections, compatible with the semantic discipline of the SV and with the single-equation architecture already established in other corpus domains.

## 1. Estatuto del dominio

El presente documento trata el dominio termodinámico factual del Sistema Vectorial SV en el rango estricto de cierre algebraico. Su objeto no es reformular la termodinámica heredada mediante sustitución terminológica, ni yuxtaponer a magnitudes clásicas una nueva notación. Su objeto es más severo: fijar un único régimen soberano del dominio y hacer que trabajo, calor, fuerza, empuje, temperatura y entalpía comparezcan sólo como proyecciones o lecturas derivadas de ese régimen.

El dominio queda sometido desde el arranque a cinco disciplinas constitutivas inseparables.

Primera, disciplina semántica: la terna canónica del SV es $K_3=\{0,1,U\}$ y el símbolo $U$ conserva su estatuto de indeterminación honesta. No equivale a probabilidad, no equivale a ausencia banal de dato y no autoriza clausura favorable por plausibilidad.

Segunda, disciplina de eventividad: el dominio se organiza sobre sucesos y sobre trayectorias de suceso. El tiempo soberano no es primitiva constitutiva.

Tercera, disciplina de trazabilidad: toda magnitud central del dominio debe admitir descenso hasta el sustrato preternario y ascenso desde él sin pérdida de control algebraico.

Cuarta, disciplina de suficiencia operatoria interna: el documento adopta como cuerpo vinculante el aparato operatorio ya fijado por el corpus y no introduce herramientas clásicas de mayor potencia allí donde el aparato factual del SV ya resulte suficiente.

Quinta, disciplina de clausura: ninguna pieza central puede quedar nombrada y suspendida; toda pieza central debe quedar definida, integrada y absorbida por la ecuación absoluta del dominio.

## 2. Sustrato semántico y suelo preternario

### 2.1. Terna canónica y proyección factual del estado

La terna canónica del sistema es

```math
K_3 = \{0,1,U\}.
```

Sobre una trayectoria factual admisible $\Gamma=(S_0,S_1,\dots,S_n)$, a cada paso $k\ge 1$ se asocia una lectura factual

```math
\chi_\Gamma(k) \in K_3.
```

Se introducen los indicadores ternarios

```math
\mathbf{1}_1(k), \qquad \mathbf{1}_0(k), \qquad \mathbf{1}_U(k),
```

caracterizados por

```math
\mathbf{1}_1(k)+\mathbf{1}_0(k)+\mathbf{1}_U(k)=1,
```

con

```math
\mathbf{1}_a(k)=1 \iff \chi_\Gamma(k)=a, \qquad a\in\{1,0,U\}.
```

Esta partición no añade un cuarto polo semántico. Descompone, dentro del propio documento, cualquier incremento factual según las tres lecturas legítimas del corpus.

### 2.2. Pares admisibles

El suelo del dominio es el sistema de pares admisibles

```math
(\alpha_i,\beta_i).
```

La notación es la canónica del corpus. Ninguna magnitud central del dominio puede recibir aquí un estatuto más originario.

### 2.3. Sesgo polar factual y activación

Sobre cada par admisible se definen el sesgo polar factual y la activación factual local por

```math
\delta_i := \beta_i - \alpha_i,
\qquad
 a_i := |\delta_i|.
```

La magnitud $\delta_i$ orienta la desviación factual entre los términos del par. La magnitud $a_i$ fija el espesor factual local de activación. Ambas forman el primer estrato derivado del suelo preternario.

### 2.4. Teorema de prioridad preternaria

**Teorema 2.4.1.** Ninguna magnitud central del dominio termodinámico factual precede al sistema $(\alpha_i,\beta_i)$.

**Demostración.** Toda pieza central del dominio comparece o bien como construcción directa sobre $(\delta_i,a_i)$, o bien como magnitud de la cadena factual de irreversibilidad, o bien como componente o proyección del fibrado termodinámico factual fijado en el apartado 6. En todos los casos el soporte originario sigue siendo el par admisible. Luego ninguna magnitud central precede a $(\alpha_i,\beta_i)$. Q.E.D.

## 3. Trayectoria factual y aritmética diferencial del dominio

### 3.1. Derivada de suceso

Para toda magnitud factual discreta $X(\Gamma,k)$ se define la derivada de suceso por

```math
D_\Gamma X(\Gamma,k) := X(\Gamma,k)-X(\Gamma,k-1),
\qquad k\ge 1.
```

La acumulación hasta el índice $n$ se fija por

```math
\Delta_\Gamma X(\Gamma,n) := \sum_{k=1}^{n} D_\Gamma X(\Gamma,k).
```

No se introduce aquí derivada temporal. Toda diferencia es diferencia factual de suceso.

### 3.2. Proyecciones diferenciales canónicas

La partición ternaria del estado induce tres proyecciones diferenciales sobre cualquier magnitud $X$:

```math
D_\Gamma^{dir}X(\Gamma,n)
:=
\sum_{k=1}^{n}\mathbf{1}_1(k)\,D_\Gamma X(\Gamma,k),
```

```math
D_\Gamma^{res}X(\Gamma,n)
:=
\sum_{k=1}^{n}\mathbf{1}_0(k)\,D_\Gamma X(\Gamma,k),
```

```math
D_\Gamma^{U}X(\Gamma,n)
:=
\sum_{k=1}^{n}\mathbf{1}_U(k)\,D_\Gamma X(\Gamma,k).
```

Se obtiene así la identidad de descomposición factual total:

```math
\Delta_\Gamma X
=
D_\Gamma^{dir}X + D_\Gamma^{res}X + D_\Gamma^{U}X.
```

Esta igualdad no es un comentario metodológico, sino una fórmula del dominio. Resuelve explícitamente la aritmética diferencial que el documento necesita para definir trabajo factual, calor factual y la contribución factual de no clausura.

### 3.3. Lema de exhaustividad diferencial

**Lema 3.3.1.** Para toda magnitud factual $X$, las tres proyecciones $D_\Gamma^{dir}X$, $D_\Gamma^{res}X$ y $D_\Gamma^{U}X$ agotan sin solapamiento su incremento total.

**Demostración.** La igualdad anterior se deduce de la partición ternaria de la unidad. Además, la exclusión mutua de los indicadores impide solapamiento en cada paso. Luego las tres proyecciones agotan y separan el incremento factual total de $X$. Q.E.D.

## 4. Cadena factual canónica de irreversibilidad

### 4.1. Cadena estratificada

La cadena factual canónica de irreversibilidad del dominio se fija por

```math
(\alpha_i,\beta_i)
\longrightarrow
(\delta_i,a_i)
\longrightarrow
H_{pre}
\longrightarrow
H_{K_3}
\longrightarrow
H_{\Xi}
\longrightarrow
H_{\Sigma_c}
\longrightarrow
H_{\Sigma_k}
\longrightarrow
H_{SV}.
```

El documento no acorta esta cadena ni suprime estratos intermedios. Cada estrato será tratado como absorción factual del anterior.

### 4.2. Dispersión preternaria

Se define la dispersión factual preternaria por

```math
H_{pre}(\Gamma,n)
:=
\sum_{k=1}^{n}\sum_i a_i(k).
```

Esta magnitud acumula activación factual antes de toda lectura ternaria inducida.

### 4.3. Transporte ternario inducido

Sea $\tau:K_3\to\mathbb{R}_{\ge 0}$ una lectura ternaria compatible con el corpus. Se define

```math
H_{K_3}(\Gamma,n)
:=
\sum_{k=1}^{n}\sum_i \tau\bigl(\chi_i(k)\bigr)\,a_i(k).
```

El transporte ternario no crea un estrato ajeno; reescribe la activación factual sobre la terna canónica.

### 4.4. Enriquecimiento canónico

Se fija el enriquecimiento factual por

```math
H_{\Xi}(\Gamma,n)
=
H_{K_3}(\Gamma,n)
+
\|\mathcal{J}_{\Gamma,SV}(n)\|_1
+
R_\Gamma(n).
```

Aquí $\mathcal{J}_{\Gamma,SV}$ es el jacobiano factual heredado del aparato operatorio absoluto y $R_\Gamma$ el residual factual del proceso. Ambos son piezas ya asentadas del corpus y, en el presente dominio, quedan absorbidos en la cadena de irreversibilidad.

### 4.5. Concentración y canalización

Se fijan las reorganizaciones canónicas

```math
H_{\Sigma_c}(\Gamma,n)
:=
C_{\Sigma}\bigl(H_{\Xi}(\Gamma,n)\bigr),
```

```math
H_{\Sigma_k}(\Gamma,n)
:=
K_{\Sigma}\bigl(H_{\Sigma_c}(\Gamma,n)\bigr).
```

La primera compacta concentración factual; la segunda fija canalización factual del régimen.

### 4.6. Entropía factual final

La forma final de irreversibilidad factual se define por

```math
H_{SV}(\Gamma,n)
:=
S_{\Sigma}\bigl(H_{\Sigma_k}(\Gamma,n)\bigr).
```

### 4.7. Teorema de absorción estratificada

**Teorema 4.7.1.** $H_{SV}$ absorbe ordenadamente la cadena factual previa sin colapsar sus estratos.

**Demostración.** $H_{pre}$ acumula activación factual; $H_{K_3}$ la transporta al plano ternario; $H_{\Xi}$ añade sensibilidad y residualidad; $H_{\Sigma_c}$ y $H_{\Sigma_k}$ reorganizan concentración y canalización. Si $H_{SV}$ no absorbiera de forma estratificada esas capas, el cierre factual del dominio sería un salto no auditable. Luego $H_{SV}$ es absorción estratificada factual. Q.E.D.

### 4.8. Teorema de irreversibilidad factual

**Teorema 4.8.1.** Para toda trayectoria factual admisible $\Gamma$ y cualesquiera índices $n_2\ge n_1$, se cumple

```math
H_{SV}(\Gamma,n_2)\ge H_{SV}(\Gamma,n_1).
```

**Demostración.** Cada estrato de la cadena anterior es construido como acumulación o reorganización no retractiva de la información factual heredada del estrato previo. La disciplina append-only del suceso excluye retrocesos que borren activación ya absorbida. En consecuencia, la composición estratificada no puede decrecer sobre una trayectoria admisible. Q.E.D.

### 4.9. Corolario diferencial

Para todo $n\ge 1$ se tiene

```math
D_\Gamma H_{SV}(\Gamma,n)\ge 0.
```

Y, por acumulación,

```math
\Delta_\Gamma H_{SV}(\Gamma,n)\ge 0.
```

## 5. Aparato operatorio heredado del SV

### 5.1. Estatuto

El dominio termodinámico factual no repropone el aparato operatorio del SV. Adopta como cuerpo heredado y vinculante el siguiente conjunto mínimo:

- flujo factual $\Phi_{SV}$;
- divergencia factual $Div_{SV}$;
- gradiente factual $\nabla^{SV}$;
- rotor factual vectorial $Rot_{SV}$;
- jacobiano factual $\mathcal{J}_{\Gamma,SV}$;
- frontera factual $\mathcal{B}_{\partial,SV}$;
- integrales factuales discretas de superficie y volumen.

### 5.2. Fórmulas canónicas heredadas

Se usan en el dominio las siguientes expresiones operativas:

```math
\Phi_{SV}(F;B)
=
\sum_j \sigma_j\,\langle F(B_j),n_{B_j}\rangle_{SV}\,\omega(B_j),
```

```math
Div_{SV}(F;C)\,\omega(C)
=
\Phi_{SV}(F;\partial C)-\mathcal{I}_{res}(F;C),
```

```math
\iint^{SV}_{\Sigma_{SV}} G
=
\sum_j \sigma_j\,G(B_j)\,\omega(B_j),
```

```math
\iiint^{SV}_{\mathcal{V}_{SV}} K
=
\sum_k K(C_k)\,\omega(C_k).
```

El rotor factual del presente documento se entiende en su lectura vectorial heredada del corpus electromagnético factual; no comparece aquí como 2-forma independiente.

### 5.3. Teorema de suficiencia operatoria interna

**Teorema 5.3.1.** El aparato anterior es suficiente para cerrar el dominio termodinámico factual sin introducir herramientas clásicas constitutivas de mayor potencia.

**Demostración.** El dominio exige balance de contenido, frontera, residualidad, gradiente, rotor y sensibilidad jacobiana. Todas esas piezas comparecen ya en el cuerpo operatorio heredado. Luego no procede introducir aparato externo más potente como fundamento. Q.E.D.

## 6. Fibrado termodinámico factual y magnitudes madre

### 6.1. Fibra factual del dominio

Sobre cada par $(\Gamma,n)$ se define la fibra factual del dominio por

```math
\mathcal{F}_{thermo}(\Gamma,n)
=
\mathbb{R}^5
\ni
\Omega_{SV}(\Gamma,n)
=
\bigl(
\mathcal{A}_{SV}(\Gamma,n),
H_{SV}(\Gamma,n),
\mathcal{J}_{\Gamma,SV}(n),
R_\Gamma(n),
\mathcal{B}_{\partial,SV}(\Gamma,n)
\bigr).
```

La sección $\Omega_{SV}$ es el objeto fibroso soberano del dominio. No es una magnitud derivada; es el soporte sobre el que se construyen las proyecciones termodinámicas.

### 6.2. Acumulación factual de trayectoria

Se define la acumulación factual de trayectoria por

```math
\mathcal{A}_{SV}(\Gamma,n)
:=
\sum_{k=1}^{n}\sum_i a_i(k)\,\omega(\nu_k).
```

Mide el espesor acumulativo del recorrido factual ponderado por el peso de suceso $\omega(\nu_k)$.

### 6.3. Volumen factual interior

Sea $K_{int}$ un campo factual interior del dominio. Se define el contenido volumétrico interior por

```math
V^{int}_{SV}(\Gamma,n)
:=
\iiint^{SV}_{\mathcal{V}_{SV}(\Gamma,n)} K_{int}.
```

### 6.4. Contenido factual interior

Se define la componente interior del contenido factual por

```math
\mathcal{C}^{int}_{SV}(\Gamma,n)
:=
\mathcal{A}_{SV}(\Gamma,n)
+
V^{int}_{SV}(\Gamma,n)
+
R_\Gamma(n).
```

La fórmula es operacional y no meramente denominativa: suma explícitamente acumulación factual, volumen factual interior y residual factual.

### 6.5. Contenido factual total

La magnitud madre de contenido factual total del dominio se define por

```math
\mathcal{C}^{tot}_{SV}(\Gamma,n)
:=
\mathcal{C}^{int}_{SV}(\Gamma,n)
+
\mathcal{B}_{\partial,SV}(\Gamma,n).
```

Esta igualdad deja fijado, dentro del propio documento, el reparto interior–contorno del contenido factual total.

### 6.6. Lectura factual de la no clausura legítima

La no clausura del dominio no introduce un cuarto polo semántico. Se fija como lectura factual de borde bajo indicador canónico $U$:

```math
\mathcal{U}_{SV}(\Gamma,n)
:=
D_\Gamma^{U}\mathcal{B}_{\partial,SV}(\Gamma,n).
```

$\mathcal{U}_{SV}$ no sustituye a $U$; despliega su contribución factual dentro del régimen de borde.

### 6.7. Teorema de exhaustividad estructural

**Teorema 6.7.1.** Toda contribución factual central del dominio termodinámico queda absorbida en $\mathcal{C}^{tot}_{SV}$ y en la lectura $\mathcal{U}_{SV}$ de la no clausura bajo $U$.

**Demostración.** El interior factual queda recogido por $\mathcal{C}^{int}_{SV}$. El contorno factual queda recogido por $\mathcal{B}_{\partial,SV}$. La parte no clausurable sin pérdida de honestidad se expresa por la proyección $D_\Gamma^{U}$ sobre la frontera. Luego no queda contribución central del dominio fuera de $\mathcal{C}^{tot}_{SV}$ y $\mathcal{U}_{SV}$. Q.E.D.

## 7. Proyecciones termodinámicas canónicas

### 7.1. Trabajo factual

El trabajo factual se define como proyección directriz del incremento factual total:

```math
W_{SV}(\Gamma,n)
:=
D_\Gamma^{dir}\mathcal{C}^{tot}_{SV}(\Gamma,n).
```

### 7.2. Calor factual

El calor factual se define como proyección residual del incremento factual total:

```math
Q_{SV}(\Gamma,n)
:=
D_\Gamma^{res}\mathcal{C}^{tot}_{SV}(\Gamma,n).
```

### 7.3. Lema de balance proyectivo

**Lema 7.3.1.** Se verifica la identidad

```math
\Delta_\Gamma \mathcal{C}^{tot}_{SV}
=
W_{SV}+Q_{SV}+\mathcal{U}_{SV}.
```

**Demostración.** Basta aplicar a $\mathcal{C}^{tot}_{SV}$ la identidad de descomposición factual total del apartado 3.2. Q.E.D.

### 7.4. Fuerza factual

Sea $\phi_{SV}$ un potencial factual escalar y $\Psi_{SV}$ un potencial factual vectorial del dominio. Se define la fuerza factual por

```math
F_{SV}(\Gamma,n)
:=
-\nabla^{SV}\phi_{SV}(\Gamma,n)
+
Rot_{SV}\Psi_{SV}(\Gamma,n)
+
J^{for}_{SV}(\Gamma,n),
```

donde la corrección jacobiana de fuerza se fija por

```math
J^{for}_{SV}(\Gamma,n)
:=
\mathcal{J}_{\Gamma,SV}(n)\,u_{for}(\Gamma,n)
```

para un vector factual de dirección de fuerza $u_{for}$.

### 7.5. Teorema de irreducibilidad de la fuerza factual

**Teorema 7.5.1.** La fuerza factual no se reduce, en general, a un gradiente puro.

**Demostración.** Si se tuviera $F_{SV}=-\nabla^{SV}\varphi$ para algún potencial $\varphi$, deberían anularse simultáneamente el término rotacional $Rot_{SV}\Psi_{SV}$ y la corrección jacobiana $J^{for}_{SV}$. La estructura general del dominio no impone tal anulación. Luego la reducción a gradiente puro no es general. Q.E.D.

### 7.6. Empuje factual

El empuje factual se define como respuesta de contorno inducida por la fuerza sobre la frontera activa:

```math
P^{emp}_{SV}(\Gamma,n)
:=
\sum_j \langle F_{SV}(B_j),n_{B_j}\rangle_{SV}\,\omega(B_j).
```

### 7.7. Temperatura factual

La temperatura factual se define como lectura metrológica factual del bloque irreversible–residual–jacobiano–frontera:

```math
\Theta_{SV}(\Gamma,n)
:=
UFT\!\left(
H_{SV}(\Gamma,n),
R_\Gamma(n),
\mathcal{J}_{\Gamma,SV}(n),
\mathcal{B}_{\partial,SV}(\Gamma,n)
\right).
```

Aquí $UFT$ es la unidad factual de temperatura fijada por el pilar metrológico del corpus. El documento no introduce un operador nuevo para sustituirla.

### 7.8. Teorema de no reducción monovariable de la temperatura factual

**Teorema 7.8.1.** La temperatura factual no es, en general, función de $H_{SV}$ solo.

**Demostración.** La definición de $\Theta_{SV}$ depende conjuntamente de $H_{SV}$, de $R_\Gamma$, de $\mathcal{J}_{\Gamma,SV}$ y de $\mathcal{B}_{\partial,SV}$. Luego no puede reducirse, en general, a una función de una sola variable $H_{SV}$. Q.E.D.

### 7.9. Entalpía factual

La entalpía factual se define por la descomposición interior–contorno

```math
\Lambda_{SV}(\Gamma,n)
:=
\mathcal{C}^{int}_{SV}(\Gamma,n)
+
\mathcal{B}_{\partial,SV}(\Gamma,n).
```

Por tanto,

```math
\Lambda_{SV}(\Gamma,n)=\mathcal{C}^{tot}_{SV}(\Gamma,n).
```

La entalpía factual no es una magnitud nueva independiente; es la lectura termodinámica de la descomposición total del contenido factual.

### 7.10. Teorema de no primitividad de las magnitudes derivadas

**Teorema 7.10.1.** $W_{SV}$, $Q_{SV}$, $F_{SV}$, $P^{emp}_{SV}$, $\Theta_{SV}$ y $\Lambda_{SV}$ no poseen estatuto primitivo independiente.

**Demostración.** $W_{SV}$ y $Q_{SV}$ son proyecciones del incremento de $\mathcal{C}^{tot}_{SV}$. $P^{emp}_{SV}$ es funcional de contorno de $F_{SV}$. $\Theta_{SV}$ es lectura metrológica factual del bloque irreversible–residual–jacobiano–frontera. $\Lambda_{SV}$ coincide con la descomposición total de contenido. Luego ninguna de esas magnitudes es primitiva. Q.E.D.

## 8. Identidades cerradas del dominio

### 8.1. Identidad de balance factual

Por el Lema 7.3.1,

```math
\Delta_\Gamma\mathcal{C}^{tot}_{SV}
-
W_{SV}
-
Q_{SV}
-
\mathcal{U}_{SV}
=
0.
```

Ésta es la identidad factual de balance del dominio.

### 8.2. Identidad de irreversibilidad factual

Por el Teorema 4.8.1, se tiene además

```math
\Delta_\Gamma H_{SV}\ge 0.
```

### 8.3. Identidad de cierre de fuerza factual

La fuerza factual satisface

```math
F_{SV}
+
\nabla^{SV}\phi_{SV}
-
Rot_{SV}\Psi_{SV}
-
J^{for}_{SV}
=
0.
```

### 8.4. Identidad de cierre de empuje factual

El empuje factual satisface

```math
P^{emp}_{SV}
-
\sum_j \langle F_{SV}(B_j),n_{B_j}\rangle_{SV}\,\omega(B_j)
=
0.
```

### 8.5. Identidad de cierre de temperatura factual

La temperatura factual satisface

```math
\Theta_{SV}
-
UFT(H_{SV},R_\Gamma,\mathcal{J}_{\Gamma,SV},\mathcal{B}_{\partial,SV})
=
0.
```

### 8.6. Identidad de cierre de entalpía factual

La entalpía factual satisface

```math
\Lambda_{SV}
-
(\mathcal{C}^{int}_{SV}+\mathcal{B}_{\partial,SV})
=
0.
```

## 9. Fórmula absoluta del dominio

### 9.1. Parte negativa de la irreversibilidad

Para un escalar $x$, se define la parte negativa por

```math
[x]_- := \max(-x,0).
```

### 9.2. Defecto factual total

Se define el defecto factual total del dominio termodinámico por

```math
\mathbb{T}^{thermo}_{SV}(\Gamma,n)
:=
\bigl|
\Delta_\Gamma\mathcal{C}^{tot}_{SV}
-
W_{SV}
-
Q_{SV}
-
\mathcal{U}_{SV}
\bigr|^2
+
\bigl|[\Delta_\Gamma H_{SV}]_-\bigr|^2
+
\|F_{SV}+\nabla^{SV}\phi_{SV}-Rot_{SV}\Psi_{SV}-J^{for}_{SV}\|_{SV}^2
+
\bigl|P^{emp}_{SV}-\sum_j \langle F_{SV}(B_j),n_{B_j}\rangle_{SV}\,\omega(B_j)\bigr|^2
+
\bigl|\Theta_{SV}-UFT(H_{SV},R_\Gamma,\mathcal{J}_{\Gamma,SV},\mathcal{B}_{\partial,SV})\bigr|^2
+
\bigl|\Lambda_{SV}-(\mathcal{C}^{int}_{SV}+\mathcal{B}_{\partial,SV})\bigr|^2.
```

### 9.3. Ecuación absoluta del dominio

La ecuación soberana del dominio termodinámico factual es

```math
\mathbb{T}^{thermo}_{SV}(\Gamma,n)=0.
```

Ésta es la fórmula absoluta buscada. Es una ecuación escalar nula, fibrosa por proyecciones y sin colisión con la arquitectura de ecuación única ya asentada en otros dominios del corpus.

## 10. Teoremas de cierre del dominio

### 10.1. Teorema de equivalencia estructural

**Teorema 10.1.1.** La ecuación $\mathbb{T}^{thermo}_{SV}(\Gamma,n)=0$ es equivalente a la conjunción de las seis identidades del apartado 8.

**Demostración.** Cada término de $\mathbb{T}^{thermo}_{SV}$ es un cuadrado o norma cuadrática no negativa. La suma total es cero si y sólo si cada término individual es cero. Eso equivale exactamente a las seis identidades del apartado 8. Q.E.D.

### 10.2. Teorema de cierre de balance e irreversibilidad

**Teorema 10.2.1.** Si $\mathbb{T}^{thermo}_{SV}=0$, entonces el dominio satisface simultáneamente balance factual total e irreversibilidad factual.

**Demostración.** Por el Teorema 10.1.1, la anulación del primer término impone la identidad de balance factual y la anulación del segundo término impone $[\Delta_\Gamma H_{SV}]_-=0$, es decir, $\Delta_\Gamma H_{SV}\ge 0$. Q.E.D.

### 10.3. Teorema de absorción de las magnitudes derivadas

**Teorema 10.3.1.** Si $\mathbb{T}^{thermo}_{SV}=0$, entonces $W_{SV}$, $Q_{SV}$, $F_{SV}$, $P^{emp}_{SV}$, $\Theta_{SV}$ y $\Lambda_{SV}$ quedan absorbidas por el régimen único y no abren ley soberana adicional.

**Demostración.** Cada una de esas magnitudes aparece como proyección, funcional o lectura de un término que entra en la ecuación absoluta. Si la ecuación es cero, su cierre queda forzado por las identidades del apartado 8. Luego ninguna de ellas constituye ley soberana independiente. Q.E.D.

### 10.4. Teorema de compatibilidad arquitectónica

**Teorema 10.4.1.** La fórmula $\mathbb{T}^{thermo}_{SV}=0$ es compatible con la arquitectura de ecuación única del corpus.

**Demostración.** La ecuación es escalar nula, no temporal, organizada sobre un objeto fibroso factual y cerrada por la anulación de un defecto total no negativo. Esa forma coincide arquitectónicamente con la disciplina de ecuación única ya empleada en otros dominios del corpus. Q.E.D.

### 10.5. Teorema de unicidad absoluta

**Teorema 10.5.1.** No existe una segunda ecuación soberana independiente del dominio termodinámico factual del SV.

**Demostración.** Toda ecuación alternativa tendría que imponer simultáneamente balance factual total, no decrecencia de $H_{SV}$, cierre de fuerza factual, definición de empuje factual, definición de temperatura factual y descomposición interior–contorno de la entalpía factual. La ecuación $\mathbb{T}^{thermo}_{SV}=0$ ya impone esas seis condiciones por anulación de sus seis defectos no negativos. Si una ecuación alternativa omite alguno de esos defectos, deja el dominio incompleto. Si los contiene todos, es reducible a $\mathbb{T}^{thermo}_{SV}=0$ por suma cuadrática no negativa. Luego no existe segunda ecuación soberana independiente. Q.E.D.

## 11. Compatibilidad metrológica restringida

### 11.1. Estatuto

El plano metrológico no funda el dominio. Sólo entra como lectura subordinada una vez cerrado el régimen factual.

### 11.2. Temperatura factual y UFT

La temperatura factual quedó ligada a $UFT$ en 7.7. Esa decisión evita duplicación operatoria y mantiene continuidad con el pilar metrológico del corpus.

### 11.3. Dimensiones factuales del bloque termodinámico

Se fijan las siguientes correspondencias de lectura:

```math
[\Theta_{SV}] = UFT,
```

```math
[W_{SV}] = [Q_{SV}] = [\Lambda_{SV}] = [\mathcal{C}^{tot}_{SV}],
```

```math
[P^{emp}_{SV}] = [F_{SV}]\cdot[\omega(B)].
```

El documento no introduce aquí una tabla metrológica completa nueva; adopta la ya fijada por el corpus cuando sea necesario proyectar a unidades.

## 12. Recorrido de consistencia visible

### 12.1. Banco A — balance factual exacto

Sea un proceso factual con

```math
\Delta_\Gamma\mathcal{C}^{tot}_{SV}=12,
\qquad
W_{SV}=5,
\qquad
Q_{SV}=4,
\qquad
\mathcal{U}_{SV}=3.
```

Entonces

```math
12-5-4-3=0.
```

El primer defecto del operador absoluto se anula.

### 12.2. Banco B — irreversibilidad factual

Sea un proceso factual con

```math
H_{SV}(0)=2.0,
\qquad H_{SV}(1)=2.4,
\qquad H_{SV}(2)=2.7.
```

Entonces

```math
\Delta_\Gamma H_{SV}(2)=0.7\ge 0.
```

El segundo defecto del operador absoluto se anula.

### 12.3. Banco C — cierre de fuerza factual

Sea una configuración con

```math
-\nabla^{SV}\phi_{SV}=(3,0,0),
\qquad
Rot_{SV}\Psi_{SV}=(1,1,0),
\qquad
J^{for}_{SV}=(-1,0,0).
```

Entonces

```math
F_{SV}=(3,0,0)+(1,1,0)+(-1,0,0)=(3,1,0),
```

y

```math
F_{SV}+\nabla^{SV}\phi_{SV}-Rot_{SV}\Psi_{SV}-J^{for}_{SV}=0.
```

### 12.4. Banco D — empuje factual

Si sobre la frontera activa del dominio se tiene

```math
\sum_j \langle F_{SV}(B_j),n_{B_j}\rangle_{SV}\,\omega(B_j)=7,
```

y se fija $P^{emp}_{SV}=7$, el defecto de empuje se anula.

### 12.5. Banco E — temperatura factual

Si

```math
UFT(H_{SV},R_\Gamma,\mathcal{J}_{\Gamma,SV},\mathcal{B}_{\partial,SV})=11,
```

y se fija $\Theta_{SV}=11$, el defecto térmico se anula.

### 12.6. Banco F — entalpía factual

Si

```math
\mathcal{C}^{int}_{SV}=9,
\qquad
\mathcal{B}_{\partial,SV}=2,
```

entonces

```math
\Lambda_{SV}=11
```

y el defecto entálpico se anula.

### 12.7. Dictamen visible

Si los seis defectos se anulan simultáneamente, se obtiene

```math
\mathbb{T}^{thermo}_{SV}=0.
```

El recorrido de consistencia visible verifica la cohesión del dominio sobre un caso factual finito y calculable.

## 13. Consideraciones finales

El dominio termodinámico factual del Sistema Vectorial SV queda organizado como una pirámide algebraica ascendente. El suelo es preternario y semántico. Sobre él se levanta la teoría del suceso y de sus proyecciones diferenciales. El siguiente piso es la cadena factual canónica de irreversibilidad, cerrada en $H_{SV}$ sin truncar estratos. El aparato operatorio heredado proporciona flujo, divergencia, rotor, gradiente, jacobiano y frontera sin necesidad de repropósito. Sobre esa base se construye el fibrado termodinámico factual $\Omega_{SV}$, la magnitud madre $\mathcal{C}^{tot}_{SV}$ y las proyecciones canónicas del dominio: trabajo, calor, fuerza, empuje, temperatura y entalpía. La culminación del edificio es la ecuación absoluta

```math
\mathbb{T}^{thermo}_{SV}(\Gamma,n)=0,
```

que concentra, en una sola fórmula nula, los defectos de balance, irreversibilidad, fuerza, empuje, temperatura y entalpía. El dominio queda así cerrado sin tiempo soberano, sin cuarto polo semántico, sin duplicación operatoria y sin aperturas residuales de su núcleo algebraico.

## 14. Referencias

Callen, H. B. (1985). *Thermodynamics and an introduction to thermostatistics* (2nd ed.). Wiley.

Clausius, R. (1865). *The mechanical theory of heat*. John van Voorst.

Gibbs, J. W. (1906). *The scientific papers of J. Willard Gibbs. Volume I: Thermodynamics*. Longmans, Green and Co.

Maxwell, J. C. (1871). *Theory of heat*. Longmans, Green and Co.

Prigogine, I. (1967). *Introduction to thermodynamics of irreversible processes* (3rd ed.). Interscience.

Lloret Egea, J. A. (2026a). *Conjunto matemático unificado del cambio factual, ciclos, medición factual y trayectorias poligonales de activación en el Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español.

Lloret Egea, J. A. (2026b). *Convergencia ternaria y gobierno determinista de trayectorias en el Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español.

Lloret Egea, J. A. (2026c). *El transductor lingüístico — morfismo de dominio — y el horizonte H_NLP del Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español.

Lloret Egea, J. A. (2026d). *Entropía factual e irreversibilidad estructural en el Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español.

Lloret Egea, J. A. (2026e). *Primitivos metrológicos del Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español.

Lloret Egea, J. A. (2026f). *Fundamentos operatorios absolutos del electromagnetismo factual en el Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español.

Lloret Egea, J. A. (2026g). *Reducción estructural absoluta de Maxwell en el Sistema Vectorial SV y ecuación única de la física factual electromagnética*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español.

Lloret Egea, J. A. (2026h). *Teoría general factual de la luz en el Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español.

Lloret Egea, J. A. (2026i). *Del origen preternario del Sistema Vectorial SV a la entidad absoluta del campo: derivación nativa de \alpha_i y \beta_i, proyección ternaria inducida, absorción basal exacta, unificación fuerte de gravitación, electricidad y magnetismo, y apertura a clases factuales emergentes*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español.

Lloret Egea, J. A. (2026j). *Absorción de E_0 = m_0 c^2 como sector basal de reposo en el Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español.

Lloret Egea, J. A. (2026k). *Del contenido físico factual del suceso a las clases factuales emergentes: programa de transmutación factual en el Sistema SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español.
