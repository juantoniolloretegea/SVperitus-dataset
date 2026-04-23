# Fuerza, trabajo, calor, entalpía, temperatura, principios y fundamentos de la termodinámica y la correlación entre ellos en el SV

## Resumen

Se construye el dominio termodinámico factual del Sistema Vectorial SV como un régimen algebraico de sucesos, no temporal, trazable en ambos sentidos y cerrado por una única ecuación absoluta. El cierre parte del sustrato preternario de pares admisibles, atraviesa la cadena factual canónica de irreversibilidad y fija, sobre ese suelo, un fibrado termodinámico factual cuyas proyecciones recuperan trabajo, calor, fuerza, empuje, temperatura y entalpía como magnitudes derivadas. El documento determina explícitamente la aritmética diferencial factual del dominio, la descomposición ternaria de incrementos, la acumulación factual, el contenido factual interior, el contenido factual total, la lectura factual de no clausura bajo la clase canónica `U`, la fuerza factual como combinación cerrada de gradiente, rotor vectorial y corrección jacobiana, el empuje factual como funcional de contorno, la temperatura factual como lectura metrológica soberana y la entalpía factual como descomposición interior–contorno del contenido total. La fórmula absoluta del dominio se presenta como anulación de un defecto factual total no negativo. Su nulidad equivale simultáneamente al balance factual del contenido, a la no decrecencia de la entropía factual, al cierre de fuerza y empuje, a la definición termométrica factual y a la descomposición entálpica. El resultado es una formulación única, fibrosa por proyecciones, compatible con la disciplina semántica del SV y con la arquitectura de ecuación única ya asentada en otros dominios del corpus.

## Abstract

The factual thermodynamic domain of the Sistema Vectorial SV is constructed as an event-based, non-temporal algebraic regime, traceable in both directions and closed by a single absolute equation. The closure starts from the preternary substrate of admissible pairs, crosses the canonical factual chain of irreversibility, and fixes on that ground a factual thermodynamic bundle whose projections recover work, heat, force, thrust, temperature and enthalpy as derived magnitudes. The document explicitly determines the factual differential arithmetic of the domain, the ternary decomposition of increments, factual accumulation, interior factual content, total factual content, the factual reading of non-closure under the canonical class `U`, factual force as a closed combination of gradient, vectorial rotor and Jacobian correction, factual thrust as a boundary functional, factual temperature as a sovereign metrological reading, and factual enthalpy as the interior–boundary decomposition of total content. The absolute formula of the domain is presented as the vanishing of a non-negative total factual defect. Its vanishing is simultaneously equivalent to factual content balance, non-decrease of factual entropy, closure of force and thrust, factual thermometric definition and the enthalpic decomposition. The result is a unique formulation, fibrous by projections, compatible with SV semantic discipline and with the single-equation architecture already established in other corpus domains.

## 1. Estatuto del dominio

### 1.1. Objeto exacto

El presente documento trata el dominio termodinámico factual del Sistema Vectorial SV en el rango estricto de cierre algebraico interno. Su objeto no es comentar la termodinámica heredada ni traducir terminología clásica a un léxico nuevo. Su objeto es construir una ley única del dominio y hacer que trabajo, calor, fuerza, empuje, temperatura y entalpía comparezcan sólo como magnitudes derivadas o como lecturas proyectivas del régimen factual soberano.

### 1.2. Prohibiciones constitutivas

El dominio queda sometido, sin excepción, a las siguientes prohibiciones:

1. prohibición de tiempo soberano como fundamento;
2. prohibición de probabilidad como criterio de verdad;
3. prohibición de estadística como sustituto de clausura;
4. prohibición de inferencia opaca y de heurística no declarada;
5. prohibición de cuarto polo semántico ajeno a `K_3`;
6. prohibición de repropósito silencioso de operadores ya fijados por el corpus;
7. prohibición de introducir herramienta clásica de mayor potencia allí donde el aparato factual del SV ya sea suficiente.

Estas prohibiciones no son advertencias metodológicas. Son condiciones constitutivas del dominio.

### 1.3. Criterio de aceptación de magnitudes físicas

Una magnitud sólo será admitida aquí como magnitud factual del SV si satisface simultáneamente las cinco condiciones siguientes:

1. descenso controlado al sustrato preternario;
2. compatibilidad explícita con la terna canónica y con el estatuto de `U`;
3. variación expresable por sucesos y no por cronología soberana;
4. cierre mediante operadores ya autorizados del corpus o derivados explícitos de ellos;
5. proyección clásica, cuando exista, sólo como lectura externa y nunca como fundamento constitutivo.

### 1.4. Objetivo de cierre

La meta del documento es demostrar que existe una única fórmula soberana del dominio termodinámico factual y que toda magnitud física central del dominio comparece como proyección o consecuencia de esa única fórmula.

## 2. Sustrato semántico y suelo preternario

### 2.1. Terna canónica

La terna canónica del sistema es

```math
K_3 = \{0,1,U\}.
```

El símbolo `U` conserva su estatuto de indeterminación honesta. No equivale a probabilidad, no equivale a déficit instrumental banal y no autoriza clausura favorable por plausibilidad.

### 2.2. Pares admisibles

El suelo del dominio es el sistema de pares admisibles

```math
(\alpha_i,\beta_i).
```

Sobre cada par admisible se definen el sesgo polar factual y la activación factual local por

```math
\delta_i := \beta_i - \alpha_i,
\qquad
a_i := |\delta_i|.
```

