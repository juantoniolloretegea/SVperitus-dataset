# Patrón común emergente del agente especializado

## Estatuto

Esta pieza tiene carácter **subordinado, arquitectónico y de aplicación**.  
No crea doctrina nueva y no redefine por sí sola el Lenguaje SV.

Su función es dejar fijado el **patrón operativo mínimo** que empieza a emerger en `SVperitus` cuando un agente especializado alcanza un grado suficiente de madurez.

## Qué se entiende aquí por agente especializado

Un agente especializado es una entidad del ecosistema SV:

- organizada por fases de desarrollo;
- tipada a un ámbito concreto de aplicación;
- acompañada de artefactos, laboratorios y superficies de uso;
- y orientada, en su madurez, a constituir un paquete autónomo y funcional.

## Patrón común emergente

Sin perjuicio de las diferencias de dominio, un agente especializado suficientemente maduro podrá comparecer con:

1. **puerta de entrada del agente**;
2. **desarrollo por fases**;
3. **publicación de fase**;
4. **laboratorio y figuras de fase**;
5. **monitor poligonal principal**;
6. **lectura por SUCESOS**;
7. **plano IA trazable**;
8. **capa R³ auxiliar**;
9. **evidencia y trazabilidad**.

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

## Primer piloto real

En el estado actual del repositorio, el **Agente especializado en Seguridad Estructural — Fase I** actúa como **primera implementación piloto** de este patrón común.

Esto no significa que el patrón pertenezca en exclusiva a seguridad.  
Significa que ha comparecido primero ahí por la dinámica efectiva del desarrollo y deberá poder tiparse después para otros agentes.

## Relación con inmunología

El **Agente especializado en Inmunología** se desarrolla también por fases.  
La futura generalización del patrón no convierte a sus fases ni a sus artefactos en “módulos” empresariales: los conserva como fases del mismo agente, con artefactos adscritos a la fase que los haya hecho necesarios.

## Relación con el Lenguaje SV

La maduración plena de este patrón exigirá, en su momento, un contrato técnico mínimo en `SV-lenguaje-de-computacion` para la capa de consulta y simulación trazable por agente. Mientras ese contrato no quede fijado, las implementaciones actuales deben leerse como **pilotos subordinados**.

## Regla final

El patrón común emergente del agente especializado en `SVperitus` no debe inflarse como doctrina soberana ni como repositorio aparte por necesidad inmediata.  
Debe consolidarse con sobriedad, quedar tipado por agente y preparar, sin precipitación, la futura convivencia entre doctrina, lenguaje, agentes e IA.
