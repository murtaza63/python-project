#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Optional
from sources.heap import Heap

"""
 # Heap Data Structure Challenges
 ## 1. Find the nth Smallest Integer
 Write a function to find the `nth` smallest integer in an unsorted array. For example:
 ```
  integers = [3, 10, 18, 5, 21, 100]
  n = 3
 ```
 If  `n = 3`, the result should be `10`.
"""


def get_nth_smallest_element_in_elements(n: int, elements: list[int]) -> Optional[int]:
    heap = Heap(sort=lambda x, y: x < y, elements=elements)

    current = 1
    while not heap.is_empty:
        element = heap.remove()
        if current == n:
            return element
        current += 1

    return None


elements = [3, 10, 18, 5, 21, 100]
nth_element = get_nth_smallest_element_in_elements(3, elements)
print(nth_element)
