# SVperitus IMMUNO-1 — Integración Kotlin (prevista)

> **Estado:** Planificado. Directorio reservado. No implementado todavía.

---

## Propósito

Fase 3 de la hoja de ruta SVperitus–IMMUNO-1: capa de integración cliente
en **Kotlin** (posiblemente Kotlin Multiplatform) para aplicaciones móviles
(Android/iOS) o de escritorio que consuman el motor normativo.

---

## Principio rector (NO negociable)

> Kotlin **consume** el motor normativo (Python o Rust vía API).
> **No redefine** la lógica P01–P25 ni introduce reglas nuevas.
> La lógica normativa vive exclusivamente en `normative_engine.py`
> y su port Rust (`rust/imm1_normative/`).

---

## Arquitectura prevista

```
Aplicación Kotlin
      │
      │  JSON (caso clínico)
      ▼
  API REST / FFI
      │
      ├── Motor Python  (normative_engine.py, servido vía FastAPI/Flask)
      │
      └── Motor Rust    (imm1_normative, compilado como biblioteca nativa)
```

---

## Estructura prevista

```
kotlin/
├── README.md                ← Este archivo
└── imm1_client/             ← módulo KMP (cuando se implemente)
    ├── build.gradle.kts
    └── src/
        ├── commonMain/      ← modelo de datos ClinicalCase, EvaluationResult
        └── androidMain/     ← integración Android (si aplica)
```

---

## Referencia cruzada

- Motor normativo Python : `IMMUNO-1/normative_engine.py`
- Port Rust              : `rust/imm1_normative/`
- Configuración canónica : `IMMUNO-1/config/imm_n25.yaml`
- Documento formal       : `docs/Documento7_IMMUNO-1.md`

---

*Este directorio se poblará en la Fase 3 de implementación.*
