# Patrón común emergente del agente especializado

## Estatuto

Esta pieza tiene carácter subordinado, arquitectónico y de aplicación.

No crea doctrina nueva y no redefine por sí sola el Lenguaje SV.

Su función es dejar fijado el patrón operativo mínimo que empieza a emerger en `SVperitus` cuando un agente especializado alcanza un grado suficiente de madurez.

## Qué se entiende aquí por agente especializado

Un agente especializado es una entidad del ecosistema SV:

- organizada por fases de desarrollo;
- tipada a un ámbito concreto de aplicación;
- acompañada de artefactos, laboratorios y superficies de uso;
- y orientada, en su madurez, a constituir un paquete autónomo y funcional.

## Patrón común emergente

Sin perjuicio de las diferencias de dominio, un agente especializado suficientemente maduro podrá comparecer con:

1. puerta de entrada del agente;
2. desarrollo por fases;
3. publicación de fase;
4. laboratorio y figuras de fase;
5. monitor poligonal principal;
6. lectura por SUCESOS;
7. plano IA trazable;
8. capa R³ auxiliar;
9. evidencia y trazabilidad.

## Estatuto del plano IA

El plano IA:

- no es soberano;
- no sustituye al álgebra;
- no sustituye al experto humano;
- no reescribe la historia real;
- no cierra `U` por sí solo;
- y debe mantener separación entre `REAL` y `SIM`.

Su función es asistir al experto con:

- consulta estructurada;
- simulación condicional;
- justificación;
- y metadatos de reconstrucción.

## Condición basal de custodia del diseño

La evolución del ecosistema obliga a fijar una condición adicional: ningún agente especializado nuevo, ninguna fase relevante y ningún artefacto sensible de uso, laboratorio o compilación deben desarrollarse al margen de una custodia basal del diseño.

Dentro del estado actual de `SVperitus`, esa custodia basal comparece por primera vez en la **Célula especializada de seguridad estructural para la custodia del diseño, el DSL y los laboratorios del Sistema Vectorial SV**.

Su papel correcto aquí no es el de doctrina soberana ni el de sede técnica del lenguaje. Su papel es otro:

- actuar como **guardarraíl basal obligatorio** del diseño;
- impedir aperturas semánticas silenciosas;
- vigilar fracturas entre manuscrito, repositorio, publicación, DSL y laboratorio;
- y conservar la `U` legítima frente a cierres impropios.

## Primer piloto real

En el estado actual del repositorio, el **Agente especializado en Seguridad Estructural — Fase I** actúa como primera implementación piloto de este patrón común y, además, como primera materialización de la custodia basal del diseño.

Esto no significa que el patrón pertenezca en exclusiva a seguridad. Significa que ha comparecido primero ahí por la dinámica efectiva del desarrollo y deberá poder tiparse después para otros agentes.

## Relación con inmunología

El Agente especializado en Inmunología se desarrolla también por fases.

La futura generalización del patrón no convierte a sus fases ni a sus artefactos en “módulos” empresariales: los conserva como fases del mismo agente, con artefactos adscritos a la fase que los haya hecho necesarios.

Esa futura generalización tampoco permite saltarse la custodia basal del diseño. Por el contrario, exige que cada fase y cada artefacto sensible de inmunología nazcan ya bajo esa vigilancia estructural.

## Relación con el Lenguaje SV

La maduración plena de este patrón exigirá, en su momento, un contrato técnico mínimo en `SV-lenguaje-de-computacion` para la capa de consulta y simulación trazable por agente.

Además, toda evolución futura del lenguaje que afecte a agentes, consultas, lowering, serialización, validación o interfaz de simulación deberá convivir con la custodia basal del diseño y no podrá bypassarla por vía puramente técnica.

Mientras ese contrato no quede fijado, las implementaciones actuales deben leerse como pilotos subordinados.

## Regla final

El patrón común emergente del agente especializado en `SVperitus` no debe inflarse como doctrina soberana ni como repositorio aparte por necesidad inmediata.

Debe consolidarse con sobriedad, quedar tipado por agente, reconocer la custodia basal obligatoria del diseño y preparar, sin precipitación, la futura convivencia entre doctrina, lenguaje, agentes e IA.
