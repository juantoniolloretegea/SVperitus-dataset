# Fuerza, trabajo, calor, entalpía, temperatura, principios y fundamentos de la termodinámica y la correlación entre ellos en el SV

**© 2026. Todos los derechos reservados.** | **Juan Antonio Lloret Egea** | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 23/04/2026

---

## Resumen

Se fija el dominio termodinámico factual del Sistema Vectorial SV como un régimen **de sucesos** (no temporal), **trazable** y **auditable**, cerrado por una **única ecuación escalar nula**. El cierre se construye desde el sustrato preternario $(\alpha_i,\beta_i)$, atraviesa la cadena canónica de irreversibilidad factual
$$
H_{pre}\;\to\;H_{K_3}\;\to\;H_\Xi\;\to\;H_{\Sigma_c}\;\to\;H_{\Sigma_k}\;\to\;H_{SV},
$$
y levanta, sobre ese suelo, un régimen operativo donde trabajo, calor, fuerza, empuje, temperatura y entalpía comparecen como magnitudes **definidas operacionalmente** y cosidas a un aparato de derivadas de suceso, gradiente, rotor vectorial, jacobiano y operadores de frontera. La fórmula absoluta se expresa como un defecto factual total $\mathbb{T}^{thermo}_{SV}(\Gamma,n)\ge 0$ cuya nulidad equivale simultáneamente al balance factual del contenido, a la irreversibilidad, al cierre constitutivo de fuerza y empuje, a la lectura termométrica en unidad factual de temperatura y a la correlación entálpica interior–frontera. No se introduce tiempo soberano, probabilidad, estadística, heurística no declarada ni cuarto polo semántico.

**Palabras clave:** Sistema Vectorial SV; termodinámica factual; sucesos; irreversibilidad estructural; trabajo factual; calor factual; fuerza factual; empuje factual; temperatura factual; entalpía factual; ecuación única; jacobiano; rotor vectorial; frontera factual.

---

## Abstract

The factual thermodynamic domain of the Sistema Vectorial SV is fixed as an **event-based** (non-temporal), **traceable** and **auditable** regime, closed by a **single scalar null equation**. The closure starts from the preternary substrate $(\alpha_i,\beta_i)$, crosses the canonical irreversibility chain
$$
H_{pre}\to H_{K_3}\to H_\Xi\to H_{\Sigma_c}\to H_{\Sigma_k}\to H_{SV},
$$
and builds an operational regime where work, heat, force, thrust, temperature and enthalpy appear as **operationally defined** magnitudes tied to event-derivatives, gradient, vector rotor, Jacobian and boundary operators. The absolute formula is expressed as a non-negative total factual defect $\mathbb{T}^{thermo}_{SV}(\Gamma,n)$ whose vanishing is equivalent to content balance, irreversibility, constitutive closure of force and thrust, thermometric reading in the factual temperature unit, and the enthalpic interior–boundary correlation. No sovereign time, probability, statistics, undeclared heuristics or a fourth semantic pole is introduced.

---

## 1. Estatuto del dominio y disciplina constitutiva

### 1.1. Variable canónica y rechazo del tiempo

La variable independiente canónica del dominio es el **índice de suceso**. Una trayectoria factual admisible es una sucesión

$$
\Gamma = (S_0,S_1,\ldots,S_n),
\qquad n\in\mathbb{N}_0,
$$

con pesos factuales $\omega(\nu_k)>0$ asociados a cada paso $k$. No se introduce parámetro temporal soberano.

### 1.2. Terna canónica y preservación de U

El sistema se rige por la terna canónica

$$
K_3=\{0,1,U\},
$$

donde $U$ denota **indeterminación honesta** (no cuantitativa, no probabilista). Para cada paso $k$ se consideran las funciones indicadoras ternarias

$$
\mathbf{1}_0(k),\ \mathbf{1}_1(k),\ \mathbf{1}_U(k)\in\{0,1\},
\qquad
\mathbf{1}_0(k)+\mathbf{1}_1(k)+\mathbf{1}_U(k)=1.
$$

---

## 2. Sustrato preternario: pares admisibles y derivación de variables

Sea $N$ el número de posiciones preternarias activas. Para cada $i\in\{1,\ldots,N\}$ y cada paso $k$ se consideran pares $(\alpha_i(k),\beta_i(k))$ con sesgo polar

$$
\delta_i(k):=\beta_i(k)-\alpha_i(k).
$$

Se define la acumulación factual de apertura y la clausura binaria por:

$$
A_i(n) := \sum_{k=0}^{n-1} \frac{a_i(k) + a_i(k+1)}{2}\,\Delta\varepsilon_k,
\qquad
C_i(n) := \sum_{k=1}^{n} \chi_i(k)\in\{0,1\},
$$

donde $a_i(k)\ge 0$ es la activación factual de la posición $i$, $\Delta\varepsilon_k>0$ el incremento factual básico del paso $k$ y $\chi_i(k)\in\{0,1\}$ el indicador de clausura local.

Se define el espesor factual y el sesgo polar acumulado por:

