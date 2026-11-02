def ordenamiento_mezcla(arreglo):
    if len(arreglo) <= 1:
        return arreglo

    medio = len(arreglo) // 2

    izquierda = ordenamiento_mezcla(arreglo[:medio])
    derecha = ordenamiento_mezcla(arreglo[medio:])

    return mezclar(izquierda, derecha)


def mezclar(izquierda, derecha):
    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


numeros = [8, 3, 5, 1, 9, 2]

print("Arreglo original:", numeros)
print("Arreglo ordenado:", ordenamiento_mezcla(numeros))