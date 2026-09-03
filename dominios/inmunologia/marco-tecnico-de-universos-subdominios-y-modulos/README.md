# Marco técnico de universos, subdominios y módulos de Inmunología

## 1. Finalidad

Esta carpeta reúne, de forma incremental, las condiciones técnicas y de responsabilidad que debe satisfacer cada universo clínico constituido en el dominio de Inmunología. Su finalidad es impedir que una salida clínica, una opinión o un consejo atribuible al sistema proceda de una transformación opaca, irreproducible o no autorizada.

Este marco no sustituye la documentación clínica de cada universo, no contiene reglas clínicas generales y no declara conformidad con norma alguna. Es un índice y un régimen de separación: cada universo dispone de su propio perfil técnico, cuya aplicabilidad debe demostrarse de manera independiente.

## 2. Términos

- **Universo:** operación clínica delimitada por una finalidad prevista, una población, un tiempo de referencia, unas exclusiones y un producto de salida determinados. Es la unidad de evaluación y de autorización.
- **Subdominio:** agrupación ordenadora de universos relacionados. No ejecuta reglas ni transmite autoridad clínica.
- **Módulo:** componente técnico que representa, transforma o presenta información. No adquiere autoridad clínica por pertenecer a un universo o subdominio.

Estos términos no son intercambiables.

## 3. Regla de no herencia

Ninguna regla, fuente, configuración, conclusión, autorización, criticidad o prueba se hereda automáticamente entre universos. La reutilización exige una referencia exacta y versionada, una justificación de aplicabilidad al nuevo universo y evidencia propia de conformidad. La semejanza clínica, el uso anterior o la pertenencia al mismo subdominio no bastan.

El documento raíz no puede convertirse en una norma clínica general encubierta. Toda exigencia que dependa de la finalidad, el riesgo, la jurisdicción o el curso clínico debe quedar adjudicada dentro del perfil del universo correspondiente.

## 4. Estados admitidos

| Estado | Significado |
|---|---|
| `APLICABLE_Y_DEMOSTRADO` | Existe evidencia identificada y reproducible de cumplimiento en la versión indicada. |
| `APLICABLE_PENDIENTE` | La exigencia corresponde al universo, pero todavía no se ha demostrado. |
| `NO_APLICABLE_JUSTIFICADO` | La exclusión está razonada, versionada y aprobada por la autoridad competente. |
| `PROHIBIDO` | El uso o la transformación no están permitidos. |
| `EJECUCION_TECNICA_NO_VALIDA` | No se cumplen las condiciones técnicas necesarias; no puede emitirse estado, opinión ni consejo clínicos. |

La ausencia de evidencia nunca equivale a `APLICABLE_Y_DEMOSTRADO`.

## 5. Garantía adversarial constitutiva

Antes de abrir este marco se atacó su lógica mediante doce contraejemplos: herencia general encubierta; duplicación documental; ambigüedad de «misma entrada»; degradación por indisponibilidad; traslado indebido de responsabilidad; certificación inferida por cita normativa; prosa generativa variable; actualización silenciosa de fuentes; criticidad fija aplicada por analogía; confusión entre subconjunto formalizado y cribado completo; exposición de datos personales; y proliferación burocrática.

El diseño **pasa con condiciones vinculantes**, incorporadas en los apartados anteriores y en el perfil de `OP-IMM-001`: identidad completa de ejecución; igualdad exacta de salida; fallo cerrado sin resultado clínico; responsabilidades separadas; prohibición de inferir conformidad; control de versiones; criticidad contextual no inventada; protección de datos; y un único perfil técnico por universo salvo cambio material. Si cualquiera de estas condiciones deja de cumplirse, el marco no pasa y la ejecución afectada es inválida.

No se crea un expediente independiente para auditar esta garantía ni una recepción de la auditoría. Sólo un cambio material puede justificar documentación adicional.

## 6. Índice de universos

| Universo | Denominación | Perfil técnico | Estado de uso clínico |
|---|---|---|---|
| `OP-IMM-001 / Q0 v0` | Información predecisional pertinente antes de iniciar tratamiento inmunosupresor en adultos | [01-op-imm-001-informacion-preinmunosupresion-adultos](01-op-imm-001-informacion-preinmunosupresion-adultos/) | `PROHIBIDO` con datos reales; validación y configuraciones pendientes |

## 7. Economía documental

Cada universo tendrá, por defecto, un índice breve y un solo perfil técnico de responsabilidad, trazabilidad, reproducibilidad y criticidad. La documentación clínica permanece en su ubicación canónica y se enlaza, no se copia. No se autoriza una cadena de manifiestos, adendas, recepciones o auditorías cuya única función sea confirmar documentos anteriores.
