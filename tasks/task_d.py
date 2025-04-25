import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from matrix.system_matrix import create_system_matrix
from matrix.excitation_vector import create_excitation_vector

from solve.lu_decomposition import solve_using_lu_decomposition

from constants import STUDENT_INDEX

system_matrix_size:int = 1200 + 10 * int(STUDENT_INDEX[4]) + int(STUDENT_INDEX[5])
main_diagonal_value:int = 3

system_matrix = create_system_matrix(system_matrix_size, main_diagonal_value)
excitation_vector = create_excitation_vector(system_matrix_size)

solution, residual_norm, time_to_find_solution = solve_using_lu_decomposition(system_matrix, system_matrix_size, excitation_vector)

print(">>> LU Decomposition Method <<<")
print("Time:", time_to_find_solution)
print("Residual norm:", residual_norm)
print("Solution:", solution)
