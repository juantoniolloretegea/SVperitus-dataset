# Auditoría externa limitada · adenda contrato epistémico IA INMUNO v0.2

- **Auditor:** Grok
- **Fecha:** 02-09-2026
- **Orden aplicada:** `14b39928e0ea20699fc3c833d649a609a0deb3f1` (`Orden_auditoria_externa_adenda_contrato_epistemico_ia_inmunologia_v0.1_2026-09-02.md`)
- **Objetos materiales pedidos por el Director:** commit `87173cde882da4ee0a3eeb382370ac6aa0f58663`
- **Estatuto de esta pieza:** auditoría externa; no es rector; no adopta; no autoriza consejo

La orden fue redactada contra el candidato v0.1 `5ddb4cabe2eb2c4454948beb34095d2885691ad3`. El Director desplazó el objeto a v0.2. Se audita v0.2. No se usa la adversarial interna como prueba. No se reabre el acta de estratificación. No se tocan G2-S1/S2, G3-OBS ni el Lenguaje SV.

## 1. Identidad calculada

| Objeto en `87173cde` | Bytes | SHA-256 |
|---|---:|---|
| `adenda-contrato-epistemico-inferencia-trazable-y-consecuencias-ia-inmunologia-2026-09-02-v0.2.md` | 29 344 | `2d3f87359ba16634fc000dc7aa50a3994f70d7821de4382be0adaa153c7e6ffd` |
| `adversarial-interna-adenda-contrato-epistemico-ia-inmunologia-2026-09-02-v0.2.md` | 13 293 | `6d638f2ee5038af69bd012688ebcd36a4e360687225c8d54d9e4a6ac53bd2147` |

Las huellas de la orden (v0.1: 15 877 / `e82e8ab0…`; 7 155 / `6c52860c…`; README 15 155 / `0af18811…`) **no** corresponden a este corte. README en `87173cde`: 16 145 B, SHA-256 `17856751b626a12650b81675b5fb60a5a64d474fcd11641f37a0e76eb1d435ce`. El commit `87173cde` no modifica el README; sólo las dos piezas v0.2.

Identidad v0.1 de la orden, verificada aparte y no auditada como objeto:

| Objeto en `5ddb4cab` | Bytes | SHA-256 |
|---|---:|---|
| adenda v0.1 | 15 877 | `e82e8ab01bfac61ea2575fb13402eca229907cbae343c9c7d5bd328f90693b79` |
| adversarial v0.1 | 7 155 | `6c52860ccb9870dae84c71eab42672ef0ddd3197323fc9f42ebf415c9451d7e9` |
| README | 15 155 | `0af18811f862bdf67d00f46e97eb706d3aa65a4b00275fffdc481837da31c753` |

## 2. Diff

**v0.1 contra línea base de la orden** (`23b700fa` → `5ddb4cab`): adición de adenda v0.1 y adversarial v0.1; actualización del README. No se reabren actas cerradas, política, catálogos, lotes G2, pilotos, hojas, ITI ni Lenguaje SV.

**v0.2 contra v0.1:** ampliación material. Añade §§3.2–3.8 (determinismo, exclusión de indeterminismo, conectores congelados, canonicalización, reproducibilidad ≠ verdad, reejecución independiente, fallo cerrado, descomposición gobernada), el término `reproducibilidad_exacta_certificada` en `CONSEJO_ADMISIBLE`, campos `Experimento_canonico_ID` y `Certificado_reproduccion`, e invariantes `INV-EPI-17`–`31`.

**Commit auditado `87173cde` contra `7404bf79`:** sólo las dos piezas v0.2 (+61 / −6). Mensaje: *Gobernar fallos y descomposicion canonica*. No toca estratificación, política, G2, catálogos ni Lenguaje SV.

## 3. Dictamen global

**PASA_CON_REPAROS**

Los ataques duros de la orden §22 quedan absorbidos por texto material. El reparo no tumba el contrato; exige un campo estructurado de fuente y localizador en la traza.

## 4. Tabla A–P

