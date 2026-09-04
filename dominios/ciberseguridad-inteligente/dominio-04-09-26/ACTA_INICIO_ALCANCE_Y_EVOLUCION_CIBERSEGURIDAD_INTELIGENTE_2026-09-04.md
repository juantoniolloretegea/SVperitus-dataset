# Acta de inicio, alcance y evolución del dominio de ciberseguridad inteligente

- **Versión:** 0.1
- **Fecha:** 04-09-2026
- **Identificador:** `ACTA-CIB-INICIO-2026-09-04`
- **Repositorio:** `SVperitus-dataset`
- **Rama de trabajo:** `dominio-ciberseguridad-inteligente`
- **Ruta:** `dominios/ciberseguridad-inteligente/dominio-04-09-26/`
- **Base de apertura de la rama, una vez alineada con `main`:** `74f849500845274799d1c4d46aa84f42895baea9`
- **Estado:** `RECTOR_DE_INICIO · SEMILLA_CONSTITUIDA · EJECUCION_DIFERIDA`

## 0. Objeto

Esta acta constituye y custodia el encargo de crear un dominio completo y versionado de **ciberseguridad inteligente**, capaz de ejercer presión real y heterogénea sobre el Lenguaje de computación SV. No constituye todavía el dominio, uno de sus universos, un perfil ejecutable, un agente, un superagente ni una ampliación del Lenguaje.

El trabajo sustantivo queda diferido hasta que la unidad de Lenguaje entregue un corte apto para contraste. Esta decisión evita diseñar el segundo dominio contra ambigüedades nucleares ya conocidas y evita, al mismo tiempo, que Ciberseguridad quede olvidada.

## 1. Decisiones constitutivas

1. El dominio se denomina **ciberseguridad inteligente** y su primera área de trabajo es esta carpeta versionada.
2. Ciberseguridad será el segundo dominio heterogéneo empleado para falsar la suficiencia transversal del Lenguaje, no una demostración automática de universalidad.
3. El dominio deberá definirse entero respecto de su versión y perímetro declarado. «Entero» no significa abarcar toda la ciberseguridad mundial, sino no ocultar dentro del perímetro elegido objetos, relaciones, operaciones, salidas, fallos, exclusiones o deudas necesarios.
4. El trabajo seguirá el rigor constitutivo observado en Inmunología, pero no copiará su ontología, sus cardinalidades, sus salidas ni su organización documental por mera analogía.
5. El Lenguaje puede formular necesidades de identidad, tipado, representabilidad, composición, determinismo, integridad, trazabilidad y serialización. No posee veto sobre el conocimiento válido del dominio ni puede exigir que se mutile para encajar en la IR existente.
6. Ciberseguridad no puede convertir una necesidad particular en semántica nuclear por simple exigencia. Cuando una necesidad legítima no sea representable, deberá entregar un requisito trazable y un testigo de pérdida.
7. Ninguna unidad trabajará en paralelo por defecto. El cambio de frente exige relevo explícito y corte identificable.

## 2. Precedente inmunológico que debe leerse, no imitarse

Existe un corte de trabajo inmunológico congelado y en pausa controlada:

```text
REPOSITORIO = SVperitus-dataset
RAMA        = dominio-inmunologia
COMMIT      = 3bea6b714be3bd1330e6ca6bbbc228b0eb9c065d
UNIVERSO    = OP-IMM-001 / Q0 v0
ESTADO      = CERRADO_PARA_TRANSFERENCIA_AL_LENGUAJE
DOMINIO_INMUNOLOGIA_GLOBAL = NO_CERRADO
```

La unidad de Ciberseguridad deberá distinguir esos dos últimos estados. Lo cerrado es el recorrido constitutivo del universo operacional `OP-IMM-001 / Q0 v0`; no toda la inmunología internacional.

En el corte citado, Inmunología trabajó con esta secuencia verificable:

