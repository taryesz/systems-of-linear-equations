import numpy
import time

from matrix.residual_vector import create_residual_vector

def solve_using_lu_decomposition(system_matrix:numpy.ndarray, system_matrix_size:int, excitation_vector:numpy.ndarray) -> tuple[numpy.ndarray, float, int]:
    
    start_time = time.time()

    # Z wykładu nr 2 (slajd 25) - algorytm wyznaczenia L i U dla algorytmu faktoryzacji LU
    upper_triangle = numpy.copy(system_matrix)
    lower_triangle = numpy.eye(system_matrix_size)

    for i in range(1, system_matrix_size):
        for j in range(0, i):
            lower_triangle[i, j] = upper_triangle[i, j] / upper_triangle[j, j]
            upper_triangle[i, :] = upper_triangle[i, :] - lower_triangle[i, j] * upper_triangle[j, :]

    forward_substitution = numpy.linalg.inv(lower_triangle) @ excitation_vector
    backward_substitution = numpy.linalg.inv(upper_triangle) @ forward_substitution

    residual_norm = numpy.linalg.norm(create_residual_vector(system_matrix, backward_substitution, excitation_vector))

    finish_time = time.time()

    time_to_find_solution = finish_time - start_time 

    return backward_substitution, residual_norm, time_to_find_solution
