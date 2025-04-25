import numpy

from constants import STUDENT_INDEX
from math import sin

def create_excitation_vector(system_matrix_size) -> numpy.ndarray:

    # Create a zero-vector of size MATRIX_SIZE that will store floats
    excitation_vector = numpy.zeros(system_matrix_size)

    # Fill the vector with values gained from a formula defined in the task's description
    for i in range(system_matrix_size): 
        excitation_vector[i] = sin(i * (int(STUDENT_INDEX[2]) + 1))

    return excitation_vector
