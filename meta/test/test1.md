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

## II.2. Electricidad y campo magnético: carga, corriente, campo, frontera y propagación

El dominio eléctrico-magnético reúne las magnitudes de fuente y campo —carga, corriente, campo eléctrico e inducción magnética— y las que rigen su comportamiento: relaciones constitutivas del medio, energía de campo, frontera y propagación (Lloret Egea, 2026k, 2026l). El raigal no se convierte en campo, carga, corriente, onda ni potencia eléctrica; fija cómo una proyección raigal retorna por magnitudes eléctricas y magnéticas cuando el dominio declara fuente, medio, frontera, canal, residual, retorno y traza.

**El régimen como sistema cerrado.** El dominio no se reduce a una lista de unidades: se recibe como sistema cerrado de relaciones. Su estado se lee como `𝕏_em = (D, B, E, H)` —desplazamiento eléctrico, inducción magnética, campo eléctrico y campo magnético—; las fuentes como `𝕐_em = (ρ, 0, 0, J)` —densidad de carga y densidad de corriente—; y la lectura constitutiva como `ℂ_em = (ε_em, μ_em, σ_em)` —permitividad, permeabilidad y conductividad—. Estos objetos no son fundamento del raigal: son magnitudes devueltas por el dominio cuando la proyección está suficientemente tipada. El sistema de primer orden es `Div_em(D) = ρ`, `Div_em(B) = 0`, `Rot_em(E) + ∂_νB = 0` y `Rot_em(H) − ∂_νD = J`, donde la derivada `∂_ν` se lee respecto del índice factual de suceso, no como tiempo rector: el Sistema Vectorial no admite el tiempo como magnitud primitiva. Las relaciones constitutivas `D = ε_em(E)`, `B = μ_em(H)` y `J = σ_em(E) + J_ext` impiden confundir campo con medio. El cierre se formula como `EM_Ξ(Ω_em) = 0`, satisfecho cuando concurren el sistema de primer orden, las relaciones constitutivas, la frontera activa, unidad nativa, unidad SI, canal, residual, retorno y traza. El dominio especializa el raigal; no lo gobierna.

> **Caso de aplicación.** Un conductor recto de cobre transporta una corriente constante `I = 15 A` en una región de campo magnético uniforme `B = 0.4 T`; su longitud activa es `L = 0.8 m` y forma un ángulo `θ = 30°` con las líneas de flujo. La lectura ordinaria aplica la ley de la fuerza magnética en su forma de Laplace. La fuerza sobre el conductor es `F = I·L·B·sin(θ) = 15 × 0.8 × 0.4 × 0.5 = 2.4 N`. Es máxima cuando el conductor queda perpendicular al campo (`θ = 90°`, `sin(90°) = 1`): `F_máx = I·L·B = 15 × 0.8 × 0.4 = 4.8 N`. Sobre este resultado conocido se construye la lectura raigal. El régimen se declara estacionario, con fuente de corriente, medio conductor de cobre, campo uniforme externo y orientación angular fijada; sin fuente, medio, geometría y frontera de orientación declaradas, la salida correcta sería `U`.

**Recepción del dominio.** El estado recibe la inducción declarada en `𝕏_em` (`B` uniforme del medio externo); las fuentes reciben la corriente en `𝕐_em`, cuya forma de línea integra densidad y sección en el producto `I·L`, de modo que no queda sección de canal sin resolver; y las constitutivas reciben en `ℂ_em` la conductividad `σ_em` del cobre como medio. Las entradas se tipan así: corriente por `𝔛_Ξ^I` (`UFC`, `15 A`), inducción por `𝔛_Ξ^B` (`UFM·UFC⁻¹·UE_MFC⁻²`, `0.4 T`), longitud activa por `𝔛_Ξ^L` (`UFE`, `0.8 m`) y orientación como frontera angular `ℬ_∂` (`θ = 30°`, `sin(θ) = 0.5`). El ángulo no es un dato accesorio: es la proyección de frontera que decide qué fracción del canal corriente-campo retorna como fuerza.

**Fuerza magnética (proyección `π_F` por `𝔛_Ξ^F`).** La fuerza retorna por el canal corriente-campo, nunca como energía electromagnética ni como campo sin mediación. La clave de la lectura raigal es que las tres proyecciones se componen exactamente en la unidad nativa de la fuerza, sin duplicar dominio: `UFC · UFE · (UFM·UFC⁻¹·UE_MFC⁻²) = UFM·UFE·UE_MFC⁻² → N`. El seno de la orientación interviene como operación de retorno —la proyección angular del canal—, no como operación nativa del raigal. Retorno: `V_Ξ^F → 2.4 N`. La fuerza es el retorno mecánico que el dominio eléctrico-magnético produce sobre el conductor; el raigal sostiene el tránsito eléctrico-magnético hacia lo mecánico sin ser él mismo fuerza ni campo.

**Fuerza máxima (reconfiguración de frontera `𝓡_em^f`).** La fuerza máxima no es un segundo cálculo independiente, sino una reconfiguración de frontera: al reorientar el canal hasta la perpendicularidad (`θ = 90°`, `sin(90°) = 1`), la frontera angular pasa a ser plenamente operativa y todo el canal corriente-campo retorna, con `F_máx → 4.8 N`. En lectura raigal se anota como `𝓡_em^f = 𝟙{frontera angular plena}·canal completo`: no aparece energía nueva, se recupera la fracción de canal que la orientación previa mantenía sin retornar.

**Residual de orientación (`R_Ξ^{∂em}`).** La diferencia entre la fuerza máxima y la fuerza a `30°` no es una pérdida que pueda encubrirse: es el residual de orientación que el régimen conserva visible, `R_Ξ^{∂em} = F_máx − F = 4.8 − 2.4 = 2.4 N`. A `30°` solo retorna la mitad del canal (`F/F_máx = sin(30°) = 0.5`); ese residual queda inscrito como frontera angular no resuelta, no como ineficiencia disimulada, y al reorientar a `90°` se reduce a cero. El criterio del dominio prohíbe declarar fuerza sin soporte de frontera y prohíbe simular continuidad de orientación: el ángulo gobierna el retorno y su residual permanece auditado.

**Admisibilidad y dictamen del caso.** El dominio se admite cuando el criterio `EM_Ξ` se satisface sin contradicción material: declarado el dominio, tipados estado, fuentes y constitutivas, presentes la fuente, el medio, la geometría y la frontera de orientación, las unidades nativa y de retorno, el residual, el retorno y la traza, sin tiempo rector y sin identificar el raigal con campo, carga, corriente, onda o energía electromagnética. En el caso, todas las condiciones se satisfacen: **dictamen `= 0`**. Los residuales materiales son la orientación angular —`R_Ξ^{∂em} = 2.4 N` a `30°`— y el de las constantes de referencia (`I`, `L`, `B`). La frecuencia no comparece, pues el régimen es estacionario; cualquier no uniformidad real del campo, resistencia de canal o disipación reabriría residuales que deberían retornarse y no absorberse en `F`.

### Matriz especializada de retorno eléctrico-magnético

El caso activa cuatro proyecciones; el inventario completo del dominio, para su consulta en otros regímenes, es el siguiente.

