import java.io.File;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Locale;

public class Benchmark {

    pprivate static final String DATA_DIR = "../../data";
private static final String RESULTS_DIR = "../results";
private static final String RESULTS_FILE = RESULTS_DIR + "/resultados_java.csv";

    public static void main(String[] args) throws Exception {
        File resultsDirectory = new File(RESULTS_DIR);
        if (!resultsDirectory.exists()) {
            resultsDirectory.mkdirs();
        }

        try (PrintWriter writer = new PrintWriter(new FileWriter(RESULTS_FILE))) {
            writer.println("algoritmo,lenguaje,tamano,tiempo_ms,complejidad_teorica");

            File dataDirectory = new File(DATA_DIR);
            File[] files = dataDirectory.listFiles((dir, name) -> name.endsWith(".txt"));

            if (files == null || files.length == 0) {
                System.out.println("No se encontraron archivos en la carpeta data.");
                return;
            }

            Arrays.sort(files, Comparator.comparing(File::getName));

            for (File file : files) {
                int size = Integer.parseInt(file.getName().replace("data_", "").replace(".txt", ""));

                System.out.println("\nProcesando archivo: " + file.getName());

                // Lectura fuera de la medición
                int[] originalData = DataLoader.loadData(file.getPath());

                runBenchmark(writer, "Cocktail Sort", "O(n^2)", size, originalData.clone());
                runBenchmark(writer, "Dual-Pivot QuickSort", "O(n log n) promedio", size, originalData.clone());
                runBenchmark(writer, "Heap Sort", "O(n log n)", size, originalData.clone());
                runBenchmark(writer, "Merge Sort", "O(n log n)", size, originalData.clone());
                runBenchmark(writer, "Radix Sort", "O(n*d)", size, originalData.clone());
            }
        }

        System.out.println("\nResultados guardados en: " + RESULTS_FILE);
    }

    private static void runBenchmark(PrintWriter writer, String algorithm, String complexity, int size, int[] data) {
        if (size == 1000000 && algorithm.equals("Cocktail Sort")) {
            System.out.println("Saltando Cocktail Sort para 1000000 por tiempo excesivo");
            writer.printf(
                Locale.US,
                "%s,Java,%d,%s,%s%n",
                algorithm,
                size,
                "No ejecutado",
                complexity
            );
            return;
        }

        System.out.println("Iniciando " + algorithm + " con tamaño " + size + "...");

        long startTime = System.nanoTime();

        switch (algorithm) {
            case "Cocktail Sort":
                CocktailSort.cocktailSort(data);
                break;

            case "Dual-Pivot QuickSort":
                if (data.length > 0) {
                    DualPivotQuickSort.dualPivotQuickSort(data, 0, data.length - 1);
                }
                break;

            case "Heap Sort":
                HeapSort.heapSort(data);
                break;

            case "Merge Sort":
                if (data.length > 0) {
                    MergeSort.mergeSort(data, 0, data.length - 1);
                }
                break;

            case "Radix Sort":
                if (data.length > 0) {
                    RadixSort.radixSort(data);
                }
                break;

            default:
                throw new IllegalArgumentException("Algoritmo no soportado: " + algorithm);
        }

        long endTime = System.nanoTime();
        double elapsedMs = (endTime - startTime) / 1_000_000.0;

        writer.printf(
            Locale.US,
            "%s,Java,%d,%.4f,%s%n",
            algorithm,
            size,
            elapsedMs,
            complexity
        );

        System.out.printf("%s | Java | %d => %.4f ms%n", algorithm, size, elapsedMs);
    }
}