# Adversarial a Watson v0.4 — Bisturí determinista

**Pieza atacada:** `bisturi-determinista-dominio-inmunologia-2026-08-31-v0.4.md` (25.045 bytes, 1.072 líneas). Copia de trabajo en `artifacts/` idéntica a `attachments/`.  
**Estatuto declarado por el texto:** candidata interna; no adoptada; cierre externo pendiente de esta adversarial y de decisión expresa del director.  
**Corte del ataque:** 31-08-2026.  
**Método:** cita de sección + contraste con (i) corte de dominio 31-08 ya declarado por el autor, (ii) dictamen ES×IMMUNO 27-08, (iii) adversarial del flujo v2, (iv) nomenclatura 1×n / 3^n, (v) G0 cerrado / G1·G2 abiertos, (vi) A1 no adoptado, (vii) estándar §4 del régimen de proyecto (bicondicional definicional ≠ teorema).  
**No se adopta v0.4. No se escribe v0.5. No se tipan células. No se cierra G1 ni G2. No se toca R2.**

Veredicto global: **no pasa entero**.  
Resiste como especificación de gobierno de una IA auxiliar en episodio.  
Colapsa si se lee como constitución del dominio clínico, como ampliación autorizada del álgebra SV, o como algoritmo ejecutable sobre catálogos que el propio texto declara inexistentes.

---

## 0. Qué resiste (no se tumba)

Estas piezas están alineadas con lo ya declarado y no se atacan como error:

- Cadena append-only v0.1 rechazada / v0.2 insuficiente / v0.3 insuficiente como cierre / v0.4 candidata. Ninguna versión reescrita (§0).
- Principio «o sabe para esta O y este E, o no sabe» (§1). No saber ≠ inferir, aprender, completar, explicar, aconsejar.
- Congelación de `RELEASE_M` durante el episodio (§3). Corrección del inmunólogo = evidencia para otra versión, no aprendizaje automático.
- Cardinalidad: (9,3) no es 3×3; (25,5) no es 5×5; espacio \(3^{n_k}\) (§4.1). B04 y B05 lo convierten en prueba de rechazo. Eso ya estaba bien en v2.
- Tiempo y estadística no primitivas internas (§11.1). Dato estadístico externo conserva método, población, fecha, incertidumbre y procedencia.
- U ≠ dato ausente por identidad; U ≠ incertidumbre del modelo; U cómoda del motor = no conformidad (§8.2, §8.4, B11–B14).
- Consecuencias de ignorancia constituidas **antes** de la decisión (§9, §13 t12–t17). Prohibición del «porqué» narrativo posterior (§19, B21).
- Prioridad 1–20 prohibida como función de decisión (§10). Alternativas incomparables permanecen incomparables.
- Firma del experto acredita información recibida; no transfiere responsabilidad jurídica ni sustituye consentimiento (§16).
- R2, IR, semántica e implementación del Lenguaje declarados fuera de alcance (encabezado). F10 abierto.
- F01–F10 explícitos: catálogos, umbrales, corpus, régimen, atribución jurídica, interfaz con el Lenguaje **no** se declaran resueltos (§22).
- Referencias §23: el ELI `eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng` existe (texto consolidado vigente 27-07-2026). La guía FDA CDS existe como final de enero 2026 (reemitida 29-01-2026). Ley 41/2002 y Ley 44/2003 existen. El texto no prejuzga clasificación del sistema. Eso resiste como frontera, no como habilitación.

Eso no salva el documento. Un bisturí se juzga por lo que **corta** y por lo que **funde**.

---

## 1. Flanco duro: fusión de tres objetos bajo notación SV

**Texto atacado.** Encabezado: «Fuera de alcance: R2, IR, semántica e implementación del Lenguaje».  
§4.1: `Aᵏ = (aᵏ₁ⱼ)`, `Aᵏ ∈ Σ^(1×nₖ)`, `Σ = {0,1,U}`, `|Σ^{nₖ}| = 3^{nₖ}`.  
§4.2: cada `aᵏ₁ⱼ` declara `clinical_knowledge_id`, reglas, consecuencias, interfaces.  
§5: el módulo clínico `Cₖ` **contiene** `Aᵏ`.  
§7: `Cᵢ ⊙[Tᵢⱼ] Cⱼ` con no conmutatividad por defecto.

**Por qué colapsa como constitución.** El corte 31-08 separó tres perímetros:

1. Fundamentos + Origen de U (inviolables);
2. álgebra de composición (solo ampliar o error demostrado);
3. Lenguaje SV (puede cerrarse más desde el dominio **antes** de R2, sin inferir).

El dictamen ES×IMMUNO 27-08 y la adversarial del flujo v2 tumbaron la fusión de:

1. dominio profesional declarado;
2. dominio clínico operativo (episodio);
3. centinela del Lenguaje.

v0.4 declara (3) fuera de alcance y acto seguido usa (3) como **representación constitutiva** de (2). El valor clínico de un módulo queda en el mismo alfabeto y la misma forma de fila que el Lenguaje. La composición clínica usa el mismo símbolo `⊙`.

Eso no es «cerrar el Lenguaje desde el dominio». Es **importar el álgebra al dominio** sin autorización expresa de ampliación del perímetro 2.

Efecto demostrable:

- un revisor de Orientation / non-closure / VII leerá `Σ={0,1,U}`, `3^n`, `⊙` no conmutativo, paridad de motores y certificado predecisional como la misma familia formal;
- G1 queda presionado: (9,3) y (25,5) reaparecen como forma de módulo, aunque el texto diga que el segundo componente no se redefine;
- G2 no se cierra hacia R2 (bien), pero se **ocupa** el objeto del Lenguaje desde el gobernador clínico.

**Qué hay que mejorar.** Tres capas con interfaz, no una sola `Aᵏ`:

- catálogo clínico (conocimiento, consecuencias, operaciones) **sin** valor ternario;
- estado de episodio (hechos congelados, no células);
- solo si el director amplia el álgebra: proyección tipada hacia una fila `1×n_k` **después** de G0, no como contrato de `Cₖ` en esta candidata.

**Veredicto:** colapsa como ampliación del álgebra. Resiste como prohibición de inferir valores `{0,1,U}` por semejanza o probabilidad (§4.2, última frase).

---

## 2. Flanco duro: algoritmo BDI sobre catálogos vacíos

**Texto atacado.** §18 presenta `BDI(E,O,M)` con 66 pasos y `RETURN GOVERNED_EXPERT_DECISION`. §6.3 define `Λ(O,E)` como «least authorized closure». §21 da `OUTPUT_ADMISSIBLE` como bicondicional de 15 conjunciones.

**Por qué colapsa como ejecutable.** El propio §22 dice que no existen:

- F01 catálogo de módulos;
- F02 contenido de cada matriz;
- F04 interfaces;
- F05 reglas y consecuencias por entidad/población/operación;
- F06 umbrales y hard stop.

Sin esos objetos, los pasos 05–07, 11–22, 32–42 y 51 no tienen operandos. `SEED(O,E)` «módulos declarados por regla clínica» (§6.2) remite a F05. `Kᵣ ⊆ Kᵥ` remite al mismo F05. `least closure` remite a `Gᶜ=(C,T)` que es F01+F04.

Circularidad:

```text
regla clínica → SEED → Λ → Kᵣ → SABE
regla clínica = F05 = no constituida
```

`SABE(M,O,E)` (§2) es entonces una **definición operativa** de un predicado que hoy no tiene instancia. Régimen de proyecto §4.1: no presentarlo como si evaluara un episodio real. El texto no lo llama teorema. El algoritmo sí lo **invoca** en el paso 51 como si devolviera un valor.

**«Least».** En un grafo dirigido finito predeclarado, la clausura por dependencias autorizadas desde `SEED` es el conjunto alcanzable. Eso es único. Si `Gᶜ` está incompleto, hay muchas clausuras «mínimas» según qué aristas falten; el documento no fija qué hacer entonces salvo `CLOSURE_REJECTED`. Eso es correcto como parada. No es constitución de Λ.

**Qué hay que mejorar.** Separar dos piezas:

- esquema de gobierno (lo que v0.4 sí es);
- instancia (un solo `O` testigo, un `SEED` finito, un `Gᶜ` finito, un k con consecuencia constituida).

Sin testigo finito, B01–B30 son criterios de un motor que no tiene datos. B26 («misma entrada y versiones producen mismo objeto») no se puede ejecutar.

**Veredicto:** el esquema resiste. La pretensión de algoritmo integrado no.

---

## 3. `SABE` y `OUTPUT_ADMISSIBLE` son definiciones, no criterios independientes

**Texto atacado.** §2:

```text
SABE(M,O,E) ⇔
  Kᵣ ⊆ Kᵥ
  ∧ Cᵥ = COMPLETA
  ∧ U꜀ = ∅
  ∧ controles = PASS
  ∧ acta predecisional sellada
```

