Almirante, he revisado ya las dos fuentes oficiales. Quedan cerrados tanto el frente operativo del portal como la decisión científica.

## 1. Qué exige realmente J-MMCT

La revista requiere:

* plantilla IEEE específica de **dos columnas**, con figuras y pies integrados;
* resumen de unas **150 palabras**;
* términos de indexación tomados, preferentemente, de la lista aprobada por IEEE;
* afiliación y datos de contacto completos;
* declaración del contenido generado con IA, identificando herramienta, contenido afectado y nivel de uso;
* **resumen gráfico con una breve leyenda**;
* declaración y cita de todo trabajo previo estrechamente relacionado;
* ocho páginas ordinarias y una novena gratuita sólo cuando sea una página completa de referencias. ([ieee-jmmct.org][1])

La opción de acceso abierto comporta APC. Para mantener la condición económica absoluta, cuando el portal lo pregunte se seleccionará la modalidad tradicional, no acceso abierto. Los cargos de 110 dólares por las primeras ocho páginas no son obligatorios; los cargos por exceso sí lo son. ([ieee-jmmct.org][1])

El **resumen gráfico** es una sorpresa operativa que ya dejamos anotada: habrá que preparar una figura muy limpia con el recorrido

[
\mathcal M_h
\overset{\mathcal R_h}{\longrightarrow}
\mathcal E
\overset{\mathcal P_h}{\longrightarrow}
\mathcal M_h.
]

## 2. Las políticas IEEE y las casillas

Las tres políticas que el portal exige revisar son:

1. **Envío único y publicación previa.** No puede existir evaluación simultánea en otra revista. Los antecedentes y preprints deben declararse, citarse y acompañarse de una explicación clara de las diferencias del nuevo artículo. ([IEEE Author Center Journals][2])
2. **Plagio y reutilización.** Todo material ajeno debe atribuirse, y la reutilización de material propio debe identificarse y relacionarse con la nueva aportación. ([IEEE Author Center Journals][2])
3. **Publicación electrónica previa.** Al enviar el artículo, IEEE exige añadir a las versiones electrónicas previamente publicadas el aviso de que el trabajo ha sido sometido a IEEE para posible publicación. Tras la aceptación y publicación, exige actualizar esos registros conforme a su política de copyright y citación. ([IEEE Author Center Journals][2])

Por tanto, en la pantalla actual:

* **Original Article:** seleccionado.
* **Envío exclusivo, con excepción de preprints:** se puede marcar.
* **Coautores informados:** se puede marcar; es autor único.
* **Tratamiento de datos por socios de producción:** se puede marcar si acepta esa condición.
* **No contiene la imagen Lena:** se puede marcar.
* **Cumplimiento de autoría:** se puede marcar.
* **Políticas de envío y revisión:** puede marcarla después de leer personalmente los tres apartados anteriores en la página oficial. Yo ya los he auditado, pero la declaración está formulada en primera persona.
* **Archivos preparados conforme al formato:** todavía no debe marcarse. Aún no existe el manuscrito final en la plantilla J-MMCT.

Los preprints tendrán que incluir, cuando se realice el envío efectivo, el aviso prescrito por IEEE. No es necesario hacerlo durante esta fase de construcción.

---

# 3. Decisión científica sobre el índice de sucesos

La decisión correcta no es escoger únicamente uno de los dos extremos de Claude. Adoptaremos una estructura de dos niveles, pero con jerarquía estricta:

## Resultado principal: exactitud discreta

Sea una secuencia temporal auxiliar declarada mediante

[
t_{j+1}-t_j=\omega_j>0,
]

y defínase el operador clásico discreto

[
\delta_t q_j
============

\frac{q_{j+1}-q_j}{t_{j+1}-t_j}.
]

Como el SV define

[
\partial_\nu^{SV}q(j)
=====================

\frac{q_{j+1}-q_j}{\omega_j},
]

se obtiene exactamente:

[
\boxed{
\partial_\nu^{SV}q(j)=\delta_tq_j
}
]

sobre la misma secuencia declarada.

No hay aproximación, límite ni error residual. La igualdad es exacta.

El teorema central se formulará, por tanto, sobre el sistema de Maxwell discretizado en la misma secuencia de sucesos:

[
\mathcal M_h.
]

Las aplicaciones serán:

[
\mathcal R_h:
\mathcal M_h
\longrightarrow
\operatorname{Im}\mathcal R_h,
]

[
\mathcal P_h:
\operatorname{Im}\mathcal R_h
\longrightarrow
\mathcal M_h.
]

