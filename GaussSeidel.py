def calculate_error(previous, current):
    errors = [abs((current[i] - previous[i]) / current[i]) * 100 if current[i] != 0 else 0 for i in range(len(current))]
    formatted_errors = [f'{error:.6f}' for error in errors]
    return formatted_errors


def gauss_seidel(A, b, initial_guess, tolerance, max_iterations):
    n = len(b)
    x = initial_guess.copy()

    for iteration in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            sum_ax = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_ax) / A[i][i]

        error = calculate_error(x, x_new)
        formatted_x = [f'{value:.6f}' for value in x_new]
        print(f"Iteration {iteration + 1}: x = {formatted_x},\nError (%) = {error}")

        if all(float(err) < tolerance for err in error):
            break

        x = x_new

    return x


# Define la matriz de coeficientes A y el vector de términos independientes b
A = [
    [17, -2, -3],
    [-5, -21, -2],
    [-5, -5, 22]]

b = [500, 200, 30]

# Valores iniciales para x, y, y z
initial_guess = [0, 0, 0]

# Tolerancia y número máximo de iteraciones
tolerance = 1e-6
max_iterations = 6

# Llama a la función Gauss-Seidel
solution = gauss_seidel(A, b, initial_guess, tolerance, max_iterations)

print("Solución final:")
formatted_solution = [f'{value:.6f}' for value in solution]
print(f"x = {formatted_solution[0]}, y = {formatted_solution[1]}, z = {formatted_solution[2]}")
