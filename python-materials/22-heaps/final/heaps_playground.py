#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable
from typing import Generic, Optional, Protocol, TypeVar


class Comparable(Protocol):
    """Protocol for annotating comparable types."""

    @abstractmethod
    def __lt__(self: Element, other: Element) -> bool:
        pass


Element = TypeVar("Element", bound=Comparable)


class Heap(Generic[Element]):
    # elements: list[Element] = []
    # sort: Callable[[Element, Element], bool]

    def __init__(self, sort: Callable[[Element, Element], bool], elements: list[Element] = []):
        self.sort = sort
        self.elements = elements

        if self.elements:
            for i in range(len(elements) // 2 - 1, -1, -1):
                self.sift_down_from_index(i)

    @property
    def is_empty(self) -> bool:
        return len(self.elements) == 0

    @property
    def count(self) -> int:
        return len(self.elements)

    def peek(self) -> Optional[Element]:
        return self.elements[0] if self.elements else None

    def left_child_index_of_parent_at_index(self, index: int) -> int:
        return (2 * index) + 1

    def right_child_index_of_parent_at_index(self, index: int) -> int:
        return (2 * index) + 2

    def parent_index_of_child_at_index(self, index: int) -> int:
        return (index - 1) // 2

    def remove(self) -> Optional[Element]:
        if self.is_empty:
            return None
        self.elements[0], self.elements[self.count - 1] = self.elements[self.count - 1], self.elements[0]
        popped = self.elements.pop()
        self.sift_down_from_index(0)
        return popped

    def sift_down_from_index(self, index: int) -> None:
        parent = index
        while True:
            left = self.left_child_index_of_parent_at_index(parent)
            right = self.right_child_index_of_parent_at_index(parent)
            candidate = parent
            if left < self.count and self.sort(self.elements[left], self.elements[candidate]):
                candidate = left
            if right < len(self.elements) and self.sort(self.elements[right], self.elements[candidate]):
                candidate = right
            if candidate == parent:
                return
            self.elements[parent], self.elements[candidate] = self.elements[candidate], self.elements[parent]
            parent = candidate

    def insert(self, element: Element) -> None:
        self.elements.append(element)
        self.sift_up_from_index(len(self.elements) - 1)

    def sift_up_from_index(self, index: int) -> None:
        child = index
        parent = self.parent_index_of_child_at_index(child)
        while child > 0 and self.sort(self.elements[child], self.elements[parent]):
            self.elements[child], self.elements[parent] = self.elements[parent], self.elements[child]
            child = parent
            parent = self.parent_index_of_child_at_index(child)

    def remove_at_index(self, index: int) -> Optional[Element]:
        if index >= len(self.elements):
            return None  # 1
        if index == len(self.elements) - 1:
            return self.elements.pop()  # 2
        else:
            self.elements[index], self.elements[len(self.elements) - 1] = self.elements[len(self.elements) - 1], self.elements[index]  # 3
            element = self.elements.pop()  # 4
            self.sift_down_from_index(index)  # 5
            self.sift_up_from_index(index)
            return element

    def index_of_element_starting_at_i(self, element: Element, i: int) -> Optional[int]:
        if i >= self.count:
            return None
        if self.sort(element, self.elements[i]):
            return None
        if element == self.elements[i]:
            return i
        if j := self.index_of_element_starting_at_i(element, self.left_child_index_of_parent_at_index(i)):
            return j
        if j := self.index_of_element_starting_at_i(element, self.right_child_index_of_parent_at_index(i)):
            return j
        return None


if __name__ == "__main__":
    unsorted = [1, 12, 3, 4, 1, 6, 8, 7]
    heap = Heap(lambda x, y: x < y, unsorted.copy())
    sorted_array = []
    while not heap.is_empty:
        next_smallest = heap.remove()
        sorted_array.append(next_smallest)
    assert sorted_array == sorted(unsorted)
    print(sorted_array)
    print(sorted(unsorted))
