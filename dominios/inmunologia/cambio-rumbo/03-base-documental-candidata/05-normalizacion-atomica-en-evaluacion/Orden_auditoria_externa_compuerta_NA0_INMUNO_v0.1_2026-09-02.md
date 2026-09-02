# Orden de auditoría externa adversarial — compuerta NA0 INMUNO v0.1

## 1. Objeto invariable

- **Repositorio:** `juantoniolloretegea/SVperitus-dataset`
- **Rama:** `dominio-inmunologia`
- **Commit material que debe auditarse:** `46152c6d16090cba2210baf6ac33c29ec7841b08`
- **Compuerta:** `NA0`, normalización atómica nivel cero
- **Finalidad:** decidir si el vocabulario, las pruebas de atomicidad y el cribado de los pilotos son aptos para gobernar el primer despiece clínico

Objetos principales y SHA-256:

| Objeto | SHA-256 |
|---|---|
| `Contrato_semantico_atomo_parametro_matriz_composicion_INMUNO_v0.1_2026-09-02.md` | `38d4e41144e4f2edf63b50e892d93a1d0719ad3abbc4c3c3bfec46e9d77a3ceb` |
| `Protocolo_adversarial_transversal_INMUNO_v0.1_2026-09-02.md` | `b4d96fed4a6a7f026c0fd022a0b281a67e477b24edc58901ea38f678b7e0dfd4` |
| `Cribado_estructural_pilotos_IMMUNO-1_IMMUNO-2_v0.1_2026-09-02.md` | `1ade948a86d3e96f1df743c98d3d1c963535b591df9a62e262f14e03cd83fc8f` |
| `Adversarial_interna_compuerta_NA0_INMUNO_v0.1_2026-09-02.md` | `f6a0b70eb917fd2253fbbe876f6c74ba4c1b3eb01bd2429b012fae03103bfbb7` |

Antecedentes que deben leerse, pero no reauditarse íntegramente:

- acta rectora de rectificación de 31-08-2026;
- acta de secuencia constitutiva de 02-09-2026 v0.1;
- catálogo profesional INMUNO v0.8;
- expediente de adjudicación comparada v0.2;
- recepción del dictamen externo `PASA` de v0.8;
- YAML y motores normativos de `IMMUNO-1` y `IMMUNO-2`;
- especificación `IMMUNO2_P01-P25_spec.md`.

No auditar otro commit ni sustituir los archivos por copias recuperadas de otro corte.

## 2. Regla del encargo

No se pide resumir ni elogiar el paquete. Se pide intentar falsarlo.

Cada reparo debe contener:

- identificador;
- severidad;
- archivo y apartado;
- texto atacado;
- contraejemplo o evidencia;
- efecto sobre la compuerta;
- corrección mínima literal.

Una objeción meramente terminológica no invalida una regla si no demuestra ambigüedad operativa. Una afirmación clínica nueva no puede introducirse sin fuente primaria y localizador.

## 3. Ataque A — Identidad y regresión

1. Confirmar el commit y los cuatro hashes principales.
2. Confirmar que la recepción de v0.8 corresponde al mismo SHA-256 del catálogo ya auditado.
3. Comparar el commit objetivo con su primer padre y enumerar todos los archivos modificados o añadidos.
4. Verificar que no cambió ningún XLSX, CSV, YAML, motor Python, compositor, archivo de `agentes/inmunologia/` ni archivo del Lenguaje SV.
5. Detectar referencias a versiones, estados o recuentos incompatibles.

## 4. Ataque B — Definición de átomo y parámetro

Intentar construir contraejemplos contra estas decisiones:

1. el objeto canónico es el parámetro clínico y `ATÓMICO` es su estatuto;
2. observable, regla, parámetro, contexto, control y puente son objetos distintos;
3. varios observables pueden sostener un único parámetro atómico;
4. un único campo informático puede ocultar un compuesto;
5. “molécula” no es necesaria como clase registral;
6. la atomicidad es relativa a operación, población, horizonte y versión.

Comprobar si las diez condiciones de atomicidad permiten decidir sin circularidad. En particular, atacar el uso de “consecuencia” y “ruta” para decidir la identidad antes de que ambas estén plenamente constituidas.

Para cada ambigüedad, proponer una formulación que produzca una salida reproducible: `ATÓMICO`, `COMPUESTO`, `CONTEXTO`, `CONTROL`, `PUENTE`, `NO_PERTINENTE` o `U_REQUIERE_ADJUDICACION`.

## 5. Ataque C — Freno de división y cierre finito

Comprobar que la prueba de corte:

- no obliga a dividir indefinidamente una analítica, imagen o procedimiento;
- no confunde dato bruto con pregunta clínica;
- no acepta agregados por conveniencia dimensional;
- no impide utilizar varios observables como evidencia del mismo estado;
- no permite esconder subdecisiones detrás de una etiqueta amplia;
- y declara un margen de aproximación explícito y versionable.

Construir al menos tres contraejemplos: uno de laboratorio, uno de tratamiento/exposición y uno de proceso o seguimiento. Para cada uno, mostrar dónde se detendría el despiece y por qué.

