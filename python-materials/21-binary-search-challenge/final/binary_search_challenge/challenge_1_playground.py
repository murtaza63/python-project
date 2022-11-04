#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from optparse import Option
from typing import Optional


"""
 # Binary Search Challenge

  ### Challenge 1: Binary search as a free function

  Implement binary search as a free function. You should be able to run:

  ```swift
  array = [1, 2, 10, 43, 55, 60, 150, 1420]
  binary_search_for_value_in_range(10, array) == 2
  ```

"""


def binary_search_for_value_in_range(element: int, collection: list[int], _range: Optional[range] = None) -> Optional[int]:
    if not _range:
        _range = range(0, len(collection))

    if _range.start >= _range.stop:
        return None
    size = _range.stop - _range.start

    middle = _range.start + size // 2
    if collection[middle] == element:
        return middle
    elif collection[middle] > element:
        return binary_search_for_value_in_range(element, collection, range(_range.start, middle))
    else:
        return binary_search_for_value_in_range(element, collection, range(middle + 1, _range.stop))


array = [1, 2, 10, 43, 55, 60, 150, 1420]
print(binary_search_for_value_in_range(10, array) == 2)
