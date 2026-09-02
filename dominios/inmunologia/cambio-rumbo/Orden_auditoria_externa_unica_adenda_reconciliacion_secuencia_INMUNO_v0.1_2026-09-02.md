# Orden única de auditoría externa — adenda de reconciliación de secuencia INMUNO v0.1

## 1. Objeto exacto

Audite exclusivamente:

| Objeto | Bytes | SHA-256 |
|---|---:|---|
| `adenda-reconciliacion-secuencia-constitutiva-y-puertas-inmunologia-2026-09-02-v0.1.md` | 13 583 | `bee483117b1572d849cfa66cd09b0fc52051e2b866997fa3a357d4b4a8ad28cf` |
| `adversarial-interna-ingenieria-procesos-adenda-reconciliacion-secuencia-inmunologia-2026-09-02-v0.1.md` | 12 691 | `a42e5b4ccc0c2ad6efbaf0eea0f1ac3e2826fb0f2d802a589ca92668450a1409` |

Directorio:

`dominios/inmunologia/cambio-rumbo/`

La línea base inmediata es `bccac19d456d3d1d46bfacfe939955bb5795a567`. Identifique el commit candidato y calcule identidad y diff. Esta orden queda fuera del objeto auditado.

## 2. Documentos de contraste obligatorios

Lea completos y confronte:

1. `acta-rectificacion-metodologica-dominio-inmunologia-2026-08-31-v0.1.md`;
2. `acta-secuencia-constitutiva-custodia-rumbo-y-acoplamiento-lenguaje-sv-inmunologia-2026-09-02-v0.1.md`;
3. `acta-estratificacion-clinica-autoridad-y-ejecucion-computacional-inmunologia-2026-09-02-v0.1.md`;
4. `Contrato_matematico_parametro_atomico_matriz_ruta_INMUNO_v0.3_2026-09-02.md`;
5. `README.md` rector;
6. estados materiales de `G2-S1`, `G2-S2`, `G3-S1`, `G4-S1`, `G3-S2` y `G4-S2`.

No utilice la adversarial interna como prueba. Debe reconstruir las precedencias desde los textos.

## 3. Regla de suficiencia

Para cada ataque B–T ejecute al menos un contraejemplo material. Una mera paráfrasis produce `U_AUDITORIA_INCOMPLETA`.

Un solo fallo `FATAL_CLINICO`, `FATAL_SEMANTICO` o `FATAL_CONFIGURACION` impide `PASA`, aunque todos los demás controles sean favorables.

## 4. Ataque A — identidad y regresión

Compruebe:

- bytes y SHA-256 de los dos objetos;
- diff completo contra `bccac19d456d3d1d46bfacfe939955bb5795a567`;
- que sólo se añaden adenda, adversarial, esta orden y referencia mínima del README;
- que no se modifica ningún acta anterior, catálogo, contrato, lote, hoja de cálculo, política, piloto, ITI o Lenguaje SV;
- que `G4-S2` permanece materialmente idéntico y congelado.

## 5. Ataque B — existencia de la colisión

Construya una tabla literal de precedencias de los cuatro documentos obligatorios. Determine si realmente coexisten:

- `átomos -> matrices -> consecuencias`;
- consecuencias *ex ante* y representación posterior;
- `observables -> consecuencias provisionales -> atomicidad -> matrices -> rutas`;
- etiquetas desnudas `G3`–`G6` con significados incompatibles.

Ataque si la adenda exagera, oculta o resuelve una colisión inexistente.

## 6. Ataque C — no reescritura y autoridad

Compruebe que la adenda:

- no altera los antecedentes;
- no declara rector al contrato técnico por mera posterioridad;
- no adquiere estatuto rector antes de auditoría y recepción;
- conserva el motivo y la evidencia de la rectificación.

Simule una corrección mediante edición del acta anterior. Debe ser rechazada.

## 7. Ataque D — nomenclatura inequívoca

Intente ejecutar una transición usando únicamente `G3`, `G4`, `G5` o `G6`. Debe resultar no admisible.

Verifique que `G0-PRO`–`G10-SV` son identificadores únicos, que ninguna puerta comparte significado y que la nomenclatura histórica no gobierna una transición prospectiva.

