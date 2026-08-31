#Fragmento 1: Acceso directo
def ultimo_elemento(lista):
    if len(lista) == 0:
        return None
    return lista[-1]

#Fragmento 2: Búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

#Fragmento 3: Detección de duplicados (Fuerza bruta)
def tiene_duplicados(lista):
    n = len(lista)

    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] == lista[j]:
                return True

    return False

#Fragmento 4: División sucesiva
def divisiones_sucesivas(n):
    contador = 0
    while n > 1:
        n = n / 2
        contador += 1
    return contador

#Fragmento 5: Búsqueda binaria
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

#Fragmento 6: Fibonacci ineficiente
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

#Fragmento 7: Iteración anidada con saltos
def iteracion_saltos(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            
#Fragmento 8: Procesamiento de múltiples conjuntos
def procesar_listas(lista_N, lista_M):
    suma = 0
    producto = 1

    for elemento in lista_N:
        suma += elemento

    for elemento in lista_M:
        producto *= elemento

    return suma, producto
