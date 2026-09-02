# Orden de auditoría externa única — `NA0-MATH` y universo precursor `Q0` INMUNO v0.1

## 1. Objeto invariable

- **Rama:** `dominio-inmunologia`
- **Commit candidato:** `bef92dd102a170653c0beb39df21ccd5ad0849c8`
- **Línea base:** `9d08c1a8ea334be9689700fb957fb1928641b32c`
- **Perímetro:** contrato matemático, registro precursor, adversarial interna y cambio de índice

| Objeto | Bytes | SHA-256 |
|---|---:|---|
| `Contrato_matematico_parametro_atomico_matriz_ruta_INMUNO_v0.3_2026-09-02.md` | 15 303 | `5426e97f4ded65198f2e347beed2203e28b1a6da269f45b6e1e4e9e164d14640` |
| `Registro_precursor_parametros_INMUNO_v0.1_2026-09-02.xlsx` | 20 886 | `2fd702da9c4cb8766594a740a0212a965e4a83e423b828053a589d9612098120` |
| `Adversarial_interna_modelo_matematico_parametros_INMUNO_v0.3_2026-09-02.md` | 7 899 | `aac9580d9de32893b518bc2011518339f494b64bed7bce9c65d073c86a6cae7f` |

No auditar otro commit ni reconstruir el XLSX desde el Markdown. La adversarial interna orienta los flancos, pero no constituye evidencia suficiente.

## 2. Regla de suficiencia

Cada ataque B–J debe incluir al menos un contraejemplo material propio. No basta afirmar que la definición parece coherente. Si el contraejemplo atraviesa el contrato sin producir el fallo previsto, el ataque no pasa.

Se solicita una sola auditoría. Debe cerrar conjuntamente el modelo matemático, la integridad del universo precursor `Q0` y el lote semántico `G2-S2`; no debe abrir auditorías laterales.

## 3. Ataque A — Identidad y regresión

1. Recalcular bytes y SHA-256 de los tres objetos.
2. Comparar el commit candidato con la línea base.
3. Confirmar que sólo cambian las tres altas declaradas y `dominios/inmunologia/cambio-rumbo/README.md`.
4. Confirmar que no cambian catálogos, pilotos, `G1`, `G2-S1`, `G2-S2`, políticas de protección, ITI ni Lenguaje SV.
5. Abrir el XLSX real, comprobar cinco hojas, rangos usados, fórmulas y ausencia de errores.

## 4. Ataque B — Identidad atómica estable y uso variable

Intentar falsar estas dos reglas simultáneas:

```text
el parámetro conserva identidad entre operaciones
la operación gobierna activación, función y consecuencia mediante u(p,O)
```

Probar al menos:

- el mismo parámetro activo en dos operaciones con consecuencias distintas;
- el mismo observable alimentando dos proposiciones diferentes;
- dos parámetros parecidos que no comparten sujeto o predicado;
- un cambio material de proposición oculto bajo el mismo `Parametro_ID`.

Dictaminar si el contrato evita tanto la duplicación de identidad como la falsa consecuencia universal.

## 5. Ataque C — Átomo, observable y compuesto

Aplicar divergencia, ablación, `U` independiente y consecuencia independiente a estos contraejemplos:

1. Un único campo informático que agrega dos decisiones clínicas.
2. Una proposición sostenida por tres observables concordantes.
3. Dos subproposiciones con `a=U` y `b=0`.
4. Una pieza inferior cuya retirada sólo elimina evidencia, sin crear una decisión propia.
5. Una proposición con varias consecuencias derivadas del mismo estado.

Comprobar que el contrato desdobla sólo cuando existe independencia gobernable y que no confunde granularidad física o informática con atomicidad clínica.

## 6. Ataque D — Tabla autorizada y clasificación

Comprobar que:

- `Parametro_ID` es identidad, no magnitud ni puntuación;
- `Familia` y `Subfamilia` ordenan, pero no determinan estado, criticidad, matriz o ruta;
- sólo `PARAMETRO_ATOMICO` entra en `A_v`;
- los siete estatutos del candidato son mutuamente excluyentes;
- una novedad crea versión o identidad explícita y no reescribe silenciosamente la tabla.

Intentar introducir una pregunta G2, un `Pxx`, una prueba o un campo como átomo sin pasar la compuerta.

## 7. Ataque E — Propiedad matricial y no duplicación

Intentar que dos matrices posean o recalculen el mismo parámetro. Verificar:

```text
owner_v : A_v -> M_v
i != j => P_i ∩ P_j = vacío
```

Comprobar que la referencia tipada conserva identidad, estado, `U` y versión, y que permite funciones distintas en matrices de destino sin crear otro átomo.

## 8. Ataque F — Composición, ruta crítica y frame

Construir contraejemplos de:

- mayoría favorable con un veto crítico;
- ahorro o disponibilidad que pretende compensar un riesgo clínico;
- `U` crítica sin tratamiento autorizado;
- frame resumen que oculta un `U` o veto del frame constitutivo;
- dimensión `(25,5)` utilizada como molde obligatorio.

Verificar que el hipergrafo dirigido, la ruta crítica y la proyección de frames absorben cada caso sin crear una decisión generativa.

## 9. Ataque G — Finitud y freno de mano

Auditar la regla de cola:

```text
Q_(t+1) = pendientes(Q_t) + hijos_de_compuestos(Q_t)
```

Intentar producir:

- análisis infinito por novedad posterior;
- compuesto declarado sin hijos ni `U`;
- residual oculto bajo una afirmación de exhaustividad;
- cierre con uso sin consecuencia o función;
- cierre con duplicación de propiedad matricial.

Dictaminar si las nueve condiciones de cierre son necesarias, comprobables y conjuntamente suficientes para cerrar una versión sin afirmar exhaustividad permanente.

## 10. Ataque H — Integridad computable de `Q0`

Verificar directamente en el XLSX:

- 32 candidatos únicos;
- 23 en `G2-S1` y 9 en `G2-S2`;
- distribución `RUT=1, CTX=5, EXP=5, HUE=5, BAR=4, HIS=5, MOD=7`;
- 50 posiciones piloto;
- 8 familias de colisión;
- 0 parámetros atómicos autorizados;
- 0 matrices constituidas;
- fórmulas de control = `PASA`;
- ningún error de fórmula;
- ninguna fila G2 convertida en parámetro, observable, consecuencia plena o matriz.

Comparar las 32 preguntas contra sus lotes Markdown y las 50 posiciones contra el cribado v0.2. Determinar si los mapeos se presentan correctamente como correspondencias estructurales provisionales, no como equivalencias clínicas.

## 11. Ataque I — Cierre semántico de `G2-S2`

Auditar las nueve preguntas `SEM-CTX-005`, `SEM-HUE-005` y `SEM-MOD-001`–`007`.

Para cada una, comprobar:

1. formulación diferenciable;
2. `U` propia posible;
3. exclusión de pruebas, escalas, umbrales, dosis y actuaciones;
4. separación edad/fragilidad, nutrición/reserva, diagnóstico/función y estado inmunológico/viabilidad;
5. ausencia de caso atribuible o metadato clínico;
6. ausencia de atomicidad prematura.

Intentar falsar al menos `SEM-HUE-005` como compuesto oculto de cantidad, función, trayectoria y causa, y `SEM-MOD-006/007` como fusión de nutrición y fragilidad. La vigilancia explícita puede ser resultado correcto; no exigir una adjudicación reservada a fases posteriores.

## 12. Ataque J — IA, reproducibilidad, privacidad y no avance

Comprobar que:

- la IA no inventa parámetros ni cierra `U`;
- la cadena de procedencia precede a la conclusión;
- misma entrada, corpus y versiones exigen reproducción byte a byte;
- un fallo técnico no genera una salida alternativa;
- los objetos son impersonales y no contienen episodios, centros o personas;
- no se modifica el Lenguaje SV;
- no se constituyen observables, consecuencias clínicas, matrices, rutas o frames;
- no se abre `G3-OBS` ni `G5-ATM` por el solo hecho de existir este lote.

## 13. Salida obligatoria

Entregar una sola auditoría con:

1. identidad calculada;
2. diff exacto contra la línea base;
3. dictamen `PASA`, `PASA_CON_REPAROS` o `NO_PASA`;
4. tabla de ataques A–J;
5. contraejemplos propios y resultado;
6. reparos numerados con texto, evidencia y corrección mínima;
7. recuentos verificados;
8. incertidumbres residuales legítimas;
9. declaraciones separadas:
   - `NA0_MATH_CERRABLE = SI/NO`;
   - `Q0_INTEGRIDAD_PASA = SI/NO`;
   - `G2_S2_CERRABLE = SI/NO`;
   - `G3_OBS_APTA_PARA_APERTURA = SI/NO`.

`G3_OBS_APTA_PARA_APERTURA = SI` sólo significa que el siguiente lote acotado puede comenzar tras decisión de continuidad. No constituye observables ni autoriza asistencia.

## 14. Límites

- No escribir ni corregir el repositorio.
- No crear PR ni tocar `main`.
- No buscar cohortes, repositorios o guías de enfermedad.
- No proponer matrices definitivas ni tamaños.
- No adjudicar las 32 preguntas como átomos.
- No modificar el Lenguaje SV.
- No usar la adversarial interna como sustituto de pruebas propias.
- No añadir estado del arte, arquitectura lateral o prosa promocional.

