# Fuerza, trabajo, calor, entalpía, temperatura, principios y fundamentos de la termodinámica y la correlación entre ellos en el SV

**© 2026. Todos los derechos reservados.** | **Juan Antonio Lloret Egea** | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 23/04/2026

---

## Resumen

Este documento fija el régimen termodinámico factual del Sistema Vectorial SV como dominio algebraico cerrado sobre sucesos, no sobre tiempo soberano. Su suelo constitutivo es el estrato preternario de pares admisibles \((\alpha_i,\beta_i)\), del cual se derivan el sesgo factual local, la activación factual, la cadena de irreversibilidad y la entropía factual final \(H_{SV}\). Sobre ese suelo se demuestra la necesidad algebraica de una magnitud factual total \(\mathfrak{C}^{tot}_{SV}\), de una acumulación factual \(\mathfrak{A}_{SV}\), de una frontera factual explícita \(\mathcal{B}_{\partial,SV}\), de un residual factual \(R_{\Gamma}\) y de una componente de no clausura legítima \(\mathcal{N}^{reap}_{SV}\). El conjunto se compacta en una única ecuación soberana del dominio,

$$
\mathbb{T}^{thermo}_{SV}(\Gamma,n)
=
\left(
\Delta_{\Gamma}\mathfrak{C}^{tot}_{SV}(n)
-
\mathcal{W}_{SV}(\Gamma,n)
-
\mathcal{Q}_{SV}(\Gamma,n)
-
\mathcal{N}^{reap}_{SV}(\Gamma,n),
\;-
\Delta_{\Gamma}H_{SV}(\Gamma,n)
\right),
$$

sujeta a la condición de régimen fuerte

$$
\mathbb{T}^{thermo}_{SV}(\Gamma,n)\in \{0\}\times \mathbb{R}_{\le 0}.
$$

Trabajo factual, calor factual, temperatura factual, fuerza factual, empuje factual y entalpía factual no comparecen como primitivas del dominio, sino como magnitudes derivadas, absorbidas y trazables dentro del régimen único. El documento desarrolla las propiedades algebraicas absolutas del operador maestro, demuestra su irreducibilidad, su unicidad representacional y su resistencia frente a ataques negativos que intentan reducir el dominio a una formulación escalar, a gradiente puro, a tiempo soberano o a integrales clásicas constitutivas. El cierre final es fuerte: no existe otra ecuación independiente del dominio; toda formulación alternativa es reducible a \(\mathbb{T}^{thermo}_{SV}\) o inconsistente con el aparato del SV.

**Palabras clave:** Sistema Vectorial SV; termodinámica factual; entropía factual; irreversibilidad estructural; contenido factual total; operador único del régimen; trabajo factual; calor factual; temperatura factual; fuerza factual; empuje factual; entalpía factual; trazabilidad factual; prioridad operatoria.

---

## Abstract

This document fixes the factual thermodynamic regime of the Sistema Vectorial SV as a closed algebraic domain built on events rather than sovereign time. Its constitutive ground is the preternary stratum of admissible pairs \((\alpha_i,\beta_i)\), from which local factual bias, factual activation, the irreversibility chain and the final factual entropy \(H_{SV}\) are derived. On that ground the document proves the algebraic necessity of a total factual content \(\mathfrak{C}^{tot}_{SV}\), a factual accumulation \(\mathfrak{A}_{SV}\), an explicit factual boundary \(\mathcal{B}_{\partial,SV}\), a factual residual \(R_{\Gamma}\) and a legitimate non-closure component \(\mathcal{N}^{reap}_{SV}\). The whole domain is compacted into a single sovereign equation,

$$
\mathbb{T}^{thermo}_{SV}(\Gamma,n)
=
\left(
\Delta_{\Gamma}\mathfrak{C}^{tot}_{SV}(n)
-
\mathcal{W}_{SV}(\Gamma,n)
-
\mathcal{Q}_{SV}(\Gamma,n)
-
\mathcal{N}^{reap}_{SV}(\Gamma,n),
\;-
\Delta_{\Gamma}H_{SV}(\Gamma,n)
\right),
$$

under the strong-regime condition

$$
\mathbb{T}^{thermo}_{SV}(\Gamma,n)\in \{0\}\times \mathbb{R}_{\le 0}.
$$

Factual work, factual heat, factual temperature, factual force, factual thrust and factual enthalpy are not primitive magnitudes but derived, absorbed and traceable within the unique regime. The document develops the absolute algebraic properties of the master operator, proves its irreducibility, its representational uniqueness and its resistance against negative attacks that attempt to reduce the domain to a scalar formulation, to a pure gradient, to sovereign time or to constitutive classical integrals. The closure is strong: there is no other independent equation for the domain; every alternative formulation is either reducible to \(\mathbb{T}^{thermo}_{SV}\) or inconsistent with the SV apparatus.

---

## Índice

