# Acta de restitución documental y matemática
## Recta-Ómicron / Lanzadera Ómicron — DOAN-Ω16

**Fecha de restitución:** 5 de agosto de 2026  
**Dirección científica y autoría:** Juan Antonio Lloret Egea  
**Unidad:** Watson — Publicaciones  
**Fuente primaria recuperada:** conversación compartida «Leer documento»  
**Identificador:** `6a2f01ce-fc10-83ed-8747-9537817dbdda`  
**Fecha de la conversación:** 14 de junio de 2026  

---

## 1. Dictamen de restitución

La magnitud

\[
\lambda_{\mathrm{acc}}
(\Omega_{\mathrm{obs}}\mid \mathrm{Tierra}\mid\Omega_{SS})
\]

no fue introducida como cifra aislada. Su generador documental recuperado es el protocolo
`DOAN-Ω16`, mediante la composición:

\[
\Delta A
\longrightarrow
N_A
\longrightarrow
g_D
\longrightarrow
\nu_{\mathrm{acc}}
\longrightarrow
\lambda_{\mathrm{acc}}.
\]

La Parte II publicada conservó el valor final, pero omitió en su cuerpo la cadena generadora
completa que sí estaba presente en la conversación originaria.

---

## 2. Regla canónica recuperada

Para un dominio declarado \(D\):

\[
\Delta A_D\mid\Omega_{SS}
=
A_D^{SV}-A_{\Omega SS}^{SV},
\]

\[
N_A(D\mid\Omega_{SS})
=
\frac{\Delta A_D\mid\Omega_{SS}}{1\,a_J},
\]

de modo que \(N_A\) es un conteo adimensional de años julianos declarados.

El factor estructural es:

\[
g_D
=
\sqrt{\frac{1+\chi_D}{2}}.
\]

La coordenada nodal interna es:

\[
\nu_{\mathrm{acc},\Omega16}^{0}
(D\mid\mathrm{Tierra})
=
N_A(D\mid\Omega_{SS})\,g_D.
\]

La escala ómicron congelada es:

\[
\sigma_{\Omega16}
=
32\,259\,171\,469.536939603289232466005322538473167
\ \mathrm{UFE}.
\]

La salida extensional queda:

\[
\operatorname{DOAN}_{\Omega16}^{0}
(\mathrm{Tierra}\rightarrow D)
=
\sigma_{\Omega16}
\,\nu_{\mathrm{acc},\Omega16}^{0}
(D\mid\mathrm{Tierra}).
\]

En notación posterior:

\[
\lambda_{\mathrm{acc}}(D\mid O)
=
\sigma_{\Omega16}\,
\nu_{\mathrm{acc}}(D\mid O).
\]

---


## 2.1. Genealogía recuperada de la escala \(\sigma_{\Omega16}\)

La escala tampoco queda ya como cifra huérfana. La conversación originaria conserva
su construcción a partir del acoplamiento de dos planos.

Coeficiente potencial del dominio base:

\[
\kappa_P
=
\frac{N_s(\mathrm{Tierra})}{N_s(\mathrm{Sol})},
\]

con:

\[
N_s(\mathrm{Tierra})
=
149\,213\,470\,700\ \mathrm{UFE},
\]

\[
N_s(\mathrm{Sol})
=
246\,934.365250679780\ \mathrm{UFE},
\]

de donde:

\[
\kappa_P
=
604\,263.6898615683206487433327670029405\ldots
\]

Coeficiente radial:

\[
\kappa_R
=
\frac{R_{\odot}}{R_{\mathrm{Tierra}}+R_{\mathrm{Luna}}},
\]

con:

\[
R_{\mathrm{Tierra}}=6\,371\,000\ \mathrm{UFE},
\quad
R_{\mathrm{Luna}}=1\,737\,400\ \mathrm{UFE},
\quad
R_{\odot}=695\,700\,000\ \mathrm{UFE},
\]

de donde:

\[
\kappa_R
=
85.7999112031966849193429036554684031\ldots
\]

El cociente plano–plano no se usa directamente como avance lineal. La conversación
define la linealización:

