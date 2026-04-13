public class DualPivotQuickSort {

    /**
     * Intercambia dos posiciones dentro del arreglo.
     */
    public static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /**
     * Ordena el arreglo usando Dual-Pivot QuickSort.
     *
     * Usa dos pivotes:
     * - uno izquierdo
     * - uno derecho
     *
     * Esto divide el arreglo en tres regiones y luego
     * ordena cada una recursivamente.
     */
    public static void dualPivotQuickSort(int[] arr, int low, int high) {
        if (low < high) {

            // piv[0] guarda la posición final del pivote izquierdo
            // piv[1] guarda la posición final del pivote derecho
            int[] piv = partition(arr, low, high);

            // Ordena la parte izquierda
            dualPivotQuickSort(arr, low, piv[0] - 1);

            // Ordena la parte central
            dualPivotQuickSort(arr, piv[0] + 1, piv[1] - 1);

            // Ordena la parte derecha
            dualPivotQuickSort(arr, piv[1] + 1, high);
        }
    }

    /**
     * Reorganiza el arreglo usando dos pivotes y devuelve
     * las posiciones finales de ambos.
     */
    public static int[] partition(int[] arr, int low, int high) {

        // Se asegura que el pivote izquierdo sea menor o igual al derecho
        if (arr[low] > arr[high]) {
            swap(arr, low, high);
        }

        // p es el pivote izquierdo, q es el pivote derecho
        int j = low + 1;
        int g = high - 1;
        int k = low + 1;
        int p = arr[low];
        int q = arr[high];

        while (k <= g) {

            // Si el elemento es menor que el pivote izquierdo,
            // va a la región izquierda
            if (arr[k] < p) {
                swap(arr, k, j);
                j++;
            }

            // Si el elemento es mayor o igual al pivote derecho,
            // va a la región derecha
            else if (arr[k] >= q) {
                while (arr[g] > q && k < g) {
                    g--;
                }

                swap(arr, k, g);
                g--;

                // Después del intercambio, puede que el elemento
                // también pertenezca a la región izquierda
                if (arr[k] < p) {
                    swap(arr, k, j);
                    j++;
                }
            }

            k++;
        }

        j--;
        g++;

        // Lleva los pivotes a sus posiciones correctas
        swap(arr, low, j);
        swap(arr, high, g);

        // Devuelve las posiciones finales de ambos pivotes
        return new int[] { j, g };
    }
}