1. Introducción y estatuto del dominio  
2. Suelo preternario del dominio termodinámico factual  
3. Cadena factual de irreversibilidad y entropía factual  
4. Magnitudes madre del dominio  
5. Prioridad operatoria del aparato del SV  
6. Ecuación maestra y operador único del régimen  
7. Trabajo factual y calor factual  
8. Temperatura factual  
9. Fuerza factual y empuje factual  
10. Entalpía factual  
11. Propiedades algebraicas absolutas del operador maestro termodinámico  
12. Ataques negativos y prueba de irreducibilidad  
13. Recorrido de consistencia visible y exigencias laboratorias  
14. Conclusión  
15. Referencias

---

## 1. Introducción y estatuto del dominio

El presente documento no traduce la termodinámica clásica al lenguaje del SV, no reetiqueta magnitudes heredadas y no concede soberanía a tiempo, probabilidad, estadística, minería de datos ni inferencia opaca. Su objeto es más estricto: fijar, dentro del aparato ya disponible del Sistema Vectorial SV, el dominio termodinámico factual y demostrar que ese dominio queda gobernado por una única ecuación soberana. La tarea no consiste en declarar una unicidad por autoridad verbal, sino en levantar un aparato en el que cualquier formulación alternativa resulte o bien reducible al régimen aquí fijado o bien incompatible con el suelo doctrinal y algebraico del sistema.

El documento adopta cuatro reglas duras.

**Regla 1 — Primacía del suceso.** Toda variación del dominio se ordena por sucesos y por índices factuales de suceso. No se admite tiempo soberano como variable constitutiva.

**Regla 2 — Primacía del suelo preternario.** Ninguna magnitud alta del dominio precede al sistema de pares admisibles \((\alpha_i,\beta_i)\).

**Regla 3 — Prioridad operatoria del SV.** Cuando el aparato ya disponible del sistema basta para resolver una necesidad local, no procede introducir herramientas externas de potencia soberana superior.

**Regla 4 — Clausura interna de lo nuclear.** Toda pieza central nombrada y tratada en el documento debe quedar cerrada en esta misma publicación.

Estas reglas imponen una consecuencia inmediata: trabajo factual, calor factual, temperatura factual, fuerza factual, empuje factual y entalpía factual no pueden entrar en el dominio como nombres heredados de la física clásica. Deben derivarse algebraicamente desde el régimen factual del SV.

---

## 2. Suelo preternario del dominio termodinámico factual

Sea el sistema de pares admisibles

$$
(\alpha_i,\beta_i),\qquad i=1,\dots,N.
$$

Se definen, para cada par, el sesgo factual local y la activación factual

$$
\delta_i := \beta_i-\alpha_i,
\qquad
 a_i := |\delta_i|.
$$

El sesgo factual local \(\delta_i\) no es todavía una magnitud termodinámica; es el primer indicador de orientación estructural mínima del dominio. La activación factual \(a_i\) no es calor, ni trabajo, ni temperatura; es sólo el módulo factual local de la separación preternaria. Pero sin \(\delta_i\) y \(a_i\), el dominio no puede levantar ninguna magnitud ulterior sin romper su trazabilidad.

**Axioma 2.1 — Prioridad absoluta del suelo preternario.** Ninguna magnitud central del dominio termodinámico factual posee estatuto más originario que \((\alpha_i,\beta_i)\).

**Demostración.** Toda magnitud del dominio será construida, directa o indirectamente, mediante operadores que actúan sobre activación factual, sesgo factual o sus concentraciones y canalizaciones. Si una magnitud central precediera a \((\alpha_i,\beta_i)\), quedaría fuera de trazabilidad factual descendente. Luego no puede preceder al suelo preternario. QED.

**Lema 2.2 — No banalidad de \(U\).** El símbolo \(U\) conserva estatuto de indeterminación honesta y no puede convertirse en cierre favorable del dominio.

**Demostración.** Si \(U\) se convirtiera en cierre favorable, el dominio sustituiría estructura por plausibilidad. Ello contradice la disciplina constitutiva del SV. QED.

---

## 3. Cadena factual de irreversibilidad y entropía factual

Sobre el suelo preternario se define la cadena factual de irreversibilidad

$$
(\alpha_i,\beta_i)
\rightsquigarrow
(\delta_i,a_i)
\rightsquigarrow
H_{pre}
\rightsquigarrow
H_{K_3}
\rightsquigarrow
H_{\Xi}
\rightsquigarrow
H_{\Sigma_c}
\rightsquigarrow
H_{\Sigma_k}
\rightsquigarrow
H_{SV}.
$$

El documento no necesita reconstruir aquí toda la teoría de esos estratos; sí necesita fijar su función exacta en el dominio tratado.

- \(H_{pre}\) recoge la dispersión factual preternaria.  
- \(H_{K_3}\) transporta esa dispersión a la terna inducida.  
- \(H_{\Xi}\) enriquece el régimen con jacobiano y residualidad.  
- \(H_{\Sigma_c}\) concentra factualidad.  
- \(H_{\Sigma_k}\) canaliza factualidad.  
- \(H_{SV}\) absorbe estratificadamente toda la cadena.

**Teorema 3.1 — Absorción estratificada factual.** La entropía factual final \(H_{SV}\) absorbe ordenadamente los estratos anteriores sin colapso ni salto no auditable.

