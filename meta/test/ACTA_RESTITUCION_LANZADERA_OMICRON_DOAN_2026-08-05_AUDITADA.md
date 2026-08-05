# Acta de restitución documental y matemática — versión auditada
## Recta-Ómicron / Lanzadera Ómicron — DOAN-Ω16

**Fecha de auditoría:** 5 de agosto de 2026  
**Dirección científica y autoría:** Juan Antonio Lloret Egea  
**Unidad auditora:** Watson — Publicaciones  
**Documento de base:** `ACTA_RESTITUCION_LANZADERA_OMICRON_DOAN_2026-08-05.md`  
**Fuente primaria recuperada:** conversación compartida «Leer documento»  
**Identificador:** `6a2f01ce-fc10-83ed-8747-9537817dbdda`  
**Fecha de la conversación:** 14 de junio de 2026  

---

# 1. Dictamen ejecutivo

La restitución **supera la auditoría aritmética y documental** en su objeto principal:

\[
\boxed{
\Delta A
\longrightarrow
N_A
\longrightarrow
g_D
\longrightarrow
\nu_{\mathrm{acc}}
\longrightarrow
\sigma_{\Omega16}
\longrightarrow
\lambda_{\mathrm{acc}}
\longrightarrow
\lambda_{\partial}
}
\]

reproduce los valores publicados cuando se respetan los dos niveles de precisión
congelada usados en la cadena histórica:

1. \(N_s(\mathrm{Sol})\) se fija con doce cifras decimales;
2. \(\sigma_{\Omega16}\) se fija con treinta y tres cifras decimales.

La Parte II no inventó \(\lambda_{\mathrm{acc}}\): **heredó una cadena generadora
real cuya demostración quedó fuera del documento final**.

El resultado de auditoría no equivale todavía a validación física ni a novedad
computacional. Quedan pendientes la justificación de los acoplamientos, la
transferencia de escala y la comparación con la literatura.

---

# 2. Entradas y regla media Luna–Sol

Se declaran:

\[
R:=D_{TS}=149\,597\,870\,700\ \mathrm{m},
\]

\[
r:=D_{TL}=384\,400\,000\ \mathrm{m}.
\]

Bajo el modelo auxiliar de órbita lunar circular, distancia Tierra–Sol fija y
fase angular uniforme:

\[
d_{LS}(\theta)
=
\sqrt{R^2+r^2-2Rr\cos\theta}.
\]

La media angular es:

\[
\overline d_{LS}
=
\frac{1}{2\pi}
\int_0^{2\pi}
\sqrt{R^2+r^2-2Rr\cos\theta}\,d\theta,
\]

o, usando la integral elíptica completa de segunda especie con parámetro \(m\),

\[
\overline d_{LS}
=
\frac{2(R+r)}{\pi}
E\!\left(\frac{4Rr}{(R+r)^2}\right).
\]

La evaluación de alta precisión produce:

\[
\overline d_{LS}
=
149\,598\,117\,634.365250679780375539616884243654\ldots\ \mathrm{m}.
\]

Por tanto, el residual no redondeado sería:

\[
N_s^{(\infty)}(\mathrm{Sol})
=
246\,934.365250679780375539616884243654\ldots\ \mathrm{UFE}.
\]

La cadena histórica no usa ese valor completo. Congela:

\[
\boxed{
N_s^{[12]}(\mathrm{Sol})
=
246\,934.365250679780\ \mathrm{UFE}.
}
\]

Esta congelación debe declararse expresamente. No debe escribirse que el valor
de doce decimales sea idéntico al residual de precisión ilimitada sin indicar
truncamiento o redondeo.

## Estatuto epistemológico

- \(D_{TS}\): anclaje externo de contraste y patrón metrológico.
- \(D_{TL}\): anclaje externo de contraste adoptado como distancia lunar media.
- \(\overline d_{LS}\): construcción geométrica auxiliar interna.
- \(N_s(\mathrm{Sol})\): residual interno construido.
- Las cifras externas no fundan la verdad del SV; fijan las entradas declaradas
  de esta instancia de retorno.

---

# 3. Escala Ómicron

Se define:

\[
N_s(\mathrm{Tierra})
=
D_{TS}-D_{TL}
=
149\,213\,470\,700\ \mathrm{UFE}.
\]

Con el valor congelado de \(N_s(\mathrm{Sol})\):

\[
\kappa_P
=
\frac{N_s(\mathrm{Tierra})}{N_s^{[12]}(\mathrm{Sol})}
\]

\[
=
604\,263.6898615683206487433327670029405000\ldots
\]

y:

\[
\kappa_R
=
\frac{R_{\odot}}{R_{\mathrm{Tierra}}+R_{\mathrm{Luna}}}
\]

\[
=
85.79991120319668491934290365546840313748\ldots
\]

La construcción define:

\[
\kappa_{\Omega}
=
\sqrt{\frac{\kappa_P}{\kappa_R}}
\]

\[
=
83.92084149203158065371808654007628131756\ldots
\]

