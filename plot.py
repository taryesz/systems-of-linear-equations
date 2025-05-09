import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def plot_residual_norm_changes(residual_norm_vectors, labels) -> None:
    
    plt.figure(figsize=(10, 6))
    
    for residual_norm_vector, label in zip(residual_norm_vectors, labels):
        plt.semilogy(range(1, len(residual_norm_vector) + 1), residual_norm_vector, linewidth=2, label=label)
    
    plt.title('Residual Norm Change in Subsequent Iterations (Logarithmic Scale)')
    plt.xlabel('Iteration')
    plt.ylabel('Residual Norm')
    plt.grid(True, which="both", ls="-")
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=10, integer=True, prune='both'))
    plt.legend()
    plt.show()

    
def plot_time_dependence(time_to_find_solution_jacobi_vector, 
                         time_to_find_solution_gauss_seidel_vector,
                         time_to_find_solution_lu_decomposition_vector,
                         system_matrix_sizes,
                         scale='lin') -> None:

    plt.figure(figsize=(10, 5))
    plt.plot(system_matrix_sizes, time_to_find_solution_jacobi_vector, label='Jacobi', marker='o')
    plt.plot(system_matrix_sizes, time_to_find_solution_gauss_seidel_vector, label='Gauss-Seidel', marker='o')
    plt.plot(system_matrix_sizes, time_to_find_solution_lu_decomposition_vector, label='LU Decomposition', marker='o')
    plt.xlabel('System Matrix Size')
    plt.ylabel('Time [s]')
    plt.title(f'Dependence of Solution Time on the Number of Unknown Values ({"Logarithmic" if scale == 'log' else "Linear"} Scale)')
    
    if scale == 'log': plt.yscale('log')

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