**Demostración.** Cada estrato añade una capa factual compatible con el anterior: \(H_{K_3}\) no destruye \(H_{pre}\), sino que lo transporta; \(H_{\Xi}\) no destruye \(H_{K_3}\), sino que lo enriquece con jacobiano y residual; \(H_{\Sigma_c}\) y \(H_{\Sigma_k}\) reorganizan factualidad sin anular el suelo ya fijado. Si \(H_{SV}\) no absorbiera estratificadamente esas capas, la entropía factual sería un salto no trazable. Luego la absorción es estratificada. QED.

**Teorema 3.2 — Irreversibilidad estructural factual.** Sea \(\Gamma\) una trayectoria factual admisible. Entonces, para cualesquiera \(n_2\ge n_1\),

$$
H_{SV}(\Gamma,n_2)\ge H_{SV}(\Gamma,n_1).
$$

**Demostración.** Por el Teorema 3.1, \(H_{SV}\) es el cierre absorbente de la cadena factual de irreversibilidad. Si decreciera efectivamente en una trayectoria admisible, o bien la trayectoria no sería factual y admisible, o bien habría reescritura retroactiva, o bien habría pérdida de honestidad estructural. Ninguna de esas tres condiciones es compatible con el dominio. Luego \(H_{SV}\) no decrece. QED.

La primera consecuencia dura es que la segunda componente del operador soberano del dominio no podrá ser otra que el signo opuesto de \(\Delta_{\Gamma}H_{SV}\).

---

## 4. Magnitudes madre del dominio

La entropía factual final fija la orientación irreversible del dominio, pero no basta para balancearlo. El régimen necesita, además, magnitudes madres que permitan distinguir acumulación, borde, residualidad y no clausura legítima.

Se introducen las siguientes magnitudes.

### 4.1. Acumulación factual de trayectoria

$$
\mathfrak{A}_{SV}(\Gamma,n).
$$

Recoge el espesor factual acumulativo del recorrido. No es todavía trabajo factual.

### 4.2. Residual factual

$$
R_{\Gamma}(n).
$$

Recoge la parte del régimen que no queda absorbida por acumulación directa.

### 4.3. Frontera factual explícita

$$
\mathcal{B}_{\partial,SV}(\Gamma,n).
$$

Recoge el balance factual de borde, superficie activa y contorno.

### 4.4. No clausura legítima

$$
\mathcal{N}^{reap}_{SV}(\Gamma,n).
$$

Recoge la parte del dominio cuya absorción favorable constituiría una clausura espuria.

### 4.5. Contenido factual total

$$
\mathfrak{C}^{tot}_{SV}(\Gamma,n).
$$

El contenido factual total no es una energía clásica rebautizada. Es la magnitud madre cuyo cambio puede balancearse dentro del régimen.

**Teorema 4.1 — Necesidad algebraica del contenido factual total.** Dado un dominio cuyo cierre irreversible viene dado por \(H_{SV}\), existe la necesidad algebraica de una magnitud factual total \(\mathfrak{C}^{tot}_{SV}\) cuya variación sea susceptible de partición y balance.

**Demostración.** \(H_{SV}\) orienta irreversiblemente el dominio, pero no discrimina, por sí sola, qué parte del régimen debe leerse como acumulación, qué parte como borde activo, qué parte como residualidad y qué parte como no clausura legítima. Si el dominio ha de balancearse algebraicamente, necesita una magnitud factual total distinta de la entropía factual. Luego \(\mathfrak{C}^{tot}_{SV}\) es necesaria. QED.

**Definición 4.2 — Construcción factual fuerte de \(\mathfrak{C}^{tot}_{SV}\).**

$$
\mathfrak{C}^{tot}_{SV}
=
\Pi_C\big(
\mathfrak{A}_{SV},
\iiint_{\mathcal{V}_{SV}}^{SV}\mathcal{G},
\iint_{\Sigma_{SV}}^{SV}\mathcal{F},
R_{\Gamma}
\big),
$$

con \(\Pi_C\) operador de ensamblaje factual de magnitudes ya trazables del régimen.

**Lema 4.3 — Estatuto de \(\Pi_C\).** El operador \(\Pi_C\) no introduce grados de libertad nuevos ni semántica exterior. Sólo ensambla magnitudes ya trazables.

**Demostración.** Sus cuatro entradas son \(\mathfrak{A}_{SV}\), volumen factual, superficie factual y residual factual. Todas ellas pertenecen al aparato del SV o son exigidas por él. Luego \(\Pi_C\) es operador de ensamblaje, no de invención. QED.

---

## 5. Prioridad operatoria del aparato del SV

El dominio termodinámico factual no puede arrancar usando herramientas clásicas más potentes que las necesarias. Debe obedecer una jerarquía dura:

1. herramienta factual ya disponible del SV;  
2. contraste de suficiencia;  
3. escalado operatorio sólo si la suficiencia falla materialmente.

### 5.1. Curvilínea, superficie y volumen factuales

Las herramientas prioritarias son:

$$
\iint_{\Sigma_{SV}}^{SV} \mathcal{F}
:=
\sum_j \sigma_j\,\mathcal{F}(B_j)\,\omega(B_j),
$$

$$
\iiint_{\mathcal{V}_{SV}}^{SV} \mathcal{G}
:=
\sum_k \mathcal{G}(C_k)\,\omega(C_k).
$$

