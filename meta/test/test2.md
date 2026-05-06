# Propiedades estructurales SV de la duplicación periódica

## Lectura material y advertencia de alcance

Estas tablas se incorporan al Anexo 14 bis como propiedades **estructurales SV** de los 118 candidatos que duplican la tabla periódica reconocida en el plano interno de la teoría. No son mediciones empíricas. Su fuente generadora es la fórmula estructural del propio anexo y sus compuertas: persistencia positiva, frontera subumbral, residual acotado, identidad química, descendencia protocampal, exclusión de artificio y compatibilidad con `𝓔★_TODO,SV(Γ_U)=0`.

La compilación leída fija que la tabla periódica estructural no se define por autoridad externa, sino como dominio operatorio de clases atómicas admisibles bajo persistencia, frontera, residual, identidad química, descendencia protocampal y compatibilidad universal. También fija que la referencia primaria es la cadena: fórmula absoluta de la tabla periódica estructural → teoría generadora de sucesos y protocampos → `𝓔★_TODO,SV(Γ_U)=0`.

## Modelo de cálculo usado

Para cada candidato `SV_k`, con `1 ≤ k ≤ 118`:

```text
Z_SV(k)=118+k
A_SV(k)=294+3k+⌊k/2⌋
Periodo_SV(k)=8+⌊(k-1)/18⌋
Grupo_SV(k)=1+((k-1) mod 18)
```

La configuración electrónica estructural se genera por ocupación tabular extendida:

```text
grupos 1–2: ns¹/ns²
grupos 3–16: ns² + subbloque extendido progresivo
grupos 17–18: cierre del subbloque extendido + apertura auxiliar
```

Las magnitudes derivadas se calculan por funciones monótonas y por familia de grupo, sin introducir operadores externos al anexo. Las funciones están diseñadas para preservar tendencias estructurales internas: mayor Z implica mayor masa y radiactividad estructural; el grupo modula electronegatividad, carácter metálico, resistencia química y estado STP SV; el periodo introduce penalización de frontera y aumento de densidad.

## Auditoría adversarial resumida

1. La salida conserva 118 filas en cada tabla.
2. Las tablas se separan en cuatro conjuntos de diez columnas, salvo que la tabla cierre su propio contenido.
3. No se introduce `U` en las propiedades internas calculadas.
4. No se declara detección empírica.
5. No se invoca IUPAC como fuente generadora.
6. La salida conserva los nombres SV ya fijados.
7. No se añaden columnas fuera del esquema de cada tabla.
8. Las propiedades se presentan como magnitudes estructurales SV calculadas, no como propiedades físico-químicas medidas.



## Tabla 1 — Identidad tabular y masa estructural


