public class Main {

    public static void main(String[] args) {

        probarPilaArreglo();
        probarPilaLista();
        compararImplementaciones();
        probarErrores();
    }

    public static void probarPilaArreglo() {

        System.out.println("======================================");
        System.out.println("     PILA IMPLEMENTADA CON ARREGLO");
        System.out.println("======================================");

        PilaArreglo<Integer> pila = PilaArreglo.crear();

        System.out.println("1. crear()");
        System.out.println("Pila creada correctamente.");
        System.out.println("estaVacia(): " + pila.estaVacia());

        System.out.println("\n2. apilar()");
        pila.apilar(10);
        pila.apilar(20);
        pila.apilar(30);
        System.out.println("Elementos agregados: 10, 20, 30");

        System.out.println("\n3. cima()");
        System.out.println("cima(): " + pila.cima());

        System.out.println("\n4. tamaño()");
        System.out.println("tamaño(): " + pila.tamaño());

        System.out.println("\n5. desapilar()");
        pila.desapilar();
        System.out.println("Elemento de cima eliminado.");
        System.out.println("Nueva cima(): " + pila.cima());

        System.out.println("\n6. estaVacia()");
        System.out.println("estaVacia(): " + pila.estaVacia());

        System.out.println();
    }

    public static void probarPilaLista() {

        System.out.println("======================================");
        System.out.println("     PILA IMPLEMENTADA CON LISTA");
        System.out.println("======================================");

        PilaLista<Integer> pila = PilaLista.crear();

        System.out.println("1. crear()");
        System.out.println("Pila creada correctamente.");
        System.out.println("estaVacia(): " + pila.estaVacia());

        System.out.println("\n2. apilar()");
        pila.apilar(10);
        pila.apilar(20);
        pila.apilar(30);
        System.out.println("Elementos agregados: 10, 20, 30");

        System.out.println("\n3. cima()");
        System.out.println("cima(): " + pila.cima());

        System.out.println("\n4. tamaño()");
        System.out.println("tamaño(): " + pila.tamaño());

        System.out.println("\n5. desapilar()");
        pila.desapilar();
        System.out.println("Elemento de cima eliminado.");
        System.out.println("Nueva cima(): " + pila.cima());

        System.out.println("\n6. estaVacia()");
        System.out.println("estaVacia(): " + pila.estaVacia());

        System.out.println();
    }

    public static void compararImplementaciones() {

        System.out.println("======================================");
        System.out.println("       COMPARACIÓN DE RESULTADOS");
        System.out.println("======================================");

        PilaArreglo<Integer> arreglo = PilaArreglo.crear();
        PilaLista<Integer> lista = PilaLista.crear();

        int[] datos = {5, 10, 15, 20, 25};

        for (int dato : datos) {
            arreglo.apilar(dato);
            lista.apilar(dato);
        }

        boolean resultadosIguales =
                arreglo.cima().equals(lista.cima())
                && arreglo.tamaño() == lista.tamaño()
                && arreglo.estaVacia() == lista.estaVacia();

        System.out.println("Cima arreglo: " + arreglo.cima());
        System.out.println("Cima lista: " + lista.cima());

        System.out.println("Tamaño arreglo: " + arreglo.tamaño());
        System.out.println("Tamaño lista: " + lista.tamaño());

        System.out.println(
                "¿Mismos resultados? " + resultadosIguales
        );

        System.out.println();
    }

    public static void probarErrores() {

        System.out.println("======================================");
        System.out.println("         MANEJO DE PRECONDICIONES");
        System.out.println("======================================");

        PilaArreglo<Integer> arreglo = PilaArreglo.crear();

        try {
            arreglo.desapilar();
        } catch (IllegalStateException e) {
            System.out.println("Arreglo - desapilar(): "
                    + e.getMessage());
        }

        try {
            arreglo.cima();
        } catch (IllegalStateException e) {
            System.out.println("Arreglo - cima(): "
                    + e.getMessage());
        }

        PilaLista<Integer> lista = PilaLista.crear();

        try {
            lista.desapilar();
        } catch (IllegalStateException e) {
            System.out.println("Lista - desapilar(): "
                    + e.getMessage());
        }

        try {
            lista.cima();
        } catch (IllegalStateException e) {
            System.out.println("Lista - cima(): "
                    + e.getMessage());
        }
    }
}