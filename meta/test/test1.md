#### Caso resuelto: primer principio en sistema cerrado, expansión isobárica de gas ideal

Este caso muestra cómo la lectura termodinámica raigal `Ω_th(Γ,n)` recibe un problema clásico de primer principio —típico para evaluar eficiencia en procesos industriales— y lo devuelve a unidades públicas sin identificar el raigal con calor, trabajo, energía, temperatura ni entropía. El raigal no aporta física nueva: aporta disciplina de retorno. La magnitud entra como horizonte raigal `H_Ξ(o,D_th)`, se proyecta por su transductor `𝔛_Ξ^X`, se conserva en unidad nativa `UR_Ξ^X(D_th)`, retorna en unidad SI y deja residual `R_Ξ^X` y traza visibles.

##### Enunciado

Un cilindro con émbolo contiene `0.2 kg` de aire, tratado como gas ideal con `R = 0.287 kJ/(kg·K)` y `c_v = 0.718 kJ/(kg·K)`. El aire se calienta a presión constante `P = 200 kPa` desde `T₁ = 300 K` hasta `T₂ = 500 K`. Determínese el trabajo de frontera `W` y el calor transferido `Q`.

El proceso queda **declarado** como isobárico, cuasiestático y de gas ideal sin fricción. Esta declaración es la que habilita el cálculo: sin proceso térmico declarado, la salida correcta sería `U`.

##### Recepción del dominio y construcción de `Ω_th`

El dominio térmico `D_th` queda declarado. La lectura especializada se construye con sus cinco componentes:

`Ω_th(Γ,n) = (𝒜_th, 𝓗_th, 𝒥_Γ, ℛ_Γ, ℬ_∂)`

y las proyecciones que este caso activa son `π_W`, `π_Q`, `π_U` (no clausura), `π_Θ` (régimen térmico) y, para el retorno térmico, `π_S` vía entropía estructural `𝓗_th`. Las entradas de banco se reciben tipadas:

| Entrada | Transductor | Unidad nativa | Retorno externo | Estado |
|---|---|---|---|---|
| Masa | `𝔛_Ξ^M` | `UFM` | `0.2 kg` | cerrada |
| Presión de frontera | `𝔛_Ξ^Π` | `UFM·UFE⁻¹·UE_MFC⁻²` | `200 kPa` | cerrada (frontera externa declarada) |
| Régimen térmico inicial | `𝔛_Ξ^Θ` | `UFT` | `300 K` | régimen, no causa |
| Régimen térmico final | `𝔛_Ξ^Θ` | `UFT` | `500 K` | régimen, no causa |
| Constante de gas | banco material | `UFE²·UE_MFC⁻²·UFT⁻¹` | `0.287 kJ/(kg·K)` | constante ancla con residual de banco |
| Calor específico a volumen | `𝔛_Ξ^c` | `UFE²·UE_MFC⁻²·UFT⁻¹` | `0.718 kJ/(kg·K)` | constante ancla con residual de banco |

El calor específico a presión constante no es un dato externo arrastrado, sino una composición de primitivos ya declarados:

`c_p = c_v + R = 0.718 + 0.287 = 1.005 kJ/(kg·K)`

##### 1. Trabajo de frontera — proyección `π_W` por `𝔛_Ξ^W`

El trabajo entra como horizonte raigal y retorna por su canal presión-volumen, nunca como "energía total disponible". En proceso isobárico:

`W = P(V₂ − V₁) = m·R·(T₂ − T₁)`

`W = 0.2 × 0.287 × (500 − 300) = 11.48 kJ`

Contraste por volúmenes de banco (`V = m·R·T/P`): `V₁ = 0.0861 m³`, `V₂ = 0.1435 m³`, `ΔV = 0.0574 m³`; `P·ΔV = 200 kPa × 0.0574 m³ = 11.48 kJ`. Coincidencia que cierra el canal mecánico.

Retorno raigal: `V_Ξ^W = W_Ξ·UR_Ξ^W(D_th) → 11.48 kJ`. El sistema realiza trabajo positivo sobre el entorno al expandirse. Residual de canal mecánico `R_Ξ^W`: solo el de banco de las constantes; no hay pérdida de canal en el régimen declarado.

##### 2. Calor transferido — proyección `π_Q` por `𝔛_Ξ^Q`

El calor exige tránsito térmico, frontera y proceso, ya declarados. En un proceso isobárico de sistema cerrado, el calor intercambiado iguala la variación de entalpía `Λ_th`, leída como acumulación más frontera (`Λ_th = 𝒜_th + ℬ_∂`):

`Q = m·c_p·(T₂ − T₁)`

`Q = 0.2 × 1.005 × (500 − 300) = 40.2 kJ`

Retorno raigal: `V_Ξ^Q = Q_Ξ·UR_Ξ^Q(D_th) → 40.2 kJ`. Se requieren `40.2 kJ` en forma de calor. La temperatura no se ha usado como calor: ha entrado como régimen `Θ_th` y el calor procede del tránsito térmico declarado, no de la escala por sí sola.

