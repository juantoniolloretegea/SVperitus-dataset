# Acta de pausa, retorno acotado y relevo de Inmunología al Lenguaje SV

> **Estado vigente tras la devolución G/H · 07/09/2026:** I1–I8 completados en alcance documental. [Paquete único de retorno](marco-tecnico-de-universos-subdominios-y-modulos/01-op-imm-001-informacion-preinmunosupresion-adultos/retorno-gh-2026-09-07/RETORNO_GH_OP-IMM-001_Q0_v0_AL_LENGUAJE_SV_2026-09-07.md) y [relevo §9](#devolucion-gh-20260907). Dictamen: suficiencia no acreditada para ejecutar Q0, con fidelidad y pérdidas documentales acotadas. **Inmunología en pausa controlada; siguiente receptor: Lenguaje, fila 7.** La nota de apertura 0.2 que sigue se conserva como antecedente.


> **Antecedente de apertura · 07/09/2026 · actualización 0.2:** retorno acotado G/H autorizado. Lea primero [§8: paquete recibido, trabajo y devolución del control](#recepcion-gh-20260907). Los estados de espera y reparación de §§1, 6 y 7 describen el corte del 04/09; I1–I8 siguen vigentes con las precisiones de §8. El siguiente receptor es Lenguaje, fila 7.


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

Esta acta establece las condiciones de reactivación de la unidad de Inmunología, el trabajo que debe realizar y los requisitos que debe satisfacer antes de devolver el control al Lenguaje de computación SV.

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

Inmunología no se reactiva por el transcurso del tiempo, por iniciativas ajenas al alcance autorizado ni por el avance de Ciberseguridad. Se reactiva mediante relevo humano expreso desde Lenguaje y debe recibir un paquete identificable que contenga:

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

Comprobará la rama, el identificador de revisión, los documentos, sus huellas criptográficas y el estado de conformidad de la versión recibida. No aceptará referencias como `latest`, «vigente» o nombres sin commit.

### I2. Validación semántica de la reconciliación

Revisará la tabla `15 ↔ 44` preparada por Lenguaje y decidirá para cada relación si existe equivalencia, refinamiento, cobertura parcial, requisito nuevo, duplicación o falta de cobertura. No renumerará silenciosamente ni emitirá una tercera taxonomía.

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

Toda clasificación llevará localizador y testigo. Una compilación satisfactoria sin denotación, cobertura o integridad referencial no contará como prueba suficiente.

### I5. Resolución disciplinada de `REQ-IMM-SV-011`

La unidad decidirá sólo si el corte recibido aporta evidencia nueva. Si no la aporta, conservará `U_NO_DECIDIDO`. No adaptará los seis grupos clínicos a la geometría del Lenguaje.

### I6. Separación normativa de resultados

Se comprobará literalmente:

> Toda ejecución válida con identidad completa idéntica debe producir exactamente los mismos bytes de salida canónica. Un fallo técnico no es una salida alternativa: determina que no existe ejecución clínica válida y sólo genera el registro técnico estructurado correspondiente.

`U` clínica pertenece a una ejecución válida cuando así lo declare el perfil; un fallo técnico no pertenece al codominio clínico.

### I7. Conservación de autoridad y límites

El dominio decide la suficiencia y verdad clínica de la representación. El Lenguaje decide su núcleo y realización. Cada unidad respeta las competencias de la otra: toda pérdida o imposibilidad se registra.

Esta fase no constituye agente. Un agente futuro podrá cubrir todo el perfil inmunológico, un subdominio o un conjunto de operaciones expresamente declarado. Dominio y agente no son objetos equivalentes.

### I8. Evaluación adversarial y expediente único de retorno

Antes del relevo, la unidad someterá el resultado a una evaluación adversarial centrada en pérdida, ambigüedad, identidad, referencias inexistentes, composición, colisiones, `U`, fallo técnico y autoridad. Después entregará a Lenguaje un paquete único controlado, con anexos sólo cuando sean necesarios para prueba.

## 4. Criterios de salida hacia Lenguaje

Inmunología no devuelve el control hasta que todos estos criterios estén satisfechos:

- identidad forense completa del corte de entrada y del corte de salida;
- cobertura explícita de las 15 necesidades y las 44 formulaciones, sin omisiones encubiertas por referencias al propio documento;
- perfil candidato completo respecto de `OP-IMM-001 / Q0 v0` y su versión;
- matriz de cobertura entre objetos del dominio y construcciones del Lenguaje;
- testigos positivos, negativos y de pérdida;
- estado explícito de `REQ-IMM-SV-011`;
- codominio sin duplicados y semántica de salida total y no ambigua;
- separación entre `U`, no aplicabilidad y fallo técnico;
- procedencia, versión y vigencia preservadas;
- ausencia de corrección silenciosa, relleno o coerción geométrica;
- evaluación adversarial concluida con las precisiones incorporadas;
- inventario único de deuda residual y responsable;
- ninguna modificación del Lenguaje desde esta rama.

El relevo deberá declarar qué afirmaciones quedan demostradas, cuáles permanecen en `U` y cuáles son responsabilidad del Lenguaje, del perfil, de infraestructura o de una fase futura.

## 5. Trabajo expresamente no exigido antes del retorno

No es condición para devolver el control:

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

## 6. Secuencia general de trabajo

```text
AHORA    = LENGUAJE_REPARA_PR_60
DESPUES  = LENGUAJE_CIERRA_N0_E_INVARIANTES_INTRINSECOS
RETORNO1 = INMUNOLOGIA_CONTRASTA_OP_IMM_001
RETORNO2 = LENGUAJE_INCORPORA_Y_FIJA_CORTE
DESPUES  = CIBERSEGURIDAD_ABRE_TRABAJO_SUSTANTIVO
RETORNO3 = LENGUAJE_RECIBE_SEGUNDO_FALSADOR
FINAL    = CONSOLIDACION_ACOTADA_DEL_NUCLEO_Y_PERFILES
```

Se mantiene una única área de trabajo sustantivo activa. Las ramas preservan trabajo y trazabilidad; no autorizan concurrencia por sí mismas.

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

Esta acta establece las condiciones de continuidad. Sólo un suceso posterior, explícito, motivado y autorizado puede alterar su secuencia.

<a id="recepcion-gh-20260907"></a>

## 8. Recepción autorizada del Lenguaje y retorno G/H · 07/09/2026

**Actualización 0.2 del acta existente. Autoridad:** Juan Antonio Lloret Egea, Director, autoriza actualizar el relevo y fijar la devolución a la unidad de programación. **Efecto:** queda autorizado el retorno acotado de Inmunología, fila 6/G-H, para OP-IMM-001 / Q0 v0. La autorización abre el contraste; no anticipa su dictamen ni constituye software clínico.

### 8.1. Cortes recibidos y sucesión del estado

| Objeto | Identidad y estado |
|---|---|
| Expediente inmunológico sustantivo recibido por Lenguaje | `3bea6b714be3bd1330e6ca6bbbc228b0eb9c065d`, OP-IMM-001 / Q0 v0 cerrado para transferencia. |
| Base de esta actualización en SVperitus-dataset | Rama `dominio-inmunologia`, commit `6c05192d0bf9fcb3d2c85ebd9d0ee62a58940a1b`, árbol `b4219d14a5fcda26743cdbda4f30a3f010a871e9`. Sólo añadió el acta de pausa al corte anterior. |
| Candidata del Lenguaje que recibe G/H | `SV-lenguaje-de-computacion/main@bc3b22c9e9319e8f191390c8cfe9fa1577904d87`, árbol `51d0215604b84519361aea6749a3d17811a1307e`, PR #76 integrada; RETP-090 y transición §30. |
| Área de trabajo autorizada | Inmunología, fila 6/G-H. Lenguaje queda a la espera del paquete de retorno de esta fase. |
| Siguiente receptor | Unidad del Lenguaje de computación SV, fila 7; incorpora o delimita únicamente cambios justificados por G/H. |

El commit que incorpora esta actualización identifica su salida documental mediante el historial de Git; no se utiliza una autorreferencia de hash dentro del propio archivo. I1 registrará el commit exacto efectivamente recibido de esta rama y lo distinguirá del corte clínico sustantivo y del corte del Lenguaje.

Los estados de espera y reparación de PR #60 de §§1, 6 y 7 se conservan como antecedentes del 04/09. La PR #60 ya está integrada; su reconciliación 15 ↔ 44 está disponible. K1 ha entregado sus cierres y delimitaciones expresas; K1-T mantiene su ruta productiva no habilitada. F está formulado y F-IF integrado en su alcance sintético. **No se repite la reparación de PR #60 ni se vuelve a K1 por leer aquellos estados históricos.** Rigen para la continuación esta recepción y la tabla del Lenguaje con su §30. I1–I8 y los criterios de §4 se mantienen, con las precisiones de salida de §8.5.

### 8.2. Paquete de lectura obligatorio

Todos los enlaces al Lenguaje de esta recepción fijan el mismo commit de §8.1. Deben leerse los documentos y apartados aplicables completos, no sólo los títulos ni el texto histórico de una PR.

| Orden | Fuente | Uso en el retorno |
|---|---|---|
| 1 | Esta acta, §§2–5 y §8; [entrada a cambio-rumbo](cambio-rumbo/README.md), sus actas rectoras y el [manifiesto terminal](cambio-rumbo/manifiesto-terminal-alcance-cobertura-y-terminacion-OP-IMM-001-Q0-v0-2026-09-03.md) | Autoridad, finitud, privacidad, perímetro y terminación; los 32 identificadores raíz de Q0 no son 32 universos que haya que cerrar. |
| 2 | [Pilares](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/calidad/PILARES_Y_RESTRICCIONES_DE_DISENO_DEL_LENGUAJE_DE_COMPUTACION_SV_2026_09_05.md), [perfiles](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/calidad/ACTA_TECNICA_DE_PERFILES_CONTRATOS_Y_ENSAMBLAJE_DEL_LENGUAJE_SV_2026_09_06.md) y [transición, en particular §§12–15 y 23–30](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/dominios/inmunologia/ACTA_DE_CONFORMIDAD_DE_TRANSICION_SECUENCIAL_DESDE_OP-IMM-001_AL_LENGUAJE_SV_2026_09_03.md#f-if-relevo-20260907) | Subordinación a la DSL —lenguaje específico de dominio—, competencias, contratos y secuencia vigente. N0 y sus decisiones K1 se consultan en la [radiografía completa del corte](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/arquitectura/N0_RADIOGRAFIA_DE_OBJETOS_INVARIANTES_Y_ORACULOS_DEL_NUCLEO_SV_2026_09_04.md). |
| 3 | [G10-SV, 15 requisitos](cambio-rumbo/03-base-documental-candidata/15-requisitos-lenguaje-sv/G10-SV_requisitos_demostrados_OP-IMM-001_v0.1_2026-09-03.md), [solicitud, 44 formulaciones](marco-tecnico-de-universos-subdominios-y-modulos/01-op-imm-001-informacion-preinmunosupresion-adultos/Solicitud_de_valoracion_y_encaje_tecnico_de_OP-IMM-001_con_el_Lenguaje_SV_2026-09-03.md) y [marco técnico de OP](marco-tecnico-de-universos-subdominios-y-modulos/01-op-imm-001-informacion-preinmunosupresion-adultos/Marco_tecnico_de_responsabilidad_trazabilidad_reproducibilidad_y_criticidad_OP-IMM-001_v0.1_2026-09-03.md) | Constituciones de origen. Sus fuentes y localizadores se conservan en esta rama; cambio-rumbo no agota el expediente técnico. |
| 4 | [Valoración reconciliada, especialmente §§3 y 5](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/dominios/inmunologia/VALORACION_TECNICA_Y_ENCAJE_DE_OP-IMM-001_CON_EL_LENGUAJE_SV_2026_09_03.md), [adversarial](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/dominios/inmunologia/ADVERSARIAL_DE_CONTINUIDAD_Y_CONFORMIDAD_DE_LA_VALORACION_OP-IMM-001_2026_09_03.md) y [sincronización](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/dominios/inmunologia/INFORME_DE_SINCRONIZACION_OPERATIVA_ENTRE_LENGUAJE_SV_E_INMUNOLOGIA_OP-IMM-001_2026_09_03.md) | Conservar la correspondencia 15 ↔ 44 y sus enlaces múltiples. Las afirmaciones históricas de realización se leen bajo F §6.1. |
| 5 | [F-SV/0.1-candidata, §§1–9](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/arquitectura/CONTRATO_CANDIDATO_F_DOMINIO_REPRESENTACION_Y_SUFIENCIA_POR_OPERACION_2026_09_07.md) y su fundamento [FFL-E](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/arquitectura/CONTRATO_MINIMO_DE_SUFIENCIA_REPRESENTACIONAL_POR_OPERACION_PARA_EL_LENGUAJE_SV_2026_08_21.md) | Contrato documental de representación y suficiencia por operación, identidad, ligaduras, soporte, pérdidas y sedes de resolución. No es un tipo nuevo de representación intermedia (IR). |
| 6 | [F-IF/1, §§1–7](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/docs/arquitectura/F_IF_SEIS_TESTIGOS_SINTETICOS_Y_RELEVO_G_H_2026_09_07.md), [constitución de casos](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/tests/f_if/cases.json), [evidencia](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/bc3b22c9e9319e8f191390c8cfe9fa1577904d87/tests/f_if/evidence.json) y observador/pruebas enlazados en el informe | Seis familias sintéticas, consultas, pérdidas y límites. Decidir su aplicación a OP-IMM-001; no transferirlas automáticamente al dominio. |

### 8.3. Trabajo sustantivo y preguntas que recibe Inmunología

La unidad ejecutará I1–I8, utilizando un único expediente principal de retorno y anexos sólo cuando sean necesarios para prueba. Reutilizará los documentos y los identificadores existentes; no emitirá una tercera familia de requisitos ni otra acta para confirmar esta recepción.

1. Validar cada correspondencia 15 ↔ 44 desde el significado del dominio, conservando equivalencia, refinamiento, cobertura parcial, ampliación, duplicación o falta de cobertura con fuente y localizador. Cubrir ambos extremos y los enlaces múltiples.
2. Constituir el candidato documental de perfil completo respecto de OP-IMM-001 / Q0 v0 y su versión: objeto, límites, cuatro salidas, reglas, procedencia, configuración, autoridad, vetos, causas de U, no aplicabilidad, no admisión y fallo técnico. Aplicar I3 sin presentarlo como tipo normativo ni operación SV ya ejecutable.
3. Para cada familia F-IF, justificar aplicación, aplicación parcial o no aplicación al perímetro; para las consultas aplicables identificar la información imprescindible, distinciones perdidas, captura, admisibilidad, identidad de instancia y ligaduras requeridas. Vincularlas a requisitos y objetos constituidos; no deducirlas de semejanza nominal ni asignarlas automáticamente a los 27 parámetros.
4. Especificar o ejecutar, donde exista realización válida, los oráculos positivos y negativos de I4. Distinguir prueba ejecutada, especificación pendiente y evidencia no disponible. Para una pérdida, conservar un par de entradas y la distinción necesaria para la operación, o declarar por qué todavía no se puede constituir ese testigo.
5. Dictaminar fidelidad, pérdida o suficiencia no acreditada por operación y representación. Identificar qué resuelve el dominio y qué debe recibir Lenguaje, perfil, interfaz o infraestructura. La aceptación documental no acredita ejecución clínica.

### 8.4. Precisiones vinculantes

- **Agrupaciones y célula:** la frase histórica de §1 «encaja directamente en SV(9,3)» queda precisada por F §6: las cardinalidades `(6,1,3,2,6,9)` son agrupaciones externas. `M-MODIFIER-001`, de nueve miembros, es candidata a posible célula, pendiente de constitución. La cardinalidad no basta para constituirla. `REQ-IMM-SV-011 = U_NO_DECIDIDO` se conserva salvo evidencia nueva; no se rellena, duplica ni fuerza la geometría.
- **Realización pendiente:** DFL-005 mantiene mínimo por operación, identidad `(C,j)` y ligaduras pendientes; K1-T no habilita observación → Tri; DFL-006 mantiene pendiente el productor de criticidad. Registrar las necesidades no crea esas realizaciones ni autoriza sortear sus bloqueos.
- **F-IF:** seis familias sintéticas, 18 consultas y 54 filas de contraste externo no son estados clínicos constituidos. Ninguna de esas 18 consultas se ofrece por ese resultado como operación ejecutable de SV. Las distinciones de laboratorio, citometría, médula, terapia, episodio e historia no amplían por sí mismas Q0; DICOM continúa no aplicable al corte OP recibido.
- **Custodia:** el compilador Python está retirado (RETP-082, F §6.1). No actúa como compilador ni autoridad de contraste del SV actual. Rust realiza la DSL y está subordinado a ella; compilar Rust no acredita conformidad semántica. Los observadores externos no constituyen SV. Toda modificación ejecutable pertinente se remite a Lenguaje con conformidad y paridad nativa/WASM —WebAssembly— exigibles sobre ese mismo corte; no se atribuye una prueba nueva a una modificación documental.
- **Perímetro y evidencia:** se conservan los 27 parámetros, cuatro salidas exclusivas y exclusiones del expediente informativo predecisional; G9-EMP permanece `NO_OBSERVABLE`, con cero conjuntos admisibles, mientras no haya evidencia nueva. Este retorno no exige obtener cohortes, habilitar asistencia, constituir agente ni cerrar toda la Inmunología.
- **Infraestructura:** DFL-009, incluido servicio nativo remoto y Cloudflare/Workers u otros, se recibe en fila 9 después del primer universo de Ciberseguridad Inteligente. No se convierte en condición nueva de G/H.

<a id="retorno-a-lenguaje"></a>

### 8.5. Cuándo y cómo devolver el control

**Retorno ordinario obligatorio:** al completar I1–I8 y la cobertura documental de §4 respecto del perímetro de esta fase, la unidad entregará un único paquete identificado a la unidad de programación y detendrá su avance sustantivo. El paquete contendrá, directamente o por localizadores inequívocos:

1. commit de entrada y de salida de Inmunología, corte exacto del Lenguaje, archivos y huellas de los testigos utilizados;
2. matriz 15 ↔ 44 revisada y aplicación de F-IF, con cobertura explícita, pendientes y motivo de cada no aplicación;
3. contrato de perfil candidato y dictamen por operación/representación, con las cuatro salidas y separación de U, no aplicación, no admisión y fallo;
4. testigos positivos, negativos y de pérdida, indicando cuáles se ejecutaron y cuáles sólo quedaron especificados;
5. resultado de la evaluación adversarial, precisiones incorporadas, estado de REQ-IMM-SV-011 y deuda residual con responsable y condición de resolución.

El dictamen puede ser **aceptación en alcance declarado o devolución fundada por pérdida/insuficiencia**. Completar el contraste no exige que todas las representaciones sean suficientes. Concluir la evaluación adversarial de G/H significa incorporar o identificar sus hallazgos y atribuir su resolución; no ocultar una refutación ni esperar indefinidamente a que Inmunología implemente una carencia del Lenguaje. La deuda imprescindible bloquea la operación afectada, no la devolución del dictamen a quien debe resolverla.

**Devolución anticipada fundada:** si I1 no puede establecer la identidad o acceso a una fuente decisiva, o una contradicción/carencia externa hace imposible completar honestamente el contraste, la unidad devolverá el control con el corte, el punto exacto, la evidencia disponible, el responsable y la lista de verificaciones no realizadas. Podrá completar antes las comprobaciones independientes que sigan siendo válidas. No presentará esa devolución como cierre favorable de I1–I8, no convertirá el impedimento documental en U clínica ni abrirá otro universo para evitarlo.

**Después de cualquiera de las dos devoluciones:** Inmunología queda en pausa controlada, a la espera de respuesta expresa. La unidad de programación recibe la fila 7, resuelve o delimita los hallazgos bajo Pilares y Calidad y fija la candidata siguiente. Si necesita una precisión exclusivamente inmunológica, solicitará un retorno acotado identificado; no se reanuda el dominio por calendario ni por una actualización incidental de main.

Ciberseguridad Inteligente, fila 8/I-J, sólo recibirá después la candidata identificada por Lenguaje mediante su relevo. Inmunología no inicia el trabajo en ese dominio, no escribe en el repositorio del Lenguaje y no abre álgebra, K2 ni R2/R3/R4. Se mantiene una única área de trabajo sustantivo activa. No se fusiona esta rama con main por este acto.

### 8.6. Alcance de esta actualización

Esta actualización corrige la continuidad y la localización de la documentación del dominio; conserva los apartados de 04/09 como antecedentes y no modifica el corpus clínico. La revisión documental comprueba cortes, enlaces, sucesión de estados, I1–I8 y las dos salidas de §8.5. No se atribuye una nueva prueba clínica, ejecución SV ni auditoría externa. Su identidad final queda en el commit de la rama que contiene el acta y las entradas de navegación actualizadas.


<a id="devolucion-gh-20260907"></a>

## 9. Devolución ordinaria fundada de G/H y pausa controlada · 07/09/2026

En ejecución de la autorización de §8 y de su regla de devolución §8.5, queda incorporado el [paquete único de retorno OP-IMM-001 / Q0 v0](marco-tecnico-de-universos-subdominios-y-modulos/01-op-imm-001-informacion-preinmunosupresion-adultos/retorno-gh-2026-09-07/RETORNO_GH_OP-IMM-001_Q0_v0_AL_LENGUAJE_SV_2026-09-07.md), con un expediente principal y seis anexos necesarios de contrato, fuentes y prueba. Este apartado registra el relevo; no abre otra acta ni modifica el corpus clínico recibido.

- Entrada de Inmunología: `d4d6c81cb9aab5194abc8e61212c0d63877a0b9c`.
- Corte del Lenguaje contrastado: `bc3b22c9e9319e8f191390c8cfe9fa1577904d87`.
- Salida: commit de incorporación del paquete y este apartado, con padre único `d4d6c81…`, localizable por el historial de alta del expediente principal; sin autorreferencia circular.
- I1–I8: completos en el alcance documental autorizado. Se verifican 44 fuentes, 15 requisitos, 44 formulaciones y 81 enlaces. Se conserva el contrato candidato completo del perímetro, 27 parámetros y cuatro salidas exclusivas.
- Prueba ejecutada: campaña F-IF reproducida (54 filas), sus 12 pruebas de sensibilidad y ocho pares documentales propios; dos ejecuciones independientes del verificador con bytes idénticos. Las doce comprobaciones integradas pendientes se identifican como solamente especificadas.
- Dictamen: **devolución fundada por suficiencia no acreditada para ejecutar Q0**, con fidelidad y pérdidas demostradas únicamente en los espacios documentales declarados. La adversarial incorpora hallazgos materiales y atribuye su resolución; no acredita ejecución clínica.
- `REQ-IMM-SV-011 = U_NO_DECIDIDO`; ninguna célula constituida por cardinalidad. K1-T y DFL-005/006 conservan sus carencias; Python no interviene. G9 continúa `NO_OBSERVABLE`, con cero conjuntos admisibles.

**Control devuelto a la unidad del Lenguaje SV, fila 7. Estado de Inmunología: `PAUSA_CONTROLADA_TRAS_DEVOLUCION_GH`.** La unidad receptora resolverá o delimitará sus hallazgos y fijará la candidata siguiente. Una precisión exclusivamente inmunológica requiere un nuevo retorno acotado identificado. No se espera aquí a resolver una carencia de Lenguaje; no se abre Ciberseguridad, otro universo ni otra fase, no se escribe en Lenguaje y no se fusiona esta rama con main.
