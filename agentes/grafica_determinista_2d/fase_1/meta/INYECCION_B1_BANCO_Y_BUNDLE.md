# INYECCIÓN B1 — BANCO Y BUNDLE TÉCNICO

## Alcance

Esta inyección no introduce todavía el corrector diferencial pleno. Su objetivo es cerrar el **banco doble** y el **bundle técnico exportable** del AE-GD2-SV.

## Entradas de esta inyección

- Banco técnico `append-only` exportable.
- Índices laterales mínimos.
- Secuencia soberana exportable en CSV.
- Logs separados de cuarentena, validación y ejecución.
- ZIP técnico generado desde Python.

## Salidas esperadas

- `events.jsonl`
- `event_index.json`
- `events_flat.csv`
- `index_by_param.csv`
- `index_by_type.csv`
- `sovereign_sequence.csv`
- `critical_parameters.csv`
- `frame25.csv`
- `gob25.csv`
- `quarantine_log.jsonl`
- `validator_log.jsonl`
- `execution_log.jsonl`
- `*.zip`
