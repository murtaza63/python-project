#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Generic, Optional, TypeVar

# from node import Node

# mypy: disallow-untyped-defs

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T, next: Optional[Node[T]] = None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        if not next:
            return str(self.value)
        return f"{self.value} -> " + str(self.next)


class LinkedList(Generic[T], Iterable[T]):
    def __init__(self, *values: T) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None

        if values:
            for value in values:
                self.append(value)

    def empty(self) -> bool:
        return self.head is None

    def push(self, value: T) -> None:
        self.head = Node[T](value, next=self.head)

        if self.tail is None:
            self.tail = self.head

    def append(self, value: T) -> None:
        if self.empty():
            self.push(value)
        else:
            assert self.tail is not None
            self.tail.next = Node[T](value)
            self.tail = self.tail.next

    def node_at_index(self, index: int) -> Optional[Node[T]]:
        current_node = self.head
        current_index = 0
        while current_node is not None and current_index < index:
            current_node = current_node.next
            current_index += 1
        return current_node

    def insert_value_after_node(self, value: T, node: Node[T]) -> Node[T]:
        if self.tail == node:
            self.append(value)
            return self.tail
        else:
            node.next = Node[T](value, next=node.next)
            return node.next

    def pop(self) -> Optional[T]:
        value_to_return = None

        if self.head:
            value_to_return = self.head.value
            self.head = self.head.next

        if self.empty():
            self.tail = None

        return value_to_return

    def remove_last(self) -> Optional[T]:
        if not self.head:  # empty list
            return None

        if self.head.next is None:  # single node
            return self.pop()

        prev = self.head
        current = self.head

        while current.next is not None:
            prev, current = current, current.next  # Don't need a temp variable this way
            # next = current.next
            # prev = current
            # current = next

        prev.next = None
        self.tail = prev
        return current.value

    def remove_after_node(self, node: Node[T]) -> Optional[T]:
        if not node.next:
            return None

        node_to_delete = node.next

        if node_to_delete == self.tail:
            self.tail = node

        node.next = node_to_delete.next

        return node_to_delete.value

    def __str__(self) -> str:
        return str(self.head)

    def __iter__(self) -> Iterator[T]:  # Makes something iterable
        return LinkedListIterator(self.head)


class LinkedListIterator(Generic[T]):
    def __init__(self, head: Optional[Node[T]]):
        self.current = head

    def __iter__(self) -> Iterator[T]:
        return self

    def __next__(self) -> T:
        if not self.current:
            raise StopIteration

        value = self.current.value
        self.current = self.current.next
        return value
