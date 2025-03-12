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
        print("Adding row" + str(table_row) + ", size: " + str(len(table_row)))
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
    """
    Compara el rendimiento de varios algoritmos de ordenamiento y genera gráficas detalladas.

    Args:
        sizes: Lista de tamaños de arreglos para probar
        algorithms: Diccionario de algoritmos {nombre: función}
        repetitions: Número de repeticiones para cada prueba
    """
    # Paleta de colores para cada algoritmo
    colors = plt.cm.viridis(np.linspace(0, 1, len(algorithms)))
    color_map = {name: colors[i] for i, name in enumerate(algorithms.keys())}

    # Almacenar resultados
    results = {name: [] for name in algorithms}
    std_devs = {name: [] for name in algorithms}

    # Configurar estilo
    plt.style.use('seaborn-v0_8-darkgrid')

    for size in sizes:
        print(f"Probando tamaño {size}")
        # Generar datos aleatorios para cada tamaño
        all_times = {name: [] for name in algorithms}

        # Ejecutar cada algoritmo varias veces con conjuntos de datos diferentes
        for rep in range(repetitions):
            data = generate_random_data(size)
            for name, func in algorithms.items():
                execution_time = measure_time(func, data)
                all_times[name].append(execution_time)

        # Calcular estadísticas
        for name in algorithms:
            results[name].append(np.mean(all_times[name]))
            std_devs[name].append(np.std(all_times[name]))

    # Crear directorio para imágenes si no existe
    import os
    os.makedirs("images", exist_ok=True)

    # 1. Gráfica regular con barras de error
    plt.figure(figsize=(12, 8))
    for name, times in results.items():
        plt.errorbar(
            sizes,
            times,
            yerr=std_devs[name],
            marker='o',
            markersize=8,
            linewidth=2,
            capsize=5,
            label=name,
            color=color_map[name]
        )

    plt.xlabel("Tamaño del Arreglo", fontsize=14)
    plt.ylabel("Tiempo (segundos)", fontsize=14)
    plt.title("Comparación de Algoritmos de Ordenamiento", fontsize=16, fontweight='bold')
    plt.legend(fontsize=12, loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("images/comparison_regular.png", dpi=300)
    plt.close()

    # 2. Gráfica logarítmica con barras de error
    plt.figure(figsize=(12, 8))
    for name, times in results.items():
        plt.errorbar(
            sizes,
            times,
            yerr=std_devs[name],
            marker='o',
            markersize=8,
            linewidth=2,
            capsize=5,
            label=name,
            color=color_map[name]
        )

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Tamaño del Arreglo (escala logarítmica)", fontsize=14)
    plt.ylabel("Tiempo (segundos) (escala logarítmica)", fontsize=14)
    plt.title("Comparación de Algoritmos de Ordenamiento (Escala Logarítmica)", fontsize=16, fontweight='bold')
    plt.legend(fontsize=12, loc='upper left')
    plt.grid(True, alpha=0.3, which='both')
    plt.tight_layout()
    plt.savefig("images/comparison_log.png", dpi=300)
    plt.close()

    # 3. Gráficas de barras para cada tamaño
    subset_sizes = sizes[::len(sizes) // min(5, len(sizes))]  # Seleccionar hasta 5 tamaños representativos

    plt.figure(figsize=(14, 10))
    x = np.arange(len(subset_sizes))
    bar_width = 0.15
    offset = 0

    for name, times in results.items():
        subset_times = [times[sizes.index(size)] for size in subset_sizes]
        subset_errors = [std_devs[name][sizes.index(size)] for size in subset_sizes]

        plt.bar(
            x + offset,
            subset_times,
            width=bar_width,
            label=name,
            yerr=subset_errors,
            capsize=5,
            color=color_map[name],
            alpha=0.8
        )
        offset += bar_width

    plt.xlabel("Tamaño del Arreglo", fontsize=14)
    plt.ylabel("Tiempo (segundos)", fontsize=14)
    plt.title("Comparación de Rendimiento por Tamaño de Entrada", fontsize=16, fontweight='bold')
    plt.xticks(x + bar_width * (len(algorithms) - 1) / 2, [str(size) for size in subset_sizes])
    plt.legend(fontsize=12)
    plt.grid(True, axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig("images/comparison_bars.png", dpi=300)
    plt.close()

    # 4. Gráfica de complejidad relativa
    plt.figure(figsize=(12, 8))
    baseline = results[list(algorithms.keys())[0]]  # Usar el primer algoritmo como referencia

    for name, times in results.items():
        if name != list(algorithms.keys())[0]:  # Omitir el algoritmo de referencia
            relative_times = [t / baseline[i] for i, t in enumerate(times)]
            plt.plot(
                sizes,
                relative_times,
                marker='o',
                markersize=8,
                linewidth=2,
                label=f"{name} / {list(algorithms.keys())[0]}",
                color=color_map[name]
            )

    plt.xlabel("Tamaño del Arreglo", fontsize=14)
    plt.ylabel(f"Tiempo Relativo a {list(algorithms.keys())[0]}", fontsize=14)
    plt.title("Rendimiento Relativo de Algoritmos", fontsize=16, fontweight='bold')
    plt.axhline(y=1, color='gray', linestyle='--')
    plt.legend(fontsize=12, loc='best')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("images/comparison_relative.png", dpi=300)
    plt.close()

    # 5. Heatmap de eficiencia
    import matplotlib.colors as mcolors

    plt.figure(figsize=(10, 8))

    # Normalizar todos los tiempos al más rápido para cada tamaño
    normalized_results = []
    for i in range(len(sizes)):
        min_time = min([results[alg][i] for alg in algorithms])
        row = [results[alg][i] / min_time for alg in algorithms]
        normalized_results.append(row)

    heatmap = plt.imshow(
        normalized_results,
        cmap='YlOrRd',
        aspect='auto',
        norm=mcolors.LogNorm(vmin=1, vmax=max([max(row) for row in normalized_results]))
    )

    plt.colorbar(heatmap, label="Veces más lento que el más rápido")
    plt.xlabel("Algoritmo", fontsize=14)
    plt.ylabel("Tamaño del Arreglo", fontsize=14)
    plt.title("Eficiencia Relativa de Algoritmos", fontsize=16, fontweight='bold')
    plt.xticks(range(len(algorithms)), list(algorithms.keys()), rotation=45)
    plt.yticks(range(len(sizes)), [str(size) for size in sizes])
    plt.tight_layout()
    plt.savefig("images/comparison_heatmap.png", dpi=300)
    plt.close()

    # Guardar datos en CSV para análisis posterior
    import csv
    with open("images/sorting_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        # Encabezado
        header = ["Size"] + [f"{name}_mean" for name in algorithms] + [f"{name}_std" for name in algorithms]
        writer.writerow(header)
        # Datos
        for i, size in enumerate(sizes):
            row = [size]
            for name in algorithms:
                row.append(results[name][i])  # Media
            for name in algorithms:
                row.append(std_devs[name][i])  # Desviación estándar
            writer.writerow(row)

    return results, std_devs