| Proyección eléctrica o magnética | Transductor | Unidad nativa | Unidad de retorno | Unidad SI | Usar cuando | No usar cuando | Retorno y residual | Dictamen |
|---|---|---|---|---|---|---|---|---|
| Carga eléctrica | `𝔛_Ξ^C` | `UFC·UE_MFC` | `UR_Ξ^C(Ω_em)` | C | hay portador, separación o balance de carga declarado | se emplea carga sin portador, frontera o canal | `V_Ξ^C=C_Ξ·UR_Ξ^C`; `R_Ξ^C` mide carga no retornada | condicionado |
| Corriente eléctrica | `𝔛_Ξ^I` | `UFC` | `UR_Ξ^I(Ω_em)` | A | hay flujo de carga por canal declarado | se confunde la señal con la identidad completa | `V_Ξ^I=I_Ξ·UR_Ξ^I`; `R_Ξ^I` mide pérdida de canal | condicionado |
| Densidad de carga | `𝔛_Ξ^ρ_e` | `UFC·UE_MFC·UFE⁻³` | `UR_Ξ^ρe(Ω_em)` | C·m⁻³ | hay volumen, carga y frontera comunes | se extrapola carga local a dominio global sin soporte | `V_Ξ^ρe=ρ_{e,Ξ}·UR_Ξ^ρe`; `R_Ξ^ρe` mide volumen o fuente no resuelta | condicionado |
| Densidad de corriente | `𝔛_Ξ^J` | `UFC·UFE⁻²` | `UR_Ξ^J(Ω_em)` | A·m⁻² | hay corriente distribuida sobre superficie o sección | se emplea la corriente total como densidad | `V_Ξ^J=J_Ξ·UR_Ξ^J`; `R_Ξ^J` mide sección u orientación no resuelta | condicionado |
| Campo eléctrico | `𝔛_Ξ^{E_c}` | `UFM·UFE·UFC⁻¹·UE_MFC⁻³` | `UR_Ξ^{E_c}(Ω_em)` | V·m⁻¹ | hay potencial-distancia, fuerza-carga o configuración de campo | se declara campo sin geometría, carga o frontera | `V_Ξ^{E_c}=E_{c,Ξ}·UR_Ξ^{E_c}`; `R_Ξ^{E_c}` mide residual de potencial y frontera | condicionado |
| Desplazamiento eléctrico | `𝔛_Ξ^D` | `UFC·UE_MFC·UFE⁻²` | `UR_Ξ^D(Ω_em)` | C·m⁻² | hay campo eléctrico y permitividad de medio | se confunde con campo eléctrico sin mediación | `V_Ξ^D=D_Ξ·UR_Ξ^D`; `R_Ξ^D` mide medio no declarado | condicionado |
| Inducción magnética | `𝔛_Ξ^B` | `UFM·UFC⁻¹·UE_MFC⁻²` | `UR_Ξ^B(Ω_em)` | T | hay flujo magnético, medio o inducción declarada | se asigna magnetismo al patrón sin configuración | `V_Ξ^B=B_Ξ·UR_Ξ^B`; `R_Ξ^B` mide residual de inducción o canal | condicionado |
| Campo magnético | `𝔛_Ξ^H` | `UFC·UFE⁻¹` | `UR_Ξ^H(Ω_em)` | A·m⁻¹ | hay corriente, medio y geometría compatibles | se confunde con inducción magnética | `V_Ξ^H=H_Ξ·UR_Ξ^H`; `R_Ξ^H` mide corriente o medio no resuelto | condicionado |
| Potencial eléctrico o tensión | `𝔛_Ξ^V` | `UFM·UFE²·UE_MFC⁻³·UFC⁻¹` | `UR_Ξ^V(Ω_em)` | V | hay dos puntos, referencia y canal eléctrico | se declara tensión sin referencia | `V_Ξ^V=V_Ξ·UR_Ξ^V`; `R_Ξ^V` mide pérdida de referencia | condicionado |
| Resistencia | `𝔛_Ξ^R` | `UFM·UFE²·UE_MFC⁻³·UFC⁻²` | `UR_Ξ^R(Ω_em)` | Ω | hay tensión, corriente y disipación declaradas | se confunde con impedancia total | `V_Ξ^R=R_Ξ·UR_Ξ^R`; `R_Ξ^R` mide disipación no resuelta | condicionado |
| Conductancia | `𝔛_Ξ^G` | `UFC²·UE_MFC³·UFM⁻¹·UFE⁻²` | `UR_Ξ^G(Ω_em)` | S | hay canal y relación corriente-tensión consistente | se emplea sin geometría de canal | `V_Ξ^G=G_Ξ·UR_Ξ^G`; `R_Ξ^G` mide canal no declarado | condicionado |
| Conductividad | `𝔛_Ξ^σ` | `UFC²·UE_MFC³·UFM⁻¹·UFE⁻³` | `UR_Ξ^σ(Ω_em)` | S·m⁻¹ | hay material, medio y campo eléctrico declarado | se extrapola entre medios sin tránsito | `V_Ξ^σ=σ_Ξ·UR_Ξ^σ`; `R_Ξ^σ` mide medio o temperatura no resuelta | condicionado |
| Permitividad | `𝔛_Ξ^ε` | `UFC²·UE_MFC⁴·UFM⁻¹·UFE⁻³` | `UR_Ξ^ε(Ω_em)` | F·m⁻¹ | hay medio dieléctrico y campo eléctrico | se emplea como constante universal del raigal | `V_Ξ^ε=ε_Ξ·UR_Ξ^ε`; `R_Ξ^ε` mide clase de medio no resuelta | condicionado |
| Permeabilidad | `𝔛_Ξ^μ` | `UFM·UFE·UFC⁻²·UE_MFC⁻²` | `UR_Ξ^μ(Ω_em)` | H·m⁻¹ | hay medio magnético y campo magnético | se emplea sin régimen material | `V_Ξ^μ=μ_Ξ·UR_Ξ^μ`; `R_Ξ^μ` mide régimen magnético no resuelto | condicionado |
| Capacitancia | `𝔛_Ξ^{C_el}` | `UFC²·UE_MFC⁴·UFM⁻¹·UFE⁻²` | `UR_Ξ^{C_el}(Ω_em)` | F | hay carga, potencial, geometría y dieléctrico | se emplea sin frontera de almacenamiento | `V_Ξ^{C_el}=C_{el,Ξ}·UR_Ξ^{C_el}`; `R_Ξ^{C_el}` mide almacenamiento no resuelto | condicionado |
| Inductancia | `𝔛_Ξ^{L_el}` | `UFM·UFE²·UE_MFC⁻²·UFC⁻²` | `UR_Ξ^{L_el}(Ω_em)` | H | hay corriente, flujo magnético y geometría inductiva | se asigna a canal sin flujo | `V_Ξ^{L_el}=L_{el,Ξ}·UR_Ξ^{L_el}`; `R_Ξ^{L_el}` mide inducción no resuelta | condicionado |
| Impedancia | `𝔛_Ξ^Z` | `UFM·UFE²·UE_MFC⁻³·UFC⁻²` | `UR_Ξ^Z(Ω_em)` | Ω | hay régimen alterno, resistencia y reactancia | se emplea como resistencia simple sin fase | `V_Ξ^Z=Z_Ξ·UR_Ξ^Z`; `R_Ξ^Z` mide separación no resuelta entre disipación y retorno oscilante | condicionado |
| Flujo magnético | `𝔛_Ξ^ΦB` | `UFM·UFE²·UFC⁻¹·UE_MFC⁻²` | `UR_Ξ^ΦB(Ω_em)` | Wb | hay inducción y superficie orientada | se declara sin área ni orientación | `V_Ξ^ΦB=Φ_{B,Ξ}·UR_Ξ^ΦB`; `R_Ξ^ΦB` mide frontera de flujo | condicionado |
| Energía electromagnética local | `𝔛_Ξ^u` | `UFM·UFE⁻¹·UE_MFC⁻²` | `UR_Ξ^u(Ω_em)` | J·m⁻³ | hay campos y excitaciones compatibles | se identifica la energía de campo con el raigal | `V_Ξ^u=u_Ξ·UR_Ξ^u`; `R_Ξ^u` mide almacenamiento no resuelto | condicionado |
| Flujo de energía electromagnética | `𝔛_Ξ^S` | `UFM·UE_MFC⁻³` | `UR_Ξ^S(Ω_em)` | W·m⁻² | hay campo eléctrico, campo magnético y frontera de flujo | se emplea como potencia total sin superficie | `V_Ξ^S=S_Ξ·UR_Ξ^S`; `R_Ξ^S` mide frontera de flujo | condicionado |
| Velocidad de propagación | `𝔛_Ξ^v` | `UFE·UE_MFC⁻¹` | `UR_Ξ^v(Ω_em)` | m·s⁻¹ | hay medio y relación constitutiva compatible | se importa por analogía sin medio | `V_Ξ^v=v_Ξ·UR_Ξ^v`; `R_Ξ^v` mide medio o régimen no resuelto | condicionado |
| Frecuencia de régimen | `𝔛_Ξ^f` | `UE_MFC⁻¹` | `UR_Ξ^f(Ω_em)` | Hz | hay ciclo medido y señal periódica | se convierte la frecuencia en tiempo rector | `V_Ξ^f=f_Ξ·UR_Ξ^f`; `R_Ξ^f` mide ciclo no declarado | condicionado |
| Longitud de onda | `𝔛_Ξ^λ` | `UFE` | `UR_Ξ^λ(Ω_em)` | m | hay propagación, medio y señal | se emplea como objeto material completo | `V_Ξ^λ=λ_Ξ·UR_Ξ^λ`; `R_Ξ^λ` mide medio o frontera | condicionado |

### Frontera, continuidad y reconfiguración del dominio

El régimen eléctrico-magnético exige frontera con más precisión que una geometría externa genérica. Las condiciones de contorno separan componentes normales y tangenciales; la frontera activa decide cuándo la interfase pasa a ser operativa; y la reconfiguración solo procede cuando el régimen pierde invertibilidad local. En lectura raigal, esto impide declarar campo, inducción, tensión o flujo sin soporte de frontera. Una magnitud puede tener dimensión correcta y, aun así, ser inadmisible por falta de superficie, orientación, medio o canal; la matriz raigal conserva ese residual como `R_Ξ^{∂em}` antes de devolver la magnitud al SI.

| Control de frontera | Forma | Función en el dominio | Riesgo bloqueado |
|---|---|---|---|
| Gauss eléctrica de frontera | `⟨D_2−D_1,n⟩=ρ_s` | controla el salto normal del desplazamiento eléctrico | carga superficial omitida |
| Gauss magnética de frontera | `⟨B_2−B_1,n⟩=0` | conserva la continuidad normal de inducción | introducir fuente magnética indebida |
| Faraday interfacial | `n×(E_2−E_1)=0` | conserva la continuidad tangencial del campo eléctrico | tensión de borde no declarada |
| Ampère interfacial | `n×(H_2−H_1)=J_s` | controla el salto tangencial del campo magnético | corriente superficial omitida |
| Frontera activa | `det(𝒥_em)=0 ⇔ ∂Ω_em activa` | localiza la pérdida de invertibilidad local | frontera por apariencia |
| Reconfiguración | `𝓡_em^f=𝟙{det(𝒥_em)=0}Λ_emB_reg` | declara la respuesta interna del régimen | respuesta opaca del medio |
| Residual de frontera | `R_Ξ^{∂em}` | conserva discontinuidades, pérdidas y no clausura | continuidad aparente |

### Patrón `P_H₂O` en el dominio eléctrico-magnético

En electricidad y campo magnético, `P_H₂O = (1 mol de H₂O líquida, 25 °C, 1 atm)` no basta para resolver el dominio. Permite trasladar cantidad, masa, volumen, temperatura y presión desde el repertorio general, pero no autoriza campo eléctrico, campo magnético, corriente, conductividad, permitividad o propagación sin configuración, medio, canal, método y frontera declarados.