### 2.3. Teorema de prioridad preternaria

**Teorema 2.3.1.** Ninguna magnitud central del dominio termodinámico factual precede a `(\alpha_i,\beta_i)`.

**Demostración.** Toda pieza central del dominio comparece o bien como construcción directa sobre `(\delta_i,a_i)`, o bien como estrato de una cadena factual ya derivada de ese suelo, o bien como componente o proyección del fibrado termodinámico factual levantado sobre esa cadena. En ningún caso aparece un objeto con prioridad ontológica superior al par admisible. Luego el suelo preternario precede a toda magnitud central del dominio. Q.E.D.

### 2.4. Persistencia factual de `U`

Para una trayectoria factual admisible `\Gamma=(S_0,S_1,\dots,S_n)`, sea `\chi_\Gamma(k)\in K_3` la lectura ternaria del paso `k`. Se introducen los indicadores ternarios

```math
\mathbf{1}_1(k),\qquad \mathbf{1}_0(k),\qquad \mathbf{1}_U(k),
```

caracterizados por

```math
\mathbf{1}_1(k)+\mathbf{1}_0(k)+\mathbf{1}_U(k)=1.
```

Se define la proporción factual ponderada de `U` por

```math
\rho_U(\Gamma,n)
:=
\frac{\sum_{k=1}^{n}\mathbf{1}_U(k)\,\omega(\nu_k)}
     {\sum_{k=1}^{n}\omega(\nu_k)},
```

y el espesor factual acumulado de `U` por

```math
\mathcal{S}_U(\Gamma,n)
:=
\sum_{k=1}^{n}\mathbf{1}_U(k)\,a(k),
\qquad
a(k):=\sum_i a_i(k).
```

### 2.5. Teorema de no supremacía de `U`

**Teorema 2.5.1.** La persistencia factual de `U` no implica supremacía ontológica de `U`.

**Demostración.** La frecuencia de aparición de `U` en el plano ternario es una propiedad de la lectura inducida sobre la trayectoria, no del rango ontológico del estado que se lee. El suelo del sistema sigue siendo preternario, porque la lectura ternaria sólo nace después de los pares admisibles y de su activación factual. Luego una `\rho_U` alta puede describir persistencia factual de no clausura, pero no convierte a `U` en principio originario del dominio. Q.E.D.

## 3. Trayectoria factual y aritmética diferencial del dominio

### 3.1. Derivada de suceso soberana

Sea `\nu_k` el índice factual del suceso `S_{k-1}\to S_k` y sea `\omega(\nu_k)` su peso factual. Para toda magnitud factual discreta `X(\Gamma,k)` se define la derivada de suceso ponderada por

```math
\mathfrak{D}_{\Gamma}X(\Gamma,k)
:=
\frac{X(\Gamma,k)-X(\Gamma,k-1)}{\omega(\nu_k)},
\qquad
k\ge 1.
```

La acumulación factual hasta el índice `n` queda fijada por

```math
\Delta_{\Gamma}X(\Gamma,n)
:=
\sum_{k=1}^{n}\omega(\nu_k)\,\mathfrak{D}_{\Gamma}X(\Gamma,k).
```

Por construcción,

```math
\Delta_{\Gamma}X(\Gamma,n)=X(\Gamma,n)-X(\Gamma,0).
```

### 3.2. Lemas estructurales de la derivada de suceso

**Lema 3.2.1 (linealidad).** Para escalares `\lambda,\mu` y magnitudes factuales `X,Y`,

```math
\mathfrak{D}_{\Gamma}(\lambda X+\mu Y)
=
\lambda \mathfrak{D}_{\Gamma}X+\mu \mathfrak{D}_{\Gamma}Y.
```

**Demostración.** Inmediata por la linealidad de la resta y por la división por el mismo peso factual `\omega(\nu_k)`. Q.E.D.

**Lema 3.2.2 (telescopía ponderada).**

```math
\Delta_{\Gamma}X(\Gamma,n)=X(\Gamma,n)-X(\Gamma,0).
```

**Demostración.** Se sustituye la definición de `\mathfrak{D}_{\Gamma}` en la suma acumulativa, se cancelan los factores `\omega(\nu_k)` y la suma resultante telescopa. Q.E.D.

### 3.3. Proyecciones diferenciales canónicas

Sobre cualquier magnitud factual `X` se definen las proyecciones diferenciales

```math
\mathfrak{D}_{\Gamma}^{dir}X(\Gamma,n)
:=
\sum_{k=1}^{n}\mathbf{1}_1(k)\,\omega(\nu_k)\,\mathfrak{D}_{\Gamma}X(\Gamma,k),
```

```math
\mathfrak{D}_{\Gamma}^{res}X(\Gamma,n)
:=
\sum_{k=1}^{n}\mathbf{1}_0(k)\,\omega(\nu_k)\,\mathfrak{D}_{\Gamma}X(\Gamma,k),
```

```math
\mathfrak{D}_{\Gamma}^{U}X(\Gamma,n)
:=
\sum_{k=1}^{n}\mathbf{1}_U(k)\,\omega(\nu_k)\,\mathfrak{D}_{\Gamma}X(\Gamma,k).
```

### 3.4. Teorema de descomposición factual total

**Teorema 3.4.1.** Para toda magnitud factual `X`,

```math
\Delta_{\Gamma}X
=
\mathfrak{D}_{\Gamma}^{dir}X
+
\mathfrak{D}_{\Gamma}^{res}X
+
\mathfrak{D}_{\Gamma}^{U}X.
```

