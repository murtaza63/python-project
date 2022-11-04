#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Optional

#: # Radix Sort Challenges
#: ## Challenge 1: Most significant digit
#:
#: The implementation discussed in the chapter used a *least significant digit*
#: radix sort. Your task is to implement a *most significant digit* radix sort.
#: This sorting behavior is called **lexicographical sorting** and is also used
#: for `str` sorting.
#:
#:  For example:
#:
#: ```swift
#: array = [500, 1345, 13, 459, 44, 999]
#: array.lexicographical_sort()
#: print(array) # outputs [13, 1345, 44, 459, 500, 999]
#: ```


def digits(num: int) -> int:
    count = 0
    while num != 0:
        count += 1
        num //= 10
    return count


def digit_at_position(num: int, position: int) -> Optional[int]:
    if position >= digits(num):
        return None
    corrected_position = float(position + 1)
    while num // int(pow(10.0, corrected_position)) != 0:
        num //= 10
    return num % 10


def max_digits(array: list[int]) -> int:
    return digits(max(array)) or 0


def lexicographical_sort(array: list[int]) -> None:
    array = msd_radix_sorted(array, 0)


def msd_radix_sorted(array: list[int], position: int) -> list[int]:
    if position >= max_digits(array):
        return array

    buckets: list[list[int]] = [[] for _ in range(10)]
    priority_bucket: list[int] = []

    for number in array:
        digit = digit_at_position(number, position)
        if not digit:
            priority_bucket.append(number)
            break
        buckets[digit].append(number)

    result = []
    for bucket in buckets:
        if not bucket:
            continue

    result.extend(msd_radix_sorted(bucket, position + 1))
    priority_bucket.extend(result)

    return priority_bucket


array = [500, 1345, 13, 459, 44, 999]
lexicographical_sort(array)
print(array)  # outputs [13, 1345, 44, 459, 500, 999]

# array2: list[int] = range(10 + 1).map { _ in int.random(in: range(1, 100000 + 1)) }
# array2.lexicographical_sort()
# print(array2)
