### 14.19.4. Compuerta global

**Definición 14.19.3.** La compuerta global absoluta $`\mathfrak{C}_{SV}`$: $`\mathcal{M}^{\mathrm{adm}}_{SV} \to \{0,1\}`$ se define como conjunción absoluta de las cuatro compuertas canónicas:

$$
\mathfrak{C}_{SV}(q,\Omega)
\;:=\;
c_{\mathrm{sep}}(q,\Omega)\cdot c_{\partial\Omega}(q,\Omega)\cdot c_{\Lambda}(q,\Omega)\cdot c_{R}(q,\Omega).
$$

El producto en $`\{0,1\}`$ coincide con la conjunción absoluta: $`\mathfrak{C}_{SV}=1`$ si y solo si las cuatro compuertas canónicas evalúan simultáneamente a $`1`$.
### 14.19.5. Núcleo compositivo Comp^poly_SV

**Definición 14.19.4.** Sea $`\mathcal{O}_{SV}`$ la colección de operadores absolutos del anexo enumerados en §14.19.1. El núcleo compositivo polimodal factual $`\mathrm{Comp}^{\mathrm{poly}}_{SV}`$ es la operación

$$
\mathrm{Comp}^{\mathrm{poly}}_{SV} :
\mathcal{O}_{SV} \times \mathcal{O}_{SV} \times \mathcal{M}^{\mathrm{adm}}_{SV}
\longrightarrow
\mathcal{O}_{SV}.
$$

que, a cada par ordenado $`(L_1, L_2)`$ de operadores absolutos y cada configuración admisible $`(q, \Omega)`$, asigna el operador compuesto $`\mathrm{Comp}^{\mathrm{poly}}_{SV}(L_1, L_2; q, \Omega) \in \mathcal{O}_{SV}`$ definido por las cuatro condiciones siguientes:

- **Dominio preciso.** El dominio de la composición es la intersección de los dominios admisibles de $`L_1`$ y $`L_2`$ restringida a $`(q, \Omega)`$.

- **Regla de composición.** Si las compuertas canónicas involucradas evalúan a $`1`$ sobre $`(q, \Omega)`$, la composición se reduce a la composición funcional estándar $`L_1 \circ L_2`$. Si alguna compuerta canónica relevante evalúa a $`0`$ sobre $`(q, \Omega)`$, la composición se modula por el operador de reconfiguración $`\mathcal{R}^{f}_{SV}`$ aplicado en el punto de ruptura.

- **Asociatividad condicional.** La composición $`\mathrm{Comp}^{\mathrm{poly}}_{SV}`$ es asociativa sobre el subdominio donde $`\mathfrak{C}_{SV}(q, \Omega)=1`$. Fuera de ese subdominio, la asociatividad queda controlada por la fórmula de reordenación de la jerarquía reconfigurativa del apartado §14.19.7.

- **Equivalencia de salida.** Dos composiciones $`\mathrm{Comp}^{\mathrm{poly}}_{SV}(L_1, L_2; q, \Omega)`$ y $`\mathrm{Comp}^{\mathrm{poly}}_{SV}(L'_1, L'_2; q, \Omega)`$ son equivalentes si y solo si producen la misma salida funcional sobre cada elemento admisible de la intersección de sus dominios, módulo aplicación de $`\mathcal{R}^{f}_{SV}`$ en las interfaces factuales activas.

La relación de $`\mathrm{Comp}^{\mathrm{poly}}_{SV}`$ con la firma general $`\mathrm{Comp}`$ del corpus, entendida como composición genérica de operadores sobre $`\Xi_{SV}`$, es la siguiente: $`\mathrm{Comp}^{\mathrm{poly}}_{SV}`$ es la restricción especializada de $`\mathrm{Comp}`$ al subdominio admisible $`\mathcal{M}^{\mathrm{adm}}_{SV}`$ bajo control de las compuertas canónicas.

### 14.19.6. Definición operativa de U_SV

**Definición 14.19.5.** El operador de conformación polimodal factual $`\mathfrak{U}_{SV}`$ se define como la aplicación

$$
\mathfrak{U}_{SV} :
\mathcal{M}^{\mathrm{adm}}_{SV}
\longrightarrow
\mathcal{O}_{SV} \cup \{U\}.
$$

y queda determinado por las dos reglas siguientes:

- Si $`\mathfrak{C}_{SV}(q,\Omega)=1`$, entonces

$$
\mathfrak{U}_{SV}[q,\Omega] \;:=\;
\mathrm{Comp}^{\mathrm{poly}}_{SV}\bigl(\mathbb{M}_{SV},\mathbb{K}_{SV};\,q,\Omega\bigr).
$$

- Si $`\mathfrak{C}_{SV}(q,\Omega)=0`$, entonces

$$
\mathfrak{U}_{SV}[q,\Omega] \;:=\; U.
$$

donde $`\mathbb{M}_{SV}`$ es la componente absoluta de las ecuaciones de primer orden y $`\mathbb{K}_{SV}`$ la componente de clausura.

### 14.19.7. Jerarquía reconfigurativa $\mathcal{R}^{f,(k)}_{SV}$

**Definición 14.19.6.** La jerarquía absoluta de operadores de reconfiguración factual se define inductivamente como sigue:

- $`\mathcal{R}^{f,(1)}_{SV} := \mathcal{R}^{f}_{SV}`$.
- $`\mathcal{R}^{f,(k+1)}_{SV} := \mathcal{R}^{f,(k)}_{SV} \circ \mathcal{R}^{f}_{SV}`$, para todo $`k \ge 1`$.

**Teorema 14.19.7.** La jerarquía $`\mathcal{R}^{f,(k)}_{SV}`$ es estable bajo composición absoluta: para todo par $`k_1, k_2 \ge 1`$, se cumple $`\mathcal{R}^{f,(k_1)}_{SV} \circ \mathcal{R}^{f,(k_2)}_{SV} = \mathcal{R}^{f,(k_1+k_2)}_{SV}`$.

*Demostración.* La igualdad se obtiene por aplicación inductiva directa de la Definición 14.19.6 sobre el orden compositivo. Q.E.D.

### 14.19.8. Teorema de existencia tipada

**Teorema 14.19.8 (existencia tipada de $`\mathfrak{U}_{SV}`$).** Para toda configuración $`(q,\Omega)`$ perteneciente a $`\mathcal{M}^{\mathrm{adm}}_{SV}`$, la salida $`\mathfrak{U}_{SV}[q,\Omega]`$ está bien definida, es única y pertenece a la unión tipada $`\mathcal{O}_{SV} \cup \{U\}`$.

*Demostración.* Por definición, la compuerta global absoluta $`\mathfrak{C}_{SV}(q,\Omega)`$ sólo puede tomar los valores $`0`$ o $`1`$. Si $`\mathfrak{C}_{SV}(q,\Omega)=1`$, la salida es

$$
\mathfrak{U}_{SV}[q,\Omega] \;:=\;
\mathrm{Comp}^{\mathrm{poly}}_{SV}\bigl(\mathbb{M}_{SV},\mathbb{K}_{SV};\,q,\Omega\bigr),
$$

y pertenece a $`\mathcal{O}_{SV}`$. Si $`\mathfrak{C}_{SV}(q,\Omega)=0`$, la salida es

$$
\mathfrak{U}_{SV}[q,\Omega] \;:=\; U,
$$

y pertenece a $`\{U\}`$. La unicidad se sigue de la unicidad del valor de $`\mathfrak{C}_{SV}(q,\Omega)`$ y de la determinación unívoca de cada una de las dos ramas. Q.E.D.
