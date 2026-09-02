# Orden de auditoría externa limitada · cierre profesional INMUNO v0.8

## 1. Objeto exacto

- **Fichero:** `Catalogo_profesional_atomico_INMUNO_v0.8_2026-09-02.xlsx`
- **Ruta:** `dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/04-planes-profesionales-en-evaluacion/`
- **Rama:** `dominio-inmunologia`
- **Bytes esperados:** `170296`
- **SHA-256 esperado:** `d9535ac933ce4eb2e35a5017c7f74f0f4b8b9e8806802b933e050ce603cfa68a`
- **Hojas esperadas:** 37
- **Antecedente de regresión:** `Catalogo_profesional_atomico_INMUNO_v0.7_2026-09-01.xlsx`
- **SHA-256 del antecedente:** `e66d51b2062a9d25dd12864226f6b47731752c6bf2f76b12f38c776f5232d5ea`

Documentos rectores y registrales:

- `acta-secuencia-constitutiva-custodia-rumbo-y-acoplamiento-lenguaje-sv-inmunologia-2026-09-02-v0.1.md`
- `Expediente_adjudicacion_comparada_INMUNO_v0.2_2026-09-02.md`

La auditoría es de sólo lectura. No modificar el libro, el repositorio ni los documentos.

## 2. Alcance exclusivo

Comprobar únicamente que v0.8 registra fielmente:

1. las cinco decisiones del lote A;
2. la preservación de los controles, el residual y los dos bloqueos;
3. el cierre explícito y finito del perímetro profesional suficiente;
4. la ausencia de ampliación hacia consecuencias clínicas, matrices, parámetros, cohortes o Lenguaje SV;
5. la regresión material contra v0.7.

No realizar estado del arte, búsqueda de cohortes, recomendaciones clínicas ni evaluación general del Sistema Vectorial SV.

## 3. Ataque A · identidad

Calcular independientemente:

- nombre;
- bytes;
- SHA-256;
- número y orden de hojas;
- fecha y versión declaradas en `00_Estatuto`.

Si no coincide exactamente con el objeto indicado, detenerse y dictaminar `U_OBJETO_NO_COINCIDENTE`.

## 4. Ataque B · regresión material contra v0.7

Comparar hoja a hoja nombres, rangos usados, valores y fórmulas. Se esperan cambios materiales únicamente en:

- `00_Estatuto`;
- `24_Fuentes_v05`, sólo el título de versión;
- `31_Deltas_v05`;
- `33_Trazabilidad_v05`, sólo el título de versión;
- `34_Cobertura_v05`;
- `35_Adversarial_v05`.

Las otras 31 hojas deben ser materialmente idénticas. Verificar además ausencia de:

- `#REF!`;
- `#DIV/0!`;
- `#VALUE!`;
- `#NAME?`;
- `#N/A`.

Entregar la lista exacta de hojas cambiadas y cualquier diferencia no autorizada.

## 5. Ataque C · adjudicación del lote A

En `31_Deltas_v05`, comprobar literalmente:

| Delta | Decisión exigida |
|---|---|
| `CMP-003` | `ADOPTAR_CORPUS_PROFESIONAL` |
| `CMP-004` | `ADOPTAR_CORPUS_PROFESIONAL` |
| `CMP-006` | `ADOPTAR_CORPUS_PROFESIONAL` |
| `CMP-009` | `ADOPTAR_CORPUS_PROFESIONAL` |
| `CMP-010` | `ADOPTAR_CORPUS_PROFESIONAL` |

Verificar que objeto, efecto, clase, fuente, localizador y modo de trazabilidad de esos cinco registros no hayan cambiado respecto de v0.7.

## 6. Ataque D · no adopción automática del resto

Comprobar que permanecen:

- `CMP-001` = `MANTENER_COMO_EJES`;
- `CMP-002` = `NO_CONVERTIR_ESCALAS`;
- `CMP-005` = `NO_USAR_COMO_MÍNIMO_ABSOLUTO`;
- `CMP-011` = `NO_FUSIONAR_EN_ESPAÑA`;
- `CMP-012` = `NO_GENERALIZAR_A_ESPAÑA`;
- `CMP-013` = `LEER_ANTES_DE_ATOMIZAR`;
- `CMP-007` y `CMP-008` = `BLOQUEADO_HASTA_G3`.

