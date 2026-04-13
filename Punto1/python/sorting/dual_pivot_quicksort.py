def dual_pivot_quicksort(arr, low, high):
    """
    Ordena una lista usando Dual-Pivot QuickSort.

    Usa dos pivotes:
    - uno izquierdo
    - uno derecho

    Esto divide la lista en tres regiones y luego
    ordena cada una recursivamente.
    """
    if low < high:
        # lp es el pivote izquierdo y rp el pivote derecho
        lp, rp = partition(arr, low, high)

        # Ordena la parte izquierda
        dual_pivot_quicksort(arr, low, lp - 1)

        # Ordena la parte central
        dual_pivot_quicksort(arr, lp + 1, rp - 1)

        # Ordena la parte derecha
        dual_pivot_quicksort(arr, rp + 1, high)


def partition(arr, low, high):
    """
    Reorganiza la lista usando dos pivotes y devuelve
    las posiciones finales de ambos.
    """
    # Se asegura que el pivote izquierdo sea menor o igual al derecho
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]

    # p es el pivote izquierdo, q es el pivote derecho
    j = low + 1
    k = low + 1
    g = high - 1
    p = arr[low]
    q = arr[high]

    while k <= g:
        # Si el elemento es menor que el pivote izquierdo,
        # va a la región izquierda
        if arr[k] < p:
            arr[k], arr[j] = arr[j], arr[k]
            j += 1

        # Si el elemento es mayor o igual al pivote derecho,
        # va a la región derecha
        elif arr[k] >= q:
            while arr[g] > q and k < g:
                g -= 1

            arr[k], arr[g] = arr[g], arr[k]
            g -= 1

            # Después del intercambio, puede que el elemento
            # también pertenezca a la región izquierda
            if arr[k] < p:
                arr[k], arr[j] = arr[j], arr[k]
                j += 1

        k += 1

    j -= 1
    g += 1

    # Lleva los pivotes a sus posiciones correctas
    arr[low], arr[j] = arr[j], arr[low]
    arr[high], arr[g] = arr[g], arr[high]

    # Devuelve las posiciones finales de ambos pivotes
    return j, g