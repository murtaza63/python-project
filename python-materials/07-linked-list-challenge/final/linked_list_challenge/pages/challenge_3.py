#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import sys
from typing import Optional

sys.path.insert(0, ".")
from src.helpers import example_of
from src.linked_list import LinkedList, Node

"""
 ## Challenge 3: Reverse a linked list

 Create a function that reverses a linked list. You do this by manipulating the nodes so that they’re linked in the other direction.
"""


def reverse_linked_list(linked_list: LinkedList):
    linked_list.tail = linked_list.head

    prev: Optional[Node] = None
    current = linked_list.head

    while current:
        next = current.next
        current.next = prev
        prev, current = current, next

    linked_list.head = prev


with example_of("reversing a list"):
    linked_list = LinkedList[int](1, 2, 3)

    print(f"Original list: {linked_list}")
    reverse_linked_list(linked_list)
    print(f"Reversed list: {linked_list}")