| Entrada del patrón | Unidad nativa | Retorno externo | Estado en el dominio | Residual |
|---|---|---|---|---|
| Cantidad de moléculas | `UFCE` | `1 mol` | entrada de referencia, no régimen eléctrico por sí sola | residual nulo solo bajo tipado de entidad |
| Carga neta | `UFC·UE_MFC` | C | `U` salvo neutralidad, ionización o separación declarada | residual de carga |
| Corriente | `UFC` | A | `U` sin canal eléctrico y desplazamiento de carga | residual de canal |
| Campo eléctrico | `UFM·UFE·UFC⁻¹·UE_MFC⁻³` | V·m⁻¹ | `U` sin configuración de potencial, carga o frontera | residual de configuración |
| Inducción magnética | `UFM·UFC⁻¹·UE_MFC⁻²` | T | `U` sin corriente, medio o flujo declarado | residual de inducción |
| Conductividad | `UFC²·UE_MFC³·UFM⁻¹·UFE⁻³` | S·m⁻¹ | `U` sin muestra, pureza, iones, temperatura y método | residual de medio |
| Permitividad | `UFC²·UE_MFC⁴·UFM⁻¹·UFE⁻³` | F·m⁻¹ | `U` sin medio y protocolo de lectura | residual dieléctrico |
| Permeabilidad | `UFM·UFE·UFC⁻²·UE_MFC⁻²` | H·m⁻¹ | `U` sin régimen magnético declarado | residual magnético |
| Potencia eléctrica | `UFM·UFE²·UE_MFC⁻³` | W | `U` sin tensión, corriente y duración externa | residual energía-ciclo |
| Energía electromagnética | `UFM·UFE²·UE_MFC⁻²` | J | `U` sin campos, volumen y proceso | residual de almacenamiento |

### Balance, propagación y lectura de onda

El régimen eléctrico-magnético conserva una identidad de balance de energía de campo: `u_em = ½(⟨E,D⟩ + ⟨H,B⟩)`, `S_em = E×H` y `∂_νu_em + Div_em(S_em) = −⟨E,J⟩`. La densidad de energía `u_em` y el flujo `S_em` no son energía raigal: son retornos del dominio cuando campos, excitaciones, medio, volumen y frontera están declarados. El término `−⟨E,J⟩` conserva la disipación o la transferencia interna, y no debe presentarse como eficiencia favorable. La propagación se admite solo cuando hay medio y relaciones constitutivas compatibles, mediante `Rot_em(Rot_em(E)) + ε_emμ_em∂_ν²E = 0` y `v_em² = 1/(ε_emμ_em)`; aquí `v_em` retorna por `UFE·UE_MFC⁻¹` y no introduce tiempo rector. Si el medio es desconocido, si `ε_em` o `μ_em` no están declaradas, o si el soporte de onda no está justificado, la salida permanece en `U`. La onda eléctrica-magnética no fundamenta el raigal; solo permite leer la propagación de una magnitud retornada del dominio.

### Criterio de admisibilidad del dominio

La admisión eléctrica-magnética exige que se satisfaga, sin contradicción material, el criterio

`EM_Ξ admisible ⇔ Ω_em declarado ∧ 𝕏_em, 𝕐_em, ℂ_em tipados ∧ 𝕄_em=0 ∧ 𝕂_em=0 ∧ frontera o volumen compatible ∧ unidades nativas ∧ unidades SI ∧ fuente, medio o canal cuando proceda ∧ residual ∧ retorno ∧ traza ∧ no tiempo rector ∧ no probabilidad ∧ no identificación del raigal con campo, carga, corriente, onda o energía electromagnética`.

Si falta fuente, medio, geometría, canal, volumen, superficie, frontera o relación constitutiva sin contradicción material, la salida permanece en `U`. Se rechaza la lectura si se declara campo sin fuente o frontera; si se identifica el raigal con campo eléctrico, campo magnético, carga, corriente, potencial, onda o energía electromagnética; si se traslada una magnitud eléctrica hacia biología, medicina, señal o química sin tránsito de dominio; o si se emplea la frecuencia como tiempo rector o la propagación como destino.

La reserva técnica es la siguiente: el dominio eléctrico-magnético se sostiene metrológicamente sobre `UE_MFC`, `UFE`, `UFM` y `UFC`. Cuando se acopla a termodinámica, química, biología, genética, inmunología o medicina, pueden comparecer `UFT` y `UFCE`, pero solo por tránsito de dominio, no por modificación del desarrollo eléctrico-magnético; esta reserva impide mezclar corriente, carga, molécula, temperatura, célula o señal clínica como si pertenecieran a un mismo plano sin transductor.

El criterio eléctrico-magnético queda así acotado: el raigal puede sostener un tránsito eléctrico y magnético completo sin ser campo, carga, corriente, onda, tensión ni energía electromagnética. Esas magnitudes vuelven a unidades externas; la referencia nativa conserva continuidad por `UR_Ξ^X(Ω_em)` y por los residuales de fuente, medio, frontera, canal y propagación.
## II.3. Cosmología: universo observable, distancias, edades relativas, Λ y clausura de observables

La cosmología reúne las magnitudes más propensas a confundir planos de lectura: edad, distancia y horizonte de los observables; señal luminosa y corrimiento al rojo; expansión, gravedad local y constante cosmológica; y la clausura de régimen (Lloret Egea, 2026m, 2026n, 2026t, 2026w, 2026aa, 2026ab, 2026ac). (Véase, para esta restricción, *Teoría del TODO y de la NADA en el Sistema Vectorial SV*.) La regla de entrada es estricta: el dominio cosmológico no mide la totalidad absoluta ni convierte el universo observable en TODO o NADA; mide contenidos físicos retornados dentro de `Ω_obs`, con frontera de lectura, identidad, magnitud, unidad, modelo, residual, retorno y traza. El raigal no se convierte en edad cósmica, distancia, curvatura, `Λ`, energía oscura, señal luminosa ni horizonte; conserva una referencia nativa de retorno cuando esas magnitudes se proyectan bajo dominio declarado.

**El dominio cosmológico.** Se formaliza como `D_cos = (Ω_obs, Obs_cos, F_obs, I_obs, M_obs, U_cos, Γ_cos, R_cos, Ret_cos, Tr_cos)`: dominio físico observable, conjunto de observables tipados, frontera de observación, identidad del observable, familia de magnitudes admitidas, unidad nativa o derivada, trayectoria de retorno, residual, retorno externo y traza. La admisión `Cosmo_Ξ(D_cos) = 0` exige que todos esos elementos se satisfagan sin contradicción. Si el objeto se presenta como totalidad absoluta, no hay edad ni distancia física admisible; si comparece como observable del dominio físico, puede recibir edad relativa, distancia, corrimiento, luminosidad, masa, campo, señal, clausura o retorno, siempre que el residual se resuelva. Si se mezclan totalidad absoluta, universo observable, horizonte de señal y objeto físico interno como si fueran el mismo plano, la lectura se rechaza.

> **Caso de aplicación.** En el estudio de la estructura a gran escala se analiza un cúmulo de galaxias cuya velocidad de recesión, medida por el flujo de Hubble, es `v = 5250 km/s`; se adopta la constante de Hubble `H₀ = 70 (km/s)/Mpc`. La lectura ordinaria resuelve dos magnitudes. La distancia, por la ley empírica de Hubble `v = H₀·d`, es `d = v / H₀ = 5250 / 70 = 75 Mpc`. El tiempo de viaje de la luz, con la conversión `1 Mpc = 3.26 millones de años luz`, es `75 × 3.26 = 244.5 millones de años luz`, de donde `t_cruce = 244.5 Ma`. Sobre este resultado conocido se construye la lectura raigal. El régimen se declara en bajo corrimiento al rojo (`z ≈ 0.0175`), con ley lineal de Hubble, sin integral de modelo `ΛCDM` y con conversión estática; el cúmulo comparece como observable de `Ω_obs`, no como totalidad absoluta. Sin observable tipado, modelo y frontera de lectura, la salida correcta sería `U`.

**Recepción del dominio.** El cúmulo se recibe como `Obs_cos` tipado, con frontera de observación `F_obs` (la ventana instrumental que recibe hoy la señal), identidad `I_obs` y familia de magnitudes `M_obs = {v_rec, d, t_L}` bajo modelo lineal. Las entradas se tipan así: velocidad recesional por `𝔛_Ξ^v` (`UFE·UE_MFC⁻¹`, `5250 km/s`), leída como tasa de separación del modelo y no como velocidad local universal; constante de Hubble `H₀` como valor de referencia y calibración (`UE_MFC⁻¹`); corrimiento al rojo `z ≈ 0.0175` como firma espectral, no como distancia directa; y el factor `1 Mpc = 3.26 Mal` como aproximación estática-euclídea declarada. La pequeñez de la distancia frente al radio de Hubble (`d/(c/H₀) ≈ 1.75 %`) justifica el régimen lineal: a bajo `z`, las distancias de modelo (`D_C`, `D_P`, `D_L`, `D_A`) casi coinciden, y el residual conserva esa cercanía sin declarar igualdad exacta.

**Distancia al cúmulo (proyección `π_L` por `𝔛_Ξ^L`).** La distancia entra como horizonte raigal y retorna como distancia tipada, no como objeto interno ni como totalidad. En el régimen lineal, `d = v_rec / H₀ = 75 Mpc`. El cociente `v_rec / H₀` interviene como operación de retorno del modelo cosmológico —con denominador, unidad y sentido declarados—, no como operación nativa del raigal. La magnitud se tipa como distancia comóvil o propia en el límite de bajo `z`, donde `D_C ≈ D_P`. Retorno: `V_Ξ^L → 75 Mpc`; el residual `R_Ξ^{DC}` mide el modelo `ΛCDM` no declarado —sin integral de `H(z)`— y la corrección relativista omitida: pequeño porque `z ≈ 0.0175`, pero conservado visible, no borrado.

