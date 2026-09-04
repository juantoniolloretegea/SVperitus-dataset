# Acta de pausa, retorno acotado y relevo de Inmunología al Lenguaje SV

- **Versión:** 0.1
- **Fecha:** 04-09-2026
- **Identificador:** `ACTA-IMM-RETORNO-LSV-2026-09-04`
- **Repositorio:** `SVperitus-dataset`
- **Rama de trabajo:** `dominio-inmunologia`
- **Corte congelado anterior a esta acta:** `3bea6b714be3bd1330e6ca6bbbc228b0eb9c065d`
- **Universo director:** `OP-IMM-001 / Q0 v0`
- **Estado:** `PAUSA_CONTROLADA · ESPERA_CORTE_DEL_LENGUAJE`
- **Naturaleza:** acta de proceso y relevo; **no es adenda inmunológica** y no reabre el expediente clínico.

## 0. Objeto

Esta acta dice a la unidad de Inmunología cuándo debe reactivarse, qué trabajo debe realizar y qué condiciones debe satisfacer antes de devolver el testigo al Lenguaje de computación SV.

No modifica `G10-SV`, la Solicitud de valoración, la PR #60, la gramática, la IR, Rust, WebAssembly ni el contenido clínico. Tampoco crea una tercera familia de requisitos. Conserva el corte y previene que una unidad futura confunda el cierre de un universo con el cierre de toda la Inmunología.

## 1. Estado exacto recibido

```text
CORTE_INMUNOLOGIA                  = 3bea6b714be3bd1330e6ca6bbbc228b0eb9c065d
OP_IMM_001_Q0_v0                  = CERRADO_PARA_TRANSFERENCIA
DOMINIO_INMUNOLOGIA_INTERNACIONAL = NO_CERRADO
SOFTWARE_CLINICO                   = NO_CONSTITUIDO
CONTRASTE_EMPIRICO                 = NO_OBSERVABLE
CONJUNTOS_ADMISIBLES               = 0
FRENTE_ACTIVO                      = LENGUAJE_DE_COMPUTACION
```

El recorrido `G0..G10` de `OP-IMM-001` produjo un mapa finito, `|A0|=27`, seis matrices de cardinalidad `(6, 1, 3, 2, 6, 9)`, cuatro salidas exclusivas, tratamiento explícito de `U`, un contrato técnico declarativo y requisitos para el Lenguaje.

Existen dos familias documentales que describen necesidades del mismo universo:

- `REQ-IMM-SV-001..015`, en `G10-SV`;
- `REQ-IMM-LSV-001..044`, en la Solicitud de valoración y en la PR #60.

La coexistencia no se resolverá mediante una adenda nueva desde Inmunología. La unidad de Lenguaje debe producir la tabla de correspondencia y cobertura dentro de su propia reparación documental.

Permanece abierto y visible:

```text
REQ-IMM-SV-011 = U_NO_DECIDIDO
```

Sólo la matriz de nueve miembros encaja directamente en `SV(9,3)`. Continúa prohibido rellenar, duplicar, fragmentar identidades o mezclar matrices para satisfacer una geometría.

## 2. Condición de reactivación

Inmunología no se reactiva por calendario, curiosidad lateral ni avance de Ciberseguridad. Se reactiva mediante relevo humano expreso desde Lenguaje y debe recibir un paquete identificable que contenga:

1. el corte exacto de la rama o candidato del Lenguaje;
2. la PR #60 reparada o un cierre documental equivalente;
3. `N0` como clasificación de objetos existentes y orden de oráculos;
4. los invariantes intrínsecos cerrados o sus decisiones explícitas;
5. la tabla de correspondencia entre las 15 necesidades `REQ-IMM-SV` y las 44 `REQ-IMM-LSV`;
6. el contrato candidato de perfil de dominio o, si aún no existe como tipo normativo, su interfaz documental de prueba;
7. las preguntas concretas que sólo el dominio puede decidir.

Sin ese paquete, el estado correcto es `PAUSA_CONTROLADA`.

## 3. Trabajo obligatorio durante el retorno inmunológico

Una vez reactivada, la unidad ejecutará en serie:

### I1. Verificación de identidad

Comprobará rama, commit, documentos, hashes y estado de conformidad del corte recibido. No aceptará referencias como `latest`, «vigente» o nombres sin commit.

### I2. Validación semántica de la reconciliación

Revisará la tabla `15 ↔ 44` preparada por Lenguaje y decidirá para cada relación si existe equivalencia, refinamiento, cobertura parcial, requisito nuevo, duplicación o hueco. No renumerará silenciosamente ni emitirá una tercera taxonomía.

### I3. Instanciación del contrato candidato

Producirá un candidato de `PerfilDominio` **completo respecto de `OP-IMM-001 / Q0 v0` y de su versión**, no respecto de toda la Inmunología. Mientras el Lenguaje no constituya ese objeto, el nombre `PerfilDominio` tendrá valor clasificatorio y de prueba, no será presentado como una construcción ya disponible.

El candidato deberá declarar al menos:

- identidad, versión y perímetro;
- objetos y relaciones necesarias;
- operaciones cubiertas y excluidas;
- estados, `U`, no aplicabilidad y fallo técnico;
- codominio y semántica de las cuatro salidas;
- procedencia, vigencia, configuración y autoridad;
- vetos, criticidades y supervisión humana;
- pérdidas, deudas y condiciones de evolución.

