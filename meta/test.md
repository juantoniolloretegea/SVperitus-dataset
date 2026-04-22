### 14.19.5. Núcleo compositivo Comp^poly_SV

**Definición 14.19.4.** Sea $\mathcal{O}_{SV}$ la colección de operadores absolutos del anexo enumerados en §14.19.1. El **núcleo compositivo polimodal factual** $\mathrm{Comp}^{\mathrm{poly}}_{SV}$ es la operación

$$
\mathrm{Comp}^{\mathrm{poly}}_{SV} : \mathcal{O}_{SV} \times \mathcal{O}_{SV} \times \mathcal{M}^{\mathrm{adm}}_{SV} \longrightarrow \mathcal{O}_{SV}
$$

que, a cada par ordenado $(L_1, L_2)$ de operadores absolutos y cada configuración admisible $(q, \Omega)$, asigna el operador compuesto $\mathrm{Comp}^{\mathrm{poly}}_{SV}(L_1, L_2; q, \Omega) \in \mathcal{O}_{SV}$ definido por las cuatro condiciones siguientes:

- **Dominio preciso.** El dominio de la composición es la intersección de los dominios admisibles de $L_1$ y $L_2$ restringida a $(q, \Omega)$.

- **Regla de composición.** Si las compuertas canónicas involucradas evalúan a $1$ sobre $(q, \Omega)$, la composición se reduce a la composición funcional estándar $L_1 \circ L_2$. Si alguna compuerta canónica relevante evalúa a $0$, la composición se modula por el operador de reconfiguración $\mathcal{R}^f_{SV}$ aplicado en el punto de ruptura.

- **Asociatividad condicional.** La composición $\mathrm{Comp}^{\mathrm{poly}}_{SV}$ es asociativa sobre el subdominio donde $\mathfrak{C}_{SV}(q, \Omega) = 1$. Fuera de ese subdominio, la asociatividad queda controlada por la fórmula de reordenación de la jerarquía reconfigurativa del apartado §14.19.7.

- **Equivalencia de salida.** Dos composiciones $\mathrm{Comp}^{\mathrm{poly}}_{SV}(L_1, L_2; q, \Omega)$ y $\mathrm{Comp}^{\mathrm{poly}}_{SV}(L_1', L_2'; q, \Omega)$ son equivalentes si y solo si producen la misma salida funcional sobre cada elemento admisible de la intersección de sus dominios, módulo aplicación de $\mathcal{R}^f_{SV}$ en las interfaces factuales activas.

La relación de $\mathrm{Comp}^{\mathrm{poly}}_{SV}$ con la firma general $\mathrm{Comp}$ del corpus, entendida como composición genérica de operadores sobre $\Xi_{SV}$, es la siguiente: $\mathrm{Comp}^{\mathrm{poly}}_{SV}$ es la restricción especializada de $\mathrm{Comp}$ al subdominio admisible $\mathcal{M}^{\mathrm{adm}}_{SV}$ bajo control de las compuertas canónicas.

### 14.19.6. Definición operativa de 𝔘_SV

**Definición 14.19.5.** El **operador de conformación polimodal factual** $\mathfrak{U}_{SV}$ se define sobre configuraciones admisibles $(q,\Omega) \in \mathcal{M}^{\mathrm{adm}}_{SV}$ por las dos reglas siguientes.

Si la compuerta global absoluta satisface $\mathfrak{C}_{SV}(q,\Omega)=1$, entonces

$$
\mathfrak{U}_{SV}[q,\Omega] \;:=\; \mathrm{Comp}^{\mathrm{poly}}_{SV}\bigl(\mathbb{M}_{SV}, \mathbb{K}_{SV}; q,\Omega\bigr).
$$

Si la compuerta global absoluta satisface $\mathfrak{C}_{SV}(q,\Omega)=0$, entonces

$$
\mathfrak{U}_{SV}[q,\Omega] \;:=\; U.
$$

donde $\mathbb{M}_{SV}$ es la componente absoluta de las ecuaciones de primer orden y $\mathbb{K}_{SV}$ la componente de clausura.

### 14.19.7. Jerarquía reconfigurativa 𝓡^(f,(k))_SV

**Definición 14.19.6.** La **jerarquía absoluta de operadores de reconfiguración factual** se define inductivamente como

$$
\mathcal{R}^{f,(1)}_{SV} := \mathcal{R}^{f}_{SV}, \qquad
\mathcal{R}^{f,(k+1)}_{SV} := \mathcal{R}^{f,(k)}_{SV} \circ \mathcal{R}^{f}_{SV}, \qquad k \ge 1.
$$

**Teorema 14.19.7.** La jerarquía $\mathcal{R}^{f,(k)}_{SV}$ es estable bajo composición absoluta: para todo par $k_1, k_2 \ge 1$,

$$
\mathcal{R}^{f,(k_1)}_{SV} \circ \mathcal{R}^{f,(k_2)}_{SV}
\;=\;
\mathcal{R}^{f,(k_1+k_2)}_{SV}.
$$

*Demostración.* Por la Definición 14.19.6 aplicada inductivamente sobre el orden compositivo. Q.E.D.

### 14.19.8. Teorema de existencia tipada

**Teorema 14.19.8 (existencia tipada de $\mathfrak{U}_{SV}$).** Para toda configuración $(q,\Omega) \in \mathcal{M}^{\mathrm{adm}}_{SV}$, la salida $\mathfrak{U}_{SV}[q,\Omega]$ está bien definida, es única, y pertenece a la unión tipada formada por $\mathcal{O}_{SV}$ y $\{U\}$.

*Demostración.* Por la Definición 14.19.3, la compuerta global absoluta satisface $\mathfrak{C}_{SV}(q,\Omega) \in \{0,1\}$.

Si $\mathfrak{C}_{SV}(q,\Omega)=1$, la salida reduce a

$$
\mathfrak{U}_{SV}[q,\Omega] \;=\; \mathrm{Comp}^{\mathrm{poly}}_{SV}\bigl(\mathbb{M}_{SV}, \mathbb{K}_{SV}; q,\Omega\bigr),
$$

y, por la Definición 14.19.4, esa salida pertenece a $\mathcal{O}_{SV}$.

Si $\mathfrak{C}_{SV}(q,\Omega)=0$, la salida reduce a

$$
\mathfrak{U}_{SV}[q,\Omega] \;=\; U,
$$

y por definición pertenece a $\{U\}$.

La unicidad resulta de la unicidad booleana del valor de $\mathfrak{C}_{SV}(q,\Omega)$ y de la unicidad de la composición en el caso activo. Q.E.D.
