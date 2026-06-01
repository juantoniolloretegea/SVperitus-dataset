## II.1. Termodinámica: balance, calor, trabajo, entropía y retorno térmico

La termodinámica inaugura la especialización de dominios porque reúne las magnitudes centrales del intercambio térmico —calor y trabajo— y las que gobiernan su lectura: temperatura, entalpía, presión, capacidad térmica y la no clausura del balance (Lloret Egea, 2026i, 2026j). Prueban, a nuestro juicio, con particular claridad la utilidad de la matriz raigal. El raigal no se convierte en energía térmica ni en entropía; muestra cómo una raíz metrológica común recibe y devuelve magnitudes térmicas conservando unidad nativa, unidad SI, proceso, frontera y residual.

> **Caso de aplicación.** Un cilindro con émbolo contiene `0.2 kg` de aire, tratado como gas ideal con `R = 0.287 kJ/(kg·K)` y `c_v = 0.718 kJ/(kg·K)`. Se calienta a presión constante `P = 200 kPa` desde `T₁ = 300 K` hasta `T₂ = 500 K`. La lectura termodinámica ordinaria resuelve el primer principio en dos pasos. El trabajo de frontera, en proceso isobárico, es `W = m·R·(T₂ − T₁) = 0.2 × 0.287 × 200 = 11.48 kJ`. El calor, igual a la variación de entalpía, emplea `c_p = c_v + R = 1.005 kJ/(kg·K)`, de donde `Q = m·c_p·(T₂ − T₁) = 0.2 × 1.005 × 200 = 40.2 kJ`. Sobre este resultado conocido se construye la lectura raigal. El proceso se declara isobárico, cuasiestático y de gas ideal sin fricción; sin proceso térmico declarado, la salida correcta sería `U`.

**Construcción de la lectura especializada.** La forma del dominio es `Ω_th(Γ,n) = (𝒜_th, 𝓗_th, 𝒥_Γ, ℛ_Γ, ℬ_∂)`: acumulación de contenido, entropía estructural, sensibilidad, residual y frontera. Recibe las entradas tipadas —masa por `𝔛_Ξ^M`, presión de frontera por `𝔛_Ξ^Π` y régimen térmico por `𝔛_Ξ^Θ`, de `300 K` a `500 K`— y activa las proyecciones `π_W`, `π_Q`, `π_U` (no clausura), `π_Θ` y `π_S`. El calor específico a presión constante no se ha tomado como dato externo, sino como composición de primitivos ya declarados.

**Trabajo (proyección `π_W` por `𝔛_Ξ^W`).** El trabajo retorna por su canal presión-volumen, nunca como energía total disponible; su unidad nativa es `UFM·UFE²·UE_MFC⁻²` y su retorno, el julio. El contraste por volúmenes de referencia confirma ese canal mecánico: con `V = m·R·T/P` se obtienen `V₁ = 0.0861 m³` y `V₂ = 0.1435 m³`, de modo que `P·ΔV = 200 kPa × 0.0574 m³ = 11.48 kJ`, en coincidencia con el valor del preámbulo. Retorno: `V_Ξ^W → 11.48 kJ`; el residual `R_Ξ^W` se reduce al de las constantes de referencia.

**Calor (proyección `π_Q` por `𝔛_Ξ^Q`).** El calor exige tránsito térmico, frontera y proceso, y se lee, en un proceso isobárico de sistema cerrado, como variación de entalpía `Λ_th = 𝒜_th + ℬ_∂` (acumulación más frontera). La temperatura ha intervenido como régimen `Θ_th`, no como causa del calor: por sí sola no debe leerse como calor. Retorno: `V_Ξ^Q → 40.2 kJ`.

