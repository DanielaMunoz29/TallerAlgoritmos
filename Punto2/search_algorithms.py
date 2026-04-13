"""
Algoritmos de Búsqueda - Implementación en Python (lenguaje interpretado)
Fuentes: https://www.geeksforgeeks.org/binary-search/
         https://www.geeksforgeeks.org/ternary-search/
         https://www.geeksforgeeks.org/jump-search/
"""

import math
import time
import json
import csv
import os

SIZES = [10000, 100000, 1000000]
DATA_DIR = "../data"


# ── Algoritmos ────────────────────────────────────────────────────────────────

def busqueda_binaria(arr: list[int], x: int) -> int:
    """Búsqueda Binaria - O(log n)"""
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = izquierda + (derecha - izquierda) // 2
        if arr[medio] == x:
            return medio
        elif arr[medio] < x:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1


def busqueda_ternaria(arr: list[int], x: int) -> int:
    """Búsqueda Ternaria - O(log3 n)"""
    l, r = 0, len(arr) - 1
    while r >= l:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2
        if x < arr[mid1]:
            r = mid1 - 1
        elif x > arr[mid2]:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1
    return -1


def jump_search(arr: list[int], x: int) -> int:
    """Jump Search - O(sqrt(n))"""
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == x:
        return prev
    return -1


# ── Carga de datos ────────────────────────────────────────────────────────────

def load_sorted_data(size: int) -> list[int]:
    raw_path = os.path.join(DATA_DIR, f"data_{size}.txt")

    if not os.path.exists(raw_path):
        print(f"Archivo no encontrado: {raw_path}")
        return []

    with open(raw_path, encoding="utf-8") as f:
        data = [int(line.strip()) for line in f if line.strip()]

    return sorted(data)


# ── Benchmark ─────────────────────────────────────────────────────────────────

def benchmark() -> list[dict]:
    results = []

    print("=" * 52)
    print("   BENCHMARK DE ALGORITMOS DE BÚSQUEDA (Python)")
    print("=" * 52)
    print(f"{'Tamaño':<12} | {'Binaria (ns)':<15} | {'Ternaria (ns)':<15} | {'Jump (ns)':<12}")
    print("-" * 62)

    for size in SIZES:
        data = load_sorted_data(size)
        if not data:
            continue

        target = data[-1]  # peor caso: último elemento

        # Calentamiento
        busqueda_binaria(data, target)
        busqueda_ternaria(data, target)
        jump_search(data, target)

        # Medición Binaria
        t0 = time.perf_counter_ns()
        busqueda_binaria(data, target)
        time_bin = time.perf_counter_ns() - t0

        # Medición Ternaria
        t0 = time.perf_counter_ns()
        busqueda_ternaria(data, target)
        time_ter = time.perf_counter_ns() - t0

        # Medición Jump
        t0 = time.perf_counter_ns()
        jump_search(data, target)
        time_jump = time.perf_counter_ns() - t0

        print(f"{size:<12} | {time_bin:<15} | {time_ter:<15} | {time_jump:<12}")

        results.append({
            "language": "Python",
            "size": size,
            "binary_ns": time_bin,
            "ternary_ns": time_ter,
            "jump_ns": time_jump,
        })

    print("=" * 52)
    return results


# ── Exportación ───────────────────────────────────────────────────────────────

def export_json(results: list[dict], path: str = "results_python.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Resultados exportados a {path}")


def export_csv(results: list[dict], path: str = "results_python.csv"):
    if not results:
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"Resultados exportados a {path}")


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    results = benchmark()
    export_json(results)
    export_csv(results)