**Tiempo de viaje de la luz (proyección `π_t` por `𝔛_Ξ^t`, tiempo de mirada atrás `t_L`).** El tiempo de tránsito de los fotones es retorno luminoso, no tiempo rector. Bajo la conversión estática declarada, `t_cruce = t_L = 244.5 Ma`: la luz recibida hoy fue emitida hace `244.5 Ma`, edad de señal luminosa del observable, no edad del objeto completo ni de la totalidad. El tiempo entra por `UE_MFC` y retorna a años; no se convierte en causa temporal del dominio. Retorno: `V_Ξ^t → 244.5 Ma`; el residual `R_Ξ^{tL}` conserva que la conversión `Mpc → Mal → años` es estática-euclídea y desatiende la expansión durante el tránsito —válida a bajo `z`, pero anotada como residual de modelo, no como resultado exacto.

**Régimen de `H₀` y residual de calibración (`R_Ξ^H`).** `H₀ = 70 (km/s)/Mpc` es expansión de modelo, no causa última. Se recibe como valor de referencia adoptado, y su residual `R_Ξ^H` conserva la tensión de calibración del dominio: las medidas tempranas y tardías del universo no concuerdan, y el valor adoptado se sitúa entre ellas. No se declara `H₀` como fundamento, sino como parámetro con residual abierto.

**Admisibilidad y dictamen del caso.** El dominio se admite cuando el criterio `Cosmo_Ξ` se satisface sin contradicción material: declarado `D_cos`, tipado el observable (el cúmulo en `Ω_obs`), presentes magnitud cosmológica propia, unidad nativa, unidad externa, modelo de bajo `z`, frontera de observación, retorno luminoso, residual, traza y conservación de `U`, sin identificar `Ω_obs` con la totalidad absoluta. En el caso, todas las condiciones se satisfacen: **dictamen `= 0`**. Los residuales materiales se conservan visibles, no se disimulan como resultado exacto: el modelo `ΛCDM` no declarado en la distancia (`R_Ξ^{DC}`), la conversión estática que desatiende la expansión (`R_Ξ^{tL}`) y la tensión de calibración de `H₀` (`R_Ξ^H`). La velocidad recesional no es velocidad local universal y `z` no se ha empleado como distancia directa.

### Núcleo cosmológico de la matriz raigal

La regla del tronco es única: toda magnitud externa se recibe como retorno de observable, no como fundamento del dominio.

| Núcleo cosmológico | Función en la matriz raigal | Unidad nativa | Retorno externo | Riesgo bloqueado |
|---|---|---|---|---|
| Universo observable | dominio físico retornado | combinación de `UE_MFC`, `UFE`, `UFM` y retornos de señal | mapas, galaxias, CMB, BAO, supernovas, señales profundas | identificar `Ω_obs` con la totalidad absoluta |
| Edad relativa | escala de contenido retornado | `UE_MFC` | s, años julianos | convertir la edad en fundamento |
| Distancia cosmológica | relación tipada entre observables | `UFE` | m, pc, Mpc, Gpc | medir la totalidad como objeto interno |
| Corrimiento al rojo | firma espectral de retorno | adimensional | `z` | emplear `z` como distancia directa |
| Retorno luminoso | señal física recibida | `UFE`, `UE_MFC`, energía derivada y señal | flujo, espectro, luminosidad, longitud de onda | convertir la luz en edad por sí sola |
| Gravitación local | retorno entre persistencias materiales | `UFM·UFE·UE_MFC⁻²` y derivados | N, m·s⁻², m³·kg⁻¹·s⁻² | emplear `G` como causa total |
| Constante cosmológica | curvatura efectiva de escala observable | `UFE⁻²` | m⁻² | tratar `Λ` como fuerza local o sustancia |
| Profundidad observacional | alcance instrumental y de señal | unidad del retorno declarado | magnitud de catálogo, sensibilidad, ventana | confundir profundidad con distancia única |
| Horizonte de observación | frontera de retorno | `UFE`, `UE_MFC` o unidad de señal | horizonte, límite de acceso, superficie de emisión | tomar la frontera de lectura por frontera absoluta |
| Clausura cosmológica local | cierre de observable o régimen interno | unidad del dominio | traza, no transmisión, saturación, cierre interno | convertir el cierre local en clausura de la totalidad |

### Edades relativas y horizonte raigal

El retorno de edad cosmológica se formula como edad de contenido observable, no como edad de la totalidad. La escala `A_Ωobs` se lee como retorno físico del observable más antiguo con firma persistente admitida en el repertorio correspondiente. Su forma nativa se expresa en `UE_MFC` y su retorno externo en años julianos: `1 s = 9 UE_MFC`, `1 a_J = 284 018 400 UE_MFC`, `A_Ωobs = 13 800 000 000 a_J` y `A_Ωobs^SV = 3 919 453 920 000 000 000 UE_MFC`. Estas expresiones no declaran una edad del TODO o de la NADA: declaran escala de contenido observable retornado. La relación con el horizonte raigal se escribe `H_Ξ(Ω_obs, D_cos) → 𝔛_Ξ^t → A_Ωobs^SV` y, cuando se declara horizonte total `F_Ωobs`, la fracción recorrida es `f_Ξ = A_Ωobs^SV / F_Ωobs^SV` y la apertura restante `α_Ξ = 1 − f_Ξ`. Si el horizonte total no está declarado, no se impone la semiclausura; si el repertorio declara ciclo completo compatible, puede calcularse, y en otro caso la salida permanece en `U`.

| Magnitud de edad | Forma nativa | Retorno externo | Usar cuando | No usar cuando | Residual raigal |
|---|---|---|---|---|---|
| Edad de contenido observable | `UE_MFC` | años julianos, s | hay firma persistente, dominio y retorno | se atribuye a la totalidad absoluta | `R_Ξ^age` mide defecto de dominio, firma o retorno |
| Edad de señal luminosa | `UE_MFC` con retorno luminoso | s, años de mirada atrás si el modelo lo declara | hay emisión, recepción, modelo y trayectoria | se confunde con la edad del objeto completo | `R_Ξ^sig` mide distancia, propagación o identificación |
| Edad de galaxia | `UE_MFC` | años, Gyr | hay población, formación, morfología, espectro y modelo | se convierte en edad del universo entero | `R_Ξ^gal` mide mezcla de señal, población y formación |
| Edad de estrella | `UE_MFC` | años, Myr, Gyr | hay masa, composición, evolución y retorno | se deduce solo por el nombre del objeto | `R_Ξ^star` mide falta de modelo o firma |
| Edad de la totalidad absoluta | no aplicable | no aplicable | nunca como edad física | siempre que se trate como objeto físico interno | salida rechazada por error de plano |
| Horizonte raigal de `Ω_obs` | `UE_MFC` o forma ciclo-distancial | retorno de ciclo si procede | hay dominio, ciclo, frontera y repertorio | se emplea como destino inevitable | `R_Ξ^Hcos` mide horizonte no declarado |

### Distancias cosmológicas, retorno luminoso y profundidad observacional

Las distancias cosmológicas no son intercambiables. La matriz conserva `D_C`, `D_M`, `D_L`, `D_A`, `D_P`, `t_L`, `z`, `v_rec`, `P_obs` y `R_E` como magnitudes tipadas, cada una con su modelo, unidad, ecuación y residual. La distancia de luminosidad no es la angular; la comóvil no es el recorrido de luz; el corrimiento al rojo no es distancia directa; la velocidad recesional no es velocidad local universal; y la profundidad observacional no es distancia física pura. La relación de escala es `R_E = 1/(1+z)`.

| Magnitud cosmológica | Unidad nativa | Retorno externo | Uso especializado | Cuándo usar | Cuándo no usar | Residual raigal |
|---|---|---|---|---|---|---|
| Corrimiento al rojo | adimensional | `z` | espectros, factor de escala, retorno energético | hay línea, emisión, recepción y modelo | se emplea como distancia directa | `R_Ξ^z` mide firma espectral o contribuciones mezcladas |
| Distancia comóvil | `UFE` | m, Mpc, Gpc | coordenada cosmológica descontando escala | hay modelo e integral declarada | se iguala al recorrido de luz | `R_Ξ^DC` mide modelo o parámetro no declarado |
| Distancia transversal comóvil | `UFE` | m, Mpc, Gpc | relación geométrica con curvatura | hay curvatura o modelo declarado | se omite la curvatura | `R_Ξ^DM` mide geometría de modelo |
| Distancia de luminosidad | `UFE` con retorno energético-luminoso | m, Mpc, Gpc | supernovas, candelas, flujo-luminosidad | hay luminosidad o calibración | se iguala a la distancia angular | `R_Ξ^DL` mide calibración, flujo o extinción |
| Distancia angular | `UFE` | m, Mpc, Gpc | tamaño físico y ángulo | hay tamaño físico y ángulo | se emplea sin tamaño físico | `R_Ξ^DA` mide escala angular o corrección omitida |
| Distancia propia | `UFE` | m, Mpc, Gpc | separación física en un régimen de escala | hay factor de escala y evento de lectura | se aplica a la totalidad absoluta | `R_Ξ^DP` mide régimen de escala |
| Tiempo de mirada atrás | `UE_MFC` | s, años | intervalo de modelo emisión-recepción | hay modelo y retorno luminoso | se convierte en tiempo rector | `R_Ξ^tL` mide modelo o señal no resuelta |
| Velocidad recesional | `UFE·UE_MFC⁻¹` | m·s⁻¹, km·s⁻¹ | tasa de separación de modelo | hay distancia, `H(z)` o régimen declarado | se toma como velocidad local universal | `R_Ξ^vrec` mide defecto de régimen |
| Profundidad observacional | unidad del canal | unidad instrumental o de catálogo | sensibilidad, ventana, selección, ruido | hay instrumento, ventana y población | se equipara a distancia única | `R_Ξ^Pobs` mide sesgo de observación |
| Retorno luminoso | combinación de `UFE`, `UE_MFC`, energía y señal | flujo, espectro, intensidad, distancia derivada | señal emitida-recibida | hay emisor, medio, recepción y transductor | se emplea como objeto completo | `R_Ξ^Lret` mide medio, atenuación, lente o firma |

