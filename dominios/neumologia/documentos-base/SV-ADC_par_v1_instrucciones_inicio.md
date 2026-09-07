# SV-ADC(par) v1 — Instrucciones maestras de arranque para nuevo chat

## 1. Objeto de este archivo

Este archivo sirve como **punto de partida autónomo** para que un nuevo chat, o una IA colaboradora como **Claude**, pueda continuar el proyecto **desde cero** sin depender del historial previo.

El núcleo ya consolidado en la **Fase I** es el siguiente:

- Arquitectura: **`SV-ADC(par) = SV-ADC_L(25,5) + SV-ADC_V(16,4)`**
- Restricción formal de cada célula: **`n = b^2`, con `b >= 3`**
- Semántica ternaria canónica: **`0 / 1 / U`**
- Composición entre células: **jerárquica por compuerta**, **no** `max()`
- CNN: **pieza nuclear**, no ornamental
- Dataset inicial: **sintético, auditable y corregible por expertos**
- Finalidad de la CNN: **motor de generalización sobre una gramática visual corregida por expertos**

---

## 2. Archivos ya generados y que deben tomarse como base oficial

Los tres archivos base del proyecto son:

1. **Documento maestro limpio**  
   `SV-ADC_par_v1_documento_maestro.docx`

2. **CSV semilla único**  
   `SV-ADC_par_v1_seed.csv`

3. **JSON semilla único**  
   `SV-ADC_par_v1_seed.json`

Cualquier nuevo trabajo debe considerarlos como la **base documental oficial de la Fase I**.

---

## 3. Decisión arquitectónica ya cerrada

Se da por cerrada la siguiente arquitectura:

## `SV-ADC(par) v1 = SV-ADC_L(25,5) + SV-ADC_V(16,4)`

### 3.1. Célula `SV-ADC_L(25,5)`
Función:
- **Sospecha clínico-lesional estructurada** de adenocarcinoma pulmonar primario.

Contiene 25 parámetros agrupados en 5 capas.

### 3.2. Célula `SV-ADC_V(16,4)`
Función:
- **Validez confirmatoria diagnóstica** del cierre anatomopatológico, inmunofenotípico y molecular.

Contiene 16 parámetros agrupados en 4 capas.

### 3.3. Regla de composición
La composición entre ambas células es **jerárquica por compuerta**:

- La célula **L** aporta **sospecha estructurada**.
- La célula **V** aporta **capacidad real de cierre confirmatorio**.
- La sospecha **no sustituye** a la confirmación.
- Si `V = U`, el sistema global permanece en `U`, aunque `L` sea altamente sospechosa.
- Si hay discordancia importante entre `L` y `V`, el resultado global debe permanecer en `U` por discordancia.

**Se descarta expresamente** el uso de `max()` como regla de composición.

---

## 4. Semántica canónica obligatoria

Cada parámetro del sistema se codifica como:

- **`0`** = no apoya adenocarcinoma pulmonar primario en ese eje
- **`1`** = apoya adenocarcinoma pulmonar primario en ese eje
- **`U`** = no consta, no evaluable, no realizado o contradicción no resuelta

### Regla dura
**Si el dato no está documentado, no se imputa `0`; se marca `U`.**

Esta regla no debe relajarse.

---

## 5. Papel exacto de la CNN

La CNN no se usa como adorno visual ni como simple replicador trivial de un render bonito.

Su papel exacto es:

- aprender sobre una **gramática visual canónica** derivada de las células SV;
- preentrenarse con **dataset sintético auditable**;
- servir como **motor de generalización** sobre esa gramática;
- ser **corregida posteriormente por expertos médicos**, que no sólo revisarán etiquetas, sino también:
  - parámetros,
  - fronteras,
  - discordancias,
  - inconsistencias,
  - y casos límite.

La formulación correcta del proyecto es:

> **motor de generalización sobre una gramática visual corregida por expertos**

No debe rebajarse a:

> render bonito de reglas fijas

---

## 6. Estructura de entrada para la CNN

### Entrada conceptual
Cada caso genera dos vectores ternarios:

- `vL ∈ {0,1,U}^25`
- `vV ∈ {0,1,U}^16`

Cada vector se transforma en un **polígono polar canónico**.

### Arquitectura recomendada en Fase I
- CNN de **doble rama**:
  - rama `L` para `SV-ADC_L(25,5)`
  - rama `V` para `SV-ADC_V(16,4)`
- **Fusión tardía**

### Regla de render canónico
Debe mantenerse fijo:

- fondo
- tamaño del lienzo
- orden angular
- convención radial de `0 / 1 / U`
- grosor de línea
- resolución
- antialiasing
- ausencia de rotación
- ausencia de reordenación angular

La CNN debe aprender **configuración**, no artefactos gráficos.

---

## 7. Orden canónico de variables

### 7.1. Orden de `SV-ADC_L(25,5)`

`L01 L02 L03 L04 L05 | L06 L07 L08 L09 L10 | L11 L12 L13 L14 L15 | L16 L17 L18 L19 L20 | L21 L22 L23 L24 L25`

### 7.2. Orden de `SV-ADC_V(16,4)`

`V01 V02 V03 V04 | V05 V06 V07 V08 | V09 V10 V11 V12 | V13 V14 V15 V16`

Este orden no debe alterarse sin una revisión metodológica expresa.

---