y:

\[
\sigma_{\Omega16}^{(\infty\mid N_s^{[12]})}
=
D_{TL}\kappa_{\Omega}
\]

\[
=
32\,259\,171\,469.5369396032892324660053225384731672667697\ldots
\ \mathrm{UFE}.
\]

La cadena histórica congela:

\[
\boxed{
\sigma_{\Omega16}^{[33]}
=
32\,259\,171\,469.536939603289232466005322538473167
\ \mathrm{UFE}.
}
\]

Este valor coincide exactamente con el cociente reconstruido:

\[
\frac{\lambda_{\mathrm{acc}}}{\nu_{\mathrm{acc}}}
=
\sigma_{\Omega16}^{[33]}.
\]

---

# 4. Acceso nodal

Para el observable retornado:

\[
A_{\Omega_{\mathrm{obs}}}=13\,800\,000\,000\ a_J,
\]

\[
A_{\Omega SS}=4\,568\,000\,000\ a_J,
\]

\[
N_A
=
\frac{A_{\Omega_{\mathrm{obs}}}-A_{\Omega SS}}{1\,a_J}
=
9\,232\,000\,000.
\]

Con:

\[
\chi_{\Omega_{\mathrm{obs}}}=\frac12,
\]

\[
g_{\Omega_{\mathrm{obs}}}
=
\sqrt{\frac{1+\chi_{\Omega_{\mathrm{obs}}}}{2}}
=
\frac{\sqrt3}{2}.
\]

Entonces:

\[
\nu_{\mathrm{acc}}
=
9\,232\,000\,000\frac{\sqrt3}{2}
\]

\[
=
7\,995\,146\,527.7379375869226923123911068458079890515887\ldots
\]

y, usando la escala congelada:

\[
\lambda_{\mathrm{acc}}
=
\sigma_{\Omega16}^{[33]}\nu_{\mathrm{acc}}
\]

\[
=
257\,916\,802\,762\,371\,004\,117.8021159948054130965383279286041549868367802475908620127745896778575090806844476\ldots
\ \mathrm{UFE}.
\]

La cifra publicada queda reproducida.

---

# 5. Frontera

Para:

\[
A_{\mathrm{fin}}(\Omega_{\mathrm{obs}})
=
27\,600\,000\,000\ a_J,
\]

se obtiene:

\[
N_{A,\partial}
=
23\,032\,000\,000.
\]

Manteniendo el mismo factor estructural:

\[
\nu_{\partial}
=
23\,032\,000\,000\frac{\sqrt3}{2}.
\]

Por tanto:

\[
\lambda_{\partial}
=
\sigma_{\Omega16}^{[33]}\nu_{\partial}
\]

\[
=
643\,451\,018\,330\,039\,966\,078.9881212730024127425769896936320296422037177927331817459081834337536989976521011\ldots
\ \mathrm{UFE}.
\]

La relación es exacta:

\[
\kappa_{\partial\leftarrow\mathrm{acc}}^{SV}
=
\frac{23\,032\,000\,000}{9\,232\,000\,000}
=
\frac{2879}{1154},
\]

\[
\lambda_{\partial}
=
\kappa_{\partial\leftarrow\mathrm{acc}}^{SV}
\lambda_{\mathrm{acc}}.
\]

---

# 6. Efecto de las congelaciones de precisión

Debe distinguirse entre tres ramas.

## Rama publicada

Usa:

\[
N_s^{[12]}(\mathrm{Sol})
\quad\text{y}\quad
\sigma_{\Omega16}^{[33]}.
\]

Reproduce exactamente las cifras publicadas de \(\lambda_{\mathrm{acc}}\),
\(\lambda_{\partial}\) y \(t_{\Omega_{\mathrm{obs}}}\).

## Rama con \(N_s^{[12]}\) y \(\sigma\) no truncada

La diferencia respecto de la rama publicada sólo aparece después de las cifras
soportadas por \(\sigma_{\Omega16}^{[33]}\). Es un efecto de presentación.

## Rama integral completa

Usa:

\[
N_s^{(\infty)}(\mathrm{Sol})
=
246\,934.365250679780375539\ldots
\]

y produce:

\[
\sigma_{\Omega16}^{(\infty)}
=
32\,259\,171\,469.5369395787592386711467601283420767\ldots
\]

La diferencia respecto de la escala histórica es:

\[
\Delta\sigma
\approx
2.4529993794858562\times10^{-8}\ \mathrm{UFE}.
\]

Aplicada al acceso:

\[
\Delta\lambda_{\mathrm{acc}}
\approx
196.1208947143966\ \mathrm{UFE}.
\]

Aplicada a la frontera:

\[
\Delta\lambda_{\partial}
\approx
489.2825440925024\ \mathrm{UFE}.
\]

El error relativo es del orden de:

\[
7.6\times10^{-19}.
\]

Es despreciable para la escala global, pero no puede ignorarse en una afirmación
de exactitud decimal ilimitada. La publicación debe escoger y declarar una sola
política:

- **reproducción histórica:** mantener las congelaciones;
- **recomputación canónica:** usar la rama integral completa y actualizar las
  cifras;
- **doble salida:** conservar ambas, distinguiendo valor histórico y valor
  recalculado.

Para un artículo se recomienda la tercera opción.

---

# 7. Auditoría dimensional

La cadena es dimensionalmente compatible:

\[
\kappa_P,\ \kappa_R,\ \kappa_{\Omega},\ N_A,\ g_D,\ \nu
\]

son adimensionales, mientras:

\[
\sigma_{\Omega16},\ \lambda_{\mathrm{acc}},\ \lambda_{\partial}
\]

se expresan en UFE.

La integral Luna–Sol devuelve longitud. Su diferencia con \(D_{TS}\) devuelve
longitud. No hay error dimensional en las operaciones auditadas.

---

# 8. Puntos todavía no cerrados

## 8.1. Puente notacional

La restitución contiene:

\[
d_{\Omega}(\mathrm{Tierra},X)
=
D_{TL}(N_c(X)-2)\kappa_{\Omega}
\]

y, en otro nivel:

\[
\nu_{\mathrm{acc}}
=
N_Ag_D.
\]

Falta consignar en el acta la igualdad, transformación o regla que relaciona:

\[
N_c(X)-2
\quad\text{con}\quad
N_A(D\mid\Omega_{SS})g_D.
\]

No debe suponerse por semejanza. Debe recuperarse de la conversación o declararse
como definición de paso.

## 8.2. Factor \(\chi_D\)

Debe documentarse:

- su definición;
- su dominio;
- su rango;
- por qué vale \(1/2\) para \(\Omega_{\mathrm{obs}}\);
- si el mismo valor gobierna la frontera;
- qué ocurre para otros dominios.

La aritmética de \(g_D\) es correcta, pero su estatuto estructural todavía no está
explicado en esta acta.

## 8.3. Necesidad de la raíz

Los planos:

\[
b-\frac{a}{\sqrt{\kappa_R}}=0,
\qquad
c-\sqrt{\kappa_P}b=0
\]

producen algebraicamente:

\[
c=a\sqrt{\frac{\kappa_P}{\kappa_R}}.
\]

Esto demuestra la consecuencia de los planos elegidos, no que esos planos sean
la única ni la necesaria construcción. La necesidad de la raíz sigue pendiente.

## 8.4. Transferencia de escala

Debe demostrarse por qué una escala construida con anclajes Tierra–Luna–Sol puede
operar sobre una rama etaria cosmológica sin convertirse en mera calibración
convencional trasladada.

## 8.5. Precisión formal y precisión física

Las largas expansiones decimales son exactitud aritmética respecto de entradas
congeladas. No expresan automáticamente exactitud física equivalente.

En una redacción internacional deberán separarse:

\[
\text{reproducibilidad formal}
\neq
\text{incertidumbre metrológica}.
\]

Los radios y la distancia lunar media usados como contraste externo tienen una
precisión física finita. La salida no puede presentarse como medición física de
cien cifras.

---

# 9. Matriz de dictamen

| Objeto auditado | Dictamen |
|---|---|
| Procedencia de \(\lambda_{\mathrm{acc}}\) | **APTO** |
| Procedencia de \(N_s(\mathrm{Sol})\) | **APTO** |
| Reproducción de \(\kappa_P,\kappa_R,\kappa_\Omega\) | **APTO** |
| Reproducción de \(\sigma_{\Omega16}\) | **APTO** |
| Reproducción de \(\nu_{\mathrm{acc}}\) | **APTO** |
| Reproducción de \(\lambda_{\mathrm{acc}}\) | **APTO** |
| Reproducción de \(\lambda_{\partial}\) | **APTO** |
| Consistencia dimensional | **APTO** |
| Política de precisión | **APTO CON CORRECCIÓN DOCUMENTAL** |
| Puente \(N_c-2\leftrightarrow N_Ag_D\) | **U** |
| Estatuto de \(\chi_D\) | **U** |
| Necesidad de \(\sqrt{\kappa_P/\kappa_R}\) | **U** |
| Transferencia local–cosmológica | **U** |
| Validación física | **U** |
| Novedad computacional | **U** |

---

# 10. Dictamen de cierre de jornada

\[
\boxed{
\textbf{RESTITUCIÓN DOCUMENTAL Y ARITMÉTICA: APTA}
}
\]

\[
\boxed{
\textbf{JUSTIFICACIÓN CIENTÍFICA Y NOVEDAD: ABIERTAS}
}
\]

La Lanzadera queda preparada para el siguiente orden de trabajo:

1. cerrar el puente notacional y el estatuto de \(\chi_D\);
2. fijar la política de precisión;
3. construir el prototipo ejecutable;
4. atacar necesidad, transferencia y generalidad;
5. contrastar anterioridad;
6. seleccionar revista;
7. redactar el artículo.

No se modifica todavía la publicación canónica ni se congela un título editorial.
