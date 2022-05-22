def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_perron(n: int, cache = {}):
    if n == 0 or n == 1:
        return 1

    try:
        return cache[n]
    except KeyError:
        resultado = fibonacci_perron(n - 1, cache) + fibonacci_perron(n - 2, cache)
        cache[n] = resultado

        return resultado

if __name__ == '__main__':
    """
    2 funciones de fibonacci, la primera es recursiva de toda la vida.
    La segunda, utiliza un diccionario para guardar los valores la calculados,
    por lo que consume mas menoria, pero ahorra consumo del procesador y tiempo
    """

    n = int(input('numero:'))
    resultado = fibonacci_recursivo(n)
    print(resultado)
