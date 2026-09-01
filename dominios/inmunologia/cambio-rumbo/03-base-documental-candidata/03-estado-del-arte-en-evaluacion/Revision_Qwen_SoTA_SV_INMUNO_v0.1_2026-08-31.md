# Revisión del estado del arte Qwen v0.1 — Formalización determinista de la decisión clínica

**Pieza:** `Qwen_markdown_20260831_zaey2r5g9.md` (25.170 bytes).  
**Estatuto declarado:** candidata interna de estructura para preprint. No adoptada.  
**Corte de esta revisión:** 31-08-2026.  
**Método:** leer el texto; separar Parte I (SoTA) / Apéndice A (caso) / Parte II (posicionamiento); contrastar con el frente real, con las sumisiones SV activas y con fuentes primarias localizables.  
**No se adopta. No se redacta el preprint. No se tipan células. No se cierra n=b².**

Veredicto: **la Parte I señala un hueco real y lo cubre con una bibliografía incompleta y con un vacío que no existe en los términos en que lo declara. La Parte II no es estado del arte: es cocina interna, atribuye mal las piezas y propone un preprint sobre un inventario no adoptado.**

---

## 0. Tres documentos en uno

| Bloque | Qué pretende ser | Qué es |
|---|---|---|
| Parte I §§1.1–1.5 | Estado de la ciencia | Borrador de Related Work, sin DOI ni proposición por fuente |
| Apéndice A | Por qué inmunología tensiona | Caso del proyecto con IDs internos (RSD-01, P-GEN-001, E-IDS-FARM) |
| Parte II | Posicionamiento SV-INMUNO | Relato de activos, no-go, roles de IA y hoja de ruta |

Un preprint puede tener las tres capas. Esta pieza las funde. El lector de journal leerá RSD-02 y «paso 9 de Watson» dentro de un supuesto estado del arte. Eso es caminar de espaldas: el manuscrito enseña el taller.

---

## 1. Parte I — qué resiste

Dirección correcta, no original:

- Los LLM completan patrones; la ausencia de dato no se declara sola. El ejemplo CMV-prevalencia → serostatus de receptor es el tipo de inferencia que el corte 31-08 prohíbe.
- CDS por reglas atómicas produce ruido si no hay contexto. Fatiga de alertas es un fenómeno documentado (overrides 49–96 % en revisiones de Sittig y otros; no hace falta inventarlo).
- XAI post-hoc no convierte correlación en causa. El AI Act (Reglamento 2024/1689, consolidado 27-07-2026) y la guía FDA CDS (final enero 2026, reemitida 29-01-2026) existen; la coincidencia «el profesional debe poder revisar la base» está en ambos.
- FHIR/SNOMED/OMOP transportan y nombran; no son un álgebra de composición ni un catálogo de consecuencias de ignorancia. Eso es un hecho de diseño de esos estándares, no un hallazgo.
- Distinguir dato ausente / observación no admisible / conocimiento no constituido es el vocabulario que el proyecto necesita. Como **propuesta**, resiste. Como «ontología que la estadística no ha formalizado», no: hay literatura de *reject option*, *selective classification*, *AI deferral* y abstención en LLMs médicos (p. ej. Machcha et al., EACL 2026; trabajos 2025–2026 de abstención por incertidumbre en texto clínico). El hueco no es «nadie se abstiene». El hueco, si se demuestra, es **abstención con consecuencia constituida ex ante, catálogo congelado y composición dirigida**, no la abstención misma.

Cardinalidad IUIS 559/508 y frontera de dos POE ES: correctas y ya usadas en el frente.

---

## 2. Parte I — dónde se equivoca

**2.1 Citas sin proposición.**  
«Bates et al. y Sittig & Singh documentaron…» No hay año, título, DOI, página ni qué proposición se toma de cada uno. Bates tiene décadas de CDS/CPOE; Sittig & Singh tienen modelo sociotécnico y trabajo de alertas. El defecto es el mismo B-02 que tumba el paquete v0.2: referencia abreviada. Un SoTA que exige a los demás fuente+versión+localizador no puede empezar así.

**2.2 Vacío sobredimensionado (§1.3.3).**  
«No existe en la literatura un formalismo que obligue a la abstención determinista / separe catálogo de motor / genere acta predecisional inmutable.»  
Eso es una pretensión de originalidad sin protocolo de búsqueda. Además omite las **propias** capas SV ya enviadas:

- Non-closure → Royal Society A.  
- Orientation — *Exact Orientation Under Heterogeneous Interfaces*, SMCA-26-08-4316, IEEE TSMC, pre-screening.  
- VII *Interdomain closure certificates…*, JMP26-AR-02262.

Un Related Work de extracción SV debe presentar esas capas con fecha y objeto, más el resultado nuevo. No citarlas aquí es caminar a ciegas respecto de la regla de no repetir objetos ya enviados y respecto de un revisor que sí las verá.

**2.3 Clasificación regulatoria afirmada de más.**  
El bisturí v0.4 decía, bien, que no se prejuzga la clasificación. Qwen afirma que el AI Act clasifica «los sistemas de apoyo al diagnóstico y tratamiento» como alto riesgo, en bloque. El Anexo III no convierte todo CDS en alto riesgo por el lema. La guía FDA distingue CDS no-dispositivo. Frontera, no habilitación.

