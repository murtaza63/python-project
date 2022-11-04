#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from collections.abc import Callable
from typing import Generic, Optional, Protocol, TypeVar


"""
 # Priority Queue Challenges
 ## 1. Array-based Priority Queue
 You know how to use a heap to construct a priority queue by conforming
 to the `Queue` protocol. Now construct a priority queue using an `Array`.
"""

Element = TypeVar("Element")


class Queue(Protocol[Element]):
    def enqueue(self, element: Element) -> bool:
        ...

    def dequeue(self) -> Optional[Element]:
        ...

    def is_empty(self) -> bool:
        ...

    def peek(self) -> Optional[Element]:
        ...


class PriorityQueueArray(Queue, Generic[Element]):
    def __init__(self, sort: Callable[[Element, Element], bool], elements: list[Element]):
        self.sort: Callable[[Element, Element], bool] = sort
        self.elements: list[Element] = elements
        # self.elements.sort(by: sort)

    @property
    def is_empty(self) -> bool:
        return bool(self.elements) is False

    @property
    def peek(self) -> Optional[Element]:
        return self.elements[0] if self.elements else None

    def enqueue(self, element: Element) -> bool:
        for index, other_element in enumerate(self.elements):
            if self.sort(element, other_element):
                self.elements.insert(index, element)
                return True
        self.elements.append(element)
        return True

    def dequeue(self) -> Optional[Element]:
        return None if self.is_empty else self.elements.pop(0)

    def __str__(self) -> str:
        return str(self.elements)


priority_queue = PriorityQueueArray(sort=lambda x, y: x < y, elements=[1, 12, 3, 4, 1, 6, 8, 7])
priority_queue.enqueue(5)
priority_queue.enqueue(0)
priority_queue.enqueue(10)
while not priority_queue.is_empty:
    print(priority_queue.dequeue())

# TODO: Fix bug
# assert False
