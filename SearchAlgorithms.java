
/**
 * Clase que contiene las implementaciones de los algoritmos de búsqueda requeridos.
 */
public class SearchAlgorithms {

    /**
     * Búsqueda Binaria - O(log n)
     * Divide el arreglo en dos mitades en cada paso.
     */
    public static int busquedaBinaria(int[] arr, int x) {
        int izquierda = 0, derecha = arr.length - 1;

        while (izquierda <= derecha) {
            int medio = izquierda + (derecha - izquierda) / 2;

            if (arr[medio] == x)
                return medio;

            if (arr[medio] < x)
                izquierda = medio + 1;
            else
                derecha = medio - 1;
        }
        return -1;
    }

    /**
     * Búsqueda Ternaria - O(log n)
     * Divide el arreglo en tres partes iguales en cada paso.
     */
    public static int busquedaTernaria(int[] arr, int x) {
        int l = 0, r = arr.length - 1;
        while (r >= l) {
            int mid1 = l + (r - l) / 3;
            int mid2 = r - (r - l) / 3;

            if (arr[mid1] == x) return mid1;
            if (arr[mid2] == x) return mid2;

            if (x < arr[mid1]) {
                r = mid1 - 1;
            } else if (x > arr[mid2]) {
                l = mid2 + 1;
            } else {
                l = mid1 + 1;
                r = mid2 - 1;
            }
        }
        return -1;
    }

    /**
     * Jump Search - O(sqrt(n))
     * Salta por bloques de tamaño sqrt(n) y luego realiza búsqueda lineal.
     */
    public static int jumpSearch(int[] arr, int x) {
        int n = arr.length;
        int step = (int) Math.floor(Math.sqrt(n));
        int prev = 0;

        while (arr[Math.min(step, n) - 1] < x) {
            prev = step;
            step += (int) Math.floor(Math.sqrt(n));
            if (prev >= n) return -1;
        }

        while (arr[prev] < x) {
            prev++;
            if (prev == Math.min(step, n)) return -1;
        }

        if (arr[prev] == x) return prev;
        
        return -1;
    }
}
