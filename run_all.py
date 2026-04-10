"""
Ejecuta todo el pipeline del taller en orden:
  1. Genera datos (si no existen)
  2. Compila y corre benchmark Java
  3. Corre benchmark Python
  4. Genera gráfico comparativo
  5. Pruebas de corrección Java
"""

import subprocess
import sys

def run(cmd: list[str], desc: str):
    print(f"\n{'='*52}")
    print(f"  {desc}")
    print(f"{'='*52}")
    result = subprocess.run(cmd, text=True, capture_output=False)
    if result.returncode != 0:
        print(f"ERROR en: {' '.join(cmd)}")
        sys.exit(result.returncode)

run([sys.executable, "data_generator.py"],
    "1. Generando datos...")

run(["javac", "MainBusqueda.java", "SearchAlgorithms.java", "TestCorrectness.java"],
    "2. Compilando Java...")

run(["java", "MainBusqueda"],
    "3. Benchmark Java")

run([sys.executable, "search_algorithms.py"],
    "4. Benchmark Python")

run([sys.executable, "generate_chart.py"],
    "5. Generando gráfico...")

run(["java", "TestCorrectness"],
    "6. Pruebas de corrección Java")

print("\n✓ Todo listo. Revisa chart_busqueda.png para el gráfico.")
