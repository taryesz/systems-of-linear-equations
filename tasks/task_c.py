import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from matrix.system_matrix import create_system_matrix
from matrix.excitation_vector import create_excitation_vector

from solve.jacobi import solve_using_jacobi
from solve.gauss_seidel import solve_using_gauss_seidel

from plot import plot_residual_norm_change
from constants import STUDENT_INDEX

system_matrix_size:int = 1200 + 10 * int(STUDENT_INDEX[4]) + int(STUDENT_INDEX[5])
main_diagonal_value:int = 3

system_matrix = create_system_matrix(system_matrix_size, main_diagonal_value)
excitation_vector = create_excitation_vector(system_matrix_size)

solution, iterations, residual_norm_vector, time_to_find_solution = solve_using_jacobi(system_matrix, system_matrix_size, excitation_vector)

print(">>> Jacobi Method <<<")
print("Time:", time_to_find_solution)
print("Iterations:", iterations)
print("Solution:", solution)

plot_residual_norm_change(residual_norm_vector)

solution, iterations, residual_norm_vector, time_to_find_solution = solve_using_gauss_seidel(system_matrix, system_matrix_size, excitation_vector)

print(">>> Gauss-Seidel Method <<<")
print("Time:", time_to_find_solution)
print("Iterations:", iterations)
print("Solution:", solution)

plot_residual_norm_change(residual_norm_vector)
