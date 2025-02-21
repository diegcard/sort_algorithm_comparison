from sort import algorithms
from sort import execution_time_gathering

if __name__ == "__main__":
    minimum_size = 10000
    maximum_size = 15000
    step = 5000
    samples_by_size = 7

    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)
    print("Size | Bubble Sort | Quick Sort | Merge Sort")
    print("-" * 50)
    for row in table:
        print(f"{row[0]:5d} | {row[1]:10d} | {row[2]:10d} | {row[3]:10d}")