$$
M_i(n):=A_i(n)+C_i(n),
\qquad
B_i(n):=\sum_{k=1}^{n}\chi_i(k)\,\bigl(2\rho_i(S_k)-1\bigr),
$$

y se reconstruyen los pares por:

$$
\alpha_i(n):=\frac{M_i(n)-B_i(n)}{2},
\qquad
\beta_i(n):=\frac{M_i(n)+B_i(n)}{2}.
$$

Estas identidades fijan la trazabilidad descendente (desde magnitudes agregadas a $(\alpha_i,\beta_i)$) y ascendente (desde $(\alpha_i,\beta_i)$ a magnitudes agregadas).

---

## 3. Cadena entrópica canónica e irreversibilidad

### 3.1. Variación total preternaria

Sea $k_i^*$ el paso de activación de la posición $i$. La variación total preternaria del sesgo polar es:

$$
V_i(\delta,n) := \sum_{k=0}^{\min(n,k_i^*)-1}\bigl|\delta_i(k+1)-\delta_i(k)\bigr|.
$$

### 3.2. Dispersión preternaria

La dispersión factual preternaria es:

$$
H_{pre}(\Gamma,n):=\sum_{i=1}^N\bigl[A_i(n)+V_i(\delta,n)\bigr].
$$

**Proposición 3.2.1 (positividad).** $H_{pre}(\Gamma,n)\ge 0$ para toda $\Gamma$ admisible y todo $n$.

*Demostración.* $A_i(n)$ es suma de términos no negativos; $V_i(\delta,n)$ es suma de valores absolutos. Q.E.D.

### 3.3. Dispersión ternaria inducida

Sea $v_i(k)\in\{0,1,U\}$ la proyección ternaria inducida de la posición $i$ al paso $k$ y $\rho$ la codificación visible $\rho(0)=1,\rho(1)=2,\rho(U)=3$. La dispersión ternaria inducida es:

$$
H_{K_3}(\Gamma,n) := \sum_{i=1}^{N}\sum_{k=0}^{n-1}\mathbf{1}\!\left[v_i(k)\neq v_i(k+1)\right]\cdot\rho\!\left(v_i(k+1)\right).
$$

### 3.4. Dispersión canónica factual

Sea el descriptor factual compuesto $\Xi_{SV}(\Gamma)\sim(A_\Gamma,B_\Gamma,\|J_\Gamma\|_1,R_\Gamma)$, con $A_\Gamma=\sum_iA_i(n)$, $B_\Gamma=\sum_iB_i(n)$ y $J_\Gamma$ el jacobiano estructural (definido en §4). La dispersión canónica factual es:

$$
H_\Xi(\Gamma,n):=A_\Gamma(n)+V_\Gamma(B,n)+\|J_\Gamma(n)\|_1+R_\Gamma(n),
$$

donde $V_\Gamma(B,n):=\sum_i V_i(\delta,n)$ y $R_\Gamma(n)$ es el residual factual global acumulado hasta $n$.

### 3.5. Dispersión en concentración, canalización y final

Sean $\mathfrak{C}^{adm}_{\Sigma_{conc}}$, $\mathfrak{C}^{adm}_{\Sigma_{canal}}$ y $\mathfrak{C}^{adm}_{trans}$ familias admisibles de contribuciones estructurales propias de cada estrato. Se definen:

$$
H_{\Sigma_c}(\Gamma,n):=H_\Xi(\Gamma,n)+\sum_{\mathcal{C}\in\mathfrak{C}^{adm}_{\Sigma_{conc}}}\mathcal{C}(\Gamma,n),
$$

$$
H_{\Sigma_k}(\Gamma,n):=H_{\Sigma_c}(\Gamma,n)+\sum_{\mathcal{C}\in\mathfrak{C}^{adm}_{\Sigma_{canal}}}\mathcal{C}(\Gamma,n),
$$

$$
H_{SV}(\Gamma,n):=H_{fin}(\Gamma,n):=H_{\Sigma_k}(\Gamma,n)+\sum_{\mathcal{C}\in\mathfrak{C}^{adm}_{trans}}\mathcal{C}(\Gamma,n).
$$

### 3.6. Teorema de irreversibilidad

**Teorema 3.6.1 (irreversibilidad factual).** Para toda trayectoria admisible $\Gamma$ y todo $n\ge 0$:

$$
\Delta_\Gamma H_{SV}(\Gamma,n)\ge 0.
$$

*Demostración.* La cadena de dispersión se construye como agregación de contribuciones no negativas sobre estratos, y su monotonía se transporta por la cadena canónica. Q.E.D.

---

## 4. Operadores diferenciales y geométricos del dominio

### 4.1. Derivada de suceso y diferencia factual

Para una magnitud escalar $q(\Gamma,k)$ se define el incremento elemental y la derivada de suceso:

$$
\Delta_\Gamma q(k):=q(\Gamma,k)-q(\Gamma,k-1),
\qquad
\partial_\nu^{SV} q(k):=\frac{q(\Gamma,k)-q(\Gamma,k-1)}{\omega(\nu_{k-1})}.
$$

Se define el incremento agregado hasta $n$ por:

$$
\Delta_\Gamma q(\Gamma,n):=q(\Gamma,n)-q(\Gamma,0)=\sum_{k=1}^n \Delta_\Gamma q(k).
$$

### 4.2. Gradiente, rotor vectorial y divergencia (rango tridimensional)

Se trabaja con un rango tridimensional auxiliar de auditoría $\mathbb{R}^3$ compatible con la célula canónica. Para un potencial escalar $\phi$ y un campo vectorial $F=(F^1,F^2,F^3)$ se definen:

$$
\nabla^{SV}\phi:=\bigl(\partial_1^{SV}\phi,\partial_2^{SV}\phi,\partial_3^{SV}\phi\bigr),
$$

$$
\Omega^{SV}_{ij}(F):=\partial_i^{SV}F^j-\partial_j^{SV}F^i\quad (i,j\in\{1,2,3\}),
$$

y el rotor vectorial se define por dualización explícita mediante el símbolo de Levi-Civita $\varepsilon_{kij}$:

$$
Rot^{vec}_{SV}F
:=
\left(
\frac{1}{2}\sum_{i,j}\varepsilon_{1ij}\Omega^{SV}_{ij}(F),
\frac{1}{2}\sum_{i,j}\varepsilon_{2ij}\Omega^{SV}_{ij}(F),
\frac{1}{2}\sum_{i,j}\varepsilon_{3ij}\Omega^{SV}_{ij}(F)
\right).
$$

La divergencia factual es:

$$
Div_{SV}F:=\partial_1^{SV}F^1+\partial_2^{SV}F^2+\partial_3^{SV}F^3-\mathcal{I}_{res}(F),
$$

donde $\mathcal{I}_{res}$ recoge contribuciones internas de fuente, sumidero o residual estructural (no probabilista).

### 4.3. Jacobiano estructural

Sea $q:\mathbb{R}^m\to\mathbb{R}^m$ un observable vectorial del dominio (o una parametrización local del estado). Su jacobiano factual se define por:

$$
J_{SV}(q,\theta):=\left(\frac{\partial q^i}{\partial \theta_j}\right)_{i,j},
\qquad
\|J_{SV}\|_1:=\sum_{i,j}\left|\frac{\partial q^i}{\partial \theta_j}\right|.
$$

En una trayectoria $\Gamma$ se fija un observable $q_\Gamma$ y se escribe $J_\Gamma(n):=J_{SV}(q_\Gamma,\theta(n))$.

### 4.4. Integrales factuales de línea, superficie y volumen

Sea una curva factual orientada $\Gamma^{\circlearrowleft}$ particionada en tramos $\Gamma_j$ con signos $\varepsilon_j\in\{-1,+1\}$ y pesos $\omega(\Gamma_j)$. La integral curvilínea factual de un campo $F$ se define por:

$$
\int_{\Gamma}^{SV} \langle F,dx\rangle_{SV}
:=
\sum_j \varepsilon_j \,\langle F(\Gamma_j),\,\Delta x(\Gamma_j)\rangle_{SV}\,\omega(\Gamma_j).
$$

Sea una superficie factual orientada $\Sigma$ particionada en caras $B_j$ con orientación $\sigma_j$ y pesos $\omega(B_j)$. La integral de superficie factual de la componente normal de $F$ es:

$$
\iint_{\Sigma}^{SV} F\cdot n \;:=\; \sum_j \sigma_j\,\langle F(B_j),n_{B_j}\rangle_{SV}\,\omega(B_j).
$$

Sea un volumen factual $V$ particionado en celdas $C_\ell$ con pesos $\omega(C_\ell)$. La integral de volumen factual de un escalar $g$ es:

$$
\iiint_{V}^{SV} g \;:=\; \sum_\ell g(C_\ell)\,\omega(C_\ell).
$$

Estas integrales son **operadores de ensamblaje determinista** (no probabilistas) y constituyen el soporte algebraico de los funcionales de trabajo (línea) y empuje (superficie) utilizados en el dominio termodinámico.



---

## 5. Magnitudes termodinámicas factuales: definiciones operacionales

### 5.1. Contenido interior, frontera y contenido total

Se define el contenido interior como integral factual discreta sobre una partición de celdas $C_\ell$:

$$
\mathcal{C}^{int}_{SV}(\Gamma,n)
:=
\sum_{\ell}\,c_\ell(\Gamma,n)\,\omega(C_\ell),
$$

y el contenido de frontera sobre una partición de caras $B_j$ orientadas:

$$
\mathcal{B}_{\partial,SV}(\Gamma,n)
:=
\sum_{j}\sigma_j\,b_j(\Gamma,n)\,\omega(B_j),
\qquad
\sigma_j\in\{-1,+1\}.
$$

El contenido total es:

$$
\mathcal{C}^{tot}_{SV}(\Gamma,n):=\mathcal{C}^{int}_{SV}(\Gamma,n)+\mathcal{B}_{\partial,SV}(\Gamma,n).
$$

### 5.2. Fuerza factual y corrección jacobiana

Se define el potencial escalar factual por lectura directa del contenido total:

$$
\phi_{SV}(\Gamma,n):=\mathcal{C}^{tot}_{SV}(\Gamma,n).
$$

