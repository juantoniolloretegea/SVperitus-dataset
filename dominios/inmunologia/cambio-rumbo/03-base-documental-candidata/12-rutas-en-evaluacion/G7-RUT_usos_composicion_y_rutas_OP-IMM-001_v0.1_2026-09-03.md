# G7-RUT — usos autorizados, composición y rutas / OP-IMM-001 v0.1

- **Fecha:** 03-09-2026
- **Base exacta:** `a3f9d8864196aaa91ad99c3cab4bd96a354ae576`
- **Entrada:** seis matrices, 27 parámetros, un control de salida y un operando de edad
- **Puerta:** `G7-RUT`
- **Estatuto:** `RUTAS_NECESARIAS_CONSTITUIDAS`
- **Decisión terapéutica:** excluida

## 1. Salidas exclusivas

```text
SALIDAS = {
  PERFIL_PREDECISIONAL_SELLADO,
  U_CRITICA_NO_CERRADA,
  FUERA_DE_ALCANCE,
  ABSTENERSE_O_ESCALAR
}
```

No existen `APTO`, `NO_APTO`, `INICIAR`, `NO_INICIAR`, puntuación global ni recomendación farmacológica.

## 2. Objetos de activación

```text
EPISODIO = <sujeto_autorizado, propuesta_sistemica, solicitud,
            reglas_versionadas, fecha_indice, alcance>

alpha(p,O,e,h) -> {ACTIVO, INACTIVO, U_ACTIVACION}
```

Un parámetro se activa cuando su proposición puede modificar la caracterización, consecuencia o ejecución del episodio. `INACTIVO` exige causa explícita; no equivale a valor `0`. Falta de información produce `U_ACTIVACION`, no inactividad.

## 3. Registro de usos por grupos homogéneos

| Parámetros | Activación | Función | Consecuencia de omisión |
|---|---|---|---|
| inicio, diagnóstico base, liderazgo | siempre en episodio iniciado | constituir tiempo, objeto y autoridad | expediente no referible o no gobernado |
| participación de Inmunología | según solicitud/acuerdo | mostrar rol real | atribución asistencial falsa |
| protocolo y restricción local | según centro y actuación | separar verdad clínica y ejecución | ruta inviable u ocultación de limitación |
| glucocorticoide sistémico planificado | si forma parte de la propuesta | caracterizar exposición | exposición incompleta |
| IgG, bazo y ANC | activos para evaluación basal; valor puede ser U | estado del huésped | perfil inmunitario incompleto |
| dispositivo IV e implante | activos como preguntas de cobertura | puerta/material | antecedente material omitido |
| ingreso y soporte por infección | activos como historia de cobertura | consecuencia infecciosa previa | gravedad histórica perdida o fabricada |
| OI y MDRO | activos; configuración ausente conserva U | historia tipada | oportunismo/resistencia falsos u omitidos |
| ingreso agudo y procedimiento invasivo | activos con ventana versionada | exposición sanitaria | contexto temporal perdido |
| DM, HF, CKD, KRT, bronquiectasias, soporte respiratorio y cirrosis | activos como condiciones documentales | reserva/ejecución | modificador omitido o inventado |
| nutrición y fragilidad | activos; paquete no admitido conserva U | reserva evaluada | diagnóstico espurio o reserva no caracterizada |

Cada fila se materializa como registros `u(p,OP-IMM-001)` individuales que heredan Parametro_ID, propietario, transductor y consecuencia G4. La agrupación no fusiona estados.

## 4. Criticidad de U

La criticidad no se deduce del nombre del parámetro ni de una tabla universal. Cada `U` produce:

```text
U_EVENT = <Parametro_ID, causa, evidencia_faltante, consecuencia_G4,
           horizonte, resolubilidad, autoridad, estado_adjudicacion>
```

Estados humanos autorizados:

- `U_CRITICA_PARA_ESTE_EPISODIO`;
- `U_NO_CRITICA_PARA_ESTE_EPISODIO_CON_MOTIVO`;
- `U_RESUELTA_POR_NUEVA_EVIDENCIA`;
- `U_NO_ADJUDICADA`.

La IA no puede asignar `NO_CRITICA`. Requiere médico autorizado, motivo, fecha y alcance. Una U no adjudicada con consecuencia potencial material impide el sellado. Una U no crítica permanece visible en el perfil; no se transforma en 0.

## 5. Vetos no compensables

