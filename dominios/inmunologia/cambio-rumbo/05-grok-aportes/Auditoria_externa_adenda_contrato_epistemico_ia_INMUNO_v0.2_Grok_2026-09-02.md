# Auditoría externa limitada · contrato epistémico y reproducción exacta v0.2

- **Fecha:** 02-09-2026
- **Orden única vigente:** `851e8eb01a0f7cf272523eb37a015c41a1c256bb`
- **Línea base inmediata:** `df6b2108466e92dcd304d15db7d9946efb6601c8`
- **Candidato material:** `2ce99c870b2c4a135e4d21a8f42cbc118a753277`
- **Serie reparadora:** `3d434af5276a2b201adf4f20fd936584236ddba6`, `2ce99c870b2c4a135e4d21a8f42cbc118a753277`
- **Estatuto de este informe:** auditoría externa; no rector; no adopción; no autorización asistencial

No se emplean órdenes anteriores ni el informe sustituido como prueba. No se emplea la adversarial interna como evidencia suficiente. No se reabre el acta de estratificación. No se tocan `G2-S1`, `G2-S2`, `G3-OBS` ni el Lenguaje SV.

## 1. Identidad calculada

| Objeto en `2ce99c87` | Bytes decl. | Bytes calc. | SHA-256 |
|---|---:|---:|---|
| adenda v0.2 | 31 380 | 31 380 | `b39d819c1b312772c9845edf67b726f889cdb9b84d491886555427fdf18a3ce8` |
| adversarial interna v0.2 | 14 798 | 14 798 | `bafde6fe52e182e7b0accafe92757088537e809814f5c7ea846366c60f6aa4a1` |
| README `cambio-rumbo` | 16 639 | 16 639 | `7b1c94c109f943bc3cc93335330712ec55055e9425cf1519adcf10cd948ece7a` |

Identidad exacta.

## 2. Diff contra la línea base inmediata

README: idéntico (16 639 B; misma huella).

Adenda: 29 344 → 31 380 B. Añade en §7 `Fuentes_aplicadas` y `Vinculos_de_procedencia`; distingue `Entradas` (dato de episodio) de fuente de conocimiento; tipa `<Fuente_ID, Version_fuente, Huella_fuente, Localizador, Evidencia_ID>`; prohíbe prosa sustitutiva y concatenación multifuente; introduce `TRAZA_DE_FUENTE_NO_PASA`; añade `INV-EPI-32`–`34` y cierra de constitución n.º 11.

Adversarial interna: 13 293 → 14 798 B. Añade ataques G2–G4 (prosa, concatenación, evidencia huérfana) y `VIG-EPI-16`.

La serie `3d434af5` + `2ce99c87` no modifica actas cerradas, política de protección, catálogos, lotes G2, pilotos, hojas, ITI ni Lenguaje SV. El commit de la orden queda fuera del objeto.

## 3. Dictamen global

**PASA_CON_REPAROS**

Los ataques de suficiencia de la orden §32 quedan absorbidos por texto material, incluida la sustitución narrativa de fuentes. El reparo no tumba el contrato: la conjunción `CONSEJO_ADMISIBLE` de §5 no nombra todavía el término de traza de fuente, aunque §7 e `INV-EPI-34` ya bloquean.

## 4. Tabla A–Z

| Ataque | Resultado |
|---|---|
| A identidad / regresión | PASA |
| B completitud vs omnisciencia | PASA |
| C conocimiento latente | PASA |
| D suficiencia nominal | PASA |
| E doble registro | PASA |
| F capturabilidad de la cadena | PASA |
| G privacidad de la cadena | PASA |
| H contenido mínimo y fuentes tipadas | PASA |
| I racionalización retrospectiva | PASA |
| J consecuencias | PASA |
| K compuerta de consejo | PASA_CON_REPAROS |
| L actualización en episodio | PASA |
| M carga cognitiva | PASA |
| N autoridad y privacidad | PASA |
| O finitud / verificabilidad | PASA |
| P no constitución prematura | PASA |
| Q experimento canónico | PASA |
| R error cero | PASA |
| S modelo aparentemente determinista | PASA |
| T herramientas y conectores | PASA |
| U reloj e identificadores | PASA |
| V pensamiento capturable | PASA |
| W plataforma y serialización | PASA |
| X salida lingüística variable | PASA |
| Y reproducción grabada y descomposición | PASA |
| Z determinismo erróneo | PASA |

