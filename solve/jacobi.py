import numpy
import time

from solve.solve import solve
from solve.solve import extract_matrix_parts

def solve_using_jacobi(system_matrix:numpy.ndarray, system_matrix_size:int, excitation_vector:numpy.ndarray) -> tuple[numpy.ndarray, int, numpy.array, float]:
    
    start_time = time.time()

    # Get necessary matrix components
    lower_triangle, upper_triangle, diagonal = extract_matrix_parts(system_matrix)

    # Calculate parts of a Jacobi formula
    iteration_matrix = (-numpy.linalg.inv(diagonal)) @ (lower_triangle + upper_triangle)
    constant_vector = numpy.linalg.inv(diagonal) @ excitation_vector
    
    # Solve using parts obtained in the previous step
    solution, iterations, residual_norm_vector = solve(system_matrix, system_matrix_size, excitation_vector, iteration_matrix, constant_vector)

    finish_time = time.time()

    time_to_find_solution = finish_time - start_time

    return solution, iterations, residual_norm_vector, time_to_find_solution