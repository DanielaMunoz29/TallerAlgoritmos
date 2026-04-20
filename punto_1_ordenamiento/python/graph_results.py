import os
import pandas as pd
import matplotlib.pyplot as plt

# Obtiene la ruta absoluta de la carpeta donde está este archivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construye la ruta hacia la carpeta donde están los resultados
RESULTS_DIR = os.path.join(BASE_DIR, "..", "results")

# Rutas de los archivos CSV generados por Python y Java
PYTHON_RESULTS = os.path.join(RESULTS_DIR, "resultados_python.csv")
JAVA_RESULTS = os.path.join(RESULTS_DIR, "resultados_java.csv")


def add_labels(ax):
    """
    Agrega el valor numérico encima de cada barra del gráfico.
    """
    for bar in ax.patches:
        height = bar.get_height()

        # Solo etiqueta valores válidos y mayores que cero
        if pd.notna(height) and height > 0:
            ax.annotate(
                f"{height:.2f}",
                (bar.get_x() + bar.get_width() / 2, height),
                ha="center",
                va="bottom",
                fontsize=8
            )


def graph_results():
    """
    Genera un gráfico comparativo por cada tamaño de arreglo.

    En cada gráfico:
    - cada algoritmo aparece en el eje X
    - se muestran dos barras por algoritmo:
      una para Python y otra para Java
    - se usa escala logarítmica en Y para que se puedan
      comparar mejor tiempos muy grandes y muy pequeños
    """
    # Lee los resultados de ambos lenguajes
    python_df = pd.read_csv(PYTHON_RESULTS)
    java_df = pd.read_csv(JAVA_RESULTS)

    # Convierte la columna tiempo_ms a numérico.
    # Si encuentra "No ejecutado", lo convierte en NaN
    python_df["tiempo_ms"] = pd.to_numeric(python_df["tiempo_ms"], errors="coerce")
    java_df["tiempo_ms"] = pd.to_numeric(java_df["tiempo_ms"], errors="coerce")

    # Une ambos resultados en una sola tabla
    all_results = pd.concat([python_df, java_df], ignore_index=True)

    # Define el orden fijo de los algoritmos
    algorithm_order = [
        "Cocktail Sort",
        "Dual-Pivot QuickSort",
        "Heap Sort",
        "Merge Sort",
        "Radix Sort"
    ]

    # Recorre cada tamaño de entrada
    for size in sorted(all_results["tamano"].unique()):
        subset = all_results[all_results["tamano"] == size].copy()

        # Fuerza el orden de aparición de los algoritmos
        subset["algoritmo"] = pd.Categorical(
            subset["algoritmo"],
            categories=algorithm_order,
            ordered=True
        )

        subset = subset.sort_values("algoritmo")

        # Reorganiza los datos para tener dos barras por algoritmo
        pivot_table = subset.pivot(
            index="algoritmo",
            columns="lenguaje",
            values="tiempo_ms"
        )

        # Crea el gráfico de barras
        ax = pivot_table.plot(kind="bar", figsize=(11, 6))

        # Título y etiquetas
        plt.title(f"Comparación de tiempos de ordenamiento - {size} elementos")
        plt.xlabel("Algoritmo")
        plt.ylabel("Tiempo (ms)")

        # Rota los nombres para que se vean mejor
        plt.xticks(rotation=15)

        # Activa la leyenda
        plt.legend(title="Lenguaje")

        # Cambia la escala del eje Y a logarítmica
        # Esto permite visualizar mejor diferencias grandes
        ax.set_yscale("log")

        # Agrega una cuadrícula horizontal suave
        ax.grid(True, which="both", axis="y", linestyle="--", alpha=0.5)

        # Agrega el valor encima de cada barra
        add_labels(ax)

        # Ajusta espacios automáticamente
        plt.tight_layout()

        # Guarda la imagen
        output_path = os.path.join(RESULTS_DIR, f"grafico_{size}.png")
        plt.savefig(output_path, dpi=300)
        plt.close()

        print(f"Gráfico generado: {output_path}")


if __name__ == "__main__":
    graph_results()