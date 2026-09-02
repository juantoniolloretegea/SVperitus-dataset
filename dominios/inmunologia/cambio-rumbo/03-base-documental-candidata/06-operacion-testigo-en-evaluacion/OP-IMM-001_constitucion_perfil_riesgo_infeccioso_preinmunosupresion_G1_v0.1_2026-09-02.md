# OP-IMM-001 · Constitución del perfil de riesgo infeccioso previo a inmunosupresión sistémica

- **Fecha:** 02-09-2026
- **Puerta:** `G1-OP`
- **Estatuto:** `CANDIDATA_PARA_AUDITORIA_EXTERNA`
- **Base metodológica:** contrato semántico y protocolo adversarial INMUNO v0.2
- **Base profesional:** catálogo profesional INMUNO v0.8

## 1. Formulación canónica candidata

**Constituir y documentar, para un paciente adulto real y antes del inicio propuesto de un tratamiento inmunosupresor farmacológico sistémico fuera del trasplante, el perfil de riesgo infeccioso inmunológicamente relevante que el médico autorizado necesita para su decisión, preservando toda incertidumbre crítica y sin emitir por el sistema la decisión terapéutica.**

La operación pregunta:

> ¿Está suficientemente caracterizado y trazado el perfil de riesgo infeccioso pertinente para esta decisión médica concreta, o permanece una incertidumbre que impide su cierre legítimo?

## 2. Sujeto, población y ámbito

- **Sujeto:** un paciente individual, no una cohorte ni un paciente promedio.
- **Edad:** adulto, definido para esta operación piloto como 18 años o más.
- **Situación:** existe una propuesta clínica documentada de iniciar inmunosupresión farmacológica sistémica.
- **Ámbito positivo:** factores inmunológicos, farmacológicos, infecciosos y preventivos pertinentes para caracterizar el riesgo asociado a esa propuesta.
- **Ámbito negativo:** trasplante de órgano sólido, trasplante de progenitores hematopoyéticos, terapia con células CAR-T, quimioterapia citotóxica de neoplasia hematológica como régimen principal y población pediátrica.

La delimitación es propia de la operación testigo. No declara que las exclusiones queden fuera del dominio internacional de inmunología; exige operaciones distintas.

## 3. Inicio y final operacional

### Inicio

La operación comienza cuando concurren:

1. paciente individual identificable dentro del sistema asistencial autorizado;
2. propuesta real de inicio de inmunosupresión farmacológica sistémica;
3. solicitud de valoración por la autoridad clínica competente;
4. versión de reglas y fuentes fijada para el episodio.

### Final

La operación termina únicamente en uno de estos estados estructurales:

| Estado | Significado |
|---|---|
| `PERFIL_PREDECISIONAL_SELLADO` | el médico autorizado confirma que el expediente presenta los elementos pertinentes, sus fuentes, temporalidad e incertidumbres; no significa que el tratamiento sea seguro, indicado o autorizado |
| `U_CRITICA_NO_CERRADA` | falta o conflicto relevante que no puede resolverse dentro del episodio y debe conservarse |
| `FUERA_DE_ALCANCE` | el paciente, tratamiento o problema exige otra operación |
| `ABSTENERSE_O_ESCALAR` | no existe cierre gobernado y la regla autorizada exige detener o elevar el caso |

No existe salida automática `APTO`, `NO_APTO`, `INICIAR` o `NO_INICIAR`.

## 4. Horizonte temporal

El horizonte común es el episodio predecisional que precede al inicio propuesto. Comienza con el suceso descrito en el apartado 3 y termina con el sellado humano, la preservación de `U`, la salida por alcance o la abstención/escalado.

Cada observable futuro conservará su propia ventana de validez clínica según fuente y regla. Esta operación no inventa una única antigüedad válida para analítica, tratamiento, antecedente, exposición o vacunación.

El seguimiento posterior al inicio constituye otra operación. No se absorbe aquí.

## 5. Autoridad

- La autoridad para cerrar el expediente predecisional y adoptar la decisión terapéutica es el médico habilitado conforme a la jurisdicción y al episodio.
- El especialista de laboratorio interpreta y aporta información dentro de su ámbito profesional; esa contribución no se presenta como prescripción autónoma cuando la jurisdicción no la autoriza.
- La inteligencia artificial ordena, verifica trazas, señala ausencias y presenta el frame; no asigna autoridad clínica ni decide el tratamiento.
- El Director constituye el dominio y sus reglas documentales; no sustituye la decisión del médico responsable del paciente.

## 6. Familias preliminares de información

La operación permite explorar en `G2-SEM`, sin convertirlas todavía en parámetros o matrices:

1. estado inmunitario pertinente;
2. exposición farmacológica propuesta;
3. antecedentes infecciosos y colonización;
4. barreras, dispositivos y exposiciones epidemiológicas;
5. estado de protección y evaluaciones preventivas;
6. elementos que obliguen a preservar `U`, abstenerse o escalar.