## 5. Contraejemplos B–Z

**B.** Leer «completo» como inmunología total sin `U`.  
Absorbed: §§1 y 8; `INV-EPI-03`. Completitud = objetos obligatorios de la operación y el corte; hueco conocido = `U` visible.

**C.** Usar pesos, hilo o un patrón como fuente de una profilaxis.  
Absorbed: §1.1, `INV-EPI-01`. Ninguna facilidad lingüística gobierna hasta resolverse contra el corpus externo.

**D.** Etiquetar suficiencia sin huella de corpus o sin consecuencias.  
Absorbed: §2, diez componentes; falta uno → `U`, abstención o escalado.

**E.** Sustituir la traza por prosa y borrar la cadena.  
Absorbed: §3.1, `INV-EPI-14`–`15`. Funciones distintas; ambas obligatorias; discordancia = bloqueo.

**F.** Tomar tokens intermedios por mapa causal neuronal.  
Absorbed: §3.1 y glosario. Sólo deliberación explícita capturable. Sin captura: `CADENA_PRIVADA_U` y no hay consejo. El sintagma «cadena privada de pensamiento» queda definido operativamente.

**G.** Cadena con identificadores del episodio, hipótesis descartadas e instrucciones de sistema.  
Absorbed: mismo régimen que el episodio; no se muestra por defecto; no entrena ni memoriza otro caso; `INV-EPI-16`. Exigir el registro no autoriza publicarlo.

**H.** «Literatura reciente» dentro de `Entradas`; un solo localizador para dos fuentes; regla sin `Evidencia_ID`.  
Absorbed: §7; `INV-EPI-32`–`34`. Campos atómicos; registros separados; vínculo obligatorio; `TRAZA_DE_FUENTE_NO_PASA` bloquea.

**I.** Consejo primero; citas y traza después.  
Absorbed: §3.1; identificadores derivados del contenido; §3.7 (reejecución independiente); `INV-EPI-05`, `INV-EPI-28`.

**J.** Ruta y datos presentes; falta consecuencia de retrasar.  
Absorbed: §4 → `CONSECUENCIA_U`; si crítica, no hay consejo (`INV-EPI-07`).

**K.** Ablación de cada término de `CONSEJO_ADMISIBLE`.  
Cada término listado, al retirarse, obliga `NO_EMITIR_CONSEJO` (§5). El consejo permanece expediente (`INV-EPI-13`). Reparo: la conjunción no incluye `traza_de_fuente_pasa`. Ver R1.

**L.** Guía externa nueva contradice el corpus cargado.  
Absorbed: §6. Cuarentena, filtros, aceptación, suceso. Pendiente ≠ ruta.

**M.** Volcar cadena y traza al frame inicial.  
Absorbed: §7, `INV-EPI-12`. Concisión permitida; `U` crítica no se oculta (`INV-EPI-08`).

**N.** Usar la cadena para abrir historias ajenas o una finalidad nueva.  
Absorbed: no altera la tabla de autoridad del acta de estratificación; política transversal intacta; la ejecución no decide finalidad (`INV-EPI-10`, §6).

**O.** Los 34 invariantes.  
Verificables uno a uno. `01`–`16` y `32`–`34` son de expediente y autoridad. `17`–`31` son pruebas de motor y entorno, asignables a bancos futuros, no tautológicas y no exigen abrir `G3-OBS`. No hay circularidad: reproducibilidad ≠ verdad (`INV-EPI-26`).

**P.** Usar la adenda para abrir observables.  
Absorbed: §9. Prohibiciones expresas.

**Q.** Mismos valores clínicos; una solicitud resuelve y otra descompone.  
Absorbed: §3.5 y `Solicitud_y_granularidad_canonicas`. Son experimentos distintos. La segunda exige átomos, reglas y consecuencias ya constituidos (§3.8, `INV-EPI-30`–`31`). Alterar un solo componente del `EXPERIMENTO_CANONICO` produce otro experimento.