Estas expresiones no son integrales clásicas soberanas; son ensamblajes factuales discretos sobre superficies y volúmenes factuales admisibles.

### 5.2. Flujo factual, divergencia factual y rotor factual

El dominio hereda del aparato factual del SV la legitimidad de flujo factual, divergencia factual y rotor factual como herramientas suficientes para describir borde, redistribución y circulación del régimen. La publicación no reabre aquí su teoría completa; sí los absorbe como parte del aparato legítimo ya construido.

### 5.3. Jacobiano estructural y curvatura factual

Se fija la notación canónica del jacobiano estructural de trayectoria:

$$
\mathcal{J}_{\Gamma,SV}(n).
$$

Y se fija la curvatura factual:

$$
\kappa^{SV}_{\Gamma}(n).
$$

Ninguna de ambas magnitudes posee soberanía semántica propia. Su función es describir distribución local de respuesta dentro del régimen factual del dominio.

**Teorema 5.1 — Suficiencia operatoria interna.** El aparato factual ya disponible del SV basta para construir el núcleo del dominio termodinámico factual tratado en esta publicación.

**Demostración.** La construcción de \(\mathfrak{C}^{tot}_{SV}\), de \(\mathbb{T}^{thermo}_{SV}\), de \(\mathfrak{T}^{fact}_{SV}\), de \(\mathfrak{F}^{fact}_{SV}\), del empuje factual y de \(\mathfrak{H}^{fact}_{SV}\) emplea trayectoria factual, volumen factual, superficie factual, residualidad, jacobiano estructural, curvatura factual y frontera explícita. No resulta necesario introducir un aparato exterior más potente como fundamento. Luego el aparato interno es suficiente. QED.

---

## 6. Ecuación maestra y operador único del régimen

Sobre las magnitudes madre del dominio se define el operador soberano del régimen termodinámico factual:

$$
\mathbb{T}^{thermo}_{SV}(\Gamma,n)
=
\left(
\Delta_{\Gamma}\mathfrak{C}^{tot}_{SV}(n)
-
\mathcal{W}_{SV}(\Gamma,n)
-
\mathcal{Q}_{SV}(\Gamma,n)
-
\mathcal{N}^{reap}_{SV}(\Gamma,n),
\;-
\Delta_{\Gamma}H_{SV}(\Gamma,n)
\right).
$$

La condición de régimen fuerte es

$$
\mathbb{T}^{thermo}_{SV}(\Gamma,n)\in \{0\}\times \mathbb{R}_{\le 0}.
$$

La primera componente expresa el balance factual total del contenido del dominio; la segunda compacta la irreversibilidad factual.

**Lema 6.1 — Descomposición factual total.**

$$
\Delta_{\Gamma}\mathfrak{C}^{tot}_{SV}(n)
=
\mathcal{W}_{SV}(\Gamma,n)
+
\mathcal{Q}_{SV}(\Gamma,n)
+
\mathcal{N}^{reap}_{SV}(\Gamma,n).
$$

**Demostración.** El cambio factual total del dominio no puede agotarse en una lectura binaria entre acumulación y residualidad. Si se eliminara \(\mathcal{N}^{reap}_{SV}\), el régimen blanquearía las regiones de no clausura legítima. Luego la descomposición mínima necesaria del dominio exige las tres componentes del lado derecho. QED.

**Teorema 6.2 — Equivalencia fuerte entre balance e irreversibilidad.** La condición

$$
\mathbb{T}^{thermo}_{SV}(\Gamma,n)\in \{0\}\times \mathbb{R}_{\le 0}
$$

equivale exactamente a la conjunción de:

1. descomposición factual total del contenido, y  
2. no decrecencia de \(H_{SV}\).

**Demostración.** La primera componente del operador se anula si y sólo si vale el Lema 6.1. La segunda pertenece a \(\mathbb{R}_{\le 0}\) si y sólo si \(-\Delta_{\Gamma}H_{SV}\le 0\), esto es, si y sólo si \(\Delta_{\Gamma}H_{SV}\ge 0\). Luego ambas condiciones son equivalentes al régimen fuerte. QED.

**Teorema 6.3 — Unicidad operatoria absoluta.** No existe ecuación independiente distinta de \(\mathbb{T}^{thermo}_{SV}\) que gobierne el dominio termodinámico factual tratado en esta publicación.

**Demostración.** Toda formulación del dominio debe absorber simultáneamente: contenido factual total, trabajo factual, calor factual, no clausura legítima y orientación irreversible. Si una formulación alternativa omitiera alguna de esas cinco piezas, sería incompleta. Si las incluyera todas, sería una reescritura de \(\mathbb{T}^{thermo}_{SV}\). Luego no existe ecuación independiente distinta. QED.

---

## 7. Trabajo factual y calor factual

Trabajo factual y calor factual no son primitivas del dominio; son lecturas internas del operador soberano.

### 7.1. Trabajo factual

$$
\mathcal{W}_{SV}(\Gamma,n)
:=
\Pi_W\big(
\mathfrak{A}_{SV}(\Gamma,n),
\mathcal{B}_{\partial,SV}(\Gamma,n),
\mathcal{J}_{\Gamma,SV}(n)
\big).
$$