**Acumulación interna y no clausura (proyección por `𝔛_Ξ^A`).** El contenido que permanece en el sistema se proyecta como `ΔU = m·c_v·(T₂ − T₁) = 0.2 × 0.718 × 200 = 28.72 kJ`. El balance térmico raigal separa de manera explícita las tres contribuciones, `𝔇_Γ𝒜_th = 𝒲_th + 𝒬_th + 𝒰_th`; la derivada `𝔇_Γ` se toma entre los sucesos declarados de la trayectoria `Γ`, no respecto de un tiempo primitivo, pues el Sistema Vectorial no admite el tiempo como magnitud rectora. La no clausura `𝒰_th` retiene aquello que el proceso no devuelve como trabajo o calor consistente, e impide presentar un resultado térmico favorable cuando queda residual sin absorber. Instanciado, el balance se satisface sin contradicción: `40.2 = 28.72 + 11.48 + 𝒰_th`, con `𝒰_th = 0` por la idealización declarada, no por omisión. El criterio del dominio prohíbe presentar `𝒰_th` como error de cálculo: permanece en cero porque el régimen ideal lo justifica, y queda anotado como hipótesis explícita.

**Retorno térmico y entropía (proyección `π_S` por `𝔛_Ξ^S`).** La lectura quedaría incompleta solo con calor y trabajo; el dominio requiere una magnitud de irreversibilidad estructural, controlada por `𝔇_Γ𝓗_th ≥ 0`. En el tramo isobárico, `ΔS = m·c_p·ln(T₂/T₁) = 0.2 × 1.005 × ln(500/300) = 0.1027 kJ/K ≈ 102.7 J/K`. El logaritmo interviene aquí como operación de retorno del dominio termodinámico externo, no como operación nativa del raigal. Como `𝔇_Γ𝓗_th > 0`, el régimen es legible y la lectura no impone temperatura por división ni reinterpreta la trayectoria como reversible. La entropía no opera aquí como desorden verbal ni como ignorancia: es retorno de régimen con unidad verificable.

**Admisibilidad y dictamen del caso.** El dominio se admite cuando el criterio `Termo_Ξ` se satisface sin contradicción material: declarados el dominio y su lectura `Ω_th`, tipadas las proyecciones, presentes las unidades nativa y de retorno, el proceso, la frontera, el residual y la traza, y conservada `U` sin identificar el raigal con ninguna magnitud térmica. En el caso, todas las condiciones se satisfacen: **dictamen `= 0`**. Los únicos residuales materiales son metrológicos —el redondeo de `R` y `c_v`, conservado como normalización pendiente y no presentado como resultado exacto—; cualquier fricción o disipación real reabriría `𝒰_th`, que debería retornarse y no absorberse en `W` o `Q`.

### Matriz especializada de retorno termodinámico

El caso anterior activa cinco proyecciones; el inventario completo del dominio, para su consulta en otros procesos, es el siguiente. Cada magnitud conserva su retorno propio según el recorrido `H_Ξ(o,D_th) → 𝔛_Ξ^X → UR_Ξ^X(D_th) → unidad SI → residual → traza`.

