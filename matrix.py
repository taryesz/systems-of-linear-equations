import numpy

from constants import MATRIX_SIZE, MAIN_DIAGONAL_VALUE, SECOND_DIAGONAL_VALUE, THIRD_DIAGONAL_VALUE

def create_system_matrix() -> numpy.ndarray:

    # Create a square system zero-matrix of size MATRIX_SIZE that will store integers
    system_matrix = numpy.zeros((MATRIX_SIZE, MATRIX_SIZE), dtype=int)

    # Fill the matrix with values as described in the task's description
    for i in range(MATRIX_SIZE):
        
        system_matrix[i][i] = MAIN_DIAGONAL_VALUE
        
        if i > 0:
            system_matrix[i][i - 1] = SECOND_DIAGONAL_VALUE
            system_matrix[i - 1][i] = SECOND_DIAGONAL_VALUE

        if i > 1:
            system_matrix[i][i - 2] = THIRD_DIAGONAL_VALUE
            system_matrix[i - 2][i] = THIRD_DIAGONAL_VALUE

    return system_matrix
