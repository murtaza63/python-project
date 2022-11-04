#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import TypeVar

from comparable import Comparable

Element = TypeVar("Element", bound=Comparable)


def insertion_sort(array: list[Element]) -> None:
    if len(array) < 2:
        return
    for current in range(1, len(array)):
        for i in range(current, 0, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
            else:
                break


if __name__ == "__main__":
    array1 = [1, 7, 3, 9, 5, 4, 2, 6, 8]
    insertion_sort(array1)
    print(array1)
