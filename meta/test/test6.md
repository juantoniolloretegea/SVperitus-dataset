Empiece por fijar el estatuto de (g_D). Después, y sólo después, construya el verificador.

La decisión es ésta:

[
g_D:=\sqrt{\frac{1+\chi_D}{2}}
]

se declarará como **factor estructural constitutivo del dominio dentro del operador DOAN-(\Omega16)**.

No se presentará como una ley física universal, ni como consecuencia necesaria de un teorema previo, ni como la única función matemáticamente posible. Tampoco se dejará en (U), porque su definición, dominio, codominio, función dentro de la cadena y comportamiento están perfectamente determinados.

Su estatuto será:

1. (\chi_D) es la firma estructural de Ciclo Suceso del dominio, obtenida del registro etario correspondiente.
2. (g_D) es la transformación constitutiva que convierte esa firma en el factor lineal adimensional con el que se pondera el conteo etario:
   [
   \nu_D=N_Ag_D.
   ]
3. Se mantiene congelado entre acceso y frontera; la variación etaria la porta (N_A), no (g_D).
4. Para (0\leq\chi_D\leq1):
   [
   \frac1{\sqrt2}\leq g_D\leq1,
   ]
   es positivo, creciente, cóncavo y conserva el orden de los dominios.
5. La raíz es coherente con la gramática interna de linealización del aparato, que también aparece en:
   [
   \kappa_\Omega=\sqrt{\frac{\kappa_P}{\kappa_R}}.
   ]
   Esa regularidad se mostrará como consistencia interna, no como demostración de unicidad.

Por tanto, la (U) no corresponde a (g_D) como definición operativa. La (U) sólo afectaría a una afirmación más fuerte que no haremos:

[
\text{“esta es la única transformación posible o necesaria”.}
]

Esa proposición no está demostrada y no hace falta para definir ni ejecutar el instrumento.

Una vez congelado este estatuto, escriba el verificador reproducible. Debe implementar exactamente la definición declarada, no intentar justificarla por código.

Y una corrección terminológica: no hablaremos de «120 cifras exactas» cuando interviene la evaluación numérica de una integral elíptica. Hablaremos de **aritmética multiprecisión con precisión declarada**, cifras reproducidas y residual controlado. Las identidades racionales o algebraicas sí pueden calificarse de exactas; la expansión decimal numérica debe llevar precisión de trabajo, criterio de redondeo y residual.

Orden autorizado:

1. ficha formal de (g_D);
2. especificación de entradas, unidades y salidas;
3. verificador multiprecisión;
4. pruebas positivas, inversas y adversariales;
5. depósito reproducible;
6. artículo;
7. selección de revista.

Así que empiece por una ficha breve y cerrada del estatuto constitutivo de (g_D). Después pase directamente al código.
