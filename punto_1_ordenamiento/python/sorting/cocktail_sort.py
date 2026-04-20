def cocktail_sort(a):
    """
    Ordena una lista usando Cocktail Sort.

    Este algoritmo recorre la lista en dos direcciones:
    de izquierda a derecha y luego de derecha a izquierda.
    """
    n = len(a)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        # Se reinicia la bandera al comenzar la pasada
        swapped = False

        # Recorrido de izquierda a derecha
        for i in range(start, end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # Si no hubo intercambios, ya está ordenado
        if not swapped:
            break

        # Se reinicia la bandera para la pasada de regreso
        swapped = False

        # El último elemento ya quedó en su posición correcta
        end -= 1

        # Recorrido de derecha a izquierda
        for i in range(end - 1, start - 1, -1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # El menor elemento ya quedó en su posición correcta
        start += 1