**Demostración.** Se sustituye la identidad ternaria `\mathbf{1}_1+\mathbf{1}_0+\mathbf{1}_U=1` en cada paso de la suma acumulativa. La exclusión mutua de indicadores impide solapamiento. Luego el incremento total se descompone de manera exhaustiva y no solapada en sus tres proyecciones canónicas. Q.E.D.

### 3.5. Corolario de cierre diferencial

Las proyecciones directriz, residual y de indeterminación honesta no son operadores ornamentales. Son la aritmética diferencial mínima del dominio. Sin ellas, no puede definirse con legitimidad ni trabajo factual, ni calor factual, ni lectura factual de no clausura.

## 4. Cadena factual canónica de irreversibilidad

### 4.1. Cadena estratificada completa

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

### 4.2. Dispersión factual preternaria

Se define

```math
H_{pre}(\Gamma,n)
:=
\sum_{k=1}^{n}\sum_i a_i(k).
```

### 4.3. Transporte ternario inducido

Sea `\tau:K_3\to\mathbb{R}_{\ge 0}` una lectura compatible con el corpus. Se define

```math
H_{K_3}(\Gamma,n)
:=
\sum_{k=1}^{n}\sum_i \tau\bigl(\chi_i(k)\bigr)\,a_i(k).
```

### 4.4. Enriquecimiento canónico

Se fija

```math
H_{\Xi}(\Gamma,n)
=
H_{K_3}(\Gamma,n)
+
\|\mathcal{J}_{\Gamma,SV}(n)\|_1
+
R_{\Gamma}(n).
```

### 4.5. Concentración y canalización

Se adoptan las reorganizaciones canónicas

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

### 4.6. Entropía factual final

La forma final de irreversibilidad factual queda dada por

```math
H_{SV}(\Gamma,n)
:=
S_{\Sigma}\bigl(H_{\Sigma_k}(\Gamma,n)\bigr).
```

### 4.7. Teorema de absorción estratificada

**Teorema 4.7.1.** `H_{SV}` absorbe ordenadamente la cadena factual previa sin colapsar sus estratos.

**Demostración.** `H_{pre}` recoge activación previa; `H_{K_3}` la transporta al plano ternario; `H_{\Xi}` añade sensibilidad y residualidad; `H_{\Sigma_c}` y `H_{\Sigma_k}` reorganizan concentración y canalización. Si `H_{SV}` no absorbiera esos estratos como pisos sucesivos, el cierre del dominio sería un salto no auditable. Luego `H_{SV}` es absorción factual estratificada. Q.E.D.

### 4.8. Lema de incremento preternario no negativo

**Lema 4.8.1.** Para toda trayectoria admisible y todo `n\ge 1`,

```math
\mathfrak{D}_{\Gamma}H_{pre}(\Gamma,n)\ge 0.
```

**Demostración.** Cada paso añade una suma de activaciones absolutas `a_i(n)\ge 0`. Luego el incremento por suceso de `H_{pre}` no puede ser negativo. Q.E.D.

### 4.9. Lema de transporte no decremental

**Lema 4.9.1.** Si `\tau(K_3)\subset \mathbb{R}_{\ge 0}`, entonces el transporte ternario inducido no destruye la no negatividad incremental:

```math
\mathfrak{D}_{\Gamma}H_{K_3}(\Gamma,n)\ge 0.
```

**Demostración.** Cada término `\tau(\chi_i(n))\,a_i(n)` es producto de dos cantidades no negativas. Luego la suma incremental es no negativa. Q.E.D.

### 4.10. Lema de enriquecimiento compatible

**Lema 4.10.1.** Si `\|\mathcal{J}_{\Gamma,SV}(n)\|_1\ge 0` y `R_{\Gamma}(n)\ge 0`, entonces

```math
\mathfrak{D}_{\Gamma}H_{\Xi}(\Gamma,n)\ge 0.
```

**Demostración.** El incremento de `H_{\Xi}` es suma de tres contribuciones no negativas: la de `H_{K_3}`, la del jacobiano factual en norma `\ell_1` y la del residual factual. Luego el incremento total es no negativo. Q.E.D.

### 4.11. Teorema de irreversibilidad factual

**Teorema 4.11.1.** Para toda trayectoria factual admisible `\Gamma` y cualesquiera `n_2\ge n_1`, se cumple

```math
H_{SV}(\Gamma,n_2)\ge H_{SV}(\Gamma,n_1).
```

**Demostración.** Por los Lemas 4.8.1, 4.9.1 y 4.10.1, la cadena factual acumula incrementos no negativos hasta `H_{\Xi}`. Los operadores canónicos `C_{\Sigma}`, `K_{\Sigma}` y `S_{\Sigma}` son absorbentes y no retractivos sobre el contenido factual ya incorporado. Luego la composición completa desde `H_{pre}` hasta `H_{SV}` no puede decrecer sobre una trayectoria admisible. Q.E.D.

### 4.12. Corolario diferencial de irreversibilidad

Para todo `n\ge 1` se tiene

```math
\mathfrak{D}_{\Gamma}H_{SV}(\Gamma,n)\ge 0
```

y, por acumulación,

```math
\Delta_{\Gamma}H_{SV}(\Gamma,n)\ge 0.
```

## 5. Aparato operatorio heredado del SV

### 5.1. Estatuto

El dominio termodinámico factual no repropone flujo, divergencia, gradiente, rotor, jacobiano ni frontera. Los adopta como cuerpo operatorio heredado y vinculante del corpus soberano.

