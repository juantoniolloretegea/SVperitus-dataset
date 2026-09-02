# Orden única de auditoría externa — `G4-S1` consecuencias de errores sobre glucocorticoides v0.1

## 1. Objeto exacto

Audite exclusivamente el contenido material de:

| Objeto | Bytes | SHA-256 |
|---|---:|---|
| `Lote_consecuencias_G4-S1_corticoides_OP-IMM-001_v0.1_2026-09-02.md` | 14 792 | `9ccaf6a544a669c08678e72ea5d3cb8beac5db531db5d4ecf482d10830974e25` |
| `Adversarial_interna_G4-S1_corticoides_OP-IMM-001_v0.1_2026-09-02.md` | 5 784 | `29dbf86e7ffa87188936718e2a0db6090c23bd9aebdd748e05e4810347b9569d` |
| `Recepcion_y_cierre_auditoria_externa_G3-S1_corticoides_OP-IMM-001_v0.1_2026-09-02.md` | 3 216 | `c83f8c04155aedd18c59841620d0efb2c2af1282cb5c3839631e3f06fd38dc7c` |

Directorio principal:

`dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/09-consecuencias-en-evaluacion/`

La recepción G3 se encuentra en el directorio `08-observables-en-evaluacion`. Calcule bytes y SHA-256 de los tres objetos desde el commit candidato. Identifique ese commit y su línea base. Esta orden queda fuera del objeto auditado.

## 2. Regla de suficiencia

Para cada ataque B–L debe construir al menos un contraejemplo material. No basta con resumir el lote, copiar la adversarial interna o declarar que el texto es prudente.

Toda afirmación clínica debe contrastarse en la fuente declarada, con versión, localizador y fuerza exacta. Si una fuente no se abre, declare `U_ACCESO`; no complete por memoria.

## 3. Ataque A — identidad y regresión

Compruebe:

1. bytes y SHA-256 de los tres objetos;
2. diff completo contra la línea base;
3. que sólo se añaden la recepción G3, el lote G4, su adversarial, esta orden y el cambio mínimo del README;
4. que no cambian `G3-S1`, catálogo v0.8, `Q0`, G2, contrato matemático, pilotos, política de protección, ITI ni Lenguaje SV;
5. que siguen en cero parámetros atómicos, matrices, rutas y frames.

## 4. Ataque B — cierre válido de la dependencia

Verifique que la recepción corresponde exactamente al candidato G3 auditado en `3117bcebac5280acf9b9878efa4d40a9fa67edf0`, conserva sus dos huellas y refleja el dictamen externo `PASA`, diez observables necesarios, cuatro normalizadores, once causas de `U` y cero reparos.

Ataque si se usa el cierre para introducir contenido no auditado o para abrir automáticamente `G5-ATM`.

## 5. Ataque C — fuentes clínicas

Abra y contraste:

- CDC, *Altered Immunocompetence*, versión indicada;
- CDC, *Pneumocystis Pneumonia Basics*, versión indicada;
- Fragoulis et al., recomendaciones EULAR 2022, PMID 36328476, DOI 10.1136/ard-2022-223335.

Determine si sostienen, con la fuerza utilizada:

1. distinción entre seguridad de vacunas vivas y efectividad vacunal;
2. posibilidad de complicaciones graves en personas con inmunocompetencia alterada que reciben ciertas vacunas vivas;
3. posible efectividad reducida y eventual repetición en contextos definidos;
4. gravedad potencial de PJP y relación con inmunodepresión farmacológica por corticoides;
5. existencia de una valoración preventiva contextual, no de una profilaxis universal.

Prohibido trasladar cifras, umbrales o recomendaciones de una finalidad a otra.

## 6. Ataque D — cinco consecuencias y dos clases

Compruebe que existen exactamente:

- `CON-GC-REP-001`;
- `CON-GC-PUR-001`;
- `CON-GC-VAC-SAF-001`;
- `CON-GC-VAC-EFF-001`;
- `CON-GC-PJP-001`.

Clasifique cada una como `CONSECUENCIA_EPISTEMOLOGICA_VALIDA`, `CONSECUENCIA_CLINICA_POTENCIAL_VALIDA`, `DUPLICADA`, `SALTO_CAUSAL`, `NO_SOSTENIDA` o `U_NO_ADJUDICABLE`.

## 7. Ataque E — cadena completa

Para cada consecuencia verifique la cadena:

`observable/U -> error -> daño epistemológico -> finalidad -> consecuencia clínica potencial, si existe`.

Construya casos donde:

- falta un observable pero no ocurre daño clínico;
- existe daño clínico por otra causa;
- la exposición está bien representada pero la regla de finalidad es incorrecta;
- el plan y la administración discrepan;
- una cita correcta se añade después a una conclusión no trazada.

Un daño clínico no puede declararse consumado por la sola existencia del error.

