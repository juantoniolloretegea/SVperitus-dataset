# DICTAMEN ADVERSARIAL DE WATSON

## Snippet R0 v4 — informe de situación del 17/07/2026

**Estado:** APTO PROVISIONAL DE LABORATORIO.
**No queda todavía auditado el código v4 ni confirmado el cierre material de la compuerta.**

El informe responde de forma sustantiva a los diez reparos anteriores. Las correcciones descritas son coherentes y las pruebas positivas muestran que la arquitectura ya no es meramente declarativa. Sin embargo, el informe no sustituye la lectura del snippet v4 completo ni la prueba negativa pendiente.

---

## 1. Resolución de los reparos anteriores

### 1.1. Prioridad 15

**APTO.**

La secuencia declarada es ahora correcta para el Régimen A descrito:

```text
ACF, prioridad 10 → guarda los valores
R0, prioridad 15 → lee y calcula
slug, prioridad 20 → deriva el enlace permanente
```

Se acepta la corrección y se registra que la prioridad 5 era un defecto material, no una mejora menor.

### 1.2. Congelación efectiva

**APTO EN PRINCIPIO; PENDIENTE DE AUDITORÍA DEL CÓDIGO.**

La combinación descrita:

* filtros `acf/update_value/name=...` para los campos protegidos;
* restauración de `post_name`;
* tratamiento de `publish` y `future`;

responde al reparo central: la inmutabilidad ya no depende de un aviso.

Las pruebas sobre la entrada 32471 aportan evidencia favorable:

* el cambio de R2 publicado fue rechazado;
* el cambio manual de slug publicado fue restaurado.

No obstante, debo comprobar en el código:

* qué valor devuelve exactamente cada filtro;
* si se protege también el interruptor;
* cómo se distingue una corrección técnica autorizada;
* si existe riesgo de restaurar un valor vacío o incorrecto en publicaciones heredadas;
* si la restauración opera también al pasar de `future` a `publish`.

### 1.3. Eliminación de `r3_cid`

**APTO Y PREFERIBLE.**

El director detectó correctamente que R3 es un dato derivado reproducible:

```text
R3 = dmeditorialiawp.<ID> + R2
```

Almacenarlo añadía una copia editable y una nueva obligación de sincronización. Recomponerlo al vuelo reduce el número de fuentes de verdad.

La eliminación no es una pérdida de trazabilidad, siempre que la interfaz pueda mostrar el R3 calculado cuando sea necesario y el código que lo compone quede estable.

### 1.4. Delimitación histórica del dominio

**APTO COMO HALLAZGO; NO COMO REGLA UNIVERSAL TODAVÍA.**

El inventario descrito acredita:

* 238 publicaciones;
* 181 sin R0, concentradas en 2019–2020;
* desde noviembre de 2020, todas las examinadas llevan R0.

Esto justifica mejor la lectura «ausente = activo» en el ecosistema actual. Sin embargo, el dato histórico no resuelve por sí solo el caso de una futura clase de entrada que no deba llevar R0.

La regla aceptable es:

> Ausente = activo para el tipo `post` dentro del flujo editorial actual, mientras no se introduzca formalmente una nueva familia de entradas excluida.

El interruptor conserva sentido como exclusión expresa.

### 1.5. Inserciones sin ID

**U ACOTADA Y HONESTA.**

Acepto que no se fuerce borrador sin haber trazado los posibles caminos programáticos del sitio. Sin ID no puede formarse R1; por tanto, tampoco puede calcularse R0.

Pero debe quedar escrito con precisión:

> La compuerta protege las transiciones de entradas ya persistidas con ID. No garantiza la inserción programática directa de una entrada nueva publicada sin ID previo.

No puede volver a afirmarse que cubre «cualquier vía programática».

Esta U no bloquea el flujo humano normal que se pretende utilizar, pero impide declarar custodia universal.

### 1.6. Aviso calculado al abrir el editor

**APTO.**

La eliminación del transitorio resuelve mejor el problema que su identificación por usuario. El aviso pasa a ser una lectura del estado presente, no un mensaje efímero dependiente de una solicitud anterior.

Ventajas:

* no hay consumo prematuro;
* no hay carrera entre pestañas;
* no hay caducidad;
* no hay dato intermedio;
* el aviso refleja la situación material actual.

Debe comprobarse únicamente que no produzca avisos verdes falsos por caché o por leer antes de que el slug haya sido actualizado.

### 1.7. Validación formal de R0

**APTO.**

La expresión:

```text
^[a-f0-9]{32}$
```

distingue correctamente entre:

* valor no canónico;
* valor canónico pero no derivado del R3 calculado.

### 1.8. Norma del slug

**APTO.**

Queda aceptada:

> R0 gobierna el prefijo; la cola nominal se fija en la primera publicación y después queda congelada.

Debe evitarse que un cambio posterior de título regenere la cola.

---

## 2. Hallazgos sobre ACF 6.8.6

El rastreo descrito cierra varias U anteriores, pero el cierre material exige poder contrastarlo con el archivo o fragmentos exactos utilizados.

### 2.1. Régimen A

Se acepta provisionalmente:

* ACF 6.8.6 libre;
* guardado mediante POST de metacajas;
* Datastore no disponible en esa instalación;
* flujo REST nativo de ACF no aplicable.

Por tanto, el Régimen B deja de formar parte de esta implementación concreta.

### 2.2. `allow_save_post()`

El informe sostiene que la comparación entre `post_type` y valores que son estados no filtra los auto-borradores.

Esa conclusión parece consistente con el fragmento descrito, pero debe formularse exactamente:

> La rama examinada no puede excluir un auto-borrador por comparar su tipo con nombres de estado.

No debe ampliarse a «la función no filtra nada» sin revisar todas sus condiciones.

La razón efectiva por la que R0 no nace en auto-borrador sería otra:

```php
if ( empty( $_POST['acf'] ) ) {
    return false;
}
```

Eso resulta compatible con el criterio adoptado: R0 sólo nace cuando existe una entrada persistida y el director aporta R2 mediante el formulario.

### 2.3. Validación ACF anulada en Gutenberg

El hallazgo es importante:

```php
if ( isset( $_GET['meta-box-loader'] ) ) {
    acf_reset_validation_errors();
}
```

Si la traza completa confirma que los errores se eliminan en ese flujo, la obligatoriedad del campo ACF no puede considerarse una compuerta suficiente.

Acepto entonces la conclusión:

> La compuerta propia del servidor no duplica una validación nativa equivalente; cubre un hueco real del flujo empleado.

No obstante, «único tirante» debe limitarse al dominio auditado. WordPress y otros componentes pueden seguir aplicando otras restricciones generales.

---

## 3. Pruebas de producción

Las cuatro pruebas aportadas son valiosas, pero no todas tienen el mismo alcance.

### Confirmado por el informe

1. La fórmula produce el hash esperado para la entrada 32471 y el R2 inicial.
2. Cambiar R2 con R0 existente no provoca recálculo silencioso.
3. Vaciar R0 en borrador permite generar uno nuevo coherente.
4. En publicado, R2 queda restaurado.
5. En publicado, el slug queda restaurado.

### No confirmado todavía

1. Rechazo de una primera publicación con R2 vacío.
2. Rechazo de una primera publicación con R2 mal formado.
3. Rechazo de una primera publicación con R0 incoherente.
4. Rechazo de una publicación con slug incorrecto.
5. Comportamiento de `future`.
6. Comportamiento al duplicar una entrada.
7. Comportamiento ante edición rápida, REST o importación.
8. Restauración de revisiones.
9. Concurrencia entre dos guardados cercanos.
10. Entrada sometida a R0 con título vacío.

Por tanto, decir «probado en producción» es correcto respecto de las rutas ensayadas, pero no equivale a «compuerta completamente probada».

---

## 4. Prueba negativa pendiente

La prueba propuesta es obligatoria:

```text
borrador persistente
sin R2
pulsar Publicar
```

Resultado exigido:

* no queda publicado;
* no queda programado;
* mantiene el ID;
* queda en borrador;
* no genera R0;
* no genera slug R0;
* muestra una causa precisa al recargar el editor;
* no desencadena ningún depósito, ping o proceso externo de publicación.