## 8. Ataque E — dos estadios de consecuencia

Intente:

1. usar una consecuencia candidata como veto clínico;
2. adjudicar atomicidad sin consecuencia candidata;
3. declarar consecuencia operacional sin parámetro, matriz o uso `u(p,O)`;
4. redactar una consecuencia después para justificar un átomo ya elegido.

Los cuatro intentos deben fracasar. Determine si la separación es semánticamente suficiente o sólo un cambio de rótulo.

## 9. Ataque F — orden de dependencias

Para cada salto siguiente construya un objeto ficticio mínimo e intente hacerlo pasar:

- `G2-SEM -> G5-ATM` sin observables ni consecuencias;
- `G3-OBS -> G6-MAT` sin parámetro;
- `G4-CON -> G7-RUT` sin atomicidad ni matriz;
- `G5-ATM -> G7-RUT` sin propietario matricial;
- `G6-MAT -> G10-SV` sin rutas ni laboratorio;
- `G9-EMP` sin pregunta nacida de objetos constituidos.

Cada salto debe producir bloqueo con causa, no avance parcial.

## 10. Ataque G — cascada global frente a corte vertical

Pruebe los dos extremos:

- exigir exhaustividad mundial antes del primer observable;
- cerrar un sublote atractivo y presentarlo como dominio completo.

Verifique que los cortes `S_k` son finitos, relativos a operación y versión, y que selección, exclusiones y residuos permanecen visibles.

## 11. Ataque H — selección oportunista

Construya una secuencia que elija primero objetos por:

- fuente accesible;
- experiencia previa;
- facilidad de programación;
- resultado clínico llamativo;
- posibilidad de obtener `PASA`.

Compruebe que ninguna razón puede fijar prioridad clínica, tabla atómica, dimensión o ruta. Exija evidencia material de cómo se registrará el motivo de selección y el residuo.

## 12. Ataque I — freno contra deriva infinita

Añada sucesivamente una fuente, subpoblación, excepción y nuevo observable. Intente impedir indefinidamente `G5-ATM`.

Verifique que:

- el corte y su presupuesto no cambian silenciosamente;
- la novedad abre versión nueva;
- un candidato puede entrar en adjudicación al cerrar sus dependencias;
- el residuo se enumera sin fingir exhaustividad.

## 13. Ataque J — exclusión mutua y carrera

Modele dos unidades que parten del mismo commit y editan dependencias solapadas. Una cierra mientras la otra mantiene la base antigua.

Compruebe `WIP(O) <= 1`, identidad del commit base, detección de dependencia sustituida y salida `BLOQUEADO_CON_CAUSA`. Ninguna actualización forzada o mezcla silenciosa es admisible.

## 14. Ataque K — matrices y propiedad

Intente:

- introducir preguntas u observables en una matriz;
- rellenar hasta `SV(9,3)` o `SV(25,5)`;
- asignar dos propietarios a un parámetro;
- copiar un parámetro en lugar de referenciarlo;
- cerrar una matriz con candidatos no adjudicados ocultos.

Todos deben fracasar sin alterar los operandos.

## 15. Ataque L — composición y ruta prematuras

Construya una ruta visualmente plausible antes de cerrar parámetros, matrices y consecuencias operacionales. Intente convertir orden gráfico en causalidad o criticidad.

Debe ser rechazada. Un frame o diagrama no constituye sus operandos.

## 16. Ataque M — evidencia puntual frente a contraste sistemático

Intente:

- declarar `G9-EMP` cerrado por una cohorte usada en `G4-CON`;
- negar una consecuencia porque aún no existe cohorte adecuada;
- usar una asociación como causalidad;
- abrir una búsqueda por interés del repositorio y no por pregunta constituida.

Verifique la separación de ambos regímenes y sus salidas.

## 17. Ataque N — auditoría y carga administrativa

Modele:

1. auditoría de auditoría sin cambio material;
2. una recepción que genera otra auditoría sólo por existir;
3. reducción documental que elimina un control de privacidad o causalidad;
4. diez documentos que no cambian estado ni evidencia.

