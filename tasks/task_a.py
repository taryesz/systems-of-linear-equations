import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from matrix.system_matrix import create_system_matrix
from matrix.excitation_vector import create_excitation_vector

from constants import STUDENT_INDEX

system_matrix_size:int = 1200 + 10 * int(STUDENT_INDEX[4]) + int(STUDENT_INDEX[5])
main_diagonal_value:int = 5 + int(STUDENT_INDEX[3])

system_matrix = create_system_matrix(system_matrix_size, main_diagonal_value)
excitation_vector = create_excitation_vector(system_matrix_size)

print(">>> System Matrix <<<")
print(system_matrix)
print(">>> Excitation Vector <<<")
print(excitation_vector)