### 5.2. Fórmulas canónicas heredadas

Se fijan para uso del dominio:

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

El rotor factual se adopta en su lectura vectorial heredada del corpus electromagnético factual. El documento no altera su tipología.

### 5.3. Jacobiano factual

El jacobiano factual estructural del corpus entra aquí como matriz soberana de sensibilidad local del régimen. Interviene en `H_{\Xi}`, en la fuerza factual y en la lectura termométrica factual.

### 5.4. Teorema de suficiencia operatoria interna

**Teorema 5.4.1.** El aparato anterior es suficiente para cerrar el dominio termodinámico factual sin introducir herramientas clásicas constitutivas de mayor potencia.

**Demostración.** El dominio exige balance de contenido, frontera, residualidad, gradiente, rotor y sensibilidad jacobiana. Todas esas piezas comparecen ya en el cuerpo operatorio heredado. Luego no procede introducir aparato externo más potente como fundamento. Q.E.D.

## 6. Fibrado termodinámico factual y magnitudes madre

### 6.1. Fibra factual del dominio

Sobre cada par `(\Gamma,n)` se define la fibra factual del dominio por

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
R_{\Gamma}(n),
\mathcal{B}_{\partial,SV}(\Gamma,n)
\bigr).
```

La sección `\Omega_{SV}` es el objeto fibroso soberano del dominio.

### 6.2. Acumulación factual de trayectoria

Se define

```math
\mathcal{A}_{SV}(\Gamma,n)
:=
\sum_{k=1}^{n}\sum_i a_i(k)\,\omega(\nu_k).
```

### 6.3. Volumen factual interior

Sea `K_{int}` un campo factual interior del dominio. Se define

```math
V^{int}_{SV}(\Gamma,n)
:=
\iiint^{SV}_{\mathcal{V}_{SV}(\Gamma,n)} K_{int}.
```

### 6.4. Contenido factual interior

Se define

```math
\mathcal{C}^{int}_{SV}(\Gamma,n)
:=
\mathcal{A}_{SV}(\Gamma,n)
+
V^{int}_{SV}(\Gamma,n)
+
R_{\Gamma}(n).
```

### 6.5. Contenido factual total

La magnitud madre del dominio queda fijada por

```math
\mathcal{C}^{tot}_{SV}(\Gamma,n)
:=
\mathcal{C}^{int}_{SV}(\Gamma,n)
+
\mathcal{B}_{\partial,SV}(\Gamma,n).
```

### 6.6. Lectura factual de la no clausura legítima

La no clausura legítima del dominio no introduce un cuarto polo; se fija por

```math
\mathcal{U}_{SV}(\Gamma,n)
:=
\mathfrak{D}_{\Gamma}^{U}\mathcal{B}_{\partial,SV}(\Gamma,n).
```

### 6.7. Teorema de exhaustividad estructural

**Teorema 6.7.1.** Toda contribución factual central del dominio termodinámico queda absorbida en `\mathcal{C}^{tot}_{SV}` y en la lectura `\mathcal{U}_{SV}` de la no clausura bajo `U`.

**Demostración.** El interior factual queda recogido por `\mathcal{C}^{int}_{SV}`. El contorno factual queda recogido por `\mathcal{B}_{\partial,SV}`. La parte de borde no clausurable con honestidad semántica se expresa por `\mathfrak{D}_{\Gamma}^{U}` sobre la frontera. Luego no queda contribución central del dominio fuera de `\mathcal{C}^{tot}_{SV}` y `\mathcal{U}_{SV}`. Q.E.D.

## 7. Proyecciones termodinámicas canónicas

### 7.1. Trabajo factual

```math
W_{SV}(\Gamma,n)
:=
\mathfrak{D}_{\Gamma}^{dir}\mathcal{C}^{tot}_{SV}(\Gamma,n).
```

### 7.2. Calor factual

```math
Q_{SV}(\Gamma,n)
:=
\mathfrak{D}_{\Gamma}^{res}\mathcal{C}^{tot}_{SV}(\Gamma,n).
```

### 7.3. Lema de balance proyectivo

**Lema 7.3.1.**

```math
\Delta_{\Gamma}\mathcal{C}^{tot}_{SV}
=
W_{SV}+Q_{SV}+\mathcal{U}_{SV}.
```

**Demostración.** Se aplica a `\mathcal{C}^{tot}_{SV}` la identidad de descomposición factual total del apartado 3.4. Q.E.D.

### 7.4. Fuerza factual

Sea `\phi_{SV}` un potencial factual escalar y `\Psi_{SV}` un potencial factual vectorial del dominio. Se define

```math
F_{SV}(\Gamma,n)
:=
-\nabla^{SV}\phi_{SV}(\Gamma,n)
+
Rot_{SV}\Psi_{SV}(\Gamma,n)
+
J^{for}_{SV}(\Gamma,n),
```

donde

```math
J^{for}_{SV}(\Gamma,n)
:=
\mathcal{J}_{\Gamma,SV}(n)\,u_{for}(\Gamma,n)
```

para un vector factual de dirección de fuerza `u_{for}`.

### 7.5. Teorema de irreducibilidad de la fuerza factual

**Teorema 7.5.1.** La fuerza factual no se reduce, en general, a un gradiente puro.

**Demostración.** Si `F_{SV}` fuera igual a `-\nabla^{SV}\varphi` para algún potencial `\varphi`, deberían anularse el término rotacional `Rot_{SV}\Psi_{SV}` y la corrección jacobiana `J^{for}_{SV}`. La estructura general del dominio no impone tal anulación. Luego la reducción a gradiente puro no es general. Q.E.D.

### 7.6. Empuje factual

```math
P^{emp}_{SV}(\Gamma,n)
:=
\sum_j \langle F_{SV}(B_j),n_{B_j}\rangle_{SV}\,\omega(B_j).
```

### 7.7. Temperatura factual

```math
\Theta_{SV}(\Gamma,n)
:=
UFT\!\left(
H_{SV}(\Gamma,n),
R_{\Gamma}(n),
\mathcal{J}_{\Gamma,SV}(n),
\mathcal{B}_{\partial,SV}(\Gamma,n)
\right).
```

### 7.8. Teorema de no reducción monovariable de la temperatura factual

**Teorema 7.8.1.** La temperatura factual no es, en general, función de `H_{SV}` solo.

**Demostración.** La definición de `\Theta_{SV}` depende simultáneamente de `H_{SV}`, `R_{\Gamma}`, `\mathcal{J}_{\Gamma,SV}` y `\mathcal{B}_{\partial,SV}`. Luego no puede reducirse, en general, a una función de una sola variable. Q.E.D.

### 7.9. Entalpía factual

```math
\Lambda_{SV}(\Gamma,n)
:=
\mathcal{C}^{int}_{SV}(\Gamma,n)
+
\mathcal{B}_{\partial,SV}(\Gamma,n)
=
\mathcal{C}^{tot}_{SV}(\Gamma,n).
```

### 7.10. Teorema de no primitividad

**Teorema 7.10.1.** `W_{SV}`, `Q_{SV}`, `F_{SV}`, `P^{emp}_{SV}`, `\Theta_{SV}` y `\Lambda_{SV}` no poseen estatuto primitivo independiente.

**Demostración.** `W_{SV}` y `Q_{SV}` son proyecciones del incremento de `\mathcal{C}^{tot}_{SV}`. `P^{emp}_{SV}` es funcional de contorno de `F_{SV}`. `\Theta_{SV}` es lectura metrológica factual del bloque irreversible–residual–jacobiano–frontera. `\Lambda_{SV}` coincide con la descomposición total de contenido. Luego ninguna de esas magnitudes es primitiva. Q.E.D.

## 8. Identidades cerradas del dominio

### 8.1. Identidad de balance factual

```math
\Delta_{\Gamma}\mathcal{C}^{tot}_{SV}
-
W_{SV}
-
Q_{SV}
-
\mathcal{U}_{SV}
=
0.
```

### 8.2. Identidad de irreversibilidad factual

```math
\Delta_{\Gamma}H_{SV}\ge 0.
```

### 8.3. Identidad de cierre de fuerza factual

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

```math
P^{emp}_{SV}
-
\sum_j \langle F_{SV}(B_j),n_{B_j}\rangle_{SV}\,\omega(B_j)
=
0.
```

### 8.5. Identidad de cierre de temperatura factual

```math
\Theta_{SV}
-
UFT(H_{SV},R_{\Gamma},\mathcal{J}_{\Gamma,SV},\mathcal{B}_{\partial,SV})
=
0.
```

### 8.6. Identidad de cierre de entalpía factual

```math
\Lambda_{SV}
-
(\mathcal{C}^{int}_{SV}+\mathcal{B}_{\partial,SV})
=
0.
```

## 9. Fórmula absoluta del dominio

### 9.1. Parte negativa de la irreversibilidad

Para un escalar `x`,

```math
[x]_-
:=
\max(-x,0).
```

### 9.2. Defecto factual total

Se define

```math
\mathbb{T}^{thermo}_{SV}(\Gamma,n)
:=
\bigl|
\Delta_{\Gamma}\mathcal{C}^{tot}_{SV}
-
W_{SV}
-
Q_{SV}
-
\mathcal{U}_{SV}
\bigr|^2
+
\bigl|[\Delta_{\Gamma}H_{SV}]_-\bigr|^2
+
\|F_{SV}+\nabla^{SV}\phi_{SV}-Rot_{SV}\Psi_{SV}-J^{for}_{SV}\|_{SV}^2
+
\bigl|
P^{emp}_{SV}
-
\sum_j \langle F_{SV}(B_j),n_{B_j}\rangle_{SV}\,\omega(B_j)
\bigr|^2
+
\bigl|
\Theta_{SV}
-
UFT(H_{SV},R_{\Gamma},\mathcal{J}_{\Gamma,SV},\mathcal{B}_{\partial,SV})
\bigr|^2
+
\bigl|
\Lambda_{SV}
-
(\mathcal{C}^{int}_{SV}+\mathcal{B}_{\partial,SV})
\bigr|^2.
```

### 9.3. Ecuación absoluta

```math
\mathbb{T}^{thermo}_{SV}(\Gamma,n)=0.
```

Ésta es la fórmula absoluta del dominio. Es escalar nula, fibrosa por proyecciones y compatible con la arquitectura de ecuación única ya asentada en el corpus.

## 10. Teoremas de cierre del dominio

### 10.1. Teorema de equivalencia estructural

**Teorema 10.1.1.** La ecuación `\mathbb{T}^{thermo}_{SV}(\Gamma,n)=0` es equivalente a la conjunción de las seis identidades del apartado 8.

**Demostración.** Cada término de `\mathbb{T}^{thermo}_{SV}` es un cuadrado o norma cuadrática no negativa. La suma total es cero si y sólo si cada término individual es cero. Eso equivale exactamente a las seis identidades del apartado 8. Q.E.D.

### 10.2. Teorema de cierre de balance e irreversibilidad

**Teorema 10.2.1.** Si `\mathbb{T}^{thermo}_{SV}=0`, el dominio satisface simultáneamente balance factual total e irreversibilidad factual.

**Demostración.** La anulación del primer término impone la identidad de balance factual. La anulación del segundo término impone `\Delta_{\Gamma}H_{SV}\ge 0`. Q.E.D.

### 10.3. Teorema de absorción de las magnitudes derivadas

**Teorema 10.3.1.** Si `\mathbb{T}^{thermo}_{SV}=0`, entonces `W_{SV}`, `Q_{SV}`, `F_{SV}`, `P^{emp}_{SV}`, `\Theta_{SV}` y `\Lambda_{SV}` quedan absorbidas por el régimen único y no abren ley soberana adicional.

**Demostración.** Cada una de esas magnitudes aparece como proyección, funcional o lectura de un término incluido en la ecuación absoluta. Si la ecuación es cero, el cierre de todas ellas queda forzado por las identidades del apartado 8. Luego ninguna constituye ley soberana independiente. Q.E.D.

### 10.4. Teorema de compatibilidad arquitectónica

**Teorema 10.4.1.** La forma `\mathbb{T}^{thermo}_{SV}=0` es compatible con la arquitectura de ecuación única ya asentada en el corpus.

**Demostración.** La ecuación es escalar nula, no temporal, organizada sobre un objeto fibroso factual y cerrada por anulación de un defecto total no negativo. Esa forma es arquitectónicamente compatible con la familia de ecuación única del corpus. Q.E.D.

### 10.5. Teorema de unicidad fuerte

**Teorema 10.5.1.** No existe una segunda ecuación escalar soberana independiente que cierre el mismo dominio con igual conjunto de exigencias constitutivas.

**Demostración.** Toda ecuación alternativa tendría que imponer simultáneamente balance factual, irreversibilidad factual, cierre de fuerza, cierre de empuje, definición termométrica factual y descomposición entálpica interior–contorno. Si omite alguna, el dominio queda incompleto. Si las contiene todas, debe anular la misma familia de defectos. Toda reescritura escalar que mantenga esas seis nulidades es equivalente, por transformación monótona positiva, a la nulidad del defecto factual total fijado. Luego no existe segunda ecuación escalar soberana independiente con el mismo alcance constitutivo. Q.E.D.

## 11. Compatibilidad metrológica restringida

### 11.1. Estatuto

El plano metrológico no funda el dominio. Sólo comparece como lectura subordinada una vez cerrado el régimen factual.

### 11.2. Correspondencias de lectura

```math
[\Theta_{SV}] = UFT,
```

```math
[W_{SV}] = [Q_{SV}] = [\Lambda_{SV}] = [\mathcal{C}^{tot}_{SV}],
```

```math
[P^{emp}_{SV}] = [F_{SV}]\cdot[\omega(B)].
```

### 11.3. Observación crítica

El documento no da por cerrada aquí una tabla metrológica total de la termodinámica factual. Fija sólo el cosido mínimo necesario para que sus magnitudes no queden flotantes ni contradigan el pilar soberano de unidades factuales.

## 12. Recorrido de consistencia visible

### 12.1. Banco A — balance factual exacto

Sea un proceso factual con

```math
\Delta_{\Gamma}\mathcal{C}^{tot}_{SV}=12,
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