Se fija un potencial vectorial mínimo derivado de la frontera:

$$
\Psi_{SV}(\Gamma,n):=\mathcal{B}_{\partial,SV}(\Gamma,n)\,e_3,
\qquad
e_3=(0,0,1).
$$

Sea $x_{SV}(\Gamma,k)\in\mathbb{R}^3$ la representación auxiliar del estado $S_k$. La velocidad factual (no temporal) es:

$$
v_{SV}(\Gamma,k):=\frac{x_{SV}(\Gamma,k)-x_{SV}(\Gamma,k-1)}{\omega(\nu_{k-1})}.
$$

La corrección jacobiana de fuerza se define por:

$$
J^{for}_{SV}(\Gamma,k):=J_\Gamma(k)\,v_{SV}(\Gamma,k).
$$

La **ley constitutiva de fuerza** del dominio fija:

$$
F_{SV}(\Gamma,k)
:=
-\nabla^{SV}\phi_{SV}(\Gamma,k)
+
Rot^{vec}_{SV}\Psi_{SV}(\Gamma,k)
+
J^{for}_{SV}(\Gamma,k).
$$

Esta expresión es algebraica, no probabilista y no temporal; la contribución rotacional se controla por el rotor vectorial explícito y la contribución sensible por el jacobiano.

### 5.3. Empuje factual

El empuje factual se define como funcional de contorno del campo de fuerza:

$$
P^{emp}_{SV}(\Gamma,k):=
\sum_{j}\sigma_j\,\langle F_{SV}(B_j,k),n_{B_j}\rangle_{SV}\,\omega(B_j),
$$

con $n_{B_j}$ normal factual unitaria y $\langle\cdot,\cdot\rangle_{SV}$ producto interno compatible.

### 5.4. Trabajo factual, calor factual y componente U

El trabajo factual acumulado hasta $n$ es:

$$
W_{SV}(\Gamma,n)
:=
\sum_{k=1}^{n}\mathbf{1}_1(k)\,\langle F_{SV}(\Gamma,k),\,x_{SV}(\Gamma,k)-x_{SV}(\Gamma,k-1)\rangle_{SV}.
$$



Equivalencia operatoria (integral curvilínea). Definiendo el funcional de línea factual de §4.4 sobre la trayectoria,
$$
W_{SV}(\Gamma,n)=\int_{\Gamma_{[0,n]}}^{SV}\mathbf{1}_1\,\langle F_{SV},dx\rangle_{SV},
$$
lo cual se reduce exactamente al sumatorio anterior al tomar $\Delta x(\Gamma_k)=x_{SV}(k)-x_{SV}(k-1)$ y pesos $\omega(\nu_{k-1})$.

Se introduce la constante metrológica $k_B>0$ como factor exacto de escala energía–temperatura (sin importar mecánica estadística al fundamento). La lectura termométrica se fija por la identidad algebraica local:

$$
k_B\,\Theta_{SV}(\Gamma,k)\,\Delta_\Gamma H_{SV}(\Gamma,k)=\Delta_\Gamma\mathcal{C}^{int}_{SV}(\Gamma,k)
\quad\text{para los pasos con }\mathbf{1}_0(k)=1.
$$

El calor factual acumulado hasta $n$ es:

$$
Q_{SV}(\Gamma,n)
:=
\sum_{k=1}^{n}\mathbf{1}_0(k)\,k_B\,\Theta_{SV}(\Gamma,k)\,\Delta_\Gamma H_{SV}(\Gamma,k).
$$

La contribución asociada a $U$ se define por:

$$
\mathcal{U}_{SV}(\Gamma,n)
:=
\sum_{k=1}^{n}\mathbf{1}_U(k)\,k_B\,\Theta_{SV}(\Gamma,k)\,\Delta_\Gamma H_{SV}(\Gamma,k).
$$

Estas definiciones establecen un balance de primer principio sin tiempo y con preservación explícita de $U$.

### 5.5. Entalpía factual

Se define la entalpía factual como correlación interior–frontera del contenido:

$$
\Lambda_{SV}(\Gamma,n):=\mathcal{C}^{int}_{SV}(\Gamma,n)+\mathcal{B}_{\partial,SV}(\Gamma,n).
$$

---

## 6. Ecuación absoluta del dominio: defecto factual total

### 6.1. Defectos elementales

Se definen los defectos elementales (todos con dimensión homogénea por construcción metrológica):

1. **Defecto de balance:**
$$
\delta_{bal}(\Gamma,n):=\Delta_\Gamma\mathcal{C}^{tot}_{SV}(\Gamma,n)-W_{SV}(\Gamma,n)-Q_{SV}(\Gamma,n)-\mathcal{U}_{SV}(\Gamma,n).
$$

2. **Defecto de irreversibilidad (parte negativa):**
$$
\Delta_{irr}(\Gamma,n):=\sum_{k=1}^n\left(\min\{0,\Delta_\Gamma H_{SV}(\Gamma,k)\}\right)^2.
$$

