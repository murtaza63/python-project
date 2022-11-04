#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys
from typing import TypeVar

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from comparable import Comparable

Element = TypeVar("Element", bound=Comparable)


def bubble_sort(array: list[Element]) -> None:
    if len(array) < 2:
        return

    for end in range(len(array) - 1, -1, -1):
        swapped = False
        for i in range(end):
            # TODO: Unsupported left operand type for > ("Element")mypy(error)
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if not swapped:
            return


if __name__ == "__main__":
    array1 = [1, 7, 3, 9, 5, 4, 2, 6, 8]
    bubble_sort(array1)
    print(array1)
