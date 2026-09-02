# Orden única de auditoría externa — `G4-S2` consecuencias sobre cuantificación linfocitaria v0.1

## 1. Objeto exacto

Audite exclusivamente el contenido material de:

| Objeto | Bytes | SHA-256 |
|---|---:|---|
| `Lote_consecuencias_G4-S2_compartimento_linfocitario_OP-IMM-001_v0.1_2026-09-02.md` | 13 023 | `f94983a51bac907deeb2c7b152b0b9316260196b5b8b5bdf347a5ca6b57750e9` |
| `Adversarial_interna_G4-S2_compartimento_linfocitario_OP-IMM-001_v0.1_2026-09-02.md` | 5 029 | `d26872a1b38441c63439115f98ecb4cedff294c423f274656720ec5afdfe03b2` |
| `Recepcion_y_cierre_auditoria_externa_G3-S2_compartimento_linfocitario_OP-IMM-001_v0.1_2026-09-02.md` | 3 025 | `dd19109211f039e4745ff199db56c6b5718333e8cd23690dc140c26459029125` |

Directorio principal:

`dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/09-consecuencias-en-evaluacion/`

La recepción G3 está en `08-observables-en-evaluacion`. Calcule bytes y SHA-256 desde el commit candidato, identifique ese commit y su línea base. Esta orden queda fuera del objeto auditado.

## 2. Regla de suficiencia

Para cada ataque B–M construya al menos un contraejemplo material. No basta resumir el lote, copiar la adversarial interna o declarar prudencia.

Toda afirmación clínica debe contrastarse en la fuente declarada con versión, localizador, diseño, población y fuerza exacta. Si no accede a una fuente, declare `U_ACCESO`; no complete por memoria ni por fuentes secundarias.

## 3. Ataque A — identidad y regresión

Compruebe:

1. bytes y SHA-256 de los tres objetos;
2. diff completo contra la línea base inmediata;
3. que sólo se añaden recepción G3, lote G4, adversarial, esta orden y cambio mínimo del README;
4. que no cambian `G3-S2`, `G4-S1`, catálogo v0.8, `Q0`, G2, `NA0-MATH`, pilotos, política, ITI ni Lenguaje SV;
5. que siguen en cero parámetros atómicos, matrices, rutas y frames.

## 4. Ataque B — cierre válido de G3-S2

Verifique que la recepción corresponde al candidato `b452975436ab837db5b0b8b914fed486b52c8740`, reproduce las tres huellas del dictamen de Grok y no introduce contenido observacional nuevo.

Compruebe directamente que la ficha pública de CLSI `H42` declara reafirmación en junio de 2017. Si la declaración existe, `U-REAFIRMA` fue una limitación del auditor y debe quedar cerrada; no puede conservarse como incertidumbre del objeto.

Verifique que `U-FUNCION` y `U-ALTERACION` sí permanecen abiertas y que el cierre no abre automáticamente `G5-ATM`.

## 5. Ataque C — fuentes y fuerza probatoria

Abra y contraste:

- Warny et al., PLOS Medicine 2018, DOI `10.1371/journal.pmed.1002685`, PMID `30383787`;
- CDC, *Altered Immunocompetence*, versión indicada, sólo `General Principles`;
- CLSI `H42-A2`, ficha, `Abstract` y `Scope` públicos.

Determine si sostienen exactamente:

1. una asociación poblacional entre la categoría definida por Warny et al. y hospitalización por infección y muerte relacionada con infección;
2. la negación expresa de inferencia causal por el diseño observacional;
3. la separación entre números, subpoblaciones y ensayos funcionales;
4. la necesidad de conservar método y calidad para comparabilidad;
5. la ausencia de un intervalo universal autorizado por CLSI.

Ataque cualquier ampliación a causalidad, persona individual, población inmunosuprimida, subpoblación concreta, diagnóstico o actuación.

## 6. Ataque D — cinco consecuencias y dos clases

Compruebe que existen exactamente:

- `CON-LYM-ID-001`;
- `CON-LYM-MAG-001`;
- `CON-LYM-TIME-001`;
- `CON-LYM-FUN-001`;
- `CON-LYM-INF-001`.

Clasifique cada una como `CONSECUENCIA_EPISTEMOLOGICA_VALIDA`, `ASOCIACION_CLINICA_POTENCIAL_NO_CAUSAL_VALIDA`, `DUPLICADA`, `SALTO_CAUSAL`, `NO_SOSTENIDA` o `U_NO_ADJUDICABLE`.

Debe haber cuatro epistemológicas y una asociación clínica potencial no causal.

## 7. Ataque E — identidad de población y definición

Construya al menos estos casos:

- total normal con una subpoblación baja;
- subpoblación normal con total discordante;
- dos resultados rotulados igual pero con definiciones o marcadores no equivalentes;
- dos subpoblaciones de una misma muestra;
- población no identificada.

Ataque si `CON-LYM-ID-001` fusiona, sustituye o permite concluir una alteración sin definición.

## 8. Ataque F — magnitud, unidad y método

Intente:

1. intercambiar porcentaje y recuento absoluto;
2. calcular el ausente sin todos los inputs;
3. comparar unidades incompatibles;
4. ocultar si la medición es directa o calculada;
5. tratar plataformas distintas como equivalentes.