La adenda debe impedir tanto el bucle burocrático como la supresión de controles críticos. Determine si “proporcional al riesgo” posee criterios suficientes: identidad, autoridad, privacidad, causalidad, propiedad, criticidad y determinismo.

## 18. Ataque O — rollback y preservación

Simule un defecto descubierto después de cerrar una matriz que obliga a regresar a observables. Compruebe que:

- no se borra el cierre anterior;
- se crea un suceso correctivo;
- se enumeran objetos y versiones afectados;
- se invalidan sólo dependientes alcanzables;
- no se usa un `reset` como sustituto de trazabilidad.

## 19. Ataque P — autoridad clínica, constitutiva y técnica

Pruebe:

- que ingeniería fusione átomos por conveniencia;
- que una limitación técnica se presente como contraindicación;
- que la inteligencia artificial cierre `U`;
- que una decisión clínica modifique retrospectivamente la admisibilidad técnica;
- que una facilidad del lenguaje cree una necesidad clínica.

Cada autoridad debe quedar confinada a su plano.

## 20. Ataque Q — privacidad indirecta

Introduzca un ejemplo sin nombre pero con combinación singular de centro, fechas, enfermedad, tratamiento y evolución. Compruebe si puede reidentificarse.

La ausencia de nombre no basta. El sistema debe exigir impersonalidad, finalidad, mínimo privilegio y ejemplo sintético gobernado cuando no exista autorización.

## 21. Ataque R — determinismo y fallo técnico

Ejecute dos veces la misma transición con orden de entrada distinto pero contenido canónico idéntico. Deben coincidir estado, dependencias, bloqueos, residuos, trazas y bytes.

Después fuerce un fallo de conector o herramienta. La única salida es `EJECUCION_TECNICA_NO_VALIDA`; no `0`, no `U` clínica, no consejo conservador.

## 22. Ataque S — acoplamiento con Lenguaje SV

Intente que el dominio:

- modifique gramática o representación intermedia;
- abra una ronda técnica;
- trate una carencia de implementación como carencia clínica;
- introduzca una primitiva por conveniencia inmunológica.

Debe producir únicamente una tensión registrada o requisito futuro en `G10-SV`.

## 23. Ataque T — estado de los objetos actuales

Verifique uno por uno:

- catálogo profesional v0.8 cerrado;
- `NA0-MATH` y `Q0` preservados;
- `OP-IMM-001` preservada;
- `G2-S1`, `G2-S2`, `G3-S1`, `G4-S1` y `G3-S2` cerrados sin reescritura;
- `G4-S2` idéntico a `bccac19d...` y congelado;
- cero parámetros, matrices, rutas y frames.

Ningún estatuto puede inferirse sólo por ubicación o nombre de archivo.

## 24. Clasificación de fallos

Clasifique cada hallazgo:

- `FATAL_CLINICO`;
- `FATAL_SEMANTICO`;
- `FATAL_CONFIGURACION`;
- `MAYOR`;
- `MENOR`;
- `OBSERVACION`.

Explique por qué no es compensable o qué reparación mínima lo cierra.

## 25. Entrega obligatoria

Emita una única auditoría con:

1. identidad calculada y diff;
2. tabla de precedencias reconstruida;
3. dictamen `PASA`, `PASA_CON_REPAROS`, `NO_PASA` o `U_AUDITORIA_INCOMPLETA`;
4. tabla A–T;
5. contraejemplo material B–T;
6. fallos clasificados y corrección mínima;
7. incertidumbres residuales y operación de cierre;
8. recuento de puertas, estados actuales y objetos modificados;
9. declaración `ADENDA_RECONCILIACION_CERRABLE`;
10. declaración expresa sobre si puede descongelarse la auditoría de `G4-S2`.

## 26. Límites

- No escribir en GitHub.
- No abrir PR.
- No tocar `main`.
- No modificar objetos.
- No cerrar `G4-S2`.
- No crear parámetros, matrices, rutas o frames.
- No abrir cohortes, estado del arte o Lenguaje SV.
- No usar episodios reales.
- No sustituir pruebas por prosa favorable.
- No compensar un fallo fatal con recuentos positivos.

