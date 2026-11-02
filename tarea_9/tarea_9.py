def busqueda_secuencial(arreglo,numero):
    for i in range (len(arreglo)):
        if arreglo[i]==numero:
            return i
        return -1
    
def busqueda_binaria(arreglo,numero):
    inicio = 0
    fin = len(arreglo)-1
    while inicio <= fin:
        medio = (inicio+fin)//2
        if arreglo[medio]==numero:
            return medio
        elif arreglo[medio] < numero:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1
    
arreglo = [1, 3, 4, 6, 12, 15, 35, 44]
numero = 12

print("¿Qué tipo de búsqueda desea realizar?")
print("a. Búsqueda Secuencial")
print("b. Búsqueda Binaria")

opcion = input("Seleccione una opción: ").lower()
while opcion!="a" and opcion!="b":
    print("Opcion no válida. Intente de nuevo")
    opcion = input("Seleccione una opción: ").lower()
numero = int(input("Ingrese el número que desea buscar: "))

if opcion == "a":
    resultado = busqueda_secuencial(arreglo, numero)
elif opcion == "b":
    resultado = busqueda_binaria(arreglo, numero)
else:
    resultado = -1
    print("Opción no válida.")

if opcion == "a" or opcion == "b":
    if resultado != -1:
        print("Número encontrado en la posición:", resultado)
    else:
        print("Número no encontrado.")
