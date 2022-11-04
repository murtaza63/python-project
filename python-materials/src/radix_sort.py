#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from functools import reduce


def radix_sort(array: list[int]) -> list[int]:
    base = 10
    done = False
    digits = 1
    while not done:
        done = True
        buckets: list[list[int]] = [[] for _ in range(base)]
        for number in array:
            remaining_part = number // digits
            digit = remaining_part % base
            print(number, remaining_part, base)
            buckets[digit].append(number)
            if remaining_part > 0:
                done = False
        digits *= base
        # Flatten array
        print(buckets)
        array = reduce(lambda z, y: z + y, buckets)
    return array


if __name__ == "__main__":
    array1 = [88, 410, 1772, 20]
    print(f"Original array: {array1}")
    print(radix_sort(array1))
    # TODO: This is wrong, make it work in place
    print(f"Radix sorted: {array1}")
