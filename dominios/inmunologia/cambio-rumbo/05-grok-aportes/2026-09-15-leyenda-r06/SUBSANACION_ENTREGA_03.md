# Subsanación de la entrega 03 · LEYENDA-CONTENIDO/3

**Sede de depósito:** `juantoniolloretegea/SVperitus-dataset`, rama `dominio-inmunologia`, directorio `dominios/inmunologia/cambio-rumbo/05-grok-aportes/2026-09-15-leyenda-r06/`.

**Contrato de partida:** `CONTRATO_CANDIDATO_LEYENDA_CONTENIDO_2.md` en `18e7178e6ec7efbb10863f4d081422f94ef163c2`.

**Seguimiento consultado:** Lenguaje `5e6edf78d8714bbbd57253991e48ba993e79e7a8`, Acta 002. La recepción del ZIP S6 no forma parte de este encargo.

**Estado:** depositado para auditoría. El contrato permanece candidato. No se implementa el reconocedor ni se declara resuelta la leyenda.

## Matriz de reparos

| Reparo | Cambio concreto | Secciones | Fundamento | Límite pendiente |
|---|---|---|---|---|
| LC2-01 · Tolerancia y tinta añadida | Se separan el anillo de 1 px (antialiasing 4-adyacente a la plantilla) y la adición inadmisible (componente de área al menos a_min, coincidencia S no asignada, o residuo total sobre umbral). E2 se parte en E2a–E2d con esperados de frontera. La propiedad exige «sin adición inadmisible», no «sin ningún píxel fuera de la máscara dilatada». | Contrato/3 §A, §B, §F | Acta 002 §4 LC2-01: la dilatación y los umbrales no pueden contradecir E2 | a_min, rho y r_max no cualificados; E2a–E2d no materializados; no hay ensayo de falso positivo |
| LC2-02 · Separadores | Régimen único: dos plantillas de separador obligatorias, orden c1<s1<c2<s2<c3, distancias al menos g_min y anchura en el intervalo declarado. Se deroga «plantilla o hueco». Esperados E12–E14: ausencia, sustitución y contacto → LEYENDA_ILEGIBLE. Un hueco blanco no sustituye al separador. | Contrato/3 §A, §D, §F | El fixture del perfil ya incluye el separador en la cadena de leyenda; la disyuntiva de /2 era ambigüedad, no un cambio de perfil | g_min y las anchuras no cualificados; E12–E14 especificados, no rasterizados |
| LC2-03 · Fondo y transparencia | Tras decodificar y antes de la banda: partición fondo / tinta / resto en todo el lienzo; alfa 0 = fondo blanco; alfa en (0, 255) = FUERA_DE_PERFIL (fondo); marco de 2 px con al menos f_min píxeles de fondo. Precedencia: formato → decodificación → fondo → leyenda. Casos E15 y E16. | Contrato/3 §A (pasos 2–4), §C.4, §F | Acta 002 §4 LC2-03: el fondo figuraba en A y faltaba en C | f_min no cualificado; no se afirma un recuento de fondo observado sobre R01 |

## Archivos

Se añaden únicamente:

- `CONTRATO_CANDIDATO_LEYENDA_CONTENIDO_3.md`
- `SUBSANACION_ENTREGA_03.md`

Se conservan el README y el resto de archivos del corte `18e7178e…`.

## Lo que este acto no resuelve

Parámetros sin cualificar; E1 sin testigo material; reconocedor no implementado; independencia de códec PNG no acreditada; Bis y S26 intactos. Ninguna frontera E2 o E12–E16 se presenta como resultado de un ensayo.