| Proyección termodinámica | Transductor | Unidad nativa | Unidad de retorno | Unidad SI | Usar cuando | No usar cuando | Retorno y residual | Dictamen |
|---|---|---|---|---|---|---|---|---|
| Trabajo | `𝔛_Ξ^W` | `UFM·UFE²·UE_MFC⁻²` | `UR_Ξ^W(D_th)` | J | hay fuerza-desplazamiento, presión-volumen o canal mecánico declarado | se confunde con energía total disponible | `V_Ξ^W=W_Ξ·UR_Ξ^W`; `R_Ξ^W` mide pérdida de canal mecánico | condicionado |
| Calor | `𝔛_Ξ^Q` | `UFM·UFE²·UE_MFC⁻²` con régimen `UFT` | `UR_Ξ^Q(D_th)` | J | hay tránsito térmico, frontera y proceso declarado | se emplea la temperatura sola como calor | `V_Ξ^Q=Q_Ξ·UR_Ξ^Q`; `R_Ξ^Q` mide calor omitido, fase o frontera | condicionado |
| No clausura térmica | `𝔛_Ξ^U` | `UFM·UFE²·UE_MFC⁻²` | `UR_Ξ^U(D_th)` | J o residual de dominio | el balance deja contenido no devuelto por trabajo o calor | se presenta como error de cálculo | `V_Ξ^U=U_Ξ·UR_Ξ^U`; `R_Ξ^U` retiene la no clausura | `U` o condicionado |
| Temperatura | `𝔛_Ξ^Θ` | `UFT` | `UR_Ξ^Θ(D_th)` | K | hay régimen térmico y escala declarada | se trata como fundamento del proceso | `V_Ξ^Θ=Θ_Ξ·UR_Ξ^Θ`; `R_Ξ^Θ` mide régimen térmico no resuelto | condicionado |
| Entropía | `𝔛_Ξ^S` | `UFM·UFE²·UE_MFC⁻²·UFT⁻¹` | `UR_Ξ^S(D_th)` | J·K⁻¹ | hay proceso, trayectoria y régimen térmico | se emplea como desorden verbal, probabilidad o ignorancia | `V_Ξ^S=S_Ξ·UR_Ξ^S`; `R_Ξ^S` mide no clausura de régimen | condicionado |
| Entalpía | `𝔛_Ξ^Λ` | `UFM·UFE²·UE_MFC⁻²` | `UR_Ξ^Λ(D_th)` | J | hay acumulación, presión, volumen y frontera | se emplea como energía total sin dominio | `V_Ξ^Λ=Λ_Ξ·UR_Ξ^Λ`; `R_Ξ^Λ` mide energía de frontera no resuelta | condicionado |
| Acumulación interna | `𝔛_Ξ^A` | `UFM·UFE²·UE_MFC⁻²` | `UR_Ξ^A(D_th)` | J | se evalúa contenido de dominio entre sucesos | se identifica con sustancia o energía oculta | `V_Ξ^A=A_Ξ·UR_Ξ^A`; `R_Ξ^A` mide contenido no recompuesto | condicionado |
| Energía libre | `𝔛_Ξ^G` | `UFM·UFE²·UE_MFC⁻²` | `UR_Ξ^G(D_th)` | J | hay entalpía, temperatura y entropía declaradas | se emplea como espontaneidad verbal | `V_Ξ^G=G_Ξ·UR_Ξ^G`; `R_Ξ^G` mide disponibilidad no resuelta | condicionado |
| Energía libre de Helmholtz | `𝔛_Ξ^{A_H}` | `UFM·UFE²·UE_MFC⁻²` | `UR_Ξ^{A_H}(D_th)` | J | hay energía interna, temperatura y entropía declaradas | se aplica sin régimen de volumen o frontera | `V_Ξ^{A_H}=A_{H,Ξ}·UR_Ξ^{A_H}`; `R_Ξ^{A_H}` mide disponibilidad no resuelta | condicionado |
| Capacidad calorífica | `𝔛_Ξ^C` | `UFM·UFE²·UE_MFC⁻²·UFT⁻¹` | `UR_Ξ^C(D_th)` | J·K⁻¹ | calor y variación térmica pertenecen al mismo sistema | se emplea sin proceso térmico | `V_Ξ^C=C_Ξ·UR_Ξ^C`; `R_Ξ^C` mide régimen térmico no resuelto | condicionado |
| Calor específico | `𝔛_Ξ^c` | `UFE²·UE_MFC⁻²·UFT⁻¹` | `UR_Ξ^c(D_th)` | J·kg⁻¹·K⁻¹ | masa, calor y temperatura pertenecen al mismo dominio | se mezcla masa seca, agua, tejido o fase sin declarar | `V_Ξ^c=c_Ξ·UR_Ξ^c`; `R_Ξ^c` mide composición térmica | condicionado |
| Potencia térmica | `𝔛_Ξ^{Pth}` | `UFM·UFE²·UE_MFC⁻³` | `UR_Ξ^{Pth}(D_th)` | W | hay energía térmica por duración externa declarada | se convierte la tasa en causa fundante | `V_Ξ^{Pth}=P_{th,Ξ}·UR_Ξ^{Pth}`; `R_Ξ^{Pth}` mide desajuste energía-ciclo | condicionado |
| Presión termodinámica | `𝔛_Ξ^Π` | `UFM·UFE⁻¹·UE_MFC⁻²` | `UR_Ξ^Π(D_th)` | Pa | hay superficie, frontera y fuerza distribuida | se reduce toda frontera a presión | `V_Ξ^Π=Π_Ξ·UR_Ξ^Π`; `R_Ξ^Π` mide tensión no resuelta | condicionado |
| Volumen de proceso | `𝔛_Ξ^V` | `UFE³` | `UR_Ξ^V(D_th)` | m³ | volumen, fase y frontera están declarados | se traslada volumen entre fases sin tránsito | `V_Ξ^V=V_Ξ·UR_Ξ^V`; `R_Ξ^V` mide fase o frontera no resuelta | condicionado |
| Cambio de fase | `𝔛_Ξ^{φ}` | combinación de `UFM`, `UFE`, `UFT` y energía derivada | `UR_Ξ^{φ}(D_th)` | unidad del proceso | hay fase inicial, fase final, frontera y calor latente declarado | se emplea la fase como etiqueta sin proceso | `V_Ξ^{φ}=φ_Ξ·UR_Ξ^{φ}`; `R_Ξ^{φ}` mide tránsito de fase incompleto | condicionado |
| Conductividad térmica | `𝔛_Ξ^k` | `UFM·UFE·UE_MFC⁻³·UFT⁻¹` | `UR_Ξ^k(D_th)` | W·m⁻¹·K⁻¹ | hay gradiente, medio y flujo térmico | se emplea sin geometría o material | `V_Ξ^k=k_Ξ·UR_Ξ^k`; `R_Ξ^k` mide medio no declarado | condicionado |
| Difusividad térmica | `𝔛_Ξ^{a}` | `UFE²·UE_MFC⁻¹` | `UR_Ξ^{a}(D_th)` | m²·s⁻¹ | hay medio, capacidad y conducción declaradas | se confunde con velocidad de calentamiento | `V_Ξ^{a}=a_Ξ·UR_Ξ^{a}`; `R_Ξ^{a}` mide régimen material | condicionado |
| Coeficiente de expansión | `𝔛_Ξ^{β}` | `UFT⁻¹` | `UR_Ξ^{β}(D_th)` | K⁻¹ | hay cambio dimensional por temperatura | se emplea sin fase ni material | `V_Ξ^{β}=β_Ξ·UR_Ξ^{β}`; `R_Ξ^{β}` mide expansión no resuelta | condicionado |