El trabajo factual recoge la componente directriz del balance factual del dominio. No equivale sin más a acumulación factual, pero no puede construirse fuera de ella.

### 7.2. Calor factual

$$
\mathcal{Q}_{SV}(\Gamma,n)
:=
\Pi_Q\big(
R_{\Gamma}(n),
\mathcal{B}_{\partial,SV}(\Gamma,n),
\mathcal{J}_{\Gamma,SV}(n)
\big).
$$

El calor factual recoge la componente residual y redistributiva del balance. Tampoco es primitivo.

**Teorema 7.1 — No primitividad de \(\mathcal{W}_{SV}\) y \(\mathcal{Q}_{SV}\).** Trabajo factual y calor factual son funcionales de ensamblaje interno del régimen y no magnitudes soberanas previas a él.

**Demostración.** Tanto \(\mathcal{W}_{SV}\) como \(\mathcal{Q}_{SV}\) dependen de magnitudes madres ya trazables del dominio. Ninguna de ellas antecede a \(\mathfrak{C}^{tot}_{SV}\) ni a \(H_{SV}\). Luego no son primitivas. QED.

---

## 8. Temperatura factual

La temperatura factual no puede reducirse a una función escalar de la entropía factual final. Debe absorber intensidad factual, residualidad, frontera, sensibilidad jacobiana, circulación y curvatura del régimen.

Se define:

$$
\mathfrak{T}^{fact}_{SV}(\Gamma,n)
=
\Pi_T\big(
H_{SV}(\Gamma,n),
R_{\Gamma}(n),
\mathcal{B}_{\partial,SV}(\Gamma,n),
\mathcal{J}_{\Gamma,SV}(n),
Rot_{SV}(\mathfrak{P}^{(v)}_{SV})(\Gamma,n),
\kappa^{SV}_{\Gamma}(n)
\big).
$$

**Teorema 8.1 — No reducción escalar.** No existe una función \(f\) tal que

$$
\mathfrak{T}^{fact}_{SV}=f(H_{SV}).
$$

**Demostración.** El operador \(\mathfrak{T}^{fact}_{SV}\) depende explícitamente de \(R_{\Gamma}\), \(\mathcal{B}_{\partial,SV}\), \(\mathcal{J}_{\Gamma,SV}\), rotor factual y curvatura factual, además de \(H_{SV}\). Si existiera \(f\), todos esos términos quedarían anulados o absorbidos trivialmente por \(H_{SV}\), lo que es falso por definición del operador. Luego la reducción escalar es imposible. QED.

**Teorema 8.2 — Absorción de la temperatura factual en el régimen único.** El operador \(\mathfrak{T}^{fact}_{SV}\) no abre un régimen independiente; queda absorbido por \(\mathbb{T}^{thermo}_{SV}\).

**Demostración.** Todos sus argumentos son magnitudes ya gobernadas por el régimen factual del dominio. Luego el operador se apoya en \(\mathbb{T}^{thermo}_{SV}\) y no lo corrige desde fuera. QED.

---

## 9. Fuerza factual y empuje factual

### 9.1. Fuerza factual

La fuerza factual expresa la presión estructural orientada del régimen. No es una ley clásica masa–aceleración ni un gradiente disfrazado.

Se define:

$$
\mathfrak{F}^{fact}_{SV}(\Gamma,n)
=
-
\nabla^{SV}\mathfrak{P}^{(s)}_{SV}(\Gamma,n)
+
Rot_{SV}(\mathfrak{P}^{(v)}_{SV})(\Gamma,n)
+
\mathfrak{J}^{for}_{SV}(\Gamma,n).
$$

El primer término recoge la directriz estructural; el segundo, la componente circulatoria; el tercero, la corrección jacobiana local.

**Teorema 9.1 — Irreducibilidad respecto del gradiente puro.** No existe \(\phi\) tal que

$$
\mathfrak{F}^{fact}_{SV}=-\nabla^{SV}\phi.
$$

**Demostración.** Si existiera tal \(\phi\), la componente rotacional y la corrección jacobiana serían reducibles a gradiente puro. Pero el segundo término es explícitamente rotacional y el tercero recoge deformación local no reducible a una única función potencial escalar. Luego la reducción es imposible. QED.

### 9.2. Empuje factual

El documento fija además una magnitud derivada de frontera, necesaria para describir la resultante efectiva de la fuerza factual sobre contorno activo. Se define el empuje factual:

$$
\mathfrak{E}^{push}_{SV}(\Gamma,n)
=
\Pi_{push}\big(
\mathfrak{F}^{fact}_{SV}(\Gamma,n),
\mathcal{B}_{\partial,SV}(\Gamma,n),
\mathbf{n}_{\partial}(\Gamma,n)
\big),
$$

donde \(\mathbf{n}_{\partial}\) denota la normal factual de frontera activa. El empuje factual no es una fuerza nueva; es la proyección activa de la fuerza factual sobre contorno factual.

**Teorema 9.2 — No primitividad del empuje factual.** El empuje factual no posee estatuto constitutivo independiente; depende de la fuerza factual y de la frontera factual explícita.

