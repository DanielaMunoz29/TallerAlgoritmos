import java.util.Arrays;

public class TestCorrectness {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
        int[] targets = {10, 50, 100, 5, 105};

        for (int x : targets) {
            int b = SearchAlgorithms.busquedaBinaria(arr, x);
            int t = SearchAlgorithms.busquedaTernaria(arr, x);
            int j = SearchAlgorithms.jumpSearch(arr, x);

            System.out.printf("Target %d -> Bin: %d, Ter: %d, Jump: %d%n", x, b, t, j);
            
            int expected = -1;
            for(int i=0; i<arr.length; i++) if(arr[i] == x) expected = i;
            
            if (b != expected || t != expected || j != expected) {
                System.out.println("ERROR for target " + x);
            }
        }
        System.out.println("Pruebas de corrección terminadas.");
    }
}
