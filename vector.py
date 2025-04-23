from constants import *
from math import sin

def create_excitation_vector() -> list[float]:

    vector:list[float] = [0 for _ in range(MATRIX_SIZE)]

    for i in range(MATRIX_SIZE):
        vector[i] = sin(i * (int(STUDENT_INDEX[2]) + 1))

    return vector