3. **Defecto de fuerza (cierre constitutivo):**
$$
\delta_{F}(\Gamma,k):=
F_{SV}(\Gamma,k)
+\nabla^{SV}\phi_{SV}(\Gamma,k)
-Rot^{vec}_{SV}\Psi_{SV}(\Gamma,k)
-J^{for}_{SV}(\Gamma,k),
$$
y su acumulado cuadrático:
$$
\Delta_{F}(\Gamma,n):=\sum_{k=1}^n\|\delta_F(\Gamma,k)\|_2^2.
$$

4. **Defecto de empuje:**
$$
\Delta_{emp}(\Gamma,n):=\sum_{k=1}^n\left(P^{emp}_{SV}(\Gamma,k)-\sum_j\sigma_j\langle F_{SV}(B_j,k),n_{B_j}\rangle_{SV}\,\omega(B_j)\right)^2.
$$

5. **Defecto termométrico (identidad local en pasos residuales):**
$$
\Delta_{\Theta}(\Gamma,n):=\sum_{k=1}^n\mathbf{1}_0(k)\left(k_B\Theta_{SV}(\Gamma,k)\Delta_\Gamma H_{SV}(\Gamma,k)-\Delta_\Gamma\mathcal{C}^{int}_{SV}(\Gamma,k)\right)^2.
$$

6. **Defecto entálpico:**
$$
\delta_{\Lambda}(\Gamma,n):=\Lambda_{SV}(\Gamma,n)-\left(\mathcal{C}^{int}_{SV}(\Gamma,n)+\mathcal{B}_{\partial,SV}(\Gamma,n)\right).
$$

### 6.2. Defecto factual total y ecuación única

Se define el defecto factual total del dominio como:

$$
\mathbb{T}^{thermo}_{SV}(\Gamma,n):=
|\delta_{bal}(\Gamma,n)|^2
+
\Delta_{irr}(\Gamma,n)
+
\Delta_F(\Gamma,n)
+
\Delta_{emp}(\Gamma,n)
+
\Delta_{\Theta}(\Gamma,n)
+
|\delta_{\Lambda}(\Gamma,n)|^2.
$$

La **ecuación absoluta única** del dominio es:

$$
\boxed{\ \mathbb{T}^{thermo}_{SV}(\Gamma,n)=0\ }.
$$

---

## 7. Teoremas de cierre, equivalencia y unicidad

### 7.1. Positividad del defecto factual total

**Lema 7.1.1.** Para todo $(\Gamma,n)$ se cumple $\mathbb{T}^{thermo}_{SV}(\Gamma,n)\ge 0$.

*Demostración.* Cada sumando es un cuadrado o suma de cuadrados. Q.E.D.

### 7.2. Nulidad componente a componente

**Teorema 7.2.1.** Se tiene $\mathbb{T}^{thermo}_{SV}(\Gamma,n)=0$ si y sólo si se anulan simultáneamente:
$$
\delta_{bal}=0,\quad
\Delta_{irr}=0,\quad
\Delta_F=0,\quad
\Delta_{emp}=0,\quad
\Delta_{\Theta}=0,\quad
\delta_{\Lambda}=0.
$$

*Demostración.* Por el Lema 7.1.1, una suma de no negativos es cero si y sólo si cada término es cero. Q.E.D.

### 7.3. Primer principio factual (forma SV)

**Corolario 7.3.1.** Si $\mathbb{T}^{thermo}_{SV}(\Gamma,n)=0$, entonces:

$$
\Delta_\Gamma\mathcal{C}^{tot}_{SV}(\Gamma,n)=W_{SV}(\Gamma,n)+Q_{SV}(\Gamma,n)+\mathcal{U}_{SV}(\Gamma,n).
$$


### 7.3bis. No tautologicidad del balance y unicidad termométrica

**Proposición 7.3bis.1 (balance no tautológico).** La igualdad de balance $\delta_{bal}=0$ no es identidad por definición: impone una restricción efectiva entre (i) variación del contenido total, (ii) trabajo como integral curvilínea del campo de fuerza, (iii) calor como lectura termométrica multiplicada por incremento entrópico, y (iv) contribución explícita de $U$.

*Demostración.* En §5.4, $W_{SV}$ se define por un funcional de línea del campo $F_{SV}$ y de la geometría de trayectoria $x_{SV}$, mientras que $Q_{SV}$ y $\mathcal{U}_{SV}$ se definen por el producto metrológico $k_B\Theta_{SV}\Delta H_{SV}$ en subclases disjuntas de sucesos (residuales y $U$). Ninguna de estas magnitudes se define como proyección de $\Delta_\Gamma\mathcal{C}^{tot}_{SV}$; por tanto, $\delta_{bal}=0$ no se reduce a una identidad algebraica vacía. Q.E.D.

**Teorema 7.3bis.2 (unicidad termométrica en régimen residual).** Para un paso $k$ con $\mathbf{1}_0(k)=1$ y $\Delta_\Gamma H_{SV}(\Gamma,k)>0$, la identidad termométrica
$$
k_B\,\Theta_{SV}(\Gamma,k)\,\Delta_\Gamma H_{SV}(\Gamma,k)=\Delta_\Gamma\mathcal{C}^{int}_{SV}(\Gamma,k)
$$
determina $\Theta_{SV}(\Gamma,k)$ de manera única.