1. perímetro profesional y mapa finito de operaciones;
2. observables y consecuencias;
3. catálogo atómico anterior a la construcción matricial;
4. matrices propietarias sin relleno, duplicación ni mezcla oportunista;
5. rutas, salidas y tratamiento explícito de `U`;
6. contrato técnico declarativo y laboratorio;
7. contraste empírico con salida terminal `NO_OBSERVABLE` cuando no hubo datos admisibles;
8. entrega de requisitos al Lenguaje sin modificarlo desde el dominio.

El universo dejó, entre otros datos, `|A0|=27`, seis matrices de cardinalidad `(6, 1, 3, 2, 6, 9)`, cuatro salidas exclusivas y una tensión abierta de representabilidad (`REQ-IMM-SV-011 = U_NO_DECIDIDO`). Estas cifras sirven como evidencia histórica de que un dominio puede refutar una abstracción; **no son parámetros para Ciberseguridad**.

Documentos de lectura obligatoria en el corte inmunológico:

- [`G10-SV — requisitos demostrados para el Lenguaje SV / OP-IMM-001`](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/3bea6b714be3bd1330e6ca6bbbc228b0eb9c065d/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/15-requisitos-lenguaje-sv/G10-SV_requisitos_demostrados_OP-IMM-001_v0.1_2026-09-03.md)
- [`Solicitud de valoración y encaje técnico de OP-IMM-001`](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/3bea6b714be3bd1330e6ca6bbbc228b0eb9c065d/dominios/inmunologia/marco-tecnico-de-universos-subdominios-y-modulos/01-op-imm-001-informacion-preinmunosupresion-adultos/Solicitud_de_valoracion_y_encaje_tecnico_de_OP-IMM-001_con_el_Lenguaje_SV_2026-09-03.md)
- [`Acta de secuencia constitutiva y acoplamiento con el Lenguaje`](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/3bea6b714be3bd1330e6ca6bbbc228b0eb9c065d/dominios/inmunologia/cambio-rumbo/acta-secuencia-constitutiva-custodia-rumbo-y-acoplamiento-lenguaje-sv-inmunologia-2026-09-02-v0.1.md)

De ese precedente se adopta la disciplina: finitud, procedencia, identidad, secuencia, puertas, adversarial, conservación de `U`, separación entre salida válida y fallo técnico, y autoridad humana. No se adoptan por herencia vocabulario clínico, FHIR, geometría, umbrales, criticidades, matrices, salidas ni jurisdicción clínica.

## 3. Dominio, perfil y agente

Se fijan como objetos distintos:

| Objeto | Función | Restricción |
|---|---|---|
| `PerfilDominio` | Declara un dominio finito respecto de identidad, versión y perímetro | No es un perfil lingüístico ni introduce por sí solo semántica nuclear |
| `UniversoOperacional` | Recorrido cerrado de una operación o familia acotada dentro del dominio | No equivale al dominio entero |
| `CoberturaAgente` | Declara qué parte del perfil o qué operaciones puede recorrer un agente | No se presume cobertura total |
| `InstanciaAgente` | Realización concreta con dependencias, autoridad y límites | No nace automáticamente al cerrar el dominio |
| `ComposicionTipadaAgentes` | Relación explícita entre agentes legitimados | Debe conservar tipado, procedencia, resolución y codominio |
| `Superagente` | Resultado eventual de una composición legitimada | No se deduce de poseer dos perfiles ni de ensamblar archivos |

Un agente podrá aprovechar el dominio completo o sólo una parte expresamente tipada. El dominio no se reducirá para adaptarse a un agente previsto y un agente no extenderá silenciosamente el dominio que declara cubrir.

La disciplina de perfiles lingüísticos español/inglés puede inspirar identidad, versionado y selección explícita, pero la analogía termina ahí: un perfil fuente no añade campo semántico a la IR; un perfil de dominio precisamente declara significado externo que debe conservarse y enlazarse.

## 4. Alcance material del futuro dominio

El primer corte deberá escoger un perímetro operacional realista y finito dentro de la ciberseguridad contemporánea, incluyendo cuando sea pertinente sistemas de IA en producción y modelos que evolucionan a corto o medio plazo. La selección exacta corresponderá a la unidad de dominio y a la Dirección, no a esta acta.

