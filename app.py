from sort.algorithms import bubble_sort, quick_sort, merge_sort, insertion_sort, shell_sort
from sort.execution_time_gathering import compare_and_plot_algorithms, take_execution_time


def run_comparison():
    sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort,
        "Insertion Sort": insertion_sort,
        "Shell Sort": shell_sort,
    }

    compare_and_plot_algorithms(sizes, algorithms)


def run_execution_time_test():
    minimum_size = 10000
    maximum_size = 15000
    step = 5000
    samples_by_size = 7

    table = take_execution_time(minimum_size, maximum_size, step, samples_by_size)

    print("Size | Bubble Sort | Quick Sort | Merge Sort | Insertion Sort | Shell Sort")
    print("-" * 50)
    for row in table:
        print(f"{row[0]:5d} | {row[1]:10d} | {row[2]:10d} | {row[3]:10d} | {row[4]:13d} | {row[5]:9d}")


if __name__ == "__main__":
    run_comparison()
    run_execution_time_test()
