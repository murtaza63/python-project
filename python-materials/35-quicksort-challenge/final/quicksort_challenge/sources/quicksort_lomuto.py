#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.


def partition_lomuto(a: list[int], low: int, high: int) -> int:
    pivot = a[high]
    i = low
    for j in range(low, high):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high] = a[high], a[i]
    return i


def quicksort_lomuto(a: list[int], low: int, high: int) -> None:
    if low < high:
        pivot = partition_lomuto(a, low, high)
        quicksort_lomuto(a, low, pivot - 1)
        quicksort_lomuto(a, pivot + 1, high)


if __name__ == "__main__":
    array = [1, 7, 3, 9, 10, 5, 4, 2, 6, 8]
    quicksort_lomuto(array, 0, len(array) - 1)
    print(array)