## 8. Variables ya fijadas

Las variables concretas, su nombre corto y la semántica `0 / 1 / U` ya están definidas en:

- `SV-ADC_par_v1_documento_maestro.docx`
- `SV-ADC_par_v1_seed.csv`
- `SV-ADC_par_v1_seed.json`

Un nuevo chat debe leer esos tres archivos antes de proponer modificaciones.

---

## 9. Uso correcto del CSV y del JSON semilla

### CSV semilla
Debe entenderse como:
- tabla maestra compacta,
- base para inspección humana,
- y punto de partida para generación tabular de casos sintéticos.

### JSON semilla
Debe entenderse como:
- versión estructurada y programáticamente interoperable,
- base para generadores automáticos,
- y soporte para pipelines reproducibles.

Ambos archivos representan la **misma ontología** y no deben divergir.

---

## 10. Qué está cerrado y qué no

### Ya cerrado
- restricción formal por células (`n=b^2`)
- arquitectura pareada `25 + 16`
- semántica `0 / 1 / U`
- composición por compuerta
- doble rama CNN
- papel no ornamental de la CNN
- tabla maestra v1
- documento maestro v1
- CSV/JSON semilla v1

### No cerrado aún
- estrategia completa de generación masiva del dataset sintético
- política exacta de muestreo de casos frontera
- protocolo de corrección médica experta
- definición plena de Fase II multimodal con imagen real
- lógica final de confluencia con una rama radiológica real

---

## 11. Instrucciones para un nuevo chat

Si este proyecto se retoma en un nuevo chat, debe seguirse este protocolo:

1. Leer este archivo completo.
2. Leer después los tres archivos oficiales:
   - `SV-ADC_par_v1_documento_maestro.docx`
   - `SV-ADC_par_v1_seed.csv`
   - `SV-ADC_par_v1_seed.json`
3. No rediscutir la arquitectura base de Fase I salvo que se solicite expresamente.
4. No sustituir la lógica de compuerta por reglas tipo `max()`.
5. No tratar la CNN como elemento decorativo.
6. No degradar la semántica `U` ni imputarla como `0` por defecto.
7. Mantener la separación entre:
   - célula lesional
   - célula confirmatoria
8. Cualquier ampliación debe respetar el formalismo de células completas compatibles con `n=b^2`.

---

## 12. Instrucciones específicas para colaboración con Claude

Cuando intervenga **Claude** u otra IA colaboradora, debe hacerse así:

### 12.1. Qué debe recibir Claude
Claude debe recibir, como paquete mínimo:

- este archivo Markdown;
- el documento maestro `SV-ADC_par_v1_documento_maestro.docx`;
- el CSV semilla `SV-ADC_par_v1_seed.csv`;
- el JSON semilla `SV-ADC_par_v1_seed.json`.

### 12.2. Qué debe entender Claude
Claude debe entender que:

- la **Fase I ya está cerrada**;
- la arquitectura de referencia es **pareada**;
- la CNN es **troncalmente importante**;
- el sistema no pretende aún ser una herramienta clínica directa acabada;
- el dataset inicial es **sintético**, pero preparado para ser **corregido por expertos**;
- la indeterminación `U` es estructural y no residual.

### 12.3. Qué tipo de colaboración debe pedirse a Claude
Las peticiones adecuadas a Claude son, por ejemplo:

- revisión adversarial de la ontología;
- propuesta de generadores sintéticos coherentes con la tabla maestra;
- diseño del pipeline de render polar;
- propuesta de arquitectura CNN de doble rama;
- diseño de criterios de corrección experta;
- ayuda para Fase II multimodal;
- validación lógica de reglas de composición y salidas.

### 12.4. Qué no debe pedirse a Claude en esta fase
No debe pedírsele que:

- rehaga la arquitectura base sin motivo;
- sustituya la semántica `0 / 1 / U`;
- trate la CNN como adorno;
- convierta prematuramente el sistema en un simple clasificador binario;
- mezcle la Fase I con Fase II sin distinguir modalidades.

---

## 13. Formulación doctrinal resumida del modelo

> **SV-ADC(par) v1** es un sistema pareado de dos células SV completas, compatibles con la restricción `n=b²`: una célula lesional `SV-ADC_L(25,5)` y una célula confirmatoria `SV-ADC_V(16,4)`. Cada parámetro se expresa en semántica ternaria `0 / 1 / U`. Cada célula se renderiza como polígono polar canónico y alimenta una CNN de doble rama. El dataset inicial es sintético y auditable. La CNN no se concibe como reemplazo de la histología ni como simple render decorativo, sino como motor de generalización sobre una gramática visual inicialmente normativa y posteriormente corregida por expertos médicos.

---

## 14. Punto de anclaje para continuar

Si un nuevo chat retoma el proyecto desde aquí, el siguiente paso lógico no es rediscutir la Fase I, sino elegir una de estas líneas:

1. **Generación formal del dataset sintético**
2. **Diseño del pipeline de render polar**
3. **Diseño de la CNN de doble rama**
4. **Diseño del protocolo de corrección médica experta**
5. **Apertura controlada de Fase II multimodal con imagen real**

---

## 15. Estado del proyecto al cierre de este archivo

**Fase I: cerrada.**  
**Modelo base: consolidado.**  
**Archivos oficiales: generados.**  
**Listo para continuación en nuevo chat o con Claude.**