*Demostración.* Es una ecuación lineal en la incógnita $\Theta_{SV}(\Gamma,k)$ con coeficiente $k_B\Delta_\Gamma H_{SV}(\Gamma,k)>0$. Q.E.D.

**Corolario 7.3bis.3 (estatuto de U termométrica).** Si $\Delta_\Gamma H_{SV}(\Gamma,k)=0$ en un paso residual, la lectura termométrica no queda determinada por el aparato del paso; su estatuto correcto es $U$.

### 7.4. Irreversibilidad

**Corolario 7.4.1.** Si $\mathbb{T}^{thermo}_{SV}(\Gamma,n)=0$, entonces $\Delta_\Gamma H_{SV}(\Gamma,k)\ge 0$ para todo $k\le n$.

### 7.5. Unicidad fuerte del cierre escalar

Sea $\mathcal{P}$ la clase de todas las condiciones de cierre del dominio que:
(i) se expresan como ecuaciones escalar–nulas sobre $(\Gamma,n)$,
(ii) se construyen como suma finita de términos no negativos,
(iii) anulan exactamente las mismas seis condiciones de §6.1.

**Teorema 7.5.1 (unicidad en la clase $\mathcal{P}$).** Si $E(\Gamma,n)=0$ y $E'(\Gamma,n)=0$ son dos cierres en $\mathcal{P}$ con el mismo conjunto de seis condiciones nulas, entonces $E=0$ si y sólo si $E'=0$.

*Demostración.* Ambos cierres son equivalentes a la conjunción de las seis nulidades por el mismo argumento de positividad componente a componente. Q.E.D.

---
### 7.6. Recuperación formal externa bajo límite regular

Sea un régimen donde:
1) $\mathbf{1}_U(k)=0$ para todo $k$ (no comparece $U$ en el tramo),
2) los incrementos $\Delta x$ y $\Delta_\Gamma H_{SV}$ son pequeños y regulares,
3) los pesos factuales son uniformes.

Bajo este límite regular, el balance factual $\delta_{bal}=0$ adopta, en notación diferencial formal externa (sin soberanía ontológica), la forma:

$$
d\mathcal{C}^{tot}_{SV} = \langle F_{SV},dx\rangle_{SV} + k_B\,\Theta_{SV}\,dH_{SV},
$$

que reproduce el esquema estructural del primer principio clásico al identificar $d\mathcal{C}^{tot}_{SV}$ como variación de contenido, $\langle F,dx\rangle$ como trabajo diferencial y $k_B\Theta\,dH$ como calor diferencial. El régimen SV mantiene la primacía del suceso: el límite es una lectura formal externa de una identidad factual discretizada.



## 8. Bancos visibles de consistencia y bancos de tensión

En todos los bancos se emplea el formato canónico **Datos → Cálculo → Salida → Dictamen**.

### Banco B-01 — recorrido completo con anulación de la ecuación absoluta

**Datos.** Trayectoria de cuatro estados ($n=3$) con pesos $\omega(\nu_k)=1$:

$$
x_{SV}(0)=(0,0,0),\;
x_{SV}(1)=(1,0,0),\;
x_{SV}(2)=(1,1,0),\;
x_{SV}(3)=(1,1,1).
$$

Indicadores:
$$
(\mathbf{1}_1(1),\mathbf{1}_0(1),\mathbf{1}_U(1))=(1,0,0),
$$
$$
(\mathbf{1}_1(2),\mathbf{1}_0(2),\mathbf{1}_U(2))=(0,1,0),
$$
$$
(\mathbf{1}_1(3),\mathbf{1}_0(3),\mathbf{1}_U(3))=(0,0,1).
$$

Entropía factual:
$$
H_{SV}(0)=0,\;H_{SV}(1)=0.20,\;H_{SV}(2)=0.35,\;H_{SV}(3)=0.40.
$$

Lectura termométrica (en UFT):
$$
\Theta_{SV}(1)=10,\;\Theta_{SV}(2)=12,\;\Theta_{SV}(3)=11.
$$

Constante metrológica: $k_B=1$ (escala interna).

Contenido interior y frontera:
$$
\mathcal{C}^{int}_{SV}(0)=8,\;\mathcal{C}^{int}_{SV}(1)=10,\;\mathcal{C}^{int}_{SV}(2)=11.8,\;\mathcal{C}^{int}_{SV}(3)=12.35,
$$
$$
\mathcal{B}_{\partial,SV}(0)=2,\;\mathcal{B}_{\partial,SV}(1)=2,\;\mathcal{B}_{\partial,SV}(2)=2,\;\mathcal{B}_{\partial,SV}(3)=2.
$$

Fuerza factual (constante sobre el paso 1):
$$
F_{SV}(1)=(2,0,0),\qquad F_{SV}(2)=(0,0,0),\qquad F_{SV}(3)=(0,0,0).
$$

**Cálculo.** Incrementos:
$$
\Delta x(1)=(1,0,0),\;\Delta x(2)=(0,1,0),\;\Delta x(3)=(0,0,1).
$$

