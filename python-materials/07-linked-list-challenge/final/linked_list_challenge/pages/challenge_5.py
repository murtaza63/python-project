#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import sys
from typing import TypeVar

sys.path.insert(0, ".")
from src.helpers import example_of
from src.linked_list import LinkedList

"""
 ## Challenge 5: Remove all occurrences of a specific element

 Create a function that removes all occurrences of a specific element from a linked list. The implementation is similar to the `remove(at:)` method that you implemented for the linked list.
"""

T = TypeVar("T")


def remove_all_matching_value_from_linked_list(value: T, linked_list: LinkedList) -> None:
    while linked_list.head and linked_list.head.value == value:
        linked_list.head = linked_list.head.next

    prev = linked_list.head
    current = linked_list.head.next

    while current:
        if current.value == value:
            prev.next = current.next
            current = prev.next
            continue

        prev, current = current, current.next

    linked_list.tail = prev


with example_of("deleting 1"):
    linked_list = LinkedList[int](1, 1, 2, 2, 3)
    remove_all_matching_value_from_linked_list(1, linked_list)
    print(linked_list)

with example_of("deleting 2"):
    linked_list = LinkedList[int](1, 1, 2, 2, 3)
    remove_all_matching_value_from_linked_list(2, linked_list)
    print(linked_list)

with example_of("deleting 3"):
    linked_list = LinkedList[int](1, 1, 2, 2, 3)
    remove_all_matching_value_from_linked_list(3, linked_list)
    print(linked_list)