Confirmar el recuento: 5 adoptados, 5 controles, 1 residual y 2 bloqueados.

## 7. Ataque E · perímetro profesional suficiente

Contrastar `00_Estatuto`, `13_Fuentes_v03`, `24_Fuentes_v05` y el expediente v0.2.

El perímetro material debe comprender exclusivamente:

- España: `CURR-ES-INM-001` y `CURR-ES-ALG-001`;
- Reino Unido: `CURR-UK-ACLI-001`, `CURR-UK-ARCP-001`, `CURR-UK-HSST-001` y `CURR-UK-STP-001`;
- Australia–Aotearoa Nueva Zelanda: `CURR-AUNZ-RACP-001` y `CURR-AUNZ-RACP-LTA-001`;
- Canadá: `CURR-CA-RCPSC-001`.

Comprobar que:

1. `CURR-AUNZ-RACP-LTA-2025-OLD` no gobierna;
2. `CURR-CA-RCPSC-PTC-001` es control histórico;
3. `CURR-AUNZ-RCPA-IP-001` permanece identificado, no leído y no atomizado;
4. el residual RCPA no se utiliza para sostener ningún objeto material nuevo;
5. el cierre no declara exhaustividad mundial;
6. una fuente futura exige un suceso prospectivo y no reabre automáticamente el corte.

## 8. Ataque F · trazabilidad

Verificar:

- 150 trazas materiales;
- ninguna traza colgante;
- al menos una traza para cada delta adoptado;
- dos trazas separadas para `CMP-004`, una por cada fuente;
- coincidencia exacta entre `Fuente_ID` y localizador;
- ausencia de cambios materiales en las trazas respecto de v0.7, salvo el título de versión.

## 9. Ataque G · recuentos e invariantes

Verificar:

- 18 metas;
- 15 definiciones de escala;
- 72 exigencias;
- 6 guías;
- 4 instrumentos;
- 10 bloques canadienses;
- 10 operaciones canadienses;
- 13 deltas;
- 6 controles de reutilización;
- 150 trazas;
- consecuencias clínicas constituidas = 0;
- matrices constituidas por este suceso = 0;
- parámetros SV derivados = 0;
- Lenguaje SV no modificado;
- interoperabilidad terminológica no iniciada;
- frontera española entre Inmunología y Alergología preservada;
- ninguna autorización asistencial.

## 10. Ataque H · dependencia empírica y próxima puerta

Comprobar que el catálogo y el expediente declaran sin ambigüedad:

1. la adopción profesional no depende de una validación previa mediante cohortes o microdatos;
2. el contraste empírico se difiere a su fase sistemática;
3. Nor-vaC, OCTAVE, SUCCEED, BIFAP, ImmPort y otros repositorios no intervienen en esta compuerta;
4. no se inicia la normalización atómica hasta dictamen externo favorable.

No juzgar aquí si una cohorte futura apoyará o refutará los objetos.

## 11. Entrega obligatoria

Entregar una sola auditoría con:

1. identidad calculada;
2. dictamen: `PASA`, `PASA_CON_REPAROS`, `NO_PASA` o `U_OBJETO_NO_COINCIDENTE`;
3. tabla de A–H con evidencia concreta;
4. diferencias materiales v0.7→v0.8;
5. recuentos verificados;
6. reparos numerados con hoja, registro, evidencia y corrección mínima;
7. incertidumbres residuales con causa;
8. declaración expresa sobre si queda abierta la fase 2, normalización del universo atómico;
9. declaración expresa de que el dictamen no constituye adopción clínica ni autorización asistencial.

## 12. Límites

- No escribir en GitHub.
- No crear una solicitud de cambios ni fusionar ramas.
- No modificar el XLSX.
- No buscar ni valorar cohortes.
- No constituir consecuencias clínicas.
- No constituir matrices ni parámetros.
- No modificar el Lenguaje SV.
- No convertir el acceso 403 al handbook RCPA en defecto de v0.8: su contenido permanece expresamente fuera del corpus material.
- No reabrir la decisión soberana del lote A salvo evidencia de falsedad registral, fuente inexistente o localizador materialmente incorrecto.
