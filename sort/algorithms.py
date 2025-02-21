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
    n = len(arr)
    arr = arr.copy()

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


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
    if len(arr) <= 1:
        return arr

    arr = arr.copy()
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


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
    if len(arr) <= 1:
        return arr

    arr = arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merges two sorted lists into a single sorted list.

    Time Complexity:
    - O(n) where n is the total number of elements in left and right

    :param left: Left sorted list
    :param right: Right sorted list
    :return: Merged and sorted list
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
