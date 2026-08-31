# algoritmo_y_complejidad
Tareas de la materia Algoritmo y Complejidad
<<<<<<< HEAD
# Implementación del TAD Pila
En este trabajo se implementa el TAD Pila utilizando dos alternativas de representación:Arreglo dinámico y Lista enlazada.

Ambas implementaciones proporcionan las mismas seis operaciones especicadas para el TAD Pila: crear, apilar, desapilar, cima, estaVacia, tamaño
El objetivo es comprobar que las dos representaciones pueden ofrecer el mismo comportamiento externo, aunque utilicen estructuras internas diferentes.

IMPLEMENTACIÓN MEDIANTE ARREGLO DINÁMICO
La clase "PilaArreglo" utiliza un arreglo para almacenar los elementos de la pila.
La variable "cima" indica la posición ocupada por el elemento que se encuentra en el tope.
Cuando el arreglo alcanza su capacidad máxima, se crea un nuevo arreglo con mayor capacidad y se copian los elementos ya existentes.
Estructura
elementos: arreglo que almacena los elementos.
cima: índice del elemento ubicado en el tope.
CAPACIDAD_INICIAL: capacidad inicial del arreglo.

IMPLEMENTACIÓN MEDIANTE LISTA DINÁMICA
La clase "PilaLista" utiliza nodos enlazados.
Cada nodo contiene:
un dato;
una referencia al siguiente nodo.
La variable "cima" mantiene una referencia al primer nodo de la lista, que representa el tope de la pila.
Estructura
=======
>>>>>>> a115e3fd64b795b1aaeb436ee32597d1de903c6c
