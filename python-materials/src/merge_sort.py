#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from __future__ import annotations

from abc import abstractmethod
from typing import Protocol, TypeVar


class Comparable(Protocol):
    """Protocol for annotating comparable types."""

    @abstractmethod
    def __lt__(self: Element, other: Element) -> bool:
        pass


Element = TypeVar("Element", bound=Comparable)


def merge_sort(array: list[Element]) -> list[Element]:
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)


def merge(left: list[Element], right: list[Element]) -> list[Element]:
    left_index = 0
    right_index = 0
    result: list[Element] = []
    while left_index < len(left) and right_index < len(right):
        left_element = left[left_index]
        right_element = right[right_index]
        if left_element < right_element:
            result.append(left_element)
            left_index += 1
        elif left_element > right_element:
            result.append(right_element)
            right_index += 1
        else:
            result.append(left_element)
            left_index += 1
            result.append(right_element)
            right_index += 1
    if left_index < len(left):
        result.extend(left[left_index:])
    if right_index < len(right):
        result.extend(right[right_index:])
    return result


if __name__ == "__main__":
    sorted_array = merge_sort([1, 7, 3, 9, 5, 4, 2, 6, 8])
    print(sorted_array)