Y la reversibilidad se demostrará correctamente como:

[
\boxed{
\mathcal P_h\circ\mathcal R_h
=============================

\operatorname{Id}_{\mathcal M_h}
}
]

y

[
\boxed{
\mathcal R_h\circ\mathcal P_h
=============================

\operatorname{Id}_{\operatorname{Im}\mathcal R_h}.
}
]

Esta segunda identidad se restringe a la imagen de la reducción. No afirmaremos alegremente una biyectividad entre todo el universo factual y todo el sistema clásico, porque el SV puede contener estructura adicional que no pertenece a Maxwell.

Ésta es una reversibilidad exacta, completa y matemáticamente limpia.

## Puente secundario: consistencia continua

No afirmaremos que el sistema continuo se recupera exactamente mediante una diferencia finita.

Pero sí podemos demostrar, sin abrir un artículo entero de análisis numérico, que para un campo suficientemente regular:

[
q\in C^2,
]

el desarrollo de Taylor da:

[
q(t_j+\omega_j)
===============

q(t_j)
+
\omega_j q'(t_j)
+
O(\omega_j^2).
]

Por tanto:

[
\partial_\nu^{SV}q(j)
=====================

# \frac{q(t_j+\omega_j)-q(t_j)}{\omega_j}

\frac{\partial q}{\partial t}(t_j)
+
O(\omega_j).
]

Y bajo refinamiento:

[
\max_j\omega_j\rightarrow0,
]

se obtiene:

[
\partial_\nu^{SV}q(j)
\longrightarrow
\frac{\partial q}{\partial t}(t_j).
]

Esto se presentará como **consistencia de primer orden del operador temporal**, no como convergencia demostrada de un solver completo.

No necesitaremos probar:

* estabilidad global;
* convergencia de soluciones;
* orden espacial total;
* teoremas de Lax;
* error acumulado del campo.

Sólo demostramos el puente local del operador. Es suficiente para que el lector clásico reconozca la relación, sin subordinar la ecuación factual al límite continuo.

---

# 4. ¿Le corta las alas a la ecuación?

No.

La ecuación

[
\mathbb E_{SV}=0
]

sigue condensando:

* las cuatro leyes;
* las constitutivas;
* las condiciones de interfaz;
* la frontera y la reconfiguración;
* los balances derivados.

Lo que se delimita es únicamente **qué significa reconstrucción exacta**.

La afirmación fuerte y verdadera será:

> La representación operatoria es exactamente reversible sobre una secuencia declarada de sucesos y es consistente, bajo refinamiento, con el operador temporal continuo.

Esto es más fuerte científicamente que decir simplemente que «converge a Maxwell», porque separa dos resultados:

[
\boxed{\text{identidad exacta en el dominio nativo}}
]

y

[
\boxed{\text{puente continuo condicionado y cuantificado}.}
]

## Título provisional corregido

> **An Exact Reversible Block-Residual Representation of Maxwell’s Equations on Declared Event Sequences**

No lleva «SV» en el título, no lleva célula y no promete equivalencia continua exacta.

La contribución queda situada donde realmente es fuerte:

* representación de bloque;
* residuos separados;
* exactitud sobre secuencias;
* reconstrucción reversible;
* evaluación computacional;
* puente continuo declarado.

---

# 5. Dos correcciones adicionales que quedan congeladas

La contradicción entre (\mathcal D_{SV}) y (\mathcal D_{SV}^{-1}) se elimina definitivamente. El propio documento define una dirección y aplica después la inversa en esa misma dirección, por lo que no se trasladará esa notación al artículo.

También queda prohibido afirmar que (\mathcal P_h) es inversa global antes de fijar su dominio. La formulación correcta será:

[
\mathcal P_h=\mathcal R_h^{-1}
\quad
\text{sobre }\operatorname{Im}\mathcal R_h.
]

## Dictamen

[
\boxed{
\text{Resultado exacto discreto como teorema principal}
+
\text{consistencia continua como proposición auxiliar}.
}
]

No aumenta materialmente la complejidad, no subordina el SV al tiempo continuo y ofrece al lector de J-MMCT una propiedad exacta junto con un puente clásico verificable. Esto queda congelado para la prearquitectura V0.2.

[1]: https://ieee-jmmct.org/information-for-authors/ "Information For Authors – Journal On Multiscale and Multiphysics Computational Techniques"
[2]: https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/ "Submission and Peer Review Policies - IEEE Author Center Journals"