**R.** Dos frames que difieren en el orden de dos posiciones; o corrupción de memoria con salida plausible.  
Absorbed: `ERROR_DE_REPRODUCCION = 0`; `REPRODUCIBILIDAD_NO_PASA`. Avería → `EJECUCION_TECNICA_NO_VALIDA`; no hay respuesta clínica alternativa (`INV-EPI-29`).

**S.** Temperatura cero como prueba de determinismo.  
Absorbed: §3.3. No basta. Componente sin identidad exacta = fuera del camino normativo.

**T.** Conector que cambia; herramienta versionada; calibración que altera el valor; servicio no reproducible.  
Absorbed: §3.4. Congelación, huella, incorporación previa. Calibración forma parte de la entrada. Conector vivo no calcula.

**U.** Hora de repetición o UUID en la cadena.  
Absorbed: §§3.2–3.5, `INV-EPI-24`. Fuente temporal = entrada. ID administrativo = sobre externo.

**V.** Mismo frame por dos cadenas distintas.  
Absorbed: `INV-EPI-17`, `INV-EPI-22`. Se exige identidad de la deliberación capturable, no equivalencia de conclusión. No hay acceso neuronal completo.

**W.** Dos plataformas con distinta coma flotante o Unicode.  
Absorbed: §3.3, `INV-EPI-23`. Identidad byte a byte o exclusión de la plataforma. El requisito no es contradictorio: es un predicado de admisión de motor, no una afirmación sobre hardware arbitrario.

**X.** Misma traza; coletilla generativa distinta.  
Absorbed: §3.5, `INV-EPI-25`, `INV-EPI-27`. Todo lo visible en modo consejo pertenece a la salida canónica.

**Y.** Devolver la caché; o elegir la partición «más natural».  
Absorbed: §3.7, `INV-EPI-28` → `PRUEBA_DE_REPRODUCCION_INVALIDA`. Descomposición sin regla canónica → `U` o `FUERA_DEL_CORPUS_CONSTITUIDO` (`INV-EPI-31`).

**Z.** Regla falsa siempre idéntica.  
Absorbed: §3.6, `INV-EPI-26`. Error cero no prueba verdad clínica ni autoriza asistencia.

## 6. Cadena privada y traza estructurada

Cadena: objeto forense de pasos explícitos, herramientas y controles.  
Traza: objeto normativo de entradas, fuentes tipadas, vínculos, reglas, `U`, consecuencias, versión y autoridad.  
Vínculo: identificadores canónicos derivados del contenido; el identificador administrativo permanece en sobre externo.  
Una no sustituye a la otra. Ausencia o discordancia bloquea.

## 7. Racionalización retrospectiva

Queda cortada por tres exigencias simultáneas: la traza reproduce sucesos ejecutados, no citas añadidas; concuerda con la cadena; la certificación exige reejecutar reglas sin leer la salida previa. Un campo libre «explicación» no cuenta.

## 8. Privacidad y conservación

Si la cadena revela el episodio, hereda confidencialidad, mínimo privilegio, finalidad, trazabilidad de acceso y borrado. Prohibida como entrenamiento, memoria, ejemplo o objeto público. El texto auditado es impersonal. `PRIVACIDAD_PASA`.

## 9. Determinismo, experimento canónico y error cero

`EXPERIMENTO_CANONICO` es una tupla cerrada. Igualdad = igualdad de esa tupla, no semejanza narrativa.  
`SALIDA_CANONICA` incluye cadena, traza, transiciones, estados, consecuencias, compuerta y frames.  
Cualquier diferencia, incluida serialización, produce `REPRODUCIBILIDAD_NO_PASA`.  
Un modelo generativo actual no queda declarado reproducible; queda expulsado del camino normativo hasta demostración bit a bit.

## 10. Herramientas, conectores, calibración y plataformas

Nada vivo calcula. El resultado externo se congela, se fecha con fuente temporal explícita, se serializa, se identifica por huella y entra como artefacto del experimento. Cambio de contenido = otro experimento. Plataforma sin garantía bit a bit = fuera.

