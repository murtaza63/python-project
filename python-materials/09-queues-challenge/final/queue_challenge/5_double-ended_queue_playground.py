#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Generic, Optional, Protocol, TypeVar
from sources.doubly_linked_list import DoublyLinkedList
from enum import Enum

#: dll[Previous](@previous)

"""
 ## 5. float-ended queue

 A doubled-ended queue — a.k.a. a **deque** — is, as its name suggests, a queue where elements
 can be added or removed from the `front` or `back`.

 ### Recall:
 - A queue **(FIFO order)** allows you to add elements to the back and remove from the front.
 - A stack **(LIFO order)** allows you to add elements to the back, and remove from the back.

 Deque can be considered both a queue and a stack at the same time.

 A simple `Deque` protocol has been provided to help you build your data structure. An enum `Direction` has been provided to help describe whether you are adding or removing an element from the front or back of the deque. You can use any data structure you prefer to construct a `Deque`.

 > Note: In **DoubleLinkedList.swift** one additional property and function has been added:
 > 1. A property called `last` has been added to help get the tail element of a double-linked list.
 > 2. A function called `prepend(_:)` has been added to help you add an element to the front of a double-linked list.

"""


class Direction(Enum):
    FRONT = 1
    BACK = 2


Element = TypeVar("Element")


class Deque(Protocol[Element]):
    def is_empty(self) -> bool:
        ...

    def peek(self, direction: Direction) -> Optional[Element]:
        ...

    def enqueue(element: Element, direction: Direction) -> bool:
        ...

    def dequeue(self, direction: Direction) -> Optional[Element]:
        ...


Element = TypeVar("Element")


class DequeDoubleLinkedList(Deque, Generic[Element]):
    def __init__(self):
        self.dll = DoublyLinkedList()

    @property
    def is_empty(self) -> bool:
        self.dll.is_empty

    def peek_from_direction(self, direction: Direction) -> Optional[Element]:
        if direction == Direction.FRONT:
            return self.dll.first.value if self.dll else None
        elif direction == Direction.BACK:
            return self.dll.last.value if self.dll else None
        else:
            return None

    def enqueue_element_to_direction(self, element: Element, direction: Direction) -> bool:
        if direction == Direction.FRONT:

            self.dll.prepend(element)
        elif direction == Direction.BACK:

            self.dll.append(element)
        return True

    def dequeue_from_direction(self, direction: Direction) -> Optional[Element]:
        element: Optional[Element]
        if direction == Direction.FRONT:

            first = self.dll.first if self.dll else None
            if not first:
                return None
            element = self.dll.remove(first)
        elif direction == Direction.BACK:

            last = self.dll.last
            if not last:
                return None
            element = self.dll.remove(last)
        return element

    def __str__(self) -> str:
        return str(self.dll)


deque = DequeDoubleLinkedList[int]()
deque.enqueue_element_to_direction(1, Direction.BACK)
deque.enqueue_element_to_direction(2, Direction.BACK)
deque.enqueue_element_to_direction(3, Direction.BACK)
deque.enqueue_element_to_direction(4, Direction.BACK)

print(deque)

deque.enqueue_element_to_direction(5, Direction.FRONT)

print(deque)

deque.dequeue_from_direction(Direction.BACK)
deque.dequeue_from_direction(Direction.BACK)
deque.dequeue_from_direction(Direction.BACK)
deque.dequeue_from_direction(Direction.FRONT)
deque.dequeue_from_direction(Direction.FRONT)
deque.dequeue_from_direction(Direction.FRONT)

print(deque)

#: dll[Next](@next)
