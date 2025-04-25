import numpy

from constants import RESIDUAL_NORM, RESIDUAL_ABSOLUTE
from matrix.residual_vector import create_residual_vector

def extract_matrix_parts(system_matrix:numpy.ndarray, lower_shift=-1, upper_shift=+1) -> tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]:

    lower_triangle = numpy.tril(system_matrix, k=lower_shift)
    upper_triangle = numpy.triu(system_matrix, k=upper_shift)
    diagonal = numpy.diag(numpy.diag(system_matrix))

    return lower_triangle, upper_triangle, diagonal

def solve(system_matrix:numpy.ndarray, system_matrix_size:int, excitation_vector:numpy.ndarray, iteration_matrix, constant_vector) -> tuple[numpy.ndarray, int, numpy.array]:
    
    # Create a zero-vector of size MATRIX_SIZE
    solution = numpy.zeros(system_matrix_size)

    # Counter to see how many iterations the given problem requires to get solved
    iterations = 0

    # Create a list to store residual norm from each iteration
    residual_norm_vector = []

    # Keep iterating until the solution is as precise as we want it to be
    current_residual_norm = numpy.linalg.norm(create_residual_vector(system_matrix, solution, excitation_vector))
    while current_residual_norm >= RESIDUAL_NORM and current_residual_norm < RESIDUAL_ABSOLUTE:
        solution = iteration_matrix @ solution + constant_vector
        current_residual_norm = numpy.linalg.norm(create_residual_vector(system_matrix, solution, excitation_vector))
        residual_norm_vector.append(current_residual_norm)
        iterations += 1

    # Convert to a numpy object for further convenience
    residual_norm_vector = numpy.array(residual_norm_vector)

    return solution, iterations, residual_norm_vector
