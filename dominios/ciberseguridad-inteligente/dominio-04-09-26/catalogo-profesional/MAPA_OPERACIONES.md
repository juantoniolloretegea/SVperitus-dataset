# Mapa finito de operaciones candidatas

**Corte:** 08-09-2026. **Estado:** 22 operaciones cartografiadas; cero universos constituidos en este corte. El detalle principal está en `07_Operaciones` del [libro Excel](CATALOGO_PROFESIONAL.xlsx).

La identidad candidata se examina como **(producto, objeto/sujeto, desencadenante, autoridad, frontera, terminación)**. Los roles, conocimientos, temarios y controles son aportaciones; no se convierten en universos por fila. Las seis dimensiones están declaradas para cada candidato en el libro. Los vínculos son de pertinencia primaria, no promesa de que una sola operación cubra todo el rol. Una diferencia material posterior puede exigir separar una variante antes de constituirla.

| ID candidato | Producto | Fundamento de procedencia |
|---|---|---|
| OPC-01 | Expediente de riesgo y plan de tratamiento | OG-WRL-002;OG-WRL-007;T1586 |
| OPC-02 | Dictamen de arquitectura y requisitos de seguridad | DD-WRL-001;DD-WRL-006 |
| OPC-03 | Expediente de autorización de acceso | NF-COM-001;T1548 |
| OPC-04 | Informe de evaluación técnica de seguridad | PD-WRL-007;DD-WRL-007;T1625 |
| OPC-05 | Dictamen de seguridad de una entrega de software o modelo | DD-WRL-003;DD-WRL-005;NF-COM-008 |
| OPC-06 | Evaluación de proveedor, componente o servicio externo | OG-WRL-017;NF-COM-004;T2056 |
| OPC-07 | Informe de triaje de una alerta con apoyo de IA | PD-WRL-001;IO-WRL-001;S0957 |
| OPC-08 | Informe de inteligencia de amenazas | PD-WRL-006;PD-WRL-005;K1333 |
| OPC-09 | Plan de respuesta a incidente para decisión autorizada | PD-WRL-003;T0510;T2067 |
| OPC-10 | Informe forense y expediente de evidencia | IN-WRL-002;PD-WRL-002;T1510 |
| OPC-11 | Informe de preparación o prueba de recuperación | NF-COM-007;T1126;T1150 |
| OPC-12 | Expediente de configuración y mantenimiento seguro | IO-WRL-005;NF-COM-003;T0084 |
| OPC-13 | Dictamen de protección criptográfica y comunicaciones | NF-COM-006;OG-WRL-001;NF-COM-005 |
| OPC-14 | Dictamen de seguridad de cambio en entorno OT | DD-WRL-009;NF-COM-010;T1020 |
| OPC-15 | Evaluación de idoneidad y seguridad de un uso de IA | NF-COM-002;K1341;S0955 |
| OPC-16 | Informe de evaluación o auditoría de controles | OG-WRL-012;OG-WRL-016;T0274 |
| OPC-17 | Dictamen de aplicabilidad jurídica y privacidad | OG-WRL-006;OG-WRL-008;T0220 |
| OPC-18 | Dictamen de diseño o revisión de programa formativo | OG-WRL-003;OG-WRL-004;T0101 |
| OPC-19 | Resultado de investigación o conocimiento técnico validable | DD-WRL-008;IO-WRL-003 |
| OPC-20 | Expediente de investigación de ciberdelito | IN-WRL-001;T1175 |
| OPC-21 | Expediente de autorización para operar un sistema | OG-WRL-013;OG-WRL-007 |
| OPC-22 | Informe de una actividad formativa y su evaluación | OG-WRL-005;OG-WRL-004 |

## Fusiones y separaciones justificadas

Arquitectura empresarial y arquitectura de seguridad pueden aportar al mismo dictamen de requisitos cuando comparten objeto, encargo y destino; sus roles no se declaran equivalentes. Roles defensivos y análisis de datos confluyen en un informe de triaje. Desarrollo seguro y evaluación de software confluyen en el dictamen de una entrega, conservando independencia y responsabilidades cuando el encargo la exija. El carácter distribuido o de nube es una variante sólo mientras no cambie la identidad de la operación.

Se separan triaje (OPC-07), inteligencia (OPC-08), plan de respuesta (OPC-09) y análisis forense (OPC-10): producto, desencadenante, mandato y término difieren. El plan no ejecuta contención. La investigación de ciberdelito (OPC-20) se distingue de forense interno por finalidad y autoridad jurídica. OT (OPC-14) explicita la frontera física y la autoridad de operación de planta.

