#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

#: ## Challenge 3: Reverse a collection
#: Reverse a collection of elements by hand. Do not rely on the
#: reverse or reversed methods.


def reverse_in_place(array: list[int]) -> None:
    left = 0
    right = len(array) - 1

    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1


array = [1, 2, 3, 4, 5]
reverse_in_place(array)
print(array)
