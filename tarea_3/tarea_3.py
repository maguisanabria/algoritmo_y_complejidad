# Fragmento 1: Acceso directo
def ultimo_elemento(lista):
    if len(lista) == 0:
        return None
    return lista[-1]
# Complejidad Big-O: O(1)
# Caso analizado: Peor caso.
# Justificación: El acceso al último elemento se realiza directamente por índice.
# La condición y el acceso tienen costo constante, sin depender del tamaño de la lista.


# Fragmento 2: Búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1
# Complejidad Big-O: O(n)
# Caso analizado: Peor caso.
# Justificación: En el peor caso se recorren todos los elementos de la lista
# porque el número buscado está al final o no se encuentra.


# Fragmento 3: Detección de duplicados (Fuerza bruta)
def tiene_duplicados(lista):
    n = len(lista)

    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] == lista[j]:
                return True
    return False
# Complejidad Big-O: O(n²)
# Caso analizado: Peor caso.
# Justificación: Hay dos ciclos anidados que comparan los elementos entre sí.
# En el peor caso se realizan todas las comparaciones posibles.


# Fragmento 4: División sucesiva
def divisiones_sucesivas(n):
    contador = 0
    while n > 1:
        n = n // 2
        contador += 1
    return contador
# Complejidad Big-O: O(log n)
# Caso analizado: Peor caso.
# Justificación: En cada iteración el valor de n se divide entre 2.
# La cantidad de iteraciones crece de forma logarítmica.


# Fragmento 5: Búsqueda binaria
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1
# Complejidad Big-O: O(log n)
# Caso analizado: Peor caso.
# Justificación: En cada paso se descarta la mitad del arreglo ordenado.
# El espacio de búsqueda se reduce a la mitad en cada iteración.


# Fragmento 6: Fibonacci ineficiente
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Complejidad Big-O: O(2^n)
# Caso analizado: Peor caso.
# Justificación: Cada llamada recursiva genera dos nuevas llamadas.
# La cantidad de llamadas aumenta de forma exponencial.


# Fragmento 7: Iteración anidada con saltos
def iteracion_saltos(n):
    for i in range(n + 1):
        j = 1
        while j < n:
            j *= 2
# Complejidad Big-O: O(n log n)
# Caso analizado: Peor caso.
# Justificación: El ciclo externo se ejecuta n veces y el interno
# realiza aproximadamente log n iteraciones al duplicar su variable.


# Fragmento 8: Procesamiento de múltiples conjuntos
def procesar_listas(lista_N, lista_M):
    suma = 0
    producto = 1
    for elemento in lista_N:
        suma += elemento
    for elemento in lista_M:
        producto *= elemento
    return suma, producto
# Complejidad Big-O: O(N + M)
# Caso analizado: Peor caso.
# Justificación: Se recorren completamente las dos listas en forma secuencial.
# Los costos de ambos recorridos se suman.
