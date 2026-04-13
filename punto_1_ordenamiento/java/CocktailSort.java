public class CocktailSort {

    /**
     * Ordena un arreglo usando Cocktail Sort.
     *
     * Este algoritmo recorre el arreglo en dos direcciones:
     * de izquierda a derecha y luego de derecha a izquierda.
     */
    public static void cocktailSort(int[] a) {
        boolean swapped = true;
        int start = 0;
        int end = a.length - 1;

        while (swapped) {
            // Se reinicia la bandera al comenzar la pasada
            swapped = false;

            // Recorrido de izquierda a derecha
            for (int i = start; i < end; i++) {
                if (a[i] > a[i + 1]) {
                    int temp = a[i];
                    a[i] = a[i + 1];
                    a[i + 1] = temp;
                    swapped = true;
                }
            }

            // Si no hubo intercambios, ya está ordenado
            if (!swapped) {
                break;
            }

            // Se reinicia la bandera para la pasada de regreso
            swapped = false;

            // El último elemento ya quedó en su posición correcta
            end--;

            // Recorrido de derecha a izquierda
            for (int i = end - 1; i >= start; i--) {
                if (a[i] > a[i + 1]) {
                    int temp = a[i];
                    a[i] = a[i + 1];
                    a[i + 1] = temp;
                    swapped = true;
                }
            }

            // El menor elemento ya quedó en su posición correcta
            start++;
        }
    }
}