import time
from sort import algorithms
from sort import constants
from sort import data_generator


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    """
    Toma medidas de tiempo de ejecución para diferentes tamaños de entrada
    """
    return_table = []
    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)
    return return_table


def take_times(size, samples_by_size):
    """
    Toma muestras de tiempo para cada algoritmo con un tamaño específico
    """
    samples = []
    for _ in range(samples_by_size):
        samples.append(data_generator.get_random_list(size))

    return [
        take_time_for_algorithm(samples, algorithms.bubble_sort),
        take_time_for_algorithm(samples, algorithms.quick_sort),
        take_time_for_algorithm(samples, algorithms.merge_sort),
    ]


def take_time_for_algorithm(samples_array, sorting_approach):
    """
    Retorna la mediana de los tiempos de ejecución para un enfoque de ordenamiento dado
    """
    times = []
    for sample in samples_array:
        start_time = time.time()
        sorting_approach(sample.copy())
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))
    times.sort()
    return times[len(times) // 2]
