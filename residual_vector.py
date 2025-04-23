import numpy

def create_residual_vector(system_matrix:numpy.ndarray, solution:numpy.ndarray, excitation_vector:numpy.ndarray) -> numpy.ndarray:
    return numpy.matmul(system_matrix, solution) - excitation_vector