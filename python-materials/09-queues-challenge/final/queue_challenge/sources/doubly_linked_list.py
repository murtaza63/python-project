#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.next: Optional[Node] = None
        self.previous: Optional[Node] = None

    def __str__(self):
        return str(self.value)


class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None

    @property
    def is_empty(self) -> bool:
        return self.head is None

    @property
    def first(self) -> Optional[Node[T]]:
        return self.head

    #   //** last and prepent were only in chapter 9
    #    08-queues//projects////Queue.playground//Pages//QueueLinkedList.xcplaygroundpage//Sources//DoublyLinkedList.swift
    #    09-queues-challenge//projects////QueueChallenge.playground//Sources//DoublyLinkedList.swift

    @property
    def last(self) -> Optional[Node]:
        return self.tail

    def prepend(self, value: T):
        new_node = Node(value=value)
        head_node = self.head
        if not head_node:
            self.head = new_node
            self.tail = new_node
            return

        new_node.previous = None
        new_node.next = head_node
        head_node.previous = new_node

        self.head = new_node

    def append(self, value: T) -> None:
        new_node = Node(value=value)

        tail_node = self.tail
        if not tail_node:
            self.head = new_node
            self.tail = new_node
            return

        new_node.previous = tail_node
        tail_node.next = new_node
        self.tail = new_node

    def remove(self, node: Node) -> T:
        prev = node.previous
        next = node.next

        if prev:
            prev.next = next
        else:
            self.head = next

        if next:
            next.previous = prev
        else:
            self.tail = prev

        node.previous = None
        node.next = None

        return node.value

    def __str__(self) -> str:
        string = ""
        current = self.head
        while node := current:
            string += f"{node.value} -> "
            current = node.next
        return string + "end"