### I4. Contraste de representabilidad

Ejecutará o especificará oráculos positivos y negativos contra el corte del Lenguaje. Para cada necesidad deberá declarar:

- representación exacta;
- representación por composición;
- obligación del perfil;
- candidata a extensión;
- conflicto;
- o `U_NO_DECIDIDO`.

Toda clasificación llevará localizador y testigo. Una compilación verde sin denotación, cobertura o integridad referencial no contará como prueba suficiente.

### I5. Resolución disciplinada de `REQ-IMM-SV-011`

La unidad decidirá sólo si el corte recibido aporta evidencia nueva. Si no la aporta, conservará `U_NO_DECIDIDO`. No adaptará los seis grupos clínicos a la geometría del Lenguaje.

### I6. Separación normativa de resultados

Se comprobará literalmente:

> Toda ejecución válida con identidad completa idéntica debe producir exactamente los mismos bytes de salida canónica. Un fallo técnico no es una salida alternativa: determina que no existe ejecución clínica válida y sólo genera el registro técnico estructurado correspondiente.

`U` clínica pertenece a una ejecución válida cuando así lo declare el perfil; un fallo técnico no pertenece al codominio clínico.

### I7. Conservación de autoridad y límites

El dominio decide la suficiencia y verdad clínica de la representación. El Lenguaje decide su núcleo y realización. Ninguna parte recorta a la otra: toda pérdida o imposibilidad se registra.

Esta fase no constituye agente. Un agente futuro podrá cubrir todo el perfil inmunológico, un subdominio o un conjunto de operaciones expresamente declarado. Dominio y agente no son objetos equivalentes.

### I8. Adversarial y paquete único de retorno

Antes del relevo, la unidad someterá el resultado a una adversarial centrada en pérdida, ambigüedad, identidad, referencias inexistentes, composición, colisiones, `U`, fallo técnico y autoridad. Después entregará a Lenguaje un paquete único controlado, con anexos sólo cuando sean necesarios para prueba.

## 4. Criterios de salida hacia Lenguaje

Inmunología no devuelve el testigo hasta que todos estos criterios estén satisfechos:

- identidad forense completa del corte de entrada y del corte de salida;
- cobertura explícita de las 15 necesidades y las 44 formulaciones, sin huecos autorreferenciales;
- perfil candidato completo respecto de `OP-IMM-001 / Q0 v0` y su versión;
- matriz de cobertura entre objetos del dominio y construcciones del Lenguaje;
- testigos positivos, negativos y de pérdida;
- estado explícito de `REQ-IMM-SV-011`;
- codominio sin duplicados y semántica de salida total y no ambigua;
- separación entre `U`, no aplicabilidad y fallo técnico;
- procedencia, versión y vigencia preservadas;
- ausencia de corrección silenciosa, relleno o coerción geométrica;
- adversarial cerrada con precisiones incorporadas;
- inventario único de deuda residual y responsable;
- ninguna modificación del Lenguaje desde esta rama.

El relevo deberá declarar qué afirmaciones quedan demostradas, cuáles permanecen en `U` y cuáles son responsabilidad del Lenguaje, del perfil, de infraestructura o de una fase futura.

## 5. Trabajo expresamente no exigido antes del retorno

No es condición para devolver el testigo:

- cerrar toda la Inmunología internacional;
- recorrer los demás universos del mapa profesional;
- obtener cohortes o datos clínicos reales;
- superar `G9-EMP = NO_OBSERVABLE` sin evidencia nueva;
- desplegar software, interfaz o infraestructura clínica;
- constituir un agente o superagente;
- iniciar Ciberseguridad;
- abrir R2;
- redactar una adenda inmunológica para subsanar la PR #60;
- ni convertir necesidades de dominio en primitivas del núcleo.

## 6. Orden global de frentes

```text
AHORA    = LENGUAJE_REPARA_PR_60
DESPUES  = LENGUAJE_CIERRA_N0_E_INVARIANTES_INTRINSECOS
RETORNO1 = INMUNOLOGIA_CONTRASTA_OP_IMM_001
RETORNO2 = LENGUAJE_INCORPORA_Y_FIJA_CORTE
DESPUES  = CIBERSEGURIDAD_ABRE_TRABAJO_SUSTANTIVO
RETORNO3 = LENGUAJE_RECIBE_SEGUNDO_FALSADOR
FINAL    = CONSOLIDACION_ACOTADA_DEL_NUCLEO_Y_PERFILES
```

Se mantiene un único frente sustantivo activo. Las ramas preservan trabajo y trazabilidad; no autorizan concurrencia por sí mismas.

## 7. Dictamen

```text
INMUNOLOGIA                       = PAUSA_CONTROLADA
ADENDA_NUEVA_PARA_PR_60           = NO
REPARACION_PR_60                  = RESPONSABILIDAD_DE_LENGUAJE
TRABAJO_PREVIO_AL_RETORNO         = NINGUNO_EN_INMUNOLOGIA
TRABAJO_DURANTE_RETORNO           = CONTRASTE_ACOTADO_Y_VALIDACION
CIERRE_TOTAL_DE_INMUNOLOGIA       = NO_REQUERIDO
AGENTE                            = NO_CONSTITUIDO
MODIFICACION_DEL_LENGUAJE_AQUI    = PROHIBIDA
```

Esta acta queda como puerta de continuidad. Sólo un suceso posterior, explícito, motivado y autorizado puede alterar su secuencia.