| Ataque | Resultado |
|---|---|
| A identidad / regresión | PASA (objeto = v0.2; huellas de la orden = v0.1, declaradas) |
| B completitud vs omnisciencia | PASA |
| C conocimiento latente | PASA |
| D suficiencia nominal | PASA |
| E doble registro | PASA |
| F capturabilidad de la cadena | PASA |
| G privacidad de la cadena | PASA |
| H contenido mínimo de la traza | PASA_CON_REPAROS |
| I racionalización retrospectiva | PASA |
| J consecuencias | PASA |
| K compuerta de consejo | PASA |
| L actualización en episodio | PASA |
| M carga cognitiva | PASA |
| N autoridad y privacidad | PASA |
| O finitud / verificabilidad | PASA |
| P no constitución prematura | PASA |

## 5. Contraejemplos propios B–N

**B.** Interpretar `CORPUS_COMPLETO_RESPECTO_DE_LA_OPERACION` como «toda la inmunología, sin U».  
Absorbed: §§1 y 8; `INV-EPI-03`. Completitud = objetos obligatorios de *esa* operación y corte; hueco conocido = `U` visible.

**C.** Usar pesos, hilo previo o un patrón estadístico como fuente de la profilaxis pre-IS.  
Absorbed: §1.1, `INV-EPI-01`. Nada de eso gobierna hasta resolverse contra el corpus externo.

**D.** Emitir `SUFICIENCIA_RELATIVA_CONSTITUIDA` con corpus huérfano de huella o sin consecuencias.  
Absorbed: §2 lista diez componentes; falta uno → `U` / abstención / escalado, no inferencia.

**E.** Mostrar sólo una prosa convincente y borrar la cadena.  
Absorbed: §3.1, `INV-EPI-14`–`15`. Funciones distintas; ambas obligatorias; discordancia = bloqueo.

**F.** Tratar tokens intermedios como mapa causal de activaciones.  
Absorbed: §3.1 y glosario. Sólo deliberación explícita capturable. Si no hay entorno que la registre: `CADENA_PRIVADA_U` y no hay consejo. El sintagma residual «cadena privada de pensamiento» queda definido operativamente; no promete inspección neuronal.

**G.** La cadena contiene hipótesis descartadas e identificadores del episodio.  
Absorbed: mismo régimen que el episodio; no se muestra por defecto; no entrena ni memoriza otro caso; `INV-EPI-16`. Exigir la cadena no legitima publicarla.

**H.** Traza con «fuentes: literatura reciente» en prosa.  
No absorbido del todo: §7 nombra procedencia dentro de `Entradas` y `Corte_dominio`, pero no un campo `Fuente_ID` / localizador obligatorio. Ver R1.

**I.** Consejo primero; después citas y traza coherente.  
Absorbed: §3.1 (citas a posteriori no cuentan); IDs canónicos derivados del contenido; §3.7 (reejecución independiente sin leer la salida previa); `INV-EPI-05`, `INV-EPI-28`.

**J.** Consejo con ruta y datos, sin consecuencia de retrasar.  
Absorbed: §4 → `CONSECUENCIA_U`; si crítica, no hay consejo (`INV-EPI-07`).

**K.** Ablación de cada conjunción de `CONSEJO_ADMISIBLE`.  
Retirar cualquiera —incluida cadena capturada o `reproducibilidad_exacta_certificada`— obliga `NO_EMITIR_CONSEJO` (§5). El consejo sigue siendo expediente, no decisión (`INV-EPI-13`).

**L.** Guía externa nueva contradice el corpus cargado.  
Absorbed: §6. Cuarentena, filtros, aceptación, suceso versionado. Pendiente ≠ ruta. No aprende en el episodio.

**M.** Volcar cadena + traza al frame inicial.  
Absorbed: §7 e `INV-EPI-12`. Frame conciso; inspección bajo demanda. Concisión no oculta `U` crítica (`INV-EPI-08`).

