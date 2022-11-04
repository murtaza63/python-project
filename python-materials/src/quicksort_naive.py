#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.


def quicksort_naive(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    less = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]

    return quicksort_naive(less) + equal + quicksort_naive(greater)


if __name__ == "__main__":
    array1 = [1, 7, 3, 9, 10, 5, 4, 2, 6, 8]
    sorted_array = quicksort_naive(array1)
    print(sorted_array)
