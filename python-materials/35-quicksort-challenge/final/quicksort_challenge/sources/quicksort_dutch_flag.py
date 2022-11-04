#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Tuple


def partition_dutch_flag(a: list[int], low: int, high: int, pivot_index: int) -> Tuple[int, int]:
    pivot = a[pivot_index]
    smaller = low
    equal = low
    larger = high
    while equal <= larger:
        if a[equal] < pivot:
            a[smaller], a[equal] = a[equal], a[smaller]
            smaller += 1
            equal += 1
        elif a[equal] == pivot:
            equal += 1
        else:
            a[equal], a[larger] = a[larger], a[equal]
            larger -= 1
    return (smaller, larger)


def quicksort_dutch_flag(a: list[int], low: int, high: int) -> None:
    if low < high:
        (middle_first, middle_last) = partition_dutch_flag(a, low, high, high)
        quicksort_dutch_flag(a, low, middle_first - 1)
        quicksort_dutch_flag(a, middle_last + 1, high)


if __name__ == "__main__":
    array = [1, 7, 3, 9, 10, 5, 4, 2, 6, 8]
    quicksort_dutch_flag(array, 0, len(array) - 1)
    print(array)