### Gravedad, `G`, `Λ` y régimen cosmológico

(Véase *Campo y energía, génesis de la masa y definición física de la gravedad: gravitación universal, constante cosmológica y dominio observable*.) El dominio separa gravitación local y constante cosmológica. `G` retorna la intensidad de la relación fuente-respuesta entre persistencias materiales bajo régimen local o relativista; `Λ` retorna la curvatura efectiva de escala cosmológica del dominio observable. No se sustituyen: `G` se vincula con masa, separación y respuesta; `Λ`, con escala, `H_0`, `Ω_Λ`, distancias de modelo y retorno observacional. Las formas de referencia son `Λ_SV,puro = 3/(c²T_obs²)`, `Λ_obs[B] = 3Ω_Λ[B]H_0[B]²/c²` y `Λ_SV,ret[B] = (Λ_obs[B], B, D_cos, UFE⁻², R_Λ, Ret_Λ, Tr_Λ)`.

| Magnitud | Unidad nativa | Retorno externo | Dominio | Usar cuando | No usar cuando | Residual raigal |
|---|---|---|---|---|---|---|
| `G` | `UFE³·UFM⁻¹·UE_MFC⁻²` | m³·kg⁻¹·s⁻² | gravitación local o relativista | hay masa persistente, separación y régimen | se emplea como explicación cosmológica total | `R_Ξ^G` mide defecto de fuente, régimen o distancia |
| Fuerza gravitatoria local | `UFM·UFE·UE_MFC⁻²` | N | retorno local entre masas | hay régimen débil y separación homogénea | se aplica a `Ω_obs` como dos cuerpos | `R_Ξ^Fg` mide extrapolación local |
| Campo gravitatorio local | `UFE·UE_MFC⁻²` | m·s⁻² | respuesta local de dominio | hay fuente y punto de lectura | se emplea como curvatura cosmológica | `R_Ξ^g` mide frontera o fuente |
| `Λ` | `UFE⁻²` | m⁻² | dominio cosmológico observable | hay escala, `H_0`, `Ω_Λ`, repertorio y retorno | se lee como fuerza local, calor o sustancia | `R_Ξ^Λ` mide mezcla de plano o repertorio |
| Densidad crítica | `UFM·UFE⁻³` | kg·m⁻³ | modelo cosmológico | hay `H_0` y régimen declarado | se emplea como materia concreta sin dominio | `R_Ξ^ρcrit` mide modelo o cierre de repertorio |
| Parámetros `Ω_i` | adimensional | 1 | composición de modelo | hay modelo y suma declarada | se tratan como sustancias directas | `R_Ξ^Ω` mide interpretación indebida |
| `H_0`, `H(z)` | `UE_MFC⁻¹` | s⁻¹, km·s⁻¹·Mpc⁻¹ | expansión de modelo | hay calibración o repertorio cosmológico | se convierten en causa última | `R_Ξ^H` mide tensión o mezcla de calibración |
| Energía oscura | forma de retorno de `Λ` o modelo declarado | unidad según modelo | denominación efectiva | hay ecuación, unidad, residual y retorno | se trata como sustancia material ordinaria | `R_Ξ^DE` mide verbalización sin transductor |

### Dominio-universo, autogobierno y comunicación estructural

(Véanse *Autogobierno topológico y comunicación estructural de observables en el Universo físico realizado* y *Potencial de un suceso: comunicación estructural en el Universo físico realizado, equipotencialidad, diferencia polar y métrica*.) El universo físico realizado comparece como dominio de observables tipados, no como organismo, agencia, conciencia ni totalidad absoluta. La comunicación estructural entre observables no es diálogo ni transmisión al unísono: es consolidación de canal, diccionario estructural, residual, traza y retorno. El potencial local de un suceso no se convierte en topología global del dominio, ni la magnitud global del comparador sustituye al suceso. La ley de tránsito por dominios se recibe como `T_D^SV(D_i, D_j; x) = 0 ⇔ R_D^SV(D_i, D_j; x) = 0`; la admisión de observable como `𝓒★ObsU(x, D_cos) ∈ {0, 1, U}`; los transductores como la especialización `𝓖★TrU(D_cos) = {𝔛_Ξ^t, 𝔛_Ξ^L, 𝔛_Ξ^M, 𝔛_Ξ^E, 𝔛_Ξ^Π, 𝔛_Ξ^Λ, 𝔛_Ξ^Tr, 𝔛_Ξ^Cl, …}`; y la consolidación como `Diag_AB^⊥ = 0`, satisfecha con canal, diccionario estructural, residual, retorno y traza.

| Capa | Forma | Función cosmológica | Riesgo bloqueado |
|---|---|---|---|
| Potencial de suceso | `P_D(e)` | separación polar local de un suceso admisible | convertir el potencial en energía, voltaje o curvatura por definición |
| Comparador global | `Φ(τ)` | lectura global del desequilibrio del dominio realizado | confundir el plano local y el global |
| Tránsito por dominios | `T_D^SV` | paso entre señal, distancia, edad, masa, campo y retorno | trasladar magnitudes sin residual |
| Gobierno de observables | `𝓒★ObsU` | admisión, rechazo o `U` de observables | cierre favorable por el nombre del objeto |
| Transductores | `𝓖★TrU(D_cos)` | retorno especializado de edad, distancia, señal, campo y clausura | emplear la unidad externa como fundamento |
| Comunicación estructural | `Diag_AB^⊥` | canal entre familias de observables | leer la comunicación como agencia o intención |
| Predominancia | compatible o lesiva | régimen de captura, desvío o gobierno local | convertir la asimetría en propósito |
| `U` | no cierre honesto | conserva la falta de retorno suficiente | resolver por plausibilidad |

### Agujeros negros y clausura interna de régimen

(Véase *El agujero negro como cierre interno sin resto exterior formulable*.) El agujero negro entra en cosmología como objeto de frontera extrema, no como modelo general del universo observable. Su lectura raigal se limita a régimen de horizonte, no transmisión exterior, conservación de efectos externos, saturación interior y cierre postfrontera. La marca `M_N2-SV` no se identifica con `U`: `U` conserva un no cierre suficiente, mientras que `M_N2-SV` designa un cierre interno sin resto exterior formulable cuando el régimen ha resuelto sus condiciones. La recepción se expresa como `BH_Ξ(Γ_BH) = 0`, satisfecha con horizonte, no transmisión exterior, fibra luminosa preservada sin salida, saturación interior, postfrontera `M_N2-SV` y residual nulo.

| Elemento BH | Unidad o forma nativa | Retorno externo | Uso cosmológico | No usar cuando | Residual raigal |
|---|---|---|---|---|---|
| Horizonte | `UFE` y frontera de dominio | radio, superficie, horizonte de evento | declarar frontera de no salida | se toma como frontera de la totalidad | `R_Ξ^BH,H` mide defecto de frontera |
| No transmisión luminosa | señal y canal | ausencia de retorno luminoso interior | distinguir interior y exterior | se confunde con inexistencia de contenido | `R_Ξ^BH,L` mide canal no resuelto |
| Efectos externos de campo | `UFM`, `UFE`, `UE_MFC` y derivados | masa, curvatura, lente, ondas | conservar el retorno exterior | se exige acceso interior | `R_Ξ^BH,ext` mide correspondencia externa |
| Saturación interior | estado de régimen | no retorno directo | clasificar el interior postfrontera | se lee como ignorancia `U` | `R_Ξ^BH,int` mide cierre de saturación |
| `M_N2-SV` | resultado de frontera | cierre interno sin resto exterior formulable | cerrar la postfrontera | se trata como `U` o como NADA pura | `R_Ξ^MN2` mide identificación indebida |
| Clausura de instancia | traza clausurada | rastro externo o efecto conservado | declarar cierre local de observable | se extiende a cierre de la totalidad | `R_Ξ^Clcos` mide extrapolación |

### Criterio de admisibilidad del dominio

La admisión cosmológica exige que se satisfaga, sin contradicción material, el criterio

`Cosmo_Ξ admisible ⇔ D_cos declarado ∧ observable tipado ∧ magnitud cosmológica propia ∧ unidad nativa ∧ unidad externa ∧ modelo o transductor ∧ frontera ∧ señal o retorno ∧ residual ∧ traza ∧ conservación de U ∧ no identificación de Ω_obs con la totalidad absoluta`.

Se rechaza la lectura si se atribuye edad física a la totalidad absoluta; si se confunde `Ω_obs` con TODO o NADA; si se emplea `z` como distancia directa; si se igualan `D_L`, `D_A`, `D_C` y `D_P` sin transductor; si se usa `G` como explicación total de la cosmología o `Λ` como fuerza local; si se declara la energía oscura como sustancia sin unidad, ecuación, residual y retorno; o si se toma el agujero negro como modelo de la totalidad o `M_N2-SV` como `U`. Si el objeto no posee identidad, firma, dominio o retorno suficiente, la salida permanece en `U`.

