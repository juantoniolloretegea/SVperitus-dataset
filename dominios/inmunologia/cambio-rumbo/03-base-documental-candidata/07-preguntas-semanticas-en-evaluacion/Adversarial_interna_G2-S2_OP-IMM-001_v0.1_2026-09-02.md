# Adversarial interna G2-S2 — OP-IMM-001 v0.1

- **Fecha:** 02-09-2026
- **Objeto:** segundo lote semántico de 9 preguntas candidatas
- **Dictamen interno:** `PASA_PARA_AUDITORIA_EXTERNA`
- **Efecto máximo:** auditar y, si resiste, cerrar G2-S2; no cerrar G2 total ni abrir G3
- **Privacidad:** `PRIVACIDAD_PASA`

## 1. Recuento e identidad

| Familia | Identificadores | Recuento |
|---|---|---:|
| Contexto biológico | `SEM-CTX-005` | 1 |
| Estado del huésped | `SEM-HUE-005` | 1 |
| Modificadores generales | `SEM-MOD-001` a `SEM-MOD-007` | 7 |
| **Total** | identificadores únicos | **9** |

Cada fila contiene formulación candidata, función provisional, dependencia, `U` propia posible y exclusión expresa.

## 2. Ataques transversales

| Ataque | Intento de falsación | Resultado interno |
|---|---|---|
| Parámetro prematuro | interpretar una pregunta como estado ya definido | no hay valores, transductor, observable, unidad, umbral o ventana |
| Comorbilidad como inmunodeficiencia | hacer equivalentes modificador general y déficit inmunitario | prohibido por función y exclusiones |
| Diagnóstico como función | cerrar reserva o estabilidad por el nombre de una enfermedad | el lote mantiene diagnóstico, función, estabilidad y pertinencia abiertos |
| Consecuencia encubierta | convertir menor reserva en daño o veto automático | no se constituye gravedad, mecanismo ni contraindicación |
| Edad como decisión | usar edad cronológica como sustituto de fragilidad o limitación terapéutica | `SEM-CTX-005` lo excluye |
| Agregado cardiometabólico | conservar el compuesto histórico del piloto | metabolismo, cardiovascular y renal tienen identidades distintas |
| Nutrición como fragilidad | cerrar una por la otra | `SEM-MOD-006` y `SEM-MOD-007` pueden divergir |
| Órgano como tratamiento | usar función renal o hepática para ajustar una dosis | prohibido expresamente |
| Protocolo local duplicado | importar medios institucionales en cada modificador | la ejecución local permanece en `SEM-CTX-004` |
| Herencia de pilotos | trasladar entradas, estados o dimensiones históricas | los pilotos sólo señalan compuestos que deben atacarse |
| Privacidad | introducir una persona, cargo, centro, lugar, cronología o episodio real | no hallado; todos los casos son abstractos y no atribuibles |

## 3. Casos sintéticos adversariales

| Caso no atribuible | Resultado exigido |
|---|---|
| edad avanzada sin fragilidad demostrada | `SEM-CTX-005` no cierra `SEM-MOD-007` |
| fragilidad con estado nutricional no alterado | `SEM-MOD-007` no cierra `SEM-MOD-006` |
| alteración nutricional sin fragilidad constituida | `SEM-MOD-006` no cierra `SEM-MOD-007` |
| condición metabólica estable sin enfermedad cardiovascular | `SEM-MOD-001` no cierra `SEM-MOD-002` |
| función renal alterada con situación metabólica desconocida | `SEM-MOD-003` conserva identidad independiente |
| diagnóstico pulmonar estable sin función ni pertinencia adjudicadas | `SEM-MOD-004` permanece abierto |
| diagnóstico hepático sin función actual documentada | `SEM-MOD-005` no se cierra por etiqueta diagnóstica |
| estado linfocitario conocido y estado neutrofílico desconocido | `SEM-HUE-005` conserva incertidumbre propia |
| identidad farmacológica conocida y estado neutrofílico no vigente | la exposición no cierra el estado del huésped |
| limitación local para ejecutar una actuación | se conserva en `SEM-CTX-004`; no redefine ningún modificador |

## 4. Ataque de atomicidad diferida

`SEM-HUE-005` puede ocultar cantidad, función, duración, trayectoria y causa. La pregunta no pasa todavía una prueba de atomicidad; por eso no se convierte en parámetro y queda priorizada para `G3-OBS` y `G5-ATM`.

Las siete filas `SEM-MOD` designan familias clínicas diferenciables, no necesariamente átomos finales. En especial:

- una condición metabólica puede exigir varias identidades;
- una condición cardiovascular puede afectar reserva o ruta por mecanismos distintos;
- alteración renal o hepática puede separar función, cronicidad y estabilidad;
- enfermedad pulmonar y reserva respiratoria pueden divergir;
- nutrición y fragilidad pueden requerir escalas y fuentes distintas.

La incertidumbre no invalida G2 si está visible y no se simula atomicidad.

## 5. Ataque de dependencia

Se intentó excluir cada pregunta por ser medicina general y no inmunología. El ataque no prospera automáticamente: `OP-IMM-001` exige el perfil que necesita una decisión preinmunosupresión, y una condición puede pertenecer por modificar susceptibilidad, consecuencia o ruta aunque no sea un déficit inmunitario.

La dependencia deberá demostrarse individualmente en fases posteriores. Si una fuente autorizada no sostiene que una familia cambia la lectura o la ruta, esa candidata se elimina; no se conserva por plausibilidad.

## 6. Freno de mano

No se añadieron:

- diagnósticos concretos ni listas de enfermedades;
- otras series hematológicas sin dependencia diferenciada;
- escalas de fragilidad o nutrición;
- pruebas de laboratorio o función de órgano;
- dosis, equivalencias o ajustes farmacológicos;
- vacunas, profilaxis, exposiciones epidemiológicas o seguimiento;
- cohortes o datos de pacientes;
- parámetros, matrices o lenguaje de programación.

## 7. Incertidumbres legítimas

| ID | Incertidumbre | Destino permitido |
|---|---|---|
| `U-G2S2-01` | cantidad y función neutrofílica podrían exigir preguntas separadas | G3/G5 |
| `U-G2S2-02` | cada familia modificadora puede contener identidades distintas | lotes posteriores y G5 |
| `U-G2S2-03` | «pertinente» carece aún de regla operativa | G3/G4 |
| `U-G2S2-04` | influencia sobre susceptibilidad, consecuencia y ruta puede divergir | G4 y composición posterior |
| `U-G2S2-05` | el universo semántico total sigue abierto | lotes G2 posteriores |

## 8. Compuerta de privacidad

La inspección del texto, nombres de archivo, tablas, casos y metadatos textuales no halló identidad directa, relación personal, institución, localización, cronología clínica ni relato de una persona real. Los casos son mínimos, abstractos y construidos sólo para producir divergencia lógica.

Resultado: `PRIVACIDAD_PASA`.

## 9. Dictamen

Las nueve preguntas son distinguibles como candidatas y mantienen visibles sus posibles desdoblamientos. Ninguna constituye parámetro, consecuencia, actuación o matriz.

**Resultado: `PASA_PARA_AUDITORIA_EXTERNA`.**

`G2-SEM` total permanece abierto. `G3-OBS` permanece bloqueada.

