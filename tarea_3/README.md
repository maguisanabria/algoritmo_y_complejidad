---
---
FRAGMENTO 1: ACCESO DIRECTO
- Complejidad: O(1)
- Caso analizado: Caso general / único acceso.
- Justificación: Se accede directamente al último elemento mediante su índice, sin recorrer la lista. La cantidad de elementos no cambia el tiempo de acceso.

FRAGMENTO 2: BÚSQUEDA LINEAL
- Complejidad: O(N)
- Caso analizado: Peor caso
- Justificación: En el peor caso, el elemento está al final o no existe, por lo que se recorren los N elementos de la lista. El ciclo realiza como máximo N comparaciones.

FRAGMENTO 3: DETECCIÓN DE DUPLICADOS - FUERZA BRUTA
- Complejidad: O(N²)
- Caso analizado: Peor caso
- Justificación: Se utilizan dos ciclos anidados que comparan los elementos entre sí. En el peor caso se realizan aproximadamente N² comparaciones.

FRAGMENTO 4: DIVISIÓN SUCESIVA
- Complejidad: O(log N)
- Caso analizado: Caso general
- Justificación: En cada iteración el valor de N se reduce a la mitad. Por eso, el número de iteraciones crece logarítmicamente respecto al tamaño inicial.

FRAGMENTO 5: BÚSQUEDA BINARIA
- Complejidad: O(log N)
- Caso analizado: Peor caso
- Justificación: En cada iteración se elimina aproximadamente la mitad del espacio de búsqueda. Por ello, como máximo se necesitan log₂(N) iteraciones.

FRAGMENTO 6: FIBONACCI INEFICIENTE
- Complejidad: O(2^N)
- Caso analizado: Peor caso
- Justificación: Cada llamada genera dos nuevas llamadas recursivas, creando un árbol de llamadas que crece exponencialmente. Se repiten muchos cálculos.

FRAGMENTO 7: ITERACIÓN ANIDADA CON SALTOS
- Complejidad: O(N log N)
- Caso analizado: Caso general
- Justificación: El ciclo externo se ejecuta N veces. El ciclo interno duplica su variable en cada paso, por lo que realiza log N iteraciones.

FRAGMENTO 8: PROCESAMIENTO DE MÚLTIPLES CONJUNTOS
- Complejidad: O(N + M)
- Caso analizado: Caso general
- Justificación: El primer ciclo recorre N elementos y el segundo recorre M elementos. Como son ciclos consecutivos y no anidados, sus costos se suman: N + M.