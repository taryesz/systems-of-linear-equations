import numpy

from constants import MATRIX_SIZE, STUDENT_INDEX
from math import sin

def create_excitation_vector() -> numpy.ndarray:

    # Create a zero-vector of size MATRIX_SIZE that will store floats
    excitation_vector = numpy.zeros(MATRIX_SIZE, dtype=float)

    # Fill the vector with values gained from a formula defined in the task's description
    for i in range(MATRIX_SIZE): excitation_vector[i] = sin(i * (int(STUDENT_INDEX[2]) + 1))

    return excitation_vector
