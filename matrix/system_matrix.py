import numpy

from constants import SECOND_DIAGONAL_VALUE, THIRD_DIAGONAL_VALUE

def create_system_matrix(system_matrix_size, main_diagonal_value) -> numpy.ndarray:

    # Create a square system zero-matrix of size MATRIX_SIZE
    system_matrix = numpy.zeros((system_matrix_size, system_matrix_size))

    # Fill the matrix with values as described in the task's description
    for i in range(system_matrix_size):
        
        system_matrix[i][i] = main_diagonal_value
        
        if i > 0:
            system_matrix[i][i - 1] = SECOND_DIAGONAL_VALUE
            system_matrix[i - 1][i] = SECOND_DIAGONAL_VALUE

        if i > 1:
            system_matrix[i][i - 2] = THIRD_DIAGONAL_VALUE
            system_matrix[i - 2][i] = THIRD_DIAGONAL_VALUE

    return system_matrix