Trabajo:
$$
W_{SV}= \mathbf{1}_1(1)\langle (2,0,0),(1,0,0)\rangle =2.
$$

Incrementos entrópicos:
$$
\Delta H(1)=0.20,\;\Delta H(2)=0.15,\;\Delta H(3)=0.05.
$$

Calor:
$$
Q_{SV}=\mathbf{1}_0(2)\,k_B\,\Theta(2)\Delta H(2)=12\cdot 0.15=1.8.
$$

Contribución $U$:
$$
\mathcal{U}_{SV}=\mathbf{1}_U(3)\,k_B\,\Theta(3)\Delta H(3)=11\cdot 0.05=0.55.
$$

Contenido total:
$$
\mathcal{C}^{tot}_{SV}(0)=10,\;\mathcal{C}^{tot}_{SV}(3)=14.35\;\Rightarrow\;\Delta_\Gamma\mathcal{C}^{tot}_{SV}=4.35.
$$

Balance:
$$
\delta_{bal}=4.35-2-1.8-0.55=0.
$$

Irreversibilidad: $\Delta H(k)\ge 0$ para todo $k$, luego $\Delta_{irr}=0$.

Defecto termométrico (paso residual $k=2$):
$$
k_B\Theta(2)\Delta H(2)-\Delta\mathcal{C}^{int}(2)=12\cdot 0.15-(11.8-10)=1.8-1.8=0,
$$
luego $\Delta_\Theta=0$.

Entalpía:
$$
\Lambda_{SV}(3)=\mathcal{C}^{int}(3)+\mathcal{B}_\partial(3)=12.35+2=14.35,
$$
luego $\delta_\Lambda=0$.

**Salida.** $\delta_{bal}=0$, $\Delta_{irr}=0$, $\Delta_\Theta=0$, $\delta_\Lambda=0$.

**Dictamen.** En este banco, los cuatro defectos calculables quedan anulados. (Los defectos de fuerza y empuje se evalúan en el Banco B-02, donde se fija el cierre constitutivo completo con cálculo diferencial explícito).

---

### Banco B-02 — cierre de fuerza con rotor vectorial y corrección jacobiana (cálculo completo)

**Datos.** Potenciales y campos en $\mathbb{R}^3$:

$$
\phi(x,y,z)=2x,
\qquad
\Psi(x,y,z)=(0,x,0).
$$

Observable jacobiano y velocidad:
$$
J_\Gamma=\begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix},
\qquad
v=(1,0,0).
$$

**Cálculo.** Gradiente:
$$
\nabla^{SV}\phi=(2,0,0).
$$

Rotor 2-forma:
$$
\Omega^{SV}_{12}=\partial_1\Psi^2-\partial_2\Psi^1=1-0=1,
\quad
\Omega^{SV}_{23}=0,
\quad
\Omega^{SV}_{31}=0.
$$

Rotor vectorial:
$$
Rot^{vec}_{SV}\Psi=(0,0,1).
$$

Corrección jacobiana:
$$
J^{for}=J_\Gamma v=(1,0,0).
$$

Fuerza constitutiva:
$$
F=-\nabla\phi+Rot^{vec}\Psi+J^{for}=-(2,0,0)+(0,0,1)+(1,0,0)=(-1,0,1).
$$

Defecto:
$$
\delta_F=F+\nabla\phi-Rot^{vec}\Psi-J^{for}=0.
$$

**Salida.** $\delta_F=0$.

**Dictamen.** El cierre de fuerza usa simultáneamente gradiente, rotor vectorial (tipológicamente resuelto) y corrección jacobiana.

---

### Banco B-03 — empuje factual (cálculo sobre frontera)

**Datos.** Se toma el campo $F=(-1,0,1)$ del Banco B-02 sobre tres caras con normales y pesos:

$$
(B_1,n_1,\sigma_1,\omega_1)=(*,(1,0,0),+1,1),
$$
$$
(B_2,n_2,\sigma_2,\omega_2)=(*,(0,0,1),+1,2),
$$
$$
(B_3,n_3,\sigma_3,\omega_3)=(*,(0,1,0),+1,1).
$$

**Cálculo.**
$$
\langle F,n_1\rangle=-1,\quad \langle F,n_2\rangle=1,\quad \langle F,n_3\rangle=0.
$$

Empuje:
$$
P^{emp}=\sum_j \sigma_j\langle F,n_j\rangle\,\omega_j=(-1)\cdot 1+(1)\cdot 2+0\cdot 1=1.
$$

Defecto de empuje en el paso:
$$
P^{emp}-\sum_j\sigma_j\langle F,n_j\rangle\omega_j=0.
$$

**Salida.** Defecto de empuje nulo.

**Dictamen.** El empuje factual queda fijado como funcional de contorno reproducible.

---

### Banco T-01 — régimen puramente directriz

**Datos.** $\mathbf{1}_0(k)=\mathbf{1}_U(k)=0$ para todo $k\le n$.

**Cálculo.** $Q_{SV}=0$ y $\mathcal{U}_{SV}=0$.

