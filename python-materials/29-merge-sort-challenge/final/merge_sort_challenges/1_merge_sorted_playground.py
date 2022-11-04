#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

#:
#: # Merge Sort Challenges
#: ## Challenge 1: Speeding up appends

# Does not apply in python
# size = 1024
# values: list[int] = []
# values.reserve_capacity(size)
# for i in range(size):
#   values.append(i)

#: ## Challenge 2: Merge two sequences


def merge_first_second(first_list: list[int], second_list: list[int]) -> list[int]:
    result: list[int] = []

    i = 0
    j = 0

    while i < len(first_list) and j < len(second_list):
        first = first_list[i]
        second = second_list[j]
        if first < second:
            result.append(first)
            i += 1
        elif second < first:
            result.append(second)
            j += 1
        else:
            result.append(first)
            result.append(second)
            i += 1
            j += 1

    while i < len(first_list):
        result.append(first_list[i])
        i += 1

    while j < len(second_list):
        result.append(second_list[j])
        j += 1

    return result


array1 = [1, 2, 3, 4, 5, 6, 7, 8]
array2 = [1, 3, 4, 5, 5, 6, 7, 7]

merged = merge_first_second(array1, array2)
print(merged)