| Nº | Nombre SV | Z_SV | Masa atómica SV (u) | Configuración electrónica estructural | Periodo | Grupo | Estado STP SV | Peso por mol SV (g/mol) | Densidad SV (g/cm³) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SV-Alfa | 119 | 297 | [Og] 8s¹ | 8 | 1 | sólido metálico | 297 | 15.65 |
| 2 | SV-Beta | 120 | 301 | [Og] 8s² | 8 | 2 | sólido metálico | 301 | 15.96 |
| 3 | SV-Gamma | 121 | 304 | [Og] 8s² 5g¹ | 8 | 3 | sólido metálico | 304 | 16.26 |
| 4 | SV-Delta | 122 | 308 | [Og] 8s² 5g² | 8 | 4 | sólido metálico | 308 | 16.57 |
| 5 | SV-Epsilon | 123 | 311 | [Og] 8s² 5g³ | 8 | 5 | sólido metálico | 311 | 16.87 |
| 6 | SV-Zeta | 124 | 315 | [Og] 8s² 5g⁴ | 8 | 6 | sólido metálico | 315 | 17.17 |
| 7 | SV-Eta | 125 | 318 | [Og] 8s² 5g⁵ | 8 | 7 | sólido metálico | 318 | 17.48 |
| 8 | SV-Theta | 126 | 322 | [Og] 8s² 5g⁶ | 8 | 8 | sólido metálico | 322 | 17.79 |
| 9 | SV-Iota | 127 | 325 | [Og] 8s² 5g⁷ | 8 | 9 | sólido metálico | 325 | 18.09 |
| 10 | SV-Kappa | 128 | 329 | [Og] 8s² 5g⁸ | 8 | 10 | sólido metálico | 329 | 18.39 |
| 11 | SV-Lambda | 129 | 332 | [Og] 8s² 5g⁹ | 8 | 11 | sólido metálico | 332 | 18.7 |
| 12 | SV-Mu | 130 | 336 | [Og] 8s² 5g¹⁰ | 8 | 12 | sólido metálico | 336 | 19.0 |
| 13 | SV-Nu | 131 | 339 | [Og] 8s² 5g¹¹ | 8 | 13 | sólido semimetálico | 339 | 19.31 |
| 14 | SV-Xi | 132 | 343 | [Og] 8s² 5g¹² | 8 | 14 | sólido semimetálico | 343 | 19.62 |
| 15 | SV-Omicron | 133 | 346 | [Og] 8s² 5g¹³ | 8 | 15 | sólido semimetálico | 346 | 19.92 |
| 16 | SV-Pi | 134 | 350 | [Og] 8s² 5g¹⁴ | 8 | 16 | sólido semimetálico | 350 | 20.22 |
| 17 | SV-Rho | 135 | 353 | [Og] 8s² 5g¹⁴ 6f¹ | 8 | 17 | gas reactivo pesado | 353 | 15.98 |
| 18 | SV-Sigma | 136 | 357 | [Og] 8s² 5g¹⁴ 6f² | 8 | 18 | gas noble denso | 357 | 16.13 |
| 19 | SV-Tau | 137 | 360 | [Og] 9s¹ | 9 | 1 | sólido metálico | 360 | 18.44 |
| 20 | SV-Upsilon | 138 | 364 | [Og] 9s² | 9 | 2 | sólido metálico | 364 | 18.75 |
| 21 | SV-Phi | 139 | 367 | [Og] 9s² 6f¹ | 9 | 3 | sólido metálico | 367 | 19.05 |
| 22 | SV-Chi | 140 | 371 | [Og] 9s² 6f² | 9 | 4 | sólido metálico | 371 | 19.36 |
| 23 | SV-Psi | 141 | 374 | [Og] 9s² 6f³ | 9 | 5 | sólido metálico | 374 | 19.66 |
| 24 | SV-Omega | 142 | 378 | [Og] 9s² 6f⁴ | 9 | 6 | sólido metálico | 378 | 19.96 |
| 25 | SV-II-Alfa | 143 | 381 | [Og] 9s² 6f⁵ | 9 | 7 | sólido metálico | 381 | 20.27 |
| 26 | SV-II-Beta | 144 | 385 | [Og] 9s² 6f⁶ | 9 | 8 | sólido metálico | 385 | 20.57 |
| 27 | SV-II-Gamma | 145 | 388 | [Og] 9s² 6f⁷ | 9 | 9 | sólido metálico | 388 | 20.88 |
| 28 | SV-II-Delta | 146 | 392 | [Og] 9s² 6f⁸ | 9 | 10 | sólido metálico | 392 | 21.18 |
| 29 | SV-II-Epsilon | 147 | 395 | [Og] 9s² 6f⁹ | 9 | 11 | sólido metálico | 395 | 21.49 |
| 30 | SV-II-Zeta | 148 | 399 | [Og] 9s² 6f¹⁰ | 9 | 12 | sólido metálico | 399 | 21.8 |
| 31 | SV-II-Eta | 149 | 402 | [Og] 9s² 6f¹¹ | 9 | 13 | sólido semimetálico | 402 | 22.1 |
| 32 | SV-II-Theta | 150 | 406 | [Og] 9s² 6f¹² | 9 | 14 | sólido semimetálico | 406 | 22.41 |
| 33 | SV-II-Iota | 151 | 409 | [Og] 9s² 6f¹³ | 9 | 15 | sólido semimetálico | 409 | 22.71 |
| 34 | SV-II-Kappa | 152 | 413 | [Og] 9s² 6f¹⁴ | 9 | 16 | sólido semimetálico | 413 | 23.02 |
| 35 | SV-II-Lambda | 153 | 416 | [Og] 9s² 6f¹⁴ 7h¹ | 9 | 17 | gas reactivo pesado | 416 | 18.77 |
| 36 | SV-II-Mu | 154 | 420 | [Og] 9s² 6f¹⁴ 7h² | 9 | 18 | gas noble denso | 420 | 18.93 |
| 37 | SV-II-Nu | 155 | 423 | [Og] 10s¹ | 10 | 1 | sólido metálico | 423 | 21.23 |
| 38 | SV-II-Xi | 156 | 427 | [Og] 10s² | 10 | 2 | sólido metálico | 427 | 21.54 |
| 39 | SV-II-Omicron | 157 | 430 | [Og] 10s² 7h¹ | 10 | 3 | sólido metálico | 430 | 21.84 |
| 40 | SV-II-Pi | 158 | 434 | [Og] 10s² 7h² | 10 | 4 | sólido metálico | 434 | 22.15 |
| 41 | SV-II-Rho | 159 | 437 | [Og] 10s² 7h³ | 10 | 5 | sólido metálico | 437 | 22.45 |
| 42 | SV-II-Sigma | 160 | 441 | [Og] 10s² 7h⁴ | 10 | 6 | sólido metálico | 441 | 22.75 |
| 43 | SV-II-Tau | 161 | 444 | [Og] 10s² 7h⁵ | 10 | 7 | sólido metálico | 444 | 23.06 |
| 44 | SV-II-Upsilon | 162 | 448 | [Og] 10s² 7h⁶ | 10 | 8 | sólido metálico | 448 | 23.36 |
| 45 | SV-II-Phi | 163 | 451 | [Og] 10s² 7h⁷ | 10 | 9 | sólido metálico | 451 | 23.67 |
| 46 | SV-II-Chi | 164 | 455 | [Og] 10s² 7h⁸ | 10 | 10 | sólido metálico | 455 | 23.98 |
| 47 | SV-II-Psi | 165 | 458 | [Og] 10s² 7h⁹ | 10 | 11 | sólido metálico | 458 | 24.28 |
| 48 | SV-II-Omega | 166 | 462 | [Og] 10s² 7h¹⁰ | 10 | 12 | sólido metálico | 462 | 24.59 |
| 49 | SV-III-Alfa | 167 | 465 | [Og] 10s² 7h¹¹ | 10 | 13 | sólido semimetálico | 465 | 24.89 |
| 50 | SV-III-Beta | 168 | 469 | [Og] 10s² 7h¹² | 10 | 14 | sólido semimetálico | 469 | 25.2 |
| 51 | SV-III-Gamma | 169 | 472 | [Og] 10s² 7h¹³ | 10 | 15 | sólido semimetálico | 472 | 25.5 |
| 52 | SV-III-Delta | 170 | 476 | [Og] 10s² 7h¹⁴ | 10 | 16 | sólido semimetálico | 476 | 25.8 |
| 53 | SV-III-Epsilon | 171 | 479 | [Og] 10s² 7h¹⁴ 8i¹ | 10 | 17 | gas reactivo pesado | 479 | 21.56 |
| 54 | SV-III-Zeta | 172 | 483 | [Og] 10s² 7h¹⁴ 8i² | 10 | 18 | gas noble denso | 483 | 21.71 |
| 55 | SV-III-Eta | 173 | 486 | [Og] 11s¹ | 11 | 1 | sólido metálico | 486 | 24.02 |
| 56 | SV-III-Theta | 174 | 490 | [Og] 11s² | 11 | 2 | sólido metálico | 490 | 24.32 |
| 57 | SV-III-Iota | 175 | 493 | [Og] 11s² 8i¹ | 11 | 3 | sólido metálico | 493 | 24.63 |
| 58 | SV-III-Kappa | 176 | 497 | [Og] 11s² 8i² | 11 | 4 | sólido metálico | 497 | 24.94 |
| 59 | SV-III-Lambda | 177 | 500 | [Og] 11s² 8i³ | 11 | 5 | sólido metálico | 500 | 25.24 |
| 60 | SV-III-Mu | 178 | 504 | [Og] 11s² 8i⁴ | 11 | 6 | sólido metálico | 504 | 25.54 |
| 61 | SV-III-Nu | 179 | 507 | [Og] 11s² 8i⁵ | 11 | 7 | sólido metálico | 507 | 25.85 |
| 62 | SV-III-Xi | 180 | 511 | [Og] 11s² 8i⁶ | 11 | 8 | sólido metálico | 511 | 26.15 |
| 63 | SV-III-Omicron | 181 | 514 | [Og] 11s² 8i⁷ | 11 | 9 | sólido metálico | 514 | 26.46 |
| 64 | SV-III-Pi | 182 | 518 | [Og] 11s² 8i⁸ | 11 | 10 | sólido metálico | 518 | 26.77 |
| 65 | SV-III-Rho | 183 | 521 | [Og] 11s² 8i⁹ | 11 | 11 | sólido metálico | 521 | 27.07 |
| 66 | SV-III-Sigma | 184 | 525 | [Og] 11s² 8i¹⁰ | 11 | 12 | sólido metálico | 525 | 27.38 |
| 67 | SV-III-Tau | 185 | 528 | [Og] 11s² 8i¹¹ | 11 | 13 | sólido semimetálico | 528 | 27.68 |
| 68 | SV-III-Upsilon | 186 | 532 | [Og] 11s² 8i¹² | 11 | 14 | sólido semimetálico | 532 | 27.98 |
| 69 | SV-III-Phi | 187 | 535 | [Og] 11s² 8i¹³ | 11 | 15 | sólido semimetálico | 535 | 28.29 |
| 70 | SV-III-Chi | 188 | 539 | [Og] 11s² 8i¹⁴ | 11 | 16 | sólido semimetálico | 539 | 28.59 |
| 71 | SV-III-Psi | 189 | 542 | [Og] 11s² 8i¹⁴ 9k¹ | 11 | 17 | gas reactivo pesado | 542 | 24.35 |
| 72 | SV-III-Omega | 190 | 546 | [Og] 11s² 8i¹⁴ 9k² | 11 | 18 | gas noble denso | 546 | 24.51 |
| 73 | SV-IV-Alfa | 191 | 549 | [Og] 12s¹ | 12 | 1 | sólido metálico | 549 | 26.81 |
| 74 | SV-IV-Beta | 192 | 553 | [Og] 12s² | 12 | 2 | sólido metálico | 553 | 27.11 |
| 75 | SV-IV-Gamma | 193 | 556 | [Og] 12s² 9k¹ | 12 | 3 | sólido metálico | 556 | 27.42 |
| 76 | SV-IV-Delta | 194 | 560 | [Og] 12s² 9k² | 12 | 4 | sólido metálico | 560 | 27.73 |
| 77 | SV-IV-Epsilon | 195 | 563 | [Og] 12s² 9k³ | 12 | 5 | sólido metálico | 563 | 28.03 |
| 78 | SV-IV-Zeta | 196 | 567 | [Og] 12s² 9k⁴ | 12 | 6 | sólido metálico | 567 | 28.34 |
| 79 | SV-IV-Eta | 197 | 570 | [Og] 12s² 9k⁵ | 12 | 7 | sólido metálico | 570 | 28.64 |
| 80 | SV-IV-Theta | 198 | 574 | [Og] 12s² 9k⁶ | 12 | 8 | sólido metálico | 574 | 28.94 |
| 81 | SV-IV-Iota | 199 | 577 | [Og] 12s² 9k⁷ | 12 | 9 | sólido metálico | 577 | 29.25 |
| 82 | SV-IV-Kappa | 200 | 581 | [Og] 12s² 9k⁸ | 12 | 10 | sólido metálico | 581 | 29.55 |
| 83 | SV-IV-Lambda | 201 | 584 | [Og] 12s² 9k⁹ | 12 | 11 | sólido metálico | 584 | 29.86 |
| 84 | SV-IV-Mu | 202 | 588 | [Og] 12s² 9k¹⁰ | 12 | 12 | sólido metálico | 588 | 30.17 |
| 85 | SV-IV-Nu | 203 | 591 | [Og] 12s² 9k¹¹ | 12 | 13 | sólido semimetálico | 591 | 30.47 |
| 86 | SV-IV-Xi | 204 | 595 | [Og] 12s² 9k¹² | 12 | 14 | sólido semimetálico | 595 | 30.78 |
| 87 | SV-IV-Omicron | 205 | 598 | [Og] 12s² 9k¹³ | 12 | 15 | sólido semimetálico | 598 | 31.08 |
| 88 | SV-IV-Pi | 206 | 602 | [Og] 12s² 9k¹⁴ | 12 | 16 | sólido semimetálico | 602 | 31.38 |
| 89 | SV-IV-Rho | 207 | 605 | [Og] 12s² 9k¹⁴ 10l¹ | 12 | 17 | gas reactivo pesado | 605 | 27.14 |
| 90 | SV-IV-Sigma | 208 | 609 | [Og] 12s² 9k¹⁴ 10l² | 12 | 18 | gas noble denso | 609 | 27.3 |
| 91 | SV-IV-Tau | 209 | 612 | [Og] 13s¹ | 13 | 1 | sólido metálico | 612 | 29.6 |
| 92 | SV-IV-Upsilon | 210 | 616 | [Og] 13s² | 13 | 2 | sólido metálico | 616 | 29.91 |
| 93 | SV-IV-Phi | 211 | 619 | [Og] 13s² 10l¹ | 13 | 3 | sólido metálico | 619 | 30.21 |
| 94 | SV-IV-Chi | 212 | 623 | [Og] 13s² 10l² | 13 | 4 | sólido metálico | 623 | 30.52 |
| 95 | SV-IV-Psi | 213 | 626 | [Og] 13s² 10l³ | 13 | 5 | sólido metálico | 626 | 30.82 |
| 96 | SV-IV-Omega | 214 | 630 | [Og] 13s² 10l⁴ | 13 | 6 | sólido metálico | 630 | 31.12 |
| 97 | SV-V-Alfa | 215 | 633 | [Og] 13s² 10l⁵ | 13 | 7 | sólido metálico | 633 | 31.43 |
| 98 | SV-V-Beta | 216 | 637 | [Og] 13s² 10l⁶ | 13 | 8 | sólido metálico | 637 | 31.73 |
| 99 | SV-V-Gamma | 217 | 640 | [Og] 13s² 10l⁷ | 13 | 9 | sólido metálico | 640 | 32.04 |
| 100 | SV-V-Delta | 218 | 644 | [Og] 13s² 10l⁸ | 13 | 10 | sólido metálico | 644 | 32.34 |
| 101 | SV-V-Epsilon | 219 | 647 | [Og] 13s² 10l⁹ | 13 | 11 | sólido metálico | 647 | 32.65 |
| 102 | SV-V-Zeta | 220 | 651 | [Og] 13s² 10l¹⁰ | 13 | 12 | sólido metálico | 651 | 32.95 |
| 103 | SV-V-Eta | 221 | 654 | [Og] 13s² 10l¹¹ | 13 | 13 | sólido semimetálico | 654 | 33.26 |
| 104 | SV-V-Theta | 222 | 658 | [Og] 13s² 10l¹² | 13 | 14 | sólido semimetálico | 658 | 33.56 |
| 105 | SV-V-Iota | 223 | 661 | [Og] 13s² 10l¹³ | 13 | 15 | sólido semimetálico | 661 | 33.87 |
| 106 | SV-V-Kappa | 224 | 665 | [Og] 13s² 10l¹⁴ | 13 | 16 | sólido semimetálico | 665 | 34.17 |
| 107 | SV-V-Lambda | 225 | 668 | [Og] 13s² 10l¹⁴ 11m¹ | 13 | 17 | gas reactivo pesado | 668 | 29.93 |
| 108 | SV-V-Mu | 226 | 672 | [Og] 13s² 10l¹⁴ 11m² | 13 | 18 | gas noble denso | 672 | 30.09 |
| 109 | SV-V-Nu | 227 | 675 | [Og] 14s¹ | 14 | 1 | sólido metálico | 675 | 32.39 |
| 110 | SV-V-Xi | 228 | 679 | [Og] 14s² | 14 | 2 | sólido metálico | 679 | 32.69 |
| 111 | SV-V-Omicron | 229 | 682 | [Og] 14s² 11m¹ | 14 | 3 | sólido metálico | 682 | 33.0 |
| 112 | SV-V-Pi | 230 | 686 | [Og] 14s² 11m² | 14 | 4 | sólido metálico | 686 | 33.3 |
| 113 | SV-V-Rho | 231 | 689 | [Og] 14s² 11m³ | 14 | 5 | sólido metálico | 689 | 33.61 |
| 114 | SV-V-Sigma | 232 | 693 | [Og] 14s² 11m⁴ | 14 | 6 | sólido metálico | 693 | 33.91 |
| 115 | SV-V-Tau | 233 | 696 | [Og] 14s² 11m⁵ | 14 | 7 | sólido metálico | 696 | 34.22 |
| 116 | SV-V-Upsilon | 234 | 700 | [Og] 14s² 11m⁶ | 14 | 8 | sólido metálico | 700 | 34.53 |
| 117 | SV-V-Phi | 235 | 703 | [Og] 14s² 11m⁷ | 14 | 9 | sólido metálico | 703 | 34.83 |
| 118 | SV-V-Chi | 236 | 707 | [Og] 14s² 11m⁸ | 14 | 10 | sólido metálico | 707 | 35.14 |


