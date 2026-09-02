# Orden de auditoría externa G1 — OP-IMM-001 v0.1

## 1. Objeto exacto

Auditar exclusivamente la constitución de la primera operación clínica testigo de INMUNO:

- **Repositorio:** `juantoniolloretegea/SVperitus-dataset`
- **Rama:** `dominio-inmunologia`
- **Commit material:** `3c8444b8ca549a90fc10d52bb6abf1465fb23d83`
- **Operación:** `OP-IMM-001`
- **Puerta:** `G1-OP`
- **Fecha:** 02-09-2026

Objetos materiales:

| Objeto | SHA-256 |
|---|---|
| `OP-IMM-001_constitucion_perfil_riesgo_infeccioso_preinmunosupresion_G1_v0.1_2026-09-02.md` | `a3b1df319305f2931a6a54c1427455fbc7e1b26ac2d80b7e1a176ac2729ab83e` |
| `Adversarial_interna_G1_OP-IMM-001_v0.1_2026-09-02.md` | `16ac6a37668bfc08631dcec0b23f581935741258bb4d2f858f5b4f2146b92ba5` |
| `README.md` del directorio G1 | `252aa86db896fad61e0a29dfffa85ffe72ffce4077c3e435e7c2b8045e110b50` |

Base rectora que debe leerse antes de auditar:

- contrato semántico INMUNO v0.2;
- protocolo adversarial transversal INMUNO v0.2;
- catálogo profesional INMUNO v0.8;
- recepción y cierre de la compuerta `NA0` v0.2.

No auditar el estado del arte clínico ni diseñar la fase siguiente. Esta orden sólo decide si la operación está suficientemente constituida para permitir posteriormente la formulación de preguntas candidatas en `G2-SEM`.

## 2. Ataque A — Identidad y regresión

1. Calcular bytes y SHA-256 de los tres objetos materiales.
2. Confirmar que el commit auditado es exactamente el indicado.
3. Compararlo con su padre `06ddc1f05c96ef8f00b8286e2857d90d1e27b74b`.
4. Verificar que sólo se añadieron el directorio G1 y la referencia correspondiente en `dominios/inmunologia/cambio-rumbo/README.md`.
5. Verificar que no cambiaron:
   - el catálogo XLSX v0.8;
   - `agentes/inmunologia/`;
   - motores normativos;
   - YAML;
   - compositor;
   - Lenguaje SV;
   - `main`.

## 3. Ataque B — Unidad real de la operación

Intentar refutar que `OP-IMM-001` sea una sola operación clínica finita.

Debe determinarse si «constituir el perfil de riesgo infeccioso inmunológicamente relevante antes del inicio propuesto de inmunosupresión farmacológica sistémica»:

- posee un solo sujeto, un solo desencadenante y un solo producto;
- o encubre varias operaciones independientes, por ejemplo diagnóstico de infección activa, selección de pruebas, vacunación, profilaxis, elección del inmunosupresor, autorización de inicio y seguimiento.

No basta enumerar temas clínicos relacionados. Para demostrar composición indebida debe identificarse qué suboperación tiene inicio, cierre, autoridad o consecuencia independientes y por qué no puede permanecer como información subordinada al mismo expediente predecisional.

Si la unidad falla, proponer únicamente el corte mínimo necesario; no diseñar parámetros ni matrices.

## 4. Ataque C — Paciente, población y alcance

Comprobar que el objeto se refiere a un paciente adulto real y no a una cohorte media.

Atacar expresamente:

- adulto de 18 años o más;
- propuesta real de inicio;
- inmunosupresión farmacológica sistémica;
- exclusión de trasplante de órgano sólido;
- exclusión de trasplante de progenitores hematopoyéticos;
- exclusión de terapia con células CAR-T;
- exclusión de quimioterapia citotóxica hematológica como régimen principal;
- exclusión de pediatría.

Determinar si las fronteras son operacionalmente reconocibles o si contienen solapamientos que permitirían incorporar indebidamente otra ruta. Una exclusión no puede interpretarse como expulsión del dominio general de inmunología: sólo de esta operación testigo.

## 5. Ataque D — Inicio, final y horizonte

Comprobar que los cuatro requisitos de inicio son necesarios y verificables.

Atacar los cuatro finales:

- `PERFIL_PREDECISIONAL_SELLADO`;
- `U_CRITICA_NO_CERRADA`;
- `FUERA_DE_ALCANCE`;
- `ABSTENERSE_O_ESCALAR`.

Debe resolverse expresamente:

1. si `PERFIL_PREDECISIONAL_SELLADO` puede confundirse con «tratamiento seguro», «tratamiento indicado» o «tratamiento autorizado»;
2. si el final es finito aunque en G1 todavía no estén constituidos los parámetros ni la clausura mínima del perfil;
3. si existe circularidad entre «perfil suficientemente caracterizado» y reglas que sólo se definirán en G2–G5;
4. si las ventanas específicas de los futuros observables pueden diferirse sin convertir el horizonte común en indefinido;
5. si una novedad posterior exige nueva versión o `REOPEN_REQUIRED`, en lugar de prolongar el episodio sin límite.

Si la operación no puede cerrar legítimamente antes de conocer sus parámetros, clasificar el defecto y precisar la corrección mínima de G1. No anticipar contenido de G2.

