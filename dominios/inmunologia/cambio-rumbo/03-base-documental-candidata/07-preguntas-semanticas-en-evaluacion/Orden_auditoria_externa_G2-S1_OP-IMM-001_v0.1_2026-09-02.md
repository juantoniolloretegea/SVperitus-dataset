# Orden de auditoría externa G2-S1 — OP-IMM-001 v0.1

## 1. Mandato

Realice una auditoría adversarial externa, limitada e independiente del primer lote semántico `G2-S1` de `OP-IMM-001`. Debe intentar falsar el objeto, no completarlo ni mejorarlo por iniciativa propia.

El resultado máximo autorizado es cerrar `G2-S1`. Esta auditoría no puede cerrar todo `G2-SEM`, abrir `G3-OBS`, constituir parámetros, elegir pruebas, fijar valores `0/1/U`, crear matrices, consecuencias clínicas, rutas críticas o frames, ni modificar el Lenguaje SV.

## 2. Identidad invariable

- **Repositorio:** `juantoniolloretegea/SVperitus-dataset`
- **Rama:** `dominio-inmunologia`
- **Commit material auditado:** `48b8a34c9f55832b7925a2391782e5d88c1b96bb`
- **Línea base — G1 cerrada:** `90938ec90bd086b69a0ffba683d23419cd8c8326`
- **Fecha de corte:** 02-09-2026

Objetos principales y SHA-256:

| Objeto | SHA-256 |
|---|---|
| `Lote_semantico_G2-S1_OP-IMM-001_v0.1_2026-09-02.md` | `fafe7938833941ed96baa09e2e356980fb61a25a62d8ca23d3d038a78d7a0d74` |
| `Adversarial_interna_G2-S1_OP-IMM-001_v0.1_2026-09-02.md` | `5658f20f00d44b29a9ef35e3554af73f76d8d72512108ea2a951f65114967559` |
| `07-preguntas-semanticas-en-evaluacion/README.md` | `3587b2aa3b3b63172ded7b6a91cf8dc5e666cd8ceb8eb5ba9518723987f0325d` |
| `cambio-rumbo/README.md` | `3c76808851c99df9515bc6fe3c92b8167937a639fe714a1b2d5511c62ec0bf75` |

No audite una copia, transcripción o commit posterior. Si no puede fijar esta identidad, emita `U_AUDITORIA_INCOMPLETA`.

## 3. Ataque A — Identidad y regresión

Compare directamente el commit material con la línea base. Verifique que el cambio se limita a:

1. crear los tres objetos de `07-preguntas-semanticas-en-evaluacion`;
2. añadir su entrada al `README.md` de `cambio-rumbo`;
3. no modificar el catálogo INMUNO v0.8, el cierre G1, las hojas de cálculo, las ITI, los pilotos `IMMUNO-1`/`IMMUNO-2`, el Lenguaje SV ni cualquier otro objeto heredado.

Enumere toda diferencia fuera de ese perímetro como reparo.

## 4. Ataque B — Perímetro de G2-S1

Determine si el lote se limita realmente a formular preguntas semánticas candidatas. Busque cualquier constitución prematura de:

- parámetro clínico;
- observable o prueba;
- unidad, umbral, ventana o fuente definitiva;
- regla de suficiencia;
- transductor `0/1/U`;
- consecuencia clínica plena o gravedad;
- atomicidad;
- propiedad matricial, ruta crítica o frame;
- indicación, recomendación o actuación asistencial.

No trate la mera posibilidad de una `U` como transductor constituido.

## 5. Ataque C — Integridad del lote

Compruebe que existen exactamente **23 identificadores canónicos únicos**:

- 1 `SEM-RUT`;
- 4 `SEM-CTX`;
- 5 `SEM-EXP`;
- 4 `SEM-HUE`;
- 4 `SEM-BAR`;
- 5 `SEM-HIS`.

Para cada pregunta, verifique que contiene: formulación canónica candidata, función provisional, dependencia con `OP-IMM-001`, posibilidad de incertidumbre propia y exclusión expresa. Señale duplicados, preguntas compuestas ocultas, dependencias no demostradas o ausencias.

## 6. Ataque D — Semántica abierta frente a ambigüedad defectuosa

Ataque especialmente los términos «pertinente», «activo», «grave», «oportunista», «recurrente», «magnitud», «duración», «aplicable» y «viable». Dictamine, para cada uno, si:

1. puede permanecer legítimamente abierto hasta una puerta posterior; o
2. impide distinguir la pregunta y constituye un defecto de `G2-S1`.

No cierre la ambigüedad inventando pruebas, umbrales, ventanas ni capacidades institucionales.

## 7. Ataque E — Control, contexto y responsabilidad asistencial

Revise individualmente `SEM-RUT-001` y `SEM-CTX-001` a `SEM-CTX-004`.

Debe comprobar:

1. que una posible infección en curso opera como control de salida y no como vértice basal;
2. que el momento previsto procede de la decisión terapéutica de origen y no importa al perfil toda la carga o urgencia de la enfermedad;
3. que la entidad nosológica y su terminología versionada son contexto y no diagnóstico ejecutado por el sistema;
4. que CIE-11 —Clasificación Internacional de Enfermedades, 11.ª revisión—, la condición de enfermedad rara y la etiqueta «inmunoterapia» no asignan automáticamente indicación, servicio responsable o competencia profesional;
5. que `SEM-CTX-003` registra quién dirige el episodio y qué participación de Inmunología está profesionalmente solicitada o acordada, pero no fabrica esa adjudicación;
6. que permite dirección principal, compartida, consultiva, diferida o ausencia de participación de Inmunología sin imponer la organización de un hospital o país;
7. que una necesidad inmunológica no equivale a transferencia del liderazgo clínico;
8. que una petición del paciente no crea indicación ni transfiere responsabilidad, aunque la autonomía y el consentimiento deban gobernarse en otra compuerta;
9. que `SEM-CTX-004` diferencia necesidad clínica general y ejecución institucional viable;
10. que un protocolo interno, los medios o la experiencia del centro pueden modificar ruta, calendario, consulta o derivación, pero no el estado biológico ni la necesidad clínica;
11. que la incompatibilidad local se hace visible y se remite a decisión profesional, sin compensarla ni ocultarla;
12. que «customización» sólo es un alias de taller de contextualización clínica e institucional gobernada y no una construcción del Lenguaje SV;
13. que una propuesta principal de quimioterapia citotóxica para neoplasia hematológica sigue fuera de `OP-IMM-001` aunque la enfermedad esté bien tipada o sea rara;
14. que una propuesta terapéutica posterior materialmente distinta exige nueva adjudicación de alcance y episodio versionado, sin reescribir retrospectivamente el anterior.

Ataque con, al menos, estos casos de divergencia:

- Hematología dirige y solicita una valoración inmunológica acotada;
- dos hospitales terciarios distribuyen de modo diferente la coordinación del mismo tipo de problema;
- el paciente solicita una intervención que no está profesionalmente indicada;
- existe un código nosológico exacto, enfermedad rara y tratamiento denominado inmunoterapia;
- el régimen inicial queda fuera de G1 y aparece después una propuesta farmacológica distinta;
- la actuación clínicamente indicada no es ejecutable conforme al protocolo o los medios del centro;
- un protocolo interno permite una actuación que el procedimiento general no sostiene.

## 8. Ataque F — Exposición propuesta

Compruebe que identidad, magnitud, duración, exposiciones concurrentes o previas y glucocorticoides sistémicos pueden variar independientemente. Ataque especialmente:

- si `SEM-EXP-004` es un conjunto encubierto que exigiría identidades separadas después;
- si «clínicamente activa» oculta una ventana ya decidida;
- si magnitud o duración presuponen dosis, equivalencia o umbral;
- si alguna pregunta elige o recomienda tratamiento.

## 9. Ataque G — Estado del huésped

Compruebe:

- que `SEM-HUE-001` no colapsa recuentos o subpoblaciones linfocitarias aún no adjudicadas;
- que inmunoglobulina G cuantitativa y respuesta humoral específica son separables;
- que vacunación administrada no equivale a protección demostrada;
- que anatomía esplénica, tamaño esplénico y función esplénica no se cierran mutuamente;
- que la duda sobre separar pérdida anatómica y disfunción se conserva para `G3-OBS`/`G5-ATM` y no se resuelve por el caso particular del Director.

## 10. Ataque H — Barreras, materiales, historia y exposición

Construya casos que intenten hacer colisionar:

- piel y mucosa;
- dispositivo intravascular y prótesis o biomaterial;
- infección grave, oportunista y recurrente;
- colonización, infección activa y exposición sanitaria previa.

Compruebe que los mismos hechos futuros podrán alimentar propiedades distintas mediante relaciones tipadas sin duplicar la historia clínica.

## 11. Ataque I — Finitud y cobertura

Determine si la exclusión temporal de neutrófilos, comorbilidades, epidemiología, vacunación, profilaxis, suficiencia global, consentimiento, pruebas, intervenciones y seguimiento es legítima para un primer lote de colisiones o produce una omisión estructural que impida cerrar `G2-S1`.

La auditoría debe distinguir:

- `G2-S1_CERRABLE`: este lote concreto resiste;
- `G2_TOTAL_NO_CERRADO`: aún hacen falta lotes semánticos posteriores.

Prohibido interpretar el cierre de `G2-S1` como cierre del universo de preguntas o autorización para abrir `G3-OBS`.

## 12. Ataque J — No herencia y no contaminación

Verifique que ningún identificador `Pxx`, valor, capa, umbral, dimensión, regla `T(25)`, matriz o conclusión de `IMMUNO-1`/`IMMUNO-2` se ha convertido en autoridad. Los pilotos sólo pueden actuar como señales para localizar colisiones.

Verifique asimismo que:

- no se incorporan cohortes ni microdatos;
- no se importan guías de una enfermedad particular para gobernar el lote;
- el caso personal del Director sólo se usa como contraejemplo adversarial y no como patrón;
- costes, tiempos o recursos no compensan riesgo clínico ni deciden la verdad del perfil;
- no se modifica ni anticipa el Lenguaje SV.

## 13. Entrega obligatoria

Entregue una sola auditoría con:

1. identidad calculada;
2. dictamen: `PASA`, `PASA_CON_REPAROS`, `NO_PASA` o `U_AUDITORIA_INCOMPLETA`;
3. tabla A–J;
4. recuento y lista de los 23 identificadores;
5. reparos numerados con severidad, objeto, texto atacado, evidencia y corrección mínima;
6. incertidumbres residuales con causa y operación de cierre;
7. declaración separada sobre `G2-S1_CERRABLE` y `G2_TOTAL_NO_CERRADO`;
8. identificación del siguiente lote semántico mínimo necesario, sin redactarlo ni abrirlo;
9. declaración expresa de que el dictamen no constituye adopción clínica, recomendación asistencial, parámetro, matriz ni autorización para `G3-OBS`.

## 14. Límites operativos

- No escribir en GitHub.
- No crear ni modificar archivos.
- No crear PR.
- No tocar `main`.
- No buscar una cohorte.
- No completar el dominio por conocimiento general.
- No recomendar tratamientos, vacunas, profilaxis o pruebas.
- No convertir diferencias organizativas entre hospitales en diferencias biológicas.
- Ninguna conclusión sin localizador verificable en el objeto auditado.
