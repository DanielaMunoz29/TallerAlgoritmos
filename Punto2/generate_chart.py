"""
Genera gráfico de barras comparativo Java vs Python para algoritmos de búsqueda.
Requiere: matplotlib, numpy  (pip install matplotlib numpy)
"""

import json
import os
import re
import subprocess
import sys

try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("Instalando dependencias...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib", "numpy"])
    import matplotlib.pyplot as plt
    import numpy as np


SIZES = [10000, 100000, 1000000]
ALGORITHMS = ["Binaria", "Ternaria", "Jump"]
KEYS_PY = ["binary_ns", "ternary_ns", "jump_ns"]


# ── Parsear resultados de Java (results_final.txt) ────────────────────────────

def parse_java_results(path: str = "results_final.txt") -> dict:
    """Devuelve {size: {binary_ns, ternary_ns, jump_ns}}"""
    data = {}
    if not os.path.exists(path):
        print(f"No se encontró {path}. Ejecuta primero MainBusqueda.java.")
        return data

    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            # Línea de datos: "10000           | 5700  | 5900  | 261800"
            m = re.match(r"\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)", line)
            if m:
                size = int(m.group(1))
                data[size] = {
                    "binary_ns":  int(m.group(2)),
                    "ternary_ns": int(m.group(3)),
                    "jump_ns":    int(m.group(4)),
                }
    return data


# ── Parsear resultados de Python ──────────────────────────────────────────────

def parse_python_results(path: str = "results_python.json") -> dict:
    """Devuelve {size: {binary_ns, ternary_ns, jump_ns}}"""
    if not os.path.exists(path):
        print(f"No se encontró {path}. Ejecuta primero search_algorithms.py.")
        return {}
    with open(path, encoding="utf-8") as f:
        rows = json.load(f)
    return {r["size"]: r for r in rows}


# ── Graficar ──────────────────────────────────────────────────────────────────

def plot(java: dict, python: dict):
    n_algos = len(ALGORITHMS)
    n_sizes = len(SIZES)

    # Una figura por algoritmo
    fig, axes = plt.subplots(1, n_algos, figsize=(16, 6))
    fig.suptitle("Comparación de Algoritmos de Búsqueda: Java vs Python", fontsize=14, fontweight="bold")

    bar_width = 0.35
    x = np.arange(n_sizes)
    size_labels = ["10K", "100K", "1M"]

    colors_java   = "#4C72B0"
    colors_python = "#DD8452"

    for idx, (algo, key) in enumerate(zip(ALGORITHMS, KEYS_PY)):
        ax = axes[idx]

        vals_java   = [java.get(s, {}).get(key, 0)   for s in SIZES]
        vals_python = [python.get(s, {}).get(key, 0) for s in SIZES]

        bars_j = ax.bar(x - bar_width / 2, vals_java,   bar_width, label="Java",   color=colors_java)
        bars_p = ax.bar(x + bar_width / 2, vals_python, bar_width, label="Python", color=colors_python)

        # Valores sobre cada barra
        for bar in bars_j:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h * 1.02,
                    f"{int(h):,}", ha="center", va="bottom", fontsize=7.5)
        for bar in bars_p:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h * 1.02,
                    f"{int(h):,}", ha="center", va="bottom", fontsize=7.5)

        ax.set_title(f"Búsqueda {algo}", fontsize=11)
        ax.set_xlabel("Tamaño del arreglo")
        ax.set_ylabel("Tiempo (ns)")
        ax.set_xticks(x)
        ax.set_xticklabels(size_labels)
        ax.legend()
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{int(v):,}"))

    plt.tight_layout()
    out = "chart_busqueda.png"
    plt.savefig(out, dpi=150)
    print(f"Gráfico guardado en {out}")
    plt.close()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    java_data   = parse_java_results()
    python_data = parse_python_results()

    if not java_data and not python_data:
        print("No hay datos para graficar.")
        sys.exit(1)

    plot(java_data, python_data)
