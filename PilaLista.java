public class PilaLista<T> {

    private Nodo<T> cima;
    private int cantidad;

    // crear()
    public PilaLista() {
        cima = null;
        cantidad = 0;
    }

    // crear()
    public static <T> PilaLista<T> crear() {
        return new PilaLista<>();
    }

    // apilar()
    public PilaLista<T> apilar(T x) {

        Nodo<T> nuevo = new Nodo<>(x);

        nuevo.siguiente = cima;
        cima = nuevo;

        cantidad++;

        return this;
    }

    // desapilar()
    public PilaLista<T> desapilar() {

        if (estaVacia()) {
            throw new IllegalStateException(
                "No se puede desapilar: la pila está vacía."
            );
        }

        cima = cima.siguiente;
        cantidad--;

        return this;
    }

    // cima()
    public T cima() {

        if (estaVacia()) {
            throw new IllegalStateException(
                "No se puede consultar la cima: la pila está vacía."
            );
        }

        return cima.dato;
    }

    // estaVacia()
    public boolean estaVacia() {
        return cima == null;
    }

    // tamaño()
    public int tamaño() {
        return cantidad;
    }
}
