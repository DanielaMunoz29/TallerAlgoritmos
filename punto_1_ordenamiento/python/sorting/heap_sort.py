def heapify(arr, n, i):
    """
    Convierte en heap el subárbol cuya raíz está en la posición i.

    Parámetros:
    - arr: lista a ordenar
    - n: tamaño actual del heap
    - i: índice de la raíz del subárbol
    """
    # Se asume inicialmente que la raíz es el mayor
    largest = i

    # Índice del hijo izquierdo
    left = 2 * i + 1

    # Índice del hijo derecho
    right = 2 * i + 2

    # Si el hijo izquierdo existe y es mayor que la raíz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Si el hijo derecho existe y es mayor que el mayor actual
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el mayor no es la raíz, se intercambian
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Se aplica heapify recursivamente al subárbol afectado
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Ordena una lista usando Heap Sort.
    """
    n = len(arr)

    # Construye el heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrae uno a uno los elementos del heap
    for i in range(n - 1, 0, -1):
        # Mueve la raíz actual (el mayor) al final
        arr[0], arr[i] = arr[i], arr[0]

        # Reconstruye el heap con el tamaño reducido
        heapify(arr, i, 0)