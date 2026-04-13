def counting_sort(arr, exp):
    """
    Aplica Counting Sort a la lista según el dígito representado por exp.

    exp = 1   -> unidades
    exp = 10  -> decenas
    exp = 100 -> centenas
    """
    n = len(arr)

    # Lista de salida donde quedarán temporalmente los valores ordenados
    output = [0] * n

    # Arreglo de conteo para los dígitos del 0 al 9
    count = [0] * 10

    # Cuenta cuántas veces aparece cada dígito
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Convierte el conteo en posiciones acumuladas
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construye la lista de salida desde el final
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copia el resultado a la lista original
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    """
    Ordena una lista usando Radix Sort.
    """
    if len(arr) == 0:
        return

    # Obtiene el número máximo para saber cuántos dígitos procesar
    max_value = max(arr)

    # Aplica counting sort por cada posición decimal
    exp = 1
    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10