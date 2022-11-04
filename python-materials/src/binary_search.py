#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Optional


def binary_search_iterative(nums: list, target: int) -> Optional[int]:
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


def binary_search_recursive(nums: list, target: int, low: int = None, high: int = None) -> Optional[int]:
    if not low or not high:
        low, high = 0, len(nums) - 1

    if low > high:
        return None

    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, high)
    else:
        return binary_search_recursive(nums, target, low, mid - 1)


# This is the original
def binary_search_in_range(nums: list, value: int, _range: Optional[range] = None) -> Optional[int]:
    if not _range:
        _range = range(0, len(nums))

    if _range.start >= _range.stop:
        return None
    size = _range.stop - _range.start
    middle = _range.start + size // 2

    if nums[middle] == value:
        return middle
    elif nums[middle] > value:
        return binary_search_in_range(nums, value, range(_range.start, middle))
    else:
        return binary_search_in_range(nums, value, range(middle + 1, _range.stop))
