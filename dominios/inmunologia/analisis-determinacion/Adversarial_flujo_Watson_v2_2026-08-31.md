# Adversarial al flujo Watson v2
**Pieza atacada:** `flujo-gobernado-inmunologia-determinista-v2.html` (114.370 bytes), título interno «Dominio clínico determinista de inmunología: ruta de constitución, validación y cierre».  
**Estatuto de la pieza:** propuesta de gobierno. No es doctrina, no es perímetro, no es hecho de trabajo del autor.  
**Corte del ataque:** 31-08-2026.  
**Método:** cita del texto propuesto + contraste con (i) órdenes del autor ya declaradas, (ii) normas de repositorio ya leídas en A1, (iii) matemática de la nomenclatura 1×n / 3^n, (iv) sumisiones y semillas ya fijadas.  
**No se adopta un flujo sustituto.** G0 sigue cerrado.

Veredicto global de la propuesta: **no pasa entero**.  
Pasa como lista de precauciones clínicas.  
Falla como «camino único» que constituye dominio, cierra ambigüedades no autorizadas y empalma el resultado con R2.

---

## 0. Qué resiste (para no tumbar lo que está bien)

Estas piezas del v2 están alineadas con lo ya declarado y no se atacan:

- Fundamentos y Origen de U como invariantes; álgebra sólo por ampliación expresa o error demostrado.
- Autorización humana previa a inferir o modificar.
- Semillas ≠ dominio (4A, checklist 7).
- Consecuencia ≠ probabilidad ≠ acción (1A, checklist 4).
- Currículo ≠ prueba de daño (3A).
- Dato nulo del repositorio ≠ U por identidad (5A, tabla lógica).
- Tiempo y estadística fuera del núcleo, como dato o tipo externo (6A, pestaña frontera).
- Composición dirigida; el orden puede cambiar la advertencia (5B, error de categoría «mismos módulos»).
- Validación retrospectiva ≠ autorización asistencial (D2, bloqueante clínico).
- Append-only (7B).
- Autocontención del manuscrito (1B, intersección 1, checklist 19).
- Protocolo de ficha de repositorio por dimensiones (gobierno, población, unidad, variables, tiempo, desenlaces, calidad, validación, singulares).
- Cardinalidad correcta en los dos ejemplos: \(3^{9}=19683\), \(3^{25}=847288609443\); instancia = vector fila, no matriz \(b\times b\).

Eso no salva el documento. Un flujo se juzga por lo que **cierra**, no por lo que **recita**.

---

## 1. El título y el «camino único» fusionan tres objetos

**Texto atacado.** H1: «Dominio clínico determinista de inmunología». Lema del mapa: «Camino único gobernado». Puerta final: revisión hostil «y decisión humana sobre R2».

**Por qué colapsa.** El autor separó, y el dictamen ES×IMMUNO del 27-08 ya tumbó la fusión:

1. dominio profesional declarado;
2. dominio clínico operativo (episodio);
3. centinela del Lenguaje (ES×IMMUNO) *antes* de exigencias a R2-1.

Un camino serial 0→7 que termina en R2 convierte (1)+(2)+(3) en un solo Q.  
Efecto demostrable:

- el centinela del Lenguaje (identificadores SVP, letter/Unicode, paridad Rust/WASM, S finito, hold-out trasplante) **desaparece del mapa**;
- la constitución clínica queda como condición de R2, que es exactamente la ambigüedad **G2** que el autor dejó abierta y prohibió inferir;
- «determinista» en el título, pese a la corrección posterior en intersección 3, es el lema que un revisor leerá primero.

**Qué hay que mejorar.** Tres carriles con interfaces, no un camino único. R2 no es la puerta final de este HTML. Si se menciona R2, debe figurar como *fuera de alcance salvo G0*, no como etapa 7.

**Veredicto:** colapsa como arquitectura de gobierno. Resiste como precaución local de no invadir el juicio médico.

---

## 2. Cierre ilícito de G1 y G2

### G1 — ¿la derivación puede reabrir las semillas?

**Texto atacado.** 4A: las representaciones (25,5) «fijadas en ITI V.1» «se usan para probar trazabilidad…». «Ninguna de las tres lo agota, dimensiona o decide.»  
5B: «El inventario clínico determina longitudes de vectores, módulos, puentes y orden.»

**Demostración del cierre.** Hay dos proposiciones distintas:

- P: las semillas no agotan el dominio. (Declarada por el autor. Resiste.)
- Q: las longitudes y la lista de parámetros de esas filas 1×25 quedan congeladas y la arquitectura nueva se deriva *después*, sin reabrirlas. (No declarada.)

4A+5B afirman Q. El paso de P a Q no está autorizado.  
Si mañana el inventario exige 27 variables en el mismo episodio, 5B obliga a *otro* vector y 4A impide tocar el 1×25. Esa es una decisión de diseño, no un hecho.

**Qué hay que mejorar.** Restaurar G1 como parada ámbar: «semillas no deciden el dominio» ≠ «semillas intocables» ≠ «semillas plantilla». Las tres lecturas deben permanecer abiertas.

### G2 — ¿el contraste clínico condiciona R2?

**Texto atacado.** Puerta final: el trabajo debe ser autocontenido «Sólo después, y con autorización expresa, puede plantearse el paso del Lenguaje a R2.»

**Demostración.** Condicionar R2 al cierre biomédico de *este* camino es resolver G2 en sentido afirmativo. El Lenguaje tiene R0/R1 cerrados y R2 abierto por persistencia material, objeto distinto. Ligarlos sin G0 mezcla O2 y O3.

**Veredicto:** colapsa. Es el mismo género de inferencia que el autor prohibió.

---

## 3. Error matemático de categoría: «n = b²» como ley

**Texto atacado.** Pestaña lógica, veredicto: «El segundo término b satisface n = b², pero no es número de filas.»  
Checklist 8: «¿Se distingue vector 1×n, parámetro b y espacio de 3ⁿ estados?»

**Hechos:**

- (9,3): \(9=3^2\). Instancia 1×9. \(|S|=3^9=19683\). Correcto.
- (25,5): \(25=5^2\). Instancia 1×25. \(|S|=3^{25}=847288609443\). Correcto.
- El autor fijó: (k,s) = una fila 1×k; estados \(s_{\text{alfabeto}}^k\). En las semillas el alfabeto de estado es ternario, luego \(3^k\). El segundo índice **no** es el tamaño del alfabeto.

**Demostración de que n = b² no es teorema aquí.**

1. De dos ejemplos con \(n=b^2\) no se sigue ∀ array, \(n=b^2\). Eso es generalización sobre una muestra de tamaño 2.
2. Si el inventario (5B) derivara un módulo de 12, 19 o 26 parámetros —T(25)=19 ya existe como conteo publicado de la semilla I y **no aparece en el v2**— la ecuación n=b² lo prohibiría sin haber demostrado que b es una ley del dominio clínico.
3. Confunde tres números distintos:
   - k = longitud del vector (columnas de la instancia);
   - alfabeto |\Sigma| = 3;
   - b = segundo índice de la notación histórica (capas / estratificación / otra función *no demostrada en este HTML*).
4. Checklist 8 convierte esa ecuación no demostrada en condición de «cierre» del manuscrito. Un ítem falso en la lista de revisión hostil **fabrica un rechazo** o **fabrica una doctrina**.

**Qué hay que mejorar.** Conservar: instancia 1×k, |S|=3^k, prohibido leer k×b como matriz rectangular.  
Suprimir o marcar como *conjetura no autorizada* cualquier «n=b²».  
Restaurar T(25)=19 como hecho de la semilla I, no como ley del dominio.

**Veredicto:** la distinción 1×n vs n×n **resiste**. La ley n=b² **colapsa**.

---

## 4. La misma letra aij nombra dos objetos

**Texto atacado.** 3B: «X = (aij): fila i = paciente/episodio; columna j = variable clínica.»  
Checklist 6: «¿Está claro qué representa cada fila y cada columna aij?»  
Pestaña lógica: X=(aij) matriz de datos N×p **y** s vector 1×n.

**Por qué es grave.** El autor exigió nomenclatura de extracción a1j = elemento de *una* fila constitutiva.  
Watson introduce, con razón, la matriz de *datos* (casos × variables). Pero reutiliza aij.  
Un revisor —o un programador— leerá X como «la matriz del sistema» y volverá a (25,5) = 25 pacientes × 5 variables. Eso es exactamente el error que el autor calificó de letal.

**Demostración de proceso.** El propio v2 dedica un bloqueante de ingeniería a «confundir (n,b) con una matriz b×b» y simultáneamente enseña aij como entrada de una matriz N×p. La pedagogía se anula sola.