### Patrón `P_H₂O` en el dominio termodinámico

En termodinámica, `P_H₂O = (1 mol de H₂O líquida, 25 °C, 1 atm)` da entrada a la lectura, pero no la resuelve por sí solo. Cantidad, masa, densidad, volumen, presión y temperatura de referencia pueden retornarse con unidad nativa y unidad externa declaradas. En cambio, calor, trabajo, potencia, entropía, energía libre, cambio de fase, conductividad o difusividad exigen proceso adicional. Sin proceso, la salida correcta es `U`.

| Entrada del patrón | Unidad nativa | Retorno externo | Estado en la referencia | Residual |
|---|---|---|---|---|
| Cantidad de entidad | `UFCE` | `1 mol` de moléculas de agua | entrada resuelta si la entidad está tipada | `R_Ξ^N = 0` bajo tipado suficiente |
| Masa del patrón | `UFM` | `0,01801528 kg` | condicionada a la masa molar de referencia | residual metrológico de referencia |
| Volumen líquido | `UFE³` | `1,8068636684×10⁻⁵ m³` | condicionado a densidad, fase y temperatura | residual de densidad y fase |
| Densidad | `UFM·UFE⁻³` | `997,047 kg·m⁻³` | condicionada a `25 °C` | residual térmico de referencia |
| Temperatura de referencia | `UFT` | `298,15 K` | condición de régimen | residual si cambia el régimen térmico |
| Presión de referencia | `UFM·UFE⁻¹·UE_MFC⁻²` | `101325 Pa` | condición externa declarada | residual de frontera externa |
| Calor sensible | `UFM·UFE²·UE_MFC⁻²` | J | `U` sin tramo térmico declarado | residual de proceso térmico |
| Trabajo presión-volumen | `UFM·UFE²·UE_MFC⁻²` | J | `U` sin cambio de volumen o presión útil | residual mecánico de frontera |
| Potencia térmica | `UFM·UFE²·UE_MFC⁻³` | W | `U` sin duración externa declarada | residual energía-ciclo |
| Entropía de proceso | `UFM·UFE²·UE_MFC⁻²·UFT⁻¹` | J·K⁻¹ | `U` sin trayectoria térmica | residual de régimen |
| Cambio de fase | unidad derivada de proceso | unidad del proceso | `U` sin fase final y calor asociado | residual de fase |

