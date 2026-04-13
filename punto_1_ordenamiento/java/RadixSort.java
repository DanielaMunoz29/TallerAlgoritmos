import java.util.Arrays;

public class RadixSort {

    /**
     * Obtiene el valor máximo del arreglo.
     * Sirve para saber cuántos dígitos tiene el número más grande.
     */
    public static int getMax(int[] arr, int n) {
        int max = arr[0];

        for (int i = 1; i < n; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }

        return max;
    }

    /**
     * Aplica Counting Sort al arreglo según el dígito representado por exp.
     *
     * exp = 1   -> unidades
     * exp = 10  -> decenas
     * exp = 100 -> centenas
     */
    public static void countSort(int[] arr, int n, int exp) {
        int[] output = new int[n];
        int[] count = new int[10];

        Arrays.fill(count, 0);

        // Cuenta cuántas veces aparece cada dígito
        for (int i = 0; i < n; i++) {
            count[(arr[i] / exp) % 10]++;
        }

        // Convierte el conteo en posiciones acumuladas
        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }

        // Construye el arreglo de salida
        for (int i = n - 1; i >= 0; i--) {
            int digit = (arr[i] / exp) % 10;
            output[count[digit] - 1] = arr[i];
            count[digit]--;
        }

        // Copia el resultado al arreglo original
        for (int i = 0; i < n; i++) {
            arr[i] = output[i];
        }
    }

    /**
     * Ordena el arreglo usando Radix Sort.
     */
    public static void radixSort(int[] arr) {
        int n = arr.length;

        if (n == 0) {
            return;
        }

        // Obtiene el número máximo para saber cuántos dígitos procesar
        int max = getMax(arr, n);

        // Aplica counting sort por cada posición decimal
        for (int exp = 1; max / exp > 0; exp *= 10) {
            countSort(arr, n, exp);
        }
    }
}