**N.** Usar la cadena para abrir historias ajenas o una finalidad nueva.  
Absorbed: no altera la tabla de autoridad del acta de estratificación; política transversal intacta; la IA no decide finalidad (`INV-EPI-10`, §6).

## 6. Cadena privada y traza estructurada

La cadena es forense: pasos explícitos, hipótesis emitidas, herramientas, controles. No es justificación normativa ni ontología neuronal.  
La traza es normativa: proyección canónica de entradas, objetos, reglas, `U`, consecuencias, versión y autoridad.  
Vínculo: identificadores derivados del contenido; el ID administrativo vive en sobre externo (§3.1, §3.5).  
Ausencia o discordancia: bloqueo. Una no sustituye a la otra.

## 7. Racionalización retrospectiva

El ataque I prospera contra un modelo que genera prosa *después* del consejo si esa prosa se toma por traza. La adenda lo corta en tres puntos: (1) la traza debe reproducir sucesos ejecutados, no citas añadidas; (2) la cadena y la traza deben concordar; (3) la certificación de reproducción exige reejecutar reglas desde el experimento, no reenviar el texto guardado. Queda vigilancia de implementación (`VIG-EPI-03`, `VIG-EPI-13`): el esquema futuro no puede aceptar un campo libre «explicación».

## 8. Privacidad y conservación

La cadena, si revela el episodio, hereda confidencialidad, mínimo privilegio, finalidad, trazabilidad de acceso y borrado. Prohibida como entrenamiento, memoria u ejemplo. No se publica en el repositorio. Coherente con la política de 02-09-2026. El objeto auditado es impersonal: `PRIVACIDAD_PASA`.

## 9. Reparos

**R1 — menor — error de extracción / esquema.**  
Hoja textual: §7.  
Afirmación atacada: la traza obligatoria cubre entrada, átomo, regla, fuente, transición, `U`, consecuencia, versión y autoridad.  
Contraejemplo: un campo `Entradas` relleno con «serología reciente, gía habitual» satisface la prosa y no identifica fuente ni localizador.  
Consecuencia: la orden §12 no puede verificarse campo a campo.  
Corrección mínima: añadir `Fuente_ID` y `Localizador` (o equivalente tipado) como columnas propias, no como texto libre dentro de `Entradas`.

No hay reparo mayor sobre determinismo: §§3.2–3.8 no afirman que un modelo generativo actual sea reproducible; lo expulsan del camino normativo hasta demostración bit a bit (`INV-EPI-17`–`23`, `INV-EPI-28`).

## 10. Incertidumbres residuales

- **U-CRIT.** «`CONSECUENCIA_U` crítica» no tiene aún umbral constituido. Cierre: `VIG-EPI-04` en fase posterior; no se constituye aquí.
- **U-CERT.** El certificado de reproducción no tiene esquema binario en este corte. Cierre: `VIG-EPI-07` y `VIG-EPI-13` sobre un motor admitido.
- **U-ORDEN.** La orden nombra v0.1; el objeto es v0.2. Cerrada en §1 de esta auditoría.

## 11. Efecto sobre G2-SEM, G3-OBS y Lenguaje SV

Ninguno de constitución. §9: no cierra G2-SEM, no abre G3-OBS, no crea parámetros, observables, matrices, rutas ni frames, no incorpora fuentes en episodio, no modifica el Lenguaje SV. El motor, el IR y el binario quedan *citados* como coordenadas del experimento canónico (`INV-EPI-21`); eso no es escritura del lenguaje.

## 12. Declaración

Esta auditoría no constituye la adenda como rectora, no autoriza consejo clínico, no adopta conocimiento, no abre fase posterior y no implementa el contrato. El estatuto del objeto permanece `RECTOR_CANDIDATO_DE_EJECUCION_EPISTEMICA` hasta el cierre que el Director declare.

Los invariantes `INV-EPI-01`–`16` son verificables uno a uno; `17`–`31` son pruebas de motor y entorno, no tautologías y no exigen abrir G3. No hay circularidad: la reproducibilidad no se presenta como verdad clínica (`INV-EPI-26`, §3.6).