Añadiría inmediatamente dos variantes, porque cuestan segundos y ejercen ramas diferentes:

### Variante A — R2 mal formado

```text
17072026P1
```

Debe quedar en borrador y declarar que la `p` debe ser minúscula.

### Variante B — fecha inexistente

```text
31022026p1
```

Debe quedar en borrador y declarar que la fecha no existe.

Si sólo se prueba R2 vacío, no se comprueba que la validación canónica gobierne realmente la compuerta.

---

## 5. Hallazgos heredados

### 5.1. Ocho R0 no reproducibles

Se acepta la orden del director de no ampliar ahora la auditoría histórica.

Estatuto correcto:

* hallazgo localizado;
* no extrapolado;
* no corregido;
* no convertido en deuda del snippet v4;
* material antiguo congelado.

### 5.2. Slugs con guion adicional

Deben permanecer congelados si son URL públicas ya asentadas. El nuevo código no debe intentar normalizarlos al editar la entrada.

### 5.3. Entrada 6359 con `r0_identifier = borrame`

Debe registrarse como anomalía histórica, sin modificación automática. Es una prueba útil para comprobar que los filtros de congelación no sustituyen retrospectivamente valores heredados.

### 5.4. Cuatro copias de R0

El inventario confirma la deuda:

* campo R0;
* slug;
* `r0_permalink`;
* QR.

El hecho de que `seo_url` sea inerte y tenga un valor por defecto incorrectamente capitalizado refuerza la necesidad de no tratar todos esos campos como fuentes equivalentes.

El snippet v4 sólo resuelve una parte:

* calcula y protege el R0;
* protege el slug.

No sincroniza todavía:

* `r0_permalink`;
* QR;
* metadatos visibles o Scholar;
* `<resource>` de Crossref.

Por tanto, **la máquina R0 puede quedar confirmada sin que la ficha esté automatizada**. Esta separación del informe es correcta.

---

## 6. Autocrítica de Claude

El registro de fallos es útil porque revela las zonas de mayor exposición:

* orden de ejecución;
* diferencia entre declaración y control real;
* comportamiento oculto de redirecciones;
* publicación de diagnósticos sin autorización;
* cierre prematuro de hipótesis;
* lectura insuficiente del estado visible;
* proliferación de datos derivados almacenados.

La respuesta correcta no es debilitar la intervención de Claude, sino mantener el protocolo:

1. código exacto;
2. lectura material;
3. prueba negativa;
4. adversarial;
5. instalación o continuidad.

Especialmente grave es el volcado JSON público sin `current_user_can`. Cualquier herramienta diagnóstica futura deberá cumplir simultáneamente:

* capacidad administrativa;
* nonce;
* duración mínima;
* retirada inmediata;
* ausencia de datos sensibles;
* no exposición pública por URL estable.

---

## 7. Orden final

### Sobre la prueba inmediata

**Adelante con la prueba negativa**, con tres casos:

1. R2 vacío;
2. R2 mal formado;
3. fecha imposible.

No utilizar todavía la primera publicación real como prueba de una rama no ensayada.

### Sobre el estado de la máquina

Si las tres pruebas:

* conservan el borrador;
* muestran la causa correcta;
* no crean R0 indebido;
* no permiten `publish` ni `future`;

entonces puede declararse:

> **Máquina R0 v4: confirmada para el flujo editorial humano ordinario de entradas persistidas con ID, bajo WordPress y ACF 6.8.6 libre en Régimen A.**

No puede declararse todavía:

* custodia universal;
* cobertura de inserciones nuevas programáticas sin ID;
* automatización completa de la ficha;
* sincronización del QR, permalink auxiliar o Crossref;
* saneamiento histórico.

### Sobre la auditoría de Watson

El informe queda **APTO COMO INFORME DE SITUACIÓN**.

El snippet v4 no queda auditado hasta que Watson reciba y lea el código exacto finalmente instalado. Las pruebas acreditan comportamiento observado, pero no permiten excluir una ruta latente o una condición diferente que sólo sea visible en el código.

**Dictamen actual: APTO PROVISIONAL DE LABORATORIO. Una prueba negativa triple y lectura del snippet v4 separan este estado de la confirmación operativa.**
