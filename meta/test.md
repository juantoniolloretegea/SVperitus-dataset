### 14.19.5. Núcleo compositivo Comp^poly_SV

**Definición 14.19.4.** Sea `O_SV` la colección de operadores absolutos del anexo enumerados en §14.19.1. El núcleo compositivo polimodal factual `Comp^poly_SV` es la operación

`Comp^poly_SV : O_SV × O_SV × M^adm_SV -> O_SV`

que, a cada par ordenado `(L1, L2)` de operadores absolutos y cada configuración admisible `(q, Ω)`, asigna el operador compuesto `Comp^poly_SV(L1, L2; q, Ω)` perteneciente a `O_SV`, definido por las cuatro condiciones siguientes:

- **Dominio preciso.** El dominio de la composición es la intersección de los dominios admisibles de `L1` y `L2`, restringida a `(q, Ω)`.

- **Regla de composición.** Si las compuertas canónicas involucradas evalúan a `1` sobre `(q, Ω)`, la composición se reduce a la composición funcional estándar `L1 ∘ L2`. Si alguna compuerta canónica relevante evalúa a `0`, la composición se modula por el operador de reconfiguración factual `R^f_SV` aplicado en el punto de ruptura.

- **Asociatividad condicional.** La composición `Comp^poly_SV` es asociativa sobre el subdominio donde `C_SV(q, Ω) = 1`. Fuera de ese subdominio, la asociatividad queda controlada por la fórmula de reordenación de la jerarquía reconfigurativa del apartado §14.19.7.

- **Equivalencia de salida.** Dos composiciones `Comp^poly_SV(L1, L2; q, Ω)` y `Comp^poly_SV(L1', L2'; q, Ω)` son equivalentes si y solo si producen la misma salida funcional sobre cada elemento admisible de la intersección de sus dominios, módulo aplicación de `R^f_SV` en las interfaces factuales activas.

La relación de `Comp^poly_SV` con la firma general `Comp` del corpus, entendida como composición genérica de operadores sobre `Ξ_SV`, es la siguiente: `Comp^poly_SV` es la restricción especializada de `Comp` al subdominio admisible `M^adm_SV` bajo control de las compuertas canónicas.

### 14.19.6. Definición operativa de U_SV

**Definición 14.19.5.** El operador de conformación polimodal factual `U_SV` se define como la aplicación

`U_SV : M^adm_SV -> O_SV ∪ {U}`

y queda determinado por las dos reglas siguientes:

- Si `C_SV(q, Ω) = 1`, entonces  
  `U_SV[q, Ω] := Comp^poly_SV(M_SV, K_SV; q, Ω)`.

- Si `C_SV(q, Ω) = 0`, entonces  
  `U_SV[q, Ω] := U`.

donde `M_SV` es la componente absoluta de las ecuaciones de primer orden y `K_SV` la componente de clausura.

### 14.19.7. Jerarquía reconfigurativa R^(f,(k))_SV

**Definición 14.19.6.** La jerarquía absoluta de operadores de reconfiguración factual se define inductivamente como sigue:

- `R^(f,(1))_SV := R^f_SV`.
- `R^(f,(k+1))_SV := R^(f,(k))_SV ∘ R^f_SV`, para todo `k ≥ 1`.

**Teorema 14.19.7.** La jerarquía `R^(f,(k))_SV` es estable bajo composición absoluta: para todo par `k1, k2 ≥ 1`,

`R^(f,(k1))_SV ∘ R^(f,(k2))_SV = R^(f,(k1+k2))_SV`.

*Demostración.* La igualdad se obtiene por aplicación inductiva directa de la Definición 14.19.6 sobre el orden compositivo. Q.E.D.

### 14.19.8. Teorema de existencia tipada

**Teorema 14.19.8 (existencia tipada de U_SV).** Para toda configuración `(q, Ω)` perteneciente a `M^adm_SV`, la salida `U_SV[q, Ω]` está bien definida, es única y pertenece a la unión tipada `O_SV ∪ {U}`.

*Demostración.* Por definición, la compuerta global absoluta `C_SV(q, Ω)` sólo puede tomar los valores `0` o `1`. Si `C_SV(q, Ω) = 1`, la salida es `Comp^poly_SV(M_SV, K_SV; q, Ω)` y pertenece a `O_SV`. Si `C_SV(q, Ω) = 0`, la salida es `U` y pertenece a `{U}`. La unicidad se sigue de la unicidad del valor de `C_SV(q, Ω)` y de la determinación unívoca de cada una de las dos ramas. Q.E.D.
