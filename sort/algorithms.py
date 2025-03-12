from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Implements the Bubble Sort algorithm.

    Time Complexity:
    - Worst case: O(n^2)
    - Best case: O(n) (when the list is already sorted)
    - Average case: O(n^2)

    :param arr: List of integers to sort
    :return: New sorted list
    """
    n = len(arr)  # O(1)
    arr = arr.copy()  # O(n)

    for i in range(n):  # O(n)
        for j in range(0, n - i - 1):  # O(n)
            if arr[j] > arr[j + 1]:  # O(1)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # O(1)
    return arr  # O(1)


## Lineal [1,2,4,8,12,45,13]


def quick_sort(arr: List[int]) -> List[int]:
    """
    Implements the Quick Sort algorithm.

    Time Complexity:
    - Worst case: O(n^2) (when the pivot is the smallest or largest element)
    - Best case: O(n log n)
    - Average case: O(n log n)

    :param arr: List of integers to sort
    :return: New sorted list
    """
    if len(arr) <= 1:  # O(1)
        return arr  # O(1)

    arr = arr.copy()  # O(n)
    pivot = arr[len(arr) // 2]  # O(1)
    left = [x for x in arr if x < pivot]  # O(n)
    middle = [x for x in arr if x == pivot]  # O(n)
    right = [x for x in arr if x > pivot]  # O(n)

    return quick_sort(left) + middle + quick_sort(right)  # O(n log n)


## [1,2,4,6,5,2,4]


def merge_sort(arr: List[int]) -> List[int]:
    """
    Implements the Merge Sort algorithm.

    Time Complexity:
    - Worst case: O(n log n)
    - Best case: O(n log n)
    - Average case: O(n log n)

    :param arr: List of integers to sort
    :return: New sorted list
    """
    if len(arr) <= 1:  # O(1)
        return arr  # O(1)

    arr = arr.copy()  # O(n)
    mid = len(arr) // 2  # O(1)
    left = merge_sort(arr[:mid])  # O(n log n)
    right = merge_sort(arr[mid:])  # O(n log n)

    return merge(left, right)  # O(n)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merges two sorted lists into a single sorted list.

    Time Complexity:
    - O(n) where n is the total number of elements in left and right

    :param left: Left sorted list
    :param right: Right sorted list
    :return: Merged and sorted list
    """
    result = []  # O(1)
    i = j = 0  # O(1)

    while i < len(left) and j < len(right):  # O(n)
        if left[i] <= right[j]:  # O(1)
            result.append(left[i])  # O(1)
            i += 1  # O(1)
        else:  # O(1)
            result.append(right[j])  # O(1)
            j += 1  # O(1)

    result.extend(left[i:])  # O(n)
    result.extend(right[j:])  # O(n)
    return result  # O(1)


def insertion_sort(arr: List[int]) -> List[int]:
    """Implements the Insertion Sort algorithm.
    Time Complexity:
    - Worst case: O(n^2) (when the array is reverse sorted)
    - Best case: O(n) (when the array is already sorted)
    - Average case: O(n^2)

    Space Complexity: O(1) - In-place sorting algorithm

    :param arr: List of integers to sort
    :return: New sorted list
    """
    arr = arr.copy()  # O(n)
    for i in range(1, len(arr)):  # O(n)
        key = arr[i]  # O(1)
        j = i - 1  # O(1)
        while j >= 0 and arr[j] > key:  # O(n)
            arr[j + 1] = arr[j]  # O(1)
            j -= 1  # O(1)
        arr[j + 1] = key  # O(1)
    return arr  # O(n)


def shell_sort(arr: List[int]) -> List[int]:
    """Implements the Shell Sort algorithm.
    Time Complexity:
    - Worst case: O(n^2) (depends on gap sequence)
    - Best case: O(n log n)
    - Average case: O(n log n)

    Space Complexity: O(1) - In-place sorting algorithm

    Shell sort is an optimization of insertion sort that allows the exchange of
    items that are far apart. The idea is to arrange the list of elements so that
    starting from anywhere, taking every hth element yields a sorted sequence.

    :param arr: List of integers to sort
    :return: New sorted list
    """
    arr = arr.copy()  # O(n)
    n = len(arr)  # O(1)
    gap = n // 2  # O(1)

    while gap > 0:  # O(log n)
        for i in range(gap, n):  # O(n)
            temp = arr[i]  # O(1)
            j = i  # O(1)
            while j >= gap and arr[j - gap] > temp:  # O(n)
                arr[j] = arr[j - gap]  # O(1)
                j -= gap  # O(1)
            arr[j] = temp  # O(1)
        gap //= 2  # O(1)

    return arr  # O(n)