El adversarial corrigió dos fusiones: OPC-03 trata acceso individual; OPC-21 autorización institucional para operar un sistema. OPC-18 diseña o revisa un programa; OPC-22 documenta una actividad realizada y su evaluación. Sus productos no se reemplazan por un rótulo amplio. OPC-11 sólo informa preparación/prueba de recuperación: la puesta en servicio efectiva exigiría un contrato y autoridad propios. OPC-16 no es certificación acreditada. OPC-15 conserva separados el juicio de utilidad del uso de IA y el de su seguridad dentro del expediente.

## Propuesta motivada para la decisión constitutiva

Se propone priorizar **OPC-07: informe de triaje de una alerta con apoyo de IA**, después de revisar y adoptar el perímetro correspondiente. Es propuesta, no selección humana ya efectuada, ni identificador definitivo de universo.

Su anclaje profesional combina PD-WRL-001 e IO-WRL-001, la competencia de identificar errores de salidas de IA S0957 y los sesgos K0658/S0443. Las subcategorías DE.AE-03/04/06/08 y RS.MA-02 de SP 800-61 Rev. 3 aportan correlación, alcance, distribución autorizada, criterios de declaración y validación inicial. AI RMF y los TKS de evaluación exigen que el apoyo de IA sea evaluable y revisable. Estas referencias se conservan en el catálogo, no se convierten todavía en reglas SV.

| Alternativa considerada | Valor para el contraste | Razón para no priorizarla en este primer recorrido |
|---|---|---|
| OPC-04, evaluación técnica autorizada | Alcance, permisos, vulnerabilidades y evidencia | Requiere concretar laboratorio y reglas de intervención; introduce efectos técnicos adicionales. |
| OPC-10, informe forense | Integridad, transformaciones, identidad de evidencia | Excelente segunda candidata; la IA no es necesaria en todo encargo y habría que justificar su aportación específica. |
| OPC-15, evaluación de uso de IA | Validez, seguridad, sesgo y supervisión | Abarca dos juicios amplios y un ciclo de evaluación que conviene acotar antes de constituirlo. |
| OPC-07, triaje asistido | Evidencia capturada, inferencia, incertidumbre, revisión humana y escalado | Producto finito y profesional; permite examinar IA sin atribuirle autoridad ni ejecutar respuesta. |

La propuesta se apoya en esas necesidades profesionales, no en comodidad de LIG ni en preferencia anticipada por un SOC. Admite un corpus sintético o público controlado y un producto finito sin acceder a objetivos reales. Todavía no se han creado alertas, datos operativos ni umbrales.

## Recorrido que deberá constituirse después de la selección

Se conserva la secuencia reconciliada de Inmunología: G0-PRO → G1-OP → G2-SEM → G3-OBS → G4-CON → G5-ATM → G6-MAT → G7-RUT → G8-ITI → G9-EMP → G10-SV. Semántica profesional, observabilidad y consecuencias se justifican antes de atomización y matriz. No se importan sus cuentas, parámetros clínicos, rutas ni geometría. El cierre de un universo no cubre los otros candidatos.

Para OPC-07 se deberá delimitar alerta, activo, ventana temporal, finalidad, destinatario, autoridad y condiciones de terminación; fijar significado profesional y evidencia observable; distinguir dato capturado, inferencia analítica y propuesta de IA; y definir qué decisión queda pendiente cuando falte evidencia. Sólo después se constituirán unidades, parámetros, matriz, rutas, itinerarios y testigos.

El contraste deberá incluir, si se admite esa operación, pares que cambien exclusivamente identidad o versión de evidencia; permiso o destinatario; dato ausente frente a fallo de adquisición; salida de IA frente a observación; actualización externa de referencia; y vigencia del contexto. Se fijarán resultados esperados antes de evaluar. Se probará sensibilidad del observador con alteraciones que sí deban producir diferencias; no se presumirá independencia semántica por usar otro serializador.

Se confrontarán los límites recibidos del Lenguaje, incluido el contrato numérico específico de `documentary_json`: preservar bytes antes de conversión; no pasar primero por coma flotante. No se declara una limitación global de todos los números del Lenguaje. Este expediente no introduce tipos o interfaces paralelos.

Son resultados legítimos del futuro contraste: pérdida demostrada, suficiencia acreditada en alcance declarado o contraste no concluyente. No se abrirá automáticamente otro universo ni se buscarán fallos hasta obtener uno. **Aquí no se afirma ninguno de esos resultados: aún no se ejecutó el contraste del universo.**
