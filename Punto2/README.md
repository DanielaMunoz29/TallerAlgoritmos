# Taller de Ordenamiento y Búsqueda

Implementación y análisis comparativo de algoritmos de ordenamiento y búsqueda en dos lenguajes: **Java** (compilado) y **Python** (interpretado).

---

## Estructura del proyecto

```
TallerAlgoritmos/
├── data/
│   ├── data_10000.txt            # Datos aleatorios (8 dígitos)
│   ├── data_100000.txt
│   └── data_1000000.txt
│
├── data_generator.py             # Genera los archivos de datos aleatorios
│
├── SearchAlgorithms.java         # Implementaciones de búsqueda en Java
├── MainBusqueda.java             # Benchmark Java → exporta CSV, JSON y TXT
├── TestCorrectness.java          # Pruebas de corrección de los algoritmos
│
├── search_algorithms.py          # Implementaciones de búsqueda en Python + benchmark
├── generate_chart.py             # Genera gráfico comparativo Java vs Python
│
├── results_java.csv / .json      # Resultados del benchmark Java
├── results_python.csv / .json    # Resultados del benchmark Python
├── results_final.txt             # Resultados Java en formato tabla
└── chart_busqueda.png            # Gráfico comparativo generado
```

---

## Punto 2 — Algoritmos de Búsqueda

### Algoritmos implementados

| Algoritmo          | Complejidad | Requisito        |
|--------------------|-------------|------------------|
| Búsqueda Binaria   | O(log n)    | Arreglo ordenado |
| Búsqueda Ternaria  | O(log₃ n)   | Arreglo ordenado |
| Jump Search        | O(√n)       | Arreglo ordenado |

Los tres algoritmos se implementaron de forma idéntica en Java y Python, siguiendo las referencias de [GeeksforGeeks](https://www.geeksforgeeks.org/).

- Búsqueda Binaria: https://www.geeksforgeeks.org/binary-search/
- Búsqueda Ternaria: https://www.geeksforgeeks.org/ternary-search/
- Jump Search: https://www.geeksforgeeks.org/jump-search/

### Tamaños de prueba

- 10.000 elementos
- 100.000 elementos
- 1.000.000 elementos

Los datos son números enteros aleatorios de 8 dígitos, generados una sola vez y reutilizados en todas las ejecuciones para garantizar comparaciones justas. Se mide únicamente el tiempo de ejecución del algoritmo, excluyendo lectura/escritura de archivos.

---

## Resultados experimentales

### Java (compilado)

| Tamaño    | Binaria (ns) | Ternaria (ns) | Jump (ns) |
|-----------|-------------|---------------|-----------|
| 10.000    | 2.800       | 2.500         | 78.300    |
| 100.000   | 3.200       | 3.301         | 341.200   |
| 1.000.000 | 4.100       | 3.199         | 351.599   |

### Python (interpretado)

| Tamaño    | Binaria (ns) | Ternaria (ns) | Jump (ns) |
|-----------|-------------|---------------|-----------|
| 10.000    | 18.600      | 17.000        | 190.000   |
| 100.000   | 6.800       | 7.200         | 155.300   |
| 1.000.000 | 8.700       | 8.200         | 584.200   |

El gráfico comparativo se encuentra en `chart_busqueda.png`.

---

## Cómo ejecutar

### Todo de una vez

```bash
python run_all.py
```

### Paso a paso

### 1. Generar los datos (solo la primera vez)

```bash
python data_generator.py
```

### 2. Benchmark Java

```bash
javac MainBusqueda.java SearchAlgorithms.java
java MainBusqueda
```

### 3. Benchmark Python

```bash
python search_algorithms.py
```

### 4. Generar gráfico comparativo

```bash
python generate_chart.py
```

> Requiere `matplotlib` y `numpy`. Se instalan automáticamente si no están presentes.

### 5. Pruebas de corrección (Java)

```bash
javac TestCorrectness.java SearchAlgorithms.java
java TestCorrectness
```

---

## Exportación de resultados

Los resultados se exportan automáticamente en los siguientes formatos:

| Archivo               | Contenido                        |
|-----------------------|----------------------------------|
| `results_java.csv`    | Tiempos Java en formato CSV      |
| `results_java.json`   | Tiempos Java en formato JSON     |
| `results_python.csv`  | Tiempos Python en formato CSV    |
| `results_python.json` | Tiempos Python en formato JSON   |
| `results_final.txt`   | Tabla de resultados Java (texto) |

---

## Análisis: compilado vs interpretado

Java, al ser un lenguaje compilado a bytecode ejecutado por la JVM con compilación JIT, tiene tiempos significativamente menores en operaciones repetitivas. Python, al ser interpretado, introduce overhead por la evaluación dinámica de cada instrucción.

En los resultados se observa que:
- Para Binaria y Ternaria, Java es entre **2x y 3x más rápido** que Python a gran escala.
- Para Jump Search, la diferencia es más pronunciada (~1.5x en 1.000.000 elementos) aunque en este caso Python se beneficia de que los datos ya están en memoria como lista nativa.
- A tamaños pequeños (10K), Python muestra mayor overhead relativo por el costo de arranque del intérprete en la primera llamada.