**Demostración.** Por definición, \(\mathfrak{E}^{push}_{SV}\) requiere como entradas \(\mathfrak{F}^{fact}_{SV}\), \(\mathcal{B}_{\partial,SV}\) y normal factual de frontera. Si cualquiera de ellas desaparece, el operador no queda definido. Luego no es primitivo. QED.

**Teorema 9.3 — Absorción conjunta de fuerza y empuje.** Tanto \(\mathfrak{F}^{fact}_{SV}\) como \(\mathfrak{E}^{push}_{SV}\) quedan absorbidos por \(\mathbb{T}^{thermo}_{SV}\).

**Demostración.** La fuerza factual depende del régimen único; el empuje factual depende de la fuerza factual y de la frontera. Luego ambos quedan absorbidos por el régimen soberano. QED.

---

## 10. Entalpía factual

La entalpía factual expresa una magnitud de interior y contorno. No es una traducción de \(U+pV\), sino una compactación factual del dominio.

Se define:

$$
\mathfrak{H}^{fact}_{SV}(\Gamma,n)
=
\mathfrak{C}^{int}_{SV}(\Gamma,n)
+
\mathcal{B}_{\partial,SV}(\Gamma,n).
$$

**Teorema 10.1 — Estatuto de contorno de la entalpía factual.** La entalpía factual no puede reducirse a magnitud de interior puro.

**Demostración.** La definición de \(\mathfrak{H}^{fact}_{SV}\) exige explícitamente contenido interior y borde factual. Si el borde desapareciera, la magnitud perdería su estatuto de contorno. Luego no es interior puro. QED.

**Teorema 10.2 — Absorción de la entalpía factual.** La magnitud \(\mathfrak{H}^{fact}_{SV}\) queda absorbida por el régimen único del dominio.

**Demostración.** \(\mathfrak{H}^{fact}_{SV}\) depende de \(\mathfrak{C}^{int}_{SV}\) y \(\mathcal{B}_{\partial,SV}\), ambas subordinadas al contenido factual total y al borde del régimen. Luego queda absorbida por \(\mathbb{T}^{thermo}_{SV}\). QED.

---

## 11. Propiedades algebraicas absolutas del operador maestro termodinámico

El operador soberano del dominio debe poseer propiedades algebraicas fuertes comparables, mutatis mutandis, a las fijadas para el operador maestro absoluto del electromagnetismo factual. Aquí se fijan las que son necesarias y suficientes para el dominio tratado.

### 11.1. Homogeneidad escalar factual

Para todo escalar factual \(\lambda\in\mathbb{R}\) y toda configuración factual admisible con linealidad factual suficiente en las magnitudes de entrada,

$$
\mathbb{T}^{thermo}_{SV}(\lambda\Gamma,n)=\lambda\,\mathbb{T}^{thermo}_{SV}(\Gamma,n)
$$

en lo concerniente a la primera componente, mientras la segunda conserva el signo de irreversibilidad bajo el mismo reescalado admisible.

### 11.2. Aditividad factual

Si \(\Gamma^{(1)}\) y \(\Gamma^{(2)}\) son trayectorias factuales admisibles compatibles, entonces

$$
\mathbb{T}^{thermo}_{SV}(\Gamma^{(1)}\oplus \Gamma^{(2)},n)
=
\mathbb{T}^{thermo}_{SV}(\Gamma^{(1)},n)
+
\mathbb{T}^{thermo}_{SV}(\Gamma^{(2)},n)
$$

siempre que los operadores de ensamblaje preserven compatibilidad de composición factual.

### 11.3. Covariancia factual bajo transformadas admisibles de trayectoria

Sea \(\mathcal{T}^{SV}_k\) una transformada factual admisible de trayectoria. Entonces

$$
\mathbb{T}^{thermo}_{SV}(\mathcal{T}^{SV}_k\Gamma,n)
=
\mathcal{T}^{SV}_k\big(\mathbb{T}^{thermo}_{SV}(\Gamma,n)\big)
$$

cuando la transformada preserva la clase factual del dominio.

### 11.4. Estabilidad estructural bajo perturbaciones admisibles

Sea \(\Gamma\) un régimen admisible que anula el operador soberano. Para toda perturbación factual admisible \(\delta\Gamma\), la linealización factual del operador satisface

