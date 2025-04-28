import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from matrix.system_matrix import create_system_matrix
from matrix.excitation_vector import create_excitation_vector

from solve.jacobi import solve_using_jacobi
from solve.gauss_seidel import solve_using_gauss_seidel
from solve.lu_decomposition import solve_using_lu_decomposition

from plot import plot_time_dependence
from constants import STUDENT_INDEX

system_matrix_sizes:list[int] = [100, 500, 1000, 2000, 3000]
main_diagonal_value:int = 5 + int(STUDENT_INDEX[3])

time_to_find_solution_jacobi_vector = []
time_to_find_solution_gauss_seidel_vector = []
time_to_find_solution_lu_decomposition_vector = []

for size in system_matrix_sizes:

    system_matrix = create_system_matrix(size, main_diagonal_value)
    excitation_vector = create_excitation_vector(size)

    _, _, _, time_to_find_solution_jacobi = solve_using_jacobi(system_matrix, size, excitation_vector)
    time_to_find_solution_jacobi_vector.append(time_to_find_solution_jacobi)

    _, _, _, time_to_find_solution_gauss_seidel = solve_using_gauss_seidel(system_matrix, size, excitation_vector)
    time_to_find_solution_gauss_seidel_vector.append(time_to_find_solution_gauss_seidel)

    _, _, time_to_find_solution_lu_decomposition = solve_using_lu_decomposition(system_matrix, size, excitation_vector)
    time_to_find_solution_lu_decomposition_vector.append(time_to_find_solution_lu_decomposition)

plot_time_dependence(time_to_find_solution_jacobi_vector, time_to_find_solution_gauss_seidel_vector, time_to_find_solution_lu_decomposition_vector, system_matrix_sizes)
plot_time_dependence(time_to_find_solution_jacobi_vector, time_to_find_solution_gauss_seidel_vector, time_to_find_solution_lu_decomposition_vector, system_matrix_sizes, scale='log')
