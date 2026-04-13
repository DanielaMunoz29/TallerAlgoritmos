public class HeapSort {

    /**
     * Convierte en heap el subárbol cuya raíz está en la posición i.
     *
     * @param arr arreglo a ordenar
     * @param n tamaño actual del heap
     * @param i índice de la raíz del subárbol
     */
    public static void heapify(int[] arr, int n, int i) {

        // Se asume inicialmente que la raíz es el mayor
        int largest = i;

        // Índice del hijo izquierdo
        int l = 2 * i + 1;

        // Índice del hijo derecho
        int r = 2 * i + 2;

        // Si el hijo izquierdo existe y es mayor que la raíz
        if (l < n && arr[l] > arr[largest]) {
            largest = l;
        }

        // Si el hijo derecho existe y es mayor que el mayor actual
        if (r < n && arr[r] > arr[largest]) {
            largest = r;
        }

        // Si el mayor no es la raíz, se intercambian
        if (largest != i) {
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;

            // Se aplica heapify recursivamente al subárbol afectado
            heapify(arr, n, largest);
        }
    }

    /**
     * Ordena el arreglo usando Heap Sort.
     *
     * @param arr arreglo a ordenar
     */
    public static void heapSort(int[] arr) {
        int n = arr.length;

        // Construye el heap máximo
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        // Extrae uno a uno los elementos del heap
        for (int i = n - 1; i > 0; i--) {

            // Mueve la raíz actual (el mayor) al final
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // Reconstruye el heap con el tamaño reducido
            heapify(arr, i, 0);
        }
    }
}