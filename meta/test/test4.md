# INFORME ADVERSARIAL PARA CLAUDE

## Primera publicación de editorialia.com — GraphRec

**Objeto:** auditoría de la ficha crítica en formato WordPress.
**Estado:** APTO CON REPAROS QUIRÚRGICOS.
**Fuera de este informe:** inserción del abstract literal e incorporación de la imagen con R0 y QR, que realizará el director.

---

## 1. Estructura general

La estructura es apta.

Funciona correctamente la separación entre:

* dato del artículo;
* material incorporado;
* lectura;
* conclusión crítica;
* tipo de afirmación;
* exposición.

También es adecuada la declaración inicial de alcance:

> This is not peer review. No proof has been checked, no experiment reproduced, no result validated.

La ficha no pretende validar resultados ni reproducir experimentos. Audita correspondencia entre afirmaciones y soporte.

---

## 2. Unidad 1 — APTA

La primera unidad es documentalmente sólida.

El artículo declara una muestra de 94 trabajos y remite la lista completa al repositorio. El archivo `SURVEYED_PAPERS.md` contiene efectivamente 94 entradas, pero sólo títulos. No incluye:

* año;
* foro;
* conjunto de datos;
* identificador;
* clasificación;
* procedimiento de búsqueda;
* criterios de inclusión.

La conclusión es proporcionada:

> What is in neither the article, nor Appendix A, nor the list itself is the classification from which the figure is computed.

No se afirma que el porcentaje sea falso ni que la selección sea incorrecta. Se registra que la clasificación necesaria para reproducir documentalmente el 86,6 % no aparece en el material incorporado.

### Reparación de alcance

No conviene incorporar el repositorio completo como unidad probatoria. La ficha sólo utiliza materialmente `SURVEYED_PAPERS.md`.

Sustituir:

> **Incorporated material**
> github.com/haoyuhan1/GraphRec · commit `38af2bb5` · consulted 17 July 2026

por:

> **Incorporated material for Unit 1 only**
> `SURVEYED_PAPERS.md`, repository `haoyuhan1/GraphRec`, commit `38af2bb55984a56f5d1a5d7a41d8d6e7bfe41957`, consulted 17 July 2026.

Y añadir:

> The repository declares no licence of its own. This critique incorporates only the factual contents of `SURVEYED_PAPERS.md` for documentary comparison. It does not reproduce, execute or validate the repository code.

---

## 3. Unidad 2 — REFORMULAR

El problema está correctamente visto, pero la conclusión actual equipara en exceso dos niveles distintos.

Ahora dice:

> The title carries the opposite of it: *Reveals*, where Section 4.2 says *could*.

Eso no es exacto.

El artículo observa que la heurística resulta competitiva en determinados bancos de prueba. Ese resultado experimental es el soporte de la expresión *shortcut-solvable*. El `could` de la sección 4.2 modera la explicación causal: las estructuras identificadas podrían explicar el rendimiento.

La ausencia de intervención impide demostrar causalidad, pero no elimina el resultado observado.

### Sustitución propuesta

> **Reading.** Nothing in the paper weakens or removes a shortcut within a fixed benchmark. What varies is the dataset. The evidence is therefore cross-sectional: fourteen benchmarks with different properties, together with an association between those properties and the relative performance of the heuristic.
>
> **Critical conclusion.** The experiments establish that the heuristic is competitive on the evaluated benchmarks. What they do not establish by intervention is that the three proposed structures are the causes of that performance. The front matter compresses those two levels: observed shortcut-solvability and a potential explanation of it.

Tabla:

> **Claim type:** Observed result followed by a causal interpretation not tested by intervention.
> **Exposure:** Low. The distinction is present in the article itself.

---

## 4. Unidad 3 — REFORMULAR

La versión actual dice:

> A property named as belonging to the benchmark is measured through a constant the authors chose.

La afirmación es demasiado fuerte.

La ramificación media es una propiedad calculada sobre el grafo de transición. No depende del presupuesto de recuperación. Lo que sí depende del presupuesto fijo es la capacidad de la heurística para explotar esa estructura.

Debe separarse:

* propiedad del conjunto;
* respuesta de la sonda bajo unas constantes elegidas.

### Sustitución propuesta

> **Reading.** Average out-degree is a property of the constructed transition graph, independent of the retrieval budget. Whether that property makes TGH effective is nevertheless evaluated through fixed budgets chosen by the authors. The diagnosis therefore combines a dataset statistic with the response of one deliberately fixed probe.
>
> **Critical conclusion.** “Shortcut-solvable” is supported relative to the diagnostic family and fixed operating conditions tested here. The article discloses that boundary; the compact label does not carry it.

Tabla:

> **Claim type:** Reading of this critique, grounded in the article’s definitions and limitations.
> **Exposure:** Medium. The facts are the article’s; the restriction of scope is an inference.

---

## 5. Unidad 4 — CORREGIR UNA AFIRMACIÓN MATERIAL

La frase:

> a pretrained language model that the heuristic does not train and does not describe

no debe permanecer.

El artículo sí identifica el modelo de lenguaje preentrenado y describe su función como generador de representaciones textuales compartidas entre los métodos que utilizan texto.

La cuestión crítica válida no es que la dependencia esté oculta, sino que la simplicidad de la heurística no equivale a simplicidad del conjunto completo de dependencias.

### Sustitución propuesta

> **Reading.** The dependency is stated plainly and the reason for sharing it across methods is sound. The heuristic does not train the text encoder, but its ranking signal depends on representations produced by that pretrained component.
>
> **Critical conclusion.** The method is simple as a trainable recommendation architecture: it fits no parameters of its own. Its complete computational stack is not correspondingly simple, because its ranking signal inherits a pretrained text encoder.

Tabla:

> **Claim type:** Title against the complete dependency stack.
> **Exposure:** Low. The dependency is explicitly declared.

---

## 6. Unidad 5 — APTA

La quinta unidad mantiene una distinción correcta:

* los autores reprodujeron las referencias;
* siguieron configuraciones descritas por los trabajos originales;
* la ficha no ha ejecutado esas reproducciones;
* no se afirma que sean deficientes.

La lectura:

> The supported claim is that the heuristic beats these implementations under this protocol, not that it beats the numbers those methods published.

es válida y suficientemente prudente.

No necesita reparación material.

---

## 7. Cierre general — REFORMULAR

El cierre actual afirma:

> The distance this ficha registers is not between the argument and the evidence. There the article holds.

Esto contradice parcialmente la Unidad 1 y reduce demasiado el alcance de las Unidades 2 y 3.

No hay un fracaso general del argumento, pero sí existen diferencias entre:

* el resultado compacto que viaja;
* sus condiciones de interpretación;
* el soporte documental disponible para la cifra nuclear.

### Sustitución propuesta

> The distance registered here is not a wholesale failure of the article’s argument. Its experimental result is stated, bounded and qualified in the body. The material distance lies between the compact claims that travel — the title, the abstract and the 86.6% anchor — and the fuller conditions or documentary support needed to read them at their exact strength.

Puede conservarse el párrafo final de recomendación:

> This article is recommended here because it declares its own frontier instead of immunising itself against it, and because it audits a consensus instead of adding a layer to it.

---

## 8. Metadato R0 visible en la página 3

La ficha muestra:

```html
<meta name="r0identifier" content="b621309bd8d28cda43682baaeb45707f" />
```

Pero el sitio emite materialmente:

```html
<meta name="citation_r0" content="b621309bd8d28cda43682baaeb45707f" />
```

Debe mostrarse la etiqueta real:

```html
<meta name="citation_r0" content="b621309bd8d28cda43682baaeb45707f" />
```

El R0, R1, R2 y R3 de la ficha son coherentes entre sí.

---

## 9. Advertencias heredadas de la página 2

El bloque histórico contiene afirmaciones que no encajan limpiamente con esta publicación CC BY 4.0.

En particular:

> to ensure private use without commercial purposes

no describe la licencia CC BY 4.0, que no excluye el uso comercial.

También se afirma que no se proporcionan enlaces hipertextuales «en general», aunque la propia ficha incluye enlaces DOI y de contacto.

No es necesario rehacer ahora toda la página 2, pero estas advertencias no deben presentarse como interpretación de la licencia específica del artículo.

Reparación mínima:

> The paper is identified as CC BY 4.0. Any reuse must comply with that licence and with the attribution, licence notice and indication-of-changes requirements applicable to the material used.

Las advertencias generales del sitio pueden permanecer como política editorial histórica, pero separadas de la licencia concreta del paper.

---

# Dictamen final

## APTO CON REPAROS QUIRÚRGICOS

Antes de publicar:

1. restringir el material incorporado a `SURVEYED_PAPERS.md`;
2. reformular la Unidad 2;
3. reformular la Unidad 3;
4. corregir la Unidad 4;
5. mantener la Unidad 5;
6. sustituir el cierre general;
7. cambiar `r0identifier` por `citation_r0`;
8. separar la licencia CC BY 4.0 de las advertencias históricas generales.

No se cuestionan:

* la arquitectura WordPress;
* la estructura de tres niveles;
* el R0;
* la ficha registral;
* el orden de páginas;
* el abstract, que insertará el director;
* la imagen y el QR, que preparará el director.

Tras estas reparaciones procede la lectura final ya renderizada en WordPress.