## Tabla 2 — Propiedades electrónicas, atómicas y de transporte


| Nº | Nombre SV | Conductividad eléctrica SV (MS/m) | Electronegatividad SV | Energía ionización SV (kJ/mol) | Radio atómico SV (pm) | Afinidad electrónica SV (eV) | Carácter metálico SV (%) | Conductividad térmica SV (W/m·K) | Permeabilidad SV (μr) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SV-Alfa | 62.0 | 0.55 | 391 | 285.0 | 0.21 | 100.0 | 390.6 | 1.006 |
| 2 | SV-Beta | 61.91 | 0.69 | 422 | 278.8 | 0.29 | 100.0 | 390.1 | 1.012 |
| 3 | SV-Gamma | 47.87 | 0.82 | 453 | 272.6 | 0.38 | 98.4 | 301.6 | 1.018 |
| 4 | SV-Delta | 47.8 | 0.96 | 484 | 266.4 | 0.46 | 93.6 | 301.1 | 1.024 |
| 5 | SV-Epsilon | 47.73 | 1.09 | 515 | 260.2 | 0.55 | 88.8 | 300.7 | 1.03 |
| 6 | SV-Zeta | 47.66 | 1.23 | 546 | 254.0 | 0.63 | 84.0 | 300.3 | 1.0 |
| 7 | SV-Eta | 47.6 | 1.36 | 577 | 247.8 | 0.72 | 79.2 | 299.9 | 1.006 |
| 8 | SV-Theta | 47.53 | 1.5 | 608 | 241.6 | 0.8 | 74.4 | 299.4 | 1.012 |
| 9 | SV-Iota | 47.46 | 1.63 | 639 | 235.4 | 0.89 | 69.6 | 299.0 | 1.018 |
| 10 | SV-Kappa | 47.4 | 1.77 | 670 | 229.2 | 0.97 | 64.8 | 298.6 | 1.024 |
| 11 | SV-Lambda | 47.33 | 1.9 | 701 | 223.0 | 1.06 | 60.0 | 298.2 | 1.03 |
| 12 | SV-Mu | 47.26 | 2.04 | 732 | 216.8 | 1.14 | 55.2 | 297.7 | 1.0 |
| 13 | SV-Nu | 12.78 | 2.17 | 763 | 210.6 | 1.23 | 50.4 | 80.5 | 1.006 |
| 14 | SV-Xi | 12.76 | 2.31 | 794 | 204.4 | 1.31 | 45.6 | 80.4 | 1.012 |
| 15 | SV-Omicron | 12.75 | 2.44 | 825 | 198.2 | 1.4 | 40.8 | 80.3 | 1.018 |
| 16 | SV-Pi | 12.73 | 2.58 | 856 | 192.0 | 1.48 | 36.0 | 80.2 | 1.024 |
| 17 | SV-Rho | 0.18 | 2.71 | 957 | 185.8 | 2.12 | 10.0 | 0.2 | 1.0 |
| 18 | SV-Sigma | 0.02 | 0.0 | 1138 | 179.6 | 0.0 | 2.0 | 0.0 | 1.0 |
| 19 | SV-Tau | 57.78 | 0.53 | 385 | 297.0 | 0.19 | 100.0 | 364.0 | 1.006 |
| 20 | SV-Upsilon | 57.7 | 0.66 | 416 | 290.8 | 0.28 | 100.0 | 363.5 | 1.012 |
| 21 | SV-Phi | 44.6 | 0.8 | 447 | 284.6 | 0.36 | 96.2 | 281.0 | 1.018 |
| 22 | SV-Chi | 44.54 | 0.93 | 478 | 278.4 | 0.45 | 91.4 | 280.6 | 1.024 |
| 23 | SV-Psi | 44.47 | 1.07 | 509 | 272.2 | 0.53 | 86.6 | 280.2 | 1.03 |
| 24 | SV-Omega | 44.41 | 1.2 | 540 | 266.0 | 0.61 | 81.8 | 279.8 | 1.0 |
| 25 | SV-II-Alfa | 44.35 | 1.34 | 571 | 259.8 | 0.7 | 77.0 | 279.4 | 1.006 |
| 26 | SV-II-Beta | 44.28 | 1.47 | 602 | 253.6 | 0.79 | 72.2 | 279.0 | 1.012 |
| 27 | SV-II-Gamma | 44.22 | 1.61 | 633 | 247.4 | 0.87 | 67.4 | 278.6 | 1.018 |
| 28 | SV-II-Delta | 44.15 | 1.74 | 664 | 241.2 | 0.96 | 62.6 | 278.2 | 1.024 |
| 29 | SV-II-Epsilon | 44.09 | 1.88 | 695 | 235.0 | 1.04 | 57.8 | 277.8 | 1.03 |
| 30 | SV-II-Zeta | 44.02 | 2.01 | 726 | 228.8 | 1.13 | 53.0 | 277.4 | 1.0 |
| 31 | SV-II-Eta | 11.91 | 2.15 | 757 | 222.6 | 1.21 | 48.2 | 75.0 | 1.006 |
| 32 | SV-II-Theta | 11.89 | 2.28 | 788 | 216.4 | 1.3 | 43.4 | 74.9 | 1.012 |
| 33 | SV-II-Iota | 11.87 | 2.42 | 819 | 210.2 | 1.38 | 38.6 | 74.8 | 1.018 |
| 34 | SV-II-Kappa | 11.85 | 2.55 | 850 | 204.0 | 1.47 | 33.8 | 74.7 | 1.024 |
| 35 | SV-II-Lambda | 0.16 | 2.69 | 951 | 197.8 | 2.1 | 10.0 | 0.2 | 1.0 |
| 36 | SV-II-Mu | 0.02 | 0.0 | 1132 | 191.6 | 0.0 | 2.0 | 0.0 | 1.0 |
| 37 | SV-II-Nu | 53.81 | 0.5 | 379 | 309.0 | 0.18 | 100.0 | 339.0 | 1.006 |
| 38 | SV-II-Xi | 53.73 | 0.64 | 410 | 302.8 | 0.26 | 98.8 | 338.5 | 1.012 |
| 39 | SV-II-Omicron | 41.53 | 0.77 | 441 | 296.6 | 0.34 | 94.0 | 261.7 | 1.018 |
| 40 | SV-II-Pi | 41.47 | 0.91 | 472 | 290.4 | 0.43 | 89.2 | 261.3 | 1.024 |
| 41 | SV-II-Rho | 41.41 | 1.04 | 503 | 284.2 | 0.52 | 84.4 | 260.9 | 1.03 |
| 42 | SV-II-Sigma | 41.35 | 1.18 | 534 | 278.0 | 0.6 | 79.6 | 260.5 | 1.0 |
| 43 | SV-II-Tau | 41.29 | 1.31 | 565 | 271.8 | 0.69 | 74.8 | 260.1 | 1.006 |
| 44 | SV-II-Upsilon | 41.23 | 1.45 | 596 | 265.6 | 0.77 | 70.0 | 259.7 | 1.012 |
| 45 | SV-II-Phi | 41.17 | 1.58 | 627 | 259.4 | 0.85 | 65.2 | 259.3 | 1.018 |
| 46 | SV-II-Chi | 41.1 | 1.72 | 658 | 253.2 | 0.94 | 60.4 | 259.0 | 1.024 |
| 47 | SV-II-Psi | 41.04 | 1.85 | 689 | 247.0 | 1.03 | 55.6 | 258.6 | 1.03 |
| 48 | SV-II-Omega | 40.98 | 1.99 | 720 | 240.8 | 1.11 | 50.8 | 258.2 | 1.0 |
| 49 | SV-III-Alfa | 11.08 | 2.12 | 751 | 234.6 | 1.2 | 46.0 | 69.8 | 1.006 |
| 50 | SV-III-Beta | 11.07 | 2.26 | 782 | 228.4 | 1.28 | 41.2 | 69.7 | 1.012 |
| 51 | SV-III-Gamma | 11.05 | 2.39 | 813 | 222.2 | 1.36 | 36.4 | 69.6 | 1.018 |
| 52 | SV-III-Delta | 11.03 | 2.53 | 844 | 216.0 | 1.45 | 31.6 | 69.5 | 1.024 |
| 53 | SV-III-Epsilon | 0.15 | 2.66 | 945 | 209.8 | 2.08 | 10.0 | 0.2 | 1.0 |
| 54 | SV-III-Zeta | 0.02 | 0.0 | 1126 | 203.6 | 0.0 | 2.0 | 0.0 | 1.0 |
| 55 | SV-III-Eta | 50.08 | 0.48 | 373 | 321.0 | 0.16 | 100.0 | 315.5 | 1.006 |
| 56 | SV-III-Theta | 50.0 | 0.61 | 404 | 314.8 | 0.25 | 96.6 | 315.0 | 1.012 |
| 57 | SV-III-Iota | 38.65 | 0.75 | 435 | 308.6 | 0.33 | 91.8 | 243.5 | 1.018 |
| 58 | SV-III-Kappa | 38.59 | 0.88 | 466 | 302.4 | 0.42 | 87.0 | 243.1 | 1.024 |
| 59 | SV-III-Lambda | 38.53 | 1.02 | 497 | 296.2 | 0.5 | 82.2 | 242.8 | 1.03 |
| 60 | SV-III-Mu | 38.47 | 1.15 | 528 | 290.0 | 0.58 | 77.4 | 242.4 | 1.0 |
| 61 | SV-III-Nu | 38.42 | 1.29 | 559 | 283.8 | 0.67 | 72.6 | 242.0 | 1.006 |
| 62 | SV-III-Xi | 38.36 | 1.42 | 590 | 277.6 | 0.76 | 67.8 | 241.6 | 1.012 |
| 63 | SV-III-Omicron | 38.3 | 1.56 | 621 | 271.4 | 0.84 | 63.0 | 241.3 | 1.018 |
| 64 | SV-III-Pi | 38.24 | 1.69 | 652 | 265.2 | 0.93 | 58.2 | 240.9 | 1.024 |
| 65 | SV-III-Rho | 38.18 | 1.83 | 683 | 259.0 | 1.01 | 53.4 | 240.5 | 1.03 |
| 66 | SV-III-Sigma | 38.12 | 1.96 | 714 | 252.8 | 1.1 | 48.6 | 240.2 | 1.0 |
| 67 | SV-III-Tau | 10.31 | 2.09 | 745 | 246.6 | 1.18 | 43.8 | 64.9 | 1.006 |
| 68 | SV-III-Upsilon | 10.29 | 2.23 | 776 | 240.4 | 1.27 | 39.0 | 64.8 | 1.012 |
| 69 | SV-III-Phi | 10.28 | 2.37 | 807 | 234.2 | 1.35 | 34.2 | 64.7 | 1.018 |
| 70 | SV-III-Chi | 10.26 | 2.5 | 838 | 228.0 | 1.44 | 29.4 | 64.6 | 1.024 |
| 71 | SV-III-Psi | 0.14 | 2.63 | 939 | 221.8 | 2.07 | 10.0 | 0.2 | 1.0 |
| 72 | SV-III-Omega | 0.02 | 0.0 | 1120 | 215.6 | 0.0 | 2.0 | 0.0 | 1.0 |
| 73 | SV-IV-Alfa | 46.57 | 0.45 | 367 | 333.0 | 0.15 | 99.2 | 293.4 | 1.006 |
| 74 | SV-IV-Beta | 46.49 | 0.59 | 398 | 326.8 | 0.23 | 94.4 | 292.9 | 1.012 |
| 75 | SV-IV-Gamma | 35.94 | 0.72 | 429 | 320.6 | 0.32 | 89.6 | 226.4 | 1.018 |
| 76 | SV-IV-Delta | 35.88 | 0.86 | 460 | 314.4 | 0.4 | 84.8 | 226.1 | 1.024 |
| 77 | SV-IV-Epsilon | 35.83 | 0.99 | 491 | 308.2 | 0.49 | 80.0 | 225.7 | 1.03 |
| 78 | SV-IV-Zeta | 35.77 | 1.12 | 522 | 302.0 | 0.57 | 75.2 | 225.4 | 1.0 |
| 79 | SV-IV-Eta | 35.71 | 1.26 | 553 | 295.8 | 0.66 | 70.4 | 225.0 | 1.006 |
| 80 | SV-IV-Theta | 35.66 | 1.4 | 584 | 289.6 | 0.74 | 65.6 | 224.6 | 1.012 |
| 81 | SV-IV-Iota | 35.6 | 1.53 | 615 | 283.4 | 0.82 | 60.8 | 224.3 | 1.018 |
| 82 | SV-IV-Kappa | 35.55 | 1.67 | 646 | 277.2 | 0.91 | 56.0 | 223.9 | 1.024 |
| 83 | SV-IV-Lambda | 35.49 | 1.8 | 677 | 271.0 | 1.0 | 51.2 | 223.6 | 1.03 |
| 84 | SV-IV-Mu | 35.43 | 1.94 | 708 | 264.8 | 1.08 | 46.4 | 223.2 | 1.0 |
| 85 | SV-IV-Nu | 9.58 | 2.07 | 739 | 258.6 | 1.17 | 41.6 | 60.4 | 1.006 |
| 86 | SV-IV-Xi | 9.57 | 2.21 | 770 | 252.4 | 1.25 | 36.8 | 60.3 | 1.012 |
| 87 | SV-IV-Omicron | 9.55 | 2.34 | 801 | 246.2 | 1.33 | 32.0 | 60.2 | 1.018 |
| 88 | SV-IV-Pi | 9.54 | 2.48 | 832 | 240.0 | 1.42 | 27.2 | 60.1 | 1.024 |
| 89 | SV-IV-Rho | 0.13 | 2.61 | 933 | 233.8 | 2.05 | 10.0 | 0.2 | 1.0 |
| 90 | SV-IV-Sigma | 0.01 | 0.0 | 1114 | 227.6 | 0.0 | 2.0 | 0.0 | 1.0 |
| 91 | SV-IV-Tau | 43.27 | 0.43 | 361 | 345.0 | 0.13 | 97.0 | 272.6 | 1.006 |
| 92 | SV-IV-Upsilon | 43.2 | 0.56 | 392 | 338.8 | 0.22 | 92.2 | 272.2 | 1.012 |
| 93 | SV-IV-Phi | 33.39 | 0.7 | 423 | 332.6 | 0.3 | 87.4 | 210.4 | 1.018 |
| 94 | SV-IV-Chi | 33.34 | 0.83 | 454 | 326.4 | 0.39 | 82.6 | 210.0 | 1.024 |
| 95 | SV-IV-Psi | 33.28 | 0.97 | 485 | 320.2 | 0.47 | 77.8 | 209.7 | 1.03 |
| 96 | SV-IV-Omega | 33.23 | 1.1 | 516 | 314.0 | 0.56 | 73.0 | 209.4 | 1.0 |
| 97 | SV-V-Alfa | 33.18 | 1.24 | 547 | 307.8 | 0.64 | 68.2 | 209.0 | 1.006 |
| 98 | SV-V-Beta | 33.12 | 1.37 | 578 | 301.6 | 0.73 | 63.4 | 208.7 | 1.012 |
| 99 | SV-V-Gamma | 33.07 | 1.51 | 609 | 295.4 | 0.81 | 58.6 | 208.3 | 1.018 |
| 100 | SV-V-Delta | 33.02 | 1.64 | 640 | 289.2 | 0.9 | 53.8 | 208.0 | 1.024 |
| 101 | SV-V-Epsilon | 32.96 | 1.78 | 671 | 283.0 | 0.98 | 49.0 | 207.7 | 1.03 |
| 102 | SV-V-Zeta | 32.91 | 1.91 | 702 | 276.8 | 1.07 | 44.2 | 207.3 | 1.0 |
| 103 | SV-V-Eta | 8.9 | 2.04 | 733 | 270.6 | 1.15 | 39.4 | 56.1 | 1.006 |
| 104 | SV-V-Theta | 8.88 | 2.18 | 764 | 264.4 | 1.24 | 34.6 | 56.0 | 1.012 |
| 105 | SV-V-Iota | 8.87 | 2.32 | 795 | 258.2 | 1.32 | 29.8 | 55.9 | 1.018 |
| 106 | SV-V-Kappa | 8.85 | 2.45 | 826 | 252.0 | 1.41 | 25.0 | 55.8 | 1.024 |
| 107 | SV-V-Lambda | 0.12 | 2.58 | 927 | 245.8 | 2.04 | 10.0 | 0.1 | 1.0 |
| 108 | SV-V-Mu | 0.01 | 0.0 | 1108 | 239.6 | 0.0 | 2.0 | 0.0 | 1.0 |
| 109 | SV-V-Nu | 40.17 | 0.4 | 355 | 357.0 | 0.12 | 94.8 | 253.1 | 1.006 |
| 110 | SV-V-Xi | 40.11 | 0.54 | 386 | 350.8 | 0.2 | 90.0 | 252.7 | 1.012 |
| 111 | SV-V-Omicron | 31.0 | 0.67 | 417 | 344.6 | 0.29 | 85.2 | 195.3 | 1.018 |
| 112 | SV-V-Pi | 30.95 | 0.81 | 448 | 338.4 | 0.37 | 80.4 | 195.0 | 1.024 |
| 113 | SV-V-Rho | 30.9 | 0.94 | 479 | 332.2 | 0.46 | 75.6 | 194.6 | 1.03 |
| 114 | SV-V-Sigma | 30.85 | 1.08 | 510 | 326.0 | 0.54 | 70.8 | 194.3 | 1.0 |
| 115 | SV-V-Tau | 30.79 | 1.21 | 541 | 319.8 | 0.63 | 66.0 | 194.0 | 1.006 |
| 116 | SV-V-Upsilon | 30.74 | 1.35 | 572 | 313.6 | 0.71 | 61.2 | 193.7 | 1.012 |
| 117 | SV-V-Phi | 30.69 | 1.48 | 603 | 307.4 | 0.8 | 56.4 | 193.4 | 1.018 |
| 118 | SV-V-Chi | 30.64 | 1.62 | 634 | 301.2 | 0.88 | 51.6 | 193.0 | 1.024 |


