#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import TypeVar

from comparable import Comparable

Element = TypeVar("Element", bound=Comparable)


def selection_sort(array: list[Element]) -> None:
    if len(array) < 2:
        return

    for current in range(0, len(array) - 1):
        lowest = current
        for other in range(current + 1, len(array)):
            if array[lowest] > array[other]:
                lowest = other
        if lowest != current:
            array[lowest], array[current] = array[current], array[lowest]


# TODO: Remove this after adding tests
if __name__ == "__main__":
    array1 = [1, 7, 3, 9, 5, 4, 2, 6, 8]
    sorted_array = sorted(array1)
    assert array1 != sorted_array
    selection_sort(array1)
    assert array1 == sorted_array
