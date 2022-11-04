#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
from quicksort_lomuto import partition_lomuto, quicksort_lomuto


def median_of_three(a: list[int], low: int, high: int) -> int:
    center = (low + high) // 2
    if a[low] > a[center]:
        a[low], a[center] = a[center], a[low]
    if a[low] > a[high]:
        a[low], a[high] = a[high], a[low]
    if a[center] > a[high]:
        a[center], a[high] = a[high], a[center]
    return center


def quicksort_median(a: list[int], low: int, high: int) -> None:
    if low < high:
        pivot_index = median_of_three(a, low, high)
        a[pivot_index], a[high] = a[high], a[pivot_index]
        pivot = partition_lomuto(a, low, high)
        quicksort_lomuto(a, low, pivot - 1)
        quicksort_lomuto(a, pivot + 1, high)


if __name__ == "__main__":
    arrays = [
        [7, 3, 9, 10, 5, 1, 4, 2, 6, 8],
        [12, 0, 3, 9, 2, 21, 18, 27, 1, 5, 8, -1, 8],
    ]

    for unsorted_array in arrays:
        array = unsorted_array.copy()
        quicksort_median(array, 0, len(array) - 1)
        assert array == sorted(unsorted_array)
        print(f"Unsorted: {unsorted_array}\n  Sorted: {array}\n{'-' * 80}")
