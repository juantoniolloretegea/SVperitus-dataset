# Auditoría — Catálogo profesional atómico INMUNO v0.2

Corte: 01-09-2026. Archivo leído:  
`03-base-documental-candidata/04-planes-profesionales-en-evaluacion/Catalogo_profesional_atomico_INMUNO_v0.2_2026-09-01.xlsx`  
SHA blob GitHub `5ba1bd07`. No adopción. No entra en watson-biblioteca.

## Conteos (hoja vs fila de datos)

| Objeto | Declara 00_Estatuto | Contado en hojas |
|---|---|---|
| Capacidades | 14 (6+8) | 14 |
| Unidades | 123 (43+80) | 123; IDs únicos; 0 huérfanas vs 04 |
| Contextos §3.4 | 174 | 174; 7 áreas; todos UK |
| Procedimientos | 11; 55 progresión | 11 y 55 (11×ST3–ST7) |
| Progresión S-CIP | — | 40 (8×5) |
| Pruebas | 14 | 14 (T-01–T-14) |
| Fronteras | — | 12 |
| Consecuencias constituidas | 0 | 123/123 `PENDIENTE_EVIDENCIA_CLÍNICA` |
| Parámetros SV | 0 | 0 |

v0.1 era 14 / 80 / 8 / 10 / 12 / 12. Lo nuevo material: 43 descriptores genéricos (cierra el hueco A-01 de v0.1), 174 contextos no atomizados, 11 procedimientos con autonomía por etapa, 14 pruebas.

## Lo que resiste
- Estatuto: `CANDIDATA_NO_ADOPTADA`. Jurisdicción Reino Unido. Lenguaje SV no tocado.
- 80 especializadas + 43 genéricas; relación 1:1 unidad–capacidad; sin IDs duplicados.
- §3.4 tipado como contexto (`CONTEXTO_CURRICULAR_NO_DIAGNÓSTICO`), no diagnóstico ni parámetro.
- 8 grupos DUP-01…08 / 16 unidades: no fusionados.
- Autonomía de procedimiento no es constante: AUTÓNOMO 11 / SUPERVISADO 18 / MANTENER 26.
- T-09 = casos críticos ST4–ST7 (ST3 vacío). ALS, Patient Survey, TO presentes.
- Consecuencias 0. Interoperabilidad bloqueada. Cuarentena v0.2 parámetros/entidades.

## Lo que no pasa o queda abierto
1. **Canon ES ausente.** Fuentes primarias = solo UK-ACLI-2021 y UK-ACLI-ARCP-2025. SCO/3255 y SCO/3081 no están en `01_Fuentes`. El acta de rumbo pedía BOE primero. ACLI sigue siendo columna vertebral candidata UK, no capa 1 ES.
2. **`Fuente_ID` inconsistente** en `04_Cap_Unidad`: `UK-ACLI-CURR-2021` (heredadas v0.1) vs `UK-ACLI-2021` (definida en `01_Fuentes`). No rompe filas; sí rompe join.
3. **A-14 ABIERTO_CONTROLADO:** transcripción literal y adjudicación clínica pendientes. El libro no puede fingir cierre semántico.
4. **174 contextos** cubren 7 áreas ACLI (alergia, ID, lab, enlace, terapéutica, urgencias). No son el mapa de familias del dominio ES. Inventario ≠ atomización.
5. Crecer la biblioteca central desde este catálogo exige autorización; este archivo no es alta bibliográfica.

## Veredicto
Resiste como corrección estructural de v0.1 (genéricas, procedimientos, pruebas, no fusión).  
Colapsa como perímetro profesional ES y como constitución de consecuencias.  
Sigue `CANDIDATA_NO_ADOPTADA`.