**Qué hay que mejorar.** Tres símbolos disjuntos, declarados una vez:

- \(X=(x_{ij})\) matriz de observaciones (caso × variable cruda);
- \(s=(s_1,\ldots,s_k)\in\{0,1,U\}^k\) instancia ternaria de un episodio admitido;
- \(A=(a_{1j})_{j=1}^{k}\) fila constitutiva del módulo (la antigua «célula»), nunca N×k.

**Veredicto:** la separación instancia / matriz de datos / espacio de estados **resiste**. La indexación compartida **colapsa**.

---

## 5. D0 está mal calibrado y el HTML niega A1

**Texto atacado.**

- Puerta D0: «NO → se detiene la constitución clínica: queda una hipótesis formal, no un resultado biomédico.»
- Pie: «No se incorpora aquí ninguna fuente clínica concreta porque su búsqueda efectiva aún no ha sido autorizada.»
- 2A aún habla de «inventariar» como etapa futura.

**Hechos de trabajo del 31-08-2026 (declarados y ejecutados por orden del autor):**

- búsqueda autorizada;
- inventario A1 de once fuentes con norma leída;
- adversarial A1: ninguna adoptada; ninguna demostrada sobre el episodio de las semillas; ImmPort 2.5 prohíbe uso para tratamiento; REDIP/ESID no son descarga abierta; IEI ≠ IS farmacológica.

**Tres fallos.**

1. **Falsedad procesal.** Decir que la búsqueda «aún no ha sido autorizada» es falso a la hora en que existe el v2 en el mismo frente. Un instrumento de gobierno que no registra A1 no gobierna: va retrasado.
2. **D0 binario contra el propio fallback ya escrito.** El autor aceptó que, sin cohortes adecuadas, puede existir demostrador formal *sin* validación clínica. D0 debe ramificar (constitución clínica detenida / demostrador formal permitido / centinela del Lenguaje no arrastrado), no apagar todo el frente.
3. **Si D0 se aplicara hoy con A1 en la mano**, la rama clínica ya está en NO para el episodio semilla. El v2 no escribe ese estado. Deja el camino dibujado como si D0 estuviera por delante, no detrás.

**Qué hay que mejorar.** Una caja de estado A1: «inventario hecho, cero adopciones, cobertura del episodio = no demostrada». D0 con tres salidas, no dos. El pie del HTML debe dejar de negar la búsqueda ya hecha.

**Veredicto:** el protocolo de *ficha* de repositorio resiste. D0 y el pie **colapsan**.

---

## 6. 1A «decisión concreta que se pretende asistir» empuja a CDS

**Texto atacado.** 1A: población, escenario, usuario, «Decisión concreta que se pretende asistir.»  
H1: constitución, validación y cierre de un «dominio clínico».

**Contraste factual.**

- Documento 7 / IMMUNO-1: sin validación clínica ni uso asistencial.
- ImmPort User Agreement 2.5: datos no aptos para informar tratamiento.
- D2 del propio v2: la validación retrospectiva no autoriza uso asistencial.
- Objetivo inmediato ya compilado: centinela pequeño que tensiona el Lenguaje, no un sistema que asiste una decisión.

**Demostración.** Si 1A exige una decisión asistida, entonces:

- las fuentes A1 con cláusula 2.5 quedan fuera de esa intención;
- el manuscrito se presenta como CDS y hereda la carga regulatoria que las publicaciones históricas eludieron;
- contradice D2 dentro del mismo archivo.

**Qué hay que mejorar.** 1A debe partir de una *operación declarada* (alerta, cobertura, residual, certificado de omisión) y decir explícitamente si esa operación es o no asistencia a decisión de tratamiento. Hoy lo presupone.

**Veredicto:** colapsa como encuadre. La separación gravedad/probabilidad/acción resiste.

---

## 7. Intersección 2 borra el residual profesional

**Texto atacado.** «Sólo entra un candidato a parámetro si puede justificarse clínicamente, localizarse o derivarse legítimamente en datos y vincularse a una operación verificable.»

Leído como conjunción de tres condiciones (justificación ∧ dato ∧ operación), un conocimiento profesional exigido por currículo pero aún no presente en un repositorio **no entra**.  
El autor declaró que puede existir resto profesional no «celular» y que Π1 ≠ Π4.