§21: `OUTPUT_ADMISSIBLE` ⇔ quince términos, entre ellos `EXPERT_DECISION_APPENDED`.

**Ataque.** Si `SABE` se **define** como esa conjunción, el bicondicional no añade contenido. Es el nombre del paquete de condiciones. Decirlo así evita que un extracto posterior lo cite como resultado.

Segundo problema: `OUTPUT_ADMISSIBLE` exige `EXPERT_DECISION_APPENDED`. Entonces la admisibilidad del **sistema** incluye el acto humano. Eso mezcla:

- admisibilidad de la salida candidata gobernada (hasta t18);
- registro del acto del inmunólogo (t19).

§16 ya distingue `ACKNOWLEDGE_INFORMATION ≠ ACCEPT_CANDIDATE` y el hard stop que mantiene el sistema en abstención aunque el experto actúe fuera. Bien. §21 lo deshace al poner la decisión humana dentro del predicado de admisibilidad del output.

**Qué hay que mejorar.** Dos predicados:

- `GOBERNADO(M,O,E)` hasta el acta sellada y el `EXPERT_FRAME` renderizado;
- `DECISIÓN_REGISTRADA` como evento posterior, que no retroactúa sobre `GOBERNADO`.

**Veredicto:** definicional. No demuestra saber clínico. No se ataca el contenido de las conjunciones; se ataca su uso como si evaluaran el dominio.

---

## 4. G1 no está cerrado, pero queda cargado

**Texto atacado.** §4.1 usa (9,3) y (25,5) solo para cardinalidad y remite el segundo componente a «fuente canónica y autoridad competente». Encabezado: semillas no se mencionan como plantilla. F03 deja abierto el estatuto del segundo componente.

**Por qué no colapsa del todo.** No afirma Q = «las filas 1×25 quedan congeladas y la arquitectura se deriva después» que tumba el flujo v2.

**Por qué sigue cargado.** El contrato de módulo `Cₖ` **es** una fila ternaria `1×n_k`. Cualquier módulo clínico futuro nace con esa forma. Eso no decide la longitud 25, pero decide el **tipo de objeto**. G1 tenía tres lecturas abiertas: semillas no agotan / no intocables / no plantilla. v0.4 no toca las longitudes y sí fija la plantilla formal de todo `Cₖ`.

**Veredicto:** no cierra G1 sobre las semillas. Cierra, sin G0, la forma de todo módulo futuro. Eso es una decisión de diseño, no un hecho del dominio.

---

## 5. Composición dirigida: el contrato es correcto; el transfer es un hueco

**Texto atacado.** §7.2: la composición solo existe si tipos, sentido, orden, precondiciones, transfer determinista, consecuencias constituidas y alcance de validación coinciden. §7.4: interfaz no registrada → abstención. La IA no ensaya rutas.

**Qué resiste.** No conmutatividad por defecto. Paradas explícitas. Prohibición de descubrir composiciones en el episodio (§3.2 `COMPOSITION_DISCOVERY`).

**Qué no resiste.** «Transfer rule is deterministic» no tiene regla. Pasar `P-LAB-IGG` a un módulo IEI no es una identidad. Sin `transfer_rule_ids` instanciados (F05), «determinista» es un adjetivo. Un transfer mal escrito es exactamente inferencia disfrazada de regla.

El grafo `Gᶜ` es el lugar donde se colaría la inferencia: si mañana se añade una arista «porque el caso lo pide», se viola §3.2. El texto lo prohíbe. No da el registro de aristas.

**Veredicto:** el régimen de parada resiste. La composición clínica no está constituida.

---

## 6. Elemento `aᵏ₁ⱼ`: el esquema y el valor no están separados

**Texto atacado.** §4.2 define `aᵏ₁ⱼ = { element_id, matrix_id, row_index=1, column_index=j, clinical_knowledge_id, ... consequence_if_ignored_ids[], ... }`. Luego: «El valor `{0,1,U}` sólo se constituye mediante regla autorizada».

**Ataque.** Hay dos objetos con el mismo nombre:

- la **ficha** del slot (catálogo: qué conocimiento, qué consecuencia, qué interfaz);
- el **estado** del slot en el episodio (`0`, `1` o `U`).

Fundirlos permite que un modelo «complete» la ficha y finja que constituyó el valor. B15 rechaza completar conocimiento ausente por inferencia. La notación no ayuda a ese rechazo.