### Irreversibilidad estructural y conservación de `U`

La lectura termodinámica quedaría incompleta si solo tratase calor y trabajo: el dominio necesita una magnitud de irreversibilidad estructural. Esa función la cumple `H_SV` en su plano propio; acompaña una trayectoria admisible, se construye por agregación estratificada y no decrece bajo adición irreversible y honestidad de coordenadas. Esa propiedad se recibe aquí como restricción del dominio: ningún balance térmico puede declararse consistente borrando residual, reinterpretando `U` como dato resuelto o convirtiendo por redacción una trayectoria en retorno reversible. La regla es `𝔇_Γ𝓗_th ≥ 0`, y la temperatura de dominio solo es legible si `𝔇_Γ𝓗_th > 0` o si el caso declara una condición límite compatible. Cuando `𝔇_Γ𝓗_th = 0`, no se impone temperatura por división ni se declara consistencia térmica plena sin justificar el régimen; la igualdad no autoriza a borrar `𝒰_th`.

| Control termodinámico | Forma | Función raigal | Riesgo bloqueado |
|---|---|---|---|
| Balance de intercambio | `𝔇_Γ𝒜_th = 𝒲_th + 𝒬_th + 𝒰_th` | separa trabajo, calor y no clausura | resultado térmico sin residual |
| Irreversibilidad | `𝔇_Γ𝓗_th ≥ 0` | impide la retrolectura del régimen | tiempo rector o reversión narrativa |
| Temperatura de dominio | `Θ_th = UFT(𝔇_Γ𝒬_th / 𝔇_Γ𝓗_th)` | devuelve el régimen térmico | temperatura como causa total |
| Entalpía | `Λ_th = 𝒜_th + ℬ_∂` | conserva acumulación y frontera | energía de frontera omitida |
| Residual térmico | `R_Ξ^Q`, `R_Ξ^S`, `R_Ξ^U` | retiene la no clausura térmica | error encubierto o promedio impuesto |
| Patrón de agua | `P_H₂O` | referencia de entrada, no fundamento | el agua como raíz del raigal |

### Criterio de admisibilidad del dominio

La admisión termodinámica exige que se satisfaga, sin contradicción material, el criterio

`Termo_Ξ admisible ⇔ D_th declarado ∧ Ω_th construida ∧ π_W, π_Q, π_U, π_F, π_Θ, π_Λ tipadas ∧ unidad nativa ∧ unidad SI ∧ proceso térmico cuando proceda ∧ frontera ∧ residual ∧ retorno ∧ traza ∧ conservación de U ∧ no identificación del raigal con energía, calor, temperatura o entropía`.

Si falta el proceso térmico, la salida permanece en `U`. Se rechaza la lectura si se emplea la temperatura como calor, si se declara la entropía como desorden verbal, si se omite la no clausura `𝒰_th`, si se toma `P_H₂O` como fundamento en lugar de referencia, o si se traslada una constante externa sin transductor y sin residual.

Permanece una reserva de normalización dimensional: la matriz de retorno adopta para las magnitudes energéticas la forma nativa `UFM·UFE²·UE_MFC⁻²`, compatible con el retorno externo en julios. Si una variable interna conserva una convención distinta por su documento de origen, esa diferencia se trata como normalización pendiente de la notación del dominio antes de declarar consistencia dimensional suficiente: no se resuelve por inferencia ni se disimula como resultado consistente, sino que se conserva como punto de revisión técnica visible hasta que la referencia termodinámica común la verifique.

El criterio térmico queda así delimitado: el raigal puede sostener un tránsito termodinámico completo sin ser calor, trabajo, energía, temperatura ni entropía. Las magnitudes vuelven a unidades externas; la referencia nativa conserva continuidad por `UR_Ξ^X(D_th)` y por el residual correspondiente.
