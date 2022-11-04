#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from collections.abc import Callable
from typing import Generic, Optional, TypeVar

from heap import Heap

Element = TypeVar("Element")


def sorted_heap(input_heap: Heap) -> list[Element]:
    heap = Heap(input_heap.sort, input_heap.elements.copy())
    for index in range(len(heap.elements) - 1, -1, -1):
        heap.elements[0], heap.elements[index] = heap.elements[index], heap.elements[0]
        heap.sift_down_from_index_upto_size(0, index)
    return heap.elements


if __name__ == "__main__":
    heap = Heap(lambda x, y: x > y, [6, 12, 2, 26, 8, 18, 21, 9, 5])
    print(sorted_heap(heap))
