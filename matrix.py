from constants import *

def create_system_matrix() -> list[list[int]]:

    matrix:list[list[int]] = [[0 for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]

    for i in range(MATRIX_SIZE):
        
        matrix[i][i] = MAIN_DIAGONAL_VALUE
        
        if i > 0:
            matrix[i][i - 1] = SECOND_DIAGONAL_VALUE
            matrix[i - 1][i] = SECOND_DIAGONAL_VALUE

        if i > 1:
            matrix[i][i - 2] = THIRD_DIAGONAL_VALUE
            matrix[i - 2][i] = THIRD_DIAGONAL_VALUE

    return matrix
