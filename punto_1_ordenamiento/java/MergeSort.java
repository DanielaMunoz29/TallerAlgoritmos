public class MergeSort {

    /**
     * Mezcla dos subarreglos ordenados dentro de arr.
     *
     * Primer subarreglo: arr[left..mid]
     * Segundo subarreglo: arr[mid+1..right]
     */
    public static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        // Arreglos temporales
        int[] L = new int[n1];
        int[] R = new int[n2];

        // Copia los datos a los arreglos temporales
        for (int i = 0; i < n1; i++) {
            L[i] = arr[left + i];
        }

        for (int j = 0; j < n2; j++) {
            R[j] = arr[mid + 1 + j];
        }

        int i = 0;
        int j = 0;
        int k = left;

        // Mezcla los arreglos temporales de vuelta en arr[left..right]
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        // Copia los elementos restantes de L[], si hay
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        // Copia los elementos restantes de R[], si hay
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    /**
     * Ordena el arreglo usando Merge Sort.
     */
    public static void mergeSort(int[] arr, int left, int right) {
        if (left >= right) {
            return;
        }

        int mid = left + (right - left) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}