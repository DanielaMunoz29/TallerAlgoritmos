import csv
import os
import time

from sorting.cocktail_sort import cocktail_sort
from sorting.dual_pivot_quicksort import dual_pivot_quicksort
from sorting.heap_sort import heap_sort
from sorting.merge_sort import merge_sort
from sorting.radix_sort import radix_sort

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
RESULTS_DIR = os.path.join(BASE_DIR, "..", "results")
RESULTS_FILE = os.path.join(RESULTS_DIR, "resultados_python.csv")


def load_data(file_path):
    """
    Lee los números desde un archivo de texto.
    Este tiempo NO se mide.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return [int(line.strip()) for line in file]


def run_cocktail_sort(data):
    cocktail_sort(data)


def run_dual_pivot_quicksort(data):
    if len(data) > 0:
        dual_pivot_quicksort(data, 0, len(data) - 1)


def run_heap_sort(data):
    heap_sort(data)


def run_merge_sort(data):
    if len(data) > 0:
        merge_sort(data, 0, len(data) - 1)


def run_radix_sort(data):
    if len(data) > 0:
        radix_sort(data)


ALGORITHMS = {
    "Cocktail Sort": run_cocktail_sort,
    "Dual-Pivot QuickSort": run_dual_pivot_quicksort,
    "Heap Sort": run_heap_sort,
    "Merge Sort": run_merge_sort,
    "Radix Sort": run_radix_sort,
}

COMPLEXITIES = {
    "Cocktail Sort": "O(n^2)",
    "Dual-Pivot QuickSort": "O(n log n) promedio",
    "Heap Sort": "O(n log n)",
    "Merge Sort": "O(n log n)",
    "Radix Sort": "O(n*d)",
}


def benchmark():
    # Si existe un archivo llamado results en vez de carpeta, esto fallará.
    # Asegúrate de que results sea una carpeta.
    os.makedirs(RESULTS_DIR, exist_ok=True)

    rows = []

    if not os.path.exists(DATA_DIR):
        print(f"No existe la carpeta de datos: {DATA_DIR}")
        return

    files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith(".txt")])

    if not files:
        print("No se encontraron archivos .txt en la carpeta data.")
        return

    for file_name in files:
        size = int(file_name.replace("data_", "").replace(".txt", ""))
        file_path = os.path.join(DATA_DIR, file_name)

        print(f"\nProcesando archivo: {file_name}")

        # Lectura fuera de la medición
        original_data = load_data(file_path)

        for algorithm_name, algorithm_function in ALGORITHMS.items():
            # Saltar Cocktail Sort para 1.000.000 por tiempo excesivo
            if size == 1000000 and algorithm_name == "Cocktail Sort":
                print("Saltando Cocktail Sort para 1000000 por tiempo excesivo")
                rows.append([
                    algorithm_name,
                    "Python",
                    size,
                    "No ejecutado",
                    COMPLEXITIES[algorithm_name]
                ])
                continue

            print(f"Iniciando {algorithm_name} con tamaño {size}...")

            # Cada algoritmo usa una copia del mismo arreglo
            data_copy = original_data.copy()

            # SOLO se mide el ordenamiento
            start_time = time.perf_counter()
            algorithm_function(data_copy)
            end_time = time.perf_counter()

            elapsed_ms = (end_time - start_time) * 1000

            rows.append([
                algorithm_name,
                "Python",
                size,
                round(elapsed_ms, 4),
                COMPLEXITIES[algorithm_name]
            ])

            print(f"{algorithm_name} | Python | {size} => {elapsed_ms:.4f} ms")

    with open(RESULTS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["algoritmo", "lenguaje", "tamano", "tiempo_ms", "complejidad_teorica"])
        writer.writerows(rows)

    print(f"\nResultados guardados en: {RESULTS_FILE}")


if __name__ == "__main__":
    benchmark()