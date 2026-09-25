class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
    def insertar(self, dato):
        self.raiz = self._insertar(self.raiz, dato)
    def _insertar(self, nodo, dato):
        if nodo is None:
            return NodoArbol(dato)
        if dato < nodo.dato:
            nodo.izquierdo = self._insertar(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            nodo.derecho = self._insertar(nodo.derecho, dato)
        return nodo
    def buscar(self, dato):
        return self._buscar(self.raiz, dato)
    def _buscar(self, nodo, dato):
        if nodo is None:
            return False
        if dato == nodo.dato:
            return True
        if dato < nodo.dato:
            return self._buscar(nodo.izquierdo, dato)
        else:
            return self._buscar(nodo.derecho, dato)
    def eliminar(self, dato):
        self.raiz = self._eliminar(self.raiz, dato)
    def _eliminar(self, nodo, dato):
        if nodo is None:
            return None
        if dato < nodo.dato:
            nodo.izquierdo = self._eliminar(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            nodo.derecho = self._eliminar(nodo.derecho, dato)
        else:
            if nodo.izquierdo is None and nodo.derecho is None:
                return None
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo
            sucesor = self._minimo(nodo.derecho)
            nodo.dato = sucesor.dato
            nodo.derecho = self._eliminar(nodo.derecho, sucesor.dato)
        return nodo
    def _minimo(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual
    def preorden(self):
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado
    def _preorden(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self._preorden(nodo.izquierdo, resultado)
            self._preorden(nodo.derecho, resultado)
    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado
    def _inorden(self, nodo, resultado):
        if nodo is not None:
            self._inorden(nodo.izquierdo, resultado)
            resultado.append(nodo.dato)
            self._inorden(nodo.derecho, resultado)
    def postorden(self):
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado
    def _postorden(self, nodo, resultado):
        if nodo is not None:
            self._postorden(nodo.izquierdo, resultado)
            self._postorden(nodo.derecho, resultado)
            resultado.append(nodo.dato)
    def por_niveles(self):
        if self.raiz is None:
            return []
        cola = [self.raiz]
        resultado = []
        while cola:
            actual = cola.pop(0)
            resultado.append(actual.dato)
            if actual.izquierdo is not None:
                cola.append(actual.izquierdo)
            if actual.derecho is not None:
                cola.append(actual.derecho)
        return resultado

arbol = ArbolBinarioBusqueda()

valores = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 90]

for valor in valores:
    arbol.insertar(valor)

print("Preorden:", arbol.preorden())
print("Inorden:", arbol.inorden())
print("Postorden:", arbol.postorden())
print("Por niveles:", arbol.por_niveles())

print("Buscar 40:", arbol.buscar(40))
print("Buscar 100:", arbol.buscar(100))

arbol.eliminar(10)
arbol.eliminar(30)
arbol.eliminar(50)

print("Inorden después de eliminar:", arbol.inorden())