La lista orienta la búsqueda semántica. No es exhaustiva, no impone seis matrices y no hereda las cinco capas de los pilotos.

## 7. Exclusiones funcionales

Esta operación no:

- diagnostica ni trata una infección activa;
- elige, prescribe, modifica o suspende el inmunosupresor;
- prescribe vacunas, profilaxis antimicrobiana o pruebas;
- decide prioridad administrativa, financiación, cama o recurso;
- ejecuta seguimiento longitudinal tras iniciar el tratamiento;
- calcula probabilidad individual de infección;
- aplica `T(25)=19` ni otro umbral global;
- hereda los 50 `Pxx` de `IMMUNO-1` y `IMMUNO-2`;
- forma una matriz;
- consulta cohortes;
- ni modifica el Lenguaje SV.

Una sospecha de infección activa puede aparecer como señal de salida, pero su resolución pertenece a otra operación clínica.

La operación sí puede identificar y trazar una necesidad de información todavía no satisfecha. Esa señal no equivale a seleccionar, indicar ni ordenar la prueba con la que pudiera resolverse: tal decisión permanece en la autoridad clínica competente y exige su regla propia.

## 8. Fundamento profesional dentro del catálogo v0.8

| Registro | Aporte a la operación | Límite preservado |
|---|---|---|
| `ES-INM-ROL-003` | interpretación de datos de laboratorio en contexto clínico y contribución a decisiones | interpretar no equivale a acto médico autónomo |
| `ES-INM-ROL-006` y `ES-INM-ROL-007` | diagnóstico, tratamiento y asistencia directa reservados a la función médica | no trasladar autoridad asistencial a otras titulaciones |
| `ES-INM-CONT-044` | conocimiento de inmunosupresión terapéutica | conocimiento no constituye decisión |
| `ES-INM-CONT-049` | inmunoglobulinas y respuesta a vacunas | la prueba no es automáticamente parámetro |
| `ES-INM-CONT-075` | monitorización de niveles de inmunosupresores | pertenece sólo si responde a la operación y al fármaco |
| `ES-INM-CONT-089` | administración y seguimiento de terapias inmunosupresoras | esta operación se limita al episodio previo al inicio |
| `CTX-A3-C06`, `CTX-A3-C07` | neoplasia, inmunodeficiencia, inmunosupresión y complicaciones | contexto curricular, no diagnóstico ni parámetro |
| `CTX-A4-P05`, `CTX-A4-P06` | inmunosupresores y profilaxis antimicrobiana como situaciones profesionales | no prescribir en G1 |
| `AUNZ-G05`, `AUNZ-G10`, `AUNZ-G11` | razonamiento, prescripción e investigaciones como operaciones distintas | no fusionarlas dentro del perfil |
| `AUNZ-G08` | atención longitudinal | se difiere a otra operación |
| `AUNZ-KG-01`, `AUNZ-KG-06` | diagnóstico/terapéutica y vacunación como familias de conocimiento | las guías son no exhaustivas |
| `CA-SCP-07`, `CA-SCP-09`, `CA-SCP-10` | infección, terapéutica, seguridad, seguimiento y daño | separa conocimiento, actuación y control |
| `CA-OP-07` a `CA-OP-10` | planificación, consentimiento, priorización y seguimiento diferenciados | esta operación no los colapsa |

Los localizadores y fuentes primarias permanecen en el catálogo y sus hojas de trazabilidad. Esta operación no reconstruye una autoridad nueva a partir de las paráfrasis.

## 9. Contrato de salida para la fase siguiente

Si `G1-OP` supera auditoría externa, `G2-SEM` podrá formular preguntas candidatas únicamente cuando demuestre su dependencia respecto de `OP-IMM-001`.

Cada pregunta deberá responder:

1. qué parte del perfil caracteriza;
2. por qué puede cambiar la lectura médica;
3. qué observable podría sostenerla;
4. qué `U` propia puede aparecer;
5. qué consecuencia ex ante provisional tendría ignorarla;
6. si pertenece a esta operación o a otra.

No se asignarán posiciones de matriz durante `G2-SEM`.

## 10. Declaración

`OP-IMM-001` es una operación testigo candidata de apoyo a la decisión. No es protocolo asistencial, guía de práctica clínica, calculadora de riesgo, autorización terapéutica ni sustituto del juicio médico.

## 11. Glosario de continuidad

| Forma | Significado |
|---|---|
| CAR-T | Linfocitos T modificados con receptor quimérico de antígeno. |
| IA | Inteligencia artificial. |
| SV | Sistema Vectorial SV. |
| U | Estado indeterminado legítimo. |
| `G1-OP` | Puerta de definición de la operación clínica. |
| `G2-SEM` | Puerta de formulación semántica de preguntas candidatas. |