## 11. Diferencia mínima

Orden de dos posiciones, un punto de Unicode o un estado ternario distinto invalidan la reproducción. No existe equivalencia aproximada.

## 12. Fallo técnico cerrado

Corrupción, pérdida de integridad o indisponibilidad no redefinen la función semántica. Producen `EJECUCION_TECNICA_NO_VALIDA`. No hay salida clínica alternativa. Una `U` clínica no se usa para disfrazar la avería.

## 13. Descomposición y granularidad

Cambio de granularidad = otra operación, declarada en `Solicitud_y_granularidad_canonicas`. Exige átomos, reglas, restricciones, consecuencias y forma canónica previos. Sin regla única: `U` o `FUERA_DEL_CORPUS_CONSTITUIDO`. No se inventan átomos en el episodio.

## 14. Fuentes, localizadores, evidencias y vínculos

| Campo | Verificación |
|---|---|
| `Entradas` | dato de episodio; no sustituye fuente de conocimiento |
| `Fuentes_aplicadas` | registros ordenados de cinco campos atómicos |
| `Fuente_ID` | identificador de fuente; no prosa |
| `Version_fuente` | versión de esa fuente |
| `Huella_fuente` | integridad del texto o artefacto usado |
| `Localizador` | exclusivo de su `Fuente_ID`; no concatenable |
| `Evidencia_ID` | unidad que sostiene un elemento |
| `Vinculos_de_procedencia` | `Evidencia_ID` → `Objeto_ID` / `Regla_ID` / `Transicion_ID` / `Consecuencia_ID` |
| ausencia / concatenación / discordancia | `TRAZA_DE_FUENTE_NO_PASA` y bloqueo |

La lista mínima de transición del §3 sigue nombrando «procedencia» en prosa; el expediente de §7 la tipa. El gobierno efectivo está en §7 e `INV-EPI-32`–`34`.

## 15. Reparos

**R1 — menor — conjunción incompleta.**  
Texto: §5, `CONSEJO_ADMISIBLE`.  
Afirmación atacada: la compuerta enumera todas las condiciones necesarias para emitir consejo.  
Contraejemplo: implementación que evalúa sólo la conjunción de §5 y omite comprobar `Fuentes_aplicadas` / `Vinculos_de_procedencia`.  
Consecuencia: §7 e `INV-EPI-34` bloquearían, pero la fórmula de §5 no lo nombra.  
Corrección mínima: añadir `traza_de_fuente_pasa` (o `¬TRAZA_DE_FUENTE_NO_PASA`) como conjunción de `CONSEJO_ADMISIBLE`.

El reparo de fuente narrativa del informe anterior queda cerrado por la serie `3d434af5` + `2ce99c87`.

## 16. Incertidumbres residuales

- **U-CRIT.** Umbral de `CONSECUENCIA_U` crítica no constituido. Cierre: esquema de criticidad en fase posterior; no aquí.
- **U-CERT.** Certificado de reproducción sin esquema binario. Cierre: banco de reejecución independiente sobre un motor admitido.
- **U-SCHEMA.** Esquema serial de `Fuentes_aplicadas` y `Vinculos_de_procedencia` no fijado como tipo. Cierre: tipado de implementación, sin abrir `G3-OBS`.

## 17. Efecto sobre G2-SEM, G3-OBS y Lenguaje SV

Ninguno de constitución. §9: no cierra `G2-SEM`, no abre `G3-OBS`, no crea parámetros, observables, matrices, rutas ni frames, no incorpora fuentes en episodio, no modifica el Lenguaje SV. Motor, IR y binario figuran como coordenadas del experimento (`INV-EPI-21`); eso no es escritura del lenguaje.

## 18. Declaración

Este informe no constituye la adenda como rectora, no autoriza consejo clínico, no adopta conocimiento, no abre fase posterior y no implementa el contrato. El estatuto del objeto permanece `RECTOR_CANDIDATO_DE_EJECUCION_EPISTEMICA` hasta el cierre que declare la autoridad funcional competente.