## 6. Ataque D — Protocolo transversal y meta-adversarial

Revisar las puertas `G0-PRO` a `G12-REL`.

1. ¿Tiene cada una objeto, entrada, ataque, salida y parada suficientes?
2. ¿Existe solapamiento o hueco entre `G3-OBS`, `G4-CON` y `G5-ATM`?
3. ¿Puede un reparo menor compensar un veto clínico crítico?
4. ¿Puede el diseñador declararse `PASA` sin evidencia por registro?
5. ¿Se distingue ataque interno de auditoría externa?
6. ¿Queda gobernada una novedad posterior mediante versión o `REOPEN_REQUIRED`?
7. ¿Hay una ruta silenciosa que permita mutar el Lenguaje SV?

Ejecutar también los ocho ataques del apartado “Meta-adversarial del propio protocolo”.

## 7. Ataque E — Reproducción de los pilotos

Recalcular desde los archivos del commit:

- 25 parámetros YAML y 25 funciones `Pxx` para `IMMUNO-1`;
- 25 parámetros YAML y 25 funciones `Pxx` para `IMMUNO-2`;
- 19 funciones que leen una clave `_get` distinta;
- 31 funciones que leen más de una;
- 50 filas materiales del inventario.

Verificar por muestreo completo, no sólo por nombre, que la columna `Entradas` del inventario es coherente con ambos motores.

Comprobar específicamente:

- la declaración de composición deliberada en `IMMUNO-2/P02`;
- el agregado oculto en `IMMUNO-2/P24`;
- la naturaleza de puente de `IMMUNO-2/P25`;
- la duplicación de `IMMUNO-1/P11` en la síntesis recibida de `FTD-AE-IMM-SV/0.3`, si la fuente está disponible;
- y las ocho familias de colisión interpiloto.

No convertir `SIMPLE`, `MULTI` o `MULTI-ALERTA` en dictámenes clínicos.

## 8. Ataque F — Seguridad clínica y no compensación

Intentar demostrar que el contrato o el protocolo permiten:

- compensar un riesgo crítico con mayoría de estados favorables;
- cerrar favorablemente una `U` crítica;
- convertir coste, camas, rapidez o carga administrativa en vector decisor clínico;
- confundir tiempo clínico con tiempo administrativo;
- o presentar el consejo de IA como orden soberana.

Atacar expresamente el umbral histórico `T(25)=19` con casos singulares. El resultado correcto de esta auditoría no es validar ni sustituir el umbral, sino confirmar que permanece no ratificado hasta su propia compuerta.

## 9. Ataque G — Frontera con IA, actualización y Lenguaje SV

Verificar que:

1. la IA no puede cerrar `U`, aprender implícitamente ni alterar reglas durante el episodio;
2. una consulta externa entra en cuarentena y requiere los filtros y la autoridad ya definidos por SV;
3. cada matriz conserva su frame y un resumen no borra los frames constitutivos;
4. Gramática 0.2 e IR 0.3 son referencias de compatibilidad, no objetos modificados;
5. las cinco clases de representabilidad no presuponen una extensión del lenguaje;
6. el paquete no escribe ni ordena escribir en el repositorio del Lenguaje SV.

Si se consulta documentación del lenguaje, usar el corte canónico vigente y distinguir lo ya representable de una inferencia del auditor.

## 10. Ataque H — Aptitud para la primera operación testigo

Evaluar si, tras corregir los reparos que procedan, `NA0` proporciona disciplina suficiente para elegir una única operación clínica y ejecutar `G1-OP` a `G5-ATM` sin:

- constituir de golpe todo el catálogo;
- heredar los 50 `Pxx`;
- buscar cohortes prematuramente;
- diseñar matrices antes de los parámetros;
- ni modificar el Lenguaje SV.

No elegir ni desarrollar la operación testigo en esta auditoría. Sólo dictaminar la aptitud de la compuerta.

## 11. Salida obligatoria

Entregar una sola auditoría con:

1. identidad calculada;
2. dictamen `PASA`, `PASA_CON_REPAROS`, `NO_PASA` o `U_AUDITORIA_INCOMPLETA`;
3. tabla de ataques A–H;
4. comprobaciones que resisten;
5. reparos numerados con corrección mínima;
6. incertidumbres residuales y causa;
7. recuentos reproducidos;
8. aptitud o no aptitud para abrir la primera operación testigo;
9. declaración expresa de que no se han constituido parámetros, consecuencias, matrices, rutas ni autorización asistencial.

## 12. Límites

- No escribir en GitHub.
- No crear rama ni pull request.
- No modificar archivos.
- No reabrir la adopción profesional del lote A ni la auditoría v0.8 salvo inconsistencia material demostrada.
- No hacer estado del arte ni buscar cohortes.
- No proponer umbrales clínicos alternativos.
- No validar clínicamente `IMMUNO-1`, `IMMUNO-2` o la pre-ITI.
- No modificar ni diseñar extensiones del Lenguaje SV.
- No constituir consecuencias clínicas.
- No confundir fallo de acceso propio con defecto del objeto.
- Desarrollar los acrónimos en su primera aparición y aportar glosario si se reutilizan.