##### 3. Balance de intercambio y acumulación interna — `𝒜_th`, `𝒰_th`

El balance térmico raigal separa explícitamente las tres contribuciones:

`𝔇_Γ𝒜_th(Γ,n) = 𝒲_th + 𝒬_th + 𝒰_th`

con la lectura de signos del primer principio del sistema cerrado (`𝒬_th` entra, `𝒲_th` sale). La acumulación interna se proyecta por `𝔛_Ξ^A`:

`ΔU = m·c_v·(T₂ − T₁) = 0.2 × 0.718 × 200 = 28.72 kJ`

de modo que `𝒬_th = 𝒜_th + 𝒲_th`:

`40.2 = 28.72 + 11.48 + 𝒰_th` → `𝒰_th = 0`

La no clausura `𝒰_th` se anula **por declaración de idealización** (gas ideal, cuasiestático, sin fricción), no por borrado. El criterio del dominio prohíbe ocultar `𝒰_th` como error de cálculo: aquí se conserva en cero porque el régimen lo justifica, y queda anotada como hipótesis explícita, no como cierre forzado.

##### 4. Retorno térmico y entropía — proyección `π_S` por `𝔛_Ξ^S`

El apartado pide retorno térmico además de balance. La irreversibilidad estructural se controla con `𝔇_Γ𝓗_th ≥ 0`. Para el tramo isobárico:

`ΔS = m·c_p·ln(T₂/T₁) = 0.2 × 1.005 × ln(500/300) = 0.1027 kJ/K ≈ 102.7 J/K`

Retorno raigal: `V_Ξ^S = S_Ξ·UR_Ξ^S(D_th) → 0.1027 kJ·K⁻¹`. Como `𝔇_Γ𝓗_th > 0`, el régimen térmico es legible y la lectura no fuerza temperatura por división ni reinterpreta la trayectoria como reversible por redacción. La entropía no se usa aquí como desorden verbal ni como ignorancia: es retorno de régimen con unidad verificable.

##### Matriz especializada de retorno (instanciada para este caso)

| Proyección | Transductor | Unidad nativa | Unidad SI | Valor retornado | Residual `R_Ξ^X` | Dictamen |
|---|---|---|---|---|---|---|
| Trabajo | `𝔛_Ξ^W` | `UFM·UFE²·UE_MFC⁻²` | J | `11.48 kJ` | solo banco de `R` | `0` condicionado |
| Calor | `𝔛_Ξ^Q` | `UFM·UFE²·UE_MFC⁻²` con `UFT` | J | `40.2 kJ` | solo banco de `c_p` | `0` condicionado |
| Acumulación interna | `𝔛_Ξ^A` | `UFM·UFE²·UE_MFC⁻²` | J | `28.72 kJ` | solo banco de `c_v` | `0` condicionado |
| No clausura térmica | `𝔛_Ξ^U` | `UFM·UFE²·UE_MFC⁻²` | J | `0 kJ` (idealización declarada) | hipótesis explícita | `0` condicionado |
| Entropía | `𝔛_Ξ^S` | `UFM·UFE²·UE_MFC⁻²·UFT⁻¹` | J·K⁻¹ | `0.1027 kJ/K` | régimen cerrado | `0` condicionado |
| Régimen térmico | `𝔛_Ξ^Θ` | `UFT` | K | `300 → 500 K` | — | `0` condicionado |
| Volumen de proceso | `𝔛_Ξ^V` | `UFE³` | m³ | `0.0861 → 0.1435 m³` | fase cerrada | `0` condicionado |

##### Residuales y conservación de `U`

Los únicos residuales materiales son metrológicos de banco: el redondeo de las constantes ancla `R = 0.287` y `c_v = 0.718 kJ/(kg·K)`, que se conserva como **normalización pendiente** de la notación del dominio y no se maquilla como cierre exacto. La no clausura `𝒰_th = 0` es válida solo bajo el régimen ideal declarado; cualquier fricción, disipación o irreversibilidad real reabriría `𝒰_th` y debería retornarse, no absorberse en `W` o `Q`.

##### Dictamen de admisibilidad

`Termo_Ξ admisible ⇔ D_th declarado ∧ Ω_th construida ∧ π_W,π_Q,π_U,π_Θ,π_S tipadas ∧ unidad nativa ∧ unidad SI ∧ proceso isobárico declarado ∧ frontera ∧ residual ∧ retorno ∧ traza ∧ conservación de U ∧ no identificación del raigal con calor, trabajo, energía, temperatura o entropía`

Todas las condiciones cierran sin contradicción material: **Dictamen = `0`**. El raigal ha sostenido un tránsito termodinámico completo —`W = 11.48 kJ`, `Q = 40.2 kJ`, `ΔU = 28.72 kJ`, `ΔS ≈ 0.1027 kJ/K`— devolviendo cada magnitud a unidad pública mientras conserva la continuidad interna por `UR_Ξ^X(D_th)` y el residual correspondiente, sin ser él mismo ninguna de esas magnitudes.
