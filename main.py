from matrix import create_system_matrix
from excitation_vector import create_excitation_vector
from jacobi import solve_using_jacobi
from gauss_seidel import solve_using_gauss_seidel

# TODO: Task A

system_matrix = create_system_matrix()
excitation_vector = create_excitation_vector()

# TODO: Task B

solution, time_to_find_solution, iterations = solve_using_jacobi(system_matrix, excitation_vector)

print(">>> Jacobi Method <<<")
print("Time:", time_to_find_solution)
print("Iterations:", iterations)
print("Solution:", solution)

solution, time_to_find_solution, iterations = solve_using_gauss_seidel(system_matrix, excitation_vector)

print(">>> Gauss-Seidel Method <<<")
print("Time:", time_to_find_solution)
print("Iterations:", iterations)
print("Solution:", solution)