La reserva técnica es doble. Primera: la lectura admite la referencia de edad `A_Ωobs` y su retorno en `UE_MFC`, pero no declara por ello una edad de la totalidad absoluta ni un destino universal. Segunda: las magnitudes externas de la cosmología contemporánea entran como retornos de referencia, no como fundamentos internos; `ΛCDM`, `CMB`, `BAO`, supernovas, galaxias profundas, lentes, horizontes, `H_0`, `Ω_Λ`, `w ≈ −1`, `D_L`, `D_A`, `D_C` y `z` conservan valor de contraste cuando su dominio se resuelve, sin sustituir la matriz raigal ni el residual.

El criterio cosmológico conserva su plano propio: el raigal puede sostener el tránsito entre edad relativa, distancia, señal, gravedad, constante cosmológica, observables y clausura sin convertirse en universo, tiempo, distancia, luz, curvatura, energía oscura ni horizonte. Las magnitudes vuelven a unidades externas; la referencia nativa conserva continuidad por `UR_Ξ^X(D_cos)` y por el residual correspondiente.

## II.4. FÃ­sica y quÃ­mica: materia, luz, campo, elementos y transiciÃ³n quÃ­mica

F­sica y quÃ­mica reciben el nÃºcleo de constituciÃ³n material que no debe duplicarse en los dominios vecinos (Lloret Egea, 2026a, 2026o, 2026p, 2026q, 2026r, 2026s). La termodinÃ¡mica conserva calor, trabajo, temperatura, entalpÃ­a y rÃ©gimen tÃ©rmico; la electricidad y el campo magnÃ©tico conservan carga, corriente, campo, frontera electromagnÃ©tica y propagaciÃ³n; la cosmologÃ­a conserva universo observable, edad relativa, distancia, gravitaciÃ³n, `G`, `Î›` y clausura de rÃ©gimen. FÃ­sica y quÃ­mica, en cambio, gobiernan la lectura de materia, luz, campo, energÃ­a de dominio, transiciÃ³n prequÃ­mica y quÃ­mica, persistencia atÃ³mica, elementos y materiales.

**El dominio fÃ­sico-quÃ­mico.** Se formaliza como `D_fq = (Î©_pre, Îž_fq, Î¦_L, ð”‰_SV, ð•´_F, ð•‹_chem, Î©_443, R_fq, Ret_fq, Tr_fq)`: dominio preternario declarado, sucesos generadores y protocampos, objeto luminoso, cierre operatorio de los sectores fÃ­sico-formales, frontera angular cuÃ¡ntica, transiciÃ³n quÃ­mica, catÃ¡logo estructural, residual, retorno y traza. La admisiÃ³n `FQ_Îž(D_fq) = 0` se satisface cuando concurren `Î©_pre`, `Îž_fq`, una magnitud fÃ­sica o quÃ­mica declarada, unidad nativa, unidad externa cuando proceda, transductor, frontera, canal, residual, retorno y traza, sin contradicciÃ³n. Si el dominio reclama una magnitud ya desarrollada en termodinÃ¡mica, electricidad o cosmologÃ­a, no la reescribe: la invoca por trÃ¡nsito declarado. La coincidencia de unidad no autoriza identidad de dominio.

> **Caso de aplicaciÃ³n.** En un reactor industrial se disocia el gas cloro (Clâ‚‚). La energÃ­a de enlace de `1 mol` de Clâ‚‚ es `E_enlace = 242 kJ/mol`. Para iniciar la transiciÃ³n se irradia con luz monocromÃ¡tica, y cada fotÃ³n es absorbido por una molÃ©cula para romper su enlace. La lectura ordinaria resuelve dos magnitudes. La energÃ­a por molÃ©cula, con `N_A = 6.022 Ã— 10Â²Â³ molÃ©culas/mol`, es `E_molÃ©cula = E_enlace / N_A = 242000 / (6.022 Ã— 10Â²Â³) = 4.0186 Ã— 10â»Â¹â¹ J`. La longitud de onda mÃ¡xima de la luz, con la relaciÃ³n `E = hÂ·c / Î»` y `hÂ·c = 1.986 Ã— 10â»Â²âµ JÂ·m`, es `Î» = hÂ·c / E_molÃ©cula = (1.986 Ã— 10â»Â²âµ) / (4.0186 Ã— 10â»Â¹â¹) = 4.942 Ã— 10â»â· m = 494.2 nm`. Cualquier luz con `Î» â‰¤ 494.2 nm` (rango verde-azul) puede provocar la disociaciÃ³n. Sobre este resultado conocido se construye la lectura raigal. El rÃ©gimen se declara como transiciÃ³n quÃ­mica `ð•‹_chem` (ruptura de enlace), proceso fotoquÃ­mico con especie y masa tipadas y absorciÃ³n idealizada de un fotÃ³n por molÃ©cula; sin proceso, especie y canal declarados, la salida correcta serÃ­a `U`.

**RecepciÃ³n del dominio.** La sustancia se recibe como `Sub_Îž = Clâ‚‚` tipada (`UFCE`, `1 mol`), con el cloro como elemento reconocido `E_k` de nÃºmero `k = 17 â‰¤ 118` â€”subdominio empÃ­rico ordinario, no candidato estructural en `U`â€”. La energÃ­a de enlace entra como proyecciÃ³n energÃ©tica del dominio fÃ­sico-quÃ­mico (`UFMÂ·UFEÂ²Â·UE_MFCâ»Â²`, `242 kJ/mol`), no como calor. La fuente entra como objeto luminoso `Î¦_L`, con la relaciÃ³n nativa `E = Î½Â·h_SV`, invocada por trÃ¡nsito de dominio declarado como interacciÃ³n luz-materia, no como campo `E/B/D/H` de electricidad. Las constantes `N_A` y `hÂ·c` son anclas de referencia con su residual propio.

**EnergÃ­a por molÃ©cula (proyecciÃ³n de cantidad por `ð”›_Îž^N`).** La energÃ­a tabulada es por mol; el paso a una sola transiciÃ³n molecular es una proyecciÃ³n de cantidad, no un cambio de naturaleza de la energÃ­a. El cociente `E_enlace / N_A` interviene como operaciÃ³n de retorno â€”con denominador, unidad y sentido declaradosâ€”, no como operaciÃ³n nativa del raigal. Retorno: `V_Îž^E â†’ 4.0186 Ã— 10â»Â¹â¹ J`. Esa es la energÃ­a que rompe el campo de enlace de una molÃ©cula. El residual `R_Îž^{sub}` se reduce al de la constante `N_A`. La energÃ­a retorna por la proyecciÃ³n energÃ©tica del dominio fÃ­sico-quÃ­mico y no se lee como calor: romper un enlace no es necesariamente un trÃ¡nsito tÃ©rmico, sino una reorganizaciÃ³n de configuraciÃ³n. La regla de no duplicaciÃ³n bloquea aquÃ­ la identificaciÃ³n entre energÃ­a de enlace y calor.

**Longitud de onda umbral (objeto luminoso `Î¦_L`).** La luz entra como `Î¦_L` con la relaciÃ³n nativa `E = Î½Â·h_SV`, que retorna externamente como `E = hÂ·c / Î»`. Despejada la longitud de onda que transporta exactamente la energÃ­a de enlace por fotÃ³n, `Î» â†’ 494.2 nm`. El valor es un umbral de frontera, no una igualdad rÃ­gida: cualquier `Î» â‰¤ 494.2 nm` transporta `E â‰¥ E_enlace` por fotÃ³n y puede disparar la transiciÃ³n (rango cian/verde-azul, en torno a `2.51 eV` por fotÃ³n). La frontera fotoquÃ­mica se lee como `Î» â‰¤ Î»_mÃ¡x â‡” E_fotÃ³n â‰¥ E_enlace`. El canal Â«un fotÃ³n por molÃ©culaÂ» resuelve la correspondencia `Î¦_L â†” entidad`; sin ese canal, la salida serÃ­a `U`.

**TransiciÃ³n quÃ­mica y elemento producto (`ð•‹_chem`, `E_k`).** La disociaciÃ³n es transiciÃ³n quÃ­mica `Q_Îž(Î“)` del enlace Clâ€“Cl hacia cloro atÃ³mico. El producto es elemento reconocido (`k = 17 â‰¤ 118`): retorno empÃ­rico ordinario, no candidato estructural en `U`. La transiciÃ³n se admite porque hay especie tipada, proceso de fotodisociaciÃ³n, energÃ­a de enlace de referencia y canal luminoso declarado.

**Admisibilidad y dictamen del caso.** El dominio se admite cuando el criterio `FQ_Îž` se satisface sin contradicciÃ³n material: declarado `D_fq`, tipada la sustancia (Clâ‚‚), declarada la transiciÃ³n `ð•‹_chem`, presentes la magnitud fÃ­sico-quÃ­mica propia, las unidades nativa y externa, los transductores (`ð”›_Îž^N`, `Î¦_L`, `ð”›_Îž^Î»`), la frontera de umbral, el canal, el residual, el retorno y la traza, sin identificar la energÃ­a de enlace con calor ni la luz con campo electromagnÃ©tico. En el caso, todas las condiciones se satisfacen: **dictamen `= 0`**. Los residuales materiales son de referencia â€”el redondeo de `N_A` y de `hÂ·c`â€” y de idealizaciÃ³n del proceso fotoquÃ­mico â€”absorciÃ³n exacta de un fotÃ³n por molÃ©cula, sin reflexiÃ³n, dispersiÃ³n, relajaciÃ³n no radiativa ni pÃ©rdidas de medioâ€”, conservados como `R_Îž^Luz`; cualquier eficiencia real menor reabrirÃ­a el balance, que deberÃ­a retornarse y no absorberse.