| Veto_ID | Condición | Efecto estructural |
|---|---|---|
| `V-SCOPE-001` | edad pediátrica, trasplante, CAR-T o quimioterapia citotóxica hematológica principal | `FUERA_DE_ALCANCE` |
| `V-ID-001` | sujeto, propuesta o episodio no identificables | `ABSTENERSE_O_ESCALAR` |
| `V-AUTH-001` | falta de autoridad clínica para solicitud o cierre | `ABSTENERSE_O_ESCALAR` |
| `V-ACTINF-001` | control SEM-RUT-001 requiere evaluación diagnóstica externa o existe infección activa no resuelta | `ABSTENERSE_O_ESCALAR` hacia operación competente |
| `V-TECH-001` | fallo de carga, huella, serialización o reproducción | `ABSTENERSE_O_ESCALAR`; nunca U clínica |
| `V-UCRIT-001` | al menos una U crítica/no adjudicada material | `U_CRITICA_NO_CERRADA` |

Ningún valor favorable, coste, disponibilidad, mayoría o juicio de IA compensa un veto.

## 6. Composición

```text
COMP-OP-IMM-001-v0.1 = <
  M-CTX-AUTH-001,
  M-EXP-001,
  M-HOST-001,
  M-BARRIER-001,
  M-HISTORY-001,
  M-MODIFIER-001,
  SEM-RUT-001,
  EDAD_EN_FECHA_INDICE
>
```

Orden:

1. validar identidad técnica, versión y privacidad;
2. adjudicar alcance;
3. ejecutar control de posible infección activa;
4. constituir contexto, tiempo y autoridad;
5. evaluar transductores activos sin completar ausencias;
6. emitir vectores matriciales;
7. formar eventos U y vetos;
8. someter criticidad y suficiencia al médico;
9. emitir una sola salida estructural.

No se calcula un escalar de riesgo. Los seis vectores, sus U, fuentes y restricciones son el perfil.

## 7. Rutas necesarias

### R-SCOPE-001

Si una exclusión de G1 se verifica: `FUERA_DE_ALCANCE`. Si la información de alcance es insuficiente: `ABSTENERSE_O_ESCALAR`. No continúa silenciosamente.

### R-ACTINF-001

El sistema no diagnostica. Si existe conclusión profesional de infección activa o necesidad de evaluación aguda: `ABSTENERSE_O_ESCALAR`. Si el control no puede cerrarse y la autoridad lo considera material: `U_CRITICA_NO_CERRADA`.

### R-PROFILE-001

Con alcance válido y sin veto previo, se proyectan los seis vectores. Los paquetes OI/MDRO/nutrición/fragilidad no registrados producen U visibles. No obligan por definición a un no go: su criticidad pertenece al episodio y a la autoridad humana.

### R-SEAL-001

`PERFIL_PREDECISIONAL_SELLADO` exige:

- identidad, alcance, propuesta, fecha índice y autoridad constituidos;
- seis matrices proyectadas sin fallo técnico;
- todas las U materiales resueltas o adjudicadas;
- toda U no crítica motivada y visible;
- decisión explícita del médico de que el expediente es suficiente para su decisión.

Sellado no significa tratamiento indicado, seguro ni autorizado.

## 8. Frames

Se constituyen siete proyecciones:

- un frame por cada una de las seis matrices;
- `F-OP-IMM-001-SUMMARY`, resumen reversible.

El resumen muestra primero: salida, vetos, U críticas, restricciones de ejecución, autoridad y versiones. Después permite recuperar cada parámetro, observable, regla, fuente y consecuencia. No borra U ni duplica estado.

## 9. Casos adversariales

1. 26 estados cerrados y una U crítica: no se sella.
2. cinco configuraciones pendientes: no equivalen automáticamente a no go; se adjudican por episodio.
3. médico marca U no crítica sin motivo: inválido.
4. IA marca U no crítica: inválido.
5. infección activa compensada por resto favorable: imposible.
6. fallo técnico convertido en U: imposible.
7. protocolo local rebaja necesidad clínica: imposible.
8. KRT y CKD sumadas como dos puntos: no existe puntuación.
9. perfil sellado interpretado como iniciar tratamiento: prohibido.
10. resumen sin acceso a fuentes/estados: frame no conforme.

## 10. Cierre

```text
PARAMETROS_CON_USO = 27
PARAMETROS_OBLIGATORIOS_SIN_USO = 0
MATRICES_CON_RUTA = 6
SALIDAS_DECIDIBLES = 4
VETOS_TIPADOS = 6
TRATAMIENTO_U = CONSTITUIDO
AUTORIDAD_HUMANA = OBLIGATORIA
G7-RUT = CERRADA
G8-ITI = NO_ABIERTA
```
