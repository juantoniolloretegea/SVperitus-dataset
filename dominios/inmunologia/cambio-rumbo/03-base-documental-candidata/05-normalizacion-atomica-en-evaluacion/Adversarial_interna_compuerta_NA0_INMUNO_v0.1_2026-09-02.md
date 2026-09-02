# Adversarial interna de la compuerta NA0 — INMUNO v0.1

- **Fecha:** 02-09-2026
- **Objeto:** contrato semántico, protocolo transversal y cribado estructural de pilotos
- **Tipo:** control interno reproducible; no sustituye auditoría externa
- **Dictamen interno:** `PASA_PARA_AUDITORIA_EXTERNA`

## 1. Identidad del paquete atacado

| Archivo | SHA-256 |
|---|---|
| `Contrato_semantico_atomo_parametro_matriz_composicion_INMUNO_v0.1_2026-09-02.md` | `38d4e41144e4f2edf63b50e892d93a1d0719ad3abbc4c3c3bfec46e9d77a3ceb` |
| `Protocolo_adversarial_transversal_INMUNO_v0.1_2026-09-02.md` | `b4d96fed4a6a7f026c0fd022a0b281a67e477b24edc58901ea38f678b7e0dfd4` |
| `Cribado_estructural_pilotos_IMMUNO-1_IMMUNO-2_v0.1_2026-09-02.md` | `1ade948a86d3e96f1df743c98d3d1c963535b591df9a62e262f14e03cd83fc8f` |
| `README.md` | `e1b44ad56e879890c409ac10e9c97a19cc3f4eaed86a2786494caff78f1770cc` |

## 2. Ataques ejecutados

| Ataque | Evidencia | Resultado |
|---|---|---|
| Identidad de base | v0.8 conserva SHA-256 `d9535ac9…a68a`; recepción externa `PASA` registrada | PASA |
| Exhaustividad del cribado histórico | 25 entradas YAML y 25 funciones `Pxx` en cada piloto; secuencias P01–P25 completas | PASA |
| Recuento de campos | análisis de sintaxis de ambos motores: 19 funciones con una clave `_get` y 31 con varias | PASA |
| Correspondencia del inventario | 50 filas materiales: 25 `IMMUNO-1` y 25 `IMMUNO-2` | PASA |
| Falsa equivalencia campo–átomo | el contrato declara que una entrada simple no prueba atomicidad y una regla multiobservable no prueba composición | PASA |
| Conveniencia dimensional | `IMMUNO-2/P02` y `T(25)=19` quedan expresamente no ratificados | PASA |
| Puente oculto | `IMMUNO-2/P25` queda identificado como puente derivado | PASA |
| Colisiones | ocho familias interpiloto quedan abiertas a adjudicación, no fusionadas automáticamente | PASA |
| Compensación clínica | el protocolo exige prueba de veto y prohíbe compensar riesgo crítico con mayoría, coste o conveniencia | PASA |
| U crítica | preservación o abstención/escalado; nunca cierre favorable por mayoría | PASA |
| Autoexención | el protocolo incluye meta-adversarial y no puede declararse aprobado por su diseñador | PASA |
| Invasión técnica | cero cambios en motores, YAML, compositor o archivos del Lenguaje SV | PASA |
| Integridad Python | ambos motores históricos compilan sin error; no se interpreta esto como validación clínica | PASA |
| Higiene de parche | `git diff --check` sin errores | PASA |

## 3. Hallazgos adversariales reales

La prueba no fue decorativa. Constituyó los siguientes riesgos:

1. los 50 nombres históricos no son 50 átomos demostrados;
2. `IMMUNO-2/P02` reconoce una agregación por economía de posiciones;
3. `IMMUNO-2/P24` muestra que una sola clave informática puede ocultar una evaluación compuesta;
4. `IMMUNO-2/P25` no debe competir como dato basal con parámetros clínicos;
5. hay ocho familias de posible duplicación o proyección entre fases;
6. la pre-ITI recibida repite `IMMUNO-1/P11` en su tabla de síntesis;
7. el umbral de predominio puede compensar indebidamente un veto o una `U` crítica.

Estos hallazgos no invalidan los pilotos en su estatuto histórico. Impiden heredarlos sin adjudicación.

## 4. Incertidumbres que la unidad interna no puede cerrar

| U | Causa | Cierre exigido |
|---|---|---|
| `U-NA0-01` | la definición de atomicidad es una decisión metodológica nueva | auditoría externa del contrato y búsqueda de contraejemplos |
| `U-NA0-02` | las alertas estructurales no prueban la descomposición clínica correcta | adjudicación operación por operación con fuentes y consecuencias |
| `U-NA0-03` | no se ha demostrado todavía qué operación clínica debe actuar como primer testigo | decisión expresa tras superar NA0 |
| `U-NA0-04` | no se ha evaluado la representabilidad concreta de parámetros futuros en Gramática 0.2 e IR 0.3 | compuerta G9 posterior, sin escritura en el lenguaje |

## 5. Reparaciones realizadas antes del dictamen

- Se incorporó un meta-ataque al protocolo para impedir su autoexención.
- Se añadieron glosarios de continuidad para acrónimos y términos recurrentes.
- Se corrigió el índice del directorio para registrar la recepción externa de v0.8 y la nueva compuerta.

## 6. Dictamen

`PASA_PARA_AUDITORIA_EXTERNA` significa únicamente que el paquete es coherente y reproducible para ser atacado por otra unidad. `NA0` permanece abierta y sus definiciones no gobiernan la normalización hasta dictamen externo favorable.

No constituye parámetros clínicos, consecuencias, matrices, rutas, umbrales ni autorización asistencial.