### 12.2. Banco B — irreversibilidad factual

Sea un proceso factual con

```math
H_{SV}(0)=2.0,
\qquad
H_{SV}(1)=2.4,
\qquad
H_{SV}(2)=2.7.
```

Entonces

```math
\Delta_{\Gamma}H_{SV}(2)=0.7\ge 0.
```

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
F_{SV}=(3,1,0),
```

y

```math
F_{SV}+\nabla^{SV}\phi_{SV}-Rot_{SV}\Psi_{SV}-J^{for}_{SV}=0.
```

### 12.4. Banco D — empuje factual

Si

```math
\sum_j \langle F_{SV}(B_j),n_{B_j}\rangle_{SV}\,\omega(B_j)=7
```

y se fija `P^{emp}_{SV}=7`, el defecto de empuje se anula.

### 12.5. Banco E — temperatura factual

Si

```math
UFT(H_{SV},R_{\Gamma},\mathcal{J}_{\Gamma,SV},\mathcal{B}_{\partial,SV})=11
```

y se fija `\Theta_{SV}=11`, el defecto térmico se anula.

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

## 13. Bancos de tensión del dominio

### 13.1. Banco T1 — borde nulo

Supóngase

```math
\mathcal{B}_{\partial,SV}=0.
```

Entonces

```math
\mathcal{C}^{tot}_{SV}=\mathcal{C}^{int}_{SV},
\qquad
\mathcal{U}_{SV}=0,
\qquad
P^{emp}_{SV}=0,
\qquad
\Lambda_{SV}=\mathcal{C}^{int}_{SV}.
```

La ecuación absoluta se reduce a cuatro defectos no triviales: balance interior, irreversibilidad, fuerza factual y lectura termométrica. El banco muestra que el régimen no colapsa cuando desaparece el borde; sólo se especializa.

### 13.2. Banco T2 — residual nulo

Supóngase

```math
R_{\Gamma}=0.
```

Entonces el enriquecimiento canónico queda reducido a

```math
H_{\Xi}=H_{K_3}+\|\mathcal{J}_{\Gamma,SV}\|_1.
```

La temperatura factual pasa a depender de

```math
\Theta_{SV}=UFT(H_{SV},0,\mathcal{J}_{\Gamma,SV},\mathcal{B}_{\partial,SV}).
```

El banco verifica que la definición termométrica no necesita residual distinto de cero para seguir siendo legítima.

### 13.3. Banco T3 — régimen puramente directriz

Supóngase

```math
\mathbf{1}_0(k)=0,
\qquad
\mathbf{1}_U(k)=0
qquad\text{para todo }k.
```

Entonces

```math
Q_{SV}=0,
\qquad
\mathcal{U}_{SV}=0,
\qquad
\Delta_{\Gamma}\mathcal{C}^{tot}_{SV}=W_{SV}.
```

El banco fuerza el límite de dominio sin calor factual ni no clausura. La ecuación absoluta debe seguir cerrando con consistencia.

### 13.4. Banco T4 — régimen puramente residual

Supóngase

```math
\mathbf{1}_1(k)=0,
\qquad
\mathbf{1}_U(k)=0
qquad\text{para todo }k.
```

Entonces

```math
W_{SV}=0,
\qquad
\mathcal{U}_{SV}=0,
\qquad
\Delta_{\Gamma}\mathcal{C}^{tot}_{SV}=Q_{SV}.
```

El banco obliga al documento a soportar un régimen factual sin parte directriz. La consistencia del balance no depende de que el trabajo factual sea distinto de cero.

### 13.5. Banco T5 — persistencia dominante de `U`

Supóngase una trayectoria con

```math
\rho_U(\Gamma,n)=0.92,
\qquad
\Delta_{\Gamma}H_{SV}(\Gamma,n)>0.
```

Entonces la ecuación absoluta no queda dañada: la mayor parte del espesor factual se lee como no clausura honesta y, sin embargo, el régimen sigue siendo irreversible. Este banco tensa el documento exactamente sobre el punto donde `U` es persistente sin volverse principio ontológico.

### 13.6. Banco T6 — colapso del término rotacional

Supóngase

```math
Rot_{SV}\Psi_{SV}=0.
```

Entonces la fuerza factual se reduce a

```math
F_{SV}=-\nabla^{SV}\phi_{SV}+J^{for}_{SV}.
```

El banco verifica que el cierre de fuerza sigue siendo no trivial si la corrección jacobiana persiste. El rotor no es decorativo; su desaparición especializa el régimen, no lo trivializa automáticamente.

### 13.7. Banco T7 — colapso jacobiano

Supóngase

```math
\mathcal{J}_{\Gamma,SV}=0.
```

Entonces

```math
H_{\Xi}=H_{K_3}+R_{\Gamma},
\qquad
J^{for}_{SV}=0,
\qquad
\Theta_{SV}=UFT(H_{SV},R_{\Gamma},0,\mathcal{B}_{\partial,SV}).
```

El banco tensa el dominio en ausencia total de sensibilidad jacobiana. La ecuación absoluta no desaparece; pierde un grado de precisión estructural y conserva los demás.

### 13.8. Banco T8 — único defecto activo

Supóngase que se anulan los cinco últimos defectos de `\mathbb{T}^{thermo}_{SV}` pero no el primero. Entonces

```math
\mathbb{T}^{thermo}_{SV}
=
\bigl|
\Delta_{\Gamma}\mathcal{C}^{tot}_{SV}-W_{SV}-Q_{SV}-\mathcal{U}_{SV}
\bigr|^2
>0.
```

Este banco muestra que el balance factual del contenido es condición necesaria independiente y no consecuencia gratuita del resto.

### 13.9. Banco T9 — defecto térmico aislado

Supóngase que se anulan todos los defectos salvo el térmico. Entonces

```math
\mathbb{T}^{thermo}_{SV}
=
\bigl|\Theta_{SV}-UFT(H_{SV},R_{\Gamma},\mathcal{J}_{\Gamma,SV},\mathcal{B}_{\partial,SV})\bigr|^2
>0.
```

El banco demuestra que la lectura termométrica factual no queda absorbida automáticamente por el resto del dominio si se le niega su propia condición de cierre.

### 13.10. Banco T10 — defecto entálpico aislado

Supóngase que se anulan todos los defectos salvo el entálpico. Entonces

```math
\mathbb{T}^{thermo}_{SV}
=
\bigl|\Lambda_{SV}-(\mathcal{C}^{int}_{SV}+\mathcal{B}_{\partial,SV})\bigr|^2
>0.
```

El banco prueba que la descomposición interior–contorno no es redundante dentro de la fórmula absoluta.

## 14. Anexo algebraico profundo

### 14.1. Positividad estructural del defecto factual total

**Lema 14.1.1.** Para todo par `(\Gamma,n)` se cumple

```math
\mathbb{T}^{thermo}_{SV}(\Gamma,n)\ge 0.
```

**Demostración.** Cada sumando del defecto factual total es o bien un cuadrado de valor absoluto, o bien una norma al cuadrado. Todos son no negativos. La suma de no negativos es no negativa. Q.E.D.

### 14.2. Teorema de nulidad componente a componente

**Teorema 14.2.1.** Se tiene

```math
\mathbb{T}^{thermo}_{SV}(\Gamma,n)=0
```

si y sólo si cada uno de sus seis sumandos es nulo.

**Demostración.** La implicación directa se sigue de la positividad estructural: una suma de seis términos no negativos sólo puede valer cero si cada término vale cero. La implicación inversa es inmediata por sustitución. Q.E.D.

### 14.3. Teorema de equivalencia entre cierre fibroso y cierre escalar

**Teorema 14.3.1.** La anulación de la ecuación escalar `\mathbb{T}^{thermo}_{SV}=0` es equivalente al cierre de las seis proyecciones termodinámicas canónicas.

**Demostración.** Cada proyección termodinámica canónica del dominio aparece exactamente una vez como diferencia cerrable dentro del defecto factual total: el balance para `W_{SV},Q_{SV},\mathcal{U}_{SV}`, la fuerza para `F_{SV}`, el empuje para `P^{emp}_{SV}`, la temperatura para `\Theta_{SV}` y la entalpía para `\Lambda_{SV}`. Por el Teorema 14.2.1, la nulidad escalar equivale a la nulidad de cada uno de esos defectos de proyección. Q.E.D.

### 14.4. Teorema de no redundancia de los seis defectos

**Teorema 14.4.1.** Ninguno de los seis defectos de `\mathbb{T}^{thermo}_{SV}` es algebraicamente redundante respecto de los otros cinco.

**Demostración.** Los Bancos T8, T9 y T10 prueban explícitamente no redundancia para balance, temperatura y entalpía. Los Bancos B, C y D del recorrido de consistencia, leídos de forma complementaria, muestran que irreversibilidad, fuerza y empuje pueden activarse como condiciones independientes de cierre. Luego ningún defecto es deducible de los otros cinco como identidad universal del dominio. Q.E.D.

### 14.5. Teorema de minimalidad estructural

**Teorema 14.5.1.** Dentro del cierre escalar por suma de defectos no negativos, el conjunto de seis defectos de `\mathbb{T}^{thermo}_{SV}` es mínimo.

**Demostración.** Por el Teorema 14.4.1, ningún defecto es redundante. Eliminar cualquiera de ellos destruye una condición constitutiva independiente del dominio. Luego no existe un cierre escalar del mismo alcance constitutivo con menos de seis defectos. Q.E.D.

### 14.6. Teorema de irreductibilidad por compresión escalar

**Teorema 14.6.1.** No existe una compresión escalar estricta de `\mathbb{T}^{thermo}_{SV}` a una suma de menos términos no negativos que conserve simultáneamente balance factual, irreversibilidad factual, cierre de fuerza, cierre de empuje, definición termométrica factual y descomposición entálpica interior–contorno.

**Demostración.** Toda compresión a menos términos exigiría absorber al menos dos defectos independientes en un único término de modo que uno de ellos fuese lógicamente deducible del otro. El Teorema 14.4.1 excluye esa deducibilidad universal. Luego tal compresión no existe. Q.E.D.

### 14.7. Teorema de estabilidad bajo especialización factual admisible

**Teorema 14.7.1.** La forma `\mathbb{T}^{thermo}_{SV}` es estable bajo las especializaciones factuales admisibles descritas en los Bancos T1–T7.

**Demostración.** En cada banco se anula o se fija una parte del aparato sin alterar la definición formal del defecto factual total. La fórmula permanece bien tipada y sigue evaluándose como suma de defectos no negativos. Luego la forma escalar es estable bajo especialización admisible del dominio. Q.E.D.

### 14.8. Teorema de unicidad fuerte reforzada

**Teorema 14.8.1.** No existe una segunda ecuación escalar soberana independiente que cierre el mismo dominio con el mismo alcance constitutivo y con igual o menor complejidad estructural.

**Demostración.** Por el Teorema 14.5.1, el número de defectos del cierre escalar actual es mínimo. Por el Teorema 14.6.1, no existe compresión ulterior sin pérdida constitutiva. Por el Teorema 14.3.1, toda ecuación escalar del mismo alcance debe anular exactamente la misma familia de cierres fibrosos. Luego toda alternativa del mismo alcance es equivalente por transformación monótona positiva a la ecuación actual y no constituye una segunda ecuación soberana independiente. Q.E.D.

## 15. Conclusión general

El dominio termodinámico factual del Sistema Vectorial SV queda organizado como una pirámide algebraica ascendente. El suelo es preternario y semántico. Sobre él se levanta la aritmética diferencial de suceso. El siguiente piso es la cadena factual canónica de irreversibilidad, cerrada en `H_{SV}` sin truncar estratos. El aparato operatorio heredado proporciona flujo, divergencia, rotor, gradiente, jacobiano y frontera sin necesidad de repropósito. Sobre esa base se construye el fibrado termodinámico factual `\Omega_{SV}`, la magnitud madre `\mathcal{C}^{tot}_{SV}` y las proyecciones canónicas del dominio: trabajo, calor, fuerza, empuje, temperatura y entalpía. La culminación del edificio es la ecuación absoluta

```math
\mathbb{T}^{thermo}_{SV}(\Gamma,n)=0,
```

que concentra, en una sola fórmula nula, los defectos de balance, irreversibilidad, fuerza, empuje, temperatura y entalpía.

El resultado debe leerse con precisión. El documento sí ofrece una respuesta genuina del SV al dominio termodinámico en su plano algebraico interno. No sustituye todavía el trabajo ulterior de contraste físico-material completo. Lo que queda aquí cerrado es la ley soberana interna del dominio, no la totalidad última de toda termodinámica experimental posible.

## 16. Referencias

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
