import numpy
import time
import matplotlib.pyplot as plt

from constants import MATRIX_SIZE, RESIDUAL_NORM
from residual_vector import create_residual_vector

def extract_matrix_parts(system_matrix:numpy.ndarray) -> tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]:

    lower_triangle = numpy.tril(system_matrix, k=-1)
    upper_triangle = numpy.triu(system_matrix, k=+1)
    diagonal = numpy.diag(numpy.diag(system_matrix))

    return lower_triangle, upper_triangle, diagonal

def solve(system_matrix:numpy.ndarray, excitation_vector:numpy.ndarray, iteration_matrix, constant_vector) -> tuple[numpy.ndarray, float, int]:
    
    # Create a zero-vector of size MATRIX_SIZE that will store floats
    solution = numpy.ones(MATRIX_SIZE, dtype=float)

    # Counter to see how many iterations the given problem requires to get solved
    iterations = 0

    start_time = time.time()

    # Create a list to store residual norm from each iteration
    residual_norm_vector = []

    # Keep iterating until the solution is as precise as we want it to be
    current_residual_norm = numpy.linalg.norm(create_residual_vector(system_matrix, solution, excitation_vector))
    while current_residual_norm > RESIDUAL_NORM:
        solution = numpy.matmul(iteration_matrix, solution) + constant_vector
        current_residual_norm = numpy.linalg.norm(create_residual_vector(system_matrix, solution, excitation_vector))
        residual_norm_vector.append(current_residual_norm)
        iterations += 1

    finish_time = time.time()

    # Convert to a numpy object for further convenience
    residual_norm_vector = numpy.array(residual_norm_vector)

    # Plot the residual change
    plt.figure(figsize=(10, 6))
    plt.semilogy(residual_norm_vector, 'b-', linewidth=2)
    plt.title('Residual Norm Change in Subsequent Iterations')
    plt.xlabel('Iteration')
    plt.ylabel('Residual Norm')
    plt.grid(True, which="both", ls="-")
    plt.show()

    time_to_find_solution = finish_time - start_time 

    return solution, time_to_find_solution, iterations