## 8. Ataque F — seguridad frente a efectividad vacunal

Intente fusionar o intercambiar `CON-GC-VAC-SAF-001` y `CON-GC-VAC-EFF-001`.

Compruebe que:

- seguridad se refiere a la complicación potencial propia de vacunas vivas en el contexto aplicable;
- efectividad se refiere a respuesta subóptima y eventual necesidad de revisión o repetición conforme a regla autorizada;
- ninguna afirma que toda vacuna sea insegura o ineficaz;
- ninguna prescribe vacuna, aplazamiento, repetición o intervalo.

## 9. Ataque G — PJP sin profilaxis automática

Ataque `CON-GC-PJP-001` con:

- exposición breve o local;
- glucocorticoide sin otros modificadores conocidos;
- otros inmunosupresores presentes;
- regla EULAR trasladada a población no cubierta;
- falso positivo que conduciría a una intervención innecesaria.

Compruebe que el lote sólo constituye la consecuencia de omitir una valoración cuando corresponda y la gravedad potencial de PJP. Debe mantener abiertas la regla, población, modificadores, umbral, balance e intervención.

## 10. Ataque H — finalidad y equivalencia

Intente usar:

1. dosis diaria definida ATC;
2. prednisona-equivalente memorizada;
3. promedio de pulsos;
4. umbral CDC vacunal para PJP;
5. intervalo EULAR para vacunación.

El lote debe producir `U(EQUIVALENCIA)`, `U(FINALIDAD)` o rechazo, no una clasificación clínica.

## 11. Ataque I — criticidad, compensación y dirección del error

Compruebe que `ALTA_POTENCIAL` no es probabilidad, puntuación, veto ejecutable ni certeza individual. Construya un intento de compensar una consecuencia grave mediante coste, tiempo o disponibilidad y verifique que fracasa.

Compruebe también que los falsos positivos no se ignoran ni reciben consecuencias clínicas inventadas.

## 12. Ataque J — trazabilidad anterior a la conclusión

Verifique que toda consecuencia puede expresar antes de concluir: `Consecuencia_ID`, observable o `U`, valor y procedencia, error, fuente clínica y localizador, finalidad, transición, incertidumbres, versión y autoridad.

Construya una conclusión clínicamente plausible con cita posterior pero sin esa cadena. Debe resultar no admisible.

## 13. Ataque K — determinismo y fallo técnico

Modele dos ejecuciones con idéntica entrada canónica, horizonte, fuentes, versiones, finalidad y autoridad. Consecuencia, cadena, `U`, localizadores, orden y serialización deben coincidir byte a byte.

Una variación material debe generar otra entrada canónica. Un fallo de herramienta sólo puede producir `EJECUCION_TECNICA_NO_VALIDA`.

## 14. Ataque L — privacidad, finitud y no avance

Compruebe que los objetos son impersonales y no contienen episodios, personas o centros identificables.

Verifique que el lote:

- termina en cinco consecuencias;
- no abre efectos adversos generales, costes, organización, cohortes o reglas institucionales;
- no constituye dosis, umbrales, equivalencias, profilaxis, vacunación o tratamiento;
- no crea parámetros atómicos, matrices, rutas o frames;
- no abre `G5-ATM`;
- no modifica el Lenguaje SV ni autoriza asistencia.

## 15. Recuentos obligatorios

Entregue recuento calculado de:

- cinco consecuencias;
- dos epistemológicas;
- tres clínicas potenciales;
- tres fuentes clínicas;
- cero umbrales;
- cero equivalencias;
- cero intervenciones prescritas;
- cero parámetros atómicos;
- cero matrices, rutas y frames.

## 16. Entrega

Emita una sola auditoría con:

1. identidad calculada y diff exacto;
2. dictamen `PASA`, `PASA_CON_REPAROS`, `NO_PASA` o `U_AUDITORIA_INCOMPLETA`;
3. tabla de ataques A–L;
4. contraejemplo material por ataque B–L;
5. clasificación individual de las cinco consecuencias;
6. reparos numerados con severidad, objeto, texto, evidencia, consecuencia y corrección mínima;
7. incertidumbres residuales y operación exacta de cierre;
8. recuentos verificados;
9. declaración separada de si `G4-S1_CERRABLE`;
10. declaración expresa de que el dictamen no autoriza abrir `G5-ATM`.

## 17. Límites

- No escribir en GitHub.
- No abrir PR.
- No tocar `main`.
- No modificar los objetos.
- No buscar cohortes ni abrir estado del arte.
- No añadir consecuencias, dosis, umbrales o intervenciones.
- No diseñar parámetros, matrices, rutas o frames.
- No usar episodios reales como ejemplos.
- No confundir gravedad potencial con causalidad individual.
- No convertir una cita decorativa en trazabilidad.
