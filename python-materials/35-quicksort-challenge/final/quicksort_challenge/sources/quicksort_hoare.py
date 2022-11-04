#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.


def partition_hoare(a: list[int], low: int, high: int) -> int:
    array = a
    start = low
    end = high
    i, j = start, end - 1

    while True:
        while array[i] <= array[end] and i < j:
            i += 1

        while array[j] >= array[end] and i < j:
            j -= 1

        if i == j:
            if array[i] <= array[end]:
                i += 1

            array[i], array[end] = array[end], array[i]
            return i
        else:
            array[i], array[j] = array[j], array[i]

    # pivot = a[low]
    # i = low + 1
    # j = high

    # while True:
    #     while i < j and a[i] < pivot:
    #         i += 1

    #     while i < j and a[j] > pivot:
    #         j -= 1

    #     if i < j:
    #         a[i], a[j] = a[j], a[i]
    #     else:
    #         return j


def quicksort_hoare(a: list[int], low: int, high: int) -> None:
    if low < high:
        p = partition_hoare(a, low, high)
        quicksort_hoare(a, low, p - 1)
        quicksort_hoare(a, p + 1, high)


if __name__ == "__main__":
    list1 = [1, 7, 3, 9, 10, 5, 4, 2, 6, 8]
    quicksort_hoare(list1, 0, len(list1) - 1)
    print(list1)

    list2 = [12, 0, 3, 9, 2, 21, 18, 27, 1, 5, 8, -1, 8]
    quicksort_hoare(list2, 0, len(list2) - 1)
    print(list2)
