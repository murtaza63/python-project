#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Optional


"""
  ### Challenge 2: Searching for a range
  Write a function that searches a **sorted** array and that finds the range of indices for a particular element. For example:

 ```swift
 array = [1, 2, 3, 3, 3, 4, 5, 5]
 find_indices_of_value_in_array(3, array)
 ```

 `find_indices` should return the range `range(2, 5)`, since those are the start and end indices for the value `3`.
"""


"""
  Unoptimized version

 ```
 def find_indices_of_value_in_array(self, value: int, array: list[int]) -> Optional[Range]:
   left_index = array.first_index(of: value)
   if not left_index:
     return None
   right_index = array.last_index(of: value)
   if not right_index:
     return None
   return range(left_index, right_index)
 ```
"""


def find_indices_of_value_in_array(value: int, array: list[int]) -> Optional[range]:
    start_index = start_index_of_value_in_array_with_range(value, array, range(len(array)))
    if not start_index:
        return None
    end_index = end_index_of_value_in_array_with_range(value, array, range(len(array)))
    if not end_index:
        return None
    return range(start_index, end_index)


def start_index_of_value_in_array_with_range(value: int, array: list[int], _range: range) -> Optional[int]:
    middle_index = _range.start + (_range.stop - _range.start) // 2
    if middle_index == 0 or middle_index == len(array) - 1:
        if array[middle_index] == value:
            return middle_index
        else:
            return None

    if array[middle_index] == value:
        if array[middle_index - 1] != value:
            return middle_index
        else:
            return start_index_of_value_in_array_with_range(value, array, range(_range.start, middle_index))
    elif value < array[middle_index]:
        return start_index_of_value_in_array_with_range(value, array, range(_range.start, middle_index))
    else:
        return start_index_of_value_in_array_with_range(value, array, range(middle_index, _range.stop))


def end_index_of_value_in_array_with_range(value: int, array: list[int], _range: range) -> Optional[int]:
    middle_index = _range.start + (_range.stop - _range.start) // 2

    if middle_index == 0 or middle_index == len(array) - 1:
        if array[middle_index] == value:
            return middle_index + 1
        else:
            return None

    if array[middle_index] == value:
        if array[middle_index + 1] != value:
            return middle_index + 1
        else:
            return end_index_of_value_in_array_with_range(value, array, range(middle_index, _range.stop))
    elif value < array[middle_index]:
        return end_index_of_value_in_array_with_range(value, array, range(_range.start, middle_index))
    else:
        return end_index_of_value_in_array_with_range(value, array, range(middle_index, _range.stop))


array = [1, 2, 3, 3, 3, 4, 5, 5]
if indices := find_indices_of_value_in_array(3, array):
    print(indices)