## 6. Ataque E — Autoridad y límites asistenciales

Verificar que:

- sólo el médico habilitado conforme a jurisdicción y episodio adopta la decisión terapéutica;
- el sellado humano del expediente no transfiere autoridad al sistema;
- la inteligencia artificial sólo ordena, verifica trazas, señala ausencias y presenta;
- el especialista de laboratorio no aparece como prescriptor autónomo donde la jurisdicción no lo permita;
- el Director constituye dominio y reglas documentales, pero no decide sobre el paciente;
- no existe ninguna salida automática `APTO`, `NO_APTO`, `INICIAR` o `NO_INICIAR`.

Buscar prescripción encubierta. En particular, distinguir entre identificar una necesidad de información y seleccionar, indicar u ordenar una prueba.

## 7. Ataque F — Fundamento profesional y trazabilidad

Abrir el XLSX del catálogo profesional INMUNO v0.8, no una conversión parcial. Comprobar que existen y sostienen, sin ampliación, los registros declarados en el apartado 8 de la operación:

- España: `ES-INM-ROL-003`, `ES-INM-ROL-006`, `ES-INM-ROL-007`, `ES-INM-CONT-044`, `ES-INM-CONT-049`, `ES-INM-CONT-075`, `ES-INM-CONT-089`;
- Reino Unido: `CTX-A3-C06`, `CTX-A3-C07`, `CTX-A4-P05`, `CTX-A4-P06`;
- Australia–Aotearoa Nueva Zelanda: `AUNZ-G05`, `AUNZ-G08`, `AUNZ-G10`, `AUNZ-G11`, `AUNZ-KG-01`, `AUNZ-KG-06`;
- Canadá: `CA-SCP-07`, `CA-SCP-09`, `CA-SCP-10`, `CA-OP-07`, `CA-OP-08`, `CA-OP-09`, `CA-OP-10`.

Para cada jurisdicción, dictaminar:

- qué parte de la pertinencia profesional sostiene;
- qué parte no sostiene;
- si se confundió una competencia, guía o contexto con un parámetro clínico ya constituido;
- y si la formulación internacional excede el corpus profesional cerrado.

No exigir que un único currículo contenga toda la operación. La prueba es de convergencia profesional comparada, no de supremacía del currículo español ni de identidad entre jurisdicciones.

## 8. Ataque G — Incertidumbre, seguridad y no compensación

Ejecutar como mínimo estos contraejemplos:

1. paciente con sospecha de infección activa;
2. inicio urgente con información crítica ausente;
3. recurso o prueba no disponible;
4. paciente que ya inició tratamiento y requiere seguimiento;
5. información discordante entre fuentes;
6. dato aparentemente tranquilizador junto a una `U` crítica.

Comprobar que:

- una sospecha de infección activa produce salida, no diagnóstico o tratamiento dentro de `OP-IMM-001`;
- la urgencia no cierra una `U`;
- coste, disponibilidad, cama, tiempo administrativo o conveniencia no compensan el riesgo clínico;
- el tiempo clínico sí puede afectar validez y ruta futura;
- una mayoría de estados favorables no vence una criticidad;
- `T(25)=19` y cualquier umbral heredado permanecen fuera;
- la salida conserva incertidumbre y no fabrica certeza.

## 9. Ataque H — No anticipación de G2 y de capas posteriores

Verificar que G1 no constituye todavía:

- parámetros clínicos;
- atomicidad;
- observables y ventanas definitivos;
- consecuencias clínicas plenas;
- vetos concretos;
- matrices;
- composiciones;
- rutas críticas;
- frames;
- cohortes;
- ni cambios del Lenguaje SV.

Las seis familias preliminares sólo pueden ser orientaciones de búsqueda semántica. Determinar si alguna actúa de hecho como matriz o clasificación cerrada.

No seleccionar fármacos, pruebas, guías, cohortes ni fuentes nuevas. No proponer semántica o Representación Intermedia del Lenguaje SV.

## 10. Salida obligatoria

Entregar una única auditoría con:

1. identidad calculada;
2. dictamen global limitado a:
   - `PASA`;
   - `PASA_CON_REPAROS`;
   - `NO_PASA`;
   - `U_AUDITORIA_INCOMPLETA`;
3. tabla de ataques A–H;
4. comprobaciones que resisten;
5. reparos numerados con severidad, texto atacado, evidencia, consecuencia y corrección mínima;
6. incertidumbres legítimas que pertenecen a fases posteriores y no son defectos de G1;
7. respuesta expresa a si `OP-IMM-001` es una operación singular y finita;
8. respuesta expresa a si queda autorizado abrir `G2-SEM`;
9. declaración de que el dictamen no constituye protocolo clínico, adopción asistencial ni decisión sobre un paciente.

## 11. Límites

- No escribir en GitHub.
- No crear PR.
- No modificar archivos.
- No tocar `main`.
- No repetir una auditoría general del catálogo v0.8.
- No abrir una búsqueda de cohortes o estado del arte.
- No diseñar parámetros, matrices, rutas ni frames.
- No convertir pilotos en autoridad.
- No convertir falta de exhaustividad mundial en defecto si la operación queda sostenida por el corpus profesional cerrado.
- No convertir una incertidumbre propia de G2–G5 en defecto de G1 salvo que haga imposible definir o cerrar la operación.