### Regla de no duplicaciÃ³n entre dominios

| Materia tratada | Dominio que conserva el desarrollo propio | Uso permitido en FÃ­sica y quÃ­mica | Riesgo bloqueado |
|---|---|---|---|
| Calor, trabajo, entropÃ­a, temperatura, entalpÃ­a, capacidad tÃ©rmica | TermodinÃ¡mica | condiciÃ³n de proceso, fase, reacciÃ³n o material cuando se declare trÃ¡nsito | duplicar el dominio tÃ©rmico dentro del quÃ­mico |
| Carga, corriente, campo elÃ©ctrico, campo magnÃ©tico, propagaciÃ³n electromagnÃ©tica | Electricidad y campo magnÃ©tico | condiciÃ³n de interacciÃ³n, enlace, espectro, polarizaciÃ³n o transporte | absorber el dominio electromagnÃ©tico en quÃ­mica general |
| Edad del universo observable, distancias cosmolÃ³gicas, `G`, `Î›`, agujeros negros | CosmologÃ­a | condiciÃ³n externa de escala, gravedad, radiaciÃ³n o retorno observacional | convertir fÃ­sica y quÃ­mica en cosmologÃ­a resumida |
| Masa, energÃ­a, luz, materia, campo, transiciÃ³n quÃ­mica, elementos, materiales | FÃ­sica y quÃ­mica | nÃºcleo propio del dominio fÃ­sico-quÃ­mico | confundir materia y quÃ­mica con la suma de subdominios vecinos |
| BiologÃ­a, inmunologÃ­a y genÃ©tica | dominio especializado propio | condiciÃ³n molecular, compositiva o material cuando el caso todavÃ­a pertenece a fÃ­sica-quÃ­mica | adelantar conclusiones biolÃ³gicas sin frontera viva, linaje, canal, residual y retorno |

### NÃºcleo fÃ­sico-quÃ­mico comÃºn

(VÃ©ase *TeorÃ­a general de sucesos generadores y de los protocampos unificados en el Sistema Vectorial SV*.) Se construye por dependencia formal, no por acumulaciÃ³n de formulaciones previas. La TeorÃ­a del TODO y de la NADA aporta la lectura de cierre â€”restricciÃ³n superior de nulidad conjunta, frontera `(Î¼,Î») = (0,0)`, alfabeto `Î£ = {0,1,U}` y prohibiciÃ³n de cierre favorable sin residualâ€”. La teorÃ­a de sucesos generadores y protocampos aporta el trÃ¡nsito desde `Î©_pre` hacia los sectores fÃ­sico-formales. La fÃ³rmula de campo unificado aporta la proyecciÃ³n exterior `ð“ = Ï‰âŠ•A` y `ð“•_ð“ = dð“ + ð“âˆ§ð“`, sin convertir geometrÃ­a, espacio de Hilbert o probabilidad en base rectora. La teorÃ­a de la luz aporta el vacÃ­o como potencialidad preternaria no activada, la energÃ­a como variaciÃ³n admisible y la relaciÃ³n `E = Î½Â·h_SV`. Bellâ€“Tsirelson aporta el rÃ©gimen angular acoplado, `Ï‡_c`, `C_SV(Î´) = âˆ’cosÎ´` y la cota `2âˆš2`. El documento de elementos y materiales aporta el trÃ¡nsito prequÃ­mico y quÃ­mico: `720` configuraciones candidatas, `675` admisibles, `443` elementos estructurales, los primeros `118` como subdominio reconocido y `k = 119â€¦443` como candidatos estructurales en `U`.

| Fuente interna | Aporte al dominio | Uso en el dominio | Lo que no se traslada |
|---|---|---|---|
| TeorÃ­a del TODO y de la NADA | `Î£ = {0,1,U}`, frontera `(Î¼,Î»)=(0,0)`, verificaciÃ³n fuerte, cadena de cierre | restricciÃ³n superior de cierre fÃ­sico-quÃ­mico | no convierte el dominio en totalidad absoluta |
| Sucesos generadores y protocampos | `Î©_pre`, pares `(Î±,Î²)`, sectores coexistentes, `ð”‰_SV` | raÃ­z de campo, materia y transiciÃ³n fÃ­sico-quÃ­mica | no hace de los primitivos metrolÃ³gicos campos generadores |
| Campo unificado y doble proyecciÃ³n | `ð“ = Ï‰âŠ•A`, `ð“•_ð“ = dð“ + ð“âˆ§ð“`, clase `ð•´_F` | proyecciÃ³n fÃ­sica exterior de conexiÃ³n, curvatura y rÃ©gimen angular | no sustituye el dominio por geometrÃ­a |
| Luz | vacÃ­o no activado, energÃ­a como variaciÃ³n, `h_SV`, `E = Î½Â·h_SV` | luz, espectro, radiaciÃ³n, transporte energÃ©tico y vÃ­nculo con materia | no reduce la luz a onda, partÃ­cula o campo aislado |
| Bellâ€“Tsirelson | `Ï‡_c`, `Râ‚€`, `Râ‚`, `Râ‚‚`, `C_SV(Î´) = âˆ’cosÎ´`, `2âˆš2` | rÃ©gimen angular acoplado de frontera fÃ­sica | no introduce la probabilidad como criterio de verdad |
| Elementos y materiales | `720 â†’ 675 â†’ 443`, criterios prequÃ­micos y quÃ­micos, `Î©_443` | transiciÃ³n quÃ­mica, elementos, materiales y candidatos | no declara existencia empÃ­rica de los candidatos en `U` |

### Matriz especializada de retorno fÃ­sico-quÃ­mico

El caso activa cuatro proyecciones â€”sustancia, energÃ­a, luz y transiciÃ³nâ€”; el inventario completo del dominio es el siguiente.

| ProyecciÃ³n fÃ­sico-quÃ­mica | Forma interna | Unidad nativa o retorno | Retorno externo | Usar cuando | No usar cuando | Residual raigal |
|---|---|---|---|---|---|---|
| Soporte preternario | `Î©_pre` | sin unidad fÃ­sica directa | sin SI directo | se declara soporte previo a la activaciÃ³n | se pretende medir como espacio fÃ­sico | `R_Îž^{Î©}` conserva ausencia de activaciÃ³n o trÃ¡nsito insuficiente |
| Suceso generador | `Îµ_g` o transiciÃ³n declarada | unidad de suceso de dominio | registro, reacciÃ³n, transiciÃ³n, emisiÃ³n | hay apertura de estructura con traza | se emplea como instante temporal | `R_Îž^{Îµ}` mide falta de soporte, traza o retorno |
| Protocampo polar | `(Î±,Î²)` | par estructural | sin SI directo salvo proyecciÃ³n | se estudia apertura o cierre antes del campo fÃ­sico | se confunde con carga, masa o espÃ­n | `R_Îž^{Î±Î²}` mide defecto de lectura polar |
| Campo fÃ­sico proyectado | `ð”‰_SV` o `ð“•_ð“` | depende del sector | curvatura, campo, acciÃ³n, energÃ­a, carga, fuerza | existe proyecciÃ³n legÃ­tima con dominio y residual | se emplea como campo universal indiferenciado | `R_Îž^{campo}` mide sector no resuelto |
| Luz y radiaciÃ³n | `Î¦_L`, `E = Î½Â·h_SV` | `UFMÂ·UFEÂ²Â·UE_MFCâ»Â²` y `UE_MFCâ»Â¹` | J, Hz, m, espectro | hay rÃ©gimen luminoso o espectral declarado | se reduce a onda o partÃ­cula aislada | `R_Îž^Luz` mide proyecciÃ³n luminosa incompleta |
| CorrelaciÃ³n angular | `C_SV(Î´) = âˆ’cosÎ´` | adimensional | correlaciÃ³n, `S`, Ã¡ngulo | hay aparato angular acoplado y bases declaradas | se emplea como probabilidad o ajuste estadÃ­stico | `R_Îž^{ang}` mide acoplamiento o base no declarada |
| TransiciÃ³n prequÃ­mica | `PreQ_Îž(Î“)` | unidad de trayectoria o clase | configuraciÃ³n candidata | hay trayectoria, acoplamiento y residual | se declara elemento sin transiciÃ³n quÃ­mica | `R_Îž^{preQ}` mide incumplimiento de admisiÃ³n prequÃ­mica |
| TransiciÃ³n quÃ­mica | `Q_Îž(Î“)` | unidad de clase elemental | elemento, isÃ³topo, material | el cierre posicional, el acoplamiento y la compatibilidad se resuelven | se afirma detecciÃ³n empÃ­rica sin contraste | `R_Îž^Q` mide falta de cierre quÃ­mico |
| Elemento reconocido | `E_k`, `k â‰¤ 118` | `UFCE`, `UFM`, propiedades derivadas | mol, kg, u, densidad, configuraciÃ³n | el elemento tiene retorno externo reconocido | se mezcla con candidatos no detectados | `R_Îž^{elem}` mide error de identidad o propiedad |
| Candidato estructural | `E_k`, `119 â‰¤ k â‰¤ 443` | clase estructural en `Î©_443` | sin existencia empÃ­rica declarada | se trabaja como candidato en `U` | se publica como elemento detectado | `R_Îž^{Uelem}` conserva la indeterminaciÃ³n honesta |
| Material o aleaciÃ³n | `Mat_Îž(E_i, E_j, â€¦)` | composiciÃ³n tipada | densidad, mÃ³dulo, punto, uso | hay composiciÃ³n, frontera y propiedades declaradas | se trasladan usos mÃ©dicos sin repertorio propio | `R_Îž^{mat}` mide composiciÃ³n o propiedad no contrastada |
| Sustancia quÃ­mica | `Sub_Îž` | `UFCE`, `UFM`, `UFEÂ³`, derivados | mol, kg, mÂ³, concentraciÃ³n | entidad, fase y cantidad estÃ¡n tipadas | se confunde la sustancia con el raigal | `R_Îž^{sub}` mide fase, entidad o cantidad no resueltas |

