import java.io.*;
import java.util.*;

/**
 * Benchmark de algoritmos de búsqueda en Java (lenguaje compilado).
 * Exporta resultados a CSV y JSON.
 */
public class MainBusqueda {

    private static final int[] SIZES = {10000, 100000, 1000000};
    private static final String DATA_DIR = "data";

    public static void main(String[] args) throws IOException {
        System.out.println("==================================================");
        System.out.println("   BENCHMARK DE ALGORITMOS DE BÚSQUEDA (Java)");
        System.out.println("==================================================");
        System.out.printf("%-12s | %-15s | %-15s | %-12s%n",
                "Tamaño", "Binaria (ns)", "Ternaria (ns)", "Jump (ns)");
        System.out.println("----------------------------------------------------------");

        List<long[]> rows = new ArrayList<>();

        for (int size : SIZES) {
            int[] data = loadOrPrepareSortedData(size);
            if (data == null) continue;

            int target = data[data.length - 1]; // peor caso

            // Calentamiento JVM
            SearchAlgorithms.busquedaBinaria(data, target);
            SearchAlgorithms.busquedaTernaria(data, target);
            SearchAlgorithms.jumpSearch(data, target);

            long start, timeBinaria, timeTernaria, timeJump;

            start = System.nanoTime();
            SearchAlgorithms.busquedaBinaria(data, target);
            timeBinaria = System.nanoTime() - start;

            start = System.nanoTime();
            SearchAlgorithms.busquedaTernaria(data, target);
            timeTernaria = System.nanoTime() - start;

            start = System.nanoTime();
            SearchAlgorithms.jumpSearch(data, target);
            timeJump = System.nanoTime() - start;

            System.out.printf("%-12d | %-15d | %-15d | %-12d%n",
                    size, timeBinaria, timeTernaria, timeJump);

            rows.add(new long[]{size, timeBinaria, timeTernaria, timeJump});
        }

        System.out.println("==================================================");

        exportTxt(rows);
        exportCsv(rows);
        exportJson(rows);
    }

    // ── Carga de datos ────────────────────────────────────────────────────────

    private static int[] loadOrPrepareSortedData(int size) {
        String inputPath = DATA_DIR + "/data_" + size + ".txt";
        String sortedPath = DATA_DIR + "/data_sorted_" + size + ".txt";
        File sortedFile = new File(sortedPath);

        if (sortedFile.exists()) {
            return loadData(sortedPath, size);
        } else {
            System.out.println("Ordenando datos para tamaño " + size + "...");
            int[] data = loadData(inputPath, size);
            if (data == null) return null;
            Arrays.sort(data);
            saveData(sortedPath, data);
            return data;
        }
    }

    private static int[] loadData(String path, int size) {
        int[] data = new int[size];
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            String line;
            int i = 0;
            while ((line = br.readLine()) != null && i < size)
                data[i++] = Integer.parseInt(line.trim());
            return data;
        } catch (IOException e) {
            System.err.println("Error cargando: " + path);
            return null;
        }
    }

    private static void saveData(String path, int[] data) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(path))) {
            for (int val : data) bw.write(val + "\n");
        } catch (IOException e) {
            System.err.println("Error guardando: " + path);
        }
    }

    // ── Exportación ───────────────────────────────────────────────────────────

    private static void exportTxt(List<long[]> rows) throws IOException {
        try (PrintWriter pw = new PrintWriter(new FileWriter("results_final.txt"))) {
            pw.println("==================================================");
            pw.println("   BENCHMARK DE ALGORITMOS DE BÚSQUEDA");
            pw.println("==================================================");
            pw.printf("%-12s | %-15s | %-15s | %-12s%n",
                    "Tamaño", "Binaria (ns)", "Ternaria (ns)", "Jump (ns)");
            pw.println("-------------------------------------------------------------------------");
            for (long[] r : rows)
                pw.printf("%-12d | %-15d | %-15d | %-12d%n", r[0], r[1], r[2], r[3]);
            pw.println("==================================================");
        }
        System.out.println("Resultados exportados a results_final.txt");
    }

    private static void exportCsv(List<long[]> rows) throws IOException {
        try (PrintWriter pw = new PrintWriter(new FileWriter("results_java.csv"))) {
            pw.println("language,size,binary_ns,ternary_ns,jump_ns");
            for (long[] r : rows)
                pw.printf("Java,%d,%d,%d,%d%n", r[0], r[1], r[2], r[3]);
        }
        System.out.println("Resultados exportados a results_java.csv");
    }

    private static void exportJson(List<long[]> rows) throws IOException {
        try (PrintWriter pw = new PrintWriter(new FileWriter("results_java.json"))) {
            pw.println("[");
            for (int i = 0; i < rows.size(); i++) {
                long[] r = rows.get(i);
                pw.printf("  {\"language\":\"Java\",\"size\":%d,\"binary_ns\":%d,\"ternary_ns\":%d,\"jump_ns\":%d}%s%n",
                        r[0], r[1], r[2], r[3], i < rows.size() - 1 ? "," : "");
            }
            pw.println("]");
        }
        System.out.println("Resultados exportados a results_java.json");
    }
}
