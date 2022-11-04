#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

#: # n² Sorting Challenges
#: ## Challenge 1: Group elements
#: Given a collection of Equatable elements, bring all instances of a given
#: value in the array to the right side of the array.


def right_align_value(array: list[int], value: int) -> None:
    left = 0
    right = len(array) - 1

    while left < right:
        while array[right] == value:
            right -= 1
        while array[left] != value:
            left += 1
        if left >= right:
            return
        array[left], array[right] = array[right], array[left]


array = [3, 4, 134, 3, 5, 6, 3, 5, 6, 1, 0]

right_align_value(array, 3)
print(array)