\[
\kappa_{\Omega}
=
\sqrt{\frac{\kappa_P}{\kappa_R}}
=
83.9208414920315806537180865400762813\ldots
\]

Los dos planos son:

\[
\Pi_{1,\Omega16}:
b-\frac{a}{\sqrt{\kappa_R}}=0,
\]

\[
\Pi_{2,\Omega16}:
c-\sqrt{\kappa_P}\,b=0.
\]

Su intersección produce:

\[
c
=
a\sqrt{\frac{\kappa_P}{\kappa_R}}
=
a\,\kappa_{\Omega}.
\]

Como:

\[
c
=
\frac{d_{\Omega}(\mathrm{Tierra},X)}
{d_{\mathrm{Tierra-Luna}}},
\]

la regla generativa local es:

\[
d_{\Omega}(\mathrm{Tierra},X)
=
d_{\mathrm{Tierra-Luna}}
\,(N_c(X)-2)
\,\kappa_{\Omega}.
\]

El paso métrico de la recta queda:

\[
\sigma_{\Omega16}
=
D_{TL}\,\kappa_{\Omega}
\]

\[
=
384\,400\,000
\cdot
83.9208414920315806537180865400762813\ldots
\]

\[
=
32\,259\,171\,469.536939603289232466005322538473167\ldots
\ \mathrm{UFE}.
\]

Por tanto, el cociente que posteriormente aparece como:

\[
\frac{\lambda_{\mathrm{acc}}}{\nu_{\mathrm{acc}}}
\]

no es una constante desconocida: es exactamente \(\sigma_{\Omega16}\).

---

## 3. Ejecución para el observable retornado

Entradas:

\[
A_{\Omega_{\mathrm{obs}}}^{SV}
=
13\,800\,000\,000\ a_J,
\]

\[
A_{\Omega SS}^{SV}
=
4\,568\,000\,000\ a_J,
\qquad
\chi_{\Omega_{\mathrm{obs}}}
=
\frac12.
\]

Entonces:

\[
\Delta A_{\Omega_{\mathrm{obs}}\mid\Omega SS}
=
9\,232\,000\,000\ a_J,
\]

\[
N_A(\Omega_{\mathrm{obs}}\mid\Omega SS)
=
9\,232\,000\,000,
\]

\[
g_{\Omega_{\mathrm{obs}}}
=
\frac{\sqrt3}{2}.
\]

Por tanto:

\[
\nu_{\mathrm{acc}}
=
9\,232\,000\,000\frac{\sqrt3}{2}
\]

\[
=
7\,995\,146\,527.737937586922692312391106845807989051588716979105605017150122806051020971\ldots
\]

y:

\[
\lambda_{\mathrm{acc}}
=
\sigma_{\Omega16}\nu_{\mathrm{acc}}
\]

\[
=
257\,916\,802\,762\,371\,004\,117.8021159948054130965383279286041549868367802475908620127745896778575090806844476\ldots
\ \mathrm{UFE}.
\]

Esta salida es una **coordenada extensional de acceso nodal**. No es frontera,
radio cosmológico primario ni distancia comóvil.

---

## 4. Distinción entre \(\nu_{\mathrm{acc}}\) y \(t_{\Omega_{\mathrm{obs}}}\)

La coordenada \(\nu_{\mathrm{acc}}\) pertenece al protocolo interno DOAN-Ω16.

La coordenada \(t_{\Omega_{\mathrm{obs}}}\) pertenece a la carta afín local
Tierra–Luna–Sol y se obtiene después de que \(\lambda_{\mathrm{acc}}\) ya ha sido calculada.

Con:

\[
D_{TL}=384\,400\,000\ \mathrm{UFE},
\]

\[
D_{TS}=149\,597\,870\,700\ \mathrm{UFE},
\]

\[
A_{LS\mid\mathrm{Tierra}}
=
D_{TS}-D_{TL}
=
149\,213\,470\,700\ \mathrm{UFE},
\]

la recta local es:

\[
\lambda_{LS}(t)
=
D_{TL}
+t\,A_{LS\mid\mathrm{Tierra}}.
\]