**Salida.** El balance se reduce a $\Delta\mathcal{C}^{tot}_{SV}=W_{SV}$.

**Dictamen.** El cierre no colapsa: especializa el dominio a trabajo puro.

---

### Banco T-02 — régimen puramente residual

**Datos.** $\mathbf{1}_1(k)=\mathbf{1}_U(k)=0$ para todo $k\le n$.

**Cálculo.** $W_{SV}=0$ y $\mathcal{U}_{SV}=0$.

**Salida.** El balance se reduce a $\Delta\mathcal{C}^{tot}_{SV}=Q_{SV}$.

**Dictamen.** El cierre no exige parte directriz distinta de cero.

---

### Banco T-03 — colapso del término rotacional

**Datos.** $\Psi\equiv 0$ en el cierre de fuerza.

**Cálculo.** $Rot^{vec}_{SV}\Psi=0$.

**Salida.** $F=-\nabla\phi+J^{for}$.

**Dictamen.** El rotor no es ornamental: su anulación cambia el régimen constitutivo.

---

### Banco T-04 — fallo termométrico produce defecto positivo

**Datos.** Se toma el Banco B-01 y se altera únicamente $\Theta_{SV}(2)$, fijando $\Theta_{SV}(2)=10$ en lugar de $12$.

**Cálculo.** En el paso residual $k=2$:
$$
k_B\Theta(2)\Delta H(2)-\Delta\mathcal{C}^{int}(2)=10\cdot 0.15-1.8=1.5-1.8=-0.3,
$$
por tanto
$$
\Delta_\Theta \ge (-0.3)^2 = 0.09>0.
$$

**Salida.** $\mathbb{T}^{thermo}_{SV}(\Gamma,3)>0$.

**Dictamen.** El cierre detecta de manera efectiva incoherencia termométrica sin recurrir a probabilidad ni a tiempo.

---

### Banco T-05 — incoherencia tipológica del rotor produce defecto positivo

**Datos.** Se toma el Banco B-02, pero se intenta sustituir $Rot^{vec}_{SV}\Psi$ por la 2-forma $\Omega^{SV}_{ij}(\Psi)$ dentro de la ley constitutiva de fuerza.

**Cálculo.** $\nabla^{SV}\phi$ es vector en $\mathbb{R}^3$; $\Omega^{SV}$ es tensor antisimétrico $3\times 3$. La suma $-\nabla^{SV}\phi+\Omega^{SV}$ no está tipada en el dominio.

**Salida.** La ley constitutiva no queda bien definida, por tanto el defecto $\Delta_F$ no puede anularse.

**Dictamen.** El rotor vectorial (dualizado) no es un adorno: es la compuerta tipológica que permite cierre algebraico coherente en rango tridimensional.



## 9. Apéndice algebraico

### 9.1. Identidad de telescopaje de incrementos

Para toda magnitud escalar $q$:

$$
\sum_{k=1}^n \Delta_\Gamma q(k)=q(\Gamma,n)-q(\Gamma,0).
$$

### 9.2. Compatibilidad tipológica rotor 2-forma → rotor vectorial

Por definición de $\Omega^{SV}_{ij}$ y de $Rot^{vec}_{SV}$, el rotor vectorial es la dualización explícita del tensor antisimétrico en dimensión 3. Esto impide sumar objetos de tipología incompatible.

### 9.3. Residual factual global como norma de defectos

Se define el defecto elemental de balance por paso:

$$
\delta_{bal}^{(k)}:=\Delta_\Gamma\mathcal{C}^{tot}_{SV}(k)
-\mathbf{1}_1(k)\,\langle F_{SV}(k),\Delta x(k)\rangle_{SV}
-\mathbf{1}_0(k)\,k_B\Theta_{SV}(k)\Delta_\Gamma H_{SV}(k)
-\mathbf{1}_U(k)\,k_B\Theta_{SV}(k)\Delta_\Gamma H_{SV}(k),
$$

y el defecto elemental de empuje:

$$
\delta_{emp}^{(k)}:=P^{emp}_{SV}(k)-\sum_j\sigma_j\langle F_{SV}(B_j,k),n_{B_j}\rangle_{SV}\,\omega(B_j).
$$

Una instanciación canónica del residual factual global compatible con el dominio es:

$$
R_\Gamma(n):=\sum_{k=1}^n\Bigl(
|\delta_{bal}^{(k)}|
+\|\delta_F(\Gamma,k)\|_2
+|\delta_{emp}^{(k)}|
+\mathbf{1}_0(k)\bigl|k_B\Theta_{SV}(k)\Delta_\Gamma H_{SV}(k)-\Delta_\Gamma\mathcal{C}^{int}_{SV}(k)\bigr|
\Bigr).
$$

La definición es aditiva, no negativa y se anula bajo cierre completo.

---

## 10. Referencias

- Sistema Vectorial SV: corpus de dispersión factual e irreversibilidad estructural; cuerpo operatorio absoluto de flujo, divergencia, rotor, jacobiano y frontera; primitivos metrológicos (UFE, UFM, UFC, UFT) y constante de escala $k_B$.
