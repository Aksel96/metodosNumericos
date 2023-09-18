# Definir el sistema de ecuaciones Ax = b
A = [[9, 2, -1],
     [7, 8, 5],
     [3, 4, -10]]

b = [-2, 3, 6]

# Establecer la aproximación inicial
x0 = [0, 0, 0]

# Número máximo de iteraciones
max_iter = 6

# Tolerancia para el criterio de parada
tolerancia = 1e-6


def jacobi_iteration(A, b, x):
    n = len(b)
    x_nuevo = [0] * n
    errores = [0] * n

    for i in range(n):
        suma = 0
        for j in range(n):
            if j != i:
                suma += A[i][j] * x[j]

        x_nuevo[i] = (b[i] - suma) / A[i][i]
        errores[i] = abs(((x_nuevo[i] - x[i])/x_nuevo[i])*100)

    return x_nuevo, errores


for iteration in range(max_iter):
    x_nuevo, errores = jacobi_iteration(A, b, x0)
    x0 = x_nuevo

    print(f"Iteración {iteration + 1}:")
    print(f"x = {x0[0]:.6f}, y = {x0[1]:.6f}, z = {x0[2]:.6f}")
    print(f"Error en x: {errores[0]:.6f} %, Error en y: {errores[1]:.6f} %, Error en z: {errores[2]:.6f} %")

    if all(error < tolerancia for error in errores):
        break

print("\nResultado final:")
print(f"x = {x0[0]}, y = {x0[1]}, z = {x0[2]}")
