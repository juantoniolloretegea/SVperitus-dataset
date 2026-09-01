# Encargo a Grok — conjuntos de datos candidatos de inmunología

**Rama obligatoria:** `dominio-inmunologia`  
**Directorio de trabajo:** `dominios/inmunologia/cambio-rumbo/05-grok-aportes/conjuntos-de-datos-candidatos/`  
**Destino canónico eventual:** `dominios/inmunologia/dominio-01-09-26/conjunto-de-datos/` en `main`  
**Estado de todo lo producido aquí:** `CANDIDATO_NO_ADOPTADO`

## Orden

Identifique, documente y someta a evaluación adversarial conjuntos de datos y cohortes que puedan aportar contrastación empírica al dominio completo de inmunología. La cobertura podrá requerir varios repositorios. No presuponga que un único conjunto es suficiente.

Trabaje exclusivamente en este directorio y en la rama `dominio-inmunologia`. No escriba en `main`, no abra ni fusione una pull request y no traslade ningún conjunto al destino canónico.

## Secuencia obligatoria

1. Consulte primero las bibliotecas temáticas ya existentes en la rama.
2. Busque fuera solo cuando la necesidad de cobertura no esté satisfecha.
3. Registre cada conjunto por separado y por versión en `inventario_candidatos_v0.1.csv`.
4. Cree un manifiesto por conjunto siguiendo `plantilla_manifiesto_conjunto_v0.1.md`.
5. Verifique la fuente primaria del repositorio, el diccionario de datos, la licencia y las condiciones de acceso. Una publicación secundaria no sustituye esta comprobación.
6. Declare qué poblaciones, variables inmunológicas, intervenciones, exposiciones y desenlaces contiene realmente.
7. Declare expresamente qué familias clínicas no cubre y qué variables necesarias están ausentes.
8. Distinga datos individuales, agregados, sintéticos, de registro, ensayo, cohorte, vigilancia o biobanco.
9. Evalúe acceso, autorización, licencia, redistribución, elegibilidad para tratamiento mediante IA, anonimización y riesgo de reidentificación por conjunto, versión y finalidad.
10. Registre las transformaciones, exclusiones, imputaciones y derivaciones ya aplicadas por los productores.
11. Separe asociación estadística, temporalidad y causalidad. No convierta ninguna asociación en consecuencia clínica.
12. Entregue al final una matriz de cobertura conjunto × familia clínica × variable × desenlace y un registro de huecos y residuales.

## Prohibiciones

- No constituir el dominio clínico.
- No constituir consecuencias de ignorancia.
- No crear ni modificar parámetros, matrices o componentes del SV.
- No armonizar rótulos clínicos por semejanza léxica.
- No imputar variables ausentes ni completar campos mediante inferencia.
- No declarar causalidad a partir de asociación.
- No subir datos personales, seudonimizados o con riesgo de reidentificación no resuelto.
- No copiar datos de acceso controlado o cuya licencia no autorice redistribución.
- No usar claves, credenciales o tokens como contenido del repositorio.
- No considerar “públicamente accesible” equivalente a “redistribuible” o “admisible para IA”.
- No promover ningún elemento a `main`.

## Tratamiento de los datos

En esta primera ronda se subirán únicamente inventarios, manifiestos, diccionarios públicos permitidos, referencias exactas y evaluaciones. Los ficheros de datos no se descargarán ni se incorporarán al repositorio sin autorización expresa posterior del Director.

Para conjuntos no redistribuibles o de acceso controlado, conserve solo accession, versión, procedimiento autorizado de acceso, consulta o receta de extracción reproducible, restricciones y huella criptográfica del resultado cuando proceda y sea lícito.

## Estados permitidos

`IDENTIFICADO` · `ACCESO_PENDIENTE` · `ACCESO_VERIFICADO` · `EVALUADO` · `ADMISIBLE_CANDIDATO` · `NO_ADMISIBLE` · `U_CAUSA_DECLARADA`

Ninguno de estos estados equivale a adopción. La admisión en `main` requiere revisión adversarial independiente y decisión humana expresa.
