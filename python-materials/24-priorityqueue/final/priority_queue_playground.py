#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable
from typing import Generic, Optional, Protocol, TypeVar

from priority_queue.sources.heap import Heap  # TODO: Import this from 22-heaps
from priority_queue.sources.queue_protocol import Queue  # TODO: Import this from src


class Comparable(Protocol):
    """Protocol for annotating comparable types."""

    @abstractmethod
    def __lt__(self: Element, other: Element) -> bool:
        pass


Element = TypeVar("Element", bound=Comparable)


class PriorityQueue(Queue, Generic[Element]):
    def __init__(self, sort: Callable[[Element, Element], bool], elements: list[Element] = []):
        self.heap = Heap(sort=sort, elements=elements)

    @property
    def is_empty(self) -> bool:
        return self.heap.is_empty

    @property
    def peek(self) -> Optional[Element]:
        return self.heap.peek()

    def enqueue(self, element: Element) -> bool:
        self.heap.insert(element)
        return True

    def dequeue(self) -> Optional[Element]:
        return self.heap.remove()


if __name__ == "__main__":
    # unsorted = [1, 12, 3, 4, 1, 6, 8, 7]
    # heap = Heap(lambda x, y: x < y, unsorted.copy())
    # sorted_array = []
    # while not heap.is_empty:
    #     next_smallest = heap.remove()
    #     sorted_array.append(next_smallest)
    # assert sorted_array == sorted(unsorted)
    # print(sorted_array)
    # print(sorted(unsorted))

    priority_queue = PriorityQueue(lambda x, y: x < y, [1, 12, 3, 4, 1, 6, 8, 7])
    while not priority_queue.is_empty:
        print(priority_queue.dequeue())