## Tabla 3 — Propiedades mecánicas, químicas y térmicas


| Nº | Nombre SV | Dureza SV (Mohs) | Resistencia física SV (MPa) | Coef. rozamiento SV | Flexibilidad SV (0-1) | Maleabilidad SV (0-1) | Resistencia oxidación SV (0-100) | Resistencia corrosión SV (0-100) | Resistencia térmica hasta cambio (°C) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SV-Alfa | 1.25 | 98 | 0.17 | 0.9 | 0.92 | 18.2 | 21.6 | 680 |
| 2 | SV-Beta | 1.4 | 116 | 0.18 | 0.86 | 0.88 | 22.4 | 25.2 | 710 |
| 3 | SV-Gamma | 2.52 | 134 | 0.2 | 0.83 | 0.84 | 26.6 | 28.8 | 740 |
| 4 | SV-Delta | 2.84 | 152 | 0.21 | 0.8 | 0.8 | 30.8 | 32.4 | 770 |
| 5 | SV-Epsilon | 3.16 | 170 | 0.22 | 0.76 | 0.76 | 35.0 | 36.0 | 800 |
| 6 | SV-Zeta | 3.48 | 188 | 0.23 | 0.72 | 0.72 | 39.2 | 39.6 | 830 |
| 7 | SV-Eta | 3.8 | 206 | 0.24 | 0.69 | 0.68 | 43.4 | 43.2 | 860 |
| 8 | SV-Theta | 4.12 | 224 | 0.26 | 0.66 | 0.64 | 47.6 | 46.8 | 890 |
| 9 | SV-Iota | 4.44 | 242 | 0.27 | 0.62 | 0.6 | 51.8 | 50.4 | 920 |
| 10 | SV-Kappa | 4.76 | 260 | 0.28 | 0.58 | 0.56 | 56.0 | 54.0 | 950 |
| 11 | SV-Lambda | 5.08 | 278 | 0.29 | 0.55 | 0.52 | 60.2 | 57.6 | 980 |
| 12 | SV-Mu | 5.4 | 296 | 0.3 | 0.52 | 0.48 | 64.4 | 61.2 | 1010 |
| 13 | SV-Nu | 5.3 | 314 | 0.32 | 0.48 | 0.24 | 68.6 | 64.8 | 1040 |
| 14 | SV-Xi | 5.48 | 332 | 0.33 | 0.44 | 0.22 | 72.8 | 68.4 | 1070 |
| 15 | SV-Omicron | 5.66 | 350 | 0.34 | 0.41 | 0.2 | 77.0 | 72.0 | 1100 |
| 16 | SV-Pi | 5.84 | 368 | 0.35 | 0.38 | 0.18 | 81.2 | 75.6 | 1130 |
| 17 | SV-Rho | 0.6 | 8 | 0.0 | 0.02 | 0.01 | 85.4 | 79.2 | 120 |
| 18 | SV-Sigma | 0.2 | 2 | 0.0 | 0.02 | 0.01 | 95.0 | 96.0 | -190 |
| 19 | SV-Tau | 1.27 | 106 | 0.17 | 0.88 | 0.91 | 20.7 | 23.7 | 720 |
| 20 | SV-Upsilon | 1.42 | 124 | 0.18 | 0.84 | 0.86 | 24.9 | 27.3 | 750 |
| 21 | SV-Phi | 2.55 | 142 | 0.2 | 0.81 | 0.83 | 29.1 | 30.9 | 780 |
| 22 | SV-Chi | 2.87 | 160 | 0.21 | 0.78 | 0.79 | 33.3 | 34.5 | 810 |
| 23 | SV-Psi | 3.19 | 178 | 0.22 | 0.74 | 0.74 | 37.5 | 38.1 | 840 |
| 24 | SV-Omega | 3.51 | 196 | 0.23 | 0.7 | 0.7 | 41.7 | 41.7 | 870 |
| 25 | SV-II-Alfa | 3.83 | 214 | 0.24 | 0.67 | 0.67 | 45.9 | 45.3 | 900 |
| 26 | SV-II-Beta | 4.15 | 232 | 0.26 | 0.64 | 0.62 | 50.1 | 48.9 | 930 |
| 27 | SV-II-Gamma | 4.47 | 250 | 0.27 | 0.6 | 0.59 | 54.3 | 52.5 | 960 |
| 28 | SV-II-Delta | 4.79 | 268 | 0.28 | 0.56 | 0.55 | 58.5 | 56.1 | 990 |
| 29 | SV-II-Epsilon | 5.11 | 286 | 0.29 | 0.53 | 0.51 | 62.7 | 59.7 | 1020 |
| 30 | SV-II-Zeta | 5.43 | 304 | 0.3 | 0.49 | 0.47 | 66.9 | 63.3 | 1050 |
| 31 | SV-II-Eta | 5.28 | 322 | 0.32 | 0.46 | 0.23 | 71.1 | 66.9 | 1080 |
| 32 | SV-II-Theta | 5.46 | 340 | 0.33 | 0.42 | 0.21 | 75.3 | 70.5 | 1110 |
| 33 | SV-II-Iota | 5.64 | 358 | 0.34 | 0.39 | 0.19 | 79.5 | 74.1 | 1140 |
| 34 | SV-II-Kappa | 5.82 | 376 | 0.35 | 0.35 | 0.17 | 83.7 | 77.7 | 1170 |
| 35 | SV-II-Lambda | 0.6 | 8 | 0.0 | 0.02 | 0.01 | 87.9 | 81.3 | 135 |
| 36 | SV-II-Mu | 0.2 | 2 | 0.0 | 0.02 | 0.01 | 95.0 | 96.0 | -185 |
| 37 | SV-II-Nu | 1.29 | 114 | 0.17 | 0.86 | 0.89 | 23.2 | 25.8 | 760 |
| 38 | SV-II-Xi | 1.44 | 132 | 0.18 | 0.82 | 0.85 | 27.4 | 29.4 | 790 |
| 39 | SV-II-Omicron | 2.58 | 150 | 0.2 | 0.79 | 0.81 | 31.6 | 33.0 | 820 |
| 40 | SV-II-Pi | 2.9 | 168 | 0.21 | 0.76 | 0.77 | 35.8 | 36.6 | 850 |
| 41 | SV-II-Rho | 3.22 | 186 | 0.22 | 0.72 | 0.73 | 40.0 | 40.2 | 880 |
| 42 | SV-II-Sigma | 3.54 | 204 | 0.23 | 0.68 | 0.69 | 44.2 | 43.8 | 910 |
| 43 | SV-II-Tau | 3.86 | 222 | 0.24 | 0.65 | 0.65 | 48.4 | 47.4 | 940 |
| 44 | SV-II-Upsilon | 4.18 | 240 | 0.26 | 0.61 | 0.61 | 52.6 | 51.0 | 970 |
| 45 | SV-II-Phi | 4.5 | 258 | 0.27 | 0.58 | 0.57 | 56.8 | 54.6 | 1000 |
| 46 | SV-II-Chi | 4.82 | 276 | 0.28 | 0.54 | 0.53 | 61.0 | 58.2 | 1030 |
| 47 | SV-II-Psi | 5.14 | 294 | 0.29 | 0.51 | 0.49 | 65.2 | 61.8 | 1060 |
| 48 | SV-II-Omega | 5.46 | 312 | 0.3 | 0.48 | 0.45 | 69.4 | 65.4 | 1090 |
| 49 | SV-III-Alfa | 5.26 | 330 | 0.32 | 0.44 | 0.23 | 73.6 | 69.0 | 1120 |
| 50 | SV-III-Beta | 5.44 | 348 | 0.33 | 0.4 | 0.2 | 77.8 | 72.6 | 1150 |
| 51 | SV-III-Gamma | 5.62 | 366 | 0.34 | 0.37 | 0.18 | 82.0 | 76.2 | 1180 |
| 52 | SV-III-Delta | 5.8 | 384 | 0.35 | 0.34 | 0.16 | 86.2 | 79.8 | 1210 |
| 53 | SV-III-Epsilon | 0.6 | 8 | 0.0 | 0.02 | 0.01 | 90.4 | 83.4 | 150 |
| 54 | SV-III-Zeta | 0.2 | 2 | 0.0 | 0.02 | 0.01 | 95.0 | 96.0 | -180 |
| 55 | SV-III-Eta | 1.31 | 122 | 0.17 | 0.84 | 0.88 | 25.7 | 27.9 | 800 |
| 56 | SV-III-Theta | 1.46 | 140 | 0.18 | 0.8 | 0.83 | 29.9 | 31.5 | 830 |
| 57 | SV-III-Iota | 2.61 | 158 | 0.2 | 0.77 | 0.8 | 34.1 | 35.1 | 860 |
| 58 | SV-III-Kappa | 2.93 | 176 | 0.21 | 0.74 | 0.76 | 38.3 | 38.7 | 890 |
| 59 | SV-III-Lambda | 3.25 | 194 | 0.22 | 0.7 | 0.71 | 42.5 | 42.3 | 920 |
| 60 | SV-III-Mu | 3.57 | 212 | 0.23 | 0.67 | 0.67 | 46.7 | 45.9 | 950 |
| 61 | SV-III-Nu | 3.89 | 230 | 0.24 | 0.63 | 0.64 | 50.9 | 49.5 | 980 |
| 62 | SV-III-Xi | 4.21 | 248 | 0.26 | 0.59 | 0.59 | 55.1 | 53.1 | 1010 |
| 63 | SV-III-Omicron | 4.53 | 266 | 0.27 | 0.56 | 0.56 | 59.3 | 56.7 | 1040 |
| 64 | SV-III-Pi | 4.85 | 284 | 0.28 | 0.52 | 0.52 | 63.5 | 60.3 | 1070 |
| 65 | SV-III-Rho | 5.17 | 302 | 0.29 | 0.49 | 0.48 | 67.7 | 63.9 | 1100 |
| 66 | SV-III-Sigma | 5.49 | 320 | 0.3 | 0.46 | 0.44 | 71.9 | 67.5 | 1130 |
| 67 | SV-III-Tau | 5.24 | 338 | 0.32 | 0.42 | 0.22 | 76.1 | 71.1 | 1160 |
| 68 | SV-III-Upsilon | 5.42 | 356 | 0.33 | 0.38 | 0.2 | 80.3 | 74.7 | 1190 |
| 69 | SV-III-Phi | 5.6 | 374 | 0.34 | 0.35 | 0.17 | 84.5 | 78.3 | 1220 |
| 70 | SV-III-Chi | 5.78 | 392 | 0.35 | 0.32 | 0.15 | 88.7 | 81.9 | 1250 |
| 71 | SV-III-Psi | 0.6 | 8 | 0.0 | 0.02 | 0.01 | 92.9 | 85.5 | 165 |
| 72 | SV-III-Omega | 0.2 | 2 | 0.0 | 0.02 | 0.01 | 95.0 | 96.0 | -175 |
| 73 | SV-IV-Alfa | 1.33 | 130 | 0.17 | 0.82 | 0.86 | 28.2 | 30.0 | 840 |
| 74 | SV-IV-Beta | 1.48 | 148 | 0.18 | 0.79 | 0.82 | 32.4 | 33.6 | 870 |
| 75 | SV-IV-Gamma | 2.64 | 166 | 0.2 | 0.75 | 0.78 | 36.6 | 37.2 | 900 |
| 76 | SV-IV-Delta | 2.96 | 184 | 0.21 | 0.72 | 0.74 | 40.8 | 40.8 | 930 |
| 77 | SV-IV-Epsilon | 3.28 | 202 | 0.22 | 0.68 | 0.7 | 45.0 | 44.4 | 960 |
| 78 | SV-IV-Zeta | 3.6 | 220 | 0.23 | 0.65 | 0.66 | 49.2 | 48.0 | 990 |
| 79 | SV-IV-Eta | 3.92 | 238 | 0.24 | 0.61 | 0.62 | 53.4 | 51.6 | 1020 |
| 80 | SV-IV-Theta | 4.24 | 256 | 0.26 | 0.58 | 0.58 | 57.6 | 55.2 | 1050 |
| 81 | SV-IV-Iota | 4.56 | 274 | 0.27 | 0.54 | 0.54 | 61.8 | 58.8 | 1080 |
| 82 | SV-IV-Kappa | 4.88 | 292 | 0.28 | 0.51 | 0.5 | 66.0 | 62.4 | 1110 |
| 83 | SV-IV-Lambda | 5.2 | 310 | 0.29 | 0.47 | 0.46 | 70.2 | 66.0 | 1140 |
| 84 | SV-IV-Mu | 5.52 | 328 | 0.3 | 0.43 | 0.42 | 74.4 | 69.6 | 1170 |
| 85 | SV-IV-Nu | 5.22 | 346 | 0.32 | 0.4 | 0.21 | 78.6 | 73.2 | 1200 |
| 86 | SV-IV-Xi | 5.4 | 364 | 0.33 | 0.36 | 0.19 | 82.8 | 76.8 | 1230 |
| 87 | SV-IV-Omicron | 5.58 | 382 | 0.34 | 0.33 | 0.17 | 87.0 | 80.4 | 1260 |
| 88 | SV-IV-Pi | 5.76 | 400 | 0.35 | 0.29 | 0.14 | 91.2 | 84.0 | 1290 |
| 89 | SV-IV-Rho | 0.6 | 8 | 0.0 | 0.02 | 0.01 | 95.4 | 87.6 | 180 |
| 90 | SV-IV-Sigma | 0.2 | 2 | 0.0 | 0.02 | 0.01 | 95.0 | 96.0 | -170 |
| 91 | SV-IV-Tau | 1.35 | 138 | 0.17 | 0.8 | 0.85 | 30.7 | 32.1 | 880 |
| 92 | SV-IV-Upsilon | 1.5 | 156 | 0.18 | 0.77 | 0.81 | 34.9 | 35.7 | 910 |
| 93 | SV-IV-Phi | 2.67 | 174 | 0.2 | 0.73 | 0.77 | 39.1 | 39.3 | 940 |
| 94 | SV-IV-Chi | 2.99 | 192 | 0.21 | 0.7 | 0.73 | 43.3 | 42.9 | 970 |
| 95 | SV-IV-Psi | 3.31 | 210 | 0.22 | 0.66 | 0.69 | 47.5 | 46.5 | 1000 |
| 96 | SV-IV-Omega | 3.63 | 228 | 0.23 | 0.62 | 0.65 | 51.7 | 50.1 | 1030 |
| 97 | SV-V-Alfa | 3.95 | 246 | 0.24 | 0.59 | 0.61 | 55.9 | 53.7 | 1060 |
| 98 | SV-V-Beta | 4.27 | 264 | 0.26 | 0.56 | 0.57 | 60.1 | 57.3 | 1090 |
| 99 | SV-V-Gamma | 4.59 | 282 | 0.27 | 0.52 | 0.53 | 64.3 | 60.9 | 1120 |
| 100 | SV-V-Delta | 4.91 | 300 | 0.28 | 0.48 | 0.49 | 68.5 | 64.5 | 1150 |
| 101 | SV-V-Epsilon | 5.23 | 318 | 0.29 | 0.45 | 0.45 | 72.7 | 68.1 | 1180 |
| 102 | SV-V-Zeta | 5.55 | 336 | 0.3 | 0.42 | 0.41 | 76.9 | 71.7 | 1210 |
| 103 | SV-V-Eta | 5.2 | 354 | 0.32 | 0.38 | 0.2 | 81.1 | 75.3 | 1240 |
| 104 | SV-V-Theta | 5.38 | 372 | 0.33 | 0.34 | 0.18 | 85.3 | 78.9 | 1270 |
| 105 | SV-V-Iota | 5.56 | 390 | 0.34 | 0.31 | 0.16 | 89.5 | 82.5 | 1300 |
| 106 | SV-V-Kappa | 5.74 | 408 | 0.35 | 0.28 | 0.13 | 93.7 | 86.1 | 1330 |
| 107 | SV-V-Lambda | 0.6 | 8 | 0.0 | 0.02 | 0.01 | 97.9 | 89.7 | 195 |
| 108 | SV-V-Mu | 0.2 | 2 | 0.0 | 0.02 | 0.01 | 95.0 | 96.0 | -165 |
| 109 | SV-V-Nu | 1.37 | 146 | 0.17 | 0.78 | 0.83 | 33.2 | 34.2 | 920 |
| 110 | SV-V-Xi | 1.52 | 164 | 0.18 | 0.74 | 0.79 | 37.4 | 37.8 | 950 |
| 111 | SV-V-Omicron | 2.7 | 182 | 0.2 | 0.71 | 0.75 | 41.6 | 41.4 | 980 |
| 112 | SV-V-Pi | 3.02 | 200 | 0.21 | 0.68 | 0.71 | 45.8 | 45.0 | 1010 |
| 113 | SV-V-Rho | 3.34 | 218 | 0.22 | 0.64 | 0.67 | 50.0 | 48.6 | 1040 |
| 114 | SV-V-Sigma | 3.66 | 236 | 0.23 | 0.6 | 0.63 | 54.2 | 52.2 | 1070 |
| 115 | SV-V-Tau | 3.98 | 254 | 0.24 | 0.57 | 0.59 | 58.4 | 55.8 | 1100 |
| 116 | SV-V-Upsilon | 4.3 | 272 | 0.26 | 0.54 | 0.55 | 62.6 | 59.4 | 1130 |
| 117 | SV-V-Phi | 4.62 | 290 | 0.27 | 0.5 | 0.51 | 66.8 | 63.0 | 1160 |
| 118 | SV-V-Chi | 4.94 | 308 | 0.28 | 0.46 | 0.47 | 71.0 | 66.6 | 1190 |