La posición local del acceso se obtiene por:

\[
t_{\Omega_{\mathrm{obs}}}
=
\frac{\lambda_{\mathrm{acc}}-D_{TL}}
{A_{LS\mid\mathrm{Tierra}}},
\]

\[
t_{\Omega_{\mathrm{obs}}}
=
1\,728\,508\,837.3859975104633908632406431458774340266626085186746934923187927831825078623940721\ldots
\]

No existe contradicción:

- \(\nu_{\mathrm{acc}}\) genera la extensión dentro de DOAN-Ω16;
- \(t_{\Omega_{\mathrm{obs}}}\) sitúa esa extensión ya generada sobre una carta local auxiliar.

---

## 5. Frontera etaria

Para la frontera:

\[
A_{\mathrm{fin}}(\Omega_{\mathrm{obs}})
=
27\,600\,000\,000\ a_J,
\]

\[
\Delta A_{\partial\Omega_{\mathrm{obs}}\mid\Omega SS}
=
23\,032\,000\,000\ a_J,
\]

\[
\nu_{\partial\Omega_{\mathrm{obs}}}
=
23\,032\,000\,000\frac{\sqrt3}{2}.
\]

La coordenada extensional de frontera es:

\[
\lambda_{\partial}
=
\sigma_{\Omega16}
\nu_{\partial\Omega_{\mathrm{obs}}},
\]

\[
\lambda_{\partial}
=
643\,451\,018\,330\,039\,966\,078.9881212730024127425769896936320296422037177927331817459081834337536989976521011\ldots
\ \mathrm{UFE}.
\]

La razón frontera–acceso es:

\[
\kappa_{\partial\leftarrow\mathrm{acc}}^{SV}
=
\frac{23\,032\,000\,000}{9\,232\,000\,000}
=
\frac{2879}{1154},
\]

y:

\[
\lambda_{\partial}
=
\kappa_{\partial\leftarrow\mathrm{acc}}^{SV}
\lambda_{\mathrm{acc}}.
\]

---

## 6. Estado documental

### Establecido

- existe una cadena generadora explícita para \(\lambda_{\mathrm{acc}}\);
- \(\nu_{\mathrm{acc}}\) y \(t_{\Omega_{\mathrm{obs}}}\) pertenecen a cartas distintas;
- la frontera se genera por la misma escala ómicron y un conteo etario distinto;
- las identidades aritméticas reproducen las cifras publicadas;
- la Parte II omitió la derivación upstream, pero no inventó el valor final.

### Pendiente de auditoría científica, no de procedencia documental

La genealogía documental de \(\sigma_{\Omega16}\), \(\nu_{\mathrm{acc}}\),
\(\lambda_{\mathrm{acc}}\), \(\lambda_{\partial}\) y las cartas locales queda recuperada.

Permanece pendiente juzgar científicamente:

- la justificación no meramente constructiva de \(\kappa_P\) y \(\kappa_R\);
- la necesidad matemática de la raíz
  \(\sqrt{\kappa_P/\kappa_R}\) como linealización;
- la legitimidad de transferir la escala obtenida en el dominio local a la rama
  etaria ascendente;
- la generalidad del protocolo fuera de los dominios usados para su clausura;
- su novedad frente a métodos previos.

---

## 7. Próximo paso autorizado

Construir una especificación ejecutable de referencia que:

1. reciba \(A_D^{SV}\), \(A_{\Omega SS}^{SV}\), \(\chi_D\) y \(\sigma_{\Omega16}\);
2. calcule \(\Delta A\), \(N_A\), \(g_D\), \(\nu_{\mathrm{acc}}\) y \(\lambda_{\mathrm{acc}}\);
3. calcule la frontera y el residual acceso–frontera;
4. produzca los retornos UFE, Tierra–Luna, Tierra–Sol y carta local \(t\);
5. conserve dictamen, dominio, unidad, residual y trazabilidad;
6. incluya ataques por sustitución de dominio y contaminación externa.

No se seleccionará revista hasta auditar la justificación científica de la escala,
ejecutar el operador completo y compararlo con la literatura previa.