**Qué hay que mejorar.** `SLOT_k_j` (inmutable en `RELEASE_M`) ≠ `STATE(E, k, j) ∈ {0,1,U}`. El segundo solo por regla. El primero no se toca en el episodio.

**Veredicto:** ambigüedad de tipo. No es un error de cardinalidad.

---

## 7. D0-L aparece y no está en esta pieza

**Texto atacado.** §11.2: «El acceso de la unidad de IA a datos queda además subordinado a la puerta jurídica y técnica D0-L».

**Hecho de esta unidad.** El archivo `registro-d0-cobertura-dominio-inmunologia-2026-08-31-v0.1.md` fue citado en el hilo autor–Watson y **no está** en artifacts ni en attachments de esta unidad. No se lee. No se inventa.

**Ataque.** Una puerta que no está en el documento no puede ser condición operativa del §11.2. O se incorpora el texto D0-L por referencia versionada con hash, o se retira la mención. Citar un objeto ausente reproduce el vicio que el propio bisturí prohíbe: continuar con un k no presente.

**Veredicto:** hueco de paquete. No se afirma que D0-L sea falso; se afirma que aquí no está.

---

## 8. Paridad de motores: objeto correcto, vocabulario de riesgo

**Texto atacado.** §12: mismos hashes, mismo `RELEASE_M`, mismo `Λ`, mismo esquema canónico. `PARITY` = igualdad de `ENGINE_RESULT` canónico. Si falla, abstención. La interfaz clínica no es prosa de cada IA.

**Qué resiste.** Encaja con «sin paridad → abstención» del hilo v0.3 y con el rechazo de la caja negra explicable.

**Riesgo.** Proximidad formal con el centinela ES×IMMUNO (paridad Rust/WASM, identificadores, S finito) y con certificados de no-cierre / VII (mismatch, ceguera de balance terminal). El objeto puede ser distinto —aquí es paridad de **mapeo a objetos clínicos canónicos**, no persistencia del Lenguaje— y el revisor igual lo leerá como la misma capa.

El encabezado pone el Lenguaje fuera. §12 construye un segundo centinela. Dos centinelas no fundidos, o uno solo con G0. El texto no elige.

**Veredicto:** resiste como regla de gobierno multi-motor. No se presenta como el centinela del Lenguaje. El solapamiento de vocabulario queda como riesgo editorial, no como plagio interno.

---

## 9. Título «determinista» y lema de cierre

**Texto atacado.** Título: «Bisturí determinista…». §11 «Núcleo determinista».

**Ataque ya hecho al v2.** «Determinista» en el lema es lo primero que se lee. Aquí el sentido técnico es: transfer sin peso libre, sin desempate narrativo, sin score. Eso está en §10 y §7. El título no lo dice.

No es un colapso matemático. Es el mismo flanco de presentación que ya costó una corrección.

---

## 10. Consecuencias: el catálogo de tipos no constituye ninguna consecuencia

**Texto atacado.** §9.1 modos de error. §9.2 tipos de daño. §10 `CONSEQ(a)` para alternativas. Frase final de §9.2: «La inclusión de un tipo no afirma que ocurra en un caso concreto».

**Qué resiste.** La frase final. La separación consecuencia de ignorancia ≠ consecuencia de alternativa (v0.2 pecaba de lo segundo). La lista incluye `FALSE_REASSURANCE` y `UNSUPPORTED_CERTAINTY`, que son el mecanismo del experto que «mete la pata» por consejo.

**Qué no resiste.** Ningún k del universo candidato v0.2 queda ligado a un modo de error autorizado y a una consecuencia de paciente **instanciada**. El paquete de parámetros (64, 27, 50, 40) no es `Kᵣ`. v0.4 no lo cita. Bien: no fusiona objetos. Mal para quien lea v0.4 como si ya hubiera bisturí sobre inmunología: hay tipología, no hay un solo `knowledge_requirement_id` con `CONSEQ` sellado.

B18: «Falta consecuencia humana de un error crítico → REJECT». Hoy, aplicado al documento mismo, el catálogo de tipos sin una sola instancia crítica **debería** impedir `SABE` para cualquier O real. El texto lo admite en F05. Hay que leerlo así, no como si B18 ya tuviera operandos.

**Veredicto:** la tipología resiste. La constitución de consecuencias no ha empezado.

---

## 11. Lo que el documento hace bien y no debe perderse en una reescritura

Si el director pide otra versión, estos cortes ya están y no se reabren por gusto:

1. No hay reparación retrospectiva del episodio (§13, último bloque; B20).
2. No hay memoria clínica entre pacientes (§3.2).
3. Potencia computacional ≠ conocimiento (§11.3, B16).
4. U fuera de Λ no tumba el dominio (B14).
5. Actuación clínica externa del experto no falsifica la salida del sistema (B30).
6. Auditoría = caminos inmutables preexistentes, no prosa (§19).
7. Abstención por defecto cuando falta un término de §21.

Eso es el núcleo que el autor pidió asimilar. Está escrito. No está instanciado. No está autorizado como álgebra SV.

---

## 12. Relación con piezas ya existentes (sin fusionarlas)

| Pieza | Relación lícita | Fusión ilícita |
|---|---|---|
| Universo candidato v0.2 (64/27/50/40) | puede alimentar **candidatos** a `knowledge_requirement_id` tras revisión humana | no es `Kᵣ` ni `C` ni `Gᶜ` |
| Mapa curricular MIR v0.1 | filtro de grano, objeto distinto | no es conocimiento exigido de un episodio |
| Inventario A1 | D0 de repos; ninguna fuente adoptada | no es `RELEASE_M` |
| Semillas IMMUNO-1/2 | no agotan; G1 abierto | no son plantilla de todo `Cₖ` |
| Flujo HTML 31-08 / flujo v2 | gobierno de proceso; v2 no pasó entero | no se reescribe como v0.4 |
| ES×IMMUNO / Orientation / VII / non-closure | sumisiones y centinela de Lenguaje | no se reutilizan como núcleo clínico |

---

## 13. Veredicto por bloque

| Bloque | Veredicto | Motivo corto |
|---|---|---|
| §0 cadena append-only | resiste | estado de versiones honesto |
| §1 principio o-sabe-o-no | resiste | no es teorema; es régimen |
| §2 SABE | resiste como definición; no demostrado como evaluador | bicondicional definicional; catálogos vacíos |
| §3 congelación | resiste | invariante de episodio |
| §4 matrices ternarias | colapsa como constitución del dominio | fusión con álgebra SV; G1 de forma |
| §5 contrato Cₖ | colapsa si Cₖ ⊆ fila SV | mismo flanco que §4 |
| §6 Λ | resiste como parada; no constituida | «least» vacío sin Gᶜ |
| §7 composición | resiste el régimen de rechazo; transfer no instanciado | F04/F05 |
| §8 U | resiste | alineado con Origen de U y v2 |
| §9–10 consecuencias | resiste la tipología; no hay instancia | F05 |
| §11 núcleo vs IA | resiste | lista de prohibiciones usable |
| §12 paridad | resiste como gobierno; riesgo de vocabulario | no fundir con centinela Lenguaje |
| §13–17 acta / experto / log | resiste | predecisional + append-only |
| §18 BDI | no pasa como algoritmo | operandos F01–F07 ausentes |
| §19 auditoría | resiste | lee lo anterior; no explica |
| §20 B01–B30 | resisten como batería de rechazo de motor | no hay banco que los ejecute |
| §21 OUTPUT_ADMISSIBLE | colapsa la última conjunción | mezcla output gobernado y acto humano |
| §22–24 fronteras y puerta | resiste | no adopción, no completez |

---

## 14. Condición para que una pieza posterior no herede la rotura

No se pide v0.5 en este corte. Si el director autoriza otra versión append-only, los mínimos para no heredar el flanco duro son:

1. Separar catálogo clínico, estado de episodio y —solo con G0— proyección a fila ternaria.
2. No usar `Aᵏ`, `⊙` y `Σ={0,1,U}` como contrato de módulo clínico hasta ampliación expresa del álgebra.
3. Un testigo finito: una O, un E sintético no asistencial, un `SEED` de tamaño declarado, una interfaz, un k con consecuencia sellada. Sin testigo no hay BDI.
4. Dos predicados: gobernado / decisión registrada.
5. D0-L por referencia con hash, o fuera.
6. Dejar G1 y G2 escritos como abiertos en el cuerpo, no solo F03/F10.
7. Título sin «determinista» si el contenido ya dice «sin peso libre».

Hasta decisión del director:

```text
NO ADOPTION
NO CLAIM OF COMPLETENESS
NO LANGUAGE CHANGE
NO CLINICAL DEPLOYMENT
NO TYPING OF SV CELLS
NO INFERENCE OF K, Λ, OR U
```

Eso ya lo dice el §24. Esta adversarial lo confirma y añade el flanco que el §24 no nombra: la fusión notacional con el álgebra SV.