$$
\mathbb{T}^{thermo\,'}_{SV}[\Gamma](\delta\Gamma)=0
$$

como condición necesaria para que el régimen perturbado continúe dentro de la variedad solución.

**Teorema 11.1 — Propiedades algebraicas absolutas.** Sobre el subespacio de regímenes factuales admisibles del dominio termodinámico factual, el operador \(\mathbb{T}^{thermo}_{SV}\) es homogéneo escalar, aditivo factual, covariante bajo transformadas admisibles de trayectoria y estructuralmente estable ante perturbaciones admisibles.

**Demostración.** Cada componente del operador se construye por suma, diferencia y ensamblaje de magnitudes factuales trazables. La linealidad y compatibilidad de esas operaciones basta para transmitir homogeneidad y aditividad. La covariancia se sigue de que el operador no introduce estructura extraña al aparato de trayectoria factual. La estabilidad estructural se sigue de la existencia de linealización factual sobre el subespacio admisible. QED.

---

## 12. Ataques negativos y prueba de irreducibilidad

La unicidad del operador soberano no se deja fijada sólo por construcción positiva. Debe resistir ataques negativos. Se ensayan aquí cinco reducciones hostiles.

### 12.1. Ataque 1 — Reducción del dominio a formulación escalar

Se postula que existe una función escalar \(f\) tal que todo el dominio termodinámico factual queda gobernado por

$$
f(H_{SV})=0.
$$

**Refutación.** Esta reducción elimina frontera factual, residualidad, no clausura legítima, jacobiano estructural, fuerza factual, empuje factual y entalpía factual. Luego no agota el dominio. Falla.

### 12.2. Ataque 2 — Eliminación de la no clausura legítima

Se postula que

$$
\mathcal{N}^{reap}_{SV}=0
$$

globalmente.

**Refutación.** Si \(\mathcal{N}^{reap}_{SV}\) se anula globalmente, el régimen no distingue entre cierre fuerte y clausura espuria. El dominio perdería su capacidad de preservar indeterminación honesta allí donde ésta es constitutiva. Falla.

### 12.3. Ataque 3 — Reintroducción de tiempo soberano

Se sustituye el índice factual de suceso por una variable temporal \(t\).

**Refutación.** El reemplazo rompe la Regla 1 y destruye la trazabilidad factual descendente al suelo preternario. Además, haría depender la irreversibilidad del tiempo y no del suceso. Falla.

### 12.4. Ataque 4 — Reducción de la fuerza factual a gradiente puro

Se postula que

$$
\mathfrak{F}^{fact}_{SV}=-\nabla^{SV}\phi.
$$

**Refutación.** Contradice el Teorema 9.1, porque elimina el término rotacional y la corrección jacobiana local. Falla.

### 12.5. Ataque 5 — Sustitución por integrales clásicas constitutivas

Se postula que el dominio puede fundarse directamente sobre curvilíneas, integrales de superficie e integrales de volumen clásicas.

**Refutación.** La prioridad operatoria del SV exige que el dominio se apoye primero en ensamblajes factuales propios. Las integrales clásicas sólo podrían comparecer, en todo caso, como correspondencias expositivas subordinadas. Falla.

**Teorema 12.1 — Irreducibilidad algebraica del operador soberano.** Toda formulación alternativa del dominio termodinámico factual es o bien reducible a \(\mathbb{T}^{thermo}_{SV}\) o bien inconsistente con el aparato del SV.

**Demostración.** Los cinco ataques anteriores agotan las reducciones hostiles fundamentales: escalarización, supresión de no clausura, temporalización, reducción a gradiente y sustitución por integrales clásicas constitutivas. Todas fallan. Luego el operador es algebraicamente irreducible. QED.

**Corolario 12.2 — Unicidad absoluta del dominio.**

$$
\boxed{\mathbb{T}^{thermo}_{SV}\text{ es la única ecuación soberana del dominio.}}
$$

---

## 13. Recorrido de consistencia visible y exigencias laboratorias

La publicación no cierra con una mera proclamación. Exige laboratorios reproducibles. El conjunto mínimo de bancos visibles debe cubrir:

1. no decrecencia factual de \(H_{SV}\);  
2. validez del balance factual total;  
3. no reducción escalar de \(\mathfrak{T}^{fact}_{SV}\);  
4. no reducción de \(\mathfrak{F}^{fact}_{SV}\) a gradiente puro;  
5. consistencia del empuje factual como proyección de frontera;  
6. trazabilidad factual descendente de las magnitudes altas hasta \((\alpha_i,\beta_i)\).

Cada runner deberá emitir JSON congelado con:

- entradas,  
- valores calculados,  
- tolerancias,  
- dictamen local,  
- y causas de error cuando falle.

El catálogo de errores del conjunto debe distinguir, al menos:

- **TFSV-E001**: decremento entrópico no admisible;  
- **TFSV-E002**: balance factual no cerrado;  
- **TFSV-E003**: reducción escalar indebida de temperatura factual;  
- **TFSV-E004**: reducción indebida de fuerza factual a gradiente puro;  
- **TFSV-E005**: empuje factual sin frontera activa;  
- **TFSV-E006**: trazabilidad factual descendente incompleta.

---

## 14. Conclusión

El dominio termodinámico factual del Sistema Vectorial SV queda fijado, en esta publicación, como régimen algebraico de sucesos construido desde el suelo preternario \((\alpha_i,\beta_i)\), absorbido por la cadena factual de irreversibilidad y compactado por una única ecuación soberana:

$$
\mathbb{T}^{thermo}_{SV}(\Gamma,n)
=
\left(
\Delta_{\Gamma}\mathfrak{C}^{tot}_{SV}(n)
-
\mathcal{W}_{SV}(\Gamma,n)
-
\mathcal{Q}_{SV}(\Gamma,n)
-
\mathcal{N}^{reap}_{SV}(\Gamma,n),
\;-
\Delta_{\Gamma}H_{SV}(\Gamma,n)
\right).
$$

La publicación no deja abiertas, dentro de su núcleo, ni la temperatura factual, ni la fuerza factual, ni el empuje factual, ni la entalpía factual, ni la propia unicidad del régimen. Cada una de esas piezas queda aquí derivada, absorbida y sometida a trazabilidad factual bidireccional.

El cierre fuerte del documento queda expresado por las dos cajas finales:

$$
\boxed{\mathbb{T}^{thermo}_{SV}\text{ es la única ecuación del dominio.}}
$$

$$
\boxed{\text{Toda formulación alternativa es reducible o inconsistente.}}
$$

Lo nuclear nombrado en el presente documento queda aquí cerrado.

---

## 15. Referencias

Lloret Egea, J. A. (2026a). *Nuevas matemáticas del Sistema Vectorial SV y Física factual como conjunto iniciador*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/nuevas-matematicas-del-sistema-vectorial-sv-y-fisica-factual-como-conjunto-iniciador

Lloret Egea, J. A. (2026b). *Conjunto matemático unificado del cambio factual, ciclos, medición factual y trayectorias poligonales de activación en el Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/conjunto-matematico-unificado-del-cambio-factual-ciclos-medicion-factual-y-trayectorias-poligonales-de-activacion-en-el-sistema-vectorial-sv

Lloret Egea, J. A. (2026c). *Primitivos metrológicos del Sistema Vectorial SV: instanciaciones contingentes de las constantes fundacionales del Sistema Internacional, justificación algebraica y tabla de equivalencias factuales*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/primitivos-metrologicos-del-sistema-vectorial-sv-instanciaciones-contingentes-de-las-constantes-fundacionales-del-sistema-internacional-justificacion-algebraica-y-tabla-de-equivalencias-factuales

Lloret Egea, J. A. (2026d). *Fourier factual y ecuación de onda electromagnética en el Sistema Vectorial SV: desarrollo cíclico, transformada modal y propagación sobre ciclo y trayectoria poligonal*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/fourier-factual-y-ecuacion-de-onda-electromagnetica-en-el-sistema-vectorial-sv-desarrollo-ciclico-transformada-modal-y-propagacion-sobre-ciclo-y-trayectoria-poligonal

Lloret Egea, J. A. (2026e). *Medición, reconstrucción e incertidumbre estructural en la física contemporánea sin probabilidad ni tiempo absoluto: un marco analítico basado en sucesos y trayectorias con laboratorios ejecutables*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/medicion-reconstruccion-e-incertidumbre-estructural-en-la-fisica-contemporanea-sin-probabilidad-ni-tiempo-absoluto-un-marco-analitico-basado-en-sucesos-y-trayectorias-con-laboratorios-ejecutables

Lloret Egea, J. A. (2026f). *Correlación, restricción de clausura y no clausura posicional en dominios cuánticos contemporáneos: una relectura doctrinal desde el Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/correlacion-restriccion-de-clausura-y-no-clausura-posicional-en-dominios-cuanticos-contemporaneos-una-relectura-doctrinal-desde-el-sistema-vectorial-sv

Lloret Egea, J. A. (2026g). *Absorción de E₀ = m₀c² como sector basal de reposo en el Sistema Vectorial SV: estructura factual ampliada, compatibilidad modal, balance con residual y criterio conservador de clausura*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/absorcion-de-e--mc-como-sector-basal-de-reposo-en-el-sistema-vectorial-sv-estructura-factual-ampliada-compatibilidad-modal-balance-con-residual-y-criterio-conservador-de-clausura

Lloret Egea, J. A. (2026h). *Del contenido físico factual del suceso a las clases factuales emergentes: programa de transmutación factual en el Sistema SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/del-contenido-fisico-factual-del-suceso-a-las-clases-factuales-emergentes-programa-de-transmutacion-factual-en-el-sistema-sv

Lloret Egea, J. A. (2026i). *Del contenido físico factual del suceso a la entidad absoluta del campo en el Sistema Vectorial SV: absorción basal exacta, unificación fuerte de gravitación, electricidad y magnetismo, y apertura a clases factuales emergentes*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/del-contenido-fisico-factual-del-suceso-a-la-entidad-absoluta-del-campo-en-el-sistema-vectorial-sv-absorcion-basal-exacta-unificacion-fuerte-de-gravitacion-electricidad-y-magnetismo-y-apertura-a-clases-factuales-emergentes

Lloret Egea, J. A. (2026j). *Del origen preternario del Sistema Vectorial SV a la entidad absoluta del campo: derivación nativa de α_i y β_i, proyección ternaria inducida, absorción basal exacta, unificación fuerte de gravitación, electricidad y magnetismo, y apertura a clases factuales emergentes*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://www.itvia.online/pub/ekd8x4l9

Lloret Egea, J. A. (2026k). *Fundamentos operatorios absolutos del electromagnetismo factual en el Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411. https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/fundamentos-operatorios-absolutos-del-electromagnetismo-factual-en-el-sistema-vectorial-sv.md

Lloret Egea, J. A. (2026l). *Teoría general factual de la luz en el Sistema Vectorial SV*. IA eñ™ — La Biblia de la IA™. Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español. ISSN 2695-6411.
