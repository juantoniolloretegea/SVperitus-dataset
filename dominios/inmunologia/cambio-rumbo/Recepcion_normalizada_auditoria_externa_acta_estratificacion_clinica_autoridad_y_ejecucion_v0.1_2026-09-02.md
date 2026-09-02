# Recepción normalizada de auditoría externa · acta de estratificación clínica, autoridad y ejecución computacional v0.1

- **Fecha:** 02-09-2026
- **Línea base:** `88445856dd2eb13b20975696f6151e6e4d9340f8`
- **Commit material auditado:** `ea18d5c7f9ecd51d17027d44f1cf281a1627b612`
- **Dictamen externo recibido:** `PASA`
- **Reparos del acta:** ninguno
- **Estatuto resultante:** `ACTA_RECTOR_CERRADA_TRAS_AUDITORIA_EXTERNA`
- **Privacidad de esta recepción:** `PRIVACIDAD_PASA`

## 1. Identidad y regresión aceptadas

La auditoría externa reprodujo las identidades declaradas:

| Objeto | Bytes | SHA-256 |
|---|---:|---|
| acta de estratificación | 16 424 | `20a586fd96b6074e27bf34fbb087f35b8b27e2048686aafdb5be8285ffccd318` |
| adversarial interna | 6 994 | `255e9d52961020251d340051d52ba4b76034dae00579aa645e4242be14ddfaf1` |
| README rector | 13 360 | `fd2a252c12815f2955ca6afebc42f6b735229d79a19fbd82a523815b6bf43a04` |

La regresión contra la línea base quedó confinada a:

- adición del acta;
- adición de su adversarial interna;
- actualización del README rector.

No se modificaron catálogos, hojas de cálculo, lotes `G2-S1` o `G2-S2`, política de protección, pilotos, Instrucción Técnica de Implementación, Lenguaje SV ni otros objetos del dominio.

## 2. Resultado de los ataques A–N

| Ataque | Resultado | Efecto aceptado |
|---|---|---|
| A · identidad y regresión | `PASA` | objeto exacto y cambio confinado |
| B · separación de capas | `PASA` | las cinco capas tienen contenido y límites diferenciados |
| C · exactitud y exhaustividad | `PASA` | exactitud relativa al corte sin pretensión de verdad clínica completa |
| D · customización | `PASA` | configuración institucional e instanciación del episodio no reescriben el núcleo |
| E · inversión por ingeniería | `PASA` | la implementación carece de autoridad clínica y semántica |
| F · autoridad técnica | `PASA` | puede bloquear una ejecución insegura sin decidir clínicamente |
| G · inteligencia artificial | `PASA` | ejecución subordinada, sin inferencia o adopción autónomas |
| H · configuración institucional | `PASA` | necesidad clínica y viabilidad local permanecen separadas |
| I · episodio y participación | `PASA` | participación pertinente sin indicación automática |
| J · costes y recursos | `PASA` | informan viabilidad sin compensar vetos clínicos |
| K · carga cognitiva | `PASA` | retaguardia, prioridad crítica y divulgación progresiva |
| L · privacidad y ejemplos | `PASA` | episodio, núcleo y fuentes de ejemplos permanecen separados |
| M · experiencia y revisión | `PASA` | la experiencia origina preguntas, pero no autoridad universal |
| N · consistencia y no avance | `PASA` | no crea objetos posteriores ni abre `G3-OBS` |

La regla de suficiencia se cumplió: el informe declara un contraejemplo material para cada ataque B–M y concluye que todos quedan absorbidos por articulado expreso.

## 3. Normalización de la recepción

La respuesta externa no se incorpora de manera literal. Se preserva su contenido técnico mediante esta recepción impersonal y se corrigen tres extremos que no afectan al dictamen sobre el acta:

1. Las cinco capas arquitectónicas y los seis planos de autoridad son clasificaciones complementarias. No se registran como una única partición de once objetos ni se presume que todos sus elementos sean disjuntos entre sí.
2. La participación y las preferencias clínicamente pertinentes se sostienen en §5.2. `INV-07` gobierna la visibilidad y no compensabilidad de una `U` crítica; no constituye la referencia de la participación.
3. El contraejemplo del ataque M se formula de manera general e impersonal, conforme a la política transversal de protección y no atribución.

Estas normalizaciones reparan la recepción del informe, no el acta auditada. No crean un reparo material ni rebajan el dictamen `PASA`.

## 4. Autoridades preservadas

### 4.1. Autoridad clínica

La decisión asistencial permanece en el profesional autorizado. La salida computacional puede aceptarse, rechazarse, completarse o ser objeto de apartamiento clínicamente motivado y trazable. La participación de la persona atendida se conserva sin transformarse en indicación automática.

### 4.2. Autoridad técnica

La ingeniería conserva responsabilidad sobre representabilidad, corrección, verificabilidad y seguridad. Puede bloquear una implementación inadecuada, pero ese bloqueo no resuelve el fondo clínico ni permite reescribir el requisito.

### 4.3. Ejecución computacional

La inteligencia artificial no adquiere autoridad clínica o semántica. Sus funciones permanecen limitadas al contrato vigente: cálculo, recuperación autorizada, presentación, registro, abstención y escalado.

## 5. Vigilancias adoptadas

Se conservan para las fases correspondientes:

| ID | Puerta o entrega | Ataque futuro obligatorio |
|---|---|---|
| `VIG-ARQ-01` | `G3-OBS` | impedir que un observable dependa exclusivamente de la disponibilidad de un centro |
| `VIG-ARQ-02` | clasificación matricial | impedir que la dimensión nazca de una preferencia de interfaz o almacenamiento |
| `VIG-ARQ-03` | rutas críticas | separar veto clínico, bloqueo técnico y restricción institucional |
| `VIG-ARQ-04` | entrega al Lenguaje SV | demostrar preservación semántica extremo a extremo |
| `VIG-ARQ-05` | interfaz | medir carga cognitiva y evitar divulgación masiva por defecto |

No son defectos de la versión 0.1 ni autorizan a constituir anticipadamente sus objetos.

## 6. Cierre y continuación

Queda cerrado el acta con estatuto rector para `G2-SEM` y las fases posteriores.

Este cierre:

- no añade preguntas a `G2-S1` o `G2-S2`;
- no cierra el conjunto total de `G2-SEM`;
- no constituye observables, parámetros, umbrales, ventanas, matrices, rutas o frames;
- no abre `G3-OBS`;
- no modifica el Lenguaje SV;
- y no autoriza asistencia clínica.

La continuación inmediata permanece en `G2-S2`, cuyo cierre depende de su propia auditoría externa y no de esta acta.

## 7. Declaración

La auditoría externa confirma que la arquitectura preserva el gobierno clínico, la responsabilidad técnica, la separación institucional, la protección del episodio y la subordinación de la ejecución computacional. El dictamen constituye un cierre metodológico y registral, no una adopción ni autorización clínica.