La salida debe conservar originales y producir `U` o rechazo. No puede adoptar fórmula, conversión o umbral.

## 9. Ataque G — tiempo, calidad y referencia

Construya resultados donde fecha de informe y muestra difieren, la calidad es inválida o desconocida, la referencia pertenece a otra población/unidad/método, o dos puntos temporalmente separados parecen una tendencia.

Compruebe que `CON-LYM-TIME-001` no declara estado actual, persistencia, tendencia, causa ni frecuencia de repetición sin reglas posteriores.

## 10. Ataque H — cantidad frente a función

Intente concluir:

- función conservada desde un recuento dentro de referencia;
- incapacidad funcional desde un recuento bajo;
- respuesta a un estímulo concreto desde una proporción;
- ausencia de déficit no medido desde una medición cuantitativa.

La única salida admisible de `CON-LYM-FUN-001` es conservar la cantidad y declarar `FUNCION_NO_CONSTITUIDA` o `U`. No debe ordenar una prueba funcional.

## 11. Ataque I — asociación frente a causalidad y transporte

Ataque `CON-LYM-INF-001` con:

- una persona bajo inmunosupresión farmacológica;
- una población de edad u origen distintos;
- una subpoblación en vez del recuento total usado en el estudio;
- comorbilidad, enfermedad o tratamiento que puedan confundir;
- una medición aislada o antigua;
- un desenlace individual posterior.

Compruebe que el lote no permite decir «el recuento causó la infección», predecir riesgo individual ni transportar automáticamente el efecto. La salida máxima es una asociación poblacional pertinente pendiente de regla o `U`.

## 12. Ataque J — punto de corte, efecto y algoritmo del estudio

Intente incorporar al dominio:

1. el punto de corte de Warny et al.;
2. sus razones de riesgo;
3. su algoritmo de riesgo absoluto;
4. sus intervalos como referencia universal;
5. una categoría clínica de gravedad.

Todos deben fracasar. Son características del estudio, no reglas constituidas para `OP-IMM-001`.

## 13. Ataque K — doble dirección del error

Compruebe que `CON-LYM-INF-001` trata dos errores distintos sin fusionarlos:

- omitir una señal cuantitativa genuina potencialmente pertinente;
- fabricar certeza causal o pronóstica a partir de una asociación.

Construya un caso sin daño clínico pese al dato ausente y otro con infección explicable por causas alternativas. Ninguno puede convertirse en daño consumado atribuible al recuento.

## 14. Ataque L — trazabilidad, reproducción y fallo

Verifique que toda salida puede expresar antes de concluir: consecuencia, observable o `U`, valor original y procedencia, error, fuente y localizador, población y diseño, finalidad, transición, límites causales y de transporte, incertidumbres, versión y autoridad.

Una conclusión plausible con cita añadida después debe resultar no admisible.

Modele dos ejecuciones con la misma entrada canónica, horizonte, fuentes, versiones, finalidad y autoridad. Cadena, `U`, localizadores, límites, orden y serialización deben coincidir byte a byte. Un fallo sólo puede producir `EJECUCION_TECNICA_NO_VALIDA`.

## 15. Ataque M — privacidad, finitud y no avance

Compruebe que los objetos son impersonales y que el lote:

- termina en cinco consecuencias;
- no abre vacunación, función linfocitaria, diagnósticos, etiologías, intervenciones, costes o reglas institucionales;
- no constituye intervalo, umbral, riesgo absoluto o pronóstico individual;
- no crea parámetros atómicos, matrices, rutas o frames;
- no abre `G5-ATM`;
- no modifica Lenguaje SV ni autoriza asistencia.

## 16. Recuentos obligatorios

Entregue recuento calculado de:

- cinco consecuencias;
- cuatro epistemológicas;
- una asociación clínica potencial no causal;
- tres fuentes externas;
- cero puntos de corte o efectos adoptados;
- cero diagnósticos o intervenciones;
- cero parámetros atómicos;
- cero matrices, rutas y frames.

## 17. Entrega

Emita una sola auditoría con:

1. identidad calculada y diff exacto;
2. dictamen `PASA`, `PASA_CON_REPAROS`, `NO_PASA` o `U_AUDITORIA_INCOMPLETA`;
3. tabla de ataques A–M;
4. contraejemplo material por ataque B–M;
5. clasificación individual de las cinco consecuencias;
6. reparos numerados con severidad, objeto, texto, evidencia, consecuencia y corrección mínima;
7. incertidumbres residuales y operación exacta de cierre;
8. recuentos verificados;
9. declaración separada de si `G4-S2_CERRABLE`;
10. declaración expresa de que el dictamen no autoriza abrir `G5-ATM`.

## 18. Límites

- No escribir en GitHub.
- No abrir PR.
- No tocar `main`.
- No modificar los objetos.
- No buscar cohortes adicionales ni abrir estado del arte.
- No añadir consecuencias, umbrales, riesgos o intervenciones.
- No diseñar parámetros, matrices, rutas o frames.
- No usar episodios reales como ejemplos.
- No confundir asociación, causalidad y predicción individual.
- No convertir una cita decorativa en trazabilidad.
