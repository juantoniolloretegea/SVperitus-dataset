# Máquina de estados de cuarentena local

```text
IDLE
  ↓
FILE_SELECTED
  ↓
TYPE_CHECK
  ├─ fail → REJECTED_TYPE
  └─ pass → LIMITS_CHECK
               ├─ fail → REJECTED_LIMITS
               └─ pass → SANITIZE_LOCAL
                            ├─ fail → REJECTED_SANITIZE
                            └─ pass → HASH_AND_PACKET
                                         ↓
                                      PACKET_READY
                                         ↓
                               DRAFT_TRANSLATION
                                         ├─ fail → U_CONTROLLED
                                         └─ pass → DRAFT_READY
                                                      ↓
                                               HUMAN_CONFIRM
                                                      ├─ reject → STOPPED_BY_USER
                                                      └─ confirm → CONFIRMED
                                                                     ↓
                                                                  CORE_RUN
                                                                     ├─ fail → INTERNAL_REJECT
                                                                     └─ pass → AUDIT_READY
                                                                                     ↓
                                                                                  EXPORT_READY
```

## Reglas duras

- no espera a red
- no depende de backend remoto
- cada transición tiene salida explícita
- `U_CONTROLLED` es estado legítimo, no error oculto
- toda denegación queda trazada en el banco de sucesos
