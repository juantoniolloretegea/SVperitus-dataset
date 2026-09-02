# Orden única de auditoría externa — `G3-S2` compartimento linfocitario v0.1

## 1. Objeto exacto

Audite el contenido material de:

| Objeto | Bytes | SHA-256 |
|---|---:|---|
| `Lote_observacional_G3-S2_compartimento_linfocitario_OP-IMM-001_v0.1_2026-09-02.md` | 11 661 | `8fef4458d77c72ff64523684d3525a3cdfce7595081ab2e9d7d9f5ac6bbaa0ab` |
| `Adversarial_interna_G3-S2_compartimento_linfocitario_OP-IMM-001_v0.1_2026-09-02.md` | 4 770 | `fd9d5319a65fd5b98f6ca5e2fa3c803c7f28374575051bc35585723953a25050` |
| `Recepcion_y_cierre_auditoria_externa_G4-S1_corticoides_OP-IMM-001_v0.1_2026-09-02.md` | 2 720 | `e048462b8d44cef91760187dae59634a4bb11b8d8b499d8a14c301190a91fbd8` |

Los dos primeros están en `08-observables-en-evaluacion`; la recepción está en `09-consecuencias-en-evaluacion`. Calcule bytes y SHA-256 desde el commit candidato. La línea base inmediata es `5bb70c1d7293913150f66aa79da77a3275cefbd8`. Identifique el commit candidato. Esta orden queda fuera del objeto auditado.

## 2. Regla de suficiencia

Para cada ataque B–K construya al menos un contraejemplo material. La adversarial interna orienta, pero no prueba. Abra las fuentes; si una no es accesible, declare `U_ACCESO` y limite la conclusión.

## 3. Ataque A — identidad y regresión

Compruebe que el diff sólo añade la recepción G4, lote G3-S2, adversarial, orden y referencia mínima del README. Verifique que no cambian `G3-S1`, `G4-S1`, catálogo v0.8, `Q0`, G2, `NA0-MATH`, pilotos, política, ITI ni Lenguaje SV. Deben seguir en cero parámetros, matrices, rutas y frames.

## 4. Ataque B — cierre G4 y freno de sesgo

Verifique que la recepción refleja exactamente candidato `5bb70c1d7293913150f66aa79da77a3275cefbd8`, tres huellas, dictamen `PASA`, cinco consecuencias, cero reparos y residuales declarados.

Ataque la decisión de no abrir `G5-ATM`: compruebe que impide que el primer subcaso vacunal/PJP determine la tabla de átomos o la dimensión matricial.

## 5. Ataque C — fuentes y fuerza exacta

Contraste:

1. CDC, *Altered Immunocompetence*, `General Principles`;
2. CLSI `H42-A2`, `Abstract` y `Scope` públicos;
3. EuroFlow, página de protocolos y referencias versionadas.

Determine si sostienen exactamente:

- número de linfocitos, recuento absoluto por volumen/proporción de subpoblaciones y función como objetos distintos;
- dependencia de la comparabilidad respecto del proceso y control analíticos, y si muestra, método, calidad y procedencia son suficientes en este nivel semántico sin reproducir el expediente técnico interno del laboratorio;
- existencia separada de referencias en porcentajes y números absolutos;
- ausencia de autorización para importar valores de referencia, umbrales o decisiones clínicas.

No utilice contenido vacunal fuera del pasaje general de laboratorio.

## 6. Ataque D — entidad y diez observables

Verifique `OBS-LYM-001`–`010`, sin huecos ni duplicados. Para cada uno aplique variación independiente, ablación y `U` propia. Clasifique como:

- `OBSERVABLE_NECESARIO`;
- `METADATO_OBLIGATORIO`;
- `DUPLICADO`;
- `COMPUESTO_A_REVISAR`;
- `U_NO_ADJUDICABLE`.

Compruebe que procedencia por campo es metadato obligatorio y no undécimo observable.

## 7. Ataque E — total, población y definición

Construya al menos:

- total normal con una subpoblación alterada;
- misma etiqueta de población con definiciones distintas;
- poblaciones distintas medidas en la misma muestra;
- definición ausente con número presente.

El lote no puede cerrar una población desde otra ni fusionar etiquetas sin equivalencia demostrada.

## 8. Ataque F — recuento absoluto por volumen y proporción

Construya:

- mismo porcentaje con absolutos distintos;
- mismo absoluto con porcentajes distintos;
- unidad ausente;
- absoluto calculado con un input ausente;
- resultado directo frente a doble plataforma.

Compruebe que `N_LYM_MEAS` y `N_LYM_PAIR` no convierten ni rellenan sin regla e inputs trazables.

## 9. Ataque G — cantidad no es función

Intente deducir función linfocitaria, competencia inmunitaria, respuesta específica, diagnóstico o riesgo desde un recuento normal o alterado. Debe fracasar.

Compruebe que `SEM-HUE-001` y `G3-S2` permanecen cuantitativos y que los ensayos funcionales quedan fuera, no negados.

## 10. Ataque H — tiempo, serie y referencia

Construya:

- fecha de informe distinta de la muestra;
- resultados repetidos con orden de llegada permutado;
- dos puntos sin regla de tendencia;
- referencia de otra población, edad, magnitud, unidad o versión;
- resultado antiguo presentado como vigente.

Compruebe que `N_LYM_SERIES` sólo ordena y `N_LYM_REF` sólo vincula; ninguno interpreta.

## 11. Ataque I — calidad, conflicto y procedencia

Ataque con resultado invalidado, calidad desconocida, dos fuentes discordantes, fuente sin localizador y valor plausible generado en texto libre.

Verifique las doce causas de `U`, la conservación de valores en conflicto y la vinculación de procedencia antes de normalizar.

## 12. Ataque J — determinismo

Modele dos ejecuciones idénticas, orden de llegada distinto, empate temporal con procedencia distinta, cambio mínimo de unidad o definición y fallo técnico.

La misma entrada canónica debe producir salida, `U`, traza, orden y bytes idénticos. Un cambio material debe ser visible. Un fallo produce sólo `EJECUCION_TECNICA_NO_VALIDA`.

## 13. Ataque K — privacidad y no avance

Compruebe que los objetos son impersonales y no contienen episodios, personas o centros identificables.

Verifique cero:

- intervalos o umbrales adoptados;
- diagnósticos, riesgos o consecuencias;
- función linfocitaria inferida;
- pruebas obligatorias;
- parámetros atómicos;
- matrices, rutas o frames;
- cambios de interoperabilidad o Lenguaje SV.

`G3-S2` no abre `G4-S2` ni `G5-ATM`.

## 14. Recuentos obligatorios

- una pregunta G2;
- tres fuentes;
- una entidad;
- diez observables;
- cuatro normalizadores;
- doce causas de `U`;
- cero umbrales o diagnósticos;
- cero parámetros;
- cero matrices, rutas o frames.

## 15. Entrega

Emita una sola auditoría con:

1. identidad calculada y diff;
2. dictamen `PASA`, `PASA_CON_REPAROS`, `NO_PASA` o `U_AUDITORIA_INCOMPLETA`;
3. tabla A–K;
4. contraejemplo material B–K;
5. clasificación individual de `OBS-LYM-001`–`010`;
6. reparos numerados y corrección mínima;
7. incertidumbres residuales y operación de cierre;
8. recuentos;
9. declaración `G3-S2_CERRABLE`;
10. declaración expresa de que no autoriza `G4-S2` ni `G5-ATM`.

## 16. Límites

- No escribir en GitHub ni abrir PR.
- No tocar `main` ni modificar los objetos.
- No abrir vacunación, cohortes o estado del arte.
- No proponer pruebas, intervalos, umbrales, diagnósticos o tratamientos.
- No diseñar parámetros, matrices, rutas o frames.
- No usar datos reales o atribuibles.
- No sustituir contraejemplo por resumen.