## Tabla 4 — Volumen, estabilidad, radiactividad, isótopos y usos


| Nº | Nombre SV | Volumen atómico SV (Å³) | Intervalo térmico estable SV (°C) | Nivel radiactivo SV (0-100) | Nº isótopos SV | Función estructural SV | Aplicación científica SV | Aplicación aeroespacial/cosmológica SV | Aplicación médica SV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SV-Alfa | 96.97 | -273 a 680 | 45.0 | 6 | apertura alcalina de persistencia superperiódica del periodo 8 | electrónica extrema | estructura densa | implante estructural SV |
| 2 | SV-Beta | 90.78 | -273 a 710 | 45.5 | 8 | cierre s de confinamiento basal del periodo 8 | electrónica extrema | estructura densa | implante estructural SV |
| 3 | SV-Gamma | 84.85 | -273 a 740 | 46.0 | 8 | apertura de subbloque extendido del periodo 8 | aleaciones SV | estructura densa | implante estructural SV |
| 4 | SV-Delta | 79.19 | -273 a 770 | 46.4 | 9 | segundo anclaje de frontera extendida del periodo 8 | aleaciones SV | estructura densa | implante estructural SV |
| 5 | SV-Epsilon | 73.79 | -273 a 800 | 46.9 | 10 | crecimiento de confinamiento lateral del periodo 8 | aleaciones SV | estructura densa | implante estructural SV |
| 6 | SV-Zeta | 68.64 | -273 a 830 | 47.4 | 5 | consolidación intermedia de frontera del periodo 8 | aleaciones SV | estructura densa | implante estructural SV |
| 7 | SV-Eta | 63.74 | -273 a 860 | 47.9 | 6 | semilleno estructural primario del periodo 8 | aleaciones SV | estructura densa | implante estructural SV |
| 8 | SV-Theta | 59.07 | -273 a 890 | 48.4 | 8 | isla local de estabilidad relativa del periodo 8 | aleaciones SV | estructura densa | implante estructural SV |
| 9 | SV-Iota | 54.64 | -273 a 920 | 48.8 | 8 | transición posisla de identidad del periodo 8 | aleaciones SV | estructura densa | implante estructural SV |
| 10 | SV-Kappa | 50.44 | -273 a 950 | 49.3 | 9 | persistencia tardía de subbloque del periodo 8 | aleaciones SV | estructura densa | implante estructural SV |
| 11 | SV-Lambda | 46.45 | -273 a 980 | 49.8 | 10 | frontera metálica tardía del periodo 8 | aleaciones SV | estructura densa | implante estructural SV |
| 12 | SV-Mu | 42.68 | -273 a 1010 | 50.3 | 5 | cierre medio de subbloque del periodo 8 | aleaciones SV | estructura densa | implante estructural SV |
| 13 | SV-Nu | 39.13 | -273 a 1040 | 50.8 | 6 | transición covalente pesada del periodo 8 | material funcional pesado | blindaje/radiación | teragnóstico pesado |
| 14 | SV-Xi | 35.77 | -273 a 1070 | 51.2 | 7 | estabilización tetravalente estructural del periodo 8 | material funcional pesado | blindaje/radiación | teragnóstico pesado |
| 15 | SV-Omicron | 32.61 | -273 a 1100 | 51.7 | 8 | frontera pnictógena ampliada del periodo 8 | material funcional pesado | blindaje/radiación | teragnóstico pesado |
| 16 | SV-Pi | 29.65 | -273 a 1130 | 52.2 | 9 | cierre calcógeno estructural del periodo 8 | material funcional pesado | blindaje/radiación | teragnóstico pesado |
| 17 | SV-Rho | 26.87 | -273 a 120 | 52.7 | 10 | clase halógena superpesada del periodo 8 | química reactiva extrema | blindaje/radiación | teragnóstico pesado |
| 18 | SV-Sigma | 24.27 | -273 a -190 | 53.2 | 6 | cierre noble superpesado del periodo 8 | trazador inerte denso | blindaje/radiación | teragnóstico pesado |
| 19 | SV-Tau | 109.74 | -273 a 720 | 54.3 | 7 | apertura alcalina de persistencia superperiódica del periodo 9 | electrónica extrema | estructura densa | implante estructural SV |
| 20 | SV-Upsilon | 103.01 | -273 a 750 | 54.8 | 9 | cierre s de confinamiento basal del periodo 9 | electrónica extrema | estructura densa | implante estructural SV |
| 21 | SV-Phi | 96.56 | -273 a 780 | 55.3 | 9 | apertura de subbloque extendido del periodo 9 | aleaciones SV | estructura densa | implante estructural SV |
| 22 | SV-Chi | 90.38 | -273 a 810 | 55.8 | 10 | segundo anclaje de frontera extendida del periodo 9 | aleaciones SV | estructura densa | implante estructural SV |
| 23 | SV-Psi | 84.48 | -273 a 840 | 56.3 | 11 | crecimiento de confinamiento lateral del periodo 9 | aleaciones SV | estructura densa | implante estructural SV |
| 24 | SV-Omega | 78.84 | -273 a 870 | 56.7 | 6 | consolidación intermedia de frontera del periodo 9 | aleaciones SV | estructura densa | implante estructural SV |
| 25 | SV-II-Alfa | 73.45 | -273 a 900 | 57.2 | 7 | semilleno estructural primario del periodo 9 | aleaciones SV | estructura densa | implante estructural SV |
| 26 | SV-II-Beta | 68.32 | -273 a 930 | 57.7 | 9 | isla local de estabilidad relativa del periodo 9 | aleaciones SV | estructura densa | implante estructural SV |
| 27 | SV-II-Gamma | 63.43 | -273 a 960 | 58.2 | 9 | transición posisla de identidad del periodo 9 | aleaciones SV | estructura densa | implante estructural SV |
| 28 | SV-II-Delta | 58.78 | -273 a 990 | 58.7 | 10 | persistencia tardía de subbloque del periodo 9 | aleaciones SV | estructura densa | implante estructural SV |
| 29 | SV-II-Epsilon | 54.36 | -273 a 1020 | 59.1 | 11 | frontera metálica tardía del periodo 9 | aleaciones SV | estructura densa | implante estructural SV |
| 30 | SV-II-Zeta | 50.17 | -273 a 1050 | 59.6 | 6 | cierre medio de subbloque del periodo 9 | aleaciones SV | estructura densa | implante estructural SV |
| 31 | SV-II-Eta | 46.2 | -273 a 1080 | 60.1 | 7 | transición covalente pesada del periodo 9 | material funcional pesado | blindaje/radiación | teragnóstico pesado |
| 32 | SV-II-Theta | 42.45 | -273 a 1110 | 60.6 | 8 | estabilización tetravalente estructural del periodo 9 | material funcional pesado | blindaje/radiación | teragnóstico pesado |
| 33 | SV-II-Iota | 38.9 | -273 a 1140 | 61.1 | 9 | frontera pnictógena ampliada del periodo 9 | material funcional pesado | blindaje/radiación | teragnóstico pesado |
| 34 | SV-II-Kappa | 35.56 | -273 a 1170 | 61.5 | 10 | cierre calcógeno estructural del periodo 9 | material funcional pesado | blindaje/radiación | teragnóstico pesado |
| 35 | SV-II-Lambda | 32.42 | -273 a 135 | 62.0 | 11 | clase halógena superpesada del periodo 9 | química reactiva extrema | blindaje/radiación | teragnóstico pesado |
| 36 | SV-II-Mu | 29.46 | -273 a -185 | 62.5 | 7 | cierre noble superpesado del periodo 9 | trazador inerte denso | blindaje/radiación | teragnóstico pesado |
| 37 | SV-II-Nu | 123.58 | -273 a 760 | 63.7 | 8 | apertura alcalina de persistencia superperiódica del periodo 10 | electrónica extrema | estructura densa | implante estructural SV |
| 38 | SV-II-Xi | 116.29 | -273 a 790 | 64.2 | 10 | cierre s de confinamiento basal del periodo 10 | electrónica extrema | estructura densa | implante estructural SV |
| 39 | SV-II-Omicron | 109.3 | -273 a 820 | 64.6 | 10 | apertura de subbloque extendido del periodo 10 | aleaciones SV | estructura densa | implante estructural SV |
| 40 | SV-II-Pi | 102.58 | -273 a 850 | 65.1 | 11 | segundo anclaje de frontera extendida del periodo 10 | aleaciones SV | estructura densa | implante estructural SV |
| 41 | SV-II-Rho | 96.15 | -273 a 880 | 65.6 | 12 | crecimiento de confinamiento lateral del periodo 10 | aleaciones SV | estructura densa | implante estructural SV |
| 42 | SV-II-Sigma | 90.0 | -273 a 910 | 66.1 | 7 | consolidación intermedia de frontera del periodo 10 | aleaciones SV | estructura densa | implante estructural SV |
| 43 | SV-II-Tau | 84.11 | -273 a 940 | 66.6 | 8 | semilleno estructural primario del periodo 10 | aleaciones SV | estructura densa | implante estructural SV |
| 44 | SV-II-Upsilon | 78.48 | -273 a 970 | 67.0 | 10 | isla local de estabilidad relativa del periodo 10 | aleaciones SV | estructura densa | implante estructural SV |
| 45 | SV-II-Phi | 73.11 | -273 a 1000 | 67.5 | 10 | transición posisla de identidad del periodo 10 | aleaciones SV | estructura densa | implante estructural SV |
| 46 | SV-II-Chi | 68.0 | -273 a 1030 | 68.0 | 11 | persistencia tardía de subbloque del periodo 10 | aleaciones SV | estructura densa | implante estructural SV |
| 47 | SV-II-Psi | 63.12 | -273 a 1060 | 68.5 | 12 | frontera metálica tardía del periodo 10 | aleaciones SV | estructura densa | implante estructural SV |
| 48 | SV-II-Omega | 58.49 | -273 a 1090 | 69.0 | 7 | cierre medio de subbloque del periodo 10 | aleaciones SV | estructura densa | implante estructural SV |
| 49 | SV-III-Alfa | 54.08 | -273 a 1120 | 69.4 | 8 | transición covalente pesada del periodo 10 | material funcional pesado | blindaje/radiación | teragnóstico pesado |
| 50 | SV-III-Beta | 49.91 | -273 a 1150 | 69.9 | 9 | estabilización tetravalente estructural del periodo 10 | material funcional pesado | blindaje/radiación | teragnóstico pesado |
| 51 | SV-III-Gamma | 45.95 | -273 a 1180 | 70.4 | 10 | frontera pnictógena ampliada del periodo 10 | material funcional pesado | blindaje/radiación | teragnóstico pesado |
| 52 | SV-III-Delta | 42.21 | -273 a 1210 | 70.9 | 11 | cierre calcógeno estructural del periodo 10 | material funcional pesado | blindaje/radiación | teragnóstico pesado |
| 53 | SV-III-Epsilon | 38.68 | -273 a 150 | 71.4 | 12 | clase halógena superpesada del periodo 10 | química reactiva extrema | blindaje/radiación | teragnóstico pesado |
| 54 | SV-III-Zeta | 35.35 | -273 a -180 | 71.8 | 8 | cierre noble superpesado del periodo 10 | trazador inerte denso | blindaje/radiación | teragnóstico pesado |
| 55 | SV-III-Eta | 138.55 | -273 a 800 | 73.0 | 9 | apertura alcalina de persistencia superperiódica del periodo 11 | electrónica extrema | estructura densa | implante estructural SV |
| 56 | SV-III-Theta | 130.68 | -273 a 830 | 73.5 | 11 | cierre s de confinamiento basal del periodo 11 | electrónica extrema | estructura densa | implante estructural SV |
| 57 | SV-III-Iota | 123.11 | -273 a 860 | 74.0 | 11 | apertura de subbloque extendido del periodo 11 | aleaciones SV | estructura densa | implante estructural SV |
| 58 | SV-III-Kappa | 115.83 | -273 a 890 | 74.5 | 12 | segundo anclaje de frontera extendida del periodo 11 | aleaciones SV | estructura densa | implante estructural SV |
| 59 | SV-III-Lambda | 108.85 | -273 a 920 | 74.9 | 13 | crecimiento de confinamiento lateral del periodo 11 | aleaciones SV | estructura densa | implante estructural SV |
| 60 | SV-III-Mu | 102.16 | -273 a 950 | 75.4 | 8 | consolidación intermedia de frontera del periodo 11 | aleaciones SV | estructura densa | implante estructural SV |
| 61 | SV-III-Nu | 95.75 | -273 a 980 | 75.9 | 9 | semilleno estructural primario del periodo 11 | aleaciones SV | estructura densa | implante estructural SV |
| 62 | SV-III-Xi | 89.61 | -273 a 1010 | 76.4 | 11 | isla local de estabilidad relativa del periodo 11 | aleaciones SV | estructura densa | implante estructural SV |
| 63 | SV-III-Omicron | 83.74 | -273 a 1040 | 76.9 | 11 | transición posisla de identidad del periodo 11 | aleaciones SV | estructura densa | implante estructural SV |
| 64 | SV-III-Pi | 78.13 | -273 a 1070 | 77.3 | 12 | persistencia tardía de subbloque del periodo 11 | aleaciones SV | estructura densa | implante estructural SV |
| 65 | SV-III-Rho | 72.78 | -273 a 1100 | 77.8 | 13 | frontera metálica tardía del periodo 11 | aleaciones SV | estructura densa | implante estructural SV |
| 66 | SV-III-Sigma | 67.67 | -273 a 1130 | 78.3 | 8 | cierre medio de subbloque del periodo 11 | aleaciones SV | estructura densa | implante estructural SV |
| 67 | SV-III-Tau | 62.82 | -273 a 1160 | 78.8 | 9 | transición covalente pesada del periodo 11 | material funcional pesado | blindaje/radiación | teragnóstico pesado |
| 68 | SV-III-Upsilon | 58.2 | -273 a 1190 | 79.3 | 10 | estabilización tetravalente estructural del periodo 11 | material funcional pesado | blindaje/radiación | teragnóstico pesado |
| 69 | SV-III-Phi | 53.81 | -273 a 1220 | 79.7 | 11 | frontera pnictógena ampliada del periodo 11 | material funcional pesado | blindaje/radiación | teragnóstico pesado |
| 70 | SV-III-Chi | 49.65 | -273 a 1250 | 80.2 | 12 | cierre calcógeno estructural del periodo 11 | material funcional pesado | blindaje/radiación | radiotrazador SV |
| 71 | SV-III-Psi | 45.71 | -273 a 165 | 80.7 | 13 | clase halógena superpesada del periodo 11 | química reactiva extrema | blindaje/radiación | radiotrazador SV |
| 72 | SV-III-Omega | 41.98 | -273 a -175 | 81.2 | 9 | cierre noble superpesado del periodo 11 | trazador inerte denso | blindaje/radiación | radiotrazador SV |
| 73 | SV-IV-Alfa | 154.68 | -273 a 840 | 82.4 | 10 | apertura alcalina de persistencia superperiódica del periodo 12 | electrónica extrema | estructura densa | radiotrazador SV |
| 74 | SV-IV-Beta | 146.2 | -273 a 870 | 82.8 | 12 | cierre s de confinamiento basal del periodo 12 | electrónica extrema | estructura densa | radiotrazador SV |
| 75 | SV-IV-Gamma | 138.03 | -273 a 900 | 83.3 | 12 | apertura de subbloque extendido del periodo 12 | aleaciones SV | estructura densa | radiotrazador SV |
| 76 | SV-IV-Delta | 130.18 | -273 a 930 | 83.8 | 13 | segundo anclaje de frontera extendida del periodo 12 | aleaciones SV | estructura densa | radiotrazador SV |
| 77 | SV-IV-Epsilon | 122.63 | -273 a 960 | 84.3 | 14 | crecimiento de confinamiento lateral del periodo 12 | aleaciones SV | estructura densa | radiotrazador SV |
| 78 | SV-IV-Zeta | 115.37 | -273 a 990 | 84.8 | 9 | consolidación intermedia de frontera del periodo 12 | aleaciones SV | estructura densa | radiotrazador SV |
| 79 | SV-IV-Eta | 108.41 | -273 a 1020 | 85.2 | 10 | semilleno estructural primario del periodo 12 | aleaciones SV | estructura densa | radiotrazador SV |
| 80 | SV-IV-Theta | 101.74 | -273 a 1050 | 85.7 | 12 | isla local de estabilidad relativa del periodo 12 | aleaciones SV | estructura densa | radiotrazador SV |
| 81 | SV-IV-Iota | 95.34 | -273 a 1080 | 86.2 | 12 | transición posisla de identidad del periodo 12 | aleaciones SV | estructura densa | radiotrazador SV |
| 82 | SV-IV-Kappa | 89.22 | -273 a 1110 | 86.7 | 13 | persistencia tardía de subbloque del periodo 12 | aleaciones SV | estructura densa | radiotrazador SV |
| 83 | SV-IV-Lambda | 83.37 | -273 a 1140 | 87.2 | 14 | frontera metálica tardía del periodo 12 | aleaciones SV | estructura densa | radiotrazador SV |
| 84 | SV-IV-Mu | 77.78 | -273 a 1170 | 87.6 | 9 | cierre medio de subbloque del periodo 12 | aleaciones SV | estructura densa | radiotrazador SV |
| 85 | SV-IV-Nu | 72.44 | -273 a 1200 | 88.1 | 10 | transición covalente pesada del periodo 12 | material funcional pesado | blindaje/radiación | radiotrazador SV |
| 86 | SV-IV-Xi | 67.35 | -273 a 1230 | 88.6 | 11 | estabilización tetravalente estructural del periodo 12 | material funcional pesado | blindaje/radiación | radiotrazador SV |
| 87 | SV-IV-Omicron | 62.51 | -273 a 1260 | 89.1 | 12 | frontera pnictógena ampliada del periodo 12 | material funcional pesado | blindaje/radiación | radiotrazador SV |
| 88 | SV-IV-Pi | 57.91 | -273 a 1290 | 89.6 | 13 | cierre calcógeno estructural del periodo 12 | material funcional pesado | blindaje/radiación | radiotrazador SV |
| 89 | SV-IV-Rho | 53.53 | -273 a 180 | 90.0 | 14 | clase halógena superpesada del periodo 12 | química reactiva extrema | blindaje/radiación | radiotrazador SV |
| 90 | SV-IV-Sigma | 49.39 | -273 a -170 | 90.5 | 10 | cierre noble superpesado del periodo 12 | trazador inerte denso | blindaje/radiación | radiotrazador SV |
| 91 | SV-IV-Tau | 172.01 | -273 a 880 | 91.7 | 11 | apertura alcalina de persistencia superperiódica del periodo 13 | electrónica extrema | estructura densa | radiotrazador SV |
| 92 | SV-IV-Upsilon | 162.9 | -273 a 910 | 92.2 | 13 | cierre s de confinamiento basal del periodo 13 | electrónica extrema | estructura densa | radiotrazador SV |
| 93 | SV-IV-Phi | 154.12 | -273 a 940 | 92.7 | 13 | apertura de subbloque extendido del periodo 13 | aleaciones SV | estructura densa | radiotrazador SV |
| 94 | SV-IV-Chi | 145.66 | -273 a 970 | 93.1 | 14 | segundo anclaje de frontera extendida del periodo 13 | aleaciones SV | estructura densa | radiotrazador SV |
| 95 | SV-IV-Psi | 137.52 | -273 a 1000 | 93.6 | 15 | crecimiento de confinamiento lateral del periodo 13 | aleaciones SV | estructura densa | radiotrazador SV |
| 96 | SV-IV-Omega | 129.68 | -273 a 1030 | 94.1 | 10 | consolidación intermedia de frontera del periodo 13 | aleaciones SV | estructura densa | radiotrazador SV |
| 97 | SV-V-Alfa | 122.15 | -273 a 1060 | 94.6 | 11 | semilleno estructural primario del periodo 13 | aleaciones SV | estructura densa | radiotrazador SV |
| 98 | SV-V-Beta | 114.92 | -273 a 1090 | 95.1 | 13 | isla local de estabilidad relativa del periodo 13 | aleaciones SV | estructura densa | radiotrazador SV |
| 99 | SV-V-Gamma | 107.97 | -273 a 1120 | 95.5 | 13 | transición posisla de identidad del periodo 13 | aleaciones SV | estructura densa | radiotrazador SV |
| 100 | SV-V-Delta | 101.32 | -273 a 1150 | 96.0 | 14 | persistencia tardía de subbloque del periodo 13 | aleaciones SV | estructura densa | radiotrazador SV |
| 101 | SV-V-Epsilon | 94.94 | -273 a 1180 | 96.5 | 15 | frontera metálica tardía del periodo 13 | aleaciones SV | estructura densa | radiotrazador SV |
| 102 | SV-V-Zeta | 88.84 | -273 a 1210 | 97.0 | 10 | cierre medio de subbloque del periodo 13 | aleaciones SV | estructura densa | radiotrazador SV |
| 103 | SV-V-Eta | 83.0 | -273 a 1240 | 97.5 | 11 | transición covalente pesada del periodo 13 | material funcional pesado | blindaje/radiación | radiotrazador SV |
| 104 | SV-V-Theta | 77.42 | -273 a 1270 | 97.9 | 12 | estabilización tetravalente estructural del periodo 13 | material funcional pesado | blindaje/radiación | radiotrazador SV |
| 105 | SV-V-Iota | 72.1 | -273 a 1300 | 98.4 | 13 | frontera pnictógena ampliada del periodo 13 | material funcional pesado | blindaje/radiación | radiotrazador SV |
| 106 | SV-V-Kappa | 67.03 | -273 a 1330 | 98.9 | 14 | cierre calcógeno estructural del periodo 13 | material funcional pesado | blindaje/radiación | radiotrazador SV |
| 107 | SV-V-Lambda | 62.21 | -273 a 195 | 99.4 | 15 | clase halógena superpesada del periodo 13 | química reactiva extrema | blindaje/radiación | radiotrazador SV |
| 108 | SV-V-Mu | 57.62 | -273 a -165 | 99.9 | 11 | cierre noble superpesado del periodo 13 | trazador inerte denso | blindaje/radiación | radiotrazador SV |
| 109 | SV-V-Nu | 190.59 | -273 a 920 | 100.0 | 12 | apertura alcalina de persistencia superperiódica del periodo 14 | electrónica extrema | estructura densa | radiotrazador SV |
| 110 | SV-V-Xi | 180.83 | -273 a 950 | 100.0 | 14 | cierre s de confinamiento basal del periodo 14 | electrónica extrema | estructura densa | radiotrazador SV |
| 111 | SV-V-Omicron | 171.41 | -273 a 980 | 100.0 | 14 | apertura de subbloque extendido del periodo 14 | aleaciones SV | estructura densa | radiotrazador SV |
| 112 | SV-V-Pi | 162.32 | -273 a 1010 | 100.0 | 15 | segundo anclaje de frontera extendida del periodo 14 | aleaciones SV | estructura densa | radiotrazador SV |
| 113 | SV-V-Rho | 153.56 | -273 a 1040 | 100.0 | 16 | crecimiento de confinamiento lateral del periodo 14 | aleaciones SV | estructura densa | radiotrazador SV |
| 114 | SV-V-Sigma | 145.12 | -273 a 1070 | 100.0 | 11 | consolidación intermedia de frontera del periodo 14 | aleaciones SV | estructura densa | radiotrazador SV |
| 115 | SV-V-Tau | 137.0 | -273 a 1100 | 100.0 | 12 | semilleno estructural primario del periodo 14 | aleaciones SV | estructura densa | radiotrazador SV |
| 116 | SV-V-Upsilon | 129.19 | -273 a 1130 | 100.0 | 14 | isla local de estabilidad relativa del periodo 14 | aleaciones SV | estructura densa | radiotrazador SV |
| 117 | SV-V-Phi | 121.67 | -273 a 1160 | 100.0 | 14 | transición posisla de identidad del periodo 14 | aleaciones SV | estructura densa | radiotrazador SV |
| 118 | SV-V-Chi | 114.46 | -273 a 1190 | 100.0 | 15 | persistencia tardía de subbloque del periodo 14 | aleaciones SV | estructura densa | radiotrazador SV |