**Demostración.** REDIP/ESID no cubren el episodio semilla (A1). ImmPort no está auditado SDY a SDY. Bajo intersección 2, el inventario 4B no puede admitir un parámetro clínicamente justificado cuya variable aún no existe en un dataset accesible. El residual queda prohibido en lugar de declarado.

**Qué hay que mejorar.** Tres colas, no una puerta:

- entra al *módulo operativo* sólo lo que cumple las tres;
- entra al *inventario profesional* lo justificado que aún no tiene dato (residual explícito);
- no entra ni al módulo ni al residual lo que no tiene ni justificación ni dato.

**Veredicto:** colapsa como criterio único de inclusión.

---

## 8. 0B eleva JavaScript a estatuto de implementación

**Texto atacado.** 0B: «Implementación: ITI V.1 y JavaScript de inmuno/inmuno2.»

**Hecho ya compilado.** Superficies: Rust/WASM `evaluate_immuno1()`, compositor `compose()`/`Γ(v)`, demo React/Babel con T(25)=19, ruta histórica. La demo JS **no** es prueba de paridad del motor. Python/JS/WASM antiguos son antecedentes.

**Por qué importa.** Si el flujo toma el JS como implementación de referencia, la puerta de fidelidad spec–código (incidente P02: dm=False, eGFR=90, marcadores ausentes → 0 contra la regla de incompleto) se evalúa contra el artefacto equivocado.

**Qué hay que mejorar.** Estatuto separado:

- especificación / ITI (si el autor la mantiene como tal);
- motor de referencia (el que se declare: no inferir cuál);
- superficies de inspección (JS, GUI);
- Lenguaje SV vigente (Gramática 0.2, IR 0.3), carril distinto.

P02 como compuerta de paridad **no está en el v2**. Debe estarlo antes de 5A.

**Veredicto:** colapsa el estatuto JS. La idea de estatutos separados resiste; la lista de 0B no.

---

## 9. 5A abre U sin regla por defecto

**Texto atacado.** «Tras admisibilidad, una insuficiencia puede transducirse a U con contexto, mecanismo y trazabilidad.»

**Contraste.** U atómica no tipada. Dato no capturado ≠ observación no admitida ≠ U. Insuficiencia representacional ≠ U.

El «puede» sin la frase «sólo si una regla versionada lo declara, y nunca por defecto» deja el mismo agujero de P02: una implementación transduce ausencia a un estado del alfabeto sin que la regla escrita lo autorice.

**Qué hay que mejorar.** Orden fijo y visible en el mapa, no sólo en la tabla lógica:

admisibilidad → (si no admisible: no hay estado) → aplicación de regla versionada → {0,1,U} o retención.  
U no es el cajón de la insuficiencia.

**Veredicto:** la negación «nulo ≠ U por identidad» resiste. La licencia de transducir insuficiencia a U **queda no demostrada** como regla general.

---

## 10. 0A convierte dos chats en etapa de constitución clínica

**Texto atacado.** Orden 0 / 0A: lectura triple de Español-Lenguaje-Inmuno e Inmuno VI como primer paso del camino clínico.

**Por qué sobra aquí.** Esa lectura ya fue ordenada a Watson y compilada. Reponerla como etapa 0 del *dominio clínico* mezcla arqueología de chat con constitución de episodio, población y datos.  
Un revisor biomédico no tiene esos chats. Si el flujo los necesita, viola intersección 1 (autocontención).

**Qué hay que mejorar.** 0A es prehistoria del gobierno interno, no caja del manuscrito ni del dominio. Fuera del camino clínico.

---

## 11. Piezas del frente que el v2 silencia

Demostrable por ausencia en el HTML leído:

| Pieza ya fijada o inventariada | En el v2 |
|---|---|
| T(25)=19 | Ausente |
| Puente P25 y compositor como artefacto, no fase | Ausente |
| Hold-out trasplante (falsador de saturación) | Ausente |
| Prohibición de IEI/alergia/autoinmunidad/laboratorio como constructoras simultáneas | Ausente |
| letter / identificadores SVP / paridad del Lenguaje | Ausente |
| ImmPort 2.5, seudónimo ESID, REDIP-RePER | Ausentes (y el pie niega la búsqueda) |
| P02 fidelidad spec–implementación | Ausente |
| n=625 no es tercer array | Ausente |
| Sumisiones activas no se reescriben | Ausente |
| G1, G2 como paradas no inferibles | Cerradas de hecho |

