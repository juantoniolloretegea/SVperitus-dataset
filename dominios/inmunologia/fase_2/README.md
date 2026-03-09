# IMMUNO-2 — Estratificación del riesgo de infección grave

> **Estado:** Especificación P01–P25 completada (borrador 0).
> Pendiente: cotejo fino de Capas 2–5, motor normativo Python, port Rust.
> Lógica clínica NO congelada todavía — sujeta a revisión adversarial.

---

## Subdominio

Estratificación del riesgo de infección grave en adultos con
inmunosupresión farmacológica sistémica no trasplante.

## Relación con IMMUNO-1

| | IMMUNO-1 (Doc 7) | IMMUNO-2 |
|---|---|---|
| Pregunta | ¿Está protegido? (profilaxis/vacunas) | ¿Cuál es su riesgo residual? |
| Población | Neoplasias hematológicas | IS farmacológica no trasplante |
| Estado | Sellado | En desarrollo |
| Puente | — | P25 integra output de IMMUNO-1 |

## Contenido de esta carpeta

| Archivo | Descripción |
|---------|-------------|
| `IMMUNO2_P01-P25_spec.md` | Especificación completa: 25 parámetros, 5 capas, criterios 0/1/U, referencias clínicas |

## Estructura prevista (cuando se complete)

```
IMMUNO-2/
├── config/imm2_n25.yaml        ← punto único de verdad
├── normative_engine.py          ← motor normativo P01–P25
├── generate_cases.py            ← generador sintético
├── generate_polygons.py         ← vectores → PNG 224×224
├── train_resnet.py              ← ResNet34
├── evaluate.py                  ← evaluación
└── IMMUNO2_P01-P25_spec.md      ← especificación (ya presente)
```

## Exclusiones

Fuera del alcance de IMMUNO-2 (reservados a módulos futuros):
- Trasplante de órgano sólido (TOS)
- TPH / CAR-T (cubierto por IMMUNO-1)
- Quimioterapia citotóxica pura (guías MASCC/ESMO)
- VIH como causa primaria

## Referencia cruzada

- Spec completa: `IMMUNO2_P01-P25_spec.md` (en esta carpeta)
- IMMUNO-1 sellado: `../fase_1/`
- Documento 7: `../../documentos/serie/Documento7_IMMUNO-1.md`
- Port Rust: `../../entornos/rust/`
