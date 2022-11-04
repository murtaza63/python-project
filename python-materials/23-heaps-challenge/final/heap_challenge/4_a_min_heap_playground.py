#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

"""
 ## 4. A Min Optional[Heap]
 Write a function to check if a given array is a min heap.
"""


def left_child_index_of_parent_at_index(index: int) -> int:
    return (2 * index) + 1


def right_child_index_of_parent_at_index(index: int) -> int:
    return (2 * index) + 2


def is_min_heap(elements: list[int]) -> bool:
    if not elements:
        return True

    for i in range(len(elements) // 2 - 1, -1, -1):
        left = left_child_index_of_parent_at_index(i)
        right = right_child_index_of_parent_at_index(i)
        if elements[left] < elements[i]:
            return False

        if right < len(elements) and elements[right] < elements[i]:
            return False

    return True


elements = [1, 3, 12, 5, 10, 18, 21, 6, 8, 11, 15, 100, 20]
print(is_min_heap(elements))
