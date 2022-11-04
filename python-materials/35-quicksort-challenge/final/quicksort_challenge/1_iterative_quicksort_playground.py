#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.


from sources.stack import Stack
from sources.quicksort_lomuto import partition_lomuto

"""
 # Quicksort Challenges
 ## 1. Iterative Quicksort

 Implement Quicksort iteratively. Choose any partition strategy you learned in this chapter.
"""


def quicksort_iterative_lomuto(a: list[int], low: int, high: int) -> None:
    stack = Stack()
    stack.push(low)
    stack.push(high)

    while not stack.is_empty:
        end = stack.pop()
        start = stack.pop()

        if not end or not start:
            continue

        p = partition_lomuto(a, start, end)

        if (p - 1) > start:
            stack.push(start)
            stack.push(p - 1)

        if (p + 1) < end:
            stack.push(p + 1)
            stack.push(end)


# assert False
# TODO: This doesn't work
array = [12, 0, 3, 9, 2, 21, 18, 27, 1, 5, 8, -1, 8]
quicksort_iterative_lomuto(array, 0, len(array) - 1)
print(array)
