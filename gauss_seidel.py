import numpy

from solve import solve, extract_matrix_parts

def solve_using_gauss_seidel(system_matrix:numpy.ndarray, excitation_vector:numpy.ndarray) -> tuple[numpy.ndarray, float, int]:
    
    # Get necessary matrix components
    lower_triangle, upper_triangle, diagonal = extract_matrix_parts(system_matrix)

    # Calculate parts of a Gauss-Seidel formula
    iteration_matrix = numpy.matmul(numpy.linalg.inv(-(diagonal + lower_triangle)), upper_triangle)
    constant_vector = numpy.matmul(numpy.linalg.inv(diagonal + lower_triangle), excitation_vector)

    # Solve using parts obtained in the previous step
    return solve(system_matrix, excitation_vector, iteration_matrix, constant_vector)