El expediente deberá poder responder, al menos, sin prejuzgar todavía sus tipos finales:

- qué activos, contextos, evidencias, amenazas, controles, acciones y autoridades pertenecen al perímetro;
- qué hechos son observados, inferidos, desconocidos, no aplicables o técnicamente fallidos;
- qué dependencias temporales y qué caducidad tienen los datos y evaluaciones;
- qué acciones requieren veto, supervisión o autorización humana;
- qué salida exclusiva o composición de salidas produce cada operación;
- qué pérdida se produciría al proyectar esos objetos al Lenguaje SV;
- qué queda expresamente fuera del corte.

Los modelos de IA actuales se tratarán según su función efectiva: fuente, componente, evaluador, objeto de riesgo o herramienta auxiliar. Cada uso deberá fijar, como mínimo cuando aplique, proveedor, familia, identificador de modelo, versión o fecha, artefacto o huella, configuración, dependencias, política de actualización, límites y evidencia reproducible.

Queda prohibido hacer depender una conclusión normativa de:

- un alias flotante como `latest`;
- una llamada en vivo no capturada;
- una respuesta no reproducible;
- una marca comercial usada como tipo semántico;
- o la autoridad aparente de un modelo.

Los secretos, credenciales, vulnerabilidades explotables no publicadas, datos personales y telemetría sensible no se incorporarán al corpus. Se usarán artefactos públicos, sintéticos, anonimizados o controlados, con manifiesto y licencia o autoridad de uso.

## 5. Relación bilateral con el Lenguaje de computación

El acoplamiento se regirá por una frontera de doble no dominación:

```text
LENGUAJE_NO_RECORTA_DOMINIO = OBLIGATORIO
DOMINIO_NO_COLONIZA_NUCLEO  = OBLIGATORIO
PERDIDA_NO_DECLARADA        = PROHIBIDA
CORRECCION_SILENCIOSA       = PROHIBIDA
NECESIDAD_NO_REPRESENTABLE  = REQUISITO_TRAZABLE
```

El Lenguaje podrá contestar `YA_REPRESENTABLE`, `REPRESENTABLE_POR_COMPOSICION`, `REQUIERE_PERFIL_DE_DOMINIO`, `CANDIDATA_A_EXTENSION`, `CONFLICTO` o `U_NO_DECIDIDO`, siempre con localizador y prueba. La unidad de dominio conserva la decisión sobre la verdad y suficiencia cibersegura de la representación; la unidad de Lenguaje conserva la decisión sobre el núcleo, la IR, la gramática y su realización.

## 6. Secuencia obligatoria y retornos

### Fase C0 — ahora: custodia de la semilla

Se crean este acta y el README. No se puebla el conjunto de datos y no se constituye un universo. Con ello queda satisfecho todo lo obligatorio de Ciberseguridad **antes de reparar la PR #60**.

### Fase L1 — Lenguaje: reparación documental inmediata

La unidad de Lenguaje repara la PR #60 y reconcilia las dos familias de requisitos inmunológicos existentes (`REQ-IMM-SV-001..015` y `REQ-IMM-LSV-001..044`) sin pedir una nueva adenda a Inmunología.

### Fase L2 — Lenguaje: frontera e invariantes intrínsecos

En rama nueva del Lenguaje se produce `N0`, entendido como clasificación de los objetos existentes y orden de oráculos, no como una segunda gramática ni una meta-IR especulativa. Después se cierran los invariantes intrínsecos independientes del vocabulario clínico: unicidad de codominio, totalidad y no ambigüedad de semántica de salida, proyección canónica sin colisiones, integridad referencial de arquitectura y dictamen del ensamblaje vacío.

### Fase I1 — retorno acotado a Inmunología

Inmunología contrasta el candidato del Lenguaje contra `OP-IMM-001`, valida la reconciliación de requisitos, mantiene visible `REQ-IMM-SV-011` y devuelve testigos de pérdida o conformidad. No completa los demás universos ni abre una nueva adenda.

