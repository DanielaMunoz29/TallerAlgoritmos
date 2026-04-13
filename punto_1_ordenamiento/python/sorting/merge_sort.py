def merge(arr, left, mid, right):
    """
    Mezcla dos subarreglos ordenados dentro de arr.
    
    Primer subarreglo: arr[left..mid]
    Segundo subarreglo: arr[mid+1..right]
    """
    n1 = mid - left + 1
    n2 = right - mid

    # Arreglos temporales
    L = [0] * n1
    R = [0] * n2

    # Copia los datos a los arreglos temporales
    for i in range(n1):
        L[i] = arr[left + i]

    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    # Mezcla los arreglos temporales de vuelta en arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copia los elementos restantes de L[], si hay
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copia los elementos restantes de R[], si hay
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    """
    Ordena una lista usando Merge Sort.
    """
    if left >= right:
        return

    mid = left + (right - left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)