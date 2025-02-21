import time
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Callable

from sort import data_generator, algorithms, constants


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    """
    Measures the execution time of different sorting algorithms for varying input sizes.

    Args:
        minimum_size (int): The minimum size of the input list.
        maximum_size (int): The maximum size of the input list.
        step (int): The increment size for the input list.
        samples_by_size (int): The number of samples to generate for each input size.

    Returns:
        list: A table where each row contains the input size and the median execution times
              for bubble sort, quick sort, and merge sort.
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
    Generates random lists and measures the execution time of different sorting algorithms.

    Args:
        size (int): The size of the input list.
        samples_by_size (int): The number of samples to generate for each input size.

    Returns:
        list: A list containing the median execution times for bubble sort, quick sort, and merge sort.
    """
    samples = []
    for _ in range(samples_by_size):
        samples.append(data_generator.get_random_list(size))

    return [
        take_time_for_algorithm(samples, algorithms.bubble_sort),
        take_time_for_algorithm(samples, algorithms.quick_sort),
        take_time_for_algorithm(samples, algorithms.merge_sort),
        take_time_for_algorithm(samples, algorithms.insertion_sort),
        take_time_for_algorithm(samples, algorithms.shell_sort),
    ]


def take_time_for_algorithm(samples_array, sorting_approach):
    """
    Measures the execution time of a given sorting algorithm on a list of samples.

    Args:
        samples_array (list): A list of random lists to be sorted.
        sorting_approach (function): The sorting algorithm to be used.

    Returns:
        int: The median execution time of the sorting algorithm in milliseconds.
    """
    times = []
    for sample in samples_array:
        start_time = time.time()
        sorting_approach(sample.copy())
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))
    times.sort()
    return times[len(times) // 2]


def measure_time(func: Callable, arr: List[int]) -> float:
    """Measure execution time of sorting function"""
    start_time = time.time()
    func(arr.copy())
    return time.time() - start_time


def generate_random_data(size: int) -> List[int]:
    """Generate random test data of given size"""
    return list(np.random.randint(1, 1000, size))


def compare_and_plot_algorithms(sizes: List[int], algorithms: Dict[str, Callable], repetitions: int = 5):
    """Compare algorithms and generate plots"""
    results = {name: [] for name in algorithms}

    for size in sizes:
        print(f"Testing size {size}")
        data = generate_random_data(size)
        for name, func in algorithms.items():
            times = []
            for _ in range(repetitions):
                execution_time = measure_time(func, data)
                times.append(execution_time)
            results[name].append(np.mean(times))

    # Generate regular plot
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(sizes, times, marker="o", label=name)

    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithms Comparison")
    plt.legend()
    plt.grid(True)
    plt.savefig("comparison_regular.png")
    plt.close()

    # Generate logarithmic plot
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.loglog(sizes, times, marker="o", label=name)

    plt.xlabel("Array Size (log)")
    plt.ylabel("Time (seconds) (log)")
    plt.title("Sorting Algorithms Comparison (Log Scale)")
    plt.legend()
    plt.grid(True)
    plt.savefig("comparison_log.png")
    plt.close()
