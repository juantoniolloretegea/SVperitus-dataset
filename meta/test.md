### 14.19.5. Núcleo compositivo Comp^poly_SV

**Definición 14.19.4.** Sea $\mathcal{O}_{SV}$ la colección de operadores absolutos del anexo enumerados en §14.19.1. El núcleo compositivo polimodal factual Comp^poly_SV es la operación

$$
\mathrm{Comp}^{\mathrm{poly}}_{SV} :
\mathcal{O}_{SV} \times \mathcal{O}_{SV} \times \mathcal{M}^{\mathrm{adm}}_{SV}
\longrightarrow
\mathcal{O}_{SV}.
$$

que, a cada par ordenado $(L_1, L_2)$ de operadores absolutos y cada configuración admisible $(q, \Omega)$, asigna el operador compuesto $\mathrm{Comp}^{\mathrm{poly}}_{SV}(L_1, L_2; q, \Omega) \in \mathcal{O}_{SV}$ definido por las cuatro condiciones siguientes:

- **Dominio preciso.** El dominio de la composición es la intersección de los dominios admisibles de $L_1$ y $L_2$ restringida a $(q, \Omega)$.

- **Regla de composición.** Si las compuertas canónicas involucradas evalúan a $1$ sobre $(q, \Omega)$, la composición se reduce a la composición funcional estándar $L_1 \circ L_2$. Si alguna compuerta canónica relevante evalúa a $0$ sobre $(q, \Omega)$, la composición se modula por el operador de reconfiguración $\mathcal{R}^{f}_{SV}$ aplicado en el punto de ruptura.

- **Asociatividad condicional.** La composición Comp^poly_SV es asociativa sobre el subdominio donde $\mathfrak{C}_{SV}(q, \Omega) = 1$. Fuera de ese subdominio, la asociatividad queda controlada por la fórmula de reordenación de la jerarquía reconfigurativa del apartado §14.19.7.

- **Equivalencia de salida.** Dos composiciones $\mathrm{Comp}^{\mathrm{poly}}_{SV}(L_1, L_2; q, \Omega)$ y $\mathrm{Comp}^{\mathrm{poly}}_{SV}(L'_1, L'_2; q, \Omega)$ son equivalentes si y solo si producen la misma salida funcional sobre cada elemento admisible de la intersección de sus dominios, módulo aplicación de $\mathcal{R}^{f}_{SV}$ en las interfaces factuales activas.

La relación de Comp^poly_SV con la firma general Comp del corpus, entendida como composición genérica de operadores sobre $\Xi_{SV}$, es la siguiente: Comp^poly_SV es la restricción especializada de Comp al subdominio admisible $\mathcal{M}^{\mathrm{adm}}_{SV}$ bajo control de las compuertas canónicas.

### 14.19.6. Definición operativa de U_SV

**Definición 14.19.5.** El operador de conformación polimodal factual $\mathfrak{U}_{SV}$ se define como la aplicación

$$
\mathfrak{U}_{SV} :
\mathcal{M}^{\mathrm{adm}}_{SV}
\longrightarrow
\mathcal{O}_{SV} \cup \{U\}.
$$

Si la compuerta global absoluta satisface $\mathfrak{C}_{SV}(q, \Omega)=1$, entonces

$$
\mathfrak{U}_{SV}[q, \Omega]
:=
\mathrm{Comp}^{\mathrm{poly}}_{SV}\bigl(\mathbb{M}_{SV}, \mathbb{K}_{SV}; q, \Omega\bigr).
$$

Si la compuerta global absoluta satisface $\mathfrak{C}_{SV}(q, \Omega)=0$, entonces

$$
\mathfrak{U}_{SV}[q, \Omega] := U.
$$

donde $\mathbb{M}_{SV}$ es la componente absoluta de las ecuaciones de primer orden y $\mathbb{K}_{SV}$ la componente de clausura.
