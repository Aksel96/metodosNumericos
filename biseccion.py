def funcion(x):
    # Define aquí la función para la cual deseas encontrar la raíz.
    return x ** 4 + 3 * x ** 3 - 2


def biseccion(a, b, tolerancia, max_iter):
    if funcion(a) * funcion(b) >= 0:
        print("La función no cumple con el requisito de cambio de signo en el intervalo.")
        return None

    iteracion = 1
    error = abs(b - a)

    while error > tolerancia and iteracion <= max_iter:
        c = (a + b) / 2
        if funcion(c) == 0:
            break
        elif funcion(c) * funcion(a) < 0:
            b = c
        else:
            a = c

        error = abs((b - a)/b)
        print(f"Iteración {iteracion}: Raíz = {c:.6f}, Error = {error:.6f}")
        iteracion += 1

    return (a + b) / 2


# Define el intervalo [a, b], la tolerancia y el número máximo de iteraciones.
a = 0
b = 1
tolerancia = 1e-5
max_iter = 6

raiz = biseccion(a, b, tolerancia, max_iter)
if raiz is not None:
    print(f"\nLa raíz aproximada es: {raiz}")