### TrÃ¡nsito prequÃ­mico y transiciÃ³n quÃ­mica

La admisiÃ³n prequÃ­mica se expresa como restricciÃ³n de trayectoria: `PreQ_Îž(Î“) = 0`, satisfecha con `ð”“_min(Î“,n) > 0`, `Î´(âˆ‚Î©_pre) < Î›_pre`, `Ï‡_c > 0`, `ð”‡_Î“g_AÂ·ð”‡_Î“g_B â‰¤ 0`, `C_SV(Î´) = âˆ’cosÎ´` y `ð”˜_unif = 0`. Esta condiciÃ³n selecciona las configuraciones que pueden aspirar a rÃ©gimen quÃ­mico, y no equivale todavÃ­a a elemento. La transiciÃ³n quÃ­mica aÃ±ade cierre posicional, acoplamiento pleno, densidad de no clausura posicional mÃ¡xima, oposiciÃ³n factual plena y compatibilidad con la ecuaciÃ³n rectora: `Q_Îž(Î“) = 0`, satisfecha con `Ï†(S_n) = 0`, `Ï‡_c = 1`, `Ï_pos = 1`, `ð”‡_Î“g_AÂ·ð”‡_Î“g_B = âˆ’1` y `ð“”â˜…_TODO,SV(Î“_U; Ï„) = 0`. La ruta cuantitativa del documento de origen se recibe como repertorio estructural. (VÃ©ase *AnÃ¡lisis preliminar de elementos quÃ­micos, materiales y aleaciones de nueva generaciÃ³n para usos mÃ©dicos y cientÃ­ficos*.)

| Fase | Cantidad | Lectura en el dominio | Resultado |
|---|---:|---|---|
| Configuraciones candidatas | `720` | variaciÃ³n sistemÃ¡tica por familias tipolÃ³gicas | dominio de bÃºsqueda |
| Configuraciones prequÃ­micas admitidas | `675` | superan las restricciones prequÃ­micas | no son todavÃ­a elementos |
| Elementos estructurales | `443` | superan la transiciÃ³n quÃ­mica | catÃ¡logo `Î©_443` |
| Subdominio reconocido | `118` | elementos detectados externamente | retorno empÃ­rico ordinario |
| Candidatos estructurales | `325` | `k = 119â€¦443` | `U` hasta contraste externo |

### Luz, campo y frontera angular dentro de FÃ­sica y quÃ­mica

(VÃ©ase *TeorÃ­a general factual de la luz en el Sistema Vectorial SV*.) La luz entra en FÃ­sica y quÃ­mica porque permite tratar energÃ­a, espectro, radiaciÃ³n, interacciÃ³n luz-materia, emisiÃ³n, absorciÃ³n, color y transporte. No desplaza el dominio elÃ©ctrico-magnÃ©tico, donde se conserva el campo local `E/B/D/H`; aquÃ­ la luz es objeto de retorno fÃ­sico-quÃ­mico, y cada uso declara magnitud, unidad y residual. El campo unificado entra como capa de proyecciÃ³n fÃ­sica, no como sustituto de la quÃ­mica: `ð“ = Ï‰âŠ•A` y `ð“•_ð“ = dð“ + ð“âˆ§ð“` permiten leer conexiÃ³n, curvatura y acciÃ³n en el plano exterior, mientras `ð”‰_SV` conserva la lectura interna por sectores. La correlaciÃ³n angular `C_SV(Î´) = âˆ’cosÎ´` no se emplea para resolver una reacciÃ³n quÃ­mica ordinaria; solo cuando el rÃ©gimen exige correlaciÃ³n angular de frontera, con `Ï‡_c`, rÃ©gimen `Râ‚€/Râ‚/Râ‚‚`, bases, correlador y retorno declarados.

| Uso fÃ­sico-quÃ­mico | Entrada | Retorno externo | RestricciÃ³n |
|---|---|---|---|
| Espectro de sustancia | `Î¦_L` + entidad quÃ­mica | frecuencia, longitud de onda, energÃ­a | no reducir la sustancia al espectro |
| Enlace y transiciÃ³n electrÃ³nica | campo proyectado + configuraciÃ³n | energÃ­a, nivel, seÃ±al | no importar probabilidad como cierre |
| FotoquÃ­mica | luz + especie + proceso | energÃ­a absorbida, producto, rendimiento | proceso y masa deben estar declarados |
| Material Ã³ptico | composiciÃ³n + respuesta luminosa | Ã­ndice, absorciÃ³n, transmisiÃ³n | la respuesta no equivale a identidad material completa |
| CorrelaciÃ³n angular | `Ï‡_c`, `C_SV(Î´)` | correlaciÃ³n, `S`, Ã¡ngulo | no usar fuera de aparato angular declarado |
| Campo-materia | `ð”‰_SV` o `ð“•_ð“` + frontera | acciÃ³n, energÃ­a, fuerza, carga o curvatura | no confundir la proyecciÃ³n exterior con la raÃ­z metrolÃ³gica |

### PatrÃ³n `P_Hâ‚‚O` en el dominio fÃ­sico-quÃ­mico

En FÃ­sica y quÃ­mica, `P_Hâ‚‚O` no se usa como referencia tÃ©rmica ni elÃ©ctrica, sino como sustancia molecular tipada: `1 mol de Hâ‚‚O lÃ­quida`, con entidad, composiciÃ³n `2H + 1O`, masa, densidad, volumen, fase, temperatura y presiÃ³n declaradas. La proyecciÃ³n quÃ­mica queda limitada a lo que el patrÃ³n declara â€”cantidad de entidad, composiciÃ³n, masa, volumen, concentraciÃ³n si se introduce disoluciÃ³n y fase si se declara rÃ©gimenâ€”. No devuelve por sÃ­ mismo calor, trabajo, entropÃ­a, corriente, campo, edad cosmolÃ³gica ni reactividad; cualquier ampliaciÃ³n exige trÃ¡nsito de dominio.

| Lectura sobre `P_Hâ‚‚O` | Resultado admisible | Dominio que gobierna | Salida si falta proceso |
|---|---|---|---|
| Cantidad de molÃ©culas | `1 UFCE` de Hâ‚‚O | FÃ­sica y quÃ­mica | `0` si la entidad estÃ¡ tipada |
| ComposiciÃ³n | `2 UFCE H + 1 UFCE O` por molÃ©cula | FÃ­sica y quÃ­mica | `0` bajo identidad molecular |
| Masa | `0,01801528 kg` | matriz general y FÃ­sica y quÃ­mica | `0` si la masa se recibe y devuelve |
| Volumen | `1,8068636684Ã—10â»âµ mÂ³` | matriz general y FÃ­sica y quÃ­mica | `0` si fase y densidad se resuelven |
| Calor de proceso | no declarado | TermodinÃ¡mica | `U` |
| Corriente o campo | no declarado | Electricidad y campo magnÃ©tico | `U` |
| ReacciÃ³n quÃ­mica | no declarada | FÃ­sica y quÃ­mica | `U` |
| Uso biolÃ³gico o clÃ­nico | no declarado | dominio posterior | `U` |

### Criterio de admisibilidad del dominio

El dominio fÃ­sico-quÃ­mico se admite cuando el objeto tratado no se limita a un nombre de disciplina, sino que declara secuencia material: soporte, transiciÃ³n, magnitud, unidad, frontera, residual y retorno. Su salida no puede apoyarse en el parecido de lenguaje entre fÃ­sica y quÃ­mica. Una energÃ­a de enlace no es automÃ¡ticamente calor; una configuraciÃ³n prequÃ­mica no es automÃ¡ticamente elemento; un candidato estructural no es automÃ¡ticamente elemento detectado; una seÃ±al espectral no es automÃ¡ticamente sustancia; una correlaciÃ³n angular no es automÃ¡ticamente probabilidad; y una geometrÃ­a exterior no es automÃ¡ticamente campo fÃ­sico completo. Los tres dictÃ¡menes se fijan asÃ­:

`FQ_Îž(D_fq) = 0 â‡” D_fq âˆ§ PreQ_Îž âˆ§ Q_Îž si procede âˆ§ unidad nativa âˆ§ unidad externa âˆ§ transductor âˆ§ frontera âˆ§ canal âˆ§ R_fq = 0 âˆ§ Ret_fq âˆ§ Tr_fq`.

`FQ_Îž(D_fq) = U â‡” falta contraste externo, proceso, unidad, fase, entidad o trÃ¡nsito, sin contradicciÃ³n material`.

`FQ_Îž(D_fq) = 1 â‡” se identifica una proyecciÃ³n con la totalidad del dominio, se declara existencia empÃ­rica sin retorno, se importa probabilidad como verdad, se convierte un candidato en detecciÃ³n o se traslada una magnitud entre dominios sin transductor`.

