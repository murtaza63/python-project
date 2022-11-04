#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Optional


"""
 # Heap Sort Challenges
 ## 1. Add Heap Sort to `Array`

 Add a `heap_sort()` method to Array. This method should sort the array
 in ascending order. A template has been provided for you in the
 starter playground.

"""


def left_child_index_of_parent_at_index(array, index: int) -> int:
    return (2 * index) + 1


def right_child_index_of_parent_at_index(array, index: int) -> int:
    return (2 * index) + 2


def sift_down_from_index_upto_size(array, index: int, size: int) -> None:
    parent = index
    while True:
        left = left_child_index_of_parent_at_index(array, parent)
        right = right_child_index_of_parent_at_index(array, parent)
        candidate = parent

        if (left < size) and (array[left] > array[candidate]):
            candidate = left
        if (right < size) and (array[right] > array[candidate]):
            candidate = right
        if candidate == parent:
            return
        array[parent], array[candidate] = array[candidate], array[parent]
        parent = candidate


def heap_sort(array: list[int]) -> None:
    # Build Heap
    if array:
        for i in range(len(array) // 2 - 1, -1, -1):
            sift_down_from_index_upto_size(array, i, len(array))

    # Perform Heap Sort.
    for index in range(len(array) - 1, -1, -1):
        array[0], array[index] = array[index], array[0]
        sift_down_from_index_upto_size(array, 0, index)


array = [6, 12, 2, 26, 8, 18, 21, 9, 5]
heap_sort(array)
print(f"heap_sort(array): {array}")


"""
 ## 2. Theory
 When performing a heap sort in ascending order, which of these starting
 arrays requires the fewest Optional[comparisons]
 - `[1,2,3,4,5]`
 - `[5,4,3,2,1]`
"""

# `[5,4,3,2,1]` will yield the fewest number of comparisons, since it’s
# already a max heap and no swaps take place.


"""
 ## 3. Descending Order
 The chapter implementation of heap sort, sorts the elements in ascending order.
 How would you sort in descending Optional[order]
"""

# Simply use a min heap instead of a max heap before sorting:
# let heap = Heap(sort: <, elements: [6, 12, 2, 26, 8, 18, 21, 9, 5])
# print(sorted(heap))
