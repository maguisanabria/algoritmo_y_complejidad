public class PilaArreglo<T> {

    private Object[] elementos; //se crea el arreglo
    private int cima; //indica el elemento superior

    private static final int CAPACIDAD_INICIAL = 5;

    public PilaArreglo() {
        elementos = new Object[CAPACIDAD_INICIAL];
        cima = -1;
    }

    // crear()
    public static <T> PilaArreglo<T> crear() {
        return new PilaArreglo<>();
    }

    // apilar()
    public PilaArreglo<T> apilar(T x) {

        if (cima == elementos.length - 1) {
            redimensionar();
        }

        cima++;
        elementos[cima] = x;

        return this;
    }

    // desapilar()
    public PilaArreglo<T> desapilar() {

        if (estaVacia()) {
            throw new IllegalStateException(
                "No se puede desapilar: la pila está vacía."
            );
        }

        elementos[cima] = null;
        cima--;

        return this;
    }

    // cima()
    @SuppressWarnings("unchecked")
    public T cima() {

        if (estaVacia()) {
            throw new IllegalStateException(
                "No se puede consultar la cima: la pila está vacía."
            );
        }

        return (T) elementos[cima];
    }

    // estaVacia()
    public boolean estaVacia() {
        return cima == -1;
    }

    // tamaño()
    public int tamaño() {
        return cima + 1;
    }

    // Aumenta la capacidad del arreglo
    private void redimensionar() {

        Object[] nuevoArreglo = new Object[elementos.length * 2];

        for (int i = 0; i <= cima; i++) {
            nuevoArreglo[i] = elementos[i];
        }

        elementos = nuevoArreglo;
    }
}