**2.4 «Lex Artis Ad Hoc europea».**  
La *lex artis* existe en la responsabilidad sanitaria. Capitalizarla como marco europeo unificado de trazabilidad del razonamiento es una etiqueta. No sustituye el artículo del Reglamento ni la Ley 41/2002.

**2.5 Composición no conmutativa como hallazgo de CDS.**  
Que el orden anti-CD20 / vacuna viva importa es clínica elemental. Que los CDS clásicos no modelan `⊙` no conmutativo es cierto como límite. Presentarlo como descubrimiento del SoTA mezcla el álgebra SV (perímetro 2, solo ampliar con G0) con la crítica a Epic/Cerner.

---

## 3. Parte II — errores de hecho sobre el frente

**3.1 Flujo v3 «gobernado».**  
Misma infracción que Watson. v3 no está en artifacts. v2 no pasó entero. No es gobierno vigente.

**3.2 Atribución de piezas.**  
«Watson: producción del universo candidato.» El paquete 64/27/50/40 lo produjo esta unidad; Watson hizo el acta de recepción.  
«Claude: auditoría de repositorios.» A1 lo hizo esta unidad; Claude entregó la cota SCO/3255/2006.  
«Grok: adversarial sobre el bisturí y el flujo.» Eso sí. Falta: producción del candidato, revisión del acta, revisión de Claude.

La división «quien produce no audita» es un principio usable. El reparto concreto está mal.

**3.3 Resultados = 64/27/50/40.**  
§2.5.4 propone un preprint con «resultados basados en los activos candidatos». El acta de recepción y su revisión lo impiden: integridad material sí; incorporación clínica no. Un N de filas no adoptadas no es un resultado. Es inventario.

**3.4 Cerrar n=b² leyendo Fundamentos (§2.5.1).**  
Eso reabre el álgebra, que solo se toca por ampliación expresa o error demostrado. Un preprint de INMUNO no es el lugar. Si hay un reparo B1 en otro manuscrito, se ataca allí, con el texto de Fundamentos abierto. Aquí es G2 por otro camino.

**3.5 Testigo finito.**  
La condición (una O, un E sintético, un SEED, una interfaz, un k con consecuencia) sale de la adversarial al bisturí. Como *condición*, resiste. Como tarea a ejecutar en caliente, no está ordenada y rozaría constitución clínica.

**3.6 Tres capas.**  
Catálogo / estado de episodio / proyección SV solo con G0. Eso resiste y debe conservarse. Qwen lo copia bien.

**3.7 Cierre retórico.**  
«Por primera vez matemáticamente trazable…» no es Related Work. Es lema. El proyecto no se demuestra por unicidad proclamada.

---

## 4. Contexto con el trabajo que hay

Estado real, no el del §2.1 de Qwen:

```text
A1 repos          leído en norma; 0 adoptados
Universo v0.2     64/27/50/40; integridad sí; adopción no
Claude 167        cota ES; experiencia; no parámetro
Bisturí v0.4      candidata; no pasa entero
Flujo v2          no pasa entero como camino único
Flujo v3          no presente aquí
G0 cerrado
G1 G2 abiertos
Paso 9            no hecho
Paso 10           prohibido
Sumisiones SV     non-closure / Orientation / VII  — fuera de este dominio
```

La intersección que Watson nombró sigue siendo el cuello:

```text
requisito profesional  ∩  conocimiento clínico vigente
∩  consecuencia documentada  ∩  posibilidad empírica
```

Qwen no la constituye. La Parte I describe por qué un motor probabilístico no la sustituye. Eso es útil como marco, no como avance de la intersección.

Caminar de espaldas sería: preprint con 64 filas como «resultados», flujo v3 como método, Fundamentos abiertos para matar \(n=b^2\), y Related Work sin las sumisiones propias.  
Caminar a ciegas sería: tratar la Parte I como SoTA cerrado cuando Bates/Sittig no tienen ficha y la abstención médica ya está en la literatura 2025–2026.

---

## 5. Qué debe seguir haciendo esta unidad (opinión, no autoencargo)

No redactar el preprint. No reparar v0.2. No construir el testigo. No leer Fundamentos para cerrar \(n=b^2\).

El punto correcto sigue siendo el de las últimas vueltas: **adversarial de piezas ajenas y defensa de perímetro**.

Sobre esta entrega, el trabajo útil —si se ordena— no es reescribir la Parte II. Es exigir a cualquier SoTA que quiera vivir en un manuscrito:

1. Ficha por afirmación: fuente + año + localizador + proposición extraída. Bates, Sittig, una revisión de fatiga de alertas, IMDRF N41, artículos concretos del AI Act, guía FDA 2026, y al menos una línea de *selective prediction / abstention* médica para no fingir vacío.  
2. Related Work en tres capas: CDS clásico / XAI y regulación / abstención y deferral actuales, **más** las capas SV ya enviadas con fecha y objeto, **más** lo que este trabajo añadiría (consecuencia ex ante + catálogo congelado) sin llamarlo teorema.  
3. Parte II fuera del SoTA: activos y no-go en un anexo de estado de proyecto, no en el cuerpo de un preprint.  
4. Ningún N de candidato como resultado.

Hasta esa orden, esta unidad no produce v0.3 ni v0.5. G0 cerrado.