Un flujo de gobierno que no reserva sitio a lo ya cerrado obliga a reabrir laterales o a olvidarlos. Las dos cosas están prohibidas.

---

## 12. La lista de 20 casillas no es un criterio de saturación

**Texto atacado.** «Una casilla pendiente no se compensa con prosa… Se responde, se declara como limitación o se mantiene el proyecto detenido.» Marcas en `localStorage`.

**Ataque ya hecho el 27-08:** «cerrar por saturación» sin conjunto finito S y sin ΔS=∅ tras hold-out no es predicado.  
Veinte preguntas de revisor son un *instrumento*. No definen S.  
Además:

- el ítem 8 incorpora n=b² (falso como ley);
- el ítem 1 presupone «decisión asistida»;
- no hay ítem sobre solapamiento con sumisiones activas ni sobre cláusula de no tratamiento de las fuentes.

**Veredicto:** útil como lista de trabajo. **Colapsa** como puerta de cierre.

---

## 13. Drift léxico del perímetro

**Texto atacado.** Orden 0: «álgebra intermodular».  
El perímetro del autor es el PDF de *Álgebra de composición intercelular*.  
«Intermodular» no está autorizado como sustituto. Evitar «célula» no permite rebautizar el perímetro.

---

## 14. Dependencia de red en un instrumento «local»

El envoltorio carga `unpkg.com` (lucide, floating-ui). El autor pidió HTML evaluable en local. Si unpkg falla, el gobierno visual se degrada. Es un fallo menor de proceso, no clínico; se anota porque el propio v2 exige trazabilidad material y reproducibilidad (checklist 20).

---

## 15. Qué habría que cambiar, blanco sobre negro

No es un flujo nuevo. Es la lista de correcciones que el v2 necesita para no ser rechazado como gobierno:

1. Cambiar el H1: no «dominio clínico determinista de inmunología». Objeto = instrumento de gobierno de un recorte aún no cubierto por datos.
2. Romper el camino único. Tres carriles. R2 fuera.
3. Reabrir G1 y G2 como paradas. Quitar 5B como ley de longitudes.
4. Borrar n=b² o etiquetarla conjetura no autorizada. Restaurar T(25)=19.
5. Separar símbolos \(x_{ij}\), \(s_j\), \(a_{1j}\).
6. Registrar A1: búsqueda hecha, cero adopciones, episodio no cubierto de forma demostrada. Corregir el pie.
7. D0 ternario: clínica detenida / demostrador formal / centinela no arrastrado.
8. 1A sin presuponer asistencia a tratamiento. Declarar la operación.
9. Intersección 2 con cola de residual profesional.
10. JS degradado a superficie. P02 como compuerta antes de 5A.
11. 5A: U sólo por regla versionada, nunca por defecto de insuficiencia.
12. 0A fuera del camino clínico.
13. Reservar cajas para P25, compositor-artefacto, hold-out trasplante, letter/SVP, cláusulas 2.5 / GDPR / RePER.
14. Checklist 20 = ayuda, no S.
15. Restaurar el nombre del perímetro algebraico.

---

## 16. Dictamen

| Capa del v2 | Veredicto |
|---|---|
| Precauciones clínicas (consecuencia ≠ riesgo; currículo ≠ daño; no CDS retrospectivo) | Resiste |
| Distinción instancia 1×k / espacio 3^k / no matriz b×b | Resiste |
| Frontera estadística-temporal y protocolo de ficha de repositorio | Resiste |
| Camino único 0→7 que cierra en R2 | Colapsa |
| n=b² como ley y como ítem 8 de cierre | Colapsa |
| Cierre de G1/G2 | Colapsa |
| aij compartido datos/constitución | Colapsa |
| D0 binario + pie que niega A1 | Colapsa |
| 1A como decisión asistida | Colapsa |
| Intersección 2 como único ingreso | Colapsa |
| JS = implementación | Colapsa |
| Lista de 20 como saturación | Colapsa |

La propuesta mejora el flujo anterior en un punto estructural cierto: *no congelar parámetros antes de preguntar por datos*.  
Ese acierto no autoriza a constituir el dominio, a decidir las semillas, a imponer n=b² ni a gobernar R2.

No se sustituye el HTML. No se abre D0 como «SÍ». No se adopta repositorio. El siguiente cambio del flujo lo autoriza el autor.
