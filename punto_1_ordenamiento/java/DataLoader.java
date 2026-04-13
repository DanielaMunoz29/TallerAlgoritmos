import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class DataLoader {

    /**
     * Lee los datos desde un archivo de texto y los devuelve como arreglo.
     * Este tiempo NO se mide.
     */
    public static int[] loadData(String filePath) throws IOException {
        List<Integer> numbers = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;

            while ((line = reader.readLine()) != null) {
                numbers.add(Integer.parseInt(line.trim()));
            }
        }

        int[] data = new int[numbers.size()];

        for (int i = 0; i < numbers.size(); i++) {
            data[i] = numbers.get(i);
        }

        return data;
    }
}