### Fase L3 — incorporación del retorno inmunológico

Lenguaje corrige o estabiliza su contrato de perfil de dominio y publica un corte identificable para el segundo falsador.

### Fase C1 — apertura sustantiva de Ciberseguridad

Por mandato expreso se activa esta rama. Antes de contenido nuevo se verifica la custodia basal aplicable y se declara el corte exacto del Lenguaje recibido. Después se ejecuta, en serie:

1. perímetro finito, propósito, exclusiones y autoridades;
2. inventario de fuentes, artefactos y datos admisibles;
3. catálogo de objetos, relaciones y operaciones antes de imponer una geometría;
4. consecuencias, salidas, `U`, fallos y vetos;
5. al menos un universo operacional falsador con corpus reproducible;
6. perfil de dominio completo respecto de ese corte;
7. matriz de cobertura y testigos de pérdida contra el Lenguaje;
8. requisitos clasificados y entrega única a Lenguaje.

### Fase L4 — segundo retorno y consolidación

Lenguaje recibe el expediente de Ciberseguridad, resuelve lo transversal y separa lo propio del perfil. Sólo después de sobrevivir a ambos dominios podrá hablar de núcleo consolidado para esos perfiles. No podrá declarar universalidad absoluta por dos muestras.

### Fase A — agentes, composición y superagente

La constitución de agentes ocurre después de los perfiles. Cada agente declara cobertura. La composición y un eventual superagente se someten a las reglas estatutarias de legitimación previa, relación semántica, tipado visible, resolución de colisiones, procedencia retrospectiva, codominio explícito y representación inteligible. Esta fase no forma parte del cierre del dominio inicial.

## 7. Puertas de entrada y salida de Ciberseguridad

### Entrada a trabajo sustantivo

Deben concurrir todos estos hechos:

- mandato humano expreso;
- custodia basal identificada;
- rama y base exactas verificadas;
- PR #60 reparada o sustituida por un cierre equivalente;
- `N0` e invariantes intrínsecos cerrados;
- retorno inmunológico incorporado en un corte del Lenguaje;
- ausencia de otro frente sustantivo activo.

### Salida hacia Lenguaje

El paquete no se entrega hasta contener:

- identidad y versión del perfil;
- perímetro y exclusiones;
- al menos un universo operacional cerrado;
- fuentes y artefactos reproducibles;
- semántica de estados, salidas y fallos;
- matriz de cobertura;
- inventario único de requisitos;
- testigos negativos y de pérdida;
- deuda visible;
- adversarial interna;
- declaración de que no existe todavía agente ni capacidad operativa, salvo que otro acto los constituya.

## 8. Evolución

Los cambios materiales no se sobrescribirán como si siempre hubieran existido. Se conservarán por commits y, cuando cambie el perímetro constitutivo, mediante un nuevo corte `dominio-DD-MM-AA` enlazado con su predecesor. La fecha identifica el corte; no sustituye dentro de los artefactos la identidad semántica ni la versión de cada objeto.

## 9. Dictamen de proceso

```text
CIBERSEGURIDAD_ANTES_DE_PR_60       = SEMILLA_Y_CUSTODIA_SOLAMENTE
NECESIDAD_DE_CERRAR_UNIVERSO_AHORA  = NO
RIESGO_DE_OMITIR_REQUISITO_ACTUAL   = CONTROLADO_POR_PUERTA_C1
INMUNOLOGIA_COMO_METODO             = SI
INMUNOLOGIA_COMO_ONTOLOGIA          = NO
DOMINIO_COMPLETO_RESPECTO_VERSION    = OBLIGATORIO
COBERTURA_TOTAL_POR_AGENTE           = NO_PRESUMIDA
SUPERAGENTE                          = NO_CONSTITUIDO
FRENTE_ACTIVO                        = LENGUAJE_DE_COMPUTACION
```

Con la firma registral de este commit queda constituida la semilla y diferido, sin pérdida, el trabajo efectivo del dominio.
